# ORACLE STATUS

**Live dashboard: prediction-market probabilities, divergences, alerts.**
**FULL REWRITE 2026-11-05 (Thu 18:11–18:2x ET, from `date`) — laptop `WilliePOwen`, Kalshi UNSIGNED (`status` rc=3, public market data).** Pulls: Polymarket `pull --log` **2026-11-05T23:11Z** (52 rows) · Kalshi 23:11Z 7/7, 23:15Z 9/9 after the Brent re-pin · spread row 23:11Z · `history --write` (8,791 rows / 52 markets) · `movers` 23:1xZ · `trade_marks --write`. The 11/05 gate read is the routine's 10:15 ET pull (15:15Z, desktop). **Tonight's 23:11Z is a later pull on the same ET date, so it is CONTEXT, never a gate read** (letter O3).

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price; re-pull. Every figure carries platform/date/depth. Thin books (<$5K liq) are flagged ⚠️ and never marked on one print. Kalshi depth proxy = open interest. "PM" = Polymarket.

---

## 🔴 Alerts (read first)

**1. 🟠 DECEMBER HIKE ODDS FELL 17 POINTS ACROSS TODAY'S SELLOFF; BOTH VENUES AGREE; NO GATE CLEARED.**
PM HIKE-at-Dec 80.5 (11/04 read, liq $349.3K) → 73.5 (11/05 read, liq $222.7K) → **63.5** (context 23:11Z, liq $417.7K, vol $4.1M). CLOB 75.5 at 15:00Z → 65.5 at 16:00Z: the step came between 10:00 and 11:00 ET. Kalshi ≥1 more by Dec 81.0 (11/05T01:40Z) → 73.0 → **65.0** (OI 88.8K). PM no change 18.5 → 33.5. Same hours: S&P −4.36%, QQQ −6.49%, VIX 28.17 (vendor reads; SIG-W-20261105-055, -057); `^TNX` 4.84, −1.16% (`fetch.py`). ⚠️ **Cause not established; timing is coincidence evidence only.** Barkin and Hammack headlines ran hawkish that morning, bodies unread (SIG-W-20261105-022). VX-ORC-12 Alert HELD: the de-alert needs two consecutive reads <50.0. → LIQUID, HENRY, BOND, PROME · KB-ORC-118

**2. 🔴 VX-ORC-07 (48h moves) STILL CRITICAL, on WTI.** WTI $110 Nov 36.0 (11/04 07Z) → 13.0 (11/05 03Z) = −23.0 in 20h, CLOB pair; it stays in the 48h window until 2026-11-06T07Z. Fed HIKE −17.0 in 32h is Alert size. Log pass covers non-thin rows only; CLOB checked for those two only. → PROME (triage)

**3. 🟠 THE CROWD STILL PRICES MORE STRIKES THAN OIL RISK.** PM effective ceasefire 11/15 **57.5** · 11/30 **38.5** · 12/31 **28.0** (liq $51.3K · $62.3K · $59.5K): implied another US strike 42.5 · 61.5 · 72.0. WTI $110 Nov **17.0** (11/05 read 16.0; vol $47.1K, liq $30.3K). US invade Iran 12.5 (vol $78.0M) · regime fall 2.9. Blockade-end 3/31/27 69.5 · next senior meeting 12/31 43.0. ⚠️ Separate contracts with different rules; they do not show what traders expect oil to do if a strike happens. PM "ceasefire" means no US strike landing on Iran, not a formal truce (KB-ORC-111). FALCON's FAL-07 RESOLVED CONFIRMED 11/04 is consistent with that record. ⚠️ FALCON: no on-record CENTCOM; 11/2 is the first CONFIRMED date, not necessarily the first strike. → HAWK, BRENT, FALCON · KB-ORC-112, KB-ORC-119

**4. 🟡 NOVEMBER $110 OIL: NO ACTIVE ALERT.** Reads 10/28 52.5 · 52.5 · 64.0 (Alert) · 36.5 · 30.5 · 25.5 (cleared) · **11/05 16.0**. Spread +73.5 (read), +72.5 (context). ⚠️ The 10/29 read came 7h42m after Polymarket's 18:33Z halt; excluded, no Alert fired. WTI ~$90.98 / Brent ~$99.15 evening bars (`fetch.py`, session spans two days, Brent contract unknown). Kalshi Brent > $97.99 at 11/30 43.0 (OI 6.3K). → BRENT, FALCON, HAWK · VX-ORC-04

