# CREED Thesis Rails

**Created:** 2026-06-21 15:10 ET  
**Status:** Current rails. **Split + current-state correction 2026-09-30** (Will-approved; CATO key-files audit CK1): this file now carries **current state only**; the full pre-split text (47,288 B, crc32 `42275fe2`) is verbatim at **`thesis/THESIS_HISTORY_2026-09-30.md`**, the reasoning trail for every figure below. Score history: convergence 20/40 → 23/45 (7/27: S8 split, S5 demoted) → 25/45 (8/20: S2 FIRED) → **27/45 (9/28: S8a 2 → 4, Will-ruled WQ-303; hold confirmed 9/30)**. See CHANGELOG.  
**Scope:** National CRE / CMBS market-stress synthesis. Not a trade recommendation.

---

## Bottom Line

CREED's current base case is **selective CRE recognition accelerating**. **Broad CRE-to-bank transmission is not confirmed.**

> CMBS is showing the pain because securitized loans force recognition faster. Banks are still absorbing/deferring through modifications, reserves, concentration management and liquidity. The edge is not "CRE bad"; it is identifying when maturity-default and special-servicing stress crosses into bank provisions, reserve-coverage deterioration, forced sales or funding pressure.

**Where the distress sits (as of 2026-09-30):** a **capital-structure / maturity** event, not a tenant-demand event. Office leasing improved in Q2 (CBRE +12.6M sf absorption) while CMBS maturity measures kept worsening, and the September equity-tape fire was rate-led. **The binding constraint is the asset against the coupon: refinancing at today's rates.**

