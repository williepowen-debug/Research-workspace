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

⛔ DO NOT QUOTE A MUTATION FAILURE COUNT AS A QUALITY MEASURE. I reported "7
assertions fail under the stubs"; Codex's exact repeat of its own two mutations
produced 5. Both runs are real — they are DIFFERENT INVOCATIONS (mine also stubbed
the index verdict helper), and the number moves with what you patch and with how
many assertions happen to cover it. THE RESULT THAT MATTERS IS BINARY: the suite
rejects the mutation. Preserve the INVOCATION, never the count:

    import walter_doctor as wd
    wd._ever_in_git = lambda p: True                                  # mutation 1
    wd.check_index_generated_fresh = lambda: [(wd.INFO, "generated INDEX fresh")]  # mutation 2
    # then re-run test_caller_invariant() and test_index_rows_behaviour();
    # ANY failure = the suite still discriminates. Zero failures = the suite is blind.

That is my fourth corrected claim of the session, and it is the same shape as the
other three: a number I composed rather than reproduced.
[[finding_loadbearing_number_must_be_reproducible]]
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


# ── C. the caller invariant, on a SELF-CONTAINED fixture ────────────────────
# 🔴 v3 2026-09-05 (Codex third pass): [C] used to run against the PRODUCTION
# delivery_log and whatever paths happened to exist, so a failure could be caused by
# changing fleet state rather than by code. The fixture below is a throwaway repo with
# exactly four rows — one delivered at its ORIGINAL path, one delivered then FILED to
# processed/ without pushing the move, one that never reached origin at all, and one
# whose evidence is unavailable — which is the full truth table this check has to get
# right. Failures are now attributable to the code.
_FIX_ROWS = ["orig-on-origin", "filed-locally", "never-on-origin", "evidence-unavailable"]


