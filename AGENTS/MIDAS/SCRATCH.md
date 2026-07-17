# MIDAS — SCRATCH (next-session pickup)

**✅ POLARITY FLIPPED 2026-07-17 (was FROZEN):** both catalyst tests resolved this week and **M1 v2 SURVIVED** — MIDAS-03 (CPI 7/14) = HIT/v2-consistent, MIDAS-04 (China GDP 7/15) = NO-FIRE. Per the PROME-round-3/Will-approved conditional, `metals_watch.py`'s M1 classifier is now **INVERTED**: CONVERGE (gold re-coupled) = quiet (rc=0); **DIVERGE (gold rising THROUGH rising real yields = premium reassertion) = the REVIEW trigger (rc=1)**. Header + verdict-block + this banner updated; verified current CONVERGE state returns rc=0. Flagged to PROME (pre-authorized, not a new decision).

---

**2026-07-17 REVIEW-AND-GRADE SESSION (PROME-spawned).** Graded the two overdue polarity tests, flipped the polarity, staged the next one, wrote the two-channel week read.

Live @ 7/17 ~12:55 ET (COMEX fut, yfinance): gold **$4,021.90**, silver **$56.26**, copper **$6.26**, Pt **$1,610.50**, Pd **$1,253.00**; GSR **71.46** (benign); DFII10 **2.32 [7/15]** (peak 2.36 [7/13]); LME Cu **300,600t [7/16]** (+24% vs 2yr-med, benign, falling −25% off peak); M1 divergence **CONVERGE** (yields +42bp, gold −12.6% 90d).

**Grades (both quoted verbatim in the 7/17 memo + resolutions in PREDICTIONS.tsv):**
- **MIDAS-03 = HIT** (CPI 7/14, v2-consistent): cool CPI (hdln −0.42% MoM, core 0.0%) but real yields REFUSED to fall (DFII10 2.36 [7/13] → 2.33 [7/14] → 2.32 [7/15]); gold +1.60% same-day 7/14 but FELL over the week (sub-$4k 7/16) = no premium reassertion. v2 was the REGISTERED frame (v0 falsified round-1). Branch caveat: both branches assumed yields-UP; actual −3bp DOWN → graded on the v2 mechanism. No BOND/LIQUID escalation. KB-021.
- **MIDAS-04 = NO-FIRE** (China GDP 7/15): 4.3% YoY MISS (weakest since Q4-2022) but copper held (−0.5% 2-sess, needed −5%). Copper reads structural/AI-grid demand, not China cyclical weakness → reconciles PROME 7/16 seam w/ ZHAO. **DATE DRIFT FIXED: GDP was 7/15, not the registered ~7/16.** KB-022.

