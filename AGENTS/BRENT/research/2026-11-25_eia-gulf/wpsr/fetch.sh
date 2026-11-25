#!/bin/bash
# BRENT 2026-11-25: poll ir.eia.gov WPSR until the week-ending 11/20 release appears, then save release-day bytes.
# Client string: honest name per WQ-735 (research-bot/1.0); no browser string. A refusal is recorded, never worked around.
cd "$(dirname "$0")"
UA="research-bot/1.0"
for i in $(seq 1 75); do
  code=$(curl -s -L -m 30 -A "$UA" -w '%{http_code}' https://ir.eia.gov/wpsr/summary.txt -o summary.txt)
  if grep -q -E 'November 20, 2026' summary.txt 2>/dev/null; then
    echo "release seen at $(date '+%F %T %Z') (http $code)" > capture.txt
    for f in table1.csv table2.csv table4.csv table9.csv psw01.xls psw09.xls wpsr.csv; do c=$(curl -s -L -m 60 -A "$UA" -w '%{http_code}' https://ir.eia.gov/wpsr/$f -o $f); echo "$f http $c" >> capture.txt; done
    c=$(curl -s -L -m 60 -A "$UA" -w '%{http_code}' https://www.eia.gov/petroleum/gasdiesel/xls/pswrgvwall.xls -o eia-retail.xls); echo "eia-retail.xls http $c" >> capture.txt
    echo "files saved $(date '+%F %T %Z')" >> capture.txt
    exit 0
  fi
  echo "poll $i $(date '+%T') http $code" >> poll.log
  sleep 15
done
echo "no release after polling $(date)" > capture.txt; exit 1
