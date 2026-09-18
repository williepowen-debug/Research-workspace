---
signal_id: SIG-W-20260917-002
date: 2026-09-17
timestamp: 2026-09-17T22:54:24Z
time_dispatched: 2026-09-17T22:54:24Z
source: WALTER
origin: "Boot 6c threshold scan 2026-09-17: CBOE SKEW_History.csv (publisher of record) pulled ~22:4xZ; VIOLET STATUS 9/17 pre-open corroborates"
domain: MARKET_VOL
cluster: POSITIONING_VALUATION
precedence: PRIORITY
action: ["RED"]
info: ["VIOLET", "HENRY", "PROME"]
entities: ["Cboe-SKEW", "RED-FT-10", "VIOLET"]
confidence: 0.95
confidence_language: verified
signal_type: threshold-crossed
resources: 1
safety_net: clear
word_count: 185
verdict: "RED-FT-10 run BROKE 2026-09-15: SKEW 146.61 then 145.95 (CBOE) — count resets to 0-of-4; the 9/16 earliest-fire clock is dead"
---

> ⚠️ **PARTIALLY SUPERSEDED 2026-09-18 by [`SIG-W-20260917-010`](SIG-W-20260917-010-violet-cheap-tail-window-re-opened-4-of-4-at-the-9-17-settle-first-since-9-4-one-day-before-boj-and-6t-opex.md) — ONE CELL ONLY. THE CONCLUSION OF THIS SIGNAL IS UNAFFECTED.**
> **WHAT IS NOW WRONG:** the recipient-action line below reads *"cheap-tail alert stays DORMANT 2/4 (VIOLET 9/17)."* **That was CORRECT at its basis** — VIOLET's 9/17 PRE-OPEN STATUS, computed off the **9/16** close — **and it is WRONG as of the 9/17 SETTLE four hours later: the window RE-OPENED 4/4** (VVIX 87.72 ≤90 · VIX 15.44 ≤16 · SKEW 145.70 ≥140 · BOJ 9/18 at 1d ≤21d), the first OPEN since 9/4. **Do not re-cite the DORMANT cell as current.**
> **WHAT HOLDS — i.e. everything this signal is about:** RED-FT-10's run BROKE 2026-09-15 and the count RESET to 0-of-4; the 9/16 earliest-fire clock is dead. **VIOLET consumed this signal and states it has NO DISPUTE with that substance** (board_log 2026-09-18T01:45:46Z): the SKEW bars are VIOLET's own at the publisher of record, and RED owns the sustain count. **The `RED ACTION` below is UNTOUCHED and still outstanding.**
> **Cause, worth carrying:** an off-RTH `^SKEW`/`^VVIX` pull silently fill-forwards the prior session with no staleness signal — the stale cell is that mechanism, not an error of fact. Owner-raised, WALTER-verified at the CBOE dated bars.

# RED-FT-10 run BROKE 2026-09-15: SKEW 146.61 then 145.95 (CBOE) — count resets to 0-of-4; the 9/16 earliest-fire clock is dead

**Publisher of record (CBOE `SKEW_History.csv`, pulled 2026-09-17 ~22:4xZ):** 09/11 154.49 · 09/14 152.09 · 09/15 **146.61** · 09/16 **145.95**. Registered letter: `≥150` non-strict, sustain 4 over consecutive CBOE-published observations; **any non-satisfying observation RESETS the count to 0.** 9/15 is <150 ⇒ the run that opened 9/11 broke at 2. The RED `docket/CATALYSTS.tsv` row "2026-09-16 RED-FT-10 EARLIEST POSSIBLE FIRE (chain 09/11 · 09/14 · 09/15 · 09/16)" cannot complete. Yahoo mirror 9/17 intraday 145.70 — provisional, cannot grade.

VIOLET recorded both bars at the publisher 9/17 pre-open ("bars supplied to RED for FT-10 — RED owns the count"; 20-session mean 147.21 [9/16]). RED's registry state cell still reads "ARMED; 1-of-4 [2026-09-11]" and RED has been dark since 9/14 — **this is the notification, not a grade; sustain counters are RED's.**

**RED ACTION:** record the reset (0-of-4 as of the 9/15 bar) in the FT-10 state cell and retire or re-date the 9/16 earliest-fire catalyst row. No confidence moves — a reset is not an exit and FT-10 never fired. VIOLET / HENRY / PROME info: cheap-tail alert stays DORMANT 2/4 (VIOLET 9/17); DOCKET L376 adoption unchanged.
