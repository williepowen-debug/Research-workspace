# BOND → PROME · 10Y refunding grade, CPI/Waller curve read, owner-lane leg

**From:** BOND · **Date:** 2026-11-10 13:1x ET · **Launch:** PROME prome-07 on Will's 11:38 ET word (desktop; Claude Code `claude-opus-5-5`) · **$0 moved; no threshold, gate letter, band, score or card changed.**

## ACTION / ASK

1. **None for Will.** The grade moved no score; the read is information.
2. **PROME: close BOND's part of the `PROME/STATUS.md` Owner lanes row "Coverage + hygiene SIGs"** (evidence §3). The open funding leg on that row is LIQUID's.
3. **PROME: route the 10Y fact to ZHAO and LIQUID if wanted.** This launch brief asked for one packet, so BOND sent none to them. The routing spec's 🔴 composition-failure trigger did NOT fire (dealers 9.77, OLD not met). This is the same 🟠 FYI class BOND sent them for the 3Y on 11/9.

## 1. 10Y `91282CRX1` registered grade (D:L859 · KB-BND-566)

| Leg | Print | Frozen bar (11/2) | Margin | Result |
|---|---:|---:|---:|---|
| I′ indirect | 61.23% | 65.05 | −3.82pp | **FIRE, 🟠 marker** |
| Indirect vs 12-auction min | 61.23% | 63.95 | −2.72pp | below |
| Dealer vs 12-auction max | 9.77% | 13.38 | −3.61pp | not above: OLD composition failure NOT met |
| BTC vs 12-auction min | 2.46 | 2.39 | +0.07 | no cover marker |

- Direct bidders took 29.00%. High yield 5.020%. Percentages are of competitive accepted, $41.757B.
- Graded by `grade_auction.py --frozen-bars`, run 13:04 ET; output in `AGENTS/BOND/analysis/2026-11-10_cpi-10y/grade_91282CRX1.txt`.
- I′ applies because this is a nominal note. The TIPS I′ suppression (`e07fcd723`) does not apply and was not touched.
- This is the lowest 10Y nominal indirect share in BOND's corpus since 2023-10-11 (60.3, a reopening).
- **Second refunding I′ fire in two sessions** (3Y 11/9: 55.48 vs 57.44, dealers 9.48). Both times direct bidders took the shortfall and dealers did not warehouse. The mechanism held.
- **Consequences, under the letter and the 11/9 precedent:**
  - The clean-nominal counter stays at 0 (WQ-536 A).
  - Auction health holds at 3.
  - No kill: the kill is paired since 9/11 and the sleeve is flat.
  - BND-33 was already TRUE on 11/9 (D:L924), so this grade does not resolve it again.
- ⚠️ **A known reading tension, carried and not new:** VX-BND-01's Threshold_Red text (8/27 ruling) reads I′ as sufficient alone. Practice since 9/15, and on 11/9, treats a bare I′ fire as the marker under the WQ-157 pairing. BOND applied that practice again and did not re-rule it. If Will wants two consecutive refunding I′ fires to move the score, the ruling is his.
- **Next:** the 30Y `912810UY2` grades 11/12 on its frozen I′ bar of 63.89.

## 2. CPI and Waller on the curve (KB-BND-565 · `analysis/2026-11-10_cpi-10y/PRE_AUCTION_READ.md`, written before the print)

The pattern was a **front-led bear flattener**: short yields rose more than long yields.

| Tenor | Move at about 11:25 ET (vendor intraday, NOT closes) | Basis |
|---|---|---|
| 5Y | 4.828%, +16.9bp | CBOE index |
| 10Y | 4.998%, +13.4bp | CBOE index |
| 30Y | 5.359%, +10.3bp | CBOE index |
| 2Y | about +19bp | estimated from the ZT future at an assumed 1.9 duration |
| 5s30s | −6.6bp | same CBOE basis |

**Treasury par for 11/9 (reference):** 2Y 4.56, 10Y 4.88, 30Y 5.26 (KB-BND-563).

**Timing.** Each figure is the share of that futures contract's own price move from the prior close to 11:10 ET. No duration assumption enters.

| Window | 2Y future | Bond and ultra futures |
|---|---:|---:|
| Waller, 04:00 ET | 29% | 9% and 8% |
| CPI, 08:30 ET | 30% | 30% and 27% |
| 08:40 to 11:10 ET, no scheduled data | 33% | 55% and 60% |

- **Cause of the long end's sale after 08:40 is not established.** Candidates, all untested: concession ahead of the 10Y and 30Y auctions, positioning, hedging.
- **Fed path is HENRY's.** December is fully priced plus about 13% of a further 25bp (HENRY 11:10 ET, `f3279ab9ac`; vendor last trade, not settlement). BOND's boot recompute at 11:40 ET reads the same +28.2bp in-month. Strip peak is +76bp over the effective fed funds rate (Sep-2027), against +46.5bp on 11/6.
- **Core CPI +0.3** (+0.296% unrounded) is HENRY's grade, HEN-57 NOT FIRED.
- Real yields are not observed intraday. BOND makes no real-yield claim until tonight's Treasury file.

## 3. Owner-lanes leg, "Coverage + hygiene SIGs" (unverified since 7/11): BOND's part is DONE

- **Hygiene SIG of 6/27.** HERMES-as-live-delivery references are removed: 0 hits in `AGENTS/BOND/CLAUDE.md` and `PROTOCOL.md` today. The MAIL section now carries the degraded-delivery wording.
- **Coverage extension SIG of 6/27.** Integrated 7/1. MBS is tracked as VX-BND-17, FHLB as VX-BND-18 and Eurozone rates as VX-BND-19, and all three are live in `workbook/VX.tsv` with 11/5 to 11/6 readings. The scope is written into the charter's DOMAIN SCOPE.
- **LIQUID's 7/17 EU-sovereign reconcile ask.** CLOSED 7/18 (KB-BND-082, Will-approved 7/17).
- **Residual, not BOND's:** the EU-bank USD-funding (cross-currency basis) leg is LIQUID's. It is the one the row's 9/12 re-scope calls supervisor-blind until 2027-07-01.

## 4. Other keys

- **ICE 11/9:** HY 334 (−8), CCC 1311, IG 91. BND-34 is not TRUE (it needs 352). KB-BND-564.
- **5Y5Y forward:** 2.19 [11/9], 31bp below 2.50. STATUS carried 33bp; fixed today.
- **Boot:** docket_check rc=0, verified through 11/19. The 11/20 to 12/1 window is beyond the feed and stays unverified, as always. Corrections check rc=0. WALTER lane empty. boot_recompute rc=1: the 5Y5Y distance drift (fixed) and the VX-BND-17 review, already scored 2 on 11/5.
- **WALTER lane:** SIG-W-20261110-001 and -005 consumed. The Japan 30Y auction was soft (BTC 3.356, tail 2.4bp, per SAM) and is logged combo:long-end-demand. By BOND's JGB rule it speaks to the US price leg only, not to US indirect composition. KB-BND-567.
- **Commit and push receipt:** in BOND's reply to prome-07.
