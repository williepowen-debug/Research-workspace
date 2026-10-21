#!/usr/bin/env python3
"""firetime_delta.py — split fire-time flags into NEW vs PERSISTING against a dispositioned baseline.

WHY THIS EXISTS (WQ-467 read 1, C4, 2026-10-21)
-----------------------------------------------
`scripts/firetime_check.py` keeps owner-routed flags listed ("persist") and does not separate new
flags from old: 47 at the 10/21 boot. Under WQ-467 an ACTION OWED line needs a disposition for ALL
of its flags, so either every persisting flag is re-answered every boot, or a NEW DATE flag needing
a full logic re-read hides inside a blanket "routed". This tool owes a disposition only for NEW flags.

CONTRACT (acceptance: PROME/tools/tests/ACCEPTANCE_firetime_delta_WQ467C4_2026-10-21.md)
--------
* A flag = an indented ⚠️ line under an artifact header line in the fire-time log. Key = artifact ·
  kind · stable core (DATE DRIFT core = "artifact says <date> ('<token>')", dropping the docket
  "near:" list, which changes as DOCKET changes).
* Baseline = PROME/state/firetime_dispositioned.tsv (tracked). Missing/unreadable ⇒ every flag NEW.
* --accept --pointer <record> rewrites the baseline to exactly the current flag set; kept rows keep
  their first date and pointer. The gate never writes the baseline.
* rc 0 no new flags · rc 1 new flags · rc 2 could not establish (log unreadable, parse miss).

Usage:
  firetime_delta.py --log <firetime log>                     # report
  firetime_delta.py --log <log> --accept --pointer <record>  # record dispositions
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASELINE = ROOT / "PROME/state/firetime_dispositioned.tsv"
HEADER = "artifact\tkind\tcore\tfirst_dispositioned\tpointer"
FLAG_RE = re.compile(r"^\s+⚠️\s+(.*)$")
ART_RE = re.compile(r"^(?:⚠️|✅|❌)\s+(\S.*)$")


def _core(kind: str, msg: str) -> str:
    if kind == "DATE DRIFT":
        m = re.match(r"(artifact says \S+ \('[^']*'\))", msg)
        return m.group(1) if m else msg.split(" — ")[0]
    if kind == "DEAD POINTER":
        m = re.match(r"(`[^`]*`)", msg)
        return m.group(1) if m else msg
    return msg[:200]


def parse(text: str) -> tuple[list[tuple[str, str, str]], int]:
    """Return (flags as (artifact, kind, core), count of raw indented ⚠️ lines)."""
    flags, raw, art = [], 0, None
    for line in text.splitlines():
        m = ART_RE.match(line)
        if m and not line.startswith((" ", "\t")):
            art = m.group(1).strip()
            continue
        f = FLAG_RE.match(line)
        if f:
            raw += 1
            body = f.group(1).strip()
            kind, _, msg = body.partition(": ")
            if not msg:
                kind, msg = "OTHER", body
            if art is not None:
                flags.append((art, kind.strip(), _core(kind.strip(), msg.strip())))
    return flags, raw


FOOTER_RE = re.compile(r"^→ (\d+) flag\(s\)\.", re.M)


def validate(text: str, raw: int, rc: int | None) -> str | None:
    """Return a reason the log cannot be trusted, else None (read 1, ❌1: a crashed checker exits 1).
    A complete run prints every flag and, when it has any, the `→ N flag(s).` footer with N == raw."""
    if "Traceback (most recent call last)" in text:
        return "the checker crashed (traceback in its output)"
    m = FOOTER_RE.search(text)
    if rc == 1 or (rc is None and raw):
        if not m:
            return ("rc 1 with no `→ N flag(s).` footer (incomplete run)" if not raw
                    else "flags reported but no `→ N flag(s).` footer (incomplete run)")
        if int(m.group(1)) != raw:
            return f"footer says {m.group(1)} flag(s) but {raw} flag line(s) printed"
    if rc == 0 and (raw or m):
        return "rc 0 with flag lines or a footer (inconsistent run)"
    if rc not in (None, 0, 1):
        return f"checker rc={rc}"
    if rc is None and not raw and not any(ART_RE.match(l) for l in text.splitlines()):
        return "no artifact lines and no flags — not a fire-time run (empty or unrelated log)"
    return None


def load_baseline(path: pathlib.Path = BASELINE) -> dict | None:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    if not lines or lines[0] != HEADER:
        return None
    out = {}
    for l in lines[1:]:
        c = l.split("\t")
        if len(c) != 5:
            return None
        out[(c[0], c[1], c[2])] = (c[3], c[4])
    return out


def split(flags, baseline):
    new = [f for f in flags if baseline is None or f not in baseline]
    old = [f for f in flags if baseline is not None and f in baseline]
    return new, old


def gone(flags, baseline):
    """Baseline rows absent from this run (read 1, ❌2). Until --accept prunes them, a fixed flag that
    recurs would read as persisting; so they are owed (prune), never silently kept."""
    cur = set(flags)
    return [k for k in (baseline or {}) if k not in cur]


def prune(flags, baseline, path: pathlib.Path = BASELINE) -> int:
    """Drop baseline rows absent from this complete run; add nothing (read 2, ❌A). Allowed while a
    NEW flag is deferred, so a fixed flag never lingers to absorb a later recurrence."""
    cur = set(flags)
    rows = [HEADER] + ["\t".join((*k, *v)) for k, v in (baseline or {}).items() if k in cur]
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return len(rows) - 1


def accept(flags, baseline, pointer: str, path: pathlib.Path = BASELINE, today: str | None = None) -> int:
    today = today or dt.date.today().isoformat()
    rows = [HEADER]
    for f in dict.fromkeys(flags):                       # current set, order kept, duplicates once
        first, ptr = (baseline or {}).get(f, (today, pointer))
        rows.append("\t".join((*f, first, ptr)))
    path.write_text("\n".join(rows) + "\n", encoding="utf-8")
    return len(rows) - 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--log", required=True, type=pathlib.Path)
    ap.add_argument("--baseline", type=pathlib.Path, default=BASELINE)
    ap.add_argument("--accept", action="store_true", help="record every current flag (only when every NEW flag is done or routed)")
    ap.add_argument("--prune", action="store_true", help="drop baseline rows no longer reported; adds nothing; always allowed")
    ap.add_argument("--pointer", default="")
    ap.add_argument("--show", type=int, default=8, help="new flags to print")
    a = ap.parse_args(argv)
    try:
        text = a.log.read_text(encoding="utf-8")
    except OSError as e:
        print(f"⚠️  FIRETIME-DELTA UNKNOWN — log unreadable: {e}")
        return 2
    flags, raw = parse(text)
    if len(flags) != raw:
        print(f"⚠️  FIRETIME-DELTA UNKNOWN — parsed {len(flags)} of {raw} flag lines; a flag outside an "
              "artifact block cannot be keyed")
        return 2
    why = validate(text, raw, None)
    if why:
        print(f"⚠️  FIRETIME-DELTA UNKNOWN — {why}")
        return 2
    baseline = load_baseline(a.baseline)
    if a.prune:
        if baseline is None:
            print("⚠️  FIRETIME-DELTA UNKNOWN — no readable baseline to prune")
            return 2
        dropped = gone(flags, baseline)
        n = prune(flags, baseline, a.baseline)
        print(f"✅ FIRETIME-DELTA baseline pruned: {len(dropped)} row(s) no longer reported removed · {n} kept → {a.baseline}")
        return 0
    if a.accept:
        ptr = a.pointer.strip()
        if not ptr or not (ROOT / ptr).is_file():
            print("❌ FIRETIME-DELTA --accept needs --pointer <existing disposition record, repo-relative>")
            return 2
        new, _ = split(flags, baseline)
        dropped = gone(flags, baseline)
        for art, kind, core in new:
            print(f"   + {kind}: {art} — {core[:100]}")
        n = accept(flags, baseline, ptr, a.baseline)
        print(f"✅ FIRETIME-DELTA baseline written: {n} flag(s) ({len(new)} added · {len(dropped)} pruned) → {a.baseline}")
        return 0
    new, old = split(flags, baseline)
    dropped = gone(flags, baseline)
    note = " (NO readable baseline — every flag counts as NEW)" if baseline is None else ""
    pointers = sorted({baseline[f][1] for f in old}) if baseline else []
    owed = bool(new or dropped)
    print(f"{'⚠️ ' if owed else '✅'} FIRETIME-DELTA {len(flags)} flag(s): {len(new)} NEW · {len(old)} persisting"
          + (f" (dispositioned at {', '.join(pointers)})" if pointers else "")
          + (f" · {len(dropped)} dispositioned flag(s) no longer reported — run --prune" if dropped else "")
          + note)
    for art, kind, core in new[:a.show]:
        print(f"⚠️  NEW {kind}: {art} — {core[:110]}")
    if len(new) > a.show:
        print(f"⚠️  NEW … {len(new) - a.show} more (full list: --show {len(new)})")
    return 1 if owed else 0


if __name__ == "__main__":
    sys.exit(main())
