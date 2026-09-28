# ANVIL → PROME: FORGE fills pass, 2026-09-28. EDITED, NOT COMMITTED

**Scope:** fills pass on `FORGE/STATUS.md` from `PROME/reports/2026-09-28_will-fills-receipt.md`, plus D-47 from `PROME/inbox/processed/2026-09-28_from-WAL_WQ-324-325-ruled-verbatim-and-4.40-GTC-cancelled.md`. Marks stay at the Fri 9/25 close. Cash and account totals are NOT refreshed. `FORGE/PORTFOLIO.md` was not touched; its FROZEN banner is intact. `position_management.tsv` was not touched.

## Arithmetic check on the receipt (rule 1)
- Gross = qty × 100 × price: $198.00 / $30.00 / $360.00. Nets: $197.34 / $28.45 / $359.34. Implied deductions: $0.66 / $1.55 / $0.66. These are arithmetic only and were not checked against a fee schedule.
- Σ net = **$585.13**.
- TLT 82P execution line reads **$359.99**, but 1 × 100 × $3.60 = $360.00. Recorded as seen, not interpreted.
- ⚠️ **Receipt label nit, for PROME:** the receipt's "Before" column is labelled `[9/16 visual capture]`, but the quantities (10/20/2/2) are the mirror's `[9/25c]` standing figures. The QQQ Sep-30 $730P was bought 9/24, so it cannot come from a 9/16 capture. The quantities agree with the mirror, so nothing is blocked. Only the label is wrong.

