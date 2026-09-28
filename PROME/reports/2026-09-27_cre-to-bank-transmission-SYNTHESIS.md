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

| D5 | **EGBN criticized multifamily maturities** | REGINALD: 4 loans, $155.8M. CREED: 7 loans, $249M | **RESOLVED 17:32 ET by the owner (REGINALD 15e2460b1, re-verified at EGBN Q2 deck, 8-K acc 0001050441-26-000088, SM/SS >$10M tables): criticized MULTIFAMILY maturing Aug–Dec 2026 = 4 loans, $155.8M, DSCR 0.15–0.89×, 6/30/26** (Prince George's $56.0M SS · DC $42.9M SM · Other US $36.4M SM · DC $20.5M SS). CREED's 7 / $249M is a different set — all property types with DSCR <1 (adds 2 storage loans + the Fairfax office), mislabelled 'MF'; the full Aug–Dec criticized window is 9 loans, $287.6M. CREED ADOPTED it at f0c937f13 (L122 re-read by REGINALD 17:37 ET); the same commit carries the FLG 20.45% basis into CREED's 9/26 property test. **D5 CLOSED.** |

No other disagreement on facts is open. CREED and REGINALD adopted each other's corrections today (the FLG 20.45% figure stands; CREED reversed its own 9/26 finding #4).

---

## 5. Observed · scenario · unknown — the load-bearing split

**OBSERVED (filings, dated):** the cohort aggregates in §1; each bank's mechanism figures in §2; capital, reserves and pre-provision revenue in §3; regional foreclosed CRE +26.4% in Q2 (FDIC QBP); Freddie MF delinquency 0.64% [Aug].

**SCENARIO ASSUMPTIONS (the bridge's, REGINALD's unless named):** every pool loss rate (FLG CRE pools: assumption only, no market anchor; FLG MF cross-checked only against one small bank's self-selected pool sale at ≤79% of face); OZK lab severity 65% (OZK desk band 50–65%, stress at the top — the "65–70%" label was corrected by OZK at 18ca81cf5); EGBN non-office haircut 13.3% (EGBN's own exits); pro-rata general-reserve credit; no earnings offset; Nano ≈ $120M / 17% until the FDIC's purchase-and-assumption terms post.

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
| **Nano P&A check-by Fri 10/9 (DOCKET L516); FDIC retained-asset sale (L515)** | FDIC loss estimate revised materially above $114M | **Evidence about small-bank Southern California CRE values only** — neighbourhood retail, medical office and small multifamily, several liens second-position (CREED §B4). It matches no FLG, EGBN or OZK pool on type or lien, so it **does not by itself move any bank's scenario rate**; at most it is weak directional evidence for a pool whose type and market it is shown to share, pool by pool. *(Corrected 17:4x ET on CATO's review: this row said "raises every scenario loss rate", adopted unchecked from REGINALD's cross-bank report §D.)* |
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
4. **One candidate is closable from existing public records, with no new tool, but its relevance is unestablished:** the FDIC's 2023 sale of Signature Bank's rent-regulated loans is a possible historical price for FLG's **NYC rent-regulated multifamily pools** (nonaccrual $1,737M · criticized $2,665M · pass $4,089M), whose loss sizes rest on the pools' own LTV and coverage with no clearing price. ⛔ It is **not** an anchor for FLG's ~$6.1B of no-comparable pools: those are CRE nonaccrual ($471M, parent mix 40% industrial / 22% office), CRE criticized ($1,367M) and multifamily criticized "other" ($4,274M, not NYC ≥50% rent-regulated), different categories that the sale may inform only where a match is shown. Before any headline discount becomes a loss assumption, a bounded read must establish what was sold, the transaction structure, and which FLG exposure each piece can inform, pool by pool — scope `PROME/plans/2026-09-27_signature-sale-relevance-SCOPE.md`. *(Corrected 17:4x ET on CATO's review: the prior text proposed it as the anchor for the whole $6.1B.)*
5. **The alternatives are weaker.** "Which bank is worst" is already answered three ways and agrees on "not tier-wide". FLG's capacity question turns mostly on the earnings path (a management question, answered by prints). The mid-pack breadth test is the right tripwire but cannot be read before late October.

