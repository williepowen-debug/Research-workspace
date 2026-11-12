#!/bin/bash
# BRENT 2026-11-12: poll ir.eia.gov WPSR until the week-ending 11/6 release appears, then save release-day bytes.
cd "$(dirname "$0")"
UA="Mozilla/5.0 (X11; Linux x86_64)"
for i in $(seq 1 60); do
  curl -s -L -m 30 -A "$UA" https://ir.eia.gov/wpsr/summary.txt -o summary.txt
  if grep -q -E 'November 0?6, 2026' summary.txt 2>/dev/null; then
    echo "release seen at $(date '+%F %T %Z')" > capture.txt
    for f in table1.csv table2.csv table4.csv table9.csv psw01.xls psw09.xls wpsr.csv; do curl -s -L -m 60 -A "$UA" https://ir.eia.gov/wpsr/$f -o $f; done
    curl -s -L -m 60 -A "$UA" https://www.eia.gov/petroleum/gasdiesel/xls/pswrgvwall.xls -o eia-retail.xls
    echo "files saved $(date '+%F %T %Z')" >> capture.txt
    exit 0
  fi
  sleep 20
done
echo "no release after 20 min $(date)" > capture.txt; exit 1
