# Phase 2 Plan — 2024-11 → 2025-01 Cluster Analog Deep Dive

**Purpose:** Build a dated template of which leading indicators fired across the 2024-11-22 → 2025-01-22 → Feb/Mar 2025 VIX-52 window, so we have a real-time checklist to apply to our 2026-04-13 → 2026-06-15 window.

**Why this analog specifically:** It's the only back-to-back SKEW divergence cluster in the 19-year sample (episode #13 → #14 in KB-VIO-036 backtest). Our Mar 27 peak + Apr 13 fire has the tightest structural parallel to it (decay → second fire), and it's the episode that produced the 52.3 VIX peak — the tail scenario we care about most.

---

## Success criteria

Phase 2 succeeds if we can answer 5 questions with dated evidence:

1. **Between the first fire (2024-11-22) and second fire (2025-01-22): which indicators moved decisively, which stayed quiet?** (the "tells")
2. **In the ~30 days before the eventual VIX 52.3 peak: what were the final-approach signals?**
3. **How does credit (HY OAS) behave across the window — does it lead, coincide, or lag?** (tests thesis v3.1 regime-dependence)
4. **What, specifically, was the peak-day external trigger?** (news, data release, or positioning unwind)
5. **Which of those tells are currently present or absent in our April 2026 setup?** — a side-by-side translation table

**Non-goals:** We're not trying to explain every wiggle. We want the 3-5 leading indicators that had signal, not the 20 that were coincident.

---

## Data pulls needed

All series span **2024-10-01 → 2025-04-01** (covers 2 months before first fire, 2 months after VIX peak) with daily cadence unless noted.

### Vol complex (yfinance — existing tooling)
- `^VIX` — spot
- `^VIX3M` — 3-month
- `^VIX9D` — 9-day (intra-month stress marker)
- `^VVIX` — vol-of-vol
- `^SKEW` — tail pricing

### VIX futures (CBOE VX settlement — our vix_futures.py)
- M1, M2, M3 daily settlement (for full term structure, not just spot vs 3M)
- Compute M1/M2 contango-backwardation, roll yield

### Credit (FRED — CSV fetcher)
- `BAMLH0A0HYM2` — HY OAS (already fetched for Phase 1)
- `BAMLC0A0CM` — IG OAS (cross-sector widening filter)
- `BAMLH0A3HYC` — CCC OAS (lower-tier stress)

### Rates (FRED)
- `DGS2` — 2Y Treasury
- `DGS10` — 10Y Treasury
- Compute 10Y-2Y slope (yield curve filter per thesis)
- `DFII10` — 10Y TIPS (real yields)

### FX / cross-asset (yfinance)
- `DX-Y.NYB` — DXY
- `JPY=X` — USD/JPY (2024-05 analog → Aug 2024 yen unwind says this matters)
- `GC=F` — Gold (safe-haven rotation proxy)
- `^TNX` — 10Y yield (alternate to FRED daily)

### Equity (yfinance)
- `^GSPC` — SPX level
- `^NDX` — Nasdaq-100
- Compute 20d realized vol → compare to VIX (vol risk premium)

### Bond vol (yfinance if available; may need alternate)
- `^MOVE` — Treasury vol (independent stress confirmation)
- If MOVE not on yfinance, pull from FRED or skip with a note

### Positioning (CFTC COT — weekly)
- VIX futures commercials vs leveraged funds (aggregator or direct CFTC CSV)
- Lower priority — weekly cadence means limited intra-window signal

### Catalyst calendar (manual / hardcoded)
- FOMC meetings in window: 2024-11-07, 2024-12-18, 2025-01-29, 2025-03-19
- CPI release dates
- NFP release dates
- Any known news triggers on peak day (news search at VIX-52 date)

**FRED CSV URL template:** `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>&cosd=2024-10-01&coed=2025-04-01`

---

## Tools to build

### 1. `scripts/fred_fetch.py` (reusable)
Small Python module:
- `fetch_series(series_id, start, end) -> pd.DataFrame`
- Writes to `workbook/fred_cache/<series>_<dates>.csv` so we don't re-pull
- No API key required (uses public CSV endpoint)

### 2. `scripts/analog_pull.py` (one-shot)
Pulls everything above into a single aligned daily DataFrame. Writes to `research/analog_2024_cluster/daily.csv`. ~150 daily rows × ~20 columns.

### 3. `scripts/analog_timeline.py` (one-shot)
- Marks T0 (2024-11-22), T+60 (2025-01-22), T+peak (VIX-52 day to be identified)
- For each indicator, compute: level at each landmark, % change, first-difference
- Identify indicators that showed monotonic move T0 → T+peak vs those that only spiked at T+peak
- Output: markdown table `research/analog_2024_cluster/tells_table.md`

No fancy plotting — tables are enough.

---

## Analysis sequence

### Step A — Data acquisition (20 min)
1. Build `fred_fetch.py`
2. Pull all FRED series (3 credit, 3 rates) into cache
3. Pull yfinance series (vol complex, FX, equity) — existing tooling
4. Pull VIX futures via existing `vix_futures.py` for M1/M2/M3
5. Verify row counts, date alignment, no gaps

