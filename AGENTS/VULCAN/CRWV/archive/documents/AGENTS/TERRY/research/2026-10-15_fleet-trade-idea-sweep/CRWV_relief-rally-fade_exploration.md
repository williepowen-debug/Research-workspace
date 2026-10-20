# CRWV relief-rally fade — EXPLORATION (not a card, not a proposal)

**Written 2026-10-15 11:3x ET** (`date`), Will's in-session ask (11:30 ET: "lets explore a CRWV relief rally trade"). Model: Claude Opus 5.5. `$0` · no order · no card registered · no gate moved. Thesis is NOT TERRY's: AI-credit spread/CDS = LIQUID; AI-financing thesis = VULCAN. Construction rules 14–23 read in full before this note.

## Idea
Wait for a relief rally in CRWV while its credit does NOT recover, then buy a defined-risk Jan put spread. The edge claimed is a DIVERGENCE (equity bouncing against unrepaired credit), not the direction. ⚠️ construction rule #15: a price-rally gate opens as the market disagrees more with the bear thesis — the credit leg is what carries thesis information; never read a fire as "the thesis is working."

## Facts (screening, vendor)
- CRWV $62.88–63.13 (11:29–11:31 ET); −28.7% = the 11:29 INTRADAY price vs the 10/1 close (⚠️ corrected 12:4x ET on VULCAN's flag: on CLOSES the strict 10-session move is −24.5% [9/30→10/14], peak-to-trough −28.3% [10/06→10/14]); −55.5% from 1y closing high $141.74 (2025-10-16); 1y closing low $60.82 (2026-07-29). 10/14 −15.46% on 108.5M sh vs ~29.8M 60-day avg.
- Credit (LIQUID via WALTER SIG-W-20261015-005): 2032 notes 77.03 / YTW 15.83% [10/14, HYG fund-eval]; DTCC 5Y CDS model ~1,059–1,120bp [10/14] vs ~840 [10/7]; LIQUID tool `crwv_cds_grade.py` is not ISDA (~7–8bp low).
- Vol: Dec-18 puts IV ~74–89%, Jan-15 ~70–88%; realized RV20 78.2% / RV60 102.0% / RV250 94.5% (n=251) ⇒ not rich vs own history.
- Q3 print date NOT ANNOUNCED (CoreWeave announced Q2 on 7/27 for 8/11; third-party estimates Nov 5–16 / Nov 9 — unverified). Known print reactions: 2025-11-11 −16.3%, 2026-08-12 +19.3% (n=2). Any Dec/Jan expiry spans it.

## Base rate — relief rallies after a ≥25% 10-session drop (CRWV, 390 daily bars since 2025-03-28 IPO; n=6 non-overlapping episodes; SMALL)
| episode | next-20-session max | min | +10% reached on day |
|---|---|---|---|
| 2025-04-16 | +65.6% | −13.0% | 11 |
| 2025-07-18 | +20.9% | −19.1% | 16 |
| 2025-08-21 | +37.5% | −3.6% | 5 |
| 2025-11-11 | +2.6% | −21.7% | never |
| 2026-05-20 | +23.2% | −5.6% | 7 |
| 2026-07-01 | +5.0% | −29.0% | never |
⇒ 4 of 6 rallied ≥10% within 20 sessions (days 5–16); 2 of 6 never did and fell a further 22–29% — the path a fade card MISSES by construction.

## Structures (MODEL, Black-Scholes, entry assumed Thu 10/22, Jan-15-2027 = 85 DTE, inside the 60–90 band; Dec-18 would be 57 DTE, outside it; ATM IV 68–72% with a modest put skew)
| entry spot | Jan 67.5/55P debit | max gain | breakeven |
|---|---|---|---|
| $68 | ~$479 | ~$771 | $62.71 (−7.8%) |
| **$72** | **~$410** | **~$840** | **$63.40 (−11.9%)** |
| $75 | ~$359 | ~$891 | $63.91 (−14.8%) |
Comparator, entering TODAY at live quotes: Jan 60/50P ≈ $402 mid / $425 worst, max ≈ $575–598, breakeven ≈ $55.75 (−11%). ⇒ waiting for ~$72 moves payoff from ~1.4:1 to ~2:1 for similar dollars — that is the measured reason to wait, and its cost is the 2-of-6 straight-down path.
Model mark on 11/20 (IV 75%) for the 67.5/55 bought at $72: CRWV $80 ≈ $270 (−$140) · $72 ≈ $386 · $63 ≈ $581 · $55 ≈ $814 · $50 ≈ $955.

## Draft letter (for a card, if Will/LIQUID/VULCAN want one)
- **Trigger (all, same session):** (a) CRWV regular-session close ≥ $70.00 between 10/16 and 11/04; (b) LIQUID's read of the CRWV 5Y CDS on that session ≥ 1,000bp model (credit NOT repaired); (c) green CRWV session (root rule #6 — a rally day is green by construction).
- **Void:** a close < $58.00 before (a) fires (new low, no rally — the card does not chase).
- **Structure:** 1× Jan-15-2027 put spread, long strike nearest 94% of fill-day spot, short 12.5 lower; net debit ≤ $480 (≤ $500 incl. fees). Leg gate `chain_fetch.py --legs` rc=0 at fill; price off Fidelity's quote.
- **Kill:** CRWV close ≥ $82.00 (10/8 close $81.58 retraced) OR LIQUID CDS < 840bp (pre-scare 10/7) ⇒ sell next session.
- **Harvest (#9):** net bid ≥ 1.8× debit ⇒ sell. **Time stop:** sell by Fri 2027-01-08.
- **N_eff:** shares the credit-recovery falsifier with the bank puts; a broad credit repair hurts both.
