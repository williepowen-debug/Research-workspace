# DAEDALUS → PROME · 2026-09-25 12:3x ET · L290 render (#4 on the row's basis) · inbox 9→0 · WQ-295 answer · WALTER staleness #5 closed from record

**Spawn:** PROME Tier-1 WQ-184 due-row (`prome-2e`, DOCKET L290), booted 12:21 ET (gate rc 0). $0. No threshold, gate or score moved.

## 1. DOCKET L290 — the coordination scorecard for the week 9/19→9/25
- **Artifact:** `AGENTS/DAEDALUS/scorecards/2026-09-25.md` plus the SCORECARD.tsv row. **Label: #4 on L290's FULL-v1 basis (the ≥4-render floor); #5 on DAEDALUS's old count, which included the 9/2 legs-only run.** Both counts are printed in the render's label block, and the row's basis governs.
- **Read vintage:** 2026-09-25 12:28:30 EDT at HEAD `7a43dd165`. ORCH_LOG's last commit was `1f7e7908f` (12:23:54). Rows PROME appended after 12:28 are NOT in the render: the first pass at 12:22 read 128 touches and this one read 130.
- **Values:** loops 26 · forecasts 3 (HIT 2, MISS 1) · catches_pre 16 · corrections_post 10 · rulings 28 · commits 1,157 · touches 130 · zero-capital 130/130 · PROME-only share 300/1,157. Col 8 prints WITHDRAWN. **DESCRIPTIVE ONLY: no threshold is proposed.** One now becomes PROPOSABLE, and only as a WQ row to Will.
- ⚠️ **Instrument repaired before delivery (`scorecard.py` v1.1→v1.2).** The first pass printed **rulings=1** (and decision_yield 26.00) because WILL_QUEUE's RECENTLY-DONE rows carry the verb in the bold title and the date in cell 2, and v1.1's stamp regex never reached that form. Acceptance conditions A1–A7 were written before the edit (`AGENTS/DAEDALUS/runs/2026-09-25_SCORECARD_V1_2_REPAIR.md`). **IMPLEMENTED · TESTED 17/17 (2 fail with the repair disabled) · INDEPENDENTLY VERIFIED** by an Opus reader using its own ten counterexample rows; it checked all 28 counted rows at their text and confirmed every v1.1 stamp unchanged for 9/05–9/25: **PASS-WITH-RESIDUE, zero ❌.** **STILL UNRESOLVED:** five latent miscount shapes plus the inherited one, none firing on today's file, declared in §5 of the record. The fix goes in before the 10/02 render.
- ⚠️ The 9/18 row's col 4 re-reads **4** against the published 6 on today's queue. Rows have rolled off since 9/24, and the old logic gives the same 4, so this is an inherited roll-off limit, not the repair. The published row is left as rendered.

## 2. L0 drain — 9 packets → `inbox/processed/`, dispositions in `AGENTS/DAEDALUS/runs/2026-09-25_INBOX_DISPOSITIONS.md` §1
- **WQ-286 (BARON freeze · G1 · G2 · R2): ACCEPTED, EXECUTION OWED.** None of the four has landed since Will's 9/24 18:32 word (git log checked), and none was in this spawn's scope. Each needs acceptance conditions first, and G2 needs an independent reader.
- **WQ-288:** census bound to Staleness #6 (~10/15).
- **BROCK 57→58/70:** the profile's refresh TRIGGER fired (`profiles/BROCK.md:8`). BROCK is queued for refresh; I did not patch the trigger value.
- **MIDAS/VULCAN/WATT PR#6 replies:** received. The write-back tail goes to PR#7 (10/01), re-verified at their artifacts. **No registry row changed.**
- **RED FROZEN token:** closed on my side. RED owns the landing through your re-spawn with `AGENTS/SAM/red/` in perimeter, and CH-009/012/017 are overdue by 1 day (owner RED).
- **VULCAN's tripwire question:** answered by packet. My 9/12 sitting never ruled it. HANS 9/18 (`ff11cf03d`) is an independent second instance, making it n=2, a PATTERNS candidate at PR#7.

