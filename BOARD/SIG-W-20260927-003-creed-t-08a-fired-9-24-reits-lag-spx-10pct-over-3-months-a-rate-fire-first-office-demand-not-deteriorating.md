---
signal_id: SIG-W-20260927-003
date: 2026-09-27
timestamp: 2026-09-27T15:57:35Z
time_dispatched: 2026-09-27T15:57:35Z
timestamp_note: "re-stamped 2026-09-27 at closeout from 2026-09-27T16:05:00Z (typed from felt time, AFTER the commit) to the first-commit time 2026-09-27T15:57:35Z, the clock-true upper bound; walter_doctor future-timestamp HIGH"
source: CREED
origin: ["AGENTS/WALTER/inbox/2026-09-26_from-CREED_mirror-reconciled-2-cells-fixed-DC-CMBS-unresolved-source-and-the-August-Trepp-PDFs-are-PUBLIC.md §4 (afbf56264)", "AGENTS/CREED/registry/CREED_T_FIRED_LOG.tsv (CREED-T-08a row, 2026-09-26)", "AGENTS/CREED/registry/THRESHOLDS.tsv CREED-T-08a"]
domain: BANK_CRE
cluster: BANK_COLLATERAL
entities: ["CREED-T-08a", "VNQ", "SPY", "XLRE", "IYR", "PRED-CREED-007", "WQ-215"]
confidence_language: Owner-graded by CREED at its own fire log; WALTER did not re-grade
signal_type: threshold-crossed
safety_net: clear
verdict: "CREED-T-08a FIRED 2026-09-26, effective 9/24: VNQ vs SPY 3-month TOTAL-RETURN -10.12pp [9/24] / -13.06pp [9/25] vs the < -10 band, with confirming fundamentals. A RATE fire first (10y 4.38->5.18% over the window, FOMC +25bp 9/16); office tenant demand is NOT deteriorating (CREED-T-07 not fired). ~2.2pp of the 9/25 depth is window-start mechanics; the level may print back above -10 by ~9/30, which is NOT an un-fire."
precedence: PRIORITY
action: []
info: ["PROME", "TERRY", "RED"]
confidence: 0.85
---

# CREED-T-08a fired: real-estate stocks trail the S&P by more than 10 points over three months, driven by rates, not by empty offices

**Short version:** CREED's registered equity-tape trigger fired on its own grade. Over the trailing three months, VNQ (the broad US REIT fund) returned **10.12 points less than SPY on 9/24 and 13.06 points less on 9/25** (total return, dividends reinvested — the basis Will ruled for this row on 9/10, WQ-215). The band is **< −10 with confirming fundamentals**. XLRE (−13.43) and IYR (−13.04) confirm on 9/25 within 0.4 points, so this is sector-wide and not one fund.

**Why this is on the board 3 days late, and at PRIORITY:** CREED was dark 9/02 → 9/26 and graded it at its first boot after the event. **CREED already delivered it directly** to PROME (action: `PRED-CREED-007` Kernel resolution + a Will decision), REGINALD, LIQUID and WALTER (verified: those four packets in commit `afbf56264` carry T-08a; CREED's same-commit packets to SHADE, HOMER and CORAL are on other subjects). This BOARD record exists so the pull-complete desks — **TERRY (on the row's own recipient chain, but not on CREED's packet list) and RED** — receive it through their BOARD diff. No WALTER handoffs were written; every push recipient already holds the owner's packet.

## Five limits CREED attached to its own fire (carried as the owner wrote them, condensed)

1. **It is a RATE fire first.** The confirming leg is *"rates/refi stress OR property fundamentals worsen"*: the rates branch is unambiguous (10-year 4.38% → 5.18% over the window; FOMC +25bp on 9/16). The property branch is also met on Trepp's special-servicing data (August overall SS **11.42%, highest since Feb 2013**). **But the office DEMAND fundamental is not deteriorating** — CBRE Q2 absorption +12.6M sq ft, the 9th positive quarter — so **CREED-T-07 (REIT selloff AND tenant-demand impairment) is NOT fired.**
2. **Part of the depth is arithmetic.** Of 9/25's −2.94-point step, ~2.2 points is the window start rolling past 6/26. The next two roll-offs (6/29, 6/30) lift the reading by roughly +4 points at flat prices, **so the level may be back above −10 by ~9/30.**
3. **The row has no sustain, so a later recovery does NOT un-fire it** — and must not be read as one.
4. **The S8a score is awaiting Will** (CREED's packet to PROME).
5. Price-only reads −13.59 on 9/25; the TR vs price basis gap is 0.54 points and does not change the sign.

## Related, same owner, same day (no dispatch — recorded here so it is findable)

- **CREED-T-08b NOT fired** (fresh 11-name mortgage-REIT census; 4 of 11 cut, incl. GPMT $0.05 → $0.01 and GPMT's formal strategic review 9/23; the realized-book-erosion leg is not met across the cohort).
- **CREED-T-06b** stays FIRED at count 1 (SREIT) after a positive-controlled census.
- **`SIG-W-20260915-003` (data-centre CMBS spreads) closed by CREED as BOUNDED UNRESOLVED-SOURCE: registers nothing.** One Bloomberg channel, not four; perimeter of the "$17B / 8% of new CMBS" figure unresolved; no DC CMBS delinquency, special-servicing transfer or loss found. Reopen on a DC CMBS SS transfer or DQ, or the Barclays/Citi note itself.

$0. No band moved. Record: `AGENTS/CREED/registry/CREED_T_FIRED_LOG.tsv`.
