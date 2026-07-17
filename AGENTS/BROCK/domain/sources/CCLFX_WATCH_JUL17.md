# CCLFX forced-sale clearing-price watch — BROCK stand-up + PREMISE CORRECTION
**Date:** 2026-07-17 Fri ~10:15 ET · **Owner:** BROCK (primary, per NEXUS spec routed by PROME 7/16)
**Consumers:** NEXUS (PRED-45 / second-root split), PROME (GATES row), REGINALD (bank leg)
**Spec consumed:** `AGENTS/NEXUS/outbox/2026-07-16_to-BROCK-cc-REGINALD_cclfx-forced-sale-watch-spec.md`

---

## VERDICT (return-format per spec §5)

`clearing price [¢] · NOT OBSERVABLE — no loan-level print exists or is scheduled`
`arms-length-confirmed · NO — the transaction is GP-led into a sponsor-organized levered vehicle`
`what-was-sold · $1B first-lien NAV sell-down; Cliffwater RETAINS ~$9B of the same assets`
`leads-manager-marks · NO`
`PRED-45 verdict · NOT FIREABLE ON THIS INSTANCE (not "refuted" — the instance is mis-specified)`
`lead time before 7/25-28 · NEGATIVE. The event is ~4 months OLD (3/10/26), and the next CCLFX primary disclosure is ~8/7/26 — AFTER the marks window.`

**Stand the watch: YES — but not as specified. Corrected rows in §3.**

---

## 1. THE PREMISE CORRECTION (the load-bearing finding)

The spec's headline — *"CCLFX gating pro-rata **and** force-selling ~$1B NAV of private loans into the secondary market **to meet redemptions**"* — **fuses two real but unrelated events, ~3 months apart.** The causal link ("to meet redemptions") is not in any source; it is an inference created by the fusion.

| | **Event A — the gate** | **Event B — the $1B secondary** |
|---|---|---|
| **What** | Q2 repurchase offer capped at 5% vs ~17% requested → pro-rata, ~⅓ satisfaction | $1B first-lien NAV moved into an investment vehicle; buyer to capitalize at **2:1 leverage** |
| **Date** | Offer window 5/8–5/29/26; priced 5/29; **reported 6/2/26** | **Reported 2026-03-10** — and "in market for **several months**" prior (→ ~Dec-25/Jan-26 origin) |
| **Source** | Bloomberg 6/2/26; N-23C3A 5/8/26 [PRIMARY] | **PitchBook 3/10/26** |
| **Structure** | Rule 23c-3 quarterly repurchase | **GP-led secondary**, Evercore-advised |
| **Motivation per source** | Redemption demand | **"Portfolio management of the interval fund rather than forced liquidity"** — PitchBook's own words |

**Event B PRE-DATES Event A by ~3 months. B cannot be a response to A.**

