#!/usr/bin/env bash
# Reproduce every number in REPORT.md from ../data. Python 3 + pandas, numpy, matplotlib, openpyxl.
set -e; cd "$(dirname "$0")"; mkdir -p ../out
python3 reindex.py        | tee ../out/log_reindex_check.txt
python3 attribution.py    | tee ../out/log_attribution.txt
python3 robust.py         | tee ../out/log_robustness.txt
python3 corr_start.py     | tee ../out/log_corr_start.txt
python3 corr_hist.py      | tee ../out/log_corr_history.txt
python3 end_date.py       | tee ../out/log_end_date.txt
python3 final_tables.py   | tee ../out/log_final_tables.txt
python3 validate.py       | tee ../out/log_validation.txt
