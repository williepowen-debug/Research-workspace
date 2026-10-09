# ORACLE STATUS

**Live dashboard: prediction-market probabilities, divergences, alerts.**
**10/9 PARTIAL UPDATE (Fri, PROME-spawned `prome-75` L0 wake, WQ-314 (b) + whole-inbox drain):** pulls 2026-10-09T14:26Z (PM `pull --log` rc=0, Kalshi 14/14 rc=0, spread row +73.0pp). **Re-read and rewritten this session: alert 2 (Fed) and alert 5 (oil) only.** Alerts 0/1/3/4/6 and every table row are the 9/27–9/28 reads and say so — ⚠️ 11 days stale; do not cite. Resolved pins flagged by `pull` (Sept 10Y/30Y, Hormuz Sept ladders, Sept $110) NOT rolled this session. ‖ **9/28 PARTIAL UPDATE (Mon, PROME-spawned L299 roll + inbox drain):** pulls 2026-09-28T13:48Z/13:49Z (PM 52+53 rows, Kalshi 14/14, rc=0). **Re-read and rewritten this session: alert 0, alert 5, the oil rows, the derived series.** Every other alert/table row below is the **9/27 read** and says so. **9/27 basis — Last pull:** 2026-09-27T16:20Z (Sun 12:20 ET). Polymarket `pull --log` 52 rows · Kalshi `pull --log` 14/14 (**authed lane LIVE, rc=0**) · `disruption_supply_spread.py` (v5 row 3). Event drill-ins (Iran ×3, Fed count, CPI, 10Y, 30Y, end-2026 rate, named banks) 16:2x–16:4xZ. **Box:** DESKTOP. Lane state is per-box, never a fleet fact.
**Session:** 2026-09-27 (Sun) boot + pull + **PROME-commissioned bank-failure-markets read** (Nano Banc, `prome-09`) → `analysis/2026-09-27_bank-failure-markets.md`. `history --write`, `movers` and `coverage` were **not** run this session (coverage next due ~10/01).

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price; re-pull. Every figure carries platform/date/volume. Thin books (<$5K liq) are flagged ⚠️ and never marked on one print.
> **Δ7d** = Polymarket's own 7-day change (Gamma). **"was"** = my 2026-09-25T01:35Z pull. Kalshi depth proxy = **open interest**. Oil and 10Y spot are **Fri 9/25 closes** (Sunday).

---

## 🔴 Alerts (read first)

**0. 🟠 9/28 13:48Z MOVERS (one read each, NOT re-graded; → PROME triage per the >10pp/48h rule).** ① **US–Iran next senior meeting:** by 9/30 **66.5** (9/27: 38.0; ⚠️ $4.2K liq) · by **10/31 75.5** (9/27: 50.0; $52.5K vol / $27.1K liq) · by 12/31 84.5 (77.5) — a **>20pp shift on the deeper 10/31 leg in ~45h** (charter route HAWK/BRENT; HAWK owns why). ② **Fed Oct hike:** Kalshi `KXFED-26OCT >4.00` **69.0** (9/27: 63.0; OI 33.6K) vs PM **65.5** (Δ7d +16.0; $3.9M / $391.7K liq) ⇒ VX-ORC-08 Alert (>66%) crossed on Kalshi only, **split venues, one read**. PM Dec-specific hike **79.0** (Δ1d +10.5; $130.4K liq). ③ Ceasefire thru 9/30 96.7 · Hormuz 0-ships ctx 37.0 (+8.5) · BOJ Oct top leg PM 66.5 (−11.5, ⚠️ $1.3K liq) / Kalshi 70.0 (−9) → SAM · FL Cat-4 6.5 (−14.5, ⚠️ $1.0K liq, one print).

**1. 🔴 THE ONLY "NEXT US BANK FAILURE" MARKET RESOLVED YES ON NANO BANC. NOTHING PRICES THE 2026 FAILURE COUNT, ON EITHER VENUE.**
PM `us-bank-failure-by-december-31-2026-20260824` (**lifetime vol $4.1K**, liq ~$0.9K) **resolved YES**, closed 2026-09-26T01:12Z. Nano Banc (Irvine CA, FDIC cert 58590) closed 9/25, the only failure on the FDIC list since the market opened 8/24. **Reactive, not leading:** 50.5–57.5 midpoint noise 12:00–18:25 ET 9/25 (2 trades, $15); first repricing trade **19:08 ET** → 99.5 by 19:15 ET. That precedes Sunwest's release (19:45 ET, per PROME) and American Banker (21:17 ET). **The FDIC/DFPI release time is unverified.** It priced **~55%** vs the 2026 pace **≈94%** / 2024-25 pace ≈51%, so **less than the base rate, on a thin book: not a crowd view.** **No successor listed** as of 16:20Z (Kalshi CERTIFIED 0 over 13,018 events; PM active+closed searched). Only open bank market: PM named-bank EOY event ($76.1K; KeyBank 4.4% ⚠️$560 liq, US Bank 4.3%, rest 0.9–3.2%), **no move outside noise.** ⛔ Self-correction: the 7/02, 7/22, 8/27 watchlist "delisted/relisted" notes were **resolutions**; the family resolved YES at every failure since April (5/1, 7/10, 8/21, 9/25). → PROME (delivered, consumed) · **KB-ORC-101**

