# ORACLE STATUS

**Live dashboard: prediction-market probabilities, divergences, alerts.**
**FULL REWRITE 2026-11-06 (Fri 17:3x ET, from `date`; Iran legs updated 18:4x ET) — desktop `DESKTOP-BC6EF81`, Kalshi SIGNED (`status` rc=0).** Pulls: Polymarket `pull --log` **2026-11-06T22:15Z** (52 rows) · Kalshi 22:15Z 9/9 · spread row 22:15Z · `history --write` (8,843 rows / 52 markets) · `movers` 22:1xZ · `trade_marks --write`. The 11/06 gate read is the routine's 10:15 ET pull (15:15Z, this box). **22:15Z is a later pull on the same ET date, so it is CONTEXT, never a gate read** (letter O3). Close refresh on Will's 17:08 ET word via prome-51.

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price; re-pull. Every figure carries platform/date/depth. Thin books (<$5K liq) are flagged ⚠️ and never marked on one print. Kalshi depth proxy = open interest. "PM" = Polymarket.

---

## 🔴 Alerts (read first)

**0. 🔴 SECOND SPIKE AND SNAPBACK, 00:05Z TO 00:52Z 11/07 (19:05–19:52 ET 11/06; laptop, CLOB book read, not a log row).** PM effective ceasefire 23:34Z → low trade → book 00:51:40Z: 11/15 48.0 → 1.2 → 25.0/27.4 · 11/30 35.5 → 1.1 → 20.9/26.9 · 12/31 22.5 → 1.0 → 6.2/8.9. No leg closed. No report of a new US strike found; cause NOT established. Oil, invade and war odds unmoved (Gamma 00:48Z, may lag). ⚠️ Touch sizes $0 to $77 in 35 of 36 readings. ⚠️ Gamma 3.75 was stale against CLOB 21/34: read the book in a fast move. No score moved. → WALTER (packet, commit 7de38dd855) · KB-ORC-130

**1. 🔴 STRIKE ODDS JUMPED AFTER THE CLOSE, THEN GAVE BACK MORE THAN HALF; QESHM REPORTS, ATTACKER UNNAMED; CAUSE NOT ESTABLISHED.** PM effective ceasefire 20:26Z → 22:15Z log → **23:34Z (Gamma read, not a log row):** 11/15 59.0 → 31.5 → **48.0** (47/49, liq $56.4K) · 11/30 40.0 → 27.0 → **35.5** (35/36, liq $75.7K) · 12/31 28.5 → 16.0 → **22.5** (22/23, liq $95.7K). Implied another US strike 52 · 64.5 · 77.5. Broke from 16:04 ET; one wallet paid about $9.0K at 16:12 ET. **Unmoved:** WTI $110 Nov 19.5 · invade 11.5 · declares war 2.2 · Hormuz normal 12/31 9.5 · oil futures to their close (Yahoo last, not settlements). **Reports (card 047, relayed):** two projectiles at Susa, Qeshm, aircraft heard, authorities silent (IRNA 21:55Z); two missiles, initial, unconfirmed (Tasnim, Reuters via JPost 22:19Z); possibly warning shots (Fars). ⚠️ Attacker unnamed and direction open; not established as a US strike. ⚠️ **No leg resolved does not mean no strike:** without an established consensus a leg stays open to the third date after its named date (11/18 for 11/15), so these can sit mid-range for days. ⚠️ Near-touch bids were $135–$448 at 22:18Z; not called insider flow. ⚠️ One strike of any size resolves these legs; they say nothing about a sustained campaign. **VX-ORC-07 Alert → Critical under WQ-439 A** (a 48h pair, −27.5 log, −23.5 CLOB, not a gate read); the retrace does not undo it while the pair is in the window. → FALCON (grade), HAWK, BRENT, WALTER, PROME · KB-ORC-128, KB-ORC-129 · `research/2026-11-06_ceasefire-break.md`

