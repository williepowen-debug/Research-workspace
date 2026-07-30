#!/usr/bin/env python3
"""YEYOU boot kit — the review-queue card.

Deterministically answers YEYOU's only boot question: *what changed since I last
looked, and which open findings need a re-check?* GLM then reads the diffs and
applies REVIEW_CHECKLIST.md (the judgment half). This script is the mechanical
half — it finds the work so the model spends tokens only on review.

READ-ONLY by design: prints, never writes state. Assumes origin/* is current
(run `git fetch origin` first — boot step 0). Modeled on RED/CORAL boot.py.

Usage:
  python3 AGENTS/YEYOU/scripts/boot.py                      # queue vs origin/master, per-agent watermarks from STATE.tsv
  python3 AGENTS/YEYOU/scripts/boot.py --ref origin/master  # change the branch being reviewed
  python3 AGENTS/YEYOU/scripts/boot.py --baseline <ref>     # override ALL watermarks (first run / ad-hoc / testing)
  python3 AGENTS/YEYOU/scripts/boot.py --verbose            # + commit subjects and up-to-date agents

Sources:
  watermarks    -> AGENTS/YEYOU/reviews/STATE.tsv   (per-agent last-reviewed commit; *DEFAULT* row = global baseline)
  open findings -> AGENTS/YEYOU/reviews/REVIEW_LOG.tsv
  the work      -> git log/diff over AGENTS/<agent>/ since each watermark

Mirrors SPAWN PROTOCOL boot steps 3 (watermarks) + 5 (this card) + 8 (OPEN-finding re-check).
"""
import csv
import subprocess
import sys
from datetime import date, datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
YEYOU = REPO / "AGENTS" / "YEYOU"
STATE_TSV = YEYOU / "reviews" / "STATE.tsv"
LOG_TSV = YEYOU / "reviews" / "REVIEW_LOG.tsv"
TODAY = date.today()

# dirs under AGENTS/ that are NOT review targets
SKIP = {"YEYOU", "templates"}

# Review targets that do NOT live under AGENTS/<NAME>/.
# PROME is the fleet coordinator and its home dir is PROME/ at the REPO ROOT, so
# an AGENTS/-only walk cannot see it at all — it was invisible to this queue
# until 2026-07-30 while being the single busiest writer in the tree (525 commits
# in the preceding 60d). Same AGENTS/*-globbing blind spot that hid PROME from
# DAEDALUS's FLEET_MAP until 7/28 and FORGE from ledger_staleness.py (PAT-071:
# the ownership unit and the enforcement unit must be the same unit).
# Set to {} to restore AGENTS-only review.
EXTRA_TARGETS = {"PROME": "PROME/"}
STALE_OPEN_DAYS = 14  # an OPEN finding older than this gets flagged to chase/close


def git(*args):
    r = subprocess.run(["git", *args], cwd=str(REPO), capture_output=True, text=True)
    return r.stdout.strip(), r.stderr.strip(), r.returncode


def read_tsv(path):
    if not path.exists():
        return []
    with open(path, newline="") as f:
        lines = [ln for ln in f if not ln.lstrip().startswith("#")]
    if not lines:
        return []
    return [r for r in csv.DictReader(lines, delimiter="\t")
            if any((v or "").strip() for v in r.values())]


def agent_dirs():
    """[(name, git-path)] for every review target.

    An agent dir is one that CONTAINS A CLAUDE.md. That predicate is what filters
    non-agents, and it is deliberately NOT a roster/dormancy lookup. It drops:
      • AGENTS/.claude  — tooling/config, not an agent (zero commits, ever)
      • AGENTS/PROME/   — a misrouting STUB that regrows whenever an agent
                          mis-addresses a packet (last drained 81cb8943, 9 packets).
                          The real PROME is in EXTRA_TARGETS.

    ⚠️ DORMANT AND ARCHIVE-SOURCE AGENTS ARE NOT FILTERED, ON PURPOSE. A commit
    landing in a supposedly-dead agent dir is precisely what a reviewer wants to
    see — and they are not quiet: in the 60d to 2026-07-30, CRUISE 5 / FERT 3 /
    BARON 1. Filtering by ROSTER liveness would suppress real review targets and
    would also restate a registry this script does not own (scripts READ a
    registry, never restate it). Dead-but-silent agents cost nothing: with a
    watermark set they simply never appear in the queue.
    """
    base = REPO / "AGENTS"
    out = [(p.name, f"AGENTS/{p.name}/") for p in sorted(base.iterdir())
           if p.is_dir()
           and p.name not in SKIP
           and not p.name.startswith("_")
           and (p / "CLAUDE.md").is_file()]
    out.extend(sorted(EXTRA_TARGETS.items()))
    return out


