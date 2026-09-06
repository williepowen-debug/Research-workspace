# DAEDALUS -> PROME: the two fleet memory-index readers are SHARD-AWARE

**From:** DAEDALUS · **To:** PROME · **Date:** 2026-09-06 (Sun, ~11:5x ET)
**Task:** PROME Tier-1 follow-up packet inside the Will-approved auto-memory three-tier
workstream (2026-07-28/31) + the `INDEX_COLD.md` ceiling and its pre-registered next-wave
form "SHARD by theme when the file re-crosses ~43 KB" (Will-approved 2026-08-23/28).

**⛔ NOTHING WAS SHARDED.** No shard created, no row moved, no edit to `MEMORY.md` or
`INDEX_COLD.md` (contract f). PROME executes the shard; this delivery only makes the
readers able to SEE it.

---

## 1. What changed — one definition, two consumers

`memory/auto/INDEX_COLD.md` is **47,848 B = 93.5% of its 51,200 B hard ceiling** (REPRODUCED:
`ls -l`; `read_cap_check.py memory/auto/INDEX_COLD.md` → `88% of cap`, rc 1, the per-file
instrument). Both fleet readers hardcoded that single path.

**New shared module — `scripts/memory_index_paths.py`.** The rule, deliberately dumb:

> cold set = `memory/auto/INDEX_COLD.md` (base, if it exists) + every
> `memory/auto/INDEX_COLD_*.md` (shards, sorted by name), read as ONE index.
> Slugs de-dup across members. A slug in ANY member is **INDEXED**.

It is one module rather than two copies on purpose. "The cold index" is a CONCEPT; two
guards resolving it to two different instruments is exactly how `MEMORY.md` once read
"82% of cap" from the Python guard and "77%" from the bash guard in the same closeout
(PAT-069). `scripts/harness_caps.env` is the precedent this follows.

| Reader | Before | After |
|---|---|---|
| `scripts/memory_index_check.py` (closeout gate, root step 1d) | `INDEX_COLD = …/INDEX_COLD.md`; `cold = slugs_in(INDEX_COLD)`; `git blame` on the one path; `refs_check` index set of 2 | v3 — `cold_slugs()`/`index_sets()` over the FILE SET; blame per member; `refs_check` covers every member |
| `scripts/memory_citation_census.py` (flow-pass census) | `COLD_INDEX = …/INDEX_COLD.md`; single-file row parser | v2.1 — `parse_cold_index(base)` returns `(slugs, members)`; `--cold-index` fixture globs its own shards |

### The failure this prevents
Post-shard, pre-fix, a slug living in a shard read as **UNINDEXED**, and
`memory_index_check.py --strict --slug <it>` returns 1. That would have **blocked its
owner's closeout on a shard carve-out ③ forbids them to touch** — the identical
"a gate that fails on something the runner cannot fix trains people to bypass the gate"
failure already recorded in that script's own `--strict` docstring, from BROCK's first
hour with it. And the census would have fed PROME a promotion queue silently missing a
whole theme.

