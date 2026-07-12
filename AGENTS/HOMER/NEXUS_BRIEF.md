# HOMER — NEXUS Brief

**Status:** 🔴 CRITICAL — GSE-vs-CMBS multifamily divergence widening (both legs now live-verified); builder margins at cycle-worst compression; foreclosure pipeline converting (not just accumulating, though May REO decelerated MoM — watch)
**Domain:** U.S. housing asset-market + credit-structure — foreclosure pipeline, multifamily (GSE + CMBS books), mortgage rate surface, builders, pricing/inventory, state-level (FL/TX priority)
**Promoted:** 2026-07-12 from CARL sub-agent (Will-directed). This is HOMER's second NEXUS_BRIEF — first was the promotion-rebuild; this one reflects HOMER's first live-data session.
**As of:** 2026-07-12 (first live-data session) | STATUS data vintage: refreshed this session (PMMS, ICE pipeline, NAR EHS) — Fannie/Trepp/Case-Shiller/HPI remain at their normal release-cadence vintage (May/June), which is expected lag, not staleness.

---

## VIEW

- **GSE-vs-CMBS multifamily divergence is the marquee open question — both legs live-verified this session.** Fannie MF serious DQ improved to 0.58% May (confirmed via CalculatedRisk/PR Newswire/StockTitan; CRL-03 invalidated on its own pre-registered trigger — the GFC-approach in the GSE book is not firing). Trepp CMBS MF DQ resumed deteriorating to 7.23% June (confirmed via Multi-Housing News/Yield PRO/ConnectCRE), maturity-adjusted 9.53% — a new multi-year high. Different books, different mod regimes: GSE extend-and-pretend cooled the headline; the CMBS book is realizing losses now (Sun Belt 2022-vintage cluster: S2 Capital $400M DFW fund $0-to-LPs, ~$900M TX CRE flagged for July auctions). **New this session: REGINALD is independently citing an 8-month-stale Fannie/Freddie GSE row (0.75% Nov-2025) that contradicts this — flagged as a route-out, see reports/2026-07-12_domain-sweep.md finding #1.**
- **Builder margin crush is the sharpest of the cycle.** KB Home FQ2: operating margin 8.6%→2.5%, net income −75% YoY. Lennar FQ2 cut its FY26 delivery guide (rates + geopolitics, not energy). DHI FQ3 reports 7/21, PHM Q2 reports 7/22 (both confirmed dates, corrected by a day from the inherited estimate) — the next test of whether the FY27 tariff leg (CRL-23, CARL-owned prediction) starts showing up early.
- **Foreclosure pipeline is converting, but May's REO print decelerated MoM (-20%) — first deceleration since the "converting, not just accumulating" narrative began.** Q1 2026 REO +45% YoY nationally, FL +108% YoY. ICE active FC inventory 280K, +34% YoY, highest in 6 years (3rd consec month above pre-pandemic Mar-2020 levels). ATTOM's Q2 print (~7/16, est. — no confirmed date/press-release yet) is the next hard test; the CRL-06 metric-clarification data package is now delivered to CARL (starts/filings already confirm >70K since April; REO does not).
- **Nominal HPI is accelerating while real HPI stays negative.** Freddie +1.9% YoY May (3rd consecutive accel month) vs. Case-Shiller real −2.4% YoY (11th consecutive negative month). Realtor.com list prices (leading edge, −2.4% YoY) suggest the nominal series rolls over Jul-Aug — next test is the confirmed Jul 28 Case-Shiller/Freddie HPI release. 30Y PMMS refreshed to 6.49% (Jul 9, +6bps off a 7-week low) — still no genuine refi relief.

---

## CALIBRATION

- **Conviction:** mechanism-HIGH on the GSE-vs-CMBS divergence and builder-margin compression (all 4 spot-checked this session against primaries, 0 drifts); MEDIUM on pipeline-pace forecasting for Q2 (starts/filings tracking >70K again, but May's REO deceleration is a genuinely open thread, not yet a trend).
- **Diverge from parent-era HOMER by:** the pre-promotion STATUS (Jun-8 vintage, superseded banners layered on top) treated CRL-03 as open/alive; it resolved MISSED 2026-07-02 at CARL — this brief and STATUS.md reflect that resolution.
- **Cross-agent tensions known to me:** REGINALD independently sources the Trepp CMBS-MF print (own STATUS carries a parallel row, self-flagged sub-series confusion) AND an 8-month-stale GSE Fannie/Freddie row that the promotion's REGINALD handoff packet didn't address (new catch this session — see sweep report). CORAL's FL condo figures (broad index) diverge in specifics from HOMER's (county medians) — different metrics, unreconciled, 2nd session flagged without action.
- **Uncertain about:** whether the CMBS-book deterioration stays TX/Sun-Belt-concentrated or broadens nationally (CREED's own S5 signal was building/3, not fired, as of 7/4); whether the FY27 tariff leg (CRL-23) shows any early read-through in the 7/21-22 builder prints, 6-9 months ahead of its formal resolution window; whether May's REO MoM deceleration persists into June.
- **Failure patterns to mind:** verify the year explicitly on any web-pulled metric before treating it as load-bearing (HOMER's own Spawn5→6 postmortem — see LESSONS.md); the two-clock workbook headers caught 3-4 weeks of drift this session on their first live test — keep running that check every boot, promotion didn't make HOMER immune to the pattern it was built to catch.

---

## CROSS-DOMAIN

**SENDING:**
- **CARL** — CRL-06 data package delivered (`reports/2026-07-12_CRL-06-data-package.md`) — starts/filings basis has confirmed >70K/qtr since Apr 17, REO basis has not; CARL's resolution call has been open 87 days on this exact ambiguity. Consumer-transmission reads (rent squeeze, condo K-shape, FHA K-shape) stay CARL's own interpretation.
- **REGINALD** — Path C collateral read (foreclosure pipeline, MF stress, Sun Belt realization cluster) — first-class chain edge. **New this session:** REGINALD's GSE Fannie/Freddie row is 8mo stale and contradicts HOMER's current read — routed via PROME (sweep finding #1), not yet confirmed actioned.
- **HENRY** — wealth-effect edge on HPI inflections (nominal-accelerating/real-negative divergence; Jul 28 Case-Shiller/HPI release is the next rollover test). No new push this session beyond the standing view above.

**WAITING-FOR:**
- **ATTOM Q2/June 2026 foreclosures (~7/16, unconfirmed)** — neither report existed as of this boot; re-check next session.
- **NAHB HMI (Jul 16, 10am ET), Census starts (Jul 17), DHI FQ3 (Jul 21, 8:30am ET), PHM Q2 (Jul 22, 8:30am ET)** — all dates/times confirmed this session.
- **Case-Shiller / Freddie HPI (Jul 28, confirmed)** — nominal-rollover test.
- **CREED + REGINALD packet consumption** — both verified still on disk/unconsumed this session (expected, lands at their next boots — not a problem).
- **CORAL FL-condo reconciliation** — logged 2 sessions running, not actioned either time.

---

*Second NEXUS_BRIEF, first reflecting a live-data session. Prior parent-era SV channel to CARL is retired — see CLAUDE.md.*
