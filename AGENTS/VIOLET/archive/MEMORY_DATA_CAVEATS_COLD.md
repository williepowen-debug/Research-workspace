# VIOLET MEMORY — DATA-CAVEAT CORRECTION NARRATIVES (COLD)

> **Split out of `MEMORY.md` on 2026-09-17** under the DAEDALUS READ-CAP contract (`scripts/read_cap_check.py --agent VIOLET` read 🟡 78% of the 32,550 B budget, rotate-tier; rule 5 requires finishing under 70%).
>
> **This file is NOT a boot read.** Read it on demand when you need the history of *why* a data caveat says what it says.
>
> **Nothing was deleted or reworded.** Each section below is the verbatim prior text of a `MEMORY.md` bullet. Every **operative rule** in those bullets stayed HOT in `MEMORY.md` — what moved here is the *correction narrative*: how the defect was found, what the entry used to claim, and why the wrong version was wrong. Those stories are load-bearing for calibration, not for a boot.

---

## ^VIX holiday phantom-prints — the misattribution and its correction

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

- **^VIX phantom-prints on US market holidays — ⚠️ AND THE SOURCE IS CBOE, NOT YFINANCE (CORRECTED 2026-09-06, KB-VIO-247).** This entry read *"yfinance ^VIX phantom-prints"* and blamed the wrong party. **CBOE's own `VIX_History.csv` publishes a VIX close on days the US equity market was closed** — 13 such dates over 2025-01-01→2026-09-04, every one a market holiday (MLK, Presidents', Memorial, Juneteenth, July 4, Labor Day, Thanksgiving, + 2025-01-09 Carter day of mourning). **yfinance inherits it; every ^VIX consumer inherits it. Switching to the publisher of record does NOT escape this defect** — which is why the attribution mattered. **Discriminator, exact at the source: 13/13 caught, 0 false positives** — on a phantom date VIX is published and `^VIX3M`/`^VIX6M`/`^VVIX`/`^SKEW`/`^VIX9D` are **all** absent. **Orphan ^VIX = phantom; a real session publishes companions.** Enforced in `backfill.py` (drops rows lacking every companion) and in `scripts/vx_daily_gapcheck.py`, which uses it to avoid demanding 13 holiday rows that should not exist.

---

## CBOE ^SKEW availability — the two wrong versions (T+1 lag; ~17:00 ET)

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

- **CBOE ^SKEW: SAME-DAY AVAILABILITY HAS BEEN OBSERVED; THE PUBLICATION SCHEDULE IS UNVERIFIED.** ⚠️ **SCOPE-CORRECTED 2026-09-06 (KB-VIO-269).** This entry read *"publishes SAME-DAY at ~17:00 ET — ~45 min after the 16:15 VIX settle"* and **that hour is not supported by the evidence behind it**: KB-VIO-137's `~17:00` is a `last_trade_time` field on CBOE's **delayed-quote endpoint** (`_SKEW.json`), pulled the **following morning** — a property of a *different artifact* than the grading source `SKEW_History.csv`, and a next-day pull cannot bound when anything became available. **What IS evidenced (n=1, 2026-07-27): the value existed by 18:30 ET the same evening**, proven by this desk's own `VX_DAILY` `source_ts`. ⇒ **Grade when the required dated CBOE bar becomes available; never schedule off an assumed hour.** 🔑 **This surface is boot-read every session, and on 2026-09-06 it taught me the unsupported hour, which I then wrote onto a live gate row as a "correction."** ⚠️ **CORRECTED 2026-07-28 (KB-VIO-137): the previous entry here claimed a "T+1 lag" and that was WRONG**, in the direction that cost two sessions of an ungradeable stand-down. A boot run before ~17:00 sees the *prior* day's stamp and looks exactly like a publication lag. **Verify with CBOE's `last_trade_time`, not by the value's apparent staleness** (`cdn.cboe.com/api/global/delayed_quotes/quotes/_SKEW.json` → `last_trade_time`; the 7/27 close 146.60 is stamped `2026-07-27T17:00:19`). **Inspect the actual dated quote/archive on every pull. Neither the clock nor a successful prior-day pull proves that today’s close is published.**

