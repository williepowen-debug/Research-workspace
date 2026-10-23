# HENRY → PROME: KRE/QQQ transition signature (Will's 14:26 ET question)

**Written 2026-10-23 14:37 EDT (`date` 14:37:33).** PROME-spawned, read-only. No card, no gate, no threshold, $0 moved. Data: yfinance closes (vendor, not exchange-official) through the **10/22** definitive close; HY OAS from FRED (pre-2023 history from VIOLET's archived FRED pull, exact match on the 645-day overlap). Full tables are in `PROME/reports/2026-10-23_kre-qqq-transition-signature/REPORT.md`, with `episodes.csv` and `build.py` beside it.

## The signature (nine joint declines, snap-anchored at the KRE+QQQ basket high)
1. **They start in lockstep, not from a see-saw.** 20-day correlation on day 0 was a median **+0.57** (range −0.02 to +0.71) and changed **+0.00** over the prior 10 sessions. It was negative in **0 of 9**.
2. **The starting state is calm:** VIX median **14.6** and falling (5-session change −0.74, 7 of 9 at ≤0); HY OAS flat (10-session change −6bp, 8 of 9 at ≤ +8bp); KRE already lagging (KRE/QQQ ratio −4.2% off its 20-session high); QQQ near its high (up over 10 sessions in 7 of 9).
3. **Then:** VIX jumps a median **+2 sessions** after day 0, the first day both fall ≥1% comes at **+3** (correlation that day +0.62), and HY OAS widens at **+6.5** (before day 0 in only **2 of 9**: credit lagged the equity break). In the first 10 sessions KRE fell a median **−9.0%** and QQQ **−1.6%**; only 20% of days went opposite ways.
4. **Nothing reliably moves first.** Each indicator's onset rate in the nine matches its rate in a random window (10-year 8/9 vs 87%, VIX 9/9 vs 76%, ratio 8/9 vs 84%). The common thread is a STATE, not a TRIGGER.
5. **The only see-saw-to-lockstep case is July 2024**, which is not one of the nine. KRE fell 10.2% and QQQ 7.6% over 7/31 → 8/5, and both were up again within 60 sessions.

## Current regime score (10/22 close)
**8 of 12 measures fall inside the nine-episode range. The 4 outside are the defining ones:** correlation **−0.24** (nine-episode minimum −0.02) · opposite-sign days **80%** of the last 10 (maximum 60%) · QQQ **−5.8%** over 10 sessions (worst −3.5%) · 10-year **−0.14** over 5 sessions (lowest −0.09). Credit and volatility are already moving: HY OAS **3.40%**, up 25bp in 10 sessions and up **74bp** from 2.66 on 9/21; VIX **19.03**, above 8 of the 9. **This is the July 2024 shape with more credit stress, not the eve of a classic joint decline.** ⚠️ The negative correlation is **one close old**; PROME's "−0.24 to −0.26 since 9/25" is wrong (the range was −0.24 to +0.21; −0.258 is the 10/23 intraday value), confirming TERRY's 13:4x correction.

## Early-warning read
Chance of a joint ≥10% decline starting within 20 sessions of a random day: **10.6%**. **Best read: KRE up ≥4% and QQQ down ≥3% over 10 sessions ("banks bid, tech sold"). It fired 18 times with known outcomes: 3 hits (2008-09, 2022-01, 2022-02) and 15 false positives, a precision of 17% (1.6× chance).** Chance alone gives 3 or more hits about 30% of the time, and the rule was picked after seeing the episodes. **It fired at the 10/22 close (outcome pending).** Its nearest miss, 2024-07-19, was the August 2024 drop. The best rule declared in advance (KRE/QQQ ratio ≥4% off its 20-session high and QQQ down ≥3% over 5 sessions): **34 false positives in 40**, 15%. The "see-saw ends" reads did worst: **1 hit in 21 alarms**.

## For Will's book (plain words; detail in REPORT § What this means)
"Hold through the lockstep" is **confirmed**: once both fall, they fall together and both legs pay. "Harvest the see-saw, then switch" has **no timing signal**: no measure announces the switch, and see-saws usually fade back to normal without a joint fall. If today follows July 2024, the joint drop is sharp and short (about a week), so harvest it rather than hold for a long decline. TERRY constructs any trade; this is not an expiry prompt.

## COMPLETION — HENRY — 2026-10-23
STATUS: ✅ DONE
CHANGED: PROME/reports/2026-10-23_kre-qqq-transition-signature/{REPORT.md, episodes.csv, build.py} · PROME/inbox/2026-10-23_from-HENRY_kre-qqq-transition-signature.md (all uncommitted, per the brief; PROME commits)
RESULT: Nine joint declines (PROME's set, reproduced exactly) start from lockstep (c20 median +0.57) and calm (VIX 14.6, OAS −6bp); no indicator leads beyond its random rate. 10/22 is outside the nine on 4 of 12 defining measures and is the July 2024 shape. Best early warning ("banks bid, tech sold", post-hoc): 15 false positives in 18 alarms, 17% vs 10.6% chance; it fired 10/22.
GAPS: n=9, overlapping (2007/08 one crisis); signals S9–S12 post-hoc; other thresholds (−7%, 40 sessions) not tested; HENRY desk write-back (STATUS, KB, MEMORY, NEXUS_BRIEF) not done (read-only brief); WALTER-lane and general-inbox boot triage not run (read-only brief, no consumption allowed).
WILL_NEEDS: None
FOLLOW-UP: HENRY's next writing session: log a KB row; re-examine charter rule H4 ("credit leads equity 2–3 sessions") against the 2/9 result; disposition the 10/22 S12 alarm at +20 sessions (2026-11-19).
