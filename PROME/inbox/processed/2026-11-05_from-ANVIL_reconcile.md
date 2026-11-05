# ANVIL → PROME: FORGE reconcile, 11/5 intraday capture. Awaiting commit authorization.

**From:** ANVIL (Claude Code subagent, Opus 5.5), spawned by PROME prome-98. **Stamp:** 2026-11-05 10:13 ET from `date`. **Scope:** only `FORGE/STATUS.md` edited. **Nothing committed.** This packet is also uncommitted.

## Headline

The mirror ties to the cent: positions $12,669.59 + cash $28,218.18 + pending $3,953.67 = **$44,841.44** `[broker export 11/5 ~10:0x ET intraday, quote clock not displayed]`. Re-verified independently: 19/19 rows on value, open G/L and Today $; Σ Today −$957.21; Σ open G/L −$6,422.38; pending = the three 11/5 fills. Both images re-read against the transcription; the figures match.

Your diff is confirmed from `git show HEAD:FORGE/STATUS.md` and the 10/30 record: 5 GONE, 2 QTY, 1 NEW, 16 MARK ONLY.

| Change vs 10/30 | Amount |
|---|---|
| Account total | **−$1,400.38** |
| Positions | −$14,257.93 |
| Cash | +$14,831.46 |
| Pending | −$1,973.91 |
| Realized and other flows | +$4,743.53 |
| Open G/L change | −$6,143.91 |

## Realized booked (all DERIVED)

| Line | Evidence | Realized |
|---|---|---|
| VLO 1 share | $366.67 vs $412.00; removal $1,296.73 → $884.73 = $412.00, ties to the 9/18 original share | −$45.33 |
| AAPL ×3 | $337.22 + $704.72 vs $70.93 | +$971.01 |
| APD ×2 | $637.04 vs $589.57 | +$47.47 |
| GLD ×10 | $3,632.97 vs relief $3,758.86 | −$125.89 |
| QQQ Nov-02 715P | $2,069.29 vs $484.66 | +$1,584.63 |
| AAPL Nov-04 345C | both legs visible | +$335.66 |
| GLD Nov-02 375C ×2 | EXPIRED | −$651.33 |
| QQQ Nov-20 690P ×1 | $2,882.28 vs $1,339.665 | +$1,542.62 |
| QQQ Nov-06 680P | **×2 round trip, INFERRED (see below)** | +$846.30 |
| QQQ Nov-04 680P lot 1 | −$649.66 / +$777.32, pairing INFERRED | +$127.66 |
| QQQ Nov-04 680P lot 2 | −$464.66, EXPIRED | −$464.66 |
| **Total** | | **+$4,168.14** |

Also booked, four 10/23 exits from the 10/23 view, **+$30.47**: USO 165C +$421.16 (average; +$398.66 or +$443.66 by lot), USO 163C +$145.68, AAPL 1 +$322.99, QQQ 705P ×2 −$859.36.

**Unbooked: +$575.39** of the +$4,743.53. It is the second 690P's result, the QQQ Nov-02 680P and Nov-05 685P results, and the $44.43 gap. The booked and unbooked sums tie to the whole-window figure.

## Where I differ from your brief: please read these

1. **Nov-06 680P is NOT an unseen-open line, so I booked it.** Your task (iii) listed it. Fee cents fit 17/17 buys of known quantity (×1 .66, ×2 .33, ×3 .99, ×4 .65, ×10 .63), so −$1,141.33 is ×2, and the two sale rows fit ×1 each. With 0 held at 11/5 and no other row, both legs are visible. Quantity is INFERRED, not displayed.
2. **Row order within a day is not execution order.** Nov-06 lists both sales below its buy, yet 0 are held.
3. **"The two QQQ Nov-04 680P lines": I did not book both buys as expired.** I paired the 11/2 buy with the +$777.32 sale (+$127.66) and expired the 11/3 buy only. The EXPIRED row shows no quantity, so the alternative stays open in D-96: the sale closed an unseen open and both buys expired, which lowers the line by that open's cost. Cents favour the pairing: two unseen ×1 opens leave D-94's close ending .30 (a fee of .70 fits); three leave .96 (no such fee). That is a fit test, not proof. Line net as booked: −$337.00.
4. **Transcription § ④ has an error, PROME's to fix.** It says AAPL 3→1→0. Its own § ② shows Sell 2 shares on 11/5, so the path is **3→2→0** and the 11/2 row is 1 share. Booked figures are unaffected (D-97). I did not touch the file.
5. **DOCKET L921's "rows 11 and 14" are file line numbers, not table rows.** Verified there: line 11 = USO Oct-30 165C @ $7.15, $714.32; line 14 = USO Oct-23 163C @ $4.36, $435.34.

## Discrepancy list, urgency-ranked

