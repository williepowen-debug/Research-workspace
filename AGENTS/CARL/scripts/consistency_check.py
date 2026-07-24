#!/usr/bin/env python3
r"""
CARL Consistency Checker — Checks A + D + E

Mechanizes the "value-mirror-drift" class: catches when a canonical value and
its STATUS.md mirror silently disagree. The manual closeout step-15 check only
re-tests rows edited that session; pre-existing drift stays invisible (Jun-8
2026 found 7 accumulated STATUS<->PREDICTIONS deltas). This automates the scan.

Spec: AGENTS/CARL/scripts/CONSISTENCY_CHECK_SPEC.md
Implemented here: **Check A** (Phase 1), plus **Checks D and E** (Phase 4).
Checks B (score/matrix) and C (catalyst set) remain unbuilt.

Phase 4 exists because of two coherence bugs found on 2026-07-24, neither of
which any single-file review could have caught:

  BUG 1 — a vector downgrade was armed against an instrument that does not
  publish the series the vector's own trigger names (V2 Subprime Auto 60+
  resolves on the Fitch ATR monthly index; it was armed against the NY Fed
  HHDC, which publishes only a BLENDED auto series and no subprime series at
  all).  The vector definition lived in THESIS.md and the arming happened in
  STATUS.md, so neither file was wrong on its own.

  BUG 2 — a monotonicity violation ACROSS the parent and sub-agent ledgers:
  POP-P06 (SBA 7(a) default >5% by Q4-2026) sat at 50% while CARL's CRL-15
  (>6.5%, SAME series, SAME date) sat at 65%.  That is impossible — >5% is
  strictly implied by >6.5%, so P(>5%) >= P(>6.5%).  Each ledger was
  internally consistent; the violation exists only in the pair, and the
  two-tier structure guarantees nobody reads both at once.

--------------------------------------------------------------------------
CHECK A — Predictions mirror
  Canonical:  thesis/PREDICTIONS.tsv   (Pred_ID / Confidence / Timeframe / Status)
  Mirror:     STATUS.md "## PREDICTIONS" section — the **Open** table
              (ID | Prediction | Conf | Timeframe | Current) and the
              **Resolved** table (ID | Prediction | Status).

  Rules (per spec):
    - Every TSV Status=OPEN Pred_ID must appear in the STATUS Open table, and
      every STATUS Open-table ID must exist as an OPEN row in the TSV.  [HARD]
    - A TSV Pred_ID with Status != OPEN must NOT appear in the STATUS Open
      table (stale-open).                                                [HARD]
    - Confidence: numeric %, extracted from both sides, compared.        [HARD]
    - Timeframe: normalized loose compare.                              [SOFT]
    - STATUS-table IDs absent from the TSV are orphan mirror rows.       [HARD]

--------------------------------------------------------------------------
CHECK D — Instrument declaration
  Every OPEN prediction must declare, in the `Instrument` column, WHICH
  published series resolves it, in the form:

      <source> :: <series> :: <op><value>

  e.g.  "SBA :: 7(a) default rate :: >6.5%"

  A blank Instrument on an OPEN row is a HARD finding: it means the
  prediction does not record what would resolve it, which is precisely how
  bug 1 happened.  A malformed Instrument (not 3 '::'-separated parts) is
  SOFT — it is declared but not machine-comparable, so Check E can't use it.
  Resolved rows are exempt from the HARD rule (declaring them is good
  hygiene for the audit trail, but not required).

  Threshold clauses may be "qualitative" where no numeric bar exists; those
  are accepted by D and skipped by E.

--------------------------------------------------------------------------
CHECK E — Cross-ledger threshold monotonicity
  Groups every prediction — CARL's own ledger AND every
  sub_agents/*/workbook/PREDICTIONS.tsv that carries an Instrument column —
  by (source, series).  Within a group, for rows sharing a normalized
  timeframe and a comparable operator direction:

      for '>' / '>=' :  a HIGHER threshold is STRICTER, so its confidence
                        must be <= the confidence of any lower threshold.
      for '<' / '<=' :  a LOWER threshold is STRICTER, so its confidence
                        must be <= the confidence of any higher threshold.

  A violation is HARD when the two rows share a normalized timeframe, SOFT
  when the timeframes differ (the implication may not hold across horizons,
  so a human decides).  Sub-agent ledgers without an Instrument column are
  reported once as a SOFT coverage gap rather than silently skipped — an
  unscanned ledger must not read as a clean one.

--------------------------------------------------------------------------
NORMALIZATION CHOICES (spec leaves some of this to implementer discretion):

  Confidence — strip markdown (**bold**, arrows up/down), then take the FIRST
    "<int>%" token. This makes "**85%** up" == "85%" and "**62%** down (was 75)"
    == "62%" (the leading figure is the live value; "(was 75)" is history).
    A cell with no %-token and containing "N/A" -> None; None == None is a match.

  Timeframe — SOFT check. Both sides are: lowercased, markdown/asterisks
    stripped, everything from the first ';' or '(' dropped (TSV timeframes
    carry inline reprice annotations like "Jun-Jul 2026; DEEPENED 40->28..."
    that the STATUS mirror deliberately omits), whitespace collapsed, trailing
    punctuation trimmed. If the resulting base strings differ, emit a SOFT warn
    (never a hard fail) — timeframes are intentionally loosely mirrored.

Only IDs matching /^CRL-\d+$/ are treated as predictions; the STATUS "Legacy
confirmed (pre-TSV)" bullet list is intentionally not TSV-backed and is ignored.

--------------------------------------------------------------------------
OUTPUT / EXIT
  Human-readable table of findings + summary line "N hard, M soft".
  exit 0 when zero HARD findings; exit 1 when any HARD finding — CI friendly.
  **--warn-only forces exit 0** while still printing everything: boot.py uses it
  so a real finding surfaces loudly without being rendered as a script FAILURE.
  "the checker found drift" and "the checker crashed" must not look identical in
  the boot summary. Standalone / closeout use keeps the strict exit-1 contract.
  --quiet trims the intro.

Usage:
  .venv/bin/python3 AGENTS/CARL/scripts/consistency_check.py
  .venv/bin/python3 AGENTS/CARL/scripts/consistency_check.py --quiet
  # override inputs (used by the acceptance test against temp copies):
  .venv/bin/python3 AGENTS/CARL/scripts/consistency_check.py --tsv X --status Y
"""

