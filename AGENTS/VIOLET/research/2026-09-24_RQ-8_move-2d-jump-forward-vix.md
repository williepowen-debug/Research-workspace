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

*[to be filled in the next step]*

## §3. Cohort enumeration

*[to be filled after data pull]*

## §4. Forward-window results

*[to be filled after cohort enumeration]*

## §5. Verdict on the intuition thresholds

*[to be filled after §4]*

## §6. What replaces the intuition thresholds (if anything)

*[to be filled after §5]*
