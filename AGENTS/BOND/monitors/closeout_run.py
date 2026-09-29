#!/usr/bin/env python3
"""closeout_run.py -- BOND's closeout RUNNER (C12): executes every MECHANICAL step,
prints RAN / FAILED / FINDINGS / NOT-APPLICABLE per step, records a working-tree
digest at START and END, appends one row to registry/CLOSEOUT_LOG.tsv, and names
the judgement steps it cannot verify. `--verify` (C12.3) says whether the tree is
unchanged since the last PASSING run.

v1 2026-09-29 (fleet survey: HANS per-step RAN/FAILED, DAEDALUS one row per run,
VIOLET handoff ordering, PROME explicit tier). v2 the same evening after a reviewer
reproduced four defects in an isolated repo, none covered by v1's selftest:
  1. the freeze digest missed untracked-file CONTENT (git status shows `??` either
     way), missed outgoing packets outside AGENTS/BOND/, and was taken only at the
     END of the run, so an edit made during the checks passed --verify;
  2. --verify said "commit now" after a FAILED run; consumer_check findings were
     discarded (it exits 0 unless --strict); crashed advisory tools (orphan_check
     exits 0 unconditionally) were labelled RAN;
  3. "commit optional" in the tier table contradicted root CLAUDE.md ("commit
     locally at session end"); fixed in CLOSEOUT.md;
  4. the handoff-ordering check forced a TRADE.md edit after any STATUS edit.
     TRADE is now covered by the bond-state TOKEN (mirror_check), not by vintage;
     NEXUS_BRIEF may be declared a stated no-op with a reason (--noop), logged.

v3 (same evening, CATO follow-up review AGENTS/CATO/runs/2026-09-29_1807_bond-closeout-review.md):
  5. a cross-agent --consumer-ack also cleared a stale finding on BOND's OWN files
     (--self scan). Now: self findings are never acknowledgeable; fix the file and re-run;
  6. affected paths and the acknowledgement text were not in the run evidence. Now: every
     run appends its full per-step transcript to registry/closeout_runs/YYYY-MM-DD.transcript.md, the
     consumer/claim context lines are printed, and ack/disposition text is a log column;
  7. a failed git read still produced a digest. Now: tree_digest() returns None on any
     non-zero git rc; the run's freeze step FAILS and --verify REFUSES on UNKNOWN;
  8. a weekday-check flag was a hard no-commit even when it was a correctly labelled quote
     (root: a flag is a prompt to LOOK, never a find-replace). Now: FINDINGS until
     --claim-ack "<file:line — why it is a quote>" records the disposition.

  THIS SCRIPT DOES NOT CERTIFY THE CLOSEOUT. It certifies that the mechanical
  steps EXECUTED, what they returned, and that nothing moved between the run and
  the commit. Whether STATUS says something true is judgement, listed as such.

Exit: 0 = every mechanical step RAN (or NOT-APPLICABLE with a stated reason)
      1 = a step FAILED, FINDINGS were not acknowledged, or the tree moved during the run
Working directory: AGENTS/BOND/. Commit and push run from the repo root.
"""
from __future__ import annotations
import argparse, datetime as dt, hashlib, os, subprocess, sys, tempfile, time
from pathlib import Path

BOND = Path(__file__).resolve().parent.parent
REPO = BOND.parent.parent
LOG = BOND / "registry" / "CLOSEOUT_LOG.tsv"
TIERS = ("bounce", "light", "standard", "heavy", "addendum")
LOG_EXCLUDE = ":(exclude)AGENTS/BOND/registry/CLOSEOUT_LOG.tsv"
RUNS_EXCLUDE = ":(exclude)AGENTS/BOND/registry/closeout_runs"
# what the freeze covers: this desk's directory + every self-authored outgoing packet
DIGEST_PATHS = ["AGENTS/BOND", "PROME/inbox/*from-BOND*", "AGENTS/*/inbox/*from-BOND*",
                "AGENTS/*/inbox/*/*from-BOND*", "AGENTS/SIGNALS.md"]