**▶ PICK UP HERE:**
1. **MIDAS-05 (China LPR ~7/20 → copper 2-session)** — STAGED, grades ~7/23. **VERIFY LPR date** vs pbc.gov.cn (convention = 20th; 7/20 Mon) + reconcile ZHAO's 7/21 (1-day fork). Anchored EXPLICITLY to the LPR event, not a bare calendar slot (date-drift guard). Current 1Y 3.0%/5Y 3.5%, held 13 mo; ZHAO ZHA-14 = cut ~35% prob.
2. **WGC Q2 GDT (~late July)** = v2 kill-cond #2 (<100t) — calendar it. Excel 403-walled (L-09).
3. **MIDAS-01 cushion thinning** — gold $4,021.90 only ~8.6% above the $3,702.33 falsify line (dipped $3,963 intraday 7/17). OPEN, DFII10 2.32 >2.0.
4. **China Cu imports −41.3% YoY [BRENT 7/17]** — base-effect check owed (ZHAO's series; my 7/12 palladium lesson). Firm price + falling LME ⇒ likely destocking/base-effect, not collapse (provisional).
5. **WPIC Pt-deficit** still PROV; **COT weekly-cadence** leg still owed.

**Lane query:** RATIFIED w/ light amendment (added real-yield/TIPS + PGM-supply terms) — see the 7/17 memo to PROME.

---

**2026-07-12 ROUND 3 (PROME/Will-directed, same day): primary-sourced the PROV legs + defined the LME baseline.**

Three deliverables: (1) **Polarity discipline** written into SCRATCH (above) + metals_watch header — no flip this round. (2) **CB figures PROV→CONF** via WGC primary (gold.org GDT Q1 central-banks page): 243.7t Q1 vs 237.0t Q1-25 (+3%), full buyer/seller list confirmed (KB-019). *Caveat:* the "17th consecutive month" streak + 700-900t FY target were NOT on that WGC section — STAY PROV; the GDT Excel (file 20499) 403-gates automated curl (documented wall, L-09). **PGM sanctions RESOLVED to primary:** Russia-Pd final antidumping margin **132.83%** (Fed Register doc 2026-08487, 5/1/26) — the round-2 "828%" was preliminary (KB-020, L-08). WPIC Pt-deficit stays PROV. (3) **LME baseline DEFINED:** trailing-2yr rolling median = 239,400t (n=507); current 306,500t = **+28% = Yellow band** (not the round-2 "benign"), but falling. Implemented as `read_lme_copper_baseline()` in metals_watch leg 6 (live, auto-updating). Closes KB-017's gap → KB-018. New lesson L-07 (define "normal" before "% vs normal").

---

**2026-07-12 ROUND 2 (PROME/Will-directed, same day): M1 v2 re-derived + LME inventory wall broken.**

Round 1's correction opened a hole; round 2 filled it with data. **M1 v2** (THESIS.md, full mechanism scoreboard): blow-off retracement (peak $5,318.40 [1/29/26], now −22.7% off, still +24% YoY) = SIZE-setter; real rates = DIRECTION-setter (cyclical layer re-coupled); ETF outflows (−$8.9B/−74t June [WGC, PROV]) = amplifier; CB floor INTACT (243.7t Q1, 17th consecutive month [WGC GDT, PROV]); USD ruled out (DXY +0.61%, flat over the window). Premium lives in the LEVEL, not the DELTA. **Kill-triad:** gold <$3,317 w/o yield spike · WGC Q2 <100t · UP-decoupling sustained 3+wk (that one = bigger stress signal, escalate). **LME copper stocks now LIVE** (westmetall scrape → `metals_watch.py` leg 6): 306,500t [7/10], −23.9% off the 4/15 peak (402,625t) = ~3mo tightening; +110.9% YTD but off a multi-year-low Jan base. **MIDAS-03 reframed under v2** — escalation polarity inverted: gold RISING on yields-up is now the alarm (premium reassertion), gold falling is v2-consistent.

**▶ PICK UP HERE (see the ROUND-3 header at top for the live pickup list; round-2 items below, round-3 status marked):**
1. **Resolve MIDAS-03** (CPI Tue 7/14, first live v2 test) by 7/16 once DFII10 T+1 publishes — sign check + v2 interpretation. [STILL OPEN — the priority]
2. **Resolve MIDAS-04** (China Q2 GDP ~7/16, copper 2-session reaction) — VERIFY exact NBS release date/time first. [STILL OPEN]
3. ~~WGC primary pulls~~ — CB core figures DONE (PROV→CONF, KB-019); streak/FY-target + goldhub ETF CSV still owed (Excel 403-walled, L-09). **Calendar WGC Q2 GDT ~late July = kill-cond #2.**
4. ~~I2 sanctions verify~~ — DONE: 132.83% final margin, Fed Reg (KB-020). WPIC Pt-deficit still PROV.
5. ~~I1 baseline definition~~ — DONE: 2yr rolling median implemented in leg 6 (KB-018).
6. **COT weekly-cadence leg** — [STILL OPEN] 12-mo arc pull (KB-013) was manual Socrata; wire it weekly. (L-05: raw API only.)
7. **metals_watch rc-polarity** — FROZEN this round per the standing instruction at top; revisit ONLY after MIDAS-03 AND MIDAS-04 resolve.

**Discipline reminder (LESSONS L-01):** monetary and industrial channels SEPARATE. Current state is the THIRD case beyond THESIS.md's two named ones: **gold down + copper up = growth-without-debasement-premium**. Name it in THESIS if it persists past MIDAS-03/04.

**Open dependencies (not MIDAS's to do):** PROME → round-1 route-outs delivered (commit 40357f1d per PROME's round-2 packet); ZHAO → copper/China seam + MIDAS-04 anchor sign-off; HAWK → I2 PGM-supply corroboration; BOND/LIQUID → v2 framing relevant to both (see NEXUS_BRIEF).

---

**2026-07-12 ROUND 1 — FIRST REAL SESSION (archive of same-day round-1 note).**

`metals_watch.py` BUILT + wired into `boot.py` leg 0. Every channel got its first dated live read. Headline: the 7/11 build session's M1 framing ("gold structurally bid despite rising real yields") did NOT survive the first spot pull — gold −18.6% vs DFII10 +36bp over 90d, verified across 5 monthly markers. M1 3→2. Detail: KB-MIDAS-005; superseded by the round-2 v2 re-derivation above.
