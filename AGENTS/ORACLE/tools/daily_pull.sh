#!/usr/bin/env bash
# ORACLE daily pulls-only routine — WQ-527 C, option A (Will 2026-10-28 20:59 ET, verbatim
# "527 C approve, 528 A approve"; DOCKET L847). Registry: AGENTS/ORACLE/SCHEDULED_RUNS.md.
#
# What it does, once per US weekday (ET date): polymarket.py pull --log, kalshi.py pull --log,
# tools/disruption_supply_spread.py; appends one receipt row to workbook/ROUTINE_RUNS.tsv;
# commits ONLY those four files, path-scoped, locally (never pushes — the next closeout does).
# What it NEVER does: grade a read, touch STATUS/VX/KB/V5_* ledgers, pin or roll a market.
# The next live ORACLE session grades the logged rows (letter O3: the first pull of the ET date
# is the read, whoever triggered it).
#
# Idempotent: cron fires it several times a day; it exits silently if ODDS_LOG already holds a
# row stamped on today's ET date (a session or an earlier slot already took the read).
set -u
ORC="$(cd "$(dirname "$0")/.." && pwd)"
REPO="$(cd "$ORC/../.." && pwd)"
PY="$REPO/.venv/bin/python3"; [ -x "$PY" ] || PY="$(command -v python3)"
RUNS="$ORC/workbook/ROUTINE_RUNS.tsv"
ODDS="$ORC/workbook/ODDS_LOG.tsv"

exec 9>"/tmp/oracle_daily_pull.lock"
flock -n 9 || exit 0

ET_DATE="$(TZ=America/New_York date +%F)"
[ "$(TZ=America/New_York date +%u)" -ge 6 ] && exit 0   # weekend: no read to take

# Already read today? (last ODDS_LOG row's UTC stamp converted to its ET date)
LAST_ET="$("$PY" - "$ODDS" <<'PY'
import sys, datetime as dt
from zoneinfo import ZoneInfo
last = None
with open(sys.argv[1]) as fh:
    for line in fh:
        if line[:2] == "20":
            last = line.split("\t", 1)[0]
if last:
    t = dt.datetime.strptime(last, "%Y-%m-%dT%H:%MZ").replace(tzinfo=dt.timezone.utc)
    print(t.astimezone(ZoneInfo("America/New_York")).date().isoformat())
PY
)"
[ "$LAST_ET" = "$ET_DATE" ] && exit 0

cd "$ORC" || exit 1
PM_OUT="$("$PY" -W ignore scripts/polymarket.py pull --log 2>&1)"; PM_RC=$?
KA_OUT="$("$PY" -W ignore scripts/kalshi.py pull --log 2>&1)"; KA_RC=$?
SP_OUT="$("$PY" -W ignore tools/disruption_supply_spread.py 2>&1)"; SP_RC=$?
PM_ROWS="$(printf '%s\n' "$PM_OUT" | sed -n 's/^logged \([0-9]*\) rows.*/\1/p' | tail -1)"
KA_ROWS="$(printf '%s\n' "$KA_OUT" | sed -n 's/^logged \([0-9]*\) rows.*/\1/p' | tail -1)"
SPREAD="$(printf '%s\n' "$SP_OUT" | sed -n 's/^ *Spread = .* = \([+-][0-9.]*pp\).*/\1/p' | tail -1)"
NOTFOUND="$(printf '%s\n' "$PM_OUT" | grep -c '^   - .*\[' || true)"

# A read exists only if Polymarket actually appended rows (0 = double-log guard skip or a dead pull).
if [ $PM_RC -eq 0 ] && [ "${PM_ROWS:-0}" -gt 0 ] && [ $KA_RC -eq 0 ] && [ $SP_RC -eq 0 ]; then STATUS=OK
elif [ $PM_RC -eq 0 ] && [ "${PM_ROWS:-0}" -gt 0 ]; then STATUS=PARTIAL
else STATUS=FAIL; fi
NOTE="spread ${SPREAD:-none}"
[ "${PM_ROWS:-0}" -eq 0 ] && NOTE="NO READ: polymarket logged 0 rows (rc=$PM_RC); $NOTE"
[ $SP_RC -ne 0 ] && NOTE="spread tool rc=$SP_RC: $(printf '%s\n' "$SP_OUT" | tail -1 | tr '\t' ' ' | cut -c1-160)"

[ -f "$RUNS" ] || printf 'run_ts_utc\tet_date\thost\tstatus\tpm_rc\tpm_rows\tkalshi_rc\tkalshi_rows\tspread_rc\tnote\n' > "$RUNS"
printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$(date -u +%FT%H:%MZ)" "$ET_DATE" "$(hostname)" \
  "$STATUS" "$PM_RC" "${PM_ROWS:-0}" "$KA_RC" "${KA_ROWS:-0}" "$SP_RC" "$NOTE" >> "$RUNS"

# Commit only this routine's own files, path-scoped (root Git Protocol; no push).
cd "$REPO" || exit 1
FILES="AGENTS/ORACLE/workbook/ODDS_LOG.tsv AGENTS/ORACLE/workbook/KALSHI_ODDS_LOG.tsv AGENTS/ORACLE/workbook/DISRUPTION_SUPPLY_SPREAD.tsv AGENTS/ORACLE/workbook/ROUTINE_RUNS.tsv"
MSG="ORACLE routine: daily pulls $ET_DATE ($STATUS, PM ${PM_ROWS:-0} rows, Kalshi ${KA_ROWS:-0}, ${SPREAD:-no spread})"
for i in 1 2 3; do
  git add -- $FILES 2>/dev/null && git commit -q -m "$MSG" -- $FILES && exit 0
  sleep 20
done
echo "oracle daily_pull: commit failed after 3 tries; rows are on disk uncommitted" >&2
exit 2
