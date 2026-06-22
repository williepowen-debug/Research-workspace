---
name: finding_private_by_construction_unverifiable
description: "a load-bearing thesis number can be private-by-construction (144A/Reg S, non-SEC-filer) → structurally unavailable from primary sources, not merely \"not yet found\"; distinguish the two, re-mark as third-party/unverified, and log the recovery path"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 3cab834d-c0af-455c-8020-7f57e89e9ba8
---

Some load-bearing figures are **structurally unavailable** from public/primary disclosure — not because you searched badly, but because the instrument is private by construction. SHADE 6/22: the "$16.5B 2026-2027 Athene FABN maturity wall" anchoring kill-path-1 could not be reconciled to any 10-K/10-Q/deck because **Athene Global Funding is not an SEC filer and 100% of the $34.5B FABN is Rule 144A / Reg S** — per-tranche principal lives only in private Pricing Supplements to QIBs. The figure had been carried as fact for months.

**Why:** "couldn't find it" gets treated as a temporary gap and the unverified number keeps getting cited as if sourced. Naming it *structurally unavailable* changes the disposition: re-mark third-party/unverified, stop banking it, and decide whether the recovery cost (terminal/paid) is worth paying — rather than re-searching free sources forever. Cousin of [[feedback_dont_bank_unpassed_forecast]], [[finding_number_carries_threshold_unit_source]], and [[feedback_suspect_fresh_pull_over_curated_record]].

**How to apply:** when a thesis-critical number won't reconcile to a primary filing, first ask *can it exist publicly at all?* (144A/Reg S, private funds, non-filer SPV trusts, captive/offshore reserves, undisclosed-by-design). If no → re-mark it third-party/UNVERIFIED in every doc that carries it (incl. the agent's own spec/kill-path), separate the **mechanism** (often still sourceable from primary — e.g. issuance cadence, substitution, tenders) from the **quantum** (hidden), and record the explicit recovery path (e.g. NPORT-P holder-level CUSIP aggregation is a free bottom-up route for 144A notes; Bloomberg DDIS/cbonds-Pro is the paid route). Don't let a private-by-construction number masquerade as a verified one.

**Validated (SHADE 6/22):** the holder-side route WORKS. A scripted EDGAR crawl of 1,602 NPORT-P fund filings recovered a $3.29B registered-fund floor on the AGF 2026-2027 wall; since registered funds held 18.1% of total AGF, grossing up bracketed the wall at ~$13-18B — corroborating the previously-unsourceable $16.5B. So "structurally unavailable from the *issuer*" ≠ "unknowable": the holders disclose what the issuer won't. Gotchas: EDGAR full-text search needs a User-Agent header (WebFetch can't set it; Bash/curl/python can); use latest-public-filing-PER-FUND (a single snapshot date undercounts because funds have staggered fiscal-quarter-ends); the aggregate is a FLOOR (excludes insurance GAs, foreign Reg-S, pensions, SMAs), so gross up by the visible ownership share.
