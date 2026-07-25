# PROMPT-19 — FHA/VA "federally absorbed" KILL: 4-axis adversarial stress-test — SYNTHESIS

**Run:** 2026-07-24 eve → 2026-07-25 00:10Z · **Commissioned:** Will (Telegram), direct follow-up on `SIG-W-20260724-001`
**Prompt:** `AGENTS/DEWEY/inbox/WALTER/DEEP-RESEARCH-PROMPT-19-fha-va-kill-stress-test.md` · **Ledger:** `REQ-DEWEY-20260724-019`
**Orchestrated by:** WALTER (4 parallel axis agents) · **Parent under test:** `AGENTS/DEWEY/output/2026-07-24_fha-va-loss-waterfall.md`

> **Axis B and D wrote their own reports to disk** (`2026-07-24_axis-B_fha-partial-claim-deferral.md`, `2026-07-24_axisD_mip-pressure-and-va-residual.md`).
> **Axis A and C did NOT** — they delivered by message only. **Their findings are preserved here.** This file is the canonical record of the run.

---

## HEADLINE VERDICT

> **The KILL SURVIVES and is now HARDENED from sector-inference to name-level fact. But the parent's supporting evidence is FALSIFIED in three places, and one of the four watched banks must NOT be switched off.**

The consistent shape across all four axes: **the parent's CONCLUSION kept surviving while its EVIDENCE kept needing replacement.** Three of four hypotheses in the prompt were WALTER's own, and two were refuted outright.

| Axis | Hypothesis | Outcome | Effect on the KILL |
|---|---|---|---|
| **A** — name-level bank exposure | Sector averages can't kill a firm-level channel | **Gap was REAL; KILL survives-with-caveat** | Hardens the conclusion, **falsifies the evidence** |
| **B** — partial-claim deferral | Ratio is deferral-flattered | **PARTIALLY — immaterial to the floor** | Survives |
| **C** — actuarial staleness | 11.47% is a stale lagging stock | **MODERATE — lands on evidence, not conclusion** | Survives; **strike the Urban citation** |
| **D** — MIP political erosion | A high buffer erodes itself | **REFUTED — premise was wrong** | Survives |

---

## AXIS A — name-level bank exposure (**the decisive axis**)

**Method:** SEC EDGAR 10-K/10-Q/8-K via `curl -H "User-Agent: …"` (HTML, no PDF path needed) + FDIC Call Report JSON API (`LNNDEPD`, REPDTE 2026-03-31) + EDGAR full-text search in **both directions**. Every figure sourced in-run.

| | **BKU** BankUnited | **SSB** SouthState | **AMTB** Amerant | **SBCF** Seacoast FL |
|---|---|---|---|---|
| Equity | $3,003M (6/30/26) | $9,030.9M | $914.4M | $2,717.7M |
| FHA/VA HFI / rebooked EBO | **$851M "Buyout Loans"** (gov-ins total $883.4M) | **ZERO** | **ZERO** | **ZERO** |
| % of equity | **28.3%** | 0% | 0% | 0% |
| Mortgage warehouse | **$877M**, +40% YoY ($627M 6/25 → $877M 6/26); **counterparties NOT disclosed** | ≈$72M | ≈$54M | ≤$73.2M (Call Report ceiling) |
| % of equity | **29.2%** | 0.8% | 5.9% | ≤2.7% |
| Servicing-advance / MSR facility | **ZERO** | ZERO | ZERO | ZERO |
| Ginnie issuer/servicer | **NO** — *"The Company is not the servicer of these loans"* | NO (GSE-only) | NO (Fannie-only, winding down) | NO |
| **Verdict** | 🔴 **MATERIAL — parent's evidence falsified** | ✅ de minimis | ✅ de minimis | ✅ de minimis |

### The BKU finding, decomposed

The parent's load-bearing sentence — *"documented current bank EBO balances are immaterial — Wintrust $187.8M vs a multi-billion equity base"* — **is FALSE as a general claim.** BKU is **4.5× Wintrust in dollars and ~20× relative to equity**; combined EBO + warehouse ≈ **58% of equity.** Exactly the sector-average-cannot-refute-idiosyncratic-concentration error the axis was built to test.

**But what BKU bears is NOT what was killed:**

