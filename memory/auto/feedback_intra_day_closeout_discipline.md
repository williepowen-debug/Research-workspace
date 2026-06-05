---
name: Intra-Day Closeout Discipline
description: Run WALTER closeout (spawn-protocol steps 12-15) at every session end, not just end-of-day; multi-session-days must honor intermediate closeout to prevent STATUS-staleness gap
type: feedback
originSessionId: 921b2057-065c-4d09-93e2-1984222066e4
---
Every WALTER session that dispatched signals, modified BOARD/INDEX, appended to route_log/kill_log, or changed any WALTER ops/design files runs closeout steps 12-15 BEFORE push — never deferred to a later "wrap-up" session.

**Why:** the architectural intent of LAST_COMPLETION + MEMORY + STATUS is single-source-of-truth at next-session boot. That only works if every session honors closeout. When intermediate sessions skip closeout (e.g., 2026-05-08 sessions c10a0cef + 97c2e353 committed BOARD updates without lead-paragraph regen), handoff docs end up N sessions stale. Next session's boot has to do git-log archaeology + commit-message reconstruction to recover truth — ~5-10 min per fresh boot, with risk of propagating wrong state if archaeology fails or if next-WALTER trusts the stale docs.

**How to apply:** at every session-end before `git push`, run steps 12-15 in spawn protocol order:
- 12: STATUS lead-paragraph regen + (b) NETWORK AWARENESS subsection regen + (c) FILTER POSTURE refresh + (d) SESSION LOG entry
- 13: REGISTRY.tsv WALTER row Updated + Focus
- 14: MEMORY.md CHANGES SINCE / NEXT SESSION rewrite
- 15: LAST_COMPLETION.md full rewrite

Even if you plan to run another session today. **Especially** if you plan to run another session today — the intermediate closeout is what makes the multi-session-day pattern not break the architecture.

**Codified 2026-05-09** in `AGENTS/WALTER/CLAUDE.md` spawn-protocol Closeout section header (paragraph immediately after `### Closeout` heading, before step 12).
