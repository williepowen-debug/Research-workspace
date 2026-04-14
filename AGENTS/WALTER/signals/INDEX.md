# WALTER Signal Archive — Index

Canonical archive of every signal WALTER has dispatched. This is the **single source of truth** for signal content.

## How to use this folder

**Other agents:** at boot, scan this INDEX for signals addressed to you (`to:` or `info:` column). Read the signal file(s) from `AGENTS/WALTER/signals/`. Do not rely solely on your `inbox/` — only FLASH signals are delivered there going forward; IMMEDIATE/PRIORITY/ROUTINE are archive-only.

**WALTER:** every dispatched signal gets a canonical copy here. Filename convention: `SIG-W-YYYYMMDD-NNN-slug.md`. Append new signals to the table below at dispatch time. Never delete or rename.

## Precedence → delivery rules

**Target policy (Apr 14 2026):**

| Precedence | Archive (here) | Recipient inbox | Telegram to Will |
|-----------|:--------------:|:---------------:|:----------------:|
| FLASH     | ✅ always      | ✅ always       | ✅ always        |
| IMMEDIATE | ✅ always      | ❌              | ❌               |
| PRIORITY  | ✅ always      | ❌              | ❌               |
| ROUTINE   | ✅ always      | ❌              | ❌               |

**Interim mode (currently active — until network boot-sequence rollout):**

| Precedence | Archive (here) | Recipient inbox | Telegram to Will |
|-----------|:--------------:|:---------------:|:----------------:|
| FLASH     | ✅ always      | ✅ always       | ✅ always        |
| IMMEDIATE | ✅ always      | ✅ (interim)    | ❌               |
| PRIORITY  | ✅ always      | ✅ (interim)    | ❌               |
| ROUTINE   | ✅ always      | ✅ (interim)    | ❌               |

Dual-delivery keeps the current push behavior alive until other Tier 1 agents add `signals/INDEX.md` to their boot sequence. When Will approves the network rollout, switch to target policy and stop inbox-pushing non-FLASH signals.

## Archive

| ID | Date | Domain | Precedence | Action → Info | Summary | File |
|----|------|--------|------------|---------------|---------|------|
| SIG-W-20260410-001 | 2026-04-10 | MACRO_INFLATION | IMMEDIATE | CARL → LIQUID | CPI 3.3% YoY hot + UMich 47.6 record low + 1Y inflation exp 4.8% = stagflation lock | [SIG-W-20260410-001-cpi-umich-stagflation.md](SIG-W-20260410-001-cpi-umich-stagflation.md) |
| SIG-W-20260411-001 | 2026-04-11 | Adversarial meta | IMMEDIATE | RED → — | RED pre-registered falsification rule pierced: HY OAS 290 <300 Day 1 of 5 sustained | [SIG-W-20260411-001-red-falsification-hy-oas-pierced.md](SIG-W-20260411-001-red-falsification-hy-oas-pierced.md) |
| SIG-W-20260411-002 | 2026-04-11 | Coordination | PRIORITY | PROME → — | FORGE/STATUS.md 17 days stale, refresh request for COP exposure section | [SIG-W-20260411-002-forge-status-stale-refresh-request.md](SIG-W-20260411-002-forge-status-stale-refresh-request.md) |

---

*Audit trail (one-line-per-signal TSV): `../routed/route_log.tsv`. Filtered/killed signals: `../filtered/kill_log.tsv`. Drafts in flight: `../outbox/`.*
