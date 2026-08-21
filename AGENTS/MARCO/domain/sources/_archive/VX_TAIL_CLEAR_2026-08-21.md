# MARCO — VX stale-tail clear, 2026-08-21 (session 22)

Full detail for the six rows worked to zero. STATUS carries the summary; this file carries the evidence.

### 🔧 8/21 LATE — THE WHOLE VX STALE TAIL WORKED TO ZERO, AND NOT ONE ROW WAS MERELY OLD
**`VX.tsv` >60d: 12 → 6, and all six survivors are stale-BY-DESIGN.** The "other" bucket is **empty for the first time**; loaded-status stale is **0**. Content clock **+212d → +51d**. **The clock moved because the tail was worked, not because a stamp was edited.**

| Row | Was | What was actually wrong |
|---|---|---|
| `TX-01` | 211d | **Narrative REVERSED** — "inventory growth ~2x the GFC build-up" is now **−2.46% YoY**; carried "18,146 listings" **off by ~7.6×** |
| `AZ-01` | 211d | **Band untrippable** — ">30% decline" names no instrument; sell-off leg measured and **not firing** |
| `TAX-01` | 178d | **Name/metric mismatch** + a **fabricated decline** caught (below) |
| `H2A-02` | 82d | **Narrative → measurement** (below) |
| `ENF-01` | 151d | **Low-information vector** — its breach leg is now structurally unlikely to fire |
| `APT-01` | 67d | **Source route DEAD** (below) |

🔴 **`TAX-01` — I nearly shipped a decline that does not exist.** The NV Gaming Control Board's latest report headlines percentage-fee collections at **−6.99% YoY** — but its own footnote says collections are **"through July 21"** while the prior-year figure is a **FULL month**. A partial month against a full month is not a comparison, and −6.99% would have pushed this row out of its own ±5% NORMAL band **on a truncation artifact**. **Not adopted.** The latest *comparable* full-month read is **+19.07%**. Also: the row is titled "tourism **TAX** receipts" and had only ever carried gaming **WIN** — two different quantities; both legs now carried. Gaming win: Strip **−1.39%** month but **+1.96% FY26**; statewide +0.82% / +2.59% FY. ⇒ **ELEVATED → NORMAL.**

🔧 **`H2A-02` — stopped being a narrative and became a measurement.** `RECEIVED_DATE` / `EMPLOYMENT_BEGIN_DATE` were in the OFLC file all along and had never been used. DOL processing lag is **improving** (Q3 median **19d** vs Q1 26d / Q2 28d). The **missed-planting-cycle rate — which is literally what the BREACHED band asks — is now measured directly**: Q1 **17.11% of workers** (the damaged quarter), Q2 2.49%, Q3 3.82%; FY26 3.97% of cases / 5.46% of workers. ⚠️ **Counterweight: median lead time is only 32 days and 38.53% are certified with <30 days of margin** — fast on average, **fragile in the tail**. ⚠️ **DOL leg ONLY — the consular visa gate is not visible in this file and stays UNKNOWN, not benign.** ⚙️ **Wired into `tools/h2a_pull.py`, so it now refreshes every quarter at boot** and reproduces the hand computation to the digit.

🔴 **`APT-01` — MIA printed NEGATIVE in the World Cup month, and the FLL route is dead.** MIA June (Miami-Dade Aviation PDF, own pull): **total −1.43% YoY**, intl −1.66%, dom −1.23%, CYTD −0.62%. **MARCO's standing caveat was the opposite risk** — *"MIA pax may print +YoY on the WC; that's an event-mask, not recovery."* **The desk was braced for a false positive and got a negative.** The most WC-exposed US airport (7 matches, Bronze Final) could not clear zero during the tournament ⇒ **hardens ES-MARCO-09's FAIL read.** Meanwhile **`broward.org` was rebuilt as a Next.js SPA**: the documented FLL route returns an app shell with zero PDF links and the legacy document tree 404s across all 7 tested months, **while search engines still index the old URLs** — so a link-level check looks fine until you fetch. **Same class as the hardcoded-filename rot that killed the H-2A puller for 101 days.** Source map corrected; **BTS T-100 would close FLL and MCO in one pull.**

