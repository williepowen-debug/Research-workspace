---
name: finding_spawned_agents_ship_artifact_skip_writeback
description: "Spawned agents reliably deliver the requested artifact and reliably SKIP writing back to their own STATUS — 3-for-3 in one session, including one agent that flagged its own stale surface inside the memo and then didn't fix it. A deliver-before-idle contract buys the deliverable, not the state update; put the write-back in the spawn contract and disk-verify STATUS mtime, not just the outbox."
metadata:
  node_type: memory
  type: finding
---

**2026-07-27.** Four agents spawned (BRENT, VIOLET, TERRY, HENRY). The first three each produced an excellent outbox memo, committed it, and went idle. **None had touched its own `STATUS.md`.**

- **BRENT** — STATUS 3 days stale, still carrying a filled position as `PENDING`. It had **flagged that exact staleness inside its own memo** — *"Both my STATUS and TRADE.md still carry it as PENDING — that is a stale surface on my side and I am fixing it at closeout"* — and then not done it.
- **TERRY** — a **live position** ($287.70, mandatory dated exit) that existed on no TERRY surface.
- **VIOLET** — STATUS predating its own re-grade, so its thesis file disagreed with its own delivered conclusion.

**n=3, one session, independently.** All three closed clean within minutes of being asked, so this is not capability — it is that **the spawn contract said "deliver, then idle" and they did precisely that.** The deliverable is what the coordinator asked for; the write-back is what the *fleet* needs, and nobody asked.

**Why it is worse than ordinary staleness.** A stale STATUS after a quiet week is a known cost. A STATUS that is stale *specifically because the agent just did the work that would update it* is inverted: the surface is **least** current exactly when the agent's analysis is **most** current, and the next cold boot reads the stale surface and re-derives — or worse, contradicts — a conclusion the agent already reached. TERRY's case is the sharp one: a live dated obligation with no owner-side record, relying entirely on the coordinator's ledger.

**Why "deliver before idle" doesn't cover it.** That contract exists to stop agents idling while *holding* a result — a delivery problem. This is a **persistence** problem, and the two are separate. An agent can fully satisfy deliver-before-idle and still leave its own state layer untouched.

**How to apply:**
1. **Put the write-back in the spawn prompt as a numbered deliverable**, not as an implied closeout step: *"(a) the memo, (b) your STATUS/ledger write-back, (c) commit both."* Naming it is enough — all three complied immediately once named.
2. **Disk-verify STATUS mtime and last-touching commit, not just the outbox file.** `git log -1 -- AGENTS/<X>/STATUS.md` takes seconds and is the check that actually catches this; an outbox memo proves delivery, never persistence.
3. **A self-flagged intention is not a completed action.** BRENT named the fix in the memo and skipped it. Grep delivered memos for "at closeout" / "I am fixing" and verify each one landed.
4. **Chase before release, not after.** All three were still warm; the correction cost one message each. After shutdown it becomes an on-behalf edit or a stale surface until that agent next boots.
5. Related: `[[finding_idle_notification_is_not_a_result]]` (idle ≠ delivered) — this is the next layer down: **delivered ≠ recorded.**
