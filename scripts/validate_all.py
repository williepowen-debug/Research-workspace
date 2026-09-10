#!/usr/bin/env python3
"""validate_all.py — the fleet's ONE mechanical-suite runner (v1, 2026-09-10, DAEDALUS).

WHAT IT IS
  A SUITE RUNNER over already-registered checks plus a small set of in-house
  LEDGER-TYPING legs.  It runs each registered check in its own self-verifying
  mode, types the three PROME decision ledgers, and returns ONE aggregate
  verdict under the CHECK_STANDARD §9 rc contract.

  Its perimeter is `AGENTS/DAEDALUS/CHECKS.tsv` — i.e. it is bounded by checks
  that already exist.

WHAT IT IS NOT  ⚠️  (scope RULED 2026-09-05 BEFORE the build; record
  `AGENTS/DAEDALUS/design/2026-09-05_VALIDATE_ALL_IS_NOT_THE_YEYOU_REPLACEMENT.md`)
  It is NOT the retired per-push mechanical-review seat.  Back-tested against
  YEYOU's 13 real findings: 1 caught cleanly, ~4 partial, 6-7 missed — the
  largest missed category (4/13) being mail-loop.  Structural, not fixable by
  adding legs: this tool is STATE-based where YEYOU was WATERMARK/DIFF-based,
  it checks FILE PROPERTIES where YEYOU judged CONTRADICTIONS against a desk's
  own stated rules, and its perimeter is the set of checks that already exist,
  which is exactly what a reviewer is for.  A green run here does not refill
  that seat and must never be reported as doing so.

PRIOR-ART LINE (CHECK_STANDARD §13)
  Symptom searched: "suite runner reports green while a leg never ran" /
  "aggregate check hides a failing member" against memory/auto/MEMORY.md,
  memory/auto/INDEX_COLD*.md and AGENTS/DAEDALUS/PATTERNS_HOT.md.
  Hits (this build is shaped around them, not novel):
    finding_guard_correctness_and_wiring_are_independent  — CAN it fire? THIS path?
    finding_a_check_that_only_advises_is_overridden_the_control_is_downstream
    finding_instrument_reports_clean_against_the_wrong_reference
    finding_lenient_parser_reports_unparseable_as_a_behavior — fail closed
    PAT-074 (what a PASS proves) · PAT-110 (rc contract) · PAT-146 (self-tests
    enumerate only the cases the author imagined).

SELF-SCOPE (CHECK_STANDARD §10) — DAEDALUS's own directory is IN SCOPE.
  Legs A2/A6/A7/A8 and D1 read or exercise DAEDALUS-authored surfaces, and
  DAEDALUS's own desk appears in the D1 fleet population like every other.

FAILURE DIRECTION (CHECK_STANDARD §6) — declared, per leg, in the LEGS table
  and again as a comment at each asymmetric site.  Short form: a leg that
  measures a CHRONIC FLEET BACKLOG (D1 read-cap, C2 KB Stale_By, C1 commit
  subjects) REPORTS but does not flip the verdict — pinning permanent-red on
  a 6/37 backlog is silent-green inverted (§3(e)) — while a leg that measures
  a STRUCTURAL DEFECT (B1-B3 ledger typing, any A selftest) DOES flip.
  Backlog legs escalate on the DELTA above their recorded baseline (§12),
  never on the level.  ⚠️ The VERDICT reads the resulting STATE, never a
  per-leg boolean: v1's first selftest run caught the inverse wiring, in which
  a delta-keyed leg computed FINDINGS and the verdict could not see it.

BASELINES (CHECK_STANDARD §12 — swept 2026-09-10, this repo, HEAD 6f342d55b)
  A1..A8 selftests   : 8/8 PASS  (0 findings)
  B1 DOCKET.tsv      : 310 data rows, 6 cols each, 0 defects AFTER the grammar
                       was cut to the measured population (241 date · 60 range
                       · 6 next-<x> event · 1 ~approx · 1 header).  Typing col 1
                       as a bare date returned 68 flags, ALL legitimate.
  B2 GATES.tsv       : 20 gate rows, 12 cols each, 0 defects after typing the
                       LEADING date token.  Every dated cell in the file carries
                       trailing annotation; 3 review_by cells are terminal
                       em-dashes.  Bare-date typing returned 27 flags, all
                       legitimate.
  B3 WILL_QUEUE.md   : 13 queue rows, 7 cols, ids unique, 0 defects.
  C1 commit subjects : 13/200 over 100 chars (report-only; history is fixed).
  C2 KB Stale_By     : 534 rows past Stale_By and non-terminal, over 1,231
                       dated cells in 31 KBs (20 KBs carry no Stale_By column).
                       A standing fleet backlog with named owners — recorded as
                       the baseline; a RISE escalates.
  D1 read-cap fleet  : 6/37 desks over BUDGET, 1/37 over CAP.

VERIFICATION (CHECK_STANDARD §3)
  (a) flag line watched on a real capable case: see `--selftest` drills, each
      of which builds a REAL defective input (a mistyped DOCKET row, a short
      GATES row, a duplicate WQ id, a failing sub-check) and the run log in
      `AGENTS/DAEDALUS/runs/2026-09-10_VALIDATE_ALL_V1.md`.
  (b) clean line watched on a clean case: `--selftest` clean drills + the
      production run against this repo.
  (e) PRODUCTION ACCEPTANCE SET (real inputs, named by path, re-run at every
      version):
        real CLEAN input     : PROME/GATES.tsv        (B2 → PASS)
        real DEFECTIVE input : PROME/DOCKET.tsv col-1 typed as date-only
                               (68 legitimate rows → 68 flags; the reason B1
                               carries a declared grammar).  Reproduce exactly
                               with `--only B1 --strict-dates`.

RC CONTRACT (CHECK_STANDARD §9)
  0  no leg in FINDINGS or CANNOT-CERTIFY
  1  >=1 leg in FINDINGS (a structural defect, or a delta above baseline)
  2  CANNOT-CERTIFY — a leg could not run, a tool is missing, an input is
     unparseable, a usage error, or an EXPIRED gap-register row.  2 dominates 1.

KNOWN-GAP REGISTER (CHECK_STANDARD §1) — `scripts/validate_all_gaps.tsv`
  Expiry-dated, per-instance, never a pattern.  An EXPIRED row re-flags itself
  and takes the run to rc 2.  A malformed register suppresses NOTHING and says
  so.

READER (CHECK_STANDARD §11)
  Read by: DAEDALUS at any tooling sitting; PROME at closeout when a decision
  ledger was touched.  Registered in AGENTS/DAEDALUS/CHECKS.tsv at build.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

TOOL = "VALIDATE-ALL"
VERSION = "v1"

# --- states (local vocabulary; CHECKS.tsv-style tokens) ----------------------
PASS = "PASS"
FINDINGS = "FINDINGS"
CANNOT = "CANNOT-CERTIFY"
GAP = "DECLARED-GAP"          # registered in the gap file, unexpired
ADVISORY = "ADVISORY"          # reports, does not flip (declared asymmetry)

FLIPPING = {FINDINGS, CANNOT}

DEFAULT_COMMIT_SCAN = 200
SUBJECT_CAP = 100              # root CLAUDE.md 4d / WQ-171 ①

# KB Status tokens that END a row's obligation — an expired Stale_By on one of
# these is not a defect.  Sourced from the 2026-09-10 fleet sweep of
# AGENTS/*/workbook/KB.tsv Status cells.
KB_TERMINAL_STATUS = {
    "SUPERSEDED", "STALE", "CORRECTED", "RESOLVED", "RESOLVED-GRADED",
    "DATED-HISTORICAL", "RETIRED", "CLOSED", "ARCHIVED",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
DATE_RANGE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\.\.\d{4}-\d{2}-\d{2}$")

# --- THE MEASURED LEDGER GRAMMARS ------------------------------------------
# CHECK_STANDARD §12: base-rate a check before wiring it.  v1's first
# production run typed col-1 as a bare date and returned 8 DOCKET + 27 GATES
# "defects", ALL of which were legitimate ledger forms.  The grammars below are
# the measured population as of 2026-09-10, not an assumption; each token class
# is named so a reader can see what was ACCEPTED, and the run prints the count
# of cells that needed each relaxation.
#
# DOCKET col 1 (the trigger cell) — 310 rows:
#   241  YYYY-MM-DD                      exact date
#    60  YYYY-MM-DD..YYYY-MM-DD          window
#     6  next-<desk-or-pass>             EVENT-keyed, no date exists yet
#     1  ~YYYY-MM-DD                     approximate date
#     1  the literal header token `date`
DOCKET_APPROX_RE = re.compile(r"^~\s*\d{4}-\d{2}-\d{2}$")
DOCKET_EVENT_RE = re.compile(r"^next-[A-Za-z0-9][A-Za-z0-9_-]*$")

# GATES `registered` / `review_by` — 20 rows: EVERY cell is a leading date (or
# the terminal em-dash) followed by free annotation.  The leg types the LEADING
# token and REPORTS how many cells carry trailing prose — it does not flag them,
# because an annotated review_by is the file's own long-standing form and
# flagging it would make a right row less right (§1's last bullet).
GATES_LEAD_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})(\s|$)")
GATES_TERMINAL_RE = re.compile(r"^[—-]\s*(\(|$)")


def repo_root() -> Path:
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        )
        return Path(out.stdout.strip())
    except Exception:
        return Path(__file__).resolve().parent.parent


class Leg:
    """One member of the suite."""

    def __init__(self, lid, group, label, flips, runner, perimeter):
        self.id = lid
        self.group = group
        self.label = label
        # ESCALATION RULE, not the flip test.  True  = STRUCTURAL: any defect is
        # FINDINGS.  False = DELTA-KEYED/REPORT-ONLY: the LEVEL is ADVISORY and
        # only a rise above the recorded baseline (§12) escalates to FINDINGS.
        # The verdict reads the resulting STATE; see verdict().
        self.flips = flips
        self.runner = runner
        self.perimeter = perimeter  # what this leg reads (printed, §2)


class Result:
    def __init__(self, leg, state, headline, detail=None, count=0, baseline=None):
        self.leg = leg
        self.state = state
        self.headline = headline
        self.detail = detail or []
        self.count = count
        self.baseline = baseline


# ============================================================================
# GROUP A — delegated selftests (the instruments prove themselves)
# ============================================================================

SELFTEST_LEGS = [
    ("A1", "scripts/corrections_boot_check.py", ["--selftest"]),
    ("A2", "scripts/docket_view.py", ["--selftest"]),
    ("A3", "scripts/orch_log.py", ["--selftest"]),
    ("A4", "scripts/claim_check.py", ["--selftest"]),
    ("A5", "scripts/memory_index_check.py", ["--selftest"]),
    ("A6", "scripts/consumer_check.py", ["--selftest"]),
    ("A7", "scripts/ledger_staleness.py", ["--selftest"]),
    ("A8", "scripts/memory_citation_census.py", ["--selftest"]),
]


def run_selftest(root: Path, script: str, args, timeout: int):
    path = root / script
    if not path.exists():
        return CANNOT, f"tool absent at {script}", []
    try:
        proc = subprocess.run(
            [sys.executable, str(path)] + args,
            capture_output=True, text=True, timeout=timeout, cwd=str(root),
        )
    except subprocess.TimeoutExpired:
        return CANNOT, f"{script} --selftest timed out at {timeout}s", []
    except Exception as exc:                      # pragma: no cover - defensive
        return CANNOT, f"{script} --selftest could not be launched: {exc}", []

    tail = [ln for ln in (proc.stdout or "").strip().splitlines() if ln.strip()]
    last = tail[-1] if tail else "(no output)"
    if proc.returncode == 0:
        return PASS, last, []
    if proc.returncode == 1:
        return FINDINGS, f"{script} --selftest rc=1 :: {last}", tail[-6:]
    # Anything else — including a Python traceback (rc 1 from the interpreter is
    # indistinguishable from a findings-1, so stderr decides) — cannot certify.
    err = (proc.stderr or "").strip().splitlines()
    return CANNOT, f"{script} --selftest rc={proc.returncode} :: {last}", (err or tail)[-6:]


def make_selftest_runner(script, args):
    def _run(ctx):
        state, headline, detail = run_selftest(ctx["root"], script, args, ctx["timeout"])
        return Result(None, state, headline, detail)
    return _run


# ============================================================================
# GROUP B — ledger typing (the WQ-171 ③ precondition: "types the ledgers")
# ============================================================================

def _tsv_rows(path: Path):
    """Yield (lineno, raw, fields) for non-comment, non-blank rows."""
    with path.open(encoding="utf-8") as fh:
        for i, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            yield i, line, line.split("\t")


def _docket_trigger_class(cell: str, strict: bool):
    """Return the token class of a DOCKET col-1 cell, or None if untyped."""
    cell = cell.strip()
    if DATE_RE.match(cell):
        return "date"
    if strict:
        # --strict-dates reproduces the v1 acceptance-set DEFECTIVE case: it
        # types col 1 as a bare date and returns the 68 range/event/approx rows
        # as flags.  Kept as a runnable demonstration of why the grammar exists.
        return None
    if DATE_RANGE_RE.match(cell):
        return "range"
    if DOCKET_APPROX_RE.match(cell):
        return "approx"
    if DOCKET_EVENT_RE.match(cell):
        return "event"
    return None


def leg_docket(ctx):
    root = ctx["root"]
    path = root / "PROME" / "DOCKET.tsv"
    if not path.exists():
        return Result(None, CANNOT, f"PROME/DOCKET.tsv absent at {path}")
    want = 6
    defects, rows, classes = [], 0, {}
    header_seen = False
    for lineno, line, fields in _tsv_rows(path):
        rows += 1
        if not header_seen and fields[0].strip().lower() in ("date", "due"):
            header_seen = True
            continue
        if len(fields) != want:
            defects.append(f"L{lineno}: {len(fields)} field(s), want {want}")
            continue
        cls = _docket_trigger_class(fields[0], ctx["strict_dates"])
        if cls is None:
            defects.append(
                f"L{lineno}: col1 outside the declared trigger grammar "
                f"(date | range | ~date | next-<x>): {fields[0][:40]!r}")
        else:
            classes[cls] = classes.get(cls, 0) + 1
        if not fields[3].strip():
            defects.append(f"L{lineno}: col4 (state) empty")
    if rows == 0:
        # Positive control (§14): a ledger that parses to ZERO rows is an
        # instrument failure, never an absence finding.
        return Result(None, CANNOT, "PROME/DOCKET.tsv parsed to 0 data rows — instrument or file defect")
    state = FINDINGS if defects else PASS
    grammar = " · ".join(f"{v} {k}" for k, v in sorted(classes.items()))
    head = (f"{len(defects)} typing defect(s) over {rows} data row(s) [{grammar}]" if defects
            else f"{rows} data row(s), {want} cols each; trigger grammar typed: {grammar}")
    return Result(None, state, head, defects, len(defects))


def leg_gates(ctx):
    root = ctx["root"]
    path = root / "PROME" / "GATES.tsv"
    if not path.exists():
        return Result(None, CANNOT, f"PROME/GATES.tsv absent at {path}")
    defects, rows, want = [], 0, None
    cols = {}
    annotated = terminal = 0
    for lineno, line, fields in _tsv_rows(path):
        if want is None:
            want = len(fields)
            cols = {name.strip(): i for i, name in enumerate(fields)}
            if "gate_id" not in cols:
                return Result(None, CANNOT,
                              f"GATES.tsv header lacks gate_id (parse is by HEADER NAME); saw {fields[:4]}")
            continue
        rows += 1
        if len(fields) != want:
            defects.append(f"L{lineno}: {len(fields)} field(s), want {want}")
            continue
        gid = fields[cols["gate_id"]].strip()
        if not gid:
            defects.append(f"L{lineno}: gate_id empty")
        for dcol in ("registered", "review_by"):
            if dcol not in cols:
                continue
            cell = fields[cols[dcol]].strip()
            if not cell:
                continue
            if GATES_TERMINAL_RE.match(cell):
                terminal += 1
                continue
            m = GATES_LEAD_DATE_RE.match(cell)
            if not m:
                defects.append(f"L{lineno}: {dcol} has no leading YYYY-MM-DD and is not terminal: {cell[:40]!r}")
                continue
            if len(cell) > len(m.group(1)):
                annotated += 1
        if "state" in cols and not fields[cols["state"]].strip():
            defects.append(f"L{lineno}: state empty")
    if rows == 0:
        return Result(None, CANNOT, "PROME/GATES.tsv parsed to 0 data rows — instrument or file defect")
    state = FINDINGS if defects else PASS
    shape = (f"{annotated} date cell(s) carry trailing annotation beyond the typed token · "
             f"{terminal} terminal em-dash cell(s)")
    head = (f"{len(defects)} typing defect(s) over {rows} gate row(s); {shape}" if defects
            else f"{rows} gate row(s), {want} cols each, leading dates parse; {shape}")
    return Result(None, state, head, defects, len(defects))


WQ_ROW_RE = re.compile(r"^\|\s*(\d+)\s*\|")


def leg_will_queue(ctx):
    root = ctx["root"]
    path = root / "PROME" / "WILL_QUEUE.md"
    if not path.exists():
        return Result(None, CANNOT, f"PROME/WILL_QUEUE.md absent at {path}")
    text = path.read_text(encoding="utf-8")
    want = None
    defects, ids, rows = [], {}, 0
    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line.startswith("|"):
            continue
        cells = [c for c in line.strip("|").split("|")]
        if set("".join(cells).strip()) <= set("-: "):
            continue                                  # the |---|---| separator
        if want is None and not WQ_ROW_RE.match(line):
            want = len(cells)                          # the header row
            continue
        m = WQ_ROW_RE.match(line)
        if not m:
            continue                                   # a table elsewhere in the doc
        rows += 1
        if want is not None and len(cells) != want:
            defects.append(f"L{lineno}: {len(cells)} cell(s), want {want} (id {m.group(1)})")
        wid = m.group(1)
        if wid in ids:
            defects.append(f"L{lineno}: duplicate WQ id {wid} (first at L{ids[wid]})")
        else:
            ids[wid] = lineno
    if rows == 0:
        # §14 positive control: the file exists and has pipe-rows, or the leg
        # cannot certify.  Zero typed rows is never reported as clean.
        return Result(None, CANNOT, "WILL_QUEUE.md parsed to 0 numbered table rows — instrument or file defect")
    state = FINDINGS if defects else PASS
    head = (f"{len(defects)} typing defect(s) over {rows} queue row(s)" if defects
            else f"{rows} queue row(s), {want} cols, ids unique")
    return Result(None, state, head, defects, len(defects))


# ============================================================================
# GROUP C — advisory backlog legs (report, do not flip; flip on DELTA)
# ============================================================================

def leg_commit_subjects(ctx):
    root, n = ctx["root"], ctx["commit_scan"]
    try:
        proc = subprocess.run(
            ["git", "log", "--format=%s", f"-n{n}"],
            capture_output=True, text=True, cwd=str(root), timeout=ctx["timeout"],
        )
    except Exception as exc:
        return Result(None, CANNOT, f"git log unavailable: {exc}")
    if proc.returncode != 0:
        return Result(None, CANNOT, f"git log rc={proc.returncode}: {(proc.stderr or '').strip()[:120]}")
    subjects = [s for s in proc.stdout.splitlines() if s.strip()]
    if not subjects:
        # §14: an empty scan is an instrument failure, not "zero long subjects".
        return Result(None, CANNOT, f"git log returned 0 subjects over -n{n} — instrument failure, not an absence")
    over = [s for s in subjects if len(s) > SUBJECT_CAP]
    # DECLARED ASYMMETRY (§6): history is FIXED — root CLAUDE.md 4b forbids
    # amend, so a past long subject can never be repaired.  Flagging it would
    # pin this run permanently red and kill the signal for the subject that CAN
    # still be fixed: the next one.  So this leg reports and never flips.
    head = (f"{len(over)}/{len(subjects)} subject(s) over {SUBJECT_CAP} chars "
            f"(advisory — history cannot be amended, root 4b)")
    detail = [f"{len(s)}c: {s[:88]}…" for s in over[:5]]
    if len(over) > 5:
        detail.append(f"(+{len(over) - 5} more not listed)")     # §4
    return Result(None, ADVISORY if over else PASS, head, detail, len(over))


def leg_kb_stale_by(ctx):
    root = ctx["root"]
    today = ctx["today"]
    files = sorted(root.glob("AGENTS/*/workbook/KB.tsv"))
    if not files:
        return Result(None, CANNOT, "no AGENTS/*/workbook/KB.tsv found — instrument or perimeter failure")
    scanned = 0          # positive control (§14): rows that HAVE a Stale_By
    expired, no_col = [], []
    for f in files:
        try:
            with f.open(encoding="utf-8") as fh:
                head = fh.readline().rstrip("\n").split("\t")
                cols = {c.strip(): i for i, c in enumerate(head)}
                if "Stale_By" not in cols:
                    no_col.append(f.parent.parent.name)
                    continue
                si, sti = cols["Stale_By"], cols.get("Status")
                idi = cols.get("ID", 0)
                for raw in fh:
                    fields = raw.rstrip("\n").split("\t")
                    if len(fields) <= si:
                        continue
                    cell = fields[si].strip()
                    if not DATE_RE.match(cell):
                        continue
                    scanned += 1
                    status = fields[sti].strip().upper() if (sti is not None and len(fields) > sti) else ""
                    if status in KB_TERMINAL_STATUS:
                        continue
                    if cell < today:
                        rid = fields[idi].strip() if len(fields) > idi else "?"
                        expired.append(f"{f.parent.parent.name}/{rid} Stale_By {cell} status={status or '(blank)'}")
        except Exception as exc:
            return Result(None, CANNOT, f"KB parse failed at {f}: {exc}")
    if scanned == 0:
        # Positive control failed: no row anywhere carried a parseable Stale_By.
        return Result(None, CANNOT,
                      f"positive control FAILED — 0 parseable Stale_By cells across {len(files)} KB(s); "
                      "an empty result here is instrument failure, not an absence")
    # DECLARED ASYMMETRY (§6): a chronic expiry backlog across 30+ desks is
    # each OWNER's judgment call, not a structural defect this tool can rule on.
    # Reports; flips only above the recorded baseline via --baseline.
    base = ctx["baseline"].get("C2_kb_stale_by")
    head = (f"{len(expired)} row(s) past Stale_By and not terminal "
            f"(control: {scanned} dated cells over {len(files)} KB(s); "
            f"{len(no_col)} KB(s) have no Stale_By column)")
    detail = [e for e in expired[:5]]
    if len(expired) > 5:
        detail.append(f"(+{len(expired) - 5} more not listed)")   # §4
    state = ADVISORY if expired else PASS
    if base is not None and len(expired) > base:
        detail.insert(0, f"DELTA +{len(expired) - base} above recorded baseline {base} — owner action owed")
        state = FINDINGS
    return Result(None, state, head, detail, len(expired), base)


# ============================================================================
# GROUP D — read-cap fleet
# ============================================================================

RC_FLEET_RE = re.compile(r"over BUDGET:\s*(\d+)\s*/\s*(\d+).*?over the CAP:\s*(\d+)\s*/\s*(\d+)")


def leg_read_cap_fleet(ctx):
    root = ctx["root"]
    tool = root / "scripts" / "read_cap_check.py"
    if not tool.exists():
        return Result(None, CANNOT, "scripts/read_cap_check.py absent")
    try:
        proc = subprocess.run(
            [sys.executable, str(tool), "--fleet"],
            capture_output=True, text=True, cwd=str(root), timeout=ctx["timeout"],
        )
    except Exception as exc:
        return Result(None, CANNOT, f"read_cap_check --fleet could not run: {exc}")
    out = (proc.stdout or "") + (proc.stderr or "")
    m = RC_FLEET_RE.search(out.replace("\n", " "))
    if not m:
        # Fail closed (finding_lenient_parser_reports_unparseable_as_a_behavior).
        return Result(None, CANNOT,
                      f"read_cap_check --fleet output did not carry the summary line (rc={proc.returncode}) — "
                      "cannot certify; run it directly")
    over_b, tot_b, over_c, tot_c = (int(m.group(i)) for i in (1, 2, 3, 4))
    base = ctx["baseline"].get("D1_read_cap_over_budget")
    head = f"{over_b}/{tot_b} desk(s) over BUDGET · {over_c}/{tot_c} over CAP"
    detail = []
    state = ADVISORY if over_b else PASS
    # DECLARED ASYMMETRY (§6): the read-cap backlog is a standing fleet queue
    # with named owners and dated sittings; pinning red on the LEVEL is
    # permanent-red = silent-green inverted (§3(e)).  The DELTA flips.
    if base is not None and over_b > base:
        detail.append(f"DELTA +{over_b - base} above recorded baseline {base} — a NEW desk crossed budget")
        state = FINDINGS
    if over_c:
        detail.append(f"{over_c} desk(s) over the hard CAP — boot reads are being silently fragmented")
    return Result(None, state, head, detail, over_b, base)


# ============================================================================
# LEG TABLE
# ============================================================================

def build_legs():
    legs = []
    for lid, script, args in SELFTEST_LEGS:
        legs.append(Leg(lid, "A", f"{Path(script).name} --selftest", True,
                        make_selftest_runner(script, args), script))
    legs += [
        Leg("B1", "B", "DOCKET.tsv typing", True, leg_docket, "PROME/DOCKET.tsv"),
        Leg("B2", "B", "GATES.tsv typing", True, leg_gates, "PROME/GATES.tsv"),
        Leg("B3", "B", "WILL_QUEUE.md typing", True, leg_will_queue, "PROME/WILL_QUEUE.md"),
        Leg("C1", "C", "commit subject <=100 chars", False, leg_commit_subjects, "git log -n<N> --format=%s"),
        Leg("C2", "C", "KB Stale_By expiry", False, leg_kb_stale_by, "AGENTS/*/workbook/KB.tsv"),
        Leg("D1", "D", "read-cap fleet budget", False, leg_read_cap_fleet, "scripts/read_cap_check.py --fleet"),
    ]
    return legs


# Legs deliberately NOT in v1 — named so the perimeter line can be honest.
NOT_CHECKED_V1 = [
    "read_cap_check.py has no --selftest (registered in the gap file, expiry-dated)",
    "ledger completeness vs the trading calendar (needs a calendar source; v2)",
    "wiring_census / asmade_audit forward legs (agent-judged output; v2)",
    "mail-loop, watermark and contradiction-against-own-rules classes — "
    "structurally outside a state-based runner (the 9/5 scope ruling)",
]


# ============================================================================
# GAP REGISTER (§1)
# ============================================================================

GAP_FILE = "scripts/validate_all_gaps.tsv"
GAP_COLS = ["leg", "artifact", "reason", "date_added", "expiry", "evidence"]


def load_gaps(root: Path, today: str):
    """Return (gaps_by_leg, expired_rows, register_state, note)."""
    path = root / GAP_FILE
    if not path.exists():
        return {}, [], CANNOT, f"gap register absent at {GAP_FILE} — a missing register suppresses NOTHING"
    rows, expired, gaps = [], [], {}
    with path.open(encoding="utf-8") as fh:
        lines = [ln.rstrip("\n") for ln in fh
                 if ln.strip() and not ln.lstrip().startswith("#")]
    if not lines:
        return {}, [], CANNOT, f"{GAP_FILE} has no header — malformed register suppresses NOTHING"
    header = [c.strip() for c in lines[0].split("\t")]
    missing = [c for c in GAP_COLS if c not in header]
    if missing:
        return {}, [], CANNOT, f"{GAP_FILE} header missing {missing} — malformed register suppresses NOTHING"
    idx = {c: header.index(c) for c in GAP_COLS}
    for ln in lines[1:]:
        f = ln.split("\t")
        if len(f) != len(header):
            return {}, [], CANNOT, f"{GAP_FILE}: row has {len(f)} field(s), header has {len(header)} — suppresses NOTHING"
        rec = {c: f[idx[c]].strip() for c in GAP_COLS}
        if not DATE_RE.match(rec["expiry"]):
            return {}, [], CANNOT, f"{GAP_FILE}: leg {rec['leg']} expiry {rec['expiry']!r} is not YYYY-MM-DD — suppresses NOTHING"
        rows.append(rec)
        if rec["expiry"] < today:
            expired.append(rec)
        else:
            gaps.setdefault(rec["leg"], []).append(rec)
    return gaps, expired, PASS, f"{len(rows)} row(s), {len(expired)} EXPIRED"


# ============================================================================
# BASELINE
# ============================================================================

BASELINE_FILE = "scripts/validate_all_baseline.json"
BUILT_IN_BASELINE = {
    "swept": "2026-09-10",
    "C2_kb_stale_by": None,          # filled by --rebaseline at build
    "D1_read_cap_over_budget": 6,
}


def load_baseline(root: Path):
    path = root / BASELINE_FILE
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return dict(BUILT_IN_BASELINE)
    return dict(BUILT_IN_BASELINE)


# ============================================================================
# RUN
# ============================================================================

def run_suite(root, only=None, timeout=300, commit_scan=DEFAULT_COMMIT_SCAN,
              strict_dates=False, today=None, baseline=None):
    today = today or dt.date.today().isoformat()
    baseline = baseline if baseline is not None else load_baseline(root)
    ctx = {
        "root": root, "timeout": timeout, "commit_scan": commit_scan,
        "strict_dates": strict_dates, "today": today, "baseline": baseline,
    }
    gaps, expired, gap_state, gap_note = load_gaps(root, today)
    results = []
    for leg in build_legs():
        if only and leg.id not in only and leg.group not in only:
            continue
        try:
            res = leg.runner(ctx)
        except Exception as exc:                        # fail closed
            res = Result(leg, CANNOT, f"leg raised {type(exc).__name__}: {exc}")
        res.leg = leg
        if res.state in (FINDINGS, CANNOT) and leg.id in gaps:
            row = gaps[leg.id][0]
            res.state = GAP
            res.headline = f"{res.headline}  [DECLARED-GAP, expires {row['expiry']}: {row['reason']}]"
        results.append(res)
    return results, gaps, expired, gap_state, gap_note, today


def verdict(results, expired, gap_state):
    if gap_state == CANNOT:
        return 2
    if expired:
        return 2
    for r in results:
        if r.state == CANNOT:
            return 2
    for r in results:
        # ⚠️ The verdict keys on the STATE, never on a per-leg boolean.  v1's
        # first selftest run caught the inverse: leg D1 computed FINDINGS above
        # its baseline and the verdict could not read it, because the flip test
        # ALSO required leg.flips — a delta-keyed leg is advisory at its LEVEL
        # and flipping at its DELTA, and one boolean cannot say both.
        # [[finding_guard_correctness_and_wiring_are_independent]]
        if r.state == FINDINGS:
            return 1
    return 0


SYMBOL = {PASS: "✅", FINDINGS: "❌", CANNOT: "⛔", GAP: "🟡", ADVISORY: "⚠️"}


def report(results, gaps, expired, gap_state, gap_note, today, rc, root, only):
    lines = []
    scope = "all legs" if not only else "legs " + ",".join(sorted(only))
    lines.append(
        f"{TOOL} {VERSION} — {today} — perimeter: {len(results)} leg(s) ({scope}); "
        f"gap register {gap_note}"
    )
    for r in results:
        flip = "structural" if r.leg.flips else "delta-keyed"
        lines.append(f"  {SYMBOL.get(r.state,'?')} {r.leg.id} {r.leg.label:<38} [{r.state}, {flip}] {r.headline}")
        for d in r.detail[:6]:
            lines.append(f"        · {d}")
        if len(r.detail) > 6:
            lines.append(f"        · (+{len(r.detail)-6} more not listed)")   # §4
    for row in expired:
        lines.append(f"  ⛔ EXPIRED GAP {row['leg']}: {row['reason']} (expired {row['expiry']}) — re-verify or re-date")
    if gap_state == CANNOT:
        lines.append(f"  ⛔ GAP REGISTER: {gap_note}")

    lines.append("")
    lines.append("  NOT CHECKED by this tool (v1) — stated so a green line cannot be over-read:")
    for n in NOT_CHECKED_V1:
        lines.append(f"     · {n}")
    lines.append("  A PASS here proves: the registered instruments pass their OWN selftests and the three")
    lines.append("  decision ledgers are well-TYPED. It proves NOTHING about whether a finding was acted on,")
    lines.append("  whether mail was read, whether a desk contradicts its own stated rules, or about external")
    lines.append("  truth. It is NOT the retired per-push review seat (scope RULED 2026-09-05).")
    lines.append("")

    n_pass = sum(1 for r in results if r.state == PASS)
    n_find = sum(1 for r in results if r.state == FINDINGS)
    n_adv = sum(1 for r in results if r.state == ADVISORY)
    n_cant = sum(1 for r in results if r.state == CANNOT)
    n_gap = sum(1 for r in results if r.state == GAP)
    tally = f"{n_pass} PASS · {n_find} FINDINGS · {n_adv} ADVISORY · {n_gap} DECLARED-GAP · {n_cant} CANNOT-CERTIFY"
    if rc == 0:
        lines.append(f"✅ {TOOL} 0 CLEAN: {tally}")
    elif rc == 1:
        lines.append(f"❌ {TOOL} 1 FINDINGS: {tally} — owner: DAEDALUS (tooling) / the named ledger owner; "
                     f"next move: fix the flagged leg, then re-run `python3 scripts/validate_all.py`")
    else:
        lines.append(f"⛔ {TOOL} 2 CANNOT-CERTIFY: {tally} — a leg could not run or the gap register is stale; "
                     f"this is a LEG FAILURE, never assume quiet (CHECK_STANDARD §9)")
    return "\n".join(lines)


# ============================================================================
# SELFTEST (§3 (a) capable case + (b) clean case, both watched)
# ============================================================================

def _write(p: Path, text: str):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")


def _fixture_repo(tmp: Path, *, docket_ok=True, gates_ok=True, wq_ok=True,
                  gap_expiry="2099-01-01", gap_rows=True, gap_broken=False):
    """Build a FROZEN fixture tree — never a live surface (root rule: a
    regression test pinned to a live surface rots on the next edit)."""
    d = tmp / "PROME"
    docket = ["# comment banner", "2026-09-10\tthing\tDAEDALUS\tPENDING\tptr\tnote"]
    docket.append("2026-08-19..2026-08-21\trange row\tPROME\tPENDING\tptr\tnote")
    if not docket_ok:
        docket.append("not-a-date\tbad row\tX\tPENDING\tptr\tnote")
        docket.append("2026-09-11\tshort row\tX")
    _write(d / "DOCKET.tsv", "\n".join(docket) + "\n")

    ghdr = "gate_id\tregistered\towner\tcondition\tconsequence_on_fire\tstate\tlast_checked\tsource\tconsumed_by\tscannable\tdefinition_surface\treview_by"
    grows = ["G-1\t2026-06-26\tLIQUID\tc\tk\tLIVE\t2026-09-09\ts\tPROME\tYES\tdoc\t2026-09-20"]
    if not gates_ok:
        grows.append("G-2\t2026-06-26\tX\tc\tk\tLIVE\t2026-09-09\ts\tPROME\tYES\tdoc")   # short
        grows.append("G-3\tnotadate\tX\tc\tk\tLIVE\t2026-09-09\ts\tPROME\tYES\tdoc\t2026-09-20")
    _write(d / "GATES.tsv", "# banner\n" + ghdr + "\n" + "\n".join(grows) + "\n")

    wq = ["# WILL QUEUE", "", "| # | Item | Type | Needed by | Since | PROME rec | Notes |",
          "|---|---|---|---|---|---|---|",
          "| 201 | a | [Approve] | 2026-09-10 | 9/9 | rec | n |"]
    if not wq_ok:
        wq.append("| 201 | dup | [Approve] | 2026-09-10 | 9/9 | rec | n |")
        wq.append("| 202 | short row | [Approve] | 2026-09-10 |")
    _write(d / "WILL_QUEUE.md", "\n".join(wq) + "\n")

    kb = tmp / "AGENTS" / "TESTDESK" / "workbook" / "KB.tsv"
    _write(kb, "ID\tFact\tStatus\tStale_By\n"
               "KB-1\tx\tACTIVE\t2099-01-01\n"
               "KB-2\ty\tSUPERSEDED\t2020-01-01\n")

    g = tmp / "scripts"
    if gap_broken:
        _write(g / "validate_all_gaps.tsv", "leg\treason\n" + "A1\tbroken\n")
    elif gap_rows:
        _write(g / "validate_all_gaps.tsv",
               "# gap register\n"
               "leg\tartifact\treason\tdate_added\texpiry\tevidence\n"
               f"Z9\tnone\tfixture row\t2026-09-10\t{gap_expiry}\tfixture\n")
    else:
        _write(g / "validate_all_gaps.tsv",
               "leg\tartifact\treason\tdate_added\texpiry\tevidence\n")
    return tmp


def selftest():
    """Drills. Each builds a REAL defective or clean fixture input and WATCHES
    the line print — never a mutated live surface (§3 monkeypatched-legs form)."""
    drills, failures = [], []

    def drill(name, fn, want_state, want_rc=None):
        try:
            got_state, got_rc, line = fn()
        except Exception as exc:
            drills.append((name, "RAISED", str(exc), False))
            failures.append(name)
            return
        ok = got_state == want_state and (want_rc is None or got_rc == want_rc)
        drills.append((name, got_state, line, ok))
        if not ok:
            failures.append(f"{name}: got {got_state}/rc{got_rc}, want {want_state}/rc{want_rc}")

    def with_fixture(**kw):
        def _inner(legid):
            def _run():
                with tempfile.TemporaryDirectory() as td:
                    root = _fixture_repo(Path(td), **kw)
                    base = {"C2_kb_stale_by": 0, "D1_read_cap_over_budget": 6}
                    res, gaps, expired, gs, gn, today = run_suite(
                        root, only={legid}, today="2026-09-10", baseline=base)
                    rc = verdict(res, expired, gs)
                    r = res[0]
                    return r.state, rc, r.headline
            return _run
        return _inner

    # --- B1 DOCKET: capable case (a real mistyped row) then clean case
    drill("B1 capable: bad date + short row -> FINDINGS, rc1",
          with_fixture(docket_ok=False)("B1"), FINDINGS, 1)
    drill("B1 clean: dates + a legitimate DATE RANGE -> PASS, rc0",
          with_fixture()("B1"), PASS, 0)

    # --- B2 GATES
    drill("B2 capable: short row + bad date -> FINDINGS, rc1",
          with_fixture(gates_ok=False)("B2"), FINDINGS, 1)
    drill("B2 clean -> PASS, rc0", with_fixture()("B2"), PASS, 0)

    # --- B3 WILL_QUEUE
    drill("B3 capable: duplicate id + short row -> FINDINGS, rc1",
          with_fixture(wq_ok=False)("B3"), FINDINGS, 1)
    drill("B3 clean -> PASS, rc0", with_fixture()("B3"), PASS, 0)

    # --- B1 instrument failure: an EMPTY ledger must never read as clean
    def b1_empty():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            _write(root / "PROME" / "DOCKET.tsv", "# only a banner\n")
            res, g, e, gs, gn, t = run_suite(root, only={"B1"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("B1 empty ledger -> CANNOT-CERTIFY, rc2 (never clean)", b1_empty, CANNOT, 2)

    # --- absent file
    def b2_absent():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            (root / "PROME" / "GATES.tsv").unlink()
            res, g, e, gs, gn, t = run_suite(root, only={"B2"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("B2 absent file -> CANNOT-CERTIFY, rc2", b2_absent, CANNOT, 2)

    # --- gap register: EXPIRED row re-flags itself to rc 2
    def gap_expired():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td), gap_expiry="2026-01-01")
            res, g, e, gs, gn, t = run_suite(root, only={"B1"}, today="2026-09-10", baseline={})
            return ("EXPIRED" if e else "NONE"), verdict(res, e, gs), gn
    drill("gap register EXPIRED row -> rc2 (re-flags itself)", gap_expired, "EXPIRED", 2)

    # --- gap register: MALFORMED suppresses nothing and says so
    def gap_broken():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td), gap_broken=True)
            res, g, e, gs, gn, t = run_suite(root, only={"B1"}, today="2026-09-10", baseline={})
            return gs, verdict(res, e, gs), gn
    drill("gap register MALFORMED -> CANNOT-CERTIFY, rc2, suppresses nothing", gap_broken, CANNOT, 2)

    # --- gap register: an UNEXPIRED row converts a FINDINGS leg to DECLARED-GAP
    def gap_covers():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td), docket_ok=False)
            (root / "scripts" / "validate_all_gaps.tsv").write_text(
                "leg\tartifact\treason\tdate_added\texpiry\tevidence\n"
                "B1\tPROME/DOCKET.tsv\tfixture defect accepted\t2026-09-10\t2099-01-01\tfixture\n",
                encoding="utf-8")
            res, g, e, gs, gn, t = run_suite(root, only={"B1"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("gap register UNEXPIRED row -> DECLARED-GAP, rc0", gap_covers, GAP, 0)

    # --- C2 delta: above baseline flips, at baseline does not
    def c2_delta():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            kb = root / "AGENTS" / "TESTDESK" / "workbook" / "KB.tsv"
            kb.write_text("ID\tFact\tStatus\tStale_By\n"
                          "KB-1\tx\tACTIVE\t2026-01-01\n"
                          "KB-2\ty\tACTIVE\t2099-01-01\n", encoding="utf-8")
            res, g, e, gs, gn, t = run_suite(root, only={"C2"}, today="2026-09-10",
                                             baseline={"C2_kb_stale_by": 0})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("C2 one expired row over baseline 0 -> FINDINGS, rc1 (delta escalates)",
          c2_delta, FINDINGS, 1)

    def c2_at_baseline():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            kb = root / "AGENTS" / "TESTDESK" / "workbook" / "KB.tsv"
            kb.write_text("ID\tFact\tStatus\tStale_By\n"
                          "KB-1\tx\tACTIVE\t2026-01-01\n", encoding="utf-8")
            res, g, e, gs, gn, t = run_suite(root, only={"C2"}, today="2026-09-10",
                                             baseline={"C2_kb_stale_by": 1})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("C2 at recorded baseline -> ADVISORY, does not flip (declared asymmetry)",
          c2_at_baseline, ADVISORY, 0)

    # --- C2 positive control: zero parseable Stale_By cells is NEVER clean
    def c2_control():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            kb = root / "AGENTS" / "TESTDESK" / "workbook" / "KB.tsv"
            kb.write_text("ID\tFact\tStatus\tStale_By\nKB-1\tx\tACTIVE\t\n", encoding="utf-8")
            res, g, e, gs, gn, t = run_suite(root, only={"C2"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("C2 positive control FAILS (0 dated cells) -> CANNOT-CERTIFY, rc2",
          c2_control, CANNOT, 2)

    # --- A-leg: a sub-check that RETURNS rc2 must take the run to rc2
    def a_leg_cannot():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            # no scripts/*.py in the fixture => tool absent => CANNOT
            res, g, e, gs, gn, t = run_suite(root, only={"A1"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("A1 sub-check tool ABSENT -> CANNOT-CERTIFY, rc2 (never silently skipped)",
          a_leg_cannot, CANNOT, 2)

    # --- A-leg: a sub-check that exits 1 must surface as FINDINGS
    def a_leg_findings():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            _write(root / "scripts" / "corrections_boot_check.py",
                   "import sys\nprint('FAKE-CHECK 1 FINDINGS: 3 rows')\nsys.exit(1)\n")
            res, g, e, gs, gn, t = run_suite(root, only={"A1"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("A1 sub-check rc=1 -> FINDINGS, rc1 (aggregate cannot hide a member)",
          a_leg_findings, FINDINGS, 1)

    # --- A-leg: a sub-check that CRASHES must not read as findings-or-clean
    def a_leg_crash():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            _write(root / "scripts" / "corrections_boot_check.py", "raise SystemExit(3)\n")
            res, g, e, gs, gn, t = run_suite(root, only={"A1"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("A1 sub-check rc=3 -> CANNOT-CERTIFY, rc2", a_leg_crash, CANNOT, 2)

    # --- A-leg clean case
    def a_leg_clean():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            _write(root / "scripts" / "corrections_boot_check.py",
                   "print('FAKE-CHECK 0 OK: clean')\n")
            res, g, e, gs, gn, t = run_suite(root, only={"A1"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("A1 sub-check rc=0 -> PASS, rc0 (clean line watched)", a_leg_clean, PASS, 0)

    # --- C1 positive control: an empty git log is an instrument failure
    def c1_control():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))       # not a git repo
            res, g, e, gs, gn, t = run_suite(root, only={"C1"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("C1 no git history -> CANNOT-CERTIFY, rc2 (absence is never a finding)",
          c1_control, CANNOT, 2)

    # --- D1 unparseable output fails CLOSED
    def d1_unparseable():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            _write(root / "scripts" / "read_cap_check.py", "print('something else entirely')\n")
            res, g, e, gs, gn, t = run_suite(root, only={"D1"}, today="2026-09-10", baseline={})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("D1 unparseable summary -> CANNOT-CERTIFY, rc2 (fails closed)",
          d1_unparseable, CANNOT, 2)

    # --- D1 delta above baseline flips
    def d1_delta():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            _write(root / "scripts" / "read_cap_check.py",
                   "print('  desks with >=1 boot read over BUDGET: 9/37 "
                   "\\u00b7 over the CAP: 1/37')\n")
            res, g, e, gs, gn, t = run_suite(root, only={"D1"}, today="2026-09-10",
                                             baseline={"D1_read_cap_over_budget": 6})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("D1 9/37 over baseline 6 -> FINDINGS (delta flips, level does not)",
          d1_delta, FINDINGS, 1)

    def d1_at_baseline():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            _write(root / "scripts" / "read_cap_check.py",
                   "print('  desks with >=1 boot read over BUDGET: 6/37 "
                   "\\u00b7 over the CAP: 1/37')\n")
            res, g, e, gs, gn, t = run_suite(root, only={"D1"}, today="2026-09-10",
                                             baseline={"D1_read_cap_over_budget": 6})
            return res[0].state, verdict(res, e, gs), res[0].headline
    drill("D1 6/37 at baseline -> ADVISORY, rc0 (no permanent red)", d1_at_baseline, ADVISORY, 0)

    # --- rc precedence: 2 dominates 1
    def rc_precedence():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td), docket_ok=False)     # B1 FINDINGS
            (root / "PROME" / "GATES.tsv").unlink()             # B2 CANNOT
            res, g, e, gs, gn, t = run_suite(root, only={"B"}, today="2026-09-10", baseline={})
            states = {r.leg.id: r.state for r in res}
            return f"{states.get('B1')}+{states.get('B2')}", verdict(res, e, gs), "precedence"
    drill("rc precedence: FINDINGS + CANNOT -> rc2 (2 dominates 1)",
          rc_precedence, f"{FINDINGS}+{CANNOT}", 2)

    # --- the perimeter/NOT-CHECKED line is present on a CLEAN run (§2)
    def perimeter_line():
        with tempfile.TemporaryDirectory() as td:
            root = _fixture_repo(Path(td))
            res, g, e, gs, gn, t = run_suite(root, only={"B"}, today="2026-09-10", baseline={})
            rc = verdict(res, e, gs)
            txt = report(res, g, e, gs, gn, t, rc, root, {"B"})
            ok = ("NOT CHECKED by this tool" in txt
                  and "A PASS here proves" in txt
                  and "NOT the retired per-push review seat" in txt)
            return ("PRESENT" if ok else "MISSING"), rc, "perimeter+what-a-PASS-proves"
    drill("clean run prints perimeter + what-a-PASS-does-NOT-prove (§2)",
          perimeter_line, "PRESENT", 0)

    print(f"{TOOL} SELFTEST — {len(drills)} drill(s), fixture-only (no live surface touched)")
    for name, state, line, ok in drills:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        print(f"        got [{state}] {str(line)[:110]}")
    n_ok = sum(1 for *_x, ok in drills if ok)
    if failures:
        print(f"❌ SELFTEST 1: {n_ok}/{len(drills)} drills behaved")
        for f in failures:
            print(f"     · {f}")
        return 1
    print(f"✅ SELFTEST 0: {n_ok}/{len(drills)} drills behaved")
    return 0


# ============================================================================
# CLI
# ============================================================================

def main(argv=None):
    ap = argparse.ArgumentParser(
        description="validate_all.py v1 — the fleet mechanical-suite runner (DAEDALUS). "
                    "NOT the retired per-push review seat (scope RULED 2026-09-05).")
    ap.add_argument("--selftest", action="store_true", help="run the fixture drills and exit")
    ap.add_argument("--list", action="store_true", help="list the legs and exit")
    ap.add_argument("--only", default="", help="comma-separated leg ids or group letters (A,B,C,D)")
    ap.add_argument("--timeout", type=int, default=300, help="per-leg subprocess timeout, seconds")
    ap.add_argument("--commit-scan", type=int, default=DEFAULT_COMMIT_SCAN,
                    help="how many commit subjects leg C1 scans")
    ap.add_argument("--strict-dates", action="store_true",
                    help="reject the DOCKET date-RANGE form (reproduces the 69-flag acceptance-set case)")
    ap.add_argument("--rebaseline", action="store_true",
                    help="write the CURRENT advisory levels to scripts/validate_all_baseline.json")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--root", default=None, help="repo root override (testing)")
    args = ap.parse_args(argv)

    if args.selftest:
        return selftest()

    root = Path(args.root) if args.root else repo_root()

    if args.list:
        print(f"{TOOL} {VERSION} legs — perimeter AGENTS/DAEDALUS/CHECKS.tsv")
        for leg in build_legs():
            print(f"  {leg.id}  [{'structural ' if leg.flips else 'delta-keyed'}]  {leg.label:<38} {leg.perimeter}")
        print("  NOT in v1:")
        for n in NOT_CHECKED_V1:
            print(f"     · {n}")
        return 0

    only = {t.strip() for t in args.only.split(",") if t.strip()} or None
    results, gaps, expired, gap_state, gap_note, today = run_suite(
        root, only=only, timeout=args.timeout, commit_scan=args.commit_scan,
        strict_dates=args.strict_dates)
    rc = verdict(results, expired, gap_state)

    if args.rebaseline:
        base = load_baseline(root)
        for r in results:
            if r.leg.id == "C2":
                base["C2_kb_stale_by"] = r.count
            if r.leg.id == "D1":
                base["D1_read_cap_over_budget"] = r.count
        base["swept"] = today
        (root / BASELINE_FILE).write_text(json.dumps(base, indent=2) + "\n", encoding="utf-8")
        print(f"{TOOL}: baseline written to {BASELINE_FILE}: {json.dumps(base)}")
        return 0

    if args.json:
        print(json.dumps({
            "tool": TOOL, "version": VERSION, "date": today, "rc": rc,
            "legs": [{"id": r.leg.id, "group": r.leg.group, "label": r.leg.label,
                      "state": r.state, "flips": r.leg.flips, "headline": r.headline,
                      "count": r.count, "baseline": r.baseline, "detail": r.detail}
                     for r in results],
            "expired_gaps": [g["leg"] for g in expired],
            "gap_register": gap_note,
        }, indent=2))
        return rc

    print(report(results, gaps, expired, gap_state, gap_note, today, rc, root, only))
    return rc


if __name__ == "__main__":
    sys.exit(main())
