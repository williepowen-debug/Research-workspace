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

## §1a. Pre-registration defects discovered during execution (amendment, dated 2026-09-25 00:5x ET)

*Written after PROME relayed a CATO peer-read (`AGENTS/CATO/runs/2026-09-24_2343_six-desk-context.md` §SG1/§SG2, commit `c93a66608`; PROME verified SG1 at my own saved CSVs before sending). §1 above stays verbatim per PROME's ask; this section names what §1 got wrong and what the re-cut §4-§6 reflect.*

**Defect A — the metric line and the baseline line don't share a clock.**
- §1 says the per-event metric is "percent change of each vs T-1 (session before the 2d window began)". The v1 implementation computed `VIX[T+k] / VIX[T-1] − 1` — a (k+1)-session return that INCLUDES the event-day co-movement.
- §1 says the baseline is "median forward VIX change over ALL sessions in the same universe (matched for series availability)" — but does NOT specify the return clock. The v1 implementation used `pct_change(k)` = `VIX[T+k] / VIX[T] − 1` — a k-session return.
- **Result:** the v1 cohort's T+1 +12.42% was compared against a T+1 baseline of −0.62% — different windows, not comparable. On matched T→T+k windows the two series are indistinguishable; details in the re-cut §4.
- Class: `finding_verify_reader_before_source` — my own §1 language wasn't unambiguous, and the code diverged from one reading of it silently.

**Defect B — PASS and FAIL rules can be simultaneously true, and §1 registers no precedence.**
- PASS clause (a): VVIX>100 in ≥60% at T+5 AND VIX3M/VIX<1.10 in ≥60% at T+5.
- FAIL: forward VIX <0.5σ separation vs unconditional at ANY T+1/3/5/10.
- Even on the ORIGINAL (mis-windowed) numbers, T+3 was 0.30σ and T+10 was 0.17σ — both under 0.5σ, so FAIL was already met while (a) was passing. On the corrected matched-window numbers, FAIL is met at every horizon (see §4).
- **Result:** the v1 §5 verdict "PASSES on the letter" was a selection of the favourable branch; a rigorous reading of §1 says the rules collided and no verdict was defined. The re-cut §5 discloses the collision and reports both branches separately without selecting one.
- Class: `finding_gate_pass_is_not_evidence_it_found_the_best_reason` — the v1 §5 named a PASS route but did not test whether a FAIL route was simultaneously open.

**Defect C — the study was commissioned by an event that its own cohort did not include.**
- yfinance ^MOVE is **missing the 2026-09-22 bar entirely** — the series jumps 9/21 (81.20) → 9/23 (95.45) → 9/24 (104.58).
- The v1 `identify_cohort()` therefore computed 9/24's `pct_change(2)` as 104.58/81.20 − 1 = 28.79% (below the 30% threshold), and 9/24 was omitted.
- My VIOLET ledger (investing.com PRIMARY) carries 9/22 = 78.56. On that basis 9/24 is 104.58/78.56 − 1 = **33.11%**, and would qualify.
- **Result:** the qualification of 9/24 is basis-dependent. The re-cut §3 discloses both; forward T+k cells for 9/24 don't exist yet regardless, so cohort statistics don't shift, but the report no longer claims coverage through 2026-09-24 without qualifying which source.
- Class: `finding_negative_reachability_is_a_claim_about_your_request` — yfinance rewrote my request silently by not having the 9/22 bar; the cohort scan against the yfinance series returned "not a member" for the event that motivated the whole study.

**Defect D — the low-starting-VIX subsegment stratification in the v1 §5 was NOT pre-registered.**
- §1 registered a whole-cohort verdict and an INCONCLUSIVE-if-n<8 rule for the whole cohort. It did NOT register a "stratify by starting VIX" analysis.
- The subsegment result in v1 §5 is EXPLORATORY. It is kept in the re-cut §5 with that label; it cannot be treated as a pre-registered finding.

