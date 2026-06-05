---
name: feedback-prediction-canonical-measure
description: "When revising a prediction, pull the canonical measure of the prediction's variable — not company-level or proxy evidence. Cross-level conflation (company revenue → industry employment) silently overweights wrong-tier signals."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c0427123-badd-4e1a-b650-13ba7c5f9ea8
---

When a prediction names a variable (e.g., "Temp YoY <-6%"), there's a **canonical measure** — the data series that authoritatively answers the question. For "Temp YoY" the canonical is BLS CES Temp Help Services. For "U-3 ≥X%" it's BLS empsit. For "credit losses >X%" it's the loss-rate filing. **Update the prediction using THAT measure at every revision; do not substitute proxies (company revenue, single-firm guidance, clustered announcements) even when proxies are the noisiest/freshest signal.**

**Why:** LAB-01 (Feb 2026) was written at 85% confidence anchored on KELYA company guidance, then revised at 65% on RHI/KFRC sequential prints, then at 75% ("TILTING CONFIRMED") on KELYA Q1 LOSS — all company-tier evidence. The canonical BLS CES Temp Help Services series was published monthly and showed temp employment GROWING through Q1 (Jan +9.1K, Mar +4.4K, Apr +7.9K SA; ASA index +4.9% YoY). The May 8 NFP release already invalidated the prediction; the falsifying data sat available for 25 days until a Phase 1 deep-read forced the canonical pull. The June 2 upgrade from 65% to 75% was wrong-direction — made with the falsifying data already public.

**How to apply:** At write-time of any new prediction, identify the canonical data source explicitly (e.g., "anchor: BLS CES industry table B-1, line: Temp Help Services, SA, YoY"). Write it in the prediction notes. At every confidence revision, pull that exact source — not the most recent company print, not the most cited talking point. If the canonical source can't be pulled in-session, mark the revision as PENDING and don't update confidence on proxies alone. This applies broadly: industry employment vs company revenue, sector default rate vs single-firm credit, system-level stress vs one-bank markdown, cohort behavior vs viral anecdote. Same pattern shows up in [[feedback_yoy_baseeffect_use_multiyear_stack]] (using noisy nominal YoY when canonical is multi-year stack) and [[feedback_verify_existence_external_primaries]] (trusting fleet consensus when canonical is independent primaries). Companion to [[feedback_dont_bank_unpassed_forecast]] — separate "what the proxies say" from "what the resolving data will say."
