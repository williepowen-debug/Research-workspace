# Idea #3 — the payer/borrower credit gap ("where the puck is going")

**Written:** 2026-10-23, 16:04–16:08 ET start (from `date`) · **Desk:** VULCAN (research only) · **Asked by:** Will, via spawned analyst session · **No trade, size, order, score or threshold change.** TERRY builds cards; Will approves (root rule #5).
**Tiers:** T1 = primary filing or own fetch · T2 = owner-desk figure or named outlet read directly · T3 = search summary or relay. Live prices = `fetch.py price` at 16:05 ET on 10/23. The close is 16:00, so these are at or near the close, but the official close is **not confirmed**.

## Bottom line

1. **The idea's premise has not held in the most recent test.** It says the payers (MSFT, GOOGL, AMZN, META) and the borrowers (CoreWeave, Oracle, developers) react in opposite directions to capex news. But from 10/13 to 10/22 they all widened together (DTCC, T1):
   - Meta 103 → 118.5bp, Alphabet 73 → 82.5bp, Oracle 264 → 314bp, CoreWeave ~1,000 → ~1,112bp.
   - Meta raised its capex guide on 10/21. The next day CoreWeave stock fell −10.06% to $55.60 while Meta's CDS (credit default swap, the price of default insurance) hit a record.
   - The common driver is the funding gap plus interest rates, so the gap trades as a common factor with different betas. It is not a seesaw.
2. **The gap is real and wide.** CoreWeave minus Meta is ~990bp. Oracle minus Meta is ~195bp. Ratings put Oracle one notch above junk at S&P, while the payers are AA-class.
3. **CoreWeave's "refinancing wall" is mostly amortisation, not bullets.** It owes $10.6B of principal from mid-2026 through 2027, against $5.52B of June cash. But no unsecured bond matures before June 2030. The binding constraint is new money for $35–39B of 2026 capex, at SOFR + 550bp marginal cost and 14.4–15.1% unsecured yields.
4. **Next week can widen or narrow the gap mainly through 2027 capex language, not 2026 dollars.** A cut YoY is unlikely on the evidence: all four signalled 2027 increases. A 2027 step-up below the ~$934.5B Street consensus (T3) is the realistic "cut" case.

## 1. Dependency map — who pays whom

| Borrower | Payer exposure | Figure (date · tier) | What we cannot see |
|---|---|---|---|
| **CoreWeave** | **Microsoft**: top customer, 67% of FY2025 revenue | 10-K FY2025 · T1 (via PROME sweep B) | MSA dated 2/22/2023; contract value not disclosed |
| | Customer A / B / C = **36% / 26% / 10%** of Q2-26 revenue; A + B = 64% of receivables | 10-Q 0001769628-26-000366 · T1 [KB-VULCAN-080] | Names withheld. A = Microsoft is **INFERRED** (A was 71% in Q2-25) |
| | **Meta**: order forms up to $14.2B (to 12/2031) + up to $21.0B (to 12/2032, incl. option) | 10-K, 10-Q · T1 (sweep B) | "Up to" amounts, not minimums |
| | **OpenAI**: $11.9B MSA (to 10/2030) + $6.5B order (to 5/2031); total $22.4B **reported** | 10-K/10-Q T1 for $18.4B; $22.4B T3 | ≈20% of backlog, INFERRED |
| | **Google**: not a named customer; competitor and interconnect partner | filings · T1 | Supplying Google's OpenAI capacity = reported 2025, **UNVERIFIED** |
| | **Amazon**: competitor only | filings · T1 | — |
| | Backlog (RPO) **$103.7B** at 6/30: 41% within 24 months, 39% in months 25–48 | 10-Q · T1 | **Counterparty split of RPO not disclosed**. "~2/3 investment-grade counterparties" is Deutsche Bank via CNBC 10/15 · T3 |
| | Nvidia: sole GPU supplier, ~9–10% holder ($2.0B at $87.20, Jan-2026) | 10-Q T1; holder % T3 | — |
| **Oracle** | RPO **$664B**, **OpenAI ≈ half** (S&P); Oracle does not name it. "~$300B OpenAI deal" (CNBC 10/19) | PROME `themes/ellison/reports/2026-10-22_sweep/00-SYNTHESIS.md` §2 · T1 RPO / T3 split | Oracle's payer is mainly **OpenAI**, not the four hyperscalers |
| | Jupiter NM (~$18B bank loan, OpenAI end user) quoted 89–91c pre-force-majeure (9/23); force-majeure notice 9/24 | sweep A · T2/T3 | Post-notice loan level **UNKNOWN** |
| **Merchant developers** | Applied Digital 9.25% 2030 secured notes (~$2.5B) fund **CoreWeave-leased** buildings | DEWEY via L782 v2 · T1 | Second-order: APLD depends on CRWV, which depends on MSFT/Meta/OpenAI |
| | Nscale ← Microsoft Loughton (50–90MW); withdrawal over power timing reported | KB-VULCAN-233 · T1 release / T3 withdrawal | Other Microsoft neocloud contracts (Nebius, IREN, Lambda) are **not in the desk record — UNVERIFIED** |
| | Anthropic ← Google TPU lease ~$125.2B, part-funded by Broadcom converts (reported) | KB-VULCAN-199 · T3 | — |

**Who is hurt by a capex cut, by payer:**

| Payer cuts | First-hit borrowers | Strength of link |
|---|---|---|
| **MSFT** | CoreWeave (Customer A, if Microsoft), Nscale/neocloud leases, OpenAI's indirect compute | **Strongest named link to CRWV.** The Microsoft–CRWV contract term and value are unknown |
| **META** | CoreWeave ($35.2B "up to" orders); Hyperion/Beignet SPV; Meta's $121.41B of 2027 commitments (10-Q · T1) are the collateral others borrow against | Strong, filed |
| **GOOGL** | Anthropic TPU chain (Broadcom, lessors); possibly CRWV via OpenAI capacity (UNVERIFIED) | Weak or indirect to CRWV |
| **AMZN** | Anthropic (Rainier); own-build contractors. **No CRWV or Oracle link found** | Weakest for this trade's borrowers |
| **OpenAI** (not reporting) | Oracle (≈ half of RPO), CRWV (~20%), SoftBank | **The single biggest common root.** It is not on next week's calendar |

## 2. CoreWeave refinancing wall

**Stack at 6/30/26** (10-Q Note 10 · T1, via PROME sweep B and KB-VULCAN-077/247):

| Layer | Principal | Rate / terms | Maturity |
|---|---|---|---|
| Recourse DDTLs (delayed-draw term loans) 1.0 / 2.0 / 2.1 / 3.0 / 5.0 | $10.81B | Effective rate 9–15%. SPV borrowers, GPU + contract collateral, parent guarantee | 3/2028 – 11/2031, amortising |
| DDTL 4.0 (**non-recourse** to the parent) | $2.84B drawn of $8.5B | SOFR + 225bp / UST + 200bp. DSCR (debt-service coverage) 1.20x to size, 1.15x maintenance | 3/2032 |
| Senior unsecured notes (9.25% 2030, 9% 2/2031, 9.75% 10/2031, 9.625% 2032, €8.5% 2032) | **$10.03B** | 9–10% | 6/2030 – 7/2032 |
| Converts (1.75% 2031, 1.75% 2032) | $6.59B | 2% | 2031–32 |
| OEM/software financing + Magnetar | $5.29B | 9–12% | 2026–2030 |
| **Total principal** | **$35.55B** | Plus $16.5B lease liabilities and **$35.5B** leases not yet commenced | |
| **Due rest-2026 / 2027** | **$4.41B / $6.18B = $10.60B** | **1.92×** June cash of $5.52B. Liquidity incl. undrawn $15.55B (availability $10.01B is conditional) | |

**Since August (T1, 8-Ks):**
- **DDTL 5.5:** $2.6B at SOFR + 550bp, matures 9/2031. DSCR ≥1.35x. Event of default on "adverse events with respect to certain material contracts".
- **$1.2B revolver draw** in August.
- **$4.2B 2.875% convert due 2033** (9/22, upsized). Cross-default on subsidiary debt above the greater of $200M or 5% of LTM EBITDA.
- **35M-share ATM / collared forwards**, window open ~10/17. Any sales are UNKNOWN.
- **No new notes, exchange offer or October issue found** (search 10/23 · T3 negative).
- The like-for-like DDTL ladder is 5.0 → 5.5 = +100bp in three months [KB-VULCAN-075].

**Reading:**
- No bond is due before June 2030, so the 2026–27 principal is **DDTL and OEM amortisation**. That composition is **INFERRED**: the 10-Q maturity table is not split by facility. It is serviced first from contract cash at the SPVs.
- The wall bites through **new-money need**:
  - 2026 capex is guided at $35–39B.
  - Q3 free cash flow consensus is ~−$10.1B (FactSet via CNBC · T3).
  - Baird estimates a ~$30B raise in 2027 (T3).
  - Q3 interest is guided at $860–940M against Q2 operating cash flow of $0.68B (sweep B: guide T3, OCF T1).
- **If it cannot refinance:**
  - Capex stops first.
  - DDTL SPVs keep their GPU and contract collateral (cash traps, DSCR tests).
  - Unsecured noteholders sit behind SPV-level secured debt for those assets. They hold subsidiary guarantees (convert terms · T1), but the SPV collateral is ring-fenced first.
  - **No sourced recovery estimate was reached.** The market prices unsecured debt at 80–86c (yields 14.4–15.1%, HYG fund evaluations as of 10/21 · T2 LIQUID). The CDS curve is ~0.3pt upfront at Jun-2027 versus ~18pt at 5 years (sweep B · T1 tape): refinancing risk out the curve, not an imminent miss.
- **Q3 report date:** **not announced** as of 10/23 search (T3 negative). The desk models ~11/09. AJ Bell lists 11/10 (T3), and last year's Q3 printed 11/10/2025 after a 10/27 announcement.

## 3. Next week — what widens vs narrows the gap

**Dates (confirmed):**
- **MSFT:** Wed 10/28, after close, call 2:30 PT (Microsoft IR release 10/7 · T2).
- **GOOGL:** Wed 10/28, call 4:30 ET ([abc.xyz notice 10/6](https://abc.xyz/investor/news/news-details/2026/Alphabet-Announces-Date-of-Third-Quarter-2026-Financial-Results-Conference-Call-2026-8tpGZsLS6v/default.aspx) · T2).
- **AMZN:** Thu 10/29, call 5:00 ET ([Amazon IR](https://ir.aboutamazon.com/events/event-details/2026/Q3-2026-Amazoncom-Inc-Earnings-Conference-Call/default.aspx) · T2).
- META already reported 10/21: capex RAISED, 2026 guide $135–145B (8-K · T1; STATUS).

**Standing guides and expectations:**

| Name | Standing 2026 guide | 2027 Street (FactSet/Goldman table, undated · T3) | Basis caveat |
|---|---|---|---|
| MSFT | ~$175B CY basis after a lease restatement, vs ~$190B earlier (trackers · T3, **conflict**). FY27 "will grow" (call 7/29 via DEWEY) | ~$207.6B | Counts finance leases at signing. DEWEY cash gap ≈ −$5.8B, headline −$26.8B |
| GOOGL | $195–205B, raised in July (T3; one Barchart read says ~$205B) | ~$284.8B | Purchases of P&E; GOOGL fell ~6% on the July raise (T3) |
| AMZN | ~$220B, raised from ~$200B on 7/30 [KB-VULCAN-041 · T2] | ~$256.5B | Net of incentives |
| 4-name total | ~$720–745B (trackers · T3) | **~$934.5B**. Evercore/BofA >$1T | Mixed basis |

**Scenario table:**
- Gap = borrower spread minus payer spread.
- "Raise" = 2026 raised and/or 2027 step-up at or above consensus.
- "Flat" = guide reiterated, 2027 language vague.
- "Cut" = 2027 below consensus, or any YoY cut. A YoY cut fires S1's red capex-cut branch; it needs no concentration condition.

| Outcome | Payers (MSFT/GOOGL/AMZN credit) | CoreWeave | Oracle | Developers (APLD etc.) | Gap | Counter-evidence |
|---|---|---|---|---|---|---|
| **Raise** | More IG supply → CDS wider, new issues at concessions (DEWEY: "absorbing at a rising price") | Revenue story intact. But **10/22 precedent: Meta raise → CRWV −10%**, CDS flat | Oracle's driver is OpenAI, not these three; little direct effect | Mildly positive | **Narrows in theory; in the last instance did NOT** (both legs moved the same way) | §4b grades a stock falling on a raise in ≥2 prints as *confirming fragility* |
| **Flat** | Neutral; supply continues | Neutral; funding-cost drift dominates (DDTL +100bp/qtr) | Neutral | Neutral | Drifts with HY and rates | — |
| **Cut** | Free cash flow better → CDS tighter, less issuance | **Backlog/renewal risk** for the Microsoft-dependent book; new-money access harder | Second-order unless OpenAI's funding is hit | Hardest hit: leases tied to CRWV/neoclouds | **Widens sharply** | Already near ~990bp (CRWV–META). Partly priced |

**What decides the direction:** 2027 capex language versus ~$934.5B; any line on inference price or ROI (the §4b confirm leg); MSFT commentary on third-party/neocloud capacity; AMZN's free cash flow. No company has given a 2027 dollar figure (DEWEY · T1/T3).

## 4. Observable instruments (levels, not recommendations)

| Pair / gauge | Leg A | Leg B | Difference | Date · tier |
|---|---|---|---|---|
| CDS: CRWV – META | ~1,112bp (upfront-derived, ±tens of bp) | 118.5bp | **~994bp** | 10/22 DTCC · T1 (VULCAN cds-breadth) |
| CDS: ORCL – META | 314bp | 118.5bp | **195.5bp** | 10/22 DTCC · T1 |
| CDS: ORCL – GOOGL | 314bp | 82.5bp | **231.5bp** | 10/22 DTCC · T1 |
| CDS: ORCL – AMZN | 314bp | 80.5bp (10/20) | **~233bp** (mixed dates) | DTCC · T1 |
| CDS: MSFT | 4 prints on 100bp coupon, upfront 1.73–2.22pts | — | **Sign-ambiguous:** ~55–65bp if protection buyer received the upfront, ~139–150bp if paid. Prior relay label 55bp (10/19 · T3) favours the low reading. **UNGRADED** | Own probe 10/21–10/22, run 16:05 ET · T1 |
| Fallen-angel cliff: BB OAS – BBB OAS | 210bp | 111bp | **99bp** | 10/22 FRED first-published · T1 |
| HY OAS / IG OAS | 340bp | 89bp | — | 10/22 FRED · T1 |
| CRWV unsecured | 9.625% 2032 80.04c / 14.91% YTW; 9.25% 2030 85.76c / 14.44% | — | — | HYG evaluation as of 10/21 · T2 LIQUID |
| Payer bonds | Meta Beignet 6.581% 2049 ~91c | — | Current hyperscaler bond yields **not reached** (no TRACE) | 10/07 · T3 |
| Equity ratio CRWV/MSFT | $54.24 (−2.46%) | $524.51 (+0.66%) | **0.1034** | 10/23 16:05 · T1 |
| CRWV/META | $54.24 | $642.62 (−0.96%) | **0.0844** | same |
| ORCL/MSFT | $126.08 (+0.43%) | $524.51 | **0.2404** | same |
| ORCL/META · APLD/META | $126.08 · $18.25 (−4.40%) | $642.62 | **0.1962 · 0.0284** | same |
| GOOGL · AMZN · NVDA | $320.21 (−1.24%) · $248.00 (−0.95%) · $210.96 (−0.59%) | — | — | same |
| HYG · LQD | $77.04 (−0.08%) · $103.83 (−0.43%) | — | — | same |

Caveats:
- 10/23 DTCC posts ~20:15 ET and is not in this report.
- CDS levels are thin (often one trade per day).
- Vendor levels (Markit/ICE) differ from DTCC prints.
- LIQUID's levels win on any conflict.
- No dated base series for the equity ratios was built here.

## 5. Oracle fallen-angel mechanics

| Item | Figure | Source · tier |
|---|---|---|
| Ratings | S&P BBB− stable (7/09); Moody's Baa2 negative; Fitch BBB | Sweep A (press; agency releases not read) · T3. LIQUID map |
| Index rule | Bloomberg uses the **middle** of three ratings; ICE uses the **average** ⇒ ejection needs **2 of 3 agencies at HY** | LIQUID `workbook/ORCL_FALLEN_ANGEL_MAP.md` §2 · T2 |
| Ladder state | R0 fired 7/9. **R1 (2nd agency to the IG floor, likeliest Moody's Baa3) NOT FIRED**; no October action | LIQUID STATUS 10/22 · T2 |
| Forced-sell universe | **~$130–160B** index-eligible, order of magnitude. Oracle borrowings **$125.3B** (10-Q 8/31 · T1) | LIQUID map §3 (bond-by-bond tally not done) |
| Records | Ford ~$36B (3/2020), Kraft Heinz ~$22B (2/2019) ⇒ Oracle ≈ 4× the record | LIQUID map §3 · T2 (not re-verified) |
| Pool context | ~$100B of USD+EUR IG-index bonds traded wider than the BB curve | Bloomberg 8/4 via The Edge 8/5 · T2 (no Oracle figure in it) |
| Forced effect | Median fallen-angel OAS over BBB: **56bp a year before → 278bp in the downgrade month** (1,188 bonds); prices often fall **before** the cut; relative performance turns positive up to 24 months after | Academic summaries via search · T3 |
| 2002 scale | **$158.5B** of IG bonds downgraded to HY in 2002 | Altman & Bana, NYU Feb-2003 · T1 (read) |

A single S&P cut to BB+ moves Oracle to R2 but **does not eject it** from the indices. Ejection needs a second agency at HY.

## 6. Historical analog — 2000–02 telecom

| Fact | Figure | Source · tier |
|---|---|---|
| Equipment vendors vs carriers | S&P comm-equipment index **−86%** 3/2000–9/2001 (−$793B equity); long-distance −65%; comm services −43%; **"Baby Bells were the least scathed"**; CLEC index collapsed | Dallas Fed, *Southwest Economy* Jan/Feb 2002, "Is Telecom Disconnected or Just on Hold?" · T1 (PDF read) |
| Overbuild | Long-haul backbone utilisation **<3%** (4/2001) vs 15% (1988) | same |
| Defaults | Telecom = **55%** of 2001 and **52%** of 2002 defaulted dollars (31% ex-WorldCom) | Altman & Bana, NYU FIN-03-010 · T1 |
| Recovery | Telecom **16.6%** vs all-issuer **25.3%** (2002); historic median 39.4% | same |
| Fallen angels | 2002 fallen-angel dollar default rate **20.3%** (8.5% ex-WorldCom) | same |
| Vendor financing | Lucent $5.7B direct customer commitments + $1.8B loan guarantees; Winstar Ch.11 4/2001, sued Lucent for $10B | Search summaries · T3 |
| Levered incumbent | **Qwest** cut to junk: S&P BB+ (late 5/2002), Moody's 5/30/2002 on **$26.4B** debt; Ba3/B−/B at YE2002 | CNN 5/30/2002 · T3; Qwest FY2002 10-K · T1 (listed, not opened) |

**What the gap did:** the incumbent–CLEC gap blew out, and the incumbents held. The exception was **Qwest**, the incumbent that had levered up for the buildout. That is the Oracle analogue: an investment-grade operator straddling both tiers. **RBOC vs CLEC bond-spread series were not reached**, so the evidence here is equity, ratings and defaults.

**Where it breaks:**
1. CLECs depended on RBOCs for network access, not revenue. Here the borrowers' revenue **is** payer capex, so a cut hurts borrowers directly.
2. CRWV has $103.7B of contracted take-or-pay backlog; CLECs had retail churn.
3. The collateral differs. Fibre outlived the bust; GPUs depreciate in years (advance rate is 90% of **cost** at funding, KB-VULCAN-051).
4. The payers today are AA and cash-rich. Their funding gap (~−$186B, mixed basis) is filled at IG with only ~$34B due through 2027 (DEWEY · T1/MEDIUM).
5. The common root (OpenAI) is private and unrated, with no telecom equivalent.

## 7. Falsifiers and dated catalysts

| Date | Event | Supports the gap thesis if… | Falsifies it if… |
|---|---|---|---|
| 10/23 ~20:15 ET | DTCC 10/23 file | — | — |
| **10/28 AMC** | MSFT, GOOGL (and SK hynix) | Payer CDS tightens on capex restraint while CRWV/ORCL widen | Both legs widen together again (common factor, not opposite sensitivity) |
| **10/29 AMC** | AMZN (and Samsung) | Same | Same |
| Rolling | Moody's ORCL action | Baa3 = R1 (pipeline deepens) | Affirmation with stable outlook |
| ~11/10 (unconfirmed) | CRWV Q3 10-Q | Customer concentration, DDTL draws, ATM use, cash bridge | New unsecured issue clears near the 14–15% curve |
| early–mid Nov | BDC Q3 schedules of investments (BROCK) | DC-loan marks cut | Marks at par |
| ~11/19 | NVDA 10-Q, guarantee book (VULCAN-17) | — | — |
| ~12/15 | ORCL Q2 FY27 10-Q | Leases not yet commenced > $288B | — |

## 8. What we can't reach

- Counterparty split of CRWV's $103.7B RPO, and the Microsoft contract value and term (not filed).
- Recovery estimates for CRWV unsecured debt; TRACE prints; hyperscaler secondary bond spreads.
- Clean MSFT CDS: the probe sign is ambiguous.
- 10/23 DTCC file.
- Sell-side quarter-specific capex consensus for 10/28–29: Quartr/FactSet unentitled. The 2027 table is undated (T3).
- Agency releases on Oracle (press only).
- A sourced Oracle forced-selling volume beyond LIQUID's order-of-magnitude estimate.
- RBOC vs CLEC spread history.
- Whether CRWV's ATM has sold any shares.
- CRWV Q3 date (not announced).

**Sources read this session:**
- VULCAN `reports/2026-10-23_L782_v3_weak-links_FINAL.md`, `reports/2026-10-22_L782_v2_weak-links.md`, `reports/2026-10-23_cds-breadth/REPORT.md`, `CRWV/README.md`, `CRWV/KB.tsv`, `STATUS.md`, `workbook/EXIT_PROTOCOL.md` §4b, `docket/CATALYSTS.tsv`.
- LIQUID `STATUS.md`, `workbook/ORCL_FALLEN_ANGEL_MAP.md`.
- PROME `themes/ellison/reports/2026-10-22_sweep/00-SYNTHESIS.md`, `A-oracle-credit.md`, `B-coreweave.md`.
- DEWEY `output/2026-10-22_hyperscaler-ai-funding-gap-ig-capacity.md`.
- Dallas Fed PDF (swe0201c); Altman & Bana NYU wpa03010 (PDFs extracted locally).
- Web searches 10/23 ~16:06 ET (IR dates, capex trackers, CRWV issuance, Qwest, fallen angels).
- Live data: `fetch.py price` 16:05 ET; `fetch.py fred` first-published 16:05 ET; `dtcc_cds_probe.py MICROSOFT 2026-10-21 2026-10-22` 16:05 ET.