import argparse
import re
import sys
from pathlib import Path

# --- cwd-proof path resolution (resolve from this file, never from cwd) ---
SCRIPTS_DIR = Path(__file__).resolve().parent
CARL_DIR = SCRIPTS_DIR.parent
DEFAULT_TSV = CARL_DIR / "thesis" / "PREDICTIONS.tsv"
DEFAULT_STATUS = CARL_DIR / "STATUS.md"

PRED_ID_RE = re.compile(r"^CRL-\d+$")
PCT_RE = re.compile(r"(\d+)\s*%")


# --------------------------------------------------------------------------
# Normalization helpers
# --------------------------------------------------------------------------
def strip_markdown(text):
    """Remove bold/italic markers and directional arrows from a cell."""
    if text is None:
        return ""
    t = text.replace("**", "").replace("*", "")
    # strip common annotation glyphs (up/down arrows, checks, warning)
    for ch in ("↑", "↓", "↔", "✅", "❌", "⚠", "️",
               "\U0001f534", "\U0001f7e0", "\U0001f7e1", "\U0001f7e2"):
        t = t.replace(ch, "")
    return t.strip()


def extract_confidence(cell):
    """Return int percent (0-100) or None. First %-token wins; else None if N/A."""
    if cell is None:
        return None
    t = strip_markdown(cell)
    m = PCT_RE.search(t)
    if m:
        return int(m.group(1))
    # no percentage — treat explicit N/A as intentional 'no confidence'
    if "n/a" in t.lower():
        return None
    return None


def normalize_timeframe(cell):
    """Loose timeframe base: strip markdown, cut inline annotations, collapse ws."""
    t = strip_markdown(cell).lower()
    # drop everything from the first annotation delimiter
    for delim in (";", "("):
        idx = t.find(delim)
        if idx != -1:
            t = t[:idx]
    t = re.sub(r"\s+", " ", t).strip()
    t = t.strip(" .,-")
    return t


