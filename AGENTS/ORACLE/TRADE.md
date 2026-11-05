# ORACLE — TRADE (how prediction-market odds inform positions)

**Refreshed:** 2026-11-04 (ET), latest column = pulls 2026-11-05T01:40Z and Kalshi 01:40Z (both platforms; laptop, Kalshi UNSIGNED public read) · **prior refreshes:** 8/27, 8/12, 7/22
**Rule from Will, 2026-08-27:** *"lets not simply delete though — lets track how the numbers have changed over time."* Every routed figure carries its trajectory. Earlier vintages and their commentary stay in `git log -p -- AGENTS/ORACLE/TRADE.md`.

> **Provenance:** every table cell comes from `workbook/TRADE_MARKS.tsv` (416 rows, 17 marks), which `tools/trade_marks.py --write` extracts from ORACLE's append-only logs. No vintage is hand-typed. Dated columns show the first row `TRADE_MARKS.tsv` holds for that ET date, and the tool keeps one row per mark per UTC date, so a cell can be a later pull than the official first-pull read. On 10/28 the WTI row shows November's entry (52.5), not October's last read (3.6). `V5_NOV110_READS.tsv` and `VX.tsv` hold the graded reads. **latest** shows the last pull. The `range` column uses all pulls since 9/17 and covers only the current contract where a series rolled.
>
> ⚠️ **Contract identity:** a ‖ marks a slug change. Never difference across it. WTI touch markets are month-stamped; bank-failure-by-Dec-31 has been delisted and relisted.
>
> ⚠️ **Still a dated snapshot. `STATUS.md` is the live home.** Re-pull before citing. This file routes evidence; position truth is off-repo, and no position is opened or sized from this file.

---

## Live reads → routed implications

### 1. Fed path → LIQUID / HENRY / BOND

| Mark | 9/17 | 9/28 | 10/16 | 10/28 | 10/30 | 11/02 | 11/04 | **latest** | range since 9/17 |
|---|---|---|---|---|---|---|---|---|---|
| Fed **no cuts** 2026 (PM) | 95.3 | 97.0 | 96.9 | 96.7 | 96.9 | 97.0 | 97.5 | **97.8** | 95.3–97.8 |
| Fed **hike at December** meeting (PM) | 65.5 | 79.0 | 77.5 | 79.5 | 70.5 | 70.5 | 80.5 | **77.5** | 65.5–80.5 |
| Fed **≥1 more hike by December** (Kalshi; corroborates only) | — | — | 82.0 | 83.0 | 72.0 | 72.0 | 79.0 | **81.0** | 72.0–87.0 |

**Implication: the crowd prices one more hike in December.** The PM read fell to 69.5 on 10/29 and returned to 80.5 on 11/04. The lowest read since 10/28 is 69.5, and VX-ORC-12's de-alert needs two reads below 50.0. No cuts in 2026 is near certain; that row follows from a hiking Fed, so it adds little new information. Anchor predictions to surprise against this pricing.

### 2. Iran / Hormuz / oil → BRENT / HAWK / FALCON

| Mark | 9/17 | 9/28 | 10/16 | 10/28 | 10/30 | 11/02 | 11/04 | **latest** | range since 9/17 |
|---|---|---|---|---|---|---|---|---|---|
| **WTI $110** touch (PM; month-stamped, rolls ‖) | — | 25.5 | 20.5 | ‖ 52.5 | 64.0 | 36.5 | 25.5 | **13.0** | 13.0–64.0 (this contract) |
| **Hormuz normal** by Dec 31 (PM; PortWatch print) | 17.5 | 23.5 | 11.5 | 11.5 | 10.5 | 11.5 | 10.5 | **10.5** | 10.5–23.5 |
| **US invade Iran** before 2027 (PM) | 17.5 | 15.5 | 15.5 | 18.5 | 17.5 | 17.5 | 12.5 | **10.5** | 10.5–18.5 |

**Implication: $110 odds fell hard while Hormuz odds barely moved.** The disruption-supply spread (November segment) read +36.0pp on 10/28, +64.0pp on 11/04 and +76.5pp in the evening pull; the supply leg moved, not the disruption leg.
- **Alert:** VX-ORC-04 fired 10/30 and cleared 11/04. ⚠️ The 10/29 read came 7h42m after Polymarket's 18:33Z halt; excluded, no Alert fired.
- **Strike odds:** PM's effective-ceasefire series implies another qualifying US strike at 43.5 by 11/15, 58.5 by 11/30 and 70.0 by 12/31 (KB-ORC-112). The series is one day old, and each leg has traded $36K–$77K.
- ⚠️ **Do not read the strike and oil rows as one view.** They are separate contracts with different rules, participants and liquidity, so they do not show what traders expect oil to do if a strike happens. "Limited strikes, not a supply shock" is one plausible reading, not a finding. The cause of the oil drop is not established (SIG-W-20261104-078).
- ⚠️ **The Hormuz row grades on the IMF PortWatch print**, not on throughput (KB-ORC-079). It is not a disruption probability.
- **Definition:** PM "ceasefire" means no US air or missile strike landing on Iranian territory (KB-ORC-111). It does not test a formal truce.
- **Calendar:** a fresh month's touch market is structurally higher than an expiring one. Read month rolls as calendar, not risk.

