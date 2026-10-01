# ANVIL → PROME: FORGE/STATUS.md reconciled to the 10/1 INTRADAY capture — AWAITING COMMIT AUTHORIZATION

**From:** ANVIL (FORGE reconcile clerk), spawned by PROME `prome-0c` · **Written:** 2026-10-01 12:31 EDT (`date`) · **Source:** `PROME/data/2026-10-01_broker-capture-TRANSCRIPTION.md` · **Base:** `git show HEAD:FORGE/STATUS.md` (= `33bc8c293`, confirmed byte-identical to HEAD before editing) · **Edited:** `FORGE/STATUS.md` only (nothing created in `FORGE/_archive/`) · **NOT COMMITTED.**

## Headline — Fidelity Traditional IRA (*1326, INFERRED by position-set match), marks `[10/1 intraday ≤12:24 ET]`, not a close

| Figure | 10/1 intraday | 9/30 post-close mirror | Δ |
|---|---|---|---|
| **Account total** | **$37,727.55** (Today +$96.70 / +0.26%; open G/L +$3,144.69 / +17.29%) | $36,384.93 | **+$1,342.62** (intraday vs post-close, so not a close-to-close move) |
| **Cash (money market)** | **$14,147.60** (37.50%) | $18,102.04 | the 9/30 −$4,007.98 has settled; **+$53.54 above** the $14,094.06 the mirror implied (D-69) |
| **Pending activity** | **+$2,245.00** (the four 10/1 sales) | −$4,007.98 | — |
| **Realized 10/1** | **+$982.02**: QQQ 740P ×5 +$890.35 · USO 150C ×1 +$91.67 | 9/30: −$3,755.12 | — |
| Robinhood | not captured; the 9/29 card stands ($295.15 / BP $8.94), labelled | — | — |

**Where the +$1,342.62 came from (it adds up exactly):**
- **+$708.00** is the three KRE Dec lines moving off their $0.01 post-close marks ($7.00 → $715.00). That is a valuation artifact unwinding, not a market move.
- **+$476.00** is the four sales coming in above the 9/30 marks on the contracts sold ($2,245.00 vs $1,769.00).
- **+$105.08** is mark moves on the rest of the book.
- **+$53.54** is the unexplained cash (D-69).

