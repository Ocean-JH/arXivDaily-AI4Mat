"""Render the public AI4Mat static-site artifacts from normalized paper data."""

from __future__ import annotations

import datetime as dt
import email.utils
import html
import json
import logging
import math
import re
import xml.etree.ElementTree as ET
from collections.abc import Sequence
from pathlib import Path
from typing import Any


LOGGER = logging.getLogger("arxiv-tracker")
SITE_BASE_URL = "https://ocean-jh.github.io/arXivDaily-AI4Mat/"
LEGACY_ARCHIVE_PAGE_FILE = re.compile(r"archive-(?P<number>[1-9]\d*)\.html\Z")
NUMBERED_ARCHIVE_PAGE_FILE = re.compile(
    r"page-(?P<number>(?:[2-9]|[1-9]\d+))\.html\Z"
)


def _html(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def _json_text(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def paper_anchor(base_id: str) -> str:
    safe = re.sub(r"[^A-Za-z0-9_.-]+", "-", base_id).strip("-")
    return f"paper-{safe or 'unknown'}"


class SiteRenderer:
    """Build paginated HTML, search data, feeds, and site health metadata."""

    def __init__(
        self,
        *,
        root_dir: Path,
        templates_dir: Path,
        archive_page_size: int,
    ) -> None:
        self.root_dir = root_dir
        self.templates_dir = templates_dir
        self.archive_page_size = archive_page_size
        self._template_cache: tuple[str, str] | None = None

    def _templates(self) -> tuple[str, str]:
        if self._template_cache is None:
            self._template_cache = (
                (self.templates_dir / "base.html").read_text(encoding="utf-8"),
                (self.templates_dir / "paper_item.html").read_text(encoding="utf-8"),
            )
        return self._template_cache

    @staticmethod
    def _paper_badge(status: str) -> str:
        if status == "new":
            return '<span class="paper-badge">New</span>'
        if status == "update":
            return '<span class="paper-badge updated">Updated</span>'
        return ""

    def render_paper(
        self,
        paper: dict[str, Any],
        index: int,
        *,
        show_badge: bool = True,
    ) -> str:
        published_date = paper.get("published", "")[:10]
        status = paper.get("status", "") if show_badge else ""
        _, paper_template = self._templates()
        return paper_template.format(
            anchor=_html(paper_anchor(paper["base_id"])),
            base_id=_html(paper["base_id"]),
            index=index,
            title=_html(paper["title"]),
            authors=_html(", ".join(paper["authors"])),
            published_iso=_html(published_date),
            published_date=_html(published_date),
            category=_html(paper["primary_category"]),
            paper_id=_html(paper["short_id"]),
            url=_html(paper["url"]),
            summary=_html(paper["summary"]),
            tag=self._paper_badge(status),
        )

    @staticmethod
    def _navbar(page_type: str, site_root: str) -> str:
        latest_current = ' aria-current="page"' if page_type == "latest" else ""
        archive_current = ' aria-current="page"' if page_type == "archive" else ""
        return (
            '<nav class="nav" aria-label="Primary navigation">'
            f'<a href="{site_root}index.html"{latest_current}>Latest</a>'
            f'<a href="{site_root}archive.html"{archive_current}>Archive</a>'
            "</nav>"
        )

    def _base_document(
        self,
        *,
        content: str,
        page_type: str,
        page_file: str,
        title: str,
        description: str,
        timestamp: dt.datetime,
        status_notice: str = "",
    ) -> str:
        canonical_url = SITE_BASE_URL + ("" if page_file == "index.html" else page_file)
        site_root = "../" if "/" in page_file else ""
        base_template, _ = self._templates()
        return base_template.format(
            title=_html(title),
            description=_html(description),
            canonical_url=_html(canonical_url),
            rss_url=_html(SITE_BASE_URL + "feed.xml"),
            og_title=_html(title),
            og_description=_html(description),
            page_type=_html(page_type),
            site_root=site_root,
            archive_search_index_url=f"{site_root}data/archive-search-index.json",
            navbar=self._navbar(page_type, site_root),
            status_notice=status_notice,
            content=content,
            timestamp_iso=_html(timestamp.isoformat()),
            timestamp=_html(timestamp.strftime("%Y-%m-%d %H:%M:%S SGT")),
            current_year=timestamp.year,
        )

    def _latest_content(
        self,
        papers: Sequence[dict[str, Any]],
        checked_at: dt.datetime,
    ) -> str:
        parts = [
            f'<div class="section-heading"><h2 id="latest-papers">Latest papers ({len(papers)})</h2>',
            f"<p>Checked {_html(checked_at.strftime('%Y-%m-%d %H:%M SGT'))}</p></div>",
        ]
        if papers:
            parts.extend(
                self.render_paper(paper, index)
                for index, paper in enumerate(papers, 1)
            )
        else:
            parts.append('<div class="notice">No tracked papers are available yet.</div>')
        return "\n".join(parts)

    def _index_document(
        self,
        papers: Sequence[dict[str, Any]],
        *,
        checked_at: dt.datetime,
        new_count: int,
        build_only: bool,
    ) -> str:
        if build_only:
            message = "Showing the most recent saved additions."
        elif new_count:
            noun = "paper" if new_count == 1 else "papers"
            message = f"<strong>{new_count} new {noun}</strong> found in the latest check."
        elif papers:
            message = "No new papers in the latest check. Showing the most recent additions."
        else:
            message = "No papers have been tracked yet."
        return self._base_document(
            content=self._latest_content(papers, checked_at),
            page_type="latest",
            page_file="index.html",
            title="AI4Mat Research Monitor — Latest Papers",
            description=(
                "The latest arXiv research connecting artificial intelligence, "
                "materials discovery, inverse design, and crystal structure prediction."
            ),
            timestamp=checked_at,
            status_notice=f"<p>{message}</p>",
        )

    @staticmethod
    def _archive_filename(page: int) -> str:
        return "archive.html" if page == 1 else f"archive/page-{page}.html"

    def _archive_page_href(self, page: int, current_page: int) -> str:
        filename = self._archive_filename(page)
        if current_page == 1:
            return filename
        return "../archive.html" if page == 1 else Path(filename).name

    def _archive_pagination(self, current_page: int, total_pages: int) -> str:
        if total_pages <= 1:
            return ""

        visible = {1, total_pages}
        visible.update(
            range(max(1, current_page - 2), min(total_pages, current_page + 2) + 1)
        )
        parts = ['<nav class="archive-pagination" aria-label="Archive pages">']
        if current_page > 1:
            parts.append(
                f'<a href="{self._archive_page_href(current_page - 1, current_page)}" '
                'rel="prev">← Previous</a>'
            )

        previous = 0
        for page in sorted(visible):
            if previous and page - previous > 1:
                parts.append('<span class="pagination-ellipsis" aria-hidden="true">…</span>')
            if page == current_page:
                parts.append(
                    f'<span aria-current="page" aria-label="Page {page}">{page}</span>'
                )
            else:
                parts.append(
                    f'<a href="{self._archive_page_href(page, current_page)}" '
                    f'aria-label="Page {page}">{page}</a>'
                )
            previous = page

        if current_page < total_pages:
            parts.append(
                f'<a href="{self._archive_page_href(current_page + 1, current_page)}" '
                'rel="next">Next →</a>'
            )
        parts.append("</nav>")
        return "\n".join(parts)

    def _archive_documents(
        self,
        papers: Sequence[dict[str, Any]],
        *,
        content_updated_at: dt.datetime,
    ) -> dict[Path, str]:
        total_pages = max(1, math.ceil(len(papers) / self.archive_page_size))
        documents: dict[Path, str] = {}
        for page in range(1, total_pages + 1):
            start = (page - 1) * self.archive_page_size
            page_papers = papers[start : start + self.archive_page_size]
            content = [
                '<div class="section-heading">',
                '<h2 id="archive-papers">Paper archive</h2>',
                f"<p>Page {page} of {total_pages} · {len(papers)} unique papers</p></div>",
            ]
            if page_papers:
                content.extend(
                    self.render_paper(
                        paper,
                        start + offset,
                        show_badge=False,
                    )
                    for offset, paper in enumerate(page_papers, 1)
                )
            else:
                content.append('<div class="notice">The archive is empty.</div>')
            content.append(self._archive_pagination(page, total_pages))

            filename = self._archive_filename(page)
            documents[self.root_dir / filename] = self._base_document(
                content="\n".join(content),
                page_type="archive",
                page_file=filename,
                title=f"AI4Mat Research Monitor — Archive page {page}",
                description=(
                    f"Browse page {page} of the AI4Mat arXiv research archive, "
                    "covering machine learning and materials science."
                ),
                timestamp=content_updated_at,
            )
        return documents

    def _archive_search_index(
        self,
        papers: Sequence[dict[str, Any]],
        *,
        generated_at: dt.datetime,
    ) -> dict[str, Any]:
        indexed_papers = [
            {
                "id": paper["short_id"],
                "base_id": paper["base_id"],
                "title": paper["title"],
                "authors": paper["authors"],
                "categories": paper["categories"],
                "primary_category": paper["primary_category"],
                "summary": paper["summary"],
                "published": paper["published"],
                "page": position // self.archive_page_size + 1,
                "anchor": paper_anchor(paper["base_id"]),
            }
            for position, paper in enumerate(papers)
        ]
        return {
            "generated_at": generated_at.isoformat(),
            "total": len(indexed_papers),
            "papers": indexed_papers,
        }

    @staticmethod
    def _feed_document(
        papers: Sequence[dict[str, Any]],
        *,
        content_updated_at: dt.datetime,
    ) -> str:
        rss = ET.Element("rss", version="2.0")
        channel = ET.SubElement(rss, "channel")
        ET.SubElement(channel, "title").text = "AI4Mat Research Monitor"
        ET.SubElement(channel, "link").text = SITE_BASE_URL
        ET.SubElement(channel, "description").text = (
            "Recent arXiv papers on artificial intelligence for materials science."
        )
        ET.SubElement(channel, "language").text = "en"
        ET.SubElement(channel, "lastBuildDate").text = email.utils.format_datetime(
            content_updated_at
        )

        for paper in papers[:50]:
            item = ET.SubElement(channel, "item")
            ET.SubElement(item, "title").text = paper["title"]
            ET.SubElement(item, "link").text = paper["url"]
            guid = ET.SubElement(item, "guid", isPermaLink="true")
            guid.text = paper["url"]
            try:
                published = dt.datetime.fromisoformat(paper["published"])
                if published.tzinfo is None:
                    published = published.replace(tzinfo=dt.timezone.utc)
                ET.SubElement(item, "pubDate").text = email.utils.format_datetime(published)
            except ValueError:
                pass
            ET.SubElement(item, "description").text = paper["summary"]

        ET.indent(rss, space="  ")
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(
            rss,
            encoding="unicode",
        ) + "\n"

    def _sitemap_document(
        self,
        archive_pages: int,
        *,
        content_updated_at: dt.datetime,
    ) -> str:
        namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
        ET.register_namespace("", namespace)
        root = ET.Element(f"{{{namespace}}}urlset")
        last_modified = content_updated_at.date().isoformat()
        filenames = [
            "",
            *(self._archive_filename(page) for page in range(1, archive_pages + 1)),
        ]
        for filename in filenames:
            url = ET.SubElement(root, f"{{{namespace}}}url")
            ET.SubElement(url, f"{{{namespace}}}loc").text = SITE_BASE_URL + filename
            ET.SubElement(url, f"{{{namespace}}}lastmod").text = last_modified

        ET.indent(root, space="  ")
        return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(
            root,
            encoding="unicode",
        ) + "\n"

    def site_outputs(
        self,
        *,
        latest_papers: Sequence[dict[str, Any]],
        all_papers: Sequence[dict[str, Any]],
        checked_at: dt.datetime,
        content_updated_at: dt.datetime,
        new_count: int,
        build_only: bool,
    ) -> tuple[dict[Path, str], set[Path]]:
        archive_documents = self._archive_documents(
            all_papers,
            content_updated_at=content_updated_at,
        )
        archive_pages = len(archive_documents)
        outputs = {
            self.root_dir / "index.html": self._index_document(
                latest_papers,
                checked_at=checked_at,
                new_count=new_count,
                build_only=build_only,
            ),
            **archive_documents,
            self.root_dir / "data/archive-search-index.json": _json_text(
                self._archive_search_index(
                    all_papers,
                    generated_at=content_updated_at,
                )
            ),
            self.root_dir / "feed.xml": self._feed_document(
                all_papers,
                content_updated_at=content_updated_at,
            ),
            self.root_dir / "sitemap.xml": self._sitemap_document(
                archive_pages,
                content_updated_at=content_updated_at,
            ),
            self.root_dir / "site-status.json": _json_text(
                {
                    "status": "ok",
                    "generated_at": checked_at.isoformat(),
                    "new_papers_count": new_count,
                    "latest_batch_count": len(latest_papers),
                    "total_papers": len(all_papers),
                    "archive_pages": archive_pages,
                }
            ),
        }
        return outputs, set(archive_documents)

    def remove_stale_archive_pages(self, desired: set[Path]) -> None:
        candidates = [
            *self.root_dir.glob("archive-*.html"),
            *self.root_dir.glob("archive/page-*.html"),
        ]
        for path in candidates:
            is_generated_archive = (
                LEGACY_ARCHIVE_PAGE_FILE.fullmatch(path.name)
                or NUMBERED_ARCHIVE_PAGE_FILE.fullmatch(path.name)
            )
            if is_generated_archive and path not in desired:
                path.unlink()
                LOGGER.info("Removed stale archive page: %s", path.name)
