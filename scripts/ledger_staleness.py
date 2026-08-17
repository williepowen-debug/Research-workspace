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
  python3 scripts/ledger_staleness.py REGINALD --days 21 # threshold (default 14)
  python3 scripts/ledger_staleness.py REGINALD --quiet   # print only when stale
  python3 scripts/ledger_staleness.py REGINALD --glob 'workbook/*.tsv'  # custom location

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


def _line_has_marker(u_line):
    """Un-negated, un-glued banner marker in the pre-tab portion of ONE uppercased
    line, within MARKER_COL_CAP, and not a row-retention policy sentence (rule 6)."""
    scan = u_line.split("\t", 1)[0]
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


def scan_agent(agent_dir, days, glob_pats, strict=False):
    name = os.path.basename(agent_dir.rstrip("/"))
    status_t = file_time(os.path.join(agent_dir, "STATUS.md"))
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
        rows.append({
            "file": os.path.relpath(led, REPO),
            "frozen": frozen,
            "exempt": exempt,
            "age_d": age,
            "stale": stale,
        })
    return name, status_t, rows


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
        flags = ", ".join(f"{os.path.basename(r['file'])} ({fmt_age(r['age_d']).strip()} behind)" for r in stale)
        print(f"⚠️  [{name}] {len(stale)} stale ledger(s) behind STATUS: {flags}")
        return len(stale)
    # In non-quiet mode hide exempt-and-fresh-looking noise unless they'd be stale.
    show = [r for r in rows if not (r["exempt"] and not r["frozen"]) or r["stale"]]
    if not show:
        if not quiet:
            print(f"[{name}] all ledgers ok/ref ({len(rows)} scanned)")
        return 0
    print(f"\n[{name}]  (ledger age relative to STATUS.md; - = older than STATUS)")
    for r in show:
        if r["frozen"]:
            tag = "FROZEN"
        elif r["exempt"]:
            tag = "ref"
        elif r["stale"]:
            tag = "⚠️ STALE"
        else:
            tag = "ok"
        print(f"  {tag:<8} {fmt_age(r['age_d'])}  {os.path.relpath(r['file'])}")
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
    args = ap.parse_args()

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
        name, status_t, rows = scan_agent(d, args.days, pats, strict=args.strict)
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
