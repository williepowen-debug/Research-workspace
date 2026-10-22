# HENRY desk sweep — 2026-10-21 ~21:30 ET

Will-requested sweep of `AGENTS/HENRY/` for anything owed, incomplete, broken or stale. Read-only except this file. Method and controls are at the bottom.

## A. OWED — dated

| # | Item | Due | Where |
|---|---|---|---|
| A1 | **HEN-46 resolves at American Q3** — apply the pre-stated disposition (AAL adj EPS < −$0.70 → CONFIRM; else NO-VERDICT-AS-WRITTEN) | Thu 10/22 pre-open (call 08:30 ET) | DOCKET L769 · `workbook/PREDICTIONS.tsv` HEN-46 |
| A2 | **F1 December crack near-line UNKNOWN ($95.05)** — close from the finalized 10/21 settlement row (volumes must differ from 10/20) or BRENT's published figure | 10/22 session | STATUS § HEN-46 |
| A3 | **Credit re-pull** — HY since 10/19, BB/CCC since 10/16 (FRED in maintenance 10/21) | first boot after FRED returns | STATUS § CREDIT |
| A4 | **Market-breadth research** (Will-requested 10/7, HENRY proposed lead) — PENDING, no date; PROME schedules | undated | DOCKET L616 |
| A5 | ECON_CALENDAR rebuild | by 2026-11-20 | `domain/ECON_CALENDAR.md` |
| A6 | Wake rows already registered by PROME: FOMC 10/28 (L773), GDP+PCE 10/29 (L774), CPI 11/10 (L775), PPI 11/13 (L776). NFP 11/6 is LABOR's L767. | — | no action |

## B. BROKEN

| # | Item | Since | Note |
|---|---|---|---|
| B1 | **Gamma cross-horizon wall guard (audit E2) not built.** `gamma_flip.py` checks near-ties within one horizon only; the 14d-vs-35d rule is manual. `boot.py` still prints "still unfixed". | 7/29 (84 days) | Applied by hand tonight. |
| B2 | **PUBLISHED.tsv duplicate key** `gamma_flip_35d_STALE @ 2026-09-04` — boot warns on every run. | 9/04 | needs a timestamped asof on the later row |
| B3 | **`scripts/status_figure_manifest.py` is a dead one-off** — hardcoded 8/28 figures (VIX 14.21, flip 7,718, CCC 1,031); no live caller. | 8/28 | retire |
| B4 | **`scripts/update_data.py` is unlisted in the charter** and predates MARKET_DATA's per-cell capture-basis guard; running it could append rows without basis notes. | 8/28 | check before use, or retire |
| B5 | `credit_monitor.py` reads FRED's maintenance page as "no data" rather than "source down". Fails closed since tonight's fix. | — | cosmetic |

## C. STALE

