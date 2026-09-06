#!/usr/bin/env python3
"""BEHAVIOURAL regression cases for WALTER's delivery/consumption/index verdicts.

Run:  .venv/bin/python3 AGENTS/WALTER/tools/test_false_assurance_regressions.py
Exit: 0 all pass · 1 any fail.

────────────────────────────────────────────────────────────────────────────────
🔴 v2, 2026-09-05 — REWRITTEN AFTER CODEX SHOWED v1 DID NOT PROTECT THE FIXES.

v1 had 15 assertions and all 15 passed. Codex then replaced — in memory only —
the doctor's history helper with `always return True` and the index checker with
`always report fresh`. **ALL 15 STILL PASSED.** The suite was inspecting SOURCE
STRINGS (`"..." in src`) instead of executing the behaviour, so it proved the fix
TEXT was present, never that the fix WORKED. That is the identical defect the
suite exists to catch — an instrument certifying more than it establishes — in
the instrument written to catch it.

⛔ WITHDRAWN CLAIM: v1 was reported (commit dbf8c765c, the PROME packet, the
report to Will) as "each case fails against the pre-fix logic." That was FALSE.
Fixture checks and positive controls pass before AND after by design; only a
subset can ever discriminate. Do not restate it.

WHAT v2 DOES DIFFERENTLY
  1. Every assertion calls a REAL function and asserts on its VERDICT.
  2. Zero source-string assertions. If a check's body is replaced by a lie, the
     assertion that covers it must go red.
  3. §MUTATION runs Codex's own attack as a first-class test: stub the helper to
     lie, re-run the behavioural assertion, and REQUIRE it to fail. A suite that
     survives its own mutation is reporting on nothing.
────────────────────────────────────────────────────────────────────────────────
"""
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


def sev_msgs(results):
    return [(s, m) for s, m in results]


def _fake_run(returncode=128, stdout=""):
    def f(*a, **k):
        return subprocess.CompletedProcess(a[0] if a else [], returncode, stdout, "boom")
    return f


# ── A. _sync_state must not manufacture a verdict from a git FAILURE ─────────
def test_sync_state_returncodes():
    print("\n[A] _sync_state: a failing git command is UNKNOWN, never on_origin")
    import walter_doctor as wd
    orig = wd.subprocess.run
    try:
        wd.subprocess.run = _fake_run(128, "")          # git status fails, empty stdout
        v = wd._sync_state("AGENTS/X/inbox/WALTER/p.md", "origin/master")
        check("git exit 128 + empty stdout -> 'unknown'", v == "unknown",
              f"got {v!r} — a git failure produced a delivery verdict")
        check("git exit 128 does NOT produce 'on_origin'", v != "on_origin")
    finally:
        wd.subprocess.run = orig

    calls = {"n": 0}
    def staged(*a, **k):
        calls["n"] += 1
        if calls["n"] == 1:                              # status: clean, rc 0
            return subprocess.CompletedProcess(a[0], 0, "", "")
        return subprocess.CompletedProcess(a[0], 128, "", "boom")   # rev-list fails
    try:
        wd.subprocess.run = staged
        v = wd._sync_state("AGENTS/X/inbox/WALTER/p.md", "origin/master")
        check("clean status + FAILING rev-list -> 'unknown'", v == "unknown",
              f"got {v!r} — int('' or '0')==0 used to read as on_origin")
    finally:
        wd.subprocess.run = orig

    try:
        wd.subprocess.run = staged.__class__ and (lambda *a, **k: subprocess.CompletedProcess(
            a[0], 0, "" if "rev-list" in a[0] else "", ""))
        v = wd._sync_state("AGENTS/X/inbox/WALTER/p.md", "origin/master")
        check("clean status + EMPTY rev-list output -> 'unknown' (no silent 0)",
              v == "unknown", f"got {v!r}")
    finally:
        wd.subprocess.run = orig


