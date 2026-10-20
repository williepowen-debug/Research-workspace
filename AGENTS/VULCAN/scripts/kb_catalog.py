#!/usr/bin/env python3
"""Maintain one KB authority per row and the legacy all-desk TSV read view.

Edit workbook/KB_GENERAL.tsv or CRWV/KB.tsv, then run --write. No source row
is copied into another editable ledger. --check is read-only and used by the
workbook validator (therefore boot and closeout). All paths are desk-relative.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import os
from pathlib import Path
import re
import sys
import tempfile

DESK = Path(__file__).resolve().parents[1]
SOURCES = ("workbook/KB_GENERAL.tsv", "CRWV/KB.tsv")
VIEW = "workbook/KB.tsv"
MIGRATION = "CRWV/KB_MIGRATION.json"
FIELDS = ("id", "date", "channel", "fact", "value", "source", "as_of", "confidence", "notes")
ID_RE = re.compile(r"KB-VULCAN-\d{3,}\Z")


def collect(desk=DESK):
    """Reject missing sources, header/width drift, shared IDs and lost baseline IDs."""
    found = {}
    for relative in SOURCES:
        path = desk / relative
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream, delimiter="\t")
            if reader.fieldnames != list(FIELDS):
                raise ValueError(f"{relative}: KB header differs from the registered schema")
            for line, row in enumerate(reader, 2):
                if None in row or any(v is None for v in row.values()):
                    raise ValueError(f"{relative}:{line}: ragged KB row")
                key = row["id"]
                if not ID_RE.fullmatch(key):
                    raise ValueError(f"{relative}:{line}: invalid KB ID {key!r}")
                if key in found:
                    raise ValueError(f"{key}: duplicate authority in {found[key][0]} and {relative}")
                found[key] = (relative, row)
    baseline = json.loads((desk / MIGRATION).read_text(encoding="utf-8"))
    missing = set(baseline["row_sha256"]) - found.keys()
    if missing:
        raise ValueError(f"Permanent KB record(s) lost since migration: {', '.join(sorted(missing))}")
    return dict(sorted(found.items(), key=lambda item: int(item[0].rsplit("-", 1)[1])))


def render(records):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(row for _, row in records.values())
    return stream.getvalue().encode("utf-8")


def check(desk=DESK):
    """Return errors rather than silently repairing a stale compatibility view."""
    try:
        expected = render(collect(desk))
        if (desk / VIEW).read_bytes() != expected:
            return ["KB.tsv: generated view differs from canonical sources; run scripts/kb_catalog.py --write"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return [f"KB authority check: {exc}"]
    return []


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--find", metavar="KB-ID")
    mode.add_argument("--next-id", action="store_true")
    args = parser.parse_args()
    try:
        if args.check:
            errors = check()
            if errors:
                print("\n".join(errors), file=sys.stderr)
                return 2
            print("KB authority/view check: PASS")
            return 0
        records = collect()
        if args.find:
            if args.find not in records:
                raise ValueError(f"Unknown KB ID: {args.find}")
            authority, row = records[args.find]
            print(json.dumps({"authority": authority, "row": row}, indent=2, ensure_ascii=False))
        elif args.next_id:
            print(f"KB-VULCAN-{max(int(k.rsplit('-', 1)[1]) for k in records) + 1:03d}")
        else:
            payload = render(records)
            destination = DESK / VIEW
            # Replace only the derived view; never write either source.
            with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(payload)
            try:
                os.replace(temporary, destination)
            finally:
                if temporary.exists():
                    temporary.unlink()
            print(f"Generated {VIEW}: {len(records)} rows; canonical sources unchanged")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"KB catalog: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
