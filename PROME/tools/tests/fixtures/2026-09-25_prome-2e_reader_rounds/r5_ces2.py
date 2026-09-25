from harness import *
exec(open("r5_ces.py").read().split("# R5-0a")[0].split("from harness import *")[1])   # helpers only

# R5-5: symref onto a NON-checked-out branch `side` that holds the unpushed packet
f = Fx("r5_5"); o, d = unpushed(f)
sh("git", "branch", "side", cwd=f.repo); s0 = sh("git", "rev-parse", "side", cwd=f.repo).strip()
sh("git", "update-ref", "-d", "refs/remotes/origin/master", cwd=f.repo)
sh("git", "symbolic-ref", "refs/remotes/origin/master", "refs/heads/side", cwd=f.repo)
f.move(o, d); f.freeze({d: o})
R("R5-5 symref -> non-checked-out side", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK")
s1 = sh("git", "rev-parse", "side", cwd=f.repo).strip(); print("   side before/after:", s0[:9], s1[:9], "UNTOUCHED" if s0 == s1 else "!!! MOVED")
f.done()

# R5-6a: tracking ref PACKED (legit move) — no false block
f = Fx("r5_6a"); sh("git", "pack-refs", "--all", cwd=f.repo)
print("   loose ref file exists?", (Path(f.repo)/".git/refs/remotes/origin/master").exists(), "| in packed-refs?", "refs/remotes/origin/master" in (Path(f.repo)/".git/packed-refs").read_text())
f.move(); f.freeze({DEST: ORIGIN})
R("R5-6a packed tracking ref, legit move", f.verify(), "PASS"); f.done()

# R5-6b: tracking ref PACKED and POISONED to a local commit holding the unpushed packet
f = Fx("r5_6b"); o, d = unpushed(f)
sh("git", "update-ref", "refs/remotes/origin/master", "HEAD", cwd=f.repo); sh("git", "pack-refs", "--all", cwd=f.repo)
f.move(o, d); f.freeze({d: o})
R("R5-6b packed + poisoned tracking ref", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK"); f.done()

# R5-7: NEGATIVE refspec in config excluding master + poisoned (loose) tracking ref
f = Fx("r5_7"); o, d = unpushed(f)
sh("git", "config", "--add", "remote.origin.fetch", "^refs/heads/master", cwd=f.repo)
sh("git", "update-ref", "refs/remotes/origin/master", "HEAD", cwd=f.repo)
p0 = sh("git", "rev-parse", "refs/remotes/origin/master", cwd=f.repo).strip()
f.move(o, d); f.freeze({d: o})
R("R5-7 negative refspec ^refs/heads/master + poisoned ref", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK")
p1 = sh("git", "rev-parse", "refs/remotes/origin/master", cwd=f.repo).strip(); print("   tracking ref before/after:", p0[:9], p1[:9], "| real master:", sh("git","rev-parse","master",cwd=f.bare).strip()[:9])
f.done()

# R5-7b: negative refspec, legit move (does it false-block?)
f = Fx("r5_7b"); sh("git", "config", "--add", "remote.origin.fetch", "^refs/heads/master", cwd=f.repo)
f.move(); f.freeze({DEST: ORIGIN})
R("R5-7b negative refspec, legit move", f.verify(), "PASS"); f.done()

# R5-8: remote.origin.uploadpack redirect — url=real, uploadpack serves the MIRROR
f = Fx("r5_8"); o, d = unpushed(f); m = mirror_with_packet(f)
sh("git", "config", "remote.origin.uploadpack", f"git-upload-pack {m} #", cwd=f.repo)
print("   get-url:", sh("git","remote","get-url","origin",cwd=f.repo).strip()[-20:], "| --push:", sh("git","remote","get-url","--push","origin",cwd=f.repo).strip()[-20:])
f.move(o, d); f.freeze({d: o})
R("R5-8 uploadpack redirect to mirror", f.verify(("PROME/SCRATCH.md", o, d)), "BLOCK")
print("   real has packet?", has(f.bare, o)); f.done()

# R5-9: url written with a trailing slash / different spelling in pushurl for the SAME repo (false-block probe)
f = Fx("r5_9"); sh("git", "remote", "set-url", "--push", "origin", f.bare + "/", cwd=f.repo)
f.move(); f.freeze({DEST: ORIGIN})
R("R5-9 pushurl = url + '/' (same server)", f.verify(), "PASS"); f.done()