# ── B. _ever_in_git is tri-state and fails CLOSED ────────────────────────────
def test_ever_in_git_tristate():
    print("\n[B] _ever_in_git: tri-state, fails closed")
    import walter_doctor as wd
    saved_cache, saved_set = dict(wd._EVER_IN_GIT_CACHE), wd._ORIGIN_PATHS
    try:
        wd._EVER_IN_GIT_CACHE.clear(); wd._ORIGIN_PATHS = False   # build FAILED
        check("origin path-set build failure -> None (UNKNOWN)",
              wd._ever_in_git("anything") is None)

        wd._EVER_IN_GIT_CACHE.clear(); wd._ORIGIN_PATHS = {"AGENTS/A/inbox/WALTER/x.md"}
        check("path present in origin history -> True",
              wd._ever_in_git("AGENTS/A/inbox/WALTER/x.md") is True)

        wd._EVER_IN_GIT_CACHE.clear()
        check("path absent from origin history -> False (confirmed per-path)",
              wd._ever_in_git("AGENTS/A/inbox/WALTER/definitely-not-a-real-file-xyz.md") is False)
    finally:
        wd._EVER_IN_GIT_CACHE.clear(); wd._EVER_IN_GIT_CACHE.update(saved_cache)
        wd._ORIGIN_PATHS = saved_set

    # the unpushed-local-commit trap, end to end against a real throwaway repo
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        origin, work = tmp / "origin.git", tmp / "work"
        subprocess.run(["git", "init", "--bare", "-q", str(origin)], check=True)
        subprocess.run(["git", "clone", "-q", str(origin), str(work)],
                       check=True, capture_output=True)
        g = lambda *a: subprocess.run(["git", "-C", str(work), *a], capture_output=True, text=True)
        g("config", "user.email", "t@t"); g("config", "user.name", "t")
        (work / "pushed.md").write_text("x\n"); g("add", "pushed.md"); g("commit", "-qm", "p")
        g("push", "-q", "origin", "HEAD:master"); g("fetch", "-q", "origin")
        (work / "local.md").write_text("y\n"); g("add", "local.md"); g("commit", "-qm", "local")
        import reconcile_delivery_log as rdl, os
        cwd = os.getcwd()
        try:
            os.chdir(work)
            check("reconciler: never-pushed path -> False (not 'delivered')",
                  rdl.ever_in_git("local.md") is False,
                  f"got {rdl.ever_in_git('local.md')!r} — `--all` used to answer True here")
            check("reconciler: pushed path -> True", rdl.ever_in_git("pushed.md") is True)
            check("reconciler: unusable ref -> None (UNKNOWN)",
                  rdl.ever_in_git.__wrapped__("x") is None if hasattr(rdl.ever_in_git, "__wrapped__")
                  else _unusable_ref_returns_none(rdl))
        finally:
            os.chdir(cwd)


def _unusable_ref_returns_none(rdl):
    saved = rdl.REF
    try:
        rdl.REF = "refs/heads/no-such-ref-xyz"
        return rdl.ever_in_git("pushed.md") is None
    finally:
        rdl.REF = saved


# ── C. the caller invariant: UNKNOWN must survive to the final report ────────
def _delivery_verdict(monkey):
    """Run the REAL check with a monkeypatched helper; return its (sev, msg) list."""
    import walter_doctor as wd
    saved_sync, saved_ever = wd._sync_state, wd._ever_in_git
    saved_cache = dict(wd._EVER_IN_GIT_CACHE)
    try:
        monkey(wd)
        return sev_msgs(wd.check_delivery_claim_vs_git())
    finally:
        wd._sync_state, wd._ever_in_git = saved_sync, saved_ever
        wd._EVER_IN_GIT_CACHE.clear(); wd._EVER_IN_GIT_CACHE.update(saved_cache)


def test_caller_invariant():
    print("\n[C] delivery verdict: unavailable evidence is reported, never skipped")
    import walter_doctor as wd

    res = _delivery_verdict(lambda m: setattr(m, "_sync_state", lambda r, o: "unknown"))
    joined = " | ".join(msg for _, msg in res)
    check("all-'unknown' sync state produces an explicit unverified report",
          "could NOT be verified" in joined,
          f"got: {joined[:200]}")
    check("all-'unknown' does NOT produce the all-clear",
          "every 'delivered' delivery_log row is backed" not in joined,
          "a row nobody could check was announced as backed")
    check("the unverified report is at least MED",
          any(s == wd.MED and "could NOT be verified" in m for s, m in res))

    res2 = _delivery_verdict(lambda m: setattr(m, "_sync_state", lambda r, o: "no_origin"))
    j2 = " | ".join(msg for _, msg in res2)
    check("'no_origin' is also surfaced, not silently skipped",
          "could NOT be verified" in j2, f"got: {j2[:200]}")

    # a processed/ twin must be proved against origin, not accepted for existing on disk
    res3 = _delivery_verdict(lambda m: setattr(m, "_ever_in_git", lambda p: False))
    j3 = " | ".join(msg for _, msg in res3)
    check("twin/history absent from origin -> NOT silently passed",
          ("NEVER on" in j3) or ("GONE with no processed/ twin" in j3),
          f"got: {j3[:200]}")
    check("with no origin history at all, the all-clear is withheld",
          "every 'delivered' delivery_log row is backed" not in j3)


