---
name: cross-flag-routing
description: "When a finding in one domain has cross-domain implications, route by recipient state — SIG file to inactive agents (they integrate on next boot), SendMessage to active teammates (immediate integration)"
metadata: 
  node_type: memory
  type: project
  originSessionId: 93c60a77-e8e4-4422-945e-267bc5b8b93d
---

When a domain-agent finding has implications for other domains, route the cross-flag based on **each recipient's current state**:

- **Active in teams mode (live this session):** SendMessage. Recipient integrates immediately; can push back; closes the loop in the same session.
- **Not active (last boot >0 sessions ago):** SIG file to their inbox with `_prome-spawned` suffix + PROVENANCE preamble (Convention B). Recipient integrates on next boot. No interruption to their workflow.

**Why:** *5/21 BOND-TIPS finding had cross-domain implications: duration-vector re-weight question for BROCK, breakeven-as-third-Fed-can't-cut confirmation for HENRY. BROCK was not in teams mode → SIG to BROCK inbox (integrated on next boot per his closeout). HENRY was active in teams mode → SendMessage → HENRY integrated as commit `526d3586` in same session. Both routes worked cleanly. Trying to SendMessage an inactive agent fails; trying to SIG-file an active teammate creates inbox lag.*

**How to apply:**

1. **Check recipient state** — `subagents(action="list")` or check which agents are addressable via SendMessage in current session.
2. **Active teammates:** SendMessage with the finding + framing question + invitation to push back.
3. **Inactive agents:** SIG file to `AGENTS/<NAME>/inbox/SIG-PROME-<NAME>-<DATE>_<topic>.md` with PROVENANCE preamble explaining the source finding + cross-domain implication.
4. **Use Convention B `_prome-spawned` suffix** for the SIG files; leave untracked; recipient commits on their next boot.
5. **Cross-flag inbox writes are per-instance Will-authorized** (default-forbidden per [[feedback_cross_agent_inbox_writes]]) — surface to Will before filing if scope isn't already covered.

**Validated:** BOND-TIPS → BROCK (SIG file) + HENRY (SendMessage), 5/21 ~14:15-14:20. Both routes integrated cleanly in respective windows.

**Related:**
- [[feedback_cross_agent_inbox_writes]] — default-forbidden gate; cross-flags need per-instance auth
- [[feedback_scan_agent_outboxes_at_boot]] — receiver-side: outbox-to-PROME signals need active scanning
- [[feedback_consolidate_domain_pressure]] — different pattern: when N agents need to weigh in on Will-decision, consolidate; cross-flag is when 1 agent's finding informs N other agents
