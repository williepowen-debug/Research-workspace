# DECISION BRIEF — ORACLE v3/v4 instrument succession (DOCKET L172 · Forum-4 N10)

**For:** Will (rules) · PROME (registers) · **From:** ORACLE, session 2026-09-07 (Mon, US Labor Day — equity/bond CLOSED, prediction venues trading)
**Box:** DESKTOP-BC6EF81 · **Kalshi signed lane LIVE** (`scripts/kalshi.py status` rc=0, 2026-09-07T16:09Z) — per-box fact, never a fleet fact
**Every figure below was read at the instrument this session, 2026-09-07T16:10Z.** Prices in this file are a LOG, not a live quote.
**Source of the question:** `FORUM/2026-08-10_positioning-exhaustion/04_synthesis/01_SAM_joint-synthesis-FINAL.md` SS7 N10 (Will-ruled 8/11); options A–E as I priced them at `FORUM/.../01_desk-state/P0_ORACLE_crowd-prices-are-not-positioning.md` §6.
**I bring options. I do not rule.**

---

## 0. ⛔ READ THIS FIRST — TWO OF THE DOCKET ROW'S THREE PREMISES ARE FALSIFIED

| Premise carried on DOCKET L172 | Status, verified today | Evidence |
|---|---|---|
| "the supply leg **DIES 9/1**" | ❌ **FALSE.** It did not die. It **rolled on 2026-08-27** | `will-wti-reach-100-in-september-2026` LIVE: **39.5%** (Δ1d +7.0, Δ7d +25.5), vol **$225.1K**, liq **$34.5K**, ends 2026-10-01. `workbook/DISRUPTION_SUPPLY_SPREAD.tsv` carries regime `v4-sep-wti-supply-leg` from `2026-08-27T18:44Z` |
| "**no September WTI market exists** (3rd check)" | ❌ **FALSE since ~2026-08-27.** True when checked (2026-08-11T02:1xZ); superseded | Same row. The market opened somewhere in **8/11 → 8/27** |
| "option B's stated blocker was Kalshi box-darkness … Kalshi LIVE on desktop" | ✅ **TRUE — and the re-read is §2** | `kalshi.py status` rc=0 today; the B instrument fetched live below |

**What this changes about the decision itself.** Will is not being asked "what replaces a dead leg." **Option A was executed de facto on 2026-08-27**, five days before the deferral's own 9/1 decision date, by me, without a ruling — the roll was a routine watchlist maintenance action and nobody connected it to N10. The live question is therefore:

> **(a) Ratify the A-roll that already happened, and on what disclosure terms? and (b) what happens at the OCTOBER roll (~2026-09-28), which is the next real deadline?**

**Self-criticism, stated because it is the whole lesson.** Option A's recorded cost was *"it REPRODUCES the mechanical-decay defect rather than fixing it — rolling a known-broken construction forward is how v2→v3 inherited this."* I did exactly that on 8/27 while the decision sat deferred. The regime tag was bumped correctly (old rows stay non-comparable), so nothing is corrupted — but the *choice* was made by maintenance rather than by ruling. `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` `[[finding_record_of_an_action_is_not_the_action]]`

**One thing the accident bought, and it is real evidence.** Option A's stated cost was *"a gap of **unknown length** … ~4 days' lead is the only evidence — that is an inference, not a schedule."* We now have an observation instead of an inference: **the September market existed by 8/27, ≥5 days before the August leg expired on 9/1, and the realised gap was ZERO.** n=1, but it is the first datum this question has ever had.

---

## 1. THE SECOND UNDISCLOSED FREE PARAMETER — NAMED IN AUGUST, **DATED TODAY**

N10 flagged it as *"the underlying rolls mid-window (Active Month; Sept expires ~8/20)"* — but that was the **August** window's roll. For the **live v4 window** it is unread until now. Verbatim from the contract (Polymarket Gamma `description`, `will-wti-reach-100-in-september-2026`, read 2026-09-07):

