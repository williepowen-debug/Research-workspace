#!/usr/bin/env python3
"""Regression cases for the four FALSE-ASSURANCE defects Codex found on 2026-09-05.

Run:  .venv/bin/python3 AGENTS/WALTER/tools/test_false_assurance_regressions.py
Exit: 0 all pass · 1 any fail.
Size: 3 test functions / **15 assertions** (7 + 4 + 4).

⚠️ THE COUNT IS STATED HERE BECAUSE I GOT IT WRONG. Commit dbf8c765c, the PROME
packet and the report to Will all said "16 cases" — an unreproduced number, in a
finding whose whole subject is instruments that certify more than they establish.
PROME docked the sweep (DOCKET L294) recording that it had NOT re-counted it; the
count is 15. Read it off the runtime output (`grep -cE "^  (PASS|FAIL)"`), never
off the source: `grep -c "^    check("` returns 10, because four call sites carry
deeper indentation inside a `with`/`try` block.
[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]
[[finding_loadbearing_number_must_be_reproducible]]

WHY THESE EXIST, AND WHY THEY ARE TESTS RATHER THAN A NEW CHECK.
All four defects are of ONE class: an instrument that certifies MORE than it
establishes. None of them fires a false alarm — each returns a clean, confident,
WRONG answer, which is the failure direction nothing prompts you to re-check.
Codex's own recommendation was to fix the existing checks and add narrow regression
cases, NOT to add another monitor — a second monitor over a lying first monitor
inherits the lie. `[[finding_test_the_guard_not_just_the_guarded]]`

Each case below FAILS against the pre-2026-09-05 logic and PASSES against the fix.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

FAILS = []


def check(name, cond, detail=""):
    print(f"  {'PASS' if cond else 'FAIL'}  {name}" + (f" — {detail}" if detail and not cond else ""))
    if not cond:
        FAILS.append(name)


def _git(cwd, *args):
    return subprocess.run(["git", "-C", str(cwd), *args], capture_output=True, text=True)


def _scratch_repo(tmp):
    """An origin + a clone whose master carries ONE commit origin never received."""
    origin, work = tmp / "origin.git", tmp / "work"
    subprocess.run(["git", "init", "--bare", "-q", str(origin)], check=True)
    subprocess.run(["git", "clone", "-q", str(origin), str(work)], check=True)
    _git(work, "config", "user.email", "t@t"); _git(work, "config", "user.name", "t")
    (work / "pushed.md").write_text("on origin\n")
    _git(work, "add", "pushed.md"); _git(work, "commit", "-qm", "pushed")
    _git(work, "push", "-q", "origin", "HEAD:master")
    _git(work, "fetch", "-q", "origin")
    # a handoff committed LOCALLY and never pushed, then deleted (the trap shape)
    (work / "local_only.md").write_text("never pushed\n")
    _git(work, "add", "local_only.md"); _git(work, "commit", "-qm", "local only")
    (work / "local_only.md").unlink()
    _git(work, "commit", "-qam", "local only removed")
    return work


# ── 1 + 2: history reachability must be scoped to origin, not `--all` ─────────
def test_history_scope():
    print("\n[1+2] delivery history must be proved against origin/master, not --all")
    with tempfile.TemporaryDirectory() as td:
        work = _scratch_repo(Path(td))
        old = _git(work, "log", "--all", "--oneline", "-1", "--", "local_only.md").stdout.strip()
        new = _git(work, "log", "origin/master", "--oneline", "-1", "--", "local_only.md").stdout.strip()
        check("`--all` DOES see the unpushed local commit (the defect is real)", bool(old),
              "if this fails the fixture is wrong, not the code")
        check("origin-scoped history does NOT see it (the fix)", not new,
              f"origin/master history returned {new!r} for a never-pushed path")

        import reconcile_delivery_log as rdl
        import os
        cwd = os.getcwd()
        try:
            os.chdir(work)
            check("reconciler ever_in_git() -> False for a never-pushed path",
                  rdl.ever_in_git("local_only.md") is False,
                  f"got {rdl.ever_in_git('local_only.md')!r} — a local-only commit would flip to `delivered`")
            check("reconciler ever_in_git() -> True for a path that reached origin",
                  rdl.ever_in_git("pushed.md") is True)
            check("reconciler ever_in_git() -> None when the ref is unusable (UNKNOWN, not delivered)",
                  rdl._unusable_ref_probe() is None if hasattr(rdl, "_unusable_ref_probe") else
                  rdl.sh(["git", "log", "no/such/ref", "--oneline", "-1", "--", "x"]).returncode != 0)
        finally:
            os.chdir(cwd)

    import walter_doctor as wd
    src = Path(wd.__file__).read_text()
    check("doctor _ever_in_git no longer returns True on an exception",
          "return True   # fail SAFE" not in src,
          "the fail-OPEN branch is still present")
    check("doctor _ever_in_git is scoped to DELIVERY_REF",
          'DELIVERY_REF = "origin/master"' in src and '"log", DELIVERY_REF,' in src)


# ── 3: a consume declaration must come from the DESTINATION owner ────────────
def test_consume_owner_match():
    print("\n[3] a consume declaration must belong to the destination owner")
    import walter_doctor as wd
    touched = [
        "R100\tAGENTS/ALPHA/inbox/WALTER/p.md\tAGENTS/ALPHA/inbox/WALTER/processed/p.md",
        "M\tAGENTS/BETA/inbox/WALTER/processed/.consumed.tsv",
    ]
    owners = wd._consume_ledger_owners(touched)
    check("BETA's ledger does NOT declare ALPHA's filing", "ALPHA" not in owners,
          f"owners={owners!r} — another desk's receipt certified ALPHA's consumption")
    check("BETA's own ledger still declares BETA", owners == {"BETA"}, f"owners={owners!r}")

    same = ["R100\tAGENTS/ALPHA/inbox/WALTER/p.md\tAGENTS/ALPHA/inbox/WALTER/processed/p.md",
            "M\tAGENTS/ALPHA/inbox/WALTER/processed/.consumed.tsv"]
    check("ALPHA's own ledger DOES declare ALPHA (no false negative)",
          "ALPHA" in wd._consume_ledger_owners(same))
    check("WALTER's own inbox shape is still recognised",
          wd._consume_ledger_owners(["M\tAGENTS/WALTER/inbox/processed/.consumed.tsv"]) == {"WALTER"})


# ── 4: index freshness must hash the rows that are THERE ─────────────────────
def test_index_rows_hashed():
    print("\n[4] index freshness must compare LIVE rows, not only the stored banner")
    import importlib.util
    spec = importlib.util.spec_from_file_location("gbi", HERE / "gen_board_index.py")
    gbi = importlib.util.module_from_spec(spec); spec.loader.exec_module(gbi)
    sigs, errors = gbi.load_signals()
    check("signal set loads for the test", bool(sigs) and not errors, f"{len(errors)} load error(s)")
    if not sigs:
        return
    marks = gbi.derive_markers(sigs)
    rows = sorted(gbi.render_row(s, marks) for s in sigs.values())

    # Tamper exactly as Codex did: change a recipient, leave the banner alone.
    tampered = list(rows)
    tampered[0] = tampered[0].replace("WALTER → ", "WALTER → ROGUE, ", 1)
    check("a changed recipient makes the live row-set differ from the projection",
          sorted(tampered) != rows,
          "the tamper was a no-op — the fixture, not the check, is wrong")

    src = Path(HERE / "walter_doctor.py").read_text()
    check("doctor hashes the live rows (`| SIG-W-` extraction present)",
          'l.startswith("| SIG-W-")' in src,
          "the post-cutover branch still compares two signal-derived values only")
    check("doctor reports row DRIFT as HIGH",
          "ROWS have DRIFTED from the generated projection" in src)


if __name__ == "__main__":
    print("WALTER false-assurance regressions (Codex 2026-09-05)")
    test_history_scope()
    test_consume_owner_match()
    test_index_rows_hashed()
    print()
    if FAILS:
        print(f"✗ {len(FAILS)} FAILED: {', '.join(FAILS)}")
        sys.exit(1)
    print("✓ all regression cases pass")
