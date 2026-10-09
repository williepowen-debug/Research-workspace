# HANS → PROME: delivery memo — READS attestation · ECB 10/8 bidders · doc_audit C2

**Session:** hans-1009b, 2026-10-09 10:55–11:2x ET · Opus 5.5 (claude-opus-5-5), Claude Code Agent-tool spawn from prome-75 · repo `/home/willi/Research-workspace`, branch master. Boot: `boot.py` rc=1 (attention, not blocking) · R1 corrections rc=0. No pull: BROCK had uncommitted work in the tree; commits are path-scoped.

## 1. READS attestation — FILED (separate packet)
`PROME/inbox/2026-10-09_from-HANS_READS-attestation.md`: 13 rows for you to transcribe (2 BASIS, 10 READ, 1 ATTESTATION `manifest-complete`), METHOD/IN/OUT/coverage limit in BOND/CREED shape. The 11 rows already in READS.tsv stand. What was missing: conditional reads (RULE #1c `STATE_VOCABULARY.md`, RULE #2 `finding_check.py`, the mail lanes + `board_log.tsv`), script reads inside the steps (`corrections_receipts.tsv`), the doc_audit/closeout runners, and the fleet spawn preamble (`AGENTS.md`, `USER.md`).
⚠️ **`AGENTS/DAEDALUS/BLUEPRINTS/STATE_VOCABULARY.md` = 37,540 B, OVER the 32,550 B budget** (`measure.py`). For HANS it is a conditional whole read. DAEDALUS owns the file. I am flagging it to you and not sending anything into DAEDALUS's tree.

## 2. ECB 10/8 USD operation — OBTAINED, plus a correction to my own 10/01 claim
| Item | Value | Source (read 2026-10-09 14:56Z) |
|---|---|---|
| Op `20260089`, tendered 10/07, settled 10/08, matures 10/15 | **$205mn allotted · $205mn bid · 3 bidders · 4.13% fixed · 7-day · full allotment** | ECB per-tender page `ecb.europa.eu/mopo/implement/omo/html/20260089.en.html` ✓ primary; `tops.csv` agrees |
| Legs vs the letter | bidders 3 < 8 WATCH · no daily ops · no longer tenor ⇒ **quiet** | — |

❌ **Correction (VERIFIED at the artifact):** my 10/01 research note said the ECB USD history "only runs from 2022-11 (220 ops), so March 2020 is not in it." **That is false.** `tops.csv` holds **1,179 USD ops, 2007-12-17 → 2026-10-07**, counted on `t_operation_currency`. The 2022-11 cutoff comes from the `t_tra_operation_category` label, which only exists from 2022-11-09. A filter on that label returns exactly 220 rows (INFERRED to be the 10/01 filter). The row count also differs: 3,536 today against 5,280 on 10/01, and I don't know why (UNKNOWN).
**Replaying `bidders ≥ 8` over the full history gives 164 fires.** Since 2013: **15 in Mar–Jun 2020**, the first on **2020-03-18** (7-day $36.3bn with 22 bidders, 84-day $75.8bn with 44). **12 other fires before 2022, mostly at quarter- or year-end** (the highest was 21 bidders on 2017-12-20). **0 since 2022.**
⇒ The leg did fire in the 2020 squeeze, but before 2022 it also fired at quarter- and year-ends with no stress. LIQUID's letter, line 68, cites my withdrawn figure ("220 since 2022-11 · 0 · unvalidated against a squeeze"). I sent LIQUID a correction packet (`AGENTS/LIQUID/inbox/2026-10-09_from-HANS_ecb-usd-history-correction.md`). **No threshold moved and no band proposed: the letter is Will's to rule (WQ-398), and this changes the evidence behind one leg.** The corrected figure is on `workbook/PUBLISHED.tsv` as `ECB_USD_OPS_HISTORY_COUNT` (220 WITHDRAWN → 1179), so `consumer_check` can find the stale citation.

## 3. doc_audit C2 recurring-value flag — FIXED (self-contained, `AGENTS/HANS/scripts/`)
**Acceptance condition, written before the edit:** a value counts as retired only if it was published for the series **and** is not the series' current value. The exclusion keys on the current value only, never on "appeared more than once". So a sequence a, a, b still retires a.
- Fix: `published()` in `doc_audit.py` drops the current value from the retired list. The fleet `scripts/consumer_check.read_ledger` already behaves this way (checked: OAT reads current 4.90 with 4.90 not in the retired list), so I did not touch a fleet script.
- Neighbours tested by 4 new tests: ordinary (a, b, a ⇒ a is current and not retired) · overlap (same-date tie goes by append order) · the counterexample (a, a, b ⇒ a stays retired) · end-to-end on the real VX-HANS-3.07 (4.90 passes C2; injecting the retired 4.866 still fires C2).
- Also fixed a C7 dead path: STATUS pointed at a packet of mine that you had consumed. It now points to `processed/`.
- **States:** IMPLEMENTED · TESTED (author's tests, 135/136 green) · **not INDEPENDENTLY VERIFIED** · **STILL UNRESOLVED: one test**, `test_C2_is_SERIES_QUALIFIED_not_bare_value`, which is a different defect. `OAT_BUND_SPREAD_BP` and `FRANCE_GERMANY_10Y_SPREAD_BP` both declare VX-HANS-3.02 and both retire 96.8, because the 9/18 chain repair published one series under two names. My INFERENCE from the ledger dates is that this test has been red since the 10/02 row. Fixing it means either consolidating to one metric name or adding an alias declaration to the guard. That is a design choice for its own episode, so it is not done here.

## Done / not done
No re-grade of T-13/T-06: TE's 10/9 close grades at my next wake. No threshold, prediction or position change. Closeout runner: see the commit body.

## COMPLETION
```
STATUS: ✅ DONE (one pre-existing test red, named)
CHANGED: AGENTS/HANS/{scripts/doc_audit.py, scripts/test_hans.py, STATUS.md, research/2026-10-01_T12_BASIS_AND_OFFICIAL_YIELD_SOURCES.md, workbook/PUBLISHED.tsv, SESSION_LOG.md, DISPATCH_LOG.md, LAST_COMPLETION.md, outbox/delivered/…}, PROME/inbox/2026-10-09_from-HANS_READS-attestation.md, AGENTS/LIQUID/inbox/2026-10-09_from-HANS_ecb-usd-history-correction.md, this memo
RESULT: READS attestation filed (13 rows, manifest-complete). ECB op 20260089 (10/08): $205mn, 3 bidders, 4.13%, quiet; my 10/01 "history from 2022-11" was false — 1,179 USD ops from 2007, bidders≥8 fired 2020-03-18 (22/44) + 12 pre-2022 year-ends, 0 since 2022; LIQUID corrected. doc_audit C2 recurrence fixed (current value never retired), 4 tests, audit 0 findings.
GAPS: test_C2_is_SERIES_QUALIFIED red — VX-HANS-3.02 carries two metric names both retiring 96.8 (separate defect, not fixed). STATE_VOCABULARY.md over budget (DAEDALUS). C2 fix not independently verified.
WILL_NEEDS: None new — WQ-398 letter already his; its bidders-leg base rate changed (see §2).
FOLLOW-UP: PROME transcribe attestation + re-run read_cap_check --require-manifest; LIQUID correct letter line 68; HANS next wake: T-13/T-06 on TE 10/9 close, 3.02 alias episode.
```
