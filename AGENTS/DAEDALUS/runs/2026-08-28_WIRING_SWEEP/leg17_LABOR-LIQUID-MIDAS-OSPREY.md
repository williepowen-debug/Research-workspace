# ⑰ METRIC-SURFACE AUDIT — LABOR / LIQUID / MIDAS / OSPREY

**Sample caveat:** n=19 rows from 4 desks, seeded random (`leg17_SAMPLE.md`, `random.seed(20260828)`). This is a sample, not a census. Findings below are per-row and per-desk; do **not** extrapolate a fleet rate from n=19.

**Line-number note:** the sample file's `L<n>` labels did not match this file's actual line numbers on any of the four desks (LABOR off by 1, LIQUID off by 2, OSPREY off by 6; MIDAS matched exactly). All citations below use **verified actual file:line** from a direct `Read` of each registry, not the sample's `L` labels. Row identity (Vector_ID) was cross-checked against the sample text in every case to confirm the correct row was audited.

---

## LABOR — `AGENTS/LABOR/workbook/VX.tsv`

### ⚠️ DESK-LEVEL FINDING (read this before the rows): the whole sampled file is FROZEN — and correctly so

`AGENTS/LABOR/workbook/VX.tsv:1` — *"# FROZEN 2026-06-26 — Not maintained. STATUS.md is the canonical truth. This ledger is preserved for historical reference only. Do not update rows; do not extend."*

Confirmed against `AGENTS/LABOR/CLAUDE.md`: line 83 ("VX.tsv + FLOW.tsv are FROZEN 2026-06-26, superseded by the STATUS Convergence Matrix — do NOT write to them"), line 111, line 296 ("**FROZEN 6/26** — Vectors ledger; superseded by STATUS Convergence Matrix. Historical reference; do not write"). This complies with root CLAUDE.md's Data Hygiene rule (a ledger must be **(a) FROZEN** or **(b) LIVE**, never silent-rot middle) — LABOR is correctly in state (a). LABOR's actual live metric surface is `STATUS.md`'s CONVERGENCE MATRIX (15 vectors, `STATUS.md:29-55`) + KEY THRESHOLDS table (`STATUS.md:90-113`), which is materially richer, differently-banded, and actively re-graded every session — a different instrument from anything in this sample.

**Consequence for this audit:** none of the 5 sampled rows are live triggers. Each is a preserved point-in-time snapshot dated 2026-02-01 to 2026-03-09 (i.e., ~5-7 months stale vs. today 2026-08-28), which is expected and compliant for a FROZEN file. Per-row verdicts below therefore answer **"was this row well-instrumented as a historical record"**, and separately note whether a **live successor** for the same underlying metric exists in `STATUS.md` today (it usually does, under different bands).

**This is a SAMPLING-POOL defect for leg ⑰, not a LABOR wiring defect:** the leg-17 pool ("22 registries VX/THRESHOLDS/TRIGGERS") drew 5 rows from a file that declares itself dead. Recommend the pool builder exclude self-declared-FROZEN files (LABOR here; LIQUID below is the same pattern) from future "is this decoration" sampling, or sample them separately under a "is the freeze itself still honored" check instead.

`AGENTS/LABOR/scripts/boot.py` (checked in full) reads only `workbook/PREDICTIONS.tsv` and `workbook/KB.tsv` — it never opens `VX.tsv`. **BOOT-RENDERED = NO for all 5 rows**, consistent with the freeze.

---

**Row 1 — `VX-LAB-1.02A`, `AGENTS/LABOR/workbook/VX.tsv:5`**
Threshold verbatim: `GREEN <1.9M | YELLOW 1.9-2.1M | ORANGE 2.1-2.5M | RED >2.5M`. Value 1,851,500, Last_Updated 2026-03-09, Source "DOL Week ending Feb 21. 3-LLM verified."
- (a) INSTRUMENT: **NONE** on-row (Source is a citation string, not a command). A live producer for the *same underlying series* exists — `AGENTS/LABOR/scripts/labor_data.py:36` fetches FRED `CCSA` ("Continuing Claims (1wk lag)") via the shared `FORGE/tools/market-data/fetch.py` — but it is **uncited on this row** and feeds `STATUS.md` vector 7 ("UI exhaustion / CC grind"), not this frozen cell. Verdict on-row: **NONE**; live-successor verdict: **PRODUCER-EXISTS-UNCITED**.
- (b) BASIS/WINDOW: **STATED** at time of record (4-week average, DOL weekly release, week-ending date given).
- CONJUNCTION: N/A — single-leg, 4 ordinal bands.
- POINTER: **NO-POINTER** (Source is prose, not a travelable in-repo id).
- MECHANISM: **CANNOT-JUDGE** — note text ("Hotel California smoothed signal rising") gestures at LABOR's freeze/duration mechanism but carries no explicit thesis link in this row.
- BOOT-RENDERED: **NO**.
- STATIONARITY: not directly gradable (historical snapshot); but note the **live successor's bands are REBASED, not reused** — `STATUS.md:96` (Continuing claims KEY THRESHOLDS row) now grades drop-to-2 at `<1,750K ×4wk`, a different scale than this row's 1.9/2.1/2.5M bands. A reader citing this frozen row's bands today would be citing superseded bands, not merely a stale value.

**Row 2 — `VX-LAB-3.01`, `AGENTS/LABOR/workbook/VX.tsv:15`**
Threshold verbatim: `GREEN >8.0M | YELLOW 7.0-8.0M | ORANGE 6.0-7.0M | RED <6.0M`. Value 6.5M ORANGE, Last_Updated 2026-02-05, Source "BLS JOLTS Dec."
- (a) INSTRUMENT: **NONE** on-row. `labor_data.py:41` fetches `JTSJOL` (JOLTS openings MoM Δ) live — **PRODUCER-EXISTS-UNCITED** for a live successor. `STATUS.md` vector 4 now grades **JOLTS NET (hires − separations)**, not raw openings level — a materially different construction than this row's band.
- (b) BASIS/WINDOW: **STATED** (BLS JOLTS, Dec reference month, dated).
- CONJUNCTION: N/A.
- POINTER: **NO-POINTER**.
- MECHANISM: **CANNOT-JUDGE** on this row's own text ("LOWEST SINCE 2017" is descriptive only); today's live mechanism framing (`STATUS.md:41`, "a gross flow cannot speak to net employment") explicitly supersedes the openings-level framing this frozen row used — worth flagging as a **superseded-mechanism** case, not a live MISMATCH.
- BOOT-RENDERED: **NO**.
- STATIONARITY: N/A (historical); band scale itself was retired per `STATUS.md:107` ("JOLTS hires GROSS — demoted 8/7").

