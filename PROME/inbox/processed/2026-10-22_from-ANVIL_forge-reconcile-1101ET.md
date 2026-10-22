# ANVIL → PROME: FORGE reconcile to the 10/22 11:01 ET Fidelity capture — AWAITING COMMIT AUTHORIZATION

**From:** ANVIL (Claude Code subagent, Opus 5.5, spawned by PROME desktop session a5be8f8c) · **Written:** 2026-10-22 11:1x ET (`date` 11:11:08 EDT at final checks) · **Channel:** SendMessage not exposed in this harness → this file + final text (contract rule 10).

## 1. Tie (re-verified independently from the transcription)

| Check | Result |
|---|---|
| Σ 25 position values | **$22,399.20** ✓ |
| + cash $15,807.97 + pending +$1,668.89 | **$39,876.06** = displayed total ✓ to the cent |
| Σ today G/L / Σ open G/L | −$797.28 ✓ / −$1,659.13 ✓ |
| Per row: last × qty (×100) = value; value − basis = open G/L; basis ÷ qty = avg cost | **25/25** ✓ |
| Pending = 8 "Processing" rows (sells $3,067.94 − buys $1,399.05) | +$1,668.89 ✓ |
| Ledger cash after last 10/21 row = displayed cash | $15,807.97 ✓ |
| GLD basis $9,019.37 + $371.41 | $9,390.78 ✓ |
| Display-only noise | 13 rows' open-% differs by 0.01 pt from G/L ÷ basis (broker rounding); recorded in D-79, no figure affected |

## 2. Row classes vs last mirror `100c63edc` (23 rows → 25)

| Class | Count | Rows |
|---|---|---|
| NEW | 5 | QQQ Oct-26 710P ×1 · QQQ Oct-22 717C ×1 · USO Oct-30 163C ×1 · KRE Nov-20 66P ×3 · KRE Nov-27 70P ×2 |
| QTY CHANGE | 1 | GLD 24 → 25 |
| GONE | 3 | QQQ Oct-20 719P (liquidated 10/20) · QQQ Oct-22 715P (sold 10/22) · QQQ Oct-20 715P (**disposition not evidenced → D-88**) |
| MARK ONLY | 19 | as transcription § ④ |
| Between-captures round trips (history lines, never rows) | 3 | QQQ Oct-21 715P −$221.67 · Oct-23 717P +$607.65 · Oct-26 720P +$921.65 |
| Open order (not booked) | 1 | VLY Dec-18 12P ×1 buy limit $0.15 → D-89 |

Parser: 25 live (sum $22,399.20) / 3 withheld (the Robinhood rows, unverified by design).

## 3. Realized — one correction to the transcription's figure

- **QQQ Oct-20 719P cohort: −$120.99**, independent of how basis is allocated (10/19 buy 2 −$554.32, 10/19 sell 1 +$224.34, 10/20 liquidation +$208.99).
- The 10/19 mirror already carried **−$53.32** for the first leg (conditional). The transcription books the second leg at **−$68.67** (10/20 displayed basis $277.66). Added together those make −$121.99, so **$1.00 is counted twice**. The leg consistent with what is already booked is **−$67.67**.
- Five lines closed since the 10/20 mirror: **+$1,537.62** on the consistent split, or PROME's +$1,536.62 on the display basis. The parts that do not depend on the split: four lines **+$1,605.29**, plus the 719P cohort −$120.99. All of these are DERIVED, not a broker realized-P/L report. Recorded in D-85 (narrowed).

## 4. Discrepancy list (urgency-ranked; expiring first)

**Will decides / supplies:**

| # | Item | Urgency | Note |
|---|---|---|---|
| DATED | QQQ Oct-22 717C ×1 (NEW) | 🔴 expires today | Value $38 on $154.66 basis. Recorded only, not a prompt (`USER.md` no-expiry-nagging rule) |
| D-60 | Fidelity expiring-option handling | 🔴 | **NARROWED:** the ledger shows broker "OPTION LIQUIDATION" rows on expiry day (719P 10/20, Oct-21 715P 10/21; also the Oct-02 740P per position_management.tsv). INFERRED: the broker liquidates some expiring contracts itself. The trigger, timing and initiator are still UNKNOWN |
| DATED | CRWV Oct-23 56P · USO Oct-23 163C | 🟠 1 DTE | Recorded only |
| **D-88 NEW** | QQQ Oct-20 715P disposition | 🟠 | Absent; basis $200.66; no ledger row is visible. **Cash bridge leaves +$17.34 unexplained:** 10/20 capture cash+pending $16,970.29 − $223.66 + $208.99 = $16,955.62, against the ledger's 10/20 closing balance of $16,972.96. HYPOTHESIS (labeled): the gap fits a sale or liquidation of this 715P at about $0.18 less fees (conditional realized −$183.32). It could equally be another credit we can't see. Nothing is booked. Will can settle it with the 10/20 Activity rows below the cut |
| **D-89 NEW** | Working-order census | 🟠 | The VLY 12P buy order was Open at capture. The 11th order is unseen (INFERRED: the 710P buy) |
| D-82 | Approved sells (WAL 65P ×4, OZK 40P ×4, TBT ×5) not evidenced | 🟡 record | All still held; no sell order among the 10 visible orders. Carried with no reminder language |
| D-84 / D-86 / D-80 | Unseen 10/19 fills · three expired contracts absent · 10/15 gaps | 🟡 | Unchanged, because this ledger window starts at 10/20 |
| D-78 | VLO extra-share scope | 🟡 | Unchanged |
| D-83 | Clock / Robinhood | 🟡 | Robinhood data is 23 days old |

