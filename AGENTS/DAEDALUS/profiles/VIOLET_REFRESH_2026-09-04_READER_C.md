# VIOLET Profile Refresh — Cluster C (quant engine: `scripts/` + `workbook/`)

DAEDALUS Mode-A reader C · 2026-09-04 (Fri) · `AGENTS/VIOLET/scripts/` (34 py) + `workbook/` (19 data files). Read-only; only `--help`/`--selftest` executed.

## 1. Script inventory

**B**=`boot.py` stage · **C**=`closeout_guard.py` · **M**=`VIOLET/CLAUDE.md` step · **—**=no invocation site.

| File | Purpose | Reads | WRITES | Invoked by | selftest | commit |
|---|---|---|---|---|---|---|
| `boot.py` | 14-stage orchestrator, collapsed brief | subprocess | — | **M** `CLAUDE.md:26-28` | no | 08-04 |
| `closeout_guard.py` | 5 blocking + 1 advisory contract | subprocess | — | **M** `CLAUDE.md:58` | no | 09-04 |
| `thresholds.py` | Live vol dashboard + append | yf + vix_futures CLI | `VX_DAILY.tsv` `:244-249` | **B** `:33` | no | 08-27 |
| `fred_fetch.py` | FRED pull + credit-gate verdict | FRED `:93` | `fred_cache/*` `:115` | **B** `:34` | no | 08-04 |
| `vix_options.py` | VIX chain OI/vol snapshot | yf chain `:43` | `VIX_OPTIONS.tsv` `:29` | **B** `:35` | no | 07-30 |
| `cftc_cot.py` | CFTC TFF VIX positioning | cftc.gov `:38-39` | `COT_VIX.tsv` `:193` | **B** `:36` | no | 06-01 |
| `move.py` | MOVE rates-vol | investing `:65`, yf `:114` | `MOVE.tsv` `:141` | **B** `:42` | no | 09-04 |
| `jpy_vol.py` | JPY carry canary (RV + FXY IV) | `JPY=X`,`FXY` `:75,119` | `JPY_VOL.tsv` `:53` | **B** `:43` | no | 07-30 |
| `ovx.py` | OVX/VIX transmission canary | `^OVX`,`^VIX` `:75-76` | `OVX.tsv` `:50` | **B** `:44` | no | 07-30 |
| `cheap_tail.py` | 4-leg cheap-tail alert | yf `:90-92`, CATALYSTS `:66` | `CHEAP_TAIL.tsv` `:65` | **B** `:45` | no | 07-30 |
| `implied_corr.py` | Implied correlation | CBOE json `:62`, yf `:73` | `IMPLIED_CORR.tsv` `:52` | **B** `:46` | no | 07-30 |
| `catalyst_countdown.py` | Countdown table | `CATALYSTS.tsv` `:21` | — | **B** `:47` | no | 09-04 |
| `canary_staleness.py` | CANARY_MAP staleness (2 legs) | 5 ledgers `:52-59`, MAP `:176` | — | **B** `:52` + **C** `:68` | **YES** `:404` | 09-04 |
| `validate_workbook.py` | KB enums vs SCHEMA | `KB/SCHEMA.tsv` `:48` | — | **B** `:57` + **C** `:70` | no | 07-30 |
| `grading_note_check.py` | Notes citing retracted KB | `CATALYSTS`,`KB` `:50-51` | — | **B** `:61` + **C** `:69` | no | 08-04 |
| `thesis_bump_check.py` | Thesis version vs KB findings | thesis, `KB.tsv` `:51-52` | — | **B** `:65` + **C** adv `:75` | no | 08-04 |
| `writeback_order_check.py` | Handoff surfaces vs STATUS | git commit times `:71-91` | — | **C** `:71` | no | 09-04 |
| `twin_check.py` | CALENDAR ⇄ CATALYSTS | `:45-46` | — | **C** `:72` | no | 09-04 |
| `_daily_log.py` | Shared upsert lib | — | caller ledger `:132` | library (4 canaries) | via test | 07-30 |
| `test_daily_log.py` | 11-case test of `upsert_row` | tmp fixtures | tmpdir only `:121` | **—** | is the test | 09-04 |
| `skew_integrity.py` | `^SKEW` yf-vs-CBOE value check | CBOE `:50`, yf `:74` | — | **—** (by design) | no | 09-04 |
| `backfill.py` | Historical VX_DAILY repair | CBOE `:49,273`, yf `:91` | `VX_DAILY.tsv` `:66` | **—** manual | no | 08-27 |
| `vx_history.py` | CBOE per-expiry term history | CBOE `:68` | `VX_TERM_HISTORY.tsv` `:162` | **—** manual | no | 08-04 |
| `convergence_score.py` | Convergence-matrix sum | `STATUS.md` `:22` | — | **—** | no | 06-11 |
| `convexity_read.py` | Convexity-pricing rubric | yf `:112-120` | — | **—** | no | 06-10 |
| `h3_basis_lead.py` | H3 basis vs index ratio | yf `:71`, CBOE | — | **—** research | no | 07-30 |
| `sustain_run_query.py` | Close-and-hold run lengths | `DIET…csv:52`, yf `:56` | — | **—** research | no | 06-10 |
| `two_anchor_ladder.py` | Two-anchor level ladder | `DIET…csv`, yf `:62` | — | **—** research | no | 06-10 |
| `diet_coiled_spring.py` | 19-yr DIET/STRICT backtest | yf `:60` | `DIET_COILED_SPRING.csv` `:167` | **—** research | no | 06-01 |
| `feb2018_m1m2.py` | Feb-2018 M1:M2 analog | CBOE `:42` | `FEB2018…csv` `:103` | **—** research | no | 06-01 |
| `skew_trajectory.py` | Post-fire SKEW trajectory | `vix_historical.csv:55`, yf | `research/…md:510` | **—** research | no | 04-16 |
| `regime_termination.py` | What ended SKEW regimes | `vix_historical.csv:41` | `research/…md:468` | **—** research | no | 04-16 |
| `analog_pull.py` | 2024-cluster daily frame | yf `:29` | `research/analog_2024_cluster/daily.csv:105` | **—** research | no | 04-16 |
| `analog_timeline.py` | 2024-cluster tell table | `…/daily.csv:12` | `…/tells_table.md:134` | **—** research | no | 04-16 |

