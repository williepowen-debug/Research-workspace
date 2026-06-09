# OTTO THESIS — v1.0

**Version:** 1.0
**Updated:** 2026-06-09
**Conviction (decomposed):**
- **Pattern / direction: HIGH** — 4 confirmed cockroaches in 8 months, recurring mechanism, no falsifying counter-evidence. The cockroach pattern is mechanistically over-determined.
- **Magnitude (recoveries near-zero): HIGH** — Tricolor ~3% vehicle recovery, ABS notes <10¢, First Brands debt 0.4¢ second-lien.
- **Near-term timing of specific tests: VARIABLE** — First Brands Ch.7 imminent (Jun 12, 85%); 2022-vintage CNL >25% in striking distance (Sep 30, 75%); subprime BBB spread test recalibrated down (Jun 30, 48% after primary-source FWP); Wilmington Trust franchise exit corporate-denied (Dec 31, 30%).
- **Carvana sub-thesis: LOWER** — allegation-only, no DOJ action, GT retained, governance vote 96% against separation. Carved out as a separate conviction layer; do not bundle with the 4 confirmed cases.

**Current state (daily):** see [`../STATUS.md`](../STATUS.md). Live forward catalysts in [`../docket/CATALYSTS.tsv`](../docket/CATALYSTS.tsv). Trajectory of view changes in [`CHANGELOG.md`](CHANGELOG.md). Falsifiable predictions in [`PREDICTIONS.tsv`](PREDICTIONS.tsv); resolved-row post-mortems in [`PREDICTIONS_ARCHIVE.md`](PREDICTIONS_ARCHIVE.md).

---

## ONE-LINER

The subprime/non-prime auto-finance ecosystem has been hiding multi-billion-dollar fraud for 5+ years and is now surfacing it in a recognizable pattern. Each new "cockroach" (Tricolor, First Brands, MFS, PrimaLend) revealed the next; recoveries are running near zero; transmission is reaching bank P&L, ABS spreads, BDCs, and private credit gating. The primary thesis is pattern-fraud; the secondary thesis ("Invisible Exit") explains *why* this cohort doesn't show up in standard DQ chains and *why* losses surface only at collapse. Both are validated, with the timing of specific tests being the variable.

---

## PRIMARY THESIS — "The Cockroach"

> **When you find one, there are more.**

### Claim
Subprime/non-prime auto finance has been hiding fraud for 5+ years through a small number of recurring archetypes. The market-clearing function (warehouse lending, ABS issuance, BDC/CLO holdings, related-party servicing) has been unable to detect or price the fraud until forced disclosure. Therefore each surfaced case is informational evidence that more exist under the same archetype.

### Mechanism — why this isn't coincidence
The non-prime auto ecosystem has four structural features that make fraud both *profitable* and *invisible* until collapse:

1. **Warehouse opacity / SPV silos.** Warehouse lender A sees only its SPV's collateral; lender B sees only its own. Double-pledging across SPVs (Tricolor, MFS) is detectable only by the *originator* or a forensic auditor — neither has incentive to flag in time.
2. **Below-IG ABS demand structure.** Subprime auto ABS subordinate tranches are bought by specialized credit funds with limited surveillance bandwidth. Servicer reports are delayed, K-1s opaque, and rating agencies rely on issuer-supplied data. Issues surface at trustee distribution, not in real time.
3. **Related-party servicing complexes.** When the originator, the servicer, and the residual-value insurer are commonly owned (DriveTime / Carvana / Bridgecrest archetype; First Brands / Point Bonita; Tricolor / Vervent), the related-party complex can mask extension rates, modify the timing of charge-offs, and shift value across the consolidated group without arms-length scrutiny.
4. **Skip-default in the immigrant subprime cohort.** Standard DQ models track 30→60→90 day delinquency rolls. When the borrower disappears with the vehicle (Tricolor: 30K missing vehicles, $1.1B), the loan never enters the standard chain — it goes from "current" to "skip" with no recovery. ABS waterfalls miss it until CNL emerges. This is the Secondary Thesis below; included here as a Cockroach feature because it's the *mechanism that lets a fraud lender's book look clean until collapse*.

