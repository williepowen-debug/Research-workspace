---
name: finding_workbook_demote_by_verification
description: "demoting a dormant agent ledger — verify live-consumer + cross-agent counterparty BEFORE freezing; triage by Group not ID-range; UNVERIFIED-RETIRED for LLM rows; re-verify your correction's own provenance"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: a9f41099-de31-4a68-abf6-1de933d714cb
---

Recipe for demoting a dormant agent workbook/ledger to archival — validated BRENT KB/VX/FLOW 2026-06-14 (Orc 2-round adversarial cross-check).

**Why:** dormant ledgers drift into three failure modes — stale snapshots read as live, LLM-sourced rows mistaken for fact, and cross-agent contracts whose counterparty already walked away. A blind "demote" can orphan a live interface or bake an error into an archive.

**How to apply:**
1. **Verify live consumer before freezing.** Grep the ledger's IDs across live docs (STATUS/THESIS/handoffs). Zero live consumers → clean freeze (VX). A live consumer exists → it's load-bearing; triage, don't blanket-freeze (FLOW had a live handoff touchpoint; KB had none but a durable structural layer).
2. **Cross-agent contract? Verify the COUNTERPARTY's own files say it's dead before freezing your side** — else you cut signals they're still sending. FLOW-BRT-30 (auto-dispatch contract) confirmed dead via WALTER's own STATUS ("dormant-structural, no BOARD-intake, 0 dispatches"), not by our say-so. This is the difference between safe-to-freeze and breaks-an-interface.
3. **Triage by the Group/type column, never by ID-range** — ranges overlap and clobber keepers that sit inside a "didn't-pan-out" range (e.g. SX-EW cost-curve KB-099 sat inside the failed-cobalt-thesis block).
4. **Separate durable FACT from failed PREDICTION** — the fact survives even when the bet on it failed (SX-EW economics true though BRT-23 failed).
5. **UNVERIFIED-RETIRED bucket for D-3 / "X-post (LLM-generated)" rows** — flipping them to HISTORICAL implies true-then; they were never established. Keep their VERIFY: notes so confirmable specs can graduate later.
6. **Archival header declares the default disposition** (event/price snapshots = historical; structural rows = live value, listed by ID). Does the bulk historicalization without 100 fragile per-cell edits — and a TSV with malformed (extra-tab) rows makes a scripted positional rewrite unsafe anyway.
7. **When CORRECTING a stale entry, re-verify YOUR replacement's own provenance.** A fix can introduce a fresh conflated citation — caught citing a D-3 LLM row (KB-090) as EIA-A-1 *while fixing a provenance error* in KB-011. Verify the fact, judge the source separately.

Generalizes [[number_carries_threshold_unit_source]] (a number carries its ERA too — "~350M" was a true 2023 trough mis-dated onto a 2026 entry). Siblings: [[finding_threshold_vs_mechanism]], [[verify_counts_before_propagating]], [[feedback_check_domain_owner_before_messaging]]. Transferable to any agent with dormant workbooks (CARL/REGINALD/HENRY/SAM).
