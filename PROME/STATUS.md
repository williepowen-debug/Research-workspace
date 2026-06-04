# PROME STATUS.md
**Updated:** 2026-06-04 ~17:35 ET (OpenClaw Prome — boot surface refresh after Jun 3-4 signal ingestion)

## Core State

**Operational priority:** Prome boot surfaces are being refreshed from Jun 2 cleanup mode into Jun 4 operating mode. The two direct Prome signals have been ingested: (1) HENRY superseded the old TLT 5/22 ticket, and (2) SAM flagged a pathspec-commit migration to reduce shared-repo overwrite risk.

**Regime:** Public credit and vol remain calm while stress persists in Japan/FX, energy, BDC/private-credit marks, and duration. Current read is **divergence**, not confirmed public-credit/vol transmission.

**Live dashboard anchor, Jun 4 ~17:45 ET:** HY OAS **275bps [FRED 6/3 close]** 🟢, CCC OAS **947bps [FRED 6/3 close]** 🟡, VIX **15.40** 🟢, Brent **$95.14** 🟡, USD/JPY **160.00** 🔴, BIZD **$12.70** 🔴, TLT **$85.50** 🟡. `HEARTBEAT.md` has been refreshed with this root state.

---

## Sync / Repo State

| Item | Status | Note |
|---|---|---|
| GitHub sync | ✅ Clean | Local `master` matched `origin/master` before closeout edits; verify with `git status` at next boot. |
| Local stale edits | ✅ Resolved | Will approved discarding stale local generated edits in `AGENTS/PROME/LAST_COMPLETION.md` and `PROME/FLEET_SCAN.md`; pull then fast-forwarded cleanly. |
| Prome boot-surface rehab | ✅ Pushed | Jun 2 rehab package committed/pushed. |
| WALTER Iran-anchor refresh | ✅ Landed | WALTER refreshed to narrative-fork + kinetic-acceleration frame. |
| SENTRY scheduled feed pushes | ✅ Disabled | Manual `workflow_dispatch` preserved; twice-daily master churn stopped. |
| HEARTBEAT refresh | ✅ Pushed | Root heartbeat now reflects Jun 4 regime/levels. |
| GitHub source-of-truth rule | ✅ Active | Local edits remain subordinate until explicitly committed/pushed. |

---

## Prome Boot Surface Trust

| File | Current trust | Note |
|---|---|---|
| `PROME/SCRATCH.md` | ✅ Current | Rewritten Jun 4; boot handoff after signal ingestion. |
| `PROME/TODAY.md` | ✅ Current | Rewritten Jun 4; live dashboard and work queue. |
| `PROME/STATUS.md` | ✅ Current | This file. |
| `PROME/FLEET_SCAN.md` | ✅ Current | Rewritten Jun 4 as bounded post-pull scan. |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Current safety index | HENRY Jun 3 TLT supersession ingested; old 5/22 roll ticket no longer actionable. |
| `HEARTBEAT.md` | ✅ Current | Refreshed Jun 4 with live levels, TLT supersession, pathspec migration, and root pending items. |
| `PROME/CLAUDE_CODE_HANDOFF.md` | Historical | Useful audit trail, not current boot state. |

---

## Agent / Domain State Since Prome Went Stale