### Step B — Landmark identification (15 min)
1. Confirm T0 = 2024-11-22 (first SKEW divergence fire from KB-VIO-036)
2. Confirm T+60 = 2025-01-22 (second fire)
3. **Identify T+peak** — the day VIX hit 52.3 per KB-VIO-036 row #14. Need to pull raw series to confirm exact date
4. Mark FOMC dates, econ releases inside the window

### Step C — Tell identification (45 min)
For each indicator, classify:
- **Class 1 — Leading:** moved decisively BEFORE T0 or between T0 and T+60
- **Class 2 — Coincident:** moved at T+peak only
- **Class 3 — Lagging:** moved after T+peak
- **Class 4 — Silent:** no material move in window

Build the tells table with dates and magnitudes. Expected Class 1 candidates (to test): HY OAS, CCC OAS, MOVE, USD/JPY, VIX term structure.

### Step D — Peak-day reconstruction (30 min)
Identify the exact VIX-52 date, then:
- What happened in markets that day (intraday path)
- What news/catalyst hit (web search on the date — separate subagent)
- Was it external shock or positioning unwind?

Deliverable: 1-paragraph "what actually happened on T+peak" narrative.

### Step E — 2026 side-by-side translation (45 min)
Build a comparison table: for each Class 1 tell from 2024-11/2025-01, what does our current (Apr 15, 2026) reading look like?

Three states per indicator: ✅ matches analog, ⚠ partial match, ❌ diverges.

The weight of ✅ vs ❌ across 3-5 tells gives us our final translation of how well-aligned we are with the 52.3 tail analog.

### Step F — Synthesis writeup (30 min)
File: `research/2024-11_2025-01_cluster_analog.md`

Sections:
1. Abstract (3 sentences: what we did, what we found, what it means)
2. Timeline of landmarks with catalyst annotations
3. Class 1 tells table with magnitudes
4. Peak-day reconstruction
5. 2026 side-by-side translation
6. What we'd need to see over the next 30 days to confirm we're on the analog path
7. Caveats (single analog, small sample)

---

## Checkpoints — places Will can redirect

- **After Step A:** data pulled. Gut check on series availability. Skip or add?
- **After Step C:** tells identified. Do they match thesis expectations? If HY OAS is Class 4 (silent) then thesis v3.1 regime-dependence takes a hit
- **After Step D:** we have an external trigger story. Agree/disagree with it before proceeding?
- **After Step E:** translation table. If most cells are ❌, the analog doesn't apply and we should dial back Scenario B probability

---

## Output artifacts

| File | Purpose |
|------|---------|
| `scripts/fred_fetch.py` | Reusable FRED CSV fetcher — future sessions too |
| `scripts/analog_pull.py` | One-shot data pull orchestrator |
| `scripts/analog_timeline.py` | One-shot landmark + tell analysis |
| `workbook/fred_cache/*.csv` | Cached raw series |
| `research/analog_2024_cluster/daily.csv` | Aligned daily DataFrame |
| `research/analog_2024_cluster/tells_table.md` | Raw tells classification |
| `research/2024-11_2025-01_cluster_analog.md` | Main deliverable — full writeup |
| `workbook/KB.tsv` | KB-VIO-039 (+ maybe 040, 041) — key findings |

---

## Time estimate

- Step A (data acquisition): **20 min**
- Step B (landmarks): **15 min**
- Step C (tells): **45 min**
- Step D (peak-day reconstruction, likely subagent): **30 min**
- Step E (2026 translation): **45 min**
- Step F (writeup): **30 min**
- **Total: ~3 hours**

Could parallelize A and D (peak-day subagent can run while main thread does data pull). Realistically **2 - 2.5 hours wall-clock** if parallelized.

---

## Risks / things that could derail

1. **Yahoo may not have ^VIX9D or ^MOVE** — substitute with VX7 or skip
2. **CBOE VX settlement backfill may not go back to 2024-11** — confirm first. If not, analysis continues without futures term-structure data
3. **T+peak date may not be a clean spike** — 2025-01-22 → T+peak is described as 52.3 in KB-VIO-036 but could be an intraday wick. Need to verify it's closing spot
4. **CFTC COT data formats change** — skip if flaky, not load-bearing
5. **Peak-day web search may not surface clean catalyst** — fallback is "positioning unwind, no clear external trigger" which is itself a finding

---

## Data we are explicitly NOT pulling (and why)

- **Dealer gamma positioning** — HENRY's domain, can't replicate reliably
- **Single-stock IV surfaces** — too expensive to pull at scale, low analog value
- **Options chain for 2024-2025 VIX expiries** — yfinance doesn't preserve historical option chains
- **Realized correlation (CIX)** — nice-to-have, cut for scope

We can revisit any of these in Phase 3 if Phase 2 leaves specific questions open.

---

## What I need from Will before kickoff

- **OK to build `scripts/fred_fetch.py` as a reusable tool?** (stays in VIOLET scripts)
- **Agree on the 5 success questions above?** Add/remove?
- **Budget: 2-3 hours wall-clock OK?**
- **Peak-day web search — OK to use a subagent (general-purpose) for that one step?** It's the only step where a web search is load-bearing

---

*VIOLET 2026-04-15. Phase 2 plan. Awaits approval before execution.*
