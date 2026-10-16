# VULCAN intake gaps — completed WALTER design and live sizing

2026-10-16; requested by VULCAN October15, completed under Will's instruction to work through unfinished WALTER work. Implementation owner: PROME / Research-Intake. This is a concrete recommendation, **not deployed** and not a new collection approval. WALTER leaves the lane read-only. Review at next coordinator maintenance pass; source request is consumed for the design decision only.

## Recommendation

1. Add a bounded AI-financing collection, routed to LIQUID/BROCK for financing and VULCAN for capex sustainability. Exact tested query and locale are in `research/2026-10-16_finish/intake-design-results.json` under `ai-financing`. Seven-day query returned56items; it recovered the Volta lender-exposure story and CoreWeave debt stress. It also returned equity pricing commentary, so collection is a discovery feed, not an automatic event/trigger. Pricing terms still require article bodies, initial-talk reference, final terms, yield basis and publication clock. Retain no-source/no-grade outcomes.
2. Add a Korean-locale collection only with an explicit per-query locale capability (`hl=ko, gl=KR, ceid=KR:ko`). Tested native query returned100items, including Yonhap, MoneyToday and ElectronicTimes.100is a response ceiling, not totalcoverage; the broadHBM sample is product-announcement-heavy. Before deployment, narrow to production/orders/component terms and named outlets, preserving counterevidence. The existing URL builder is English-US; copying only query text would not reproduce this test. Native-language collection and English WATCH_FOR are separate paths; translation must retain originaltitle+URL and cannot be silently assumed.
3. Add GPU collateral/useful-life collection as discovery, routed BROCK/LIQUID financing and VULCAN assumptions. Exact tested query returned7items this week, including unrelated9fin event and broaderOracle/SpaceX stories. Narrow Google relevance is not guaranteed. Body verification and domain filtering remain necessary; the query is not a measured GPU valuation series.

No numerical fleet threshold changes. All three queries are free GoogleNewsRSS; no new vendor spend or licensed-access claim. Use existing weekday cadence, `when:7d`, URLdedup, publication-time field and source verification. Do not make a zero-hit day evidence of no stress. A two-week observation review should measure relevant unique bodies found, false alerts, misses against these known positive cases, and distinct publisher families, not raw headlinecount. Proposed review begins only after an actual deployment receipt.

## R3 matcher result

Real lane matcher,5,498unique stored headlines sinceSeptember16,163live query results plus explicit synthetic controls; no lane mutation. Full hits retained in intake-design-results.json.

- **Reject `HBM order cut`:** `cut` is threecharacters and discarded. It matched two historical headlines about Samsung/AMD and futureHBM orders, plus the synthetic denial. Cannot signal a cut.
- **Do not deploy unmeasured pricing phrases:** `Volta price talk`, `Volta loan pricing`, `CoreWeave loan pricing` matched only synthetic positives, missing actual recovered Volta titles. Zero historical hits do not establish useful recall.
- `GPU useful life` has one historical on-topic item; `GPU collateral`8 and `GPU depreciation`9 non-synthetic hits. These are topic matches, including opinions and a suspect rehost, not verified events. Keep discovery-only unless VULCAN explicitly adopts precise WATCH_FOR candidates under R3.
- `DRAM component shipments` matched only its synthetic positive; live recall not established.

**Disposition of VULCAN ask:** YES to the three coverage objectives; bounded deployment recommendation for financing, refine GPU noise, and implement/test Korean locale before adoption. NO to copying the suggested short-word phrases directly. No silent production change or new alert promise.

## GIBBS and article-age carry

GIBBS remains scheduled for first owner session October19 (L704). Owner-proposed WATCH_FOR phrases are still unset; WALTER does not invent/adopt its alert criteria before that session. Existing routing wiring remains active. Ask GIBBS at that already-planned session for entity-bound phrases; then run the same historical/live R3 path. The observed old-article/new-batch issue is a separate lane proposal: retain sourcepublicationdate and flag its disagreement with collectiondate. No automatic discard solely because old: an old primary can be newly decision-relevant.

## Reproduction

`python3 AGENTS/WALTER/research/2026-10-16_finish/intake_design_probe.py` reads the lane and fetches publicRSS only; outputs remain underWALTER. Exact configSHA and sample timestamps in results. Source bodies were not fully assessed for all163queryrows; no precision/recall percentage asserted. This is completed design/sizing, not consumer acceptance or deployment.