# --------------------------------------------------------------------------
# Parsers
# --------------------------------------------------------------------------
def parse_tsv(path):
    """Parse PREDICTIONS.tsv -> {id: {confidence, timeframe, status, raw_conf, raw_tf}}."""
    rows = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    header = None
    col = {}
    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = line.split("\t")
        if header is None:
            header = fields
            col = {name.strip(): i for i, name in enumerate(header)}
            for req in ("Pred_ID", "Confidence", "Timeframe", "Status"):
                if req not in col:
                    raise SystemExit(f"FATAL: TSV missing required column '{req}' "
                                     f"(have: {list(col)})")
            continue
        pid = fields[col["Pred_ID"]].strip() if len(fields) > col["Pred_ID"] else ""
        if not PRED_ID_RE.match(pid):
            continue

        def get(name):
            i = col[name]
            return fields[i].strip() if len(fields) > i else ""

        raw_conf = get("Confidence")
        raw_tf = get("Timeframe")
        raw_inst = get("Instrument") if "Instrument" in col else None
        rows[pid] = {
            "confidence": extract_confidence(raw_conf),
            "timeframe": normalize_timeframe(raw_tf),
            "status": get("Status").upper(),
            "raw_conf": raw_conf,
            "raw_tf": raw_tf,
            "instrument": raw_inst,
            "has_inst_col": "Instrument" in col,
        }
    return rows


def _split_md_row(line):
    """Split a markdown table row on '|', dropping leading/trailing empties."""
    parts = [c.strip() for c in line.strip().strip("|").split("|")]
    return parts


def parse_status(path):
    """
    Parse STATUS.md predictions section.
    Returns (open_rows, resolved_rows):
      open_rows: {id: {confidence, timeframe, raw_conf, raw_tf}}
      resolved_rows: {id: {raw_status}}
    """
    text = path.read_text(encoding="utf-8").splitlines()

    # Bound the "## PREDICTIONS" section (until next top-level '## ' header).
    start = None
    end = len(text)
    for i, line in enumerate(text):
        if line.strip() == "## PREDICTIONS":
            start = i
            break
    if start is None:
        raise SystemExit("FATAL: '## PREDICTIONS' section not found in STATUS.md")
    for i in range(start + 1, len(text)):
        if text[i].startswith("## "):
            end = i
            break

    open_rows = {}
    resolved_rows = {}
    subsection = None  # 'resolved' | 'open' | None
    for line in text[start:end]:
        low = line.strip().lower()
        if low.startswith("**resolved:") or low.startswith("resolved:"):
            subsection = "resolved"
            continue
        if low.startswith("**open:") or low.startswith("open:"):
            subsection = "open"
            continue
        if not line.lstrip().startswith("|"):
            continue
        cells = _split_md_row(line)
        if not cells:
            continue
        pid = strip_markdown(cells[0])
        if not PRED_ID_RE.match(pid):
            continue  # skips header ("ID") + separator ("----") rows
        if subsection == "open":
            raw_conf = cells[2] if len(cells) > 2 else ""
            raw_tf = cells[3] if len(cells) > 3 else ""
            open_rows[pid] = {
                "confidence": extract_confidence(raw_conf),
                "timeframe": normalize_timeframe(raw_tf),
                "raw_conf": raw_conf,
                "raw_tf": raw_tf,
            }
        elif subsection == "resolved":
            resolved_rows[pid] = {
                "raw_status": cells[2] if len(cells) > 2 else "",
            }
    return open_rows, resolved_rows


