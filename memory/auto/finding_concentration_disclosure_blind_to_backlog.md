---
name: finding_concentration_disclosure_blind_to_backlog
description: The "no customer ≥10% of revenue" disclosure keys on RECOGNIZED revenue, so it returns clean on a backlog that is ~50% one counterparty — check RPO, not the concentration line
metadata:
  type: reference
---

**A customer-concentration screen run against the standard SEC disclosure returns a FALSE NEGATIVE on long-dated contracted backlog.** The disclosure ("no single customer accounted for 10% or more of our total revenues") keys on **recognized revenue**. Contracted-but-unrecognized exposure lives in **remaining performance obligations (RPO)** and is invisible to it.

**Worked case (DEWEY DR-1, 2026-08-02, all SEC-primary):** ORCL's FY2026 10-K states *"No single customer accounted for 10% or more of our total revenues in fiscal 2026, 2025 or 2024."* In the same filing, **RPO went $138B → $638B** (4.6×) on "certain significant cloud contracts," with **only 12% expected to convert within twelve months** — and S&P estimated roughly **half of that $638B is one counterparty (OpenAI)**. Both statements are true and they do not conflict. The concentration simply had not reached the P&L yet.

**Why this bites:** the clean concentration line is exactly what a screen, a checklist, or a risk model reads. On AI-era infrastructure contracts — huge, multi-year, front-loaded on capex and back-loaded on revenue — the gap between backlog concentration and revenue concentration is at its widest precisely when the exposure is at its largest.

**How to apply:** when assessing counterparty concentration, read **RPO / backlog disclosures and the surrounding prose**, not the revenue-concentration line. Issuers often disclose the dependency in prose instead — ORCL's was *"The economic returns on these investments are dependent on customer demand and the ability of our key customers to meet their contractual obligations."* Also note the issuer may **name no customer at all**; a counterparty attribution circulating in press (S&P's ~50% estimate here) is a third-party **estimate**, not a filed number, and must not be propagated as disclosed.

Related: [[finding_visibility_is_layered_not_binary]] (the exposure is reported, just not through the gate you're reading), [[finding_proxy_segment_masks_trigger_series]], [[finding_composition_mask_unmask_discriminator]], [[finding_relabeled_number_viral_stat]].
