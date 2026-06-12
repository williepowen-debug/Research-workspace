# BDC Mark Convergence Monitor

**Purpose:** Track whether public BDC marks catch down to the divergence signaled by TCW's Red Lobster 98% equity / 100¢ debt writedown. This is the specific transmission mechanism between private credit mark-to-model fiction and public-market price discovery.
**Built:** 2026-04-16 | **Light-populated:** 2026-06-12 (Q1 NAVs from public prints, sourced per-cell; FV/Cost + PIK% deferred to a 10-Q pass) | **Trigger for full activation:** any 2 signals below cross threshold — **see Trigger status table: div-cut trigger FIRED; activation conditionally met pending FV/Cost verification**

---

## Why this monitor exists

TCW Private Credit Fund writing Red Lobster equity to 2¢ while keeping the corresponding 2029-maturity loan marked at par (Apr 14, Bloomberg) is the canonical Stage 3 precursor — not Stage 3 itself. The mechanism:

1. Equity goes to zero quietly (fund manager write, one line item)
2. Loan stays at par because "PIK'ing, no covenant breach, no marking event"
3. Eventually: redemption pressure / audit / secondary sale forces the loan to mark down
4. Once marked down in one fund, reference pricing forces mark-downs across other holders
5. Public BDCs (mark to daily NAV) hit first → their prices / dividends / NAV move
6. That's the transmission event public markets have to reprice

**Watching for:** Step 5. The public tell.

**Key tension:** My Apr 16 STATUS reads "PC Stage 3 decelerating" based on APO +15.9% / BIZD +4.9%. But those are public equity price action — they can keep bouncing even while private marks diverge. This monitor is the check on my own narrative.

---

## Candidate BDCs to track

Criteria: (a) public daily mark, (b) meaningful PC loan book, (c) liquid enough that NAV/price dislocations are visible.

| Ticker | Manager | Size ($B AUM) | Why track |
|--------|---------|--------------|-----------|
| **ARCC** | Ares Capital | ~25 | Largest public BDC; reference for sector sentiment |
| **BXSL** | Blackstone Private Credit | ~13 | Directly parent-linked to BCRED (non-traded; Q2 gate test is Proposal 5) |
| **OBDC** | Blue Owl / OBDC | ~14 | Owner group's other vehicles (OCIC, OTIC) have already gated Apr 2 |
| **MAIN** | Main Street Capital | ~5 | Smaller, higher-quality book; behaves as a "clean" benchmark |
| **FSK** | FS KKR | ~14 | Mid-market workout-heavy book; historically first to mark down when cycle turns |

**Note:** I do NOT know which of these (if any) holds Red Lobster paper. That's a specific 10-Q deep-dive that isn't done here. What I'm tracking is the **sector-level mark behavior**, not the specific position.

## Data fields per BDC (quarterly + price-action)

Per-quarter (from 10-Q / earnings):
- NAV per share
- NAV change QoQ
- Portfolio fair-value ratio (total investments at FV / at cost) — **this is the mark signal**
- Non-accrual % (by fair value)
- PIK income as % of total investment income
- Top 10 holdings and their fair-value/cost ratios (look for 70–90% marks)

Daily (price-action):
- Close price
- Price-to-NAV (or last-reported NAV)
- Dividend yield
- Volume

Cross-sector derivatives:
- **BIZD** (BDC ETF) — on my main dashboard already; sector-level sentiment
- Non-traded BDC redemption prints (BCRED, Ares, Apollo, Golub) — stagger release schedule

## Baseline (light populate 6/12 — Q1 2026, NAVs as of 3/31/26; prices = 6/11 raw closes per basis canon)

