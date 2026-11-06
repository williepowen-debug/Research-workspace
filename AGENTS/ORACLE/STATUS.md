# ORACLE STATUS

**Live dashboard: prediction-market probabilities, divergences, alerts.**
**FULL REWRITE 2026-11-06 (Fri 15:3x ET, from `date`) — desktop `DESKTOP-BC6EF81`, Kalshi SIGNED (`status` rc=0).** Pulls: Polymarket `pull --log` **2026-11-06T20:26Z** (52 rows) · Kalshi 20:26Z 9/9 · spread row 20:26Z · `history --write` (8,861 rows / 52 markets) · `movers` 20:2xZ · `trade_marks --write`. The 11/06 gate read is the routine's 10:15 ET pull (15:15Z, this box). **20:26Z is a later pull on the same ET date, so it is CONTEXT, never a gate read** (letter O3).

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price; re-pull. Every figure carries platform/date/depth. Thin books (<$5K liq) are flagged ⚠️ and never marked on one print. Kalshi depth proxy = open interest. "PM" = Polymarket.

---

## 🔴 Alerts (read first)

**1. 🟠 DECEMBER HIKE ODDS BACK AT ABOUT 78 AFTER PAYROLLS; THREE MARKETS AGREE; NO GATE CLEARED.** PM HIKE-at-Dec **77.5** at 20:26Z (book 77/78, vol $5.0M, liq $312.4K); 11/06 read 77.5 (liq $322.7K). Kalshi ≥1 more by Dec **78.0** (book 77/78, OI 92.5K). Expected move at 15:18–15:26 ET: PM +19.3bp, Kalshi +19.0bp, futures +19.0 to +19.5bp (Yahoo last trades, EFFR 3.88 [11/05]; ZQZ26 = 76, ZQF27 = 78). No dislocation. '78 from 70' holds as a level (PM 69.5 at 08:25 ET → 77.5 at 08:35 ET). ⚠️ The Reuters sentence itself is unverified: the cp24 relay carries no odds line. ⚠️ About 6 of the 14-point rebound came BEFORE the print (PM 63.5 → 69.5 by 05:00 ET), cause not established. The 11/05 fall: −17.0 from the 80.5 spike, −14.0 from PM's held 77.5, −17.0 on Kalshi; five markets moved together 10:40–10:50 ET, so it was no venue artifact. ⚠️ **Cause still NOT established**; the Hammack headline at 10:41 ET reads hawkish, the wrong direction, body unread. VX-ORC-12 Alert HELD; lowest read 69.5; next read Mon 11/09. → HENRY, LIQUID, BOND, PROME · KB-ORC-125, KB-ORC-126 · `research/2026-11-06_dec-hike-verification.md`

**2. 🟠 VX-ORC-07 (48h moves) STEPPED DOWN, CRITICAL TO ALERT.** The WTI pair (36.0 → 13.0) left the 48h window at 2026-11-06T07Z. Largest inside the window: Fed HIKE 63.5 (11/05T23:11Z) → 77.5 (11/06T15:15Z) = +14.0 in 16h, log; +15.0 on CLOB. WTI $110 Nov largest CLOB pair +8.5. Log pass covers non-thin rows only; CLOB checked for Fed HIKE, WTI and AI bubble only. → PROME (triage)

**3. 🟠 THE CROWD STILL PRICES MORE STRIKES THAN OIL RISK.** PM effective ceasefire 11/15 **59.0** · 11/30 **40.0** · 12/31 **28.5** (liq $67.3K · $82.7K · $115.5K): implied another US strike 41.0 · 60.0 · 71.5. WTI $110 Nov **20.0** (11/06 read 19.0; vol $65.2K, liq $38.4K). US invade Iran 10.5 (vol $78.2M) · regime fall 3.0. Blockade-end 3/31/27 71.5 · next senior meeting 12/31 41.0. ⚠️ Separate contracts with different rules; they do not show what traders expect oil to do if a strike happens. PM "ceasefire" means no US strike landing on Iran, not a formal truce (KB-ORC-111). No leg has resolved NO. → HAWK, BRENT, FALCON · KB-ORC-112, KB-ORC-119

