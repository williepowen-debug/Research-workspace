# FLG — THESIS

**Version: v1.0.5 — THESIS OF RECORD** (v1.0 + amendments, log at end) · **Authored: 2026-08-28 by FLG at its first live session** · *(v0.1 skeleton: DAEDALUS, 2026-08-20, at build)*

> ✅ **This document now contains a thesis and may be cited as one.** The v1.0 bar at the foot of this file is met on four of five items, with item 4 **PARTIAL and named**: FLG pulled and verified its own EDGAR primary (10-Q Q2-2026, Flagstar Bank N.A., acc `0000910073-26-000068`, filed 2026-08-06), then verified the 2026Q1/Q2 MDRM-level MI3 cells at FFIEC CDR on 2026-10-28 and pulled the Q3 row on 2026-11-01. The ten earlier MI3 rows remain MIRROR-grade; `MI3_FLG.tsv` marks authority per row.
>
> **What changed from v0.1:** the skeleton's remaining blocking question (Q2c) is answered, the mechanism's front end (stages 1–2) is instrumented for the first time, and the thesis moved off the figure the desk was built on.

---

## 🔴 THE THESIS, IN ONE PARAGRAPH

**The bear case on FLG is not concentration, and it is not the level of nonaccruals. Both are improving.** It is that a **$2.8B nonaccrual book carrying a $155M specific reserve (5.5%, 9/30)** was cleared in H1-2026 **almost entirely by payoff and disposition — 87.5% of all outflow — while cures ran at 1.6%.** That exit channel is **exogenous to the bank**: it requires a functioning refinance and asset-sale market for NYC rent-regulated multifamily. Meanwhile **gross formation of $780M in H1-2026 replaced 81.7% of the outflow**, so the book is churning rather than draining, and **NYC has frozen the rents on the collateral behind $8.5B of its multifamily book** (≥50% rent-regulated, 9/30 10-Q; $8.9B at 6/30, KB-033; the non-accrual subset was $1,737M at 6/30, KB-062) — RGB-approved June 2026 (Order #58, 0% on both one- and two-year renewals), effective **October 2026**, with a **~21-month fuse** to the **Q2-2028** DSCR review. ⚠️ *(Corrected from "~12 months / Q2-2027", KB-FLG-052 — the order governs leases COMMENCING through 2027-09-30, so FY2027 financials are the first carrying most of a freeze year. And a 0% guideline CAPS revenue rather than cutting it: expect grinding cost-driven DSCR decay, not a cliff.)*

> 🟠 **AMENDMENT 2026-11-07 (v1.0.5), Q3 10-Q: direction unchanged, one load-bearing claim weakened.** Q3 outflow inverted: **cures $144M = 56.3%, payoffs $76M = 29.7%** (9M: 13.1% and 75.3%; identity ties, *derived*). Cure class and cause are undisclosed, and a cure after a rate cut from about 9% to about 5% would be a concession, not a recovery (INFERRED, untested), so this is **not yet repair**. But the flat claim "nothing is healing" is withdrawn pending the Q4 roll-forward. Holding the other way: coverage **30.85%, FLG-02 HIT**; specific reserve **$155M = 5.5%**; multifamily criticized plus classified **+$483M** to 36.8% of the book while the book fell $983M; MF + CRE reserve **−$24M** under a flat total, charge-offs / provision **1.67×** there against 1.13× whole-bank. Formation $273M was the lowest since Q4-2023. Read: `reports/2026-11-07_Q3-2026_10Q_LEG.md`.

> ⚠️ **AMENDMENT 2026-09-27 (v1.0.1) — two figures in the paragraph above carry new caveats; neither number changes.** **(1) "Payoff" is not "par exit".** The reserve table's gross charge-offs exceed the nonaccrual schedule's charge-off line by 50–73% in every period since FY2023 (H1-26: $233M vs $100M). Loss taken at exit is one candidate home for the gap (KB-FLG-061), but the gap does not scale with payoff volume (FY2023 gap was 3.5× that year's payoffs), so appraisal write-downs on accruing loans fit at least as well, and neither leads (KB-FLG-066). The H1-26 payoff leg is also lumpy — mostly one bankrupt borrower relationship resolved in Q1 (KB-FLG-063). Net effect on the thesis: **none established.** Payoffs can no longer be cited as evidence of clean exits, and there is no positive evidence either that they were below par beyond one anecdote. **(2) The 5.8% is the *remaining* reserve.** On the NYC ≥50% rent-regulated nonaccrual subset, $351M (16.8%) was already charged off since Jan-2024 before the 4.38% reserve, so loss recognised there is ~20.5% (KB-FLG-062). The live question on the no-allowance $1,571M is unchanged — whether those written-down values survive re-appraisal — but "5.8%" alone overstates how thin the cushion is. *(Both raised by REGINALD 9/26, verified by FLG at the primary 9/27.)*

> ⚠️ **AMENDMENT 2026-09-27 (v1.0.2, written 2026-09-27 23:49 ET) — three evening findings; the direction of the thesis is unchanged.** **(3) The largest H1 exit was loss-bearing and mostly stayed on the books.** The Q1 'single borrower relationship undergoing bankruptcy' is very likely **Pinnacle** (~5,100 NYC rent-stabilized units; PRESS-GRADE, the issuer does not name it). It sold for **$451.3M** against Flagstar debt **>$564M**, closing 3/31/26, and **Flagstar lent the buyer $338.5M (~75%)**. So the nonaccrual schedule's payoff/disposition leg overstates exposure actually removed from the bank. Any effect of that financing on the price is a HYPOTHESIS; the terms were not examined (KB-FLG-067). **(4) Modifications began in 2026 and are highly delinquent.** No MF modifications in 2025. The 12-month MF modified stock was **47% past due at 6/30** ($176M of $375M; 11% at 3/31). Per Will's ruling (20:49 ET), that is a **changing aggregate population, NOT a cohort failure rate**. The issuer's 'subsequently defaulted' figures ($29M three months, $286M six months) are **UNRECONCILED**, and an earlier cohort failure is not excluded (KB-FLG-069/070; Q3 check T-13). **(5) A $250M buyback (authorised 7/24)** would, if executed, cut the SR 07-1 denominator by ~2.5% (≈327.5% → ~335.9%, ESTIMATE), against the concentration channel's path below 300% (KB-FLG-064). **Net:** (3) and (4) bear on the thesis's exit-channel claim — the problem book is being *handed off*, and part of the hand-off is back to Flagstar. Neither is a measured loss rate.

✅ **AND IT IS NO LONGER n=1.** At v1.0 that split rested on a single six-month roll-forward. FLG has since built `workbook/NONACCRUAL_FLOW.tsv` from **13 EDGAR filings, 2023Q2–2026Q2, identity ties 13/13**, and the split is the endpoint of a **monotone three-year migration** (KB-FLG-041):

| share of non-accrual outflow | 2023H1 | 2023FY | 2024FY | 2025FY | 2026H1 | **2026 9M** | **Q3 *derived*** |
|---|---:|---:|---:|---:|---:|---:|---:|
| **cures (restored to performing)** | **59.5%** | 24.0% | 5.5% | 8.5% | **1.6%** | **13.1%** | **56.3%** |
| **payoffs / dispositions** | 23.8% | — | — | 74.4% | **87.5%** | **75.3%** | **29.7%** |

**Through H1-2026 FLG had moved from curing its problem loans to handing them off.** That migration is the desk's core finding. ⚠️ Q3 is the first quarter against it, and one quarter with an undisclosed cause does not reverse three years; the Q4 roll-forward is the next read.

🔴 **AND THE THESIS NOW HAS A DATE. THREE CLOCKS, 2026-10 → 2028-Q2:**

| when | what | source |
|---|---|---|
| **2026-10** | NYC rent freeze takes **effect** — NOI growth on rent-regulated collateral goes to zero | KB-FLG-032 |
| **2027 (full year)** | **$8,519M of multi-family reprices or matures (9/30 table; $8,503M at 6/30)**, into that freeze | KB-FLG-046/111 |
| **2028-Q2** | The **DSCR review** carrying most of a freeze year (FY2027 financials) — ⚠️ **corrected from Q2-2027, KB-FLG-052** | KB-FLG-037/052 |

⚠️ **And the deleveraging is not reducing the wall.** The 2027 vintage **grew +2.1%** in H1 ($8,327M → $8,503M) and held **+0.2%** in Q3 ($8,519M) while the multi-family book **fell −7.08% and −3.65%** (KB-FLG-047/111). **The loans leaving are the ones that can leave.** That is the sharpest available answer to the deleveraging counter-thesis.

**The thesis is therefore about the DURABILITY OF AN EXIT CHANNEL, not about a stock of bad loans.** FLG's credit metrics improve for exactly as long as borrowers can refinance out. The rent freeze attacks the NOI that makes them refinanceable, and the reserve behind them has been drawn down 15.6% in six months.

⚠️ **One inherited word corrected:** coverage is **not** "monotonic" (KB-FLG-042). It fell steeply through 2024, then sat **flat in a 33–36% band for five quarters**, and **31.04% is a new series low** — a five-quarter floor that has just given way. That makes it more interesting than a smooth slide, not less.

⚠️ **The honest counterweight, stated up front:** capital is **$9,804M / 15.74%** at Q3 (CET1 12.38%), down from **$10,003M / 16.58% / 13.16%** at Q2 after the ~$216M buyback and C&I/RWA growth. Nonaccruals are **$2,817M / 4.55%**, and concentration fell to **322.11%** from 327.52%. MF 30–89-day delinquencies rose **$233M → $392M (+68%)** in Q3 after Q1's $676M: **n=3, watch, not a trend.** Management continues its stated pivot out of multifamily into C&I. **Stage 6 (capital) is NOT reached and there is no evidence for it.** This is a thesis about a channel that could close, not a bank that is failing.

---

## The mechanism this desk exists to test

> **NYC rent-regulated multifamily repricing → CRE concentration → nonaccrual formation → reserve adequacy → capital.**

**Stage table** (blueprint §1, OTTO transmission form). `State` is the current read after the Q3 10-Q, 2026-11-07.

| # | Stage | Mechanism | 🔴 Current state |
|---|---|---|---|
| 1 | **Rent regulation constrains NOI** | HSTPA-2019 caps rent growth on stabilized units; NOI cannot rise to meet debt service | ✅ **INSTRUMENTED 2026-08-28, AND IT JUST FIRED.** NYC RGB approved a **RENT FREEZE** June 2026, **effective October 2026** (KB-FLG-032); FLG booked a Q2 provision increase for it. Exposure sized at 6/30: **$8.9B** with ≥50% rent-regulated units, inside **$13.4B** of NYC multifamily (KB-FLG-033); 9/30: **$8.5B**, inside $12.9B. Wake rows **T-08 / T-09** |
| 2 | **Refinance repricing** | Loans written at low rates reprice at maturity into higher rates against constrained NOI | ✅ **INSTRUMENTED 2026-08-28 — the wall is 2027.** **$8,519M** of multi-family reprices or matures in 2027 (9/30 table, $6,938M of it Option loans hitting reset), up from $8,503M at 6/30 while the book shrank (KB-FLG-046/047/111). Ledger: `workbook/MATURITY_WALL.tsv`. Formerly: The issuer states the mechanism verbatim: repricing rent-regulated loans "approach or exceed some properties' net operating income and may require the borrower to support the loan from sources unrelated to the collateral." ~~the maturity-wall schedule is not in any FLG ledger — the largest remaining gap~~ **CLOSED.** |
| 3 | **CRE concentration** | (construction + multifamily + non-owner-occ NFNR) / total risk-based capital vs the SR 07-1 300% line | ⬇️ **DE-RISKING — 322.11% at 2026-09-30**, from 327.52% at Q2: numerator **$31,580,906K (−3.61%)**, denominator **$9,804,386K (−1.99%)** (FFIEC CDR, 2026-11-01). Level-high, trajectory-down. **Not deterioration** |
| 4 | **Nonaccrual formation** | Constrained borrowers stop performing | 🟠 **Q3 FLOW IS IN, AND IT MOVED.** Nonaccruals **$2,817M / 4.55%**. Q3 formation **$273M** against outflow $256M; **cure 56.3%, payoff 29.7%**, charge-off 13.7%. 9M formation **$1,053M replaced 87.0% of outflow**, payoff 75.3%, cure 13.1%, charge-off 11.1% (KB-105). The +$17M is C&I; MF NAL −$7M, CRE −$9M |
| 5 | **Reserve adequacy** | ACL must cover recognised nonaccruals | 🔴 **STILL THE DETERIORATING LEG.** Coverage **30.85%, a series low, FLG-02 HIT**. Specific allowance **$155M = 5.5%**, with **$1,548M carrying no allowance** (Q2 $163M, $1,571M; KB-106). Provision $74M vs charge-offs $84M = 1.13× in Q3, but MF + CRE 1.67× and that reserve −$24M (KB-108) |
| 6 | **Capital** | Losses exceed reserves → capital event | **NOT REACHED, BUT Q3 MOVED CLOSER.** Total risk-based capital **$9,804M / 15.74%**, CET1 **12.38%**, versus Q2 **$10,003M / 16.58% / 13.16%**. The ~$216M Q3 buyback plus C&I/RWA growth reduced capital and the ratio. Do not assume stage 6 from stages 4–5 |

**Read the state column honestly.** At build, stages 1–2 — *the causal front end, and the reason this is a separate desk* — were **entirely un-instrumented**, and the desk owned one live signal (stage 5) with no mechanism to explain it. ✅ **That is the single biggest change at this session: stage 1 is now instrumented, dated and sized, and it fired.** The desk now has a mechanism *and* a signal, and they connect: the rent freeze (stage 1) attacks the NOI that makes stage-4 borrowers refinanceable, which is the only working exit from the stage-5 problem.

✅ *Stage 2 was the top gap at v1.0; CLOSED 8/28 by `MATURITY_WALL.tsv` (see Q3).* **Stages 3 and 4-level are improving; stage 6 is not reached but weakened in Q3.** A read of this name as broadly deteriorating remains wrong.

---

## The three open questions (in priority order)

### Q1 — Is the concentration ratio measuring risk, or measuring a shrinking denominator? ✅ **ANSWERED 2026-08-20 — REFUTED**

REFUTED: numerator −32.2%, capital −2.6%, ratio falling every quarter, so no denominator artifact (`fb1f68659`). Channel 1 is level-high, trajectory-de-risking; "cohort-worst concentration" must not be read as deterioration. Full text rotated 2026-11-07, `archive/THESIS_ROTATED_2026-11-07.md`.

### Q2 — Has the deleveraging already bottomed? ✅ **ANSWERED 2026-08-28 — YES for TOTAL loans, NO for MULTIFAMILY, and the question was pointed at the wrong book**

Total loans turned positive on C&I; multifamily did not (−7.08% H1, −3.65% Q3). K-1 re-cut to multifamily dollars 8/28; FLG-03 graded HIT 11/07. Full text rotated 2026-11-07, `archive/THESIS_ROTATED_2026-11-07.md`.

### Q2b — Why is the reserve falling faster than the problem book resolves? ✅ **ANSWERED 2026-08-20 — and the answer is a THIRD case**

Nonaccruals are **past peak and improving** (5.49% [25Q3] → 4.88%). **ACL has fallen in every one of 8 quarters** ($1.27B [24Q2] → $0.87B). Coverage went **87% [24Q1] → 29%, monotonic**. The reserve is drawing down **~1.7× faster than the problem book resolves** (ACL −26% vs nonaccrual −15% off respective peaks), against a still-**$3.0B** nonaccrual book.

✅ **ANSWERED THE SAME EVENING** by REGINALD at Schedule RI-B Part II (`6dfd8ed53`, matrix §3b-ii; the identity was re-derived first-hand at FLG and **ties to the dollar**): begin **$1,029,999K** + provision **$15,923K** − charge-offs **$232,410K** + recoveries **$55,488K** = **$869,000K**.

**My binary was wrong — it needed a third cell:**

| Candidate | Verdict |
|---|---|
| **Release** into earnings | ❌ **NO** — provision positive in every quarter **on the Call Report RI-B basis**; ⚠️ the Q1-2026 *release* line reads $0 (KB-081), a different line, unreconciled; never mix bases |
| Clean **disposition** (the EGBN case) | ❌ **NO** — at EGBN the ACL was consumed by disposition *and* the concentration left the balance sheet |
| 🔴 **Consumption by charge-off with provisioning STOPPED** | ✅ **THIS, through H1.** Q3 provision restarted, $74M vs $84M charge-offs; one quarter (KB-108) |

**The regime change is the finding — CO/provision by year:**

| | provision | charge-offs | CO/prov |
|---|---:|---:|---:|
| FY2023 | $781.1M | $210.7M | 0.3× *building* |
| FY2024 | $1,101.6M | $874.5M | 0.8× |
| FY2025 | $180.3M | $436.1M | 2.4× *draining* |
| **2026 H1 ×2** | **$31.8M** | **$464.8M** | **🔴 14.6×** |

**Provisioning fell −97.1% from FY2024 while charge-offs held near half a billion a year.** ⇒ **$869M reserve ÷ $403.8M TTM charge-offs ≈ **2.15 years** of reserve runway** *(corrected 2026-08-20 from ~1.9yr, which used H1×2 = $465M, ~15% high. `20308388d`)*, against a still-**$2,988M** nonaccrual book.

⚠️ **CAVEATS — carried, not smoothed, and they bind:** `RIAD` is **year-to-date**, so the **×2 is REGINALD's annualisation, not a company figure**. **All 12 quarters tie** once RIAD5523 write-downs on transfer and RIADC233 adjustments are included (REGINALD 11/07; 168 of 168 across the cohort, KB-112). The peer base rate is in Q2d. ⛔ **Do NOT register 14.6× or 2.15-years as a threshold** — see Q2d.

### Q2e — What kill condition can this thesis have? ✅ **ANSWERED 2026-08-20 — NONE, AND THAT IS A MEASURED RESULT**

REGINALD built the runway instrument (`AGENTS/REGINALD/workbook/RUNWAY_COHORT.tsv`, `20308388d`, 168 rows; re-derived here and reproduces). **No cut clears all four requirements, and the reason is not marginal.**

| cut (runway, yr) | cohort base rate | FLG past fires | breached now | latency |
|---|---:|---:|---|---|
| < 0.75 | **3.6%** ✅ | 0/8 ✅ | no ✅ | **~23q** ❌ |
| < 1.00 | **4.5%** ✅ | 0/8 ✅ | no ✅ | **~19q** ❌ |
| < 1.25 | **6.2%** ✅ | 0/8 ✅ | no ✅ | **~15q** ❌ |
| < 1.50 | 13.4% ❌ | 2/8 ❌ | — | — |

**Three cuts clear three of four criteria and all fail latency. Corrected 2026-11-07 (KB-112): the runway did not lengthen every quarter, it ran 1.29 [3/31/25], 1.59, 1.90, 2.36 [12/31/25], 2.25, 2.15, 2.17 [9/30/26], 2.12yr with RIAD5523. Since the peak the slope is about −0.06yr/quarter, so the cuts sit about 15 / 19 / 23 quarters away (ESTIMATE), not infinity, and still fail the 2–3 quarter requirement.** So K-3's kill cell stays **UNSET, for a measured reason.**

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

⚠️ *H1-2026 read; Q3 inverted the mix, amendment at top.*

🔴 **AND THIS IS WHERE THE THESIS RELOCATED.** Q2b found the ACL drawdown was neither release nor disposition; Q2c now finds the nonaccrual decline is neither charge-off nor cure. **Twice, the binary was wrong and the true answer was a third cell.** The pattern: *this bank's problem book is not resolving — it is being handed off.* **The only exit that could mean a borrower recovered was 1.6% in H1.**

**Why that matters more than the level:** payoff is **exogenous**. It needs a buyer or a refinancing lender for NYC rent-regulated multifamily. Every improving credit metric on this name is a **derivative of that market staying open**, and stage 1 has just been attacked (October 2026 rent freeze).

- **Stage 4 verdict:** the LEVEL reads ⬇️ improving; the FLOW reads 🔴 still-forming ($780M/half). **Both are true and the level alone is misleading** — cite them together or neither.
- ~~Candidate kill: cure share ≥10% of outflow, 2 halves~~ **RETIRED 8/28** (not cohort-parseable; fires on FLG's own 2023 repair). K-3 UNSET; cure share is a standing observable (EXIT K-3).

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

⚠️ Other caveats bind: `RIAD` is YTD (annualisations are REGINALD's, not company figures); the earlier tie-rate outlier claim is **RETIRED**: with RIAD5523 and RIADC233 all 12 FLG quarters tie, 168 of 168 across the cohort (REGINALD 11/07, KB-112); and **14 named filers is not the industry.**

🔴 **The same base rate then killed this desk's kill condition — see `EXIT_PROTOCOL.md` K-3.** `CO/prov < 1.0× ×2 quarters` fires on **42.8%** of ordinary bank behaviour, and FLG itself satisfied it for **six consecutive quarters before the pattern the thesis is about had begun.** Four replacement forms were base-rated here before any was proposed and **all four died** (42.8% / 46.4% / 58.0% / 42.9%; even a 5-quarter sustained form is 27.3% and costs 15 months of latency). **The cell is now UNSET with a stated requirement** — an honest gap beats a falsifier that retires theses at random.

### Q3 — Does the rent-regulation mechanism actually transmit? 🟠 **MOSTLY ANSWERED — mechanism real, dated, sized; timing instrumented 8/28 (wall 2027, DSCR bite Q2-2028); transmission not yet observed**

At build, stages 1–2 had no instrument, and the desk therefore held a credit-quality observation rather than a causal thesis — which is REGINALD's cohort work, not a reason for a separate seat. **That is no longer the position.**

✅ **STAGE 1 IS INSTRUMENTED, AND THE ISSUER CONFIRMS THE TRANSMISSION IN ITS OWN WORDS.** From the Q2-2026 10-Q: rent-regulated loans that are repricing *"are incurring debt service levels that, when combined with inflationary pressure on operating costs and limits on the ability to increase rental rates, approach or exceed some properties' net operating income and may require the borrower to support the loan from sources unrelated to the collateral."* **That is this desk's charter mechanism, stated by the company.**

✅ **AND IT FIRED, ON A DATE** (KB-FLG-032): NYC RGB approved a **rent freeze** in **June 2026**, **effective October 2026**; FLG's Q2 provision rose $18M QoQ explicitly for it. Sized (KB-FLG-033): **$8.9B** with ≥50% rent-regulated units; **$12.8B** subject to rent regulation to some degree; **$13.4B** of NYC multifamily.

⏱️ **THE FUSE IS ~21 MONTHS — I FIRST SAID ~12 AND WAS WRONG (KB-FLG-052).** FLG re-tests DSCR on borrower financials received *"generally during the second calendar quarter"*, downgrading sub-1.0× DSCR loans then (KB-FLG-037). Order #58 governs leases **commencing** 2026-10-01 → 2027-09-30, so it **phases in as leases renew.** FY2026 financials (reviewed **Q2-2027**) hold at most Oct–Dec 2026 of partial exposure; **FY2027 financials, reviewed Q2-2028, are the first carrying most of a freeze year.** ⛔ **A quiet Q2-2027 is the EXPECTED path, not disconfirmation** — and I had that date wrong by a year in v1.0. ⚠️ **A 0% guideline CAPS revenue rather than cutting it**, so DSCR degrades by operating costs outrunning frozen rents — grinding and compounding, not a step down. Wake rows: **T-08** (2026-10-01, HARD) and **T-09** (2027-08-06, RULE).

- ✅ **CLOSED 2026-08-28 — the former top gap.** The multi-family maturity/repricing schedule is now `workbook/MATURITY_WALL.tsv`: **2027 is the wall, $8,519M at 9/30**, and it grew +2.1% in dollars while the book shrank (grade on dollars, never share: KB-049). Freeze 2026-10, wall 2027, DSCR bite Q2-2028 (KB-052).
- ⚠️ **New open item — the issuer's own repricing metric is uninformative and must not be cited** (KB-FLG-048): *"93% of loans that repriced during 2026 are current on their contractual payments **or paid off**"* **fuses the thesis's confirming case with its refuting one.** Still-current means the borrower absorbed the reset; paid off means the loan left via the very channel this thesis is about. The 89% → 93% improvement is equally consistent with the payoff channel working harder. **The split is not disclosed.**
- **K-4 is FURTHER from firing, not closer,** and the evidence is confirming rather than falsifying — the freeze is the opposite of the "increases materially above run-rate" its kill requires.

---

## Q3 fold-in, the rows owed since 10/23 (one line each; the KB row carries the figures)

| Row | What it adds |
|---|---|
| KB-071 / 073 / 096 | The freeze took force 10/1 with no stay. No injunction as of 10/1; merits expected before year-end; later docket entries NOT OBTAINED, the read dropped by Will 2026-11-10 (WQ-477, KB-118); no ruling at reachable sources 11/11 |
| KB-081 / 090 | Provision guidance halved 4/24, then raised 10/23 to $160–170M for FY2026 and $175–225M for FY2027. **The issuer's 2027 provision rise concedes the wall costs more** |
| KB-082 | Refinance is priced off Treasuries plus CRE spread, not high yield. Borrower coupon ~+35bp, about 5% smaller refi on DSCR-limited loans (CREED estimate) |
| KB-086 / 087 / 088 | Criticized + classified +$670M in Q3, first rise across five charted quarter-ends. Par payoffs $1.2B, 35% substandard. NYC ≥50% RR ACL on the criticized book rose to 5.00% |
| KB-089 / 093 | Buyback completed in October; none in Q4; resume expected 2027 (call, secondary) |
| KB-091 | Q3 EPS $0.01 includes a $22M tax benefit; pre-tax −$10M. **Stage 6 headroom is being earned thinly** |
| KB-092 / 094 | Exits run 1–5% of the mark (call, secondary). $34M of Q3 net charge-offs was already reserved. $2.9B of the 2027 reset is NYC ≥50% rent-regulated |
| KB-097 | The 2024 shock is the precedent for this name's tail. Level comparison only; no live analogue claimed |

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
| 3 | Stage 1 or 2 instrumented | ✅ **MET (stage 1).** Rent freeze dated and sized; DSCR fuse ~20 months (Q2-2028, KB-052). Stage 2 CLOSED 8/28 |
| 4 | Every seed figure re-verified at a primary, `Conf` upgraded | 🟠 **PARTIAL — AND NAMED.** ✅ FLG verified the Q2 EDGAR figures, then verified the **2026Q1/Q2 MDRM-level MI3 cells at FFIEC CDR on 2026-10-28** and pulled Q3 on 2026-11-01 (KB-FLG-098). **The ten earlier MI3 rows remain MIRROR-grade**; `MI3_FLG.tsv` marks authority per row |
| 5 | A bidirectional flip surviving contact with 1–3 | ✅ **MET.** Confirm leg re-based 29% → 31.04% (denominator correction, difficulty unchanged) + a second formation-based confirming read added. **Falsify leg UNSET**: the cure-rate candidate was RETIRED 8/28; re-derivation due after the Q3 read (EXIT) |

⚠️ **What v1.0 does NOT mean.** It does not mean the thesis is proven; it means it is **stated, instrumented, falsifiable and sourced to primaries FLG pulled itself.** Two of its legs still carry no registered kill, by design and with reasons. **The single largest residual risk is that the payoff channel stays open indefinitely** — in which case this book resolves quietly and the thesis is simply wrong.

---

## Version log

Rows v0.1 → v1.0.2 rotated verbatim to `archive/THESIS_VERSION_LOG_2026-10-22.md` (crc32 `53455222`).

| Version | Date | Author | Note |
|---|---|---|---|
| v1.0.3 | 2026-10-22 | FLG (desk-sweep fix pass, Will-directed) | Corrections only, direction unchanged: Stage 2 / cure-kill / 29% lines struck to their 8/28 answers; fuse Q2-2028 (KB-052) where Q2-2027 lingered; "grows as a share" replaced by dollars (KB-049); ~11pp merger basis noted on the −143pp (KB-080); provision basis caveat (KB-081); runway arithmetic fixed ($869M ÷ $403.8M TTM). Not yet absorbed: T-08 fired 10/1 (KB-071), docket read (KB-073), budgeted provision (KB-081), refi-cost context (KB-082) — fold in after the Q3 read |
| v1.0.4 | 2026-11-02 | FLG | Freshness corrections from the external audit: Q3 capital, concentration, nonaccrual, delinquency and coverage-preview figures now current; MI3 primary-verification scope corrected. Direction and all thresholds/kill conditions unchanged. Full post-10-Q fold-in and kill-rail re-derivation still owed |
| v1.0.5 | 2026-11-07 | FLG (PROME prome-bf spawn) | Q3 10-Q: FLG-02/03 HIT; Q3 cure/payoff inversion folded in, 'nothing is healing' withdrawn as a flat claim; specific reserve, wall and ≥50% RR figures updated; REGINALD's tie and runway corrections applied at source; five blocks rotated to `archive/THESIS_ROTATED_2026-11-07.md`. Direction and all thresholds/kill conditions unchanged. Rail re-derived 11/07 |
