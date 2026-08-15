#!/usr/bin/env python3
"""
memory_index_check.py — fleet-level integrity check for the auto-memory index.

v2 (2026-07-28, PROME REQ, Will-approved 2026-07-28): TWO-INDEX MODEL.
`memory/auto/MEMORY.md` stays the auto-loaded HOT index; `memory/auto/INDEX_COLD.md`
takes rare/historical/embedded rows (PROME migrates ~8/1-8/2). Until that file
exists, ABSENT IS TREATED AS EMPTY, NOT AS AN ERROR — v2 is safe to run today.

THE PROBLEM (two failure modes, opposite directions, different fixes):

  FORWARD — a dangling index pointer. An index is loaded into agents' context at
  session start. A slug listed there whose file is NOT COMMITTED is invisible to
  every other machine and every other agent, while READING as though the memory
  exists. Found live 2026-07-25: a root `.gitignore` glob (`*secret*` / `*token*`)
  silently swallowed `finding_state_token_sweep_all_surfaces.md` because the SLUG
  contained "token". The index pointed at it; git never tracked it; nobody was told.
  Sub-cases need DIFFERENT fixes and are reported separately:
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

  v2 adds the THIRD direction — FILE → INDEX. A committed memory that appears in
  NO index is the mirror of a dangling pointer: the file ships fine and no agent
  ever loads it. Nothing detected this before, because v1 only ever walked
  index → file. See EXACTLY-ONE-INDEX below.

USAGE
  python3 scripts/memory_index_check.py              # forward + reverse-coverage (all slugs)
  python3 scripts/memory_index_check.py --refs SLUG  # inbound references, pre-rename
  python3 scripts/memory_index_check.py --quiet      # only problems
  python3 scripts/memory_index_check.py --strict     # EXIT 1 on ANY sync-breaking pointer (fleet/CI gate)
  python3 scripts/memory_index_check.py --strict --slug NAME [--slug NAME ...]
                                                     # EXIT 1 only for the named memories (agent closeout gate)

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
half of that; the other half is invocation, now in root CLAUDE.md carve-out ③.

--strict fails ONLY on the sync-breaking classes (GITIGNORED, UNCOMMITTED,
UNINDEXED). MISSING and DOUBLE-LISTED stay advisory even under --strict — see
the rationale at each check.

⚠️ USE --slug FOR AN AGENT CLOSEOUT GATE. Bare --strict fails on the WHOLE index,
which is right for a fleet/CI gate and WRONG for one agent's closeout: root
CLAUDE.md carve-out ③ lets you commit only memories YOU authored, so a bare
--strict can block your closeout on another agent's orphan that you are
forbidden to fix. Found the hard way within an hour of shipping --strict — five
orphans from two other live sessions failed BROCK's own closeout, on files
carve-out ③ explicitly excluded it from touching. A gate that fails on something
the runner cannot fix trains people to bypass the gate, which is exactly the
inertia that let the always-exit-0 version rot unused. Scope it to what you wrote:
  --strict --slug finding_your_memory_name
The full index picture is still PRINTED either way; --slug only narrows what is
allowed to FAIL the run. **This applies to EVERY v2 check too** (BROCK's addendum
to the REQ, folded in by PROME the same morning): the new two-index and
exactly-one-index logic is scoped by --slug exactly as the v1 forward check is.

HOMED FLEET-LEVEL, NOT IN walter_doctor, deliberately: `memory/auto/` is
fleet-shared, so the check must be runnable at ANY agent's session, not only
WALTER's boots. walter_doctor may call it as a convenience; this script is canon.

Provenance: proposed by WALTER (gitignore packet, 2026-07-25); commissioned by
PROME with Will's ruling the same day ("build it, homed fleet-level as
scripts/memory_index_check.py, NOT inside walter_doctor"); reverse-direction
requirement added from that day's field test. Built by WALTER 2026-07-25.
--strict added by BROCK 2026-07-27. v2 (two-index + exactly-one-index + byte
warning + stale embed-pendings) built by WALTER 2026-07-28 on PROME's REQ.
"""

import os
import re
import subprocess
import sys
import time

REPO = subprocess.run(
    ["git", "rev-parse", "--show-toplevel"],
    capture_output=True, text=True,
).stdout.strip() or "."

