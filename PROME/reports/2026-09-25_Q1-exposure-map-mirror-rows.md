# Q1 — PROME's mirror-derived rows for TERRY's exposure map (Will-directed 02:55 ET 9/25; DOCKET L477)

**Basis:** `FORGE/STATUS.md` (three vintages: standing quantities `[9/16 13:57 visual capture]`, VLO `[9/18 receipt]`, marks `[9/10 CLOSE]`) — ⚠️ **WQ-274: NOT transaction-reconciled, NOT current-book-verified.** These rows give TERRY the line, the mirror quantity with its vintage, and PROME's read of which scenario each line loses or gains under; **TERRY owns the management-rule column, the "loses together / offsets" verdict and the §9 test.** Scenarios: (a) oil falls, real yields stay high · (b) both fall · (c) credit broadens while oil stays high · (d) quiet through the 9/30 expiry. "Needs reconcile" = the conclusion depends on a quantity or existence the mirror cannot certify.

| Line (mirror row) | Qty [vintage] | Direction of the bet | (a) oil ↓, real ↑ | (b) both ↓ | (c) credit broadens, oil high | (d) quiet to 9/30 | Needs reconcile? |
|---|---|---|---|---|---|---|---|
| 004 TLT Sep-30 $77P ×20 (Fidelity) | 20 `[9/16]` (25→20, 5 sold 9/10 by Will) | short duration | flat/gain (already ~$0.01 bid; TLT $79.42 [9/24c] is $2.42 above strike) | loses the residual (bid $0.01 → $0) | flat | expires worthless Wed 9/30 (harvest gate ≥$0.3469 unreachable) | N — quantity is the one cell the 9/16 capture corrected |
| TLT Oct-16 $82P ×2 | 2 `[9/16]` | short duration | gain | loss | mild gain (flight to quality lifts TLT? — direction ambiguous, TERRY) | decay | Y — ⚠️ NO RULING on file for this line |
| KRE Dec-18 $60P ×5 (two lots) | 5 `[9/16]` | short regional banks | gain if real ↑ hurts banks' duration books; loses if oil ↓ eases stress | loss | **gain** (the line built for (c)) | decay | N |
| KRE Sep-30 $60P ×2 | 2 `[9/16]` | short regional banks | ~0 (LAPSE ruled WQ-168 ⑥) | 0 | small gain only on a crash before Wed | expires 9/30 | N |
| APO Dec-18 $95P ×1 | 1 `[9/16]` | short alt-manager / private-credit vehicle | mixed | loss | **gain** (private-credit redemption stress = (c)) | decay | Y — no ruling on file; BROCK thesis vehicle |
| HBAN Oct-16 $16P ×2 | 2 `[9/16]` | dust (Will 7/18: rides to expiry) | ~0 | ~0 | small gain | expires | N |
| WAL Dec-18 $70P ×1 (Robinhood) | 1 `[9/10 verified; 9/16 corroborated]` | short FL/AZ regional bank | as KRE | loss | **gain** | decay; `GATE-TERRY-ROLL70-EXIT` WAL ≥$81.90 ×3 (0-of-3, WAL $76.26 [9/24c]) | N |
| KRE Jan-15-2027 $25P ×1 (Robinhood) | 1 `[9/16 corroborated]` | deep-OTM lottery | ~0 | ~0 | ~0 unless systemic | ~0 | N |
| USO 37 sh | 37 `[9/16 = matched control cell]` | long crude | **loses** (the whole line: ≈$5,664 at $153.09 [9/24c], 100% undefended, WQ-200 declined) | **loses** | gain/flat (oil high) | flat | N for quantity; **Y for any P/L figure** (cost $122.28, mark 9/10 stale) |
| GLD 17 sh | 17 `[9/16]` (+1 unrecorded, D-56) | long gold (net long duration via real yields) | **loses** (real ↑ is the MIDAS beta, −0.186 %/bp) | gains | gain (flight) | flat | Y — the +1 share has no recorded fill |
| TBT 10 sh | 10 `[9/16]` (−4 unrecorded) | short duration (2× inverse 20Y+) | gain | **loses** | mixed | flat/decay | Y — the −4 has no recorded fill |
| AAPL 10 sh | 10 `[9/16]` (−5 unrecorded) | long equity | loses mildly (rates ↑) | gains | loses | flat | Y — the −5 has no recorded fill |
| APD 2 sh | 2 | long industrial | ~0 | ~0 | loses mildly | flat | N (thesis tag unassigned since 7/30) |
| VLO 1 sh held @ $412.00 [9/18] (+2 STAGED under WQ-213/VLO-SCALE) | 1 held, 2 staged | long refining margin (crack) | **loses if the crack collapses with crude** (F1 <$95 stands the staging DOWN — Q5: does the held share share that thesis?) | loses | gain/flat | flat | **Y — account + fill time UNKNOWN (D-55)** |

**PROME's reading, for TERRY to confirm or refute (this is the §9 test):**
- **(a) oil ↓ with real yields high** is the scenario where the two largest lines lose together — USO (crude) and GLD (real-yield beta) — while the duration shorts (004 residual, TBT, Oct-16 82P) gain little because 004 is already at a one-cent bid. Net: the book is NOT one bet in (a); it is a crude-long plus a gold-long that both lose, offset only marginally.
- **(b) both ↓** is the "Mideast cools" scenario: USO, TBT, the TLT puts and the KRE/WAL puts all lose; GLD gains. This is the single-shared-falsifier case §9 describes — and it is real: roughly every line except GLD and AAPL loses.
- **(c) credit broadens with oil high** is where the bank/credit puts (KRE ×5+2, WAL, APO) finally pay while USO/VLO hold: the book's only diversifying scenario, and the one the transmission test (Q2/Q4) says is NOT yet in evidence.
- **(d) quiet to 9/30:** two expiries (004 ×20, KRE Sep-30 ×2) go to zero on schedule; nothing else moves; the staged VLO shares are the only capital that could act.
- **Reconciliation dependence:** the qualitative map holds without it; **any dollar figure per line does not** (marks 9/10; four unrecorded stock fills; VLO account unknown). The §9 sleeve totals are kill-on-sight until a broker mark (HEARTBEAT §KOS).
