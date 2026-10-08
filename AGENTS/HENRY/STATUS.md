# HENRY STATUS

**Last owner update:** 2026-10-08T08:25:29-04:00 — PROME WQ-389 due-row wake (`prome-fc`, Tier 1). **DOCKET L612 graded:** September ISM Services first print, HEN-48–56 → ranges **5/6 HIT** (business activity MISS), directions **2/3 HIT** (headline >55.4 MISS). Fresh pre-open gamma board: **POSITIVE at both horizons**, flip ~7,746–7,750. Whole inbox drained (19 logged). $0; no letter, threshold, score or capital line moved.
**Superseded blocks** (10/4 adoption block, 10/2 gamma boards, RSP week-7 detail, Sep NFP, 10/2 GAPS/BOTTOM LINE) → `STATUS_COLD.md` §ROT-10/8, verbatim.

## SEPTEMBER ISM SERVICES — GRADED (DOCKET L612) · detail `research/2026-10-08_ISM-services-september-grade/GRADE.md`

| Release | Actual (first print, 10/5 10:00 ET) | Consensus | Prior (Aug) | Market reaction | Thesis implication |
|---|---|---|---|---|---|
| Services PMI | **54.9** | 55.0 / 55.2 / 55.7 by source (secondary, unreconciled) | 55.4 | ~1bp 10Y dip + SPX −0.08% at 10:00, both round-tripped by 10:30; day: 10Y +3bp, SPX +0.66% | Soft on VOLUME, firm on HIRING, hot on COSTS — a stagflation-leaning mix |
| Activity · Orders | **56.5** (−5.2) · **59.8** (−1.1) | — | 61.7 · 60.9 | — | The miss sits here |
| Employment | **50.1** (+2.3, first expansion in 3 months) | — | 47.8 | — | Weakens the soft-labor path read taken from NFP +29K |
| Prices | **74.0** (+1.4; highest since Jul-2022 74.5) | — | 72.6 | — | Premium/inflation side: with Mfg Prices 77.9 [Sep], both surveys >70 |
| Deliveries | **53.2** · Export orders 46.9 (−9.4) | — | 51.3 · 56.3 | — | — |

**Source:** ISM's own report PDF `rain202609svcs.pdf` (sha256 `a953539c…`, metadata ModDate 2026-09-30, pre-release), corroborated by investingLive at 10:04 EDT 10/5. The ISM HTML page was reCAPTCHA-walled. KB `ML-HEN-177`.

| ID | Claim | Grade | Err |
|---|---|---|---|
| HEN-48 · 49 · 50 | headline [54,58] · employment [47,52] · prices [70,78] | ✅ HIT · ✅ HIT · ✅ HIT | −1.1 · +0.6 · 0.0 |
| HEN-51 · 52 · 53 | activity [58,64] · orders [58,65] · deliveries [50,55] | ❌ **MISS** · ✅ HIT · ✅ HIT | −4.5 · −1.7 · +1.2 |
| HEN-54 · 55 · 56 | headline >55.4 · employment >47.8 · prices ≥70 | ❌ **MISS** · ✅ HIT · ✅ HIT | −0.5 · +2.3 · +4.0 margin |

- **L612 adoption outcome:** adoption was **prospective** (declared 10/4 20:52:57 EDT, commit `2bb57dddb` 21:20:09, ~13h pre-release), so the no-retroactive-adoption clause was **not engaged**. The market map was **never registered** and is not graded; the reaction above is observation only.
- ⚠️ **Graded ~64h after the CHOSEN 10/5 16:00 deadline.** This is disclosed, not silently extended. The release was published inside the window, and none of the letter's NO-VERDICT conditions hold. **But under an evaluator-timing reading of the review's sentence, all nine rows are NO-VERDICT** (GRADE.md §4). That reading is open for PROME/a reader to rule.
- ⚠️ **5/6 is weak skill evidence:** the ranges were 4–8 points wide and would have contained 17/24 of the prior four months' cells. The informative outcomes are the activity MISS, which also decided HEN-54, and the employment-direction HIT.

