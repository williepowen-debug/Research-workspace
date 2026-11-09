#!/usr/bin/env bash
# Scratch test of AGENTS/ORACLE/tools/daily_pull.sh sync-first (PROME brief 2026-11-09).
# Never touches the live repo: bare "origin" + clones boxA/boxB in a mktemp dir, stub pullers
# (no market calls). Usage: bash AGENTS/ORACLE/tools/test_daily_pull_sync.sh   (rc 0 = all pass)
# Holds /tmp/oracle_daily_pull.lock briefly in case 6: do not run it across a cron slot (:15).
set -u
LIVE="$(cd "$(dirname "$0")/../../.." && pwd)"
NEW_SCRIPT="$LIVE/AGENTS/ORACLE/tools/daily_pull.sh"
OLD_SCRIPT_REV="${OLD_REV:-45a7701876~1}"   # pre-sync-first version, for the "exactly as before" comparison
T="$(mktemp -d "${TMPDIR:-/tmp}/oracle_sync_test.XXXXXX")/synctest"; trap 'rm -rf "$(dirname "$T")"' EXIT
PASS=0; FAIL=0
ok()  { echo "  PASS: $1"; PASS=$((PASS+1)); }
bad() { echo "  FAIL: $1"; FAIL=$((FAIL+1)); }
chk() { if eval "$1"; then ok "$2"; else bad "$2  [cond: $1]"; fi; }
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@t GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@t

setup() {   # $1 = script source file to install
  rm -rf "$T"; mkdir -p "$T"
  git init -q --bare -b master "$T/origin.git"
  local S="$T/seed"; git init -q -b master "$S"
  mkdir -p "$S/AGENTS/ORACLE/tools" "$S/AGENTS/ORACLE/scripts" "$S/AGENTS/ORACLE/workbook" "$S/AGENTS/OTHER"
  cp "$1" "$S/AGENTS/ORACLE/tools/daily_pull.sh"
  for f in polymarket:ODDS_LOG:3 kalshi:KALSHI_ODDS_LOG:2; do
    IFS=: read -r name log n <<<"$f"
    cat > "$S/AGENTS/ORACLE/scripts/$name.py" <<PY
import datetime, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'workbook', '$log.tsv')
ts = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
with open(p, 'a') as fh:
    for i in range($n): fh.write(f"{ts}\tstub-$name-{i}\t0.5\n")
print("logged $n rows to $log.tsv")
PY
  done
  cat > "$S/AGENTS/ORACLE/tools/disruption_supply_spread.py" <<'PY'
import os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'workbook', 'DISRUPTION_SUPPLY_SPREAD.tsv')
with open(p, 'a') as fh: fh.write("stub\t+77.0\n")
print("  Spread = 90.0 - 13.0 = +77.0pp")
PY
  printf 'ts_utc\tslug\tprob\n2026-11-06T15:15Z\tseed\t0.4\n' > "$S/AGENTS/ORACLE/workbook/ODDS_LOG.tsv"
  printf 'ts_utc\tticker\tprob\n' > "$S/AGENTS/ORACLE/workbook/KALSHI_ODDS_LOG.tsv"
  printf 'date\tspread\n' > "$S/AGENTS/ORACLE/workbook/DISRUPTION_SUPPLY_SPREAD.tsv"
  printf 'run_ts_utc\tet_date\thost\tstatus\tpm_rc\tpm_rows\tkalshi_rc\tkalshi_rows\tspread_rc\tnote\n' > "$S/AGENTS/ORACLE/workbook/ROUTINE_RUNS.tsv"
  printf 'line one\nline two\n' > "$S/AGENTS/OTHER/x.md"
  (cd "$S" && git add -A && git commit -qm seed && git remote add origin "$T/origin.git" && git push -q origin master)
  git -C "$T/origin.git" symbolic-ref HEAD refs/heads/master
  git clone -q "$T/origin.git" "$T/boxA"; git clone -q "$T/origin.git" "$T/boxB"
  [ -f "$T/boxA/AGENTS/ORACLE/tools/daily_pull.sh" ] && [ -n "$(git -C "$T/boxA" rev-parse -q --verify HEAD)" ] \
    || { echo "SETUP FAILED: boxA has no seeded checkout; aborting (no vacuous passes)"; exit 99; }
}
run() { RUN_OUT="$(bash "$1/AGENTS/ORACLE/tools/daily_pull.sh" 2>&1)"; RUN_RC=$?; echo "    [rc=$RUN_RC] ${RUN_OUT:-<no output>}"; }
snap() {    # everything a "repo as found" claim covers, incl. tracked-file mtimes
  (cd "$1" && git rev-parse HEAD && git status --porcelain --branch --untracked-files=all \
   && git diff | sha1sum && git diff --cached | sha1sum && git stash list \
   && ls "$(git rev-parse --git-path rebase-merge)" "$(git rev-parse --git-path rebase-apply)" 2>/dev/null; true)
}
mtimes() { (cd "$1" && git ls-files -z | xargs -0 stat -c '%n %y'); }
commit_on_B() { (cd "$T/boxB" && printf '%s\n' "$1" >> AGENTS/OTHER/x.md && git commit -qam "B: $1" && git push -q origin master); }
today_rows() { local et; et="$(TZ=America/New_York date +%F)"; grep -c "	$et	" "$1/AGENTS/ORACLE/workbook/ROUTINE_RUNS.tsv"; }

