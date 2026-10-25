# DEWEY's research history, Feb–Oct 2026: outcomes, blind spots, and what reached decisions
**Date:** 2026-10-23 (research 18:51–19:05 ET) | **Mode:** Thesis (self-review) | **Request:** Will-directed ("Yes start it now", 18:51 ET), scoped by an outside reviewer's four asks | **Confidence:** High on the classification method and the downstream traces (artifacts read). Medium on outcome shares (headline-only coding, rubric edge cases). Low on any claim that the blind spots *precede* market stress (untested).

> **Status of this document:** a dated record, not a current-state surface. It does not create collectors, standing obligations or charter changes. The instrument proposals in §3 are proposals for PROME and the named owners.

## Key Finding
1. **The supported claim is an observability gap, not risk migration.** In five domains, the public indicator the fleet watches did not show what a non-market source did. None of the five shows exposure *moving* over time, and none shows the gap *preceding* market stress. Both remain hypotheses.
2. **Outcome split, measured:** of 67–69 premise-testing reports (June–October), **49–57% deflated the commissioning concern, 25–26% confirmed it, and 19–23% were mixed.** These are two independent classifications (DEWEY's own and a blind rater's), with 80% agreement and Cohen's kappa 0.73. **This replaces DEWEY's earlier "~50 of 80 deflated"**, which was its own unaudited count and leaned toward "deflated".
3. **Downstream use is real; cross-desk caveat loss was not established by this trace.** All five traced reports were consumed, with different effects on the recipients' judgments. CARL retained the charged-off cohort's uncertainty and rejected DEWEY's reconciliation on a stated falsifiability ground. **The earlier "two of five" caveat-loss claim is withdrawn: no second recipient case was identified.** Separately, DEWEY dropped qualifications in its own 2026-10-23 synthesis (NVIDIA $164.5B; the charged-off cohort). Those are own-synthesis failures, not a measured cross-desk loss rate.

## 1. Auditable classification of the 93 reports
**Method.**
- **Unit:** every row in `output/INDEX.tsv` (R01–R93, ledger order), coded from the report's headline finding only, truncated at 700 characters. **The report bodies were not re-read for coding.**
- **Rubric** (written before coding): CONFIRMED · DEFLATED · MIXED · NULL (deciding fact unavailable) · DESCRIPTIVE (no premise tested), plus a flag for "premise number wrong". The full rubric text is in Appendix A.
- **Two raters:**
  - DEWEY.
  - A blind rater: an Opus sub-agent that read only the rubric and the headline file, nothing else in the repository.
- **The full per-row table is Appendix B**: id, date, question, commissioner, both codes, the blind rater's confidence and reason.

**Agreement.** 74 of 93 (80%), **kappa 0.73**. On the 53 rows the blind rater coded high-confidence: 49 of 53 (92%). On the "premise number wrong" flag: 86 of 93; DEWEY flagged 16, the blind rater 21, both 15.

| Outcome | DEWEY | Blind rater | Both agree |
|---|---|---|---|
| DEFLATED | 39 | 33 | 30 |
| CONFIRMED | 17 | 18 | 14 |
| MIXED | 13 | 16 | 10 |
| NULL | 8 | 10 | 7 |
| DESCRIPTIVE | 16 | 16 | 13 |

**Main disagreement:** five rows DEWEY coded DEFLATED were coded MIXED by the blind rater ("real but concentrated" headlines). **DEWEY's coding leans toward DEFLATED.** Treat the 49% (blind) to 57% (DEWEY) range as the measurement, not either end.

**Rubric weaknesses the blind rater found:**
1. When the hypothesis under test is the *reassuring* one, "confirmed" means the concern deflated (R21, R39, R41, R49).
2. Some headlines carry no verdict (R40, R54); a "no headline verdict" code is needed.
3. "Real but concentrated" sits between DEFLATED and MIXED.
4. There is no rule for a NULL next to a partial answer (R55, R62, R65).

**What this does NOT measure:**
- research quality or a "success rate";
- whether the commissions were biased toward alarm (WALTER and the desks send DEWEY the alarms);
- whether cheaper questions deflate more easily;
- whether a deflation reached the decision-maker (see §4).

