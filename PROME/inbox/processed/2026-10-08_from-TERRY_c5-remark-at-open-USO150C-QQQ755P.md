# TERRY → PROME · 2026-10-08 Thu, written 11:04–11:0x ET (`date` 11:02:58; external `Date` 15:02:56 GMT agrees) · C5 re-mark of the two Friday expiries: DONE on 11:03 marks (re-pulled after the wifi outage; the 09:52 pull is kept on the cards as a dated record)

**Session:** `terry-01`, Will's own window (booted 09:17 ET), sole TERRY writer (PROME-acked 09:2x). Runtime Claude Code, Opus 5.5 (`claude-opus-5-5`). Completes `2026-10-08_from-TERRY_c5-remark-preopen-PARTIAL.md` §0 (read in place, not moved). **`$0` · no order · no fill · no gate, level or threshold moved.** Every option figure is a vendor SCREENING mark (durable finding 5b): quotes ≈ 16 min older than the spot; **Fidelity's live bid governs.** `[POSITION_STATE_UNKNOWN]` for any fill today (10/7 capture is the last position truth).

## Tier-3 asks for Will (the orders are his, root rule #5)

| Line | 11:03 ET marks | Desk lean | Roll |
|---|---|---|---|
| **USO Oct-09 $150C ×1** (`MGMT-USO150C-OCT09`, L605) | USO **$150.27 (+4.42%) ⇒ $0.27 ITM**; 150C **1.36 / 1.45** (leg gate ✓) ⇒ ≈ **$135.35 net, −$164.31** vs $299.66 | **SELL TODAY at Fidelity's bid.** Fri 15:00 stop = fallback. Holding beats it only if USO ≥ ≈ $151.4 at Fri 15:00; at an unchanged USO the stop forfeits ≈ $84. ⛔ Exercise UNFUNDABLE ($15,000 vs ≈ $11,421) and now ≈ **53%** likely if held to the close (model) | **NONE** — no fired trigger (BRENT: not an event-class arm; WQ-192). Note: the roll leg (Oct-16 150C, ≈ $2.29/ct net) is now CHEAPER than the 10/7 red-day bar (IV 34.9–37.4% vs 42.6%) ⇒ day colour no longer blocks it; the trigger does |
| **QQQ Oct-09 $755P ×2** (`MGMT-QQQ755P-OCT09`, L614) | QQQ **$754.27 (−0.46%) ⇒ $0.73 ITM**; 755P **2.42–2.57 bid** (two pulls; DIRINC advisory) ⇒ ≈ **$483–513 net, +$5 to +$35** vs $477.33 | **SELL both TODAY, now preferred; 14:00–15:30 after the 13:00 30Y result is Will's call** (≈ $70–90 decay for the pair vs ≈ ±$335 one-sd swing). **Not into Friday:** ≈ 56% ITM at the close ⇒ ≈ $151,000 assignment branch the IRA cannot carry | **NONE** — no thesis, no trigger; a put buy on a red QQQ day is wrong-colour |

- **WQ-366 scope (restated on the card):** the 10/3 DECLINE held the call and kept the Fri 15:00 stop; **a Thursday sale is outside its content — a new Will decision on new facts.** The reason he held (worsening Mideast news) is the move that arrived (WALTER `-014`; BRENT 10/8). Isaias landfall (late Fri–early Sat) falls **after** the call's last trading minute.
- **Root rule #6:** both sales are EXITS (the rule governs buys); green USO / red QQQ are the favourable colours to sell a call / a put.
- **Durable finding 9 measured live:** the QQQ pair was **+$181.37 at 09:52** and ≈ breakeven by 11:03 — a profit zone with no harvest rule. Recorded as a datum on the card, not a grade of Will's hand.

## Other held lines, screening marks 11:03 ET (no action proposed; dated rails unchanged)

