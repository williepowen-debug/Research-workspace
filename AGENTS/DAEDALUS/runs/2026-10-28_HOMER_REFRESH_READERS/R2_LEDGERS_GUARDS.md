# HOMER refresh — Reader 2 of 3: LEDGERS · FALSIFICATION · GUARDS

**Run:** 2026-10-28 ~21:00–21:20 EDT · DAEDALUS Mode-A helper (not owner) · HOMER not in a live session (last HOMER-authored commit `454435973` 2026-10-19 13:24, "close desk session at Will request"; every HOMER-path commit since is WALTER signal delivery, `git log -- AGENTS/HOMER`).
**Write perimeter honoured:** this file + fixtures under `/tmp/claude-1000/homer_guard_copy/` only. `git status --porcelain -- AGENTS/HOMER` = 0 lines after every tool run.
**Cluster file list (bytes):** thesis/ PREDICTIONS.tsv 36,472 · THESIS.md 23,077 — workbook/ BUILDER 58,735 · KB 30,499 · KB_LIVE 71,786 · MULTIFAMILY 89,022 · PIPELINE 61,902 · PRICING 97,910 · RATES 53,951 · RENT_BREADTH_ROSTER 3,650 · SCHEMA 5,320 · STATE_HSG 42,491 · rent_breadth_inputs/Apartment_List_2026_09_roster100.csv 67,539 · rent_breadth_inputs/README.md 701 — registry/corrections_receipts.tsv 1,827 — docket/CATALYSTS.tsv 120,296 — state_vectors/ SV-06-08-02 2,071 · SV-06-08-03 11,406 · SV-07-10-01 4,797 · SV-07-10-02 4,123 · corrected/SV-06-08-01 7,149 — tools/rent_breadth.py 5,993.

---

## 1. Ledger register

`tsv_append.py --check` rc read bare (not through a pipe). "Consumers" = basename grep hits in `AGENTS/HOMER/CLAUDE.md` / `STATUS.md` / `NEXUS_BRIEF.md`; script hits are fleet tools that read by glob or pattern, not HOMER-specific consumers.

| Ledger | Bytes | Header state | `Last real data refresh` | Data rows | tsv_append --check | `Next:` dates passed as of 10/28 | Consumers (CLAUDE / STATUS / NEXUS_BRIEF) |
|---|---:|---|---|---:|---|---|---|
| workbook/BUILDER.tsv | 58,735 | LIVE two-clock, line 1 | 2026-10-19 (line 1 also carries a PRIOR HEADER VERBATIM 2026-10-15 clock) | 99 | rc 0, 8 cols | PHM 10/22 passed | 2 / 1 / 0 |
| workbook/KB.tsv | 30,499 | **FROZEN** 2026-07-10 banner (:1) | — | 65 | **rc 1: 3 rows with 10 cols vs 12-col header** (lines 14, 26, 27; trailing Stale_By/Notes missing) | n/a | 3 / 0 / 0 |
| workbook/KB_LIVE.tsv | 71,786 | LIVE two-clock, line 1 (prior headers moved to line 2) | 2026-10-19 | 38 | rc 0, 11 cols | none dated | 3 / 1 / 0 |
| workbook/MULTIFAMILY.tsv | 89,022 | LIVE two-clock, line 1 (+ prior verbatim on same line) | 2026-10-19 | 78 | rc 0, 9 cols | GSE Sept ~10/23–30 (window closing) | 2 / 1 / 4 |
| workbook/PIPELINE.tsv | 61,902 | LIVE two-clock, line 1 (+ prior verbatim) | 2026-10-19 | 80 | rc 0, 10 cols | ICE First Look "lateOct" (window closing); PFSI 10/29 | 2 / 1 / 1 |
| workbook/PRICING.tsv | 97,910 | LIVE two-clock, line 1 (+ prior verbatim) | 2026-10-19 | 64 | rc 0, 8 cols | Redfin ~10/22, Census/NAR 10/20, NHS 10/27 passed | 2 / 0 / 3 |
| workbook/RATES.tsv | 53,951 | LIVE two-clock, line 1 (+ prior verbatim) | 2026-10-19 | 41 | rc 0, 8 cols | MBA 10/21, PMMS 10/22 passed | 2 / 0 / 1 |
| workbook/STATE_HSG.tsv | 42,491 | LIVE two-clock, line 1 (+ prior verbatim) | 2026-10-19 | 74 | rc 0, 10 cols | none passed | 2 / 0 / 0 |
| workbook/RENT_BREADTH_ROSTER.tsv | 3,650 | **FROZEN** 2026-09-29 (membership fixed by Will ruling; :1) | — | 100 | rc 0, 4 cols | n/a | 1 / 0 / 0; read by `tools/rent_breadth.py:27` |
| workbook/SCHEMA.tsv | 5,320 | neither (no header comment; a schema, exempt by name in ledger_staleness) | — | 76 | rc 0, 4 cols | n/a | 1 / 0 / 0 |
| thesis/PREDICTIONS.tsv | 36,472 | neither banner nor two-clock; line 1 is the load-bearing prose preamble (DO-NOT-TOUCH) | — | 2 | rc 0, 11 cols | none (HOM-02 Resolve_By 2027-02-28) | 6 / 1 / 0 |
| docket/CATALYSTS.tsv | 120,296 | neither (docket; boot step 5 prints it by awk) | — | 45 | rc 0, 7 cols | ~10 rows' NEXT dates passed (see §8 item 2) | 5 / 1 / 1 |
| registry/corrections_receipts.tsv | 1,827 | neither (append-only receipts) | — | 7 | rc 0, 4 cols | n/a | 1 / 0 / 0; read by `scripts/corrections_boot_check.py` |
| *(aside, outside cluster)* board_log.tsv | 70,745 | neither | — | 96 | **rc 1: 3 rows with 4 cols vs 5-col header** (lines 65–67, dated 2026-10-02; timestamp column missing, signal_id shifted into col 1) | — | — |

