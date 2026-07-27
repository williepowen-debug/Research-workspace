#!/usr/bin/env python3
"""
memory_index_check.py — fleet-level integrity check for the auto-memory index.

THE PROBLEM (two failure modes, opposite directions, different fixes):

  FORWARD — a dangling index pointer. `memory/auto/MEMORY.md` is the index
  loaded into every agent's context at session start. A slug listed there whose
  file is NOT COMMITTED is invisible to every other machine and every other
  agent, while READING as though the memory exists. Found live 2026-07-25: a
  root `.gitignore` glob (`*secret*` / `*token*`) silently swallowed
  `finding_state_token_sweep_all_surfaces.md` because the SLUG contained
  "token". The index pointed at it; git never tracked it; nobody was told.
  Note the two sub-cases need DIFFERENT fixes and are reported separately:
    - GITIGNORED  → fix the ignore rule (a commit will not help; `git add`
                    silently no-ops without -f)
    - UNCOMMITTED → just commit it
    - MISSING     → the file does not exist at all; write it or drop the row

  REVERSE — an unchecked blast radius before a rename/retire. The same 7/25
  incident nearly produced a second one: the proposed fix was to RENAME the
  slug, and a repo-wide grep found it referenced in FIVE agent-owned files
  (DAEDALUS PATTERNS.tsv, LABOR/REGINALD/FALCON CLAUDE.mds, a LABOR memo). The
  rename would have broken links the renaming agent could not edit. The
  original blast-radius check covered the IGNORE surface, not the REFERENCE
  surface. `--refs <slug>` is that missing check.

USAGE
  python3 scripts/memory_index_check.py              # forward check (all slugs)
  python3 scripts/memory_index_check.py --refs SLUG  # reverse check, pre-rename
  python3 scripts/memory_index_check.py --quiet      # only problems
  python3 scripts/memory_index_check.py --strict     # EXIT 1 on a sync-breaking pointer

CONTRACT: advisory, read-only, <5s, no network. Never stages, writes or commits.
Exit 0 ALWAYS **unless --strict is passed** — the default is unchanged and still
matches scripts/orphan_check.sh.

WHY --strict EXISTS (added 2026-07-27 by BROCK, Will-directed). Detection was
never the problem: on 2026-07-27 this script correctly found SIX distinct
orphaned memories across the day, from four different agents. It caught every
one and nothing happened, for two compounding reasons:
  (1) it always exited 0, so no closeout, hook or CI could ever be failed by it;
  (2) NOTHING INVOKED IT. A repo-wide grep that day returned only prose mentions
      in STATUS/handoff/log files — no protocol, hook or script called it.
A detector that cannot fail and is never run is documentation. `--strict` closes
half of that; the other half is invocation, which belongs in the callers' own
closeout protocols (BROCK wired it into AGENTS/BROCK/CLAUDE.md §12 the same day).

--strict fails ONLY on the sync-breaking classes (GITIGNORED, UNCOMMITTED).
MISSING stays advisory even under --strict, deliberately: the original design
notes that a forward-reference to a memory you intend to write later is
legitimate, and that judgement is preserved.

HOMED FLEET-LEVEL, NOT IN walter_doctor, deliberately: `memory/auto/` is
fleet-shared, so the check must be runnable at ANY agent's session, not only
WALTER's boots. walter_doctor may call it as a convenience; this script is canon.

Provenance: proposed by WALTER (gitignore packet, 2026-07-25); commissioned by
PROME with Will's ruling the same day ("build it, homed fleet-level as
scripts/memory_index_check.py, NOT inside walter_doctor"); reverse-direction
requirement added from that day's field test. Built by WALTER 2026-07-25.
"""

import os
import re
import subprocess
import sys

REPO = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True,
).stdout.strip() or "."

MEM_DIR = os.path.join(REPO, "memory", "auto")
INDEX = os.path.join(MEM_DIR, "MEMORY.md")

# The four canonical auto-memory prefixes (root CLAUDE.md "Memory" section).
SLUG_RE = re.compile(r"\b((?:finding|feedback|project|reference|user)_[a-z0-9_]+)\b")

# Rows that are prose about the index rather than pointers to a memory.
SKIP_SLUGS = {"user_email"}


def sh(args, cwd=REPO):
    """Run a command, return stdout ('' on any failure). Never raises."""
    try:
        r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, timeout=20)
        return r.stdout
    except Exception:
        return ""


def tracked_files():
    out = sh(["git", "ls-files", "memory/auto"])
    return {os.path.basename(p) for p in out.splitlines() if p.strip()}


def ignored(relpath):
    """True if the path is excluded by a gitignore rule."""
    try:
        r = subprocess.run(
            ["git", "check-ignore", "-q", relpath],
            cwd=REPO, capture_output=True, timeout=10,
        )
        return r.returncode == 0
    except Exception:
        return False


def index_slugs():
    """Every slug referenced by the index, in first-appearance order."""
    if not os.path.exists(INDEX):
        return None
    with open(INDEX, encoding="utf-8", errors="replace") as f:
        text = f.read()
    seen, ordered = set(), []
    for m in SLUG_RE.finditer(text):
        s = m.group(1)
        if s in SKIP_SLUGS or s in seen:
            continue
        seen.add(s)
        ordered.append(s)
    return ordered


