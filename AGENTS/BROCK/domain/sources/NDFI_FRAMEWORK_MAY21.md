# BROCK NDFI Framework — May 21 2026

**Source for this integration:** WALTER REQ-BROCK-20260514-ndfi-scope-correction (7 days open at integration).
**Independent validation:** FDIC 2026 Risk Review (primary), FFIEC RC-C call reports, WFC Q1 10-Q.
**Why this exists:** BROCK's working "$128B top-4-banks PC" figure is the PE/PC sub-slice of full NDFI; the regulatory primary scope is **$1.4T industry YE 2025**, 11× larger. The bank-PC-cascade transmission channel BROCK's Stage 2 thesis depends on is structurally bigger than the working framing.

---

## 1. Scope correction — headline figures

| Figure | Old (BROCK working) | New (FFIEC primary) | Multiple | Notes |
|---|---|---|---|---|
| Aggregate industry NDFI | $128B (top 4 US banks, PC subset only) | **$1.4T YE 2025** | **~11×** | FDIC 2026 Risk Review; FFIEC RC-C aggregate of 10.a-10.e |
| NDFI as % of industry assets | n/a | **5.6%** | — | FDIC 2026 Risk Review |
| YoY growth | n/a | **+22.7% CAGR** | — | Multi-year compound; WALTER REQ cited +35.2% (likely YE2024→YE2025 single-year; CAGR is the more conservative cite) |
| Concentration | n/a | **86% at banks >$100B assets** | — | Top-tier-bank channel is the BROCK-relevant cohort |
| Large-bank NDFI share of loans | 1.2% in 2010 | **15.6% (banks >$250B)** | **~13×** | Structural growth in bank-NDFI exposure over the cycle |
| WFC single-name NDFI | n/a (BROCK had warehouse subset) | **$212.1B YE 2025** | — | WFC Q1 10-Q + call report; **larger than BROCK's full top-4 working figure on a single-bank basis** |

**Mechanism of the prior scope drift:** "Private credit exposure" (BROCK framing) is one sub-category of NDFI on the FFIEC RC-C call report — specifically 10.d (loans to PE/PC funds). The full NDFI category is the 5-cat aggregate 10.a-10.e. BROCK was tracking 10.d at the top-4-bank slice; full NDFI is the industry-wide 5-cat aggregate.

---

## 2. FFIEC RC-C 5-category schema (NDFI bulk schedule)

| Sub | Category | Notes |
|---|---|---|
| **10.a** | Loans to securities firms | Broker-dealers, prime-brokerage exposure |
| **10.b** | Loans to insurers | SHADE-overlap (PE-insurer nexus); Athene-style captive reinsurance arrangements appear here |
| **10.c** | Loans to other financial vehicles | SPVs, securitization vehicles; one of the highest-risk slices per WALTER deep-dive |
| **10.d** | Loans to PE/PC funds | **BROCK primary domain — the warehouse/subscription/NAV facility exposure to BDC, private-credit fund, and PE fund borrowers** |
| **10.e** | Loans to other NDFIs | Residual; includes some fintech / mortgage-lender exposure |

**May 15, 2026 = first publicly available bank-level 5-cat splits.** CDR Q1 2026 NDFI bulk release published this date per WALTER REQ. **Not yet pulled by BROCK; queued for next session.** This is the first ground-truth dataset for 10.d bank-by-bank exposure.

---

## 3. Single-name NDFI concentration watchlist

Anchored to NDFI as % of total bank loans (top-of-cohort tier). Per WALTER REQ, validated against primary call-report data where available.

| Bank | NDFI / Total Loans | Δ QoQ | Tier | Read | Source |
|---|---|---|---|---|---|
| **CUBI** (Customers Bancorp) | **33%** | — | Mid-bank, highest concentration | Idiosyncratic high-NDFI flag; small bank, big book proportionally | WALTER REQ (verify on CDR Q1 pull) |
| **WFC** | **21%** | — | Top-4 / GSIB | $212.1B absolute; Q1 first fraud-related NDFI loss disclosed | WFC Q1 10-Q ✓ |
| **MS BCI** (Morgan Stanley Business Credit Intermediary) | **19.73%** | **+316bps QoQ** | GSIB / IB | Rapid concentration build is the diagnostic; momentum tell | WALTER REQ (verify on CDR Q1 pull) |

**Why concentration matters more than aggregate:** FDIC framing says NDFI direct credit quality is benign (PDNA 0.15%). But indirect risk (simultaneous-draw scenario under stress) is concentration-dependent. A bank at 33% NDFI concentration has a different stress profile than one at 5%, even if both have the same PDNA on the direct loan portfolio.