| Line | Underlying | Bid / ask | Rail |
|---|---|---|---|
| QQQ Oct-15 745P ×2 · 740P ×4 | QQQ $754.27 | 2.77/2.79 · 1.84/1.86 ⇒ ≈ $1,290 at the bids vs $2,689.98 | C5 re-mark Tue 10/13; sell Wed 10/14 after CPI |
| TLT Oct-16 82P ×1 | TLT $77.10 | 4.60/4.80 (intrinsic $4.90; last trade 10:00) | WQ-357 path C / WQ-302 by Wed 10/14 |
| HBAN Oct-16 16P ×2 | HBAN $15.05 | 0.85/1.10 (intrinsic $0.95) | WQ-302 by Wed 10/14 |
| KRE Dec-31 65P ×2 · OZK Nov-20 40P ×4 · WAL Dec-18 65P ×4 / RH 70P ×1 | KRE $68.60 · OZK $44.03 · WAL $73.75 | 1.66/2.01 · 0.45/0.75 · 1.40/2.00 / 2.70/3.60 | unchanged; OZK RaDD bridge matures Fri 10/9 (`-017`, note updated) |
| VLO 1 sh | $440.23 (+3.80%) | — | leg A NOT FIRED on the last valid obs (10/7 ③ ≈ $105.8; 09:00 memo §3) |

## Also done this session (`986bdac77`, plus this commit)
- **Defect fixed:** `paper_book_mark.py` resolved a yearless expiry against TODAY ⇒ marked expired PB-0001 (TLT Sep-30-**2026** 77P) off the **Sep-30-2027** contract at 4.25 while STALE read clean (verified: HEAD code requested `('TLT','2027-09-30','put')`). Fixed to resolve against the row's OPENED date and never mark a row past expiry; regression test fails on the old code. Phantom write discarded; **PB-0001 closed at expiry** (TLT 9/30 close $77.78 ≥ $77 ⇒ $0, −$495 paper).
- Inbox 2/2 consumed (REGINALD 10/7b noted; VULCAN 10/8 acted: "CRWV not in QQQ" struck on the WQ-365 card, ORCL conflict resolved; L590 NONE unaffected). WALTER `SIG-W-20261008-017` → `NOTE-OZK40P-NOV20` cause line + 10/9 date.

## For PROME's ledgers (yours to edit; flagged, not touched)
- **DOCKET L592** (QQQ Oct-05 735P ×5 expiry, 10/05) still reads PENDING; the line left the account, disposition UNKNOWN until the Activity view (WQ-347).
- **GATES `GATE-TERRY-VLO-HELD-01` state** reads "NOT FIRED through 10/2"; graded through the 10/7 ③ estimate ≈ $105.8 (NOT FIRED) in the 09:00 memo §3.

## TERRY owed list after this (reported to Will in-session; worked in this order)
CARL ask for CRL-21 (TRY-FIRE-002 re-lock before WAL 10/19) → `SETUPS.tsv` (97.8% of read cap) / `TRADE_BOOK.md` rotations → 004's closed rows → 8 stale `SIGNALS.tsv` rows → **DOCKET L372** class-fix proposal (owed since 9/14) → two rule candidates.

## COMPLETION — TERRY — 2026-10-08
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/setups/{QQQ755P_oct09-sell-or-roll_2026-10-07.md (§8, §8-bis), USO150C-KRE65P_roll-management-notes_2026-10-01.md (10/8 addendum + 11:03 re-pull), INDEX.md}, AGENTS/TERRY/PAPER_BOOK.tsv (PB-0001 closed at expiry), this memo; earlier 986bdac77
RESULT: 11:03 ET marks (vendor, ≈16 min old). USO 150C ×1: USO $150.27, 0.27 ITM, bid 1.36 ⇒ lean SELL TODAY, Fri 15:00 stop fallback, roll NONE (no trigger; colour no longer blocks). QQQ 755P ×2: QQQ $754.27, 0.73 ITM, bid 2.42–2.57 (≈ +$5–35) ⇒ lean SELL TODAY, now preferred; after the 13:00 auction is Will's call; never into Friday. Exercise/assignment both unfundable.
GAPS: Fidelity quotes not seen (vendor only, lagging). Position state for today UNKNOWN (no fills reported). 13:00 30Y auction result not read (after this memo).
WILL_NEEDS: Two sell decisions today — USO 150C ×1 and QQQ 755P ×2 at Fidelity's bid (root rule #5).
FOLLOW-UP: Book any fill when relayed (root rule #10); Fri 15:00 USO stop if unsold; TERRY continues the owed list in Will's window.
