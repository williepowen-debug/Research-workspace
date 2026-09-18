# ORACLE STATUS

**Live dashboard — prediction-market probabilities, divergences, alerts.**
**Last pull:** 2026-09-18T01:49–01:52Z (Polymarket 43 rows `pull --log` + Kalshi 11 tickers via the **PUBLIC** trade-api + `history --write` 7,469 daily rows + `coverage` + `movers`). **Box:** **LAPTOP** (`WilliePOwen`) — the **authenticated** Kalshi lane is **DOWN here by design** (`~/.config/kalshi` absent; `kalshi.py` dies at import). **Per-box, never a fleet fact.**
**Session:** 2026-09-17 (Thu) — **first session since 2026-09-07. THE DESK WAS DARK FOR TEN DAYS AND MISSED BOTH THE 9/11 CPI AND THE 9/16 FOMC.** Catch-up session at Will's direction.

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

**2. 🔴🔴 WTI TOUCHED $100 AND THEN $105 IN SEPTEMBER. THE v4 SUPPLY LEG RESOLVED YES — the instrument did not flip regime, it TERMINATED, and its $100 threshold is now AT-THE-MONEY rather than a supply tail.**
`will-wti-reach-100-in-september-2026` settled **100.0%** (Δ7d +62.9, vol $443.1K). The **$105** leg went **Δ7d +84.5 → 100.0%** (vol $713.5K); the **$110** leg sits **15.5–16.0%** at **Δ7d −29.0** ⇒ **the September high printed between $105 and $110.** Already retraced: the 9/18 close-above ladder reads above-$96 **55.0%** / above-$100 **7.0%**, and `dip-to-100-from-september-14` is **100.0%** ⇒ **spot is back near $96.**
✅ **`tools/disruption_supply_spread.py` HARD-EXITED and logged nothing** ("STALE-PAIRED … 11d apart") — the registered leg-resolution killer fired exactly as designed.
⛔ **DO NOT compute 82.5 − 100 = −17.5pp as a spread.** Differencing against a settled leg is the v1 failure this guard was built after. I name the tempting-but-wrong number so no consumer derives it independently.
⚠️ **NO OCTOBER WTI $100 MARKET EXISTS** — searched four ways 9/17 (`"WTI October 2026"`, `"WTI 100"`, `"WTI crude"`, `"oil price"`). **Absence RECORDED, not inferred away** — that was my own 9/07 pre-commitment.
⛔ **I did NOT re-pin or re-strike a successor, deliberately.** WQ-190 ratified $100 as v4 **when $100 was a 22–40% tail.** It has been touched. Any successor at $100 measures something the ratified instrument did not — a **change of MEANING, not a maintenance roll** — and doing it silently is exactly the option-A error I caught myself in on 9/07. **Candidate for a ruling, not adopted: the $110 rung** (vol $633.6K, liq $86.6K — genuinely deep). → **PROME/Will packet written.** → BRENT, HAWK, FALCON, TERRY · **KB-ORC-084** · VX-ORC-04

**3. 🔴 SEPTEMBER CPI IS PRICED FAR HOTTER THAN AUGUST WAS — the `>3.5%` rung is at 83.0 mid where August's was 10.0%.**
**August RESOLVED (printed 9/11):** `KXCPIYOY-26AUG-T3.3` **YES** · `T3.4` **NO** · `T3.5` **NO** ⇒ **August headline CPI YoY landed in (3.3%, 3.4%].**
**September ladder** (prints **2026-10-14**): `>3.3%` **98.5 mid** (OI 6,768) · `>3.4%` **95.0 mid** (OI 15,490) · `>3.5%` **83.0 mid** (bid 80 / ask 86 — ⚠️ 6¢, **cite the mid**, OI 19,679).
⚠️ **The ~+73pp like-for-like jump is NOT clean and I will not quote it as one:** August was read at **T-4 days**, September at **T-27 days**. A longer horizon normally carries *more* uncertainty, which pushes a `>3.5%` rung **down** — so the bias runs **against** the finding and the move is very likely real, but **re-read on 2026-10-10 (T-4) for the honest comparison.** ⚠️ Depth is modest vs August's 95K–162K at settlement; early books thicken. → HENRY, LIQUID, BOND, RED, LABOR · **KB-ORC-085**

