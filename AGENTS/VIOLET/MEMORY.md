# VIOLET MEMORY

Curated long-term insights on VIX, volatility regimes, and credit-vol transmission.

---

## CORE PRINCIPLES

1. **VIX is a coincident indicator, not a leading one.** It reacts to realized vol, not predicts it.
2. **But term structure is leading.** Inversion predicts stress before spot VIX spikes.
3. **Credit leads vol.** HY spreads widen before VIX spikes — quantify this lag.
4. **VVIX is the fear gauge for the fear gauge.** When vol-of-vol spikes, something is breaking.
5. **SKEW is the cost of crash protection.** High SKEW = expensive puts = fear present.

---

## REGIME DEFINITIONS

### Low Vol Regime
- VIX 12-20
- Steep contango (VIX3M/VIX > 1.15)
- VVIX 70-90
- SKEW 115-130
- **Duration:** Can persist for months
- **Exit signal:** Term structure flattening, VVIX rising

### Rising Vol Regime
- VIX 20-30
- Contango flattening (VIX3M/VIX 1.0-1.15)
- VVIX 90-110
- SKEW 130-145
- **Duration:** Weeks to months
- **Exit signal:** Term structure inversion or VIX > 30

### High Vol Regime
- VIX 30-40
- Flat to slight backwardation
- VVIX 110-140
- SKEW > 145
- **Duration:** Days to weeks
- **Exit signal:** VIX spike > 40 (crash) or VIX decline < 30

### Crash Regime
- VIX > 40
- Extreme backwardation
- VVIX > 150
- SKEW > 160 (or crashes as puts get monetized)
- **Duration:** Days
- **Exit signal:** VIX mean reversion, backwardation resolves

---

## HISTORICAL ANALOGS (To Research)

### February 2018 — VIX Spike
- **Trigger:** Vol targeting funds, short vol unwind
- **VIX move:** 17 → 37 in one day
- **Credit lead?** TBD — research needed
- **Term structure:** Inverted before spike?
- **Lesson:** Short vol crowdedness → sudden unwind

### March 2020 — Pandemic Crash
- **Trigger:** COVID lockdowns
- **VIX move:** 27 → 82 in 3 weeks
- **Credit lead?** Yes — HY OAS widened first
- **Term structure:** Deep backwardation
- **Lesson:** Macro shock + credit stress = vol explosion

### February 2021 — Meme Stock Vol
- **Trigger:** GME short squeeze
- **VIX move:** 21 → 37
- **Credit lead?** No — idiosyncratic
- **Term structure:** Brief inversion
- **Lesson:** Single-stock vol can bleed into index vol

---

## CREDIT-TO-VOL TRANSMISSION (Four-Model Synthesis — COMPLETE)

**Synthesized from:** Gemini, Perplexity, Claude (native research), Grok

**Core Finding:** Aggregate HY OAS leads VIX by 2-6 weeks at tactical level (100bps widening → VIX spike) and ~7 months at cycle level (trough → peak) when conditions are met.

**Mechanism:**
1. Credit markets price default risk (HY OAS widens) — bond investors face permanent loss, force earlier repricing
2. Equity markets slow to react (VIX flat) — equity retains optionality, complacency persists
3. Realization → equity vol catches up as systematic risk recognized
4. VIX spikes, correlation strengthens

**Why Aggregate HY Leads Even Though Individual Equity Leads:**
- Firm level: Equity leads individual CDS (Norden & Weber 2009, Hilscher et al. 2015)
- Aggregate level: HY OAS captures deterioration across many issuers simultaneously
- Asymmetric news: CDS leads for negative, firm-specific credit info; equity leads for systematic/positive news
- Crisis amplification: Equity hedge ratios increase 3-4× during turbulent periods (Alexander & Kaeck 2008)

**Quantified Lag Times:**
| Regime | VIX Level | Credit Lead Time | Signal Quality |
|--------|-----------|------------------|----------------|
| Extreme complacency | < 15 | 6-16 weeks | **Highest** |
| Low vol | 15-20 | 3-8 weeks | **High** |
| Rising vol | 20-30 | 1-4 weeks | **Moderate** |
| High vol | 30-40 | 0-2 weeks | **Low** |
| Crash | > 40 | VIX leads credit | **None** |

**Hit Rate & False Positives:**
- **Hit rate:** ~70% when all conditions met
- **False positive rate:** 25-30% (unfiltered); 15-20% (with yield curve filter)
- **Main false positive sources:**
  - Sector-specific stress (energy 2015-16) without systemic transmission
  - Technical VIX spikes without credit confirmation (Volmageddon 2018, yen unwind 2024)
  - Rate-driven equity selloffs with healthy credit (2022)
  - Fed QE backstop suppressing credit spreads (2020-21)

**What Breaks the Relationship:**
1. **Exogenous shocks** (COVID) — compress lead time to days
2. **Rate-driven selloffs** (2022, Q4 2018) — VIX leads or coincident
3. **Technical VIX events** (Volmageddon, yen unwind) — no credit component
4. **Fed intervention** (2020-21) — credit spreads artificially suppressed
5. **Crash regimes** (VIX > 40) — relationship inverts, VIX leads credit

