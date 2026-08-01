from __future__ import annotations

import datetime as dt
import importlib.util
import json
import shutil
import sys
import types
from pathlib import Path

import pytest


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))


if importlib.util.find_spec("arxiv") is None:
    arxiv_stub = types.ModuleType("arxiv")

    class _Client:
        def __init__(self, **_kwargs):
            pass

    class _Search:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

    class _SortCriterion:
        LastUpdatedDate = "last-updated"

    class _SortOrder:
        Descending = "descending"

    arxiv_stub.Client = _Client
    arxiv_stub.Result = object
    arxiv_stub.Search = _Search
    arxiv_stub.SortCriterion = _SortCriterion
    arxiv_stub.SortOrder = _SortOrder
    sys.modules["arxiv"] = arxiv_stub


from arxiv_tracker import ArxivTracker, SGT  # noqa: E402


NOW = dt.datetime(2026, 8, 1, 9, 30, tzinfo=SGT)


class FakeClient:
    def __init__(self, results=(), error: Exception | None = None):
        self._results = list(results)
        self._error = error

    def results(self, _search):
        if self._error:
            raise self._error
        return iter(self._results)


class FakeResult:
    def __init__(
        self,
        short_id: str,
        title: str,
        *,
        entry_id: str | None = None,
        published_day: int = 1,
    ) -> None:
        self._short_id = short_id
        self.entry_id = entry_id or f"http://arxiv.org/abs/{short_id}"
        self.pdf_url = f"http://arxiv.org/pdf/{short_id}"
        self.title = title
        self.authors = ["Ada Researcher", "Lin Scientist"]
        self.summary = f"Abstract for {title}."
        self.published = dt.datetime(2026, 7, published_day, tzinfo=dt.timezone.utc)
        self.updated = self.published
        self.categories = ["cond-mat.mtrl-sci", "cs.LG"]
        self.primary_category = "cond-mat.mtrl-sci"
        self.comment = None
        self.journal_ref = None
        self.doi = None

    def get_short_id(self) -> str:
        return self._short_id


def make_project(tmp_path: Path, *, page_size: int = 40, client=None) -> ArxivTracker:
    shutil.copytree(REPOSITORY_ROOT / "templates", tmp_path / "templates")
    (tmp_path / "data/results").mkdir(parents=True)
    (tmp_path / "data/known_papers.json").write_text("{}\n", encoding="utf-8")
    (tmp_path / "README.md").write_text(
        "# Test monitor\n\n<!-- ARXIV_PAPERS_START -->\n<!-- ARXIV_PAPERS_END -->\n",
        encoding="utf-8",
    )
    return ArxivTracker(
        query="all:materials",
        max_results=20,
        output_dir="data/results",
        known_papers_file="data/known_papers.json",
        templates_dir="templates",
        root_dir=tmp_path,
        archive_page_size=page_size,
        client=client or FakeClient(),
        now_provider=lambda: NOW,
    )


def stored_record(tracker: ArxivTracker, short_id: str, title: str, day: int) -> dict:
    return tracker.paper_to_dict(
        FakeResult(short_id, title, published_day=day),
        status="new",
    )


def write_results(tracker: ArxivTracker, records: list[dict]) -> Path:
    path = tracker.output_dir / "arxiv_results_20260730_065715.json"
    path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def test_version_parsing_preserves_legacy_category_ids(tmp_path: Path) -> None:
    tracker = make_project(tmp_path)

    assert tracker._extract_short_id(
        "https://arxiv.org/abs/cond-mat/0603304v2"
    ) == "cond-mat/0603304v2"
    assert tracker._get_base_id("cond-mat/0603304v2") == "cond-mat/0603304"
    assert tracker._get_version("cond-mat/0603304v2") == 2


def test_first_seen_v2_is_new_and_uses_safe_https_url(tmp_path: Path) -> None:
    paper = FakeResult(
        "2607.00001v2",
        "A first-seen revision",
        entry_id="javascript:alert(1)",
    )
    tracker = make_project(tmp_path)

    records = tracker.filter_new_papers([paper])

    assert records[0]["status"] == "new"
    assert records[0]["url"] == "https://arxiv.org/abs/2607.00001v2"
    rendered = tracker.renderer.render_paper(records[0], 1)
    assert ">New<" in rendered
    assert ">Updated<" not in rendered
    assert "javascript:" not in rendered


def test_existing_paper_revision_is_marked_updated(tmp_path: Path) -> None:
    tracker = make_project(tmp_path)
    tracker.known_papers["2607.00001"] = 1

    records = tracker.filter_new_papers(
        [FakeResult("2607.00001v2", "A revised paper")]
    )

    assert records[0]["status"] == "update"
    assert ">Updated<" in tracker.renderer.render_paper(records[0], 1)