| # | State | Finding | Owner |
|---|---|---|---|
| **D-94** 🆕 | 🟠 open | Second 690P ×1: basis $1,339.665 unbooked. Every row 11/2→11/5 was read and shows no other 690P row, so the close is below the view, on 10/30 after the capture (INFERRED by elimination). The $17.95 order is **not shown filled**. Cash test: $19,314.30 − $532.66 = $18,781.64 vs displayed $19,397.62 ⇒ +$615.98 net of unseen rows. HYPOTHESIS: a $17.95 fill nets ≈$1,794.30, leaving ≈$1,178.32 for two opens. It fits, it does not prove | **Will** Activity; **PROME**; **TERRY** |
| **D-96** 🆕 | 🟡 | Opens unseen: QQQ Nov-02 680P (+$52.34 sale) and Nov-05 685P (+$1,202.31 sale). Nov-04 pairing as item 3 above | **Will**; **PROME** |
| **D-95** 🆕 | 🟡 | $44.43 gap, unbooked. CONJECTURE only: month-end money-market dividend, same form as D-45 +$43.81 (8/31) and D-69 +$53.54 (9/30). No such row has ever been displayed | **Will**; **PROME** |
| **D-97** 🆕 | 🟡 | Share counts per row implied only. GLD 5 + 5 ≈ $362.90 / $363.69 DERIVED. AAPL 3→2→0 correction | **PROME**; **Will** |
| **D-89** | 🟡 narrowed | 11/5 panel: three fills, no open order. Earlier orders not shown | **Will**; **PROME** |
| **D-90 / WQ-548 / L921** | 🟡 narrowed | Answered by the 10/23 view: USO 163C, one 165C, AAPL −1, the spread opening, the 705P buy. **Stays unseen:** GLD +3 · TBT +5 · KRE 68P ×10, GLD 375C ×2, VLY, FLG buys · USO Oct-28 165C ×1, USO Oct-30 165C ×1, CMG 28P outcomes · any 10/28–10/29 rows · the 10/23 Buy 4 FLG @ $0.52 order (the held ×1 at $0.71 cannot be that limit). Residual +$770.04; cash unexplained −$1,303.11 (was −$1,604.84). The $962.00 step no longer shows | **Will**; **PROME** |
| **D-60** | 🟡 narrowed | Three expiry paths now seen; GLD 375C and QQQ Nov-04 680P lapsed as EXPIRED rows | **Will** |
| **D-74, D-77, D-70, D-78, D-76, D-83, D-79, D-87, D-91** | 🟡 refreshed | Cluster value now $554.00, was $1,910.00. USO 172C has no card. Text updated to 11/5 | as recorded |
| **D-88, D-85, D-84, D-86, D-80, D-81 + 18 carried** | 🟡 unchanged | Nothing in this capture answers them | as recorded |
| **D-93** | ✅ closed | 690P flat, card CLOSED | — |
| **D-82** | ✅ closed | L709 RESOLVED 10/31; OZK ×4 and WAL 65P ×4 still held 11/5, no order; lines ride | — |

## Gates: proximity only, none adjudicated

- **`GATE-TERRY-VLO-HELD-01`:** the consequence is "a SELL of the ONE held share (filled $412.00 9/18, WQ-213)", and that share is the one sold. You and TERRY moved the row while I ran: PROME/GATES.tsv read RESOLVED 2026-11-05 EXECUTED at my 10:07 ET read (TERRY `42b47b6b8`). The mirror records that and sets nothing. The 2 shares left carry no TERRY rule (D-78).
- **`MGMT-GLD-SHARES-OCT24`:** $376.53 is an intraday last, $15.82 above "GLD close < $360.71" and $14.55 below "GLD close > $391.08". TERRY recorded the first as crossed at the 10/30 close, $355.78.
- **MIDAS's dated line, not in the mirror (no bytes), not read by me:** the 3-month line "a second LIQUIDATION day by 11/05 and tonnes ≤ −20 t since 9/30" dates to today. MIDAS grades it.
- **USO +20.36%:** a mark; WQ-200 was declined, no rule is live. **USO 172C −93.25%:** a mark; no card.

## Consumer verdict: no sweep owed

No structural change: no header, section or row-convention change. The `Mark` header changed its date only, which the parser binds by prefix. Rows were removed and added inside existing tables.

| Consumer | Result |
|---|---|
| `positions_from_forge.py --selftest` | rc 0, read bare; 19 live / 3 RH withheld / 0 warnings; live values sum to $12,669.59 |
| `desk_attention.holdings()` | 22 rows, 0 errors; `forge_vintage` = 2026-11-05 intraday, marks known |
| `will_brief.py --book-line` | rc 0; reads $44,841.44 · 62.93% |
| `pending_receipts.py` | runs; still flags the USO Oct-30 165C remainder as outcome-owed, which is correct (D-90); its lots $270.66 / $315.66 gave the booked range above |
| `position_management.tsv` | 0 mappings sourced to this file, so the footer's withhold clause does not fire. For D-70: the AAPL row now describes a flat line, the VLO row still reads 3 shares, and I saw no USO 172C row |

## Size

**32,523 B by `PROME/tools/measure.py`, 27 B under the 32,550 B cap** (was 33,186 B). Done by replacing superseded history with pointers to `git show 3064691ae:FORGE/STATUS.md`, plus dropping seven per-row KRE stamps that the section line already carries. No new rotation file, as instructed. **The hot/cold split is still owed before the next reconcile; this run does not relieve it.**

## Diff stat

```
 FORGE/STATUS.md | 116 ++++++++++++++++++++++++++++----------------------------
 1 file changed, 57 insertions(+), 59 deletions(-)
```

`git status --short -- FORGE/`: only `FORGE/STATUS.md`. `FORGE/PORTFOLIO.md` untouched, FROZEN banner intact.

## Housekeeping

- SendMessage was not available, so this packet plus my final text is the delivery.
- The ANVIL charter's Known-state block was not updated; you said to touch only `FORGE/STATUS.md`.

**Awaiting commit authorization.**