# --------------------------------------------------------------------------
# Check A
# --------------------------------------------------------------------------
def check_a(tsv, status_open, status_resolved):
    """Return list of findings: (severity, pred_id, message)."""
    findings = []
    HARD, SOFT = "HARD", "SOFT"

    all_ids = set(tsv) | set(status_open) | set(status_resolved)
    for pid in sorted(all_ids, key=lambda x: (int(x.split("-")[1]))):
        t = tsv.get(pid)
        o = status_open.get(pid)
        r = status_resolved.get(pid)

        # ---- orphan mirror rows (in STATUS, absent from TSV) ----
        if t is None:
            if o is not None:
                findings.append((HARD, pid,
                    "orphan: present in STATUS Open table but not in PREDICTIONS.tsv"))
            if r is not None:
                findings.append((HARD, pid,
                    "orphan: present in STATUS Resolved table but not in PREDICTIONS.tsv"))
            continue

        is_open = (t["status"] == "OPEN")

        # ---- presence ----
        if is_open:
            if o is None:
                findings.append((HARD, pid,
                    "OPEN in TSV but ABSENT from STATUS Open table (unmirrored)"))
            if r is not None:
                findings.append((HARD, pid,
                    "OPEN in TSV but present in STATUS Resolved table (contradiction)"))
        else:  # resolved in TSV
            if o is not None:
                findings.append((HARD, pid,
                    f"resolved in TSV (status={t['status']}) but STILL in STATUS "
                    f"Open table (stale-open)"))
            if r is None:
                findings.append((SOFT, pid,
                    f"resolved in TSV (status={t['status']}) but not listed in "
                    f"STATUS Resolved table"))

        # ---- field agreement (only meaningful when both sides present & open) ----
        if is_open and o is not None:
            if t["confidence"] != o["confidence"]:
                findings.append((HARD, pid,
                    f"confidence drift: TSV={_fmt_conf(t['confidence'])} "
                    f"(raw '{t['raw_conf']}') vs STATUS={_fmt_conf(o['confidence'])} "
                    f"(raw '{o['raw_conf']}')"))
            if t["timeframe"] != o["timeframe"]:
                findings.append((SOFT, pid,
                    f"timeframe differs: TSV='{t['timeframe']}' vs "
                    f"STATUS='{o['timeframe']}'"))

    return findings


# --------------------------------------------------------------------------
# Phase 4 — Instrument parsing shared by Checks D and E
# --------------------------------------------------------------------------
OP_RE = re.compile(r"^(>=|<=|>|<|=)\s*(.+)$")
NUM_RE = re.compile(r"[-+]?[\d,]*\.?\d+")
_MULT = {"k": 1e3, "m": 1e6, "b": 1e9, "bn": 1e9, "t": 1e12}


def parse_instrument(cell):
    """
    '<source> :: <series> :: <op><value>' -> dict or None.
    Returns {'source','series','op','value','qualitative','raw'}.
    value is a float in canonical units where parseable, else None.
    """
    if not cell or not cell.strip():
        return None
    parts = [x.strip() for x in cell.split("::")]
    if len(parts) != 3:
        return {"malformed": True, "raw": cell}
    source, series, thresh = parts
    qualitative = thresh.lower().startswith("qualitative")
    op = value = None
    if not qualitative:
        m = OP_RE.match(thresh)
        if m:
            op = m.group(1)
            rest = m.group(2).strip()
            n = NUM_RE.search(rest.replace(",", ""))
            if n:
                value = float(n.group(0))
                tail = rest[n.end():].strip().lower() if n.end() <= len(rest) else ""
                # scale suffixes: $100B, 500000, +30bps, 1500000
                for suf, mult in _MULT.items():
                    if tail.startswith(suf):
                        value *= mult
                        break
    return {
        "malformed": False,
        "source": source,
        "series": series,
        "op": op,
        "value": value,
        "qualitative": qualitative,
        "raw": cell,
    }


def _series_key(inst):
    return (inst["source"].strip().lower(), inst["series"].strip().lower())


