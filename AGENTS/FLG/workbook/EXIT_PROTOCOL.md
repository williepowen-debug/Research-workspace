# FLG — EXIT PROTOCOL (kill rail)

**Kill rail re-derived: 2026-08-28 (FLG FIRST LIVE SESSION + same-day K-3 resolution on a 13-filing series FLG built itself — every leg re-tested against EDGAR primaries pulled by FLG; K-1 re-cut after a construct-validity defect, K-3's Q2c suspension LIFTED, K-4's mechanism found already FIRED)** *(this in-content stamp is the vintage the Falsification Freshness Sweep dates from — never mtime, PAT-039/044)*
**Author:** DAEDALUS at build · **Re-derived by:** FLG, first live session 2026-08-28 · **Status:** 🟢 **LIVE — no longer build scaffolding.** Re-derived against `THESIS.md` v1.0 and against FLG's own EDGAR primary pull (10-Q Q2-2026, Flagstar Bank N.A., acc 0000910073-26-000068, filed 2026-08-06). Legs still carrying an UNSET kill cell say so and say why.

---

## What this rail is for

The stance at build: *FLG carries the cohort's worst instrumented CRE concentration, credit quality and reserve coverage, and no desk has ever written a thesis on it.* This file names what would prove that stance wrong — **in both directions** — before anyone builds a position on it.

**Channel-kill vs thesis-kill (blueprint §4).** Three channels below are independent enough to die separately. A dead channel is not a dead thesis; say which one died and name the migration path. ⚠️ **But see the Independence note** — this is a single name, so the channels share one antecedent (the multifamily book) more than a multi-name thesis would. Two legs failing on the same root count once.

---

## K-1 — THE COUNTER-THESIS: deleveraging works

**This leg is listed first deliberately.** It is the leg the seed data already partly supports, and a rail that buries its strongest counter-evidence is decoration.

| | |
|---|---|
| **Fires from state** | STANCE-BEARISH (the only state where it means anything) |
| **Instrument** | 🔴 **RE-CUT 2026-08-28.** Leg 1: **multi-family loans HFI in dollars**, 10-Q MD&A multi-family geographical-analysis table (`Total` row) — *not* `total_loans_k`. Leg 2: **non-accrual rate**, 10-Q MD&A "Non-accrual loans to total loans held for investment". Both land in the same filing. `workbook/MI3_FLG.tsv` `loans_qoq_pct`/`total_loans_k`/`total_assets_k` are retained as CONTEXT, not as the kill instrument |
| **Kill condition** | **multi-family loans HFI rising QoQ for 2 consecutive filed quarters** AND non-accrual rate falling across the same 2 quarters |
| **What HEALTHY looks like** | The series is populated and moving: 12 quarters present, QoQ values ranging −10.9% to +12.7% (observed). **A frozen or all-zero column means the instrument died, not that the bank stabilised** (PAT-060) |
| **If it fires** | The run-off stopped while credit improved. The bear framing is not "early" — it is **wrong on mechanism**. Re-derive from scratch; do not re-date and hold |
| **Migration path** | None. This is a **thesis-kill**, not a channel-kill |

**Already-known evidence AGAINST the bear stance, recorded at build:** assets −21.1% and loans −28.8% (2023-09-30 → 2026-06-30), MI3 `v1_pct` 5.28% → 3.65%. The bank has been shrinking for eleven quarters.

🔴 **CONSTRUCT-VALIDITY DEFECT FOUND AND FIXED AT THE PRIMARY, 2026-08-28 — K-1 AS WRITTEN WOULD HAVE FIRED ON THE WRONG BOOK.** The old leg 1 was `loans_qoq_pct > 0` on **total** loans. The 10-Q shows total loans are flat-to-up (**$60,732M → $60,987M, +0.42%** over H1-2026) **while the multi-family book — the entire subject of this thesis — fell −7.08% ($28,983M → $26,931M)**. The difference is **C&I, which grew +22% ($15,217M → $18,563M) on $4.8B of new originations** (KB-FLG-040). ⇒ **`loans_qoq_pct` turning positive measures a MIX SHIFT, not the end of the multi-family run-off.** A kill on total loans would have declared this thesis dead on the strength of commercial-and-industrial growth in a thesis about NYC rent-regulated multifamily. Leg 1 is re-cut onto multi-family dollars, where it is **NOT satisfied and not close** — multifamily has fallen in every observed quarter.