**Recognition speed is a property of the *holder*, not just the *wrapper*.** Fast-recognition holders are every publicly marked, quarterly reporting CRE holder (CMBS, commercial mortgage REITs); slow-recognition holders include banks and **insurance balance sheets**. Named instance: **ARI sold its CRE loan book to Athene (closed 4/24/26; ~$9B commitments, $8.7B final per Athene's Q2 10-Q) at 99.7% of commitments; ARI stockholders approved dissolution 9/29/26** (8-K Item 5.07). Track the *migration*, not just the delinquency rate.

---

## Current State Classification

| Regime | Definition | Current read |
|---|---|---|
| Extend-and-pretend still absorbing | Stress is real, but modifications/cures/denominator effects keep headline bank metrics contained | Still active (banks; fund level via the SREIT gate) |
| Selective CRE recognition accelerating | CMBS and specific property types/metros show forced recognition while banks remain uneven | **Base case** |
| Broad CRE→bank transmission | Bank PDNA/provisions/nonaccruals/funding stress confirm CRE losses moving onto financial-system balance sheets | **Not confirmed** |

**Current evidence** (dated; primary unless marked):
- **Trepp AUGUST 2026 delinquency [PRIMARY-READ, archived `AGENTS/WALTER/sources/`]: overall 7.85% (−1bp); office 12.00% (+9bp); retail 7.20% (+24bp); lodging 5.84%; industrial 1.14%; multifamily 7.69% (unchanged; HOMER-owned, cite HOMER).** The flat headline hides the maturity book: **maturity-adjusted DQ 9.81% (+19bp)**, its gap to headline widening 176 → 196bp as performing matured balloons accumulated (1.76 → 1.96% of balance). ⚠️ Headline basis (defeased included); never mix Trepp's CMBS-2.0 set.
- **Composition: non-performing matured balloon = 81% of August's newly delinquent balances**, the 4th consecutive print above 50 (`CREED-T-02` fired 8/20, spent). ⚠️ **August printed no newly-delinquent dollar total, so no shape word is written** (trap #6). The dollar series (`VX-3.05`) peaked at **$3.96B in July**.
- **Trepp AUGUST 2026 special servicing [PRIMARY-READ]: overall 11.42% (+33bp, highest since Feb 2013); office 16.90% (+32bp), 110bp below the >18 line and moving toward it.** Transfers in $3.16B / 32 loans (~2× July), mostly imminent-maturity-default rather than payment distress (Trepp). Office SS−DQ spread 4.90pp; ⚠️ its sign is not an instrument (`KB-CREED-034`): read the gross flows.
- **Maturity wall:** >$100B 2026 CMBS maturities, >50% expected not to repay; Trepp hard maturities **$76.6B, 39% in Q4, 36% at debt yield ≤8%**. Sept hard maturities $2.74B (office 54%).
- **FDIC Q2 2026 [QBP pub 8/25, PRIMARY-READ]:** overall PDNA 1.44% (−9bp); >$250B nonfarm-nonres CRE PDNA **2.48% (−25bp)**; reserve coverage 172.7% industry / **145.6% community banks**. `CREED-T-03` NOT FIRED 8/27; S3 held at 2. ⚠️ Composition leans recognition, not healing: regional CRE OREO **+26.4% QoQ**, large-bank CRE charge-offs +57% QoQ (`KB-CREED-023`). ⚠️ A clean print is not "no CRE stress at banks": unsecured CRE books as C&I (scope limit, REGINALD's to close).
- **CRE lender cohort (census 2026-09-26): 4 of 11 cut or liquidating** (ARI wind-down, stockholders approved 9/29; KREF −60%; RC −92%; GPMT $0.05 → $0.01 + formal review 9/23); **7 held Q3**. Q2 book-value erosion **concentrated** (GPMT −19.1%, KREF −13.7%, RC −8.1%, BXMT −4.4%; rest −3.4% to +0.4%). `CREED-T-08b` graded NOT FIRED 9/26.
- **CRE equity tape:** `CREED-T-08a` **FIRED 9/24** (VNQ vs SPY 3-mo TR −10.12pp; −13.06 on 9/25), a **rate fire** (10y 4.38 → 5.18% on the window; FOMC +25bp 9/16). **9/30 close −9.14pp TR (9/29 −7.89), inside the band, 0.86pp from it; the step is inside noise (10-session σ 2.85pp). The fire stands; S8a = 4 (Will, 9/28; hold confirmed 9/30).** Recompute with `scripts/s8a_relative.py` before citing.
- **Realized recognition (cluster, not an instance):** 205 W Randolph −72% realized; Aon −58% appraisal; Galveston $8.79/sf; OZK Seattle deed-in-lieu; **3000 Post Oak (Houston) CMBS REO sale 9/28: trusts netted $11.4M on an $80M senior** (`KB-CREED-046`). 2026 CMBS loss severity CREFC Jul 48.8% / Aug 72.6%, all-types YTD 35% (`KB-CREED-041`).
- **Insurer absorption:** MBA Q2 life-insurer CM/MF holdings **+$7.8B → $781.6B** (whole loans only, a floor on insurer CRE; `KB-CREED-047`).

Source trail: `research/REFRESH_2026-07-27.md` is the **prior** pack (CRE lender leg, June SS, life-science bifurcation); it predates the T-02 fire and the August prints. `REFRESH_2026-07-04.md` / `REFRESH_2026-06-21.md` are older trails. Current figures live in `workbook/VX.tsv` and the catch-ups.

---

## Mechanism Map

### 1. Maturity-default channel
Loans can still cash-flow and still default at maturity if refinance proceeds no longer cover prior debt. **The cleanest 2026 CREED forcing function, and now the one firing.**
Watch: non-performing matured balloon share **and dollars** of new CMBS delinquencies · hard-maturity loans with no extension options · low debt-yield cohorts (≤8%) · the Q4 2026 maturity bulge.

### 2. Special-servicing / appraisal channel
Special servicing forces updated appraisals, modification decisions or liquidation paths. Large-loan cures/returns can improve headline rates without genuine market repair.
Watch: SS rate by property type · transfer volume and largest transfers · repeat transfers / re-defaults after modification · office and mixed-use concentration.

### 3. Bank-recognition channel
Banks can lag CMBS because they can modify, extend, reserve or hold collateral at non-market-clearing marks. The trade-relevant signal is convergence: bank PDNA/provisions/charge-offs catching up to CMBS stress.
Watch: FDIC non-owner CRE PDNA by bank size · community/regional reserve coverage · provision spikes and CRE charge-offs · modifications and second modifications · CRE OREO · FHLB/repo/funding usage if CRE losses force liquidity needs.

### 4. Multifamily property-level channel
Multifamily is not only a maturity wall: term defaults tie to occupancy, operating costs and local weakness. **HOMER owns MF scoring** (see S5).

### 5. Forced-sale / NAV channel
CRE valuation truth appears when assets transact under pressure; forced sales turn private marks into comparable marks.
Watch: sales >30% below prior appraisal / loan basis · **open-end fund gates: OBSERVED (SREIT, eff. 2026-04-29; `CREED-T-06b` fired 8/27), and a gate BLOCKS recognition rather than showing it** · redemption-queue reversal · appraisal reductions and LTV covenant breaches · ODCE / private-fund redemption data.

---

## Expected Signals — v1.0 (trigger terms are frozen in `registry/THRESHOLDS.tsv`; this list is descriptive)

| # | Signal | Trigger examples | Response |
|---|---|---|---|
| 🔴 1 | Office CMBS stress re-accelerates | office DQ > 12% and holds (2 prints) · office SS > 18% · multiple gateway-city SS transfers in a month | update tracker; REGINALD if bank-exposed metros overlap; LIQUID if refi-driven |
| 🔴 2 | Maturity-default wave confirms | matured balloons = majority of new delinquencies, consecutive months · >50% of 2026 maturities failing to repay · Q4 hard maturities transferring early | maturity wall = active forcing mechanism; route LIQUID + REGINALD |
| 🔴 3 | Bank CRE convergence | non-owner CRE PDNA re-rising · community/regional reserve coverage deteriorating while CRE noncurrents rise · CRE provisions/charge-offs jump across REGINALD's watchlist | urgent handoff to REGINALD (property/metro/source map, never trade execution) |
| 🟠 4 | Modification exhaustion / re-default | new mods fall as extension capacity runs out · second-mod / re-default rates rise · loans returned to master servicer re-transfer | classify extend-and-pretend as failing in the segment; move toward broad transmission only if bank evidence confirms |
| 🟠 5 | MF term-default broadening — **HOMER-fed cross-reference** | MF DQ/SS uptrend · term defaults dominate new MF delinquencies · DSCR stress in 2022–23 vintages | HOMER scores; CARL for household overlap; CORAL only if Florida-specific |
| 🟠 6 | Forced-sale / private-NAV recognition | large sale >30% below appraisal/basis · fund gates / queue reversal · appraisal marks force LTV/covenant consequences | LIQUID (funding), REGINALD (collateral/LGD) |
| 🟡 7 | Office-demand structural hit, tape-confirmed | REIT selloff **AND** direct tenant-demand impairment · AI/automation cuts showing up in leasing, sublease or vacancy | treat AI as narrative until vacancy/leasing/default data support it |
| 🟡 8a | CRE **equity** tape | VNQ underperforms SPY by >10pp/3mo (total return) with rate/refi or property confirmation · office REIT NAV discounts >50% with confirming data · REIT dividend cuts on NOI/refi stress | update the REIT tape module; never treat REIT price action alone as CRE→bank confirmation |
| 🟡 8b | CRE **credit / lender** tape | dividend cuts or realized book erosion **across multiple names** · a lender exits/liquidates/sells its book · cohort-wide provisioning on risk-rated-5 credits · lenders persistently below book with cuts | LIQUID (lender appetite), REGINALD (collateral), CARL (consumer spillover) |

S5 is **HOMER-owned** (DAEDALUS ruling 7/12, Will-approved; applied 7/27): HOMER owns the Trepp CMBS-MF row, the GSE-vs-CMBS divergence and Sun-Belt MF realization. CREED cites `AGENTS/HOMER/STATUS.md` and never publishes a second Trepp-MF citation as a CREED vote. S8 was split into 8a/8b on 7/27 because the equity and credit legs diverged; numbering 1–8 is unchanged so citations still resolve.

**Discipline on 8b (all live):**
1. **Separate lender ECONOMICS from CREDIT LOSS.** ARI exiting at 99.7% (economics) is not KREF reserving against risk-5 credits (credit loss). ARI's clearing is evidence *against* "marks are fictional" even as its exit is evidence *for* credit withdrawal.
2. **Check corporate actions before reading a price.** ARI printed −33.4% on 7/16 on a $3.75 return of capital. ARI's first liquidating distribution will print the same way.
3. **Count the cohort, not the headline.** 4 of 11 cut or liquidating, 7 held (9/26): selective, not a cascade.

---

## Convergence Matrix (5-pt stackable handle)

Maps the 8 Expected Signals onto the universal 5-pt scale so NEXUS/PROME can stack CREED's read **without spawning this tier-2 agent**. Scale: 5 firing → 4 🔴 elevated → 3 🟠 building → 2 🟡 latent → 1 ⚪ dormant. Independence = shared-antecedent flag. **Reads as of 2026-09-30**; full prior cell texts (as of 9/28) are in the history snapshot.

| # | Vector | Score | Current read [as-of] | Independence | Upgrade trigger |
|---|---|---:|---|---|---|
| 1 | Office CMBS stress | 3 | Office DQ **12.00% [Aug]: exactly AT the `> 12` band, 0 of 2 legs** (12.00 is not > 12; the September print can only start leg 1, graded on `registry/PREREG_2026-10_TREPP_PRINT.md`). Office SS **16.90% [Aug]**, 110bp below >18, moved toward. Not fired. | shares maturity/refi root with #2 | DQ >12% for 2 prints OR SS >18% |
| 2 | Maturity-default wave | **5 🔴 FIRED** | `CREED-T-02` fired 8/20 (effective June; spent). Aug: matured-balloon share 81% (no $ base printed), mat-adj DQ 9.81%, SS transfers ~2× July on imminent maturity default. Dollar series peak $3.96B [Jul]. | one root with #1 | ✅ met |
| 3 | Bank CRE convergence | 2 | FDIC Q2 graded 8/27: `T-03` NOT FIRED. **Basis ruled by Will 8/27: level leg SUSPENDED, re-declared to the QBP combined cell, level revisit at n=12** (`KB-CREED-024`; no ruling pending). Legs (b) direction + (c) reserve coverage graded by hand. Regional CRE OREO +26.4% QoQ is the Q3 watch. **Next test: FDIC Q3 QBP ~late Nov** (DOCKET L514). | downstream of #1/#2 | PDNA re-rising + reserve-coverage deterioration |
| 4 | Modification exhaustion | 2 | No aggregate series. Asset level: Aon and Seattle recaps failed; Sangertown 3rd extension refused on a DSCR hurdle. Mods exhausting one credit at a time. | independent | re-default / 2nd-mod rates rise |
| 5 | MF term-default broadening | *(3)* | **HOMER-fed cross-reference; not a CREED vote.** Cite `AGENTS/HOMER/STATUS.md`. Excluded from the independent-root count. | not a CREED vote | *(HOMER's call)* |
| 6 | Forced-sale / NAV recognition | 3 | Realized-comp cluster holds (incl. 3000 Post Oak 9/28). **`CREED-T-06b` FIRED 8/27 (SREIT gate); S6 HELD AT 3, Will-ruled**: a gate is a refusal to sell, so it blocks recognition. Counter: ARI's book cleared at 99.7%. | independent | a gated fund actually **selling**, or a large **performing** book clearing materially below par (not another gate) |
| 7 | Office-demand structural hit | 2 | Q2 national office leasing improved (CBRE 18.3%, −30bp, +12.6M sf absorption, 9th positive quarter; JLL −60bp). The tenant-demand leg is moving away. ⚠️ `VX-9.03` Moody's → CBRE was a basis change, not an improvement. | shares office-demand root with #8a | REIT selloff **AND** direct tenant-demand impairment |
| 8a | CRE equity tape | **4 🔴** | `CREED-T-08a` FIRED 9/24 (TR −10.12; −13.06 9/25). **Rate-led** (10y 4.38 → 5.18%; FOMC +25bp 9/16); ~2.2pp of the 9/25 depth was window roll. **9/30 close −9.14pp TR (9/29 −7.89), inside the band, inside noise; the fire stands.** Scored 4 by Will 9/28 (WQ-303); hold confirmed 9/30. Confirms the maturity/coupon root, adds no new root. | equity-tape read of #7 / coupon root | VNQ −10pp vs SPY/3mo + confirming fundamentals |
| 8b | CRE credit / lender tape | 3 | 4 of 11 cut or liquidating, 7 held (census 9/26); Q2 book erosion concentrated in four names; ARI dissolution approved 9/29. `T-08b` NOT FIRED 9/26 (cuts, but erosion not cohort-wide). | **independent** (lender-capital channel) | multi-name cuts **AND** realized book erosion across the cohort |

**Composite: 27/45 (60.0%)**: S8a 2 → 4, Will-ruled 2026-09-28 (WQ-303); hold confirmed 2026-09-30. ⚠️ **Caveat travels with the score:** a rate-led fire, with ~2.2pp of the 9/25 depth from the window roll. It argues against 5 and does not lower the 4. Prior: 25/45 from 8/20 (S2 3 → 5); 23/45 from 7/27.

**How S5 is counted (two different exclusions):** the **composite INCLUDES** S5's 3 (CREED still tracks MF as a CRE-stress vector); the **independent-root count EXCLUDES** it. A single S5-free number on today's basis is **24/40 (8-vector basis), not comparable to the 7/20 20/40**. Do not drop S5 from the composite to "simplify".

**Counting once for shared antecedents:** maturity/coupon root (S1+S2, now also what S8a's fire confirms); office-demand root (S7+S8a); S3 downstream of S1/S2; S5 not a CREED vote; **S8b a genuinely independent root**. ⇒ **~4–5 independent roots elevated, not 8.** Read 27/45 as *recognition accelerating in its own channels*; **broad CRE-to-bank transmission is not confirmed** (S3 still 2).

---

## Counter-Signals

Would weaken the bear read:
- CMBS delinquency below **6.5%** with SS falling on genuine cures/payoffs, not denominator effects.
- Office delinquency below **9%** and office SS below **13%**.
- 2026 maturity repayments materially beating the >50% non-repayment expectation.
- FDIC bank CRE PDNA improving while reserve coverage stabilizes.
- Transaction volume and price discovery improving without forced-sale discounts.
- Funding/rates easing enough to refinance low-debt-yield cohorts.

**Live counter-signals as of 2026-09-30:**
- **ARI's CRE loan book cleared at 99.7% of commitments** (Athene, closed 4/24/26): the strongest evidence that marks in the **performing** lender channel are not fictional. ⚠️ Do not generalize it into "the sink absorbs at par"; distressed single-asset comps and performing-book prices measure different populations.
- **Office leasing improved in Q2 2026** (CBRE −30bp with +12.6M sf absorption; JLL −60bp; C&W's −10bp is largely inventory removal). This sharpens the thesis rather than weakening it: buildings leasing better while still failing to refinance locates the distress in values and debt.
- **The lender leg is selective:** 7 of 11 held Q3 dividends; Q2 book erosion concentrated in four names (9/26 census).
- **FDIC Q2 bank CRE metrics improved** (PDNA down, reserve coverage up), with the recognition-composition and C&I scope caveats above.
- ⛔ **No longer live:** the 7–8/2026 CRE **equity-tape** counter-signal. `CREED-T-08a` fired 9/24; its history is in the snapshot.

---

## Agent Handoffs

| Desk | CREED sends | CREED does not send / own |
|---|---|---|
| **REGINALD** | bank-size CRE PDNA and reserve-coverage deterioration · property/metro maps tied to bank exposures · mod-exhaustion / re-default evidence · LGD comps | bank trade recommendations or sizing |
| **CORAL** | Florida-specific CMBS / hotel / MF / condo-linked stress (national Trepp monthlies have no geographic table, so FL items come from named-loan prose, `KB-CREED-025`) | whole-Florida synthesis |
| **LIQUID** | maturity-wall funding/refi pressure · forced-sale / NAV evidence · lender appetite and credit-closure signs (S8b) | the funding/plumbing thesis |
| **CARL** | non-MF property-level stress with household spillover | MF (routes via HOMER) |
| **HOMER** | the MF row from CREED's own Trepp pulls, opportunistically (courier killed 8/13; no cadence) · MF-relevant lender evidence | an independent MF score or a second Trepp-MF citation |
| **SHADE** | CRE-asset migration onto insurance balance sheets (ARI → Athene) · the CRE leg of the MBA life-insurer series: **Q2 +$7.8B → $781.6B, whole loans only** (`KB-CREED-047`) | the combined-sink question and insurer credit judgment |

---

## Current Open Questions

1. Is Q4 2026 the real maturity-wall pain point? (39% of 2026 hard maturities fall in Q4.)
2. Which regional/community banks have deteriorating reserve coverage plus high CRE concentration? Does the Q2 regional OREO jump carry into Q3 (FDIC Q3 QBP ~late Nov)?
3. Does AI office-demand risk show up in leasing/vacancy/default data, or stay equity narrative?
4. **How much CRE credit is migrating from fast-recognition holders (mREITs, CMBS) to slow-recognition holders (insurers, banks), and does migration *defer* recognition or merely *relocate* it?** If the fast channel keeps shedding at par into balance-sheet buyers, headline CMBS/mREIT metrics understate system CRE risk by construction. *(SHADE owns the insurer side.)*
5. **Is ARI the first of several lender exits?** Partly answered: by 9/26, 4 of 11 had cut or were liquidating and GPMT opened a formal review (9/23). Whether that becomes cohort-wide book erosion is the `T-08b` test.
6. **Reframed 2026-09-30 (no new research):** the July question *"why did the equity and credit tapes diverge?"* is overtaken. The equity leg sold off in September on **rates**, so the two legs now point the same way for different reasons (rates vs lender economics). **Open:** whether the lender leg's cuts become cohort-wide erosion, and whether rates keep leading the equity tape. The July framing is in the snapshot.
7. *(HOMER's question since 7/27: whether MF stress stays metro-specific.)*
8. **Research candidate — potentially useful, presently unconnected, lower priority** *(added 2026-09-30, Will via PROME)*: **is office / multifamily maturity risk concentrated in a few sponsors or loans, the way Trepp found for self-storage** (`KB-CREED-048`: three loans = 97.9% of that sector's estimated shortfall under an 8% debt-yield screen)? If so, stress would arrive as a few large events rather than a gradual rise, which changes how a monthly print should be read. **Bounded:** first check whether a published study already answers it; a new loan-level calculation may need data CREED does not have. ⛔ **Recording this does not authorize the research: starting it is a new direction and returns to Will as a proposal.**

---

## Operating Rule

Do not trade directly from CREED. CREED identifies stress mechanisms and routes evidence. Trade construction belongs to TERRY; bank-level trade construction and bank thesis belong to REGINALD; Will approves all trades.
