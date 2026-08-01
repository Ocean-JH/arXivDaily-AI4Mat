from pathlib import Path

import pytest

from scripts.prepare_site_artifact import SiteValidationError, _site_html_files


def _write_archive_shell(project: Path) -> None:
    (project / "index.html").write_text("index", encoding="utf-8")
    (project / "archive.html").write_text("archive", encoding="utf-8")


def test_generated_archive_pages_must_not_use_the_repository_root(
    tmp_path: Path,
) -> None:
    _write_archive_shell(tmp_path)
    (tmp_path / "archive-2.html").write_text("legacy", encoding="utf-8")

    with pytest.raises(SiteValidationError, match="moved under archive"):
        _site_html_files(tmp_path)


def test_nested_archive_pages_must_be_contiguous(tmp_path: Path) -> None:
    _write_archive_shell(tmp_path)
    archive_dir = tmp_path / "archive"
    archive_dir.mkdir()
    (archive_dir / "page-2.html").write_text("page 2", encoding="utf-8")
    (archive_dir / "page-4.html").write_text("page 4", encoding="utf-8")

    with pytest.raises(SiteValidationError, match="contiguous"):
        _site_html_files(tmp_path)
