# L460 / L409 D5 — `scripts/market.py` previousClose fallback: completion record (2026-10-01)

**Session:** DAEDALUS spawned by PROME `prome-0c` (WQ-184 due row, DOCKET L460, due 9/30). **Finding at boot:** the repair had **already landed on 2026-09-24** in `92a7c5354` (build record `runs/2026-09-24_SAFEPUSH_MARKET_BUILD.md`). PROME was told in the 9/24 delivery memo (`PROME/inbox/processed/2026-09-24_from-DAEDALUS_catch-up-…md`, row 22). The three consumer notes went to WAL and OZK (9/24 packets) and REGINALD (Staleness #5 packet). **L460 has stayed PENDING because the consume step was never done, not because the work was missing** (`finding_directive_overtaken_between_authorship_and_delivery`). No code was edited this session.

## Acceptance conditions (PROME's, packet 2026-09-23; the test set)
1. When the live price is absent and `previousClose` is used, the row prints `⚪ TICKER $x ⚠prev-close` with no % and no arrow.
2. When `regularMarketTime`'s NY date is not today, the row prints `⚠stale <date>`.
3. A normal live row is byte-identical to the old output.
4. Neighbours: ordinary · overlap · wrong owner · missing info · concurrent.

## Four states (WQ-229, kept separate)
| State | Evidence |
|---|---|
| **IMPLEMENTED** | `92a7c5354` 2026-09-24 17:24 ET, `fmt()` / `_num()` / `_asof_tag()` + `--selftest` |
| **TESTED** | Author suite re-run 2026-10-01 12:15 ET: `.venv/bin/python3 scripts/market.py --selftest` → **14/14 PASS rc=0**. Live smoke 12:15 ET in market hours: `quote WAL OZK CL=F ^TNX` → 4 rows, original format, no tags. 9/24: the FAIL path was watched (old `fmt()` gave 4/14). |
| **INDEPENDENTLY VERIFIED** | **PASS-WITH-RESIDUE, 0 ❌.** An independent Opus reader on 2026-10-01 wrote **30 counterexamples of its own** and did not re-run the author's suite. It ran 10,000 random live same-day rows through the old and new `fmt()` with **0 differences** (condition 3). It confirmed live that yfinance 1.2.0 sends `regularMarketTime` as integer epoch seconds, and that both the watchlist and `quote` paths go through `fmt()`. Its ledger is reproduced below. |
| **STILL UNRESOLVED** | The residue list below. None of it breaches a condition. R1 and R6 are owed as a **new episode**; nothing is fixed in this session (Review budget: a fix after the final read would go unreviewed). |

## Residue (declared, not fixed)
| # | Shape | Severity / owner call |
|---|---|---|
| R1 | Live price == prev close and the as-of is yesterday ⇒ `🟢 WAL $75.60 (+0.00%)  ⚠stale 2026-09-30`. Condition 2 is met, but the row still has the defect's LOOK (a flat green line), and only the trailing tag warns. | ⚠️ Next repair episode: a stale row should drop the arrow, or print ⚪. PROME may treat this as an amendment to condition 2. |
| R2 | A negative prev close flips the arrow and sign (−20→−10 prints 🔴 −50%). This is pre-existing maths. | Low. Only reachable at negative prices. |
| R3 | `True` prints as `$1.00` and `1e-9` prints as `$0.00`. | Not reachable from yfinance. |
| R4 | A future-dated as-of (a clock fault) is labelled `⚠stale`. | The word is wrong, but the row is still flagged. |
| R5 | When `regularMarketPrice` is absent, a live `currentPrice` is ignored and the row is shown as `⚠prev-close`. | This fails in the safe direction (it understates). |
| R6 | **`options_chain()` prints `lastPrice` without going through `fmt()` and with no date check.** An illiquid strike's last trade can be days old. This is the same class of defect outside the D5 perimeter. | ⚠️ Owed: a new episode, with acceptance conditions written first. Its consumers are the desks that call `market.py` with an options argument. |
| R7 (9/24) | A price of exactly 0 is treated as absent, and the no-yfinance error wording is pre-existing. | As stated in the 9/24 record. |

---
## Independent reader ledger (verbatim from the reader's scratch file, 2026-10-01)
# Independent read: scripts/market.py @ 92a7c5354 (HEAD content unchanged since; `git diff 92a7c5354` empty)
Reader: independent, read-only · 2026-10-01 ~12:20 ET · harness: scratchpad/cx.py (fmt() driven directly, today=date(2026,10,1) unless noted)
Author suite: `--selftest` 14/14 PASS (re-run only as a smoke check, not as evidence).

## Source + bypass check (VERIFIED)
- `info` = `yf.Tickers(...).tickers[sym].info` (yfinance 1.2.0). Live probe 12:16 ET: `regularMarketTime` is `int` epoch SECONDS for WAL, CL=F, ^TNX, DX-Y.NYB; `currentPrice` None on non-equities.
- Watchlist and `quote` paths both go through fmt(); their except branch prints `(error: …)`, no price. Live `python3 scripts/market.py quote WAL CL=F` (bare python3, venv re-exec) -> untagged live rows in-session, rc 0.
- BYPASS: `options_chain()` prints chain `lastPrice` with no as-of — never goes through fmt(). Out of the stated conditions' scope, same defect class (illiquid strike lastPrice can be days old).
- C3 differential: pre-fix fmt (4e27100f2) vs new fmt over 10,000 random live/today rows, 5 tickers incl. 8-char `DX-Y.NYB`: 0 mismatches.

## Counterexamples (input · exact repr · verdict)
| # | input (price / prev / regularMarketTime) | output | verdict |
|---|---|---|---|
| X1 | "76.26" / "75.6" (strings) / today 16:00 | `'  🟢 WAL      $     76.26  (+0.87%)'` | ✅ float() coerces; pre-fix would have crashed to (no data) |
| X2 | 76.26 / 75.6 / today in MILLISECONDS | `'… (+0.87%)  ⚠asof-unreadable'` | ✅ fails closed (marked); source is seconds anyway |
| X3 | 76.26 / 75.6 / ISO string today | `'… (+0.87%)  ⚠asof-unreadable'` | ✅ fails closed |
| X4 | 76.26 / 75.6 / datetime obj today | `'… (+0.87%)  ⚠asof-unreadable'` | ✅ fails closed (false alarm, safe direction) |
| X5 | 76.26 / 75.6 / str(epoch) today | `'  🟢 WAL      $     76.26  (+0.87%)'` | ✅ |
| X6 | 75.6 / 75.6 / yesterday 16:00 (live == prev, stale) | `'  🟢 WAL      $     75.60  (+0.00%)  ⚠stale 2026-09-30'` | ⚠️ C2 met (tagged), but yesterday's close still renders flat GREEN with a % — the defect's exact visual, rescued only by a trailing tag |
| X7 | 76.26 / 75.6 / yesterday (off-hours fill, prev = day-before) | `'… (+0.87%)  ⚠stale 2026-09-30'` | ✅ stale tagged |
| X8 | absent / 75.6 / today; currentPrice 77.0, post/preMarket set | `'  ⚪ WAL      $     75.60  ⚠prev-close'` | ✅ C1; ⚠️ minor: a live currentPrice is ignored (under-claims, safe direction) |
| X9 | True / 75.6 / today | `'  🔴 WAL      $      1.00  (-98.68%)'` | ⚠️ bool accepted as $1.00 live price (unrealistic from yfinance) |
| X10 | 76.26 / 75.6 / True | `'… (+0.87%)  ⚠stale 1969-12-31'` | ✅ marked (odd date) |
| X11 | 76.26 / 75.6 / 0 | `'… (+0.87%)  ⚠stale 1969-12-31'` | ✅ marked; 0 not treated as absent here (inconsistent with _num, harmless) |
| X12 | 76.26 / 75.6 / NaN | `'… (+0.87%)  ⚠asof-unreadable'` | ✅ |
| X13 | 76.26 / 75.6 / TOMORROW 10:00 | `'… (+0.87%)  ⚠stale 2026-10-02'` | ⚠️ future stamp (clock skew) labelled "stale" — marked, word wrong |
| X14 | today 23:59:59 NY | `'  🟢 WAL      $     76.26  (+0.87%)'` | ✅ |
| X15 | today 00:00:00 NY | `'  🟢 WAL      $     76.26  (+0.87%)'` | ✅ |
| X16 | yesterday 23:59:59 NY | `'… (+0.87%)  ⚠stale 2026-09-30'` | ✅ midnight boundary correct |
| X17 | info = None | `'  ⚪ WAL      (no data)'` | ✅ |
| X18 | 76.26 / prev "0", regularMarketPreviousClose 75.6 | `'  🟢 WAL      $     76.26  (+0.87%)'` | ✅ fallback works |
| X19 | -10.0 / -20.0 / today (negative regime, price ROSE) | `'  🔴 WAL      $    -10.00  (-50.00%)'` | ⚠️ arrow/sign inverted when prev < 0 (pre-existing math; selftest blesses negative live) |
| X20 | Decimal / Decimal / today | `'  🟢 WAL      $     76.26  (+0.87%)'` | ✅ |
| X21 | "nan" / 75.6 / today | `'  ⚪ WAL      $     75.60  ⚠prev-close'` | ✅ |
| X22 | None / 75.6 / missing | `'  ⚪ WAL      $     75.60  ⚠prev-close'` | ✅ |
| X23 | absent / None / regPrev 0 | `'  ⚪ WAL      (no data)'` | ✅ |
| X24 | 76.26 / 75.6 / today (C3 string) | `'  🟢 WAL      $     76.26  (+0.87%)'` | ✅ byte-identical to C3 |
| X25-27 | time 1e20 / -1 / [epoch] | `asof-unreadable` / `stale 1969-12-31` / `asof-unreadable` | ✅ all marked |
| X28 | 1e-9 / 75.6 / today | `'  🔴 WAL      $      0.00  (-100.00%)'` | ⚠️ sub-cent non-zero passes _num, prints $0.00 live (unrealistic) |
| X29 | today=None, time=now | `'  🟢 WAL      $     76.26  (+0.87%)'` | ✅ default-today path |
| X30 | today passed as datetime (caller misuse) | `'… (+0.87%)  ⚠stale 2026-10-01'` | ⚠️ every row false-stale; unreachable from main() (today=None) |

## Not covered by the conditions (observations)
- Prev-close rows (C1) carry no date — reader cannot tell WHICH day's close; not required by C1.

## Overall verdict: PASS-WITH-RESIDUE
No ❌: no input made fmt() show a non-live price unmarked, break a normal live row, or crash.
Residue (⚠️): X6 stale flat-green arrow+% retained behind a tag · X19 inverted arrow when prev < 0 · X9 bool / X28 sub-cent accepted as live · X13 future stamp called "stale" · X8 currentPrice ignored · options_chain() lastPrice bypasses fmt() with no as-of.