echo "== Case 1: ordinary (up to date, no read today) -> reads and commits exactly as before"
OLD="$(dirname "$T")/old.sh";git -C "$LIVE" show "$OLD_SCRIPT_REV:AGENTS/ORACLE/tools/daily_pull.sh" > "$OLD"
setup "$OLD"; run "$T/boxA"; OLD_RC=$RUN_RC
OLD_FILES="$(git -C "$T/boxA" show --name-only --format= HEAD | sort | tr '\n' ' ')"
OLD_SUBJ="$(git -C "$T/boxA" log -1 --format=%s | sed 's/[0-9]\{4\}-[0-9-]*//')"
setup "$NEW_SCRIPT"; run "$T/boxA"
NEW_FILES="$(git -C "$T/boxA" show --name-only --format= HEAD | sort | tr '\n' ' ')"
NEW_SUBJ="$(git -C "$T/boxA" log -1 --format=%s | sed 's/[0-9]\{4\}-[0-9-]*//')"
chk '[ $RUN_RC -eq 0 ] && [ $OLD_RC -eq 0 ]' "both versions exit 0"
chk '[ "$NEW_FILES" = "$OLD_FILES" ]' "same four files committed as the old script ($NEW_FILES)"
chk '[ "$NEW_SUBJ" = "$OLD_SUBJ" ]' "same commit subject shape ($NEW_SUBJ)"
chk '[ "$(today_rows "$T/boxA")" -eq 1 ] && [ -z "$(git -C "$T/boxA" status --porcelain)" ]' "one OK receipt row, tree clean"
B4="$(snap "$T/boxA")"; run "$T/boxA"
chk '[ $RUN_RC -eq 0 ] && [ -z "$RUN_OUT" ] && [ "$B4" = "$(snap "$T/boxA")" ]' "second slot same day: silent exit, nothing changed"

echo "== Case 2a: behind + clean, origin holds the other box's read for today -> pull, silent exit"
setup "$NEW_SCRIPT"; run "$T/boxB"; git -C "$T/boxB" push -q origin master
run "$T/boxA"
chk '[ $RUN_RC -eq 0 ] && [ -z "$RUN_OUT" ]' "silent exit 0"
chk '[ "$(git -C "$T/boxA" rev-parse HEAD)" = "$(git -C "$T/boxA" rev-parse origin/master)" ]' "boxA now at origin/master, no second commit"
chk '[ "$(today_rows "$T/boxA")" -eq 1 ] && [ -z "$(git -C "$T/boxA" status --porcelain)" ]' "exactly one receipt row (boxB's), tree clean"

echo "== Case 2b: behind + clean, origin newer but no read today -> pull, read, commit on top of origin"
setup "$NEW_SCRIPT"; commit_on_B "other desk work"
run "$T/boxA"
chk '[ $RUN_RC -eq 0 ]' "exit 0"
chk 'git -C "$T/boxA" merge-base --is-ancestor origin/master HEAD && [ "$(git -C "$T/boxA" rev-parse HEAD~1)" = "$(git -C "$T/boxA" rev-parse origin/master)" ]' "read commit sits directly on origin/master (fast-forwardable)"
chk '(cd "$T/boxA" && git push -q --dry-run origin master)' "push dry-run is a fast-forward"
chk '[ "$(today_rows "$T/boxA")" -eq 1 ]' "one receipt row"

echo "== Case 3: behind + dirty (tracked file elsewhere modified) -> skip, nothing touched"
setup "$NEW_SCRIPT"; commit_on_B "upstream change"
echo "dirty desk edit" >> "$T/boxA/AGENTS/OTHER/x.md"; git -C "$T/boxA" fetch -q
B4="$(snap "$T/boxA")"; M4="$(mtimes "$T/boxA")"; run "$T/boxA"
chk '[ $RUN_RC -eq 3 ] && printf "%s" "$RUN_OUT" | grep -q "SKIP.*behind origin/master by 1 and tracked files are modified"' "exit 3 with a named SKIP reason"
chk '[ "$B4" = "$(snap "$T/boxA")" ]' "git status / HEAD / diffs identical before and after"
chk '[ "$M4" = "$(mtimes "$T/boxA")" ]' "no tracked file touched (mtimes identical, ROUTINE_RUNS included)"
echo "   (3b: staged instead of modified)"
git -C "$T/boxA" add AGENTS/OTHER/x.md; B4="$(snap "$T/boxA")"; run "$T/boxA"
chk '[ $RUN_RC -eq 3 ] && [ "$B4" = "$(snap "$T/boxA")" ]' "staged file: skip, state identical"

