# HAWK — Cluster C: Ledgers, Scripts & Guards (Mode-A comprehension read)

Reader: read-only DAEDALUS sub-reader · window 2026-10-22 17:42:51 → 17:47:35 EDT (from `date`) · repo HEAD at start `0ffc5373a`.
Scope: `AGENTS/HAWK/workbook/` (12 files), `registry/` (2), `scripts/` (7 .py + PLAN.md + `__pycache__`/2 .pyc), `audits/` (26, newest 3 read whole + derived-acceptance.json), `board_log.tsv`, plus `thesis/PREDICTIONS.tsv` (the prediction ledger lives in `thesis/`, not `workbook/`).

---

## 1. Ledger table

| Path | Purpose | Rows | Schema valid? | Two-clock header | ledger_staleness state | Open / past-due rows |
|---|---|---|---|---|---|---|
| `workbook/KB.tsv` (437,561 B, 456 lines) | Fact ledger; ≤223 frozen pre-split, 224+ synthesis/dormant | 454 data (KB-HAWK-001..452 + dup 131/132) | 🟠 PARTIAL. 444/454 rows have 13 cols; 7 rows 12 cols (KB-040/041/042/050/051/085/088) and 3 rows 14 cols (KB-091/092/093), all pre-split. Off-vocabulary: Epistemic `ANALYTICAL` ×6, `DERIVED` ×2; Status `WATCH` ×1 (KB-149); 2 non-ISO Stale_By. All defects are in the frozen ≤223 band; all post-split rows are clean on these tests. | none (SPLIT-NOTE comment only) | `ok +0d` (git-time vs STATUS) | **113 post-split ACTIVE rows have Stale_By < 2026-10-22** (213 post-split rows set Stale_By). Examples: KB-224..227 (9/08), KB-231/232 (8/04), KB-254..281 cluster (9/30). Plus 113 in the pre-split band. No tool or step reads Stale_By. CLAUDE §KB "Currency pass" (L169) says filter them out at read time; nothing ever re-dates or re-statuses them. |
| `workbook/VX.tsv` (86,640 B) | Dormant book of vectors | 11 (10 live + CEASEFIRE-01 SUPERSEDED) | 🟠 13/13 cols on every row; Guard vocabulary is CLOCK/EVENT/CLOCK+EVENT, but **TRADE-01's Guard cell = `CLOCK+EVENT \| ADOPTION-STAGE (WQ-211 ② …) …`** (prose added after the token, so a strict reader will not see a valid token) | none (GRADING-DECLARATION + SPLIT-NOTE comments) | `ok +0d` | Last_Updated ages: VEN/TWN/TWNMIL/TRADE-02/CODIF 1d (10/21 re-sweep); IRAQ/SULPHUR/FININFRA 24d; EURMIL 34d; **TRADE-01 42d, hits the 45-day backstop on 2026-10-25**; CEASEFIRE-01 124d (SUPERSEDED, excluded). |
| `workbook/FLOW.tsv` (36,487 B) | Transmission pathways; FLOW-HAWK-19 is the canonical thesis | 8 (10,13,15,16,18,19,20,21) | ✅ 9/9 cols on every row | none (SPLIT-NOTE) | `ok +23d` | FLOW-10 MUTED dormant-armed (Notes cite "[STALE Apr20 figs]"); 13/15 RETIRED; 18 RETIRED-BY-ROUTING; 19/20/21 LIVE/ACTIVE. Last commit 9/28. |
| `workbook/CATALYSTS.tsv` (18,966 B) | Dated observation obligations (created 9/08) | 37 | ✅ 5/5 cols; one non-ISO Date (`2027-Q1`) | none | `ok +11d` (last commit 10/10 `62240556c`) | 🔴 **21 rows still PENDING with a date before 10/22.** At least 3 were done on 10/21 but the ledger was never updated: 9/09 Sept-STEO N6 and 10/07 Oct-STEO N6 (both run per KB-HAWK-448), and 9/24 dormant review (KB-451 re-sweep). Others include 10/18 Article-4 NATO primary, 10/18 H.R.5334, 10/12 EU 22nd package, 10/17 FE1 Suez sailing. The **10/03 "EURMIL first 45-day checkpoint" is wrong on its own terms: 9/18 + 45d = 11/02.** No row exists for HAW-22's 12/15–12/21 final search or its 12/22 resolution. |
| `workbook/PRICE_BREACHES.tsv` | Legacy Brent log (BRENT owns oil price) | 1 (2026-04-20, $94.28) | ✅ | FROZEN banner 2026-07-09 | `FROZEN +72d` | n/a. Still read by frozen `thresholds.py --quick` as a "cached price" (see S-table). |
| `workbook/SCHEMA.tsv` | KB data dictionary + VX.Guard / VX.Watch_Source | 15 vars | ✅ | n/a | (not listed) | Boot-read whole (2,113 B). |
| `thesis/PREDICTIONS.tsv` (96,616 B, 44 lines) | Calibration record | 22 (HAW-01..22) | ✅ All 22 rows have 10 cols. Preamble L20's "HAW-10 9 cols / HAW-11 11 cols" DATA NOTE is **stale** (both are 10 now). There is **no Resolve_By and no anchor_type column.** Both sit as prose in Notes. | none | **NOT SCANNED** (tool's perimeter line names it) | Tally verified by count: 6 CONFIRMED / 9 FAILED / 1 PARTIALLY / 1 VOIDED / 2 REHOMED / 1 DEFECTIVE-INSTRUMENT / 2 OPEN. This matches preamble L5 (9/28). **OPEN:** HAW-20 (65%, Resolve_By **2026-10-31**, ANCHOR TYPE: **IMMOVABLE**); HAW-22 (65% UNCALIBRATED, Resolve_By **2026-12-22**, **IMMOVABLE**, event window 10/01–10/31, observation cutoff 12/21). **No OPEN row is past due** as of 10/22. No EXPECTED_EVENT anchors among the OPEN rows. |
| `workbook/BOOT_LOG.md` | One 4/20 legacy boot run | 1 entry | n/a | 🧊 FROZEN 2026-08-10 banner | not a TSV | n/a |
| `workbook/EXIT_PROTOCOL.md` | Pre-split exit ladder | n/a | n/a | 🧊 FROZEN 2026-08-10, labelled "most dangerous dead surface" | — | n/a |
| `workbook/POLITICAL_SUSTAINABILITY_MODEL.md` | Kent-resignation model | n/a | n/a | 🧊 FROZEN 2026-08-10 | — | n/a |
| `workbook/FOUR_STRUCTURAL_BREAKS_MAR18.md` | 3/18 snapshot | n/a | n/a | **No banner.** Only "Created Mar 20" in the title. The only `FROZEN` token is body prose ("Rate path is FROZEN", L75). FILES.md L40 calls it frozen-historical. | — | n/a |
| `workbook/STATUS_archive_20260326.md`, `_20260522.md` | Archived STATUS snapshots | n/a | n/a | Dated filenames; FILES.md L42 classifies them | — | n/a |
| `registry/corrections_receipts.tsv` | R1 receipts | 16 | ✅ 4 cols; WQ-399 key=value tokens on 2026-10-10+ rows | — | NOT SCANNED (coverage note) | 0 unreceipted NAMED rows (corrections check rc 0) |
| `registry/derived_inputs.json` | derived_freshness receipt | 2 products / 11 edges | ✅ v1 | recorded_at 2026-10-22T01:39:02Z | — | **Drifted:** FALCON NEXUS_BRIEF re-committed 2026-10-22 13:37 −0400 (after the record), so derived_freshness exits rc 1 (see S-table) |
| `board_log.tsv` (174,493 B) | WALTER/BOARD disposition log | 491 data + 1 split-marker comment (L67) | ✅ 5/5 cols on all rows; timestamp format is mixed (`Z`, `-04:00`, microseconds) | — | excluded by design (`NON_LEDGER_NAMES`) | Dispositions: acted 200 / noted 178 / info-only 105 / deferred 7 / skipped 1. Five of the 7 deferred have a later `acted` row under the same key. **Two (9/02 `DAEDALUS-20260815-…`, `PROME-20260817-…`) used truncated keys and were closed 9/08 under their full filenames**, so a by-ID join reads them as open forever. Newest row 2026-10-22T01:38:19Z. |

