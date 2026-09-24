# Build record: safe-push wording + market.py prev-close/stale repair (2026-09-24)

**Builder:** DAEDALUS build subagent (team-lead task) · **Standard:** `BLUEPRINTS/CHECK_STANDARD.md` §3 (alert line watched on a capable case; clean line watched on a clean case)
**Files changed (only these two):** `scripts/safe-push.sh` · `scripts/market.py` (+ this record). **No git mutation run; `safe-push.sh` was NOT executed.**
Pre-edit copies: session scratchpad `fix-push-market/{safe-push.sh,market.py}`.

## REPAIR 1: `scripts/safe-push.sh` (WORDING ONLY)

**Defect (PROME, measured):** two agents in one hop read `CANNOT-CONFIRM: git push exited $push_rc …` as the SCRIPT's rc.

| Line (new) | Before | After |
|---|---|---|
| 108 | `CANNOT-CONFIRM: git push exited $push_rc, but the post-push fetch …` | `CANNOT-CONFIRM (safe-push rc=2): the \`git push\` subcommand exited $push_rc, but the post-push fetch …` |
| 114 | `(note: git push exited $push_rc but the ref IS on origin — …)` | `(note: the \`git push\` subcommand exited $push_rc, but the ref IS on origin — …; safe-push rc=0)` |
| 117 | `(git push rc=$push_rc)` | `(the \`git push\` subcommand's rc=$push_rc; safe-push rc=1)` |
| 33–42 | (none) | Header: RC CONTRACT line + **KILLED RUN** clause (rc 124/external kill = CANNOT-CONFIRM; ref-update line = subcommand, not certification; any fallback = ONE captured `git ls-remote`, CRUISE 9/19) |

**`--help`/usage:** none exists. The only usage text is the header comment `# Usage: safe-push.sh [--dry-run]`, and the KILLED-RUN clause sits directly under it. No `--help` flag was added, because that would change behaviour.

**Verification:**
- `bash -n scripts/safe-push.sh` → `bash -n: OK`
- Non-comment code diff (pre vs post) = exactly the 3 echo lines above; nothing else.
- Exit statements: 8 before, 8 after, **content byte-identical** (line numbers +9 from the header clause):
  before `45 exit 1 · 56 exit 1 · 69 exit 1 · 74 exit 0 · 83 exit 0 · 101 exit 2 · 106 exit 0 · 116 exit 1`
  after  `54 exit 1 · 65 exit 1 · 78 exit 1 · 83 exit 0 · 92 exit 0 · 110 exit 2 · 115 exit 0 · 125 exit 1`
- The rc token printed in each changed line matches the `exit` that follows it: CANNOT-CONFIRM→`exit 2` (:110), note→`exit 0` (:115), NOT PUSHED→`exit 1` (:125).
- **Capable case:** the lines were extracted from the file and eval'd with `push_rc=0/1 REMOTE=origin BRANCH=master`. The note line is shown without its `push_rc -ne 0` guard.
```
CANNOT-CONFIRM (safe-push rc=2): the `git push` subcommand exited 0, but the post-push fetch of origin/master FAILED — the receipt cannot be issued either way.
  (note: the `git push` subcommand exited 0, but the ref IS on origin — a concurrent train carried it; safe-push rc=0)
NOT PUSHED: HEAD 0c45fcbf4 is NOT on origin/master after the push (the `git push` subcommand's rc=0; safe-push rc=1).
CANNOT-CONFIRM (safe-push rc=2): the `git push` subcommand exited 1, but the post-push fetch of origin/master FAILED — …
NOT PUSHED: HEAD 0c45fcbf4 is NOT on origin/master after the push (the `git push` subcommand's rc=1; safe-push rc=1).
```
- **Clean case:** every other message is byte-identical, including ABORT (×3), `Nothing to push`, `[--dry-run] stopping before push.`, `Pushed. CONFIRMED: …` and the RECOVERY block. This is proven by the non-comment code diff. The script was NOT run live, because `--dry-run` still does `git fetch`, which updates remote-tracking refs, and the brief forbids mutating git.

**rc contract (unchanged, quoted from ⑦b):** "rc contract: 0 confirmed · 1 NOT confirmed (the push output is above; treat it as a failed push and re-run the rebase recipe) · 2 CANNOT-CONFIRM."

