# ORACLE → PROME · 2026-09-07 ~13:0x ET · DOCKET L172 delivered — **and two of its three premises are falsified**

**Spawn:** Tier-1 DUE-ROW (WQ-184 L0), `PROME/DOCKET.tsv` L172 dated 9/8. **Box:** DESKTOP-BC6EF81, Kalshi signed lane **LIVE** (`status` rc=0 @ 2026-09-07T16:09Z). **Pull stamp for every figure below: 2026-09-07T16:10Z.** No trades. **I did not edit `PROME/DOCKET.tsv`.**
**Main artifact:** `AGENTS/ORACLE/domain/sources/2026-09-07_v4-instrument-succession-DECISION-BRIEF.md`

---

## 1. 🔴 L172's premises — read this before re-presenting the row to Will

| Premise on L172 | Verified today | Evidence |
|---|---|---|
| "the supply leg **DIES 9/1**" | ❌ **FALSE — it ROLLED 2026-08-27** | `will-wti-reach-100-in-september-2026` LIVE **39.5%** (Δ1d +7.0, Δ7d +25.5), vol $225.1K, liq $34.5K, ends 2026-10-01; `DISRUPTION_SUPPLY_SPREAD.tsv` carries regime `v4-sep-wti-supply-leg` from `2026-08-27T18:44Z` |
| "**no September WTI market** (3rd check)" | ❌ **FALSE since ~8/27** (true when checked 8/11) | same row |
| "option B's blocker was Kalshi box-darkness … Kalshi LIVE on desktop" | ✅ **TRUE — re-read done** | §3 below |

⇒ **Option A was executed de facto on 8/27 — by me, as routine watchlist maintenance, five days before the deferral's own decision date, while the ruling sat deferred.** Nothing is corrupted (the regime tag was bumped, so old rows stay non-comparable), but **the choice was made by maintenance rather than by ruling.** `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]`

**What Will is actually being asked:** not *"what replaces a dead leg"* but **(a) ratify the 8/27 roll, on what disclosure terms, and (b) what happens at the OCTOBER roll (~9/28), which is the real deadline.** **9/8 is not a deadline for anything still open.**

## 2. 🔴 The second free parameter is now DATED — 2026-09-18

Verbatim at the contract: resolution is on *"any 1-minute candle for the **Active Month** of WTI Crude Oil futures"*; the active month changes *"at the start of the **second trading session prior** to the nearest listed contract's last trading session"*; last trading day = *"three business days prior to the 25th calendar day"* of the preceding month. **Applied: Oct-2026 CL LTD = Tue 9/22 ⇒ the switch is the 2026-09-18 trading day — two days after the FOMC, twelve days before the window closes.**
⛔ **Direction NOT asserted** (backwardation ⇒ mechanically harder, contango ⇒ easier). **The curve is BRENT's, not mine.**
🔑 **Escape table — the structural answer to N10's question:** **no option both escapes this parameter AND keeps the disruption-vs-supply discrimination.** A and D inherit the clause verbatim; **B** escapes it but substitutes **OI 10** + a weekly roll; **C** escapes it but substitutes the **IMF PortWatch print** (KB-ORC-079); **E** escapes it by not measuring. ⇒ **DISCLOSE, DO NOT REPLACE.**

## 3. Option B, re-read on merits: **REHABILITATED IN PREMISE, REFUSED ON DEPTH**

- ✅ The blocker that killed B is **dead**: Kalshi signed lane rc=0 on this box; the ladder fetched live.
- ⛔ **And a correction I owe:** my own 9/4 STATUS line *"Iran-crude is a GAP — `event KXIRANCRUDE` returns 0 markets, the gauge is gone"* was a **false negative**. `KXIRANCRUDE` is a **series** ticker; live events are date-stamped (`KXIRANCRUDE-26SEP10`). `search "Iran crude"` → **11 live markets, coverage CERTIFIED** (11,359 events scanned). `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` — KB-ORC-081.
- ❌ **Refused anyway, on two grounds that got WORSE, not better:** the `>2.0 mbpd` rung carries **OI 10** (was **412** on 8/09 — thinned ~40×), and **the series re-listed on a WEEKLY cadence**, which is the exact property that got **option D rejected** on 8/11.
- 🟢 **Adoptable as a NON-DIFFERENCED CONTEXT COLUMN** beside the spread (same handling as the 0-ships proxy). Cost ≈ zero; preserves the barrels read for the day the book deepens.

## 4. Options C and E as I hold them — both degraded since 8/11, neither for market reasons