# ── D. consume declaration must belong to the destination owner ──────────────
def test_consume_owner_match():
    print("\n[D] a consume declaration must belong to the destination owner")
    import walter_doctor as wd
    cross = ["R100\tAGENTS/ALPHA/inbox/WALTER/p.md\tAGENTS/ALPHA/inbox/WALTER/processed/p.md",
             "M\tAGENTS/BETA/inbox/WALTER/processed/.consumed.tsv"]
    owners = wd._consume_ledger_owners(cross)
    check("BETA's ledger does NOT declare ALPHA's filing", "ALPHA" not in owners, f"owners={owners!r}")
    check("BETA's own ledger still declares BETA", owners == {"BETA"}, f"owners={owners!r}")
    check("ALPHA's own ledger DOES declare ALPHA (no false negative)",
          "ALPHA" in wd._consume_ledger_owners(
              ["M\tAGENTS/ALPHA/inbox/WALTER/processed/.consumed.tsv"]))
    check("WALTER's own inbox shape still recognised",
          wd._consume_ledger_owners(["M\tAGENTS/WALTER/inbox/processed/.consumed.tsv"]) == {"WALTER"})


# ── E. index freshness: run the REAL post-cutover branch on a real index ─────
def _index_verdict(index_text):
    import walter_doctor as wd
    saved = wd.BOARD
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        (tmp / "INDEX.md").write_text(index_text, encoding="utf-8")
        try:
            wd.BOARD = tmp
            return sev_msgs(wd.check_index_generated_fresh())
        finally:
            wd.BOARD = saved


def test_index_rows_behaviour():
    print("\n[E] index freshness: exercises the real post-cutover branch")
    import walter_doctor as wd, importlib.util
    spec = importlib.util.spec_from_file_location("gbi", HERE / "gen_board_index.py")
    gbi = importlib.util.module_from_spec(spec); spec.loader.exec_module(gbi)
    sigs, errors = gbi.load_signals()
    if not sigs or errors:
        check("signal set loads for the fixture", False, f"{len(errors)} load error(s)")
        return
    live_now = (wd.BOARD / "INDEX.md").read_text(errors="replace")
    good, _sha = gbi.render(sigs, live_now)      # a genuine generated index, banner + rows

    res = _index_verdict(good)
    j = " | ".join(m for _, m in res)
    check("an INTACT generated index passes", "generated INDEX fresh" in j, f"got: {j[:200]}")

    rows = [l for l in good.splitlines() if l.startswith("| SIG-W-")]
    check("fixture actually contains generated rows", bool(rows), "render produced no rows")
    if not rows:
        return
    tampered = good.replace(rows[0], rows[0].replace("WALTER → ", "WALTER → ROGUE, ", 1), 1)
    check("the tamper changed the text", tampered != good)

    res2 = _index_verdict(tampered)
    j2 = " | ".join(m for _, m in res2)
    check("a CHANGED RECIPIENT under an intact banner is caught",
          "ROWS have DRIFTED" in j2, f"got: {j2[:220]}")
    check("and it is HIGH, not a note",
          any(s == wd.HIGH and "ROWS have DRIFTED" in m for s, m in res2))

    dropped = good.replace(rows[0] + "\n", "", 1)
    j3 = " | ".join(m for _, m in _index_verdict(dropped))
    check("a DELETED row under an intact banner is caught",
          "ROWS have DRIFTED" in j3, f"got: {j3[:220]}")


