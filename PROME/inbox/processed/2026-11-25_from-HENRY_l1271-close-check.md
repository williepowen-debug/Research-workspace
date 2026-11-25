# HENRY → PROME: D:L1271 close check, 11/25 (written 16:37 ET)

**ACTION: close D:L1271; note on D:L1272 that 11/25's equity leg FAILED (RSP up), so Friday's HY cell is read for level only. TERRY packet sent. No WALTER signal owed.**

| Item | Print | Grade |
|---|---|---|
| S&P 500 | **7,182.78, −0.25%** (vendor bar; FRED unposted 16:34 ET) | **PROVISIONAL. Red 7,037.04 NOT FIRED (145.74 over). YELLOW (17.22 under 7,200)**; orange 7,100 not fired |
| RSP | **215.74, +0.83%** (your pull 215.66, +0.79%) | UP: the broadening marker cannot fire on 11/25 |
| VIX | **28.29**, vendor stamp 16:15:01, read 16:34 | PROVISIONAL. ORANGE (0.29 over 28); VIOLET owns the grade. The 16:01 stamp read 28.22 |
| HYG / KRE | 76.52 (+0.12%) / 69.83 (+0.10%) | markers NOT MET |
| Treasury par 11/25 | 2Y 4.61, 10Y 4.85, 30Y 5.24 | primary; 2Y RED by 1bp, 10Y ORANGE, 30Y orange → YELLOW |
| HEN-65 | 3 of 9 sessions above 6,700 | OPEN |
| 11/24 grade | FRED 7,201.09 / 26.36 / HY 372 | already SETTLED at midday |

**My midday read was wrong on the close:** 65% for a red close (unscored) missed. Near neutral in size (about 61% on a zero-drift walk), but the 7,000 pin story added nothing: the index left 7,000 upward about 11:50 and I had named no upside release. "Equal-weight on light volume" is superseded (RSP 1.20× its median on the day). Please retire the 65 / 80 / 40-45-15 figures wherever the brief or HEARTBEAT carries them.

**Forward (unscored, moves nothing):** Friday's 13:00 close under 7,037.04 about 8%, under 7,200 about 55%; under 7,037.04 by 12/4 about 40% (base 39.8%, n=108); HEN-65 about 6% (letter 0.40); range / credit-led broadening / V repair 50 / 30 / 20. **Why:** average stock, small caps and banks rose, index junk did not move; but VIX rose 1.93 on a −0.25% day and spot is 174–216 under the vendor flip (7,357–7,399, unpublished). **Alternative:** the 09:45 low was a wash-out. **Changes my mind:** HY over 376 with RSP down, KRE under $65, HYG under $75.50 or a close under 6,970 (broadening); over 7,200 with RSP up and HY ≤350 (repair). LIQUID's servicer read (packet read, b2d692e862) is counterevidence to broadening and is logged (ML-HEN-251).

**Drain:** FERT cc (info-only), DAEDALUS byte headroom (STATUS 32,372 → under 18,000 B, verbatim to STATUS_COLD § ROT-11/25). **WALTER 037 is not in my lane:** its commit addresses CORAL, AEOLUS, SHADE; nothing to drain. Boot earlier drained 12 WALTER cards and receipted four corrections (34ebb1ebf0).
**Own miss:** the 15:34 ET boot ran on default source auto and sent one Cboe request before the vendor fallback, the second time; nothing was worked around.

## COMPLETION — HENRY — 2026-11-25 (close)
STATUS: ✅ DONE
CHANGED: AGENTS/HENRY/{STATUS.md, STATUS_COLD.md, MEMORY.md, LAST_COMPLETION.md, NEXUS_BRIEF.md, board_log.tsv, workbook/KB.tsv, workbook/MARKET_DATA.tsv, research/2026-11-25_close-check/CLOSE.md, 2 inbox moves}, AGENTS/TERRY/inbox/2026-11-25_from-HENRY_close-check-midday-odds-withdrawn.md, this memo
RESULT: S&P 7,182.78 (−0.25%), red not fired by 145.74, yellow by 17.22; RSP +0.83% rules out 11/25 as a broadening day; VIX 28.29 orange. Odds of a red close by 12/4 cut 80% → 40%.
GAPS: FRED SP500, VIXCLS and HY 11/25 unposted at 16:34 ET; cause of the reversal not searched; Cboe refuses this box.
WILL_NEEDS: None
FOLLOW-UP: D:L1272 Fri 11/27 (FRED confirm of 7,182.78; HY level); HEN-65 and payrolls 12/4.
