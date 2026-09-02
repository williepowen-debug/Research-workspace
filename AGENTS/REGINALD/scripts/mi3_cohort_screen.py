#!/usr/bin/env python3
"""MI3 (hidden-CRE) cohort screen — FFIEC CDR REST/JWT, RetrieveFacsimile/SDF.

================================ RUNBOOK ================================
⚠️  READING THIS RUNBOOK: every FIGURE below is a DATED SNAPSHOT (2026Q2 unless
    stated); every RULE is permanent. A runbook is a teaching surface, and a
    teaching surface ages like data - its authority is exactly what stops anyone
    freshness-checking the numbers inside it. Trust the rules; RE-MEASURE the
    figures each run. (Labelled 2026-08-20 after LESSONS.md was found teaching
    a WAL NDFI figure that had quadrupled while its rule stayed correct.)

🔴 RULING 2026-08-28 — v1a DEFINITION REVISED. The prior v1a formula
    `MI3 / (item 4 + item 9.a + item 9.b)` is SUPERSEDED. The current formula is
    `v1a = MI3 / (item 4 + item 9.a)` — drop item 9.b (RCONJ464 for 041/051;
    the 9.b component for 031). Basis: OZK's `RCONPV09 ≡ RCON2746` across 6 of 6
    quarters proves MI3 is a 9.a mirror, not a distribution across 9.a and 9.b;
    item 9.b is a heterogeneous residual catchall unrelated to the MI3 loan
    population; cross-bank comparability requires a denominator matched to the
    numerator's residence. See `reports/2026-08-13_MI3_cohort_rerun.md`
    ADDENDUM 2026-08-28 and the WAL packet at `AGENTS/WAL/inbox/2026-08-28_
    from-REGINALD_ruling-v1a-is-4-plus-9a-only-...md`. The 2026-11-07 cohort
    refresh applies this at the code level; until then any prior-run cohort
    v1a Q2-2026 LEVEL is superseded and any prior-run RANK is UNVERIFIED (not
    arithmetically recoverable — needs the re-run).
    [[finding_a_teaching_surface_ages_like_data]]
WHAT THIS MEASURES
  Numerator  RCON/RCFD 2746 — "Loans to finance commercial real estate,
  construction, and land development activities (NOT secured by real estate)
  included in Schedule RC-C part I, items 4 AND 9, column B" (sched RCCI, M3).

  TWO BASES, ALWAYS BOTH — the choice inverts the cross-bank rank:
    v1  (LEGACY, continuity only) : MI3 / item 4
    v1a (UNIFORM, cross-bank)     : MI3 / (item 4 + item 9) = the numerator's
                                    OWN stated parent per its FFIEC label.
  Item-9 share of the base ran 5.5%-65.8% across this cohort [MEASURED 2026Q2 -
  a DATED SNAPSHOT, re-measure each run], so v1 is NOT cross-bank comparable.
  ⚠️ THE RULE IS PERMANENT ("v1 is not cross-bank comparable"); THE RANGE IS DATA.
  See finding_normalization_choice_picks_opposite_winners.

  AND THE DOLLARS. A ratio screen structurally cannot see a book migrating
  up-cap: at 2026Q2 MTB held the cohort's LARGEST absolute MI3 book ($4.95B)
  at an unremarkable ratio, because its C&I denominator is huge. mi3_k and
  mi3_yoy_pct are therefore FIRST-CLASS OUTPUT, not an optional derivation.
  ⚠️ "$4.95B / MTB" IS A 2026Q2 SNAPSHOT, NOT A STANDING FACT - the largest
  absolute book may be a different bank next run. The RULE (report dollars, a
  ratio screen cannot see an up-cap migration) does not depend on which name.

⚠️  V1a != V1 FENCE. MI3 is CRE *not secured by RE*. Secured books (WAL office
    + the $99M life-science credit, OZK RESG) are a DIFFERENT OBJECT and are
    not measured here. "The hidden-CRE screen fell" is one keystroke from
    "the CRE thesis fell", and the second is false.

COHORT (definition + rationale — a NAMED cohort, never a population)
  Every name the legacy v1 screen scored (OZK/WAL/EGBN/ZION/SSB)
  + the REGINALD Convergence-Matrix watchlist (CFG/BKU/SBCF/AMTB/FLG)
  + clean large-cap benchmarks (MTB/HBAN/VLY)
  + one NDFI-heavy control (CUBI).
  RSSDs are BANK-LEVEL filers resolved from RetrievePanelOfReporters — never
  holdcos, and never the affiliated trust companies (WAL trust = RSSD 5805451,
  a separate filer; do not conflate).
  ⚠️ OPEN QUESTION carried 2026-08-13, deliberately NOT closed by the script:
  the cohort was selected by RATIO-era priors, and the 2026Q2 run found the
  DOLLARS pooling at names admitted as clean benchmarks. If the screen's
  purpose is "where is hidden CRE pooling", the selection rule may need
  re-stating. See registry/NOTES.md and ROADMAP. Do not silently grow the list.

QUARTERS
  Rolling: same-quarter prior year (for YoY) + the last three published.
  Prior-year quarter must stay in QUARTERS or mi3_yoy_pct degrades to UNKNOWN.

CADENCE + READ-PATH
  Quarterly, ~45d after quarter-end (Call Reports file ~30d after; CDR
  availability lags). Next due 2026-11-07 for 2026Q3.
  ⚠️ HARD PREREQUISITE, and the dates nearly collide: the FFIEC CDR JWT
  EXPIRES 2026-11-05 — two days before the next scheduled run. Renewal is a
  WILL action (PWS account login). Registered on CALENDAR so a lapsed window
  is visible rather than discovered by archaeology (deferral rule).

CREDENTIALS
  FORGE/tools/market-data/.env : FFIEC_CDR_USERNAME, FFIEC_CDR_TOKEN (gitignored).
  ⚠️ DESKTOP ONLY. .env does not travel with git; the laptop lacks both keys
  and env_doctor announces the gap at boot. Running this on the laptop fails
  at creds(), by design, rather than emitting a partial cohort.

TRAPS (each cost a real session — do not re-discover them)
  1. Header is literally "Authentication:", NOT "Authorization:".
  2. `dataSeries: Call` is a HEADER, not a query param (else 500 / code 5001).
  3. A 403 is the Azure WAF rejecting python-urllib's User-Agent — NOT an auth
     failure. curl succeeds on identical headers. Real auth failures are 401,
     or 500 with codes 5001/5003. Do not debug the token on a 403.
  4. RetrieveFacsimile returns the SDF as BASE64 INSIDE A JSON STRING.
  5. "Item 4"/"item 9" are CONCEPTS, not MDRMs — see INSTRUMENT RESOLUTION below.

USAGE
  python3 mi3_cohort_screen.py                     # normal run (guards armed)
  python3 mi3_cohort_screen.py --no-cache          # ignore /tmp facsimile cache
  python3 mi3_cohort_screen.py --accept-restatement "FFIEC amended filing X"
                                                   # ONLY way to overwrite a
                                                   # cell that fails to reproduce
Exit 0 = wrote. Exit 2 = guard tripped, NOTHING written (fail loud, not partial).
=========================================================================
"""
import argparse
import base64
import csv
import json
import os
import datetime
import subprocess
import sys
from pathlib import Path

