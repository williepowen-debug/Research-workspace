# ANVIL → PROME: FORGE reconcile report, 9/30 post-close (spawner prome-94)
**Written 2026-09-30 18:4x ET (`date` 18:40:17 EDT).** Scope: `FORGE/STATUS.md` only. **Awaiting commit authorization. Nothing is committed.** `SendMessage` isn't available in this harness, so this file plus my final text are the delivery.

## Headline
- **Arithmetic checks to the cent.** I recomputed every row myself:
  - value = last × qty (×100 for options) holds on 15 of 15 rows, and G/L = value − basis holds on 15 of 15.
  - Positions $22,290.87 + cash $18,102.04 + pending −$4,007.98 = **$36,384.93**, which matches the account total.
  - Σ Today = +$753.44 and Σ G/L = +$2,837.63, both matching the broker's figures.
  - The 9 filled Activity rows net to −$4,007.98, which equals Pending.
  - New-line bases = fill × qty × 100 + fees on 4 of 4.
  - 6 broker % cells differ from my recomputation by 0.01. That's broker rounding, so I kept the values as shown.
- **Account total:** $36,384.93, down from $36,822.87 `[9/29 13:4x intraday]`, a change of −$437.94. The base is intraday, so this is not a close-to-close move.
- **Cash and pending:** cash is unchanged at $18,102.04 (49.75%). Pending is −$4,007.98, so cash after settlement is $14,094.06 (derived).
- **The 4 Sep-30 lines are GONE. All were SOLD TO CLOSE, none expired or lapsed.** Realized P&L below is against the mirror's broker basis:

| Line | Ledger row | Proceeds | Realized |
|---|---|---|---|
| QQQ 730P ×9 | row 10 | +$8.43 | −$2,229.54 (campaign total −$2,280.86) |
| USO 159C ×2 | row 5 | +$1.87 | −$919.46 |
| TLT 77P ×15 | rows 9 + 12 | +$18.80 | −$154.64 (third hand-deviation from the HOLD; recorded, not adjudicated) |
| KRE 60P Sep-30 ×2 | row 1 | +$1.87 | −$451.48 (basis $453.35 from the 9/29 transcription; LAPSE was ruled, the line was sold instead; recorded) |

  Σ realized = **−$3,755.12**.
- **4 NEW lines, none with a card:**
  - QQQ 740P Oct-01 ×9: bought @ $1.92, $1,733.97.
  - QQQ 735P Oct-05 ×5: bought @ $2.73, $1,368.32. This is ADDED size, a single-leg buy.
  - USO 150C Oct-09 ×2: bought @ $2.99, $599.33.
  - KRE 65P Dec-31 ×2: bought @ $1.68, $337.33. I placed it in the KRE table.
- **11 Fidelity rows are MARK ONLY.** Quantities and bases are identical to the 9/29 mirror. Stock marks are stamped `[9/30c]`; option marks `[9/30 post-close]`.
- **Header:** `**Updated:** 2026-09-30`, `marks = 2026-09-30`, and the account scope banner now reads IRA *****1326, with Robinhood NOT captured and its rows unverified today.

## Discrepancy list (urgency-ranked, expiring first)

