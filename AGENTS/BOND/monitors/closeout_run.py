#!/usr/bin/env python3
"""closeout_run.py -- BOND's closeout RUNNER: executes every MECHANICAL closeout
step, prints RAN / FAILED / NOT-APPLICABLE per step with its rc, appends one row
to registry/CLOSEOUT_LOG.tsv, and then NAMES the judgement steps it cannot verify.

Built 2026-09-29 (Will: "we should update our close out protocol") from the fleet
survey: HANS scripts/closeout_check.py (RAN/FAILED per step -- an omitted step
otherwise looks like a shorter checklist), DAEDALUS daedalus_gate.py (one log row
per run), VIOLET scripts/writeback_order_check.py (handoff surfaces may not lag
STATUS; dirty file = now, clean file = last commit time), TERRY ledger_sweep
check I (advisory inbox re-scan, never blocking), PROME CLOSEOUT.md (the tier is
passed explicitly; omitting it means "not enforced", and the runner says so).

  THIS SCRIPT DOES NOT CERTIFY THE CLOSEOUT. It certifies that the mechanical
  steps EXECUTED and what they returned. Whether STATUS says something true is a
  judgement step and is listed as UNVERIFIED BY DESIGN.

Exit: 0 = every mechanical step RAN and passed (NOT-APPLICABLE steps state why)
      1 = a step FAILED or errored (LOOK; never "closeout invalid" by itself)
  --verify: C12.3 — prints FREEZE MATCH (tree digest unchanged since the last run) or FREEZE MOVED.
  Working directory: AGENTS/BOND/ (the commit and push steps run from the repo root).

Usage:
  python3 monitors/closeout_run.py --tier standard
  python3 monitors/closeout_run.py --tier standard --superseded 14/35 15/35 --memory-slug <name>
  python3 monitors/closeout_run.py --selftest
"""
from __future__ import annotations
import argparse, datetime as dt, subprocess, sys, time
from pathlib import Path

BOND = Path(__file__).resolve().parent.parent
REPO = BOND.parent.parent
LOG = BOND / "registry" / "CLOSEOUT_LOG.tsv"
TIERS = ("bounce", "light", "standard", "heavy", "addendum")

# handoff surfaces that another reader consumes INSTEAD of STATUS -> may not lag it
TRACKED = {
    "NEXUS_BRIEF.md": "NEXUS reads this in place of STATUS (Amendment 10 ordering)",
    "SCRATCH.md": "my own next boot reads this as 'where are we'",
    "TRADE.md": "TERRY/PROME read posture here; it inverted vs STATUS for 20 days (9/9->9/29)",
}
JUDGEMENT = [
    "STATUS.md write-back is TRUE (dashboard · matrix re-summed · gates · bottom line)",
    "SCRATCH.md carries a STATE AT WRITING block and a stated no-op per surface",
    "THESIS/CHANGELOG written back for any thesis-level change (and the bond-state token moved WITH the prose)",
    "CATALYSTS pruned/added and the STATUS twin has the same event SET",
    "NEXUS_BRIEF.md re-pin REWRITTEN (not appended) and folded LAST",
    "RECEIPT.md overwritten if signals or a tasked deliverable were processed",
    "Promotion scan done (auto-memory vs local MEMORY)",
]


def sh(cmd, cwd=REPO, timeout=600):
    try:
        p = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, timeout=timeout)
        return p.returncode, (p.stdout + p.stderr).strip()
    except FileNotFoundError as e:
        return None, f"tool not found: {e}"
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT"


# ---------------- handoff ordering (pure predicate + git-backed vintage) ------
def lags(status_v: float, surface_v: float) -> bool:
    """True iff the surface is OLDER than STATUS. Equal = fine (same commit)."""
    return surface_v < status_v


def vintage(rel: str) -> float:
    """dirty in working tree -> now ; clean -> last commit time ; untracked/new -> now."""
    rc, out = sh(["git", "status", "--porcelain", "--", f"AGENTS/BOND/{rel}"])
    if out.strip():
        return time.time()
    rc, ts = sh(["git", "log", "-1", "--format=%ct", "--", f"AGENTS/BOND/{rel}"])
    try:
        return float(ts.strip().splitlines()[-1])
    except Exception:                                    # noqa: BLE001
        return 0.0


def check_ordering() -> tuple[str, str]:
    sv = vintage("STATUS.md")
    bad = []
    for rel, why in TRACKED.items():
        v = vintage(rel)
        if lags(sv, v):
            age = (sv - v) / 3600
            bad.append(f"{rel} lags STATUS by {age:.1f}h ({why})")
    if bad:
        return "FAILED", "; ".join(bad)
    return "RAN", f"STATUS + {len(TRACKED)} handoff surfaces in order (vintage, not content)"


