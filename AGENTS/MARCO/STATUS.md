# MARCO STATUS
**Last Updated:** 2026-07-31 ET (session 19) | **Thesis:** v3.0 | **Status:** 🟠 ELEVATED

**This session in one line:** **Channel 1 is demoted from thesis spine.** The floor-controlled test v2.8 called for was pre-registered and run — **NULL, robust to control choice** (all 3 CONFIRM conditions failed under both controls; TX negative in all 6 months of 2026). Channel 1 is now **quantity HIGH / transmission UNDEMONSTRATED** after three pre-registered nulls, and MARCO is **not hunting a fourth instrument** — the payroll-survey instrument class cannot see the affected population. Also this session: the H-2A fetcher was found **dead ~101 days** (boot was printing "✓ ran cleanly" beside its own FAIL) and rebuilt; the docket had **3 duplicate event pairs hiding 3 stale premises**, deduped.

## 7/31 UPDATE (session 19) — READ FIRST

> ### ⚫ CHANNEL 1 DEMOTED FROM SPINE (thesis v2.8 → **v3.0**, MAJOR)
> **The test:** restrict to **federal-minimum ($7.25, no step) states** — L&H runs ~$16–18/hr against a floor that is non-binding and did not move, so the Amendment-2 confound **cannot exist by construction**. Within each state, difference L&H wage growth against a control sector; compare high- vs low-immigrant-share strata. Thresholds fixed **before any pull** (`thesis/PREREG_2026-07-31_floor_controlled_channel1.md`).
>
> | Pre-registered condition | TTU control | E&H control |
> |---|---|---|
> | high-imm mean DID ≥ +1.5pp | **−1.94pp** FAIL | **+1.25pp** FAIL |
> | DID > 0 in ≥70% of stratum | **33%** FAIL | **33%** FAIL |
> | high−low gap ≥ +1.5pp | **−2.57pp** FAIL | **+1.27pp** FAIL |
> | TX DID ≤ 0 (null trigger) | **−8.01pp** FIRED | **−1.88pp** FIRED |
>
> **Three things make this structural, not just a third miss:**
> 1. **The stratum difference flips sign with the control** (−2.57 vs +1.27pp), neither significant (|t|<1). A real effect doesn't invert on a control swap.
> 2. **Detection floor ≈ 6pp — larger than the +4.88pp FL headline promoted on 7/25.** That signal was never distinguishable from cross-state heterogeneity, *independent of* the Amendment 2 story. Harsher than the 7/25 verdict: the instrument was **under-powered from the start**, not merely confounded.
> 3. **The gaps are stable, not noisy** (median 6-month within-state swing 3.2pp; TX −6.0 to −8.6 *every* month) — they measure something real that **is not immigrant exposure**. Energy-sector mix inside the control supersector contaminates exactly the TX/OK/KS cells.
>
> **Net state:** quantity evidence **HIGH and untouched** (foreign-born LF −700K YoY, LFPR 61.5%, less-than-HS LFPR 43.1%, H-2A FY26-thru-Q2 **254,688** certified re-verified from OFLC primary today). Transmission: **NONE — UNDEMONSTRATED**, three pre-registered tests, all MARCO's own, all null. **Channel 2 (Canadian travel) is now MARCO's highest-conviction transmitting channel** — by Channel 1's demotion, not its own strengthening.
>
> **No fourth instrument, and that is a conclusion.** CES is an establishment **payroll** survey; the population that withdrew is disproportionately undocumented and therefore substantially off-payroll or unresolvable within it. The workers whose exit *is* the mechanism are the ones it can least see. Reopening needs a source that observes them directly — H-2A **offer premia above** the AEWR floor (never AEWR itself: it is administratively set, and its NASS basis was canceled Aug 2025), vacancy duration in immigrant-intensive occupations, or firm-level cost disclosure.
>
> **The downgrade was pre-committed on 7/25**, before this test was designed, so it could not be re-litigated once the answer was known. Executed as written. → `research/2026-07-31_floor_controlled_channel1_RESULTS.md`.
>
> **🔴 Consumers must update:** CARL (cost-push), LABOR (U-3 supply floor), REGINALD. Channel-1 **transmission** is **UNSUPPORTED** — not "pending a better test," which is what v2.8 said. **Quantity claims remain citable.**

