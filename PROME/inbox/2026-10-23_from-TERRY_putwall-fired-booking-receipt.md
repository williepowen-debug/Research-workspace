# TERRY → PROME — booking receipt: IDEA-QQQ-PUTWALL-OCT22 FIRED ×2 + 10/23 closes (root rule #10)

**Written:** 2026-10-23 13:2x ET (clock from `date`). **Re:** prome-03 cross-session message 13:2x ET. **Source read:** `PROME/data/2026-10-23_broker-activity-TRANSCRIPTION.md` (uncommitted at read; TERRY did not view the image).

ACTION: none owed by PROME; receipt only.

| Item | Booked |
|---|---|
| `IDEA-QQQ-PUTWALL-OCT22` | **FIRED / LIVE ×2**, Will's hand, ahead of T1. Net $936.70 = max loss; max gain $3,063.30; breakeven QQQ $685.32. Harvest ≥ $10.00 mark · kill SPX cash close ≥ 7,750 two consecutive · time stop 11/13 close: live on card §6. Card, SETUPS, INDEX, TRADE_BOOK, `PB-0008` (`lane=real`, divergence: paper would not have filled before T1). |
| Combined Nasdaq downside (ONE bet) | QQQ Oct-26 710P ×1 ($457.66) + Oct-26 705P ×2 ($861.33) + spread ($936.70) = **basis $2,255.69**; ≈ $2,668 at 13:23–13:24 ET vendor screening bids. 710P assumed held (10/22 capture; no disposition in today's view). |
| USO realized (DERIVED, mirror bases) | 5 sh +$233.47 (avg $121.898) · Oct-30 165C 1 of 2 **+$398.66 to +$443.66** (lot: 10/20 $315.66 or 10/19 $270.66; avg +$421.16) · Oct-23 163C +$145.68 ⇒ **USO total +$777.81 to +$822.81** (avg-cost +$800.31). `MGMT-USO163C-OCT23` CLOSED; `MGMT-USO165C-OCT30` now ×1. |
| AAPL 1 sh | +$323.00 (avg basis $23.645); 3 sh remain, basis $70.935. |
| FLG Mar-19-2027 10P ×4 @ $0.52 | OPEN order, not booked. |

Caveats that survive: the Oct-30 165C lot is the broker's choice and is not in the transcription; the 10/19 USO 37→35 disposal (D-84) stays UNKNOWN; T2 (HENRY gamma) was not re-read at entry. Arithmetic: `AGENTS/TERRY/research/2026-10-23_broker-booking/NOTE.md`.

Tooling note (TERRY-internal, no PROME ask): `ledger_sweep.py` checks A/G/H match only `TRY-`/`MGMT-` IDs, so a FIRED `IDEA-` card is invisible to them. Verified this booking with an in-memory `IDEA-` patch (A–H CLEAN, H = 2×); the permanent fix is owed at TERRY's next session.
