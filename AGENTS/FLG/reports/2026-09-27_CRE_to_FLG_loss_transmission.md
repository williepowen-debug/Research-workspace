# FLG leg — how CRE distress becomes Flagstar losses, what absorbs them, and the case against (2026-09-27, Sun PM)

**Commissioned by:** PROME, for Will's 17:24 ET objective (`PROME/plans/2026-09-27_cre-to-bank-loss-transmission-PLAN.md`, e614dee5e). **Author:** FLG. Research only: no score, threshold, gate, tool or trade change.
**Entity:** Flagstar Bank, N.A. (NYSE: FLG · CIK 0000910073 · RSSD 694904). This is a single legal entity since Oct-2025, so 10-Q, earnings release and Call Report figures describe the same bank.
**Primaries (all read or re-verified by FLG on 2026-09-27):** 10-Q Q2-26 (acc 0000910073-26-000068) · Q2 earnings 8-K of 2026-07-24 (acc 0000910073-26-000065: release, deck, EX-99.3 buyback) · 10-Q Q1-26 (acc …-26-000047) · 10-K FY2025 (acc …-26-000025) · 10-K FY2024 (acc …-25-000038). FLG ledgers: `workbook/KB.tsv` (KB-FLG-0xx), `workbook/NONACCRUAL_FLOW.tsv` (13 filings, identity ties 13/13).

---

## Bottom line (for PROME's synthesis)

1. **The best-evidenced route from CRE distress to Flagstar losses is value, not exits.** Annual re-appraisal of classified NYC rent-regulated multifamily collateral produces charge-offs at a steady ~1.0–1.2% annualised multifamily rate. The book feeding it is still refilling ($780M of new nonaccrual loans in H1-26). The rent freeze and the 2027 resets are **forward amplifiers of that same channel**. Neither has produced a loss yet. Today's withdrawal (KB-FLG-066) removes "losses hidden in payoffs" as an evidenced channel, which leaves appraisal write-downs as the one the filings actually name.
2. **Capacity: I agree with REGINALD's loss dollars and capital arithmetic. I differ on the earnings yardstick.** The bridge divides the stress hit by *trailing* pre-provision revenue ($143M), measured at the bottom of a turnaround that included a loss quarter. That gives 8.4–10.5×. On Q2's own run-rate the multiple is **4.5–5.7×**. On management's 2027 guidance it is **0.8–1.3×**, but that guidance needs net interest income up ~45%. **Capital is the backstop in every case.** CET1 13.16% would end ~0.4–1.2pp above the 10.5% target under the bridge's stress if the $250M buyback proceeds.
3. **The strongest case against:** the bank is already self-liquidating its problem book at par at scale ($1.1B a quarter, 39% substandard), faster than new problems form. Its credit metrics except coverage are improving. And the one input that would drive the stress case, the rent freeze, bites in 2028, leaving 2+ years of earnings between now and the bite.

---

## (1) Strongest evidenced mechanism

### OBSERVED

