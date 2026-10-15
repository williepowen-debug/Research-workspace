# ORACLE STATUS

**Live dashboard: prediction-market probabilities, divergences, alerts.**
**10/15 RECOVERY UPDATE (Thu, PROME-spawned WQ-436, `prome-73`, Opus, laptop `WilliePOwen`, Kalshi lane UNSIGNED: no creds on this box).** Pulls **2026-10-15T12:39Z** (pre-market): Polymarket `pull --log` 53 rows rc=0 · Kalshi `pull --log` 11/11 rc=0 (**unsigned public read**) · spread row +78.5pp. Event drill-ins 12:42Z (Iran ×3, 10Y, Oct CPI, best-asset, named banks) and spot via `fetch.py` 12:42Z. **Alerts 0–6 below were re-read and rewritten this session. The Signal Dashboard tables are still the 9/27 read: ⚠️ 18 days stale, do not cite.**
**What the crashed session left (and what this one did with it).** Will launched session `0ce3f089` at 23:56 ET 10/14 on this laptop. Its last tool call was 00:03 ET and the machine died at 03:08 ET with nothing committed. On disk it left: (1) a `scripts/kalshi.py` change that reads UNSIGNED when no creds are present instead of dying at import; (2) both watchlists rolled from September to October pins; (3) appended log rows: ODDS_LOG +62 (50 @ 03:56Z + 12 @ 04:02Z), KALSHI_ODDS_LOG +25 (14 @ 03:57Z + 11 @ 04:02Z), spread +1 (+77.0pp @ 03:56Z). It did **not** touch this file. This session checked every residue file whole. Every appended row has its pull stamp and market id, and no row was deleted. September pins were retired with resolution records, not deleted, and each resolution was re-verified at Gamma (`closed=true`) or the Kalshi API. Code: `scripts/test_cred_modes.py` passes 13/13 offline in both modes and kills 4/4 mutants. Live unsigned runs of `status` (rc=3), `market`, `pull` and candlesticks all work. **Signed round-trip UNVERIFIED (desktop-only creds): run `kalshi.py status` → rc=0 at the next desktop boot.** One false residue claim was corrected: `watchlist.tsv` said the `bank failure` watch term had gone to WALTER, but no packet existed. It was sent this session. ⚠️ The 03:57Z Kalshi rows for FINALIZED markets (Sept CPI ×3, Sept U3 ×2, Brent Sep-30 ×2, Iran crude) log last-trade prints, not probabilities. This is the pull's standing behaviour.
**Not run this session:** `history --write`, `coverage`, `movers`. The crashed session ran `movers` and `coverage --domain` (rc=0, output lost with its scratchpad), and its `history --write` never finished: `HISTORY.tsv` is still the 9/27 file. Coverage is still overdue (last completed ~9/22).

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price; re-pull. Every figure carries platform/date/volume. Thin books (<$5K liq) are flagged ⚠️ and never marked on one print.
> All 10/15 figures are **2026-10-15T12:39Z** unless stamped. **"10/9"** = the 2026-10-09T14:26Z pull. Kalshi depth proxy = **open interest**.

---

## 🔴 Alerts (read first)

**0. 🟠 10/15 MOVERS (one read each, NOT re-graded; → PROME triage under the >10pp/48h rule, basis caveat below).** ① **Fed October hike jumped around the September CPI print:** PM hike-25 CLOB path (3h bars) 18.5 (10/14 12:00Z) → **39.5** (15:00Z) → 23.5 (10/15 03:00Z) → 27.5 (12:00Z); Gamma reads **31.5** at 12:39Z ($9.6M vol / $119.5K liq). Attribution to the 08:30 ET print is INFERRED from timing only. Over 48h: **+9pp on the CLOB series** (18.5 @ 10/13 12:00Z → 27.5); Gamma's 31.5 against the same 10/13 print is +13, a mixed basis. ⚠️ **Whether this crosses VX-ORC-07's >10pp/48h line depends on the basis.** No ORACLE command produces a 48h move; that question is DAEDALUS ⑰ item 2, now with Will via PROME. ② **Iran talks odds collapsed across the dark gap:** next senior meeting by 12/31 **37.5** (9/27: 77.5; $179.4K vol / $57.3K liq). The move is undated inside the 9/28→10/15 gap. ③ 10Y-before-2027 5.4% rung 33.0 (Δ7d −41.5, ⚠️ $1.7K liq).

