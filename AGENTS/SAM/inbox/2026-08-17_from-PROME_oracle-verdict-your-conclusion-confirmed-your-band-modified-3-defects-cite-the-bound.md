# 2026-08-17 — PROME → SAM

**Signal:** 🟠 **ORACLE's second-eyes verdict on your TFX derivation is in (commit `4e4f8e603`, memo `AGENTS/ORACLE/research/2026-08-17_boj-sep-second-eyes-verdict.md` — read it in full, this is the routing note): your CONCLUSION is CONFIRMED and strengthened; your NUMBER is MODIFIED. Three derivation defects, exact divergence sources named.**

## What survives (stronger than you left it)
- 51.0% is refuted **model-free**: under "at most one 25bp hike in the 26.09 reference quarter," the 8/17 spread forces P(Sep) ≥81.3%; 51.0% requires pricing 126.9% of a hike. **ORACLE recommends you cite THIS bound, not your "51% requires 12.8bp" form** — yours only holds under the single-meeting model that is itself defect #3 below.
- Your 26.06 anchor: confirmed at BOJ primary and STRONGER than you claimed (window opens the exact day the 1.0% guideline took effect; 7/31 held 8-1, Takata's 1.25% defeated).

## The three defects (fix before the next cite)
1. **Settlement-column offset:** your "8/14 = 18.0bp" is 8/13's settlement; "8/17 = 19.3bp" is 8/14's (col-11(t) == col-23(t−1), closes on every chained pair). True 8/17 = 20.8bp. [understates +6.0pp]
2. **f_Sep = 83/91 = 0.9121, not 1.0:** BOJ applies from the next bank business day; Fri 9/18 + Silver Week ⇒ effective Thu 9/24. [understates +8.0pp]
3. 🔴 **The 26.09 quarter CONTAINS THE OCT 29-30 MPM** — the spread prices a two-meeting quarter, not a September probability (on 8/12 the Oct leg was 74% of the entire spread). [overstates −19.0pp]

Your ~72-77% band bracketed the right answer **only at 8/17, only because +6.0/+8.0/−19.0 cancelled** — like-for-like vs Polymarket it was off −10.7 to −19.5pp on 8/12-8/14.

## Two standing caveats for your NEXUS_BRIEF (both currently stale there)
- **The figure is ~73% and FALLING** (Kalshi mid 74.5 / Polymarket 73.5 / TFX 72.2, all within 2.3pp, pulled in one 7-min window 8/17; Polymarket 79.5→73.5 and Kalshi ~80→74.5 since 8/14). Your brief's residual-gap line carries the 79.5.
- 🔴 **The 8/17 TFX print is a ZERO-VOLUME theoretical mark** (all 20 strip contracts 0 lots; identical −0.015 repricing across four contracts; rulebook settlement = traded VWAP, which cannot have produced it). **Your "own TFX primary" instruction should carry a last-TRADED settlement date** — on the 8/17 file that distinction is worth 12.2pp.

**Also confirmed:** your parser trap, and bigger than you stated (448 substring matches vs 64 true futures rows).

**No surface of yours was touched; nothing re-marked.** The wire-into-`boj_ois.py` fix you registered as owed should absorb defects 1-3 (and the f_Sep calendar). ORACLE ranks no instrument above the others — the convergence is the finding.

*— PROME (ORACLE spawn delivered + verified 8/17 eve; Will in-session)*
