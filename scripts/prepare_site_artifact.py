#!/usr/bin/env python3
"""Validate and assemble the allowlisted GitHub Pages artifact."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


NUMBERED_ARCHIVE_PAGE = re.compile(
    r"page-(?P<number>(?:[2-9]|[1-9]\d+))\.html\Z"
)
LEGACY_ARCHIVE_PAGE = re.compile(r"archive-[1-9]\d*\.html\Z")
PUBLIC_ROOT_FILES = (
    "404.html",
    "CNAME",
    "atom.xml",
    "feed.xml",
    "robots.txt",
    "rss.xml",
    "sitemap.xml",
)
REQUIRED_STATUS_FIELDS = {
    "status",
    "generated_at",
    "new_papers_count",
    "latest_batch_count",
    "total_papers",
    "archive_pages",
}


class SiteValidationError(RuntimeError):
    """Raised when generated site files are unsafe or incomplete."""


class DocumentInspector(HTMLParser):
    """Collect the small amount of structure needed for a static-site check."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.doctype_seen = False
        self.start_tags: dict[str, int] = {}
        self.end_tags: dict[str, int] = {}
        self.ids: set[str] = set()
        self.duplicate_ids: set[str] = set()
        self.local_references: list[str] = []

    def handle_decl(self, decl: str) -> None:
        if decl.strip().lower() == "doctype html":
            self.doctype_seen = True

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        self.start_tags[tag] = self.start_tags.get(tag, 0) + 1
        attributes = dict(attrs)

        element_id = attributes.get("id")
        if element_id:
            if element_id in self.ids:
                self.duplicate_ids.add(element_id)
            self.ids.add(element_id)

        for name in ("href", "src"):
            reference = attributes.get(name)
            if reference:
                self.local_references.append(reference)

    def handle_endtag(self, tag: str) -> None:
        self.end_tags[tag] = self.end_tags.get(tag, 0) + 1


def _archive_sort_key(path: Path) -> tuple[int, str]:
    if path.name == "archive.html":
        return (1, path.name)
    match = NUMBERED_ARCHIVE_PAGE.fullmatch(path.name)
    if not match:
        return (sys.maxsize, path.name)
    return (int(match.group("number")), path.name)


def _site_html_files(source: Path) -> list[Path]:
    index = source / "index.html"
    archive = source / "archive.html"
    missing = [
        str(path.relative_to(source))
        for path in (index, archive)
        if not path.is_file()
    ]
    if missing:
        raise SiteValidationError(
            f"Missing required generated HTML: {', '.join(missing)}"
        )

    legacy_pages = [
        path for path in source.glob("archive-*.html")
        if LEGACY_ARCHIVE_PAGE.fullmatch(path.name)
    ]
    if legacy_pages:
        names = ", ".join(sorted(path.name for path in legacy_pages))
        raise SiteValidationError(
            f"Legacy archive pages must be moved under archive/: {names}"
        )

    archive_candidates = list((source / "archive").glob("page-*.html"))
    invalid_pages = [
        path for path in archive_candidates
        if not NUMBERED_ARCHIVE_PAGE.fullmatch(path.name)
    ]
    if invalid_pages:
        names = ", ".join(sorted(path.name for path in invalid_pages))
        raise SiteValidationError(f"Invalid numbered archive pages: {names}")

    numbered_pages = sorted(archive_candidates, key=_archive_sort_key)
    page_numbers = [
        int(NUMBERED_ARCHIVE_PAGE.fullmatch(path.name).group("number"))
        for path in numbered_pages
    ]
    expected_numbers = list(range(2, len(numbered_pages) + 2))
    if page_numbers != expected_numbers:
        raise SiteValidationError(
            "Numbered archive pages must be contiguous from page 2"
        )
    return [index, archive, *numbered_pages]


def _resolve_local_reference(
    source: Path,
    document: Path,
    reference: str,
) -> Path | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "//", "/")):
        return None

    relative = unquote(parsed.path)
    if not relative:
        return None

    candidate = (document.parent / relative).resolve()
    try:
        candidate.relative_to(source)
    except ValueError as exc:
        raise SiteValidationError(
            f"Local reference escapes the site root: {reference!r}"
        ) from exc
    return candidate


def _validate_html(source: Path, path: Path) -> None:
    inspector = DocumentInspector()
    try:
        inspector.feed(path.read_text(encoding="utf-8"))
        inspector.close()
    except (OSError, UnicodeError) as exc:
        raise SiteValidationError(f"Cannot read {path.name}: {exc}") from exc

    problems: list[str] = []
    if not inspector.doctype_seen:
        problems.append("missing <!DOCTYPE html>")
    for tag in ("html", "head", "title", "body"):
        if inspector.start_tags.get(tag) != 1:
            problems.append(f"expected one <{tag}> element")
    for tag in ("html", "head", "title", "body"):
        if inspector.end_tags.get(tag) != 1:
            problems.append(f"expected one </{tag}> element")
    if inspector.duplicate_ids:
        problems.append(
            f"duplicate IDs: {', '.join(sorted(inspector.duplicate_ids))}"
        )

    missing_references: list[str] = []
    for reference in inspector.local_references:
        target = _resolve_local_reference(source, path, reference)
        if target is not None and not target.exists():
            missing_references.append(reference)
    if missing_references:
        problems.append(
            f"missing local references: {', '.join(sorted(set(missing_references)))}"
        )

    if problems:
        raise SiteValidationError(f"{path.name}: {'; '.join(problems)}")


