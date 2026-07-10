---
name: finding_refuted_claim_citation_vs_fact_failure
description: "When adversarial-verify KILLS a load-bearing claim, triage citation-failure (source doesn't say it → re-source) vs fact-failure (claim is wrong → drop) before abandoning it"
metadata: 
  node_type: memory
  type: finding
  originSessionId: cb850d17-5aa7-48f3-a41d-56fcd6c45a8a
---

A `/deep-research` (or any adversarial-verify) pass reports killed claims as votes (e.g. "5 of 25 refuted"). A refute vote means **the assigned source does not support the claim as written** — it does NOT always mean the claim is FALSE. On a load-bearing item, triage the kill into two cases before acting:

- **Citation failure** — the *fact* is true (structural/textbook/otherwise well-established) but the workflow's chosen source didn't actually contain it, or attributed it to the wrong document. Fix by **re-sourcing** to a correct primary/authoritative reference; the finding survives.
- **Fact failure** — the claim itself is wrong. Drop it.

**Why it matters:** treating "refuted" as "false" silently drops TRUE load-bearing facts — the mirror-image of [[finding_triage_summary_compression_inversion]] (where a compressed one-liner *inverted* a finding). Both are ways an automated verify/triage layer corrupts a load-bearing conclusion if you consume its verdict uncritically.

**How to apply:** for any KILLED claim that is load-bearing (the sign/verdict hinges on it), spend one targeted primary re-source pass (`scripts/` or a focused WebFetch) before abandoning it — this is the [[finding_deep_research_primary_pull_owns_three_data_classes]] discipline applied to the verify output, not just the search output. Live instance (DEWEY prompt-08, 2026-07-10): the fan-out refuted the "Japanese lifers run a negative duration gap" claim (1-2) because the cited Milliman PDF didn't state it — but the negative gap is structural bedrock of Japanese lifer ALM (IMF/BOJ/BIS/TwentyFour corroborate). A one-line DEWEY WebSearch re-sourced it cleanly; had I read "refuted" as "false," the entire ALM-buyer sign adjudication (the report's core deliverable) would have collapsed on a citation artifact. Relates to [[finding_deep_research_stale_vintage_headline]] and [[finding_fail_loud_on_incomplete_data]].
