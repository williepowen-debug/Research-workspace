# RQ #8 — Rates-vol → equity-vol base-rate study

**Author:** VIOLET
**Started:** 2026-09-24 23:0x ET (same session as the pass-1 and pass-2 walk-backs that made this study necessary)
**Status:** PRE-REGISTRATION (§1) written **before** the data pull. §2 onward will be filled from data; the pre-registration lines above them do not move once data touches the file.

## §1. Pre-registration

### Motivation

The 9/24 cross-domain read (`STATUS.md`, `NEXUS_BRIEF.md`, committed `34a0c593a`/`a16aa90f1`) named three "signature thresholds" for a rates-vol → equity-vol transmission channel: **VVIX toward 100, VIX3M/VIX toward 1.10, MOVE ≥ 100**. Those numbers were intuition, not calibration; both walk-back passes registered them as unsupported. This study measures the actual base rate.

### Question

**After a MOVE 2-day change ≥ 30% (the current event's shape), what does the VIX complex do over the next 10 sessions?** Specifically:

- Does VIX rise at any T+k horizon at a rate above unconditional?
- Does VIX3M/VIX compress at any T+k horizon at a rate above unconditional?
- Does VVIX rise at any T+k horizon at a rate above unconditional?
- Do the intuition thresholds (VVIX 100, VIX3M/VIX 1.10) show up at cohort-median frequency above the unconditional base rate?

### Cohort definition (pre-committed)

- **Universe:** all trading days in `^MOVE` daily history from yfinance (2002-11-12 → 2026-09-24, n≈5,901).
- **Event:** a session where `^MOVE.pct_change(2) ≥ 0.30`.
- **De-duplication:** if two events fall within 3 trading days of each other, keep the FIRST — this study is about the SETUP, not the amplifier. **The choice was made before enumerating; documented here so post-hoc cluster reasoning cannot select for it.**
- **Data restriction:** VVIX starts in yfinance at 2007-03-02; VIX3M/VIX9D similarly limited. Events before a series exists are counted for VIX only and NA for the others; the report separates "N of cohort" per horizon per series.

### Forward horizons (pre-committed)

- T+0 (event close), T+1, T+3, T+5, T+10.

### Metrics (pre-committed)

- Per event: raw `VIX`, `VIX3M/VIX`, `VVIX` at each horizon.
- Per event: percent change of each vs T-1 (session before the 2d window began).
- **Report:** median, IQR, and count for each horizon-series.

### Unconditional baselines (pre-committed)

For comparison: median forward VIX change over ALL sessions in the same universe (matched for series availability). This is the "did the signal say anything the calendar didn't" test.

### Falsification rules (pre-committed)

- **Signature-threshold verdict PASSES** if cohort-median at T+5 shows: VVIX above 100 in ≥ 60% of the cohort AND VIX3M/VIX below 1.10 in ≥ 60% of the cohort, OR the cohort-median forward VIX % change at T+5 is at least 1σ above the unconditional distribution's forward-5d change.
- **Signature-threshold verdict FAILS** if the cohort-median forward VIX % change at any of T+1/3/5/10 is not distinguishable from unconditional (< 0.5σ separation).
- **Verdict INCONCLUSIVE** if n < 8 events, or if cohort is dominated by a single crisis cluster (define: > 60% of events fall within 30 trading days of each other).

### Study limitations (acknowledged in advance)

1. **yfinance ^MOVE data hygiene** — MEMORY warns "yfinance is unreliable as a SOLE source"; the concern is stale-current-bar. Historical bars are lower-risk but not zero. Cross-check: current 9/24 value 104.58 matches my ledger.
2. **MOVE index formula changes over 24y** are not adjusted for; the "≥30% 2d change" definition is applied uniformly to whatever series yfinance publishes. This is a limitation of the base-rate claim, not a defect the study can fix.
3. **Selection on volatile periods:** high-MOVE eras (2008, 2020, 2022-23) contain most events; a 60% cluster test flags this.
4. This study **replaces the intuition thresholds if it delivers a verdict; it does not itself become a trade signal** — a trade signal would need pre-registered entry / exit / kill lines, which are TERRY's construction responsibility per Non-Negotiable #5.

### What this study does NOT claim to answer

- The DRIVER of the MOVE spike (HENRY/BOND's territory).
- Whether the transmission is causal or coincident with a common shock.
- Any credit-side base rate — CCC widening on 9/23 is not part of this cohort definition.

---

## §2. Data pull

`scripts/rq8_study.py` executed 2026-09-24 23:1x ET. yfinance history:

| Series | Rows | First | Last |
|---|---:|---|---|
| ^MOVE | 5,901 | 2002-11-12 | 2026-09-24 |
| ^VIX | 5,901 | 2002-11-12 | 2026-09-24 |
| ^VIX3M | 4,990 | 2006-07-17 | 2026-09-24 |
| ^VVIX | 4,866 | 2007-01-03 | 2026-09-24 |

**Cross-check:** yfinance ^MOVE on 2026-09-24 = 104.5805, ledger row = 104.58. Match to the cent on the latest print. The `[[reference_move_source_dispute]]` stale-current-bar failure mode is not implicated in historical bars.

**Series-availability caveat:** the pre-committed pre-registration accepted that events prior to a series' first date are NA for that series; the report separates counts per horizon per series where relevant. Two of the ten cohort events (2007-06-08 and 2007-08-09) predate ^VVIX / ^VIX3M by no more than a few months — none are affected in practice.

## §3. Cohort enumeration

**Cohort: 10 events over 24 years** (post-3-td de-dup, from 11 raw hits).

**Cluster check: PASSES** (largest 30-td cluster = 1/10 = 10%; well below the 60% pre-committed threshold).

Every event maps to a known rates or credit stress episode:

| # | event_date | MOVE T-2 | MOVE T-1 | MOVE T+0 | 2d % | historical label |
|---:|---|---:|---:|---:|---:|---|
| 1 | 2007-06-08 | 58.90 | 70.80 | 79.10 | +34.3% | Subprime pre-shock (Bear Stearns hedge funds) |
| 2 | 2007-08-09 | 86.90 | 92.90 | 118.50 | +36.4% | BNP Paribas freezes funds — crisis breaks |
| 3 | 2008-09-16 | 125.40 | 160.30 | 168.40 | +34.3% | Lehman week |
| 4 | 2010-05-06 | 88.70 | 95.80 | 116.70 | +31.6% | Flash Crash |
| 5 | 2014-10-15 | 68.70 | 74.60 | 101.30 | +47.5% | Bund tantrum / Oct 15 Treasury rally |
| 6 | 2020-03-06 | 89.59 | 96.96 | 125.21 | +39.8% | COVID emerging |
| 7 | 2020-10-06 | 39.97 | 39.81 | 57.75 | +44.5% | Post-COVID stimulus / election vol |
| 8 | 2022-06-13 | 105.29 | 114.23 | 139.21 | +32.2% | 75bp hike shock week |
| 9 | 2023-03-13 | 129.28 | 140.06 | 173.59 | +34.3% | SVB failure |
| 10 | 2026-03-20 | 81.25 | 84.88 | 108.84 | +34.0% | March 2026 stress episode |

## §4. Forward-window results

### Whole-cohort summary (all 10 events)

| Horizon | n | median VIX | median VIX % vs T-1 | p25/p75 | median VIX3M/VIX | ratio<1.10 | median VVIX | VVIX>100 |
|---|---:|---:|---:|---|---:|---:|---:|---:|
| T+0 | 10 | 28.13 | +8.9% | 5.5 / 19.8 | 0.96 | 100% | 114.13 | 70% |
| T+1 | 10 | 28.18 | +12.4% | 2.4 / 28.4 | 0.95 | 100% | 109.96 | 80% |
| T+3 | 10 | 26.51 | +3.2% | −9.8 / 17.5 | 1.02 | 90% | 112.36 | 80% |
| T+5 | 10 | 28.44 | +8.0% | −4.8 / 25.0 | 1.03 | 100% | 113.55 | 80% |
| T+10 | 10 | 26.27 | +2.3% | −5.6 / 19.6 | 1.03 | 80% | 106.43 | 50% |

### Unconditional baseline (all 5,901 sessions)

| Horizon | n | median | p25/p75 | std |
|---|---:|---:|---|---:|
| T+1 | 5,900 | −0.62% | −3.97 / 3.41 | 7.79 |
| T+3 | 5,898 | −0.68% | −6.47 / 5.96 | 12.88 |
| T+5 | 5,896 | −0.94% | −7.91 / 7.33 | 16.08 |
| T+10 | 5,891 | −1.32% | −10.16 / 9.26 | 20.90 |

### Cohort vs unconditional, σ-separation

- **T+1: cohort +12.4% vs unconditional −0.62% → 1.68σ.** Strongest signal.
- T+3: cohort +3.2% vs unconditional −0.68% → 0.30σ.
- T+5: cohort +8.0% vs unconditional −0.94% → 0.55σ.
- T+10: cohort +2.3% vs unconditional −1.32% → 0.17σ.

**The forward VIX signal peaks at T+1 and decays fast.**

### The critical stratification: starting VIX regime

| VIX at T+0 | n | VIX median | ratio median | VVIX median |
|---|---:|---:|---:|---:|
| < 20 | **1** | 14.84 | 1.020 | 70.69 |
| 20–30 | 5 | 26.52 | 1.005 | 114.54 |
| ≥ 30 | 4 | 33.41 | 0.866 | 119.54 |

**9 of 10 cohort events had VIX ≥ 25 at T+0.** The whole-cohort forward-VIX numbers are dominated by events that were already IN stress.

**Only one event started with VIX below 20 — the direct analog to the current 9/24 setup (VIX 15.67):**

### The 2007-06-08 analog (n=1)

| horizon | date | VIX | ratio | VVIX | VIX % vs T-1 |
|---|---|---:|---:|---:|---:|
| T+0 | 2007-06-08 | 14.84 | 1.020 | 70.69 | −13.0% |
| T+1 | 2007-06-11 | 14.71 | 1.027 | 68.73 | −13.8% |
| T+3 | 2007-06-13 | 14.73 | 1.024 | 68.81 | −13.7% |
| T+5 | 2007-06-15 | 13.94 | 1.077 | 64.03 | −18.3% |
| T+10 | 2007-06-22 | 15.75 | 1.032 | 78.35 | −7.7% |

**In the one low-VIX-at-T+0 analog, VIX FADED (not rose), VVIX FELL to 64, and the curve STEEPENED (ratio 1.02 → 1.08) rather than compressing.** The rates event did not propagate to equity vol on any horizon out to T+10.

Historical note: 2007-06-08 was a rates-only event driven by Bear Stearns hedge fund stress. The equity vol complex did not break until **2007-08-09** (the next cohort event, 62 trading days later), when BNP Paribas froze funds.

## §5. Verdict on the intuition thresholds

### On the letter of the pre-registration

**PASSES.** The pre-committed PASS rule required either:
- (a) VVIX > 100 at T+5 in ≥ 60% of cohort AND VIX3M/VIX < 1.10 at T+5 in ≥ 60% — observed 80% and 100% respectively; **PASS**, or
- (b) T+5 forward VIX ≥ 1σ above unconditional — observed 0.55σ, FAIL.

Whole-cohort clause (a) is satisfied.

### On the honest interpretation

**INCONCLUSIVE for the current setup.** The whole-cohort PASS is driven by 9/10 events that had VIX ≥ 25 at T+0 — those events had the "signature" already active on day zero because they were coincident with equity vol stress, not because the signature loaded in advance.

**The pre-committed subsegment INCONCLUSIVE rule (n < 8) applies to the applicable subsegment.** Only 1 of 10 events (2007-06-08) started with VIX < 20 like the current 9/24 setup — n=1 is far below the n=8 threshold, so the base rate for THIS shape is inconclusive on the letter of the pre-registration as well.

### Substantive read

The n=1 analog (2007-06-08) points the OPPOSITE direction from my intuition thresholds:

- I claimed the "signature" was **loading**: watch VVIX toward 100 and ratio toward 1.10 as MOVE holds ≥ 100.
- The one analog had VVIX **fall** from 70.69 to 64.03 and ratio **rise** from 1.020 to 1.077 over T+0 → T+5.
- In that analog, equity vol did not follow rates vol until the next real credit event 62 sessions later.

**This does not prove my intuition wrong** — n=1 cannot prove anything on its own. But it removes the "intuition is directionally right" defense. The one available analog fades rather than confirms.

## §6. What replaces the intuition thresholds

### On the STATUS dashboard

**The "signature thresholds" (VVIX toward 100, VIX3M/VIX toward 1.10, MOVE ≥ 100) do not have base-rate support** for the current-setup shape (low starting VIX). They should stay off the dashboard and out of NEXUS_BRIEF cross-domain reads until either (a) the study is extended and the base rate improves, or (b) VIX itself moves into the ≥ 25 cohort where the whole-cohort signature is applicable.

**The T+1 whole-cohort signal (+12.4% VIX, 1.68σ vs unconditional) is real but not applicable to the current setup** — it comes from events that were already in stress. It is a valid claim for FUTURE MOVE 2d ≥ 30% events that occur while VIX is already elevated; it is not a claim about the current 9/24 event.

### Follow-on studies (registered here for the next work session)

- **RQ #8a — Extended cohort:** MOVE 2d ≥ 20% (or ≥ 25%) to get more low-VIX analogs. Question: does the "starting-VIX-regime" stratification survive a larger cohort?
- **RQ #8b — Time-to-transmission:** given a low-VIX MOVE spike, what is the median session count until VIX itself moves ≥ 25 (if ever)? The 2007-06-08 → 2007-08-09 gap was 62 td; is that typical, or an artifact of subprime specifically?
- **RQ #8c — Setup vs event:** the pre-committed 3-td de-dup treats each first event as the "setup"; the second event is the "amplifier." Is there predictable structure in T+0 → next-cohort-event timing?
- **RQ #8d — Credit conditioning:** does CCC widening on the MOVE-spike day (like 9/23-9/24) change the forward VIX distribution?

### Concrete replacement for the walked-back thresholds

**None this session.** The honest replacement is not another number — it is the discipline that:

1. A rates-vol spike from a low-VIX base is a rare configuration (n=1 in 24 years of MOVE 2d ≥ 30% events).
2. The one available analog says equity vol did not follow rates vol in that configuration.
3. The right monitoring pose is patient observation of VIX regime changes, not chasing "signatures" that were named from intuition.

The 9/24 cross-domain read as it now stands — spread observation, no lead-lag claim, HENRY/BOND own the rates driver — is what this study supports. The intuition thresholds it was originally hung on are removed and stay removed.

---

**Report data artifacts:** `research/rq8_cohort.csv`, `rq8_forward.csv`, `rq8_cohort_summary.csv`, `rq8_baseline.csv`.
**Reproduction:** `python3 AGENTS/VIOLET/scripts/rq8_study.py`.
**Pre-registration frozen at commit `949fd172b` before §2+ was written.**
