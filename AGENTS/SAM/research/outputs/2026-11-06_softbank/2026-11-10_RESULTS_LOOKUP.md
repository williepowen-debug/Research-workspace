# SoftBank results 11/10: the lookup, written before the print

**Written:** 2026-11-09 11:20 ET (clock), before release; the commit timestamp is the pre-registration. **Owner:** SAM. **Basis:** PROME packet 11/9 on Will's word 11:14 ET; $0. **Release:** tanshin 15:30 JST = **01:30 ET 11/10**; briefing 16:30 JST = 02:30 ET. ⚠️ LTV has historically been in the CFO's finance deck, not the tanshin (assumption, unverified for this quarter): if only the tanshin is up, the LTV rows wait for the deck.
**Not a `PREDICTIONS.tsv` row:** this tests an estimate of a quantity, not a probability call. Grading it changes no score, band or gate.
**Calculator:** `python3 ltv_lookup.py --nd <net debt ¥T> --v <value of holdings ¥T> --arm <Arm price now>` (add `--svf2-inside` if row 2 says so; `--oct-in-nd` if 9/30 net debt already carries the October tranche). `--selftest` reproduces the 11/6 figures.

## What I am testing

| My figure | Value | Basis |
|---|---|---|
| Re-mark at 11/6 close, Arm $172.34 | **22.1%** SoftBank's definition (A) · **24.2%** with the guaranteed $10B SVF2 loan (C) | `ltv_remark.py`, 11/6 |
| Same, Arm $187.71 (11/9 vendor intraday, +7.5%) | **21.3% / 23.3%** | `ltv_lookup.py` |
| **What the 9/30 headline should print** if my model is right | **15.2%** if the SVF2 loan sits outside the ratio · **17.0%** if inside | Model at Arm $289.66, before the October tranche |
| Arm price where today's figure hits 25% | **$127 (A) / $160 (C)** | Arm now $187.71: 32% and 15% above |

**SoftBank's ceiling, read at source 11/9:** LTV = adjusted net interest-bearing debt ÷ equity value of holdings; **below 25% "in normal times", upper threshold 35% even in emergencies** (SBG management-policy page; FY2026 annual report). Management said on the Q3 FY2025 call that LTV may temporarily exceed 25% and it would then explain its plan. ⇒ **Above 25% is a self-set trigger to explain a plan, not a covenant breach or a default.** 35% on the reported basis needs Arm near $28: not a live question.

## The lookup: four figures decide it

| # | Read this disclosed figure | Where | Decides |
|---|---|---|---|
| 1 | **9/30 LTV, and its two parts: net debt and equity value of holdings (¥T)** | Finance deck, LTV slide | Whether my model is calibrated; feed both into the calculator |
| 2 | **Is the SVF2 TSUBAKI $10B loan inside SBG stand-alone net debt?** Look for it in the net-debt bridge or the "self-financing entities" footnote; the guarantee in the contingent-liabilities (guarantee obligations) note | Deck footnote; tanshin notes | View A vs C, about 2 points. If inside, C **is** SoftBank's number and A was the kind one |
| 3 | **OpenAI fair value at 9/30** (was carried flat at $852B) | Deck / SVF section | A mark-up toward $1.25T lowers LTV about 2.6 points **with no cash moving**: record it separately as a mark, not deleveraging |
| 4 | **Any pro forma or "latest" LTV after 9/30**, and Gotō's words on 25% and on selling Arm, T-Mobile or SoftBank Corp | Deck, briefing | The ceiling question directly; a monetisation is the tell that 25% is being defended |

## Grading rules (fixed now)

Run the calculator on row 1's figures at the Arm price of the read.

| Result on SoftBank's own basis, rolled to now | Grade |
|---|---|
| Within **±1.5 points** of my A figure at that Arm price (21.3% at $187.71) | ✅ **Estimate CONFIRMED** |
| More than 1.5 points **above** | ❌ **REFUTED, too kind.** If it reaches 25%, SoftBank is over its own normal-times ceiling at today's prices: packet PROME |
| More than 1.5 points **below** | ❌ **REFUTED, too harsh.** Name the input that was wrong (net debt or value) |

**Quick read if only the headline percentage is out** (holding value near my ¥72.9T, Arm $187.71): a 9/30 print of **14.0–16.5%** confirms; **above 16.5%** refutes too kind; **below 14.0%** refutes too harsh. A print of **≥ 18.3%** puts SoftBank's own basis at **≥ 25% today**; **≥ 16.6%** does so for the recourse view (C) if the SVF2 loan is outside. These shortcuts are superseded by the calculator once net debt and value are read.

**Kill-on-sight in tomorrow's write-up:** "SoftBank reported 22%" (my estimate) · "leverage is 13%" (6/30 only) · "a $40B bridge wall" (repaid 9/15, cancelled 9/30) · a 9/30 headline quoted as today's leverage (Arm was $289.66 then).

## Also read (from `SOFTBANK_FUNDING_STACK.md` §6, unchanged)

SVF2 loan drawn and the OpenAI fair-value trigger input (§6 #3) · Arm margin loan drawn, pledged shares, maturity (#5) · borrower, collateral and recourse of the $11.87B and Apollo loans (#6; if outside the ratio, A falls toward 18.8% at today's Arm) · cash against two years' redemptions, ¥2.3T vs ¥1.5T at 6/30 (#7) · ABB (#8) · **commitments and guarantees note (#9): any SBG guarantee of SB Energy obligations, which is the only way Musk's turbine claim (card 20261109-005, unverified) would reach SoftBank's leverage.** SBG's own share price (¥3,400, −4.2% on 11/9) is not in its LTV; its holdings are.

## Japan consequence, for the after-results packet

Unchanged from 11/6: no bank or household break found; per-bank exposure undisclosed; senior retail bonds about ¥3.9T, 0.16% of household financial assets. A reported basis at or above 25%, a rating action, or a pulled yen retail deal is what would move it (combo theme KB-SAM-262).

Sources: [SBG management policy](https://group.softbank/en/ir/investors/management_policy) · [FY2026 annual report](https://group.softbank/media/Project/sbg/sbg/pdf/ir/financials/annual_reports/annual-report_fy2026_03_en.pdf) · [Q3 FY2025 call](https://group.softbank/media/Project/sbg/sbg/pdf/ir/presentations/2025/earnings-conference-call_q3fy2025_01_en.pdf) (search snippets 11/9; the 25%/35% wording matches across all three, page text not re-read) · Arm, 9984.T, USD/JPY: `fetch.py` 11/9 about 11:15 ET, vendor intraday · 9/30 USD/JPY 157.434, own ledger.
