# ORACLE STATUS

**Live dashboard: prediction-market probabilities, divergences, alerts.**
**FULL REWRITE 2026-11-04 (Wed 20:40–21:xx ET, from `date`) — Will-launched catch-up, laptop `WilliePOwen`, Kalshi UNSIGNED (`status` rc=3, public market data).** Pulls: Polymarket `pull --log` **2026-11-05T01:40Z** (52 rows) + 01:45Z (11 new pins) · Kalshi `pull --log` 01:40Z 11/11 · spread row 01:40Z · `history --write` (HISTORY.tsv 8,904 rows / 52 markets) · `coverage` + `movers` 01:4xZ · Gamma closed-market reads 01:2xZ · spot via `fetch.py` 01:4xZ. **Every row below is this session's read unless stamped otherwise.** The 10/29–11/04 reads came from the scheduled routine and were graded tonight.

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price; re-pull. Every figure carries platform/date/depth. Thin books (<$5K liq) are flagged ⚠️ and never marked on one print. Kalshi depth proxy = open interest. "PM" = Polymarket. The first pull of an ET date is that day's read (letter O3); tonight's 01:40Z is ET 11/04, so it is **context**, and the 11/04 read is the 10:15 ET pull.

---

## 🔴 Alerts (read first)

**1. 🔴 THE PM "CEASEFIRE" MARKETS RESOLVED NO ON 11/03. THEY MEAN "A US STRIKE LANDS ON IRAN", NOT "A TRUCE BROKE".**
PM ceasefire through 11/30 resolved NO (closed 2026-11-03T03:23Z, vol $1.26M); through 12/31 resolved NO (closed 03:07Z, vol $1.24M). Text: NO on a US air or missile strike landing on Iranian territory, with no defensive exemption. CLOB 11/30 leg 36.0 (11/03 00Z) → 6.3 (01Z) → 0.6 (03Z) = Mon 11/2 19:00–22:00 ET. Consistent with the reported Mon 11/2 Qeshm strikes (SIG-W-20261104-002, -019). ⚠️ The market does not name its trigger; UMA's basis unread; FALCON owns FAL-07 and this is not a grade of it. → FALCON, HAWK, BRENT, PROME · KB-ORC-111

**2. 🟠 THE CROWD PRICES MORE STRIKES AND LESS OIL RISK AT THE SAME TIME.**
New PM "effective ceasefire" series (created 2026-11-04T06:07Z, same strike definition, counts only from creation; never difference against the retired legs). No further strike through 11/5 96.0 · 11/6 88.5 · 11/8 81.5 · 11/15 **56.5** · 11/30 **41.5** · 12/31 **30.0** (each leg vol $36K–$77K, liq $20K–$57K). Implied another strike: 43.5 by 11/15, **58.5 by 11/30**, 70.0 by 12/31. Same evening: WTI $110 Nov **13.0** · US invade Iran <2027 10.5 (Gamma d1 −9.0, vol $77.8M) · regime fall 3.5. Blockade-end 11/15 9.5 · 11/30 23.5 · 12/31 43.4 · 3/31/27 71.0 (d1 +8.0). Next senior meeting 11/30 26.0 · 12/31 41.5 (d1 +7.0). ⚠️ Working reading, not a finding: limited strikes rather than a supply shock. These are separate contracts with different rules, participants and liquidity, so they do not show what traders expect oil to do if a strike happens. No deal, reopening or US acceptance is established (SIG-W-20261104-078). HAWK owns the reality. → HAWK, BRENT, FALCON, RED · KB-ORC-112

**3. 🟠 NOVEMBER $110 OIL: VX-ORC-04 ALERT FIRED 10/30 AND CLEARED 11/04; NOBODY WAS TOLD UNTIL TONIGHT.**
Reads (first pull of ET date, all QUALIFIED): 10/28 52.5 · 10/29 52.5 · 10/30 **64.0 = Alert** · 11/02 36.5 · 11/03 30.5 · 11/04 **25.5 = cleared** (liq $5.8K, just above the floor). No Critical: one read ≥60.0. ⚠️ **The 10/29 read came 7h42m after Polymarket's 18:33Z halt; resumption time not established; the quote and volume moved after it; excluding it means no Alert fired.** Evening context 01:40Z 13.0 (vol $34.4K, liq $28.7K). Ladder 01:45Z: $100 33.0 · $105 24.0 · $115 9.5 · $120 8.5 · $130 2.7 · LOW $85 83.0 · LOW $80 52.0. October $110 resolved NO (closed 2026-10-31T03:12Z). Oil: WTI $88.12 / Brent $94.62 CNBC 11/04 settles, contract months unnamed (SIG-W-20261104-078); CLZ26 $87.41, BZ=F $94.02 (`fetch.py`, session unverified) ⇒ $110 ≈ +25.8% above CLZ26. **Spread +76.5pp** (89.5 − 13.0, context) · +64.0 at the 11/04 read. The supply leg moved, the disruption leg did not. → BRENT, FALCON, HAWK · KB-ORC-113 · VX-ORC-04

