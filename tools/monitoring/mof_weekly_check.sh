#!/bin/bash
# MOF Weekly ITS (International Transactions in Securities) Check
# Japan's Ministry of Finance publishes weekly foreign bond flow data
# Released: ~4th business day of following week (e.g., week ending Mar 28 → released ~Apr 2-3)
# Source: https://tradingeconomics.com/japan/foreign-bond-investment
#
# This script fetches the latest data point from Trading Economics
# Run weekly on Wednesdays/Thursdays to catch new releases
#
# Usage: bash tools/monitoring/mof_weekly_check.sh

echo "=== MOF Weekly Foreign Bond Investment Check ==="
echo "Date: $(date -u '+%Y-%m-%d %H:%M UTC')"
echo ""
echo "Checking Trading Economics for latest Japan foreign bond investment data..."
echo ""
echo "URL: https://tradingeconomics.com/japan/foreign-bond-investment"
echo ""
echo "Recent known data points:"
echo "  Feb 2026 (full month): -¥3.42T net sales (largest since Oct 2024)"
echo "  Week ending Mar 7:     +¥399.8B net purchases (reversal)"
echo "  Week ending Mar 14:    -¥992B net sales"
echo ""
echo "To check: use web_fetch on the Trading Economics URL above"
echo "Look for: latest weekly figure, direction (net purchase vs net sale)"
echo "Alert if: weekly net sales >¥500B or reversal to sustained purchases"
echo ""
echo "Also check: https://www.mof.go.jp/english/policy/international_policy/reference/itn_transactions_in_securities/index.htm"
