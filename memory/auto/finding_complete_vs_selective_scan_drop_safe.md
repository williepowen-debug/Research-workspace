---
name: finding_complete_vs_selective_scan_drop_safe
description: Before dropping a redundant delivery channel for an agent, test whether its OTHER intake path is COMPLETE vs SELECTIVE — complete=drop-safe, selective=keep.
metadata:
  type: finding
---

When a consumer has two overlapping intake paths (e.g. WALTER's per-recipient `inbox/WALTER/` delivery lane AND a `/BOARD/INDEX.md` diff-scan) and you're deciding whether the redundant one can be **dropped**, the discriminator is whether the *other* path is **COMPLETE** (dispositions every item) or **SELECTIVE/tiered** (scoped, can skip items):

- **Complete → drop-safe.** CARL runs a whole-INDEX BOARD-diff (dispositions every unrecorded SIG-W). Its inbox/WALTER copies are pure redundancy → drop the lane, archive the backlog. Verified: all 40 inbox items were reachable via /BOARD/INDEX.md, so CARL's scan catches them regardless.
- **Selective → keep the lane.** REGINALD runs a *tiered* BOARD scan (three-tier scope). It genuinely **missed** a single-name ACTION (SIG-704-004, the OZK deed-in-lieu) that fell outside its tiers → the lane is the only guaranteed-delivery path for those. Keep it; install a drain-step.

**Why:** "redundant channel" is a claim about *coverage*, not just overlap. A selective scan overlaps the delivery lane on most items but not all — the tail it misses is exactly what the guaranteed-delivery lane exists for. Dropping it silently loses that tail.

**How to apply:** Don't take an owner's (or your own) "the other path covers it, drop the lane" on faith. **Verify the backlog's item-set is a subset of what the other path actually catches** (e.g. grep each inbox SIG-W against the agent's BOARD_LOG *and* against /BOARD/INDEX.md — the intake path, not just the log, since an un-booted agent's log lags). If any item isn't reachable via the surviving path, don't drop/archive it. This is the concrete test for the [[project_messaging_overhaul]] channel-cutting decisions. Pairs with [[feedback_verify_counts_before_propagating]] and [[finding_asymmetric_records_need_reconciliation]] (the same session's WALTER packet undercounted the CARL backlog by 6 items that postdated its last scan).
