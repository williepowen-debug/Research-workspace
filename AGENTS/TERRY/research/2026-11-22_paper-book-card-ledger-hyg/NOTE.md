# Paper book, card ledger and the HYG record — Will's word of 11/22 (WQ-727 item 3)

**Written:** 2026-11-22, started 04:06 EST and resumed 16:47 EST after a network drop (`date`), TERRY, Claude Code, Claude Opus 5.5, laptop. Task letter `inbox/2026-11-22_from-PROME_will-word-paper-book-card-ledger-HYG-record.md` (e03240da10). $0. No trade, no card, no new file class. Markets closed: no price below is live. Record fix only; nothing here asks Will to act on any approval.

## 1. Coverage

| Surface | Covers | Does not cover |
|---|---|---|
| `PAPER_BOOK.tsv` (15 rows, PB-0001 to PB-0011 with RULING-D splits; opened 2026-07-17 to 2026-11-06; marks last 2026-11-18 10:11) | Every card that reached would-fire state, paper-filled at ask/bid and tracked to close (lane paper), plus the cards Will filled (lane real), and one Will-hand trade (PB-0008) that the paper algorithm would not have filled. 4 OPEN (PB-0004 KRE, PB-0009 RSP, PB-0010 UNG, PB-0011 HYG). | Cards that never reached would-fire (every lapsed, void, shelved or declined idea); NO-TRADE reads; management cards; Will's own trades without a card. No would-fire event after 2026-11-06 exists to record (QQQ 200-day: trigger met 11/13 but debit over its limit; QQQ capitulation card pending with Will, WQ-724). Scoring gate (N >= 10 closed per lane) not reached: paper lane 2 closed (PB-0001, PB-0005). |
| `CARD_LEDGER.tsv` (32 rows, WQ-716) | Every new-trade card that reached Will: ruling, placed, fill, close, result, basis. From today also the as-written terms of the 17 lapsed / void / shelved / retired-unfired cards. | Management cards (MGMT-*), Will's own trades with no card (no WILL-OWN rows yet), contemporaneous terms of Will's 7 declines and passes, paper results. |

**Finished today from repository evidence** (cells rewritten in `CARD_LEDGER.tsv`, two corrections labelled in the cell):
- TRY-BRENT-REFINER: WQ-213; approval date corrected 8/27 → 9/10 (row title and card); same note added to PAPER_BOOK PB-0007.
- TRY-WAL-ROLL70: WQ-144 (Will 9/1 18:13 ET).
- TRY-NOTRADE-MRNA-ESMO: WQ-498, corrected from "declined" to LAPSED with no ruling.
- TRY-FIRE-004 and TRY-VIOLET-VIXCS: no queue row can exist; both rulings predate WILL_QUEUE (born 2026-07-30, 090b283891).
- TRY-WAL-ROLL70 close: last seen on the Robinhood card 2026-09-29 13:46 ET, absent 2026-11-05; date and price UNKNOWN.
- IDEA-QQQ-PUTWALL-OCT22 second 690P: closed between the 2026-10-30 13:21 ET capture and 2026-11-05; price UNKNOWN (FORGE D-94, permanently unsupplied under WQ-548).
- IDEA-QQQ-CAPIT-NOV20: now "pending with Will (WQ-724)".

**Still uncovered after today** (named, nothing built):
1. TRY-BRENT-USOARM queue row: SEARCH-NOT-FOUND (Will ruled in session 8/13).
2. TRY-WAL-ROLL70 close date, price and result: needs a Robinhood history line.
3. Second QQQ 690P close price, so the card's result stays partial (+$1,683.92 known).
4. IDEA-HYG-FOLLOW-NOV05 placement and reason (part 4).
5. Terms for Will's 7 declines and passes are not copied into the ledger (they stay on their cards; PB-0009 holds RSP-DEC).
6. Will's own card-less trades have no ledger rows (the WILL-OWN prefix exists; no rows written).
7. Within the 17 lapsed cards, terms the cards never wrote: limit or order on TRY-BUILDER-DHI-PHM, TRY-FIRE-006 (strikes, debit, count, target), TRY-BRENT-DIESEL (count, harvest), TRY-COND-CRWV-RALLYFADE (limit, per-contract fee), IDEA-NVDA-CEOGAP-NOV12 (fee); X1 text absent on 11 of 17 (fields read UNKNOWN).

## 2. Lapsed-unfired terms

Put in `CARD_LEDGER.tsv`, not the paper book: the paper book takes only cards that reached would-fire (`PAPER_BOOK_DESIGN.md` §Decision Logic 1), and none of these did, so a paper row would be a fill that the book's own rule forbids; the ledger is the WQ-716 surface Will named. Eight new columns: terms_source (card @ first commit), entry, size, exit, costs, research_trigger, x1_sizing_limit, terms_label. 17 rows; extraction from `git show <add commit>`, numbers spot-checked by TERRY on USOARM, VFADE, TLT-WQ339, ORCL, QQQ-200D and HYG-BDC. Terms that changed later are named in terms_label (USOARM became 125/130 ×2 @ $1.50 the same day; CRWV rewritten 10/20 as 65/60P @ 2.00; FIRE-006 trigger inverted 7/20; ORCL gained an IR-date entry condition 10/24), never merged. Nothing RECONSTRUCTED; no result computed.

