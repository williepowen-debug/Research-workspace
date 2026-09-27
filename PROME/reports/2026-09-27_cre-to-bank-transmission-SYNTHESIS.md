# CRE → regional-bank losses: first synthesis (2026-09-27, Sun evening)

**Asked by:** Will, 2026-09-27 17:24 ET: *"determine how CRE distress is reaching regional-bank losses, whether the evidence supports isolated bank problems or broader exposure, and what would change that assessment."* **Status: FIRST SYNTHESIS, 5 of 5 desk legs in, 17:3x ET.** First synthesis from EXISTING evidence, before any new research. Research only: no score, threshold, tool or trade change is proposed here.
**Plan:** `PROME/plans/2026-09-27_cre-to-bank-loss-transmission-PLAN.md` (e614dee5e).
**Inputs (each read in full at its commit):**
| Desk | Artifact | Commit |
|---|---|---|
| REGINALD | `AGENTS/REGINALD/reports/2026-09-27_cross-bank_CRE_transmission.md` | f2ba5de14 |
| OZK | `AGENTS/OZK/research/threads/2026-09-27_CRE_LOSS_TRANSMISSION_OZK_LEG.md` | a7c8e5792 |
| FLG | `AGENTS/FLG/reports/2026-09-27_CRE_to_FLG_loss_transmission.md` | ff355bc8c |
| WAL | `AGENTS/WAL/research/2026-09-27_cre-transmission-WAL-leg.md` | 56390ca84 |
| CREED | `AGENTS/CREED/analysis/2026-09-27_property-comparable-transfer-test.md` | cd4674c5e |
Base analysis: REGINALD `reports/2026-09-26_CRE_top3_loss_bridge.md` (b93e3ac58, corrected).