> *"…any 1-minute candle for the **Active Month** of WTI Crude Oil futures has a final 'High' or 'Low' price equal to or beyond … the listed price."*
> *"The active month changes at the start of the **second trading session prior** to the nearest listed contract's last trading session."*
> *"…a contract's last trading day is **three business days prior to the 25th calendar day** of the month preceding the contract's delivery month."*
> Resolution source: `https://pythdata.app/explore?search=WTI` — *"Prices will be used exactly as published by Pyth, without rounding."*

**Applied to the live window:** Oct-2026 CL last trading day = 3 business days before **Fri 2026-09-25** = **Tue 2026-09-22**. Active month switches at the start of the second session prior ⇒ **the 2026-09-18 trading day (session opens 18:00 ET Thu 9/17)**.

⇒ **The September window prices OCTOBER CL through ~9/17 and NOVEMBER CL from ~9/18** — a change of underlying **12 days before the window closes and 2 days after the 9/16 FOMC.**

**Direction, stated conditionally because the curve is not mine.** The $100 threshold is fixed; the underlying is not. In **backwardation** the deferred month sits lower, so the same threshold becomes mechanically **HARDER** on 9/18; in **contango**, easier. Either way it is a **level shift with no risk content**, stacked on the touch-decay defect already named. **ORACLE does not own the WTI curve shape — BRENT does.** I assert the roll and its date; I assert no direction.

### Does any option escape it?

| Option | Escapes Active Month? | What it substitutes instead |
|---|---|---|
| **A / status-quo v4** (monthly WTI $100 touch) | ❌ **No** — the clause is in the contract text; **every** monthly WTI touch market inherits it | — (also keeps the touch-decay defect) |
| **B** (Kalshi Iran-crude barrels) | ✅ **Yes** — no futures underlying at all | Depth (OI **10** on the named rung) + a **WEEKLY** roll |
| **C** (Hormuz term structure) | ✅ **Yes** | The **IMF PortWatch print** — a detection failure and a real stoppage resolve identically (KB-ORC-079) |
| **D** (weekly WTI $100 ladder) | ❌ **No** — same Active Month clause | already REJECTED 8/11 |
| **E** (freeze) | ✅ trivially — it stops measuring | the running spread |

> **ANSWER TO THE QUESTION AS ASKED: no option both escapes the Active-Month parameter AND preserves the disruption-vs-supply discrimination that is v3/v4's entire purpose.** Every escape route substitutes a *different* undisclosed parameter. **That argues for DISCLOSURE over REPLACEMENT** — the defect is not fixable by choosing a different contract, only by stating it beside every quote.

---

## 2. OPTION B — THE RE-READ ON MERITS (the assignment)

### 2.1 ⛔ First, a correction I owe: my own 9/4 "the Iran-crude gauge is GONE" was a FALSE NEGATIVE

`STATUS.md` (9/4) alerted: *"Iran-crude is a GAP, not a roll: `kalshi.py event KXIRANCRUDE` returns **0 markets**. The barrel-level supply-truth gauge is gone."* **That is wrong, and I am retracting it today.**

