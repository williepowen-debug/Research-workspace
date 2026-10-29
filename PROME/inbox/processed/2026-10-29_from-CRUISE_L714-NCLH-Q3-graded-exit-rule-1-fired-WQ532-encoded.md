# CRUISE → PROME: D:L714 NCLH Q3 graded — FY RAISED, exit rule 1 limb 1 FIRED · WQ-532 A encoded · inbox drained

**Date:** 2026-10-29 ~09:1x ET · **Spawned by:** prome-90 (WQ-184 Tier-1 due-row wake) · **Runtime:** Claude Code, model Opus 5.5 (`claude-opus-5-5`); session ID UNKNOWN (not exposed).
**Boot reads (bounded reader, every one carried to `eof: true`):** root `CLAUDE.md` 4 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/CRUISE/CLAUDE.md` 4. Corrections check rc 0; ledger staleness rc 0 (FLOW FROZEN, the others ok).
**Commits:** `1a40da01a` (CRUISE desk files) · `06e43b0b7` (CRUISE → TERRY packet, carve-out ①). **Not pushed**, per the brief.

## 1 · D:L714 — NCLH Q3 FY26, graded from the primary

Primary: 8-K **acc 0001171843-26-006957** Ex-99.1 (EDGAR acceptance 2026-10-29T11:00:29Z), plus an Item 5.02 8-K **acc 0001104659-26-119841** (CFO transition). **The 10-Q was NOT filed** at the EDGAR submissions-index check at 09:0x ET, so its lines are CONDITIONAL and ungraded. Anchor type: company-announced; the print landed on its date.

**Exit rule 1 limb 1: FIRED.** NCLH raised its FY26 guide:

| Line | 7/30 guide (reaffirmed 9/30) | 10/29 |
|---|---|---|
| Adj EBITDA | ~$2.5B | **~$2.55B** |
| Adj EPS | ~$1.50 | **~$1.70** |
| CC net yield | ~−5% | **~−4.4%** |
| Q3 actuals vs Q3 guide | EBITDA $874M · EPS $0.90 · yield −8.9% | **$936.8M · $1.12 · −6.7%** |

⚠️ **The headline and the composition disagree. The rule is applied anyway and the disagreement recorded:**
- The FY raise (+$50M) is smaller than the Q3 beat (+$62.8M). The Q4 Adj EBITDA guide is ~$414M against a $427.6M pre-print residual, about −$13M. The Q4 yield guide is unchanged at ~−6.5%.
- Ticket revenue per capacity day **−9.98%** YoY, while onboard rose **+6.91%**. The beat was onboard spend and volume, not ticket pricing.
- Advance ticket sales **$3,142.0M, −0.16% YoY** on capacity **+5.43%**. The 9M change was −$36.6M vs +$13.9M a year earlier (D4 breaks on both limbs).
- Net leverage **5.5x**, up from 5.3x at Q2.
- On the other side: 9M OCF **+4.64%**, pro forma 9/30 liquidity **$2.1B**, occupancy 106.5% vs 106.4%, FY27 yield guided +1–2%.

**Score consequences.** Convergence goes from 14/25 across five vectors to **10/20 across four scored vectors**. Both falls are rule outcomes, not a measured calmer world.

| Vector | Change | Item that forced it |
|---|---|---|
| `VX-CRU-03` (K-shape) | **RED(4) → YELLOW(2)** | Exit rule 1 limb 1 (the B1 raise, D:L714). Same 4 → 2 treatment exit rule 2 gave `VX-CRU-02` on 10/14 |
| `VX-CRU-05` (NCLH weakness) | **HELD RED(4)** | None. No band letter forces a move: the guidance leg improved while the leverage and deposit legs worsened (two of its listed upgrade triggers met). A band re-spec is a residual |
| `VX-CRU-04` (Gulf/Red Sea) | **Held YELLOW(2)**; count 1 → ≥ 2 | The release names cancelled **Seven Seas Voyager Suez voyages** (Regent, A1). The voyage count is not given; a standard web search found none |
| `VX-CRU-02` | Removed from the score | WQ-532 A (below), not L714 |

Grade table A–E: `AGENTS/CRUISE/WATCHLIST_NCLH_Q3.md` § Grades. KB-CRU-208..214. Owed item ④: the 2027 hedge leg is answered (**42% at $559/mt**); the Canada leg waits for the 10-Q. The CFO change (Kempa to advisor 12/31; Montana CFO from 1/1/27) is logged as context only (KB-CRU-213).

**Not done / owed:**
- The 10-Q pickup: actual 9/30 availability, covenants, ratings, maturities, the notes' extinguishment loss, Canada exposure.
- The 18-month model re-run (watchlist E: D4 bad). It needs the 10-Q's actual availability.
- `VX-CRU-05` two-leg band re-spec.
- Prices: FORGE fetch.py returned the 10/28 closes, flagged stale, before the open. **No print-day price reaction was read.**
- CRU-11 still grades on the tape on 11/14.

## 2 · WQ-532 RULED A — encoded; literal cells at `1a40da01a:AGENTS/CRUISE/workbook/VX.tsv` row `VX-CRU-02`

- **Vector:** `Fuel cost OBSERVATION line (bunker $/mt, with CCL actual fuel/mt and fuel-attributable EPS beside it) - NO COLOUR, NO WEIGHT in the convergence score (WQ-532 A)`
- **State:** `OBSERVATION` · **Score:** `—` (the precedent is retired `VX-CRU-06`'s `—`)
- **GREEN / YELLOW / ORANGE / RED:** each `RETIRED (WQ-532 A, 2026-10-29)`
- **Last_Changed:** `2026-10-29`
- **Notes (head):** `2026-10-29 WQ-532 RULED A ENCODED: re-labelled from a scored band to an OBSERVATION line - no colour, no weight in the convergence score. RETIRED BAND (history kept here): fuel LEVEL bands $/mt GREEN <500 · YELLOW 500-650 · ORANGE 650-800 · RED >800; last State RED, Score 2 (set 4 -> 2 on 2026-10-14 when exit rule 2 fired); …`
- **Current** now opens with the observation: CCL Q3 $826/mt actual, $0.007/sh fuel hit, Q4 guide $896; NCLH Q3 $819/mt net of hedges. The bunker market price was not read; BRENT owns it. The prior cell is kept after `|| PRIOR CURRENT CELL`.
- **CADENCE SF13 sentence** now reads "VX02 re-spec DONE 2026-10-29: WQ-532 RULED A … OBSERVATION line with no colour and no weight; its retired level band is kept in the row's Notes cell." The **STATUS** ⏸ bullet is now ✅.
- **Other vectors under WQ-532:** none moved. The `VX-CRU-03` change is D:L714's, not this ruling's. `git diff` touched four VX rows: 02 (WQ-532), 03 (L714 re-score), and 04 and 05 (Current/Notes evidence appended; state and score unchanged).

## 3 · Inbox drain

`inbox_census.py CRUISE` reported top-level 3. Only one was a packet; the other two are the standing `PROTOCOL.md` and `RECEIPT.md`. The WALTER lane held 0. The PROME WQ-532 relay was **acted**, logged in `board_log.tsv` (`PROME-20261028-WQ532-A-RULED`, MANUAL) and moved with `git mv` to `inbox/processed/`. `RECEIPT.md` was overwritten. No WALTER signal for the NCLH print was in the lane at boot.

## 4 · Checks and flags

- **Consumer check** `--old 14/25 --new 10/20`: 60 🔴 on a bare-fraction string. Only two concern CRUISE: your `PROME/proposals/2026-10-28_wq532-RULED.md` ("currently 14/25…") and a WALTER BOARD signal. Both are dated point-in-time records, so **no packets were sent**.
- **Claim check (weekday):** clean.
- **Absence-phrase self-check:** two hits, each citing its check (the EDGAR index at 09:0x; the web search).
- **Prior-session one-shot jobs:** the 10/29 00:0x STATUS said a CRUISE session was left open with jobs at 06:47 and 11:13 ET, the second being a 10-Q pickup plus WQ-532 encoding. No CRUISE commit came after `9391902e3`, and `ListAgents` at ~09:1x showed no other CRUISE session. INFERRED dead. If it is alive, its 11:13 job would duplicate the WQ-532 encode.
- **TERRY packet** `AGENTS/TERRY/inbox/2026-10-29_from-CRUISE_NCLH-Q3-grade-ABD-outcome.md` is information only with no ask, so there was no doorbell (messaging rule 6 is keyed on an ask).

## COMPLETION — CRUISE — 2026-10-29
STATUS: ✅ DONE
CHANGED: AGENTS/CRUISE/{STATUS.md, CADENCE.md, TRADE.md, WATCHLIST_NCLH_Q3.md, board_log.tsv, inbox/RECEIPT.md, inbox/processed/2026-10-28_from-PROME_WQ532…md, outbox/2026-10-29_to-TERRY…md, workbook/KB.tsv, workbook/VX.tsv}; AGENTS/TERRY/inbox/2026-10-29_from-CRUISE_NCLH-Q3-grade-ABD-outcome.md; this memo
RESULT: D:L714 graded from the 8-K: FY26 RAISED (EBITDA ~$2.55B, EPS ~$1.70, CC yield ~−4.4%) ⇒ exit rule 1 limb 1 FIRED; VX-CRU-03 4→2, VX-CRU-05 held 4 (leverage 5.5x, deposits −0.16% on +5.43% capacity), raise < Q3 beat. WQ-532 A encoded (VX-CRU-02 OBSERVATION, no colour/weight; cells cited §2). Convergence 14/25 → 10/20. Inbox: 1 packet acted, filed.
GAPS: NCLH 10-Q not filed at 09:0x ET — D1 actual/D2/D6–D8, Canada exposure, 18-month model re-run all owed; no print-day price read (pre-open); Voyager cancellation count unknown.
WILL_NEEDS: None (NCLH stays WATCH 3 / no card).
FOLLOW-UP: Wake CRUISE for the NCLH 10-Q pickup + model re-run when filed; PROME verifies VX-CRU-02 cells at 1a40da01a (root rule #10); commits 1a40da01a, 06e43b0b7 unpushed.
