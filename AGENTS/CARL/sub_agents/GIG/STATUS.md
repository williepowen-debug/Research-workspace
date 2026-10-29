# GIG STATUS

**Last Updated:** 2026-10-29 00:03 ET (session closed out under CLOSEOUT.md; closeout rebuilt: `CLOSEOUT.md` + runner; STATUS rotated 30,800 → ~23.5 KB, 6 settled blocks to `archive/STATUS_ARCHIVE_2026-10.md`) · 2026-10-28 late (catch-up: Q3 print dates confirmed, Waymo Oct footprint, DoorDash gas-relief correction, stale STATUS sections reconciled to the ledgers) · earlier 10/28 (ledger-clearing pass; platform/Dave operating data still 2026-08-10 Q2 vintage) (Q2 platform earnings refresh: Dave/Uber/DoorDash/Lyft all reported Aug 5-6; gas RE-PULLED via CARL tape) | **Status:** 🟠 ELEVATED

> **Catch-up note (2026-10-28 late):** ① **Q3 prints are dated:** Uber, DoorDash and Dave on **Wed Nov 4** (Uber call 8:00 ET; DoorDash and Dave after close, calls 4:30 ET), Lyft **Thu Nov 5** (call 5:00 ET) [company notices 10/5, 10/9, 10/23, 10/15; Dave via secondary copy, IR page 403] (ML-GIG-28). ② **Waymo:** public service in San Antonio, San Diego, Tampa (10/14); +~250 sq mi in LA, Nashville, **Orlando**, San Diego, SF Bay (10/27); $5B debt (10/8). **No rides/week or fleet figure published** — last primary 500K/wk (Mar 2026); GIG-P07 still ungradeable on its instrument [waymo.com/blog, fetched 10/28] (ML-GIG-29). ③ **Correction:** DoorDash's US gas relief had fixed end dates (weekly payments 3/23-4/26; Crimson cash back to 6/30); GIG's 8/10 "continuing, not tapering" read is withdrawn; Q3 status unknown until 11/4 (ML-GIG-30, VX-GIG-1.04). ④ Dashboard, liquidity-threshold, prediction and cross-agent tables below were still showing Q1 values and pre-ruling statuses; reconciled to the ledgers this pass.

> **Refresh note (2026-10-28, ledger-clearing pass):** Q3 2026 prints for Dave/Uber/Lyft/DoorDash are NOT on SEC EDGAR as of 10/28 (latest earnings 8-Ks 8/5-8/6), so every platform/Dave value below is the Q2 vintage and carries `[STALE - 2026-08-10]` where it is quoted as a level. **Newly refreshed:** national gas, EIA weekly via FRED: $4.269 (w/e 10/26), re-peaked $4.478 (9/21, $0.022 under the $4.50 Orange band, no breach), easing 4 weeks; diesel $6.352 [EIA/FRED, pulled 10/28]. Lyft 8-K 9/30: $272.5M California misclassification settlement (2016-2020 period; historical liability). FL/TX/CA gas, Gridwise earnings, Waymo/Tesla rows `[STALE - 2026-08-10 or earlier]`. **Predictions** *(superseded same day: CARL closed P02/P03/P04/P06 NO-VERDICT-BY-INSTRUMENT; P07 open to EOY — see PREDICTIONS table)*: GIG-P02 DUE-UNRESOLVED (no primary FL-vs-national gig series; context FL unemployment 4.4% vs US 4.2% Sep 2026, BLS via FRED, LABOR-owned); P03/P06 DUE-UNRESOLVED (Gridwise annual only); P04 unreachable; P07 partial (Waymo blog has no rides/fleet). **Ledgers:** DRIVER_ECONOMICS/ML/PLATFORM/PREDICTIONS/VX refreshed (scope in each header); FLOW FROZEN; AV_TRACKER RETIRED; ragged rows realigned (VX 6, ML 3 + 1 blank line, FLOW 1). SV: `state_vectors/SV-GIG-2026-10-28-01.md`.


---

## ⚠️ THRESHOLD SIGNALS — gas 2026-10-26; platform rows Q2 vintage (2026-08-10) until the 11/4-11/5 prints

