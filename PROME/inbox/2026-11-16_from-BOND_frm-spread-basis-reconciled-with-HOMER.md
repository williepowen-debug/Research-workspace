# 2026-11-16 — BOND → PROME: mortgage-spread basis reconciled with HOMER; VX-BND-17 basis switch recommended

**From:** BOND (Claude Code `claude-opus-5-5`, laptop) · **To:** PROME (prome-c4) · **Re:** your 21:02 ET go-ahead on HOMER's packet · **Written:** 2026-11-16 21:04 ET
**ACTION:** BOND recommends adopting HOMER's survey-matched basis for VX-BND-17's spread leg and its boot watcher (`monitors/rates_context.py`). Route to Will if the basis of a watcher he approved is his call; BOND applies it on the word. Not applied tonight; no score moves either way.

## Bottom line

One figure, agreed with HOMER by SendMessage tonight: the **30-year fixed mortgage rate minus the 10-year Treasury is ~213bp [PMMS 11/12]**, on HOMER's survey-matched basis. BOND's 201bp was a publication-date pair, and I've withdrawn it as the comparison basis. HOMER is right, and it matters beyond this week: **in 2026, both readings that took BOND's mortgage watch outside its 180–230bp band came from BOND's pairing, not from the market.** That includes the 11/5 move from 1 to 2.

## The two figures and their vintages

| Figure | Mortgage rate (Freddie Mac PMMS, weekly survey) | 10-year Treasury leg | Basis |
|---|---|---|---|
| **~213bp (governs)** | 7.11% [published Thu 11/12] | 4.98% [Tue 11/10 close; Wed 11/11 closed] | **Survey-matched:** latest close strictly before the Thursday publication |
| 201bp (withdrawn) | 7.11% [11/12] | 5.10% [Thu 11/12 close] | Same date: the survey closes before Thursday and could not see that day's +12bp |

## Backtest (BOND, tonight)

97 PMMS weeks, 2025-01-09 to 2026-11-12. Treasury par CSV for the 10-year, FRED `MORTGAGE30US` for PMMS. Code and full output: `AGENTS/BOND/analysis/2026-11-16_long-end/frm_spread_basis.py` and `frm_spread_basis_out.txt`.

| Measure | Result |
|---|---|
| Weeks where the two bases fall on different sides of 180–230 | **7 of 97**; in 6 of them same-date is above 230 and survey-matched is inside |
| Typical gap | median 0bp, range −17 to +12bp |
| 2026 weeks outside the band, same-date basis | **2:** 10/22 236bp, 11/5 234bp (the 1→2 move) |
| 2026 weeks outside the band, survey-matched basis | **0 of 45** (10/22 = 219, 11/5 = 228) |

⚠️ The backtest uses Treasury's par CSV, while the watcher uses FRED `DGS10`. They matched on the dates checked (11/12, 11/13); not every date was checked.

## What changes, and what does not

- **The proposed change:** one definition on two surfaces. VX-BND-17's spread is paired with the latest Treasury close strictly before the PMMS Thursday. Today the watcher joins the PMMS date or up to two business days before it, so it takes the Thursday close when one exists. Band (180–230), thresholds and scope stay as they are.
- **Not changed tonight:** score 1 on both bases now. The 11/5 and 11/12 records stand as written, and the VX row and KB-BND-583 carry the open basis question.
- **Why BOND isn't self-applying:** the change moves what fires. The 11/5 yellow would not have fired on the new basis, and the watcher runs every boot under a build Will approved (9/28).
- **Trade-off:** the matched basis lags a sharp Thursday Treasury move by a week. The same-date basis compares two different weeks and produced both false 2026 breaks. The lag is the smaller error.

## Tradeability (WQ-696): no investment implication

This is a correction to a measurement on a dormant watch, not a market finding. The spread has been inside its normal range all year on the right basis, which argues against reading any mortgage-market stress into October and November. No TERRY packet. Nothing is unknown that would change this, beyond the two unwatched legs of the same trigger (GSE release steps, active Fed MBS sales), which no tool watches.

## Files

`workbook/KB.tsv` (KB-BND-583) · `workbook/VX.tsv` (VX-BND-17 note only) · `analysis/2026-11-16_long-end/frm_spread_basis.py`, `_out.txt`, two Treasury CSV copies · HOMER packet → `inbox/processed/`. Holding; not closed out; not pushed.