**Defer:** new screens or tools (a national leading CRE screen is the obvious gap, but it is a build — it comes back separately if Will wants it) · scoring changes (REGINALD's matrix re-score stays at 11/07).

---

## 9. WQ-309 — the Signature Bank sale: integrated conclusion (17:5x ET)

**Authorization:** Will 17:44 ET (WQ-309), within `PROME/plans/2026-09-27_signature-sale-relevance-SCOPE.md`; no model or loss-rate change. **Inputs:** CREED `AGENTS/CREED/analysis/2026-09-27_signature-bank-2023-sale-economics.md` (515d18483, transaction economics from four primary FDIC releases) · FLG `AGENTS/FLG/reports/2026-09-27_signature-sale-vs-FLG-pools.md` (b119666fd, pool-by-pool). PROME re-read pr23105 and pr23107 at fdic.gov 17:5x ET: figures match CREED verbatim (FLG also re-read both).

**Conclusion: the sale gives no usable loss-rate comparison for any of FLG's seven pools.** The two desks agree; no disagreement to resolve.

**What the sale establishes (OBSERVED, FDIC primaries):**
- It was not a loan sale. The FDIC-Receiver sold **minority equity stakes in joint ventures** and kept the majority: market-rate venture $16.8B (office, retail, market-rate MF; *"does not hold any"* rent-stabilized loans), 20% for $1.2B, FDIC 80% **plus FDIC financing of 50% of venture value (~$6B note)** (pr23105, 12/14/2023) · rent-stabilized, Santander, $9.0B, 20% for $1.1B, FDIC 80%, no financing stated (pr23107, 12/20/2023) · rent-stabilized, CPC, $5.8B, 5% for $129M + $42M, FDIC 95% (pr23106, 12/15/2023). $16.8B + $9.0B + $5.8B = $31.6B of the ~$33B marketed.
- The prices are **levered minority-equity checks, not clearing prices for loans.** The only imputable value — ≈71% of book on the market-rate venture ($6.0B equity + ~$6B note ≈ $12B on $16.8B) — is a strike the FDIC sold 20% at, possibly affected by its own financing (a HYPOTHESIS: financing terms not examined, so neither direction nor size is established), and it covers the property types that exclude rent-stabilized loans. ~~For the two rent-stabilized ventures, leverage is undisclosed, so **no value is computable at all.**~~ *(Superseded by §12: the bid summary shows the Santander winning bid's leverage as "N/A".)*

**Which FLG pools it informs:**
| FLG pool (6/30/26) | Grade | Why |
|---|---|---|
| MF nonaccrual NYC ≥50% RR $1,737M | PARTIAL — directional only | Best type + market match, but Signature's performing/non-performing split is undisclosed and this pool is 100% nonaccrual; priced Dec-2023, pre-freeze; no computable value |
| MF criticized NYC RR $2,665M | PARTIAL — directional only | Same; "criticized-accruing" cannot be isolated |
| MF pass NYC RR $4,089M | PARTIAL — directional only | Weak evidence a performing rent-stabilized book had bidders pre-freeze; not a mark |
| MF nonaccrual other $395M · MF criticized other $4,274M | DOES NOT INFORM | Mostly non-NYC; an undisclosed NYC market-rate slice meets only the levered, blended ≈71% strike |
| CRE nonaccrual $471M · CRE criticized $1,367M | DOES NOT INFORM | 40% industrial (no analogue); NY office/retail slice meets only the levered strike |

The scope's expectation (relevance concentrates in the NYC rent-regulated pools) **held on collateral resemblance and inverted on numbers**: the only number that exists relates to the pools ranked least relevant, and even there it is not a clearing price.

**What it cannot tell us (named gaps; research stopped here per the authorization):** the FDIC's **realised recoveries** on the rent-stabilized ventures, 2024–26 (receivership / DIF reporting; the only route to a rate) · leverage on the CPC and Santander ventures · Signature's performing/non-performing, vintage and count mix · FLG-side splits not disclosed (geography by grade for "other" MF, property type by grade for CRE).

**New link found by FLG:** FLG itself bought **$1,680M of Signature CRE loans at fair value, and no multifamily**, in March 2023 (10-K FY2024, acc 0000910073-25-000038). So FLG's multifamily pools hold no disclosed Signature loans; its CRE pools may, measured from the acquisition fair-value mark, not par. Remaining balance and grade: not disclosed.

**Effect on this synthesis:** §8 item 4's candidate is **closed as no usable comparison**. The highest-value question in §8 is unchanged, and the sharper observation for FLG's NYC rent-regulated pools is now **FLG's own disposition pricing** (sale price vs carrying on its rent-regulated exits) at the Q3 call (~10/23) or 10-Q (~11/9) — same lender, same book, 2026 regime. The FDIC's realised Signature-venture recoveries are a possible later corroboration of direction, never a transferable rate; pursuing them is new research and needs Will's word.

---

## 10. Addendum — FLG's Pinnacle disposition (17:59 ET, FLG cd03d16be, KB-FLG-067; not a PROME assignment)

**The largest H1 exit from FLG's rent-regulated problem book was very likely below the debt and mostly financed by Flagstar itself.** [PRESS-GRADE: the 10-Q does not name the borrower; FLG rates the identification "very likely".] Pinnacle Group (~93 buildings, ~5,100 mostly rent-stabilized NYC units, Ch.11 since May 2025) sold to Summit Properties for **$451.3M**, closing 2026-03-31, against Flagstar debt reported at **>$564M** (so at least ~20% below the debt); **Flagstar lent the buyer $338.5M (~75% of the price)** (Multifamily Dive 2026-01-20; TRD).

**What it changes:**
- **FLG's case against stress (§3 A1, "self-liquidation at par") is overstated for the nonaccrual schedule's payoff leg.** The separately reported $1.1B/quarter CRE par payoffs are a different issuer series and are not contradicted.
- **It is the closest comparator on file for FLG's NYC rent-regulated nonaccrual pool** — same lender, same asset class, defaulted, 2026 — closer than Signature (§9). **It is still not a loss rate:** Flagstar's carrying value at sale is undisclosed, the debt figure is press-reported, and seller financing at ~75% may affect the price — a HYPOTHESIS until its terms (rate, tenor, recourse) are examined.
- It fits the synthesis's central finding (§1, §8): the one observed exit from this book did not clear at the loan's face, and the price that exists is financed by the lender.

**What would settle it:** Flagstar's carrying value and realized charge-off on the relationship (Q3 10-Q ~11/9 or the call ~10/23, if disclosed) — the "FLG's own disposition pricing" observation named in §9. No score, rate or grade changed.

---

## 11. EGBN follow-up — can the Fairfax maturity be observed? (18:00 ET, REGINALD a4fab14b6)

**Not observable now; definitively observable at EGBN's Q3 deck (~10/21, estimate).** EGBN names the loan only "Office, CRE, Fairfax" ($22.1M, 96% LTV, appraised $23.0M 4/2/26, DSCR 0.74, matured 9/25/26); every public record channel is keyed on property or party. The Q3 deck's own ">$10M criticized" table flags post-quarter payoffs (footnote 5), so it will show payoff, extension, downgrade or nonaccrual. Fairfax land records (CPAN, $150/quarter, or the courthouse in person) could identify it earlier — Will's hands and a spend: **WQ-310, PROME and REGINALD recommend waiting for the deck.** New context: a second Fairfax office loan ($18.5M, matured 2/28/26) is already nonaccrual — one Fairfax office loan has already failed at maturity; context for this one, not evidence about it. The other three criticized >$10M loans due 8/10–9/30 (Montgomery storage $56.2M · Prince George's apartments $56.0M, already extended once · Anne Arundel storage $15.0M) share the identification gate; silence is consistent with extension, not proof of payoff.

---

## 12. WQ-309 completion check — the Santander bid summary (18:0x ET; CREED c0461e5b5, FLG 9e3dcdf5a)

**Will's catch (17:57) was right: §9's "no value is computable for the rent-stabilized ventures" is WITHDRAWN. "Not a loss rate" STANDS.** CREED had inferred the absence of leverage information from the press releases without opening the FDIC's separate bid summaries (CREED's own named trap). PROME re-read the SIG RCRS A/B bid summary at fdic.gov 18:0x ET: winning bid SBNA Investor LLC (Santander) **$1,086,445,000, "LLC, 20% equity", leverage "N/A"**; every other bid 20% equity at **"1:1"**; **no legend defines "N/A"**.

