# ORACLE STATUS

**Live dashboard: prediction-market probabilities, divergences, alerts.**
**FULL REWRITE 2026-10-28 (Wed 20:4x–21:xx ET, from `date`) — Will-launched catch-up session, laptop `WilliePOwen`, Kalshi UNSIGNED (`status` rc=3, public market data).** Pulls: Polymarket `pull --log` **2026-10-29T00:44Z** (51 rows) + 00:46Z (Nov $110 pin) + 00:48Z (5 new pins) · Kalshi `pull --log` 00:44Z 11/11 · spread rows 00:44Z (+84.9, Oct segment) and 00:46Z (+36.0, Nov segment) · `history --write` (HISTORY.tsv 8,784 rows / 56 markets, was the 9/27 file) · `coverage` + `movers` 00:5xZ · event drill-ins 00:5xZ · spot via `fetch.py` 00:4x–00:5xZ. **Every row below is this session's read unless stamped otherwise.** ORACLE was dark 10/22–10/27 (no pulls).

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price; re-pull. Every figure carries platform/date/depth. Thin books (<$5K liq) are flagged ⚠️ and never marked on one print. Kalshi depth proxy = open interest. "PM" = Polymarket.

---

## 🔴 Alerts (read first)

**1. 🟠 OIL: THE NOVEMBER $110 LEG OPENED AT 52.5% — BUT ON ONLY $3.4K OF TRADING. ALERT CAN FIRE AT THE 10/30 READ.**
November pinned 00:46Z (market id 6172751, listed 2026-10-25T04:01Z; resolution text identical to October's except the month ⇒ REGIME `v5-nov26-icewti110`, letter §9.4). **Entry read 52.5%** (bid 52 / ask 53) · liq $28.6K = QUALIFIED under the letter's liquidity test · **lifetime volume $3.4K** (fetcher volume floor flags it thin: the price is quoted more than traded). CLOB since listing: 50.0 → 60.0 (10/26 18Z) → 38.0 (10/27 06Z) → 52.5 = round-trip. November ladder: $120 14.5 · $130 3.6 ($84.7K event). **October exits at 3.6%** (liq $46.6K, vol $334.6K; 2 sessions left) — the last October arming read, run 1 after the R2 gap restart, state none. Spot proxy CME CLZ26 **$102.04** (last trade 20:35 ET 10/28, evening session, not a settle) ⇒ $110 is +7.8%. Brent proxy $110.78 (contract unconfirmed). Kalshi Brent @Oct-30 `>$98.99` 98.0 / `>$100.99` 95.0 (wide books). **Spread +36.0pp** (88.5 − 52.5) on the Nov segment — first row, never compare to the Oct segment's +84.9. **ALERT PATH:** Nov reads 10/29 and 10/30 each ≥40.0 and qualified ⇒ VX-ORC-04 Alert fires at the 10/30 read. DOCKET L729's daily cadence ends 10/30; November reads after that need a PROME cadence decision. → BRENT, FALCON, HAWK · KB-ORC-110 · VX-ORC-04

**2. ✅ FED HELD ON 10/28; THE CROWD HAD IT (~95%). DECEMBER IS NOW PRICED ~80% FOR A HIKE.**
PM "no change after October meeting" **resolved YES**, "increase 25 bps" **resolved NO** (both closed 2026-10-28T20:01:40Z, Gamma `closed=true`). Kalshi `KXFED-26OCT >4.00` finalized 3.0. Hike leg slid 12.5 (10/21) → 5.5 (10/23) → ~4 (10/28 CLOB) into the decision. **VX-ORC-11 retired unfired** (0 reads ≥50.0). Rate stays 3.75–4.00% (9/16 hike, KB-ORC-083). **December:** PM HIKE-at-Dec **79.5** ($1.7M vol / $557.3K liq; Δ1d +3.0) · no-change-at-Dec 17.5 ($536.7K liq) · Kalshi ≥1 more by Dec (`>4.00`) **83.0** (OI 50.0K) / two more (`>4.25`) 4.0. Count ladder: 2 hikes in 2026 **80.0** (Δ7d +11.0, $35.2K liq). No cuts 2026 96.7 ($9.2M). ORACLE did not read the FOMC statement — LIQUID/HENRY own it. → LIQUID, HENRY, BOND · KB-ORC-109 · VX-ORC-11 (retired)

**3. 🟠 IRAN: CEASEFIRE PRICED TO HOLD THROUGH OCTOBER, THEN A CLIFF — MORE LIKELY THAN NOT TO END IN NOVEMBER.**
Ceasefire continues through 10/31 **96.7** · **11/30 39.5** ($981.1K vol / $100.4K liq; CLOB 44.5 on 10/19 → 46.5 on 10/21 → 38.5 on 10/22 → 35.0 on 10/25 → 39.5) · 12/31 27.5 ($838.4K / $96.3K; 33.5 on 10/19). Blockade-end by 10/31 2.8 · 11/30 27.5 · **12/31 40.5** (Δ7d +6.7; $4.3M / $183.1K) · 3/31/27 61.5. Next senior meeting by 11/30 26.5 · **12/31 39.5** (Δ30d −44, from ~80 in late Sept; $262.6K). US invade Iran <2027 18.5 ($75.7M, deepest on the board) · regime fall 5.5 ($28.2M) · declares war 3.0 · Iran ends enrichment 12.5. Hormuz-normal-by-Dec **11.5** ($15.7M / $332.5K; Δ90d −42; ⚠️ resolves on the IMF PortWatch PRINT, KB-ORC-079). Read: the crowd prices November as the risk window, and both "ceasefire ends" and "blockade lifted by year-end" rose — it expects the status quo to break, direction unsettled. Consistent with the Nov $110 leg at 52.5. **HAWK owns the reality.** → HAWK, BRENT, FALCON

**4. 🟠 VX-ORC-07 (48h moves) 🟠 ALERT — PARTIAL GRADE.** No ORACLE log pair ≤48h (prior pull 10/22T02:22Z = 166h). Graded on Gamma d1 for all pins + CLOB on 2 legs. Largest non-thin: **WTI $110 Nov 39.0 → 52.5 in 48h** (+14.5 range; Δ1d +11.0; low-volume round-trip). Thin-excluded d1 moves: 10Y Oct downside −30.5 ($121 liq), 30Y Oct downside −26.5 ($1.1K), Hormuz shipping on-date −16.0 ($125). Full 37-market CLOB pass NOT run. → PROME (triage)

**5. 🟠 BANK FAILURE: THE ANY-BANK MARKET IS STILL TOO THIN TO READ.**
PM any US bank fails by 12/31 **73.0%** (Δ7d +14.5) on **$1.7K liq / $14.5K lifetime vol ⚠️ thin**. Prints: 42.0 (10/15) → 84.5 (10/16) → 58.5 (10/21) → 73.0. Four thin prints over 13 days — not a crowd view, not marked, not routed. Named-bank EOY top 3.4 (⚠️ $215 liq). Bailout <2027 7.0 (⚠️ $696 liq). KB-ORC-101's priced-below-base-rate read stays untested. → REGINALD (no signal) · VX-ORC-01

**6. 🟡 RATES, LABOR, INFLATION, RECESSION.**
`^TNX` **5.05%** (`fetch.py`, 10/28 close, proxy; ladder resolves on the Treasury par curve, par==DGS10 unconfirmed → BOND/TERRY). 10Y/30Y October rungs all ⚠️ <$1.1K liq, resolve 11/1 — not marked; November rungs not yet found. October CPI (prints ~mid-Nov): PM modal **3.7% at 90.0** ($12.8K vol / $8.1K liq; Δ7d +5.5); Kalshi `KXCPIYOY-26OCT` still **0 markets**. October U3 (prints Fri 11/06): Kalshi `>4.1%` 68.0 (⚠mid 69.5, OI 43.3K) / `>4.2%` 31.0 (OI 5.7K). Recession: PM **6.0** ($2.4M / $64.8K liq; Δ90d −4) vs Kalshi GDP-rule **3.0** (OI 922K) — definitions differ (KB-ORC-099). US credit downgrade 2026 Kalshi 5.9. Corporate bankruptcies >750 Kalshi 72.0 (⚠mid 75.0, 8¢ book).

**7. 🟡 TAIL / SENTIMENT.** Nothing Ever Happens 2026 **81.5** ($868.2K; Δ90d +10) · best asset 2026: S&P **74.5** (Δ30d +17) / BTC 12.5 (Δ7d −7.0) / gold 5.5 — the registered tell (gold retaking the lead) has NOT fired. Spot: S&P 7,743.98 (+0.28% 10/28), gold GCZ26 $4,049.60 (evening). AI bubble burst 7.8 · Clarity Act signed 2026 **3.2** ($24.7M; Δ90d −25) · MicroStrategy bankruptcy 6.0 (⚠️ $1.4K liq, Δ1d +3.9) · Russia–Ukraine ceasefire by 12/31 15.5 (Δ90d −19).

---

## Signal Dashboard — 2026-10-29T00:44Z (= ET Wed 10/28)

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ1d | Δ7d | Depth | Note |
|---|---|---|---|---|---|---|
| US bank failure by 12/31 (any) | PM | 73.0 | −2.5 | +14.5 | $1.7K liq ⚠️ | not marked |
| Which banks fail EOY (top) | PM | 3.4 | — | +0.9 | $215 liq ⚠️ | |
| Major bank bailout <2027 | PM | 7.0 | — | — | $696 liq ⚠️ | |
| Fed: HIKE at Dec mtg | PM | **79.5** | +3.0 | +1.0 | $557.3K liq | Dec 9 decision |
| Fed: NO change at Dec mtg | PM | 17.5 | −3.0 | −1.0 | $536.7K liq | pinned 10/28 |
| Fed ≥1 more hike by Dec (`>4.00`) | Kalshi | 83.0 | 0.0 | — | OI 50.0K | |
| Fed 2 more by Dec (`>4.25`) | Kalshi | 4.0 | −5.0 | — | OI 53.5K | |
| Fed: ANOTHER hike 2026 | PM | 79.5 | +2.5 | −1.0 | $232.0K liq | Δ30d −14 (Oct leg dropped out) |
| Fed hike count = 2 | PM | 80.0 | +4.0 | +10.5 | $35.2K liq | 1 hike 18.0 |
| End-2026 upper 4.25% | PM | 78.6 | +7.6 | +12.9 | $2.8K liq ⚠️ | |
| Fed: NO cuts 2026 | PM | 96.7 | +0.7 | −0.3 | $441.7K liq | |
| US recession 2026 (GDP or NBER) | PM | 6.0 | −1.5 | −1.5 | $64.8K liq | ≠ Kalshi definition |
| Recession 2025-26 (GDP rule) | Kalshi | 3.0 | 0.0 | — | OI 922K | |
| US inflation >5% 2026 | PM | 8.0 | — | — | $24.8K liq | |
| Oct CPI modal 3.7% | PM | 90.0 | −2.5 | +5.5 | $8.1K liq | Kalshi not listed |
| Oct U3 `>4.1%` / `>4.2%` | Kalshi | 68.0 / 31.0 | 0 / −2 | — | OI 43.3K / 5.7K | 11/06 |
| US unemployment ladder (top) | PM | 9.2 | +4.6 | +5.1 | $3.5K liq ⚠️ | |
| Hormuz traffic normal by 12/31 | PM | 11.5 | — | — | $332.5K liq | PortWatch PRINT |
| Ceasefire through 11/30 | PM | **39.5** | +2.0 | — | $100.4K liq | pinned 10/28 |
| Ceasefire through 12/31 | PM | 27.5 | +2.0 | −2.5 | $96.3K liq | pinned 10/28 |
| Blockade-end by 12/31 / 3/31/27 | PM | 40.5 / 61.5 | — | +6.7 / +6.5 | $183.1K / $93.6K | |
| China invade Taiwan <2027 | PM | 2.1 | — | −0.1 | $415.9K liq | |
| China GDP 2026 (top) | PM | 96.3 | +0.1 | −0.1 | $12.4K liq | → ZHAO |
| **WTI $110 Nov (v5 supply leg)** | PM | **52.5** | +11.0 | — | $28.6K liq / ⚠️ $3.4K vol | entry read: thin volume, run 1, NOT armed — Alert needs a 3-read run each ≥40.0 |
| WTI $110 Oct (rolled out) | PM | 3.6 | −0.1 | −10.9 | $46.6K liq | ends 11/1 |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ7d | Depth | Note |
|---|---|---|---|---|---|
| US invade Iran <2027 | PM | 18.5 | +2.0 | $75.7M vol | |
| Iranian regime fall <2027 | PM | 5.5 | — | $28.2M vol | |
| Next US–Iran senior meeting by 12/31 | PM | 39.5 | +2.0 | $67.8K liq | 11/30 26.5 |
| US–Iran deal 2026 (top) | PM | 14.5 | — | $43.4K liq | |
| Iran ends enrichment by 12/31 | PM | 12.5 | +3.2 | $77.1K liq | |
| US declares war on Iran | PM | 3.0 | +0.6 | $56.8K liq | |
| Hormuz weekly wk-of-10/26 (modal 20–24) | PM | 39.0 | — | $21.0K liq / $2.4K vol | <20 at 29.0 · rolled 10/28 |
| Hormuz avg daily transits end-Oct (top) | PM | 91.5 | +1.5 | $25.9K liq | ends 11/1 |
| Bab el-Mandeb closed (by-date top) | PM | 13.5 | −2.0 | $104.1K liq | |
| Houthi vs Israel by 10/31 | PM | 1.7 | −4.0 | $23.1K liq | |
| Saudi military action vs Yemen (on-date 10/28) | PM | 99.6 | +36.6 | $1.7K liq ⚠️ | on-date, thin → HAWK owns |
| OPEC: another exit 2026 | PM | 9.0 | +2.0 | $18.0K liq | → BRENT |
| Venezuela: Delcy out <2027 | PM | 7.5 | +1.0 | $21.9K liq | |
| BOJ October (top) / Kalshi | PM / Kalshi | 99.9 / 97.0 | +2.5 | $41.5K / OI 22.8K | 10/30 → SAM |
| BOJ Dec: hike 25bp | PM | 77.0 | +6.0 | $2.7K liq ⚠️ | pinned 10/28 |
| Russia–Ukraine ceasefire by 12/31 | PM | 15.5 | −4.5 | $124.3K liq | |
| Clarity Act signed 2026 | PM | 3.2 | −2.1 | $197.1K liq | → BROCK |
| AI bubble burst 2026 | PM | 7.8 | −1.6 | $31.0K liq | → BROCK |
| US debt default <2027 | PM | 1.4 | −0.2 | $4.6K liq ⚠️ | |
| MicroStrategy bankruptcy <2027 | PM | 6.0 | +3.1 | $1.4K liq ⚠️ | |

### Tier 3 — sentiment
| Market | Plat | Now | Δ7d | Note |
|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 81.5 | −1.5 | resolution text unread |
| Best asset 2026 (S&P / BTC / gold) | PM | 74.5 / 12.5 / 5.5 | +1.0 / −7.0 / +1.0 | gold tell not fired |
| FL Cat-4 / Cat-5 by 2027 | PM | 4.0 / 2.7 | −1.0 / +0.1 | ⚠️ $1.1K liq each |

**Derived series (`DISRUPTION_SUPPLY_SPREAD.tsv`):** v5 **Nov segment +36.0pp @ 2026-10-29T00:46Z** (first row) ‖ v5 Oct segment last **+84.9 @ 00:44Z** · +75.0 @ 10/22T02:22Z · +78.5 @ 10/15 · +51.0 @ 9/28 (thin) ‖ v5 Sept segment +75.1 last. Never chart across segments.

---

## Convergence Matrix (2026-10-29T00:44Z)

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| Bank failure | any-bank 73.0 (⚠️ $1.7K liq); named top 3.4 | REGINALD | book too thin to mark; KB-ORC-101 untested | 🟠 thin instrument |
| Fed path | Oct HELD (resolved); Dec hike PM 79.5 / Kalshi 83.0 | LIQUID/HENRY own | venues within ~3.5pp; meeting-specific vs cumulative contracts | 🟠 |
| Rates (10Y) | ^TNX 5.05; Oct rungs thin | BOND/TERRY own | par==DGS10 unconfirmed | 🟡 |
| Inflation | Oct CPI modal 3.7 at 90.0 | HENRY owns the print | Kalshi Oct ladder not listed | 🟡 |
| Recession 2026 | PM 6.0 / Kalshi 3.0 | RED 4–12% (NBER-dated) | structural definitional gap | 🟡 |
| Oil: premium vs shortage | Nov $110 52.5 (thin volume, run 1, not armed); WTI $102 | premium ≠ shortage | Nov spread +36.0 — narrower mainly because a fresh month has more days to touch | 🟠 |
| Iran | ceasefire 10/31 96.7 → 11/30 39.5; blockade-end 12/31 40.5 | HAWK owns | November priced as the break window | 🟠 |
| Tail complacency | NEH 81.5; S&P best-asset 74.5 | — | NEH resolution text unread | 🟠 standing |

---

## Maintenance flags

*Structural detail → `MAINTENANCE.md` (entry 2026-10-28); findings → `workbook/KB.tsv` (KB-ORC-109/110).*

- ✅ **10/28 rolls:** Nov $110 pinned + REGIME `v5-nov26-icewti110` + Oct relabel (one edit) · Oct FOMC pins retired with resolution records · Fed no-change-at-Dec pinned · Hormuz weekly → wk-of-10/26 · ceasefire 11/30 + 12/31 legs pinned as markets · BOJ Dec hike-25 pinned.
- ⏳ **Rolls due:** BOJ Oct (resolves 10/30 → retire event) · 10Y/30Y Oct rungs + Hormuz any-day + avg transits + Oct $110 (all end 11/1) → November successors not found yet · Houthi by-10/31 · ceasefire-through event top leg (10/29) · Hormuz 0-ships closure pin RESOLVED since 8/01 (context column suppressed) → re-pin a live rung · Kalshi Oct CPI when `KXCPIYOY-26OCT` lists.
- 🔵 **Coverage sweep run 10/28** (last ~9/22): largest untracked theme = **US midterms 11/3** (PM House D 92.5 / $14.7M; Senate D 67.5 / $6.1M; balance-of-power D/D 65.5). Nominated, NOT pinned — relevance is PROME's/HENRY's call. Next sweep due ≤11/4.
- ⚠️ **ORACLE was dark 10/22–10/27** (4 business days unread; R2 restart on the Oct leg; VX-ORC-11 got only one read before retiring).
- ⚠️ **Kalshi lane is per-box:** laptop = UNSIGNED (`status` rc=3). Signed round-trip still unverified since the 10/15 code change — run `kalshi.py status` → rc=0 at the next desktop boot.
- ⚠️ **Kalshi `pull` logs FINALIZED markets' last trades as `yes_prob`.** Read `[finalized]` / API `result` for settled markets.
- ⚠️ **`PINNED BUT NOT FOUND` cannot tell resolved from a bad slug.** Query `closed=true` first (10/28: both not-founds were resolutions).
- ⚠️ **Never use `pull --log --force` to log new pins.** The double-log guard is per slug, so a plain re-pull logs newly pinned markets at once; `--force` re-logs EVERY row by design. Misused once 10/28; the 51 duplicates were removed. Not a tool defect.
- ⚠️ `STATUS.md` read-cap: re-check each closeout (`scripts/read_cap_check.py --agent ORACLE`).

## BOTTOM LINE

**The Fed held today, as the crowd expected (~95%).** The October hike odds had already drained from ~12% to ~4% during the week ORACLE was dark. Money now prices December as the hike meeting at about 80% on both venues.

**The live question has moved to November oil and the Iran ceasefire.** The new November "$110 WTI" market opened at 52.5%, with WTI at about $102. The ceasefire is priced near-certain through October but only 39.5% to last through November 30. ⚠️ Barely $3.4K has traded on the November oil market, so 52.5% is a quote, not a conviction. If it holds ≥40% on the 10/29 and 10/30 reads, the oil Alert fires on 10/30.
