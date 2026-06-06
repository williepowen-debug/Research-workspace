---
name: finding-boot-protocol-live-event-override
description: "SPAWN PROTOCOL framing pulls agents toward CLOSEOUT after boot even mid-event; the fix is neutral \"Write-back\" framing + explicit live-event override in EXECUTE step. Validated on VIOLET 2026-06-05 mid-VIX-spike."
metadata: 
  node_type: memory
  type: finding
  originSessionId: 0c455318-cecf-4b91-8272-7408397a9677
---

When an agent's SPAWN PROTOCOL emphasizes "boot and closeout are one symmetric sequence... CLOSEOUT phase... run at EVERY session end, not just end-of-day. It is not optional; it is the back half of this protocol" — combined with section header `### CLOSEOUT (write-back — run at EVERY session end)` — the agent snap-closes on quiet boots. The failure mode: when EXECUTE is open-ended (live event, active monitoring), the agent treats boot itself as the session and immediately proposes the closeout ceremony instead of staying engaged.

**Diagnostic:** Caught on VIOLET 2026-06-05 mid-VIX-+40pct-spike. Will-asked boot during NFP-shock session; agent presented live read and immediately proposed full closeout package. Will: "Why would we want to close out so quick?"

**Comparison across fleet (as of 2026-06-05):**
- VIOLET / BRENT: aggressive "symmetric sequence / not optional / EVERY session end" preamble + `CLOSEOUT` section header
- SAM: no preamble; `Boot (read phase)` → `Execute` → `Write-back` (neutral); intra-day discipline lives in auto-memory only

**Fix (applied to VIOLET 2026-06-05; declined for BRENT):**
1. Drop the symmetric-sequence preamble. Replace with a single neutral line about read↔write pairings + auto-memory pointer for intra-day discipline.
2. Rename `CLOSEOUT` → `Write-back` (section header + discipline-overlay anchor).
3. Add live-event override to EXECUTE step: "If boot reveals a live regime-moving print or active catalyst window, EXECUTE stays open — snapshot STATUS as a working dashboard and stay engaged. Don't trigger the full Write-back sequence until the event stabilizes, the task completes, or Will signals stop. **The session is not over because boot is over.**"

**Why:** Wording matters more than content. The intra-day-closeout discipline ([[feedback_intra_day_closeout_discipline]]) is correct in principle — agents SHOULD write-back at session end. The bug is in what "session end" means. A boot-only ping during a live event is not session-end. The aggressive framing collapsed EXECUTE to "present the read" and snapped to closeout. Neutral "Write-back" framing treats the write-back as natural tail of execution rather than ceremonial gate.

**How to apply:** When updating any agent's SPAWN PROTOCOL, prefer SAM's neutral "Write-back" framing over VIOLET/BRENT's "CLOSEOUT" framing. If symmetry preamble exists, audit whether it's pulling toward premature closeout on live events. Live-event override clause is generally applicable — most agents in stress-research fleet have monitoring duties where boot can land in mid-event.

**Validation:** Same VIOLET session 2026-06-05 — after fix applied, agent stayed engaged through NFP-shock analysis (3 hour session, 3 verification passes, NFP analog backtest, decision tree pre-commit) before write-back. Validates the fix in the same session it was applied.

**Cross-references:** [[feedback_intra_day_closeout_discipline]] (the rule whose framing was over-emphasized); [[finding_closeout_as_writeback_tail]] (BRENT 2026-05-31 codification that introduced the preamble); [[feedback_handoff_cadence]] (related — when to close vs when to keep going).