echo "== Case 4: pull conflict (unpushed local commit conflicts with origin) -> abort, skip, as found"
setup "$NEW_SCRIPT"
(cd "$T/boxA" && sed -i 's/line one/line one LOCAL/' AGENTS/OTHER/x.md && git commit -qam "A local unpushed")
(cd "$T/boxB" && sed -i 's/line one/line one REMOTE/' AGENTS/OTHER/x.md && git commit -qam "B remote" && git push -q origin master)
git -C "$T/boxA" fetch -q; B4="$(snap "$T/boxA")"; M4="$(mtimes "$T/boxA")"; run "$T/boxA"
chk '[ $RUN_RC -eq 3 ] && printf "%s" "$RUN_OUT" | grep -q "SKIP.*pull --rebase failed or stopped, rebase aborted"' "exit 3 with a named SKIP reason"
chk '[ "$B4" = "$(snap "$T/boxA")" ]' "HEAD, status, diffs identical; no rebase in progress"
chk '[ "$(today_rows "$T/boxA")" -eq 0 ]' "no read taken, no receipt row"
if [ "$M4" = "$(mtimes "$T/boxA")" ]; then ok "tracked-file mtimes identical"; else
  echo "  NOTE: mtimes changed on: $(diff <(echo "$M4") <(mtimes "$T/boxA") | grep '^>' | cut -d' ' -f2 | tr '\n' ' ')(content identical; the rebase checkout + abort rewrote them)"; fi

echo "== Case 5: fetch fails (unreachable remote URL) -> skip, nothing touched"
setup "$NEW_SCRIPT"; git -C "$T/boxA" remote set-url origin "$T/does-not-exist.git"
B4="$(snap "$T/boxA")"; M4="$(mtimes "$T/boxA")"; run "$T/boxA"
chk '[ $RUN_RC -eq 3 ] && printf "%s" "$RUN_OUT" | grep -q "SKIP.*git fetch origin failed"' "exit 3 with a named SKIP reason"
chk '[ "$B4" = "$(snap "$T/boxA")" ] && [ "$M4" = "$(mtimes "$T/boxA")" ]' "state and mtimes identical"

echo "== Case 6: concurrent slot -> the existing flock still blocks it"
setup "$NEW_SCRIPT"
flock /tmp/oracle_daily_pull.lock sleep 4 & HOLDER=$!; sleep 0.5
B4="$(snap "$T/boxA")"; run "$T/boxA"; wait $HOLDER
chk '[ $RUN_RC -eq 0 ] && [ -z "$RUN_OUT" ] && [ "$B4" = "$(snap "$T/boxA")" ]' "blocked slot exits 0 silently, no fetch/read/commit"
run "$T/boxA"
chk '[ $RUN_RC -eq 0 ] && [ "$(today_rows "$T/boxA")" -eq 1 ]' "after the lock frees, the next slot reads"

echo "== Case 7 (extra): another session's rebase already stopped in this checkout -> skip, NOT aborted"
setup "$NEW_SCRIPT"
(cd "$T/boxA" && sed -i 's/line one/line one LOCAL/' AGENTS/OTHER/x.md && git commit -qam "A local")
(cd "$T/boxB" && sed -i 's/line one/line one REMOTE/' AGENTS/OTHER/x.md && git commit -qam "B remote" && git push -q origin master)
(cd "$T/boxA" && git pull --rebase -q >/dev/null 2>&1); B4="$(snap "$T/boxA")"; run "$T/boxA"
chk '[ $RUN_RC -eq 3 ] && [ -d "$(git -C "$T/boxA" rev-parse --absolute-git-dir)/rebase-merge" ] && [ "$B4" = "$(snap "$T/boxA")" ]' "skip; the foreign rebase is left in place untouched"

echo "== Case 8 (extra): behind with only an UNTRACKED file -> pulls and reads; untracked file kept"
setup "$NEW_SCRIPT"; commit_on_B "upstream"; echo scratch > "$T/boxA/AGENTS/OTHER/untracked.txt"
run "$T/boxA"
chk '[ $RUN_RC -eq 0 ] && [ "$(git -C "$T/boxA" rev-parse HEAD~1)" = "$(git -C "$T/boxA" rev-parse origin/master)" ] && [ -f "$T/boxA/AGENTS/OTHER/untracked.txt" ]' "read committed on top of origin, untracked file intact"

echo "== Case 9 (extra): this checkout already holds today's read, origin newer -> silent exit, NO fetch/pull"
setup "$NEW_SCRIPT"; run "$T/boxA"; commit_on_B "later upstream"
REF4="$(git -C "$T/boxA" rev-parse origin/master)"; B4="$(snap "$T/boxA")"; run "$T/boxA"
chk '[ $RUN_RC -eq 0 ] && [ -z "$RUN_OUT" ] && [ "$B4" = "$(snap "$T/boxA")" ] && [ "$REF4" = "$(git -C "$T/boxA" rev-parse origin/master)" ]' "silent exit; HEAD and origin/master ref unchanged (no fetch, no rebase of unpushed commits)"

echo; echo "RESULT: $PASS passed, $FAIL failed"; [ $FAIL -eq 0 ]
