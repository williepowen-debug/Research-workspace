# FLG — EXIT PROTOCOL (kill rail)

**Kill rail re-derived: 2026-08-20 (evening — re-stamped after K-2 was tested and REFUTED at the primary; see K-2 and the re-derivation log)** *(this in-content stamp is the vintage the Falsification Freshness Sweep dates from — never mtime, PAT-039/044)*
**Author:** DAEDALUS at build · **Status:** ⚠️ **PROVISIONAL — authored against the SEED, not against a thesis.** `THESIS.md` is v0.1 (a skeleton of open questions), so these legs kill a *stance*, not a finished thesis. **FLG re-derives this rail at first live session and re-stamps it.** Until then, cite it as build scaffolding.

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
| **Instrument** | `workbook/MI3_FLG.tsv` → `loans_qoq_pct`, `total_loans_k`, `total_assets_k` (FFIEC Call Report, RSSD 694904) |
| **Kill condition** | `loans_qoq_pct > 0` for **2 consecutive filed quarters** AND nonaccrual rate falling across the same 2 quarters |
| **What HEALTHY looks like** | The series is populated and moving: 12 quarters present, QoQ values ranging −10.9% to +12.7% (observed). **A frozen or all-zero column means the instrument died, not that the bank stabilised** (PAT-060) |
| **If it fires** | The run-off stopped while credit improved. The bear framing is not "early" — it is **wrong on mechanism**. Re-derive from scratch; do not re-date and hold |
| **Migration path** | None. This is a **thesis-kill**, not a channel-kill |

**Already-known evidence AGAINST the bear stance, recorded at build:** assets −21.1% and loans −28.8% (2023-09-30 → 2026-06-30), MI3 `v1_pct` 5.28% → 3.65%. The bank has been shrinking for eleven quarters. **This leg is close to live, not hypothetical.**

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
| **Kill condition** | ⛔ **UNSET — DELIBERATELY, WITH A REASON. Do not fill this cell with a number until the requirement below is met.** The previous condition (`CO/prov < 1.0× ×2 quarters`) was **withdrawn 2026-08-20 after base-rating**, and no replacement survived testing. Nonaccrual-rate legs remain SUSPENDED pending THESIS Q2c |
| **What HEALTHY looks like** | Both ratios present and moving quarter to quarter. **Coverage pinned at an identical value across quarters is a parse failure, not stability** — check the underlying cells |
| **If it fires** | Channel-kill on credit quality — **and since K-2 died 2026-08-20 and channel 1 is de-risking, this is now the LAST live leg: if K-3 fires the thesis has no channel left.** Treat a K-3 fire as a thesis-kill, not a channel-kill |
| **Migration path** | Thesis migrates onto the concentration + rent-regulation mechanism alone — **which is weaker, and say so at the time** |

🔴 **K-3 IS NOW THE DESK'S PRIMARY LEG (promoted 2026-08-20 evening).** REGINALD's §3b re-read: nonaccrual is **past peak and improving** (5.49% [25Q3] → 4.88%), while **ACL has fallen in every one of 8 quarters** ($1.27B [24Q2] → $0.87B) and coverage went **87% [24Q1] → 29%, monotonic**. The reserve is being drawn down **~1.7× faster than the problem book resolves** (ACL −26% vs nonaccrual −15% off respective peaks), against a still-**$3.0B** nonaccrual book.

⚠️ **THE DISCRIMINATOR IS `CO / PROVISION` — NOT THE RATIO, AND NOT THE ACL LEVEL** *(corrected 2026-08-20 evening, REGINALD's second pass; my first fix — "add ACL in dollars" — was still not sufficient).* The ACL roll-forward at Schedule RI-B Part II answers it directly (`6dfd8ed53`, identity ties to the dollar): begin $1,029,999K + provision $15,923K − charge-offs $232,410K + recoveries $55,488K = $869,000K. **The drawdown is NEITHER release NOR clean disposition — provision is positive in every quarter, so nothing was reversed into income, but the reserve is eaten by realized losses and NOT replenished.** CO/prov by year: FY2023 **0.3× (building)** · FY2024 0.8× · FY2025 **2.4× (draining)** · 2026 H1 ×2 **🔴 14.6×**. Provisioning −97.1% from FY2024 against charge-offs near half a billion a year ⇒ **~1.9 years of reserve runway** vs a $2,988M nonaccrual book.

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

*Seed reads: nonaccrual 4.88% vs cohort median ~0.89% (implied by REGINALD's "5.5× the median"); coverage 29%. MIRROR-grade — re-verify at first live session.*

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

⚠️ **Compound-gate audit on K-4** (blueprint §3, PAT-072): two legs, `AND`-joined. **Not base-rated — admitted, not hidden.** The RGB series is annual, so this gate can fire at most once per year and needs ≥2 years to satisfy. **Base-rate it at first live session or retire it**; an un-base-rated compound kill is the exact shape that fails silently.

---

## BIDIRECTIONAL FLIP — the cleanest single read each way

*Blueprint §4: name the one thing that falsifies the stance in BOTH directions, testable at the next data release.*

**Next testable release: Q3-2026 Call Report, ~2026-11-14** (RULE-anchored: quarter-end + 45d).

| Direction | The single read | Threshold |
|---|---|---|
| **Confirms the stance** | Coverage keeps falling — **regardless of the nonaccrual direction** | coverage **< 29%** at the filing *(deliberately SINGLE-CLAUSE — see the free-clause note)* |
| **Falsifies the stance** | ⛔ **UNSET pending the K-3 requirement** — the `CO/prov < 1.0×` form was withdrawn after base-rating (42.8% of ordinary bank behaviour) | — |

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
| *(next)* | FLG, first live session | **Re-derive against `THESIS.md` v1.0, re-verify every seed figure at a primary, re-stamp the date above.** |
