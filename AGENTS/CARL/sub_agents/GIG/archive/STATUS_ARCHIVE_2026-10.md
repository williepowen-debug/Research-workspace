# GIG STATUS archive — 2026-10

Rotated verbatim out of `STATUS.md` on 2026-10-28 (read-cap rotation; STATUS 30,800 B → 23,512 B, cap 32,550 B, rotate-tier 75%). Each block is byte-for-byte as it stood in STATUS; byte count and CRC32 are of the block text.

## §1. Refresh note 2026-08-10 (preamble)

`bytes=1074 crc32=e9549212`

<!-- BEGIN VERBATIM -->
> **Refresh note (2026-08-10):** Dave Q2 2026 pre-registered re-cut test on VX-GIG-3.08 RESOLVED — provision growth decelerated +151%→+14.3% YoY, confirming mgmt's timing-artifact claim over persistent stress; GIG PROPOSES downgrade CRITICAL→NORMAL (CARL to ratify). Gas RE-BREACHED $4.00 and has HELD since 7/20 (AAA $4.0091 8/10) — VX-GIG-6.01's own re-arm rule triggers, reversing the Jun-22 "receding" read; corroborates CARL-parent V5 Gas Squeeze 3→4 (8/3). Uber/Lyft/DoorDash Q2 supply signals are MIXED, not a clean oversupply confirm: Uber flagged localized driver tightness (India two-wheel, Brazil) despite a record 10.2M aggregate driver/courier count; Lyft supply "historically strong/near all-time highs"; DoorDash continuing ~$50M/qtr gas subsidy. GIG-P03/P06 (Gridwise weekly-$/hourly-$) hit their THIRD consecutive no-print search — marked ⚠ DUE-UNRESOLVED [DATA-NEEDED], recommend re-instrumenting off Gridwise's annual-only cadence. The **AV surface remains Apr-17/Jul-8 vintage** — not touched this pass (no cheap dated trigger surfaced).

<!-- END VERBATIM -->

## §2. THESIS squeeze vectors (reconciled Jun-22)

`bytes=1196 crc32=8f046c20`

<!-- BEGIN VERBATIM -->
**Squeeze vectors (reconciled Jun-22):**
1. **Oversupply — CONFIRMED, mechanism intact.** SIGNAL: JOLTS ratio 1.04 (May 2026); the Feb-2026 0.91 inversion has resolved (parent V16 re-anchored 4→3, v2.5.2 Jun-6); LFPR 61.5%. INTERPRETATION: the oversupply mechanism no longer rests on a JOLTS *inversion* — it now rests on the direct supply-surge / AV / extraction legs (see vector 2-4), which the Jun-22 platform data confirms. [Parent STATUS Jun-6; BLS May]
2. **Gas squeeze — RECEDING.** SIGNAL: peaked ~$4.50 May-11 (EIA wk), now $3.929 national (AAA Jun 22), still +$1.04/gal YoY. INTERPRETATION: 🔴→🟠; the acute pump squeeze is easing, but structurally elevated. FL no longer the gas outlier (leg inverted). [AAA/EIA Jun 22]
3. **Platform extraction — CONFIRMED.** SIGNAL: Gridwise 2.7× extraction (fares/trip +9.6% YTD vs driver pay/trip +3.6% YTD); take rates +33% (2025). INTERPRETATION: platforms capturing the per-fare growth; drivers absorbing cost increases. [Gridwise May 13]
4. **AV acceleration — `[STALE — Apr-17 vintage]`.** Waymo 11 cities (Nashville Apr 7 + Lyft partnership), Tesla driverless Austin. Jun-22 SV did not refresh AV — carries UNVERIFIED.

<!-- END VERBATIM -->

## §3. Primary Liquidity Signal — Q1 2026 history (28DPD retirement rationale + Q1 table)

`bytes=1669 crc32=41fcc893`

<!-- BEGIN VERBATIM -->