**5. 🟡 FRIDAY JOBS.** Kalshi October U3 `>4.1` 68.0 → 78.0 (10:15 ET) → **64.0** (OI 48.1K, 2¢) · `>4.2` 27.0 → 25.0 → **25.0** (OI 8.9K). Same-day whipsaw on last trades. Close 11/06. → LABOR, HENRY

**6. 🟡 AI DOWNTURN ODDS ROSE; RECESSION ODDS BARELY DID.** PM AI bubble burst 8.25 → **12.45** (liq $68.1K). PM recession 4.5 flat. Kalshi GDP-rule recession 2.0 → 4.0 (OI 857.8K). PM S&P best asset 85.5. ⚠️ Market text not re-read tonight. → BROCK, VULCAN · KB-ORC-123

**7. 🟠 BANK FAILURE: STILL TOO THIN TO READ, EVEN TODAY.** PM any-bank 12/31 **70.5**, liq $2.6K ⚠️, vol unchanged at $14.6K on a day KRE fell 2.46%. Named top 3.4 ($372 liq ⚠️). Bailout 7.0 ($842 liq ⚠️). Not marked, not routed. → REGINALD (no signal) · KB-ORC-122

**8. 🟡 POLYMARKET PLATFORM RISK.** Halted 10/29 18:33Z after a third-party compromise (SIG-W-20261029-045). Resumption time not established. Tonight's PM/Kalshi agreement on the Fed (63.5 vs 65.0) is one point of comfort, not a clearance. KB-ORC-121

---