| Quantity | Santander A/B ($9.0B rent-stabilized, Dec-2023) | Supported? |
|---|---|---|
| Implied equity value | $1.086B ÷ 20% = **$5.43B** | Yes, on a pari-passu equity assumption |
| Implied portfolio value | **≈60% of the $9.0B balance (~40% implied discount)** | Conditionally: only if "N/A" = no venture debt (strongly supported by the column's N/A-vs-1:1 contrast; not FDIC-labelled; the venture LLC agreements would confirm and were not opened) |
| Realized credit loss | — | No: not in any 2023 document (the recovery-history question Will did not authorize) |

The CPC ventures (C/D) went to a mission-driven bidder **below its cover bids** — a floor, not a market value.

**FLG's grades (9e3dcdf5a §F):** the three NYC rent-regulated pools stay **PARTIAL — as a valuation cross-check only**, never a rate, with five caveats (N/A unconfirmed · Dec-2023 pre-freeze · minority stake — how much of the ~40% reflects rates or illiquidity rather than credit is a HYPOTHESIS, not examined · blended performing/NPL mix · not a loss). Against FLG's own carrying basis: **row 1 (nonaccrual, $1,737M) carries at ~79.6% of original after 20.45% recognised — numerically ~20pp above the conditional bid valuation, a comparison across different populations, dates and bases, not a measured gap**, and for a 100%-nonaccrual pool a blended 60% is if anything an upper reference; the credit-only gap is not determinable · row 2 (criticized) carries ~95%, a weaker cross-check · row 3 (pass) ~99%, borderline does-not-inform. Rows 4–7 unchanged: DOES NOT INFORM.

**Pinnacle vs Signature:** ~~biased in opposite directions … They bracket the collateral in direction only~~ **WITHDRAWN 18:5x ET on CATO's review.** That seller financing inflated Pinnacle's price, and that an unlevered minority stake depressed Santander's, are **HYPOTHESES** — neither financing terms nor the minority-stake pricing were examined. The two observations cover different loan populations, dates (Dec-2023 vs Mar-2026) and valuation bases (a minority-equity bid vs a whole-portfolio sale against reported debt), so they are **not upper and lower bounds** and do not bracket collateral value.

**Net for the synthesis (corrected 18:5x ET on CATO's review):** the conditional Santander valuation (≈60% of book, Dec-2023) and FLG's Pinnacle exit (≤80% of reported debt, 3/2026) are **imperfect valuation references worth investigating, not a measured carrying-value gap.** Their numbers sit below FLG's ~79.6% carrying basis on its nonaccrual rent-regulated pool, but different populations, dates and bases mean the comparison does not measure how far FLG's marks are from clearing prices. WQ-309 is complete; no further Signature research is proposed.

---

## 13. WQ-311 — Valley National (VLY): integrated assessment (19:1x ET)

**Authorization:** Will 19:04 ET (WQ-311). **Inputs:** REGINALD `AGENTS/REGINALD/reports/2026-09-27_VLY_CRE_transmission.md` (part 1 6e21a2c37, parts 2–4 b4c2147ed; VLY Q2-26 8-K acc 0000714310-26-000036, 10-Q acc 0000714310-26-000041, Call Reports) · CREED `AGENTS/CREED/analysis/2026-09-27_VLY_property_comparable_challenge.md` (7415801fb). Both read in full at their commits.

**Assessment: NEITHER — VLY is not evidence of broader CRE-to-bank transmission, and not yet a bank-specific problem at the loss level. It carries one bank-specific early flag. Its Q3 print (est. Thu 10/22, not announced) is the next CHECKPOINT, not a guaranteed resolution — the Q2 payment deferrals run ~8 months, beyond Q3.** *(Qualified 19:5x ET on CATO's review, relayed by Will.)* The desks agree; no disagreement to resolve.

**Composition (OBSERVED, 6/30/26):** CRE ex-construction $27.9B, LTV 59%, DSCR 1.67×; Florida/Alabama 28% · NYC 25% · NJ 19% · national 21%. The national stress channels are small here: office $3.0B (11%; Manhattan $0.2B; average loan $3.5M; DSCR 1.83×) · NYC >50% rent-regulated **$559M (1.1% of loans)**, ~$1.5B counting 21–50%-regulated buildings — about 1/16 of FLG's $8.9B on the narrow definition, ~1/6 on the broad one; NYC multifamily DSCR 1.24× vs FLG's 1.01×. The 320% SR 07-1 concentration includes ~25pp of co-ops at 12% LTV (~292% ex-co-ops) and has fallen from 474% (12/23). **VLY is not a small FLG.**

**Deterioration vs mechanics (Will's distinction):**
| Effect | Finding |
|---|---|
| Loan sales / held-for-sale transfers | **One disclosed sale: a $9.1M non-performing CRE relationship, moved to held-for-sale in Q4-25 and sold in Q1-26 at a $767K gain; no other H1-26 transfers.** Materiality: ~1.5% of the $0.6B year-on-year fall in criticized CRE; its Q4-25 transfer lowered CRE nonaccrual by at most $9.1M, so without it the 6/25→6/26 nonaccrual rise would be up to ~$71M rather than $62.5M — **immaterial to the improvement, and if anything it slightly understates the deterioration** (DERIVED from REGINALD VLY §2) |
| Charge-offs | Small; they **understate** new problems (gross CRE nonaccrual inflow ≥ ~$42M vs net +$30.7M) |
| Denominator | Loan growth (+$649M CRE in Q2) flatters every ratio — ~40% of the criticized-CRE ratio improvement is denominator |
| **Genuine Q2 deterioration** | CRE nonaccrual +$30.7M (non-owner-occupied +$20.8M) · **multifamily 30–89 days past due $9.4M → $101.5M** · **CRE payment-delay modifications $108M (8-month deferral; 16× the year-ago quarter)** · one $25.8M office loan to nonaccrual at maturity |
| **Genuine improvement** | Criticized CRE **−$0.6B** year on year in dollars · classified −$131M in H1 · 12-month modification stock −44% |

**The flag (bank-specific, early):** the Q2 flow jump arrived in the same quarter VLY reported **"a decline in quantitative reserves largely within certain CRE loan categories"**, partly offsetting higher specific and forecast reserves. ⚠️ That does **not** establish that VLY's model ignored the deterioration: the model inputs and the categories are undisclosed, and the falling criticized book is one plausible input among others; payment deferrals keep loans current, so nonaccrual (+), charge-offs (0.17%) and foreclosed property ($4.1M) **understate stress by construction** until the deferrals end (~Q1-27); ACL/nonaccrual fell 164% → 128% in a year. Stock measures say improving; flow measures say a cluster of larger loans went bad. Which inputs drove the quantitative-reserve decline is UNKNOWN.

**Strongest contrary evidence:**
- *For stress:* multifamily past-dues and $108M of deferrals appeared in the same quarter as a decline in quantitative CRE reserves (cause undisclosed); NYC multifamily carries VLY's weakest coverage (1.24×).
- *Against stress:* criticized CRE down $0.6B in dollars, not only ratio; concentration 474% → 317%; only one immaterial loan sale ($9.1M, Q1); LTV 59%; pre-provision revenue ~$1.0B a year (covers a ~3.2% loss on the whole CRE book in a year, DERIVED).

**The decisive unknown — NOT in the filings:** where the $101.5M of late multifamily loans and the $108M of deferrals sit (NYC rent-regulated? Florida? one or two credits?), and whether they are the same loans. The two desks frame it on two axes: **whether the cohort rolls** into nonaccrual (Q3 is a checkpoint; the deferrals run past it, to ~Q1-27) (REGINALD: roll + another reserve cut → bank-specific; cure → neither confirmed), and **where it sits** (CREED: spread across the NYC rent-regulated or Florida multifamily book → a weak corroborant of the national multifamily cash-flow channel, still small; concentrated in one or two credits → bank-specific). No further desk work can place it before VLY discloses.

**Effect on the breadth question (§1, §6):** VLY does not move the synthesis off "concentrated at named banks". It is one of the mid-pack names in REGINALD's Q3 breadth test (≥3 of WAL · VLY · SSB · BKU · SBCF with CRE bad loans up >50% QoQ or a foreclosure build → broader); its Q3 multifamily roll is now the most specific single item in that test. Next: VLY Q3 release + deck (est. 10/22) · Q3 10-Q modifications and re-defaults (~early Nov) · Q3 Call Report (REGINALD run 11/07) · deferral end ~Q1-27.

---

## 14. How each bank handles troubled CRE — and what counts as recovery (19:4x ET, synthesis from existing desk work only)

**Asked by:** Will 19:34 ET: compare how each bank handles troubled loans (repayment, renewal, payment deferral, sale, write-down, foreclosure); distinguish demonstrated borrower recovery from a change in classification or timing; give the strongest evidence that workouts succeed; name the single unresolved distinction that matters most and an answerable investigation. **No new data collected** — every figure below is from a desk file already read today, cited by commit. ⚠️ The "bounded qualifications" in the same instruction are **NOT applied**: their source text is not in PROME's context; asked of Will.

### 14.1 Each bank's dominant workout route (6/30/26 filings as read by the desks)

| Bank | Repayment | Renewal / extension | Payment deferral / modification | Sale | Write-down | Foreclosure | Dominant route |
|---|---|---|---|---|---|---|---|
| **FLG** | CRE par payoffs $1.1B/qtr, 39% from substandard (issuer series); NYC RR payoffs $2.0B since 2024, 56% from substandard (FLG leg A1) | not disclosed as a series | ~40% of nonaccrual loans are **current** on contractual terms (O6) | Pinnacle: $451.3M vs >$564M debt, **FLG financed 75% of the price** (press; §10) | annual re-appraisal → partial charge-offs; MF NCO 1.0–1.2%; 20.45% recognised on RR nonaccrual | not prominent | **Payoff + appraisal write-down.** Cures are **1.6%** of nonaccrual outflow (from 59.5% in 2023H1) — the book is handed off, not healed (FLG leg) |
| **OZK** | RESG commitments −$2.1B in one quarter, mostly repayments; San Carlos paid off **with** a $14.8M charge-off | RaDD extension/recap in negotiation | Boston forbearance expired → nonaccrual | Wauwatosa hard-deposit sale and The Jack new-equity LOI slated for Q3 | $49.3M of Q2 partial charge-offs on 4 loans; 86% of nonaccrual carries $0 reserve (collateral method) | **Foreclosed assets $61M → $293M in H1; sales $6.9M** | **Foreclosure and hold.** Sullivan ($156.4M nonaccrual) **recapitalised into a pass loan** with new sponsor equity (OZK leg O1–O8, A2) |
| **EGBN** | office paydowns $156M over three years | Prince George's apartments ($56.0M) **extended** 4/21 → 8/21 | — | **Held-for-sale then sale:** office bridge 6/23→6/26 = $976M − charge-offs $205M − HFS $82M − paydowns $156M = $533M; 2026 non-office transfers FV $238.5M after a $36.7M write-down (**13.3%**), sales then cleared at **101–103% of carrying** | the write-down is taken **at transfer**, before the sale | Fairfax $18.5M matured 2/28/26 → nonaccrual | **Write down, move to held-for-sale, sell** (REGINALD q2_EGBN.md L40–46, L85) |
| **VLY** | Q2 maturities $1,457M: **$341M (23%) paid off and left** | **$1,082M (74%) retained by VLY** — its own renewal, not a third-party refinancing | **$108M payment-delay modifications** (8-month deferral; 16× a year earlier) | none in H1 (one $9.1M sale in Q1) | partial charge-offs; NCO 0.17% | OREO $4.1M | **Retain and modify** (REGINALD VLY §2–3) |
| **WAL** | — | — | $99M life-science credit: borrower **brought current** end-June, still nonaccrual, appraisal pending | — | fraud leg: Q1 $152.5M charge-off | OREO count 15 → 22, "primarily office" | **Charge-off on the fraud leg; buying senior liens** ($64M protective liens) (WAL leg §C–D) |
| PFBC (news sweep, f97e56783) | — | — | — | **$68.4M of note sales largely at par**, one −$0.95M | — | — | **Sale near par** (fraud-linked single relationship) |

### 14.2 Demonstrated recovery vs a change in classification or timing

| Evidence of… | Examples | Why it belongs here |
|---|---|---|
| **Demonstrated recovery** (cash from outside the bank, or new sponsor equity) | OZK Sullivan recap into pass with new equity · OZK RESG repayments · EGBN office paydowns · VLY's $341M paid off and left · PFBC notes sold near par · EGBN sales at 101–103% of written-down carrying | The risk left the bank, or someone put new money in below it |
| **Loss recognised, then exit** (resolution, not recovery) | EGBN 13.3% write-down then sale at carrying · OZK San Carlos payoff after a $14.8M charge-off · FLG appraisal charge-offs · WAL's fraud charge-off | The problem is resolved; the lender took the loss |
| **Classification or timing change** (no outside cash yet) | **VLY's 74% "retained" maturities** (its own renewal proves willingness, not the borrower's market access) · **VLY's $108M 8-month deferrals** (keep loans current) · EGBN's Prince George's extension · OZK's Boston forbearance and RaDD extension talks · **WAL's $99M borrower "brought current"** (appraisal pending) · FLG's 40% of nonaccrual loans still current · criticized-book declines described as "upgrades" (VLY, the split between upgrades and payoffs undisclosed) | Status or date moved; whether the borrower can pay or refinance is untested |
| **Exit with the risk retained** | **FLG's Pinnacle sale, 75% financed by FLG** (press) | The nonaccrual loan left the schedule; a new FLG loan to the buyer took its place |
| **Ambiguous — the funding source is undisclosed** | **FLG's $1.1B/qtr CRE par payoffs, 39% from substandard** · OZK's $2.1B RESG runoff | Who funded them is undisclosed — a limit on the conclusion, not evidence of deterioration. Either source can be a sound or an unsound resolution; what decides it is the borrower's capacity on the new terms and the loss recognised (§14.4, corrected) |

### 14.3 The strongest evidence that workouts are succeeding
1. **EGBN** cut criticized office from $287M to $77M, and its 2026 sales cleared at 101–103% of written-down carrying — marks taken at transfer were **sufficient**, the cleanest demonstrated success on file (after a 13.3% loss, not without one).
2. **FLG's** par payoffs: $1.1B a quarter, 39% from substandard, and classified loans fell $9.7B → $8.5B in H1-26 — the largest volume of problem-loan exits at face value in the fleet's evidence, **if** third-party funded.
3. **OZK's** Sullivan recap into a pass loan with new equity, and $2.1B of RESG repayments in a quarter; **PFBC's** fraud book sold near par; **VLY's** criticized CRE down $0.6B in dollars.
4. Outside banks: ARI's ~$9B performing book cleared at 99.7% of par (CREED).

**What limits it:** the strongest successes are EITHER after a write-down (EGBN) OR of undisclosed funding source (FLG, OZK runoff); FLG's own largest disclosed exit was lender-financed below the debt; FLG cures are 1.6% of nonaccrual outflow; VLY's retention and deferrals are untested by an outside lender.

### 14.4 The single unresolved distinction that matters most — CORRECTED 19:5x ET on CATO's review (relayed by Will)

~~When a troubled CRE loan leaves a bank at or near par, did an outside lender or new equity take the risk — or did the bank re-lend, renew or finance the buyer? … If exits are third-party funded … the named-bank losses stay isolated. If they are lender-funded … losses are deferred rather than avoided, and the 2027–29 maturity walls … test it everywhere at once.~~ **WITHDRAWN.** Who funded an exit does not by itself decide isolated vs broader: outside financing can move the risk to another lender without resolving the property problem, and a bank's own renewal can be a successful workout. Interagency workout guidance judges a workout on the borrower's repayment capacity, the loan's terms, the collateral, and the loss recognised — not on whether the lender changed (CATO's citation; the guidance itself not re-read by PROME). **Undisclosed funding is a limit on our conclusion, not evidence of concealed deterioration.**

**Restated distinction:** for the problem loans that left, or were kept and restructured, at these banks — **did the borrower demonstrate the capacity to pay on the new terms, and was the loss recognised at resolution enough?** That separates real recovery from a change in label or timing, symmetrically for successes and failures, and it is what the appraisal hinge (§8) turns on from the exit side.

### 14.5 Recommended investigation — SUPERSEDED by CATO's narrower scope (see WQ-312)

~~An "exit-source ledger" … categories (a)–(h) … Q3-26 as the test.~~ **Withdrawn as framed:** its categories overlapped (one loan can be written down, sold, and financed by the original lender), and it assumed the causal claim withdrawn in §14.4. CATO's narrower proposal, awaiting Will's own word (WQ-312): a **one-time Q2 diagnostic** from existing filings, in an existing report, covering the material disclosed problem-loan resolutions at the five banks and stating how much of total activity the evidence covers; **four separate fields per resolution** — what happened to the loan · where the cash came from · what exposure the bank retained · what loss was already recognised — plus later repayment performance where available; no double-counting; successes and failures tested symmetrically; a Q3 update only if the Q2 pass proves useful.

---

## 15. WQ-312 — the one-time Q2 workout check: integrated assessment (20:3x ET)

**Authorization:** Will 20:25 ET (WQ-312, his own word). **Integration:** REGINALD cross-bank report §F (c89788148), built from OZK 68fd0f4d5 · FLG 485507d09 · WAL 171338055 · REGINALD's own EGBN and VLY rows · CREED observability 38f5e3c7a. Each resolution carries four separate fields — F1 what happened · F2 where the cash came from · F3 exposure retained · F4 loss already recognised. Existing filings only; no recurring ledger.

**The answer: the check shows what happened to problem loans, but for most of the money it cannot show whether the resolutions succeeded.** The clean successes are few and small; the strongest evidence in the set is a failure signal inside retained, modified loans at Flagstar; and banks recognise the same kind of loss in different quarters.

### Successful resolutions
- **Clean, primary-sourced successes: two.** OZK's Sullivan loan ($156.4M) recapitalised to a pass loan with **new sponsor equity** (equity amount undisclosed) · EGBN's held-for-sale pipeline: 10 loans sold at ~101–103% of their post-write-down value, after 13.3–16.5% write-downs — the marks were sufficient, **after** a loss.
- **The funding source is undisclosed for most exit dollars** (FLG $190M of Q2 nonaccrual exits + ~$1.1B of par payoffs · OZK $2.92B of repayments · EGBN $161.5M sold · VLY $341M paid off · WAL's closings). **CREED: not observable in aggregate** — banks disclose the payoff, not the loan or its takeout. "Par payoffs prove the refinancing market is open" is an inference, not an observation. Per the rules, this is a limit on the conclusion, not a signal of hidden deterioration.
- Named outside-cash exits are press-grade: one third-party refinancing (FLG, $80.5M performing loan, 6% discount) and Pinnacle (75% financed by Flagstar).

### Retained risk
- ~~★ The strongest single signal in the set is a failure signal … $286M of modified multifamily loans re-defaulted within 12 months in H1-26~~ **CORRECTED (§16, Will 20:49 ET):** the issuer's MF "subsequently defaulted" figures — **$29M (three months) and $286M (six months) to 6/30/26 — are preserved as unreconciled disclosures**, not as a re-default flow. **What stands:** Flagstar's stock of MF loans modified in the prior 12 months was **$375M at 6/30/26, ~47% past due ($176M)** — a high delinquency level in a population that changed quarter to quarter, **not a cohort failure rate and not proof that the modifications failed**; 20% of its 12-month CRE modifications are past due. Flagstar made $382M of new CRE/MF modifications in Q2 (MF rate 7.68% → 5.17%, +1.2 years).
- **Untested retained risk:** VLY's $108M of 8-month payment deferrals · OZK's $141M of new foreclosed property carried at 95–100% of appraisal, unsold · WAL's $99M life-science loan at $0 loss and +7 foreclosed properties, plus **+$51M of senior liens WAL bought in Q2 — exposure added as a workout tactic, not resolved** · EGBN's $56M apartment loan extended to 8/21/26 and matured again, outcome undisclosed.
- ⚠️ **The modification tables are not comparable across banks:** OZK reported $0 of CRE hardship modifications against 37 construction-loan extensions. A low number can mean few problems or a narrow reporting definition.

### Recognised losses
- **Where severity is measurable, problem exits cost ~13–28% of balance** (OZK foreclosures 19.6%, range 7–28%; OZK San Carlos payoff 23.3%; EGBN transfers 13.3–16.5%); the one performing exit was 6% (press-grade). These sit inside the range of the bridge's cumulative assumptions; they do not calibrate any specific pool (different banks, property types and dates).
- **Recognition timing differs by bank, so the same economic loss lands in different quarters.** EGBN writes down at transfer and proves the mark by selling; OZK recognises little at foreclosure and carries foreclosed property near appraisal; WAL has recognised $0 on its named CRE. **Two readings are carried side by side (Will 20:38 ET):** RECOGNISED — OZK $49.3M of Q2 charge-offs on named loans (foreclosures at 19.6% severity), WAL $0 on its named CRE; and a HYPOTHESIS of **delayed loss** — OZK's $141M of new foreclosed property carried at 95–100% of appraisal and unsold, and WAL's $99M loan and seven new foreclosed properties at no recognised loss, may carry losses that land when they sell or are re-appraised. Neither reading is established; cross-bank charge-off comparisons mislead until they are tested.

### Coverage — how much activity the evidence sees
| Bank | Denominator | Funding source + retained exposure known | Loan-level |
|---|---|---|---|
| FLG | Q2 nonaccrual outflow $258M | 26% | $0 |
| OZK | Q2 construction-loan repayments $2.92B | 14% at credit level ($402M) | ~33% of its 3/31 classified + criticized book |
| EGBN | nonaccrual outflow $53.7M + $161.5M sold | 0% of cash exits | ~$122M |
| VLY | CRE maturities $1,457M | 0% of cash exits (renewals and modifications are its own) | $41.7M |
| WAL | none disclosed in dollars | — | 58% of H1 charge-offs were fraud/C&I, not CRE |

⚠️ **The named rows over-represent failures** (failures get named, successes get aggregated). Do not read the named sample as a failure rate.

### What it changes about our judgment
1. **The case against stress is weaker at Flagstar, and the modification route is now the one to watch.** Flagstar's par payoffs remain unverified, and its stock of recently modified multifamily loans was ~47% past due at 6/30 — a high delinquency level, not a cohort failure rate (§16).
2. **VLY's $108M deferral cohort now has a relevant warning, not a verdict:** Flagstar's stock of recently modified multifamily loans was ~47% past due at 6/30 (a changing population, not a failure rate; §16). Whether VLY's do is a different bank's loans — a HYPOTHESIS to test at VLY's Q3 and 10-Q, not an inference.
3. **Possible delayed losses at OZK and WAL are a HYPOTHESIS, kept alongside the losses already recognised, until their foreclosed property sells or is re-appraised.** This sharpens §8's hinge: the appraisal question now has a concrete test in OZK's OREO sales and WAL's $99M appraisal.
4. **Nothing here changes "concentrated at named banks, not tier-wide" at 6/30.** It changes how much weight the fleet can put on "the banks are working their problems out": that claim is observable for a small share of the activity.

### What remains unknown
Takeout funding for most exits (not observable in aggregate) · other buyer-financing beyond Pinnacle · exit prices vs par · OZK's foreclosed-property sale marks · the VLY deferral and FLG modification cohorts' Q3 performance · the route by which EGBN's $48.7M Fairfax apartment loan left the criticized list · whether modification reporting is comparable across banks.

### Would a Q3 update justify its maintenance cost?
**Not as a full re-run** — loan-level coverage is too low for a second pass to change the picture. **Yes as a targeted read of five items, folded into each desk's normal Q3 print work, no ledger:** ① FLG's modification past-due and re-default tables · ② VLY's Q2 deferral cohort and Q3 modifications · ③ OZK's foreclosed-property sales vs carrying value · ④ WAL's $99M appraisal and OREO valuation · ⑤ EGBN's held-for-sale sales vs marks and the Prince George's loan. Registered for Will's word as WQ-313.


---

## 16. Flagstar's modification finding, from evidence already held (20:4x ET; revised 20:5x ET on Will's ruling)

**Asked by:** Will 20:38 ET; **revised on his 20:49 ET ruling:** preserve the issuer's $29M and $286M figures as unreconciled disclosures · keep the ~$257M derivation withdrawn · remove the exclusion of an earlier cohort failure and the ~$48M bound · keep the high-delinquency finding without converting changing aggregate populations into a cohort failure rate · Q3 may add evidence but is not guaranteed to identify the Q2 cohort · capture the exact reconciliation question for the existing Q3 follow-up (WQ-313) · no further interpretive round on the same tables. **Evidence:** FLG's reading of Flagstar's 10-Qs (Q3-25, Q1-26, Q2-26) and FY25 10-K modification tables (FLG 767015a65, KB-FLG-069/070; REGINALD 43072e99e).

**Answer: the cohort detail is insufficient to distinguish a concentrated earlier failure, continuing deterioration, or delinquency carried through modification.** What the tables do establish is a high and rising delinquency level in Flagstar's stock of recently modified multifamily loans.

**The stock — loans modified in the prior 12 months still on the books (issuer-reported, aggregate populations that change quarter to quarter):**
| Date | MF 12-month stock | Current | 30–89 DPD | 90+ DPD | Past due |
|---|---:|---:|---:|---:|---:|
| 12/31/25 | no MF row reported | | | | |
| 3/31/26 | $123M | $109M | $0 | $14M | 11% |
| 6/30/26 | $375M | $199M | $23M | $153M | **47%** |
MF modifications made: Q1-26 ≈ $105M (derived: $364M H1 − $259M Q2; Q1 rate 9.63% → 3.87%) · Q2-26 $259M (7.68% → 5.17%, +1.2 years). ⚠️ The two stock readings cover **different populations** (the stock tripled between them), so the move from 11% to 47% is **not a cohort failure rate** and does not show that any particular vintage failed.

**The flows — issuer-reported "subsequently defaulted" (payment default = 30+ days past due, per the issuer), preserved as UNRECONCILED disclosures:** Q2-26 three months ended 6/30 — **MF $29M** · Q2-26 six months ended 6/30 — **MF $286M** · Q1-26 three months ended 3/31 — no multifamily row. The six-month figure does not reconcile to the two quarters as reported, and the basis is undisclosed. **The ~$257M "Q1" derivation stays WITHDRAWN** (it assumed the columns were additive). ~~Why not a concentrated earlier failure …~~ and ~~at least ~$48M of the 90+ bucket very likely predates the modification~~ — **REMOVED (Will 20:49 ET):** neither is supported; an earlier cohort failure is not excluded by the evidence, and the reset policy that the ~$48M bound depended on is undisclosed.

**What can be said about the newly modified loans:** the delinquent dollars sit in the stock of loans modified within the prior 12 months, and that stock was 47% past due at 6/30/26. **What cannot:** which quarter's modifications are delinquent · whether any modified loan failed after its new terms took effect or was delinquent when modified · what the $29M and $286M figures measure relative to each other · how the Q2 $259M cohort is performing.

**What it means for the thesis:** the modifications are **not yet evidence of borrower recovery**, and the delinquency level is a live warning at Flagstar; they are not evidence of a cohort failure rate or of accelerating loss.

**Carried to WQ-313 item ① (Flagstar's Q3 modification tables) — the exact unresolved question:** *In the Q2-26 10-Q, the MF "subsequently defaulted" figure is $29M for the three months ended 6/30/26 and $286M for the six months ended 6/30/26, while the Q1-26 10-Q reports no MF row for the three months ended 3/31/26. What population and period does each figure measure, and does the Q3-26 10-Q (three- and nine-month columns) reconcile them — including whether any of the $286M relates to loans modified before 2026?* Q3 may add evidence but is **not guaranteed** to identify the Q2 cohort. **No further interpretive round on the Q2 tables.**