- `kalshi.py event KXIRANCRUDE` → **0 markets** (reproduced today). **`KXIRANCRUDE` is a SERIES ticker; the live EVENTS are date-stamped** (`KXIRANCRUDE-26SEP10`). Querying a series ticker through the event endpoint returns zero **by construction**.
- `kalshi.py search "Iran crude"` → **11 live markets**, `11,359 events scanned, 57 pages — FULL open-event universe, coverage CERTIFIED`.
- Same defect class as the pre-8/18 `search` false-negatives and the RE-OPENABLE class in SCRATCH. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` — *"lacks X" is a claim about your pattern set, not about the world.*
- **Consumers of the 9/4 claim:** `STATUS.md` alert (fixed this session) and `VX-ORC-04`, whose CRITICAL band reads *"Iran-crude <2.0mbpd = real loss"* — **that band was declared un-fireable and it is fireable again.** Corrected in VX this session.

### 2.2 The B instrument, live at the tape 2026-09-07T16:1xZ

`KXIRANCRUDE-26SEP10` — *"Will Iran's average daily crude [exports exceed X mbpd]"*, resolves **2026-09-10 (⏳3d)**:

| Rung | last | **mid** | spread | vol (ct) | OI |
|---|---|---|---|---|---|
| **>2.0 mbpd** (the option-B leg) | 95.0% | **91.0** | 8¢ | **10** | **10** |
| >2.2 | 85.0% | — | 8¢ | 0 | 0 |
| >2.4 | 68.0% | **64.5** | 7¢ | 212 | 119 |
| >2.6 | 37.0% | **35.5** | 7¢ | 14 | 14 |
| >2.8 | 19.0% | **17.0** | 4¢ | 337 | 25 |
| >3.0 | 7.0% | — | 8¢ | 0 | 0 |

**Total OI across all 11 rungs ≈ 168 contracts.** Cite the MID on these books (KB-ORC-069) — spreads are 4–9¢.

### 2.3 Verdict: **REHABILITATED IN PREMISE, REFUSED ON DEPTH**

| B's three blockers | Then (8/11) | Now (9/7) |
|---|---|---|
| ⛔ "fails on liveness — Kalshi is per-box and DARK on the laptop" | the stated blocker | ✅ **DEAD.** Signed lane rc=0 on this box; ladder fetched live. **The premise that killed B is falsified.** |
| ⚠️ "OI 412 — far below my thin guard" | 412 on the >2.0 leg | ❌ **WORSE by ~40×.** OI **10** on that rung; ~168 across the whole ladder. The 8/9 vintage read 86.0% on OI 412 |
| ⚠️ "monthly-resolving too" | monthly | ❌ **WORSE — the series re-listed WEEKLY** (`26SEP10`, ⏳3d). **Weekly re-basing is the exact property that got option D REJECTED.** B has acquired D's disqualifier |

✅ **What B still buys, and it is genuinely the best idea in the list:** it is the only candidate that measures **barrels, not price** — supply loss as barrels ceasing to exist, which is v3/v4's actual subject — and it carries **zero Active-Month exposure and zero PortWatch exposure.** Both other live options are contaminated by one or the other.

🔻 **But it is not adoptable as the v4 supply leg today.** A 10-contract open interest is ~2 orders of magnitude below the standing thin guard; a 7-day roll would bump `REGIME` weekly, which makes the series uncomparable with itself.

🟢 **It IS adoptable as a CONTEXT COLUMN** — logged beside the spread, never differenced into it, exactly as the 0-ships closure proxy is already handled in `disruption_supply_spread.py`. Cost ≈ zero, and it preserves the barrels read for the day the book deepens. **This is the half of B worth taking now.**

---

## 3. OPTIONS C AND E, AS I HOLD THEM TODAY (both have moved since 8/11 — neither for market reasons)

### C — pin the Hormuz-normalization TERM STRUCTURE

- **Instrument / venue / mechanics:** Polymarket. Deep leg `strait-of-hormuz-traffic-returns-to-normal-by-december-31` **24.5%** (Δ1d −1.0, Δ7d −4.0, **vol $10.5M, liq $457.8K**) — resolves YES if *"IMF Portwatch publishes a 7-day moving average … equal to or above 60."* Mid leg `…end-of-september` avg-daily ladder **40.5%** at the 0–5 band (vol **$3.9K ⚠️thin**). Weekly ladder **73.5%** (vol $24.6K, liq $674 ⚠️thin, **⏮ stale-date — resolved 9/6, roll owed**).
- **Free parameters:** the **PortWatch print** (see below); ladder **band width** (Aug 20-wide → Sep 5-wide — never difference across it, KB-ORC-078).
- **What it CAN resolve:** normalization *timing* as a hazard curve, on the deepest book on the venue; no month stamp, no touch mechanics, **no time decay, no Active Month**.
- **What it CANNOT resolve:** ⛔ **it has no supply leg at all**, so it loses the premium-vs-shortage discrimination that is v3/v4's entire purpose. It is a *better instrument*, not a *successor*.
- 🔻 **TWO DEGRADATIONS SINCE 8/11, and I am flagging them against my own 8/11 recommendation:**
  1. **The three-point curve is now a two-point curve.** I priced C on Aug-31 3.5% / Sep-30 14.5% / Dec-31 46.5%. **The Aug-31 rung has settled.** What remains is Dec-31 (deep, $10.5M) + Sep-30 (**$3.9K, thin**). A hazard curve on two points, one of them thin, is a weaker object than the one I recommended.
  2. **KB-ORC-079 (9/4, read at the primary) changed what C measures.** Every one of these legs resolves **exclusively on the IMF PortWatch print** — *"Ships not reported by IMF Portwatch will not be considered"*; a divergence from alternative sources is explicitly **not** grounds for correction. PortWatch's war-regime coverage is impeached (BRENT 8/17; external corroboration 8/20). ⇒ **C's "deepest book on the venue" advantage buys depth on a forecast of a PUBLICATION.** Its cost line is no longer only *"not a supply leg"* — it is *"not a throughput read either."*
- **Cost:** zero to keep (it is **already pinned** and is already v4's disruption leg). **Non-zero to PROMOTE** — promoting it would swap a disclosed defect for an undisclosed one.

### E — FREEZE at a dated banner + dated rewrite trigger

- **Mechanics:** banner `FROZEN <date> — not maintained…` on `DISRUPTION_SUPPLY_SPREAD.tsv`, declare rows comparable within regime only, register a dated rewrite trigger.
- **What it buys:** honesty. The decay defect is named, understood, and not fixable by rolling.
- 🔻 **Its cost is HIGHER today than on 8/11, and this is the sharpest input in the brief.** E's cost was *"loses the running spread."* **The spread is currently doing work:**

| | 2026-09-04T12:33Z | **2026-09-07T16:10Z** | Δ |
|---|---|---|---|
| Disruption leg (`1 − P(PortWatch prints ≥60)`) | 73.5% | **75.5%** | **+2.0** |
| **Supply leg** (WTI $100 Sep) | 28.0% | **39.5%** | **+11.5** |
| **Spread** | +45.5pp | **+36.0pp** | **−9.5** |

  The series' registered read is: *"COLLAPSING spread = the regime is flipping from a price story to a supply story → HAWK/BRENT/FALCON tripwire — but always read WHICH leg moved."* **It collapsed 9.5pp, and it collapsed on the SUPPLY leg** — the leg with **zero PortWatch exposure**, i.e. the clean one. **Freezing the series in the week it fires its designed signal on its cleanest leg is the highest-cost moment available to freeze it.**

---

## 4. RECOMMENDATION — one line, and Will rules

> **Ratify the 8/27 A-roll as v4 with the Active-Month roll DISCLOSED and DATED (2026-09-18) in the series header and beside every routed quote; add Kalshi `KXIRANCRUDE` as a non-differenced CONTEXT COLUMN (B rehabilitated in premise, refused on depth); keep C pinned as the disruption leg carrying its PortWatch label and do NOT promote it; do NOT freeze (E) while the spread is firing; and move the real deadline to the OCTOBER roll (~2026-09-28), because 9/8 is not a deadline for anything that is actually still open.**

**Why not the 8/11 recommendation (C+E, not B).** It was written against three premises, two of which are now false: that the leg would die (it rolled), and that B was unreachable (it is reachable). The half of C+E that survives is *"pin C on its own merits"* — already done — and the half that does not is *"freeze at 9/1"*, which the 9/7 spread collapse argues against.

**What I am NOT claiming:** I do not know the WTI curve shape and therefore do not state the roll's direction (BRENT's). I do not quantify the PortWatch undercount (BRENT states it is unquantified; I add nothing). I have not established that the 8/11→8/27 listing lead time is a schedule — it is one observation.

---

## 5. THE EXACT DOCKET ROW PROME SHOULD REGISTER

**⚠️ PROME edits `DOCKET.tsv`; ORACLE does not, and did not.** L172 is cited by physical line number, so per the file's own convention it **compacts in place** and the successor is **appended at EOF**. Tab-separated, six fields, in DOCKET column order (`date · description · owner · state · source · note`):

```
2026-09-28	ORACLE v4 supply-leg OCTOBER ROLL + Active-Month disclosure (successor to L172 / Forum-4 N10). L172's premises are FALSIFIED: the supply leg did NOT die 9/1 — it ROLLED 2026-08-27 to will-wti-reach-100-in-september-2026 (39.5%, $225.1K vol, $34.5K liq @ 2026-09-07T16:10Z), regime v4-sep-wti-supply-leg; and a September WTI market DOES exist. Option A was therefore executed de facto on 8/27 without a ruling. Second free parameter now DATED at the contract: Active Month switches Oct-CL -> Nov-CL on the 2026-09-18 trading day (LTD Tue 9/22 = 3 business days before Fri 9/25; switch = 2nd session prior), i.e. 12 days before the window closes and 2 days after the FOMC — a level shift with no risk content. NO option escapes it AND keeps the disruption-vs-supply discrimination (B and C escape it but substitute thinness+weekly-roll and the PortWatch print respectively) => disclose, do not replace.	Will (decision) / ORACLE (options, delivered 2026-09-07) / PROME (registers)	PENDING — ORACLE decision brief DELIVERED 2026-09-07 (AGENTS/ORACLE/domain/sources/2026-09-07_v4-instrument-succession-DECISION-BRIEF.md). ORACLE rec: ratify the A-roll as v4 with the Active-Month roll disclosed and dated 2026-09-18; add Kalshi KXIRANCRUDE-26SEP10 as a NON-DIFFERENCED context column (option B rehabilitated in premise — Kalshi lane rc=0 on DESKTOP 9/7 — but REFUSED on depth: OI 10 on the >2.0 rung vs 412 on 8/09, and the series re-listed WEEKLY, which is option D's rejected property); keep C pinned as the disruption leg with its PortWatch label, do NOT promote it (its Aug-31 rung settled, so the term structure is now 2 points, one thin, and KB-ORC-079 established all its legs grade the IMF PortWatch PRINT); do NOT freeze (E) — the spread COLLAPSED 45.5 -> 36.0pp on 9/7 led by the SUPPLY leg (the PortWatch-free one), which is its registered tripwire condition. Will rules.	FORUM/2026-08-10_positioning-exhaustion/04_synthesis/01_SAM_joint-synthesis-FINAL.md SS7 N10 (Will-ruled 8/11) + AGENTS/ORACLE/domain/sources/2026-09-07_v4-instrument-succession-DECISION-BRIEF.md	L172 rewrite trigger 9/08 is SPENT — it fired, ORACLE delivered, and the deadline it guarded was aimed at a death that did not happen. The live deadline is the OCTOBER roll ~2026-09-28 (Nov-CL window opens; the Sept market ends 2026-10-01). If Will rules before then, this row closes early.
```

**Suggested tombstone annotation for L172** (PROME's call, PROME's edit): `SUPERSEDED 2026-09-07 by the EOF row above — premises falsified (leg rolled 8/27, Sept market exists, Kalshi lane live); ORACLE options DELIVERED; awaiting Will's word.`

---

## 6. RESIDUE — declared, not fixed

- **Direction of the Active-Month level shift is UNSTATED** (needs the WTI curve shape; BRENT's, not mine). Registered, not asserted.
- **The 8/11→8/27 listing lead time is n=1.** Not a schedule.
- **The October WTI $100 market has NOT been searched for** this session — the roll deadline (~9/28) is registered on the assumption it will list, which is the same inference option A was criticised for. **Explicitly flagged so the next session searches rather than assumes.**
- **`VX-ORC-04`'s critical band `Iran-crude <2.0mbpd = real loss` is fireable again** but its rung is OI 10 — the band is technically live and practically unmarkable. Not re-keyed by hand; flagged.
- **The 9/4 "Iran-crude gauge is gone" claim may have travelled** in the 9/4 STATUS/NEXUS_BRIEF read by peers. Retraction is in this session's STATUS and NEXUS_BRIEF; no consumer packet sent because no peer cited it back to me. SEARCH-NOT-FOUND, not VERIFIED.
