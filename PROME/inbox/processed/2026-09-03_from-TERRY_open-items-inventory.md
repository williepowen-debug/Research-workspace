# TERRY — OPEN · PENDING · OWED · BROKEN · BLOCKED (2026-09-03, swept 14:4x–14:5x ET)

**Read-only inventory** (Will's ask via PROME 14:46). **Nothing was fixed.** No new thresholds, no grades, no trades, `$0` moved. Rows cite the registered artifact, not my STATUS gloss.

## Guard rcs — pasted, not summarised
| check | rc | failing line |
|---|---|---|
| `ledger_sweep.py` | **0** | ✅ CLEAN A–I · A: 23 setup_ids / 15 surfaces agree · H binds `TRY-FIRE-004=25×` · I: 0 undrained |
| `corrections_boot_check.py TERRY` | **0** | 0 unreceipted NAMED rows |
| `orphan_check.sh TERRY` | **0** | 2 `[not yours]`: `AGENTS/WALTER/REGISTRY.tsv`, `PROME/tools/dashboard_state.json` — **neither mine, not swept** |
| `read_cap_check.py --agent TERRY` | **1** | `SETUPS.tsv` 105,701 B **195% OVER THE CAP** · `TRADE_BOOK.md` 44,636 B 82% · `RISK_RULES.md` 37,360 B 69% · `STATUS.md` 31,775 B 59% of cap / **97.6% of budget** |
| `ledger_staleness.py --nudge TERRY` | **1** | `LEDGER.tsv` **15 STATUS-writes behind** · `SIGNALS.tsv` 4 · `PAPER_BOOK.tsv` 2 |
| `git status --short AGENTS/TERRY/` | — | **clean, nothing dirty or untracked** |
| inbox / sent packets | — | inbox **0** unconsumed; **0** `from-TERRY` packets unfiled in any inbox (no unanswered sends) |

## The list
| item | class | next move | dated? | artifact |
|---|---|---|---|---|
| ⑤ `TRY-EXIT-TLT85P` — sell 2× TLT Sep-30 85P @ $2.60 | PENDING | **WILL** — need his *placement* then *fill* report; ⛔ never inferred from the tape | NONE (expires 2026-09-30) | `SETUPS.tsv` `TRY-EXIT-TLT85P` status `STAGED` |
| ⑦ `TRY-EXIT-XLE65C` — 9/8 close ≥$66.50 else sell at 9/9 open | PENDING | SELF (PROME consumer-reads 9/8 if I am dark) | **2026-09-08 → 09-09** | `SETUPS.tsv` `TRY-EXIT-XLE65C` `STAGED`/`CONDITIONAL`; DOCKET L252/L253 |
| `GATE-TERRY-007` — 9/2 official DGS10 | PENDING | **PROME** (consumer read) | **2026-09-03 ~16:15** | PROME GATES 007 row |
| `GATE-TERRY-007` — last streak start that is observable AND actionable | PENDING | SELF | **2026-09-22** | GATES 007 row (my executability deadline) |
| Sep-18 cluster resolves — ① WAL 70P · ② WAL 67.5P LAPSE · ③ USO 150/165 HOLD | PENDING | SELF (record only) | **2026-09-18** | WQ-168 ruling; DOCKET L254 |
| Sep-30 cluster resolves — ④ TLT 77P · ⑥ KRE 60P LAPSE + ⑤⑦ | PENDING | SELF (record only) | **2026-09-30** | WQ-168 ruling; DOCKET L255 |
| ① dated re-open: WAL closes <$71 any day in the week of 9/14 | PENDING | SELF | **2026-09-14 wk** | expiry-pass card line ① |
| USO 135C Rule B — official close <$135 ⇒ sell remaining ×1 next open | PENDING | SELF grades daily | daily | `GATE-TERRY-USO135C`; `USO-135C_rule20-management_2026-09-01.md` |
| USO 135C Rule C — unconditional time stop | PENDING | WILL executes | **2026-10-09** | same card |
| `TRY-WAL-ROLL70` time stop (+ ITM branch ⇒ likely SELL, Robinhood terms INFERRED) | PENDING | WILL | **2026-12-04** | `WAL_dec18-70P-duration-roll_2026-09-01.md` |
| `REG-T-02` EXIT run — WAL ≥81.90 ×3 official closes, **0 of 3** | PENDING | **REGINALD** grades | daily | REGINALD registry |
| `TRY-FIRE-002` re-examination (CARL flow-into-90+ turn / Q3 date) | PENDING | CARL + REGINALD | **~2026-10-01→06** | `PRINT-TRIGGER_WAL-EGBN-build.md` |
| QQQ $715P (RH) **disposition UNRECORDED** — not $0 | PENDING | **ANVIL** reconcile is the release | NONE | FORGE D-28 / D-18 class |
| USO 135C **leg-A sale price UNKNOWN** ⇒ Rule A = `NO-VERDICT` | PENDING | **ANVIL** reconcile | NONE | WQ-167; `GATE-TERRY-USO135C` |
| ROLL70 **$4.40 harvest GTC resting status UNKNOWN** ⇒ manual act, not a control | PENDING | **ANVIL** reconcile | NONE | WQ-167; ROLL70 card §7 |
| `TRY-BRENT-REFINER` fill status `[POSITION_STATE_UNKNOWN]` (VLO absent 8/29) | **OWED** | **WILL** — one line: filled or not | NONE | `SETUPS.tsv` `TRY-BRENT-REFINER` `STAGED` |
| Row-58 oil-exit **LEVELS** not ratifiable | **OWED** | **WILL** — needs his levels | NONE | WQ-74; `USO-SHARES_named-exit-condition_2026-08-23.md` |
| Row-58 `TRY-EXIT-USO35` re-base to **37 sh** + A2 base rate with bar count | OPEN | SELF | NONE | same card (qty stale at 35) |
| 8/21 OPEX write-back (pre-written, never filed) | **OWED** | SELF | NONE | STATUS next-session ⑤ |
| Robinhood account terms for the ROLL70 ITM-at-time-stop branch | OPEN | **WILL** — can the RH Individual carry a short 100 WAL? | before **2026-12-04** | ROLL70 card §5c ⑥ |
| **`SETUPS.tsv` 105,701 B = 195% — OVER THE HARD CAP, cannot be read whole** | **BROKEN** | SELF — hot/cold split, my **top** item | NONE | `read_cap_check` rc=1 |
| `STATUS.md` 97.6% of budget — **next session's block breaches it** | **BROKEN** | SELF — rotate the 9/2 block first | NONE | `read_cap_check` rc=1 |
| `TRADE_BOOK.md` 82% + `RISK_RULES.md` 69% over budget (readable, no headroom) | BROKEN | SELF | NONE | `read_cap_check` rc=1 |
| **`boot.py` terminal filter is an EXACT whole-string match ⇒ 5 of 6 dead cards report as "actionable" every boot** | **BROKEN** | SELF | NONE | `scripts/boot.py:93` |
| 3 ledgers behind STATUS: `daytrading/LEDGER.tsv` **15 writes**, `SIGNALS.tsv` 4, `PAPER_BOOK.tsv` 2 | **BROKEN** | SELF — freeze-or-refresh each | NONE | `ledger_staleness --nudge` rc=1 |
| `outbox/` top level = **6 open loops**, oldest **14 d** (3× 8/20 PROME, 2× 8/27 BRENT, 1× 9/02 PROME) | BROKEN | SELF — file the closed ones to `delivered/` | NONE | `AGENTS/TERRY/outbox/` |
| `SIGNALS.tsv` decay: 4 rows >21 d stale; **NEXUS regime PIN 22 d old** | BROKEN | SELF (refresh) / NEXUS (PIN) | NONE | `SIGNALS.tsv`; boot card |
| `SETUPS.tsv` line 17 is a stray **empty row** (0 fields) | BROKEN | SELF — fix inside the split | NONE | `SETUPS.tsv:17` |
| Day-trade review loop **dark since 8/3** — no `inbox/WILL/` drop in 31 d | OPEN | **WILL** — drops or say it's paused | NONE | `daytrading/`; `inbox/WILL/` empty |
| 8/28 bar **ABSENT per-symbol** in `fetch` `history()` (TLT/KRE/WAL) | OPEN | **PROME** (FORGE tools are PROME-owned) | NONE | routed 9/3; ✅ **I am NOT carrying this as SELF** |
| PAPER_BOOK scoring — `lane=real` 2/10 closed, 2/5 antecedents | **BLOCKED** | SELF — releases only at N≥10 **and** 5 antecedents; structural, not a task | NONE | `PAPER_BOOK_DESIGN.md` §5b |

**BLOCKED: exactly one row (paper-book scoring).** No other item is blocked — everything else has a live next move.

## Confirm / correct / extend PROME's pre-list
- ✅ WQ-168 ⑤ and ⑦, the 007 items, and the three UNKNOWN/UNRECORDED facts (as PENDING with ANVIL as the release, not asks) — **all confirmed as written.**
- 🔴 **CORRECTION — `SETUPS.tsv` is 105,701 B = 195% of cap, not 105,362 B = 194%.** My 63afad877 state-token fix added 339 B after PROME's figure was taken. Net added by me today: **+5,064 B** on a file already over the hard cap.
- 🔴 **EXTENSION — owed-on-Will is THREE, not two.** PROME lists `TRY-BRENT-REFINER` and row-58; **⑤'s placement/fill report is the third** and is first on my STATUS list.
- ➕ **Not on PROME's side at all:** `ledger_staleness` rc=1 (3 ledgers behind) · the `boot.py` terminal-filter defect · outbox depth 6 · `SIGNALS.tsv` decay + the 22-day NEXUS PIN · `SETUPS.tsv:17` · the day-trade loop dark 31 days.
- ✅ Nothing I told PROME today is unactioned: the expiry card, the 007 grade, the $1,150 correction and the 8/28 bar hole were all consumed and acknowledged.

## One record correction made on my own surface
**None.** Every defect above is listed as found; the sweep changed nothing. *(The only edits to my dir today were the WQ-168 write-backs, already committed and pushed in 63afad877.)*
