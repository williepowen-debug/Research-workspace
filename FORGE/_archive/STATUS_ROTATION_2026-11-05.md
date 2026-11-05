# FORGE STATUS rotation — 2026-11-05

Source: `FORGE/STATUS.md` at `8e50c72a388ea8e08eea087641a0b16f09c9c247` (the Robinhood section as committed for the 11:06 ET capture). Three chunks retained byte-exact, each with its SHA256 and UTF-8 byte count; the read cap forced the move, because the Robinhood after-close reconcile would otherwise have passed 32,550 B. Superseded by the after-close capture; nothing here is live, and every open duty stays in the hot file (D-98, D-99, D-20, D-54).

- **Chunk A** — the Robinhood section body at the 11:06 capture: italic line, banner, table, GONE line, round-trip line. SHA256 `c1b40be3f1287a7f99429dd06c4155dffc21bb976a7d9c5704014b03b0bf4d69`; 2596 UTF-8 bytes.
- **Chunk B** — the D-98 row as first written, with the 11:06 derivations of $1,058.37 and $20.00. SHA256 `3c369cf2a7fe3219e5b19cb8f9d481155a0a22d8f39298a6167b23f5f10819db`; 602 UTF-8 bytes.
- **Chunk C** — the D-70 row before its Robinhood sentence was shortened. SHA256 `976e990930f99ec6c6bb14edd1be5e8417be9b22c0f626af1e9f17d1de96b264`; 455 UTF-8 bytes.

## Chunk A — source

*All cells `[RH 11/5 ≤11:06 ET intraday]`, T excepted. The panel shows P/L and P/L% per line only: every basis and value is IMPLIED (no Mark column ⇒ machine class `unverified` by design).*

> ⚠️ **CAPTURED 11/5, FIRST SINCE 9/29. INTRADAY, NOT A CLOSE. DOES NOT TIE TO THE CENT (D-98).** Two screenshots Will posted 11:06 ET; `AGENTS/TERRY/research/2026-11-05_robinhood-capture/TRANSCRIPTION.md` (TERRY, not independently checked; images not available to ANVIL; fill clocks are relative ages). **Account value $2,349.37 · buying power $1,510.37 · Today +$2,030.37 / +636.48%, so $319.00 at the start of the day (DERIVED).** Vs `568764c2b`: **3 NEW / 0 QTY CHANGE / 1 GONE / 1 MARK ONLY / T no evidence.** Three lines are not on the 9/29 card; the view outranks Will's 10/29 "all dead". Prior rows, 9/29 card (D-64) → `git show 568764c2b:FORGE/STATUS.md`; prediction-market line and 9/01→9/25 dead-by-date bookings USO $159C Sep-11, QQQ $713C Sep-16, USO $165C Sep-16 (D-57, D-58) → rotation 10/08 chunk B.

| Position | Expiry | Qty | Cost | Value | State | Note |
|----------|--------|-----|------|-------|-------|------|
| **QQQ $651P** | Nov-05-2026 | 1 | $4.30 ($430) — Recent row | ≈$587.00 *(implied)* | 🆕 **NEW: +$157.00 / +36.51%** | Bought today. No card seen. |
| **USO $148C** | Nov-06-2026 | 1 | $2.36 ($236) — Recent row | ≈$221.00 *(implied)* | 🆕 **NEW: −$15.00 / −6.36%** | Bought today. No card seen. |
| **WAL $70P** | Nov-20-2026 | 1 | $0.40 ($40) — implied, open unseen | ≈$50.00 *(implied)* | 🆕 **NEW: +$10.00 / +25.00%** | No card seen. TERRY's vendor mid $0.50 (11:07 EST) agrees. Not the Dec-18 line. |
| **KRE $25P** | 1/15/2027 | 1 | $0.53 ($53) — implied | ≈$1.00 *(implied)* | ✅ **MARK ONLY: −$52.00 / −98.11%**, as 9/29 | Entry never recorded — **D-54**. |
| T | stock | 1 | — | — | ⚠️ NO EVIDENCE either way: no stock line in the 11/5 transcription; no stocks card 9/29 | Hypothesis: sold before 9/01, unconfirmed — **D-20**. |

*GONE, no close seen: **WAL $70P Dec-18-2026 ×1** (TRY-WAL-ROLL70, 9/02 @ $2.20, basis $220): the panel ends at "Lists" after four option lines without it. Date, price, realized UNKNOWN; nothing booked (D-98). PB-0006 reads CLOSED on absence; PROME's recount ruling 2 treats that as INFERRED, pending TERRY's contest. `GATE-TERRY-ROLL70-EXIT` RETIRED 11/5 (WQ-610 A).*

*Round trips in view, QQQ 11/5 ×1 each (as transcribed; realized DERIVED; list cut, not the whole day): 672P +$188 · 668P +$141 · 663P +$178 · 658P +$467 · 672C −$149 = **+$825**. Deposit +$5.00.*

## Chunk B — source

| **D-98** 🆕 | Robinhood 11/5 capture does not tie; Recent list cut | 🟠 two gaps | **① $1,058.37 of Today unexplained:** +$2,030.37 − $5.00 deposit − visible +$967 (+$825, QQQ +$157, USO −$15); BP less visible cash +$164 implies opening cash $1,346.37 vs $319.00 start value. **② $20.00:** BP + implied options $859.00 = $2,369.37 vs $2,349.37. Sums re-derived by ANVIL; the transcription itself unchecked | CONJECTURE: ① rows below the cut; ② panels quote differently, or BP ≠ cash. Nothing inferred about unseen rows | **Will** full Recent list, cash detail; **PROME** records |

## Chunk C — source

| **D-70** | Management mappings | 🟡 new RH lines unmapped | PROME source-hash review 2026-11-04: 46 of 47 mappings matched. The 47th, **Robinhood WAL Dec-18 70P**, was removed 11/5 (WQ-612 A): not listed in the 11/5 capture (D-98), exit gate retired (WQ-610 A). Valid hashes are evidence-vintage checks, not current broker truth | Mapping is not a card, trade approval, or proof of a current position | **PROME** mapping/record; **TERRY** card owner |
