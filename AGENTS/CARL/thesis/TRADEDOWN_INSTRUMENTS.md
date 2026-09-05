# K-Shape Trade-Down — Registered Instrument Set (V8 leg)

**Created 2026-09-05, Will-directed re-base.** ⛔ **NOT a boot-read surface** — referenced from `thesis/THESIS.md` V8 and `STATUS.md`, read at grade time only. Canonical for *which series resolve the trade-down leg*; THESIS owns the score.

---

## Why this file exists — the leg it replaces was measured with the wrong instrument, in the wrong direction

**RETIRED 2026-09-05: the EMPLOYMENT proxy.** From 2026-08-10 the trade-down leg was evidenced by **`USTRADE` (retail-trade payrolls)** and **`CES4245100001` (gen. merch / warehouse clubs & supercenters)**, on the reading *"retail trade −19K, club stores −21K… the trade-down destination is shedding staff."*

**Two independent defects, either one fatal:**
1. **THE SIGN WAS BACKWARDS.** If squeezed consumers trade **down into** discount/club retail, that destination gets **busier** — more trips, plausibly **more** headcount. A staff shed is not what the mechanism predicts; **it is closer to the opposite.** The leg read a decline as confirmation of a mechanism that predicts an increase.
2. **HEADCOUNT DOES NOT MEASURE CONSUMER STRESS.** Retailer staffing is set by store openings, wage floors, automation and margin plans — not by whether customers are squeezed. It is LABOR's series answering a question LABOR was not asked. *(Scope note: CARL reached into another desk's data for a proxy when the mechanism is measurable on CARL's own surface. Borrowed corroboration is one witness, re-labelled.)*

*(Both series have since revised positive in 5-6 of the last 6 months, so the evidence also failed — but **the spec was wrong before the data moved**, and that is the part worth remembering. `[[finding_threshold_spec_fails_before_world]]`.)*

---

## The mechanism, stated so it can be falsified

> Bottom-60 households under multi-vector cost squeeze **shift spending INTO discount/club/supercenter channels, and within those channels buy SMALLER REAL BASKETS MORE OFTEN.**

⇒ **THE SIGNATURE IS: TRIPS UP **AND** REAL BASKET DOWN.**

| observed | reading |
|---|---|
| trips ↑ **and real basket ↓** | 🔴 **trade-down / stress — the registered signature** |
| trips ↑ and real basket ↑ | 🟢 healthy share gain — **NOT stress**; the leg does not fire |
| trips ↓ | 🟢 no trade-down into this channel; leg fails |

⛔ **DEFLATE THE TICKET, ALWAYS.** A nominal ticket can print **positive** while the real basket is **negative** — Q2-2026 is exactly that case (+1.5% nominal, **−1.11% real**). **The nominal number carries the opposite sign to the mechanism.** Reading it undeflated is the same error class as reading a sector payroll print without asking what it measures.

---

## TIER 1 — aggregate, monthly, published (CHEAP · TIMELY · **MASKED BY CONSTRUCTION**)

| # | Instrument | Series | Mechanism predicts |
|---|---|---|---|
| T1-a | **Food AT home vs AWAY from home, REAL** | `RSDBS` ÷ `CUSR0000SAF11` vs `RSFSDP` ÷ `CUSR0000SEFV` | grocery **>** restaurants (substitution into the cheaper channel) |
| T1-b | **General-merchandise share of retail** | `RSGMS` ÷ `RSXFS` | share **RISING** |
| T1-c | **Discretionary apparel, real** | `RSCCAS` ÷ `CPIAPPSL` | **falling** (deferral category) |

**Reading 2026-09-05 [obs 2026-07-01] — ALL THREE AGAINST THE LEG:**
- **T1-a: grocery real −1.70% vs restaurants real +1.63% ⇒ spread −3.33pp. WRONG DIRECTION**, and by a wide margin.
- **T1-b: GM share 12.237% (Jul-25) → 12.084% (Jul-26), FALLING** ~15bps YoY *(though off a 11.963% June low)*.
- **T1-c: apparel real +1.18% — GROWING**, not deferred.

⚠️ **`MRTSSM45291USS` (Warehouse Clubs & Superstores) — the single most on-point series — is DISCONTINUED, last obs 2025-02-01.** The best-fitting instrument for this leg no longer publishes. `RSGMS` is the surviving proxy and it is broader.

⛔ **TIER 1 CANNOT CONFIRM THIS LEG AND MUST NEVER BE USED TO.** These are aggregates dominated by the top-40% who do most of the spending — CARL's own masking framework says so. **Tier 1 is a DISCONFIRMATION tripwire only.**

## TIER 2 — cohort-resolved, quarterly, company-reported (WHERE THE MECHANISM IS ACTUALLY VISIBLE)

| # | Instrument | Source | Note |
|---|---|---|---|
| T2-a | **DG comps decomposed: traffic vs ticket** | DG quarterly **earnings release / call** | ⚠️ **NOT in the 10-Q** — the split lives in the release and call. Register the call as the resolving document. |
| T2-b | **DLTR / WMT same-store traffic vs ticket** | quarterly releases | WMT adds the income-cohort commentary |
| T2-c | **Issuer language on the low/fixed-income cohort** | 10-Q MD&A + call | qualitative; corroborates, never resolves |

**Reading 2026-09-05 — DG Q2 FY2026, quarter ended 2026-07-31 (rel 8/27).**

# ⛔ THIS OBSERVATION IS RETROSPECTIVE AND IN-SAMPLE. IT IS NOT EVIDENCE FOR THE LEG.

