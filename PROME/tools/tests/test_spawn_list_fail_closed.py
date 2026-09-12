"""spawn_list.py must FAIL CLOSED when liveness cannot be established.

Defect (DAEDALUS, L294 origin-proof sweep, 2026-09-12): `last_self_commit` read only `.stdout`
and never `.returncode`, so a FAILED `git log` was indistinguishable from "no commits" and
classified DARK. DARK at a due row IS the WQ-184 Tier-1 spawn trigger, so a git failure
authorised spawning every owner.

Acceptance conditions -> PROME/tools/tests/ACCEPTANCE_spawn_list_dark_on_git_failure.md
Run: python3 PROME/tools/tests/test_spawn_list_fail_closed.py   (rc 0 pass / 1 fail)
"""
import datetime as dt, pathlib, subprocess, sys, types

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "PROME" / "tools"))
import spawn_list as S

TODAY = dt.date(2026, 9, 12)
START = dt.date(2026, 9, 11)
DUE = dt.date(2026, 9, 11)


class FakeRun:
    """Stand in for subprocess.run with a chosen returncode/stdout/stderr."""
    def __init__(self, rc, out="", err=""):
        self.rc, self.out, self.err = rc, out, err
    def __call__(self, *a, **k):
        return types.SimpleNamespace(returncode=self.rc, stdout=self.out, stderr=self.err)


def classify_with(rc, out="", err="", owner="BROCK"):
    orig = S.subprocess.run
    S.subprocess.run = FakeRun(rc, out, err)
    try:
        live = S.Liveness(None)
        return S.classify(owner, START, DUE, TODAY, live)
    finally:
        S.subprocess.run = orig


GOOD = "2026-09-09\t6c01f41a1\tBROCK: CRMT Q2 grade\n"
checks = []

# 1 — git FAILURE must not be DARK (the reported defect)
d, cls, basis = classify_with(128, "", "fatal: index.lock exists")
checks.append(("git rc!=0 => UNKNOWN, never DARK", cls == "UNKNOWN"))
checks.append(("  and the basis says liveness was NOT established", "not established" in basis.lower()))
checks.append(("  and it says NOT a spawn candidate", "not a spawn" in basis.lower()))

# 2 — a GENUINE empty result must STILL be DARK (the repair must not blunt the real signal)
d, cls, basis = classify_with(0, "")
checks.append(("rc=0 + empty => still DARK (real signal preserved)", cls == "DARK"))
checks.append(("  with the original 'no self-commit' basis", "no self-commit" in basis))

# 3 — the two are distinguishable
_, c_err, b_err = classify_with(128, "", "boom")
_, c_ok, b_ok = classify_with(0, "")
checks.append(("failure and absence are DISTINGUISHABLE", c_err != c_ok and b_err != b_ok))

# 4 — ordinary path still works (regression)
d, cls, basis = classify_with(0, GOOD)
checks.append(("rc=0 with a commit before row start => DARK", cls == "DARK"))
d, cls, basis = classify_with(0, "2026-09-11\tabc1234\tBROCK: later\n")
checks.append(("rc=0 with a commit on/after row start => ACTIVE", cls == "ACTIVE"))

# 5 — OVERLAP neighbour: no commits AND a failing call => error dominates
d, cls, _ = classify_with(1, "", "fatal: bad object")
checks.append(("overlap (no commits AND failure) => UNKNOWN, error dominates", cls == "UNKNOWN"))

# 6 — WRONG-OWNER neighbour: an unparseable owner cell is a parse failure, not a dark desk
d, cls, basis = classify_with(0, "", owner="?")
checks.append(("unparseable owner '?' => UNKNOWN, not DARK", cls == "UNKNOWN"))
checks.append(("  and says so", "unparseable" in basis.lower()))

# 7 — UNKNOWN must move the exit code and be visible (never a quiet all-clear)
rows = [("D:L260", "2026-09-11", 1, "BROCK", "UNKNOWN", "git log FAILED, liveness not established (x) — NOT a spawn candidate", "cat")]
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    rc = S.render(rows, TODAY, 0, False)
out = buf.getvalue()
checks.append(("UNKNOWN => rc 2 (not 0, not DARK's 1)", rc == 2))
checks.append(("UNKNOWN is flagged in the header line", "UNKNOWN 1" in out))
checks.append(("output warns never to spawn on UNKNOWN", "NEVER spawn on UNKNOWN" in out))

# 8 — a clean DARK row still returns 1, not 2
rows_d = [("D:L260", "2026-09-11", 1, "BROCK", "DARK", "no self-commit found in history", "cat")]
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    rc_d = S.render(rows_d, TODAY, 0, False)
checks.append(("a real DARK row still returns rc 1", rc_d == 1))

ok = True
for name, passed in checks:
    print(("PASS " if passed else "FAIL ") + name)
    ok &= passed
print(f"\ntest_spawn_list_fail_closed: {'PASS' if ok else 'FAIL'} {sum(p for _, p in checks)}/{len(checks)}")
sys.exit(0 if ok else 1)