# handoff surfaces another reader consumes INSTEAD of STATUS. TRADE.md is NOT here:
# its sync is the bond-state token (mirror_check), and vintage forced pointless edits.
TRACKED = {
    "NEXUS_BRIEF.md": "NEXUS reads this in place of STATUS (Amendment 10 ordering)",
    "SCRATCH.md": "my own next boot reads this as 'where are we'",
}
NOOP_ALLOWED = {"NEXUS_BRIEF.md"}          # SCRATCH is written at every ending; no no-op
JUDGEMENT = [
    "STATUS.md write-back is TRUE (dashboard · matrix re-summed · gates · bottom line)",
    "SCRATCH.md carries a STATE AT WRITING block and a stated no-op per surface",
    "THESIS/CHANGELOG written for any thesis-level change; the bond-state token moved WITH the prose",
    "CATALYSTS pruned/added and the STATUS twin has the same event SET",
    "NEXUS_BRIEF.md re-pin REWRITTEN (not appended) and folded LAST — or a --noop reason that is true",
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


# ---------------- pure classifiers (selftested) --------------------------------
def classify(rc, out, mode: str) -> str:
    """mode 'strict': rc 0 = RAN, else FAILED.
       mode 'advisory': the tool reports, never blocks; RAN iff it actually ran (rc 0/1,
       produced output, no traceback). A crash is FAILED, never RAN."""
    if rc is None:
        return "FAILED"
    text = out or ""
    if "Traceback" in text or "Error:" in text and "error" in text.lower()[:200]:
        return "FAILED"
    if mode == "strict":
        return "RAN" if rc == 0 else "FAILED"
    if rc in (0, 1) and text.strip():
        return "RAN"
    return "FAILED"


def classify_consumer(rc, out, acked: bool, form: str = "cross") -> str:
    """consumer_check run with --strict: rc 1 = at least one 🔴 STALE consumer.
       form 'cross': other desks' files — FINDINGS until the operator acknowledges that packets went out.
       form 'self' : BOND's OWN files — never acknowledgeable; fix the file and re-run (CATO BC2)."""
    if rc is None or rc not in (0, 1) or "Traceback" in (out or ""):
        return "FAILED"
    if rc == 1:
        if form == "self":
            return "FINDINGS"
        return "RAN" if acked else "FINDINGS"
    return "RAN"


def classify_claim(rc, out, acked: bool) -> str:
    """claim_check --check weekday: rc 1 = a weekday asserted beside a date that is not that weekday.
       A flag is a prompt to LOOK (root 1e): FINDINGS until --claim-ack records why each hit is a
       correctly labelled quote, or the line is fixed and the run repeated."""
    if rc is None or rc not in (0, 1) or "Traceback" in (out or ""):
        return "FAILED"
    if rc == 1:
        return "RAN" if acked else "FINDINGS"
    return "RAN"


def context_lines(out: str, marker: str = "🔴", after: int = 3) -> list:
    """the marker line plus the next `after` lines — consumer_check prints the path and source text
       on the lines FOLLOWING the 🔴 line (CATO BC2: 'the path is absent from stdout and the log')."""
    lines = (out or "").splitlines(); keep = []
    for i, l in enumerate(lines):
        if marker in l:
            keep += lines[i:i + 1 + after]
    return keep


def verify_decision(last_row: list, now_digest: str) -> tuple[bool, str]:
    """last_row = a CLOSEOUT_LOG row split on tabs (timestamp tier head overall steps digest)."""
    if now_digest is None:
        return False, "FREEZE UNKNOWN: a required git read failed — error text is not a snapshot; fix git, restart C12 at 1"
    if not last_row or len(last_row) < 6:
        return False, "FREEZE UNKNOWN: no complete run logged — run the runner first"
    ts, tier, head, overall, _steps, digest = last_row[:6]
    if not digest or digest == "UNKNOWN":
        return False, f"FREEZE REFUSED: last run ({ts}) logged no usable digest — restart C12 at 1"
    if overall != "RAN":
        return False, f"FREEZE REFUSED: last run ({ts}, tier={tier}) was {overall} — fix, then restart C12 at 1"
    if digest != now_digest:
        return False, f"FREEZE MOVED: tree digest now {now_digest}, last passing run logged {digest} ({ts}) — restart C12 at 1"
    return True, f"FREEZE MATCH: tree digest {now_digest} unchanged since the last passing run ({ts}, tier={tier}) — commit now"


def lags(status_v: float, surface_v: float) -> bool:
    return surface_v < status_v


# ---------------- git-backed pieces ---------------------------------------------
def tree_digest(repo: Path = REPO, paths=None) -> str:
    """sha1 over: porcelain status (all untracked files listed), unstaged + staged diffs, HEAD,
       and the CONTENT of every untracked file in scope. Same digest = nothing moved."""
    paths = list(paths or DIGEST_PATHS)
    h = hashlib.sha1()
    rc, status = sh(["git", "status", "--porcelain", "--untracked-files=all", "--", *paths, LOG_EXCLUDE, RUNS_EXCLUDE], cwd=repo)
    if rc != 0:
        return None                                   # a failed git read is not a snapshot (CATO BC1 residual)
    h.update((status or "").encode("utf-8", "replace"))
    for cmd in (["git", "diff", "--", *paths, LOG_EXCLUDE, RUNS_EXCLUDE], ["git", "diff", "--cached", "--", *paths, LOG_EXCLUDE, RUNS_EXCLUDE]):
        rc, out = sh(cmd, cwd=repo)
        if rc != 0:
            return None
        h.update((out or "").encode("utf-8", "replace"))
    for line in (status or "").splitlines():
        if line.startswith("??"):
            p = repo / line[3:].strip().strip('"')
            if p.is_file():
                h.update(p.read_bytes())
    rc, head = sh(["git", "rev-parse", "HEAD"], cwd=repo)
    if rc != 0:
        return None
    h.update((head or "").encode())
    return h.hexdigest()[:12]


def vintage(rel: str) -> float:
    rc, out = sh(["git", "status", "--porcelain", "--", f"AGENTS/BOND/{rel}"])
    if out.strip():
        return time.time()
    rc, ts = sh(["git", "log", "-1", "--format=%ct", "--", f"AGENTS/BOND/{rel}"])
    try:
        return float(ts.strip().splitlines()[-1])
    except Exception:                                    # noqa: BLE001
        return 0.0


def check_ordering(noops: dict) -> tuple[str, str]:
    sv = vintage("STATUS.md")
    bad, notes = [], []
    for rel, why in TRACKED.items():
        if rel in noops:
            notes.append(f"{rel}: stated no-op — {noops[rel]}")
            continue
        v = vintage(rel)
        if lags(sv, v):
            bad.append(f"{rel} lags STATUS by {(sv - v) / 3600:.1f}h ({why}); write it, or declare --noop {rel} \"reason\"")
    if bad:
        return "FAILED", "; ".join(bad + notes)
    return "RAN", "; ".join([f"STATUS + {len(TRACKED)} handoff surfaces in order (vintage, not content)"] + notes)


def inbox_scan() -> str:
    items = []
    for pat in ("inbox/*.md", "inbox/WALTER/*.md"):
        for p in sorted(BOND.glob(pat)):
            rc, ts = sh(["git", "log", "-1", "--format=%ct", "--", str(p.relative_to(REPO))])
            try:
                items.append(f"{p.relative_to(BOND)} ({(time.time() - float(ts.strip().splitlines()[-1])) / 3600:.0f}h since commit)")
            except Exception:                            # noqa: BLE001
                items.append(f"{p.relative_to(BOND)} (uncommitted)")
    return "; ".join(items) if items else "inbox lanes empty"


def verify() -> int:
    rows = [l for l in LOG.read_text(encoding="utf-8").splitlines()[1:] if l.strip()] if LOG.exists() else []
    ok, msg = verify_decision(rows[-1].split("\t") if rows else [], tree_digest())
    print(msg)
    return 0 if ok else 1


# ---------------- main -------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", choices=TIERS)
    ap.add_argument("--superseded", nargs=2, action="append", metavar=("OLD", "NEW"))
    ap.add_argument("--consumer-ack", metavar="NOTE", help="packets to every 🔴 STALE owner were sent: NOTE names them")
    ap.add_argument("--claim-ack", metavar="NOTE", help="weekday-check hits are correctly labelled quotes: NOTE names file:line and why")
    ap.add_argument("--memory-slug", action="append")
    ap.add_argument("--noop", nargs=2, action="append", metavar=("SURFACE", "REASON"),
                    help="declare a handoff surface unchanged on purpose (NEXUS_BRIEF.md only)")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--verify", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.verify:
        return verify()

    tier = a.tier or "standard"
    noops = {}
    for surf, reason in (a.noop or []):
        if surf not in NOOP_ALLOWED:
            print(f"  ⛔ --noop {surf} not allowed (only {sorted(NOOP_ALLOWED)}); SCRATCH is written at every ending")
            return 1
        noops[surf] = reason
    d0 = tree_digest()
    now = dt.datetime.now()
    RUNS = BOND / "registry" / "closeout_runs"
    RUNS.mkdir(parents=True, exist_ok=True)
    transcript = RUNS / f"{now:%Y-%m-%d}.transcript.md"   # not .log: the repo gitignores *.log
    tlog = [f"===== RUN {now:%Y-%m-%dT%H:%M} tier={tier} tree_start={d0 or 'UNKNOWN'} =====",
            f"args: superseded={a.superseded} consumer_ack={a.consumer_ack!r} claim_ack={a.claim_ack!r} memory_slug={a.memory_slug} noop={a.noop}"]
    print("=" * 74)
    print(f"  BOND CLOSEOUT RUNNER · {now:%Y-%m-%d %H:%M} local · tier={tier} · tree {d0 or 'UNKNOWN'}"
          + ("" if a.tier else "  ⚠️ --tier OMITTED: treated as standard, NOT enforced"))
    print("=" * 74)
    rows = []

    def step(name, outcome, detail, full=None):
        rows.append((name, outcome, detail))
        mark = {"RAN": "✅", "FAILED": "🔴", "FINDINGS": "🟠", "NOT-APPLICABLE": "▫️"}[outcome]
        print(f"  {mark} {outcome:<14} {name}")
        for ln in str(detail or "").splitlines()[-12:]:
            print(f"        {ln[:170]}")
        tlog.append(f"--- {outcome} · {name}")
        tlog.append(str(detail or ""))
        if full:
            tlog.append("[full tool output]")
            tlog.append(str(full))

    rc, out = sh([sys.executable, "monitors/closeout_check.py"], cwd=BOND, timeout=900)
    step("closeout_check (0/4 lint · 1/4 numeric · 2/4 assertions · 3/4 mirror)", classify(rc, out, "strict"),
         f"rc={rc}\n" + "\n".join(out.splitlines()[-3:]), full=out)

    if tier == "bounce":
        step("handoff ordering (STATUS vs NEXUS_BRIEF/SCRATCH)", "NOT-APPLICABLE", "bounce tier: STATUS not rewritten")
    else:
        o, d = check_ordering(noops)
        step("handoff ordering (STATUS vs NEXUS_BRIEF/SCRATCH)", o, d)

    rc, out = sh(["bash", "scripts/orphan_check.sh", "BOND"])
    yours = [l for l in out.splitlines() if "likely YOURS" in l]
    step("root 1b orphan_check", classify(rc, out, "advisory"),
         f"rc={rc} · [likely YOURS]={len(yours)} (commit them, carve-out ①)" + ("\n" + "\n".join(yours) if yours else ""), full=out)

    if a.superseded:
        worst, detail, fulls = "RAN", [], []
        rank = {"RAN": 0, "FINDINGS": 1, "FAILED": 2}
        for old, new in a.superseded:
            for form, extra in (("cross", []), ("self", ["--self"])):
                rc, out = sh([sys.executable, "scripts/consumer_check.py", "--agent", "BOND", "--strict", *extra, "--old", old, "--new", new])
                oc = classify_consumer(rc, out, bool(a.consumer_ack), form)
                ctx = context_lines(out, "🔴", 3)
                detail.append(f"{form} {old}->{new}: rc={rc} → {oc}" + (f" · {sum(1 for l in ctx if '🔴' in l)} 🔴 finding(s), paths below" if ctx else ""))
                detail += ["   " + l[:170] for l in ctx[:16]]
                if form == "self" and oc == "FINDINGS":
                    detail.append("   ⛔ SELF findings are never acknowledgeable: fix the file(s) above, then restart C12 at 1")
                fulls.append(f"[{form} {old}->{new} rc={rc}]\n{out}")
                worst = oc if rank[oc] > rank[worst] else worst
        if a.consumer_ack:
            detail.append(f"CROSS ACK recorded: {a.consumer_ack}")
        step("root 1c consumer_check --strict (cross + --self)", worst, "\n".join(detail), full="\n".join(fulls))
    else:
        step("root 1c consumer_check (cross + --self)", "NOT-APPLICABLE",
             "no superseded figure DECLARED (--superseded OLD NEW). Self-declaration: a changed threshold, score, split or band must be declared.")

    rc, out = sh([sys.executable, "scripts/ledger_staleness.py", "--nudge", "BOND"])
    step("root 1c-bis ledger_staleness --nudge (advisory)", classify(rc, out, "advisory"), f"rc={rc} · " + (out.splitlines()[-1] if out else ""))

    if a.memory_slug:
        cmd = [sys.executable, "scripts/memory_index_check.py", "--strict"]
        for s in a.memory_slug:
            cmd += ["--slug", s]
        rc1, o1 = sh(cmd); rc2, o2 = sh(["bash", "scripts/check_memory_length.sh"])
        oc = "RAN" if classify(rc1, o1, "strict") == "RAN" and classify(rc2, o2, "strict") == "RAN" else "FAILED"
        step("root 1d memory_index_check + check_memory_length", oc, f"index rc={rc1} · length rc={rc2} (1 approaching, 2 over → flag PROME)")
    else:
        step("root 1d memory_index_check", "NOT-APPLICABLE", "no auto-memory slug declared (--memory-slug)")

    paths = ["PROME/DOCKET.tsv", "PROME/GATES.tsv", "PROME/WILL_QUEUE.md", "AGENTS/BOND/docket/CATALYSTS.tsv", "AGENTS/BOND/STATUS.md"]
    rc, out = sh([sys.executable, "scripts/claim_check.py", "--check", "weekday"] + paths)
    oc = classify_claim(rc, out, bool(a.claim_ack))
    hits = [l for l in out.splitlines() if l.strip() and "CLAIM-CHECK" not in l][-12:] if rc == 1 else []
    cd = f"rc={rc} · " + (out.splitlines()[-1] if out else "")
    if hits:
        cd += "\n" + "\n".join("   " + h[:170] for h in hits)
        cd += "\n   a flag is a prompt to LOOK: fix the line, or --claim-ack \"<file:line — why it is a correctly labelled quote>\""
    if a.claim_ack:
        cd += f"\nCLAIM ACK recorded: {a.claim_ack}"
    step("root 1e claim_check --check weekday", oc, cd, full=out)

    rc, out = sh([sys.executable, "scripts/read_cap_check.py", "--agent", "BOND"])
    res = [l for l in out.splitlines() if "READ-CAP-RESULT" in l]
    step("read_cap_check --agent BOND", classify(rc, out, "strict"), f"rc={rc} · " + (res[-1] if res else "(no result line)"))

    step("inbox re-scan (advisory: what landed since boot)", "RAN", inbox_scan())

    d1 = tree_digest()
    if d0 is None or d1 is None:
        step("freeze integrity (tree digest start == end)", "FAILED", f"start {d0 or 'UNKNOWN'} · end {d1 or 'UNKNOWN'} — a git read failed; no snapshot, no verify")
    else:
        step("freeze integrity (tree digest start == end)", "RAN" if d0 == d1 else "FAILED",
             f"start {d0} · end {d1}" + ("" if d0 == d1 else " — the tree MOVED during the checks; restart C12 at 1"))

    blocking = [r for r in rows if r[1] in ("FAILED", "FINDINGS")]
    print("\n" + "-" * 74)
    print("  JUDGEMENT STEPS — NOT VERIFIED BY THIS RUNNER (by design; name each outcome in SCRATCH):")
    for j in JUDGEMENT:
        print(f"   · {j}")
    print("-" * 74)
    rc, head = sh(["git", "rev-parse", "--short", "HEAD"])
    LOG.parent.mkdir(exist_ok=True)
    if not LOG.exists():
        LOG.write_text("timestamp\ttier\thead\toverall\tsteps\tdigest\tnoops\tacks\ttranscript\n", encoding="utf-8")
    overall = "FAILED" if blocking else "RAN"
    acks = "; ".join(x for x in [f"consumer_ack: {a.consumer_ack}" if a.consumer_ack else "",
                                 f"claim_ack: {a.claim_ack}" if a.claim_ack else ""] if x)
    with LOG.open("a", encoding="utf-8") as f:
        f.write("\t".join([now.strftime("%Y-%m-%dT%H:%M"), tier, head.strip(), overall,
                           " | ".join(f"{n}={o}" for n, o, _ in rows), d1 or "UNKNOWN",
                           "; ".join(f"{k}: {v}" for k, v in noops.items()), acks,
                           str(transcript.relative_to(BOND))]) + "\n")
    tlog.append(f"===== END overall={overall} tree_end={d1 or 'UNKNOWN'} =====\n")
    with transcript.open("a", encoding="utf-8") as f:
        f.write("\n".join(tlog) + "\n")
    print(f"  {'🔴 ' + str(len(blocking)) + ' blocking step(s) — rc=1, no commit' if blocking else '✅ every mechanical step RAN'}"
          f" · row → {LOG.relative_to(BOND)} · transcript → {transcript.relative_to(BOND)} · next: `--verify` → commit by pathspec (repo root) → safe-push")
    print("=" * 74)
    return 1 if blocking else 0


# ---------------- selftest ---------------------------------------------------------
def _tmp_repo_digest_test() -> list:
    """Isolated repo: the digest must change on (a) untracked-file CONTENT, (b) an outgoing
       packet outside AGENTS/BOND, (c) a tracked-file edit; and must NOT change on a log append."""
    out = []
    with tempfile.TemporaryDirectory() as td:
        repo = Path(td)
        env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
        def g(*args):
            return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, env=env)
        g("init", "-q"); (repo / "AGENTS/BOND/registry").mkdir(parents=True); (repo / "PROME/inbox").mkdir(parents=True)
        (repo / "AGENTS/BOND/STATUS.md").write_text("s\n"); (repo / "AGENTS/BOND/registry/CLOSEOUT_LOG.tsv").write_text("h\n")
        g("add", "-A"); g("commit", "-qm", "init")
        base = tree_digest(repo)
        (repo / "AGENTS/BOND/new_untracked.md").write_text("v1\n"); d_a1 = tree_digest(repo)
        (repo / "AGENTS/BOND/new_untracked.md").write_text("v2\n"); d_a2 = tree_digest(repo)
        out.append(("REAL v1 defect: untracked-file CONTENT edit changes the digest", d_a1 != d_a2 and d_a1 != base))
        (repo / "PROME/inbox/2026-09-29_from-BOND_x.md").write_text("p1\n"); d_b1 = tree_digest(repo)
        (repo / "PROME/inbox/2026-09-29_from-BOND_x.md").write_text("p2\n"); d_b2 = tree_digest(repo)
        out.append(("REAL v1 defect: outgoing packet outside AGENTS/BOND is in the freeze", d_b1 != d_a2 and d_b2 != d_b1))
        (repo / "AGENTS/BOND/STATUS.md").write_text("s2\n"); d_c = tree_digest(repo)
        out.append(("tracked-file edit changes the digest", d_c != d_b2))
        with (repo / "AGENTS/BOND/registry/CLOSEOUT_LOG.tsv").open("a") as f:
            f.write("row\n")
        out.append(("appending the runner's own log does NOT change the digest", tree_digest(repo) == d_c))
        (repo / "AGENTS/BOND/registry/closeout_runs").mkdir(); (repo / "AGENTS/BOND/registry/closeout_runs/x.transcript.md").write_text("t\n")
        out.append(("a new transcript file does NOT change the digest", tree_digest(repo) == d_c))
    with tempfile.TemporaryDirectory() as nd:
        out.append(("REAL CATO BC1 residual: a failed git read (a directory that is not a repo) yields None, not a digest", tree_digest(Path(nd)) is None))
    return out


