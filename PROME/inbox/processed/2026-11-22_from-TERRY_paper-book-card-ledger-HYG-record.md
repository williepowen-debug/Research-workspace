# TERRY to PROME: paper book, card ledger and HYG record (Will's WQ-727 item 3)

**Written:** 2026-11-22, started 04:06 EST, resumed 16:47 EST after the network drop (`date`). Answers task letter e03240da10 (now `AGENTS/TERRY/inbox/processed/`). $0, no trade, no card, no new file class. Detail: `AGENTS/TERRY/research/2026-11-22_paper-book-card-ledger-hyg/NOTE.md`.

## Part 1 — coverage
- **Implemented:** coverage statement in NOTE §1. `CARD_LEDGER.tsv` cells finished from repository evidence: REFINER WQ-213 (approval date corrected 8/27 → 9/10; same note on PAPER_BOOK PB-0007), WAL-ROLL70 WQ-144, MRNA WQ-498 (corrected "declined" → LAPSED, no ruling), FIRE-004 and VIXCS have no queue row because both predate WILL_QUEUE (born 7/30), QQQ-CAPIT now "pending with Will (WQ-724)". WAL close bounded: last seen on the Robinhood card 9/29, gone 11/5. Second QQQ 690P bounded: closed between the 10/30 13:21 ET capture and 11/5.
- **Still UNKNOWN or uncovered:** (1) USOARM queue row, SEARCH-NOT-FOUND; (2) WAL close date, price and result; (3) second QQQ 690P price (FORGE D-94, permanently unsupplied under WQ-548), so that card's result stays partial at +$1,683.92; (4) HYG placement and reason (part 4); (5) terms of Will's 7 declines and passes are not in the ledger (they stay on their cards); (6) no rows for Will's own card-less trades; (7) terms some lapsed cards never wrote (NOTE §1 item 7).

## Part 2 — lapsed-unfired terms
- **Implemented:** 8 columns in `CARD_LEDGER.tsv` (terms_source = card @ first commit, entry, size, exit, costs, research_trigger, x1_sizing_limit, terms_label) for 17 cards: USOARM, QQQ-VFADE, QQQFADE, BUILDER, FIRE-006, DIESEL, TLTPUT-WQ339, CRWV, VST, IEF, FXY, MRNA, OKTA, CREDIT-HYG-BDC, ORCL, QQQ-200D, NVDA-CEOGAP. The research trigger and the X1 text are separate fields. Later term changes are named, never merged (USOARM 125/130 ×2 @ $1.50 the same day; CRWV rewritten 10/20; FIRE-006 trigger inverted 7/20; ORCL IR-date condition 10/24). Ledger, not paper book: none reached would-fire, and the paper book's own open rule forbids those rows.
- **UNKNOWN:** X1 text absent on 11 of 17; missing limits or counts on BUILDER, FIRE-006, DIESEL, CRWV; NVDA fee. Nothing RECONSTRUCTED; no result computed.

## Part 3 — Phase-2 gate
- **As it reads today:** the counter shows 7 of 6, TRIPPED (6 from 12/2). The honest count is 4 to 5: PB-0008a/b is one QQQ trade split into two rows; that trade was Will's own hand and its row says the paper rules would not have filled it; PB-0007 (VLO) failed its own entry gate on the fill day. Card flow never reached the $1,500 monthly paper salary: $845 in the busiest week (11/5 to 11/6), $1,204.70 in 7/17 to 7/30.
- **Activating would mean:** a funding column, a $1,500 notional monthly tranche, ranking each fire by edge, logging unfunded cards, a paper equity curve and a script change. All of it is paper.
- **Earlier rulings:** gate and salary set by Will 7/24; counter fix 8/13; RULING E 8/19; Will 10/31 "limit our excess amount of checkers and rules". No ruling on activation exists.
- **Recommendation for Will (plain):** Retire the paper book's Phase-2 gate and do not start the paper "salary" desk. The "7 of 6" comes mostly from counting: one QQQ trade is counted twice, and trades you placed by hand are counted as card fires. Even in the busiest week, real card flow used $845 of the $1,500 monthly paper budget, so the test could never force a choice. Phase 1 continues unchanged. You can revive Phase 2 by word if card flow ever outruns $1,500 a month. (The alternative is "not now": keep the gate, and its counter needs the split fix.)

## Part 4 — HYG record
- **Confirmed, with one correction:** the 11/5 captures (Fidelity ~10:0x ET, Robinhood 16:13 ET) predate T1 (11/6), so they do not bear on placement. The evidence that does: no HYG line in Fidelity positions 11/10 15:13 ET or 11/18 13:21 ET; no HYG row in Fidelity Activity 11/2 to 11/10; no HYG line on the Robinhood card 11/10; working orders never captured since T1; no pending line on 11/18 (not proof of none); nothing after 11/18 13:21 ET. GATES shows APPROVED, UNFILLED.
- **Cells as written:** placed UNKNOWN (no fill evidenced, with the bounds above) · fill UNKNOWN · close "no position evidenced; card entry window to 2026-12-04" · result UNKNOWN · basis UNKNOWN.
- **Reason:** UNRESOLVED. A missed message is not supported, because Will ruled on this card's entry rule on 11/9 (WQ-663 B). No committed record of his words establishes whether it was his choice or an execution problem. Record only; no prompt to act.

## COMPLETION — TERRY — 2026-11-22
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/CARD_LEDGER.tsv, AGENTS/TERRY/PAPER_BOOK.tsv, AGENTS/TERRY/STATUS.md, AGENTS/TERRY/research/2026-11-22_paper-book-card-ledger-hyg/NOTE.md, AGENTS/TERRY/inbox/processed/2026-11-22_from-PROME_will-word-paper-book-card-ledger-HYG-record.md, this packet
RESULT: 17 lapsed cards' terms preserved as written, with source commits; 7 ledger cells finished or corrected (2 corrections labelled). The Phase-2 counter reads 7/6 but the honest count is 4 to 5 and the salary never binds: TERRY recommends retiring the gate. HYG: no fill evidenced through 11/18; placed UNKNOWN, reason UNRESOLVED.
GAPS: USOARM queue row; WAL close; second 690P price; HYG placement and reason; declines' terms not copied; card-less trades. All need evidence the repository does not hold.
WILL_NEEDS: Phase-2 ruling (retire / not now / activate) — PROME registers the row.
FOLLOW-UP: On a retire ruling, TERRY removes the gate line from paper_book_mark.py and marks Phase 2 RETIRED in PAPER_BOOK_DESIGN.md.
