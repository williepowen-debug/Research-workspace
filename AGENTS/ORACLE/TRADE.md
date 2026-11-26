# ORACLE — TRADE (how prediction-market odds inform positions)

**Refreshed:** 2026-11-26 (ET, Thanksgiving), latest column = pulls 2026-11-26T16:40Z, Polymarket and Kalshi (laptop, Kalshi UNSIGNED public read; US exchanges shut, so holiday context) · **prior refreshes:** 11/04, 8/27, 8/12, 7/22
**Rule from Will, 2026-08-27:** *"lets not simply delete though — lets track how the numbers have changed over time."* Every routed figure carries its trajectory. Earlier vintages and their commentary stay in `git log -p -- AGENTS/ORACLE/TRADE.md`.

> **Provenance:** every table cell comes from `workbook/TRADE_MARKS.tsv` (624 rows, 17 marks, written 2026-11-26), which `tools/trade_marks.py --write` extracts from ORACLE's append-only logs. No vintage is hand-typed. Dated columns show the first row `TRADE_MARKS.tsv` holds for that ET date; the tool keeps one row per mark per UTC date, so a cell can be a later pull than the official first-pull read (11/04 here is the 15:15Z routine read; 10/30 is the 10/31T02:15Z pull, ET 10/30). `V5_NOV110_READS.tsv` and `VX.tsv` hold the graded reads. **latest** shows the last pull. The `range` column uses all pulls since 10/16 and covers only the current contract where a series rolled.
>
> ⚠️ **Contract identity:** a ‖ marks a slug change. Never difference across it. WTI touch markets are month-stamped; bank-failure-by-Dec-31 has been delisted and relisted.
>
> ⚠️ **Still a dated snapshot. `STATUS.md` is the live home.** Re-pull before citing. This file routes evidence; position truth is off-repo, and no position is opened or sized from this file.

---

## Live reads → routed implications

### 1. Fed path → LIQUID / HENRY / BOND

| Mark | 10/16 | 10/30 | 11/4 | 11/12 | 11/18 | 11/25 | **latest** | range since 10/16 |
|---|---|---|---|---|---|---|---|---|
| Fed **no cuts** 2026 (PM) | 96.9 | 96.9 | 97.5 | 98.6 | 98.4 | 98.5 | **98.2** (11/26) | 96.7–98.6 |
| Fed **hike at December** meeting, +25 leg (PM) | 77.5 | 70.5 | 80.5 | 90.5 | 92.5 | 93.5 | **93.5** (11/26) | 63.5–94.5 |
| Fed **≥1 more hike by December** (Kalshi; corroborates only) | 82.0 | 72.0 | 79.0 | 95.0 | 97.0 | 97.0 | **96.0** (11/26) | 65.0–97.0 |

**Implication: a December quarter-point hike is all but priced, and the next question is January.** The PM +25 leg climbed 70.5 (10/30) → 93.5; the half-point leg fell to 2.2 and hold sits at 3.5. Futures imply +24.7bp (KB-ORC-143; ⚠️ Yahoo last trades, not settlements; ⚠️ a size of move, not odds). **January 2027 is now pinned:** PM hike 25 53.5, Kalshi decision market 57 (OI 128.1K), futures about +16bp (KB-ORC-152). The crowd puts a second straight hike near even odds. Anchor predictions to surprise against this pricing; a fleet forecast of a December hike at 70 (HEN-63) is below the market on the same letter.

### 2. Iran / Hormuz / oil → BRENT / HAWK / FALCON

| Mark | 10/16 | 10/30 | 11/4 | 11/12 | 11/18 | 11/25 | **latest** | range since 10/16 |
|---|---|---|---|---|---|---|---|---|
| **WTI $110** touch (PM; month-stamped, rolls ‖) | 20.5 | ‖ 64.0 | 25.5 | 5.5 | 2.7 | 1.1 | **0.7** (11/26) | 0.7–64.0 (this contract) |
| **Hormuz normal** by Dec 31 (PM; PortWatch print) | 11.5 | 10.5 | 10.5 | 6.5 | 4.5 | 2.7 | **2.8** (11/26) | 2.7–11.5 |
| **US invade Iran** before 2027 (PM) | 15.5 | 17.5 | 12.5 | 7.5 | 7.5 | 5.5 | **5.5** (11/26) | 5.5–18.5 |

