#!/usr/bin/env python3
"""active_decisions_digest.py — the BOOT step-3 read of PROME/ACTIVE_DECISIONS.md.

One line per row of § Live Decision Index: title · the State cell's first 72 chars · Next (bounded) ·
bytes · class. Classes (never a silent default):
  ACTIONABLE   — any of the file's own non-terminal states (its § Rules bullet) appears in the first
                 72 chars of the State cell, case-insensitive, as a whole token;
  GUARD        — the leading token is a KNOWN terminal/guard token (the Rules' terminal list + the
                 explicit GUARD_TOKENS list below): a closed or monitor-only row kept for its
                 standing guards; read whole (`--row N`) when the session touches it;
  UNCLASSIFIED — anything else: printed with ★, counted in the header, rc=1 (read the row whole).
A GUARD/UNCLASSIFIED row whose cells carry a date inside the next 7 days gets a ⏱ cue.

Exit 1 (loud) on: no index heading · a row without exactly six cells (`\\|` honoured) · an empty
State cell · an UNCLASSIFIED row · the Rules bullet's state list disagreeing with this tool's list ·
any pipe-line in the section the parser did not consume.
Acceptance: PROME/tools/tests/ACCEPTANCE_active_decisions_digest_2026-10-16.md.
"""
import argparse
import datetime as dt
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT = ROOT / "PROME" / "ACTIVE_DECISIONS.md"
HEADING = "## Live Decision Index"
NON_TERMINAL = ("DRAFT", "PROPOSED", "WILL_APPROVED", "BROKER_PENDING", "ORDER_PLACED",
                "FILLED", "POSITION_UPDATED", "LOGGED", "DEFERRED")
TERMINAL = ("COMPLETED", "REJECTED", "EXPIRED", "SUPERSEDED", "CANCELLED")
# Leading tokens of rows kept for their standing guards (closed / executed / monitor-only).
# A new leading token is UNCLASSIFIED until it is added here or the owner re-states the row.
GUARD_TOKENS = ("CLOSED", "MONITOR_ONLY", "RE-BASED", "REBUILT", "LIVE", "EXECUTED", "WILL_RULED",
                "PHASE_1_EXECUTED", "WORKTREE_ISOLATION_OPEN", "RESOLVED", "RETIRED", "LAPSED")
_MD = re.compile(r"[*`]")
_PIPE = re.compile(r"(?<!\\)\|")
_MDY = re.compile(r"\b(\d{1,2})/(\d{1,2})\b")
_ISO = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_RULES = re.compile(r"non-terminal states?:\s*(.+)$", re.M)


def _clean(s, n):
    s = _MD.sub("", s).replace("\\|", "|").strip()
    s = re.sub(r"\s+", " ", s)
    return s if len(s) <= n else s[: n - 1] + "…"


def _split(line):
    return [c.strip() for c in _PIPE.split(line.strip().strip("|"))] if not line.strip().endswith("\\|") \
        else [c.strip() for c in _PIPE.split(line.strip()[1:])]


def _classify(state_clean):
    head = state_clean[:72].upper()
    tokens = set(re.findall(r"[A-Z][A-Z0-9_\-]*[A-Z0-9]|[A-Z]", head)) | set(re.findall(r"[A-Z][A-Z0-9_]*", head))
    lead = re.split(r"[\s—(:;,/→]", head, 1)[0].strip("`*_") if head else ""
    if tokens & set(NON_TERMINAL):
        return "ACTIONABLE"
    if lead in TERMINAL or lead in GUARD_TOKENS:
        return "GUARD"
    return "UNCLASSIFIED"


