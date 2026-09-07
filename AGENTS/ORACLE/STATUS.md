# ORACLE STATUS

**Live dashboard — prediction-market probabilities, divergences, alerts.**
**Last pull:** 2026-09-07T16:10Z (Polymarket 45 rows + Kalshi 12 rows, both `pull --log`; derived spread same stamp). **Box:** desktop (DESKTOP-BC6EF81); Kalshi signed lane **LIVE** (`status` rc=0, 16:09Z) — **per-box, never a fleet fact.**
**Session:** 2026-09-07 (Mon) — **US Labor Day: equity and bond markets CLOSED, prediction venues trading.** Tier-1 spawn by PROME on DOCKET L172 (dated 9/8). Main deliverable = the v3/v4 instrument-succession **DECISION BRIEF** for Will: `domain/sources/2026-09-07_v4-instrument-succession-DECISION-BRIEF.md`.

> **Prices here are a LOG, not a live quote.** Never cite this file as the current price — re-pull. Every figure carries platform/date/volume; thin (<$5K liq) is flagged ⚠️ and is never marked on one print.
> ⚠️ **EVERY Δ1d BELOW SPANS A US MARKET HOLIDAY.** Prediction venues traded; equities and Treasuries did not. There is no cash-market cross-check on today's moves. Re-check anything load-bearing on a full session (9/8–9/9).

---

## 🔴 Alerts (read first)

**1. 🔴 DOCKET L172's PREMISES ARE FALSIFIED — the supply leg never died, it ROLLED on 8/27, and option A was executed de facto without a ruling.**
`will-wti-reach-100-in-september-2026` is **LIVE: 39.5%** (Δ1d +7.0, Δ7d **+25.5**, vol **$225.1K**, liq $34.5K, ends 2026-10-01), and `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` has carried regime **`v4-sep-wti-supply-leg` since 2026-08-27T18:44Z**. The row's "supply leg DIES 9/1" and "no September WTI market (3rd check)" were true when checked on 8/11 and false by 8/27. **I rolled it as routine watchlist maintenance while the decision sat deferred** — which is exactly the "roll a known-broken construction forward" move option A was flagged for. One thing the accident bought: option A's cost was *"a gap of unknown length … an inference, not a schedule"*, and the **realised gap was ZERO** (market listed ≥5 days before the August leg expired). n=1, but the first datum this question has ever had. → PROME, Will · KB-ORC-082

**2. 🔴 The second free parameter is now DATED at the contract: the underlying rolls OCT→NOV WTI on the 2026-09-18 trading day — 2 days after the FOMC, 12 days before the window closes.**
Verbatim (Polymarket Gamma description, read 2026-09-07): resolution is on *"any 1-minute candle for the **Active Month** of WTI Crude Oil futures"*; *"the active month changes at the start of the **second trading session prior** to the nearest listed contract's last trading session"*; *"a contract's last trading day is **three business days prior to the 25th calendar day** of the month preceding the … delivery month."* Applied: Oct-2026 CL LTD = 3 business days before Fri 9/25 = **Tue 9/22**; switch = 2nd session prior = **the 9/18 trading day**. Prices from Pyth, unrounded.
⛔ **Direction NOT asserted** — in backwardation the same $100 threshold gets mechanically HARDER on 9/18, in contango easier. **I do not own the WTI curve; BRENT does.** Either way it is a level shift with no risk content, stacked on the touch-decay defect.
🔑 **The structural finding: NO option both escapes this parameter AND keeps the disruption-vs-supply discrimination.** A and D inherit the clause verbatim; B escapes it and substitutes OI 10 + a weekly roll; C escapes it and substitutes the PortWatch print; E escapes it by not measuring. ⇒ **disclose, do not replace.** → PROME, BRENT, HAWK, FALCON, TERRY · KB-ORC-082