**2. 🟠 DECEMBER HIKE ODDS STILL ABOUT 77 TO 78; NO GATE CLEARED.** PM HIKE-at-Dec **76.5** at 22:15Z (vol $5.0M, liq $359.7K); 11/06 read 77.5 (liq $322.7K). Kalshi ≥1 more by Dec **78.0** (OI 92.4K). Futures equal about 76 (`ZQZ26` 95.985) to 80 (`ZQF27` 95.92) on Yahoo last trades 21:5xZ, EFFR 3.88 [11/05]; not settlements. No gap worth flagging. ⚠️ About 6 of the 14-point rebound came BEFORE payrolls, cause not established; the 11/05 fall (−14 to −17 by basis) also has no established cause. VX-ORC-12 Alert HELD; lowest read 69.5; next read Mon 11/09. → HENRY, LIQUID, BOND, PROME · KB-ORC-125, KB-ORC-126

**3. 🟠 THE CROWD PRICES FAR MORE STRIKES THAN OIL RISK.** Implied another US strike by 11/30 about 64.5 (23:34Z) against WTI $110 Nov **19.5** (11/06 read 19.0; vol $65.2K, liq $36.5K). Invade 11.5 (vol $78.3M) · regime fall 2.9. Blockade-end 3/31/27 71.5 · next senior meeting 12/31 41.5. ⚠️ Separate contracts with different rules; they do not show what traders expect oil to do if a strike happens. PM "ceasefire" means no US strike landing on Iran, not a formal truce (KB-ORC-111). → HAWK, BRENT, FALCON · KB-ORC-112, KB-ORC-119

**4. 🟡 NOVEMBER $110 OIL: NO ACTIVE ALERT.** Reads 10/28 52.5 · 52.5 · 64.0 (Alert) · 36.5 · 30.5 · 25.5 (cleared) · 16.0 · **11/06 19.0** (liq $21.4K, run 8; context 22:15Z 19.5). Spread +71.5 (11/06 read), +71.0 (context 22:15Z). ⚠️ The 10/29 read came 7h42m after Polymarket's 18:33Z halt; excluded, no Alert fired. Settles per BRENT, wire reports, no exchange page: WTI Dec $90.83, Brent Jan $98.32. Kalshi Brent > $97.99 at 11/30 44.0 (⚠mid 43.0, OI 6.5K). → BRENT, FALCON, HAWK · VX-ORC-04

**5. 🟡 OCTOBER JOBS GRADED.** Print 4.1% (BLS 11/06). Kalshi `KXU3-26OCT` finalized 4.1%; the crowd's 4.2 mode missed one notch to the stronger-labor side. First logged rows of the roll, 22:15Z: `KXU3-26NOV-T4.1` 48.0 (⚠mid 47.0, OI 2.0K) · `T4.2` 13.0 (⚠mid 6.5, 13¢ book, OI 3.0K). → LABOR, HENRY · KB-ORC-124

**6. 🟡 AI DOWNTURN ODDS ROUND-TRIPPED.** PM AI bubble burst 8.25 (11/05 10:00 ET) → 15.9 → **7.5** (22:15Z, liq $129.6K, vol $2.6M). PM recession 4.5 · Kalshi GDP-rule 4.0 (OI 858.1K, 1¢ book; 3.0 at 20:26Z is book noise) · S&P best asset 87.0 (liq $15.3K). ⚠️ Market text not re-read. → BROCK, VULCAN · KB-ORC-123

**7. 🟠 BANK FAILURE: STILL TOO THIN TO READ.** PM any-bank 12/31 **70.5**, liq $2.2K ⚠️, vol $14.6K. Named top 3.4 ($415 liq ⚠️). Bailout 7.0 ($873 liq ⚠️). Not marked, not routed. → REGINALD (no signal) · KB-ORC-122

**8. 🟡 VENUE RISK.** Polymarket halted 10/29 18:33Z after a third-party compromise; resumption time not established (KB-ORC-121). Utah charged Kalshi and its CEO and COO about 10/28, CFTC contesting, no ruling found; Kalshi lane live (KB-ORC-127).

---