## GEX / GAMMA — PRE-OPEN 10/8 08:18 ET (OI = 10/7 EOD; spot = 10/7 close)

`HENRY 2026-10-08 pre-open: flip ~7,750 (14d, 4,141 contracts) / ~7,746 (35d, 7,307 contracts), src=CBOE; spot 7,801.77 [^GSPC 10/7 close] → +52/+56pt ABOVE at both. Sign POSITIVE at both horizons; Net GEX +$42.0B / +$50.8B per 1%. Walls WITHHELD.`

- **Walls withheld:** 14d call near-tie (7,800 vs 8,000, 3% apart); 35d put ≡ call ≡ 8,000 (impossible as stated); the horizons disagree on the call wall. The boot 14d run at 08:14 gave 7,747 / +$44.8B on 4,217 contracts, so the flip band is **7,746–7,750**.
- **Reading:** dealers are long gamma with ~0.67–0.72% of cushion. The trajectory since 9/28: NEG both → 10/2 close POS (+25pt) → **10/8 POS (+52/+56pt)**. The flip rose ~50pt with spot. **Shelf life ends at the 10/8 open.** ⚠️ +GEX cushions a LEVEL move, not a duration/correlation shock (LESSONS): today's 30Y auction (13:00 ET, BOND's L617) is a duration event. ⚠️ Free tier: the sign and flip are robust; the $B figures are assumption-dependent. NDX gamma is not measured.

## RATES *(Treasury par + real, official CSV pulled 10/8 08:18 ET)*

| Close | 2Y | 10Y | 30Y | 10Y real | 30Y real | 10Y BE |
|---|---|---|---|---|---|---|
| 9/30 | 4.88 | 5.29 | 5.64 | 2.93 | 3.33 | 2.36 |
| 10/2 | 4.83 | 5.28 | 5.63 | 2.92 | 3.34 | 2.36 |
| **10/5** | 4.84 | **5.31** | 5.66 | **2.95** | **3.37** | 2.36 |
| 10/6 | 4.79 | 5.27 | 5.64 | 2.91 | 3.35 | 2.36 |
| **10/7** | **4.77** | **5.28** | **5.67** | **2.92** | **3.36** | 2.36 |

- **30Y 5.67 [10/7]** is the highest close in the **Treasury par window 2023-01-03 → 2026-10-07** (n=942 30Y cells; series query run 10/8). ⚠️ No longer-history claim (DGS30 coverage conflict stands).
- ⛔ **The 30Y real 3.36 [10/7] is NOT a new cycle high:** the Treasury real curve printed **3.37 on 10/5**, the high of the 2023→2026 window. HEARTBEAT's "NEW CYCLE HIGH [10/7, BOND]" tag is not BOND's wording (BOND says "3.36% (+1)") and is routed to PROME.
- **Breakeven flat at 2.36 every session** ⇒ the long-end move is **real yield / premium, not inflation expectations**, even with prices 74.0 in services.
- **Fed path:** October +25bp ≈ **20%** [ZQX26 96.07 vendor, 10/8 08:19 ET pre-open; EFFR 3.88 FRED 10/5; ±2pp; contract name UNKNOWN on vendor truncation; not FedWatch/settle] · 24% [10/2] · 68% [9/28]. **Minutes (pub 10/7, Sept 15–16 meeting): most participants see ANOTHER hike likely appropriate BY YEAR END, conditional** — the bias lives in Dec/Jan pricing, not October (WALTER −002, BOND 10/7). BOND's vendor YE +24.93bp [10/7] is its own basis.
- ACM term premium **not re-pulled** this session (last 0.888 [9/30]).

## VOL REGIME *(VIX family co-owned with VIOLET — she owns the broadcast)*