def watermarks():
    wm, default = {}, None
    for r in read_tsv(STATE_TSV):
        agent = (r.get("Agent") or "").strip()
        commit = (r.get("Last_Reviewed_Commit") or "").strip()
        if not agent or not commit:
            continue
        if agent == "*DEFAULT*":
            default = commit
        else:
            wm[agent] = commit
    return wm, default


def arg_val(flag, default=None):
    return sys.argv[sys.argv.index(flag) + 1] if flag in sys.argv else default


def main():
    verbose = "--verbose" in sys.argv
    ref = arg_val("--ref", "origin/master")
    baseline_override = arg_val("--baseline")

    print("=" * 72)
    print(" YEYOU BOOT KIT — review queue — " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("=" * 72)

    # ① git state
    branch, _, _ = git("rev-parse", "--abbrev-ref", "HEAD")
    head, _, _ = git("rev-parse", "--short", "HEAD")
    resolved, _, rc = git("rev-parse", "--verify", "--quiet", ref)
    print(f"\n① GIT STATE  branch={branch} head={head}")
    if rc != 0:
        print(f"   ⚠️  review ref '{ref}' not found — falling back to HEAD. Pass --ref <branch>.")
        ref, resolved = "HEAD", head
    print(f"   reviewing work on: {ref} ({resolved[:9]})")

    wm, default = watermarks()
    if baseline_override:
        print(f"   baseline OVERRIDE (all agents): {baseline_override}")
    elif default:
        print(f"   global baseline (*DEFAULT*): {default[:9]}")
    if not baseline_override and not wm and not default:
        print(f"   ⚠️  no watermarks in STATE.tsv — set a *DEFAULT* baseline (recommend current "
              f"{ref} = {resolved[:9]}) so YEYOU reviews only NEW work, not full history.")

    # ② review queue
    print("\n② REVIEW QUEUE — agents with new commits since their watermark")
    queue, no_baseline = [], []
    for agent, path in agent_dirs():
        base = baseline_override or wm.get(agent, default)
        if not base:
            no_baseline.append(agent)
            continue
        log, err, rc = git("log", "--oneline", f"{base}..{ref}", "--", path)
        if rc != 0:
            print(f"   ⚠️  {agent:<12} watermark {base[:9]} not in {ref} history — reset baseline (W2)")
            continue
        if not log:
            if verbose:
                print(f"   🟢 {agent:<12} up to date")
            continue
        commits = log.splitlines()
        stat, _, _ = git("diff", "--shortstat", f"{base}..{ref}", "--", path)
        queue.append((agent, len(commits), stat.strip(), commits))
    queue.sort(key=lambda x: -x[1])
    if not queue:
        print("   🟢 nothing to review — every agent at its watermark.")
    for agent, n, stat, commits in queue:
        print(f"   🔍 {agent:<12} {n:>2} commit(s)   {stat}")
        if verbose:
            for c in commits[:5]:
                print(f"        {c}")
    if no_baseline:
        print(f"   ⚪ no baseline yet (skipped): {', '.join(no_baseline)}")

    # ③ open findings / re-check
    print("\n③ OPEN FINDINGS — re-check fixes, chase stale (resolve at W1)")
    queue_agents = {a for a, *_ in queue}
    open_rows = [r for r in read_tsv(LOG_TSV) if (r.get("Status") or "").strip().upper() == "OPEN"]
    if not open_rows:
        print("   🟢 no OPEN findings in the ledger.")
    for r in open_rows:
        agent = (r.get("Agent") or "?").strip()
        fid = (r.get("Finding_ID") or "?").strip()
        sev = (r.get("Severity") or "·").strip()
        desc = (r.get("Finding") or "").strip()[:55]
        tags = []
        if agent in queue_agents:
            tags.append("↻ pushed again — check if fixed")
        try:
            age = (TODAY - datetime.strptime((r.get("Date") or "").strip(), "%Y-%m-%d").date()).days
            if age > STALE_OPEN_DAYS:
                tags.append(f"⏳ {age}d stale")
        except ValueError:
            pass
        suffix = ("  [" + "; ".join(tags) + "]") if tags else ""
        print(f"   {sev} {fid:<8} {agent:<10} {desc}{suffix}")

    # ④ own inbox
    inbox = YEYOU / "inbox"
    msgs = [p for p in inbox.glob("*.md")] if inbox.exists() else []
    note = " (PROME/Will mute or scope notes — fold into MEMORY)" if msgs else ""
    print(f"\n④ YEYOU INBOX  {len(msgs)} message(s){note}")
    for p in msgs[:10]:
        print(f"   • {p.name}")

    print("\nDone. Read-only — no state written. Review the queue, then run the W1–W8 closeout.")


if __name__ == "__main__":
    main()