**Row 3 — `VX-LAB-5.03`, `AGENTS/LABOR/workbook/VX.tsv:24`**
Threshold verbatim: `GREEN <0.5M | YELLOW 0.5-0.7M | ORANGE 0.7-1.0M | RED >1.0M`. Value 461K GREEN, Last_Updated 2026-02-01, Source "BLS Dec 2025."
- (a) INSTRUMENT: **NONE** anywhere — grepped `labor_data.py`'s full `LABOR_SERIES` list (no "discouraged workers" series present) and `STATUS.md` (zero hits for "Discouraged"). No live successor found.
- (b) BASIS/WINDOW: **STATED** (BLS Dec 2025, dated).
- CONJUNCTION: N/A.
- POINTER: **NO-POINTER**.
- MECHANISM: **CANNOT-JUDGE** (note "Low but watch trend" states no causal link).
- BOOT-RENDERED: **NO**.
- STATIONARITY: **CANNOT-JUDGE** — unlike rows 1-2, this metric appears to have been **fully retired at the freeze with no live successor**, not merely rebased. Worth a one-line flag to LABOR: confirm this was a deliberate drop, not a silent gap.

**Row 4 — `VX-LAB-8.02`, `AGENTS/LABOR/workbook/VX.tsv:43`**
Threshold verbatim: `<750K | 750K-1M | 1M-1.2M | >1.2M`. Value 1,206,374, Last_Updated 2026-02-02, Source "Challenger Year-End."
- **Schema-integrity defect found on this specific row** (not desk-wide — rows 1,2,3,5 in this sample are correctly 11-field-aligned): field 3 ("Current Value" by header position) holds the string `"Announced Layoffs"` (a units label, not a value), and field 4 ("Status" by header position) holds `"1,206,374"` (the number, not a color token). A script parsing this file positionally for a Status color would read a **number** where it expects `GREEN/YELLOW/ORANGE/RED`. Confirmed via `awk -F'\t'` field count (11 fields on both header and this row — the *values* are shifted, not the field count). Practical severity is low only because the file is FROZEN and unread by boot.py; if this file were ever revived to LIVE without a schema fix, this row would silently break a positional parser.
- (a) INSTRUMENT: **NONE** on-row or elsewhere in `labor_data.py`. Live successor: `STATUS.md:84` ("Challenger July") carries the current Challenger read (33,429, level+AI-share framing) sourced "Challenger, Gray & Christmas... issuer's own release" — no script producer either; this is a manually-transcribed press release read on both the frozen row and its live successor. Verdict: **PROSE-VALUE** in substance (a manually-copied press number), though the cell itself is numeric.
- (b) BASIS/WINDOW: **STATED** (Challenger Year-End 2025 annual total, dated).
- CONJUNCTION: N/A.
- POINTER: **NO-POINTER**.
- MECHANISM: **CANNOT-JUDGE**.
- BOOT-RENDERED: **NO**.
- STATIONARITY: N/A; live successor uses a **different denominator** (monthly level + AI-share %, not annual cumulative) — not a reusable band even if un-frozen.

**Row 5 — `VX-LAB-15.02`, `AGENTS/LABOR/workbook/VX.tsv:64`**
Threshold verbatim: `GREEN <0.7% | YELLOW 0.7-1.0% | ORANGE 1.0-1.3% | RED >1.3%`. Value 1.24% RED, Last_Updated 2026-02-10, Source "NY Fed Q4 2025 Household Debt Report."
- (a) INSTRUMENT: **NONE** — no script anywhere in LABOR's `scripts/` fetches NY Fed Household Debt Report series (quarterly PDF/data-tool release, not FRED-mirrored in this repo). No live successor found in `STATUS.md` (zero hits for "HELOC").
- (b) BASIS/WINDOW: **STATED** (NY Fed Q4 2025 Household Debt Report, quarterly, dated; "90+ Delinquency Transition Rate" — unit and series named).
- CONJUNCTION: N/A.
- POINTER: **NO-POINTER**.
- MECHANISM: **PARTIAL** — note text states a mechanism ("Homeowner liquidity crisis... precedes foreclosure wave 6-12mo") but this is a housing/credit-transmission mechanism that reads as closer to HOMER/CARL/REGINALD's domain (per root CLAUDE.md's transmission chain HOMER → {CARL, REGINALD}) than a core LABOR freeze/duration vector — worth flagging as a possible cross-domain orphan (row never re-homed after the freeze, and no LABOR live surface carries it forward).
- BOOT-RENDERED: **NO**.
- STATIONARITY: **CANNOT-JUDGE** — no live tracking found to compare against.

### LABOR summary table

| Row | (a) Instrument | (b) Basis/Window | Conjunction | Pointer | Mechanism | Boot-rendered | Stationarity |
|---|---|---|---|---|---|---|---|
| VX-LAB-1.02A | NONE (uncited producer exists) | STATED | N/A | NO-POINTER | CANNOT-JUDGE | NO | rebased live |
| VX-LAB-3.01 | NONE (uncited producer exists) | STATED | N/A | NO-POINTER | CANNOT-JUDGE | NO | rebased live |
| VX-LAB-5.03 | NONE (no producer anywhere) | STATED | N/A | NO-POINTER | CANNOT-JUDGE | NO | CANNOT-JUDGE (orphaned) |
| VX-LAB-8.02 | NONE (+ row-local schema defect) | STATED | N/A | NO-POINTER | CANNOT-JUDGE | NO | N/A (denominator changed) |
| VX-LAB-15.02 | NONE (no producer anywhere) | STATED | N/A | NO-POINTER | PARTIAL | NO | CANNOT-JUDGE (orphaned) |

**Triage: CONVENTION, not per-row.** The dominant defect is whole-registry: the file is (correctly) FROZEN, so "no instrument, not boot-rendered" is true of every row by design, not a per-row failure to fix. Two second-order per-row findings are genuine and narrow: (i) `VX-LAB-8.02`'s column-value shift (schema defect, row-local, latent until un-frozen); (ii) `VX-LAB-5.03` and `VX-LAB-15.02` appear to have **no live successor at all** post-freeze — worth a one-line confirm-or-flag to LABOR, not a rewrite of the registry (rewriting a correctly-FROZEN file would violate its own banner).

---

## LIQUID — `AGENTS/LIQUID/workbook/VX.tsv`

### ⚠️ DESK-LEVEL FINDING: same FROZEN pattern as LABOR, independently confirmed

`AGENTS/LIQUID/workbook/VX.tsv:1` — *"# FROZEN 2026-07-11 — not maintained; STATUS.md/KB.tsv canonical, do not cite rows as current (root CLAUDE.md Data Hygiene; Will-approved 7/11 sweep item 5)."* Line 2 adds: *"REGISTRY - POINT-IN-TIME, NOT LIVE... Live state = STATUS.md + scripts/boot.py."* Same compliant pattern as LABOR — this is the fleet's own convention working as intended, and the same sampling-pool caveat applies: this file should probably not have been eligible for a "decoration" sample in the first place.