---

## CBOE VX settlement — the one-axis version that nearly bought a subscription

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

- **⚠️ CBOE VX SETTLEMENT — TWO ENDPOINTS ON TWO AXES; I recorded only one and drew a false conclusion (KB-VIO-158).** ① `/us/futures/market_statistics/settlement/csv/?dt=` is keyed by **TRADE DATE**, one request per date, and really is a **~12-month rolling window** — good for today, useless for history. ② `cdn.cboe.com/data/us/futures/market_statistics/historical_data/VX/VX_{EXPIRY}.csv` is keyed by **CONTRACT EXPIRY**, one file per expired contract carrying its **entire life** with a real `Settle` column, **FREE, 2013 → current.** **A multi-year VX study is neither an effort problem NOR a paid one** — `scripts/vx_history.py` builds 28,555 contract-days in ~1 minute → `workbook/VX_TERM_HISTORY.tsv`. 🔑 **This entry previously said the opposite and nearly bought a data subscription. The generalizable lesson: when a source looks limited, ask what OTHER AXIS it might publish on before concluding it cannot be done.**

---

## ^MOVE / fetch.py — the caveat that stayed OPEN after PROME fixed it

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

- **`^MOVE` is unreliable via yfinance as a SOLE source** — it returns a lone stale bar days old. *(Re-confirmed 7/30 PM: `period=10d` returned exactly one bar, **7/17**, and no 5m bars at all.)* **Primary = investing.com; `FORGE/tools/market-data/fetch.py price MOVE` also resolves correctly since PROME's 7/30 alias fix** (verified 74.18 to the cent). ✅ **CORRECTED 2026-07-30 PM — this entry previously said "`fetch.py` prints no data-date."** That was true when written and **PROME then fixed it the same day** (`4eb65340`, crediting this defect report): the `price` output now carries an **As-of column that flags a non-today bar `⚠stale`** and, when the date is unverifiable, **keeps the value and labels it `date?` rather than suppressing it** (fail-safe: label, never hide). Verified live — `MOVE`/`SKEW` flag `2026-07-29 ⚠stale`, `VIX` reads `2026-07-30` clean. ⚠️ **The recurrence worth noting is mine, not the tool's:** this is the second time (after KB-VIO-151) that a VIOLET surface advertised a defect as OPEN for days *after another agent had fixed it* — **a stale caveat wastes exactly as much of the next session as a stale "unbuilt" does, and no freshness check can see either.**

---

---

## Crisis-analog table — the zero-inbound-reference near-miss that created the citation rule

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

⚠️ **Source-citation discipline (added 2026-08-04, staleness sweep).** Each row now names its underlying corpus under `research/`. **Reason: a reference-count sweep found all seven crisis-analog source files at ZERO inbound references** — they were retirement candidates under the >60d rule purely because **this table used them without citing them.** The framework was live and its evidence base looked dead. **A live doc that cites nothing makes its own sources look retirable** — cite the corpus, or a future sweep deletes the ground under the framework.

---

## CFTC TFF release schedule — the invariant that was wrong three times

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

**CFTC TFF release schedule** — ⛔ **DO NOT ENCODE A CALENDAR RULE FROM THIS LINE. Its earlier version taught "Tue close → Fri 3:30 PM ET release" as a dependable invariant and I built a guard on it THREE TIMES, wrong each time (KB-VIO-243, retracted 2026-09-04 17:28).** What is true: report dates are **usually** Tuesdays and releases **usually** Friday 15:30 ET — **usually is not a schedule.** Federal holidays can delay a release, and the report date is **not** shifted Tue→Wed by a Monday holiday (my own `COT_VIX.tsv` has `2026-05-26`, a Tuesday straight after Memorial Day; the only non-Tuesdays in the ledger are two **Mondays**). **The staleness rule now uses observed cadence + a grace window and synthesizes no calendar at all.**