**Also 7/31 — boot infrastructure:** `h2a_pull.py` dead ~101d (hardcoded filename list vs DOL's advancing-quarter cumulative file; Wayback fallback also dead). Rebuilt — discovers the filename live, fetches dol.gov direct (full browser headers clear the Akamai wall; UA-only 403s), 300s→11s. **`boot.py` was printing "✓ ran cleanly" beside its own FAIL** for any failure whose text missed a marker whitelist — fixed to branch on exit status. Cadence moved to content-vintage (an mtime skip armed today would have blinded MARCO to the Q3 file publishing tomorrow). Docket: **3 duplicate event pairs**, hiding a live row that still pointed Aug 8 at the falsified wage instrument, MAR-24 at a stale 45% (canonical 60%), and the retracted "2.2M". All fixed; duplicate/vocabulary/sort checks now run at every boot.

---

*Session history lives in `thesis/CHANGELOG.md` — not in this header. Prior sessions: s17 (7/9) WALTER backlog drain + LFPR 43.1 verify + energy re-shock forward-read; s16 (7/2) SDL-01 magnitude re-mark 2.2M→~1.0M + June jobs + FL Citizens MAR-17 invalidated. Superseded READ-FIRST blocks (s13 6/15, 5/31 thesis inflection) → `domain/sources/_archive/STATUS_readfirst_blocks_s13_and_20260531.md`.*


---

## 7/25 UPDATE (session 18) — READ FIRST

16-day catch-up. One pre-registered test resolved, one thesis re-instrumentation, and a live vector refresh that corrected two of MARCO's own surfaces in **opposite** directions.

> ### 🔴🔴 s18b SAME-SESSION REVERSAL — the 7/25 wage instrument was FALSIFIED (archived)
> **Superseded by v3.0 — the open path this block named was tested 7/31 and came back NULL; see the 7/31 block above.** In brief: the FL/TX/CA/AZ panel meant to confirm the instrument killed it (Jun'26 L&H gap vs national — FL +4.88 · **TX −6.45 and falling** · CA −1.94 · AZ −1.05; 2 of 8 cells positive), FL's cell being an Amendment 2 statutory-floor artifact. Retractions went to LABOR (full), CARL (partial), CORAL (one line) same day. Full text → `domain/sources/_archive/STATUS_s18b_reversal_block.md`; canonical → `thesis/CHANGELOG.md` v2.8 + v3.0.

1. **🔴 ES-MARCO-08 RESOLVED — against the produce thermometer. Thesis → v2.7.** The 7/9 contamination risk **did not materialize**: despite the Iran-truce collapse and the Russian diesel ban, June gasoline fell **−9.68% MoM** (energy −5.7% MoM, largest since Apr 2020), so the pump-relief premise held and the fork fired as designed. Result: fresh F&V (`SAF1131`) **+6.74% → +5.71% YoY, −1.05% MoM** — produce fell **with** the pump. Per the pre-registered spec, **freight carried more of the spike than labor.** Produce CPI demoted a second time (v2.1 confounded → v2.7 **weak corroboration only**); stop citing F&V prints as Channel-1 evidence in either direction. *(Series note: MARCO's carried "+6.1% fresh F&V" for Apr/May was actually the broader `SAF113` aggregate; true fresh F&V was 6.51/6.74. Mislabel corrected, direction unaffected.)*
2. **~~🟢 REPLACEMENT INSTRUMENT — wage divergence~~ — ❌ FALSIFIED same session, see the reversal block above. Retained as the record of what was claimed.** FL leisure & hospitality AHE **$23.99 (Jun'26) vs US $23.62 = +1.6% ABOVE national**, against a carried row that said **11% below** at $20.74 (Jan vintage). **FL +8.75% YoY vs national +3.87%, three straight months at >2x national** (BLS CES, live API). No freeze, tariff, or diesel pulse can enter a wage series — the confounders that killed the produce thermometer are structurally absent. Promoted to the primary Channel-1 instrument at **MEDIUM-HIGH** (provisional: single state/sector/3 months; FL minimum-wage schedule + general tightness are named, undecomposed co-drivers). **Build next session:** FL/TX/CA/AZ × hospitality/construction/ag-adjacent wage panel vs national.
3. **🟠 FLL May −10.7% is a SUPPLY shock, not FL demand — do not route it as tourism deterioration.** Broward PDF (primary): total 2,255,277 **−10.7% YoY / −26.1% 2-yr stack**; intl 319,493 **−27.5% / −48.7% stack**. Cause: **Spirit Airlines liquidated 5/2/26** holding **31.4% of FLL** (11M pax 2024) and was its primary Central/South America link — which is the international leg entirely. **JetBlue backfilled +75% daily departures** (share 22%→37%), so net deletion ≪ gross. A supply shock that gets substantially backfilled is weak evidence *against* a demand collapse. MAR-24 raised 45%→60% **with a TRUE-in-letter/FALSE-in-spirit caveat attached.**
4. **🟡 Canadian: stack holds, air leg narrowing into a fresh tariff.** June StatCan (rel 7/13): 1.7M return trips **+3.2% YoY** (3rd consecutive) but 2-yr stack **−28.7%** (auto −29.6%, air −25.0%) — TOUR-01 (<−25%) holds. **The air stack narrowed −28.4% → −25.0%** and now sits *on* the threshold; air is the FL-snowbird-relevant leg. Against it: **Trump's 7/20 50% Section 338 tariff** on broad Canadian goods = fresh sentiment re-escalation into the thaw; reporting notes the boycott has shifted "from emotional protest into logistical habit." Unchanged conviction, higher variance.
5. **⚠️ VX REFRESH — 7 vectors re-pulled live; two of MARCO's own surfaces were wrong in OPPOSITE directions.** Prompted by Will catching an unverified universal claim built from an inbound packet while **42/57 vectors sat >60d stale**. Corrections: **FL-01 hospitality wages REVERSED** (CRITICAL→NORMAL, "DEMAND WEAKNESS" label falsified — see #2); **3.01 household insurance cost STALE-FLAGGED with NO figure adopted** (secondary aggregators span **$3,815–$8,458**; the carried "4.5x national" doesn't reproduce — needs FL OIR primary). **Level breached, momentum broken**: FL still the most expensive state (~2.8–3.3x national) but premium growth decelerated from ~+18% (2025) to ~+2% projected (2026). **Critical distinction now written into both rows: VX-3.01 = household cost (breached) ≠ VX-SFE-03 = Citizens insurer-side exposure (improving). They moved opposite ways; migration responds to the household number.**
6. **Other refreshed:** condo **8.1mo June** (median +1.7% = first positive; MAR-08 dead); **MIA May +0.52%** YoY (intl +3.52%, domestic −1.75%), YTD −0.47%; **Citizens PIF corrected 385K → 278,246** (Jun 30) with the rate cut effective **7/1 not 6/1**; migration proxies **FLHSMV +3.0% H1 / voter-net −0.8% May** (flat — no acceleration, no recovery). **MCO still JS-blocked** (re-verified 7/25) → BTS T-100.
7. **Predictions marked:** MAR-14 **74%→45%** (also reconciled a 74-vs-55 STATUS/TSV drift to one number), MAR-12 **60%→35%**, MAR-24 **45%→60%** (caveated), MAR-22 hold 50% (blocked on MCO). ES-MARCO-01 resolved **DID_NOT_APPEAR** (FL-state leg failed — FL L&H *added* jobs), ES-MARCO-05 → **RECEDING**.

**Net:** No thesis break — but the first genuinely **negative** evidence in months, and MARCO took it on a test it wrote itself. Channel 1's mechanism is untouched and is now measured by a **cleaner instrument** than before; the produce terminus is what failed. Florida reads as **bifurcating along a supply/demand seam**: labor supply tightening (wages +8.75%), air capacity deleting via carrier failure rather than boycott, household costs high but decelerating, distress concentrating in SW-FL metros that statewide blended metrics cannot see (CORAL/ATTOM overlap).

---

## 7/9 UPDATE (session 17) + 7/2 UPDATE (session 16) — ARCHIVED

*Both blocks moved to `domain/sources/_archive/STATUS_prior_header_s17_and_earlier.md` (7/25, s18b) for the 250-line cap. Canonical session history → `thesis/CHANGELOG.md`. Load-bearing content from both is already folded into the dashboard, ACTIVE SITUATIONS and the 7/25 block above. Note: several s17/s16 reads have since been superseded — the ES-MARCO-08 'contamination watch' resolved (it never contaminated), the energy watch stood down, and the FL Citizens policy count was corrected 385K → 278,246.*

---

## SIGNAL DASHBOARD

| Indicator | Value (2026-05-31) | Status |
|-----------|--------|--------|
| DHS Shutdown | **ENDED Apr 30** (Trump signed; 76-day record). TSA/FEMA/CG/CISA/SS funded. ICE/CBP carved out → reconciliation. | 🟢 RESOLVED |
| ICE/CBP Reconciliation | **SIGNED INTO LAW Jun 10 (6/15 update).** After missing the Jun 1 deadline + Byrd carve, GOP reworked to comply and passed **Senate 52-47 (Jun 5) / House 214-212 (Jun 9); Trump signed Jun 10.** ~$70B (ICE + parts of CBP; $38B/$26B split = pre-trim May-4 proposal, enacted split pending signed-text reconciliation), funds **through end of term (Jan 2029).** Enforcement FLOW now law (trimmed from $71.7B via Byrd rework). | 🔴 LOCKED — LAW (was 🟠 CONTESTED) |
| Produce / CPI F&V | **+5.71% YoY Jun** (fresh F&V `SAF1131`, BLS API live) — DOWN from +6.74% May / +6.51% Apr; **−1.05% MoM**. Broader F&V +5.31%. **ES-MARCO-08 RESOLVED AGAINST LABOR:** gasoline −9.68% MoM (energy −5.7%, largest since Apr'20) and produce fell WITH it = freight branch. **Thermometer demoted to weak-corroboration-only (v2.7).** | 🔻 DEMOTED — no longer a Channel-1 readout |
| ICE Ag/Construction Raids | **AG: eased off farms** (harvest-protection). **CONSTRUCTION: ACTIVE** — the "off worksites" pivot was AG-ONLY (Tallahassee 100+/San Antonio; May South starts −17% MoM). Q4 ag-resumption risk (funding now law). | 🟠 AG-OFF / CONSTRUCTION-ON |
| H-2A Bottleneck | Red River Valley potato delays; South Africa consular interviews → July (past planting). FY26 demand accelerating. | 🔴 LIVE |
| FL Condo Inventory | **8.1mo Jun** (8.9 Apr → 8.6 May → 8.1 Jun, 3rd straight decline); median **$305K +1.7% YoY = FIRST POSITIVE**; closed sales **+14% YoY**. **MAR-08 (>9.0) decisively DEAD.** CORAL caveat: blended statewide strength masks vintage bifurcation (SE-FL 30+yr pending $313/sf, −9%). | 🟢 ABSORBING |
| Canadian Visitors to US | **Jun (StatCan 7/13): 1.7M return trips +3.2% YoY (3rd consecutive)** — but **2-yr stack −28.7%** (auto −29.6%, air −25.0%). **TOUR-01 (<−25%) HOLDS.** ⚠️ **Air stack NARROWED −28.4% → −25.0%** — now sitting ON the threshold; air is the FL-snowbird leg. Counter: **Trump 50% Section 338 tariff on Canadian goods 7/20** = fresh sentiment re-escalation into the thaw; boycott reportedly shifted "emotional protest → logistical habit." | 🔴 STRUCTURAL (air leg narrowing, higher variance) |
| Intl Arrivals (NTTO/overseas) | **Apr 2026 overseas −14.1% YoY** (2.6M; −26.5% vs 2019); non-US-citizen air −9.8% YoY (4.5M); YTD overseas −4.3%. ⚠️ **Apr partly Easter-timing + Iran-war distorted** (per TOURISM IVF-26) — not clean structural deterioration; the durable read is "stuck 14–26% below 2019," not the −14.1% point. | 🟠 STUCK <2019 |
| FL Airports (May) | **FLL May: 2,255,277 −10.7% YoY / −26.1% 2-yr stack; intl 319,493 −27.5% / −48.7% stack** (Broward PDF primary, pdfminer 7/25). ⚠️ **ATTRIBUTION = SPIRIT LIQUIDATION 5/2/26** (31.4% FLL share, 11M pax 2024, primary C/S-America link); **JetBlue backfilled +75% departures** (share 22%→37%) → net ≪ gross. **SUPPLY shock, NOT FL demand — do not route as tourism deterioration.** **MIA May +0.52% YoY** (intl +3.52%, domestic −1.75%); YTD-May −0.47%. **MCO still JS-blocked** (re-verified 7/25) → BTS T-100. **MAR-24: FLL negative, MIA ~flat, MCO unknown → 60%, caveated.** | 🟠 FLL SUPPLY-SHOCKED / MIA FLAT |
| Canadian Airline Capacity | **Air Transat COMPLETE US exit Jun 30** (executed); AC winter 26-27 zero new FL routes + **now canceling 3,000+ flights** on the boycott (7/2 verify); **WestJet 41 intl routes cut (57% US), summer −32% ASM**; Cdn carriers −450K seats Q1. | 🔴 DELETING |
| LAS / NV (Apr) | **LVCVA Apr (6/8): total visitors 3.28M −1.8% YoY; convention +3.2%; occ 83.1%; ADR record $190.41.** LAS airport pax −7.1% Apr (harsher metric); NV gaming +5.3% Apr. Bodies down, dollars up (high-end/convention substitution). **ES-07 (>5% decline) NOT breached on visitor-volume.** | 🟠 BODIES↓ $↑ |
| Mexico Remittances | **May +3.8% YoY** ($5,611M; 4th straight growth month). Count **−1.7% YoY** (SDL-01 tell intact), avg transfer **+5.6%/$404**. Jan-May $25.29B (+2.8%, record period). Mother's-Day (May 10) seasonal high. **Pull-forward paradox normalized; no Q2-Q3 air-pocket; count still neg = SDL-01 tell intact.** *(Confirms the garbled "$5.69B/+26% Apr" trade-press claim was a mislabeled MAY figure, as hypothesized 6/2.)* | 🟡 NORMALIZING (count-tell intact) |
| NFP June 2026 (7/2) | **+57K** (May revised DOWN to +129K from +172K); UE **4.2%** but LFPR **61.5% = lowest 50yr ex-Covid**; household emp **−507K** (June); **total LF −1M+ YoY** (≈ foreign-born LF decline); net migration halved. **L&H −61K** *during* World Cup ("weak seasonal hiring") = **ES-01 mask INVERTED** (May +70K→June −61K). | 🔴 SDL-01 VISIBLE + WC-MASK INVERTED |
| FL Net Domestic Migration | 22,517 (93% collapse); Miami −2.0% — STALE (annual Census, no new print). **⚠️ 7/9: BofA-internal (SKIP-VERIFY 0.72) claims Miami/Orlando/Tampa net-negative Q1'26 — divergent vintage/basis, NOT reconciled; canonical figure unchanged pending CORAL reconcile.** | 🟡 STALE |
| LFPR — Less-Than-HS-Diploma, 25+ (7/9) | **43.1% Jun'26 vs 49.0% series-high Jul'25** (FRED LNS11327659, live-verified) — 5.9pp drop in 11mo, accelerating (Apr 45.0→May 44.0→Jun 43.1). Immigrant-weighted proxy (education ≠ nativity) — corroborating texture for SDL-01, not an independent print. | 🟠 CORROBORATES SDL-01 |
| **FL Hospitality Wages — ❌ FALSIFIED as a Channel-1 instrument (7/25b)** | **FL L&H AHE $23.99 Jun'26 vs US $23.62 = +1.6% ABOVE national** (carried row said 11% BELOW at $20.74 — Jan vintage, REVERSED). **FL +8.75% YoY vs national +3.87%, 3 straight months >2x national** (BLS CES `SMU12000007000000003` vs `CES7000000003`, live API). Wage series carries no freeze/tariff/diesel confound → replaces produce CPI as the Channel-1 readout. **The panel ran and killed it:** TX L&H −6.45pp vs national and FALLING despite maximal immigrant exposure + no state minimum above $7.25; CA −1.94pp; AZ −1.05pp. FL's cell is **Amendment 2** ($13→$14 Sep-30-2025→$15 Sep-30-2026 = 7.7% statutory floor rise inside the YoY window). Reclassified: a **statutory-cost variable in CARL's lane**, not a MARCO population signal. Forward: floor steps $14→$15 Sep 30 2026 = dated ~7% FL services-cost impulse in Q4. | ❌ FALSIFIED — not a MARCO signal |
| E-Verify | ✅ OPERATIONAL | 🟢 ACTIVE |

**Composite (rev 7/31 — session 19):** **Channel 1 DEMOTED FROM SPINE — quantity HIGH, transmission UNDEMONSTRATED.** Mechanism/quantity intact and untouched (H-2A ~455-465K pace on 254,688 certified thru Q2, LFPR 61.5%, foreign-born LF −700K YoY, less-than-HS LFPR 43.1%); but **all three transmission instruments are now dead** — produce CPI (ES-MARCO-08 → freight), wage divergence (statutory-floor artifact), and the floor-controlled re-test (NULL under both controls, TX negative every month, detection floor ~6pp > the 4.88pp signal it was meant to test). **Channel 2 is now the highest-conviction transmitting channel by default.** *(Prior composite, 7/25: "Channel 1 RE-INSTRUMENTED, not weakened" — that read is superseded; the replacement instrument it referred to was falsified the same session and the follow-up test confirmed the null.)* **Channel 2 unchanged, higher variance**: TOUR-01 holds on the −28.7% stack but the air leg narrowed to −25.0% (on the line) while a fresh 50% Canada tariff (7/20) re-arms sentiment. **FL acute-stress layer still NOT firing on MARCO's own metrics** (condo 8.1mo dead, FL L&H adding jobs, Citizens de-escalating) — but that is now understood as **statewide-blend masking metro concentration**, not as absence: ATTOM puts the national foreclosure epicenter (Punta Gorda #1, Cape Coral, FL #1 state) in exactly MARCO's SW-FL snowbird/migration geography. **FLL −10.7% excluded from the composite** — Spirit-liquidation supply shock, not demand. *(Prior composite, 6/15: 4 structural-hardening / 4 reversed-softened / 2 stale.)*

---

## NEXT SESSION FOCUS

**→ Forward planning lives in `SCRATCH.md` (NEXT SESSION section) — single source of truth, refreshed every close.** Near-term at-a-glance is the KEY DATES block below + `docket/CALENDAR.md`. *(The old 5/31 tier-list here was pruned 7/2 — all items resolved/superseded; MAINTENANCE T2-A.)*

---

## ACTIVE SITUATIONS

### DHS Shutdown — RESOLVED (🟢, was 🔴 CRITICAL)
- **Ended Apr 30, 2026.** Trump signed bill funding TSA, FEMA, Coast Guard, CISA, Secret Service. **76-day record shutdown.**
- **ICE/CBP deliberately carved out** of the funding bill → routed to partisan reconciliation.
- TSA: callout ~10.6% post-shutdown (down from 12.4% Mar 27 peak), still above ~2% normal. 1,110+ quit since Feb; new hires need 4-6mo training → lingering capacity drag into summer, but acute crisis over.

### ICE/CBP Reconciliation — SIGNED INTO LAW Jun 10 (🔴 LOCKED, was 🟠 CONTESTED — RE-LOCKED 6/10)
- **Signed Jun 10 2026:** after missing the Jun 1 deadline + the parliamentarian's Byrd carve, GOP reworked the bill to comply and it passed **Senate 52-47 (Jun 5) / House 214-212 (Jun 9); Trump signed Jun 10.** ~$70B, funds **ICE + parts of CBP through end of Trump's term (Jan 2029).**
- **Sub-split caveat:** do NOT cite "$38B ICE / $26B CBP" as enacted — those are the pre-trim May-4 $71.7B *proposal*; the signed ~$70B allocation is **pending signed-text reconciliation.** Some CBP/HSGAC provisions were trimmed via the Byrd rework.
- **Correction to the 6/2 framing:** I'd downgraded this structural→CONTESTED after the Jun-1 miss + Byrd carve. That read is **superseded** — the flow is now law, not just intent.
- **Implication for SDL-01:** the durable-accelerator claim is RESTORED. The 2.2M *stock* loss was always the irreversible spine; the *flow* of new enforcement funding is now **funded by law through Jan 2029, re-locked** (not uncertain). **Channel-1 conviction UP.** Logged to thesis v2.5 (CHANGELOG).

### Produce Price Spike — REAL BUT MULTI-CAUSAL; THERMOMETER DEMOTED (🟠, was 🔴 "PRIMARY LIVE SIGNAL" — DECOMP RESOLVED 5/31, thesis v2.1)
- **🔴 7/25 — THERMOMETER RETIRED (thesis v2.7).** The forward test below (ES-MARCO-08) **resolved AGAINST labor**: June gasoline −9.68% MoM (energy −5.7%, largest since Apr'20) so the pump-relief premise held, and fresh F&V fell *with* it (+6.74%→+5.71% YoY, −1.05% MoM) = the **freight** branch of MARCO's own fork. Produce CPI demoted a 2nd time → **weak corroboration only; do not cite F&V as Channel-1 evidence in either direction.** Replaced by the **wage instrument** (FL L&H +8.75% vs national +3.87%). MAR-14 74%→45%; ES-05 → RECEDING.
- CPI Apr 2026: **fresh fruits & vegetables +6.1% YoY** (up from +4.0% Mar); **fresh vegetables +3.1% MoM**; fresh fruit +1.2% MoM. Food-at-home +0.7% MoM / +2.9% YoY. *(Spike is real — not in dispute.)*
- **ATTRIBUTION RESOLVED (deep-research + external-primary verification):** the spike is MULTI-CAUSAL — **labor (SDL-01) is one co-driver, NOT the dominant/clean signal STATUS previously claimed.** A slow labor *stock* drift doesn't produce a one-month +4.0%→+6.1% *acceleration*; supply/cost shocks do. Verified co-drivers: (1) **FL freeze** Dec'25–Feb'26, **$3.17B, USDA disaster declaration**, hit berry/tomato crops — *fleet blind spot, nobody caught it*; (2) **Mexican tomato tariff** 17% AD duty (Jul'25); (3) **diesel/freight** from the oil-war spike. Crop-"fingerprint" confounded by the freeze.
- **Diesel/freight is TRANSIENT (BRENT cross-check, session 8):** crude $87.51 (Apr 17) → $116.55 (May 5 peak) → **$92.05 (May 29, −19% on month)**; distillate ~11% below 5-yr (structurally tight → relief partial/lagged); pump relief lands **May 31–Jun 14**. The freight contribution was a spike-window pulse feeding the Apr print and is **now reversing.** Edge logged → `COUPLINGS.md` (MARCO↔BRENT). 
- **Forward test (ES-MARCO-08):** if F&V CPI holds ≳+5% YoY into **June 10 / July CPI while pump prices fall** → transient driver exiting, labor re-weights UP. If F&V softens with diesel → freight carried more of the spike. This discriminates the labor-vs-transient split.
- **Correction note:** I first called the freeze fabricated (fleet silence) — WRONG; verified real via USDA + multiple outlets. Full record + analyst-error log → `domain/sources/PRODUCE_ATTRIBUTION_DECOMP_2026-05-31.md`.
- **Implication:** v2.1 splits Channel 1 — labor-shock **mechanism HIGH/intact**, produce CPI **thermometer MEDIUM/confounded**. Stop citing "+6.1% produce" as strong labor proof. **MAR-21 RESOLVED (wrong-mechanism).** Exact %-split unknowable; directional conclusion (labor over-credited as the produce driver) is robust.

### ICE Ag Enforcement — PIVOTED OFF FARMS (🟠, was 🔴 EXPANDING)
- Reporting (Stateline Nov 2025; ag-press May 2026): ICE **refraining from agricultural worksite raids**, concentrating on Democratic-led cities. Harvest-protection motive explicit.
- The Apr-23 "expanding to rural ag/meatpacking" framing has reversed *on the raid vector specifically.*
- **Caveat:** the labor-supply shock already happened and is structural — produce prices reflect the *stock/level* loss, not new raids. And if enforcement returns to ag post-harvest (Q4 2026), transmission re-accelerates. *(Magnitude re-marked v2.6: **~1.0M realized foreign-born LF decline / ~1.5M pop**, NOT the previously-cited "2.2M CBO" — that was a mis-attributed disputed-DHS claim; see 7/2 UPDATE #1 + thesis magnitude note.)*

### H-2A / Ag Labor (🔴 — bottleneck persists)
- Red River Valley (MN/ND) potato growers: H-2A delays threaten 2026 crop. South Africa consular interviews backed to **July** (past planting).
- ~44% of ~2M US farmworkers undocumented (govt surveys). Structural trend toward larger industrial farms + mechanization as small farms lose labor access.
- NASS Farm Labor Survey still CANCELED (Aug 2025) — permanent data blind spot. Replacement framework: OFLC H-2A disclosure, BLS QCEW NAICS 11, NASS Crop Progress, State Dept visa issuances, CPI F&V. (→ `domain/sources/LABOR/AG_LABOR_ALT_SOURCES_MAR26.md`)
- Prediction #11 (H-2A >425K FY26) **on track → upgraded 80→88% (7/2):** OFLC H1 FY26 certified **254,688 (+16.9% YoY)**; front-loaded season projects ~455–465K full-year, comfortably above 425K. FY25 certified 398,258 (record). Bottleneck = processing, not demand.

### Canadian Travel — STRUCTURAL (🔴, re-classified from 🟠 BIFURCATED — session-9 full refresh)
- **🟡 7/25 — June: stack holds, air leg narrowing into a fresh tariff.** StatCan (rel 7/13): 1.7M return trips **+3.2% YoY** (3rd consecutive) / **2-yr stack −28.7%** (auto −29.6%, air −25.0%) — TOUR-01 holds. **The air stack narrowed −28.4% → −25.0%** and now sits *on* the threshold — that is the FL-snowbird leg thawing at the margin against still-deleted capacity. Counter-force: **Trump's 7/20 50% Section 338 tariff** on broad Canadian goods re-arms the sentiment driver; reporting notes the boycott has shifted from emotional protest to **logistical habit** (stickier). Net: conviction unchanged, variance up. **NB: FLL's May collapse is NOT this channel** — Spirit liquidation, see dashboard.
- **Macro frame (v2.4):** the boycott sits *inside* the **first US inbound-tourism decline in 20 years** (CY2025 −5.5%, 68.3M; overseas stuck 14–26% below 2019). Canada is the sharp edge, not the whole story. **FIFA World Cup (Jun 11–Jul 19) is the live reversal test** — Q2 not yet encouraging; if it doesn't pull inbound back above 2019, structural read hardens. *(Owner: `thesis/THESIS.md` Channel 2 / KB-MARCO-IVF-27 → ES-MARCO-09.)*
- **The April "recovery" was base-effect.** StatCan Mar-full (May 21): 2.6M, −6.4% YoY but **−28.0% vs 2024**. Apr prelim: 1.85M, +1.4% YoY but **−30.0% vs 2024** — the 2-yr stack *worsened* even as the headline flipped positive. Absolute Canadian volume still sliding; the comparison base eased, not the boycott. TOUR-01 (framed on the stack) confirmed; conf 80→85.
- **Sentiment NOT softening:** Nanos May 3-6 (n=1,003) — **82% call the boycott "helpful"** (53%+29%). A May reading, post any trade-thaw. 15th+ consecutive month of decline.
- **Air ≠ auto:** auto (same-day land) drives the headline bounce (+5.8% Apr); **air −8.1% Apr / −10.8% Mar** — the snowbird/FL-relevant channel, structurally negative and its capacity permanently deleting. FL $ rides on air.
- **MIA flipped negative** (Mar −1.76%, Apr −2.02%; Apr domestic −3.27% = new broader-demand signal) → TOUR-04 RESOLVED-CORRECT. But **MAR-24 (all 3 FL airports negative) NOT met** — FLL +10.2% Mar / MCO record spring break print positive on base-effect (lapping depressed 2025). Base-effect protects FLL/MCO headline.
- **Capacity deletion locked:** Air Transat **complete US exit Jun 30** (YUL-FLL last flight; YUL-MCO May 4, YQB-FLL May 30); AC winter 2026-27 zero new FL/US routes (dropped YVR-Tampa; 11 new snowbird routes all non-US); WestJet 41 intl routes cut (57% US) spanning winter forward bookings, summer −32% ASM; Cdn carriers −450K seats Q1. TOUR-03→90%, TOUR-05→85%.
- **Asymmetry widening:** US→Canada Apr +7.3% (air +10.8%); Q1 BOP (May 28) — Canada now net travel-services exporter (+$1.3B), US-travel spend declining.
- **$ stress delayed not absent:** NV shows the pattern early (LAS pax −7%, gaming +5% on high-end/convention substitution). FL Canadian-$ hole lands **winter 2026-27** ($600M-$1.2B) → REGINALD bank/CRE stress Q1-Q2 2027. Detail: `domain/sources/TOUR_REFRESH_2026-05-31.md`.

### Mexico Remittances — PARADOX SOFTENING, NORMALIZING (🟡)
- **Banxico Apr 2026 (released ~Jun 1):** $4.98B, **+3.7% YoY** — YoY *decelerating* from +4.9% Mar. Jan-Apr cumulative $19.68B, **+2.6% YoY** — record for the period. MoM −9.47% is **Easter seasonal** (fewer working days), not signal.
- **The paradox is fading, not deepening:** transfer **count −1.7% YoY** (narrowing from −3.6% Mar); avg transfer **+5.5% / $403** (premium compressed from +8.9% / $417 Mar). The "fewer, larger transfers" tax-pull-forward signature is *softening* toward a normal pattern — argues *against* a sharp pull-forward-then-air-pocket.
- **What survives:** the count is **still negative YoY** — the structural SDL-01 tell (fewer senders in the US) persists even as dollar value and avg-transfer normalize. Full-year 2025 was −4.6%.
- **Read:** lean "no dramatic Q2-Q3 collapse; pattern reverting toward normal." Not a labor-income *recovery* (count still negative), but not the air-pocket either. Pull-forward hypothesis partially supported (premium shrinking as Jan-tax distortion ages out) but no cliff. Keep watching count YoY as the cleanest SDL-01 readout.

### Energy Re-Shock → FL Tourism/Cost Channel — ✅ STOOD DOWN 7/25 (was 🟡 WATCH 7/9)
- **RESOLVED — the re-arm did not sustain and the threshold was never approached.** June energy fell **−5.7% MoM** (largest 1-month drop since April 2020) with gasoline **−9.68% MoM** — the opposite of the feared squeeze. Brent never came near the **$85 sustained-2wk** re-engagement threshold set 7/9 (7/9 settle was $76.01; the Spirit precedent fired near $116). **Second-order win: the feared ES-MARCO-08 contamination never happened**, so the test ran clean (and resolved against labor — see Produce). Stood down; re-arm only on a fresh sustained >$85.
- **Mechanism:** Iran truce collapse (7/7-7/8, Brent spiked $78.82) + Russia diesel-export ban (7/9, Saratov refinery halted) = sustained-Brent re-arm per fleet regime (BRENT/HAWK). Two downstream legs for MARCO:
  1. **Airfare/capacity:** Spirit Airlines' 5/2 SDNY liquidation = precedent for jet-fuel-cost-kills-marginal-carrier (~$100M cost spike Mar-Apr, Iran-strike-driven, per WALTER SIG-008) — but that fired when Brent approached **$116 (May 5 peak)**, well above the current **$76.01 (7/9 settle)**. **Threshold set: sustained Brent >$85 for 2+ weeks** before treating this as a live risk to FL-relevant airline capacity (already deleting on the Canadian boycott independent of energy). DOT Transport CPI +9.3% YoY (April) is the confirming datum to re-check.
  2. **ES-MARCO-08 contamination:** my own produce-vs-pump discriminating test (due ~Jul 15 CPI) assumed the pump-price relief window (Brent $91→$83 mid-June) held through the print. The 7/8-7/9 re-arm risks closing that window early — if pump prices reverse before Jul 15, the test can't cleanly discriminate labor vs freight this cycle. Flag to BRENT/PROME before citing ES-MARCO-08 either way.
- **Not a threshold breach — a pre-position for HAWK's Russia-flag / Friday 7/10 BRENT sustain-verdict cross-flag.** Revisit at $85 Brent or the next CPI print, whichever comes first.

### Florida Triple Exposure — COOLING (🟡, was UPGRADED)
- **⚠️ 7/25 — the three legs now point in THREE directions, and the statewide blend hides it.** **Insurance:** split into two vectors that moved *opposite* ways — Citizens' insurer-side exposure de-escalating (PIF corrected 385K→**278,246** Jun-30, rate cut eff **7/1** not 6/1) while **household cost (VX-3.01) stays breached** at ~2.8-3.3x national, most expensive state in the US; momentum broken though (+18% 2025 → ~+2% 2026E). **Migration responds to the household number, not the insurer's balance sheet — do not substitute.** No figure adopted; needs FL OIR primary. **Tourism/condo:** condo 8.1mo (MAR-08 dead), FL L&H *adding* jobs, FL UR 4.7% first decline since 2024, Orlando TDT record — statewide metrics benign. **But:** ATTOM H1-2026 puts the **national foreclosure epicenter — Punta Gorda 0.50% (#1 US), Cape Coral 0.35%, FL #1 state (0.27%)** — in exactly MARCO's SW-FL snowbird/migration geography, with Cape Coral carrying the #1 US negative-equity share (11.1%). **Read: stress is metro-concentrated and statewide blends cannot see it** — an instrument problem, not an absence. → CORAL joint reconcile (open 7/17).
- Condo inventory **8.6mo May** statewide (↓ from 8.9 Apr; inventory −13.4% YoY, sales +6.6% 9th straight). Miami-Dade May: median $415K (−2.35% YoY), sales +5.4% (9th straight up), inventory declining (~12.9mo elevated but absorbing; days-to-sale 106); PB 8.2mo. The distress-inventory thesis softened — supply absorbed, not piling up (MAR-08 >9.0 not met).
- Migration (93% collapse, Miami −2.0%) stale — annual Census, no new print.
- Airports (session-9 update): **MIA flipped negative** (Mar −1.76%, Apr −2.02%); FLL +10.2% Mar but base-effect; MCO record spring break (domestic anchor). Canadian/discretionary weakness concentrated in air + winter capacity, not yet aggregate FL airport volume.
- Insurance (FL Citizens) — **RE-MARKED 7/2 (live-verified): crisis PAST-PEAK.** Exposure **~$295.1B (June'25, −43% YoY from $520.1B)**, 67% below peak entering 2026; ~385K policies (lowest ever). **MAR-17 (>$750B) INVALIDATED.** Rates now being **CUT** — Citizens filed −2.6% personal-lines cut for Jun'26 (reversing a +15% ask 6mo prior; 2022 reforms working; commercial +10.4% the exception). Crisis easing on exposure AND personal rates, not just risk-shifted. FL insurance → CORAL's domain, reconcile.
- **Net:** FL acute-stress timing pushed right; aggregate $ stress still projected for **winter 2026-27** (snowbird no-show, $600M-$1.2B), not Q2-Q3 2026.
- **FL labor cooling context (WALTER SIG-007, 6/19, April UCF data):** FL jobless **4.8% > US 4.3%** — FL no longer outperforming post-COVID; UCF forecasts payroll growth slowing to 0.1% 2026, slight contraction 2027. Directional support for the cooling read; not yet independently re-verified this session.
- **Forward driver, new (7/9):** FL property-tax amendment (Nov 3 2026 ballot, Amendment 3/HJR 1F) caps new-resident (post-12/31/26) homestead exemption at $50K for 5yr vs existing residents' $150K→$250K — **structurally anti-migration by design** (FL Phoenix: "without fueling a fresh migration wave"). If passed (poll 64%±3.8 vs 60% bar — tight), reinforces rather than reverses the migration-collapse thesis; does not create a new tax-arbitrage pull for movers. Watch Nov 3.

---

## PREDICTIONS (Active)

| # | Prediction | Timeframe | Conf | Notes (2026-05-31) |
|---|-----------|-----------|------|-------|
| 21 | Planting-season raid surge → produce spike | Mar-May 2026 | **RESOLVED** | ✅ RESOLVED 5/31 (window closed) — **WRONG-MECHANISM.** Produce DID spike (+6.1%) but NOT via raid surge: raids eased off farms + H-2A wages cut during window. Spike multi-causal (freeze + tariff + transient freight + labor co-driver). Scored on mechanism, not the print. → PREDICTIONS.tsv + thesis v2.1. |
| 14 | CA produce prices +15% | H2 2026 | **45%** ↓ |
| 26 | ICE construction raids → housing-start delays (TX, AZ, FL) | Q2 2026 | **RESOLVED (7/2)** | ✅ RESOLVED (Q2 window) — **MECHANISM-CONFIRMED / threshold EMERGING.** Construction raids active (Tallahassee/San Antonio). May NRC: **South-region starts −17.0% MoM** — the biggest regional drop, REVERSING April's pattern (South had fallen least) → geography now leans WITH the raid signal. But one MoM print (noisy), no clean South YoY. National SF starts −1.9% MoM; total −8.7% YoY. Starts lag raids 1-3mo → **Q3 is the clean test** (spun forward). Scored on mechanism. |
| 11 | H-2A certifications >425K | FY 2026 | 75% | Demand accelerating; bottleneck = processing, not demand. |
| 24 | All 3 FL airports negative simultaneously | Q3 2026 | **60%** ↑ |
| 22 | OIA/MCO flips negative | Q2-Q3 2026 | **50%** = |
| 25 | ✅ TSA disruption → measurable FL airport delays | NOW | ✅ | RESOLVED-CORRECT. Shutdown ended; thesis played out. |
| 8 | ✅ FL condo inventory >9 months | Q2 2026 | ✅ | RESOLVED-CORRECT (9.1mo Mar). NB: reverted to 8.9mo Apr — one-month breach, now tightening. |

---

## KEY DATES

**→ Forward state now lives in the docket: `docket/CATALYSTS.tsv` (machine feed) + `docket/CALENDAR.md` (countdown).** Resolved events spine → `thesis/TIMELINE.md`. This section is the at-a-glance near-term cut only.

**Imminent (next ~3 weeks):**
| Date | Event | Priority |
|------|-------|----------|
| **Aug 1** | **Banxico June remittances** — transfer COUNT YoY is the cleanest surviving SDL-01 readout (May: −1.7%, still negative = tell intact) | 🟠 |
| **Aug 1** | OFLC H-2A Q3 FY26 disclosure — MAR-11 (>425K, 88%); H1 254,688 (+16.9%) projects ~455-465K | 🟡 |
| **Aug 8** | BLS July NFP — L&H post-World-Cup (ES-MARCO-01) + LFPR / foreign-born LF (SDL-01 quantity). ⚠️ **The state-CES wage leg is NOT a Channel-1 instrument read** (v3.0) — do not re-run the >2pp gap test as a confirm | 🟠 |
| **~Aug 12** | BLS July CPI — ES-MARCO-05 (RECEDING): a 3rd sub-6% F&V print → resolve DID_NOT_APPEAR rather than push a 4th time | 🟡 |
| **~Aug 15** | **NTTO June arrivals (1st World-Cup month)** — ES-MARCO-09 fork: PASS if Jun+Jul overseas ≥5.5M AND ≥−10% vs 2019; FAIL if ≥−20%. Advance signals lean FAIL | 🟠 |
| **~Aug 15** | Banxico Q1/H1 state-of-origin map — SDL-01 *spatial* test: concentrated drop in high-enforcement states = confirmation | 🟡 |
| **Aug 18** | FL Citizens next assumption round (CORAL owns; MARCO reads the depop trajectory) | 🟢 |
| **Nov 3** | FL property-tax Amendment 3 / HJR 1F — caps new-resident homestead exemption at $50K/5yr vs $150K→$250K for existing. **Anti-migration by design.** Poll 64%±3.8 vs a 60% bar — tight | 🟠 |

*Full forward docket (StatCan travel, FL Realtors, Banxico state-of-origin, OFLC H-2A, FL airports, ICE Q4, Census annual) → `docket/CALENDAR.md`.*

---

## CROSS-AGENT SIGNALS

**→ The live cross-agent SENDING surface is `NEXUS_BRIEF.md` (SENDING table) + `outbox/`.** *(The old Apr-21-23 "NEEDS RE-SEND" candidate table was retired 7/2 — figures stale (8.9→8.6mo condo, 2.2M→~1.0M LF, $71.7B→$70B-law) and the re-sends are now handled by NEXUS_BRIEF + this session's LABOR/CORAL/CARL/PROME outbox notes; MAINTENANCE T2-A.)*

---

## UNRESOLVED / PENDING

*(Resolved items pruned 7/25 to `thesis/TIMELINE.md` — remittance paradox 6/2, ICE/CBP reconciliation 6/10, TOURISM shelve, SDL-01 formalization. This table now carries OPEN items only.)*

| Item | Priority |
|------|----------|
| ✅ **VX stale sweep DONE 7/31** — 37 stale rows triaged: **19 FROZEN/RETIRED** (17 abandoned border-fiscal + STR-01 never-built + 2.07), **6 stale-by-design** (annual Census/CBO cadence or no live primary), **2 fixed** (2.02 carried the retracted "2.2M/CBO" for 4 months; H2A-01 refreshed to live OFLC 254,688), **10 stale-marked**. Boot alert now shows **5 real loaded guns**, was 37 undifferentiated | ✅ |
| ✅ **Boot guard BUILT 7/31** — `staleness.py` now ranks **BREACHED/CRITICAL + >60d** as its own 🔴 alert, excludes FROZEN/RETIRED (age by design), and separates **stale-by-design** (awaiting a scheduled print / no primary) from real rot. Validated against the pre-sweep file: fires 25, matching s18b's hand triage exactly | ✅ |
| **VX refresh backlog — 5 named rows, all BREACHED/CRITICAL and genuinely refreshable** (not annual, not dead): **FL-03** FL Days on Market (FL Realtors, monthly — rotting with a live monthly source), **TX-02** Austin Price Decline, **CA-01** CA Wildfire Insurance, **3.02** Sunbelt-Snowbelt Price Differential, **GTR-01** Google Trends Tourism Intent (free live source, 157d). These are the actionable remainder — the boot guard now names them every session | 🟠 |
| ⚠️ **Channel 4 has NO live vector behind it** (surfaced by the 7/31 freeze) — all 17 border-fiscal vectors were untouched since Feb 2026 and are now FROZEN, yet THESIS carries Channel 4 at **MEDIUM**. A conviction resting on a 6-month-old evidence base is the same fault v3.0 just corrected in Channel 1. **Decide: rebuild the vectors or re-mark the conviction.** NB MAR-01's 7/2 resolution explicitly pointed to VX-BDR-03/NOG-01 as where the mechanism lives — that pointer now resolves to frozen Feb data | 🔴 |
| **VX-MARCO-3.01 household insurance cost — NO FIGURE ADOPTED.** Secondary aggregators span $3,815–$8,458; carried "4.5x national" doesn't reproduce. **Needs FL OIR primary** before any number is cited or routed | 🟠 |
| **MCO pax — blocked since session 16.** flymco/GOAA JS-rendered, re-verified 7/25 (no PDF assets in DOM). BTS T-100 is the only path; April should be postable now. **MAR-24 and MAR-22 both now hinge entirely on this** | 🟠 |
| **Wage-panel build (thesis v2.7 follow-through)** — FL/TX/CA/AZ × leisure-hospitality / construction / ag-adjacent vs national, BLS CES public API. Confirms or falsifies the promoted Channel-1 instrument | 🟠 |
| **FL migration divergence → CORAL joint reconcile** (open since 7/9): canonical +22,517 / 93% collapse (2025 annual, Census) vs BofA-internal Miami/Orlando/Tampa net-negative Q1'26 (SKIP-VERIFY 0.72). Divergent vintage + basis; not unilaterally resolvable | 🟠 |
| **ATTOM SW-FL foreclosure overlap → CORAL** (open since 7/17): Punta Gorda #1 US / Cape Coral / FL #1 state sits on MARCO's snowbird+migration geography. The metro-concentration read that statewide blends mask | 🟠 |
| **SDL-01 magnitude reconcile → LABOR + CORAL** (one number: ~700K LF YoY / ~1.0M peak-to-trough). LABOR sourced the old ~1.6–1.9M *to MARCO*; adoption of the corrected figure still unconfirmed | 🟠 |
| **WALTER consume boot-step never installed** (asked 7/11) — mechanical cause of 9 unread SIGs. One-time `CLAUDE.md` edit | 🟠 |
| **Inbox: 17 unprocessed** (8 top-level + 9 WALTER SIGs). Separate spawn per MAIL protocol | 🟠 |
| ES-MARCO-05 → RECEDING: if July + August F&V stay <6%, resolve DID_NOT_APPEAR rather than push a 4th time | 🟡 |
| PREDICTIONS_ARCHIVE + calibration scoreboard (maturity gap, carried s16→s18); PREDICTIONS.tsv mixed col-count (T1-D) | 🟡 |
| VX-MARCO-EMG-01 (emigration) — WATCH/PENDING | 🟡 |
| ICE off-farm pivot: durable or tactical (Q4 2026 ag re-acceleration risk) | 🟡 |

---

## ROLE & DATA SOURCES

**Domain:** Population movement disruptions — international visitor flows, workforce displacement, internal migration.

*Canonical thesis → `thesis/THESIS.md` (v2.0) · Full prediction detail → `thesis/PREDICTIONS.tsv` · Findings index → `FINDINGS.md`*
*SDL-01 → `domain/sources/SDL/` · EMG-01 → `domain/sources/EMG/` · LABOR → `domain/sources/LABOR/`*
*Live tools → `tools/h2a_pull.py`, `tools/slaughter_pull.py`, `tools/banxico_reverse.py`*
*Archived STATUS → `domain/sources/_archive/` (prior: STATUS_2026-04-23_session5.md)*
