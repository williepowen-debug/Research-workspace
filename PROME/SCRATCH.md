# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-25 ~13:05 ET (Claude Code Prome — Desktop CC origin; do-now batch + write-back + regime refresh + agent closeout COMPLETE)

## Session Context
- Operated from **Desktop Claude Code**, not OpenClaw — **Codex/OpenClaw API degraded.** Prome was the live surface.
- Will authorized teammate-mode spawns. SAM, BROCK, LIQUID spawned (report-only → closed out → **released/shut down at session end**). HENRY one-off.

## What Happened (full session)
- **Boot + live-data refresh:** tree clean, synced at `3d6091a7`. The 6/21 HEARTBEAT/TODAY were regime-stale; refreshed off the live tape.
- **Do-now batch (report-only):** SAM (FXY position), BROCK (APO put + PC read), HENRY (May PCE). Follow-ups B1/S1/X1.
- **Full write-back → regime refresh → targeted intel pulls → agent closeout batch** — all committed LOCAL, unpushed (8-commit ledger below).
- **HENRY declined** the relayed write-approval (principled: coordinator relay ≠ direct Will consent); its PCE read lives in the synthesis doc.

## Regime Read (current) — see `synthesis/2026-06-25_donow_reconciliation.md` + HEARTBEAT
- Energy tail **DEFLATED** (Brent $74, Hormuz non-kinetic; Cushing sub-20M → BRENT Boundary #3).
- Credit-bear **PAUSED** above the <260 kill (HY 271, cushion 11bp; LIQUID: kill dead, bear not).
- Bank-vs-PC divergence = **MACRO multiple-compression, NOT credit-substance** (wrappers flat, banks rallied). Fresh: Apollo gated ADS at 5% (6/23) — flow not mark.
- **★ X1 rule (SAM+BROCK+LIQUID, independent):** carry-unwind + PC-compression = ~1 root on macro days — DON'T double-count. Independent PC confirmation gated on **wrapper-leading + HY OAS >280** (both UNFIRED → root single/macro).
- May PCE firm-but-as-priced; real disinflation test = June CPI 7/14.

## Git State (CLOSEOUT)
- **8 commits ahead of origin `3d6091a7`, ALL UNPUSHED** (defer to Will push window). Tree clean.
  - `e11daae4` BROCK discriminator+APO+X1 · `8e6f4350` SAM MOF playbook+X1 · `3c03818d` PROME synthesis+SCRATCH/HANDOFF · `85395063` PROME HEARTBEAT/TODAY refresh · `4f4448c6` PROME HEARTBEAT intel fix · `5a4569b8` BROCK Q2 catalyst map+ADS · `df1adae5` SAM live-placement log · `9bdf0b10` LIQUID PAUSED verdict+KB-LIQ-062.
  - (+ this SCRATCH/HANDOFF closeout commit.)

## Open Follow-ups (next session)
1. **FXY broker truth (Will):** did 13→6 trim fill 6/23? price + count? live stop level/mental? Hold-if-filled / trim-if-not (binding stop USD/JPY 162.5; near-zone hard stop = whipsaw trap). SAM released — respawn or handle next session.
2. **Coordinated PUSH** of the 8 local commits when Will opens a window.
3. **CFTC COT Fri 6/26** (data as of 6/23, NOT Jun-16) — read framework in `AGENTS/SAM/MOF_INTERVENTION_PLAYBOOK.md` (vs −150,132 baseline).
4. **NEXUS refresh** deferred (Will hold) — needs the X1 don't-double-count rule (it double-counts otherwise) + the regime delta.
5. **HENRY domain update** pending direct-Will-confirm — read preserved in synthesis doc.
6. **Auto-memory finding** (X1 don't-double-count rule) worth capturing — MEMORY.md over-limit (26.7KB vs 24.4KB); prune first (`MEMORY_PRUNE_PLAN_2026-06-14.md`). LIQUID already logged KB-LIQ-062 in its own KB.
7. **Live bear-root watch:** wrapper-leading + HY>280 (both unfired). Catalysts: ARCC Q2 7/28, NFP 7/3, CPI 7/14, Q2 BDC marks ~7/25.

## Agents
- SAM, BROCK, LIQUID **released (shut down)** at session end after closeout. Respawn as needed next session.

## Cautions
- **No push without Will's explicit coordination.**
- Position truth (FXY fill, APO basis) = **broker/Will**, not these files.
- HEARTBEAT is now current (6/25) but refresh dashboard/FRED before re-citing levels as live.
- `git add` only specific own-dir paths; never broad-add.
