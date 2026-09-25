# ORACLE STATUS

**Live dashboard — prediction-market probabilities, divergences, alerts.**
**Last pull:** 2026-09-25T01:35–01:48Z (= 2026-09-24 21:35–21:48 ET). Polymarket `pull --log` 51 rows + 4 new-pin rows · Kalshi `pull --log` 13 → 14 tickers after rolls (**authed lane LIVE, rc=0**) · `history --write` 8,155 daily rows · `movers` · `coverage` · `disruption_supply_spread.py` (v5 row 2). **Box:** DESKTOP. Lane state is per-box, never a fleet fact.
**Session:** 2026-09-24 (Thu evening) full update; **late boot 23:38 ET** cleared the KXRECSSNBER-26 rules read (Alert 6 only — other rows unchanged since 01:48Z) at Will's direction — *"We need to update."* First **full** re-tabulation since 9/17 (the 9/24 afternoon session refreshed v5 rows only).

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price — re-pull. Every figure carries platform/date/volume; thin (<$5K liq) is flagged ⚠️ and is never marked on one print.
> **Δ7d** below = Polymarket's own 7-day change (Gamma). **Δ30d** = CLOB daily series (`history`). Kalshi Δ = vs the prior session's price. Depth proxy on Kalshi = **open interest**.

---

## 🔴 Alerts (read first)

**1. 🔴🔴 THE OCTOBER FED HIKE WENT FROM A COIN FLIP TO ~2-IN-3 IN A WEEK, AND BOTH VENUES AGREE.**
PM hike-25 at the 10/28 meeting **66.5%** (Δ7d **+16.0**, Δ30d **+42**; $3.4M vol / $546.6K liq) vs no-change **32.5%**. Kalshi `KXFED-26OCT` differenced: `>4.00` 67.0 − `>4.25` 2.0 ⇒ **hike ≈ 65.0** (OI 33.3K, 1¢ book) ⇒ **cross-venue gap ~1.5pp**.
**December:** Kalshi `>4.25` **50.0%** (OI 24.7K) = **two more hikes by 12/09** · PM end-2026 upper bound ≥4.5% **50.3%**. "Another hike in 2026": PM **90.5%** / Kalshi Dec `>4.00` **90.0%**. Hike-count ladder: 2 hikes **48.5%** (Δ7d −13.0) · **3 hikes 41.9% (Δ7d +23.4)** · 1 hike 8.5%.
⚠️ **Aligned with HENRY's futures read (9/25, KB-ORC-100, supersedes the ~11–12pp in KB-ORC-097):** at **15:00 ET 9/24**, in **expected bp** — futures ZQX26 **+18.0bp** (HENRY) · PM **+16.5bp** · Kalshi **+16.1–16.6bp** ⇒ venues **~1.5–2bp under** (≈6–8pp in P terms), **inside the event basis** (Nov-avg EFFR vs upper bound) — **not quotable as a lag.** P(hike) itself cannot be matched (futures price only an expected change). → `research/2026-09-25_oct-hike-alignment-with-HENRY.md`. The press 73–77.5% figures are secondary, time-unmatched. **Drivers:** 9/16 dots (16/18 see ≥1 more) · 9/23 Barr + flash PMI 58.4 (62-mo high) + 10Y ~5.12% (since 2007) · 9/24 Williams "reasonable". Daily PM path: 37.5 (9/16) → 54.5 (9/19) → 52.5 (9/23) → 64.5 → 66.5. Oct × Dec priced ~independent (not "one and done"). **KB-ORC-097**
⇒ **VX-ORC-08 Alert cell (>66%) is met on Polymarket and ~1pt short on Kalshi** — one print, not a re-grade. Third episodic cross-venue agreement (9/07 0.5pp · 9/17 0.0pp · 9/24 ~1.5pp); **still not a standing-basis claim**. ⚠️ Four different questions (Oct meeting / another hike / count / end-rate) — cite the named contract. → LIQUID, HENRY, BOND, RED, PROME · **KB-ORC-093**

