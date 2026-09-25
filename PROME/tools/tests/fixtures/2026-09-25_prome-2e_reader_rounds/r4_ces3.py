# R4-5b: refs/remotes/origin/master symref -> refs/heads/master (CHECKED-OUT) with an unpushed local commit
from harness import *
f = Fx("r4c_5")
commit(f.repo, "PROME: unpushed work", [write(f.repo, "PROME/STATUS.md", "unpushed\n")])
head0 = sh("git", "rev-parse", "HEAD", cwd=f.repo).strip()
sh("git", "update-ref", "-d", "refs/remotes/origin/master", cwd=f.repo)
sh("git", "symbolic-ref", "refs/remotes/origin/master", "refs/heads/master", cwd=f.repo)
f.move()
A.record_review(["PROME/SCRATCH.md", "PROME/STATUS.md"], consumed_moves={DEST: ORIGIN}); print("mark:", A.mark_reviewed("fx"))
rc, out = f.verify(("PROME/SCRATCH.md", "PROME/STATUS.md", ORIGIN, DEST)); print("rc", rc); [print("   ", l[:220]) for l in out]
head1 = sh("git", "rev-parse", "HEAD", cwd=f.repo).strip()
print("HEAD before/after verify:", head0[:9], head1[:9])
print("status:", sh("git", "status", "--short", cwd=f.repo).replace("\n", " ; "))
print("reflog:", sh("git", "reflog", "-3", "master", cwd=f.repo).replace("\n", " ; "))
f.done()
