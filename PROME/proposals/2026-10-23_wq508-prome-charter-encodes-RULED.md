# WQ-508 — PROME's two charter encodes (P01: the C5 pause · P02: the C8 grant), canon-drafts record

**Written:** 2026-10-23 10:3x ET (PROME, session prome-03, desktop). **Status:** RULED — Will in PROME's window 2026-10-23 10:27 ET, verbatim *"ok approved"*, on WQ-508 (DAEDALUS Harness Audit #3 changelist), whose one OK for Tiers 1/3/4/5 expressly includes PROME's P01 and P02 charter edits (WILL_QUEUE row 508, RECENTLY DONE). Both edits RECORD words Will already gave; neither creates authority. Route: `PROME/CLAUDE.md` § Session Process Controls "Canon drafts live in the ruling record, transplanted once" — drafted here, blind plan read here, ONE insertion per line, one result read; DOCKET L644's own instruction ("drafted in the ruling record, plan read + result read; PROME's own charter is never C4").

## 1. Inputs, each at its artifact

| Input | Artifact | What it fixes |
|---|---|---|
| The C5 pause | `USER.md` § No expiry nagging (Will 2026-10-20 11:32 ET verbatim); `PROME/CLAUDE.md` line 53 already carries "**C5 — PAUSED by Will 2026-10-20 11:32 ET**"; `PROME/AUTONOMY.md` change log 2026-10-20 row | Line 45 of `PROME/CLAUDE.md` still reads as if C5 were live ("C5 below permits commissioning one held-option card") — Harness Audit #3 P01 (Tier 3: text contradicting Will's standing words). |
| The C8 grant | Will to WALTER 2026-10-04 ~20:00 ET, verbatim *"WQ-369 yes"*; committed relay 8a2dbfa65; `PROME/AUTONOMY.md` change log 2026-10-04 row ("Narrow C8 — IMMEDIATE dark-desk own-theater spawn (WQ-369)"); DOCKET L644 (registered 2026-10-08, overdue since 10/12) | `PROME/CLAUDE.md` § Ask First lists C1–C7 and "⛔ Nothing else moved" although C8 was ruled 10/4 and exercised ≥5 times on 10/8 — Harness Audit #3 P02. |
| The approval to edit PROME's charter | WQ-508 RULED APPROVE 10:27 ET, the row's one OK naming P01 and P02 | PROME's own charter is ask-first; this is the ask, answered. |

## 2. The two edits — exact text

**P01 — line 45 of `PROME/CLAUDE.md`.** Replace the sentence
> `C5 below permits commissioning one held-option card, never executing its recommendation.`
with
> `C5 below is PAUSED by Will (2026-10-20); while paused, no sell-or-roll card is commissioned under it, and when lifted it permits commissioning one held-option card, never executing its recommendation.`

**P02 — line 53 of `PROME/CLAUDE.md`, three substring replacements in the "Done without asking" paragraph, and nothing else in it:**
1. `Seven kinds of step no longer stop for Will's word;` → `Eight kinds of step no longer stop for Will's word;`
2. Immediately after the C7 clause (the text ending `… anything that costs money, or sends Will's name or email to an outside party, stays ask-first.`) insert, before `**Guard, all seven:**`:
   > `**C8 (WQ-369, Will to WALTER 2026-10-04 ~20:00 ET, verbatim *"WQ-369 yes"*; committed relay 8a2dbfa65; AUTONOMY change log 2026-10-04 row; encoded 2026-10-23 under WQ-508):** ONE bounded session where the dispatch class is IMMEDIATE, the ACTION owner is dark and the event is in that owner's registered theater — an ordinary-cap / Tier-2 exception; same-day report; the same one-undo-in-60-days guard; NOT an unattended-run grant (WQ-388 is separate and unruled). First applications 2026-10-08 (AEOLUS · CORAL · BRENT; `PROME/state/ORCH_LOG.tsv`). `
3. `**Guard, all seven:**` → `**Guard, all eight:**`

The closing "⛔ Nothing else moved — ask-first exactly as before: …" sentence is unchanged: C8 is a class moved on Will's word, which is exactly what that sentence reserves to him.

## 3. Invariants the plan read checks