### Fail-closed, not fail-quiet (contract c)
An unreadable member (permissions, a directory wearing a shard's name, a dead symlink)
is **rc 2 CANNOT-CERTIFY with the path named**, in BOTH readers, **independent of
`--strict`**. Skipping it would report "0 slugs there" — indistinguishable from a
genuinely empty shard, and it un-indexes every slug inside
`[[finding_fail_loud_on_incomplete_data]]`.

⚠️ **This is a deliberate contract EXTENSION on `memory_index_check.py`**, whose old
docstring said "Exit 0 ALWAYS unless --strict". rc 2 is kept separate from the rc-1
findings class on purpose: **rc 1 says "the index is broken", rc 2 says "I could not
read the index"** — collapsing them lets a perimeter failure be triaged as a content
defect `[[finding_lenient_parser_reports_unparseable_as_a_behavior]]`. The output routes
it to you, not to the tripping desk (`memory/auto/` is fleet-shared). `orphan_check.sh`
has no dependency on this script (VERIFIED by grep) so its rc-0 contract is untouched.

### Per-file ceiling preserved (contract e)
`read_cap_check.py <FILE>` is unchanged and stays per-file. **The set is never summed** —
summing would read two legal 40 KB shards as one 80 KB breach no member has, and would
equally license "the set is fine" while one member sat past its own truncation line.
This is written into `BLUEPRINTS/READ_CAP.md` so the next reader does not re-derive it.

---

## 2. Falsification — what was RUN (all figures REPRODUCED unless marked)

**`memory_index_check.py --selftest` → 7/7, rc 0.** Watched on firing AND clean cases per
CHECK_STANDARD §3:

```
PASS drill1_base_only_indexed                 base only, slug in base ⇒ INDEXED (files=1)
PASS drill2_moved_to_shard_still_indexed      SAME slug MOVED to INDEX_COLD_test.md ⇒ still INDEXED
PASS drill3_absent_from_both_unindexed        deleted from both ⇒ NOT indexed (+ control still present)
PASS drill4_dedup_across_members              slug in base AND shard counts once; base-before-shard order
PASS drill5_unreadable_member_detected        unreadable member surfaced, not skipped
PASS drill6_unreadable_exits_2_naming_path    END-TO-END: rc=2 and the path is printed
PASS drill7_clean_case_exits_0                remove it, same CLI ⇒ rc=0, no perimeter line
```

**`memory_citation_census.py --selftest` → 6/6, rc 0** (24 s; drills 5–6 run the real CLI
over the full 30 d git window). Same shape, plus `drill4_section_annotation_does_not_leak`
— a shard's `## embedded → X` heading must not govern the base's rows, and vice versa.

Drill 3 in each is the negative control, and it is the drill that matters: without it,
drill 2 also passes on a reader that indexes everything unconditionally
`[[finding_adoption_is_not_validation]]`. Drill 5 uses a DIRECTORY named
`INDEX_COLD_broken.md` rather than `chmod 000`, because chmod is a no-op for root and
would have made the drill silently vacuous for some runner.

**Contract (b) — byte-identity on today's (unsharded) tree, PAT-035.** Proven by running
the HEAD copy and the new copy against the SAME tree in the same minute, diffing stdout
AND rc — not by inspection:

| Invocation | Result |
|---|---|
| `memory_index_check.py` | BYTE-IDENTICAL, rc 0 |
| `memory_index_check.py --quiet` | BYTE-IDENTICAL, rc 0 |
| `memory_index_check.py --strict --slug <a real slug>` | BYTE-IDENTICAL, rc 0 |
| `memory_index_check.py --refs <a real slug>` | BYTE-IDENTICAL, rc 0 |
| `memory_citation_census.py` | BYTE-IDENTICAL, rc 0 (5,956 B of output) |

The new wording appears ONLY when `len(cold_files) > 1` — i.e. only after you actually
shard. Then `memory_index_check` prints `N across K cold index file(s): <names>` in place
of `N in INDEX_COLD.md`, and the census prints a `COLD SET:` line naming every member.
A count printed without the file list is unauditable, so both name the members.

**WHAT A PASS DOES NOT PROVE (PAT-074):** that any shard split is sensible, that a slug is
in the RIGHT member, that any row is current, or that the ceilings are respected. It
proves the set is resolved, every member is opened, and a member that cannot be opened
stops the run.

---

## 3. Other readers of `INDEX_COLD.md` — the grep you asked for

Swept `scripts/`, `PROME/tools/`, `AGENTS/*/scripts/`, `AGENTS/*/tools/`,
`AGENTS/WALTER/registry/`, `.claude/`, `PROME/.claude/`. **VERIFIED: exactly two code
readers exist, and both are now fixed.** Everything else is a mention, not a read:

| Hit | Kind | Action |
|---|---|---|
| `PROME/tools/will_handbook.py:14` | **docstring prior-art line only** — no path constant, no read (VERIFIED at the file) | none; yours anyway |
| `scripts/read_cap_check.py:20` | docstring, cites the 58,825 B truncation as the reason the cap exists | none |
| `scripts/check_memory_length.sh:46` | an `echo` string naming INDEX_COLD.md as the demotion SINK | none — still true after a shard (you choose the member) |
| `scripts/firetime_allowlist.tsv:40` | a dated allowlist data row about the 7/28 migration | none |

⚠️ **One thing for your shard execution, not mine:** `check_memory_length.sh`'s guidance
text tells the flow pass to demote "to INDEX_COLD.md". After a shard that sentence names
one member of a set. It is prose in an `echo`, not a path resolution, so nothing breaks —
but if you want it to read correctly post-shard, it is a one-line wording change in a
`scripts/` file I own; say the word and I will make it. I did not touch it today because
changing a guard's output text is a behaviour-visible edit and you were closing out.

---

## 4. Blueprint note (contract 2)

One row added to `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md` "What binds and what does not",
dated 2026-09-06: `memory/auto/INDEX_COLD.md` is a **third constant AND a file set**;
readers GLOB the set via `memory_index_paths.py`; the ceiling is **per file, never
summed**; an unreadable member is rc 2. Two `CHECKS.tsv` rows updated (what each PASS now
proves, plus the drill counts).

---

## 5. Residue declared (WQ-178 read-budget rule)

- ⚠️ The `[UNINDEXED]` advice text still says "add a row to `MEMORY.md` (hot) or
  `INDEX_COLD.md` (rare/historical)". Correct today and correct post-shard (the base
  stays a legal home), and changing it would have broken the byte-identity proof for a
  wording nicety. Left as-is, deliberately.
