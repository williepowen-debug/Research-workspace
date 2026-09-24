# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension; + the sovereign-credibility instrument set per the 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-24 Thu ~13:00→ ET (Will boot, `bond-b0`; markets OPEN) — **first session since 9/17; BOND was dark 9/18–9/23** · **Prior:** 2026-09-17

> 📕 **HOT/COLD SPLIT — NOTHING DELETED.** Full pre-rewrite snapshot of the 9/17 file: `domain/sources/2026-09-24_STATUS_full-snapshot_pre-9-24-rewrite.md` (23,719 B, crc32 `2559402921`). Older rotations: `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md` and `domain/sources/2026-09-1*_STATUS_*`. **Budget 32,550 B — rotate, never raise.**

**Canonical elsewhere — no second copy here:** thesis → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalysts → `docket/CATALYSTS.tsv` · gates/positions → `TRADE.md` · learnings → `MEMORY.md` · handoff → `SCRATCH.md`.

---

## 🔴 TOP OF FILE — what changed since 9/17

1. 🔴 **9/23 5Y `91282CRN3` = OLD CONJUNCTIVE COMPOSITION FAILURE** — indirect **54.31%** (min 59.24; **lowest 5Y since 2020-03-25**) AND dealer **15.77%** (max 15.61, **+0.16pp**) · BTC **2.21** (lowest since 2018-12-26) · `I'` fired. ⇒ **the TLT-put ADD RE-ARM condition is MET — and Will DECLINED the add (WQ-280, ruled 13:17 ET 9/24, verbatim *"Approve WQ-280 and WQ-281 with your recs"*); no trade, no fresh card approved; `$0`.** ⛔ **Paired thesis kill NOT fired** (SOFR−IORB **−3bp** [9/23]). ⚠️ **Dealer 15.77 is ordinary on multi-year history (five 2023–24 prints higher, max 20.37); it cleared into a hot-PMI sell-off. THRESHOLD FIRED — MECHANISM NOT SHOWN FAILED.** Graded ~24h late. → `analysis/2026-09-24_GRADE_month-end-cluster_2Y-5Y-7Y.md`, `KB-BND-312`.
2. 🟠 **9/24 7Y `I'` marker by 0.037pp**; 9/22 2Y 🟢 clean. Downgrade counter **0**.
3. 🔴 **`BND-26` FALSE (70%, a MISS):** 1y1y **5.03 on FOMC day**, 5.08 [9/18] = new 2023-forward sample high. **This desk's 9/14 "a hawkish SEP has little room to surprise" is WITHDRAWN; the 4.75–4.95 terminal band is retired for reuse.** `BND-25` TRUE (55%). `KB-BND-315`.
4. 🔴 **9/23 OFFICIAL CURVE (U.S. Treasury par/real curves — the identical source of H.15: 182/182 exact 2026 matches on DGS30/10/2 and DFII10, verified 9/24): 30Y 5.40 = FRESH 2026 HIGH, highest since 2004-07-28 · 10Y 5.11, highest since 2007-07-13 · 2Y 4.85 · 10Y REAL 2.76 (+13bp d/d), highest since 2008-11-25 — 33 of 5,935 days ever ≥ it.** ⇒ matrix row 1's letter ("fresh DGS30 high WITH weak composition") FIRED on 9/23 ⇒ **row 1 3→4, composite 14/35.** ⚠️ The weak composition that day was the 5Y, not a long-end auction; the upgrade confirms this desk's own thesis — scored on the letter, disclosed. FRED republishes the same cells ~9/25.
5. 🔴 **The macro tape:** 9/23 flash composite PMI **58.4** (highest since 7/2021), input prices fastest since 10/2022 (S&P Global, secondary reports) ⇒ 5Y crossed **5%** first time since 2007; vendor 10Y **5.14**, 30Y **5.43** intraday 9/24 (**above the 5.37 official 2026 high — vendor, NOT counted**); October hike ~70% priced (TE 9/24, secondary). BOJ hiked to 1.25% 9/18; press-reported Japanese rate check ~¥158 (unconfirmed). BoE paused APF gilt sales 9/17 (a long-end SUPPLY withdrawal — `KB-BND-317`).
6. 🟠 **CCC 1093 [9/23] fresh 2026 high, 7bp from 1100**; CCC−BB **934** > the 926 span max. HY index 273, inert.

---

## Regime (one-line)