**Unowned in practice (3)** — the other 11 un-invoked scripts are correctly DELIBERATE (one-shot research derivations, manual repair tools):
- `test_daily_log.py` — the desk's only test, in no boot/closeout/CLAUDE.md step. That is how its own wall-clock bug survived 9 days (`test_daily_log.py:22-28`).
- `skew_integrity.py` — deliberately not a boot check, but nothing else invokes it either ⇒ ritual, not mechanism.
- `convergence_score.py` — built because the hand-sum was wrong twice in 48h (`:12-15`); now in no step.

**Ledger written that nothing reads:** `VX_TERM_HISTORY.tsv` (`vx_history.py:162`; no reader in `scripts/`).

## 2. `boot.py` — the 14 checks

Verdict **dual-keyed, keys disagree**: the brief filters on 60 `KEY_MARKERS` (`:68-88`, `collapse():111-112`); the SUMMARY ✅/❌ keys on rc (`:104,157`).

| Stage (`boot.py:`) | PASS proves | Cannot see |
|---|---|---|
| thresholds `:33` | yf returned the 5 spot series; row hit `VX_DAILY` | omitted / value-disagreeing yf bars (§5) |
| fred_fetch `:34` | cache reachable, gate verdict rendered | revisions; cache staleness not rc-gated |
| vix_options `:35` | chain fetched, row appended | chain truncation (`except` `:52,59`) |
| cftc_cot `:36` | freshness-gated fetch | nothing — rule lives in `canary_staleness:100-110` |
| move `:42` | primary parsed **or** labelled fallback printed | **rc=0 on primary failure w/o `--strict`** (`move.py:163`) ⇒ ✅ while MOVE is uncorroborated |
| jpy_vol `:43` | RV spine computed, IV leg attempted | legitimate IV absence (OI≥100 guard) |
| ovx `:44` | ratio + pctiles re-derived each run | oil-vol substance (correctly BRENT/HAWK) |
| cheap_tail `:45` | 4-leg state computed + logged | `^SKEW` integrity — L3 is the self-healing-omission series |
| implied_corr `:46` | `^COR*` pulled, basis stamped | CBOE-vs-yf disagreement (`except` `:66,74` silent) |
| catalyst_countdown `:47` | CATALYSTS parses, renders | whether a row's DATE is right (`twin_check`, closeout only) |
| canary_staleness `:52` | 5 ledgers inside 2× cadence + no MAP cell >4d | year-rollover dates (§7-3); a fresh-but-wrong value |
| validate_workbook `:57` | KB enums/IDs/refs conform | truth of the Fact cell |
| grading_note_check `:61` | no note cites a retracted KB row | a wrong note citing nothing |
| thesis_bump_check `:65` | thesis version vs KB counter | semantic contradiction (stated, `closeout_guard:53-56`) |