**4. 🔴 VX-ORC-07 (48h moves) CRITICAL.** WTI $110 Nov 42.0 (11/03 12Z) → 13.0 (11/05 00Z) = −29.0 in 36h, CLOB pair, liq $28.7K. Log pair 30.5 → 13.0 = −17.5 in 31h. Thin-excluded: Hormuz weekly −43.3 ($62 liq), any-day −24.0 ($68 liq). Full CLOB pass NOT run on every market. → PROME (triage)

**5. 🟡 FED: DECEMBER HIKE STILL ABOUT 80%. VX-ORC-12 ALERT HELD SINCE 10/29, MECHANICALLY.**
PM HIKE-at-Dec reads 79.5 · 69.5 · 70.5 · 70.5 · 73.5 · **80.5** (11/04, liq $349.3K); context 77.5 (01:40Z, liq $587.7K, vol $3.2M). Kalshi ≥1 more by Dec **81.0** (OI 92.1K) · two more 3.0 (OI 70.6K). PM no change 21.5. Lowest read 69.5; the de-alert needs two reads <50.0. Business-day calendar named: NYSE trading days (letter §10.2). → LIQUID, HENRY, BOND · VX-ORC-12

**6. ✅ MIDTERMS: BOTH FAVORITES WON.** PM House D resolved YES (closed 2026-11-04T13:06Z, vol $37.4M; last read 94.5) · Senate D resolved YES (closed 10:53Z, vol $17.1M; last read 74.5, entry 67.5). A market resolution, not state certification (SIG-W-20261104-038). → HENRY · KB-ORC-114

**7. 🟠 BANK FAILURE: STILL TOO THIN TO READ.** PM any-bank by 12/31 **70.5** (Δ7d −1.5) on **$2.0K liq / $14.6K vol ⚠️ thin**. Named top 3.4 (⚠️ $354 liq). Bailout 7.0 (⚠️ $768 liq). Not marked, not routed. VX-ORC-01's band now names the any-bank binary as its grading market. → REGINALD (no signal)

**8. 🟡 POLYMARKET PLATFORM RISK.** Trading halted 10/29 18:33Z after a third-party provider compromise; users to be made whole; drained accounts reported, size unknown (SIG-W-20261029-045; CYB-INC-057 OWNER-ASSERTED, CYPHER). Prints resumed by that evening on the CLOB, resumption time not established. Treat PM reads from 10/29 with that caveat.

---