# --------------------------------------------------------------------------
# Check D — instrument declaration
# --------------------------------------------------------------------------
def check_d(tsv):
    """Every OPEN prediction must name the published series that resolves it."""
    findings = []
    HARD, SOFT = "HARD", "SOFT"
    if not any(v.get("has_inst_col") for v in tsv.values()):
        findings.append((SOFT, "-", "PREDICTIONS.tsv has no 'Instrument' column — "
                                    "Check D cannot run (add the column to enable it)"))
        return findings
    for pid in sorted(tsv, key=lambda x: int(x.split("-")[1])):
        v = tsv[pid]
        inst = parse_instrument(v.get("instrument"))
        is_open = v["status"] == "OPEN"
        if inst is None:
            if is_open:
                findings.append((HARD, pid,
                    "OPEN but no Instrument declared — nothing records which published "
                    "series resolves it (this is the bug-1 class)"))
            continue
        if inst.get("malformed"):
            findings.append((SOFT, pid,
                f"Instrument malformed (need '<source> :: <series> :: <op><value>'): "
                f"'{inst['raw'][:60]}'"))
            continue
        if is_open and not inst["qualitative"] and inst["op"] is None:
            findings.append((SOFT, pid,
                f"Instrument threshold clause not parseable as <op><value> "
                f"(Check E will skip it): '{inst['raw'].split('::')[-1].strip()[:40]}'"))
    return findings


# --------------------------------------------------------------------------
# Check E — cross-ledger threshold monotonicity
# --------------------------------------------------------------------------
def collect_ledgers(carl_tsv_path, carl_rows):
    """
    Returns (entries, coverage_gaps).
    entries: list of dicts {ledger, pid, confidence, timeframe, inst, status}
    coverage_gaps: [(ledger_name, reason)] for ledgers that could not be scanned.
    """
    entries, gaps = [], []

    def add(ledger, rows):
        for pid, v in rows.items():
            inst = parse_instrument(v.get("instrument"))
            if not inst or inst.get("malformed"):
                continue
            entries.append({
                "ledger": ledger, "pid": pid, "confidence": v["confidence"],
                "timeframe": v["timeframe"], "inst": inst, "status": v["status"],
            })

    add("CARL", carl_rows)

    sub_glob = sorted((CARL_DIR / "sub_agents").glob("*/workbook/PREDICTIONS.tsv"))
    for sp in sub_glob:
        name = sp.parts[-3]
        try:
            rows = parse_sub_tsv(sp)
        except Exception as exc:                      # noqa: BLE001
            gaps.append((name, f"unreadable ({exc.__class__.__name__})"))
            continue
        if rows is None:
            gaps.append((name, "no 'Instrument' column — ledger NOT scanned"))
            continue
        add(name, rows)
    return entries, gaps


