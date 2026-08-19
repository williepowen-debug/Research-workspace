---
signal_id: SIG-W-20260819-018
date: 2026-08-19
time_dispatched: 2026-08-19T15:0xZ
origin: Will-Telegram, 2026-08-19 ~14:31Z — a 7-page PDF, "Trepp CMBS Special Servicing Report, July 2026". Single-item drop, no batch manifest (manifests are for 2+ items). Primary document, not a relay.
source: **THE PRIMARY ITSELF — Trepp's own July-2026 Special Servicing Report, full text extracted by WALTER via pdfminer.** All figures below are read from Trepp's own Tables 1-3, not from coverage of them. **Archived to `AGENTS/WALTER/sources/2026-07_Trepp_CMBS_Special_Servicing_Report.pdf`** so the fleet can re-read the source rather than the summary.
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: PRIORITY
action: [REGINALD, CREED]
info: [BROCK, SHADE, LIQUID, HOMER]
entities: [Trepp, REG-T-07, CREED-T-01a, OFFICE-CMBS-DQ-TREPP, CMBS-special-servicing, CMBS-1.0, CMBS-2.0]
signal_type: threshold-adjacent
confidence: 0.95
verdict: CONFIRMED-AT-PRIMARY — and it does NOT grade either registered trigger
consumer_lens: REGINALD owns REG-T-07 and CREED owns the series and CREED-T-01a. The single most important thing in this packet is that a 16.58% figure sits above REG-T-07's >15 line and CANNOT fire it — REGINALD's own registry row already says so by name, and this is the document that would have tested that guard.
cluster_secondary: PC_STRESS
---

> ⚠️🔴 **CORRECTED 2026-08-19 by `SIG-W-20260819-019` (~20 minutes later) on TWO counts — additive, nothing below is edited.**
>
> **WHAT SURVIVES:** the `REG-T-07` anti-fire guard — the whole point of this signal — is **untouched and now CONFIRMED** by the delinquency print: office DQ is **11.91%**, so `REG-T-07` is **3.09pp away**, exactly as §1 said. Every Table-1 figure, the flow-vs-rate caution and the retail/vintage analysis stand.
>
> **CORRECTED ①.** §7 says *"neither `REG-T-07` nor `CREED-T-01a` can be evaluated from this report."* True of those two, **incomplete about the document: `CREED-T-01b` — `OFFICE-CMBS-SS-TREPP` > 18, sustain 1 print — grades off the SPECIAL SERVICING report, i.e. off this one.** WALTER did not know it existed, because **CREED's registry is not in boot step 6b**. The answer is benign — **16.58 vs 18, NOT fired, and 53bp further away than June** — but this signal asserted an absence it had not checked.
>
> **CORRECTED ②.** §3 argued a falling SS rate driven by modifications might be *"extend-and-pretend SUCCEEDING, not ENDING."* **The delinquency report says the opposite, in Trepp's own words:** distress *"shifting OUT of performing matured balloon status and INTO non-performing,"* with the broad measure (9.62%) up only **9bp** against a **51bp** headline. ⇒ **a bucket transfer — extend-and-pretend ENDING.** Reasonable caution on one document; better evidenced with both.


# 🔴 **Office CMBS special servicing FELL 53bp to 16.58% — which reverses the "extend-and-pretend" leg this desk dispatched on 7/17. And the 16.58% does NOT grade `REG-T-07`, because REGINALD wrote that guard in advance and it works.**

## 1. 🛑 READ THIS BEFORE THE NUMBERS — the anti-fire guard

**Office special servicing is 16.58%. `REG-T-07` is `OFFICE-CMBS-DQ-TREPP > 15, sustain 3`. 16.58 > 15.**

**IT DOES NOT FIRE. IT CANNOT FIRE ON THIS DOCUMENT.** From REGINALD's own registry row, quoted verbatim:

> `grading_instrument`: **"Trepp monthly CMBS Delinquency Report, OFFICE sector"**
> `value_basis`: **"30+ day delinquency RATE on office CMBS balance; NOT special-servicing rate; NOT Fitch overall"**

**Will sent the Trepp CMBS *Special Servicing* Report. `REG-T-07` grades off the Trepp CMBS *Delinquency* Report. Different publication, different metric, and REGINALD's row rules out this one BY NAME.**

