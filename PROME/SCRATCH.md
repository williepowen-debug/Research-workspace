# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-20 14:59 ET (OpenClaw Prome — closeout after CORAL inbox + thesis rails install)

## What Just Happened

1. **CORAL boot hardening landed and pushed.**
   - Added `AGENTS/CORAL/scripts/boot.py` as a read-only situational card: continuity/staleness, WALTER/mail state, FL bank/regional prices, cross-agent snippets, active calendar gates.
   - Updated `AGENTS/CORAL/CLAUDE.md` to run the boot card while preserving full manual boot reads.
   - Fixed `SCRATCH.md` pending WALTER count from 2 → 3 after `SIG-W-20260619-008` arrived.

2. **CORAL processed all pending WALTER signals correctly.**
   - Consumed `SIG-W-20260619-002`, `SIG-W-20260619-007`, and `SIG-W-20260619-008` through `board_log.tsv` and `git mv` to `inbox/WALTER/processed/`.
   - Integrated negative equity, bankruptcy acceleration, and the insurance split into `STATUS.md`, `SCRATCH.md`, `NEXUS_BRIEF.md`, `MEMORY.md`, `FL_BANK_WATCHLIST.md`, and workbook ledgers (`KB.tsv`, `VX_Vectors.md`, `FLOW_Pathways.md`).
   - Key result: WALTER inbox now 0 pending; legacy BayFirst REGINALD item remains out of scope.

3. **CORAL thesis rails were drafted, reviewed, tightened, installed, and pushed.**
   - Draft v1 and v2 proposal files were created under `AGENTS/CORAL/proposals/`.
   - Prome installed v2 with two tightenings: USCB trigger requires **explicit condo-association loan deterioration**; association bankruptcy/receivership clusters are bridge/corroborating evidence, not bank deterioration by themselves.
   - Installed `AGENTS/CORAL/thesis/THESIS.md` + `AGENTS/CORAL/thesis/CHANGELOG.md` and updated `CLAUDE.md`, `STATUS.md`, `NEXUS_BRIEF.md`, `SCRATCH.md`, `MEMORY.md`, and `scripts/boot.py` pointers.

4. **Repo is clean and synced to GitHub.**
   - All today’s Prome/CORAL work was committed and pushed through origin.
   - Current head at closeout: `CORAL: install thesis rails`; working tree clean.

## Current Git State

- Clean and synced to origin as of closeout.
- No local-only Prome/CORAL commits are pending.
- Continue pathspec-only commits; avoid broad add/reset/stash.

## Current Operating Picture

- **System lane:** CORAL is now operationally mature enough for normal use: boot card, WALTER board-log intake, processed inbox, NEXUS brief, thesis rails, changelog, and closeout/write-back procedure are all on origin.
- **CORAL thesis:** v1.0 installed. Durable rule: household/condo stress is confirmed, but bank-loss transmission upgrades only on bank evidence — synchronized deterioration across ≥2 FL-exposed banks or explicit USCB condo-association loan deterioration with corroborating consumer/collateral data.
- **Market lane:** HEARTBEAT remains the current regime source: Geneva de-escalation branch fired, immediate energy shock deferred, HY <260 kill still unconfirmed, banks/VIX calm, carry red.
- **Positions:** no position/expiry action without broker/Will truth.

## Next Reboot Entry Point

1. Run repo-state first; expected clean/synced.
2. If CORAL lane: next useful work is the per-metro convergence grid (Miami/Tampa/Orlando/Jax/SW-FL) using the new negative-equity/bankruptcy/insurance vectors, or Q2 FL-bank earnings prep.
3. If market lane: refresh dashboard/FRED HY; key question remains whether HY sustains <260 or banks/PC re-weaken enough to offset.
4. If SAM lane: check Jun20 CFTC against SAM v1.6 carry-convexity survival gates.
5. If WALTER lane: monitor behavior / doctor output; Prome does not edit WALTER specs unless Will explicitly scopes it.

## Cautions

- CORAL thesis rails are installed; future CORAL should keep live metric values in STATUS/workbooks, not THESIS.
- Do not upgrade CORAL bank-transmission on collateral/household stress alone; require the installed bank-upgrade rail.
- Do not edit WALTER specs from Prome; WALTER owns future tuning.
- No trade execution or old option/expiry cleanup without broker/Will reconciliation.