⚠️ **Brief correction (PROME's error, caught by REGINALD):** the plan cited REGINALD's live view as "concentrated at OZK/EGBN". That is the 8/13 wording on a retired page. The live STATUS claim since 8/20 is **FLG / EGBN / AMTB on the matrix, with WAL and OZK mid-pack**; the 9/26 CRE-specific cut is **FLG · EGBN · OZK** (AMTB out: its credit points are mostly non-CRE). No desk's assignment depended on the wording.

---

## 1. The answer first

- **Through the 6/30/26 filings, CRE losses at regional banks are CONCENTRATED at named banks, each by its own mechanism, not spread across the tier.** In REGINALD's 14-bank cohort, the CRE bad-loan rate FELL 2.46% → 2.23% year on year and H1 CRE net charge-offs fell $528M → $452M (FFIEC Call Reports). Only OZK had a sharp new rise (0.04% → 1.34%). [OBSERVED]
- **The property stress is broader than the bank losses so far, and it reaches banks with a lag of one to several quarters.** Freddie multifamily delinquency has risen four months running (0.42% Feb → 0.64% Aug); at regional banks, foreclosed CRE rose +26.4% in Q2 while their noncurrent rate fell (FDIC QBP). "Concentrated" is a statement about 6/30, not about Q3. [OBSERVED market side; the lag is INFERENCE]
- **The common thread is not a shared loss, it is a shared recognition route: every bank's CRE loss is gated by appraisals, and the appraisals have not yet been tested by sales at scale.** OZK carries $288–293M of foreclosed property at 86–100% of appraisal against one own sale at 58%; FLG carries $1,571M of nonaccrual loans with no allowance on the strength of appraisals; EGBN's remaining office values rest mostly on pre-6/30/25 appraisals while its own re-appraisals ran −14% to −29%; WAL's live bear waits on one $99M life-science appraisal. **If appraisals are systematically above clearing prices, the losses are deferred everywhere, not isolated.** That is the hinge between "isolated" and "broader".
- **CREED's test makes the hinge sharper: there is no clearing price for a bank-held CRE loan anywhere on the board.** Every realized comparable the fleet holds is a CMBS liquidation or a one-off property sale. So every bank pool's loss size rests on the bank's own appraisals and exits, or on a borrowed comparable of imperfect fit. The bridge's arithmetic is sound; most of its anchors are not market comparables. Pools with **no defensible comparable at all** carry real weight (FLG's three alone ≈ $6.1B of balance), so the bridge's *stress* totals are more assumption-driven than its *base*. Appraisal vintage biases every mark **high**: ~70% of FLG's LTV appraisals predate 1/1/24, ~89% of EGBN's office LTVs predate 6/30/25, and distressed office clears ~20% below even the latest appraisal (Deutsche Bank via CREFC, SECONDARY).
- **Capacity differs by an order of magnitude, and the yardstick matters.** OZK: an earnings question (stress ≈ 0.4–0.6× a year of pre-provision revenue). EGBN: 1.6–2.3×. FLG: 4.5–10.5× on observed earnings, ~1× only on management's 2027 guidance; capital is FLG's backstop, ending ~0.4–1.2pp above its 10.5% CET1 target under the stress with the buyback. None of these is a solvency finding: the loss rates are scenario assumptions, and FLG's CRE rates have no market anchor.
- **Nano Banc does not change the picture.** Its capital was destroyed mostly by legal costs; nationally no other bank matched three of its four ratios. For WAL it adds no new exposure. Its one transferable lesson is reserve coverage collapsing while bad loans rose; three cohort banks are below 100% today (FLG 29% · AMTB 51% · EGBN 88%).

---

## 2. How CRE distress becomes bank losses — four banks, four mechanisms

| Bank | Best-evidenced mechanism (desk's pick, not the most alarming) | Stage now | Key observed figures | Source |
|---|---|---|---|---|
| **FLG** | **Value, not exits:** capped rent-regulated NYC multifamily income → lower value at the annual re-appraisal → partial charge-off, on a classified pool that keeps refilling | Running now; the rent freeze and 2027 resets are future amplifiers with no loss yet | MF NCO rate flat 1.0–1.2% annualised; $780M new nonaccrual H1-26; ~40% of nonaccrual loans current (collateral, not payment, failure); 20.45% of RR nonaccrual original balance already recognised | FLG leg (1); 10-Q Q2-26; deck s16 |
| **OZK** | **Maturity failure → nonaccrual → foreclosure → foreclosed-property marks** on 2022-vintage construction/transitional loans. NOT the lab loan (RaDD), which has no observed loss | Running now; losses recognised late | 82% of H1 gross charge-offs are 2022-vintage ($85.2M / $103.5M); foreclosed assets $61M → $293M in H1, sales $6.9M; 86% of nonaccrual carries $0 reserve | OZK leg (1); 10-Q |
| **EGBN** (no desk; REGINALD) | DC office largely cleaned up; the remaining stress is under-appraised pass office + multifamily maturities | Pending | Criticized office $287M → $77M; 4 criticized MF loans $155.8M maturing Aug–Dec 2026 at DSCR 0.15–0.89× (D5 resolved: CREED's 7 / $249M was all property types) | REGINALD A2; 10-Q acc 0001050441-26-000096 |
| **WAL** | What already happened was **fraud-driven** (Cantor/Stupin; Q1 $152.5M charge-off) — Nano sits inside that closed leg. The **live** channel is **ordinary office / life-science CRE** | Fraud leg closed (recovery tail only); CRE leg priced, unresolved | NPL $781M (+15% QoQ); OREO count 15 → 22 "primarily office"; $99M life-science credit on nonaccrual, $0 charged off, appraisal pending | WAL leg §D; Q2 10-Q |

**One broader channel exists beyond the four names:** OZK's loans to other CRE lenders ("debt-on-debt", $430M) took their first charge-offs in 18 quarters in H1-26 ($42.4M, `RIAD5409`) — non-bank CRE-lender stress arriving at a bank. The book has shrunk 64% in a year, so it is running off, not building. [OBSERVED; attribution to The Jack + San Carlos INFERRED-HIGH by OZK]

---

## 3. Capacity to absorb — reconciled

| Bank | Stress loss on covered pools (REGINALD bridge) | ÷ a year of pre-provision revenue | CET1 if it lands at once, no earnings offset | Desk's reading |
|---|---:|---|---|---|
| **FLG** | $1,618M | **8.4–10.5×** trailing-4Q ($143M, observed) · **4.5–5.7×** Q2 run-rate ($264M, one observed quarter annualised) · **0.8–1.3×** 2027 guidance (management assertion; needs NII +42–51%) | 13.16% → 11.3–11.7%; **10.9–11.3% with the $250M buyback** (target 10.5%) | Agrees on dollars and CET1 arithmetic; differs on the earnings yardstick. Management's own 2026+27 provision guidance ($190–290M) ≈ the bridge's BASE case, not its stress |
| **EGBN** | $226M | 1.6–2.3× | 14.58% → 12.6–13.1% | (REGINALD only) |
| **OZK** | $656M | 0.6× (trailing $1,082.6M, re-verified by OZK); ~0.4× on OZK's probability-weighted reading | 11.80% → 10.7–10.8%; ~10.3% with the $200M buyback | Agrees on arithmetic and on "earnings, not capital"; reads $656M as a tail-at-once (see §4) |
| **WAL** | not in the bridge | — | — | Nano adds no new exposure; bounded by $72.4M gross Cantor residual + $64M protective liens, both booked |

---

## 4. Disagreements and how PROME resolves them

| # | Disagreement | Positions | Resolution |
|---|---|---|---|
| D1 | **FLG earnings yardstick** | REGINALD: trailing-4Q is the only observed basis → 8.4–10.5×. FLG: trailing is a turnaround trough incl. a loss quarter; show run-rate 4.5–5.7× and guidance 0.8–1.3× too | **Show all three, labelled by basis, never averaged.** Trailing = observed four quarters; run-rate = one observed quarter ×4; guidance = management's assertion and the optimistic bound (its 2026 margin guide was already cut once). The conclusion does not change on any basis: **at FLG, capital, not earnings, is the loss absorber if the stress arrives within two years.** |
| D2 | **How to read OZK's $656M** | REGINALD: stress scenario, lab loan at 65% severity applied in full. OZK: $361M of it is the foreclosure branch (17% on OZK's tree) applied with certainty; probability-weighted ≈ $424M (~0.4×); 65% is the top of OZK's own 50–65% adjusted band, anchored on a lender's credit bid; losses arrive over quarters | **Different quantities, not a conflict.** $656M is a stress (a branch assumed to happen); $424M is an expected loss conditional on stress. Both desks conclude "earnings drag, not capital". Carry $656M as the stress and OZK's weighting beside it as an alternative, never mixed. ⚠️ The 65% severity anchor (Campus at Horton) is a single credit bid with post-foreclosure leasing UNKNOWN — thin either way. |
| D3 | **FLG CRE concentration: 350% vs 327.5%** | Management reports 350%; FLG's SR 07-1 computation 327.5% | **Definitional, not a dispute:** the issuer's figure matches FLG's owner-occupied-included variant (≤351.6%). Cite the basis with the number. |
| D4 | OZK foreclosed property $288.1M vs $292.7M | REGINALD (Call Report, RESG foreclosed) vs OZK (10-Q, all foreclosed assets) | Perimeter difference; state the basis. Not material to any conclusion. |

| D5 | **EGBN criticized multifamily maturities** | REGINALD: 4 loans, $155.8M. CREED: 7 loans, $249M | **RESOLVED 17:32 ET by the owner (REGINALD 15e2460b1, re-verified at EGBN Q2 deck, 8-K acc 0001050441-26-000088, SM/SS >$10M tables): criticized MULTIFAMILY maturing Aug–Dec 2026 = 4 loans, $155.8M, DSCR 0.15–0.89×, 6/30/26** (Prince George's $56.0M SS · DC $42.9M SM · Other US $36.4M SM · DC $20.5M SS). CREED's 7 / $249M is a different set — all property types with DSCR <1 (adds 2 storage loans + the Fairfax office), mislabelled 'MF'; the full Aug–Dec criticized window is 9 loans, $287.6M. CREED's adoption step is PENDING at its inbox (2026-09-27b). |

No other disagreement on facts is open. CREED and REGINALD adopted each other's corrections today (the FLG 20.45% figure stands; CREED reversed its own 9/26 finding #4).

---

## 5. Observed · scenario · unknown — the load-bearing split

**OBSERVED (filings, dated):** the cohort aggregates in §1; each bank's mechanism figures in §2; capital, reserves and pre-provision revenue in §3; regional foreclosed CRE +26.4% in Q2 (FDIC QBP); Freddie MF delinquency 0.64% [Aug].

**SCENARIO ASSUMPTIONS (the bridge's, REGINALD's unless named):** every pool loss rate (FLG CRE pools: assumption only, no market anchor; FLG MF cross-checked only against one small bank's self-selected pool sale at ≤79% of face); OZK lab severity 65% (OZK desk band 50–65/70%); EGBN non-office haircut 13.3% (EGBN's own exits); pro-rata general-reserve credit; no earnings offset; Nano ≈ $120M / 17% until the FDIC's purchase-and-assumption terms post.

**UNKNOWNS that gate the answer:** (1) Q3 at every bank — all bank figures are 6/30, and the 10Y at 5.18% [9/24] and the MF delinquency rise are post-quarter; (2) **clearing prices for problem CRE held by these banks** — almost none of OZK's foreclosed property has sold, FLG's payoff loss content is unestablished (KB-FLG-066), WAL's $99M appraisal is pending; (3) the population — the cohort is 14 names chosen under earlier priors, and no national CRE-specific leading screen exists; (4) office is not separable in the Call Report; (5) WAL's Nano lien ownership and priority at failure, all three states open (Ontario/Chino/Moreno Valley/Bellflower); (6) buyback execution at FLG and OZK (first read: Q3).

---

## 6. What would change the assessment

| When | Observation | Moves toward |
|---|---|---|
| **Q3 prints ~10/20–28; Call Reports → REGINALD run 11/07** | Mid-pack banks (WAL, VLY, SSB, BKU, SBCF): **≥3 with CRE bad-loan rate up >50% QoQ or a new foreclosure build** | **BROADER** |
| Q3 (OZK) | Foreclosed-property sale prices vs carrying (8150 Sunset, Seattle, Atlanta); Boston 10 Prospect title vs sale | Sales < ~80% of carrying → marks were high → **severity up** (and a signal for appraisal-gated books elsewhere) · at carrying → OREO stress overstated |
| Q3 (WAL) | The $99M life-science appraisal; any new office migration | Low mark / migration → WAL bear-medium confirms · benign → bear narrows |
| Q3 (FLG) | New nonaccrual formation, MF NCO rate vs its 1.0–1.2% band, par payoffs and their substandard share, buyback executed | Formation up / NCO above band / payoffs slow → stress · payoffs ≥ $1B/qtr at par → against |
| EGBN Q3 10-Q ~early Nov | The 4 criticized MF maturities ($155.8M; 9 / $287.6M across all types — D5): par payoff/extension vs held-for-sale at a haircut | Par → scenarios overstate · haircut → EGBN severity up (still concentrated) |
| **Nano P&A check-by Fri 10/9 (DOCKET L516); FDIC retained-asset sale (L515)** | FDIC loss estimate revised materially above $114M | Harsher small-bank CRE marks → **raises every scenario loss rate**, not the ranking |
| FDIC Q3 QBP ~late Nov | A second consecutive rise in regional foreclosed CRE **and** CREED-T-03 firing | **BROADER** |
| 10/1 (FLG) | Rent freeze in force (T-08) | Confirms the input; changes no loss figure — the effect reaches FLG's reviews ~Q2-2028 |

---

## 7. CREED — do the loss comparables transfer?

Six-dimension grade (property type · market · vintage · appraisal date · lien · performing vs defaulted) of every anchor in the bridge and the Nano scenario:

| Grade | Anchors |
|---|---|
| **Transfers best** | OZK's own Seattle office exit at **58% of appraisal** → The Jack (same bank, type, market, basis; **n=1**, a different asset) · Concord lab appraisal **−32% in 13 months** → Boston 10 Prospect (best type match; an appraisal move, not a sale) · EGBN's own office re-appraisals **−14% to −29%** (an appraisal signal, not a sale) · FLG's own 20.45% recognised |
| **Partial** | BCB's NJ/NY problem-pool sale at **≤79% of face** for FLG rent-regulated nonaccrual (a ceiling, rent-reg share undisclosed, self-selected pool; brackets the implied 24–34% cumulative severity without contradicting it) · ARI's **99.7%** as a cap on pass books (national performing book, not NYC rent-regulated) · EGBN's **13.3%** non-office exit haircut on its multifamily (right bank, type not shown to be MF; the 30% stress is defensible only on the high-LTV tail) · OZK's 58–80% exits applied across three foreclosed offices (appraisal dates differ asset by asset) |
| **No defensible comparable** | FLG CRE nonaccrual ($471M) · FLG MF criticized "other" ($4,274M) · FLG CRE criticized ($1,367M) · EGBN owner-occupied criticized ($64.6M), other income CRE special mention ($92.1M), construction criticized ($62.0M) · OZK other nonaccrual ($48.5M), Tahoe ($29.4M), OREO life-sci and LA land (soft/LOI) · the Nano retained pool |
| **Removed already (correctly)** | Office sale-vs-2017-purchase prints (−61/−72%) as FLG loss rates · EGBN's 39.6% office-era haircut on a multifamily book |

**The OZK lab loan (RaDD) is the one case** where a distressed severity on a pass-rated loan transfers, and only on collateral condition (≈3.3% leased, interest paid from reserves), not a borrowed sale. It swings OZK's stress by ~$250M, more than every other OZK pool combined.

**Nano:** no comparable matches its property type (neighbourhood retail / medical office / small multifamily) or its lien position (four named liens are seconds). The CMBS severity range (35–73%) is consistent with, not confirming, its ~17% loss scenario. A second-lien sale price measures the lien, never the building.

**What CREED says cannot be closed from the desk:** no NYC rent-stabilized clearing price after June 2026 exists on any fleet surface (the FDIC's 2023 Signature Bank rent-regulated sale is the obvious historical comparable and is in no fleet record) · no EGBN multifamily-specific exit haircut · no DC-area multifamily market data (HOMER has no metro layer) · Boston 10 Prospect's $330M pending sale does not reconcile with its ~$186M implied appraisal.

---

## 8. Highest-value remaining question

**Are these banks' appraisal-based carrying values on problem CRE above what that CRE actually clears at — and by how much?**

**Why this one:**
1. **It is the hinge between "isolated" and "broader".** Every bank's recognition route runs through appraisals (§1, third bullet). If marks hold when tested, the concentrated reading stands. If they are systematically high, the same deferred loss sits inside every appraisal-gated book, including banks nobody is watching.
2. **It converts the scenarios into observations.** Every loss rate in the bridge is an assumption; FLG's have no anchor at all. Observed clearing prices are the only thing that can anchor them.
3. **It is answerable from events already on the calendar**, without building anything, and the first bank-held clearing prices the fleet has ever had arrive in sequence: **OZK's Q3 call (mid/late Oct)** — foreclosed-office sale prices vs 89–100% carrying, Boston 10 Prospect's $330M sale closing or failing, the RaDD report-back · **WAL's $99M life-science appraisal (Q3)** · **EGBN's Q3 10-Q (~early Nov)** — CREED's single highest-value observation: its criticized multifamily maturities resolving at par, extension or a held-for-sale haircut would be the fleet's **first measured bank multifamily exit haircut**, replacing the borrowed 13.3%; EGBN's reserve coverage swings 2.0× → 0.67× on that one number · **the Nano P&A (~10/5–10/9) and the FDIC's pool sale (+3–9 months, L515)** — the first bank-held SoCal CRE clearing price, to be recorded by lien position.
4. **One gap is closable from existing public records, with no new tool:** the FDIC's 2023 Signature Bank rent-regulated portfolio sale is a historical clearing price for exactly FLG's collateral class, and no fleet surface holds it. It is the cheapest single piece of evidence that would anchor FLG's ~$6.1B of no-comparable pools. **This is the one piece of additional research PROME would recommend first, if Will wants to expand** (a CREED or FLG read of the FDIC's own sale disclosures).
5. **The alternatives are weaker.** "Which bank is worst" is already answered three ways and agrees on "not tier-wide". FLG's capacity question turns mostly on the earnings path (a management question, answered by prints). The mid-pack breadth test is the right tripwire but cannot be read before late October.

**Defer:** new screens or tools (a national leading CRE screen is the obvious gap, but it is a build — it comes back separately if Will wants it) · scoring changes (REGINALD's matrix re-score stays at 11/07).