| # | Fact | Source · date | KB |
|---|---|---|---|
| O1 | MF + CRE gross charge-offs H1-26 **$193M**, "primarily driven by **appraisals** received on those loans and the resolution of a single borrower relationship undergoing bankruptcy proceedings" (Q1-26) | 10-Q Q2-26, asset-quality text | 061, 063 |
| O2 | Policy: updated appraisals **at least annually** on all substandard and non-accrual MF/CRE/land loans. **70%** of NYC rent-regulated criticized + classified loans appraised since 1/1/2024 | 10-Q Q2-26; deck (NYC MF Credit Details) | — (annual-review timing: 037) |
| O3 | MF net charge-off rate (annualised): Q2-25 **1.17%** · Q1-26 **1.01%** · Q2-26 **1.17%**. **Flat year on year.** MF NCOs since Jan-2024: **$689M** | Q2 earnings release NCO table; deck | 062 |
| O4 | NYC ≥50% rent-regulated **criticized + classified** $4,401M: LTV **78%**, amortizing DSCR **1.01×**, **49%** reset within 18 months. Pass-rated RR $4,089M: LTV 61%, DSCR 1.51× | Deck, NYC MF Portfolio Details, 6/30/26 | — (exposure: 033) |
| O5 | RR nonaccrual: original $2,088M, **$351M (16.80%) already charged off**, ACL $76M (4.38% of $1,737M book) ⇒ **20.45%** recognised | Deck s16 (REGINALD + FLG agree; the 17.5% variant is withdrawn) | 062 |
| O6 | Gross new nonaccrual **$780M in H1-26**, replacing 81.7% of outflow. **~40% of nonaccrual loans are current** on contractual terms | 10-Q non-accrual roll-forward | 030 |
| O7 | Charge-off perimeter gap: reserve-table gross vs nonaccrual-schedule charge-offs, 50–73% every period FY23–Q2-26. **It does not scale with payoffs** (11%–350% of exits; FY2023 gap 3.5× exits) ⇒ loss-at-exit is **not** the evidenced channel | 10-Qs/10-Ks as listed | 061, **066** |
| O8 | Rent freeze (RGB Order #58, 0%) takes effect for leases commencing **2026-10-01 → 2027-09-30**. No stay at the 9/24 hearing; merits ruling "before the end of the year." Q2 provision rose $18M, partly for "recent NYC rent-regulated multi-family developments" | THE CITY 2026-09-24; Q2 release | 032, 060 |
| O9 | MF repricing/maturity: **$8,503M (31.6% of MF) in 2027**; the 2027 vintage **grew +2.1%** in dollars while MF shrank −7.08% | 10-K FY25 + 10-Q Q2-26 maturity tables | 046, 047 |

**Selected mechanism: capped rent-regulated income → lower appraised collateral value at the annual re-appraisal → partial charge-off, applied to a classified pool that keeps refilling.** O1, O2, O3 and O5 show it operating now. O6 shows the pool refilling: 40% of the book is "paying but failing on collateral," the signature of a value channel, not a payment channel. O4, O8 and O9 are the inputs that could make it worse.

**How KB-FLG-066 changes it:** before today, "loss-bearing exits" (par payoffs that were not really par) was a candidate second channel. The gap profile makes that unsupported as the main route. This **concentrates** the evidenced mechanism on appraisals. It neither widens nor narrows the loss estimate, because charged-off losses are excluded from REGINALD's bridge whichever route they took.

### SCENARIO ASSUMPTIONS
- **S1.** The freeze lowers NOI growth, and appraisers capitalise that lower NOI into lower values, which flow into charge-offs at the following annual review. Basis: management's own stress assumes a **3-year** freeze with NOI −7–8% over 3 years on >70%-regulated buildings (May 2026 conference, KB-055, MIRROR-grade).
- **S2. Timing:** leases renew through 9/2027, so FY2027 borrower financials, reviewed **Q2-2028**, are the first carrying most of a freeze year (KB-052). A quiet Q2-2027 is expected and would not disconfirm.
- **S3.** The 2027 resets (coupons ~3.9% → ~8% at reset, per the bridge's anchor) push DSCR on the 1.01× pool below 1.0× unless the loan is paid off or modified. This is the cash-flow leg (A); the appraisal leg is value (B).

### UNKNOWNS
- **U1.** Where the $133M H1 charge-off gap sits (exit vs accruing write-down). Not disclosed. Next split test: the Q3 10-Q.
- **U2.** Whether a merits annulment after 10/1 would unwind leases already signed at 0%. No source read addresses retroactivity.
- **U3.** Identity and remaining exposure of the Q1 bankruptcy relationship (not named in the 10-Q; press candidate only, KB-063).

---

## (2) Capacity to absorb

### OBSERVED

| # | Fact | Source · date |
|---|---|---|
| C1 | CET1 **13.16%** (Q1 13.23%, YE25 12.83%); Tier 1 13.99%; total RBC 16.58%; leverage 9.70% | Q2 release, regulatory capital table, 6/30/26 |
| C2 | Target CET1 **10.5–11.5%**; management states **excess capital $1.6B** at the 10.5% low end ⇒ implied RWA ≈ $60B (derived: $1.6B / 2.66pp) | Q2 release; deck long-term targets |
| C3 | ACL **$869M** total; MF $439M + CRE $153M = $592M on MF/CRE; specific reserve on nonaccrual $163M | 10-Q Note 6 |
| C4 | PPNR (non-GAAP, company): Q2-26 **$66M**, Q1-26 **$32M**; adjusted $62M. REGINALD's trailing-4Q **$143M** ⇒ Q3-25 + Q4-25 = $45M combined | Q2 release PPNR table |
| C5 | **$250M buyback** authorised 7/24/26, 12 months; execution to date unknown | 8-K EX-99.3 (KB-064) |
| C6 | Management guidance, **2027**: NII $2,500–2,650M · non-interest income $390–430M · adjusted opex $1,650–1,700M · **provision $100–150M** · net income $800–900M. 2026: NII $1,860–1,960M, provision $90–140M, net income $225–300M | Deck guidance table, 7/24/26 |
| C7 | Management's CRE concentration: **350%** (Q1 367%). FLG's own SR 07-1 computation: **327.5%**. The gap matches FLG's owner-occupied-included variant (≤351.6%), so **the issuer's definition is wider**. Same direction, different level | Q2 release; FLG STATUS 8/28 reconciliation table |

### Reconciliation to REGINALD's bridge (b93e3ac58)

| Item | REGINALD | FLG | Verdict |
|---|---|---|---|
| Pool balances, reserve credits | $35.2B MF+CRE; reserves $113–420M; ties to MF $439M + CRE $153M | Same figures at the primary | ✅ **AGREE** |
| 20.45% recognised on RR nonaccrual | 20.45% (17.5% withdrawn) | 20.45% | ✅ **AGREE**, one figure |
| Stress loss $1,618M, new hit $1.2–1.5B | Assumption-driven; FLG CRE pools ASSUMPTION ONLY (CREED) | No better anchor exists; I do not re-rate them | ✅ **AGREE** it is a scenario, not a forecast |
| CET1 13.16% → 11.3–11.7% (10.9–11.3% with buyback) | Tax-effected at ~25% on ~$60B RWA | Reproduces: $1,198M × 0.75 / $60.2B = 1.49pp; buyback $250M / $60.2B = 0.42pp | ✅ **AGREE** |
| **Earnings yardstick** | **8.4–10.5×** trailing-4Q PPNR ($143M) | Trailing 4Q is the trough of a turnaround and includes a loss quarter. Q2 run-rate ($66M × 4 = $264M) ⇒ **4.5–5.7×**. Guided 2027 PPNR (C6: NII + NonII − opex) = **$1,190–1,430M** ⇒ **0.8–1.3×** | ⚠️ **DIFFER on basis, not arithmetic.** All three belong in the synthesis, labelled. Trailing is the only *observed* one; guidance is management's assertion |
| Management's own credit budget | — | 2026 + 2027 provision guidance **$190–290M** in total ≈ the bridge's **BASE** new hit ($211–407M). **Management plans on roughly the base case, not the stress** | ➕ FLG addition |
| Buyback | Included as a sensitivity | Also pushes the CRE concentration ratio **up** ~8pp (2.5% of the total-RBC denominator, KB-064), against its path below 300% | ➕ FLG addition |

### SCENARIO ASSUMPTIONS
- **S4.** Stress losses arrive over 2027–2029, the freeze and appraisal cycle, not in one quarter. If so, earnings absorb a share before capital does. At the Q2 run-rate that is ~$0.26B a year; on guidance, ~$1.2–1.4B a year. The bridge's CET1 figures assume **no earnings offset**, which is conservative on timing.
- **S5.** The guidance ramp requires NII to rise from a ~$1.76B run-rate (Q2 $440M × 4) to $2.5–2.65B (+42–51%), with NIM from 2.13% to 2.70–2.80%. The 2026 NIM guide was **already cut** to 2.20–2.30% on higher payoffs (KB-056). **Treat guidance-based capacity as the optimistic bound.**

### UNKNOWNS
- **U4.** Buyback execution to date (first read: Q3 10-Q).
- **U5.** Whether regulators constrain capital return at a 350% issuer-defined CRE concentration. No public signal read.
- **U6.** RWA path. C&I grew $2.0B in Q2 (+12%). Mix shift toward C&I raises RWA and dilutes CET1 independently of CRE losses.

---

## (3) Strongest evidence AGAINST the stress thesis (stated as strongly as I can)

### OBSERVED
- **A1. Self-liquidation at par, at scale.** CRE par payoffs were **$1.1B in Q2-26, 39% substandard**, and "unchanged compared to first quarter" (Q2 release). Since 2024: **$2.0B of NYC rent-regulated payoffs, 56% from substandard** (deck). Classified loans fell **$9.7B → $8.5B** in H1-26 (10-Q). A bank that exits substandard loans at par every quarter is converting its problem book into cash faster than the problem book grows.
- **A2. Every credit trend except coverage is improving.** SR 07-1 **470.5% → 327.5%**, falling all 11 quarters. Nonaccrual rate **4.90% → 4.59%** in H1. 30–89 day delinquencies **−63%** ($986M → $368M). MF NCO rate flat, not rising (O3). Capital up (CET1 12.83% → 13.16% over H1).
- **A3. Markets clear similar paper near par.** ARI's ~$9B loan book cleared at **99.7% of par** (CREED 9/26, primary per CREED; MIRROR to FLG). That caps how harsh a stress on FLG's **pass** book should be.
- **A4. The loss content of payoffs is not established.** After KB-066 there is no positive evidence that payoffs came in below par, beyond one $4.8M (6%) discount on a performing loan (Bisnow 2026-04-27, KB-065).
- **A5. The freeze might not survive.** A judge wrote of "significant concern" about the Board's procedure (~9/16) and promised a merits ruling by year-end. Annulment removes the stress thesis's newest input. (Quoted legal experts **expect the landlords to lose**, KB-053. The court leg is therefore the *weaker* half of this argument.)
- **A6. Time.** The freeze's first full effect reaches FLG's reviews in **Q2-2028** (S2). If the guidance ramp is even partly achieved, 2+ years of earnings sit between now and the bite. Management's own 3-year-freeze stress is already harsher than the 1-year order (KB-055).

### What the case against does NOT answer (its limits, so PROME can weigh it)
- Par payoffs depend on an **exogenous refinance market** for NYC rent-regulated buildings. That market is exactly what the freeze and higher rates impair. The 2027 wall ($8.5B) tests it.
- **Cures are 1.6%** of nonaccrual outflow (from 59.5% in 2023H1). The book is being handed off, not healed.
- **Coverage is at a series low** (31.04%), and $1,571M of nonaccrual carries no allowance on the strength of appraisals.

---

## Next observations that would change the conclusion

| When | Observation | Toward stress if … | Against stress if … |
|---|---|---|---|
| **2026-10-01** (T-08) | Freeze in force on the effective date | In force: the input is confirmed. **This changes no loss figure**; the effect is a 2028 fuse | A last-minute stay: removes the 2026 leg |
| **~10/23 release / ~11/9 10-Q** (T-03/T-02) | Gross new nonaccrual (Q3) · MF NCO rate · par payoffs and their substandard share · provision language on the freeze · buyback shares repurchased | Formation re-accelerates, the MF NCO rate rises above the 1.0–1.2% band, par payoffs slow, or the buyback proceeds while coverage falls | Formation stays below H1's run-rate, payoffs hold at ~$1B+ per quarter with a high substandard share, and the NCO rate stays flat |
| **~10/24 → year-end** (T-12) | City's full production, then the merits ruling | Freeze upheld | Freeze annulled (check retroactivity, U2) |
| **Q3 10-Q** | Charge-off gap vs payoff volume (KB-066 split test) | Gap tracks exits: payoffs were lossy | Gap tracks the Q2-loaded appraisal cycle on accruing loans: the appraisal channel confirmed as the only one |
| **Q2-2028** (T-11) | First DSCR review on a mostly-frozen year | Formation step-up from the RR pass book ($4.1B, DSCR 1.51×) | No step-up: the freeze is absorbed |

**Isolated vs broader (FLG's contribution to that question):** FLG's mechanism is **name- and city-specific**. NYC rent regulation, HSTPA-2019 and RGB Order #58 are not tier-wide inputs. Two parts do carry beyond FLG: the refinance-dependence of the exit channel (any bank clearing problem CRE by payoff) and the appraisal-lag recognition route. The cohort read is REGINALD's.

— FLG


---

## ADDENDUM 2026-09-27 ~18:1x ET — news sweep found the Q1 bankruptcy resolution (KB-FLG-067). Changes §(1) U3 and §(3) A1; the body above is left as delivered

- **What:** the Pinnacle Group portfolio (~93 buildings, ~5,100 mostly rent-stabilized NYC units; Chapter 11 since May 2025; Flagstar debt ">$564M" / ">$600M" in press) was sold to Summit Properties for **$451.3M**, closing **2026-03-31**. **Flagstar financed the buyer: $338.5M, ~75% of the price** (Multifamily Dive 2026-01-20; TRD 2026-03-31). This is a **strong candidate, not issuer-confirmed**, for the 10-Q's Q1 "single borrower relationship undergoing bankruptcy." The borrower is unnamed in the 10-Q and the docket was not read.
- **§(1) U3 (identity):** answered to candidate grade.
- **§(3) A1 weakens.** "Self-liquidation at scale" overstates how much exposure left the bank. The largest H1 exit was **(a) below Flagstar's debt** (price ≤80% of it, before costs) and **(b) about three-quarters refinanced into a new Flagstar loan** to the buyer. Only ~$113M arrived as buyer cash. The "par payoffs" of $1.1B/quarter are a different, company-labelled series and are not contradicted by this. What this undercuts is reading the nonaccrual schedule's payoff/disposition leg as exposure removed.
- **§(1) and KB-066:** this is one confirmed loss-bearing disposition inside the payoff line in Q1. It does **not** restore loss-at-exit as the leading explanation of the multi-year charge-off gap (Q2's $60M gap had no such event).
- **Next observation added:** the grade and performance of the $338.5M Summit loan, if it is ever disclosed. It sits on the same rent-stabilized collateral, now at ~75% of a 2026 clearing price.
