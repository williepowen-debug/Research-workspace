---
request_id: REQ-DEWEY-20260702-007
from: PROME (Will-directed batch 2026-07-02 — fleet-mined slate; WALTER logs + routes, see AGENTS/WALTER/inbox/2026-07-02_from-PROME_dewey-batch2-13-prompts.md)
to: DEWEY
created: 2026-07-02T04:00:00Z
state: NEW
flag_trigger: T3 (load-bearing-but-thin)
originating_evidence: "⚠️ urea $850 is single-source (WALTER aggregator, CORRECTED-FRAMING 0.60) — VERIFY against primary" (AGENTS/CARL/ROADMAP.md; fetch paths 403-blocked); "sole forward-CPI rail" (AGENTS/NEXUS/SIGNALS.md S-26060701). Three miners converged (CARL+NEXUS+MARCO).
clusters: V6 food squeeze / Channel-1 thermometer / R5 forward-CPI rail / CONSUMER_STAGFLATION
ledger_ref: AGENTS/WALTER/registry/DEEP_RESEARCH_FLAGGED_LOG.tsv (WALTER logs row at next boot, disposition QUEUED)
run_order: 7 of 13
deliver_by: 2026-07-09 (CPI 7/14; if run before ~7/10, use June WASDE per the prompt's own fallback)
---

# DEEP-RESEARCH PROMPT 11 — Food-supply shock stack: fertilizer verification + Apr-Jun produce audit for the 7/14 CPI fork

**Decision question:** Does the supply path support Food-CPI >4% YoY by Q4 (hold/cut CRL-10's 75%), and if F&V CPI holds ≳+5% on 7/14 while pump prices fall, is that labor re-weighting up or an uncaught supply shock?

**Materiality gate:**
- **(a) What a cheap verify can't answer:** the urea price conflict ($850 single-source vs CARL's $585 May row) needs multi-primary triangulation with basis reconciliation (retail vs benchmark); the Apr-Jun produce shock catalog and Russia/Qatar/Iran export status are scattered-source assembly work; CARL's own fetch paths are 403-blocked.
- **(b) Consequence:** CRL-10 confidence + STATUS urea-row correction before 7/14; ES-MARCO-08 fork adjudication → Channel-1 thermometer and prediction #14 (74%); promotes or kills NEXUS's sole surviving forward-CPI rail (S-26060701) into the stagflation-trap input.

## `/deep-research` prompt (paste-and-go)

> Food-CPI supply-path verification ahead of the Jul-14 June-CPI fork (report needed by 2026-07-09). IN-BOUNDS: (1) Triangulate current urea price from ≥2 independent public primaries (AFBF/DTN Progressive Farmer retail survey, World Bank Pink Sheet, Green Markets prints, trade press citing Argus/CRU) — reconcile CARL's $585/t May-1 US row vs the single-sourced "$850/t 4-yr high" claim; state which is right, with vintage and US-retail-vs-international-benchmark basis; include DAP and ammonia. (2) Russia ammonium-nitrate/urea export status post-Mar-24-2026 (bans, quotas, actual flows — trade press, UN Comtrade shadow). (3) Test NEXUS's 6/27 de-rate: have Qatar (QAFCO) urea/ammonia exports resumed post-Hormuz-reopening, and what is Iran ammonia status? (4) El Niño leg: latest ECMWF + NOAA CPC/IRI ENSO plume vintages — probability of the claimed ~+3C NINO3.4 Oct-Nov 2026 peak — plus the most recent USDA WASDE (Jul-10 if out, else June) 2026/27 wheat/corn/soy outlooks. (5) Catalog ALL Apr-1-to-Jun-30-2026 US fresh-produce supply shocks (USDA/FSA disaster declarations, freeze/drought in CA/FL/TX/AZ, produce tariffs, reefer freight), each dated+sourced, and confirm which BLS CPI line item equals "fresh fruits & vegetables" as used in ES-MARCO-08. OUT-OF-BOUNDS: grocery-retail margins, meat/eggs/dairy, ag-labor/H-2A analysis (MARCO owns), energy-price forecasting, predicting the Jul-14 CPI print itself. TIMEFRAME: prices latest-available Jun-2026 vintage; shock catalog Apr-Jun 2026; ENSO/WASDE current official vintages. ENTITIES: USDA (WASDE, FSA), AFBF, BLS, ECMWF, NOAA CPC/IRI, Russia AN exporters, QAFCO, Iran ammonia, World Bank Pink Sheet.

**On return:** hand back to WALTER via `AGENTS/WALTER/inbox/DEWEY/` naming flag REQ-DEWEY-20260702-007; WALTER routes as a `research-output` signal (→ CARL action [CRL-10/V6] / MARCO action [ES-MARCO-08] / NEXUS, AEOLUS, LABOR info) and closes the ledger row.