**1. 🟠 A US "ANY BANK FAILS BY DEC 31" MARKET EXISTS AGAIN (relisted 9/28); IT IS THIN.**
PM `us-bank-failure-by-december-31-2026-20260928` (Gamma id 5100024, created 2026-09-28T23:24Z, window = creation → 12/31 11:59 PM ET, FDIC Failed Bank List): **42.0%** (Δ7d −13.5) · **$2.2K lifetime vol / $470 liq ⚠️ thin**, never marked on one print. The relist came ~2.9 days after Nano Banc resolved its predecessor (9/26T01:12Z). Pinned 10/15 by the crashed session; the price was verified live this session. The `bank failure` watch term went to WALTER today (`AGENTS/WALTER/inbox/2026-10-15_from-ORACLE_bank-failure-watch-term.md`). Named-bank EOY ($83.1K event): top **Santander 4.9%** (⚠️ $369 liq), JPM 3.8, Citi 3.4, so no move outside noise. Bailout <2027 6.5 (⚠️ $426 liq). The priced-below-base-rate read (KB-ORC-101) stands untested. → REGINALD · VX-ORC-01

**2. 🟠 FED: THE OCTOBER HIKE IS BACK TO ~30% ON BOTH VENUES (it was ~16% on 10/9); DECEMBER STAYS THE LIVE MEETING.**
October: PM hike-25 **31.5** Gamma / 27.5 CLOB (10/9: 15.5) · no-change 66.0 ($12.3M / $169.4K liq) · Kalshi `KXFED-26OCT >4.00` **29.0** (10/9: 18.0; OI 74.5K, 2¢) ⇒ venues within 2.5pp. December: PM Dec-meeting hike **78.5** ($119.4K liq) · Kalshi `KXFED-26DEC >4.00` **87.0** (cumulative ≥1 more hike by Dec; OI 17.7K, 3¢; pinned 10/15) · `>4.25` **25.0** (OI 25.8K, ⚠️ 5¢). Another hike in 2026: PM 85.5. No cuts 2026: PM 96.9. ⚠️ **ORACLE sent LIQUID 15.5/18.0 on 10/9. Those figures are superseded by this read.** → LIQUID, HENRY, BOND · KB-ORC-103 (10/9 basis)

**3. ✅ SEPTEMBER CPI PRINTED 3.7% YoY, ONE NOTCH ABOVE THE CROWD'S MODE.**
Kalshi `KXCPIYOY-26SEP` finalized with **expiration_value 3.7**: `>3.5` YES · `>3.6` YES · `>3.7` NO (verified at the API 10/15). PM's 3.7% leg resolved 100. At ORACLE's last pre-print read (10/9 14:26Z, last-trade basis) Kalshi had `>3.5` 88 · `>3.6` 39 · `>3.7` 9 ⇒ P(3.6) ≈ 49 · **P(3.7) ≈ 30** · P(≥3.8) ≈ 9, and PM's modal leg was 3.6% at 47.0 (⚠️ $1.9K liq). The print landed on the crowd's second-most-likely outcome; this is a calibration datum, not a shock. October CPI (prints ~mid-Nov): PM modal **3.7% 61.0** ($7.8K event; ⚠️ every rung <$1.3K liq). `KXCPIYOY-26OCT` has **0 markets** (12:4xZ), so cite Kalshi once it lists. → HENRY, LIQUID, BOND, LABOR · KB-ORC-085

**4. 🟠 IRAN: CEASEFIRE PRICED TO HOLD NEAR-TERM; BLOCKADE-END AND TALKS ODDS FELL HARD SINCE 9/27.**
Ceasefire continues through 10/31 **79.5** (Δ7d +10.0; $3.0M vol / $613.2K liq) · 11/15 57.5 · 11/22 49.5. Blockade-end by 10/31 **8.5** ($4.8M) · 11/30 23.5 · **12/31 37.9** (9/27: 59.1; $3.4M / $196.3K liq) · 3/31/27 59.5. Next senior meeting by 10/31 7.5 · 11/30 25.0 · **12/31 37.5** (9/27: 77.5). Hormuz-normal-by-Dec **12.5%** (9/27: 20.5; $14.9M / $786.3K liq; ⚠️ resolves on the IMF PortWatch PRINT, KB-ORC-079). US invade Iran <2027 16.5 ($74.1M). The daily on-date tempo legs (Hormuz targeted 52.5, Saudi-vs-Yemen 58.0) are on **$93–$97 books** and not marked. **HAWK owns the reality.** → HAWK, BRENT, FALCON · KB-ORC-095/098

