#!/usr/bin/env python3
"""
agent_freshness.py — ground-truth agent staleness, replacing narrative-derived reads.

WHY (Will-directed 2026-08-14): PROME's "who is stale / who needs a boot" was
derived from narrative snapshots (SCRATCH spawn-queue lines, HANDOFF watch
lists) written at closeout — which rot within HOURS on multi-window days.
Case study, same morning this shipped: SCRATCH said HOMER was lapsed-and-owed;
HOMER had run the previous afternoon in Will's own window, and its
encode-confirms sat UNREAD in PROME/inbox while PROME wrote a launch brief
tasking the already-ratified work. Two distinct rots, both invisible to prose:
  1. AGENT staleness — when did the agent's OWN surfaces last change?
     (commits touching its tree EXCLUDING inbox/, since inbound packets land
     there without the agent running)
  2. PROME's KNOWLEDGE staleness — packets FROM that agent sitting unread in
     PROME/inbox. This is the one that actually bit: the agent was fresh,
     PROME's model of it was not.

CONTRACT (encoded in ORCHESTRATION_PLAYBOOK pre-spawn checklist, 2026-08-14):
  Before writing ANY launch brief:  python3 PROME/tools/agent_freshness.py --agent <NAME>
  rc=1 there means STOP — unread from-<NAME> packets exist in PROME/inbox (or
  its tree holds uncommitted work): drain/inspect BEFORE briefing, because a
  brief written against undrained packets tasks work that may already be done.

USAGE
  agent_freshness.py                # fleet table, quiet tail (>45d + no signals) hidden
  agent_freshness.py --all          # include the quiet tail (dormant/retired dirs)
  agent_freshness.py --agent HOMER  # scoped pre-spawn check; rc=1 = drain first
  agent_freshness.py --gate         # prome_gate mode: one line; rc=1 if ANY unread
                                    # from-agent packets sit in PROME/inbox
  (always from repo root — pathspecs resolve relative to cwd)

Notes: uses `git log -1` (never bare --since — finding_bare_since_date_drops_
same_day_commits). Committer time, not mtime (finding_mtime_is_corrupted_by_
git_sync). Own-surface age is a LOWER bound on staleness, not proof of
caught-up (finding_freshness_audit_vs_caught_up): a fresh agent can still be
behind on its inbox — which is why inbox depth prints beside age.
"""
import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
AGENTS = ROOT / "AGENTS"
PROME_INBOX = ROOT / "PROME" / "inbox"
CONSUMED = {"processed", "delivered", "archive", "archived"}
STALE_DAYS = 7          # flag threshold on own-surface age
QUIET_DAYS = 45         # default-hidden tail (dormant/retired dirs, ROSTER is truth)


def git(*args):
    p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=60)
    return p.stdout.strip()


def own_surface_age_days(name):
    """Days since the agent's own (non-inbox) tree last changed in a commit."""
    ts = git("log", "-1", "--format=%ct", "--",
             f"AGENTS/{name}", f":(exclude)AGENTS/{name}/inbox")
    if not ts:
        return None
    return (time.time() - int(ts)) / 86400


def pending_inbox(name):
    """Unconsumed files in the agent's inbox (any depth, consumed dirs excluded)."""
    box = AGENTS / name / "inbox"
    if not box.is_dir():
        return []
    return sorted(p for p in box.rglob("*") if p.is_file()
                  and not (CONSUMED & {q.lower() for q in p.relative_to(box).parts[:-1]}))


def unread_to_prome(name):
    """Packets FROM this agent sitting unconsumed in PROME/inbox (flat, per the
    7/24 ruling — anything in a subdir except processed/ is itself a defect)."""
    pat = re.compile(rf"from-{re.escape(name)}[_.]", re.IGNORECASE)
    return sorted(p for p in PROME_INBOX.rglob("*") if p.is_file()
                  and not (CONSUMED & {q.lower() for q in p.relative_to(PROME_INBOX).parts[:-1]})
                  and pat.search(p.name))


