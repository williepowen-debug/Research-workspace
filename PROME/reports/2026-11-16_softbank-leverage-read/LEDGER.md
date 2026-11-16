# SoftBank leverage roll: independent check of SAM's 22.5% / "25% at Arm about $145"

**Checker:** independent read-only subagent, spawned by PROME on 2026-11-16. I did not make the estimate. **Cost:** $0. Public web only; no Quartr and no paid data. **Time used:** about 25 minutes.
**Object checked:** SAM `AGENTS/SAM/STATUS.md` line 7; `research/outputs/2026-11-06_softbank/2026-11-10_RESULTS_GRADE.md`; `ltv_lookup.py`; `ltv_fx_sensitivity.py`.
**Primary sources:** SoftBank Group IR PDFs, downloaded by curl on 2026-11-16 at about 14:10 ET into a mktemp scratch directory outside the repo.

| File | SHA-256 prefix (mine) | SHA-256 prefix (SAM's record) |
|---|---|---|
| `investor-presentation_q2fy2026_01_en.pdf` (Finance and Accounting sections) | 1e5ced7c | a9c2649e (**differs**) |
| `earnings-presentation_q2fy2026_01_en.pdf` | ec90cfa4 | 1e69c9ec (**differs**) |
| `financial-report_q2fy2026_01_en.pdf` | c3fa95f8 | c3fa95f8 (match) |
| `earnings-datasheet_q2fy2026_02.pdf` | 87990f8b | 87990f8b (match) |

Page references below are SoftBank's printed slide labels, for example "Finance 40".

## 1. Inputs

| Input | SAM's value | Value found | Source, date | State |
|---|---|---|---|---|
| Adjusted SBG stand-alone net debt, 9/30 | ¥11.30T | ¥11.30T = 18.56 stand-alone before adjustment − 0.76 hybrid − 6.49 asset-backed (Arm 3.90, SBKK 1.20, Intel collar 1.14, T-Mobile collar 0.26) | Investor deck Finance 41–42, as of 2026-09-30 | VERIFIED |
| Adjusted equity value of holdings, 9/30 | ¥71.14T | ¥71.14T = Arm 38.16 (42.06 gross − 3.90 margin loan) + SBKK 3.42 + T-Mobile 0.00 + SVF1 3.45 + SVF2 20.07 + LatAm 0.96 + Others 5.07 (6.31 − 1.24 Intel collar) | Finance 39–40 | VERIFIED |
| LTV, 9/30 | 15.9% | 15.9% | Finance 6, 39, 41 | VERIFIED |
| Arm price, 9/30 | $289.66 | $289.66 | Finance 23 chart | VERIFIED |
| Arm ADSs held by SBG | 923M | 922.8M (my arithmetic: $267.3B ÷ $289.66; deck gives $267.3B, ¥42,056.4B). The pro forma gives the same: (23.3 + 3.92) ÷ 158.34 ÷ $186.30 = 922.8M. The Q2 bridge's Arm −¥9.7T is also consistent: (354.57 − 289.66) × 922.8M ≈ $59.9B ≈ ¥9.5–9.7T | Finance 23, 40, 45 | VERIFIED |
| USD/JPY, 9/30 base | 157.35 | $1 = ¥157.35 (and €1 = ¥178.34) | Finance 7 note | VERIFIED |
| USD/JPY at the roll | 158.63 (vendor, 10:06 ET 11/10) | Not checked at a source. SoftBank's pro forma uses 158.34 (11/9) | — | NOT REACHED |
| Arm price at the roll | $183.26 (vendor intraday, 10:06 ET 11/10) | Intraday not verifiable. 11/10 close $181.49 (Benzinga and MarketScreener, secondary, −2.58% on the day), which implies an 11/9 close of $186.30, matching SoftBank's pro forma price | [Benzinga](https://www.benzinga.com/quote/ARM/charts), [MarketScreener](https://in.marketscreener.com/quote/stock/ARM-HOLDINGS-PLC-159091235/), read 11/16 | NOT REACHED (intraday); bracket consistent |
| October OpenAI tranche | +$10B to both net debt and value | Third tranche of $10.0B, funded 10/1 (a subsequent event). It was funded from Q2 bond proceeds, so SBG cash falls and net debt rises. OpenAI fair value $99.6B at 9/30; SVF2 position about $110B after the tranche, carried at cost | Financial report note 16(1)d and note 17; Accounting 4–5; Finance 8 | VERIFIED (debt side); value-at-cost INFERRED from the $110B |
| SVF2 OpenAI-shares loan | Inside the ratio | Inside: it is SBG stand-alone debt and is excluded from the SVF2 NAV. ¥1,543.7B outstanding. Margin-call trigger references the value of OpenAI preferred shares; guaranteed by SBG; no pledge of OpenAI shares | Finance 20, 40, 42 *1 | VERIFIED |
| Margin loans and asset-backed finance | Netted from both sides | Netted from both sides: Arm ¥3,896.9B, SBKK ¥1,197.5B, Intel and T-Mobile collars | Finance 40, 42 | VERIFIED |
| Arm shares pledged | Not used in the roll | **769,029,000 of 922.8M** pledged. Loan ¥3,896.9B (about $24.8B), maturity extended to Sep 2028. Cash-collateral and prepayment clauses trigger on a "significant decrease" in the pledged shares' value. Non-recourse to SBG | Financial report p.67 note 5 | VERIFIED |
| Hybrid bonds | Not separately used | Dated hybrids: 50% deducted from debt. Perpetuals: 50% added to debt. Net adjustment −¥0.76T | Finance 42 | VERIFIED |
| Vision Funds | Held flat except the tranche | SVF1, SVF2 and LatAm are carried at SBG's share of NAV and calculated in USD. The pro forma holds SVF listed shares at 9/30 prices | Finance 40; pro forma note *1 | VERIFIED |
| Pro forma at 11/9 | Equity value ¥56.0T, implying 20.2% without the tranche | Equity value ¥56.0T and NAV ¥44.7T, at 11/9 closes and FX for **Arm, SBKK and Intel only**. "**Sep 30 for other listed shares**." Excludes the third tranche. No LTV % printed | Finance 23, 11 | VERIFIED |
| 25% ceiling | Normal-times ceiling, 35% extraordinary | "Maintain LTV below 25% in normal circumstances (upper threshold of 35% even in extraordinary circumstances)", headed "Adherence to Financial Policy". A policy, not a covenant: "covenant" has zero hits in the financial report | Finance 6, 11, 12 | VERIFIED (policy wording); covenant absence = SEARCH-NOT-FOUND |
| Debt or asset changes 10/1–11/9 | Only the tranche | The deck's "FY2026 Q3 (through Nov 9)" table lists only the $10B OpenAI tranche. Upcoming: ABB $5.4B "Q3 onwards", with $1.8B of LBO finance. Some foreign senior bonds were redeemed early in October; that is cash-for-debt and leaves net debt unchanged | Finance 8, p.1794 note | VERIFIED |
| ABB status | Conditional add of 23.4–23.9% | China **prohibited** the acquisition of ABB's robotics business in China (notified 2026-11-04). The parties are "working constructively". Not closed | Financial report note 16(2) | VERIFIED (SAM already logged this in `SOFTBANK_FUNDING_STACK.md`) |

## 2. Reconstruction of SAM's arithmetic (`ltv_lookup.py --nd 11.30 --v 71.14 --arm 183.26 --fx 158.63 --svf2-inside`)

- October tranche: $10B × 158.63 = ¥1.586T.
- Net debt: 11.30 + 1.586 = **¥12.886T**.
- Arm move: 923M × (183.26 − 289.66) × 158.63 = −$98.21B × 158.63 = −¥15.578T.
- Value: 71.14 + 1.586 − 15.578 = **¥57.148T**.
- LTV = 12.886 ÷ 57.148 = **22.55%**, so **22.5% follows**.
- Arm price at 25%: required value = 12.886 ÷ 0.25 = 51.545. Arm = 183.26 + (51.545 − 57.148) × 10¹² ÷ (923M × 158.63) = 183.26 − 38.27 = **$144.99**, so **"$145" follows**.
- Convention in this script: the 9/30 base stays at 157.35. Only the post-9/30 Arm move and the tranche are converted at 158.63. Debt is not revalued for FX. SAM's later full-revaluation script gives the same 22.5% at $181.49 and 158.81.
- Repeat by a second route, mine: start from SoftBank's own 11/9 pro forma (V ¥56.0T, L ¥11.30T), then:
  - move Arm from $186.30 to $183.26;
  - FX 158.34 → 158.63 on the 95% USD holdings;
  - revalue the foreign 62% of net debt from 157.35 to 158.63;
  - add the tranche to both sides.
  - Result: L 12.943 ÷ V 57.239 = **22.61%**, and 25% at **$145.9**. Rounding the pro forma's 56.0 by ±0.05 moves this by ±0.02 point. **SAM's two numbers reproduce on SoftBank's own basis.**

## 3. Tests

| # | Test | Finding | RAN / INFERRED |
|---|---|---|---|
| a | Arm's share of holdings; margin-loan netting | At 9/30, Arm net was ¥38.16T, 54% of value. At $183.26 it is ¥22.9T, **40%**. The margin loan is netted from both sides at a fixed amount, so the full gross price change flows to value. SAM's elasticity is right: $1 on Arm ≈ ¥0.146T of value. 769.0M shares are pledged. Loan-to-collateral is 17.6% at $183.26 and 22.2% at $145. The trigger level is not disclosed. The loan is non-recourse, but a cash-collateral call would draw SBG cash and raise net debt. Drawing *more* margin loan *lowers* the reported ratio: the Q2 bridge shows "Increase in Arm margin loan −0.8ppt". The facility is nearly full ($24.8B drawn of $25B) | RAN (deck, financial report); trigger behaviour INFERRED |
| b | Other holdings held constant | SBKK, Intel and FX moved to 11/9 inside SoftBank's pro forma, and SAM's cross-check shows they net to about zero. **Still held at 9/30 by both SAM and SoftBank:** non-Arm, non-SBKK, non-Intel listed shares (SVF listed holdings and other listed). Their size is about ¥2.8T, my arithmetic: listed share 63% × 71.14 = 44.8, minus Arm 38.16, SBKK 3.42 and Intel net about 0.41 (Intel gross ¥1.645T − collar ¥1.236T). ±20% on them moves the ratio by about ∓0.2 point. **The OpenAI mark is held at $99.6B + $10B, about ¥17.4T, 30% of value at Arm $183.26.** ±20% moves LTV to 21.3% / 24.1%. T-Mobile is collared to zero, so its price does not matter | RAN for sizes; price moves of the unmoved holdings NOT REACHED (no 11/10 quotes pulled) |
| c | Yen | Full revaluation with 95% USD holdings and 62% foreign net debt gives 22.61% vs SAM's 22.55% at the same inputs. A stronger yen *raises* the ratio, about +0.04 point per yen (SAM's full-revaluation script). `ltv_lookup.py` gives the wrong FX sign; SAM has already flagged this. Immaterial at these rates | RAN (own arithmetic) |
| d | Debt added since 9/30 | Tranche: in SAM's roll. **Not in SAM's headline:** (i) the SB7 power-equipment settlement, ¥140.2B to be paid in cash "from Q3 onward" (SAM logs it separately as 22.8%); (ii) **interest and operating carry**. SoftBank's own Q2 bridge shows "Payments of interest +0.4ppt" in one quarter, about ¥0.28T at Q2's value. Over the 41 days from 9/30 to 11/10 that is about ¥0.125T (my arithmetic), +0.2 point. (iii) No bridge loan, new margin loan or other borrowing is listed through 11/9 | RAN (bridge figure); carry pro-rating INFERRED |
| e | Asset sales since 9/30 | None listed in SoftBank's through-11/9 table. A Lenskart block sale on 11/6 (about $0.2B, secondary, [fourweekmba relaying PTI/BSE](https://fourweekmba.com/ai-softbank-sells-1-56-of-lenskart-for-1896-crore-in-blocks/)) is about −0.04 point if the cash reaches SBG; it may sit inside SVF | RAN (deck); Lenskart = secondary |
| f | Nature of 25% / 35% | Financial policy ("Adherence to Financial Policy"). 35% is the "upper threshold even in extraordinary circumstances". No LTV covenant found in the financial report. Being above 25% is a policy breach that management must explain, not a default. Covenant terms in the bank-loan agreements were not read | RAN (deck); covenant absence SEARCH-NOT-FOUND |