## Signal Dashboard — 2026-11-06T22:15Z (= ET Fri 11/06, context pull after the close)

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ1d | Δ7d | Depth | Note |
|---|---|---|---|---|---|---|
| US bank failure by 12/31 (any) | PM | 70.5 | — | −1.0 | $2.2K liq ⚠️ | not marked |
| Which banks fail EOY (top) | PM | 3.4 | +0.1 | −0.2 | $415 liq ⚠️ | |
| Major bank bailout <2027 | PM | 7.0 | — | — | $873 liq ⚠️ | |
| Fed: HIKE at Dec mtg | PM | **76.5** | +13.0 | +6.0 | $359.7K liq | 11/06 read 77.5 |
| Fed: NO change at Dec mtg | PM | 20.5 | −13.0 | −7.0 | $396.8K liq | |
| Fed ≥1 more hike by Dec (`>4.00`) | Kalshi | 78.0 | +11.0 | — | OI 92.4K | 1¢ book |
| Fed 2 more by Dec (`>4.25`) | Kalshi | 3.0 | +1.0 | — | OI 73.9K | 1¢ book |
| Fed: ANOTHER hike 2026 | PM | 76.5 | +13.0 | +5.0 | $115.8K liq | |
| Fed hike count (top) | PM | 75.5 | +10.0 | +4.0 | $24.0K liq | |
| End-2026 funds rate (top) | PM | 75.5 | +11.1 | +6.8 | $1.9K liq ⚠️ | thin at this pull |
| Fed: NO cuts 2026 | PM | 97.7 | +0.3 | +0.9 | $622.7K liq | |
| US recession 2026 (GDP or NBER) | PM | 4.5 | — | −2.0 | $63.4K liq | ≠ Kalshi definition |
| Recession 2025-26 (GDP rule) | Kalshi | 4.0 | 0.0 | — | OI 858.1K | 1¢ book; 3.0 at 20:26Z |
| US inflation >5% 2026 | PM | 4.5 | −1.5 | −4.0 | $69.7K liq | |
| Oct CPI modal | PM | 86.0 | +5.5 | −3.5 | $3.3K liq ⚠️ | ends 11/11; no Kalshi October YoY event |
| Nov U3 `>4.1%` / `>4.2%` | Kalshi | 48.0 / 13.0 (⚠mid 47.0 / 6.5) | — | — | OI 2.0K / 3.0K | first logged 22:15Z; wide books |
| US credit downgrade 2026 | Kalshi | 4.9 (⚠mid 3.0) | +3.7 | — | OI 33.3K, 4¢ book | not a move; book noise |
| Hormuz traffic normal by 11/30 | PM | 3.5 | −0.1 | −2.0 | $257.8K liq | |
| Hormuz traffic normal by 12/31 | PM | 9.5 | −1.0 | −1.0 | $381.3K liq | PortWatch PRINT |
| Effective ceasefire 11/15 · 11/30 · 12/31 | PM | **31.5 · 27.0 · 16.0** log; **48.0 · 35.5 · 22.5** at 23:34Z | −26.0 · −10.5 · −13.0 | new | $60.6K · $71.3K · $101.1K | broke from 16:04 ET, part retraced; none resolved |
| Blockade-end 3/31/27 (top) | PM | 71.5 | +1.0 | +6.0 | $129.7K liq | |
| China invade Taiwan <2027 | PM | 1.7 | −0.2 | −0.4 | $512.3K liq | |
| China GDP 2026 (top) | PM | 96.2 | +0.1 | −0.1 | $6.9K liq | → ZHAO |
| **WTI $110 Nov (v5 supply leg)** | PM | **19.5** | +3.5 | −39.5 | $36.5K liq / $65.2K vol | 11/06 read 19.0; state none |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ7d | Depth | Note |
|---|---|---|---|---|---|
| US invade Iran <2027 | PM | 11.5 | −6.0 | $78.3M vol | did not follow the ceasefire legs |
| Iranian regime fall <2027 | PM | 2.9 | −2.6 | $29.6M vol | |
| Next US–Iran senior meeting by 12/31 | PM | 41.5 | −4.0 | $74.1K liq | |
| US–Iran deal 2026 (top component) | PM | 13.5 | −0.5 | $58.5K liq | |
| Iran ends enrichment by 12/31 | PM | 7.2 | +1.5 | $67.0K liq | |
| US declares war on Iran | PM | 2.2 | −2.2 | $71.0K liq | |
| Hormuz weekly wk-of-11/2 (top) | PM | 52.0 | +13.5 | $83 liq ⚠️ | roll 11/09 |
| Hormuz avg daily end-Nov (top) | PM | 54.0 | — | $5.8K liq | top leg; not read |
| Hormuz any-day by 11/30 (top) | PM | 24.0 | — | $11.7K liq | top leg; not read |
| Bab el-Mandeb closed (top) | PM | 9.5 | −4.0 | $107.8K liq | |
| Brent >$97.99 / >$95.99 @ 11/30 | Kalshi | 44.0 / 47.0 | — | OI 6.5K / 4.1K | ⚠mid 43.0 / 49.5 |
| OPEC: another exit 2026 | PM | 6.5 | −3.0 | $20.3K liq | → BRENT |
| Venezuela: Delcy out <2027 | PM | 7.5 | — | $23.2K liq | |
| BOJ Dec: hike 25bp | PM | 78.0 | −0.5 | $2.4K liq ⚠️ | d1 −11.5 on a thin book → SAM |
| Russia–Ukraine ceasefire by 12/31 | PM | 14.5 | — | $129.8K liq | |
| Clarity Act signed 2026 | PM | 2.5 | −0.6 | $149.4K liq | → BROCK |
| AI bubble burst 2026 | PM | 7.5 | −2.1 | $129.6K liq | d1 −5.1 → BROCK |
| US debt default <2027 | PM | 1.4 | −0.1 | $6.2K liq | |
| MicroStrategy bankruptcy <2027 | PM | 1.5 | −1.5 | $16.3K liq | |
| 10Y / 30Y Nov ladders | PM | — | — | all <$1.0K liq ⚠️ | not marked |
| Corporate bankruptcies >750 | Kalshi | 69.0 (⚠mid 73.0) | — | OI 6.0K, 8¢ book | |