Not scanned by `ledger_staleness` (its own perimeter line): `domain/energy-strikes/STRIKES.tsv`, `domain/europe-rearm/INCURSIONS.tsv` (this one carries `# Last real data refresh: 2026-09-18`), `registry/corrections_receipts.tsv`, `thesis/PREDICTIONS.tsv`. HAWK has **no `workbook/LEDGER_GLOB`**. The two-clock header `Last real data refresh:` appears **nowhere in `workbook/`** (only in `domain/europe-rearm/LADDER.md` and `INCURSIONS.tsv`). Every LIVE workbook ledger is therefore graded on git-commit time.

---

## 2. Scripts / guards table

| Script | What it claims | Invoked by | Ran? result | Discriminates? (evidence) |
|---|---|---|---|---|
| `derived_freshness.py` (live; 5,341 B) | sha256 fingerprints for 2 aggregates and 11 owner edges; rc 0 agree / 1 drift / 2 missing | **CLAUDE boot 6a-3 + closeout 13a-2** (FILES.md L69). Its docstring still says "closeout 13b", which is stale: 13b is now the FALSIFICATION page. | ✅ default mode (read-only): **rc=1**, `REVIEW: … changed AGENTS/FALCON/NEXUS_BRIEF.md` on both aggregates (FALCON committed it 10/22 13:37, after HAWK's 10/22 01:39Z record) | ✅ **YES, both directions, run in memory with no writes.** Real receipt reports exactly the one genuine drift. Flipping the FALCON WARRISK input digest adds that edge. Flipping the output digest adds the output edge. Dropping one edge raises `ValueError: dependency scope differs` (rc-2 path). Limit: the edge list is static. A FALCON `KB-` citation in CROSS_WAR_SUMMARY is outside it (inferred), and a newer owner analysis replacing the 9/16 REPORTs is caught only if HAWK edits the list by hand (CLAUDE 6a-3 says so). |
| `war_monitor.py` (frozen scenario constants; fail-loud source accounting since 9/02) | reached N/M; partial coverage suppresses interpretation; rc 0 only on full coverage, 2 otherwise; `--save` gated | nobody (only frozen boot.py) | ✅ default: `reached 5/5`, **rc=0**. `--selftest`: `reached 5/6`, DEAD SELFTEST-DEAD (URLError), INTERPRETATION SUPPRESSED, **rc=2** | ✅ The coverage guard discriminates both ways. 🟠 **But an interpretation bug was observed live:** the same full-coverage run printed `🔴 Escalation indicators detected / Impact: D +5-10%` **and** `🟡 No keyword shift across a FULLY covered scan`. Cause: `calculate_scenario_shift` does `int("5-10")`, which raises ValueError and is swallowed by a bare `except: pass` (verified: `parse fails: ValueError invalid literal for int() with base 10: '5-10'`). The escalation branch can never move D, so the interpretation line can never print the 🔴 path. The script was declared honest on 9/02, and this is the same silent-swallow class it was repaired for. It also prints "War Day 235 / Ceasefire Day 193" from hardcoded 3/1 and 4/12 anchors. |
| `thresholds.py` (FROZEN banner) | Brent zones vs $60/80/100/120/150; `--save` writes PRICE_BREACHES | nobody | ✅ `--quick` (cached, no network, no write): **rc=0**, `BRENT CRUDE: $94.28 (+0.00%)`, zone C, `$100 🟢 Clear`, "✅ No active alerts" | ❌ The cached-price path builds a `"2026-04-20 (cached)"` timestamp but **never prints it**, so it shows a 185-day-old price with no date. Live Brent per KB-HAWK-440 was $110.03 on 10/21. The alert ladder has a dead branch: `elif … price >= 120` sits under `if … price >= 100`, so CRITICAL can never print. Not cited (banner says do not). Default/live mode not run (it would fetch over the network). |
| `catalyst_countdown.py` (no in-file banner) | Days-to-event from CALENDAR.md | nobody | ✅ rc=0. Header `War Day: 51 \| Scenario: D 82% / C 12% / B 6%` (hardcoded). Only 6 "Ongoing" TBD rows parsed, no dated events. | ❌ Its parser handles only `Mon DD` forms, so ISO-dated rows are invisible and a run would show no imminent events. It reads CALENDAR.md, not CATALYSTS.tsv, so the 21 past-dated PENDING catalysts are invisible to it. |
| `oil_infrastructure.py` (no in-file banner) | Gulf facility status and repair timelines | nobody | ✅ rc=0. "4 of 6 DAMAGED (67%)", every row `Last update: 2026-04-13` | ❌ Hardcoded registry, nothing fetched. It cannot fail and prints 6-month-old status at rc 0. `--save` would create `workbook/INFRASTRUCTURE*` files (not run). |
| `sanctions_tracker.py` (FROZEN banner) | Shadow-fleet, enforcement, insurance scan | nobody | ✅ rc=0. Prints `🔴 Enforcement: Detected in news flow` **and**, in its own SIGNAL SUMMARY, `Enforcement: No new actions` (hardcoded) | ❌ Both Reuters feeds are **DEAD** (probed: `URLError Errno -2`), yet nothing reports it. `run_web_search`/`fetch_rss_feed` use bare `except: return ""/[]`, the exact dead-feed-equals-quiet-world defect war_monitor fixed on 9/02. All metrics are BASELINE placeholders. |
| `boot.py` (FROZEN banner L1-16) | Orchestrates the 5 monitors | nobody | **NOT RUN.** Not read-only: `save_boot_log()` appends to `workbook/BOOT_LOG.md` (a FROZEN file) on every run, pass or fail. Hardcoded "War Day: 51" banner. | n/a. A runnable writer into a frozen file with no runtime refusal. Its sub-scripts' rc contracts are mixed (war_monitor 0/2, the rest always 0). |
| `scripts/PLAN.md` | 4/20 "Draft" automation plan | — | read head + grep | Has no FROZEN/superseded marker. It describes the frozen suite as a plan. |
| `__pycache__/` (2 .pyc, 9/25) | interpreter cache | — | untouched (mtimes unchanged, 2026-09-25) | FILES.md L65 classifies it as non-instrument |

Fleet tools (repo-root `scripts/`) as HAWK guards: `ledger_staleness` (boot 6a), `corrections_boot_check` (6a-2), `read_cap_check` (closeout 10), `claim_check` (root 1e). Discrimination evidence for these is in §3.

---

## 3. Fleet-check results (verbatim key lines)

```
$ python3 scripts/ledger_staleness.py HAWK            # rc=0
  ok         +11d  AGENTS/HAWK/workbook/CATALYSTS.tsv
  ok         +23d  AGENTS/HAWK/workbook/FLOW.tsv
  ok          +0d  AGENTS/HAWK/workbook/KB.tsv
  FROZEN     +72d  AGENTS/HAWK/workbook/PRICE_BREACHES.tsv
  ok          +0d  AGENTS/HAWK/workbook/VX.tsv
  perimeter [HAWK]: 6 ledger(s) scanned; 4 TSV(s) NOT scanned by this pass: domain/energy-strikes/STRIKES.tsv, domain/europe-rearm/INCURSIONS.tsv, registry/corrections_receipts.tsv, thesis/PREDICTIONS.tsv
```
(It reports "6 scanned" but prints 5 rows. The 6th is probably SCHEMA.tsv suppressed from the listing; inferred, not traced.) `--quiet` prints only the perimeter line, rc 0. `--nudge HAWK`: `STATUS not moving this session — no gap being created`, rc 0.

```
$ python3 scripts/ledger_staleness.py --trade HAWK    # rc=0
  FROZEN    +112d  AGENTS/HAWK/TRADE.md
trade perimeter: 1 agent(s) with a matching trade surface graded; 0 agent(s) matched NO trade surface and are NOT certified by this pass
```

```
$ python3 scripts/read_cap_check.py --agent HAWK      # rc=0
  ✅ LESSONS.md        23,180 B    71% of budget  ↳ 70–75% BAND … Headroom to the trigger: 1,232 B.
  ✅ STATUS.md         15,819 B    49%
  ✅ NEXUS_BRIEF.md     7,961 B    24%
  ✅ SCRATCH.md         6,471 B    20%
  ✅ workbook/SCHEMA.tsv 2,113 B    6%
✅ READ-CAP 0 [HAWK] … ⚠️ PERIMETER IS THE CHARTER HEURISTIC — this desk has no declaration in PROME/registry/READS.tsv
  ℹ️  charter AGENTS/HAWK/CLAUDE.md = 28,967 B — OUT OF PERIMETER by rule 20 unless declared
READ-CAP-RESULT v1 … reads=5 over_budget=0 … rotation_due=0 … charter_bytes=28967
```
(LESSONS was rotated 10/21 per commit `7943b8bdb`. It sits at 71%, so if that rotation targeted <70% it is 396 B short. Only the owner knows which case applies.)

```
$ python3 scripts/corrections_boot_check.py HAWK      # rc=0  (verified read-only first: writes only under --receipt / --selftest tempdir)
  INFO 1 dead-at-cap with no receipt from this desk: COR-20260925-13 — 0 NAMED … 1 ALL-row (broadcast expired: no warn, no block)
CORRECTIONS-CHECK 0 OK: 0 unreceipted NAMED rows for HAWK (register 100 row(s), 0 ALL-warn, 1 ALL-row(s) past cap unreceipted …; receipts on file: 16)
```

```
$ python3 scripts/claim_check.py --check weekday AGENTS/HAWK/STATUS.md AGENTS/HAWK/CALENDAR.md   # rc=0
CLAIM-CHECK ✓ 2 file(s) clean [weekday]
$ … AGENTS/HAWK/workbook/CATALYSTS.tsv  → CLAIM-CHECK ✓ 1 file(s) clean [weekday]  rc=0
$ python3 scripts/claim_check.py --selftest → CLAIM-CHECK SELFTEST ✓ 36/36 cases behaved [weekday]  rc=0
```
Both-directions check on HAWK's actual form (in-memory `check_text`). Real line `**Last Updated:** 2026-10-21 Wed 21:38 ET` gives `[]` (correct, 10/21 is a Wednesday). Mutated to `Thu` it flags `2026-10-21 is a Wednesday, not Thu`. ✅ Discriminates. STATUS carries exactly one weekday claim; CALENDAR carries none.

**Fleet-tool defect found while testing (DAEDALUS-owned `scripts/claim_check.py`, not HAWK's):** passing a path with no allowed suffix (I used process substitution `/dev/fd/63` containing `Thursday 2026-10-23`, which is wrong) printed `CLAIM-CHECK ✓ 1 file(s) clean` rc 0. `check_file()` returns `[]` for an unsupported suffix or a non-file, and the file still counts toward "N file(s) clean". This is the PAT-074 zero-bytes-read-certified-clean class again, on the suffix branch rather than the directory branch the 9/xx fix closed. Verified.

**Concurrency note:** `git status` at the end shows ` M scripts/ledger_staleness.py` (mtime 17:45:24) and ` M scripts/read_cap_check.py` (mtime 17:46:59). Both changed during this window, and **not by this reader**: I made no edits, and every command I ran was a read or a run of a HAWK script from cwd `/tmp`. Another session is editing the fleet tools. My ledger_staleness run (~17:43) predates the edit. The `--nudge`/`--quiet` runs (~17:47) used the edited working tree.

---

## 4. Findings

| # | Sev | Finding | Evidence | V/I |
|---|---|---|---|---|
| 1 | 🔴 | **CATALYSTS.tsv write-back is broken.** 21 of 37 rows are PENDING with dates 9/09–10/18, and the ledger has not been committed since 10/10. The 10/21 session **did** the N6 Sept/Oct observations (KB-448) and the dormant re-sweep (KB-451) but left their catalyst rows (9/09, 10/07, 9/24) PENDING. `ledger_staleness` grades the file `ok +11d` because it measures file age, not row currency. The "dated-obligation ledger" (FILES.md L63) cannot currently be trusted to say what is owed. | CATALYSTS rows listed in §1; `git log` 62240556c 10/10; KB-HAWK-448/451 dated 10/21 | V |
| 2 | 🟠 | **KB Stale_By is decorative.** 113 post-split ACTIVE rows are past their Stale_By (213 set it). No tool, boot step or closeout step reads the column. The CLAUDE "currency pass" (L169) only filters at query time. | python count over KB.tsv | V |
| 3 | 🟠 | **war_monitor's escalation branch is dead.** The `D +5-10%` impact string fails `int()` inside a bare `except: pass`, so the 🔴 interpretation can never print. A live run showed 🔴 signal + 🟡 "No keyword shift" in the same output. The script is frozen and unwired, but it is the one script the desk called honest (9/02 FAIL-LOUD contract). | live run 17:45, rc 0; parse repro | V |
| 4 | 🟠 | **Frozen-suite banners are incomplete.** `catalyst_countdown.py` and `oil_infrastructure.py` carry **no in-file FROZEN banner**: a reader opening either sees nothing, both run rc 0 on April constants, and the freeze lives only in boot.py's docstring, FILES.md and CLAUDE L223. `boot.py` is a frozen file that still **appends to the FROZEN BOOT_LOG.md** whenever it runs, with no refusal. | grep -c FROZEN = 0 on both; boot.py `save_boot_log` | V |
| 5 | 🟠 | **sanctions_tracker still swallows errors silently**, the defect war_monitor was repaired for. Both Reuters feeds are dead (probed 17:46) and it reports nothing. Its output contradicts itself ("Detected in news flow" vs "No new actions"), rc 0. Old-profile claim "sanctions LANE genuinely unbuilt" still holds. | live run + feed probe | V |
| 6 | 🟠 | **derived_freshness is DUE now (rc 1).** FALCON NEXUS_BRIEF changed 10/22 13:37 −0400, after HAWK's 10/22 01:39Z record. This is correct guard behaviour, and the next HAWK boot owes a reconcile of both aggregates. | rc 1 output; git log of input | V |
| 7 | 🟡 | **VX TRADE-01 hits the 45d backstop on 10/25** (Last_Updated 9/10, 42d). Its Guard cell has prose appended after the token (`CLOCK+EVENT \| ADOPTION-STAGE …`), so it is not a clean vocabulary token for any machine reader (finding_text_appended_after_a_machine_read_object). | VX parse | V |
| 8 | 🟡 | **CATALYSTS 10/03 "EURMIL first 45-day checkpoint" contradicts its own arithmetic.** EURMIL was registered 9/18, and 9/18 + 45d = 11/02. The real backstop date is not on the ledger. | row text; date arithmetic | V |
| 9 | 🟡 | **Open-prediction dates are only partly on the dated ledger.** HAW-20 10/31 has a CATALYSTS row. HAW-22's 12/15–12/21 final-search window and 12/22 resolution are not on CATALYSTS (STATUS L67 carries them). PREDICTIONS has no Resolve_By or anchor_type column; both are prose in Notes. Both OPEN rows are anchored IMMOVABLE. None is past due. | grep CATALYSTS/STATUS; PREDICTIONS Notes | V |
| 10 | 🟡 | **Boot step 6(b)'s awk `NR==1 \|\| $6=="OPEN"` prints the first comment line, not the column header** (the header is line 22). OPEN rows reach the reader with no column names (finding_a_verbatim_cell_without_its_column_header). | ran the awk: line 1 = `# HAWK Predictions — Calibration Record` | V |
| 11 | 🟡 | **Count/size drift in the inventory surfaces.** FILES.md L18 says "FLOW 7 rows" (actual 8: FLOW-21 registered 9/11 is missing). FILES.md L19 and CLAUDE L47 say "~69 KB" for PREDICTIONS (actual 96,616 B; still over cap, so the directional rule holds). CLAUDE L69 closeout 11 says "VX.tsv (10 rows, including the superseded…)" (actual 11; CLAUDE L54 and FILES L17 say 11). The PREDICTIONS preamble L20 "HAW-10 9 cols / HAW-11 11 cols" is stale (all are 10). derived_freshness docstring says "closeout 13b" (actual 13a-2). | wc/awk vs text | V |
| 12 | 🟡 | **No two-clock header on any workbook ledger, and no LEDGER_GLOB.** Freshness falls back to git time (root Data Hygiene prefers a content-derived vintage). PREDICTIONS.tsv and the domain TSVs sit outside the staleness perimeter (the tool discloses this). | grep; tool perimeter line | V |
| 13 | 🟡 | **board_log truncated-key residue.** Two 9/02 `deferred` rows keyed on truncated IDs were closed 9/08 under the full filenames, so by-ID they read as permanently open. Timestamps use 3 formats. | awk over board_log | V |
| 14 | 🟡 | **FOUR_STRUCTURAL_BREAKS_MAR18.md has no freeze banner.** Its only `FROZEN` token is body prose (L75), which is a marker-word-in-prose hazard for any banner scanner. FILES.md L40 asserts it is frozen. | head + grep | V |
| 15 | 🟡 | **LESSONS.md is at 71% of budget after a 10/21 rotation** (1,232 B to the 75% trigger). If that rotation was a rule-5 rotation it stopped 396 B short of <70%. | read_cap_check output | V (number) / I (whether owed) |
| 16 | 🟡 (fleet, not HAWK) | **`claim_check.py` counts unsupported-suffix paths as clean files** (`✓ 1 file(s) clean` over zero bytes read). Route to DAEDALUS `scripts/` duty. | /dev/fd repro | V |
| 17 | 🟡 | **KB pre-split band schema debt is preserved, not cleaned:** 10 width defects, 9 off-vocabulary cells, dup IDs 131/132. This is declared and intentional (SPLIT-NOTE; batch2 acceptance json says "no assertion that whole legacy ledger is schema-clean"). Post-split rows are clean. | python validation | V |

Clean / working as designed: corrections receipts (16, rc 0); read-cap all under budget; PRICE_BREACHES and TRADE.md properly FROZEN; PREDICTIONS tally is arithmetically consistent with its latest preamble line; no OPEN prediction is past due; derived_freshness discriminates; war_monitor's coverage guard discriminates; claim_check weekday discriminates on HAWK's form; VX GRADING-DECLARATION (eyeball-graded by design) is consistent with boot.py being unwired.

---

## 5. Reconciliation against the old profile (`profiles/HAWK.md`, body 8/07; §3, PAT-089 items, File anatomy, ★Correction)

| Old claim | Verdict | Now |
|---|---|---|
| EXIT_PROTOCOL.md "140d, unstamped… **must NOT be frozen**" | **CHANGED** | FROZEN 2026-08-10, with a "most dangerous dead surface / do not execute" banner (contrary to the profile's 8/07 advice; the profile's own L7 notes this trigger fired) |
| Unbannered MARCH COHORT (POLITICAL_SUSTAINABILITY, DECK_EVIDENCE, BOOT_LOG) | **CHANGED** (mostly closed) | POLITICAL and BOOT_LOG FROZEN 8/10; DECK_EVIDENCE bannered 9/28. **FOUR_STRUCTURAL_BREAKS still has no banner** (F14). |
| PREDICTIONS 18 rows: 5C/8F/1P/1V/2R/1 OPEN; sole OPEN HAW-18 → 9/1 | **OBSOLETE** | 22 rows: 6C/9F/1P/1V/2R/1 DEFECTIVE/2 OPEN (HAW-20 → 10/31, HAW-22 → 12/22, both IMMOVABLE). HAW-18 FAILED 8/04; WQ-208 scoring vintage ruled 55%. HAW-19 DEFECTIVE-INSTRUMENT 9/28. |
| Dormant book 9 VX rows; 45d clock expired 8/4 | **CHANGED** | 11 rows (EURMIL-01 added 9/18, CODIF-01 earlier); 5 re-swept 10/21. Next clock: **TRADE-01 on 10/25**. The clock now also has CATALYSTS rows (partly wrong, F8). |
| FLOW 6 rows; FLOW-10 self-deferred past 8/4 | **CHANGED** | 8 rows (FLOW-21 added 9/11). FLOW-10 still MUTED dormant-armed with "[STALE Apr20 figs]" in Current_Position, so the stale-figure carry is **STILL TRUE** in substance. |
| KB 253 lines → KB-HAWK-249; dup 131/132 known-frozen | **CHANGED / STILL TRUE** | 456 lines → KB-HAWK-452; dups unchanged and declared |
| "boot 0-8 invokes NO HAWK script — only repo-root ledger_staleness" | **OBSOLETE** | Boot now runs ledger_staleness (6a), corrections_boot_check (6a-2) **and HAWK's own `derived_freshness.py` (6a-3)**, which also runs at closeout 13a-2 |
| "five scripts exit rc=0 printing stale constants" | **CHANGED** | 4 of 5 still do (thresholds, catalyst, oil_infra, sanctions; reproduced today). war_monitor was rebuilt 9/02 to rc 0/2 fail-loud (verified both ways) but has a new dead escalation branch (F3). |
| "sanctions-tracker LANE genuinely HAWK's and genuinely unbuilt" | **STILL TRUE** | Frozen, silent-swallow, 2 dead feeds (F5) |
| boot.py "invokes all five unconditionally" REFUTED | **STILL TRUE (refutation holds)** | boot.py is invoked by nothing. New nuance: if run by hand it **writes into frozen BOOT_LOG.md** (F4). |
| CROSS_THEATER_WAR_RISK 5/5 legs past bar; CROSS_WAR_SUMMARY understates sibling | **CHANGED** (mechanism added) | Now guarded by derived_freshness fingerprints. Today it reads rc 1 on FALCON NEXUS_BRIEF drift (F6). Leg-age content is the architecture reader's lane. |
| board_log 7/28 "22 undispositioned behind it" | **OBSOLETE** | Newest row 10/22 01:38Z. L0 drain 10/10 (66/66 WALTER) and 10/21 intake. 491 rows, 7 deferred (5 closed under same key, 2 under a different key). |
| Ledgers had no workbook TSV for catalysts | **CHANGED** | CATALYSTS.tsv created 9/08; it is now itself stale (F1) |
| PRICE_BREACHES / TRADE / CALENDAR frozen-with-successor 7/9 | **STILL TRUE** | PRICE_BREACHES FROZEN +72d; TRADE FROZEN +112d |
| PAT-089 "correctly quiet: HAW-18 Sep-1, US-China truce Nov-10" | **CHANGED** | HAW-18 resolved. Nov-10 Chinese export-control clock is still on CATALYSTS (PENDING 11/10; KB-442 says the truce extension to 2027-01-10 is ANNOUNCED-only). New PAT-089 candidates: the 21 past-dated PENDING catalysts (F1), TRADE-01 10/25, HAW-20 10/31. |

---

## 6. Coverage & proof of no writes

**Read whole:** `scripts/boot.py`, `derived_freshness.py`, `thresholds.py`, `war_monitor.py`, `catalyst_countdown.py`, `sanctions_tracker.py` (L1-60, 60-215, 247-336; L216-246 are the `--save` writers, seen via grep); `audits/2026-09-10_HAW18_WQ112_application.md`, `audits/2026-09-08_batch2_documents.md`, `audits/2026-09-08_batch2_acceptance.json`, `audits/2026-09-08_derived-acceptance.json`; `registry/corrections_receipts.tsv` (cells cut at 260 chars), `registry/derived_inputs.json`; `workbook/SCHEMA.tsv`; `workbook/PRICE_BREACHES.tsv`.
**Parsed programmatically (every row, selected cells displayed):** KB.tsv (454 rows), VX.tsv (11), FLOW.tsv (8), CATALYSTS.tsv (37), PREDICTIONS.tsv (22 + preamble L1-21; HAW-20/22 cells read in full up to ~1,500 chars each), board_log.tsv (491).
**Read partially:** `oil_infrastructure.py` (L1-45 + IO grep; ran it), `scripts/PLAN.md` (head 15 + FROZEN grep), the 5 workbook .md heads (first 5 lines), KB-HAWK-435..452 Fact cells (170 chars), KB-448 (600 chars), HAWK `CLAUDE.md` lines 47-54, 68-74, 220-225 + grep, `FILES.md` grep lines, old profile L22-42 and L50-51 + grep.
**Not read:** the other 22 audits (inventoried by name, size and last-commit only); `PREDICTIONS_ARCHIVE.md`; domain/, thesis/ other than PREDICTIONS, STATUS/SCRATCH/NEXUS bodies (other readers' clusters); `thresholds.py` live mode and `--save` modes of every script; `boot.py` (not run, because it writes).
**Commands run:** `ledger_staleness.py HAWK` / `--trade HAWK` / `HAWK --quiet` / `--nudge HAWK`; `read_cap_check.py --agent HAWK`; `corrections_boot_check.py HAWK` (read-only path confirmed by reading `main()`); `claim_check.py --check weekday` on STATUS+CALENDAR and on CATALYSTS, plus `--selftest` and in-memory `check_text` both directions; HAWK `derived_freshness.py` (default) + in-memory `inspect()` mutation tests; `war_monitor.py` default and `--selftest`; `catalyst_countdown.py`; `oil_infrastructure.py`; `thresholds.py --quick`; `sanctions_tracker.py` (default) + urllib probe of its 2 Reuters feeds. All Python ran with `PYTHONDONTWRITEBYTECODE=1`; HAWK scripts ran from cwd `/tmp`.
**Proof of no writes:** `git status --short -- AGENTS/HAWK` was empty at 17:42:51 and empty again at 17:47:19. `AGENTS/HAWK/scripts/__pycache__` mtimes are unchanged (2026-09-25). No `WAR_LOG.md`, `SCENARIO_HISTORY.tsv`, `SHADOW_FLEET.tsv`, `SANCTIONS_LOG.md` or `INFRA*` file exists in `workbook/`. The `M` flags on repo-root `scripts/ledger_staleness.py` and `scripts/read_cap_check.py` come from a concurrent session (mtimes 17:45:24 / 17:46:59), not from this reader. Only file written: this one.
