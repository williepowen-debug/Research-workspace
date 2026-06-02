# PROME STATUS.md
**Updated:** 2026-06-02 ~10:55 ET (OpenClaw Prome — closeout after boot-surface + HEARTBEAT rehab)

## Core State

**Operational priority:** Prome is boot-safe again after the Jun 2 catch-up. Will explicitly deprioritized trade-position work for this pass; old trade rails remain verification-required until a separate reconciliation pass.

**Regime:** Public credit and vol remain calm while stress persists in Japan/FX, energy, BDC/private-credit marks, and duration. Current read is **divergence**, not confirmed public-credit/vol transmission.

**Live dashboard anchor, Jun 2 ~10:45 ET:** HY OAS **272bps [FRED 6/1 close]** 🟢, CCC OAS **946bps [FRED 6/1 close]** 🟡, VIX **16.12** 🟢, Brent **$94.90** 🟡, USD/JPY **159.82** 🔴, BIZD **$12.78** 🔴. HEARTBEAT is current as of Jun 2 closeout.

---

## Sync / Repo State

| Item | Status | Note |
|---|---|---|
| GitHub sync | ✅ Clean | Local `master` matched `origin/master` before closeout edits; verify with `git status` at next boot. |
| Local stale edits | ✅ Resolved | Will approved discarding stale local generated edits in `AGENTS/PROME/LAST_COMPLETION.md` and `PROME/FLEET_SCAN.md`; pull then fast-forwarded cleanly. |
| Prome boot-surface rehab | ✅ Pushed | Jun 2 rehab package committed/pushed. |
| WALTER Iran-anchor refresh | ✅ Landed | WALTER refreshed to narrative-fork + kinetic-acceleration frame. |
| SENTRY scheduled feed pushes | ✅ Disabled | Manual `workflow_dispatch` preserved; twice-daily master churn stopped. |
| HEARTBEAT refresh | ✅ Pushed | Root heartbeat now reflects Jun 2 regime/levels. |
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
| `HEARTBEAT.md` | ✅ Current | Refreshed Jun 2 with live dashboard, WALTER frame, and SENTRY pointer. Cadence/ownership remains an open design decision. |
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
| Refresh Prome boot files | ✅ | Completed and pushed Jun 2. |
| Disable SENTRY scheduled pushes | ✅ | Completed; stops twice-daily master churn. |
| Integrate WALTER Jun 2 frame | ✅ | Prome surfaces now carry narrative-fork + kinetic-acceleration caveat. |
| Add fresh OpenClaw handoff | ✅ | `PROME/HANDOFF.md` has Jun 2 top block. |
| Refresh HEARTBEAT | ✅ | Completed with Jun 2 live dashboard. |
| Reconcile old trade rails / fills | 🟠 | Deferred per Will; mark as verification-required, not actionable. |
| Decide HEARTBEAT cadence / ownership | 🟠 | Open design decision for next operating pass. |

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

Close out this session cleanly. Next session should not reopen boot rehab unless a specific stale surface is found; choose a bounded next lane such as HEARTBEAT cadence, Prome inbox triage, position-state reconciliation, or stale domain revive shortlist.