### Tier 3 — sentiment
| Market | Plat | Now | Δ7d | Note |
|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 88.0 | +8.0 | 13 extreme events, not a complacency gauge (KB-ORC-115) |
| Best asset 2026 (top = S&P) | PM | 87.0 | +6.5 | $15.3K liq |
| FL Cat-4 / Cat-5 by 2027 | PM | 4.0 / 2.6 | −1.5 / −0.1 | ⚠️ $2.2K / $1.3K liq |

**Derived series (`DISRUPTION_SUPPLY_SPREAD.tsv`):** v5 Nov segment +36.0 (10/28) · +36.0 · +25.5 (10/30) · +52.0 · +58.0 · +64.0 · +73.5 (11/05) · **+71.5 (11/06 read)** · +71.0 @ 22:15Z context. Never chart across segments.

---

## Convergence Matrix (2026-11-06T22:15Z)

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| Bank failure | any-bank 70.5 (⚠️ $2.2K liq); named top 3.4 | REGINALD | book too thin to mark | 🟠 thin instrument |
| Fed path | Dec hike PM 76.5 / Kalshi 78.0; futures about 76–80 | LIQUID/HENRY own | no gap worth flagging | 🟠 repriced twice in two days |
| Rates (10Y) | Nov rungs thin; not re-read | BOND/TERRY own | par==DGS10 unconfirmed | 🟡 |
| Inflation | Oct CPI modal at 86.0 ⚠️ thin | HENRY owns the print | no Kalshi October YoY event | 🟡 |
| Recession 2026 | PM 4.5 / Kalshi 4.0 | RED 4–12% (NBER-dated) | structural definitional gap | 🟡 |
| Oil: premium vs shortage | Nov $110 19.5; WTI Dec settle $90.83 (wire, per BRENT) | premium ≠ shortage | spread +71.0 | 🟠 |
| Iran | another US strike 64.5 by 11/30 (60.0 at 20:26Z, about 73 at the low); invade 11.5 | HAWK owns; FALCON grades Qeshm | jumped alone, part retraced, cause not established | 🔴 |
| Tail sentiment | S&P best-asset 87.0; AI bubble 7.5 | — | two days | 🟡 |

---

## Maintenance flags

*Structural detail → `MAINTENANCE.md`; findings → `workbook/KB.tsv` (KB-ORC-118 to 129).*

