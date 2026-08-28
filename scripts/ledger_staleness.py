#!/usr/bin/env python3
"""
ledger_staleness.py — boot-time workbook-ledger staleness alert.

Enforces the root CLAUDE.md "Data Hygiene" rule: a workbook TSV ledger must be
in ONE of two states, never the silent-rot middle —
  (a) FROZEN — first line is a banner beginning 'FROZEN' (declared dead; exempt), or
  (b) LIVE and within `--days` of the agent's STATUS.md.
This script reports any LIVE ledger that has fallen behind STATUS, so the gap is
surfaced at boot instead of rotting silently. (Audit 2026-06-27 found 8 agents
with the rule on the books but no mechanism enforcing it — this is the mechanism.)

Usage:
  python3 scripts/ledger_staleness.py REGINALD          # one agent by name
  python3 scripts/ledger_staleness.py AGENTS/REGINALD   # one agent by path
  python3 scripts/ledger_staleness.py --all             # every AGENTS/*/workbook
  python3 scripts/ledger_staleness.py REGINALD --days 21 # threshold (default 30)
        (docstring previously said "default 14" while argparse said 30 — BRENT copied
        the 14 into its boot doc and reasoned off half the real coverage window for
        4 days. Fixed 2026-08-21; the argparse default is the ONLY authority.)
  python3 scripts/ledger_staleness.py REGINALD --quiet   # print only when stale
  python3 scripts/ledger_staleness.py REGINALD --glob 'workbook/*.tsv'  # custom location

Staleness-cadence modes (Will-approved 2026-08-20 — design/2026-08-11_STALENESS_CADENCE_PROPOSAL.md;
all three ADDITIVE, default output byte-identical without the flags):
  python3 scripts/ledger_staleness.py <NAME> --nudge      # (b) closeout nudge: one advisory line
        if STATUS is moving this session while live ledgers sit >=1 STATUS-write behind.
        Thresholdless; rc 0 no-gap / 1 nudged / 2 cannot-certify. Root-canon closeout step.
        Output shape v2 (2026-08-20, OSPREY+HAWK day-one field report via PROME — both
        defects observed live at n=2 desks the day the nudge shipped):
        - ENUMERATES every behind-ledger, count first ("3 ledger(s) behind: VX.tsv (8w), ...").
          v1 named the worst + "+N more behind"; both desks fixed the NAMED ledger and nearly
          stopped while the unnamed remainder held the larger gap. The list is a work-list.
        - EVENT-DRIVEN declaration: a ledger whose data clock must not advance without a
          real print (OSPREY WARRISK class — per-voyage premia that reach print only on a
          step-change canvass) declares "Cadence: EVENT-DRIVEN" in its header comment block.
          The nudge then reports it under a distinct label with its re-pull clock ("Last
          re-pull ATTEMPTED: YYYY-MM-DD") instead of counting it behind — for that surface
          class writes-behind measures how busy the desk is, not how stale the ledger is,
          and a structurally always-red check trains skipping on every surface. The
          declaration affects --nudge ONLY: the --days/--writes/--abs-floor scans still
          grade the file (OSPREY's own disposition: "leave it flagging"). A declaration
          with NO parseable re-pull clock line is MISCONFIGURED (rc 2): absence-expected
          certifies nothing unless somebody provably looked.
  python3 scripts/ledger_staleness.py --all --writes      # (a) activity-denominated backstop:
        staleness in STATUS-commits-since-ledger-commit, flag at --writes-bar (default 12).
        Sprints can't hide a gap; idle agents don't false-flag. First fleet pass = CANDIDATES
        not defects (owners confirm real cadence) at Staleness Sweep #4 ~9/1.
  python3 scripts/ledger_staleness.py --all --abs-floor   # (c) absolute floor: flag any live
        ledger whose CONTENT vintage exceeds --abs-days (default 90) regardless of the relative
        delta — the PAT-092 counter (a stalled agent freezes the relative clock).

Per-agent glob declaration (2026-07-31, DAEDALUS TERRY-S1 fix, Will-approved):
an agent whose ledgers live outside workbook/*.tsv declares them in
AGENTS/<NAME>/workbook/LEDGER_GLOB — whitespace-separated globs relative to the
agent dir, '#' comments allowed (e.g. "*.tsv" + "daytrading/*.tsv"). Read in
both single-agent and --all modes; an explicit CLI --glob still wins. The file
doubles as the do-not-delete marker for a deliberately empty workbook/.
Fail-loud contract (PAT-074 — a PASS must say what it searched):
  🔴 MISCONFIGURED        — LEDGER_GLOB exists but matches 0 files (all modes)
  ⚠️ LEDGERS-OUTSIDE-GLOB — workbook/ exists, glob matched 0, but non-exempt
                            top-level TSVs exist (all modes, incl. --quiet).
                            TERRY sat in this state for weeks reading as clean.
  note: ... unenforced    — no workbook/, no LEDGER_GLOB, top-level TSVs exist
                            (non-quiet only; owner's call whether to opt in)
  perimeter [NAME]: ...   — the glob MATCHED, and TSVs still sit outside it
                            (all modes, incl. --quiet; advisory, does NOT set rc).
                            The three lines above only speak when the glob matches
                            ZERO files, so an agent whose glob matched fine while
                            load-bearing ledgers sat in SUBDIRECTORIES read as fully
                            clean. This states the pass's PERIMETER: "not scanned" is
                            a coverage fact, never a defect claim — whether a file
                            belongs under enforcement stays the owner's call.
                            Base-rated before wiring (2026-08-22, Will-approved):
                            20 of 33 agents hold >=1, most often thesis/PREDICTIONS.tsv
                            (7) and docket/CATALYSTS.tsv (10). Silent on the other 13.
                            Skips archive/_archive/inbox/outbox/processed/sources/tests
                            by declared choice (UNSCANNED_SKIP_DIRS) — a live ledger
                            landing in one of those is invisible here BY THAT CHOICE.
board_log.tsv is excluded from the outside-glob signature — it is the fleet-wide
WALTER-consumption log, not a workbook ledger (would false-fire on ~15 agents).

Timestamps use each file's last git-commit time (falls back to filesystem mtime
for uncommitted files).

Exit-code contract (REVISED 2026-08-17 — DAEDALUS, PROME-approved, riding
CHECK_STANDARD §8 rule 3; supersedes the founding "always 0, alert not gate"
line, which left every rc-keyed consumer reading ✅ OK over stale findings —
the silent-fallback-green class, BRENT-verified 8/17):
  0 — clean: everything scanned, nothing stale, no enforcement warnings
  1 — FINDINGS: stale ledger(s) found (workbook or --trade mode)
  2 — CANNOT-CERTIFY: MISCONFIGURED LEDGER_GLOB / LEDGERS-OUTSIDE-GLOB /
      agent-not-found / usage error. 2 dominates 1 when both occur (--all).
Markers remain the primary wrapper contract per §8 rule 5 (⚠️/🔴 lines);
rc now agrees with them instead of contradicting them. Consumers updated in
the same batch: WATT/VULCAN/MIDAS/FERT run_alert, OTTO, MARCO, BRENT boots.

⚠️ KNOWN LIMIT (2026-07-28, VIOLET KB-VIO-142): this check compares AGES, so it
PASSES a file that is brand new and affirmatively false (TRADE.md read 'ACTIVE
POSITIONS: None.' for 17h with $287.70 live; this script said 'ok +2d'). The
AGREEMENT test lives in scripts/position_agreement_check.py — run both.

Boot wiring (drop into an agent's boot sequence):
    .venv/bin/python3 scripts/ledger_staleness.py <NAME> --quiet
and surface the one-line summary; decide freeze-vs-refresh at closeout.
"""
import argparse
import datetime
import glob
import json
import os
import re
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# PAT-044 two-clock header: "Last real data refresh: YYYY-MM-DD" in the header block.
# The portable staleness signal — survives clone-flattened git history (cloud sessions)
# and hygiene-edit git-time resets (banner/tag passes), both of which make time-based
# grading go false-clean on genuinely stale data (PAT-039, 2 observed instances).
CONTENT_DATE_RE = re.compile(r"last\s+real\s+data\s+refresh[:\s]+(\d{4}-\d{2}-\d{2})", re.IGNORECASE)