⚠️ **This is the second construct-validity defect found on this rail in eight days, and both were the same shape:** K-2 asked whether a ratio moved on its denominator; K-1 asked whether a book shrank, and was reading a *different, larger* book that contains it. **Both were invisible to a row-level audit and only fell out of a primary pull.** Note the direction of the error: this defect made the kill **EASIER** to fire, so the rail was biased toward retiring a live thesis — the failure mode nobody complains about (`finding_measurement_bias_sign_is_fixed_harm_direction_is_not`).

✅ **DAEDALUS's 2026-08-23 sweep finding is RESOLVED (its ASK, answered).** It flagged that leg 2 (non-accrual rate) had **no registered instrument**, so K-1 rendered `NOT FIRED` when the honest state was `⚠️ UNGRADEABLE`. The instrument existed all along in the 10-Q — it just was not in the cell. Both legs now name a surface in the same filing. **Neither leg was dropped**, so the kill did not get easier by removal (DAEDALUS's own caveat, honoured). ⛔ **And the scanner's "exit-rules lack session counts" flag on this row remains a FALSE POSITIVE — "2 consecutive filed quarters" is a correct count the regex cannot see (PAT-118). Do not "fix" it.**

---

## K-2 — The concentration ratio is a denominator artifact

| | |
|---|---|
| **Fires from state** | STANCE-BEARISH-ON-CONCENTRATION |
| **Instrument** | Call Report CRE composition (construction / multifamily / non-owner-occ NFNR, separately) + total risk-based capital, both as levels |
| **Kill condition** | The **CRE numerator in dollars** is flat-or-falling across ≥3 filed quarters while the ratio rises — i.e. the ratio moved on the denominator |
| **What HEALTHY looks like** | Both numerator and denominator quoted as **dollar levels** beside the ratio. **A ratio published without its two levels cannot test this leg at all** (`finding_spread_metric_blind_to_common_mode`) |
| **If it fires** | Channel-kill on concentration. The credit-quality channel (K-3) survives independently |
| **Migration path** | Drop concentration to a reported-not-scored channel; the thesis migrates onto nonaccrual + coverage |

✅ **K-2 IS RESOLVED — FIRED AND REFUTED, 2026-08-20, before it was ever load-bearing.** REGINALD tested it at the primary (`fb1f68659`, matrix §3b): the CRE numerator fell **−32.2%** ($48.33B → $32.76B) while total risk-based capital held **flat at −2.6%** ($10.27B → $10.00B), so the ratio fell **−143pp in all 11 quarters**. The denominator did not shrink; the artifact is arithmetically impossible on this name. **K-2 is retained, not deleted** — it records a leg that was tested and died, which is the point of a kill rail.

🔴 **What replaces it is stronger, and it is now K-3's job:** channel 1 is **de-risking** (level high, trajectory monotonic down, ~2 quarters from crossing 300%), so the concentration channel is NOT where this thesis lives. **The live signal is COVERAGE** — see K-3, and re-read it as the desk's primary leg rather than its secondary one.

---

## K-3 — Credit quality repairs

