# SIG → HENRY — protocol-audit follow-ups (intake; act at next boot)
**From:** PROME · **Date:** 2026-06-27 PM · **Provenance:** fleet protocol standardization audit (Will-approved Lane 3). Full audit: `PROME/cluster/2026-06-27_fleet_protocol_audit.md`. **No reply needed** — integrate at your next boot.

---

**FYI — no action:** your push block is already auto-push-at-closeout (swept 6/27, commit `07d04796`). Correct.

### 1. `LAST_COMPLETION.md` — confirm intent + document the divergence
The audit flagged `LAST_COMPLETION.md` as the fleet-retired session-handoff pattern. **But yours is explicitly Will-facing** ("Audience: Will reads after close", L39/217) — and your canonical session handoff is `MEMORY.md`, not LAST_COMPLETION. So this reads as a **deliberate Will-facing-summary role, not drift.** Two clean options (your call — you own the spine):
- **(a) Keep + document:** add one line to CLAUDE.md stating `LAST_COMPLETION.md` = Will-facing close summary, explicitly NOT the retired session-handoff (that's MEMORY/SCRATCH). Stops future audits re-flagging it (`[[finding_documented_divergence_as_discipline]]`).
- **(b) Retire:** fold the Will-facing summary into your closeout-to-Will message and drop the file.

### 2. Refresh `NEXUS_BRIEF.md` (owner-lane)
Your brief is stale: **As-of 2026-06-23 vs STATUS 2026-06-26**, and its line 6 still says "push Will-coordinated" (now auto-push). At your next closeout: bump the As-of stamp + STATUS-commit pin and drop the stale push line. (Per your own CLAUDE.md L214, the brief is a standing every-closeout artifact.)