**Five further disqualifiers on Event B as an "arms-length clearing print":**
1. **Structure.** Assets move into a *new vehicle* the buyer capitalizes at **2:1 leverage**. The negotiated price of a levered-vehicle stake is **not** a loan mark — financing terms are inside the price. This is the spec's own §3 guard #1 (affiliate/organized) and DEWEY's trap-class 3 (GP-led CVs are sponsor-organized; no arms-length breakdown).
2. **Retention.** Cliffwater **keeps ~$9B of exposure to the same assets** in CCLFX. A ~10% sell-down that retains the rest is the opposite of a fire sale — and it is textbook adverse-selection exposure (spec guard #2: what got sold?).
3. **Routine, not novel-distress.** PitchBook: Cliffwater *"conducted secondary-market transactions to manage its portfolio like this before."*
4. **Precedent cuts the other way.** Same-technique deals: **New Mountain ~$500M** and **Blue Owl $1.4B** — Blue Owl's was **larger**. This is an emerging BDC/semi-liquid portfolio-management tool, not a Cliffwater distress tell.
5. **No price, by construction.** Cliffwater and Evercore **declined to comment**; pricing undisclosed and unlikely to publish. There is no scheduled venue where a loan-level clearing price surfaces.

> **⚠️ Same error class as BRK-25, one week apart, same domain.** DEWEY 7/16 killed the "$0.85/NAV Apollo bid" by showing it was **MFIC's May trading ratio welded onto ADS's tender** — two true facts, different vehicles, fused. This is the identical shape: **a March GP-led rebalance welded onto a June redemption wave.** `[[finding_deep_research_stale_vintage_headline]]` · `[[finding_designation_date_lags_event_date]]` · `[[finding_catalyst_vs_consequence_conflation]]`
>
> **Honest caveat against my own correction:** the sell-down IS contemporaneous with the repurchase escalation (in market from ~Dec-25, i.e. alongside the 5.32% → 7.00% climb). "Wholly unrelated to redemptions" would be **overclaiming**. The defensible statement is narrower and sufficient: **it is not a July event, not a forced sale per its only source, and structurally incapable of producing an arms-length loan print.** Motivation = AMBIGUOUS; vintage and structure = SETTLED.

### The "it's early" premise fails on the filing calendar
The spec's core value claim is that the clearing price *"lands BEFORE the 7/25-28 BDC marks = the slow layer's first honest mark."* **No CCLFX primary disclosure lands before the marks window.**

| Venue | Next date | vs 7/25-28 |
|---|---|---|
| N-23C3A (repurchase offer) — cadence 8/7/25 · 11/6/25 · 2/5/26 · 5/8/26 [PRIMARY: EDGAR CIK 1735964] | **~2026-08-07** | **AFTER** |
| N-CSRS (semi-annual, incl. proration + peak revolver draw) | **~Dec 2026** | **AFTER** |
| NPORT-P (~60d lag) | next ~8/22 (covers 6/30) | **AFTER** |

**Only paywalled trade press (PitchBook LCD / Bloomberg) can reach it pre-window** — and DEWEY 7/16 recorded that *"the CCLFX 17%/$1B never reached a primary."* A watch whose only fast path is a paywall we do not hold is a watch that will not fire on schedule. **State this to NEXUS plainly rather than running a 2-3×/wk cadence that manufactures the appearance of coverage.**

---

## 2. WHAT IS ACTUALLY THERE — and it is worth having (primary-confirmed, new)

Stripping the fused premise does **not** leave nothing. The N-CSR gives a clean, primary series neither DEWEY report nor the spec framed:

**[PRIMARY: CCLFX N-CSR, filed 2026-06-08, FY-end 3/31/26, CIK 1735964 — BROCK-verified verbatim from the filing]**

| Repurchase pricing date | 6/9/25 | 9/8/25 | 12/9/25 | **3/10/26** | *5/29/26* |
|---|---|---|---|---|---|
| **% of Class I shares repurchased** | 3.42% | 2.90% | 5.32% | **7.00%** | **5% (capped)** |
| **Amount repurchased (Class I)** | $1.025B | $0.918B | $1.757B | **$2.344B** | n/d |
| **NAV/share (Class I)** | $10.76 | $10.72 | $10.67 | **$10.52** | **$10.39** [5/5/26] |

**Two findings fall straight out:**

**(a) 🔴 THE DISCRETIONARY ACCOMMODATION WAS EXHAUSTED, THEN WITHDRAWN.** CCLFX's fundamental policy is a ≥5% quarterly offer; Rule 23c-3 permits repurchasing up to **2% above** the offer before prorating. At the **3/10/26** pricing CCLFX repurchased **7.00% = 5% + the FULL 2% discretionary top-up** — $2.344B, **the largest in fund history**. At the **5/29/26** pricing it offered **5% and used none of the top-up — while demand ROSE 14% → ~17%.**
> **This is the tell, and it is the opposite of the industry comp.** BCRED breached its own 5% cap **UPWARD** to ~7% in Q1 to fill 100% (via an insider-feeder offset) [DEWEY 7/16, PRIMARY]. CCLFX went to its ceiling and then **retreated** into rising demand. Accommodation is a finite resource and CCLFX spent it. **But note precisely what this is: a LIQUIDITY-TERMS escalation, not a PRICE event** — exactly the distinction the spec's own §3 insists on (*"do not read a gate alone as a mark-down"*). It does **not** fire PRED-45 and must not be laundered into one.

**(b) 🟠 NAV/share in a monotonic 5-quarter decline:** $10.76 → $10.72 → $10.67 → $10.52 → **$10.39** (−3.4% over the year, and the two largest steps are the last two). Parallels OBDC's 5th consecutive decline. Feeds the NAV-discount vector; not an independent vote (same Q2-wave antecedent).

---

## 3. THE WATCH ROWS (corrected — what fires, on what data, checked when)

| # | Row | Fires on | Data / venue | Checked | Priority |
|---|---|---|---|---|---|
| **C1** | **Q3 repurchase-cap decision** — does CCLFX hold 5%, re-arm the 2% top-up, or cut below 5%? | 🔴 offer **<5%** or suspension = escalation · 🟠 **5% held** into still-elevated demand = accommodation stays withdrawn (base case) · 🟢 **7% top-up re-armed** = accommodation restored, de-escalates | **N-23C3A, EDGAR CIK 1735964** [PRIMARY] | **~8/7/26** (cadence-derived; check 8/5–8/12) | 🔴 |
| **C2** | **Q3 satisfaction rate** | 🔴 <⅓ (worse than Q2) · 🟠 ~⅓ flat · 🟢 >50% | Trade press ~1wk post-pricing; N-CSRS ~Dec | ~early Sept | 🟠 |
| **C3** | **Peak intra-year revolver draw** (DEWEY's best marker) | 🔴 peak **>$4.0B** (vs $3.15B FY26) **or** accordion exercised toward $10B | **N-CSRS ~Dec 2026** / N-CSR Jun-2027 [PRIMARY] | ~Dec 2026 | 🟠 |
| **C4** | **GP-led sell-down RECURRENCE** — *the reframed Event B* | 🔴 a **second** CCLFX sell-down, or one at a **widening** size/cadence, or a named **discount** attached to any BDC GP-led | PitchBook/Bloomberg/Creditflux/9fin | opportunistic (news-driven) | 🟠 |
| **C5** | **PRED-45 proper — an actual arms-length loan print** | 🔴 ≤90¢ **third-party, non-sponsor-organized, loan-level**, in-window | Any BDC/interval fund — **not scoped to CCLFX** | opportunistic | 🔴 |
| **C6** | **NAV/share direction** | 🟠 6th consecutive decline | N-23C3A (NAV stamped on each offer) | ~8/7/26 | 🟡 |

**Cadence verdict: NOT 2-3×/week.** The primary calendar is empty until ~8/7. A 2-3×/wk cadence on a paywalled fast-path buys nothing and manufactures false coverage. **Adopt: one dated primary checkpoint (~8/7 N-23C3A, C1 — the highest-information row in the set) + opportunistic news capture on C4/C5.** Revisit if a *named* secondary print surfaces.

**Three guards carried forward (spec §3), all of which the March deal FAILS:**
1. Arms-length vs affiliate → **FAILS** (GP-led, sponsor-organized vehicle).
2. Cream-skimming → **UNTESTABLE and adversely indicated** — first-lien sold, ~$9B retained; residual quality unknown.
3. Single-print → **moot**; there is no print.

---

## 4. CROSS-AGENT

- **NEXUS:** PRED-45 does **not** fire and is **not refuted** — CCLFX is **not a valid instance**. The candidate **NON-oil second root does not exist on this evidence**; the 2-6wk split should **not** move Break↑ on CCLFX. The real second-root candidate, if any, is the **OTF §5 valuation litigation** (below) — but that is allegation-tier, not a price.
- **REGINALD:** the spec points you at **NAV facilities / subscription lines. Cliffwater has none** [DEWEY prompt-14, PRIMARY: N-CSR]. The actual channel is a **PNC-agented senior secured revolver** ($4.84B committed / $1.25B drawn at FY-end, **peak $3.15B intra-year**, accordion to $10B) + **$6.51B senior notes, purchasers undisclosed**. Marker = **peak intra-year draw, not year-end balance**. Thresholdable bank names are **CFG** ($8,756M capital-call + $4,096M secured private-credit finance) and **WAL** ($14,928M NDFI, but ~69% is mortgage-warehouse — PE funds only $1,260M/2.1%). Note routed → `AGENTS/REGINALD/inbox/`.
- **PROME:** **do NOT register a GATES row on the clearing print** — there is no observable print and no scheduled venue. If a gate is wanted, register **C1 (~8/7 N-23C3A cap decision)**, which is dated, primary, and binary. Per DEWEY prompt-14 §5c, the bank-leg conjunction is *"a watch, not a trip"* — registering it would overstate its calibration.

---

**Sources:** PitchBook, "Cliffwater in market with $1B private credit secondary sale," **2026-03-10** (via Yahoo Finance relay; pitchbook.com direct = 403) · Bloomberg, "Cliffwater Private Credit Fund Stung by 17% Redemption Requests," **2026-06-02** (via Advisor Perspectives 6/4, Benzinga 6/2, Seeking Alpha, Investing.com relays) · **CCLFX N-CSR 2026-06-08, CIK 1735964 [PRIMARY, BROCK-verified]** (repurchase table, NAV series) · CCLFX N-23C3A 2026-05-08 [PRIMARY, via DEWEY] · EDGAR submissions JSON CIK 1735964 (filing cadence, BROCK-pulled 7/17) · `AGENTS/DEWEY/output/2026-07-16_bank-private-credit-exposure.md` · `AGENTS/DEWEY/output/2026-07-16_bdc-brk25-print-hunt.md`