def dirty_paths(name):
    out = git("status", "--porcelain", "--", f"AGENTS/{name}")
    return [ln for ln in out.splitlines() if ln.strip()]


def agent_names():
    return sorted(d.name for d in AGENTS.iterdir()
                  if d.is_dir() and not d.name.startswith("."))


def row(name):
    return {
        "name": name,
        "age": own_surface_age_days(name),
        "inbox": pending_inbox(name),
        "to_prome": unread_to_prome(name),
        "dirty": dirty_paths(name),
    }


def fmt_age(a):
    return "  never" if a is None else f"{a:6.1f}d"


def main():
    ap = argparse.ArgumentParser(description="ground-truth agent freshness")
    ap.add_argument("--agent", help="scoped pre-spawn check for one agent")
    ap.add_argument("--all", action="store_true", help="include the quiet tail")
    ap.add_argument("--gate", action="store_true", help="prome_gate one-liner mode")
    ap.add_argument("--stale-days", type=float, default=STALE_DAYS)
    args = ap.parse_args()

    if args.agent:
        n = args.agent.upper()
        if not (AGENTS / n).is_dir():
            print(f"no such agent dir: AGENTS/{n}")
            return 2
        r = row(n)
        print(f"AGENT FRESHNESS · {n} · own-surface age {fmt_age(r['age']).strip()}"
              f" (excludes inbound packets; lower bound, not caught-up proof)")
        for label, items in (("unread from-agent packets in PROME/inbox — DRAIN BEFORE BRIEFING",
                              r["to_prome"]),
                             ("pending in its own inbox (brief should name these)", r["inbox"]),
                             ("uncommitted paths in its tree (in-flight or orphaned — do not sweep)",
                              r["dirty"])):
            print(f"  {len(items)} {label}")
            for it in items[:20]:
                print(f"      {it if isinstance(it, str) else it.relative_to(ROOT)}")
            if len(items) > 20:
                print(f"      (+{len(items)-20} more)")
        blocked = bool(r["to_prome"]) or bool(r["dirty"])
        print(("  🔴 rc=1 — drain/inspect the above BEFORE writing the launch brief"
               if blocked else "  ✅ clear to brief"))
        return 1 if blocked else 0

    rows = [row(n) for n in agent_names()]
    if args.gate:
        unread = [(r["name"], len(r["to_prome"])) for r in rows if r["to_prome"]]
        if unread:
            print("unread from-agent packets in PROME/inbox: "
                  + ", ".join(f"{n}×{c}" for n, c in unread)
                  + " — drain before briefing/spawning those agents")
            return 1
        print("PROME/inbox holds no unread from-agent packets")
        return 0

    shown, hidden = [], 0
    for r in rows:
        quiet = (r["age"] is not None and r["age"] > QUIET_DAYS
                 and not r["inbox"] and not r["to_prome"] and not r["dirty"])
        if quiet and not args.all:
            hidden += 1
            continue
        shown.append(r)
    shown.sort(key=lambda r: -(r["age"] or 1e9))
    print(f"{'agent':10} {'own-age':>8} {'inbox':>6} {'→PROME':>7} {'dirty':>6}   flags")
    for r in shown:
        flags = []
        if r["age"] is not None and r["age"] > args.stale_days:
            flags.append(f"STALE>{args.stale_days:g}d")
        if r["to_prome"]:
            flags.append("DRAIN-FIRST")
        if r["dirty"]:
            flags.append("IN-FLIGHT/ORPHANED")
        print(f"{r['name']:10} {fmt_age(r['age'])} {len(r['inbox']):6d} "
              f"{len(r['to_prome']):7d} {len(r['dirty']):6d}   {' '.join(flags)}")
    if hidden:
        print(f"(+{hidden} quiet-tail dirs hidden: >{QUIET_DAYS}d old, zero pending signals — "
              f"--all to show; ROSTER.md is the live-vs-shelved truth, this table is activity only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