**Yield Curve Filter (Claude's Contribution):**
- Fed research (King, Levin, Perli 2007): False positive rates "dramatically reduced" by combining credit spreads with yield curve slope
- 2006 example: Yield curve inversion alone signaled recession (false positive), but adding credit spreads correctly showed low risk
- **Action:** Require yield curve NOT inverted for high-confidence signals

---

## TERM STRUCTURE SIGNALS

### Contango (Normal)
- VIX3M > VIX
- Interpretation: Vol mean reversion expected
- Trade: Short vol (dangerous in stress)

### Flat Contango (Warning)
- VIX3M ≈ VIX
- Interpretation: Vol uncertainty rising
- Trade: Reduce short vol, consider hedges

### Inversion (Alert)
- VIX > VIX3M
- Interpretation: Near-term stress priced
- Trade: Long vol, hedge equity

### Backwardation (Crisis)
- VIX6M > VIX3M > VIX
- Interpretation: Immediate crisis
- Trade: Crisis mode, tail risk protection

---

## VVIX PATTERNS

**VVIX > 120:** Option market stress
- Vol sellers at risk
- Gamma squeeze potential
- Often precedes VIX spike

**VVIX > 150:** Extreme stress
- Vol-of-vol explosion
- Market structure breaking
- 2008, 2020 analogs

**VVIX < 70:** Complacency
- Vol sellers complacent
- Short vol crowded
- Reversal risk high

---

## SKEW PATTERNS

**SKEW > 150:** Fear present
- Crash protection expensive
- Tail risk bid
- Often coincides with VIX > 30

**SKEW < 120:** Complacency
- Crash protection cheap
- Tail risk ignored
- Contrarian buy signal

**SKEW crash during vol spike:**
- Puts get monetized
- Supply of protection overwhelms demand
- Often marks vol peak

---

## KEY RELATIONSHIPS

| Relationship | Normal | Stress | Implication |
|--------------|--------|--------|-------------|
| VIX vs Realized Vol | VIX > RV (risk premium) | VIX < RV (vol shock) | Premium compression = stress |
| VIX vs HY OAS | Correlated | VIX lags | Credit leads vol |
| VIX vs VIX3M | Contango | Backwardation | Term structure predicts regime |
| VIX vs VVIX | Correlated | VVIX leads | Vol-of-vol is early warning |
| VIX vs SKEW | Correlated | SKEW leads | Tail risk pricing predicts spot |

---

## DATA SOURCES

| Source | Data | URL |
|--------|------|-----|
| CBOE | VIX, VIX futures, VVIX, SKEW | cboe.com/tradable_products/vix |
| Yahoo Finance | Historical VIX | finance.yahoo.com/quote/%5EVIX |
| FRED | VIX, credit spreads | fred.stlouisfed.org |
| CBOE LiveVol | Options data | livevol.com |

---

---

## SESSION NOTES

### 2026-04-15 — empirical audit session (PUSH DEFERRED)

**Status at close:** VIOLET has **4 commits staged locally, NOT pushed to GitHub**.

Commit hashes (local master): `69cd3c05 → 8b36c813 → ca48167c → 69cd3c05`
- `69cd3c05` — session tooling + empirical audit — posture 🟡→🟠 ELEVATED WATCH
- `8b36c813` — Mar 27 trigger analysis + catalyst tracking
- `ca48167c` — VIX options positioning tool + first snapshot

**Why push was deferred:** Attempted push was rejected (non-fast-forward). Local was 4 commits ahead, remote had advanced 3 commits from another session while VIOLET was working. Cannot safely `git pull --rebase` because working tree has uncommitted work from CARL, WALTER, OTTO. Protocol (CLAUDE.md "Before pulling") says STOP when other agents have uncommitted changes outside VIOLET's directory.

**Next-session push protocol:**
1. Check git status at boot. If other agents still have uncommitted work, defer again.
2. If working tree is clean outside VIOLET/: `git stash push -- AGENTS/VIOLET/` → `git pull --rebase` → `git stash pop` → `git push`.
3. If stash-pop conflicts, resolve only in VIOLET files. Never touch other agents' conflicts.

**Shared files from this session NOT committed (flagged to Will):**
- `FORGE/tools/market-data/vix_futures.py` — new shared tool, VIOLET-authored. Prome or Will to commit.
- `AGENTS/WALTER/inbox/SIG-VIOLET-WALTER-20260415-vix-apr15-refresh.md` — PRIORITY signal. Will be picked up on WALTER next boot.
- `AGENTS/WALTER/inbox/SIG-VIOLET-WALTER-20260415-002-skew-divergence-escalation.md` — IMMEDIATE signal. Posture change routing.

**Key state for next session:**
- Posture: 🟠 ELEVATED WATCH (revised from 🟡)
- Scenario B (new VIX event within 60d) probability: **66%** (revised from 30%)
- Scheduled checkpoints: **2026-04-29 early** (FOMC day), **2026-06-15 full**
- Tools now daily: `boot.py` runs `thresholds.py` + `vix_options.py` + `catalyst_countdown.py`
- Workbook time series active: `VX_DAILY.tsv`, `VIX_OPTIONS.tsv`, `CATALYSTS.tsv`
- 39 KB entries as of close (1 superseded KB-VIO-019, 1 corrected KB-VIO-023, thesis prediction #2 empirically falsified)

**Open investigation pathways for next session** (user's stated interest — continue digging on VIX calls):
1. Observe Apr 29 C/P OI ratio daily (currently 9.01 — extraordinarily high)
2. IV term structure probe across forward expirations
3. Full strike-by-strike call-wall / put-wall map for May 19
4. CFTC COT VIX futures positioning (weekly, independent data source)
5. Backtest: historical C/P OI ratio on FOMC-day expirations (need data source)

---

*Created: 2026-04-12*
*Last Updated: 2026-04-15 (empirical audit session + posture escalation + push deferred)*
