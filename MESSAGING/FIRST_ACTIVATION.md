# Direct Messaging v1 — First Activation

**Approved by:** Will  
**Activation date:** 2026-07-14  
**Sender:** PROME  
**Recipients:** BRENT, SAM  
**WALTER:** Unchanged and outside this activation

## Purpose

Activate the coded direct-message path with two active recipients whose own handoffs identify current analytical debt. This is a live first cohort, not a return to an observation-only pilot.

## Live routes

- PROME → BRENT
- PROME → SAM

Every other route fails closed in `MESSAGING/config.yaml`.

## First messages

### BRENT

Re-score the full convergence matrix after the July 8 crack and July 10 sustain-test DENY. BRENT's `SCRATCH.md` explicitly marks the numeric re-score as owed while confirming that the Independence column is already current.

### SAM

Recompute the four-anchor carry-unwind probability buckets after the June 30 CFTC build and July 7 cover round trip, then reconcile the next-CFTC-release date conflict. SAM's current STATUS/NEXUS surfaces explicitly mark both items as unresolved.

## Success evidence

For each obligation:

1. Committed inbox file exists.
2. Recipient-owned receipt records a disposition.
3. Accepted work closes as `INTEGRATED` with target/effect or `NO_CHANGE` with rationale.
4. Message moves to `inbox/processed/` under the recipient's normal Git discipline.

## Stop conditions

- Tool attempts a non-allowlisted route.
- Receipt ownership mismatch.
- Duplicate or conflicting message identity.
- Recipient instructions conflict with WALTER processing.
- Required Python dependency is unavailable and cannot be installed safely.

On a stop condition, leave the message readable in the inbox, record `BLOCKED` where possible, and do not broaden the cohort.

