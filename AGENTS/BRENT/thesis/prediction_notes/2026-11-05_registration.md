# BRT-32 to BRT-35 — registration note, 2026-11-05 18:35 EST

Registered under `PROME/reports/2026-11-05_prediction-registration-brief.md` (WQ-596, L930), by BRENT session launched by prome-96 under WQ-623. New rows only. No existing row, gate, band, level, card or thesis score changed. No backfill. The cells in `thesis/PREDICTIONS.tsv` govern; this note holds the pre-flight only.

| ID | Call | Price | Settles at | Resolves by |
|---|---|---|---|---|
| BRT-32 | Yanbu crude loadings stop at least 24 hours on hostile action or threat | 20% | Aramco, ministry or SPA statement; Reuters or Bloomberg | 2026-12-31, reports to 2027-01-08 |
| BRT-33 | M1−M3 BZF27−BZH27 window proxy strictly under +$3.50 | 20% | Vendor one-minute bars, proxy | 2026-11-27 |
| BRT-34 | EIA distillate stocks strictly under 95,000 kb | 45% | EIA WPSR | Data week 12/18, release about 12/23 |
| BRT-35 | GASREGW strictly under $4.000 | 70% | EIA weekly retail or FRED | Print dated 12/21 |

**Pre-flight, PREDICTIONS.tsv header:**

| ID | Can it fail to fire | True for wrong reasons | False while the thesis holds | Mechanism |
|---|---|---|---|---|
| BRT-32 | No: dated window, default NO | A precautionary 24-hour stop with no damage counts; the letter means that, because a stop is what removes barrels | Risk is real and no halt comes | Via hostile action or threat at the terminal, not via pipeline repair alone |
| BRT-33 | M3 can miss the window, as on 11/5: 8 valid sessions required, else NO-VERDICT | A thin M3 print. Both legs must print; the proxy label travels | A deal scare narrows paper while barrels stay short: that is exactly what it would show, so it is not a Phase 2 call | Via paper repricing, not throughput |
| BRT-34 | No: weekly print | Export surge or a refinery outage, each named beside a YES | Stocks build on high runs while global diesel stays tight | Via exports and runs, not demand |
| BRT-35 | No: weekly print | Crude falls on a deal headline: price is what is asked | Retail falls on deal hopes while the physical market stays tight | Via wholesale gasoline passed to retail, not demand weakness |

**Lessons (`lessons_check.py --concept threshold`):** L22 honoured, every row names a number and an instrument that prints; BZH27's missing bars are carried as a stated failure mode, not assumed away. L23 honoured, named contracts only. L21: BRT-33 sets its own window on a thin leg; no joint leg. L05 honoured: BRT-33 reads only the settlement window, never a daily bar. L06: crack context is carried in the BRT-34 price, not graded. L08: BRT-34 grades the data week, with publication about 5 days later. L09 does not apply: no row reads product supplied. L25: BRT-32 treats a failed fetch of a wire as no evidence, not as no halt; its default NO is on the absence of a report at the window end.

**On a miss:** add one line to the row, what surprised me and what changes in the next comparable forecast (WQ-619 A).

**Addendum 2026-11-06 11:4x EST, BRT-34, mechanism only:** the pre-flight line "via exports and runs, not demand" does not fit week 10/30. Against a year ago, production +445 kb/d, exports +146, product supplied +729; four-week product supplied +8.7%, exports +118 kb/d. The draw ran mainly through product supplied, a residual that absorbs export error, one week. Claim, price 45%, window and row unchanged; registered text stands as written, so the miss in reasoning stays visible. A YES on this print path should name that leg beside it. Arithmetic: `research/2026-11-06_wake/NOTE.md`, `dist.py`.

**Addendum 2 2026-11-06 11:56 EST, BRT-34 mechanism resolved, supersedes the reading above:** over 39 weeks against the 5-yr average, exports took −79.1M barrels and production gave +77.8M; product supplied −3.5M. Exports: right, the largest change. Runs: wrong, they are the offset, not a cause. Not demand: right over 39 weeks, wrong over the last 4 (−6.0M). The 8-week draw, −7.0M, matches the 5-yr −7.4M. Weekly exports tracked monthly within 12 kb/d on average, January–August 2026, so "absorbs export error" above was too strong. Claim, price 45%, window and row unchanged. On a miss or hit, name the legs. `research/2026-11-06_diesel/NOTE.md` § 2.
