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
  agent_freshness.py                # activity table; manual sessions labeled, quiet tail hidden
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

Manual sessions: read the explicit exclusion in ROSTER's CLASSIFICATION PENDING
section once per invocation. Activity and messages remain visible, without fleet
staleness or launch-clearance cues. An unreadable or ambiguous declaration exits
2 (CANNOT-EVALUATE), never clearance. --gate still reports unread manual messages
with rc=1 for inspection; it does not authorize launching or routing to them.
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


# L294 F-4 (reproduced 2026-09-12 before repair): `git()` returned p.stdout.strip()
# without ever reading `returncode`, so rc=128 and rc=0-with-no-output were the SAME
# value — "" — to every caller. Two different facts, one representation. Acceptance
# conditions: PROME/tools/tests/ACCEPTANCE_agent_freshness_L294_F4.md
class _Unknown:
    """Sentinel: the query FAILED. Distinct from "" (ran, found nothing) and from
    None (which callers already use for "no data").

    ⛔ FALSY, deliberately, and this is a REGRESSION FIX (independent review
    2026-09-12): the first version was a bare `object()`, which is TRUTHY.
    `fleet_dashboard.py:1014` reads `int(ts) if ts else None` — with a truthy
    sentinel that became `int(<object>)` -> TypeError where it used to yield None
    and classify the desk "no git history". Truthiness is the one property no
    caller thinks to check, so the sentinel must answer it correctly: a failed
    query is not a value, and `if ts:` must be False.
    `[[finding_inherited_defect_propagates_though_both_ends_act_correctly]]`"""
    __slots__ = ()

    def __bool__(self):
        return False

    def __repr__(self):
        return "<agent_freshness.UNKNOWN: git query failed>"

    def __len__(self):
        return 0          # so `len(x)` and emptiness tests degrade to "nothing", not a raise

    def __iter__(self):
        return iter(())   # a caller iterating results gets no rows, never a crash


UNKNOWN = _Unknown()


def git(*args):
    """stdout on success; UNKNOWN if git exited non-zero or could not be run.

    ⛔ `""` is a legitimate SUCCESS value here (no commits match, no dirty paths) and
    must never be conflated with failure — that conflation IS F-4."""
    try:
        p = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True, timeout=60)
    except Exception:
        return UNKNOWN
    return UNKNOWN if p.returncode != 0 else p.stdout.strip()


def own_surface_age_state(name):
    """Three states, because there are three facts:
         ("aged", <float days>)  the tree has commits
         ("never", None)         the query RAN and found no commit touching it
         ("unknown", None)       the query FAILED — nothing was established
    A desk with no commits is the MOST stale state, not the freshest; collapsing it
    into a number is what made it unflaggable."""
    ts = git("log", "-1", "--format=%ct", "--",
             f"AGENTS/{name}", f":(exclude)AGENTS/{name}/inbox")
    if ts is UNKNOWN:
        return ("unknown", None)
    if not ts:
        return ("never", None)
    try:
        return ("aged", (time.time() - int(ts)) / 86400)
    except ValueError:
        return ("unknown", None)


def own_surface_age_days(name):
    """Days since the agent's own (non-inbox) tree last changed in a commit.
    None for BOTH "never committed" and "query failed" — kept for the display
    paths, which render None honestly as `never`/`no git history`.
    ⚠️ Any caller that BRANCHES on the value must use own_surface_age_state()
    instead: `(own_surface_age_days(x) or 0)` reads None as 0 days = brand new."""
    return own_surface_age_state(name)[1]


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
    """Porcelain lines for the agent's tree, or UNKNOWN if git could not tell us.

    ⛔ Returning [] on a FAILED `git status` printed "clear to brief" over an
    in-flight tree — and this feeds the pre-spawn STOP in the module header.
    Fail closed: unknown is not clean."""
    out = git("status", "--porcelain", "--", f"AGENTS/{name}")
    if out is UNKNOWN:
        return UNKNOWN
    return [ln for ln in out.splitlines() if ln.strip()]


def agent_names():
    return sorted(d.name for d in AGENTS.iterdir()
                  if d.is_dir() and not d.name.startswith("."))