---

## yfinance lastPrice — full 2026-07-30 root-cause note

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

**⚠️ `yfinance` `fast_info['lastPrice']` SERVES A PRIOR-SESSION CLOSE WITH NO STALENESS SIGNAL** (root cause of KB-VIO-139/149, found 2026-07-30). It returns the last price that *exists*, never saying when it was struck. **`^VIX` quotes during CBOE global trading hours; `^VIX3M` / `^VIX6M` / `^VVIX` / `^SKEW` do NOT publish pre-open** — so any pre-open row silently fill-forwards those four, and a derived `VIX3M/VIX` becomes a **cross-date artifact**. The direction is the dangerous one: a fill-forward prior is too HIGH, so every 1-day change against it is **overstated — it manufactures peak-markers.** Guarded in `thresholds.py` since 7/30 (preventive + detective). **Use the publisher’s own timestamp and value together. An intraday-bar witness cannot certify an EOD-only series such as SKEW (KB-VIO-283); never trust `lastPrice` alone.**

---

## SESSION NOTES pointer — full 2026-09-02 split rationale

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

> **Moved 2026-09-02 to `archive/MEMORY_SESSION_NOTES_COLD.md`** (verbatim, 21,363 B) under the DAEDALUS P1 READ-CAP ruling — this file is a boot-step-3 whole-read and was 42,166 B = 78% of cap. **Read that file only when you need trajectory context**; it is not a boot read. Nothing was deleted or reworded.
>
> Arc covered there: 2026-04-16 → 2026-07-30 (Phase-2 cluster analog · the NFP shock arc · the gate working twice · first Bin-A · the VIXCS arc). Durable lessons that were load-bearing already live above in CORE PRINCIPLES / SKEW PATTERNS / METRIC SEMANTICS / DATA SOURCES.

---

## Aug-2026 unmatched SKEW configuration — fuller wording

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

⚠️ **Gap noted, not closed (2026-08-04): the 4 Aug 2026 SKEW configuration has no analog here.** SKEW at a 3-year low (126.41, 0.3rd pct) with VIX 16.50 and the index at a record close — crash protection dumped INTO a melt-up, the inverse of the coiled spring, and *not* the catalogued "SKEW crash during a vol spike" (there was no spike). **Recorded as an unmatched configuration rather than forced into the nearest row.** → KB-VIO-186.

---

## CBOE daily-prices caveat — fuller wording

**Verbatim, as it stood in `MEMORY.md` until the 2026-09-17 hot/cold split:**

- **CBOE daily-prices CSVs are the PUBLISHER OF RECORD for all six spot columns and are free, complete and key-less** (`cdn.cboe.com/api/global/us_indices/daily_prices/{VIX,VIX9D,VIX3M,VIX6M,VVIX,SKEW}_History.csv`; 3,941–9,266 rows each). **Use them, not yfinance, for anything graded** — yfinance has two `^SKEW` defect modes (omission + wrong value, RED 2/253) and serves **no** daily history at all for `^VIX9D`/`^VIX3M`/`^VIX6M`, which is why 226 of 416 term-structure cells sat blank until 2026-09-06. `backfill.py`'s CBOE pass runs second and **wins** — it fills blanks *and* corrects disagreements, printing every correction. Layout differs: OHLC indices expose `CLOSE`, VVIX/SKEW expose a column named for the index. → KB-VIO-246/247/248

---

## Dropped rows (not narrative — recorded so the split is fully reversible)

- From the DATA SOURCES table, 2026-09-17: `| CBOE LiveVol | Options data | livevol.com |` — removed to finish the byte target. Never used by any VIOLET script; `vix_options.py` reads CBOE's delayed-quote API, not LiveVol.
- Compressed-in-place (wording only, no fact lost): the SKEW >150 / <120 / crash-during-spike bullets in SKEW PATTERNS, and the dated example "Our Apr 13 SKEW peak: 156.9 (high cohort)".
