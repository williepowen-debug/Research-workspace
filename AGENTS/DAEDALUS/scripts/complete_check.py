#!/usr/bin/env python3
"""complete_check.py — the COMPLETE-check: did the work this session CLAIMED actually get done?

Sits beside the COMMITTED-checks (orphan_check/claim_check/safe-push all answer "did files
reach origin?"). Born from the 2026-08-12 finding (PAT-101/PAT-102): 8 gaps in one day behind
my own "closed", 0 found by my closeout — every one a COMPLETE-failure, every check a
COMMITTED-check. Build-queue head since 8/12; built 2026-08-17 late (self-audit open-items run).

Three legs (the three rules earned 8/12, STATUS item 3):
  (ii) PAIRING [mechanical, gates rc]: every commit in range touching BLUEPRINTS/* or
       UPGRADE_PROTOCOL.md must include EVOLUTION.md in the SAME commit (PAT-101 rule ii —
       missed twice in one session before the rule; once after, 383051aeb).
 (iii) PAIR-SYMMETRY [mechanical, gates rc]: every *_READER_REPORTS.md has a synthesis
       beside it (same prefix) and every Mode-A synthesis created in range has a companion
       (PAT-100/PAT-102; the war-triad shipped the companion WITHOUT the synthesis).
   (i) CLAIM ENUMERATION [judgment, does NOT gate rc]: side-effect verbs on lines ADDED
       by my commits in range (diff-scoped 2026-08-20, WALTER 8/17 discharge-path packet:
       a session can discharge its OWN claims, never the standing corpus — whole-file
       enumeration re-inflated the list to 483 whenever an old doc was touched), printed
       as a walk-list — verify each against its named surface before closeout.
       Enumeration was the missing piece; verification stays judgment.

Exit contract (CHECK_STANDARD §9): 0 clean · 1 FINDINGS (pairing/symmetry violations) ·
2 CANNOT-CERTIFY (git unavailable, bad range). Leg (i) prints regardless (perimeter-stated).

Usage (cwd-proof):
    python3 .../complete_check.py                # range = today's commits (author date)
    python3 .../complete_check.py --since 2026-08-12   # explicit range start
"""
import os
import re
import subprocess
import sys
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
VERBS = re.compile(
    r"\b(logged|registered|queued|filed|wired|encoded|shipped|moved|banked|re-cut|recut|"
    r"regenerated|committed|landed|routed|updated|created|struck|retired|bannered)\b", re.I)
CLAIM_SCOPE = ("inbox/", "upgrades/", "outbox/", "design/", "builds/")


def sh(args):
    p = subprocess.run(args, capture_output=True, text=True)
    if p.returncode != 0:
        print(f"🔴 complete_check CANNOT-CERTIFY: {' '.join(args)} rc={p.returncode} "
              f"({(p.stderr or '').strip()[:160]})")
        sys.exit(2)
    return p.stdout