**SCHEMA coverage now:** BUILDER 8 · KB 12 · KB_LIVE 11 · MULTIFAMILY 9 · PIPELINE 10 · PRICING 8 · RATES 8 · STATE_HSG 10 (`cut -f1 workbook/SCHEMA.tsv | sort | uniq -c`). Every LIVE ledger is covered. Not covered: RENT_BREADTH_ROSTER (FROZEN), PREDICTIONS, CATALYSTS, corrections_receipts.

**ledger_staleness results (all read-only):**

| Invocation | rc | Result |
|---|---:|---|
| `ledger_staleness.py HOMER` | 0 | 7 LIVE `ok` (+1 to +5d behind STATUS) · 2 FROZEN. **6 of 7 LIVE ledgers report `⚠️ 2 data clocks (2026-10-15 / 2026-10-19), oldest governs`.** Perimeter: CATALYSTS, corrections_receipts, PREDICTIONS not scanned |
| `HOMER --quiet` (the charter boot form, CLAUDE.md:199) | 0 | prints only the perimeter line, i.e. reads all green |
| `HOMER --writes` | 0 | all `ok`; 1–3 STATUS writes behind |
| `HOMER --abs-floor --abs-days 7` | 1 | 7 STALE at abs 10–14d (shows the default run's blind spot: the desk is uniformly idle, so the STATUS-relative clock reads green) |
| `HOMER --trade` | 0 | "1 agent(s) matched NO trade surface and are NOT certified by this pass: HOMER" |
| `--glob thesis/*.tsv` / `--glob docket/*.tsv` | 0 / 0 | PREDICTIONS +20d `ok`; CATALYSTS +0d `ok` |
| `--selftest` | 0 | `✓ 40/40 cases behaved` |

**Why two clocks:** BUILDER/MULTIFAMILY/PIPELINE/PRICING/RATES/STATE_HSG put `PRIOR HEADER VERBATIM: # LIVE — Last real data refresh: 2026-10-15 …` on the same line 1 as the current clock (e.g. RATES.tsv:1). The tool reads both and lets the older one govern, so it under-reports freshness by 4 days. KB_LIVE moves prior headers to line 2 (KB_LIVE.tsv:2) and reads as one clock. The error is in the safe direction (it reports more staleness, not less), but the tool reports a vintage the desk did not intend.

---

## 2. Invalidation-surface inventory (one row per instrument)

"Mech?" = a mechanical check reads the surface. **Direct answer: a DATED thesis-level kill rail EXISTS now.** It is `thesis/THESIS.md`, title "THESIS + THESIS-LEVEL KILL RAIL" (:1). It reads "Kill rail re-derived: 2026-09-29 … Criteria FROZEN from this commit · Next formal grade: 2026-11-20" (:3). §4 is "PRE-REGISTERED 2026-09-29, before any grade under it" (:74), and the rail is registered as `GATE-HOMER-THESIS-KILL` (PROME/GATES.tsv:21). **Date correction:** the rail dates from **2026-09-29**, not 10/15. The 10/15 items are the §7 clarifications (:127), the §8 convergence handle (:141) and the first §9 fired-count entry (:177).

| # | Instrument | path:line | In-content dated stamp | Status 10/28 | Mech? |
|---|---|---|---|---|---|
| 1 | Thesis decision rule (both cores killed ⇒ FALSIFIED; one core ⇒ PARTIAL; ≥2 amplifiers ⇒ intensity note) | THESIS.md:74–89 | "PRE-REGISTERED 2026-09-29"; formal grades 2026-11-20, 2027-02-20 (:89) | LIVE, 0/5 legs fired (:106, :188, :202) | **Partly.** The boot awk prints docket row 37 (CATALYSTS.tsv:37), and GATES:21 has review_by 2026-11-20 (JUDGEMENT class, "no producer", GATES:21 col 10). **`falsification_scan.py` does NOT read it** (see §6) |
| 2 | C1 residential conversion kill (ICE FC sales YoY ≤0% AND FC inventory COUNT YoY ≤0%, 3 prints) | THESIS.md:37–42; V4 count-not-rate :136 | 2026-09-29 | LIVE 0/3. **Sept First Look (~10/22–28) not integrated**; HOMER idle since 10/19 | docket row CATALYSTS.tsv:11 (boot awk) |
| 3 | C2 CMBS kill (Trepp MF DQ <6.00%, 3 prints) | THESIS.md:45 | 2026-09-29 | LIVE 0/3; Sept 8.04% integrated 10/15 (:182); Oct due ~11/02 | CATALYSTS.tsv:25 |
| 4 | C2 GSE kill (max(Freddie, Fannie serious) <0.50%, 3 prints) + Fannie-provision HALF rule | THESIS.md:46–48; V3 :135 | 2026-09-29 / 10-15 | LIVE 0/3; Sept prints ~10/23–30 not integrated | CATALYSTS.tsv:20 |
| 5 | A1 FHA-bottom kill (FHA SA QoQ ↓ ×2 AND ICE cure YoY better than −15%) | THESIS.md:53–57 | 2026-09-29 | LIVE, half of the first conjunct (:102, :184); decider is Q3 NDS mid-Nov | CATALYSTS.tsv:26, :27 |
| 6 | A2 rate kill (PMMS ≤6.50%, 4 weeks) | THESIS.md:60–63 | 2026-09-29 | LIVE 0/4. **PMMS 10/22 7.32% sits unlogged** in `inbox/WALTER/SIG-W-20261022-029.md`, so the §9 ledger was not updated (count unchanged either way) | CATALYSTS.tsv:5 |
| 7 | A3 builder kill (NAHB HMI ≥40, 3 prints) | THESIS.md:66–70 | 2026-09-29 | LIVE 0/3; Oct HMI 29 graded 10/19 (:200) | CATALYSTS.tsv:21 |
| 8 | Between-grade clarifications V1–V5 (resolving vintage, UNGRADED pauses, provision QoQ, count-vs-rate, "11/20 cannot return FALSIFIED/PARTIAL on cores") | THESIS.md:127–137 | 2026-10-15 | LIVE (definitions only, "no level moved") | no |
| 9 | Defect register D1–D8 | THESIS.md:112–123 | 2026-09-29 / 2026-10-15 | LIVE; D2/D3/D4 base-window pulls still owed (no closure row) | no |
| 10 | HOM-01 FMHPI rollover, early-kill arm (both Jun and Jul prints > +1.9% SA) | PREDICTIONS.tsv:3 (Invalidation, Status, Outcome) | registered 2026-07-12; rulings 2026-08-22; Resolve_By 2026-09-30 | **FIRED: RESOLVED MISSED (EARLY-KILL) 2026-08-31** (Jul +2.31% SA). IF-MISSED clause executed to LESSONS 8/31 | consumer_check / asmade_audit read PREDICTIONS.tsv fleet-wide |
| 11 | HOM-02 FHA SA DQ ≥12.00%; early-kill = QoQ decline in both Q2 and Q3 | PREDICTIONS.tsv:4 | registered 2026-07-24; Resolve_By 2027-02-28 HARD | **LIVE.** Arm 1 of 2 FIRED 2026-08-13 (11.79%, −9bp); modal decider Q3 NDS ~mid-Nov | CATALYSTS.tsv:26 |
| 12 | 7/24 HOM-01 grading sheet (frozen pre-print card) | reports/2026-07-24_HOM-01-grading-sheet.md (exists; outside cluster, not re-read) | 2026-07-24 | spent, closed with HOM-01 | no |
| 13 | PMMS 10/01 pre-registration card (HOLD ≥7.05 / SOFTEN / LIFT) | reports/2026-09-29_PMMS-2026-10-01_PRE-REGISTRATION.md:9–11 | 2026-09-29 | **FIRED: HOLD** (7.28%: board_log.tsv:65, THESIS.md:154). The card carries no grade, which is consistent with the never-edit-post-print practice | no |
| 14 | Dated kill: Trepp MF maturity-adjusted rate (re-spec the leg if absent a 3rd month) | CATALYSTS.tsv:9; MULTIFAMILY.tsv:74 | pre-committed 2026-08-22 | **FIRED / EXECUTED 2026-10-15**; successor is MF special servicing (MULTIFAMILY.tsv:73) | docket (RESOLVED, filtered out of boot awk) |
| 15 | Dated kill: $160B+ MF maturity wall | MULTIFAMILY.tsv:17 | "RETIRED 2026-09-02" | **FIRED / EXECUTED** 2 days early (PROME DOCKET:224 owned the row) | no |
| 16 | Servicer-watch class rail A–G (+Z), any one class ⇒ 🔴 | CATALYSTS.tsv:3 (row 39 KB; only ~3K read) | ratified 2026-08-13, amended 8/14, encoded 8/22 | **FIRED: Class A 2026-08-07** (Fitch UWM BB- → B+), found 2026-09-29; "LAST FULL SWEEP: 2026-09-29 — re-run at each quarter's 10-Q window (~early Nov)" | docket boot awk |
| 17 | Non-funding leverage rider (no-verdict precursor, cannot fire by construction) | CATALYSTS.tsv:18; KB-HOMER-032 | encoded 2026-09-29 | FROZEN-by-design (never scored) | no |
| 18 | Rent-decline breadth band >20/>40/>55% (Apartment List, 100 frozen cities) | MULTIFAMILY.tsv:68; RENT_BREADTH_ROSTER.tsv:1; CATALYSTS.tsv:42 | re-armed 2026-09-29 (Will) | LIVE ORANGE 46/100 (Sep); **Oct file due ~10/27–31 not run** | **YES**: `tools/rent_breadth.py` (verified both ways, §6) |
| 19 | National FC STARTS band >100K/130K/175K | PIPELINE.tsv:77; CATALYSTS.tsv:10 | re-armed 2026-09-29 (Will) | LIVE below Yellow (Q2 81,935 derived); Q3 ATTOM access UNRESOLVED (CATALYSTS.tsv:2, :38) | no |
| 20 | Charter Key-Thresholds rail (all bands) | CLAUDE.md:~76–121 (outside cluster; :110–119 seen) | inline RE-ARMED stamps 2026-09-29 | not re-verified by this reader (Reader 1 cluster) | partly (docket band rows) |

---

## 3. Convergence handle

| Item | Value | Cite |
|---|---|---|
| Built | "Convergence handle (L3 build 3c) — BUILT 2026-10-15" | THESIS.md:141; :6 ("6 days past its 10/09 due date") |
| Composite | "**4 + 4 + 4 + 4 + 3 = 19/25 across 5 legs.** Independent roots: **3** (R1, R2, R3). A1 folds into R1; A2 is an input to CARL's V12, not a new root." | THESIS.md:157 |
| Scores' vintage | "Scores are the ones PROPOSED 2026-09-29 … Not re-scored on 10/15 … Re-score at each formal grade (next 2026-11-20)." | THESIS.md:147 |
| Independence rule | A1 "Co-rooted with C1 (R1): count once"; A2 "Co-rooted with CARL's V12 … count once" (:153–154). Double-count guard: "one HOMER fact feeds one CARL vector. A fact that bears on two vectors (A1 → V10 and V8) is counted at V10; V8 is CARL's own reading of it." | THESIS.md:153–154, :171 |
| CARL join | C1+A1 → V10 CONFIRMED · A2 → V12 CONFIRMED · C2 → V3 "NOT re-scoped … peer evidence only … ⛔ Never map C2's state onto V3's score" · A3 → R3 CANDIDATE | THESIS.md:163–169 |
| Pending upgrade | "C2's upgrade trigger (→ 5) is **MET** by the Trepp 8.04% print. **Not re-scored today** … Composite stays **19/25** until then." | THESIS.md:190 |
| Open defect in the handle | A2 has no upgrade rung: "None defined: PMMS has no uncrossed rung above RED. Set one at the 11/20 grade or leave the score capped at 4" | THESIS.md:154 |

FLEET_MAP's "19/25, 3 independent roots" is **CONFIRMED** at the file.

---

## 4. Predictions

| ID | Date_Made | Resolve_By | Confidence | Status (verbatim head) | Date_Resolved |
|---|---|---|---|---|---|
| HOM-01 | 2026-07-12 | "2026-09-30 — HARD" | 60% (PROVISIONAL — mechanism EMPIRICAL, magnitude/timing ESTIMATE) | "RESOLVED MISSED (EARLY-KILL) 2026-08-31 — arm 2 fired on the July-data release (+2.31% SA > +1.9%)" | 2026-08-31 |
| HOM-02 | 2026-07-24 | "2027-02-28 — HARD" | 65% (PROVISIONAL - persistence trajectory EMPIRICAL, counter-mechanism live) | "OPEN — RESOLVER 1 OF 3 GRADED 2026-08-13: CONFIRM LEG NOT MET (11.79%, 21bps short); EARLY-KILL ARM 1 OF 2 FIRED … MODAL DECIDER: the Q3-2026 NDS release, ~mid-Nov 2026." | (empty, by design) |

- The FLEET_MAP claims are CONFIRMED: HOM-01 MISSED by early-kill, HOM-02 live. The ledger has only 2 rows, and **no new HOM-xx has been registered since 2026-07-24** (95 days).
- **The November 20 frozen scoring cadence is NOT in the PREDICTIONS ledger or in CLAUDE.md** (grep for "11/20 | 11-20 | November 20 | Nov 20" finds no hit in either file). The PREDICTIONS ledger names only "~mid-Nov 2026" as HOM-02's decider (PREDICTIONS.tsv:4). The cadence is stated at:
  - THESIS.md:3: "Criteria FROZEN from this commit · Next formal grade: **2026-11-20** … If any leg reaches its kill count before 11/20, re-date by packet to PROME."
  - THESIS.md:89: "**Formal grade dates: 2026-11-20** (after MBA Q3 NDS, ICE October First Look, Trepp November), then **2027-02-20**. Earlier only if any leg reaches its kill count."
  - THESIS.md:86: "⛔ **No criterion may be reworded, split or merged at grading time.**"
  - CATALYSTS.tsv:37 (row key "2026-11-20 — FORMAL GRADE … then 2027-02-20"; "⛔ No criterion reworded at grade time")
  - PROME/GATES.tsv:21 col 12
  - STATUS.md:140
- This is correct by design. The 11/20 cadence belongs to the thesis rail, not to the per-prediction ledger (THESIS.md:5: "A HOM-02 resolution is evidence for leg A1 below, not a thesis grade"). CLAUDE.md:245 says THESIS.md is "Not boot-read — its formal grade has a docket row".

---

## 5. TRADE surface (reading A)

| Leg | Finding | Evidence |
|---|---|---|
| TRADE surface | **None.** No TRADE.md or position file anywhere in AGENTS/HOMER | `find -iname '*trade*' -o -iname '*position*'` → 0 hits; `ledger_staleness --trade` → "matched NO trade surface" |
| Declared flat with a re-arm condition | **No.** No re-arm condition exists for a trade rail | — |
| No book by charter | **IMPLICIT, not chartered.** CLAUDE.md has no "book", "TERRY" or "trade" clause (grep). The only explicit statement is PROME's gate row: "Moves no capital; no position rides on HOMER's state." Charter edges are peer feeds only: "HOMER → CARL … → REGINALD … → HENRY" (CLAUDE.md:11) | PROME/GATES.tsv:21 col 5; CATALYSTS.tsv:18 ("TERRY (if it ever reaches a trade rail)") |
| Signals reach a consumer (last 45 days, since 9/13) | **DEMONSTRATED for CARL, partly for REGINALD, NONE for TERRY or HENRY.** HOMER-authored packets: `CARL/inbox/processed/2026-09-29_from-HOMER_3c-convergence-handle…` · `REGINALD/inbox/processed/2026-09-24_from-HOMER_GSE-MF-both-books-rising…` · `REGINALD/inbox/processed/2026-09-29_from-HOMER_servicer-watch-class-A-FIRED…`. TERRY: 0. HENRY: 0. Receiver-side citations: `CARL/STATUS.md` (commit 2026-10-28) :32, :36, :39 ("HOMER owns assets, builders, mortgage rates…"), :82; REGINALD/STATUS_DASHBOARD.md:33–34, :48 (commit 2026-10-11; cites HOMER's 8/22 packet, but carries the **stale** Apr Trepp 7.71% where the current figure is 8.04%); NEXUS reads NEXUS_BRIEF.md whole (read_cap owner notice "← read whole by NEXUS:6") | `find … -newermt 2026-09-13`; git log on inboxes |
| Idle-cost tell | CARL:41 sourced PMMS 10/22 7.32% **from FRED itself** ("HOMER owns housing grading"). CARL:37 marks FL foreclosures "[STALE — August vintage, checked 2026-10-28] … HOMER owns the read and its ATTOM access is unresolved". The consumer is waiting on HOMER | CARL/STATUS.md:37, :41 |

**Reading-A verdict for the scorer:** reading A's third disjunct can only pass if "no book by charter" accepts a PROME gate-row statement in place of a charter clause. Its consumer leg is evidenced for CARL. **A one-line charter clause would make it clean** (owner/Will lane). This reader makes no grade call.

---

## 6. Guards in both directions

| Guard | Docstring purpose | Clean/report run (rc + tail) | Capable case (alert) | Clean case | What the PASS proves |
|---|---|---|---|---|---|
| `tools/rent_breadth.py` (read-only; prints only, no writes) | Rent-decline breadth band over the frozen 100-city roster; UNGRADED on incomplete pairs; integer compare; pairs by calendar date (:1–21) | rc 0 on the real Sep extract: `LATEST 2026-09: 46/100 = ORANGE; next rung >55% needs 10 more cities`; sha256 printed; "months ABSENT from file: none". **Reproduces docket row 42 and README to the figure** | **(c) Real known defect, reproduced:** CATO's case "Delete column 2025_09 … incorrectly 54/100 Orange" (AGENTS/CATO/runs/2026-09-29_1112_homer-band-review.md:81). On the copy, `drop2509.csv` gives `LATEST 2026-09: 0/0 = UNGRADED (no column for 2025-09)` with months ABSENT `['2025-09']`, so the defect is fixed. Synthetic `red.csv` (60 cities negative) gives `60/100 = RED`. `blank1.csv` gives `46/99 = UNGRADED (incomplete pairs)`. `edge55.csv` gives `55/100 = ORANGE` (strict >55 holds). `--prior-file` flags the 1 changed month | `clean.csv` gives `0/100 = BELOW-YELLOW; next rung >20% needs 21 more cities`. Shuffled columns give output IDENTICAL to base (`diff` empty, all 105 months). `--prior-file` self-compare gives `0 changed` | It proves 4 things: date-pairing (not positional), the incomplete-pair refusal, the strict-inequality band edge, and revision reporting. **It does not prove:** (i) **rc is 0 in every state (RED, UNGRADED, BELOW-YELLOW alike)**, so the exit code cannot disagree with clean (CHECK_STANDARD §9) and the verdict is text-only; (ii) **no shipped selftest or named production acceptance set** in the docstring (§3(e)); the regression evidence lives in CATO's run dir and docket prose (CATALYSTS.tsv:42); (iii) roster integrity is only `assert len==100` (:108), with no sha check of the roster itself |
| `scripts/ledger_staleness.py HOMER --quiet` (CLAUDE.md:199) | Two-state ledger staleness | rc 0; perimeter line only | `--abs-floor --abs-days 7` gives 7 STALE at rc 1 (same files) | default gives all `ok` | Its own `--selftest` shows 40/40. **For HOMER, the PASS proves ledger-vs-STATUS coherence only.** It cannot see a uniformly idle desk (9 days idle, ~10 passed `Next:` dates, still green). It misreads 6 headers as two clocks (§1) |
| `scripts/corrections_boot_check.py HOMER` (CLAUDE.md:200) | R1 corrections receipts | rc 0: "0 unreceipted NAMED rows for HOMER … receipts on file: 7" | SAM gives rc 1 BLOCK (real). Typo `HOMERX` gives rc 2 CANNOT-EVALUATE | HOMER rc 0 (real) | Real two-direction behaviour observed. Aside for DAEDALUS (scripts owner): the docstring's named clean acceptance case `HAWK` now returns **rc 1** (COR-20261025-26), so the acceptance set has drifted, as the docstring itself warns ("Time-bound … re-pick") |
| Byte-tier one-liner (CLAUDE.md:216) | STATUS soft/hard | `STATUS 22,157B OK` | not exercised (no fixture; this reader would not mutate STATUS) | OK | 22,157 B < 22,785 B soft line |
| `scripts/read_cap_check.py --agent HOMER` (CLAUDE.md:217) | Boot read-cap | rc 0. LESSONS 23,910 B = 73% ("70–75% BAND"), STATUS 68%, SCRATCH 12%; NEXUS_BRIEF 41% (owner notice). **"this desk has no declaration in PROME/registry/READS.tsv"**; charter 38,671 B "OUT OF PERIMETER by rule 20 unless declared" | — | — | Clean only within the charter-heuristic perimeter. If the charter is explicitly read whole at boot (root rule: "Load … the desk's own instructions explicitly"), it is **119% of budget** and unassessed |
| Boot docket awk (CLAUDE.md:195, :225) | Print unresolved docket rows | 40 rows printed; 5 RESOLVED filtered (lines 9, 10, 17, 18, 19) | — | — | Lists rows; it does not judge due-ness |
| Inbox membership loop (CLAUDE.md boot step 9) | WALTER packets not in board_log | **29 of 29 `inbox/WALTER/*.md` UNLOGGED** (SIG-W-20261020-001 … 20261027-071) | — | — | Works as designed; it shows the backlog the idle desk owes |
| `AGENTS/DAEDALUS/scripts/falsification_scan.py --agent HOMER` (fleet sweep #3; DAEDALUS-owned) | Freshness of falsification surfaces | **rc 1: "Searched: 0 falsification surfaces … ⚠ HAS A THESIS, NO SEPARATE FALSIFICATION SURFACE (1): HOMER"** | — | — | **False candidate finding.** At `falsification_scan.py:318–319` (`if tpath and p == tpath: continue  # the thesis is the reference, not a surface`), a rail that lives *inside* `thesis/THESIS.md` is dropped as the reference. HOMER's dated rail is therefore invisible to the fleet's only falsification-freshness check, and the sweep reports a gap that does not exist. No mechanical freshness check reads HOMER's rail |
| `maturity_scan.py` (DAEDALUS) | Objective floor | rc 0; `HOMER | Market | L2 | L3? ⚠needs-read | 86 | —` | — | — | Floor L2 with a mechanical L3 hint; no conformance gaps |

---

## 7. Old-profile reconciliation (profile HOMER.md §3 :43–52 and "two L3-blocking absences" :40–41, vintage 2026-08-07)

| Old claim | Verdict | Evidence |
|---|---|---|
| "No `thesis/THESIS.md`" (:41) | **GONE** | THESIS.md exists, 23,077 B, built 2026-09-29 (:3) |
| "No convergence handle of any kind" (:41) | **GONE** | §8 built 2026-10-15, 19/25, 3 roots (THESIS.md:141–171) |
| "No thesis-level kill rail in ANY local form … AUTHOR-from-scratch" (:41, :50 "🔴 DOES NOT EXIST") | **GONE** | Authored from scratch 2026-09-29, frozen and GATES-registered (THESIS.md:3, :34–89; GATES:21). It did not generalize HOM-01/02, as the 8/23 caution required (CATALYSTS.tsv:19) |
| §3 row "PREDICTIONS Invalidation col … LIVE unfired, 7/31; HOM-01 instrument-blocked, HOM-02 resolver ~mid-Aug" | **CHANGED** | HOM-01 FIRED (MISSED early-kill 2026-08-31); HOM-02 arm 1 FIRED 2026-08-13, still LIVE |
| §3 row "HOM-02 NEWLY DISCOVERED SPEC RISK block … exemplary" | **STILL TRUE** | Preserved verbatim in PREDICTIONS.tsv:4 Notes, plus the 8/13 composition-tell grade ("A falling DQ with a rising FC inventory is MIGRATION, NOT CURE") |
| §3 row "7/24 HOM-01 grading sheet … correctly frozen" | **CHANGED** (spent) | The sheet exists; HOM-01 closed 8/31. Per PREDICTIONS.tsv:3 Notes, the sheet now carries rulings A–D. Not re-read by this reader |
| §3 row "CLAUDE Key-Thresholds rail … no scanner-datable stamp … one unrepaired GSE-MF band" | **CHANGED, partly verified** | Re-armed bands now carry dated stamps (CLAUDE.md:114, :119, 2026-09-29). The GSE-MF provision-pairing rule was promoted into thesis C2 (THESIS.md:48, V3 :135). Full threshold table not read (Reader 1) |
| §3 row "Thesis-level kill rail — DOES NOT EXIST" | **GONE** | see above |
| §3 row "MARQUEE … structurally undatable" | not assessed | outside cluster (STATUS) |
| §3 row "board_log … SIG-W-20260802-008 sits at the wire unlogged 5d" | **CHANGED (worse in count)** | Now 29 WALTER packets are unlogged (all dated 10/20–10/27), and board_log has 3 malformed rows (lines 65–67) |
| Anatomy: "SCHEMA.tsv covers only 6 of 8 (no RATES/PRICING rows)" | **GONE** | RATES 8 and PRICING 8 rows present; KB_LIVE 11 |
| Anatomy: "KB_LIVE 15 rows · PIPELINE 54 · MULTIFAMILY 41 · STATE_HSG 59 · BUILDER 80 · RATES 11 · PRICING 20" | **CHANGED** | Now 38 · 80 · 78 · 74 · 99 · 41 · 64 data rows (`tsv_append --check`) |
| 🟡 flag "$160B+ MF-wall re-source owed to CREED" | **GONE** | MULTIFAMILY.tsv:17 "⛔ RETIRED 2026-09-02 … NO PRIMARY EXISTS PUBLICLY" |
| Open question "uniformly-idle-agent blind spot in ledger_staleness" | **STILL TRUE, demonstrated live** | default/`--quiet` all green at 9 days idle; `--abs-floor` exists but is not in HOMER's boot form (CLAUDE.md:199) |
| DO-NOT-TOUCH #1 KB.tsv FROZEN / row-ID contract | **STILL TRUE** | KB.tsv:1 banner. New fact: 3 short rows (rc 1); never "fix" by rewriting rows |
| DO-NOT-TOUCH #2 `state_vectors/corrected/` retrieval hazard | **STILL TRUE** | corrected/SV-06-08-01 carries the CORRECTED banner; SV-06-08-02 carries the REFILED note |
| DO-NOT-TOUCH #8 PREDICTIONS line-1 preamble | **STILL TRUE** | PREDICTIONS.tsv:1 intact (adds a 2026-09-29 correction clause) |

---

## 8. Routing candidates (ranked)

| # | Sev | Owner | Finding | file:line | Where I may be wrong |
|---|---|---|---|---|---|
| 1 | 🔴 | DAEDALUS (tool owner) | `falsification_scan.py` drops a kill rail that lives inside `thesis/THESIS.md` and reports HOMER as NO-RAIL. The only fleet freshness check is blind to HOMER's dated rail, and the sweep produces a false finding against an L3 leg | AGENTS/DAEDALUS/scripts/falsification_scan.py:318–319; output "HAS A THESIS, NO SEPARATE FALSIFICATION SURFACE (1): HOMER" | The exclusion may be intentional: a thesis file is the reference clock. The fix could be a "combined thesis+rail" class (header token like "KILL RAIL") rather than removing the skip. Other desks (AEOLUS, MIDAS, OSPREY in the same bucket) may hit the same skip, or may genuinely lack a rail; I did not check them |
| 2 | 🟠 | PROME (spawn) → HOMER | Desk idle 9 days (last session 10/19) through a dense release window. ~10 docket NEXT dates and 4 ledger `Next:` dates have passed: PMMS 10/22, PHM 10/22, NVR, NRC/PHSI 10/20, NHS 10/27, Case-Shiller ~10/27, Redfin weekly, ICE Sept First Look ~10/22–28 (C1's registered cleanest-flip print), GSE Sept ~10/23–30 (C2 GSE), Apartment List Oct ~10/27–31 (rent band), MTH 10/28. THESIS §9 owes a mechanical fired-count update "at each print" (:89, :175). 29 WALTER packets are unlogged, and CARL is back-filling HOMER's lane (CARL/STATUS.md:37, :41). This is PAT-089 class, but the cause is no session, not a missed pull | CATALYSTS.tsv:5, 11, 13, 14, 16, 20, 24, 28, 31, 42, 43; THESIS.md:202; inbox/WALTER/ | Several prints may not be out yet (GSE window ends 10/30; ICE First Look sometimes lands late). I did not web-verify publication. Until 11/20 no count can change on the cores (V5 :137), so the cost is staleness and consumer drift, not a missed kill |
| 3 | 🟡 | HOMER (and DAEDALUS for the tool) | 6 LIVE ledger headers put `PRIOR HEADER VERBATIM: …Last real data refresh: 2026-10-15` on line 1. ledger_staleness reads 2 clocks and lets the oldest govern, under-reporting freshness by 4 days. KB_LIVE's line-2 form is the fix pattern | RATES.tsv:1, PRICING.tsv:1, PIPELINE.tsv:1, MULTIFAMILY.tsv:1, BUILDER.tsv:1, STATE_HSG.tsv:1; KB_LIVE.tsv:1–2 | The tool could equally learn to ignore clocks after a "PRIOR HEADER VERBATIM" token. Which side moves is a design choice |
| 4 | 🟡 | HOMER / Will | Reading A "no book by charter" is not in the charter; it rests on PROME's gate-row sentence | PROME/GATES.tsv:21 col 5; CLAUDE.md (no clause) | A scorer may accept the GATES sentence plus CARL's consumption as sufficient |
| 5 | 🟡 | HOMER | `tools/rent_breadth.py` exits rc 0 in every band state, and its regression set is not named in its docstring (CHECK_STANDARD §3(e), §9). It is a calculator, not a gate, so this is low risk | tools/rent_breadth.py:1–21, :99–141 | If no script consumes its rc, §9 may be judged not applicable |
| 6 | 🟡 | HOMER (10/19 "orch" session) · PROME (GATES:21) · DAEDALUS (own FLEET_MAP row) | Glued words break the root Output Canon ("never glue words together"): CATALYSTS rows 43–46 ("CONSUMED10/19", "Report2026-10-19_…", "issuer10/16:12.3mo,417090"); RATES/PRICING/PIPELINE line-1 headers ("MND observed7.40", "NHS10/27", "change1/1/27"); GATES:21 col 6 ("owner0/5 killed … formal11/20"); FLEET_MAP HOMER Gaps ("5-point19/25,3independent roots", "liveHOM-02") | as listed | none material; this is a register issue, not a data issue |
| 7 | 🟡 | HOMER | KB.tsv (FROZEN) has 3 rows at 10 of 12 cols, so `tsv_append --check` rc 1. Never rewrite them (frozen, row-ID contract). At most an owner annotation in the banner so a fleet lint does not read it as live corruption. board_log.tsv:65–67 has 4 of 5 cols (Reader 1/3 cluster) | workbook/KB.tsv:14, 26, 27; board_log.tsv:65–67 | The short KB rows may be parent-era trailing-empty trimming that consumers tolerate |
| 8 | 🟡 | HOMER | THESIS defect register D2/D3/D4 (base windows inferred or general knowledge) has been open since 9/29 with no dated pull. A3's satisfiability still rests on "search summaries" | THESIS.md:116–119, :54, :68 | These may be deliberately deferred to the 11/20 grade; no date says so |
| 9 | 🟡 | DAEDALUS | `corrections_boot_check.py`'s named clean acceptance case (HAWK) now returns rc 1. Re-pick it, per its own docstring | scripts/corrections_boot_check.py docstring (rc contract block) | — |
| 10 | 🟡 | REGINALD (informational) | REGINALD's dashboard carries HOMER-domain Trepp MF 7.71% (Apr). HOMER's current figure is 8.04% (Sep) | REGINALD/STATUS_DASHBOARD.md:33; THESIS.md:182 | The row may be a historical vector entry, not a current-value claim |

---

## 9. Not read / coverage limits

| Surface | Coverage |
|---|---|
| thesis/THESIS.md | **WHOLE** (lines 1–202, two chunks 1–80, 81–202; final line 202 seen) |
| thesis/PREDICTIONS.tsv | **WHOLE** (line 1 preamble; header; every cell of HOM-01 and HOM-02, with Notes read through to the final clause) |
| docket/CATALYSTS.tsv | Rows 1–2 and 4–46 **whole**. **Row 3 (servicer watch, 39,082 B) PARTIAL:** fields 1–3, 5–6 whole; F4 (12,377 B) and F7 (26,301 B) first 1,500 chars each, plus regex windows at every 2026-09-29 / 2026-10-xx stamp. ~35 KB of row 3 unread |
| workbook/*.tsv (8 data ledgers) | **Header lines + column-count lint + targeted row reads only** (MULTIFAMILY:17, :74; KB:14; kill/arm regex hits listed in §2). **Bodies NOT read whole** (~556 KB). Row-level content claims rest on the regex hits |
| workbook/SCHEMA.tsv | column-1 counts only |
| workbook/RENT_BREADTH_ROSTER.tsv, rent_breadth_inputs CSV | via header + tool execution only; README whole |
| registry/corrections_receipts.tsv | **WHOLE** (row 2 `COR-20260927-07 APPLIED` has an empty note; it predates the 10/08 WQ-399 field rule) |
| state_vectors/ (5 files) | first 5 lines each only (RETIRED channel) |
| tools/rent_breadth.py | **WHOLE** (1–145) |
| Outside cluster, consulted narrowly | CLAUDE.md lines 1–36, 185, 195–230, 245 + grep hits; STATUS.md 1–12 + grep hits; GATES.tsv:21; CARL/STATUS.md grep; REGINALD/STATUS_DASHBOARD.md grep; CATO run :81; 2 WALTER signal headers |
| Not done | No web verification of whether ICE Sept First Look, GSE Sept, Case-Shiller Aug or Apartment List Oct have published. reports/2026-07-24 grading sheet not re-read. `falsification_scan` behaviour on AEOLUS/MIDAS/OSPREY not checked |
