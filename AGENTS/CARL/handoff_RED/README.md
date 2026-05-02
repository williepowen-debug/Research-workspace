# CARL → RED Handoff Staging

**Created:** 2026-05-01
**Reason:** Architectural realignment under THESIS v2.5. CARL is the bear-thesis specialist; RED is the counter-signal agent. Counter-evidence and alternative-hypothesis material that CARL was previously maintaining internally belongs in RED's domain.

This folder is transitional staging. RED can review, integrate, and relocate to `AGENTS/RED/` when activated.

---

## Contents

| File | Origin | What it is | Recommended RED action |
|------|--------|-----------|------------------------|
| `COUNTER_LOG.md` | `AGENTS/CARL/red_team/` (moved May 1) | Running log of thesis-weakening data points with dates. Most recent: MS/Piper Sandler "2026 ≠ 1990/91" structural counter (Apr 19), ALLY Q1 clean (Apr 17), and ~10 prior entries through Mar 2026. | Adopt as RED's counter-evidence ledger or merge into RED's existing structure. |
| `SOFT_LANDING.md` | `AGENTS/CARL/red_team/` | Competing hypothesis #1 — "consumer stress is transitory, soft landing achieved." Last updated Apr 7, current confidence <5%. Includes validation criteria, supporting evidence, contradicting evidence. | Promote to canonical alternative-hypothesis tracking in RED. |
| `CONTAINMENT.md` | `AGENTS/CARL/red_team/` | Competing hypothesis #2 — "subprime cracks but prime holds." Last updated Apr 7, current confidence 15-20%. Most likely "wrong about magnitude" hypothesis. Includes monitoring metrics + key tests. | Promote to canonical alternative-hypothesis tracking in RED. **Note for RED:** v2.5 introduces explicit falsification windows (CRL-21 Q3 2026 intermediate, CRL-20 Q1 2027 outer) that test masking-thesis vs CONTAINMENT. RED should be the adversarial pressure on the masking framework. |
| `README_old.md` | `AGENTS/CARL/red_team/` (former README.md) | Original red_team folder description. Kept for context; can be deleted after RED has reviewed the rest. | Reference only. |

---

## What's coming (pending v2.5 r3 work)

THESIS v2.5 r3 will strip the standalone "Counter-Evidence (Active)" section from `AGENTS/CARL/thesis/THESIS.md` and stage that content here as well. Specifically:

- Counter-narrative observations (ALLY headline clean, NFP +178K, retail sales bounce, savings rate 4.0%, etc.) that are tracked alongside cohort-decompose rebuttals — RED domain.
- The MS/Piper Sandler structural counter-frame rebuttal — already in `COUNTER_LOG.md`, will not be duplicated.
- Disposition rules (when aggregate-only counter-data should be downgraded under v2.5 masking framework).

Will be added as `COUNTER_EVIDENCE_FROM_THESIS.md` when r3 ships.

---

## Architectural notes for RED

**Interface contract pending:** v2.5 review surfaced the need for an explicit RED-CARL handshake protocol. CARL is willing to:
- Escalate puzzles unresolved across 2+ thesis versions to RED for counter-investigation
- Send fast-warning trigger fires (e.g., HY OAS >350bps) to RED for verify counter-direction signal
- Receive RED counter-vector scores into CARL's PENDING_VERIFY queue
- Accept RED adversarial pressure on the data-masking framework as load-bearing

**Specifically on the data-masking framework:** RED should be running the adversarial test "build the strongest case that masking is post-hoc rationalization for clean prints." If RED can't generate that case credibly, the framework hardens. If RED generates it and CARL can't rebut at the mechanism level, framework softens. CRL-21 is the empirical falsification; RED is the epistemic falsification. Both should be running.

**Puzzle handoff candidates:** The Puzzles section in v2.5 currently includes 5 items, of which 3 are RED-natural-territory (prime mortgage stable, auto insurance cooling, savings rate 4%). v2.5 r3 will trim CARL's puzzles to thesis-internal mechanism puzzles only and route counter-narrative puzzles to RED.

---

*Will: this folder is yours to move/transfer to RED whenever you're ready. CARL has stopped maintaining these files as of May 1 2026 unless you explicitly direct otherwise.*