**Dead-on-arrival class: none** — every stage's subject list is a literal (`BOOT_SEQUENCE:31-66`, `CANARIES:52-59`); no enumerator can exclude a subject. **Two fail-open paths:** `:92-93` a missing script returns a `SKIP:` string with no KEY_MARKER; `:147-156` a crashed script whose stderr carries no marker prints **`✓ ran cleanly, no alerts`** while the ❌ sits 40 lines lower. The line read at boot is the wrong one.

## 3. `closeout_guard.py` — 5 blocking + 1 advisory

| Contract | Script/args | Both paths tested | Fail direction |
|---|---|---|---|
| CANARY_MAP staleness | `canary_staleness --strict` `:68` | **Yes** — 13-case `--selftest`, ran rc=0 today | closed on data; **OPEN** if `CANARY_MAP.md` missing (`canary_staleness:177`) |
| Grading-note citations | `grading_note_check --strict` `:69` | no | closed |
| KB schema conformance | `validate_workbook` `:70` | no | closed |
| Write-back ordering | `writeback_order_check --quiet` `:71` | no | **open by design** — vintage only (`closeout_guard:49-50`); a dirty file is stamped `now` `:86` and passes |
| CALENDAR/CATALYSTS twin | `twin_check --quiet` `:72` | no | closed; refuses to name a winner `:41-44` |
| Thesis currency (ADVISORY) | `thesis_bump_check` `:75` | no | never blocks `:109-113`, deliberate `:53-56` |

⛔ **All five fail OPEN on file absence:** `run():81-82` returns `(0, "(skipped — … not present)")` ⇒ a renamed/trashed check yields `✓ All blocking contracts green` `:122`, exit 0. ⚠️ `PY=sys.executable:65` vs boot's `VENV_PY:29` — outside `.venv` subscripts import-fail (blocks; safe direction, wrong message).

## 4. Workbook (19 data files)

**No file carries a `Last real data refresh:` header** (0 hits under `AGENTS/VIOLET/`). **No `workbook/LEDGER_GLOB`** ⇒ root closeout step 1c-bis has nothing to nudge on.

| Ledger | rows | bytes | cadence | last row | banner | writer | reader |
|---|---|---|---|---|---|---|---|
| `KB.tsv` | 243 | 548,743 | per-finding | KB-VIO-243 09-04 | — | hand | 3 checks |
| `VX_DAILY.tsv` | 412 | **32,656** | EOD (4d) | 2026-09-04 | — | `thresholds:249`,`backfill:66` | `:53-55` |
| `VX_TERM_HISTORY.tsv` | 28,582 | 988,592 | none | **2026-08-03 (32d)** | — | `vx_history:162` manual | **NONE** |
| `VX_M1_HISTORY.tsv` | 248 | 15,008 | none | **2026-07-29 (37d)** | — | **NONE** | **NONE** |
| `VIX_OPTIONS.tsv` | 175 | 24,263 | daily | 2026-09-04 | — | `vix_options:29` | **no automated reader** |
| `COT_VIX.tsv` | 192 | 25,073 | weekly+grace `:100-110` | 2026-09-01 | — | `cftc_cot:193` | `:60` |
| `CHEAP_TAIL.tsv` | 16 | 3,196 | EOD (4d) | 09-04 `4/4 OPEN` | — | `cheap_tail:65` | `:58` |
| `OVX.tsv` | 17 | 1,870 | EOD (4d) | 09-04 `WATCH` | — | `ovx:50` | `:57` |
| `JPY_VOL.tsv` | 18 | 2,794 | EOD (4d) | 09-04 `CALM` | — | `jpy_vol:53` | `:56` |
| `MOVE.tsv` | 44 | 1,480 | every boot (`CLAUDE.md:176`) | 09-03 (`stale` in-row) | — | `move:141` | **not in CANARIES** |
| `IMPLIED_CORR.tsv` | 11 | 2,083 | every boot | 2026-09-04 | — | `implied_corr:52` | **not in CANARIES** |
| `CATALYSTS.tsv` | 5 | 3,930 | at closeout | fwd to 09-30 | — | hand | 4 scripts |
| `FLOW.tsv` | 28 | 21,426 | formal sends | 2026-09-02 | — | **hand, no script** | none |
| `SCHEMA.tsv` | 13 | 1,829 | static | — | — | hand (04-12) | `validate_workbook:48` |
| `DIET_COILED_SPRING.csv` | 83 | 18,132 | static | 2026-04-13 | README-exempt | `diet_coiled_spring:167` | 2 scripts |
| `FEB2018…M1M2.csv` | 37 | 1,688 | static | 2018-02-23 | README-exempt | `feb2018_m1m2:103` | none |
| `combined_vix_credit.csv` | 2,020 | 214,676 | — | 2026-04-09 | **FROZEN 07-11** | — | none |
| `hy_oas_fred.csv` | 7,739 | 123,929 | — | 2026-04-09 | **FROZEN 07-11** | — | none |
| `vix_historical.csv` | 2,079 | 645,998 | — | **2026-04-10 (147d)** | **none** | hand | `skew_trajectory:55`,`regime_termination:41` |