- **VIX 15.08 [^VIX 10/7 close]** · 15.77 live [10/8 08:14, pre-market] · VIX9D 11.78 · VIX3M 17.72 · VVIX 83.18 · SKEW 141.84 [boot tape 10/8 08:14; last bars]. Contango intact (9D < 1M < 3M). 10/6 close 15.01, **0.01 shy of the <15 kill leg** (dated bar; CBOE publisher not read).
- Vol-control trigger >23: 7.9 under [10/7 close].

## CREDIT EARLY-WARNING MONITOR *(FRED, curl pull 10/8 08:23 ET)*

**HY 303 · BB 185 · CCC 1,214 · gap 1,029 [FRED 10/6]** · ratio 6.56× · Δgap 5d **+61**, 20d +128, ~3mo +214 (CCC +240 vs BB +26). Path HY: 312 [9/30] → **324 [10/1]** → 310 [10/2] → 312 [10/5] → **303 [10/6]**; CCC 1,179 → 1,215 → 1,202 → 1,211 → 1,214. **The index tightened back under the 320 yellow while the tail held** ⇒ the K-shape widened through a headline retreat (BOND 10/7: "tail divergence"). One 324 print, no sustain: REG-T-03 is graded by its owner, not here.

## THESIS — axis verdicts

| Axis | Verdict |
|---|---|
| **1 — CYCLICAL (rates/Fed)** | Premium regime continuing: 30Y 5.67 at a 2023→ window high with the breakeven flat. October hike odds keep fading (20%) while the minutes keep a **conditional year-end hike**. Services prices 74.0 and employment >50 lean hawkish against the NFP softness. Supply calendar (30Y today) is the live risk. Real-yield letter: unregistered |
| **2 — AI-CAPEX** | ✅ Mechanism RESOLVED-CONFIRMED (HEN-36); equity-de-rate expression FALSIFIED. 10/8 WALTER −006 build-friction/financing items are relays, VULCAN/BROCK's — no HENRY figure |
| **3 — STRUCTURAL CREDIT** | 🔴 CCC 1,214 through red; gap 1,029 and widening (+61/5d) while HY retreated to 303 — the tail diverging from the index is the bifurcation signature |

**VERDICT:** dealers long gamma ~55pt above the flip, VIX 15, SPX near highs and the long end at window highs on real yield; the credit tail is widening under a tighter index. The tape is calm, and the rates and credit-tail substance are not.

## INVALIDATION TRIAD — STANDING RULE vs STATE

> **⚖️ STANDING RULE, Will-ruled 2026-08-10 (full text → archive `STATUS_ARCHIVE_2026-09.md` block 14):** ① H-1 SIMULTANEITY, NON-LATCHING — VIX <15 **AND** HY OAS <260 on the SAME session, 5 consecutive; nothing banks. ② H-2 — my leg 1 and LIQUID's `GATE-HY-REKILL` are THE SAME KILL.

**LEG STATE [10/8 pre-open]:** **Leg 1 HY <260 — 303 [FRED 10/06] = 0 of 5, 43bp away** (⛔ NON-KILL OBSERVABLE, WQ-106) · **Leg 2 VIX <15 — not satisfied; 15.01 [10/6], 15.08 [10/7]; last satisfied 9/25 (14.87 publisher)** · **Leg 3 SPX >7,100 × 5 — FIRED, deep.** 🟠 **JOINT: 0 sessions.**

## ACTIVE THRESHOLDS

*Current carries `[src M/D]`; Yellow/Orange/Red = STANDING rule.*

