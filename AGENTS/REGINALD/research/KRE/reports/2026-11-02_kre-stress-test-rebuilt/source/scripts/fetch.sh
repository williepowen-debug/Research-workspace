#!/usr/bin/env bash
# Rebuilt stress-test data fetch (KRE–KBWB decoupling, data through 10/30/2026 close).
# Usage: bash scripts/fetch.sh   (run from the folder root; writes into data/)
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data/px data/ust
UA="Mozilla/5.0"
P1=1104537600      # 2005-01-01
P2=1800000000      # far future: Yahoo drops the latest days if period2 is not after today

# 1) SSGA: KRE daily holdings (as of 30-Oct-2026 when fetched) and NAV history
curl -s -A "$UA" -o data/kre_holdings.xlsx "https://www.ssga.com/library-content/products/fund-data/etfs/us/holdings-daily-us-en-kre.xlsx"
curl -s -A "$UA" -o data/kre_navhist.xlsx  "https://www.ssga.com/library-content/products/fund-data/etfs/us/navhist-us-en-kre.xlsx"

# 2) Yahoo chart API (daily, adjusted close). ETFs + megabanks + all KRE members.
ETFS="KRE KBWB SPY IWM KBE IAT QABA RSP JPM BAC WFC C GS MS"
MEMBERS=$(python3 - <<'EOF'
import pandas as pd
h = pd.read_excel("data/kre_holdings.xlsx", header=4)
h = h[h.Ticker.notna() & (h.Ticker != "-")]
print(" ".join(h.Ticker.astype(str)))
EOF
)
for t in $ETFS $MEMBERS; do
  [ -s "data/px/$t.json" ] || curl -s -A "$UA" -o "data/px/$t.json" \
    "https://query1.finance.yahoo.com/v8/finance/chart/$t?period1=$P1&period2=$P2&interval=1d&events=div%7Csplit&includeAdjustedClose=true"
done

# 3) US Treasury daily par yield curve, one CSV per year
for y in $(seq 2011 2026); do
  curl -s -A "$UA" -o "data/ust/ust_$y.csv" \
    "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/$y/all?type=daily_treasury_yield_curve&field_tdr_date_value=$y&page&_format=csv"
done
echo "fetch done"
