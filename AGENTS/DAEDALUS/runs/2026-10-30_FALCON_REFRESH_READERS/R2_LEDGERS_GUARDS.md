# R2 — LEDGERS · FALSIFICATION · GUARDS (FALCON whole-profile refresh)

**Reader:** R2 of 3 · **Started:** 2026-10-30 17:38:47 EDT · **HEAD:** b2188833f · read-only on tracked files; only write = this report. Scratch copies at /tmp/claude-1000/falcon-r2/.
**FALCON tree at start:** `git status --porcelain -- AGENTS/FALCON/` = empty (clean) at 17:38:47.

**Status:** COMPLETE 2026-10-30 17:48 EDT. Sections A–I below. Verified = receipt in a file:line or a command run here; Inferred = marked I.

## A. Ledger table (workbook/ 7 files + adjacent instrument TSVs)

| File | Rows | Header clock(s) | LIVE/FROZEN | ledger_staleness verdict (17:40) | Notes (Verified unless marked) |
|---|---:|---|---|---|---|
| `workbook/VX.tsv` | 10 vectors (L3–L12) + 1 comment + header | **none** — no `Last real data refresh`, no Cadence line; per-row `Last_Updated` 10/29–10/30 | LIVE | ok +0d (git-commit fallback); `--nudge` rc1 "VX.tsv 1 STATUS-write behind" | Band integrity defects → §F. **`VX-HAWK-BABMANDAB-01` Notes cell = bare `2026-09-14` (10 B)**: 695 B of Notes history overwritten by commit `a8d259b44` (9/14, gate review) — Last_Updated stayed 2026-09-08 that commit, so the date landed in the wrong column. Undetected 46 days; prior text recoverable at `c4b8c83b9:AGENTS/FALCON/workbook/VX.tsv` |
| `workbook/EXIT_PROTOCOL.md` | 111 lines | in-content `v3 REWRITTEN 2026-10-01`; `Closeout reviewed 2026-10-26` (:4); §2 line reconciled 10/30 (:42); §5 last review 10/29 | LIVE (STATE rail) | n/a (not .tsv); `falsification_scan` STALE-FLAGGED 29d (§E) | §1 header "status 2026-10-01", §2 table "Status 2026-10-01", §3 "status 2026-10-01" — kill-cell evidence is 10/01-vintage (PortWatch 1/88 9/27; Brent $100.83 10/01; war-risk 6–9% 9/25). Verdicts (0/7) still hold on current evidence I can see (VX IRAN-02 10/30: PortWatch 2 total 10/25) but the cells are 29d old. §3 #7 cell (stamped 10/26: "no newer print than October 16 … HOLDING 92,073 vs floor 32,115") is behind VX IRAN-02 [Oct30] "bypass DEGRADED (Sohar empty), Fujairah HOLDING to 10/23" — two surfaces, two states |
| `workbook/KB.tsv` | 376 (KB-FALCON-001..376, 0 duplicate IDs) | none (append log); newest Date 2026-10-30 (7 rows) | LIVE | ok +0d | **179 ACTIVE rows past their own `Stale_By` (61 >30d past)** — Status column not maintained against Stale_By. 4 Status values off the SCHEMA enum (`ACTIVE;CONFIRMED;STALE;SUPERSEDED;CORRECTED`): KB-092 `SUPERSEDED-SEE-KB-095-FIRED`, KB-094 `CONFIRMED-SECONDARY`, KB-095 `FIRED`, KB-166 `UNVERIFIED-CLAIM` |
| `workbook/WARRISK.tsv` | 5 data rows (L30–34) + 28 comment lines | `Cadence: EVENT-DRIVEN` (:1, added `35bd7d149` 10/26) · `Last re-pull ATTEMPTED: 2026-10-26` (:2) · `Last real data refresh: 2026-09-25` (:4) | LIVE | **quiet +36d** `[EVENT-DRIVEN re-pull 2026-10-26]` at default AND at FALCON's own `--days 7` | Data clock 35d old; all 5 rows EXPIRED per own guard (rc1, 🎯 falsifier +24d). **The 7-day gate is disarmed — see §E/§H #1** |
| `workbook/FLOW.tsv` | 5 (FLOW-FALCON-01..05) + 6 comment lines | `Last real data refresh: 2026-10-01` · `Cadence: EVENT-DRIVEN` · `Last re-pull ATTEMPTED: 2026-10-26` | LIVE | ok +30d (one day under the 30d default) | Conservation line (16 = 4+11+1, written 10/26) is now short by one: FLOW-FALCON-05 (Iranian administrative enforcement on Sinokor fleet, ARMED, eff. 11/01) added `eb3a39f88` 10/29 without advancing the data clock (still 10/01) or the count line. Verified: pre-split file `35bd7d149~1` held 01,02,03,04×2 + 11 HAWK = 16. Data clock 10/01 sits at +30d — the default 30d gate fires on the next STATUS write unless the clock moves; but a NEW row written 10/29 under a 10/01 data clock is itself a two-clock mismatch |
| `workbook/FLOW_HAWK_MIGRATED_FROZEN.tsv` | 11 | `FROZEN 2026-10-26` banner | FROZEN | FROZEN | Correct form (root Data Hygiene (a)) |
| `workbook/SCHEMA.tsv` | 13 | none | reference | exempt by name; `--strict` ⚠️ STALE +110d | Verbatim-from-HAWK, DO-NOT-TOUCH #8; benign |
| `domain/vessel-incidents/VESSELS.tsv` (SUNK-01 instrument) | ~95 data | `Last real data refresh: 2026-10-30` | LIVE | **NOT SCANNED** (outside `workbook/*.tsv`; no `workbook/LEDGER_GLOB`) | 8/15 Δ② "outside the glob, nothing reads it" — still outside the glob 76 days later |
| `domain/casualties/CASUALTIES.tsv` (CASUALTY-01 instrument) | ~38 | `Last real data refresh: 2026-10-26` | LIVE | **NOT SCANNED** | Rate-step last computed 10/26 ("not recomputed" per VX [Oct29]) on a rolling window |
| `domain/energy-strikes/STRIKES.tsv` (rung §2a evidence) | ~50 | `swept-complete through: 2026-10-29` (reviewed 10/30) | LIVE | **NOT SCANNED** | Current |

