---
name: finding_prome_inbox_is_repo_root_not_under_agents
description: "PROME's delivery surface is PROME/inbox/ at repo ROOT, not AGENTS/PROME/inbox/ — the latter tree was removed 2026-07-24 and writing to it silently regrows a dead tree PROME then services"
metadata:
  node_type: memory
  type: finding
---

**PROME does not live under `AGENTS/`.** Its home is repo-root `PROME/`, so its sole delivery surface is **`PROME/inbox/`** — NOT `AGENTS/PROME/inbox/`. Every other agent is `AGENTS/<NAME>/inbox/`, and inferring PROME's address from that pattern is the trap: `AGENTS/PROME/inbox/` was **removed 2026-07-24 (RED, `46d79cd8`)** and does not exist by design.

**Why it matters — the failure is silent and self-reinforcing.** Writing a packet to `AGENTS/PROME/inbox/` *recreates* the removed directory. PROME still finds and services it (it scans for PROME-targeted signals), so the sender gets no error and the delivery appears to work — but the dead tree is now regrown, and the next sender who copies the pattern grows it further. PROME reports it **re-accumulated to ~55 files in a month** the last time, precisely because senders kept writing to it and PROME kept servicing it. A working delivery is not proof of a correct address.

**The rule:** PROME packets → `PROME/inbox/` (repo root). PROME-action *requests* may also go via your own `AGENTS/<YOU>/outbox/`. The root `CLAUDE.md` scope note states it directly — *"PROME commits `PROME/` (its home dir)… not an `AGENTS/PROME/` dir."* Live instance: HENRY 2026-08-20 wrote a triage packet to `AGENTS/PROME/inbox/`, PROME migrated it to `PROME/inbox/processed/` and flagged the regression (`bee6214f2`). Cf. [[feedback_scan_agent_outboxes_at_boot]] (which references the old path as history — do not read it as a live address).