## REPAIR 2: `scripts/market.py` `fmt()`

**Defect (PROME, DOCKET L409 D5):** when `regularMarketPrice` was absent, `price` fell back to `previousClose`. Because `prev` was also `previousClose`, the row printed `🟢 … (+0.00%)`, which is yesterday's close shown as live and green. No as-of time was read.

**Diff summary:**
- New `_num()` treats a price as absent when it is None, 0, NaN, inf or non-numeric. Negative prices are kept.
- New `_asof_tag()` reads `regularMarketTime` as epoch seconds and converts it to a date in America/New_York.
- `fmt(ticker, info, today=None)`: call sites are unchanged, and `today` is injected only by the selftest.
- The bare `except:` is narrowed to `except Exception`.
- New `--selftest` mode needs no network. It runs without yfinance: the import guard skips the exit-2 only when `--selftest` is in argv.

| Case | Row |
|---|---|
| live, as-of today | unchanged: `  🟢 WAL      $     76.26  (+0.87%)` |
| live price absent / 0 / NaN, prev present | `  ⚪ WAL      $     75.60  ⚠prev-close` (no %, no arrow, no as-of tag) |
| as-of NY date ≠ today | `…(+0.87%)  ⚠stale 2026-09-22` |
| `regularMarketTime` missing on a live row | `…  ⚠no-asof` (**fail closed**; live smoke showed yfinance supplies it on every row sampled: WAL OZK KRE EGBN DX-Y.NYB CL=F ^TNX ^VIX) |
| `regularMarketTime` unparseable | `…  ⚠asof-unreadable` |
| live and prev both absent | `  ⚪ WAL      (no data)` (was `$      0.00`) |
| live present, prev absent | `  ⚪ WAL      $     76.26` (as before) + as-of tag if not today |

**Capable case: defect fixture `{"previousClose": 75.6}`:**
```
OLD:   🟢 WAL      $     75.60  (+0.00%)
NEW:   ⚪ WAL      $     75.60  ⚠prev-close
```
**Selftest (`.venv/bin/python3 scripts/market.py --selftest`) → 14/14 PASS, rc=0.** The same result holds under bare python3 with yfinance absent and the venv re-exec suppressed. The cases cover C1 ×2, C2 ×2 (incl. 23:30 NY 9/23 = 03:30 UTC 9/24 → stale 9/23, which proves the NY tz is used rather than UTC), C3 ×2, and C4 ×8.

**FAIL path watched:** swapping the pre-fix `fmt()` into the selftest gives **4/14 PASS, rc=1**. The FAIL lines include `🟢 WAL $ 75.60 (+0.00%)` against the wanted `⚠prev-close`, `$ nan (+nan%)` for NaN, and `$ 0.00` for no-data.

**Clean case / live-row byte identity:** OLD and NEW `fmt()` are IDENTICAL on three live-today fixtures. Live smoke at 2026-09-24 16:50 EDT: `quote WAL OZK CL=F ^TNX` → rc 0, all 4 rows in the original format with no tag. The default watchlist → rc 0, 40 lines, **0 `⚠` tags, 0 errors/no-data**.

**rc contract:** the `quote`/watchlist paths and the exit-2 on a missing yfinance are unchanged: `ERROR: yfinance not importable …` rc=2 was re-verified. New: `--selftest` returns rc 0 when all cases pass and 1 when any fails.

## Residue
- **Weekends/holidays:** every live row will carry `⚠stale <last session date>`. This is accurate: the quote is not today's. Consumers (WAL · OZK · REGINALD · POSITIONS) should expect it. Team-lead notifies them.
- The prev-close row carries no as-of tag, because `⚠prev-close` already marks it as not live. A prev-close that is days old is not dated.
- `_num()` treats a price of exactly 0 as absent. This is correct for the current watchlist and would be wrong for an instrument that can genuinely print 0.00.
- There is a pre-existing wording issue, left untouched: the no-yfinance error says "no repo .venv found" even when the venv exists but the re-exec was suppressed.
- Nothing is committed. The owner must commit `scripts/safe-push.sh`, `scripts/market.py` and this record path-scoped.
