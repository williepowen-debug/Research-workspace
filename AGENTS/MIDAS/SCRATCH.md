# MIDAS — SCRATCH (next-session pickup)

**2026-07-12 — FIRST REAL SESSION (Will-directed, priority: stand up `metals_watch.py` + first live baseline).**

`metals_watch.py` is BUILT and wired into `boot.py` as leg 0 (self-locating, imports FORGE `fetch.py`). Every channel now carries a dated live read for the first time. **Headline finding: the 7/11 build session's M1 framing ("gold structurally bid despite rising real yields") does NOT survive the first spot pull** — trailing 90d shows gold -18.6% while DFII10 +36bp, the classic inverse relationship, verified across 5 monthly markers. M1 downgraded 3→2. Full detail: STATUS.md "HEADLINE CORRECTION" + KB-MIDAS-005.

**▶ PICK UP HERE (next session, priority order):**
1. **LME/COMEX inventory (I1)** — still a gap; no free API found this session (CME `warehouseStockAPI.json` → 403; LME vendor-gated). Try westmetall.com scrape next.
2. **I2 primary-source verify** — the 132.83%/828% Russian-Pd tariff figures need reconciliation (Federal Register / Commerce Dept determination); WPIC 240koz Pt-deficit figure needs the actual WPIC quarterly, not a WebSearch summary. Currently PROVISIONAL, not EMPIRICAL.
3. **Resolve MIDAS-03** (CPI 7/14 gold-vs-real-yield same-day sign check) by 7/16 once DFII10 T+1 publishes.
4. **Resolve MIDAS-04** (China Q2 GDP ~7/16, copper 2-session reaction) — VERIFY the exact NBS release date/time first (this session's 7/16 is WebSearch-derived).
5. **Consider wiring COT into a weekly-cadence leg** — this session's CFTC pull was manual (direct Socrata API, NOT WebSearch/WebFetch — see LESSONS L-05, those hallucinated wrong numbers on first attempt).
6. **CB gold-buying / WGC flow data** — Tier-2 M1 structural leg, still unpulled (quarterly cadence candidate).

**Discipline reminder (LESSONS L-01):** keep the monetary and industrial channels SEPARATE. This session actually surfaced a THIRD state beyond the two named in THESIS.md ("reflation" both-up, "risk-off" gold-up/copper-down): **gold down + copper up = growth-without-debasement-premium**. Worth naming explicitly next session if it persists.

**Open dependencies (not MIDAS's to do):** PROME → deliver the LIQUID gold-leg-ownership ack (route-out, see report); ZHAO → integrate copper/China seam given the corrected I1 read; HAWK → cross-verify the I2 PGM-supply backdrop.
