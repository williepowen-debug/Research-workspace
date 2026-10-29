# ANVIL → PROME — FORGE reconcile to Will's 10/29 post-close capture (anvil-1029) — AWAITING COMMIT AUTHORIZATION

**Written 2026-10-29 18:34 ET (`date`).** Claude Code subagent `anvil` (Opus 5.5), spawned by PROME prome-5c. Edit on disk: `FORGE/STATUS.md` only, uncommitted. SendMessage is not available in this harness, so this file plus my final text is the delivery.

## 1. Headline

| Item | 10/22 mirror (`ec5a7058b`) | 10/29 capture `[10/29 close rcv 18:25 ET]` | Δ |
|---|---|---|---|
| Account total | $39,876.06 | **$39,159.02** | −$717.04 |
| Positions | $22,399.20 | $24,810.30 | +$2,411.10 |
| Cash (money market) | $15,807.97 | $13,386.72 (34.19%) | −$2,421.25 |
| Pending | +$1,668.89 (processing trades) | +$962.00 ("Margin credit balance", Will 11:58 ET) | −$706.89 |
| Today / open G/L | — | +$527.49 / −$2,726.32 (−8.79% on $31,021.88) | — |

- **Rule 1 check, done again by ANVIL:** all 28 rows: value = last × qty (×100) to the cent, and open G/L = value − basis (for the short leg, value + credit). Σ values $24,810.30 + cash + pending = $39,159.02 ✓. Σ Today +$527.49 ✓. Σ G/L −$2,726.32 ✓. 11 rows show an open % that is 0.01 pt off G/L ÷ basis (rounding, D-79). The transcription holds.
- **Row classes:** 10 NEW long lines (QQQ Oct-30 711P ×2 · QQQ Oct-30 710P ×1 · QQQ Nov-02 715P ×1 · GLD Nov-02 375C ×2 · USO Nov-20 170C ×1 · QQQ Nov-20 690P ×2 · KRE Nov-27 68P ×10 · VLY Dec-18 12P ×1 · FLG Mar-19-2027 10P ×1) + 1 NEW SHORT (QQQ Nov-20 670P ×−2) / 4 QTY CHANGE (AAPL 4→3 · GLD 25→28 · USO 35→30 · TBT 5→10) / 7 GONE / 13 MARK ONLY (one of them is the 10/22 VLY open order, now a position; I count it under NEW).
- **No realized P/L booked.** No ledger came with this capture. The DERIVED window identity is in D-90: sales + other cash flows − round-trip buys = **+$3,026.50**; minus removed basis $2,676.35 gives **+$350.15** for realized results plus other cash flows across the window. That is an aggregate only, not booked, and its split is UNKNOWN.
- **GONE, outcomes unseen and nothing booked.** Expiry date passed: QQQ Oct-22 717C, CRWV Oct-23 56P, USO Oct-23 163C, QQQ Oct-26 710P (marked +$325.34 on 10/22), USO Oct-28 165C. Gone before expiry: USO Oct-30 165C ×2 and CMG Oct-30 28P. Removed basis $2,058.28. I did not infer a worthless expiry for any of them.
- **Robinhood:** rows kept and bannered "not in this export's account, unverified today". Will's word 10/29 ("all dead", written off) is recorded with its source (TERRY NOTE). Nothing was deleted.

## 2. Discrepancy list (ranked by urgency, expiring items first)

### Will decides or supplies

| # | Item | Urgency | Known / conjectured |
|---|---|---|---|
| DATED | QQQ Oct-30 711P ×2 ($1,350) · QQQ Oct-30 710P ×1 ($613) · USO Oct-30 163C ×1 ($545) | 🔴 1 DTE | Recorded only, per USER.md § No expiry nagging. No cards. |
| D-60 | Fidelity handling of expiring options | 🔴 next 10/30 | Five more expiry dates passed this window with outcomes unseen. Broker auto-liquidation is INFERRED. ITM exercise has never been observed. |
| DATED | QQQ Nov-02 715P ×1 ($1,047, +116.02%) · GLD Nov-02 375C ×2 ($102) | 🟠 4 DTE | The +116.02% is a mark. No harvest or disarm line is registered for this contract. |
| **D-90 NEW** | Activity & Orders 10/22→10/29 unseen | 🟠 | Covers every quantity change, all 11 new lines, 7 GONE outcomes and the cash+pending drop of −$3,128.14. USO basis relief was $594.42, not the $609.49 average cost would give: either specific lots or unseen offsetting trades. GLD added at $366.25/sh and TBT at $38.72/sh, both DERIVED and both assuming plain adds. **Round 2 resolves this.** |
| D-88 | QQQ Oct-20 715P disposition | 🟡 | Unchanged. The ledger would need to reach back to 10/20. |
| D-89 | Working orders | 🟡 NARROWED | VLY filled. Its $15.66 basis is consistent with a fill at the $0.15 limit (DERIVED). This capture has no Orders page, so working orders at 10/29 are UNKNOWN. |
| D-82 | Approved sells not evidenced | 🟡 NARROWED | **TBT leg CLOSED** on Will's word (WQ-357 resolved, "no sale owed"). OZK 40P ×4 ($40) and WAL 65P ×4 ($100) are still held at the close. |
| D-84 / D-86 / D-80 / D-76 / D-78 | Earlier unseen fills, lots and VLO scope | 🟡 | Carried with current state. CRWV and CMG under D-84 are now GONE. |
| D-83 | Clock / Robinhood | 🟡 | Post-close lasts, not settles. Robinhood is 30 days old and written off by Will's word; the rows are kept. |
| 18 carried | D-75 · D-66 · D-69 · … · D-1 | 🟡 | All OPEN and unchanged. D-66 now covers every fill clock in this window. |