**3. 🔴 The disruption−supply spread COLLAPSED 9.5pp and the SUPPLY leg led it — the registered tripwire condition, on the PortWatch-free leg. NOT raised, and the trajectory is why.**
| | 9/04T12:33Z | **9/07T16:10Z** | Δ |
|---|---|---|---|
| Disruption leg (`1 − P(PortWatch prints ≥60)`) | 73.5% | **75.5%** | +2.0 |
| **Supply leg** (WTI $100 Sep) | 28.0% | **39.5%** | **+11.5** |
| **Spread** | +45.5pp | **+36.0pp** | **−9.5** |
⛔ **But do NOT attribute the week to the 9/5 US-Iran exchange.** Daily closes on the supply leg: **9/1 26.5 · 9/2 37.5 · 9/3 34.0 · 9/4 35.0 · 9/5 31.5 · 9/6 30.5 · 9/7 39.5.** The +11.0 jump was **9/1→9/2, BEFORE the exchange**; the leg **FELL 4.5pp across 9/5–9/6, the two days of the exchange itself**; today's +9.0 is a holiday-session print. ⇒ one print is not a ≥3-read confirmation. **Re-check 9/8–9/9.** → HAWK, BRENT, FALCON, PROME · VX-ORC-04

**4. 🔴 THE SEPTEMBER FOMC CROSSOVER HAS UN-CROSSED — the 9/4 headline "HIKE is modal, five straight sessions" is RETIRED.**
Polymarket: **HIKE-25 50.5%** (Δ1d +1.0, **Δ7d −8.0**, $19.1M) vs **NO-CHANGE 49.5%** (Δ1d −1.0, **Δ7d +10.0**, $23.9M) — a **1.0pp gap**, inside noise. Kalshi `KXFED-26SEP` differenced (Above-3.50 99.0 / Above-3.75 **52.0** / Above-4.00 2.0) ⇒ **cut ~1.0 · hold 47.0 · hike-to-4.00 50.0** (+2.0 above 4.00). **Venues 0.5pp apart on the modal leg.** 18pp of mass moved back in a week.
⭐ **The three-venue spread BOND handed me has half-answered itself:** 9/3 was CME ~62–67 / PM 53.5 / Kalshi 45 (**17–22pp**); today the **PM–Kalshi leg is 0.5pp** ⇒ that half was **EPISODIC, not a standing basis.** Whether CME carries a *persistent* hawkish basis is **still unanswerable** — FedWatch is a JS shell `WebFetch` cannot read; every CME figure I hold is a WALTER relay; **I assert nothing about CME.** → LIQUID, HENRY, BOND, WALTER, RED, LABOR · VX-ORC-08

**5. 🟠 I am retracting my own 9/4 claim that the Kalshi Iran-crude barrel gauge is gone. It was a series-vs-event ticker false negative.**
`kalshi.py event KXIRANCRUDE` → **0 markets** (reproduced today) — because **KXIRANCRUDE is a SERIES ticker**; the live events are date-stamped. `kalshi.py search "Iran crude"` → **11 live markets**, coverage **CERTIFIED** (11,359 events scanned). Ladder `KXIRANCRUDE-26SEP10`, resolves 9/10: **>2.0 mbpd 95.0 last / mid 91.0, vol 10 ct, OI 10** · >2.4 68.0 / 64.5, OI 119 · >2.8 19.0 / 17.0, OI 25. **Total OI ~168 across 11 rungs; the 8/9 vintage of the >2.0 leg was 86.0% on OI 412** ⇒ the book thinned ~40× on that rung. **`VX-ORC-04`'s critical band "Iran-crude <2.0mbpd = real loss" is FIREABLE AGAIN** — but at OI 10 it is practically unmarkable. Flagged, **not silently re-keyed.** `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` · KB-ORC-081

**6. 🟠 RED's 83-day ask is answered BOTH WAYS, and the recession row STAYS.**
RED delivered **4–12%, no point estimate** (disclosed anchoring: it read my 7.0% first) — **the interval CONTAINS 7.0%**, so a desk at net-bear 58 does **not** dispute the crowd's level. RED's return ask — *publish the resolution criterion, verbatim, nobody has* — is answered at the primary today: the contract is a **DISJUNCTION**, not an NBER-declaration market. Leg 1 = two consecutive negative **BEA advance** quarterly prints anywhere **Q2-2025→Q4-2026**; leg 2 = an NBER announcement by the Q4-2026 advance estimate. **Leg 1 needs no NBER at all ⇒ RED's "unwinnable regardless of the economy" branch is FALSIFIED and the row is not retired.**
⚠️ **Perimeter mismatch remains, stated in RED's favour:** leg 1's window opens at **Q2 2025**, so part of the 7.0% prices quarters already printed and positive — **comparable in kind, not in perimeter.**
🆕 **And the venue agreement BROKE:** PM **7.0%** vs Kalshi `KXRECSSNBER-26` **4.0%** (Δp −2.0; 3.4M ct vol, **891.9K OI**, 1¢ book — not a thin artifact). Gap **0.0 → 3.0pp in three days.** Kalshi's contract is the **NBER-only** form, so the gap **may BE the disjunction premium** — registered as a hypothesis, **not asserted** (n=1; Kalshi rules text unread). → RED, PROME · KB-ORC-080

