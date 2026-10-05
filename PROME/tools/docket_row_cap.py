#!/usr/bin/env python3
"""docket_row_cap.py — byte cap on CHANGED rows of PROME/DOCKET.tsv.

WHY THIS EXISTS
---------------
The STATUS read cap (32,550 B) worked: PROME/STATUS.md went 105 KB → 17 KB. The bytes
did not disappear — they moved into DOCKET.tsv, which has no cap: 15 KB in July 2026
→ 1.3 MB on 2026-10-05 (612 lines; average row 430 B → 2,170 B; L386 is a 19 KB rule
stored as a docket row). Between 2026-09-15 and 2026-10-05 the file grew 627 KB:
508 KB in 210 new rows (median 2,013 B) and 118 KB in 114 in-place edits of existing
rows. A cap on NEW rows alone misses the second channel, so this check meters every
row that CHANGED relative to a base, never the file as a whole.

CONTRACT
--------
* Base = `git show <base>:PROME/DOCKET.tsv` (default HEAD). Candidate = the working
  tree file (default), or the index with --staged (`git show :PROME/DOCKET.tsv`,
  which honours GIT_INDEX_FILE, so `git commit <path>` and the pre-commit hook see
  exactly the content being committed).
* Rows pair by PHYSICAL LINE NUMBER. That is the docket's own citation key (header
  L1: rows are cited by line number; never insert, delete or reorder; append at EOF;
  terminal rows compact IN PLACE). A candidate with FEWER lines than the base is a
  finding (ROWS REMOVED) for the same reason — citations would silently re-point.
* A changed row (added, or different from its base row) must be ≤ --cap bytes
  (UTF-8). A row ALREADY over the cap in the base may be edited only to SHRINK or
  stay the same size (ratchet) — grandfathered rows never block an unrelated commit,
  and never get bigger.
* Comment lines (`#`) and unchanged rows are never findings.
* rc 0 clean · rc 1 finding · rc 2 could not establish (git unavailable, no base
  blob, unreadable candidate) — never read 2 as clean (CHECK_STANDARD §9).
* The number is Will's and is NOT in this file: it is read from `scripts/harness_caps.env`
  (`DOCKET_ROW_CAP_BYTES=…`, the same shared-constants file the memory guards use), or
  given explicitly with --cap. With --staged the policy comes from the INDEX, the same
  version as the candidate rows (CATO PR1, 2026-10-05: a working-tree read let an unstaged
  edit to the policy decide what a commit could contain). With neither, the mechanism is DORMANT (rc 0): the "not
  configured" line is visible at the pre-commit hook (git relays hook stderr even on a
  successful commit) and in the closeout gate's row; the PostToolUse save hook stays SILENT
  when dormant — its exit-0 stderr does not reach the model (handoff finding, 2026-10-05).
  Merging the mechanism decides nothing about the policy; one line activates all three sites.

Tests: PROME/tools/tests/test_docket_row_cap.py (throwaway repos only).
"""
from __future__ import annotations

import argparse
import os
import pathlib
import subprocess
import sys

DOCKET = "PROME/DOCKET.tsv"
CAPS_ENV = "scripts/harness_caps.env"
CAP_KEY = "DOCKET_ROW_CAP_BYTES"


def parse_cap(text: str):
    """The policy number in a harness_caps.env text, or None when the key is unset.
    Malformed ⇒ ValueError (never a silent default)."""
    values = [l.split("=", 1)[1].strip() for l in text.splitlines() if l.startswith(CAP_KEY + "=")]
    if not values:
        return None
    if len(values) > 1:
        raise ValueError(f"{CAP_KEY} set {len(values)} times in {CAPS_ENV}")
    cap = int(values[0])
    if cap <= 0:
        raise ValueError(f"{CAP_KEY} must be positive, got {cap}")
    return cap


def configured_cap(root: pathlib.Path):
    """Working-tree policy (save hook, closeout gate). Absent file ⇒ None (dormant)."""
    try:
        text = (root / CAPS_ENV).read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    return parse_cap(text)


def staged_cap(root: pathlib.Path):
    """Index policy for --staged (CATO PR1, 2026-10-05): the cap must come from the SAME index
    as the docket candidate, or an unstaged edit to the shared policy file (another session's,
    unfinished) decides what a commit may contain. Honours GIT_INDEX_FILE like `git show :path`.
    Not in the index ⇒ None (dormant — the commit carries no policy file, same rule as an
    absent working-tree file). Listed but unreadable, unmerged, not a regular file (symlink,
    submodule, directory) or not UTF-8 ⇒ ValueError."""
    listed = _git(["ls-files", "--stage", "--", CAPS_ENV], root)
    if listed.returncode != 0:
        raise ValueError(f"cannot list {CAPS_ENV} in the index")
    entries = [e.split("\t", 1) for e in listed.stdout.decode("utf-8", "replace").splitlines()]
    if not entries:
        return None
    if any(len(e) != 2 or e[1] != CAPS_ENV for e in entries):
        raise ValueError(f"{CAPS_ENV} is not a single file in the index (a directory of that name?)")
    if len(entries) != 1 or entries[0][0].split()[2] != "0":
        raise ValueError(f"{CAPS_ENV} is unmerged in the index")
    if entries[0][0].split()[0] not in ("100644", "100755"):    # independent reader C5/C7, 2026-10-05:
        raise ValueError(f"{CAPS_ENV} in the index is not a regular file "   # a symlink's blob is its target
                         f"(mode {entries[0][0].split()[0]})")              # text — reading it fails open
    blob = read_blob(f":{CAPS_ENV}", root)
    if blob is None:
        raise ValueError(f"{CAPS_ENV} is in the index but unreadable")
    try:
        text = blob.decode("utf-8")
    except UnicodeDecodeError:
        raise ValueError(f"{CAPS_ENV} in the index is not UTF-8") from None
    return parse_cap(text)