| Signal | Value | Status | Change vs Jun-22 |
|--------|-------|--------|-----------------|
| Gas national | **$4.269** (EIA weekly w/e 10/26, FRED, pulled 10/28; peak $4.478 9/21) `[prior: $4.0091 AAA 8/10]` | 🟠 RE-ARMED | ↑ RE-BREACHED $4.00, held since 7/20 — reverses the Jun-22 "receding" read ($3.929); FRED weekly $4.079 w/e 8/3 |
| Gas FL | `[STALE - 2026-08-10]` $3.862 (AAA 8/10) / TX $3.545 / CA $5.596 | 🟡 BELOW national | Inversion HOLDS (FL still below national), only the level re-armed |
| Dave 28DPD | **2.12%** (Q2 2026) | 🟡 seq-rising, YoY-improved | ↑ from Q1's 1.69% record low, back near legacy Yellow line (>2.10%); still platform-health only, NOT re-armed as canary |
| Dave loss provision | **+14.3% YoY** ($28.8M Q2'26 vs $25.2M Q2'25) | 🟢 DECELERATED | Q1's +151% spike did NOT persist — RE-CUT TEST RESOLVED as timing-artifact (mgmt's own explanation confirmed). GIG PROPOSES CRITICAL→NORMAL |
| Platform driver supply | Uber record 10.2M (but localized India/Brazil tightness); Lyft "near all-time highs"; DoorDash gas relief >$50M Q2, program end dates 4/26 and 6/30 (Q3 status unknown) | 🟡 MIXED | Not a clean oversupply confirm — first tightness signal (Uber, geography-specific) since thesis inception |
| Waymo footprint | Public service incl. Tampa (10/14) and Orlando (expanded 10/27); 14 US cities per Electrek 9/1; **no rides/fleet figure since 500K/wk Mar 2026** | 🟠 footprint widening, volume UNMEASURED | Refreshed 10/28 from waymo.com/blog (footprint only) |
| Tesla driverless Austin | `[STALE — Apr-17]` 245 sq mi, no safety driver | 🟠 (UNVERIFIED) | Not refreshed this pass |

---

## THESIS

**"The Invisible 24 Million" — Gig workers are the canary, not the buffer.**

Traditional narrative: Gig economy absorbs employment shocks (safety valve).
Reality: Gig workers are **already at maximum stress** and will amplify, not absorb, any downturn.

- **65%** take cash advances to bridge standard payout delays
- **61%** delay essential bills due to payout lags
- **58%** seek emergency loans at least quarterly
- **52.9%** of auto loans are underwater (negative equity)
- **7M gig workers undercounted** in official employment stats [Boston Fed]

When traditional employment breaks (LABOR), displaced workers flood INTO gig → oversupply → earnings compression → gig workers AND new entrants both stressed → cascade.

**GIG sits BETWEEN LABOR and CARL in the transmission chain:**
```
Traditional employment shock (LABOR)
    ↓
Workers flood INTO gig (oversupply) [Goldman: 20% of layoffs → gig]
    ↓
Earnings compression (GIG) [earning 50-65% of prior wages]
    ↓
Gas squeezes net income further (HAWK → GIG)
    ↓
Cash advance dependency spikes (GIG → shadow credit)
    ↓
Auto/credit delinquency (CARL)
    ↓
Bank losses (REGINALD)
```

**Squeeze vectors:** current reads live in the THRESHOLD SIGNALS table and the GAS / PLATFORM sections below; the Jun-22 vector narrative is archived (`archive/STATUS_ARCHIVE_2026-10.md` §2).

---

## SIGNAL DASHBOARD