**Flags** — *No writer:* `VX_M1_HISTORY`, `FLOW`, `vix_historical.csv`, both FROZEN CSVs. *No reader:* `VX_TERM_HISTORY`, `VX_M1_HISTORY`, `VIX_OPTIONS`, `FEB2018…`, both FROZEN CSVs. *Past cadence:* `VX_M1_HISTORY` 37d, `VX_TERM_HISTORY` 32d, `vix_historical.csv` 147d — none in `CANARIES:52-59`, none bannered ⇒ the silent-rot middle the root two-state rule forbids. *Outside the contract:* `MOVE.tsv` + `IMPLIED_CORR.tsv` are boot-cadence with no `CANARIES` row; MOVE already produced a five-session silent failure (`move.py:5-10`). *>32,550 B:* `KB.tsv`, `VX_TERM_HISTORY`, `vix_historical.csv`, `VX_DAILY.tsv` — **none is a boot whole-read** (`CLAUDE.md:47`; the rest are touched only through scripts). **No read-cap breach in this cluster.**

## 5. Instrument mirrors

| Series | Puller | Fallback | In output? | In rc? | Value-level check |
|---|---|---|---|---|---|
| `^SKEW` | `thresholds:87/128`, `cheap_tail:92`, `convexity_read:114` | CBOE CSV — only inside `skew_integrity:50` | n/a | n/a | **YES `skew_integrity.py`** (omission + disagreement, rc 0/1/2 `:115,122,159`) — **wired to no puller** |
| `^VIX/^VIX3M/^VIX6M/^VVIX` | `thresholds:87-130` | tick→settle retry `:96,130` | partial | **no** (silent `except`) | none |
| `^MOVE` | `move:114` | investing.com PRIMARY `:65`; yf is the fallback | **YES** `⚠️ FALLBACK [UNCORROBORATED…]:163` | **NO on the boot path** — `return 1 if a.strict else 0` `:163`; `boot.py:42` passes only `--boot` | shared-bar delta `:173-175` |
| `^OVX` | `ovx:75` | none | `except` `:163` | rc≠0 | none |
| `JPY=X`/`FXY` | `jpy_vol:75/119` | IV leg optional, thin-strike guard | YES (ledger leg note) | no | none |
| `^COR1M/3M/30D` | CBOE json `implied_corr:62` → yf `:73` | **silent two-stage** `except` `:66,74` | **NO** | **no** | none |
| VIX chain | `vix_options:43` | per-expiry `except` `:52,59` | partial | partial | none |
| CBOE VX settles | `backfill:49`,`vx_history:68`,`feb2018:42` | none | raises | rc≠0 | none |
| FRED | `fred_fetch:93` | merge-on-write cache `:111` | silent | no | none |
| CFTC TFF | `cftc_cot:38-39` | annual-zip backfill | yes | yes | none |

`move.py` is the only mirror whose fallback is *labelled* in output — and its rc is silent on the wired path (§7-2). `implied_corr:62-74` is the worst case: a CBOE→yf switch with no trace in output, rc or ledger. **`skew_integrity.py` is the model; it covers 1 of 10 mirrors.**

## 6. Test coverage