**Implication: the oil war premium is gone while disruption stays priced.** The November $110 leg fell from 64.0 (10/30) to 0.7; Hormuz "normal by 12/31" fell from 10.5 to 2.8, so the crowd prices the disruption as lasting and the supply loss as not happening. Spread +96.6pp (11/26). The 2-week pause by 11/30 is 72.0 and by 12/31 85.5: the crowd expects the US to hold off striking Iran even as Iranian and Houthi strikes hit Gulf states and shipping (KB-ORC-145).
- ⚠️ **Do not read the strike and oil rows as one view.** They are separate contracts with different rules, participants and liquidity. "Limited strikes, not a supply shock" is a plausible reading, not a finding.
- ⚠️ **The Hormuz row grades on the IMF PortWatch print**, not on throughput (KB-ORC-079).
- ⚠️ **The November $110 leg ends 11/30 and no December market is listed (11/26).** The series stops unless one lists (KB-ORC-154).
- **Definition:** PM "ceasefire"/"pause" means no qualifying US air or missile strike landing on Iranian territory (KB-ORC-111, KB-ORC-145).

### 3. Recession → RED / HENRY / LABOR

| Mark | 10/16 | 10/30 | 11/4 | 11/12 | 11/18 | 11/25 | **latest** | range since 10/16 |
|---|---|---|---|---|---|---|---|---|
| Recession 2026 (PM; GDP or NBER) | 6.5 | 6.5 | 5.5 | 2.1 | 2.2 | 2.6 | **2.8** (11/26) | 2.1–7.5 |
| Recession 2025-26 (Kalshi; 2Q negative GDP only, KB-ORC-099) | 4.0 | 3.0 | 4.0 | 3.0 | 1.0 | 3.0 | **3.0** (11/26) | 1.0–4.0 |

**Implication: the crowd is calm.** Both venues sit near their lows (PM 2.1 to 2.8 since 11/12). The two rows differ in definition, so the gap is structural. Kalshi depth is open interest (902.4K), and its last trade swings point to point.

### 4. Bank failure → REGINALD

| Mark | 10/16 | 10/30 | 11/4 | 11/12 | 11/18 | 11/25 | **latest** | range since 10/16 |
|---|---|---|---|---|---|---|---|---|
| **ANY** US bank failure by Dec 31 (PM; ⚠️ thin) | 84.5 | 71.0 | 70.5 | 70.5 | 59.0 | 53.5 | **48.5** (11/26) | 48.5–84.5 |
| **Named** bank EOY, top leg (PM; ⚠️ thin) | 3.4 | 3.5 | 3.4 | 3.4 | 2.8 | 2.4 | **3.0** (11/26) | 2.4–20.4 |

**Implication: still too thin to read, and this crowd has under-priced failures all year.** ANY sits at 48.5 on $2.8K of liquidity; the fall since 11/13 matches time running out with no failure, not information. F-1 Brier over five resolved instances is 0.217 against 0.250 for a coin flip, and every miss under-priced a failure (`workbook/F1_BRIER.tsv`, KB-ORC-146). Not marked, not routed. ANY and Named ask different questions.

### 5. Tail sentiment → VIOLET / RED

| Mark | 10/16 | 10/30 | 11/4 | 11/12 | 11/18 | 11/25 | **latest** | range since 10/16 |
|---|---|---|---|---|---|---|---|---|
| **Nothing Ever Happens** 2026 (PM) | 83.0 | 80.0 | 85.5 | 92.5 | 92.5 | 93.5 | **92.5** (11/26) | 79.5–93.5 |
| Best asset 2026, top leg (PM) | 69.0 | 80.5 | 85.0 | 88.5 | 92.5 | 93.0 | **94.5** (11/26) | 69.0–95.5 |

**Implication: equities keep the best-asset lead (94.5), and gold has not taken it.** ⚠️ **NEH is not a complacency gauge.** It resolves NO only on one of 13 extreme events; the full rules PDF was read 11/26 and confirms a US strike on Iran does not count, only a land offensive (KB-ORC-150).

### 6. Blind-spot axis → BOND

| Mark | 10/16 | 10/30 | 11/4 | 11/12 | 11/18 | 11/25 | **latest** | range since 10/16 |
|---|---|---|---|---|---|---|---|---|
| US credit-rating downgrade 2026 (Kalshi) | 7.9 | 8.0 | 1.3 | 1.2 | 5.1 | 2.3 | **2.3** (11/26) | 1.2–8.0 |

**Implication: downgrade odds stay low and noisy** (1.2 to 7.0 since 11/12 on a 2¢ book). ORACLE's instruments price the policy path only and cannot see term premium or credibility. ⛔ Never read this file as "rates calm per ORACLE." BOND owns the regime label.

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
