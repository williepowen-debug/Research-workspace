# ANVIL -> PROME: FORGE/STATUS.md reconcile to the 10/20 Fidelity capture — awaiting commit authorization

**Run:** ANVIL, Claude Code Agent (model Opus 5.5), spawned by PROME session b94e8a3e, 2026-10-20 11:1x ET. NOT COMMITTED.

## Headline
- Tie VERIFIED independently (Decimal, 23/23 rows): positions $20,870.62 + cash $17,053.29 − pending $83.00 = **$37,840.91**; Σ today G/L −$2,480.70, Σ open G/L −$2,340.98, every row value − basis = open G/L. Activity net 665.32 − 432.66 − 315.66 = −83.00 = pending. Cash continuity 18,574.21 − 1,520.92 = 17,053.29.
- Change vs 10/19 mirror: account −$2,046.38 (positions −$1,963.38, cash −$1,520.92, pending +$1,437.92); snapshot change, not a return.
- Diff (re-derived by parsing HEAD and the new file with positions_from_forge.py): **NEW** QQQ Oct-22 715P ×1 · **QTY** USO Oct-30 165C 1→2 (basis $586.32 = 270.66 + 315.66) · **GONE** QQQ Oct-20 720P ×1 (sold, broker-verified, DERIVED realized +$474.66, booked once) · **21 MARK ONLY**. ⚠️ The transcription §④ and the spawn prompt say 20 mark-only; 23 rows − 1 new − 1 qty = 21. Header records the correction.
- All Fidelity cells are stamped `[10/20 intraday rcv]` (received ~10:43 ET; capture/quote/fill clocks UNKNOWN; not closes). The account is written as •1326 only.
- Per Will's 10/20 11:10 ET preference: I took the per-row "SELL-OR-ROLL before expiry" repeats out of the off-thesis notes. The rail is quoted once in the section banner as Will's own rule (USER.md). No sell recommendation appears anywhere. In D-82 his stated preference is recorded as context, not as a ruling on the WQ-428/429/357 approvals.

## Discrepancy list (urgency-ranked; full text in § Reconcile discrepancies)
1. DATED 🔴 QQQ Oct20 719P ($98) / 715P ($37) expire TODAY; no cards. Owner: Will (TERRY if asked).
2. D-60 🔴 Fidelity ITM-expiry policy is UNKNOWN and there is no underlying QQQ quote. Owner: Will.
3. DATED 🟠 QQQ Oct22 715P (NEW) and CRWV/USO163C Oct23: 2/3/3 DTE, no cards (D-77).
4. DATED 🟡 USO Oct28 165C · CMG Oct30 28P · USO Oct30 165C ×2: 8/10/10 DTE.
5. D-82 🟠 WAL65P4 / OZK40P4 / TBT5 still displayed despite approved sales; no fill in the five-row crop; the OZK backstop is 15:30 ET today. Owner: Will.
6. D-85 🟠 The QQQ719P displayed basis is now $277.66 (+$1.00 vs 10/19). Conditional realized would be −$52.32 vs the prior −$53.32; not certified.
7. **D-87 NEW** 🟡 On 10 option rows (and the USO Oct30 lot, −$15), 10/20 Today G/L ≠ the 10/20 value minus the 10/19 mirror value (−$2 to −$40). The stocks and 5 other options tie exactly. INFERRED: the 10/19 post-close capture marks were not Fidelity's prior-close reference. Record only.
8. D-86 · D-84 · D-78 · D-80 · D-76 · D-70 (this file's bytes changed, so mappings are withheld; the 720P mapping, if any, now describes a closed contract; Oct22 715P and the 2nd USO Oct30 lot are unmapped) · D-77 · D-74 · D-81 · D-83 (Robinhood 21 days old) · D-79 · and the 18 carried rows. All carried; none resolved.

## Consumer verdict (rule 3)
Structure is unchanged: same sections, headers and row conventions. The only header text change is `Mark 10/19 rcv` → `Mark 10/20 intraday rcv`, which is prefix-bound.
- `positions_from_forge.py --selftest` rc=0 (23 live / 3 withheld). The `--json` parse gives 23 live rows, all account Fidelity; the 3 withheld are Robinhood. Σ value = $20,870.62. No warnings.
- `will_brief.parse_money()` → total 37,840.91, cash 45.07%, vintage 2026-10-20.
- `desk_attention.holdings()` → 23 Fidelity + 3 RH rows, no errors.
- `pending_receipts.py` → clean.
- `position_management.tsv` source_sha256: these bytes changed, so every mapping sourced to this file is WITHHELD until PROME re-reviews (D-70).
- **Consumer sweep owed: NO structural sweep. The D-70 mapping re-review IS owed.**

## Artifact
- `git diff --stat -- FORGE/`: `FORGE/STATUS.md | 122 +++---` (63+/59−), 1 file. Nothing staged. PORTFOLIO.md FROZEN banner intact, untouched.
- `measure.py`: FORGE/STATUS.md 29,923 B (wc -c), 166 lines, crc32 1333088703. Under 32,550 B.

**Awaiting commit authorization.** On PROME's word I will commit via `PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md`. If PROME commits itself instead, use the same path. Note that this inbox packet is uncommitted.
