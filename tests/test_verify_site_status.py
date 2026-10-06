import json
from pathlib import Path

import pytest

from scripts.verify_site_status import verify_status


EXPECTED_GENERATED_AT = "2026-10-06T06:00:00+08:00"


@pytest.mark.parametrize(
    ("status", "exit_code"),
    [
        ({"generated_at": EXPECTED_GENERATED_AT, "status": "ok"}, 0),
        ({"generated_at": EXPECTED_GENERATED_AT, "status": "stale"}, 2),
        ({"generated_at": EXPECTED_GENERATED_AT}, 2),
        ({"generated_at": "2026-10-05T06:00:00+08:00", "status": "ok"}, 1),
        ({"generated_at": "2026-10-05T06:00:00+08:00", "status": "stale"}, 1),
        ({"status": "ok"}, 1),
        ([], 1),
    ],
)
def test_deployed_status_requires_current_successful_refresh(
    tmp_path: Path, status: object, exit_code: int, capsys: pytest.CaptureFixture,
) -> None:
    path = tmp_path / "site-status.json"
    path.write_text(json.dumps(status), encoding="utf-8")

    assert verify_status(path, EXPECTED_GENERATED_AT) == exit_code
    output = capsys.readouterr()
    if exit_code == 2:
        assert "::error::" in output.err
        assert "Generate site logs" in output.err


def test_unreadable_deployed_status_can_be_retried(tmp_path: Path) -> None:
    path = tmp_path / "site-status.json"

    assert verify_status(path, EXPECTED_GENERATED_AT) == 1
    path.write_text("upstream error", encoding="utf-8")
    assert verify_status(path, EXPECTED_GENERATED_AT) == 1
