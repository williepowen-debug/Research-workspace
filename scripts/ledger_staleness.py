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
import glob
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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


def file_time(path):
    """Prefer git-commit time (clone/checkout-stable); fall back to fs mtime."""
    t = git_time(path)
    if t is not None:
        return t
    try:
        return int(os.path.getmtime(path))
    except OSError:
        return None


def is_frozen(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return "FROZEN" in f.readline().upper()
    except OSError:
        return False


def resolve_agent_dir(arg):
    if os.path.isdir(arg):
        return os.path.abspath(arg)
    cand = os.path.join(REPO, "AGENTS", arg)
    return cand if os.path.isdir(cand) else None


def scan_agent(agent_dir, days, glob_pat, strict=False):
    name = os.path.basename(agent_dir.rstrip("/"))
    status_t = file_time(os.path.join(agent_dir, "STATUS.md"))
    rows = []
    for led in sorted(glob.glob(os.path.join(agent_dir, glob_pat))):
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
    ap.add_argument("--quiet", action="store_true", help="print only agents with stale ledgers (one line each)")
    ap.add_argument("--strict", action="store_true", help="disable by-name exemptions (schema/archive/backup/history/etc.)")
    args = ap.parse_args()

    if args.all:
        dirs = sorted(
            os.path.dirname(p)
            for p in glob.glob(os.path.join(REPO, "AGENTS", "*", "workbook"))
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
        name, status_t, rows = scan_agent(d, args.days, args.glob, strict=args.strict)
        total_stale += report(name, status_t, rows, args.quiet)

    if args.all and not args.quiet:
        print(f"\n== {total_stale} stale ledger(s) across {len(dirs)} agents (threshold {args.days}d behind STATUS) ==")
    return 0


if __name__ == "__main__":
    sys.exit(main())
