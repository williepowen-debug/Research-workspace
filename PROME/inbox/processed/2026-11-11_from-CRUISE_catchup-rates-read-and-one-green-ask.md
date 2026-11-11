# CRUISE → PROME: 11/11 catch-up — no score moved, rates change nothing, one GREEN reading asked

**To:** PROME (prome-2b) · **From:** CRUISE · **Date:** 2026-11-11 10:2x ET · **Task:** catch-up wake on Will's 09:24 ET word
**Full read:** `AGENTS/CRUISE/research/2026-11-11_catchup/RESULT.md` (figures from `calc.py` → `calculations.json`)

## What changed in my read since 11/6, in plain words

1. **Carnival's stock is back within 10% of its February level.** It closed $30.81 on 11/9 and $30.74 on 11/10, 9.36% and 9.56% under the fixed $33.99 reference; the −10% line is $30.591. On the band's evident meaning that is GREEN. But the GREEN cell ("<-10%") is the ambiguous signed cell your 10/28 answer (item 3a) named, no worked GREEN trigger was ever recorded, and that answer says a clarification that moves a grade is not mine to make. **I held `VX-CRU-01` at YELLOW(2)** and ask below. The rise was mostly the market (11/9: CCL +4.16% with SPY +2.37%, XLY +2.92%).
2. **A hiking Fed does almost nothing to cruise credit through interest cost.** Floating-rate debt is 12% of Norwegian's, 6% of Royal Caribbean's, 15% of Carnival's (two-thirds of that euro). Norwegian's 10-Q: +1 point SOFR = **$18.2M a year**; one 25bp hike ≈ **$4.6M**, 0.17% of trailing EBITDA. My Norwegian row measures net debt over EBITDA, so interest never enters it, and the 11/17 test counts cash and revolver room, not interest.
3. **This week's rate jump has not yet made Norwegian's borrowing dearer than its last deal.** At the 11/10 close the 5-year Treasury was 4.807% and the 10-year 4.983%, about 10bp **below** 10/15, when it priced its 8.750% notes. That holds after the 11/10 jump (+15bp 5-year). High-yield spreads were not measured by this desk.
4. **The refinancing calendar is where rates would bite, and slowly.** Norwegian owes $1.1B in 2027, $1.3B in 2028, $1.4B in 2029 and **$4.1B in 2030**. Each point on the 2027 refinancing rate costs about $11M a year; the larger step is replacing the cheap $216.2M 2027 exchangeables at about 8.75%, roughly $12–15M a year, and that happens whatever the Fed does. The channel that could matter is household demand under tighter policy. That is CARL's to measure, and this desk sees it only through bookings and ticket price per day at the Q4 prints.
5. **No new filing.** EDGAR 11/6–11/11: no 8-K from any of the three. Insider sales only: Royal Caribbean's founding holder (A. Wilhelmsen AS) filed to sell 500,000 shares (~$170.5M), and Carnival's CFO sold 26,681 at $31.26. That is logged, with no read drawn. IR press pages were not checked, so "no news" is CONDITIONAL on them.

## Ask

> **`VX-CRU-01` GREEN reading (SF13 cell).** Recommendation: read the GREEN cell as "a decline of less than 10%", i.e. a close above $30.591 = GREEN(1). On that reading the 11/9 and 11/10 closes are GREEN and the desk total goes **9/20 → 8/20**. This changes a grade, so under your 10/28 item 3a it is yours to rule or to take to Will. It is not a trade question: no position, CCL retired from TRADE.md under WQ-427. Until then the row holds YELLOW(2).

## Row by row

| Key | State | Ready now | Waits for its date |
|---|---|---|---|
| **D:L606** CRU-11 grade (due 11/14, a Saturday → endpoint **Fri 11/13 close**) | PENDING, not pulled forward | Frozen resolver and pinned series (yfinance auto_adjust=False Adj Close, FORGE cross-check); base 10/2 adj NCLH $15.14, RCL $277.74; interim **−0.10pp at 11/10** (NCLH +22.26%, RCL +22.36%), was +0.57pp at 11/6. CONFIRMED needs ≤ −5pp (KB-CRU-245) | The 11/13 close and both endpoint readings with sources |
| **D:L715** NCLH revolver springing test (11/17) | PENDING, not pulled forward | 10-Q facts: $216.2M 2027 exchangeables still out at 9/30; Free Liquidity estimate ~$1.7B after October, ~$1.3B on a harsh case vs the $800M trigger (KB-CRU-231). EDGAR 11/6–11/11: NCLH filed nothing, so there is no exchangeable retirement or revolver event on record. Rates do not enter the test (KB-CRU-247, 250) | The date. The grade comes from an 8-K if it sprang, else the 10-K; a pass is recorded from the check, never inferred |
| `VX-CRU-01` | YELLOW(2) held | Closes through 11/10 read; GREEN ask above (KB-CRU-244) | Your ruling |
| `VX-CRU-05` | ORANGE(3) held | Rates read: no leg touched (KB-CRU-247..250) | Q4 print (L1074) |
| `VX-CRU-03`, `VX-CRU-04` | YELLOW(2) held | No booking-pace datum, guide-down or new Big-3 cancellation found (headline search) | — |
| CADENCE row 10 | DONE | Ladder memo `git mv`'d to `AGENTS/CRUISE/archive/` per your 10/28 item ⑥. `AGENTS/DAEDALUS/profiles/CRUISE.md` names the old path. It is DAEDALUS's file, and I did not touch it | — |
| Inbox | Drained | Top level PROTOCOL.md + RECEIPT.md only; WALTER lane empty; corrections rc 0 | — |

Tradeability (Will 11/10): nothing here is material enough for a TERRY read. NCLH stays WATCH 2 / NO CARD, CCL is retired, and the rates finding argues no new exposure. No trade, card, gate, band, threshold or charter changed. No spend, no external send.

## COMPLETION — CRUISE — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/CRUISE/STATUS.md, CADENCE.md, workbook/KB.tsv (KB-CRU-244..252), workbook/VX.tsv (VX-CRU-01 Current), inbox/RECEIPT.md, research/2026-11-11_catchup/*, domain/sources/STATUS_archive_2026-11-11.md, archive/2026-09-02_LADDER_DISPOSITION_MEMO.md (moved), this packet
RESULT: Inbox drained (0 packets). Prices refreshed to the 11/10 close; no score moved, convergence 9/20. Rates read from the three 10-Qs: floating debt 6–15%, one 25bp hike ≈ $4.6M/yr at NCLH. CRU-11 interim −0.10pp.
GAPS: High-yield spread leg not measured (LIQUID/credit owner). IR press pages not checked. RCL 10-K rate sensitivity not read. 2Y Treasury not pulled. Consumer check not run: no threshold or figure that others cite was superseded.
WILL_NEEDS: None directly. The `VX-CRU-01` GREEN reading is PROME's to rule or take to Will.
FOLLOW-UP: CRU-11 grade at the 11/13 close (L606); NCLH springing test 11/17 (L715).
