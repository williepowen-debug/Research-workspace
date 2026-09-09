# BRENT SCRATCH — September 9 maintenance

## CHANGES SINCE LAST SESSION

The autonomous September 9 EIA routine correctly recorded no new WPSR: holiday release remains September 10. September STEO published during the audit, confirmed at the primary by 12:07 ET (forecast completed September 3); full comparison remains pending. The morning retail, futures and delayed-option observations retain their original dates/times; no audit-boot quote adopted. No XLE execution receipt arrived. Final sync inspection found PROME commit 7a6b05a58, recorded during this audit: Will sold the remaining USO October call. Reconciled to TRADE; zero contracts remain and B/C are discharged.

## WHAT I DID THIS SESSION

Implemented audit A1–A4 and A7–A9; extended A6 with complete STNG/FRO/DHT diagnostics and explicit matched-contract futures calculations. Quote freshness, EIA per-metric completeness/date alignment/local fallback, obsolete wording, prediction outer bounds and BRT-29 M alert, weekday labels and retired refiner CLI repaired. Forty-one regression tests pass. Live boot rc=2: dated EIA, unresolved BRT-29 M, Baker Hughes timeout and ledger nudge remain visible. Full November contract diagnostic passes source/date/unit checks; no observation adopted as a new dashboard or grade. Dated STATUS/rationale/hints archived verbatim with checksums; FASTOW memory reconciled with current calendar rules. A5 remote timing/prompt update is ready but NOT INSTALLED: no routine-control tool available. Full results and commands: audits/2026-09-09_maintenance/REPORT.md. No new capital rule, thesis probability, prediction grade or broker receipt.

## NEXT SESSION (dated, future-verifiable)

**September 9 decision:** keep existing Claude routines; Astra/Fable BRENT sessions consume the shared files. Timing/publication repair still awaits remote application; no migration or routine-model change. Next substantive task remains the published September STEO comparison.

**September 9 planning addendum:** execution order and completion tests are in [remaining-work plan](audits/2026-09-09_maintenance/REMAINING_PLAN.md). Brief scheduler-access pass, release reads at their windows, BRT-12 definition/history recovery, then prioritized source gaps. Plan only; no activation or new evidence this turn.

1. **September 9 XLE receipt pending:** user was asked for actual quantity, price and time; no response yet. Keep selected exit pending until receipt. TERRY/Will own broker checks/execution. Never infer fill from intention, quote or screenshot.
2. **September 9 STEO PUBLISHED; comparison pending:** retrieve September workbooks and compare saved August baseline in research/2026-09-09_squeeze-review/august-steo-baseline.json. Key question: Q3→Q4 supply recovery/draw slowdown and 2027 effective-spare recovery date. Same IDs/units/months; flows simple monthly means, stock quarter-end. August issue August 11, forecast August 6. September issue dated September 9, forecast completed September 3; no full September revision comparison yet measured.
3. **September 10 noon / later file batch 14:00 ET WPSR:** verify each file covers September 4. Worksheet in integrated report; baseline Cushing 22.508M, SPR 286.604M, utilization 98.0%, PADD3 gross inputs 9.662 mb/d. Preserve September 4/11 SPR weeks/bands and wording/premise gap. One print cannot resolve two-print test. Reuse paired EIA 52-week method; current pandas/xlrd versions require direct xlrd for legacy xls, as in the new analysis script.
4. **September 11 after ~13:00 / ~15:30 ET:** primary Baker Hughes/CFTC as-of September 8. cot_grade.py --expect 2026-09-08; exit 3 WAIT. No schedule change installed; 14:00 Friday routine precedes COT. Exact 16:15 ET update and Thursday fallback await remote activation in audits/2026-09-09_maintenance/ROUTINE_UPDATE.md.
5. **BRT-29 next research:** three further eligible carriers remain unestablished. AF-KLM one group; Ryanair Sep2 outside M window; Norse distinct post-baseline announcement unestablished. Do not multiply subsidiaries, count old cuts or relabel airspace-only causes. M explicitly unresolved after Aug31; T requires <=-3.0 by Sep25 observation, final Sep30. No final grade from incomplete search.
6. **BRT-12 before September 30:** original historical contract IDs/roll rules and dated refiner/upstream E&P credit history. Archived March narratives and fixed-November diagnostic do not establish ordering; broad HY is not upstream. No missing-data-to-neither inference.
7. **Source follow-ups retained:** exact PortWatch August 31–September 1 query in setups/2026-09-08_market-docket-owner-read.md; Vortexa weekly Sidi; official No.1097/publication/original No.954. No target or Q1/Q2/Q3 clock substitution; OSPREY October 1 retiming not adopted. September 15 OSPREY objection window remains, with owner downgrade/channel review before consuming new marks.
8. **Later dates:** Sep18 spread expiry; Sep25 final in-window rig/threshold week; Sep30 resolutions; Oct1 full owner read; Oct4 OPEC November decision; Oct26 BRT-30. TRADE/CATALYSTS own exact letters.

