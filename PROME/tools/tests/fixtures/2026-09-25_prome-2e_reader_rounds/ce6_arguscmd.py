# CE-R3-6: execute ARGUS leg (b)① exactly as written: `git diff --stat <that sha>:ORIGIN DEST` "must print NOTHING (no output = identical)"
from harness import *
f = Fx("ce6"); f.move()
sha = sh("git", "ls-remote", "origin", "refs/heads/master", cwd=f.repo).split()[0]
def run(label):
    r = subprocess.run(["git", "diff", "--stat", f"{sha}:{ORIGIN}", DEST], cwd=f.repo, capture_output=True, text=True)
    print(f"[{label}] rc={r.returncode} stdout={r.stdout.strip()[:160]!r} stderr={r.stderr.strip()[:160]!r}")
run("identical")
write(f.repo, DEST, "packet body DIFFERENT\n"); run("DEST differs on disk (unstaged)")
sh("git", "add", DEST, cwd=f.repo); run("DEST differs, staged")
sh("git", "commit", "-q", "-m", "c", "--", ORIGIN, DEST, cwd=f.repo); run("after commit, DEST differs")
r = subprocess.run(["git", "diff", "--stat", f"{sha}:{ORIGIN}", f"HEAD:{DEST}"], cwd=f.repo, capture_output=True, text=True)
print(f"[blob:blob form, differs] rc={r.returncode} stdout={r.stdout.strip()[:160]!r}")
os.chdir(Path(f.repo) / "PROME")   # ARGUS spawned from PROME/ cwd (the agent's launch dir)
r = subprocess.run(["git", "diff", "--stat", f"{sha}:{ORIGIN}", DEST], capture_output=True, text=True)
print(f"[from PROME/ cwd, differs] rc={r.returncode} stdout={r.stdout.strip()[:160]!r} stderr={r.stderr.strip()[:200]!r}")
r = subprocess.run(["git", "cat-file", "-e", f"{sha}:{ORIGIN}"], capture_output=True, text=True)
print(f"[cat-file -e from PROME/ cwd] rc={r.returncode} stderr={r.stderr.strip()[:120]!r}")
f.done()
