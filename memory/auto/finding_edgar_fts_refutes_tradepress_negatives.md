---
name: edgar-fts-refutes-tradepress-negatives
description: Trade-press absence ≠ market absence — refute pricing/event negatives via EDGAR full-text search before grading
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8174072b-8cba-4d9a-a553-26cee268b00b
---

When research concludes "no print above X ever occurred" (or any negative) from trade-press/aggregator evidence, the coverage is often paywall-gated (PitchBook/Creditflux/Bloomberg) and systematically hides tail prints. Structured-finance pricing lives in PRIMARY filings: BDC/fund 8-Ks disclose CLO tranche spreads at closing; SC TO-I/A amendments disclose tender prorations. EDGAR full-text search (efts.sec.gov) over the window is the cheap refute pass.

**Why:** LIQUID LIQ-03 (7/1/26): researcher graded MISS ("CLO AAA never >SOFR+160 in H1") from trade-press sweeps; the adversarial verifier ran EDGAR and found Diameter PC CLO 8-Ks pricing AAA at S+170/185 in-window — flipped the grade to ACHIEVED. Same session, the gates-negative verify used EDGAR FTS ("repurchase requests exceeded", "pro rata basis" on SC TO-I/A) to make a news-negative actually load-bearing.

**How to apply:** before resolving any prediction or propagating any "never happened / none found" claim about priced deals, tenders, or fund events, run an adversarial pass explicitly pointed at EDGAR full-text + per-CIK filing lists for the window. Related: [[verify-existence-external-primaries]].