def parse_sub_tsv(path):
    """
    Sub-agent ledgers use their own Pred_ID prefix and may lack columns.
    Returns {} / rows dict, or None if there is no Instrument column.
    """
    rows = {}
    header, col = None, {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        fields = line.split("\t")
        if header is None:
            header = fields
            col = {n.strip(): i for i, n in enumerate(header)}
            if "Instrument" not in col:
                return None
            continue
        def get(name):
            i = col.get(name, -1)
            return fields[i].strip() if 0 <= i < len(fields) else ""
        pid = get("Pred_ID")
        if not pid or pid.startswith("#"):
            continue
        rows[pid] = {
            "confidence": extract_confidence(get("Confidence")),
            "timeframe": normalize_timeframe(get("Timeframe")),
            "status": get("Status").upper(),
            "instrument": get("Instrument"),
        }
    return rows


def check_e(entries, gaps):
    """
    Nested thresholds on one series must carry monotone confidence.

    Returns (findings, stats).  stats exists so a CLEAN result carries its own
    coverage evidence: a check that compared nothing must not read the same as a
    check that compared everything and found no violation.  (False-zero guard —
    a tool scanning the wrong slice manufactures a clean bill of health.)
    """
    findings = []
    HARD, SOFT = "HARD", "SOFT"

    for name, reason in gaps:
        findings.append((SOFT, name, f"coverage gap: {reason}"))

    groups = {}
    skipped_qual = skipped_noconf = 0
    for e in entries:
        if e["inst"]["qualitative"] or e["inst"]["value"] is None:
            skipped_qual += 1
            continue
        if e["confidence"] is None:
            skipped_noconf += 1
            continue
        groups.setdefault(_series_key(e["inst"]), []).append(e)

    multi = {k: v for k, v in groups.items() if len(v) > 1}
    stats = {
        "entries": len(entries),
        "comparable": sum(len(v) for v in groups.values()),
        "skipped_qualitative": skipped_qual,
        "skipped_no_conf": skipped_noconf,
        "series": len(groups),
        "compared_groups": len(multi),
        "compared_pairs": sum(len(v) * (len(v) - 1) // 2 for v in multi.values()),
        "group_names": sorted(f"{k[0]} :: {k[1]} ({len(v)})" for k, v in multi.items()),
        "ledgers_scanned": sorted({e["ledger"] for e in entries}),
        "gaps": [g[0] for g in gaps],
    }

    for key, rows in sorted(groups.items()):
        if len(rows) < 2:
            continue
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                a, b = rows[i], rows[j]
                oa, ob = a["inst"]["op"], b["inst"]["op"]
                if oa is None or ob is None:
                    continue
                dir_a = ">" if oa.startswith(">") else ("<" if oa.startswith("<") else None)
                dir_b = ">" if ob.startswith(">") else ("<" if ob.startswith("<") else None)
                if dir_a is None or dir_a != dir_b:
                    continue
                va, vb = a["inst"]["value"], b["inst"]["value"]
                if va == vb:
                    continue
                # identify stricter / looser
                if dir_a == ">":
                    strict, loose = (a, b) if va > vb else (b, a)
                else:
                    strict, loose = (a, b) if va < vb else (b, a)
                if strict["confidence"] > loose["confidence"]:
                    same_tf = strict["timeframe"] == loose["timeframe"]
                    sev = HARD if same_tf else SOFT
                    tf_note = ("same timeframe" if same_tf
                               else f"timeframes differ: '{strict['timeframe']}' vs "
                                    f"'{loose['timeframe']}' — human call")
                    findings.append((sev,
                        f"{strict['ledger']}/{strict['pid']}",
                        f"MONOTONICITY: {strict['ledger']}/{strict['pid']} "
                        f"({strict['inst']['op']}{_short(strict['inst']['value'])}) "
                        f"at {strict['confidence']}% EXCEEDS "
                        f"{loose['ledger']}/{loose['pid']} "
                        f"({loose['inst']['op']}{_short(loose['inst']['value'])}) "
                        f"at {loose['confidence']}% on '{key[0]} :: {key[1]}' — "
                        f"the stricter threshold cannot be more likely ({tf_note})"))
    return findings, stats


def _print_e_coverage(s):
    """Coverage evidence for Check E — so 'clean' is never mistaken for 'thorough'."""
    print(f"       coverage: {s['comparable']}/{s['entries']} rows comparable "
          f"({s['skipped_qualitative']} qualitative, {s['skipped_no_conf']} no-confidence) "
          f"across {s['series']} distinct series")
    if s["compared_groups"] == 0:
        print(f"       \u26a0\ufe0f  {s['compared_pairs']} pairs actually compared — "
              f"NO series has 2+ numeric thresholds, so Check E asserted nothing this run. "
              f"'Clean' here means 'nothing to compare', not 'verified consistent'.")
    else:
        print(f"       {s['compared_pairs']} pair(s) compared across "
              f"{s['compared_groups']} multi-threshold series: "
              f"{'; '.join(s['group_names'])}")


def _short(v):
    if v is None:
        return "?"
    if abs(v) >= 1e9:
        return f"{v/1e9:g}B"
    if abs(v) >= 1e6:
        return f"{v/1e6:g}M"
    if abs(v) >= 1e3 and v == int(v):
        return f"{int(v):,}"
    return f"{v:g}"


def _fmt_conf(c):
    return "N/A" if c is None else f"{c}%"


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------
def print_report(groups, tsv, status_open, n_entries, e_stats=None, quiet=False):
    """groups: ordered list of (label, findings)."""
    all_f = [f for _, fs in groups for f in fs]
    hard = [f for f in all_f if f[0] == "HARD"]
    soft = [f for f in all_f if f[0] == "SOFT"]

    if not quiet:
        print(f"\n{'=' * 78}")
        print(f"  CARL CONSISTENCY CHECK — A (mirror) · D (instrument) · E (monotonicity)")
        print(f"{'=' * 78}")
        print(f"  Canonical : thesis/PREDICTIONS.tsv "
              f"({sum(1 for v in tsv.values() if v['status'] == 'OPEN')} OPEN "
              f"/ {len(tsv)} total)")
        print(f"  Mirror    : STATUS.md '## PREDICTIONS' Open table "
              f"({len(status_open)} rows)")
        print(f"  Ledgers   : {n_entries} instrument-declared rows across "
              f"CARL + sub-agents")
        if e_stats:
            print(f"              scanned: {', '.join(e_stats['ledgers_scanned'])}"
                  + (f"  |  NOT scanned: {', '.join(e_stats['gaps'])}"
                     if e_stats["gaps"] else ""))

    for label, fs in groups:
        if not fs:
            print(f"\n  ✅ {label} — clean.")
            if e_stats and label.startswith("CHECK E"):
                _print_e_coverage(e_stats)
            continue
        print(f"\n  {label}")
        print(f"  {'SEV':<5} {'ROW':<16} FINDING")
        print(f"  {'-' * 74}")
        for sev, pid, msg in fs:
            mark = "\U0001f534" if sev == "HARD" else "⚠️ "
            print(f"  {mark} {sev:<4} {pid:<16} {msg}")
        if e_stats and label.startswith("CHECK E"):
            _print_e_coverage(e_stats)

    print(f"\n  SUMMARY: {len(hard)} hard, {len(soft)} soft")
    if hard:
        print(f"  ❌ {len(hard)} HARD finding(s) — fix before commit "
              f"(canonical wins on mirrors; declare the instrument; "
              f"reconcile the monotonicity pair).\n")
    else:
        print(f"  (soft-only — no hard drift)\n")


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="CARL consistency checker — Checks A, D, E.")
    ap.add_argument("--quiet", action="store_true", help="summary + findings only")
    ap.add_argument("--warn-only", action="store_true",
                    help="always exit 0 (findings still print). Used by boot.py so a "
                         "consistency finding surfaces loudly without being reported as a "
                         "script FAILURE — 'drift found' and 'the script broke' are "
                         "different things and must not look the same in the boot summary.")
    ap.add_argument("--tsv", default=str(DEFAULT_TSV), help="override PREDICTIONS.tsv path")
    ap.add_argument("--status", default=str(DEFAULT_STATUS), help="override STATUS.md path")
    args = ap.parse_args()

    tsv_path = Path(args.tsv)
    status_path = Path(args.status)
    if not tsv_path.exists():
        raise SystemExit(f"FATAL: TSV not found: {tsv_path}")
    if not status_path.exists():
        raise SystemExit(f"FATAL: STATUS not found: {status_path}")

    tsv = parse_tsv(tsv_path)
    status_open, status_resolved = parse_status(status_path)

    fa = check_a(tsv, status_open, status_resolved)
    fd = check_d(tsv)
    entries, gaps = collect_ledgers(tsv_path, tsv)
    fe, e_stats = check_e(entries, gaps)

    groups = [
        ("CHECK A — predictions mirror (PREDICTIONS.tsv ↔ STATUS.md)", fa),
        ("CHECK D — instrument declaration (does each OPEN row name what resolves it?)", fd),
        ("CHECK E — cross-ledger threshold monotonicity (parent + sub-agents)", fe),
    ]
    print_report(groups, tsv, status_open, len(entries), e_stats=e_stats,
                 quiet=args.quiet)

    hard = [f for _, fs in groups for f in fs if f[0] == "HARD"]
    if hard and args.warn_only:
        # Leading 🔴 is deliberate: boot.py's KEY_MARKERS filter surfaces this line
        # even in collapsed mode, so a skimmed boot cannot miss it just because the
        # script itself exited 0.
        print(f"  \U0001f534 CONSISTENCY: {len(hard)} HARD FINDING(S) OPEN — "
              f"boot exits 0 (this is a FINDING, not a script failure), but these "
              f"must be fixed before commit. Re-run without --warn-only at closeout.\n")
        return 0
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