ROOT = Path(subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True,
                           text=True, check=True).stdout.strip())
ENV = ROOT / "FORGE/tools/market-data/.env"
CACHE = Path("/tmp/mi3/fac")
BASE = "https://ffieccdr.azure-api.us/public"
OUT_TSV = ROOT / "AGENTS/REGINALD/workbook/MI3_COHORT.tsv"
OUT_MD = ROOT / "AGENTS/REGINALD/workbook/MI3_COHORT_SUMMARY.md"

COHORT = [
    ("OZK",  107244,  "BANK OZK",                       "legacy-screen + matrix"),
    ("WAL",  3138146, "WESTERN ALLIANCE BANK",          "legacy-screen + matrix"),
    ("EGBN", 2652092, "EAGLEBANK",                      "legacy-screen + matrix"),
    ("ZION", 276579,  "ZIONS BANCORPORATION, N.A.",     "legacy-screen clean cell"),
    ("SSB",  1929247, "SOUTHSTATE BANK, N.A.",          "legacy-screen clean cell"),
    ("CFG",  3303298, "CITIZENS BANK, N.A.",            "matrix watchlist"),
    ("BKU",  3938186, "BANKUNITED, N.A.",               "matrix watchlist (FL small-tier)"),
    ("SBCF", 34537,   "SEACOAST NATIONAL BANK",         "matrix watchlist (FL small-tier)"),
    ("AMTB", 83638,   "AMERANT BANK, N.A.",             "matrix watchlist (FL small-tier)"),
    ("FLG",  694904,  "FLAGSTAR BANK, N.A.",            "matrix watchlist"),
    ("MTB",  501105,  "MANUFACTURERS AND TRADERS TRUST", "clean large-cap benchmark"),
    ("HBAN", 12311,   "HUNTINGTON NATIONAL BANK",       "clean large-cap benchmark"),
    ("VLY",  229801,  "VALLEY NATIONAL BANK",           "clean large-cap benchmark"),
    ("CUBI", 2354985, "CUSTOMERS BANK",                 "NDFI-heavy control"),
]