**Real-rate / higher-for-longer — and the policy path is still repricing HAWKISHLY.** C-36 TWO-PART (ruled 9/1): policy-path channel ALIVE · term premium drove the July delta. **9/16 FOMC +25bp to 3.75–4.00 (12–0); the curve priced ABOVE the SEP median (4.125) and then kept going (`BND-26`).** **Auctions: "expensive, not broken" is UNDER TEST — first OLD-conjunctive fire on this desk's LIVE-graded record (KB searched 9/24; out-of-sample base rate 4/224 = 1.8%), on a macro sell-off day, with calm funding.** Full ruling → `thesis/THESIS.md` v1.2.7.

---

## Current Dashboard

*Pulled live **2026-09-24 13:01–13:10 ET** via `monitors/boot_recompute.py` + `fetch.py` (cache-busted) unless tagged. No naked numbers.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.40%** | 🔴🔴 | [CONF **U.S. Treasury par curve 9/23** = the H.15 source, 182/182 identity; FRED 5.29 [9/22]] — **FRESH 2026 HIGH (prior 5.37 [9/10]); highest since 2004-07-28**; run ≥5.00 = 56. Vendor `^TYX` 5.434 [9/24 intraday] |
| 10Y (DGS10) | **5.11%** | 🔴 | [CONF Treasury par curve **9/23**] — highest since 2007-07-13; `GATE-TERRY-007` **61bp** from 4.50. Vendor `^TNX` 5.137 [9/24 intraday] |
| 5Y (DGS5) | **4.99%** | 🔴 ↑ | [CONF Treasury par curve **9/23**] — +16bp d/d (4.83 [9/22]); vendor `^FVX` 5.011 [9/24] |
| 2Y · 1Y | **4.85% · 4.49%** | 🔴 ↑ | [CONF Treasury par curve **9/23**] — 2Y highest since 2024-06-10; **1y1y 5.21 = new 2023-forward sample high** (prior 5.08 [9/18]; `BND-26` FALSE) |
| **10Y real (DFII10)** | **2.76%** | 🔴🔴 **GATE THROUGH** | [CONF **Treasury real curve 9/23**] — **+26bp above 2.50; +13bp d/d; highest since 2008-11-25 (33 of 5,935 obs ever ≥2.76)**; every published session ≥2.50 since 9/10. "Sustained" count = WQ-246 (Will) |
| 5Y5Y fwd (T5YIFR) | **2.36%** | 🟡 | [CONF FRED **9/23**, computed from Treasury curves] — **14bp from 2.50.** ⚠️ *Corrected 9/24 ~13:2x: an hour earlier this row called the 9/23 cell "provisional" on WALTER −011's mechanism, which was already retracted (LIQUID 9/22, WALTER −004 9/24); FRED builds it from Treasury BC_/TC_ data — a real value on Treasury's schedule (`KB-BND-320` CORRECTED)* |
| 10Y BE (T10YIE) | **2.35%** | 🟡 | [CONF FRED **9/23**] = 5.11 − 2.76 exactly — **the 9/23 move was REAL-led (+13bp real vs +2bp breakeven)** |
| ACM 10Y TP · KW TP | 0.7090 [9/15] · 0.9610 [9/11] | 🔴 `[STALE 9/24]` | Not re-pulled this session (re-pull at next full boot). KW 0.9610 = highest since 2011-02-11 at the time. **Name the model in any TP claim** (5.1bp model gap, `KB-BND-298/299`) |
| **HY OAS** | **273bps** | 🟢 | [CONF FRED **9/23**] — 27bp from the 300 reopen line; 2026 max 346 |
| **CCC OAS** | **1093bps** | 🟠 ↑ | [CONF FRED **9/23**] — **fresh 2026 high** (+18bp d/d; prior max 1085 [9/15]); **7bp from 1100** (`BND-27`) |
| IG OAS | **77bps** | 🟢 | [CONF FRED **9/23**] |
| CCC−BB tail gap | **934bp** | 🟠 ↑ | [CONF FRED, BOND computation **9/23**] — BB 159; **above the 926 span max** |
| **FR2004 long-end** | **$146.2B** [as-of 9/9] | 🟡 | [NY Fed via `fr2004_fetch.py`, 9/24] — **+$1.5B w/w** after −$7.1B; 11-21Y $66.8B flat, >21Y $43.4B, 7-11Y $36.0B; −16.5% off the 6/24 peak. One build ≠ the two-consecutive-builds trigger |
| **SOFR − IORB** | **−3bp** | 🟢 | [CONF FRED SOFR 3.87 · IORB 3.90, **9/23**] — funding calm through the 5Y failure. LIQUID owns the plumbing read (asked 9/24) |
| TLT · ^MOVE | **$80.05 −0.51%** · — | 🟠 | [yfinance **9/24 ~13:0x intraday** — a MOMENT property, re-pull at any decision, root rule #4]. TLT 81.80 [9/21] → 80.46 [9/23] → 80.05. ^MOVE not re-pulled (off-RTH fill-forward hazard, `SIG-W-20260919-001`) |
| UK 10Y · Bund 10Y · JGB | 5.29 [TE 9/18] · 3.50–3.52 [9/18] · MOF dark to ~9/24 | 🟠 `[HANS/SAM own]` | UK basis caveat: BoE IADB par 5.2421 [9/16] vs TE — **name the basis** (`KB-BND-319`) |
| USD/JPY · Brent · VIX | **cite SAM · BRENT · VIOLET** | — | this desk keeps no copy |

### Gate distances *(recomputed this session, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — TLT-put add-gate (a)** | 🔴 **THROUGH by 26bp** [2.76, 9/23 Treasury] | Level leg held every published session since 9/10. ⛔ "Sustained" count = **WQ-246 (Will)**; authorises no add |
| **Auction re-arm (OLD conjunctive) — TLT-put add-gate** | 🔴 **MET 9/23 (5Y)** | ✅ **ADD DECLINED — WQ-280 RULED 9/24 13:17 ET** (four §B.1 grounds, `TRADE.md` Reactivation Matrix). Spent on 004 |
| T5YIFR >2.50 | 14bp [9/23] | 🟡 |
| DGS30 >5.00 · DGS10 >4.50 | — | 🔴 BREACHED (run 56) · 🔴 BREACHED |
| `GATE-TERRY-007` (DGS10 <4.50 ×5) | 61bp [9/23] | TERRY's rail; counter 0 |
| HY OAS >300 (reopen HYG) | 27bp [9/23] | 🟢 |
| CCC >1100 escalation | **7bp** [9/23] | 🟠 closing |
| Credit-equity lead (HY +75–100 from the 263 trough) | 65–90bp | 🟢 inactive |

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **4** ▲ | 🔴 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | **9/23: DGS30 5.40 = fresh 2026 high ON the 5Y composition-failure day ⇒ upgrade letter FIRED ⇒ 4**; DFII10 2.76 (highest since 2008-11); 1y1y 5.21 | ⇒5: a composition failure on a LONG-END auction (20Y/30Y) or the paired kill's mechanism leg confirming |
| 2 | Treasury auction health | **3** ▲ | 🟠 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED (tail) | **9/23 5Y: BTC 2.21 < 2.28 cover bar (and <2.3 KEY-THRESHOLD cover marker) + OLD composition failure + `I'`; 7Y `I'` by 0.04pp.** Paired kill NOT fired (funding −3bp; FR2004 leg unevaluable ~mid-Oct) | A composition failure with the funding/FR2004 leg CONFIRMED (paired kill) ⇒ 4 |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | FR2004 9/9 long-end $146.2B (+$1.5B, one build); 5Y dealer 15.77 is the trailing-12 max but ordinary vs 2023–24. **9/24 20–30Y buyback: $4.078B of $6B, F2 0.02% ⇒ OFF-THE-RUN (2 of 2 ops)** | Two consecutive builds on TOTAL with weak composition, or SOFR−IORB positive; F2 ON-THE-RUN fire |
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `VX-BND-11` | HY 273 inert; **CCC 1093 fresh high, 7bp from 1100**; CCC−BB 934 new span max | HY >300 with velocity, or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 77 [9/23] | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF z20 +1.28 [9/8, STALE] | Synthetic leading cash, sustained |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — 65–90bp headroom | HY +75–100bp from 263 while VIX <20 |

**Composite: 14/35 — UP 2 (12 → 14), the first change in sixteen scoring sessions.** **Row 1 moved 3 → 4 on its registered letter** (fresh DGS30 high 5.40 with weak composition, 9/23 — scored on the Treasury par curve, identical to H.15 at 182/182; the weak composition was the 5Y, not a long-end auction; FRED confirms ~9/25). Row 2 moved **2 → 3 on a pre-registered rule, not a judgement**: the 5Y BTC 2.21 is below both its trailing-12 min (2.28) and the KEY-THRESHOLDS 2.3 cover marker, which "escalates the vector" (the 7/27 precedent, when the vector moved on a benign story because that is what pre-registration is for). **The KILL is a different test and did not fire.** Distribution: 🔴 1 · 🟠 1 · 🟡 2 · 🟢 3. **Re-summed: 4+3+2+2+1+1+1 = 14 ✅.** ⚠️ `VX.tsv` row-state write-back for `VX-BND-01` owed at closeout.

**Outside the composite:** `VX-BND-15` inflation anchoring (2) · `VX-BND-17` MBS relay (1) · `VX-BND-18` FHLB (2) · `VX-BND-19` EZ rates (3 — HANS: ECB T-04 no longer a hawkish lean; German 2027 debt service +38%; "disorderly" UNDEFINED → 10/1) · `VX-BND-20` benchmark UST demand (2, checkpoint 10/6).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 1** — `BND-27` (CCC <1100 through 9/30, 65%; **7bp away, 1093 [9/23], five sessions left** — momentum against it). **Resolved 9/24:** `BND-25` **TRUE** (55%) · `BND-26` **FALSE** (70%). Earlier: `BND-29` TRUE 9/17 · `BND-28` TRUE 9/15. **Tally: 14 TRUE · 12 FALSE · 1 VOID.** Archives: `thesis/archive/PREDICTIONS_resolved_*`. ⚠️ **No new predictions registered this session; the 10/28 FOMC curve-shape row is owed with a base rate by 10/21.**

---

## Trade Interface *(full view → `TRADE.md`; construction is TERRY's lane)*

- **TLT puts (Sep-30 77P ×20 — 5 of 25 sold 9/10, `FORGE/STATUS.md:54`) — HOLD, no add, `$0`.** 🔴 **BOTH add-gates now read through on their letters:** (a) DFII10 2.63 (sustain count WQ-246) and **the OLD-conjunctive auction re-arm (9/23 5Y)**. ⛔ **Neither is an add: WQ-280 RULED 9/24 — ADD DECLINED (Will verbatim *"Approve WQ-280 and WQ-281 with your recs"*); a fresh TLT card is NOT approved by that word; 7/16 NO-ADD; root rule #5.** **Expiry 9/30 = 6 days; harvest/roll is TERRY's.** *Posture, never a direction.*
- **HYG puts — closed at the INDEX level** (HY 273). CCC tail 7bp from 1100 → if it arms: single-name/CCC, **never HYG**.
- **Credit-equity lead — inactive.**

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all duration shorts).** WQ-157 leg ① (Will 9/4): **`I'` + a NON-AUCTION mechanism confirmation (FR2004 dealer stock and/or SOFR−IORB)** since 9/11. **9/23 5Y: `I'` fired; SOFR−IORB −3bp ⇒ funding leg UNMET; FR2004 leg needs the as-of straddling 9/23 (~mid-October) ⇒ KILL NOT FIRED, partly UNEVALUABLE.** Unpaired `I'` fires: 9/15 20Y-R · 9/23 5Y · 9/24 7Y. **WQ-157 leg ② still with Will** (the join found the pairing INVERTS, p=0.009; funding leg p=0.523; MDE ≈16bp; BOND recommends nothing). Also: 10Y back below 4.15 ×3 with clean auctions ⇒ spent.
- ⚠️ `I'` bars: `monitors/AUCTION_HEALTH.md` §GRADING BASIS. **Grader defect `KB-BND-314`: reopenings of older longer issues are pooled by ORIGINAL term (the Jan-2026 2Y sits in the 5Y pool) — verdict-neutral so far; fix before the 10/6 3Y.**
- 🔴 Direction disclosed: `I'` is the easier test and its firing confirms this desk's own bear thesis.

