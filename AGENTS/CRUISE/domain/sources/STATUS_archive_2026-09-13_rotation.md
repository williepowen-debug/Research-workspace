# CRUISE STATUS — rotated blocks, 2026-09-13

**Rotated VERBATIM out of `AGENTS/CRUISE/STATUS.md` on 2026-09-13 ~12:3x ET** for the 32,550 B read-cap budget (`scripts/read_cap_check.py --agent CRUISE` read 107% of budget after the CRU-05 grade block landed). ⛔ **Nothing here was rewritten, re-dated or re-graded — the text is byte-identical to what STATUS carried.** Both blocks are **2026-09-02 vintage**: their figures are 9/2 closes and were already superseded as a tape read before this rotation. ⛔ **Historical — do not cite any level here as current** (root rule #4). The permanent record is `workbook/KB.tsv` KB-CRU-028..KB-CRU-037.

---

## A — the 9/2 prior-session block (what changed while the desk was dark 8/14 → 9/2)

> **⚠️ PRIOR SESSION (9/2) — WHAT CHANGED WHILE THIS DESK WAS DARK 8/14 → 9/2 (19 days), and the 8/14 headline finding is FALSIFIED.** *(Kept as the standing evidence base for both rulings above; its figures are 9/2 closes, superseded as a tape read by item 6.)*
> The 8/14 STATUS said *"the fuel tape has NOT priced through into CCL's stock… CCL is $28.28, up-drift from $27 despite Brent doubling."* **The lag closed, hard.** Closes 8/14 → 9/2: **CCL $28.12 → $23.74 (−15.6%)**, **RCL $305.00 → $265.60 (−12.9%)**, **NCLH $19.01 → $15.57 (−18.1%)**, against SPY −1.4% and XLY −2.8%. CCL made a 4-month low $23.23 on 9/1. (KB-CRU-033)
> **⛔ BUT THE DRAWDOWN DOES NOT RANK BY FUEL HEDGING, AND THAT IS THE SESSION'S FINDING.** Hedge ratios FY26: **CCL 0%** (now verified), NCLH 52%, RCL 58%. A fuel-driven move should hurt CCL most. Observed: **NCLH −18.1% > CCL −15.6% > RCL −12.9%** — CCL's excess over RCL is **2.7pp against a 58-point hedge gap**, and NCLH's excess is idiosyncratic. It is a **common-mode sector de-rate ordered by demand tier**, not a CCL-specific unhedged-fuel effect. (KB-CRU-034, VX-CRU-06)
> **Three primaries pulled this session closed three open questions and corrected one fleet figure by 2.7×** — see "What the primaries settled" below.


---

## B — What the primaries settled (9/2 session)

## What the primaries settled this session

Three documents, none of them read before today, closed three questions the 8/14 STATUS listed as owed and corrected one number the fleet was carrying.

**1. "CCL is unhedged" — VERIFIED, was a 7/2 assertion carried two months.** FY25 10-K Note 10 *Financial Risks — Fuel Price Risks*, in full: *"We manage our exposure to fuel price risk by managing our consumption of fuel. Substantially all of our exposure to market risk for changes in fuel prices relates to the consumption of fuel on our ships. We manage fuel consumption through fleet optimization, energy efficiency, itinerary efficiency, new technologies and alternative fuels."* **Zero occurrences of "fuel derivative"** in the 10-K or the Q2 FY26 10-Q; the only derivatives disclosed are FX and interest-rate swaps, all IR swaps terminated July 2025; the 10-Q adds *"no material changes to our exposure to market risks since the date of our 2025 Form 10-K."* Confidence: **VERIFIED**. (KB-CRU-028)

**2. ⛔ The fuel-sensitivity number this desk was using is ~2.7× too large.** `FLOW.tsv` FL-CRU-06 carried *"$145–156M net income hit per 10% fuel move"* — unsourced, inherited from the 3/20 boot thesis. **CCL's own published table says $56M (3Q26) and $102M (remainder-2026).** And the shape matters more than the level: in the same table **a 1% net-yield move is worth $60M in 3Q — MORE than a 10% fuel move.** At CCL's current scale, demand is the dominant P&L lever and fuel is second-order. (KB-CRU-029)

**3. The Q3 grading bar was set against the wrong perimeter.** The 8/14 watchlist pre-registered *"if CCL prints ≥$920/mt → fuel-drag confirmed"* — derived from **RCL $839 / NCLH $888**, which are *net-of-hedge* figures for *different fiscal quarters at differently-hedged companies*. **CCL published $812 for this exact quarter on 6/23** and it went unread. The Q3 print is graded against **$812**, full stop. The watchlist's companion inference — *"if ≤$860, CCL has hedging cushion I didn't know about"* — is now provably wrong: CCL has no hedges, so a low print would mean bunker/crude decoupling or purchase timing, never a hedge book. Both fixed in the watchlist. (KB-CRU-030/031)

---


---

## C — the 9/10 session's FIRST 9/3-base `VX-CRU-06` reading (superseded 2026-09-13)

**Rotated VERBATIM 2026-09-13.** Superseded by the 9/11-close reading (1.07pp, headroom 3.93pp) in the 9/13 STATUS block; permanent record KB-CRU-045. ⛔ Historical figures — the 9/10 closes are not current.

> 7. **✅ FIRST 9/3-BASE `VX-CRU-06` READING — NOT TRIPPED: 1.84pp against the ruled >5pp leg.** Four official closes, **own live pull** (`.venv/bin/python3 FORGE/tools/market-data/fetch.py price CCL|RCL` for the 9/10 closes + yfinance daily bars through the repo `.venv` for 9/3; 20:4x ET, markets closed): **CCL $23.48 [9/3] → $22.47 [9/10] = −4.3015%** · **RCL $265.55 [9/3] → $259.01 [9/10] = −2.4628%**. Excess = (22.47/23.48 − 1) − (259.01/265.55 − 1) = −4.3015 − (−2.4628) = **−1.8387pp**, i.e. CCL's excess **drawdown** over RCL is **1.8387pp — NOT TRIPPED**, 3.16pp of headroom. **Every in-window close is inside it too:** 9/4 **+0.26pp** (CCL *out*performed), 9/8 −0.80pp, 9/9 −1.14pp, 9/10 −1.84pp — max in-window excess drawdown **1.84pp** — so the test does not fire under *either* sampling reading. ⛔ **KB-CRU-043's 2.87pp is a 9/2 base and is NOT the graded reading.** (KB-CRU-045)

---

## D — the 2026-09-10 session block (three Will rulings encoded)

**Rotated VERBATIM 2026-09-13** for the read cap. ⛔ Historical: its tape figures are **9/10 closes**, superseded by the 9/11 closes on STATUS. **The RULINGS it encodes are live and are carried on STATUS elsewhere** — WQ-164 at § DOCKET L220, WQ-222 at exit rule #3, WQ-218 in `TRADE.md`. Permanent record: KB-CRU-038..KB-CRU-045.

> ## ⬛ PRIOR SESSION 2026-09-10 Thu ~18:0x-18:5x + ~20:5x ET — **INBOX DRAINED 6/6 THEN 1/1 · THREE WILL RULINGS ENCODED (WQ-164 · WQ-218 · WQ-222) · NO THRESHOLD OR CONVICTION MOVED · $0**
> **This block is the STATE.** No trade proposed, no capital, no vector re-scored. Every encode below is a ruling already made by Will; nothing here is a CRUISE judgement call.
>
> 1. **WQ-164 RULED (Will 2026-09-03 07:41 ET, verbatim *"Approve WQ-151 with your rec and WQ-164 retire"*) — the 7/2 arm-CCL fuel LADDER IS RETIRED, no replacement level.** `DOCKET L220` RESOLVED 9/3 on the word. *"Brent sustained >$85–90 = arm CCL"* is **kill-on-sight as a live trigger** from that date. **Fuel stays a tracked COST line** (VX-CRU-02, graded at CCL's own $812/mt at the Q3 print). Any future cruise trigger is a **NEW registration** keyed to the demand tier, two legs, drawdown clause — never a revival of this band. §L220 below and the disposition memo now carry the ruling stamp. (KB-CRU-038)
> 2. **WQ-218 RULED (Will 2026-09-10 20:45Z, Decision Deck tap) — the CCL FUEL-CONVEXITY FRAMING IS RETIRED.** Distinct from WQ-164: that retired the *ladder*, this retires the *framing*, which failed its own discriminator (unhedged CCL −15.6% fell LESS than 52%-hedged NCLH −18.1% over 8/14→9/2). **CCL stays a WATCH at conviction 2; NCLH stays a WATCH at conviction 3, no card** (spent edge, thesis intact). **No entry, no capital.** `TRADE.md` rows 5/13/14 encoded. (KB-CRU-039)
> 3. **✅ WQ-222 RULED (Will 2026-09-11T00:16:33Z = 20:16 ET 9/10, Decision Deck tap APPROVE on PROME's recommendation, no note) — THE `VX-CRU-06` EXCESS-DRAWDOWN FALSIFIER NOW HAS ONE NUMBER, ONE BASE AND ONE WINDOW.** **Number:** CCL excess drawdown over RCL **>5pp** — the WQ-164 packet's figure governs; the *"inside ~3pp"* text is **RETIRED and replaced** at exit rule #3 below, never annotated beside. **Base:** the **2026-09-03 official closes** (the WQ-164 ruling date) — a retirement is graded from the day it was ruled, so **the 8/14 base is not this test and its 5.01pp reading is retired, not carried forward**. **Window:** through the **CCL Q3 print** (~10/5 ESTIMATED, `DOCKET L221`; confirming primary = CCL's own conference-call release). **Sampling:** graded on **each in-window close at every CRUISE touch** — CRUISE's own letter (*"stays inside … through the Q3 prints"*) agrees with PROME's reading, so **ONE reading is encoded, not both**. **Consequence unchanged** — it is WQ-164's registered one: a fire means a CCL-specific drawdown existed; nothing new is armed. **First 9/3-base reading, computed live this session: 1.84pp — NOT TRIPPED**, 3.16pp of headroom (item 7). **$0, CCL/NCLH stay WATCH rows, no card, no score move, no new threshold.** (KB-CRU-044)
> 4. **FALCON's hostile-action total-loss count is NOT `VX-CRU-04`'s input — unit question answered at the ledger.** FALCON asked (9/7) whether its 1→2 move was a threshold input here. **It is not:** VX-CRU-04's band counts **Gulf itinerary CANCELLATIONS** (`1-5 · 5-15 · >15 or full season`), not vessel losses. Count verified at FALCON STATUS 9/10 as **3** (Kylo 9/5, Riesco 9/8) — already past FALCON's own 9/7 figure. **No score move**; the registered spec defect on this band stands unrepaired and un-scored. (KB-CRU-040)
> 5. **🔴 THE CRUISE-RELEVANT FINDING IN FALCON'S PACKET IS THE LINK THAT DIDN'T FIRE.** A hull was lost and **the listed war-risk area did not change**: BRENT re-probed the JWC/Lloyd's listing 9/7, HTTP 200, newest circular still **JWLA-034, byte-identical to its 9/1 probe**. This desk's transmission chain runs *incident → listing revision → premium → itinerary economics*; **the second link has not fired across two tanker sinkings.** `FL-CRU-02` re-based to the FALCON 9/10 vintage. (KB-CRU-041)
> 6. **Tape 9/10 (own pull, markets closed):** CCL **$22.47** (−1.01% d), RCL **$259.01** (−0.29%), NCLH **$14.57** (−1.89%). CCL is **−32.8% vs the named $33.45 pre-conflict reference** — still inside the −20/−35% ORANGE band, but the RED line (−35% ≈ **$21.74**) is now **$0.73 / 3.2% away**. VX-CRU-01 **HELD ORANGE(3)** on the letter. (KB-CRU-043)
> 7. **✅ FIRST 9/3-BASE `VX-CRU-06` READING (9/10 closes) — NOT TRIPPED at 1.84pp, max in-window 1.84pp.** ⚑ **Rotated VERBATIM 2026-09-13 for the read cap → `domain/sources/STATUS_archive_2026-09-13_rotation.md` § C**; permanent record KB-CRU-045. **Superseded as the latest reading by the 9/13 block item 5 (9/11 closes: 1.07pp, headroom 3.93pp).** ⛔ KB-CRU-043's 2.87pp is a 9/2 base and was never the graded reading.