Together, these four features mean: there is no functioning market mechanism for detecting subprime-auto fraud in real time. Discovery is forced by external shock (a lender default, a noteholder lawsuit, a DOJ raid). Therefore *each surfaced case re-priors the probability of additional cases existing under the same archetype*, conditional on no structural change in the four features above.

### Confirmed cases (4) + 1 alleged
*Live status table, distinguishes archetype:*

| Case | Archetype | Magnitude | Status |
|------|-----------|-----------|--------|
| **Tricolor** | Double-pledging + skip-default | $2B debt, $800M pledge gap, 30K missing vehicles ($1.1B) | Auctions ran; ~3% recovery; $113M distribution gridlock; Chu/Goodgame criminal trial Oct 19 2026 |
| **First Brands** | Invoice fabrication + Ponzi factoring | $12B debt | Indicted (Patrick James, 9 counts); 4 Evolution SPV debtors already Ch.7 (Apr 9); UST convert-or-dismiss **Jun 12** = OTTO-32 resolver |
| **MFS (UK)** | Double-pledging | £2B+ ($2.7B), shortfall £1.3B | CONFIRMED Feb 26 2026; Barclays + Atlas SP (Apollo); Bloomberg "regulatory black hole" |
| **PrimaLend** | BVY2 fraud | $286M debt | Plan confirmation Feb 2026 |
| *Carvana (alleged)* | Related-party manipulation | $70B+ mkt cap | Discovery production 2 **Jun 12**; GT retained May 5 (disconfirms one red-line trigger); see Carvana sub-thesis below |