Perimeter line printed by the tool itself: "6 ledger(s) scanned; 5 TSV(s) NOT scanned" — the three instruments behind VX SUNK-01 / CASUALTY-01 / §2a are in the unscanned set.

## B. Predictions (`thesis/PREDICTIONS.tsv`, 38 lines: 30 comment/header-preamble + column header + 7 rows)

| Row | Made | Conf | Window / Resolve_By | Status | Dated search instrument (WQ-172/433 form) | Notes |
|---|---|---:|---|---|---|---|
| FAL-01 | 07-12 | 70% | Jul 12–26 | FAILED 07-27 | n/a (pre-rule) | pointer row → `archive/PREDICTIONS_snapshot_2026-10-26.tsv#FAL-01` (archive row present, 869 B) |
| FAL-02 | 07-12 | 65% | Jul 12–17 | CONFIRMED 07-17 | n/a | pointer; archive 864 B |
| FAL-03 | 07-27 | 58% | Jul 27–Aug 17 | FAILED 07-30 | n/a | pointer; archive 1,571 B |
| FAL-04 | 07-30 | 62% | Jul 30–Aug 20 | PARTIALLY 08-20 | n/a | pointer; archive 2,367 B |
| FAL-05 | 09-07 | 55% | Sep 7–Oct 7 | FAILED 09-28 | n/a | pointer; archive 3,225 B |
| **FAL-06** | 10-01 | 70% | Oct 1–**Nov 5** (CONFIRMED if no route fires by 11-05 23:59 ET) | OPEN | **Compliant:** "run on 2026-11-05 (floor = ceiling = the resolve date) … after 11/05 = NO-VERDICT" (WQ-433 adopted 10/14). Sources named: operator/state FM notices + latest Kpler/Vortexa weekly print per country | Due in 6 days. Own Notes disclose "no held weekly national-export series; route (c) depends on vendor publication" — route (c) can only be graded on a print somebody else publishes |
| **FAL-07** | 10-21 | 65% | Oct 22 00:00–**Dec 31** 23:59 ET | OPEN | **Non-compliant as written:** FAILED requires "a dated search run on 2027-01-02 … a later attempt = NO-VERDICT" — 2 days outside the window (WQ-172 ceiling = resolve date) | Routed: **WQ-559** registered by PROME 10/30 (`PROME/WILL_QUEUE.md:55`, DECISION, due 12-15, rec A = search ON 12-31, re-present 12-10). Verified |

**Scoreboard:** header :4 "1C / 3F / 1P / 0V / 2 OPEN" — recomputed from Status cells: C=FAL-02; F=01,03,05; P=04; OPEN=06,07 → **matches**. Past-due OPEN rows: **0**. Brier: **0 mentions** in PREDICTIONS or the archive snapshot — "no Brier by choice" (prior profile, n=4) still the posture at n=5 resolved; prior trigger was "revisit n≈8". Header rotation: 9 dated "As of" lines + 3 "Prior header" lines, newest first, no row edited by interim grades — clean append discipline.

