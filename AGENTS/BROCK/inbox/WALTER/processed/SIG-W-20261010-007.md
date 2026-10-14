---
signal_id: SIG-W-20261010-007
date: 2026-10-10
timestamp: 2026-10-10T18:21:25Z
time_dispatched: 2026-10-10T18:21:25Z
timestamp_note: stamped from the system clock at write, not typed
source: WALTER
origin: ["REGINALD signal packet 2026-10-10 (FRED H.8 H8B3094NSMA/DPSSCBW027SBOG/CASSCBW027SBOG/WLCFLPCL, pulled 10/10)", "REGINALD amendment packet 2026-10-10 ~14:1x ET (b680ef50d; H8B3094NSMD/NLGA, FHLBanks Office of Finance monthly debt files through 9/30, preliminary)", "AGENTS/REGINALD/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md", "Will X-bookmark @junkbondanalyst 2108971320377761980 (2026-10-10T17:22Z, chart image)", "FRED BAMLH0A0HYM2/BAMLH0A3HYC WALTER pull 10/10"]
domain: FUNDING_LIQUIDITY
cluster: BANK_COLLATERAL
entities: ["FHLB", "Federal-Reserve-H8", "small-banks", "discount-window", "HY-issuance", "HY-OAS", "CCC-OAS"]
precedence: PRIORITY
action: ["LIQUID"]
info: ["HENRY", "BROCK", "PROME", "RED"]
confidence: 0.8
confidence_language: "H.8 and Office of Finance figures are REGINALD's pulls at the publishers (OF monthly files preliminary); the Q3 advances figure is a fitted nowcast, not a print; the issuance count is one X account, unsourced"
signal_type: research
safety_net: clear
event_window: closed
word_count: 797
dispatch_note: "FUNDING_LIQUIDITY -> LIQUID action. REGINALD sent it as info; whether it enters LIQUID's structural read is a decision assigned to LIQUID, so it sits on action: (BOARD_CONSUMPTION_SPEC 3.5.4). HENRY backup/info; BROCK info (refinancing access). REGINALD originated (own report; no handoff). PROME and RED via BOARD ID-diff (exempt). Will's X bookmark FOLDed here (same lane, same day). No convergence (0 FHLB/H.8 signals 10/5-10/9). LIQUID is dark (last touch 10/9 PM; not in ListAgents; not IN-FLIGHT); no doorbell: weekly series, no dated referent (next H.8 10/16; WQ-414 is Will's, due 10/24)."
---

# Small banks borrowed +$32.9B (+11.7%) in the three weeks to 9/30 with deposits flat. That is the 4th-largest 3-week rise since 2022, behind only the three SVB weeks, and about one-ninth of SVB's first week. FHLB debt rose only +$6.2B in September, against +$54.5B in banks' H.8 borrowings. Q3 FHLB advances nowcast ~$770B, down ~5%. Plus: an X account says junk-bond issuance slowed to 4 deals this week (UNSOURCED); its "+309bp" is the 10/7 FRED print, not the latest

**$0 · no registered threshold fired.** Origin: REGINALD's 10/10 signal packet plus its same-day AMENDMENT, routed together at REGINALD's request (both read whole; the amendment qualifies the original, so the two travel as one card). REGINALD moved nothing.

**1. The datum (REGINALD; Fed H.8 via FRED, last updated 10/9, pulled 10/10).**

| Item | Value | Basis |
|---|---|---|
| Small-bank borrowings (FHLB + other) | 281.6 [9/09] → 286.7 → 298.3 → **314.5 [9/30]** $B = **+$32.9B / +11.7%** in three weeks | `H8B3094NSMA` (SA) |
| Deposits, same banks | 5,674.3 → **5,673.4** (flat, SA); NSA −0.2% | `DPSSCBW027SBOG` / `…NBOG` |
| Cash, same banks | +$21.2B SA but only **+$5.6B NSA**, so the "held as cash" read is **NOT robust** | `CASSCBW027SBOG` / `…NBOG` |
| Discount window (all banks, Wed level) | 5.84 [9/09] → 8.74 [9/30] → 9.97 [10/7] $B, so it explains at most ~$3B of the $33B | `WLCFLPCL` |
| Large banks, same three weeks | **+0.9% SA**: a smaller-bank event | `H8B3094NLGA` |

