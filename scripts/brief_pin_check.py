#!/usr/bin/env python3
"""NEXUS brief amendment-11 pin check — `pin-follows-STATUS-HEAD`, computed over every brief.

WHY (Prose-Remedy Census #1, 2026-10-08, `AGENTS/DAEDALUS/runs/2026-10-08_PROSE_REMEDY_CENSUS_01.md`):
the brief-vs-STATUS ordering rule was carried as a sentence on 7 desks (CARL 43 sessions, FALCON 48,
LABOR 33, MARCO 32, OTTO 7, ZHAO 5, NEXUS's readers 3) and coded only at VIOLET and SAM, both in the
amendment-10 TIMESTAMP form that amendment 11 superseded on 2026-08-07. Amendment 11
(`AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md:164`): "The brief's STATUS commit hash must EQUAL that
agent's STATUS HEAD at the moment the brief is committed." The schema's scope constraint (:165, :175)
says it is a CHECK on an existing obligation and must NOT be added as a closeout step in any desk's
CLAUDE.md — so this is ONE repo-root instrument, run by the reader (NEXUS), not seven desk copies.

USAGE:  python3 scripts/brief_pin_check.py [DESK ...] [--root PATH] [--quiet]   (no DESK = every brief)
        python3 scripts/brief_pin_check.py --selftest

Per brief (AGENTS/<D>/NEXUS_BRIEF.md), with S = the last commit touching AGENTS/<D>/STATUS.md and
B = the last commit touching the brief:
  OK-SAME-COMMIT   B == S (brief folded in the same commit as STATUS — always satisfies A11)
  OK-PINNED        the pin hash in the brief's header equals S (prefix match)
  STALE-PIN        the pin names an older STATUS commit: STATUS was re-committed after the fold  ⇒ rc 1
  PIN-UNRESOLVED   the pin is not a commit that touched STATUS (typo, other file, rebased away)  ⇒ rc 1
  UNPINNED         no hash in the header (prose pointer or no line): A11 cannot be checked; the line
                   reports the A10 fallback (is B at or after S?) — ADVISORY, never rc 1
  DIRTY            STATUS or brief has uncommitted changes (mid-closeout) — reported, not graded
rc: 0 = no STALE-PIN / PIN-UNRESOLVED · 1 = at least one · 2 = cannot evaluate (git failed, no
briefs found, unknown desk named). WHAT A PASS DOES NOT PROVE: brief CONTENT matches STATUS (a fresh
pin over a stale body passes — header-over-body is out of reach by construction); UNPINNED desks
are not checked for A11 at all.
"""
import argparse, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HEADER_LINES = 40
PIN_RE = re.compile(r"STATUS commit\W{0,12}([0-9a-f]{7,40})\b", re.I)
BLOCKING = {"STALE-PIN", "PIN-UNRESOLVED"}


def git(root, *args):
    r = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or "").strip().split("\n")[0] or f"git {' '.join(args)} rc={r.returncode}")
    return r.stdout.strip()


HISTORICAL_RE = re.compile(r"\bhistorical\b", re.I)


def find_pin(brief_text):
    """First STATUS-commit hash in the header, skipping lines that label themselves historical: BRENT's
    header carries 'Historical October7 catch-up delivery … STATUS commit `88364423e`' as a past-delivery
    note, and reading it as the live pin produced a false STALE-PIN on the first live run (2026-10-08)."""
    for ln in brief_text.splitlines()[:HEADER_LINES]:
        if HISTORICAL_RE.search(ln):
            continue
        m = PIN_RE.search(ln)
        if m:
            return m.group(1).lower()
    return None