**2 · POSITION-SPECIFIC.** TLT puts: kill on 10Y <4.15 AND 30Y <5.0 ×3 sessions AND a clean refunding (THESIS §2). Expiry 9/30 is TERRY's rail.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal coupons passing both legs (indirect ≥ median AND dealer ≤ median). **Counter 0** (2Y failed the dealer leg 13.19 vs 11.33; 5Y and 7Y failed indirect). Next eligible: 10/6 3Y.

**4 · TIME-BASED.** H.15 9/23 cells (row 1) **9/25** · quarter-end + PCE + `BND-27` + expiry **9/30** · F2 reads **9/24 · 10/1 · 10/8 · 10/15 · 10/27 · 11/4** · quarterly `I'` refresh + `VX-19` definition + **F2 10Y–20Y vintage fix** **10/1** · `VX-20` **10/6** · FHLB Q3 **11/9** · FRBNY FX **11/13** · US-sov-CDS re-test **12/1**.

⚠️ **RETIRED, NOT REVIVABLE: the auction TAIL.** The 9/23 "2nd biggest tail ever" wire claim is `[med-conf]` and fires nothing.

---

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| ✅ **Thu 9/24 1:40 PM — READ & ROUTED** | **20Y–30Y buyback op: $4.078B of $6B cap (68%) on 1.74× offered; recent_share 0.02% ⇒ OFF-THE-RUN** | Packet → RED 9/24 ~14:1x; ledger row; `KB-BND-324`. Complete at read (35/35) |
| ✅ 9/22 · 9/23 · 9/24 | 2Y 🟢 · **5Y 🔴 OLD composition failure** · 7Y 🟠 `I'` by 0.04pp | Graded 9/24 (`KB-BND-312/313`) |
| ✅ 9/18 (carried) | `BND-25` TRUE · `BND-26` FALSE | `KB-BND-315` |
| ✅ **9/23 official curve (Treasury) — DGS30 5.40 > 5.37** | Row 1 letter FIRED ⇒ 4 | **Fri 9/25:** confirm FRED republishes 5.40 (identity check, not a new grade) |
| **Wed 9/30** | 🔴 **Quarter-end · Aug PCE + Q2 GDP 3rd (8:30) · `BND-27` window closes · TLT 77P expiry** | PCE vs the PMI input-price shock; SOFR−IORB across quarter-end; CCC vs 1100 |
| **Thu 10/1** | Quarterly `I'` refresh · `VX-19` "disorderly" · **10Y–20Y buyback op (F2 — vintage fix first)** · Oct refunding sizes | `AUCTION_HEALTH.md` §3d; `KB-BND-314` fix |
| **Fri 10/2** | Sept Employment Situation (8:30) | 2Y / 1y1y reaction |
| **10/6 · 10/7 · 10/8** | 3Y · 10Y-R · 30Y-R + 20–30Y op (F2) · `VX-20` review | bars frozen at the 10/1 announcement |
| **Wed 10/14 · 10/15** | Sept CPI (8:30) · 10–20Y op (F2) | breakevens on input-supported cells only |
| **10/21 · 10/22 · 10/26–29** | 20Y-R · 5Y TIPS · month-end cluster | bars at each announcement |
| **Wed 10/28 2:00 PM** | 🔴 **October FOMC** (~70% hike priced, TE secondary) · ECB 10/29 | register a curve-shape row by 10/21 |
| **10/27 · 11/4** | 20–30Y op · **QRA + 10–20Y op (F1/F3 resolve; sb0607 window ends)** | carrier + `VX-BND-16` |
| **11/9 · 11/13 · 12/1 · 2027-01-25** | FHLB Q3 · FRBNY FX · US-sov-CDS re-test · Norwegian MoF expert group | as docketed |
| **— STANDING —** | MOF FX intervention · Warsh task force · FR2004 weekly · credit weekly · F2 carrier every boot | `FL-BND-11` · `VX-04` · `VX-02/11` · `VX-16` |

---

## BOTTOM LINE

**[2026-09-24 Thu ~13:3x ET — boot after a six-day gap; markets open.]**

**The auction side just produced this desk's hardest test since the thesis was written.** The 9/23 5Y failed the strict two-part composition test: foreign-type buyers took their smallest 5Y share since March 2020 while dealers took the most in a year. That meets the pre-set condition for adding to the TLT puts. **Will declined the add at 13:17 ET (WQ-280); no trade.** The caveats that decide it: funding stayed calm (−3bp), dealers were not stuffed by any multi-year standard (they took more five times in 2023–24), and the print cleared on the day hot PMIs sold the whole curve off. **Threshold fired; mechanism not shown failed.** **And the long end broke out the same day: official 30Y 5.40 (highest since 2004), 10Y 5.11 (since 2007), and the 10Y real yield 2.76 — highest since November 2008, +13bp in one session, real-led.** That fires the long-end vector's registered upgrade. The rate path is also still repricing up: this desk's 9/14 view that the hawkish path was fully priced was **wrong** (`BND-26`). **Position: TLT 77P ×20 HOLD, no add, `$0`, expiry 9/30. Composite 14/35 (▲2). Counter 0. OPEN predictions 1.**