**Scope of the amendment:** §1 remains as written (that is the pre-registration record). §4-§6 below are re-cut on the matched-window analysis, with PASS/FAIL collision disclosed, 9/24 basis discrepancy disclosed, and the subsegment analysis labelled EXPLORATORY. The v1 §5 verdict "PASSES on the letter" is WITHDRAWN. The v1 KB row (KB-VIO-311) is being superseded by a corrected KB-VIO-312.

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

## §4. Forward-window results (re-cut on matched clocks — supersedes v1)

*The v1 table under this heading compared a (k+1)-session cohort return (T-1 → T+k) against a k-session unconditional return (T → T+k). §1a defect A. Both clocks are now reported side by side; the σ-separation is on matched T→T+k windows only.*

### CONTEMPORANEOUS RESPONSE (T-1 → T event day)

This is the event-day co-movement — MOVE spiked AND VIX moved on the same close. It is not a forward signal; it is what "MOVE 2d ≥30%" tautologically includes on the event day.

- **Cohort VIX % change T-1 → T0: median +8.91%** (p25 5.5% / p75 19.8%). By construction, unconditional day-to-day median VIX % change is close to 0.
- This is the fact my pass-1 walk-back already established ("MOVE +21.5% & VIX +6.83% on 9/23; MOVE +9.55% & VIX +3.23% on 9/24 — same-day"). The re-cut §4 confirms it as a cohort median across 24 years.

### POST-EVENT forward returns (T → T+k), matched clocks

| Horizon | n | median VIX | cohort VIX %  vs T (matched) | p25 / p75 | vs T-1 (v1, retained for context) |
|---|---:|---:|---:|---|---:|
| T+0 | 10 | 28.13 | **0.00%** by construction | 0 / 0 | +8.91% |
| T+1 | 10 | 28.18 | **−0.58%** | −3.5 / +16.4 | +12.42% |
| T+3 | 10 | 26.51 | **−4.28%** | −13.6 / +3.2 | +3.22% |
| T+5 | 10 | 28.44 | **−7.50%** | −11.1 / +16.3 | +7.95% |
| T+10 | 10 | 26.27 | **−6.28%** | −16.1 / +24.0 | +2.33% |

### Unconditional baseline (matched clock, all 5,901 sessions)

| Horizon | n | median (T→T+k) | p25 / p75 | std |
|---|---:|---:|---|---:|
| T+1 | 5,900 | −0.62% | −3.97 / 3.41 | 7.79 |
| T+3 | 5,898 | −0.68% | −6.47 / 5.96 | 12.88 |
| T+5 | 5,896 | −0.94% | −7.91 / 7.33 | 16.08 |
| T+10 | 5,891 | −1.32% | −10.16 / 9.26 | 20.90 |

### Cohort vs unconditional, σ-separation (matched clock — canonical)

- **T+1: cohort −0.58% vs unconditional −0.62%; σ std 7.79 → separation +0.005σ. Noise, not signal.**
- T+3: cohort −4.28% vs −0.68%; std 12.88 → **−0.28σ.**
- T+5: cohort −7.50% vs −0.94%; std 16.08 → **−0.41σ.**
- T+10: cohort −6.28% vs −1.32%; std 20.90 → **−0.24σ.**

**On matched forward windows, the cohort median VIX % change is at or below the unconditional median at every horizon.** The v1 finding that "T+1 is a +12.4% signal at 1.68σ" was the +8.91% event-day co-movement carried into a two-session return; it is WITHDRAWN.

The v1 whole-cohort claims about VVIX>100 at T+5 (80%) and VIX3M/VIX<1.10 at T+5 (100%) still hold as descriptive facts about the cohort's *state* at T+5. But they no longer support a forward transmission claim; the cohort's forward VIX is not moving above unconditional. Those facts describe events that were already in stress AT T+0 (VVIX median 114 and ratio 0.96 at T+0), not a signature that loaded in advance.

