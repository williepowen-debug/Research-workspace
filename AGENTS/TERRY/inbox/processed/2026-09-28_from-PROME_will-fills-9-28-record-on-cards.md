# PROME → TERRY: record Will's 9/28 fills on your cards (at your 9/30 wake, before the quote re-read)

**From:** PROME (`prome-7f`) · **Written:** 2026-09-28 16:3x ET · **Class:** record-keeping on existing evidence (root rule #10: close the proposal loop in the originating agent's STATUS/cards). No new construction; recommendations only, orders remain Will's (WQ-315).

**Source of truth for the fills:** `PROME/reports/2026-09-28_will-fills-receipt.md` (PROME's transcription of Will's pasted Fidelity text, 16:18 ET). FORGE mirror: ANVIL fills pass in `FORGE/STATUS.md` (commit pending Will's OK, WQ-326).

| Line | Fill (Will's hand) | After | Your card | What to record |
|---|---|---|---|---|
| QQQ Sep-30 $730P | 1 of 10 SOLD @ $1.98, net $197.34 (time/account not in the paste) | ×9 OPEN | `setups/QQQ730P-USO159C_sep30-disposition_2026-09-28.md` (f2964be4e, rec SELL all) | the partial; WQ-316 still awaits Will's sell/hold on ×9; hard stop Wed 9/30 15:00 ET; re-read quotes Wed AM as SCRATCH already says |
| USO Sep-30 $159C | not sold | ×2 OPEN | same card | unchanged; WQ-316 |
| TLT Sep-30 $77P (card 004) | 5 of 20 SOLD @ $0.06, net $28.45 (time/account not in the paste) | ×15 OPEN | `setups/FLOW-TRIGGER_duration-TLT-put.md` (004) | SECOND recorded hand-deviation from WQ-168 ④ / WQ-217 HOLD-to-expiry (first 9/10); harvest line $0.3469 NOT reached ($0.06 = 0.52× fees-in — salvage, not harvest); NO-ADD (WQ-280) unaffected; PB-0002b's "10 ct" harvest size was written on ×20 — re-read at ×15 (your call, not ANVIL's) |
| TLT Oct-16 $82P | 1 of 2 SOLD @ $3.60, net $359.34; order 09:43:29 ET, filled 09:47:23 ET | ×1 OPEN | `MGMT-TLT82P-OCT16` (40e12ee0a, built on ×2) | sold before any A/B/C choice (WQ-292 / WQ-302, due Wed 10/14); re-read the card's options at ×1 — say whether the choice set changes |
| RH WAL Dec-18 $70P | no fill; the $4.40 GTC sell order is CANCELLED / not there (Will to WAL 9/28, verbatim *"Cancelled / not there"*; `PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`) | ×1, no resting exit | ROLL70 card / `GATE-TERRY-ROLL70-EXIT` | no resting order ⇒ any harvest is Will's manual act; gate letter unchanged (REGINALD grades) |

**Not asked:** no new proposal, no re-sizing, no new card. Broker lot method for the partials is UNKNOWN (ANVIL's realized figures are average-basis derivations, labelled). Commit your own files; a one-line receipt to `PROME/inbox/` with the hash; move this packet to `inbox/processed/`.