def _dated_soon(raw, today, days=7):
    hits = set()
    for m in _ISO.finditer(raw):
        try:
            d = dt.date(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            continue
        if 0 <= (d - today).days <= days:
            hits.add(d.strftime("%-m/%-d"))
    for m in _MDY.finditer(raw):
        try:
            d = dt.date(today.year, int(m[1]), int(m[2]))
        except ValueError:
            continue
        if 0 <= (d - today).days <= days:
            hits.add(d.strftime("%-m/%-d"))
    return sorted(hits, key=lambda s: tuple(map(int, s.split("/"))))


def parse(text, today=None):
    """→ (rows, errors). rows = [{n,title,state,cls,next,bytes,raw,dated}] in file order."""
    today = today or dt.date.today()
    errors = []
    m = _RULES.search(text)
    if not m:
        errors.append("Rules bullet 'non-terminal states:' not found — the state list cannot be cross-checked")
    else:
        declared = tuple(re.findall(r"`([A-Z_]+)`", m[1]))
        if declared != NON_TERMINAL:
            errors.append(f"Rules bullet lists {declared}; this tool's NON_TERMINAL is {NON_TERMINAL} — fix the tool or the file")
    lines = text.split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == HEADING)
    except StopIteration:
        return [], errors + [f"no heading `{HEADING}`"]
    rows, n, seen_header, pipe_lines, consumed = [], 0, False, 0, 0
    for i in range(start + 1, len(lines)):
        l = lines[i]
        if l.startswith("## "):
            break
        if not l.lstrip().startswith("|"):
            continue                              # blank, comment or prose: skipped, never ends the table
        pipe_lines += 1
        cells = _split(l)
        if not seen_header:
            seen_header = True; consumed += 1     # header row
            continue
        if all(set(c) <= set("-: ") for c in cells):
            consumed += 1; continue               # separator row
        n += 1; consumed += 1
        if len(cells) != 6:
            errors.append(f"row {n} (line {i+1}) has {len(cells)} cells, exactly 6 required: {_clean(cells[0], 60)}")
            continue
        state_clean = _clean(cells[1], 10_000)
        if not state_clean:
            errors.append(f"row {n} (line {i+1}) has an EMPTY State cell: {_clean(cells[0], 60)}")
            continue
        cls = _classify(state_clean)
        if cls == "UNCLASSIFIED":
            errors.append(f"row {n} (line {i+1}) UNCLASSIFIED — leading token `{state_clean.split(' ')[0]}` is neither non-terminal nor a known guard token: {_clean(cells[0], 60)}")
        rows.append(dict(n=n, title=_clean(cells[0], 70), state=_clean(cells[1], 72), cls=cls,
                         next=_clean(cells[3], 72), bytes=len(l.encode("utf-8")), raw=l,
                         dated=_dated_soon(l, today)))
    if pipe_lines != consumed:
        errors.append(f"{pipe_lines - consumed} pipe-line(s) in the section were not consumed by the parser")
    if not rows and not any("cells" in e or "EMPTY" in e for e in errors):
        errors.append("index table has no rows")
    return rows, errors


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("path", nargs="?", default=str(DEFAULT))
    ap.add_argument("--row", type=int, help="print row N whole (byte-exact) and exit")
    ap.add_argument("--check", action="store_true", help="parse only; rc=1 on any defect")
    ap.add_argument("--today", help="YYYY-MM-DD for the ⏱ cue (tests); default = today")
    a = ap.parse_args(argv)
    today = dt.date.fromisoformat(a.today) if a.today else dt.date.today()
    p = Path(a.path)
    if not p.is_file():
        print(f"ACTIVE-DECISIONS-DIGEST 1 FAIL: {p} not found"); return 1
    data = p.read_bytes()
    rows, errors = parse(data.decode("utf-8"), today)
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
    act = sum(r["cls"] == "ACTIONABLE" for r in rows)
    unc = sum(r["cls"] == "UNCLASSIFIED" for r in rows)
    rel = p.relative_to(ROOT) if p.is_relative_to(ROOT) else p
    print(f"ACTIVE_DECISIONS digest · {rel} · sha {sha} · {len(data):,} B · {len(rows)} rows · "
          f"{act} ACTIONABLE · {unc} UNCLASSIFIED · as-of {today.isoformat()}")
    for r in rows:
        mark = "★" if r["cls"] != "GUARD" else "·"
        cue = f"  ⏱ dated inside next 7d: {', '.join(r['dated'])}" if r["dated"] and r["cls"] != "ACTIONABLE" else ""
        print(f"{mark} [{r['n']}] {r['cls']:<12} {r['bytes']:>5} B  {r['title']}{cue}")
        print(f"      state: {r['state']}")
        print(f"      next:  {r['next']}")
    for e in errors:
        print("  ❌ " + e)
    print("Whole row: `python3 PROME/tools/active_decisions_digest.py --row <n>` — read ★ rows whole (ACTIONABLE and "
          "UNCLASSIFIED), any ⏱ row, and any GUARD row the session will touch; standing guards live in the rows, never here.")
    if errors:
        print(f"ACTIVE-DECISIONS-DIGEST 1 FAIL: {len(errors)} defect(s) — a row the digest cannot class is a row the boot must read whole")
    return rc


if __name__ == "__main__":
    sys.exit(main())