MEM_DIR = os.path.join(REPO, "memory", "auto")
INDEX = os.path.join(MEM_DIR, "MEMORY.md")
INDEX_COLD = os.path.join(MEM_DIR, "INDEX_COLD.md")

# --- shared caps (2026-08-14) -----------------------------------------------
# Both this script AND scripts/check_memory_length.sh read from ONE source of
# truth so the two guards can never disagree on what "the cap" is. Born off
# DEWEY's 8/12 flag: the same MEMORY.md read "82% of cap" (py, when this file
# said 24,400) and "77%" (sh, at 25,600) in the SAME closeout, because each
# tool had its own local constant. PAT-069 shape: "the cap" is a concept, each
# tool resolved a different instrument. Fix = ONE file, both read.
# Root canon 1d is authoritative: 25,600 bytes / 200 lines. If the harness cap
# changes, edit scripts/harness_caps.env and both guards move together.
_CAPS_FILE = os.path.join(REPO, "scripts", "harness_caps.env")
_CAPS_DEFAULTS = {
    "MEMORY_HARNESS_CAP_BYTES": "25600",
    "MEMORY_HARNESS_CAP_LINES": "200",
    "MEMORY_WARN_PERCENT": "80",
    "MEMORY_HOOK_WARN_CHARS": "80",
}


def _load_caps():
    """Line-parse KEY=VALUE from harness_caps.env; fall back to root-canon defaults."""
    values = dict(_CAPS_DEFAULTS)
    if not os.path.exists(_CAPS_FILE):
        return values, False  # signal: caps file missing — defaults in play
    try:
        with open(_CAPS_FILE, encoding="utf-8") as f:
            for raw in f:
                line = raw.split("#", 1)[0].strip()
                if "=" not in line:
                    continue
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip()
                if k in values:
                    values[k] = v
    except OSError:
        return values, False
    return values, True


_CAPS, _CAPS_PRESENT = _load_caps()
HOT_CAP_BYTES = int(_CAPS["MEMORY_HARNESS_CAP_BYTES"])
HOT_WARN_FRACTION = int(_CAPS["MEMORY_WARN_PERCENT"]) / 100.0
HOOK_WARN_CHARS = int(_CAPS["MEMORY_HOOK_WARN_CHARS"])

# --- stale embed-pendings (REQ 1.4) -----------------------------------------
EMBED_PENDING_RE = re.compile(r"embed-pending\s*(?:→|->)\s*(\S+)")
EMBED_STALE_DAYS = 14

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


def slugs_in(path):
    """Every slug referenced by one index file, in first-appearance order.

    Returns None if the file does not exist. For INDEX_COLD.md that is the
    NORMAL state until PROME's ~8/1-8/2 migration, and the caller treats it as
    empty rather than as an error (REQ 1.1).
    """
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    seen, ordered = set(), []
    for m in SLUG_RE.finditer(text):
        s = m.group(1)
        if s in SKIP_SLUGS or s in seen:
            continue
        seen.add(s)
        ordered.append(s)
    return ordered


def hook_length_warning(scope):
    """Advisory (2026-08-14, PROME ask): warn when a named slug's inline hook
    in MEMORY.md is longer than the canon cap (~80 chars).

    Measured driver of the ~535 B/day growth in the hot index: appended hooks
    running 150–250 B against the ≤80-char canon, and NOTHING TOLD THE WRITER
    at the moment they were appending. This surfaces the length at the one
    time the author is looking. Advisory only, never fails — the canon line
    itself already exists in the index header; this just makes it visible.

    A hook is text after ` — ` immediately following the slug on the same
    row, up to the next ` · ` separator or line end. A slug with no inline
    hook (just `· slug_name`) has nothing to lint and is skipped silently.
    """
    if not scope or not os.path.exists(INDEX):
        return
    with open(INDEX, encoding="utf-8", errors="replace") as f:
        text = f.read()
    findings = []
    for slug in scope:
        # Match `slug` followed by ` — hook…` on the same line; hook ends at
        # the next ` · ` sibling separator or end of line.
        pat = re.compile(
            re.escape(slug) + r"\s+[—–-]\s+(.+?)(?=(?:\s+·\s+)|$)",
            re.MULTILINE,
        )
        m = pat.search(text)
        if not m:
            continue  # no inline hook to lint; not a defect
        hook = m.group(1).strip()
        n = len(hook)
        if n > HOOK_WARN_CHARS:
            findings.append((slug, n, hook))
    if not findings:
        return
    print(f"\n  [HOOK LENGTH — {len(findings)}]  advisory (canon ≤{HOOK_WARN_CHARS} chars)")
    print(f"    Long hooks are the measured driver of MEMORY.md's byte growth (~535 B/day).")
    print(f"    This is the one moment the author is looking — trim now, or leave it and move on.")
    for slug, n, hook in findings:
        print(f"      - {slug}  ({n} chars):  {hook[:120]}{'…' if len(hook) > 120 else ''}")


