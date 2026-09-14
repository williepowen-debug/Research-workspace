---
signal_id: SIG-W-20260914-020
date: 2026-09-14
timestamp: 2026-09-14T18:05:47Z
time_dispatched: 2026-09-14T18:05:47Z
source: WALTER
origin: "Will desktop drop-zone inbox/WILL/IMG_2321.JPG + IMG_2320.JPG (batch BM-20260914-02 items 43 and 45) — two Google Trends captures, 2026-09-06. NOTE THE GEOGRAPHIES DIFFER and are NOT merged here."
domain: HOUSING
cluster: CONSUMER_STAGFLATION
precedence: ROUTINE
action: ["HOMER"]
info: ["CORAL", "CARL", "MARCO", "REGINALD", "RED", "TERRY", "PROME", "BOND"]
entities: ["Google-Trends", "US-housing", "mortgage-distress"]
confidence: 0.45
confidence_language: the-CHARTS-are-what-they-are-but-Google-Trends-is-a-RELATIVE-normalised-index-with-a-known-baseline-drift-problem-and-WALTER-did-NOT-pull-them-itself
signal_type: data
resources: 1
safety_net: clear
word_count: 400
verdict: "Two Google Trends series on household housing distress. 'Help with mortgage' (UNITED STATES, 2004-present) is at 100 -- its all-time high -- against a 2008-09 GFC peak of roughly 52. 'Can't sell house' (WORLDWIDE, 2004-present) is also at 100, up from ~37 in 2022, with the final segment DOTTED, which in Google Trends means partial or incomplete data. ⛔ THESE ARE ROUTED AT ROUTINE WITH LOW CONFIDENCE AND THE CAVEAT IS NOT DECORATION: Google Trends is a RELATIVE index normalised so the window maximum equals 100, so '2x the GFC peak' is a statement about SEARCH SHARE, not about how many households are in distress -- and general search volume has grown enormously since 2004, which mechanically inflates later periods against 2008. ⚠️ THE TWO CHARTS ALSO HAVE DIFFERENT GEOGRAPHIES, US versus WORLDWIDE, and must not be read as one series. What survives the caveats is a direction, not a magnitude."
---

# "Help with mortgage" searches are at an all-time high, roughly double the 2008 peak — with the methodology caveat attached

## The two series, kept separate

| Query | Geography | Shape |
|---|---|---|
| **"help with mortgage"** | **UNITED STATES** | ~10 (2004) → **~52 at the 2008–09 peak** → ~22–25 flat 2013–2021 → rising from ~2022 → **100 now (window max)** |
| **"can't sell house"** | 🔴 **WORLDWIDE** | ~0 until ~2019 → ~20 (2021) → ~37 (2022) → **100 now**, final segment **DOTTED** |

⛔ **DIFFERENT GEOGRAPHIES. They are NOT one story and I have not merged them.** ⚠️ **The dotted tail on the second chart is Google Trends' marker for PARTIAL/INCOMPLETE data — the final point is not yet a settled observation.**

## ⛔ Why the confidence is 0.45 and not higher

🔑 **Google Trends is a RELATIVE index: the window maximum is defined as 100.** **So "double the GFC peak" means the query's SHARE OF SEARCHES is double — not that twice as many households are in trouble.**
⚠️ **And there is a known directional bias: total search volume has grown enormously since 2004, and more of life is searched now than in 2008.** **That mechanically inflates recent periods against the GFC benchmark.** ⛔ **Anyone citing "2× the 2008 peak" as a distress magnitude is over-reading it, and that is exactly how this chart will travel.**

✅ **What survives the caveats: a DIRECTION.** **Both series are at their window maximum, both inflected around 2022, and neither has rolled over.** **That is consistent with — not evidence for — household housing stress.**

## Why it is routed at all

**It pairs with today's `SIG-W-20260914-008`:** a claim that mortgage rates are **back above 7%** against our own `MORTGAGE30US` **6.76%**, which I routed to HOMER as a series-basis question. **With the 10Y at ~5.00% and mortgage rates at or near 7%, a rise in household-distress search behaviour is the mechanism you would expect to see, and HOMER is the desk that can say whether harder data corroborates it.**

⚠️ **This is a SOFT indicator being routed BECAUSE a hard question is already open, not on its own merits.**

## Requested action

- **HOMER** — `ROUTINE`, no clock. **(a) Do you track any hard household-distress series** — delinquencies, forbearance requests, foreclosure filings — **that would corroborate or refute this direction?** **(b) Is Google Trends of any use to you at all, or is the normalisation problem disqualifying?** ⛔ **A clean "not useful" is a fine answer and I would rather have it than a forced read.**
- **CORAL** on `info:` — **Florida is a top-priority geography and the US series bears on it**, alongside the enrollment/affordability thread you already carry.
- **CARL** on `info:` — household balance-sheet stress, alongside the credit-card chart note sent earlier today.

⛔ **NOT ASSERTED:** any distress magnitude; that searches measure households; that either series is comparable to 2008. **ESTABLISHED:** the two charts show what is described above, at the stated geographies.