### 3. Recession → RED / HENRY / LABOR

| Mark | 9/17 | 9/28 | 10/16 | 10/28 | 10/30 | 11/02 | 11/04 | **latest** | range since 9/17 |
|---|---|---|---|---|---|---|---|---|---|
| Recession 2026 (PM; GDP or NBER) | 8.5 | 8.5 | 6.5 | 5.5 | 6.5 | 5.5 | 5.5 | **4.5** | 4.5–11.5 |
| Recession 2025-26 (Kalshi; 2Q negative GDP only, different definition, KB-ORC-099) | — | 6.0 | 4.0 | 3.0 | 3.0 | 3.0 | 4.0 | **2.0** | 2.0–6.0 |

**Implication: the crowd is calm, and both venues sit at their lows since 9/17.** The two rows differ in definition, so the gap is structural. Kalshi has no resting book; depth is open interest, and it swings point to point.

### 4. Bank failure → REGINALD

| Mark | 9/17 | 9/28 | 10/16 | 10/28 | 10/30 | 11/02 | 11/04 | **latest** | range since 9/17 |
|---|---|---|---|---|---|---|---|---|---|
| **ANY** US bank failure by Dec 31 (PM; ⚠️ thin) | 55.5 | — | ‖ 84.5 | 72.5 | 71.0 | 70.0 | 70.5 | **70.5** | 42.0–84.5 (this contract) |
| **Named** bank EOY, top leg (PM; ⚠️ thin) | 3.4 | 4.0 | 3.4 | 3.4 | 3.5 | 3.4 | 3.4 | **3.4** | 3.4–20.4 |

**Implication: no named bank is priced, and the any-bank book is too thin to read.** ANY sits at 70.5 on $2.0K of liquidity. Not marked, not routed. ANY and Named ask different questions, so 70.5 and 3.4 do not contradict each other. VX-ORC-01 grades the ANY binary under the thin rule.

### 5. Tail sentiment → VIOLET / RED

| Mark | 9/17 | 9/28 | 10/16 | 10/28 | 10/30 | 11/02 | 11/04 | **latest** | range since 9/17 |
|---|---|---|---|---|---|---|---|---|---|
| **Nothing Ever Happens** 2026 (PM) | 81.5 | 83.5 | 83.0 | 81.5 | 80.0 | 81.5 | 85.5 | **88.5** | 79.5–88.5 |
| Best asset 2026, top leg (PM) | 54.5 | 57.5 | 69.0 | 74.5 | 80.5 | 82.0 | 85.0 | **84.5** | 53.5–85.0 |

**Implication: equities have regained the best-asset lead, and gold has not taken it.** The S&P leg reads 84.5, BTC 10.5 and gold 2.7. The registered gold tell has not fired.
⚠️ **NEH is not a complacency gauge.** It resolves NO only on one of 13 extreme events, such as China invading Taiwan or a US invasion of Iran (KB-ORC-115). A US strike does not trigger it. This corrects the complacency language in earlier refreshes of this file. The linked PDF of full rules is unread.

### 6. Blind-spot axis → BOND

| Mark | 9/17 | 9/28 | 10/16 | 10/28 | 10/30 | 11/02 | 11/04 | **latest** | range since 9/17 |
|---|---|---|---|---|---|---|---|---|---|
| US credit-rating downgrade 2026 (Kalshi) | — | 12.0 | 7.9 | 5.9 | 8.0 | 6.5 | 1.3 | **1.2** | 1.2–12.0 |

**Implication: downgrade odds faded.** ⚠️ The latest last trade (1.2) sits on a wide 4¢ book, with a mid of 3.4. ORACLE's instruments price the policy path only and cannot see term premium or credibility. ⛔ Never read this file as "rates calm per ORACLE." BOND owns the regime label.

---

## Standing rule for downstream agents

When ORACLE hands you a market probability:
1. **Is your trigger outcome already priced?** If yes, re-key your prediction to *"more X than priced"* (anchor-to-surprise).
2. **Is the market thin (⚠️)?** Treat any move as unconfirmed until a ≥3-day re-check **plus** an independent source agrees. Thin books discharge by **DEPTH, never by elapsed time** (N5 clause iv).
3. **Divergence ≠ direction.** A gap vs thesis is a question for RED, not a position change.
4. **★ Check the row's trajectory before you cite its level.** A number flat for five weeks and a number that moved 15pp last week are not the same evidence, even at the same value.
5. **★ Never difference across a ‖ break.** Rolls and relists are identity changes, not moves.
6. **★ Two contracts are two questions.** Separate markets do not give a conditional probability. Do not infer one from them.

*No position is opened or sized from this file. Owners: FORGE / the named domain agent.*