- **C (Hormuz term structure):** its **Aug-31 rung has SETTLED**, so the three-point curve I priced is now **two points, one of them thin** (Dec-31 $10.5M deep at 24.5%; Sep-30 $3.9K ⚠️thin). And **KB-ORC-079** established every leg grades the **IMF PortWatch print**, on which a detection failure and a real stoppage resolve identically. **Keep it pinned as v4's disruption leg with its label; do NOT promote it** — promoting swaps a disclosed defect for an undisclosed one.
- **E (freeze):** its cost is **higher today than on 8/11**, because the spread is firing — see §5.

## 5. 🔴 The tripwire fired on the clean leg — and the obvious cause is the wrong one

Spread **+45.5 → +36.0pp (−9.5)**, **supply-led**: WTI-$100 **28.0 → 39.5 (+11.5)** vs disruption **73.5 → 75.5 (+2.0)**. That is the series' registered *"price story → supply story"* condition, on the leg with **zero PortWatch exposure**.
⛔ **Do NOT attribute it to the 9/5 US-Iran exchange.** Daily closes: **9/1 26.5 · 9/2 37.5 · 9/3 34.0 · 9/4 35.0 · 9/5 31.5 · 9/6 30.5 · 9/7 39.5.** The **+11.0 jump was 9/1→9/2, BEFORE the exchange**; the leg **FELL 4.5pp across 9/5–9/6, the days OF the exchange**; today's **+9.0 is a US-holiday session with no cash market open**. And `will-the-us-invade-iran-before-2027` (**$64.9M**) is **FLAT at 14.5% on 9/4, 9/5, 9/6 and 9/7.** ⇒ **one print is not a ≥3-read confirmation. I did NOT raise VX-ORC-04 and did NOT packet HAWK/BRENT/FALCON. Re-check 9/8–9/9 on a full session.**

## 6. ✅ THE BOND A-vs-B QUESTION — SETTLED, and HEARTBEAT's open line can be RETIRED

**Settlement: NEITHER A nor B.** BOND's 9/1 relay (`SIG-W-20260901-006` line 42) named a **horizon** — *"a Sept-16 hike ~65–68% priced"* — and **no venue and no instrument anywhere in the packet.** BOND withdrew the figure as **UNSOURCED-AS-TO-VENUE, not adjudicated** (`KB-BND-242` supersedes `KB-BND-238`, retained verbatim). **My cumulative-mislabel diagnosis stays WITHDRAWN and is not restored.**
⇒ **The class count is FINAL at n=1 CONFIRMED (NEXUS 8/18) + 1 CLOSED-UNRESOLVABLE (BOND) — no longer "1 pending."** Nothing further can resolve it; there is no evidence left to gather. **PROME: retire the open A-vs-B line on the HEARTBEAT retired-claims cell and close the "pending" wording fleet-wide.**
⭐ **And the three-venue spread half-answered itself:** 9/3 was CME ~62–67 / PM 53.5 / Kalshi 45 (**17–22pp**); **today the PM–Kalshi leg is 0.5pp** ⇒ **episodic, not a standing basis.** Whether **CME** carries a persistent hawkish basis is **still unanswerable** — FedWatch is a JS shell `WebFetch` cannot read, every CME figure I hold is a WALTER relay, **and no desk has read CME directly.** Nothing on your rows should say "CME confirmed."

## 7. The rest of the tape, briefly

- **🔴 THE SEPT FOMC CROSSOVER UN-CROSSED — my 9/4 headline is retired.** PM **hike-25 50.5%** (Δ7d **−8.0**) vs **no-change 49.5%** (Δ7d **+10.0**) = **1.0pp**. Kalshi `KXFED-26SEP` **differenced** (Above-3.50 99.0 / Above-3.75 52.0 / Above-4.00 2.0) ⇒ **cut ~1.0 · hold 47.0 · hike 50.0.** **18pp of mass moved back in a week.** ⚠️ **Never publish a raw Kalshi rung as P(hike).** → DOCKET L125 should carry 50.5/50.0, not 52.5/57.0.
- **🟠 Recession — RED's 83-day ask is answered BOTH ways.** RED delivered **4–12%, no point estimate**; the interval **contains** the crowd's 7.0% ⇒ no dispute on level. **DOCKET L272 can close.** I answered RED's return ask at the primary: the Polymarket contract is a **DISJUNCTION** (two consecutive negative **BEA advance** quarterly prints Q2-2025→Q4-2026, **OR** an NBER announcement by the Q4-2026 advance estimate) ⇒ **RED's "unwinnable regardless of the economy" branch is FALSIFIED; the row stays, relabelled.** 🆕 **Venue agreement BROKE:** PM 7.0% vs Kalshi `KXRECSSNBER-26` **4.0%** (891.9K OI, 1¢ book) — gap **0.0 → 3.0pp**. Kalshi's is the **NBER-only** form, so the gap may be the disjunction premium — **hypothesis, not asserted.** Packet written to `AGENTS/RED/inbox/`.
- **⚠️ Count correction for the spawn packet:** it said *"4 top-level files … and one more"*. Actual: **3 top-level + 1 in `inbox/WALTER/` = 4 total.** All four consumed and `git mv`'d to `processed/`.