# ⚠️ CONTIGUOUS BY REQUIREMENT, NOT BY CONVENIENCE (Will-approved 2026-08-13).
# The original grid was Q2-25 · Q4-25 · Q1-26 · Q2-26 — it SKIPPED 2025Q3, which is the
# quarter containing OZK's entire -36% MI3 step. Every figure published off that grid was
# measured ACROSS a discontinuity it could not show, and two-thirds of the headline
# "-64% YoY" turned out to be one quarter. A gapped window CANNOT distinguish a STEP from
# a TREND. Keep this list CONTIGUOUS when rolling it forward; add at the front, drop at
# the back, never sample.
QUARTERS = [
    "9/30/2023", "12/31/2023", "3/31/2024", "6/30/2024",
    "9/30/2024", "12/31/2024", "3/31/2025", "6/30/2025",
    "9/30/2025", "12/31/2025", "3/31/2026", "6/30/2026",
]
# Same quarter, prior year — derived from QUARTERS so it cannot drift out of sync.
YOY_PAIRS = {q: p for q, p in zip(QUARTERS[4:], QUARTERS[:-4])}

# ★ TWO-CLOCK HEADER (PAT-044) — emitted by the WRITER, never hand-added.
# Registered cadence: quarterly, ~45d after quarter-end (Call Reports file ~30d out,
# CDR availability lags). ROLL THIS WITH `QUARTERS` — it is the ledger's own
# "quiet until" date, read by scripts/ledger_staleness.py (`Cadence: SCHEDULED
# next_due=`). A stale NEXT_DUE makes a correctly-quiet ledger nag every closeout,
# which is how a guard family trains its reader to ignore it.
NEXT_DUE = "2026-11-07"


def header_lines(data_refresh, attention=None):
    """The PAT-044 comment block written ABOVE the column header.

    ⛔ Hand-adding a `#` line to MI3_COHORT.tsv does NOT work and is not a shortcut:
    this script rewrites the file via csv.DictWriter on every run and would silently
    delete it (`finding_a_fix_can_relocate_a_constraint_and_report_it_removed`). The
    header is emitted HERE so it survives the next run, and BOTH readers of this file
    skip comments (`decomment()` below + mi3_guard_selftest.load()).

    Markers must stay FRONT-LOADED on their lines — ledger_staleness only honours a
    `Cadence:` marker that starts before its MARKER_COL_CAP."""
    att = attention or data_refresh
    return [
        f"# Last real data refresh: {data_refresh} — FFIEC CDR REST/JWT "
        "(RetrieveFacsimile/SDF); every row at the FFIEC primary, both bases reported.",
        f"# Last attention check: {att} — generated by scripts/mi3_cohort_screen.py; "
        "guards (coverage/schema/repro) ran green or the run aborted before writing.",
        f"# Cadence: SCHEDULED next_due={NEXT_DUE} — quarterly, ~45d after quarter-end. "
        "The data clock is old ON PURPOSE between runs; this is the quiet-until date.",
        "# ⛔ GENERATED FILE — do not hand-edit and do not hand-add header lines; the "
        "writer rewrites it wholesale. Change scripts/mi3_cohort_screen.py instead.",
        "# ⚠️ v1 = MI3 ÷ item 4 (legacy, continuity only). v1a = MI3 ÷ (item 4 + item 9.a) "
        "— the ONLY basis valid for cross-bank claims; the basis choice INVERTS the rank.",
        "# ⛔ 37.6% (OZK) is KILL-ON-SIGHT — no reproducible provenance at any quarter. "
        "repro_guard() exists to catch that class; run scripts/mi3_guard_selftest.py.",
    ]


def decomment(lines):
    """Strip PAT-044 header comments before csv parsing.

    ⚠️ Both readers of MI3_COHORT.tsv MUST use this. A bare csv.DictReader takes the
    first '#' line as the column header and then silently returns unusable rows — which
    would disarm repro_guard(), the guard that catches the 37.6% class."""
    return [ln for ln in lines if not ln.lstrip().startswith("#")]

# ★ STEP DETECTOR (Will-approved 2026-08-13). A reporting/classification change and an
# economic runoff look identical at the endpoints and completely different quarter to
# quarter: a re-designation moves the LABEL in one quarter while the BOOK barely moves.
# Flags |QoQ MI3| > 25% while |QoQ total loans| < 5%. This is a PROMPT TO LOOK, never a
# finding — it cannot distinguish a legitimate re-designation from a disclosure narrowing,
# and the Call Report alone never will. Calibrated on the OZK 2025Q3 event (MI3 -36.0%,
# total loans -0.4%), which it must catch.
STEP_MI3_PCT = 25.0
STEP_LOANS_PCT = 5.0