def manual_only_names():
    """Read the existing roster hold; never infer manual status from directories."""
    lines = (ROOT / "PROME/ROSTER.md").read_text(encoding="utf-8").splitlines()
    starts = [i for i, line in enumerate(lines)
              if re.match(r"^## CLASSIFICATION PENDING(?:\s|$)", line)]
    if len(starts) != 1:
        raise ValueError("ROSTER needs exactly one CLASSIFICATION PENDING section")
    start = starts[0]
    count = re.search(r"\((\d+)\)\s*$", lines[start])
    if count is None:
        raise ValueError("CLASSIFICATION PENDING needs its declared member count")
    names = set()
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        if re.match(r"^\s*(?:[-+*]|\d+[.)])\s", line) and not line.startswith("- "):
            raise ValueError("unsupported manual-session bullet in CLASSIFICATION PENDING")
        if not line.startswith("- "):
            continue
        match = re.match(r"^- \*\*([A-Z][A-Z0-9_-]*)\*\*", line)
        if match is None or "Excluded from automatic launch and signal routing." not in line:
            raise ValueError("malformed manual-session row in CLASSIFICATION PENDING")
        name = match.group(1)
        if name in names:
            raise ValueError(f"duplicate manual-session row: {name}")
        names.add(name)
    if len(names) != int(count.group(1)):
        raise ValueError("CLASSIFICATION PENDING count disagrees with its named rows")
    return names


def row(name):
    return {
        "name": name,
        "age_state": own_surface_age_state(name)[0],
        "age": own_surface_age_days(name),
        "inbox": pending_inbox(name),
        "to_prome": unread_to_prome(name),
        "dirty": dirty_paths(name),
    }


def fmt_age(a, state=None):
    """`never` = the query ran and found no commit. `  ???` = the query FAILED.
    Rendering both as `never` would assert a fact git never supplied."""
    if a is None:
        return "   ???" if state == "unknown" else "  never"
    return f"{a:6.1f}d"


