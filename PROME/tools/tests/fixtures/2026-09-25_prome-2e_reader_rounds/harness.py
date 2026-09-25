import importlib.util, os, subprocess, tempfile, sys, json
from pathlib import Path
from unittest.mock import patch
RW = Path("/home/willi/Research-workspace")
spec = importlib.util.spec_from_file_location("argus_scope_r3", RW / "PROME/tools/argus_scope.py")
A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
SP = Path(os.environ["SP"])
PKT = "2026-09-24_from-VIOLET_walkback.md"
ORIGIN = f"PROME/inbox/{PKT}"; DEST = f"PROME/inbox/processed/{PKT}"
def sh(*a, cwd, check=True):
    r = subprocess.run(a, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode: raise RuntimeError(f"{a}: {r.stderr}")
    return r.stdout
def write(repo, rel, text="x\n", mode="w"):
    p = Path(repo) / rel; p.parent.mkdir(parents=True, exist_ok=True)
    (p.write_bytes(text) if isinstance(text, bytes) else p.write_text(text, encoding="utf-8")); return rel
def commit(repo, subject, paths):
    sh("git", "add", *paths, cwd=repo); sh("git", "commit", "-q", "-m", subject, "--", *paths, cwd=repo)
class Fx:
    def __init__(self, name, pre_packet=None):
        self.tmp = Path(tempfile.mkdtemp(prefix=name + "_", dir=SP))
        self.repo = str(self.tmp / "work"); self.bare = str(self.tmp / "origin.git")
        sh("git", "init", "-q", "--bare", "-b", "master", self.bare, cwd=self.tmp)
        sh("git", "init", "-q", "-b", "master", self.repo, cwd=self.tmp)
        sh("git", "config", "user.email", "t@t", cwd=self.repo); sh("git", "config", "user.name", "t", cwd=self.repo)
        sh("git", "remote", "add", "origin", self.bare, cwd=self.repo)
        write(self.repo, "PROME/state/AUDIT_PERIMETER.tsv", (RW / "PROME/state/AUDIT_PERIMETER.tsv").read_text())
        if pre_packet: pre_packet(self)
        commit(self.repo, "PROME: STANDARD closeout", [write(self.repo, "PROME/STATUS.md", "s\n"), "PROME/state/AUDIT_PERIMETER.tsv"])
        commit(self.repo, "VIOLET -> PROME: walkback", [write(self.repo, ORIGIN, "packet body v1\n")])
        sh("git", "push", "-q", "-u", "origin", "master", cwd=self.repo)
        self.p = patch.object(A, "ROOT", Path(self.repo)); self.p.start()
        os.chdir(self.repo)
        A.record_baseline(sh("git", "rev-parse", "HEAD", cwd=self.repo).strip())
        write(self.repo, "PROME/SCRATCH.md", "scratch v2\n")
    def move(self, o=ORIGIN, d=DEST):
        (Path(self.repo) / d).parent.mkdir(parents=True, exist_ok=True); sh("git", "mv", o, d, cwd=self.repo)
    def freeze(self, moves, reviewed=True):
        A.record_review(["PROME/SCRATCH.md"], consumed_moves=moves)
        if reviewed:
            rc, msg = A.mark_reviewed("fx"); assert rc == 0, msg
    def verify(self, paths=("PROME/SCRATCH.md", ORIGIN, DEST), ref=None):
        return A.verify_review(paths=list(paths) if paths is not None else None, ref=ref)
    def done(self): self.p.stop(); os.chdir(SP)
def show(tag, res):
    rc, out = res; print(f"[{tag}] rc={rc}")
    for l in out: print("    ", l[:260])
