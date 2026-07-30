#!/usr/bin/env python3
"""
positions_from_forge.py — extract Will's positions from FORGE/STATUS.md into a
clean, normalized structure for the TERRY desk dashboard (PROME suggestion #6,
2026-07-20). Kills the re-key-from-screenshots transcription risk: FORGE/STATUS.md
is the fleet's PROME-reconciled broker mirror (refreshed on each Will export), so
one reconcile feeds both surfaces.

What it does: walks the markdown position tables under "## Fidelity — …" and
"## Robinhood …", maps each table's own header row to fields, and emits normalized
rows: group / ticker / instrument / expiry / qty / cost / mark / value / pnl / dte /
note. Option rows get days-to-expiry (DTE) vs --asof (default: today).

DESIGN: fail LOUD, never fabricate. A row it cannot parse — or that it can parse
but cannot VOUCH for — is reported in `WARNINGS` and withheld from the live set,
never emitted silently (PROME: "if FORGE format quirks block parsing, flag me —
do not fork a second position record").

⚠️ HARDENED 2026-07-30 (TERRY, after DAEDALUS FORGE-audit §S3 caught it emitting
the CLOSED VIXCS spread as an OPEN position while printing "no parse warnings").
The v1 failure was not detection — it was that the docstring promised loud failure
and no guard implemented it (`finding_test_the_guard_not_just_the_guarded`, n+1).
Five hardenings, each with a selftest:
  1. Markdown emphasis stripped from every cell (`**`, `~~`, backticks).
  2. `~~struck~~` in the identity cell => CLOSED. Withheld from the live set.
  3. Column keys match by PREFIX — `Mark 7/30`, `Mark 7/20`, `Mark` all bind.
  4. "Event boxes" is a distinct CLASS (dated, dies on the clock) — never a live
     position, regardless of strikethrough.
  5. HARD ASSERT: a row emitted live must have a non-empty ticker AND a non-null
     mark, when its table HAS a mark column. Tables with no mark column at all
     (e.g. the unverified Robinhood block) are emitted as class `unverified`,
     which is honest rather than silently mark-less.

Usage (repo-root-relative — PAT-031, always wrap):
  (cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/positions_from_forge.py)
  ... --json                 # machine-readable  {live, withheld, warnings}
  ... --asof 2026-07-20      # DTE reference date (default today)
  ... --all                  # also print withheld rows with their reasons
  ... --selftest             # live-file parse-check + synthetic bad-row injection
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

POS_SECTION_RE = re.compile(r"^##\s+(Fidelity|Robinhood)\b", re.I)
SUBSEC_RE = re.compile(r"^###\s+(.+)$")
# a ## header that is a Fidelity/Robinhood section but NOT a live-position class
EVENT_BOX_RE = re.compile(r"^##\s+.*\bevent\s+box", re.I)
# words in a State/Outcome cell that mean "this is not a live position"
DEAD_RE = re.compile(r"\b(closed|expired|realized|assigned|exercised)\b", re.I)


def _md(s):
    """Strip markdown emphasis/backticks. '**15**' -> '15', '~~4~~' -> '4'."""
    if s is None:
        return None
    return (s.replace("~~", "").replace("**", "").replace("`", "")
             .replace("★", "").strip())


def _is_struck(s):
    """True if the cell is (or contains) a ~~strikethrough~~ — FORGE's CLOSED marker."""
    return bool(s) and "~~" in s


def _num(s):
    """Loose numeric parse: '$333.74' -> 333.74, '−69.3%' -> -69.3, '3 (M)' -> 3."""
    if s is None:
        return None
    t = _md(s).replace("−", "-").replace(",", "").replace("$", "").replace("%", "")
    m = re.search(r"-?\d+(?:\.\d+)?", t)
    return float(m.group()) if m else None


