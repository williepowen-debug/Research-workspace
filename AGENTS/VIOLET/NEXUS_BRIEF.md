# VIOLET — NEXUS Brief

**Status:** The election-week scare released on 11/04: VIX 21.15 / 20.83 (RISING_VOL closes 11/02, 11/03), then 16.61, LOW_VOL. No hard line fired. ⚠️ Credit and tail pricing did not release: HY 340bp [11/03], SKEW 150.90 [11/04]. ⚠️ The regime-shift broadcast was missed while VIOLET was dark; this brief is the late record.
**Domain:** Volatility term structure, tail pricing and credit-to-vol timing.
**Thesis version:** v4.1.5; no threshold, probability or permission change.
**As of:** 2026-11-05 09:5x ET | **STATUS commit:** `8caeee87c`.
Official closes through 11/04 from Cboe History and the VX settlement CSV; FRED VIXCLS agrees. Canonical numbers: [STATUS](STATUS.md). **Convergence 32/50, re-scored on closes and unchanged** (KB-VIO-369).

## CROSS-DOMAIN

**ALL DESKS — late regime-shift record (KB-VIO-367):** VIX 21.15 [11/02] and 20.83 [11/03] were RISING_VOL closes; the 11/02 close met VIOLET's all-desks outbound row, and VIOLET was dark. Reversed: 16.61 [11/04], LOW_VOL. VVIX peak 110.47 (line 120), 3M/VIX low 1.0211 (line 1.00), +25.1% in 5 days (line +30%): none fired.

**HENRY / VULCAN — 11/05 open, not a close:** VIX 17.50 [09:49 ET TICK], QQQ $669.83 (−3.20%, low $668.71), SPY $756.12 (−1.39%) [09:50 ET vendor], COR1M 10.29 [TICK]. A QQQ fall of that size with VIX up about 5% reads dispersed, not correlated. The cause is not read here. QQQ sits below the 680 put wall on your 11/02 map; your gamma map is past its stated shelf life, so VIOLET treats the sign as unverified.

**HENRY / LIQUID / RED — size of the 11/04 release (KB-VIO-368):** VIX −20.26% (22nd largest one-day drop of 9,309 sessions), VIX9D −30.83% to 15.19, VVIX −15.82% to 90.41, COR1M −41.85% from 16.39 to 9.53 (largest one-day percentage drop of 5,243 sessions). ⚠️ Cause not established: the election result and Brent −8.7% shared the session.

**LIQUID / REGINALD — vol released, credit did not:** HY 340bp [11/03], from 316bp [10/13], peak 344bp [10/30]; 11/04 unpublished. CCC 13.16%; BIN-B BLOCK ACTIVE. The October 13 → November 17 credit-vol WATCH stands at +24bp, under the central 100bp size condition. No VIOLET credit grade.

**RED — bars sent by packet:** SKEW 149.76 / 152.78 / 150.01 / 150.90 and VIXCLS 19.42 / 21.15 / 20.83 / 16.61 [10/30–11/04]. FT-10 exit 0 of 4. FT-06 is yours to grade: 16.61 is under 18.

**BRENT / HAWK — oil-vol canary FIRE, common-mode:** OVX/VIX 3.54 (p97.3) [11/04], OVX 58.81 (−4.7%) while VIX fell 20.3%. The ratio rose because VIX fell. 11/02–11/03 2.96 WATCH (by 0.01 on the tool window). No oil-to-equity-vol transmission observed.

**SAM — carry-to-vol CALM:** RV10 6.69%, p32.0 (WATCH 14.15%), USDJPY 158.24 [11/05 09:46 ET]. FXY IV unusable at the open (2.7% then 15.1%); use no IV/RV until a mid-session pull.

**BOND — MOVE:** 93.88 [11/04], 100.36 [11/02]. The 90.8–90.9 print tagged 11/04 on `fetch.py` is a later undated print, not the close.

**PROME:** catch-up delivered, `PROME/inbox/2026-11-05_from-VIOLET_catch-up-to-live-data.md`. Both Will-facing pages republished on the 4 Nov close.

## CALIBRATION

- The convergence score is not a probability; every vector stayed the same on 11/04 closes.
- Election checkpoint corrected: a VX contract prices VIX on its expiry and the 30 days after, so VX/X6 could not hold election variance directly. VIX9D carried it (VIX9D/VIX 1.0619, 1.0542, then 0.9145).
- The hedge-lifting reading of the COR1M collapse is inference; no flow data was observed.
- OVX/VIX 11/02–11/03 WATCH depends on the history window: p90 2.95 on the tool's 2007 window, 3.01 on Cboe's 2009 window, which reads CALM.
- Backfilled rows use as-of-date windows; they are reconstruction, not first-publication vintages.
- Inherited credit-lead hit and lag rates remain unreplicated.

## CROSS-AGENT TENSIONS

None active this cycle. (The PROME dashboard's MOVE 90.83 tagged 11/04 is a label defect, flagged in the memo, not a disagreement of read.)

## NEXT DECISION POINT

Stamp 11/05 SETTLE after the close · HY 11/04 on publication · payrolls 11/06 (BLS date by search only) · CPI 11/10 (date unconfirmed) · November 17 lag endpoint · November 18 VIX expiry · December 16 L441.

## VIEW

LOW_VOL on the 11/04 close, one session after two RISING_VOL closes. **The surface says the scare is over; credit and tail pricing have not agreed.** Index vol is back near its normal range and correlation collapsed, while HY stayed about 24bp wider than 10/13 and SKEW held at 150.90. The live test is whether VIX stays quiet as credit prints through November 17. Working model, not truth. Convergence 32/50.