def _load_json(path: Path) -> object:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise SiteValidationError(f"Invalid JSON in {path}: {exc}") from exc


def _validate_status(path: Path) -> dict[str, object]:
    status = _load_json(path)
    if not isinstance(status, dict):
        raise SiteValidationError("site-status.json must contain a JSON object")

    missing = REQUIRED_STATUS_FIELDS.difference(status)
    if missing:
        raise SiteValidationError(
            f"site-status.json is missing: {', '.join(sorted(missing))}"
        )
    if status["status"] != "ok":
        raise SiteValidationError("site-status.json status must be 'ok'")

    try:
        generated_at = datetime.fromisoformat(str(status["generated_at"]))
    except ValueError as exc:
        raise SiteValidationError(
            "site-status.json generated_at must be an ISO 8601 timestamp"
        ) from exc
    if generated_at.tzinfo is None:
        raise SiteValidationError(
            "site-status.json generated_at must include a UTC offset"
        )

    for field in (
        "new_papers_count",
        "latest_batch_count",
        "total_papers",
        "archive_pages",
    ):
        value = status[field]
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise SiteValidationError(
                f"site-status.json {field} must be a non-negative integer"
            )
    if status["archive_pages"] < 1:
        raise SiteValidationError(
            "site-status.json archive_pages must be at least one"
        )
    return status


def validate_site(source: Path, *, require_deploy_files: bool) -> list[Path]:
    """Validate generated HTML and, for deployment, its data dependencies."""
    source = source.resolve()
    if not source.is_dir():
        raise SiteValidationError(f"Site source does not exist: {source}")

    html_files = _site_html_files(source)
    for path in html_files:
        _validate_html(source, path)

    static_dir = source / "static"
    if not static_dir.is_dir():
        raise SiteValidationError("Missing required static/ directory")

    search_index = source / "data" / "archive-search-index.json"
    status_file = source / "site-status.json"
    status: dict[str, object] | None = None
    if require_deploy_files:
        for path in (search_index, status_file):
            if not path.is_file():
                raise SiteValidationError(
                    f"Missing required deployment file: {path.relative_to(source)}"
                )
        _load_json(search_index)
        status = _validate_status(status_file)
    else:
        if search_index.is_file():
            _load_json(search_index)
        if status_file.is_file():
            status = _validate_status(status_file)

    if status and status["archive_pages"] != len(html_files) - 1:
        raise SiteValidationError(
            "site-status.json archive_pages does not match generated archive pages"
        )

    return html_files


def _copy_file(source: Path, destination: Path) -> None:
    if source.is_symlink():
        raise SiteValidationError(f"Public artifact cannot contain symlink: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def _copy_tree(source: Path, destination: Path) -> None:
    for path in sorted(source.rglob("*")):
        if path.is_symlink():
            raise SiteValidationError(
                f"Public artifact cannot contain symlink: {path}"
            )
        if path.is_file():
            _copy_file(path, destination / path.relative_to(source))


def build_artifact(source: Path, output: Path) -> list[Path]:
    """Build a new Pages directory from an explicit public-file allowlist."""
    source = source.resolve()
    output = output.resolve()
    if output == source or source in output.parents:
        raise SiteValidationError("Artifact output must be outside the source tree")
    if output.exists():
        raise SiteValidationError(f"Artifact output already exists: {output}")

    html_files = validate_site(source, require_deploy_files=True)
    output.mkdir(parents=True)

    for path in html_files:
        _copy_file(path, output / path.relative_to(source))
    _copy_tree(source / "static", output / "static")
    _copy_file(
        source / "data" / "archive-search-index.json",
        output / "data" / "archive-search-index.json",
    )
    _copy_file(source / "site-status.json", output / "site-status.json")

    for name in PUBLIC_ROOT_FILES:
        path = source / name
        if path.is_file():
            _copy_file(path, output / name)

    (output / ".nojekyll").touch()
    return html_files


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    check_parser = subparsers.add_parser(
        "check", help="validate the generated site currently in the repository"
    )
    check_parser.add_argument("--source", type=Path, default=Path.cwd())

    build_parser = subparsers.add_parser(
        "build", help="validate and build the allowlisted Pages artifact"
    )
    build_parser.add_argument("--source", type=Path, default=Path.cwd())
    build_parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    try:
        if args.command == "check":
            html_files = validate_site(args.source, require_deploy_files=False)
            print(f"Validated {len(html_files)} generated HTML files.")
        else:
            html_files = build_artifact(args.source, args.output)
            print(
                f"Prepared {args.output.resolve()} with "
                f"{len(html_files)} generated HTML files."
            )
    except SiteValidationError as exc:
        print(f"Site validation failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
