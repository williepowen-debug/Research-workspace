# Agent Registration Checklist — canonical surface list (all builds / promotions / splits / retirements / reclassifications)

**Created 2026-07-22** off PROME's 7/12 packet (`inbox/processed/2026-07-12_from-PROME_registration-checklist-gap-group-pages.md`): the 7/12 OSPREY/FALCON/HOMER sweep hit the canonical surfaces but missed the thematic group pages — a PAT-050 instance (registration plumbing asymmetric across surface classes). This file is the single durable home (PAT-041); build-doc WP lines cite it, never restate it.

**Order gate (PAT-047):** ROSTER row lands FIRST (PROME-lane), THEN FLEET_MAP row + FLEET_DIRECTORY regen in one pass — `render_directory.py` fails loud on a FLEET_MAP agent absent from ROSTER. Never add the FLEET_MAP row first.

| # | Surface | Owner/lane | Note |
|---|---------|-----------|------|
| 1 | `PROME/ROSTER.md` | PROME (route packet w/ exact insert text) | Existence + classification. FIRST per PAT-047 |
| 2 | Root `CLAUDE.md` (roster line + transmission chains) | PROME/Will-scoped | |
| 3 | `AGENTS.md` | PROME/Will-scoped | |
| 4 | `AGENTS/_INDEX.md` | shared (Will-authorized edit or PROME packet) | |
| 5 | `AGENTS/_NETWORK.md` | shared | Transmission-chain wiring |
| 6 | **Thematic group pages** — `AGENTS/_CREDIT.md` · `_ENERGY.md` · `_FUNDING_MACRO.md` · `_PRIVATE_CREDIT.md` · `_SYNTHESIS_OPS.md` (sweep ALL five; add any page created since) | shared | **The 7/12 miss.** Human-nav surfaces register in the SAME pass as canonical ones |
| 7 | WALTER `ROUTING_TABLE` (+ `who_cares` / ticker routing where applicable) | WALTER-lane (route packet) | |
| 8 | `FLEET_MAP.tsv` row | DAEDALUS | AFTER ROSTER lands (PAT-047) |
| 9 | `FLEET_DIRECTORY.md` regen (`scripts/render_directory.py`) | DAEDALUS | Same pass as #8; never hand-edit |
| 10 | Peer/parent surface updates (e.g. hub agent's peer list + boot step, sub-agent counts, matrix-row → pointer) | owning agent (packet if live, direct if idle+approved) | Split/promotion cases |
| 11 | Inbox handoff notes to affected consumers | DAEDALUS | Per cross-agent delivery protocol |

**Retirements:** same list, inverse — every surface above is un-wired or successor-pointed in one sweep; check dangling refs by grep across all 11 surface classes.