**Action item:** WALTER+REGINALD+BROCK coordinated CDR Q1 pull. Add 5-10 more single names to watchlist after CDR data lands. Particularly want: ZION (regional w/ heavy NDFI?), HBAN, FITB, OZK (already in REGINALD's NDFI scope per earlier work), EGBN, FLG.

---

## 4. Sponsor-bifurcation diagnostic — new BROCK framework

Same underlying signal (defaults accelerating + NAV compression at sponsor-affiliated BDCs), opposite sponsor strategies.

### Diagnostic table

| Sponsor | Strategy | Evidence | Read |
|---|---|---|---|
| **KKR** | **DOUBLES DOWN** | FSK $450M+ support package ($150M perp pref + $150M tender @$11 + $300M repurchase + 50% incentive-fee waiver); KREST $50M backstop; KREF concurrent stress | 3 named KKR vehicles in concurrent stress; sponsor committing real capital to absorb slow-motion recognition. **Bearish-evidence-disguised-as-bullish-optics.** |
| **APOLLO** | **CASHES OUT** | MFIC Q1 $61M markdowns; Apollo shopping captive listed BDC at $0.85/NAV (~$3B portfolio); lending halted; 11% redemption quarter | Sponsor monetizing exposure into stress; APO-parent-level signal not just MFIC-level. **Bearish-evidence-as-de-leveraging.** |
| Blackstone | **BACKSTOPS** | BCRED $400M sponsor backstop + 7% cap upsize at Q1 7.9% redemption | Defensive maintenance; not committed-capital scale of KKR. **Mid-range.** |
| Blue Owl | **HOLDS-AND-PAYS** | OWL Q1 DL -1.1%, net deployment -$0.5B, fee-rally cracked; OBDC MIXED; no sponsor support package | Vehicle bleeding without sponsor action. **Bearish-by-omission.** |

### How to use the diagnostic

**When multiple sponsor-affiliated BDCs hit stress signals concurrently:**
- **Doubles-down (KKR pattern):** Sponsor with full information thinks slow-motion recognition is absorbable. Stage 2 grinding, not Stage 3 imminent. Bear-by-evidence, not bear-by-timing.
- **Cashes-out (Apollo pattern):** Sponsor reading the cycle and pre-positioning exit. Suggests sponsor-internal-view bearish enough to justify book-value losses + reputation costs. Stage 3 closer than tape suggests.
- **Backstops (Blackstone pattern):** Defensive, not directional. Maintenance mode.
- **Holds-and-pays (Blue Owl pattern):** Inertial — sponsor hasn't yet had to choose. Sponsor-strategy signal not yet activated.

**Trade implication:** Don't short the doubles-down sponsor's BDC (FSK example — tender at $11 is a hard floor). Short the cashes-out sponsor's vehicle or basket (BIZD captures the mix; MFIC direct if liquidity allows). Watch the holds-and-pays sponsor for inflection — when Blue Owl is forced to choose, that's the next big sponsor-bifurcation update.

**Cross-flag conditions:**
- KKR adds to FSK support package within 90 days → doubling down twice → bear signal upgraded
- Apollo announces successful BDC portfolio sale → cashing out validated → BIZD basket short conviction up
- Blackstone refuses BCRED Q2 backstop → backstop pattern breaks → gate cascade fires
- Blue Owl announces any OBDC support package → inertia broken; sponsor-strategy signal activates

---

## 5. Steelman the FDIC counter-case (RED-edge discipline)

FDIC 2026 Risk Review concludes NDFI lending presents **lower credit risk than traditional commercial lending**, supported by:
- PDNA (past-due / non-accrual) rate of **0.15%** on direct NDFI loans
- Strong historical performance data
- More favorable credit ratings on average than commercial book
- Stable concentration among well-capitalized GSIBs (86% at banks >$100B)

**The bull read:** NDFI growth is structural and benign. Banks have lent prudently to non-bank financials with strong collateral, robust covenants, and concentrated counterparty risk among the largest, best-capitalized sponsors. The 22.7% CAGR is post-2008 financial-system-deepening, not pre-crisis-leverage build.

**Why this doesn't dissolve BROCK's Stage 2 thesis:**

1. **FDIC measures direct credit performance — BROCK's thesis is on indirect transmission.** PDNA 0.15% is on the bank's loan to the NDFI. The Stage 2 thesis is about NDFI portfolio borrowers (PC underlying borrowers) defaulting → NAV markdowns → forced sales → gate cascades → eventual bank-loan stress. The transmission is 2-3 hops downstream of where FDIC measures.

2. **FDIC explicitly flagged the indirect risk** ("substantial indirect risks... NDFIs facing margin calls could collectively draw down their bank-funded credit lines, triggering a sudden and massive liquidity drain on banks"). The simultaneous-draw scenario is exactly the Stage 3 cascade BROCK has been pre-staging. FDIC named it; they just don't think it's imminent.

3. **The data cutoff matters.** FDIC 2026 Review uses YE 2025 data, pre-FSK Q1, pre-BlackRock probe, pre-Fed Barr 5/16 comment, pre-WSJ 5/16 narrative inflection. Q1 2026 data (CDR May 15 release) will be the first regulator-grade view incorporating actual cycle deterioration.

4. **PDNA is a lagging indicator.** Bank-disclosed metrics lag credit deterioration by 1-3 quarters. PIK conversion, non-accrual transition, and write-down sequencing all extend the lag. The 0.15% is the tape, not the substance.

5. **86% concentration in top-tier banks is the BROCK-relevant risk surface, not a mitigant.** When the simultaneous-draw scenario fires, it fires at the GSIB tier where the exposure concentrates. Concentration is the diagnostic, not the buffer.

**Net:** FDIC framing is correct on direct-loan PDNA today. BROCK thesis is on the indirect channel, lagged data, and the cycle-transition scenario FDIC named as the substantial indirect risk. The two are not in conflict — FDIC is benchmarking the current tape; BROCK is positioning for the next 2-4 quarter substance breakthrough.

---

## 6. Integration into BROCK STATUS / convergence matrix

**Already in STATUS** (this revival session):
- SIGNAL DASHBOARD row "Full NDFI scope (WALTER REQ)" with $1.4T / WFC $212B / +35.2% YoY framing
- CONVERGENCE MATRIX vector "Bank warehouse lines / NDFI" re-scored to 🔴🔴 (5) on WALTER NDFI correction
- BOTTOM LINE notes WALTER NDFI integration pending

**Updates required to STATUS following this framework doc:**
1. Replace SIGNAL DASHBOARD row "Top 4 US bank PC (BROCK working figure)" — demote with historical note rather than parallel-track
2. Update growth-rate citation from "+35.2% YoY" to "+22.7% CAGR multi-year" (more conservative; both citations have basis)
3. Add reference to this framework doc in BOTTOM LINE and FOLLOW-UP / NEXT SESSION
4. Add sponsor-bifurcation diagnostic to the convergence matrix vector with the 4-sponsor table

**To verify on next session:**
- CDR Q1 2026 NDFI 5-cat release (May 15) — pull 10.a-10.e splits for at least: JPM, BAC, Citi, WFC, MS, USB, GS, plus regionals OZK, ZION, HBAN, FITB, CUBI, FLG, EGBN
- MS BCI 19.73% +316bps QoQ — primary source confirmation (Q1 10-Q via call report)
- CUBI 33% NDFI — primary source confirmation

---

## 7. Cross-feeds to other agents

| Agent | Cross-feed | Status |
|---|---|---|
| **REGINALD** | NDFI 5-cat schema enables bank-side ticker × NDFI-channel × sponsor-affiliation lookup. WALTER appended schema to REGINALD CROSS_REFS 5/14. BROCK should send "post-CDR Q1 pull alignment" outbox after WALTER+BROCK coordinated pull. | Pending |
| **SHADE** | Sub-set 10.b (insurer NDFI) is SHADE's overlap. Athene/Apollo PE-insurer nexus surfaces here. Coordinated SHADE STATUS refresh request after CDR Q1 lands. | Deferred (SHADE not currently active) |
| **LIQUID** | NDFI growth +22.7% CAGR is funding-side credit-creation outside traditional bank-loan series. May reframe LIQUID's credit-cycle aggregate. | Reference-only for now |
| **OTTO** | BDC earnings data primary — sponsor-bifurcation diagnostic should inform OTTO's tier framework. | Reference-only for now |
| **WALTER** | Acknowledge REQ closed via this integration. Outbox reply file. | This session (pending) |

---

*BROCK framework doc. Sources: WALTER REQ-BROCK-20260514 + FDIC 2026 Risk Review + WFC Q1 10-Q + FFIEC RC-C schedule. Authored 2026-05-21 by BROCK.*