# ⚠️ INSTRUMENT RESOLUTION (finding_registry_names_a_concept_tool_resolves_an_instrument).
# "Item 4" and "item 9" are CONCEPTS; the MDRM carrying them depends on the FORM:
#   FFIEC 041/051 (domestic-only): RCON series; item-4 and item-9b TOTALS printed.
#   FFIEC 031 (foreign offices — CFG/MTB/HBAN/FLG/VLY/AMTB here): RCFD series, and
#     the item-4 / item-9b TOTAL lines are NOT printed, only their 4a/4b, 9b1/9b2 parts.
# A naive RCON1766-only screen returns None for every 031 filer — which reads as
# "these banks have no hidden CRE." That is a FABRICATED CLEAN RESULT, and it is
# the failure this resolver + the STATUS_VOCAB guard below exist to make impossible.
PREFIXES = ("RCON", "RCFD")    # domestic-office preferred, consolidated fallback
NUM_CODES = ["2746"]
I4_TOTAL = ["1766"]
I4_PARTS = ["1763", "1764"]
I9A_CODES = ["J454"]
I9B_TOTAL = ["J464"]
I9B_PARTS = ["1545", "J451"]
TOTAL_CODES = ["2122"]
ASSET_CODES = ["2170"]

COLS = ["ticker", "rssd", "name", "cohort_reason", "quarter", "status", "mi3_zero_class",
        "mi3_k", "mi3_qoq_pct", "mi3_yoy_pct", "loans_qoq_pct", "step_flag",
        "item4_k", "item9a_k", "item9b_k", "item9_k",
        "v1_pct", "v1a_pct", "item9_share_of_base_pct",
        "total_loans_k", "total_assets_k",
        "num_mdrm", "denom_v1_mdrm", "denom_v1a_mdrm", "repro_vs_prior"]

# STATE VOCABULARY (STATE_VOCABULARY.md class; zero != unknown != not-applicable).
# SCORED_STATUSES must carry every ratio/dollar cell; the others must carry NONE.
SCORED_STATUSES = {"OK", "OK-V1-ONLY"}
UNSCORED_STATUSES = {"NOT-REPORTED", "DENOM-MISSING", "PULL-FAILED"}
STATUS_VOCAB = SCORED_STATUSES | UNSCORED_STATUSES
ZERO_VOCAB = {"REPORTED-ZERO", "NONZERO", "UNKNOWN"}
# Columns that MUST be non-empty on a scored row (v1a/item9 excluded — OK-V1-ONLY
# is a legitimate scored state where item 9 genuinely is not reported).
REQUIRED_ON_SCORED = ["mi3_k", "item4_k", "v1_pct", "num_mdrm", "denom_v1_mdrm"]
REPRO_TOL_PCT = 0.02          # pp tolerance on v1/v1a; dollars must match exactly


class GuardTripped(Exception):
    """Raised when output would be wrong or silently incomplete. Nothing is written."""


def creds():
    env = {}
    with open(ENV) as fh:
        for line in fh:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    u, t = env.get("FFIEC_CDR_USERNAME"), env.get("FFIEC_CDR_TOKEN")
    if not u or not t:
        sys.exit("FFIEC_CDR_USERNAME / FFIEC_CDR_TOKEN missing from " + str(ENV) +
                 "\n(Expected on the DESKTOP only — .env does not travel with git.)")
    return u, t


