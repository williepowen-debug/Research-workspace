# LIQUID Credit-Detection Pipeline Audit — 280/260 Trigger
**2026-06-26 · PROPOSE-ONLY · scope: credit-detection pipeline (HY OAS 280/260)**

## WHERE
The 280/260 logic lives in **ONE place: `AGENTS/LIQUID/scripts/boot.py:86–98`** (`build_credit()`). Full ladder, correct: `<260` KILL, `<265` TRIGGER-A, `<270` PRE-TRIGGER, `>320` confirm, `>300` approaching, `>280` X1 DECOUPLING, else green-with-cushion.

The shared **`config.py:36–38` does NOT watch 280/260** — HY OAS is green `<300` / yellow `300–320` / red `320+`, hysteresis 5. So `dashboard.py` (the only cron-shaped tool, consumes `config.classify`) marks **281 = GREEN and 261 = GREEN** — both silent. (config.py:100–101's "280000" is Init Claims, unrelated.)

## AUTO?
**No. Nothing fires automatically.** Verified:
- `crontab -l` → "no crontab for willi" — **empty**. No scheduler runs either tool.
- No `dashboard.service` (`systemctl --user status dashboard` → not found).
- `cron_dashboard.sh` / `morning_briefing.sh` both hard-coded to the dead VPS path `/home/moltbot/.openclaw/...`; `morning_briefing.sh` also `exit 0`-disabled (4/15).
- `dashboard.py` Telegram is dead: `notify_transitions()` returns at line 409; send commented at 425 (4/15).

**If HY prints 281 on a Tuesday and nobody boots LIQUID, NOTHING catches it.** boot.py is manual-only + stdout-only.

## BREAKS (where a 280 cross goes unseen)
1. **No scheduler** — neither tool runs between manual boots; the FRED pull never happens unattended.
2. **Wrong thresholds in the cron-shaped tool** — even if `dashboard.py` cron were restored, `config.py` green-`<300` marks 281 GREEN. Silent by design.
3. **boot.py manual + stdout-only** — correct ladder, but no scheduler invokes it and no push leaves the terminal.
4. **Telegram dead** — both notify paths disabled since 4/15; no alert reaches Will even if generated.
5. **boot.py exit code = fetch-health only** (line 24–25) — a wrapper checking `$?` sees 0 on a 281 cross.
6. **FRED T+1 + weekend lag** — a Friday-close cross isn't visible until Mon/Tue.

## FIX (minimal — no logic change needed)
The detection logic already exists and is correct (boot.py). The gap is **scheduling + push only**:
- **Cron `boot.py --quick`** (FRED-only, fast) weekday ~9:15am ET; a 3-line wrapper greps stdout for the HY OAS 🟠/🔴 line and pushes to Telegram on match. Re-point the `/home/moltbot` path to `/home/willi`; parse stdout, **not `$?`**.
- **Secondary (route to config owner, NOT me):** align `config.py` HY OAS to 280/260 so `dashboard.py` stops masking — flag to SENTRY (owns whole-config).

Guarantees catch without editing config.py or boot.py logic.
