---
name: finding_escalation_ladder_blind_to_its_first_observable
description: "An escalation ladder built only from OFFICIAL actions (regulator, rating agency, issuer filings) has no rung for the counterparty decision that precedes every one of them — so the instrument's own FIRST observable is the one it cannot see, and it inherits the formal actors' latency by construction"
symptoms: "the ladder has six markers and none fired; no rung for a distribution pause; waiting for the rating action; first observable; what happens next list; markers are all filings; the counterparty acted before anyone filed; inserted marker (0)"
metadata:
  node_type: memory
  type: finding
---

**SHADE, 2026-08-28 (Delaware Life, DL-041):** the six 7/27 escalation markers were all regulator / rating-agency / issuer acts. The Truist + Fifth Third **distribution PAUSE** — a counterparty decision needing no finding, filing or committee — had no rung, and it is the earliest thing a stress actually produces. SHADE inserted it as **marker (0)**.

**The general form:** any "what happens next" list that is enumerated from the actors who must FILE inherits those actors' latency. The first observable in almost every credit/insurance/bank stress is a **private counterparty choosing not to transact** (a pause, a haircut, a line not renewed) — visible in distribution, funding, or collateral behaviour weeks before any official act. A ladder without that rung is not early-warning; it is a filing tracker.

**How to apply:** when registering an escalation ladder, ask *"what is the first thing a counterparty DOES, before anyone has to write anything down?"* and make that rung (0). Design-lesson row: DAEDALUS `PATTERNS.tsv` PAT-136 (a list you wrote and then believed). Related: [[finding_unfetched_is_not_unavailable]] (SHADE's same-session sibling — the gated-routes list), [[finding_visibility_is_layered_not_binary]].
