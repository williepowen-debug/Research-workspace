# HOMER — NEXUS Brief

**Status:** 🔴 CRITICAL — GSE-vs-CMBS multifamily divergence widening; builder margins at cycle-worst compression; foreclosure pipeline converting (not just accumulating)
**Domain:** U.S. housing asset-market + credit-structure — foreclosure pipeline, multifamily (GSE + CMBS books), mortgage rate surface, builders, pricing/inventory, state-level (FL/TX priority)
**Promoted:** 2026-07-12 from CARL sub-agent (Will-directed). This is HOMER's first NEXUS_BRIEF as a top-level peer agent.
**As of:** 2026-07-12 (promotion rebuild) | STATUS data vintage: May/June 2026 (CARL's freshest current rows at cutover) — see STATUS.md Open Items for the owed live refresh.

---

## VIEW

- **GSE-vs-CMBS multifamily divergence is the marquee open question.** Fannie MF serious DQ improved to 0.58% May (CRL-03 invalidated on its own pre-registered trigger — the GFC-approach in the GSE book is not firing). Trepp CMBS MF DQ resumed deteriorating to 7.23% June, maturity-adjusted 9.53% — a new multi-year high. Different books, different mod regimes: GSE extend-and-pretend cooled the headline; the CMBS book is realizing losses now (Sun Belt 2022-vintage cluster: S2 Capital $400M DFW fund $0-to-LPs, ~$900M TX CRE flagged for July auctions).
- **Builder margin crush is the sharpest of the cycle.** KB Home FQ2: operating margin 8.6%→2.5%, net income −75% YoY. Lennar FQ2 cut its FY26 delivery guide (rates + geopolitics, not energy). DHI/PHM Q2/Q3 report 7/22-23 — the next test of whether the FY27 tariff leg (CRL-23, CARL-owned prediction) starts showing up early.
- **Foreclosure pipeline is converting, not just accumulating.** Q1 2026 REO +45% YoY nationally, FL +108% YoY (greatest % rise nationally). ICE active FC inventory above pre-pandemic March-2020 levels for a 2nd consecutive month. ATTOM's Q2 print (7/16) is the next hard test and may already confirm CRL-06 (>70K/qtr) at the FC-starts level.
- **Nominal HPI is accelerating while real HPI stays negative.** Freddie +1.9% YoY May (3rd consecutive accel month) vs. Case-Shiller real −2.4% YoY (11th consecutive negative month). Realtor.com list prices (leading edge, −2.4% YoY) suggest the nominal series rolls over Jul-Aug.

---

## CALIBRATION

- **Conviction:** mechanism-HIGH on the GSE-vs-CMBS divergence and builder-margin compression (multiple independent primary sources); MEDIUM on pipeline-pace forecasting (878K 90+/FC figure is Feb-vintage, stale).
- **Diverge from parent-era HOMER by:** the pre-promotion STATUS (Jun-8 vintage, superseded banners layered on top) treated CRL-03 as open/alive; it resolved MISSED 2026-07-02 at CARL — this brief and STATUS.md reflect that resolution.
- **Cross-agent tensions known to me:** REGINALD independently sources the same Trepp CMBS-MF print (its own STATUS carries a parallel row) — the promotion is meant to collapse this to HOMER-primary/REGINALD-consumer, not yet executed. CORAL's FL condo figures (broad index) diverge in specifics from HOMER's (county medians) — different metrics, unreconciled.
- **Uncertain about:** whether the CMBS-book deterioration stays TX/Sun-Belt-concentrated or broadens nationally (CREED's own S5 signal was building/3, not fired, as of 7/4); whether the FY27 tariff leg (CRL-23) shows any early read-through in the 7/22-23 builder prints, 6-9 months ahead of its formal resolution window.
- **Failure patterns to mind:** verify the year explicitly on any web-pulled metric before treating it as load-bearing (HOMER's own Spawn5→6 postmortem — see LESSONS.md); don't let a hygiene/rebuild pass silently mask genuine data staleness (this rebuild is dated May/June, said so explicitly, not backdated to "current").

---

## CROSS-DOMAIN

**SENDING:**
- **CARL** — consumer-transmission-relevant housing reads (rent squeeze, condo K-shape, FHA K-shape context) stay CARL's own interpretation; HOMER feeds the underlying data. No new findings to push this session (promotion-build only).
- **REGINALD** — Path C collateral read (foreclosure pipeline, MF stress, Sun Belt realization cluster) — first-class chain edge as of this promotion. REGINALD's own STATUS already carries a parallel Trepp MF row; flag for reconciliation to HOMER-primary at REGINALD's next session.
- **HENRY** — wealth-effect edge on HPI inflections (nominal-accelerating/real-negative divergence, potential Jul-Aug nominal rollover per Realtor.com leading indicator).

**WAITING-FOR:**
- **ATTOM Q2 2026 foreclosures (7/16)** — first live test of the rebuilt agent; anchors the owed data refresh.
- **DHI FQ3 / PHM Q2 earnings (7/22-23)** — CRL-23 read-through.
- **CREED packet consumption** (S5 demotion + Trepp MF routing — delivered 7/12 to `AGENTS/CREED/inbox/`, lands at CREED's next Tier-2 spawn).
- **CORAL FL-condo reconciliation** — logged, not actioned.

---

*First NEXUS_BRIEF as a top-level agent. Prior parent-era SV channel to CARL is retired — see CLAUDE.md.*