def check_desk(root, desk):
    rel_s, rel_b = f"AGENTS/{desk}/STATUS.md", f"AGENTS/{desk}/NEXUS_BRIEF.md"
    if not (root / "AGENTS" / desk).is_dir():
        return "CANNOT-EVALUATE", f"unknown desk: AGENTS/{desk}/ does not exist (a typo must never read as clean)"
    if not (root / rel_b).is_file():
        return "NO-BRIEF", f"{rel_b} absent"
    if not (root / rel_s).is_file():
        return "CANNOT-EVALUATE", f"{rel_s} absent"
    dirty = git(root, "status", "--porcelain", "--", rel_s, rel_b)
    s = git(root, "log", "-1", "--format=%H", "--", rel_s)
    b = git(root, "log", "-1", "--format=%H", "--", rel_b)
    if not s or not b:
        return "CANNOT-EVALUATE", "no commit history for STATUS or brief"
    pin = find_pin((root / rel_b).read_text(errors="replace"))
    note = " (uncommitted edits present — mid-closeout; graded on committed state)" if dirty else ""
    if b == s:
        return "OK-SAME-COMMIT", f"brief and STATUS last committed together in {s[:9]}{note}"
    if pin:
        if s.startswith(pin):
            return "OK-PINNED", f"pin {pin} = STATUS HEAD{note}"
        status_commits = git(root, "log", "--format=%H", "--", rel_s).split()
        hit = [c for c in status_commits if c.startswith(pin)]
        if hit:
            n_after = status_commits.index(hit[0])
            return "STALE-PIN", (f"pin {pin} is {n_after} STATUS commit(s) behind HEAD {s[:9]} — STATUS was "
                                 f"re-committed after the brief fold; re-pin and re-commit the brief{note}")
        return "PIN-UNRESOLVED", f"pin {pin} is not a commit that touched {rel_s} (STATUS HEAD {s[:9]}){note}"
    s_ahead = subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", s, b]).returncode == 0
    return "UNPINNED", (f"no STATUS hash in the first {HEADER_LINES} header lines — A11 not checkable; "
                        f"A10 fallback: brief commit {b[:9]} is {'AFTER' if s_ahead else 'BEFORE'} STATUS HEAD {s[:9]}{note}")


def run(root, desks, quiet=False):
    if not desks:
        desks = sorted(p.parent.name for p in (root / "AGENTS").glob("*/NEXUS_BRIEF.md"))
        if not desks:
            print(f"BRIEF-PIN 2 CANNOT-EVALUATE: 0 briefs found under {root}/AGENTS/*/NEXUS_BRIEF.md — "
                  f"an empty population is not compliance")
            return 2
    out, rc = [], 0
    for d in desks:
        try:
            v, why = check_desk(root, d)
        except RuntimeError as e:
            v, why = "CANNOT-EVALUATE", f"git failed: {e}"
        out.append((d, v, why))
    # precedence: a found stale pin is actionable (1) even if another desk could not be read; otherwise
    # any CANNOT-EVALUATE means the run cannot certify (2) — never a silent 0 (CHECK_STANDARD §9)
    if any(v in BLOCKING for _, v, _ in out):
        rc = 1
    elif any(v == "CANNOT-EVALUATE" for _, v, _ in out):
        rc = 2
    counts = {}
    for _, v, _ in out:
        counts[v] = counts.get(v, 0) + 1
    head = " · ".join(f"{k} {n}" for k, n in sorted(counts.items()))
    tag = "BRIEF-PIN 1 STALE" if rc == 1 else ("BRIEF-PIN 2 CANNOT-EVALUATE" if rc == 2 else "BRIEF-PIN 0 OK")
    print(f"{tag}: {len(out)} brief(s) checked against amendment 11 (pin-follows-STATUS-HEAD) — {head}. "
          f"A PASS proves the pin, never the brief's content; UNPINNED briefs are not A11-checked.")
    for d, v, why in out:
        if quiet and v in ("OK-SAME-COMMIT", "OK-PINNED", "NO-BRIEF"):
            continue
        mark = "⛔" if v in BLOCKING else ("⚠️" if v in ("UNPINNED", "CANNOT-EVALUATE") else "✅")
        print(f"  {mark} {d:<9} {v:<15} {why}")
    return rc


