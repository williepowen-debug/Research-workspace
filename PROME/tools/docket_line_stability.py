#!/usr/bin/env python3
"""docket_line_stability.py — refuse a commit that moves any existing PROME/DOCKET.tsv row.

WHY THIS EXISTS
---------------
DOCKET rows are cited by PHYSICAL LINE NUMBER (L#) everywhere in the fleet. A commit
that inserts a row mid-file, swaps two rows, or deletes one and appends another leaves
every later citation pointing at a different, perfectly well-formed obligation — no
reader can tell. `docket_row_cap.py` held the only ROWS-REMOVED test, it is dormant
until a byte cap is configured, and it pairs rows by position, so an insert, a swap
and a delete+append all passed it (PROME, 2026-10-20; Will "ok check" 22:13 ET).

CONTRACT (acceptance: PROME/tools/tests/ACCEPTANCE_docket_line_stability_2026-10-21.md)
--------
* Base = `git show <base>:PROME/DOCKET.tsv` (default HEAD). Candidate = the working
  tree, or the index with --staged (honours GIT_INDEX_FILE, so the pre-commit hook and
  `git commit <path>` see exactly what is committed).
* Allowed: edits IN PLACE (any line keeps its number) and APPENDS at EOF.
* Refused (rc 1): fewer lines than the base (ROWS-REMOVED); any line whose content is a
  base row that sat at a DIFFERENT line (MOVED) — that is the signature of an insert,
  a swap or a delete+append, because the rows after it shift. Only base lines that occur
  exactly once and are not blank are position keys, so repeated lines never false-flag.
* Always on: no configuration, no dormant state. rc 2 = could not establish (no base
  blob, unreadable candidate) — never read 2 as clean (CHECK_STANDARD §9).
* Sanctioned renumbering (e.g. a Will-approved archival rotation): set
  DOCKET_LINE_SHIFT_APPROVED=<record> — the findings still print, with a ⚠️ line naming
  the record, and the result is rc 0. Never silent.
* Known limits (independent read 1, 2026-10-21): any displacement where EVERY moved row
  is also edited (e.g. a swap of two rows that are both edited, or a whole-file reformat
  that changes every row's bytes) is invisible — no unedited row is left to show it. The
  hook runs only inside `git commit` against HEAD: a `pull --rebase` replay or a merge
  that re-orders two desks' concurrent EOF appends is not checked (`--base HEAD^2` /
  `--base ORIG_HEAD` can be run by hand). The guard protects line identity, not content.

Tests: PROME/tools/tests/test_docket_line_stability.py (throwaway repos only).
"""
from __future__ import annotations

import argparse
import os
import pathlib
import subprocess
import sys
from collections import Counter

DOCKET = "PROME/DOCKET.tsv"
ESCAPE = "DOCKET_LINE_SHIFT_APPROVED"


def _git(args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True)


def read_blob(spec, cwd):
    """`git show <spec>`; None when the blob does not exist."""
    p = _git(["show", spec], cwd)
    if p.returncode != 0:
        return None
    return p.stdout


def split_rows(data: bytes) -> list[bytes]:
    rows = data.split(b"\n")
    if rows and rows[-1] == b"":
        rows.pop()
    # one trailing CR per row is ignored, so a CRLF flip in the same commit cannot hide a shift
    return [r[:-1] if r.endswith(b"\r") else r for r in rows]


def scan(base: bytes, cand: bytes) -> list[dict]:
    """Pure: findings over (base, candidate). Lines are 1-based in findings."""
    b_rows = split_rows(base)
    c_rows = split_rows(cand)
    counts = Counter(b_rows)
    keys = {row: i for i, row in enumerate(b_rows)
            if counts[row] == 1 and row.strip() != b""}
    findings: list[dict] = []
    if len(c_rows) < len(b_rows):
        findings.append({"kind": "ROWS-REMOVED", "line": len(c_rows) + 1,
                         "removed": len(b_rows) - len(c_rows)})
    for i, row in enumerate(c_rows):
        if i < len(b_rows) and row == b_rows[i]:
            continue
        j = keys.get(row)
        if j is not None and j != i:
            findings.append({"kind": "MOVED", "line": i + 1, "from": j + 1,
                             "head": _head(row)})
    return findings


def _head(row: bytes) -> str:
    cell = row.split(b"\t")[1] if b"\t" in row else row
    return cell[:70].decode("utf-8", "replace")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--base", default="HEAD", help="git rev holding the base docket")
    ap.add_argument("--staged", action="store_true",
                    help="candidate = the index (pre-commit hook / `git commit <path>`)")
    ap.add_argument("--docket", default=DOCKET, help="repo-relative docket path")
    ap.add_argument("--quiet", action="store_true", help="findings and verdict only")
    args = ap.parse_args()

    top = _git(["rev-parse", "--show-toplevel"], os.getcwd())
    if top.returncode != 0:
        print("⚠️  DOCKET-LINES UNKNOWN — not inside a git repository")
        return 2
    root = pathlib.Path(top.stdout.decode().strip())
    base = read_blob(f"{args.base}:{args.docket}", root)
    if base is None:
        print(f"⚠️  DOCKET-LINES UNKNOWN — no {args.docket} at {args.base}; "
              "cannot pair lines (an absent base is not an empty one)")
        return 2
    if args.staged:
        cand = read_blob(f":{args.docket}", root)
        if cand is None:
            print(f"⚠️  DOCKET-LINES UNKNOWN — {args.docket} is not in the index")
            return 2
    else:
        try:
            cand = (root / args.docket).read_bytes()
        except OSError as exc:
            print(f"⚠️  DOCKET-LINES UNKNOWN — {args.docket}: {exc}")
            return 2

    findings = scan(base, cand)
    for f in findings[:10]:
        if f["kind"] == "ROWS-REMOVED":
            print(f"❌ DOCKET-LINES {args.docket}: {f['removed']} row(s) REMOVED vs {args.base} "
                  f"(candidate ends at L{f['line'] - 1}) — tombstone in place, never delete")
        else:
            print(f"❌ DOCKET-LINES {args.docket}:L{f['line']} holds the row that was L{f['from']} "
                  f"at {args.base} — MOVED: {f['head']}")
    if len(findings) > 10:
        print(f"❌ DOCKET-LINES … {len(findings) - 10} more")
    if findings:
        approved = os.environ.get(ESCAPE, "").strip()
        if approved:
            print(f"⚠️  DOCKET-LINES {len(findings)} finding(s) PASSED under {ESCAPE}={approved} — "
                  "every L# citation after the first shift now re-points; record it there")
            return 0
        print(f"❌ DOCKET-LINES {len(findings)} finding(s) — rows are cited by line number: "
              "edit in place or append at EOF; never insert, reorder or delete")
        return 1
    if not args.quiet:
        print(f"✅ DOCKET-LINES ok — every L# at {args.base} still addresses its row")
    return 0


if __name__ == "__main__":
    sys.exit(main())