- ✅ **Kalshi U3 rolled 11/06:** `KXU3-26NOV-T4.1`, `T4.2`, first logged 22:15Z.
- ✅ **Signed Kalshi lane verified on the desktop 11/06:** `status` rc=0 at 22:1xZ.
- ⏳ **Rolls due:** Hormuz weekly → wk-of-11/9 at 11/09 · Hormuz on-date (no November event found) · December $110 when listed.
- ⏳ **Kalshi CPI:** `KXCPIYOY-26OCT` returns 404; open events are `26NOV` (November data, closes 12/10; OI 57.4K on `T3.8`) and `26DEC`. Candidate pin, not pinned.
- ✅ **Hormuz 0-ships closure `⛔` is a false flag:** the row says do not replace (`watchlist.tsv`, diagnosed 8/27). Context column only.
- 🔵 **Coverage due ≤11/11.** Movers ran 22:1xZ: 6 hits, none Iran, none pinned. Russian diesel nomination still awaits BRENT/OSPREY.
- ⚠️ **The routine pulls and never grades.** Owner question sits on WQ-599 (Will, Sat 11/07). Routine unchanged.
- ⚠️ **Two boxes collide:** both crons run; `SCHEDULED_RUNS.md` § Known limits.
- ⚠️ **Kalshi lane is per-box:** laptop = UNSIGNED.
- ⚠️ **Kalshi `pull` has no double-log guard.** It also logs FINALIZED markets' last trades as `yes_prob`; read `[finalized]` / API `result`.
- ⚠️ **Never use `pull --log --force` to log new pins.**
- ⚠️ **`TRADE.md` tables not regenerated;** `TRADE_MARKS.tsv` is current, the rendered tables are as of 11/04.
- ⚠️ `STATUS.md` read-cap: re-check each closeout (`scripts/read_cap_check.py --agent ORACLE`).

## BOTTOM LINE

**The one change since the afternoon: Polymarket's odds of another US strike on Iran by 11/15 jumped from 41% to about 68% after the stock close, then fell back to 52% by 18:34 ET.** Iranian media reported projectiles on Qeshm around that time, with no attacker named, and no one has established a US strike. Oil odds did not move. These legs can stay open for days while attribution is argued, so an unresolved price is not an all-clear.

**December hike odds stayed near 77 to 78%, matching futures.** AI downturn odds stayed at 7.5, $110 oil near 20, recession under 5%, and bank-failure books stayed too thin to read.

---

## Cross-agent tensions

1. 🟠 **ORACLE ↔ LIQUID/HENRY/BOND: Fed repricing, cause open.** Odds fell 14 to 17 points on 11/05 with stocks and rebounded 14 on 11/06, part before the print. Packets sent 11/05 and 11/06.
2. 🔴 **ORACLE ↔ BRENT/HAWK/FALCON: strike odds vs oil odds.** Another US strike 64.5 by 11/30 (23:34Z) against $110 at 19.5; widened after the close, part retraced, cause not established. Packets 11/06 22:2xZ and 23:4xZ.
3. 🟠 **ORACLE ↔ BOND/TERRY: 10Y resolution basis.** The ladder resolves on the Treasury par "10 Yr"; gates key on DGS10. Equivalence unconfirmed since 9/17.
4. 🟠 **ORACLE ↔ RED: recession definitions.** Kalshi GDP-rule 4.0 vs PM GDP-or-NBER 4.5 is structural (KB-ORC-099).

---

## Forward catalysts (dated)

| Date | Event | Instrument | Note |
|---|---|---|---|
| Mon 11/09 | Hormuz weekly rolls · next gate reads | wk-of-11/9 listed | ⚠️ thin |
| Wed 11/11 | October CPI market end | PM modal at 86.0 ($3.3K liq ⚠️) | → HENRY |
| 11/15 | Effective ceasefire (11:59 PM Iran time) | PM 48.0 (23:34Z); stays open to 11/18 if attribution is unsettled | → HAWK, FALCON |
| 2026-11-17T01:00Z | Nov $110 Active-Month switch Dec26→Jan27 (INFERRED) | v5 Nov | R3 reset |
| 11/30 | Effective ceasefire · Hormuz normal · Kalshi Brent month-end | PM 35.5 · 3.5 · `>$97.99` 44.0 | → HAWK, BRENT, FALCON |
| 12/04 | November jobs | Kalshi `KXU3-26NOV` | → LABOR, HENRY |
| Wed 12/09 | FOMC December | PM hike 76.5 / Kalshi 78.0 | → LIQUID, HENRY, BOND |
| 2026-12-15 | Kalshi gap-fill quarterly re-check (WQ-305) | KXCREDEFMAX · KXCCDELINQ · KXCCCHGOFF · KXFEDFACILITY | |
