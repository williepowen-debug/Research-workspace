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

Timestamps use each file's last git-commit time (falls back to filesystem mtime
for uncommitted files). Exit code is always 0 — this is an alert, not a gate.

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
STATIC_BANNER_MARKERS = ["FROZEN", "RETIRED", "NOT CURRENT", "DO NOT CITE", "NOT MAINTAINED", "ARCHIVED"]

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

# Trade/position surfaces scanned under --trade (default glob stays workbook/*.tsv).
TRADE_GLOBS = ["TRADE.md", "trade/TRADE.md", "TRADE_BOOK.md", "POSITIONS.md"]


def is_frozen(path):
    """True if the header (first ~6 lines) declares the surface intentionally static.
    Named is_frozen for call-site compatibility; recognizes the whole dead-banner set.
    Banner-FORM rules (2026-07-22 hardening, see MARKER_RES comment): "Status: LIVE"
    wins; marker must start within MARKER_COL_CAP of its line; negated/glued
    mentions don't count."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            lines = [f.readline() for _ in range(6)]
        head = "".join(lines).upper()
        if LIVE_DECL_RE.search(head):
            return False
        for line in lines:
            u = line.upper()
            for rx in MARKER_RES:
                m = rx.search(u)
                if m and m.start() < MARKER_COL_CAP:
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

    globs = TRADE_GLOBS if args.trade else [args.glob]

    if args.all:
        # trade mode: anchor on STATUS.md (every real agent) and let scan_agent find
        # its trade surfaces; workbook mode: anchor on the workbook/ dir as before.
        anchor = "STATUS.md" if args.trade else "workbook"
        dirs = sorted(
            os.path.dirname(p)
            for p in glob.glob(os.path.join(REPO, "AGENTS", "*", anchor))
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
    for d in dirs:
        name, status_t, rows = scan_agent(d, args.days, globs, strict=args.strict)
        total_stale += report(name, status_t, rows, args.quiet)

    if args.all and not args.quiet:
        print(f"\n== {total_stale} stale ledger(s) across {len(dirs)} agents (threshold {args.days}d behind STATUS) ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