**2. 🟠 OCTOBER FED HIKE PRICED OUT ON BOTH VENUES (10/9 14:26Z); THE HIKE MOVED TO DECEMBER.**
PM hike-25 at 10/28 **15.5%** (9/28: 65.5; $7.1M vol / $615.6K liq) · no-change **84.5%** ($325.4K liq) · Kalshi `KXFED-26OCT >4.00` **18.0** (9/28: 69.0; OI 61.3K, 1¢) · `>4.25` **1.0** (OI 34.7K) ⇒ venues within 2.5pp; **VX-ORC-08 Alert cell (>66%) no longer crossed anywhere.** Dec: PM Dec-meeting hike **74.5** ($141.0K liq) · Kalshi `KXFED-26DEC >4.00` **82.0 last / 86.5 mid** (cumulative), `>4.25` 19.0 / 17.5 mid. Another hike 2026 PM 77.5. ⚠️ One read after an 11-day dark gap — the move is not dated inside it. → LIQUID (packet 10/9, answers its 9/29 ask late), HENRY, BOND · KB-ORC-103

**3. 🟠 SEPTEMBER CPI (prints 10/14): THE CROWD COOLED A NOTCH.**
Kalshi `KXCPIYOY-26SEP`: `>3.5%` **78.0** (was 82.0 mid) · `>3.6%` **35.0 last / 36.5 mid** (was 46.0; OI 47.3K) · `>3.7%` 12.0 / 13.5 mid ⇒ P(3.6%) ≈ **41.5** · P(≥3.7%) ≈ 36.5 · P(≤3.5%) ≈ 22. PM modal **3.6% 47.0** · 3.7% 30.5 · 3.5% 11.5 (every rung ⚠️ <$5K liq; **cite Kalshi**). "+73pp vs August" still not quotable (T-4 re-read 10/10). → HENRY, LIQUID, BOND, LABOR · KB-ORC-085