def tree_digest() -> str:
    """sha1 over BOND's working-tree state (status + unstaged + staged diffs). Same digest = nothing moved."""
    import hashlib
    h = hashlib.sha1()
    # the runner's own log is excluded: it is appended by every run and would make each --verify read MOVED
    ex = ":(exclude)AGENTS/BOND/registry/CLOSEOUT_LOG.tsv"
    for cmd in (["git", "status", "--porcelain", "--", "AGENTS/BOND", ex],
                ["git", "diff", "--", "AGENTS/BOND", ex],
                ["git", "diff", "--cached", "--", "AGENTS/BOND", ex]):
        rc, out = sh(cmd)
        h.update((out or "").encode("utf-8", "replace"))
    rc, head = sh(["git", "rev-parse", "HEAD"])
    h.update((head or "").encode())
    return h.hexdigest()[:12]


def verify() -> int:
    if not LOG.exists():
        print("FREEZE UNKNOWN: no CLOSEOUT_LOG.tsv yet — run the runner first"); return 1
    rows = [l for l in LOG.read_text(encoding="utf-8").splitlines()[1:] if l.strip()]
    if not rows:
        print("FREEZE UNKNOWN: log empty — run the runner first"); return 1
    last = rows[-1].split("\t")
    logged = last[5] if len(last) > 5 else ""
    now = tree_digest()
    if logged and logged == now:
        print(f"FREEZE MATCH: tree digest {now} unchanged since the last run ({last[0]}, tier={last[1]}, {last[3]}) — commit now")
        return 0
    print(f"FREEZE MOVED: tree digest now {now}, last run logged {logged or 'none'} ({last[0] if last else '?'}) — restart C12 at 1")
    return 1


