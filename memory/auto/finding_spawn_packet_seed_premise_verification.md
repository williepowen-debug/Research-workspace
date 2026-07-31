---
name: finding_spawn_packet_seed_premise_verification
description: Coordinator-authored spawn-packet context claims (current time, an agent's ledger state, tool/file ownership) are load-bearing citations, not framing — verify each against ground truth before sending; recipient catches are the backstop, not the design.
metadata:
  type: feedback
---

Three same-day instances (2026-07-23, PROME) of unverified seed claims shipped in spawn packets: (1) the operator's "11:58 PM" boot time was actually 11:58 AM — propagated verbatim into THREE spawn prompts ("all four prints landed", "it's Friday in Kazakhstan") before CORAL machine-clock-verified and refused to grade unprinted names; (2) MIDAS's packet asserted "your ledgers were rebuilt 7/22 (VX 5×9...)" — that was VULCAN's commit `83df8be9`, conflated across agents; (3) OSPREY's packet seeded "your scripts state-JSONs" — FALCON's infrastructure, OSPREY has no scripts dir.

**Why:** a spawn packet reads as authoritative context to a cold agent — an unverified premise doesn't get challenged by default, it gets *executed* (graded, stamped, propagated). All three catches happened only because the fleet's verify-before-inherit discipline is strong; the coordinator was the weakest link that day. Same root as [[feedback_reconciliation_is_last_line_move_catch_upstream]]: install the guardrail at ORIGIN.

**How to apply:** before sending any spawn packet or warm-agent tasking, verify each factual seed the same way you'd verify a figure for canon: current time → machine clock (`date`), never the operator's message or your own assumption (extends [[finding_subagent_prefire_date_verification]] — a *stated* time can be wrong, not just a missing one); an agent's ledger/file state → `git log -- AGENTS/<NAME>/` + `ls`, never memory of "recent work" (cross-agent commit conflation is easy when several agents rebuilt similar surfaces the same day); tool/infra ownership → check the target dir exists. Seeds you cannot verify get labeled "UNVERIFIED — check before relying" in the packet, or dropped. Related: [[feedback_subagent_prompt_discipline]].

**n+1 (2026-07-31, PROME):** two stale seeds in ONE day from the SAME source — a 7/28 review record. Seeded BRENT "BRT-26 due today" (its ledger: end-Q3 window; BRENT refused to grade to the wrong date) and "your boot lacks a general-inbox step" (fixed 7/28, the seed described the pre-fix state). Fix that held: seeds drawn from review/record prose must be EXISTENCE-CHECKED at the current artifact before packeting — a review is a snapshot, and its findings have owners who fix them.
