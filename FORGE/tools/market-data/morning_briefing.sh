#!/bin/bash
# PROME Morning Briefing — sends compact dashboard to Telegram at 6 AM ET
#
# Cron: 0 6 * * * /home/moltbot/.openclaw/workspace/FORGE/tools/market-data/morning_briefing.sh

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# Get compact output (with 60s timeout)
OUTPUT=$(timeout 60 python3 dashboard.py --compact --no-save 2>/dev/null)

if [ -z "$OUTPUT" ]; then
    exit 0
fi

# Build message
TIMESTAMP=$(date +"%a %b %d, %I:%M %p %Z")

# Get stress summary from JSON mode (with 60s timeout)
SUMMARY=$(timeout 60 python3 dashboard.py --json --no-save 2>/dev/null | python3 -c "
import sys, json
d = json.load(sys.stdin)
r,y,g = d['summary']['red'], d['summary']['yellow'], d['summary']['green']
print(f'{r}🔴 {y}🟡 {g}🟢')
" 2>/dev/null)

MESSAGE="☀️ *PROME Morning Briefing*
_${TIMESTAMP}_

${OUTPUT}

${SUMMARY}"

# Send to Telegram
curl -s -X POST "https://api.telegram.org/bot8533568512:AAEf4FwstJbg0GE0FcEB-w96I9hJokPuY8k/sendMessage" \
    -H "Content-Type: application/json" \
    -d "{\"chat_id\": \"8463631023\", \"text\": $(echo "$MESSAGE" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read()))'), \"parse_mode\": \"Markdown\"}" \
    > /dev/null 2>&1
