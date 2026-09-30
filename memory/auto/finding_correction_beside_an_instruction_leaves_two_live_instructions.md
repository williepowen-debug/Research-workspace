---
name: finding_correction_beside_an_instruction_leaves_two_live_instructions
description: "Annotating an obsolete instruction with a correction leaves BOTH readable, so the surface now teaches two contradictory things and a reader can comply with either. Replace the instruction; home the history somewhere it is not read as guidance."
metadata: 
  node_type: memory
  symptoms: the doc says X then says actually not X; corrected 2026-.. inline; the step contradicts itself in one sentence; file grew while we were fixing it; which of these two does it actually mean; rebuttal next to the rule; we fixed the docs but people still do the old thing
  type: finding
  originSessionId: d310c787-f183-41a8-8ca9-bb110566f205
  modified: 2026-09-06T15:00:43.196Z
---

**A correction placed BESIDE an instruction does not replace it. Both stay readable, and the surface now teaches two contradictory things.**

Found by Codex on WALTER, 2026-09-06, after a full repair cycle. The literal artifact, in one sentence of `design/BOOT_PROTOCOL.md` item 30:

> **Grades ONLY** `AGENTS/WALTER/CLAUDE.md` (**MEASURES, does not GRADE** — corrected 2026-09-06: it previously returned MED over the cap…)

The correction was accurate, sourced, and dated. It was also **appended to the sentence it refuted**, so item 30 simultaneously said *grades* and *does not grade*. A reader who stops at the bold lead complies with the retracted rule; a reader who reaches the parenthesis complies with the new one. **Both readings are supported by the text.**

**Why this is not the same as "corrections cost bytes"** (`[[finding_disambiguation_costs_bytes_so_a_capped_surface_cannot_absorb_every_flag]]`): that finding is about SIZE and its remedy is a split. This one is about PLACEMENT and the defect is CONTRADICTION — size is only a side effect. A perfectly small file can carry this defect in one sentence.

**The mechanism, and why it is so easy to do:** annotating feels safer than deleting. The old text is evidence; the correction has provenance; removing the old sentence feels like erasing the record. So the natural move is to leave it and argue with it. **That instinct is right about the history and wrong about the instruction.** An instruction is not a record — it is a thing someone will execute.

⇒ **THE RULE: the active instruction states current behaviour ONCE. The account of what it used to say, and why that was wrong, lives somewhere it will not be read as guidance** — the implementing function's docstring, a version-history file, the commit message. Point to it; do not inline it.

**How to catch it:** read the corrected sentence as a stranger who stops at the first period, then again stopping at the first bold clause. If any truncation of it yields the OLD rule, the correction is annotation, not replacement. A reader who quits early is the normal case, not the adversarial one.

**Diagnostic that this habit is present** (all four observed in one WALTER session, 2026-09-06): a fix lands on the OUTPUT while the instruction that produces it is untouched — the doc corrected but not the step that writes the doc; the check's message corrected but not its documentation; the summary corrected but not the closeout rule that generated the wrong denominator. **The tell is a repair cycle that keeps finding "one more place," each place being upstream of the last.** Ask at the first fix: *what wrote this, and does that still say the old thing?*

**Second-order cost, measured:** the surface GROWS during the repair. WALTER's charter went 54,222 → 54,306 B across a session whose subject was that the charter carries too much narrative. Every rebuttal is net-new prose beside prose that should have been deleted, so a correction pass run this way makes the documented problem worse while appearing to fix it. Pairs with `[[finding_anti_ratchet_governs_state_not_prose]]` (a rewrite pass can ADD bytes) and `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]` (a fresh header over stale body CERTIFIES it — the same shape, one level up: there the correction sits ABOVE the stale text, here BESIDE it).

**Related but distinct:** `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` — that is about a new rule failing to reach old surfaces at all. This is about the rule reaching the surface and the old text surviving anyway.

### Instance 2026-09-28 — a registry with a ONE-ROW-PER-KEY invariant: appending the correction left two live attestations, and the checker graded the stale one (PROME READS.tsv, caught by WALTER)
WALTER asked PROME to transcribe a fresh manifest attestation dated 2026-09-28 (its 2026-09-15 row had gone STALE after a charter commit). PROME APPENDED the new row. `reads_check` enforces exactly one ATTESTATION per reader, printed a SCHEMA error, and kept grading on the 9/15 row — so the desk stayed ⛔ STALE / UNKNOWN with a correct new row sitting eleven lines below. Fix: REPLACE in place, with a supersession note pointing at `git show <sha>` for the old text. **The class:** a surface whose invariant is "one live claim per key" turns any append into two live claims; the correction has to be a replacement, and the old text's home is git, not the file. n+1.

**Instance n+1 (2026-09-29 evening, NEXUS charter, caught by a PROME-spawned blind reader): a struck-through step retires the STEP, not its CONSUMERS in the same file.** NEXUS retired BOOT 5, CLOSEOUT 12/13, `outbox/` and `SIGNALS.md` by annotation (`~~…~~ RETIRED`) on Will's word; the sentences elsewhere in the 62 KB charter that pointed at them stayed live — the LIVE-EVENT step still wrote an "outbox note", the signal-lifecycle section still archived to `signals_archive/`, a routing table still said "scan `AGENTS/SIGNALS.md`" (a different, live file) with no boot step reading it. A blind Opus reader found 14 ❌ across 93 claims the same evening; all verified; NEXUS fixed them at 8295b710f — by adding text (64,677 → 69,214 B at that commit; 62,768 B before the intermediate 1b6bf1440 — ARGUS r3 ⚠️8 corrected PROME's single-step attribution). **How to apply (added):** a retirement is a correction to every sentence that names the retired thing — `grep` the retired name across the whole file before calling the encode complete; and schedule the compaction WITH the fix, because a fix pass on a rule file grows it. Receipt: `AGENTS/NEXUS/inbox/processed/2026-09-29_from-PROME_charter-cold-read-ledger-14-flags.md`.
