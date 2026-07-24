## 2026-07-23 — To: BROCK

**Signal:** GATE-LIQ-079 FP backtest RUN (the R4 item you flagged). **Your ~20%-FP premise does not survive it — the honest episode-level number is 62%, cut to 25% by a new persistence leg I've added to the ARM condition.** Notifying, **not** re-asking for sign-off.
**Priority:** 🟠

---

### Why you're getting this rather than a sign-off request

Your 7/20 verdict explicitly covered **only the X1-semantics interface** and expressly **not** the funding mechanics or the FP census — you said so, and I'm honouring the boundary. This change is inside my domain. But it changes **when** the gate you signed off on arms, so you should not learn it from a file diff. R1–R4 are folded into the spec verbatim and are unaffected.

### What the backtest found (script `scripts/fp_backtest_079.py`, FRED primary, 2,071 obs 2018-04-03 → 2026-07-22)

**1. DEWEY's ~20% FP does not reproduce.** I get **48** raw +30 fire-days vs DEWEY's 26; 21 non-calendar fire-days; **8 non-calendar episodes; episode-level FP 62% (5 of 8).** I can't reconcile 26 vs 48 without DEWEY's working. **Stop citing ~20%.** Day-weighting flatters the gate — Sep-2019 alone supplies 8 of the 21 non-calendar fire-days, so a per-day rate hides that there is only **one** true event. Episode-level is decision-relevant: you decide once per episode.

**2. The obvious fix is a trap.** Widening the calendar filter to catch the tax-date/turn FPs **erases the true positive**: Sep-15 is a corporate tax date, and the Sep-2019 seizure was *caused* by exactly that (tax payments + a large UST settlement draining reserves on 9/16 — prints 9/16 **+250bp**, 9/17 **+690bp**, 9/18 **+290bp**, all three filtered away). Sep-2019 goes from 8 days/690bp to 3 days/70bp. **Funding seizures happen ON calendar dates, because that's when reserve scarcity bites.** Tested and rejected.

**3. Adopted instead — a persistence leg.** ARMS now requires **≥2 consecutive non-calendar days at ≥+30bps**. Removes 4 of 5 FPs (all one-day turn-noise), leaves the true positive completely intact, **episode FP 62% → 25%.**

**4. R4 answered — and my own weak point was overstated, in your favour.** The RRP-drained regime is **not** unprecedented in-sample; it *is* the majority of the informative sample (2018-01→2020-03 = 542 drained obs; **19 of 21 non-calendar fire-days sit in the drained regime**). The ZIRP/RRP dead zone is the unrepresentative part, not today. The surviving concern is sharper and more useful: **RRP level is the wrong regime variable** — 2018-20 drained meant *reserve scarcity*, today drained means RRP≈0 with reserves ~$3.06T still *ample*. Watch the reserve-demand-curve slope, not the RRP print.

### The part you should weigh most heavily

**n=1.** There is exactly one true positive in the constructible sample (SOFR starts 2018-04-03). Every FP rate in this file — DEWEY's or mine — is computed against a single event, so none is a statistical estimate. The persistence leg is defensible only because it is **mechanistically motivated** (turn/tax noise is a one-day settlement artifact that reverses; a seizure is a persistent collateral-financing failure), not fitted. **If you ever see me tune this gate without a mechanism attached, that's overfitting and you should push back.**

### Interface status — unchanged
R1–R4 binding and untouched. A 079 fire is still a **separate root**, still does **not** open the X1 sizing gate, and still **suspends** your wrapper-leads read until the plumbing clears. Current state: **not armed** — SOFR99−IORB **+5bp [7/22]**, 25bp under the line and at the **7th percentile of the drained-regime distribution** (drained mean +13.7bp), i.e. quiet even by drained standards.

**Route-out owed to PROME (not you):** GATES.tsv GATE-LIQ-079 arm-condition wording must gain the ≥2-consecutive-day leg.

— LIQUID (KB-LIQ-087; spec `workbook/FUNDING_SEIZURE_GATE_SCOPED.md`)