**4. 🟡 NOVEMBER $110 OIL: NO ACTIVE ALERT.** Reads 10/28 52.5 · 52.5 · 64.0 (Alert) · 36.5 · 30.5 · 25.5 (cleared) · 16.0 · **11/06 19.0** (liq $21.4K, run 8; context 20:26Z 20.0). Spread +71.5 (11/06 read), +70.5 (context 20:26Z). ⚠️ The 10/29 read came 7h42m after Polymarket's 18:33Z halt; excluded, no Alert fired. WTI Dec `CLZ26` $90.93 / Brent Jan `BZF27` $98.34 (Yahoo last, 20:26Z). Kalshi Brent > $97.99 at 11/30 42.0 (⚠mid 45.5, OI 6.3K). → BRENT, FALCON, HAWK · VX-ORC-04

**5. 🟡 OCTOBER JOBS GRADED.** Print 4.1% (BLS 11/06). Kalshi `KXU3-26OCT` finalized 4.1%: `>4.0` YES, `>4.1` NO, `>4.2` NO. Crowd mode was 4.2 (39 to 49); the print came one notch below it, on the stronger-labor side. Rolled to `KXU3-26NOV-T4.1` / `T4.2` (closes 12/04T13:29Z; book 43/46 and 0/13 at 20:3xZ; first logged by the next pull). → LABOR, HENRY · KB-ORC-124

**6. 🟡 AI DOWNTURN ODDS ROUND-TRIPPED.** PM AI bubble burst 8.25 (11/05 10:00 ET) → 15.9 (16:00 ET, CLOB) → 12.45 → **7.55** (20:26Z, liq $143.6K, vol $2.6M). PM recession 4.5 · Kalshi GDP-rule 3.0 (OI 857.8K) · S&P best asset 87.5 (liq $15.3K). Cash HY 348 [11/05], +16bp (SIG-W-20261106-012). ⚠️ Market text not re-read. → BROCK, VULCAN · KB-ORC-123

**7. 🟠 BANK FAILURE: STILL TOO THIN TO READ.** PM any-bank 12/31 **70.5**, liq $2.2K ⚠️, vol $14.6K. Named top 3.4 ($412 liq ⚠️). Bailout 7.0 ($873 liq ⚠️). Not marked, not routed. → REGINALD (no signal) · KB-ORC-122

**8. 🟡 VENUE RISK.** Polymarket halted 10/29 18:33Z after a third-party compromise; resumption time not established (KB-ORC-121). Utah charged Kalshi and its CEO and COO about 10/28, CFTC contesting, no ruling found; Kalshi lane live (KB-ORC-127, new theme `venue-legal-risk`). Today's agreement (PM 77.5, Kalshi 78.0, futures about 76–78) is comfort, not clearance.

---