**7. 🟢 SETTLED — the BOND A-vs-B venue question is CLOSED as UNRESOLVABLE, not adjudicated. PROME can retire the HEARTBEAT open line.**
BOND's second 9/4 packet supplied the verbatim provenance: `SIG-W-20260901-006` line 42 named a **horizon** (*"a Sept-16 hike ~65–68% priced"*) and **no venue and no instrument anywhere in the packet.** ⇒ **NEITHER A (PM by-Oct cumulative) NOR B (CME September meeting).** BOND withdrew the figure as **UNSOURCED-AS-TO-VENUE** (`KB-BND-242` supersedes `KB-BND-238`, retained verbatim). **My cumulative-mislabel diagnosis stays WITHDRAWN and is not restored.**
⇒ **The class count is final at n=1 CONFIRMED (NEXUS 8/18) + 1 CLOSED-UNRESOLVABLE (BOND) — not "1 pending."** Nothing further can resolve it; there is no evidence left to gather.
🔑 **The rule BOND's case adds, and it is the better half:** my horizon rule would NOT have caught this — BOND's figure **had** the horizon and lacked the **venue**. ⇒ **state the VENUE *and* the HORIZON.** And the nastier property: *a figure with a **wrong** attribution fails the ask-the-desk check; a figure with **no** attribution reads as ordinary reporting and survives review.* **The undersourced number is more durable than the mis-sourced one.** → PROME (retire the line), BOND, NEXUS, HEARTBEAT

---

## Signal Dashboard — 2026-09-07T16:10Z

### Tier 1 — direct thesis relevance
| Market | Plat | Now | Δ1d | Δ7d | Vol | Note |
|---|---|---|---|---|---|---|
| **Fed: NO change at Sept mtg** | PM | **49.5%** | −1.0 | **+10.0** | $23.9M | ⚠️ **regained the lead-ish — 1.0pp gap** |
| **Fed: HIKE at Sept mtg (specific)** | PM | **50.5%** | +1.0 | **−8.0** | $19.1M | crossover **un-crossed** |
| Fed hike Sept, `Above 3.75%` rung | Kalshi | 52.0% | +1.0 | — | 582.8K ct | ⚠️ **cumulative ladder — difference it** ⇒ **50.0% hike** |
| Fed: HIKE by **Sept** mtg (cumulative) | PM | 51.5% | +2.0 | −3.0 | $1.3M | ⚠️ **not** the meeting-specific leg |
| Fed: HIKE by **Oct** (cumulative) | PM | 61.5% | — | −0.5 | $621.3K | ⚠️ **not** a Sept number |
| Fed: HIKE in 2026 (**aggregate**) | PM | 70.5% | −1.0 | −2.0 | $8.8M | ⚠️ **not** a Sept number |
| Fed: NO cuts 2026 | PM | **92.8%** | −0.2 | +4.2 | $8.1M | 🔴 2nd read through the >90% line |
| Fed: 1 cut 2026 | PM | 5.1% | +0.3 | −2.4 | $2.9M | |
| Fed funds end-2026 (dist, top) | PM | 41.2% | −0.5 | +3.2 | $1.4M | liq $1.6K ⚠️thin |
| **US recession 2026** | PM | **7.0%** | −0.5 | −0.5 | $1.7M | ⚠️ **DISJUNCTION contract** — see Alert 6 |
| Recession 2026 (NBER-only) | Kalshi | **4.0%** | −2.0 | — | 3.4M ct | 🆕 **gap 0.0 → 3.0pp**, 891.9K OI, 1¢ |
| August CPI `>3.3%` | Kalshi | **63.0%** | **+13.0** | — | 109.4K ct | 🔴 prints **Fri 9/11**; 2¢ book |
| August CPI `>3.4%` | Kalshi | 25.0% | — | — | 119.0K ct | ⚠️ 6¢ book — **mid 22.0** |
| August CPI `>3.5%` | Kalshi | 10.0% | — | — | 86.4K ct | ⚠️ 4¢ — **mid 8.0** |
| August CPI print (modal) | PM | 44.5% | — | −1.5 | $29.2K ⚠️ | thin — **cite Kalshi, not this**; ⏳4d |
| Sept U3 `>4.2%` | Kalshi | **16.0%** | — | — | 10.8K ct | ⚠️ **was 49.0 last / 41.5 mid on 9/4 — a −25pp move on a 1¢ book; NFP-driven, re-check** |
| Sept U3 `>4.3%` | Kalshi | 6.0% | — | — | 2.9K ct | ⚠️ 4¢ — mid 7.0 |
| US unemployment ladder 2026 (top) | PM | 9.8% | +0.6 | +0.9 | $133.6K | liq $3.7K ⚠️thin |
| US inflation >5% 2026 | PM | 8.5% | — | +1.5 | $320.0K | |
| US credit rating downgrade 2026 | Kalshi | 11.0% | −1.0 | — | 75.3K ct | |
| Major bank bailout before 2027 | PM | 7.0% | — | −0.5 | $4.2K ⚠️ | |
| US bank failure by Dec 31 | PM | 68.5% | −1.0 | **−4.0** | $2.2K ⚠️ | ⚠️ **thin — NOT marked**; the 9/4 +11.0 climb did **not** persist |
| Which banks fail by EOY (top) | PM | 5.1% | +0.6 | +2.4 | $1.0K ⚠️ | |
| China GDP 2026 (top) | PM | 89.5% | — | +1.0 | $222.3K | → ZHAO |
| China invade Taiwan before 2027 | PM | 3.8% | −0.1 | — | $41.0M | |

