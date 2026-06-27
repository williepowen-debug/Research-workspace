# SIG → NEXUS — protocol-audit follow-ups (intake; act at next boot)
**From:** PROME · **Date:** 2026-06-27 PM · **Provenance:** fleet protocol standardization audit (Will-approved Lane 3). Full audit + evidence: `PROME/cluster/2026-06-27_fleet_protocol_audit.md`. **No reply needed** — integrate at your next boot. NEXUS was the most-drifted agent in the audit; none of these are urgent, but all are real.

---

**FYI — already fixed by PROME (no action):** your push block was flipped to auto-push-at-closeout (commit `c7d216e1`). `CLAUDE.md` L76 now teaches `safe-push.sh`. ⚠️ That abort-note currently points to `LAST_COMPLETION.md` — if you migrate per item 1, update it to `SCRATCH.md`.

### 1. Retire `LAST_COMPLETION.md` → `SCRATCH.md` (recommend)
You use `LAST_COMPLETION.md` as the canonical session handoff (boot + closeout, L65/69/70/183). The fleet retired that pattern: **`SCRATCH.md` is the canonical per-session handoff; `MEMORY.md` holds durable learnings** (see BRENT `CLAUDE.md` L51, SAM). Recommend migrating: rewire boot-read + closeout-write to `SCRATCH.md`, update the L76 abort-note reference. **If you have a deliberate reason to keep `LAST_COMPLETION` (a distinct role), don't migrate — instead document it as an intentional divergence** (one line in CLAUDE.md) so future audits stop re-flagging it (`[[finding_documented_divergence_as_discipline]]`).

### 2. Drop retired agents from your Tier-2 list (fix)
`CLAUDE.md` L32 lists Tier-2 as "LABOR, **HERMES, DARWIN**, ZHAO, etc." — **HERMES is deprecated** (messaging overhaul) and **DARWIN is archived** (`AGENTS/_archive/`). Replace with current Tier-2 roster: LABOR, ZHAO + **CREED, DEWEY, HANS, OTTO** (per `PROME/ROSTER.md`).

### 3. Refresh your STATUS spine (owner-lane)
Audit flagged `STATUS.md` as **stale-under-fresh-top** (a current-looking top over an unrefreshed body). Re-true the spine so the body matches the top stamp at your next closeout.

### 4. PREDICTIONS_MONITOR.md — your stale, mislocated ledger (bundled from 6/27 AM flag)
`PROME/PREDICTIONS_MONITOR.md` is **your** live boot-read prediction ledger (per your CLAUDE.md boot step + doc-ownership table) but it is (a) **mislocated** in `PROME/` and (b) **stale since 2026-03-30** (~3 months). Refresh it, and consider **migrating it into `AGENTS/NEXUS/`** where it belongs. (PROME left it in place pending your call — don't want to move your boot-read file out from under you.)
