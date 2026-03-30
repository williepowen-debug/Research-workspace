#!/bin/bash
# PROME Dashboard Cron Wrapper
# Handles schedule logic: 15min market hours, 60min off-hours, 4hr weekends
#
# Install: crontab -e → add:
#   */5 * * * * /home/moltbot/.openclaw/workspace/FORGE/tools/market-data/cron_dashboard.sh
#
# The script self-throttles based on time — safe to run every 5 min from cron.

DIR="$(cd "$(dirname "$0")" && pwd)"
LOCK_FILE="$DIR/.cache/cron.lock"
LAST_RUN_FILE="$DIR/.cache/cron_last_run"

mkdir -p "$DIR/.cache"

# Prevent overlapping runs
if [ -f "$LOCK_FILE" ]; then
    pid=$(cat "$LOCK_FILE" 2>/dev/null)
    if kill -0 "$pid" 2>/dev/null; then
        exit 0
    fi
    rm -f "$LOCK_FILE"
fi
echo $$ > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

# Get current ET hour and day
ET_HOUR=$(TZ="America/New_York" date +%H | sed 's/^0//')
ET_DOW=$(TZ="America/New_York" date +%u)  # 1=Mon, 7=Sun
ET_MIN=$(TZ="America/New_York" date +%M | sed 's/^0//')
NOW=$(date +%s)

# Determine interval (seconds)
if [ "$ET_DOW" -ge 6 ]; then
    # Weekend: every 4 hours
    INTERVAL=14400
elif [ "$ET_HOUR" -ge 9 ] && [ "$ET_HOUR" -lt 16 ]; then
    # Market hours (rough): every 15 min
    INTERVAL=900
elif [ "$ET_HOUR" -eq 9 ] && [ "$ET_MIN" -ge 30 ]; then
    INTERVAL=900
else
    # Off-hours weekday: every 60 min
    INTERVAL=3600
fi

# Check if enough time has passed since last run
if [ -f "$LAST_RUN_FILE" ]; then
    LAST_RUN=$(cat "$LAST_RUN_FILE")
    ELAPSED=$((NOW - LAST_RUN))
    if [ "$ELAPSED" -lt "$INTERVAL" ]; then
        exit 0
    fi
fi

# Run the dashboard
echo "$NOW" > "$LAST_RUN_FILE"
cd "$DIR"
python3 dashboard.py --cron 2>>"$DIR/.cache/cron_errors.log"
