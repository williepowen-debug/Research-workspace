# ANVIL → PROME — 9/10 reconcile, BOTH captures (Fidelity CLOSE + Robinhood 16:10) — FORGE/STATUS.md edited, NOT committed
**Written:** 2026-09-10 16:30 ET (supersedes this memo's 16:3x first version) · **Inputs:** `PROME/data/2026-09-10_fidelity-close-capture-TRANSCRIPTION.md` + `PROME/data/2026-09-10_robinhood-capture-1610-TRANSCRIPTION.md` · **Artifact:** `FORGE/STATUS.md` uncommitted — `git diff --stat -- FORGE/`:  1 file changed, 44 insertions(+), 40 deletions(-)

## Headline
- **Vintage now "9/10 CLOSE (Fidelity) + 16:10 ET (Robinhood)"**; the ⚠️ MARKS-ARE-INTRADAY header warning retired (stays for nothing).
- **Fidelity account $39,885.25** = Σ positions $19,261.81 + cash $19,335.00 + pending $1,288.44 — **re-verified independently to the cent**; today **+$463.50 / +1.18%**; open G/L **+$1,796.64 / +10.29%** on $17,465.17. Every one of 15 rows re-marked to the CLOSE cells (Last · Value · Today · Total G/L) `[Fidelity positions, 9/10 CLOSE]`. **Quantities UNCHANGED vs ~10:3x (15 rows); the close-view ledger = the morning's four rows ⇒ no new fills.** D-49 (XLE 1-lot) left OPEN, no date inferred.
- **Robinhood $946.13 (▲ $364.54 / 62.68%), BP $489.69 [16:10]**; USO 150/165 spread **CLOSED +$330.00** (struck); **USO 159C Sep-11 ×1 @ $1.52 added — expires TOMORROW (Fri, CPI)**; QQQ 713C −$11.00 struck (Robinhood table, same `~~` convention — placement flagged); WAL 70P +$10.00; KRE 25P → **D-54** (entry never recorded); prediction line recorded, no D-row.
- **WQ-200 proximity (rule 7, not adjudicated): 9/10 CLOSE USO $158.38 = ABOVE "≥$152.96 official close"** (9/9 close $149.97 below). ⚠️ ORCH_LOG L82 logs a 12:46 TERRY "WQ-200 decline receipt" — the file now says "queue status per PROME, unverified here" rather than OPEN. **PROME confirms the queue status.**

## Arithmetic (rule 1) — both transcriptions VERIFIED
**Fidelity CLOSE:** all 15 rows value = last×qty ✓, G/L = value − basis ✓, today = Δ×qty ✓, both % ✓; Σ values / Σ today / Σ G/L / Σ basis all tie (19,261.81 / 463.50 / 1,796.64 / 17,465.17); 1,796.64/17,465.17 = 10.29% ✓; 463.50/39,421.75 = 1.18% ✓; cash 48.48% ✓. **One labeled correction to the transcription's gloss:** "Today +$463.50" = Σ of the open rows' day change EXACTLY ⇒ it does NOT include realized fills (the note said "incl. realized"). Not a cell error — the cells are right.
**Robinhood 16:10:** $216 + $230 + $1 + prediction $9.44 + BP $489.69 = $946.13 to the cent ✓ (needs BP = cash and "26.22" = contract count — both INFERRED); $581.59 × 62.68% ✓; $630 − $300 ✓; all three P/L% ✓. Not decomposable: the day's +$364.54 (no 9/9 close marks).

## ⚠️ Task premise refuted at the artifact (item 3)
KRE $25P Jan-2027 has been on the mirror since the **7/16 reconcile (`6568be33e`, −$52/−98.1%; 7/20 `bb54321ef` −$38/−71.7%)**; no duplicate row added. D-54 opened only for the never-recorded entry date/price, with the "NOT new" correction in the row. Same class as D-34/D-41 (8/29).

## Discrepancy list — one list, both captures, urgency-ranked
| # | Item | Urg. | Known | Conjectured (labeled) | Owner |
|---|---|---|---|---|---|
| — | RH USO $159C Sep-11 ×1 expires TOMORROW | 🔴 1 DTE | $1.52 in; ≈$2.16 at 16:10 | none | Will (his hand; no ask) |
| D-49 | XLE 65C ×1 survivor; 1-lot sale still outside BOTH ledger views | 🟠 20 DTE | 1.47 / $147, −35.44% | (a)/(b)/(c) unchanged; ANVIL picks none | Will (Activity before 9/10) |
| D-53 · D-45 · D-44 | 153C entry · −$190.35 bridge · QQQ 3 sh | 🟠/🟡 | unchanged | — | Will (same view) |
| WQ-200 | LINE-1 harvest — CLOSE 158.38 ABOVE the line | 🟡 | proximity only | queue status = the 12:46 decline receipt? | TERRY grades / **PROME confirms** |
| D-47 | RH WAL 70P +$10.00 / ≈$230 | 🟡 | guard 0-of-3 since 9/2 | — | REGINALD / TERRY |
| D-31 | TLT 77P ×20 — 0.08 / $160, 0.69× fees-in | 🟡 | GATE-TERRY-007 0-of-5 | — | TERRY |
| WQ-168 ①②⑥ | WAL pair LAPSE; KRE 60P Sep-30 now 0.01 / $2 | 🟡 | fully specified | — | REGINALD / rides |
| D-28 | RH QQQ 715P outcome; 8/28→16:10 cash bridge ≈+$68 unattributed | 🟡 | labeled arithmetic | 715P proceeds and/or inflow | next RH history |
| **D-54 NEW** | RH KRE 25P entry never recorded | 🟡 | on mirror since 7/16 | ≈$0.53 derived | Will, when convenient |
| D-20 | T share — 16:10 sum closes with no stock line ⇒ not held (INFERRED) | 🟡 | $8.67 residue gone | T sold | Will |
| D-37 · D-18 · D-17 · D-1 | carried, unchanged | 🟡 | — | — | — |
**Closed this run:** WQ-168 ③ (spread CLOSED by Will's hand). **UNKNOWN written as UNKNOWN:** spread legs / per-contract price · KRE 25P entry · the RH +$364.54 decomposition · 713C exact times.

## Every cell changed
**Robinhood pass (16:3x):** L5 header · L7 scope · L9 event box · L11 RH account · L13 (+RH arithmetic) · L33 USO parenthetical (cross-ref) · L51 blurb · L97 RH banner (+prediction) · WAL 70P · USO spread (struck) · +USO 159C · +QQQ 713C (struck) · KRE 25P (D-54) · D-preamble · +159C row · −WQ-168 ③ row · WQ-200/D-47/D-28/D-20/D-37 · +D-54 · Immediate Actions ×3 · footer ×2.
**Fidelity CLOSE pass:** L5 header (vintage; intraday warning retired) · L7 · L9 (+no-new-fills) · L11 (cash % 48.48, Σ positions, total, session, G/L) · L13 (CLOSE verification; the four-row half-cent note dropped — moot at close cells) · L27 stamp · **every Longs row** (AAPL · GLD · USO incl. WQ-200 text, energy sleeve $6,007.06 = 15.06%, 52-wk 158.88 · APD · TBT incl. 52-wk 39.67 · XLE) · TLT 77P (0.08 / $160, 0.69×) · TLT 82P (1.96 / $392, +$56.65) · duration-short line (+$53.71) · KRE 60P Sep-30 (0.01 / $2) · APO (0.85) · HBAN (0.25) · KRE 60P Dec ×2 rows and WAL pair UNCHANGED (same cells at close) · D-preamble · D-49 · WQ-200 row · D-31 · WQ-168 ⑥ · Immediate Actions WQ-200 · footer ×2. Byte trims (no fact removed): L5 pointer shortened, D-45 example range dropped, D-53 tail, scope-banner D-45 sentence.

## Consumer sweep (rule 3) — NOT owed
No header/section/column change; Fidelity cells re-marked in place. Parser `AGENTS/TERRY/scripts/positions_from_forge.py`: **15 live / 14 withheld, warnings []**, selftest PASS; live marks read = the CLOSE cells (spot-checked all 15). Baseline before this run 15 / 12.

## Byte cap · process residue
`measure.py` → **FORGE/STATUS.md  32426 B (wc -c)  168 lines (wc -l)  crc32 1766503892  crc32-no-final-nl 1125997247** (cap 32,550). Two trim passes were needed (33,539 → 32,465 after RH; 32,785 → now after CLOSE) — **that is the two-correction stop on this file: ANVIL makes no further edit to FORGE/STATUS.md this session**; any further change needs a cold read first, and a rotation (the struck RH spread / 713C rows are the cold candidates). Declared residue: none ❌; ⚠️ the WQ-200 queue-status sentence in the USO row and the D-table is PROME's to settle.

## Git
Nothing staged; `git status -- FORGE/` shows only STATUS.md. Other dirty paths (AGENTS/BOND/*, PROME/state/board_cursor.txt, memory/auto/…) = other sessions' live work, untouched. This memo uncommitted. **Awaiting commit authorization** → `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md`.

## COMPLETION — ANVIL — 2026-09-10
STATUS: ✅ DONE
CHANGED: FORGE/STATUS.md (uncommitted), PROME/inbox/2026-09-10_from-ANVIL_robinhood-1610-reconcile.md
RESULT: Both 9/10 captures reconciled: Fidelity CLOSE $39,885.25 verified to the cent, 15 rows re-marked, qty unchanged, D-49 left open; Robinhood $946.13 verified, spread CLOSED +$330.00, USO 159C Sep-11 added (expires tomorrow), QQQ 713C −$11.00 struck, D-54 opened. Parser 15 live / 14 withheld, warnings [], selftest PASS, no consumer sweep owed; file FORGE/STATUS.md  32426 B under the 32,550 cap.
GAPS: Item 3's "KRE 25P not on any prior mirror" is false at the artifact (on the mirror since 7/16) — no duplicate row. Transcription gloss "Today +$463.50 incl. realized" is wrong (it is Σ open-row day change exactly) — cells unaffected. Two-correction stop reached on STATUS.md — no further ANVIL edits this session.
WILL_NEEDS: None beyond standing captures (Fidelity Activity before 9/10 → D-49/D-53/D-45/D-44; RH dated history → D-28/D-54/D-18).
FOLLOW-UP: PROME verifies at the artifact → commit go; confirm WQ-200 queue status (12:46 decline receipt) and close WQ-207 / TRY-MGMT-USORH150165 / BRENT row on the spread; rotation before the next STATUS edit.
