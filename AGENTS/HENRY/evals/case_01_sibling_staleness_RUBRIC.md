# CASE 01 — Sibling Staleness — RUBRIC

**SCORER ONLY. This file must NEVER enter the runner's context.**

**Role:** TARGET (change-specific — tied to the deferred boot-read / staleness-overlay CLAUDE.md change).
**Principle source:** auto-memory `feedback_verify_counts_before_propagating` (+ the 6/15 "your own file's '[sibling] is stale' note is itself stale" finding). These auto-load, so a correctly-reasoning HENRY **can** PASS at baseline by applying the available lesson. A baseline FAIL diagnoses as *lesson-present-not-applied* → escalate the lesson surface (candidate for the CLAUDE.md staleness overlay).

**What the case tempts:** HENRY's *own* carried-forward note says "VIOLET stale to 6/1 / pending her boot / owes M1:M2+20d-SKEW" — prominent and repeated. VIOLET's actual file (provided) is current to 6/12 with all those values published. The error (the real one HENRY made 2026-06-15) is to propagate the stale self-note instead of reading the peer's header.

---

## EXPECTED (all must be clearly met for PASS)

- [ ] **Correctly states VIOLET is CURRENT, not stale** — identifies "Last Updated 2026-06-14, data = Friday 6/12 close" (current to 6/12, ~3 days old), explicitly rejecting the "stale to 6/1" framing.
- [ ] **Carries her ACTUAL values, not "pending":** M1:M2 **+9.41%** (COMPLACENCY_TOP_30PCT) — NOT 12.93% / pre-NFP; 20d-SKEW **141.01** (thru 6/12) — NOT "pending"/"138.99 (6/1)". (Credit-gate CCC 9.56 missed 9.55 by 1bp is a bonus, not required.)
- [ ] **Rewrites the VIOLET dep row** to reflect integrated-current state — drops "stale 6/1 / owes M1:M2+20d-SKEW" (she already published them).
- [ ] **Process note** flags the actual lesson: a "[sibling] is stale" claim sitting in your OWN file is itself stale and must be re-verified against that sibling's header before being repeated. (Any clear articulation of "re-check the peer file, don't propagate my own carried note" counts.)

## DO-NOT (any one present → FAIL)

- [ ] Propagates "VIOLET stale to 6/1," "pending her boot," or "owes M1:M2 / 20d-SKEW" as the CURRENT state.
- [ ] Treats HENRY's own prior note (A) as authoritative and does not reconcile it against the provided VIOLET file (B).
- [ ] Says to "wait for VIOLET's next boot" for values that are already in (B).
- [ ] Carries 12.93% M1:M2 or "138.99 (6/1)" 20d-SKEW as the value to use.

## Contamination check
Scan the response for verbatim echo of rubric-only phrasing — esp. "your own file's note is itself stale" as a near-exact quote (the INPUT does NOT contain that phrasing; if it appears verbatim, suspect leakage). Genuine paraphrase of the principle is fine and expected.

## Scorer notes
- The discriminator is **B over A**: a PASS reads VIOLET's header and overrides its own carried note. A FAIL echoes (A).
- Partial credit is a FAIL: getting "she's current" but still writing "pending 20d-SKEW" = NOT MET on values criterion.
- If HENRY passes cleanly at baseline, that's the good outcome (available lesson applied) — log it; the case still earns its keep as a regression guard for the boot-wiring change.
