"""Paced arXiv requests with bounded retries for temporary failures."""

from __future__ import annotations

import datetime as dt
import logging
import random
import time
from email.utils import parsedate_to_datetime

import arxiv
import requests


LOGGER = logging.getLogger("arxiv-tracker")
TRANSIENT_HTTP_STATUSES = {408, 429}


class _Session(requests.Session):
    """Keep Retry-After available when arxiv.py converts a response to an error."""

    retry_after: str | None = None

    def get(self, url, **kwargs):
        self.retry_after = None
        kwargs.setdefault("timeout", (10, 60))
        response = super().get(url, **kwargs)
        self.retry_after = response.headers.get("Retry-After")
        return response


def _retry_after_seconds(value: str | None) -> float:
    if not value:
        return 0.0
    if value.strip().isdigit():
        return float(value)
    try:
        deadline = parsedate_to_datetime(value)
        if deadline.tzinfo is None:
            deadline = deadline.replace(tzinfo=dt.timezone.utc)
        return max(0.0, (deadline - dt.datetime.now(dt.timezone.utc)).total_seconds())
    except (TypeError, ValueError, OverflowError):
        return 0.0


class BackoffClient(arxiv.Client):
    """Retry the failed page, preserving arxiv.py's parsing and pagination.

    The _parse_feed and _session integration is specific to pinned arxiv==2.2.0.
    Native retries are disabled so retries do not multiply across layers.
    """

    def __init__(
        self,
        *,
        page_size: int,
        delay_seconds: float,
        num_retries: int,
        retry_backoff_seconds: float = 60.0,
        retry_max_seconds: float = 300.0,
    ) -> None:
        super().__init__(page_size=page_size, delay_seconds=delay_seconds, num_retries=0)
        self._session.close()
        self._session = _Session()
        self._page_retries = num_retries
        self._retry_backoff_seconds = retry_backoff_seconds
        self._retry_max_seconds = retry_max_seconds
        # Shared across pages, keeping repeated outages within the CI time budget.
        self._retry_wait_remaining = 900.0

    def _parse_feed(self, url: str, first_page: bool = True, _try_index: int = 0):
        backoff = self._retry_backoff_seconds
        for attempt in range(self._page_retries + 1):
            try:
                return super()._parse_feed(url, first_page=first_page)
            except (
                arxiv.HTTPError,
                arxiv.UnexpectedEmptyPageError,
                requests.exceptions.ConnectionError,
                requests.exceptions.Timeout,
            ) as error:
                if isinstance(error, arxiv.HTTPError):
                    if error.status not in TRANSIENT_HTTP_STATUSES and error.status < 500:
                        raise
                if attempt == self._page_retries:
                    raise

                delay = min(
                    self._retry_max_seconds,
                    backoff + random.uniform(0, min(10.0, backoff * 0.1)),
                )
                delay = max(
                    delay,
                    self.delay_seconds,
                    _retry_after_seconds(self._session.retry_after),
                )
                if delay > self._retry_wait_remaining:
                    # Never shorten the server's cooldown to fit our wait budget.
                    LOGGER.warning("arXiv retry wait budget exhausted; stopping the search")
                    raise
                LOGGER.warning(
                    "Temporary arXiv failure (%s); retrying the same page in %.1fs (%d/%d)",
                    error, delay, attempt + 1, self._page_retries,
                )
                time.sleep(delay)
                self._retry_wait_remaining -= delay
                backoff = min(backoff * 2, self._retry_max_seconds)
                # Also pace attempts that failed before a response was received.
                self._last_request_dt = None