def _parse_expiry(tok, asof):
    """'Sep-30' / 'Oct-16' / '7/22' / 'Aug-05-2026' -> (iso, dte) or (None,None)."""
    if not tok:
        return None, None
    t = _md(tok)
    t = re.sub(r"\(.*?\)", "", t)
    t = re.sub(r"[—–-]{1,2}\s*(EXPIRES|EXPIRED).*$", "", t, flags=re.I).strip()
    iso = None
    m = re.match(r"([A-Z][a-z]{2})-(\d{1,2})-(\d{4})", t)            # Aug-05-2026
    if m and m.group(1) in MONTHS:
        iso = date(int(m.group(3)), MONTHS[m.group(1)], int(m.group(2)))
    if iso is None:
        m = re.match(r"([A-Z][a-z]{2})-(\d{1,2})(?!\d)", t)          # Sep-30
        if m and m.group(1) in MONTHS:
            mo, dy = MONTHS[m.group(1)], int(m.group(2))
            yr = asof.year if mo >= asof.month else asof.year + 1
            iso = date(yr, mo, dy)
    if iso is None:
        m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", t)              # 1/15/2027
        if m:
            iso = date(int(m.group(3)), int(m.group(1)), int(m.group(2)))
    if iso is None:
        m = re.match(r"(\d{1,2})/(\d{1,2})(?!/)", t)                 # 7/22
        if m:
            mo, dy = int(m.group(1)), int(m.group(2))
            yr = asof.year if mo >= asof.month else asof.year + 1
            iso = date(yr, mo, dy)
    if iso is None:
        m = re.match(r"([A-Z][a-z]{2})-(\d{4})", t)                  # Jan-2027
        if m and m.group(1) in MONTHS:
            iso = date(int(m.group(2)), MONTHS[m.group(1)], 1)
    if iso is None:
        return None, None
    return iso.isoformat(), (iso - asof).days


def _clean_expiry_token(tok):
    """'Jul-30-2026 — ★ EXPIRES TODAY' -> 'Jul-30-2026'. Display only."""
    if not tok:
        return None
    t = _md(tok)
    t = re.sub(r"\s*[—–-]{1,2}\s*(★\s*)?(EXPIRES|EXPIRED|TODAY).*$", "", t, flags=re.I)
    return re.sub(r"\(.*?\)", "", t).strip() or None


def _first_pct(s):
    """'+$403.11 / +116.2% — long prose' -> 116.2 ; '−0.2%' -> -0.2."""
    if not s:
        return None
    m = re.search(r"([+\-−]?[\d,]+(?:\.\d+)?)\s*%", s.replace("−", "-"))
    return float(m.group(1).replace(",", "").replace("−", "-")) if m else None


def _short(s, n):
    """Leading scalar part of a cell that may carry paragraphs of commentary."""
    if not s:
        return ""
    head = re.split(r"\s+[—–]\s+", s, maxsplit=1)[0].strip()
    return head if len(head) <= n else head[: n - 1] + "…"


def _tail(s):
    """The commentary that followed the scalar, if any — preserved, not discarded."""
    if not s:
        return ""
    parts = re.split(r"\s+[—–]\s+", s, maxsplit=1)
    return parts[1].strip() if len(parts) > 1 else ""


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _get(header, cells, *names):
    """Exact match first, then PREFIX match — so 'Mark 7/30' binds to 'mark'."""
    for n in names:
        if n in header:
            return cells[header.index(n)]
    for n in names:
        for j, h in enumerate(header):
            if h.startswith(n):
                return cells[j]
    return None


def _has_col(header, *names):
    return any(n in header or any(h.startswith(n) for h in header) for n in names)


