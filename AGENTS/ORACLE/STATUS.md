# ORACLE STATUS

**Live dashboard: prediction-market probabilities, divergences, alerts.**
**UPDATE 2026-11-06 (Fri 15:3x ET, from `date`) — desktop `DESKTOP-BC6EF81`, Kalshi SIGNED (`status` rc=0).** Pulls 20:26Z: Polymarket 52 rows, Kalshi 9/9, spread row. The 11/06 gate read is the routine's 15:15Z pull; 20:26Z is a later pull, context under letter O3. Alerts 1, 2, 4, 5 and 6 below are as of this update. The dashboard tables below stay 11/05T23:11Z until the closeout rewrite.

**FULL REWRITE 2026-11-05 (Thu 18:11–18:2x ET, from `date`) — laptop `WilliePOwen`, Kalshi UNSIGNED (`status` rc=3, public market data).** Pulls: Polymarket `pull --log` **2026-11-05T23:11Z** (52 rows) · Kalshi 23:11Z 7/7, 23:15Z 9/9 after the Brent re-pin · spread row 23:11Z · `history --write` (8,791 rows / 52 markets) · `movers` 23:1xZ · `trade_marks --write`. The 11/05 gate read is the routine's 10:15 ET pull (15:15Z, desktop). **Tonight's 23:11Z is a later pull on the same ET date, so it is CONTEXT, never a gate read** (letter O3).

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price; re-pull. Every figure carries platform/date/depth. Thin books (<$5K liq) are flagged ⚠️ and never marked on one print. Kalshi depth proxy = open interest. "PM" = Polymarket.

---

## 🔴 Alerts (read first)

**1. 🟠 DECEMBER HIKE ODDS BACK AT ABOUT 78 AFTER PAYROLLS; THREE MARKETS AGREE; NO GATE CLEARED.** PM HIKE-at-Dec **77.5** at 20:26Z (book 77/78, vol $5.0M, liq $312.4K); 11/06 read 77.5 (liq $322.7K). Kalshi ≥1 more by Dec **78.0** (book 77/78, OI 92.5K). Expected move at 15:18–15:26 ET: PM +19.3bp, Kalshi +19.0bp, futures +19.0 to +19.5bp (Yahoo last trades, EFFR 3.88 [11/05]; ZQZ26 = 76, ZQF27 = 78). No dislocation. '78 from 70' holds as a level (PM 69.5 at 08:25 ET → 77.5 at 08:35 ET). ⚠️ The Reuters sentence itself is unverified: the cp24 relay carries no odds line. ⚠️ About 6 of the 14-point rebound came BEFORE the print (PM 63.5 → 69.5 by 05:00 ET), cause not established. The 11/05 fall: −17.0 from the 80.5 spike, −14.0 from PM's held 77.5, −17.0 on Kalshi; five markets moved together 10:40–10:50 ET, so it was no venue artifact. ⚠️ **Cause still NOT established**; the Hammack headline at 10:41 ET reads hawkish, the wrong direction, body unread. VX-ORC-12 Alert HELD; lowest read 69.5; next read Mon 11/09. → HENRY, LIQUID, BOND, PROME · KB-ORC-125, KB-ORC-126 · `research/2026-11-06_dec-hike-verification.md`

**2. 🟠 VX-ORC-07 (48h moves) STEPPED DOWN, CRITICAL TO ALERT.** The WTI pair (36.0 → 13.0) left the 48h window at 2026-11-06T07Z. Largest inside the window: Fed HIKE 63.5 (11/05T23:11Z) → 77.5 (11/06T15:15Z) = +14.0 in 16h, log; +15.0 on CLOB. WTI $110 Nov largest CLOB pair +8.5. Log pass covers non-thin rows only; CLOB checked for Fed HIKE, WTI and AI bubble only. → PROME (triage)

**3. 🟠 THE CROWD STILL PRICES MORE STRIKES THAN OIL RISK.** PM effective ceasefire 11/15 **57.5** · 11/30 **38.5** · 12/31 **28.0** (liq $51.3K · $62.3K · $59.5K): implied another US strike 42.5 · 61.5 · 72.0. WTI $110 Nov **17.0** (11/05 read 16.0; vol $47.1K, liq $30.3K). US invade Iran 12.5 (vol $78.0M) · regime fall 2.9. Blockade-end 3/31/27 69.5 · next senior meeting 12/31 43.0. ⚠️ Separate contracts with different rules; they do not show what traders expect oil to do if a strike happens. PM "ceasefire" means no US strike landing on Iran, not a formal truce (KB-ORC-111). FALCON's FAL-07 RESOLVED CONFIRMED 11/04 is consistent with that record. ⚠️ FALCON: no on-record CENTCOM; 11/2 is the first CONFIRMED date, not necessarily the first strike. → HAWK, BRENT, FALCON · KB-ORC-112, KB-ORC-119

**4. 🟡 NOVEMBER $110 OIL: NO ACTIVE ALERT.** Reads 10/28 52.5 · 52.5 · 64.0 (Alert) · 36.5 · 30.5 · 25.5 (cleared) · 16.0 · **11/06 19.0** (liq $21.4K; context 20:26Z 20.0). Spread +71.5 (11/06 read), +70.5 (context 20:26Z). ⚠️ The 10/29 read came 7h42m after Polymarket's 18:33Z halt; excluded, no Alert fired. WTI ~$90.98 / Brent ~$99.15 evening bars (`fetch.py`, session spans two days, Brent contract unknown). Kalshi Brent > $97.99 at 11/30 43.0 (OI 6.3K). → BRENT, FALCON, HAWK · VX-ORC-04

**5. 🟡 OCTOBER JOBS GRADED.** Print 4.1% (BLS 11/06). Kalshi `KXU3-26OCT` finalized 4.1%: `>4.0` YES, `>4.1` NO, `>4.2` NO. Crowd mode was 4.2 (39 to 49); the print came one notch below it, on the stronger-labor side. Rolled to `KXU3-26NOV-T4.1` / `T4.2` (closes 12/04T13:29Z; book 43/46 and 0/13 at 20:3xZ; first logged by the next pull). → LABOR, HENRY · KB-ORC-124

**6. 🟡 AI DOWNTURN ODDS ROUND-TRIPPED.** PM AI bubble burst 8.25 (11/05 10:00 ET) → 15.9 (16:00 ET, CLOB) → 12.45 → **7.55** (20:26Z, liq $143.6K, vol $2.6M). PM recession 4.5 · Kalshi GDP-rule 3.0 (OI 857.8K) · S&P best asset 87.5 (liq $15.3K). Cash HY 348 [11/05], +16bp (SIG-W-20261106-012). ⚠️ Market text not re-read. → BROCK, VULCAN · KB-ORC-123

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