### EXPLORATORY (not pre-registered — §1a defect D): stratification by starting VIX regime

| VIX at T+0 | n | VIX median | ratio median | VVIX median |
|---|---:|---:|---:|---:|
| < 20 | 1 | 14.84 | 1.020 | 70.69 |
| 20–30 | 5 | 26.52 | 1.005 | 114.54 |
| ≥ 30 | 4 | 33.41 | 0.866 | 119.54 |

**9 of 10 cohort events had VIX ≥ 25 at T+0.** Only one event started with VIX < 20 like the current 9/24 setup — 2007-06-08. Its forward path (retained as narrative, n=1, EXPLORATORY):

| horizon | date | VIX | ratio | VVIX | matched % (T→T+k) |
|---|---|---:|---:|---:|---:|
| T+0 | 2007-06-08 | 14.84 | 1.020 | 70.69 | 0.00% |
| T+1 | 2007-06-11 | 14.71 | 1.027 | 68.73 | −0.88% |
| T+3 | 2007-06-13 | 14.73 | 1.024 | 68.81 | −0.74% |
| T+5 | 2007-06-15 | 13.94 | 1.077 | 64.03 | −6.06% |
| T+10 | 2007-06-22 | 15.75 | 1.032 | 78.35 | +6.13% |

Historical note: 2007-06-08 was a rates-only event driven by Bear Stearns hedge fund stress. The next cohort event (2007-08-09 BNP freeze) was 62 trading days later. **This is a single-event narrative, not a base rate.** Any weight it carries for the current 9/24 setup rests on it being the only available analog, not on statistical power.

## §5. Verdict on the intuition thresholds (re-cut — supersedes v1) — HEADLINE per Will 2026-09-25 01:01 ET

### HEADLINE VERDICT (verbatim per Will)

> ***"The corrected ten-event sample does not establish a forward VIX signal in either direction."***

The evidence table and rule-collision disclosure below stand; the headline no longer implies a sign. Under-the-headline language on other surfaces was updated to match this wording; the σ figures remain as evidence, not as directional claim.

### On the letter of the pre-registration — RULES COLLIDE (§1a-B disclosure, kept verbatim)

- **PASS clause (a)** — VVIX > 100 at T+5 in ≥ 60% (observed 80%) AND VIX3M/VIX < 1.10 at T+5 in ≥ 60% (observed 100%): **satisfied**.
- **PASS clause (b)** — T+5 forward VIX ≥ 1σ above unconditional: **not satisfied** (matched: −0.41σ; even under the mis-windowed v1 clock: 0.55σ, still below 1σ).
- **FAIL rule** — forward VIX <0.5σ separation at ANY of T+1/3/5/10: **satisfied at every horizon** on matched clocks (0.005 / −0.28 / −0.41 / −0.24). On the v1 clocks it was also met at T+3 (0.30σ) and T+10 (0.17σ).
- **§1 registers no precedence for PASS-a vs FAIL when both are met. Rules collide. §1a defect B.**
- **The correct disclosure is that the rules collided and neither branch is selected.** The v1 §5 selecting the PASS branch was a retroactive selection of the favourable side.

### Substantive verdict (after honest disclosure of the collision)

**The corrected ten-event sample does not establish a forward VIX signal in either direction.** The "signature-thresholds fire at T+5" fact (PASS-a) is descriptive of cohort STATE at T+5, driven by 9 of 10 events being already in stress at T+0. The FAIL rule captures what the study was actually trying to test — whether the cohort's forward VIX moves distinctly from unconditional — and observes matched-clock separations well within the noise band (T+1 +0.005σ, T+3 −0.28σ, T+5 −0.41σ, T+10 −0.24σ). The evidence does not support a positive forward signature; it also does not support a firm negative claim from n=10 alone. It supports the headline: nothing is established either way from this sample.

### Where the v1 "T+1 +12.4% is real" claim went