def extract(text, asof):
    live, withheld, warnings = [], [], []
    lines = text.splitlines()
    section = subsec = None
    section_class = "position"
    in_region = False
    i = 0
    while i < len(lines):
        ln = lines[i]
        if POS_SECTION_RE.match(ln):
            in_region = True
            section = POS_SECTION_RE.match(ln).group(1)
            subsec = None
            section_class = "event_box" if EVENT_BOX_RE.match(ln) else "position"
        elif ln.startswith("## "):
            in_region = False
        elif SUBSEC_RE.match(ln):
            subsec = _md(SUBSEC_RE.match(ln).group(1))

        if in_region and ln.lstrip().startswith("|") and i + 1 < len(lines) \
                and re.match(r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            header = [h.lower() for h in _cells(_md(ln) or ln)]
            table_has_mark = _has_col(header, "mark")
            i += 2
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                raw = _cells(lines[i])
                if len(raw) == len(header):
                    try:
                        r = _normalize(header, raw, section, subsec, asof,
                                       section_class, table_has_mark)
                        if r is not None:
                            (live if r["status"] == "live" else withheld).append(r)
                            if r["status"] == "defect":
                                warnings.append(
                                    f"{r['group']}: {r['reason']} -> WITHHELD {raw!r}")
                    except Exception as e:
                        warnings.append(f"{section}/{subsec}: unparsed row {raw!r} ({e})")
                else:
                    warnings.append(f"{section}/{subsec}: column-count mismatch {raw!r}")
                i += 1
            continue
        i += 1
    return live, withheld, warnings


def _normalize(header, raw, section, subsec, asof, section_class, table_has_mark):
    if not any(c.strip() for c in raw):
        return None
    cells = [_md(c) for c in raw]

    ticker = _get(header, cells, "ticker")
    typ = _get(header, cells, "type")
    strike = _get(header, cells, "strike")
    expiry_tok = _get(header, cells, "expiry")
    pos = _get(header, cells, "position")
    state = _get(header, cells, "state", "outcome")

    # identity cell carries the CLOSED marker in FORGE
    ident_raw = _get(header, raw, "position", "ticker", "strike") or ""
    struck = _is_struck(ident_raw)

    if pos and not ticker:
        mp = re.match(r"([A-Z]{1,6})\s*(\$?[\d.]+[CP])?", pos)
        if mp:
            ticker = mp.group(1)
            if mp.group(2) and not strike:
                strike = mp.group(2)
    if not ticker and subsec:
        ticker = re.split(r"[ —\-]", subsec.strip())[0]
    if typ and not strike and (typ.startswith("$") or "C " in typ or "P " in typ):
        mt = re.match(r"(\$?[\d.]+[CP])\s+([A-Za-z0-9/\-]+)", typ)
        if mt:
            strike, expiry_tok = mt.group(1), mt.group(2)
            typ = "Option"

    iso, dte = _parse_expiry(expiry_tok, asof)
    # FORGE annotates expiry cells ("Jul-30-2026 — ★ EXPIRES TODAY") and P&L cells
    # (a number followed by paragraphs of owner commentary). Keep the full text on
    # `note`/`pnl_raw`; give the dashboard clean scalars.
    exp_clean = _clean_expiry_token(expiry_tok)
    instrument = "Stock" if (typ and typ.lower() == "stock") else \
        " ".join(x for x in [strike, exp_clean] if x)
    mark = _num(_get(header, cells, "mark"))
    pnl_raw = (_get(header, cells, "p&l") or "").strip()

    row = {
        "group": (subsec or section or "").strip(),
        "section": section,
        "class": section_class,
        "ticker": (ticker or "").strip(),
        "instrument": (instrument or "").strip() or (typ or ""),
        "expiry_iso": iso,
        "dte": dte,
        "qty_raw": _get(header, cells, "qty"),
        "qty": _num(_get(header, cells, "qty")),
        "cost": _num(_get(header, cells, "cost")),
        "mark": mark,
        "value": _num(_get(header, cells, "value")),
        "pnl_pct": _first_pct(pnl_raw),
        "pnl": _short(pnl_raw, 22),
        "pnl_raw": pnl_raw,
        "note": (_get(header, cells, "owner note", "note") or "").strip() or _tail(pnl_raw),
        "status": "live",
        "reason": "",
    }

    # ---- classification, most-conclusive first -------------------------------
    if section_class == "event_box":
        row["status"], row["reason"] = "event_box", \
            "Event-box class: dated, dies on the clock — never a standing position"
    elif struck:
        row["status"], row["reason"] = "closed", "row struck through (~~) in FORGE = CLOSED"
    elif state and DEAD_RE.search(state):
        row["status"], row["reason"] = "closed", f"state/outcome says {state.strip()!r}"
    elif not table_has_mark:
        row["status"], row["reason"] = "unverified", \
            "table carries no Mark column — cannot be marked, do not treat as valued"
    # ---- HARD ASSERTS on anything still claiming to be live -------------------
    elif not row["ticker"]:
        row["status"], row["reason"] = "defect", "empty ticker on a row claiming to be live"
    elif row["mark"] is None:
        row["status"], row["reason"] = "defect", \
            "null mark on a row claiming to be live (mark column exists but did not bind)"
    elif dte is not None and dte < 0:
        row["status"], row["reason"] = "closed", f"expiry {iso} already passed ({dte}d)"
    return row


def render(live, withheld, warnings, asof, show_all=False):
    out = [f"POSITIONS from FORGE/STATUS.md  (as-of DTE ref {asof.isoformat()})", "=" * 72]
    cur = None
    for r in live:
        if r["group"] != cur:
            cur = r["group"]
            out.append(f"\n▸ {cur}")
        dte = f"{r['dte']}d" if r["dte"] is not None else "—"
        out.append(f"  {r['ticker']:<6} {r['instrument']:<18} "
                   f"qty={str(r['qty_raw'] or ''):<7} mark={r['mark']:<7} "
                   f"val={str(r['value'] if r['value'] is not None else ''):<8} "
                   f"pnl={r['pnl']:<9} exp={r['expiry_iso'] or '—'} dte={dte}")
    out.append(f"\nLIVE positions: {len(live)}   |   WITHHELD: {len(withheld)}")

    if withheld:
        byc = {}
        for r in withheld:
            byc.setdefault(r["status"], []).append(r)
        out.append("\nWITHHELD from the live set (by design — not silently dropped):")
        for k in sorted(byc):
            out.append(f"  [{k}] {len(byc[k])}")
            if show_all:
                for r in byc[k]:
                    who = f"{r['ticker'] or '?'} {r['instrument']}".strip()
                    out.append(f"      - {who:<34} {r['reason']}")
    if warnings:
        out.append(f"\n⚠ WARNINGS ({len(warnings)}) — DEFECTS, verify vs FORGE before use:")
        out.extend(f"  - {w}" for w in warnings)
    else:
        out.append("\nNo parse defects.")
    return "\n".join(out)


BAD_ROW_FIXTURE = """
## Fidelity — Longs
| Ticker | Type | Qty | Cost | Mark 7/30 | Value | P&L | Owner note |
|---|---|---|---|---|---|---|---|
| **GOOD** | Stock | **15** | $100 | $110 | $1650 | +10% | fine |
| | Stock | 3 | $100 | $110 | $330 | +10% | MISSING TICKER |
| **NOMARK** | Stock | 2 | $100 |  | $200 | +0% | MISSING MARK |
| ~~**DEAD**~~ | Stock | ~~4~~ | $100 | $110 | $440 | +10% | struck = closed |

## Fidelity — Event boxes (dated, mandatory-exit — NOT thesis positions)
| Position | Expiry | Qty | Cost | Outcome |
|---|---|---|---|---|
| ~~**VIX $20C/$25C spread**~~ | Aug-05-2026 | ~~4~~ | $0.70 | **CLOSED** |
"""


def _selftest(asof):
    ok = True
    print("positions_from_forge SELFTEST")
    print("-" * 60)

    # --- 1. synthetic bad-row injection: do the guards actually FIRE? ---------
    live, withheld, warnings = extract(BAD_ROW_FIXTURE, asof)
    tickers = {r["ticker"] for r in live}
    checks = [
        ("good row survives", tickers == {"GOOD"}),
        ("markdown stripped from qty", any(r["qty"] == 15 for r in live)),
        ("'Mark 7/30' binds by prefix", all(r["mark"] == 110 for r in live)),
        ("missing ticker -> defect", any(r["status"] == "defect"
                                         and "ticker" in r["reason"] for r in withheld)),
        ("missing mark -> defect", any(r["status"] == "defect"
                                       and "mark" in r["reason"] for r in withheld)),
        ("struck row -> closed", any(r["status"] == "closed" for r in withheld)),
        ("event box -> event_box", any(r["status"] == "event_box" for r in withheld)),
        ("defects raise warnings", len(warnings) == 2),
    ]
    for label, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
        ok &= passed

    # --- 2. live file ---------------------------------------------------------
    if FORGE_STATUS.exists():
        L, W, warn = extract(FORGE_STATUS.read_text(encoding="utf-8"), asof)
        vix_live = any("VIX" in (r["ticker"] or "") for r in L)
        nulls = [r for r in L if r["mark"] is None or not r["ticker"]]
        live_checks = [
            (f"live file parses ({len(L)} live / {len(W)} withheld)", len(L) >= 10),
            ("CLOSED VIXCS spread NOT in live set", not vix_live),
            ("no null ticker/mark in live set", not nulls),
            ("no parse defects", not warn),
        ]
        for label, passed in live_checks:
            print(f"  [{'PASS' if passed else 'FAIL'}] {label}")
            ok &= passed
        if warn:
            for w in warn:
                print(f"        ! {w}")
    else:
        print("  [SKIP] live FORGE/STATUS.md not found")

    print("-" * 60)
    print(f"SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Extract positions from FORGE/STATUS.md")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--asof", help="DTE reference date YYYY-MM-DD (default today)")
    ap.add_argument("--all", action="store_true", help="detail every withheld row")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    asof = datetime.strptime(args.asof, "%Y-%m-%d").date() if args.asof else date.today()
    if args.selftest:
        return _selftest(asof)

    if not FORGE_STATUS.exists():
        print(f"ERROR: {FORGE_STATUS} not found — cannot source positions.", file=sys.stderr)
        return 2
    live, withheld, warnings = extract(FORGE_STATUS.read_text(encoding="utf-8"), asof)

    if args.json:
        print(json.dumps({"asof": asof.isoformat(), "live": live,
                          "withheld": withheld, "warnings": warnings}, indent=2))
    else:
        print(render(live, withheld, warnings, asof, show_all=args.all))
    # non-zero exit when a row claiming to be live failed a hard assert
    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