| Domain | Freshness | Current state for Prome |
|---|---|---|
| **SAM / Japan** | Fresh Jun 1 + Jun 4 Prome signal | BOJ Jun 16 single-path base case; USD/JPY now **160.01** live. SAM also flagged pathspec migration; Prome/SAM done, other owner edits pending. |
| **BRENT / Energy** | Fresh Jun 1 + WALTER Jun 2 correction | Iran/energy stress re-armed, but channel state is contested: Tasnim/IRGC suspension vs MFA/Trump ongoing/rapid-pace denial. Trump rhetoric is tape-not-info in both directions. |
| **VIOLET / Vol** | Fresh Jun 1 | R11 analog dead / gradual fade won; R12 technically terminated but spot/SKEW watch near re-establishment; timing reset later. |
| **MARCO / Migration-labor** | Fresh Jun 1 | Acute crisis softened; structural ag-labor and Canadian travel channels remain. |
| **CARL / Consumer** | Fresh enough May 31 | Consumer/stagflation hardened via GDP/PCE; important but not state-rehab blocker. |
| **WALTER / Routing** | Fresh Jun 2 | Iran anchor reverified: **narrative-fork + kinetic-acceleration**. Kuwait strike cadence load-bearing; Bab al-Mandab rhetorical only; next anchor boundary 2026-06-09. WALTER still owns news/signal routing. |
| **REGINALD / Banks** | Domain stale May 21 | WAL v2.2 remains last deep state; later commits were housekeeping. Do not refresh until concrete need. |
| **BROCK / Private credit** | Domain stale May 21 | BIZD remains red; APO now below $130 live. Needs refresh if PC/BDC decision becomes live, not during this catch-up pass. |
| **HENRY / Market structure** | Jun 3 TLT signal; broader domain partially refreshed | TLT 5/22 ticket superseded. Jun $85P salvage is Will-handled; Sep add deferred to CPI. Do not rely on old R11 clock language without current HENRY. |
| **LIQUID / Funding-duration** | Stale May 20 | Funding/duration state needs refresh before any duration decision. |
| **BOND / Auctions** | Stale May 21 | June 9-11 nominal 10Y matrix remains next hard test; refresh closer to auction window. |

---

## Jun 3-4 Prome Signals Ingested

| Signal | Status | Prome handling |
|---|---|---|
| HENRY TLT ticket supersession | ✅ Ingested | `PROME/ACTIVE_DECISIONS.md` now marks the old 5/22 TLT roll ticket as superseded. Jun $85P are a Will-handled catalyst salvage bet; Sep add waits for CPI confirmation. |
| SAM pathspec migration audit | ✅ Tracker created | `PROME/PATHSPEC_MIGRATION_STATUS.md` tracks 8 agents / 9 sites. Prome fixed its own `AGENTS/PROME/CLAUDE.md` protocol; other agents own their own edits at next boot. |

## Current Work Queue

| Action | Pri | Status |
|---|---:|---|
| Refresh Prome boot files | ✅ | Jun 4 refresh completed after signal ingestion. |
| Disable SENTRY scheduled pushes | ✅ | Completed; stops twice-daily master churn. |
| Integrate WALTER Jun 2 frame | ✅ | Prome surfaces now carry narrative-fork + kinetic-acceleration caveat. |
| Add fresh OpenClaw handoff | ✅ | `PROME/HANDOFF.md` has Jun 2 top block. |
| Refresh HEARTBEAT | ✅ | Refreshed Jun 4 with live dashboard/root state. |
| Ingest HENRY TLT supersession | ✅ | Old 5/22 TLT roll ticket superseded by Jun 3 Will/HENRY handling. |
| Track pathspec migration | 🟠 | Tracker created; Prome/SAM done; remaining owners pending. |
| Refresh root HEARTBEAT | ✅ | Completed Jun 4. |
| Reconcile old trade rails / fills | 🟠 | Deferred per Will; non-TLT rails remain verification-required, not actionable. |
| Decide HEARTBEAT cadence / ownership | 🟠 | Open design decision for next operating pass. |

---

## Rules of Engagement

- **No trade execution without Will approval.**
- **No trade recommendations in the state-rehab pass unless explicitly requested.**
- **No external/public messages without approval.**
- **Do not spawn persistent agents casually:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- **WALTER routes signals/news; Prome maintains state, tasking, rails, and Will-facing synthesis.**
- **Use pathspec commits only; never `git add .`, `git add -A`, or broad `git reset HEAD`.** Track migration in `PROME/PATHSPEC_MIGRATION_STATUS.md`.
- **Read current files before editing; verify after edits.**

---

## Next Best Action

Verify and commit the Jun 4 root HEARTBEAT refresh. Next recommended lane: decide whether to coordinate remaining pathspec owner edits or pause cleanup before position reconciliation.
