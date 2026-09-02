# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension, integrated 7/1; + the sovereign-credibility instrument set per the Will-ruled 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-09-01 ~21:0x–2x ET · **Prior:** 2026-08-27 (desk dark 8/28 → 9/1)

> ### 📕 THIS FILE WAS SPLIT HOT/COLD ON 2026-09-01 — READ THIS BEFORE ASSUMING SOMETHING IS MISSING
> It had reached **160,077 B = 295% of the 32,550 B read cap**, i.e. **no session could read its own STATUS at boot** — a Read returns a partial file with no error, so every line-count guard passed while the boot silently degraded to fragments. Ruled by DAEDALUS 8/28 (`inbox/2026-08-28_from-DAEDALUS_P1-read-cap-RULED-*`, canon `AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md`), executed this session on PROME's scope.
> **NOTHING WAS DELETED.** The complete pre-split file is verbatim at **`archive/2026-09-01_STATUS_cold_pre-split-full-snapshot.md`** — **160,077 B, crc32 `1210262`**, byte-identical to the source at copy time.
> **What moved to cold:** the correction riders, retraction blocks, teaching quotes, per-auction evidence essays and archived BOTTOM LINE blocks. **They are history and they are intact.** **What stayed hot:** every live value, score, gate, exit criterion and dated catalyst.
> ⚠️ **The riders were the bulk and they are the un-rotatable mass** — they must stay verbatim *somewhere*, and keeping them in the boot-read surface is what breached the cap. Moving them is the remedy the ruling names, not a loss of the record.

**Canonical elsewhere — this file carries NO second copy:** thesis + full falsification → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalyst source of truth → `docket/CATALYSTS.tsv` · positions/gates → `TRADE.md` · durable learnings → `MEMORY.md` · session handoff → `SCRATCH.md`.

---

## Regime (one-line)

**Real-rate / higher-for-longer.** ★ **C-36 RULED 2026-09-01 — THE LABEL IS TWO-PART: the policy-path channel is ALIVE AND TRANSMITTING · term premium drove the July delta.** The board's oldest open ask, CONTESTED ~50% since the Will-ruled 8/10 forum downgraded the one-part *"policy-path-led"* CONFIRM. **Decided on HENRY's pre-registered branch, which resolved on published data:** the 8/28 print (published 8/31, graded here at the FRED primary) is **monotonically front-led — Δ2Y +14.0 > Δ10Y +6.0 > Δ30Y +3.0**, 2s10s **47 → 39bp**, against a **measured** +17pp Sept-hike repricing. ⇒ leg 2's mechanism CONFIRMED LIVE. **A one-part label over-reads the evidence in EITHER direction** — the pure term-premium reading over-reads HEN-42 (HENRY's own correction), and the pure policy-path reading is dead on leg 1, which failed **21 of 21** sessions. **THESIS v1.1.9 → v1.2.0; four caveats travel with it → `thesis/CHANGELOG.md`** — chiefly that **one session is not a path** (this confirms the channel TRANSMITS, not that a policy-path trend resumed) and the 8/28 tape is confounded by Warsh + the repricing + the global selloff. ⚠️ **This does NOT move C-36 "toward term premium" — the 8/10 forum guard-rail stands. It SPLITS the label.**

**The configuration, restated:** the long end is engaged (30Y in a **40-session run ≥5.00%**, 56 days in 2026) with **no Fed coupon backstop post-QT**, so long-end absorption is entirely private/foreign/dealer. **Auctions remain "expensive, not broken" — 18 consecutive benign resolutions since 7/9**, no composition failure at any tenor on either live definition. Credit is inert at the index with a live CCC tail.

---

## Current Dashboard