### Tier 2 — catalyst / theater
| Market | Plat | Now | Δ1d | Δ7d | Vol | Note |
|---|---|---|---|---|---|---|
| **WTI $100 (Sep) — war premium** | PM | **39.5%** | **+7.0** | **+25.5** | $225.1K | 🔴 **the v4 supply leg** · see Alerts 1–3 |
| Hormuz normal by Dec 31 | PM | **24.5%** | −1.0 | −4.0 | $10.5M | ⚠️ **= P(PortWatch prints 7dMA ≥60)**, not throughput |
| Hormuz avg daily transits **end-Sep** | PM | 40.5% *(0–5 band)* | +3.0 | +0.5 | $3.9K ⚠️ | ⚠️ band width changed vs Aug · **grades PortWatch** |
| Hormuz ships-any-day **by Sep 30** | PM | 60.5% | −4.5 | **−19.5** | $12.5K ⚠️ | ⚠️ title≠slug, read the title |
| Hormuz ships-transit weekly | PM | 73.5% | −6.0 | −3.0 | $24.6K ⚠️ | ⏮ **STALE-DATE — resolved 9/6, ROLL OWED** |
| Kalshi Iran crude `>2.0 mbpd` | Kalshi | 95.0 *last* / **91.0 mid** | — | — | 10 ct ⚠️ | 🆕 **RESTORED** (Alert 5) · **OI 10** · ⏳3d |
| Kalshi Iran crude `>2.4 mbpd` | Kalshi | 68.0 *last* / **64.5 mid** | — | — | 212 ct ⚠️ | deepest rung; OI 119 |
| Iran targets shipping (on-date) | PM | 100.0% | +84.5 | +87.0 | $13.8K | ⛔ **RESOLVED settled-leg artifact — NOT a move.** Roll owed |
| Hormuz 0-ships closure (by-date) | PM | 100.0% | +95.5 | +93.0 | $529.1K | ⛔ **known FALSE ⛔RESOLVED — DO NOT REPLACE** |
| Iran ends enrichment by Dec 31 | PM | 12.5% | — | −2.0 | $1.7M | |
| **US invade Iran before 2027** | PM | **14.5%** | — | −1.0 | $64.9M | 🔑 **FLAT 14.5 on 9/4, 9/5, 9/6, 9/7 — zero reaction to the 9/5 exchange** |
| US declares war on Iran by Dec 31 | PM | 3.0% | — | −0.5 | $838.6K | |
| Iranian regime fall before 2027 | PM | 6.5% | — | — | $25.6M | unchanged |
| US-Iran deal 2026 (top) | PM | 10.5% | — | +1.0 | $121.7K | |
| Bab el-Mandeb closed (by-date) | PM | 17.5% | +1.0 | — | $540.0K | |
| Houthi vs Israel by Sep 30 | PM | 7.4% | +0.9 | +0.1 | $3.9K ⚠️ | |
| Saudi military action vs Yemen | PM | 86.5% | **+42.0** | +40.0 | $3.5K ⚠️ | ⚠️ **thin ($1.8K liq) — NOT a mark**, ≥3d re-check |
| Brent >$85.99 @ Sep30 | Kalshi | 82.0% | +5.0 | — | 736 ct ⚠️ | → BRENT |
| Brent >$91.99 @ Sep30 | Kalshi | 61.0% | −1.0 | — | 3.7K ct | → BRENT |
| BOJ September decision (top) | PM | 98.2% | +0.4 | +10.2 | $232.0K | → SAM, BOND |
| BOJ September decision | Kalshi | 97.0% | — | — | 79.2K ct | venues agree 1.2pp |
| BOJ October decision (top) | PM | 83.5% | +2.5 | −2.0 | $30.7K ⚠️ | → SAM |
| Clarity Act signed 2026 | PM | 16.5% | +1.0 | +4.0 | $14.2M | → BROCK |
| AI bubble burst 2026 | PM | 10.8% | −1.1 | +0.9 | $2.4M | 2nd non-negative week → BROCK |
| MicroStrategy bankruptcy by 2027 | PM | 3.4% | −0.4 | −0.1 | $202.5K ⚠️ | |
| Corporate bankruptcies 2026 >750 | Kalshi | 83.0 *last* / **87.0 mid** | — | — | 6.2K ct | ⚠️ 6¢ book — cite MID |
| US debt default by 2027 | PM | 1.7% | −0.1 | −1.1 | $17.1K ⚠️ | |
| Russia-Ukraine ceasefire by Dec 31 | PM | 22.5% | −1.0 | +3.0 | $2.6M | |
| Venezuela: Delcy out by 2027 | PM | 10.5% | −0.5 | — | $188.0K | → BRENT |

