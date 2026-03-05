# Systems Thinking — Design Principles

*Notes on building better agent systems. Started Mar 4, 2026.*

---

## Silo complexity between steps

When designing agent workflows, eliminate complexity *between* steps. If an action requires a different cognitive mode than the primary task, don't bundle it — silo it off as its own command.

**Example:** INBOX processing was step 3 of every agent's spawn protocol. But processing cross-agent signals is a completely different mode than executing a time-sensitive task like "process NFP." Mixing them in one spawn meant agents spent tokens on irrelevant parsing, produced worse output on both tasks, and occasionally got distracted from the actual priority.

**Fix:** Removed INBOX from spawn protocol entirely. It's now a separate command — spawn agents specifically for inbox processing when needed, not as a tax on every spawn.

**The principle:** Some actions *look* like they belong together (boot up → check mail → do work) but actually compete for attention. Systems get better when you identify those hidden conflicts and separate them. Simplicity between steps > comprehensiveness within steps.

**Watch for:** The risk of siloing is that siloed tasks become "the thing that never gets done." Need a mechanism to ensure they still happen (cron, batch spawns, etc.).
