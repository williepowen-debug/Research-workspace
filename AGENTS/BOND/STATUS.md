# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension; + the sovereign-credibility instrument set per the 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-24 Thu ~13:00→ ET (Will boot, `bond-b0`; markets OPEN) — **first session since 9/17; BOND was dark 9/18–9/23** · **Prior:** 2026-09-17

> 📕 **HOT/COLD SPLIT — NOTHING DELETED.** Full pre-rewrite snapshot of the 9/17 file: `domain/sources/2026-09-24_STATUS_full-snapshot_pre-9-24-rewrite.md` (23,719 B, crc32 `2559402921`). Older rotations: `archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md` and `domain/sources/2026-09-1*_STATUS_*`. **Budget 32,550 B — rotate, never raise.**

**Canonical elsewhere — no second copy here:** thesis → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalysts → `docket/CATALYSTS.tsv` · gates/positions → `TRADE.md` · learnings → `MEMORY.md` · handoff → `SCRATCH.md`.

---

## 🔴 TOP OF FILE — what changed since 9/17

1. 🔴 **9/23 5Y `91282CRN3` = OLD CONJUNCTIVE COMPOSITION FAILURE** — indirect **54.31%** (min 59.24; **lowest 5Y since 2020-03-25**) AND dealer **15.77%** (max 15.61, **+0.16pp**) · BTC **2.21** (lowest since 2018-12-26) · `I'` fired. ⇒ **the TLT-put ADD RE-ARM condition is MET — Will-gated as WQ-280, PROME rec DECLINE; 7/16 NO-ADD stands; `$0`.** ⛔ **Paired thesis kill NOT fired** (SOFR−IORB **−3bp** [9/23]). ⚠️ **Dealer 15.77 is ordinary on multi-year history (five 2023–24 prints higher, max 20.37); it cleared into a hot-PMI sell-off. THRESHOLD FIRED — MECHANISM NOT SHOWN FAILED.** Graded ~24h late. → `analysis/2026-09-24_GRADE_month-end-cluster_2Y-5Y-7Y.md`, `KB-BND-312`.
2. 🟠 **9/24 7Y `I'` marker by 0.037pp**; 9/22 2Y 🟢 clean. Downgrade counter **0**.
3. 🔴 **`BND-26` FALSE (70%, a MISS):** 1y1y **5.03 on FOMC day**, 5.08 [9/18] = new 2023-forward sample high. **This desk's 9/14 "a hawkish SEP has little room to surprise" is WITHDRAWN; the 4.75–4.95 terminal band is retired for reuse.** `BND-25` TRUE (55%). `KB-BND-315`.
4. 🔴 **The macro tape:** 9/23 flash composite PMI **58.4** (highest since 7/2021), input prices fastest since 10/2022 (S&P Global, secondary reports) ⇒ 5Y crossed **5%** first time since 2007; vendor 10Y **5.14**, 30Y **5.43** intraday 9/24 (**above the 5.37 official 2026 high — vendor, NOT counted**); October hike ~70% priced (TE 9/24, secondary). BOJ hiked to 1.25% 9/18; press-reported Japanese rate check ~¥158 (unconfirmed). BoE paused APF gilt sales 9/17 (a long-end SUPPLY withdrawal — `KB-BND-317`).
5. 🟠 **CCC 1093 [9/23] fresh 2026 high, 7bp from 1100**; CCC−BB **934** > the 926 span max. HY index 273, inert.

---

## Regime (one-line)

**Real-rate / higher-for-longer — and the policy path is still repricing HAWKISHLY.** C-36 TWO-PART (ruled 9/1): policy-path channel ALIVE · term premium drove the July delta. **9/16 FOMC +25bp to 3.75–4.00 (12–0); the curve priced ABOVE the SEP median (4.125) and then kept going (`BND-26`).** **Auctions: "expensive, not broken" is UNDER TEST — first OLD-conjunctive fire since the test was built (base rate 1.8%/auction), on a macro sell-off day, with calm funding.** Full ruling → `thesis/THESIS.md` v1.2.7.

---

## Current Dashboard