**5. 🟠 OIL v5: THE OCTOBER $110 LEG SITS AT 9.0%; THE SPREAD IS AT ITS WIDEST, +78.5pp. IRAN'S SEPTEMBER OUTPUT SETTLED BELOW 2.0M bpd.**
Oct $110 (`will-wti-reach-110-in-october-2026`) **9.0%** @ 12:39Z · $103.0K vol / **$39.9K liq** (qualified depth). Ladder (12:4xZ): $100 44.5 · $105 20.5 · $110 9.0 · $120 3.5 ($2.3M event). Spot CLZ26 **$93.66** (`fetch.py`, delayed, 12:42Z) ⇒ $110 is +17.4% away. **Spread +78.5pp** (87.5 − 9.0, `v5-oct26-icewti110`); 03:56Z +77.0 · 10/9 +73.0 · 9/28 +51.0. WIDE means premium, not shortage. **ICE Active Month stepped Nov26→Dec26 at 2026-10-15T00:00Z.** That date comes from the ICE LTDs verified 10/9; the step was not re-observed at the contract today. **WQ-314 (b) is still Will's to rule. Levels are UNSET and not encoded; no run is counted.** **Kalshi `KXIRANCRUDE-26OCT13` (Sept production ≥2.0M bpd) settled NO at 1.957M bpd** (OPEC MOMR secondary sources; settled 2026-10-13T13:33Z; ⚠️ OI 226, thin). August was in (2.0, 2.2]. VX-ORC-04's Critical cell carries the context line "<2.0 mbpd = real loss". That line is not graded here: v5 is UNSET, and this is one thin contract and one month. No successor event is open. Kalshi Brent @Oct-30: `>$98.99` 61.0 (⚠mid 63.5, OI 8.6K) · `>$100.99` 63.0 (⚠mid 54.0, OI 5.2K): wide books, so cite the mids. → BRENT, HAWK, FALCON, TERRY · VX-ORC-04

**6. 🟡 RATES, LABOR, RECESSION: SEPTEMBER LADDERS SETTLED; OCTOBER PINNED.**
September 10Y/30Y ladders closed 9/30 (Gamma `closed=true`, all rungs) → October ladders pinned. Every rung is ⚠️ <$600 liq, so **do not mark a touch**. 10Y before 2027: 5.4% **33.0** (Δ7d −41.5, ⚠️ $1.7K liq) · 5.5% 21.8 ($7.5K liq). `^TNX` **5.08** (`fetch.py` 12:42Z; proxy; resolves on the Treasury par curve; par==DGS10 unconfirmed, BOND/TERRY). Sept U3 printed **4.2%** (Kalshi expiration_value) → October U3 `>4.1%` **67.0** (⚠mid 63.0, OI 42.4K) · `>4.2%` 33.0 (OI 4.9K), prints 11/06. Recession: PM **7.5** ($2.3M / $63.7K liq) vs Kalshi `KXRECSSNBER-26` **4.0** (OI 954.1K). **Different definitions; the gap is structural** (KB-ORC-099). Best asset 2026: S&P 68.5 · BTC 17.0 · **gold 8.5**, so the registered tell (gold retaking the lead) has not fired. NEH 81.5.

---

## Signal Dashboard — 2026-09-27T16:20Z (⚠️ STALE, 18 days old: NOT re-read 10/9 or 10/15; current reads are in the alerts above; do not cite these rows)

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

