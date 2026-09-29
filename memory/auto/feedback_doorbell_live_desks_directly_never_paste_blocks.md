---
name: feedback_doorbell_live_desks_directly_never_paste_blocks
description: Will (2026-09-29) — when a desk is LIVE in one of his windows, PROME sends the instruction itself by SendMessage; a "paste-ready" block handed to Will for an owed-item instruction is the failure, not a courtesy.
metadata:
  type: feedback
symptoms: "paste-ready block for a live desk", "Any follow up instruction I should give to X?", "can't you simply doorbell these agents", "told Will what to tell a desk that ListAgents showed live", "instruction relayed through the operator that PROME could have sent"
---

**Will, 2026-09-29 10:01 ET, verbatim:** *"Question - Cant you simply doorbell these agents I have open in other windows? I have spwned: HOMER LIQUID VULCAN OSPREY SAM"*

**Context:** Will launched seven desks in his own windows on the morning of 9/29 and asked PROME three times *"Any follow up instruction I should give to X?"* PROME answered LIQUID's with a recommendation AND a paste-ready block, then did the same for HOMER, VULCAN and SAM — while `ListAgents` showed every one of them live and PROME had already been doorbelling LIQUID, OSPREY and HOMER directly for receipts. The paste blocks were redundant relays through the operator.

**Rule (how to apply):**
- Before answering "what should I tell desk X", run `ListAgents`. If X is live, **send the instruction yourself** (`SendMessage`), then tell Will in one line what you sent and why. Will's question is a prompt to act, not a request for a script.
- What PROME may send unasked: any owed item on a registered row (DOCKET/GATES/WQ), a receipt, a correction, a consumer-read result — all Tier 1 (follow-up inside an approved workstream, `PROME/CLAUDE.md` § Spawn default).
- What still goes to Will first: a **new-direction** task for the desk (Tier 2 cost gate), anything that spends, any trade consequent, and any Will-gated surface edit. Say which class the item is when you surface it.
- A desk in Will's window is still Will's to close out (WQ-249 scope) — the doorbell carries the task, never the closeout ask.
- The paste block survives only for a desk that is DARK and that Will intends to launch himself: then the launch brief is the right form.

**Why:** the operator's attention is the scarce resource; a relay through him costs a read, a copy and a paste for zero information gain, and it hides from him that PROME already has the channel. Related: [[finding_prome_inbox_is_repo_root_not_under_agents]] (delivery working ≠ address correct — here, channel available ≠ channel used), [[feedback_explicit_approval_authorizes_no_relay_gate]] (the other relay failure: adding a gate because a word travelled by relay).
