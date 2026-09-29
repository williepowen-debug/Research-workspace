# ANVIL → PROME: FORGE reconcile to the 9/29 intraday captures (REPORT, awaiting commit authorization)

**From:** ANVIL (spawned by PROME `prome-e6`, 2026-09-29 13:5x ET) · **Written:** 2026-09-29 ~14:0x ET · **Source:** `PROME/data/2026-09-29_broker-capture-TRANSCRIPTION.md` · **Files edited:** `FORGE/STATUS.md` (modified) · `FORGE/_archive/STATUS_ROTATION_2026-09-29.md` (new, untracked). Nothing else was touched. **No commit made.**

## 1. Arithmetic, checked independently from the transcription tables (the clerk has no image access)

| Check | Result |
|---|---|
| Σ position values + cash = account total | $18,720.83 + $18,102.04 = **$36,822.87** ✓ to the cent (no pending shown); cash 49.16% ✓ |
| Σ Today $ / Σ Total G/L $ | −$845.38 ✓ / −$479.55 ✓ |
| Per-row value = last × qty (×100) · G/L = value − basis · today = chg × qty (×100) | 15 of 15 ✓ on every dollar cell |
| % cells and avg cost | 14 % cells and 2 avg-cost cells (AAPL 23.645, APD 294.785) differ by 0.01: broker rounding. Shown values kept |
| Ledger chain (prior + amount = balance) | **33 of 34 links ✓**; the single break is 9/28 17,740.43 + 359.34 = 18,099.77 vs shown 18,099.32 (**D-62**, PROME's finding reproduced) |
| 9/28 ledger vs the 9/28 fills receipt | QQQ 730P +$197.34 ✓ · TLT 82P +$359.34 ✓ · **TLT 77P: three rows Σ $28.43 vs the receipt's $28.45 (Δ $0.02, new; kept on D-61)** · Σ $585.11 vs receipt $585.13 |
| Cash bridge | $17,514.66 (9/25-close cash + pending) + $585.11 = $18,099.77 → positions $18,102.04 ⇒ **+$2.27** (+$2.72 vs the shown balance) — **D-63** |
| RH card | $265.00 + $1.00 + $15.21 + $8.94 = $290.15 vs $295.15 ⇒ **$5.00** — **D-64** |
| RH D-59 | buys −$380.00 · sells +$27.00 · deposits +$233.05 ⇒ −$119.95 vs BP −$120.43 ⇒ Δ −$0.48 ✓ (PROME's figure reproduced) |

The transcription passes rule 1. The dollar totals close exactly. The two unexplained items (D-62 and D-63) are in the broker's own views, not in the transcription's arithmetic.

## 2. Task 1: reconcile, row by row

**The claim "ALL ROWS = MARK ONLY" holds.** I checked qty and avg cost against the mirror at HEAD (`9ef686295`) for every row:

| Row | Mirror qty/cost | Capture qty/cost | Verdict |
|---|---|---|---|
| AAPL · GLD · USO · VLO · APD · TBT | 10 · 17 · 37 · 1 · 2 · 10 | same; costs same | MARK ONLY ×6 |
| QQQ $730P Sep-30 | 9 `[9/28 fills receipt]` @ $2.49 | 9 @ $2.49, basis $2,237.97 | MARK ONLY; ×9 now **broker-CONFIRMED** |
| USO $159C Sep-30 | 2 @ $4.61 | 2 @ $4.61 | MARK ONLY |
| TLT $77P Sep-30 | 15 `[receipt]` @ $0.12 | 15 @ $0.12, basis **$173.44** | MARK ONLY; **restated at ×15** |
| TLT $82P Oct-16 | 1 `[receipt]` @ $1.68 | 1 @ $1.68, basis **$167.67** | MARK ONLY; **restated at ×1** |
| KRE $60P Dec-18 lots | 2 @ $2.57 · 3 (M) @ $2.93 | same | MARK ONLY; two-lot structure kept |
| KRE $60P Sep-30 | 2 @ $2.27 | same | MARK ONLY |
| APO $95P · HBAN $16P | 1 @ $11.85 · 2 @ $0.96 | same | MARK ONLY |
| RH WAL $70P · KRE $25P | 1 · 1 | 1 · 1 | MARK ONLY (derived values) |
| RH T share | 1 (hypothesis: sold) | not on card, no activity row | unchanged, D-20 |

There are no NEW rows, no QTY CHANGE and nothing GONE. Every Fidelity mark, Value, P&L and Today figure is refreshed and labelled `[9/29 13:4x intraday]`. None of them is labelled as a close. The three sold-down rows (QQQ 730P, TLT 77P, TLT 82P) carry numeric Value and P&L again, because the broker now marks them at the new quantities. Realized P&L on the 9/28 sales was re-derived from the broker basis deltas:
- QQQ −$51.32
- TLT 77P −$29.39 (on the ledger's $28.43)
- TLT 82P +$191.66 (was derived as +$191.67 on 9/28)

**Header:** cash $18,102.04 (49.16%) · total $36,822.87 (−$251.47 vs 9/25c) · RH $295.15, BP $8.94 (+$67.00 vs 9/27).

**Gate proximity (rule 7; nothing adjudicated):**
- TLT 77P: $0.08 = 0.69× its $0.11563 fees-in basis. The harvest line (≥$0.3469) is NOT reached.
- TLT 82P: +156.45% is a mark, not a card option firing.
- WAL 70P: +20.45% is not the ROLL70 gate, which reads WAL's own close (0-of-3 as last recorded; not re-read this pass).

## 3. Task 2: `§ Reconcile discrepancies`, rebuilt and ranked by urgency

**Expiring Wed 9/30 (hard stop 15:00 ET):**
1. **QQQ 730P ×9.** Will decides (WQ-316). $1,143.00, −48.93%.
2. **USO 159C ×2.** Will decides (WQ-316). $2.00, −99.79%.
3. **D-60 (NARROWED).** The four penny "OPTION LIQUIDATION" rows (IWM 9/04 +$1.97 · QQQ 716P 9/08 +$0.99 · QQQ 710P 9/18 +$3.77 (Margin) · QQQ 730P Sep-25 9/25 +$1.97) show that OTM liquidation is OBSERVED. Their OTM status is INFERRED from the proceeds, because the ledger shows no underlying price. Three others show EXPIRED with no cash row (QQQ 716P Sep-21, WAL 70P and 67.5P Sep-18). **Two things are still open:** (i) what happens to an in-the-money long option at expiry is UNOBSERVED; (ii) what decides liquidate vs expire is UNKNOWN. This bears on QQQ 730P ×9 and TLT 82P. Owner: Will, via the Fidelity question.
4. **D-31 TLT 77P ×15.** HOLD, ruled. TERRY watches the harvest line, Will executes.
5. **WQ-168 ⑥ KRE 60P Sep-30.** LAPSE, ruled.

**Will decides / PROME re-reads:**
- **WQ-302:** Will's A/B/C choice on TLT 82P ×1 and HBAN ×2 is due Wed 10/14.
- **D-62 🆕 ($0.45 ledger break):** PROME re-reads the image cell. The positions cash ties better to the arithmetic balance than to the shown one. That is a lean, not proof.
- **D-63 🆕 (+$2.27 cash bridge):** unattributed; candidates are a money-market dividend, the APD dividend or interest. Owner: Will, low.
- **D-64 🆕 ($5.00 RH card gap):** Will. The 9/27 card closed to the cent by the same method, so this is new.
- **D-65 🆕 (my own finding, not in PROME's list):** the RH 9/14–9/15 put/call labels don't pair.
  - A 707 **Put** was bought, then a 707 **Call** was sold.
  - A 708 **Call** was bought, then a 708 **Put** expired, while both 708P buys read Canceled.
  - Hypothesis: the 9/15 "Call" labels should read "Put", which would give 707P +$104 and 708P −$41. That is labelled, not booked. No live position depends on it and it falls outside the D-59 window.
  - PROME re-reads the image.
- **D-61 (NARROWED):** the account leg is CLOSED. Still open: fill TIMES for QQQ 730P and TLT 77P, plus the $0.02 receipt-vs-ledger gap on TLT 77P.
- **D-59 (NARROWED to −$0.48).** The window start is INFERRED: the 9/16 capture shows that day's 713C buy, so it was taken after the last 9/16 row.
- **D-45 pre-view residual (NEW leftover, flagged):** the ORIGINAL 8/28→9/03 +$3,702.46 bridge still leaves **+$43.81** between the 8/28 cash + pending ($14,323.25, from the 8/29 record) and the ledger's derived 9/01 opening ($14,367.06). That falls before the view starts, so it needs Activity for 8/28–8/31.
- **D-55:** VLO fill time is still missing.
- **Carried, still open (all pre-9/01 or not in these views):** D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1.

**Owner decides:**
- **D-47:** the gate stays open. The **entry is CONFIRMED**: bought 9/02 @ $2.20 = $220.00, with two same-day attempts Canceled.
- Also carried: VLO-SCALE · WQ-200 · APD tag.

**RESOLVED this pass:**
- The 9/28 quantities are broker-CONFIRMED.
- **D-61 account leg → CLOSED.**
- **D-44 → CLOSED:** 9/02 +$2,125.00, which is $708.33/sh on 3 sh. The quantity is INFERRED because the ledger shows none. That is ≈−$19.23 against the broker 3-sh basis of $2,144.23.
- **D-45 → CLOSED** on its 9/10 definition. The 9/3 capture cash of $18,025.71 equals the ledger balance after 9/02 to the cent, and the 9/03 IWM 293P −$85.33 is exactly the residual.
- **D-57 → CLOSED:** 713C −$167.00 and 165C −$150.00, both expired $0 on 9/16.
- **D-58 RH leg → CLOSED:** −$152.00, expired 9/11.
- **Recorded as seen, not verified by me:** the RH "USO Call Debit Spread $630.00" on 9/10. The transcription doesn't show direction; PROME reads it as the close.

## 4. Task 3: consumer verdict (rule 3)

- **Structure: no breaking change.** Sections, table headers, column order and row conventions are the same. `Mark 9/25` became `Mark 9/29`, which binds by prefix.
- **`positions_from_forge.py --selftest`: rc=0, SELFTEST PASS.** Live run: 15 live / 3 withheld (the RH `unverified` class, by design), no parse defects, no warnings. The live values sum to **$18,720.83**, which equals the broker's Σ positions.
- **`will_brief.parse_money()`** returns `{'total': '36,822.87', 'cash_pct': '49.16', 'vintage': '2026-09-29', 'marks': '2026-09-29', 'age': 0}`. It will render "Broker export 2026-09-29" even though the marks are intraday. The header text says NOT a close, but the rendered brief will not carry that caveat.
- **`desk_attention.holdings()`:** 18 rows, 0 errors.
- **`position_management.tsv` `source_sha256`:** ⚠️ **every mapping sourced to FORGE/STATUS.md is now withheld until PROME re-reviews and re-hashes it.** The file changed byte-for-byte, as on every pass, so **a mapping review is owed at commit**. Rows sourced elsewhere are not affected.
- **`AGENTS/BRENT/scripts/pending_receipts.py`:** rc=2, *"CANNOT CERTIFY: missing TRADE section: POSITIONS (live)"*. That error names BRENT's own `AGENTS/BRENT/TRADE.md` (script line 49/64), not FORGE. It looks INFERRED unrelated to this edit, but I did not run it against the HEAD version, so this is UNVERIFIED. It is flagged for BRENT through PROME.
- **Consumer sweep owed: NO** for structure. **YES** for the `position_management.tsv` re-hash review (routine on every byte change).

## 5. Task 4: byte cap

- `FORGE/STATUS.md`: **27,981 B** (`measure.py`, crc32 3491208405). It was 30,396 B; the cap is 32,550 B.
- Rotation file `FORGE/_archive/STATUS_ROTATION_2026-09-29.md` (18,438 B, crc32 1399141383) holds two chunks, both proven byte-identical to the source with `in`-checks:
  - **Chunk A** = HEAD lines 5–11, the 9/28 + 9/27 header blocks (4,390 B · crc32 1230443836).
  - **Chunk B** = HEAD lines 93–158, the 9/27-built discrepancy list with its RESOLVED list, plus Immediate Actions (12,463 B · crc32 42615261).
- The receipts are written in the file's header. The superseded row cells are left in git at `9ef686295`, as the header says. The live file points to the rotation file from its first banner and from the discrepancy preamble.
- `FORGE/PORTFOLIO.md`: the FROZEN banner is intact and the file was not touched.

## 6. Diff stat and tree

```
 FORGE/STATUS.md | 132 ++++++++++++++++++++++++++++----------------------------
 1 file changed, 65 insertions(+), 67 deletions(-)
?? FORGE/_archive/STATUS_ROTATION_2026-09-29.md   (new — a commit must `git add` it explicitly and name it in the pathspec)
```

The four dirty WALTER paths already in the tree belong to another agent and were left alone. Side note for PROME: `.claude/agents/anvil.md` § "Known state at last edit" is stale (it still says 9/03). That file is outside my scope for this run.

**For the commit, when authorized:** `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md FORGE/_archive/STATUS_ROTATION_2026-09-29.md`, after an explicit `git add` of the new archive file.

**⛔ NO COMMIT MADE — awaiting commit authorization.**
