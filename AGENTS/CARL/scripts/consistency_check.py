#!/usr/bin/env python3
r"""
CARL Consistency Checker — Checks A + B + D + E + F + G

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
  Mirror:     PREDICTIONS_MIRROR.md "## PREDICTIONS" section — the **Open** table
              (moved out of STATUS.md 2026-09-01, read-cap remedy; Check B still reads STATUS.md)
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
# 2026-09-01: the PREDICTIONS mirror MOVED OUT of STATUS.md under the read-cap
# ruling (STATUS was 119% of the 54,250 B whole-read cap; that section was 23.7%
# of it). Check A now reads THIS file; Check B (convergence matrix) still reads
# STATUS.md, because the matrix did not move. The move, this re-point and the
# CLAUDE.md Doc Ownership re-point were made in ONE commit deliberately -- a
# relocated mirror whose checker still points at the old location is how a check
# starts passing green against a file nobody updates.
DEFAULT_PRED_MIRROR = CARL_DIR / "PREDICTIONS_MIRROR.md"
DEFAULT_THESIS = CARL_DIR / "thesis" / "THESIS.md"

PRED_ID_RE = re.compile(r"^CRL-\d+$")
# Tolerant form for MIRROR tables: the STATUS ID cell sometimes carries an
# annotation ("**CRL-27** *(NEW 7/24)*").  Matching strictly there makes the row
# read as UNMIRRORED, which is a confusing false positive — the row is present,
# just decorated.  The canonical TSV stays strict.
PRED_ID_LEAD_RE = re.compile(r"^(CRL-\d+)\b")
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
            "prediction": get("Prediction") if "Prediction" in col else "",
            "notes": get("Notes") if "Notes" in col else "",
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
        raise SystemExit(f"FATAL: '## PREDICTIONS' section not found in {path}")
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
        m_pid = PRED_ID_LEAD_RE.match(strip_markdown(cells[0]))
        if not m_pid:
            continue  # skips header ("ID") + separator ("----") rows
        pid = m_pid.group(1)
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
# Check G — registration-time failure-shape lint
# --------------------------------------------------------------------------
# WHY THIS EXISTS. The 2026-07-24 Brier audit found CARL's documented failure
# taxonomy did NOT reduce CARL's failure rate: boot step 7c forces reading the
# MISSED notes every session, and CRL-24 was still registered 2026-06-25 as a
# CONJUNCTION at 60% -- AFTER CRL-01 and CRL-09 were already logged as that exact
# family. **Reading a taxonomy at boot is not applying it at registration.**
# Check G moves the check to the moment the prediction is WRITTEN.
#
# Shapes, each sourced from an actual CARL failure:
#   G1 CONJUNCTION            CRL-24: "NCO >5.5% AND coverage down" at 60%,
#                             when P(A and B) <= min(P(A),P(B))
#   G2 REVISION-PRONE SERIES  CRL-09 (JOLTS ratio), CRL-11 (hires rate revised away)
#   G3 CONFIDENCE >= 75%      the 75-85% band went 0-for-2 ex-ante
#   G4 SEASONAL SERIES, RAW-LEVEL THRESHOLD   CRL-22 v1 (insurer MCR H1->H2),
#                             V2/Fitch ATR (tax-refund dip), RED's diesel-crack falsifier
#   G5 NO NUMERIC BAR         CRL-07: "triggers a DQ spike" -- unfalsifiable by vagueness
#
# ⚠️ RULES ARE TIERED BY MEASURED PRECISION, NOT BY HOW GOOD THEY SOUNDED.
# Validated against CARL's own resolved record (N=10) by asking: does the rule fire
# on the predictions that MISSED, and not on the ones that HIT?
#
#   TIER 1 — G1 (1/1 misses) and G2 (2/2 misses): 100% precision, and independently
#            grounded (conjunction arithmetic; revision is a documented mechanism).
#            These GATE: HARD on a newly-registered prediction.
#   TIER 2 — G3 (2/4), G4 (1/2), G5 (1/2): ~50% precision — they fire on hits as
#            often as misses, so they DO NOT discriminate. **ADVISORY ONLY, never
#            HARD**, and the message says so. They are kept because they encode real
#            lessons, not because they predict outcomes.
#
# Small-N honesty: tier-1 precision rests on N=1 and N=2. The theoretical grounding is
# doing more work than the sample. Re-validate at N~20.
#
# SEVERITY: tier 1 is HARD on NEWLY-REGISTERED predictions (absent from the previous
# commit) -- that is the registration gate -- and SOFT on pre-existing rows, so the
# check gates new work without spamming a standing inventory. Tier 2 is always SOFT.
#
# ESCAPE HATCHES are deliberate and must be written down, not silent: put
# [LEVEL-CONTINUATION] or [MECHANICAL] in Notes to justify G3; [SEASONALITY-MATCHED]
# to clear G4; [CONJUNCTION-PRICED] to clear G1. The point is to force an explicit
# claim at registration, not to forbid the shape.
REVISION_PRONE = ("jolts", "hires rate", "nonfarm", "payroll", "nfp", "quits",
                  "job openings", "lfpr", "labor force participation")
SEASONAL_SERIES = ("delinquency rate", "medical care ratio", "benefit expense ratio",
                   "mcr", "bcr", "crack", "retail sales", "foreclosure")
SEASON_OK = ("yoy", "same-month", "same month", "seasonal", "ttm", "trailing")
# NB: no trailing \b after the unit — '%' is a non-word char, so \b would require a
# word character immediately after it and "13.74% (GFC peak)" would read as NO BAR.
# That bug false-positived 10 of 16 rows on the first run.
NUMERIC_BAR = re.compile(
    r"[<>]=?\s*[-+]?[\d,.]+"                 # >13.74 / <=6.5 / >= 1,500,000
    r"|[-+]?\d[\d,]*(?:\.\d+)?\s*(?:%|bps|bp\b|pp\b)"   # 13.74% / +30bps / 2.2pp
    r"|\$\s?\d[\d,]*(?:\.\d+)?\s*[KMBT]?"                # $4.00 / $100B / $1,500
    r"|\b\d[\d,]{2,}(?:\.\d+)?\s*(?:K|M|B|per|/)"        # 70K/qtr / 2,600,000
)


def _prior_pred_ids(tsv_path):
    """Pred_IDs present in the previous commit. Separate from _prior_confidences:
    a row whose Confidence does not parse (e.g. 'N/A (BROCK's count)') still EXISTS,
    and inferring newness from the confidence map made such rows look newly
    registered on every run."""
    import subprocess
    try:
        root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                            cwd=str(tsv_path.parent), text=True).strip())
        rel = tsv_path.resolve().relative_to(root)
        out = subprocess.check_output(["git", "show", f"HEAD:{rel}"],
                                      cwd=str(tsv_path.parent), text=True,
                                      stderr=subprocess.DEVNULL)
    except Exception:                                  # noqa: BLE001
        return None
    return {ln.split("\t")[0].strip() for ln in out.splitlines()
            if PRED_ID_RE.match(ln.split("\t")[0].strip())}


def check_g(tsv, tsv_path):
    """Registration-time lint for known failure shapes."""
    findings, HARD, SOFT = [], "HARD", "SOFT"
    known = _prior_pred_ids(tsv_path)

    counts = {"new": 0, "scanned": 0, "flagged": set()}
    for pid in sorted(tsv, key=lambda x: int(x.split("-")[1])):
        v = tsv[pid]
        if v["status"] != "OPEN":
            continue
        counts["scanned"] += 1
        is_new = (known is not None) and (pid not in known)
        if is_new:
            counts["new"] += 1
        sev = HARD if is_new else SOFT          # tier 1 only
        adv = SOFT                               # tier 2 never gates
        tag = " [NEWLY REGISTERED]" if is_new else ""
        ADVISORY = " [ADVISORY — this rule measured ~50% precision on CARL's own " \
                   "resolved record; it fires on hits as often as misses]"
        text = (v.get("prediction") or "")
        notes = (v.get("notes") or "")
        inst = (v.get("instrument") or "")
        blob = f"{text} {inst}".lower()
        conf = v["confidence"]

        # G1 — conjunction
        # ⚠️ 2026-09-01: the test used to be `" AND " in text` and MISSED a real
        # conjunction (CRL-29) because this desk's house style bolds it: "**AND**".
        # Markdown emphasis is stripped before the test, so `**AND**`, `*AND*` and
        # `__AND__` all count. A tier-1 HARD gate that any emphasis mark defeats is
        # not a gate. Found by registering CRL-29 and noticing G1 stayed silent.
        text_plain = re.sub(r"[*_`]+", " ", text)
        if re.search(r"\bAND\b", text_plain) and len(NUMERIC_BAR.findall(text)) >= 2 \
                and "[conjunction-priced]" not in notes.lower():
            findings.append((sev, pid,
                f"G1 CONJUNCTION{tag}: two+ thresholds joined by AND. P(A∧B) ≤ min(P(A),P(B)) — "
                f"price it as a conjunction or split it. This is the CRL-24 shape "
                f"(registered at 60%, MISSED). [TIER 1 — 1/1 precision on the resolved record]"))
            counts["flagged"].add(pid)

        # G2 — revision-prone series
        hit = next((k for k in REVISION_PRONE if k in blob), None)
        if hit:
            findings.append((sev, pid,
                f"G2 REVISION-PRONE SERIES{tag}: names '{hit}'. Prints get revised away — "
                f"CRL-11 missed exactly this way (hires 3.2% revised to 3.3%), CRL-09 on the "
                f"denominator. Register at ≤40% or not at all. "
                f"[TIER 1 — 2/2 precision on the resolved record]"))
            counts["flagged"].add(pid)

        # G3 — high confidence without a written justification
        if conf is not None and conf >= 75 \
                and not any(k in notes.lower() for k in ("[level-continuation]", "[mechanical]")):
            findings.append((adv, pid,
                f"G3 CONFIDENCE {conf}% ≥75% with no justification token. The 75-85% band "
                f"went 0-for-2 ex-ante (Brier audit) — but note CRL-04 at 98% HIT, which is why "
                f"this is advisory. Add [LEVEL-CONTINUATION] or [MECHANICAL] to Notes, or cut it."
                + ADVISORY))
            counts["flagged"].add(pid)

        # G4 — seasonal series measured at a raw level
        s_hit = next((k for k in SEASONAL_SERIES if k in blob), None)
        if s_hit and not any(k in blob for k in SEASON_OK) \
                and "[seasonality-matched]" not in notes.lower():
            findings.append((adv, pid,
                f"G4 SEASONAL SERIES, RAW LEVEL: '{s_hit}' with no YoY/same-month/TTM framing. "
                f"Four instances in 8 days fired on seasonality not mechanism (CRL-22 v1, the "
                f"Fitch ATR trigger, the diesel-crack falsifier). Prefer a seasonality-matched spec."
                + ADVISORY))
            counts["flagged"].add(pid)

        # G5 — no numeric bar at all
        if not NUMERIC_BAR.search(text):
            findings.append((adv, pid,
                f"G5 NO NUMERIC BAR: prediction states no threshold — unfalsifiable by "
                f"vagueness. This is the CRL-07 shape (cut 85→40 by the Brier audit)."
                + ADVISORY))
            counts["flagged"].add(pid)

    counts["flagged"] = len(counts["flagged"])
    counts["prior_available"] = known is not None
    return findings, counts


def _print_g_coverage(s):
    if not s:
        return
    if not s.get("prior_available"):
        print(f"       ⚠️  previous commit unavailable — every row treated as PRE-EXISTING "
              f"(all findings SOFT); a genuinely new registration would not be gated this run")
    print(f"       scanned {s['scanned']} OPEN predictions · {s['new']} newly registered · "
          f"{s['flagged']} carrying at least one failure shape")
    print(f"       tiering (validated on CARL's N=10 resolved record): "
          f"G1 conjunction 1/1 · G2 revision-prone 2/2 = TIER 1, gate on new registrations · "
          f"G3/G4/G5 ~50% = ADVISORY, they do not discriminate")


# --------------------------------------------------------------------------
# Check F — bias tripwire (position-linked confidence behaviour)
# --------------------------------------------------------------------------
# ⚠️ HONEST SCOPE. The tripwire in CARL_BOOK_DESIGN.md §5 reads: "any session
# where CARL holds a live position AND adverse data lands AND no confidence
# moves." **"Adverse data lands" is NOT mechanically detectable** — no file
# records whether a print was adverse to the thesis. So this check does NOT
# implement the tripwire as written. It implements the parts that ARE
# measurable, which are arguably sharper because they look at BEHAVIOUR rather
# than at a judgement call:
#
#   F1  a position is open against a prediction that is no longer OPEN
#       (holding an expression on a dead thesis — the CRL-21 class, mechanised)
#   F2  a position is open against a pred_id that does not exist (entry-gate breach)
#   F3  THE ASYMMETRY SIGNATURE: versus the previous commit, a POSITIONED
#       prediction was RAISED in the same change-set where an UNPOSITIONED one
#       was CUT. That is what motivated reasoning looks like in the ledger.
#   F4  the bias STATISTIC: mean confidence delta, positioned vs unpositioned.
#   F5  marking discipline: open positions with a stale or absent mark.
#
# What remains human judgement: deciding that a given print was adverse. F3/F4
# substitute a comparison that needs no such call — if positioned predictions
# systematically fare better than unpositioned ones, the bias is visible in the
# deltas whether or not anyone labelled the data adverse.
SLEEVE = CARL_DIR / "book" / "PAPER_SLEEVE.tsv"
STALE_MARK_DAYS = 5


def _read_sleeve(path):
    """Return list of open position dicts, or None if the sleeve does not exist."""
    if not path.exists():
        return None
    rows, hdr = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        f = line.split("\t")
        if hdr is None:
            hdr = {n.strip(): i for i, n in enumerate(f)}
            continue
        def g(k):
            i = hdr.get(k, -1)
            return f[i].strip() if 0 <= i < len(f) else ""
        if g("status").upper() != "OPEN":
            continue
        rows.append({"paper_id": g("paper_id"), "pred_id": g("pred_id"),
                     "ticker": g("ticker"), "mark_asof": g("mark_asof"),
                     "opened": g("opened")})
    return rows


def _prior_confidences(tsv_path):
    """Confidences from the previous commit of the TSV, or None if unavailable."""
    import subprocess
    try:
        rel = tsv_path.resolve().relative_to(
            Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                         cwd=str(tsv_path.parent), text=True).strip()))
        out = subprocess.check_output(["git", "show", f"HEAD:{rel}"],
                                      cwd=str(tsv_path.parent), text=True,
                                      stderr=subprocess.DEVNULL)
    except Exception:                                  # noqa: BLE001
        return None
    conf, hdr = {}, None
    for line in out.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        f = line.split("\t")
        if hdr is None:
            hdr = {n.strip(): i for i, n in enumerate(f)}
            continue
        pid = f[0].strip()
        if not PRED_ID_RE.match(pid):
            continue
        i = hdr.get("Confidence", -1)
        if 0 <= i < len(f):
            c = extract_confidence(f[i])
            if c is not None:
                conf[pid] = c
    return conf


def check_f(tsv, tsv_path, today=None):
    """Bias tripwire — see the honest-scope note above."""
    findings, HARD, SOFT = [], "HARD", "SOFT"
    sleeve = _read_sleeve(SLEEVE)
    if sleeve is None:
        return [(SOFT, "-", "no paper sleeve at book/PAPER_SLEEVE.tsv — Check F inapplicable "
                            "(no positions ⇒ no position-linked bias to detect)")], None
    if not sleeve:
        return [(SOFT, "-", "paper sleeve exists but holds no OPEN positions — "
                            "Check F asserted nothing this run")], None

    positioned = {r["pred_id"] for r in sleeve if r["pred_id"]}

    # F1 / F2 — position against a dead or non-existent prediction
    for r in sleeve:
        pid = r["pred_id"]
        if not pid:
            findings.append((HARD, r["paper_id"],
                "ENTRY-GATE BREACH: open position carries no pred_id"))
            continue
        t = tsv.get(pid)
        if t is None:
            findings.append((HARD, r["paper_id"],
                f"ENTRY-GATE BREACH: pred_id {pid} does not exist in PREDICTIONS.tsv"))
        elif t["status"] != "OPEN":
            findings.append((HARD, r["paper_id"],
                f"DEAD-THESIS POSITION: {r['ticker']} is open against {pid}, which is "
                f"{t['status']} — holding an expression on a resolved thesis (the CRL-21 class)"))

    # F5 — marking discipline
    for r in sleeve:
        if not r["mark_asof"]:
            findings.append((SOFT, r["paper_id"],
                f"{r['ticker']} has NEVER been marked (mark_asof empty) — "
                f"a paper book that isn't marked rots (TERRY failure-mode 3)"))

    # F3 / F4 — confidence-trajectory asymmetry vs the previous commit
    prior = _prior_confidences(tsv_path)
    stats = {"positions": len(sleeve), "positioned_preds": sorted(positioned),
             "prior_available": prior is not None}
    if prior is None:
        findings.append((SOFT, "-", "previous commit of PREDICTIONS.tsv unavailable — "
                                    "F3/F4 (confidence-trajectory asymmetry) could not run"))
        return findings, stats

    deltas = {}
    for pid, cur in tsv.items():
        if cur["confidence"] is None or pid not in prior:
            continue
        d = cur["confidence"] - prior[pid]
        if d != 0:
            deltas[pid] = d
    pos_up = {p: d for p, d in deltas.items() if p in positioned and d > 0}
    unpos_dn = {p: d for p, d in deltas.items() if p not in positioned and d < 0}
    if pos_up and unpos_dn:
        findings.append((HARD, "bias",
            f"ASYMMETRY SIGNATURE: positioned prediction(s) RAISED "
            f"({', '.join(f'{p} {d:+d}pp' for p, d in sorted(pos_up.items()))}) in the same "
            f"change-set where unpositioned prediction(s) were CUT "
            f"({', '.join(f'{p} {d:+d}pp' for p, d in sorted(unpos_dn.items()))}) — "
            f"this is what motivated reasoning looks like in the ledger. Justify or reverse."))

    pos_d = [d for p, d in deltas.items() if p in positioned]
    unpos_d = [d for p, d in deltas.items() if p not in positioned]
    stats.update({
        "changed": len(deltas),
        "pos_mean": (sum(pos_d) / len(pos_d)) if pos_d else None,
        "unpos_mean": (sum(unpos_d) / len(unpos_d)) if unpos_d else None,
        "pos_n": len(pos_d), "unpos_n": len(unpos_d),
        "degenerate": len(positioned) < 2,
    })
    return findings, stats


def _print_f_coverage(s):
    if not s:
        return
    print(f"       positions: {s['positions']} open across "
          f"{len(s['positioned_preds'])} prediction(s) ({', '.join(s['positioned_preds'])})")
    if not s.get("prior_available"):
        return
    pm, um = s.get("pos_mean"), s.get("unpos_mean")
    if s.get("changed", 0) == 0:
        print(f"       no confidence changed vs the previous commit — F3/F4 asserted nothing")
    else:
        f = lambda v, n: f"{v:+.1f}pp (n={n})" if v is not None else "none changed"
        print(f"       confidence delta since last commit — positioned {f(pm, s['pos_n'])} · "
              f"unpositioned {f(um, s['unpos_n'])}")
    if s.get("degenerate"):
        print(f"       \u26a0\ufe0f  all positions sit on ONE prediction — the positioned-vs-"
              f"unpositioned comparison is DEGENERATE and proves nothing yet")


# --------------------------------------------------------------------------
# Check B — convergence-score cross-surface (THESIS ↔ STATUS ↔ histogram)
# --------------------------------------------------------------------------
SCORE_RE = re.compile(r"\b([1-5])\b")
VEC_RE = re.compile(r"V(\d+)")


def _find_matrix(lines):
    """
    Locate the convergence matrix by its HEADER ('# | Vector'), then take the
    contiguous pipe-table beneath it.  Bounding by header is required: THESIS.md
    contains other tables whose rows share the '| <int> | ...' shape, and a naive
    row-pattern grep silently mixes them in.
    """
    start = None
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("|") and "vector" in s.lower() and re.search(r"\|\s*#\s*\|", s):
            start = i
            break
    if start is None:
        return {}
    scores = {}
    for line in lines[start + 1:]:
        s = line.strip()
        if not s.startswith("|"):
            if s == "":
                continue
            break
        cells = _split_md_row(line)
        if len(cells) < 4:
            continue
        num = strip_markdown(cells[0])
        if not num.isdigit():
            continue  # separator row
        m = SCORE_RE.search(strip_markdown(cells[3]))
        if m:
            scores[int(num)] = int(m.group(1))
    return scores


def _find_histogram(lines):
    """Parse STATUS '### Score histogram' -> (buckets, total_count, total_sum, raw_total)."""
    start = None
    for i, line in enumerate(lines):
        if line.strip().lower().startswith("### score histogram"):
            start = i
            break
    if start is None:
        return None
    buckets, total_count, total_sum, raw_total = {}, None, None, None
    for line in lines[start + 1:]:
        s = line.strip()
        if not s.startswith("|"):
            if s == "" or s.startswith("|---"):
                continue
            if buckets:
                break
            continue
        cells = _split_md_row(line)
        if len(cells) < 4:
            continue
        label = strip_markdown(cells[0])
        if label.lower() == "total":
            m = re.search(r"(\d+)", strip_markdown(cells[2]))
            total_count = int(m.group(1)) if m else None
            raw_total = strip_markdown(cells[3])
            m2 = re.search(r"(\d+)\s*/\s*(\d+)", raw_total)
            total_sum = (int(m2.group(1)), int(m2.group(2))) if m2 else None
            break
        if not label.isdigit():
            continue
        score = int(label)
        vecs = [int(v) for v in VEC_RE.findall(cells[1])]
        cm = re.search(r"(\d+)", strip_markdown(cells[2]))
        sm = re.search(r"(\d+)", strip_markdown(cells[3]))
        buckets[score] = {
            "vectors": vecs,
            "count": int(cm.group(1)) if cm else None,
            "sum": int(sm.group(1)) if sm else None,
        }
    return buckets, total_count, total_sum, raw_total


def check_b(thesis_path, status_path):
    """Convergence score must agree across THESIS matrix, STATUS mirror, and histogram."""
    findings = []
    HARD, SOFT = "HARD", "SOFT"

    if not thesis_path.exists():
        return [(SOFT, "-", f"THESIS not found ({thesis_path}) — Check B skipped")], None

    tl = thesis_path.read_text(encoding="utf-8").splitlines()
    sl = status_path.read_text(encoding="utf-8").splitlines()
    th = _find_matrix(tl)
    st = _find_matrix(sl)

    if not th:
        findings.append((SOFT, "-", "THESIS convergence matrix not found — B1 skipped"))
    if not st:
        findings.append((SOFT, "-", "STATUS convergence matrix mirror not found — B1 skipped"))

    # --- B1/B2: per-vector agreement ---
    if th and st:
        for v in sorted(set(th) | set(st)):
            a, b = th.get(v), st.get(v)
            if a is None:
                findings.append((HARD, f"V{v}", "in STATUS matrix but MISSING from THESIS matrix"))
            elif b is None:
                findings.append((HARD, f"V{v}", "in THESIS matrix but MISSING from STATUS mirror"))
            elif a != b:
                findings.append((HARD, f"V{v}",
                    f"SCORE DRIFT: THESIS={a} vs STATUS mirror={b} (canonical is THESIS)"))

    # --- histogram ---
    hist = _find_histogram(sl)
    if hist is None:
        findings.append((SOFT, "-", "STATUS '### Score histogram' not found — B3/B4 skipped"))
        return findings, None
    buckets, total_count, total_sum, raw_total = hist

    stats = {"thesis_vectors": len(th), "status_vectors": len(st),
             "buckets": len(buckets), "total": raw_total}

    # --- B3: histogram membership vs STATUS matrix ---
    if st:
        hist_map = {}
        for score, b in buckets.items():
            for v in b["vectors"]:
                if v in hist_map:
                    findings.append((HARD, f"V{v}",
                        f"listed in MORE THAN ONE histogram bucket ({hist_map[v]} and {score})"))
                hist_map[v] = score
        for v in sorted(set(st) | set(hist_map)):
            m, h = st.get(v), hist_map.get(v)
            if h is None:
                findings.append((HARD, f"V{v}",
                    f"scored {m} in STATUS matrix but ABSENT from the histogram"))
            elif m is None:
                findings.append((HARD, f"V{v}",
                    f"in histogram bucket {h} but ABSENT from the STATUS matrix"))
            elif m != h:
                findings.append((HARD, f"V{v}",
                    f"HISTOGRAM MISMATCH: STATUS matrix says {m}, histogram puts it in bucket {h}"))

    # --- B4: histogram arithmetic (self-consistency, no external input needed) ---
    calc_count = calc_sum = 0
    for score in sorted(buckets, reverse=True):
        b = buckets[score]
        n = len(b["vectors"])
        if b["count"] is not None and b["count"] != n:
            findings.append((HARD, f"hist[{score}]",
                f"count says {b['count']} but {n} vectors are listed"))
        if b["sum"] is not None and b["sum"] != score * n:
            findings.append((HARD, f"hist[{score}]",
                f"sum says {b['sum']} but {n} vectors x {score} = {score * n}"))
        calc_count += n
        calc_sum += score * n
    if total_count is not None and total_count != calc_count:
        findings.append((HARD, "hist[total]",
            f"total count says {total_count} but buckets hold {calc_count} vectors"))
    if total_sum is not None:
        stated, denom = total_sum
        if stated != calc_sum:
            findings.append((HARD, "hist[total]",
                f"TOTAL SCORE WRONG: stated {stated} but buckets sum to {calc_sum}"))
        expected_denom = calc_count * 5
        if denom != expected_denom:
            findings.append((HARD, "hist[total]",
                f"denominator {denom} != {calc_count} vectors x 5 = {expected_denom}"))

    # --- B5: CURRENT-score ASSERTION sites must agree ---
    #
    # Deliberately NOT "every \d\d/70 in the file".  STATUS legitimately carries
    # prior scores as history ("Net 52->51", "recalibrated 58/60 -> 53/70",
    # "52/70 held"), and flagging those produces false positives — which is worse
    # than no check at all, because a checker that cries wolf gets ignored.
    # So B5 matches only the phrasings that ASSERT the live score.
    ASSERTION_PATTERNS = (
        r"Convergence\s+\**(\d+)\s*/\s*70",     # Overall line + BOTTOM LINE
        r"Total:\s*\**(\d+)\s*/\s*70",          # the total line under the histogram
    )
    if total_sum:
        stated, denom = total_sum
        want = f"{stated}/{denom}"
        body = "\n".join(sl)
        sites = []
        for pat in ASSERTION_PATTERNS:
            sites.extend(re.findall(pat, body))
        bad = sorted({s for s in sites if int(s) != stated})
        if bad:
            findings.append((HARD, "score",
                f"CURRENT-SCORE DRIFT: histogram totals {want}, but a current-score "
                f"assertion in STATUS reads {', '.join(b + '/70' for b in bad)} "
                f"(history mentions are ignored; these are live assertions)"))
        stats["assertion_sites"] = len(sites)
        if not sites:
            findings.append((SOFT, "score",
                "no current-score assertion site found in STATUS ('Convergence N/70' "
                "or 'Total: N/70') — B5 asserted nothing this run"))
    return findings, stats


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
def print_report(groups, tsv, status_open, n_entries, e_stats=None, b_stats=None,
                 f_stats=None, g_stats=None, quiet=False, mirror_path=None):
    """groups: ordered list of (label, findings)."""
    all_f = [f for _, fs in groups for f in fs]
    hard = [f for f in all_f if f[0] == "HARD"]
    soft = [f for f in all_f if f[0] == "SOFT"]

    if not quiet:
        print(f"\n{'=' * 78}")
        print(f"  CARL CONSISTENCY CHECK — A mirror · B score · D instrument · E monotonicity · F bias · G failure-shape")
        print(f"{'=' * 78}")
        print(f"  Canonical : thesis/PREDICTIONS.tsv "
              f"({sum(1 for v in tsv.values() if v['status'] == 'OPEN')} OPEN "
              f"/ {len(tsv)} total)")
        # Name the file actually read, never a hardcoded one (PAT-137: a mirror
        # check that does not say what it read licenses every copy outside the
        # pair it names). Derived from the live path so it cannot go stale again.
        _mirror = Path(mirror_path).name if mirror_path else DEFAULT_PRED_MIRROR.name
        print(f"  Mirror    : {_mirror} '## PREDICTIONS' Open table "
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
            if f_stats is not None and label.startswith("CHECK F"):
                _print_f_coverage(f_stats)
            if g_stats is not None and label.startswith("CHECK G"):
                _print_g_coverage(g_stats)
            if b_stats and label.startswith("CHECK B"):
                print(f"       verified: {b_stats['thesis_vectors']} THESIS vectors vs "
                      f"{b_stats['status_vectors']} STATUS mirror rows vs "
                      f"{b_stats['buckets']} histogram buckets; total {b_stats['total']}"
                      + (f"; {b_stats['assertion_sites']} current-score assertion site(s) agree"
                         if b_stats.get('assertion_sites') else ""))
            continue
        print(f"\n  {label}")
        print(f"  {'SEV':<5} {'ROW':<16} FINDING")
        print(f"  {'-' * 74}")
        for sev, pid, msg in fs:
            mark = "\U0001f534" if sev == "HARD" else "⚠️ "
            print(f"  {mark} {sev:<4} {pid:<16} {msg}")
        if e_stats and label.startswith("CHECK E"):
            _print_e_coverage(e_stats)
        if f_stats is not None and label.startswith("CHECK F"):
            _print_f_coverage(f_stats)
        if g_stats is not None and label.startswith("CHECK G"):
            _print_g_coverage(g_stats)
        if b_stats and label.startswith("CHECK B"):
            print(f"       verified: {b_stats['thesis_vectors']} THESIS vectors vs "
                  f"{b_stats['status_vectors']} STATUS mirror rows vs "
                  f"{b_stats['buckets']} histogram buckets; total {b_stats['total']}"
                  + (f"; {b_stats['assertion_sites']} current-score assertion site(s)"
                     if b_stats.get('assertion_sites') else ""))

    print(f"\n  SUMMARY: {len(hard)} hard, {len(soft)} soft")
    if hard:
        print(f"  ❌ {len(hard)} HARD finding(s) — fix before commit "
              f"(canonical wins on mirrors; declare the instrument; "
              f"reconcile the monotonicity pair).\n")
    else:
        print(f"  (soft-only — no hard drift)\n")


# --------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="CARL consistency checker — Checks A, B, D, E, F, G.")
    ap.add_argument("--quiet", action="store_true", help="summary + findings only")
    ap.add_argument("--warn-only", action="store_true",
                    help="always exit 0 (findings still print). Used by boot.py so a "
                         "consistency finding surfaces loudly without being reported as a "
                         "script FAILURE — 'drift found' and 'the script broke' are "
                         "different things and must not look the same in the boot summary.")
    ap.add_argument("--tsv", default=str(DEFAULT_TSV), help="override PREDICTIONS.tsv path")
    ap.add_argument("--status", default=str(DEFAULT_STATUS), help="override STATUS.md path")
    ap.add_argument("--pred-mirror", default=str(DEFAULT_PRED_MIRROR),
                    help="override PREDICTIONS_MIRROR.md path (Check A's mirror side)")
    ap.add_argument("--thesis", default=str(DEFAULT_THESIS), help="override THESIS.md path")
    args = ap.parse_args()

    tsv_path = Path(args.tsv)
    status_path = Path(args.status)
    if not tsv_path.exists():
        raise SystemExit(f"FATAL: TSV not found: {tsv_path}")
    if not status_path.exists():
        raise SystemExit(f"FATAL: STATUS not found: {status_path}")

    tsv = parse_tsv(tsv_path)
    pred_mirror_path = Path(args.pred_mirror)
    if not pred_mirror_path.exists():
        raise SystemExit(
            f"FATAL: predictions mirror not found: {pred_mirror_path}\n"
            "  Check A's mirror side moved out of STATUS.md on 2026-09-01 (read-cap remedy).\n"
            "  Fail LOUD rather than silently falling back to STATUS.md: a checker that\n"
            "  quietly re-points at a stale location is the failure this move was guarding.")
    status_open, status_resolved = parse_status(pred_mirror_path)

    fa = check_a(tsv, status_open, status_resolved)
    fb, b_stats = check_b(Path(args.thesis), status_path)
    fd = check_d(tsv)
    ff, f_stats = check_f(tsv, tsv_path)
    fg, g_stats = check_g(tsv, tsv_path)
    entries, gaps = collect_ledgers(tsv_path, tsv)
    fe, e_stats = check_e(entries, gaps)

    groups = [
        ("CHECK A — predictions mirror (PREDICTIONS.tsv ↔ PREDICTIONS_MIRROR.md)", fa),
        ("CHECK B — convergence score (THESIS matrix ↔ STATUS mirror ↔ histogram)", fb),
        ("CHECK D — instrument declaration (does each OPEN row name what resolves it?)", fd),
        ("CHECK E — cross-ledger threshold monotonicity (parent + sub-agents)", fe),
        ("CHECK F — bias tripwire (position-linked confidence behaviour)", ff),
        ("CHECK G — registration-time failure-shape lint", fg),
    ]
    print_report(groups, tsv, status_open, len(entries), e_stats=e_stats,
                 b_stats=b_stats, f_stats=f_stats, g_stats=g_stats, quiet=args.quiet,
                 mirror_path=pred_mirror_path)

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