| # | Item | Age | Note |
|---|---|---|---|
| C1 | **Operating Dashboard artifact** (Will-facing, "living") last updated **2026-07-24**. Its own rule: refresh after a prediction resolves or a threshold changes state. Listing URL `claude.ai/artifact/W7ALXXxkW4mGJHLHjrbeyr`; the memory file stores `claude.ai/code/artifact/ebb53cd8-…` — confirm they are the same page before redeploying. | 89 days | refresh same URL |
| C2 | **Evals last run 2026-07-10.** `boot.py`/`credit_monitor.py` changed since (incl. tonight). | 103 days | re-run the 3-case suite |
| C3 | **Charter (`CLAUDE.md`) stale claims:** (a) ECON_CALENDAR row says "DOCKET EXPIRED … Mar-Jul only" — rebuilt tonight; (b) KB "132 rows, last ID ML-HEN-160" → now **158 rows, ML-HEN-186**; (c) line ~256 says "REGINALD 14-col schema", contradicting the 15-column correction at line ~241; (d) LESSONS "All 37 rule headings" → **44** by heading count, and "25 SETTLED" vs **35** settled bullets now. | various | own-file edit |
| C4 | **Outbox: 8 PROME-action packets (7/16 → 9/2) never moved to `outbox/delivered/`.** 7 of 8 have no filename citation anywhere in `PROME/`; content may still have been consumed by topic (the 7/31 boot-doc audit's rulings are in the charter). **Consumption UNVERIFIED, not "unread".** | 50–97 days | verify, then file |
| C5 | **Carry-ins aging:** Asia exchange-halt verification and tanker-cyberattack attribution (since 10/15); real-yield letter unregistered; ISM late-evaluator ambiguity; KRE Muse / TLT-flow sources; DGS30 history scope; direct Treasury availability; ISM release dates unverified (503). | 6+ days | — |
| C6 | **Retirement-eligible (>60 days, not boot-read, no live-doc reference) — 16 items:** `sources/` ×3 Burry files (2/13) · `research/deep_dives` (4/17) · `research/NVDA_5_20_READ_THROUGH_2026-05-21.md` · `proposals/2026-06-06_automem_proposal_folder.md` · `proposals/2026-06-15_boot_closeout_hardening.md` · `BOOT_AUDIT.md` · `MODERNIZATION_PLAN.md` · `research/2026-06-23_cta_gamma_levels_sourcing.md` · `research/2026-06-23_gap_catchup_workflow.json` · `research/2026-06-23_staleness_audit_workflow.json` · `reports/2026-07-11_full-boot-sweep.md` · `reports/2026-07-11_threads-sweep.md` · `research/2026-07-11_cpi-disregard-steelman.md` · `reports/2026-08-06_rulings-implementation-and-falsification-disposition.md`. Target `AGENTS/HENRY/archive/` does not exist (deleted by the 6/30 prune `1cb18fbc3`) and must be recreated. | — | `git mv` at a closeout |
| C7 | `proposals/2026-08-28_DRAFT_rung4-relabel-nonkill-observable.md` — a DRAFT with no live reference; decide submit or withdraw. | 54 days | — |

## D. FORMAT (Output Canon: no glued words)

| # | Item |
|---|---|
| D1 | Glued text remains in **KB ML-HEN-182–186** (ML-HEN-146/159/176 may be false positives from FRED series IDs), **4 board_log rows dated 10/19**, the 10/19 HEN-46 note in `PREDICTIONS.tsv` (below the detector threshold, found by eye), and the `research/2026-10-19_*` files. Records, not boot surfaces. Counts are a FLOOR. |
| D2 | PREDICTIONS carries 22 distinct status tokens, not STATE_VOCABULARY canon. Legacy, grandfathered; the boot due-scan only needs OPEN/ACTIVE. Low. |

## E. VERIFIED CLEAN

Working tree clean; inbox and WALTER lane empty · PREDICTIONS 51 rows, all 7 columns, one live row (HEN-46) · KB 158 rows × 15 columns, no duplicate IDs · all TSVs LF · boot self-test PASS · corrections check rc 0 · weekday claim check clean · read-cap rc 0 (STATUS 13.3 KB, 41%) · STATUS 110/250 lines, MEMORY 68/100 · every charter file pointer resolves (bare names under `scripts/`/`workbook/`; `walter_route_check.py` lives in DAEDALUS; TRADE.md, BEIGE_BOOK, ML_deprecated, power_watch are documented retirements) · live boot surfaces have no glued text · no tracked `__pycache__`.

## Method and controls

- Glued-text detector tested against a known positive (pre-rewrite NEXUS_BRIEF: 18 hits) before reading any zero. The first detector version excluded tokens containing "/" and would have missed the 10/19 style; it was discarded.
- Outbox citation scan: the one packet PROME did cite (`2026-07-27_to-PROME_gamma-refresh`, 3 refs) proves the scan runs.
- Retirement scan: an old file that IS cited (the VECTOR-4 screen, via HEN-46) was correctly excluded.
- DOCKET rows naming HENRY read at their state cells (L477, 478, 487, 489, 490, 531, 543, 565, 612, 616, 700, 769, 773–776); only L616 is open on HENRY.

## Fixes applied 2026-10-21 (Will: "yes go ahead and fix those")

| Item | Status |
|---|---|
| C1 Operating Dashboard | **FIXED** — republished at the same URL (version 2); both URL forms confirmed to be artifact ebb53cd8. Source now in `dashboard/`. |
| C2 Evals | **FIXED** — 3/3 PASS. Case 01 needs date-neutralizing (new item). |
| C3 Charter stale claims | **FIXED** — all four; the LESSONS figures were worse than reported (the archive holds 35 sections, not 25). |
| B2 PUBLISHED duplicate key | **FIXED** — warning count 0. |
| New: STATUS headers | **FIXED** — charter § pointers (VOL REGIME, CREDIT EARLY-WARNING MONITOR, INVALIDATION TRIAD, CATALYST STACK) resolve again. |
| Everything else in A–D | Open as listed. |

## Second fix pass 2026-10-21 ~22:00 ET (Will: "fix the rest of the sweep items too")

| Item | Status |
|---|---|
| A1 HEN-46 at American Q3 | **Cannot be done tonight** — waits for the 10/22 pre-open print; disposition is pre-stated in PREDICTIONS |
| A2 F1 near-line 10/21 | **Advanced, still waits** — BRENT published and concurs UNKNOWN at $95.0479; needs a settlement-grade print |
| A3 Credit re-pull | **Cannot be done tonight** — FRED still in maintenance at 21:5x ET (now reported as "source DOWN", item B5) |
| A4 Breadth research (L616) | **PROME's to schedule** — undated backlog row; no HENRY action without a date |
| A5 Calendar rebuild by 11/20 | Dated; nothing to do yet |
| B1 Cross-horizon wall guard | **FIXED** — `gamma_flip.py --both`; live run and 7/29 replay tested; charter updated in three places |
| B3/B4 Dead scripts | **FIXED** — `status_figure_manifest.py` and `update_data.py` moved to `archive/scripts/` |
| B5 FRED outage message | **FIXED** — reports "FRED source DOWN — served an HTML page, not CSV (site maintenance)" |
| C4 Outbox | **FIXED** — 8 packets filed to `outbox/delivered/` with `FILING_2026-10-21.md`; 7 consumed by topic evidence, 1 (7/31 closeout-doc audit) UNVERIFIED and stated as such |
| C5 Carry-ins | **FIXED** — Treasury direct works (official par yields now in STATUS and the dashboard); Asia 10/15 halt corroborated; tanker cyberattack closed as unverifiable; Muse → REGINALD; ISM evaluator → PROME; TLT flow deferred to positioning work; DGS30 is a standing rule; real-yield letter closed. ISM services date still unverified (site 503) |
| C6/C7 Retirement + rung-4 draft | **FIXED** — 20 files `git mv`-ed into a recreated `archive/` with `archive/README.md`; the rung-4 draft is superseded (WQ-106 ruled 9/1); no live doc points at any moved path |
| D1 Glued text | **FIXED in live ledgers** — KB ML-HEN-178–186, 4 board_log rows, the HEN-46 10/19 note. **Not done, deliberately:** `research/2026-10-19_*` files, because LIQUID and CRUISE recorded consumption receipts against their exact file hashes; rewriting them would break those receipts |
| D2 Status vocabulary | **No change, by rule** — legacy tokens are grandfathered (root Output Canon); new rows use canonical tokens |
| New: eval case 01 aging | **FIXED** — scenario date pinned to 2026-06-15 (v1.1); rubric notes the change |
