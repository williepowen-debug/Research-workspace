#!/usr/bin/env python3
"""
positions_from_forge.py — extract Will's positions from FORGE/STATUS.md into a
clean, normalized structure for the TERRY desk dashboard (PROME suggestion #6,
2026-07-20). Kills the re-key-from-screenshots transcription risk: FORGE/STATUS.md
is the fleet's PROME-reconciled broker mirror (refreshed on each Will export), so
one reconcile feeds both surfaces.

What it does: walks the markdown position tables under "## Fidelity — Longs",
"## Fidelity — Thesis Puts" (+ its ### ticker subsections), "## Other puts", and
"## Robinhood …", maps each table's own header row to fields, and emits normalized
rows: group / ticker / instrument / expiry / qty / cost / mark / value / pnl / dte /
note. Option rows get days-to-expiry (DTE) vs --asof (default: today).

DESIGN: fail LOUD, never fabricate. A row it cannot parse is reported in a
`WARNINGS` block, not silently dropped (PROME: "if FORGE format quirks block
parsing, flag me — do not fork a second position record"). If the file moves or
the headers change shape, it says so.

Usage (repo-root-relative — PAT-031, always wrap):
  (cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/positions_from_forge.py)
  ... --json                 # machine-readable
  ... --asof 2026-07-20      # DTE reference date (default today)
  ... --selftest             # offline parse-check against the live FORGE file
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
FORGE_STATUS = REPO / "FORGE" / "STATUS.md"

MONTHS = {m: i for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
     "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}

# where positions live — start at the first Longs table, stop at the reshape/other
# trailing sections. Section headers we treat as position groups:
POS_SECTION_RE = re.compile(r"^##\s+(Fidelity|Robinhood)\b", re.I)
SUBSEC_RE = re.compile(r"^###\s+(.+)$")
# a non-position ## header that ends the region
END_SECTION_RE = re.compile(r"^##\s+(Reshape|Next|Notes|Reconcile|History)", re.I)


def _num(s):
    """Loose numeric parse: '$333.74' -> 333.74, '−69.3%' -> -69.3, '3 (M)' -> 3."""
    if s is None:
        return None
    t = s.strip().replace("**", "").replace("−", "-").replace(",", "")
    t = t.replace("$", "").replace("%", "")
    m = re.search(r"-?\d+(?:\.\d+)?", t)
    return float(m.group()) if m else None


def _parse_expiry(tok, asof):
    """'Sep-30' / 'Oct-16' / '7/22' / '7/20 (TODAY)' -> (iso, dte) or (None,None)."""
    if not tok:
        return None, None
    t = tok.strip().replace("**", "")
    t = re.sub(r"\(.*?\)", "", t).strip()  # drop '(TODAY)' etc.
    iso = None
    m = re.match(r"([A-Z][a-z]{2})-(\d{1,2})", t)          # Sep-30
    if m and m.group(1) in MONTHS:
        mo, dy = MONTHS[m.group(1)], int(m.group(2))
        yr = asof.year if mo >= asof.month else asof.year + 1
        iso = date(yr, mo, dy)
    if iso is None:
        m = re.match(r"(\d{1,2})/(\d{1,2})", t)             # 7/22
        if m:
            mo, dy = int(m.group(1)), int(m.group(2))
            yr = asof.year if mo >= asof.month else asof.year + 1
            iso = date(yr, mo, dy)
    if iso is None:
        m = re.match(r"([A-Z][a-z]{2})-(\d{4})", t)         # Jan-2027 style
        if m and m.group(1) in MONTHS:
            iso = date(int(m.group(2)), MONTHS[m.group(1)], 1)
    if iso is None:
        return None, None
    return iso.isoformat(), (iso - asof).days


def _cells(line):
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    return parts


def extract(text, asof):
    rows, warnings = [], []
    lines = text.splitlines()
    section = subsec = None
    i = 0
    in_region = False
    while i < len(lines):
        ln = lines[i]
        if POS_SECTION_RE.match(ln):
            in_region = True
            section = POS_SECTION_RE.match(ln).group(1)
            subsec = None
        elif ln.startswith("## "):  # any other ## header ends the position region
            in_region = False
        elif SUBSEC_RE.match(ln):
            subsec = SUBSEC_RE.match(ln).group(1)
        # table header row followed by a |---| divider
        if in_region and ln.lstrip().startswith("|") and i + 1 < len(lines) \
                and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            header = [h.lower() for h in _cells(ln)]
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = _cells(lines[i])
                if len(cells) == len(header):
                    try:
                        r = _normalize(header, cells, section, subsec, asof)
                        if r is not None:
                            rows.append(r)
                    except Exception as e:  # never drop silently
                        warnings.append(f"{section}/{subsec}: unparsed row {cells!r} ({e})")
                else:
                    warnings.append(f"{section}/{subsec}: column-count mismatch {cells!r}")
                i += 1
            continue
        i += 1
    return rows, warnings


def _get(header, cells, *names):
    for n in names:
        if n in header:
            return cells[header.index(n)]
    return None


def _normalize(header, cells, section, subsec, asof):
    if not any(c.strip() for c in cells):  # blank continuation row -> skip
        return None
    ticker = _get(header, cells, "ticker")
    typ = _get(header, cells, "type")
    strike = _get(header, cells, "strike")
    expiry_tok = _get(header, cells, "expiry")
    # Robinhood table: the "Position" col carries "QQQ $696P" (ticker + strike)
    pos = _get(header, cells, "position")
    if pos and not ticker:
        mp = re.match(r"(\**)([A-Z]+)\s*(\$?[\d.]+[CP])?", pos.replace("**", ""))
        if mp:
            ticker = mp.group(2)
            if mp.group(3) and not strike:
                strike = mp.group(3)
    # ticker-less strike tables: pull the ticker from the ### subsection ("TLT — ...")
    if not ticker and subsec:
        ticker = re.split(r"[ —\-]", subsec.strip())[0]
    # 'Type' may itself be "$65C Sep-30" (Longs table) -> split
    if typ and not strike and (typ.startswith("$") or "C " in typ or "P " in typ):
        mt = re.match(r"(\$?[\d.]+[CP])\s+([A-Za-z0-9/\-]+)", typ.replace("**", ""))
        if mt:
            strike, expiry_tok = mt.group(1), mt.group(2)
            typ = "Option"
    iso, dte = _parse_expiry(expiry_tok, asof)
    instrument = "Stock" if (typ and typ.lower() == "stock") else \
        " ".join(x for x in [strike, expiry_tok] if x)
    return {
        "group": (subsec or section or "").strip(),
        "ticker": (ticker or "").replace("**", "").strip(),
        "instrument": instrument.replace("**", "").strip() or (typ or ""),
        "expiry_iso": iso,
        "dte": dte,
        "qty": _get(header, cells, "qty"),
        "cost": _num(_get(header, cells, "cost")),
        "mark": _num(_get(header, cells, "mark", "mark 7/20")),
        "value": _num(_get(header, cells, "value")),
        "pnl": (_get(header, cells, "p&l", "p&l (rh display)") or "").replace("**", "").strip(),
        "note": (_get(header, cells, "owner note", "note") or "").strip(),
        "section": section,
    }


def render(rows, warnings, asof):
    out = []
    out.append(f"POSITIONS from FORGE/STATUS.md  (as-of DTE ref {asof.isoformat()})")
    out.append("=" * 72)
    cur = None
    for r in rows:
        if r["group"] != cur:
            cur = r["group"]
            out.append(f"\n▸ {cur}")
        dte = f"{r['dte']}d" if r["dte"] is not None else "—"
        tick = f"{r['ticker']:<6}"
        inst = f"{r['instrument']:<16}"
        out.append(f"  {tick} {inst} qty={str(r['qty'] or ''):<6} "
                   f"mark={str(r['mark'] if r['mark'] is not None else ''):<6} "
                   f"val={str(r['value'] if r['value'] is not None else ''):<7} "
                   f"pnl={r['pnl']:<9} exp={r['expiry_iso'] or '—'} dte={dte}")
    out.append(f"\nParsed {len(rows)} rows.")
    if warnings:
        out.append(f"\n⚠ WARNINGS ({len(warnings)}) — parse gaps, verify vs FORGE:")
        out.extend(f"  - {w}" for w in warnings)
    else:
        out.append("No parse warnings — all position rows mapped.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Extract positions from FORGE/STATUS.md")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--asof", help="DTE reference date YYYY-MM-DD (default today)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if not FORGE_STATUS.exists():
        print(f"ERROR: {FORGE_STATUS} not found — cannot source positions.", file=sys.stderr)
        return 2
    asof = datetime.strptime(args.asof, "%Y-%m-%d").date() if args.asof else date.today()
    text = FORGE_STATUS.read_text(encoding="utf-8")
    rows, warnings = extract(text, asof)

    if args.selftest:
        ok = len(rows) >= 15 and not warnings
        print(f"positions_from_forge SELFTEST: {'PASS' if ok else 'CHECK'} "
              f"({len(rows)} rows, {len(warnings)} warnings)")
        return 0 if ok else 1
    if args.json:
        print(json.dumps({"asof": asof.isoformat(), "rows": rows, "warnings": warnings}, indent=2))
    else:
        print(render(rows, warnings, asof))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