**4. 🟠 THE TWO IRAN AXES HAVE DECOUPLED AND POINT OPPOSITE WAYS: chokepoint disruption deepening, Gulf-state escalation draining.**
**Deepening:** Hormuz-normal-by-Dec-31 **17.5%** (Δ30d −18, **Δ90d −69**, $11.8M — deep) · normal-by-Oct-31 **6.5%** · end-Sept **0–5 transits/day band 64.0%** (was 40.5% on 9/07, **+23.5pp**).
**Draining:** Iran-targets-Bahrain **11.5%** (Δ7d −61.0) · Iran-targets-UAE **18.5%** (Δ7d −54.0) · US-declares-war **2.6%** · US-invade-Iran **16.5%** (Δ30d −1 on **$66.7M**) · regime-fall **6.5%** (Δ30d +0). Also drained: SPR-to-280M-by-9/25 **10.2%** (Δ7d −65.5).
⚠️ **INFERENTIAL, not measured** — the instrument that *would* have measured this is dead by resolution (Alert 2), so I am reasoning around a hole in my own toolkit and saying so. ⚠️ **The Hormuz-normal leg resolves on the IMF PortWatch PRINT, not throughput** (KB-ORC-079): a detection failure and a real stoppage resolve identically, so "deepening" may partly be "PortWatch still not printing ≥60." **That caveat cuts against my own headline and is not optional when this is quoted.** ⚠️ Bahrain/UAE are thin ($1.2K / $4.3K) — directional, **not marks**.
**Hypothesis, not a finding:** a supply interruption that has **already happened** and is priced as **slow to reverse**, rather than a war still widening. → HAWK, BRENT, FALCON · **KB-ORC-087**

**5. 🟠 My "cite the MID on wide books" rule silently returns 50.0% on every SETTLED Kalshi market — it recommends maximum uncertainty for a known outcome.**
A resolved contract quotes **bid 0.00 / ask 1.00**, so the midpoint of a fully-wide book is **50**. Observed on **five** settled rungs in one pull (`KXFED-26SEP-T3.75` result **yes**, mid reads **50.0**; the three August CPI rungs identically). **The "WIDE book" flag fires on exactly these rows**, so the rule does not merely go silent — **it actively recommends the wrong number.**
**Amendment:** apply the mid rule **only when `result` is empty**; when settled, read `result`. KB-ORC-069 is **under-scoped, not wrong** — it was derived on live books and nobody asked what it does at resolution.
🔑 **Second time in three sessions an ORACLE instrument made a settled contract look live** — the Polymarket settled-leg artifact is the same bug on the *other* side (falsely **certain**; this one falsely **uncertain**). **One shared cause: a display layer that does not read the resolution field.** ⚠️ **NOT yet audited:** whether any past ORACLE surface quoted a 50.0 mid off a settled rung. **Open check, not a clean bill.** → PROME, DAEDALUS · **KB-ORC-086**

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
| WTI $110 (Sep) | PM | 15.5–16.0% | **−29.0** | — | $633.6K | 🔑 **succession candidate, NOT adopted** |
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

**Derived series:** ⛔ **NO ROW WRITTEN THIS SESSION.** `disruption_supply_spread.py` hard-exited on the resolved supply leg. Last valid row: **+36.0pp @ 2026-09-07T16:10Z** `[v4-sep-wti-supply-leg]`. **The series is PAUSED pending a successor ruling — it is not stale-by-neglect, it is stopped by design.**

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

*Detail lives in `MAINTENANCE.md` (structural) and `workbook/KB.tsv` (findings). This section carries only what a reader must act on or avoid.*

