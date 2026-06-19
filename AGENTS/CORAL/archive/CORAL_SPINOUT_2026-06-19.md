# CORAL Spinout Record — Promotion to Top-Level Peer Agent

**Date:** 2026-06-19
**Authorized by:** Will (explicit — "Promote to peer agent")
**Executed by:** Claude Code session (branch `claude/cool-keller-yxf8l3`)
**Precedent:** OZK spinout 2026-04-24 (`AGENTS/OZK/archive/OZK_SPINOUT_PLAN.md`) — same pattern.

---

## Why peer, not nested

Claude Code auto-loads CLAUDE.md files walking upward from cwd. As a nested sub-agent at `AGENTS/REGINALD/sub-agents/CORAL/`, any CORAL session also loaded REGINALD's CLAUDE.md — a dual-identity problem. Moving CORAL to `AGENTS/CORAL/` means its session walks up past `AGENTS/` (no CLAUDE.md there) directly to root CLAUDE.md. Clean identity, no dispatch hacks. CORAL now runs its own sessions in parallel with REGINALD, coordinating via inbox/outbox + read-only cross-reads.

Context: CORAL had gone dormant (STATUS last updated 2026-03-03; REGINALD sub-agent sync tracker last logged 2026-02-11) while Florida coverage was de facto carried by MARCO. Promotion makes Florida a first-class agent again.

## What moved

`AGENTS/REGINALD/sub-agents/CORAL/` → `AGENTS/CORAL/` (single `git mv`, history preserved). All existing content came along: STATUS.md, DATA_SOURCES.md, research/, sources/ (incl. SBCF_Research_Feb2026/), workbook/.

## What was created (peer-agent infrastructure)

| File | Source |
|------|--------|
| `CLAUDE.md` | Rewritten as a peer-agent instruction file (was a 75-line sub-agent stub) — boot/closeout protocol, git protocol, doc ownership, domain scope, cross-agent signals; modeled on OZK/MARCO. |
| `MEMORY.md` | NEW — Feedback/Findings/References + session handoff. |
| `CALENDAR.md` | NEW — forward FL catalyst calendar (extracted from the old STATUS monitoring table; flagged stale). |
| `LESSONS.md` | NEW — seeded from REGINALD/OZK LESSONS + FL-specific rules. |
| `inbox/`, `outbox/` (with `processed/`, `delivered/`) | NEW dirs — replaced single-file `INBOX.md`/`OUTBOX.md`. The one pending signal (BayFirst SBA exit, 2026-03-04) migrated to `inbox/`. |
| `archive/CORAL_SPINOUT_2026-06-19.md` | This file. |

## Reference updates (other files)

- **root `CLAUDE.md`** — added `CORAL*` to active agents; added promotion note line alongside the OZK note.
- **`AGENTS/REGINALD/CLAUDE.md`** — CORAL removed from sub-agent coordination lists; pointers updated to `../CORAL/`; noted CORAL is now a peer.
- **`AGENTS/REGINALD/SUB_AGENTS.md`** — CORAL row marked promoted-to-peer.
- **`AGENTS/REGINALD/STATUS.md`** — CORAL dashboard row annotated as peer agent.
- **`AGENTS/MARCO/CLAUDE.md`** — `REGINALD/CORAL` references updated to `CORAL` (now a peer); reconciliation boundary noted.
- **`AGENTS_DIRECTORY.md`** — CORAL given its own peer row.
- **`docs/ARCHITECTURE.md`** — CORAL moved from REGINALD-subs to peer list.

## What CORAL still owes (first post-promotion session)

CORAL's STATUS.md was NOT refreshed — promotion was structural only. The Mar-3 dashboard is stale and in places contradicted by MARCO's April reads (condo inventory tightened to 8.9mo; acute timing pushed to winter 2026-27). First session must refresh STATUS, capture passed-catalyst outcomes, and establish the MARCO reconciliation handshake. See `MEMORY.md` NEXT SESSION.

## REGINALD ↔ CORAL ↔ MARCO boundary (locked)

- **CORAL** owns bank-/CRE-level FL stress → feeds REGINALD's convergence matrix.
- **MARCO** owns population-driven FL stress (snowbird $, airport pax, migration).
- **REGINALD** integrates CORAL's FL loss estimates as one geography in the multi-bank matrix.
- Shared metrics (condo inventory, FL airports, migration): MARCO is the live owner; CORAL references rather than re-deriving.
