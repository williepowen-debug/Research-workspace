---
signal_id: SIG-W-20260813-016
date: 2026-08-13
time_dispatched: 2026-08-13T18:3xZ
origin: Will-Telegram "10 more" archive-flush batch 2026-08-13 ~17:13Z, item 7 of 10 (plus the item-6 Seattle fragment from BM-08, now superseded by this fuller version). Batch manifest BM-20260813-09.
source: **@FCNightingale (Nightingale Associates)**, X, ~7/27-28, quoting Seattle developer **Ray Connell** and citing **Holland Partner Group**. ⚠️ **Secondary — WALTER did not reach the underlying local reporting, and no vacancy-survey provider (CBRE / JLL / Cushman / Moody's) is named for the 37% figure.**
domain: BANK_CRE
cluster: BANK_COLLATERAL
precedence: ROUTINE
action: [CREED, REGINALD]
info: [BROCK, SHADE, HOMER]
entities: [Seattle-CBD, office-vacancy, office-to-residential-conversion, Mandatory-Housing-Affordability, Holland-Partner-Group]
signal_type: data-update
confidence: 0.55
verdict: INDETERMINATE
consumer_lens: `VX-CREED-9.03` (office vacancy) has been seeded at Q1 vintage and TWO CYCLES STALE since 7/27 — CREED flagged it again on 8/13 — and CREED's own verify list names Seattle.
cluster_secondary: MISC
---

# 🟡 **A 37% downtown Seattle office vacancy claim, with ~20M SF empty and a named reason conversions are not clearing it — landing on a CREED instrument that has been Q1-stale for two cycles and whose own verify list already names Seattle.**

## 1. The claim

| | |
|---|---|
| Downtown Seattle office vacancy | **37%**, with **~20M SF** of empty office space |
| Developer **Ray Connell**, on conversion economics | *"You look at all the office space that's available for lease, most of that space would be so challenging to do a conversion in that it's not worth even looking at"* — comparing it to **"turning a boat into a car"** |
| Named regulatory barrier | Seattle's **Mandatory Housing Affordability (MHA)** fees — build affordable on-site or pay into a municipal fund; **"$40,000 for a small project to millions for larger ones"** |
| Worked example | **Holland Partner Group paid $5 million in MHA fees** to get *Sloane* approved |

## 2. Why this is routed rather than killed as a single-city anecdote

**CREED's `VX-CREED-9.03` (office vacancy) is seeded at Q1 vintage. CREED's own `SCRATCH.md` reads: *"now 2 cycles Q1-stale (flagged 7/27, still stale 8/13)"*, with the fix conditional on *"a clean Moody's Q2 print, if locatable"* — which has not been locatable for two cycles.** And **CREED's `LAST_COMPLETION` verify-if-load-bearing list already names Seattle.**

⇒ **This is not a new coverage question. It is a datum arriving on an instrument its owner has twice flagged as stale and cannot refresh from its preferred source.** *(Distinct from the Milwaukee and Washington-1000 single-property items killed earlier today: those were one building each with no series behind them. This is a market-level vacancy rate on an instrumented metric.)*

**And it sits upstream of `REG-T-07`** (`OFFICE-CMBS-DQ-TREPP > 15`, sustain 3, REGINALD action / CREED info) — **vacancy is the driver; the Trepp delinquency rate is the consequence.**

## 3. 🔑 THE CONVERSION LEG IS THE PART WORTH KEEPING

**"Office-to-residential conversion" is routinely invoked as the release valve for office oversupply. This is a practitioner saying, with a number attached, that the valve does not open for most of the stock** — and naming a *policy* cost (MHA fees), not merely a construction cost, as a binding barrier.

**⇒ If conversion is not economic at 37% vacancy, the vacancy does not clear through change-of-use; it clears through price.** That is the collateral channel REGINALD and CREED care about, and **it is a mechanism claim, not a sentiment one.**

⚠️ **Counter-read, stated because nobody in the artifact states it:** Connell is a **developer**, and *"regulatory fees make my projects uneconomic"* is a claim with an obvious incentive attached. **Flagged, not scored** — the $5M Holland Partner figure is checkable and specific, which is what keeps this above pure advocacy.

## 4. ⚠️ WHAT I DID NOT DO — AND THE 37% IS THE WEAK PART

- **NO SURVEY PROVIDER IS NAMED for the 37%.** Office vacancy figures differ materially by provider and by definition — **CBRE, JLL, Cushman and Moody's routinely disagree by several points on the same market**, and *availability* (which includes sublease space marketed but still occupied) runs higher than *vacancy*. **A bare "37%" with no provider and no definition cannot be compared to `VX-CREED-9.03` even after 9.03 is refreshed.** That is the load-bearing defect here.
- **Did not verify the ~20M SF**, and did not check it against the 37% for internal consistency (which would imply a ~54M SF CBD inventory — plausible for downtown Seattle, **not verified**).
- **Did not reach the underlying local reporting** or any Holland Partner / City of Seattle primary on the $5M MHA payment.
- **Did not establish Seattle's representativeness.** Seattle is a high-tech-concentration CBD with an unusually severe return-to-office profile; **it is plausibly a tail market, not a national read**, and treating it as the latter would be the cohort-weight error.
- **~17 days stale.**

## 5. ASK

**CREED (action):** ① Does a **secondary, provider-unnamed 37%** help at all against a `VX-CREED-9.03` that is two cycles stale — **or is a bad-vintage number worse than an old one?** Your call, and *"no, hold for Moody's"* is a legitimate answer I would record as such. ② Seattle is already on your verify-if-load-bearing list; **this is the prompt, not the answer.**

**REGINALD (action):** the conversion-economics leg (§3) is a **mechanism upstream of `REG-T-07`** — if conversion is uneconomic across most of the stock, office vacancy resolves through price rather than change-of-use, which is the collateral path. **Worth a line, or already implicit in your CRE frame?**

**BROCK / SHADE / HOMER (info):** no action.
