# MIDAS — SCRATCH (next-session pickup)

**2026-07-12 ROUND 2 (PROME/Will-directed, same day): M1 v2 re-derived + LME inventory wall broken.**

Round 1's correction opened a hole; round 2 filled it with data. **M1 v2** (THESIS.md, full mechanism scoreboard): blow-off retracement (peak $5,318.40 [1/29/26], now −22.7% off, still +24% YoY) = SIZE-setter; real rates = DIRECTION-setter (cyclical layer re-coupled); ETF outflows (−$8.9B/−74t June [WGC, PROV]) = amplifier; CB floor INTACT (243.7t Q1, 17th consecutive month [WGC GDT, PROV]); USD ruled out (DXY +0.61%, flat over the window). Premium lives in the LEVEL, not the DELTA. **Kill-triad:** gold <$3,317 w/o yield spike · WGC Q2 <100t · UP-decoupling sustained 3+wk (that one = bigger stress signal, escalate). **LME copper stocks now LIVE** (westmetall scrape → `metals_watch.py` leg 6): 306,500t [7/10], −23.9% off the 4/15 peak (402,625t) = ~3mo tightening; +110.9% YTD but off a multi-year-low Jan base. **MIDAS-03 reframed under v2** — escalation polarity inverted: gold RISING on yields-up is now the alarm (premium reassertion), gold falling is v2-consistent.

**▶ PICK UP HERE (next session, priority order):**
1. **Resolve MIDAS-03** (CPI Tue 7/14, first live v2 test) by 7/16 once DFII10 T+1 publishes — sign check + v2 interpretation.
2. **Resolve MIDAS-04** (China Q2 GDP ~7/16, copper 2-session reaction) — VERIFY exact NBS release date/time first (7/16 is WebSearch-derived).
3. **WGC primary pulls** — GDT Q1 CB data file + goldhub ETF-flows CSV → upgrade KB-014/015 PROVISIONAL→EMPIRICAL. **Calendar: WGC Q2 GDT ~late July = v2 kill-condition #2 test (<100t kills).**
4. **I2 primary-source verify** — 132.83%/828% Russian-Pd tariff reconciliation (Federal Register); WPIC 240koz Pt-deficit vs the actual quarterly.
5. **I1 inventory-threshold baseline** — "+100% vs normal" has no defined normal; proposal: rolling 2-yr median of LME stocks (now data-feasible, series is live).
6. **COT weekly-cadence leg** — the 12-mo arc pull (KB-013) was manual Socrata; wire it weekly. (L-05: raw API only, never WebFetch-summarized.)
7. **metals_watch.py rc-polarity revisit** — CONVERGE currently trips REVIEW (kept deliberately until v2 survives MIDAS-03/04); if v2 holds, flip: CONVERGE=quiet, DIVERGE=REVIEW.

**Discipline reminder (LESSONS L-01):** monetary and industrial channels SEPARATE. Current state is the THIRD case beyond THESIS.md's two named ones: **gold down + copper up = growth-without-debasement-premium**. Name it in THESIS if it persists past MIDAS-03/04.

**Open dependencies (not MIDAS's to do):** PROME → round-1 route-outs delivered (commit 40357f1d per PROME's round-2 packet); ZHAO → copper/China seam + MIDAS-04 anchor sign-off; HAWK → I2 PGM-supply corroboration; BOND/LIQUID → v2 framing relevant to both (see NEXUS_BRIEF).

---

**2026-07-12 ROUND 1 — FIRST REAL SESSION (archive of same-day round-1 note).**

`metals_watch.py` BUILT + wired into `boot.py` leg 0. Every channel got its first dated live read. Headline: the 7/11 build session's M1 framing ("gold structurally bid despite rising real yields") did NOT survive the first spot pull — gold −18.6% vs DFII10 +36bp over 90d, verified across 5 monthly markers. M1 3→2. Detail: KB-MIDAS-005; superseded by the round-2 v2 re-derivation above.