1. Each replaced substring occurs exactly once in `PROME/CLAUDE.md` before the edit (the insertion script asserts it).
2. No level, operator, instrument, route or threshold changes; no class is added that Will did not rule (C8 = WQ-369; the pause = 10/20).
3. The C5 sentence keeps the original permission intact for when the pause lifts, and does not reinstate it now.
4. The C8 clause matches the AUTONOMY 2026-10-04 row and DOCKET L644 in every term: IMMEDIATE · dark owner · registered theater · one bounded session · same-day report · one-undo guard · not unattended.
5. `git diff --stat` on `PROME/CLAUDE.md` = 2 lines changed (lines 45 and 53), nothing else.
6. Byte flow: `PROME/CLAUDE.md` is a boot-injected charter; its size after the edit is reported by `PROME/tools/measure.py` in the commit body (the 20,000 B target of the WQ-299 freeze is a measure, not a gate).

## 4. Consequents (not in this record's edits)

- `PROME/BOOT.md` line 73 and `PROME/CLOSEOUT.md` line 118 say "every C1–C7 act" in their report lines; they read C1–C8 after this lands. Pointer-form fixes, carried to the next session with D12 (CLOSEOUT.md line 31 "Optional" → commit) because today's process-change count reaches its ceiling of five with this edit.
- DOCKET L644 → RESOLVED pointing here. Harness Audit #3 lines P01/P02 → done; DAEDALUS informed in the WQ-508 round.

## 5. Reads
- Plan read (blind, on this record): DONE 2026-10-23 10:31 ET — coldreader (Sonnet), ledger `PROME/reports/2026-10-23_wq508-cold-reads/plan_read.md`: 11/16 ✅ · 4 ⚠️ · 1 ❌. ❌3 fixed: the C8 clause had an added "Tier-1" label that neither the AUTONOMY 2026-10-04 row nor DOCKET L644 carries — re-cut to the AUTONOMY row's own words. Residue (WQ-178): ⚠️13 "the insertion script asserts it" = the Python edit run in this session (the commit body carries its assert output); ⚠️14 today's five process changes are listed in the session's closeout report, not here; ⚠️15 RULED in the header = Will's approval of the edits, the reads are this section; ⚠️16 FIXED beyond the ❌ because it changes a record: AUTONOMY line 103 ("charter propagation still OWED") and line 108 ("six active kinds") get a dated change-log receipt in this commit (seven active of eight, C5 paused). "D12" = Harness Audit #3's label for the Light-closeout commit question, WQ-508 Tier 2.
- Insertion: DONE 2026-10-23 10:31 ET — `PROME/CLAUDE.md` lines 45 and 53, exactly the § 2 text (with ❌3's re-cut).
- Result read (on `PROME/CLAUDE.md` lines 45 and 53): DONE 10:33 ET — coldreader (Sonnet), ledger `PROME/reports/2026-10-23_wq508-cold-reads/result_read.md`: 9/14 ✅ · 5 ⚠️ · 0 ❌. C5 pause consistent across lines 45/53 and USER.md; C1–C8 count and guard agree; C8 matches the AUTONOMY 2026-10-04 row on all eight terms; 10/8 first applications exist in ORCH_LOG; "Nothing else moved" consistent. Early stop at ❌ = 0 (episode reads: 2).
- Residue (declared 10:33 ET 10/23, WQ-178 — left unfixed by rule, none changes what C8 permits): a stranger cannot tell from line 53 alone what "dispatch class IMMEDIATE", "dark" and "ordinary-cap" mean (defined in WALTER's BOARD spec, the Desk-spawn preflight and the WQ-184 cap of four) · whether "ONE bounded session" is per event (it is: one session per qualifying event, the 10/4 letter) · whether an undo of a C8 act demotes only C8 or all eight (the guard sentence says "the whole class" — the WQ-348 class, i.e. all eight; the 2026-10-04 AUTONOMY row says "as registered") · what WQ-388 is (the separate, unruled unattended-run question; its row rolled off the live queue, ledger has it) · "eight kinds no longer stop" while C5 is paused (seven active — AUTONOMY's receipt row says so; the charter line keeps the class count) · line 53 does not cite this record (the AUTONOMY receipt row does). These are candidates for the next charter pass (DOCKET L817 ④/⑤), not for a fourth edit now.