- **🔑 Credit risk CONFIRMS the KILL from a bank's own accounting.** BKU FY2025 10-K: *"The Company expects to collect the amortized cost basis of government insured residential loans due to the nature of the government guarantee, **so the ACL is zero for these loans**."* Delinquent gov-insured loans are excluded from non-accrual on the same basis. **A bank holding $851M of defaulted FHA/VA paper books ZERO credit reserve against it.** Federal absorption, corroborated at name level by a party with money at stake.
- **BKU is NOT the servicer** → bears no curtailed debenture interest, no reasonable-diligence/conveyance penalties, no P&I advance drain. The servicer-residual leg does not land on it.
- **What BKU DOES bear (absent from the parent):** (a) **resolution-timeline / carry risk** on a nonperforming pool — exactly what HUD's new mandatory waterfall lengthens; (b) **direct dependence on nonbank Ginnie servicers** — *"The Company and the servicer share in the economics of the sale of these loans into new securitizations"*: BKU's exit path runs THROUGH the entities the parent named as the weak link; (c) **$877M warehouse growing 40% YoY** — the only channel here that is growing.
- **Deterioration tell:** 90+ DPD still accruing (substantially all Buyout Loans) **$159M (12/31/25) → $197M (3/31/26), +24% QoQ**. Against a *shrinking* stock (−34% since 12/2023). **Shrinking book, rising delinquent share inside it.**

### Post-VASP regime change — mechanism confirmed, magnitude REFUTED

Axis D inferred that post-VASP, bought-out VA loans staying with servicers would GROW bank counterparty exposure. BKU is the one place this was measurable — it buys exactly this paper. **Its book went the other way:**

| Date | Gov-insured resi HFI |
|---|---|
| 12/31/2023 | $1,306.0M |
| 12/31/2024 | $1,071.9M |
| **2025-05-01** | **VASP terminated** |
| 12/31/2025 | $891.0M |
| 3/31/2026 | $883.4M |

**−19% across the four quarters spanning termination.** What moved as predicted is the *delinquent share inside* the shrinking book — consistent with **resolution timelines stretching, not volumes migrating.**

### Ex-VASP counterparty search — both directions, 20+ queries

Nineteen of twenty zero. One false positive worth recording: **AMTB × NewRez is NOT an exposure** — an 8-K exhibit (Master Loan Sale Agreement, 2024-12-27) where AMTB is the **SELLER** of business-purpose investor DSCR paper and NewRez/Shellpoint appears once in §1.57 as the purchaser's *successor servicer*. Direction is AMTB divesting; no lending relationship, no FHA/VA. Reverse direction: **SIC 6162 (Mortgage Bankers) does not appear in the top-10 SIC buckets for any of the four banks**; direct queries against Rithm/PFSI/PMT/loanDepot/UWM/Onity/Rocket returned zero for all four bank names.

**Structural wall, flagged honestly: four of five named ex-VASP heavies (Village Capital, The Money Source, Planet Home, CrossCountry) have NO EDGAR presence.** Their warehouse-lender lists are not publicly filed → **UNVERIFIABLE, not negative.**

