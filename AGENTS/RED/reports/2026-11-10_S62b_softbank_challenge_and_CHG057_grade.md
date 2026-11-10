# SoftBank investigation: RED's challenge, and CHG-RED-057 graded (S62-b)

**Written:** 2026-11-10, started 17:39 ET (from `date`). **Asked by:** PROME prome-07 at 17:40 ET, on Will's word at 17:18 ET ("alright lets have you direct and orchestrate the investigation into softbank. Feel free to spawn or direct whatever agents we need to help us do so"). RED is the challenger. $0. No weight, band, threshold, gate letter or card moved.

**The working read under attack (PROME's wording):** "The Q2 loss (about 1.12 trillion yen) is mostly paper and already inside the reported 15.9% leverage; rolled to today's Arm close it is 22.7 to 22.9% against a 25% ceiling; the $3.7B equipment charge is a re-plan, not a default and not a cancelled campus; the stress is SoftBank-specific, not the AI cohort; no financing has been refused."

**What RED read itself (✔):**
- SoftBank IR PDFs from SAM's download, checked by SHA-256 prefix: the earnings deck `1e69c9ec` (pages 16–18, 23, 71, 79, 82) and the accounting deck `2945557a` (pages 7–8). Text extracted with pdfminer.
- Cited from the owners and not re-read:
  - SAM: `AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-10_LOSS_INVESTIGATION.md`, `2026-11-10_RESULTS_GRADE.md` and `SOFTBANK_FUNDING_STACK.md`, plus the two SAM packets in `PROME/inbox/processed/`.
  - VULCAN: `AGENTS/VULCAN/reports/2026-11-10_softbank/REPORT.md`, its `readers/sb_docs.md`, the VULCAN packet, and VULCAN-191 (MISS) in VULCAN's resolved archive.
  - LIQUID: `PROME/inbox/processed/2026-11-10_from-LIQUID_softbank-credit-leg.md`.
  - BROCK: `BOARD/SIG-W-20261110-004`.
- Arm $181.49 (−2.58%, 11/10 close), from `fetch.py` at 17:42 ET. USD/JPY 158.69 is SAM's 17:23 ET figure.

**Arithmetic:** RED's own, on SoftBank's reported inputs. Script: `/tmp/.../scratchpad/sb_math.py`, reproduced in § A. Same roll as SAM's `ltv_lookup.py`: only Arm and the October $10B tranche move.

---

## Answer first

The working read is **right on SoftBank's own arithmetic and wrong in what it implies.**
- Its numbers check: 15.9% at 9/30, 22.66% rolled to Arm $181.49, and 22.9% with the ¥140.2B settlement (RED's figures match SAM's).
- The weakness is the ruler. SoftBank's ratio **goes down when SoftBank borrows against its shares.**
  - In Q2, SoftBank booked ¥2.1T ($12.4B) as "asset monetization" (deck p.79). It was secured borrowing: the Intel collar ($7.4B) and an extra $5.0B on the Arm margin loan. SoftBank used the cash to repay an unsecured bridge.
  - On SoftBank's definition this lowered leverage: the loans are deducted from net debt and netted out of the share values (deck p.82, items f and i).
  - For a bondholder it moved $12.4B of claims ahead of them on SoftBank's two best liquid assets.
  - The bondholder's own market agrees. 5-year CDS went from 347 (August median) to 497 on 11/9, which is about a one-in-three five-year default price at 40% recovery.
- The 2.3-point headroom also leaves out a pending item SoftBank discloses itself: the $5.4B ABB robotics purchase. With it, leverage is **24.05%**, and the 25% line sits at Arm **$166**, 8.3% below the 11/10 close.
- About 70% of the value that leverage is measured against is two correlated AI prices: Arm (net of its loan) and OpenAI (an unlisted mark that SoftBank sets itself).

**Strongest counter-case, in plain words:** SoftBank isn't sinking from a paper loss. It is carrying a cash interest bill that more than doubled, with assets it keeps pledging. The leverage measure it promises to keep under 25% flatters it every time it pledges more. Disclosed commitments alone take it to about 24%. A 10% fall in both Arm and the OpenAI mark breaches its own ceiling. The credit market already prices it like a single-B name, not the BB+ it is rated.

| Line | Verdict |
|---|---|
| R1 "Mostly paper" vs the cash cost of carry (RED's line) | **WEAKENED** |
| R2 = PROME 1: does SoftBank's LTV hide what a creditor counts? | **WEAKENED** (close to broken on the implication, not on the numbers) |
| R3 Headroom leaves out disclosed items (RED's line) | **WEAKENED** |
| PROME 2: what CDS 497 knows | **WEAKENED** |
| PROME 3: deposits, open commitments, AEP collateral as cash demands | **HOLDS on liquidity; WEAKENED on the cushion's definition** |
| PROME 4: "completely unrelated to PORTS-Pike" | **WEAKENED** |
| PROME 5: "SoftBank-specific" | **WEAKENED** |
| "No financing has been refused" | **HOLDS on the letter**; lenders refused the shares-only terms in July (relay) |
| "A re-plan, not a default, not a cancelled campus" | **HOLDS** |

Nothing is BROKEN. Every number in the working read checks. Each line it uses to suggest comfort is weaker than stated.

---

## The lines

### R1 (RED's line). "Mostly paper" hides the recurring cash cost

| Evidence | Source |
|---|---|
| SBG interest expense **¥676.4B in H1, +¥407.2B year on year**, "mainly due to higher interest expenses from increased borrowing and corporate bond balances, and full recognition of unamortized financing costs upon early repayment of the bridge loans" (the bridge-fee part is non-cash; amount not stated) | accounting deck p.7 ✔ |
| Stand-alone Q2 cash bridge: "Payments of interest, etc." **−¥0.3T ($2.0B) in one quarter** | earnings deck p.79 ✔ |
| The cash policy covers **bond redemptions only**: ¥5.0T ($32B) against ¥1.6T over two years. The ¥5.0T includes ¥511.4B of undrawn lines | deck p.23, p.65 ✔ (p.65 via SAM) |

- **Reading:** at Q2's pace, interest is about ¥1.2T a year (RED arithmetic, ×4; "etc." may include other items).
  - Over two years: about ¥2.4T of interest + ¥1.6T of redemptions = about ¥4.0T, against ¥5.0T of cash.
  - Add the known calls below and the cushion is fully used without new monetization or refinancing.
- **What survives:** the loss itself is mostly non-cash (SAM's bridge reconciles to the yen). SoftBank has always rolled its debt and has just done a record $56.5B quarter.
- **Verdict:** WEAKENED. "Mostly paper" is true of the loss and silent on the carry.

### R2 = PROME line 1. SoftBank's ratio hides what a creditor counts

| Evidence | Source |
|---|---|
| Holdings are valued **net of** the Arm and SoftBank Corp margin loans and the T-Mobile and Intel collars. The same liabilities are **deducted** from net debt (items f, g, h, i). Item (j) **includes** the SBG-guaranteed SVF2 OpenAI-shares loan | deck p.82 ✔ |
| Q2 "Asset monetization" **¥2.1T ($12.4B)** = Intel prepaid forward ¥1.2T ($7.4B) + increase in the Arm margin loan ¥0.8T ($5.0B). Bridge fully repaid −¥4.2T | deck p.79 ✔ |
| SAM: Q2 monetization moved LTV about **−2.1 points** on SoftBank's bridge | SAM RESULTS_GRADE line 30 |
| Adjustments at 9/30: asset-backed **¥6.49T**; hybrid 50% equity credit ¥0.76T | SAM RESULTS_GRADE line 36 (data sheet p.17) |

- **RED arithmetic, gross creditor view** (asset-backed debt added back to both sides): 22.9% at 9/30, rising to **30.6% rolled to Arm $181.49**. With hybrids at full debt, **31.8%**. That compares with the 35% "extraordinary" ceiling.
  - This is not S&P's adjusted measure, which RED has not read. It shows how much of the gap between 22.7% and the bondholder's exposure is definition.
- **The point:** when SoftBank pledges a share to raise cash, its ratio falls, but the unsecured bondholder now stands behind a larger secured claim. Q2 did exactly that, at size, to repay the bridge that funded OpenAI (financial report p.38 and p.6, via VULCAN § e).
- **The steelman for SoftBank's measure:**
  - The margin loans are non-recourse to SBG (financial report p.14/12, via SAM). Netting is the correct recourse view for a bondholder whose claim on those shares is the residual anyway.
  - The SVF2 loan is counted in net debt (item j) although SVF2 is the borrower. Unless the "etc." in SVF2's NAV adds it back, that is conservative.
  - RED cannot settle the item (j) point from the deck.
- **Margin terms on the unlisted mark:**
  - The SVF2 loan's cash collateral and mandatory prepayment trigger on "a significant fall in the fair value" of the referenced OpenAI preferred shares. The threshold is undisclosed (SAM stack, FILING).
  - OpenAI's mark was "unchanged" in Q2 (SAM). A down round is therefore a cash call on an SBG-guaranteed loan.
- **Energy Global's warrant liability to OpenAI (¥541.8B):** a derivative, not interest-bearing debt. It dilutes SoftBank's claim on Energy Global; it is not a cash call (SAM fr 71/69). No weight.
- **Verdict:** WEAKENED. The number is right on SoftBank's basis. Its comfort comes partly from pledging, and a creditor counts closer to 31% than 23%.

### R3 (RED's line). The headroom leaves out items SoftBank itself discloses

| Case (Arm $181.49, ¥158.69) | Leverage | Arm at 25% |
|---|---:|---:|
| A. SoftBank basis rolled (RED reproduces SAM) | 22.66% | $145 |
| B. + ¥140.2B settlement (if SBG pays) | 22.90% | $149 |
| **C. + ABB robotics $5.4B at cost, debt-funded** ("Q3 onwards", SAM grade line 54) | **24.05%** | **$166 (−8.3%)** |
| C + a further $10B debt-funded investment | 26.08% | — |

- ABB may be partly LBO-financed outside the ratio (about $1.8B, SAM). In that case C is a little lower.
- Also left out (direction only):
  - The SVF1 and SVF2 listed holdings since 9/30. SoftBank's pro forma re-marks only Arm, SoftBank Corp and Intel (SAM line 39), and the AI and tech tape fell from 10/29.
  - Any further SB7 equipment commitments (not quantified).
- **Verdict:** WEAKENED. "22.7 to 22.9%" is the figure before a disclosed pending deal. The figure after it is about 24%, with the line about 8% below Arm's close. Arm fell 2.58% on 11/10 alone.

### PROME line 2. What a 5-year CDS of 497 knows that 22.7% does not

| Evidence | Source |
|---|---|
| 5Y CDS **497 median on 11/9** (496–513, 7 prints), widest since at least 8/3. Monthly medians: August 347, September 360, October 394 | LIQUID, DTCC public files (US-nexus trades only, about ±10bp) |
| Oracle 305 → 301.5 and CoreWeave about 1,240 → 1,136 over 11/6–11/9 | LIQUID |
| Ratings: JCR A Negative, S&P BB+ Stable since 7/16, Fitch BB+ Stable | deck p.71 ✔ |

- **RED arithmetic, risk-neutral, 40% recovery:** 497bp implies a hazard of about 8.3% a year, or **about 34% cumulative default over 5 years**. August's 347bp implied about 25%. This contains a risk premium and thin-sample error; it is not a probability forecast.
  - It is single-B pricing on a BB+ rating.
- **What CDS knows:** CDS references senior unsecured debt, exactly the claim that Q2's ¥2.1T of secured borrowing moved behind (R2). It also prices the correlation between Arm and OpenAI, and the carry (R1).
  - The spread rose about 150bp while SoftBank's own ratio rose from 13% (6/30) through 15.9% (9/30) to about 22.7% (rolled). Direction agrees; the size of the move says the market weights the tail more than the ratio's headroom implies.
- **The bull answer:** a thin, US-nexus sample before the results; yen retail demand just set a record (the ¥1T 70th bond at 4.75%, sold out).
- **Verdict:** WEAKENED.
- **Contradiction to fix, not a finding against SoftBank:** LIQUID's packet says "S&P BB+/Negative since 3/3" (relay). SoftBank's own deck p.71, read by RED: "S&P BB+ Outlook: Negative → Stable (Jul 16)". LIQUID's line looks overtaken. LIQUID's relayed "path back to adjusted LTV <35%" may be the March Negative-outlook text. Sent to LIQUID by packet.

### PROME line 3. Deposits, open commitments and AEP's collateral as cash demands

| Item | Cash on SBG? | Source |
|---|---|---|
| $6.6B of advances still on the balance sheet | **No:** already paid. It is an asset that could be written down again, and the deck flags no impairment trigger | deck p.18 ✔; SAM |
| SB7 commitments beyond the $6.6B | **Unknown.** No purchase-obligation table found | SAM, VULCAN |
| ¥140.2B settlement | Yes, "from Q3 onward"; payer not stated | accounting deck p.8 ✔ |
| ABB $5.4B | Yes, about $1.8B possibly LBO | SAM |
| SB Energy: SBG committed $3.0B, $1.5B funded | Likely the remaining $1.5B; the SB Energy IPO is postponed | SAM grade line 55; VULCAN |
| AEP "fully collateralize" OHTCo equipment purchases (three 765 kV lines, about $5B) | At **the customer** (the campus side; non-recourse to SBG, no SBG guarantee found). It reaches SBG only if SBG funds SB Energy while its IPO is postponed | AEP 10-Q 10/28 via VULCAN; SAM |
| Interest at the Q2 rate | About ¥1.2T a year | deck p.79 ✔ (R1) |

- **Verdict:** HOLDS on near-term liquidity: ¥5.0T covers the known calls. WEAKENED on the cushion's definition: counting interest, the two-year buffer is used up (R1). The binding unknown is SB7's forward commitments.

### PROME line 4. "Completely unrelated to PORTS-Pike" is SoftBank's word in one of two decks

| Evidence | Source |
|---|---|
| Accounting deck p.8 (server Last-Modified 16:08Z): $9.5B split as "PORTS-Pike power generation PJ and others $6.6B" and "Other than the above $2.9B — No longer in the revised plan"; red box "The loss of $3.7B is completely unrelated to PORTS-Pike" | ✔ `2945557a` |
| Earnings deck p.16 and p.18 title the **whole** $9.5B "Advance payments related to PORTS-Pike power generation project and others"; p.18: total 9.5, loss −2.9, balance 6.6 | ✔ `1e69c9ec` |
| Investor Briefing deck (Last-Modified 09:21Z) p.12: realignment covers projects "including PORTS-Pike power generation project in Ohio"; "unrelated" occurs 0 times | VULCAN reader sb_docs.md line 31, 88 (not read by RED) |
| Financial report: the program covered US projects "including the PORTS-Pike Technology Campus" | SAM fr 7/5 |
| The only reported SoftBank turbine reservations were for the Ohio 9.2 GW gas plant | VULCAN (SECONDARY) |

- **Reading:** the narrow claim can be true. The dropped equipment may have been for "others", such as the tenantless Borden/Scurry 1.7 GW site in the S-1 (INFERENCE, VULCAN's candidate list).
  - Against it: SoftBank's own earnings deck files the written-off $2.9B under the "PORTS-Pike … and others" heading. The briefing version said the realignment included Ohio, and the word "completely" appears only in the version posted about 7 hours later.
- **What survives:** no outside record shows a campus scope cut (AEP lines in effect, OPSB hearing 12/10, plant II sessions).
- **Verdict:** WEAKENED. "Not a cancelled campus" HOLDS. "Completely unrelated" is an issuer allocation that its own decks label inconsistently, and it is not checkable from outside.

### PROME line 5. "SoftBank-specific, not the AI cohort"

| Evidence | Source |
|---|---|
| CDS 11/6→11/9: SoftBank +27, Oracle flat, CoreWeave tighter | LIQUID |
| US 11/10, the first full session after results: **NVDA −5.47%**, **IREN −7.85%**, **NBIS −5.27%**, SFTBY −4.00%, ARM −2.58%, ORCL −1.51%, CRWV −0.51%, SPY −0.88% | VULCAN and LIQUID, vendor closes; no cause attributed |
| PORTS-Pike rent guaranteed by **NVIDIA up to $105.0B** on the first 4.25 GW | NVIDIA 8-K 8/17 and 10-Q via VULCAN (KB-126) |
| About 70% of SoftBank's rolled holdings value is Arm net of its loan (≈¥22.7T, 39.9%) plus OpenAI (≈$110B fair value ≈ ¥17.5T, 30.7%) | RED arithmetic on SAM inputs |

- **Reading:** "specific" fits the credit window to 11/9. On 11/10's equity tape the cohort fell as much as SoftBank's ADR or more (cause unknown, two of the moves larger).
  - SoftBank's stress is AI-asset stress by construction: it is the most leveraged holder of AI equity, so it shows strain first. A campus problem lands on NVIDIA's guarantee before it lands on SoftBank.
- **Against the attack:** CoreWeave raised its capex floor and its CDS tightened. Oracle's CDS is flat. Funding for the cohort is not stressed on what is read.
- **Verdict:** WEAKENED. Specific in who shows the strain, not in its cause.

### "No financing has been refused"

- Reuters, July (relay, via SAM's 11/06 stack): banks refused a shares-only OpenAI loan, and the filing confirms SoftBank Group as guarantor. That is terms refused, then funded with a parent guarantee: pickier, not refused.
- **Verdict:** HOLDS on the letter.

### PROME line 6. What, in the next two weeks, would show the working read wrong

| Date (ET) | Observation | Reads as wrong if |
|---|---|---|
| Tonight about 20:15 | DTCC 11/10 CDS file (LIQUID) | Above **513** (the 11/9 high) while Oracle and CoreWeave are flat = specific stress building. Wider together = cohort |
| 11/10 19:00 to 11/11 01:30 | First Tokyo session on the results (SAM) | 9984.T closes below **¥3,400** (11/9 low) on volume above 64.8M |
| Any day | Arm close (RED, FORGE) | Below **$166** puts case C at 25%; below **$145** puts SoftBank's own basis at 25% |
| 11/11 → | TDnet: a block sale or new margin loan on Arm, SoftBank Corp or T-Mobile, or a new share-backed collar | Defending 25% by pledging or selling = Attack 6 confirms (R2's mechanism in use) |
| Any day | An OpenAI round or tender priced under the mark SoftBank carries | Triggers the SVF2 loan's cash collateral or prepayment, which SBG guarantees |
| 11/11 Tokyo hours | JCR or S&P comment (LIQUID) | JCR downgrade from A, or S&P outlook back to Negative |
| ~11/11 | Siemens Energy FY results (VULCAN) | A settlement line or cancellation tied to a US data-center developer |
| ~11/19 | NVIDIA Q3 FY27 10-Q: SB Energy guarantee line and phase schedule (VULCAN) | Guarantee reduced or phases re-dated = the campus moved |
| 11/19 | ING data-center loan auction, about $500M (LIQUID and BROCK) | Pulled, or clears well under par |
| When posted | SoftBank call transcript (SAM) | Gotō's Ohio words match Agora's "procure power externally" rather than "not scaling back" |
| Any day | EDGAR: SB Energy S-1 withdrawn (RW) | IPO abandoned while AEP's collateral requirement is in effect |

---

## CHG-RED-057 graded under its own letter (tree `research/2026-11-10_AI_FUNDING_TEST_TREE.md`)

| Tree branch | What happened | Result |
|---|---|---|
| SVF2 loan inside the ratio → "Attack 6 reopens: capacity is binding, re-grade on 11/11" | Inside (item j, deck p.82 ✔). Re-graded now: on SoftBank's own basis with its disclosed ABB and settlement, **24.05%**. One more $10B debt-funded check makes **26.1%**, over its own ceiling. NYT's anonymous "hundreds of millions" fits a capacity limit. Not proven as the cause | **Attack 6: FAILED (11/06) → SUCCEEDS ON CAPACITY**, not on cause |
| New secured or parent-guaranteed borrowing → Attack 4 +1; unsecured → −1 | **+1:** Intel prepaid-forward collar, $7.4B secured on all 87.0M Intel shares, first read at this print. **−1:** $11.9B senior term loan listed under debt financing, not asset-backed (deck p.79 ✔; SAM line 52). The +$5.0B on the Arm margin loan was already known on 11/06 (SAM stack) and is not counted again | **Attack 4: net 0** |
| CoreWeave: a cut naming funding → STRONG; held or cut for site timing → MODERATE | FY2026 capex **$37–39B, low end raised** from $35–39B, "deploy infrastructure and deliver it to customers sooner than planned" (8-K Ex 99.1, via VULCAN-191 MISS). DDTL 5.5 $2.6B closed; ATM for up to 35M shares (VULCAN STATUS) | **Not the STRONG branch** |
| Microsoft named as reducing → RED-31 | Not named at this print (per VULCAN; RED did not re-read the release). BROCK 11/10: a Microsoft cut is not a default on IREN's GPU loan (card 004) | RED-31 stays OPEN |

**Grade: MODERATE, unchanged.**
- The not-failing leg HOLDS:
  - CoreWeave raised its capex floor and closed a $2.6B DDTL.
  - SoftBank did a record $56.5B quarter and repaid the bridge early.
  - The ¥1T retail bond sold out.
  - No refusal or named deferral of a campus has been read.
- "Pickier" gains its first filed instance at a primary: SB7 wrote off $2.9B of equipment orders it no longer plans to buy and won rebates (developer-side selection).
- "Rather than" stays the weak part.
  - The same SB7 event is how a squeeze starts.
  - SoftBank, the largest single funder of OpenAI, now has capacity that binds for any new large debt-funded check.
  - It is funding by pledging shares, which flatters its own ratio.
  - The model still has no falsifier.
- New edge: CoreWeave's ATM (equity at up to 35M shares) is pricier funding, not refused funding.
- **Re-review 2026-11-19:** NVIDIA's 10-Q guarantee line, the ING auction bids, and the SoftBank Tokyo, CDS and rating reads by then.

**Counter-signal weight (RED, discretionary, not registered):** P(working read holds through 11/24, i.e. no SBG asset sale or new share pledge to defend 25%, no rating downgrade, no OpenAI down-mark) ≈ 70%. This feeds the post-11/12 re-derivation as War-independent AI-funding evidence, counted once. **No weight moves here.**

## Narrative assessment

Where the market may be right and the fleet wrong: the tape and the CDS treat SoftBank as a leveraged option on AI valuations, and the fleet's working read treats it as a balance sheet with headroom. Both are true. The headroom exists only on SoftBank's ruler, it shrinks with each pledge that funds it, and it measures against two correlated prices that SoftBank partly marks itself. What the fleet may be filtering out: "mostly paper" is the right answer to the wrong question. The question for a creditor was never the size of the quarter's loss. It is how many quarters of carry the unpledged assets can still cover.

## § A. RED arithmetic, reproduced

```
A  SoftBank basis rolled           22.66%  L=12.887 V=56.883  Arm25 $145
B  + settlement                    22.90%  Arm25 $149
C  + settlement + ABB at cost      24.05%  Arm25 $166  drop 8.3%
D  gross: asset-backed added back  30.58%   +hybrid 50% back 31.78%
   9/30 gross                       22.92%  +hybrid 23.90%
   OpenAI 17.46T = 30.7% of V; Arm net 22.68T = 39.9%
E  OpenAI mark -15% (on C)        25.19%
E  OpenAI mark -20% (on C)        25.59%
E  OpenAI mark -30% (on C)        26.44%
F  Arm -10% & OpenAI -10% on A 24.56%  on C 26.03%
F  Arm -10% & OpenAI -15% on A 24.97%  on C 26.46%
F  Arm -5% & OpenAI -10% on A 23.95%  on C 25.40%
G  CDS 347bp R40 -> hazard 5.8%/yr, 5y cum PD 25% (risk-neutral)
G  CDS 497bp R40 -> hazard 8.3%/yr, 5y cum PD 34% (risk-neutral)
H  new $10B debt-funded check on C: 26.08%
```

Inputs:
- ND 11.30 and V 71.14 are reported for 9/30 (data sheet p.17 via SAM).
- 923M Arm shares, $289.66 at 9/30. The October $10B tranche goes into both debt and value.
- Asset-backed ¥6.49T and hybrid ¥0.76T at 9/30 (SAM line 36).
- OpenAI at $110B fair value is SAM's 10/1 figure, and RED treats it as SBG's share (approximate).
- The interest annualization (×4 of Q2) is RED's.