| Ticker | Price (6/11) | NAV (3/31) | P/NAV | NAV Δ QoQ | FV/Cost | Non-accrual % | PIK % |
|--------|-------|-----|-------|-----------|---------|---------------|-------|
| ARCC | 19.07 | **19.59** (8-K/10-Q) | 0.97 | prior-Q not pulled — pending | 10-Q deferred | deferred | deferred |
| BXSL | 23.90 | **26.26** (8-K/earnings pres.) | 0.91 | **DECLINE** (per Q1 slides headline; magnitude pending) | deferred | deferred | deferred |
| OBDC | 11.17 | **NOT FOUND** — searches surfaced Onex Direct Lending ($18.75), which is NOT Blue Owl; do not transcribe | — | pending | deferred | deferred | deferred |
| MAIN | 51.74 | **33.46** (8-K: +0.13, **+0.4% QoQ** from 33.33) | 1.55 | **+0.4% — clean benchmark holding** | deferred | deferred | deferred |
| FSK | 10.82 | **20.89** (trade press; cross-corroborates BROCK's verified **-9.9% QoQ**) | **0.52 ⚠️** | **-9.9%** | deferred | deferred | deferred |

- **⚠️ FSK P/NAV 0.52 is an extreme print** — verify no split/NAV-vintage mismatch before citing as a distress signal; if real, it's the loudest mark-vs-price divergence on the board.
- **Sector datapoint (not in the five):** GSBD NAV $12.17 vs $12.64 (**-3.7% QoQ**, NII -$0.12/sh) — second confirmed NAV decliner.
- BIZD 12.62 (6/11 close); 2-week trend up, not down — no 🔴 conjunction.

*Deep fields (FV/Cost ratio, non-accrual %, PIK %) need the 10-Qs — deferred to a full-populate pass if the BCRED Q2 window or a trigger escalation warrants it.*

## Trigger thresholds (status column added 6/12)

| Signal | What it means | Priority | Status 6/12 |
|--------|--------------|----------|-------------|
| Any BDC reports **FV/Cost <95%** AND **QoQ NAV drop >2%** | Mark convergence started | 🟡 | **NAV leg met ×2** (FSK -9.9%, GSBD -3.7%); FV/Cost leg unverified (10-Q deferred) — conditionally met |
| **Two BDCs** report FV/Cost dropping QoQ by >1pt in same quarter | Sector-wide mark reset | 🟠 | Unknown — FV/Cost deferred |
| Any BDC **cuts regular dividend** or converts to "supplemental only" | Income model breaking | 🟠 | **FIRED (recorded late — cuts landed May–early-June):** MFIC, OCSL, OBDC regular-div cuts (BROCK 6/8 read) + FSK cut (trade press 6/12 confirm). **Four cutters, not one.** |
| Non-accrual % jumps >150bps QoQ on any BDC | Specific-portfolio stress | 🟠 | Unknown — deferred |
| **Simultaneous** FV/Cost drop across 3+ BDCs AND BIZD down >8% in 2 weeks | Stage 3 transmission event | 🔴 | Not met — BIZD trend is UP (12.45→12.71 over the week) |

> **Activation read (6/12):** the monitor's "any 2 signals" full-activation test is **conditionally met** — the 🟠 div-cut trigger has unambiguously fired (×4), and the 🟡 NAV leg is met twice with only the FV/Cost confirmation outstanding. The *tension this monitor was built to catch is live*: NAV marks and dividends deteriorating while BDC equity prices bounce (BIZD up, APO >$130 ×3 closes). Matches BROCK's Stage 2→3 pivot. Full 10-Q populate is the escalation step if BCRED Q2 gates.

## Known information gaps

1. **Red Lobster specific holders:** Not mapped. Would require searching BDC 10-Q schedule of investments for "Red Lobster" or its restructured entity name (post-Ch11 it's a Golden Gate / Fortress subsidiary; exact debtor entity name requires SEC filing lookup). Deferred to a follow-up session if needed.
2. **Non-traded BDC marks:** BCRED, Apollo Debt Solutions, Blackstone's non-traded vehicles — these report quarterly with lag. They're where the biggest mark-model fiction is, but I can't monitor them continuously. The public-BDC monitor is the visible early signal; non-traded is where the real Stage 3 breaks.
3. **Cross-holder PIK chains:** If one BDC holds a loan at 100¢ that another marks at 85¢ in the same quarter, that's a loud bell. Would need to cross-reference specific CUSIPs across 10-Qs — worthwhile if a specific loan becomes a focal point.

## Schedule

- **Weekly:** BIZD price, top-5 BDC closes, any dividend/earnings events
- **Post-earnings season (mid-May):** Pull Q1 10-Q data for the 5 BDCs; update baseline table
- **Ad hoc:** If any BDC pre-announces, declares special charge, or gate/redemption event at sister non-traded vehicle

## Relationship to other LIQUID signals

- **Feeds into:** Credit dashboard (HY OAS trigger) — if BDC marks diverge while HY OAS stays tight, confirms the "public-equity-sentiment-vs-underlying-marks" disconnect in my STATUS thesis.
- **Cross-agent:** BROCK owns the non-traded PC side; my monitor is the public reflection. Share findings via outbox signal if Stage 3 trigger fires.
- **Does NOT replace:** BROCK's direct PC tracking. This is the LIQUID-domain reflection (public plumbing), not the upstream cause.

---

*Monitor is a scaffold — values populated as earnings print. First refresh target: Q1 2026 earnings cycle (mid-May through early-June 2026).*
