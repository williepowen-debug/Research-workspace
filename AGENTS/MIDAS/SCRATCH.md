# MIDAS — SCRATCH (next-session pickup)

**2026-07-23 MIDAS-05 GRADE SESSION (PROME-spawned, ~12:30 PM ET, ON-TIME — grade due ~7/23).** Graded the owed LPR prediction, reconciled the date-fork, refreshed all marks (7/23 live intraday, US mkts open). *(Spawn prompt initially gave a wrong "Fri 7/24 midnight" premise; PROME corrected to Thu 7/23 midday — grade is on-time, not day-late.)*

**MIDAS-05 = NO-FIRE (correct null; KB-027, PREDICTIONS resolved).** China LPR **HELD** 7/20 Beijing (1Y 3.00%/5Y 3.50%, 14th consecutive month, fully expected — Reuters poll 23/23 hold; PBoC via CNBC/People's Daily 7/20) yet copper **RALLIED +4%** over the 2 sessions post-fixing (HG=F $6.299 [7/20] → $6.511 [7/21 endpoint] vs the $6.26 anchor; actual 7/17 settle $6.22 → +4.7%), eased to $6.3435 [7/23]. I1 yellow (HOLD+copper−5%) did NOT fire; no ZHAO/HENRY flag. **Discrimination (mirror of MIDAS-04):** copper rallied THROUGH a no-stimulus hold = structural/AI-grid demand, NOT China policy/cyclical. Brier-equiv ~0.02 (P(fire)~0.15 pre-reg, outcome 0).

**Date-fork status:** ✅ my ledger internally CONSISTENT + CORRECT — fixing 7/20 Beijing (~9:15pm ET Sun 7/19), verified vs the actual print (announced Mon 7/20). **ZHAO-side reconcile REMAINS:** PROME already sent ZHAO a 7/17 date-fix (`ZHAO/inbox/2026-07-17_from-PROME_lpr-date-fix-and-midas-seams.md`, "MIDAS caught the fork") but ZHAO's own files STILL carry 7/21 un-reconciled — STATUS.md:187/212, NEXUS_BRIEF.md:72, PREDICTIONS.tsv ZHA-14. ZHA-14 is now gradable too (=hold; the 30% cut call missed direction, correctly low-conf). **Flagged to PROME for routing — did NOT edit ZHAO's files.**

**Marks refreshed 7/23 intraday ~12:30 PM ET (venv yfinance; US mkts open, live not closes):** gold **$4,050.80**, silver **$57.96**, copper **$6.3435**, Pt **$1,605.60**, Pd **$1,262.50**; GSR **69.89** (benign); DFII10 **2.37 [7/21] = NEW series high**; LME Cu **284,175t [7/22]** (+16% vs 2yr-med, benign, −29% off peak). MIDAS-01 cushion ~9.4% above the $3,702.33 falsify line (recovered from ~8.6%). **NASCENT M1 WATCH (not fired):** gold +0.7% while DFII10 hit a new high 2.37 = mild gold-through-rising-yields (v2-kill-cond-#3-shaped) but only ~4 days, FAR short of the 3+wk sustain → WATCH, not the DIVERGE alarm.

**⚠️ boot.py leg-0 failed under system python3** (`No module named 'yfinance'`) — the metals_watch spot/GSR legs need the repo venv (`.venv/bin/python`). FRED + LME legs ran fine (urllib). Boot instruction / venv-invocation is the fix (auto-mem `finding_market_data_venv_invocation`); flag for a boot.py shebang/venv fix if it recurs. rc=2 was the yfinance fail, NOT a real leg failure.

**▶ PICK UP HERE (7/23):**
1. **ZHAO-side LPR date-fork reconcile** — flagged to PROME; watch for ZHAO to process PROME's 7/17 fix + grade ZHA-14. Not MIDAS's to edit.
2. **WGC Q2 GDT (~late July)** = v2 kill-cond #2 (<100t). Excel 403-walled (L-09); WGC web pages carry figures.
3. **Nascent M1 divergence** — gold holding through a rising-yield tape; if it sustains 3+wk it trips v2 kill-cond #3 (escalate BOND/LIQUID). ~4 days so far, WATCH only.
4. **boot.py venv fix** — if leg-0 fails again, wire `.venv/bin/python` into the boot invocation.
5. Carryover: China Cu imports −41.3% YoY base-effect (ZHAO's series); COT weekly-cadence leg; WPIC Pt-deficit PROV.

---

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

**POST-DELIVERY (7/17): LIQUID curve check consumed → KB-026 + STATUS/NEXUS corrected.** The WALTER SIG-011 "higher-rate bets" mechanism is REFUTED by the tape (DGS2 −8bp 4.21→4.13 [7/10→7/15], MIDAS-verified vs FRED; DFII10 off its 7/13 peak). Corrected: gold's sub-$4k dips = real-yield LEVEL opportunity-cost cap + positioning unwind, NOT a rate-hike repricing — the "gold weakness ≠ risk-on" conclusion still holds. EndGame stays 1-of-4 (DXY 100.75 soft; a real liquidity event pairs gold-down w/ dollar-squeeze UP). Gold-leg NOT an EndGame confirm unless DXY breaks UP >102-103. LIQUID now owns metals-board gold levels (stopped own-pulling).

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
