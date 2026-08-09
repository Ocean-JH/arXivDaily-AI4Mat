#!/usr/bin/env python3
"""Fetch arXiv papers and publish the static AI4Mat research monitor."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import logging
import os
import re
import tempfile
from collections.abc import Callable, Iterable, Sequence
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlsplit

from site_renderer import SiteRenderer

try:
    import arxiv
except ModuleNotFoundError:  # Build-only mode does not need the API dependency.
    arxiv = None  # type: ignore[assignment]


LOGGER = logging.getLogger("arxiv-tracker")
SGT = dt.timezone(dt.timedelta(hours=8), name="SGT")
README_START = "<!-- ARXIV_PAPERS_START -->"
README_END = "<!-- ARXIV_PAPERS_END -->"
VERSIONED_ARXIV_ID = re.compile(r"^(?P<base>.+?)v(?P<version>\d+)$")
SAFE_ARXIV_ID = re.compile(r"^[A-Za-z0-9./-]+(?:v\d+)?$")
ALLOWED_ARXIV_HOSTS = {"arxiv.org", "www.arxiv.org", "export.arxiv.org"}
TRANSIENT_ARXIV_HTTP_STATUSES = {408, 429}
_arxiv_error = getattr(arxiv, "ArxivError", None)
ARXIV_ERROR_TYPES = (_arxiv_error,) if isinstance(_arxiv_error, type) else ()


def _json_text(value: Any, *, indent: int | None = 2) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        indent=indent,
        sort_keys=indent is not None,
    ) + "\n"


def _atomic_write_text(path: Path, content: str) -> bool:
    """Atomically replace *path* when its UTF-8 content has changed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return False

    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            dir=path.parent,
            prefix=f".{path.name}.",
            suffix=".tmp",
            delete=False,
        ) as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
            temporary_path = Path(handle.name)
        os.replace(temporary_path, path)
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise
    return True


