# HOMER Promotion — DAEDALUS Structural Review + Rulings

**Author:** DAEDALUS · **Date:** 2026-07-12 · **Status:** EXECUTING TODAY (Will directive 7/12 — overrides CARL's wait-until-post-7/24 recommendation; review compressed, not skipped)
**Case:** `inbox/2026-07-12_from-CARL_homer-promotion-case.md` (CARL, Will-directed)
**Evidence:** `builds/homer_promotion/MANIFEST_D_homer.md` (full HOMER read + CARL housing rows + CREED + external-consumer sweep)

## Verdict: PROMOTE — the case is sound and the evidence strengthens it

- HOMER is structurally clean (7/10 restructure verified by its own SV; no open defects; KB properly FROZEN w/ provenance).
- External consumers = **0 live references outside CARL's tree** → lowest-risk promotion of the three precedents (OZK/CORAL/AEOLUS all had live consumers to rewire).
- The CARL-retain set is actually ~5 rows, not ~10 — MORE of the housing section is pure asset-market than CARL estimated. The domain has outgrown the sub-scope even more than the case claims.
- Counter-case (current structure caught CRL-03 cleanly) is real but optimizes for the past leg; Path C ACTIVE-RED + the 2026 MF maturity wall is the forward load.

## ★ Rulings (the 4 judgment calls)

| ★ | Ruling | Basis |
|---|---|---|
| **CREED disposition** | **HOMER = primary owner** of the Trepp CMBS-MF row, the GSE-vs-CMBS divergence, and Sun-Belt-MF realization tracking. **CREED keeps non-MF CMBS** (office/retail/industrial/lodging + fund/NAV + REIT tape) and **demotes S5 to a HOMER-fed cross-reference** (not retired — avoids shrinking CREED's matrix denominator mid-cycle; S5 just fired). CREED pulls the whole Trepp print anyway for office; it routes the MF row to HOMER (option b in MANIFEST_D §5) — one pull, one owner, no dup parse. Matrix change is CREED's to apply → **task packet to CREED inbox** (Tier-2, applies at next spawn), NOT a silent edit. | MF data not separable at source; no CREED workbook exists to migrate; S5/S6 double-count risk is live today |
| **CRL-06 / CRL-23** | **Parent-retain, HOMER = data owner** (the case's own fallback, now firm). Both are CARL thesis-scoring instruments (V10 / Vector #10 on CARL's convergence matrix); moving them means duplicating thesis machinery. HOMER opens its own **HOM-xx** ledger for new predictions; feeds ATTOM/builder data upstream. CRL-06 metric-clarification (starts vs filings vs REO — may already be CONFIRMED at starts-level) stays **CARL-owed**, flagged in the handoff. | MANIFEST_D §4/§7.3 |
| **WAL queue order** | HOMER jumps WAL — **decided by Will 7/12** (ordering the promotion today). Recorded, not re-litigated. WAL remains next-promotion-candidate on ROSTER. | Will directive |
| **Rate/mortgage-spread surface** | **HOMER owns the mortgage-specific surface** (30Y PMMS, 10Y-FRM spread, FHA-vs-Conv DQ spread) — it's housing-demand mechanics and nobody else owns it. Treasury/Fed rate direction stays **referenced-only** (BROCK/HENRY upstream). One-figure rule: mortgage spread = HOMER's number. | MANIFEST_D §3 row 3; no upstream owner exists for the spread itself |

## Seam resolutions (beyond the case's §3 table)

1. **Trepp MF triple-tracking collapses to one owner:** HOMER owns the figure; CREED (via its own pull, routing MF row) and REGINALD (consumer, keeps its bank-collateral interpretation) cite HOMER's number. REGINALD note rides the promotion handoff packet — its own STATUS already flags the sub-series reconciliation confusion this fixes.
2. **FL condo reconciliation (CORAL↔HOMER):** live divergence confirmed (CORAL broad-index −6.1% vs HOMER county medians −8/−10%). Not blocking (different metrics), but the reconcile-to-one-figure pass is logged as a HOMER first-boot docket item w/ CORAL cc.
3. **Stale-STATUS mitigation (promotion-today consequence):** HOMER's own STATUS is 34d stale vs CARL's current housing rows. The new top-level STATUS is REBUILT from CARL's current rows (the fresher source) on HOMER's structure — not a straight copy — and HOMER's first-boot mandate = the owed full data refresh (ATTOM Q2 lands 7/16, perfectly timed).

## Migration plan (execution WPs)

- **WP-H1 (editor):** `git mv AGENTS/CARL/sub_agents/HOMER AGENTS/HOMER` (history preserved) → top-level CLAUDE.md rewrite (standalone boot/closeout, git pathspec, staleness wiring, docket, SV-protocol section retired → NEXUS_BRIEF + inbox/outbox pattern) → STATUS rebuild ≤250 from CARL current rows → fresh SCRATCH/NEXUS_BRIEF/LESSONS/MEMORY/board_log/inbox/outbox → thesis/PREDICTIONS.tsv (HOM-xx, preamble notes CRL-06/23 parent-retained w/ HOMER-as-data-owner).
- **WP-H2 (editor):** CARL-side shed: STATUS housing section 28→~5 retained rows + pointer block to HOMER; CLAUDE.md sub-agent roster line + TEAM.md update; solves CARL's over-cap (266→~240) as the case predicted. CARL is idle+committed (verified 7/12) → direct edit authorized under the promotion approval.
- **WP-H3:** handoff packets: CREED (S5 demotion + Trepp MF routing), REGINALD (consume HOMER's MF figure + first-class HOMER→REGINALD edge), CORAL (FL reconcile pass cc), CARL (completion note + CRL-06 clarification owed).
- **WP-H4:** registration — ROSTER (+HOMER, provenance "promoted from CARL sub-agent 2026-07-12"), root CLAUDE.md chain (+`HOMER → {CARL, REGINALD}` + HENRY wealth-effect edge), AGENTS.md, WALTER who_cares, then FLEET_MAP row (L2 at entry — has live accruing ledgers + structured record, unlike a scratch L1 build; first content-grade after first solo session) + FLEET_DIRECTORY regen. Batched with the OSPREY/FALCON registration (PAT-047 order).
