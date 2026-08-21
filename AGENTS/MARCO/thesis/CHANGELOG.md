# MARCO THESIS — CHANGELOG

Version-transition log. Newest first. Each entry: old view → new view, trigger, conviction deltas. Version bump rule: **major (X)** = structural change / conviction reversal / phase transition; **minor (Y)** = refinement.

---

## v3.0 → v3.1 (2026-07-31, session 19) — MINOR — **Channel 4 re-marked MEDIUM → MED-LOW and split along its own mechanism** *(Will-directed)*

**Trigger:** the same-day VX stale sweep froze 17 border-fiscal vectors, which surfaced that THESIS was carrying Channel 4 at MEDIUM on an evidence base nobody had touched since **February 2026**. Flagged as a decision rather than actioned unilaterally; Will directed the re-mark.

**The finding that shaped it — the channel bifurcates exactly where it matters.** Of Channel 4's **14 vectors, 2 are live and 12 are frozen**, and the split is not random:

| Leg | Vectors live | Conviction | Basis |
|---|---|---|---|
| **Flow** (remittances) | **2 / 2** — `2.08` Mexico, `REM-02` CentAm | **MEDIUM** (unchanged) | Maintained monthly off Banxico; May $5,611M +3.8% YoY, **transfer count −1.7% YoY** = the surviving SDL-01 tell. Next print Aug 1 |
| **Fiscal terminus** (muni deficits, pensions, bond risk) | **0 / 12** | **LOW — UNVERIFIED** ⚠️ | All `ELP/NOG/MCA/PHR/BDR/CAL/SFE` rows FROZEN at Feb-2026. This is the **tradeable** end, and it has no live evidence |

**And the one pre-registered test of this channel MISSED.** MAR-01 (Nogales residential floor at −50/−60%, Q2 2026) resolved **7/2 as MISS-on-threshold**: the floor never materialized, ~−43% held, median ~$245K, market **"stabilizing-soft," not collapsed.** Its resolution confirmed the mechanism in a **different terminus** — cross-border **retail** (ICE at all three Nogales POEs, shoppers staying away, Morley Ave foot traffic) — so the mechanism is real and the *specified* stress channel was wrong. That resolution pointed readers at `VX-BDR-03`/`NOG-01`, **which now resolve to frozen February data.**

**Old view (v3.0):** Channel 4 🟠 STRUCTURAL-SLOW, **MEDIUM**, quoting Laredo shopper share 51%→13%, McAllen 36%→28%, Nogales −43.2%, El Paso $55-62M deficit + 60% pension funding, Pharr S&P negative — all as current.
**New view (v3.1):** 🟡 **FLOW LIVE / FISCAL TERMINUS UNVERIFIED · MED-LOW**; those five figures are re-labelled a **frozen Feb-2026 snapshot, not to be cited as current.**

**⚠️ The basis, stated plainly because it matters for how much weight this carries:** the downgrade rests on **absence of maintained evidence plus one missed test — NOT on fresh contradicting data.** MARCO has not looked at border-municipal finances in six months and does not know whether the stress deepened, stabilized or reversed. That is *why* conviction falls: **conviction tracks warranted confidence, not the world.** An unmaintained evidence base cannot support MEDIUM regardless of what is true out there — the same fault v3.0 corrected in Channel 1, applied one channel over.

**Falsifiable both ways (named, so this is not an unfalsifiable downgrade):** rebuild the municipal leg from live primaries — **EMMA/MSRB filings + rating actions** (El Paso, Pharr, Laredo, Nogales), **TX Comptroller / AZ DOR sales-tax receipts** by border city, **CBP border-crossing counts**. Deficits widening + ratings under pressure ⇒ **MEDIUM restored.** Stabilization ⇒ **LOW confirmed or the channel retired.**

**Conviction deltas:** Channel 4 overall MEDIUM → **MED-LOW**; flow leg MEDIUM (unchanged); fiscal terminus → **LOW/UNVERIFIED**. No other channel touched.

---

## v2.8 → v3.0 (2026-07-31, session 19) — **MAJOR** — **CHANNEL 1 DEMOTED FROM SPINE: transmission undemonstrated after three pre-registered nulls**

**Trigger:** the floor-controlled test that v2.8 named as the open path was designed, **pre-registered with thresholds fixed before any data pull**, and run. It returned NULL.

**Design (the thing v2.8 said was needed):** restrict to **federal-minimum ($7.25, no step) states** — where leisure-hospitality runs ~$16–18/hr against a floor that is non-binding and did not move, so the Amendment-2 class of confound **cannot exist by construction**. Within each state, difference L&H wage growth against a control sector; then compare **high-immigrant-share** ($7.25) states against **low-immigrant-share** ($7.25) states. June 2026 vs June 2025, BLS CES state AHE.

**Old view (v2.8):** quantity HIGH; transmission has no working instrument *"pending a better-specified test"* — with TX flagged as an informative null.

