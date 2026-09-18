# Independent read — SPAWN PROTOCOL compaction (blind reader, read-only)

**Date:** 2026-09-17 · **Reader:** independent Opus session, no edits made · **Objects:** ORIGINAL `/tmp/claude-1000/spawn_orig.md` (7,541 B) · COMPACT `/tmp/claude-1000/spawn_compact.md` (6,260 B) · plan `AGENTS/DAEDALUS/design/2026-09-17_SPAWN_PROTOCOL_COMPACTION_PLAN.md` §1/§3/§4.

**Provenance verified before reading:** the ORIGINAL file is byte-identical to the live `AGENTS/DAEDALUS/CLAUDE.md` § SPAWN PROTOCOL (`diff` clean). Independently recomputed: orig = 7,541 B, crc32 **1151981870** — both match the plan's claim and the crc the COMPACT's tail pointer asserts for block 6. Compact = 6,260 B (−17.0%), matching §1.

---

## A. FAIL rows

| Row | Original fragment | What the compact does | Severity |
|---|---|---|---|
| **24** | `+ regenerate `PATTERNS_HOT.md` if PATTERNS.tsv changed` (conservation-checked) — **no path named** | Substitutes a named path: **`scripts/regen_patterns_hot.py`**. **That file does not exist.** `git ls-files \| grep regen_patterns` returns exactly one path: `AGENTS/DAEDALUS/scripts/regen_patterns_hot.py`; repo-root `scripts/regen_patterns_hot.py` is absent. `CHECKS.tsv:29` registers the agent-local path as canonical. In this bullet list the sibling entries are repo-root-qualified (`scripts/read_cap_check.py` = "the ROOT tool", `scripts/safe-push.sh` = root) or fully qualified (`AGENTS/DAEDALUS/scripts/complete_check.py`), so a bare `scripts/` here reads as repo-root and a stranger running it from repo root gets `No such file or directory`. | **MED-HIGH** |
| **22** | Battery order in the original: root 1b–1e → **`scripts/safe-push.sh`** → re-cut FLEET_MAP row → regen PATTERNS_HOT → read_cap_check → complete_check → verify-push paragraph. safe-push sits **second**. | Compact moves the push to the **last** operational bullet (after complete_check) and adds an explicit preceding step, `commit path-scoped`. Same tool, same flags; **different position in the sequence**. Judged against the brief's rule ("re-ordering … is a FAIL") this is a re-order. It is a **repair, not a weakening** — the original was internally incoherent (push at position 2, verify-push at the end, with three checks in between), and running the checks before the push is what the checks are for. But plan §1 says "Nothing else changes meaning," and a battery's order is meaning. | **LOW** (benign; wants declaring) |

**PASS: 31 of 33.**

### Notes on rows that passed but moved
- **Row 4** — "Cold ≠ unwatched" is promoted out of a parenthetical into the bold body. Same three readers named (`sweeps_due.py` SELF-ROW, Production Review, co-registration guard). Emphasis up, action identical. PASS.
- **Row 8** — "the guard is the promise; the prose is only its label" → "The byte guard on every boot read is `read_cap_check.py` at closeout (step 9), never this line's promise." Reworded, adds a correct cross-reference. A stranger acts identically. PASS.
- **Row 10** — compact adds "(… also carries the profile-clock, SELF-ROW and DIRECTORY-STALE lines)". **Independently verified true**: `sweeps_due.py` emits `⏰ SELF-ROW`, `⏰ DIRECTORY-STALE`, and shells `profile_clock_check.py`. Accurate, but it is a third addition — see §C.
- **Row 17** — command byte-identical. Drops the descriptive clause "keeps `FLEET_DIRECTORY.md` in sync" and says "regenerate the directory" rather than "the readable directory"; the target filename is named in step 2 and by the guard warning. Cosmetic. PASS.
- **Row 21** — original says "steps **1b–1e** by name" (a range that already contains 1c-bis) and then enumerates 1b·1c·1e·1d. The compact enumerates 1b·1c·**1c-bis**·1d·1e — i.e. it makes the range explicit and restores root's own numeric order. Not an expansion of scope; the range already bound it. PASS.
- **Row 25/26** — command, `--agent` flag, two-tool warning, standing basename rule and the ⛔ never-raise clause all preserved. Verified root `scripts/read_cap_check.py` does take `--agent` (usage block lines 58–60). One pointer is dropped — see §B item 2.
- **Row 28** — compact names a third rc-gating leg, EVOLUTION-placement. **Independently verified true**: `complete_check.py` leg (iv) "EVOLUTION PLACEMENT [mechanical, gates rc; added 2026-08-21]". This corrects a stale description in the original. Accurate, but undeclared in §1 — see §C.
- **Rows 29/30/32** — verify_push command, the three-state rc contract (0/1/2), the retry, the concurrent-git reason and the `git show origin/master:<path> | md5sum` content check are all present with identical text. Verified the script's own header declares the same contract.

