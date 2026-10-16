# BOOT.md rotation — the plan (verbatim MOVE class; plan read BEFORE any edit, result read after) — 2026-10-16

**Written:** 2026-10-16 16:1x ET (PROME, session 8fb641db). **Authority:** WQ-445 A (16:04 ET) — the sitting's third process change; READ_CAP rule 5 already owes this rotation (BOOT.md 31,033 B = 95% of 32,550 B, `measure.py` 16:06 ET). **Class:** PROCESS (a boot-read surface shrinks; no rule changes meaning; every moved line is conserved byte-exact and reached by ONE pointer at the step that used it).

## The moves (source → destination; each block measured by `measure.py` crc32 before and after the move)
| # | Block in `PROME/BOOT.md` | Bytes | Destination | Pointer left in BOOT.md | When it is read after the move |
|---|---|---|---|---|---|
| M1 | header line 3, from the first ` Prior:` to end of line (the stamp chain) | 742 | `PROME/archive/BOOT_STAMP_CHAIN_2026-10-16.md` (the CLOSEOUT precedent, 2026-10-16 00:01) | `Prior stamps → archive/BOOT_STAMP_CHAIN_2026-10-16.md; this line keeps the latest and at most ONE prior.` | never at boot (history) |
| M2 | `**Repeat boot:** …` paragraph | 1,083 | `PROME/BOOT_MODULES.md` § Repeat boot | one line after "Bounded reads": `**Repeat boot** (reuse of acknowledged reads, `--refresh`): BOOT_MODULES.md § Repeat boot — read it only on a repeat boot.` | repeat boots only |
| M3 | step 3b, the `**A unit tap (Change A, DOCKET L660 …** … `say which set he saw. ` clause | 1,334 | `PROME/BOOT_MODULES.md` § Deck unit taps (Change A) | in 3b, at the clause's place: `Unit taps (CHOICE / plain-unit / LATER / no-decision_id / two rows on one position): BOOT_MODULES.md § Deck unit taps — read it when the store returns ANY unconsumed document.` | only when a tap exists (none today) |
| M4 | § Conditional Modules (heading through the table, up to § Closeout Pointer) | 3,378 | `PROME/BOOT_MODULES.md` § Conditional modules | `## Conditional Modules → BOOT_MODULES.md § Conditional modules (need → read/use table; open the row you need).` | on need |
| M5 | § Boot-class fleet memories: the two trigger-keyed groups "Reviving a stale desk" and "Domain-desk boot-protocol patterns" (the every-boot group and the "Already mechanized" group STAY) | ≈1,100 | `PROME/BOOT_MODULES.md` § Trigger-keyed fleet memories | one line under the section: `Trigger-keyed groups (desk revival · desk hardening) → BOOT_MODULES.md § Trigger-keyed fleet memories.` + the same pointer appended to the heading line of `memory/auto/INDEX_COLD_EMBEDDED.md` § Boot/closeout (the embed census names BOOT.md as the home; carve-out ③, PROME-authored shard) | at spawn / hardening time |

**Expected size:** 31,033 − (742 + 1,083 + 1,334 + 3,378 + ~1,100) + pointers (~600) ≈ 24,000 B ≈ 74% — under the 75% rotate line; measured after the move, never asserted. `PROME/BOOT_MODULES.md` is an on-demand file: READS.tsv gets ONE new row, mode `scoped`, source step `PROME:BOOT.md-pointers`; BOOT.md's row stays `whole`.

## Invariants (the plan reader checks these; the result reader re-checks them)
1. Every moved block appears in its destination byte-identical (crc32 of the block = crc32 of the destination section body under its two-line header).
2. No rule changes meaning: the pointer names the SAME trigger the block stated (repeat boot · a tap exists · a need · a spawn/hardening moment); the every-boot memory group is untouched.
3. Every citation that reached the moved text still resolves: `grep -rn "Conditional Modules\|Boot-class fleet memories\|Repeat boot\|Change A" PROME/.claude/skills PROME/registry/READS.tsv memory/auto/INDEX_COLD*.md PROME/CLOSEOUT.md` — each hit either points at BOOT.md's surviving pointer or is updated to BOOT_MODULES.md (list the hits in the result).
4. Both `/boot` runner copies stay identical; step 4b's instruction in the runner still names the every-boot group.
5. `scripts/read_cap_check.py --agent PROME --require-manifest --charter-mode explicit` rc=0 after; `rotation_due` drops by one.
6. Nothing else in BOOT.md changes (the diff is the five cuts + five pointers; `git diff --stat` one file plus the two new files and the index line).

## Acceptance (categories): ordinary = invariants 1–6 · overlap = a block cited from TWO places (M5: BOOT.md + the embed census) keeps both reachable · wrong owner = `memory/auto/INDEX_COLD_EMBEDDED.md` is a shared index — the edit is ONE appended pointer on a PROME-authored heading, nothing else · missing information = a crc mismatch or a dead citation ⇒ the move is reverted, not patched · concurrent = N/A (one session, MACHINE_LOCAL).
