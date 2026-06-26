# SENTRY Audit — Detection Config vs Thesis Triggers + Automation
**2026-06-26 · PROPOSE-ONLY (read-only; no edits/commits) · Prome sub-role**
Scope: whole-config correctness + automation coverage. (LIQUID owns credit-alert pipeline deep-dive.)

## DRIFTS (config.py SERIES vs live thesis triggers — HEARTBEAT 6/25)

| Series | Config band | Thesis line | Verdict |
|---|---|---|---|
| **HY OAS** | green<300 / yel 300-320 / red 320+ | **>280 X1 master (red); <260 two-closes = bear-axis kill** | 🔴 **STALE.** classify(276)→GREEN; HEARTBEAT manually shows 276🟡. Red line 320 is 40bp above the actual trigger. Kill-line (<260) not representable (single-sided higher_worse). Bands are Mar-28-era. |
| **10Y** | green<4.00 / yel 4.00-4.50 / red 4.50+ | **>4.40 sustained = AOCI path-(b) confirm** | 🟠 **DRIFT.** classify(4.39)→yellow; HEARTBEAT manually 🔴. Red 4.50 is 10bp past the AOCI line. |
| **KRE** | grn 68+ / yel 63-68 / red <63 | live ~74.6 (regime ~75) | 🟡 Bands stale-low; KRE sits deep-green, alert range never re-centered to current trading regime. |
| **WAL** | grn 78+ / yel 65-78 / red <65 | live ~81.4; **path-(c) live single-name exception** | 🟡 Stale-low + wide; the one Q2-able name has no thesis-tuned line. |
| **OZK** | grn 50+ / yel 40-50 / red <40 | live ~51.9 | 🟡 50-line ≈ current; red <40 far below. Re-center. |
| **CCC OAS** | 900/1000 (964→yel) | dispersion tell (CCC ~2× HY) | ⚪ Absolute band ~ok; the **CCC–HY/BB tail-gap (~798)** discriminator has no series. |
| **FXY** | tier-2 active | **position CLOSED by Will 6/25** | 🟡 Residual; demote to regime-only note. |

## MISSING TRIGGERS (no series at all)
- **Wrapper-decoupling composite** — ARCC/FSK/OBDC (+BIZD) basket *leading APO/ARES down* = BROCK's half of the X1 bear-root. **Zero coverage**: no ARCC/FSK/OBDC tickers, no basket, no relative-lead logic. The single biggest hole.
- HY **>280 / <260** trigger lines un-encoded. 10Y **>4.40**. CCC–HY **dispersion gap**.

## AUTOMATION — ZERO unattended detection between sessions
- `crontab -l` → **no crontab for willi.** No systemd `--user` timer; `dashboard.service` **not found**. cron_dashboard.sh / morning_briefing.sh hardcode the **defunct VPS path** `/home/moltbot/.openclaw/...` and nothing schedules them.
- `.cache/cron_last_run` = **Apr 10 16:00** — cron hasn't fired in 2.5 months.
- `morning_briefing.sh` hard-disabled (`exit 0`). `dashboard.py notify_transitions()` **returns immediately** (line 409) — Telegram alerting fully off since 4/15.
- dashboard.py is **human-pull, display-only**: market_data.log touched today = a manual agent run. Even on-demand runs raise **no alert** on a new-red transition. → Between sessions, nothing watches the tape and nothing pings Will.

## GAP LIST
**(a) Stale thresholds:** HY 280/260, 10Y 4.40, KRE/WAL/OZK bands not re-centered, FXY residual.
**(b) Missing triggers:** wrapper-decoupling basket (ARCC/FSK/OBDC + lead logic); CCC–HY dispersion; explicit HY/10Y trigger lines.
**(c) Automation holes:** no scheduler on this host; alert code disabled; paths point at dead VPS.

## FIX (minimal)
1. **HY OAS** → green(None,265)/yellow(265,280)/red(280,None), hyst 5; note "<260 two-closes = bear-axis kill". (276→🟡, ≥280→🔴 matches HEARTBEAT.)
2. **10Y** → yellow(4.00,4.40)/red(4.40,None).
3. Re-center **KRE/WAL/OZK** yellow/red toward current put-relevant levels; demote **FXY** to regime-note.
4. **Add ARCC/FSK/OBDC** as tier-1 series so the wrapper basket is visible (relative-lead alert = LIQUID/BROCK logic, flag to them).
5. **Automation:** install one `systemd --user` timer (or crontab) → local `cron_dashboard.sh`; if Will wants between-session alerts, re-enable `send_telegram` for **new-red Tier-1 only** (exit-2 path) to cap cost.
All Will-gated; no edits made.
