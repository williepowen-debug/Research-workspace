# PRE-PRINT RECORD — 9/17 10Y TIPS-R `91282CRE3` · SEP-vs-path grade (`KB-BND-283` falsifier) · F2 per-op carrier scope

**Written 2026-09-17 08:2x–08:4x ET — BEFORE the 1:00PM ET TIPS print. Committed pre-print deliberately.**
**Author:** BOND · **Driver:** PROME WQ-184 L0 Tier-1 spawn (`prome-ae`) on `PROME/DOCKET.tsv` **L404** (dated today) + **L401** (9/16); inbox item `2026-09-16_from-PROME_morning-decision-work.md` (SEP assessment + F2 carrier).
**Purpose:** state the frozen bars and the pass/fail arithmetic before the result exists; grade the SEP against the falsifier registered 9/14; and record what the F2 letter does and does not owe since 9/10 — all before anything prints today.

> ⛔ **NO TIPS RESULT IS ASSERTED IN THIS FILE.** TA_WS returns `91282CRE3` for 2026-09-17 with no `competitiveAccepted` — the primary itself says PENDING. Every TIPS figure below is a BAR or a PRIOR print.

---

## 0 · WHAT WAS VERIFIED, AND HOW (not carried)

| Claim | Status | Instrument |
|---|---|---|
| TIPS bars frozen **pre-print** | **VERIFIED** | `git log -S "56.08" -- docket/CATALYSTS.tsv` → `742d4533e`, **2026-09-09**, eight days before the print. The bytes' commit date, not a header claim. |
| Frozen bars still **reproduce** | **VERIFIED** | `grade_auction.py --cusip 91282CRE3` re-run 08:2x ET → window `2024-09-19 → 2026-07-23`, **n=12**, ind min **56.08** / dlr max **17.79** / BTC min **2.20**; medians ind **66.94** / dlr **10.64** / BTC **2.40**; means 65.76 / 10.90 / 2.39; ind max 71.94, BTC max 2.52. Identical to the frozen row. |
| Size | **VERIFIED** | TA_WS: **$19B**, reopening=Yes, 9-Year 10-Month, competitive close 1:00 PM, settles 9/30. |
| FOMC decision | **VERIFIED at two primaries** | federalreserve.gov statement 9/16: **+25bp to 3.75–4.00%, 12–0**, no forward-guidance sentence, "continuing … ample reserves". FRED `IORB` **3.90 [2026-09-17]** (3.65 → 3.90 = the hike in the administered rate). |
| SEP medians | **VERIFIED** | federalreserve.gov `fomcprojtabl20260916`: FFR median **4.1 (2026) · 4.1 (2027) · 3.9 (2028) · 3.2 LR**; core PCE 3.4 / 2.5; U-3 4.1 / 4.1. Dots end-2026: 4.375 ×4 · 4.125 ×12 · 3.875 ×2. End-2027: 4.375 ×8 · 4.125 ×6 · 3.625 ×3 · 3.125 ×1 (median = avg of 9th/10th = **4.125** ✓). |
| H.15 frontier | **VERIFIED** | FRED cache-busted 08:2x: nominals + `DFII10` through **9/15**; `T10YIE`/`T5YIFR` through **9/16**. **No 9/16 Treasury cell exists yet** (~16:15 ET today). |
| 10Y TIPS stop history | **VERIFIED, computed not asserted** | TA_WS `type=TIPS`, 10Y original term, **n=139 (1997-01-29 → 2026-07-23)**: the 7/23 stop **2.438%** is the highest since **2008-10-08 (2.85%)**; series max 4.338 (2000-01-12). ⇒ a stop **>2.438** today is the highest 10Y TIPS stop since Oct-2008; **>2.85** would be the highest since **2002-07-10 (3.099)**. |
| Buyback ops since 9/10 | **VERIFIED at FiscalData** | 9/15 = **TIPS** LS op, 10Y–30Y, $500M of $2.088B offered · **9/17 = Nominal LS op, 7Y–10Y, cap $4B** (announcement row; results ~2:15 PM). **Neither is a stepped-up 10–20Y / 20–30Y op.** Issuer PDF (dated 9/9) parsed per-page and sanity-checked on three rows. |

---

## 1 · THE FROZEN BARS — 10Y TIPS-R `91282CRE3`, $19B, 1:00PM ET

**Frozen 2026-09-09.** Trailing-12 **10Y TIPS only** (new + reopenings), strictly prior, `2024-09-19 → 2026-07-23`, n=12. **Unit: % of COMPETITIVE ACCEPTED.** Never benchmarked against nominals — different buyer base.

