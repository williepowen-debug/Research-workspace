# Criticized-credit migration — FFIEC tier pull + leading-bucket→NCO conversion base rates
**Date:** 2026-07-10 | **Mode:** Thesis | **Confidence:** High (Q1 data, primary + reconciled) / Medium (base rate directional; forward-conversion call)
**Flag:** REQ-DEWEY-20260702-009 (Batch-2 #13) | **Feeds:** REGINALD (V1 falsifier un-blind; REG-24/25), RED (CHG-RED-040; WAL/OZK beat/miss tree), CORAL/OZK/TERRY (info)

> *Delivered 2026-07-10 (completed after a mid-run session-limit interruption; fan-out resumed from cache, leg-1 bank pull re-run — both legs now complete).*
> **Freshness re-anchor (docket):** WAL & OZK Q2 prints are **7/21 AMC** (not the prompt's "~7/16") — single-day triple w/ ALLY. OZK's Seattle U-District deed-in-lieu (recorded wk-7/2) is a **Q3 subsequent event** → the 7/21 Q2 print shows the *specific-reserve build* vs REGINALD's pre-registered **$15-30M fail-band** ($20M mid already in the $628.5M ACL). This run grades **Q1 state + base rates** so the 7/21 Q2 prints can be graded live.

## Key Finding
The Q1-2026 un-blind shows the leading criticized creep is **REAL but concentration-driven, not a broad tier-wide surge** — **OZK is the standout** (a few large RESG office/condo/hotel credits drove 30-89 past-due +184% and Substandard +32%, migrating into nonaccrual while special-mention fell = real progression — but idiosyncratic single-large-credit, and OZK *released* reserves into it); **WAL** posted a genuine special-mention build (+24% to $403M, reconciliation confirmed) with no classified conversion yet; **EGBN/SBCF** show modest office-adjacent nonaccrual creep; **BKU is improving.** Against the base rate — a one-quarter criticized surge **predominantly reverts at the aggregate level, but the tail is where concentrated names fail**, and the master discriminators are driver-reversibility (secular office = worse), office-concentration, reserve build, and breadth — the two yellow flags are **OZK's secular-office RESG concentration** and the **cohort-wide reserve RELEASES** (only WAL built); the mitigant is that OZK's surge is a few lumpy credits, not broad. **Net: RED's early edge (CHG-RED-040) has real support at the concentrated names but reads idiosyncratic-concentration, not broad-tier.** NCOs lag, so a clean Q2 NCO beat would NOT falsify the bear; the 7/21 prints test whether OZK's RESG credits convert (the deed-in-lieu is the Q3 realization) and whether the reserve releases reverse.

---

## Required sub-answers (completeness-critic checklist)

| # | Sub-question | Status | Where |
|---|---|---|---|
| 1 | **FFIEC/10-Q data pull** — Q1-2026 special-mention / classified / 30-89d CRE buckets + QoQ vs Q4-25 for WAL/OZK/EGBN/BKU/SBCF | ✅ CONFIRMED (primary 10-Q/FDIC) | §(1) |
| 1b | **WAL reconciliation** — confirm/correct 10-Q Special Mention $403M / Classified $947M; un-blind the MI3 line | ✅ $403/$947 CONFIRMED exact; **MI3 not a 10-Q line** | §(1) |
| 2 | **Base rate** — how often does a ≥20-25% QoQ special-mention/criticized/30-89d surge CONVERT to NCOs within 1-2Q vs REVERT? (GFC / 2015-16 energy / 2023) | ✅ (fan-out, full synthesis) | §(2) |
| 2b | **Discriminating features** — bucket breadth, single-vs-multi-credit, reserve build, appraisal timing, quarter-end lumpiness, office share | ✅ (fan-out) | §(2) |

**Decision outputs owed:** adjudicate CHG-RED-040 (RED vs REGINALD/CORAL); re-grade REG-24 (70%) / REG-25 (75%); pre-position RED's WAL/OZK beat/miss tree (beat-clean cuts RED 69→62); un-blind REGINALD's V1 Bear-fast falsifier (dark 5+ wks).

---

## Evidence

### (1) Q1-2026 criticized-credit data pull — cohort BIFURCATED, concentration-driven not broad  *(DEWEY primary)*
As-of 2026-03-31 vs 2025-12-31; $M. Source: SEC 10-Qs (WAL/EGBN/BKU/SBCF); **OZK via FDIC cert #110** (deregistered from SEC 2017 — not on EDGAR).

| Bank | Special Mention (QoQ) | Classified¹ (QoQ) | 30-89 past-due total (QoQ) | Nonaccrual signal | ACL (QoQ) |
|---|---|---|---|---|---|
| **WAL** | **$403 (+$78, +24%)** | $947 (−$3, flat) | $251 (−$2) | Other-CRE non-OO NA $263 (+$35) | $461.1 (**+$0.5 build**) |
| **OZK** | $397.4 (−$23.9) | **$663.3 (+$161.3, +32%)** | **$408.1 (+$264.4, +184%)** ⚠️ | 60-89 incl NA $181.1 (vs $5.6); CRE 30-89 $344.6 (**+533%**) | $628.5 (**−$3.4 release**) |
| **EGBN** | $290.8 (+$21.9) | $447.6 (−$66.9) | $18.0 (−$31.9) | Nonaccrual $128.8 (+$21.9), IPCRE-led | $147.2 (**−$12.4 release**) |
| **BKU** | $177.9 (+$2.9) | $874.5 (−$149.0) | $234.6 (−$16.0) | CRE Substandard $492.6 (−$91) | $208.8 (**−$11.0 release**) |
| **SBCF** | $136.7 (−$26.4) | $220.1 (+$26.7, +14%) | $28.2 (−$4.7) | Nonaccrual $95.0 (+$23.0), CRE-OO-led | $176.3 (−$2.6) |

¹ WAL reports a single combined "Classified"; OZK/EGBN/BKU/SBCF = Substandard+Doubtful summed. **WAL reconciliation CONFIRMED exact** ($403 SM / $947 Classified, cross-foots Pass+SM+Classified−hedge = $59,142 total). **"MI3" line NOT PRESENT** in WAL's Q1-2026 10-Q (exhaustive grep) — un-blinds REGINALD's V1 falsifier: the MI3 figure is **not a 10-Q disclosure item** (likely an earnings-supplement/desk metric), so the "5+ weeks overdue FFIEC MI3" is chasing something that isn't in the filing.

**Read — the leading creep is REAL but CONCENTRATION-driven, NOT a broad tier-wide surge:**
- **OZK = the standout.** Past-due +184% / CRE past-due +533% / Substandard +32%, migrating INTO nonaccrual while SM FELL (= credits moving *through* SM into classified = real progression, not curing — discriminator #2). BUT driven by a **few large RESG credits** (4 substandard-accrual $326.9M + 4 nonaccrual $240.2M; office/condo/life-science/hotel) = **single-large-credit / lumpy** (discriminator #4 → less-systemic-signal, idiosyncratic), and it's the **secular office/CRE** channel (discriminator #1 → may not revert). And OZK **released** reserves into it (discriminator #3 → the concerning direction). *(Ties to the docket: OZK's Seattle deed-in-lieu is a Q3 event; the 7/21 Q2 print shows the specific-reserve build vs REGINALD's $15-30M fail-band.)*
- **WAL = a genuine SM build** (+24% to $403M) but classified flat and NCOs ≈ provision — a *leading-bucket* build with no conversion yet (base-rate-consistent: the leading tell fires before NCOs).
- **EGBN / SBCF = modest nonaccrual creep** (IPCRE / CRE-OO — the office-adjacent buckets) against improving/mixed classified.
- **BKU = improving** (Classified −$149M).
- **Cohort-wide reserve RELEASES** (OZK −3.4, EGBN −12.4, BKU −11, SBCF −2.6; only WAL a token +0.5): banks are NOT provisioning alongside the deterioration — per discriminator #3 a yellow flag (or benign confidence, per the contested extend-and-pretend read). ⚠️ **Office is NOT separately tagged** by any of the five (embedded in IP/non-OO CRE) — the office-specific breakout the base rate says matters most is not disclosed at loan-class level.

### (2) Conversion-vs-reversion base rates + discriminating features  *(fan-out, 109 agents, 21 confirmed / 4 refuted, full synthesis)*
**Base rate — at AGGREGATE level a one-quarter criticized/classified surge PREDOMINANTLY REVERTS or is absorbed rather than converting to institution-threatening NCOs — PROVIDED the driver is a reversible macro/commodity condition AND management builds reserves. BUT the aggregate revert story MASKS the concentrated-bank tail where names actually fail — so it does NOT extend to a single concentrated name.**
- **2015-16 energy (cleanest quantified "reverts" case):** the SNC criticized surge peaked 2016-17 then fell **−29.4% YoY to 2018** ($417.6B→$294.9B; classified −36.2%, non-accruals −38.2%) "largely because of improving economic conditions in the oil and gas sectors"; aggregate CRE NCOs stayed **~0.20% throughout** (0.20% 2015:Q4 → 0.07% 2016:Q4); no widespread failures [PRIMARY: OCC SNC 2018, Dallas Fed]. Yet the surge was **real and violent at concentrated names** (O&G classified 0.7%→15.2% in one year ~20x; energy-bank NPL +50% vs peers) — reverted in aggregate, genuine at the tail.
- **GFC (aggregate ceiling):** aggregate commercial-bank CRE NCO peaked **~2.80% annualized (2009:Q4)** — even the worst episode converted only a low-single-digit fraction at system level [PRIMARY: FRED CORCREXFACBS]. **Explicitly masks the regional-bank tail where concentrated banks FAILED.**
- **⚠️ Honest limit (load-bearing caveat):** **no single source gives a clean "X% of one-quarter special-mention surges convert within 2 quarters" statistic** for a CRE-concentrated *regional-bank* reference class — the base rate is *directional/assembled* from aggregate NCO series + SNC YoY reversions + sector-concentration (mostly C&I/energy) analogs. And historical base rates are largely **cyclical/commodity**; they may **NOT transfer to a SECULAR office-demand shock** (the 2023-onward structural remote-work channel).

**Discriminating features — real build vs revert/noise (empirically supported):**
1. **Driver reversibility — the master discriminator.** Macro/commodity-conditioned migration reverts when the sector recovers (2015-16 energy). A **secular office-demand impairment may NOT revert** — flagged explicitly as a fundamentally different channel [PRIMARY: OCC SNC 2018 mechanism].
2. **Office-specific vs broad CRE.** The 2023 bank CRE-NPL rise was "almost wholly attributable to **office** loans" at large banks; composition (office share + loan size) explains **70-80%** of the large-vs-small-bank NPL gap; small-bank CRE "remained strong." "CRE cannot be viewed as a single strained asset class." [PRIMARY: FEDS 2024-072].
3. **Contemporaneous reserve/ACL build absorbs.** In episodes where losses materialized, management built reserves alongside — energy-bank provisions rose ~3x non-energy; TX provisions exceeded charge-offs [PRIMARY: Dallas Fed]. A criticized surge *with* an ACL build reads as recognized-and-absorbed; a surge *without* is the worry.
4. **Breadth vs single-large-credit / quarter-end lumpiness.** A broad multi-credit build reads real; a single-large-credit or appraisal-timed one-quarter jump is more likely lumpy noise. *(NB: OZK's Seattle deed-in-lieu is a single large credit — the lumpy, less-systemic-signal pattern.)*
5. **⚠️ Extend-and-pretend — CONTESTED, do NOT bank either way.** One side: less-capitalized banks are slower to classify distressed CRE → a LOW NPL reading can MASK deterioration (tighter capital ↔ smaller NPL ratios at $10-100B regionals) [NY Fed SR1130]. Counter: a May-2026 FEDS paper finds 2023 CRE extensions "predominantly address **temporary payment frictions**," not evergreening, and extended loans performed well [FEDS 2026-025, Glancy — single-author, counter-consensus, medium-conf]. The evidence is genuinely two-sided; treat a benign print at a capital-constrained regional as *ambiguous*, not decisive either way.

**Implication for the WAL/OZK Q2 (7/21) read (feeds RED beat/miss tree + REG-24/25):**
- The aggregate base rate leans **reverts/absorbs**, but that comfort **does NOT transfer to a CRE-concentrated single name** — the tail is where failures live. What decides WAL/OZK's path is the discriminators: **is the strain office-concentrated (real risk) or broad; reversible or secular; accompanied by an ACL build; broad or a single-large-credit (OZK's deed-in-lieu = the latter).**
- **NCOs LAG** — so a clean Q2 **NCO** beat does NOT falsify the bear (it's mechanically too early for conversion). The real leading tell is the **criticized/special-mention build** + its composition + the reserve response. RED's "beat-clean cuts 69→62" should be conditioned on WHICH metric beats: an NCO beat is near-mechanical; a criticized-bucket build is the signal.
- **Tempers REG-24/25:** the leading creep is signal-consistent, but the base rate says aggregate conversion is slow/partial and often reverts — so grade the Q2 prints on the *discriminators*, not the headline NCO. The extend-and-pretend read is contested, so don't lean on "benign = deferral" as hard as a one-sided view would.

---

## Counter-Evidence
- **For "reverts / idiosyncratic" (against the bear):** OZK's surge is a **few large RESG credits**, not a broad multi-credit deterioration — the base rate says single-large-credit/lumpy surges are the noise pattern, and aggregate criticized surges predominantly revert (2015-16: −29.4% YoY). BKU is *improving*; WAL's classified is flat; EGBN/SBCF classified is mixed. So the cohort is NOT uniformly deteriorating — this cuts against a broad tier-wide bear (supports the "idiosyncratic" read, consistent with prior WAL-bear-is-idiosyncratic framing).
- **For "converts / real" (against reversion):** OZK migrated *through* SM into classified+nonaccrual (real progression, not curing); the driver is **secular office/CRE** (the discriminator the base rate flags as possibly NOT reverting like a cyclical shock); and the **cohort-wide reserve releases** mean deterioration is not being provisioned — if the extend-and-pretend read (contested) is right, the benign classified prints understate the problem.
- **What would flip it:** the 7/21 OZK print showing the RESG credits convert to NCOs beyond the $15-30M fail-band, or the reserve releases reversing into builds (recognition); conversely, OZK curing the RESG credits or building reserves would confirm "idiosyncratic/absorbed."

## Source Quality Assessment
Leg 1 is **strong-primary** — SEC 10-Qs (WAL/EGBN/BKU/SBCF) + FDIC cert-#110 filings (OZK), every figure cross-footed, WAL reconciliation exact. Gaps: **office is not separately tagged** at loan-class level by any of the five (the base rate's most-important discriminator is undisclosed); past-due basis differs by filer (SBCF/OZK aging include vs exclude nonaccrual differently — cross-bank comparisons need care); EGBN/SBCF give no aggregate risk-rating total (summed from per-class sub-tables, cross-footed). Leg 2 base rate is **directional/assembled**, not a clean bank-level point statistic; much of the strongest quantified evidence is C&I/energy analog, and cyclical history may not transfer to the secular office shock (see §2 caveats). Fan-out: 21 confirmed / 4 refuted (some refutations were URL-mismatch, not substantive). *(Run completed across a session-limit interruption: fan-out resumed from cache, leg-1 bank pull fully re-run.)*

## References
- WAL Q1-2026 10-Q: SEC EDGAR acc 0001628280-26-033054 (filed 2026-05-11), Note 4 [PRIMARY]
- OZK Q1-2026 10-Q: FDIC securities-filings cert #110, filing id 11933 (filed 2026-05-06) [PRIMARY]
- EGBN 10-Q acc 0001050441-26-000066; BKU acc 0001504008-26-000043; SBCF acc 0001628280-26-031220 [PRIMARY]
- OCC Shared National Credit reviews 2018 + 2025: https://www.occ.gov/publications-and-resources/publications/shared-national-credit-report/ [PRIMARY]
- OCC Semiannual Risk Perspective Spring-2016: https://www.occ.treas.gov/publications-and-resources/publications/semiannual-risk-perspective/files/pub-semiannual-risk-perspective-spring-2016.pdf [PRIMARY]
- FEDS 2024-072 (office-specific CRE-NPL composition): federalreserve.gov FEDS Notes [PRIMARY/ACADEMIC]
- FEDS 2026-025 (Glancy — CRE extensions temporary-friction, counter-consensus): federalreserve.gov [ACADEMIC]
- NY Fed SR1130 (capital-driven CRE loss-deferral): https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr1130.pdf [PRIMARY/ACADEMIC]
- OFR Brief 24-04 (CRE NCO lag; 2023 PDNA +72%): https://www.financialresearch.gov/briefs/files/OFRBrief-24-04-bank-health-and-future-commercial-real-estate-losses.pdf [PRIMARY]
- FDIC 2025 Risk Review; Dallas Fed 2025/02; NY Fed Liberty St (2016 energy); FRED CORCREXFACBS (CRE NCO) [PRIMARY]

## Process Report
**Searches run:** 1 `/deep-research` fan-out for the base rates (109 agents, 6 angles, 26 sources → 25 verified, 21 confirmed / 4 refuted, ~7.5M tokens across the interrupted run + resume) + 1 DEWEY primary-pull agent for the 5-bank Q1 data (~141K tokens, 56 tool calls). **The run spanned a session-rate-limit interruption:** the first fan-out's synthesis + leg-1 pull were killed mid-flight; recovered by resuming the fan-out from cache (73 of 110 agents replayed, only the killed verify votes + synthesis re-ran) and re-spawning the leg-1 pull with a "return-partial-not-die" guardrail.
**Data gaps:** (1) **office not separately tagged** at loan-class level by any of the 5 banks — the base rate's key discriminator is undisclosed in the credit-quality tables; (2) no clean bank-level "X% convert within 2Q" base-rate statistic exists (directional/assembled); (3) WAL "MI3" is not a 10-Q line (so the "FFIEC MI3 overdue" blind is chasing a non-10-Q metric — flag to REGINALD).
**Source frustrations:** SEC 403s generic fetchers (browser-UA / edgar_doc.py workaround); **OZK is not on EDGAR** (SEC-deregistered 2017 → FDIC cert #110 filings, per `finding_fdic_securities_filings_api`); past-due-basis heterogeneity across filers complicates cross-bank comparison; the biggest operational hit was the **session rate limit** mid-run.
**Confidence in findings:** High on the Q1 cohort data (primary, reconciled, cross-footed); Medium on the base rate (directional; cyclical-history-may-not-transfer-to-secular-office caveat) and the forward-conversion call.
**If I had more time/tools:** pull the FFIEC call-report CRE past-due memoranda directly (bank-level office splits where the schedule carries them) to get the office breakout the 10-Qs omit; assemble a bank-level (not aggregate) conversion base rate from a panel of concentrated regionals across 2015-16/2023.
**Suggestions:** the workflow-mid-run rate-limit recovery (resume-from-cache + re-spawn the failed leg with a "return-partial" guardrail) worked cleanly and is worth an auto-memory. A `scripts/` FFIEC-call-report puller (CRE past-due memoranda + office where disclosed) would parallel `edgar_doc.py` for the recurring bank-credit runs → BACKLOG candidate.
