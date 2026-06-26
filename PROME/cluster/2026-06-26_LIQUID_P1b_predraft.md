# P1b — Local HY OAS Scheduler + Alert Wrapper (LIQUID)  ✅ BUILT & ENABLED
**2026-06-26 · DELIVERED. Timer enabled+active, next fire Mon–Fri 13:00 ET.**

## AS-BUILT (deviations from the pre-draft below — go-signal answers applied)
- **Source of truth = config.py (NOT boot.py).** Watcher is `AGENTS/LIQUID/scripts/hy_oas_watch.py` (Python, not bash) and `import`s `config.classify` + the HY OAS series def → auto-inherits SENTRY's retuned bands (🟢<265 / 🟡265-280 / 🔴>280) and any future retune, no copy.
- **Covers BOTH triggers:** zone escalation into 🟡/🔴 (no hysteresis up = earliest catch) AND the `kill_below=260` two-way bear-axis kill on **2 consecutive closes** (date-aware via `obs_date`, so a weekend doesn't double-count one print).
- **boot.py reconciled** to the same config.py bands (stale 270-280/320 ladder removed) + 1-line next-boot echo of `HY_OAS_STATE`. Selftest PASS.
- **Verified:** live run 278bps → 🟡, fired amber transition; 2nd run idempotent (no spam); systemd service run `Result=success`; timer `enabled`+`active`.
- Alert surface = file-only as agreed (no libnotify/sudo). `alerts/*.log` + `HY_OAS_STATE` are runtime state — recommend NOT committing (suggest `AGENTS/LIQUID/alerts/` in .gitignore; flagging, not doing).

---
# Pre-Draft (historical — superseded by AS-BUILT above)
**read-only pre-draft, nothing installed/enabled**

Goal: guarantee an HY OAS 280 (X1) / 260 (kill) cross is caught and surfaced **on this local host** without a human booting LIQUID — no dead VPS path, no Telegram.

## Host facts (verified live, 6/26)
- `systemd --user` is **running**, **Linger=yes** → user timers fire even when Will is logged out. ✅ (this is what makes unattended daily checks viable)
- User unit dir exists: `~/.config/systemd/user/` (outside the git repo — not a commit concern).
- `.venv/bin/python3` works for FRED; `requests 2.33.1` present → `boot.py --quick` (FRED-only, no yfinance) runs clean in ~4s, 0 fetch errors.
- TZ = America/New_York (EDT) → `OnCalendar` times are local ET, no conversion needed.
- `notify-send` is **NOT installed** (no `/usr/bin/notify-send`); `DISPLAY=:0` + Wayland present. Desktop-popup alerting is therefore an *optional* enhancement requiring a one-time `sudo apt install libnotify-bin` (needs Will) — NOT in the baseline.

## Live stdout format the wrapper parses (captured 6/26)
HY OAS row (collapsed view always shows it — it's `headline=True`):
```
    🟢 HY OAS       278bps               cushion 18bps to 260 kill / 2bps to 280 X1-trigger / 42bps to 320 confirm
```
boot.py HY OAS ladder (scripts/boot.py:91–97, if/elif order):
`<260`🔴KILL · `<265`🟠TRIGGER-A · `<270`🟡PRE-TRIG · `>320`🔴CONFIRM · `>300`🟠 · `>280`🟠X1 · else(270–280)🟢.
⚠️ At 278 the marker is 🟢 — so **a value-only grep is not enough; we key on the marker emoji + a persisted prior state to detect the *transition*.** Severity map (boot.py SEV): 🟢0 🟡1 🟠2 🔴3.

## Alert surface design (baseline = durable local files; no network)
1. **Append-only alert log** → `AGENTS/LIQUID/alerts/HY_OAS_ALERTS.log` (my dir; durable, greppable, survives reboot).
2. **Next-boot surface** → `AGENTS/LIQUID/alerts/HY_OAS_STATE` (last marker+bps+date). boot.py can read this next session to echo "since-last-session cross" (belt + suspenders; a 1-line boot.py addition I'll propose separately, NOT in P1b).
3. **Run log** → `AGENTS/LIQUID/alerts/watch.log` (every run, 1 line — proves the timer is alive; lets us see silent failures).
4. *Optional later:* desktop `notify-send` once `libnotify-bin` is installed.

## ARTIFACT 1 — wrapper: `AGENTS/LIQUID/scripts/hy_oas_watch.sh`
Transition rule: fire when **SEV(now) ≥ 2 (🟠/🔴) AND SEV(now) > SEV(prev)** → catches fresh escalations and 🟠→🔴 deepening; suppresses re-fire while parked at same level (no spam). First-ever run while already ≥🟠 also fires (no prior state). Parse done in-python (emoji-safe) since we invoke python anyway.
```bash
#!/usr/bin/env bash
# LIQUID HY OAS watcher — runs boot.py --quick, alerts on transition into 🟠/🔴.
# Surfaces locally only (no Telegram / no VPS path). Owned by LIQUID.
set -uo pipefail
WS="/home/willi/Research-workspace"
PY="$WS/.venv/bin/python3"
BOOT="$WS/AGENTS/LIQUID/scripts/boot.py"
ALERTDIR="$WS/AGENTS/LIQUID/alerts"
STATE="$ALERTDIR/HY_OAS_STATE"
ALOG="$ALERTDIR/HY_OAS_ALERTS.log"
RLOG="$ALERTDIR/watch.log"
mkdir -p "$ALERTDIR"
TS="$(date '+%Y-%m-%d %H:%M %Z')"

OUT="$("$PY" "$BOOT" --quick 2>&1)"; RC=$?
# emoji-safe parse of the HY OAS row -> "MARKER\tBPS\tNOTE"
PARSED="$(printf '%s' "$OUT" | "$PY" - <<'PYEOF'
import sys,re
SEV={"🟢":0,"🟡":1,"🟠":2,"🔴":3}
for ln in sys.stdin:
    if "HY OAS" in ln and "bps" in ln:
        mk=next((c for c in ln if c in SEV),"")
        m=re.search(r"(\d+)bps",ln)
        if mk and m:
            note=ln.split("bps",1)[1].strip()
            print(f"{mk}\t{m.group(1)}\t{SEV[mk]}\t{note}"); break
PYEOF
)"

if [ -z "$PARSED" ]; then
  echo "$TS  PARSE-FAIL (rc=$RC) — HY OAS row not found" >>"$RLOG"
  exit 3
fi
MK="$(printf '%s' "$PARSED"|cut -f1)"; BPS="$(printf '%s' "$PARSED"|cut -f2)"
SEVNOW="$(printf '%s' "$PARSED"|cut -f3)"; NOTE="$(printf '%s' "$PARSED"|cut -f4)"
SEVPREV=0; [ -f "$STATE" ] && SEVPREV="$(cut -f3 "$STATE" 2>/dev/null || echo 0)"
echo "$TS  HY OAS ${BPS}bps ${MK} (sev $SEVNOW, prev $SEVPREV) rc=$RC" >>"$RLOG"

if [ "$SEVNOW" -ge 2 ] && [ "$SEVNOW" -gt "$SEVPREV" ]; then
  echo "$TS  🚨 HY OAS TRANSITION → ${MK} ${BPS}bps — ${NOTE}" >>"$ALOG"
  command -v notify-send >/dev/null && notify-send -u critical "HY OAS ${MK} ${BPS}bps" "$NOTE" || true
fi
printf '%s\t%s\t%s\t%s\n' "$MK" "$BPS" "$SEVNOW" "$TS" >"$STATE"
exit 0
```

## ARTIFACT 2 — `~/.config/systemd/user/liquid-hy-watch.service`
```ini
[Unit]
Description=LIQUID HY OAS credit-trigger watcher (280 X1 / 260 kill)
[Service]
Type=oneshot
ExecStart=/home/willi/Research-workspace/AGENTS/LIQUID/scripts/hy_oas_watch.sh
```

## ARTIFACT 3 — `~/.config/systemd/user/liquid-hy-watch.timer`
FRED ICE-BofA OAS publishes T+1, appearing late-morning/midday ET → schedule **midday weekdays**, `Persistent=true` so a missed run (laptop asleep) fires on next wake.
```ini
[Unit]
Description=Run LIQUID HY OAS watcher midday on weekdays
[Timer]
OnCalendar=Mon..Fri 13:00 America/New_York
Persistent=true
[Install]
WantedBy=timers.target
```
Enable (on go): `systemctl --user daemon-reload && systemctl --user enable --now liquid-hy-watch.timer`; verify `systemctl --user list-timers liquid-hy-watch.timer`; dry-run `systemctl --user start liquid-hy-watch.service && cat AGENTS/LIQUID/alerts/watch.log`.

## OPEN ITEMS for team-lead's go signal
1. **SENTRY's final config thresholds** — if P1a moves the boundaries off the boot.py ladder (280/260), I retune the wrapper's transition rule to match SENTRY's canonical zones so the two surfaces don't diverge again. My parse keys on boot.py's marker today; confirm boot.py stays the source of the *ladder* or tell me to mirror config.py.
2. **Schedule time** — 13:00 ET weekday is my pick for catching same-day FRED publish; confirm or override. (Could add a 2nd 09:15 run to catch prior-day late prints — say if you want belt+suspenders.)
3. **Alert surface** — baseline is local files only. Want me to also propose the one-time `libnotify-bin` install for a desktop popup, or keep it file-only?
4. **boot.py next-boot echo** — optional 1-line add so a between-session cross also shows at next manual LIQUID boot. Separate proposal; say if in-scope.
