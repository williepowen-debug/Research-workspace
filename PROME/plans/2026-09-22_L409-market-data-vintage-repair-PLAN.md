# L409 — FORGE market-data vintage + fallback repair — PLAN (acceptance conditions first)

**Author:** PROME `prome-a5` · **Written:** 2026-09-22 18:4x ET · **Status:** PLAN, no code edited · **Due:** DOCKET L409 2026-09-24
**Class:** WQ-229 consequential (gate instruments + a shared contract with ≥6 fleet callers). Sequence: acceptance conditions (this file) → blind plan read → edit → tests → an independent result reader who brings its own counterexample → only then "fixed". This PLAN carries no claim that anything is fixed.

## What was re-measured today (2026-09-22 18:3x ET), before writing anything

| Claim on the row | Today's check | Result |
|---|---|---|
| `fetch.py fred` lags the API by ≥3 observations (9/17 instance) | `fetch.py fred DGS10/WRESBAL/BAMLH0A0HYM2` vs a direct FRED API call in the same minute | **NOT REPRODUCED.** The tool's newest rows (4.96 [9/21] · 3,013,794 [9/16] · 2.68 [9/18]) match the API. ⚠️ PROME first read the output as one row behind. That was PROME's own `tail -4` cutting off the newest line, not the tool. The 9/17 instance stays **UNEXPLAINED**. It may be the same reader error; that is INFERRED, not shown. The acceptance condition from it stays in (A5). |
| `fred_fetch` sends no `realtime_*`, so it returns latest-revised values | `fetch.py:330-357` params | **CONFIRMED** at the artifact: only `series_id`, `api_key`, `file_type`, `sort_order` and `limit` are sent. |
| `scripts/market.py` falls back silently to `previousClose` and takes no date | `scripts/market.py:26-36` `fmt()` | **CONFIRMED**: `price = regularMarketPrice or previousClose`, with no as-of and no stale mark. |
| Off-RTH fill-forward is not flagged on `dashboard.py` (WALTER SIG-W-20260919-001) | `dashboard.py:141-150` and `_date_stamp` at :250 | **CONFIRMED in mechanism**: yfinance entries carry `date=asof`, but `_date_stamp` is documented for FRED only, and nothing marks `asof != today` or a zero change on a vol mark. `fetch.py price` does mark `⚠stale` (:1257/:1376), so the two surfaces disagree. |
| 🆕 not on the row: `fred_spread` dates a two-leg spread by leg A only | `dashboard.py:167-172` | **FOUND TODAY.** `entry["date"] = obs_a[0]["date"]` is taken without checking that `obs_b[0]["date"]` matches. Two legs on independent clocks produce one mixed-date figure (`[[finding_two_legs_with_independent_vintage_clocks_mix_dates_invisibly]]`). |

## Acceptance conditions — the test list, in the defects' own terms

**A1 — basis is explicit, never implied.** Every `fred_fetch` result states which basis it holds: `latest-revised` (current default behaviour) or `first-published` (ALFRED `realtime_start`/`realtime_end`/`output_type` request). A caller that declares first-published gets first-published values, or an explicit error. It never silently gets latest-revised.

**A2 — default behaviour for existing callers is unchanged.** The six callers found by grep (LIQUID gate069_legs / sofr_dispersion / t3_decoupling / hy_oas_watch; LABOR indeed_lead_test; dashboard.py) get the same values as before unless they opt in. LIQUID's `hy_oas_watch.py`, rebuilt today with its own first-published path, is not broken or double-converted.

**A3 — the cache cannot cross bases.** A first-published result is never served to a latest-revised caller or the reverse: the basis is part of the cache key. A cached result also carries its basis.

**A4 — no silent price fallback.** `market.py` never shows `previousClose` as a live price without saying so. When the price is a fallback, or its as-of is not today, the row is marked (`⚠prev-close` / `⚠stale <date>`).

