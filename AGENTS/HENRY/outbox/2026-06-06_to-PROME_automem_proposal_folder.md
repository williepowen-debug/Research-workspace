## 2026-06-06 — To: PROME
**Signal:** Auto-memory collision fix proposal — pair it with SAM's separate-clones migration.
**Detail:** `memory/auto/` is the one shared-write directory that breaks the disjoint-ownership model separate-clones relies on (every agent writes the shared `MEMORY.md` index; commit `86aada2a` already shows an "index merge"). SAM's separate-clones proposal does NOT cover it. HENRY drafted a fix (Will's idea): per-agent `proposed/<AGENT>/` folders + canonical memory becomes processor-only + one serialized processor that regenerates the index. Restores disjoint ownership to memory. Draft (REVIEW-NOT-APPLY): `AGENTS/HENRY/proposals/2026-06-06_automem_proposal_folder.md`. Recommend bundling into the post-Jun-16 separate-clones decision; lighter interim available ("regenerate index instead of hand-append" alone fixes ~95%).
**Source:** HENRY analysis + Will (this session).
**Priority:** 🟡
