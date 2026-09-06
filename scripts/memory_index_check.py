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

v3 (2026-09-06, DAEDALUS, PROME Tier-1 packet): THE COLD INDEX IS A FILE SET.
`memory/auto/INDEX_COLD.md` sits at 93.5% of its 51,200 B hard ceiling and the
next legal move its own header pre-registers is SHARD BY THEME into sibling
`memory/auto/INDEX_COLD_<theme>.md` files. This script hardcoded the single path,
so a sharded slug would have read as UNINDEXED and `--strict --slug <it>` would
have BLOCKED its owner's closeout on a condition carve-out (3) forbids them to
fix — the same "gate fails on what the runner cannot fix" failure recorded below
for bare --strict. The set is now resolved by scripts/memory_index_paths.py
(base + INDEX_COLD_*.md, sorted; ONE definition, shared with
memory_citation_census.py so the two guards cannot disagree — the
harness_caps.env shape, PAT-069). Slugs de-dup across members; a slug in ANY
member is INDEXED. Self-falsified by `--selftest`.

USAGE (cont.)
  python3 scripts/memory_index_check.py --selftest   # fixture drills; rc 0 pass / 1 fail
  python3 scripts/memory_index_check.py --mem-dir D  # fixture override of memory/auto

CONTRACT: advisory, read-only, <5s, no network. Never stages, writes or commits.
Exit 0 ALWAYS **unless --strict is passed** — the default is unchanged and still
matches scripts/orphan_check.sh — **with ONE v3 exception: rc 2 CANNOT-CERTIFY
when a cold-index member EXISTS BUT CANNOT BE READ** (permissions, a directory
wearing a shard's name, a dead symlink). That is not a finding and not an
internal error; it is the check's own perimeter failing, and it fails CLOSED
regardless of --strict, naming the path. Silently skipping an unreadable shard
would report "0 slugs there", which un-indexes every slug inside it and reads
identically to a shard that is genuinely empty
`[[finding_fail_loud_on_incomplete_data]]`. rc 2 is a FLAG TO PROME (the shared
index is not the tripping agent's to repair), same routing as the size flag.

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

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from memory_index_paths import (  # noqa: E402  (path shim above is deliberate)
    cold_index_files, read_cold_indexes, describe as describe_cold_set,
)

MEM_DIR = os.path.join(REPO, "memory", "auto")
INDEX = os.path.join(MEM_DIR, "MEMORY.md")
# Kept as a NAME for the single canonical base file (blame target, refs_check,
# prose). The SET is resolved at call time by cold_index_files(MEM_DIR) — never
# assume this one path is the whole cold index (v3).
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
    "MEMORY_WARN_PERCENT": "75",  # = the Will-ruled flow-rule trip line (8/12); re-keyed 8/28 with harness_caps.env — a default that disagrees with the shared file is the exact seam this block exists to close
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
    # Relative to MEM_DIR, not a hardcoded "memory/auto", so --mem-dir (fixture)
    # does not silently read the REAL repo's tracked set while claiming to
    # describe the fixture. A fixture dir outside the repo simply returns {} —
    # "nothing is committed here", which is true and says so.
    rel = os.path.relpath(MEM_DIR, REPO)
    out = sh(["git", "ls-files", rel])
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


def _collect_slugs(text, seen, ordered):
    """Append first-appearance slugs from `text` into `ordered`, de-duped via `seen`.

    Shared by the single-file (hot) and multi-file (cold set) readers so the two
    tiers can never diverge on what counts as a slug or on de-dup semantics.
    """
    for m in SLUG_RE.finditer(text):
        s = m.group(1)
        if s in SKIP_SLUGS or s in seen:
            continue
        seen.add(s)
        ordered.append(s)


def slugs_in(path):
    """Every slug referenced by ONE index file, in first-appearance order.

    Returns None if the file does not exist. For the cold base that is the
    NORMAL state until PROME's ~8/1-8/2 migration, and the caller treats it as
    empty rather than as an error (REQ 1.1). Still the reader for MEMORY.md;
    the cold tier goes through cold_slugs() because it is a FILE SET (v3).
    """
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    seen, ordered = set(), []
    _collect_slugs(text, seen, ordered)
    return ordered


def cold_slugs(mem_dir=None):
    """The COLD tier read as ONE index across its whole FILE SET (v3).

    Returns (slugs_or_None, files, unreadable):
      slugs_or_None — first-appearance order, base first then shards sorted,
                      de-duped ACROSS members; None when no cold file exists at
                      all (the pre-migration state, not an error).
      files         — the resolved member list, for reporting. A count printed
                      without the file list is unauditable.
      unreadable    — [(path, reason)]; NON-EMPTY MEANS THE CALLER MUST FAIL.
                      Members that DID read are still returned, so the report can
                      say what it managed to see — but the partial set may never
                      be used to conclude a slug is unindexed.

    The set definition lives in scripts/memory_index_paths.py, shared with
    memory_citation_census.py.
    """
    mem_dir = mem_dir or MEM_DIR
    files = cold_index_files(mem_dir)
    if not files:
        return None, [], []
    texts, unreadable = read_cold_indexes(files)
    seen, ordered = set(), []
    for text in texts:
        _collect_slugs(text, seen, ordered)
    return ordered, files, unreadable


def index_sets(mem_dir=None):
    """The two tiers exactly as forward_check unions them (hot list, cold list,
    cold file list, unreadable). Extracted so --selftest exercises the REAL
    computation rather than a re-implementation of it — a drill against a copy
    of the logic proves nothing about the logic that ships
    `[[finding_crosscheck_with_free_parameter_validates_nothing]]`.
    """
    mem_dir = mem_dir or MEM_DIR
    hot = slugs_in(os.path.join(mem_dir, "MEMORY.md"))
    cold, cold_files, unreadable = cold_slugs(mem_dir)
    return hot, cold, cold_files, unreadable


def cold_perimeter_failure(mem_dir=None):
    """Fail-closed gate (v3): cold-index members that EXIST but cannot be READ.

    Returns [(path, reason)] — empty is the clean case. Checked BEFORE any
    verdict is computed, because every downstream verdict (UNINDEXED above all)
    is a claim about the WHOLE cold set, and a partial read cannot support it.
    """
    _, _, unreadable = cold_slugs(mem_dir)
    return unreadable


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
    files = cold_index_files(MEM_DIR)
    if not files:
        return  # normal until the ~8/1-8/2 migration; silent, not an error.

    # v3: blame EVERY member of the cold set. A shard is a normal tracked file,
    # so its embed-pending promises age exactly like the base's — and a promise
    # that stopped being audited the day it was moved into a shard is the
    # sharding turning a live check off by accident.
    now, stale, total, unblamed = time.time(), [], 0, []
    for path in files:
        rel = os.path.relpath(path, REPO)
        out = sh(["git", "blame", "--line-porcelain", "--", rel])
        if not out:
            # Untracked or unreadable — report the rows without ages rather than
            # silently skipping them. A promise with an unknown age is still a promise.
            try:
                with open(path, encoding="utf-8", errors="replace") as f:
                    rows = [l for l in f if EMBED_PENDING_RE.search(l)]
            except OSError as e:
                print(f"\n  [EMBED-PENDING]  ⚠ {os.path.basename(path)} unreadable "
                      f"({e.__class__.__name__}) — ages AND rows unknown for this member.")
                continue
            if rows:
                unblamed.append((os.path.basename(path), rows))
            continue
        author_time = None
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

    for basename, rows in unblamed:
        print(f"\n  [EMBED-PENDING — {len(rows)}]  ({basename} not yet committed; ages unknown)")
        for r in rows:
            print(f"      - {r.strip()[:110]}")

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
    hot, cold, cold_files, cold_unreadable = index_sets()
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
    cold_note = describe_cold_set(len(cold), cold_files)
    print(f"  {len(slugs)} slug(s) across both indexes · {len(hot)} in MEMORY.md · {cold_note}")
    if cold_unreadable:
        # Belt and braces: main() already gates on this and returns rc 2. If a
        # future caller reaches forward_check directly, it must still not read a
        # partial cold set as a complete one.
        for path, reason in cold_unreadable:
            print(f"  ⛔ COLD-INDEX MEMBER UNREADABLE: {path} — {reason}")
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

    index_rels = {os.path.join("memory", "auto", "MEMORY.md")}
    index_rels |= {os.path.relpath(p, REPO) for p in cold_index_files(MEM_DIR)}
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


def selftest():
    """FIXTURE DRILLS for the v3 shard-aware cold tier (CHECK_STANDARD §3).

    Falsification set. Each drill is watched on a case that CAN fire and on the
    matching clean case — `py_compile` and rc=0 are not evidence a guard works.

    WHAT A PASS PROVES (PAT-074): that the cold tier resolves to base + shards,
    that a slug in ANY member reads as INDEXED, that a slug in NO member reads
    as UNINDEXED, that duplicates across members collapse, and that an
    unreadable member fails CLOSED at rc 2 end-to-end with its path named.
    It proves NOTHING about whether a shard split is sensible, whether any row
    is current, or whether the byte ceilings are respected (that is
    read_cap_check.py, per FILE — the set is never summed).
    """
    import shutil
    import tempfile

    SLUG = "finding_selftest_shard_probe"
    OTHER = "finding_selftest_base_resident"
    results = []

    def check(name, ok, detail):
        results.append((name, ok, detail))
        print(f"  {'PASS' if ok else 'FAIL'}  {name}: {detail}")

    tmp = tempfile.mkdtemp(prefix="memidx_selftest_")
    try:
        hot_p = os.path.join(tmp, "MEMORY.md")
        base_p = os.path.join(tmp, "INDEX_COLD.md")
        shard_p = os.path.join(tmp, "INDEX_COLD_test.md")

        def write(path, *slugs):
            with open(path, "w", encoding="utf-8") as f:
                f.write("# fixture\n" + "".join(f"- {x} — hook\n" for x in slugs))

        # DRILL 1 (clean/baseline) — base only, slug in the base ⇒ INDEXED.
        write(hot_p, "finding_selftest_hot_row")
        write(base_p, OTHER, SLUG)
        hot, cold, files, unreadable = index_sets(tmp)
        indexed = set(hot or []) | set(cold or [])
        check("drill1_base_only_indexed",
              SLUG in indexed and len(files) == 1 and not unreadable,
              f"{SLUG} in indexed={SLUG in indexed}, files={len(files)}, unreadable={len(unreadable)}")

        # DRILL 2 (the shard case) — SAME slug MOVED out of the base into a
        # shard ⇒ still INDEXED. This is the whole point of v3: pre-change this
        # read UNINDEXED and would have failed the owner's --strict --slug gate.
        write(base_p, OTHER)
        write(shard_p, SLUG)
        hot, cold, files, unreadable = index_sets(tmp)
        indexed = set(hot or []) | set(cold or [])
        check("drill2_moved_to_shard_still_indexed",
              SLUG in indexed and len(files) == 2 and not unreadable,
              f"{SLUG} in indexed={SLUG in indexed}, files={[os.path.basename(f) for f in files]}")

        # DRILL 3 (the negative control) — deleted from BOTH ⇒ NOT indexed.
        # Without this, drill 2 would also pass on a reader that indexes
        # everything unconditionally `[[finding_adoption_is_not_validation]]`.
        write(shard_p, "finding_selftest_unrelated")
        hot, cold, files, unreadable = index_sets(tmp)
        indexed = set(hot or []) | set(cold or [])
        check("drill3_absent_from_both_unindexed",
              SLUG not in indexed and OTHER in indexed,
              f"{SLUG} absent={SLUG not in indexed}, control {OTHER} still present={OTHER in indexed}")

        # DRILL 4 — a slug in BOTH base and shard counts ONCE (de-dup across
        # members), and ordering is base-first then shards sorted.
        write(base_p, OTHER, SLUG)
        write(shard_p, SLUG, "finding_selftest_shard_only")
        _, cold, files, _ = index_sets(tmp)
        check("drill4_dedup_across_members",
              cold.count(SLUG) == 1 and cold.index(OTHER) < cold.index("finding_selftest_shard_only"),
              f"count({SLUG})={cold.count(SLUG)}, order base-before-shard="
              f"{cold.index(OTHER) < cold.index('finding_selftest_shard_only')}")

        # DRILL 5 — an unreadable member is DETECTED, not skipped. A directory
        # wearing a shard's name is used because it is uid-independent: chmod
        # 000 is a no-op for root and would silently make this drill vacuous.
        bad_p = os.path.join(tmp, "INDEX_COLD_broken.md")
        os.mkdir(bad_p)
        unreadable = cold_perimeter_failure(tmp)
        check("drill5_unreadable_member_detected",
              any(os.path.basename(pth) == "INDEX_COLD_broken.md" for pth, _ in unreadable),
              f"unreadable={[os.path.basename(pth) for pth, _ in unreadable]}")

        # DRILL 6 (END-TO-END rc) — the same fixture through the real CLI must
        # exit 2 and NAME the path. A detector that finds the condition and
        # returns 0 is documentation
        # `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]`.
        r = subprocess.run([sys.executable, os.path.abspath(__file__), "--mem-dir", tmp],
                           capture_output=True, text=True, timeout=60)
        check("drill6_unreadable_exits_2_naming_path",
              r.returncode == 2 and "INDEX_COLD_broken.md" in r.stdout,
              f"rc={r.returncode}, path named={'INDEX_COLD_broken.md' in r.stdout}")

        # DRILL 7 (the CLEAN end-to-end line, CHECK_STANDARD §3(b)) — remove the
        # broken member and the SAME CLI must exit 0 with no perimeter line.
        os.rmdir(bad_p)
        r = subprocess.run([sys.executable, os.path.abspath(__file__), "--mem-dir", tmp],
                           capture_output=True, text=True, timeout=60)
        check("drill7_clean_case_exits_0",
              r.returncode == 0 and "COLD-INDEX MEMBER UNREADABLE" not in r.stdout,
              f"rc={r.returncode}, no perimeter line={'COLD-INDEX MEMBER UNREADABLE' not in r.stdout}")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    failed = [n for n, ok, _ in results if not ok]
    print(f"\nSELFTEST {len(results) - len(failed)}/{len(results)} passed"
          + (f" — FAILED: {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


def main():
    """Returns the process exit code."""
    global MEM_DIR, INDEX, INDEX_COLD
    args = sys.argv[1:]
    if "--selftest" in args:
        return selftest()
    if "--mem-dir" in args:
        i = args.index("--mem-dir")
        if i + 1 >= len(args):
            print("usage: memory_index_check.py --mem-dir <dir>")
            return 2
        MEM_DIR = os.path.abspath(args[i + 1])
        INDEX = os.path.join(MEM_DIR, "MEMORY.md")
        INDEX_COLD = os.path.join(MEM_DIR, "INDEX_COLD.md")
        print(f"[FIXTURE MODE] memory dir overridden → {MEM_DIR}")
        print("  git-tracking legs read this repo's index for that path, so an")
        print("  out-of-repo fixture correctly reports nothing as committed.")
    if "--refs" in args:
        i = args.index("--refs")
        if i + 1 >= len(args):
            print("usage: memory_index_check.py --refs <slug>")
            return 0
        refs_check(args[i + 1].strip().removesuffix(".md"))
        return 0

    # v3 fail-closed perimeter gate, BEFORE any verdict. Every downstream
    # verdict is a claim about the WHOLE cold set; a partial read cannot carry
    # one. Independent of --strict: this is not a finding, it is the check
    # unable to run. rc 2 = CANNOT-CERTIFY (CHECK_STANDARD §9).
    unreadable = cold_perimeter_failure()
    if unreadable:
        print("memory_index_check v3 — ⛔ CANNOT-CERTIFY: cold-index member(s) unreadable")
        print("=" * 78)
        for path, reason in unreadable:
            print(f"  ⛔ COLD-INDEX MEMBER UNREADABLE: {path}")
            print(f"     {reason}")
        print("\n  The cold index is a FILE SET (INDEX_COLD.md + INDEX_COLD_*.md). A member")
        print("  that cannot be read is NOT an empty member: skipping it would report every")
        print("  slug inside it as UNINDEXED and could fail an owner's closeout on a shard")
        print("  they never touched. No verdict is issued on a partial read.")
        print("  → FLAG TO PROME (memory/auto/ is fleet-shared, not the tripping agent's to")
        print("    repair). Fix the member, then re-run.")
        return 2

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
    # v3 adds rc 2 = CANNOT-CERTIFY, --strict or not, for an unreadable member of
    # the cold FILE SET. It is deliberately NOT folded into the rc-1 findings
    # class: rc 1 says "the index is broken", rc 2 says "I could not read the
    # index" — collapsing them would let a perimeter failure be triaged as a
    # content defect `[[finding_lenient_parser_reports_unparseable_as_a_behavior]]`.
    sys.exit(code)