*Pulled live **2026-09-24 13:01–13:10 ET** via `monitors/boot_recompute.py` + `fetch.py` (cache-busted) unless tagged. No naked numbers.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.29%** | 🔴 | [CONF FRED **9/22**] — 2026 high 5.37 [9/10]; **55-session run ≥5.00** (maximal run, whole-series); 71 of 182 2026 sessions. **Vendor `^TYX` 5.401 [9/23 close] · 5.434 [9/24 intraday]** — a fresh official high on 9/23 is LIKELY and NOT counted until H.15 publishes (docketed 9/25) |
| 10Y (DGS10) | **4.96%** | 🔴 | [CONF FRED **9/22**] — 99.8th pctile post-2010. `GATE-TERRY-007` **46bp** from 4.50. Vendor `^TNX` 5.114 [9/23] · 5.137 [9/24 intraday] |
| 5Y (DGS5) | **4.83%** | 🔴 ↑ | [CONF FRED **9/22**] — vendor `^FVX` 4.997 [9/23] (+16bp from 9/21), 5.011 [9/24] |
| 2Y · 1Y | **4.71% · 4.43%** | 🔴 ↑ | [CONF FRED **9/22**] — **1y1y 4.99**; 5.08 [9/18] = 2023-forward sample high (`BND-26` FALSE) |
| **10Y real (DFII10)** | **2.63%** | 🔴 **GATE THROUGH** | [CONF FRED **9/22**] — **+13bp above 2.50**; run since 9/10 all ≥2.50, high **2.68 [9/18]**; 98.8th pctile full, 99.9th post-2010. "Sustained" count = WQ-246 (Will) |
| 5Y5Y fwd (T5YIFR) | **2.34%** | 🟡 | [CONF FRED **9/22**, last INPUT-SUPPORTED cell] — **16bp from 2.50.** ⚠️ FRED's 2.36 [9/23] is PROVISIONAL (inputs stop 9/22; WALTER −011, `KB-BND-320`) |
| 10Y BE (T10YIE) | **2.33%** | 🟡 | [CONF FRED **9/22**] = 4.96 − 2.63 exactly; 2.35 [9/23] provisional |
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
| **DFII10 ≥2.50 — TLT-put add-gate (a)** | 🔴 **THROUGH by 13bp** [2.63, 9/22] | Level leg held every published session since 9/10. ⛔ "Sustained" count = **WQ-246 (Will)**; authorises no add |
| **Auction re-arm (OLD conjunctive) — TLT-put add-gate** | 🔴 **MET 9/23 (5Y)** | ⛔ **Re-arm ≠ add.** WQ-280 with Will; PROME rec DECLINE; 7/16 NO-ADD; root rule #5 |
| T5YIFR >2.50 | 16bp [9/22] | 🟡 |
| DGS30 >5.00 · DGS10 >4.50 | — | 🔴 BREACHED (run 55) · 🔴 BREACHED |
| `GATE-TERRY-007` (DGS10 <4.50 ×5) | 46bp [9/22] | TERRY's rail; counter 0 |
| HY OAS >300 (reopen HYG) | 27bp [9/23] | 🟢 |
| CCC >1100 escalation | **7bp** [9/23] | 🟠 closing |
| Credit-equity lead (HY +75–100 from the 263 trough) | 65–90bp | 🟢 inactive |

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **3** = | 🟠 | `VX-BND-05` · `12` · `14` | DGS30 5.29 [9/22], run 55; DFII10 2.63 through the gate since 9/10; 1y1y new sample high; vendor 30Y 5.43 intraday | **A fresh DGS30 high WITH weak composition — 9/23 HAS the weak composition; if H.15 DGS30[9/23] >5.37 the letter fires ⇒ 4** (docketed 9/25). Or DFII10 sustained (WQ-246) |
| 2 | Treasury auction health | **3** ▲ | 🟠 | `VX-BND-01` · `08` · `13` | **9/23 5Y: BTC 2.21 < 2.28 cover bar (and <2.3 KEY-THRESHOLD cover marker) + OLD composition failure + `I'`; 7Y `I'` by 0.04pp.** Paired kill NOT fired (funding −3bp; FR2004 leg unevaluable ~mid-Oct) | A composition failure with the funding/FR2004 leg CONFIRMED (paired kill) ⇒ 4 |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `16` | FR2004 9/9 long-end $146.2B (+$1.5B, one build); 5Y dealer 15.77 is the trailing-12 max but ordinary vs 2023–24. **9/24 20–30Y buyback op: F2 read ~14:15** | Two consecutive builds on TOTAL with weak composition, or SOFR−IORB positive; F2 ON-THE-RUN fire |
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `11` | HY 273 inert; **CCC 1093 fresh high, 7bp from 1100**; CCC−BB 934 new span max | HY >300 with velocity, or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `10` | IG 77 [9/23] | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF z20 +1.28 [9/8, STALE] | Synthetic leading cash, sustained |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — 65–90bp headroom | HY +75–100bp from 263 while VIX <20 |

