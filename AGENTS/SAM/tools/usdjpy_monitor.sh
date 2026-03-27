#!/bin/bash
# SAM USD/JPY Threshold Monitor
# Pulls USD/JPY from Yahoo Finance, alerts on threshold breaches
# State file prevents repeated alerts for the same breach

STATE_FILE="/home/moltbot/.openclaw/workspace/AGENTS/SAM/tools/.usdjpy_alert_state"
touch "$STATE_FILE" 2>/dev/null

# Fetch USD/JPY
RATE=$(curl -s -H "User-Agent: Mozilla/5.0" \
  "https://query1.finance.yahoo.com/v8/finance/chart/USDJPY=X?range=1d&interval=1m" 2>/dev/null \
  | jq -r '.chart.result[0].meta.regularMarketPrice // empty' 2>/dev/null)

if [ -z "$RATE" ]; then
  echo "⚠️ SAM Monitor: Failed to fetch USD/JPY. Yahoo Finance may be down."
  exit 1
fi

# Also fetch FXY for context
FXY=$(curl -s -H "User-Agent: Mozilla/5.0" \
  "https://query1.finance.yahoo.com/v8/finance/chart/FXY?range=1d&interval=1d" 2>/dev/null \
  | jq -r '.chart.result[0].meta.regularMarketPrice // empty' 2>/dev/null)

TIMESTAMP=$(date -u '+%Y-%m-%d %H:%M UTC')
ALERT=""

# Threshold checks — ordered by severity
# Each threshold has a unique key to prevent repeat alerts

check_threshold() {
  local KEY="$1"
  local CONDITION="$2"  # "above" or "below"
  local LEVEL="$3"
  local EMOJI="$4"
  local MESSAGE="$5"
  
  local TRIGGERED=false
  if [ "$CONDITION" = "above" ]; then
    TRIGGERED=$(python3 -c "print('true' if $RATE > $LEVEL else 'false')")
  else
    TRIGGERED=$(python3 -c "print('true' if $RATE < $LEVEL else 'false')")
  fi
  
  if [ "$TRIGGERED" = "true" ]; then
    # Check if already alerted
    if ! grep -q "^${KEY}$" "$STATE_FILE" 2>/dev/null; then
      echo "$KEY" >> "$STATE_FILE"
      ALERT="${ALERT}${EMOJI} ${MESSAGE}\n"
    fi
  else
    # Clear the alert if rate has moved back (allows re-alert on next breach)
    sed -i "/^${KEY}$/d" "$STATE_FILE" 2>/dev/null
  fi
}

# 🔴🔴 CRITICAL thresholds
check_threshold "USDJPY_167" "above" "167" "🔴🔴" "USD/JPY BREACHED 167 ($RATE) — STOP LOSS LEVEL. FXY position thesis may be broken. No MOF response at this level = cut."
check_threshold "USDJPY_165" "above" "165" "🔴🔴" "USD/JPY BREACHED 165 ($RATE) — Approaching stop. Yen weakness accelerating despite JGB yields. Watch for MOF emergency action."
check_threshold "USDJPY_162" "above" "162" "🔴" "USD/JPY BREACHED 162 ($RATE) — Stress level. Intervention overdue. Oil shock dominating rate differentials."
check_threshold "USDJPY_160" "above" "160" "🔴" "USD/JPY BREACHED 160 ($RATE) — MOF intervention trigger. July 2024 precedent: ~\$37B spent, 5-6% reversal."

# 🟢 POSITIVE thresholds (yen strengthening = FXY thesis working)
check_threshold "USDJPY_155" "below" "155" "🟢" "USD/JPY BELOW 155 ($RATE) — Carry unwind Phase 2 onset. FXY thesis playing out. Consider Tranche 2 if not already added."
check_threshold "USDJPY_150" "below" "150" "🟢🟢" "USD/JPY BELOW 150 ($RATE) — Deep carry unwind. FXY target zone approaching (\$60-62)."
check_threshold "USDJPY_145" "below" "145" "🟢🟢🟢" "USD/JPY BELOW 145 ($RATE) — Full carry unwind / HANS Fed cut path activated. Consider taking partial FXY profits."

# Output
if [ -n "$ALERT" ]; then
  echo "🇯🇵 SAM THRESHOLD ALERT — $TIMESTAMP"
  echo "USD/JPY: $RATE | FXY: \$${FXY:-N/A}"
  echo ""
  echo -e "$ALERT"
  echo "Thresholds: 🔴 160/162/165/167 (stop) | 🟢 155/150/145 (thesis working)"
else
  # Silent — no thresholds breached, no output (cron won't notify)
  # Uncomment below for debug logging:
  # echo "SAM Monitor: USD/JPY $RATE — no threshold breach. FXY \$${FXY:-N/A}"
  exit 0
fi
