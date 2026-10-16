#!/usr/bin/env python3
"""active_decisions_digest.py — the BOOT step-3 read of PROME/ACTIVE_DECISIONS.md.

One line per row of § Live Decision Index: title · leading state token (first 72 chars of the
State cell) · Next (bounded) · bytes · ACTIONABLE | GUARD. ACTIONABLE = the leading token is one of
the file's own non-terminal states (its § Rules). Everything else is a GUARD row: closed or
monitor-only, kept for standing guards; read it whole (`--row N`) only when the session touches it.

Exit 1 (loud) on: no index heading · a row with fewer than six cells · an empty State cell.
Acceptance: PROME/tools/tests/ACCEPTANCE_active_decisions_digest_2026-10-16.md.
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT = ROOT / "PROME" / "ACTIVE_DECISIONS.md"
HEADING = "## Live Decision Index"
NON_TERMINAL = ("DRAFT", "PROPOSED", "WILL_APPROVED", "BROKER_PENDING", "ORDER_PLACED",
                "FILLED", "POSITION_UPDATED", "LOGGED", "DEFERRED")
_MD = re.compile(r"[*`]")


def _clean(s, n):
    s = _MD.sub("", s).strip()
    s = re.sub(r"\s+", " ", s)
    return s if len(s) <= n else s[: n - 1] + "…"


def parse(text):
    """→ (rows, errors). rows = [{n,title,state,token,next,bytes,cls,raw}] in file order."""
    lines = text.split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == HEADING)
    except StopIteration:
        return [], [f"no heading `{HEADING}`"]
    rows, errors, n, in_table = [], [], 0, False
    for i in range(start + 1, len(lines)):
        l = lines[i]
        if l.startswith("## "):
            break
        if not l.startswith("|"):
            if in_table:
                break
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if not in_table:
            in_table = True          # header row
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue                 # separator row
        n += 1
        if len(cells) < 6:
            errors.append(f"row {n} (line {i+1}) has {len(cells)} cells, 6 required: {_clean(cells[0], 60)}")
            continue
        state = _MD.sub("", cells[1]).strip()
        if not state:
            errors.append(f"row {n} (line {i+1}) has an EMPTY State cell: {_clean(cells[0], 60)}")
            continue
        token = re.split(r"[\s—(:]", state, 1)[0].strip("`*")
        cls = "ACTIONABLE" if token in NON_TERMINAL else "GUARD"
        rows.append(dict(n=n, title=_clean(cells[0], 70), state=_clean(cells[1], 72), token=token,
                         next=_clean(cells[3], 72), bytes=len(l.encode("utf-8")), cls=cls, raw=l))
    if not rows and not errors:
        errors.append("index table has no rows")
    return rows, errors


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("path", nargs="?", default=str(DEFAULT))
    ap.add_argument("--row", type=int, help="print row N whole (byte-exact) and exit")
    ap.add_argument("--check", action="store_true", help="parse only; rc=1 on any defect")
    a = ap.parse_args(argv)
    p = Path(a.path)
    if not p.is_file():
        print(f"ACTIVE-DECISIONS-DIGEST 1 FAIL: {p} not found"); return 1
    data = p.read_bytes()
    rows, errors = parse(data.decode("utf-8"))
    sha = hashlib.sha256(data).hexdigest()[:12]
    if a.row is not None:
        hit = [r for r in rows if r["n"] == a.row]
        if not hit:
            print(f"ACTIVE-DECISIONS-DIGEST 1 FAIL: no row {a.row} (rows 1–{len(rows)})"); return 1
        sys.stdout.write(hit[0]["raw"] + "\n"); return 0
    rc = 1 if errors else 0
    if a.check:
        for e in errors:
            print("  ❌ " + e)
        print(f"ACTIVE-DECISIONS-DIGEST {rc} {'FAIL' if rc else 'OK'}: {len(rows)} rows · {len(errors)} defect(s) · sha {sha}")
        return rc
    act = [r for r in rows if r["cls"] == "ACTIONABLE"]
    print(f"ACTIVE_DECISIONS digest · {p.relative_to(ROOT) if p.is_relative_to(ROOT) else p} · sha {sha} · "
          f"{len(data):,} B · {len(rows)} rows · {len(act)} ACTIONABLE")
    for r in rows:
        mark = "★" if r["cls"] == "ACTIONABLE" else "·"
        print(f"{mark} [{r['n']}] {r['cls']:<10} {r['bytes']:>5} B  {r['title']}")
        print(f"      state: {r['state']}")
        print(f"      next:  {r['next']}")
    for e in errors:
        print("  ❌ " + e)
    print(f"Whole row: `python3 PROME/tools/active_decisions_digest.py --row <n>` — read ACTIONABLE rows whole, "
          f"and any GUARD row the session will touch; standing guards live in the rows, never here.")
    if errors:
        print(f"ACTIVE-DECISIONS-DIGEST 1 FAIL: {len(errors)} defect(s) — a row the digest cannot show is a row the boot did not read")
    return rc


if __name__ == "__main__":
    sys.exit(main())
