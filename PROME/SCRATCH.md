# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-06-25 ~12:20 ET (Claude Code Prome — Desktop CC origin; do-now batch + full write-back)

## Session Context
- Operating from **Desktop Claude Code**, not OpenClaw — **Codex/OpenClaw API degraded.** Prome is the live surface this session.
- Will authorized **teammate-mode agent spawns** this session (confirmed no other agents running). **SAM + BROCK** spawned persistent (still warm/idle); HENRY one-off.

## What Just Happened
- **Boot + live-data refresh:** tree clean, synced at `3d6091a7`. Refreshed dashboard (markets open) — the 6/21 HEARTBEAT/TODAY are now **regime-stale** (see delta below).
- **Do-now batch (report-only sub-agents):** SAM (FXY position truth-up), BROCK (APO put confirm + PC read), HENRY (May PCE ingest). Follow-ups **B1** (BROCK credit-recognition discriminator), **S1** (SAM MOF intervention playbook), **X1** (independent shared-antecedent test, both agents).
- **Full write-back (Will-approved), sequenced, committed LOCAL (unpushed):**
  - **BROCK `e11daae4`** — `domain/sources/MACRO_VS_CREDIT_DISCRIMINATOR_JUN25.md` (B1 watch-set + APO live mark + X1) + SCRATCH/STATUS pointers.
  - **SAM `8e6f4350`** — `MOF_INTERVENTION_PLAYBOOK.md` (S1 + X1) + STATUS note (FXY PENDING broker recon).
  - **HENRY — DECLINED** the relayed write-approval (principled: coordinator relay ≠ direct Will consent; commit is ask-first). No HENRY-domain commit; **its PCE read is captured in `PROME/synthesis/2026-06-25_donow_reconciliation.md`** — nothing lost.
  - **Prome** — `synthesis/2026-06-25_donow_reconciliation.md` + this SCRATCH + HANDOFF.

## Regime Delta vs 6/21 HEARTBEAT (live tape ~11:09 ET)
- **Energy tail DEFLATED:** Brent $74.24 (−8%, Jun-20 Hormuz declaration → non-kinetic; HAW-11 expired unfired).
- **HY OAS 271 [6/23]** — back ABOVE the <260 kill (kill-the-bear scare off; modestly bear-supportive). 6/24 print pending.
- **Bank-vs-PC divergence but MACRO not credit:** managers (APO/ARES/BX) −11/−13% cumulative while wrappers (ARCC/FSK/OBDC/BIZD) flat, KRE rallied. Today = pause, not acceleration.
- **Cushing sub-20M → BRENT Boundary #3 fired** (EIA 6/24).
- **May PCE firm (core 3.4%) but as-priced** — backward-looking; real disinflation test = June CPI Jul 14.

## ★ Crown-jewel synthesis (X1 reconciliation) — see synthesis doc
SAM + BROCK independently converged: **carry-unwind risk and PC-manager compression are ~1 root on macro/risk-off days — DON'T double-count as two bear confirmations.** The ONE trigger that makes PC a genuine independent confirmation = **wrapper basket LEADS managers down + HY OAS >280 sustained** (≡ BROCK's "now it's credit" trigger ≡ the decoupling marker). Today reads MACRO; discount PC+carry co-move ~50%. → Feed NEXUS (it double-counts otherwise). **HY>280 is LIQUID's half — motivates LIQUID reactivation.**

## Current Git State
- Local **ahead of origin by 3** (`e11daae4` BROCK, `8e6f4350` SAM, + this Prome commit) on top of origin `3d6091a7`. **All unpushed — defer to Will-coordinated push window.**
- Working tree clean post-commits. Each agent committed own-dir only, pathspec-scoped.

## Open Follow-ups
1. **FXY broker truth (Will):** did 13→6 trim fill 6/23? fill price + remaining count? live stop order at what FXY level (or mental)? → relay to warm **SAM** to finalize hold-vs-trim. Near-zone hard stop is a whipsaw trap (S1).
2. **LIQUID reactivation (Will-decision):** now well-motivated — HY>280 is half the live bear-root trigger.
3. **Regime-surface refresh PENDING:** HEARTBEAT + TODAY + NEXUS still on 6/21 "energy re-fat / HY-near-kill-from-below" read — now wrong. Refresh once, Prome-owned.
4. **HENRY domain update** pending direct-Will-confirm (or next HENRY real session) — read preserved in synthesis doc.
5. **Auto-memory finding** (don't-double-count rule, ratified by independent convergence) worth capturing — but **MEMORY.md over-limit (26.7KB vs 24.4KB); prune first** (see `MEMORY_PRUNE_PLAN_2026-06-14.md`).

## Warm Agents
- **SAM** + **BROCK** still alive (idle/available) for follow-ups (e.g. B2 late-July Q2 BDC catalyst map). Release at closeout if unused.

## Cautions
- **No push without Will's explicit coordination.**
- Position truth (FXY fill, APO basis) = **broker/Will**, not these files.
- HEARTBEAT levels are 6/21 Fri-close-stale; refresh dashboard/FRED before citing as current.
- `git add` only specific own-dir paths; never broad-add.