Dave Inc. (DAVE) reports "28 Days Past Due" (28DPD) on cash advances — **but this metric is survivorship-biased and has been RETIRED as the primary canary** (reconciled 2026-07-10 from Jun-22 SV). Dave underwrites OUT the worst subprime credits (CashAI filtering), so a low/improving 28DPD reflects selection, not population health. **28DPD is now a platform-health indicator only, NOT a bottom-60 delinquency barometer.**

**New primary liquidity signal = provision-for-credit-losses trajectory + ExtraCash portfolio contraction.** *(Table below is the Q1 history that set up the test; the current read is the Q2 RESULT section that follows.)*

| Metric | Q1 2026 | Prior | Read |
|--------|---------|-------|------|
| 28DPD | **1.69%** | 1.89% Q4 / 1.70% Q1'25 | Record Q1 low — but optically improved (survivorship). Platform-health only. |
| Provision for credit losses | **$26.6M** | $10.6M Q1'25 | **+151% YoY** — loss expectations rising even as reported DQ falls. THE signal. |
| ExtraCash portfolio | **$279.1M** (Mar) | $297.3M (Dec) | −6% QoQ — portfolio contracting. |
| Net monetization | **5.1%** | — | 4-yr high. |
| ARPU | **+24% YoY** | — | Revenue growth ≠ borrower health. |

**Interpretation:** The +151% provision spike moves OPPOSITE the improving DQ metric — that divergence is the informative signal. Mgmt attributes the spike to Mar-31 quarter-end timing (intra-week advance peak). **Q2 print (~Aug) is the test:** does the provision spike persist (→ real stress) or revert (→ timing artifact)? New vector VX-GIG-3.08 tracks this (bands `[FLAG: uncertain — Will to review]`). [Dave Q1 2026, PRNewswire May 5; SEC 8-K]


<!-- END VERBATIM -->

## §4. AV DISPLACEMENT — Apr-17 detail (Waymo city table, Nashville-Lyft, trajectory, Tesla)

`bytes=1464 crc32=e2b5ea56`

<!-- BEGIN VERBATIM -->
> ⚠️ **This entire section is Apr-17 vintage.** The Jun-22 refresh did not update AV data. Do not cite as current; carries UNVERIFIED to next spawn. **GIG-P07 (Waymo >10K displaced by EOY) rests entirely on this un-refreshed data.**

**Waymo — 11 Cities as of Apr 7, 2026 `[STALE]`:**
| City/Region | Status | Notes |
|-------------|--------|-------|
| Phoenix | Mature | Original market. Magna production plant doubling. |
| San Francisco | Mature | -6.9% driver pay YoY |
| Los Angeles | Active | -4.7% driver pay YoY |
| Austin | Active | -5.3% driver pay YoY. Tesla also here. |
| Nashville | Launched Apr 7 | Lyft partnership — Lyft provides fleet services via Flexdrive subsidiary |
| London | Testing | ~100 vehicles, safety operator aboard, commercial launch 2026H2 |

**Nashville-Lyft partnership significance `[STALE]`:** Waymo chose Lyft over Uber for Nashville; Lyft handles vehicle readiness/charging/depot via Flexdrive. Template for Waymo-as-infrastructure, Lyft-as-operator — Lyft cannibalizes its own human drivers via AV partnerships.

**Waymo trajectory `[STALE]`:** ~500K rides/week, targeting >1M by EOY 2026. At 1M/week ≈ ~8K FT-driver-equivalent displacement (from ~4K). Still <0.1% of 9.7M Uber drivers — trajectory is what matters.

**Tesla driverless `[STALE — Mar 31]`:** Unsupervised (no safety driver) in Austin, geofence 245 sq mi. Expanding to Las Vegas, Dallas by EOY 2026. Only 4-8 vehicles unsupervised currently.

<!-- END VERBATIM -->

## §5. GEOGRAPHIC CONCENTRATION (reconciled Jun-22)

`bytes=1450 crc32=36a03087`

<!-- BEGIN VERBATIM -->
## GEOGRAPHIC CONCENTRATION (reconciled Jun-22)