Unlike LABOR, however, LIQUID's `boot.py` (`AGENTS/LIQUID/scripts/boot.py`, checked in full) **does** render several of the *same metric families* live via a completely separate, well-instrumented path (FRED pulls in `build_domestic()`/`build_credit()`), so per-row "does a live successor exist" answers below are mostly **yes, and boot-rendered** — just never via this frozen row.

**Row 1 — `VX-LIQUID-1.01` SOFR-IORB Spread, `AGENTS/LIQUID/workbook/VX.tsv:4`**
Full row: `SOFR 3.62% / IORB 3.65% / spread -3bps [FRED 6/24] | Yellow +5bps | Orange +15bps | Red +25bps | GREEN | 98% | 2026-06-24 | FRED SOFR (6/24)`.
- (a) INSTRUMENT: on-row **NONE** (no command cited), but the **live successor is the same metric, actively boot-rendered**: `AGENTS/LIQUID/scripts/boot.py:179-195` pulls FRED `SOFR`/`IORB` and computes `SOFR-IORB` every boot (`add("DOMESTIC", "SOFR-IORB", ...)`). Verdict: **PRODUCER-EXISTS-UNCITED** on-row; **COMMAND-NAMED** for the live surface.
- (b) BASIS/WINDOW: **STATED** (FRED SOFR/IORB, dated 6/24, spread computed).
- CONJUNCTION: N/A — single-leg.
- POINTER: **NO-POINTER** (Source is a citation, not travelable).
- MECHANISM: row note explicitly states the mechanism and its verdict — *"Structural-leak hypothesis remains REJECTED (KB-LIQ-051, Apr breach mechanical)"* — **MATCH** (measures funding-plumbing stress at the level the thesis targets).
- BOOT-RENDERED: **YES** for the live successor — `boot.py:195`. (Not this row itself, which is frozen and never read by boot.py.)
- STATIONARITY: **VERIFIED, not the drifting one.** The prompt flagged `KB-LIQ-106` (SOFR75−IORB, a *different* boot.py line, 2026-08-27) as regime-drifted (≥0bp on 89.5%+ of days). I checked directly: `STATUS.md:23` and `AGENTS/LIQUID/CLAUDE.md:192` confirm KB-LIQ-106 is about **`SOFR75−IORB`** (the 75th-percentile dispersion line), a *distinct* boot.py row from **this sampled row's `SOFR-IORB`** (median spread). Per `STATUS.md:23`: *"SOFR−IORB ≥0 on only 25.5% of days (median −5bp)"* — i.e. plain SOFR-IORB is **well-calibrated and NOT the drifting band**; LIQUID's own 8/27 finding explicitly uses SOFR-IORB's 25.5% clear-rate as the *contrast case* proving SOFR75-IORB is broken by construction. **OK, per the prompt's own instruction to verify rather than assume — this row is not an instance of the flagged drift.**

**Row 2 — `VX-LIQUID-1.03` Treasury FTD, `AGENTS/LIQUID/workbook/VX.tsv:6`**
Full row: `Settlement | $42.4B | Yellow $40B | Orange $50B | Red $60B | YELLOW | 80% | 2026-01-25 | SEC/DTCC | Elevated due to central clearing transition friction + high rate scarcity. Monitor aged fails ratio for deterioration.`
- (a) INSTRUMENT: **NONE** — grepped all of `AGENTS/LIQUID/scripts/*.py` (`boot.py`, `cftc_tff_rates.py`, `hy_oas_watch.py`, `sofr_dispersion.py`, `fp_backtest_079.py`) for "FTD"/"fail to deliver"/"settlement": zero hits. No producer anywhere in LIQUID, and `boot.py`'s three dashboards (Credit/Domestic/Foreign) carry no FTD line. **No live successor found.**
- (b) BASIS/WINDOW: **PARTIAL** — level and vendor stated (SEC/DTCC, $42.4B), but no window/cadence given (Treasury fails-to-deliver data is a settlement-level metric with no stated observation window on this row — daily? weekly aggregate? not specified), and Last_Updated (2026-01-25) predates even LIQUID's own freeze (2026-07-11) by over 5 months at the point it was frozen — this was already the stalest row in the file when frozen.
- CONJUNCTION: N/A.
- POINTER: **NO-POINTER**.
- MECHANISM: **CANNOT-JUDGE** — note gestures at "central clearing transition friction," no explicit tie to a stated LIQUID thesis leg in this row.
- BOOT-RENDERED: **NO** (confirmed absent from `boot.py`'s three dashboards).
- STATIONARITY: **CANNOT-JUDGE** (no live series to compare against; this channel appears dropped, not merely stale).

**Row 3 — `VX-LIQUID-2.03` Auction Tail, `AGENTS/LIQUID/workbook/VX.tsv:13`**
Full row: `Auctions | 2.0bps (20Y Feb 19) | Yellow >1.5bps | Orange >3.0bps | Red >5.0bps | YELLOW | 90% | 2026-02-20 | Treasury | ...Watch for >3.0bps (ORANGE).`
- (a) INSTRUMENT: **NONE** on-row or in `boot.py`. Note: `boot.py` DOES compute a differently-named "**SOFR99 tail**" (`boot.py:219-220`, repo-market tail-blowout, threshold ≥20bp) and a **CCC-BB "tail-gap"** (`boot.py:127-131`) — both use the word "tail" but are *unrelated instruments* (repo-distribution / credit-spread tails, not Treasury-auction bid-to-cover tails). A grep for "tail" alone would false-positive match these; confirmed by reading context that none of them fetch Treasury auction results. **No live successor for this specific metric (Treasury auction tail bps) found anywhere in LIQUID.**
- (b) BASIS/WINDOW: **STATED** (specific auction: 20Y, Feb 19, tenor and date named; unit bps).
- CONJUNCTION: N/A.
- POINTER: **NO-POINTER**.
- MECHANISM: **CANNOT-JUDGE**.
- BOOT-RENDERED: **NO**.
- STATIONARITY: **CANNOT-JUDGE**.

**Row 4 — `VX-LIQUID-6.06` BCRED Redemption Cap Utilization, `AGENTS/LIQUID/workbook/VX.tsv:23`**
Full row: `Credit Transmission | 7.9% gross ($3.7B); cap raised 5%→7% | Cap >4% | Cap raised | Gate activated | RED | 90% | 2026-03-04 | Blackstone/Press | CONFIRMED Mar 3: BCRED received $3.7B gross redemption requests...`
- (a) INSTRUMENT: **NONE** — press-sourced qualitative event, not a fetchable series; no script anywhere targets private-credit BDC redemption data (this is not published on a machine-readable cadence). Verdict: **PROSE-VALUE** in substance (a numeric % embedded in a narrative press event), not a live-fetchable instrument.
- (b) BASIS/WINDOW: **PARTIAL** — the specific event and its date are stated (Mar 3 2026 redemption requests, cap raise), but the *ongoing* metric (redemption-cap utilization) has no stated observation cadence (is it checked monthly? per fund NAV release? undefined) — this reads as a one-shot event log dressed as a continuous-threshold vector.
- CONJUNCTION: the three bands (`Cap >4%` / `Cap raised` / `Gate activated`) are effectively an escalation ladder of *qualitatively different event types*, not one metric crossing thresholds — this is closer to a state machine than a numeric gate. N/A in the strict sense (single reported state, not an AND/OR of legs), but flagged: the band design itself conflates "% utilization" with "did management act" (cap raise, gate activation), which are policy responses, not the underlying stress metric.
- POINTER: **NO-POINTER**.
- MECHANISM: row states the mechanism explicitly ("Private credit → public market transmission ACTIVE") — **MATCH** in direction, though un-updated: `STATUS.md:178` shows the *live* PC-redemption picture has moved on materially since this row (BCRED July distribution cut −10%, term-funding door still open per a fresh $750M note deal) — a **different, more current narrative** than this frozen row's March snapshot, which the live text does not contradict in direction but does update substantially (BX raised cap in March; by the live STATUS text the credit stress is described as "term-funding door stayed OPEN," a materially calmer read than this row's RED/"Gate activated" framing).
- BOOT-RENDERED: **NO**.
- STATIONARITY: N/A (event-based, not a stationarity question).