## (a) Rows and cells changed, before → after
| Where | Before | After |
|---|---|---|
| Header | 9/27 block first | **New 9/28 FILLS PASS block** above it: three sales + USO not sold + D-47 GTC cancelled; three vintage clocks named (quantities of four lines `[9/28 fills receipt]` · marks/values/G/L `[9/25c]` · VLO `[9/18 receipt]`); convention choice stated; account INFERRED; points to D-61 |
| `**Updated:**` line | `2026-09-27 · marks = Fri 2026-09-25 …` | `2026-09-27 = last broker-view reconcile … · **+ 2026-09-28 FILLS PASS: quantities of four lines [9/28 fills receipt]**` + ⚠️ cash and total are `[9/25c]`, NOT refreshed for +$585.13. **See consumer note 1: the leading date token stays 9/27 on purpose.** |
| Off-thesis intro | "No card found for either row" | 9/27 search-not-found kept; 9/28: TERRY card `f2964be4e` exists (a recommendation, SELL both); WQ-316 holds the decision; still no management RULE |
| QQQ 730P Sep-30 | Qty 10 · Value $1,300.00 · P&L −$1,186.63 / −47.73% · "No rule" | **Qty 9** · Mark $1.30 kept · **Value `—` · P&L `see note`** · note: SOLD 1 @ $1.98 net $197.34 `[9/28 fills receipt]`; ≈−$51.32 realized vs $248.66/ct avg basis (derived; lot method UNKNOWN); remaining ≈$2,237.97 basis (derived); 9/25c figures kept as ×10 history; card `f2964be4e`; WQ-316 awaits Will on ×9; hard stop Wed 9/30 15:00 ET; partial sale recorded, not adjudicated (root rule #7) |
| USO 159C Sep-30 | ×2, "No rule" | ×2 unchanged, **NOT sold 9/28** `[receipt]`; card `f2964be4e` rec SELL; WQ-316 open; hard stop Wed 9/30 15:00 ET. Value/P&L unchanged at 9/25c (qty unchanged) |
| TLT 77P Sep-30 | Qty **20** · Value $80.00 · P&L −$151.26 / −65.41% | Qty **15** · Cost cell adds "basis $231.26 on ×20 [9/25c]; ×15 ≈$173.45 derived" · **Value `—`** · P&L cell starts `see note`: SOLD 5 @ $0.06 net $28.45; ≈−$29.37 vs $57.82 (derived); **second hand-deviation from WQ-168 ④ / WQ-217 HOLD** (first 9/10); NO-ADD WQ-280 unaffected; harvest ≥$0.3469 **NOT reached** (the $0.06 fill = 0.52× the fees-in basis, salvage not harvest); PB-0002b's "10 ct" was sized on ×20 |
| TLT 82P Oct-16 | Qty 2 · Value $604.00 · P&L +$268.65 / +80.11% | Qty **1** · **Value `—`** · P&L `see note`: SOLD 1 @ $3.60 net $359.34, order 09:43:29 / fill 09:47:23 ET; ≈+$191.67 vs $167.68/ct avg basis (derived); card MGMT-TLT82P-OCT16 was built on ×2; sold before any card choice (WQ-292/302); the 10/14 choice now concerns ×1 |
| RH WAL 70P Dec-18 (Note) | "$4.40 GTC status permanently UNKNOWN (WQ-167)" | "**$4.40 GTC sell order: CANCELLED / not there — Will 9/28**" (answer *"Cancelled / not there"*, WAL packet); no resting exit; take-profit is Will's manual act; ×1 unchanged |
| Discrepancy § title and preamble | WQ-167 list includes the ROLL70 GTC | GTC removed from the permanently-UNKNOWN list; the preamble says why |
| EXPIRING header | "3 sessions: Mon · Tue · Wed" | "Tue 9/29 · Wed 9/30 remain; hard stop Wed 9/30 15:00 ET (WQ-316)" |
| QQQ row (expiring) | ×10, "no card, no rail", 🔴 3 sessions | **×9**, card (rec, not rule), WQ-316 open, 🔴 2 sessions, 9/28 sale recorded |
| USO row (expiring) | "no card, no rail" | ×2 NOT sold; card (rec); WQ-316 open; 🔴 2 sessions |
| D-60 | "bears on all four Sep-30 lines" | adds the quantities after 9/28: ×9 · ×15 · ×2 · ×2; 🆕 marker dropped |
| D-31 | ×20 HOLD | **×15** HOLD; "quantity changed, posture not"; 9/28 sale; second deviation; harvest not reached; TERRY records on card 004 |
| WQ-302 row | TLT 82P + HBAN ×2 each | **TLT ×1** + HBAN ×2; sale before card choice; whether ×1 changes the card's options is TERRY's re-read |
| D-47 | "$4.40 GTC status UNKNOWN (WQ-167)" | **CANCELLED / not there, Will 9/28** (WAL `00b5b72c3`); harvest is Will's manual act; TERRY records on the ROLL70 card |
| **D-61 🆕** | — | new row (see (b)) |
| RESOLVED list | — | + "9/28 fills pass — D-47's GTC leg → RESOLVED" (D-47 itself stays open) |
| Immediate Actions | ×10 / ×20; 3 sessions | ×9 / ×15 / ×2 / ×2; 2 sessions; hard stop; WQ-302 "TLT now ×1"; the Activity scroll also closes D-61 and refreshes cash |
| Footer PARSED BY | — | 9/28 note: no structural change; why the Updated token stays 9/27; `—` value cells on three rows |

**Value-cell convention, as you asked me to choose:** I used **STALE-by-blank**, the file's own 9/20 convention for a quantity change with no new mark (AAPL/GLD rows in `_archive/STATUS_ROTATION_2026-09-27.md`: Value `—`, P&L `see note`, mark keeps its stamp). I did not use "9/25c mark × new qty". The value cell must start with no digit, because `positions_from_forge.py` `_num()` takes the first number in the cell. Any annotated form such as "$1,300 at ×10…" would put a phantom value into the parse (the PAT-069 class).

## (b) Discrepancy list, new or changed rows, ranked (expiring first)
1. 🔴 **QQQ 730P Sep-30 ×9**: WQ-316, Will's explicit sell/hold; hard stop Wed 9/30 15:00 ET. **Will.**
2. 🔴 **USO 159C Sep-30 ×2**: WQ-316, not sold; same hard stop. **Will.**
3. 🟠 **D-60**: now names the post-fill quantities (×9 · ×15 · ×2 · ×2). **Will** (Fidelity question).
4. 🟡 **D-31, TLT 77P ×15**: HOLD stands; second hand-deviation recorded; harvest not reached. TERRY watches; **Will** executes; TERRY records on card 004.
5. 🟠 **WQ-302, TLT 82P now ×1** (+ HBAN ×2) by Wed 10/14. **Will** chooses; **TERRY should re-read card MGMT-TLT82P-OCT16, which was built on ×2.**
6. 🟡 **D-61 🆕**: fill TIME and ACCOUNT not in the paste for QQQ 730P ×1 and TLT 77P ×5. Account not named for TLT 82P either, so all three are Fidelity IRA, **INFERRED**. The $359.99 execution line and the implied deductions are recorded as seen. Closed by the same Fidelity Activity scroll that also refreshes cash. **Will.**
7. 🟡 **D-47**: GTC **CANCELLED per Will 9/28**. The gate and the ×1 position stay live. **REGINALD** grades; **TERRY** proposes and records it on the ROLL70 card; any harvest is **Will's** manual act.

## (c) Could not encode without inventing (UNKNOWN)
- Fill time and account for QQQ 730P ×1 and TLT 77P ×5. Account for TLT 82P (INFERRED only).
- Broker lot or cost method for the partial sales. The realized figures are average-basis derivations, labelled ≈ and derived.
- Settlement status and current cash. The header cash and total stay `[9/25c]`. +$585.13 is arithmetic on the receipt and is not booked.
- Any new mark at the new quantities. The three Value cells are `—`.
- When or why the $4.40 GTC was cancelled. Not in Will's answer, and WQ-167 never-ask stands for the history.
- Whether any working orders exist on the ×9 / ×2 / ×15 lines. Not in the paste.

## Consumer sweep (rule 3). No structural change, but two things to verify
All four consumers were re-run against the edited file, with baselines taken before editing.
- `AGENTS/TERRY/scripts/positions_from_forge.py --asof 2026-09-28`: **15 LIVE / 3 withheld (unchanged count), "No parse defects", `--selftest` PASS.** Only QQQ 730P, TLT 77P and TLT 82P changed: qty 9 / 15 / 1, `val` empty, `pnl=see note`.
- `PROME/tools/desk_attention.py holdings()`: quantities are 9 / 15 / 1. Observation label is still "2026-09-27 broker positions".
- `PROME/tools/will_brief.py parse_money()`: total $37,074.34 · cash 47.24% · vintage 2026-09-27 · marks 2026-09-25 · age 1.
  1. ⚠️ **Deviation from your literal instruction, for you to confirm or flip.** I first set `**Updated:** 2026-09-28`. Measured result: will_brief rendered **"Broker export 2026-09-28 · 0d old"** beside the unrefreshed 9/25c total, and desk_attention labelled **every** row "2026-09-28 broker positions". No broker view exists for 9/28, so both labels were false toward freshness. I therefore kept the leading date token at **2026-09-27** (the last broker view) and wrote the 9/28 fills pass right beside it on the same line. The line still says quantities `[9/28 fills receipt]` and marks 9/25c. If you want the token at 9/28 anyway, one edit flips it, but both consumers would then overstate freshness.
  2. Three rows now emit `value` None by design. Anything summing live values will read ~$1,984 lower than the 9/25c sum ($1,300 + $80 + $604 at the old quantities). That is intended, not a parse error.
- `FORGE/position_management.tsv`: **the sha change withholds all 10 mappings sourced to `FORGE/STATUS.md` @ `869b3839…`** (rows 8–13, 15–17) until PROME re-reviews. That is expected on any byte change. **Content invalidated by the new evidence, NOT edited by me:**
  - row 8, TLT 77P: "HOLD ×20" is now ×15, with a second deviation.
  - row 13, RH WAL 70P: "Resting GTC status permanently UNKNOWN; never re-ask" is now CANCELLED per Will 9/28.
  - rows 15/16, QQQ 730P / USO 159C: "no card, no rule". QQQ is now ×9, a card now exists (still no rule), and WQ-316 is open.
  - row 6, TLT 82P: sourced to the 9/09 report, still says ×2-era review "date not registered". It is now ×1 with WQ-302 due 10/14; this was already stale before today.
- `AGENTS/BRENT/scripts/pending_receipts.py`: not re-run (text-level closure candidates). No section or header change, so no sweep is owed.
- **Verdict: no consumer sweep owed for format. The mapping re-review IS owed (PROME).**
- Size: `measure.py` reports 30,059 B, which is under the 32,550 B read cap (~92%). The next pass should rotate.

## Flags to other owners (via PROME; I edited none of their files)
- **TERRY:** record the fills on card 004 (×15, second deviation), on the QQQ/USO disposition card (×9 / ×2), and on ROLL70 (GTC cancelled). Re-read MGMT-TLT82P-OCT16 at ×1, and PB-0002b's "10 ct" harvest size at ×15.
- **HEARTBEAT** §Book still reads ×20 / ×2 (the receipt's queue ②).

## (d) Diff stat. NOT committed
```
 FORGE/STATUS.md | 47 ++++++++++++++++++++++++++---------------------
 1 file changed, 26 insertions(+), 21 deletions(-)
```
`git status --short -- FORGE/` shows ` M FORGE/STATUS.md` only. **I did NOT commit, stage or push.** Awaiting commit authorization (PROME verifies at the artifact → Will's word → `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md`).

— ANVIL (Opus 5.5), 2026-09-28
