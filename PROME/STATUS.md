# PROME STATUS.md
**Updated:** 2026-06-02 ~10:15 ET (OpenClaw Prome — Phase 1 factual cleanup after SENTRY/WALTER updates)

## Core State

**Operational priority:** Keep Prome boot-safe after the Jun 2 catch-up. Will explicitly deprioritized trade-position work for this pass. Current work is factual cleanup of Prome surfaces, then handoff, then HEARTBEAT.

**Regime:** Public credit and vol remain calm while stress persists in Japan/FX, energy, BDC/private-credit marks, and duration. Current read is **divergence**, not confirmed public-credit/vol transmission.

**Live dashboard anchor, Jun 2 ~09:45 ET:** HY OAS **272bps [FRED 6/1 close]** 🟢, CCC OAS **946bps [FRED 6/1 close]** 🟡, VIX **16.18** 🟢, Brent **~$95** 🟡, USD/JPY **159.79** 🔴, BIZD **~$12.74** 🔴. Do not quote old HEARTBEAT/TODAY levels.

---

## Sync / Repo State

| Item | Status | Note |
|---|---|---|
| GitHub sync | ✅ Clean | `master` matches `origin/master` at HEAD `e8e11442` before this Phase 1 cleanup edit pass. |
| Local stale edits | ✅ Resolved | Will approved discarding stale local generated edits in `AGENTS/PROME/LAST_COMPLETION.md` and `PROME/FLEET_SCAN.md`; pull then fast-forwarded cleanly. |
| Prome boot-surface rehab | ✅ Pushed | Jun 2 rehab package committed/pushed as `79a66053`. |
| WALTER Iran-anchor refresh | ✅ Landed | Commit `ddb94d13` refreshed WALTER to narrative-fork + kinetic-acceleration frame. |
| SENTRY scheduled feed pushes | ✅ Disabled | Commit `e8e11442`; manual `workflow_dispatch` preserved. |
| GitHub source-of-truth rule | ✅ Active | Local edits remain subordinate until explicitly committed/pushed. |

---

## Prome Boot Surface Trust

| File | Current trust | Note |
|---|---|---|
| `PROME/SCRATCH.md` | ✅ Current | Rewritten Jun 2; session handoff for state rehab. |
| `PROME/TODAY.md` | ✅ Current | Rewritten Jun 2; state-rehab objective and live dashboard. |
| `PROME/STATUS.md` | ✅ Current | This file. |
| `PROME/FLEET_SCAN.md` | ✅ Current | Rewritten Jun 2 from bounded fleet scan. |
| `PROME/ACTIVE_DECISIONS.md` | ✅ Current safety index | Old trade rails marked verification-required until broker/Will state is verified. |
| `HEARTBEAT.md` | ⚠️ Stale | Injected but not safe for levels; scenario narrative predates Jun 2 WALTER/SENTRY cleanup and needs a separate Phase 3 refresh. |
| `PROME/CLAUDE_CODE_HANDOFF.md` | Historical | Useful audit trail, not current boot state. |

---

## Agent / Domain State Since Prome Went Stale

| Domain | Freshness | Current state for Prome |
|---|---|---|
| **SAM / Japan** | Fresh Jun 1 | BOJ Jun 16 single-path base case; market ~88%, SAM 70%; USD/JPY near 160 intervention zone; v1.5 says Sep $60 calls not warranted. |
| **BRENT / Energy** | Fresh Jun 1 + WALTER Jun 2 correction | Iran/energy stress re-armed, but channel state is contested: Tasnim/IRGC suspension vs MFA/Trump ongoing/rapid-pace denial. Trump rhetoric is tape-not-info in both directions. |
| **VIOLET / Vol** | Fresh Jun 1 | R11 analog dead / gradual fade won; R12 technically terminated but spot/SKEW watch near re-establishment; timing reset later. |
| **MARCO / Migration-labor** | Fresh Jun 1 | Acute crisis softened; structural ag-labor and Canadian travel channels remain. |
| **CARL / Consumer** | Fresh enough May 31 | Consumer/stagflation hardened via GDP/PCE; important but not state-rehab blocker. |
| **WALTER / Routing** | Fresh Jun 2 | Iran anchor reverified: **narrative-fork + kinetic-acceleration**. Kuwait strike cadence load-bearing; Bab al-Mandab rhetorical only; next anchor boundary 2026-06-09. WALTER still owns news/signal routing. |
| **REGINALD / Banks** | Domain stale May 21 | WAL v2.2 remains last deep state; later commits were housekeeping. Do not refresh until concrete need. |
| **BROCK / Private credit** | Domain stale May 21 | BIZD remains red; APO now below $130 live. Needs refresh if PC/BDC decision becomes live, not during this catch-up pass. |
| **HENRY / Market structure** | Domain stale May 21 | R11 window has passed and needs adjudication if used. Do not rely on old clock language. |
| **LIQUID / Funding-duration** | Stale May 20 | Funding/duration state needs refresh before any duration decision. |
| **BOND / Auctions** | Stale May 21 | June 9-11 nominal 10Y matrix remains next hard test; refresh closer to auction window. |

---

## Current Work Queue

| Action | Pri | Status |
|---|---:|---|
| Refresh Prome boot files | ✅ | Jun 2 refresh committed/pushed as `79a66053`. |
| Disable SENTRY scheduled pushes | ✅ | Completed as `e8e11442`; stops twice-daily master churn. |
| Integrate WALTER Jun 2 frame | 🟠 | Phase 1 cleanup in progress across Prome surfaces. |
| Add fresh OpenClaw handoff | 🟠 | Phase 2; needed because `PROME/HANDOFF.md` top block is May 17. |
| Refresh HEARTBEAT | 🟠 | Phase 3; pull live dashboard first. |
| Reconcile old trade rails / fills | 🟠 | Deferred per Will; mark as verification-required, not actionable. |

---

## Rules of Engagement

- **No trade execution without Will approval.**
- **No trade recommendations in the state-rehab pass unless explicitly requested.**
- **No external/public messages without approval.**
- **Do not spawn persistent agents casually:** CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome.
- **WALTER routes signals/news; Prome maintains state, tasking, rails, and Will-facing synthesis.**
- **Use explicit path staging only; never `git add .` or `git add -A`.**
- **Read current files before editing; verify after edits.**

---

## Next Best Action

Finish Phase 1 factual cleanup, verify the diff, then proceed to Phase 2 (`PROME/HANDOFF.md`) before touching HEARTBEAT.
