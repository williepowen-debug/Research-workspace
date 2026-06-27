---
name: insurer-entity-scope-trap
description: "an insurer balance-sheet figure (Level-3/leverage/Bermuda book) is scope-dependent across parent-segment vs sub-holding vs statutory-sub-group; gross−net = the third-party NCI sidecar; and a \"verified\" pundit number can be a stale vintage"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 9d8db5a0-1cc5-4069-9175-12f92381f859
---

When verifying a contested insurer balance-sheet figure, the same entity reports 3+ non-equal "totals" — grade against the WRONG scope and you'll false-confirm or false-refute. (DEWEY 2026-06-27, Apollo/Athene, REQ-DEWEY-20260627-001.)

**The scopes (Athene case):** (a) parent-consolidated *segment* — Apollo "Retirement Services" (APO CIK 1858681); (b) sub-holding consolidated — Athene Holding Ltd (CIK 1527469 — *still files a 10-K* via registered debt/preferred despite being Apollo-owned); (c) statutory *sub-group* — Athene Bermuda Sub-Group AARe/ALRe (BMA Financial Condition Report PDF, not EDGAR).

**The reconciliations that resolve contested figures:**
- **Gross ↔ net = the third-party NCI sidecar.** Burry's "$217bn Bermuda" ≈ a net/economic measure; gross AARe = $315bn (FY2024 BMA filing); the gap is the ACRA/ADIP co-invest, which surfaces on the GAAP balance sheet as the **noncontrolling-interest line** (Athene Holding NCI = $15.9bn = equity-incl-NCI $33.7bn − parent $17.8bn). Find the NCI, you find the gross/net bridge.
- **Leverage is equity-definition-dependent.** Apollo consol 11.8× (incl-NCI) / 23.4× (parent) vs Athene Holding standalone 13.3× / 25.1× vs Burry's "16.6×" (not reproducible on any GAAP basis) — all "true," none equal.
- **Date the figure.** A pundit number can be ~accurate for an old vintage yet materially stale: Athene Level-3 = $104bn at YE2024 (≈ Burry's "$103bn") → $147.7bn YE2025 → $154.8bn Q1-2026. The high-value move is to pin the source vintage AND pull the current primary to show the delta (here +49% YoY).
- **Level-3 ≠ collateral-typed.** The fair-value hierarchy is NOT broken out by underlying collateral — "Athene = AI/data-center amplifier" is an inference, not a disclosed fact.

**How to apply:** before grading an insurer figure verified/refuted, pin its scope + denominator, reconcile gross↔net via the NCI line, and date it to its filing vintage. Recurs on any SHADE/BROCK insurer-PC-nexus work. Generalizes [[finding_number_carries_threshold_unit_source]]; pairs with [[feedback_suspect_fresh_pull_over_curated_record]] and [[finding_private_by_construction_unverifiable]].