### Tier 3 — sentiment
| Market | Plat | Now | Δ1d | Δ7d | Note |
|---|---|---|---|---|---|
| Nothing Ever Happens 2026 | PM | 81.5% | −1.0 | −3.0 | 2nd weekly decline off the 85.0 high |
| Best asset 2026 (S&P top) | PM | 54.5% | — | −1.0 | ⚠️ **gave back the 9/4 retrace** — see VX-ORC-09 |
| Mamdani freezes NYC rents <2027 | PM | 85.0% | −0.9 | +2.5 | |
| FL Cat-4 hurricane by 2027 | PM | 6.5% | −4.5 | −8.0 | ⚠️thin $989 → CORAL/AEOLUS |
| FL Cat-5 hurricane by 2027 | PM | 6.6% | +0.2 | −7.4 | ⚠️thin $1.4K |

**Derived series:** disruption−supply spread **+36.0pp** `[v4-sep-wti-supply-leg]` — **COLLAPSED 9.5pp from +45.5, supply-led.** ⚠️ the disruption leg is `1 − P(PortWatch prints ≥60)`, **NOT** "disruption persists" (KB-ORC-079).

---

## Convergence Matrix

| Axis | Crowd says | Our thesis | Gap | State |
|---|---|---|---|---|
| **Fed path (Sept)** | hike 50.5% PM / 50.0% Kalshi; hold 49.5% — **a coin flip** | BOND's 65–68% **withdrawn as unsourced-as-to-venue** | no live disagreement | 🟢 **closed** |
| **Fed venue basis** | PM–Kalshi 0.5pp apart today (was 8.5pp on 9/3) | CME ~62–67 (WALTER relay, **unread by any desk**) | PM–Kalshi half was **episodic**; CME half **unanswerable** | 🟡 |
| **Recession (2026 contract)** | PM 7.0% (**disjunction**) / Kalshi 4.0% (**NBER-only**) | RED **4–12%, interval contains 7.0%** | **no dispute on level**; 3.0pp cross-venue gap is new | 🟠 **relabelled, not retired** |
| **Oil: premium vs shortage** | disruption 75.5%, WTI-$100 39.5% | premium ≠ shortage | spread **+36.0, supply-led collapse** | 🔴 **tripwire fired — re-check on a full session** |
| Bank failure / bailout | bailout 7.0%, ANY-bank 68.5% (⚠️thin, Δ7d −4.0) | REGINALD regional stress | the 9/4 climb did not persist | 🟢 |
| Tail complacency | NEH 81.5%, S&P leg 54.5% | — | complacency easing as tails reprice | 🟠 standing |
| Credit credibility | downgrade 11.0% | BOND owns the label | policy axis ≠ credibility axis | 🟡 |

