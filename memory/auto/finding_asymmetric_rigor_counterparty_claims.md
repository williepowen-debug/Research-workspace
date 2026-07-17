---
name: finding_asymmetric_rigor_counterparty_claims
description: an agent greps rigorously for its OWN claims then asserts about the counterparty on zero evidence — deference AND suspicion are both unverified; a claim about another agent's state/process needs the same receipts as a claim about a filing
metadata:
  type: finding
---

**An agent can be rigorous exactly where it MEASURES and sloppy exactly where it INFERS — and the inference is reliably about the OTHER side.** The asymmetry is invisible from inside, because the sloppy claim rides in the same message as real, demonstrated rigor.

**Worked case (2026-07-16, VULCAN ↔ WALTER, 3 instances in one session).** VULCAN grepped hard for everything in its own domain — and got all three cross-agent claims wrong:

1. **Published `199`** for a shared metric. It reproduced under **no** method — *not even its own*, which yields 198. An arithmetic artifact over a `head`-truncated `uniq -c` list: **not a near-miss, but a figure that never measured any quantity.**
2. **Resolved a metric divergence by DEFERENCE** — *"you counted signals, I counted grep hits, yours is better."* The counterparty had counted **the same thing, mislabeled**. The concession rested on a **guess about the counterparty's method**.
3. **Asserted the counterparty's check "ran against a stale read."** Timestamps refuted it: the commit landed **2 minutes AFTER** the check, and the counterparty had **already `git log`ged the dir first.**

## Two forms, one failure

- **Deference is not verification** — accepting the counterparty's figure because conceding *feels* like humility.
- **Suspicion is not verification** — asserting the counterparty erred is **exactly as unevidenced** as deferring to them.

**Both resolve a cross-agent claim by a SOCIAL move instead of a measurement.** Conceding a point does not license sloppiness about *why* you're conceding.

## How to apply

- **A claim about another agent's state, process, or method is a claim requiring evidence — same standard as a claim about a filing.** `git log` their dir. Read the timestamp. Open their file. **Do not infer their method from their number.**
- **Reconciling a shared metric: state the UNIT, don't defer.** The 190-vs-192-vs-199 divergence dissolved the moment units were attached — *190 signals carrying 192 tag instances* (2 multi-tagged); 250 raw incl. `n/a`. **Two numbers with a polite deference between them is not a reconciliation.** → `[[finding_number_carries_threshold_unit_source]]`, `[[finding_asymmetric_records_need_reconciliation]]`
- **Watch for the self-congratulation tell:** the failure lands in the same message where the agent is (correctly) reporting that it checked. Rigor in one paragraph does not transfer to the next.

## Corollary — a chase and a delivery can CROSS IN FLIGHT

That is a **benign race**, not a stale read, and **not an error by either party.** Do **not** encode a *"check before chasing"* lesson from it when the chaser **already checked** — that was true here and the proposed lesson was withdrawn. The mirror of `[[finding_workflow_scratch_crash_recovery]]`'s *"idle ≠ reported, so chase"*: **"chased ≠ actually missing"** is only sometimes true, and asserting it about the counterparty is instance #3 of this very finding.

**Distinct from `[[finding_confabulated_counterparty_position]]`** (which is about attributing a *fabricated* stance/source to a counterparty). This one is narrower and more common: the counterparty's position is **real**; the *characterization of their method or state* is the invention.

**Why it matters:** cross-agent verification is the fleet's main defense against a single agent's error becoming canon. It only works if the skepticism points **both** ways. An auditor who greps its own claims and infers about its auditee has kept the *form* of verification and lost the *function* — and the resulting verdict is worth what the weakest inference in it is worth.