### Kill-condition re-verify: NO discrete nonbank-servicer stress event
Swept Freedom, loanDepot, Lakeview/Bayview, Carrington, Onity, PFSI, Rocket (2026-05-01→07-24). **Two traps caught:** a loanDepot "downgrade" circulating July 2026 is a **Goldman equity Sell / PT cut — a stock call, not a credit action**; a "Fitch downgrades Finance of America" headline is **October 2023 recirculating** (FOA's 2026 posture is the opposite: Q1-26 $35M net income). Live theme is **structural pressure, not a realized event.**

---

### 🔬 AXIS A WAS INDEPENDENTLY REPLICATED — and the two runs CONVERGE

Axis A was accidentally run **twice**: the original agent went silent, a disk check confirmed no output, and a replacement was spawned — which had already produced its own report before the stop order reached it. **Two agents, separate sessions, no shared working state, same question.** The second report is preserved at `AGENTS/DEWEY/output/2026-07-25_axisA_fha-va-bank-name-level-exposure.md`.

**They agree on every load-bearing point**, independently sourced:
- **Verdict identical: SURVIVES-WITH-CAVEAT.**
- **BKU is the exception; SSB / AMTB / SBCF are clean.**
- **~58% of equity combined** at BKU (run 1: 28.3% + 29.2%; run 2: 29.3% + 29.2%) — the small delta is 3/31 vs 6/30 equity denominators, not a disagreement.
- **BKU ≈ 4.5× the Wintrust datapoint**, both runs, independently derived.
- **The zero-ACL corroboration** — both runs independently identified that BKU reserving $0 against defaulted FHA/VA paper *confirms* the absorption conclusion while falsifying the evidence. Run 2 phrases it well: *"a bank willingly holds $883M of 22%-90-days-delinquent paper at zero reserve precisely because the sovereign eats the credit."*
- **Counterparty search: zero hits, both runs, both directions.** Neither found any of the five named ex-VASP nonbanks in any of the four banks' filings.

**Where they COMPLEMENT rather than repeat — each closes a gap the other left open:**
| | Run 1 (original) | Run 2 (replacement) |
|---|---|---|
| **FFIEC Call Report** | ✅ **Queried via the FDIC JSON API**, and the NDFI series **cross-validates each bank's own disclosure** (AMTB to the dollar; BKU/SSB to <0.2%) | ❌ Not queried — CDR bulk download is registration-gated; **flagged as its single largest open gap** |
| **AMTB forward risk** | Scored de minimis (5.9% of equity), no forward flag | ⚠️ **NEW: AMTB's single-family residential book grew $1,515M → $1,954M = +29% in six months** against $914M equity, with **no government-insured breakout**. De minimis today, but *"if FHA/VA-adjacent paper entered the book it would not be separately visible at current disclosure granularity."* **Check the Q2-2026 10-Q loan-composition note.** |
| **BKU deterioration** | 90+ DPD still accruing $159M → $197M, **+24% QoQ** | **22.3% of the book is 90-days-delinquent**; warehouse **+49.7% since 12/31/24** |

**Net effect: run 1 closes the exact gap run 2 flagged as its weakest point (bank-level Call Report data), and run 2 adds a forward monitoring item run 1 missed (the AMTB disclosure-granularity gap).** Confidence in the decisive finding is materially higher than a single agent's report would warrant — this is the one conclusion in the study that changes what a domain agent does, and it now rests on two independent primary-sourced derivations rather than one.

**⚠️ One methodological caution carried from run 2, against itself:** its "no discrete nonbank-servicer stress event" negative was **web-search only** — *"treat as 'no evidence of,' not 'confirmed absence of.'"* Run 1's sweep was broader (it caught and excluded two recirculation traps run 2 did not surface), so the kill-condition negative rests primarily on run 1.

---

## AXIS C — actuarial staleness (findings preserved; not written to disk by the agent)

**Method:** 6 PDFs downloaded and locally extracted (annual report 327K chars, actuarial review 389K chars), tables re-extracted with `pdftotext -layout` and **foot-checked**.

### Ratio composition — ~47% is NOT cash

| Leg | pp of IIF | ~$B | Share | Assumption-sensitivity |
|---|---|---|---|---|
| Cash & equivalents | **>6.07** | >100 | ~53% | None |
| HUD-held notes + REO (partial-claim receivables) | ~2.41 | ~39.7 | ~21% | High |
| NPV of projected future cash flows | 2.99 | 49.2 | ~26% | Highest |

Foot-checked: 139,665 + 49,206 = 188,871 ✓ / 1,647,236 = 11.466% ✓.
**But the counter-fact is decisive: cash alone is >6.07% of IIF — >3× the 2.0% floor, and growing ($200.5B, +$4.09B in Q1-FY2026).** Write off the entire NPV leg AND every note and property and the fund still clears the minimum. Reaching 2.0% needs an extrapolated **~35–42% national house-price decline, ~1.7–2× the GFC**.

### 🔑 STRIKE the Urban Institute ">5×" citation
Goodman/Zhu/Tozer/Choi, **July 2025**, pp.16-17 — verified by local grep of the PDF. Six defects; two fatal:
- **Wrong vintage:** its own text reads *"At the end of **fiscal year 2024**, the ratio was 11.47 percent."* FY2024 and FY2025 are **both 11.47%** — a coincidence that concealed the error. The cushion rests on **Sept-30-2024 data, ~22 months stale.**
- **Flow-vs-stock:** compares an *annual* loss rate to a *cumulative* capital stock. "2.5% annual losses, well below the buffer" holds one year; **sustained five years it is 12.5% and exceeds it.** GFC stress ran ~5 years.
- Also asserts capital resources are *"unaffected by any increase in delinquencies"* — **false**, they include partial-claim receivables behind a ~60% one-year re-default rate.
**→ Replace with FHA's own Exhibit II-27 sensitivity ladder + the ">6.07% cash-alone" floor. The conclusion survives; the evidence under it should be upgraded, not defended.**

### The surface the parent never cited
**FHA publishes a QUARTERLY Report to Congress (12 U.S.C. 1708(a)(5))** with a statutorily-compelled predicted-vs-actual table. FY2026-Q1 Figure 6: **claim counts −57.4% vs forecast, claim dollars −50.8%, net loss on claims +7.75pp (+30.9%).** Claim VOLUME running at less than half the model; claim SEVERITY ~31% above it. FHA attributes part of the volume shortfall to waterfall timing — **part of the beat is DEFERRAL, not avoidance.**
**Q2 edition (data as of 2026-03-31) is ~3 months OVERDUE.**

### FHA's own worst case is thinning
Exhibit II-28 worst-scenario ratio: **6.31% (FY22) → 5.43% (FY23) → 5.48% (FY24) → 4.42% (FY25).** The headline sits flat while the tail thins. The worst scenario burns **~61% of the cushion.**

### ROAD Act §702 — verified at TWO primaries
Enrolled bill (`govinfo.gov`, BILLS-119hr6644enr, line 5958) + House FSC section-by-section. **Pub. L. 119-101, law 2026-07-11 without signature.** Requires **monthly** reports on the capital ratio + sub-floor notification.
- **Legally the FULL ACTUARIAL ratio** — §702 → §205(f)(2) → 12 U.S.C. 1711(f)(4)(C): capital = *"current cash available… PLUS the net present value of all future cash inflows and outflows."*
- **But probably delivered cheap:** the NPV leg comes from an **annual** OMB PEA and an **annual** contracted actuarial engagement (no monthly input exists); **§1202 authorizes zero new funding**; and §702 specifies **no effective date, methodology, format or content** — in pointed contrast to ¶(5), whose content Congress *did* enumerate. **§702 SUPPLEMENTS the quarterly and annual obligations; it supersedes neither.**
- **§702(B) is a floor alarm, not an early warning** — it fires *after* a breach.

---

## AXIS B — partial-claim deferral (full report on disk)

**Verdict: PARTIALLY deferral-flattered; KILL survives on magnitude.**
- Partial claims are **marked, not carried at face** — valued at NPV of expected cash flows, allowance ratio **rising 23.2% → 31.4%**. HUD is marking harder, not concealing. Defeats the strong form.
- Gross receivable **$13.78B (FY20) → $39.80B (FY25), +189%**; net $27.86B ≈ **21% of forward capital resources and effectively the entire non-cash residual.**
- **🔑 Re-default is NOT benign:** one-year re-default after loss mitigation **11% (2020/21Q1) → 53% (2023Q4) → 58% (2024Q4)**, vs a 2009-2019 average of 46%. **~40% of Sept-2025 recipients were on their THIRD option in five years** (vs ~2% in Jan-2018).
- The actuarial review mentions "redefault" **exactly once in 381,721 characters** — and only to describe a policy response, never to model the risk. **Independently verified by axis C via local grep of both PDFs.** The actuary explicitly declines the cost-benefit question: *"not addressed in sensitivity tests."*
- Ratio books **$2.07B (0.126pp)** of savings from a waterfall effective **the day AFTER** the measurement date.
- **⚖️ DECISIVE: net receivable = 1.69pp of IIF. Zero the ENTIRE thing → 11.47% falls to 9.78%, still 4.9× the floor.** Breaching needs $155.9B of destruction; the whole gross receivable is $39.8B. **It cannot get there.**
- **Premise correction: ML 2025-06 was superseded by ML 2025-12** (eff. Oct 1 2025).
- HUD OIG 2026 (secondary, Cloudflare-blocked): **74 of 81** sampled partial-claim loans had servicing/collection problems. **GAO: nothing.**

---

## AXIS D — MIP politics + VA residual (full report on disk)

**D(i) REFUTED.** MIP history vs the ratio at the time: **2015 cut at 0.41% (BELOW the floor)** · 2017 attempt at 2.32% (at the floor), suspended ~1hr after inauguration · **2023 cut at 11.11%**. **Only one of three came at a high ratio — the premise that a high buffer generates cut pressure does not hold.** MIP tracks the administration's affordability posture, not the capital ratio; the 2017 suspension is the clean proof (the ratio didn't move in those 11 days, the administration did). **Nothing proposed/announced/enacted/effective for FY2026-27**; the ROAD to Housing Act contains **zero** single-family MIP provisions (full-text verified). The 2023 cut (−30bp, ~35% less premium revenue, ~$2.6B/yr forgone) was **absorbed with the ratio ending higher**.