## Signal Dashboard — 2026-11-05T23:11Z (= ET Thu 11/05, context pull)

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ1d | Δ7d | Depth | Note |
|---|---|---|---|---|---|---|
| US bank failure by 12/31 (any) | PM | 70.5 | — | −1.0 | $2.6K liq ⚠️ | not marked |
| Which banks fail EOY (top) | PM | 3.4 | −0.1 | −0.5 | $372 liq ⚠️ | |
| Major bank bailout <2027 | PM | 7.0 | — | — | $842 liq ⚠️ | |
| Fed: HIKE at Dec mtg | PM | **63.5** | −14.0 | −8.0 | $417.7K liq | 11/05 read 73.5 |
| Fed: NO change at Dec mtg | PM | 33.5 | +12.0 | +7.0 | $401.6K liq | |
| Fed ≥1 more hike by Dec (`>4.00`) | Kalshi | 65.0 | −15.0 | — | OI 88.8K | |
| Fed 2 more by Dec (`>4.25`) | Kalshi | 2.0 | 0.0 | — | OI 69.0K | |
| Fed: ANOTHER hike 2026 | PM | 63.5 | −14.0 | −8.5 | $96.1K liq | |
| Fed hike count (top) | PM | 65.0 | −12.5 | −8.0 | $54.6K liq | |
| End-2026 funds rate (top) | PM | 64.3 | −11.7 | −11.1 | $16.1K liq | |
| Fed: NO cuts 2026 | PM | 97.5 | −0.2 | +0.3 | $524.2K liq | |
| US recession 2026 (GDP or NBER) | PM | 4.5 | −1.0 | −2.5 | $84.3K liq | ≠ Kalshi definition |
| Recession 2025-26 (GDP rule) | Kalshi | 4.0 | +1.0 | — | OI 857.8K | |
| US inflation >5% 2026 | PM | 6.0 | −0.5 | −2.5 | $67.7K liq | |
| Oct CPI modal 3.7% | PM | 86.0 | −4.0 | −3.5 | $1.3K liq ⚠️ | ends 11/11; Kalshi YoY not listed |
| Oct U3 `>4.1%` / `>4.2%` | Kalshi | 64.0 / 25.0 | −4 / −1 | — | OI 48.1K / 8.9K | Fri 11/06 |
| US credit downgrade 2026 | Kalshi | 1.2 (⚠mid 3.1) | −0.1 | — | OI 33.3K, 4¢ book | |
| Hormuz traffic normal by 11/30 | PM | 3.6 | −0.2 | −1.9 | $257.9K liq | |
| Hormuz traffic normal by 12/31 | PM | 10.5 | — | −1.0 | $351.9K liq | PortWatch PRINT |
| Effective ceasefire 11/15 · 11/30 · 12/31 | PM | 57.5 · 38.5 · 28.0 | +0.5 · −4.0 · −2.5 | new | $51.3K · $62.3K · $59.5K | new series 11/04 |
| Blockade-end 3/31/27 (top) | PM | 69.5 | −1.5 | +10.0 | $120.8K liq | |
| China invade Taiwan <2027 | PM | 1.8 | — | −1.1 | $476.0K liq | |
| China GDP 2026 (top) | PM | 96.1 | −0.1 | −0.4 | $5.5K liq | → ZHAO |
| **WTI $110 Nov (v5 supply leg)** | PM | **17.0** | +4.0 | −33.0 | $30.3K liq / $47.1K vol | 11/05 read 16.0; state none |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ7d | Depth | Note |
|---|---|---|---|---|---|
| US invade Iran <2027 | PM | 12.5 | −7.5 | $78.0M vol | |
| Iranian regime fall <2027 | PM | 2.9 | −3.6 | $29.5M vol | |
| Next US–Iran senior meeting by 12/31 | PM | 43.0 | −2.0 | $87.8K liq | |
| US–Iran deal 2026 (top component) | PM | 13.5 | +0.5 | $75.3K liq | d1 −4.0 |
| Iran ends enrichment by 12/31 | PM | 7.6 | +1.3 | $67.4K liq | |
| US declares war on Iran | PM | 2.2 | −2.9 | $69.8K liq | |
| Hormuz weekly wk-of-11/2 (top) | PM | 47.5 | +31.5 | $67 liq ⚠️ | wk-of-11/9 listed, no volume yet |
| Hormuz avg daily end-Nov (top) | PM | 46.5 | — | $411 liq ⚠️ | |
| Hormuz any-day by 11/30 (top) | PM | 36.0 | — | $1.3K liq ⚠️ | |
| Bab el-Mandeb closed (top) | PM | 7.5 | −7.0 | $99.5K liq | |
| Brent >$97.99 / >$95.99 @ 11/30 | Kalshi | 43.0 / 55.0 | new | OI 6.3K / 4.1K | pinned 11/05; last trades |
| OPEC: another exit 2026 | PM | 6.5 | −8.5 | $22.3K liq | → BRENT |
| Venezuela: Delcy out <2027 | PM | 7.5 | −0.5 | $21.0K liq | |
| BOJ Dec: hike 25bp | PM | 89.5 | +14.0 | $2.9K liq ⚠️ | → SAM |
| Russia–Ukraine ceasefire by 12/31 | PM | 16.0 | +0.5 | $126.0K liq | d1 +3.5 |
| Clarity Act signed 2026 | PM | 3.0 | −0.2 | $183.6K liq | → BROCK |
| AI bubble burst 2026 | PM | 12.4 | +2.2 | $68.1K liq | d1 +5.7 → BROCK |
| US debt default <2027 | PM | 1.5 | −0.1 | $6.2K liq | |
| MicroStrategy bankruptcy <2027 | PM | 2.4 | −1.1 | $15.1K liq | |
| 10Y / 30Y Nov ladders | PM | — | — | all <$130 liq ⚠️ | not marked; `^TNX` 4.84 11/05 |
| Corporate bankruptcies >750 | Kalshi | 69.0 (⚠mid 73.0) | — | OI 6.0K, 8¢ book | |

### Tier 3 — sentiment
| Market | Plat | Now | Δ7d | Note |
|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 88.0 | +8.0 | 13 extreme events, not a complacency gauge (KB-ORC-115) |
| Best asset 2026 (top = S&P) | PM | 85.5 | +10.0 | BTC and gold legs not re-read tonight |
| FL Cat-4 / Cat-5 by 2027 | PM | 4.0 / 2.6 | −1.5 / −0.1 | ⚠️ $1.7K / $1.3K liq |

