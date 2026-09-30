# TERRY → PROME — Sep-30 expiry grades on the 9/30 closes

**Written:** 2026-09-30 Wed 17:3x ET (`date` 17:33:44 at boot, 17:37:04 before this memo) · **Spawn:** `prome-94`, Tier 1 follow-up of the 9/30 wake (ORCH_LOG terry-0930 / terry-61). Will's TERRY window died in a machine crash after ~15:05 ET, before these grades.
**`$0` MOVED · NO PROPOSAL · NO NEW CARD · NO GATE OR THRESHOLD MOVED · NO TRADE REC.**

## Closes (regular session; `fetch.py price <T>` + yfinance daily bar `prepost=False`, pulled 17:33–17:35 ET)

| underlying | O | H | L | **C** | strike | at expiry |
|---|---:|---:|---:|---:|---:|---|
| TLT | 78.18 | 78.21 | 77.55 | **77.78** | 77P | OTM by $0.78 (1.0% of the close) |
| KRE | 69.82 | 70.26 | 69.11 | **69.44** | 60P | OTM by $9.44 (13.6%) |
| QQQ | 740.19 | 745.08 | 739.46 | **739.77** | 730P | OTM by $9.77 (1.3%) |
| USO | 147.17 | 147.87 | 145.33 | **145.66** | 159C | OTM by $13.34 (9.2%) |

These match PROME's 17:3x reads exactly. **No line finished in the money, so none has an exercise path.**

## Grades

| line | outcome | realized (average basis; broker lot method UNKNOWN; FORGE governs the cent) | card |
|---|---|---|---|
| **004** TLT Sep-30 77P ×15 | **EXPIRED WORTHLESS.** HOLD-to-expiry rail **DISCHARGED** (WQ-168 ④ / WQ-217). NO-ADD (WQ-280) held. Harvest line (≥$0.3469 fees-in ⇒ TLT ≤ ~$76.65) **NOT REACHED**: the day low was $77.55. The D-60 afternoon flag (TLT < ~$77.25) never tripped. **`PB-0002b` NOT-REACHED per the pre-registered grind** ("grind pays $0"; the 7/17 build said a slow drift in the right direction would expire it worthless, and that is what happened). Shadow row CLOSED | ×15: **−$173.45 (−100%)**. Whole card, all lots: +$128.86 − $29.38 − $29.36 − $173.45 = **≈ −$103.33** on $346.89 deployed | `setups/FLOW-TRIGGER_duration-TLT-put.md` — header verdict → CLOSED; EXPIRY GRADE block at the foot |
| **KRE** Sep-30 60P ×2 | **EXPIRED WORTHLESS.** The LAPSE ruling (WQ-168 ⑥) is discharged | **−$454.00 (−100%)** | `setups/KRE_add-puts_conditional-card_2026-09-30.md` § 9, one graded line appended. **§§ 1–8 and the A1–A3 arm are unchanged** |
| **QQQ** Sep-30 730P ×9 | **OTM at expiry.** ⚠️ **Will's action is UNKNOWN, PENDING HIS WORD:** either (a) he sold at the bid before 15:00, or (b) he held into expiry. Neither is assumed. Both branches end OTM, so **no exercise and no IRA short** | ×9 basis $2,237.97. (a) sold at ~$0.07 ⇒ ≈ −$2,181 (his fill supplies the cent) · (b) held ⇒ **−$2,237.97**. Whole line including the 9/28 1-lot (−$51.32): (a) ≈ −$2,232 · (b) −$2,289.29 | `setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md` § ⑨; header verdict → CLOSED with the UNKNOWN beside it |
| **USO** Sep-30 159C ×2 | **EXPIRED WORTHLESS**, as recommended. There was no bid to sell into | **−$921.33 (−100%)** | same card § ⑨ |

- **D-60 stays UNOBSERVED.** This is the open question of what Fidelity does with an in-the-money long option when the IRA holds no shares. Nothing expired in the money, so today added no observation.
- **Neither § ⑧ re-look trigger fired.** QQQ's low was $739.46 against a $733 trigger, and USO's high was $147.87 against a ~$156 trigger.
- **Surfaces updated:** STATUS gets a new 9/30 17:33 block, and the WQ-316 line, the expiries line and the "owed after the close" line are replaced in place. The 9/25 table's 004 row is marked SUPERSEDED. Both INDEX rows (TRY-FIRE-004 and MGMT-QQQ730P-USO159C-SEP30) are updated, and PAPER_BOOK `PB-0002b` is closed. `ledger_sweep.py`: ✅ CLEAN on checks A–H, rc 0, with CHECK H showing 004 no longer among the live counts. `read_cap_check --agent TERRY`: rc 0, and STATUS is at 22,223 B.
- **Inbox:** census reads top-level 1 (`.gitkeep`), WALTER/ 0 and WILL/ 2 (README + `.gitkeep`). Nothing to drain. **BOARD scan run:** 21 action-line signals, all logged, 0 new.

## COMPLETION — TERRY — 2026-09-30
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/{STATUS.md, PAPER_BOOK.tsv, setups/INDEX.md, setups/FLOW-TRIGGER_duration-TLT-put.md, setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md, setups/KRE_add-puts_conditional-card_2026-09-30.md} (`ee04fbb26`); this memo
RESULT: All four Sep-30 lines expired OTM on the 9/30 closes (TLT 77.78 · KRE 69.44 · QQQ 739.77 · USO 145.66), so no line has an exercise path. 004 ×15 lost −$173.45; the whole card, all lots, is ≈ −$103.33. Its HOLD rail is discharged and PB-0002b is CLOSED as NOT-REACHED per the pre-registered grind. KRE ×2 lost −$454.00 and USO ×2 lost −$921.33.
GAPS: The QQQ ×9 disposition is UNKNOWN because Will's 15:02 answer was lost in the crash. Scoped out and still owed: POSTMORTEMS.md for 004 (and QQQ/USO once known), and the SETUPS/TRADE_BOOK rows, which wait on the rotations still owed. Not pushed: PROME pushes at its closeout.
WILL_NEEDS: Did he sell the 9 QQQ 730P before 15:00, and at what fill, or hold them into expiry? (WQ-316 closeout.) FORGE needs broker truth for all four expired lines.
FOLLOW-UP: Record Will's QQQ word on card § ⑨ and INDEX · a TERRY postmortem pass · the SETUPS/TRADE_BOOK rotations.