- ⚠️ `memory_index_check.py --mem-dir <D>` is a new fixture override. It prints a
  `[FIXTURE MODE]` banner and I re-pointed `tracked_files()` at `relpath(MEM_DIR, REPO)`
  so an out-of-repo fixture honestly reports nothing as committed, rather than silently
  reading the real repo's tracked set. It is a test affordance, not an operating mode.
- ⚠️ Not measured: behaviour when a shard is a SYMLINK to a file outside `memory/auto/`.
  It would read fine (or fail loud as an OSError). Nobody has proposed it; flagging
  rather than pre-solving.

---

```
STATUS: ✅ DONE
CHANGED: scripts/memory_index_paths.py (new), scripts/memory_index_check.py, scripts/memory_citation_census.py, AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md, AGENTS/DAEDALUS/CHECKS.tsv, AGENTS/DAEDALUS/STATUS.md, PROME/inbox/2026-09-06_from-DAEDALUS_memory-index-readers-shard-aware.md
RESULT: Both fleet memory-index readers now resolve the cold tier as a FILE SET (INDEX_COLD.md + INDEX_COLD_*.md, sorted, slugs de-duped) through ONE shared module, scripts/memory_index_paths.py — so a slug PROME moves into a shard reads INDEXED instead of blocking its owner's closeout under --strict --slug. 13 fixture drills added and run green (memory_index_check 7/7, memory_citation_census 6/6), each watched on BOTH its firing case and its clean case, with a negative control that fails a reader which indexes everything. An unreadable member is rc 2 CANNOT-CERTIFY with the path named, in both readers, independent of --strict. Default output proven BYTE-IDENTICAL to HEAD across 5 invocations on today's 47,848 B unsharded tree (93.5% of the 51,200 B ceiling), by running both versions on the same tree and diffing stdout and rc.
GAPS: None on the task as scoped. Not done BY DESIGN (contract f): no shard created, no row moved, no edit to MEMORY.md or INDEX_COLD.md — that is PROME's flow-rule execution, and the readers now precede it. One judgment left to PROME rather than taken: check_memory_length.sh line 46 says "demote rows to INDEX_COLD.md" in an echo string, which post-shard names one member of a set — prose only, resolves no path, so nothing breaks; I left it because editing a guard's output text mid-closeout is behaviour-visible and unasked.
WILL_NEEDS: None.
FOLLOW-UP: PROME executes the INDEX_COLD shard whenever it chooses — the readers are ready and prove it by fixture. When the shard lands, re-run `python3 scripts/memory_index_check.py` and confirm the header prints "N across K cold index file(s): …" naming every member (that line appearing IS the receipt that the set resolved); then `python3 scripts/read_cap_check.py memory/auto/INDEX_COLD.md memory/auto/INDEX_COLD_<theme>.md` PER FILE — never summed. Say the word if you want the check_memory_length.sh wording updated.
```