## 3. WQ-295 — `PROME/inbox/2026-09-25_from-DAEDALUS_cadence-and-watch-terms.md`
**CADENCE: WEEKLY. Not a query desk, so no WATCH_FOR list.** Half (a): I DECLINED a hand-kept FLEET_MAP `watch_terms` column, because the lists live out-of-repo in `Research-Intake/scripts/newsweep_config.py` and a hand column would be a drifting mirror. In its place I propose a GENERATED `WF` column in FLEET_DIRECTORY that prints UNKNOWN when the lane is unreadable (a build, awaiting your or Will's word). Half (b): the B1–B5 acceptance skeleton is in the packet. The full spec-letter is owed by the L487 row (10/02), and **N is a threshold, so it goes to Will.** R2/R4 are not encoded because WQ-295 was unruled when I read it.

## 4. WALTER staleness #5 — the six DOORBELL_LOG rows
**All six were consumed by their own desks, on or before their referent dates, per each desk's own `board_log.tsv`.** They read PENDING only because `consumed_at` was never back-filled. The values went to WALTER by packet (`AGENTS/WALTER/inbox/2026-09-25_from-DAEDALUS_staleness5-…md`). **L22 BROCK is the exception:** its referent date preceded the DISPATCH itself, so whether it counts as a miss is WALTER's call. The BRENT L144/L145 `processed/` moves were swept into WALTER's `7362cdf2d` through the shared index, but the consumer is BRENT.

## Skipped / not run (named, per the skipped-control rule)
- **Profile-refresh queue, Prose-Remedy Census #1, H2 as-made audit:** all DUE today per `sweeps_due.py`. Not run, because they were outside the spawn's four tasks.
- **WQ-286 builds:** not run (same reason).

## COMPLETION — DAEDALUS — 2026-09-25
STATUS: ⚠️ PARTIAL (all four tasks done; WQ-286 builds + three DUE queues carried, outside scope)
CHANGED: AGENTS/DAEDALUS/{scorecards/2026-09-25.md, scorecards/SCORECARD.tsv, scripts/scorecard.py, runs/2026-09-25_SCORECARD_V1_2_REPAIR.md, runs/2026-09-25_INBOX_DISPOSITIONS.md, STATUS.md, sweeps/REGISTRY.tsv, inbox/→processed/ ×9}; packets PROME/inbox/…cadence-and-watch-terms.md · AGENTS/WALTER/inbox/…staleness5-…md · AGENTS/VULCAN/inbox/…tripwire-…md; this memo
RESULT: The L290 render landed as #4 on the row's basis (#5 on my old count), read at 12:28:30 EDT: loops 26 · rulings 28 · touches 130, descriptive only. rulings=1 was an instrument blind spot, repaired to v1.2 and independently verified (PASS-WITH-RESIDUE, 0 ❌). The inbox went 9→0. Cadence is WEEKLY, and DAEDALUS is not a query desk. All six "stale" DOORBELL rows were consumed on or before their referents.
GAPS: The WQ-286 ①–④ builds are owed (Will-approved 9/24, not landed). The profile queue (+BROCK), Prose-Remedy Census #1 and H2 are DUE and not run. scorecard v1.2 residue 1–5 is to be fixed before 10/02. The HENRY/LIQUID DOORBELL rows were not checked.
WILL_NEEDS: None new. A future threshold on the scorecard, and N in the dark-days check, are his when proposed as WQ rows.
FOLLOW-UP: A DAEDALUS session for WQ-286 ①–④ plus the profile queue. PROME consumer-reads L290 at the artifact. PROME/Will give a word on the generated WF column. WALTER back-fills 6 consumed_at values and rules L22.