def test_build_splits_archive_and_creates_search_feed_and_status(tmp_path: Path) -> None:
    tracker = make_project(tmp_path, page_size=2)
    records = [
        stored_record(tracker, "2607.00003v1", "Newest paper", 3),
        stored_record(tracker, "2607.00002v1", "Middle paper", 2),
        stored_record(tracker, "2607.00001v1", "Oldest paper", 1),
    ]
    write_results(tracker, records)
    stale_page = tmp_path / "archive/page-3.html"
    stale_page.parent.mkdir()
    stale_page.write_text("stale", encoding="utf-8")
    legacy_page = tmp_path / "archive-9.html"
    legacy_page.write_text("legacy", encoding="utf-8")

    tracker.build_from_saved(checked_at=NOW, update_readme=False)

    first_page = (tmp_path / "archive.html").read_text(encoding="utf-8")
    second_page = (tmp_path / "archive/page-2.html").read_text(encoding="utf-8")
    assert first_page.count('<article class="paper"') == 2
    assert second_page.count('<article class="paper"') == 1
    assert 'href="archive/page-2.html"' in first_page
    assert 'href="../archive.html"' in second_page
    assert 'src="../static/js/search.js"' in second_page
    assert not stale_page.exists()
    assert not legacy_page.exists()

    search_index = json.loads(
        (tmp_path / "data/archive-search-index.json").read_text(encoding="utf-8")
    )
    assert search_index["total"] == 3
    assert [paper["page"] for paper in search_index["papers"]] == [1, 1, 2]
    assert search_index["papers"][0]["anchor"] == "paper-2607.00003"

    status = json.loads((tmp_path / "site-status.json").read_text(encoding="utf-8"))
    assert status == {
        "archive_pages": 2,
        "generated_at": NOW.isoformat(),
        "latest_batch_count": 3,
        "new_papers_count": 0,
        "status": "ok",
        "total_papers": 3,
    }
    assert "Newest paper" in (tmp_path / "feed.xml").read_text(encoding="utf-8")
    assert "archive/page-2.html" in (
        tmp_path / "sitemap.xml"
    ).read_text(encoding="utf-8")


def test_empty_run_keeps_latest_batch_on_homepage(tmp_path: Path) -> None:
    tracker = make_project(tmp_path, client=FakeClient())
    record = stored_record(tracker, "2607.00001v1", "Still useful", 1)
    write_results(tracker, [record])
    known_path = tmp_path / "data/known_papers.json"
    known_path.write_text('{"2607.00001": 1}\n', encoding="utf-8")
    tracker.known_papers = tracker._load_known_papers()

    new_papers = tracker.run()

    assert new_papers == []
    homepage = (tmp_path / "index.html").read_text(encoding="utf-8")
    assert "Still useful" in homepage
    assert "No new papers in the latest check" in homepage
    assert len(list(tracker.output_dir.glob("arxiv_results_*.json"))) == 1
    assert known_path.read_text(encoding="utf-8") == '{"2607.00001": 1}\n'


def test_api_failure_propagates_and_does_not_publish(tmp_path: Path) -> None:
    tracker = make_project(
        tmp_path,
        client=FakeClient(error=RuntimeError("arXiv unavailable")),
    )

    with pytest.raises(RuntimeError, match="arXiv unavailable"):
        tracker.run()

    assert not (tmp_path / "index.html").exists()
    assert not (tmp_path / "site-status.json").exists()


def test_render_failure_does_not_advance_durable_known_state(tmp_path: Path) -> None:
    tracker = make_project(
        tmp_path,
        client=FakeClient([FakeResult("2607.00001v1", "New paper")]),
    )
    (tmp_path / "templates/base.html").unlink()
    known_path = tmp_path / "data/known_papers.json"

    with pytest.raises(FileNotFoundError):
        tracker.run()

    assert known_path.read_text(encoding="utf-8") == "{}\n"
    assert list(tracker.output_dir.glob("arxiv_results_*.json")) == []


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"query": ""}, "query"),
        ({"query": "x", "max_results": 0}, "max_results"),
        ({"query": "x", "archive_page_size": 0}, "archive_page_size"),
    ],
)
def test_configuration_validation(tmp_path: Path, kwargs: dict, message: str) -> None:
    shutil.copytree(REPOSITORY_ROOT / "templates", tmp_path / "templates")

    with pytest.raises(ValueError, match=message):
        ArxivTracker(
            output_dir=tmp_path / "results",
            known_papers_file=tmp_path / "known.json",
            templates_dir=tmp_path / "templates",
            **kwargs,
        )