**Row 5 — `VX-LIQUID-7.02` Japan Treasury Holdings, `AGENTS/LIQUID/workbook/VX.tsv:27`**
Full row: `Foreign Official | $1,225.3B (Jan 2026 TIC) | Yellow <$1.0T | Orange <$900B | Red <$800B | GREEN | 85% | 2026-03-18 | TIC Data (Jan 2026, released Mar 18) | ...watch Feb/Mar TIC (May release) for reversal.`
- (a) INSTRUMENT: **NONE** — grepped `boot.py`'s FOREIGN dashboard (`boot.py:272-283`): it carries only `USD/JPY` (yfinance price) and `Brent` price refs, **no TIC/Treasury-holdings series at all**. TIC data (monthly, ~6-week-lag Treasury release) is not fetchable via FRED/yfinance and has no script producer anywhere in LIQUID. **No live successor found** — confirmed by reading `STATUS.md`'s FOREIGN section narrative (line 56, "FOREIGN DASHBOARD REPRICED on ZHAO's...packets"), which shows TIC-derived reads are now **ZHAO's domain**, sourced via ZHAO's own analysis and delivered as packets/prose to LIQUID rather than fetched by any LIQUID script.
- (b) BASIS/WINDOW: **STATED** (TIC data, Jan 2026 reference month, released Mar 18, dated).
- CONJUNCTION: N/A.
- POINTER: **NO-POINTER**.
- MECHANISM: row note states "Phase 2 carry trade — Japan BUYING as flight-to-safety... oil-in-yen +140% YTD will force repatriation — watch Feb/Mar TIC" — this is a stated, specific, falsifiable mechanism. Cross-checked against the *live* STATUS text (line 56): the China/Japan TIC read has since been **substantially revised** — a "Rule Zero" was added to `TIC_FRAMEWORK.md` ("a TIC level change is NOT a flow; the wedge flips sign inside one release") specifically because an earlier framework mis-read TIC levels as flows. Verdict: **MISMATCH** in the sense that this frozen row's mechanism framing (simple level-watch) is the exact framing LIQUID's own later self-audit (STATUS.md:56, "TIC_FRAMEWORK.md rewritten with a new Rule Zero") found defective for the *China* TIC row and presumably applies equally to this un-revisited *Japan* TIC row — worth a flag, not a rewrite (file is frozen).
- BOOT-RENDERED: **NO**.
- STATIONARITY: **CANNOT-JUDGE** (no live series to compare; ownership has moved to ZHAO, a different agent's instrument this audit did not sample).

### LIQUID summary table

| Row | (a) Instrument | (b) Basis/Window | Conjunction | Pointer | Mechanism | Boot-rendered | Stationarity |
|---|---|---|---|---|---|---|---|
| VX-LIQUID-1.01 SOFR-IORB | NONE on-row / COMMAND-NAMED live | STATED | N/A | NO-POINTER | MATCH | YES (live successor) | OK — verified, not the flagged drift |
| VX-LIQUID-1.03 Treasury FTD | NONE (no producer anywhere) | PARTIAL (no window) | N/A | NO-POINTER | CANNOT-JUDGE | NO | CANNOT-JUDGE |
| VX-LIQUID-2.03 Auction Tail | NONE (name-collides with 2 unrelated boot.py "tail" instruments) | STATED | N/A | NO-POINTER | CANNOT-JUDGE | NO | CANNOT-JUDGE |
| VX-LIQUID-6.06 BCRED | PROSE-VALUE | PARTIAL | N/A (state-machine, not gate) | NO-POINTER | MATCH-but-stale | NO | N/A |
| VX-LIQUID-7.02 Japan TIC | NONE (no producer; ownership moved to ZHAO) | STATED | N/A | NO-POINTER | MISMATCH (superseded framing) | NO | CANNOT-JUDGE |

**Triage: CONVENTION dominates (the FROZEN/POINT-IN-TIME banner, correctly applied), but 3 of 5 rows also carry a genuine PER-ROW gap that survives the freeze context: Treasury FTD, Auction Tail, and Japan TIC have** ***no live successor anywhere in LIQUID*** **— unlike SOFR-IORB and (loosely) BCRED, which do have live tracking elsewhere.** This is worth a specific flag to LIQUID/PROME: three funding/auction/foreign-official channels that were tracked pre-freeze appear to have been dropped outright rather than migrated to `boot.py`/`STATUS.md`, not merely archived.

---

## MIDAS — `AGENTS/MIDAS/workbook/VX.tsv`

**Not FROZEN** — this registry is LIVE and actively re-graded (`Last_Updated`/`as_of` on all 5 sampled rows = 2026-08-27, i.e. the day before this audit). `AGENTS/MIDAS/boot.py` (read in full) runs `metals_watch.py` as its leg 0 (`boot.py:152-162`), which mechanically computes real yield (FRED `DFII10`), gold/silver/copper/Pt/Pd spot, GSR, LME copper inventory vs. a rolling 2yr median, and the M1 DIVERGE/CONVERGE classifier — a genuinely well-instrumented desk. This is the healthiest of the four desks sampled.

**Row 1 — `VX-MIDAS-M1`, `AGENTS/MIDAS/workbook/VX.tsv:2`** (gold vs. real-yield divergence)
Threshold cell verbatim: *"v2 kills: gold <$3,317 w/o a real-yield spike · WGC Q2 <100t (UNMEASURED — overdue) · gold re-decouples UP 3+wk = FIRED 8/7. POLARITY (7/17): DIVERGE=REVIEW rc=1, CONVERGE=quiet rc=0."*
- This is **three independently-OR'd kill conditions**, not one conjunctive gate — treating each as its own leg:
  - Leg (i) "gold <$3,317 w/o a real-yield spike": (a) COMMAND-NAMED — `metals_watch.py` fetches `GC=F` closes and `DFII10` every boot (per `boot.py`'s leg 0 + the row's own Source cell "metals_watch.py (leg 5b...) + FRED DFII10/T10YIE/DGS10 + GC=F closes"). (b) STATED (level threshold, real-yield-spike qualifier named).
  - Leg (ii) "WGC Q2 <100t": self-flagged by MIDAS itself in the same cell as **"UNMEASURED — overdue"** — (a) **NONE**, confirmed no script fetches World Gold Council quarterly demand data anywhere in `AGENTS/MIDAS/`. This is a disclosed gap, not a hidden one: the row names its own dead leg. (b) STATED in form (quarterly, <100t), UNSTATED in that no instrument exists to grade it.
  - Leg (iii) "gold re-decouples UP 3+wk = FIRED 8/7": (a) COMMAND-NAMED — `metals_watch.py:340-388` implements a dedicated "kill-condition #3 window (3-WEEK/21d)" classifier, confirmed mechanically computed (not agent judgment) and **it fired** (per the row's own Value cell, "kill-cond #3 FIRED, count 1/4"). (b) STATED.
- CONJUNCTION verdict: **N/A in the strict AND sense (these are 3 independent OR'd kill triggers, each single-leg)**, but flagged: one of the three (WGC Q2) is **permanently CANNOT-FIRE today** (no instrument exists) — so the *effective* live gate is 2-of-3 legs, and MIDAS has disclosed this itself rather than silently carrying a dead leg. This is the healthy version of the pattern AEOLUS/MARCO found elsewhere: **self-disclosed, not hidden.**
- POINTER: `KB-071` cited in-cell — **UNCHECKED** (a knowledge-base row id, not verified against `KB.tsv` in this pass; low materiality, informational cross-ref not a source-of-truth pointer).
- MECHANISM: row explicitly ties the vector to a "debasement premium" mechanism and cites a measured beta-attenuation caveat (GC=F vs GLD, ~23% attenuated) — **MATCH**, and unusually rigorous (quotes the caveat against its own favored reading: "the attenuation OVERSTATES the unexplained residual - the self-serving direction").
- BOOT-RENDERED: **YES** — `metals_watch.py` leg 5b computes and prints the kill-cond-#3 classification at every boot (`metals_watch.py:340-388`, `boot.py:152-162`).
- STATIONARITY: **CANNOT-JUDGE** for the debasement-premium level itself (regime question, not a quick check); the real-yield leg (`DFII10`) is a standard macro series, plausibly stationary over the row's life.

**Row 2 — `VX-MIDAS-M2`, `AGENTS/MIDAS/workbook/VX.tsv:3`** (silver + GSR)
Threshold verbatim: `GSR>85 sustained 3+ sess = 2; >95 = 4 — moving AWAY from both`.
- (a) INSTRUMENT: **COMMAND-NAMED** — `metals_watch.py (GC=F/SI=F closes)`, confirmed the script computes GSR from both futures closes.
- (b) BASIS/WINDOW: **STATED** (level bands + explicit "3+ sess" sustain window).
- CONJUNCTION: N/A (single metric, ordinal bands).
- POINTER: `KB-032` cited, unchecked (informational).
- MECHANISM: row explicitly checks for a roll-artifact confound before re-basing its own narrative ("VERIFIED REAL, NOT A ROLL ARTIFACT, BEFORE RE-BASING") — **MATCH**, and a good instance of self-verification before a narrative flip.
- BOOT-RENDERED: **YES** (`metals_watch.py`, GSR leg).
- STATIONARITY: **OK** — GSR is a standard, long-tracked ratio; row itself cites a 1986-2026-style historical distribution elsewhere in the desk (via the M1-POS row's COT context) suggesting the desk is aware of long-run norms.

**Row 3 — `VX-MIDAS-I1`, `AGENTS/MIDAS/workbook/VX.tsv:4`** (copper)
Threshold verbatim: `copper -20% AND LME inv +100% vs 2yr-median (244,175t [7/22] → +100%=488kt) = 5 (conjunction NOT met — price firm, inv benign-and-falling); LPR hold + copper -5% in 2 sess (MIDAS-05) = yellow trigger`.
- CONJUNCTION: this is a genuine **AND** gate (price −20% AND inventory +100% vs. 2yr median).
  - Leg (price −20%): (a) COMMAND-NAMED, `HG=F` closes via `metals_watch.py`. (b) STATED.
  - Leg (inventory +100% vs 2yr median): (a) COMMAND-NAMED, `metals_watch.py` leg 6 scrapes westmetall.com LME stocks and computes a trailing-2yr rolling median (`metals_watch.py:123-151`, confirmed a real, non-trivial baseline computation with its own basis note). (b) STATED (n=507, as-of date given).
  - Gate verdict: **CAN-FIRE** — both legs are live-instrumented and the row itself reports the conjunction status each session ("conjunction NOT met").
- **Self-disclosed defect (row's own notes column, verbatim):** *"Stays 1 UNSCOREABLE-up per L-13(a): the registered bands are all DOWNSIDE and cannot score the tightening, its death, OR its resurrection."* This is exactly the audit's target pattern (a registered gate that structurally cannot fire in one direction), but again **self-disclosed and escalated** — the row states it was escalated to Will 2026-08-21 as L-13(b). Verdict: the *downside* conjunction CAN-FIRE; the *upside/tightening* case is **CANNOT-FIRE by construction** (no band exists for it at all, not merely an unmet threshold) — MIDAS has flagged this rather than let it pass silently.
- POINTER: `KB-045`/`KB-059`, unchecked (informational).
- MECHANISM: row explicitly lists ≥4 candidate mechanisms for the copper-up/inventory-down state (demand strength / SA-Chile-Peru supply outage / AI-grid structural / COMEX-LME warrant relocation) and states only one is the "China-growth tell I1 exists to produce" — **PARTIAL MATCH**, disclosed ambiguity rather than an unexamined mismatch.
- BOOT-RENDERED: **YES**.
- STATIONARITY: **OK** — the row itself tracks baseline drift explicitly ("Third median vintage recorded... KB-059 drift, n=3"), i.e. the desk is actively watching for exactly this failure mode on its own baseline.

**Row 4 — `VX-MIDAS-I2`, `AGENTS/MIDAS/workbook/VX.tsv:5`** (PGMs)
Threshold verbatim: `major SA/Russia outage = 4` (single registered band; no Yellow/Orange gradient in this schema — MIDAS uses a single freetext threshold cell + 1-5 score, not G/Y/O/R columns).
- (a) INSTRUMENT: **COMMAND-NAMED** for spot (`metals_watch.py (PL=F/PA=F)`) + a named primary for the registered trigger itself ("Fed Register 2026-08487 (CONF)" — a supply-outage disclosure channel) + WebSearch (labeled PROV, i.e. provisional-tier).
- (b) BASIS/WINDOW: **PARTIAL** — spot levels are STATED (dated closes); the *trigger* itself ("major SA/Russia outage") has no quantified magnitude or window (what counts as "major"? over what period?) — qualitative escalation criterion.
- CONJUNCTION: N/A (single trigger).
- **Self-disclosed defect, row's own notes (verbatim, the strongest finding in this sample):** *"BAND BLINDNESS IS THE LIVE FINDING: this vector's registered triggers key on CONFIRMED SA/Russia outages, so a 3.11-sigma joint PGM repricing with NO news is UNSCOREABLE... Score unchanged at 2 (yellow) because nothing registered fired, NOT because the tape was quiet — do not read the score as calm."* This is a textbook CANNOT-FIRE instance (the gate requires a *news event*, so a pure *price* dislocation — even a 3-sigma one — cannot move the score) — again **self-disclosed, flagged not repaired** ("FLAGGED NOT REPAIRED (L-20, tier test 4); no recommendation offered").
- POINTER: `KB-062/063/064`, `KB-008`, unchecked (informational).
- MECHANISM: row explicitly retracts its own prior mechanism read ("'Pt outrunning Pd => monetary-adjacent' is FALSE") based on measured beta-residual analysis — **MATCH**, rigorous self-correction.
- BOOT-RENDERED: **YES** for spot values; **NO** for the news-trigger itself (no script can render "an outage occurred").
- STATIONARITY: **CANNOT-JUDGE** for the beta-to-gold relationship (regime question).

**Row 5 — `VX-MIDAS-M1-POS`, `AGENTS/MIDAS/workbook/VX.tsv:6`** (COT positioning)
Threshold cell verbatim: `n/a` / notes: `NO REGISTERED BAND — reporting vector only. MIDAS-07's branch levels were a one-off frozen grading frame that has now RESOLVED; converting them into standing bands would be a new threshold and is Will-gated (not done)`.
- (a) INSTRUMENT: **COMMAND-NAMED** — `AGENTS/MIDAS/cot_gold.py`, confirmed present, reading CFTC legacy futures-only raw data, code-keyed and vintage-verified per the row's own Source cell.
- (b) BASIS/WINDOW: **STATED** where it applies (weekly CFTC print, dated 2026-08-11 — note: 16 days stale vs. the desk's other rows at 2026-08-27, since COT is a Friday-only release and `cot_gold.py` is **not wired into `boot.py`** — confirmed by grepping `boot.py` for "cot"/"COT": zero hits, unlike `metals_watch.py` which IS wired at boot).
- CONJUNCTION/threshold: **N/A by design** — this is honestly a **PROSE-VALUE / reporting-only row**, and the row is explicit and correct about that ("deliberately carries NO band so it cannot silently become a trigger"). This is the *opposite* of decoration: a row that could easily have been given a plausible-looking-but-uncalibrated band, and was deliberately left un-banded and Will-gated instead.
- POINTER: `KB-041/042`, unchecked (informational).
- MECHANISM: N/A (reporting vector, no fire condition to check against a mechanism).
- BOOT-RENDERED: **NO** — `cot_gold.py` exists but is not called from `boot.py`; this is a genuine (mild) staleness risk since nothing surfaces "COT hasn't been re-pulled in N weeks" automatically. Given the row explicitly disclaims triggering, materiality is low.
- STATIONARITY: N/A.

### MIDAS summary table

| Row | (a) Instrument | (b) Basis/Window | Conjunction | Pointer | Mechanism | Boot-rendered | Stationarity |
|---|---|---|---|---|---|---|---|
| VX-MIDAS-M1 | COMMAND-NAMED (2 of 3 legs); 1 leg self-flagged NONE | STATED | CAN-FIRE (2 legs); dead leg disclosed | KB-071 unchecked | MATCH | YES | CANNOT-JUDGE |
| VX-MIDAS-M2 | COMMAND-NAMED | STATED | N/A | KB-032 unchecked | MATCH | YES | OK |
| VX-MIDAS-I1 | COMMAND-NAMED (both legs) | STATED | CAN-FIRE (downside); CANNOT-FIRE (upside, disclosed) | KB-045/059 unchecked | PARTIAL (disclosed ambiguity) | YES | OK (drift actively tracked) |
| VX-MIDAS-I2 | COMMAND-NAMED (spot) / news-trigger has no instrument | PARTIAL | N/A | KB-062-064/008 unchecked | MATCH | YES (spot) / NO (trigger) | CANNOT-JUDGE |
| VX-MIDAS-M1-POS | COMMAND-NAMED | STATED | N/A (deliberately unbanded) | KB-041/042 unchecked | N/A | NO (not wired into boot.py) | N/A |

**Triage: PER-ROW, and mostly self-caught by the desk already.** MIDAS is the strongest-instrumented of the four desks sampled: every value cell names a real, checkable producer, and where a gate structurally cannot fire (WGC leg, I1 upside, I2 news-only trigger), **MIDAS's own notes column says so explicitly and routes it to Will/tier-test rather than letting it pass as a live gate.** The one live gap this audit adds beyond what MIDAS already disclosed: `cot_gold.py` is not wired into `boot.py`, so `M1-POS` staleness (currently 16 days) has no automatic surfacing — low materiality since the row is explicitly non-triggering, but worth a one-line CHECKS.tsv-style note if MIDAS wants boot-time staleness coverage for it.

---

## OSPREY — `AGENTS/OSPREY/workbook/VX.tsv`

### ⚠️ DESK-LEVEL FINDING: no `boot.py`, no `scripts/` directory at all

`find AGENTS/OSPREY -iname "*.py"` returns **zero results**. OSPREY has no boot script, no producer script, nothing mechanical anywhere in its directory. **BOOT-RENDERED = NO for all 4 sampled rows, trivially — there is no boot surface to render them.** This is a domain-appropriate design, not obviously a defect: OSPREY is a geopolitical intelligence desk (Russia-Ukraine energy-war strike tracking) whose inputs are press reporting and primary-source documents (Federal Register, Bloomberg, Kyiv/Moscow claims), not fetchable numeric series — there is no FRED/yfinance equivalent for "was a refinery struck." The relevant question for this domain is not "is there a script" but "is there a disciplined, checkable manual-sweep process with a real freshness clock," which is answered below.

Schema note: rows still carry legacy `VX-HAWK-*` IDs (OSPREY spun out of HAWK 2026-07-12; `VX.tsv:6` documents this is deliberate — "IDs kept as VX-HAWK-* ... continuity of history matters more than a clean ID reset"). Not a defect.

**Row 1 — `VX-HAWK-UKR-01` Russia-Ukraine Energy, `AGENTS/OSPREY/workbook/VX.tsv:8`**
Status=RED. Green/Yellow/Orange/Red cells are qualitative state descriptions (e.g. Red = "✅ TRIGGERED: ~1/3 refining offline; record campaign intensity"), not numeric bands.
- (a) INSTRUMENT: **PROSE-VALUE** — no runnable command; value is a synthesized narrative citing named primaries (Bloomberg 8/18, etc.) per-claim.
- (b) BASIS/WINDOW: **PARTIAL** — individual claims inside the cell are dated and sourced (e.g. "3.58 M bpd 4-wk to 8/16... [Bloomberg 8/18]"), but the **band definitions themselves** (Green/Yellow/Orange/Red) are qualitative descriptions with no quantified threshold or window (what specifically moves Orange→Red is narrative judgment, not a stated numeric rule) — this is consistent with `AGENTS/OSPREY/CLAUDE.md:15`, which explicitly rejects "a scenario-ladder A/B/C/D construct" in favor of judgment-scored channels.
- CONJUNCTION: this single VX row **textually aggregates three independently-scored channels** (Channel 1 refineries=4, Channel 2 crude-terminals=5, Channel 3 shadow-fleet=3, per the cell's own "★★ CHANNEL-2 UPGRADED 4->5... Channels 1 (4) and 3 (3) carried") into **one** Status/Green-Red set of columns. **Flagged tension**: `AGENTS/OSPREY/CLAUDE.md:137` explicitly instructs *"Do not force a composite sum — report the three scores side by side"* for the three-channel dashboard, yet this VX.tsv row's schema (one Status cell, inherited from HAWK) can only hold a single aggregate value. The three channel scores are readable only by parsing free text inside the Value cell, not by column. This is a **schema-shape MISMATCH** between OSPREY's own stated methodology (three independent, non-summed scores) and the row's structure (one composite RED) — mitigated in practice because `STATUS.md` maintains the correctly-shaped three-channel table separately (per `CLAUDE.md:137`, "same instance there"), so the VX.tsv row is effectively a legacy/secondary surface, not the desk's primary channel record.
- POINTER: Source cell = `"domain/energy-strikes/ ledger; KB-HAWK-184..187; sub-agent sweep Jun 19"`. **Traveled: OK.** `AGENTS/OSPREY/domain/energy-strikes/STRIKES.tsv` exists, is current (two-clock header: `"# swept-complete through: 2026-08-20"`, an 8-day-old sweep vs. today 2026-08-28), and is unusually rigorous — it carries a documented history of self-caught completeness failures (e.g. a Taman terminal strike missed for 3 weeks, found and logged 8/20) and explicit vintage-trap catches (a WebFetch cross-check that rejected a fabricated "August 18" strike date). This is a strong, verified pointer.
- MECHANISM: the row's implicit mechanism (strikes → refining/export capacity offline → price) is stated and, per the linked STRIKES.tsv, actively cross-checked against outcome data (Bloomberg export-volume prints) — **MATCH**.
- BOOT-RENDERED: **NO** (no boot.py exists).
- STATIONARITY: N/A (event-driven state, not a stationary series).

**Row 2 — `VX-HAWK-SHADOW-01` Shadow Fleet Enforcement, `AGENTS/OSPREY/workbook/VX.tsv:9`**
- (a) INSTRUMENT: **PROSE-VALUE**.
- (b) BASIS/WINDOW: **PARTIAL** — individual claims dated/sourced, band definitions qualitative (e.g. Red = "Naval confrontation, European vessel seized by Russia" — an event description, not a threshold).
- CONJUNCTION: N/A (single-channel row, no internal AND/OR).
- POINTER: Source = "Guardian, United24, DOJ; SIG-W-20260419-026" — the `SIG-W-*` id is a WALTER signal-routing reference; **UNCHECKED** in this pass (not travelable to a file without accessing WALTER's board log, out of scope for this leg's file set). Press names are not travelable pointers by construction (external, correctly marked **UNCHECKED-EXTERNAL** — not fetched, per instructions).
- MECHANISM: row explicitly separates "enforcement" (Western seizure/sanctions) from "kinetic" (Ukrainian strikes) mechanisms and flags where the two get conflated by other desks routing to OSPREY — *"the ~135M bbl loaded-not-delivered backlog is attributed by Bloomberg to the REFINERY campaign + tighter US/EU sanctions enforcement... NOT to Ukraine's kinetic tanker strikes. Enforcement synthesis is HAWK's lane; do not claim the backlog as this vector's output."* — **MATCH**, and a good instance of scope discipline (declining to bank an adjacent desk's evidence as its own).
- BOOT-RENDERED: **NO**.
- STATIONARITY: N/A.

**Row 3 — `VX-HAWK-SHADOW-02` Shadow Fleet Naval Confrontation, `AGENTS/OSPREY/workbook/VX.tsv:10`**
- (a) INSTRUMENT: **PROSE-VALUE**.
- (b) BASIS/WINDOW: **PARTIAL**, same pattern as row 2.
- CONJUNCTION: N/A.
- POINTER: Source = "Al Jazeera, Guardian; SIG-W-20260419-026; SIG-W-20260419-028" — **UNCHECKED-EXTERNAL** (press) / SIG ids unchecked (out of scope).
- MECHANISM: row explicitly self-corrects a misclassification — *"Both HAWK and FALCON routed this to OSPREY as if it were a shadow-fleet/Channel-3 item; it is the opposite — Russia attacking Ukraine's export corridor, non-oil... Confrontation is now TWO-WAY... which this row's framing did not represent."* — this is the row **catching its own mechanism error mid-record**: worth noting positively (the fleet's cross-agent routing put a wrong-direction event into this vector, and OSPREY caught and corrected it rather than silently scoring it). Verdict: **MATCH**, post-correction.
- BOOT-RENDERED: **NO**.
- STATIONARITY: N/A.

**Row 4 — `VX-OSPREY-GAS-01` Russia Gas/LNG Export Supply Loss, `AGENTS/OSPREY/workbook/VX.tsv:11`**
- (a) INSTRUMENT: **PROSE-VALUE**.
- (b) BASIS/WINDOW: **PARTIAL** — Red band states a quantified window ("Sustained (>2wk) loss of a major gas/LNG export route, or FM on an Arctic LNG train") — this is actually the **best-specified band of the four OSPREY rows sampled** (has an explicit duration threshold), though Green/Yellow/Orange remain qualitative.
- CONJUNCTION: N/A.
- POINTER: Source = "Gazprom via RT 7/7; Moscow Times 7/15; Bloomberg 7/10; REPowerEU regulation" — **UNCHECKED-EXTERNAL**.
- MECHANISM: row explicitly documents its own creation as a gap-fix — *"CREATED IN RESPONSE TO FALCON'S 7/30 PACKET, which grepped OSPREY's whole directory for Nord Stream/TurkStream/... and got ZERO hits, against the world's largest gas exporter"* — and states a deliberate scope boundary (gas SUPPLY-LOSS facts only; pricing→SAM, EU politics→HANS, cross-war synthesis→HAWK). **MATCH**, and a well-documented instance of a coverage gap being found and closed with scope discipline rather than scope creep.
- BOOT-RENDERED: **NO**.
- STATIONARITY: N/A.

### OSPREY summary table

| Row | (a) Instrument | (b) Basis/Window | Conjunction | Pointer | Mechanism | Boot-rendered | Stationarity |
|---|---|---|---|---|---|---|---|
| VX-HAWK-UKR-01 | PROSE-VALUE | PARTIAL | schema MISMATCH (3 channels forced into 1 composite; mitigated by a correctly-shaped STATUS.md table) | OK (STRIKES.tsv verified current) | MATCH | NO | N/A |
| VX-HAWK-SHADOW-01 | PROSE-VALUE | PARTIAL | N/A | UNCHECKED-EXTERNAL | MATCH | NO | N/A |
| VX-HAWK-SHADOW-02 | PROSE-VALUE | PARTIAL | N/A | UNCHECKED-EXTERNAL | MATCH (self-corrected) | NO | N/A |
| VX-OSPREY-GAS-01 | PROSE-VALUE | PARTIAL (best-specified Red band of the 4) | N/A | UNCHECKED-EXTERNAL | MATCH | NO | N/A |

**Triage: CONVENTION.** All four rows share the same shape: no script producer (domain-appropriate — this is qualitative intelligence, not a numeric feed), qualitative bands with per-claim (not per-band) sourcing, and no boot-time rendering (no boot.py exists at all). The one genuine per-row finding is `VX-HAWK-UKR-01`'s schema/methodology tension (single composite column vs. OSPREY's own "report three scores separately" rule) — this is a **legacy-schema** issue (inherited from HAWK at spinout) rather than evidence of a decorative/unfireable gate; OSPREY's actual channel-scoring discipline (documented in `CLAUDE.md` §Channel kill/re-arm rules with explicit day-count windows, e.g. "no vessel-strike incident for 21+ days") is materially more rigorous than the VX.tsv row alone would suggest. Recommend: if the pool re-samples OSPREY, prefer reading `STATUS.md`'s three-channel dashboard directly rather than this legacy VX.tsv row, which under-represents the desk's actual discipline.

---

## What this audit could NOT see

- **External sources not fetched** (per instructions — do NOT fetch): all press citations (Bloomberg, Guardian, Reuters, Kyiv Independent, etc.) across all four desks; FRED/BLS/DOL/Treasury/TIC/NY-Fed primary releases; CFTC COT raw files; westmetall.com LME data; Federal Register documents. All were treated as UNCHECKED-EXTERNAL / cited-as-stated rather than verified.
- **KB.tsv cross-references not verified**: MIDAS's `KB-071/032/045/059/062-064/008/041/042` and OSPREY's `KB-HAWK-184..187`/`SIG-W-*` ids were noted but not opened against their source `KB.tsv`/board-log rows — labeled "unchecked" throughout rather than defaulted to OK.
- **STATUS.md was read in full for LABOR and substantially for LIQUID** (to establish live-successor existence) but only **grepped/spot-read** for MIDAS and OSPREY — I did not do a line-by-line audit of MIDAS's STATUS.md convergence matrix or OSPREY's three-channel STATUS.md dashboard; my MIDAS/OSPREY findings rest on the VX.tsv rows, `boot.py`/`metals_watch.py`/`CLAUDE.md` reads, and (for OSPREY) `STRIKES.tsv` and `CLAUDE.md`'s channel-kill rules.
- **LIQUID's `sofr_dispersion.py`, `cftc_tff_rates.py`, `hy_oas_watch.py`, `fp_backtest_079.py` were grepped for specific keywords, not read line-by-line** — it's possible one of them has an undiscovered secondary relevance to Auction Tail/FTD/Japan TIC that a keyword grep missed (judged low-probability given their names and the docstrings visible in `CLAUDE.md`'s tool-inventory table, but not exhaustively ruled out).
- **The `VX-LAB-8.02` schema defect (column-value shift) was found by field-count inspection of this one row against the header** — I did not systematically re-scan LABOR's entire 77-row VX.tsv for the same defect elsewhere; I noted (from earlier context while reading the full file) that at least `VX-LAB-6.03`–`6.06` and the `8.0x` block appear to use a **different, wider column layout** (an extra "Category" field + a "Confidence%" field not in the declared 11-column header) than the declared header — this looks like a desk-wide schema-drift pattern in LABOR's frozen file, not limited to the one sampled row, but I did not audit it exhaustively since it is out of this leg's 19-row sample and the file is FROZEN (low live impact).
- **Judgment calls I am least certain of**: (1) whether `VX-LIQUID-6.06` BCRED's conjunction structure should be scored N/A (single reported state) vs. a genuine 3-leg escalation ladder — I called it N/A-with-a-flag rather than forcing it into CAN-FIRE/CANNOT-FIRE, since the three "bands" are qualitatively different event types, not one metric crossing cutoffs; (2) whether OSPREY's single-composite VX.tsv row for UKR-01 counts as a "conjunction" in the audit's sense at all, versus a display artifact of a legacy schema — I called it a schema MISMATCH rather than CANNOT-FIRE, since I found no evidence the underlying three-channel scoring (which does live correctly in STATUS.md, per the desk's own CLAUDE.md) is actually blocked from firing — only that the VX.tsv row's shape can't represent it cleanly.