### What would falsify the Primary Thesis?
- **18 months with no new case discovery** under any of the four archetypes (would suggest the surfacing wave has exhausted, not that the pattern was wrong — but the pattern's *forward* utility weakens).
- **A confirmed structural change** to one of the four mechanism features (e.g., real-time warehouse cross-pledge registry, mandated independent third-party servicing, etc.) — would weaken the prior on undiscovered cases.
- **Recovery rate normalization to pre-pandemic (~43%)** alongside Cockroach-magnitude losses — would suggest the cases are isolated fraud, not a systemic discovery problem (but this contradicts current data: 32.64% YE2025).

---

## SECONDARY THESIS — "The Invisible Exit"

> **Immigrant subprime borrowers don't default — they disappear.**

### Claim
A material fraction of subprime auto loans, concentrated in immigrant borrower cohorts (Tricolor: 75% undocumented Hispanic, 68% no credit score, 50% no driver's license), exits through skip-default rather than 30/60/90-day delinquency. Standard DQ chains miss this. Loss surfaces only at CNL, which lags origination by 18-36 months. Roll-rate models built on the non-skip cohort systematically under-predict ultimate losses on the skip-heavy cohort.

### Mechanism
1. Borrower receives loan with minimal credit history; vehicle is the collateral.
2. Loan stays current (often via cash payments) until borrower decides to relocate, return to country of origin, or otherwise become unreachable.
3. Borrower disappears with vehicle. Loan is recorded as "current" through the disappearance month, then becomes "skip" at next billing cycle.
4. Servicer skiptrace fails (no driver's license → no DMV trail; no credit score → no credit-bureau trail; cross-border → no enforcement). Recovery = $0.
5. ABS waterfall continues paying interest from reserve funds and trust cash until charge-off, masking the deterioration for months.

### Industrial validation (May 21 2026)
- **30,000 Tricolor vehicles missing** (~$1.1B), distinct from the 29,000 known double-pledged loans (CHANGELOG 2026-05-21 entry).
- **Vervent launched bilingual "Fresh Start" loan-modification program** for 30K+ delinquent borrowers (half >4 months DQ) — institutional concession that this cohort cannot be pursued via standard recovery.
- **Recovery rate 32.64% YE2025** vs pre-pandemic 43.73% (industry-wide, not Tricolor-only) — suppressed recoveries across the industry are consistent with rising skip prevalence, not just collateral deflation.
- **2022 vintage CNL realized 22.42% (Apr 15)** trajectory toward ~24.3-24.5% by Sep 30 (OTTO-04 75%) vs trigger 25%.

### Why this matters for the Primary Thesis
The Invisible Exit is what makes a fraud lender's book *look clean* until forced disclosure. A lender concentrating originations in skip-prone cohorts can post benign DQ statistics for 12-24 months while ultimate losses build toward 90%+. This connects the two theses: the cockroaches surface in the cohorts where the Invisible Exit is densest, because that's where fraud is hardest to detect via standard credit metrics. **Tricolor is both a cockroach and the industrial proof of the Invisible Exit. That's not a coincidence — it's the explanatory link.**

### What would falsify the Secondary Thesis?
- **Recovery ratio rebounds above 40%** sustained for 2+ quarters — would suggest skip prevalence is normalizing.
- **Q2 2026 NY Fed HDC** shows auto transition-to-90+ accelerating in line with ABS-level stress — would suggest the divergence I've been calling "Invisible Exit" is just measurement noise and the standard DQ chain is in fact catching the deterioration.
- **2022-vintage CNL stays below 22%** through Sep 30 — would suggest the cohort skip-effect has been overstated.

---

## CARVANA SUB-THESIS *(carved out — lower conviction)*

### Claim
Carvana's related-party servicing complex (Bridgecrest, DriveTime, GarciaCo) is being used to manipulate reported margin and credit performance: Bridgecrest services $26B at 0.117% (below-market) so DriveTime can absorb the loss while Carvana posts inflated gain-on-sale on loan portfolios sold to DriveTime. Discovery (Mar 15 → Jun 12 production 2) is the legal vector that would surface the mechanism.

### Why lower conviction
- **Allegation, not conviction.** No DOJ indictment, no SEC enforcement action, no auditor resignation.
- **Grant Thornton ratified May 5 2026** (96% for) — DISCONFIRMS the "GT resigns" red-line trigger that would have been a strong corroborator. Removed from active watchlist (CHANGELOG-equivalent in MEMORY-22).
- **Insider activity mixed.** CFO Form-144 selling $19.5M / 3mo zero buys is bearish, but RSU withholding at $334.16/share Mar 1 = insiders still holding, not fleeing.
- **William Blair added CVNA to June conviction list** — high-quality bull offset.
- **No short-seller activity Mar 15–Jun 8** (Gotham/Hindenburg/Muddy Waters silent). When the activist-short community goes quiet on a target with prior coverage, it's mild evidence the thesis isn't ripening fast.

### Status
Tracked but flagged as **separate-conviction layer** to the Primary Cockroach thesis. Do NOT count Carvana toward the "4 confirmed cases" count. If Jun 12 discovery production surfaces specific manipulation evidence, conviction reweights upward and Carvana can re-enter the primary case table.

### What would resolve
- **Bridgecrest servicing fee benchmark** (HIGH on research queue) — confirm 0.117% is below-market vs FHFA / industry peers.
- **Discovery production 2 outcomes Jun 12** — what documents are produced, what's withheld, motion practice.
- **Any GT engagement-letter modification or auditor change.**
- **Any new short-seller report** post-Jun 12 production.

---

## TRANSMISSION CHAIN

End-to-end, fraud-discovery to systemic spread:

```
[1] Fraud event surfaces (collapse / lawsuit / DOJ)
       ↓
[2] ABS subordinate tranches mark down (notes trade to <10¢)
       ↓
[3] ABS spread widens, BBB / BB+ tranches stop clearing
       ↓
[4] Warehouse lenders disclose exposure (bank 8-K / earnings)
       ↓
[5] BDC / CLO marks down holdings (BCRED, FSK, PSEC)
       ↓
[6] Private credit retail gates trigger (MS North Haven, Blue Owl, BlackRock HPS)
       ↓
[7] Spread back to subprime ABS issuance (loop closes — IG-only? below-IG re-prices?)
```

### Current state of the chain (Jun 9 2026)
| Stage | Confirmed instances | Status |
|-------|--------------------|--------|
| [1] Fraud surface | Tricolor, First Brands, MFS, PrimaLend | 🔴 — 4 events in 8mo |
| [2] ABS tranche markdown | Tricolor notes <10¢; First Brands debt 0.4¢ 2L | 🔴 — confirmed |
| [3] Subprime BBB spread | +190bps (EART 2026-2 Class D, Mar 20 `[CONF SEC FWP]`) vs 250 trigger | 🟠 — below trigger, recalibrated down Jun 8 |
| [4] Bank disclosure | JPM $170M, 5/3 $178M, BCS $150M, Regions $68M, MTB litigation TBD, OBK $74.7M | 🔴 — 6 named banks |
| [5] BDC markdown | $237M First Brands BDC exposure, FSK div cut, PSEC div cut | 🔴 — confirmed cascade |
| [6] PC gating | BCRED 7.9% redemptions, MS North Haven gated, Blue Owl gated, BlackRock HPS restricted | 🔴🔴 — systemic |
| [7] Spread back to ABS | Below-IG IS clearing (Jun 8 falsification of "IG-only" claim) | 🟢 reframed — below-IG market functional |

### Critical observation
**Stages 1-6 of the chain are all firing.** Stage 7 (the loop-back to ABS issuance) was OTTO's working hypothesis for "system breaks here" — the Jun 8 EART 2026-2 below-IG print falsifies the "issuance halt" version of that hypothesis. **What this means:** the market is absorbing the cockroach wave through *higher spreads* (BBB ~190bps, 2× pre-pandemic) and *demand for higher-quality issuers* (Exeter cleared, but smaller stressed shelves may not). It is NOT absorbing through full issuance shutdown. OTTO-07 (subprime ABS shelf halt) remains the right open test for stage 7 — needs revision down from 55% in light of EART clearing the full stack.

---

## WHY NOW — the timing claim

The Cockroach pattern is *surfacing* in 2025-2026 (not 2027, not 2024) for three reasons, all current:

1. **2022 vintage maturation.** Subprime auto loans peak losses 24-36 months after origination. 2022 was the worst-underwritten vintage in the modern series (S&P explicit) — post-COVID demand surge + used-car bubble + lax warehouse covenants. Losses are emerging *now* because the math says so. Confirmation: Fitch Jan 2026 subprime ANL 9.81% (post-pandemic high); 2022 CNL realized 22.42% Apr 15.
2. **Post-Fed-pause ABS market re-pricing.** Through 2023-24, ABS spread compression masked deteriorating fundamentals — investors reached for yield in a low-spread environment. The 2024-25 Fed pause + 2026 rate-cut anticipation shifted the spread-yield tradeoff; subprime BBB went from ~120bps (Jan '25) to ~190bps (Mar '26) and could go further. Stress at the issuer level (Tricolor, Flagship, CPS) now has a discount-rate amplifier on top of the cash-flow problem.
3. **Auditor cycle catching up to the 2022-23 origination wave.** Independent auditor work on 2022-23 originated portfolios is finishing now. First Brands examiner report (Feb 25 2026), Tricolor 2022+2024 auditor warnings (cited in Feb 27 noteholder suit), and the Carvana Discovery Order are all the natural endpoint of a 2-3 year audit cycle. Surfacing is *backlog-clearing*, not coincidence.

### Why this matters
A "why now" claim has to be defensible against the alternative *"this is the usual fraud rate, OTTO is pattern-matching noise."* The three timing drivers above are all observable and dateable — not vibes. If 18 months from now the auditor backlog is cleared, the 2022 vintage has matured into the loss curve, and ABS spreads have re-stabilized, the *current* surfacing rate should decelerate. That's a falsifiable prediction baked into the timing claim.

---

## KEY THRESHOLDS

Live dashboard values are in [`../STATUS.md`](../STATUS.md). Threshold *rules* (the single-metric mechanical triggers, severity ladder) are in [`../CLAUDE.md`](../CLAUDE.md) § Thresholds (Quick Reference). When CLAUDE.md rules and STATUS § SIGNAL DASHBOARD severity disagree, **STATUS is the operative read** — STATUS integrates cross-metric and systemic context.

---

## RISK FACTORS / INVALIDATION

| Risk | Prob | Impact | Mitigation |
|------|------|--------|-----------|
| **Carvana earnings/disclosure clean + substantive rebuttal of Garcia related-party allegations** | 25% | Carvana sub-thesis -40%; primary thesis unchanged (Carvana is carve-out) | Already carved out — primary thesis isolated from Carvana resolution. Bridgecrest fee benchmark research priority HIGH. |
| **DOJ finds fraud is limited to named companies (no expanding witness list)** | 20% | Pattern conviction -30%; "more cockroaches" prior weakens | Watch DOJ press releases + cooperating-witness motions. Tricolor Chu trial Oct 19 2026 is the major discovery event. |
| **No additional lender failures in 6 months (through Dec 31 2026)** | 25% | Surfacing-wave conviction -25%; "auditor backlog clearing" timing claim weakens | Watch warehouse lender tape (Barclays ABL pullback continues, Flagship Credit ratings, CPS ECNL revisions). |
| **Recovery ratio rebounds >35% by Q3 2026** | 15% | Invisible Exit -30%; secondary thesis weakens | Track quarterly Fitch / Auto Remarketing recovery prints. |
| **Subprime ABS market continues issuing below-IG cleanly into Q3** | 35% | Stage-7 transmission weakens; OTTO-07 falsifies. Note: this risk is **already partly materialized** (Jun 8 EART 2026-2 print). | Re-rate OTTO-07 downward from 55%; watch Q3 issuance pipeline for smaller stressed shelves vs Exeter. |
| **Bank disclosures plateau at current 6 names + dollar amounts don't grow** | 20% | OTTO-30 falsifies; bank-transmission magnitude conviction -20% | Q2 2026 bank earnings (Jul-Aug) is the operative test. M&T litigation dollar update is the key marginal print. |

### What would STRENGTHEN the thesis (confirmation triggers)
| Condition | Impact |
|-----------|--------|
| 5th fraud case discovered (any archetype) | Pattern +20% |
| Bank loss >$500M new disclosure | Magnitude +15% |
| Recovery ratio <28% | Invisible Exit +15% |
| Cooperating witness reveals new participants (Chu trial prep) | Pattern +15%, Tricolor magnitude +10% |
| 2022 vintage CNL crosses 25% (OTTO-04 confirms) | Mechanism +15% |
| Carvana discovery production surfaces specific manipulation evidence | Sub-thesis re-promotes to primary (case-count → 5 confirmed) |

### Thesis break condition
The primary Cockroach thesis breaks when (a) no new case surfaces for 18+ months AND (b) 2022-vintage CNL fails to cross 25% AND (c) recovery rates rebound to >35%. **All three** are needed because each addresses a different leg (surfacing-rate, mechanism, magnitude). The secondary Invisible Exit thesis can break independently of (a) on (b)+(c) alone.

---

## POSITION VIEW

**OTTO generates signal; OTTO does NOT size positions.** Trade flow is: OTTO research → PREDICTIONS.tsv (if predictive) → TRADE.md (position ideas) → PROME consolidates across agents → Will decides. Active trade rails (CVNA puts, ALLY puts, monoline expressions) live in [`../TRADE.md`](../TRADE.md).

> ⚠️ **TRADE.md is materially stale** (last refreshed pre-CVNA 5-for-1 split May 7; strikes off by 5×; triggers dated Feb 18 2026). Active rehab pending — do not size off TRADE.md figures without re-verifying. See [`../STALE_PUNCHLIST.md`](../STALE_PUNCHLIST.md) item #1.

### What this thesis implies for positioning (substance-level, sizing-agnostic)
- **CVNA equity puts** are the cleanest expression of the Carvana sub-thesis IF discovery surfaces manipulation evidence. Currently lower conviction (see sub-thesis section). Insider/auditor signal mixed.
- **Bank credit / equity** (KRE-style + select names) is the cleanest expression of Stage 4-5 transmission. REGINALD owns this — OTTO routes signal, doesn't size.
- **BDC equity** (BCRED/FSK/PSEC) is the cleanest expression of Stage 5-6. BROCK owns this.
- **Subprime ABS spread** (CDX or single-name) is the cleanest market-verdict expression of Stage 3. No active OTTO position; market-verdict tracking via OTTO-05.
- **Duration (TLT)** captured "same credit stress" thesis at +$600 historical, while equity puts ran -84% — auto-memory `[[feedback_put_vs_duration_expression]]` lesson. Re-applies if Will wants to express the systemic-stress thesis without equity-tape regime risk.

---

## PREDICTIONS

Canonical source: [`PREDICTIONS.tsv`](PREDICTIONS.tsv). Post-mortems for resolved rows: [`PREDICTIONS_ARCHIVE.md`](PREDICTIONS_ARCHIVE.md).

### Calibration scoreboard (as of 2026-06-09)
- **Resolved: 5** — OTTO-01 ✅ (MFS UK, 4th cockroach), OTTO-08 ✅ (BDC gate, MS North Haven + Blue Owl), OTTO-09 ✅ (BDC marks >10% on First Brands), OTTO-27 ✅ (FSK div coverage <1.0x), OTTO-26 ❌ (PSEC div cut — directionally correct, date wrong by ~2.5mo)
- **Open: 12** — see TSV. Three resolve Jun 30 (OTTO-05, OTTO-28); one resolves Jun 12 effectively (OTTO-32 First Brands Ch.7 via UST hearing); four resolve Sep 30 (OTTO-04 CNL, OTTO-06 monoline DPD, OTTO-10 subprime origination share, OTTO-29 Tricolor distribution); rest Dec 31.
- **Hit rate (substance): 5/5 directionally correct** (100%); **1/5 missed on date specificity** — calibration lesson: date-specific Resolve_Dates at <50% confidence are the weakest link (see archive post-mortem for OTTO-26).

### Failure-pattern synthesis (for future predictions)
- **Date-specificity at low confidence is the weakest link** (OTTO-26 — right substance, wrong window by 2.5mo).
- **Forward-discovery vs known-unknown blur** (OTTO-30 — Origin Bancorp surfaced predating prediction window; counts toward named-banks list but doesn't auto-confirm the prediction whose spirit was *forward* discovery).
- **Extrapolation off adjacent benchmarks** (OTTO-05 — extrapolated subprime BBB from A-rated +30bps lag; primary-source FWP came in below extrapolation, forcing 62→48% recal).
- **Litigation-allegation weighting** (OTTO-31 — plaintiff allegation of full custodial-business exit ≤40% pending corporate-side confirmation; corporate denial dropped 60→30%).

These are the working calibration warnings before writing any new prediction.

---

## CROSS-AGENT LINKS

### → Outbound (signals OTTO routes via WALTER)
- **→ REGINALD:** Bank disclosure tracking — JPM/5-3/BCS/Regions/MTB/OBK. OTTO surfaces named banks; REGINALD sizes exposure. MFS UK Barclays £600M+ exposure is the largest single-bank cross-link. M&T Tricolor litigation $ update is the key marginal print.
- **→ CARL:** Auto DQ transmission; recovery ratio; ABS-level stress vs consumer-level flow divergence. CARL owns the consumer-flow read.
- **→ BROCK:** BDC exposure ($237M First Brands across 15 BDCs); CLO transmission; private credit gating cascade. BROCK owns BDC/CLO sizing.
- **→ LIQUID:** Funding stress from lender collapses; warehouse line pull-back patterns.
- **→ MARCO:** Immigration cohort employment + remittance signals — input to Invisible Exit transmission timing.
- **→ NEXUS:** Cross-domain synthesis (Tier-2 opt-in brief at [`../NEXUS_BRIEF.md`](../NEXUS_BRIEF.md)).

### ← Inbound (signals OTTO consumes)
- **← REGINALD:** Bank-level exposure sizing; warehouse facility commitments; NDFI aggregate disclosures.
- **← CARL:** Consumer DQ-chain reads (NY Fed HDC quarterly).
- **← MARCO:** Immigration enforcement intensity; remittance flows (proxy for cohort employment).
- **← HENRY:** Vol regime / IV context for option-expression sizing inputs to TRADE.md.

---

*OTTO THESIS v1.0 | 2026-06-09 | Seeded from STATUS § THESIS block + CHANGELOG trajectory + PREDICTIONS ledger + MEMORY § Findings. Replaces scattered thesis-content across STATUS / CLAUDE.md / CHANGELOG. Future version bumps logged in [`CHANGELOG.md`](CHANGELOG.md).*