def selftest():
    """Frozen git fixtures: every verdict reached on a capable case, and each blocking one shown to block."""
    ok, n = True, 0

    def sh(td, *a):
        subprocess.run(["git", "-C", td, *a], check=True, capture_output=True,
                       env={"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
                            "GIT_COMMITTER_EMAIL": "t@t", "PATH": "/usr/bin:/bin"})

    def commit(td, rel, text, msg):
        p = Path(td) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        sh(td, "add", rel)
        sh(td, "commit", "-q", "-m", msg)
        return git(Path(td), "rev-parse", "HEAD")

    with tempfile.TemporaryDirectory() as td:
        sh(td, "init", "-q")
        s1 = commit(td, "AGENTS/A/STATUS.md", "s1", "A status 1")
        # A: pinned to s1, brief committed after → OK-PINNED
        commit(td, "AGENTS/A/NEXUS_BRIEF.md", f"**As of:** x | STATUS commit: `{s1[:9]}`\n", "A brief")
        # B: brief + status in one commit → OK-SAME-COMMIT
        p = Path(td) / "AGENTS/B"; p.mkdir(parents=True)
        (p / "STATUS.md").write_text("b"); (p / "NEXUS_BRIEF.md").write_text("STATUS commit: same commit\n")
        sh(td, "add", "AGENTS/B"); sh(td, "commit", "-q", "-m", "B both")
        # C: pinned to c1, then STATUS re-committed → STALE-PIN
        c1 = commit(td, "AGENTS/C/STATUS.md", "c1", "C status 1")
        commit(td, "AGENTS/C/NEXUS_BRIEF.md", f"STATUS commit: {c1[:9]}\n", "C brief")
        commit(td, "AGENTS/C/STATUS.md", "c2", "C status 2 after fold")
        # D: pin is a non-STATUS hash → PIN-UNRESOLVED
        commit(td, "AGENTS/D/STATUS.md", "d1", "D status")
        commit(td, "AGENTS/D/NEXUS_BRIEF.md", f"STATUS commit: `{s1[:9]}`\n", "D brief pinned to A's status")
        # E: no pin line, brief after status → UNPINNED (advisory)
        commit(td, "AGENTS/E/STATUS.md", "e1", "E status")
        commit(td, "AGENTS/E/NEXUS_BRIEF.md", "STATUS commit: see git log\n", "E brief")
        # F: only hash is in a line labelled Historical (BRENT 10/8 shape), STATUS moved on → UNPINNED, not STALE
        f1 = commit(td, "AGENTS/F/STATUS.md", "f1", "F status 1")
        commit(td, "AGENTS/F/NEXUS_BRIEF.md", f"> **Historical delivery — STATUS commit `{f1[:9]}`.**\n", "F brief")
        commit(td, "AGENTS/F/STATUS.md", "f2", "F status 2")
        want = {"A": "OK-PINNED", "B": "OK-SAME-COMMIT", "C": "STALE-PIN", "D": "PIN-UNRESOLVED", "E": "UNPINNED",
                "F": "UNPINNED"}
        for d, w in want.items():
            got = check_desk(Path(td), d)[0]
            good = got == w; ok &= good; n += good
            print(f"  {'PASS' if good else 'FAIL'}  {d}: {got} (want {w})")
        import io, contextlib
        cases = [(["A", "B", "E"], 0, "advisory UNPINNED never blocks"), (["A", "C"], 1, "STALE-PIN blocks"),
                 (["D"], 1, "PIN-UNRESOLVED blocks"), (["ZZ"], 2, "an unknown desk is CANNOT-EVALUATE, never clean"),
                 (["C", "ZZ"], 1, "a stale pin outranks an unreadable desk")]
        for desks, want_rc, label in cases:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                got = run(Path(td), desks)
            good = got == want_rc; ok &= good; n += good
            print(f"  {'PASS' if good else 'FAIL'}  rc {desks}: {got} (want {want_rc}) — {label}")
    with tempfile.TemporaryDirectory() as td2:
        (Path(td2) / "AGENTS").mkdir()
        subprocess.run(["git", "-C", td2, "init", "-q"], check=True)
        buf = __import__("io").StringIO()
        with __import__("contextlib").redirect_stdout(buf):
            got = run(Path(td2), [])
        good = got == 2 and "0 briefs found" in buf.getvalue(); ok &= good; n += good
        print(f"  {'PASS' if good else 'FAIL'}  empty population -> rc {got} (want 2)")
    total = 12
    print(f"BRIEF-PIN SELFTEST {'0 PASS' if ok and n == total else '1 FAIL'}: {n}/{total}")
    return 0 if ok and n == total else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("desks", nargs="*")
    ap.add_argument("--root")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        sys.exit(selftest())
    root = Path(a.root) if a.root else ROOT
    sys.exit(run(root, [d.strip().upper() for d in a.desks], a.quiet))


if __name__ == "__main__":
    main()
