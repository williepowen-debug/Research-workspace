# BROCK → PROME (prome-75): Kellermeyer vs FSK SOI · BRK-31 bank-Q3 frame

**Date:** 2026-10-09 Fri 11:00 ET (`date`) · **Session:** fresh bounded Tier-1 spawn (Opus), Will's 10:24 ET idle-desk list #9 · **Runtime:** Claude Code, model claude-opus-5-5; booted from root + `AGENTS/BROCK/CLAUDE.md` by explicit read.

## 1. Kellermeyer on FSK's schedule of investments — FOUND (VERIFIED at EDGAR)

FSK Q2-26 10-Q (acc 0001628280-26-053783, period 6/30/26, filed 8/6/26 — FSK's latest periodic report). Kellermeyer Bergensons Services LLC is a **control investment** of FSK (footnote ad), not an unnamed "KKR affiliate".

| Position (6/30/26) | Par | Amortized cost | Fair value | FV % of par | Status |
|---|---|---|---|---|---|
| 1st lien A, SF+5.3% PIK, 11/2028 | $229.6M | $226.8M | $226.0M | 98.4% | **Accruing**; H1-26 income all PIK, $10.7M; cash interest $0 |
| 1st lien B, SF+8.0% PIK, 11/2028 | $107.9M | $94.3M | $10.9M | 10.1% | **Non-accrual** (z), non-income producing (y) |
| Preferred (26,230,661 units) | — | $48.3M | $0 | — | — |
| Common (26,230,661 units) | — | $0 | $0 | — | — |
| **Total** | | **$369.4M** | **$236.9M** | 64.1% of cost | |

Tranche B fair value: $87.7M (12/31/24) → $40.3M (12/31/25) → $13.1M (3/31/26) → $10.9M (6/30/26). Tranche A: $201.6M → $220.3M → $225.0M → $226.0M. **Semafor's "~10¢ to ~100¢" is confirmed at primary.** Context: FSK's Form 40-33 (0001104659-26-084660) is *St. Louis ERS v. FS/KKR Advisor*, SDNY 1:26-cv-06003, a §36(b) fee suit filed 7/15/26. Its §VI.A is a Kellermeyer case study (serial PIK conversions, selective non-accrual). These are allegations. **No vector or score moved.** It does not grade BRK-25, because a mark on a controlled company is not an arm's-length print. KB-BRK-325. Next mark: FSK Q3 10-Q, ~early November.

## 2. BRK-31 bank-Q3 frame: it did NOT exist, so I wrote it and froze it

The BRK-31 letter (7/27) and a CATALYSTS row existed. **No per-bank frame with numbers and operators existed.** It is written now at `AGENTS/BROCK/research/2026-10-09_BRK-31_bank-Q3_frame_FROZEN.md` and frozen at this commit, before JPM's ~07:00 ET release on Tue 10/13. It contains:
- **8 reading rules.** What counts as the "print". BUILD means the attributed ACL rises, or provision exceeds charge-offs with the bank attributing the excess (strictly `>`; no magnitude floor, because the letter sets none). Attribution must be in the bank's own words. A named exclusion list: mortgage warehouse, card or seasonal builds, office CRE, generic C&I, macro-weighting builds. The F2 counterparty must be the PC vehicle itself, not a portfolio company. Press reports do not grade. GS/BAC/MS are context only. Supervision is not a print.
- **Per-bank table for all 11 names**, with the Q2 baseline, what fires F1 and F2, and the named traps.
- **Outcome table.** Q3 alone cannot resolve BRK-31 FALSE. A bank that does not disclose the category is INSUFFICIENT, never read as flat.
- **Two weaknesses declared before the data.** A token NDFI-labelled build fires in a world where private credit is fine (no floor). GSIB releases often do not split wholesale reserves.

**No threshold, population or confidence moved. GATE-BRK-R2 untouched. The OTIC letter stays FROZEN pending WQ-403.**

## 3. Date correction: Wells Fargo prints Tue 10/13, not Wed 10/14 (VERIFIED at the issuer)

The WFC newsroom update dated 2/20/26 moved Q3 to Tue 10/13, ~07:00 ET (call 10:00). JPM is Tue 10/13 ~07:00 (call 08:30, JPM IR 9/17). C is Tue 10/13 ~08:00 (call 11:00, Citi PR 10/2). GS is Tue 10/13 ~07:30 (context). MTB is Fri 10/16 pre-open (syndicated M&T PR 9/18). My 10/2 note marked WFC 10/14 as "verified"; that was wrong, and I have fixed it in STATUS, CATALYSTS, NEXUS_BRIEF and SCRATCH (KB-BRK-327). **Other desks still carry WFC 10/14:** `AGENTS/WALTER/research/2026-10-09_morning/{morning-sweep,desk-status-context}.md` · `AGENTS/TERRY/setups/HBAN_oct16-16P_ITM-management-card_2026-09-26.md` · `AGENTS/CARL/SCRATCH.md`. Not edited; flagged here.

## 4. By-catch: a BRK-26 spec question (not graded)

The complaint cites **SEC *In re Madison Capital Funding LLC*, IA Rel. 6948, AP 3-22599, 2/25/26**. I read it in full at sec.gov. It is a settled formal action on a private-credit lender's loan-valuation pricing: sales to its own funds at par-less-fee without determining fair market value, Mar–May 2020. Penalty $900K plus censure. **It predates BRK-26's registration (5/1/26) by 65 days.** My KB had no row for it, and STATUS's "NO CHARGES on any PC-valuation matter" was false as a historical statement; that line is now qualified. BRK-26's letter ("First SEC enforcement filing … by Q4 2026") does not say whether a pre-registration filing counts. **That is a spec question for the letter's owner chain (RED/Will), not mine to settle.** Confidence stays at 55%. KB-BRK-326.

Price: FSK $10.90 [fetch.py 2026-10-09 ~11:00 ET].

```
STATUS: ✅ DONE
CHANGED: AGENTS/BROCK/{research/2026-10-09_BRK-31_bank-Q3_frame_FROZEN.md (new), workbook/KB.tsv (KB-BRK-325..327), STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, docket/CATALYSTS.tsv, catchups/2026-10-09.md, catchups/INDEX.md}, this memo
RESULT: Kellermeyer FOUND on FSK Q2-26 SOI as a control investment: tranche A $226.0M FV (98.4% of par, accruing PIK), tranche B $10.9M (10.1%, non-accrual), equity $0; total FV/cost 64.1%. BRK-31 frame did not exist — written and frozen pre-print (8 rules, 11-bank table, F1/F2, traps). WFC Q3 is Tue 10/13, not 10/14 (issuer).
GAPS: Dates for CFG/WAL/OZK/EGBN/BKU/SSB/AMTB cited to REGINALD's 10/7 issuer verification, not re-read; MTB read via syndicated issuer text. No score/threshold/population moved.
WILL_NEEDS: None new. BRK-26 'first' spec question (Madison Capital order 2/25/26 predates registration) may need a ruling — PROME to route (RED/Will).
FOLLOW-UP: PROME: notify WALTER/TERRY/CARL of WFC 10/13; route BRK-26 spec question. BROCK: read JPM/WFC/C Tue 10/13 against the frozen frame; CABO same morning.
```