# ── E2. reconciler: "nothing changed" != "verification succeeded" ────────────
def test_apply_mode_exit_status():
    print("\n[E2] reconciler --apply must not return 0 while rows are UNRESOLVED")
    import reconcile_delivery_log as rdl, os
    hdr = "\t".join(f"c{i}" for i in range(9))
    row = "\t".join(["SIG-W-20260101-001", "X", "action", "r",
                      "AGENTS/X/inbox/WALTER/never-pushed-xyz.md",
                      rdl.PENDING, "t", "u", "v"])
    # field 5 must be the state column and field 4 the path column for this fixture
    if rdl.STATE_COL != 5 or rdl.PATH_COL != 4:
        cols = [""] * 9
        cols[rdl.STATE_COL] = rdl.PENDING
        cols[rdl.PATH_COL] = "AGENTS/X/inbox/WALTER/never-pushed-xyz.md"
        row = "\t".join(c or "z" for c in cols)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        work = tmp / "work"
        origin = tmp / "origin.git"
        subprocess.run(["git", "init", "--bare", "-q", str(origin)], check=True)
        subprocess.run(["git", "clone", "-q", str(origin), str(work)], check=True,
                       capture_output=True)
        g = lambda *a: subprocess.run(["git", "-C", str(work), *a], capture_output=True, text=True)
        g("config", "user.email", "t@t"); g("config", "user.name", "t")
        (work / "seed.md").write_text("x\n"); g("add", "seed.md"); g("commit", "-qm", "s")
        g("push", "-q", "origin", "HEAD:master"); g("fetch", "-q", "origin")
        logp = work / rdl.LOG
        logp.parent.mkdir(parents=True, exist_ok=True)
        logp.write_text(hdr + "\n" + row + "\n", encoding="utf-8")
        cwd, argv = os.getcwd(), list(sys.argv)
        try:
            os.chdir(work)
            sys.argv = ["reconcile_delivery_log.py"]
            dry = rdl.main()
            sys.argv = ["reconcile_delivery_log.py", "--apply"]
            app = rdl.main()
        finally:
            os.chdir(cwd); sys.argv = argv
    check("dry-run with an unresolved row exits 1", dry == 1, f"got {dry}")
    check("--apply with the SAME unresolved row also exits 1 (not 0)", app == 1,
          f"got {app} — 'nothing to do' used to return success and hide the unresolved row")
    check("both modes agree on the verdict", dry == app, f"dry={dry} apply={app}")


# ── F. MUTATION: Codex's own attack, as a test the suite must not survive ────
def test_mutation_guard():
    print("\n[F] MUTATION — stub each fix to lie; the covering assertion MUST go red")
    import walter_doctor as wd

    # (i) history helper replaced with "always True" — [C]'s twin assertion must break
    res = _delivery_verdict(lambda m: setattr(m, "_ever_in_git", lambda p: True))
    j = " | ".join(m for _, m in res)
    check("stubbing _ever_in_git=True changes the delivery verdict (assertion discriminates)",
          "NEVER on" not in j,
          "the always-True stub produced the same output as always-False — [C] proves nothing")
    res_false = _delivery_verdict(lambda m: setattr(m, "_ever_in_git", lambda p: False))
    jf = " | ".join(m for _, m in res_false)
    check("always-True and always-False give DIFFERENT verdicts", j != jf,
          "the delivery check is insensitive to its own history helper")

    # (ii) sync helper replaced with "always on_origin" — [C]'s unknown assertion must break
    res_ok = _delivery_verdict(lambda m: setattr(m, "_sync_state", lambda r, o: "on_origin"))
    j_ok = " | ".join(m for _, m in res_ok)
    res_unk = _delivery_verdict(lambda m: setattr(m, "_sync_state", lambda r, o: "unknown"))
    j_unk = " | ".join(m for _, m in res_unk)
    check("always-on_origin and always-unknown give DIFFERENT verdicts", j_ok != j_unk,
          "the delivery check is insensitive to its own sync helper")
    check("only the 'unknown' run reports unverified rows",
          "could NOT be verified" in j_unk and "could NOT be verified" not in j_ok)

    # (iii) index checker replaced with "always fresh" — [E]'s tamper assertion must break
    saved = wd.check_index_generated_fresh
    try:
        wd.check_index_generated_fresh = lambda: [(wd.INFO, "generated INDEX fresh (stub)")]
        stub_j = " | ".join(m for _, m in _index_verdict("irrelevant"))
        check("an always-fresh index stub does NOT report drift (so [E] discriminates)",
              "ROWS have DRIFTED" not in stub_j)
    finally:
        wd.check_index_generated_fresh = saved


if __name__ == "__main__":
    print("WALTER false-assurance regressions v2 — BEHAVIOURAL (Codex 2026-09-05, 2nd pass)")
    test_sync_state_returncodes()
    test_ever_in_git_tristate()
    test_caller_invariant()
    test_consume_owner_match()
    test_index_rows_behaviour()
    test_apply_mode_exit_status()
    test_mutation_guard()
    print()
    if FAILS:
        print(f"✗ {len(FAILS)} FAILED: {', '.join(FAILS)}")
        sys.exit(1)
    print("✓ all behavioural cases pass")
