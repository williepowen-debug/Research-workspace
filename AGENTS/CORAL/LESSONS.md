# LESSONS.md — CORAL Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever. Verified mistakes that burned us — each with a prevention rule. For Will's working preferences and data-source learnings, see `MEMORY.md`. Seeded from REGINALD/OZK LESSONS during CORAL spinout 2026-06-19: shared structural rules copied, FL-specific rules added.*

---

### [Data] — Verify Agent Data Against Primary Filings
**Mistake:** PSEC was reported at 35% PIK across the fleet — actual was 8.6% per SEC filing. Agent-relayed and aggregator numbers propagate as fact.
**Rule:** Before any metric informs a trade or a cross-agent signal, verify against the primary — SEC 10-K/10-Q for banks, FL OIR for insurers, FL Realtors for housing, the Call Report for bank ratios. Agent research and trade-press headlines are a starting point, not ground truth.

### [Data] — Verify Real-Time Prices Before Building Narratives
**Mistake:** A STATUS file stated Brent $118–125 and an entire FL energy-shock cascade was built on it. Actual was ~$81. The error propagated through multiple sections before being caught.
**Rule:** Confirm price/level inputs from a live source before modeling downstream effects. A large error on one input produces garbage on every output.

### [Analysis] — Don't Confuse a Thermometer With the Mechanism (FL condo inventory)
**Mistake pattern:** The "FL condo inventory >9 months = distress" threshold breached in Mar 2026 (9.1mo) then reverted to 8.9mo in April — sales rose, inventory tightened. Treating the single-month breach as confirmation of an accelerating cascade would have been wrong.
**Rule:** Separate the durable *mechanism* (SIRS reserve gap, assessment cascade, receivership pipeline — structural) from the monthly *thermometer* (inventory months, DOM — noisy, mean-reverting). State which one moved. A one-month threshold tag is not a trend.

### [Analysis] — A Falling Early-Delinquency Bucket Can Be Up-Migration, Not Cooling
**Mistake pattern (caught in self-steelman, 2026-06-25):** I read SBCF's 30-89d past-due −14% QoQ as "cooling / benign" and led with it — while the *same* print showed nonaccrual +32% QoQ ($72→95M) and the 60-89 sub-bucket up ~10×. By the OCC bucket-migration model (loans migrate UP: 30-89 → 90+ → nonaccrual), a *falling* early bucket with a *rising* late bucket is the cascade **steepening** (loans rolling forward), not curing. Leading with the early-bucket headline inverts the signal.
**Rule:** Never grade a delinquency trend off one bucket. Read the **whole aging ladder QoQ** (30-59 / 60-89 / 90+ / nonaccrual) together. A falling early bucket is only "cooling" if the later buckets are ALSO flat/down; if nonaccrual or 60-89 is rising, it's up-migration — flag it as the cascade advancing. The sharpest fresh-quarter signal usually sits in nonaccrual, not the headline 30-89.

### [Analysis] — FL Stress Is Timing-Delayed, Not Absent
**Mistake pattern:** Framing the FL cascade as acute/imminent when the transmission is slow. The snowbird-$ hole and assessment-default wave land on a winter-2026-27 timeline, not Q2-Q3 2026.
**Rule:** Date the *expected landing* of each FL channel explicitly. Don't upgrade to acute on a structural-but-slow signal. "Real but delayed" is the honest call.

### [Process] — Reconcile the FL Read With MARCO Before Publishing
**Mistake risk:** CORAL and MARCO both cover FL condo inventory, airports, and migration. Divergent numbers across two agents on the same geography is data fiction.
**Rule:** Before publishing an FL housing/airport/migration figure, cross-read `../MARCO/STATUS.md`. MARCO owns the population-driven read; reference it rather than maintaining a drift-prone parallel copy. Flag genuine disagreements to REGINALD, don't paper over them.

### [Process] — Date Your Data
**Rule:** Every metric carries a date and a source tag. "FL #2 foreclosure" or "Citizens ~$678B" means nothing without the as-of date. FL housing and insurance data go stale within a month.

### [Process] — STATUS.md Is a Dashboard, Not a Research Report
**Rule:** STATUS.md is current state — signal status, thresholds, FL bank exposure. Research detail belongs in `sources/`, `research/`, or `workbook/`. Keep STATUS under 250 lines.

### [Data] — A Scope Label Is a Claim Too: Verify Personal-vs-Total Before It Becomes Canon
**Mistake (caught 2026-07-21):** CORAL carried "Citizens 294,253 **personal-lines** policies (May 15)" as a dashboard canonical for ~5 weeks. The number was real but the LABEL was wrong — Citizens' own policies-in-force reports show it was a mid-May **TOTAL** (true Apr-30 personal was 289,824). The mislabel then manufactured a phantom cross-agent divergence with AEOLUS (whose ~395K was simply a stale Jan-31 total), which cost an open reconcile item across three sessions — chasing a scope difference that didn't exist.
**Rule:** when adopting any count/level from press, verify the SCOPE dimension (personal vs total, capped vs uncapped, SA vs NSA, monthly vs cumulative window) against the primary before writing the label into a dashboard row. A wrong label is worse than a wrong number: the magnitude looks plausible, so it survives sanity checks while corrupting every downstream comparison. Most treacherous exactly when scopes nearly coincide (Citizens is ~98% personal, so total ≈ personal and nothing looked off).

### [Data] — In Season, Pull the Full NHC Advisory, Not the Outlook
**Mistake pattern (near-miss 2026-07-21):** a research pull based on the NHC Tropical Weather Outlook (MIATWOAT) carried TS Bertha as "45 kt, S of Panama City" with no track — reading it alone would have left the FL-landfall trigger question open. The full public advisory (MIATCPAT2) showed 60 mph, moving W AWAY from FL toward MS/LA, weakening — trigger question closed in one fetch.
**Rule:** any time a named storm exists, the advisory (position/intensity/track/watches) is the load-bearing document; the outlook is only a formation-odds product. Verify trigger-adjacent storm claims against the advisory before writing dispositions.

---

*Last reviewed: 2026-07-21 (added scope-label + NHC-advisory rules). Seeded 2026-06-19 during spinout from REGINALD/OZK LESSONS.*