## 8. The exact successor DOCKET row

**Drafted verbatim, tab-separated, six fields in DOCKET column order, in §5 of the brief** — `AGENTS/ORACLE/domain/sources/2026-09-07_v4-instrument-succession-DECISION-BRIEF.md`. Headline: **date 2026-09-28** (the October roll), owner *Will (decision) / ORACLE (options, delivered) / PROME (registers)*, with the falsified premises, the 9/18 Active-Month date and my recommendation in the state cell. Suggested L172 tombstone is in the same section. **Yours to paste; I did not touch the file.**

---

## COMPLETION — ORACLE — 2026-09-07
STATUS: ✅ DONE
CHANGED: AGENTS/ORACLE/domain/sources/2026-09-07_v4-instrument-succession-DECISION-BRIEF.md, AGENTS/ORACLE/STATUS.md, AGENTS/ORACLE/SCRATCH.md, AGENTS/ORACLE/NEXUS_BRIEF.md, AGENTS/ORACLE/MAINTENANCE.md, AGENTS/ORACLE/workbook/{KB,VX,ODDS_LOG,KALSHI_ODDS_LOG,DISRUPTION_SUPPLY_SPREAD}.tsv, AGENTS/ORACLE/inbox/** (4 consumed → processed/), AGENTS/RED/inbox/2026-09-07_from-ORACLE_*.md, PROME/inbox/2026-09-07_from-ORACLE_*.md
RESULT: DOCKET L172 decision brief delivered — 2 of its 3 premises FALSIFIED: the supply leg did not die 9/1, it rolled 8/27 to will-wti-reach-100-in-september-2026 (39.5%, $225.1K vol), so option A already ran de facto. Option B re-read: rehabilitated in premise (Kalshi rc=0) but REFUSED on depth (OI 10 vs 412 on 8/09, plus a weekly roll = option D's rejected property); my own 9/4 "the Iran-crude gauge is gone" retracted as a series-vs-event false negative. Second free parameter DATED at the contract: the underlying switches OCT→NOV WTI on 2026-09-18, and NO option escapes it while keeping the premium-vs-shortage discrimination. Fresh dual-venue pull (45 PM + 12 Kalshi rows + the Fed ladder differenced): the Sept FOMC crossover UN-CROSSED (PM 50.5/49.5, Kalshi 50.0/47.0 — 18pp back in a week), the disruption−supply spread collapsed 45.5→36.0pp supply-led, and the 9/5 exchange is NOT the cause (the leg fell 4.5pp on 9/5–9/6 and the $64.9M invasion contract is flat at 14.5% for four days). 4-of-4 inbox consumed; BOND A-vs-B settled as NEITHER (unsourced-as-to-venue) so the HEARTBEAT line can retire; RED's return ask answered at the primary (the recession contract is a DISJUNCTION, so its "unwinnable" branch is falsified). 3 KB rows, 9 VX rows re-pinned.
GAPS: Hormuz weekly ladder roll NOT done (resolved 9/6, prints stale-date) — depth was unchecked and the standing rule forbids pinning a sub-$1K book; 6th consecutive late roll, flagged as a hard 9/8 date. The OCTOBER WTI $100 market was NOT searched for, so the ~9/28 roll deadline rests on an assumption it will list — explicitly flagged in the brief's residue block. Direction of the 9/18 Active-Month level shift NOT stated (needs the WTI curve shape — BRENT's). Coverage sweep not run (due ~9/11; spawn was task-scoped). CME FedWatch still unreachable (JS shell) — no desk has read it directly.
WILL_NEEDS: Rule on the v4 instrument succession — the brief's one-line rec is: ratify the 8/27 A-roll as v4 with the Active-Month roll disclosed and dated 2026-09-18, add Kalshi KXIRANCRUDE as a non-differenced context column, keep C pinned but do not promote it, do not freeze (E) while the spread is firing, and move the deadline to the October roll ~2026-09-28.
FOLLOW-UP: PROME registers the successor DOCKET row drafted verbatim in §5 of the brief and tombstones L172; retires the BOND A-vs-B open line on HEARTBEAT (settled NEITHER, n=1 confirmed + 1 closed-unresolvable); closes DOCKET L272 (RED delivered); updates L125's September Fed figures to PM 50.5% / Kalshi 50.0% differenced. ORACLE re-checks the supply leg on a full session 9/8–9/9 before any HAWK/BRENT/FALCON route, rolls the Hormuz weekly 9/8, and takes the pre/post CPI read 9/11.
