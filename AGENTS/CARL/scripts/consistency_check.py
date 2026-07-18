#!/usr/bin/env python3
r"""
CARL Consistency Checker — Phase 1 (Check A only)

Mechanizes the "value-mirror-drift" class: catches when a canonical value and
its STATUS.md mirror silently disagree. The manual closeout step-15 check only
re-tests rows edited that session; pre-existing drift stays invisible (Jun-8
2026 found 7 accumulated STATUS<->PREDICTIONS deltas). This automates the scan.

Spec: AGENTS/CARL/scripts/CONSISTENCY_CHECK_SPEC.md
This file implements **Check A** only (Phase 1). Checks B (score/matrix) and
C (catalyst set) plus boot wiring are later phases and are NOT built here.

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
  exit 0 when zero HARD findings (soft warns still allow 0? see below);
  exit 1 when any HARD finding — boot/CI friendly.
  Per spec the eventual boot wiring is warn-and-surface (exit 0); Phase 1 keeps
  the stricter exit-1-on-hard-drift contract requested for the standalone/CI
  use, which the later boot step can choose to ignore. --quiet trims the intro.

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
        rows[pid] = {
            "confidence": extract_confidence(raw_conf),
            "timeframe": normalize_timeframe(raw_tf),
            "status": get("Status").upper(),
            "raw_conf": raw_conf,
            "raw_tf": raw_tf,
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


def _fmt_conf(c):
    return "N/A" if c is None else f"{c}%"


# --------------------------------------------------------------------------
# Reporting
# --------------------------------------------------------------------------
def print_report(findings, tsv, status_open, quiet=False):
    hard = [f for f in findings if f[0] == "HARD"]
    soft = [f for f in findings if f[0] == "SOFT"]

    if not quiet:
        print(f"\n{'=' * 72}")
        print(f"  CARL CONSISTENCY CHECK — Check A (Predictions mirror)")
        print(f"{'=' * 72}")
        print(f"  Canonical : thesis/PREDICTIONS.tsv "
              f"({sum(1 for v in tsv.values() if v['status'] == 'OPEN')} OPEN "
              f"/ {len(tsv)} total)")
        print(f"  Mirror    : STATUS.md '## PREDICTIONS' Open table "
              f"({len(status_open)} rows)")

    if not findings:
        print(f"\n  ✅ CHECK-A clean — PREDICTIONS.tsv and STATUS.md agree.")
        print(f"\n  SUMMARY: 0 hard, 0 soft\n")
        return

    print(f"\n  {'SEV':<5} {'PRED':<8} FINDING")
    print(f"  {'-' * 66}")
    for sev, pid, msg in findings:
        mark = "\U0001f534" if sev == "HARD" else "⚠️ "
        print(f"  {mark} {sev:<4} {pid:<8} {msg}")

    print(f"\n  SUMMARY: {len(hard)} hard, {len(soft)} soft")
    if hard:
        print(f"  ❌ {len(hard)} HARD drift(s) — canonical/mirror disagree; "
              f"fix the STATUS mirror (canonical wins).\n")
    else:
        print(f"  (soft-only: timeframe/annotation differences, no hard drift)\n")


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="CARL consistency checker (Phase 1: Check A).")
    ap.add_argument("--quiet", action="store_true", help="summary + findings only")
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
    findings = check_a(tsv, status_open, status_resolved)
    print_report(findings, tsv, status_open, quiet=args.quiet)

    hard = [f for f in findings if f[0] == "HARD"]
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