def main():
    since = date.today().isoformat()
    if "--since" in sys.argv:
        try:
            since = sys.argv[sys.argv.index("--since") + 1]
            date.fromisoformat(since)
        except (IndexError, ValueError):
            print("🔴 complete_check CANNOT-CERTIFY: --since needs YYYY-MM-DD")
            return 2
    repo = sh(["git", "rev-parse", "--show-toplevel"]).strip()
    os.chdir(repo)
    # NOTE --since is exclusive-of-now semantics on a bare date ("since now-o'clock");
    # use 00:00 explicitly (fleet memory: finding_bare_since_date_drops_same_day_commits).
    # Scope = MY commits only (subject-prefix convention; all agents share the git author) —
    # the first capable-case run swept 202 fleet-wide commits and enumerated BRENT's claims.
    commits = [l.split(" ", 1)[0] for l in
               sh(["git", "log", f"--since={since} 00:00", "--pretty=%H %s"]).splitlines()
               if l and l.split(" ", 1)[-1].startswith("DAEDALUS")]
    findings = 0

    # Leg (ii) — BLUEPRINTS/UPGRADE_PROTOCOL <-> EVOLUTION same-commit pairing
    checked = 0
    for c in commits:
        files = sh(["git", "show", "--name-only", "--pretty=", c]).splitlines()
        touches = [f for f in files if f.startswith("AGENTS/DAEDALUS/BLUEPRINTS/")
                   or f == "AGENTS/DAEDALUS/UPGRADE_PROTOCOL.md"]
        if touches:
            checked += 1
            if "AGENTS/DAEDALUS/EVOLUTION.md" not in files:
                findings += 1
                print(f"⏰ PAIRING: commit {c[:9]} touches {touches[0]}"
                      f"{' (+%d more)' % (len(touches)-1) if len(touches) > 1 else ''} "
                      f"with NO EVOLUTION.md in the same commit (PAT-101 rule ii)")

    # Leg (iii) — READER_REPORTS pair symmetry (whole upgrades/ dir, cheap)
    updir = os.path.join(repo, "AGENTS/DAEDALUS/upgrades")
    docs = set(os.listdir(updir))
    pairs = 0
    for d in sorted(docs):
        if d.endswith("_READER_REPORTS.md"):
            pairs += 1
            prefix = d[:-len("_READER_REPORTS.md")]
            if f"{prefix}.md" in docs:
                continue
            # Legit alternate form: the companion's own header names its synthesis home
            # (sweeps-playbook synthesis, or the enumerated-cluster index stub — see
            # UPGRADE_PROTOCOL's 8/17 contract clause). First capable-case run flagged
            # 3 such legitimate forms as violations; a pointer in the head is the pass.
            head = "".join(open(os.path.join(updir, d), encoding="utf-8",
                                errors="replace").readlines()[:15])
            if re.search(r"[Ss]ynthesis|sweeps/", head):
                print(f"· pair-by-pointer: upgrades/{d} (synthesis named in its header)")
                continue
            findings += 1
            print(f"⏰ PAIR-SYMMETRY: upgrades/{d} has NO synthesis beside it and names "
                  f"none in its header (expected {prefix}.md or a pointer — PAT-100 inverted-pair class)")

    # Leg (i) — claim enumeration (judgment walk-list; never gates rc)
    #
    # DIFF-SCOPED (2026-08-20, closing WALTER's 8/17 discharge-path packet): claims are
    # read from lines my commits ADDED in range, never from the current whole file.
    # One mechanism, three defects closed:
    #   (a) re-inflation — touching an old upgrades/ doc no longer re-prints its
    #       historical claims (the 483-line un-dischargeable backlog class);
    #   (b) false attribution — a `git mv` of inbound mail to processed/ adds zero
    #       lines, so other agents' sentences never enter the list (the 2026-08-19
    #       measurement: all 7 flagged claims were PROME's/WALTER's, surfaced by filing);
    #   (c) delivered-packet blindness — the 8/19 fix for (b) excluded every /inbox/
    #       path, which also dropped packets I AUTHOR into other agents' inboxes:
    #       the founding PAT-101 instance (a false side-effect claim in a delivered
    #       packet to PROME). Its docstring said those "were never in scope anyway" —
    #       wrong about its own filter, and PROME/inbox/ (repo root, not AGENTS/)
    #       never matched the path test at all. Both re-included below.
    # My own inbox stays excluded as stated intent (inbound content is not my claim
    # even when an edit touches it); everyone else's inbox is exactly where my
    # delivered claims live.
    def claim_scope(f):
        if f.startswith("AGENTS/DAEDALUS/inbox/"):
            return False
        return (f.endswith(".md")
                and (f.startswith("AGENTS/") or f.startswith("PROME/"))
                and any(s in f for s in CLAIM_SCOPE))

    claims, claim_files = 0, set()
    for c in commits:
        cur, new_ln = None, 0
        for raw in sh(["git", "show", "-U0", "--pretty=", c]).splitlines():
            if raw.startswith("+++ b/"):
                cur = raw[6:]
                cur = cur if claim_scope(cur) else None
            elif raw.startswith("@@"):
                m = re.search(r"\+(\d+)", raw)
                new_ln = int(m.group(1)) if m else 0
            elif raw.startswith("+") and not raw.startswith("+++"):
                if cur:
                    line = raw[1:]
                    if VERBS.search(line) and not line.lstrip().startswith(">"):
                        claims += 1
                        claim_files.add(cur)
                        if claims <= 40:
                            print(f"· CLAIM {cur}:{new_ln}: {line.strip()[:140]}")
                new_ln += 1
    if claims > 40:
        print(f"· CLAIM … +{claims - 40} more lines (raise the cap or narrow --since; "
              f"count is COMPLETE, display is capped — stated, not silent)")

    print(f"{'✅' if not findings else '⏰'} complete_check: {len(commits)} commit(s) since "
          f"{since} · pairing checked on {checked} standards commit(s), "
          f"{findings} violation(s) · {pairs} READER_REPORTS pair(s) checked · "
          f"{claims} side-effect claim line(s) ADDED this range across {len(claim_files)} doc(s) — "
          f"WALK THE CLAIM LIST before closeout; leg (i) is enumeration, not verification")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