## Signal Dashboard — 2026-11-05T01:40Z (= ET Wed 11/04, context pull)

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ1d | Δ7d | Depth | Note |
|---|---|---|---|---|---|---|
| US bank failure by 12/31 (any) | PM | 70.5 | — | −1.5 | $2.0K liq ⚠️ | not marked |
| Which banks fail EOY (top) | PM | 3.4 | −0.3 | +0.5 | $354 liq ⚠️ | |
| Major bank bailout <2027 | PM | 7.0 | — | — | $768 liq ⚠️ | |
| Fed: HIKE at Dec mtg | PM | **77.5** | +3.0 | — | $587.7K liq | 11/04 read 80.5 |
| Fed: NO change at Dec mtg | PM | 21.5 | −2.0 | +2.0 | $469.0K liq | |
| Fed ≥1 more hike by Dec (`>4.00`) | Kalshi | 81.0 | +6.0 | — | OI 92.1K | |
| Fed 2 more by Dec (`>4.25`) | Kalshi | 3.0 | 0.0 | — | OI 70.6K | |
| Fed: ANOTHER hike 2026 | PM | 77.5 | +2.0 | +1.0 | $109.7K liq | |
| Fed hike count (top) | PM | 77.5 | +5.0 | −2.0 | $35.4K liq | |
| End-2026 funds rate (top) | PM | 76.0 | +4.2 | −2.6 | $9.2K liq | |
| Fed: NO cuts 2026 | PM | 97.8 | +0.9 | +0.9 | $646.6K liq | |
| US recession 2026 (GDP or NBER) | PM | 4.5 | −1.0 | −2.0 | $67.6K liq | ≠ Kalshi definition |
| Recession 2025-26 (GDP rule) | Kalshi | 2.0 | −1.0 | — | OI 857.6K | |
| US inflation >5% 2026 | PM | 6.5 | −0.5 | −1.5 | $41.6K liq | |
| Oct CPI modal 3.7% | PM | 90.0 | +0.5 | — | $6.9K liq | ends 11/11; Kalshi YoY not listed |
| Oct U3 `>4.1%` / `>4.2%` | Kalshi | 68.0 / 27.0 | 0 / −3 | — | OI 47.7K / 6.9K | Fri 11/06 |
| US credit downgrade 2026 | Kalshi | 1.2 (⚠mid 3.4) | −5.7 | — | OI 33.3K, 4¢ book | |
| Hormuz traffic normal by 11/30 | PM | 3.8 | −1.8 | −1.8 | $346.6K liq | pinned 11/04 |
| Hormuz traffic normal by 12/31 | PM | 10.5 | — | — | $350.4K liq | PortWatch PRINT |
| Effective ceasefire 11/15 · 11/30 · 12/31 | PM | 56.5 · 41.5 · 30.0 | new | new | $29.7K · $29.9K · $56.7K | pinned 11/04, new series |
| Blockade-end 3/31/27 (top) | PM | 71.0 | +8.0 | +9.5 | $121.9K liq | 12/31 43.4 |
| China invade Taiwan <2027 | PM | 1.8 | +0.1 | −0.2 | $454.4K liq | |
| China GDP 2026 (top) | PM | 96.2 | +0.1 | −0.1 | $5.6K liq | → ZHAO |
| **WTI $110 Nov (v5 supply leg)** | PM | **13.0** | −20.5 | −38.5 | $28.7K liq / $34.4K vol | 11/04 read 25.5; state none |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ7d | Depth | Note |
|---|---|---|---|---|---|
| US invade Iran <2027 | PM | 10.5 | −8.0 | $77.8M vol | Gamma d1 −9.0 |
| Iranian regime fall <2027 | PM | 3.5 | −0.9 | $29.3M vol | |
| Next US–Iran senior meeting by 12/31 | PM | 41.5 | −0.5 | $74.9K liq | 11/30 26.0 |
| US–Iran deal 2026 (top component) | PM | 15.5 | +4.0 | $43.9K liq | |
| Iran ends enrichment by 12/31 | PM | 8.3 | −0.1 | $70.9K liq | |
| US declares war on Iran | PM | 2.2 | −0.7 | $66.3K liq | |
| Hormuz weekly wk-of-11/2 (top) | PM | 45.0 | +22.5 | $73 liq ⚠️ | rolled 11/04 |
| Hormuz avg daily end-Nov (top) | PM | 33.5 | — | $307 leg liq ⚠️ | rolled 11/04 |
| Hormuz any-day by 11/30 (top) | PM | 38.5 | — | $3.9K vol ⚠️ | rolled 11/04 |
| Bab el-Mandeb closed (top) | PM | 7.5 | −6.0 | $114.4K liq | |
| OPEC: another exit 2026 | PM | 8.0 | −1.0 | $21.4K liq | → BRENT |
| Venezuela: Delcy out <2027 | PM | 6.5 | −1.0 | $19.9K liq | |
| BOJ Dec: hike 25bp | PM | 90.5 | +10.5 | $3.7K liq ⚠️ | → SAM |
| Russia–Ukraine ceasefire by 12/31 | PM | 12.5 | −3.0 | $146.7K liq | |
| Clarity Act signed 2026 | PM | 3.2 | — | $119.8K liq | → BROCK |
| AI bubble burst 2026 | PM | 8.1 | −0.2 | $28.0K liq | → BROCK |
| US debt default <2027 | PM | 1.5 | — | $6.1K liq | |
| MicroStrategy bankruptcy <2027 | PM | 2.5 | −0.2 | $11.1K liq | |
| 10Y Nov ladders / 30Y Nov ladders | PM | — | — | all <$300 liq ⚠️ | not marked; `^TNX` 4.89 11/04 (5.05 on 10/28) |
| Corporate bankruptcies >750 | Kalshi | 69.0 (⚠mid 71.5) | −6.0 | OI 6.0K, 7¢ book | |

### Tier 3 — sentiment
| Market | Plat | Now | Δ7d | Note |
|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 88.5 | +7.0 | text read: 13 extreme events, not a complacency gauge (KB-ORC-115) |
| Best asset 2026 (S&P / BTC / gold) | PM | 84.5 / 10.5 / 2.7 | +10.0 / −2.0 / −2.8 | gold tell not fired; GCZ26 $4,124.10 (session unverified) |
| FL Cat-4 / Cat-5 by 2027 | PM | 4.5 / 2.6 | −0.5 / −0.1 | ⚠️ $1.7K / $1.3K liq |