class ArxivTracker:
    """Version-aware arXiv ingestion and static-site generation."""

    def __init__(
        self,
        query: str,
        max_results: int = 200,
        output_dir: str | Path = "./data/results",
        known_papers_file: str | Path = "./data/known_papers.json",
        templates_dir: str | Path = "./templates",
        *,
        root_dir: str | Path = ".",
        archive_page_size: int = 40,
        arxiv_page_size: int = 100,
        arxiv_delay_seconds: float = 10.0,
        arxiv_num_retries: int = 5,
        client: Any | None = None,
        now_provider: Callable[[], dt.datetime] | None = None,
    ) -> None:
        query = str(query).strip()
        if not query:
            raise ValueError("query must not be empty")
        if isinstance(max_results, bool) or int(max_results) <= 0:
            raise ValueError("max_results must be a positive integer")
        if isinstance(archive_page_size, bool) or int(archive_page_size) <= 0:
            raise ValueError("archive_page_size must be a positive integer")
        if isinstance(arxiv_page_size, bool) or int(arxiv_page_size) <= 0:
            raise ValueError("arxiv_page_size must be a positive integer")
        if isinstance(arxiv_delay_seconds, bool) or float(arxiv_delay_seconds) <= 0:
            raise ValueError("arxiv_delay_seconds must be a positive number")
        if isinstance(arxiv_num_retries, bool) or int(arxiv_num_retries) < 0:
            raise ValueError("arxiv_num_retries must be a non-negative integer")

        self.query = query
        self.max_results = int(max_results)
        self.archive_page_size = int(archive_page_size)
        self.arxiv_page_size = int(arxiv_page_size)
        self.arxiv_delay_seconds = float(arxiv_delay_seconds)
        self.arxiv_num_retries = int(arxiv_num_retries)
        self.root_dir = Path(root_dir).resolve()
        self.output_dir = self._resolve(output_dir)
        self.known_papers_file = self._resolve(known_papers_file)
        self.templates_dir = self._resolve(templates_dir)
        self.now_provider = now_provider or (lambda: dt.datetime.now(SGT))

        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.known_papers_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.templates_dir.is_dir():
            raise FileNotFoundError(f"Template directory not found: {self.templates_dir}")

        self.known_papers = self._load_known_papers()
        self.client = client
        self.renderer = SiteRenderer(
            root_dir=self.root_dir,
            templates_dir=self.templates_dir,
            archive_page_size=self.archive_page_size,
        )

    def _resolve(self, path: str | Path) -> Path:
        candidate = Path(path)
        return candidate if candidate.is_absolute() else self.root_dir / candidate

    def _now(self) -> dt.datetime:
        value = self.now_provider()
        if value.tzinfo is None:
            raise ValueError("now_provider must return a timezone-aware datetime")
        return value.astimezone(SGT)

    def _load_known_papers(self) -> dict[str, int]:
        if not self.known_papers_file.exists():
            return {}
        with self.known_papers_file.open(encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, dict):
            raise ValueError("known_papers_file must contain a JSON object")

        known: dict[str, int] = {}
        for paper_id, version in data.items():
            parsed_version = int(version)
            if parsed_version < 1:
                raise ValueError(f"Invalid known-paper version for {paper_id!r}")
            known[str(paper_id)] = parsed_version
        return known

    def _save_known_papers(self) -> None:
        _atomic_write_text(
            self.known_papers_file,
            json.dumps(self.known_papers, ensure_ascii=False, sort_keys=True) + "\n",
        )

    def search_papers(self) -> list[arxiv.Result]:
        if arxiv is None:
            raise RuntimeError(
                "The arxiv package is required for live searches. "
                "Install requirements.txt or use --build-only."
            )
        client = self.client or arxiv.Client(
            page_size=self.arxiv_page_size,
            delay_seconds=self.arxiv_delay_seconds,
            num_retries=self.arxiv_num_retries,
        )
        search = arxiv.Search(
            query=self.query,
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.LastUpdatedDate,
            sort_order=arxiv.SortOrder.Descending,
        )
        return list(client.results(search))

    @staticmethod
    def _get_base_id(short_id: str) -> str:
        match = VERSIONED_ARXIV_ID.match(str(short_id))
        return match.group("base") if match else str(short_id)

    @staticmethod
    def _get_version(short_id: str) -> int:
        match = VERSIONED_ARXIV_ID.match(str(short_id))
        return int(match.group("version")) if match else 1

    @staticmethod
    def _extract_short_id(value: Any) -> str:
        text = str(value or "").strip().rstrip("/")
        if not text:
            return ""

        parsed = urlsplit(text)
        if parsed.scheme or parsed.netloc:
            path = parsed.path.rstrip("/")
            for marker in ("/abs/", "/pdf/"):
                if marker in path:
                    short_id = path.split(marker, 1)[1]
                    return short_id.removesuffix(".pdf")
            return path.rsplit("/", 1)[-1].removesuffix(".pdf")
        return text.removesuffix(".pdf")

    def _paper_base_id(self, paper: dict[str, Any]) -> str:
        base_id = str(paper.get("base_id") or "").strip()
        if base_id:
            return base_id
        short_id = self._extract_short_id(paper.get("short_id") or paper.get("id") or paper.get("url"))
        return self._get_base_id(short_id)

    def _paper_version(self, paper: dict[str, Any]) -> int:
        try:
            version = int(paper.get("version", 0))
            if version > 0:
                return version
        except (TypeError, ValueError):
            pass
        short_id = self._extract_short_id(paper.get("short_id") or paper.get("id") or paper.get("url"))
        return self._get_version(short_id)

    def _paper_short_id(self, paper: dict[str, Any]) -> str:
        return f"{self._paper_base_id(paper)}v{self._paper_version(paper)}"

    @staticmethod
    def _markdown(value: Any) -> str:
        return (
            str(value or "")
            .replace("\\", "\\\\")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace("\r", " ")
            .replace("\n", " ")
            .strip()
        )

    @staticmethod
    def _clean_list(value: Any) -> list[str]:
        if value is None:
            return []
        values = value if isinstance(value, list) else [value]
        return [str(item).strip() for item in values if str(item).strip()]

    def _normalize_arxiv_url(
        self,
        value: Any,
        short_id: str,
        *,
        endpoint: str,
    ) -> str:
        if not SAFE_ARXIV_ID.fullmatch(short_id):
            raise ValueError(f"Unsafe arXiv identifier: {short_id!r}")

        parsed = urlsplit(str(value or "").strip())
        expected_prefix = f"/{endpoint}/"
        if (
            parsed.hostname
            and parsed.hostname.lower() in ALLOWED_ARXIV_HOSTS
            and parsed.path.startswith(expected_prefix)
        ):
            normalized_path = parsed.path.removesuffix(".pdf") if endpoint == "abs" else parsed.path
            return f"https://arxiv.org{quote(normalized_path, safe='/.-')}"

        suffix = ".pdf" if endpoint == "pdf" else ""
        return f"https://arxiv.org/{endpoint}/{quote(short_id, safe='/.-')}{suffix}"

    def _normalize_saved_paper(self, paper: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(paper, dict):
            raise ValueError("Each saved paper must be a JSON object")

        base_id = self._paper_base_id(paper)
        version = self._paper_version(paper)
        short_id = f"{base_id}v{version}"
        title = str(paper.get("title") or "").strip()
        if not base_id or not title:
            raise ValueError("Saved papers require base_id and title")

        status = str(paper.get("status") or paper.get("tag") or "").lower()
        if status == "updated":
            status = "update"
        if status not in {"new", "update"}:
            status = ""

        return {
            "id": self._normalize_arxiv_url(
                paper.get("url") or paper.get("id"),
                short_id,
                endpoint="abs",
            ),
            "short_id": short_id,
            "base_id": base_id,
            "version": version,
            "title": title,
            "authors": self._clean_list(paper.get("authors")),
            "summary": str(paper.get("summary") or "").strip(),
            "published": str(paper.get("published") or ""),
            "updated": str(paper.get("updated") or paper.get("published") or ""),
            "categories": self._clean_list(paper.get("categories")),
            "primary_category": str(paper.get("primary_category") or ""),
            "comment": paper.get("comment"),
            "journal_ref": paper.get("journal_ref"),
            "doi": paper.get("doi"),
            "pdf_url": self._normalize_arxiv_url(
                paper.get("pdf_url"),
                short_id,
                endpoint="pdf",
            ),
            "url": self._normalize_arxiv_url(
                paper.get("url") or paper.get("id"),
                short_id,
                endpoint="abs",
            ),
            "status": status,
        }

    def paper_to_dict(self, paper: arxiv.Result, *, status: str = "") -> dict[str, Any]:
        short_id = paper.get_short_id()
        raw = {
            "id": paper.entry_id,
            "short_id": short_id,
            "base_id": self._get_base_id(short_id),
            "version": self._get_version(short_id),
            "title": paper.title,
            "authors": [str(author) for author in paper.authors],
            "summary": paper.summary,
            "published": paper.published.isoformat(),
            "updated": paper.updated.isoformat(),
            "categories": list(paper.categories),
            "primary_category": paper.primary_category,
            "comment": paper.comment,
            "journal_ref": paper.journal_ref,
            "doi": paper.doi,
            "pdf_url": paper.pdf_url,
            "url": paper.entry_id,
            "status": status,
        }
        return self._normalize_saved_paper(raw)

    def filter_new_papers(self, papers: Sequence[arxiv.Result]) -> list[dict[str, Any]]:
        latest_results: dict[str, arxiv.Result] = {}
        for paper in papers:
            short_id = paper.get_short_id()
            base_id = self._get_base_id(short_id)
            current = latest_results.get(base_id)
            if current is None or self._get_version(short_id) > self._get_version(current.get_short_id()):
                latest_results[base_id] = paper

        new_papers: list[dict[str, Any]] = []
        for base_id, paper in latest_results.items():
            version = self._get_version(paper.get_short_id())
            previous_version = self.known_papers.get(base_id, 0)
            if version <= previous_version:
                continue
            status = "new" if previous_version == 0 else "update"
            new_papers.append(self.paper_to_dict(paper, status=status))
            self.known_papers[base_id] = version
        return new_papers

    @staticmethod
    def _is_transient_arxiv_error(error: Exception) -> bool:
        if arxiv is None:
            return False

        http_error = getattr(arxiv, "HTTPError", None)
        if isinstance(http_error, type) and isinstance(error, http_error):
            status = int(getattr(error, "status", 0))
            return status in TRANSIENT_ARXIV_HTTP_STATUSES or status >= 500

        empty_page_error = getattr(arxiv, "UnexpectedEmptyPageError", None)
        return isinstance(empty_page_error, type) and isinstance(error, empty_page_error)

    def run_with_api_fallback(
        self,
        update_readme: bool = True,
    ) -> list[dict[str, Any]]:
        """Run ingestion, rebuilding saved data if arXiv is temporarily unavailable."""
        try:
            return self.run(update_readme=update_readme)
        except ARXIV_ERROR_TYPES as error:
            if not self._is_transient_arxiv_error(error) or not self._result_files():
                raise
            LOGGER.warning(
                "arXiv remained unavailable after retries (%s); "
                "rebuilding from the most recent saved results",
                error,
            )
            # Preserve the README's last successful check timestamp.
            return self.build_from_saved(update_readme=False)

    def _dedupe_papers(self, papers: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
        latest: dict[str, dict[str, Any]] = {}
        for raw_paper in papers:
            paper = self._normalize_saved_paper(raw_paper)
            base_id = paper["base_id"]
            current = latest.get(base_id)
            if current is None or (
                paper["version"],
                paper.get("updated", ""),
            ) > (
                current["version"],
                current.get("updated", ""),
            ):
                latest[base_id] = paper
        return list(latest.values())

    def _result_files(self) -> list[Path]:
        return sorted(self.output_dir.glob("arxiv_results_*.json"))

    def _load_result_file(self, path: Path) -> list[dict[str, Any]]:
        with path.open(encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, list):
            raise ValueError(f"Result file must contain a JSON array: {path}")
        return [self._normalize_saved_paper(paper) for paper in data]

    def load_all_saved_papers(self) -> list[dict[str, Any]]:
        papers: list[dict[str, Any]] = []
        for path in self._result_files():
            papers.extend(self._load_result_file(path))
        deduped = self._dedupe_papers(papers)
        deduped.sort(
            key=lambda paper: (paper.get("published", ""), paper.get("updated", "")),
            reverse=True,
        )
        return deduped

    def load_latest_batch(self) -> list[dict[str, Any]]:
        for path in reversed(self._result_files()):
            papers = self._load_result_file(path)
            if papers:
                return papers
        return []

    def _content_updated_at(self, fallback: dt.datetime) -> dt.datetime:
        files = self._result_files()
        if not files:
            return fallback
        match = re.search(r"(\d{8}_\d{6})", files[-1].stem)
        if not match:
            return fallback
        return dt.datetime.strptime(match.group(1), "%Y%m%d_%H%M%S").replace(tzinfo=SGT)

    def save_results(
        self,
        papers: Sequence[dict[str, Any]],
        timestamp: str,
    ) -> Path | None:
        if not papers:
            return None
        path = self.output_dir / f"arxiv_results_{timestamp}.json"
        _atomic_write_text(path, _json_text(list(papers)))
        return path

    def generate_markdown(
        self,
        papers: Sequence[dict[str, Any]],
        *,
        checked_at: dt.datetime,
        new_count: int,
    ) -> str:
        heading = "New Papers" if new_count else "Latest Papers"
        lines = [f"## {heading} ({len(papers)})", ""]
        if not new_count and papers:
            lines.extend(
                [
                    "_No new papers were found in the latest check; showing the most recent additions._",
                    "",
                ]
            )
        lines.extend(
            [
                f"*Last checked: {checked_at:%Y-%m-%d %H:%M:%S} (SGT)*",
                "",
            ]
        )

        if not papers:
            lines.extend(["No tracked papers are available yet.", ""])
            return "\n".join(lines)

        for index, paper in enumerate(papers, start=1):
            lines.extend(
                [
                    f"### {index}. {self._markdown(paper['title'])}",
                    "",
                    f"**Authors:** {self._markdown(', '.join(paper['authors']))}",
                    "",
                    f"**Published:** {self._markdown(paper['published'][:10])}",
                    "",
                    f"**Category:** {self._markdown(paper['primary_category'])}",
                    "",
                    f"**ID:** {self._markdown(paper['short_id'])}",
                    "",
                    f"**Link:** [{paper['url']}]({paper['url']})",
                    "",
                    f"**Summary:** {self._markdown(paper['summary'])}",
                    "",
                    "---",
                    "",
                ]
            )
        return "\n".join(lines)

    def _updated_readme_content(
        self,
        papers: Sequence[dict[str, Any]],
        *,
        checked_at: dt.datetime,
        new_count: int,
        path: Path,
    ) -> str:
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        generated = self.generate_markdown(
            papers,
            checked_at=checked_at,
            new_count=new_count,
        )
        section = f"{README_START}\n\n{generated}\n{README_END}"
        if README_START in existing and README_END in existing:
            start = existing.index(README_START)
            end = existing.index(README_END, start) + len(README_END)
            return existing[:start] + section + existing[end:]
        separator = "\n\n" if existing else ""
        return existing.rstrip() + separator + section + "\n"

    def update_readme(
        self,
        papers: Sequence[dict[str, Any]],
        readme_path: str | Path = "README.md",
        *,
        checked_at: dt.datetime | None = None,
        new_count: int | None = None,
    ) -> None:
        path = self._resolve(readme_path)
        timestamp = checked_at or self._now()
        count = len(papers) if new_count is None else new_count
        _atomic_write_text(
            path,
            self._updated_readme_content(
                papers,
                checked_at=timestamp,
                new_count=count,
                path=path,
            ),
        )

    def build_from_saved(
        self,
        *,
        checked_at: dt.datetime | None = None,
        update_readme: bool = True,
    ) -> list[dict[str, Any]]:
        timestamp = checked_at or self._now()
        all_papers = self.load_all_saved_papers()
        latest_papers = self.load_latest_batch()
        content_updated_at = self._content_updated_at(timestamp)
        outputs, desired_archives = self.renderer.site_outputs(
            latest_papers=latest_papers,
            all_papers=all_papers,
            checked_at=timestamp,
            content_updated_at=content_updated_at,
            new_count=0,
            build_only=True,
        )
        if update_readme:
            readme_path = self.root_dir / "README.md"
            outputs[readme_path] = self._updated_readme_content(
                latest_papers,
                checked_at=timestamp,
                new_count=0,
                path=readme_path,
            )
        for path, content in outputs.items():
            _atomic_write_text(path, content)
        self.renderer.remove_stale_archive_pages(desired_archives)
        return latest_papers

    def run(
        self,
        update_readme: bool = True,
        create_html: bool = True,
    ) -> list[dict[str, Any]]:
        checked_at = self._now()
        timestamp = checked_at.strftime("%Y%m%d_%H%M%S")
        LOGGER.info("Searching arXiv for: %s", self.query)

        results = self.search_papers()
        LOGGER.info("Found %d matching arXiv results", len(results))
        new_papers = self.filter_new_papers(results)
        LOGGER.info("Found %d new or updated papers", len(new_papers))

        saved_papers = self.load_all_saved_papers()
        all_papers = self._dedupe_papers([*saved_papers, *new_papers])
        all_papers.sort(
            key=lambda paper: (paper.get("published", ""), paper.get("updated", "")),
            reverse=True,
        )
        latest_papers = new_papers or self.load_latest_batch()
        content_updated_at = checked_at if new_papers else self._content_updated_at(checked_at)

        outputs: dict[Path, str] = {}
        desired_archives: set[Path] = set()
        if update_readme:
            readme_path = self.root_dir / "README.md"
            outputs[readme_path] = self._updated_readme_content(
                latest_papers,
                checked_at=checked_at,
                new_count=len(new_papers),
                path=readme_path,
            )
        if create_html:
            site_outputs, desired_archives = self.renderer.site_outputs(
                latest_papers=latest_papers,
                all_papers=all_papers,
                checked_at=checked_at,
                content_updated_at=content_updated_at,
                new_count=len(new_papers),
                build_only=False,
            )
            outputs.update(site_outputs)

        # All rendering and validation above completes before durable state changes.
        if new_papers:
            self.save_results(new_papers, timestamp)
        for path, content in outputs.items():
            _atomic_write_text(path, content)
        if create_html:
            self.renderer.remove_stale_archive_pages(desired_archives)
        if new_papers:
            self._save_known_papers()
        return new_papers


DEFAULT_CONFIG: dict[str, Any] = {
    "query": (
        '(cat:cond-mat.mtrl-sci OR cat:cs.AI OR cat:cs.LG) AND '
        '(all:"materials design" OR all:"materials discovery" OR all:"inverse design") AND '
        '(all:"generative" OR all:"crystal structure prediction")'
    ),
    "max_results": 500,
    "output_dir": "./data/results",
    "known_papers_file": "./data/known_papers.json",
    "templates_dir": "./templates",
    "archive_page_size": 40,
    "arxiv_page_size": 100,
    "arxiv_delay_seconds": 10.0,
    "arxiv_num_retries": 5,
}


def _load_config(path: Path) -> dict[str, Any]:
    config = dict(DEFAULT_CONFIG)
    if not path.exists():
        return config
    with path.open(encoding="utf-8") as handle:
        loaded = json.load(handle)
    if not isinstance(loaded, dict):
        raise ValueError("Configuration must contain a JSON object")
    config.update(loaded)
    return config


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("config.json"))
    parser.add_argument("--query", help="Search query (overrides config)")
    parser.add_argument("--max-results", type=int, help="Maximum results (overrides config)")
    parser.add_argument("--no-readme", action="store_true", help="Do not update README")
    parser.add_argument(
        "--build-only",
        action="store_true",
        help="Regenerate the static site from saved result files without contacting arXiv",
    )
    args = parser.parse_args()

    config = _load_config(args.config)
    if args.query is not None:
        config["query"] = args.query
    if args.max_results is not None:
        config["max_results"] = args.max_results

    tracker = ArxivTracker(
        query=config["query"],
        max_results=config["max_results"],
        output_dir=config["output_dir"],
        known_papers_file=config["known_papers_file"],
        templates_dir=config.get("templates_dir", "./templates"),
        archive_page_size=config.get("archive_page_size", 40),
        arxiv_page_size=config.get("arxiv_page_size", 100),
        arxiv_delay_seconds=config.get("arxiv_delay_seconds", 10.0),
        arxiv_num_retries=config.get("arxiv_num_retries", 5),
    )
    if args.build_only:
        tracker.build_from_saved(update_readme=not args.no_readme)
    else:
        tracker.run_with_api_fallback(update_readme=not args.no_readme)
    return 0


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    raise SystemExit(main())
