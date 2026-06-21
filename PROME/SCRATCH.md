# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-21 10:08 ET (OpenClaw Prome — pre-clear hygiene after AGENTS/PROME organization pass)

## What Just Happened

- AGENTS organization pass is complete and pushed: grouped directory views live under `AGENTS/_INDEX.md` + group files; canonical agent folders remain flat as `AGENTS/<NAME>/`.
- PROME path cleanup is complete and pushed: live Prome docs no longer point at retired Toscanini paths; moved inbox/outbox refs were fixed where canonical targets existed.
- Canonical topology is now `AGENTS/_NETWORK.md`; main dashboard Network tab mirrors it; standalone `dashboard/network.html` is a pointer/redirect.
- Post-closeout hygiene landed locally/pushed sequence-ready: `PROME/BOOT.md` now has weekend/market-holiday freshness rules; `HEARTBEAT.md` labels Fri-close levels as orientation-only; `PROME/HANDOFF.md` is tightened to 3 live entries; `PROME/STATUS.md` refreshed after hygiene pass.

## Current Git State

- Expected boot state after final push: clean and synced to origin.
- Current work is Prome/system doc hygiene only; no agent domain folders were moved or edited.
- Continue pathspec-only commits; avoid broad add/reset/stash.

## Current Operating Picture

- **Market regime:** use `HEARTBEAT.md`: signed-but-fraying MOU, Hormuz re-closure declared, contested/not kinetic, energy tail re-fat, broad cascade unconfirmed.
- **Market data freshness:** Sunday/market-closed orientation only. Do not cite levels as fresh without dashboard/FRED refresh.
- **Near market gates:** Jun22 Brent reopen/tape response; next HY print vs <260 kill line; SAM/CFTC carry read; Jun24 EIA/Cushing <20M risk.
- **System lane:** use `AGENTS/_INDEX.md` for grouped browsing and `AGENTS/_NETWORK.md` for topology. Do not create a second live network map.
- **Decision rails:** `PROME/ACTIVE_DECISIONS.md` remains verification-first; no trade/expiry action without broker/Will truth.

## Next Reboot Entry Point

1. Run repo-state first; expected clean/synced after final hygiene push.
2. Read `PROME/HANDOFF.md`, `PROME/SCRATCH.md`, `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/STATUS.md` per `PROME/BOOT.md`.
3. If market lane: refresh dashboard/FRED before citing current levels; then watch Jun22 Brent/Hormuz + HY <260 + CFTC/carry.
4. If system/docs lane: use `AGENTS/_INDEX.md` and `AGENTS/_NETWORK.md`; avoid physical agent-folder moves.
5. If position lane: start with broker/Will reconciliation, not old action-card rails.

## Cautions

- Do not physically move agent directories without a dedicated migration script + grep/replace + tests.
- Do not maintain separate live network maps; canonical topology is `AGENTS/_NETWORK.md`, dashboard is rendering only.
- Do not edit WALTER specs/state from Prome unless Will explicitly scopes it.
- Do not treat Hormuz re-closure as kinetic until behavior confirms: vessel hit/seized/mined, Gulf infra hit, JWC/insurer withdrawal, or hard Brent/vol repricing.
- No trade execution or old option/expiry cleanup without broker/Will reconciliation.