**Composite: 13/35 — UP 1 (12 → 13), the first change in sixteen scoring sessions.** Row 2 moved **2 → 3 on a pre-registered rule, not a judgement**: the 5Y BTC 2.21 is below both its trailing-12 min (2.28) and the KEY-THRESHOLDS 2.3 cover marker, which "escalates the vector" (the 7/27 precedent, when the vector moved on a benign story because that is what pre-registration is for). **The KILL is a different test and did not fire.** Distribution: 🟠 2 · 🟡 2 · 🟢 3 · 🔴 0. **Re-summed: 3+3+2+2+1+1+1 = 13 ✅.** ⚠️ `VX.tsv` row-state write-back for `VX-BND-01` owed at closeout.

**Outside the composite:** `VX-BND-15` inflation anchoring (2) · `VX-BND-17` MBS relay (1) · `VX-BND-18` FHLB (2) · `VX-BND-19` EZ rates (3 — HANS: ECB T-04 no longer a hawkish lean; German 2027 debt service +38%; "disorderly" UNDEFINED → 10/1) · `VX-BND-20` benchmark UST demand (2, checkpoint 10/6).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 1** — `BND-27` (CCC <1100 through 9/30, 65%; **7bp away, 1093 [9/23], five sessions left** — momentum against it). **Resolved 9/24:** `BND-25` **TRUE** (55%) · `BND-26` **FALSE** (70%). Earlier: `BND-29` TRUE 9/17 · `BND-28` TRUE 9/15. **Tally: 14 TRUE · 12 FALSE · 1 VOID.** Archives: `thesis/archive/PREDICTIONS_resolved_*`. ⚠️ **No new predictions registered this session; the 10/28 FOMC curve-shape row is owed with a base rate by 10/21.**

---

## Trade Interface *(full view → `TRADE.md`; construction is TERRY's lane)*

- **TLT puts (Sep-30 77P ×20 — 5 of 25 sold 9/10, `FORGE/STATUS.md:54`) — HOLD, no add, `$0`.** 🔴 **BOTH add-gates now read through on their letters:** (a) DFII10 2.63 (sustain count WQ-246) and **the OLD-conjunctive auction re-arm (9/23 5Y)**. ⛔ **Neither is an add: Will's 7/16 NO-ADD governs, WQ-280 is with Will (PROME rec DECLINE, with a fresh TERRY card as the named alternative), root rule #5.** **Expiry 9/30 = 6 days; harvest/roll is TERRY's.** *Posture, never a direction.*
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
| **Thu 9/24 1:40 PM** | 🔴 **20Y–30Y buyback op (cap $6B) — first in-scope F2 read of the carrier** | `buyback_f2.py --op 2026-09-24` **only when results are COMPLETE** (new `complete()` guard) → packet to RED same day |
| ✅ 9/22 · 9/23 · 9/24 | 2Y 🟢 · **5Y 🔴 OLD composition failure** · 7Y 🟠 `I'` by 0.04pp | Graded 9/24 (`KB-BND-312/313`) |
| ✅ 9/18 (carried) | `BND-25` TRUE · `BND-26` FALSE | `KB-BND-315` |
| **Fri 9/25** | 🔴 **H.15 9/23 cells** — DGS30 >5.37? | Row 1 upgrade letter (weak composition day) |
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

**[2026-09-24 Thu ~13:1x ET — boot after a six-day gap; markets open.]**

**The auction side just produced this desk's hardest test since the thesis was written.** The 9/23 5Y failed the strict two-part composition test: foreign-type buyers took their smallest 5Y share since March 2020 while dealers took the most in a year. That meets the pre-set condition for adding to the TLT puts. **It is Will's call (WQ-280), PROME recommends declining, and BOND proposes nothing.** The caveats that decide it: funding stayed calm (−3bp), dealers were not stuffed by any multi-year standard (they took more five times in 2023–24), and the print cleared on the day hot PMIs sold the whole curve off. **Threshold fired; mechanism not shown failed.** The rate path is also still repricing up: this desk's 9/14 view that the hawkish path was fully priced was **wrong** (`BND-26`). **Position: TLT 77P ×20 HOLD, no add, `$0`, expiry 9/30. Composite 13/35 (▲1). Counter 0. OPEN predictions 1.**
