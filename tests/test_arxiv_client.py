"""Exercise the pinned arxiv parser and pagination using mocked HTTP responses."""

import datetime as dt
from email.utils import format_datetime
from urllib.parse import parse_qs, urlsplit

import arxiv
import pytest
import requests

import arxiv_client
from arxiv_client import BackoffClient


def response(status=200, *, retry_after=None, ids=(), total=None):
    result = requests.Response()
    result.status_code = status
    if retry_after is not None:
        result.headers["Retry-After"] = retry_after
    entries = "".join(
        f"""<entry>
          <id>https://arxiv.org/abs/{paper_id}</id><title>Test paper</title>
          <link href="https://arxiv.org/abs/{paper_id}" rel="alternate"/>
          <published>2026-09-22T15:02:50Z</published><updated>2026-09-22T15:02:50Z</updated>
          <summary>Test abstract</summary><author><name>Test author</name></author>
          <arxiv:primary_category term="cond-mat.mtrl-sci"/>
          <category term="cond-mat.mtrl-sci"/>
        </entry>"""
        for paper_id in ids
    )
    result._content = f"""<feed xmlns="http://www.w3.org/2005/Atom"
        xmlns:arxiv="http://arxiv.org/schemas/atom"
        xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">
        <opensearch:totalResults>{len(ids) if total is None else total}</opensearch:totalResults>
        {entries}</feed>""".encode()
    return result


def mock_client(monkeypatch, responses, **settings):
    pending = iter(responses)
    calls, sleeps = [], []

    def get(_session, url, **kwargs):
        calls.append((url, kwargs))
        item = next(pending)
        if isinstance(item, Exception):
            raise item
        return item

    monkeypatch.setattr(requests.Session, "get", get)
    monkeypatch.setattr(arxiv_client.time, "sleep", sleeps.append)
    monkeypatch.setattr(arxiv_client.random, "uniform", lambda _start, _end: 0)
    client = BackoffClient(**{
        "page_size": 500, "delay_seconds": 10, "num_retries": 5, **settings,
    })
    return client, calls, sleeps


def search(client, max_results=500):
    return list(client.results(arxiv.Search(query="all:materials", max_results=max_results)))


def test_429_backs_off_then_recovers_without_duplicate_retries(monkeypatch):
    client, calls, sleeps = mock_client(monkeypatch, [
        response(429), response(429), response(ids=["2609.26547v1"]),
    ])

    assert [p.get_short_id() for p in search(client)] == ["2609.26547v1"]
    assert sleeps == [60, 120]
    assert len(calls) == 3
    assert len({url for url, _ in calls}) == 1
    assert all(kwargs["timeout"] == (10, 60) for _, kwargs in calls)


@pytest.mark.parametrize("header, expected", [("180", 180), ("600", 600), ("bad", 60)])
def test_retry_after_is_respected_even_above_backoff_cap(monkeypatch, header, expected):
    client, _, sleeps = mock_client(monkeypatch, [response(429, retry_after=header), response()])
    assert search(client) == []
    assert sleeps == [expected]


def test_retry_after_http_date(monkeypatch):
    header = format_datetime(dt.datetime.now(dt.timezone.utc) + dt.timedelta(seconds=180))
    client, _, sleeps = mock_client(monkeypatch, [response(503, retry_after=header), response()])
    search(client)
    assert 178 <= sleeps[0] <= 180


def test_network_failure_does_not_reuse_previous_retry_after(monkeypatch):
    client, _, sleeps = mock_client(monkeypatch, [
        response(429, retry_after="180"), requests.exceptions.Timeout(), response(),
    ])
    search(client)
    assert sleeps == [180, 120]


def test_excessive_retry_after_stops_without_an_early_retry(monkeypatch):
    client, calls, sleeps = mock_client(monkeypatch, [response(429, retry_after="3600")])
    with pytest.raises(arxiv.HTTPError):
        search(client)
    assert len(calls) == 1
    assert sleeps == []


def test_wait_budget_bounds_persistent_failures(monkeypatch):
    client, calls, sleeps = mock_client(monkeypatch, [response(429)] * 6)
    with pytest.raises(arxiv.HTTPError):
        search(client)
    assert len(calls) == 5
    assert sleeps == [60, 120, 240, 300]


def test_retry_count_is_bounded(monkeypatch):
    client, calls, sleeps = mock_client(monkeypatch, [response(503)] * 3, num_retries=2)
    with pytest.raises(arxiv.HTTPError):
        search(client)
    assert len(calls) == 3
    assert sleeps == [60, 120]


def test_zero_retries_means_one_attempt(monkeypatch):
    client, calls, sleeps = mock_client(monkeypatch, [response(429)], num_retries=0)
    with pytest.raises(arxiv.HTTPError):
        search(client)
    assert len(calls) == 1
    assert sleeps == []


@pytest.mark.parametrize("status", [400, 401, 403, 404])
def test_permanent_errors_are_not_retried(monkeypatch, status):
    client, calls, sleeps = mock_client(monkeypatch, [response(status)])
    with pytest.raises(arxiv.HTTPError):
        search(client)
    assert len(calls) == 1
    assert sleeps == []


@pytest.mark.parametrize("failure", [
    response(408), response(500), response(502), response(503),
    requests.exceptions.Timeout("timed out"),
    requests.exceptions.ConnectionError("connection reset"),
])
def test_transient_failures_recover(monkeypatch, failure):
    client, calls, sleeps = mock_client(monkeypatch, [failure, response()])
    assert search(client) == []
    assert len(calls) == 2
    assert sleeps == [60]


@pytest.mark.parametrize("failure", [response(429), response(total=2)])
def test_retry_later_page_does_not_refetch_previous_page(monkeypatch, failure):
    client, calls, sleeps = mock_client(monkeypatch, [
        response(ids=["2609.26547v1"], total=2), failure,
        response(ids=["2609.26548v1"], total=2),
    ], page_size=1)
    assert [p.get_short_id() for p in search(client, 2)] == ["2609.26547v1", "2609.26548v1"]
    assert [parse_qs(urlsplit(url).query)["start"] for url, _ in calls] == [["0"], ["1"], ["1"]]
    assert 9 <= sleeps[0] <= 10  # Normal pacing between successful pages.
    assert sleeps[1:] == [60]


def test_jitter_never_reduces_backoff(monkeypatch):
    client, _, sleeps = mock_client(monkeypatch, [response(429), response()])
    monkeypatch.setattr(arxiv_client.random, "uniform", lambda _start, end: end)
    search(client)
    assert sleeps == [66]
