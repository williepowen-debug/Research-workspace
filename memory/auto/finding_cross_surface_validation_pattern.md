---
name: cross-surface-validation-pattern
description: OpenClaw Prome and CC-Prome independently catching the same correction from different evidence paths — concrete validation of the dual-surface redundancy thesis
metadata: 
  node_type: memory
  type: finding
  originSessionId: 34d1328c-d6e8-433a-9a51-08ce3b96c4b3
---

When OpenClaw Prome and Claude Code Prome operate on the same problem with different tool affordances, they can independently surface the same correction from different evidence paths. This is the redundancy the dual-Prome architecture was hypothesized to produce — the 5/21 TIPS catch was the first concrete instance.

**Concrete instance (2026-05-21):** The 1pm Treasury auction was widely understood to be a "10-Year reopening" because Treasury's `term` field labels it that way — but it was actually a 9Y8M TIPS reopening, not the nominal 10Y that the BOND matrix Q4 conditional rule depended on.

- **OpenClaw caught it** via FiscalData API's `inflation_index_security = Yes` flag on CUSIP 91282CPU9
- **CC-Prome caught it** via direct Treasury PDF inspection (`R_20260521_4.pdf`) + CUSIP-family heuristic (91282CP* = TIPS, 91282CQ* = nominal)
- Both surfaces flagged "this CUSIP is TIPS not nominal" within ~30 minutes of each other, before any cross-talk between them
- OpenClaw's catch arrived as a COMM message in `TO_CLAUDE_CODE/` while CC's correction was already on master (commits `724169c3` + `526d3586`)

**Why this matters:** Different tool affordances catch different errors. OpenClaw's FiscalData access surfaces structured-field flags that CC doesn't see; CC's direct-file access surfaces PDF/CUSIP details that OpenClaw can't easily fetch. Convergent catches across these different evidence paths produce real redundancy. The dual-Prome architecture was hypothesized to produce this; before 5/21 we had no concrete example.

**How to apply:**

1. **Don't dismiss the second surface's catch as "we already caught it."** That misses the point — the redundancy *is* the value. File the ACK as `completed` with a note acknowledging the cross-surface convergence (see `PROME/COMM/ACKS/20260521T193904Z_ack_bond-cusip-caveat.md` for the template).
2. **The COMM mailbox is the canonical channel** for capturing cross-validation moments, even when the substantive issue is already resolved by the time the second message arrives. Preserve the message + ACK as part of the audit trail.
3. **Expect the pattern to extend.** Wherever the two surfaces have non-overlapping tool affordances (FiscalData vs PDF inspection, Telegram vs file-system, web search vs domain-agent STATUS), look for similar cross-validation opportunities.
4. **Use cross-surface convergence as evidence weight.** If both surfaces independently catch X, X is more confidently right than either surface's solo conclusion. If they disagree, that's a flag worth investigating before acting.

Related: [[scan-agent-outboxes-at-boot]] (workflow gap: OpenClaw's signal arrived via COMM mailbox; agent-to-PROME signals arriving via agent outboxes still depend on PROME proactively scanning). [[finding-revival-proxy-pattern]] (another cross-surface coordination pattern).