### PROME or another desk decides

| # | Item | Urgency | Owner |
|---|---|---|---|
| **D-91 NEW** | **Short-leg representation (consumer interface).** The 670P is written with a signed Qty `−2` and a negative value. `positions_from_forge.py` parses it correctly (qty −2.0; Σ live values $24,810.30 ties). **`desk_attention.py holdings()` raises `FORGE line 88: quantity unknown`**: it expects `^\d+`. The row is still emitted, so the failure is loud, not silent. | 🟠 **before commit** | **PROME** (owns desk_attention); TERRY (parser) |
| D-70 | `position_management.tsv` mappings withheld (source bytes changed). Seven GONE contracts' rows now describe absent lines, and the 11 NEW rows are unmapped. | 🟡 | PROME; TERRY cards |
| D-74 | Bank-put ownership. The cluster is now 41 contracts / $6,644.24 basis, against 28 / $4,646.62 on TERRY's 10/24 view. KRE 68P ×10, VLY and FLG have no owner or card. | 🟡 | PROME scope; Will/REGINALD/TERRY |
| D-77 | Off-thesis cards. Six lines have no card. The 690/670 spread does have one (TERRY `IDEA-QQQ-PUTWALL-OCT22`). | 🟡 | PROME scope; Will/TERRY |
| D-85 / D-87 / D-81 / D-79 | Records | 🟡 | PROME |

### Rule 7: gate text written beside each number
- **QQQ 690/670 ×2.** Net $754.00 against the $936.70 debit, which is $3.77 per spread from two lasts. Card § 6: harvest "≥ $10.00 … on the broker bid" (a last-price difference is not a bid); kill "SPX cash close ≥ 7,750 on two consecutive sessions" (not read); time stop Fri 11/13 close.
- **GLD `MGMT-GLD-SHARES-OCT24`.** 1-month line "GLD close < $360.71". The $368.57 last is $7.86 / 2.13% above it. It is not a close and was not graded.
- **VLO `GATE-TERRY-VLO-HELD-01`.** Leg A is the ULSD crack settlement below $90.16, a crack-basis gate. The stock's −11.03% reads nothing on it.
- **`MGMT-KRE65P-DEC31`.** Time stop Thu 12/31 15:00 ET; not a price gate.
- **USO.** WQ-200 declined; no live rule.
- No gate adjudicated.

## 3. Consumer verdict (rule 3)
- `positions_from_forge.py --selftest`: **rc=0**, 19/19 PASS, live file 28 live / 3 withheld (the Robinhood rows, unverified), no parse defects. A full parse shows 28 live rows, Σ value $24,810.30 = the transcription.
- `will_brief.parse_money()`: total 39,159.02 · cash 34.19% · vintage 2026-10-29 · marks "2026-10-29 post-close" · marks_known True ✓.
- `desk_attention.forge_vintage` ✓. **`holdings()`: 31 rows, 1 error (D-91, the short leg's signed qty).**
- `AGENTS/BRENT/scripts/pending_receipts.py`: rc=0, clean.
- `position_management.tsv`: source_sha256 changes, so mappings are withheld (D-70, expected).
- **Sweep verdict: a consumer sweep IS owed** for the new signed-Qty convention, which is recorded in the PARSED-BY footer. The narrowest fix is in `desk_attention.py` (accept a leading `−`/`-`). The alternative, an unsigned "2 short" Qty, would make TERRY's parser read the short as +2 long: that is a phantom long, the PAT-069 class, so I did not choose it. Headers, section names and the header money line are unchanged. The spread legs sit in the existing "Other puts" table, so no new section was added.

## 4. Diff and size
- `git diff --stat FORGE/` → `FORGE/STATUS.md | 146 +++---- (72 insertions, 74 deletions)`. No other FORGE path touched. `PORTFOLIO.md` FROZEN banner intact.
- `measure.py`: **32,517 B** against the 32,550 B cap, **33 B of headroom**. No rotation was needed: I got under the cap by replacing my own duplicated guards summary with a pointer, and the gate text stays beside the numbers. ⚠️ **Round 2 (the ledger) will need a hot/cold rotation FIRST.** Candidates: the historical italic lines (TLT, WAL Sep-18, Event-box, prior terminal records) moved verbatim to `FORGE/_archive/STATUS_ROTATION_2026-10-29.md`.

## 5. Awaiting
**AWAITING COMMIT AUTHORIZATION.** Nothing is committed and nothing will be pushed. On your word I commit via `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md` and report the hash. I am staying reachable for round 2 (the Activity ledger) and the D-91 decision: either keep the signed Qty and sweep desk_attention, or tell me a different representation.
