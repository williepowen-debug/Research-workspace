# MARCO — VX stale-tail clear, 2026-08-21 (session 22)

Full detail for the six rows worked to zero. STATUS carries the summary; this file carries the evidence.

### 🔧 8/21 LATE — THE WHOLE VX STALE TAIL WORKED TO ZERO, AND NOT ONE ROW WAS MERELY OLD
**`VX.tsv` >60d: 12 → 6, and all six survivors are stale-BY-DESIGN.** The "other" bucket is **empty for the first time**; loaded-status stale is **0**. Content clock **+212d → +51d**. **The clock moved because the tail was worked, not because a stamp was edited.**

| Row | Was | What was actually wrong |
|---|---|---|
| `TX-01` | 211d | **Narrative REVERSED** — "inventory growth ~2x the GFC build-up" is now **−2.46% YoY**; carried "18,146 listings" **off by ~7.6×** |
| `AZ-01` | 211d | **Band untrippable** — ">30% decline" names no instrument; sell-off leg measured and **not firing** |
| `TAX-01` | 178d | **Name/metric mismatch** (titled *tax*, carried *win*) + a single-month print misread as a trend — ⚠️ **and my own first correction of it was ALSO wrong; see the withdrawal below** |
| `H2A-02` | 82d | **Narrative → measurement** (below) |
| `ENF-01` | 151d | **Low-information vector** — its breach leg is now structurally unlikely to fire |
| `APT-01` | 67d | **Source route DEAD** (below) |

⚠️ **`TAX-01` — CORRECTED ON REVIEW, SAME SESSION. My original entry here was wrong and is preserved-then-withdrawn.**

> *Original claim (WITHDRAWN):* "The NV Gaming Control Board's latest report headlines percentage-fee collections at −6.99% YoY — but its own footnote says collections are 'through July 21' while the prior-year figure is a FULL month… Not adopted."

**Why it was wrong:** I reasoned from a footnote on ONE side and never tested whether the same convention applies to the comparison basis. **It does.** The prior month's report carries the identical footnote (*"Percentage fee collections are through June 23, 2026"*), so truncation is a standing convention, not an asymmetry. And the decisive test: across FY26's twelve monthly YoY prints the **mean is +7.09% with 6 of 12 negative** — a one-sided truncation would have produced a systematic NEGATIVE skew, and there isn't one. **The −6.99% is a real reported figure.**

**The correct finding, which is stronger than the one I replaced it with:** monthly percentage-fee YoY in this series is extremely volatile — FY26 prints were **+25.98 / −0.74 / +33.80 / −12.35 / +5.02 / −5.39 / −2.24 / −7.08 / −3.01 / +17.11 / +14.85 / +19.07**, **σ = 14.04pp**. **July's −6.99% is a −1.0σ move, and 2 of 12 FY26 months were at least as negative. A single month at −7% carries no signal in this series.** FY26 total collections **$1,036,360,554 vs $986,388,787 = +5.07%**.

⇒ **ELEVATED → NORMAL still stands, but on BASE-RATE grounds, not on an artifact.** Note the carried Dec-2025 read ("Oct +8.21, Nov −0.56, Dec −6.07 = clear deterioration") was **the same error mirrored** — three monthly prints called a trend in a 14pp-σ series.

**Caveats that DO survive:** the July figure is explicitly "through July 21" and "subject to revision", and collections exclude $1,829,717 of transferable tax credits taken FYTD — so treat any single month as provisional. And the **name/metric mismatch is unaffected**: the row is titled "tourism TAX receipts" and had only ever carried gaming WIN. Gaming win June: Strip **−1.39%** month, **+1.96% FY26**; statewide +0.82% / +2.59% FY.

**Lesson:** *a footnote naming a limitation on one side does not establish asymmetry — check whether the same convention governs the comparison basis before calling a published figure an artifact.*

🔧 **`H2A-02` — stopped being a narrative and became a measurement.** `RECEIVED_DATE` / `EMPLOYMENT_BEGIN_DATE` were in the OFLC file all along and had never been used. DOL processing lag is **improving** (Q3 median **19d** vs Q1 26d / Q2 28d). The **missed-planting-cycle rate — which is literally what the BREACHED band asks — is now measured directly**: Q1 **17.11% of workers** (the damaged quarter), Q2 2.49%, Q3 3.82%; FY26 3.97% of cases / 5.46% of workers. ⚠️ **Counterweight: median lead time is only 32 days and 38.53% are certified with <30 days of margin** — fast on average, **fragile in the tail**. ⚠️ **DOL leg ONLY — the consular visa gate is not visible in this file and stays UNKNOWN, not benign.** ⚙️ **Wired into `tools/h2a_pull.py`, so it now refreshes every quarter at boot** and reproduces the hand computation to the digit.

🔴 **`APT-01` — MIA printed NEGATIVE in the World Cup month, and the FLL route is dead.** MIA June (Miami-Dade Aviation PDF, own pull): **total −1.43% YoY**, intl −1.66%, dom −1.23%, CYTD −0.62%. **MARCO's standing caveat was the opposite risk** — *"MIA pax may print +YoY on the WC; that's an event-mask, not recovery."* **The desk was braced for a false positive and got a negative.** The most WC-exposed US airport (7 matches, Bronze Final) could not clear zero during the tournament ⇒ **hardens ES-MARCO-09's FAIL read.** Meanwhile **`broward.org` was rebuilt as a Next.js SPA**: the documented FLL route returns an app shell with zero PDF links and the legacy document tree 404s across all 7 tested months, **while search engines still index the old URLs** — so a link-level check looks fine until you fetch. **Same class as the hardcoded-filename rot that killed the H-2A puller for 101 days.** Source map corrected; **BTS T-100 would close FLL and MCO in one pull.**

