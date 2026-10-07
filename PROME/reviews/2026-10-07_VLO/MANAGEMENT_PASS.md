# VLO management pass — October 7, 2026

PROME, Codex `/root`, evidence checked 13:40–13:45 EDT. Will requested this pass in-session. Scope: the ONE held share and existing WQ-330 management letter; consumer verification and decision preparation, not a TERRY owner grade or a new order.

**Disposition: no exit trigger established by the evidence checked. Existing management letter remains in force through October 14. The two additional shares remain stood down under the separate terminal scale gate. The overdue month decision and owner review remain OPEN.**

## Position and price evidence

Will answered **“Yes, still one share”** to “For this VLO review, do you still hold the one Fidelity share bought September 18 at $412?” on October 7 in this session. Quantity/continued holding is now operator-confirmed. This is not a new broker capture, current mark, activity reconciliation, or fill receipt; no account totals or P&L are refreshed.

Independently recalculated the saved 13:07 EDT vendor capture from `HOX26.NYM_1m.csv` and `CLX26.NYM_1m.csv`. Each leg has all three 14:28, 14:29 and 14:30 EDT bars. Typical-price VWAP is calculated separately by leg, then HO×42−CL. Named November identities and vendor expiries are in `evidence.json`; no continuous series used. This replicates the saved arithmetic, not an independent market-data source.

| Completed session | Matched November crack, $/bbl | Existing held-share letter |
|---|---:|---|
| October 2 | 97.93763 | Above both lines |
| October 5 | 101.44597 | Above both lines |
| October 6 | 102.50577 | Above both lines |

October 6 is **$7.34577 above the $95 notice line and $12.34577 above the $90.16 exit line**. Single-vendor settlement-window ESTIMATE, not CME settlement. The saved October 6 daily rows repeat October 5 volume and remain rejected under the existing rule. October 7 settlement has not happened at this pass. There is no new stock-price stop and no new add instruction.

## Policy and operating context

- **B1:** Read the [October 5 signed White House diesel order](https://www.whitehouse.gov/presidential-actions/2026/10/emergency-tax-relief-on-diesel-fuel/) and [Presidential Actions index](https://www.whitehouse.gov/presidential-actions/) again. The order directs tax-payment deferral and penalty relief; it contains no operative diesel export ban, cap or licensing restriction. This specific order does **not** satisfy B1. The earlier saved Federal Register searches and this pass's targeted search establish no qualifying restriction, not exhaustive absence or continuous monitoring.
- **B2:** Valero IR news and SEC company pages returned dynamic shells; targeted primary-domain searches found no qualifying Valero export-curb announcement. **Coverage remains incomplete; absence is not certified.** A Valero commitment would require TERRY review, not an automatic sale.
- **B3:** The current [EIA Table 9, page 21](https://www.eia.gov/petroleum/supply/weekly/pdf/table9.pdf) now supplies the missing export observation: week ending **October 2**, estimated distillate exports **1.764 million b/d**, versus **1.529 million b/d** the prior week; four-week average **1.560 million b/d**. Change = +235,000 b/d, about +15.4%. This closes the earlier consumer report's B3 data gap. Aggregate exports rose in this reporting week; this neither proves Valero's own behavior nor describes the days after October 2. B3 never triggers an exit.
- [EIA Table 1](https://www.eia.gov/petroleum/supply/weekly/pdf/table1.pdf): distillate stocks 105.1 million barrels, 13.5% below year ago; four-week supplied 3.769 million b/d, down 1.6% year over year. [Table 2](https://www.eia.gov/petroleum/supply/weekly/pdf/table2.pdf): distillate output 5.290 million b/d, +287,000 b/d week over week. Inference: no evidence here of aggregate export collapse, with softer demand alongside low inventories. These are context, not new gate criteria.
- [Valero events page](https://investorvalero.com/events-and-presentations/default.aspx): Q3 earnings call **October 22, 10:00 ET**. Current price-leg authority expires before that catalyst.

## Contract-month decision: evidence assembled, proposed safeguard not ready

DAEDALUS's October 1 options memo and HENRY's October 2 response have both been consumed. Files: `PROME/inbox/processed/2026-10-01_from-DAEDALUS_WQ-252-crack-contract-month-options-memo.md` and `PROME/inbox/processed/2026-10-02_from-HENRY_WQ-252-step-measurements-and-calibration-pair.md`. TERRY's consequence delivery was not found in its current STATUS, relevant setup or searched inbox/processed packets. Owner discovery remains incomplete, so no potentially duplicate writing launch was made.

| Existing option | Practical consequence for the held share |
|---|---|
| A: December from October 15 | A real matched December reading; one switch before November crude expiry. The month switch itself can lower the measured margin toward either line. |
| A′: November through October 19, December from October 20 | Extends November authority three trading sessions beyond October 14; needs Will's ruling. Same potential downward step, later. |
| B: December plus frozen Nov−Dec adjustment | Preserves continuity at the chosen observation but measures an adjusted series, not the actual December margin. The offset depends on the chosen day's curve. |
| C: persistence or changed separation | Changes exit timing/threshold semantics; not merely a month selection. |
| D with A/A′: ±2-session two-month comparison | Proposed suppression of a one-month-only crossing can delay a real exit; requires explicit missing-data treatment when the outgoing contract no longer trades. |

September Nov−Dec median step **$4.72/bbl**, range −$0.03 to $7.24. Both months straddled $95 on 7/21 sessions, but $90.16 on 0/21. HENRY and DAEDALUS use the SAME vendor; agreement is not independent confirmation. Historical frequencies are not forward probabilities.

**Material calibration caveat:** HENRY withdrew its statement that July 23's $90.16 baseline was verified as a matched pair. The heating-oil contract identity is UNKNOWN. None of these month choices repairs that uncertainty or establishes a newly calibrated exit level.

**New PROME implementation finding, not an owner ruling:** A′ switches October 20, the recorded CLX26 last-trade date. The ±2-session window is October 16, 19, 20, 21 and 22. October 21–22 cannot provide fresh matched November observations once CLX26 stops trading. The memo does not specify how D resolves a one-month-only crossing on those days. Its stated “up to two sessions” delay is therefore not established by the written rule: with missing data treated as UNKNOWN, a resolution instruction is still needed. Do not reuse the expired leg's last value as a current observation. No calendar rows were exposed by the CME calendar page at this touch, so the date premise retains the memo's vendor-expiry basis.

PROME withholds endorsement of **A′+D as operationally complete** pending the TERRY/DAEDALUS consequence and missing-data clarification. This does not amend or withdraw the owners' memo or any existing gate. Option A is already described in the memo and avoids this particular post-expiry overlap within its October 15 ±2-session window, but selecting it remains Will's decision and does not fix the calibration caveat.

## Record and remaining work

Recorded Will's quantity confirmation and corrected the stale staged-share descriptions in FORGE from the existing terminal gate; October 1 marks/account vintage retained. Added sourced receipt to existing DOCKET L471/L472; no new workstream, threshold, review date, gate grade or approval created. Prior staged evidence files remain untouched.

Needed before a complete extension: TERRY's consequence read, a precise resolution of D's unavailable outgoing contract if D remains proposed, and Will's month ruling. Without a ruling, **A becomes SUSPENDED/UNKNOWN after October 14; B1 continues** until sale or withdrawal. No automatic monitoring exists. This pass establishes no immediate sale/add action and does not clear the overdue owner-review gate.