## OPEN THREADS / WATCHES

- **Maintenance remaining:** A5 requires actual remote configuration access and read-back receipts; local plan is not live coverage. A6 tanker components are complete, but registered WTI–Brent/diesel probes remain component-only pending the original benchmark/roll/history construction. Explicit named-contract diagnostics do not repair that historical identity. BRT-29 internal T and other event preconditions still require owner review; the new scanner only adds explicit outer bounds and current unresolved M. No unattended monitor installed.

- CPC partial restart remains dated August evidence; SPM-3/current throughput UNKNOWN. Jazan restart/current loss and older incident backlog remain open. No aggregate outage quote.
- Port Arthur's existing RF-008 already contains the Q2 SEC source: normal refinery throughput then does not prove diesel unit recovery or resolve September storm operations. September 2 port reopening does not certify refinery restart.
- Treasury operative instruments/real flows; exact SPR contract/current authority; Russian same-series product flows and Vortexa Sidi remain open.
- WALTER Saudi SIG-011/Dangote SIG-023, late Novorossiysk/Kstovo/Novatek and other FALCON source follows remain deferred; this research did not consume those packets. OSPREY Urals differential ask remains deferred without same-basis current quote.
- Existing off-ramp/persistence, alternate measurement and historical OVX obligations remain. WQ-189/192 STAND DOWN.

## POSITION DECISIONS PENDING

XLE execution receipt only. TRADE holds corrected 37-share mirror and USO October call CLOSED on the September 9 PROME receipt. October 9 time stop/B close management discharged; no trigger claimed fired. USO October call first-sale price permanently UNKNOWN/no re-ask; no second 14.25 target. Spread HOLD through expiry; current Robinhood position not in Fidelity capture. Share scaffold unratified; TERRY's August 23 scaffold still says 35, while its newer call-management card and broker mirrors say 37. Consumer note/NEXUS record this owner follow-up; no external packet sent. No new proposal. TERRY’s older October-call card still shows one held; PROME receipt supersedes that state, owner reconciliation pending.

## MAIL STATE

OSPREY packet remains DEFERRED in place; September 15 objection window already recorded. WALTER/MSG lanes were empty at boot. No packets consumed, moved or sent this pass. Existing outbox loop closures retain prior September 8 disposition.

## WORKBOOK HEALTH

Maintenance tests 41/41 pass. Network boot rc=2 with no crashed script; source/obligation findings remain as listed above. Tanker probe now measures all three components; WTI–Brent/diesel registry probes remain partial. Nine ACTIVE and three other stale present-status incident rows still require sources; no aggregate outage estimate. Lessons unchanged (no new lesson); board_log unchanged (no packet consumed); incident ledger unchanged (no new source verification); registry changed only tanker probe metadata, no numerical letter or vintage refresh. Hot-file rotations preserve every moved block with checksums; generated calendar still matches all 20 docket rows. Frozen ledgers, prediction grades and binding trade specs unchanged. No new XLE receipt; USO closure retains prior PROME source. Report includes validation scope and remote activation instructions.