# By-name non-live files: definitions/archives/backups/snapshots are SUPPOSED to
# be static, so staleness is meaningless for them. Exempt from the alert (shown as
# 'ref') unless --strict. Matched case-insensitively as substrings of the basename.
EXEMPT_SUBSTR = ["schema", "archive", "_old_", "backup", "_bak", "history", ".template", "template"]


def is_exempt(path):
    base = os.path.basename(path).lower()
    return any(s in base for s in EXEMPT_SUBSTR)


def git_time(path):
    """Last commit unix time for path, or None if not committed/error."""
    try:
        out = subprocess.run(
            ["git", "-C", REPO, "log", "-1", "--format=%ct", "--", path],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        return int(out) if out else None
    except Exception:
        return None


def content_time(path):
    """Two-clock header date (first ~8 lines), or None. Preferred over git time when
    present: the DATA clock can't be laundered by a hygiene edit or a flattened clone."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            head = "".join(f.readline() for _ in range(8))
        m = CONTENT_DATE_RE.search(head)
        if m:
            return int(datetime.datetime.strptime(m.group(1), "%Y-%m-%d").timestamp())
    except (OSError, ValueError):
        pass
    return None


def git_last_commit(path):
    """Last commit hash for path, or None."""
    try:
        out = subprocess.run(
            ["git", "-C", REPO, "log", "-1", "--format=%H", "--", path],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        return out or None
    except Exception:
        return None


def status_writes_since(agent_dir, ledger):
    """STATUS-commits-since-ledger-commit — the activity-denominated staleness unit
    (staleness-cadence proposal (a), Will-approved 2026-08-20). None if the ledger
    has never been committed (cannot anchor the count)."""
    anchor = git_last_commit(ledger)
    if anchor is None:
        return None
    status = os.path.join(agent_dir, "STATUS.md")
    try:
        out = subprocess.run(
            ["git", "-C", REPO, "log", "--oneline", f"{anchor}..HEAD", "--", status],
            capture_output=True, text=True, timeout=10,
        ).stdout
        return len([l for l in out.splitlines() if l.strip()])
    except Exception:
        return None


def status_moved_this_session(agent_dir):
    """True if STATUS.md is dirty in the working tree OR its last commit is today —
    the (b)-nudge's 'STATUS moving' condition (fires where the gap is created)."""
    status = os.path.join(agent_dir, "STATUS.md")
    try:
        dirty = subprocess.run(
            ["git", "-C", REPO, "status", "--porcelain", "--", status],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        if dirty:
            return True
    except Exception:
        pass
    t = git_time(status)
    if t is None:
        return False
    return datetime.date.fromtimestamp(t) == datetime.date.today()


def file_time(path):
    """Prefer the in-content two-clock date (PAT-044/PAT-039); then git-commit time
    (clone/checkout-stable); then fs mtime. Files without the header behave exactly
    as before this change (2026-07-22)."""
    t = content_time(path)
    if t is not None:
        return t
    t = git_time(path)
    if t is not None:
        return t
    try:
        return int(os.path.getmtime(path))
    except OSError:
        return None


# Header banners that declare a surface intentionally static (dead/retired).
# Broadened 2026-07-04 (DAEDALUS TRADE-staleness sweep, PAT-025) beyond the literal
# "FROZEN" to the fleet's real dead-banner vocabulary — CARL "⛔ RETIRED" (line 1),
# MARCO "⚠️ FEB-VINTAGE … NOT CURRENT" (line 3) — scanning the header block so an
# intentional dead-banner is never a false-flag. Kept to strong, unambiguous phrases
# (not bare "stale"/"vintage") to avoid exempting a genuinely-rotten file.
STATIC_BANNER_MARKERS = ["FROZEN", "RETIRED", "NOT CURRENT", "DO NOT CITE", "NOT MAINTAINED", "ARCHIVED", "SUPERSEDED"]
# SUPERSEDED added 2026-07-31 (DAEDALUS state-vocabulary registry build, PAT-075):
# the #2 banner token fleet-wide (52 banner-position files) was absent here — latent,
# not live (instances sat on .md docs outside these globs), closed with the TERRY-S1
# fix. Canonical semantics per BLUEPRINTS/STATE_VOCABULARY.md: SUPERSEDED = replaced
# by a NAMED successor; banner-form guards below (col-cap, glue, negation) apply.

# Recognizer hardening 2026-07-22 (DAEDALUS AEOLUS+LABOR QCs, Will-approved —
# PAT-035/PAT-059: a dead-banner is a FORM, not a keyword). Ground truth from a
# fleet-wide header survey of every marker hit (34 files): every GENUINE banner
# front-loads its marker at column ≤31 of its line ("# FROZEN 2026-07-01 — …",
# "⛔ RETIRED", "⚠️ FEB-VINTAGE … NOT CURRENT" col 31); every FALSE positive sits
# at column 63+ — prose mentions ("Position frozen: 13 shares" col 2747, SAM),
# revival-history notes ("GAP: frozen 6/26→7/10" col 281, LABOR KB), successor
# pointers ("full ledger frozen at AGENTS/HAWK/…" col 120+, FALCON×3/OSPREY×2),
# partial-row warnings (REGINALD VX col 278), and data-row text (CRUISE/CARL).
# Guards, in order:
#  1. "Status: LIVE" declaration anywhere in the header overrides all markers
#     (AEOLUS TRADE.md rule-citation case).
#  2. Marker must start within MARKER_COL_CAP chars of its own line — banners
#     front-load; prose buries. (Survey: genuine max col 31; false min col 63.)
#  3. FROZEN preceded by "NOT " doesn't count (HAWK KB "…continues under HAWK
#     (not frozen)" — a LIVE declaration, col 63).
#  4. Markers glued by hyphen OR slash don't count ("refresh-or-FROZEN",
#     "FROZEN-PENDING", "a FROZEN/NOT-CURRENT banner" — VULCAN/WATT §8 citation).
#  4b. NARROWED 2026-08-11 (staleness sweep #3, CARL/PHAN reader finding): a
#     LINE-INITIAL marker with a hyphen-SUFFIXED qualifier IS a banner —
#     "# FROZEN-VINTAGE 2026-07-10 — carried into DOSSIER.md" (3 PHAN ledgers
#     false-flagged +31d). Guard #4 was aimed at markers glued as the SECOND
#     token of a compound; a front-loaded FROZEN-<qualifier> is the opposite
#     shape. Mid-line glued forms (prose-cited FROZEN-PENDING, refresh-or-FROZEN)
#     still rejected: the allowance requires the marker to be the line's first
#     word after comment/emphasis chars.
# NOTE: no line-leading-LIVE override — tried and REVERTED same-day: it wrongly
# un-froze BRENT FLOW/VX via their "# LIVE HOMES/# LIVE SUCCESSOR" pointer lines.
# Validated 2026-07-22: fleet diff = false-FROZENs flip to tracked (list in
# AGENTS/DAEDALUS/upgrades/LABOR_QC_2026-07-22.md); zero genuine banners lost.
LIVE_DECL_RE = re.compile(r"STATUS\s*:?\s*\**\s*LIVE\b", re.IGNORECASE)
MARKER_COL_CAP = 100
MARKER_RES = [
    re.compile(r"(?<!NOT )(?<![\w/-])" + re.escape(k) + r"(?![\w/-])") if k == "FROZEN"
    else re.compile(r"(?<![\w/-])" + re.escape(k) + r"(?![\w/-])")
    for k in STATIC_BANNER_MARKERS
]

# Recognizer hardening 2026-08-07 (TERRY isolation-tested reproduction, 2026-08-04
# packet — 7 ledgers fleet-wide silently exempted by NON-banner text, incl. BROCK
# VX_HISTORY at +140d invisible because a DATA ROW said "permanently frozen").
# Unifying mechanism TERRY proved: for a TSV whose line 1 is a column header, any
# status word in the first few DATA rows exempted the whole ledger. Three new
# banner-FORM rules (a banner is a FORM, not a keyword — PAT-059 extended):
#  5. BANNER REGION ENDS AT THE DATA BOUNDARY — scanning stops at the first
#     non-comment line containing a tab (the column-header or first data row).
#     A bare-column-header file has an EMPTY banner region (BROCK/CARL-PHAN/
#     LABOR/SAM class). Genuine banners front-load ABOVE the data by convention
#     (survey 7/22: all 46 genuine banners sit on line 1).
#  6. A MARKER AFTER A TAB IS A CELL VALUE, NOT A BANNER — each scanned line is
#     truncated at its first tab before marker search (kills commented-out data
#     rows and Status/notes cells: HAWK 🪦 RETIRED rows, LABOR SUPERSEDED note
#     cell). Also: a marker immediately followed by "ROWS"/"ENTRIES" is a
#     row-retention POLICY sentence, not a file banner (TERRY line-5 class:
#     "# RETIRED rows are kept, never deleted").
#  7. A LINE-1 LIVE DECLARATION DOMINATES LATER MARKERS (TERRY rule c) — if
#     line 1 declares the file live ("... LIVE (not frozen)", "⚠️ LIVE-BUT-NOT-
#     BOOT-READ ...", "NOT FROZEN"), no later line can exempt it. Guards that
#     keep the 7/22 revert case reverted: a LIVE token in a POINTER PHRASE
#     ("LIVE SUCCESSOR/HOME(S)/CANONICAL" — BRENT FLOW/VX pointer lines, HAWK
#     split-note) does NOT count as a self-declaration; and a valid un-negated
#     banner marker ON LINE 1 ITSELF beats a live token on the same line
#     ("# SUPERSEDED — live at <path>" stays exempt).
# Validated 2026-08-07: TERRY's 5-line isolation matrix re-run against the fix +
# full-fleet before/after diff (workbook + trade modes) — exactly the 7 wrongly-
# exempt ledgers flip to tracked, zero genuine banners lost.
ROW_POLICY_RE = re.compile(r"(?:RETIRED|FROZEN|SUPERSEDED|ARCHIVED)\s+(?:ROWS?|ENTRIES)\b")
LINE1_LIVE_RE = re.compile(r"NOT\s+FROZEN\b|(?<![\w/-])LIVE\b(?!\s+(?:SUCCESSORS?|HOMES?|CANONICAL))")

# EVENT-DRIVEN cadence declaration (2026-08-20, nudge output-shape v2 — see --nudge
# docstring). A FORM, not a keyword (PAT-059): requires the "Cadence:" prefix and a
# column cap, because the bare words "event-driven" appear mid-line in header PROSE
# on the very file that motivated this (OSPREY WARRISK caveat lines) — a bare-token
# match would have self-declared it before the owner chose to. Scanned over the
# header comment block only (stops at the data boundary, same as the banner region).
CADENCE_EVENT_RE = re.compile(r"cadence\s*:\s*event-driven", re.IGNORECASE)
# Re-pull clock — the two-clock header's second clock ("nobody looked" vs "nothing
# published"). The check that fits an event-driven surface is THIS clock, not the
# data clock (OSPREY 8/20 memo).
REPULL_RE = re.compile(r"last\s+re-?pull\s+attempted[:\s]+(\d{4}-\d{2}-\d{2})", re.IGNORECASE)
HEADER_SCAN_LINES = 40  # event-driven headers run long (WARRISK ~15 comment lines)

# ---------------------------------------------------------------------------
# "CORRECTLY QUIET" DECLARATIONS + KERNEL BYTE-PINS (2026-08-28, DAEDALUS 8/28 wiring
# sweep, register leg ② + PROME item 8/27g). One law, four surfaces (STATE_VOCABULARY
# Class 11 exemption law): a guard family that cannot express "correctly quiet" trains
# its reader to ignore it. Before this edit the nudge could say EVENT-DRIVEN and nothing
# else, so three legitimately-quiet shapes all read as "behind" every closeout:
#   - AEOLUS seismic/ (a folder the CHARTER exempts) -- answered in commit messages,
#   - CREED CREED_T_FIRED_LOG.tsv (an append-only EVENT ledger with one fire) -- "8 behind",
#   - MIDAS PREDICTIONS.tsv (a row byte-PINNED by a Kernel submission) -- "18 behind",
#     where the nudge's remedy ("refresh") is FORBIDDEN on the pinned row.
# Same FORM rule as EVENT-DRIVEN (PAT-059): `Cadence:`-prefixed, front-loaded, header
# block only. Bare prose ("scheduled for review", "exempt") never declares.
#   Cadence: SCHEDULED next_due=YYYY-MM-DD   -> quiet until next_due; counted behind after
#   Cadence: EXEMPT-BY-CHARTER -- <charter clause>  -> never counted; a bare token with no
#                                                    clause is MISCONFIGURED (rc 2)
# Kernel pins are not a declaration -- they are READ from the submissions/events
# (native_refs[].path + locator), so the nudge names the pinned rows beside a behind
# ledger and the remedy becomes "refresh only UNPINNED rows". No new state file (Will's
# no-second-store constraint); the pin set is the Kernel's own record.
# A2 rule (WALTER 8/26, bought live): an unparseable next_due is rc 2, never a row-skip.
CADENCE_SCHED_RE = re.compile(r"cadence\s*:\s*scheduled\b", re.IGNORECASE)
NEXT_DUE_RE = re.compile(r"next_due\s*[=:]\s*(\S+)", re.IGNORECASE)
CADENCE_EXEMPT_RE = re.compile(r"cadence\s*:\s*exempt-by-charter\b(.*)$", re.IGNORECASE)
KERNEL_PIN_GLOBS = ["AGENTS/*/outbox/kernel/submissions/*.json",
                    "KERNEL/shadow/events/*/*/*.json"]
_PIN_CACHE = None


def scheduled_next_due(path):
    """None if no `Cadence: SCHEDULED` declaration; ('ok', date) if next_due parses
    (strict YYYY-MM-DD); ('unparseable', raw) otherwise -- rc 2 at the caller."""
    for line in _header_block(path):
        m = CADENCE_SCHED_RE.search(line)
        if m and m.start() < MARKER_COL_CAP:
            d = NEXT_DUE_RE.search(line)
            raw = d.group(1).strip().rstrip(".,;") if d else "<none>"
            mm = re.fullmatch(r"(\d{4})-(\d{2})-(\d{2})", raw)
            if not mm:
                return ("unparseable", raw)
            try:
                return ("ok", datetime.date(int(mm.group(1)), int(mm.group(2)), int(mm.group(3))))
            except ValueError:
                return ("unparseable", raw)
    return None


def exempt_by_charter(path):
    """None if no `Cadence: EXEMPT-BY-CHARTER` declaration; ('ok', clause) when a charter
    clause follows the token; ('missing-reason', None) on a bare token."""
    for line in _header_block(path):
        m = CADENCE_EXEMPT_RE.search(line)
        if m and m.start() < MARKER_COL_CAP:
            clause = re.sub(r"^[\s\-\u2014\u2013:]+", "", m.group(1)).strip()
            return ("ok", clause) if len(clause) >= 8 else ("missing-reason", None)
    return None


def kernel_pins():
    """repo-relative path -> set of locators pinned by Kernel submissions/accepted events.
    Read-only; cached per process. Unparseable JSON is recorded under '__unparseable__'
    and reported, never swallowed (PAT-106)."""
    global _PIN_CACHE
    if _PIN_CACHE is not None:
        return _PIN_CACHE
    pins = {}
    for gp in KERNEL_PIN_GLOBS:
        for f in glob.glob(os.path.join(REPO, gp)):
            try:
                with open(f, encoding="utf-8") as fh:
                    d = json.load(fh)
            except (OSError, ValueError):
                pins.setdefault("__unparseable__", set()).add(os.path.relpath(f, REPO))
                continue
            for r in d.get("native_refs") or []:
                pth = r.get("path")
                if pth:
                    pins.setdefault(pth, set()).add(str(r.get("locator") or "?"))
    _PIN_CACHE = pins
    return pins


def _header_block(path):
    """Header comment lines up to the data boundary (first non-comment line with a
    tab), max HEADER_SCAN_LINES. The region both cadence declarations and re-pull
    clocks must live in."""
    out = []
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            for _ in range(HEADER_SCAN_LINES):
                line = f.readline()
                if not line:
                    break
                if "\t" in line and not line.lstrip().startswith("#"):
                    break
                out.append(line)
    except OSError:
        pass
    return out


def is_event_driven(path):
    """True if the header block declares 'Cadence: EVENT-DRIVEN' (match must start
    within MARKER_COL_CAP of its line — front-loaded declarations only)."""
    for line in _header_block(path):
        m = CADENCE_EVENT_RE.search(line)
        if m and m.start() < MARKER_COL_CAP:
            return True
    return False


def repull_date(path):
    """The re-pull clock date string ('Last re-pull ATTEMPTED: YYYY-MM-DD'), or None."""
    for line in _header_block(path):
        m = REPULL_RE.search(line)
        if m:
            return m.group(1)
    return None


# Trade/position surfaces scanned under --trade (default glob stays workbook/*.tsv).
TRADE_GLOBS = ["TRADE.md", "trade/TRADE.md", "TRADE_BOOK.md", "POSITIONS.md"]

# Excluded from the LEDGERS-OUTSIDE-GLOB signature: shared-log conventions that are
# NOT workbook ledgers. board_log.tsv is the WALTER BOARD-consumption log carried by
# ~15 agents at top level by design — counting it would false-fire the warning fleet-wide.
NON_LEDGER_NAMES = {"board_log.tsv"}


def read_ledger_glob(agent_dir):
    """Parse AGENTS/<NAME>/workbook/LEDGER_GLOB. Returns a list of glob patterns,
    [] if the file exists but declares none (MISCONFIGURED), or None if absent."""
    p = os.path.join(agent_dir, "workbook", "LEDGER_GLOB")
    if not os.path.isfile(p):
        return None
    pats = []
    try:
        with open(p, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                line = line.split("#", 1)[0].strip()
                if line:
                    pats.extend(line.split())
    except OSError:
        return []
    return pats


def outside_glob_candidates(agent_dir):
    """Non-exempt, non-board-log top-level TSVs — the ledgers a 0-match glob is missing."""
    return sorted(
        p for p in glob.glob(os.path.join(agent_dir, "*.tsv"))
        if os.path.basename(p) not in NON_LEDGER_NAMES and not is_exempt(p)
    )


# Zones that hold no live ledger by fleet convention. DECLARED, not incidental: a
# coverage line that lists archived and inbox TSVs trains its reader to ignore it,
# which is the failure mode this line exists to avoid. tests/ holds this script's own
# fixtures. ⚠️ If a live ledger ever lands in one of these it is invisible here BY THIS
# CHOICE — written down so the next reader sees a decision rather than an oversight.
UNSCANNED_SKIP_DIRS = ("archive", "_archive", "inbox", "outbox", "processed", "sources", "tests")


def unscanned_outside_glob(agent_dir, matched):
    """TSVs under agent_dir that this pass did NOT scan.

    A COVERAGE statement, never a defect claim. "Not scanned" is a fact about this
    pass's perimeter; whether a file BELONGS under staleness enforcement is the
    owner's call and this function does not express an opinion on it.

    Why it exists (PAT-074 — audit a check by what its PASS proves): the pre-existing
    fail-loud contract above only speaks when the glob matches ZERO files. An agent
    whose glob matches fine, while load-bearing ledgers sit in SUBDIRECTORIES, got a
    clean report with nothing indicating anything went unexamined — so "all ledgers
    ok" read as "this desk's records are current" while certifying only the matched set.

    Measured fleet-wide 2026-08-22 before wiring (CHECK_STANDARD §12): 20 of 33 agents
    hold at least one unscanned TSV, most commonly thesis/PREDICTIONS.tsv (7 desks) and
    docket/CATALYSTS.tsv (10) — i.e. the prediction ledgers and dated-obligation
    registries, fleet-wide, outside every staleness instrument and silently so.
    Founding case: HOMER's boot ran this check, got rc=0 and eight green rows, and was
    structurally incapable of seeing the two files that held a live 9-day-old spec
    defect (DAEDALUS HOMER review, 2026-08-22; owner-confirmed at its own boot).
    """
    seen = {os.path.realpath(p) for p in matched}
    out = []
    for p in glob.glob(os.path.join(agent_dir, "**", "*.tsv"), recursive=True):
        rel = os.path.relpath(p, agent_dir)
        if any(d in UNSCANNED_SKIP_DIRS for d in rel.split(os.sep)[:-1]):
            continue
        if os.path.basename(p) in NON_LEDGER_NAMES or is_exempt(p):
            continue
        if os.path.realpath(p) in seen:
            continue
        out.append(rel)
    return sorted(out)


def report_unmatched(agent_dir, name, pats, decl, quiet):
    """Workbook mode, glob matched 0 files. Never a bare benign line when ledgers
    exist unscanned (TERRY-S1, PAT-074): distinguish MISCONFIGURED / OUTSIDE-GLOB /
    unenforced-advisory / genuinely-nothing. Returns 1 if a loud warning printed."""
    top = outside_glob_candidates(agent_dir)
    has_wb = os.path.isdir(os.path.join(agent_dir, "workbook"))
    if decl is not None:
        shown = " ".join(decl) if decl else "<empty file>"
        print(f"🔴 [{name}] LEDGER_GLOB matched 0 files (patterns: {shown}) — MISCONFIGURED; "
              f"enforcement is silently absent. Fix {os.path.join('AGENTS', name, 'workbook', 'LEDGER_GLOB')}.")
        return 1
    if has_wb and top:
        names = ", ".join(os.path.basename(p) for p in top)
        print(f"⚠️  [{name}] LEDGERS-OUTSIDE-GLOB: 0 ledgers matched {' '.join(pats)} but "
              f"{len(top)} TSV(s) sit outside it: {names} — UNENFORCED. Declare them in workbook/LEDGER_GLOB.")
        return 1
    if not quiet:
        if top:
            names = ", ".join(os.path.basename(p) for p in top)
            print(f"[{name}] note: {len(top)} top-level TSV(s) unenforced (no workbook/, no LEDGER_GLOB): {names}")
        else:
            print(f"[{name}] no ledgers matched {' '.join(pats)} (no non-exempt top-level TSVs outside it)")
    return 0


# Rule 4b (2026-08-11, sweep #3): a line-INITIAL single-word marker with a
# hyphen-SUFFIXED qualifier is a banner ("# FROZEN-VINTAGE 2026-07-10 — …"),
# not a glued mention. Only comment/emphasis/emoji chars may precede it — any
# preceding WORD ("refresh-or-FROZEN", prose-cited "… FROZEN-PENDING …") still
# fails, which is what guard #4 exists for.
LINE_INITIAL_QUALIFIED_RE = re.compile(
    r"^[^A-Z0-9]{0,12}(?:FROZEN|RETIRED|SUPERSEDED|ARCHIVED)-[A-Z]")


# KEY LINES ARE NEVER BANNERS (2026-08-28, OZK live footgun): a PAT-044 two-clock header
# "# Last real data refresh: … re-anchored to the frozen Option-2 window" carried the word
# 'frozen' in PROSE and the recognizer silently reclassified a LIVE ledger as FROZEN — every
# other check kept passing. Banner vocabulary is common in exactly the sentences that explain
# an irregular cadence. A line whose first token is a header KEY is a key/value line, not a
# declaration; markers on it are prose. Declarations start the line (after # and decoration).
KEY_LINE_RE = re.compile(r"^\s*#\s*(?:Last|Cadence|Status|Source|Owner|Schema|Note|Notes|Vintage|"
                         r"Re-?pull|Refresh|Provenance|Basis|Unit|Units)\b", re.IGNORECASE)


def _line_has_marker(u_line):
    """Un-negated, un-glued banner marker in the pre-tab portion of ONE uppercased
    line, within MARKER_COL_CAP, and not a row-retention policy sentence (rule 6).
    Rule 8 (2026-08-28): a header KEY line (Last …/Cadence …/Status …) never declares."""
    scan = u_line.split("\t", 1)[0]
    if KEY_LINE_RE.match(scan):
        return False
    if ROW_POLICY_RE.search(scan):
        return False
    if LINE_INITIAL_QUALIFIED_RE.match(scan):
        return True
    for rx in MARKER_RES:
        m = rx.search(scan)
        if m and m.start() < MARKER_COL_CAP:
            return True
    return False


def is_frozen(path):
    """True if the banner region declares the surface intentionally static.
    Named is_frozen for call-site compatibility; recognizes the whole dead-banner set.
    Banner-FORM rules (2026-07-22 hardening + 2026-08-07 TERRY hardening, see the
    MARKER_RES / ROW_POLICY_RE comments): "Status: LIVE" wins; a line-1 live
    declaration wins unless line 1 itself carries a marker; scanning stops at the
    data boundary; a marker after a tab is a cell value; negated/glued/row-policy
    mentions don't count; marker must start within MARKER_COL_CAP of its line."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            lines = [f.readline() for _ in range(6)]
        head = "".join(lines).upper()
        if LIVE_DECL_RE.search(head):
            return False
        u1 = lines[0].upper() if lines else ""
        # Rule 7: line-1 live declaration dominates later markers — unless line 1
        # itself carries a valid marker (same-line conflict → the marker wins).
        if LINE1_LIVE_RE.search(u1.split("\t", 1)[0]) and not _line_has_marker(u1):
            return False
        for line in lines:
            u = line.upper()
            # Rule 5: banner region ends at the first non-comment line containing
            # a tab (column-header row or first data row).
            if "\t" in u and not u.lstrip().startswith("#"):
                break
            if _line_has_marker(u):
                return True
        return False
    except OSError:
        return False


def resolve_agent_dir(arg):
    if os.path.isdir(arg):
        return os.path.abspath(arg)
    cand = os.path.join(REPO, "AGENTS", arg)
    return cand if os.path.isdir(cand) else None


def scan_agent(agent_dir, days, glob_pats, strict=False, writes=False, writes_bar=12,
               abs_floor=False, abs_days=90):
    name = os.path.basename(agent_dir.rstrip("/"))
    status_t = file_time(os.path.join(agent_dir, "STATUS.md"))
    now = datetime.datetime.now().timestamp()
    rows = []
    matched = []
    for gp in glob_pats:
        matched.extend(glob.glob(os.path.join(agent_dir, gp)))
    for led in sorted(set(matched)):
        t = file_time(led)
        frozen = is_frozen(led)
        exempt = (not strict) and is_exempt(led)
        age = (status_t - t) / 86400.0 if (status_t and t) else None
        stale = (not frozen) and (not exempt) and age is not None and age > days
        live = not frozen and not exempt
        # (a) activity-denominated unit: STATUS-writes since the ledger's commit.
        wb = status_writes_since(agent_dir, led) if (writes and live) else None
        stale_w = writes and live and wb is not None and wb >= writes_bar
        # (c) absolute floor: content vintage beats the relative delta (PAT-092 counter).
        abs_age = (now - t) / 86400.0 if (abs_floor and live and t) else None
        stale_a = abs_floor and live and abs_age is not None and abs_age > abs_days
        rows.append({
            "file": os.path.relpath(led, REPO),
            "frozen": frozen,
            "exempt": exempt,
            "age_d": age,
            "stale": stale or stale_w or stale_a,
            "writes_behind": wb,
            "stale_writes": stale_w,
            "abs_age_d": abs_age,
            "stale_abs": stale_a,
        })
    return name, status_t, rows


def nudge(agent_dir, name):
    """(b) pre-commit nudge (staleness-cadence proposal, Will-approved 2026-08-20):
    thresholdless — if STATUS is moving this session and live ledgers are >=1
    STATUS-write behind, enumerate them all, count first (output shape v2, see module
    docstring — v1's worst+"+N more" buried the work-list at n=2 desks on day one).
    Ledgers declaring 'Cadence: EVENT-DRIVEN' report under a distinct label with
    their re-pull clock and do NOT count behind (nudge mode only). rc: 0 no-gap ·
    1 nudged · 2 cannot-certify (incl. event-driven with no re-pull clock).
    Advisory by design (the lines are the deliverable); it fires at the moment the
    gap is created, which is the PAT-095 lesson."""
    decl = read_ledger_glob(agent_dir)
    pats = decl if decl is not None else ["workbook/*.tsv"]
    matched = []
    for gp in pats:
        matched.extend(glob.glob(os.path.join(agent_dir, gp)))
    live = [l for l in sorted(set(matched)) if not is_frozen(l) and not is_exempt(l)]
    if not live:
        print(f"nudge: [{name}] no live ledgers under {' '.join(pats)} — nothing to nudge (scope stated, not silent)")
        return 0
    if not status_moved_this_session(agent_dir):
        print(f"nudge: [{name}] STATUS not moving this session — no gap being created")
        return 0
    behind, event_driven, sched_quiet, exempt_ok, misdeclared = [], [], [], [], []
    today = datetime.date.today()
    pins = kernel_pins()
    for l in live:
        wb = status_writes_since(agent_dir, l)
        if wb is None or wb < 1:
            continue
        ex = exempt_by_charter(l)
        if ex is not None:
            (exempt_ok if ex[0] == "ok" else misdeclared).append((wb, l, "EXEMPT-BY-CHARTER", ex[1]))
            continue
        sch = scheduled_next_due(l)
        if sch is not None:
            if sch[0] == "unparseable":
                misdeclared.append((wb, l, "SCHEDULED", sch[1]))
            elif sch[1] > today:
                sched_quiet.append((wb, l, sch[1]))
            else:
                behind.append((wb, l, f"SCHEDULED, next_due {sch[1]} PASSED"))
            continue
        if is_event_driven(l):
            event_driven.append((wb, l))
        else:
            behind.append((wb, l, None))
    if not (behind or event_driven or sched_quiet or exempt_ok or misdeclared):
        print(f"nudge: [{name}] STATUS moving WITH its ledgers — clean ({len(live)} live ledger(s) checked)")
        return 0
    rc = 0
    if behind:
        behind.sort(key=lambda t: t[0], reverse=True)
        # UNIT RENDERED AS MEASURED (fix 2026-08-20, REGINALD via PROME): this counter is
        # STATUS-WRITES-behind, and "w" read as WEEKS. On a high-volume day every ledger
        # accumulates one per STATUS commit regardless of freshness -- REGINALD committed
        # STATUS 8x and a ledger written NINE MINUTES earlier printed "3w". A check that
        # reads catastrophically wrong on the desk's most productive day trains skipping
        # (PAT-110 inverse / PAT-116 family: measurement right, output shape misleads).
        def _item(wb, l, note):
            bits = [f"{wb} STATUS-write{'' if wb == 1 else 's'} behind"]
            if note:
                bits.append(note)
            rel = os.path.relpath(l, REPO)
            if rel in pins:
                locs = sorted(pins[rel])
                shown = ", ".join(locs[:4]) + ("…" if len(locs) > 4 else "")
                bits.append(f"⛔ {len(locs)} Kernel-pinned row(s): {shown} — byte-frozen, refresh only UNPINNED rows")
            return f"{os.path.basename(l)} ({'; '.join(bits)})"
        items = ", ".join(_item(wb, l, note) for wb, l, note in behind)
        print(f"⚠️  nudge: [{name}] STATUS moving without ledgers — {len(behind)} ledger(s) behind: "
              f"{items} — freeze-or-refresh EACH, or say why not in the commit")
        rc = 1
    for wb, l, nd in sorted(sched_quiet, key=lambda t: t[0], reverse=True):
        print(f"ℹ️  nudge: [{name}] scheduled: {os.path.basename(l)} ({wb} STATUS-write"
              f"{'' if wb == 1 else 's'} behind — correctly quiet by declaration until next_due {nd})")
    for wb, l, _, clause in sorted(exempt_ok, key=lambda t: t[0], reverse=True):
        print(f"ℹ️  nudge: [{name}] exempt-by-charter: {os.path.basename(l)} ({wb} STATUS-write"
              f"{'' if wb == 1 else 's'} behind — not counted; charter clause: {clause[:90]})")
    for wb, l, kind, raw in misdeclared:
        what = (f"declares Cadence: SCHEDULED but next_due {raw!r} is not a strict YYYY-MM-DD date"
                if kind == "SCHEDULED" else
                "declares Cadence: EXEMPT-BY-CHARTER with NO charter clause after the token")
        print(f"🔴 nudge: [{name}] {kind}: {os.path.basename(l)} ({wb} STATUS-write"
              f"{'' if wb == 1 else 's'} behind) {what} — a declaration that cannot be read "
              f"exempts nothing; fix the header or drop the declaration")
        rc = 2
    if "__unparseable__" in pins:
        bad = sorted(pins["__unparseable__"])
        print(f"🔴 nudge: [{name}] {len(bad)} Kernel submission/event file(s) UNPARSEABLE — pin set incomplete: "
              f"{', '.join(bad[:3])}{'…' if len(bad) > 3 else ''}")
        rc = 2
    for wb, l in sorted(event_driven, reverse=True):
        rp = repull_date(l)
        if rp:
            print(f"ℹ️  nudge: [{name}] event-driven: {os.path.basename(l)} ({wb} STATUS-write"
                  f"{'' if wb == 1 else 's'} behind — absence "
                  f"expected by declaration; re-pull attempted {rp}) — confirm the re-pull clock moved")
        else:
            print(f"🔴 nudge: [{name}] event-driven: {os.path.basename(l)} ({wb} STATUS-write"
                  f"{'' if wb == 1 else 's'} behind) declares "
                  f"Cadence: EVENT-DRIVEN but has NO parseable 'Last re-pull ATTEMPTED: YYYY-MM-DD' "
                  f"line — absence-expected certifies nothing unless somebody provably looked; "
                  f"add the re-pull clock or drop the declaration")
            rc = 2
    return rc


def fmt_age(age):
    if age is None:
        return "  ?  "
    return f"{age:+5.0f}d"


def report(name, status_t, rows, quiet):
    stale = [r for r in rows if r["stale"]]
    if quiet and not stale:
        return 0
    if not rows:
        if not quiet:
            print(f"[{name}] no workbook ledgers found")
        return 0
    if quiet:
        # One-line boot alert.
        def _why(r):
            bits = [f"{fmt_age(r['age_d']).strip()} behind"]
            if r.get("stale_writes"):
                bits.append(f"{r['writes_behind']}w")
            if r.get("stale_abs"):
                bits.append(f"ABS {r['abs_age_d']:.0f}d")
            return f"{os.path.basename(r['file'])} ({', '.join(bits)})"
        flags = ", ".join(_why(r) for r in stale)
        print(f"⚠️  [{name}] {len(stale)} stale ledger(s) behind STATUS: {flags}")
        return len(stale)
    # In non-quiet mode hide exempt-and-fresh-looking noise unless they'd be stale.
    show = [r for r in rows if not (r["exempt"] and not r["frozen"]) or r["stale"]]
    if not show:
        if not quiet:
            print(f"[{name}] all ledgers ok/ref ({len(rows)} scanned)")
        return 0
    # Legend sign verified against the arithmetic 2026-08-21 (BRENT flag, confirmed):
    # age = status_mtime − ledger_mtime, so an OLDER-than-STATUS ledger prints "+".
    # The legend below said "-" for 6+ weeks — inverted since birth.
    print(f"\n[{name}]  (ledger age relative to STATUS.md; + = older than STATUS)")
    for r in show:
        if r["frozen"]:
            tag = "FROZEN"
        elif r["exempt"]:
            tag = "ref"
        elif r["stale"]:
            tag = "⚠️ STALE"
        else:
            tag = "ok"
        extra = ""
        if r.get("writes_behind") is not None:
            extra += f"  {r['writes_behind']:>3}w"
        if r.get("abs_age_d") is not None:
            extra += f"  abs {r['abs_age_d']:>4.0f}d"
        print(f"  {tag:<8} {fmt_age(r['age_d'])}{extra}  {os.path.relpath(r['file'])}")
    if stale:
        print(f"  → {len(stale)} stale: freeze (add 'FROZEN <date> — ...' banner) or refresh at closeout.")
    return len(stale)


def main():
    ap = argparse.ArgumentParser(description="Workbook-ledger staleness alert (Data Hygiene enforcement).")
    ap.add_argument("agent", nargs="?", help="agent name (REGINALD) or path (AGENTS/REGINALD)")
    ap.add_argument("--all", action="store_true", help="scan every AGENTS/*/ with a workbook/")
    ap.add_argument("--days", type=int, default=30, help="staleness threshold in days behind STATUS (default 30 = rot, not mild drift)")
    ap.add_argument("--glob", default="workbook/*.tsv", help="ledger glob relative to agent dir (default workbook/*.tsv)")
    ap.add_argument("--trade", action="store_true", help="scan trade/position surfaces (TRADE.md / trade/TRADE.md / TRADE_BOOK.md / POSITIONS.md) instead of workbook/*.tsv")
    ap.add_argument("--quiet", action="store_true", help="print only agents with stale ledgers (one line each)")
    ap.add_argument("--strict", action="store_true", help="disable by-name exemptions (schema/archive/backup/history/etc.)")
    ap.add_argument("--nudge", action="store_true", help="(b) closeout nudge: enumerate all live ledgers >=1 STATUS-write behind while STATUS is moving this session (single agent only; thresholdless). Correctly-quiet declarations (header block, `Cadence:`-prefixed): EVENT-DRIVEN (+re-pull clock) · SCHEDULED next_due=YYYY-MM-DD · EXEMPT-BY-CHARTER — <clause>. Kernel byte-pinned rows are named beside a behind ledger (refresh only UNPINNED rows). rc 0/1/2 (2 = a declaration or pin set that cannot be read)")
    ap.add_argument("--writes", action="store_true", help="(a) also measure staleness in STATUS-commits-since-ledger-commit; flag at --writes-bar (activity-denominated — sprints can't hide, idle agents don't false-flag)")
    ap.add_argument("--writes-bar", type=int, default=12, help="writes-behind flag threshold for --writes (default 12)")
    ap.add_argument("--abs-floor", action="store_true", help="(c) also flag any live ledger whose absolute content vintage exceeds --abs-days regardless of the relative delta (PAT-092 counter)")
    ap.add_argument("--abs-days", type=int, default=90, help="absolute-age floor in days for --abs-floor (default 90)")
    args = ap.parse_args()

    if args.nudge:
        if args.all or not args.agent:
            print("error: --nudge takes a single agent (it is a closeout step, not a sweep)", file=sys.stderr)
            return 2
        d = resolve_agent_dir(args.agent)
        if not d:
            print(f"error: agent dir not found for '{args.agent}'", file=sys.stderr)
            return 2
        return nudge(d, os.path.basename(d.rstrip("/")))

    cli_glob_explicit = args.glob != ap.get_default("glob")

    if args.all:
        # Anchor on STATUS.md (every real agent) in BOTH modes. The old workbook/
        # anchor made an agent without that dir invisible to the sweep entirely —
        # the same enumeration-omission class as YEYOU-couldn't-see-PROME (PAT-071
        # family; TERRY-S1 fix 2026-07-31). report_unmatched() decides what a
        # workbook-less agent's 0-match means; it is never silently skipped.
        dirs = sorted(
            os.path.dirname(p)
            for p in glob.glob(os.path.join(REPO, "AGENTS", "*", "STATUS.md"))
        )
    elif args.agent:
        d = resolve_agent_dir(args.agent)
        if not d:
            print(f"error: agent dir not found for '{args.agent}'", file=sys.stderr)
            return 2
        dirs = [d]
    else:
        ap.print_help()
        return 2

    total_stale = 0
    warnings = 0
    trade_unmatched = []
    for d in dirs:
        if args.trade:
            pats, decl = TRADE_GLOBS, None
        else:
            decl = read_ledger_glob(d)
            if cli_glob_explicit:
                pats = [args.glob]
            elif decl is not None:
                pats = decl
            else:
                pats = [args.glob]
        name, status_t, rows = scan_agent(d, args.days, pats, strict=args.strict,
                                          writes=args.writes, writes_bar=args.writes_bar,
                                          abs_floor=args.abs_floor, abs_days=args.abs_days)
        if not args.trade and not rows:
            warnings += report_unmatched(d, name, pats, decl, args.quiet)
            continue
        if args.trade and not rows:
            # Fail-loud on the trade pass's silent-null class (sweep #3, 2026-08-11):
            # 16 of 38 agents matched NO trade surface and, under --quiet, printed
            # NOTHING — so a zero-flag pass read as "the fleet's position surfaces
            # are clean" while certifying only the ~24 matched files. Collected here,
            # stated once in the perimeter line below (CHECK_STANDARD §2/§4).
            trade_unmatched.append(name)
            continue
        total_stale += report(name, status_t, rows, args.quiet)
        # Perimeter line (2026-08-22, Will-approved): state what this pass did NOT
        # examine. Prints under --quiet BY DESIGN — --quiet is exactly where the
        # false-green lived (a boot step that printed nothing and meant "clean").
        # Fires only when there IS something to say, so the 13 agents with no
        # unscanned TSVs see no new output. Advisory: does NOT touch the rc contract,
        # because "not scanned" is a coverage fact, not a finding.
        if not args.trade:
            matched_now = []
            for gp in pats:
                matched_now.extend(glob.glob(os.path.join(d, gp)))
            unscanned = unscanned_outside_glob(d, matched_now)
            if unscanned:
                shown = ", ".join(unscanned[:4])
                more = f" (+{len(unscanned) - 4} more)" if len(unscanned) > 4 else ""
                print(f"  perimeter [{name}]: {len(rows)} ledger(s) scanned; "
                      f"{len(unscanned)} TSV(s) NOT scanned by this pass: {shown}{more}")
    if args.trade:
        graded = len(dirs) - len(trade_unmatched)
        line = (f"trade perimeter: {graded} agent(s) with a matching trade surface graded; "
                f"{len(trade_unmatched)} agent(s) matched NO trade surface and are NOT "
                f"certified by this pass")
        if trade_unmatched:
            line += ": " + ", ".join(sorted(trade_unmatched))
        print(line)

    if args.all and not args.quiet:
        tail = f"; {warnings} enforcement warning(s)" if warnings else ""
        print(f"\n== {total_stale} stale ledger(s) across {len(dirs)} agents (threshold {args.days}d behind STATUS){tail} ==")
    # Exit-code contract (2026-08-17, header): 2 = enforcement/config warnings
    # (cannot certify scope) dominates 1 = stale findings; 0 = clean.
    if warnings:
        return 2
    return 1 if total_stale else 0


if __name__ == "__main__":
    sys.exit(main())