## Signal Dashboard — 2026-11-06T20:26Z (= ET Fri 11/06, context pull)

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ1d | Δ7d | Depth | Note |
|---|---|---|---|---|---|---|
| US bank failure by 12/31 (any) | PM | 70.5 | — | −1.0 | $2.2K liq ⚠️ | not marked |
| Which banks fail EOY (top) | PM | 3.4 | +0.1 | −0.8 | $412 liq ⚠️ | |
| Major bank bailout <2027 | PM | 7.0 | — | — | $873 liq ⚠️ | |
| Fed: HIKE at Dec mtg | PM | **77.5** | +12.0 | +7.0 | $312.4K liq | 11/06 read 77.5 |
| Fed: NO change at Dec mtg | PM | 20.5 | −11.0 | −7.0 | $380.6K liq | |
| Fed ≥1 more hike by Dec (`>4.00`) | Kalshi | 78.0 | +12.0 | — | OI 92.5K | book 77/78 |
| Fed 2 more by Dec (`>4.25`) | Kalshi | 3.0 | +2.0 | — | OI 73.9K | book 1/2 |
| Fed: ANOTHER hike 2026 | PM | 76.5 | +10.0 | +6.5 | $85.8K liq | |
| Fed hike count (top) | PM | 75.5 | +10.0 | +4.0 | $25.4K liq | |
| End-2026 funds rate (top) | PM | 75.3 | +10.0 | +6.9 | $6.2K liq | |
| Fed: NO cuts 2026 | PM | 97.7 | +0.3 | +1.2 | $613.8K liq | |
| US recession 2026 (GDP or NBER) | PM | 4.5 | — | −2.0 | $63.4K liq | ≠ Kalshi definition |
| Recession 2025-26 (GDP rule) | Kalshi | 3.0 | −1.0 | — | OI 857.8K | |
| US inflation >5% 2026 | PM | 4.5 | −1.5 | −4.0 | $68.3K liq | |
| Oct CPI modal | PM | 87.5 | −1.5 | −2.0 | $3.4K liq ⚠️ | ends 11/11; no Kalshi October YoY event |
| Nov U3 `>4.1%` / `>4.2%` | Kalshi | 43/46 · 0/13 book | — | — | OI 2.0K / 3.0K | not yet logged |
| US credit downgrade 2026 | Kalshi | 4.9 (⚠mid 3.0) | +3.7 | — | OI 33.3K, 4¢ book | not a move; book noise |
| Hormuz traffic normal by 11/30 | PM | 3.5 | −0.3 | −2.5 | $255.2K liq | |
| Hormuz traffic normal by 12/31 | PM | 9.5 | −1.0 | −1.0 | $380.8K liq | PortWatch PRINT |
| Effective ceasefire 11/15 · 11/30 · 12/31 | PM | 59.0 · 40.0 · 28.5 | −3.5 · +2.5 · −1.0 | new | $67.3K · $82.7K · $115.5K | |
| Blockade-end 3/31/27 (top) | PM | 71.5 | +1.0 | +9.0 | $124.3K liq | |
| China invade Taiwan <2027 | PM | 1.8 | −0.1 | −0.4 | $502.3K liq | |
| China GDP 2026 (top) | PM | 96.2 | +0.1 | −0.1 | $6.9K liq | → ZHAO |
| **WTI $110 Nov (v5 supply leg)** | PM | **20.0** | +1.5 | −38.0 | $38.4K liq / $65.2K vol | 11/06 read 19.0; state none |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ7d | Depth | Note |
|---|---|---|---|---|---|
| US invade Iran <2027 | PM | 10.5 | −8.0 | $78.2M vol | |
| Iranian regime fall <2027 | PM | 3.0 | −2.5 | $29.5M vol | |
| Next US–Iran senior meeting by 12/31 | PM | 41.0 | −4.0 | $68.4K liq | |
| US–Iran deal 2026 (top component) | PM | 12.5 | −1.5 | $62.8K liq | |
| Iran ends enrichment by 12/31 | PM | 7.2 | +0.8 | $68.3K liq | |
| US declares war on Iran | PM | 2.4 | −2.2 | $71.4K liq | |
| Hormuz weekly wk-of-11/2 (top) | PM | 52.0 | +12.0 | $70 liq ⚠️ | roll 11/09 |
| Hormuz avg daily end-Nov (top) | PM | 53.0 | — | $5.3K liq | top leg, d1 +12.5; not read |
| Hormuz any-day by 11/30 (top) | PM | 24.0 | — | $11.7K liq | top leg, d1 −12.5; not read |
| Bab el-Mandeb closed (top) | PM | 8.5 | −5.0 | $106.8K liq | |
| Brent >$97.99 / >$95.99 @ 11/30 | Kalshi | 42.0 / 54.0 | — | OI 6.3K / 4.1K | ⚠mid 45.5 / 51.5 |
| OPEC: another exit 2026 | PM | 6.5 | −3.0 | $19.9K liq | → BRENT |
| Venezuela: Delcy out <2027 | PM | 7.5 | −1.0 | $21.0K liq | |
| BOJ Dec: hike 25bp | PM | 78.0 | +0.5 | $2.3K liq ⚠️ | d1 −11.5 on a thin book → SAM |
| Russia–Ukraine ceasefire by 12/31 | PM | 14.5 | — | $117.8K liq | |
| Clarity Act signed 2026 | PM | 2.5 | −0.6 | $150.0K liq | → BROCK |
| AI bubble burst 2026 | PM | 7.5 | −2.1 | $143.6K liq | d1 −10.2 → BROCK |
| US debt default <2027 | PM | 1.4 | −0.1 | $6.2K liq | |
| MicroStrategy bankruptcy <2027 | PM | 1.5 | −2.1 | $16.7K liq | |
| 10Y / 30Y Nov ladders | PM | — | — | all <$130 to $1.2K liq ⚠️ | not marked; `^TNX` 4.859 19:59Z |
| Corporate bankruptcies >750 | Kalshi | 69.0 (⚠mid 73.0) | — | OI 6.0K, 8¢ book | |