**Derived series (`DISRUPTION_SUPPLY_SPREAD.tsv`):** v5 Nov segment +36.0 (10/28) · +36.0 · +25.5 (10/30) · +52.0 · +58.0 · +64.0 (11/04) · **+73.5 (11/05 read)** · +72.5 @ 23:11Z context. Never chart across segments.

---

## Convergence Matrix (2026-11-05T23:11Z)

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| Bank failure | any-bank 70.5 (⚠️ $2.6K liq); named top 3.4 | REGINALD | book too thin to mark | 🟠 thin instrument |
| Fed path | Dec hike PM 63.5 / Kalshi 65.0 (context) | LIQUID/HENRY own | venues within 1.5pp | 🟠 repricing |
| Rates (10Y) | ^TNX 4.84; Nov rungs <$130 liq | BOND/TERRY own | par==DGS10 unconfirmed | 🟡 |
| Inflation | Oct CPI modal 3.7 at 86.0 ⚠️ thin | HENRY owns the print | Kalshi YoY ladder not listed | 🟡 |
| Recession 2026 | PM 4.5 / Kalshi 4.0 | RED 4–12% (NBER-dated) | structural definitional gap | 🟡 |
| Oil: premium vs shortage | Nov $110 17.0; WTI ~$91 | premium ≠ shortage | spread +72.5, the supply leg moved | 🟠 |
| Iran | another US strike 61.5 by 11/30; invade 12.5 | HAWK owns | both priced; separate contracts give no conditional read | 🟠 |
| Tail sentiment | S&P best-asset 85.5 through a −4.4% day | — | one day | 🟡 |

---

## Maintenance flags

*Structural detail → `MAINTENANCE.md` (entry 2026-11-05); findings → `workbook/KB.tsv` (KB-ORC-118 to 124).*

- ✅ **Combination watch set up 11/05 (WQ-622 A):** six themes, KB-ORC-119 to 124; charter step 7a; list sent to PROME.
- ✅ **Kalshi Brent re-pinned 11/05:** `KXBRENTMON-26NOV3017` T97.99, T95.99. Off-center rungs are OI 0 and not monotonic.
- ⏳ **Rolls due:** Hormuz weekly → wk-of-11/9 at 11/09 · Hormuz on-date (no November event found) · Kalshi `KXCPIYOY-26OCT` 0 markets · December $110 when listed · Kalshi `KXU3-26NOV` after 11/06 (event is open).
- ✅ **Hormuz 0-ships closure `⛔` is a false flag:** the row says do not replace (`watchlist.tsv`, diagnosed 8/27). Context column only.
- 🔵 **Coverage due ≤11/11.** Movers ran 23:1xZ: top hits were crypto and SPY dip ladders (near-resolution or equity tape), none pinned. Russian diesel nomination still awaits BRENT/OSPREY.
- ⚠️ **The routine pulls and never grades.** Owner question sits on WQ-599 (Will, Sat 11/07). Routine unchanged.
- ⚠️ **Two boxes collide:** both crons run; `SCHEDULED_RUNS.md` § Known limits.
- ⚠️ **Kalshi lane is per-box:** laptop = UNSIGNED. Signed round-trip unverified since the 10/15 code change.
- ⚠️ **Kalshi `pull` has no double-log guard:** the 23:15Z re-pull logged all 9 rows, so 7 markets have two context rows tonight. Polymarket has one; Kalshi does not.
- ⚠️ **Kalshi `pull` logs FINALIZED markets' last trades as `yes_prob`.** Read `[finalized]` / API `result`.
- ⚠️ **Never use `pull --log --force` to log new pins.**
- ⚠️ **`TRADE.md` tables not regenerated tonight;** `TRADE_MARKS.tsv` is current, the rendered tables are as of 11/04.
- ⚠️ `STATUS.md` read-cap: re-check each closeout (`scripts/read_cap_check.py --agent ORACLE`).

## BOTTOM LINE

**December hike odds fell from 80.5% to 63.5% in about a day.** Stocks fell 4.4% and VIX reached 28 on the same day, and both venues moved together. The cause is not established, and no gate cleared.

**The rest moved far less.** Strike odds stayed high, $110 oil stayed low, recession stayed under 5%, AI downturn odds rose to 12%, and bank-failure books stayed too thin to read. Tomorrow's jobs report is the next real test of the Fed repricing.