---

## B. Live clauses in the ORIGINAL not covered by the 35-row checklist

**I walked the original line by line (18 lines, clause by clause within each numbered step).** Four items are not enumerated by §3. None is a command, order, or rc value. Two carry weak prescriptive force; two are pointers.

1. **Step 7 — "don't restate."** Original: *"record at `outbox/delivered/`'s FROZEN banner, **don't restate**."* The checklist's row 15 covers the STRUCK fact and the pointer, not the instruction. The compact writes *"its record is `outbox/delivered/`'s FROZEN banner"* — it **complies** with the dropped instruction but no longer **issues** it, so a future editor is not told to keep the record single-homed. Class: authority (weak). Severity **LOW**.
2. **Step 2 — the corrected archive address for the EVOLUTION entry.** Original: *"(Re-homed 2026-08-23 → EVOLUTION (c), now `archive/EVOLUTION_ARCHIVE_2026-09.md` block 1."* The compact drops it and keeps only "*Story → `archive/CLAUDE_ARCHIVE_2026-09.md` block 4*". **This degrades a pointer chain**: `CLAUDE_ARCHIVE` block 4's own text points at "full record → `EVOLUTION.md` (c)", and I verified live `EVOLUTION.md` no longer carries a 2026-08-23 entry — (c) was rotated into `EVOLUTION_ARCHIVE_2026-09.md` block 1. So after the compaction the charter → block 4 path **dead-ends on a stale pointer**; the correct address survives only inside block 6 (which is the verbatim original), i.e. two hops. Against §1's promise "Every pointer in it resolves," this is the one soft spot. Fix is one of: keep the archive address inline in step 2, or correct block 4's internal pointer. Severity **LOW-INFO**.
3. **Step 3 — "a generated file cannot be rotated."** From the dropped 9/03 parenthetical. This is a standing design constraint (it tells you what you may *not* do when `PATTERNS_HOT.md` grows: split the row set, don't rotate the file), not merely provenance. It is not in §3's rows and not in §3's "moved to archive" list either. Its practical bite is small — the split is already executed and `read_cap_check` is the live guard. Severity **LOW**.
4. **Step 9 — the retracted one-liner DO-NOT.** *"The bare one-liner this line used to prescribe (`git merge-base --is-ancestor <hash> origin/master`) is WRONG…"* Read strictly this is narrative (how the rule was earned) and correctly archived. Read as a negative prescription, it is a DO-NOT that no longer appears anywhere live: an agent who knows the one-liner from another surface loses the warning. Mitigated because the compact prescribes the correct tool and never mentions the one-liner. Severity **INFO**.

Zero command / order / rc-value / threshold clauses are uncovered. Every executable string in the original — the four `python3 …` invocations, the `bash …verify_push.sh` invocation, the `grep -P '^AGENT\t'`, the `git show … | md5sum`, the `--receipt/--action` enum, `--agent DAEDALUS`, and the three rc contracts — appears in the compact with identical text, and is enumerated by §3.

---

## C. Rows 34, 35, 31 — and every undeclared meaning change

**Row 35 (step 3b, inbox read) — is what the plan says, and slightly more.** It is a new numbered step, openly flagged in the text itself. Two clauses ride with it that §1 does not spell out: *"every packet present, **whole**"* and *"**disposition each before idling**."* Both are consistent with the existing step 8 ("never idle holding") and with standing practice, but "whole" is a read-scope commitment on an unbounded directory and "disposition each" is an obligation gate on idling. If Will is approving an addition, these are the two words being approved. Verdict: **as declared, plus two riders worth naming.**

**Row 34 (step 9 report form) — is what the plan says, plus a scope widening.** The report form RAN · NOT-APPLICABLE(with reason) · FAILED · UNKNOWN is exactly CATO #5. But the same new lead line also hoists **"by name"** from the root-1b–1e sub-clause to *"run **every step** by name"* — the original only required naming for the root closeout steps. That is a strengthening of scope on every other battery item. Benign and probably intended; undeclared. Verdict: **as declared + one undeclared widening.**

**Row 31 (verify_push re-scoping) — is what the plan says, in a strengthening direction.** Original: *"Verify by commit SUBJECT, not hash — a rebase rewrites unpushed hashes … **Add** a content check (`git show …`) on files you care about."* Compact: *"The subject LOCATES the commit …; **IDENTITY is** the content check."* This is CATO #4 as described. Note the direction: the content check moves from an **optional adjunct** ("Add …") to the **determining test** of identity. That raises the bar, does not lower it, and the command is unchanged. Secondary: the explicit prohibition *"not hash"* becomes implicit (the compact keeps the reason — "a rebase rewrites unpushed hashes" — and the script's own interface takes a subject). Verdict: **as declared; flagging that "re-scope" understates it — it is also a strengthening.**

**Other meaning changes the plan does NOT declare** (beyond the two already tabled as FAIL rows 22/24):
- **§1 says "Two ADDITIONS are made and declared"; I count five changes of substance beyond the two.** Rows 10 (`sweeps_due.py` now names three carried lines), 28 (complete_check's third rc-gating leg), 21 (1c-bis made explicit) and 22's `commit path-scoped` are each factually correct and each verified against the artifact — but four of them are disclosed only in §3's table cells, and one (`commit path-scoped`) in neither. The honest count for Will is: **2 declared additions + 1 declared re-scoping + 4 accurate-but-undeclared corrections/additions + 1 undeclared re-order + 1 broken new path.**
- Direction of every undeclared change except row 24 is *toward* the artifact (they make the charter match what the scripts actually do). None weakens an authority clause. No ⛔ / ⚠️ / "never" clause in the original is absent from the compact: I checked all of them individually — *never hand-edit FLEET_DIRECTORY* (kept, twice), *never raise the budget / the read cap is not ours to move* (kept verbatim), *never idle holding* (kept verbatim), *never this line's promise* (kept), *never read cannot-certify as absent* (kept, and made explicit where the original left it as a story), *NOT a boot read* (kept), *two tools may not share a basename* (kept).

---

## D. The clause I would most expect this compaction to lose

**The ⚠️ two-tool basename warning on `read_cap_check.py`** — a six-line defensive aside hanging off a one-line command, written in the retracted-diagnosis voice a compaction is built to strip, and the single most archive-shaped block in the section.

**It was not lost.** The command, the `--agent` flag, the local-namesake explanation and the standing rule ("two tools may not share a basename across `scripts/` and `AGENTS/<NAME>/scripts/`") all survive in step 9 bullet 4.

**The sting:** the class of error that warning exists to prevent was **newly introduced two bullets above it**, in this same compaction. Bullet 3 now names `scripts/regen_patterns_hot.py` — a bare `scripts/` basename whose only real home is `AGENTS/DAEDALUS/scripts/`, sitting in the one bullet list on the fleet that warns about exactly this ambiguity. The compaction preserved the rule and broke it in the adjacent line. That is PAT-050 / the charter's own rule-applies-to-its-own-artifact clause (row 33), firing on the artifact that carries it.

---

## Pointer check (mechanical)

| Pointer in the COMPACT | Resolves? |
|---|---|
| `archive/CLAUDE_ARCHIVE_2026-09.md` **block 4** | ✅ present (`## block 4 — SPAWN step 2 re-homing story`, crc32 4059475864; 702 B) |
| `archive/CLAUDE_ARCHIVE_2026-09.md` **block 5** | ✅ present (`## block 5 — SPAWN step 3 hot/cold story`, crc32 3351236551; 761 B) |
| `archive/CLAUDE_ARCHIVE_2026-09.md` **block 6** | ⛔ not yet — **expected**, the plan creates it. File currently ends at block 5. Tail's asserted crc32 1151981870 / 7,541 B **independently confirmed** against the original, so block 6 will verify if written verbatim. |
| `AGENTS/DAEDALUS/outbox/delivered/` | ✅ exists |
| root `scripts/read_cap_check.py` | ✅ exists, takes `--agent` |
| root `scripts/safe-push.sh` | ✅ exists |
| root `scripts/corrections_boot_check.py` | ✅ exists |
| **root `scripts/regen_patterns_hot.py`** | ❌ **ABSENT** — see FAIL row 24. Only `AGENTS/DAEDALUS/scripts/regen_patterns_hot.py` exists (git-tracked, registered in `CHECKS.tsv:29`). |
| `AGENTS/DAEDALUS/scripts/sweeps_due.py` | ✅ exists; emits SELF-ROW, DIRECTORY-STALE, profile-clock lines as the compact now claims |
| `AGENTS/DAEDALUS/scripts/render_directory.py` | ✅ exists |
| `AGENTS/DAEDALUS/scripts/complete_check.py` | ✅ exists; legs (ii) pairing, (iii) pair-symmetry, (iv) EVOLUTION-placement all gate rc as the compact now claims |
| `AGENTS/DAEDALUS/scripts/verify_push.sh` | ✅ exists; rc contract 0/1/2 matches the compact verbatim |
| `AGENTS/DAEDALUS/scripts/read_cap_check.py` (named as the namesake) | ✅ exists — the warning's premise is real |
| `PATTERNS_COLD_INDEX.md` | ✅ exists |
| root CLAUDE.md steps 1b · 1c · 1c-bis · 1d · 1e | ✅ all five exist under §Git Protocol "At session end" |
| Indirect: `CLAUDE_ARCHIVE` block 4 → "full record → `EVOLUTION.md` (c)" | ⚠️ **stale** — (c) was rotated to `archive/EVOLUTION_ARCHIVE_2026-09.md` block 1. The original charter carried that corrected address; the compact drops it (§B item 2). |

**Format note (out of scope, FYI):** existing block headers in `CLAUDE_ARCHIVE_2026-09.md` read `## block N — block N — <what> …` (the label is duplicated). §1 states the format without the duplication. Match the file, or fix all six.

---

## Bottom line

The compaction is **substantively faithful**: 31 of 33 checklist rows pass, every executable command string and every rc contract survives byte-for-byte, every ⛔/⚠️/never authority clause survives, and no live clause escaped the author's enumeration except four minor items (two weak prescriptions, two pointers) listed in §B. Two things should be fixed before it lands: **(1) row 24 — `scripts/regen_patterns_hot.py` does not exist; write `AGENTS/DAEDALUS/scripts/regen_patterns_hot.py`** (or restore the original's path-free wording); **(2) declare in §1 the four accurate-but-undeclared corrections and the safe-push re-order**, so Will approves what is actually changing rather than a count of two. §B item 2's pointer chain is worth one line of repair while someone is in the file.