**New view (v3.0): the better-specified test was run and it is also null — and the instrument class itself now looks structurally unable to answer the question.**

| Pre-registered condition | TTU control (primary) | E&H control (robustness) |
|---|---|---|
| c1 · high-imm mean DID ≥ +1.5pp | **−1.94pp** FAIL | **+1.25pp** FAIL |
| c2 · DID > 0 in ≥70% of stratum | **33%** FAIL | **33%** FAIL |
| c3 · high−low stratum gap ≥ +1.5pp | **−2.57pp** FAIL | **+1.27pp** FAIL |
| n3 · TX DID ≤ 0 → null trigger | **−8.01pp** FIRED | **−1.88pp** FIRED |

Three things make this a MAJOR bump rather than a fourth data point:

1. **The stratum difference flips sign with the control sector** (−2.57pp vs +1.27pp), and neither is significant (|t| < 1). A real effect does not invert when you swap controls.
2. **The design is badly under-powered, and the +4.88pp FL headline promoted on 7/25 is far inside its noise.** Pooled cross-state sd **5.88pp**; 80%-power MDE **8.78pp** on the pre-registered stratum difference; **~11.53pp** band around any single state's gap. FL's headline sat at ~0.4 sd of ordinary cross-state variation — never distinguishable from heterogeneity, *independent of* the Amendment 2 story. Harsher than v2.8: not merely confounded, **under-powered from the start.**
3. **The gaps are stable, not noisy** (median within-state 6-month **range 4.02pp**; 11 of 14 states hold sign; TX −6.0 to −8.6 every month, a best-behaved cell). They measure something real and persistent that **is not immigrant exposure** — energy-sector mix inside the control supersector contaminates precisely the TX/OK/KS cells.

> **AMENDED 2026-07-31 eve (session 20), PROME audit — no version bump, verdict unchanged.** All 34 DID cells, the t-statistics and the 7/25 pre-commitment reproduce exactly under independent recomputation. Three fixes in the layer around the result: **(i)** points 2 and 3 above carried an unreproducible "3.2pp swing" (now 4.02pp, definition stated) and a "~6pp detection floor" that named a stratum-difference significance threshold and was mis-scoped to single-state gaps — **corrections sent to CARL and LABOR**, who had both received the mis-scoped rule; **(ii)** the pre-registered **FL diagnostic MISSED** (predicted DID ≈ 0, actual +6.89pp) and had been left unscored, which let the outbound CARL packet read the failure as confirmation — **that reading is retracted**; **(iii)** every figure is now derived in `../scripts/fl_diagnostic_score.py`. The power correction cuts both ways and both ways are unfavourable to MARCO's 7/25 self: the null is a weaker test than claimed, and the promoted signal was a weaker signal than claimed.

**Conviction deltas:**
- Channel 1 **quantity**: HIGH → **HIGH (unchanged, explicitly not walked back)**.
- Channel 1 **transmission**: "no current instrument" → **NONE / UNDEMONSTRATED, and demoted from thesis spine**.
- Channel 2 (Canadian travel): MEDIUM-HIGH, unchanged in absolute terms but **now MARCO's highest-conviction *transmitting* channel** — by Channel 1's demotion, not by its own strengthening.

**Why no fourth instrument (a conclusion, not fatigue):** CES is an **establishment payroll survey**, and the population that withdrew is disproportionately undocumented — substantially off-payroll or unresolvable within it. The workers whose exit *is* the mechanism are the ones the instrument can least observe. Reopening requires a source that sees the affected population directly (H-2A offer premia **above** the AEWR floor; vacancy duration in immigrant-intensive occupations; firm-level cost disclosure) — **not** a fourth specification of state payroll wages.

**Discipline note:** the downgrade was **pre-committed in `SCRATCH.md` on 2026-07-25**, before this test was designed, precisely so the decision could not be re-litigated once the result was known. It is executed here as written. Spec `PREREG_2026-07-31_floor_controlled_channel1.md` (incl. Amendment 1, which discloses that the L&H leg had already been seen when the control sector was replaced for availability reasons) · results `../research/2026-07-31_floor_controlled_channel1_RESULTS.md`.

---

## v2.7 → v2.8 (2026-07-25, session 18b) — MINOR — **SAME-SESSION SELF-CORRECTION: the v2.7 wage instrument is FALSIFIED**

**Trigger:** the FL/TX/CA/AZ state-CES panel that v2.7 named as "the confirmation step" was built the same session — as the first item of a stale-vector sweep, because `VX-MARCO-2.05` (Agricultural Wage Growth) and `2.06` (Construction Wage Differential, High-Immigrant) turned out to *already exist* at 184 days stale. Refreshing them ran the test early.

**Old view (v2.7, hours old):** produce CPI demoted; **wage divergence promoted to primary Channel-1 instrument** at MEDIUM-HIGH on FL leisure & hospitality +8.75% YoY vs national +3.87%, three consecutive months.

**New view (v2.8): falsified as specified.** June 2026 YoY gap vs national (pp):