def facsimile(user, token, rssd, period, use_cache=True):
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{rssd}_{period.replace('/', '-')}.sdf"
    if use_cache and path.exists() and path.stat().st_size > 1000:
        return path.read_text(errors="replace")
    cmd = [
        "curl", "-s", "--fail-with-body", "-H", f"UserID: {user}",
        "-H", f"Authentication: Bearer {token}",      # trap 1: NOT "Authorization"
        "-H", "Content-Type: application/json",
        "-H", "dataSeries: Call",                     # trap 2: header, not query param
        "-H", f"reportingPeriodEndDate: {period}",
        "-H", "fiIDType: ID_RSSD", "-H", f"fiID: {rssd}",
        "-H", "facsimileFormat: SDF",
        f"{BASE}/RetrieveFacsimile",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    body = r.stdout
    if r.returncode != 0 or len(body) < 1000 or body.lstrip().startswith("{"):
        return None
    try:                                              # trap 4: base64 inside JSON
        text = base64.b64decode(json.loads(body)).decode("utf-8", errors="replace")
    except Exception:
        return None
    if "MDRM" not in text.splitlines()[0]:
        return None
    path.write_text(text)
    return text


def parse(sdf):
    """SDF header: Call Date;Bank RSSD;MDRM #;Value;Last Update;Short Def;Schedule;Line."""
    out = {}
    for line in sdf.splitlines():
        f = line.split(";")
        if len(f) < 4:
            continue
        mdrm, val = f[2].strip(), f[3].strip()
        if not mdrm or not val:
            continue
        try:
            out[mdrm] = int(float(val))
        except ValueError:
            continue
    return out


def pick(d, codes, prefixes=PREFIXES):
    """Return (value, mdrm_used). Sums multi-code chains; None if ANY part absent.
    NEVER coerces a missing part to 0 — zero != unknown (audit convention 2026-08-12)."""
    for p in prefixes:
        keys = [p + c for c in codes]
        if all(k in d for k in keys):
            return sum(d[k] for k in keys), "+".join(keys)
    return None, ""


# ---------------------------------------------------------------- guards

def load_prior():
    """Prior COMMITTED vintage from git HEAD (not the working tree — the working
    tree may be this run's own half-written output)."""
    rel = OUT_TSV.relative_to(ROOT).as_posix()
    r = subprocess.run(["git", "-C", str(ROOT), "show", f"HEAD:{rel}"],
                       capture_output=True, text=True)
    if r.returncode != 0 or not r.stdout.strip():
        return {}
    rows = csv.DictReader(decomment(r.stdout.splitlines()), delimiter="\t")
    return {(x["ticker"], x["quarter"]): x for x in rows}


def repro_guard(rows, prior, accept_reason):
    """★ THE 37.6% CLASS GUARD. Cross-check every overlapping bank-quarter against
    the prior committed vintage. A published cell that silently stops reproducing
    is exactly the defect that poisoned the legacy OZK figure for months and was
    only caught by archaeology. Restatements are REAL (FFIEC amended filings) —
    so they are allowed, but only when DECLARED via --accept-restatement."""
    fails = []
    for r in rows:
        key = (r["ticker"], r["quarter"])
        p = prior.get(key)
        if not p:
            r["repro_vs_prior"] = "NEW"
            continue
        if p.get("status") not in SCORED_STATUSES or r["status"] not in SCORED_STATUSES:
            r["repro_vs_prior"] = "NOT-COMPARABLE"
            continue
        diffs = []
        if str(p.get("mi3_k", "")) != str(r.get("mi3_k", "")):
            diffs.append(f"mi3_k {p.get('mi3_k')} -> {r.get('mi3_k')}")
        for col in ("v1_pct", "v1a_pct"):
            a, b = p.get(col, ""), r.get(col, "")
            if a in ("", None) or b in ("", None):
                if (a in ("", None)) != (b in ("", None)):
                    diffs.append(f"{col} {a!r} -> {b!r}")
                continue
            if abs(float(a) - float(b)) > REPRO_TOL_PCT:
                diffs.append(f"{col} {a} -> {b}")
        if diffs:
            r["repro_vs_prior"] = "RESTATED: " + "; ".join(diffs)
            fails.append((key, diffs))
        else:
            r["repro_vs_prior"] = "REPRODUCES"
    if fails and not accept_reason:
        msg = ["REPRODUCTION GUARD TRIPPED — %d previously published cell(s) no longer "
               "reproduce. NOTHING WRITTEN." % len(fails)]
        for (t, q), d in fails:
            msg.append(f"    {t} {q}: " + "; ".join(d))
        msg.append("  A cell that stops reproducing is EITHER an amended FFIEC filing")
        msg.append("  OR the single-cell data defect that killed the legacy 37.6% figure.")
        msg.append("  Establish WHICH at the primary, then re-run with:")
        msg.append('    --accept-restatement "<why, with the source that proves it>"')
        raise GuardTripped("\n".join(msg))
    if fails:
        print(f"  !! {len(fails)} restated cell(s) ACCEPTED: {accept_reason}", file=sys.stderr)
    return fails


def schema_guard(rows):
    """Fail loud rather than emit a blank that reads as zero. Every cell is either
    a number with a status that licenses it, or an explicit unscored status."""
    problems = []
    for r in rows:
        tag = f"{r.get('ticker')} {r.get('quarter')}"
        st = r.get("status")
        if st not in STATUS_VOCAB:
            problems.append(f"{tag}: status {st!r} outside vocabulary {sorted(STATUS_VOCAB)}")
            continue
        if r.get("mi3_zero_class") not in ZERO_VOCAB:
            problems.append(f"{tag}: mi3_zero_class {r.get('mi3_zero_class')!r} outside vocabulary")
        if st in SCORED_STATUSES:
            for c in REQUIRED_ON_SCORED:
                if r.get(c) in (None, ""):
                    problems.append(f"{tag}: status={st} but {c} is empty "
                                    f"(a blank here would read as zero)")
            if st == "OK" and r.get("v1a_pct") in (None, ""):
                problems.append(f"{tag}: status=OK but v1a_pct empty "
                                f"(use OK-V1-ONLY when item 9 is genuinely unreported)")
            if st == "OK-V1-ONLY" and r.get("v1a_pct") not in (None, ""):
                problems.append(f"{tag}: status=OK-V1-ONLY but v1a_pct is populated")
        else:
            for c in ("mi3_k", "v1_pct", "v1a_pct"):
                if r.get(c) not in (None, ""):
                    problems.append(f"{tag}: unscored status {st} must carry no {c}")
    if problems:
        raise GuardTripped("SCHEMA/STATE GUARD TRIPPED — NOTHING WRITTEN.\n    " +
                           "\n    ".join(problems))


def coverage_guard(rows):
    expected = len(COHORT) * len(QUARTERS)
    if len(rows) != expected:
        raise GuardTripped(f"COVERAGE GUARD TRIPPED — {len(rows)} rows, expected {expected}. "
                           "NOTHING WRITTEN.")
    unscored = [r for r in rows if r["status"] in UNSCORED_STATUSES]
    if unscored:
        # Not fatal — a bank genuinely may not report — but it must be LOUD and counted,
        # never a silent gap that a reader mistakes for a clean cell.
        print(f"  !! {len(unscored)} unscored bank-quarter(s) — each carries an explicit "
              f"status, none are blank:", file=sys.stderr)
        for r in unscored:
            print(f"       {r['ticker']} {r['quarter']} {r['status']}", file=sys.stderr)


# ---------------------------------------------------------------- output

def write_summary(rows, latest, fails, accept_reason):
    """★ Dual-basis + ABSOLUTE DOLLARS + YoY, generated BY CONSTRUCTION.
    The up-cap migration must be visible in default output, never something an
    analyst has to think to compute."""
    scored = [r for r in rows if r["quarter"] == latest and r["status"] in SCORED_STATUSES]
    by_v1 = sorted(scored, key=lambda r: -(r["v1_pct"] or 0))
    by_v1a = sorted([r for r in scored if r.get("v1a_pct") is not None],
                    key=lambda r: -r["v1a_pct"])
    by_dollars = sorted(scored, key=lambda r: -(r["mi3_k"] or 0))
    L = []
    L.append("# MI3 COHORT SCREEN — GENERATED SUMMARY")
    L.append("")
    L.append(f"**Generated by `scripts/mi3_cohort_screen.py` from `MI3_COHORT.tsv`. "
             f"Do not hand-edit — re-run the script.** Latest quarter: **{latest}** · "
             f"cohort {len(COHORT)} banks × {len(QUARTERS)} quarters = {len(rows)} bank-quarters, "
             f"{len(scored)} scored at {latest}.")
    L.append("")
    L.append("> ## ⚠️ BASIS-NAMING RULE — binding on every claim off this file")
    L.append("> **No cross-bank statement without its basis named.** `v1` (÷ item 4) is the "
             "LEGACY basis and is **not cross-bank comparable** — the item-9 share of the base "
             "varies bank to bank, and the two bases rank the cohort differently. "
             "**`v1a` (÷ item 4 + item 9) governs every cross-bank claim; `v1` exists only for "
             "continuity against v1-vintage records.**")
    L.append("> **And never quote a ratio without its dollars.** A ratio screen cannot see a book "
             "migrating up-cap to a large-denominator bank.")
    L.append("> ⚠️ **V1a ≠ V1:** MI3 is CRE *not secured* by real estate. Secured office books are "
             "a different object and are untouched by anything in this file.")
    L.append("")
    L.append(f"## Ranked THREE ways — {latest}")
    L.append("")
    L.append("| by **v1** (legacy) | | by **v1a** (uniform, cross-bank) | | by **MI3 $ level** |  | YoY $ |")
    L.append("|---|---:|---|---:|---|---:|---:|")
    for i in range(len(by_v1)):
        a = by_v1[i]
        b = by_v1a[i] if i < len(by_v1a) else None
        c = by_dollars[i]
        yoy = c.get("mi3_yoy_pct")
        if yoy in (None, ""):
            yoy_s = "UNKNOWN"
        elif isinstance(yoy, str):
            yoy_s = yoy                    # N-A-ZERO-BASE
        else:
            yoy_s = "{:+.1f}%".format(yoy)  # 1dp: displaying .0f double-rounds
        b_tic = b["ticker"] if b else "—"
        b_val = "{:.2f}".format(b["v1a_pct"]) if b else "—"
        dollars = "${:,.0f}M".format((c["mi3_k"] or 0) / 1000)
        L.append("| {} | {:.2f} | {} | {} | {} | {} | {} |".format(
            a["ticker"], a["v1_pct"], b_tic, b_val, c["ticker"], dollars, yoy_s))
    L.append("")
    rank_v1 = [r["ticker"] for r in by_v1]
    rank_v1a = [r["ticker"] for r in by_v1a]
    if rank_v1[:1] != rank_v1a[:1]:
        L.append(f"⚠️ **THE BASES DISAGREE ON THE TOP NAME — v1 says {rank_v1[0]}, "
                 f"v1a says {rank_v1a[0]}. The disagreement IS the finding**; do not pick "
                 f"the lens that flatters the thesis.")
        L.append("")
    if by_dollars and by_v1 and by_dollars[0]["ticker"] != by_v1[0]["ticker"]:
        L.append(f"⚠️ **THE LARGEST ABSOLUTE MI3 BOOK IS {by_dollars[0]['ticker']} "
                 f"(${by_dollars[0]['mi3_k']/1000:,.0f}M), which ranks "
                 f"#{rank_v1.index(by_dollars[0]['ticker'])+1} of {len(rank_v1)} by ratio.** "
                 f"A ratio screen structurally cannot see this. "
                 f"Cohort-selection open question → `registry/NOTES.md`.")
        L.append("")
    L.append("## Reproduction guard vs the prior committed vintage")
    if fails:
        L.append(f"⚠️ **{len(fails)} cell(s) RESTATED and explicitly accepted:** {accept_reason}")
        for (t, q), d in fails:
            L.append(f"- `{t} {q}` — " + "; ".join(d))
    else:
        n = sum(1 for r in rows if r.get("repro_vs_prior") == "REPRODUCES")
        L.append(f"✅ **{n} overlapping bank-quarter(s) reproduce** against the prior committed "
                 f"vintage; 0 unexplained restatements. Per-row verdict → `repro_vs_prior`.")
    L.append("")
    L.append("## Unscored cells (zero ≠ unknown ≠ not-applicable)")
    zeros = [r for r in rows if r.get("mi3_zero_class") == "REPORTED-ZERO"]
    unsc = [r for r in rows if r["status"] in UNSCORED_STATUSES]
    L.append(f"- **REPORTED-ZERO** (the bank filed a 0 — this is DATA): {len(zeros)} cell(s)"
             + (" — " + ", ".join(sorted({r['ticker'] for r in zeros})) if zeros else ""))
    L.append(f"- **UNSCORED** (no number exists; never rendered as 0): {len(unsc)} cell(s)"
             + (" — " + ", ".join(f"{r['ticker']} {r['quarter']} {r['status']}" for r in unsc)
                if unsc else ""))
    L.append("")
    L.append("*Full per-bank-quarter series, MDRM chains and both denominators → "
             "`MI3_COHORT.tsv`. Method, cohort rationale, traps and cadence → the script header "
             "and `registry/NOTES.md`.*")
    tmp = OUT_MD.with_suffix(".tmp")
    tmp.write_text("\n".join(L) + "\n")
    os.replace(tmp, OUT_MD)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--accept-restatement", default="",
                    help="Declare WHY a previously published cell changed, with its source.")
    args = ap.parse_args()

    user, token = creds()
    rows = []
    for tic, rssd, name, why in COHORT:
        for q in QUARTERS:
            sdf = facsimile(user, token, rssd, q, use_cache=not args.no_cache)
            rec = dict(ticker=tic, rssd=rssd, name=name, cohort_reason=why, quarter=q,
                       mi3_zero_class="UNKNOWN")
            if sdf is None:
                rec["status"] = "PULL-FAILED"
                rows.append(rec)
                print(f"  !! {tic} {q}: pull failed", file=sys.stderr)
                continue
            d = parse(sdf)
            num, num_src = pick(d, NUM_CODES)
            i4, i4_src = pick(d, I4_TOTAL)
            if i4 is None:
                i4, i4_src = pick(d, I4_PARTS)
            i9a, i9a_src = pick(d, I9A_CODES)
            i9b, i9b_src = pick(d, I9B_TOTAL)
            if i9b is None:
                i9b, i9b_src = pick(d, I9B_PARTS)
            i9 = None if (i9a is None or i9b is None) else i9a + i9b
            total, _ = pick(d, TOTAL_CODES)
            assets, _ = pick(d, ASSET_CODES)
            rec.update(mi3_k=num, item4_k=i4, item9a_k=i9a, item9b_k=i9b, item9_k=i9,
                       total_loans_k=total, total_assets_k=assets, num_mdrm=num_src,
                       denom_v1_mdrm=i4_src,
                       denom_v1a_mdrm=("|".join(x for x in (i4_src, i9a_src, i9b_src) if x)
                                       if i9 is not None else ""))
            rec["mi3_zero_class"] = ("UNKNOWN" if num is None else
                                     "REPORTED-ZERO" if num == 0 else "NONZERO")
            if num is None:
                rec["status"] = "NOT-REPORTED"
            elif i4 is None:
                rec["status"] = "DENOM-MISSING"
            else:
                rec["status"] = "OK" if i9 is not None else "OK-V1-ONLY"
                rec["v1_pct"] = round(100.0 * num / i4, 2) if i4 else None
                if i9 is not None and (i4 + i9):
                    rec["v1a_pct"] = round(100.0 * num / (i4 + i9), 2)
                    rec["item9_share_of_base_pct"] = round(100.0 * i9 / (i4 + i9), 1)
            rows.append(rec)

    # ★ QoQ + step detector — computed on the CONTIGUOUS grid, which is the whole point
    # of making it contiguous. A gapped grid cannot compute a QoQ at all.
    idx = {(r["ticker"], r["quarter"]): r for r in rows}
    qpos = {q: i for i, q in enumerate(QUARTERS)}
    for r in rows:
        i = qpos[r["quarter"]]
        if i == 0:
            continue
        prev = idx.get((r["ticker"], QUARTERS[i - 1]))
        if not prev:
            continue
        if isinstance(r.get("mi3_k"), int) and isinstance(prev.get("mi3_k"), int):
            if prev["mi3_k"] == 0:
                r["mi3_qoq_pct"] = "N-A-ZERO-BASE"
            else:
                r["mi3_qoq_pct"] = round(100.0 * (r["mi3_k"] / prev["mi3_k"] - 1), 1)
        if isinstance(r.get("total_loans_k"), int) and isinstance(prev.get("total_loans_k"), int) \
                and prev["total_loans_k"]:
            r["loans_qoq_pct"] = round(
                100.0 * (r["total_loans_k"] / prev["total_loans_k"] - 1), 1)
        m, l = r.get("mi3_qoq_pct"), r.get("loans_qoq_pct")
        if isinstance(m, float) and isinstance(l, float):
            r["step_flag"] = ("STEP-CANDIDATE" if abs(m) > STEP_MI3_PCT
                              and abs(l) < STEP_LOANS_PCT else "")

    # YoY on the DOLLARS — first-class, computed here so no analyst has to remember.
    for r in rows:
        base_q = YOY_PAIRS.get(r["quarter"])
        prev = idx.get((r["ticker"], base_q)) if base_q else None
        if not (prev and isinstance(r.get("mi3_k"), int)
                and isinstance(prev.get("mi3_k"), int)):
            continue                      # leave empty: genuinely UNKNOWN
        if prev["mi3_k"] == 0:
            # zero != unknown != not-applicable. A YoY off a zero base is
            # UNDEFINED, which is a THIRD state -- not a missing number.
            r["mi3_yoy_pct"] = "N-A-ZERO-BASE"
            continue
        r["mi3_yoy_pct"] = round(100.0 * (r["mi3_k"] / prev["mi3_k"] - 1), 1)

    for r in rows:
        print(f"  {r['ticker']:5s} {r['quarter']:10s} {r['status']:13s} "
              f"{r['mi3_zero_class']:13s} MI3={r.get('mi3_k')} "
              f"v1={r.get('v1_pct')} v1a={r.get('v1a_pct')} yoy={r.get('mi3_yoy_pct')}",
              file=sys.stderr)

    try:
        coverage_guard(rows)
        schema_guard(rows)
        fails = repro_guard(rows, load_prior(), args.accept_restatement)
    except GuardTripped as e:
        print("\n⛔ " + str(e) + "\n", file=sys.stderr)
        return 2

    tmp = OUT_TSV.with_suffix(".tmp")
    today = datetime.date.today().isoformat()
    with open(tmp, "w", newline="") as fh:
        for line in header_lines(today):
            fh.write(line + "\n")
        w = csv.DictWriter(fh, fieldnames=COLS, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow(r)
    os.replace(tmp, OUT_TSV)
    write_summary(rows, QUARTERS[-1], fails, args.accept_restatement)
    print(f"wrote {OUT_TSV} ({len(rows)} rows) + {OUT_MD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