### Tier 3 — sentiment
| Market | Plat | Now | Δ7d | Note |
|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 88.0 | +8.0 | 13 extreme events, not a complacency gauge (KB-ORC-115) |
| Best asset 2026 (top = S&P) | PM | 87.5 | +7.0 | $15.3K liq |
| FL Cat-4 / Cat-5 by 2027 | PM | 4.0 / 2.6 | −1.5 / −0.1 | ⚠️ $2.8K / $1.3K liq |

**Derived series (`DISRUPTION_SUPPLY_SPREAD.tsv`):** v5 Nov segment +36.0 (10/28) · +36.0 · +25.5 (10/30) · +52.0 · +58.0 · +64.0 · +73.5 (11/05) · **+71.5 (11/06 read)** · +70.5 @ 20:26Z context. Never chart across segments.

---

## Convergence Matrix (2026-11-06T20:26Z)

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| Bank failure | any-bank 70.5 (⚠️ $2.2K liq); named top 3.4 | REGINALD | book too thin to mark | 🟠 thin instrument |
| Fed path | Dec hike PM 77.5 / Kalshi 78.0; futures 76–78 | LIQUID/HENRY own | within 1bp of expected move | 🟠 repriced twice in two days |
| Rates (10Y) | ^TNX 4.859 (19:59Z); Nov rungs thin | BOND/TERRY own | par==DGS10 unconfirmed | 🟡 |
| Inflation | Oct CPI modal at 87.5 ⚠️ thin | HENRY owns the print | no Kalshi October YoY event | 🟡 |
| Recession 2026 | PM 4.5 / Kalshi 3.0 | RED 4–12% (NBER-dated) | structural definitional gap | 🟡 |
| Oil: premium vs shortage | Nov $110 20.0; WTI Dec $90.93 | premium ≠ shortage | spread +70.5, the supply leg moved | 🟠 |
| Iran | another US strike 60.0 by 11/30; invade 10.5 | HAWK owns | both priced; separate contracts give no conditional read | 🟠 |
| Tail sentiment | S&P best-asset 87.5; AI bubble back to 7.5 | — | two days | 🟡 |

---

## Maintenance flags

*Structural detail → `MAINTENANCE.md`; findings → `workbook/KB.tsv` (KB-ORC-118 to 127).*

