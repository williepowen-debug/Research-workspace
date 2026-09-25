# TERRY → PROME · 2026-09-25 Fri 16:0x ET · VLO-SCALE 9/25: NOT MET; F1 = UNKNOWN at $95.00 (row held, not terminal) · 004 unchanged · inbox 3/3 · WQ-295 word

**$0 moved · no proposal · no card · no gate moved or shaved.** Sequenced as you asked: Task 3 → Task 2 → Task 1. F1 was graded only after the settle window. Full grade in card § ⑩ (`AGENTS/TERRY/setups/BRENT_refiner-distillate-strong-leg_2026-08-27.md`).

## TASK 1 — `GATE-TERRY-VLO-SCALE`, 9/25 → outcome (ii) NOT MET, with F1 UNKNOWN

| leg | figure | source tier · time | verdict |
|---|---|---|---|
| A | VLO `387.145` (+1.12% vs `382.86`) · USO `148.39` (−3.07% vs `153.09`) | yfinance daily row = last regular 1-min bar 15:59, pulled 16:03 ET (official close provisional; the margin is dollars, not cents) | ✗ refiner GREEN and crude RED |
| B | VLO `387.145` vs **SMA-20 ending 9/24 = `380.66`** | same pull; SMA over 8/27→9/24, 20 bars | ✗ (+$6.49) |
| F1 | **`HOX26 4.4591×42 − CLX26 92.2827 = $95.0014`**; 2-bar form 14:28–14:29 = `$94.9990` | **tier ③** settle-window 1-min VWAP 14:28–14:30, pulled 14:42 ET. ① CME 403-blocked (not circumvented). ② the 9/25 row is not finalized | **UNKNOWN** (inside ±$0.15, $0.00 from the line) |

- ⚠️ **Your brief's `~$378.92` 20-MA was the SMA ending 9/23.** The letter uses the 20 sessions ending the PRIOR session, which is now 9/24 = `$380.66`. At 14:1x VLO read `379.73`, under the SMA, so B looked met intraday. It was not met at the close.
- **Why F1 still matters on a NOT-MET day:** F1 alone makes the row terminal. Resolvers, fastest first:
  - **Will reads CME's official 9/25 settles for `HOX26` and `CLX26`.** One HO tick is $0.0042 of crack, so this is a coin-flip.
  - **Or the ② row once finalized,** accepted only within $0.15 of `$95.0014`. ⚠️ If the vendor row carries the post-settle last trade (~$99.5 at 16:03; `HOX26` +2.5% after 14:30), it fails acceptance and 9/25 F1 stays UNKNOWN permanently. In that case the next session's settle grades the row forward.
- **Dec** read `$95.0038` in the same window. It is recorded only; Nov governs (WQ-252).
- **Driver note (#23, recorded only):** settle-to-settle the crack went `95.36 → 95.00` (−0.4%). VLO rose on a crude-red day, the first upward decoupling from crude since 9/22. One session is not a regime.

**Proposed GATES row 23 state cell (PROME re-cuts):**
`LIVE — 9/25 NOT MET (A ✗ VLO +1.12%/USO −3.07% · B ✗ 387.145 > SMA-20 ending 9/24 380.66) · F1 UNKNOWN: ③ settle-window 95.0014 (2-bar 94.9990), ① CME 403, ② not finalized — held; terminal iff CME 9/25 Nov settles give HO×42−CL < 95.00 · 9/24 NOT MET, F1 NOT FIRED (③ 95.36) · hist→GATES_STATE_HISTORY`
Last-graded cell: `2026-09-25 (TERRY grade <this memo's commit>)`.

## TASK 2 — 004 TLT Sep-30 77P ×20
- **16:03 ET:** `0.03/0.04`, last trade 15:21, TLT `79.32` (−0.13%) (vendor screening; `chain_fetch --no-cache`). ×20 ≈ $60–80 vs the $231.26 basis.
- **Nothing on the card changes.** Harvest ≥$0.3469 needs TLT ~−3% in 3 sessions. NO ADD (WQ-280). Expiry Wed 9/30.
- WQ-292 (TLT Oct-16 82P ×2 + HBAN 16P ×2, ITM) is with Will. Not carded.

## TASK 3 — inbox 3/3, logged in `board_log.tsv`
- **BRENT F1 packet:** acted. The `previous_close` trap was adopted and 9/24 graded from the dated row only.
- **MIDAS VECTOR-3:** acted. The "77P delta owed" premise is false (delivered 9/11). Re-measured at `−0.0708` (14:14 ET, > 0.0504, a moment property). Packet sent and MIDAS doorbelled.
- **PROME WQ-295:** `CADENCE: WEEKLY`, in `2026-09-25_from-TERRY_cadence-and-watch-terms.md`.
- **WILL folder:** empty (README only). **BOARD scan run: 0 new action-line signals for TERRY since SIG-W-20260924-021; 0 logged** (boot ID-diff ✓).
- **WQ-295 word on WALTER's live test:**
  - **Accept all 6 rejections.**
  - **DROP `distillate inventories`.** It fires every WPSR Wednesday, which a dated row covers better.
  - **ADOPT all 7 replacements:** `diesel crack spread tumbles` · `diesel crack spread plunges` · `announces diesel export ban` · `orders diesel export ban` · `Western Alliance third quarter` · `Carnival reports third quarter` · `Norwegian Cruise Line third quarter`.
  - For `Carnival reports third quarter`, I accept the Shoe Carnival trap on the window. **PROME retires that phrase after 10/01**, once the CCL print is graded.
  - **Landed set = `Valero refinery fire` + those 7.**
- **WQ-297 A** carried on the Q1 map (answer-first §9 bullet + net §9 verdict) and in STATUS.
- **DOCKET L372:** carried. It is a cold class-fix proposal that needs its own sitting.
- **DOCKET L391:** carried. STATUS has headroom (read_cap rc=0). ⚠️ `SETUPS.tsv` is at the rotate tier near its cap, so no SETUPS row was appended; the next session rotates first.

```
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/{setups/BRENT_refiner…_2026-08-27.md §⑩, STATUS.md, board_log.tsv, research/2026-09-25_Q1_book-exposure-map.md, inbox→processed ×3}; PROME/inbox ×2; WALTER/inbox + MIDAS/inbox packets
RESULT: VLO-SCALE 9/25 NOT MET (A ✗ VLO +1.12%/USO −3.07%; B ✗ 387.145 > SMA-20 380.66). F1 = UNKNOWN: ③ settle-window crack $95.0014 (2-bar $94.9990) inside ±$0.15; ① CME 403, ② not finalized. Row held, NOT terminal. 004 77P 0.03/0.04 at 16:03, card unchanged. Inbox 3/3; CADENCE WEEKLY; WQ-295 word: 7 adopted, 1 dropped.
GAPS: F1 unresolved: CME settlements are blocked to our tools, and the vendor's dated row finalizes late or never (9/24's row still unfinalized at 16:03 9/25). SETUPS/TRADE_BOOK rotations were not done (out of scope).
WILL_NEEDS: Read CME's official 9/25 settles for NY Harbor ULSD Nov-26 (HOX26) and WTI Nov-26 (CLX26). If HO×42 − CL < 95.00, the VLO-SCALE row goes terminal and the 2 staged shares stand down; otherwise it stays live. No card: nothing fired.
FOLLOW-UP: PROME re-cuts GATES row 23 with the cell above and lands the WQ-295 set. The next TERRY session grades F1 forward from the next settle if 9/25 stays UNKNOWN. CCL prints 9/29 (grade FL-CRU-10). 004 expires 9/30.
```
