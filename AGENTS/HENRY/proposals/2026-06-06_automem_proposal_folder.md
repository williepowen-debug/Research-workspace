# Proposal — Collision-Safe Auto-Memory via Per-Agent Proposal Folder

**Status:** REVIEW-NOT-APPLY draft. Land via Will + PROME decision, not unilaterally — `memory/auto/` is shared fleet infra outside any agent's owned write-set.
**Author:** HENRY, Sat Jun 6 2026 (core idea: Will, this session).
**Pairs with:**
- `AGENTS/SAM/proposals/2026-06-04_separate_clones_CLAUDE_md_section.md` (the architecture this gap belongs inside)
- `AGENTS/SAM/proposals/2026-06-04_separate_clones_migration_checklist.md`
- Auto-memory `[[project_automem_symlink_migration]]` (the Jun-5 symlink that pulled memory into git)
**Earliest execution window:** bundle with the post-Jun-16 separate-clones migration (same class of problem; same decision-makers).

---

## The problem

`memory/auto/` is the **one directory that breaks disjoint ownership.** Every agent — on both machines — writes to it via the symlink (`~/.claude/projects/-home-willi-Research-workspace/memory → /home/willi/Research-workspace/memory/auto/`). Everything else in the operation is safe because each agent writes only to its own `AGENTS/<NAME>/` slice; memory is the exception, and it has no owner.

The collision surface splits in two:

1. **Individual fact-files** (`feedback_*.md`, `finding_*.md`, …) — each has a unique slug. Two agents writing two different facts = two different filenames = git adds both, **no conflict.** Already safe.
2. **`MEMORY.md` — the shared index.** Every agent appends a one-line pointer to *the same file*. Concurrent appends = merge conflict. **This is not hypothetical:** commit `86aada2a` is literally titled *"auto-memory: capture from laptop (8 laptop-only memories + index merge)"* — the index already had to be merged. With two machines now running agents concurrently, this fires more often.

**Separate-clones does NOT fix this.** SAM's migration solves `AGENTS/<NAME>/` collisions via disjoint ownership, and routes shared files (HEARTBEAT, FORGE) through PROME. Neither mechanism covers memory: you can't make memory disjoint (every agent must write it), and you can't route *every memory write* through PROME (absurd volume). So `memory/auto/` is an **unaddressed gap** in the current separate-clones proposal.

---

## The proposal

Apply the **inbox/outbox pattern to memory.** Agents never write canonical memory directly; they drop proposals, and one processor integrates them.

### Layout

```
memory/auto/
  MEMORY.md                      # canonical index — PROCESSOR-ONLY write
  <slug>.md                      # canonical fact-files — PROCESSOR-ONLY write
  proposed/
    HENRY/                       # HENRY's owned write-set within memory
      add_<slug>.md              # a new fact to integrate
      edit_<slug>.md             # a proposed edit to an existing fact
    SAM/
    BROCK/
    ...
```

### Rules

- **Agents write ONLY to `proposed/<AGENT>/`.** Canonical `MEMORY.md` + fact-files become **read-only to agents.**
- **Proposal files are uniquely named** (`add_<slug>.md` / `edit_<slug>.md`). Many agents dropping distinct files = collision-free, same as today's fact-files.
- **One serialized processor** reads `proposed/*/`, integrates into canonical memory, **regenerates `MEMORY.md`** from fact-file frontmatter (rather than hand-merging), clears the integrated proposals, and commits.

### Why this works

- **Capture is collision-free:** distinct filenames, git just adds them.
- **Integration is serialized:** only the processor touches the canonical index → the `MEMORY.md` append-race disappears by construction.
- **Disjoint ownership is restored:** each agent owns `proposed/<AGENT>/`; the processor owns canonical. Memory now fits the *same* model that makes separate-clones safe — closing the gap, not papering over it.
- **Edits become explicit:** an agent proposing an edit to an existing (possibly cross-agent) memory drops `edit_<slug>.md` instead of editing a shared file directly. Two conflicting proposed edits get reconciled *deliberately by the processor* — surfaced, not silently clobbered. Optional review/veto gate falls out for free.

---

## The one thing this does NOT remove

**Something must be the single writer of the canonical index, and that step must run single-threaded.** If two machines run the processor simultaneously, the collision just moves to the processor. So the processor needs to be one machine or hold a lock. This is unavoidable for *any* solution — the value here is isolating that requirement to one small, infrequent step instead of every agent's every memory write.

---

## Decision points (for Will + PROME)

1. **Processor identity** — a sweep script, PROME, or a designated agent? *Lean: a script, run serialized (one machine / lock).*
2. **Index: regenerated or hand-merged?** *Lean: regenerated from frontmatter `description:` — kills the append-race entirely and removes the manual "add a pointer line" step agents currently must remember.*
3. **Integration latency** — a memory isn't "live" in the index until the processor runs. Acceptable? *Already true today (batch sweep), so not a regression.*
4. **Migration instruction change** — every agent's memory-writing instructions ("write to `~/.claude/.../memory/` + add a `MEMORY.md` pointer") change to "write to `proposed/<AGENT>/`; never touch canonical." Fleet-wide instruction edit = PROME-owned.

---

## Where I might be wrong

1. **Redundancy with a generated index, for pure additions.** If fact-files are already collision-free and the index is regenerated from frontmatter, you arguably don't need a proposal folder for *additions* at all — agents drop fact-files directly, processor regenerates. The folder earns its keep on **edits**, the **ownership boundary**, and the **review gate**. The best system is likely both: capture via `proposed/<AGENT>/`, integrate via regeneration. If Will wants the lightest possible change, "generated index, no proposal folder" is a viable smaller step that fixes ~95% of the pain (the index race) without the folder.
2. **Latency could bite time-sensitive memory.** If an agent writes a memory it needs another agent to see *this session*, the proposal-then-process delay matters. Counter: cross-agent realtime hand-offs already go through inbox/outbox, not shared memory; memory is for durable cross-*session* facts, where latency is fine.
3. **Processor as a new single point of failure.** If the processor doesn't run, proposals pile up un-integrated. Mitigation: run it on the existing sweep cadence; pile-up is visible (folder non-empty) and self-healing on next run.
4. **I benefit from proposing my own simpler write path.** Same bias SAM flagged on separate-clones — the Will + PROME review is the bias-check.

---

## Recommendation

Bundle this into the **post-Jun-16 separate-clones migration** — it's the same class of problem (a shared-write resource that breaks disjoint ownership) and the same decision-makers. If a smaller interim is wanted before then, **"regenerate `MEMORY.md` instead of hand-appending"** alone removes the index race for free and is independent of the folder decision.

**Interim until any of this lands:** keep committing `memory/auto/` via the existing single-machine sweep ("capture from laptop" pattern) — one committer = no concurrent index race. Individual agents should NOT commit `memory/auto/` themselves.
