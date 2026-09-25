# Round-4 reader, pass 2: --ref cases with SCRATCH committed (pass 1's rc=1 there came from an uncommitted SCRATCH)
import subprocess as S, json
from harness import *
from unittest.mock import patch as P
def R(tag, res, must):
    rc, out = res; got = "PASS" if rc == 0 else "BLOCK"; r100 = any("R100-CONSUMED-MOVE" in l for l in out)
    print(f"[{tag}] rc={rc} {got} (must {must}) r100_receipt={r100} => {'OK' if got == must else '!!! HOLE' if must == 'BLOCK' else '!!! FALSE-BLOCK'}")
    for l in out: print("     ", l[:200])
def consume(f): sh("git", "commit", "-q", "-m", "PROME: consume", "--", ORIGIN, DEST, "PROME/SCRATCH.md", cwd=f.repo)
def addscratch(f): sh("git", "add", "PROME/SCRATCH.md", cwd=f.repo)

# R4-1/2 with --ref HEAD, clean fixture
f = Fx("r4b_1")
write(f.repo, ORIGIN, "packet body LOCAL EDIT\n"); commit(f.repo, "PROME: local edit", [ORIGIN])
addscratch(f); f.move(); f.freeze({DEST: ORIGIN}); consume(f)
X = sh("git", "rev-parse", f"origin/master:{ORIGIN}", cwd=f.repo).strip(); Y = sh("git", "rev-parse", f"HEAD:{DEST}", cwd=f.repo).strip()
R("control --ref HEAD no replace", f.verify(ref="HEAD"), "BLOCK")
sh("git", "update-ref", f"refs/replace/{X}", Y, cwd=f.repo)
R("R4-1 update-ref refs/replace, --ref HEAD", f.verify(ref="HEAD"), "BLOCK")
env_wo = {k: v for k, v in os.environ.items() if k != "GIT_NO_REPLACE_OBJECTS"}
real_run = S.run
def strip_flag(argv, *a, **k):
    if argv[:2] == ["git", "--no-replace-objects"]: argv = ["git"] + argv[2:]
    return real_run(argv, *a, **k)
with P.object(A, "_NOREPLACE_ENV", env_wo):
    R("R4-2a env UNSET, argv kept", f.verify(ref="HEAD"), "BLOCK")
with P.object(A.subprocess, "run", strip_flag):
    R("R4-2b argv STRIPPED, env kept", f.verify(ref="HEAD"), "BLOCK")
def strip_both(argv, *a, **k):
    k["env"] = env_wo; return strip_flag(argv, *a, **k)
with P.object(A.subprocess, "run", strip_both):
    R("R4-2c CONTROL both removed", f.verify(ref="HEAD"), "BLOCK")
f.done()

# R4-8a legit committed move, --ref HEAD explicit
f = Fx("r4b_8")
addscratch(f); f.move(); f.freeze({DEST: ORIGIN}); consume(f)
R("R4-8a --ref HEAD explicit legit", f.verify(ref="HEAD"), "PASS")
calls = []; real = A._fetch_origin_sha
with P.object(A, "_fetch_origin_sha", lambda: (calls.append(1), real())[1]):
    rc, out = A.verify_review(paths=None, ref="HEAD")
print(f"[R4-8b --ref HEAD manifest-only] rc={rc} fetches={len(calls)} {out}")
# malformed consumed_moves: manifest-only vs explicit
m = Path(f.repo) / A.REVIEW_FILE; d = json.loads(m.read_text()); d["consumed_moves"] = ["not", "a", "map"]; m.write_text(json.dumps(d))
print("[R4-9 malformed consumed_moves] manifest-only:", A.verify_review(paths=None, ref="HEAD")[0],
      "| explicit:", f.verify(ref="HEAD")[0])
f.done()

# R4-5b: refs/remotes/origin/master symref -> refs/heads/master (the CHECKED-OUT branch) with an unpushed commit
f = Fx("r4b_5")
commit(f.repo, "PROME: unpushed work", [write(f.repo, "PROME/STATUS.md", "unpushed\n")])
head0 = sh("git", "rev-parse", "HEAD", cwd=f.repo).strip()
sh("git", "update-ref", "-d", "refs/remotes/origin/master", cwd=f.repo)
sh("git", "symbolic-ref", "refs/remotes/origin/master", "refs/heads/master", cwd=f.repo)
f.move(); f.freeze({DEST: ORIGIN})
R("R4-5b symref -> checked-out master", f.verify(), "PASS")
head1 = sh("git", "rev-parse", "HEAD", cwd=f.repo).strip()
print("   HEAD before/after verify:", head0[:9], head1[:9], "| status:", sh("git", "status", "--short", cwd=f.repo).replace("\n", " ; "))
f.done()