FIXTURES = [
    ("classify: advisory tool crashed (rc None) → FAILED", classify(None, "", "advisory") == "FAILED"),
    ("classify: advisory tool traceback with rc 0 → FAILED (orphan_check exits 0 unconditionally)", classify(0, "Traceback (most recent call last)...", "advisory") == "FAILED"),
    ("classify: advisory tool rc 1 with output → RAN", classify(1, "nudge: behind", "advisory") == "RAN"),
    ("classify: advisory tool rc 0 but NO output → FAILED (did it run?)", classify(0, "", "advisory") == "FAILED"),
    ("classify: strict tool rc 1 → FAILED", classify(1, "x", "strict") == "FAILED"),
    ("consumer cross: rc 1 unacked → FINDINGS (blocking)", classify_consumer(1, "🔴 STALE", False, "cross") == "FINDINGS"),
    ("consumer cross: rc 1 acked → RAN", classify_consumer(1, "🔴 STALE", True, "cross") == "RAN"),
    ("consumer SELF: rc 1 with a CROSS ack → still FINDINGS (CATO BC2: ack must not clear own files)", classify_consumer(1, "🔴 STALE AGENTS/BOND/STATUS.md:42", True, "self") == "FINDINGS"),
    ("consumer SELF: rc 0 → RAN", classify_consumer(0, "", True, "self") == "RAN"),
    ("consumer: rc 2 → FAILED", classify_consumer(2, "", False) == "FAILED"),
    ("claim: rc 1 unacked → FINDINGS (a flag is a prompt to LOOK, not a hard block)", classify_claim(1, "flag", False) == "FINDINGS"),
    ("claim: rc 1 with documented disposition → RAN", classify_claim(1, "flag", True) == "RAN"),
    ("claim: crash → FAILED", classify_claim(None, "", True) == "FAILED"),
    ("context: path lines AFTER the 🔴 line are kept (CATO BC2)", context_lines("x\n🔴 STALE owner\n  AGENTS/X/STATUS.md:42\n  'text'\ny", "🔴", 2) == ["🔴 STALE owner", "  AGENTS/X/STATUS.md:42", "  'text'"]),
    ("verify: digest UNKNOWN (git read failed) → refuse", verify_decision(["t", "standard", "h", "RAN", "s", "abc"], None)[0] is False),
    ("verify: last run logged UNKNOWN digest → refuse", verify_decision(["t", "standard", "h", "RAN", "s", "UNKNOWN"], "abc")[0] is False),
    ("verify: REAL v1 defect — last run FAILED must not say 'commit now'", verify_decision(["t", "standard", "h", "FAILED", "s", "abc"], "abc")[0] is False),
    ("verify: last run RAN + same digest → commit", verify_decision(["t", "standard", "h", "RAN", "s", "abc"], "abc")[0] is True),
    ("verify: last run RAN + different digest → MOVED", verify_decision(["t", "standard", "h", "RAN", "s", "abc"], "abd")[0] is False),
    ("verify: no log → refuse", verify_decision([], "abc")[0] is False),
    ("ordering: older surface lags", lags(100.0, 50.0) is True),
    ("ordering: dirty surface (now) never lags", lags(100.0, 1e12) is False),
]


def selftest() -> int:
    bad = 0
    fx = list(FIXTURES) + _tmp_repo_digest_test()
    print(f"  closeout_run SELFTEST — {len(fx)} fixtures (pure classifiers + isolated-repo digest)")
    for name, ok in fx:
        print(f"  {'✅' if ok else '❌'} {name}")
        bad += 0 if ok else 1
    print(f"  {'ALL PASS' if not bad else str(bad) + ' FAILURE(S)'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
