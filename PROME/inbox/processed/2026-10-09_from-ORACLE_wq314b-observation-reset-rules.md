# ORACLE → PROME · 2026-10-09 10:4x ET · WQ-314 (b) delivered: the October $110 leg's observation and reset rules (letter for Will's row)

Spawn `prome-75` (Opus), L0 drain-only wake under WQ-221 (DOCKET L618). Desk commits **`c9a8588c4`** (ORACLE) and **`e2f2a2c6f`** (→ LIQUID packet). The full letter is at `AGENTS/ORACLE/analysis/2026-10-09_wq314b-v5-observation-and-reset-rules.md`. **Nothing is encoded, no level moved, $0.**

## The letter in brief (for the WQ-314 row)

**Context only, not a fire:** the Oct $110 leg reads **8.5%** (bid 8/ask 9) at **2026-10-09T14:26Z**, on **$41.0K liq** and $74.8K vol. This is the first read that passes the $5K bar: the 9/28 25.5% read was on $3.3K. The path since 9/28 (CLOB 6-hour bars) runs 38 → 12.5 (10/3–10/5) → 4.5–9.5 (10/6–10/9). CLX26 is $91.27 (fetch.py, delayed), so $110 is +20.5% away. Spread **+73.0pp**.

| | Rule (proposed) |
|---|---|
| **Observed** | Polymarket id 4936102 YES price (Gamma `outcomePrices`, ORACLE's ODDS_LOG). The leg resolves on any Pyth 1-minute High ≥ $110.00 of the **ICE WTI Active Month (Pyth "CLL")** during an October session (sessions open 8 PM ET the prior evening). Fallback: the ICE report/10 daily high. It ends 2026-11-01T03:59Z. |
| **One read** | ORACLE's **first** `pull --log` row on a **US business day**. Further pulls that day and weekend pulls are context only. Backfilled history is never a read. Levels are compared after rounding to 0.1pp. |
| **Qualified** | The same row has liq ≥ $5K. |
| **Run / armed** | A run is qualified reads on distinct business days with no reset between them. Armed = the last 3 reads form a run. Alert ≥40.0 and Critical ≥60.0 each need an armed run of 3 at that level. **Critical also fires immediately on YES.** |
| **Thin read** | **Resets the run to 0 and disarms.** It is not skipped. |
| **Gap** | More than 2 business days between reads restarts the run. |
| **Active-Month switch** | **2026-10-15T00:00Z = 8:00 PM EDT Wed 10/14**, Nov26 → Dec26 (ICE LTDs re-VERIFIED 10/9: Nov26 10/19 · Dec26 11/19). It resets the run and disarms. Reads are classed by UTC timestamp. The step is now $0.89 (it was $3.95 on 9/28). |
| **Clearing** | A fired state clears only on 3 qualified reads below its level. **A reset never clears a fired state** (fail closed). |
| **Resolution record** | YES is recorded when Gamma shows the market closed with YES = 1. The record is a KB row with the Pyth candle or the ICE daily high, plus VX-ORC-04 set to Critical. A news report of a print is not a record. NO is recorded at the 11/01 close; late-month decay is expiry, not de-escalation. |
| **November** | Not listed at 14:26Z. It is expected **~10/25 04:0xZ** (all seven prior months were created on the 25th; INFERRED). Pin, REGIME `v5-nov26-icewti110`, the Oct relabel and MAINTENANCE go in **one edit**, after the November text has been read. If strike, venue and rule are unchanged, it stays v5. Any difference goes to Will first. The run restarts at 0 with an entry read, never differenced against October. November's own switch is 8 PM EST Mon 11/16 = 2026-11-17T01:00Z (INFERRED from Dec26 LTD 11/19). If nothing lists, the leg pauses and ORACLE does not re-strike. |

**Caveats that must reach Will with the row:**
- ⚠️ A higher chance of touching $110 is evidence about a price event, not proof of lost physical supply.
- ⚠️ **Cadence:** ORACLE does not wake itself. The bands can arm only with pulls on most business days. With the 9/28 → 10/9 dark gap they would never have armed, so approval works only together with a pull cadence, which is PROME's to schedule.
- ⚠️ Polymarket's settlement text has been read by ORACLE only (9/28 and 10/9). No second reader has checked it.

**ORACLE rec:** approve (b) as written, with the cadence named beside it.

## Fed (the >10pp/48h triage rule plus the LIQUID ask)

The October hike has been **priced out on both venues** since 9/28: PM 65.5 → **15.5**, Kalshi `>4.00` 69 → **18.0**, and `>4.25` is 1.0. The hike has moved to **December** (PM meeting-specific 74.5; Kalshi cumulative `>4.00` 82.0). VX-ORC-08 (>66%) is no longer crossed. This is one read after an 11-day gap. LIQUID was answered late by packet (its 9/30 deadline passed while the desk was dark). KB-ORC-103.

## Inbox drain (census 10:24 ET: top-level 6 including `.gitkeep` = 5 packets · WALTER/ 2)

| Item | Disposition |
|---|---|
| PROME 9/28 v5 reads-and-resets (CATO) | **Acted:** the letter above |
| LIQUID 9/29 Fed-path ask | **Acted, late:** packet `AGENTS/LIQUID/inbox/2026-10-09_from-ORACLE_fed-path-read-oct-hike-priced-out.md` |
| PROME 9/30 WQ-305 RULED | **Acted:** charter Kalshi gap-fills moved to a dated quarterly re-check, next 2026-12-15 |
| DAEDALUS L546 float-tie | **Acted:** `kalshi.py` rounds before the edge comparisons. `scripts/test_mid_flag_edge.py` passes 7/7, and the old code fails the exact one-cent case |
| DAEDALUS wiring ⑰ run 3 | **DEFERRED, left in the inbox.** ORC-07 window and ORC-08 venue change what fires, which makes them gate letters and outside an L0 drain. The row→command map goes with them |
| WALTER SIG-W-20261008-033 (WQ-399) | **Acted:** charter receipt line rewritten in the field form. COR-20260904-02 receipted **NO-OP** (KB-ORC-075 refuted that figure on 9/4); the corrections check is rc 0 |
| WALTER SIG-W-20261008-034 (Iran, Trump midterms) | **Noted:** context for the oil read |

All 7 are logged in `board_log.tsv`; 6 moved to `processed/`. DOCKET L173/L175 were DROPPED (WQ-378); no ORACLE action.

## COMPLETION — ORACLE — 2026-10-09
STATUS: ✅ DONE
CHANGED: ORACLE analysis/2026-10-09_wq314b-v5-observation-and-reset-rules.md, CLAUDE.md, STATUS, SCRATCH, NEXUS_BRIEF, MAINTENANCE, board_log.tsv, registry/corrections_receipts.tsv, scripts/kalshi.py, scripts/test_mid_flag_edge.py, workbook/{VX,KB,ODDS_LOG,KALSHI_ODDS_LOG,DISRUPTION_SUPPLY_SPREAD}.tsv, 6 inbox→processed; LIQUID inbox packet; this memo
RESULT: WQ-314 (b) letter delivered. It sets one read per US business day, qualified at liq ≥$5K; a thin read resets; a gap over 2 business days restarts; the 2026-10-15T00:00Z Active-Month switch resets; resolutions and the November roll (~10/25) have stated rules. Levels unchanged (40/60/YES), not encoded. Oct $110 8.5% on $41.0K liq @ 14:26Z (first qualified read). Fed Oct hike priced out (PM 15.5 / Kalshi 18.0). Inbox: 6 of 7 consumed, 1 deferred.
GAPS: The DAEDALUS wiring ⑰ packet is deferred because ORC-07/08 fixes change what fires. STATUS is a partial update: alerts 2 and 5 only, the rest labelled 9/27–9/28. Resolved pins were not rolled. The coverage sweep is overdue (due ~10/01). Polymarket's settlement text has not had a second reader.
WILL_NEEDS: Rule WQ-314 (b): approve the observation and reset rules as written (ORACLE rec: approve). Note that the bands work only with near-daily ORACLE pulls.
FOLLOW-UP: PROME: re-present WQ-314 (b) before 10/14 20:00 EDT and decide a pull cadence. ORACLE: pin the November leg ~10/25–10/31 in one edit; roll resolved pins; take the deferred wiring ⑰ packet to Will via PROME.
