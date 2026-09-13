#!/usr/bin/env python3
"""Build a throwaway repository the gate can be run against.

WHY THIS EXISTS (CODEX, 2026-09-12 23:1x): the first version of
test_gate_isolation_L294_F7 deleted the REAL `PROME/CLOSEOUT.md`, ran the live boot
gate against the shared checkout, and restored the file from a crc-verified copy.
A `finally` and a checksum do not make that safe:

  * a terminated process skips restoration entirely;
  * restoration can overwrite another session's intervening edit;
  * the raw boot gate runs `board_scan --advance` and other writers, so restoring one
    file does not restore the other state a run may change.

This is the SECOND time this session pattern has bitten — `PROME/SCRATCH.md` already
carried the earlier instance (a test that chmod-000'd Will's real credential file).
`[[finding_regression_test_pinned_to_a_live_surface_rots_on_the_next_edit]]`

CONTRACT
  * Exports tracked files from a commit into a temp directory. The live working tree
    is never read, written, or restored.
  * `git init`s the fixture so git-dependent checks have a repo and a history of
    their own. Adds are PATHSPEC adds — `git add -A` is prohibited fleet-wide and
    `git_guard` blocks it even here, which is the guard behaving correctly.
  * Every gate write (board cursor, dashboard state, receipts) lands inside the
    fixture and dies with it.
  * Caller deletes fixture files to create the missing-input case. No production file
    is ever removed.
"""
from __future__ import annotations

import pathlib
import subprocess
import tempfile

REPO = pathlib.Path(__file__).resolve().parents[3]

# The perimeter a boot gate actually travels. AGENTS/ is 346 MB at HEAD and is
# exported as a THIN slice — the gate needs the directory names and each desk's own
# small surfaces, never the research corpora.
BULK = ["PROME", "scripts", ".claude", "docs", "MESSAGING", "BOARD",
        "HEARTBEAT.md", "AGENTS.md", "CLAUDE.md", "USER.md"]
THIN_GLOBS = ["AGENTS/*/STATUS.md", "AGENTS/*/CLAUDE.md", "AGENTS/*/CALENDAR.md",
              "AGENTS/DAEDALUS/BLUEPRINTS/*", "AGENTS/WALTER/design/*",
              "AGENTS/WALTER/registry/*", "AGENTS/WALTER/LAST_COMPLETION.md"]


def _run(args, cwd, check=True):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    if check and p.returncode != 0:
        raise RuntimeError(f"{args[:3]} rc={p.returncode}: {p.stderr[:300]}")
    return p


# Every allocation this module makes, keyed by its resolved path. `destroy()` will
# only ever clean up an entry it finds HERE.
#
# ⛔ WHY (Will, 2026-09-12 23:41, after inspecting the first version): destroy()
# guarded with `str(root).startswith(tempfile.gettempdir())`. With deletion mocked,
# that accepted `/tmp/../home/willi/Research-workspace` — a raw string prefix, no
# resolve() — which is the real repository. It also accepted bare `/tmp` and any
# path merely PREFIXED by the tempdir string, and `ignore_errors=True` meant a wrong
# deletion would report nothing. In a module whose entire thesis is "tests must not
# touch real state", a containment guard that can be walked past with `..` is the
# defect it exists to prevent. The fix is not a better string test: the fixture OWNS
# its TemporaryDirectory and cleans up that exact allocation, so an arbitrary path is
# not something destroy() can be asked to delete at all.
_OWNED: dict[pathlib.Path, tempfile.TemporaryDirectory] = {}


def build(ref: str = "HEAD") -> pathlib.Path:
    """Export `ref` into a fresh temp repo and return its root."""
    holder = tempfile.TemporaryDirectory(prefix="gate-fixture-")
    root = pathlib.Path(holder.name).resolve()
    _OWNED[root] = holder
    paths = list(BULK)
    listed = _run(["git", "ls-files", "--", *THIN_GLOBS], REPO).stdout.split()
    paths += listed
    # BINARY, deliberately: `_run` decodes as text and a tar stream is not text.
    p = subprocess.run(["git", "archive", ref, "--", *paths], cwd=REPO,
                       capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(f"git archive rc={p.returncode}: {p.stderr[:300]!r}")
    subprocess.run(["tar", "-x", "-C", str(root)], input=p.stdout, check=True)

    # Directory NAMES matter to agent_freshness even for desks whose files we skip.
    for d in _run(["git", "ls-tree", "-d", "--name-only", ref, "AGENTS/"], REPO).stdout.split():
        (root / d).mkdir(parents=True, exist_ok=True)

    _run(["git", "init", "-q", "."], root)
    # ⛔ Set the identity IN THE REPO, not only via `-c` on the first commit. Without this
    # every later `git commit` a TEST makes inside the fixture fails rc 128 "Author identity
    # unknown" — and tests that capture output without checking rc read as passing while the
    # commit never happened, so the tree under test is not the tree the test believes in.
    # Found 2026-09-13 when a round-3 case asserted a clean run over a staged-not-committed
    # overlay. (finding_test_the_guard_not_just_the_guarded.)
    _run(["git", "config", "user.email", "fixture@local"], root)
    _run(["git", "config", "user.name", "fixture"], root)
    # PATHSPEC adds only. `git add -A`/`git add .` are prohibited and git_guard
    # blocks them by command text, fixture or not — correct behaviour, not a
    # limitation to work around.
    top = sorted({q.split("/", 1)[0] for q in paths if (root / q.split("/", 1)[0]).exists()})
    _run(["git", "add", "--", *top], root)
    _run(["git", "-c", "user.email=fixture@local", "-c", "user.name=fixture",
          "commit", "-qm", "gate fixture"], root)
    return root


def run_gate(root: pathlib.Path, mode: str = "boot", *extra):
    """Run the gate INSIDE the fixture. Every write it makes stays there."""
    return subprocess.run(
        ["python3", str(root / "PROME/tools/prome_gate.py"), mode, *extra],
        cwd=root, capture_output=True, text=True)


def destroy(root) -> bool:
    """Clean up a fixture THIS MODULE allocated. Returns True if it did.

    Anything else — a path we did not create, `/tmp`, a traversal that resolves
    outside our allocations — is REFUSED and nothing is deleted. There is no
    argument that makes this delete an arbitrary directory."""
    if root is None:
        return False
    try:
        key = pathlib.Path(root).resolve()
    except OSError:
        return False
    holder = _OWNED.pop(key, None)
    if holder is None:
        return False          # not ours: refuse, delete nothing, say so
    holder.cleanup()          # removes exactly the allocation, and raises on failure
    return True


if __name__ == "__main__":
    r = build()
    print("fixture:", r)
    p = run_gate(r)
    print("rc:", p.returncode)
    print("\n".join(l for l in p.stdout.split("\n")
                    if "[ERROR" in l or "PROME GATE" in l or "DID NOT RUN" in l))
    print("stderr:", p.stderr[-400:] if p.stderr.strip() else "(clean)")