**The signature above (`trips↑ AND real basket↓`) was constructed AFTER seeing this result.** The DG Q2 print is what motivated the re-base, and it is the dataset the rule was fitted on. **A same-dataset construction is not a test.** It cannot count as a confirming observation, and it does not make the leg supported. *(Codex review 2026-09-05, relayed via PROME — correct, and it is the same discipline I applied to the employment proxy, which I failed to apply to my own replacement. `[[finding_a_correction_pass_is_unreviewed_work]]`.)*

⚠️ **THREE SEPARATE WEAKNESSES, STACKED — none of them individually fatal, together decisive:**
1. **IN-SAMPLE** — rule built on this observation (above).
2. **THE SPLIT IS NOT PRIMARY** — traffic/ticket is press; the 10-Q does not carry it. Unconfirmed at the call.
3. **THE DEFLATOR IS A PROXY, AND I MIS-NAMED THE OUTPUT.** Food-at-home CPI against a **whole-company** ticket yields an **INFLATION-ADJUSTED TICKET PROXY**, *not* a literal real basket and *not* units-per-basket. DG's mix is not food-at-home. **Corrected terminology throughout: say "inflation-adjusted ticket (food-at-home CPI basis)" and never "real basket" or "units."**

**The figures, so they are on the record with their status attached:**
- **PRIMARY-VERIFIED (SEC 10-Q `dg-20260731x10q.htm`):** net sales **$11,290,380K, +5.2%**; **same-store sales +3.5%**.
- **PRESS, NOT PRIMARY — flagged:** traffic **+2.0%**, nominal ticket **+1.5%**; *5th consecutive quarter of traffic growth.* ⚠️ **The 10-Q does NOT carry the split.** It is arithmetically consistent with the primary comp (2.0 + 1.5 = **3.5** ✓), which corroborates but does not substitute for the primary. **Confirm at the call transcript before this figure grades anything.**
- **DERIVED — inflation-adjusted ticket proxy** = +1.5% − 2.61% (`CUSR0000SAF11` food-at-home YoY, Jul-26) = **−1.11pp**. ⛔ **Read as: the ticket grew 1.11pp SLOWER than food-at-home inflation.** It is **NOT** a measured real basket and **NOT** a unit count. Basis: whole-company ticket vs a food-only deflator — approximate by construction.
- ⇒ trips +2.0% AND inflation-adjusted ticket −1.11pp ⇒ the signature's **shape** is present — **IN-SAMPLE, so this is the rule's DESCRIPTION of its own training case, not a fire.**
- **Issuer's own words (10-Q MD&A, primary):** *"Our customers continue to feel constrained in the current macroeconomic environment and to experience elevated expenses that generally comprise a large portion of their household budgets, such as rent, healthcare, energy and fuel prices."* — **that is CARL's multi-vector cost-squeeze mechanism, stated by the counterparty**, and *"The majority of our customers are value-conscious, and many have low and/or fixed incomes."*

---

## ⛔ The anti-escape-hatch rule (the most important line in this file)

**"Tier 1 is masked" must NOT become an unfalsifiable defence.** If every aggregate reading that cuts against the leg is dismissed as masking, the leg can never die, and it stops being a claim.

**Therefore the masking defence is admissible ONLY while Tier 2 still shows the signature.** Concretely:

- **LEG DIES** if **T2-a real ticket turns POSITIVE for 2 consecutive quarters**, OR **DG traffic turns NEGATIVE for 2 consecutive quarters** — regardless of what Tier 1 says. *(Single-quarter discipline applies in both directions.)*
- **LEG ALSO DIES** if Tier 1 stays against it **AND** Tier 2 stops showing the signature — i.e. both tiers agree against.
- **Tier 1 turning FOR the leg is a strengthening, not a confirmation** — it is the masked instrument.
- **⛔ CURRENT STATE, CORRECTED 2026-09-05 AFTER THE CODEX REVIEW — AND IT IS WEAKER THAN I FIRST WROTE.** I said *"the leg survives on Tier 2 alone,"* which implied Tier 2 was supporting evidence. **It is not. Tier 2 has ZERO out-of-sample observations.** ⇒ **Tier 1 is 3-of-3 AGAINST and Tier 2 is a retrospective in-sample construction, so THE LEG CURRENTLY HAS NO OUT-OF-SAMPLE SUPPORT ON EITHER TIER.** It is a **registered hypothesis awaiting its first real test**, not a supported claim. **V8 holds 4 on the vector's other evidence, NOT on this leg.**
- **FIRST OUT-OF-SAMPLE TEST: DG Q3 FY2026, ~Dec 2026.** Until it prints, this leg contributes **nothing** to conviction and must not be cited as if it did.
- **Optional strengthening, and it must be DECLARED if run:** back-testing the signature across DG's prior 4-6 quarters would widen n — but it is a **BACKTEST, not out-of-sample**, and labelling it otherwise would repeat this exact error one level down.

## Resolvers
| when | what |
|---|---|
| monthly, ~15th | Census advance retail sales ⇒ refresh T1-a/b/c (deflate, always) |
| **~Dec 2026** | **DG Q3 FY2026 — the T2-a resolver. Real ticket + traffic sign.** |
| quarterly | DLTR / WMT traffic-vs-ticket |

**Vintage discipline (WQ-175):** retail sales and CPI are **revisable**. Every figure here carries its observation date; **recompute on the current vintage before grading — never grade off a stored delta.**