**Withdrawn.** The +12.4% was `VIX[T+1]/VIX[T-1] − 1`, a two-session return that includes the +8.91% event-day co-move. On the matched T→T+1 window the cohort median is −0.58%, which the corrected ten-event sample does not distinguish from the unconditional median of −0.62%.

**What CAN honestly be said:** MOVE 2d ≥30% events are *coincident* with a ~+9% VIX event-day co-move (cohort median T-1 → T0). This is not a forward signal and does not license the "MOVE-leads-VIX" framing that the walk-back passes already rejected.

## §6. What replaces the intuition thresholds (re-cut) — HEADLINE per Will

### HEADLINE (verbatim per Will)

> ***"The corrected ten-event sample does not establish a forward VIX signal in either direction."***

### On the STATUS dashboard

**The intuition thresholds (VVIX toward 100, VIX3M/VIX toward 1.10, MOVE ≥ 100) do not have base-rate support** — neither as forward transmission signatures (the corrected ten-event sample does not establish either direction) nor as pre-registered pattern claims (§1 did not register any such thresholds; they were named intuition-first in the 9/24 STATUS/NEXUS_BRIEF that the pass-1 walk-back removed). They stay off the dashboard.

**The v1 "T+1 whole-cohort signal is real" line is WITHDRAWN in all downstream state.**

### RQ #8 status: PARKED (Will 2026-09-25 01:01 ET)

- The main study is CLOSED at this verdict. No further work on RQ #8 itself is scheduled without a new instruction.
- RQ #8a-d (extended cohort, time-to-transmission, setup-vs-amplifier, credit-conditioning) remain **HELD**: registered as candidate follow-ons, none started, none scheduled.
- If any future work reopens the question, it starts on the corrected base (matched clocks, labelled event-day co-move separated from post-event returns, PASS/FAIL precedence explicitly specified in a new pre-registration).

### Facts that survive the correction

1. Between 2002 and 2026, ten MOVE 2d ≥30% events, all named crises (subprime start, BNP freeze, Lehman, Flash Crash, Bund tantrum, COVID, post-COVID election, 75bp hike week, SVB, 2026-03).
2. MOVE 2d ≥30% events are contemporaneously accompanied by an event-day VIX co-move (cohort median +8.91%, T-1 → T0). This is not a forward signal.
3. Post-event, at every horizon T+1 through T+10, cohort forward VIX is not distinguishable from (and slightly weaker than) unconditional.
4. The single analog for the current 9/24 setup (2007-06-08, VIX<20 at T+0) is EXPLORATORY, n=1, and cannot ground a base-rate claim by itself.

### Follow-on studies (retained; NONE started on the corrected base yet, per PROME/CATO)

- **RQ #8a — Extended cohort:** MOVE 2d ≥ 20% (or ≥ 25%) to get more low-starting-VIX analogs. Question: does the "starting-VIX-regime" stratification survive a larger cohort?
- **RQ #8b — Time-to-transmission:** given a low-VIX MOVE spike, what is the median session count until VIX itself moves ≥ 25 (if ever)? The 2007-06-08 → 2007-08-09 gap was 62 td; is that typical, or an artifact of subprime specifically?
- **RQ #8c — Setup vs event:** the pre-committed 3-td de-dup treats each first event as the "setup"; the second event is the "amplifier." Is there predictable structure in T+0 → next-cohort-event timing?
- **RQ #8d — Credit conditioning:** does CCC widening on the MOVE-spike day (like 9/23-9/24) change the forward VIX distribution?

---

**Report data artifacts:** `research/rq8_cohort.csv`, `rq8_forward.csv`, `rq8_cohort_summary.csv`, `rq8_baseline.csv` (re-cut 2026-09-25 with matched-clock columns).
**Reproduction:** `python3 AGENTS/VIOLET/scripts/rq8_study.py`.
**Pre-registration §1 frozen at commit `949fd172b` before §2+ was written; §1a amendment dated 2026-09-25 00:5x ET.**

