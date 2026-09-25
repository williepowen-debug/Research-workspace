# Round-5 reader counterexamples (read-only against the repo; throwaway repos under SP)
from harness import *
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
    for l in out: print("     ", l[:260])
def has(bare, path):
    return bool(sh("git", "ls-tree", "-r", "--name-only", "master", "--", path, cwd=bare).strip())
def mirror_with_packet(f):
    m = str(f.tmp / "mirror.git"); sh("git", "clone", "-q", "--bare", f.repo, m, cwd=f.tmp); return m

# R5-0a: re-run R4-4 (url=mirror has packet, pushurl=real lacks)
f = Fx("r5_0a"); o, d = unpushed(f); m = mirror_with_packet(f)
sh("git", "remote", "set-url", "origin", m, cwd=f.repo); sh("git", "remote", "set-url", "--push", "origin", f.bare, cwd=f.repo)
f.move(o, d); f.freeze({d: o})
R("R5-0a (R4-4) pushurl mirror", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK"); f.done()

# R5-0b: re-run R4-5b (symref onto CHECKED-OUT master + unpushed commit)
f = Fx("r5_0b")
commit(f.repo, "PROME: unpushed work", [write(f.repo, "PROME/STATUS.md", "unpushed\n")])
h0 = sh("git", "rev-parse", "HEAD", cwd=f.repo).strip()
sh("git", "update-ref", "-d", "refs/remotes/origin/master", cwd=f.repo)
sh("git", "symbolic-ref", "refs/remotes/origin/master", "refs/heads/master", cwd=f.repo)
f.move(); A.record_review(["PROME/SCRATCH.md", "PROME/STATUS.md"], consumed_moves={DEST: ORIGIN}); print("mark:", A.mark_reviewed("fx"))
R("R5-0b (R4-5b) symref->checked-out master", f.verify(("PROME/SCRATCH.md", "PROME/STATUS.md", ORIGIN, DEST)), "BLOCK")
h1 = sh("git", "rev-parse", "HEAD", cwd=f.repo).strip(); print("   HEAD before/after:", h0[:9], h1[:9], "UNTOUCHED" if h0 == h1 else "!!! MOVED")
print("   reflog:", sh("git", "reflog", "-2", "master", cwd=f.repo).replace("\n", " ; ")); f.done()

# R5-1: remote.origin.url MULTI-VALUED [mirror(has), real(lacks)], no pushurl: fetch reads url[0], push goes to ALL
f = Fx("r5_1"); o, d = unpushed(f); m = mirror_with_packet(f)
sh("git", "config", "--replace-all", "remote.origin.url", m, cwd=f.repo)
sh("git", "config", "--add", "remote.origin.url", f.bare, cwd=f.repo)
print("   get-url --all:", sh("git", "remote", "get-url", "--all", "origin", cwd=f.repo).split(), "| --push --all:", sh("git", "remote", "get-url", "--push", "--all", "origin", cwd=f.repo).split())
f.move(o, d); f.freeze({d: o})
R("R5-1 url=[mirror,real] (push goes to both)", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK")
print("   real origin has packet?", has(f.bare, o), "| mirror has?", has(m, o))
sh("git", "commit", "-q", "-m", "PROME: consume", cwd=f.repo)
sh("git", "push", "-q", "origin", "HEAD:master", cwd=f.repo)
print("   AFTER `git push origin HEAD:master` (safe-push's command): real has DEST?", has(f.bare, d), "| real ever had ORIGIN in history?",
      bool(sh("git", "log", "--all", "--format=%h", "--", o, cwd=f.bare).strip()))
f.done()

# R5-1b: pushurl = SAME string as url AND a second url — url=[real], pushurl=[real]? and url=[m,real] pushurl=[real,m]
f = Fx("r5_1b"); o, d = unpushed(f); m = mirror_with_packet(f)
sh("git", "config", "--replace-all", "remote.origin.url", m, cwd=f.repo); sh("git", "config", "--add", "remote.origin.url", f.bare, cwd=f.repo)
sh("git", "config", "--add", "remote.origin.pushurl", f.bare, cwd=f.repo); sh("git", "config", "--add", "remote.origin.pushurl", m, cwd=f.repo)
f.move(o, d); f.freeze({d: o})
R("R5-1b url=[mirror,real] pushurl=[real,mirror] (sorted-equal)", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK"); f.done()

# R5-2: pushInsteadOf — url=mirror, url.<real>.pushInsteadOf=<mirror>
f = Fx("r5_2"); o, d = unpushed(f); m = mirror_with_packet(f)
sh("git", "remote", "set-url", "origin", m, cwd=f.repo); sh("git", "config", f"url.{f.bare}.pushInsteadOf", m, cwd=f.repo)
print("   get-url:", sh("git", "remote", "get-url", "origin", cwd=f.repo).strip(), "| --push:", sh("git", "remote", "get-url", "--push", "origin", cwd=f.repo).strip())
f.move(o, d); f.freeze({d: o})
R("R5-2 pushInsteadOf rewrites push to real", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK"); f.done()

# R5-3: insteadOf (both directions) — url=alias:, url.<mirror>.insteadOf=alias: ; consistent → fetch AND push go to mirror
f = Fx("r5_3"); o, d = unpushed(f); m = mirror_with_packet(f)
sh("git", "remote", "set-url", "origin", "alias:repo", cwd=f.repo); sh("git", "config", f"url.{m[:-len('mirror.git')]}.insteadOf", "alias:", cwd=f.repo)
sh("git", "config", f"url.{m}.insteadOf", "alias:repo", cwd=f.repo)
print("   get-url:", sh("git", "remote", "get-url", "origin", cwd=f.repo).strip(), "| --push:", sh("git", "remote", "get-url", "--push", "origin", cwd=f.repo).strip())
f.move(o, d); f.freeze({d: o})
R("R5-3 insteadOf both ways -> mirror (push target HAS it: PASS acceptable)", f.verify(("PROME/SCRATCH.md", o, d)), "PASS"); f.done()

# R5-3b: insteadOf fetch-only asymmetry via pushurl literal: url=alias:repo(->mirror), pushurl=alias:repo? get-url --push on pushurl also expands insteadOf?
f = Fx("r5_3b"); o, d = unpushed(f); m = mirror_with_packet(f)
sh("git", "remote", "set-url", "origin", "alias:repo", cwd=f.repo); sh("git", "config", f"url.{m}.insteadOf", "alias:repo", cwd=f.repo)
sh("git", "config", f"url.{f.bare}.pushInsteadOf", "alias:repo", cwd=f.repo)
print("   get-url:", sh("git", "remote", "get-url", "origin", cwd=f.repo).strip(), "| --push:", sh("git", "remote", "get-url", "--push", "origin", cwd=f.repo).strip())
f.move(o, d); f.freeze({d: o})
R("R5-3b insteadOf->mirror + pushInsteadOf->real", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK"); f.done()

# R5-4: pushurl list of two URLs [real, mirror], url=real
f = Fx("r5_4"); o, d = unpushed(f); m = mirror_with_packet(f)
sh("git", "config", "--add", "remote.origin.pushurl", f.bare, cwd=f.repo); sh("git", "config", "--add", "remote.origin.pushurl", m, cwd=f.repo)
f.move(o, d); f.freeze({d: o})
R("R5-4 url=real pushurl=[real,mirror]", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK"); f.done()