def hot_size_warning():
    """REQ 1.3 — the MECHANIZED compaction trigger.

    ⚠️ DELIBERATELY ADVISORY-ONLY, NO DISTINCT EXIT CODE. The REQ offered "a
    distinct rc if you prefer"; taking it would CONTRADICT the standing ruling
    this warning exists to encode. Will ruled 7/28 — after BOND and DEWEY both
    correctly refused a harness hook telling them to compact — that an over-size
    condition is A FLAG ROUTED TO PROME, NEVER AN INSTRUCTION TO THE AGENT THAT
    TRIPS IT. A failing exit code is an instruction: it stops the tripping
    agent's closeout and hands them a problem whose only in-scope fix is the one
    they have just been told is not theirs. So this prints and never fails.
    PROME consumes the line at its own boot, where acting on it IS in scope.
    """
    if not os.path.exists(INDEX):
        return
    size = os.path.getsize(INDEX)
    pct = size / HOT_CAP_BYTES
    threshold = int(HOT_CAP_BYTES * HOT_WARN_FRACTION)
    print("\n  [HOT-INDEX SIZE]")
    if size >= threshold:
        print(f"    ⚠ MEMORY.md is {size:,} bytes = {pct:.0%} of the {HOT_CAP_BYTES:,}-byte auto-load cap"
              f" (warn at {HOT_WARN_FRACTION:.0%} = {threshold:,}).")
        print("    → THIS IS A FLAG ROUTED TO PROME. It is NOT an instruction to compact.")
        print("      Standing ruling (Will, 2026-07-28): an over-size condition is routed to")
        print("      PROME, never actioned by the agent that trips it. Do not compact a shared")
        print("      index because a tool told you to; do not re-litigate this. Report and move on.")
    else:
        print(f"    ✓ MEMORY.md {size:,} bytes = {pct:.0%} of the {HOT_CAP_BYTES:,}-byte cap"
              f" (warn at {HOT_WARN_FRACTION:.0%}).")


def stale_embed_pendings():
    """REQ 1.4 — a cold row promising an embed that never landed.

    A row annotated `embed-pending → <target>` is a promise made to the owner of
    <target>. Unlike `embedded → <target>` (done), a pending one is a
    record-of-an-action that is not the action — the class that reads as covered
    while nothing has happened. Age comes from `git blame` on the row itself, so
    it cannot be gamed by editing elsewhere in the file.
    """
    if not os.path.exists(INDEX_COLD):
        return  # normal until the ~8/1-8/2 migration; silent, not an error.

    out = sh(["git", "blame", "--line-porcelain", "--", "memory/auto/INDEX_COLD.md"])
    if not out:
        # Untracked or unreadable — report the rows without ages rather than
        # silently skipping them. A promise with an unknown age is still a promise.
        with open(INDEX_COLD, encoding="utf-8", errors="replace") as f:
            rows = [l for l in f if EMBED_PENDING_RE.search(l)]
        if rows:
            print(f"\n  [EMBED-PENDING — {len(rows)}]  (INDEX_COLD.md not yet committed; ages unknown)")
            for r in rows:
                print(f"      - {r.strip()[:110]}")
        return

    now, author_time, stale, total = time.time(), None, [], 0
    for line in out.splitlines():
        if line.startswith("author-time "):
            try:
                author_time = int(line.split()[1])
            except (ValueError, IndexError):
                author_time = None
        elif line.startswith("\t"):  # the content line for the current blame hunk
            body = line[1:]
            if EMBED_PENDING_RE.search(body):
                total += 1
                if author_time:
                    age = (now - author_time) / 86400.0
                    if age >= EMBED_STALE_DAYS:
                        stale.append((age, body.strip()))
            author_time = None

    if not total:
        return
    if stale:
        print(f"\n  [EMBED-PENDING STALE — {len(stale)} of {total}]  promised >{EMBED_STALE_DAYS}d ago, not landed.")
        print("    A cold row saying `embed-pending → X` is a promise to X's owner. The row")
        print("    existing is not the embed happening — check the TARGET artifact, not this file.")
        for age, body in sorted(stale, reverse=True):
            print(f"      - {age:.0f}d  {body[:100]}")
    else:
        print(f"\n  [EMBED-PENDING]  ✓ {total} pending, none older than {EMBED_STALE_DAYS}d.")