| Metric | Current | Yellow | Orange | Red | State |
|---|---|---|---|---|---|
| ISM Mfg PMI | 54.5 [Sep, ismworld.org 10/2] | <50 | <48 | <47 | NOT FIRED — 4.5 above yellow |
| ISM Mfg Employment | 52.7 [Sep] | <47 | <45 | <43 | NOT FIRED |
| ISM Mfg Prices Paid | 77.9 [Sep] | >60 | >70 | >75 | 🔴 THROUGH RED (observation; no sustain row). Services prices 74.0 [Sep] corroborate |
| PPI final demand | +0.4% m/m · +5.4% y/y [Aug, BLS 9/10] | >0.4 | >0.5 | >0.6 | 🟠 AT YELLOW. Sep PPI = Thu 10/15 |
| VIX | **15.08 [10/7 close]** · 15.77 [10/8 pre-mkt] | >23 | >28 | >30 sust | NOT FIRED — 7.9 under yellow |
| SPX | **7,801.77 [10/7 close]** · 7,818.93 [10/6] | <7,200 | <7,100 | <6,494 | 🟢 ABOVE the flip (~7,746–7,750, POS both horizons). 8.4% above yellow |
| KRE | **$68.89 [10/7 close, −1.68%]** · $70.07 [10/6] | <$65 | <$62 | <$60 | ARMED — 3.89 above yellow |
| 10Y | **5.28% [Treasury 10/7]** | >4.5 | >4.8 | >5.0 | 🔴 RED — every close since 9/23 |
| 2Y | **4.77% [Treasury 10/7]** | >4.25 | >4.40 | >4.60 | 🔴 RED — 17bp over |
| 30Y | **5.67% [Treasury 10/7]** | >5.0 | >5.25 | >5.50 | 🔴 RED since 9/28; 17bp through red; window high (see RATES) |
| HY OAS | **303 [FRED 10/06]** · 312 [10/5] · 310 [10/2] · 324 [10/1] | >320 | >400 | >500 | 🟢 back UNDER yellow (17bp) after one 324 print; no sustain clause on my row |
| CCC OAS | **1,214 [FRED 10/06]** · BB 185 | >900 | >1000 | >1100 | 🔴 RED since 9/24 |
| USD/JPY | 158.23 [live 10/8 08:14, +0.15%] | *(levels retired)* | — | — | Velocity \|Δ\| ≥2%/day — SAM's call; NOT FIRED |
| SKEW | 141.84 [10/8 boot tape, last bar] | >145 | >150 | >160 | UNDER yellow. ⛔ `RED-FT-10` is RED's |
| VIX kill leg | **15.08 [10/7 close]** · 15.01 [10/6] | <17 | <16 | <15, 1 session | ARMED at ORANGE (<16); NOT satisfied RED |
| HY kill leg ⛔ *observable, H-2* | 303 [FRED 10/06] | <290 | <270 | <260 sust. 5 | NOT FIRED — 0 of 5 |

## CATALYST STACK