def main():
    ap = argparse.ArgumentParser(description="ground-truth agent freshness")
    ap.add_argument("--agent", help="scoped pre-spawn check for one agent")
    ap.add_argument("--all", action="store_true", help="include the quiet tail")
    ap.add_argument("--gate", action="store_true", help="prome_gate one-liner mode")
    ap.add_argument("--stale-days", type=float, default=STALE_DAYS)
    args = ap.parse_args()

    try:
        manual = manual_only_names()
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"CANNOT-EVALUATE: manual-session classification unavailable: {exc}")
        return 2

    if args.agent:
        n = args.agent.upper()
        if not (AGENTS / n).is_dir():
            print(f"no such agent dir: AGENTS/{n}")
            return 2
        r = row(n)
        if n in manual:
            print(f"MANUAL SESSION · {n} · no automatic launch or signal routing")
            print(f"  own-surface age {fmt_age(r['age'], r['age_state']).strip()} "
                  "(activity only; no cadence expectation)")
            for label, items in (("messages in PROME/inbox awaiting inspection", r["to_prome"]),
                                 ("files in the session inbox", r["inbox"]),
                                 ("uncommitted paths; do not sweep", r["dirty"])):
                if items is UNKNOWN:
                    print(f"  UNKNOWN {label}")
                else:
                    print(f"  {len(items)} {label}")
                    for item in items[:20]:
                        print(f"      {item if isinstance(item, str) else item.relative_to(ROOT)}")
                    if len(items) > 20:
                        print(f"      (+{len(items)-20} more)")
            blocked = bool(r["to_prome"]) or r["dirty"] is UNKNOWN or bool(r["dirty"])
            print("  inspection needed; no launch authorization" if blocked else
                  "  manual-session inspection complete; no launch authorization")
            return 1 if blocked else 0
        print(f"AGENT FRESHNESS · {n} · own-surface age "
              f"{fmt_age(r['age'], r['age_state']).strip()}"
              + (" — ⚠️ git could not answer; this is NOT a freshness claim"
                 if r["age_state"] == "unknown" else
                 " — NO COMMIT EVER TOUCHED ITS OWN TREE (the most stale state, not the freshest)"
                 if r["age_state"] == "never" else "")
              + " (excludes inbound packets; lower bound, not caught-up proof)")
        for label, items in (("unread from-agent packets in PROME/inbox — DRAIN BEFORE BRIEFING",
                              r["to_prome"]),
                             ("pending in its own inbox (brief should name these)", r["inbox"]),
                             ("uncommitted paths in its tree (in-flight or orphaned — do not sweep)",
                              r["dirty"])):
            if items is UNKNOWN:
                print(f"  ⚠️ UNKNOWN (git failed) {label}")
                continue
            print(f"  {len(items)} {label}")
            for it in items[:20]:
                print(f"      {it if isinstance(it, str) else it.relative_to(ROOT)}")
            if len(items) > 20:
                print(f"      (+{len(items)-20} more)")
        unknown_dirty = r["dirty"] is UNKNOWN
        blocked = bool(r["to_prome"]) or unknown_dirty or bool(r["dirty"])
        print("  🔴 rc=1 — git could not report this tree's state; UNKNOWN is not CLEAN, "
              "establish it before briefing" if unknown_dirty else
              "  🔴 rc=1 — drain/inspect the above BEFORE writing the launch brief" if blocked else
              "  ✅ clear to brief")
        return 1 if blocked else 0

    rows = [row(n) for n in agent_names()]
    if args.gate:
        unread = [(r["name"], len(r["to_prome"])) for r in rows if r["to_prome"]]
        if unread:
            domain_unread = [(n, c) for n, c in unread if n not in manual]
            manual_unread = [(n, c) for n, c in unread if n in manual]
            if domain_unread:
                print("unread from-agent packets in PROME/inbox: "
                      + ", ".join(f"{n}×{c}" for n, c in domain_unread)
                      + " — drain before briefing/spawning those agents")
            if manual_unread:
                print("manual-session messages awaiting inspection: "
                      + ", ".join(f"{n}×{c}" for n, c in manual_unread)
                      + " — no automatic launch or routing")
            return 1
        print("PROME/inbox holds no unread from-agent packets")
        return 0

    shown, hidden = [], 0
    for r in rows:
        quiet = (r["age"] is not None and r["age"] > QUIET_DAYS
                 and not r["inbox"] and not r["to_prome"]
                 and r["dirty"] is not UNKNOWN and not r["dirty"])
        if quiet and not args.all:
            hidden += 1
            continue
        shown.append(r)
    shown.sort(key=lambda r: -(r["age"] or 1e9))
    print(f"{'agent':10} {'own-age':>8} {'inbox':>6} {'→PROME':>7} {'dirty':>6}   flags")
    for r in shown:
        if r["name"] in manual:
            flags = ["manual session; no automatic launch/routing"]
            if r["to_prome"]:
                flags.append("inspect messages")
            if r["age_state"] == "unknown" or r["dirty"] is UNKNOWN:
                flags.append("state UNKNOWN")
            elif r["dirty"]:
                flags.append("uncommitted work")
            nd = "     ?" if r["dirty"] is UNKNOWN else f"{len(r['dirty']):6d}"
            print(f"{r['name']:10} {fmt_age(r['age'], r['age_state'])} {len(r['inbox']):6d} "
                  f"{len(r['to_prome']):7d} {nd}   {'; '.join(flags)}")
            continue
        flags = []
        if r["age"] is not None and r["age"] > args.stale_days:
            flags.append(f"STALE>{args.stale_days:g}d")
        if r["to_prome"]:
            flags.append("DRAIN-FIRST")
        if r["age_state"] == "never":
            flags.append("NEVER-COMMITTED")
        elif r["age_state"] == "unknown":
            flags.append("AGE-UNKNOWN")
        if r["dirty"] is UNKNOWN:
            flags.append("DIRTY-UNKNOWN")
        elif r["dirty"]:
            flags.append("IN-FLIGHT/ORPHANED")
        nd = "     ?" if r["dirty"] is UNKNOWN else f"{len(r['dirty']):6d}"
        print(f"{r['name']:10} {fmt_age(r['age'], r['age_state'])} {len(r['inbox']):6d} "
              f"{len(r['to_prome']):7d} {nd}   {' '.join(flags)}")
    if hidden:
        print(f"(+{hidden} quiet-tail dirs hidden: >{QUIET_DAYS}d old, zero pending signals — "
              f"--all to show; ROSTER.md is the live-vs-shelved truth, this table is activity only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