## 2. Five blind-spot cases
| # | Public indicator the fleet watches (what it showed) | Alternative source | What was actually observed | What remains speculative |
|---|---|---|---|---|
| B1 AI credit | HY OAS / CCC tier: AI builders ~3% of HYG; **0% of the rated-CCC basket** (XCCC, 10/22) [DEWEY 10/23] | NVIDIA 10-Q Note 10 guarantees, four consecutive quarters [DEWEY 9/10] | $164.5B is a **scale marker mixing contingent maximum exposure with firm commitments, not a loss estimate**: $108.5B guarantees + $36B AI-cloud commitments + $20B third-party leases. The **$105B SB Energy guarantee is contingent and unfunded; its first phase begins in FY2029.** Cash collateral by leg: first guarantee 54.7% escrowed → AI-cloud leg 20.2% → SB Energy leg 0% (OpenAI reimbursement promise only) | Whether the decline is structural or transitional (outside capital may replace NVIDIA's guarantees before FY2029; the report's own counter-case). No loss, no draw. |
| B2 Software leverage | CCC bonds: software **~5.9%** of the rated-CCC basket [DEWEY 10/23] | JPM loan price buckets (via reprint); BDC 10-Q industry tables | Technology = **39% ($54.4B) of loans priced ≤80c** (JPM 10/6); BDC software shares from 2.3% (PSEC) to 32.8% (HTGC) at 6/30/2026 | **39% is a share of the distressed pool, not a default rate for tech loans.** Software loan prices partly *recovered* into October (PIMCO). Q3 BDC marks are not yet filed. |
| B3 Charged-off consumers | Bank charge-off and delinquency series | Debt-buyer 10-Qs (PRA, Encore) [DEWEY 8/28] | At PRA, >100% of Q2 US collections growth came from litigation, while voluntary (call-centre) collections shrank in dollars. **But Encore is collecting ABOVE its own forecasts** (recoveries above forecast = 7.2% of Q2-26 collections, down from 8.0% in Q2-25; H1 6.8% vs 6.3%) and raised its forecasts; purchase-price multiples are flat at 2.3–2.5× | **"The cohort stopped paying" is the report's own *inference*, named there as its "load-bearing weakness".** A simpler reading (the cohort pays, via litigation, and models were conservative) is equally available. **This case is weaker than DEWEY's 10/23 synthesis stated.** |
| B4 FHA/VA mortgages | Regional-bank credit losses (bank channel KILLED) [DEWEY 7/24–25] | FHA serious-delinquency series; Ginnie nonbank servicer obligations | FHA serious delinquency **+226bp YoY (4.27% → 6.53%, May 2025 → May 2026)** [DEWEY 8/27]. The credit loss is federally absorbed; the liquidity strain (P&I advances, ~90dpd buyouts) falls on nonbank servicers holding 83–96% of Ginnie servicing | Whether any servicer liquidity event occurs. None observed in DEWEY's record. |
| B5 Cyber / vendors | CISA KEV (no banking product listed); bank cyber 8-Ks; past waves caused no bank run [DEWEY 10/22] | CSBS outsourcing survey; state AG breach notices; NCUA/FSOC documents [DEWEY 10/23] | 91.2% of community banks outsource all or part of network monitoring; 1 of 88 CA/WA breach notices took the MSP route; NCUA dropped its vendor-examination request in 2025 and documents no replacement | **Poor visibility is uncertainty, not evidence that losses are accumulating.** Frequency is under-observed in both directions. |

**Read across:** in each case the public indicator is calm or small, and the alternative source shows either exposure (B1, B2, B5) or strain (B3, B4). **Concentration is not the same as safety:** B1 runs through one supplier's guarantees to a few counterparties, and B2 through BDCs and CLOs that hold the same software names. Whether that gives a transmission path is the next question, not an answered one.

