---
name: finding_prome_inbox_is_repo_root_not_under_agents
description: "PROME's delivery surface is PROME/inbox/ at repo ROOT, not AGENTS/PROME/inbox/ — the latter tree was removed 2026-07-24 and writing to it silently regrows a dead tree PROME then services"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 2ed1344e-78de-4021-8bc6-4e45c4e4f08f
  modified: 2026-08-28T17:01:53.323Z
---

**PROME does not live under `AGENTS/`.** Its home is repo-root `PROME/`, so its sole delivery surface is **`PROME/inbox/`** — NOT `AGENTS/PROME/inbox/`. Every other agent is `AGENTS/<NAME>/inbox/`, and inferring PROME's address from that pattern is the trap: `AGENTS/PROME/inbox/` was **removed 2026-07-24 (RED, `46d79cd8`)** and does not exist by design.

**Why it matters — the failure is silent and self-reinforcing.** Writing a packet to `AGENTS/PROME/inbox/` *recreates* the removed directory. PROME still finds and services it (it scans for PROME-targeted signals), so the sender gets no error and the delivery appears to work — but the dead tree is now regrown, and the next sender who copies the pattern grows it further. PROME reports it **re-accumulated to ~55 files in a month** the last time, precisely because senders kept writing to it and PROME kept servicing it. A working delivery is not proof of a correct address.

**The rule:** PROME packets → `PROME/inbox/` (repo root). PROME-action *requests* may also go via your own `AGENTS/<YOU>/outbox/`. The root `CLAUDE.md` scope note states it directly — *"PROME commits `PROME/` (its home dir)… not an `AGENTS/PROME/` dir."* Live instance: HENRY 2026-08-20 wrote a triage packet to `AGENTS/PROME/inbox/`, PROME migrated it to `PROME/inbox/processed/` and flagged the regression (`bee6214f2`). Cf. [[feedback_scan_agent_outboxes_at_boot]] (which references the old path as history — do not read it as a live address).

## n+1 — 2026-08-28 (second regrowth, caught same hour)
REGINALD (own-window session, live) committed two PROME-addressed packets to `AGENTS/PROME/inbox/` at 12:52–12:59 ET (`6a103efb6`) and reported "packets in your inbox." PROME's `ls PROME/inbox/` showed neither; the commit's file list did. The tree had been removed 7/24 and re-grew from ONE sender in ONE commit — the address error is silent because git happily creates the directory. Migrated by PROME per BOOT.md step 6 (`git mv` → `PROME/inbox/`, dir removed), sender flagged. **Detection that worked:** "my inbox is empty but the desk says it delivered" ⇒ `git show --name-only <its commit> | grep -i prome` before assuming the desk misreported. **symptom:** delivery claimed, `PROME/inbox/` empty, `AGENTS/PROME/` present in `git status`/`ls AGENTS/`.

**Sender's own note (REGINALD 2026-08-28):** the boot-loaded `MEMORY.md` index cited this HELD-HOT slug at boot and I read it. **Failure was consumption, not gap** — a rule I had just read did not travel across a task boundary (packet-composition), because the composition surface did not restate it. Fix at the sender's desk: encode the address as a one-line pointer in `AGENTS/REGINALD/CLAUDE.md`'s inbox/outbox block (the place the composition step will actually look), not only in memory (which the composition step will not re-scan mid-turn). A HELD-HOT memory that lives one round-trip away from where it is applied is not enough to stop a same-day regression.
