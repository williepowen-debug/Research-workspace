# ORACLE STATUS

**Live dashboard — prediction-market probabilities, divergences, alerts.**
**Last pull:** 2026-09-18T01:49–01:52Z (Polymarket 43 rows `pull --log` + Kalshi 11 tickers via the **PUBLIC** trade-api + `history --write` 7,469 daily rows + `coverage` + `movers`). **Box:** **LAPTOP** (`WilliePOwen`) — the **authenticated** Kalshi lane is **DOWN here by design** (`~/.config/kalshi` absent; `kalshi.py` dies at import). **Per-box, never a fleet fact.**
**🆕 2026-09-24 (Thu) PROME-spawned DRAIN + ENCODE session (WQ-206; DESKTOP, authed Kalshi lane LIVE rc=0):** Polymarket `pull --log` + Kalshi `pull --log` 13-of-13 @ 2026-09-24T19:07Z. **Only the v5 supply-leg rows below (Alert 2, Tier 2 WTI rows, Derived series) were refreshed; every other figure in this file is still the 9/17–18 read** — the 9/24 prints are in `workbook/ODDS_LOG.tsv` / `KALSHI_ODDS_LOG.tsv`, not transcribed here.
**Session (prior full):** 2026-09-17 (Thu) — **first session since 2026-09-07. THE DESK WAS DARK FOR TEN DAYS AND MISSED BOTH THE 9/11 CPI AND THE 9/16 FOMC.** Catch-up session at Will's direction.

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price — re-pull. Every figure carries platform/date/volume; thin (<$5K liq) is flagged ⚠️ and is never marked on one print.
> ⚠️ **Δ1d IS UNRELIABLE THROUGHOUT THIS SESSION.** The fetcher differences against my last logged print, which for most rows is **ten days old**. **Read Δ7d and Δ30d**, and prefer the `history`-derived Δ30d — it is computed off the CLOB daily series, not off my own gappy log.
> ⚠️ **Kalshi figures below are UNAUTHENTICATED public reads.** Per `PROME/MACHINE_LOCAL.md` row 6 the public trade-api answers without creds and a public-read task is **not** to be stood down on the desktop-only row. Depth proxy = **open interest**.

---

## 🔴 Alerts (read first)