**Owner (PROME / TERRY / REGINALD) decides:**

| # | Item | Owner |
|---|---|---|
| D-85 (narrowed) | Cohort −$120.99 booked; per-leg split still open; the transcription double-counts $1.00 | PROME |
| D-70 | Mapping re-review: the source bytes changed. Rows for the Oct-20 719P/715P and Oct-22 715P now describe absent contracts; the 5 NEW rows and the added GLD share are unmapped | PROME |
| D-74 | NEW KRE 66P ×3 and 70P ×2: owner/card UNKNOWN. They sit under the KRE heading for navigation only | PROME scope; Will/REGINALD/TERRY |
| D-77 | 8 off-thesis rows (incl. NEW 717C, 710P, USO Oct-30 163C) + KRE 67P have no card | PROME scope; Will/TERRY |
| D-76 | Fill lots/prices: the 710P and USO 163C buys show ledger nets only | Will lots; PROME/TERRY |
| D-87 | Can't be tested on this capture (two sessions apart; 10/21 reference marks not captured) | PROME record |
| D-81 · D-79 | Historical cash mismatch · display precision | PROME record |
| 18 carried | Unchanged (rotation 10/08 D1/D2) | as recorded |

No D-row closed. D-60 and D-85 narrowed; D-88 and D-89 new.

## 5. Consumer verdict (rule 3)

- `positions_from_forge.py --selftest` **rc=0** (25 live / 3 withheld, no parse defects). The parsed value sum is $22,399.20 = the tie.
- `will_brief.parse_money()` → total 39,876.06 · cash 39.64% · vintage 2026-10-22 · marks "2026-10-22 intraday" (known) ✓.
- `desk_attention.holdings()` → 28 rows (25 Fidelity + 3 RH) ✓.
- `BRENT pending_receipts.py` rc=0.
- `position_management.tsv` source_sha256: **withheld by design** (D-70 re-review owed).
- **No structural change:** sections, headers and row conventions are preserved. Only the `Mark <m/d>` header text changed, which binds by prefix. → **No consumer sweep owed.**

## 6. Byte size and rotation

- The draft measured 34,042 B, over the 32,550 B cap, so I did a **hot/cold split**. New `FORGE/_archive/STATUS_ROTATION_2026-10-22.md` (14,566 B; sha256 `214faaea…5b7e`) holds four byte-exact chunks from `100c63edc`, each with a SHA256 and byte count:
  - A: the 10/14 740P / USO Oct-14 terminal records
  - B: the TLT terminal records
  - C: the WAL Sep-18 expiry record
  - D: the 10/20 discrepancy section + Immediate Actions, kept for provenance
- Each moved chunk is replaced by a pointer line. I also trimmed duplicated new prose from this run; no history text was compressed.
- **`FORGE/STATUS.md` is now 32,002 B (`measure.py`), 548 B under the cap. ⚠️ The next run will need another rotation first.** sha256 `81bf6e37…25ad`.

## 7. Git

- `git diff --stat -- FORGE/`: `FORGE/STATUS.md | 141 +++---- (71 insertions, 70 deletions)` plus untracked `?? FORGE/_archive/STATUS_ROTATION_2026-10-22.md`.
- **Commit pathspec must name BOTH files:** `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md FORGE/_archive/STATUS_ROTATION_2026-10-22.md`. The spawn prompt named only STATUS.md; the rotation file is the split the task list required.
- Plus this inbox report (PROME's to commit).

## 8. What I did NOT change

`FORGE/PORTFOLIO.md` (FROZEN banner intact, untouched) · `FORGE/position_management.tsv` (D-70 is PROME's) · the Robinhood rows (9/29, only the banner's day-count changed) · the 18 carried D-rows · gates/GATES.tsv · any other agent's dirty files · no live quote fetched (the export stamp was enough; no decision needed a fresh price) · no commit, no push.

**Awaiting commit authorization.**