- `test_daily_log.py` — 11 cases over `upsert_row`, both directions (`:5-9`): header write, supersede, null-preserve, skip-exists, mid-file order, ragged-row tolerance `:120-125`, today-only guard.
- **Wall clock:** mostly fixed — `:22-28` records that a fixture dated 2026-07-30 with no `today=` passed *only on 2026-07-30* and had failed 9 days (DAEDALUS 2026-09-03). Cases 2–5,7,8 now pin `today=`. **Cases 1 (`:56`) and 6 (`:106-107`) still omit it** — clock-independent only because the append path returns at `_daily_log:130-133`, before the clock read at `:165`: luck of the code path, not construction.
- `canary_staleness --selftest` — 13 assertions, rc=0 today; the desk's only selftest. Its docstring `:81-83` states a selftest cannot falsify the premise it was derived from (v2 and v3 both passed their own).
- **Untested:** the other 32 scripts — incl. 4 of the 5 blocking closeout contracts, every ledger writer, and `skew_integrity.py` itself.

## 7. TOP 5

| # | Item | Line | Failure risked | Owner |
|---|---|---|---|---|
| 1 | **All 5 blocking closeout contracts fail OPEN on file absence** | `closeout_guard.py:81-82` | A renamed/moved/trashed check makes the guard print `✓ All blocking contracts green` (`:122`) and exit 0 — the guard built *because* detection wasn't converting to action certifies health it never checked (PAT-074). Fix: missing ⇒ RED, or rc=2 CANNOT-CERTIFY. | VIOLET desk |
| 2 | **`boot.py` prints `✓ ran cleanly, no alerts` for a crashed stage** | `boot.py:111-112`, `:147-156` (+`:92-93`) | Stderr with no KEY_MARKER collapses to the clean line; ❌ sits in a separate block below. Compounded by `move.py:163` returning **0** on primary failure under `--boot` (`boot.py:42` passes no `--strict`) ⇒ MOVE dark reads ✅ — one flag from re-running the five-session failure `move.py:5-10` exists to end. Fix: `--strict` at `:42`; print `⚠️ rc=N, no recognised markers`. | VIOLET desk |
| 3 | **CANARY_MAP leg is blind across the year boundary; fails open if the map is gone** | `canary_staleness.py:207`, `:176-177` | `date(today.year, mon, day)` on a `Current [12/28]` cell read 2026-01-02 gives `age=-360` ⇒ never fires `:210`: the leg goes dark ~2 weeks every New Year, on the file with four documented stale-`CURRENT` incidents. Missing `CANARY_MAP.md` returns clean. Fix: pick the year minimising \|age\|, flag negatives; missing-map ⇒ RED. | VIOLET desk |
| 4 | **`skew_integrity.py` covers 1 of 10 mirrors and has no invocation site** | `skew_integrity.py` (B=0,C=0); `cheap_tail.py:90-92`; `implied_corr.py:62-74` | "Run at the moment of use" is a ritual with no mechanism (`finding_mechanize_the_cap_not_the_ritual`). Acute at `cheap_tail:92` — L3 consumes `^SKEW`, the self-healing-omission series, unchecked, on an operator-decision surface reading `4/4 OPEN` (9/2–9/4). Second: `implied_corr:62-74` degrades CBOE→yf with no trace in output, rc or the `source` column. Fix: call `skew_integrity` from `cheap_tail` and stamp the verdict in the row; record the implied-corr fallback in `source`. | VIOLET desk (+ DAEDALUS: promote as mirror standard) |
| 5 | **Three historical files in the silent-rot middle; no `LEDGER_GLOB`** | `VX_M1_HISTORY.tsv` 37d (no writer, no reader) · `VX_TERM_HISTORY.tsv` 32d/988,592 B (`vx_history:162`, no reader) · `vix_historical.csv` 147d (un-bannered while both siblings carry FROZEN) · absent `workbook/LEDGER_GLOB` | Neither FROZEN nor LIVE-with-alert (root §Data Hygiene). `vix_historical.csv` feeds `skew_trajectory:55` + `regime_termination:41` — a rerun today silently emits a 2018→2026-04 study labelled current. No `LEDGER_GLOB` ⇒ step 1c-bis nudges on nothing. Also add `MOVE.tsv`/`IMPLIED_CORR.tsv` to `CANARIES:52-59`. | VIOLET desk · DAEDALUS (LEDGER_GLOB = fleet gap) |