def forward_check(quiet=False, scope=None):
    """Index → file, across BOTH indexes; plus file → index coverage.

    Returns the count of SYNC-BREAKING conditions.

    MISSING is intentionally excluded from the count: a forward-reference to a
    memory you intend to write later is legitimate (original design note).

    `scope` — an iterable of slugs. When given, the full picture is still
    REPORTED but only these slugs may contribute to the returned failure count.
    This is what makes the gate usable at an individual agent's closeout, where
    carve-out ③ permits committing only memories that agent authored. It applies
    to every v2 check as well as the v1 ones (BROCK's addendum).
    """
    hot = slugs_in(INDEX)
    cold = slugs_in(INDEX_COLD)
    cold_exists = cold is not None
    if hot is None and not cold_exists:
        print(f"memory_index_check: no index at {INDEX} — nothing to check.")
        return 0
    hot = hot or []
    cold = cold or []

    hot_set, cold_set = set(hot), set(cold)
    # Union, preserving first-appearance order: hot first, then cold-only.
    slugs = hot + [s for s in cold if s not in hot_set]

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

    # --- REQ 1.2: exactly-one-index -----------------------------------------
    # UNINDEXED  = a COMMITTED memory file in NEITHER index. Sync-breaking in the
    #              mirror direction: the file ships and no agent ever loads it.
    #              v1 could not see this at all — it only walked index → file.
    # DOUBLE     = in BOTH indexes. Hygiene, not sync-breaking: the memory still
    #              resolves. But it burns HOT-index bytes on a row that was moved
    #              to cold precisely to free them, so it works against the cap
    #              this restructure exists to manage. Advisory, per the same
    #              asymmetry that keeps MISSING advisory.
    # ⚠️ Filter by the CANONICAL SLUG SHAPE, not by a denylist of known non-memories.
    # v1 of this check flagged `README` as an unindexed memory on its very first
    # run — it lives in memory/auto/ and ends in .md, which was the whole test.
    # A denylist ({MEMORY, INDEX_COLD, README}) would have silenced today's case
    # and broken again on the next template, script or note anyone drops in the
    # directory. SLUG_RE already encodes what a memory IS (root CLAUDE.md's four
    # prefixes + `user`), so requiring a full match rules out every non-memory by
    # construction and stays correct as the directory grows. Third guard running
    # where v1 produced a false positive that only RUNNING it revealed.
    committed_slugs = {
        f[:-3] for f in tracked
        if f.endswith(".md") and SLUG_RE.fullmatch(f[:-3])
    }
    committed_slugs -= SKIP_SLUGS
    indexed = hot_set | cold_set
    unindexed = sorted(s for s in committed_slugs if s not in indexed)
    double = sorted(hot_set & cold_set)

    ok = len(slugs) - len(gitignored) - len(uncommitted) - len(missing)

    if scope is not None:
        scope = {s.removesuffix(".md") for s in scope}
        unknown = scope - indexed
        blocking = [s for s in (gitignored + uncommitted + unindexed) if s in scope]
    else:
        unknown, blocking = set(), gitignored + uncommitted + unindexed

    print("memory_index_check v2 — forward (index → committed file) + coverage (file → index)")
    print("=" * 78)
    if not _CAPS_PRESENT:
        print(f"  ⚠ scripts/harness_caps.env MISSING — using root-canon defaults "
              f"({HOT_CAP_BYTES}B / {HOOK_WARN_CHARS}-char hook). The bash guard will FAIL LOUD "
              f"on the same file; restore it.")
    cold_note = f"{len(cold)} in INDEX_COLD.md" if cold_exists else "INDEX_COLD.md absent (normal pre-migration)"
    print(f"  {len(slugs)} slug(s) across both indexes · {len(hot)} in MEMORY.md · {cold_note}")
    print(f"  {ok} resolve to committed files · {len(committed_slugs)} committed memory file(s) on record")

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

    if unindexed:
        print(f"\n  [UNINDEXED — {len(unindexed)}]  COMMITTED memory file in NEITHER index.")
        print("    The mirror of a dangling pointer: the file ships fine and NO AGENT EVER")
        print("    LOADS IT. Indexes are the only discovery surface — an unindexed memory is")
        print("    written, committed, pushed and inert. Add a one-line row to MEMORY.md (hot)")
        print("    or INDEX_COLD.md (rare/historical).")
        for s in unindexed:
            print(f"      - {s}")

    if double:
        print(f"\n  [DOUBLE-LISTED — {len(double)}]  in BOTH indexes (advisory).")
        print("    Not sync-breaking — it still resolves. But it spends HOT-index bytes on a")
        print("    row moved to cold precisely to free them. Drop whichever copy is wrong.")
        for s in double:
            print(f"      - {s}")

    if not (gitignored or uncommitted or missing or unindexed or double):
        print("\n  ✓ every index pointer resolves to a committed file, and every committed")
        print("    file appears in exactly one index.")
    elif not quiet:
        print("\n  Nothing was changed (read-only). Pass --strict to make this exit 1.")

    hot_size_warning()
    stale_embed_pendings()
    if scope is not None:
        hook_length_warning(scope)

    if scope is not None:
        others = (len(gitignored) + len(uncommitted) + len(unindexed)) - len(blocking)
        print(f"\n  [SCOPED] gate limited to {len(scope)} named slug(s): {len(blocking)} blocking"
              + (f"; {others} other issue(s) reported but NOT failing (not yours to commit —"
                 " root CLAUDE.md carve-out ③)." if others else "."))
        if unknown:
            print(f"  [SCOPED] ⚠ {len(unknown)} --slug name(s) appear in NEITHER index: "
                  + ", ".join(sorted(unknown)))
            print("           A memory with no index row is invisible at boot — add its one-line entry.")

    return len(blocking) + len(unknown)


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

    index_rels = {
        os.path.join("memory", "auto", "MEMORY.md"),
        os.path.join("memory", "auto", "INDEX_COLD.md"),
    }
    foreign = [p for p in hits if p not in index_rels]

    print(f"\n  ⚠ {sum(len(v) for v in hits.values())} reference(s) across {len(hits)} file(s).")
    if foreign:
        print(f"    {len(foreign)} of those files are OUTSIDE the indexes — and under the")
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

    scope = [args[i + 1] for i, a in enumerate(args) if a == "--slug" and i + 1 < len(args)]
    broken = forward_check(quiet="--quiet" in args, scope=scope or None)
    if "--strict" in args and broken:
        print(f"\n❌ FAIL (--strict): {broken} sync-breaking index condition(s).")
        print("   An index loads at every agent boot, so a dangling row advertises a memory")
        print("   whose file is absent on the other machine — and an UNINDEXED file is a")
        print("   memory no agent will ever load. Commit the file (or fix the ignore rule for")
        print("   the GITIGNORED class, or add the index row for UNINDEXED) and re-run.")
        return 1
    return 0


if __name__ == "__main__":
    try:
        code = main()
    except Exception as e:  # a broken detector must never fail a closeout by accident
        print(f"memory_index_check: non-fatal error ({e.__class__.__name__}: {e})")
        code = 0
    # Default stays exit 0 (orphan_check.sh contract). Only --strict can return 1,
    # and only for sync-breaking conditions — never for an internal error, and
    # never for the HOT-INDEX SIZE flag (that one is PROME's to action, not the
    # tripping agent's — see hot_size_warning()).
    sys.exit(code)