**2. 🔴 THE 10-YEAR CROSSED 5.1% SINCE 9/17; THE CROWD PRICES 5.2% AS NEAR-CERTAIN.**
`how-high-will-10-year-treasury-yield-go-before-2027` ($644.9K): **5.1% rung SETTLED 100.0%** (was 72.5% on 9/17) · **5.2% 91.6%** (Δ1d +14.5, Δ7d +57.1; $136.1K vol but ⚠️ **$4.0K liq**) · 5.3% 76.5% (⚠️ $780 liq) · **5.5% 29.1%** (Δ7d +15.8, $102.3K vol / $5.0K liq) · 5.7% 14.9% · 6.0% 6.9%. Spot proxy `^TNX` **5.16** (FORGE `fetch.py`, 2026-09-24).
30Y: Sept-upside **5.45% SETTLED** (Δ7d +90.6); 5.50% **50.4%** (⚠️ $663 liq); `^TYX` **5.46**. Sept-downside 10Y/30Y ladders are dead weight (2.1% / 2.5%), resolve 9/30.
⚠️ Resolution = Treasury Daily Par Yield Curve "10 Yr". `^TNX` is a proxy — it corroborates, it does not resolve. **Treasury-par == DGS10 still unconfirmed (BOND/TERRY).** The 5.2% rung is 91.6% **on a thin book — do not mark a touch on it.** Curve point: the gate keys on DGS10; the held instrument is TLT (20+yr) — **not the same read.** ⛔ ORACLE owns the crowd read only. → BOND, TERRY, LIQUID, HENRY · **KB-ORC-094**