def forward_check(quiet=False):
    """Returns the count of SYNC-BREAKING pointers (gitignored + uncommitted).

    MISSING is intentionally excluded from the count: a forward-reference to a
    memory you intend to write later is legitimate (original design note).
    """
    slugs = index_slugs()
    if slugs is None:
        print(f"memory_index_check: no index at {INDEX} — nothing to check.")
        return 0

    tracked = tracked_files()
    on_disk = set(os.listdir(MEM_DIR)) if os.path.isdir(MEM_DIR) else set()

    gitignored, uncommitted, missing = [], [], []
    for slug in slugs:
        fname = slug + ".md"
        if fname in tracked:
            continue
        rel = os.path.join("memory", "auto", fname)
        if fname in on_disk:
            (gitignored if ignored(rel) else uncommitted).append(slug)
        else:
            missing.append(slug)

    ok = len(slugs) - len(gitignored) - len(uncommitted) - len(missing)

    print("memory_index_check — forward (index → committed file)")
    print("=" * 68)
    print(f"  {len(slugs)} slug(s) referenced in MEMORY.md · {ok} resolve to committed files")

    if gitignored:
        print(f"\n  [GITIGNORED — {len(gitignored)}]  on disk but EXCLUDED by a gitignore rule.")
        print("    A commit will NOT fix these: `git add` silently no-ops without -f.")
        print("    FIX THE IGNORE RULE, then commit. This is the class that hid")
        print("    finding_state_token_sweep_all_surfaces (slug contained 'token').")
        for s in gitignored:
            print(f"      - {s}")

    if uncommitted:
        print(f"\n  [UNCOMMITTED — {len(uncommitted)}]  on disk, tracked by nothing. Just commit them.")
        print("    Until then they exist on ONE machine and no other agent can read them.")
        for s in uncommitted:
            print(f"      - {s}")

    if missing:
        print(f"\n  [MISSING — {len(missing)}]  indexed but NO FILE EXISTS.")
        print("    Either the memory was never written, or it was deleted without")
        print("    removing its index row. A forward-reference to a memory you intend")
        print("    to write later is legitimate — check before deleting the row.")
        for s in missing:
            print(f"      - {s}")

    if not (gitignored or uncommitted or missing):
        print("\n  ✓ every index pointer resolves to a committed file.")
    elif not quiet:
        print("\n  Nothing was changed (read-only). Pass --strict to make this exit 1.")

    return len(gitignored) + len(uncommitted)


def refs_check(slug):
    """Reverse direction: who points AT this slug? Run BEFORE any rename/retire."""
    print(f"memory_index_check — reverse (inbound references to '{slug}')")
    print("=" * 68)

    hits = {}
    # -F: the slug is a literal, not a pattern. Search tracked files only.
    out = sh(["git", "grep", "-n", "-F", slug, "--", "."])
    self_file = os.path.join("memory", "auto", slug + ".md")
    for line in out.splitlines():
        parts = line.split(":", 2)
        if len(parts) < 3:
            continue
        path, lineno, body = parts
        if path == self_file:
            continue  # the memory naming itself is not an inbound reference
        hits.setdefault(path, []).append((lineno, body.strip()))

    if not hits:
        print(f"\n  ✓ no inbound references. '{slug}' is safe to rename or retire.")
        return

    index_rel = os.path.join("memory", "auto", "MEMORY.md")
    foreign = [p for p in hits if p != index_rel]

    print(f"\n  ⚠ {sum(len(v) for v in hits.values())} reference(s) across {len(hits)} file(s).")
    if foreign:
        print(f"    {len(foreign)} of those files are OUTSIDE memory/auto/ — and under the")
        print("    fleet pathspec rule you likely CANNOT edit them. A rename breaks links")
        print("    you cannot repair. This is exactly why the 7/25 rename was DROPPED in")
        print("    favour of fixing the ignore rule instead.")
    for path, entries in sorted(hits.items()):
        print(f"\n    {path}  ({len(entries)})")
        for lineno, body in entries[:3]:
            print(f"      {lineno}: {body[:110]}")
        if len(entries) > 3:
            print(f"      … {len(entries) - 3} more")

    print("\n  Before renaming or retiring: re-point every file above, or don't rename.")


def main():
    """Returns the process exit code."""
    args = sys.argv[1:]
    if "--refs" in args:
        i = args.index("--refs")
        if i + 1 >= len(args):
            print("usage: memory_index_check.py --refs <slug>")
            return 0
        refs_check(args[i + 1].strip().removesuffix(".md"))
        return 0

    broken = forward_check(quiet="--quiet" in args)
    if "--strict" in args and broken:
        print(f"\n❌ FAIL (--strict): {broken} index pointer(s) name a memory git will not ship.")
        print("   MEMORY.md loads at every agent boot, so on another machine these rows")
        print("   advertise memories whose files are absent. Commit them (or fix the")
        print("   ignore rule for the GITIGNORED class) and re-run.")
        return 1
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as e:  # a broken detector must never fail a closeout by accident
        print(f"memory_index_check: non-fatal error ({e.__class__.__name__}: {e})")
        code = 0
    # Default stays exit 0 (orphan_check.sh contract). Only --strict can return 1,
    # and only for sync-breaking pointers — never for an internal error.
    sys.exit(code)