**FAL-07 wording exposure (Verified text, severity Inferred):** the Prediction cell says "at least one **OFFENSIVE** kinetic strike"; NEVER-COUNTS lists only *interception* as the defensive exclusion; the row's own MODAL OUTCOME CHECK says a self-defence strike at sea is "counted only if offensive". The 10/30 interim grade (KB-FALCON-372 Notes) has already adopted a reading — a "defensive manner" strike on a Qeshm launcher "WOULD meet COUNTS (a); the 'defensive' framing is not a NEVER-COUNTS item". That reading is defensible, but it settles the headline adjective inside a grade note, before any confirmation lands, on a 65% row. Same family as HAW-10/14/15, FAL-01/03 (wording wedge, n=5 on the desk's own header :15). Second instrument limit in the same note: "No Reuters/AP/Bloomberg/AFP report … found (those domains unreachable to this box's search - limitation)" — the confirmation path's two-wire limb, and the 1/2-or-12/31 FAILED search, both name sources this box cannot search.

## C. Falsification surface inventory

| Surface | Kind | In-content stamp | In force? | Scanned by `falsification_scan`? |
|---|---|---|---|---|
| `workbook/EXIT_PROTOCOL.md` §0–§3 (regime, 7 kills, ladder, 8 D-indicators) | STATE | `v3 REWRITTEN 2026-10-01` (:3); `Closeout reviewed 2026-10-26` (:4); §1/§2/§3 table headers "status 2026-10-01" | Yes; 0/7 kills; marks B1/C14/D85 | Yes — **STALE-FLAGGED 29d** (stamp 10/01 vs ref 10/30; "header also carries 2026-10-26") |
| `workbook/EXIT_PROTOCOL.md` §2a production rung D 85→92 | STATE (registered letter, immutable) | REGISTERED 2026-10-01 WQ-355 | ARMED, not fired | (inside the same file) |
| `workbook/EXIT_PROTOCOL.md` §5 time-based review + DATED rewrite trigger | STATE (clock) | last review 2026-10-29, next 2026-11-04; rewrite trigger 2026-11-05 | Yes, current | — |
| `archive/EXIT_PROTOCOL_archive_2026-10-01.md` §2 D 75→85 letter | APPEND-ONLY (canonical letter, spent) | 2026-09-08 | Spent (fired 9/28 on (b), "cannot fire again") | — |
| `thesis/PREDICTIONS.tsv` FAL-06, FAL-07 | EVENT (dated rows) | header As of 2026-10-30 | 2 OPEN | **No** (pattern set did not list it) |
| `workbook/WARRISK.tsv` 🎯 WC-Saudi registered falsifier + MIRROR watch line #2 | STATE | data 2026-09-25; attempt 2026-10-26 | Registered, but the falsifier leg is EXPIRED +24d and the file gate is quiet (§E) | No |
| `workbook/VX.tsv` 10 band rows | STATE | per-row Last_Updated 10/29–10/30; no file clock | Partly — see §F (4 rows carry retired/no-instrument or stale "current" band text) | No |
| `domain/CASUALTY_RATCHET.md` + `CASUALTIES.tsv` (D-indicator #5) | STATE + APPEND-ONLY ledger | last commit 10/26; ledger clock 10/26 | RED rate-step 24 vs 7 (computed 10/26, not recomputed since — rolling-30d window has moved 4 days) | No |
| `domain/vessel-incidents/VESSELS.tsv` (SUNK-01, D-indicator #6) | APPEND-ONLY | `Last real data refresh: 2026-10-30` | Census 6 | No; also outside ledger_staleness glob |
| GATE-FALCON-001 (STATUS.md:15; VX BABMANDAB) | STATE | reviewed 10/29, next 11/04 | LIVE; leg 2 NOT MET (80.0% vs ≤65%) | No |
| `domain/FALSE_FIRE_REGISTER.md` | APPEND-ONLY (guards) | last commit 10/14 | Yes (DO-NOT-TOUCH #5 class) | No |
| `thesis/CHANGELOG.md` | APPEND-ONLY | newest entry 2026-10-29 | n/a | Yes — CURRENT |

Scanner perimeter: 2 surfaces found for FALCON; 10 of the 12 above are outside its pattern set. That is by design for row-ledgers, but it means sweep #5's "1 STALE / 1 CURRENT" is a statement about two files, not the rail.

## D. Trade leg (FLEET_MAP reading A3)

| Leg of A3 | Still holds? | Receipt |
|---|---|---|
| Charter excludes oil as a trade | **Yes** | `AGENTS/FALCON/CLAUDE.md:257` "Oil as a trade → LIQUID (tanker/crude positions live there)"; :7 OIL HANDOFF to BRENT; :261 price levels → BRENT |
| FALCON owns theater signals | Yes | `CLAUDE.md:237-249` DOMAIN SCOPE |
| HAWK consumes them | **Yes, current to FALCON 10/26 + the 10/29 QUBA review** | `AGENTS/HAWK/STATUS.md:18` "FALCON (KB-HAWK-468): B 1 / C 14 / D 85 held … MSV QUBA … 6 confirmed losses"; HAWK STATUS updated 10/29 13:5x. FALCON's 10/30 grade (LOUISE 1 / RITI / Qeshm) post-dates HAWK's close — expected lag, not a defect |
| No TRADE file obligation | Holds | no `TRADE.md` / `trade/` in tree; `ledger_staleness --trade` rc0 "matched NO trade surface … NOT certified" (honest perimeter line) |
| Rung ≠ trade signal | Holds | `EXIT_PROTOCOL.md:66` "Does NOT … constitute a trade signal — WQ-192's stand-down on new energy capital holds" |

Side note (out of cluster, Verified): `PROME/ROSTER.md:95` FALCON row still reads "DAEDALUS `L3` + live signal flow … provisional" while FLEET_MAP carries L4 H (scored 10/21) — a mirror of a DAEDALUS figure that has not followed it.

## E. Guard runs (all from repo root unless noted; FALCON tree `git status --porcelain -- AGENTS/FALCON/` = empty before every run, 17:38:47 → 17:44, and after)

| Cmd | rc | Key line | Both directions watched? |
|---|---:|---|---|
| `ledger_staleness.py FALCON` | 0 | FLOW ok +30d · FROZEN +4d · KB ok · VX ok · WARRISK **quiet +36d [EVENT-DRIVEN re-pull 2026-10-26]**; "6 scanned; 5 TSV(s) NOT scanned: CASUALTIES, STRIKES, VESSELS, corrections_receipts (+1)" | — |
| `… FALCON --trade` | 0 | "1 agent(s) matched NO trade surface and are NOT certified by this pass: FALCON" | — |
| `… FALCON --glob workbook/WARRISK.tsv --days 7` (FALCON boot 5a-2, `CLAUDE.md:50`) | 0 | `quiet +36d [EVENT-DRIVEN re-pull 2026-10-26]` | **Mutation on scratch copy** (`/tmp/claude-1000/falcon-r2/AGENTS/FALCX`): re-pull clock moved to 2026-10-01 (29d) → still `quiet`, rc0. Cadence line removed → `⚠️ UNATT +36d [attention 24d]`, rc1. **The 7-day gate cannot fire while the declaration stands, whatever the re-pull clock's age** |
| `… FALCON --abs-floor` / `--writes` | 0 / 0 | WARRISK quiet abs 36d / 10w | — |
| `… FALCON --nudge` | 1 | "VX.tsv (1 STATUS-write behind)"; WARRISK 10 writes / FLOW 3 writes behind "absence expected by declaration" | — |
| `… FALCON --strict` | 1 | SCHEMA.tsv ⚠️ STALE +110d (reference file, benign) | — |
| `AGENTS/FALCON/scripts/warrisk_row_staleness.py` (boot 5a-3) | **1** | "5 rows: 5 EXPIRED" — 🎯 WC Saudi +24d (As_Of 09-24), Hormuz +13d (10-06), Bab +88d (07-23), S. Red Sea +24d, spread +24d; "🔴 A REGISTERED FALSIFIER LEG IS EXPIRED" | **Yes.** Fire on real file; clean on scratch fixture (all Stale_By → 2026-12-31) → "0 EXPIRED, 5 current", rc0. Defect found: a row with fewer columns than `Role` is skipped silently (`if len(c) <= i_role: continue`) — fixture with Bab truncated printed "5 rows: 4 EXPIRED, 0 current, 0 undated" (counts do not conserve, no flag) |
| `falsification_scan.py --agent FALCON` (+`--tsv`) | 1 | EXIT_PROTOCOL STALE-FLAGGED 29d; CHANGELOG CURRENT. Note: `--help` is not handled — it runs the whole-fleet sweep (41 surfaces / 29 agents) | — |
| `claim_check.py --check weekday STATUS PREDICTIONS EXIT_PROTOCOL VX` | 0 | `✓ 4 file(s) clean` — but my regex finds **0** weekday-adjacent dates in those four files, so clean is vacuous | Fire watched on a scratch copy of STATUS + planted "Thursday 2026-10-30" → rc1 "is a Friday, not Thursday" |
| `corrections_boot_check.py FALCON` | 0 | "0 unreceipted NAMED rows … receipts on file: 13"; INFO COR-20260925-13 ALL-row past cap | — |
| `hormuz_transit_watch.py` (scratch copy, own state) | 2, then 0, 0 | run 1: "ArcGIS error after 6 attempts: 400 Invalid URL"; runs 2–3: "newest print 2026-10-25 = 2/88 … band DEEPENING (previous DEEPENING)" | **Yes.** Scratch state set to `last_band=MIXED` → "⚠️ BAND TRANSITION: MIXED → DEEPENING", rc1. rc2 message still says "the **7/5-vintage** fallback in FRESH_LEG_BASELINE.md row 2 stays canonical" (`hormuz_transit_watch.py:136-137`) — the fallback it names is 3½ months old; the last good print is in the state file (10/25) |
| `bypass_watch.py` (scratch) | **2** | "EMPTY SERIES for Sohar … DEGRADED (missing primary: Sohar); NO combined verdict"; Fujairah newest 10/23, trail-14d 77,581 t/d vs floor 25,951 HOLDING | **Monkeypatched-legs fixture:** HOLDING→rc0, COLLAPSE→rc1, Sohar-empty→rc2. All branches correct. But with Sohar dropped upstream the live gauge is **permanent rc2** — it can never again print HOLDING or COLLAPSED (CHECK_STANDARD §3(e): permanent-red). A real Fujairah collapse now prints "⚠️ BELOW FLOOR" on a per-port line under an rc the boot card reads as "fetch failure". Collapse text also says "(D toward 75)" — stale ladder (D is 85) |
| `kharg_loadings_watch.py` (scratch) | 2 | run 1: "400 Invalid query parameters"; run 2: "endpoint returned 0 rows — verify portid='port2164'"; committed state last_run 2026-09-16 | Gate retired 8/20 ("optional, not load-bearing", `CLAUDE.md` 5b triad line) — dead instrument still listed in the boot triad |
| `baghdad_watch.py` (scratch) | 0 | "QUIET — last embassy alert 2026-10-24 … BACKSTOP ONLY … SILENCE IS NOT EVIDENCE" | Fire branch not exercised (low value; demoted backstop) |

Real-tree state files were not touched: watchers ran from `/tmp/claude-1000/falcon-r2/run/scripts/` (copies), writing only the scratch state JSONs.

## F. VX band integrity (bands extracted `awk -F'\t'` cols 4–8, VX.tsv L3–L12)

| Row (VX.tsv line) | Status token | Band defect | Instrument state | V/I |
|---|---|---|---|---|
| IRAN-01 (:3) | RED | Green "Hormuz reopens to **>25/day** sustained"; Orange "Hormuz **<2/day**" — UKMTO-era tanker counts; that basis was retired at IRAN-02 10/14 ("UKMTO-tanker band text kept as labelled legacy") | **No instrument.** PortWatch total transits is the live series; its bands are <10/10–14/14–18/>18. Note: the live print **is** 2/88 on 10/25 — sitting exactly on the Orange "<2/day" boundary, so a reader applying the orphaned band to the live series gets a pseudo-signal. Deferred by FALCON to 11/04 (owner disposition) | V |
| **DIPLOMACY-01 (:7)** | YELLOW | Green "Hormuz reopen verified at **>25/day**" — the **same retired basis**, not named in Wiring 17 #8 nor in FALCON's 10/30 deferral. Yellow "Iran returns to mediation **by Jun 15**" (a dated band 4½ months past); Orange "(current **Jun 2-8**)"; Red "✅ **HOLDING**: Iran walked Jun 1; deal probability 12%" — band cells carry June state markers that contradict the YELLOW status | No instrument for the Green leg; Yellow/Orange/Red are spent June events | V |
| GULFSTATE-01 (:6) | RED | Orange band text ends "intercepts hold **(current)**" — contradicts RED | Qualitative; FIRMS + state statements | V |
| BABMANDAB-01 (:9) | RED | Yellow band "Iran rhetoric + Houthi quiet **(current)**" — contradicts RED. **Notes cell destroyed** — bare `2026-09-14` since `a8d259b44`, 695 B lost (text recoverable at `c4b8c83b9`) | GATE-FALCON-001 leg 2 = own TankerMap bars (live) | V |
| ISR-01 (:8) | ORANGE | Yellow band "(current **Apr 12-20** window)" — 6-month-old marker, contradicts ORANGE | Search-not-found dormancy check (10/29) | V |
| SUNK-01 (:11) | class-(ii) FIRED ×2 | Red band (iii-A) "trip (a) FIRES as registered" — D 75→85 is spent ("One move; cannot fire again", EXIT :51). Current_Value [Oct30] already reads a first (iii-A) as "EXIT §5 rewrite + memo, no mark move" — band text and current reading disagree | VESSELS.tsv (live 10/30), outside ledger_staleness glob | V |
| CASUALTY-01 (:12) | RED RATE-STEP | Red band cites "[= D→85 trigger (d), on/after 9/8]" — spent trigger (same as above); class-step itself still live under WQ-434. Rate-step is a rolling-30d statistic last computed 10/26 ("not recomputed", [Oct29]) | CASUALTIES.tsv (10/26), not scanned | V |
| IRAN-02 (:4) | RED | Clean: one named instrument (PortWatch via hormuz_transit_watch.py), legacy UKMTO text labelled "(retired)"; OWED note superseded in place [Oct30] — **FALCON's 10/30 claim verified** | Live; watched both directions (§E) | V |
| USIRAN-KINETIC-01 (:5) | RED | Clean; cites FAL-07, does not restate (HAW-10 discipline) | FAL-07 letter | V |
| GASLNG-01 (:10) | RED | Clean; qualitative FM bands, verified-date discipline (LESSONS 6) | Operator notices | V |

**Instrument-loss outside VX but on the rail:** EXIT §3 indicator #7 ("Fujairah+Sohar below the ROLLING floor … read the floor from a live `bypass_watch.py` run") — Sohar's series is gone upstream (script comment `bypass_watch.py` empty-series guard, 10/29: "Daily_Ports_Data holds 0 rows for it (whole history)"). The indicator's letter names two ports; one no longer exists in the source. EXIT :83 still reads "no newer print than October 16 … HOLDING 92,073 versus rolling floor 32,115" (stamped 10/26) while VX IRAN-02 [Oct30] and STATUS matrix read "bypass DEGRADED (Sohar empty)". V.

## G. Reconcile — prior profile (8/7 + 8/15 Δ), war-triad 8/15, 10/21 production review, 10/30 sweep replies

| Item (source) | Now | Receipt |
|---|---|---|
| Write-back tail: VX-FALCON-SUNK-01 absent (8/7 🔴) | **CLOSED** (8/10) | VX.tsv:11 |
| VESSELS.tsv outside ledger_staleness glob (8/15 Δ②) | **STILL OPEN** — plus CASUALTIES.tsv and STRIKES.tsv now in the same unscanned set; no `workbook/LEDGER_GLOB` | §E perimeter line |
| EXIT §5 past own clock (8/7 🟠) | **CLOSED** — §5 last 10/29, next 11/04 | EXIT :102 |
| EXIT §1 Status cells stale vs live (8/7 🟠) | **RECURRED** in v3: §1/§2/§3 headers "status 2026-10-01"; scanner STALE 29d | EXIT :24, :44, :73; §E |
| First-fatality claim live in rail/VX:6 (8/15 Δ③④) | **CLOSED** — v3 rewrite; CASUALTY-01 Notes carries the standing correction | VX.tsv:12 Notes |
| No `workbook/PUBLISHED.tsv` (8/7 "real debt") | **STILL ABSENT** | `ls` → no such file |
| Calibration-as-prose, no Brier (8/7 mild, revisit n≈8) | Unchanged at n=5 resolved; within its own trigger | §B |
| DO-NOT-TOUCH #2 rc-inverted bypass/kharg | Preserved in code; **kharg now dead** (0 rows / 400) | §E |
| DO-NOT-TOUCH #3 WARRISK `--days 7` "never widen to silence" | **REGRESSED** — `Cadence: EVENT-DRIVEN` (added `35bd7d149` 10/26) makes the gate permanently quiet | §E mutation test |
| DO-NOT-TOUCH #1 bypass floor never hardcoded | Holds (runtime 30% of 60d mean) | `bypass_watch.py:66` |
| DO-NOT-TOUCH #7 88/day provenance block | Present | `hormuz_transit_watch.py:45-58` |
| 10/21: FAL-06 dated-search rule (WQ-433) | **Encoded** verbatim in row | PREDICTIONS FAL-06 col 3 |
| 10/21: D 85→92 registered (WQ-355) | Encoded §2a, ARMED | EXIT :52-69 |
| 10/21: WQ-432 gate leg 2 provisional | Graded 10/29 NOT MET | STATUS:15; VX:9 |
| 10/21: "L5 on registered date grading" | FAL-06 grade due 11/05 (future); FAL-07 search date non-compliant, routed WQ-559 | §B |
| Sweep #5: EXIT §2 vs §5 dates | **DONE as claimed** — :42 now "last full review HELD 2026-10-29 (owed 10/28); next due 2026-11-04 — §5 governs" | EXIT :42 |
| Sweep #5: FAL-07 2027-01-02 | **Routed as claimed** — WQ-559 registered | `PROME/WILL_QUEUE.md:55` |
| Wiring 17 #8: IRAN-01 bands | Deferred to 11/04 (owner's call, threshold change) — **scope incomplete: DIPLOMACY-01 Green ">25/day" shares the retired basis** | §F |
| Wiring 17 #8: VX:4 OWED text | **DONE as claimed** — superseded in place | VX.tsv:4 [Oct30] |

## H. Ranked route list

| Rank | Sev | Finding (numbers) | Owner | Ask | V/I |
|---:|---|---|---|---|---|
| 1 | 🟠 | **WARRISK 7-day gate permanently quiet.** `Cadence: EVENT-DRIVEN` (added 10/26 `35bd7d149`) + `declared_quiet()` (`scripts/ledger_staleness.py:566-568`) returns quiet for ANY parseable re-pull date: data clock 36d, re-pull clock moved to 29d on a scratch copy → still `quiet` rc0; line removed → `⚠️ UNATT` rc1. SCHEDULED ages its date against now (:561); EVENT-DRIVEN does not age its re-pull clock at all. Docstring :44 still says "The declaration affects --nudge ONLY: the --days/--writes/--abs-floor scans still grade the file" — contradicted by M1 (WQ-147, `b5494ecac`). Residual protection exists: FALCON's per-row guard (5a-3) fires rc1 with the 🎯 falsifier +24d | **DAEDALUS** (shared script) · FALCON informed | Age the EVENT-DRIVEN re-pull clock against `--days` (quiet only while attempt age ≤ days; fail closed), fix docstring :44; re-run FALCON 5a-2 both ways after. Fleet-wide: same path silences OSPREY-class EVENT-DRIVEN ledgers — run `--all` before/after diff | V |
| 2 | 🟠 | **VX BABMANDAB-01 Notes cell overwritten** with bare `2026-09-14` by `a8d259b44` (9/14 gate review); 695 B of HAW-10 wording-wedge history lost; Last_Updated stayed 09-08 in that commit (wrong-column write). Undetected 46 days across ≥6 FALCON VX commits | FALCON | Restore the 695 B from `c4b8c83b9:AGENTS/FALCON/workbook/VX.tsv` and append the intended 9/14 entry; note the repair in the row | V |
| 3 | 🟠 | **EXIT §3 indicator #7 has lost an instrument leg.** Sohar series dropped upstream (0 rows, whole history; script comment 10/29) → `bypass_watch.py` permanent rc2 "NO combined verdict"; indicator letter needs Fujairah+Sohar. A real Fujairah collapse now surfaces only as a per-port "⚠️ BELOW FLOOR" under rc2 (= "fetch failure" on the boot card). EXIT :83 (stamped 10/26) still shows the 10/16 two-port HOLDING 92,073 vs 32,115 while VX:4 and STATUS read DEGRADED | FALCON → PROME → Will (indicator letter) | Propose a re-basis (Fujairah-only floor, or a second source for Sohar) at the 11/04 review; meanwhile mark #7 CANNOT-FIRE-AS-LETTERED on EXIT :83 and make DEGRADED with a primary BELOW FLOOR exit 1, not 2 | V |
| 4 | 🟠 | **FAL-07 headline adjective decided in a grade note.** Row text "OFFENSIVE kinetic strike"; KB-FALCON-372 (10/30) rules a "defensive manner" launcher strike WOULD count. Same note: Reuters/AP/Bloomberg/AFP "unreachable to this box's search" — the confirmation two-wire limb and the FAILED dated search both name sources this box cannot search | FALCON → PROME (bundle with WQ-559 for Will) | Put the OFFENSIVE-vs-self-defence reading and the wire-reachability limit on the same Will packet as the WQ-559 date fix, before a confirmation lands | V (text) / I (severity) |
| 5 | 🟡 | **Band rows with no instrument or spent/stale state:** IRAN-01 Green >25/day + Orange <2/day (retired UKMTO basis; live PortWatch print 2/88 sits on the Orange boundary); **DIPLOMACY-01 Green >25/day (same basis, not in the 11/04 deferral)** + Yellow "by Jun 15" + Orange "(current Jun 2-8)" + Red "✅ HOLDING… 12%"; GULFSTATE Orange "(current)" vs RED; BABMANDAB Yellow "(current)" vs RED; ISR-01 Yellow "(current Apr 12-20)" vs ORANGE; SUNK-01/CASUALTY-01 Red bands cite the spent D→85 trigger | FALCON | Widen the 11/04 band proposal from IRAN-01 to IRAN-01 + DIPLOMACY-01; strip "(current …)" markers from band cells (a status lives in Status) | V |
| 6 | 🟡 | EXIT §1/§2/§3 tables headed "status 2026-10-01" (29d; scanner STALE-FLAGGED); kill evidence cites PortWatch 1/88 9/27, Brent $100.83 10/01, war-risk 6–9% 9/25 | FALCON | Re-stamp the kill and indicator cells at the 11/04 review (verdicts unchanged on what I saw) | V |
| 7 | 🟡 | Instrument TSVs behind SUNK-01 / CASUALTY-01 / §2a (VESSELS, CASUALTIES, STRIKES) are outside `ledger_staleness`; no `workbook/LEDGER_GLOB`. Open since 8/15 (76 d) | FALCON | Add `AGENTS/FALCON/workbook/LEDGER_GLOB` (`workbook/*.tsv domain/*/*.tsv`) — own-dir change | V |
| 8 | 🟡 | FLOW.tsv: FLOW-FALCON-05 added 10/29 under `Last real data refresh: 2026-10-01`; conservation line still "16" (now 17); file sits at +30d, so the default gate trips on the next STATUS write | FALCON | Advance the data clock for the 10/29 row (or say why not); update the count line | V |
| 9 | 🟡 | CASUALTY-01 RED rate-step 24 vs 7 last computed 10/26 on a rolling-30d window; "not recomputed" 10/29 | FALCON | Recompute at each grade, or date the figure as a 10/26 value | V |
| 10 | 🟡 | KB.tsv: 179 ACTIVE rows past own Stale_By (61 >30d); 4 Status values off the SCHEMA enum (KB-092/094/095/166) | FALCON | Status sweep at a quiet session; map the 4 to enum + Notes | V |
| 11 | 🟡 | `warrisk_row_staleness.py`: short row skipped silently (fixture: "5 rows: 4 EXPIRED, 0 current, 0 undated") | FALCON | Count short rows as malformed → rc2 | V |
| 12 | 🟡 | Stale alert text: `hormuz_transit_watch.py:136-137` rc2 names a "7/5-vintage fallback"; `bypass_watch.py` collapse line "(D toward 75)" | FALCON | Point rc2 at the state file's last good print; drop the 75 reference | V |
| 13 | 🟡 | `kharg_loadings_watch.py` dead (400 / 0 rows; last state 9/16) yet still in the boot 5b triad | FALCON | Banner FROZEN in script + boot card, or retire from the triad | V |
| 14 | 🟡 | `falsification_scan.py --help` runs the full fleet sweep (no argparse) | DAEDALUS | Add a `--help` guard | V |
| 15 | 🟡 | `PROME/ROSTER.md:95` FALCON "DAEDALUS `L3` … provisional" vs FLEET_MAP L4 H (10/21) | PROME | Refresh the mirror text, or cite FLEET_MAP instead | V |
| 16 | ⚪ | No `workbook/PUBLISHED.tsv` (8/7 "real debt") still absent | FALCON / DAEDALUS blueprint | Decide waive-or-build at the next blueprint pass | V |

Positives (for the profile, Verified): FAL-06 dated-search letter is the cleanest WQ-433 encoding I have seen; scoreboard reconciles to the Status cells; interim grades append without editing rows; IRAN-02 is a model single-instrument band row; bypass_watch's empty-series guard (10/29) fails toward "unknown", not "collapse"; FALCON's two 10/30 sweep claims (EXIT :42, VX:4) verified as stated; WQ-559 routed same day.

## I. Coverage

| Path | Read | Range / method |
|---|---|---|
| `workbook/VX.tsv` | whole by column | NF per line (12 lines); cols 1–2,4–10 whole; col 3 first 900 chars per row; col 11 first 300 chars (+ BABMANDAB whole); git history of BABMANDAB col 11 across 20 commits |
| `workbook/EXIT_PROTOCOL.md` | whole | lines 1–111 (Read) |
| `workbook/KB.tsv` | column extracts | header + lines 1–8 (400 chars); cols 1,2,9,10 all 376 rows; KB-372 cols 5,13 |
| `workbook/WARRISK.tsv` | header + rows | lines 1–34, 420 chars/line for 1–28; data rows cols 1–12 |
| `workbook/FLOW.tsv`, `FLOW_HAWK_MIGRATED_FROZEN.tsv`, `SCHEMA.tsv` | headers + IDs | FLOW all lines (col 1,2,4); FROZEN head; SCHEMA whole |
| `thesis/PREDICTIONS.tsv` | whole | lines 1–30 (700 chars); 31–38 all columns; FAL-06/07 cols 3,9,10 whole; archive snapshot FAL-01..05 cols 1,6,7 |
| `registry/corrections_receipts.tsv` | whole (260 chars/line) | 14 lines |
| `scripts/` 5 .py + 4 JSON | warrisk_row_staleness 40–162 whole; bypass_watch 60–204 whole; others grep-surveyed for writes/rc; all 4 JSON whole (baghdad head 400 B) | |
| `board_log.tsv` | shape + tail | NF all 286 rows; disposition counts; last 6 rows |
| STATUS.md | 1–8, 45–64, grep | not whole (R1/R3 scope) |
| Not read | THESIS.md body, TIMELINE, domain/*.md bodies (stamps only), PREDICTIONS_ARCHIVE.md, reports/ | out of cluster |

**Tree check at end:** see final line.
**FALCON tree at end:** `git status --porcelain -- AGENTS/FALCON/` = empty (clean) at 2026-10-30 17:48:14 EDT. Scratch artifacts: /tmp/claude-1000/falcon-r2/ (copies only).