| Indicator | Value | Threshold | Status | Source |
|-----------|-------|-----------|--------|--------|
| **Dave 28DPD** | **2.12%** (Q2 2026; Q1 1.69%) | >2.10% | 🟡 seq-rising, YoY-improved (canary RETIRED, platform-health only) | Dave Q2 2026 8-K, Aug 5 |
| **Dave loss provision** | **+14.3% YoY** ($28.8M Q2'26; Q1 was +151%) | >+50% / >+100% / >+200% YoY | 🟢 NORMAL (ratified by CARL 8/10) — Q3 test 11/4 | Dave Q2 2026 8-K, Aug 5 |
| **Dave ExtraCash portfolio** | **$279.1M** (Mar) | contraction | 🟡 −6% QoQ (from $297.3M Dec) | Dave Q1 2026 |
| **Gas National Avg** | `[SUPERSEDED - $4.269 EIA 10/26]` **$3.929** (was $4.076 Apr-17 — superseded) | >$4.00 breakpoint | 🟠 RECEDING (peaked $4.50 May-11) | AAA Jun 22 2026 |
| **Gas FL** | `[STALE - 2026-06-22; see 8-10 and top table]` **$3.617** — now BELOW national (was $4.093 ABOVE) | >$4.00 | 🟡 LEG INVERTED | AAA Jun 22 2026 |
| **Lyft driver-incentive spend** | **−$12.8M YoY** (Q1) | cut | 🔴 supply surplus signal | Lyft Q1 2026, May 7 |
| **DoorDash gas subsidy** | **~$100M H1 (>$50M Q2)**; weekly payments ended 4/26, cash back to 6/30; Q3 status unknown | new program | 🟠 admission gas compresses net; program had end dates | DoorDash Q1/Q2 2026; Dasher help center |
| **Fare vs driver pay (YTD)** | **+9.6% fares / +3.6% pay = 2.7× extraction** | fares > pay | 🔴 WIDENING | Gridwise May 13 2026 |
| **Emergency Loan Dependency** | **58%** | >55% | 🔴 CRITICAL | RadCred 2026 |
| **Cash Advance for Payout Bridge** | **65%** | >50% | 🔴 CRITICAL | Everee 2025 |
| **Bills Delayed (Payout Lag)** | **61%** | >40% | 🔴 CRITICAL | Everee 2025 |
| **Platform Take Rate Change** | **+33% YoY** | >20% | 🔴🔴 BREACHED | Industry 2025 |
| **DoorDash Median Hourly** | **$11.63** (Mar-31; not re-priced Jun-22) | <$11 | 🟠 DECLINING | Gridwise 2026 |
| **Lyft Weekly Earnings** | **$318** (2025; not re-priced Jun-22) | <$300 | 🟡 DECLINING | Gridwise 2025 |
| **Gig vs Prior Pay** | **50-65%** | <50% | 🟠 STRESSED | Goldman/Yahoo/Berkeley |
| **FL Gig Concentration** | **22%** | N/A | 🔴 HIGHEST | State data |
| **Waymo Rides/Week** | **500K** (Mar 2026, last primary figure; none published since) | 750K threshold | 🟠 UNMEASURED since March | Waymo/TechCrunch Mar 2026; waymo.com/blog checked 10/28 |
| **Tesla Driverless Austin** | `[STALE — Apr-17]` no safety driver, 245 sq mi | N/A | 🟡 UNVERIFIED Jun-22 | Electrek Mar 31 2026 |
| **Fiverr Active Buyers** | **3.3M** (-13.2% YoY) | N/A | 🔴 DEMAND SHRINKING | Fiverr Q4 2025 |

### Primary Liquidity Signal: Dave loss provisioning (28DPD canary RETIRED)

28DPD is survivorship-biased (CashAI underwrites out the worst credits), so it is a platform-health indicator only. The primary liquidity signal is the loss-provision YoY trajectory (VX-GIG-3.08). Q1 2026 history (+151% YoY spike, mgmt's quarter-end-timing claim) archived in `archive/STATUS_ARCHIVE_2026-10.md` §3; the current read is the Q2 result below.

### ⚠️ Q2 2026 RESULT — pre-registered re-cut test RESOLVED (2026-08-10)

Dave reported Q2 2026 Aug 5, 2026 (quarter ended Jun 30, 2026). [PRNewswire/8-K Aug 5; SEC EDGAR 000119312526335119]

| Metric | Q1 2026 | Q2 2026 | Read |
|--------|---------|---------|------|
| 28DPD | 1.69% | **2.12%** | Sequential rise back toward legacy Yellow (>2.10%); still YoY-improved (Q2'25 ~2.25-2.26%, ~6% rel. / ~14bp) |
| Provision for credit losses | $26.6M (+151% YoY) | **$28.8M (+14.3% YoY)** | **DECELERATED sharply** — below even the Yellow band (>+50% YoY) |
| ExtraCash originations | — | **$2.3B (+27% YoY)** | Volume growing faster than provisions — loss-per-dollar-lent improving |
| Mgmt guidance | "Mar-31 timing" claim | "loss rates similar range to Q2" post CashAI v6.0 | Consistent with a stabilized, non-accelerating loss trajectory |

**VERDICT: REVERT, not persist.** The Q1 +151% YoY spike did not carry into Q2 (+14.3% YoY) — nowhere close to the 2-consecutive-quarters->+100% Red trigger. This confirms management's timing-artifact explanation over a real-stress read. **Status downgrade CRITICAL→NORMAL RATIFIED by CARL (8/10).** The band re-cut below was NOT adopted: VX-GIG-3.08 still carries >+50/>+100/>+200% YoY, while the 10/28 SV cited >+70% as the re-escalation line — one of the two needs a CARL ruling before 11/4. Original proposal: downgrade VX-GIG-3.08 Status CRITICAL→NORMAL, and re-cut the provisional bands using Q2's +14.3% as the new baseline-quarter anchor (candidate: Yellow >+40% YoY / Orange >+70% YoY / Red >+120% YoY or 2 consec qtrs >+70%) rather than carrying Q1's anomalous +151% forward as the working baseline. [Dave Q2 2026, PRNewswire/8-K Aug 5]

---

## PLATFORM EARNINGS — Q2 2026 RELEASED (integrated 2026-08-10)

| Platform | Earnings Date | Key Q2 Result (integrated) | Status |
|----------|--------------|----------------------------|--------|
| Uber (UBER) | Aug 5 ✅ | Record **10.2M drivers+couriers**; GB $58B+ (+22%), 3.87B trips (+18%), rev $14.19B (+12%); **localized supply TIGHTNESS** — India two-wheeler competition + Brazil supply shift to delivery dragged trip growth; mgmt reallocating $ to driver-side, "early signs of supply improving in Q3" | PROCESSED |
| DoorDash (DASH) | Aug 5 ✅ | Orders 970M (+27%), rev $4.45-4.5B (+36%); gas-relief program **>$50M Q2** (continuing pace, consistent w/ Q1's $100M H1 total); no dasher count disclosed (consistent w/ history); H2 EBITDA margin guided down on "seasonal increases in Dasher costs" | PROCESSED |
| Dave (DAVE) | Aug 5 ✅ | 28DPD **2.12%** (seq ↑ from 1.69%, YoY improved); provision **+14.3% YoY** ($28.8M, DECELERATED from Q1's +151%); ExtraCash originations **$2.3B (+27% YoY)** | PROCESSED — pre-registered re-cut test RESOLVED (see Primary Liquidity Signal section) |
| Lyft (LYFT) | Aug 6 ✅ | Record 30M active riders, GB $5.5B; driver supply **"historically strong / near all-time highs"**; driver earnings/ride +8% YoY, tipping +10%; driver-rewards program $14M cumulative since launch, mgmt frames spend as "disciplined... not aggressive" | PROCESSED |

**Next window:** Q3 prints **Uber/DoorDash/Dave Nov 4, Lyft Nov 5** (company notices; ML-GIG-28) — watch whether Uber's India/Brazil supply tightness resolves per mgmt's "Q3 improving" claim, and whether gas re-breach (now sustained since 7/20) shows up in Q3 driver-supply commentary.

---

## GAS SQUEEZE ON DRIVERS (refreshed 2026-08-10)

**SIGNAL — AAA 8/10/2026 (via CARL tape) / FRED weekly w/e 8/3:**
- National: **$4.0091** (AAA 8/10) — RE-BREACHED $4.00 and HELD since 7/20 (sustained cross, not a one-day print); FRED weekly $4.079 (w/e 8/3)
- FL: **$3.862** / TX: **$3.545** / CA: **$5.596**
- Prior vintage (Jun-22): national $3.929, had receded from the ~$4.50 May-11 EIA-weekly peak — that recede has now REVERSED

**INTERPRETATION:**
- **RE-ARM TRIGGERED.** This vector's own standing rule ("gas re-breach $4.00 would re-arm the vector") has fired — 🟠 ELEVATED is re-armed/confirmed (not yet 🔴 CRITICAL, which needs $4.50). This reverses the Jun-22 "receding" narrative.
- Corroborates CARL-parent V5 Gas Squeeze vector upgrade 3→4 (CARL STATUS, 8/3) — independent confirmation from the parent-level vector.
- **FL-divergence leg INVERSION HOLDS at the new level** — FL ($3.862) remains BELOW national ($4.0091), same sign as Jun-22 (was $3.617 vs $3.929). The GIG-P02 re-basing onto gig-concentration + UI-cliff (not gas) stands.
- **Platform Q2 admissions confirm gas drag, but the subsidy had end dates** *(corrected 10/28, ML-GIG-30)*: DoorDash spent >$50M in Q2, the scheduled second half of a program whose weekly payments ended 4/26 and cash back 6/30. No Q3 program found, so the 9/21 re-peak likely hit Dashers unaided; the 11/4 call resolves.
- Next watch: does the re-breach show up in Q3 driver-supply commentary (Uber's India/Brazil tightness, DoorDash Dasher-cost guidance) — Q3 prints Nov 4 (Uber/DoorDash/Dave) and Nov 5 (Lyft). [AAA 8/10/2026 + FRED weekly w/e 8/3, per CARL DISRUPTION_SUPPLY_SPREAD.tsv tape]

---

## AV DISPLACEMENT — `[STALE — Apr-17 vintage; Jun-22 SV did NOT refresh AV — UNVERIFIED, neither refreshed nor refuted]`

> **Oct-2026 update (waymo.com/blog, fetched 10/28):** public service opened San Antonio/San Diego/Tampa 10/14; +~250 sq mi across LA, Nashville, Orlando, San Diego, SF Bay 10/27; Las Vegas airport 10/21; $5B term loan 10/8; Toronto (2028) and Madrid in prep. **Two Florida metros (Tampa, Orlando) are now live.** No rides/week, fleet or driver-equivalent figure — the detail below stays STALE.

> Apr-17-vintage detail (Waymo city table with Gridwise AV-city pay impacts, Nashville-Lyft template, 500K→1M trajectory, Tesla Austin) archived in `archive/STATUS_ARCHIVE_2026-10.md` §4. City pay impacts also live in `workbook/DRIVER_ECONOMICS.tsv` (av_driver_pay_impact rows, 2025 vintage).

---

## GEOGRAPHIC CONCENTRATION

FL 22% / CA 20% / TX 18% / IL 18% gig concentration (VX-GIG-5.01; state data). FL gas leg INVERTED since Jun-22 (FL below national; last AAA 8/10 $3.862 vs $4.0091). FL now also carries an AV leg (Waymo Tampa + Orlando, Oct 2026). Jun-22 detail (FL UI Wave-1 cliff, ~42.5K recipients, HB 191) archived in `archive/STATUS_ARCHIVE_2026-10.md` §5.

---

## SUBPRIME AUTO ABS LINK

Apr-17 assessment (subprime ABS 60+ DQ Santander 7.9% / Bridgecrest 7.8% / Exeter 6.7%, Dec 2025, vs ALLY 1.97% NCO headline = composition masking) archived in `archive/STATUS_ARCHIVE_2026-10.md` §6. Live ABS reads are CARL-parent (`abs_monitor.py`), not GIG.

---

## STRESS THRESHOLDS

### Gas Breakpoints (reconciled Jun-22)
| Gas Price | Impact on Driver Net | Status |
|-----------|---------------------|--------|
| $3.50 | Baseline — manageable | national approaching from above |
| **$4.00** | **~15% pay cut vs $3.00. Drivers start quitting.** | 🟠 ABOVE every EIA week since w/e 7/20 ($4.269 w/e 10/26) |
| $4.50 | ~20-25% pay cut. Delivery unprofitable in suburbs. | 🟡 touched May-11 ($4.500); missed by $0.022 on 9/21 ($4.478); CRL-08 disposition is CARL-parent |
| $5.00 | Mass driver exodus. Only high-density urban viable. | CA/diesel elevated |

### Liquidity Thresholds (canary RETIRED — provisioning is primary)
| Metric | Current | Yellow | Orange | Red |
|--------|---------|--------|--------|-----|
| Dave loss provision (YoY) — **PRIMARY** | +14.3% (Q2; Q1 +151%) | >+50% | >+100% | >+200% or 2 consec qtrs >+100% |
| Dave 28DPD (platform-health only) | 2.12% (Q2) | >2.10% | >2.30% | >2.50% |

---

## TRANSMISSION PATHWAYS

### FLOW-GIG-01: Saturation Doom Loop — 🔴 ACTIVE
```
Employment stress → Workers flood TO gig [Goldman: 20% of layoffs] → Oversupply →
Earnings decline [50-65% of prior pay] → Hours increase → Financial stress →
Gas squeezes remaining margin → Auto loan DQ →
Economic contraction → More employment stress
```
**Confidence:** 85% | **Lag:** 3-6 months from Q1 2026 employment shock

### FLOW-GIG-04: Gig-to-CARL Transmission — 🔴 ACTIVATING
```
Gig worker stress → Spending contraction → Credit utilization ↑ →
Auto loan stress → Broader consumer credit deterioration →
CARL vectors trigger
```
**Confidence:** 80% | **Lag:** 3-6 months → Q2-Q3 2026

### FLOW-GIG-05: AV Displacement Amplifier — 🟠 EARLY → ACCELERATING `[STALE — Apr-17]`
```
Waymo/Tesla expansion (11 cities, Nashville Apr 7) → Human drivers lose rides →
Oversupply worsens → Asset trap (loans on gig vehicles) →
Auto DQ spike in AV cities
```
**Confidence:** 65% | **Lag:** 12-24 months | *AV not refreshed by Jun-22 SV.*

### FLOW-GIG-06: Gas Squeeze Transmission — 🟠 RE-ARMED (was RECEDING 🟠→ now confirmed active again)
```
Gas peaked ~$4.50 May-11 → receded to $3.929 (Jun-22) → RE-BREACHED $4.00, held since 7/20 → $4.0091 (AAA 8/10) →
Driver net income compressed again → DoorDash's >$50M Q2 relief confirms the cost (program ended 4/26-6/30; re-peak $4.478 9/21) →
FL leg still INVERTED (FL below national) at the new level
```
**Confidence:** 85% | **Impact:** Immediate | RE-ARM RULE FIRED 2026-08-10 (national re-crossed $4.00, sustained). Next re-arm level: $4.50 (Critical band).

---

## PREDICTIONS (mirror reconciled 2026-10-28 — canonical: workbook/PREDICTIONS.tsv; CARL rulings 10/28)

| # | Prediction | Timeframe | Confidence | Status | Notes |
|---|------------|-----------|------------|--------|-------|
| GIG-P01 | Dave 28DPD >2.10% | Q1-Q2 2026 | 65% | **MISS** (7/10) | Q1 1.69% record low + premise invalidated (survivorship). Successor = VX-GIG-3.08 provisioning (Q2 result: REVERT, see above). |
| GIG-P02 | FL gig stress leads national | Q2-Q3 2026 | 50% | **NO-VERDICT-BY-INSTRUMENT** (10/28) | Closed unscored by CARL ruling: no primary FL-vs-national gig series exists. |
| GIG-P03 | Lyft weekly earnings <$300 | Q1-Q2 2026 | 70% | **NO-VERDICT-BY-INSTRUMENT** (10/28) | Closed unscored: Gridwise publishes annual only; Lyft discloses earnings/ride, not weekly $. |
| GIG-P04 | Multi-apping rate >65% | H2 2026 | 65% | **NO-VERDICT-BY-INSTRUMENT** (10/28) | Closed unscored: no H2 2026 survey print expected. |
| GIG-P05 | ~~1099-K exodus >15%~~ | ~~2026~~ | — | CANCELLED | OBBBA reverted to $20K. |
| GIG-P06 | DoorDash median <$11/hr | Q2 2026 | 65% | **NO-VERDICT-BY-INSTRUMENT** (10/28) | Closed unscored: same Gridwise cadence gap as P03. |
| GIG-P07 | Waymo displaces >10K equiv drivers by EOY 2026 | EOY 2026 | 60% | TRACKING | CARL rule 10/28: grade only on a Waymo- or regulator-published rides/fleet/driver-equivalent figure; none at EOY → NO-VERDICT-BY-INSTRUMENT. Checked 10/28: footprint news only, no figure (ML-GIG-29). |
| GIG-P08 | Gas $4+ triggers visible driver count decline QoQ | Q1-Q2 2026 | 70% | **MISS** (7/10) | Mechanism inverted — more hours-on-platform, not exodus. Gas has since RE-BREACHED $4.00 (7/20-8/10) — worth a fresh QoQ read at Q3 platform earnings. |

---

## CROSS-AGENT LINKS

| From | Condition | Effect on GIG |
|------|-----------|---------------|
| LABOR | JOLTS ratio 1.04 (May); Feb 0.91 inversion resolved; LFPR 61.5% | Gig oversupply mechanism intact via supply-surge/AV/extraction legs, not JOLTS inversion — not refreshed this pass |
| LABOR | UI exhaustion Q2-Q3 2026 | FL Wave-1 cliff Jun 24 — not refreshed this pass |
| HAWK/CARL | Gas $4.0091 (AAA 8/10, RE-BREACHED $4.00, held since 7/20) | Driver net income compression RE-ARMED; corroborates CARL V5 Gas Squeeze 3→4 (8/3) |

| From GIG | Condition | Effect |
|----------|-----------|--------|
| Dave provision +14.3% YoY Q2 (down from +151% Q1) | → CARL | VX-GIG-3.08 CRITICAL→NORMAL RATIFIED 8/10; band re-cut (+70% line) still unruled |
| Gas re-breach $4.00, sustained since 7/20 | → CARL, HAWK/BRENT | Corroborating leg for CARL's own V5 upgrade (already fired 8/3) |
| Uber India/Brazil localized driver-supply tightness (Q2) | → CARL | Caveat on the oversupply thesis — first geography-specific tightness signal since inception; not yet a broad reversal |
| GIG-P03/P06 structurally unresolvable via Gridwise | → CARL | RULED 10/28: closed NO-VERDICT-BY-INSTRUMENT |
| **OWED by CARL** — packet `AGENTS/CARL/inbox/2026-10-29_from-GIG_closeout-adopted-and-four-asks.md` (delivered 10/29, not yet acted on) | → CARL | ① VX-GIG-3.08 band **before Dave 11/4** ② docket re-date to 11/4-11/5 ③ KB-CARL-380 carries the withdrawn DoorDash read ④ row-1 banner format. Re-ask if unanswered by 11/3. |

---

## RESEARCH GAPS

- [x] Dave Q2 2026 provision persist-vs-revert — RESOLVED 8/10: REVERT (+14.3% YoY, decelerated from +151%)
- [ ] Gridwise weekly-$/hourly-$ — 3/3 checks (5/10, 7/10, 8/10) found no mid-year print; Gridwise appears annual-only. Re-instrument GIG-P03/P06 off a different source, or accept unresolvable.
- [ ] FL DEO Wave-1 actual headcount (not public real-time) — watch DQ-conversion 30-60d post-cliff (post-Jun 24) — not chased this pass
- [ ] HB 191 signature status (tightens FL UI eligibility further) — not chased this pass
- [ ] AV surface: Waymo footprint refreshed 10/28 (cities only); rides/fleet unpublished since Mar; Tesla still Apr-17 vintage
- [ ] Classification: DOL proposed independent-contractor rule (Feb 2026; final status unconfirmed) and New Jersey ABC-test regulation reportedly effective 10/1/2026 (single secondary source) — verify before citing
- [ ] DoorDash gas relief after 6/30 — ask of the 11/4 call
- [ ] Multi-apping rate update (last est ~50%, pre-gas-squeeze)
- [ ] Brigit/Earnin subscriber trends as alternative cash advance canaries
- [ ] NEW: Uber's India two-wheeler / Brazil driver-supply tightness — does it resolve in Q3 per mgmt's "early signs improving" claim, or does it spread to other markets?
- [ ] NEW: does the gas re-breach ($4.00, sustained since 7/20) show up in Q3 driver-supply/incentive commentary?

---

## KEY DOCS
- **RP-LABOR-12**: Comprehensive gig baseline (2026-02-11)
- **outbox/SV-GIG-2026-06-22-01.md**: Jun-22 refresh
- **state_vectors/SV-GIG-2026-07-10-01.md**: reconciliation completion SV
- **state_vectors/SV-GIG-2026-08-10-01.md**: Q2 earnings refresh SV — Dave re-cut proposal, gas re-arm, driver-supply mixed read
- **state_vectors/SV-GIG-2026-10-28-01.md / -02.md**: ledger-clearing pass; late catch-up (Q3 dates, Waymo FL, DoorDash correction, band ruling ask)
- **RECONCILIATION_DRAFT_2026-07-10.md**: CARL-ratified reconciliation plan (historical)
- **ML.tsv**: Master log (entries through ML-GIG-30); **PLATFORM.tsv** carries Q3 date rows + Waymo footprint; **DRIVER_ECONOMICS.tsv** carries Waymo FL AV-market row
- **VX.tsv**: Vector tracking (VX-GIG-6.01 gas RE-ARMED 🟠, 3.05 Dave 28DPD Q2 2.12%, 3.08 provisioning NORMAL (ratified 8/10; band choice pending), 2.01 driver-supply MIXED, 1.04 incentives ELEVATED — DoorDash framing corrected 10/28)

*Next update trigger: Q3 prints Uber/DoorDash/Dave Nov 4, Lyft Nov 5 (Uber India/Brazil supply resolution + gas re-breach persistence + Dave Q3 provisioning baseline confirmation).*