## 3. Phase-2 volume gate

> **CORRECTED 2026-11-23 (WQ-730, Will's word):** the July figure below left PB-0002 out without saying why, and the counter first read 6 on 10/23, not 11/5 to 11/6. The figures, the reason for the exclusion, each stage-two condition and the recommendation as it now stands are in `../2026-11-23_will-rulings-paper-book-print/NOTE.md` §2, which supersedes this section's figures.

**As it reads today (2026-11-22, instrument `paper_book_mark.py` `would_fire_90d`, run offline):** 7 of 6 distinct events in the trailing 90 days → the tool prints GATE TRIPPED (first at 6+ on 2026-11-05/06). It falls to 6 on 2026-12-02 when PB-0006 (opened 9/2) leaves the window. Not in WILL_QUEUE; STATUS has carried it as "open for Will".

**What the 7 are:** PB-0006 WAL roll (9/2), PB-0007 VLO share (9/18), PB-0008a and PB-0008b (one QQQ trade, 10/23), PB-0009 RSP (11/5), PB-0010 UNG (11/5), PB-0011 HYG (11/6).
- PB-0008a/b are one trade split into two rows; the counter keys them as two instruments after the split (a counting defect: the 8/13 fix was meant to collapse splits). True distinct: 6.
- PB-0008 itself was not a would-fire: its row says the paper algorithm would not have filled (T1 not fired; Will's own hand). Without it: 5.
- PB-0007's fill day failed the card's own entry gate (refiners not down vs USO up at 11:00, WQ-213 row), so it is contestable too: 4 to 5.
- From 2026-12-02: 3 to 4.

**Would the salary have bound?** The busiest would-fire stretch (11/5 to 11/6: RSP $380 + UNG $235 + HYG $230 = $845) is well under the $1,500 monthly paper tranche. The other busy stretch, 7/17 to 7/30 (TLT $495 paper, VIX $287.70, KRE $422), totals $1,204.70, and $1,464.70 even with the RULING-E-excluded USO row ($260). No 30-day window ever held 4 distinct counted would-fire cards, so the design's own test (`PAPER_BOOK_DESIGN.md` §Phase 2: binds once would-fire runs at least 4 cards a month) was never met. Only by counting Will's own QQQ trade ($936.70) does a window exceed $1,500.

**What activating would involve:** a `funding_status` column, a $1,500 notional tranche topped up on the 1st (use-it-or-lose-it), ranking each would-fire card by edge bucket then edge score, UNFUNDED rows for losers, a running paper equity curve, a script change in `paper_book_mark.py`, TERRY time each card. All paper, no real capital.

**Earlier rulings on this (stated per Will's 11/22 word):** gate and salary pinned by Will 2026-07-24; counter dedup Will-authorized 2026-08-13; RULING E 2026-08-19 excludes approval-pending rows; Will 2026-10-31 "limit our excess amount of checkers and rules". No ruling on activation exists.

**TERRY recommendation: retire the gate; do not activate Phase 2.** Reasons: the trip is mostly counting (one trade counted twice, plus trades that were Will's hand and not card fires); even the busiest week of real card flow spent $845 of a $1,500 salary, so prioritization would never have bound and Phase 2 would measure nothing; Phase 1 has not reached its own N >= 10 closed-per-lane scoring floor. Retiring means `paper_book_mark.py` stops printing the line and the design marks Phase 2 RETIRED, revivable by Will's word if card flow ever outruns $1,500 a month; Phase 1 is unchanged. Alternative: "not now" keeps the counter (it would need the split fix) and the line keeps printing.

## 4. IDEA-HYG-FOLLOW-NOV05

PROME's read confirmed with one correction: the 11/5 Fidelity capture (~10:0x ET) and the 11/5 Robinhood close capture (16:13 ET) both predate T1 (11/6), so they say nothing about placement. Evidence that does bear: Fidelity positions 2026-11-10 15:13 ET and 2026-11-18 13:21 ET, no HYG line; Fidelity Activity rows 11/2 to 11/10, no HYG row; 11/10 pending −$1,053.33 equals the QQQ 668P buy; 11/18 pending: no line shown (not proof of none); Robinhood 11/10 card, no HYG line; working orders never captured since T1; nothing after 2026-11-18 13:21 ET. GATES `GATE-TERRY-HYG-FOLLOW-01`: APPROVED, UNFILLED.

Cells as written: placed UNKNOWN (no fill evidenced, bounds above) · fill UNKNOWN · close "no position evidenced; card entry window to 2026-12-04" · result UNKNOWN · basis UNKNOWN. Reason: UNRESOLVED. A missed message is not supported by the record: Will ruled on this card's entry rule on 11/9 23:10 ET (WQ-663 B, after an explainer on his 22:27 ET request), so the card had reached him. Whether it was his choice or an execution problem is not established by any committed record of his words.
