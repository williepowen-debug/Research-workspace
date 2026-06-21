# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-21 09:55 ET (OpenClaw Prome — closeout after AGENTS organization + PROME path cleanup + canonical network map)

## What Just Happened

1. **AGENTS directory organization landed and pushed without moving canonical folders.**
   - Added grouped index files under `AGENTS/`: `_INDEX.md`, `_CREDIT.md`, `_PRIVATE_CREDIT.md`, `_ENERGY.md`, `_FUNDING_MACRO.md`, `_SYNTHESIS_OPS.md`.
   - Kept canonical paths flat as `AGENTS/<NAME>/` to avoid breaking scripts, docs, and Claude/OpenClaw workflows.
   - Linked grouped views from `AGENTS.md` and `AGENTS_DIRECTORY.md`.

2. **PROME path cleanup landed and pushed.**
   - Scanned PROME files for broken Markdown links and stale concrete path refs.
   - Fixed retired `PROME/TOSCANINI/...` references in live Prome docs to promoted live files (`PROME/AUTONOMY.md`, `PROME/COMPLETION_SPEC.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/ORCHESTRAL_LAYER_DESIGN.md`) or historical archive `PROME/archive/TOSCANINI_2026-03/`.
   - Fixed processed/delivered inbox/outbox paths and BOND/HENRY historical references where moved files had canonical current locations.
   - Verification before commit: broken Markdown links across PROME = 0; missing concrete refs in live PROME = 0; `git diff --check` clean.

3. **Canonical agent network map landed and pushed.**
   - Created `AGENTS/_NETWORK.md` as the live topology / transmission map source.
   - Updated `dashboard/index.html` Network tab to mirror the canonical map.
   - Demoted standalone `dashboard/network.html` to a pointer/redirect so it cannot drift as a second live graph.
   - Left old `PROME/archive/agent_network.*` untouched as historical archive.
   - Verification before commit: dashboard nodes matched canonical map; network nodes missing dirs = none; touched doc links clean; dashboard inline JS parsed cleanly.

4. **Two commits were pushed and repo is synced.**
   - `1cb8a774 Add grouped agent directory indexes`
   - `9a6f155a Clean up Prome paths and agent network map`
   - Working tree was clean and `HEAD...origin/master` was 0/0 after push.

## Current Git State

- Clean and synced to origin at closeout start.
- Latest pushed work is system/doc cleanup only; no agent domain files were moved.
- Continue pathspec-only commits; avoid broad add/reset/stash.

## Current Operating Picture

- **Market regime:** unchanged from `HEARTBEAT.md`: signed-but-fraying MOU, Hormuz re-closure declared, contested/not kinetic, energy tail re-fat, broad cascade unconfirmed.
- **Market data:** not refreshed in this session. Use `HEARTBEAT.md` as current orientation until next live dashboard/FRED refresh.
- **Near market gates:** Jun22 Brent reopen/tape response; next HY print vs <260 kill line; SAM/CFTC carry read; Jun24 EIA/Cushing <20M risk.
- **System lane:** AGENTS navigation and topology are now cleaner: `_INDEX.md` for grouped directory view, `_NETWORK.md` for topology, `dashboard/index.html` for the visual rendering.
- **Standalone dashboard network:** `dashboard/network.html` is now a pointer, not a separate live topology.
- **PROME docs:** live Prome docs no longer point at retired `PROME/TOSCANINI/` paths.

## Next Reboot Entry Point

1. Run repo-state first; expected clean/synced after this closeout push.
2. Read `HEARTBEAT.md` for market regime; do not infer fresh levels from this session.
3. If market lane: refresh dashboard/FRED HY and watch Jun22 Brent response / HY <260 / CFTC carry / bank-PC offset.
4. If system/docs lane: use `AGENTS/_INDEX.md` for grouped browsing and `AGENTS/_NETWORK.md` for topology.
5. If dashboard lane: use main dashboard Network tab; standalone `dashboard/network.html` intentionally redirects/pointers.
6. If closeout continuation: verify no uncommitted closeout docs remain, then commit/push with explicit pathspecs.

## Cautions

- Do not physically move agent directories without a dedicated migration script + grep/replace + tests.
- Do not maintain separate live network maps; canonical topology is `AGENTS/_NETWORK.md`, dashboard is rendering only.
- Do not edit WALTER specs/state from Prome unless Will explicitly scopes it.
- Do not treat Hormuz re-closure as kinetic until behavior confirms: vessel hit/seized/mined, Gulf infra hit, JWC/insurer withdrawal, or hard Brent/vol repricing.
- No trade execution or old option/expiry cleanup without broker/Will reconciliation.
