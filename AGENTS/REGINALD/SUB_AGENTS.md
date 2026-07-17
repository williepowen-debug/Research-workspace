# REGINALD Sub-Agent & Peer Coordination

> **Rewritten 2026-07-17 (audit)** — the prior version (Feb-16 vintage) listed dead `sub-agents/TEX|RENO/` paths, described CREED as a live local sub-agent, omitted OZK, and shipped retired OpenClaw `sessions_spawn` recipes (platform cut 2026-06-26). Prior content → git history.

## Overview

REGINALD is the convergence point for regional-bank stress. Domain coverage that once lived in local sub-agents has largely **promoted to top-level agents** — coordination is now file-based (inbox/outbox + read-only cross-reads), not spawn-based. All agents are Claude Code sessions per root `CLAUDE.md`.

## Directory (verified 2026-07-17)

| Agent | Domain | Where | Status |
|-------|--------|-------|--------|
| **CREED** | CRE / CMBS market-level (DQ, special servicing, maturity wall) | `AGENTS/CREED/` — **top-level Tier-2 agent** (STATUS updated 7/4) | 🟢 LIVE — read `../CREED/STATUS.md`; local `sub-agents/CREED/` = FROZEN Feb fossil (bannered 7/17), workbook TSVs frozen 7/9 |
| **BROCK** | BDC / private credit | `AGENTS/BROCK/` — top-level peer | 🟢 LIVE |
| **CORAL** | Florida (condo/HOA/SIRS, Citizens, FL-bank exposure) | `AGENTS/CORAL/` — top-level peer (promoted 2026-06-19) | 🟢 LIVE |
| **OZK** | Single-name bank deep coverage | `AGENTS/OZK/` — top-level peer | 🟢 LIVE (REGINALD cross-reads; positions OZK-owned) |
| **BELT** | Mortgage-DQ belt (MS/LA/MD) | `sub-agents/BELT/` | 🧊 FROZEN shell (Feb vintage, bannered 7/17) — revive only on a mortgage-DQ catalyst |
| **RENO** | Nevada stress | `archive/sub-agents/RENO/` | ⬜ ARCHIVED (research/sources only, no live STATUS) |
| **TEX** | Texas/Florida stress | `archive/sub-agents/TEX/` | ⬜ ARCHIVED (research/sources only, no live STATUS) |

## Coordination protocol (current)

- **Read-only cross-reads:** peer STATUS files at boot step 9 when relevant (`../CREED/`, `../BROCK/`, `../CORAL/`, `../OZK/`).
- **Signals:** write `.md` packets directly to the target agent's `inbox/` (outbox = PROME-action requests only). See CLAUDE.md Outbox Protocol.
- **Escalation:** threshold breach → STATUS.md + `AGENTS/SIGNALS.md` row per CLAUDE.md Cross-Agent Signals.
- **No spawn recipes** — OpenClaw `sessions_*` API retired 6/26; agents are launched by Will as CC sessions.

## Historical vector-sync map (reference only — Feb vintage, verify before reuse)

CREED → VX-REG-3.01, 9.01-9.03, 13.01-13.02 · BROCK → VX-REG-2.03, 9.04, 12.01 · CORAL → VX-REG-8.01, 15.03, 19.02, FLOW-REG-6.01/20.01. *(VX.tsv itself is STALE-VINTAGE-bannered for Jan-Apr rows — see its header.)*

---

*Last updated: 2026-07-17 (audit rewrite; prior 2026-02-16)*