## 4. My estimates

**LTV at Arm $183.26 (SoftBank's basis, October tranche in, OpenAI mark held, ABB excluded): 22.4%–23.3%, central about 22.6–23.1%.**
- Low end: unmoved listed holdings +20%, no carry.
- High end: interest carry ¥0.125T, plus the SB7 settlement ¥0.14T, plus unmoved listed holdings −20%.
- Outside this core range:
  - OpenAI marked −20% / +20%: 24.1% / 21.3%.
  - ABB closes debt-funded: 23.7–24.2% (with carry and SB7).

**Arm price at 25%: $142–$157, central about $146–$153.**
- $142: unmoved listed holdings +20%.
- $146: SoftBank's own pro forma path.
- $149: plus carry.
- $153: plus carry and SB7.
- $157: plus carry and SB7, with unmoved listed holdings −20%.
- Outside the range: ABB $163–171 · OpenAI −20% $170 · OpenAI +20% $122.

**Against SAM:** 22.5% sits at the bottom of my LTV range, about 0.1–0.8 point low. **$145 sits at the generous end of my crossing range; the central case is $1–8 higher**, because SAM's headline carries no net-debt drift after 9/30.

**Check of my own, not in SAM's work:** I sized the drift from SoftBank's own Q2 LTV bridge ("Payments of interest +0.4ppt"; "Others" +0.7). Each ¥0.1T of net debt moves the 25% crossing by about $3 of Arm. I also sized the holdings that *both* SAM and SoftBank's pro forma leave at 9/30 prices (about ¥2.8T of other listed shares, plus OpenAI at 30% of value), using the deck's 63% listed-share figure and the Intel collar amounts. SAM's cross-check against the pro forma cannot catch either: the pro forma shares the same blind spots.

## 5. Findings

| # | Class | Finding | Proposed correction |
|---|---|---|---|
| F1 | **BLOCKING** (the $145 only) | "25% at Arm about $145" is the most favourable point of the range. It carries no net-debt growth after 9/30: interest carry about ¥0.125T, and the SB7 settlement ¥0.14T, which SAM itself identified. Each ¥0.1T moves the crossing by about $3. A consumer citing $145 as the 25% line overstates the cushion by about $4–8 of Arm price | Cite **"25% at Arm about $146–153 on SoftBank's basis (ABB excluded, OpenAI mark held); $145 = no drift since 9/30"**. Keep ABB and OpenAI as named scenarios |
| F2 | NON-BLOCKING | The 22.5% reproduces exactly (22.55%) and by a second route (22.61%). With carry and SB7 it is about 23.1% | State it as "22.5–23.1% depending on post-9/30 cash outflows" |
| F3 | NON-BLOCKING | The OpenAI mark (about ¥17.4T, now 30% of value) is held flat. It is the second-largest swing factor after Arm (±20% → 21.3% / 24.1%, crossing $122 / $170). The SBG-guaranteed $10B loan has a margin trigger keyed to OpenAI share value | Name it as a conditional beside every rolled figure |
| F4 | NON-BLOCKING | About ¥2.8T of other listed holdings (SVF listed and others) sit at 9/30 prices in both SAM's roll and SoftBank's pro forma. SAM's "✅ pro forma cross-check" therefore cannot test them | Note the shared blind spot; reprice them if a bigger move is suspected |
| F5 | NON-BLOCKING | 769M of 922.8M Arm shares are pledged; the trigger is undisclosed; the loan is non-recourse. SoftBank can *lower* its reported ratio by drawing more margin loan (Q2: −0.8ppt), but the Arm facility is about full | Add: "25% is managed, not mechanical; asset-backed headroom on Arm is about nil at the current facility" |
| F6 | NON-BLOCKING | 25% / 35% is policy wording, not a covenant (VERIFIED wording; covenant absence SEARCH-NOT-FOUND). SAM's STATUS already says this | None |
| F7 | NON-BLOCKING | ABB is not closed and China prohibited the China leg on 11/4. SAM's ABB-inclusive 23.4–23.9% / $156–164 must stay a scenario, never the base | Keep it as a conditional |
| F8 | NON-BLOCKING | The SHA-256 prefixes of the investor and earnings presentations I downloaded on 11/16 differ from SAM's recorded prefixes. The figures used are identical. Possibly a re-posted file | Re-hash, or note the version |
| F9 | NON-BLOCKING | The $183.26 intraday price and 158.63 are unverifiable vendor ticks. The 11/10 close of $181.49 (secondary) gives about the same ratio | Prefer completed closes for registered figures |

**Not reached:** prices on 11/10 for the non-Arm listed holdings; the text of bank-loan covenants; the margin-call thresholds (undisclosed); Gotō's spoken words (only a secondary AI transcript exists, per SAM).