**A5 — freshness.** For a daily FRED series, the tool's newest observation is never older than the API's newest by more than one publication day. The test is a same-minute comparison, run with the output read whole (see today's reader error).

**A6 — dashboard stale marks match fetch.py.** A yfinance entry whose `asof` is not today shows `⚠stale <date>` on the dashboard, exactly as `fetch.py price` does. A vol-index mark (^VIX, ^VVIX, ^MOVE, ^SKEW, ^OVX) with |Δ| below its reporting resolution is flagged `⚠Δ≈0 possible fill-forward`. WALTER's limit is written into the code comment: a near-zero change is a tell, and a non-zero change is **not** an all-clear.

**A7 — spreads carry both dates.** A `fred_spread` entry whose legs have different newest dates either aligns both legs on the common latest date or shows both dates. It is never stamped with leg A's date alone.

## Neighbour categories (WQ-229: consider all five; a justified N/A where one does not apply)

- **Ordinary:** A1–A7 above, each with a fixture test in `PROME/tools/tests/` style.
- **Overlap:** a caller that passes `limit=5000` (sofr_dispersion) under first-published. ALFRED vintage queries are heavier, so check limits and row counts. A series with **no revisions**, where the two bases agree and the test cannot tell them apart (LIQUID's own named gap): add a known-revised series (e.g. PAYEMS or GDP) as the discriminating fixture.
- **Wrong owner:** the intake lane's `~/Research-Intake/scripts/fetch_fred.py` is a separate implementation in a separate repo. It is **out of scope for code**, but its basis gets stated to its consumers. `AGENTS/VIOLET/scripts/fred_fetch.py` is VIOLET's own module with the same name; do not touch it, and name it so nobody confuses the two.
- **Missing information:** FRED's `"."` for an unpublished cell is already dropped (keep that). ALFRED returns an empty set for a date before a series existed, which becomes an explicit error, not `[]`. yfinance without `asof` shows `date?`, not live.
- **Concurrent activity:** LIQUID's `hy_oas_watch.py` timer runs on this box (`liquid-hy-watch` unit), so an edit to `fetch.py` must not break an in-flight import. Run the watcher once after the edit and read its output. No cache wipe while the timer might run; move stale cache files to trash only after the edit.

## Out of scope (named so it is not assumed done)

The continuation-ticker contract-month defect (**L429**) and the metric-name split (**L431**) are sibling rows with their own carriers. The FORGE-vs-intake `newsweep_config` divergence belongs to the CRUISE lane (L452). None of these is touched here.

## Consumers to tell at the end (A2 notice)

LIQUID (gate069 / sofr / t3 / hy_oas_watch) · TERRY (`GATE-TERRY-007` declares first-published) · LABOR · WALTER (its SIG-W-20260919-001 evidence is consumed here) · the intake-lane owner note (the basis of `fetch_fred.py`, stated, not changed).

---

## Plan read v1 — verdict NO (coldreader `l409plancold`, Opus, 2026-09-22 ~18:3x ET; 9 ✅ · 6 ⚠️ · 5 ❌). No code edited. A v2 plan is owed and gets its own read.

**❌1 "the lag DID reproduce today": REFUTED by PROME at the artifact, and the refutation is recorded, not assumed.** The reader dated the cache files wrongly. Their real write times (`ts` field):
- `fred_DGS10_20000` was written **2026-09-17 16:06** with newest row 9/15. That is correct at the time: the 9/16 H.15 cell publishes ~16:15.
- `fred_DGS10_2` was written **2026-09-21 12:18** with newest row 9/17. Also correct: Friday 9/18's cell publishes Monday 9/21 ~16:15.
- `fred_DGS10_8` was written 9/17 18:45 with newest 9/16, which is correct.

**No cache file shows a lag.** The row-1 verdict "NOT REPRODUCED" stands. The 9/17 instance is still UNEXPLAINED. ⚠️ Honest limit: this shows the files are consistent with publication timing. It does not prove the 9/17 terminal read had no lag.

**Accepted, and they shape v2:**
- ❌2 **A5 must not use the API as its own reference.** Take an independent `limit=1` probe in the same run, and have the tool refuse or mark a result that disagrees with it. `limit=20000` callers are live: BOND `boot_recompute.py:320` and `closeout_check.py:99`, and BOND co-owns GATE-TERRY-007.
- ❌3 **A first-published pull needs a bounded realtime window.** `output_type=4` with no window errors; with a full window it hits FRED's 2000-vintage cap (DGS10 has 5113 vintages). "Or an explicit error" in A1 is too weak. Each declared gate series must pull successfully under a stated window rule.
- ❌4 **A window silently drops rows.** PAYEMS returned 1 of 3 requested rows. A1 needs a row-count check, and the A3 cache key needs EVERY request parameter, not only the basis label.
- ❌5 **Caller census.** There are ~21 more callers than the 6 grepped: BOND×4, CARL×4, RED×2, TERRY `snapshot.py`, BRENT, MIDAS, LIQUID `boot.py`, WALTER's test that mocks `dashboard.fred_fetch`, the `fetch.py fred --json` readers, and `test_fetch_contract_repairs.py`. Changing the return shape therefore breaks callers, so the basis must be carried **beside** the rows, not by changing them. `hy_oas_watch.py` imports private names (`_retry_request`, `FRED_BASE`, `FRED_API_KEY`) and swallows exceptions into `VINTAGE-FETCH-FAIL` with rc 0, so the post-edit check greps for that token's absence.

**⚠️ carried into v2:**
- A7 fails live on SOFR-IORB: IORB is dated 9/23, ahead of SOFR's 9/21, and two 2-row pulls share no date. Alignment needs a deeper pull.
- A6 misses a fill-forward whose price and date come from different sources.
- A4 still shows a green "+0.00%" on a fallback row.
- A third basis, as-known-on-a-past-date, is missing.
- **The claim that GATE-TERRY-007 declares first-published is WRONG as written.** Only GATE-HY-REKILL's row says "as first published"; 007's row and TERRY's card do not. The L409 row inherited PROME's misstatement, and v2 corrects the consumer list.
- The L429 scope boundary needs one sentence.

**Reader correction, 22:37Z:** the reader WITHDREW ❌1 after PROME's rebuttal. It had printed the cache times as hours and minutes with no date, so it read 9/17 files as today's. It downgraded ❌2 to ⚠️: A5's self-referential API comparison is a design point, with no observed lag behind it, and v2 should still cover the 20000-row pulls. **Revised score: 10 ✅ · 7 ⚠️ · 3 ❌ (❌3/4/5), verdict GO-WITH-FIXES.** v2 fixes ❌3–5 and declares the ⚠️ as residue per WQ-178.

---

## PLAN v2 — `prome-68`, written 2026-09-22 20:5x ET (laptop `WilliePOwen`). Fixes ❌3 · ❌4 · ❌5; the ⚠️ are either built or declared as residue below. No code edited. This v2 gets ONE blind plan read (WQ-178).

### New evidence: live ALFRED probes, 2026-09-22 20:4x ET, direct API calls with the full JSON read whole

| # | Request | Observed |
|---|---|---|
| P1 | DGS10 `output_type=4`, `observation_start=realtime_start=2026-09-01`, `realtime_end=9999-12-31` | 15 rows, each with its own `realtime_start` = its first-publication day (9/18 obs → `realtime_start` 9/21, which is the T+1 publication, now measured instead of assumed). |
| P2 | PAYEMS, same shape, `observation_start=realtime_start=2026-05-01` | 4 of 4 rows are first-published: Jul **158,858** vs the latest-revised **158,913** (C), Jun 158,984 vs 158,892. **PAYEMS discriminates between the two bases, so it is the fixture.** |
| P3 (= the reader's "1 of 3") | PAYEMS `observation_start=2026-05-01` but `realtime_start=2026-08-01` | **2 of 4 rows, with no error.** The rule: `output_type=4` returns only observations whose FIRST release falls inside the realtime window, and it silently drops earlier ones. That drop IS ❌4's mechanism. |
| P4 | DGS10 `output_type=4` with no `observation_start`, `realtime_start=2026-09-01` | 16 rows, 8/31 onward. It does not error, and it does not return old observations at a 9/01 vintage either. It drops them. |
| P5 | DGS10 window from 2015-01-01 | **HTTP 400: "2894 vintage dates … exceeds the maximum … (2000)"**. From 2022-01-01: 1,231 rows OK. From 2024-01-01: 711 OK. |
| P6 | PAYEMS P2 shape plus `sort_order=desc&limit=2` | Works: the 2 newest first-published rows. |

### Design (v2)

**D1 — the basis lives BESIDE the rows; the return shape is unchanged (❌5).** `fred_fetch(series_id, limit=5)` stays byte-identical in signature, return value (`[{date, value}]`) and cache key `fred_{series}_{limit}`, so existing latest-revised cache files stay valid and nothing needs wiping while LIQUID's timer might be running. A **new** function `fred_fetch_vintage(series_id, limit, basis="first-published", observation_start=None)` returns `{"basis", "rows": [{date, value, first_published}], "request": {every param}, "short": bool, "missing": [dates], "error"?}`. Private names that `hy_oas_watch.py` imports (`_retry_request`, `FRED_BASE`, `FRED_API_KEY`) are **not renamed or re-signatured**. The CLI gets an opt-in `fetch.py fred <ID> --first-published`, and the default output does not change.

**D2 — window rule (❌3).** `realtime_start := observation_start` (a publication never precedes its observation date, so no first release can fall before the window: P3 and P4 are what happens otherwise). `observation_start` is the caller's, or else derived as `today − ceil(limit × period_days × 2) − 10d` from the series' FRED `frequency_short` (D=1.4 calendar days/obs, W=7, M=31, Q=92), and rows are trimmed to `limit` after a desc sort. **Cap:** if FRED returns the 2000-vintage 400 (P5), return an explicit `error` that names the cap and the window. The function never chunks or retries with a narrower window, because that would be a silent drop. Every **declared gate series** (below) gets a live test that the default window pulls successfully.

**D3 — row-count check (❌4).** In the same call, pull the latest-revised observation dates over the same `observation_start` (one cheap request, `limit` large enough for the window). Any date present latest-revised but absent first-published goes into `missing` and sets `short: true`. The result is still returned, never silently completed. Zero rows is an `error`. This check does the work; the P3 window rule only prevents the known cause.

**D4 — cache (A3 plus ❌4).** The vintage key covers EVERY request param: `fredv_{series}_{basis}_{observation_start}_{realtime_start}_{realtime_end}_{limit}`. The cached value carries `basis` and `request`, so a hit is self-describing. No latest-revised hit can be served to a vintage call or the reverse, because the prefixes differ (`fred_` vs `fredv_`). TTL is the existing ECON class.

**D5 — A4 fallback (`scripts/market.py`), including ⚠️ "green +0.00%".** When `regularMarketPrice` is absent and `previousClose` is used, the row prints `⚪ TICKER $x ⚠prev-close` with **no change % and no colour arrow**. Where yfinance supplies `regularMarketTime` and its date is not today (ET), the row gets `⚠stale <date>`.

**D6 — A6 dashboard stale marks.** yfinance entries whose `asof` ≠ today (ET) render `⚠stale <date>`, matching `fetch.py price` (:1257/:1376, re-read at edit time). Vol marks (^VIX ^VVIX ^MOVE ^SKEW ^OVX) with |Δ| < 0.005 get `⚠Δ≈0 possible fill-forward`, and WALTER's limit goes in the code comment: *a zero change is a tell; a non-zero change is not an all-clear.*

**D7 — A7 spreads, including ⚠️ SOFR-IORB.** `fred_spread` pulls `limit=10` per leg and aligns on the **latest common date**. `entry.date` = that date, and `entry.prev` = the previous common date. With no common date in 10 rows, the entry shows both legs' dates (`a <date> / b <date>`) and **no value**, never leg A's date alone. For IORB (an administered rate stamped on its effective date, and 9/23 is already in the series), the common-date rule automatically pairs SOFR with the IORB in effect on SOFR's date. That is HEARTBEAT's convention, now enforced in code.

**D8 — A5 freshness, re-stated (the ⚠️ downgraded ❌2).** A TEST-time check, not a runtime probe. In one run it compares the newest date from `fred_fetch(s, 2)` and `fred_fetch(s, 20000)` with an uncached `limit=1` request (`sort_order=desc`) built independently in the test, for DGS10 and BAMLH0A0HYM2. It asserts equality, reads the output whole, and never uses `tail`. This covers BOND's `limit=20000` path (`boot_recompute.py:320`, `closeout_check.py:99`).

### Declared gate series (the D2 live-pull test list)

`BAMLH0A0HYM2` (`GATE-HY-REKILL`: its row is the **only** one that declares "as first published"; LIQUID's `hy_oas_watch.py` builds that path itself and is **not** migrated by this repair) · `DGS10` (`GATE-TERRY-007`: ⛔ it does **not** declare first-published, so v1's consumer claim is corrected; it stays latest-revised) · `DFII10` (004 add line) · `PAYEMS` (the discriminating fixture). This PLAN changes no gate's basis. A gate adopting first-published is its OWNER's edit, made after this lands.

### Caller census (❌5), measured 2026-09-22 20:5x ET by `grep -rln` over `*.py`, excluding `.venv` and `archive`

38 files touch the name or its internals. **6 define their OWN `fred_fetch` and are out of scope** (CARL `gas_tracker`/`consumer_pulse`/`thresholds`/`housing_pulse` · BRENT `thresholds` · VIOLET `fred_fetch.py`, a same-name module). **The FORGE importers are the regression surface:** dashboard · LIQUID ×5 (`boot`, `gate069_legs`, `t3_decoupling`, `sofr_dispersion` at limit 5000, `hy_oas_watch`, which also takes the private names) · TERRY `snapshot` · BOND ×4 (`boot_recompute` / `closeout_check` at 20000, `assertion_check` / `dm_cross_section` at 400) · RED ×2 · MIDAS · LABOR · WALTER ×2 research + `test_boot_repairs` (mocks `dashboard.fred_fetch`) · CARL research ×2 · PROME `test_contract_probe_acceptance` · BOND `cdx_proxy` (CLI text). ⚠️ This census is a grep over import and name forms, so an importer using another spelling (`importlib`, `import fetch as F`) could be missing. It is **SEARCH-NOT-FOUND for others, not VERIFIED complete**. D1 makes that acceptable: nothing a caller already receives changes.

**A2 regression test:** before the edit, capture `fred_fetch` output for DGS10 at limits 2 · 400 · 5000 · 20000 plus IORB 5000, cache-bypassed. After the edit, repeat and assert byte-equality. Run `hy_oas_watch.py` once and grep its output for the ABSENCE of `VINTAGE-FETCH-FAIL`, because that script swallows errors to rc 0. Run WALTER's `test_boot_repairs.py` and PROME's tests.

### Scope boundary (the ⚠️ asked for one sentence)

**L429** (a continuation ticker such as `CL=F` naming no contract month) is a yfinance *identity* defect. L409 is a FRED/yfinance *vintage and fallback* defect. D6's stale mark can fire on a rolled continuation ticker without diagnosing the roll, so a clean D6 says nothing about L429.

### Residue declared (WQ-178), not built in this repair

- ⚠️ A6 cannot see a fill-forward where price and date come from **different** sources (a fresh date stamped over a stale price). D6 detects same-source staleness only.
- ⚠️ The third basis, **as-known-on-a-past-date** (`realtime_start=realtime_end=D`), is not built. `fred_fetch_vintage`'s `basis` parameter is the extension point. No gate needs it today.
- ⚠️ The 9/17 observed lag stays **UNEXPLAINED** (v1 row 1). D8 guards against a recurrence; it does not explain the past instance.
- ⚠️ The intake lane's `~/Research-Intake/scripts/fetch_fred.py` and VIOLET's module are not touched. Their basis gets stated to consumers in the A2 notice.

### Sequence from here

Blind plan read of THIS v2 section (coldreader, Opus) → fix ❌ only, declare ⚠️ → capture the A2 baseline → edit `fetch.py` / `dashboard.py` / `scripts/market.py` → fixtures A1–A7 plus the live-pull list → independent RESULT reader bringing its own counterexample (WQ-229 consequential) → then, and only then, "fixed" → consumer notice (LIQUID · TERRY · BOND · LABOR · WALTER · intake-lane note). ⚠️ `scripts/market.py` is root `scripts/`. Before editing it, check its owner (DAEDALUS holds the `scripts/` grant per ACTIVE_DECISIONS) — **if it is not PROME's, D5 becomes a packet, not an edit.**

---

## Plan read v2 — `l409v2plancold` (coldreader, Opus, 2026-09-22 ~20:4x ET): **14 ✅ · 10 ⚠️ · 3 ❌, GO-WITH-FIXES.** Ledger: session scratchpad `l409v2plancold_ledger.md`.

### ❌ fixes. These amend v2 in place of the text they name; per WQ-178 this is the one fix pass on the plan.

**❌7 → D2 amended: lead buffer.** PROME reproduced the counterexample at 20:4x ET. IORB `output_type=4` with `observation_start=2026-09-20`:
- `realtime_start=2026-09-20` returns 9/22 and 9/23 only.
- `realtime_start=2026-09-13` returns 9/20, 9/21, 9/22 and 9/23. The 9/20 and 9/21 rows were first published on **9/18**.

"A publication never precedes its observation date" is **false for administered and forward-stamped series**. **New rule:** `realtime_start := observation_start − lead`, where `lead = max(14 days, 2 × period_days)`. Rows are then filtered to `date ≥ observation_start`, so the buffer only admits early publications and never extra observations. The 2000-vintage cap check (P5) is applied to the buffered window. D3's `missing` list is computed over **`date ≥ observation_start` only**, which answers ⚠️9. The IORB case becomes a fixture next to PAYEMS.

**❌12 → D4 amended: failures are never cached.** `fred_fetch_vintage` calls `_cache_set` **only** when the result has no top-level `error`, `short` is false and `rows` is non-empty. That follows the 2026-09-14 rule at `fetch.py` `_cache_set`. A `short` result is returned to the caller but never cached, so a recovery is re-fetched on the next call. Fixture: an error result plus a `short` result, then assert that no `fredv_` cache file was written.

**❌21 → the census and the A2 test are amended.**
1. **CLI readers added:** `AGENTS/HENRY/scripts/update_data.py:79`, `AGENTS/LABOR/scripts/labor_data.py:70`, `AGENTS/LABOR/scripts/spine_check.py:97` (reader-found; PROME re-greps at build) and `FORGE/tools/market-data/test_fetch_contract_repairs.py` (named by v1 and dropped by v2).
2. **A2 now also asserts byte-equality of `fetch.py fred <ID> --json` default output**, before and after, for DGS10 and IORB. That covers the parser/`cmd_fred` edit.
3. **A real cache bypass:** the A2 baseline and after-run point `CACHE_DIR` at two **separate fresh temp directories** through an env override (`FORGE_CACHE_DIR`, added in this repair, defaulting to the current path). Neither run can be served by the other's cache, which answers ⚠️24. The same override serves D8, which answers ⚠️18.

The "38 files" count is withdrawn (⚠️20). The build re-runs the census with the command recorded, and the notice lists what that command returns.

**`scripts/market.py` owner, answered:** DAEDALUS (`ACTIVE_DECISIONS.md` FORGE row, transferred 7/31 with the `scripts/` grant; reader cited git `4e27100f2`, `10ce7b2dc`). **D5 therefore becomes a packet to DAEDALUS, not a PROME edit.** A4 is verified at DAEDALUS's artifact once it lands.

### Declared residue (WQ-178). Not fixed in the plan text; each is carried into the build as a constraint or left explicitly open.

- ⚠️6 CLI default-output equality → **absorbed by the ❌21 fix** (point 2).
- ⚠️11 `_cache_ttl` keys on `"fred_" in key`, so `fredv_` keys fall to the STANDARD TTL (120 s), not ECON. The plan's "ECON" claim is wrong. **Build constraint:** extend the `_cache_ttl` match to `fredv_`, with a fixture.
- ⚠️13 **`api_key` must never enter `request`.** The build strips it from the echoed params before caching or returning. Fixture: grep the cached JSON and the returned dict for the key and assert it is absent.
- ⚠️17 A D7 spread's `prev`/Δ can span a `"."` gap (DCPF3M: 9/21 → 9/11, six sessions). **Build constraint:** when prev-common is more than one publication period back, mark the Δ `Δ over <n> sessions`; never show it as a daily change.
- ⚠️19 "004 add line" means ACTIVE_DECISIONS TERRY row: DFII10 ≥2.50, `BND-29`. Defined here, not re-worded above.
- ⚠️23 D5/D6/D7 **do** change what some surfaces show (`scripts/market.py` users WAL · OZK · REGINALD · POSITIONS; the dashboard tiles). D1's "nothing changes" holds for `fred_fetch` only. **The consumer notice adds WAL, OZK and REGINALD.**
- The remaining v1 residue (A6 cross-source fill-forward · third basis · the unexplained 9/17 lag · intake lane/VIOLET untouched) stands as declared in v2.

**The plan is now closed to further reads this session (WQ-178).** The next read is the independent RESULT reader after code, who must bring its own counterexample (WQ-229).