| | Leisure & Hosp | Construction | Total Private |
|---|---|---|---|
| **FL** | **+4.88** | +1.02 | +0.76 |
| **TX** | **−6.45** (−2.58% YoY, falling) | −3.22 | −0.74 |
| **CA** | −1.94 | +3.96 | −0.80 |
| **AZ** | −1.05 | −0.36 | −0.35 |

**Two of eight state-sector cells positive.** If immigrant-supply withdrawal drove hospitality wages, **TX should show it most** — largest immigrant workforce exposure, most aggressive enforcement environment — and TX hospitality wages are **falling outright**.

**The FL cell has a mundane and sufficient cause: Amendment 2.** FL is mid-ramp $13 (Sep'24) → **$14 (Sep 30 2025)** → $15 (Sep 30 2026). The June-2026 YoY window spans that step = a **7.7% statutory increase in the wage floor**, in the sector most exposed to the floor. FL printed +8.75%. **TX — $7.25, unchanged since 2009, no floor push — went negative.** The co-driver v2.7 named as "undecomposed" accounts for essentially the whole divergence.

**Why MINOR despite being a reversal:** no channel added or removed, and the Channel-1 **quantity** evidence is untouched. But this is a **genuine downgrade, not a re-framing** — see below.

**Conviction deltas:**
- Channel-1 **mechanism / quantity**: HIGH → **HIGH** (unchanged — LF −700K YoY, LFPR 61.5%, H-2A ~455-465K pace all stand)
- Channel-1 **wage instrument**: MED-HIGH → **FALSIFIED**, removed
- Channel-1 **transmission to prices/costs**: **NO WORKING INSTRUMENT.** Produce demoted in the morning, wages falsified in the afternoon — both pre-registered, both MARCO's own, both against the thesis.
- Net: MARCO can assert the labor shock **happened and is large**; MARCO **cannot currently demonstrate it is transmitting** to food prices, service costs, or regional cost-of-living. That is the part downstream agents consume.

**Open path (a question, not a finding):** a valid test must control for statutory wage floors — immigrant-heavy vs immigrant-light sectors *within* a state, or states with no minimum-wage step. **TX is the clean laboratory and TX says no**, which is an informative null pointing *against* transmission rather than merely absent evidence.

**Retractions issued same day:** 🔴 full retraction → LABOR (which had been asked to re-anchor its supply-adjusted U-3 work on the wage figure); 🔴 partial → CARL (§2 retracted, §1 produce demotion stands; the cost-push point survives on *statutory* grounds with a dated Q4 2026 impulse as the floor steps $14→$15); 🟡 minor → CORAL (one interpretive line).

**Process note — the failure was sequencing, not specification.** The falsifier and the co-driver decomposition were both correctly written down *at promotion time*. They simply weren't run before promoting. Promoting an instrument on three months of a single state-sector while naming an unrun decomposition is MARCO's characteristic error (single-mechanism over-attribution) committed on the way *in* to a new instrument — which the v2.7 text explicitly warned against and then did anyway. **Rule adopted: a pre-registered falsifier that can be run today gets run BEFORE promotion, not after.**

---

## v2.6 → v2.7 (2026-07-25, session 18) — MINOR — Channel-1 RE-INSTRUMENTATION (produce thermometer demoted a 2nd time; wage divergence promoted)

**Trigger:** (1) **ES-MARCO-08 resolved** at the June CPI print (BLS public API, primary) — MARCO's own pre-registered labor-vs-freight discriminator. (2) A live VX refresh, prompted by Will catching an unverified universal claim ("every FL metric I own is improving"), which surfaced that the FL hospitality-wage vector was 6 months stale and pointing the **wrong way**.

**Old view (v2.1–v2.6):** Channel 1 = labor-supply shock measured through **produce prices**. The mechanism was HIGH-conviction; the produce CPI thermometer was "confounded, MEDIUM" after v2.1 but still the named readout, and ES-MARCO-08 was the test that would re-weight labor back *up* if F&V held while pump prices fell.

**New view (v2.7):** **The test fired clean and went the other way.** The 7/9 contamination risk did not materialize — despite the Iran-truce collapse and the Russian diesel-export ban, June gasoline fell **−9.68% MoM** (energy −5.7% MoM, largest since April 2020), so the pump-relief premise held. And fresh F&V (`SAF1131`) fell *with* it: **+6.74% → +5.71% YoY, −1.05% MoM**. Per the pre-registered spec, **freight carried more of the spike than labor did.**

So produce CPI is demoted a second time, on independent grounds: **confounded (v2.1) → weak corroboration only (v2.7).** Two failures as a readout is enough — MARCO stops citing F&V prints as Channel-1 evidence in either direction.

**The replacement — measure the shock at the INPUT price, not the output price.** FL leisure & hospitality average hourly earnings **$23.99 (Jun'26) vs US $23.62**: FL is now **+1.6% above** national, against a carried (Jan-vintage) row that said 11% *below*. **FL +8.75% YoY vs national +3.87%, three consecutive months at >2x national.** No freeze, no tariff, no diesel pulse can enter a wage series — the exact confounders that killed the produce thermometer are structurally absent. Wages sit one step from the mechanism; produce prices sit at the far end of a multi-causal chain.

**Why MINOR not MAJOR:** no channel added or removed, and **conviction on the Channel-1 mechanism is unchanged at HIGH** (H-2A ~455-465K pace, LFPR 61.5%, foreign-born LF −700K YoY, less-than-HS LFPR 43.1% all intact). This is a **measurement** change, not a direction change — the same class as v2.1, applied a second time to the same channel. The thesis got *better instrumented*, not weaker.

**Conviction deltas:**
- Channel-1 **mechanism**: HIGH → **HIGH** (unchanged)
- Channel-1 **produce thermometer**: MEDIUM → **LOW** (demoted; corroboration only)
- Channel-1 **wage instrument**: *(new)* → **MEDIUM-HIGH**, provisional pending the 4-state panel
- Channel-2 (Canadian): MEDIUM-HIGH → **MEDIUM-HIGH** (unchanged; see mixed evidence below)

**Channel-2 evidence this session (no version impact, both directions):** June StatCan — total return trips 1.7M **+3.2% YoY** (3rd consecutive gain) but 2-yr stack **−28.7%**, so TOUR-01 holds; **the air stack narrowed −28.4% → −25.0%** and is now sitting *on* the threshold line, which is the FL-snowbird-relevant leg thawing. Against that: **Trump's 7/20 50% Section 338 tariff** on broad Canadian goods is a fresh sentiment re-escalation arriving into the thaw, and reporting notes the boycott has shifted "from emotional protest into logistical habit" (habit being stickier than anger). Net: unchanged conviction, higher variance, watch the air stack.

**Explicit non-finding (logged so it is not mistaken for confirmation later):** FLL May printed **−10.7% YoY / −26.1% 2-yr stack** with international **−27.5% / −48.7%**. This is **not** Channel-2 evidence. Spirit Airlines liquidated 5/2/26 holding **31.4% of FLL** and was its primary Central/South America link; JetBlue backfilled **+75% daily departures** (share 22%→37%). A supply shock that gets substantially backfilled is weak evidence *against* a demand collapse. MAR-24 raised 45%→60% **with a TRUE-in-letter/FALSE-in-spirit caveat attached** ([[finding_threshold_vs_mechanism]]).

**Also this session:** ES-MARCO-01 resolved **DID_NOT_APPEAR** at the FL-state leg (FL L&H *added* jobs in June; FL UR 4.7%, first decline since 2024) — and the wage data re-reads that as labor scarcity rather than the demand weakness the signal was built to detect. ES-MARCO-05 → RECEDING. MAR-14 74%→45% (and a 74-vs-55 STATUS/TSV drift reconciled to one number), MAR-12 60%→35%. VX household-insurance-cost vector (3.01) stale-flagged with **no figure adopted** — secondary aggregators span $3,815–$8,458; needs an FL OIR primary.

---

## v2.5 → v2.6 (2026-07-02, session 16) — MINOR — Channel-1 magnitude/provenance RE-MARK (2.2M "CBO" → ~1.0M realized LF) + June-jobs aggregate corroboration
**Trigger:** (1) PROME Tier-2 verification (Workflow `wzlhvzlcb`, vs CBO / NFAP-BLS-CPS / KC-Fed primaries; `../inbox/2026-06-26_from-PROME_immigration-magnitude.md`) — resolves the long-open MAINTENANCE T1-B / NOTES.md flag that the "2.2M" spine sat un-cross-referenced. (2) June 2026 jobs report (released 7/2).

**Old view (v2.0–v2.5):** Channel-1 spine = "irreversible **2.2M** self-deportation stock loss **(CBO)**" — treated as the smoking-gun magnitude, cited flat across STATUS/THESIS/VX/KB/NEXUS_BRIEF.

**New view (v2.6):** The 2.2M figure is **wrong on both count and source.** (a) It is a **disputed DHS** self-deportation claim (CMS: "the Two Million Deportation Myth"), **NOT CBO-modeled** — CBO removals ≈ **290K + 30K voluntary emigration (2026–30)**, an order of magnitude smaller. (b) The **realized** magnitude is **~1.0M foreign-born labor-force decline / ~1.5M population** (NFAP/BLS-CPS; FRED LNU01073395 ~−1.1M NSA, Mar'25→Feb'26). The U-3/supply-floor mechanism runs through the LF number → cite ~1.0M for the labor channel, state the basis. Breakeven payrolls ~50K/mo (KC-Fed, derived).

**Why MINOR not MAJOR:** PROME's own framing — "the immigration supply-floor mechanism SURVIVES; a smaller-but-real ~1.0M LF cut still keeps U-3 genuinely low — a provenance + quantum re-mark, **not a direction change.**" Conviction direction/HIGH on the mechanism unchanged; only the headline count + attribution corrected. No channel added/removed.

**Independent corroboration (June jobs, 7/2):** total labor force −1M+ YoY, employed −1.06M YoY, LFPR **61.5% = lowest in 50 yrs ex-Covid**, household employment −507K in June, net migration "fell by more than half." The corrected ~1.0M realized LF contraction is now visible in the flagship aggregate — the shock has moved from proxies (produce, remittance counts) into headline labor data. Multi-causal caveat (characteristic error): the aggregate LF drop also reflects aging + discouraged workers + degraded CPS response (66.6%); immigration is a named, material co-driver, not sole.

**Also this session (June-jobs Channel-2 leg):** national Leisure & Hospitality **−61K in June** *during* the World Cup — the hospitality-jobs mask (ES-MARCO-01) INVERTED (May +70K WC-hiring → June −61K, net ~flat). Tourism→jobs transmission firing through the WC tailwind; reinforces ES-09 (WC flop). No thesis-version impact — logged as ES-01 APPEARING.

**Conviction deltas:**
| Item | v2.5 | v2.6 |
|---|---|---|
| Channel-1 mechanism (labor-supply shock exists) | HIGH | **HIGH** — unchanged |
| Channel-1 magnitude | "2.2M CBO" (over-stated, mis-sourced) | **~1.0M realized LF / ~1.5M pop** (NFAP/BLS-CPS, FRED) — corroborated by June LF −1M+ YoY |
| SDL-01 visibility | proxy-only (produce, remittance count) | **now visible in flagship aggregate** (LFPR 50-yr low, LF −1M+ YoY) |

**Reconcile-to-one-number action:** propagate ~1.0M LF / ~1.5M pop to CORAL + LABOR (LABOR's supply-adjusted U-3 counterfactual sourced the old ~1.6–1.9M to MARCO). Cross-agent notes in `../outbox/`.

**Propagation note:** canonical (THESIS) + all live-cited surfaces (STATUS, VX-SDL-01, KB, FINDINGS, NEXUS_BRIEF) re-marked this session; dated historical/archival mentions (older CHANGELOG/TIMELINE entries, `sub_agents/WORKFORCE`, `domain/sources/SDL/`, ML.tsv frozen) retain the old figure as as-of snapshots — swept opportunistically, not load-bearing.

---

## v2.4 → v2.5 (2026-06-15, session 13) — Channel-1 enforcement FLOW re-locked (funding now law)
Old view (v2.3): funding FLOW CONTESTED — bill missed the Jun 1 deadline, parliamentarian carved the core under Byrd; flow accelerator uncertain (2.2M stock loss irreversible regardless).
New view (v2.5): funding FLOW is LAW. The reworked ~$70B ICE/CBP package was signed Jun 10 2026 (Senate 52-47 / House 214-212), funding ICE + parts of CBP through the end of Trump's term (Jan 2029). Channel-1 conviction UP.
Stock/flow distinction PRESERVED: the 2.2M self-deportation stock loss was always the irreversible spine; what re-locks is the flow accelerator (fresh removals atop the stock) that v2.3 marked uncertain.
Unchanged: 5-channel structure; produce-CPI thermometer stays MEDIUM/confounded (v2.1).
Provenance caveats (open): (1) enacted ICE/CBP sub-split not reconciled — "$38B/$26B" are the pre-trim May-4 proposal, not the signed allocation. (2) Construction-raid → housing leg stays anecdote-grade: April 2026 NRC shows national SF starts −9.0% MoM / SF permits −2.6%, but weakness is broad and rate/affordability-confounded, and geography runs AGAINST a South-concentrated raid signal (South SF starts −2.7% / permits −1.9% = smallest declines of any region, vs West −22.9% / NE −18.8%). Mechanism-confirming, not threshold-confirming.

---

## v2.3 → v2.4 — 2026-06-02 (session 11) — MINOR — "Channel 2 has a macro frame: the first US inbound decline in 20 years"

**Trigger:** A TOURISM-assessment pass surfaced a thesis-grade fact that had sat in the sub-agent (KB-MARCO-IVF-26) since session 9 without propagating up: **CY2025 was the first US inbound-tourism decline in 20 years (−5.5%, 68.3M arrivals; NTTO/Inbound Travel Assoc).** The propagation gap is itself the finding — the sub-agent does good work that doesn't reliably rise to MARCO.

**Old view (v2.2/v2.3):** Channel 2 was framed as the **Canadian boycott** — air/winter structural, base-effect headline — plus a secondary overseas/NTTO line. The boycott was treated as a largely self-contained Canada story.

**New view (v2.4):** Channel 2 is re-framed one level up. **The Canadian boycott is the sharp edge of a broader structural inbound contraction** — the whole US inbound complex turned negative for the first time in two decades, and overseas arrivals are stuck 14–26% below 2019 on top of the Canadian collapse. Canada (#1 market) is the leading edge, not the whole story. **No conviction-level change** — Channel 2 stays MEDIUM-HIGH; the frame strengthens it rather than reclassifying it.

**New forward test (the live piece):** the **FIFA World Cup (US co-host, Jun 11–Jul 19 2026)** is the event that *should* pull inbound back above 2019 — the natural reversal catalyst. Q2 data is not yet encouraging. If the World Cup fails to reverse the 20-yr decline, the structural read hardens. Added as ES-MARCO-09 + a docket catalyst + a TIMELINE forward branch point. **Note:** this catalyst was absent from MARCO's docket entirely despite being the single largest US-inbound event of 2026 and already live.

**Why MINOR not MAJOR:** adds a frame + a forward test to an existing channel; no conviction reversal, no new channel, no spine change.

**Conviction deltas:**
| Item | v2.3 | v2.4 |
|---|---|---|
| Channel 2 (visitor flows → FL CRE) | MEDIUM-HIGH (Canada boycott) | **MEDIUM-HIGH** — unchanged level, frame widened to first-20-yr-inbound-decline |
| World Cup as inbound-reversal test | not tracked | **live forward catalyst** (ES-MARCO-09, docket Jun 11–Jul 19) |

---

## v2.2 → v2.3 — 2026-06-02 (session 10) — MINOR — "Enforcement-funding lock is contested, not locked"

**Trigger:** Session-10 pull of the Jun 1 reconciliation outcome + April Banxico print. The reconciliation bill **MISSED Trump's June 1 deadline**; Senate Parliamentarian MacDonough struck core ICE/CBP enforcement-and-screening provisions under the Byrd rule (jurisdiction), plus the $1.8B DOJ fund and $1B ballroom security. No floor passage.

**Old view (v2.0–v2.2):** The $71.7B reconciliation text (May 4) was treated as a near-certain lock — "ICE enforcement funded and unconstrained through Trump's term; funding is no longer a brake." This was filed as Channel 1's *structural accelerator* and as a HARDENED bullet in the thesis inflection.

**New view (v2.3):** The funding **flow** is CONTESTED, not locked. The bill is intent, not law, and the parliamentarian carved out the enforcement core. **The crucial distinction the prior framing blurred: SDL-01's durable driver is the irreversible 2.2M self-deportation *stock* loss — that is untouched.** What just got downgraded is the *flow* accelerator (new enforcement funding feeding fresh removals on top of the stock). Direction unchanged (GOP can rework + pass simple-majority), certainty cut.

**Why MINOR not MAJOR:** the thesis spine (stock-loss → labor supply shock → produce/ag transmission) does not move — the stock loss already happened and is irreversible. Only the *certainty of the flow accelerator* changed. Symmetric to v2.1/v2.2: a conviction-by-component refinement, separating the irreversible stock (intact) from the contested funding flow.

**Conviction deltas:**
| Item | v2.2 | v2.3 |
|---|---|---|
| ICE enforcement-funding lock (flow accelerator) | 🔴 STRUCTURAL / locked | **🟠 CONTESTED ↓** — missed Jun 1, core carved |
| SDL-01 stock-loss driver (2.2M) | irreversible | **unchanged** — irreversible |

**Companion data point (not a thesis change):** Banxico Apr remittances +3.7% YoY ($4.98B); the Mar pull-forward paradox (count −3.6% / avg +8.9%) is FADING (count −1.7% narrowing, avg premium +5.5% compressing) — normalizing, no Q2-Q3 air-pocket so far. Count still negative = SDL-01 senders-decline tell intact. Resolves the remittance-paradox open thread toward "normalizing." Logged KB-MARCO-REM-04 *(renumbered from KB-MARCO-REM-03 on 2026-08-21 to resolve an ID collision; the handle now resolves uniquely)*; not a conviction change (consistent with existing structural read).

**Discipline note:** third correction in the same direction — don't bank a forecast (here, a legislative passage) as a *resolved structural fact* before it clears. v2.1 demoted an over-claimed signal (produce), v2.2 re-promoted an under-claimed one (tourism), v2.3 un-banks a not-yet-true one (the funding lock). The robust core each time is the irreversible stock fact; the contaminated layer is the readout/forecast on top.

---

## v2.1 → v2.2 — 2026-05-31 (session 9) — MINOR — "Canadian travel is structural, not softened"

**Trigger:** Session-9 TOURISM full refresh (sub-agent frozen since Apr 20; top-level dashboard had absorbed only the April headline). 4 parallel research agents pulled current data — and the new StatCan March-full release (May 21) supplied the clean 2-yr stack that v2.0/v2.1 were missing.

**Old view (v2.0/v2.1):** Channel 2 "BIFURCATED," MEDIUM, filed in the *softened/cyclical* column of the thesis inflection. The April Canadian return-trips +1.4% YoY was read as a headline reversal (auto-driven, air still negative) — softening, not recovery, but on the "reversed" side of the ledger.

**New view (v2.2):** Channel 2 splits into **structural (air/winter/capacity, MEDIUM-HIGH) vs. base-effect-readout (headline + FLL/MCO airport YoY, LOW).** The April "recovery" is base-effect: the 2-yr stack vs 2024 *worsened* (−28% Mar → −30% Apr) even as the headline went positive. The boycott isn't easing — the comparison base is. Canadian travel moves OUT of the "softened" bucket back to **structural**, joining Channel 1 as the thesis's second durable spine.

**Three confirming facts (current, primary-sourced):**
- **2-yr stack worsening:** StatCan Mar-full (dq260521a) −28.0% vs 2024; Apr prelim (dq260511a) −30.0%. Headline +1.4% is the base easing.
- **Sentiment 82%:** Nanos May 3-6 (n=1,003) — 82% call the boycott helpful. A May reading; no softening.
- **Capacity permanently deleting:** Air Transat complete US exit Jun 13; AC winter 2026-27 zero new FL routes; WestJet summer −32% ASM. MIA flipped negative (−2.02% Apr).

**Why MINOR not MAJOR:** structurally symmetric to v2.1. v2.1 separated Channel 1's mechanism (solid) from its thermometer (confounded); v2.2 separates Channel 2's structural signal (air/winter) from its misleading readout (base-effect headline). Both are conviction-by-indicator refinements, not spine reversals. If anything v2.2 *raises* Channel 2 conviction by correcting a too-generous "softened" read.

**Conviction deltas:**
| Item | v2.1 | v2.2 |
|---|---|---|
| Channel 2 air/winter (structural) | MEDIUM (bifurcated) | **MEDIUM-HIGH ↑** structural |
| Canadian headline YoY as readout | (implicit signal) | **LOW** — base-effect noise |

**Prediction resolutions logged:** TOUR-04 (MIA flips negative) RESOLVED-CORRECT (−1.76% Mar, −2.02% Apr); TOUR-02 (LV Canadian share <5%) RESOLVED-CORRECT on share-of-total (~3%). TOUR-01/03/05 confidence raised (80→85, 85→90, 75→85). Top-level MAR-22 70→50, MAR-24 55→45 (base-effect protects FLL/MCO headline). Detail: `PREDICTIONS.tsv`, `../sub_agents/TOURISM/`.

**Discipline note:** this is the inverse of the v2.1 correction — there the data forced a *demotion* (produce over-claimed); here it forced a *re-promotion* (tourism under-claimed when I let the April headline soften the top-level read). Same lesson: read the clean metric (2-yr stack), not the contaminated one (headline YoY). The base-year caveat the TOURISM sub-agent held since Apr 20 was right; the top level had partly lost it.

---

## v2.0 → v2.1 — 2026-05-31 (session 8) — MINOR — "The produce thermometer is confounded"

**Trigger:** Session-8 produce-attribution decomp (deep-research harness + external-primary verification, completed session 7; reviewed against BRENT's diesel/freight files session 8). v2.0 leaned on CPI fresh F&V +6.1% YoY as the clean confirmation that the workforce shock (Channel 1) was transmitting to food prices. The decomp showed the spike is multi-causal.

**Old view (v2.0):** Channel 1 "load-bearing," HIGH conviction, with the produce CPI print read as direct, hardening confirmation of labor→food transmission. "+6.1% produce" carried as strong thesis evidence.

**New view (v2.1):** Channel 1 splits into **mechanism (HIGH, intact)** vs. **thermometer (MEDIUM, demoted).** The ag-labor supply shock (2.2M stock loss + H-2A bottleneck) is undisputed. But the produce CPI is **multi-causal** — labor is one co-driver, not the dominant/measurable one. A slow labor *stock* drift cannot mechanically produce a one-month +4.0%→+6.1% *acceleration*; supply/cost shocks can.

**Three co-drivers — verified, well-timed, magnitude-material:**
- **FL freeze** Dec'25–Feb'26 — $3.17B, USDA disaster declaration, hit exactly the spiking crops (berry/tomato). Fleet-wide blind spot; nobody caught it. (I first called it fabricated on fleet silence — WRONG; Will pushed back, external primaries confirmed it real. Lesson → auto-memory `feedback_verify_existence_external_primaries`.)
- **Mexican tomato tariff** — 17% AD duty (Jul'25) on the most-weighted fresh vegetable.
- **Diesel/freight** — crude spiked to $116 (May 5), distillate ~11% below 5-yr; timed to the April acceleration. Cross-checked against BRENT's files (session 8): the freight co-driver is **transient/mean-reverting** (crude −19% on the month; pump relief May 31–Jun 14), which sets up a dated forward test.

**Why MINOR not MAJOR:** the thesis spine (workforce supply shock) is unchanged and still HIGH. What changed is the *evidentiary status of one indicator* — we can no longer cite produce CPI as clean labor proof. Refinement of conviction-by-indicator, not a structural reversal.

**Conviction deltas:**
| Item | v2.0 | v2.1 |
|---|---|---|
| Channel 1 mechanism (labor shock) | HIGH | **HIGH** (unchanged) |
| Produce CPI as proof of it | (implicit HIGH) | **MEDIUM ↓** — confounded |

**Forward test added:** ES-MARCO-08 (`EXPECTED_SIGNALS.md`) — June 10 / July CPI vs. pump-price decoupling discriminates labor-vs-transient weighting. New coupling logged: `COUPLINGS.md` MARCO↔BRENT (decaying freight-input edge).

**Prediction resolution:** MAR-21 (planting-season raid surge → produce spike) RESOLVED — mechanism largely WRONG (raids eased, H-2A wages cut; spike attributable to freeze/tariff/freight). See `PREDICTIONS.tsv`.

**Discipline note:** v2.1 is the honest correction of a v2.0 over-claim. The "verify via external primaries" lesson was *satisfied* here — freeze, tariff, and crude all verified against primaries before the demotion — which is what licensed the rewrite rather than blocking it.

---

## v1.0 → v2.0 — 2026-05-31 (session 6) — MAJOR — "The thesis narrows to its spine"

**Trigger:** Session-6 full-sweep data refresh (STATUS was 5 weeks cold; last updated Apr 23). Live pulls on every stale board item revealed a **bifurcation** the v1.0 "everything compounding" frame had masked.

**Old view (v1.0, ~Jan–Apr 2026):** Acute, multi-front population-stress crisis. 76% confidence, STRENGTHENING, Phase 2→3. All channels (tourism, workforce, migration, border) treated as compounding simultaneously toward a unified regional-stress event. Dashboard carried ~10 "breached" indicators read as a single hardening crisis.

**New view (v2.0):** The thesis **bifurcated**. Cyclical channels reversed; the structural channel hardened. The thesis did not break — it **narrowed to its durable spine** (Channel 1: workforce displacement → produce prices). Conviction is now **split by channel** — that split is the substance of v2.0.

**What reversed/softened (→ cyclical, conviction cut):**
- DHS shutdown ENDED Apr 30 (76-day record) — acute disruption over.
- FL condo inventory 8.9mo Apr (back below 9.0, tightening) — Channel 3 ↓.
- Canadian visitors +1.4% YoY Apr headline (air still −8.1%) — Channel 2 ↓ to bifurcated.
- NFP rebounded +115K / UE 4.3% — Feb −92K "smoking gun" was a blip.
- Mexico remittance $-value flipped +4.9% Mar (count −3.6%) — Channel 4 residual signal only.
- ICE eased off ag worksite raids — Channel 1 *flow* softened.

**What hardened (→ structural, conviction held/raised):**
- CPI fresh F&V +6.1% YoY (was +4.0% Mar); fresh veg +3.1% MoM — produce spike accelerating.
- ICE/CBP $71.7B reconciliation text (May 4) — enforcement funded & unconstrained through Trump's term; funding no longer a brake.
- H-2A consular bottleneck persists (South Africa→July; Red River Valley potato).
- 2.2M self-deportation stock loss — irreversible; Channel 1's foundation.

**Conviction deltas (channel-level):**
| Channel | v1.0 | v2.0 |
|---|---|---|
| 1 Workforce→Produce | (folded into 76% composite) | **HIGH ↑** load-bearing |
| 2 Visitor Flows→FL CRE | high/compounding | MEDIUM ↓ bifurcated |
| 3 Migration→Sun Belt | high/compounding | MED-LOW ↓ softening |
| 4 Cross-border→muni | strong | MEDIUM → slow grind |
| 5 American emigration | watch 65% | LOW → watch (unchanged) |

**Invalidation note:** Two of v1.0's four invalidation conditions *partially fired* (Canadian headline rebound, FL RE stabilization). Under v1.0's monolithic frame that would read as the thesis weakening broadly; under v2.0 it correctly localizes to Channels 2-3, leaving the spine (Channel 1) intact. This is exactly why the channel-split reframe was necessary.

**Prediction resolutions logged this session:** MAR-08 (FL condo >9mo) CONFIRMED; MAR-27 (DHS >60d) CONFIRMED. Notes refreshed on MAR-14/-18/-26. (`PREDICTIONS.tsv`)

**Structural note:** v2.0 is the first time MARCO's thesis lives in the house `thesis/` format (consolidated from `MARCO_SKELETON.md` v1.0 + `DECK_EVIDENCE.md` + `FINDINGS.md` + `workbook/FLOW.tsv`). SKELETON retained as v1.0 historical artifact.

---

## v1.0 — pre-2026-05-31 (baseline, reconstructed)

Original thesis articulated in `MARCO_SKELETON.md`: "Population movement disruptions create localized economic stress that compounds in regions with multiple exposures; traditional indicators miss or lag." 76% confidence, STRENGTHENING, Phase 2→3 (Stress Emergence → Economic Transmission). Four FLOW cascades (FLOW-REG-01 FL triple-exposure, FLOW-IVF-01, FLOW-WFD-01, FLOW-IMG-01). Detail in that file; not re-versioned here.
