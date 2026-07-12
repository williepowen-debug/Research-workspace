# MIDAS — SCRATCH (next-session pickup)

**⚠ STANDING INSTRUCTION — POLARITY DISCIPLINE (PROME round 3, Will-approved, 2026-07-12):** `metals_watch.py`'s M1 classifier flags **CONVERGE = REVIEW (rc=1)**, and that polarity is **FROZEN through MIDAS-03 (CPI 7/14) AND MIDAS-04 (China GDP ~7/16)**. **NO flip until BOTH resolve.** Only if M1 v2 survives both tests do you flip the script polarity (CONVERGE→quiet, DIVERGE→review trigger) and update the metals_watch header + verdict-block comments. This is written into the metals_watch.py header comment too. Do not flip early.

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