---

## §7. v1 as shipped — SUPERSEDED (kept for record)

⛔ **EVERYTHING FROM HERE TO END OF FILE IS THE v1 §5/§6 AS ORIGINALLY SHIPPED (2026-09-24 commit `bc33b3861`).** Superseded 2026-09-25 by §4-§6 above and §1a amendment. **Do NOT read the v1 verdict as live.** Retained so the git-log record + §1a class attributions can point at what actually shipped. The PASSES claim below is exactly the retroactive-branch-selection defect §1a-B names; the "opposite direction from my intuition" argument below is the exploratory n=1 subsegment §1a-D names.

*Corrected verdict is: on matched T→T+k forward windows the cohort's forward VIX medians sit at or below the unconditional baseline at every horizon (T+1 +0.005σ, T+3 −0.28σ, T+5 −0.41σ, T+10 −0.24σ); the v1 "+12.4% / 1.68σ at T+1" was the +8.9% event-day co-movement carried into a two-session return. See §5 (re-cut) above.*

### v1 §5. Verdict on the intuition thresholds  ⛔ SUPERSEDED

#### On the letter of the pre-registration  ⛔ SUPERSEDED

**PASSES.** The pre-committed PASS rule required either:
- (a) VVIX > 100 at T+5 in ≥ 60% of cohort AND VIX3M/VIX < 1.10 at T+5 in ≥ 60% — observed 80% and 100% respectively; **PASS**, or
- (b) T+5 forward VIX ≥ 1σ above unconditional — observed 0.55σ, FAIL.

Whole-cohort clause (a) is satisfied.

#### On the honest interpretation  ⛔ SUPERSEDED

**INCONCLUSIVE for the current setup.** The whole-cohort PASS is driven by 9/10 events that had VIX ≥ 25 at T+0 — those events had the "signature" already active on day zero because they were coincident with equity vol stress, not because the signature loaded in advance.

**The pre-committed subsegment INCONCLUSIVE rule (n < 8) applies to the applicable subsegment.** Only 1 of 10 events (2007-06-08) started with VIX < 20 like the current 9/24 setup — n=1 is far below the n=8 threshold, so the base rate for THIS shape is inconclusive on the letter of the pre-registration as well.

#### Substantive read  ⛔ SUPERSEDED

The n=1 analog (2007-06-08) points the OPPOSITE direction from my intuition thresholds:

- I claimed the "signature" was **loading**: watch VVIX toward 100 and ratio toward 1.10 as MOVE holds ≥ 100.
- The one analog had VVIX **fall** from 70.69 to 64.03 and ratio **rise** from 1.020 to 1.077 over T+0 → T+5.
- In that analog, equity vol did not follow rates vol until the next real credit event 62 sessions later.

**This does not prove my intuition wrong** — n=1 cannot prove anything on its own. But it removes the "intuition is directionally right" defense. The one available analog fades rather than confirms.

### v1 §6. What replaces the intuition thresholds  ⛔ SUPERSEDED

#### Concrete replacement for the walked-back thresholds  ⛔ SUPERSEDED

**None this session.** The honest replacement is not another number — it is:

1. On matched forward windows, the MOVE 2d ≥30% cohort does not produce a distinguishable forward VIX signal over 5,901 sessions of universe.
2. The event-day co-movement (~+9% median VIX) is real but tautological — it is what "MOVE 2d ≥30%" contains at T=0, not a signature that loaded in advance.
3. Patient observation of VIX regime changes; the 9/24 STATUS cross-domain read as it stands (spread observation, no lead-lag claim, HENRY/BOND own the rates driver) survives this correction; the "T+1 real signal" line does not.

*(Note on v1 §6: the "Concrete replacement" content above was itself already a partial re-write on peer-read discovery. The point-3 "the 9/24 STATUS cross-domain read... survives this correction" is compatible with the corrected §6; the point-1/2 framing is superseded by the re-cut §4-§6.)*