**0. 🔴🔴 COVERAGE GAP CLOSED — a $503.0K ladder on the 10-YEAR TREASURY YIELD has existed all along and this desk never tracked it. The crowd says the 10Y crossed 5.0% THIS WEEK.**
`how-high-will-10-year-treasury-yield-go-before-2027`: the **5.0% rung is SETTLED at 100.0% on Δ7d +60.5** ($139.0K vol) — **that delta is what dates the touch to this week** rather than somewhere in the contract's 14-month window. **Live rungs: 5.1% 72.5% · 5.2% 33.6%** ($89.0K vol, $9.4K liq — deepest live) **· 5.5% 13.4% · 5.7% 7.1% · 6.0% 4.8%.**
**The downside complement is the sharper read:** `how-low-will-10-year-treasury-yield-get-in-september` prices dip-below-4.76% at **9.6%** (Δ7d −6.9), below-4.73% **7.0%** (Δ7d −12.4), **below-4.51% at 2.6%**, below-4.45% **1.9%** — **the entire dip ladder fell on the week.** 30Y corroborates: hit-5.36%-in-Sept settled **100.0%** (Δ7d +45.6).
✅ **Resolution source read VERBATIM before publishing** (the KB-ORC-079 discipline applied *before*, not after): *"Daily Treasury Par Yield Curve Rates … column '10 Yr'"* — **an OFFICIAL daily series, not an intraday proxy.** That distinction decides whether a gate keyed to official closes can consume it at all.
⚠️ **I do NOT assert Treasury-par-curve == FRED DGS10.** Same series family, and I believe they are the same number — **but a GATE must not consume a believed equivalence. BOND/TERRY confirm at the primary.**
⛔ **ORACLE owns the crowd read ONLY — no trade view, no position implication, no gate verdict** (root rule #5; TERRY owns construction; positions are off-repo). **What I assert is a COVERAGE fact:** the deepest public market on this variable was un-tracked by the desk whose job is to track exactly that. **Now pinned** (⚠️ with a DO-NOT-REPLACE banner — it trips the settled-top-leg artifact on its first pull). → BOND, TERRY, LIQUID, HENRY, PROME · **KB-ORC-088**

**1. 🔴🔴 THE FED HIKED 25BP TO 3.75–4.00% ON 2026-09-16 — first increase since 2023, vote 12-0 unanimous — and my standing "coin flip" was a pre-CPI vintage the market resolved against.**
Primary: Kalshi `KXFED-26SEP-T3.75` settled **`result: yes`**, **`expiration_value: "4.00%"`**, OI **637,353 ct**, lifetime vol **1,080,771 ct**, **last trade before close 86.0¢**. Corroborated CNBC / Fox Business / Yahoo 9/16 (Warsh: a "timelier return" to 2%; rationale explicitly names **oil-driven inflation**).
⭐ **PROME's ASK ① is answered, and the answer is that the gap closed by CONVERGENCE, not by a basis.** On 9/07 I had PM hike-25 50.5 / Kalshi differenced 50.0. PROME's 9/14 packet relayed futures **~90%** and Reuters **86-of-101 (85%)** post-CPI. Kalshi's own final settle was **86.0¢**. ⇒ **the venues moved TO the futures.**
⛔ **I claim no lead-lag.** I hold no intraday series across 9/11–9/16 for any venue, so "who moved first" is unsourced and I am not guessing. CME FedWatch remains a JS shell — **do NOT re-attempt `WebFetch` on it**; BOND's three-venue question is unchanged and unadvanced.
⛔ **The honest framing: this is a COVERAGE failure, not a measurement failure.** My figure was correct when written and my own note called the 9/11 CPI "the CPI that arms the FOMC five days later." It then sat as **the fleet's only live Fed read for nine days** while I was dark. → PROME, LIQUID, HENRY, BOND, RED, LABOR · **KB-ORC-083** · VX-ORC-08

**2-v5. 🟠 THE SUPPLY LEG IS BACK UP AS v5 AT THE $110 RUNG — WQ-260, Will-ruled 2026-09-24 14:59 ET ("Approve WQ-282, 254, 261, 260 and 276 with your recs"). A VINTAGE BREAK, NOT A ROLL.**
Re-pinned at the venue by this desk 2026-09-24T19:05Z: `will-wti-reach-110-in-september-2026` (Polymarket id 3866512) **mid 3.85%** (bid 2.7 / ask 5.0), Δ7d −14.6, **vol $837.4K, liq $29.9K** ⇒ passes the $5K thin bar. Spot: CL=F **$94.42** (CLX26, `fetch.py` 2026-09-24) ⇒ $110 is +16.5% above spot, a tail again. **First v5 row: 78.5 − 3.9 = +74.65pp @ 2026-09-24T19:07Z** `[v5-wti110-vintage-break]`.
⛔ **Never chart or difference v5 against v4** (v4 last valid +36.0pp @ 9/07; its $100 leg settled YES). ⚠️ **The September segment has 7 days left and will drift toward 0 by expiry, not by repricing — read v5 as meaningful from the October leg.** ⚠️ **No October WTI market is listed** (4 searches 9/24) → DOCKET L299 re-pins on 9/28; if none lists by the 10/01 close, v5 dies and that gets written down. Active Month = CLX26 for the whole September segment (switch was 9/18, before entry); next switch INFERRED ~10/16. Kalshi context column (WQ-190 ②) now live: `KXIRANCRUDE-26OCT13-T2.0` **51.5% book mid, OI 0 — no trades behind it.** → BRENT, HAWK, FALCON, TERRY

**2. (9/17 record, superseded by 2-v5)** WTI touched $100 then $105 in September; the v4 $100 leg resolved YES and the spread tool hard-exited by design. ⛔ Never compute 82.5 − 100 = −17.5pp as a spread. Full record → **KB-ORC-084**, `MAINTENANCE.md` 2026-09-17, git history of this file.

**3. 🔴 SEPTEMBER CPI IS PRICED FAR HOTTER THAN AUGUST WAS — the `>3.5%` rung is at 83.0 mid where August's was 10.0%.**
**August RESOLVED (printed 9/11):** `KXCPIYOY-26AUG-T3.3` **YES** · `T3.4` **NO** · `T3.5` **NO** ⇒ **August headline CPI YoY landed in (3.3%, 3.4%].**
**September ladder** (prints **2026-10-14**): `>3.3%` **98.5 mid** (OI 6,768) · `>3.4%` **95.0 mid** (OI 15,490) · `>3.5%` **83.0 mid** (bid 80 / ask 86 — ⚠️ 6¢, **cite the mid**, OI 19,679).
⚠️ **The ~+73pp like-for-like jump is NOT clean and I will not quote it as one:** August was read at **T-4 days**, September at **T-27 days**. A longer horizon normally carries *more* uncertainty, which pushes a `>3.5%` rung **down** — so the bias runs **against** the finding and the move is very likely real, but **re-read on 2026-10-10 (T-4) for the honest comparison.** ⚠️ Depth is modest vs August's 95K–162K at settlement; early books thicken. → HENRY, LIQUID, BOND, RED, LABOR · **KB-ORC-085**

**4. 🟠 THE TWO IRAN AXES HAVE DECOUPLED AND POINT OPPOSITE WAYS: chokepoint disruption deepening, Gulf-state escalation draining.**
**Deepening:** Hormuz-normal-by-Dec-31 **17.5%** (Δ30d −18, **Δ90d −69**, $11.8M — deep) · normal-by-Oct-31 **6.5%** · end-Sept **0–5 transits/day band 64.0%** (was 40.5% on 9/07, **+23.5pp**).
**Draining:** Iran-targets-Bahrain **11.5%** (Δ7d −61.0) · Iran-targets-UAE **18.5%** (Δ7d −54.0) · US-declares-war **2.6%** · US-invade-Iran **16.5%** (Δ30d −1 on **$66.7M**) · regime-fall **6.5%** (Δ30d +0). Also drained: SPR-to-280M-by-9/25 **10.2%** (Δ7d −65.5).
⚠️ **INFERENTIAL, not measured** — the instrument that *would* have measured this is dead by resolution (Alert 2), so I am reasoning around a hole in my own toolkit and saying so. ⚠️ **The Hormuz-normal leg resolves on the IMF PortWatch PRINT, not throughput** (KB-ORC-079): a detection failure and a real stoppage resolve identically, so "deepening" may partly be "PortWatch still not printing ≥60." **That caveat cuts against my own headline and is not optional when this is quoted.** ⚠️ Bahrain/UAE are thin ($1.2K / $4.3K) — directional, **not marks**.
**Hypothesis, not a finding:** a supply interruption that has **already happened** and is priced as **slow to reverse**, rather than a war still widening. → HAWK, BRENT, FALCON · **KB-ORC-087**

**5. 🟠 Kalshi "cite the MID" returns a meaningless 50.0 on SETTLED (bid 0/ask 1) and UNTRADED books** — apply the mid only when `result` is empty AND OI > 0; when settled, read `result`. Full record → **KB-ORC-086**, Maintenance flags below. *(Collapsed 2026-09-24 read-cap rotation.)*

---

## Signal Dashboard — 2026-09-18T01:49–01:52Z

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ7d | Δ30d | Vol/OI | Note |
|---|---|---|---|---|---|---|
| **Fed: HIKE at Oct mtg (specific)** | PM | **50.5%** | **+17.0** | **+27** | $1.5M | 🔴 the live Fed question |
| **Fed: NO change at Oct mtg** | PM | **49.5%** | **−16.0** | **−22** | $1.9M | |
| Fed Oct, `Above 4.00%` rung | Kalshi | 52.0 mid | — | — | 21.8K OI | ⚠️ **cumulative — difference it** ⇒ **hike ≈50.5** |
| Fed Oct, `Above 4.25%` rung | Kalshi | 1.5 mid | — | — | 7.0K OI | ⇒ hike-50+ ≈1.5 |
| **Fed: how many hikes 2026 (2)** | PM | **61.5%** | — | **+47** | $114.3K | ★ new pin; 1 hike 18.5 / 3 hikes 18.5 |
| Fed: ANOTHER hike in 2026 | PM | 83.5% | — | — | $38.5K | ★ new pin (basis change — see watchlist) |
| Fed funds end-2026 (4.25% bucket) | PM | 50.4% | **+27.5** | **+38** | $441.0K | ≥4.5% at 30.0% (Δ7d +21.3) |
| **Fed: NO cuts 2026** | PM | **95.3%** | +2.6 | +10 | $8.4M | 🔴 3rd read >90%; series high |
| Fed: 1 cut 2026 | PM | 1.8% | −3.9 | −8 | $3.2M | complement collapsed |
| **US recession 2026** | PM | **8.5%** | — | +1 | $2.0M | ⚠️ **DISJUNCTION contract** |
| Recession 2026 (NBER-only) | Kalshi | **5.0 last / 5.5 mid** | — | — | 927.5K OI | gap persisted 10d — **n=2** |
| **Sept CPI `>3.5%`** | Kalshi | **83.0 mid** | — | — | 19.7K OI | 🔴 ⚠️6¢ · prints 10/14 · Alert 3 |
| Sept CPI `>3.4%` | Kalshi | 95.0 mid | — | — | 15.5K OI | |
| Sept CPI `>3.3%` | Kalshi | 98.5 mid | — | — | 6.8K OI | |
| Aug CPI `>3.3%` / `>3.4%` / `>3.5%` | Kalshi | **YES / NO / NO** | — | — | settled | ⇒ **Aug YoY ∈ (3.3, 3.4]** |
| Sept U3 `>4.2%` | Kalshi | 13.5 mid | — | — | 13.3K OI | was 16.0 on 9/07 |
| Sept U3 `>4.3%` | Kalshi | 4.5 mid | — | — | 5.2K OI | ⚠️3¢ |
| US inflation >5% in 2026 | PM | 8.5% | +0.5 | +1 | $332.7K | |
| US unemployment ladder 2026 (top) | PM | 9.0% | −0.5 | −1 | $142.1K | liq $3.1K ⚠️thin |
| US credit downgrade 2026 | Kalshi | 9.0 mid | — | — | 33.8K OI | 11.0 last |
| Hormuz traffic normal by Dec 31 | PM | **17.5%** | +1.0 | **−18** | $11.8M | ⚠️ **PortWatch PRINT**, not throughput |
| Major bank bailout before 2027 | PM | 6.5% | — | −2 | $4.2K ⚠️ | |
| US bank failure by Dec 31 | PM | 55.5% | −7.5 | — | $2.4K ⚠️ | ⚠️thin — **NOT marked** |
| Which banks fail by EOY (top) | PM | 3.4% | — | +0 | $539 ⚠️ | |
| China GDP 2026 (top) | PM | 89.5% | — | +1 | $223.7K | → ZHAO |
| China invade Taiwan before 2027 | PM | 4.7% | +0.6 | +1 | $42.2M | |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ7d | Δ30d | Vol | Note |
|---|---|---|---|---|---|---|
| **WTI $100 (Sep)** | PM | **100.0%** | **+62.9** | — | $443.1K | ⛔ **RESOLVED YES — v4 leg dead** |
| **WTI $105 (Sep)** | PM | **100.0%** | **+84.5** | — | $713.5K | ⇒ high printed $105–$110 |
| **WTI $110 (Sep) — v5 supply leg** | PM | **3.85%** (9/24) | **−14.6** | — | $837.4K | ★ **ADOPTED as v5 9/24 (WQ-260); liq $29.9K; 7d to close** |
| WTI closes above $96 on 9/18 | PM | 55.0% | — | — | $58 ⚠️ | ⇒ spot ≈ $96 |
| Hormuz avg daily transits end-Sep (0–5) | PM | **64.0%** | −6.0 | — | $10.8K ⚠️ | 🔴 **40.5% on 9/07 ⇒ +23.5pp** |
| Hormuz ships-transit weekly (25–29) | PM | 28.0% | — | — | $3.7K ⚠️ | ✅ **ROLLED to week-of-9/14** |
| Hormuz ships-any-day by Sep 30 | PM | 52.5% | +1.5 | — | $16.0K ⚠️ | |
| **Hormuz shipping targeted (daily)** | PM | curve below | — | — | $2.1K ⚠️ | ★ **NEW PIN — ⚠️ BASIS CHANGE** |
| Hormuz 0-ships closure (by-date) | PM | 100.0% | +93.0 | −3 | $529.1K | ⛔ **known FALSE ⛔RESOLVED — DO NOT REPLACE** |
| **US invade Iran before 2027** | PM | **16.5%** | +1.0 | **−1** | **$66.7M** | 🔑 still flat — deepest contract on the board |
| US declares war on Iran by Dec 31 | PM | 2.6% | +0.7 | −1 | $852.1K | |
| Iranian regime fall before 2027 | PM | 6.5% | — | +0 | $26.1M | |
| Iran ends enrichment by Dec 31 | PM | 12.5% | −0.5 | +2 | $1.7M | |
| US-Iran deal 2026 (top) | PM | 13.5% | +2.0 | −8 | $259.6K | |
| Bab el-Mandeb closed (by-date) | PM | 18.5% | −7.0 | −2 | $878.3K | |
| Houthi vs Israel by Sep 30 | PM | 2.9% | −3.5 | — | $20.2K | |
| Brent >$85.99 @ Sep30 | Kalshi | **94.5 mid** | — | — | 2.1K OI | **was 82.0 on 9/07 (+12.5)** → BRENT |
| Brent >$91.99 @ Sep30 | Kalshi | **80.0 mid** | — | — | 5.6K OI | **was 61.0 on 9/07 (+19.0)** → BRENT |
| BOJ September decision (top) | PM | 99.9% | +1.8 | +16 | $431.4K | ⏳**resolves 9/18** → SAM, BOND |
| BOJ October decision (top) | PM | 79.0% | −6.5 | +6 | $38.8K ⚠️ | → SAM |
| Corporate bankruptcies 2026 >750 | Kalshi | 83.5 mid | — | — | 6.0K OI | ⚠️9¢ book |
| Clarity Act signed 2026 | PM | 8.2% | **−9.3** | **−12** | $21.7M | → BROCK |
| AI bubble burst 2026 | PM | 9.8% | −3.0 | −2 | $2.4M | → BROCK |
| MicroStrategy bankruptcy by 2027 | PM | 3.1% | +0.7 | +0 | $202.7K ⚠️ | |
| US debt default by 2027 | PM | 2.6% | −0.4 | −0 | $18.3K ⚠️ | |
| Russia-Ukraine ceasefire by Dec 31 | PM | 22.5% | +1.0 | +1 | $2.6M | |
| Venezuela: Delcy out by 2027 | PM | 8.5% | −1.0 | +0 | $188.9K | → BRENT |

**Hormuz shipping-targeted forward curve** (read the CURVE, not the current leg — hot-theater rule): **9/17 50.0% · 9/18 29.5% · 9/19 35.0% · 9/20 33.0% · 9/21 31.0% · 9/22 37.5%.** ⚠️ Event vol **$2.1K = NOMINATION-grade**, not a mark; ≥3-day re-check before any routed read.

### Tier 3 — sentiment
| Market | Plat | Now | Δ7d | Δ30d | Note |
|---|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 81.5% | −2.0 | **+0** | 🔑 **flat on the month through a hike, $105 oil and a hot CPI** |
| Best asset 2026 (S&P top) | PM | 54.5% | — | **−14** | stabilised ~14pp below August — VX-ORC-09 |
| Mamdani freezes NYC rents <2027 | PM | 87.8% | +5.0 | +9 | ⚠️thin $1.1K |
| FL Cat-4 hurricane by 2027 | PM | 4.5% | −1.0 | −12 | ⚠️thin → CORAL/AEOLUS |
| FL Cat-5 hurricane by 2027 | PM | 2.5% | −4.0 | −9 | ⚠️thin |

**Derived series (9/24):** ✅ **v5 LIVE — +74.65pp @ 2026-09-24T19:07Z** `[v5-wti110-vintage-break]` (disruption 78.5 PortWatch-print basis − supply $110 3.85; 0-ships context 33.0; Kalshi ctx KXIRANCRUDE >2.0 51.5% mid, OI 0). **Not comparable to any v4 row.**
**Derived series (9/17 record):** no row written (v4 leg settled); last valid v4 row +36.0pp @ 2026-09-07T16:10Z.

---

## Convergence Matrix

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| **Fed path (Sept)** | **SETTLED — hiked to 3.75–4.00% on 9/16**, Kalshi settle 86.0¢ | my 50.5/50.0 coin flip was a pre-CPI vintage | **resolved against the standing read** | 🟢 **closed by resolution** |
| **Fed path (Oct)** | PM hike 50.5% / Kalshi differenced ≈50.5% | no desk carries a live Oct number | **venues agree to 0.0pp** | 🟠 **live — the new question** |
| **Fed venue basis** | PM–Kalshi 0.0pp (Oct); futures ~90% → Kalshi settle 86¢ (Sept) | — | **episodic convergence, n=2**; CME half still **unanswerable** | 🟡 |
| **Inflation** | Sept CPI `>3.5%` **83.0 mid** vs August's 10.0% at the same rung | HENRY owns the print | crowd repriced hard **upward** | 🔴 **new** |
| **Recession (2026)** | PM 8.5% (**disjunction**) / Kalshi 5.0–5.5% (**NBER-only**) | RED 4–12%, interval contains both | ~3pp cross-venue gap **persisted 10 days (n=2)** | 🟠 |
| **Oil: premium vs shortage** | **the supply event HAPPENED** — WTI touched $105 | premium ≠ shortage | ⛔ **instrument dead by resolution** | 🔴 **successor needs a ruling** |
| **Iran: chokepoint vs escalation** | disruption **deepening** (normal-by-Dec 17.5%) / escalation **draining** (Bahrain −61, UAE −54) | HAWK owns the reality | **axes decoupled** | 🟠 **new** |
| Bank failure / bailout | bailout 6.5%, ANY-bank 55.5% (⚠️thin, Δ7d −7.5) | REGINALD regional stress | continued fade | 🟢 |
| Tail complacency | NEH 81.5% (Δ30d +0), S&P leg 54.5% (Δ30d −14) | — | **NEH did not move through a month of events** | 🟠 standing |

---

## Maintenance flags
- ✅ **Closed 9/17 items moved to their single home** (settled-top-leg selector fix KB-ORC-090 · no standalone Kalshi VIX market KB-ORC-089 · `history` two-rows-for-today, unpatched by design): `MAINTENANCE.md` 2026-09-17 entries. Moved 2026-09-24 read-cap rotation.

*Detail lives in `MAINTENANCE.md` (structural) and `workbook/KB.tsv` (findings). This section carries only what a reader must act on or avoid.*

- ⚠️ **Kalshi mid-price rule, tightened:** apply the mid **only when `result` is empty AND open interest is non-zero.** A settled book (bid 0 / ask 100) and an *untraded* book (bid 0 / ask 99) both yield a meaningless ~50.0. → KB-ORC-086, KB-ORC-089
- ⚠️ **`pull`'s `PINNED BUT NOT FOUND` still does not distinguish "resolved" from "bad slug."** Unfixed. Six pins fired it this session and **one had resolved YES** — the resolution *was* the signal.
- ⛔ **Still absent (dated, do not re-chase):** no **October WTI $100** market (4-way search) · no **September Iran-ACTOR** shipping event (5th consecutive recorded absence) · **three of four Kalshi gap-fills have zero open events**, the fourth sits at **OI 26** → recommend demoting to a **quarterly** re-check. → KB-ORC-089
- ⛔ **Kalshi is NOT a venue for the oil supply question** (all supply series untraded or no open events) ⇒ **any successor to the dead supply leg must come from Polymarket.** ⚠️ **Partly overtaken 9/24:** KXIRANCRUDE re-lists MONTHLY (August production finalized in (2.0, 2.2] mbpd; September event `-26OCT13` open) — still near-untraded (OI 0–900 per rung), so it is a CONTEXT column only, never a leg.
- ✅ **Coverage sweep run 9/17** (6d late) — nothing pinned from it. **Next due ~2026-09-24.** Venue sweep same day: **5 new pins**, 2 considered-and-rejected (30Y before-2027 too thin; 5Y has no named consumer).
- 🔑 **Curve-point distinction:** the gate keys on **DGS10**; the held instrument is **TLT (20+ year)**. **Not the same read.** The deepest market sits on the gate's variable ($503.0K); the point nearest the held instrument is thinner ($34.5K). **TERRY/BOND own which matters.**
- ⚠️ **`STATUS.md` read-cap:** this file was rotated 9/17 at 85% of budget; maintenance detail moved to its single home in `MAINTENANCE.md`. **Re-check at each closeout.**

## BOTTOM LINE

**Three things happened while this desk was dark, and they are one story.** The Fed hiked 25bp to 3.75–4.00% on 9/16 — its first increase since 2023, unanimous — and it named **oil-driven inflation** as the reason. WTI touched **$105**. August CPI printed in **(3.3%, 3.4%]** and the crowd now prices September's `>3.5%` rung at **83.0 mid** where August's sat at **10.0%** at the same stage. **The oil shock, the inflation print and the hike are not three signals; they are one transmission chain, and my 9/07 alert was standing at the front of it** — I flagged the supply leg at 39.5% (+25.5pp/7d) and asked *"what is bidding the oil supply tail, if not the missiles?"* **The tail was right about direction within seven days. I still cannot name the cause**, and the 9/07 finding that the $66.7M invasion contract was **flat through the US-Iran exchange** still stands — it is 16.5% today, Δ30d −1.

**The instrument that was built to catch exactly this is dead, and it died by succeeding.** The disruption−supply spread existed to detect a flip from a price story to a supply story. The supply event **happened**: the leg resolved YES and the script correctly refused to log across it. **I did not re-pin a successor and that is the deliberate call** — WQ-190 ratified $100 when $100 was a 22–40% tail, and it has now been touched, so any successor at that strike measures a different thing. Re-striking silently would repeat the exact error I caught myself in on 9/07. **The $110 rung is deep enough to carry it ($633.6K vol) and Will/PROME should rule.**

**The thing I got wrong is not a number, it is coverage.** On 9/07 I held VX-ORC-04 at 🟠 pending "a ≥3-read confirmation on a full session." The reasoning was sound — a holiday print is not a confirmation. Then nobody was there to re-check for ten days, and the move completed unobserved. **A pre-commitment to re-check is worth nothing without a session to honour it in.** The same gap left a pre-CPI coin flip standing as the fleet's only live Fed read for nine days, which is what PROME's 9/14 packet was written to point at. **Both are recorded as coverage failures, not dressed up as calls.**