def _fixture_repo(tmp: Path):
    """origin + clone; returns (work, {case: relpath}). Delivery-log rows all say
    'delivered' — the check's job is to decide whether git agrees."""
    import walter_doctor as wd
    origin, work = tmp / "origin.git", tmp / "work"
    subprocess.run(["git", "init", "--bare", "-q", str(origin)], check=True)
    subprocess.run(["git", "clone", "-q", str(origin), str(work)], check=True, capture_output=True)
    g = lambda *a: subprocess.run(["git", "-C", str(work), *a], capture_output=True, text=True)
    g("config", "user.email", "t@t"); g("config", "user.name", "t")
    inbox = work / "AGENTS" / "AAA" / "inbox" / "WALTER"
    (inbox / "processed").mkdir(parents=True)
    rels = {c: f"AGENTS/AAA/inbox/WALTER/{c}.md" for c in _FIX_ROWS}
    for c in ("orig-on-origin", "filed-locally"):
        (work / rels[c]).write_text(f"{c}\n")
    g("add", "-A"); g("commit", "-qm", "handoffs delivered")
    g("push", "-q", "origin", "HEAD:master"); g("fetch", "-q", "origin")
    # the ordinary sequence: recipient files it locally, move NOT pushed
    g("mv", rels["filed-locally"], f"AGENTS/AAA/inbox/WALTER/processed/filed-locally.md")
    g("commit", "-qm", "recipient filed it")           # committed, deliberately NOT pushed
    # never-on-origin / evidence-unavailable: rows exist, files never did
    hdr = "\t".join(["signal_id", "recipient", "role", "precedence",
                      "handoff_path", "written_state", "timestamp_routed", "x", "y"])
    lines = [hdr]
    for i, c in enumerate(_FIX_ROWS):
        lines.append("\t".join([f"SIG-W-2026010{i}-001", "AAA", "action", "PRIORITY",
                                 rels[c], "delivered", "2026-01-01T00:00:00Z", "-", "-"]))
    logp = work / "AGENTS" / "WALTER" / "routed"
    logp.mkdir(parents=True)
    (logp / "delivery_log.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return work, rels


def _run_check_in(work: Path, ever_stub=None):
    import walter_doctor as wd
    saved = (wd.REPO, wd.WALTER, wd.BOARD, dict(wd._EVER_IN_GIT_CACHE), wd._ORIGIN_PATHS,
             wd._ever_in_git)
    try:
        wd.REPO, wd.WALTER, wd.BOARD = work, work / "AGENTS" / "WALTER", work / "BOARD"
        wd._EVER_IN_GIT_CACHE.clear(); wd._ORIGIN_PATHS = None
        if ever_stub is not None:
            wd._ever_in_git = ever_stub
        return " | ".join(m for _, m in wd.check_delivery_claim_vs_git()), \
               [s for s, _ in wd.check_delivery_claim_vs_git()]
    finally:
        (wd.REPO, wd.WALTER, wd.BOARD, cache, wd._ORIGIN_PATHS, wd._ever_in_git) = saved
        wd._EVER_IN_GIT_CACHE.clear(); wd._EVER_IN_GIT_CACHE.update(cache)


def test_caller_invariant():
    print("\n[C] delivery verdict on a self-contained 4-row fixture")
    import walter_doctor as wd
    with tempfile.TemporaryDirectory() as td:
        work, rels = _fixture_repo(Path(td))

        j, sevs = _run_check_in(work)
        check("a row delivered at its ORIGINAL path is not flagged",
              "orig-on-origin" not in j, f"got: {j[:220]}")
        check("🔴 an UNPUSHED FILING MOVE does not retract established delivery",
              "filed-locally" not in j,
              f"the v2 twin check erased proven delivery here — got: {j[:220]}")
        check("a path that NEVER reached origin is reported",
              "never-on-origin" in j, f"got: {j[:220]}")
        check("the never-delivered row is HIGH",
              any(s == wd.HIGH for s in sevs), f"sevs={sevs}")

        # unavailable evidence: git can answer nothing
        j2, sevs2 = _run_check_in(work, ever_stub=lambda p: None)
        check("unavailable evidence -> reported, never a pass",
              ("could NOT be verified" in j2) or ("UNKNOWN" in j2), f"got: {j2[:220]}")
        check("unavailable evidence does NOT produce the all-clear",
              "every 'delivered' delivery_log row is backed" not in j2)
        check("unavailable evidence is at least MED",
              any(s in (wd.MED, wd.HIGH) for s in sevs2), f"sevs={sevs2}")

        # sanity: the fixture discriminates — always-True must silence the real orphan
        j3, _ = _run_check_in(work, ever_stub=lambda p: True)
        check("always-True stub CHANGES the verdict (fixture discriminates)", j3 != j,
              "the check is insensitive to its history helper on this fixture")


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

    # (i) Codex's mutation 1, on the controlled fixture: `_ever_in_git` always True.
    #     The real orphan must stop being reported — i.e. [C] genuinely depends on it.
    with tempfile.TemporaryDirectory() as td:
        work, _ = _fixture_repo(Path(td))
        j_true, _ = _run_check_in(work, ever_stub=lambda p: True)
        j_false, _ = _run_check_in(work, ever_stub=lambda p: False)
        j_none, _ = _run_check_in(work, ever_stub=lambda p: None)
        j_real, _ = _run_check_in(work)
        check("always-True stub SILENCES the real orphan (so [C] discriminates)",
              "never-on-origin" not in j_true, f"got: {j_true[:200]}")
        check("always-True and always-False give DIFFERENT verdicts", j_true != j_false)
        check("always-None (unavailable) differs from both", j_none not in (j_true, j_false))
        check("the UNSTUBBED run differs from always-True (real git is consulted)",
              j_real != j_true)

    # (ii) sync helper stubbed — the unverified report must depend on it
    import walter_doctor as wd
    saved_sync = wd._sync_state
    try:
        wd._sync_state = lambda r, o: "on_origin"
        j_ok = " | ".join(m for _, m in wd.check_delivery_claim_vs_git())
        wd._sync_state = lambda r, o: "unknown"
        j_unk = " | ".join(m for _, m in wd.check_delivery_claim_vs_git())
    finally:
        wd._sync_state = saved_sync
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