**4. 🟠 IRAN: THE ~9/29 DEADLINE IS PRICED AS LEVERAGE, AND TALKS ODDS ROSE.**
Ceasefire holds thru 9/30 **94.5%** (was 85.5; $1.8M vol / $147.5K liq) · 10/31 55.5 · 11/30 38.5 · 12/31 34.5. US announces end of blockade by 9/30 **4.2** (was 8.5) · 10/15 16.5 · 10/31 29.5 · 11/30 45.5 · **12/31 59.1** ($2.5M) · 3/31/27 74.0 ($32.6M event). Next senior meeting by 9/30 **38.0** (was 29.0) · 10/31 **50.0** (45.5) · 12/31 **77.5** (69.0) (⚠️ $15–40K books; ⚠️ the 9/30 leg's slug says "march-31-2027", so read the question). Hormuz-normal-by-Dec **20.5%** (was 22.5; $13.3M / $451.6K liq; ⚠️ resolves on the IMF PortWatch PRINT, KB-ORC-079). US invade Iran <2027 15.5 ($69.8M). Daily tempo legs for 9/27 (Hormuz targeted 62.5, Saudi-vs-Yemen 86.5) are on **$117–$129 books**, not marked. **HAWK owns the reality.** → HAWK, BRENT, FALCON · KB-ORC-095/098

**5. 🟠 OIL v5 OCTOBER LEG: 8.5% ON A NOW-DEEP BOOK; WQ-314 (b) RULES DELIVERED, NOT ENCODED.**
Oct $110 (id 4936102) **8.5%** (bid 8/ask 9) @ 2026-10-09T14:26Z · vol **$74.8K** · liq **$41.0K** = first **qualified** October read (9/28 25.5% on $3.3K was thin). Path (CLOB 6h bars, context only): 38.0 9/28 00Z → 12.5 10/3–10/5 → 4.5–9.5 10/6–10/9. Ladder $100 34.0 · $110 8.5 · $120 3.9 ($1.4M event). Spot CLX26 **$91.27** / CLZ26 $90.38 (fetch.py, delayed) ⇒ $110 +20.5%. Spread **+73.0pp** (81.5 − 8.5), segment `v5-oct26-icewti110`. Stays v5, ICE venue disclosed (WQ-314 (a) RULED 9/28). **Active Month Nov26→Dec26 at 8:00 PM EDT Wed 10/14 = 2026-10-15T00:00Z** (ICE LTDs re-VERIFIED 10/9: Nov26 10/19 · Dec26 11/19 · Jan27 12/18); step now **$0.89** (was $3.95). **WQ-314 (b):** observation + reset rules in `analysis/2026-10-09_wq314b-v5-observation-and-reset-rules.md` (levels unchanged: Alert ≥40.0 / Critical ≥60.0 or YES on an armed run of 3 qualified business-day reads). November leg expected ~10/25 (INFERRED). ⚠️ Touch odds = price event, not lost supply. → BRENT, HAWK, FALCON, TERRY · VX-ORC-04 · KB-ORC-102

**6. 🟡 RATES AND RECESSION: SMALL DRIFT, NOTHING NEW.**
10Y before 2027: **5.2% 88.7** (was 91.6; ⚠️ $3.9K liq, **do not mark a touch**); 5.1% settled. `^TNX` **5.18** (Fri close; proxy, resolves on the Treasury par curve; par==DGS10 unconfirmed, BOND/TERRY). 30Y Sept 5.50% **61.2** (Δ1d +20.0, ⚠️ $1.1K liq) · 5.55% 38.6 (⚠️ $239). Recession: PM **8.5** (was 10.5; $2.2M / $112.5K liq) vs Kalshi `KXRECSSNBER-26` **5.0** (OI 957.9K). **Different definitions; the gap is structural** (KB-ORC-099).

---

## Signal Dashboard — 2026-09-27T16:20Z

### Tier 1 — direct thesis relevance
| Market | Plat | Now | was 9/25 | Δ7d | Vol/OI | Note |
|---|---|---|---|---|---|---|
| **US bank failure by Dec 31 (any bank)** | PM | **RESOLVED YES** | 53.5 | — | $4.1K life | Nano Banc 9/25 · pin retired · no successor |
| Named-bank EOY (top: KeyBank) | PM | 4.4 | 3.4 (**different top leg**, $539 vol) | +1.8 | $76.1K event | ⚠️ $560 liq · noise · not a like-for-like Δ |
| Major bank bailout before 2027 | PM | 5.0 | 5.0 | −1.5 | $4.2K | ⚠️ $788 liq |
| **Fed: HIKE at Oct mtg** | PM | **64.5** | 66.5 | +9.0 | $3.7M | alert cell NOT confirmed |
| Fed Oct `>4.00%` | Kalshi | 63.0 | 67.0 | — | 33.4K OI | |
| Fed: HIKE at Dec mtg | PM | 67.5 | 71.5 | — | $367.0K | |
| Fed Dec `>4.25%` (= 2 more hikes) | Kalshi | 48.0 | 50.0 | — | 24.6K OI | |
| Fed: ANOTHER hike 2026 | PM | 90.5 | 90.5 | +4.0 | $180.9K | |
| Fed hike count (2 / 3) | PM | 53.0 / 39.1 | 48.5 / 41.9 | −8.5 / +15.3 | $692.5K event | 1 hike 8.5 |
| End-2026 upper 4.25% / ≥4.5% | PM | 47.3 / 41.8 | 40.9 / 50.3 | −13.7 / +12.6 | $6.9M event | ⚠️ thin books |
| Fed: NO cuts 2026 | PM | 97.5 | 97.0 | +1.8 | $8.6M | |
| US recession 2026 (GDP rule OR NBER) | PM | 8.5 | 10.5 | — | $2.2M | ⚠️ different definition from Kalshi |
| Recession 2025-26 (GDP rule only) | Kalshi | 5.0 | 5.5m | — | 957.9K OI | |
| 10Y hits 5.2% before 2027 | PM | 88.7 | 91.6 | +44.4 | $138.9K | ⚠️ $3.9K liq |
| Sept CPI `>3.5` / `>3.6` / `>3.7` | Kalshi | 78.0 / 36.5m / 13.5m | 82.0m / 46.0 / 15.0m | — | 37.4K / 47.3K / 17.1K OI | |
| Sept CPI modal 3.6% | PM | 47.0 | 46.5 | +3.5 | $78.0K event | ⚠️ $2.9K liq |
| Sept U3 `>4.2%` / `>4.3%` | Kalshi | 7.0 / 2.0 | 11.0 / 10.0m | — | 21.5K / 6.4K OI | resolves 10/02 |
| US credit downgrade 2026 | Kalshi | 12.0 | 7.8m | — | 34.2K OI | ⚠️ 3¢ |
| US inflation >5% in 2026 | PM | 8.5 | 8.5 | — | $333.8K | |
| Hormuz traffic normal by Dec 31 | PM | 20.5 | 22.5 | +4.0 | $13.3M | ⚠️ PortWatch PRINT |
| **Ceasefire holds thru 9/30** | PM | **94.5** | 85.5 | +18.0 | $1.8M | ⏳ 9/30 |
| Blockade-end by 12/31 | PM | 59.1 | 61.5 | −0.9 | $2.5M | 9/30 leg 4.2 |
| China invade Taiwan <2027 | PM | 3.6 | 3.8 | −0.6 | $42.9M | |
| China GDP 2026 (top) | PM | 91.5 | 90.5 | +1.5 | $234.8K | → ZHAO |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ7d | Vol | Note |
|---|---|---|---|---|---|
| WTI $110 **Oct (v5 supply leg, ICE CLL)** 9/28 | PM | 25.5 | — | $224 vol / $3.3K liq ⚠️ | pinned 9/28 · Active-Month step 10/14 20:00 ET |
| WTI $110 Sept (rolled out; context) 9/28 | PM | 1.4 | −6.1 | $1.0M | ⏳ 10/01 03:59Z · decay |
| Brent `>$91.99` / `>$85.99` @Sep30 | Kalshi | 87.0 / 92.0 | — | 6.2K / 2.4K OI | ⏳ 9/30 · wide books |
| Next US–Iran senior meeting by 12/31 | PM | 77.5 | — | $15.1K | 10/31 50.0 · 9/30 38.0 |
| US invade Iran <2027 | PM | 15.5 | −1.5 | $69.8M | deepest on the board |
| US–Iran deal 2026 (top) | PM | 15.5 | +3.0 | $195.7K | |
| Iranian regime fall <2027 | PM | 6.5 | — | $26.4M | |
| Iran ends enrichment by Dec 31 | PM | 10.0 | −2.5 | $1.8M | |
| US declares war on Iran | PM | 2.6 | −0.1 | $856.6K | |
| Hormuz avg transits end-Sep (0–5) | PM | 86.5 | +22.0 | $20.5K | ⏳ 10/01 |
| Hormuz ≥10 ships any day by 9/30 | PM | 13.5 | −21.0 | $19.3K | slug says 30, question says 10 |
| Hormuz weekly wk-of-9/28 (modal 20–24) | PM | 36.5 | — | $18.6K event | ★ rolled 9/27 |
| Hormuz 0-ships by-date (top) | PM | 28.5 | +7.0 | $3.9K | ⚠️ thin |
| Bab el-Mandeb closed (by-date) | PM | 18.5 | −3.0 | $1.2M | |
| Houthi vs Israel by 9/30 | PM | 1.1 | −6.2 | $60.9K | ⏳ |
| Venezuela crude ladder (live rung) | PM | 69.0 | +13.5 | $11.1K | ⚠️ $788 liq |
| OPEC: another exit 2026 | PM | 16.5 | +3.5 | $186.2K | → BRENT |
| Venezuela: Delcy out <2027 | PM | 9.0 | — | $190.2K | |
| BOJ Oct (PM top / Kalshi hold) | PM / Kalshi | 77.5 / 79.0 | −5.5 | $48.0K / 3.8K OI | → SAM |
| Corporate bankruptcies >750 | Kalshi | 79.0 last | — | 6.0K OI | ⚠️ 10¢ book |
| Clarity Act signed 2026 | PM | 6.6 | +0.1 | $23.1M | → BROCK |
| AI bubble burst 2026 | PM | 10.3 | −1.1 | $2.4M | → BROCK |
| Russia–Ukraine ceasefire by Dec 31 | PM | 21.5 | +1.0 | $2.7M | |
| MicroStrategy bankruptcy <2027 | PM | 2.2 | −0.7 | $204.7K | ⚠️ |
| US debt default <2027 | PM | 1.9 | −0.2 | $18.3K | ⚠️ |

### Tier 3 — sentiment
| Market | Plat | Now | Δ7d | Note |
|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 82.5 | +0.5 | flat; resolution text unread |
| Best asset 2026 (S&P top) | PM | 56.5 | +2.0 | |
| Mamdani freezes NYC rents | PM | 85.8 | −0.8 | ⚠️ $9.0K liq |
| FL Cat-4 / Cat-5 by 2027 | PM | 24.0 / 3.0 | +15.5 / −0.5 | ⚠️ Cat-4 **$961 liq**; Δ1d +17.5 is one print. **No Atlantic system threatens FL** (NHC 2026-09-27T15:00Z: TD Fay 29.3N 43.8W moving SSE). Not marked → CORAL/AEOLUS |

**Derived series:** v5 **Oct segment +51.0pp @ 2026-09-28T13:49Z** (⚠️ thin supply leg) ‖ v5 Sept segment: +75.1 @ 9/28T13:48Z · +78.2pp @ 2026-09-27T16:20Z (Sept leg decaying) · +74.10 @ 9/25T01:35Z · +74.65 @ 9/24T19:07Z · v4 last valid +36.0 @ 9/07 (**not comparable**).

---

## Convergence Matrix

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| **Bank failure** | any-bank market resolved YES (Nano); **no count/next-failure market open** | REGINALD (Nano forensics today) | crowd priced below the 2026 base rate on a $4.1K book | 🟠 **blind spot: no instrument** |
| Fed path (Oct) | hike 64.5 PM / 63.0 Kalshi | no desk carries a live Oct number | venues agree | 🟠 (alert cell not confirmed) |
| Fed path (Dec / count) | 2 more by Dec ~48% | — | agree | 🟠 |
| Rates (10Y) | 5.2% 88.7 (thin) | BOND/TERRY own | par==DGS10 unconfirmed | 🟠 |
| Inflation (Sept CPI) | modal 3.6%; `>3.6` down to 36.5 | HENRY owns the print | — | 🟠 |
| Recession 2026 | PM 8.5 / Kalshi 5.0 | RED 4–12% (NBER-dated) | structural definitional gap | 🟡 |
| Oil: premium vs shortage | v5 Oct segment +51.0 (9/28, thin) | premium ≠ shortage | Oct leg thin; ≥3 reads before any mark | 🟠 |
| Iran: talks vs tempo | deadline priced as leverage; talks up; Dec-normal 20.5 | HAWK owns the reality | three axes | 🟠 |
| Tail complacency | NEH 82.5 | — | resolution text unread | 🟠 standing |

---

## Maintenance flags

*Structural detail → `MAINTENANCE.md`; findings → `workbook/KB.tsv`.*

- ✅ **9/27:** any-bank Dec-31 pin **retired** (resolved YES), watchlist history notes corrected · Hormuz weekly → **wk-of-9/28**.
- ⏳ **Rolls due:** ✅ WTI $110 Oct pinned + REGIME segment (9/28) · re-search a relisted any-bank successor **every pull** (past relist gaps 58d / 10d / 3d) · 9/30–10/01 resolutions: 10Y/30Y Sept ladders, Houthi, Hormuz Sept ladders, ceasefire-9/30 leg, Saudi on-date, Kalshi Brent Sep-30, Sept U3 (10/02).
- ⚠️ **`PINNED BUT NOT FOUND` cannot tell resolved from a bad slug** (unfixed). **Query `closed=true` before calling a pin delisted**: the bank-failure family proved every not-found was a resolution.
- ⚠️ **Kalshi mid rule:** mid only when `result` is empty AND OI > 0 (KB-ORC-086).
- ⚠️ **Polymarket slug ≠ question** on the Hormuz any-day ladder and on the US–Iran-meeting 9/30 leg; read the question text.
- ⛔ **Kalshi is not a venue for the oil supply question, or for bank failures** (0 markets, certified 9/27).
- ⚠️ `STATUS.md` read-cap: re-check each closeout (`scripts/read_cap_check.py --agent ORACLE`).

## BOTTOM LINE

**A US bank failed and the prediction markets had nothing to say about it in advance.** Polymarket's only "any US bank fails by year-end" contract paid out on Nano Banc Friday night. It moved at 19:08 ET on the release, not before, and it had priced a failure at about a coin flip despite six failures this year. It traded $4.1K in total, so this is a thin market's miss, not the crowd's. **No market on either venue now prices another failure or the 2026 count.**

**Elsewhere the crowd eased a notch since Thursday.** An October hike is ~64% on both venues, just under the alert line; September CPI expectations softened (3.7%+ down from 46% to ~37%). On Iran, the crowd prices the ~9/29 deadline as leverage (ceasefire through 9/30 at 94.5%) and gave talks better odds. **9/28:** the oil gauge rolled to October's $110 leg (+51.0pp, thin book, resolves on ICE WTI not CME — Will's call whether that venue change matters; ORACLE says it doesn't). US–Iran talks odds jumped again (meeting by 10/31: 50 → 75.5).
