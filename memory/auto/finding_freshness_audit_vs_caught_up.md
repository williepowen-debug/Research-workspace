---
name: finding_freshness_audit_vs_caught_up
description: mtime/STATUS-freshness ≠ caught-up; a fresh agent can still be behind on inbox backlog AND on a pending test in its own STATUS that already resolved
metadata: 
  node_type: memory
  type: finding
  originSessionId: d5c97007-686e-4b2a-923e-8c6156e59355
---

A fleet staleness audit ranked by STATUS mtime + self-`Updated` stamp is necessary but **not sufficient** — "fresh file" ≠ "caught up." Two miss-modes surfaced when prepping catch-up packets (2026-06-26):

1. **Fresh STATUS, stale inbox.** HAWK was 6 days fresh on STATUS (🟢) yet held a 9-item unprocessed inbox backlog. The freshness metric said "fine"; the work-waiting metric said "behind." Always pair mtime with **pending-inbox count**.
2. **The agent's own pending test already resolved while it sat idle.** HAWK's STATUS explicitly held its marks "pending the Mon 6/22 Brent open = the decoupling test" — but that test had already run *days before the audit* and resolved in the thesis's favor (Brent shrugged the re-closure). The agent didn't know because it hadn't booted since. The single highest-value thing in its catch-up packet wasn't a stale-number fix — it was **"the test you're waiting on has an answer now."**

Contrast: OZK was a true cold revival (63d) where mtime *did* capture the problem — and there the load-bearing catch was that its **position state was unsafe** (expiries/roll-deadline weeks past), which no freshness metric shows either.

**Why:** freshness metrics measure when a file was last *touched*, not whether the world moved past what the file is waiting on. Load-bearing staleness lives in (a) unprocessed inbound, (b) resolved-but-unobserved pending tests/triggers the agent pre-registered, and (c) position/execution state that decays on a calendar the file doesn't track.

**How to apply:** when auditing fleet staleness or prepping any catch-up/revival packet — beyond mtime, (1) count pending inbox items, (2) grep the agent's own STATUS for its "pending / waiting-on / next-trigger / decision-by" language and check whether those have since FIRED or RESOLVED (that's the highest-value line in the packet), and (3) flag any position/expiry/deadline whose date is now past as UNSAFE-until-reconciled. Weight the ranking by load-bearing-to-live-thesis, not raw days. Relates to [[finding_revival_boot_doc_sweep]], [[finding_boot_predictions_scan]], [[finding_refresh_not_retire_perentity_profiles]].
