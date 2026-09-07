# ORACLE — NEXUS Brief

**As of:** 2026-09-07 (Mon, 16:10Z / 12:10 ET — **US Labor Day: equity + bond markets CLOSED, prediction venues trading**) | **STATUS commit:** *(this session — see `git log AGENTS/ORACLE/STATUS.md`)* | **Session:** PROME Tier-1 spawn on DOCKET L172 (dated 9/8); desk was dark since 9/4.
**Status:** 🔴 — a registered oil tripwire fired on its clean leg, the September FOMC crossover **un-crossed**, and the docket question I was spawned to answer rests on **two falsified premises**.
**Domain:** Prediction-market monitoring (Polymarket + Kalshi) — crowd-implied probabilities & crowd-vs-thesis divergence. Inbound routed by WALTER.
**Box:** desktop (DESKTOP-BC6EF81); Kalshi **signed** lane LIVE (`status` rc=0, 16:09Z). **Record lane state per-box, never as a fleet fact.**
**Constraint honored:** no trade implied, no P&L, no position language. No new gate registered.
⚠️ **Every Δ1d in this brief spans a US market holiday** — prediction venues traded, cash markets did not. No cross-check exists on today's moves. Re-check anything load-bearing on a full session.

> **★ THE ONE THING TO TAKE FROM THIS BRIEF — something is bidding the oil supply tail, and on the evidence it is NOT the missiles.**
> The disruption−supply spread **COLLAPSED +45.5 → +36.0pp (−9.5)** and it collapsed on the **SUPPLY** leg (WTI-$100 Sep **28.0 → 39.5%, +11.5**) while the disruption leg moved only +2.0 (73.5 → 75.5). That is the series' **registered tripwire condition** — *"COLLAPSING = the regime is flipping from a price story to a supply story"* — firing on the one leg with **zero IMF-PortWatch exposure**, i.e. the epistemically clean half.
> ⛔ **But do NOT attribute it to the 9/5 US-Iran exchange.** Daily closes on the supply leg: **9/1 26.5 · 9/2 37.5 · 9/3 34.0 · 9/4 35.0 · 9/5 31.5 · 9/6 30.5 · 9/7 39.5.** The +11.0 jump was **9/1→9/2, BEFORE the exchange**; the leg **FELL 4.5pp across 9/5–9/6, the two days of the exchange itself**; today's +9.0 landed on a holiday session. And Polymarket's **$64.9M** invasion contract has sat at **14.5% on 9/4, 9/5, 9/6 and 9/7 — four flat days, zero reaction.** ⇒ **one print is not a ≥3-read confirmation. Re-check 9/8–9/9 on a full session before any desk acts on it.** (VX-ORC-04 · KB-ORC-082)
>
> **★ THE SEPTEMBER FOMC CROSSOVER HAS UN-CROSSED — my own 9/4 headline is RETIRED.** *"HIKE is the modal outcome, five straight sessions"* no longer holds. Polymarket **HIKE-25 50.5%** (Δ7d **−8.0**, $19.1M) vs **NO-CHANGE 49.5%** (Δ7d **+10.0**, $23.9M) — a **1.0pp gap, inside noise.** Kalshi `KXFED-26SEP` differenced (Above-3.50 99.0 / Above-3.75 **52.0** / Above-4.00 2.0) ⇒ **cut ~1.0 · hold 47.0 · hike-to-4.00 50.0.** Venues **0.5pp apart** on the modal leg. **18pp of mass moved back in one week.** ⚠️ **Never publish a raw Kalshi "Above X%" rung as P(hike) — the ladder is cumulative and must be differenced.**
> ⭐ **The three-venue spread BOND handed me has half-answered itself.** On 9/3 it was CME ~62–67 / PM 53.5 / Kalshi 45 (**17–22pp**). Today the **PM–Kalshi leg is 0.5pp** ⇒ **that half was EPISODIC, not a standing basis.** Whether CME carries a *persistent* hawkish basis is **still unanswerable**: FedWatch is a JS shell `WebFetch` cannot read, every CME figure I hold is a WALTER relay, and **I assert nothing about CME.** (VX-ORC-08)
>
> **★ THE DOCKET QUESTION I WAS SPAWNED FOR RESTS ON TWO FALSIFIED PREMISES — and the correction is the deliverable.** DOCKET L172 asks what replaces an ORACLE supply leg that *"DIES 9/1"* with *"no September WTI market (3rd check)."* **Both were true on 8/11 and false by 8/27:** `will-wti-reach-100-in-september-2026` is live (**39.5%**, $225.1K vol), and my derived series has carried regime `v4-sep-wti-supply-leg` **since 2026-08-27T18:44Z**. ⇒ **option A was executed de facto, by me, as routine watchlist maintenance, while the ruling sat deferred** — the exact "roll a broken construction forward" move option A was flagged for. The live decision is whether to **ratify** it, and the real deadline is the **October roll ~9/28**, not 9/8. Full brief + the verbatim successor DOCKET row: `domain/sources/2026-09-07_v4-instrument-succession-DECISION-BRIEF.md`. **Will rules; I brought options.** (KB-ORC-082)
>
> **★ THE FREE PARAMETER IS NOW DATED, AND NO OPTION ESCAPES IT.** Read verbatim at the contract: the WTI-$100 market resolves on *"any 1-minute candle for the **Active Month**"*, and the active month switches *"at the start of the second trading session prior to the nearest listed contract's last trading session."* Applied: Oct-2026 CL last trading day = **Tue 9/22**; the switch is **the 2026-09-18 trading day** — **2 days after the FOMC, 12 days before the window closes.** The $100 threshold is fixed and the underlying is not; **direction is NOT asserted** (backwardation makes it mechanically harder, contango easier — **the curve is BRENT's, not mine**). **No option both escapes this AND keeps the premium-vs-shortage discrimination:** A and D inherit the clause verbatim, B escapes it and substitutes OI 10 plus a weekly roll, C escapes it and substitutes the PortWatch print, E escapes it by not measuring. ⇒ **disclose, do not replace.**
>
> **★ A RETRACTION OF MY OWN, 72 HOURS OLD.** My 9/4 alert *"the Kalshi Iran-crude barrel gauge is GONE — `event KXIRANCRUDE` returns 0 markets"* was a **false negative**: `KXIRANCRUDE` is a **series** ticker and the live events are **date-stamped** (`KXIRANCRUDE-26SEP10`). `search "Iran crude"` returns **11 live markets, coverage CERTIFIED**. **Consumers: the gauge exists.** But it is unusable as a mark — the `>2.0 mbpd` rung carries **open interest of 10 contracts** (vs 412 on 8/09) and the series now rolls **weekly**. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` (KB-ORC-081)

---

## Cross-agent tensions

**Two live, one closed this session.**

1. 🟠 **RED ↔ ORACLE, recession — RESOLVED ON LEVEL, RELABELLED ON PERIMETER.** RED delivered **4–12%, no point estimate** (disclosed anchoring), and **the interval contains the crowd's 7.0%** ⇒ a desk at net-bear 58 does **not** dispute the crowd level. RED's return ask is answered at the primary: the Polymarket contract is a **DISJUNCTION** — two consecutive negative **BEA advance** quarterly prints anywhere **Q2-2025→Q4-2026**, **OR** an NBER announcement by the Q4-2026 advance estimate. **Leg 1 needs no NBER, so RED's "unwinnable regardless of the economy" branch is FALSIFIED and the convergence row is NOT retired.** ⚠️ Perimeter caveat, in RED's favour: leg 1's window opens at **Q2 2025**, so part of the 7.0% prices quarters already printed and positive — **comparable in kind, not in perimeter.** 🆕 **Cross-venue agreement BROKE:** PM 7.0% vs Kalshi `KXRECSSNBER-26` **4.0%** (891.9K OI, 1¢ book) — gap **0.0 → 3.0pp in three days**. Kalshi's is the **NBER-only** form, so the gap **may be the disjunction premium** — **hypothesis, not asserted** (n=1, Kalshi rules unread). (KB-ORC-080)
2. 🟠 **ORACLE ↔ BRENT/HAWK/FALCON, oil supply.** The tripwire fired on the clean leg but the trajectory refuses the obvious cause. **I own the crowd read only.** Whether the 9/1→9/2 bid and today's holiday-session +9.0 correspond to anything physical is **BRENT's and HAWK's**, and the **WTI curve shape** — which sets the direction of the 9/18 Active-Month step — is **BRENT's alone.**
3. ✅ **CLOSED — ORACLE ↔ BOND, the A-vs-B venue question.** BOND supplied the verbatim provenance: its 9/1 relay named a **horizon** (*"Sept-16"*) and **no venue and no instrument**. ⇒ **NEITHER A nor B; the 65–68% is withdrawn as UNSOURCED-AS-TO-VENUE, not adjudicated.** My cumulative-mislabel diagnosis stays withdrawn. **The class is final at n=1 CONFIRMED (NEXUS 8/18) + 1 CLOSED-UNRESOLVABLE — not "1 pending."** Nothing further can resolve it. **PROME: the HEARTBEAT retired-claims open line can be retired.**
   🔑 **The rule this adds:** my horizon rule would not have caught it — BOND's figure **had** the horizon and lacked the **venue**. **State the VENUE *and* the HORIZON.** And: *a figure with a **wrong** attribution fails the ask-the-desk check; a figure with **no** attribution reads as ordinary reporting and survives review.* **The undersourced number is more durable than the mis-sourced one.**

---

## Forward catalysts (ORACLE-relevant, dated)

| Date | Event | Instrument to read | Note |
|---|---|---|---|
| **Tue 9/8** | Hormuz weekly roll — **overdue, 6th consecutive late roll** | `polymarket.py search` the wk-of-9/7 ladder | **hard date**; do not pin a sub-$1K book |
| **Thu 9/10** | Kalshi `KXIRANCRUDE-26SEP10` resolves | the barrels ladder | context only — OI 10 |
| **Fri 9/11** | **August CPI, 08:30 ET** | **Kalshi is the instrument:** `>3.3%` **63.0%** (Δp **+13.0**, 109.4K ct); the PM modal market is ⚠️thin $29.2K | the CPI that arms the FOMC 5 days later; **take a pre/post read** — the NFP method is proven |
| Fri 9/11 | Coverage sweep due (last 9/04) | `polymarket.py coverage` | weekly cadence |
| **Tue–Wed 9/15–16** | **FOMC decision 2:00pm ET 9/16** | PM hike/no-change pair + Kalshi ladder **differenced** | **a coin flip on both venues.** Pin the day before; read same-day |
| **Fri 9/18** | ⚠️ **v4 supply leg's underlying switches OCT→NOV WTI** | `will-wti-reach-100-in-september-2026` | **mechanical level shift, no risk content.** Disclose beside every quote |
 | Fri 9/18 | BOJ September MPM (decision day; MPM runs 9/17–9/18) | PM 98.2% / Kalshi 97.0% (top leg) | → SAM |
| **~Mon 9/28** | **v4 OCTOBER ROLL — the real succession deadline** | search for an October WTI $100 market | ⚠️ **not yet searched — the roll assumes it will list** |
| Wed 9/30 | Sept Hormuz ladders + Brent Sep30 rungs resolve | | |
| Thu 10/1 | `will-wti-reach-100-in-september-2026` ends | | |

---

## Standing limitations consumers must carry

- **`tools/metrics.py collapse` scores entropy DROPS only.** A pure mass-transfer repricing is **unscored by construction**. ***Never read "collapse scan clean" as "nothing moved."***
- **Kalshi `KXFED-26SEP` is a cumulative "Above X%" ladder** — difference it. A raw rung is not P(hike).
- **Every Hormuz transit market ORACLE tracks grades the IMF PortWatch PRINT, not the strait** — a detection failure and a real stoppage resolve identically. Valid as a forecast of the print; **not** a throughput read. Undercount **not** quantified. (KB-ORC-079)
- **The Iran daily-tempo ladder prices events up to 4 days LATE.** Cite the date the **price moved**, not the leg's date.
- **`polymarket.py history` writes two rows stamped with today's date** (intraday bar + live point) — fine for trajectory, wrong as "today's close." Reproduced today.
- **`kalshi.py event <SERIES-TICKER>` returns 0 markets and is indistinguishable from a delisting.** Confirm absence with `search`, which certifies its own coverage.
- **Kalshi lane state is PER-BOX.** LIVE on DESKTOP-BC6EF81 today; that says nothing about the laptop.
- **Thin (<$5K liq) is never marked on one print** — ≥3-day re-check. Live today: Saudi-vs-Yemen +42.0 on $1.8K liq, ANY-bank-failure 68.5% on $1.1K.
