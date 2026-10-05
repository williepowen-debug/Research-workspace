"""Read-only owner import; exercise BOND's freeze in disposable repositories.

Run from any directory with PYTHONDONTWRITEBYTECODE=1. No network or owner edits.
This demonstrates present behavior, not acceptance tests for a proposed repair.
"""
import hashlib
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "AGENTS/BOND/monitors/closeout_run.py"
spec = importlib.util.spec_from_file_location("bond_closeout_probe", SOURCE)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def git(repo, *args):
    return subprocess.run(
        ["git", *args], cwd=repo, check=True, capture_output=True, text=True
    ).stdout.strip()


print("source_sha256", hashlib.sha256(SOURCE.read_bytes()).hexdigest())
with tempfile.TemporaryDirectory(prefix="cato-bond-freeze-") as directory:
    repo = Path(directory)
    git(repo, "init", "-q")
    git(repo, "config", "user.name", "CATO isolated probe")
    git(repo, "config", "user.email", "cato-probe@example.invalid")
    owned = repo / "AGENTS/BOND/STATUS.md"
    other = repo / "AGENTS/OTHER/note.md"
    for path in (owned, other):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("initial\n")
    git(repo, "add", "AGENTS/BOND/STATUS.md", "AGENTS/OTHER/note.md")
    git(repo, "commit", "-qm", "initial fixture")
    before = runner.tree_digest(repo)
    contents = owned.read_bytes()
    other.write_text("unrelated owner update\n")
    git(repo, "add", "AGENTS/OTHER/note.md")
    git(repo, "commit", "-qm", "unrelated owner commit")
    after = runner.tree_digest(repo)
    row = ["fixture", "standard", "recorded-head", "RAN", "steps", before]
    accepted, reason = runner.verify_decision(row, after)
    assert owned.read_bytes() == contents
    assert before != after and not accepted
    print("unchanged BOND bytes + unrelated commit: FREEZE MOVED reproduced")
    print(reason)
    owned.write_text("actual BOND edit\n")
    changed = runner.tree_digest(repo)
    assert changed != after
    print("actual BOND tracked edit: digest changes")
    new = repo / "AGENTS/BOND/new-note.md"
    new.write_text("first\n")
    first = runner.tree_digest(repo)
    new.write_text("second\n")
    assert runner.tree_digest(repo) != first
    print("untracked BOND content edit: digest changes")
    packet = repo / "PROME/inbox/fixture_from-BOND.md"
    packet.parent.mkdir(parents=True)
    packet.write_text("packet first\n")
    first = runner.tree_digest(repo)
    packet.write_text("packet second\n")
    assert runner.tree_digest(repo) != first
    print("outgoing BOND packet content edit: digest changes")
    with tempfile.TemporaryDirectory(prefix="cato-not-git-") as empty:
        assert runner.tree_digest(Path(empty)) is None
    print("missing git repository: UNKNOWN preserved")
    assert not runner.verify_decision(
        ["fixture", "standard", "head", "FAILED", "steps", changed], changed
    )[0]
    print("matching digest after FAILED run: refusal preserved")