- ✅ **Kalshi U3 rolled 11/06:** `KXU3-26NOV-T4.1`, `T4.2`. First logged by the next pull; never `--force`.
- ✅ **Signed Kalshi lane verified on the desktop 11/06:** `status` rc=0.
- ⏳ **Rolls due:** Hormuz weekly → wk-of-11/9 at 11/09 · Hormuz on-date (no November event found) · December $110 when listed.
- ⏳ **Kalshi CPI:** `KXCPIYOY-26OCT` returns 404; open events are `26NOV` (November data, closes 12/10; OI 57.4K on `T3.8`) and `26DEC`. Candidate pin, not pinned.
- ✅ **Hormuz 0-ships closure `⛔` is a false flag:** the row says do not replace (`watchlist.tsv`, diagnosed 8/27). Context column only.
- 🔵 **Coverage due ≤11/11.** Movers ran 20:2xZ: hits unread, sent to PROME for triage, none pinned. Russian diesel nomination still awaits BRENT/OSPREY.
- ⚠️ **The routine pulls and never grades.** Owner question sits on WQ-599 (Will, Sat 11/07). Routine unchanged.
- ⚠️ **Two boxes collide:** both crons run; `SCHEDULED_RUNS.md` § Known limits.
- ⚠️ **Kalshi lane is per-box:** laptop = UNSIGNED.
- ⚠️ **Kalshi `pull` has no double-log guard.** It also logs FINALIZED markets' last trades as `yes_prob`; read `[finalized]` / API `result`.
- ⚠️ **Never use `pull --log --force` to log new pins.**
- ⚠️ **`TRADE.md` tables not regenerated;** `TRADE_MARKS.tsv` is current, the rendered tables are as of 11/04.
- ⚠️ `STATUS.md` read-cap: re-check each closeout (`scripts/read_cap_check.py --agent ORACLE`).

## BOTTOM LINE

**December hike odds are back near 78%, about where they stood before Thursday's selloff.** Polymarket, Kalshi and fed funds futures agree to within 1bp of expected move. Friday's jobs beat did part of it, but about 6 of the 14 points came before the print. The cause of Thursday's fall is still not established.

**Elsewhere the crowd is calmer than Thursday.** AI downturn odds round-tripped to 7.5, strike odds stayed high, $110 oil stayed near 20, recession stayed under 5%, and bank-failure books stayed too thin to read.

---

## Cross-agent tensions

1. 🟠 **ORACLE ↔ LIQUID/HENRY/BOND: Fed repricing, cause open.** Odds fell 14 to 17 points on 11/05 with stocks and rebounded 14 on 11/06, part before the print. Packets sent 11/05 and 11/06.
2. 🟠 **ORACLE ↔ BRENT/HAWK/FALCON: strike odds vs oil odds.** Another US strike 60.0 by 11/30 against $110 at 20.0.
3. 🟠 **ORACLE ↔ BOND/TERRY: 10Y resolution basis.** The ladder resolves on the Treasury par "10 Yr"; gates key on DGS10. Equivalence unconfirmed since 9/17.
4. 🟠 **ORACLE ↔ RED: recession definitions.** Kalshi GDP-rule 3.0 vs PM GDP-or-NBER 4.5 is structural (KB-ORC-099).

---

## Forward catalysts (dated)

| Date | Event | Instrument | Note |
|---|---|---|---|
| Mon 11/09 | Hormuz weekly rolls · next gate reads | wk-of-11/9 listed | ⚠️ thin |
| Wed 11/11 | October CPI market end | PM modal at 87.5 ($3.4K liq ⚠️) | → HENRY |
| 11/15 | Effective ceasefire | PM 59.0 | → HAWK, FALCON |
| 2026-11-17T01:00Z | Nov $110 Active-Month switch Dec26→Jan27 (INFERRED) | v5 Nov | R3 reset |
| 11/30 | Effective ceasefire · Hormuz normal · Kalshi Brent month-end | PM 40.0 · 3.5 · `>$97.99` 42.0 | → HAWK, BRENT, FALCON |
| 12/04 | November jobs | Kalshi `KXU3-26NOV` | → LABOR, HENRY |
| Wed 12/09 | FOMC December | PM hike 77.5 / Kalshi 78.0 | → LIQUID, HENRY, BOND |
| 2026-12-15 | Kalshi gap-fill quarterly re-check (WQ-305) | KXCREDEFMAX · KXCCDELINQ · KXCCCHGOFF · KXFEDFACILITY | |