**3. 🟠 FIRST US–IRAN ROUND OF THE WAR HAPPENED 9/22 — AND HORMUZ SHIP ATTACKS INTENSIFIED THE SAME WEEK.**
**Talks:** 3h session at the UN in New York 2026-09-22 — Araghchi / Witkoff / Kushner, **Qatar PM Al Thani mediating**, Hormuz reopening top of the agenda (Axios, Times of Israel, Israel Hayom 9/22). PM $1.0M attendance event settled Kushner / Witkoff / Araghchi **YES** (Δ7d +68 to +72.5); Al Thani 84.0% (Δ7d +70.5, $94.6K). **★ New pin — next senior meeting:** by 9/30 **29.0%** (⚠️ $4.8K liq) · by 10/31 **45.5%** · by 12/31 **69.0%** ($43.1K event).
⚠️ **Contested form:** Witkoff later said the US side talked **through mediators**, not face-to-face. Polymarket resolved "attend" YES anyway — **never cite the settle as proof of direct talks.**
**Tempo (same week):** "shipping targeted in Hormuz on date" — **9/18 SETTLED YES · 9/21 92.8% · 9/23 98.0%** · 9/24 8.5% · forward 9/25 52.5% · 9/26 59.5% · 9/29 49.0% · 9/30 39.5%. ⚠️ Every leg's book is <$300 — **volume is real ($15–21K on 9/25–9/26), the book is not.** End-Sept 0–5 avg daily transits band **88.5%** (Δ7d +24.5, ⚠️ $1.6K liq). ≥10 ships on any day by 9/30 **15.5%** (Δ7d −40.5).
**But the long-dated leg improved:** Hormuz-normal-by-Dec-31 **22.5%** (Δ7d +5.0, $12.8M / $368.8K liq; was 17.5% on 9/17). ⚠️ Resolves on the **IMF PortWatch PRINT**, not throughput (KB-ORC-079).
**★ Two deep ladders pinned late (invisible to `coverage` until tonight's fix):** US-Iran **ceasefire continues** thru 9/30 **85.5%** (Δ7d +11.0; $830K vol) · 10/31 56.5% · 12/31 41.0% ($2.8M event). **US announces end of blockade** by 9/30 **8.5%** · 10/31 30.5% · 12/31 61.5% ($31.7M event). **9/24: Iran gave the US 5 days (≈9/29)** to accept its road map (≤60-day ceasefire, phased reopening, end of blockade) — the crowd prices it as **leverage, not a trigger** (~91% not met, ~85% ceasefire survives). ⚠️ The ~39pp gap blockade-end-by-Dec (61.5) vs traffic-normal-by-Dec (22.5) is widened by the PortWatch undercount + phased reopening — not a clean spread. **KB-ORC-098**
⇒ **Hypothesis, not a finding:** the crowd reads the near term as *worse* (attacks, transits) and the year-end as *slightly better* (talks). KB-ORC-087's "two decoupled axes" now has a third — diplomacy opening while tempo rises. **HAWK owns the reality.** → HAWK, BRENT, FALCON, PROME · **KB-ORC-095**

**4. 🟠 v5 SUPPLY LEG — SECOND ROW +74.10pp; SEPTEMBER LEG HAS 6 DAYS LEFT.**
`disruption_supply_spread.py` @ 2026-09-25T01:35Z `[v5-wti110-vintage-break]`: disruption **77.5** (100 − 22.5 PortWatch-print basis) − supply WTI-$110-Sept **3.4%** ($837.9K vol, **$85.2K liq**) = **+74.10pp** (row 1: +74.65 @ 9/24T19:07Z). CL=F **$93.34** (CLX26, 2026-09-24); $110 is +17.8% above spot.
⚠️ The September leg drifts to 0 by **expiry**, not repricing — **read v5 as meaningful from the October leg.** **No October WTI $110 market listed yet** → DOCKET L299 **9/28**; if none by the 10/01 close, v5 dies and that gets written down (a new strike is Will's call). Context: 0-ships closure **42.0** is the **Oct-31 leg on $3.5K (thin)** — the deeper Sept-30 leg is **22.5%** ($71.6K). Kalshi `KXIRANCRUDE-26OCT13-T2.0` 51.0 on **OI 0 — no trades, never cite as a probability.** ⛔ Never chart/difference v5 against v4. → BRENT, HAWK, FALCON, TERRY · VX-ORC-04
⚠️ `BZ=F` printed **$105.70** vs WTI $93.34 (a ~$12 spread) with contract **UNKNOWN** in the fetcher — **not verified; BRENT owns the tape.** Kalshi Brent Sep-30: `>$85.99` 92.0 last / 95.5 mid (⚠️ 3¢), `>$91.99` **75.0** (1¢, OI 6.2K).

**5. 🟠 SEPTEMBER CPI — MODAL BAND IS 3.6%.** (prints **2026-10-14**)
Kalshi `KXCPIYOY-26SEP`: `>3.5%` 84.0 last / **82.0 mid** (4¢, OI 34.7K) · **`>3.6%` 46.0%** (1¢, OI 44.5K) · `>3.7%` 13.0 last / **15.0 mid** (4¢). ⇒ (3.5, 3.6] ≈ 36–38%. PM headline modal: **3.6% 46.5%** · 3.7% 31.0% · 3.5% 13.5% (every rung ⚠️ <$5K liq — **cite Kalshi**, PM corroborates). August landed in (3.3, 3.4]. **The "+73pp vs August" figure is still not quotable — clean T-4 re-read due 2026-10-10.** → HENRY, LIQUID, BOND, LABOR · KB-ORC-085

**6. 🟠 RECESSION — THE KALSHI "NBER" CONTRACT HAS NO NBER LEG (rules read 2026-09-25T03:39Z).** `KXRECSSNBER-26` resolves YES on **two consecutive negative BEA GDP quarters in 2025 or 2026** — the ticker says NBER, the rules never do. PM `us-recession-by-end-of-2026` = the **same GDP rule OR an NBER announcement** made by the Q4-2026 advance release ⇒ PM is a near-superset, so **PM ≥ Kalshi is structurally expected**; the gap is the crowd's price on "NBER declares by ~late Jan 2027 without two negative quarters," plus noise. Fresh pair 03:39Z: PM **10.5%** ($2.1M / $75.6K liq) vs Kalshi **5.5 mid** (5/6¢, OI 957.4K; last 7.0 printed above the ask) ⇒ **gap ~5.0pp**. ⚠️ **Neither venue is an NBER-dated read** — RED's object (NBER recession *beginning* in 2026) is matched in kind by neither. My "NBER-only" label (since 6/27) reached RED's KB-RED-096 — correction packet sent. → RED, HENRY, LABOR · **KB-ORC-099** (096 CORRECTED) · VX-ORC-02

---

## Signal Dashboard — 2026-09-25T01:35Z

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ7d | Δ30d | Vol/OI | Note |
|---|---|---|---|---|---|---|
| **Fed: HIKE at Oct mtg** | PM | **66.5%** | **+16.0** | **+42** | $3.4M | 🔴 VX-ORC-08 alert cell met |
| Fed: NO change at Oct mtg | PM | 32.5% | −17.0 | — | $3.5M | |
| Fed Oct `>4.00%` (= hike) | Kalshi | 67.0 | — | — | 33.3K OI | minus `>4.25` 2.0 ⇒ ≈65 |
| **Fed: HIKE at Dec mtg** | PM | **71.5%** | +6.0 | — | $363.2K | |
| Fed Dec `>4.25%` (= 2 more hikes) | Kalshi | **50.0** | — | — | 24.7K OI | ★ new pin |
| Fed: ANOTHER hike 2026 | PM | 90.5% | +7.0 | — | $169.2K | Kalshi Dec `>4.00` 90.0 |
| Fed: hike count (2 / **3**) | PM | 48.5 / **41.9** | −13.0 / **+23.4** | — | $677.0K event | 1 hike 8.5 |
| Fed funds end-2026 (≥4.5% upper) | PM | 50.3% | +22.9 | — | $2.4M | 4.25% bucket 40.9 |
| Fed: NO cuts 2026 | PM | 97.0% | +1.6 | — | $8.5M | |
| **US recession 2026** | PM | **10.5%** | +2.0 | +2 | $2.1M | ⚠️ **DIFFERENT DEFINITION from the Kalshi row** — GDP rule OR NBER; the gap is structural, not a disagreement |
| Recession 2025-26 (2Q neg GDP — **no NBER leg**) | Kalshi | 5.5m | — | — | 957.4K OI | ⚠️ **DIFFERENT DEFINITION from the PM row** — GDP rule only · gap ~5.0pp @03:39Z |
| **10Y hits 5.2% before 2027** | PM | **91.6%** | **+57.1** | — | $136.1K | ⚠️ $4.0K liq · 5.1% SETTLED |
| 10Y hits 5.5% before 2027 | PM | 29.1% | +15.8 | — | $102.3K | |
| Sept CPI `>3.5%` / `>3.6%` / `>3.7%` | Kalshi | 82.0m / **46.0** / 15.0m | — | — | 34.7K / 44.5K / 15.8K OI | ★ rolled from August |
| Sept CPI modal (3.6%) | PM | 46.5% | +1.5 | — | $76.7K event | ⚠️ $3.9K liq |
| Sept U3 `>4.2%` / `>4.3%` | Kalshi | 11.0 / 10.0m | — | — | 15.8K / 6.2K OI | resolves 10/02 |
| US inflation >5% in 2026 | PM | 8.5% | — | — | $333.7K | |
| US unemployment ladder (top) | PM | 5.0% | −4.1 | — | $143.8K | ⚠️ $3.9K liq |
| US credit downgrade 2026 | Kalshi | 7.8 mid | — | — | 33.8K OI | ⚠️ 4¢ |
| Hormuz traffic normal by Dec 31 | PM | **22.5%** | **+5.0** | −17 | $12.8M | ⚠️ PortWatch PRINT |
| Major bank bailout before 2027 | PM | 5.0% | −1.5 | — | $4.2K ⚠️ | |
| US bank failure by Dec 31 | PM | 53.5% | −1.5 | — | $2.9K ⚠️ | thin — NOT marked |
| China GDP 2026 (top) | PM | 90.5% | +1.0 | — | $233.2K | → ZHAO |
| China invade Taiwan <2027 | PM | 3.8% | −0.7 | +0 | $42.8M | |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ7d | Vol | Note |
|---|---|---|---|---|---|
| **WTI $110 (Sep) — v5 supply leg** | PM | **3.4%** | −11.1 | $837.9K | liq $85.2K · ⏳ closes 10/01 |
| Brent `>$91.99` @ Sep30 | Kalshi | 75.0 | — | 6.2K OI | ⏳ 9/30 |
| Brent `>$85.99` @ Sep30 | Kalshi | 95.5 mid | — | 2.4K OI | ⚠️ 3¢ |
| **US–Iran next senior meeting by 12/31** | PM | **69.0%** | — | $43.1K event | ★ new pin · by 9/30 29.0 · by 10/31 45.5 |
| US-Iran deal 2026 (top) | PM | 16.5% | +3.0 | $280.8K | |
| US invade Iran before 2027 | PM | 14.5% | −2.0 | **$68.7M** | deepest on the board |
| Iranian regime fall <2027 | PM | 6.5% | — | $26.3M | |
| US declares war on Iran | PM | 2.5% | −0.1 | $856.1K | |
| Iran ends enrichment by Dec 31 | PM | 11.5% | −1.0 | $1.8M | |
| Hormuz avg transits end-Sep (0–5) | PM | **88.5%** | **+24.5** | $18.0K | ⚠️ $1.6K liq |
| Hormuz ≥10 ships any day by 9/30 | PM | 15.5% | −40.5 | $18.5K | ⚠️ slug says "30", question says "10" — read the question |
| Hormuz weekly (wk 9/21–27), modal 20–24 | PM | 43.0% | — | $4.9K event | ★ rolled · ⚠️ thin |
| Hormuz 0-ships by 9/30 / by 10/31 | PM | 22.5 / 42.0 | +8.5 / +19.5 | $71.6K / $3.5K | Oct leg thin |
| Hormuz shipping targeted (daily) | PM | curve ↑ | — | $74.1K event | see Alert 3 |
| Bab el-Mandeb closed (by-date) | PM | 19.5% | +0.5 | $1.2M | |
| Houthi vs Israel by 9/30 | PM | 1.4% | −1.5 | $60.8K | ⏳ |
| **Saudi action vs Yemen (on-date)** | PM | 9/24 71.0 · 9/28 52.5 · 9/30 29.6 | — | $165.4K event | ★ rolled — by-date **settled YES by 9/15** · ⚠️ books <$600 |
| Venezuela crude ladder (live rung) | PM | 57.5% | +2.0 | $11.1K | ⚠️ thin · BRENT: context only |
| OPEC: another exit 2026 | PM | 17.0% | −7.5 | $186.1K | → BRENT |
| Venezuela: Delcy out <2027 | PM | 11.0% | +2.5 | $190.2K | |
| BOJ October: PM top leg / Kalshi HOLD | PM / Kalshi | 83.0 / 83.0 | +4.0 | $45.4K / 3.3K OI | ★ Kalshi rolled · Sept resolved |
| Corporate bankruptcies >750 | Kalshi | 79.0 last | — | 6.0K OI | ⚠️ 93¢ book — no mid |
| Clarity Act signed 2026 | PM | 7.2% | −0.9 | $23.0M | → BROCK |
| AI bubble burst 2026 | PM | 10.4% | +0.7 | $2.4M | → BROCK |
| Russia-Ukraine ceasefire by Dec 31 | PM | 22.5% | +1.0 | $2.7M | |
| MicroStrategy bankruptcy <2027 | PM | 2.2% | −0.9 | $204.6K ⚠️ | |
| US debt default <2027 | PM | 2.1% | −0.5 | $18.3K ⚠️ | |

### Tier 3 — sentiment
| Market | Plat | Now | Δ7d | Δ30d | Note |
|---|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 82.5% | +1.0 | +1 | still flat through a hike, $105 oil, 10Y >5.1% |
| Best asset 2026 (S&P top) | PM | 53.5% | −1.0 | +0 | held ~14pp below August |
| Mamdani freezes NYC rents | PM | 80.7% | −7.2 | — | ⚠️ $1.0K liq |
| FL Cat-4 / Cat-5 by 2027 | PM | 7.5 / 3.4 | +3.0 / +0.8 | −8 / −8 | ⚠️ thin → CORAL/AEOLUS |

**Derived series:** v5 **+74.10pp @ 2026-09-25T01:35Z** · +74.65 @ 9/24T19:07Z · v4 last valid +36.0 @ 9/07 (**not comparable**).
**Entropy-collapse scan (`metrics.py collapse`):** no market ≥ k=3. Scores entropy **drops** only — "clean" ≠ "nothing moved."

---

## Convergence Matrix

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| **Fed path (Oct)** | hike **66.5 PM / ~65 Kalshi** | no desk carries a live Oct number | venues agree ~1.5pp | 🔴 **alert cell met** |
| **Fed path (Dec / count)** | 2 more hikes by Dec **50%** both venues | — | agree | 🟠 |
| **Rates (10Y)** | 5.1% crossed; 5.2% 91.6% (thin) | BOND/TERRY own | par==DGS10 unconfirmed | 🔴 |
| **Inflation (Sept CPI)** | modal 3.6%; `>3.5` 82 mid | HENRY owns the print | — | 🔴 |
| **Recession 2026** | PM 10.5 / Kalshi 5.5m | RED 4–12% (NBER-dated) | ~5.0pp = PM's extra NBER leg (structural); neither venue is NBER-dated | 🟠 |
| **Oil: premium vs shortage** | v5 +74.10pp (Sept leg expiring) | premium ≠ shortage | meaningful from Oct leg | 🟠 |
| **Iran: talks vs tempo** | talks happened, next by Dec 69%; attacks up; Dec-normal +5 | HAWK owns the reality | three axes, not two | 🟠 |
| Bank failure / bailout | bailout 5.0%, any-bank 53.5% (⚠️ thin) | REGINALD | fading | 🟢 |
| Tail complacency | NEH 82.5% (Δ30d +1) | — | NEH resolution text unread | 🟠 standing |

---

## Maintenance flags

*Structural detail → `MAINTENANCE.md`; findings → `workbook/KB.tsv`.*

- ✅ **Rolled this session (9/24 evening):** Polymarket — Aug CPI → **Sept CPI** · Hormuz weekly → **wk-of-9/21** · Saudi by-date → **on-date** (basis change) · BOJ Sept retired. Kalshi — Fed Sept → **Oct `>4.00` + Dec `>4.25`** · Aug CPI ×3 → **Sept `>3.5/>3.6/>3.7`** · BOJ Sept → **Oct**. ★ New pin: **US–Iran next senior meeting**.
- ⏳ **Rolls due next:** Hormuz weekly → wk-of-9/28 (listed, $7.1K) on ~9/28 · WTI $110 Oct (L299, 9/28) · 30Y/10Y Sept ladders, Houthi 9/30, Hormuz Sept ladders, Kalshi Brent Sep-30 all resolve 9/30–10/01 · Saudi on-date ends 9/30.
- 🔧 **Coverage/movers were silently capped at 100 rows** (Gamma truncates `limit`, no error) — **fixed 9/24 late** with offset paging; coverage 5 → 120 hits. **Every past "nothing new" coverage verdict only covered markets >~$959K liquidity.** Next sweep due ~**2026-10-01** — run `--domain` first. MAINTENANCE 2026-09-24 (late).
- ✅ **PROME v5 residue fixed** — `disruption_supply_spread.py` L78/L81/L238 no longer say $100 (L238 now reads `SUPPLY_PREFIX`).
- ⚠️ **Kalshi mid rule:** apply the mid only when `result` is empty AND OI > 0 (settled or untraded books yield a meaningless ~50). KB-ORC-086.
- ⚠️ **`PINNED BUT NOT FOUND` still does not distinguish "resolved" from "bad slug."** Unfixed.
- ⚠️ **Polymarket slug ≠ question on the Hormuz any-day ladder** (slug `will-30-ships…`, question "at least 10") — read the question text.
- ⛔ **Kalshi is not a venue for the oil supply question** (KXIRANCRUDE is context only, OI 0).
- ⚠️ **`STATUS.md` read-cap:** re-check at each closeout (`scripts/read_cap_check.py --agent ORACLE`).

## BOTTOM LINE

**The week after the Fed's first hike since 2023, the crowd priced a second one — soon.** An October hike went from 50% to **66.5%** on Polymarket and **~65%** on Kalshi; two more hikes by December is a **coin flip on both venues**. The 10-year crossed **5.1%** and the crowd puts 5.2% at 91.6%, though that rung trades on a thin book. September CPI is priced at a **3.6%** modal print. These are consistent with each other: the rates complex is still repricing toward a Fed that keeps going.

**Iran got more complicated, not calmer.** The first US–Iran round of the war happened at the UN on 9/22, with Qatar mediating — though the US says it was through mediators, not face-to-face. The crowd gives a second meeting 69% by year-end, and the year-end Hormuz-normal leg ticked up 5pp. At the same time, ships were hit on 9/18, 9/21 and 9/23, and near-term transit markets deteriorated. **Near term worse, year-end slightly better** — that is the crowd's read, and HAWK owns whether it is right.

**What's owed next:** the October WTI $110 re-pin on **9/28** (L299), without which v5 dies at the 10/01 close. The `KXRECSSNBER-26` rules-text read is **done** (9/25 03:39Z): the Kalshi recession contract has no NBER leg, so the cross-venue gap is structural — correction owed to RED, sent.
