# Round-4 reader counterexamples (read-only against the repo; throwaway repos under SP)
import sys, subprocess as S
from harness import *
from unittest.mock import patch as P

def unpushed(f, name="2026-09-25_from-LOCAL_unpushed.md"):
    o, d = f"PROME/inbox/{name}", f"PROME/inbox/processed/{name}"
    commit(f.repo, "LOCAL -> PROME", [write(f.repo, o, "local only\n")])
    return o, d

def R(tag, res, must):
    rc, out = res
    got = "PASS" if rc == 0 else "BLOCK"
    r100 = any("R100-CONSUMED-MOVE" in l for l in out)
    verdict = "OK" if got == must else "!!! HOLE" if must == "BLOCK" else "!!! FALSE-BLOCK"
    print(f"[{tag}] rc={rc} {got} (must {must}) r100_receipt={r100} => {verdict}")
    for l in out: print("     ", l[:230])

# R4-1: replace ref written DIRECTLY with update-ref (no `git replace` porcelain)
f = Fx("r4_1")
write(f.repo, ORIGIN, "packet body LOCAL EDIT\n"); commit(f.repo, "PROME: local edit", [ORIGIN])
f.move(); f.freeze({DEST: ORIGIN})
X = sh("git", "rev-parse", f"origin/master:{ORIGIN}", cwd=f.repo).strip()
Y = sh("git", "rev-parse", f":{DEST}", cwd=f.repo).strip()
sh("git", "update-ref", f"refs/replace/{X}", Y, cwd=f.repo)
print("plain git sees origin blob as:", repr(sh("git", "cat-file", "-p", X, cwd=f.repo)))
R("R4-1 update-ref refs/replace, worktree", f.verify(), "BLOCK")
sh("git", "commit", "-q", "-m", "PROME: consume", cwd=f.repo)
R("R4-1 update-ref refs/replace, --ref HEAD", f.verify(ref="HEAD"), "BLOCK")
# R4-2: belt-and-braces — each guard alone, then neither (control that the fixture can detect the hole)
env_wo = {k: v for k, v in os.environ.items() if k != "GIT_NO_REPLACE_OBJECTS"}
with P.object(A, "_NOREPLACE_ENV", env_wo):
    R("R4-2a env var UNSET by wrapper, argv flag kept", f.verify(ref="HEAD"), "BLOCK")
real_run = S.run
def strip_flag(argv, *a, **k):
    if argv[:2] == ["git", "--no-replace-objects"]: argv = ["git"] + argv[2:]
    return real_run(argv, *a, **k)
with P.object(A.subprocess, "run", strip_flag):
    R("R4-2b argv flag STRIPPED, env var kept", f.verify(ref="HEAD"), "BLOCK")
    with P.object(A, "_NOREPLACE_ENV", env_wo):
        def strip_both(argv, *a, **k):
            k.pop("env", None); k["env"] = env_wo
            return strip_flag(argv, *a, **k)
        with P.object(A.subprocess, "run", strip_both):
            R("R4-2c CONTROL both removed (expect the round-3 hole to reappear)", f.verify(ref="HEAD"), "BLOCK")
f.done()

