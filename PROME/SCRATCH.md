# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-21 19:40 ET (OpenClaw Prome — post REITS/TRADES archive + ORACLE/TERRY tooling push)

## What Just Happened

- Repo was safely rebased over newer WALTER/SAM remote commits and pushed cleanly.
- Landed pushed commits:
  - `9cf41161 CREED: absorb REIT equity tape`
  - `cdd6ce96 TERRY: archive legacy TRADES playbook`
  - `6219553f TERRY: add risk scoring module`
  - `0ad1def6 ORACLE: add prediction market metrics`
- REITS is now archived/dormant; live public REIT equity-market tape belongs to CREED.
- TRADES is now archived/dormant; useful legacy verification pattern belongs to TERRY.
- TERRY now has risk scoring/calibration tooling: pre-trade gates, edge scoring, fractional Kelly reference, Brier tracking, execution-block checklist, postmortem tags.
- ORACLE now has prediction-market metric tooling: entropy, KL bits, entropy-collapse alerts, liquidity/resolution discounts, ORACLE→TERRY handoff packet.
- Claude Code command reference was updated earlier and now excludes REITS/TRADES launch commands.

## Current Git State

- Expected after closeout write: local Prome closeout files may be ahead if committed but not pushed.
- Last verified pre-closeout: repo clean/synced with origin after pushing ORACLE/TERRY/CREED work.

## Current Ownership Truth

- **CREED** owns national CRE / CMBS **plus public REIT equity-market tape**.
- **REITS** folder remains source archive only; do not launch unless Will explicitly revives it.
- **TERRY** owns live trade construction and the old TRADES verification playbook.
- **TRADES** folder remains source archive only; do not launch unless Will explicitly revives it.
- **ORACLE** owns prediction-market diagnostics; TERRY owns tradeability; Will approves any action.
- No auto-trading.

## Next Reboot Entry Point

1. Verify repo state first.
2. Read this file plus `PROME/HANDOFF.md`, `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/STATUS.md`.
3. If continuing system cleanup, next candidates are other dormant folders in `AGENTS_DIRECTORY.md` / `_INDEX.md` only after inspecting actual value.
4. If market lane, refresh dashboard/FRED before citing current levels; `HEARTBEAT.md` remains Fri-close/weekend orientation until refreshed.

## Cautions

- No trade execution; TERRY proposals still require Will approval.
- No auto-trading for ORACLE/prediction markets.
- No REITS/TRADES launch from command reference; they are archived.
- `AGENTS/REGINALD/sub-agents/CREED/` remains legacy source archive only.
- Continue pathspec-only commits; no broad add/reset/stash.