def inbox_scan() -> str:
    items = []
    for pat in ("inbox/*.md", "inbox/WALTER/*.md"):
        for p in sorted((BOND).glob(pat)):
            rc, ts = sh(["git", "log", "-1", "--format=%ct", "--", str(p.relative_to(REPO))])
            try:
                age = (time.time() - float(ts.strip().splitlines()[-1])) / 3600
                items.append(f"{p.relative_to(BOND)} ({age:.0f}h since commit)")
            except Exception:                            # noqa: BLE001
                items.append(f"{p.relative_to(BOND)} (uncommitted)")
    return "; ".join(items) if items else "inbox lanes empty"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=TIERS)
    ap.add_argument("--superseded", nargs=2, action="append", metavar=("OLD", "NEW"),
                    help="a figure this session superseded; runs consumer_check (cross + --self)")
    ap.add_argument("--memory-slug", action="append", help="auto-memory slug written this session")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verify", action="store_true", help="C12.3: is the tree unchanged since the last run?")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.verify:
        return verify()

    tier = a.tier or "standard"
    now = dt.datetime.now()
    print("=" * 74)
    print(f"  BOND CLOSEOUT RUNNER · {now:%Y-%m-%d %H:%M} local · tier={tier}"
          + ("" if a.tier else "  ⚠️ --tier OMITTED: treated as standard, NOT enforced"))
    print("=" * 74)
    rows = []

    def step(name, outcome, detail):
        rows.append((name, outcome, detail))
        mark = {"RAN": "✅", "FAILED": "🔴", "NOT-APPLICABLE": "▫️"}[outcome]
        print(f"  {mark} {outcome:<14} {name}")
        if detail:
            for ln in str(detail).splitlines()[-6:]:
                print(f"        {ln[:160]}")

    # 1. content pass (kb_lint · numeric drift · assertions · mirror sync)
    rc, out = sh([sys.executable, "monitors/closeout_check.py"], cwd=BOND, timeout=900)
    tail = "\n".join(out.splitlines()[-3:])
    step("closeout_check (0/4 lint · 1/4 numeric · 2/4 assertions · 3/4 mirror)",
         "RAN" if rc == 0 else "FAILED", f"rc={rc}\n{tail}")

    # 2. handoff ordering
    o, d = check_ordering()
    if tier == "bounce":
        step("handoff ordering (STATUS vs NEXUS_BRIEF/SCRATCH/TRADE)", "NOT-APPLICABLE", "bounce tier: STATUS not rewritten")
    else:
        step("handoff ordering (STATUS vs NEXUS_BRIEF/SCRATCH/TRADE)", o, d)

    # 3. root 1b orphan (advisory)
    rc, out = sh(["bash", "scripts/orphan_check.sh", "BOND"])
    yours = [l for l in out.splitlines() if "likely YOURS" in l]
    step("root 1b orphan_check", "RAN" if rc is not None else "FAILED",
         f"[likely YOURS]={len(yours)} (commit them, carve-out ①)" + ("\n" + "\n".join(yours) if yours else ""))

    # 4. root 1c consumer check
    if a.superseded:
        fails = []
        for old, new in a.superseded:
            rc1, o1 = sh([sys.executable, "scripts/consumer_check.py", "--agent", "BOND", "--old", old, "--new", new])
            rc2, o2 = sh([sys.executable, "scripts/consumer_check.py", "--agent", "BOND", "--self", "--old", old, "--new", new])
            if rc1 not in (0, 1) or rc2 not in (0, 1):
                fails.append(f"{old}->{new}: rc {rc1}/{rc2}")
            print(f"        consumer_check {old}->{new}: cross rc={rc1} · self rc={rc2} (🔴 STALE owners get a packet; fix own by pattern)")
        step("root 1c consumer_check (cross + --self)", "FAILED" if fails else "RAN", "; ".join(fails))
    else:
        step("root 1c consumer_check (cross + --self)", "NOT-APPLICABLE",
             "no superseded figure DECLARED (--superseded OLD NEW). ⚠️ This is a self-declaration: if a threshold, split, "
             "score or band changed this session, re-run with it.")

    # 5. root 1c-bis ledger nudge (advisory)
    rc, out = sh([sys.executable, "scripts/ledger_staleness.py", "--nudge", "BOND"])
    step("root 1c-bis ledger_staleness --nudge", "RAN" if rc is not None else "FAILED",
         out.splitlines()[-1] if out else "")

    # 6. root 1d memory index
    if a.memory_slug:
        cmd = [sys.executable, "scripts/memory_index_check.py", "--strict"]
        for s in a.memory_slug:
            cmd += ["--slug", s]
        rc1, o1 = sh(cmd)
        rc2, o2 = sh(["bash", "scripts/check_memory_length.sh"])
        step("root 1d memory_index_check + check_memory_length", "RAN" if rc1 == 0 and rc2 == 0 else "FAILED",
             f"index rc={rc1} · length rc={rc2} (rc=1 approaching, 2 over: flag PROME, never compact)")
    else:
        step("root 1d memory_index_check", "NOT-APPLICABLE", "no auto-memory slug declared (--memory-slug)")

    # 7. root 1e claim check
    paths = ["PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md",
             "AGENTS/BOND/docket/CATALYSTS.tsv", "AGENTS/BOND/STATUS.md"]
    rc, out = sh([sys.executable, "scripts/claim_check.py", "--check", "weekday"] + paths)
    step("root 1e claim_check --check weekday", "RAN" if rc == 0 else "FAILED", out.splitlines()[-1] if out else "")

    # 8. read cap
    rc, out = sh([sys.executable, "scripts/read_cap_check.py", "--agent", "BOND"])
    step("read_cap_check --agent BOND", "RAN" if rc == 0 else "FAILED",
         [l for l in out.splitlines() if "READ-CAP" in l][-1:] and [l for l in out.splitlines() if "READ-CAP" in l][-1] or "")

    # 9. inbox re-scan (advisory, never blocks)
    step("inbox re-scan (advisory: what landed since boot)", "RAN", inbox_scan())

    failed = [r for r in rows if r[1] == "FAILED"]
    print("\n" + "-" * 74)
    print("  JUDGEMENT STEPS — NOT VERIFIED BY THIS RUNNER (by design; name each outcome in SCRATCH):")
    for j in JUDGEMENT:
        print(f"   · {j}")
    print("-" * 74)
    rc, head = sh(["git", "rev-parse", "--short", "HEAD"])
    LOG.parent.mkdir(exist_ok=True)
    if not LOG.exists():
        LOG.write_text("timestamp\ttier\thead\toverall\tsteps\tdigest\n", encoding="utf-8")
    with LOG.open("a", encoding="utf-8") as f:
        f.write("\t".join([now.strftime("%Y-%m-%dT%H:%M"), tier, head.strip(),
                           "FAILED" if failed else "RAN",
                           " | ".join(f"{n}={o}" for n, o, _ in rows), tree_digest()]) + "\n")
    print(f"  {'🔴 ' + str(len(failed)) + ' step(s) FAILED — rc=1, LOOK' if failed else '✅ every mechanical step RAN and passed'}"
          f" · logged to {LOG.relative_to(BOND)} · then: commit (pathspec) → safe-push (read its receipt line)")
    print("=" * 74)
    return 1 if failed else 0


FIXTURES = [
    ("surface older than STATUS lags", 100.0, 50.0, True),
    ("surface same commit as STATUS does not lag", 100.0, 100.0, False),
    ("surface dirty (now) never lags", 100.0, 1e12, False),
    ("REAL 2026-09-29 class: NEXUS_BRIEF 5 days behind STATUS", 1_759_100_000.0, 1_758_700_000.0, True),
]


def selftest() -> int:
    bad = 0
    print(f"  closeout_run SELFTEST — {len(FIXTURES)} ordering fixtures")
    for name, sv, v, exp in FIXTURES:
        ok = lags(sv, v) == exp
        bad += 0 if ok else 1
        print(f"  {'✅' if ok else '❌'} {name}")
    print(f"  {'ALL PASS' if not bad else str(bad) + ' FAILURE(S)'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
