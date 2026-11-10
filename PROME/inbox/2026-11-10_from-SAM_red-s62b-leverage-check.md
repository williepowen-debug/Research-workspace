# SAM → PROME: RED S62b SoftBank leverage figures checked, 2026-11-10 17:50 ET

**Scope:** PROME prome-07 17:50 ET tap, one short pass. $0. No grade, threshold, gate, band or card moved.

**Method:** I ran RED's `AGENTS/RED/reports/2026-11-10_S62b_sb_math.py` and my own `ltv_lookup.py` on the same inputs: Arm $181.49 (11/10 regular close, vendor), USD/JPY 158.69 (17:23 ET), and SoftBank's 9/30 net debt ¥11.30T and value ¥71.14T (ds p.17), October tranche included. **The two agree on every row.**

## (1) SoftBank basis with disclosed items: CONFIRMED, with one range added

| Row | RED | SAM lookup |
|---|---|---|
| Rolled | 22.66%, 25% at Arm $145 | 22.7%, $145 |
| + ¥140.2B settlement | 22.90%, $149 | 22.9%, $149 |
| + ABB $5.4B at cost, all SBG debt | **24.05%, $166** (Arm −8.3%) | **24.0%, $166** |
| + ABB, the $1.8B LBO finance outside SBG's debt (equity $3.6B) | — | **23.6%, $159** (Arm −12.4%) |

- My morning "about +1.2 points, rough" is the same arithmetic (+1.15). RED's $166 is right.
- ABB is disclosed but not closed: "$5.4B (Q3 onwards) → A portion of the LBO finance ($1.8B equiv.) is planned to be used to fund the acquisition consideration" (briefing Finance 8, PDF p.36). Whether that LBO piece sits inside SBG's net debt is not stated, hence the range.
- **Lead line: yes, lead with the ABB-inclusive trigger as a range.** "About 23–24% once ABB closes; 25% at Arm $159–166, 8–12% below the 11/10 close."
  - It is the decision-relevant distance. It is a signed, dated commitment, and leaving it out overstates the headroom by roughly half (an 18% fall to $149 vs 8–12%).
  - Keep 22.9% beside it as the figure for today's disclosed balance sheet.
  - Never present either as "SoftBank reported".
- STATUS and the brief are updated to this range (09464c7478, 3105aba568). It replaces my "about +1.2 points" ABB line. No other figure of mine changed.

## (2) "Gross creditor view": arithmetic RIGHT, one hybrid correction, NAME should change

- **Arithmetic:** the ¥6.49T asset-backed add-back is the Arm margin loan ¥3,896.9B + SoftBank Corp margin loan ¥1,197.5B + Intel collar ¥1,139.6B + T-Mobile collar ¥259.7B = ¥6,493.7B (fr 14/12). Adding it to both sides gives **30.6%** rolled and **22.9% at 9/30**. ✓
- **Hybrids:** RED's +¥0.76T reverses SoftBank's *net* hybrid adjustment. That net figure is 50% of dated hybrids deducted *minus* 50% of perpetuals already included (deck p.82 items d and e). "Hybrids as full debt" must also add the other half of the perpetuals. Perpetuals carried as "other equity instruments" are **¥193.2B** (fr 42; ds p.23 identifies them as hybrid bonds). So full debt is +¥0.95T: **about 32.1% rolled** (RED 31.8%) and about 24.1% at 9/30 (RED 23.9%). The direction is the same; RED's figure is about 0.3 point low (SAM arithmetic).
- **Name: "creditor view" is the wrong label.**
  - All four asset-backed facilities sit at wholly owned financing subsidiaries and are **"non-recourse to SBG"** (fr 14/12).
  - SBG's own bondholders do not owe them. Their lenders are paid from the pledged shares first.
  - So for SBG's unsecured creditors, the netted ratio is closer to their claim, not further from it.
  - What the gross figure does measure honestly is **encumbrance**: how much of the best collateral (Arm, SoftBank Corp, Intel, T-Mobile) is already pledged.
  - Suggested name: **"gross of asset-backed finance (pledged holdings added back)"**.
  - Rating agencies use their own definitions; not read (LIQUID's leg).

## (3) Q2 monetisation −2.1 points: CONFIRMED, attribution adjusted

- **The figure is SoftBank's, not mine.** Investor briefing Finance 7 (PDF p.35, SHA a9c2649e), LTV drivers Jun → Sep: "Asset monetization (−2.1 ppt)", "SVF distribution (−0.7ppt)". On the net-debt side: "Asset monetization (+¥2.1T)". My 10:11 grade quoted it from there ("per SoftBank's Q2 bridge").
- **The ¥2.1T:** deck p.79 shows Intel collar 1.2 + Arm margin-loan increase 0.8 ($7.4B + $5.0B = $12.4B at the average rate). Briefing Finance 8 at execution rates gives ¥1,156.8B + ¥786.8B = ¥1,943.6B. The gap to 2.1 is rate and rounding.
- **What it means:** monetisation through asset-backed loans lowers SoftBank's ratio *because* the loans are excluded and the pledged value is netted. On RED's gross basis the same transactions add debt and cash together and **do not lower leverage**. The −2.1 points is real on SoftBank's definition and close to nil on the gross one. Both statements should travel together.

## Interest line: CONFIRMED

- SBG interest expenses **¥676.4B in H1, +¥407.2B YoY** (acct p.7; includes the full write-off of unamortised bridge fees on early repayment; the non-cash share is not stated).
- **Q2 "Payments of interest, etc." −¥0.3T (−$2.0B)** in SBG's stand-alone cash bridge (deck p.79). "Etc." is not itemised.

**Records:** STATUS 09464c7478 · brief 3105aba568. My full leg: `AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_LOSS_INVESTIGATION.md`. The CONFIRMED grade is not touched.
