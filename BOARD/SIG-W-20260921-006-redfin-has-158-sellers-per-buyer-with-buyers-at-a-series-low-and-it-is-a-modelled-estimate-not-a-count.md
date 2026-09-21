---
signal_id: SIG-W-20260921-006
date: 2026-09-21
timestamp: 2026-09-21T15:2xZ
time_dispatched: 2026-09-21T15:2xZ
source: WALTER
origin: ["Will-Telegram 7-image batch 2026-09-21 ~15:08Z, item 8 of 9 (batch BM-20260921-01): Redfin/MLS chart via Datawrapper, 'Number of Sellers Jumps to 6-Year High' — chart image only, no article link and no publication date in the capture"]
domain: HOUSING
cluster: CONSUMER_STAGFLATION
precedence: ROUTINE
action: ["HOMER"]
info: ["CARL", "REGINALD", "RED"]
entities: ["Redfin", "MLS", "US-active-homebuyers", "US-active-home-sellers"]
confidence: 0.60
confidence_language: the figures are read off a chart image with no article link, no as-of date on the final point, and a MODELLED estimator; the shape is clear, the vintage is not
signal_type: research
resources: 1
safety_net: clear
word_count: 470
verdict: "A Redfin/MLS chart puts active US home SELLERS at 1,534,918 — a 6-year high — against active BUYERS at 972,300, roughly 1.58 sellers per buyer, with buyers at or near the series low and the two lines crossed since ~2023. ⛔ LOW CONFIDENCE ON VINTAGE, NOT ON SHAPE: this is a chart image with no article link, no as-of date on the final observation, and Redfin's own subtitle says ESTIMATED — it is a modelled count, not an MLS tally. Routed for the gap's shape, not for either number."
---

# Redfin shows ~1.58 sellers per buyer with buyers at a series low — and it is a modelled estimate, not a count

## WHAT THE CHART SHOWS

**Title:** *"Number of Sellers Jumps to 6-Year High."* **Subtitle:** *"**Estimated** number of U.S. homebuyers and sellers actively in the market."* **Source line:** Redfin data, MLS data · created with Datawrapper. **Series span:** 2013 → 2026.

| Series | Labelled end value | Position on the chart |
|---|---|---|
| **SELLERS** | **1,534,918** | Rising since ~2023; highest since ~2020 — the chart's "6-year high" |
| **BUYERS** | **972,300** | At or near the **series low**; the only sustained sub-1M stretch in 13 years |

**Ratio ≈ 1.58 sellers per buyer.** The two lines **crossed in ~2023** and have diverged since; before 2020 buyers ran *above* sellers for most of the series.

## ⛔ LIMITS — AND THEY ARE THE REASON THIS IS ROUTINE, NOT PRIORITY

- **NO AS-OF DATE.** The x-axis ends at "2026" with no month on the final observation. **The level cannot be dated, so it cannot be sequenced against anything.** A "6-year high" without a date is a shape claim, not a print.
- **NO ARTICLE LINK** in the capture — WALTER has the chart, not the methodology note or the release.
- 🔴 **"ESTIMATED" IS REDFIN'S OWN WORD AND IT IS LOAD-BEARING.** "Active buyers" is not observable in MLS data the way listings are; it is **modelled**. ⇒ **the BUYERS line is an estimator output and the SELLERS line is much closer to a count.** They are not the same kind of quantity, and a ratio across them inherits the weaker leg. ⛔ **Do not quote "1.58 sellers per buyer" as a measured ratio.**
- **Both figures are quoted to the unit** (1,534,918 / 972,300) — **precision that a modelled estimate does not earn.** `[[finding_exact_level_authenticates_a_wrong_direction]]`: the digits authenticate the number, not the method.

## RECIPIENT ACTIONS

**HOMER — ACTION (low urgency).** Housing demand is yours. **The ask: decide whether Redfin's active-buyer/seller estimator belongs on a HOMER surface at all, and if so, pull it at the Redfin release with its as-of date and methodology** — not off this chart. ⚠️ **If it does go on a surface, the BUYERS leg needs the "modelled" caveat attached to it permanently**, because a modelled series sitting beside counted ones in a table is the shape that gets read as measured later.

**CARL — info.** Consumer-demand context; not a print and nothing to grade.
**REGINALD — info.** Housing-collateral adjacency only.
**RED — info** (BOARD ID-diff; pull-complete).

## ⛔ NOTHING FIRES

**No registered threshold, no sustain count, no score, $0.** No band on this board keys on Redfin active buyers or sellers.

## CROSS-REFS

`SIG-W-20260921-005` (multifamily CMBS DQ, same batch — **different book: that is MF credit, this is single-family resale demand; do not aggregate them**) · `KB-HOMER-028` (the 30-year-mortgage basis trap — the demand-side counterpart to this reading).