| State | Gig Concentration | Gas Price (Jun-22) | Status | Notes |
|-------|-------------------|-----------|--------|-------|
| **Florida** | **22%** | **$3.617** (BELOW national) | 🔴 CONVERGENCE (re-based) | Gas leg INVERTED — FL now below national. Convergence re-rests on gig-concentration + UI-cliff, NOT gas. UI Wave-1 cliff NOW (Jun 24). |
| California | 20% | (not re-priced Jun-22) | 🔴 CRITICAL | Waymo active (SF, LA). |
| Texas | 18% | (not re-priced Jun-22) | 🟡 SHELTER | Tesla robotaxi Austin. |
| Illinois | 18% | (not re-priced Jun-22) | 🟠 | |

**FL convergence (re-based Jun-22):** SIGNAL — FL UI **Wave-1 cliff is NOW (Jun 24)**: FL 12-week hard cap (max $275/wk) → Mar 10-24 filers exhaust ~Jun 10-24; no federal EB/EUC bridge = zero replacement income. FL UR 4.8% Apr (highest since 2021, +1.1pp YoY, 532K jobless). **MAGNITUDE CAVEAT:** only ~8% of unemployed Floridians receive UI (lowest recipiency nationally) → **~42,500 active recipients statewide** — a real income cliff but small in absolute terms. INTERPRETATION — the load-bearing transmission is the **gig-supply-surge channel** (Wave-1 exhaustees drive-to-earn → compress per-trip earnings), NOT aggregate UI dollars, and NOT gas (leg inverted). Legislative risk: HB 191 (passed House 81-31 Feb) tightens eligibility further if signed. [BLS Apr 2026; Florida Policy Institute; FloridaJobs.org]

<!-- END VERBATIM -->

## §6. SUBPRIME AUTO ABS: ALLY K-SHAPE LINK (Apr-17 vintage)

`bytes=1947 crc32=bf569afa`

<!-- BEGIN VERBATIM -->
## SUBPRIME AUTO ABS: ALLY K-SHAPE LINK ASSESSMENT *(Apr-17 vintage — not refreshed by Jun-22 SV)*

**Context:** ALLY Q1 showed headline clean (retail auto NCO 1.97%, 5 consec quarters improving) but CARL audit flagged composition masking: S-tier share 40→37%, nonprime share 9.7→10.1%, ACL -6%. CARL asks: is subprime ABS showing stress that ALLY near-prime print masks?

**Finding: YES — subprime ABS diverges from ALLY headline**

| Source | Dec 2025 DQ (60+) | Status |
|--------|-------------------|--------|
| Santander Consumer (subprime ABS/SDART) | **7.9%** | 🔴 ELEVATED |
| Bridgecrest (subprime auto) | **7.8%** | 🔴 ELEVATED |
| Exeter Finance (subprime) | **6.7%** | 🔴 ELEVATED |
| All-auto 60+ DQ | 1.61% (Dec 2025) | 🟡 |
| ALLY retail auto NCO | 1.97% (Q1 2026) | 🟢 (HEADLINE) |

**Gap analysis:** Santander subprime at 7.9% 60+ DQ vs ALLY headline 1.97% NCO reflects composition bias, not credit health improvement. ALLY has actively shifted toward S-tier (prime) borrowers, shrinking nonprime exposure — so the "improvement" is selection, not population improvement. Subprime borrowers (where gig workers concentrate) are at 7.9% 60+ vs <2% prime. The population that gig workers live in is in acute stress.

**Platform financing arms:** No direct signal on Uber Fleet/Hertz Flexdrive program showing ABS stress. However: Hertz is ALLY's largest rental fleet customer (Hertz gig program = Uber Express Drive partnership). Weekly rental $150-280 is a FIXED COST for gig drivers, not escapable like a monthly car note. Gas squeeze hits rental drivers harder because they can't defer the payment.

**Gig worker auto concentration estimate:** 52.9% of gig worker auto loans underwater (RP-LABOR-12). With Santander/Bridgecrest/Exeter showing 7.9%/7.8%/6.7% 60+ DQ, and gig workers disproportionately subprime, the visible gig worker auto stress exists in ABS trusts — just not in ALLY's near-prime headline.

<!-- END VERBATIM -->