- ✅✅ **The settled-top-leg artifact is FIXED IN CODE — five standing exceptions retired at once.** `_select_event_leg()` now prefers the modal **UNRESOLVED** leg. Verified before/after **with controls**; genuinely-resolved events still flag correctly. ⇒ **the `⛔RESOLVED` flag is now TRUSTWORTHY — act on it.** The two `DO-NOT-REPLACE` banners in `watchlist.tsv` are **SUPERSEDED / non-operative**, kept as history only. ⚠️ **`ODDS_LOG` rows for the five affected markets are NOT comparable across 2026-09-17** (selector regime boundary). ⚠️ **The Kalshi half of the same root cause is disciplined, NOT fixed.** → KB-ORC-090, MAINTENANCE 9/17 #2
- ⚠️ **Kalshi mid-price rule, tightened:** apply the mid **only when `result` is empty AND open interest is non-zero.** A settled book (bid 0 / ask 100) and an *untraded* book (bid 0 / ask 99) both yield a meaningless ~50.0. → KB-ORC-086, KB-ORC-089
- ⚠️ **`pull`'s `PINNED BUT NOT FOUND` still does not distinguish "resolved" from "bad slug."** Unfixed. Six pins fired it this session and **one had resolved YES** — the resolution *was* the signal.
- ⛔ **Still absent (dated, do not re-chase):** no **October WTI $100** market (4-way search) · no **September Iran-ACTOR** shipping event (5th consecutive recorded absence) · **three of four Kalshi gap-fills have zero open events**, the fourth sits at **OI 26** → recommend demoting to a **quarterly** re-check. → KB-ORC-089
- ✅ **"No standalone VIX market on Kalshi" CONFIRMED** by a **4,546-series title scan** — retires the RE-OPENABLE class's only named candidate. **CLOSED-UNLESS-RE-LISTED**, bound named (5 categories, titles only). 🔑 `kalshi.py search` **could never have settled it** — it does not index series-level titles.
- ⛔ **Kalshi is NOT a venue for the oil supply question** (all supply series untraded or no open events) ⇒ **any successor to the dead supply leg must come from Polymarket.**
- ✅ **Coverage sweep run 9/17** (6d late) — nothing pinned from it. **Next due ~2026-09-24.** Venue sweep same day: **5 new pins**, 2 considered-and-rejected (30Y before-2027 too thin; 5Y has no named consumer).
- 🔑 **Curve-point distinction:** the gate keys on **DGS10**; the held instrument is **TLT (20+ year)**. **Not the same read.** The deepest market sits on the gate's variable ($503.0K); the point nearest the held instrument is thinner ($34.5K). **TERRY/BOND own which matters.**
- ⚠️ **`polymarket.py history` still stamps two rows with today's date** (intraday bar + live point). Unpatched by design — the duplicates enable pre/post event studies.
- ⚠️ **`STATUS.md` read-cap:** this file was rotated 9/17 at 85% of budget; maintenance detail moved to its single home in `MAINTENANCE.md`. **Re-check at each closeout.**

## BOTTOM LINE

**Three things happened while this desk was dark, and they are one story.** The Fed hiked 25bp to 3.75–4.00% on 9/16 — its first increase since 2023, unanimous — and it named **oil-driven inflation** as the reason. WTI touched **$105**. August CPI printed in **(3.3%, 3.4%]** and the crowd now prices September's `>3.5%` rung at **83.0 mid** where August's sat at **10.0%** at the same stage. **The oil shock, the inflation print and the hike are not three signals; they are one transmission chain, and my 9/07 alert was standing at the front of it** — I flagged the supply leg at 39.5% (+25.5pp/7d) and asked *"what is bidding the oil supply tail, if not the missiles?"* **The tail was right about direction within seven days. I still cannot name the cause**, and the 9/07 finding that the $66.7M invasion contract was **flat through the US-Iran exchange** still stands — it is 16.5% today, Δ30d −1.

**The instrument that was built to catch exactly this is dead, and it died by succeeding.** The disruption−supply spread existed to detect a flip from a price story to a supply story. The supply event **happened**: the leg resolved YES and the script correctly refused to log across it. **I did not re-pin a successor and that is the deliberate call** — WQ-190 ratified $100 when $100 was a 22–40% tail, and it has now been touched, so any successor at that strike measures a different thing. Re-striking silently would repeat the exact error I caught myself in on 9/07. **The $110 rung is deep enough to carry it ($633.6K vol) and Will/PROME should rule.**

**The thing I got wrong is not a number, it is coverage.** On 9/07 I held VX-ORC-04 at 🟠 pending "a ≥3-read confirmation on a full session." The reasoning was sound — a holiday print is not a confirmation. Then nobody was there to re-check for ten days, and the move completed unobserved. **A pre-commitment to re-check is worth nothing without a session to honour it in.** The same gap left a pre-CPI coin flip standing as the fleet's only live Fed read for nine days, which is what PROME's 9/14 packet was written to point at. **Both are recorded as coverage failures, not dressed up as calls.**