---

## Maintenance flags

- ⏳ **ROLL OWED (now overdue, literal-date gate): the Hormuz weekly ladder resolved 9/6** and prints `⏮stale-date`. **Not rolled this session** — the standing rule is "do not pin a $40 book" and depth was not checked. Sixth consecutive late roll; **treat 9/8 as hard.**
- ⏳ **ROLL OWED: no September Iran-shipping on-date event** (unchanged from 9/4). The August pin shows `⛔RESOLVED` at 100.0% with Δ1d +84.5 — **a settled-leg display artifact, not a move.**
- ⚠️ **Do NOT replace the 0-ships market** on its false `⛔RESOLVED` — by-date ladder, settled rung wins top-leg selection. Fires every session. Row annotated DO-NOT-REPLACE.
- 🔧 **`polymarket.py history` still writes TWO rows stamped with today's date** (intraday bar + live point). Reproduced today on four slugs: e.g. WTI-$100 printed `9/7 35.5` and `9/7 39.5`. Harmless for trajectory, **wrong if read as today's close.** Logged, not patched — the duplicate rows are what make pre/post event studies possible, so the fix is a separate intraday accessor, not a dedupe.
- 🔧 **`kalshi.py event <SERIES>` returns 0 markets for a date-stamped series and looks identical to a delisting** — this cost me a false "the gauge is gone" alert on 9/4 (Alert 5). **Interim discipline: never conclude absence from `event`; confirm with `search`, which certifies its own coverage.** A real fix would make `event` fall back to the series endpoint. Logged in MAINTENANCE.md.
- **Coverage sweep last run 9/04 → next due ~2026-09-11.** Not run today (spawn was task-scoped).
- **Kalshi watchlist pulled 12-of-12**; only the `Above 3.75%` rung of `KXFED-26SEP` is pinned, so **the ladder must be fetched via `event KXFED-26SEP` to difference it** — done this session.

---

## BOTTOM LINE

**The decision Will was asked to make on 9/8 is not the decision that is actually open.** DOCKET L172 asks what should replace a supply leg that died on 9/1. It did not die — **it rolled on 8/27, and I rolled it, as maintenance, while the ruling sat deferred.** So the live question is whether to *ratify* that roll and on what disclosure terms, and the real deadline is the **October roll around 9/28**, not tomorrow. The brief is written, the successor DOCKET row is drafted verbatim, and **Will rules.**

**The one genuinely new fact in the succession question is a date.** The v4 supply leg changes its underlying from October to November WTI on **2026-09-18** — two days after the FOMC, twelve days before the window closes — and **no option escapes that parameter while keeping the premium-vs-shortage discrimination.** Option B, the idea I called the best in the list and killed on a box-darkness premise, is **rehabilitated in premise and refused on depth**: the Kalshi lane is live, the ladder is real and I was wrong to call it gone — but its named rung carries **open interest of ten contracts** and it now rolls weekly, which is what got option D rejected. The answer is to **disclose the defect, not to shop for a contract without one.**

**Two things moved on the tape and one of them is being widely misread.** The September FOMC un-crossed — hike 50.5 vs hold 49.5 on Polymarket, 50.0 vs 47.0 on Kalshi, an 18pp round trip in a week — so *"the crowd flipped the Fed"* is now a stale sentence. And the oil supply leg is up **25.5pp on the week** into a US-Iran exchange, which reads like a war repricing until you look at the daily closes: **the jump was 9/1→9/2, before the exchange; the leg FELL on 9/5 and 9/6, the days of the exchange; and today's +9.0 landed on a holiday session with no cash market open.** The crowd's own invasion contract — $64.9M deep — has not moved off **14.5%** for four straight days. **Something is bidding the oil tail, and on this evidence it is not the missiles.**
