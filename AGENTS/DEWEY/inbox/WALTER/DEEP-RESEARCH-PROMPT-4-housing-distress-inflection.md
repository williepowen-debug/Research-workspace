---
request_id: REQ-DEWEY-20260627-004
from: WALTER
to: DEWEY
created: 2026-06-27T20:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin — multiple distress threads need current data) + T1 (consolidates a national housing-distress coverage view)
originating_signal: National Mortgage News screenshot cluster (Will-Telegram 2026-06-27) — "Foreclosures 'could signal shifting housing market dynamics'" (Bonnie Sinnock, Apr-16-2026, Q1 Attom) + 5 RELATED teasers (distressed-sales "normalization" / zombie foreclosures rising / underwater-mortgage-rate 4-yr high / property-tax bills jump despite falling values / 31 of 50 riskiest markets cluster in 4 states). Paywalled headlines used as INVESTIGATION POINTERS, not routed.
clusters: BANK_COLLATERAL, CONSUMER_STAGFLATION
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (disposition PENDING)
---

# DEEP-RESEARCH PROMPT 4 — Is US residential housing distress inflecting? (current data behind the Q1-vintage NMN headlines)

**Origin note (the method Will named 6/27):** these were paywalled NMN headlines Will couldn't read. We're NOT routing the headlines — we're using the *existence* of the articles as pointers to a topic worth investigating, and asking DEWEY to recover what they're communicating + pull the **current** underlying data (the articles are ~April-vintage / Q1 Attom, so a key job is refreshing to the latest prints).

**Decision question:** Is US residential housing distress genuinely *inflecting* (foreclosures / underwater / zombie / distressed-sales), where is it geographically concentrated, and what does the **current** data show vs the Q1-vintage "shifting dynamics" framing?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the multi-thread current picture — foreclosure trajectory + negative-equity rate + zombie/vacant + distressed-sales share + geographic concentration, refreshed past the Q1/April vintage, and whether they cohere into "inflecting" vs "normalizing."
- **(b) Consequence:** housing-deflation thesis TIMING (CARL) + FL-distress escalation (CORAL) + bank/GSE residential-collateral trajectory (REGINALD). Separates a genuine distress inflection from the "market normalization" counter-read.

## `/deep-research` prompt (paste-and-go)

> US residential housing distress in 2026 — is it inflecting or normalizing, and where is it concentrated? Investigate and pull the CURRENT data behind this cluster of (mostly Q1-vintage) claims: (1) foreclosure activity — Attom/ICE Q1 and latest-2026 foreclosure filings, starts, completions, and YoY change, and whether "foreclosures surged ahead of last year in a way that points to shifting dynamics" holds in the most recent print; (2) negative equity — the current share of mortgaged homes underwater (test the "underwater mortgage rate hits a 4-year high" claim), by vintage (2022-2024 purchases) and geography; (3) zombie / vacant foreclosures — count, trend, and the states most affected; (4) distressed-sales share — level and trend, and the competing "distressed sales show signs of market normalization" read; (5) property taxes rising despite falling home values — magnitude and which states; (6) the "31 of 50 riskiest housing markets cluster in 4 states" claim — which 4 states/markets, and the risk metric used (affordability, equity, unemployment, foreclosure). Scope: in-bounds = US residential (single-family + condo) distress, equity, foreclosure, property-tax burden, geographic concentration; out-of-bounds = commercial real estate, mortgage-rate forecasting. Timeframe: 2025–2026, prioritizing the most recent available prints over Q1. Region/entities: US national + the most-stressed states/metros (note FL specifically — it feeds a dedicated FL agent). This informs: the housing-deflation thesis timing, FL-distress escalation, and bank/GSE residential-collateral trajectory — specifically whether the distress threads cohere into an inflection or a normalization. Prioritize primary sources (Attom, ICE/Black Knight Mortgage Monitor, CoreLogic/Cotality, Census, FHFA, state property-appraiser data); flag where claims are stale, model-specific, or contested, and separate "inflecting" evidence from "normalizing" evidence.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260627-004; WALTER routes as a `research-output` signal (→ CARL / CORAL / REGINALD, RED info) and closes the ledger row.