| Date | Event | HENRY lens |
|------|-------|------------|
| **Thu 10/8** | **30Y auction 13:00 ET (BOND, L617 — not HENRY's grade)** · FR2004 as-of 9/30 · Isaias pre-landfall · Samsung Q3 prelim (VULCAN) | +GEX does not cushion a duration shock; the 30Y is 17bp through my red |
| Fri 10/9 | **RSP week-8 close** — 210.60 [10/7] vs 209.73 [10/2 week close] = +0.41%, so the 7-week streak is at risk · Isaias landfall late 10/9–early 10/10 (Gulfport–Panama City; 25% Gulf oil shut in [10/7]) | Breadth row; energy impulse into CPI |
| **Wed 10/14** | **Sept CPI (HENRY-owned release)** · F1 November-fixed basis ends (HEN-46) | Aug CPI breadth 11/21 >3% y/y (WALTER −009, chart-level); energy leg live |
| Thu 10/15 | Sept PPI · matched-December basis begins for the VLO share (WQ-386, settled) | PPI yellow row |
| Mon 10/19 | Last session a matched November crack can be read (CLX26 expires 10/20) | WQ-252 |
| Tue–Wed 10/27–28 | FOMC | Oct +25bp ≈ 20% [10/8]; minutes = conditional YE hike |
| Fri 10/30 | ECI — last on the current basis | LABOR tripwire |
| Sat 10/31 | Russian diesel ban expiry | |
| late Oct | AAL / LUV Q3 prints | **HEN-46 proper** |
| ~Wed 11/4 | October ISM Services (date per secondary calendar; not ISM-verified) | No forecast registered |

## ACTIVE PREDICTIONS · *canonical → `workbook/PREDICTIONS.tsv`*

| ID | Prediction | Resolves | Status |
|----|------------|----------|--------|
| **HEN-46** | Diesel/jet squeeze: AAL/LUV miss on Q3 fuel. F1 crack <$95 stand down / <$90.16 dead (matched `HOX26×42 − CLX26`, CME settle, through 10/14) · F2 Jazan · F3 SPENT · F4 guide raised · F5 AAL −12% | Q3 prints, late Oct | ✅ ACTIVE 0.35 / 0.30. F1 NOT FIRED on BRENT's Nov estimate $105.82 [10/7 settlement-window VWAP, single vendor, NOT CME] — consumed, not re-measured. ⚠️ Roll hazard: *"one roll is comparable to the whole separation"*. WQ-386 did not amend HEN-46 (ruling item 1) |
| HEN-47 | FORUM-7 verdict rule | 10/2 | ✅ RESOLVED — PREMIUM-ABSORPTION; **BOND CO-SIGNED 10/2 (KB-BND-389)** |
| HEN-48–56 | Sept ISM Services first print | 10/5 | ✅ RESOLVED — 7 HIT / 2 MISS (§ above) |

**No new prediction registered.**

## CROSS-AGENT DEPENDENCIES

| Desk | Live item |
|---|---|
| **PROME** | HEARTBEAT's "30Y real 3.36 NEW CYCLE HIGH [10/7, BOND]" is false on the Treasury real curve (3.37 on 10/5) — routed in the 10/8 delivery memo. Late-grade reading (GRADE.md §4) is open for a ruling |
| **BOND** | FORUM-7 co-signed (KB-BND-389). 30Y auction today is BOND's (L617). Consumes HENRY's Fed-path series (WQ-327): Oct ≈20% [10/8] |
| **CARL** | SIG-W-20261004-012 activity-vs-employment gap: **closed from 13.9 to 6.4 pts** in the Sept print (activity −5.2, employment +2.3) — CARL's row, information on ML-HEN-177 |
| **DAEDALUS / TERRY** | WQ-252 sitting (L471/L472) — HENRY non-first owner; no packet received. WQ-386 SETTLED |
| **LIQUID** | `GATE-HY-REKILL` = THE kill |
| **RED** | ⛔ No counts mirrored — read `AGENTS/RED/registry/FALSIFICATION_TRIGGERS.tsv` |
| **VIOLET** | Owns the vol broadcast; HENRY keeps gamma/0DTE/put-wall |
| **WALTER** | Lane drained 10/8: 17 signals logged + moved (incl. late −015 after WALTER committed it). Weekday correction packeted: SIG-W-20261008-009 says "Tue 10/14", but 10/14 is a Wednesday |

## GAPS

- **Not done this session:** ACM 10/1–10/7 cells (not re-pulled) · HEN-46 F1 crack (consumed BRENT's estimate, not re-measured) · S&P Global final services PMI 10/5 (not read) · CBOE publisher VIX closes (dated yfinance bars only) · 10/7 FRED HY cell (not yet posted at pull).
- **Residue carried in:** real-yield letter (unregistered) · KRE "Muse" deposit-flight (REGINALD's) · own `CLAUDE.md` KB count stale (KB last ID now `ML-HEN-177`) · DGS30 coverage conflict (no 30Y superlative beyond the Treasury 2023→ window) · TLT flow verification (WALTER −013 of 10/4) DEFERRED · gamma wall cross-horizon gap (audit E2) unfixed.

## BOTTOM LINE

September services did not confirm the strong-demand case: activity fell 5.2 points. It did confirm the two hawkish legs, with hiring back over 50 and prices at a three-year high. The bond market agrees: the long end is at window highs on real yield, with breakevens flat. Equity is calm and dealers are long gamma, but that cushion does not cover a duration shock, and today's 30Y auction is one. The credit tail keeps widening under a tighter index. No HENRY threshold moved, and no Will decision is needed.