*Every value pulled live this session via `monitors/boot_recompute.py` (cache-busted) unless tagged otherwise. **No naked numbers** — source + date on every row.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y (DGS30) | **5.25%** | 🔴 | [CONF FRED **8/31**] |
| 10Y (DGS10) | **4.75%** | 🔴 | [CONF FRED **8/31**] · wire marks 4.798–4.80 on 9/1, FRED publishes 9/2 |
| 2Y (DGS2) | **4.34%** | 🟠 ↑ | [CONF FRED **8/31**] |
| **10Y real (DFII10)** | **2.44%** | 🟠 ↑ | [CONF FRED **8/31**] — **96.7th pctile full series (n=5,920, from 2003), 99.7th post-2010** |
| 5Y5Y fwd (T5YIFR) | **2.33%** | 🟡 ↑ | [CONF FRED **9/1**] — **+2.0bp on 9/1.** Publishes one date ahead of the nominals (H.15 partial split, `KB-BND-168`) |
| 10Y BE (T10YIE) | **2.35%** | 🟠 ↑ | [CONF FRED **9/1**] — 🔴 **+4.0bp ON 9/1**, after a week of flat-to-FALLING. Publishes one date ahead |
| ACM 10Y term premium | **+0.73%** | 🟠 | [CONF NY Fed, **Jul-2026 monthly — NOT daily**] |
| Kim-Wright 10Y TP (daily) | **0.8682** | 🟠 ↑ | [CONF FRED `THREEFYTP10` **8/21** — model output, not a market price] |
| **HY OAS** | **263bps** | 🟢 ↓ | [CONF FRED `BAMLH0A0HYM2` **8/31**] |
| **CCC OAS** | **1042bps** | 🟠 ↑ | [CONF FRED `BAMLH0A3HYC` **8/31**] |
| IG OAS | **80bps** | 🟢 = | [CONF FRED `BAMLC0A0CM` **8/31**] |
| **FR2004 11–21Y** | **$68.9B** [as-of **8/19**] | 🟡 ↑ | [CONF NY Fed API `SBN2024`, pulled **9/1** via `monitors/fr2004_fetch.py`] |
| SOFR−IORB | **−2bp** | 🟢 = | [CONF FRED, 8/20 — stale, refresh next session] |
| TLT | **$81.87 −0.79%** | 🟠 ↓ | [CONF yfinance **9/1 close**, pulled 9/1 ~21:1x ET] |
| ^MOVE (rates vol) | **77.88 +3.39%** | 🟡 ↑ | [CONF yfinance **9/1**] — up from 73.18 [8/20] |
| JGB 10Y | **2.987%** | 🟠 ↑ | [CONF **MOF primary**, **9/1**, BOND's own pull — wires report 3.00%, first since 1996] |
| JGB 30Y | **4.131%** | 🟠 ↑ | [CONF MOF primary, **9/1**] |
| EA AAA 10Y | **3.340%** | 🟠 ↑ | [CONF ECB SDW, **8/31**] — wire 3.364 on 9/1, highest since Apr-2011 |
| UK 10Y | **5.025%** | 🟠 ↑ | [CONF BoE IADB, **8/27** — BoE's own lag; 8/31 a UK bank holiday] |
| USD/JPY | **cite SAM** | 🟠 | [**SAM owns** — read the level at `AGENTS/SAM/STATUS.md`. This desk keeps NO copy] |
| Brent | **cite BRENT** | 🟠 | [**BRENT owns** — read at `AGENTS/BRENT/STATUS.md`. BOND needs the DIRECTION for the breakeven read, not a level of its own] |
| Fed b/s (WALCL) | **$6.746T** [8/19] | 🟢 = | [CONF FRED, 8/19] |

### Gate distances — the numbers that drive decisions *(recomputed every boot, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — the ONLY live TLT-put add-gate** | **6bp** [8/31] | 🔴 **closest since 8/17** |
| T5YIFR >2.50 (inflation-unanchor) | 17bp [9/1] | 🟡 |
| DGS30 >5.00 (long-end level) | — | 🔴 **BREACHED**, 40-session run |
| DGS10 >4.50 (arm-#2 line) | — | 🔴 **BREACHED** |
| HY OAS >300 (reopen HYG) | 37bp [8/31] | 🟢 |
| CCC/HY ratio >1100 escalation | 58bp [8/31] | 🟠 |
| Credit-equity lead reactivate (HY +75–100 from the 263 trough) | 75–100bp | 🟢 inactive |

🔴 **THE ADD-GATE MOVED 12bp TOWARD FIRING WHILE THIS DESK WAS DARK, and every BOND surface said 18bp until this session.** True path: 2.32 [8/25] → 2.34 → 2.34 → **2.42 [8/28] → 2.44 [8/31]**. **Position UNCHANGED — Will's standing 7/16 NO-ADD governs, root rule #5 backstops, and no add executes without [Approve].**

### ★ FR2004 8/19 — a compositional fact that runs AGAINST this desk's recent framing

**Dealers EXTENDED DURATION in the week to 8/19:** 7-11Y **$39.3B → $30.7B (−$8.6B)** while **11-21Y $61.2B → $68.9B (+$7.7B, +12.6%)**; >21Y −$1.9B; total long-end −$2.9B to $146.3B.

⚠️ **Consequence for a claim these surfaces have carried since 7/28:** the 11-21Y drawdown off the 6/24 peak was reported as **−17.4% / −20.9%** and is now **−11.0%** (77.4 → 68.9). The total long-end drawdown is **−16.4%** (175.0 → 146.3) and still widening. ⇒ **"Record dealer stock has unwound, so the bear case is less pre-positioned" is now only half true** — it holds for the long end in aggregate and **has partially reversed in the 11-21Y bucket this desk's own vector tracks.**
**NOT scored:** dealer absorption is a **STOCK** vector and one print with the total still falling is ambiguous by the monitor's own discriminator (benign distribution vs forced de-risking). **No pre-registered trigger fired ⇒ the vector holds at 2.** Logged, not traded.

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **3** = | 🟠 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | 30Y 5.25 in a **40-session run ≥5.00**, 56 days in 2026; DFII10 2.44 = 96.7th pctile full / 99.7th post-2010 | DFII10 ≥2.50 sustained, or a fresh DGS30 high with weak composition |
| 2 | Treasury auction health | **2** = | 🟡 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED | **18 consecutive benign resolutions since 7/9.** 8/27 7Y: BTC 2.50, ind 60.78% (+3.54pp clear of the `I'` bar), dlr 12.26% — clean on BOTH live definitions | A composition failure (see kill spec), or 3 consecutive auctions passing both legs (counter = **0**) |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` · `VX-BND-16` | FR2004 8/19: long-end −16.4% off peak, **but 11-21Y +12.6% w/w** — duration extension, ambiguous | A further 11-21Y build **with** weak auction composition or SOFR−IORB positive |
| 4 | HY market function | **2** = | 🟡 | `VX-BND-02` · `VX-BND-11` | HY 263 inert, zero pulled deals, primary open every session; **CCC tail 1042 and rising** | HY OAS >300 with velocity, or a pulled-deal cluster |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` · `VX-BND-10` | IG 80, ~$56B priced the week of 8/11 without disruption | IG >120 or a failed syndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | No sustained divergence | Synthetic leading cash on a sustained basis |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive — HY 71bp below the reactivation band | HY +75–100bp from the 263 trough while VIX <20 |

**Composite: 12/35 — UNCHANGED for an EIGHTH consecutive scoring session** (8/15 · 8/18 · 8/20 · 8/21 · 8/27 · **9/1**). Distribution: 🟠 1 · 🟡 3 · 🟢 3 · 🔴 0.
**Re-summed and verified against the vector scores this session: 3+2+2+2+1+1+1 = 12.** ✅

**Tracked OUTSIDE the composite** (they enter the matrix only when they earn weight, so the composite stays comparable across sessions): `VX-BND-15` inflation-expectations anchoring (2) · `VX-BND-17` MBS / housing-finance relay (1) · `VX-BND-18` FHLB advances (2) · `VX-BND-19` eurozone rates / ECB shock (3).

> ⚠️ **OPEN MIRROR DIVERGENCE, found by `kb_lint` this session and NOT papered over: `VX-BND-05` (Yield Curve / Long-End Duration) carries score **4** in `workbook/VX.tsv` while the matrix row it rolls into carries **3**, and `VX-BND-16` (Treasury Buyback Posture) carries **4** against a dealer-absorption row of **2**.** A roll-up legitimately differs from its components — the composite counts each vector once — but **the direction here is that the components are HOTTER than the matrix**, i.e. the divergence runs toward under-stating risk. **It predates this session; it is flagged, not silently reconciled, and is owed a ruling next session.** Reconciling it by editing whichever number is convenient is exactly the failure `finding_reconcile_mismatch_does_not_say_which_side_is_wrong` describes.

⚠️ **It held against evidence pushing BOTH ways this session:** bearish — the add-gate closed 12bp, the 11-21Y dealer bucket re-built, CCC made a fresh high, and 9/1 was a synchronised global selloff. Bullish/neutral — the 8/27 7Y was clean on both definitions and Japan moved LEAST of four DM sovereigns 8/13→8/27. **Nothing crossed a pre-registered line.** The auction-health downgrade counter is **0**, not 1 (TIPS do not count toward it).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 2 — `BND-21` and `BND-22`, both registered this session.** `BND-15` resolved **TRUE** (2026-09-01) and is **re-armed as `BND-22`** over the window that matters (9/1→9/11, the refunding cluster) with **confidence CUT 70% → 55%** — the gate is 6bp away vs 8bp at BND-15's closest approach. **`BND-21` is the `FL-BND-12` test** — whether the real leg stayed insulated on 9/1 — **registered BEFORE `DFII10` [9/1] publishes on 9/2**, because the breakeven half is already visible and grading it after publication would be grading a half-known answer.
**Live file holds `BND-18` → `BND-22`**; **`BND-01` → `BND-17` rotated verbatim** to `thesis/archive/PREDICTIONS_resolved_BND-01_to_BND-17.tsv` under the same read-cap ruling as this file — **22 rows conserved, 5 + 17, nothing deleted.** Resolved tally across both files: **9 TRUE · 10 FALSE · 1 VOID.**

---

## Trade Interface *(full view → `TRADE.md`; positions are TERRY's construction lane)*

- **TLT puts — HOLD, NO ADD.** The only live add-gate (**DFII10 ≥2.50 sustained**) is **6bp away [8/31]** — the closest since 8/17 and **12bp closer than every BOND surface said before this session**. Gates (b), (c), (d) are all **RESOLVED-AND-DEAD**. ⛔ **Will's standing 7/16 NO-ADD governs; root rule #5 means no add executes without [Approve]; harvest/roll/sizing are TERRY's calls on TERRY's rules.** *This bullet states POSTURE, never a direction — it has been corrected for a wrong direction word twice.*
- **HYG puts — stay closed at the INDEX level.** HY 263, access unimpaired, zero pulled deals. Reopen only on **HY OAS >300 with velocity** (37bp away). **The live residue is the CCC tail at 1042 — a fresh 2026 high, NOT a series high** (series max 1137, 2025-04-07). Tail widening with an inert index is a **repricing of the worst credits, not a market-function event** ⇒ if it ever arms, the expression is single-name/CCC, never HYG.
- **Credit-equity lead — inactive.** 71bp of headroom.

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all).** 🔴 **A composition failure at any coupon auction — and TWO definitions are deliberately live until the kill next evaluates (~9/8–9/10), dual-printed:**
- **NEW (Will-ruled 8/27, `PROME/proposals/2026-08-27_matrix-v2-kill-scope-RULED.md`), governs auctions graded 8/27 forward:** **indirect below that tenor's own trailing-12 15th PERCENTILE, SUFFICIENT ALONE.** Dealer take is **dropped as a bearish criterion** (descriptive only; >18% is contrarian-**BULLISH**). **Derive the bar PER TENOR at grade time — 7Y = 57.24% is the only one computed; the full table is owed 9/4.**
- **OLD (retained for the dual-print):** indirect below trailing-12 min **AND** dealer above trailing-12 max, same tenor.
- 🔴 **Direction disclosed: the new test is STRICTLY EASIER TO FIRE, and the kill firing is what CONFIRMS this desk's own bear thesis.** History was NOT re-scored. Percentages are of **competitive accepted**; never reuse another tenor's numbers.
- ⛔ **NAMED EXCEPTION — the TLT-put ADD re-arm in `TRADE.md` is governed by the OLD, STRICTER test** (WQ-99, Will 2026-09-01 17:22 ET). An ADD authorization must never loosen as a side effect of a definition reconcile. Harmonize only by fresh word with TERRY in the loop.
- ⚠️ **`monitors/grade_auction.py` still computes the OLD test — deliberately.** Until the kill next evaluates, its print **IS** the old-definition half of the dual-print: **useful, NOT the authority.** Patch owed before the old print retires.

**2 · POSITION-SPECIFIC.** TLT puts: exit on a decisive break of the real-rate regime — **DFII10 <2.00 sustained 5 sessions** — or on the thesis kill. 60-DTE mandatory review is TERRY's rail.

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal-coupon auctions passing **both** legs (indirect at/above median **and** dealer at/below median). **Counter = 0** — the 8/19 20Y failed the condition and reset it; **TIPS do not count.**

**4 · TIME-BASED.** MATRIX_V2 per-tenor base-rating due **9/4**. Quarterly percentile-snapshot refresh in `monitors/AUCTION_HEALTH.md` due **10/1**. FHLB Q3 combined report **11/9**. FRBNY quarterly FX report **11/13**.

⚠️ **RETIRED AND NOT REVIVABLE: the auction TAIL (>2bp).** A tail needs the when-issued yield at the bid deadline and **TreasuryDirect does not publish it** ⇒ unscoreable by construction. **No gate, threshold or pre-registration may be keyed on a tail**; wire-reported tails are `[med-conf]` and may never fire anything.

---

## Immediate Catalysts *(source of truth = `docket/CATALYSTS.tsv`; this is the human twin and must not diverge in event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| 🔴 **Tue 9/8** | **3Y auction `91282CRL7`** — September refunding leg 1 | **Docketed 9/1 off `docket_check` v2.** Composition vs the 3Y trailing-12, derived at grade time. |
| 🔴 **Wed 9/9** | **10Y REOPENING `91282CRF0`** ("9-Year 11-Month") — refunding leg 2 | Reopening: different benchmark set, do NOT reuse new-issue bars. **First auction the KILL evaluates on the dual-print.** |
| 🔴 **Thu 9/10** | **30Y REOPENING `912810UW6`** ("29-Year 11-Month") — refunding leg 3 | The long-end referendum. **Derive the 30Y `I'` bar per tenor BEFORE the print.** |
| 🔴 **Wed 9/9 → Wed 11/4** | **sb0607 stepped-up buyback window — F2 goes live at the first op (9/9)** | **STANDING OBLIGATION, EXTERNAL DEPENDENCY: route the F2 read to RED as the ops publish — do NOT batch to a closeout.** `RED-FT-11` v1.1 is an ex-ante conditional **gated on BOND's F2** and **RED will not rebuild it.** Their pre-registered response: off-the-run ⇒ they add a butterfly leg at the next NON-FIRED window; on-the-run ⇒ no change. |
| **Wed 9/9 – Thu 9/10** | **ECB Governing Council** (Berlin, presser 9/10) — ✅ date verified at the ECB primary 8/19 | 2nd 2026 hike? QT language. **EZ Aug HICP 3.3%, a 9/10 hike ~99% priced** (WALTER 9/1). Trigger: **BTP-Bund >200 sustained** — ⚠️ last read 83bp [7/17], **46 days stale, refresh before the meeting.** |
| **Thu 9/10** | **August MTS** — the calendar-artifact test | July's −$432.3B was +48.5% YoY inside an FYTD **+1.3%**, consistent with 8/1 falling on a Saturday. **If August does NOT give back most of the spike, the calendar explanation dies and it becomes a deterioration signal.** Net interest FYTD $931.4B (+10.8% YoY). |
| 🟠 **Tue 9/8** | **CANADIAN RETALIATORY TARIFFS TAKE EFFECT** (dollar-for-dollar vs the US 50% tariff on ~$28B, effective 8/21) | **BREAKEVEN LEG ONLY.** T10YIE / T5YIFR across 9/8 vs the pre-date close, **with DFII10 beside them** to separate a real-yield move from an inflation-expectations one. ⚠️ **NO threshold registered and none is being invented** — the standing insulation claim (`FL-BND-12`, `KB-BND-091`) is the thing under test. A T10YIE move materially larger than its recent daily dispersion **without** a matching real-yield move would qualify it. The $28B basis is UNSTATED in the source. |
| 🟠 **from Fri 9/11** | **`docket_check` BLIND SPAN 9/11 → 9/22 — hand-verify against the Treasury QRA** | The feed reaches ~5 days for coupons and the forward schedule is a QRA **PDF outside TA_WS**, so **no API path closes it.** The tool declares the span UNVERIFIED every run and **deliberately refuses to adjudicate it.** This row is the owed human action. |
| **Tue 9/15 – Wed 9/16** | **SEPTEMBER FOMC — decision + SEP land 9/16** ✅ verified at the Fed primary 8/21 | **A Sept hike is ~65–68% priced post-Warsh** (wires, 9/1). Resolver context for the Fed-path arm. Rest of 2026: 10/27-28 · 12/8-9 (SEP). |
| **~Wed 9/16 · ~Thu 9/17** | **20Y · 10Y TIPS** — PATTERN-EXPECTED, **NOT verified** | 🔴 **Inside `docket_check`'s BLIND SPAN (9/11→9/22) — the feed cannot see them.** Confirm at the Treasury QRA / tentative schedule by hand before docketing. |
| **~Tue 9/22 – Thu 9/24** | **month-end 2Y/5Y/7Y cluster** — PATTERN-EXPECTED, **NOT verified** | Same blind span. Same hand-verification owed. |
| **Fri 9/4** | **MATRIX_V2 per-tenor base-rating** (Will-ruled) + **the re-dated US-sovereign-CDS item** | **PER TENOR, NEVER POOLED** — the `I'` bar sits +4.84pp (2Y) / +0.82pp (7Y) / +0.24pp (5Y) above the trailing-12 min: one rule, three effective strictnesses. CDS: establish existence + pullability BEFORE proposing any threshold. |
| **Mon 11/9** | **FHLB Q3-2026 combined financial report** | `REG-T-06` leg 3 fires if system advances >$700B (REGINALD's, at leg 2 of 3). `VX-BND-18` re-scores. Carries the base rate the escalation-leg retune needs. vs $810.7B [6/30/26]. |
| **Fri 11/13** | **FRBNY quarterly FX report Q3** | **The definitive public record of the 7/30-31 operation** — ESF-vs-SOMA split, size via Table 1. **Until it prints, `FL-BND-11`'s "intervention = mechanical UST reserve selling" must NOT be restated as automatic.** |
| **— STANDING —** | MOF FX intervention · Warsh task force (end-2026) · buyback accept-cap | UST reserve selling = `FL-BND-11` fires · 2027 lane · YCC-lite tell |

**Recently resolved:** ✅ **8/27 7Y `91282CRJ2` CLEAN** (BTC 2.50 · ind 60.78% · dlr 12.26%) — 18th consecutive benign resolution; `I'` did NOT fire on its first live test, **+3.54pp clear**. ✅ **8/25–8/27 cluster all clean.** ✅ **T6 = NO-VERDICT** (trigger never fired, PROME-graded 8/30). ✅ **HEN-42 = DENY** (HENRY, FINAL 8/28). ✅ **MOF monthly 8/31 → intervention ¥15,399.3B ≈ $96B** (SAM owns the figure).

---

## BOTTOM LINE

**[2026-09-01 Tue ~22:4x ET — THE 9/1 SELLOFF, GRADED.]** Full working: `analysis/2026-09-01_GRADE_the-9-1-global-selloff.md`.

★ **IT IS NOT ONE MOVE, IT IS TWO, AND THEY HAVE OPPOSITE SIGNATURES.** Treating them as one "global bond selloff" merges the two things this desk exists to keep apart.
**LEG 1 — the week INTO 9/1 (8/26→8/31, fully published): essentially 100% REAL and monotonically FRONT-LED.** 5Y nominal **+12.0 = real +12.0 + BE +0.0** (real share **100%**); 10Y **+9.0 = real +10.0 + BE −1.0** (**111%**); the identity closes to **0.0bp residual** at both tenors. `DGS2` **+15.0** > `DGS5` +12.0 > `DGS10` +9.0 > `DGS30` **+7.0**, and every curve measure flattened (2s10s **−6.0**, 5s30s −5.0, 2s30s −8.0). **The long-end real did NOT lead** — `DFII30` +7.0 vs `DFII5` +12.0. ⇒ **Textbook POLICY-PATH, explicitly not term premium.** ★ **This is OUT-OF-SAMPLE corroboration of tonight's C-36 two-part ruling, on data that had not been decomposed when the label was ruled** — the label was not fitted to it.
**LEG 2 — the 9/1 session itself (breakeven leg only): breakevens JUMPED where the week had them flat-to-down.** `T5YIE` **+6.0** · `T10YIE` **+4.0** · `T5YIFR` **+2.0** — a near-dated inflation impulse **decaying with horizon**, the shape an energy shock makes. 🔑 **This is a LIVE TEST of `FL-BND-12`** (an oil shock is a BREAKEVEN event, real/policy leg INSULATED) **run in the opposite direction from the crude collapse that promoted it.**

⛔ **THE GRADE IS INCOMPLETE BY CONSTRUCTION AND I AM NOT COMPLETING IT TONIGHT.** The H.15 partial split has breakevens reaching **9/1** while nominals and reals stop at **8/31** and publish **9/2**. 🔴 **I did NOT infer the real leg from a wire nominal** — differencing a wire benchmark quote against a FRED constant-maturity close is the exact construction that made T6's `>5.28` leg unreachable by design. **Registered as `BND-21` instead of guessed.**

🔴 **THE SELLOFF FIRED NOTHING.** DFII10 **6bp** from the add-gate · T5YIFR 17bp · HY 37bp · CCC/HY 58bp. The only "fired" rows (`DGS30` >5.00, `DGS10` >4.50) were breached long before 9/1. ⇒ **A multi-decade-high tape across four sovereigns moved NO pre-registered line on this desk** — the levels are historic and the thesis is exactly where it was. **Composite 12/35. Position UNCHANGED: TLT puts HOLD, no add. $0.**

**Credit:** CCC **1042** (+16.0bp) vs HY **263** (+3.0) — **the tail widened 5.3× the index.** Computed at write time (`BAMLH0A3HYC`, daily closes, 2023-09-04→2026-08-31, **n=785**): a **fresh 2026 high**, **NOT a series high** (max **1137**, 2025-04-07), with **13 obs ≥1042 distributed 2023:1 · 2024:1 · 2025:10 · 2026:1** ⇒ **elevated and unremarkable against 2025, not unprecedented.**
**Funding:** SOFR−IORB flipped **+3bp [8/31]** — **month-end, NOT called as stress**, but it is a named input to `DEALER_CAPACITY`'s forced-de-risking discriminator: **if it does not normalise on 9/1–9/2, the FR2004 11-21Y re-build re-reads as forced rather than benign.**
**International, like-for-like 8/26→8/31:** EA AAA 10Y **+9.1** ≈ US **+9.0** · JP +5.1 · ~~UK +1.3~~ **unusable, endpoint 8/27** (`re-test: 2026-09-03` — BoE IADB republishes daily; this is a 4-day lag, NOT an unavailable source)**.** ⛔ **The min-across-legs bound is NOT quoted** — it would come from the stale UK leg, which is precisely the coverage artifact logged tonight as `KB-BND-207`.

🔴 **ROUTED TO MIDAS, NOT RULED HERE — "gold fell, so it's real rates" is not safe for 9/1.** It is right for LEG 1 (100% real). But **9/1's breakevens ROSE +4–6bp, which is gold-POSITIVE**, and gold fell 2.35% anyway. **Candidate resolution is MIDAS's own finding:** their pre-registered positioning falsifier fired against their own read on 8/28 — gold COT **net/OI 56.86%**, composition **CHASED** (NC longs **+20,257**). **A crowded spec long unwinds hard with or without a real-rate impulse.** Gold is their instrument class.

**[2026-09-01 Tue ~21:0x–2x ET — first boot after four dark days, into a live global selloff.]**

🔴 **The one number that matters moved while nobody was watching: the TLT-put add-gate is 6bp away, not the 18bp every BOND surface carried.** DFII10 went 2.32 [8/25] → **2.44 [8/31]**, its 96.7th percentile on the full series and 99.7th post-2010. **Position UNCHANGED — HOLD, no add** — but the desk spent four days describing its only live decision number as three times further away than it was. **The failure is structural, not attentional: this file had grown to 295% of the read cap, so no session could read it whole; it was split hot/cold this session and nothing was deleted.**

★ **9/1 was a synchronised sovereign selloff and it is the right shape for this desk's thesis, which is exactly why it needs discipline:** US 10Y 4.80% (since Jan-2025) · JGB 10Y 3.00% (first since 1996) · Bund 3.36% (since Apr-2011) · UK 30Y 5.89% (since Mar-1998), **with gold −2.35%** ⇒ a real-rate story, not flight-to-quality. **No threshold fired and nothing is claimed from it yet** — FRED publishes 9/1 on 9/2, so the US legs are wire marks tonight.

★ **The cross-section was rebuilt as a standing instrument and it points AGAINST the crowd read.** `monitors/dm_cross_section.py` (built this session — the Will-ruled 8/10 scope has claimed a "standing series" for 22 days and it was an ad hoc hand-pull until tonight). **8/13→8/27 like-for-like, all four legs at the same endpoint: EA +12.2 > UK +8.2 > US +4.0 > JP +2.4bp — Japan LAST of four, 3.7bp below the DM median.** 🔑 **And the "global common factor" bound turns out to be a COVERAGE ARTIFACT: min-across-legs takes the value of whichever leg moved least, and a leg moves less mechanically when its endpoint stops early — so the bound is set by the leg that can see the LEAST.** Japan's implied idiosyncratic residual is +3.2bp on the mixed-endpoint table and **0.0bp once the 5-day-stale UK leg is dropped.** Bias direction disclosed: it inflates the residual attributed to Japan — toward H2, **the side SAM's verdict gets scored on.** Delivered to SAM (live) with the explicit warning that **no leg reaches 9/1**, so the table must not stand in for the selloff.

★ **`docket_check` v2 justified its existence on the event class it was built for.** Three undocketed September coupon auctions — **9/8 3Y · 9/9 10Y-reopen · 9/10 30Y-reopen** — i.e. **the September refunding**, the exact recurrence of the August failure that caused the tool. It is now docketed. ⚠️ **The blind span 9/11→9/22 remains UNVERIFIED by design** and the 20Y / 10Y TIPS / month-end cluster inside it are **pattern-expected, not confirmed** — hand-verification against the QRA is still owed.

✅ **`BND-15` RESOLVED TRUE.** Window 8/18→8/29 fully graded including the 8/28 close (2.42), which published 8/31 exactly as the prior handoff predicted. **Max in window 2.42 — closest approach 8bp; no close ≥2.50.** The prior session's refusal to grade it early on 8/29 was right: it would have graded a window missing its final observation, and the error ran toward a **false TRUE**, i.e. toward this desk's own comfort.

⚠️ **One finding runs against my recent framing and is stated plainly:** FR2004 8/19 shows dealers **extended duration** — 7-11Y −$8.6B into **11-21Y +$7.7B (+12.6%)**. The 11-21Y drawdown off the 6/24 peak narrows from −20.9% to **−11.0%**. ⇒ **"Record dealer stock has unwound, so the bear case is less pre-positioned" is now only half true.** Not scored — one print with the total long-end still falling is ambiguous by the monitor's own discriminator, and no pre-registered trigger fired.

⛔ **What I did NOT do:** rule the C-36 two-part label. HEN-42's DENY makes the narrow reading live and **HENRY re-ran my own v2 discriminator and it now points the other way** (long-end real led by 8bp over 7/23→8/26 — the exact test that produced my CONFIRM now produces DENY). That deserves its own session, not a corner of a closeout.

**Composite 12/35 — eighth consecutive unchanged scoring session. Position: TLT puts HOLD, no add. Book untouched. $0.**

**Next dated:** 9/3 SAM's 30Y JGB grade (my input delivered) · **9/4 MATRIX_V2 per-tenor base-rating + US-sovereign-CDS existence check** · 9/8–9/10 the refunding, where the kill first evaluates on the dual-print and the WQ-99 add-rearm exception becomes load-bearing · 9/9 F2 goes live, **route to RED as ops publish** · 9/9–10 ECB · 9/10 August MTS · 9/16 FOMC.