| | |
|---|---|
| **Fires from state** | STANCE-BEARISH-ON-CREDIT |
| **Instrument** | 🔴 **PRIMARY: `charge-offs / provision` from Schedule RI-B Part II (RIAD lines, YTD).** Secondary: ACL in dollars; nonaccrual / total loans; ACL / nonaccrual. ⚠️ **The coverage RATIO alone cannot grade this leg** — see the discriminator note below |
| **Kill condition** | ⛔ **STILL UNSET — DELIBERATELY, WITH A REASON.** The `CO/prov < 1.0× ×2 quarters` form was withdrawn 2026-08-20 (fires on 42.8% of ordinary bank-quarters). ✅ **Q2c IS NOW ANSWERED (2026-08-28, at the primary), so the non-accrual-rate SUSPENSION IS LIFTED** — but the answer disqualifies the obvious replacement rather than supplying one. **A named candidate (the CURE RATE) is with REGINALD for cohort base-rating; it is a PROPOSAL, not a gate, and this cell stays UNSET until that run returns.** See § Q2c below |
| **What HEALTHY looks like** | Both ratios present and moving quarter to quarter. **Coverage pinned at an identical value across quarters is a parse failure, not stability** — check the underlying cells |
| **If it fires** | Channel-kill on credit quality — **and since K-2 died 2026-08-20 and channel 1 is de-risking, this is now the LAST live leg: if K-3 fires the thesis has no channel left.** Treat a K-3 fire as a thesis-kill, not a channel-kill |
| **Migration path** | Thesis migrates onto the concentration + rent-regulation mechanism alone — **which is weaker, and say so at the time** |

🔴 **K-3 IS NOW THE DESK'S PRIMARY LEG (promoted 2026-08-20 evening).** REGINALD's §3b re-read: nonaccrual is **past peak and improving** (5.49% [25Q3] → 4.88%), while **ACL has fallen in every one of 8 quarters** ($1.27B [24Q2] → $0.87B) and coverage went **87% [24Q1] → 29%, monotonic**. The reserve is being drawn down **~1.7× faster than the problem book resolves** (ACL −26% vs nonaccrual −15% off respective peaks), against a still-**$3.0B** nonaccrual book.