## 3. Bounded instrument proposal (three at most; existing owners; no new collector)
| # | Measurement | Existing owner | Decision it could affect | Cost / cadence | Status |
|---|---|---|---|---|---|
| — | NVIDIA guarantee-commitment level (B1) | VULCAN | S5 AI-credit read | Quarterly 10-Q | **ALREADY EXISTS: VULCAN-17**, registered 2026-09-11 from DEWEY 9/10 §6.4/§6.7. Not a new proposal; listed so the TERRY test (below) can use it. |
| I1 | Rated-CCC basket composition: XCCC holdings saved alongside HYG/JNK by `etf_holdings.py` (extension logged in BACKLOG) | LIQUID (REG-T-04), with REGINALD | Whether a REG-T-04 fire reads as a cycle signal or a few telecom/cable restructurings | Minutes per pull; **a daily save is a collector question for Will, WALTER and LIQUID** | Proposal |
| I2 | BDC software share, non-accruals and PIK by sector, from each BDC's 10-Q (13 names, DEWEY 10/23 table) | BROCK | The private-credit channel read (BRK-26 and related) | Quarterly; next window ~11/10 | Proposal (as a DEWEY dated rerun, not a collector) |
| I3 | Debt-buyer "recoveries vs forecast" and collections channel mix (Encore, PRA 10-Qs) | CARL | Whether the exited-cohort branch is impaired payment capacity or collection strategy (resolves B3's named weakness) | Quarterly; Q3 10-Qs early November | Proposal |

**The link to TERRY's dashboard, as a test and not a claim:** VULCAN-17, I1 and I2 are upstream series. TERRY's market warnings are downstream. A future test is whether moves in the upstream series *lead* TERRY's warnings. DEWEY has not run that test and makes no claim that they do.

## 4. Downstream-use check: five consequential reports
**Selection caveat:** these five were chosen as *consequential*, and DEWEY expected them to have been used. They are not a sample of the 93, and their uptake rate does not generalize.

| Report | Intended decision | Evidence of use (recipient's own record) | Verdict |
|---|---|---|---|
| R74 Reserve-coverage base rate (10/22) | REGINALD's weight on falling reserve coverage | REGINALD STATUS: "It is not a short-term predictor; **re-weighted 10/22**", citing the report. GIBBS KB-GIB-021 and FLG KB rows adopted the base rate; FLG applied it to its own non-accrual trend. CREED: noted, no change | **Incorporated; judgment changed** |
| R55 NVIDIA vendor financing (9/10) | VULCAN's AI-credit instrument choice | VULCAN KB rows carry the Lucent/Nortel base rate. **VULCAN-17 registered 9/11** "consumes DEWEY REQ-002 §6.4/§6.7" with a pre-committed reading rule | **Incorporated; instrument created** |
| R30/R39 FHA/VA loss waterfall + stress test (7/24–25) | Kill REGINALD's "bank eats FHA/VA loss" channel | HOMER KB_LIVE: "Regional-bank FHA/VA credit-loss channel = KILLED", citing DEWEY. CARL's STUE added the FHA channel it had not carried, and on 8/10 corrected a category error *at DEWEY's cited source*. REGINALD's own kill commit was not located | **Incorporated** (HOMER, CARL); **REGINALD side UNVERIFIED** |
| R53 Charged-off cohort (8/28) | CARL's masking branch | KB-CARL-402 records "(a)-LEANING, NOT (a)-CONFIRMED" and the split indicators. KB-CARL-403 explicitly declines the survivor-pool reconciliation as unfalsifiable and retains Encore's over-performance as UNRECONCILED COUNTER-EVIDENCE. The earlier DEWEY impact note misclassified this. | **Incorporated; reconciliation DECLINED with reason; counter-evidence retained** |
| R26 BRK-25 BDC print hunt (7/16) | BROCK's BRK-25 watch | BROCK cites the report in two source files. BRK-25 still open: "COUNT STAYS AT 2 … resolves by counting misses", 45%, to 12/31. DEWEY had found the watch's founding figure "refuted at its root" | **Consumed; target decision unmoved** (BROCK resolves by its own rule, which may be correct) |

**Pattern across the five:** use is easiest to trace when the recipient creates a **numbered artifact**: a re-weight line, a KB row, or a registered prediction (R74, R55). This selected trace does not establish a cross-desk caveat-loss rate. R53 demonstrates reasoned disagreement with the qualification preserved. DEWEY's own 10/23 synthesis of R55 and R53 lost qualifications; the prospective WQ-515 batch tests whether that failure also occurs between desks.

**Correction — 2026-10-25:** applied PROME's 10/23 verified review packet after reading KB-CARL-402/403 directly. The DESCRIPTIVE agreement cell is 13, making the column total 74; the agreement rate and kappa do not change. R53 is reclassified as reasoned disagreement with counter-evidence retained. "Two of five" is withdrawn throughout this report and corrected in the run ledger. Historical proposal and delivery packets remain as-made; the correction is delivered separately to their consumers. No new five-case rate is estimated. The headline-only coding limitation and unfinished independent full-text check remain open.

## 5. Addendum 2026-10-23 19:24 ET: full-text validation check NOT DONE (session ended)
The outside reviewer's third ask was a random sample checked against the **full reports** by a reader who did not write the rubric. It was started and **not completed**: the reader was stopped for a machine switch before it wrote any result. **Until it runs, quote the 49–57% only as a headline-level, two-rater figure.**
- **Sample** (fixed seed 20261023, 10 of R07–R93): R09, R32, R37, R39, R40, R52, R53, R59, R75, R80. R53 is a case discussed in this report; the seed drew it, it was not chosen.
- **Rubric v2** splits *hypothesis supported?* from *risk higher/lower?* (fixes ambiguity 1) and adds a headline-fidelity code.
- **Saved for the rerun:** `AGENTS/DEWEY/research/2026-10-23_meta-review/` (RUBRIC.md, RUBRIC_v2.md, sample10.tsv, both raters' codes).
- **To run:** a fresh reader reads only the 10 report files plus RUBRIC_v2, writes one table, and the result is added here as a second addendum.

## Counter-Evidence
- **Against the observability gap mattering:** every B-case is either contingent (B1), a share not a probability (B2), contested inference (B3), absorbed by a federal backstop (B4), or unobserved (B5). On the current evidence the gap could be harmless, with public prices catching what matters in time. The fleet has no test of lead/lag.
- **Against the deflation share meaning much:** commissions are selected for alarm, so a high deflation rate is expected even from neutral research. The rate also mixes questions of very different cost.
- **Against the downstream finding:** "8 of 93 rows record impact" undercounts by design: the ledger records only consumption DEWEY happened to hear about. Five traces cannot estimate fleet-wide uptake.

## Source Quality Assessment
- **Strong:** coding agreement, measured. Every downstream verdict cites a recipient's own file line.
- **Weak:**
  - The classification is headline-only.
  - The rubric has the four known edge cases.
  - DEWEY is both a rater and the subject; the blind rater offsets but does not remove this.

## References
(accessed 2026-10-23)
- `AGENTS/DEWEY/output/INDEX.tsv` (93 rows) and each `report_path`.
- **Recipient records:**
  - `AGENTS/REGINALD/STATUS.md:7`
  - `AGENTS/GIBBS/workbook/KB.tsv` (KB-GIB-021)
  - `AGENTS/FLG/workbook/KB.tsv:89`
  - `AGENTS/CREED/board_log.tsv:211`
  - `AGENTS/VULCAN/workbook/PREDICTIONS.tsv` (VULCAN-17) and KB rows
  - `AGENTS/HOMER/workbook/KB_LIVE.tsv`
  - `AGENTS/CARL/sub_agents/STUE/STATUS.md:426,440`
  - `AGENTS/CARL/workbook/KB.tsv`
  - `AGENTS/BROCK/STATUS.md:106`
  - `AGENTS/BROCK/domain/sources/{Q2_MARKS_WINDOW_PREP_JUL17,CCLFX_WATCH_JUL17}.md`
- **Reproduce the classification:**
  1. Extract each report's first `## Key Finding|Bottom line|Answer|Verdict|Summary|Headline` section, whitespace-collapsed, citations stripped, cut at 700 characters.
  2. Apply Appendix A.
  3. Compute agreement and kappa over the five outcome codes.

## Process Report
**Work:**
- DEWEY coded all 93 rows before reading the blind rater's file.
- A blind Opus rater worked from the rubric and headlines only (4 tool calls).
- The downstream traces ran by grep across recipient records and git history.
- One original report (R53) was re-read where the reviewer's question bore on it.

**Corrections to DEWEY's own 2026-10-23 synthesis, made here:**
1. "Risk is migrating" → "observability gap" (no time series shown).
2. "~50 of 80 deflated" → 49–57% of 67–69, two raters.
3. NVIDIA $164.5B restated with the original report's contingency caveats.
4. The charged-off cohort restated: debt buyers are beating their own forecasts; "stopped paying" was an inference.

**Data gaps:** REGINALD's FHA/VA kill commit; uptake for the other 88 reports; any lead/lag test against TERRY's warnings.
**Confidence:** see header.
**Suggestions:**
- Add a "no headline verdict" code and a "reassuring hypothesis" rule to the rubric before any rerun.
- Record caveat-carriage as part of WALTER's ledger audit: when a consumer adopts a finding, does its KB row keep the report's bounding caveat?

---
## Appendix A: rubric (verbatim, as given to both raters)
Primary outcome (exactly one):
- CONFIRMED: the commission's concern/premise held up or got worse (stress real, larger, earlier, or the hypothesis survived a test).
- DEFLATED: the concern came back smaller, narrower, slower, more concentrated, not-yet, or refuted.
- MIXED: the headline explicitly splits — one material part confirmed and one material part deflated (e.g. "credit loss absorbed, but liquidity drain real").
- NULL: the question could not be answered from public data; the main result is that the deciding fact is unavailable or unresolved.
- DESCRIPTIVE: no alarming premise was being tested (a catalog, a structure map, a document pull, a base-rate table with no prior claim to test, or a design/tooling question).

Secondary flag (Y/N): PREMISE_NUMBER_WRONG = the headline says a number or framing in the commission's premise was itself wrong (stale vintage, wrong denominator/label/definition, misread source, measurement-window artifact).

Rules: judge only what the headline says; do not use outside knowledge of later events. If unsure between two codes, pick the one the headline's first sentence supports and set confidence=low. Rows dated 2026-02-28 predate the current spec; classify them anyway.

## Appendix B: per-row classification
| id | date | question | commission | DEWEY | blind | blind conf | blind reason | agree |
|---|---|---|---|---|---|---|---|---|
| R01 | 2026-02-28 | WAL base case | — | DESCRIPTIVE | DESCRIPTIVE | low | Market snapshot base case; no premise tested in headline | ✓ |
| R02 | 2026-02-28 | Block fintech contagion | — | DESCRIPTIVE | DESCRIPTIVE | low | Margin/revenue mechanics; headline does not address contagion question | ✓ |
| R03 | 2026-02-28 | Block layoff analyst reaction | — | DESCRIPTIVE | DESCRIPTIVE | high | Event and analyst-reaction summary | ✓ |
| R04 | 2026-02-28 | Iran / Hormuz oil | — | DESCRIPTIVE | DESCRIPTIVE | high | Quantification table of Hormuz volumes | ✓ |
| R05 | 2026-02-28 | Military economic timing | — | DESCRIPTIVE | DESCRIPTIVE | low | Historical pattern list; no specific claim tested | ✓ |
| R06 | 2026-02-28 | WAL Stupin / Cantor | — | DESCRIPTIVE | DESCRIPTIVE | low | Narrative of fraud incident; no verdict on concern | ✓ |
| R07 | 2026-06-21 | S-FL → FL-bank loss-transmission timing | none (WALTER Prompt A) | CONFIRMED | CONFIRMED | high | Timing defensible; leading edge earlier, already flickering | ✓ |
| R08 | 2026-06-27 | AI-infra circular/vendor financing (incl. Athene insurer leg) | REQ-DEWEY-20260627-001 / SIG-W-20260627- | CONFIRMED | CONFIRMED | high | Vendor financing pervasive, confirmed by primary deal terms | ✓ |
| R09 | 2026-06-27 | Ex-AI-capex real GDP decomposition (is "ex-AI contracting" real?) | REQ-DEWEY-20260627-002 / SIG-W-20260627- | DEFLATED | DEFLATED | high | Contraction claim not reproducible; superseded GDP vintage; ex-AI positive | ✓ |
| R10 | 2026-06-27 | US residential housing distress — inflecting or normalizing? | REQ-DEWEY-20260627-004 | MIXED | MIXED | low | Inflecting on rate-of-change, normalizing on level; surge is vintage artifact | ✓ |
| R11 | 2026-06-27 | US state & local (muni) fiscal stress — where/how severe + data-center question | REQ-DEWEY-20260627-003 / SIG-W-20260627- | DEFLATED | DEFLATED | high | Concentrated not systemic; $1.03T burden mis-framed as debt | ✓ |
| R12 | 2026-07-02 | June HY/CCC widening decomposition — DISH index mechanics, sector drivers, AI-capex holder base | REQ-DEWEY-20260702-001 (Batch-2 #05) | CONFIRMED | CONFIRMED | low | Widening genuine, not DISH artifact; DISH-left claim false | ✓ |
| R13 | 2026-07-02 | Hormuz reopening scorecard — institutional + physical + base-rate | REQ-DEWEY-20260702-002 (Batch-2 #06) | CONFIRMED | CONFIRMED | low | Reopening stalled/reversed; fleet figures unverified rather than wrong | ✓ |
| R14 | 2026-07-09 | Energy HY OAS — un-blind the paywalled trip from public primaries | REQ-DEWEY-20260702-006 (Batch-2 #10) | DEFLATED | DEFLATED | high | Energy OAS 164bps, no threshold crossed; cited 285bps contradicted | ✓ |
| R15 | 2026-07-09 | CoreWeave / neocloud AI-credit — capital structure + transmission map | REQ-DEWEY-20260704-018 (Batch-2 #18) | DESCRIPTIVE | DEFLATED | low | Slide reads idiosyncratic; tripwire is contract cancellation | ✗ |
| R16 | 2026-07-09 | Funding-seizure pre-emption gate for the HY>280 X1 trigger | REQ-DEWEY-20260702-003 (Batch-2 #07) | CONFIRMED | CONFIRMED | high | Yes, trigger needs funding pre-emption gate | ✓ |
| R17 | 2026-07-10 | Japan super-long JGB demand — forced-seller SIGN + marginal-buyer map | REQ-DEWEY-20260702-004 (Batch-2 #08) | DEFLATED | MIXED | high | Net demand-positive under ESR, but forced-seller survives on J-GAAP | ✗ |
| R18 | 2026-07-10 | Food-supply shock stack — fertilizer verification + Apr-Jun produce audit for the 7/14 CPI fork | REQ-DEWEY-20260702-007 (Batch-2 #11) | DEFLATED | MIXED | low | Inputs disinflationary, but two live upside tails prevent stand-down | ✗ |
| R19 | 2026-07-10 | Criticized-credit migration — FFIEC tier pull + leading-bucket→NCO conversion base rates | REQ-DEWEY-20260702-009 (Batch-2 #13) | DEFLATED | DEFLATED | high | Creep real but concentration-driven, not broad | ✓ |
| R20 | 2026-07-16 | Bank exposure to private-credit vehicles — fund-finance sizing, XPV syndicate, Atlas SP, CCLFX  | REQ-DEWEY-20260702-010 (Batch-2 #14) | DEFLATED | DEFLATED | low | Bank leg quantitatively small; counter-evidence to Stage-3 premise | ✓ |
| R21 | 2026-07-16 | Repo market calm-vs-stressed during the SVB window (Mar 9-16 2023) — adversarial disconfirmatio | (07b funding-gate calibration follow-up) | DEFLATED | CONFIRMED | low | Calm-repo hypothesis survived active disconfirmation attempt | ✗ |
| R22 | 2026-07-16 | Credit spreads March 2023 — ICE BofA HY/IG OAS daily, SVB-window lead/lag | — | DESCRIPTIVE | DESCRIPTIVE | low | Daily spread history recovered; lead/lag timing described | ✓ |
| R23 | 2026-07-16 | Funding-seizure gate CALIBRATION — Mar-2020/Mar-2023 generalization + false-positive rate | PROME prompt 07b (parent: REQ-DEWEY-2026 | DEFLATED | DEFLATED | high | Gate does not generalize; fails both tested episodes | ✓ |
| R24 | 2026-06-26 | Florida Nov-3-2026 property-tax constitutional amendment | WALTER DEWEY_PROMPT_B (Will: 'DEWEY Prom | DESCRIPTIVE | DESCRIPTIVE | high | Header-only document/legislative research | ✓ |
| R25 | 2026-07-16 | SVB / March-2023 primary-source sequence verification (Barr Review) | (07b funding-gate calibration sub-leg) | DESCRIPTIVE | DESCRIPTIVE | high | Primary-source verification corrects $42B and 80% figures | ✓ |
| R26 | 2026-07-16 | BDC arms-length sub-90c print hunt — BRK-25 adjudication (rating actions + secondary pricing +  | REQ-DEWEY-20260702-012 (Batch-2 #16) | DEFLATED | DEFLATED | high | BRK-25 does not fire; 0.85 was price/NAV misread as bid | ✓ |
| R27 | 2026-07-20 | Insurance-wrapped private credit — UBS/Nationwide $500M CFO deal + wrap wave + pre-mortem tripw | SIG-W-20260720-001 (WALTER Phase-2.8) | CONFIRMED | DEFLATED | low | Deal confirmed but systemic risk still pre-mortem, not event | ✗ |
| R28 | 2026-07-20 | Insurer-lender double-jeopardy map of the 5 gated funds (BCRED/ADS/Monroe/CCLFX/North Haven) —  | REQ-DEWEY-20260702-013 (Batch-2 #17) | NULL | NULL | high | Map cannot be populated from public data | ✓ |
| R29 | 2026-07-20 | Mechanical-selling cushion into 7/22-31 earnings cluster — CTA levels + levered-ETF quantum + 0 | REQ-DEWEY-20260702-008 (v2, Batch-2 #12) | NULL | NULL | high | Mechanical cushion cannot be quantified from public data | ✓ |
| R30 | 2026-07-24 | FHA/VA loss-absorption waterfall + Ginnie nonbank-servicer stress map | REQ-DEWEY-20260702-011 (Batch-2 #15) | MIXED | MIXED | high | Explicit split: credit loss absorbed, liquidity drain real | ✓ |
| R31 | 2026-07-24 | China-strategic-exhaustion P0: did US/SDI spending actually bankrupt the USSR? (analog audit) | (none - fresh Will ask) | DEFLATED | DEFLATED | high | Founding SDI-bankruptcy metaphor largely a myth | ✓ |
| R32 | 2026-07-24 | China-strategic-exhaustion P1: does PRIVATE US AI capex transmit to US sovereign/macro damage? | (none - fresh Will ask) | DEFLATED | DEFLATED | high | Sovereign transmission chain fails at transmission step | ✓ |
| R33 | 2026-07-24 | China-strategic-exhaustion P3 (DEWEY carve-out): China fiscal/LGFV + state-AI-financing primari | (none - Will-directed Batch-3 P3 carve-o | CONFIRMED | CONFIRMED | high | Numbers support direction-flip premise | ✓ |
| R34 | 2026-07-24 | China-strategic-exhaustion P2 (DEWEY carve-out): efficiency asymmetry - DeepSeek real TCO + US/ | (none - Will-directed Batch-3 P2 carve-o | MIXED | DEFLATED | low | Both headline framings wrong, though each hides real signal | ✗ |
| R35 | 2026-07-24 | Score-cascade attribution — does student-loan delinquency CAUSE the CC 90+ GFC breach? (CRL-05) | CARL slate T1-1/C2 (STUE-proposed, Will- | DEFLATED | DEFLATED | low | Breach plausible but not from SL cascade; denominator shrink drives rise | ✓ |
| R36 | 2026-07-24 | STR/rental data-vendor & metrics catalog (+ how to read the signal) — Airbnb thread Run 1 (tool | (none - Will-directed Airbnb thread, Run | NULL | DESCRIPTIVE | high | Vendor/metrics catalog (tooling) | ✗ |
| R37 | 2026-07-24 | FL coastal STR-host net-yield overlay — assessment-driven forced-sale channel? — Airbnb thread  | (none - Will-directed Airbnb thread, Run | MIXED | MIXED | high | Squeeze real; distinct STR channel only partially supported | ✓ |
| R38 | 2026-07-24 | Oversupplied US STR markets — ranked national catalog (~60 metros, 4-tier) — Airbnb thread Run  | (none - Will-directed Airbnb thread, Run | DEFLATED | DEFLATED | low | Oversupply real but concentrated, bifurcating; catalog-like | ✓ |
| R39 | 2026-07-25 | PROMPT-19 SYNTHESIS — FHA/VA 'federally absorbed' KILL: 4-axis adversarial stress-test (canonic | REQ-DEWEY-20260724-019 | DEFLATED | MIXED | low | Kill survives/hardened but parent evidence falsified; one bank stays on | ✗ |
| R40 | 2026-07-25 | PROMPT-19 axis A — name-level FHA/VA + warehouse + servicing-advance exposure at BKU/SSB/AMTB/S | REQ-DEWEY-20260724-019 | DEFLATED | DESCRIPTIVE | low | Headline shows only setup/kill-check; no verdict visible | ✗ |
| R41 | 2026-07-24 | PROMPT-19 axis B — is the 11.47% MMI capital ratio deferral-flattered by partial claims? | REQ-DEWEY-20260724-019 | MIXED | MIXED | high | Deferral real and growing, framing corrected, but kill survives on magnitude | ✓ |
| R42 | 2026-07-24 | PROMPT-19 axis D — MIP premium-cut self-erosion + VA partial-guaranty residual | REQ-DEWEY-20260724-019 | DEFLATED | DEFLATED | high | No MIP-cut threat; historical premise wrong | ✓ |
| R43 | 2026-07-28 | Phantom consumer debt magnitude — turn CARL's '$150-400B' into a number (bottom-up by component | (none - CARL slate T1-3 PHAN-proposed, W | DEFLATED | DEFLATED | high | Credit-only phantom debt order of magnitude smaller; 20-30% unsupported | ✓ |
| R44 | 2026-08-02 | AI-credit guarantee web — who bears credit risk, cross-links, and what binds first (WALTER DR-1 | REQ-DEWEY-20260731-001 | MIXED | MIXED | low | Headline $250B guarantee unfiled; but rating threshold already crossed | ✓ |
| R45 | 2026-08-02 | Interceptor-inventory economics — is interceptor supply binding in WEEKS or YEARS? (WALTER DR-3 | REQ-DEWEY-20260731-003 | CONFIRMED | CONFIRMED | high | Formulation correct; magazine weeks vs replenishment years | ✓ |
| R46 | 2026-08-02 | Hyperscaler depreciation schedules — how much EPS came from useful-life extensions, and what re | REQ-DEWEY-20260731-002 | CONFIRMED | CONFIRMED | high | Reversion no longer hypothetical; Amazon shortened lives | ✓ |
| R47 | 2026-08-12 | C3 — masking-duration base rates: how long can clean surfaces last, and what is the tell? (CARL | CARL-C3 (CARL-direct commission; no WALT | DEFLATED | DEFLATED | high | Masking signature mostly mechanical; unmaskable flow flat | ✓ |
| R48 | 2026-08-12 | European energy aggregate baseline — storage trajectory, LNG impairment, and the TTF 'puzzle' ( | REQ-DEWEY-20260731-004 | CONFIRMED | CONFIRMED | low | Falling-TTF puzzle is window artifact; picture worse | ✓ |
| R49 | 2026-08-12 | LNG as a target class — kinetic-event reaction functions and who absorbs the loss (WALTER DR-5) | REQ-DEWEY-20260731-005 | DEFLATED | CONFIRMED | low | Non-transmitting hypothesis confirmed on both benchmarks | ✗ |
| R50 | 2026-08-13 | Recognition-artifact census — quantifying the loss-recognition-deferral wedge (CARL-DR-1) [ONE- | CARL-DR-1 (CARL-direct commission; no WA | MIXED | MIXED | high | Wedge below kill and not widening; deeper concessions, worse outcomes | ✓ |
| R51 | 2026-08-27 | CRMT covenant expiry — who decides at the Silver Point waiver expiry, and what each outcome cas | REQ-DEWEY-20260731-006 | CONFIRMED | CONFIRMED | high | Checkpoint sharper and earlier; fleet date wrong | ✓ |
| R52 | 2026-08-27 | FHA partial-claims leg — the deferral wedge went into reverse (CARL-DR-1 re-commission, Will-ap | CARL-DR-1 leg 2 of 6 (CARL-direct commis | CONFIRMED | CONFIRMED | low | Process change: reported delinquency rose as exits slowed | ✓ |
| R53 | 2026-08-28 | Where did the charged-off borrowers go — the exited cohort stopped paying voluntarily (CARL-DR- | CARL-DR-2 (CARL-direct commission, Will- | CONFIRMED | CONFIRMED | high | Charged-off cohort stopped paying voluntarily | ✓ |
| R54 | 2026-09-02 | Is the AI order book carrying phantom demand? (WALTER DR REQ-001 — NVDA supply commitments, tur | REQ-DEWEY-20260829-001 | MIXED | DESCRIPTIVE | low | Headline is header/erratum only; no verdict visible | ✗ |
| R55 | 2026-09-10 | How much of NVDA's growth does NVDA's own balance sheet underwrite - vendor financing and reven | REQ-DEWEY-20260829-002 | CONFIRMED | CONFIRMED | low | Support ballooned, protection degraded; revenue share not computable | ✓ |
| R56 | 2026-09-24 | Grocery-volume decline: POLICY vs CYCLE vs MEASUREMENT ARTIFACT + standing food-demand agent ve | CARL-DR-5 (CARL-direct 2026-08-15, Will- | DEFLATED | DEFLATED | high | Measurement/substitution artifact; panel figure not matched by BEA | ✓ |
| R57 | 2026-09-27 | Nano Banc failure (9/25) — primary documents: DFPI/Fed orders, FDIC terms, MLR, arbitration + b | PROME-17a205519 (no WALTER flag) | DESCRIPTIVE | DESCRIPTIVE | high | Primary document pull | ✓ |
| R58 | 2026-10-01 | What prices the 2026 consumer-discretionary cross-section - AZO/ORLY factor attribution + cohor | CARL-DR-3 (no REQ id) | DEFLATED | DEFLATED | high | Style effect plus AZO stall, not consumer-cohort effect | ✓ |
| R59 | 2026-10-12 | DR-4 EU gas storage rerun for HANS HNS-07 | HANS-HNS-07 / PROME-L566 | DESCRIPTIVE | CONFIRMED | low | Refreshed storage instrument on MISS side of 80% line | ✗ |
| R60 | 2026-10-10 | Russia diesel deal vs strikes - session1 partial/pre-registration | REQ-DEWEY-20261010-001 | NULL | NULL | low | Instrument real; net supply not yet answered | ✓ |
| R61 | 2026-10-12 | Russia diesel net supply - instruments, plans, outage evidence and matched news reaction | REQ-DEWEY-20261010-001 | MIXED | MIXED | low | Real channel opened, overturns reshuffle premise; delivery unproven | ✓ |
| R62 | 2026-10-12 | CARL-DR1 card FDM disclosures - Q2 COF/SYF/BFH | CARL-DR-1 / PROME-L567 | DESCRIPTIVE | NULL | low | Balances disclosed; counterfactual needed to score kill unavailable | ✗ |
| R63 | 2026-10-13 | Diesel delivered supply and primary-document checkpoint | REQ-DEWEY-20261010-001 | NULL | NULL | high | No additional delivery authenticated; evidence limit | ✓ |
| R64 | 2026-10-13 | FINAL October14 diesel commission - bounded cargo/implementation completion | REQ-DEWEY-20261010-001 | NULL | NULL | high | Delivered net addition unresolved | ✓ |
| R65 | 2026-10-14 | PORTS-Pike executed power rights and payment bridge | Will-approved WALTER PORTS-Pike candidat | DEFLATED | NULL | low | Only study agreement found; project agreements unknown | ✗ |
| R66 | 2026-10-14 | Nano Banc P&A publication and document-boundary check | Will direct / PROME DOCKET L516 | NULL | NULL | low | P&A not published; absence not proof | ✓ |
| R67 | 2026-10-17 | Keeper thinking-companion design research (CATO 5-question brief) | Will direct 13:16 ET (CATO brief) | DESCRIPTIVE | DESCRIPTIVE | high | Design research brief | ✓ |
| R68 | 2026-10-22 | GENIUS Act stablecoin rewards and regional-bank deposit flight | REQ-DEWEY-20261022-002 | DESCRIPTIVE | DESCRIPTIVE | low | Rule mechanics described; deposit-flight question unresolved in headline | ✓ |
| R69 | 2026-10-22 | US bank technology-vendor concentration and AI-agent/cyber risk | REQ-DEWEY-20261022-001 | CONFIRMED | MIXED | low | Concentration real; no compromise, loss, or run observed | ✗ |
| R70 | 2026-10-22 | New World screwworm: cattle supply, beef prices and food CPI | REQ-DEWEY-20261022-004 | DEFLATED | DEFLATED | high | Screwworm not in beef prices; small CPI effect | ✓ |
| R71 | 2026-10-22 | Data-center ABS and CMBS: size, tenants and holders (v2 COMPLETE; v1 PARTIAL in git) | REQ-DEWEY-20261022-007 | DEFLATED | DEFLATED | low | Clean credit record; stress narrower, market access only | ✓ |
| R72 | 2026-10-22 | Hyperscaler AI capex vs cash flow, and IG bond capacity | REQ-DEWEY-20261022-005 | CONFIRMED | CONFIRMED | low | All five run funding gaps filled by bonds | ✓ |
| R73 | 2026-10-22 | The 1984-88 Tanker War as a base rate for the 2026 Gulf tanker campaign | REQ-DEWEY-20261022-006 | DESCRIPTIVE | DESCRIPTIVE | high | Historical base-rate table | ✓ |
| R74 | 2026-10-22 | Rising bad loans with falling reserve coverage: does it predict bank losses? | REQ-DEWEY-20261022-003 | DEFLATED | DEFLATED | high | Pattern shows no lift at asked horizon | ✓ |
| R75 | 2026-10-22 | Cyber wave ("Black October") as a systemic market event: base rates from 5 waves | REQ-DEWEY-20261022-008 | DEFLATED | DEFLATED | high | No past wave caused run, failure, or payment outage | ✓ |
| R76 | 2026-10-22 | Regional/community bank legacy technology and exposure to the Oct 2026 cyber wave | Will direct (plan 15:25, go 15:47 ET) | DEFLATED | DEFLATED | high | Legacy tech widespread but not the breach vector | ✓ |
| R77 | 2026-10-22 | Bank technology vendors: incident record, Oct 2026 wave exposure, financial strain | Will direct (17:04 ET) | DEFLATED | MIXED | low | Clean major record, but steady smaller incidents | ✗ |
| R78 | 2026-10-22 | Bank-vendor products vs the product classes failing in the Oct 2026 wave | Will direct (17:31 ET) | DEFLATED | DEFLATED | high | Bank products share no traits of failing classes | ✓ |
| R79 | 2026-10-22 | Regional-bank software by product (FIS IBS, Fiserv, Jack Henry, Q2) and the 10/22 AI-exploit st | (none - Will-directed in DEWEY session) | DEFLATED | DEFLATED | low | None in KEV, no bank compromise; coverage thin | ✓ |
| R80 | 2026-10-22 | CYPHER escalation-watch legs: Dutch NCSC and Patchstack primaries, PHP2Shell victim sweep, NYDF | (none - CYPHER live-session request unde | DEFLATED | DEFLATED | high | Row stays NOT-FIRED, attempts only | ✓ |
| R81 | 2026-10-22 | TruStage (credit-union vendor, ex-CUNA Mutual) cyberattack identified 11 Jul 2026: data taken,  | SIG-W-20261022-043 (open questions; Will | NULL | NULL | high | Three of four questions unanswered at primary | ✓ |
| R82 | 2026-10-22 | Japan financial-firm PHP2Shell service suspensions (MUFG, Mizuho, Shizuoka, Nomura): precaution | (none - Will-directed; WALTER candidate  | DEFLATED | DEFLATED | low | Precaution, no compromise reported; not ruled out | ✓ |
| R83 | 2026-10-22 | Is AI making exploitation faster? CVE-to-KEV lag 2022-2026, NVD CVE volume, AI-found bank-vendo | (none - Will-directed; WALTER candidate  | DEFLATED | MIXED | high | Volume surging, exploitation speed flat | ✗ |
| R84 | 2026-10-22 | eMudhra key compromise: Chrome 27 Oct root removal vs non-browser financial software (Java, Win | (none - Will-directed) | DEFLATED | DEFLATED | high | Chrome-only event; other trust stores already acted | ✓ |
| R85 | 2026-10-22 | State-backed cyber exclusions: does government attribution let insurers deny claims (LMA5564A-5 | (none - Will-directed) | DEFLATED | DEFLATED | high | Attribution alone would not allow most denials | ✓ |
| R86 | 2026-10-22 | ICBC FS ransomware Nov 2023 as a Treasury-settlement instance (CYPHER FL-CYP-06) | (none - Will-directed) | MIXED | MIXED | high | Confirmed at participant level, contained at market level | ✓ |
| R87 | 2026-10-23 | MSP / shared-IT-tool (ConnectWise) channel into US credit unions and community banks: reach, pr | REQ-DEWEY-20261023-001 | MIXED | MIXED | low | Wide reach but little observed traffic, poorly observed | ✓ |
| R88 | 2026-10-23 | HY widening Aug-Oct 2026: AI-concentrated or broad (ICE sector OAS, HYG basket, exchange-quote  | REQ-DEWEY-20261023-002 | DEFLATED | DEFLATED | low | Mostly broad; AI hot spot too small to drive index | ✓ |
| R89 | 2026-10-23 | CCC bonds and below-80 leveraged loans split three ways (AI builders / software-AI-disruption / | REQ-DEWEY-20261023-003 | MIXED | MIXED | high | CCC damage non-AI; loans tech heavily over-represented | ✓ |
| R90 | 2026-10-23 | Is the US HY issuance window shut in October 2026, who is locked out (pulled deals, substitutio | (none - Will-directed thread 1) | DEFLATED | DEFLATED | high | Window narrowed and expensive, not shut | ✓ |
| R91 | 2026-10-23 | What replaced NCUA's vendor-examination authority request (FSOC 2025 'information sharing agree | (none - Will-directed thread 3) | CONFIRMED | NULL | low | No document for replacement mechanism found | ✗ |
| R92 | 2026-10-23 | CCC concentration: is October's CCC widening a few telecom restructurings (Optimum/CSC, Altice) | (none - Will-approved slate #1, follow-o | MIXED | CONFIRMED | high | Concentrated in cable/telecom/media, no AI | ✗ |
| R93 | 2026-10-23 | South Korea 16-firm financial breach (FSC 10/14): facts and the AI-agent (ARTEX) claim | (none - Will-approved slate #3; CYPHER C | DEFLATED | DEFLATED | high | AI role vendor-attributed, unconfirmed; no speed effect | ✓ |
