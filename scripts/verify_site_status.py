#!/usr/bin/env python3
"""Check deployed freshness: exit 0 for healthy, 1 to retry, 2 for failed refresh."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def verify_status(path: Path, expected_generated_at: str) -> int:
    """Retry old deployments, but reject a current deployment with stale data."""
    try:
        status = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Cannot read deployed status: {exc}", file=sys.stderr)
        return 1

    if not isinstance(status, dict):
        print("Deployed status must be a JSON object.", file=sys.stderr)
        return 1
    if status.get("generated_at") != expected_generated_at:
        print("Waiting for the deployed status to become current.")
        return 1
    if status.get("status") != "ok":
        print(
            f"::error::Deployment is current at {expected_generated_at}, "
            f"but its refresh status is {status.get('status')!r}. "
            "The site is serving saved papers. Check the Generate site logs "
            "for the arXiv refresh failure.",
            file=sys.stderr,
        )
        return 2

    print(f"Deployment and arXiv refresh are current at {expected_generated_at}.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("status_file", type=Path)
    parser.add_argument("--expected-generated-at", required=True)
    args = parser.parse_args()
    if not args.expected_generated_at:
        parser.error("--expected-generated-at must not be empty")
    return verify_status(args.status_file, args.expected_generated_at)


if __name__ == "__main__":
    raise SystemExit(main())