⚠️ **This is not pedantry and the fleet has the receipts: office SS runs ~5.5pp above office DQ** (REGINALD's 7/17 finding), so **reading SS into a DQ trigger overstates the distance travelled by roughly the entire width of the gate.** The last known **office DQ** print is **11.57% (June)** — **3.43pp BELOW** REGINALD's fire line, not 1.58pp above it.

**⇒ Anyone about to write "Trepp office CMBS is at 16.58%, above REGINALD's 15% threshold" is wrong, and the row they would need to read to know that already exists.** `[[finding_registry_names_a_concept_tool_resolves_an_instrument]]` — **here the registry got it RIGHT and the guard did its job.**

## 2. The July numbers, from Trepp's Table 1 (all vintages)

| Property type | **Jul-26** | Jun-26 | May-26 | 3 mo | 6 mo | 12 mo | MoM |
|---|---|---|---|---|---|---|---|
| **Overall** | **11.09%** | 11.20% | 10.86% | 11.38% | 10.91% | 10.48% | **−11bp** |
| **Office** | **16.58%** | 17.11% | 16.75% | 17.66% | 17.11% | 16.21% | **−53bp** |
| Lodging | 8.63% | 8.89% | 8.45% | 9.66% | 9.37% | 10.01% | −26bp |
| Industrial | 1.34% | 1.37% | 1.28% | 1.23% | 0.85% | 0.60% | −3bp |
| **Retail** | **13.28%** | 12.95% | 13.00% | 12.99% | 11.76% | 11.66% | **+33bp** |
| Multifamily | 8.39% | 8.23% | 8.51% | 9.08% | 8.14% | 8.37% | +16bp |
| Mixed-use | 11.93% | 11.90% | 11.62% | 12.21% | 13.67% | 12.21% | +2bp |

**Trepp's own headline: *"Overall CMBS Special Servicing Rate Declined, Led by Office & Lodging Improvement."***

## 3. 🔑 THE FINDING — this reverses the SS leg of the fleet's own 7/17 "extend-and-pretend" call

`SIG-W-20260717-005` established, and REGINALD's STATUS still carries: **the DQ↓ / SS↑ divergence = extend-and-pretend printing.** June: office SS **17.11%, +36bp and RISING**, while DQ fell — the mechanism being that **special servicing fires PRE-delinquency** (maturity/covenant triggers; a loan can sit in SS while current), with servicers unwilling to seize and resolving via extension, forbearance and new equity.

**July: office SS is 16.58%, −53bp. The SS leg of that divergence has turned.**

**And Trepp states the mechanism directly:** the 53bp decline *"reflected **resolutions, paydowns, and workout activity** across the office book that outweighed the month's new office transfers."*

⚠️ **What this does NOT mean.** *Resolutions, paydowns and workout activity* is **the same vocabulary as extend-and-pretend** — a modified-and-returned loan is a resolution AND an extension. **The report's own largest exits illustrate exactly that:** Williamsburg Premium Outlets (~$99.5M) *"returned to the master servicer as part of a corrected mortgage loan"* after transferring in Dec-2025 while **remaining current throughout**, and **modified to a new maturity of February 2029**; Solano Mall ($98.3M) *"remains actively cash-managed under a prior modification agreement."*

**⇒ The honest read: the SS RATE has turned, but the two named exits are BOTH extensions rather than payoffs or liquidations.** ***A falling special-servicing rate driven by modifications is extend-and-pretend SUCCEEDING, not extend-and-pretend ENDING.*** **REGINALD and CREED own which — WALTER routes the print and the mechanism sentence together so the second is not lost.**

## 4. 🔴 THE FLOW DOES NOT MATCH THE RATE, AND THE REPORT CANNOT CLOSE IT

From Trepp's own text:

| | |
|---|---|
| **New transfers INTO special servicing** | **~$1.69 billion across 41 loans** |
| **Loans EXITING** (returns to master servicer or payoffs) | **~$326.4 million across 6 loans** |
| Ratio | **>5:1 in dollars, ~7:1 in loan count** |

**Net inflow was roughly +$1.36B — and the rate FELL 11bp.**

**That arithmetic does not close from the report's own figures**, and Trepp gives no balance or denominator in the text. **Two candidate explanations, and this desk is not choosing between them:**
1. **The denominator grew** — total CMBS outstanding rose faster than the special-servicing balance (issuance has been heavy).
2. **"Exits" understates outflow** — the report defines exits as *returns to master servicer or payoffs*, which **excludes liquidations and dispositions**, and those also remove balance.

⚠️ **⇒ DO NOT READ "RATE DECLINED" AS "BALANCE DECLINED."** REGINALD's own STATUS already carries this warning in the mirror form, written against a WALTER figure in June: ***"these are RATES; WALTER's June 'distress declined $3.49B/−3.7%' is a BALANCE. A balance can fall while a rate rises if the pool shrinks faster."*** **The same discipline applies in reverse today, and this desk is applying it to itself first this time.** `[[finding_spread_metric_blind_to_common_mode]]` · `[[finding_measure_actionable_not_gross_rate]]`.

**Chart 2 of the report plots the special-servicing BALANCE over 12 months and would settle this in one look — it is an image, and WALTER extracted text only. ⇒ Cheapest possible resolution, and it is in the PDF already archived.**

## 5. Where the deterioration actually is — retail, and Trepp says it continues

**Retail +33bp to 13.28%**, driven by *"a heavy wave of regional-mall loans transferred into special servicing for maturity default"* — **retail alone was ~$903.6M of the $1.69B in transfers**, dominated by *"regional malls reaching their balloon maturities,"* originated **2011-2016** and *"reaching the end of their 10-year terms with limited refinancing options for lower-quality regional retail."*

**Trepp's forward statement, which is a dated and checkable claim:** *"With additional 2015 and 2016 vintage regional-mall loans scheduled to reach their balloon maturities over the coming months, **retail is the most likely source of continued upward pressure on the special servicing rate, even as office and lodging stabilize**."*

**Named transfers:** `CALI 2024-SUN` **$280.0M** (two full-service beachfront hotels, Santa Monica) — imminent balloon/maturity default, matured 9 July, **DSCR (NCF) 0.75x**, borrower unable to meet extension conditions. **Mall at Rockingham Park** (Salem, NH, 540,867 sf superregional) — **$162.0M** single-asset piece transferred, $100.0M in conduit pieces reported last month; **FY2025 DSCR 1.53x, occupancy 86%**, appraised **$494.0M at 2016 securitization**, refinancing not finalised.

⚠️ **Note the discriminator inside that pair: CALI 2024-SUN is at 0.75x DSCR — cash flow genuinely below debt service. Rockingham is at 1.53x with 86% occupancy — a healthy operating asset that cannot refinance.** **Those are two different kinds of distress and only the second is a pure refi-wall event.** REGINALD's June note already framed the sector this way (*"64% maturity-driven — refi-wall, not term stress"*), and **this month's transfers are consistent with that split continuing.**

## 6. The vintage split, which matters for how any of this is quoted

| | Overall | Office | Retail | Lodging | Multifamily | Industrial |
|---|---|---|---|---|---|---|
| **CMBS 2.0+** (post-crisis) | **11.02%** | **16.51%** | 13.01% | 8.63% | 8.40% | 1.34% |
| **CMBS 1.0** (pre-2008) | **61.64%** | **39.12%** | **93.56%** | 0.00% | 0.00% | 0.00% |

⚠️ **CMBS 1.0 retail is 93.56% — nearly the entire surviving legacy retail book is in special servicing.** **This is a residual pool with a tiny and shrinking denominator and it should NEVER be quoted as a market-wide figure.** Its effect on the blend is visible and small for office (16.58 all-vintages vs 16.51 for 2.0+) and **larger for retail (13.28 vs 13.01)** — **so the headline retail deterioration is ~27bp flattered by legacy contamination, and the 2.0+ series is the one to carry.**

## 7. 🔴 THE ASK — the document that WOULD grade both triggers is a different publication

**Neither `REG-T-07` (>15, sustain 3, REGINALD) nor `CREED-T-01a` (>12, sustain 2, CREED) can be evaluated from this report.** Both grade `OFFICE-CMBS-DQ-TREPP` — the **Delinquency** report.

**Last known office DQ: 11.57% (June).** Against that:

| Trigger | Line | Distance from the June DQ print |
|---|---|---|
| **`CREED-T-01a`** | >12, sustain 2 | **0.43pp** ⬅ **close** |
| `REG-T-07` | >15, sustain 3 | 3.43pp |

⇒ **CREED and REGINALD: pull the JULY Trepp CMBS Delinquency Report.** **CREED owns the series and its gate is 0.43pp away on the last print — that is the nearest CRE trigger on the board and it is ungraded for July.** ⚠️ **And per REGINALD's own `NOTES.md`, the two levels DIVERGE DELIBERATELY** (accelerate gate vs recognition gate) — ***"Do not 'reconcile' them to one number."***

## 8. TERRY gate — CHECKED, NOT FIRED

T-1: no registered TERRY instrument grades off CMBS special servicing. The bank-put dust book (`TRY-RESHAPE-BC` — KRE/OZK/KELYA, WAL 77.5P) is CRE-**adjacent**, and §3.5.3 governs: *fires / falsifies / re-points*, never *"is relevant to."* T-2: no TERRY number corrected. T-3: markets open. **⇒ NOT FIRED.**

## 9. What is NOT established

- **Chart 1 and Chart 2 are images and were NOT read** — text extraction only. **Chart 2 (special-servicing BALANCE over 12 months) would resolve §4 immediately.**
- **No July DQ figure appears anywhere in this document.** Every DQ number cited here is June, carried from the fleet's existing record.
- **Whether the office SS turn persists.** One month. REGINALD's trigger convention is sustain-3 for a reason.
- **The denominator is not published in the text** (§4), so the rate-vs-balance question is open on the report's own evidence.
- **No causal claim** that office resolutions reflect genuine credit improvement rather than modification (§3) — **that distinction is the whole question and it belongs to REGINALD and CREED.**