| Leg | Bar | Fires when | Consequence |
|---|---|---|---|
| **Composition (conjunctive)** | ind < **56.08** AND dlr > **17.79** | both legs, same print | 🟠 TIPS composition marker → outbound to LIQUID/ZHAO at 🟠 (PROTOCOL row; TIPS variant). ⚠️ Both legs are single-print trailing-12 extremes (the ind min 56.08 is the 2025-09-18 reopening; WHICH print sets the dealer max 17.79 was not verified at authorship — the two extremes may or may not share a print) — a narrow gate, named now, not after it fails to fire. |
| **Cover marker** | BTC < **2.20** | with composition intact | 🟠 — and **say the mechanism did not fail** (the 7/27 lesson). 2.20 IS the trailing-12 min (9/18/25). |
| **Medians (reference)** | ind 66.94 · dlr 10.64 · BTC 2.40 | — | above-median indirect = real money took the higher real yield with less dealer help. |
| **`I'`** | ⛔ **NONE** | — | TIPS are outside the MATRIX_V2 kill. **Not a downgrade-counter print (counter stays 0).** |
| **Real stop vs the add-gate** | read, not a gate | — | `DFII10` **2.62 [9/15]**; a stop ≥2.60 prints the real yield the gate fired on **as an auction-cleared level**, which the gate letter never required and which nothing on this desk turns into an add (WQ-246 sustain count still with Will; 7/16 NO-ADD; root rule #5). |

**Most recent same-instrument prints:** 7/23 new issue $21B — ind 65.16 · dir 24.98 · dlr 9.86 · BTC 2.30 · **2.438%** · 5/21 reopening $19B — ind 61.4 · dlr 11.1 · BTC 2.52 · 2.169%.

**Reference points on the same axis:** ind median 66.94 · 7/23 65.16 · 5/21 61.4 · **bar 56.08**. A repeat of 7/23 fires nothing.

### Distances that decide it
- Composition fires only if indirect falls **≥9.08pp below the 7/23 print** AND dealers take **≥7.93pp more** than on 7/23 — both in one print.
- Cover fires at BTC < 2.20: the 7/23 print (2.30) was **0.10 above** the line; the 5/21 reopening (2.52) was 0.32 above.

## 2 · WHAT TODAY CANNOT DO
No kill leg exists here, no counter moves, no add re-arms. A weak print is a **🟠 TIPS marker** and a data point on real-yield demand; a strong print is "real money buys 2.6% real" — consistent with, not evidence for, the duration thesis. **Grade composition, never the tape.** No tail may fire anything (retired 7/28, unscoreable).

## 3 · CONTEXT THAT TRAVELS WITH TODAY'S PRINT (stated pre-print so it cannot be promoted later)
- **Day-after-FOMC + a 7% Brent drop the same morning** (BZ=F $98.37, −7.05% at 08:3x, BRENT's lane): breakevens already fell 5bp on 9/16 (`T10YIE` 2.38 → **2.33**; `T5YIFR` 2.35 → **2.31**) and an oil collapse pushes them further. **A TIPS auction on a falling-breakeven day is a real-yield-UP tape** — a soft print today has a non-structural explanation available and I will not read a demand hole into it.
- **The 9/17 7Y–10Y buyback op runs 1:40–2:00 PM** — 40 minutes after the TIPS close; it touches nominal 2033–2036 paper, not TIPS. No contamination of the TIPS composition read; post-1:40 nominal tape is contaminated for the 7Y–10Y sector.

---

## 4 · SEP-vs-PATH GRADE — `KB-BND-283`'s pre-registered falsifier

**The falsifier as registered 9/14:** *"a SEP median terminal at or above ~5.00% with the curve unchanged would show the hawkish path was NOT fully priced and the asymmetry claim is wrong."*

| Leg | Value | Verdict |
|---|---|---|
| SEP median terminal | **4.125%** (end-2026 = end-2027 median; 2028 median 3.9 ⇒ cuts pencilled for 2028, none for 2027) | **Falsifier NOT TRIGGERED** — the SEP terminal is **~88bp BELOW** the ~5.00 trip, and **60–85bp BELOW the curve's own implied terminal (4.75–4.95, 9/10 basis)**. |
| Curve reaction 9/16 (vendor closes, `^IRX ^FVX ^TNX ^TYX`) | 3M **+1bp** (3.96→3.97) · 5Y **+3.3bp** (4.826→4.859) · 10Y **+1.0bp** (4.996→5.006) · 30Y **−1.5bp** (5.364→5.349) · TLT **+0.21%** · TIP **−0.38%** · MOVE 83.7→80.7 | **UNCHANGED-TO-HIGHER** on vendor closes. ⚠️ Official grade waits on the 9/16 H.15 cells (~16:15 ET). |

**So the falsifier did not fire — and the branch that WAS tested went the other way.** My 9/14 asymmetry read said a dovish plot (*terminal <4.75, or cuts pencilled*) *"is a large repricing"* that would unwind the move that fired the add-gate. **The SEP came in dovish on exactly that definition — median path 4.125 with 2028 cuts — and the curve did not reprice: belly +3bp, breakevens −5bp, TIP ETF down, TLT up 0.2%.** The curve is holding a policy path **60–85bp above the Fed's own median** through the one event that could have re-anchored it.

**Read (working model, not truth):** the priced path is a **market view, not a guidance view** — the 4.8-ish terminal is the market pricing that the Committee will have to do more than its dots say (core PCE median 3.4 for 2026 against a 4.1 terminal is a projected real policy rate of ~+0.7; the curve prices ~+1.2 on the same inflation). That is a **credibility/inflation-risk spread between the dots and the curve**, and it lives in the same real-rate leg that fired the add-gate. **Consequences, each stated as a distance not a call:**
1. The "dovish SEP unwinds the add-gate move" risk **did not materialise on the day it was scheduled to.** `DFII10` 2.62 [9/15]; TIP −0.38% on 9/16 says the real leg rose again (INFERRED from the ETF — the 9/16 `DFII10` cell is not published; do not quote a level).
2. **`GATE-TERRY-007`** (five DGS10 closes <4.50): DGS10 **5.00 [9/15]**, vendor 5.006 [9/16] — **50bp** from the line; the "only realistic near-term route" (a dovish-SEP rally) came and delivered −0bp. The exit gate is **further**, not closer; TERRY's lane, stated not proposed.
3. **`BND-26`** (1y1y fwd does NOT close ≥4.95 on any session 9/16–9/23): the 9/15 official cell computes to **2×4.67 − 4.39 = 4.95 exactly — one day before the window opens.** Whether the row is dead on its first day is decided by the 9/16 `DGS1`/`DGS2` cells at ~16:15 ET. Registered 70% and now sitting on the line; **the direction of the miss will be reported with the number, not tidied.**
4. **`BND-25`** (belly-led on the FOMC session): vendor proxies say belly (5Y +3.3 vs 10Y +1.0, 30Y −1.5, 3M +1.0) — **not resolved on proxies**; the letter is the CMT set. Grade at the H.15 post.
5. **C-36 read holds:** no front-end rally on a dovish median (2Y vendor n/a; 3M +1bp) — the policy-path channel is transmitting **and** the curve is ahead of the Fed. Not a label change.

**What would change this read:** the 9/16 H.15 cells showing a belly rally ≥8bp (a repricing the vendor bars missed), or the 9/17–9/18 sessions delivering the rally with a one-day lag (the Brent −7% morning is a confound in the SAME direction as a dovish SEP — lower breakevens, so a real-yield read must separate the two before crediting either).

---

## 5 · F2 PER-OP CARRIER — L401 scope, and what has been owed since 9/10

**The letter (RED-FT-11 / DOCKET L235):** *BOND routes the F2 read per op* for the **stepped-up long-end nominal liquidity-support ops (sb0607: 10Y–20Y and 20Y–30Y, ≥$4B/op, 9/9 → 11/4)**. FT-11 reads nominal benchmarks; F2 is per-op CUSIP concentration on those ops.

**Ops in the window at the FiscalData primary, classified:**

| Date | Op | In scope? | F2 read |
|---|---|---|---|
| 9/10 | Nominal LS **10Y–20Y**, cap $6B | ✅ | **ROUTED 9/10** (RED inbox, verified by RED at the primary) — ledgered |
| 9/15 | **TIPS** LS 10Y–30Y, $500M of $2.088B | ❌ security type | none owed — listed, not dropped |
| **9/17** | Nominal LS **7Y–10Y**, cap **$4B**, 10 eligible (2033-11 → 2036-02) | ❌ not a stepped-up sector | none owed — results ~2:15 PM today will be recorded as context only |
| 9/24 · 10/1 · 10/8 · 10/15 · 10/27 · 11/4 | 20–30Y · 10–20Y · 20–30Y · 10–20Y · 20–30Y · 10–20Y, each ≥$4B (issuer PDF 9/9) | ✅ | **SIX reads to come**, one per op, routed as each publishes |

⇒ **Answer to L401's open count: ZERO in-scope ops have run since 9/10; ZERO reads are individually owed today.** The obligation was not silently missed between 9/10 and now — there was nothing in scope to route. **The gap was structural (no carrier), not an arrears.**

**The carrier, built this session:** `monitors/buyback_f2.py` (+ `registry/f2_reads.tsv` ledger, + `monitors/fixtures/buyback_20260910.json`), **invoked from `boot_recompute.py` every boot** so it needs no memory. Semantics: rc=1 = an in-scope op has PUBLISHED with no ledgered read (fail loud); rc=0 = nothing owed *now*; rc=2/GAP = fetch failure. Out-of-scope ops are listed with the reason, never dropped. `--op DATE` renders the RED packet; `--history` base-rates the metric. **Metric declared (BOND, not Will-ruled): recent_share = accepted par in the newest quartile of the eligible list by maturity ÷ total accepted; ON-THE-RUN fires iff > 50% (strict). Base rate 0 of 52 long-end LS ops since 2024-06-05 (max 47.4%, the programme's first op; median 0.0%).** Selftest 22 assertions: the real 9/10 op reproduces RED's 75.09% / 71.39%; wrong-owner (TIPS, 7Y–10Y, cash-mgmt) excluded; missing-information (announced, null results) not owed today / owed if past; overlap (ledgered) not owed; positive direction (75% fires, exactly 50% does not); schedule-vs-feed both ways. **IMPLEMENTED ✅ · TESTED ✅ (author's suite) · INDEPENDENTLY VERIFIED ❌** — the neighbour case *concurrent activity* is N/A (single writer, append-only ledger).

---

## 6 · LIVE MARKET STATE AT AUTHORSHIP (root rule #4)

FRED cache-busted 08:2x ET · yfinance closes.

| Series | Level | Date | Note |
|---|---|---|---|
| `DFII10` | **2.62** | 9/15 | 2.55 · 2.60 · 2.60 · **2.62** for 9/10–9/15 ⇒ **`BND-29` RESOLVES TRUE** (≥3 of the first 5 published sessions ≥2.50 is met at 4-of-4, whatever 9/16 prints). 98.8th pctile full series (n=5,930) |
| `DGS10` / `DGS30` / `DGS20` | **5.00 / 5.36 / 5.40** | 9/15 | 10Y at 5.00 = 50bp from GATE-TERRY-007's line; 20Y still above 30Y |
| `DGS2` / `DGS1` | 4.67 / 4.39 | 9/15 | 1y1y = **4.95** (see §4 item 3) |
| `T10YIE` / `T5YIFR` | 2.33 / 2.31 | **9/16** | −5bp / −4bp on FOMC day |
| HY / CCC / BB / IG OAS | 276 / **1085** / 161 / 80 | 9/15 | CCC **15bp** from the 1100 line (`BND-27`, 65% on the no-breach side); CCC−BB 924 |
| `IORB` | **3.90** | 9/17 | the hike, at the administered rate |
| TLT / TIP / MOVE | 80.88 (+0.21%) / 105.39 (−0.38%) / 80.73 | 9/16 close | |
| Brent / VIX | $98.37 (−7.05%) / 15.70 (−11.35%) | 9/17 08:3x | BRENT/VIOLET lanes; cited for the breakeven confound only |

## 7 · WHAT I WILL DO AT 1:00PM, IN ADVANCE
1. Pull `91282CRE3` at TA_WS; recompute ind/dir/dlr as % of competitive accepted **from raw dollar fields**.
2. Grade against §1 exactly as frozen; margins in pp on every leg; state the real stop vs `DFII10` and vs the n=139 history (computed above).
3. **Counter unchanged (TIPS never count). No `I'`. No add. No trade action.**
4. ~2:15 PM: record the 7Y–10Y op result as context (out of F2 scope; no packet to RED); re-run `buyback_f2.py --pending`.
5. At ~16:15 ET, if still live: grade `BND-25`/`BND-26` on the 9/16 H.15 cells and re-run the SEP curve leg on officials. If the session ends first, **those two grades are OWED and unexecuted, and this file says so.**

**If the session ends before 1:00PM, the TIPS grade is OWED and unexecuted — this file says so rather than inferring the print.**
