---
id: SIG-W-20260511-043
date: 2026-05-11
origin: WALTER image-batch 2026-05-11 — @FirstSquawk X-post (5/11 9:37 AM, 114K views) citing CNBC; verify-research recovered NY Fed Q4 2025 + FRED DRCCLACBS primaries
domain: CONSUMER_CREDIT
cluster: CONSUMER_STAGFLATION
cluster_secondary: BANK_COLLATERAL
signal_type: thesis-frame
precedence: PRIORITY
confidence: 0.55
to: CARL
info: [REGINALD, RED, OTTO, BROCK, LIQUID]
signal_role: standalone
event_window: closed
verify_research_verdict: CORRECTED-FRAMING
---

# First Squawk Citing CNBC: Auto+CC Delinq "All-Time Highs" — Verified CORRECTED-FRAMING: Record Balances + Record Subprime ≠ Record System-Wide Rates

**Verbatim claim (X-source):** @FirstSquawk (5/11/2026 9:37 AM): *"AUTO LOAN AND CREDIT CARD DELINQUENCIES IN THE US HAVE HIT ALL-TIME HIGHS, ACCORDING TO CNBC"*

**Verified against primary Fed data:**

**Auto loan 90+ day serious delinquency (NY Fed HHDC Q4 2025, released 2/10/2026):**
- 5.2% Q4 2025 = **highest since 2010 (5.3% peak)** — elevated, near-2010-peak, NOT all-time high
- Total household debt $18.8T; aggregate delinquency 4.8% (+0.3pp QoQ)

**Credit card commercial-bank delinquency rate (FRED DRCCLACBS, Q4 2025):**
- **2.94%** — 6th straight quarterly decrease
- All-time peak = **6.77% April 2009** — current rate **less than half** of all-time high

**What IS at record (cohort-specific or balance-level):**
- Subprime-auto 60-day delinq **6.9%** (Fitch, Jan 2026) — narrow subprime cohort
- Auto debt **$1.68T** nominal balance (record dollar level, per SIG-W-20260509-002)
- Average new-car payment **$773** (record)
- 84-month loans **22.9%** share of auto originations (record)

**Source primaries:**
- NY Fed Q4 2025 HHDC release (2/10/2026) — https://www.newyorkfed.org/newsevents/news/research/2026/20260210
- FRED DRCCLACBS — https://fred.stlouisfed.org/series/DRCCLACBS
- Fed Note 11/24/2025 — Consumer Delinquency Dynamics — https://www.federalreserve.gov/econres/notes/feds-notes/a-note-on-recent-dynamics-of-consumer-delinquency-rates-20251124.html
- Bankrate (auto delinq 15-year high context) — https://www.bankrate.com/loans/auto-loan-delinquencies-hit-15-year-high/
- Fortune (5/7/2026, $1.68T auto debt + subprime context) — https://fortune.com/2026/05/07/americans-auto-loan-debt-crisis/
- First Squawk X post — https://x.com/FirstSquawk/status/2053831846979662252

## Substance

- **CNBC primary article UNLOCATED** — possibly the older CNBC Select "Credit Card Delinquency Is at a Record High" piece (pre-2026, loose framing) or the 2/10/26 CNBC piece on NY Fed Q4 2025 $1.28T CC balances. First Squawk likely paraphrased loosely. INDETERMINATE on exact CNBC source.
- **The framing conflation pattern** = same family as 4/20 "% of 2009" lessons: First Squawk conflates (a) record-nominal-dollar balances + record-subprime-cohort rates with (b) system-wide-record-delinquency-rates. (b) is false; (a) is true-but-trivial (balances trend up with nominal economy).
- **Bear thesis directionally CORRECT** — consumer-credit stress is real, accumulating, elevated. Subprime-auto at 15-year high IS substantive. But "all-time high" reads as Great-Depression-level systemic risk, which the system-wide rates don't support.

## Dispatch notes

**Confidence 0.55** — directional thesis (consumer-credit stress elevated, near-post-GFC highs) CONFIRMED; "all-time high" headline claim CORRECTED-FRAMING (system rates remain below 2009 peaks).

**vs prior WALTER signals:**
- SIG-W-20260424-007 NY Fed Q4 2025 CC 90-day transition 12.7% (transitioning into delinquency, approaching 2009 peak — not exceeded) — that 12.7% is the **transition-rate-into-delinquency** metric, NOT stock delinquency rate. Different metric, near-peak-but-not-exceeded.
- SIG-W-20260509-002 Auto loan debt $1.68T (level not rate) — re-affirmed by Fortune 5/7 piece.

**REGINALD/BROCK relevance:** subprime-auto 60-day at 6.9% Fitch + 22.9% 84-month loan share = ABS market stress vector (OTTO domain). REGINALD watch for bank CC + auto loan portfolio quality. BROCK watch for PC/BDC consumer-credit exposure.

**Standalone signal_role** — NOT cluster_mediating; framing-correction on broad-cluster claim. CORRECTED-FRAMING auto-cc RED per By-Tag rule.

**Calibration register:** 4th CORRECTED-FRAMING dispatch this image-batch session (FANG / Tulsa / SPR / now this) + 2 from Trump-IRIB framing-paraphrase + Kalshi sub-CORRECTED-FRAMING. CORRECTED-FRAMING is the dominant verdict-class this batch (extends 4/25 finding "CORRECTED-FRAMING becoming dominant verdict").

## Recipient routing

- **CARL action** — consumer-credit transmission primary (CONSUMER_CREDIT default per routing-table v0.4).
- **REGINALD info** — bank CC + auto loan portfolio quality cross-feed; subprime-auto-ABS bank-exposure tier.
- **RED info** — CORRECTED-FRAMING auto-cc per By-Tag rule.
- **OTTO info** — subprime-auto-ABS primary; 6.9% Fitch 60-day delinq + 22.9% 84-mo loan share = OTTO-domain core.
- **BROCK info** — PC/BDC consumer-credit exposure (some BDCs hold subprime-auto-ABS).
- **LIQUID info** — credit-spread context if ABS market deterioration accelerates.