def _git(args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True)


def read_blob(spec, cwd):
    """`git show <spec>`; None when the blob does not exist (base absent)."""
    p = _git(["show", spec], cwd)
    if p.returncode != 0:
        return None
    return p.stdout


def split_rows(data: bytes) -> list[bytes]:
    rows = data.split(b"\n")
    if rows and rows[-1] == b"":
        rows.pop()
    return rows


def scan(base: bytes | None, cand: bytes, cap: int) -> list[dict]:
    """Pure: findings over (base, candidate) row lists. base None = every row is new."""
    b_rows = split_rows(base) if base is not None else []
    c_rows = split_rows(cand)
    findings: list[dict] = []
    if len(c_rows) < len(b_rows):
        findings.append({"kind": "ROWS-REMOVED", "line": len(c_rows) + 1,
                         "size": 0, "base_size": 0,
                         "removed": len(b_rows) - len(c_rows), "head": ""})
    for i, row in enumerate(c_rows):
        if row.lstrip().startswith(b"#"):
            continue
        size = len(row)
        base_row = b_rows[i] if i < len(b_rows) else None
        if base_row is not None and base_row == row:
            continue                                     # unchanged: never a finding
        base_size = len(base_row) if base_row is not None else None
        head = row.split(b"\t")[1][:80].decode("utf-8", "replace") if b"\t" in row \
            else row[:80].decode("utf-8", "replace")
        if size <= cap:
            continue
        if base_size is not None and base_size > cap:
            if size <= base_size:
                continue                                 # grandfathered row shrank or held
            kind = "GREW-OVER-CAP"
        else:
            kind = "NEW-OVER-CAP" if base_row is None else "EDIT-OVER-CAP"
        findings.append({"kind": kind, "line": i + 1, "size": size,
                         "base_size": base_size, "head": head})
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--cap", type=int, default=None,
                    help=f"bytes per changed row (default: {CAP_KEY} in {CAPS_ENV}; unset = dormant)")
    ap.add_argument("--base", default="HEAD", help="git rev holding the base docket")
    ap.add_argument("--staged", action="store_true",
                    help="candidate = the index (pre-commit hook / `git commit <path>`)")
    ap.add_argument("--docket", default=DOCKET, help="repo-relative docket path")
    ap.add_argument("--quiet", action="store_true", help="findings and verdict only")
    args = ap.parse_args()

    top = _git(["rev-parse", "--show-toplevel"], os.getcwd())
    if top.returncode != 0:
        print("⚠️  DOCKET-ROW-CAP UNKNOWN — not inside a git repository")
        return 2
    root = pathlib.Path(top.stdout.decode().strip())
    cap = args.cap
    if cap is None:
        source = f"{CAPS_ENV} (index)" if args.staged else CAPS_ENV
        try:
            cap = staged_cap(root) if args.staged else configured_cap(root)
        except ValueError as exc:
            print(f"⚠️  DOCKET-ROW-CAP UNKNOWN — {exc}")
            return 2
        if cap is None:
            print(f"·  DOCKET-ROW-CAP not configured — set {CAP_KEY}=<bytes> in {source} to activate "
                  "(mechanism dormant; this line is the only effect)")
            return 0
    args.cap = cap

    base = read_blob(f"{args.base}:{args.docket}", root)
    if base is None:
        print(f"⚠️  DOCKET-ROW-CAP UNKNOWN — no {args.docket} at {args.base}; "
              "cannot pair rows (an absent base is not an empty one)")
        return 2
    if args.staged:
        cand = read_blob(f":{args.docket}", root)
        if cand is None:
            print(f"⚠️  DOCKET-ROW-CAP UNKNOWN — {args.docket} is not in the index")
            return 2
    else:
        try:
            cand = (root / args.docket).read_bytes()
        except OSError as exc:
            print(f"⚠️  DOCKET-ROW-CAP UNKNOWN — {args.docket}: {exc}")
            return 2

    findings = scan(base, cand, args.cap)
    for f in findings:
        if f["kind"] == "ROWS-REMOVED":
            print(f"❌ DOCKET-ROW-CAP {args.docket}: {f['removed']} row(s) REMOVED vs {args.base} "
                  f"(candidate ends at L{f['line'] - 1}) — rows are cited by line number; "
                  "tombstone in place, never delete")
            continue
        was = f" (was {f['base_size']:,} B)" if f["base_size"] is not None else ""
        print(f"❌ DOCKET-ROW-CAP {args.docket}:L{f['line']} — {f['kind']}: {f['size']:,} B "
              f"> cap {args.cap:,}{was}: {f['head']}")
    changed = sum(1 for i, r in enumerate(split_rows(cand))
                  if i >= len(split_rows(base)) or split_rows(base)[i] != r)
    if findings:
        print(f"❌ DOCKET-ROW-CAP {len(findings)} finding(s) over {changed} changed row(s) "
              f"(cap {args.cap:,} B per changed row; base {args.base}) — shorten the ROW: "
              "move narrative to the owner's file and leave a pointer; a rule is not a docket row")
        return 1
    if not args.quiet:
        print(f"✅ DOCKET-ROW-CAP ok — {changed} changed row(s) within {args.cap:,} B (base {args.base})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
