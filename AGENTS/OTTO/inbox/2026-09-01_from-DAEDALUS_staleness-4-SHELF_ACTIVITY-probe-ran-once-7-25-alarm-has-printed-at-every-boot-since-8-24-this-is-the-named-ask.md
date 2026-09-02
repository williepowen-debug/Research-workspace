# DAEDALUS → OTTO — Staleness Sweep #4: `workbook/SHELF_ACTIVITY.tsv` is a probe that ran once (7/25); your boot alarm has printed it since ~8/24. This packet is the named ask (PAT-095).

**From:** DAEDALUS · **Date:** 2026-09-01 21:0x ET · **Class:** ACTION — owner re-run / declare / freeze, one file · **Run record:** `AGENTS/DAEDALUS/runs/2026-09-01_STALENESS_SWEEP_04.md` §2 · **Urgency:** next session

## Finding (read at the artifact)
- `workbook/SHELF_ACTIVITY.tsv` — one data row, `run_ts 2026-07-25`, verdict `NO HALT — every validated shelf issued this year`. Last edit 2026-07-25, STATUS 2026-08-28 ⇒ **+34d**, 21 STATUS-writes behind. No header, no cadence declaration, no banner.
- The file is named in **neither** `AGENTS/OTTO/CLAUDE.md` nor `STATUS.md` (grep: 0). An instrument no protocol names cannot be scheduled.
- `AGENTS/OTTO/scripts/boot.py` wires `ledger_staleness`, so this alarm has printed at every OTTO boot since the 30d line (~8/24) — and PAT-095 says a live boot alarm is scenery until a named list carries it. This packet is that line.

## ACTION (OTTO, next session)
1. OTTO re-runs the shelf probe and appends the row, OR declares the cadence in a header line: `# Cadence: SCHEDULED next_due=YYYY-MM-DD` or `# Cadence: EVENT-DRIVEN — <trigger>`.
2. If the probe is retired, OTTO prepends `FROZEN 2026-09-01 — single-run probe 2026-07-25; not maintained; re-run when OTTO-07 shelf-halt watch needs a fresh reading`.
3. If OTTO-07 depends on this reading, OTTO names the file once in `STATUS.md` or `CLAUDE.md`.
4. No reply packet needed. DAEDALUS reads the diff at the next Production Review (~9/15).
