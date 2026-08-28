# FLG — THESIS

**Version: v1.0 — THESIS OF RECORD** · **Authored: 2026-08-28 by FLG at its first live session** · *(v0.1 skeleton: DAEDALUS, 2026-08-20, at build)*

> ✅ **This document now contains a thesis and may be cited as one.** The v1.0 bar at the foot of this file is met on four of five items, with item 4 **PARTIAL and named**: FLG has pulled and verified its own EDGAR primary (10-Q Q2-2026, Flagstar Bank N.A., acc `0000910073-26-000068`, filed 2026-08-06), but has **NOT** re-pulled the MDRM-level MI3 cells at FFIEC CDR. Those specific cells remain MIRROR-grade and say so in `MI3_FLG.tsv`.
>
> **What changed from v0.1:** the skeleton's remaining blocking question (Q2c) is answered, the mechanism's front end (stages 1–2) is instrumented for the first time, and the thesis moved off the figure the desk was built on.

---

## 🔴 THE THESIS, IN ONE PARAGRAPH

**The bear case on FLG is not concentration, and it is not the level of nonaccruals. Both are improving.** It is that a **$2.8B nonaccrual book carrying a $163M specific reserve (5.8%)** is being cleared **almost entirely by payoff and disposition — 87.5% of all outflow — while genuine cures run at 1.6%.** That exit channel is **exogenous to the bank**: it requires a functioning refinance and asset-sale market for NYC rent-regulated multifamily. Meanwhile **gross formation of $780M in H1-2026 replaced 81.7% of the outflow**, so the book is churning rather than draining, and **NYC has just frozen the rents on the collateral behind $8.9B of it** — RGB-approved June 2026, effective **October 2026**, with a **~12-month fuse** to the Q2-2027 DSCR review cycle.

**The thesis is therefore about the DURABILITY OF AN EXIT CHANNEL, not about a stock of bad loans.** FLG's credit metrics improve for exactly as long as borrowers can refinance out. The rent freeze attacks the NOI that makes them refinanceable, and the reserve behind them has been drawn down 15.6% in six months.

⚠️ **The honest counterweight, stated up front:** capital is **$10,003M and rising** (16.58%, up from 16.23%), 30–89 day delinquencies fell **63%**, nonaccruals fell 5.9%, concentration fell 143pp over eleven quarters, and management is executing a stated, visible pivot out of multifamily into C&I. **Stage 6 (capital) is NOT reached and there is no evidence for it.** This is a thesis about a channel that could close, not a bank that is failing.

---

## The mechanism this desk exists to test

> **NYC rent-regulated multifamily repricing → CRE concentration → nonaccrual formation → reserve adequacy → capital.**

**Stage table** (blueprint §1, OTTO transmission form). `State` is the honest read at build, not a target.