⚠️ **THE DISCRIMINATOR IS `CO / PROVISION` — NOT THE RATIO, AND NOT THE ACL LEVEL** *(corrected 2026-08-20 evening, REGINALD's second pass; my first fix — "add ACL in dollars" — was still not sufficient).* The ACL roll-forward at Schedule RI-B Part II answers it directly (`6dfd8ed53`, identity ties to the dollar): begin $1,029,999K + provision $15,923K − charge-offs $232,410K + recoveries $55,488K = $869,000K. **The drawdown is NEITHER release NOR clean disposition — provision is positive in every quarter, so nothing was reversed into income, but the reserve is eaten by realized losses and NOT replenished.** CO/prov by year: FY2023 **0.3× (building)** · FY2024 0.8× · FY2025 **2.4× (draining)** · 2026 H1 ×2 **🔴 14.6×**. Provisioning −97.1% from FY2024 against charge-offs near half a billion a year ⇒ **runway ≈2.15 years on a TTM basis** *(corrected from ~1.9yr — H1×2 overstated charge-offs ~15%; TTM $403,816K, not $464,820K)*** vs a $2,988M nonaccrual book.

**Why the ratio alone fails:** coverage can move on the numerator (reserve build/burn) or the denominator (book resolving), and ACL-in-dollars still cannot separate *consumed-by-loss* from *released-into-income*. **Only provision vs charge-offs does.** A rail on the ratio cannot tell the three cases apart; a rail on CO/provision can.

✅ **BASE-RATED 2026-08-20 — 168 bank-quarters, 14 banks × 12 quarters, all at the primary** (`AGENTS/REGINALD/workbook/ACL_ROLLFORWARD_COHORT.tsv`, `84bd8b485`; every figure below re-derived first-hand at FLG and reproduces). **14.6× IS remarkable and the line STANDS, now with a denominator:** cohort median CO/prov **1.00×** (banks provision almost exactly what they charge off), p75 1.31 · p90 1.63 · p95 2.00. **The entire ≥10× tail across 168 bank-quarters is FLG's own two 2026 quarters — 74.7× [Q1] and 14.6× [Q2]. No other bank reaches 10× in three years.** True releases (provision ≤ 0) are 2/168 = 1.2%, ZION only — FLG never released.

🔴 **BUT THE SAME BASE RATE KILLED THIS LEG'S KILL CONDITION, AND THAT IS THE MORE IMPORTANT RESULT.**

`CO/prov < 1.0× ×2 quarters` sits **exactly on the cohort median**: single quarter **50.0%**, two consecutive **42.8% of all adjacent pairs cohort-wide** (re-derived: 65/152). ⇒ **a falsifier firing on ~43% of ordinary bank behaviour kills the thesis on normal provisioning, not on repair.** The receipt is FLG's own history: it satisfied that condition in **six consecutive quarters (2023Q3→2024Q4, 0.15× → 0.79×)** — continuously true for eighteen months *before the pattern the thesis is about had begun*.

**Raising the level makes it worse, not better** (≤1.31× → 64.5%, ≤2.00× → 93.4%), so the FORM is wrong, not the level. **Four further candidate forms were base-rated at FLG before proposing any of them, and all four died:**

| Candidate form | Cohort base rate | Verdict |
|---|---:|---|
| `CO/prov < 1.0×` ×2 consecutive *(the withdrawn one)* | **42.8%** | ❌ |
| `ACL$ rises QoQ` ×2 consecutive | **46.4%** | ❌ |
| `ACL$ above its level 4 quarters ago` (YoY build) | **58.0%** | ❌ |
| `ACL$ ≥5% above its level 4 quarters ago` | **42.9%** | ❌ |
| `CO/prov < 1.0×` sustained 5 quarters | **27.3%** | ❌ still common, **and 15 months of latency** |

⇒ **STRUCTURAL FINDING: no threshold on CO/provision — and no short-window "reserves improved" condition on any of these measures — is a usable falsifier for this thesis.** *"CO/prov returns to normal"* is not evidence of repair; it is evidence of **not currently being extreme**, which is every bank's default state. The measure is excellent as a **state descriptor** (it found the 99th percentile) and bad as a **kill**.

**REQUIREMENT a replacement must meet before it goes in the cell above** — all four, and base-rated by a second reader (REGINALD has the dataset and has offered the run):
1. **Cohort base rate materially below ~10%** — it must discriminate, not describe the population's default.
2. **Not satisfied by FLG's current trailing window** (no threshold already breached at write time).
3. **Low spurious-fire count in FLG's own history** — the six-quarter receipt is the test to beat.
4. **Latency ≤ 2–3 filed quarters** — a kill that takes 15 months to fire cannot protect a position.

**Design direction (not a proposal — FLG's call at its first live session):** the thesis is about a **STOCK depleting with finite runway**, so a **FLOW ratio returning to its own median cannot be the evidence the stock recovered.** The likely instrument is the runway itself (ACL ÷ annualised charge-offs) or coverage against nonaccrual — **both blocked today**, the first because `RIAD` is YTD and needs a validated per-quarter charge-off series, the second because Q2c has not split cure from charge-off.

⚠️ **An UNSET cell with a stated reason is the honest state and is better than a number.** A falsifier that fires on 43% of normal behaviour does not protect a thesis — it retires one at random.

*Seed reads: nonaccrual 4.88% vs cohort median ~0.89% (implied by REGINALD's "5.5× the median"); coverage 29%. MIRROR-grade — re-verified at first live session 2026-08-28, see below.*

---

### ✅ Q2c ANSWERED AT THE PRIMARY — 2026-08-28, FLG first live session

DAEDALUS suspended every non-accrual-rate leg on 2026-08-20 pending Q2c, on the reasoning that *"a rate falling by charge-off would fire the kill on its own losses."* **The 10-Q's non-accrual roll-forward answers it directly** (Q2-2026, six months ended 2026-06-30 — KB-FLG-029):

| Line | $M | Share of outflow |
|---|---:|---:|
| Balance 2025-12-31 | 2,975 | |
| **New non-accrual (formation)** | **+780** | |
| Charge-offs | −100 | **10.5%** |
| Transferred to other assets | −4 | 0.4% |
| **Loan payoffs, dispositions, paydowns** | **−836** | **🔴 87.5%** |
| **Restored to performing (CURE)** | **−15** | **🔴 1.6%** |
| Balance 2026-06-30 | **2,800** | |

**The rate is falling by PAYOFF. Not by charge-off (10.5%), and emphatically not by cure (1.6%).** ⇒ **The suspension is LIFTED** — a non-accrual leg does not fire the kill on its own losses, because losses are not what is moving the number.

🔴 **But the answer is a THIRD case again, and it re-frames the thesis rather than resolving it.** Q2b found the ACL drawdown was neither release nor disposition; Q2c now finds the non-accrual decline is neither charge-off nor cure. **The only working exit from a $2.8B non-accrual book is refinancing or sale into a functioning market — and that channel is exogenous to the bank.** Cures, the one exit that means the borrower recovered, are 1.6%. **Nothing here is healing; it is being handed off.** ⚠️ And gross formation of **$780M replaced 81.7% of the outflow** (KB-FLG-030), so the net −5.9% headline overstates the drain by ~4.5×.

### 🔴 RESOLVED SAME SESSION — THE CANDIDATE IS RETIRED, ON TWO INDEPENDENT GROUNDS

**① REGINALD's cohort pilot (n=3 at the primary, `180ca0157`): the cohort base rate CANNOT BE BUILT.** WAL, EGBN and CFG all disclose ACL roll-forwards, non-accrual balances, aging and NCO tables — and **none discloses a non-accrual roll-forward with a separate cure line.** The `returned to accrual` flow is an **FR Y-14Q Schedule H** item (non-public), not a GAAP 10-Q footnote; FLG discloses it as a **NYCB-legacy enhanced-disclosure choice**. OZK is structurally out entirely (deregistered SEC periodic reporting in 2017). ⚠️ **REGINALD's strongest point is not the sample size — it is composition:** the names that voluntarily disclose are the enhanced-disclosure large caps, so any rate built from them is *a self-selected subset median on the wrong cohort*, which is the same composition defect that killed the earlier five forms. **A bigger pilot would not fix it.** Retire on the structural argument, not on n.

**② FLG's own history kills it too — and I could have known before proposing it.** Having built `workbook/NONACCRUAL_FLOW.tsv` (13 filings, identity ties 13/13) the same session, requirement 3 is now testable at this desk:

| half | 23H1 | 23H2 | 24H1 | 24H2 | 25H1 | 25H2 | 26H1 |
|---|---:|---:|---:|---:|---:|---:|---:|
| cure share of outflow | **59.5%** | **13.1%** | 2.9% | 6.1% | **16.1%** | 1.8% | 1.6% |

**Single-half ≥10% fires 3 of 7 (43%). Two consecutive halves fires once — 2023H1+2023H2.** ⇒ **Requirement 3 FAILS.** ⛔ **And I proposed this form to REGINALD BEFORE base-rating it, which is precisely the order this charter forbids.** The rule I broke is my own.

**③ REGINALD's offered alternative also fails, on data it did not have.** The suggested single-name-persistence form — *"cure-share <5% for 2 consecutive semi-annuals"* — is **ALREADY SATISFIED**: 2025H2 **1.8%** and 2026H1 **1.6%**. That breaches requirement 2 (no threshold already met at write time) on the day it was proposed. **And it points the wrong way**: a *low* cure share is thesis-**CONFIRMING**, so it cannot serve as K-3's kill, which must fire when credit **repairs**. Recorded so nobody re-derives it.

### 🔑 WHY SIX CANDIDATES HAVE NOW DIED — the requirement, not the candidates

> **Requirement 3 is MIS-SPECIFIED for a bank whose regime changed mid-sample.** "Low spurious-fire count in the name's own history" assumes one regime throughout. FLG's history contains a break — non-accrual **$798M [24Q1] → $1,942M [24Q2], +143%** — and in 2023 the bank had a $233M problem book curing at **59.5%**. **A kill built to detect credit repair SHOULD fire in 2023, because in 2023 this bank genuinely was repairing.** Counting that as a spurious fire scores a **correct positive as a false positive**.

⇒ **No repair-detecting kill can ever pass requirement 3 for a bank that used to be healthy.** The run of six failures is a property of the **test**, not of the candidates — and every previous post-mortem, mine included, blamed the candidate.

**The fix, and its own limit.** Evaluate requirement 3 on the **post-regime-break window only, with the break dated and the exclusion stated**. On FLG's post-24Q2 window (4 halves: 6.1 / 16.1 / 1.8 / 1.6) the ≥10%-two-consecutive form fires **zero** times and would **pass**. ⛔ **But n=4 halves is too thin to register a kill on, and requirement 1 is now known to be unbuildable for this instrument** — so passing a re-specified requirement 3 is not sufficient. **K-3's cell stays UNSET.** Routed to REGINALD as a **framework-level** finding: it applies to every name in the matrix whose regime broke, not to FLG alone.

**What replaces the gate, and it is better than a gate nobody can calibrate:** cure share is now a **standing observable** on `NONACCRUAL_FLOW.tsv`, refreshed every filing, with three years of history behind it. **A watched series with a known trend beats an uncalibrated threshold** — and if cure share ever returns to double digits for two halves, that is visible on the ledger at the next print whether or not a gate exists.

---

*(Superseded proposal, retained so it is not re-derived — this was the candidate before the two tests above killed it:)*

**⇒ CANDIDATE KILL, ROUTED TO REGINALD FOR COHORT BASE-RATING (not registered here):**

> **`Restored to performing` ≥ 10% of total non-accrual outflow for 2 consecutive semi-annual periods.**

Why this form and not another: it is a **positively-measured instrument** (PAT-060 — healthy = the line is populated and rising, so instrument-death is distinguishable from thesis-survival); it measures the **STOCK genuinely repairing** rather than a **FLOW returning to its median**, which is the structural finding that killed all five earlier candidates; and at **1.6% today it is nowhere near breached** (requirement 2). ⚠️ **It is UNVERIFIED against requirements 1, 3 and 4** — FLG cannot base-rate it alone, because the non-accrual roll-forward is a **10-Q disclosure, not a Call Report cell**, so a 14-bank cohort rate needs 14 banks × N filings parsed. REGINALD has the cohort and offered the run. **Until that returns, the cell above stays UNSET, and an UNSET cell with a stated reason remains better than a number.**

---

## K-4 — The mechanism itself is wrong

| | |
|---|---|
| **Fires from state** | ANY |
| **Instrument** | NYC RGB published rent-guideline orders + FLG multifamily nonaccrual trend |
| **Kill condition** | RGB grants rent increases materially above the recent run-rate for 2 consecutive annual votes **AND** FLG multifamily nonaccrual falls across the same window |
| **What HEALTHY looks like** | RGB publishes an order annually; a missing order means the vote slipped, not that rents were frozen |
| **If it fires** | The rent-regulation transmission is severed. **This kills the reason FLG is a separate desk at all** — escalate to PROME for a scope review, do not quietly re-scope |
| **Migration path** | None that keeps this desk distinct from REGINALD's cohort view |

⚠️ **Compound-gate audit on K-4** (blueprint §3, PAT-072): two legs, `AND`-joined. **Not base-rated — admitted, not hidden.** The RGB series is annual, so this gate can fire at most once per year and needs ≥2 years to satisfy.

🔴 **2026-08-28 — THE MECHANISM FIRED, IN THE OPPOSITE DIRECTION, AND THE WAKE REGISTER MISSED IT.** At its first live session FLG found in the 10-Q (KB-FLG-032) that the **NYC Rent Guidelines Board approved a RENT FREEZE on rent-regulated NYC multi-family buildings in JUNE 2026, effective OCTOBER 2026** — and that FLG had **already booked a Q2-2026 provision increase for it**: the quarter's provision rose $18M QoQ *"primarily due to credit adjustments driven by recent regulatory action in New York City to freeze rents on multifamily properties."*

**K-4 is therefore further from firing than at build, not closer.** Its kill needs increases *materially above* the run-rate; the RGB delivered **zero**. The leg is **NOT FIRED**, and the evidence is **confirming for the thesis**, not falsifying.

⚠️ **The process failure is the finding, and it is worse than the leg being unbase-rated.** `TRIGGERS.tsv` T-06 carried the RGB vote as `[EST] 2027-05-03`, so **an event that had already happened rendered as PENDING**, and nothing in the register could distinguish the two states (`finding_dated_carry_item_has_no_expiry_check`). **A desk whose entire reason to exist is the rent-regulation mechanism was ~10 weeks blind to that mechanism firing, while holding a correctly-formatted, in-date wake row pointed at it.** T-06 is corrected and re-scoped to the 2027 cycle; the fired 2026 leg is now **T-08 (effective 2026-10-01, HARD)**; the transmission lag is **T-09 (Q2-2027)**.

⏱️ **The fuse, and why a quiet Q4 proves nothing.** FLG re-tests DSCR on borrower financials received *"generally during the second calendar quarter"* (KB-FLG-037). A freeze effective October 2026 therefore first reaches **formation** in the **Q2-2027** review cycle — a **~12-month fuse**. Expect provision *commentary* at Q3/Q4-2026 and **not** formation. ⛔ **Anyone reading two quiet quarters as "the freeze did not bite" is reading the fuse, not the charge** — write that on any surface that cites this leg.

**Base-rating status:** still **NOT base-rated**, now for a stated reason rather than an open to-do. The RGB order series is annual and administrative; a "materially above run-rate" leg needs a numeric comparator before it can be graded at all (DAEDALUS's 2026-08-23 §3 finding, unresolved and carried). **Retirement is not yet right** — the mechanism just demonstrated it is live and market-moving. **Carried to the next session with the quantification owed.**

---

## BIDIRECTIONAL FLIP — the cleanest single read each way

*Blueprint §4: name the one thing that falsifies the stance in BOTH directions, testable at the next data release.*

**Next testable release: Q3-2026 Call Report, ~2026-11-14** (RULE-anchored: quarter-end + 45d).

| Direction | The single read | Threshold |
|---|---|---|
| **Confirms the stance** | Coverage keeps falling — **regardless of the non-accrual direction** | coverage **< 31.04%** at the filing *(deliberately SINGLE-CLAUSE — see the free-clause note)* ⚠️ **RE-BASED 2026-08-28 from 29% to 31.04%: this is a DENOMINATOR CORRECTION, not a loosened threshold.** The seed's 29% used the Call Report's $2,988M non-accrual; the primary reads ACL $869M / non-accrual HFI $2,800M = 31.04% (KB-FLG-028). Both endpoints move together, so the leg's difficulty is unchanged — but a reader comparing the two numbers without the basis would see a threshold that got easier. **Grade this leg on the 10-Q basis only** |
| **Falsifies the stance** | ⛔ **STILL UNSET pending the K-3 requirement.** The `CO/prov < 1.0×` form was withdrawn after base-rating (42.8% of ordinary bank behaviour); the **cure-rate candidate is with REGINALD** and is not a gate until its cohort base rate returns | — |
| **Second confirming read, added 2026-08-28** | **Gross non-accrual FORMATION**, not the net balance — the net hid $780M of H1 formation behind a −5.9% headline | H1-2027 formation **≥ $780M** (H1-2026 baseline). ⚠️ **H1-vs-H1 only — formation is Q2-seasonal (KB-FLG-037), so an H2 or annualised comparison is invalid by construction** |

⚠️ **FREE-CLAUSE FINDING, 2026-08-20 — the mirror of the unsatisfiable-AND fixed earlier the same evening, on this same rail.** REGINALD base-rated a candidate CONFIRM conjunction *jointly*: `ACL fell QoQ AND CO/prov ≥ X`. **At every cut the joint rate EQUALS the ratio leg exactly** (≥2.0×: both 6.5%; ≥5.0×: both 3.2%) — every bank-quarter above 2.0× also had a falling ACL, so **the "ACL fell" clause never excludes anything.** That is a **single-clause gate wearing a compound disguise**: it reads as more rigorous and is not. **PAT-072 is a gate that can never FIRE; this is a leg that can never BIND** — same family, same fix, and exactly why the check must be JOINT rather than two marginal base rates.

⚠️ **CORRECTED 2026-08-20 evening — the original confirm-leg was a compound gate that could not fire on the actual signal.** It read *"coverage < 29% **AND** nonaccrual > 4.88%"*, requiring nonaccruals to RISE. REGINALD's §3b then measured nonaccruals **past peak and falling** — so the observed pattern (reserve drawn down while the problem book slowly resolves) would have satisfied the coverage leg and **failed the gate**, exactly PAT-072: legs that are individually reasonable and jointly unsatisfiable in the only state that matters. **The `AND` was doing no work except suppressing the fire.** Both legs are now single-clause and the ACL-dollars discriminator carries the nuance the conjunction was pretending to.

**Both readings come off ONE filing, and neither needs an intervening judgment.** That is the property to preserve when this rail is re-derived.

---

## Standing discipline on this rail

- **Every `AND` above states the state it fires FROM.** A kill that cannot fire is indistinguishable from a thesis that is still true — and unlike a broken deploy gate, nobody ever complains about it (blueprint §4).
- **"Sustained" carries a count everywhere it appears** — here always in *filed quarters*, never in days, because the instrument is quarterly. A day-count on a quarterly instrument is untrippable by construction.
- **No leg above was already satisfied at write time.** Verified at build: coverage 29% (not >50%), `loans_qoq_pct` +0.9% at 2026-06-30 — ⚠️ **one quarter positive already.** K-1 needs two consecutive; it is **one quarter from firing.** This is the single most important line in this file.
- **Executability (`finding_executability_is_a_separate_audit_axis`):** every leg grades off a quarterly filing available to any reader at a public source. No leg needs an instrument that quotes faster than the claim it grades.

---

## Re-derivation log

| Date | By | What changed |
|---|---|---|
| 2026-08-20 | DAEDALUS (build) | Rail authored against seed evidence. PROVISIONAL — no thesis exists yet. K-1 flagged one quarter from firing. |
| 2026-08-20 evening | DAEDALUS (post-build) | **K-2 tested at the primary by REGINALD (`fb1f68659`, matrix §3b) and REFUTED** — CRE numerator −32.2%, capital flat −2.6%, ratio −143pp across all 11 quarters. K-2 retained-and-marked, not deleted. **K-3 promoted to primary leg** with a new ACL-in-dollars instrument. **Bidirectional confirm-leg corrected** — its `AND` was jointly unsatisfiable against the pattern REGINALD identified (PAT-072, in a rail I authored). Rail re-stamped. |
| 2026-08-20 evening (2nd) | DAEDALUS, on REGINALD's unprompted Q2b answer | **K-3's instrument corrected AGAIN, hours after the first correction.** My first fix added ACL-in-dollars; REGINALD's roll-forward showed that is still insufficient — **the discriminator is `CO / provision`**, because neither the ratio nor the ACL level separates consumed-by-loss from released-into-income. Kill condition re-cut to CO/prov < 1.0× ×2 quarters; **nonaccrual-rate legs SUSPENDED** pending Q2c (a rate falling by charge-off would fire the kill on its own losses); falsify-leg re-pointed to "provisioning restarts". ⛔ No threshold registered on 14.6× — no base rate exists (Q2d). |
| **2026-08-28** | **FLG, FIRST LIVE SESSION** | **Rail re-derived against FLG's own EDGAR primary pull** (10-Q Q2-2026, acc 0000910073-26-000068). **K-1 RE-CUT** — construct-validity defect: leg 1 measured *total* loans (+0.42% H1, rising on +22% C&I growth) when the thesis is about *multi-family* (−7.08% H1); the kill would have fired on a mix shift. Leg 2's missing instrument (DAEDALUS 8/23) supplied from the same filing; **no leg dropped**. **K-3 — Q2c ANSWERED, non-accrual suspension LIFTED**: the rate falls by payoff (87.5%), not charge-off (10.5%) or cure (1.6%); cure-rate candidate routed to REGINALD, cell stays UNSET. **K-4 — mechanism FOUND ALREADY FIRED**: RGB rent freeze approved 2026-06, effective 2026-10, provision already booked; leg is further from firing and the evidence is confirming, but T-06 had rendered a fired event as pending. **Bidirectional confirm-leg re-based** 29% → 31.04% (denominator correction, not a loosened threshold) and a second formation-based confirming read added. Capital denominator **$10,003M verified at the primary — REGINALD's $10.00B reproduces exactly.** |