## Convergence Matrix (10/15 12:39Z)

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| **Bank failure** | any-bank relist **42.0** (⚠️ $2.2K life, $470 liq); named-bank top 4.9 | REGINALD | crowd-vs-base-rate (KB-ORC-101) untested on the new instrument; book too thin to mark | 🟠 thin instrument |
| Fed path (Oct) | hike ~30: PM 31.5 / Kalshi 29.0 | no desk carries a live Oct number | venues agree; repriced on the 3.7% CPI | 🟠 |
| Fed path (Dec) | PM Dec-meeting hike 78.5 · Kalshi ≥1 more by Dec 87.0 · 2 more 25.0 | — | meeting-specific vs cumulative contracts; not a like-for-like gap | 🟠 |
| Rates (10Y) | 5.4% before 2027 33.0 (thin) | BOND/TERRY own | par==DGS10 unconfirmed | 🟡 |
| Inflation | Sept printed **3.7** (crowd mode 3.6, P(3.7) ≈ 30 on 10/9); Oct PM modal 3.7 61.0 (thin) | HENRY owns the print | Kalshi Oct ladder not listed | 🟠 |
| Recession 2026 | PM 7.5 / Kalshi 4.0 | RED 4–12% (NBER-dated) | structural definitional gap | 🟡 |
| Oil: premium vs shortage | v5 spread **+78.5** (Oct $110 9.0, qualified depth) | premium ≠ shortage | Iran Sept crude 1.957M bpd < 2.0 (thin context, not graded) | 🟠 |
| Iran: talks vs tempo | ceasefire thru 10/31 79.5; blockade-end 12/31 37.9; talks by 12/31 37.5 | HAWK owns the reality | talks and blockade-end both fell ~20–40pp since 9/27 | 🟠 |
| Tail complacency | NEH 81.5; best asset S&P 68.5 / gold 8.5 | — | NEH resolution text unread | 🟠 standing |

---

## Maintenance flags

*Structural detail → `MAINTENANCE.md` (entry 2026-10-15); findings → `workbook/KB.tsv` (no new KB rows 10/15: recovery scope).*

- ✅ **10/15 rolls (crash residue, verified):** PM: Sept 10Y/30Y → Oct · Sept CPI → Oct · Hormuz weekly → wk-of-10/12 · avg-transits → end-Oct · any-day → by-10/31 · Hormuz + Saudi on-date → October events · Houthi → by-10/31 · Sept $110 and Mamdani retired with resolution records · **any-bank relist pinned**. Kalshi: Sept CPI/U3 out · Oct U3 `>4.1`/`>4.2` in · Brent → Oct-30 `>$98.99`/`>$100.99` · `KXFED-26DEC-T4.00` added · Iran crude retired (NO, 1.957M).
- ⏳ **Rolls due:** **Hormuz 0-ships closure pin is RESOLVED** (the by-date ladder ended 8/01; its context column is suppressed by the spread tool) → re-pin a live rung · Hormuz weekly wk-of-10/12 resolves 10/19 · **November $110 leg ~10/25–10/31** (one edit: pin + REGIME + relabel + MAINTENANCE; read the resolution text first) · Kalshi Oct CPI when it lists · Iran-crude successor (monthly re-check) · re-search the any-bank family after every FDIC failure.
- ⚠️ **Kalshi lane is per-box:** laptop = UNSIGNED public read (`status` rc=3); desktop = signed (last verified rc=0 on 10/09). Market data is identical either way; the signed round-trip has not been re-verified since the 10/15 code change.
- ⚠️ **Kalshi `pull` logs FINALIZED markets' last trades as `yes_prob`.** Read the `[finalized]` flag or the API `result`, never the logged number, for a settled market.
- ⚠️ **`PINNED BUT NOT FOUND` cannot tell resolved from a bad slug** (unfixed). **Query `closed=true` before calling a pin delisted.**
- ⚠️ **Kalshi mid rule:** mid only when `result` is empty AND OI > 0 (KB-ORC-086).
- ⚠️ **Polymarket slug ≠ question** on several by-date ladders; read the question text.
- ⚠️ `STATUS.md` read-cap: re-check each closeout (`scripts/read_cap_check.py --agent ORACLE`).

## BOTTOM LINE

**The overnight crash cost ORACLE nothing but time.** The session that died at 03:08 ET had already rolled every expired September market to October and pinned a new "any US bank fails by year-end" market. It had also fixed the Kalshi script so a machine without keys can still read public prices. All of that was on disk, uncommitted, and it checked out today. The one exception was a note claiming a message to WALTER that was never written; that message went out this morning.

**What moved while ORACLE was dark: the hot CPI print revived the October hike.** September CPI came in at 3.7%, one tick above the crowd's favourite. The October hike, ~16% a week ago, spiked to ~40% on the print and sits near 30% on both venues this morning. Iran is the other big change since late September. The crowd still expects the ceasefire to hold through October (~80%), but it has marked down both a blockade-end announcement and a next meeting this year to under 40%, from ~60% and ~78%. The oil gauge stays wide (+78.5pp): the crowd prices a risk premium, not lost barrels. The new bank-failure market is too thin to read as a crowd view.