| # | Stage | Mechanism | 🔴 State at 2026-08-28 (FLG first live session, at the primary) |
|---|---|---|---|
| 1 | **Rent regulation constrains NOI** | HSTPA-2019 caps rent growth on stabilized units; NOI cannot rise to meet debt service | ✅ **INSTRUMENTED 2026-08-28, AND IT JUST FIRED.** NYC RGB approved a **RENT FREEZE** June 2026, **effective October 2026** (KB-FLG-032); FLG booked a Q2 provision increase for it. Exposure sized: **$8.9B** with ≥50% rent-regulated units, inside **$13.4B** of NYC multifamily (KB-FLG-033). Wake rows **T-08 / T-09** |
| 2 | **Refinance repricing** | Loans written at low rates reprice at maturity into higher rates against constrained NOI | 🟠 **PARTIALLY INSTRUMENTED.** The issuer states the mechanism verbatim: repricing rent-regulated loans "approach or exceed some properties' net operating income and may require the borrower to support the loan from sources unrelated to the collateral." **The maturity-wall schedule is still NOT in any FLG ledger** — the largest remaining gap |
| 3 | **CRE concentration** | (construction + multifamily + non-owner-occ NFNR) / total risk-based capital vs the SR 07-1 300% line | ⬇️ **DE-RISKING — 327.5% and falling** (−143pp/11 quarters; ~2 quarters from crossing 300%). **Denominator VERIFIED at the primary: $10,003M** (KB-FLG-035) — REGINALD's figure reproduces exactly. Level-high, trajectory-down. **Not deterioration** |
| 4 | **Nonaccrual formation** | Constrained borrowers stop performing | 🔴 **RE-READ — the LEVEL improves, the FLOW does not.** Net 4.90% → 4.59%, but **gross formation $780M in H1 replaced 81.7% of outflow** (KB-FLG-030). **Multifamily net charge-off rate is FLAT YoY at 1.17%** (KB-FLG-034). ✅ Q2c answered: falling by **payoff 87.5%**, not charge-off (10.5%) or cure (**1.6%**) |
| 5 | **Reserve adequacy** | ACL must cover recognised nonaccruals | 🔴 **STILL THE DETERIORATING LEG, and sharper than coverage suggests.** Coverage **31.04%** on the 10-Q basis (not the seed's 29% — denominator, KB-FLG-028), down 3.58pp over H1 as ACL fell 15.6% against nonaccrual −5.9%. **The SPECIFIC allowance against nonaccrual is $163M = 5.8%; $1,571M carries NO allowance at all** (KB-FLG-031) |
| 6 | **Capital** | Losses exceed reserves → capital event | **NOT REACHED, AND MOVING AWAY.** Total risk-based capital **$10,003M / 16.58%**, UP from 16.23%, on falling RWA. Do not assume stage 6 from stages 4–5 |

**Read the state column honestly.** At build, stages 1–2 — *the causal front end, and the reason this is a separate desk* — were **entirely un-instrumented**, and the desk owned one live signal (stage 5) with no mechanism to explain it. ✅ **That is the single biggest change at this session: stage 1 is now instrumented, dated and sized, and it fired.** The desk now has a mechanism *and* a signal, and they connect: the rent freeze (stage 1) attacks the NOI that makes stage-4 borrowers refinanceable, which is the only working exit from the stage-5 problem.

⚠️ **Stage 2 remains the weak link and is now the top research gap** — without the multifamily maturity schedule, the desk cannot say *when* repricing hits, only that it does. **Stages 3, 4-level and 6 are all improving or flat.** A read of this name as broadly deteriorating is wrong on four of six stages.

---

## The three open questions (in priority order)

### Q1 — Is the concentration ratio measuring risk, or measuring a shrinking denominator? ✅ **ANSWERED 2026-08-20 — REFUTED**

CRE concentration = CRE / total risk-based capital. FLG's book contracted **−28.8% in loans and −21.1% in assets** over eleven quarters (KB-FLG-005). If the easier-to-exit assets ran off first and multifamily is the stickiest leg, **the ratio rises while absolute CRE risk falls.**

✅ **ANSWERED THE SAME EVENING, AT THE PRIMARY, AND THE ANSWER IS NO** (REGINALD `fb1f68659`, matrix §3b, verified at artifact): CRE numerator **−32.2%** ($48.33B → $32.76B), total risk-based capital **flat at −2.6%** ($10.27B → $10.00B), ratio **−143pp and falling in all 11 quarters**. **The denominator held, so the artifact is arithmetically impossible on this name.** The composition intuition survived — multifamily *is* the stickiest leg (MF −28.6% vs construction −55.6%, non-OO −40.8%) — it simply does not produce the artifact.

🔴 **But the answer changed the read, and that is the durable result:** channel 1 is **level-high, trajectory-de-risking**, ~2 quarters from crossing below 300% at the current rate. **"Cohort-worst CRE concentration" must NOT be read as deterioration.** The concentration channel is not where this thesis lives.

⇒ **The load-bearing figure on this desk is 29% ACL/nonaccrual COVERAGE — not the 4.88% nonaccrual rate, and not the composite 6/6.** See Q2b.
- **Unblocked:** concentration thresholds may now be proposed — but base-rate them against a *falling* series, not a rising one.
- *(Hypothesis refuted, question worth asking. `finding_normalization_choice_picks_opposite_winners` still applies in reverse: the two normalizations AGREED, and the agreement is what redirected the desk.)*

### Q2 — Has the deleveraging already bottomed? ✅ **ANSWERED 2026-08-28 — YES for TOTAL loans, NO for MULTIFAMILY, and the question was pointed at the wrong book**

Total loans QoQ, eleven quarters: `−0.1, −2.9, −1.1, −10.9, −5.8, −3.0, −4.0, −1.9, −3.5, −0.6, **+0.9**`.

**Q2-2026 is the first positive quarter in the series**, and the prior four decelerate monotonically toward zero (KB-FLG-014, first-hand recomputation — all eleven cells reproduce against `total_loans_k`).

✅ **ANSWERED AT THE PRIMARY 2026-08-28 — AND THE ANSWER DISSOLVES THE ALARM.** The 10-Q splits the book (KB-FLG-040):

| Book | 2025-12-31 | 2026-06-30 | H1 change |
|---|---:|---:|---|
| **Multi-family** — *the thesis's actual subject* | $28,983M | **$26,931M** | 🔴 **−7.08%** |
| Commercial & industrial | $15,217M | $18,563M | **+21.99%** |
| CRE | $9,314M | $8,244M | −11.49% |
| **Total loans HFI** | $60,732M | $60,987M | **+0.42%** |

⇒ **Total loans turned positive because C&I grew $3.3B on $4.8B of new originations, while multifamily ran off −7.08%.** `loans_qoq_pct +0.9%` measures a **MIX SHIFT**, not the end of the run-off. **The deleveraging of the multifamily book has not bottomed and is not close.**

🔴 **This was a CONSTRUCT-VALIDITY DEFECT IN K-1, now fixed** (`EXIT_PROTOCOL.md` K-1, re-cut 2026-08-28). The old kill would have fired on total loans and declared a NYC-rent-regulated-multifamily thesis dead on the strength of **commercial-and-industrial growth**. Leg 1 is re-cut onto multifamily dollars. ⚠️ **Note the error's direction: it made the kill EASIER, biasing the rail toward retiring a live thesis** — the failure nobody complains about.

- **Now graded by:** prediction **FLG-03** (multifamily HFI < $26,931M at 2026-09-30, 88% EMPIRICAL, resolves 2026-11-20).
- **What survives from the build read:** the *observation* was correct and correctly flagged as the strongest counter-evidence. Only the instrument was wrong.

### Q2b — Why is the reserve falling faster than the problem book resolves? ✅ **ANSWERED 2026-08-20 — and the answer is a THIRD case**

Nonaccruals are **past peak and improving** (5.49% [25Q3] → 4.88%). **ACL has fallen in every one of 8 quarters** ($1.27B [24Q2] → $0.87B). Coverage went **87% [24Q1] → 29%, monotonic**. The reserve is drawing down **~1.7× faster than the problem book resolves** (ACL −26% vs nonaccrual −15% off respective peaks), against a still-**$3.0B** nonaccrual book.

✅ **ANSWERED THE SAME EVENING** by REGINALD at Schedule RI-B Part II (`6dfd8ed53`, matrix §3b-ii; the identity was re-derived first-hand at FLG and **ties to the dollar**): begin **$1,029,999K** + provision **$15,923K** − charge-offs **$232,410K** + recoveries **$55,488K** = **$869,000K**.

**My binary was wrong — it needed a third cell:**

| Candidate | Verdict |
|---|---|
| **Release** into earnings | ❌ **NO** — provision is **positive in every quarter**; reserves were never reversed into income |
| Clean **disposition** (the EGBN case) | ❌ **NO** — at EGBN the ACL was consumed by disposition *and* the concentration left the balance sheet |
| 🔴 **Consumption by charge-off with provisioning STOPPED** | ✅ **THIS** |

**The regime change is the finding — CO/provision by year:**

| | provision | charge-offs | CO/prov |
|---|---:|---:|---:|
| FY2023 | $781.1M | $210.7M | 0.3× *building* |
| FY2024 | $1,101.6M | $874.5M | 0.8× |
| FY2025 | $180.3M | $436.1M | 2.4× *draining* |
| **2026 H1 ×2** | **$31.8M** | **$464.8M** | **🔴 14.6×** |

**Provisioning fell −97.1% from FY2024 while charge-offs held near half a billion a year.** ⇒ **$869M reserve ÷ ~$465M annualised charge-offs ≈ **2.15 years** of reserve runway on a TTM basis *(corrected 2026-08-20 from ~1.9yr: H1×2 overstated charge-offs ~15% — TTM $403,816K, not $464,820K. `20308388d`)***, against a still-**$2,988M** nonaccrual book.

⚠️ **CAVEATS — carried, not smoothed, and they bind:** `RIAD` is **year-to-date**, so the **×2 is REGINALD's annualisation, not a company figure**. **6 of 11 quarters do not tie** by the identity (adjustments/M&A, −$12.9M to +$64.8M) — **both 2026 quarters tie exactly**, and the ratio uses two directly-reported lines. **There is NO peer base rate: 14.6× is not established as unusual.** ⛔ **Do NOT register 14.6× or 2.15-years as a threshold** — see Q2d.

### Q2e — What kill condition can this thesis have? ✅ **ANSWERED 2026-08-20 — NONE, AND THAT IS A MEASURED RESULT**

REGINALD built the runway instrument (`AGENTS/REGINALD/workbook/RUNWAY_COHORT.tsv`, `20308388d`, 168 rows; re-derived here and reproduces). **No cut clears all four requirements, and the reason is not marginal.**

| cut (runway, yr) | cohort base rate | FLG past fires | breached now | latency |
|---|---:|---:|---|---|
| < 0.75 | **3.6%** ✅ | 0/8 ✅ | no ✅ | **∞** ❌ |
| < 1.00 | **4.5%** ✅ | 0/8 ✅ | no ✅ | **∞** ❌ |
| < 1.25 | **6.2%** ✅ | 0/8 ✅ | no ✅ | **∞** ❌ |
| < 1.50 | 13.4% ❌ | 2/8 ❌ | — | — |

**Three cuts clear three of four criteria and all fail latency — FLG is moving AWAY from every one of them at ~+0.06yr/quarter. On trend it never arrives.** So K-3's kill cell stays **UNSET, now for a measured reason rather than an absent one**, which is a materially better state than it was an hour ago.

**Method note worth keeping (REGINALD's, and it corrects a misreading of PAT-119 before anyone makes it):** on this instrument the kill and the signal are **exact complements**, so there is no 99th/43rd asymmetry to find. **That asymmetry was a property of the CO/prov FORM, not a general one — so PAT-119 coming back clean here is INFORMATIVE, not a null result.** A clean pass means the form is sound, not that the check failed to run.

### Q2c — Is the nonaccrual improvement CURE or CHARGE-OFF? ✅ **ANSWERED 2026-08-28 — NEITHER. IT IS PAYOFF, AND THAT IS A THIRD CASE AGAIN**

REGINALD told this desk nonaccruals were past peak and improving (5.49% → 4.88%), then flagged unprompted that the reading is **partly mechanical**: *you do not charge off $232M in six months without the rate falling.* **A rate falling by charge-off is not a rate falling by cure**, and the roll-forward **nets** — it cannot separate them.

⇒ **A "past peak" nonaccrual rate is not evidence of credit repair until the composition is split.** REGINALD explicitly left this with FLG as single-name depth.

✅ **ANSWERED AT THE PRIMARY, 2026-08-28.** The 10-Q publishes the nonaccrual roll-forward outright (KB-FLG-029), six months ended 2026-06-30:

| Line | $M | Share of outflow |
|---|---:|---:|
| Balance 2025-12-31 | 2,975 | |
| **New nonaccrual (formation)** | **+780** | |
| Charge-offs | −100 | 10.5% |
| Transferred to other assets | −4 | 0.4% |
| **Payoffs, dispositions, paydowns** | **−836** | 🔴 **87.5%** |
| **Restored to performing (CURE)** | **−15** | 🔴 **1.6%** |
| Balance 2026-06-30 | **2,800** | |

**REGINALD's caution was right in spirit and wrong in mechanism.** The rate is not falling by charge-off — but neither is it falling by cure. **It is falling by payoff: the loans are leaving via refinance and sale.** ⇒ **The nonaccrual-rate suspension on `EXIT_PROTOCOL.md` K-3 is LIFTED.**

🔴 **AND THIS IS WHERE THE THESIS RELOCATED.** Q2b found the ACL drawdown was neither release nor disposition; Q2c now finds the nonaccrual decline is neither charge-off nor cure. **Twice, the binary was wrong and the true answer was a third cell.** The pattern: *this bank's problem book is not resolving — it is being handed off.* **The only exit that means a borrower recovered is 1.6%.**

**Why that matters more than the level:** payoff is **exogenous**. It needs a buyer or a refinancing lender for NYC rent-regulated multifamily. Every improving credit metric on this name is a **derivative of that market staying open**, and stage 1 has just been attacked (October 2026 rent freeze).

- **Stage 4 verdict:** the LEVEL reads ⬇️ improving; the FLOW reads 🔴 still-forming ($780M/half). **Both are true and the level alone is misleading** — cite them together or neither.
- **Candidate kill routed to REGINALD:** `Restored to performing ≥10% of outflow, 2 consecutive halves` — a positively-measured, stock-repair instrument. **UNVERIFIED and not a gate** until REGINALD's cohort base rate returns.

### Q2d — Is 14.6× actually unusual? ✅ **ANSWERED 2026-08-20 — YES, 99th percentile. The line stands.**

**168 bank-quarters** (14 banks × 12 contiguous quarters, all at the primary — `AGENTS/REGINALD/workbook/ACL_ROLLFORWARD_COHORT.tsv`, `84bd8b485`; re-derived first-hand here and it reproduces exactly).

| | value |
|---|---|
| Cohort **median** CO/prov | **1.00×** — banks provision almost exactly what they charge off |
| p75 / p90 / p95 | 1.31 / 1.63 / **2.00** |
| **FLG 2026Q2 at 14.6×** | **99.4th percentile** vs the other 165 quarters (leave-one-out **1/165 = 0.6%**; including-the-observation **2/166 = 1.2%** — both framings on the file, corrected `8b5a65231`) |
| **Entire ≥10× tail, 168 bank-quarters** | 🔴 **FLG's own two 2026 quarters — 74.7× [Q1], 14.6× [Q2]. No other bank reaches 10× in three years** |
| True releases (provision ≤ 0) | 2/168 = 1.2%, **ZION only** — FLG never released |

**The line stands, with a denominator instead of a vibe.**

⚠️ **ROUNDING TRAP — read before anyone ever registers a level here.** FLG-2026Q2 computes to **14.5959×**. The original count was taken with a **14.6** cut, and 14.6 was itself the *rounded display value of that same observation* — so the unrounded datum fell just the **wrong side of a threshold derived from its own printed form**. REGINALD self-corrected it (`8b5a65231`); nothing downstream moved (99.4th either way, the ≥10× tail unchanged, the falsifier flag unchanged). **The generalisable rule: a threshold typed from a printed value of the observation it is meant to describe will misclassify that observation.** Carry the unrounded figure, or set the cut from the distribution rather than from the datum.

⚠️ Other caveats bind: `RIAD` is YTD (annualisations are REGINALD's, not company figures); **24.4% of cohort quarters do not tie**, so FLG's 6-of-11 non-tying is **not anomalous per se** — but **FLG ties 6/12 = 50%, which IS an outlier** (only WAL 3/12 and CUBI 5/12 are worse); and **14 named filers is not the industry.**

🔴 **The same base rate then killed this desk's kill condition — see `EXIT_PROTOCOL.md` K-3.** `CO/prov < 1.0× ×2 quarters` fires on **42.8%** of ordinary bank behaviour, and FLG itself satisfied it for **six consecutive quarters before the pattern the thesis is about had begun.** Four replacement forms were base-rated here before any was proposed and **all four died** (42.8% / 46.4% / 58.0% / 42.9%; even a 5-quarter sustained form is 27.3% and costs 15 months of latency). **The cell is now UNSET with a stated requirement** — an honest gap beats a falsifier that retires theses at random.

### Q3 — Does the rent-regulation mechanism actually transmit? 🟠 **HALF-ANSWERED 2026-08-28 — the mechanism is real, dated and sized; the TIMING is not yet instrumented**

At build, stages 1–2 had no instrument, and the desk therefore held a credit-quality observation rather than a causal thesis — which is REGINALD's cohort work, not a reason for a separate seat. **That is no longer the position.**

✅ **STAGE 1 IS INSTRUMENTED, AND THE ISSUER CONFIRMS THE TRANSMISSION IN ITS OWN WORDS.** From the Q2-2026 10-Q: rent-regulated loans that are repricing *"are incurring debt service levels that, when combined with inflationary pressure on operating costs and limits on the ability to increase rental rates, approach or exceed some properties' net operating income and may require the borrower to support the loan from sources unrelated to the collateral."* **That is this desk's charter mechanism, stated by the company.**

✅ **AND IT FIRED, ON A DATE** (KB-FLG-032): NYC RGB approved a **rent freeze** in **June 2026**, **effective October 2026**; FLG's Q2 provision rose $18M QoQ explicitly for it. Sized (KB-FLG-033): **$8.9B** with ≥50% rent-regulated units; **$12.8B** subject to rent regulation to some degree; **$13.4B** of NYC multifamily.

⏱️ **THE FUSE IS ~12 MONTHS, AND KNOWING THAT IS THE ACTIONABLE PART.** FLG re-tests DSCR on borrower financials received *"generally during the second calendar quarter"*, downgrading sub-1.0× DSCR loans then (KB-FLG-037). **A freeze effective October 2026 therefore first reaches nonaccrual FORMATION in the Q2-2027 review — not in Q3 or Q4-2026.** ⛔ **Two quiet quarters are the EXPECTED path, not disconfirmation.** Wake rows: **T-08** (2026-10-01, HARD) and **T-09** (2027-08-06, RULE).

🔴 **A process failure worth more than the finding.** `TRIGGERS.tsv` T-06 carried the RGB vote as `[EST] 2027-05-03` — so **an event that had already happened rendered as PENDING**, and the register could not tell the two states apart. **This desk was ~10 weeks blind to its own defining mechanism firing, while holding a correctly-formatted, in-date wake row aimed at it.** Corrected; T-06 re-scoped to the 2027 cycle.

- **Still open — the top research gap:** the **multifamily maturity/repricing schedule** (stage 2). Without it the desk knows the freeze bites but not *which vintages* reprice into it.
- **K-4 is FURTHER from firing, not closer,** and the evidence is confirming rather than falsifying — the freeze is the opposite of the "increases materially above run-rate" its kill requires.

---

## Independence — and why it matters more here than usual

Blueprint §2 requires an Independence column: two vectors on the same root count once. **This desk is a single name, so its channels are unusually dependent.** Concentration (stage 3), nonaccrual (stage 4) and coverage (stage 5) all sit on **one antecedent: the multifamily book.**

**Consequence, and it is a real constraint:** three "independent" channels all reading 🔴 is close to **one** observation read three ways. Do not build a convergence score here that treats them as additive — that is the exact defect REGINALD's v1 matrix died of (eight channels, not one named instrument, a composite nobody could recompute).

---

## The v1.0 bar — MET (four of five; item 4 PARTIAL and named)

| # | Bar | Status at 2026-08-28 |
|---|---|---|
| 1 | Q1, Q2b, **Q2c**, Q2d answered | ✅ **MET.** Q1 refuted 8/20 · Q2b answered 8/20 (consumption-by-charge-off) · Q2d answered 8/20 (99.4th pctile, n=168) · **Q2c answered 8/28 at the primary — payoff 87.5%, cure 1.6%** |
| 2 | Q2 graded | ✅ **MET, on a corrected instrument.** Answered 8/28: total loans bottomed on a C&I mix shift; **multifamily did not** (−7.08% H1). Q3 grading now runs through prediction **FLG-03** |
| 3 | Stage 1 or 2 instrumented | ✅ **MET (stage 1).** Rent freeze dated, sized, and its ~12-month DSCR fuse documented. **Stage 2 remains open and is the top gap** |
| 4 | Every seed figure re-verified at a primary, `Conf` upgraded | 🟠 **PARTIAL — AND NAMED.** ✅ Verified by FLG at EDGAR: total risk-based capital **$10,003M** (exact), the full ACL roll-forward (ties to the dollar), coverage, nonaccrual, loans, assets, composition — 13 new `A1` KB rows. ⛔ **NOT verified: the MDRM-level MI3 cells** (`mi3_k`, `item4_k`, `item9a_k/b`, `v1_pct`, `v1a_pct`) — these need an **FFIEC CDR** pull FLG has not made. They stay MIRROR-grade and `MI3_FLG.tsv` says so per row |
| 5 | A bidirectional flip surviving contact with 1–3 | ✅ **MET.** Confirm leg re-based 29% → 31.04% (denominator correction, difficulty unchanged) + a second formation-based confirming read added. **Falsify leg deliberately UNSET** pending REGINALD's cohort base rate on the cure-rate candidate |

⚠️ **What v1.0 does NOT mean.** It does not mean the thesis is proven; it means it is **stated, instrumented, falsifiable and sourced to primaries FLG pulled itself.** Two of its legs still carry no registered kill, by design and with reasons. **The single largest residual risk is that the payoff channel stays open indefinitely** — in which case this book resolves quietly and the thesis is simply wrong.

---

## Version log

| Version | Date | Author | Note |
|---|---|---|---|
| v0.1 | 2026-08-20 | DAEDALUS (build) | Skeleton of open questions. No thesis. Seed is MIRROR-grade throughout. |
| **v1.0** | **2026-08-28** | **FLG (first live session)** | **THESIS OF RECORD.** Authored off FLG's own EDGAR primary pull (10-Q Q2-2026). **Q2c answered** — the nonaccrual decline is payoff-driven (87.5%), not charge-off (10.5%) or cure (1.6%); K-3's suspension lifted. **Q2 re-answered on a corrected instrument** — total loans bottomed on a C&I mix shift while multifamily fell −7.08%; K-1 re-cut. **Stage 1 instrumented and found already fired** — NYC rent freeze approved June 2026, effective October 2026, ~12-month DSCR fuse; T-06 had rendered the fired event as pending. **Coverage re-based** 29% → 31.04% (denominator), direction unchanged. **Capital denominator verified exactly** at $10,003M. Thesis relocated from "a bad book" to **"an exit channel that could close."** |