**2. Scale: read the headline with this attached (REGINALD's amendment, which corrects its own first framing).** "Largest 3-week rise in 160 weeks" is true, but **the 160-week window starts 9/13/2023, after SVB.** Since 12/2022 the move ranks **4th, behind the three SVB weeks**. **SVB's first week was +$290.0B in ONE week** (376.1 [3/08/23] → 666.1 [3/15/23], SA); this is +$32.9B over three. The +11.7% runs from a 9/09 low: **month-end to month-end, small banks were +$17.1B (+5.9%) NSA in September.** The level is still below 2023–24 (~$350–420B). The 12 prior quarter-end weeks ran −4.9% to +1.4%, so this is not the usual quarter-end pattern.

**3. Mostly NOT an FHLB funding surge.** FHLB system debt (Office of Finance monthly files through 9/30, preliminary) rose only **+$6.2B in September**, while banks' H.8 borrowings (small + large, NSA month-end) rose **+$54.5B**. The gap is the 3rd-largest of 41 months (Sep-23 and Jan-24 were similar). ⚠️ **Not yet separable, three candidate causes:** (a) borrowing outside the FHLBs (repo, fed funds, discount window); (b) FHLBanks funding advances from liquidity holdings; (c) large members paying down. **Which banks:** unknown until the Call Reports (11/07).

**4. Q3 FHLB system.** Total FHLB debt **−$42.1B in Q3** ($1,330.8B [6/30] → $1,288.8B [9/30]). REGINALD's fit on 25 quarters ⇒ **Q3 advances ≈ $770B** (three fits $770–778B; range ≈ $728–813B), vs **$810.7B in Q2**, i.e. likely **down ~5%**. Report: `AGENTS/REGINALD/reports/2026-10-10_FHLB_Q3_nowcast_from_OF_debt.md`.

**REGINALD's read (INFERENCE, unchanged in direction):** smaller banks lining up cash in the selloff weeks without losing deposits (a precautionary liquidity build), not deposit replacement and not credit transmission. **What the amendment changed:** the move is small next to 2023, and it did not show up as an FHLB funding surge.

⚠️ **`REG-T-06` (FHLB advances >$700B for 3 quarters) is Will's call under WQ-414, due 10/24.** On REGINALD's nowcast the letter would fire on the Q3 print (~late Oct) in a quarter when FHLB lending shrank. REGINALD is holding its LIQUID/BOND packets on that question until Will rules. **This card does not pre-empt them, and nothing fired today.**

**5. Same lane, same day: junk-bond market access (Will's X bookmark, @junkbondanalyst, 10/10 17:22Z).** *"Spreads are at +309bps, CCCs are 12.5 points wide, and issuance slowed to 4 deals this week."*
- **"4 deals this week" is UNSOURCED.** The account names no source, and one WALTER search found no current-week issuance report. Carry it as a single account's claim. **It is the only element that is new to the board.**
- **The levels are stale and a day apart.** The post's chart ends at **309 = FRED's 10/7 print** (the chart's last three points match FRED's 312 / 303 / 309 for 10/5–10/7). **The latest FRED is 315 [10/8]**, so the post understates HY by 6bp. Its CCC "12.5 points" is FRED's **1,252 [10/8]**. IG 82 matches LIQUID's own 10/8 read. FRED's 10/9 print is not posted yet (Saturday 10/10, ~14:30 ET).

**LIQUID (action):** you decide whether the small-bank borrowing jump (with the scale and FHLB qualifications attached) and the unsourced issuance slowdown enter your funding read. No threshold fired. **Info:** HENRY · BROCK (refinancing access) · PROME · RED. **Next data:** H.8 Fri 10/16 (week of 10/7, the same day as CFG's Q3) · Office of Finance Q3 combined advances ~late Oct · Call Reports 11/07.
