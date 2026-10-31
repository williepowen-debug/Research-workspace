#!/bin/bash
# WSV PEGELONLINE bulk raw-data route (the JS "Zeitreihen-Download" modal on /gast/pegeltabelle, driven directly).
# Verified 2026-10-31 09:28 ET: HTTP 200, 7,195,546 B zip, 15-min W from 2000-01-01 01:00 local (MEZ/MESZ).
# Licence: DL-DE->Zero-2.0 (pegelonline.wsv.de/gast/nutzungsbedingungen). Data are UNCHECKED raw data (quality=unchecked).
# usage: pull_wsv_long_series.sh <outdir> [start YYYY-MM-DD] [end YYYY-MM-DD]
set -euo pipefail
OUT="$1"; START="${2:-2000-01-01}"; END="${3:-$(date +%F)}"
mkdir -p "$OUT"; CJ="$OUT/cj.txt"
PID=$(python3 -c 'import uuid;print(uuid.uuid4())')
# step 1: POST the form (Kaub + Duisburg-Ruhrort uuids, parameter W, csv) -> JSON {"downloadUrl": ...}
URL=$(curl -sL -c "$CJ" -b "$CJ" -X POST "https://pegelonline.wsv.de/gast/download/prepare" \
  --data-urlencode "uuid=1d26e504-7f9e-480a-b52c-5932be6549ab" \
  --data-urlencode "uuid=c0f51e35-d0e8-4318-afaf-c5fcbc29f4c1" \
  --data-urlencode "parameter=W" --data-urlencode "start=$START" --data-urlencode "end=$END" \
  --data-urlencode "progressId=$PID" --data-urlencode "format=csv" --max-time 590 \
  | python3 -c 'import json,sys;print(json.load(sys.stdin)["downloadUrl"])')
# step 2: GET the zip (kaub/*.csv, duisburgruhrort/*.csv; "timestamp;value", 15-min, cm)
curl -sL -b "$CJ" -o "$OUT/w.zip" "https://pegelonline.wsv.de$URL"
sha256sum "$OUT/w.zip"; unzip -o -q "$OUT/w.zip" -d "$OUT"