**My own arithmetic check (I did not rely on PROME's § ④):** Σ positions $21,334.95 + cash $14,147.60 + pending $2,245.00 = **$37,727.55 to the cent ✓**. Value = last × qty (×100) holds on all 15 rows ✓. G/L = value − basis holds on all 15 rows ✓. Σ Today = +$96.70 ✓. Σ G/L = +$3,144.69 ✓. Σ basis $18,190.26 = the 9/30 mirror's $19,453.24 minus the $1,262.98 of basis sold today ✓. The four fills sum to +$2,245.00 = Pending ✓. The 13 unchanged lines have the same bases as the 9/30 mirror to the cent.

## What changed in the mirror
- **QQQ $740P Oct-01: 9 → 4.** Sold to close 10/1:
  - 1 @ $3.44 → +$343.34
  - 1 @ $3.97 → +$396.34
  - 3 @ $3.72 on a $3.66 limit → +$1,113.98

  Total proceeds +$1,853.66 against $963.31 of basis removed ⇒ **+$890.35**. Per lot at $192.66/contract: +$150.68 · +$203.68 · +$535.99. A 3-lot $4.00 limit was Verified Canceled. Remaining basis $770.66.
- **USO $150C Oct-09: 2 → 1.** Sold 1 @ $3.92 → +$391.34 against $299.67 of basis ⇒ **+$91.67**. Remaining basis $299.66.
- Basis removed = the 9/30 basis minus the remaining basis Fidelity shows. That is within 1¢ of a pro-rata split; I used the broker's cells.
- The other 13 Fidelity rows are mark-only changes. All six DTE counts and the Robinhood banner ("NOT CAPTURED 9/30 OR 10/1") were updated.
- **Wording brought into line with Will's standing practice** (`USER.md` 9/30 19:03 ET: a sale before expiry is not a deviation). I removed the "third recorded hand-deviation from the HOLD" line (TLT 77P) and the "WQ-168 ⑥ LAPSE not followed" line (KRE 60P). Both now cite the standing practice. The phrases saying these lines have "no card" were replaced with the TERRY card IDs: `MGMT-QQQ740P-OCT01` (`391bc5d95`/`4ee8783d4`), `MGMT-QQQ735P-OCT05`, `MGMT-USO150C-OCT09` and `MGMT-KRE65P-DEC31` (`5ce609f80`).
- **Gate proximity (rule 7):**
  - 740P card text is quoted on the row: *"SELL-OR-ROLL BEFORE 15:00 ET TODAY — desk lean SELL"*. That is a time rail, not a price trigger.
  - USO 150C: rail *"Hard stop Fri 10/09 15:00 ET"*. The notes' *"any Fidelity bid ≥ $5.98"* is a suggested form, not a registered gate. The $3.92 sale is Will's own decision.
  - TLT 82P +150.49% (2.50× basis) is a mark. The card offers A/B/C choices; nothing fired.
- **Moved to archive:** nothing. The 9/30 CLOSED list, header and discrepancy list are pruned to a pointer, `git show 33bc8c293:FORGE/STATUS.md`. One-line summaries of the 9/30 terminal sales stay in the section italics.

## Discrepancy list — ranked, expiring first (full table in `§ Reconcile discrepancies`)

| Rank | # | Item | Known | Conjectured (labelled) | Owner |
|---|---|---|---|---|---|
| 1 🔴 | WQ-347 | **QQQ $740P Oct-01 ×4 EXPIRES TODAY** | ×4 left, $2.65 / $1,060.00 / +$289.34. QQQ $738.40 `[vendor 12:09 ET, PROME-supplied, not broker-verified]` ⇒ $1.60 ITM. If exercised, the IRA sells 400 QQQ at $740 ($296,000 short) and holds 0 QQQ. Card rail: 15:00 ET | Whether an order is working on the ×4 is NOT SHOWN. Whether the canceled $4.00 3-lot came before or after the $3.72 fill is NOT SHOWN | **Will**; TERRY card on file |
| 2 🔴 | D-60 | Fidelity ITM expiry handling still UNOBSERVED | 10/1 adds no observation (all dispositions were sales before expiry) | — | **Will** (ask Fidelity before 15:00 if the ×4 are held) |
| 3 🟠 | WQ-347 | QQQ $735P Oct-05 ×5 | $3.80 / $1,900.00; $3.40 OTM at 12:09; card *"SELL-OR-ROLL BY MON 10/05 15:00 ET — no action owed today"* | — | Will / TERRY |
| 4 🟠 | — | USO $150C Oct-09 ×1 | $3.30 / $330.00; $2.29 OTM; hard stop Fri 10/09 15:00 | WQ-297 A tie to the USO stock (PROME's read) | Will / TERRY |
| 5 🟠 | WQ-302 | TLT 82P ×1 + HBAN 16P ×2 (Oct-16) | $420.00 / $180.00; A/B/C by Wed 10/14 | — | Will |
| 6 🟡 | **D-69 🆕** | Cash +$53.54 with no row | 9/30-implied $14,094.06 vs $14,147.60 shown | September money-market dividend at month-end (only a plausibility check: ≈0.30%/month ≈ 3.5%/yr), UNVERIFIED. **Kept separate from D-63** (+$2.27 is the 9/28→9/30 window, before month-end; D-69 is 9/30 post-close → 10/1). APD is an unlikely source today | **Will** — one Activity view 9/29→10/01 answers both |
| 7 🟡 | **D-70 🆕** | Other records still show pre-sale quantities | `position_management.tsv` row 18 says 740P ×9 and row 20 says USO 150C ×2. The TERRY 740P card was written on ×9 and the USO notes on ×2. **BRENT `TRADE.md` still lists USO Sep-30 $159C ×2 as OPEN** (`pending_receipts.py` flags "EXPIRY OUTCOME REQUIRED"); it was sold 9/30 for −$919.46 | Expected lag, not an error | **PROME** (TSV) · **TERRY** (cards) · **BRENT** (TRADE.md); ANVIL edits none of them |
| 8 🟡 | D-66 (widened) | Fill times for 9/30 and 10/1 | Not shown | — | Will, low |
| 9+ 🟡 | carried | D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1 | unchanged except D-63 (cross-ref to D-69) and D-45 (an August month-end credit would look like D-69 — labelled conjecture) | — | as listed |
| ⚪ | APD | **(D) badge** | last − Today $chg = $276.42 vs the mirror's $278.23 9/30 close: −$1.81/sh | An ex-dividend adjustment, INFERRED; amount and pay date not shown | PROME / Will |

**CLOSED this pass:**
- **D-67:** the KRE $0.01 marks are answered by today's live marks ($0.71 / $0.71 / $1.80). Fidelity's own 9/30 reference (last − Today $chg) was $0.63 on the 60P and $1.68 on the 65P, so the $0.01 was a post-close artifact (INFERRED). The same test on the other option lines shows Fidelity's 9/30 reference 5–15¢ above the mirror's post-close marks on 5 more lines (740P · 735P · USO 150C · HBAN · APO). TLT 82P was equal. The 9/30 mirror's option values were post-close marks, as labelled.
- **D-68:** TERRY `5ce609f80` and PROME `11b419932` corrected their records. I checked at the artifacts: TERRY's INDEX line 24 and TSV rows 8 · 9 · 15 · 16 now read SOLD TO CLOSE.
- **The two partial sales.**

## Consumer verdict (rule 3)
**There is no structural change, so no consumer sweep is owed.** Sections, headers and row conventions are unchanged. The `Mark 9/30` → `Mark 10/1` rename is prefix-bound. Two Qty cells changed and no row was added or removed. The header money line keeps its `money market):** $X (Y%)` shape. The footer gains a 10/1 pass note.

| Consumer | What I ran | Result |
|---|---|---|
| `positions_from_forge.py --selftest` | selftest | **rc=0, SELFTEST: PASS** (19/19; "live file parses (15 live / 3 withheld)", no parse defects). A live run shows 740P qty=4, USO 150C qty=1, KRE marks 0.71/0.71/1.8 and correct DTE |
| `will_brief.py parse_money()` | called directly | `{'total': '37,727.55', 'cash_pct': '37.50', 'vintage': '2026-10-01', 'marks': '2026-10-01', 'age': 0}` ✓ |
| `desk_attention.py holdings()` | called directly | 18 rows (15 Fidelity + 3 RH); 740P qty 4, USO 150C qty 1 ✓ |
| `position_management.tsv` `source_sha256` | — | Any byte change withholds every mapping sourced to this file, by design. **PROME re-review owed**, and the review should include rows 18 and 20 (D-70) |
| BRENT `pending_receipts.py` | run | Advisory only. It flags BRENT's own stale USO 159C row (D-70). Its "closure candidates" are now the USO **150C** partial-sale rows, which are the wrong contract; the tool itself warns "match contract/account before resolving" |

## Read cap — ⚠️ almost no room left
`FORGE/STATUS.md` is **32,044 B** (`measure.py`: 172 lines, crc32 1761905422), against a cap of 32,550 B, leaving **506 B**. It was 30,011 B before this pass. **The next reconcile must rotate first** (candidates: the footer's accumulated per-pass notes, the 9/15–9/28 provenance notes on the long rows, the carried pre-9/01 RH D-rows).

## Diff stat
```
 FORGE/STATUS.md | 121 ++++++++++++++++++++++++++++----------------------------
 1 file changed, 61 insertions(+), 60 deletions(-)
```
`git status --short -- FORGE/` shows only ` M FORGE/STATUS.md`. `FORGE/PORTFOLIO.md` is untouched and its FROZEN banner is intact. `git diff --check` is clean, and the file has LF endings.

## Skipped / not done
- **No live quote fetched.** The decision on the expiring ×4 is Will's, at Fidelity's own bid. I recorded PROME's QQQ $738.40 (12:09 ET, vendor) with its stamp and no fresher figure.
- I did not re-read the screenshots (I have no image access). Everything comes from the transcription's cells.

**⏸ AWAITING COMMIT AUTHORIZATION.** On PROME's word I commit via `python3 PROME/tools/commit_check.py commit -F <msgfile> -- FORGE/STATUS.md` (subject ≤100 chars, blank line, body) and report the hash. No push.
