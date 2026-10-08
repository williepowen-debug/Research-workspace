# TERRY → PROME: Will's three 10/8 fills booked; QQQ 750C Oct-09 gets its own card; the Friday rails restated

**From:** TERRY (`terry-1008pm`, PROME spawn under C5 / WQ-348 plus Tier-1 follow-up of PROME's 15:32 ET packet; laptop) · **Written:** 2026-10-08 19:12 ET (`date`) · **Runtime:** Claude Code, Claude Opus 5.5 (`claude-opus-5-5`); tools Bash/Read/Write/Edit, with SendMessage loaded via ToolSearch for delivery. **Commit:** `beb763aa3` (TERRY files). This memo is a separate commit. **`$0` MOVED · NO ORDER · NOTHING APPROVED · NO GATE, LEVEL OR THRESHOLD MOVED.**
**Sources:** `PROME/data/2026-10-08_broker-capture-TRANSCRIPTION.md` (ties to the cent at $34,650.69) · `git show ef2bc83f1:FORGE/STATUS.md` (ANVIL). `positions_from_forge.py` read the live mirror at 19:0x with FORGE clean at `ef2bc83f1`, before PROME's rotation touched it: 19 live positions, 0 defects, and the Oct-09/Oct-15 quantities match the broker.

## 1. Booked (root rule #10)

| Line | Will's 10/8 activity | Booked on | Now |
|---|---|---|---|
| QQQ 755P Oct-09 | SOLD 1 of 2 @ $8.36 (+$835.32; realized ≈ +$596.65, derived); 2nd sell $8.50 Verified Canceled | `MGMT-QQQ755P-OCT09` § 9 + header/verdict + INDEX | **×1**, basis $238.66 |
| QQQ 745P Oct-15 | SOLD 1 of 2 @ $6.06 (+$605.32; realized ≈ +$321.65) | `MGMT-QQQ745P-OCT15` § 9 + INDEX | **×1**, basis $283.66 |
| QQQ 750C Oct-09 | BOUGHT 1 @ $1.56 (−$156.66) | **NEW card `MGMT-QQQ750C-OCT09`** + INDEX | ×1 |
| USO 150C Oct-09 | NOT sold (no USO option row in the Activity) | `MGMT-USO150C-OCT09` evening addendum + ⏩ CURRENT line + INDEX | ×1 held |

- The fill times are UNKNOWN, so there is no execution grade (durable finding 6). Both QQQ sales cleared the card-suggested harvest levels that Will never adopted ($4.78 / $5.68). The 740P Oct-15 $5.31 average is a **real 10/2 opening debit** (Activity, D-73), not the carried roll basis the 10/7 card had flagged; that ⚠️ is resolved on the card.

## 2. The 750C card question: a SEPARATE card (PROME's read was "a note, no card")

- **Choice: `setups/QQQ750C_oct09-sell-or-roll_2026-10-08.md`, id `MGMT-QQQ750C-OCT09`, not a §-bis on the 755P card.** ① It is a distinct identity with a distinct exercise branch: a $75,000 *purchase*, the mirror image of the put's ≈ $75,500 *short*. ② **With both Oct-09 lines held, every Friday close leaves at least one of them in the money.** Below $750 the 755P is at least $5 in the money; above $755 the 750C is at least $5 in the money; between the strikes both are. The pair is never safer than at QQQ $752.50, where each is still $2.50 in the money. Both cards carry this and point at each other. On paper the two exercises offset each other between $750 and $755, but whether Fidelity nets them is UNOBSERVED (D-60), so do not plan on it. ③ INDEX stays one id per line, and `ledger_sweep.py` reads one verdict per card.
- **I disagree with "no new card" on ②.** The joint fact is the load-bearing reason neither line can see Friday's close, and a one-line note would not carry it. C5's two-session lead is impossible at 1 DTE, and the card records that.
- **Card verdict:** SELL at Fidelity's bid **Fri 10/09, 09:45–10:30 ET, no later than 12:00**; never into the close; **roll NONE** (no thesis, no trigger; the construction rule #21 forms are given for the record only). Day colour: the sale is an exit, so root rule #6 does not bind it; a green QQQ session gets a better price for the call. The buy was on a red day, the favourable colour; it is recorded, not re-opened.
- **Model** (calibrated to the vendor end-of-session mid at QQQ $748.00 [16:14]; shape, not price): at an unchanged QQQ the call is ≈ $1.72 at 09:45, $1.21 at noon and $0.29 at 15:00. The $156.66 basis comes back at 10:00 only if QQQ is above ≈ $747.3. Chance of a Friday close above $750 ≈ 36%.

## 3. Restated rails (task items 3–4)

| Line | Rail | `[10/8c]` (closes / vendor end-of-session quotes, NEVER bids) |
|---|---|---|
| QQQ 755P **×1** | SELL at Fidelity's bid Fri morning (09:45–10:30), **never into Friday's close**; ≈ $75,500 assignment branch, ≈ 85% likely if held (model). Roll NONE | QQQ $747.58 ⇒ **$7.42 in the money**; 7.08/7.30 (bid below intrinsic: quote struck against QQQ ≈ $748.00 at 16:14) |
| QQQ 750C ×1 | as § 2 | **$2.42 out of the money**; 1.92/1.94 |
| USO 150C ×1 | **Fri 15:00 ET HARD STOP STANDS** (WQ-366 DECLINE; L605); exercise $15,000 vs ≈ $11,421 cash is UNFUNDABLE; earlier is Will's choice | USO $147.58 ⇒ $2.42 out of the money; 0.58/0.65; P(close above 150) ≈ 26% (model) |
| QQQ 745P ×1 · 740P ×4 | Tue 10/13 C5 re-mark; SELL Wed 10/14 09:45–10:30 after CPI, ≤ Thu 12:00. Exercise path re-sized to $370,500 | $2.58 / $7.58 out of the money; 5.22/5.27 · 3.63/3.67 |
| TLT 82P ×1 · HBAN 16P ×2 | WQ-357 path C / WQ-302, Wed 10/14 (unchanged) | TLT $77.87 · HBAN $15.37 |

Post-market QQQ was $748.92–748.99 at 18:55–19:00 ET (not a close). Friday's marks come from Fidelity's bid at the open. No Friday 10/9 catalyst is registered on BOND's calendar.

## 4. Housekeeping done

STATUS gets a new evening CURRENT STATE block. The demoted 10/8 AM and 10/7 blocks were rotated verbatim to `archive/STATUS_ARCHIVE_2026-10-08b.md` (9,400 B, crc32 `a82ed377`; legs verified in its header), taking STATUS from 28,526 to 19,533 B (the read cap had flagged it at 88% of budget). `ledger_sweep.py` is CLEAN on A–H. `claim_check` is clean. The PROME packet went to `processed/` with a `board_log` row. `SIG-W-20261008-033` (WQ-399) is logged `noted`.

## COMPLETION — TERRY — 2026-10-08
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/setups/QQQ750C_oct09-sell-or-roll_2026-10-08.md (new), setups/QQQ755P_oct09-sell-or-roll_2026-10-07.md, setups/QQQ745P-740P_oct15-sell-or-roll_2026-10-07.md, setups/USO150C-KRE65P_roll-management-notes_2026-10-01.md, setups/INDEX.md, STATUS.md, archive/STATUS_ARCHIVE_2026-10-08b.md (new), board_log.tsv, inbox PROME packet → processed/ (`beb763aa3`); this memo
RESULT: Three 10/8 fills booked: 755P Oct-09 2→1 @ $8.36 (+$596.65 realized), 745P Oct-15 2→1 @ $6.06 (+$321.65), USO 150C not sold, Fri 15:00 stop stands. The new 750C Oct-09 got its own card: SELL Fri 09:45–10:30 ET, ≤ 12:00, never into the close (an in-the-money call buys $75,000 of QQQ, unfundable); roll NONE. With the 755P ×1 also held, every Friday close leaves at least one Oct-09 line in the money, so both should be sold Friday morning. Marks are 10/8 closes and screening quotes, never bids.
GAPS: R1: `corrections_boot_check.py TERRY` rc=1, 5 NAMED unreceipted (COR-20260928-17, -20260929-09, -20261002-16, -20261002-27, -20261008-41), not done in this bounded spawn. DAEDALUS ×3 (10/8) read but left unconsumed. D-72 booking on the closed Oct-02/Oct-05 cards not done. Fidelity's ITM handling (D-60) is still UNOBSERVED.
WILL_NEEDS: Fri 10/09 orders (his, root rule #5): sell QQQ 755P ×1 and 750C ×1 at Fidelity's bid, 09:45–10:30 ET, never into the close; USO 150C by the 15:00 ET stop (WQ-366). The 750C has no WQ row; PROME decides whether to fold it into WQ-397 or register one.
FOLLOW-UP: Fri 10/09: book Will's fills (TERRY re-spawn or next wake). Tue 10/13: C5 re-mark of the Oct-15 lines. Next full wake: R1 receipts in WQ-399 form, the DAEDALUS ×3 drain incl. the CLOSEOUT-hold four-item record, the D-72 card booking, and the BOOT step 14 receipt-line fix.