| # | Item | Owner |
|---|---|---|
| WQ-347 | 🔴 **QQQ 740P ×9 expires THU 10/01.** It was $0.23 in the money at the 9/30 close (QQQ $739.77, per PROME/TERRY; not in the capture). Exercise would mean selling 900 QQQ at $740 ($666,000), and the IRA holds none. No card. | Will; TERRY writes a card Thu |
| D-60 | 🔴 **What Fidelity does when an in-the-money option expires in the IRA is still UNOBSERVED.** 9/30 adds no observation, because all four Sep-30 lines were sold before the close. The out-of-the-money case has been OBSERVED 4 times. | Will (a Fidelity question before Thu 15:00 if the 740P is held) |
| WQ-347 | 🟠 QQQ 735P ×5 expires Mon 10/05. It was $4.77 out of the money at the close. No card. | Will / TERRY |
| — | 🟠 USO 150C ×2 expires Fri 10/09. It was $4.34 out of the money. No card and no rule. I found no WQ row naming it. | Will |
| WQ-302 | 🟠 TLT 82P ×1 and HBAN 16P ×2 expire Oct-16; Will's choice is due by Wed 10/14. TLT is at +174.34% (2.74× basis), but that is a mark: the card offers an A/B/C choice, not a price trigger, and nothing has fired. | Will |
| **D-68 🆕** | 🟠 **Other desks' records conflict with the broker ledger:**<br>• TERRY `setups/INDEX.md` TRY-FIRE-004 says *"EXPIRED WORTHLESS … −$173.45"*. The ledger shows it SOLD, −$154.64.<br>• The WQ-316 "EXPIRY OUTCOME" row (citing TERRY `ee04fbb26`) says USO 159C *"expired worthless (−$921.33)"* and "BOTH LEGS EXPIRED OTM". The ledger shows it SOLD, −$919.46.<br>• `FORGE/position_management.tsv` rows 8 · 9 · 15 · 16 still describe the four Sep-30 lines as open. `DASHBOARD.md` asks for that TSV to be reconciled in the same pass.<br>I edited none of these. | TERRY (INDEX/card) · PROME (WQ-316, TSV re-review) |
| **D-67 🆕** | 🟡 All three KRE Dec lines are marked $0.01 post-close: −98% on the day while KRE fell only 0.56%. At the 9/29 mark plus the 65P fill, these lines would be worth about $566 versus the $7 shown (DERIVED, not a valuation). Σ Today includes −$595.33 from these marks. | PROME (the next regular-session capture) |
| **D-66 🆕** | 🟡 No fill times are shown for any of the 9/30 fills or cancels. | Will, low |
| D-62 · D-63 · D-64 · D-65 · D-61 · D-59 · D-45 · D-55 · D-28 · D-54 · D-18 · D-20 · D-37 · D-17 · D-1 | 🟡 Carried as before. **D-63 (+$2.27) is untouched:** the Sep-30 Activity shows no dividend or interest row, and 9/29 was not captured. | as listed in the file |

**Closed this pass:**
- D-31: the TLT 77P line was sold.
- WQ-316: answered by Will's roll.
- The four Sep-30 dispositions, all booked from ledger rows.

## Consumer-sweep verdict (rule 3)
**No structural change:**
- Sections, table headers and row conventions are the same.
- The Off-thesis/Longs header `Mark 9/29` became `Mark 9/30`; the parser matches it by prefix, as on 9/29.
- Terminal records are now italic lines, which no parser reads as rows.
- The header gained a `Pending activity` figure *after* the money-market cell.
- The footer PARSED-BY contract is intact, and I added a 9/30 pass note.

Receipts:
- `positions_from_forge.py --selftest` rc=0. A full run gives 15 LIVE and 3 WITHHELD (the Robinhood rows, which have no Mark column), no parse defects and no phantom rows. The Sep-30 rows are gone and the 4 new rows parse with the correct expiries (1/5/9/92 DTE).
- `will_brief.parse_money()` returns `{'total': '36,384.93', 'cash_pct': '49.75', 'vintage': '2026-09-30', 'marks': '2026-09-30'}`.
- `desk_attention.holdings()` returns 18 rows with 0 defects. One thing to note there: its Robinhood observation string is hardcoded *"Not captured September 3"*. That is the tool's own stale label, not something this file controls; it's PROME's tool.
- BRENT `pending_receipts.py` reports ✅ with no elapsed expiries.
- `FORGE/position_management.tsv` `source_sha256`: every mapping sourced to this file is now withheld until PROME re-reviews it (by design). **A consumer sweep is owed only for that TSV re-review (D-68)**, not for any parser.
- `FORGE/PORTFOLIO.md` still carries its FROZEN banner.

## Diff and size
- `git diff --stat -- FORGE/`: `FORGE/STATUS.md | 139 ++++---- 1 file changed, 74 insertions(+), 65 deletions(-)`. `git status -- FORGE/` shows only ` M FORGE/STATUS.md`.
- `measure.py`: **30,011 B**, 171 lines, crc32 2392788505. That is under the 32,550 B cap, so no rotation was needed. The prior list is pointed to via `git show b983d745a:FORGE/STATUS.md`.
- I did not touch `position_management.tsv`. The new lines need no mapping; they show as unrecorded, which is the honest state. The TSV's re-review of the four closed rows is flagged under D-68.

**⛔ Awaiting commit authorization.** On Will's word relayed by PROME, I'll commit via `commit_check.py commit -F <msgfile> -- FORGE/STATUS.md`, with a subject of 100 characters or fewer, then a blank line, then the body.