**D(ii) PARTIALLY CONFIRMED.** VA guaranty is a **25% stop-loss, not insurance** (FHA insures 100%). The **"no-bid"** is the loss-transfer valve: VA pays the guaranty cap and the servicer/holder eats `indebtedness − (guaranty + proceeds)`. **Mechanism confirmed at regulation; magnitude UNQUANTIFIED — no no-bid frequency or loss-severity-vs-cap data exists at primary.**
**🔑 The advocacy figures survive as counts but their causal story does not:** "~90,000 VA loans seriously past due" — **AEI counted ~80,000 seven weeks BEFORE VASP terminated.** The increment attributable to the 13-month gap is **~10,000 (~12%), not 90,000.** ">10,000 veterans lost homes" is at or below the ~15,000/yr 2017-19 baseline. "~33,000 in foreclosure" traces circularly back to the same ICE series. **Cite instead: MBA NDS Q1-2026 — VA foreclosure rate at its highest since Q2 2017, VA DQ ~225bp above conventional.** The deterioration is real *in rate*; the 10,000 figure is not the evidence for it.

---

## CONSEQUENCE FOR REGINALD

> **Switch off SSB, AMTB and SBCF with confidence — figures now on record.**
> **DO NOT switch off BKU. Re-point it.** Its watch item is no longer FHA/VA credit loss (ACL is zero, by BKU's own accounting) — it is **(i) mortgage-warehouse growth and undisclosed counterparty identity, (ii) the 90+ delinquent share inside the buyout book (+24% QoQ), and (iii) resolution-timeline risk that HUD's new waterfall lengthens.**
> **BKU is the fleet's one direct wire between a watched regional bank and the nonbank-servicer credit the parent says to trade.**

## CATALYST STACK (revised — November is NOT the top item)

1. **🔴 Overdue, any day — FHA FY2026-Q2 Quarterly Report, Figure 6.** Richer than the monthly ratio: it reports *the model is wrong and in which direction*. Does the −57.4% claim shortfall persist (deferral holding) or reverse (deferred claims landing)?
2. **🔴 4-8 weeks — HUD's first §702 monthly report.** One question settles it: **does the reported ratio move the NPV leg, or only capital resources?** Cheap, near-dated, free.
3. **2026-07-28 — SBCF Q2 print.** **Early Aug — BKU Q2 10-Q** (closes the derived 6/30/26 gov-insured figure + any warehouse counterparty detail).
4. **~mid-Aug — MBA NDS Q2-2026.**
5. **Nov 2026 base / Dec-31 late — FY2026 Annual Report + Actuarial Review.** Watch the capital-resources composition line and Exhibit II-28's worst case (5.48% → 4.42% last year).

## HONEST LIMITS
- Four of five named ex-VASP nonbanks have **no EDGAR presence** → unverifiable, not negative.
- **BKU does not name warehouse counterparties**; whether the $877M runs to FHA/VA-concentrated nonbanks is unknown from public filings.
- Ginnie Mae's canonical issuer directory unreachable (site rebuilt as a JS SPA ~2026-07-14) → issuer negatives rest on filings, not Ginnie's list.
- **The PEA house-price forecast path — the single most important assumption behind 11.47% — is NOT PUBLISHED ANYWHERE.** Grepped both full documents. That is itself the finding.
- MBA NDS Q1-2026 (the 11.88% / +212bps figures) **403'd — unverified at primary**; FHA's own LPT series is a different, explicitly non-reconciling methodology.
- Axis B's specific 58%/46% cohort figures not independently re-derived by axis C (its AR cut is consistent but different).

## THREE CORRECTIONS TO PROMPT-19 ITSELF (all inherited from the parent, not introduced by WALTER)
1. **VASP termination instrument is Circular 26-25-2, issued 2025-04-23, effective 2025-05-01** — not "announced 4/3/25, Circular 26-23-25".
2. **ML 2025-06 was superseded by ML 2025-12.**
3. **"Check whether the FY2026 actuarial review has been released" was a category error** — FY2026 does not end until 2026-09-30.

## PROCESS NOTE
**All four agents idled WITHOUT delivering; three had completed work behind the silence.** Reading the first idle notification as "found nothing" would have scored this entire study a failure. Axis A produced nothing on its first run and was re-spawned only after a disk check confirmed genuine absence. Axis B diagnosed the likely cause: **WebFetch returns `cannot parse binary/encoded streams` on PDFs but STILL SAVES the file** — recorded fleet-wide as `[[finding_webfetch_pdf_saves_despite_parse_error]]`. (Axis A ultimately needed no PDF path — all filings parsed as HTML via curl+UA.)
