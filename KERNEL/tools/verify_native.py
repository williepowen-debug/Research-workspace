#!/usr/bin/env python3
"""Verify one fixture command's exact native references without writing state."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from native import SubprocessGitBoundary, verify_native_references


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=Path)
    parser.add_argument("--repository", type=Path, required=True)
    args = parser.parse_args()
    command = json.loads(args.command.read_text(encoding="utf-8"))
    result = verify_native_references(command, SubprocessGitBoundary(args.repository))
    print(f"perimeter: command={args.command} repository={args.repository} references={len(command.get('native_refs', []))}")
    if result.valid:
        print("PASS: exact native bytes and material structured terms verified; research quality was not judged")
        return 0
    print("EXCEPTION: native-reference verification failed closed")
    for finding in result.findings:
        print(f"{finding.code}\t{finding.location}\t{finding.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
