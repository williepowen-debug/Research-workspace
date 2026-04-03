#!/bin/bash
# News Sweep Cron Wrapper
# Runs M-F at 8:30 AM ET only. Sweeps, routes to inboxes, sends Telegram summary.
#
# Crontab: 30 12 * * 1-5 /home/moltbot/.openclaw/workspace/FORGE/tools/news-sweep/cron_sweep.sh

DIR="$(cd "$(dirname "$0")" && pwd)"
LOCK_FILE="$DIR/.cache/cron.lock"
LOG_FILE="$DIR/.cache/cron.log"
TELEGRAM_BOT_TOKEN="***REMOVED***:***REMOVED***"
TELEGRAM_CHAT_ID="8463631023"

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

# Check day: M-F only (1-5)
ET_DOW=$(TZ="America/New_York" date +%u)
if [ "$ET_DOW" -gt 5 ]; then
    exit 0
fi

# Check time: 8:30 AM ET only (allow 8:25-8:35 window)
ET_HOUR=$(TZ="America/New_York" date +%H | sed 's/^0//')
ET_MIN=$(TZ="America/New_York" date +%M | sed 's/^0//')

if [ "$ET_HOUR" -ne 8 ]; then
    exit 0
fi
if [ "$ET_MIN" -lt 25 ] || [ "$ET_MIN" -gt 35 ]; then
    exit 0
fi

# Check if already ran today
TODAY=$(TZ="America/New_York" date +%Y-%m-%d)
LAST_DATE_FILE="$DIR/.cache/cron_last_date"
if [ -f "$LAST_DATE_FILE" ]; then
    LAST_DATE=$(cat "$LAST_DATE_FILE")
    if [ "$LAST_DATE" = "$TODAY" ]; then
        exit 0
    fi
fi

# Run the sweep
echo "$TODAY" > "$LAST_DATE_FILE"
echo "$(date): Running news sweep for $TODAY" >> "$LOG_FILE"

cd "$DIR"
SWEEP_OUTPUT=$(python3 sweep.py --compact --route 2>>"$LOG_FILE")
EXIT_CODE=$?

echo "$(date): Sweep completed with exit code $EXIT_CODE" >> "$LOG_FILE"

# Send Telegram notification
if [ $EXIT_CODE -eq 0 ] && [ -n "$SWEEP_OUTPUT" ]; then
    # Truncate to Telegram message limit (4096 chars)
    MSG=$(echo "$SWEEP_OUTPUT" | head -c 4000)
    curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
        -d chat_id="$TELEGRAM_CHAT_ID" \
        -d parse_mode="Markdown" \
        --data-urlencode "text=📰 *Morning News Sweep*

${MSG}" \
        >> "$LOG_FILE" 2>&1

    echo "$(date): Telegram notification sent" >> "$LOG_FILE"
else
    echo "$(date): Sweep failed or empty output, no notification" >> "$LOG_FILE"
fi
