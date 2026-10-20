#!/usr/bin/env python3
"""Render on-demand metal KBs from the permanent ledger and reviewed tags.

No network or third-party dependencies. --check is read-only: 0 current,
1 missing/stale views, 2 invalid/missing inputs. --refresh validates every row
before replacing any view. Dates, corrections and original IDs are preserved.
"""

import argparse
import csv
import io
import os
from pathlib import Path
import sys
import tempfile

HERE = Path(__file__).resolve().parent
METALS = ("gold", "silver", "platinum", "palladium", "copper")
FIELDS = ("id", "date", "channel", "fact", "value", "source", "as_of",
          "confidence", "notes")


def read_table(path, fields):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t", strict=True)
        if reader.fieldnames != list(fields):
            raise ValueError(f"{path}: unexpected header")
        rows = list(reader)
    seen = set()
    for row in rows:
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"{path}: malformed row")
        key = row["id"]
        if not key or key in seen:
            raise ValueError(f"{path}: empty or duplicate ID {key!r}")
        seen.add(key)
    if not rows:
        raise ValueError(f"{path}: empty table")
    return rows


def build_views(root):
    rows = read_table(root / "workbook/KB.tsv", FIELDS)
    assignments = read_table(root / "KB_METALS.tsv", ("id", "metals", "rationale"))
    tags = {}
    for row in assignments:
        labels = row["metals"].split(",")
        if (len(set(labels)) != len(labels)
                or not set(labels) <= set((*METALS, "shared"))
                or ("shared" in labels and labels != ["shared"])
                or not row["rationale"].strip()):
            raise ValueError(f"invalid metal assignment for {row['id']}")
        tags[row["id"]] = labels
    ids = {row["id"] for row in rows}
    if ids != set(tags):
        raise ValueError(f"unclassified IDs: {sorted(ids - set(tags))}; "
                         f"unknown IDs in tags: {sorted(set(tags) - ids)}")
    views = {}
    for metal in (*METALS, "shared"):
        stream = io.StringIO(newline="")
        writer = csv.DictWriter(stream, fieldnames=FIELDS, delimiter="\t",
                                lineterminator="\n")
        writer.writeheader()
        selected = [row for row in rows if metal in tags[row["id"]]
                    or (metal == "shared" and len(tags[row["id"]]) > 1)]
        writer.writerows(selected)
        views[root / metal / "KB.tsv"] = stream.getvalue().encode("utf-8")
    return views


def run(root, refresh=False):
    try:
        views = build_views(root)
        stale = [path for path, data in views.items()
                 if not path.exists() or path.read_bytes() != data]
        if refresh:
            for path in stale:
                path.parent.mkdir(parents=True, exist_ok=True)
                # Unique same-directory temp files; interrupted writes cannot
                # replace a view with a partial TSV. A later check detects a
                # partially completed refresh across the six files.
                name = None
                try:
                    with tempfile.NamedTemporaryFile(dir=path.parent,
                                                     delete=False) as stream:
                        name = stream.name
                        stream.write(views[path])
                    os.replace(name, path)
                finally:
                    if name and os.path.exists(name):
                        os.unlink(name)
            print(f"Metal KB views current: six views, {len(stale)} refreshed.")
            return 0
        if stale:
            print("⚠️ Metal KB views missing/stale: "
                  + ", ".join(str(path.relative_to(root)) for path in stale)
                  + ". Review KB_METALS.tsv and run refresh_metal_kbs.py --refresh.")
            return 1
        print("Metal KB views current (content checked against ledger and tags).")
        return 0
    except (OSError, ValueError, csv.Error) as exc:
        print(f"🔴 Metal KB check FAILED: {exc}", file=sys.stderr)
        return 2


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--refresh", action="store_true")
    args = parser.parse_args(argv)
    return run(HERE, refresh=args.refresh)


if __name__ == "__main__":
    sys.exit(main())