**Derived series (`DISRUPTION_SUPPLY_SPREAD.tsv`):** v5 Nov segment +36.0 (10/28) · +36.0 · +25.5 (10/30) · +52.0 · +58.0 · +64.0 (11/04 read) · **+76.5 @ 2026-11-05T01:40Z**. Laptop context row +51.0 (11/03T00:15Z). Never chart across segments.

---

## Convergence Matrix (2026-11-05T01:40Z)

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| Bank failure | any-bank 70.5 (⚠️ $2.0K liq); named top 3.4 | REGINALD | book too thin to mark | 🟠 thin instrument |
| Fed path | Dec hike PM 77.5–80.5 / Kalshi 81.0 | LIQUID/HENRY own | venues within ~3.5pp | 🟠 |
| Rates (10Y) | ^TNX 4.89; Nov rungs <$300 liq | BOND/TERRY own | par==DGS10 unconfirmed | 🟡 |
| Inflation | Oct CPI modal 3.7 at 90.0 | HENRY owns the print | Kalshi YoY ladder not listed | 🟡 |
| Recession 2026 | PM 4.5 / Kalshi 2.0 | RED 4–12% (NBER-dated) | structural definitional gap | 🟡 |
| Oil: premium vs shortage | Nov $110 13.0; WTI ~$88 | premium ≠ shortage | spread +76.5, widening on the supply leg | 🟠 |
| Iran | another US strike 58.5 by 11/30; invade 10.5 | HAWK owns | both priced; separate contracts give no conditional read | 🟠 |
| Tail sentiment | NEH 88.5; S&P best-asset 84.5 | — | NEH is a high-bar basket, not a complacency read | 🟡 |

---

## Maintenance flags

*Structural detail → `MAINTENANCE.md` (entry 2026-11-04); findings → `workbook/KB.tsv` (KB-ORC-111 to 115).*

- ✅ **11/04 rolls:** resolved pins retired with records; November successors pinned (full list in MAINTENANCE). `polymarket.py` now prints `✅ PIN RESOLVED` with the outcome.
- ⏳ **Rolls due:** Hormuz on-date (no November event found) · Hormuz 0-ships closure (RESOLVED since 8/01, context column only) · Kalshi Brent date ladder (search uncertified) · Kalshi `KXCPIYOY-26OCT` 0 markets · Hormuz weekly → wk-of-11/9 · December $110 when listed · Kalshi `KXU3-26NOV` after 11/06.
- 🔵 **Coverage + movers run 11/04** (last 10/28): nominated only: **US imports Russian diesel** by 12/31 16.0 (Δ7d −66.5, $130.6K vol), by 11/30 15.5 (Δ7d −60.5, $349.7K vol) → BRENT/OSPREY, not pinned; WALTER flagged the diesel headline as recirculated 10/29 (SIG-W-20261029-052). Next sweep due ≤11/11.
- ⚠️ **The routine pulls and never grades:** an Alert sat unrouted 5 days; a resolution waited 2 days. Grading belongs to a live ORACLE session (`SCHEDULED_RUNS.md` contract 1), and nobody is assigned to launch one daily. CATO delivered the launcher preset 10/29 (c7519854e3); DOCKET L848 still reads PENDING PROME acceptance. A preset does not establish a daily launch. → PROME
- ⚠️ **Two boxes collide:** both crons run; `SCHEDULED_RUNS.md` § Known limits.
- ⚠️ **Kalshi lane is per-box:** laptop = UNSIGNED (`status` rc=3). Signed round-trip unverified since the 10/15 code change.
- ⚠️ **Kalshi `pull` logs FINALIZED markets' last trades as `yes_prob`.** Read `[finalized]` / API `result`.
- ⚠️ **Never use `pull --log --force` to log new pins.** A plain re-pull within 10 minutes logs only them.
- ⚠️ `STATUS.md` read-cap: re-check each closeout (`scripts/read_cap_check.py --agent ORACLE`).

## BOTTOM LINE

**The US struck Iranian soil on Monday, and oil fell anyway.** Polymarket's "ceasefire" markets resolved NO within hours. Their wording means a US strike landing on Iran, not a formal truce ending. Two days later, oil dropped 8–9% on deal hopes.

**The crowd now holds two views at once.** It prices another US strike at 58.5% by November 30, but WTI reaching $110 in November at only 13%. "Limited strikes, not a supply shock" is a plausible reading, not a finding: separate contracts do not show what traders expect oil to do if a strike happens. No deal or reopening is established, and the cause of the oil drop is not established.

**The November oil gate fired and cleared while the desk was dark.** The Alert fired on 10/30 and cleared today. ⚠️ One of its three reads came hours after Polymarket's trading halt; without that read, no Alert fired.
