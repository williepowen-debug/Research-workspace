#!/usr/bin/env python3
"""One-off acceptance evidence; all Git mutations/remotes stay in /tmp fixtures.

Exercises the existing safe-push script, not a new production runner or repair
command. Writes only a dated result beside this file. No real-repo Git mutation.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent


def run(cwd, *args, check=True):
    result = subprocess.run(args, cwd=cwd, capture_output=True, timeout=30)
    if check and result.returncode:
        raise RuntimeError(result.stderr.decode(errors="replace"))
    return result


def git(cwd, *args, check=True):
    return run(cwd, "git", *args, check=check)


def text(cwd, *args):
    return git(cwd, *args).stdout.decode().strip()


def write(repo, path, content):
    p = repo / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)


def foreign(repo):
    paths = repo / "AGENTS/FOREIGN"
    return {
        "index_entries": git(repo, "ls-files", "--stage", "-z", "--", "AGENTS/FOREIGN").stdout,
        "cached_diff": git(repo, "diff", "--cached", "--binary", "--", "AGENTS/FOREIGN").stdout,
        "unstaged_diff": git(repo, "diff", "--binary", "--", "AGENTS/FOREIGN").stdout,
        "rename_status": git(repo, "status", "--porcelain=v1", "-z", "--", "AGENTS/FOREIGN").stdout,
        "working_bytes": {str(p.relative_to(repo)): p.read_bytes()
                          for p in sorted(paths.rglob("*")) if p.is_file()},
    }


def digest(snapshot):
    return {k: hashlib.sha256(v).hexdigest() if isinstance(v, bytes) else
            {p: hashlib.sha256(b).hexdigest() for p, b in v.items()}
            for k, v in snapshot.items()}


def main():
    results = []
    with tempfile.TemporaryDirectory(prefix="terry-closeout-git-") as temporary:
        base = Path(temporary)
        remote, repo, peer = base / "origin.git", base / "owner", base / "peer"
        git(base, "init", "--bare", "--initial-branch=master", str(remote))
        git(base, "init", "--initial-branch=master", str(repo))
        git(repo, "config", "user.name", "Disposable TERRY fixture")
        git(repo, "config", "user.email", "fixture@example.invalid")
        write(repo, "AGENTS/TERRY/owned.md", "baseline\n")
        write(repo, "AGENTS/FOREIGN/edit.md", "baseline\n")
        write(repo, "AGENTS/FOREIGN/old.md", "".join(f"baseline {n}\n" for n in range(30)))
        write(repo, "PROME/ROSTER.md", "fixture marker, no actual desk activation\n")
        scripts = ["scripts/safe-push.sh", "scripts/install-git-hooks.sh",
                   "scripts/githooks/commit-msg", "scripts/githooks/pre-commit",
                   "scripts/githooks/pre-push"]
        for path in scripts:
            target = repo / path
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / path, target)
        git(repo, "add", "--", "AGENTS/TERRY/owned.md", "AGENTS/FOREIGN/edit.md",
            "AGENTS/FOREIGN/old.md", "PROME/ROSTER.md", *scripts)
        git(repo, "commit", "-m", "Fixture baseline")
        git(repo, "remote", "add", "origin", str(remote))
        git(repo, "push", "-u", "origin", "master")
        git(base, "clone", str(remote), str(peer))
        git(peer, "config", "user.name", "Disposable peer fixture")
        git(peer, "config", "user.email", "peer@example.invalid")

        write(repo, "AGENTS/FOREIGN/edit.md", "foreign staged\n")
        git(repo, "add", "--", "AGENTS/FOREIGN/edit.md")
        write(repo, "AGENTS/FOREIGN/edit.md", "foreign staged plus unstaged\n")
        git(repo, "mv", "--", "AGENTS/FOREIGN/old.md", "AGENTS/FOREIGN/new.md")
        with (repo / "AGENTS/FOREIGN/new.md").open("a") as out:
            out.write("foreign unstaged after staged rename\n")
        write(repo, "AGENTS/FOREIGN/in-flight.md", "foreign untracked\n")
        before = foreign(repo)
        assert b"R" in before["rename_status"] and before["cached_diff"] and before["unstaged_diff"]

        write(repo, "AGENTS/TERRY/owned.md", "owned transition\n")
        git(repo, "commit", "-m", "Exact owned transition", "--", "AGENTS/TERRY/owned.md")
        owned = text(repo, "rev-parse", "HEAD")
        assert foreign(repo) == before
        assert text(repo, "show", "--format=", "--name-only", owned) == "AGENTS/TERRY/owned.md"
        results.append({"case": "exact_path_commit_preserves_foreign_state", "result": "PASS",
                        "foreign_before": digest(before), "foreign_after": digest(foreign(repo))})

        pushed = run(repo, "bash", "scripts/safe-push.sh")
        log = (pushed.stdout + pushed.stderr).decode()
        assert "Pushed. CONFIRMED: HEAD " in log
        assert foreign(repo) == before
        assert git(repo, "merge-base", "--is-ancestor", owned, "origin/master").returncode == 0
        results.append({"case": "actual_safe_push_preserves_index_tree_and_rename", "result": "PASS",
                        "script_receipt": next(line for line in log.splitlines() if "Pushed. CONFIRMED:" in line)})

        git(peer, "pull", "--ff-only")  # disposable peer is clean, no shared working tree
        write(peer, "peer.md", "remote successor\n")
        git(peer, "add", "--", "peer.md")
        git(peer, "commit", "-m", "Later remote successor")
        git(peer, "push", "origin", "master")
        git(repo, "fetch", "origin")
        assert git(repo, "merge-base", "--is-ancestor", owned, "origin/master").returncode == 0
        counts = text(repo, "rev-list", "--left-right", "--count", "origin/master..." + owned)
        assert counts == "1\t0"
        assert text(repo, "rev-parse", "origin/master") != owned
        assert foreign(repo) == before
        results.append({"case": "delivered_commit_survives_fresh_remote_successor", "result": "PASS",
                        "origin_vs_owned_count": counts, "ancestor_rc": 0, "equality_required": False})

        write(repo, "AGENTS/TERRY/owned.md", "unpublished local transition\n")
        git(repo, "commit", "-m", "Another exact owned transition", "--", "AGENTS/TERRY/owned.md")
        blocked_before = foreign(repo)
        rejected = run(repo, "bash", "scripts/safe-push.sh", check=False)
        rejected_log = (rejected.stdout + rejected.stderr).decode()
        assert rejected.returncode == 1 and "ABORT:" in rejected_log
        assert "Pushed. CONFIRMED:" not in rejected_log
        assert foreign(repo) == blocked_before
        results.append({"case": "non_ff_stops_without_foreign_mutation", "result": "PASS",
                        "safe_push_rc": rejected.returncode, "foreign_preserved": True})

        git(repo, "remote", "set-url", "origin", str(base / "unavailable-origin.git"))
        assert git(repo, "merge-base", "--is-ancestor", owned, "origin/master").returncode == 0
        fetch = git(repo, "fetch", "origin", check=False)
        assert fetch.returncode != 0
        failed = run(repo, "bash", "scripts/safe-push.sh", check=False)
        assert failed.returncode != 0 and b"Pushed. CONFIRMED:" not in failed.stdout
        assert foreign(repo) == blocked_before
        results.append({"case": "failed_fetch_does_not_certify_stale_ancestry", "result": "PASS",
                        "fetch_rc": fetch.returncode, "current_confirmation": "UNKNOWN",
                        "stale_ancestor_rc": 0, "foreign_preserved": True})

        # Sensitivity: a staging-only mistake must be caught despite identical working bytes.
        staging_copy = base / "staging-counterexample"
        shutil.copytree(repo, staging_copy)
        original = foreign(staging_copy)
        git(staging_copy, "restore", "--source=HEAD", "--staged", "--", "AGENTS/FOREIGN")
        disturbed = foreign(staging_copy)
        assert original["working_bytes"] == disturbed["working_bytes"]
        assert original["index_entries"] != disturbed["index_entries"]
        assert original["cached_diff"] != disturbed["cached_diff"]
        assert original["rename_status"] != disturbed["rename_status"]
        results.append({"case": "fixture_detects_staging_and_rename_loss_with_unchanged_bytes",
                        "result": "PASS", "working_bytes_preserved": True,
                        "index_and_cached_diff_preserved": False, "rename_state_preserved": False})

        destructive_copy = base / "old-recipe-counterexample"
        shutil.copytree(repo, destructive_copy)
        original = foreign(destructive_copy)
        git(destructive_copy, "restore", "--source=HEAD", "--staged", "--worktree", "--", "AGENTS/FOREIGN")
        disturbed = foreign(destructive_copy)
        assert original["working_bytes"] != disturbed["working_bytes"]
        assert original["index_entries"] != disturbed["index_entries"]
        assert original["rename_status"] != disturbed["rename_status"]
        results.append({"case": "fixture_detects_retired_foreign_restore_hazard", "result": "PASS",
                        "working_bytes_preserved": False, "index_preserved": False,
                        "rename_state_preserved": False})

    report = {"validation": "AUTHOR PASS", "cases": results, "live_repo_mutated_by_fixtures": False,
              "safe_push_sha256": hashlib.sha256((ROOT / "scripts/safe-push.sh").read_bytes()).hexdigest(),
              "scope": "local disposable origin/owner/peer repositories; logical foreign staging and working state",
              "limits": "No live integration/rebase or independent acceptance; whole index bytes may legitimately change for owned commits; foreign logical entries/diffs/rename state are compared."}
    (HERE / "git-results.json").write_text(json.dumps(report, indent=2) + "\n")
    for item in results:
        print(item["result"], item["case"])
    print("7 cases passed; hold/independent acceptance not adjudicated.")


if __name__ == "__main__":
    main()
