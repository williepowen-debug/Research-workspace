# PROPOSAL: Fleet Closeout-Protocol Addendum (Tier-1 standards)
**Date:** 2026-06-26 | **Author:** Prome (Claude Code) | **Status:** ✅ APPROVED + APPLIED (Will, 2026-06-26) — root `CLAUDE.md` sections A+B live (Git Protocol "Before committing" step 5 + new "Data Hygiene" section)
**Source:** `PROME/cluster/2026-06-26_fleet_arch_compare.md` (5-agent architecture review)

> **Approval gate:** This codifies the Tier-1 fixes — which agents self-applied to their own dirs on 2026-06-26 — as **canonical fleet policy**. It proposes edits to **root `CLAUDE.md`** (shared, all agents). **Do not apply until Will approves.** The per-agent self-applications already done this session stand regardless; this addendum makes them the standing rule for every agent (incl. those not in today's batch).

---

## What changed this session (already applied, own-dir)
CARL / REGINALD / LABOR / BROCK / SHADE each applied T1a–T1c to their own trees and committed. This addendum generalizes those into fleet policy so the rule survives and binds agents who weren't in the room.

---

## Proposed additions to root `CLAUDE.md`

### A. Under "Git Protocol → At session end" (new step before commit)

> **Pre-commit sanity check (mandatory):** run `git status -- AGENTS/<YOUR_NAME>/` before committing. Confirm: no dangling deletions (bash-mv residue), no unstaged new files you meant to commit, no changes staged outside your own dir. This is a 5-second guard against the `git mv`-vs-`bash mv` residue class (see auto-memory `git_mv_for_inbox_processing`) and the cross-dir-leak class.

*(Rationale: SHADE hit exactly this today — a `processed/` copy committed but the `inbox/` deletion left dangling, forcing a separate cleanup commit in the push window.)*

### B. New "Data hygiene" subsection (closeout discipline)

> **Ledger staleness (STATUS is canonical truth):** TSV workbook ledgers (KB/VX/FLOW/etc.) drift behind STATUS silently — this was a *universal* finding across the fleet. Each agent must either (a) **freeze** a dead ledger with a header banner — `FROZEN <date> — not maintained; STATUS is canonical. Do not cite rows as current.` — and stop maintaining it, or (b) keep it **live** with a **boot-time mtime staleness alert** (surface "X.tsv stale Nd" at boot, not at closeout). Do not leave a ledger in the silent-rot middle state.
>
> **Research/sources retirement:** at closeout, apply — *file >60 days old AND not boot-read AND not referenced by a live doc → `git mv` to `archive/`.* Prevents the research-graveyard accumulation found in every agent (LABOR 17 March files, etc.).

---

## Explicitly OUT of scope (do not build now)
- **Outbox-kill / NEXUS_BRIEF-as-send-surface / inbox boot-auto-triage** (Tier-4). These touch file-based messaging, which is **slated for replacement** (auto-memory `messaging_overhaul`). Interim guidance only: *stop writing dead outbox files*; do **not** build a new send protocol the overhaul will discard. Route these to the messaging-overhaul design instead.
- STATUS §-section standard, unified prediction/trigger schema, per-entity folder tiering, calibration-loop fix — Tier-2/3, separate scoped passes.

---

## Rollout
1. **Will approves this addendum** → Prome (or Will) edits root `CLAUDE.md` sections A + B above. *(Root CLAUDE.md is shared — single coordinated edit, flagged, not agent-by-agent.)*
2. Tier-1 already self-applied by today's 5 agents.
3. Next boot, every agent inherits the standard from root CLAUDE.md.
4. Agents not in today's batch apply T1a–T1c on their next session per the new rule.

**Decision needed from Will:** approve the root-CLAUDE.md edits (A + B) as written, edit, or hold.
</content>