# R4-3: `origin` IS configured, but its url is a LOCAL PATH to a nested clone holding the unpushed packet
f = Fx("r4_3")
o, d = unpushed(f)
sh("git", "clone", "-q", "--bare", f.repo, str(Path(f.repo) / "origin"), cwd=f.repo)
(Path(f.repo) / ".git/info/exclude").write_text("origin/\n")
sh("git", "remote", "set-url", "origin", "./origin", cwd=f.repo)
f.move(o, d); f.freeze({d: o})
R("R4-3 remote.origin.url=./origin (nested clone w/ unpushed packet)", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK")
print("   ls-remote of the REAL bare (safe-push's historic target) has the packet?:",
      bool(sh("git", "ls-tree", "-r", "--name-only", "master", "--", o, cwd=f.bare).strip()))
f.done()

# R4-4: fetch url and pushurl DIVERGE — url = a mirror that holds the unpushed packet, pushurl = the real origin
f = Fx("r4_4")
o, d = unpushed(f)
mirror = str(f.tmp / "mirror.git")
sh("git", "clone", "-q", "--bare", f.repo, mirror, cwd=f.tmp)
sh("git", "remote", "set-url", "origin", mirror, cwd=f.repo)
sh("git", "remote", "set-url", "--push", "origin", f.bare, cwd=f.repo)
print("   git remote -v:", sh("git", "remote", "-v", cwd=f.repo).replace("\n", " | "))
f.move(o, d); f.freeze({d: o})
R("R4-4 url=mirror(has packet) pushurl=real(lacks)", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK")
f.done()

# R4-5: refs/remotes/origin/master is a SYMREF to a local branch holding the unpushed packet
f = Fx("r4_5")
o, d = unpushed(f)
sh("git", "branch", "side", cwd=f.repo)
sh("git", "update-ref", "-d", "refs/remotes/origin/master", cwd=f.repo)
sh("git", "symbolic-ref", "refs/remotes/origin/master", "refs/heads/side", cwd=f.repo)
side0 = sh("git", "rev-parse", "side", cwd=f.repo).strip()
f.move(o, d); f.freeze({d: o})
R("R4-5 origin/master symref -> local branch", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK")
print("   side before/after verify:", side0[:9], sh("git", "rev-parse", "side", cwd=f.repo).strip()[:9],
      "| symref still?:", sh("git", "symbolic-ref", "-q", "refs/remotes/origin/master", cwd=f.repo, check=False).strip() or "no")
f.done()

# R4-6: textconv driver on *.md — does `git show REF:path` (--ref form) hash converted output?
f = Fx("r4_6")
write(f.repo, ORIGIN, "packet body LOCAL EDIT\n"); commit(f.repo, "PROME: local edit", [ORIGIN])
f.move(); f.freeze({DEST: ORIGIN}); sh("git", "commit", "-q", "-m", "PROME: consume", cwd=f.repo)
conv = f.tmp / "conv.sh"; conv.write_text("#!/bin/sh\nprintf 'packet body v1\\n'\n"); conv.chmod(0o755)
(Path(f.repo) / ".git/info/attributes").write_text("*.md diff=cv\n")
sh("git", "config", "diff.cv.textconv", str(conv), cwd=f.repo)
R("R4-6 textconv on *.md, --ref HEAD", f.verify(ref="HEAD"), "BLOCK")
f.done()

# R4-7: mark_reviewed (verify_review() no args) with a declared move and a CHANGED candidate
f = Fx("r4_7")
f.move(); f.freeze({DEST: ORIGIN}, reviewed=False)
write(f.repo, "PROME/SCRATCH.md", "scratch v3 EDITED AFTER FREEZE\n")
calls = []; real = A._fetch_origin_sha
with P.object(A, "_fetch_origin_sha", lambda: (calls.append(1), real())[1]):
    print("[R4-7 mark_reviewed on changed candidate w/ declared move] ->", A.mark_reviewed("x"), "fetches:", len(calls))
f.done()

# R4-8: --ref HEAD in both forms: explicit legit committed move (must PASS w/ receipt), manifest-only (no fetch)
f = Fx("r4_8")
f.move(); f.freeze({DEST: ORIGIN}); sh("git", "commit", "-q", "-m", "PROME: consume", "--", ORIGIN, DEST, cwd=f.repo)
R("R4-8a --ref HEAD explicit, legit committed move", f.verify(ref="HEAD"), "PASS")
calls = []
with P.object(A, "_fetch_origin_sha", lambda: (calls.append(1), real())[1]):
    rc, out = A.verify_review(paths=None, ref="HEAD")
print(f"[R4-8b --ref HEAD manifest-only] rc={rc} fetches={len(calls)}", out)
# R4-8c: only DEST listed (partial recovery) — must block
R("R4-8c --ref HEAD, --paths lists DEST only", f.verify(("PROME/SCRATCH.md", DEST), ref="HEAD"), "BLOCK")
f.done()
