# BOND SCRATCH — 2026-11-10 standard closeout (desktop, PROME prome-07 launch); night closeout 19:3x ET on PROME's ask, window closed by Will

> STATE AT WRITING (13:1x ET): Composite **17/35** (5+3+2+3+1+1+2, unchanged). **Clean-nominal counter 0** (3Y 11/9 and 10Y 11/10 registered I′ fires); auction health 3. **OPEN predictions 4 (BND-34 to 37), earliest resolution 12/17.** Position: **FLAT** per the FORGE 10/30 reconcile (last broker capture 10/30 intraday; FORGE stale mirror); WQ-592 declined; NO-ADD WQ280. Latest official cells: Treasury 2Y/10Y/30Y 4.56/4.88/5.26 [11/9]; real 10Y 2.66 [11/9]; 5Y5Y 2.19 [11/9]; Bund 3.29 [11/6]; HY/CCC/IG 334/1311/91 [11/9]; SOFR−IORB +2 [11/5]; FR2004 long-end $146.946B [as-of 10/28]; PMMS 7.18 [11/5]; ACM 0.6428 [11/6]. THESIS v1.2.13, token unchanged.

## WHAT I DID

PROME prome-07 launch on Will's 11:38 ET word (desktop after the machine switch). Limits: $0, no threshold/gate/band/card change, live prices, quiet mode.

- **Boot 11:40 ET:** tree clean, pull no-op (local = origin + 2 unpushed PROME commits); corrections rc=0; docket_check rc=0 (verified through 11/19, blind span 11/20–12/1); WALTER lane empty; boot_recompute rc=1 = T5YIFR distance drift (STATUS 33bp → 31bp, fixed) + VX-BND-17 review (already 2).
- **ICE 11/9:** HY 334, CCC 1311, IG 91; BND-34 not TRUE. KB-BND-564.
- **CPI/Waller read (before the print, file unchanged after):** front-led bear flattener; Waller 04:00 ET = 29% of the 2Y future's move, 8–9% of bond/ultra; CPI ~30% everywhere; bond/ultra 55–60% after 08:40, cause not established. KB-BND-565.
- **10Y `91282CRX1` REGISTERED grade 13:04 ET:** indirect 61.23 / direct 29.00 / dealer 9.77, BTC 2.46, high 5.020. I′ 65.05 → FIRE (−3.82pp); min 63.95 → below; dealer max 13.38 → not above (OLD not met); BTC min 2.39 → no cover marker. Lowest 10Y indirect in corpus since 10/2023. Counter stays 0; health held 3; no kill. KB-BND-566, VX-BND-01, docket rows (CPI + 10Y).
- **Owner-lane leg:** BOND part DONE; asked PROME to close it (packet §3).
- **WALTER lane at closeout (landed 11:45 ET, after boot):** SIG-W-20261110-001 (CPI/Waller, matches KB-BND-565) and -005 (JGB 30Y auction soft, BTC 3.356, tail 2.4bp, SAM; combo:long-end-demand, price leg only) → KB-BND-567, board_log ×2, moved to `inbox/WALTER/processed/`.
- **Night closeout 19:3x ET (PROME ask, Will closing):** SIG-W-20261110-011 (bookmark small items; 10Y 4.98 vendor ^TNX 22:14Z, consistent with KB-BND-565/566; rest not BOND) → KB-BND-568, board_log, processed. No other work.

## NOT MOVED

No score, band, gate or threshold. Composite 17. Token unchanged. ⚠️ VX-BND-01 Threshold_Red text (8/27) vs the 9/15 practice: carried, flagged to PROME, not re-ruled.

## UNPUBLISHED OR UNREAD

Treasury par/real 11/10 (evening) · ICE 11/10 (11/11) · SOFR/EFFR 11/6–11/10 · Bund after 11/6 · KW after 10/30 · FR2004 as-of 11/4 (11/12).

## NEXT SESSION (dated)

1. **11/11 boot (carried from 11/10 evening, window closed first):** Treasury 11/10 par/real close: confirm the intraday read (KB-BND-565) and the vendor 4.98 (KB-BND-568) on official cells; real 10Y on a CPI/hike-repricing day.
2. **11/12:** **30Y `912810UY2`** registered grade: `.venv/bin/python monitors/grade_auction.py --cusip 912810UY2 --frozen-bars AGENTS/BOND/registry/auction_bars/2026-11-12_912810UY2.json` (from AGENTS/BOND); bars 59.95 / 14.74 · BTC 2.29 · I′ 63.89. PMMS re-scores VX-BND-17; FR2004 as-of 11/4.
3. 11/11 VX-20 review; 11/12–11/17 freeze 20Y (11/18) and 10Y TIPS (11/19) bars; 11/13 FHLB CFR, L226, FRBNY FX report; 11/17 F2 op 20–30Y; 11/19 freeze month-end bars.
4. Before 12/2: register any 12/9 curve-shape row with a base rate. R1, R5 and the shared-HEAD digest defect still to Will / CATO-DAEDALUS.
5. Check BND-34 and BND-37 for early TRUE at each read. 12/17 BND-36; 12/31 BND-34, 35, 37.

## OPEN THREADS

Whether two consecutive refunding I′ fires should move auction health is Will's ruling if he wants it (packet §1 ⚠️). L226 FHLB retune waits on 11/13. 7Y reopening handling before April 2027. True CDX, pulled-deal census, private funding, event-time TIPS unchanged. WQ291 funding window UNGRADED. FR2004 confirmation legs for the 3Y/10Y fires not graded (settle 11/16; position flat). BLS 403 here.

## CLOSEOUT STEPS (standard)

C1 STATUS done (top line, frontiers, auctions + rates paragraphs, dashboard 5Y5Y/HY, auction table, gates, matrix, catalysts, bottom line) · C2 KB 564, 565, 566, 567, 568; VX-BND-01; FLOW no-op; no row past Stale_By flipped (none newly due found) · C3 no-op, none due, no owed row · C4 no-op, token unchanged · C5 CPI and 10Y rows marked; STATUS twin updated · C6 TRADE no-op, no gate or position change · C7 this file · C8 RECEIPT rewritten; board_log 3 rows (SIG-W-20261110-001, -005, -011) · C9 no new lesson · C11 NEXUS_BRIEF re-pinned last.

## POSITION

FLAT on this thesis. BOND executes nothing; no expiry reminders.

## MAIL / DELIVERY

Sent: `PROME/inbox/2026-11-10_from-BOND_L859-10Y-graded-I-prime-fire-CPI-read.md` (carve-out ①). No ZHAO/LIQUID packets (one-packet brief; PROME asked to route). One-line SendMessage to prome-07 with the push receipt.
