# DAEDALUS fan-out — VERIFIER P2: independent locator verification of the CARL + LIQUID profile drafts

**Verifier:** P2-VERIFY (read-only, adversarial second reader) · **Run:** 2026-09-17 (Thu)
**Input graded:** `AGENTS/DAEDALUS/profiles/REFRESH_2026-09-17_READER_P2_CARL_LIQUID.md` — PART A for CARL and PART A for LIQUID only (PART B read for cross-reference, not graded).
**Repo HEAD at verification:** `e6abbfd1b` · **Reader's HEAD at draft:** `b824b5a13` (2026-09-17 09:31 ET, an ancestor of HEAD). **Three commits landed between the two** and two of them move cells the draft grades — flagged inline as OVERTAKEN, not as reader error.
**Method:** every claim naming a file, line, section, count, byte size, date, version, script, column or behaviour was opened at the artifact. Bytes by `wc -c`, counts by `grep -c`/`awk`, dates by `git log -1 --format=%cs`, script behaviour by reading the code. Tool runs: `read_cap_check.py --agent {CARL,STUE,DOC,GIG,META,PHAN,POLLY,POP,LIQUID}` · `ledger_staleness.py {CARL,LIQUID}` · `corrections_boot_check.py {CARL,LIQUID}` · `roadmap_index.py --check` · `falsification_scan.py` (whole, `--agent CARL --tsv`, `--agent LIQUID --tsv`) · `AGENTS/LIQUID/scripts/boot.py --selftest` · `fetch.py fred BAMLH0A0HYM2`. Nothing outside this file was written.

⚠️ **SCANNER-VINTAGE CAVEAT (self-correction, made before this file was delivered).** `AGENTS/DAEDALUS/scripts/falsification_scan.py` is **modified-uncommitted in the working tree** — DAEDALUS fixed it during this fan-out, and the fix's own comment credits *"P2 reader D-1"*. My first pass ran the working-tree build and graded the reader's two scanner claims FAILED. That was **my** error, of exactly the class the fleet memory names `finding_a_pinned_reproduction_cannot_confirm_a_cure`: I tested the CURE and graded the DIAGNOSIS. Both claims are re-graded below against the **committed** scanner, with the root cause reproduced directly. Every scan figure in this file states which build produced it.

**Verdicts:** VERIFIED (matches) · FAILED (artifact says otherwise) · DRIFTED (true, locator/count off — correct one given) · UNLOCATED (no locator and not found in ≤2 tries) · OVERTAKEN (true at the reader's HEAD, moved since).

---
---

# DESK 1 — CARL

## 1. Verification table — CARL PART A

| § | Claim (≤20 words) | Verdict | Correction / evidence |
|---|---|---|---|
| Hdr | Sources: CLAUDE.md 290 ln / 48,543 B | VERIFIED | `wc -c/-l` exact |
| Hdr | Sources: STATUS.md 118 ln / 22,780 B | VERIFIED | exact |
| Hdr | Sources: THESIS.md 471 ln / 94,117 B | VERIFIED | exact |
| Hdr | Sources: `thesis/PREDICTIONS.tsv` (32 rows) | DRIFTED | 33 lines = 2 comment/declaration + 1 column-header + **30** data rows |
| Hdr | Sources: KB.tsv 482 rows · CATALYSTS 24 rows | VERIFIED | `grep -c '^KB-CARL-'` = 482; CATALYSTS 24 data rows |
| Hdr | Staleness ①: `THESIS.md:2` `**Version:** 2.6.6` | VERIFIED | line 2 reads `**Version:** 2.6.6 \| **Updated:** 2026-08-27` |
| Hdr | Staleness ②: score token on `STATUS.md:1` ≠ `53/70` | **FAILED** | `STATUS.md:1` is `# CARL STATUS` — **no score token**. The clause fires on day one (a permanent-red guard). Score lives on **`STATUS.md:2`** (also `:94`, `:96`). Corrected below |
| Hdr | Staleness ③: `sub_agents/*/` count ≠ 7 | VERIFIED | `ls -d` = 7 |
| Hdr | Staleness ④: `read_cap_check --agent STUE` stops returning 🔴 | VERIFIED | rc=1; `🔴 STATUS.md 124,067 B 381% of budget, OVER THE CAP (229%)` |
| Hdr | Staleness ⑤: >45d, checkpoint 2026-11-01 | VERIFIED | 2026-09-17 +45d = 2026-11-01 |
| §1 | Class Market per FLEET_MAP col 2 | VERIFIED | `FLEET_MAP.tsv` CARL col 2 = `Market` |
| §1 | `LABOR → CARL → REGINALD` at `CLAUDE.md:4` | VERIFIED | verbatim |
| §1 | Cedes list at `CLAUDE.md:34-39` | VERIFIED | `:34` "**You do NOT own:**"; `:39` RED/handoff_RED |
| §1 | Housing promoted to HOMER 2026-07-12 (`CLAUDE.md:23`) | VERIFIED | verbatim |
| §1 | STATUS Housing section at `:29-34` | DRIFTED | section heading is **`STATUS.md:26`**; range is **:26-34** |
| §1 | 7 sub-agents, file counts STUE 52 DOC 18 GIG 20 PHAN 24 POLLY 16 POP 18 META 7 | VERIFIED | `git ls-files` each; total 155 |
| §1 | All seven carry `inbox/` (`TEAM.md:9-20`) | VERIFIED | 7/7 dirs exist; `TEAM.md:9` is the INBOX LAYER header |
| §1 | POP dossier 7/24 · POLLY 8/10 · META FROZEN | VERIFIED | `TEAM.md` §Dossier-mode / §Frozen-dead |
| §2 | Execution-contract reconciliation at `CLAUDE.md:90-92` | VERIFIED | `:90` "Execution contract (reconciled September16)" |
| §2 | Doc-ownership / mirror-pair table `:162-180` | DRIFTED | `:162` header, mirror pairs `:175-178`; `:180` is `---` → **:162-179** |
| §2 | Workbook discipline `:182-197` · matrices `:200-224` · thresholds `:226-238` · FILES `:252-290` | VERIFIED | each header on its stated line |
| §2 | STATUS 118 ln / 22,780 B = 70% of 32,550 B | VERIFIED | 22,780/32,550 = 69.98% |
| §2 | STATUS anchors `:64` matrix · `:87` histogram · `:98` obligations · `:113` judgment | VERIFIED | all four exact |
| §2 | Prediction mirror moved out 2026-09-01 | VERIFIED | `CLAUDE.md:177` "MOVED OUT OF STATUS.md 2026-09-01" |
| §2 | THESIS anchors `:69 :100 :137 :183 :193 :205 :225 :241 :277 :306 :319 :333 :344 :355 :370 :395 :443 :457` | VERIFIED | all 18 exact |
| §2 | PREDICTIONS "11 cols, 30 CRL rows + 2 header/declaration rows" | DRIFTED | 11 cols ✓, 30 rows ✓; **three** non-data lines (2 comments + 1 column header) |
| §2 | Tally 15 OPEN / 7 MISSED / 4 CONFIRMED / 1 CONFIRMED\* / 1 MIXED / 1 RETIRED / 1 NO-VERDICT | VERIFIED | `awk` col 6 tally exact |
| §2 | Cols incl. `Invalidation` (9) and `Instrument` (11) | VERIFIED | column header line 3 |
| §2 | Header line 1 two-clock `2026-09-11`; line 2 cadence declaration (Sweep #4) | VERIFIED | verbatim |
| §2 | CHANGELOG 229,073 B | VERIFIED | exact |
| §2 | Seven grading-card files present | VERIFIED | `thesis/` holds all 7 + THESIS + PREDICTIONS + CHANGELOG + `proposals/` = 11 tracked |
| §2 | KB.tsv 482 rows, max KB-CARL-486, 561,702 B, 15 cols, `Delegated_To` | VERIFIED | all exact |
| §2 | VX/FLOW/BNPL_STRESS/STATE_DIFFUSION/TRENDS FROZEN 2026-06-26 line 1 | VERIFIED | all five banners read verbatim |
| §2 | ABS_BASELINE FROZEN 2026-07-10 line 1 | VERIFIED | verbatim |
| §2 | SCHEMA 4,211 B; LEDGER_GLOB extended to `sub_agents/*/workbook/*.tsv\|md` (STUE 7/31, 37 child ledgers) | VERIFIED | LEDGER_GLOB body verbatim |
| §2 | PREDICTIONS_MIRROR 20,529 B, Check-A-enforced | VERIFIED | `CLAUDE.md:176-177` |
| §2 | ROADMAP 18,617 B + THREADS 38,755 B; `--check` ✓ byte-for-byte, 35 threads | VERIFIED | ran it: `ROADMAP-INDEX ✓ live index block matches regeneration byte-for-byte (35 thread(s))`, rc=0 |
| §2 | Check C declined, "no script checks this pair" (`CLAUDE.md:180`) | DRIFTED | text is at **`CLAUDE.md:178`** |
| §2 | NEXUS fold ordering checkable (`CLAUDE.md:14b`) | DRIFTED | `14b` is a **boot-step number**, not a line — it is **`CLAUDE.md:110`** |
| §2 | NEXUS_BRIEF header `As of: 2026-09-17 08:46 ET \| STATUS commit: a5bfc743b` | VERIFIED | verbatim, `NEXUS_BRIEF.md:6` |
| §2 | SCRATCH 7,392 / MEMORY 11,908 / TEAM 14,029 / SPAWN_PROTOCOL 13,461 B | VERIFIED | exact |
| §2 | `board/BOARD_LOG.tsv` 766 ln 9 cols; `board_log.tsv` 70 ln 5 cols; walter_doctor no fallback (`CLAUDE.md:5b`) | DRIFTED | all content VERIFIED; `5b` is a **step number** — the text is **`CLAUDE.md:73-74`** |
| §2 | TRADE.md 51 ln, retired by design | VERIFIED | own banner line 1-2 |
| §2 | `scripts/` (18 files) | DRIFTED | 18 **top-level entries** = **16 files + 2 dirs** (`__pycache__`, `data`); **20** tracked paths |
| §2 | boot.py runs thresholds·gas·consumer·housing·docket·abs·consistency_check·board_gap, board_gap unconditional fail-closed | VERIFIED | `boot.py:34-61`; `board_gap.py` returns 2 at `:125,:129,:148` |
| §2 | consistency_check 60,338 B, A/B/D/E/F/G shipped, C declined, spec 24,336 B | VERIFIED | `def check_{a,b,d,e,f,g}` present; spec `:249` "Check C — NOT built, and the reasoning" |
| §2 | handoff_RED 6 files; COUNTER_LOG fresh 2026-09-11 | VERIFIED | `git log -1 --format=%cs` = 2026-09-11 |
| §2 | sub_agents 155 tracked files | VERIFIED | exact |
| §2 | `domain/sources/2026-09-16_{key-file-audit,news-catchup,closeout-procedure-review}.md` | VERIFIED | all three present (+ a closeout-receipt JSON) |
| §3 | 53/70 (76%), 14 vectors, Independence map ≈ ~10 roots (`THESIS.md:319`) | VERIFIED | `:331` "14 vectors ≈ **~10 effectively independent roots**" |
| §3 | Re-spec base rates 5.4% / incumbent 25.0% / direction-only 43.5% over 94 quarters; 25:Q2 counterfactual | VERIFIED | `THESIS.md:412,414,416,418` |
| §3 | Count RESET 1-of-2 → 0-of-2; Rider 1 shadow grade mandatory | VERIFIED | `THESIS.md:410,420` |
| §3 | 13.74% retired, replaced by CRL-30 flow ≥7.50%; struck row at `CLAUDE.md:205` | DRIFTED | struck send-matrix row is **`CLAUDE.md:207`**; the struck KEY-THRESHOLDS row is **`:232`**. `:205` is a table separator |
| §3 | CRL-05 closed `NO-VERDICT-BY-BASIS` 2026-09-10 | VERIFIED | Status cell token is `NO-VERDICT`; the phrase `NO-VERDICT-BY-BASIS` is in the Outcome cell |
| §3 | CRL-30 instrument `>=7.50%` NY Fed HHDC CC flow into 90+ | VERIFIED | col 11 verbatim |
| §3 | ⛔ SIGNALS→WALTER, ANALYSIS/PACKETS→direct (`CLAUDE.md:12`, corrected 2026-09-02) | **FAILED** (locator) | `:12` is the K-shape line. The rule is at **`CLAUDE.md:101`** (boot step 12) and **`:269`** (FILES row, "Corrected 2026-09-02") |
| §3 | TEAM §REFRESH RULES rewritten 7/10; "staleness is a citation rule, not a spawn alarm" | VERIFIED | `TEAM.md:64`, quote verbatim at `:67` |
| §3 | WQ-183 ② Will 2026-09-07 — parent holds the pen | VERIFIED | `inbox/processed/2026-09-07_from-PROME_WQ-183-RULED-…` |
| §3 | CRL-01/09/19 are the boot-step-7c calibration set | NOT-ADJUDICATED | not opened this pass |
| §3b | "`falsification_scan.py` finds **ZERO** surfaces for CARL" | VERIFIED *(committed build)* / OVERTAKEN | **Root cause reproduced:** the committed `live_thesis()` tests `"STALE-VINTAGE" in head.upper()`, which matches the **prose** phrase *"two stale-vintage recirculation traps"* at `CARL/thesis/THESIS.md:2` → CARL's LIVE v2.6.6 thesis was classified dead-bannered, `ver` forced None, no surface row emitted. **The working-tree build (uncommitted) fixes this and credits "P2 reader D-1"**; under the fixed build CARL yields **one** row — `thesis/CHANGELOG.md`, CURRENT, stamp 2026-09-16 |
| §3b | "CARL appears only in the prose bucket *dead-bannered (2): CARL, HAWK*" | VERIFIED *(committed build)* / OVERTAKEN | Correct against the committed scanner and correctly diagnosed as a false positive (flag D-1). The **fixed** build prints `dead-bannered (1): HAWK` and CARL appears in no bucket. Marker-word-in-prose — `[[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]]` |
| §3b | `SURFACE_PATTERNS` at `falsification_scan.py:38-43` | VERIFIED | exact |
| §3b | Exit row: leg1 <220K×8wk AND leg2 ≥100bp over 2 qtrs; "CURRENT STANDING: 0 OF 2" inline | VERIFIED | `THESIS.md:398-399,410` |
| §3b | Per-vector triggers V1 <12%×2 · V3 <0.65%×2 FIRED 7/2 · V4 <9% | VERIFIED | V3 row at `THESIS.md:292` |
| §3b | V5 "AAA <$4.00 sustained 2wk" listed as a **downgrade** trigger | DRIFTED | the registered $4.00 gate (`THESIS.md:294`) is an **UPGRADE** gate — *"still ≥$4.00 at Monday 8/3 close → EXECUTE 3→4; retrace <$4.00 first → hold 3"* — executed 2026-08-03 |
| §3b | CRL-20/21 masking windows at `THESIS.md:405-407` | DRIFTED | they are at **`THESIS.md:426-428`**; `:405-407` is the SUPERSEDED-TEXT quote block |
| §3b | KILL_RULE_RESPEC 26,220 B · HHDC_Q2 card 28,817 B · TRADEDOWN 10,426 B · COUNTER_LOG 30,513 B | VERIFIED | all four exact |
| §3b | "August graded 3 of 3 AGAINST (`STATUS.md:54`)" | DRIFTED | the row is **`STATUS.md:59`** (also mirrored at `:77`); `:54` is the UI-exhaustion row |
| §3b | Child ledgers: DOC 10 · GIG 8 · **PHAN 45** · **POLLY 9** · **POP 9** | **FAILED** | Actual prediction IDs: DOC **10** ✓ · GIG **8** ✓ · PHAN **7** (P01–P07) · POLLY **8** · POP **8**. STUE keeps no PREDICTIONS.tsv. "45" is PHAN's *line* count (46 lines, almost all comment prose) |
| §4 | Better-than-blueprint 1–6 (re-spec, 3-mechanism split, independence map, Delegated_To, check suite, two read-mode splits) | VERIFIED | each sub-claim checked at the artifact |
| §4 | ROADMAP.md:6 quoted "CARL has a coherence checker; a sub-agent does not" | DRIFTED | locator right, **quotation is a paraphrase**: *"CARL ruled against a hot/cold split on STUE's surface because no coherence checker reaches a sub-agent. **CARL has one**"* |
| §4 | TRADE.md not-a-gap (`CLAUDE.md:272`) | DRIFTED | the TRADE.md FILES row is **`CLAUDE.md:262`**; `:272` is the THESIS.md row |
| §4 | CLAUDE.md 48,543 B rule-exempt per `READ_CAP.md:38` | VERIFIED | `:38` is the `CLAUDE.md` "**No** — auto-loaded into context… watch, don't rotate on this rule" row |
| §4 | debt (a) `CLAUDE.md:10` and `:272` still assert v2.5.1 | VERIFIED | both lines read `v2.5.1` |
| §4 | debt (b) 7 of 24 docket rows past-dated, oldest 8/29 | VERIFIED | 8/29, 8/31×2, 9/10, 9/14, 9/15, 9/16 = 7 |
| §4 | debt (c) STUE bounded head = 80,967 B, defect at `STUE/CLAUDE.md:246` | VERIFIED | measured head(1-471)+ROUTED(533-556)+BOTTOM LINE(663-end) = **80,967 B** exactly; rule at `:246` |
| §4 | debt (d) **16** sub-agent ledgers STALE (DOC 6, GIG 6, POLLY 5, STUE 1) | **FAILED** | `ledger_staleness.py CARL` → **"17 stale"**: DOC **5** · GIG 6 · POLLY 5 · STUE 1. Parent ledgers: 0 stale |
| §4 | debt (d) "TEAM.md's 9/16 header states this itself" | DRIFTED | `TEAM.md:3` says *"No subagents launched or child ledgers refreshed"* — it declares the **non-refresh**, not a stale count |
| §4 | debt (e) 4 unprocessed sub-agent packets; DOC 37d, POP 33d | VERIFIED | STUE 9/10 · DOC 8/11 (37d) · PHAN 9/11 · POP 8/15 (33d); CARL top-level inbox = 0 |
| §4 | debt (f) no literal BOTTOM LINE heading; `## Current judgment` at `:113` | VERIFIED | `grep -i "bottom line" STATUS.md` → 0 hits |
| §4 | closed: ABS_BASELINE frozen · consistency_check shipped · STATUS 118 ln rc=0 | VERIFIED | all three |
| §5 | 1 payment hierarchy Auto→Mortgage→Student→CC | VERIFIED | `CLAUDE.md:51` |
| §5 | 2 masking narrowed 6→4 issuers | VERIFIED | `THESIS.md:100,102` |
| §5 | 3 Page 14 Data, never report prose, NEVER Page 28 (±0.01pp ×5 qtrs then +0.39pp in 26:Q2) | VERIFIED | **verbatim at `THESIS.md:400`** (locator was missing in the draft) |
| §5 | 4 13.74% dead; charged-off stay on bureau reports ~40%→80% at 1yr | VERIFIED | `CLAUDE.md:232` |
| §5 | 5 Bifurcated timing axis A (FFIEC, un-maskable) vs B (extend-and-pretend) | VERIFIED | `THESIS.md:205,210-211` |
| §5 | 6 six frozen ledgers; KB the only live parent ledger | VERIFIED | banners + `ledger_staleness` |
| §5 | 8 Check C declined, no script covers CATALYSTS↔CALENDAR | VERIFIED | `CLAUDE.md:178` + spec `:249` |
| §5 | 10 `board_log.tsv` path lock; ~3 months read as "keeps no board_log" | VERIFIED | `CLAUDE.md:73`; `board_log.tsv:3` root-cause note |
| §5 | 11 CARL is §3.5 pull-complete EXEMPT | VERIFIED | `AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md:116` names CARL; `inbox/WALTER/` = 0 files |
| §5 | 12 KB-CARL-450: INFO_ONLY sat 27 days before CRL-10 cut 62%→8% | VERIFIED | disposition 2026-08-15 → self-audit 2026-09-11 = 27d; CRL-10 conf cell `8% (was 62 …)` |
| §5 | 13 boot.py prints with `flush=True`; never pipe | VERIFIED | `boot.py:214` |
| §5 | 16 META packet has no scheduled reader (`TEAM.md:22`) | DRIFTED | text is at **`TEAM.md:25`**; `:22` is blank |
| §6 | FLEET_MAP CARL row L4 / H / last-scored 2026-09-01 | VERIFIED (at HEAD) | `git show HEAD:` = `2026-09-01`. ⚠️ The **working tree** carries an uncommitted DAEDALUS edit to `2026-09-17` with Gaps *"L5 DENIAL REFUTED … All three prior Next_upgrade legs are discharged or re-homed"* — the draft's D-2/D-3 finding is already being actioned |
| §6 | boot.py whitelist widened 9/1 21:51 (`052c36faf`) / 22:05 (`dcfdb9037`), 23 min after the row was cut | VERIFIED | Production Review #5 `31e0b90d7` 21:28:53 → 21:51:58 = **23 min** |
| §6 | `zero YEYOU flags` is a default-zero instrument (PAT-060 / WQ-181 ②) | VERIFIED | `AGENTS/DAEDALUS/CLAUDE.md:99` + ladder table |
| §7 | Q1–Q6 carried as NOT-ADJUDICATED / CANNOT-EVALUATE | VERIFIED | self-declared, correctly |

## 2. Totals — CARL

| Verdict | N |
|---|---:|
| VERIFIED | 59 |
| DRIFTED | 15 |
| FAILED | 4 |
| UNLOCATED | 0 |
| OVERTAKEN | 0 *(2 rows carry VERIFIED/OVERTAKEN jointly)* |
| NOT-ADJUDICATED | 1 |
| **Graded** | **79** |

**The four FAILED:** ① staleness clause ② keyed to `STATUS.md:1` (no score token there — a permanently-firing trigger) · ② child prediction counts PHAN 45 / POLLY 9 / POP 9 (actual 7 / 8 / 8) · ③ 16 stale sub-agent ledgers (actual **17**; DOC is 5 not 6) · ④ the `CLAUDE.md:12` locator for the SIGNALS→WALTER rule (it is `:101` / `:269`).
**Withdrawn by the verifier:** the two scanner claims, first graded FAILED against the fixed working-tree build, are correct against the committed build — see the SCANNER-VINTAGE CAVEAT.

## 3. CORRECTED PART A — CARL *(install-ready)*

---

# Agent Profile — CARL

**Profile vintage:** 2026-09-17 (Mode-A: reader draft P2 + independent locator verification; installed by DAEDALUS)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** Mode-A — 1-reader full re-read (fan-out slot P2) + an independent adversarial locator verification pass (slot P2-VERIFY), both read-only, artifact-verified.
**Sources read:** `AGENTS/CARL/CLAUDE.md` (290 ln / 48,543 B), `STATUS.md` (118 ln / 22,780 B), `TEAM.md`, `NEXUS_BRIEF.md`, `ROADMAP.md` + `ROADMAP_THREADS.md` (index check run), `thesis/THESIS.md` (471 ln / 94,117 B), `thesis/PREDICTIONS.tsv` (30 data rows + 3 header lines), `thesis/` dir listing (11 tracked), `workbook/` (KB.tsv 482 rows, SCHEMA, LEDGER_GLOB, 6 frozen ledgers), `docket/CATALYSTS.tsv` (24 rows) + `CALENDAR.md`, `scripts/` listing + `boot.py` KEY_MARKERS/FAILURE_MARKERS_CF, `board_log.tsv` + `board/BOARD_LOG.tsv`, `handoff_RED/` listing, all seven `sub_agents/*/`, plus tool runs: `scripts/read_cap_check.py --agent CARL` and `--agent {DOC,GIG,META,PHAN,POLLY,POP,STUE}`, `scripts/ledger_staleness.py CARL`, `scripts/corrections_boot_check.py CARL`, `AGENTS/CARL/scripts/roadmap_index.py --check`, `AGENTS/DAEDALUS/scripts/falsification_scan.py` (whole + `--agent CARL --tsv`).
**Staleness (file-readable — every clause machine-evaluable; run 2026-09-17, all five at their stated values):** refresh when **ANY** of —
1. `AGENTS/CARL/thesis/THESIS.md:2` `**Version:**` ≠ `2.6.6`; **or**
2. the score token on `AGENTS/CARL/STATUS.md:2` ≠ `53/70` *(⚠️ **not line 1** — line 1 is the bare title `# CARL STATUS`; a clause keyed there fires every run)*; **or**
3. the count of `AGENTS/CARL/sub_agents/*/` directories ≠ **7**, or a row moves between the ROSTER / Dossier-mode / Frozen tables of `AGENTS/CARL/TEAM.md`; **or**
4. `python3 scripts/read_cap_check.py --agent STUE` stops returning a 🔴 on `STATUS.md` (i.e. the sub-agent read-cap breach is cured — at 2026-09-17 it is rc=1, **124,067 B = 381% of budget, 229% of the hard cap**); **or**
5. **> 45 days** — hard checkpoint **2026-11-01**.

> Durable understanding — section-tasks read THIS, not the raw (heavy) agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity

U.S. consumer financial stress: credit delinquency (CC / auto / student / mortgage-consumer-read), K-shape bifurcation, consumer spending and trade-down, gas-pump and energy-CPI pass-through, ABS (subprime auto / card trusts), consumer-cost insurance & healthcare, small-business owner-income. **Class:** Market (`FLEET_MAP.tsv` CARL row col 2). **Transmission seat — the MIDDLE:** `LABOR → CARL → REGINALD` (`AGENTS/CARL/CLAUDE.md:4`), i.e. CARL measures how employment + cost stress *converts* into credit deterioration; also feeds HENRY (V14 wealth effect), LIQUID (ABS subordinate-CE breach), MARCO/CORAL (FL), BROCK (private-credit pointer). **Spawnable by:** PROME / Will.

**Cedes (one-source-of-truth), `CLAUDE.md:34-39`:** employment → LABOR · bank-level impact → REGINALD · migration/tourism → MARCO · oil/Brent spot → HAWK/BRENT (CARL owns pump + downstream energy CPI) · counter-thesis → RED (CARL *stages* in `handoff_RED/`, does not maintain) · HY OAS series → LIQUID · private-credit gate-count → BROCK. **Housing promoted out:** foreclosures/builders/MF → `AGENTS/HOMER/` since 2026-07-12; CARL retains the consumer-transmission reads (`CLAUDE.md:23`; STATUS Housing section at `STATUS.md:26-34`).

**Sub-agent layer — 7 dirs at HEAD** (`AGENTS/CARL/sub_agents/`, 155 tracked files): **STUE** student loans (52 files, the heaviest child) · **PHAN** phantom debt — **DOSSIER form** (24) · **GIG** gig economy (20) · **DOC** healthcare (18) · **POP** small business — **dossier-mode since 2026-07-24** (18) · **POLLY** insurance — **dossier-mode since 2026-08-10** (16) · **META** — **FROZEN, do-not-spawn** (7). Roster + demotion record: `TEAM.md` §ROSTER / §Dossier-mode / §Frozen-dead. All seven carry an `inbox/` (Will-ruled 2026-08-02, built 8/3 — `TEAM.md:9-20`).

**One line:** *"Is the U.S. consumer cracking, and how fast does the cost/employment squeeze convert into credit deterioration that lands on banks?"*

## 2. File anatomy (where the richness lives) — HEAVY: `thesis/` + `workbook/` + `docket/` + `sub_agents/` + two board ledgers

| File | Holds | Richness? |
|---|---|---|
| `CLAUDE.md` (290 ln / **48,543 B**) | charter: identity, domain scope, K-shape methodology, **the fleet's longest BOOT+CLOSEOUT contract** (steps 0→16 with a September-16 "execution contract" reconciliation at `:90-92`), doc-ownership/mirror-pair table (`:162-179`), workbook-mutation discipline (`:182-197`), send/receive matrices (`:200-223`), key thresholds (`:226-237`), FILES map (`:252-290`). ⚠️ **Boot steps are numbered separately from lines** — step 5b = `:73-74`, step 12 = `:101`, step 14b = `:110`, step 15 = `:111`. Cite the line, never the step, in a locator | charter — **the densest in the fleet**; excluded from the read-cap rule (`BLUEPRINTS/READ_CAP.md:38`) but auto-loaded every boot |
| `STATUS.md` (118 ln / 22,780 B; 70% of the 32,550 B budget) | live dashboard — 4 dashboard tables (Credit `:11` / Housing-consumer `:26` / Insurance-Health `:35` / Macro-Energy `:39`) with Value·AsOf·Status, **CONVERGENCE MATRIX mirror** (`:64`), score histogram (`:87`), **Active obligations and limitations** (`:98`), **Current judgment** (`:113`). Score token lives on `:2`. Prediction mirror MOVED OUT 2026-09-01 → `PREDICTIONS_MIRROR.md` (`CLAUDE.md:177`) | live state |
| `thesis/THESIS.md` (471 ln / 94,117 B) — **canonical** | "Beneath the Ice" **v2.6.6** (`:2`, updated 2026-08-27). Core thesis · 5 Load-Bearing Vectors (`:69`) · **Cross-Industry Data Masking Framework** (`:100`, 4 issuers, narrowed 6→4 at `:102`) · K-shape Selection + Tariff Transmission siblings (`:137`, separation argument `:171`) · Path C ladder + provisional/firm distinction (`:183,:193`) · Path C **Bifurcated Timing Axis** (`:205`) · Path PC (`:225`) · Trade Duration (`:241`) · **Convergence Score 53/70** (`:277`) + histogram (`:306`) + **Independence map** (`:319`, reading rule `:331`) + honest commentary (`:333`) + upgrade path (`:344`) + **Fast Early-Warning 1-mo Kill** (`:355`) · Thesis Evolution (`:370`) · **Exit / Invalidation Rules** (`:395`, instrument pin `:400`, superseded text `:405-407`, masking windows `:426-428`) · Counter-Signals→RED (`:443`) · Open Work Items (`:457`) | **the brain — fleet-exemplary** |
| `thesis/PREDICTIONS.tsv` (11 cols, **30 CRL rows** + 3 header lines: 2 comment/declaration + 1 column header; 103,186 B) | canonical ledger CRL-01..CRL-30. **15 OPEN · 7 MISSED · 4 CONFIRMED · 1 CONFIRMED\* · 1 MIXED · 1 RETIRED · 1 NO-VERDICT.** Cols: Pred_ID/Date_Made/Prediction/Confidence/Timeframe/Status/Date_Resolved/Outcome/**Invalidation**(9)/Notes/**Instrument**(11). Header line 1 = two-clock (`Last real data refresh: 2026-09-11`); line 2 = a **cadence declaration** answering Staleness Sweep #4 (event-driven, not calendar) | institutional learning loop |
| `thesis/CHANGELOG.md` (229,073 B) | every version bump + prediction change, old→new. ⚠️ **This is the ONE CARL surface `falsification_scan.py` sees** (class `changelog/pivot log`, CURRENT, stamp 2026-09-16) | history — **SKIP at grade** |
| `thesis/KILL_RULE_RESPEC_2026-08-15.md` · `HHDC_Q2_2026_GRADING_CARD.md` · `HHDC_Q3_..._TEMPLATE.md` · `TRADEDOWN_INSTRUMENTS.md` · `BRIER_AUDIT_2026-07-24.md` · `CARL_BOOK_DESIGN.md` · `FOMC_JUL28-29_CARL_CONSUMER_LEG.md` | the grading-card layer: pre-registered grade defs + the v2.6.6 kill re-spec working + the T1/T2 trade-down instrument spec + the Brier calibration audit | **where falsification actually gets executed** |
| `workbook/KB.tsv` (482 rows, max **KB-CARL-486**, 561,702 B, 15 cols, LIVE) | canonical record — Admiralty conf + EMPIRICAL/ESTIMATE/ASSUMPTION epistemic + **Delegated_To** (7 sub-agents) | permanent record |
| `workbook/{VX,FLOW,BNPL_STRESS,STATE_DIFFUSION,TRENDS}.tsv` | **FROZEN 2026-06-26** banners verified on all five (line 1 of each) | frozen — do NOT append |
| `workbook/ABS_BASELINE.tsv` | **FROZEN 2026-07-10** banner verified (line 1) — *the old profile's open debt item (d) is CLOSED* | frozen |
| `workbook/SCHEMA.tsv` (4,211 B) · `workbook/LEDGER_GLOB` | col defs (boot step 3) · **glob extended to `sub_agents/*/workbook/*.tsv` and `*.md`** (STUE 7/31 fix — 37 child ledgers were outside enforcement) | durable method |
| `PREDICTIONS_MIRROR.md` (20,529 B) | human mirror of the TSV; **machine-checked by consistency_check Check A**. Never resolve here | mirror |
| `ROADMAP.md` (18,617 B) + `ROADMAP_THREADS.md` (38,755 B) | **RESTRUCTURED 2026-09-05 (Will-directed read-cap fix, `ROADMAP.md:4-6`):** ROADMAP carries a **GENERATED index** (`roadmap_index.py --rebuild`; `--check` is a closeout gate — verified 2026-09-17: `✓ byte-for-byte, 35 thread(s)`, rc=0); the per-thread narrative lives in THREADS, **grep-only, never read whole** | cross-session process state |
| `docket/CATALYSTS.tsv` (24 rows, 7 cols) + `docket/CALENDAR.md` | **single source of truth for forward catalysts**; boot countdown inside `boot.py`; past-due rows flagged "integrate & prune". **Check C (TSV↔CALENDAR) was EVALUATED AND DECLINED — no script checks this pair** (`CLAUDE.md:178`; reasoning in `scripts/CONSISTENCY_CHECK_SPEC.md:249`) | forward state |
| `NEXUS_BRIEF.md` (9,160 B) | cross-agent twin of SCRATCH; **mandatory every session**, and the **fold must be the LAST write-back** (NEXUS Amendment 10; checkable as brief-commit-ts ≥ STATUS-commit-ts, `CLAUDE.md:110`, boot step 14b). Header at HEAD: `As of: 2026-09-17 08:46 ET \| STATUS commit: a5bfc743b` | sync surface |
| `SCRATCH.md` (7,392 B) / `MEMORY.md` (11,908 B) / `TEAM.md` (14,029 B) / `SPAWN_PROTOCOL.md` (13,461 B) | handoff (template-rewritten every session) / persistent feedback+findings / sub-agent roster+freshness+spawn rules / how to spawn | process memory |
| `board/BOARD_LOG.tsv` (766 ln, 9 cols) **and** `board_log.tsv` (70 ln, 5 cols) | **TWO live, non-duplicate ledgers**: `board/BOARD_LOG.tsv` = v0.1 canonical disposition scan of `BOARD/INDEX.md`; root `board_log.tsv` = v0.2 delivery-lane mirror **read by `AGENTS/WALTER/tools/walter_doctor.py` at exactly that path with NO fallback** (`CLAUDE.md:73-74`, boot step 5b) | intake ledgers |
| `TRADE.md` (51 ln) | **⛔ RETIRED BY DESIGN (Jun 26)** — transmission-middle desk holds no book. **NOT a gap** (see §4; FILES row at `CLAUDE.md:262`) | retired stub |
| `scripts/` (16 files + `data/` + `__pycache__`; 20 tracked paths) | `boot.py` (boot step 7.0 orchestrator, `:34-61` — thresholds · gas_tracker · consumer_pulse · housing_pulse · docket_countdown · abs_monitor · consistency_check · **board_gap unconditionally, fail-closed rc=2**) · `consistency_check.py` (**60,338 B — Checks A/B/D/E/F/G SHIPPED**; C declined) + its 24,336 B spec · `roadmap_index.py` · `board_gap.py` + `test_board_gap.py` · `brier_audit.py` · domain pulls | **the fleet's deepest agent-local check suite** |
| `handoff_RED/` (6 files) | counter-evidence staged for RED. `COUNTER_LOG.md` fresh (last commit 2026-09-11); the other four are Apr–Jun vintage **by design** — CARL stages, RED owns, **do NOT maintain** | cross-agent stage |
| `sub_agents/` (155 tracked files) | see §1 and §5. Per-agent anatomy → `upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md` | audited layer |
| `archive/`, `status_archive/`, `research/`, `domain/sources/` | rotation blocks, retired docs, deep dives; `domain/sources/2026-09-16_{key-file-audit,news-catchup,closeout-procedure-review}.md` are the freshest reports | reference |

## 3. Per-dimension local representation

| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | `thesis/THESIS.md` (canonical) → STATUS header line summary | "Beneath the Ice" **v2.6.6**; 5 Load-Bearing Vectors + Paths A/B/C/F/PC + **3 separately-held mechanisms** (Masking `:100` / K-shape Selection `:137` / Tariff Transmission) | exemplary |
| Convergence / scoring | `THESIS.md:277` Convergence Score (canonical) → `STATUS.md:64` matrix mirror + `:87` histogram | 14 vectors, 5-pt definition biased AGAINST 5, **53/70 (76%)**, per-vector version history + reason-for-change + downgrade trigger; **Independence map** (`THESIS.md:319`) says 14 vectors ≈ **~10 effectively independent roots** (`:331`) — "never read 53/70 as 14 confirmations" | exemplary |
| Invalidation / exit | `THESIS.md:395` Exit/Invalidation + `:355` Fast Early-Warning 1-mo Kill + per-vector downgrade triggers + the CRL-20/21 masking windows (`:426-428`) + the Path-C ladder; STATUS `:98` Active obligations | **the deepest falsification loop in the fleet**, and it got *deeper* this period: the **full-thesis kill was RE-SPECCED v2.6.6 (8/27)** — leg 2 moved off the CC 90+ balance SHARE onto the NY Fed **Page 14 Data** transition rate into 90+, with a **≥100bp cumulative floor** over 2 consecutive quarters, **base-rated at 5.4% over 94 quarters** against the incumbent's **25.0%** and a direction-only draft's **43.5%** (`THESIS.md:412-418`). The count **RESET 1-of-2 → 0-of-2** (`:410`) and CARL is the beneficiary and said so before Will ruled. **Rider 1: the AS-WRITTEN shadow grade is MANDATORY on every future card** (`:420`) | exemplary |
| Thresholds | `CLAUDE.md:226-237` KEY THRESHOLDS + STATUS dashboard (live) + PREDICTIONS `Instrument` column + per-vector triggers | named anchors with implication and source-tag discipline. **Live state:** the CC-90+ **13.74% GFC bar is RETIRED** (CRL-05 closed 2026-09-10, Status `NO-VERDICT`, Outcome `NO-VERDICT-BY-BASIS`) and replaced by **CRL-30 flow ≥7.50%**; the send-matrix row for it is struck through in place at **`CLAUDE.md:207`** and the KEY-THRESHOLDS row at **`:232`**, rather than deleted | conformant, and self-correcting |
| Predictions | `thesis/PREDICTIONS.tsv` (canonical) → `PREDICTIONS_MIRROR.md` (mirror, Check-A-enforced) | 30 IDs; resolved rows carry failure-mode notes; CRL-21/24 carry **literal position-action commitments** | exemplary |
| Cross-agent routing | `CLAUDE.md:200-223` send/receive matrices + `NEXUS_BRIEF.md` CROSS-DOMAIN + `outbox/` + `board/` | condition→target→priority; **⛔ SIGNALS → WALTER, ANALYSIS/PACKETS → direct** (`CLAUDE.md:101` boot step 12, and the FILES row `:269`, corrected 2026-09-02 off the DAEDALUS route-around census) | conformant |
| Sub-agent governance | `TEAM.md` + `SPAWN_PROTOCOL.md` + `sub_agents/*/inbox/` | **catalyst-driven, not calendar** (`TEAM.md:64` REFRESH RULES, rewritten 7/10): *"Staleness is a citation rule, not a spawn alarm"* (`:67`). Three lifecycle states: **standing** (STUE/DOC/GIG) · **dossier-mode** (POP/POLLY/PHAN) · **FROZEN** (META). **WQ-183 ② (Will 2026-09-07): the PARENT holds the pen on a sub-agent card** | **fleet-unique — no other desk has this layer** |

## §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows — PAT-088)

⚠️ **Scanner reality, 2026-09-17, and it changed mid-day.** Under the **committed** `falsification_scan.py`, CARL was reported in the prose bucket *"Thesis file is itself dead-bannered"* and emitted **zero** surface rows — a **false positive**: the committed `live_thesis()` tested `"STALE-VINTAGE" in head.upper()`, which matches the *prose* phrase "two stale-vintage recirculation traps" at `thesis/THESIS.md:2`, so a LIVE v2.6.6 thesis was graded dead. DAEDALUS fixed that the same day (banner-FORM regex + `.md` H1 no longer skipped as a comment). Under the **fixed** build the scan emits exactly **ONE** CARL row — `thesis/CHANGELOG.md`, class `changelog/pivot log`, verdict **CURRENT** (stamp 2026-09-16) — and CARL appears in no prose bucket at all.

**Both readings are bad and the second is worse.** A desk whose falsification loop is the fleet benchmark is now represented in the sweep by its **changelog**, graded CURRENT — a clean verdict on a surface that is not a rail. `thesis/THESIS.md` is consumed as the live-version *reference*, never enumerated; `KILL_RULE_RESPEC_2026-08-15.md` cannot match `SURFACE_PATTERNS`' `KILL[_A-Z0-9]*` because the hyphens in the date fall outside the character class. That is a DAEDALUS-lane defect in `SURFACE_PATTERNS` (`falsification_scan.py:38-43`), not a CARL gap. Inventory hand-derived:

| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `thesis/THESIS.md:395` "Exit / Invalidation Rules" | **FULL THESIS KILL** — leg 1 claims <220K × 8wk **AND** leg 2 CC transition-into-90+ falling 2 consecutive quarters with ≥100bp cumulative (`:398-399`) | `THESIS.md:2` `**Updated:** 2026-08-27` + the v2.6.6 clause | 🔢 "CURRENT STANDING: **0 OF 2**" written inline (`:410`); superseded text preserved verbatim at `:405-407`; **shadow grade (AS-WRITTEN vs RE-SPEC) recorded side-by-side on every card** (`:420`) |
| `thesis/THESIS.md:355` Fast Early-Warning Kill Mechanism | 1-month-cadence early-warning kill table | inherits THESIS header stamp | table rows |
| Per-vector downgrade triggers inside `THESIS.md:277` Convergence Score table | **single-vector partial invalidation** (V1 <12%×2, V3 <0.65%×2 [FIRED Jul 2, `:292`], V4 <9%, …). ⚠️ **V5's $4.00 AAA gate at `:294` is an UPGRADE gate, not a downgrade trigger** — *"still ≥$4.00 at Monday 8/3 close → EXECUTE 3→4; retrace <$4.00 first → hold 3"*, executed 2026-08-03 | per-row version + reason-for-change cells | vector score moves + a CHANGELOG entry + the STATUS mirror |
| `thesis/PREDICTIONS.tsv` `Invalidation` column (col 9) on all 30 CRL rows | per-prediction kill/re-arm | header line 1 two-clock `Last real data refresh: 2026-09-11` + a **cadence declaration** (line 2) declaring the ledger EVENT-driven | `Status` cell → CONFIRMED / MISSED / MIXED / RETIRED / **NO-VERDICT** + `Outcome` + `Notes` failure-mode prose |
| **CRL-20 / CRL-21** masking falsification windows (`THESIS.md:426-428`) | kills the **data-masking sub-thesis**; CRL-21 (Q3-2026 intermediate) carries a literal position action; CRL-20 (Q1-2027 outer) invalidates masking and validates CONTAINMENT | dated in-row | prediction Status + a THESIS version bump |
| `thesis/KILL_RULE_RESPEC_2026-08-15.md` (26,220 B) | the working that produced the v2.6.6 re-spec — base rates, the rejected drafts, the demonstration that a direction-only rule *would already have killed the thesis at 25:Q2* | filename + 8/27 body stamps | n/a (a derivation, not a live rail) |
| `thesis/HHDC_Q2_2026_GRADING_CARD.md` (28,817 B) + `HHDC_Q3_2026_GRADING_CARD_TEMPLATE.md` | the **executed** and **pre-registered** grading instruments for the kill's own instrument (NY Fed HHDC Page 14) | filenames carry the quarter | a completed card |
| `thesis/TRADEDOWN_INSTRUMENTS.md` (10,426 B) | **T1 trade-down disconfirmation battery** — August graded **3 of 3 AGAINST** (`STATUS.md:59`, mirrored at `:77`); "T1 only disconfirms"; DG Q2 IN-SAMPLE, first OOS ~Dec | in-file + STATUS row | STATUS cell ⚪ "hypothesis unsupported"; V8 held at 4 on other evidence |
| `handoff_RED/COUNTER_LOG.md` (30,513 B, last commit 2026-09-11) | the counter-evidence running log **staged for RED** | in-file dated entries | **CARL stages, RED grades** — CARL must not maintain it |
| `sub_agents/*/workbook/PREDICTIONS.tsv` (**DOC 10 · GIG 8 · POLLY 8 · POP 8 · PHAN 7**; STUE keeps none) | child-level falsification, in-scope of boot step 7b's due-scan since 7/10 | each file's own header | child `Status` cell; **resolution routes to the owning sub-agent's next spawn, never a CARL-side edit** |

## 4. Deviations from standard (+ why)

**Better than blueprint**
1. **The falsification loop is the fleet benchmark, and it got harder on itself this period.** v2.6.6 didn't loosen the kill, it *base-rated three candidate rules and picked the 5.4% one over the incumbent 25.0%* — then wrote the rejected draft's counterfactual kill (25:Q2) into the file. The mandatory shadow grade means the two counts now start one apart and a divergence **cannot be absorbed silently**. No other desk re-specs a kill against its own base rate and keeps the loser on the page.
2. **Three-mechanism discrimination held SEPARATE** (masking vs K-shape selection vs tariff transmission, `THESIS.md:100,:137,:171`) — the §"Why this section exists separately" is an explicit falsifiability argument.
3. **The Independence map** (`THESIS.md:319`) — 14 vectors, ~10 roots, co-rooted pairs named. A convergence score that tells you not to over-read it.
4. **KB `Delegated_To`** = 7-way fan-out ownership orthogonal to `Status` — richer than a single-desk KB.
5. **Agent-local mechanical checks that actually gate:** `consistency_check.py` at 60,338 B with Checks **A** (prediction mirror), **B** (convergence score across surfaces), **D** (every OPEN prediction must NAME its resolving series), **E** (cross-ledger threshold monotonicity **across parent AND sub-agent**), **F** (bias tripwire), **G** (registration-time failure-shape lint). Check **C** was evaluated and **declined with reasoning** (`scripts/CONSISTENCY_CHECK_SPEC.md:249`) — and the charter says so in the mirror-pair table (`CLAUDE.md:178`) rather than implying coverage.
6. **Two structural read-mode splits executed under Will direction, both with a guard:** ROADMAP→ROADMAP_THREADS (2026-09-05, generated index + `--check` gate) and the PREDICTIONS mirror out of STATUS (2026-09-01). CARL argued *why a split is safe here and was not safe for STUE* — it ruled against a hot/cold split on STUE's surface **because no coherence checker reaches a sub-agent, and CARL has one** (`ROADMAP.md:6`).

**Not a gap, do not flag**
- **`TRADE.md` RETIRED BY DESIGN.** CARL is the transmission *middle*; the L4 trade-feed criterion is met by cross-agent routing to REGINALD/HENRY/OZK/FORGE. Any mechanical "no TRADE.md ⇒ sub-L4" scan produces a false negative here (`CLAUDE.md:262`, TRADE.md's own banner).
- **`handoff_RED/` files at Apr–Jun vintage.** Staging surface; RED owns. Age is not rot.
- **`thesis/CHANGELOG.md` at 229 KB.** Append-only audit trail, explicitly SKIP-at-grade.
- **`CLAUDE.md` at 48,543 B.** `BLUEPRINTS/READ_CAP.md:38` rules charters OUT of the byte budget ("auto-loaded into context, not a Read… watch, don't rotate on this rule"). Watch-worthy (149% of budget in context cost) but **not a breach**.

**Live debt (verified at HEAD 2026-09-17)**
- (a) **`CLAUDE.md` asserts thesis `v2.5.1` in two places** (`:10`, `:272`) while canon is **v2.6.6** since 8/27.
- (b) **7 of 24 docket rows are past-dated** (8/29, 8/31 ×2, 9/10, 9/14, 9/15, 9/16) — the boot's own integrate-&-prune flag class.
- (c) **STUE's bounded-head read rule is self-contradictory and over the hard read cap** — the rule at `sub_agents/STUE/CLAUDE.md:246` names top→end-of-`## CATALYSTS` + `## ROUTED TO PARENT` + `## BOTTOM LINE`, which measures **80,967 B** (verified twice independently) against a 54,250 B hard cap; the whole file is 124,067 B = 381% of budget. **The single largest structural item on this desk.**
- (d) **17 sub-agent ledgers flagged STALE** by `ledger_staleness.py CARL` — **DOC 5 · GIG 6 · POLLY 5 · STUE 1**; parent ledgers 0 stale. `TEAM.md:3` (9/16) declares that no sub-agent was launched and no child ledger refreshed — the non-refresh is *declared*, the count is not.
- (e) **4 sub-agent inbox packets unprocessed**, two of them >30d (**DOC 37d**, **POP 33d**; STUE 7d, PHAN 6d) — and TEAM.md's own build spec says packet AGE is a finding. CARL's own top-level `inbox/` is drained (0).
- (f) **No literal `BOTTOM LINE` heading** in `STATUS.md` (`grep -i` → 0 hits); the function is served by `## Current judgment` (`STATUS.md:113`). Naming-only, not substance.
- ~~ABS_BASELINE LIVE-stale~~ ✅ **CLOSED** — FROZEN 2026-07-10 banner verified.
- ~~consistency_check.py IN BUILD~~ ✅ **CLOSED** — A/B/D/E/F/G shipped.
- ~~STATUS over 250 lines / over cap~~ ✅ **CLOSED** — 118 ln, 70% of budget, `read_cap_check --agent CARL` rc=0, 0 over budget.

## 5. Load-bearing context / DO NOT TOUCH

1. **K-shape methodology.** Every datum decomposed bottom-60 vs top-40; "aggregate improvement is NOT improvement if the bottom is still deteriorating." Public issuers (SYF/ALLY) carry survivorship bias. **Payment hierarchy Auto → Mortgage → Student → CC** (`CLAUDE.md:51`).
2. **The masking framework's 3-mechanism separation** and its deliberate **4-issuer** load-bearing scope (narrowed 6→4 on external review, `THESIS.md:102`). Collapsing them re-breaks falsifiability.
3. **The v2.6.6 kill spec is Will-ruled and instrument-pinned** (`THESIS.md:400`, verbatim): leg 2 reads **`HHD_C_Report_<QTR>.xlsx`, sheet `Page 14 Data`**, numeric only — **the report prose is chart-only for this series and must not be used**, and **"Never substitute Pg 28" (tracked Pg 14 within ±0.01pp for five quarters, then diverged +0.39pp in 26:Q2)**. Grade both quarters from **ONE vintage** (`:401`). **The AS-WRITTEN shadow grade is mandatory and the two counts start one apart.**
4. **⛔ 13.74% is DEAD.** CRL-05 closed 2026-09-10 (`NO-VERDICT-BY-BASIS`) — charged-off balances stay on bureau reports ~40%→80% at 1yr (`CLAUDE.md:232`), so a 2010:Q2 peak and a 2026 print are different measurements. **Never re-arm anything on 13.74%.** Successor is **CRL-30** (flow ≥7.50%).
5. **Bifurcated timing axis** (`THESIS.md:205-211`). Axis A (unsecured monoline, FFIEC-mandated charge-off, un-maskable) is the leading tell but **NEVER a proxy for Axis B** (CRE/regional, extend-and-pretend). A monoline-only break confirms A; it does not flip B.
6. **Frozen ledgers** — VX / FLOW / BNPL_STRESS / STATE_DIFFUSION / TRENDS (6/26) and **ABS_BASELINE (7/10)**: do not append. KB.tsv is the only live parent ledger.
7. **KB `Delegated_To` is orthogonal to `Status`** — never overload; a delegated row keeps its ACTIVE/CONFIRMED state.
8. **Mirror pairs, canonical wins:** THESIS matrix → STATUS matrix (Check B) · PREDICTIONS.tsv OPEN IDs → `PREDICTIONS_MIRROR.md` (Check A) · CATALYSTS.tsv → CALENDAR.md (**hand-verify only — Check C declined, `CLAUDE.md:178`; no script covers this pair**).
9. **`ROADMAP.md`'s index block is GENERATED.** Edit `ROADMAP_THREADS.md`, then `roadmap_index.py --rebuild`; `--check` is a closeout gate. **Hand-edits to the index are overwritten.**
10. **`board_log.tsv` must stay at the repo-relative path `AGENTS/CARL/board_log.tsv`.** `walter_doctor.py` reads it there with **no fallback** (`CLAUDE.md:73`); for ~3 months CARL's work sat one directory down and read to WALTER's telemetry as "keeps no board_log" (`board_log.tsv:3`). **Both ledgers are live and are not duplicates.**
11. **CARL is `BOARD_CONSUMPTION_SPEC` §3.5 pull-complete EXEMPT** (`AGENTS/WALTER/design/BOARD_CONSUMPTION_SPEC.md:116`) — WALTER does **not** deliver to `inbox/WALTER/`. An empty `inbox/WALTER/` is **not evidence of anything** for this desk; the INDEX scan (boot step 5) is the sole channel and it runs unconditionally inside `boot.py` via `board_gap.py`, fail-closed (rc=2 if it cannot read INDEX). ⚠️ §3.5.6 of that spec records the exemption's failure mode materialising on RED — the exemption removes the only artifact that would show the pull was skipped.
12. **Before any non-acting disposition** (`INFO_ONLY`/`NOTED`/`SKIPPED`) **grep the signal against the OPEN-prediction instrument list.** If it names or bears on a registered series the only legal dispositions are `acted` or `deferred` WITH A DATE. (KB-CARL-450: a resolvability hazard filed INFO_ONLY on 2026-08-15 sat **27 days** inside CARL's own note before CRL-10 was cut **62%→8%** on 2026-09-11 using that same argument.)
13. **⛔ Never pipe `boot.py` to `tail`/`head`.** It prints progressively with `flush=True` (`boot.py:214`); a piped slow run is indistinguishable from a dead one. Redirect to a file.
14. **`handoff_RED/` — CARL stages, RED owns. Do not maintain.**
15. **The PARENT holds the pen on a sub-agent card** (WQ-183 ②, ruled 2026-09-07), with riders: a card edit is a **dated ruling in the parent's tree**, plus the two-correction stop. A peer session's word does not move a child charter.
16. **META is FROZEN with an explicit do-not-spawn, and POP/PHAN are dossier-mode** — a packet placed in META's inbox has **no scheduled reader whatsoever** (`TEAM.md:25`). Route methodology to DAEDALUS or CARL.
17. **Cede lines:** HY OAS = LIQUID's series (counter-signal, never double-counted) · labor = LABOR · bank = REGINALD · oil spot = HAWK/BRENT · private-credit gate-count = BROCK · housing assets = HOMER.
18. **Boot-step numbers are not line numbers.** CARL's charter numbers its boot contract 0→16 with sub-steps (5b, 14b); a locator must cite the line. Map at HEAD: step 5b = `:73-74` · step 12 = `:101` · step 14b = `:110` · step 15 = `:111`.

## 6. Maturity snapshot

**Per `FLEET_MAP.tsv` CARL row at HEAD commit: L4 / conf H / last-scored 2026-09-01** (classification not restated here). Work queue → `AGENTS/DAEDALUS/upgrades/CARL_CARD.md`; sub-agent layer → `upgrades/CARL_SUBAGENT_AUDIT_2026-07-10.md`.

Section-level read at 2026-09-17: **exemplary** on Thesis / Convergence / Invalidation-exit / Predictions / Agent-local checks; **conformant** on Thresholds / Cross-agent routing; **fleet-unique** on sub-agent governance. Both L4 criteria are met (trade-feed via cross-agent routing; signals flowing via NEXUS_BRIEF + outbox + SIGNALS.md).

⚠️ **The committed row's three `Next_upgrade` legs are all discharged at HEAD** — the `boot.py` failure-marker whitelist was widened on 2026-09-01 at **21:51** (`052c36faf`) and casefolded at **22:05** (`dcfdb9037`), i.e. **23 minutes after the row was cut** (Production Review #5, `31e0b90d7`, 21:28:53); `FAILURE_MARKERS_CF` now carries `"ERROR"` at `boot.py:91-97`. PREDICTIONS carries a graded cadence declaration; PHAN hygiene clocks were bumped 9/10-9/11. **DAEDALUS has already begun encoding this: the working tree carries an uncommitted CARL row at last-scored 2026-09-17 with Gaps reading "L5 DENIAL REFUTED … All three prior Next_upgrade legs are discharged or re-homed."** The ladder's `zero YEYOU flags` leg is a **default-zero instrument that can never fire** (PAT-060 / WQ-181 ②, ruled N/A) — adjudicate L5 on the remaining legs only.

## 7. Open questions / comprehension gaps

- **Q1 — What is the live L5 verdict?** The row's three named blockers are cured. Is there a *new* blocker, or is CARL an L5 candidate at the 2026-09-19 sitting? **NOT-ADJUDICATED** from a reader/verifier seat.
- **Q2 — Who owns the STUE bounded-head fix?** WQ-183 ② says the parent holds the pen, and the defect is in `sub_agents/STUE/CLAUDE.md:246` (CARL's tree). The measurement that the head is **80,967 B** under the literal rule has now been made twice independently and agrees to the byte; CARL may still read the boundary differently. Needs CARL's own re-measure before the fix.
- **Q3 — Are the two dossier-mode inboxes (POP, PHAN) doing net harm?** TEAM.md names the risk and the READMEs disclose it, but there are live packets sitting in them (POP 33d). Is "an inbox with no scheduled reader, disclosed" the right design, or should dossier-mode packets route to the parent?
- **Q4 — CRL-06 metric ambiguity (FC filings vs starts basis).** `STATUS.md:33` says "CRL-06 closed CONFIRMED July16 on starts." Reads resolved at HEAD; the underlying grade was not verified against ATTOM. **CANNOT-EVALUATE.**
- **Q5 — Is the `docket/CATALYSTS.tsv` ↔ `CALENDAR.md` hand-verify pair actually being run?** Check C is declined by design, so the only evidence of a pass is a session saying so. No receipt found.
- **Q6 — The GIG ratification thread.** `sub_agents/GIG/RECONCILIATION_DRAFT_2026-07-10.md` still exists at HEAD alongside `GIG/STATUS.md` (refreshed 8/10). Whether the draft was ratified or superseded is not readable from the files. **CANNOT-EVALUATE** — needs CARL's word.

## 4b. 🔴 Findings the first reader missed — CARL

| # | Finding | Locator |
|---|---|---|
| **V-C1** | **The reader's flag D-1 was right, and fixing it makes CARL's sweep coverage *worse*, not better.** Pre-fix: false-positive dead-banner, zero rows. Post-fix: **one** row, `thesis/CHANGELOG.md`, verdict **CURRENT** — a clean bill issued on a changelog, while the actual rails (the `:395` exit block, the v2.6.6 instrument pin, the 30-row `Invalidation` column, the grading cards) stay invisible. The cure moved CARL from *loudly mis-bucketed* to *quietly certified*. `KILL_RULE_RESPEC_2026-08-15.md` cannot match `KILL[_A-Z0-9]*` — the hyphens in the date fall outside the character class. **Recommend a D-1b follow-up on `SURFACE_PATTERNS` before this sweep is cited as coverage for CARL.** | `falsification_scan.py:38-43`; `--agent CARL --tsv` (fixed build) |
| **V-C2** | **The draft's own two halves disagree on PHAN's prediction count** — PART A §3b says 45, PART B §B1 says "PHAN 7 predictions re-marked 9/10". The artifact says **7** (`PHAN-P01..P07`). A line count was read as a row count on a file that is 46 lines of which ~38 are comment prose. | `AGENTS/CARL/sub_agents/PHAN/workbook/PREDICTIONS.tsv` |
| **V-C3** | **Six locators in the draft are CARL boot-STEP numbers presented as line numbers** (`CLAUDE.md:5b`, `:12`, `:14b`, `:15`). CARL is the one desk in the fleet where this is systematically ambiguous because its boot contract runs 0→16 with lettered sub-steps. Any downstream consumer following `CLAUDE.md:12` lands on the K-shape sentence. | `CLAUDE.md:73-74 / :101 / :110 / :111` are the true lines |

---
---

# DESK 2 — LIQUID

## 1. Verification table — LIQUID PART A

| § | Claim (≤20 words) | Verdict | Correction / evidence |
|---|---|---|---|
| Hdr | Sources: CLAUDE.md 227 ln / 31,873 B · STATUS 124 ln / 34,662 B · MEMORY 306 ln / 64,873 B | VERIFIED | all three exact |
| Hdr | "all 19 `workbook/` files" · "all 7 `scripts/`" | VERIFIED | `ls` = 19 workbook entries; 7 `.py` in `scripts/` |
| Hdr | `registry/corrections_receipts.tsv` (4 rows) | VERIFIED | 5 lines = header + 4 receipts |
| Hdr | `read_cap_check --agent LIQUID` rc=1 | VERIFIED | rc=1, `🟠 STATUS.md 34,662 B 106% of budget`, 0 over cap |
| Hdr | `corrections_boot_check.py LIQUID` rc=1 | VERIFIED | `CORRECTIONS-CHECK 1 BLOCK: COR-20260915-02 [LIVE] 2026-09-15` unreceipted |
| Hdr | `boot.py --selftest` PASS | VERIFIED | ran it: `CATALYSTS.tsv OK (26 rows, 8 cols)` · `PREDICTIONS.tsv OK` · `KB.tsv OK (125 rows, 13 cols)` · `SELFTEST: PASS`, rc=0 |
| Hdr | live `fetch.py fred BAMLH0A0HYM2` | VERIFIED | HY OAS **2.76 (2026-09-15)** = 276bp; 0 prints <260 |
| Hdr | Staleness ①: `THESIS.md:1` version ≠ `v2.0` | VERIFIED | `# LIQUID — Core Thesis v2.0` |
| Hdr | Staleness ②: `## Drill log` at `KILL_MEMO…:229` row count ≠ 1 | VERIFIED | heading at `:229`; **1** data row (2026-07-01) |
| Hdr | Staleness ③: 5 `owner==LIQUID` GATES rows, states as listed | VERIFIED | HY-REKILL `LIVE — 0 of 2` · 069 `LIVE — ARMED 1-of-2` · 072 `LIVE` · 076 `LIVE — 0-of-3` · 079 `LIVE / NOT ARMED` |
| Hdr | Staleness ④: `read_cap_check --agent LIQUID` returns rc=0 | VERIFIED | currently rc=1 — the clause is live and evaluable |
| Hdr | Staleness ⑤: >30d, checkpoint 2026-10-17 | VERIFIED | 2026-09-17 +30d = 2026-10-17 |
| §1 | Class Market; `{BOND,ZHAO} ↔ MIDAS → LIQUID → HENRY`; no book by design | VERIFIED | FLEET_MAP col 2 = Market |
| §1 | Owns list at `CLAUDE.md:99-115`; cedes at `:116-124` | VERIFIED | `:99` "**You own:**"; `:116` "**You do NOT own:**" |
| §1 | X1 is conjunctive; two-sided KILL_MEMO ladder; GATE-LIQ-079 separate root | VERIFIED | `KILL_MEMO…:45,:64`; `FUNDING_SEIZURE_GATE_SCOPED.md` R1 |
| §1 | PAT-013 (channel-kill ≠ thesis-kill + migration theorem) | VERIFIED | `AGENTS/DAEDALUS/PATTERNS.tsv:15` verbatim |
| §1 | "the period's self-authored commit subjects are literally [3 quotes]" | DRIFTED | 2 of 3 are in period, both **2026-09-02**. *"I published a scary number measured off its own peak"* is **2026-08-23** — outside the 2026-09-01→now window |
| §1 | Drill log still n=1 | VERIFIED | 1 data row |
| §2 | `CLAUDE.md` anchors `:18-36` spawn · `:37-65` inbox/outbox · `:97` scope · `:126` signals · `:152` thresholds · `:156-166` state-flip · `:167` basis canon · `:185` dashboard · `:196` FILES | VERIFIED | all nine exact |
| §2 | retired-and-repointed private-credit-gate row at `:72-74` | DRIFTED | the block opens at **`:69`** ("CLOSED 2026-09-12. The row is RETIRED AND REPOINTED"); BROCK's 9/9 ruling is `:74` → **:69-74** |
| §2 | STATUS anchors `:4` BOTTOM LINE · `:23` Current State · `:27` LIVE STATE · `:57` Triggers · `:79` Calendar · `:85` Playbooks · `:101` Open Monitors · `:120` Durable Signals | VERIFIED | all eight exact |
| §2 | STATUS = 106% of budget, the desk's only over-budget boot read | VERIFIED | 34,662/32,550 = 106.5%; the other boot read (`workbook/PREDICTIONS.tsv`) is 28% |
| §2 | THESIS 21,443 B; v2.0, 2026-06-25, Conviction 61%; §3 `:31` §5 `:56` §7 `:85` | VERIFIED | `:1` v2.0; `:3` `Last Updated: 2026-06-25 \| Conviction: 61%`; all three §-anchors exact |
| §2 | CHANGELOG 32,978 B; TWO-STATED 2026-08-28; 8-row revision table; named v3.0 trigger | VERIFIED | `:3` banner verbatim; `:5` rewrite trigger; `:7` table header; **8** data rows |
| §2 | TIMELINE 9,681 B, 7/06, 8 decision windows | VERIFIED (size/date) | branch count NOT re-walked — self-declared |
| §2 | KB.tsv 125 rows, max KB-LIQ-125, 267,966 B | VERIFIED | exact; 13 cols |
| §2 | KILL_MEMO 36,259 B / 233 ln; `:7` STATE AS-OF 2026-08-23; `:45` canonical letter WQ-162 Will 2026-09-02 21:29 ET; `:93` Trigger B retired WQ-106; `:229` drill log n=1 | VERIFIED | all five exact and verbatim |
| §2 | FUNDING_SEIZURE 18,548 B, BROCK riders R1–R4 2026-07-20 | VERIFIED | exact |
| §2 | DEALER_POSITIONING 34,770 B, 2-of-3 rule, "as-of 8/18" | VERIFIED | exact; largest workbook `.md` |
| §2 | EXPECTED_SIGNALS 10,319 B; `:2` Born 2026-07-11; `:21` ★ REVIEW 2026-08-24; `:57` Resolved log first row | VERIFIED | all verbatim, incl. *"Two bands and two SOURCES were wrong; one nearly produced a false 🔴"* |
| §2 | ORCL 8,237 B; `:3` "CHECKED 2026-08-24 … NO CHANGE" (24d) | VERIFIED | verbatim |
| §2 | Pre-registration cluster: Tests B/C CLOSED, Test A v1 UNGRADEABLE-UNDERPOWERED (WQ-113), dry-run grades nothing, Hormuz graded neither path | VERIFIED | `STATUS.md:96`; `T3_..._DRYRUN.md:69`; `CHANGELOG.md:16` |
| §2 | CATALYSTS 26 rows / 8 cols incl. `date_class`; PREDICTIONS LIQ-01..06; FLOW/VX FROZEN 2026-07-11 | VERIFIED | all exact |
| §2 | `LIQ-04_KERNEL_NATIVE_COMPANION.json` + `kernel_staging/` (4 CMD JSONs + README) | VERIFIED | exactly 4 CMD + README |
| §2 | boot.py 36,748 B; 3-dashboard sweep; `watcher_echo()`; exit code = FETCH health only | VERIFIED | `boot.py:24` "Exit code = FETCH health only… NOT alert state"; `def watcher_echo()` at `:539` |
| §2 | `sofr_dispersion.py` drift-robust successor, `--baserate` re-prints realised fire rates | VERIFIED | `:36,:84,:205,:212` |
| §2 | `fp_backtest_079.py` "**pinned** calibration artifact" | UNLOCATED | nothing in `AGENTS/LIQUID/` names it pinned or do-not-touch — the script header (`:1-14`) carries no such banner. The designation is DAEDALUS's own, at **`profiles/LIQUID.md:34`**. Kept below, re-attributed, and raised as an owner ask |
| §2 | MEMORY 64,873 B / 306 ln; `### NEXT SESSION` at `:283` | VERIFIED | exact |
| §2 | NEXUS_BRIEF 20,328 B (banner history `:9`) · CALENDAR 32,060 B · CLOSEOUT 11,476 B · CREDIT_THRESHOLDS HISTORICAL · CATCHUP_PUNCHLIST FROZEN 7/10 | VERIFIED | CREDIT_THRESHOLDS `:2` `Date: 2026-02-28 \| Status: HISTORICAL`; punchlist `:3` `FROZEN 2026-07-10` |
| §2 | `board_log.tsv` 167,390 B / 264 ln | VERIFIED | exact |
| §2 | archive 53 · domain/sources 26 · outbox 25 · reports 2 (7/11) · research 1 (7/11) · analysis 1 | VERIFIED | `git ls-files` counts; `git log -1 --format=%cs` = 2026-07-11 on both |
| §2 | `analysis/2026-07-30_hy-attribution.md` 17,782 B is load-bearing | VERIFIED | exact |
| §3 | Migration theorem at `THESIS.md:98`, used live 7/30 | VERIFIED (concept) | `:98` = *"Channel-kill vs full-thesis-kill is the key distinction."* The phrase "migration theorem" is DAEDALUS's label (PATTERNS.tsv:15), not LIQUID's wording |
| §3 | No 5-pt overlay; conviction % on `THESIS.md:3`; DORMANT→ARMED→TAGGED→TRIGGERED | VERIFIED | `:3` `Conviction: 61%` |
| §3 | Invalidation: `THESIS.md:85` §7 · KILL_MEMO letter · `STRATEGY.md:29` · 5 GATES rows · pre-reg layer; H-2 counting rule | VERIFIED | `KILL_MEMO…:26` H-2 header; `STRATEGY.md:29` exists |
| §3 | Basis canon: FRED H.15 · raw unadjusted closes · accepted basis · ICE front-month settle · 5pm ET NY close · H.4.1 as-of Wednesday · Rule Zero on TIC | VERIFIED | `CLAUDE.md:167` verbatim |
| §3 | Predictions LIQ-01 ACHIEVED · 02 MISS · 03 ACHIEVED (reversed) · 04 OPEN · 05 VOID · 06 ACHIEVED | VERIFIED | col 6 exact |
| §3 | Gates: every owned row carries a `review_by`; 069 graded 9/12 three days early; successor set by PROME on LIQUID's recommendation | VERIFIED | `review_by` was 2026-09-15 → graded 9/12 = **3 days**; `review_by` cell states PROME set 2026-10-15 and LIQUID "explicitly declined" to self-set |
| §3 | Routing corrected 2026-09-03; `CLOSEOUT.md:95` and `:96` contradict | VERIFIED | `:95` "self-commit it (carve-out ①)" vs `:96` "Do NOT commit files outside `AGENTS/LIQUID/`" — a real live contradiction |
| §3 | Watcher: systemd `liquid-hy-watch.timer` Mon–Fri 13:00 ET; `alerts/watch.log` last line 2026-09-16 276bps 🟡 obs 2026-09-15; delivery leg built 2026-08-27 (`d0126416e`) | VERIFIED | timer at `hy_oas_watch.py:12`; log line verbatim; commit `d0126416e` 2026-08-27 |
| §3 | Delivery writes to `PROME/inbox/` + appends `AGENTS/SIGNALS.md`, never raises, discloses machine-authorship | VERIFIED | `PROME_INBOX = WORKSPACE/"PROME"/"inbox"  # repo ROOT, not AGENTS/PROME/` at `:179`; SIGNALS `:180`; disclosure text verbatim at `:211-212` |
| §3b | "`falsification_scan.py` sees exactly **ONE** LIQUID surface" | OVERTAKEN | Under the **fixed** working-tree build it sees **TWO**: `workbook/KILL_MEMO_HY_OAS_260.md` **STALE-FLAGGED** 25d ✓ (the draft's figure, exact), **and** `thesis/CHANGELOG.md` **CURRENT** (stamp 2026-08-28, 20d, CitedVer v2.0). The `.md`-H1 half of the same-day fix changes which header lines are read, so the second row is plausibly post-fix; the STALE-FLAGGED row is unaffected either way |
| §3b | Other rails invisible because they miss `SURFACE_PATTERNS` (`:38-43`) | VERIFIED | exact |
| §3b | THESIS `:3` `Last Updated: 2026-06-25` — 84d | VERIFIED | 2026-06-25 → 2026-09-17 = 84d |
| §3b | GATE-HY-REKILL letter: strictly <260.0 bp, TWO consecutive published obs, as-first-published, terminal | VERIFIED | `KILL_MEMO…:45` block |
| §3b | 079 spec `:2` Registered 2026-07-17, BROCK sign-off 2026-07-20 | VERIFIED | exact |
| §3b | HY_HORMUZ `:2` Registered 2026-07-17, KB-LIQ-081; graded neither path (KB-LIQ-101) | VERIFIED | `CHANGELOG.md:16` |
| §3b | DEMAND_HOLE Built 2026-07-06 · BDC Built 2026-04-16, light-populated 6/12, card 7/18, window past and ungraded | VERIFIED | `BDC…:4` verbatim |
| §3b | `archive/CONSUMER_CREDIT_MONOLINES_PREREG_GRADED_2026-08-24.md` | VERIFIED | file present |
| §4 | 1 two-sided falsification on one series | VERIFIED | `KILL_MEMO…:64-99` |
| §4 | 2 pre-registration defects recorded as defects | VERIFIED | `STATUS.md:96`; `CHANGELOG.md:16` |
| §4 | 3 "`SOFR75−IORB ≥0` killed DEAD-LOUD after the **median day** cleared it (**59.9% of non-Q-end sessions, n=615**)" | **FAILED** | **59.9% is a RETRACTED figure.** `MEMORY.md:20`: *"Published a SOFR-dispersion base rate (59.9%) computed over a window **I truncated myself with a `limit=900` fetch arg**. True full-window figure **30.7%**."* And `MEMORY.md:25` states the band is dead **"by DRIFT, not construction"** — *"cleared by the median day; satisfied 27 consecutive sessions"*. **`n=615` is UNLOCATED** — it appears nowhere in `AGENTS/LIQUID/` |
| §4 | 3 successor's first drift flag re-cut after firing on 60.8% of sessions | VERIFIED | `sofr_dispersion.py:92,:205` |
| §4 | 3 "Four registered bands died in six days, three of them dead-loud" | VERIFIED | `thesis/CHANGELOG.md:19` verbatim (ES-LIQ-04 UST-fails · TIC_FRAMEWORK line · SOFR75−IORB · GATE-LIQ-076 cumulative leg) |
| §4 | 4 `fp_backtest_079.py` named as do-not-touch | UNLOCATED | see §2 row — no LIQUID-side banner exists |
| §4 | 5 watcher delivery leg at `hy_oas_watch.py:179-227` | VERIFIED | constants `:179-180`, `_deliver` `:183-227` |
| §4 | 6 "NO LIVE LEVELS IN THIS FILE" adopted `CALENDAR.md:17` (2026-08-20) | VERIFIED | verbatim |
| §4 | 7 `CATCHUP_PUNCHLIST` 🔴 CORRECTED 2026-08-24 quote; `NEXUS_BRIEF.md:9` banner history | VERIFIED | both verbatim (`CATCHUP_PUNCHLIST.md:5`) |
| §4 | `alerts/` gitignored by design | VERIFIED | `AGENTS/LIQUID/.gitignore`: *"# P1b HY OAS watcher runtime state — regenerated each run, never commit"* / `alerts/` |
| §4 | debt (a) THESIS still v2.0 / 61%; 5 of 8 revision rows are leg-level | VERIFIED | `:1`,`:3`; rows 3,4,5,6,8 of the 8-row table are leg-level |
| §4 | debt (b) STATUS 106% | VERIFIED | rc=1 |
| §4 | debt (c) MEMORY session log stops 2026-09-03; NEXT SESSION re-cut 2026-08-27 | VERIFIED | `:283` block |
| §4 | debt (d) `IDENTITY.md:18` live-sounding level from 6/24 | VERIFIED | *"HY OAS **276** (6/24), cushion above the 260 KILL 16bps"* — reads current, is 85d old |
| §4 | debt (e) `STRATEGY.md:29` kill count disagrees with the ruled letter | VERIFIED | `:29` says "<260 **sustained ≥3 sessions**"; the WQ-162 letter says **TWO consecutive published observations** |
| §4 | debt (f) 18 of 26 CATALYSTS rows past-dated | VERIFIED | exact |
| §4 | debt (g) no two-clock header on any LIQUID `.tsv`; no `workbook/LEDGER_GLOB`; scanner sees 5 TSVs, none of the 13 `.md` rails | VERIFIED | `LEDGER_GLOB` absent; `ledger_staleness.py LIQUID` = "5 ledger(s) scanned"; 13 `.md` in `workbook/` |
| §5 | 1 KILL_MEMO filename LOCK; it is the GATES `definition_surface` | VERIFIED | GATES cell = `AGENTS/LIQUID/workbook/KILL_MEMO_HY_OAS_260.md` |
| §5 | 2 WQ-162 letter, Will 2026-09-02 21:29 ET, folded 9/03 | VERIFIED | `KILL_MEMO…:45` verbatim |
| §5 | 4 H-2 counting rule Will-ruled 2026-08-10 | VERIFIED | `KILL_MEMO…:26` |
| §5 | 5 X1 conjunctive; BROCK adjudicated NOT ARMED 2026-08-28 (KB-BRK-219, `17d87df22`) | VERIFIED | commit `17d87df22` = BROCK 2026-08-28; `STATUS.md:105` records KB-BRK-219 |
| §5 | 7 private-credit gate RETIRED-AND-REPOINTED 2026-09-12; instrument is BROCK's `GATE-BRK-R2` | VERIFIED | `CLAUDE.md:69`; GATES `GATE-BRK-R2` owner BROCK, definition_surface `AGENTS/BROCK/workbook/PC_REDEMPTION_REGISTER.tsv (header + gate_status column)` |
| §5 | 8 Belgium inference FALSIFIED: rho ≈ +0.05, n=41; bought in 56% of China-selling months; reinstate at rho < −0.5 rolling-24m | VERIFIED | `TIC_FRAMEWORK.md:40` `+0.050`, `:45` "15 (56%)" of 27, `:48` reinstatement band, `:49` >$500B survives as a bare level |
| §5 | 10 GATE-079 FP cites in denominator form only (5-of-8 → 2-of-8, n=1 TP) | VERIFIED | `MEMORY.md:111,:113` verbatim, incl. *"never a bare '62%', adopted 7/30 per BROCK's flag"* |
| §5 | 12 `ofr_stfm.py` lives in DEWEY's tree | VERIFIED | `AGENTS/DEWEY/scripts/ofr_stfm.py` |
| §5 | 13 `config.py` imported never forked; boot.py exit = FETCH health only | VERIFIED | `from config import classify, get_agent` at `hy_oas_watch.py:108`; the file is **`FORGE/tools/market-data/config.py`** — there is no `config.py` in LIQUID's tree. `boot.py:24` |
| §5 | 16 FLOW/VX FROZEN 2026-07-11; CREDIT_THRESHOLDS HISTORICAL; PUNCHLIST FROZEN 7/10 | VERIFIED | all three banners |
| §5 | 17 quoted *"THE LEVEL FIRED ON A MECHANISM THE LADDER WAS NOT BUILT FOR"* at `THESIS.md:98` | **FAILED** | that sentence appears **nowhere** in `AGENTS/LIQUID/`. `:98` reads *"Channel-kill vs full-thesis-kill is the key distinction."* The 7/30 attribution it cites IS real: **68–84% broad DM HY beta · 15–30% AI/data-center · ~0% bank/CRE, HIGH conf** (`CLAUDE.md:163`, `analysis/2026-07-30_hy-attribution.md`) |
| §6 | "FLEET_MAP LIQUID row: L4 / conf H / last-scored **2026-09-01**" + the quoted `Next_upgrade` + "Gaps 'Dark since 8/28' is REFUTED" | **OVERTAKEN** | Correct at `b824b5a13`. **`7bfee0060` (PR#6 map re-cut, 2026-09-17 09:53 ET, 22 min after the reader's read)** moved the row to **last-scored 2026-09-17** with a new 4-leg `Next_upgrade`; "Dark since 8/28" is gone. The refutation was right and is already actioned — **31** LIQUID-authored commits after 8/28, last 2026-09-12 |
| §7 | Q1–Q6 carried as NOT-ADJUDICATED / CANNOT-EVALUATE | VERIFIED | self-declared, correctly; `hy_oas_watch.py` has no de-escalation branch |

## 2. Totals — LIQUID

| Verdict | N |
|---|---:|
| VERIFIED | 58 |
| DRIFTED | 3 |
| FAILED | 2 |
| UNLOCATED | 2 |
| OVERTAKEN | 2 |
| **Graded** | **67** |

**The two FAILED:** ① the `59.9% / n=615` SOFR base rate (a figure LIQUID itself retracted — true full-window **30.7%**, `MEMORY.md:20`) · ② the quoted migration-theorem sentence at `THESIS.md:98` (not in the tree).
**The two UNLOCATED** are one claim in two places: `fp_backtest_079.py` as "pinned / named do-not-touch" — the designation exists only in DAEDALUS's own prior profile.

## 3. CORRECTED PART A — LIQUID *(install-ready)*

> Note the format change: the 2026-08-07 file is a free-form rewrite with no template section numbering and **no §3b** heading; this restores template order.

---

# Agent Profile — LIQUID

**Profile vintage:** 2026-09-17 (Mode-A: reader draft P2 + independent locator verification; installed by DAEDALUS)

**Built by:** DAEDALUS · **Date:** 2026-09-17 · **Comprehension method:** Mode-A — 1-reader full re-read (fan-out slot P2) + an independent adversarial locator verification pass (slot P2-VERIFY); read-only, artifact-verified; live FRED pull for the level claims.
**Sources read:** `AGENTS/LIQUID/CLAUDE.md` (227 ln / 31,873 B), `STATUS.md` (124 ln / 34,662 B), `MEMORY.md` (306 ln / 64,873 B), `NEXUS_BRIEF.md`, `CALENDAR.md`, `CLOSEOUT.md`, `IDENTITY.md`, `STRATEGY.md`, `USER.md`, `CREDIT_THRESHOLDS.md`, `CATCHUP_PUNCHLIST.md`, `LAST_COMPLETION.md`, `thesis/{THESIS.md, CHANGELOG.md, TIMELINE.md}`, all 19 `workbook/` files, all 7 `scripts/`, `registry/corrections_receipts.tsv`, `kernel_staging/`, `reports/`, `research/`, `analysis/`, `inbox/` + `inbox/WALTER/` listings, `alerts/` runtime (gitignored), plus `PROME/GATES.tsv` (5 LIQUID-owned rows + GATE-BRK-R2), and tool runs `read_cap_check.py --agent LIQUID` (rc=1), `ledger_staleness.py LIQUID` (0 stale, 5 scanned), `corrections_boot_check.py LIQUID` (rc=1), `AGENTS/LIQUID/scripts/boot.py --selftest` (PASS), `falsification_scan.py` (whole + `--agent LIQUID --tsv`), and a live `fetch.py fred BAMLH0A0HYM2` (276bp, obs 2026-09-15).
**Staleness (file-readable — all five clauses machine-evaluable; run 2026-09-17, all five at their stated values):** refresh when **ANY** of —
1. the version token on `AGENTS/LIQUID/thesis/THESIS.md:1` ≠ `v2.0`; **or**
2. the `## Drill log` table at `workbook/KILL_MEMO_HY_OAS_260.md:229` holds a row count ≠ **1**; **or**
3. any row in `PROME/GATES.tsv` with `owner == LIQUID` changes its `state` cell (currently: HY-REKILL *LIVE 0-of-2* · 069 *LIVE — ARMED 1-of-2* · 072 *LIVE* · 076 *LIVE 0-of-3* · 079 *LIVE / NOT ARMED*); **or**
4. `python3 scripts/read_cap_check.py --agent LIQUID` returns **rc=0** (i.e. the `STATUS.md` budget breach is cured); **or**
5. **> 30 days** (the desk's declared window) — hard checkpoint **2026-10-17**.

> Durable understanding — section-tasks read THIS, not the raw agent. Re-read the actual file before applying any change (PAT-009).

---

## 1. Identity

Financial plumbing + the credit axis. **Class:** Market (`FLEET_MAP.tsv` LIQUID row col 2) — **the amplification node**, `{BOND, ZHAO} ↔ MIDAS → LIQUID → HENRY`; **no book by design**. **Spawnable by:** PROME / Will.

**Owns** (`CLAUDE.md:99-115`): repo markets (SOFR/SRF/RRP/dealer positioning) · credit spreads (HY/IG OAS, CLO tranches) · **HY breadth / spread dispersion as its own named lane** (WALTER ROUTING_TABLE v0.27, Will-authorized 2026-08-18 — *"breadth is what the level cannot see,"* since RED-FT-01/-02 both key on the HY **level**) · Treasury auctions · foreign official flows (TIC / Belgium **bare level**) · basis-trade leverage · Fed balance sheet · private-credit→public transmission · war-risk/shipping insurance. **Mandate extension (Will-approved 6/27, integrated 7/1):** funding-market microstructure (dealer capacity, GC-vs-special, SOFR dispersion, MMF flows, PB constraints) · IG OAS + HY−IG basis · Eurozone credit as a USD-funding contagion vector.

**Cedes** (`CLAUDE.md:116-124`): individual banks → REGINALD · AI-capex/semis **fundamentals** → VULCAN (LIQUID keeps the AI-credit **spread tells**; seam registered 2026-07-12) · BDC/private-credit fundamentals → BROCK · Japan/BOJ → SAM · equity market structure → HENRY · oil/geopolitical → HAWK · rates/bund/ECB → BOND.

**Outputs:** the **X1 conjunction** (HY>280 sustained **AND** BROCK's wrapper-leads half — *conjunctive; no HY level alone can make this "X1 MET"*) · the **two-sided KILL_MEMO ladder** (kill <260 / confirm >280 / confirmation >320) · the **funding-seizure scoped gate** GATE-LIQ-079 (a separate root, never "X1 MET") · and four more registry gates. **Durable fleet contribution:** PAT-013 (channel-kill ≠ thesis-kill + the migration theorem — DAEDALUS's label for `THESIS.md:98`).

**Characteristic strength:** grades itself against its own instruments and loses honestly — in-period self-authored commit subjects include *"I misapplied my own delta rule within an hour of writing it"* and *"4 of 5 gates unpinned"* (both 2026-09-02); the same habit produced *"I published a scary number measured off its own peak"* on 2026-08-23. **Characteristic failure (unchanged, and now measurable):** the record of a fired event lives in prose no boot-independent process reads — the drill log is still **n=1**.

## 2. File anatomy (where the richness lives)

| File | Holds | Richness? |
|---|---|---|
| `CLAUDE.md` (227 ln / 31,873 B) | charter. **SPAWN PROTOCOL 0→6** (`:18-36`) with the read→board-intake→execute→write-back ordering rule and a **live-event override** · inbox/outbox protocols (`:37-65`, the routing correction at `:64-65`) · the **retired-and-repointed private-credit-gate row** with BROCK's 2026-09-09 ruling folded in verbatim (`:69-74`) · DOMAIN SCOPE (`:97`) · CROSS-AGENT SIGNALS (`:126`) · **KEY THRESHOLDS** (`:152`) — a 2026-07-01 snapshot table **explicitly self-labelled STALE**, preceded by a re-stamped state-flip list (`:156-166`) and the **basis canon** (`:167`) · DASHBOARD STRUCTURE (`:185`) · FILES (`:196`) | charter — **the basis canon at `:167` is the single most reusable paragraph on this desk** |
| `STATUS.md` (124 ln / **34,662 B = 106% of budget**) | `## BOTTOM LINE` (`:4`) — a long, dated, observation-stamped block, rotated verbatim to `archive/status_snapshots/` · `## Current State` (`:23`) + `### LIVE STATE` (`:27`) · **`## Triggers & Thresholds`** (`:57`, durable reference, live levels delegated to boot.py) · `## Catalyst Calendar` (`:79`, pointers only — the human mirror table was **rotated out 9/2 as a third copy**) · **`## Active Playbooks / Monitors`** (`:85`, the index of the falsification layer) · `## Open Monitors` (`:101`) · `## Durable Signals Log → KB.tsv` (`:120`) | live state — **and the desk's only over-budget boot read** |
| `thesis/THESIS.md` (21,443 B) | **v2.0 (`:1`), Last Updated 2026-06-25, Conviction 61% (`:3`) — 84d.** §1 Core Frame · §2 What LIQUID Actively Owns · **§3 Three Structural Failure Legs (A Fed-control / B foreign-bid / C basis-leverage)** (`:31`) · §4 Transmission Channel Map · §5 Bilateral Credit Framework (`:56`) · §6 Stagflation Trap · **§7 Kill Conditions** (`:85`) · **channel-kill vs full-thesis-kill** (`:98`) · §8 Cross-Agent Interface Table · §9 Epistemic Notes · Open Questions (as of 6/25) | durable frame — **architecturally sound and 84 days unversioned; see §4 (a)** |
| `thesis/CHANGELOG.md` (32,978 B) | **⚠️ TWO-STATED 2026-08-28** (`:3`, DAEDALUS sweep #2 ASK 1): *"This file is NO LONGER how this desk records thesis change, and pretending otherwise is the defect."* Pivots now live as dated `KB-LIQ-NNN` rows. Carries a **"Running revision log since v2.0 — pointers, not a version history"** table (`:7`, **8 data rows**) and a **named rewrite trigger** (`:5`): a v3.0 is authored the next time a *structural leg* is added, retired or inverted — not for a level move, band recut or gate grade; nearest candidate named as the **tail-recognition leg (KB-LIQ-101)**. ⚠️ **This is one of only two LIQUID surfaces `falsification_scan` can see** (CURRENT, stamp 2026-08-28) | **the 8/23–8/28 rework lives HERE, not in THESIS.md** — this table is the substitute for a version bump |
| `thesis/TIMELINE.md` (9,681 B, 7/06) | forward-only Active Branch Points (8 decision windows) | aging (73d); branches not re-walked this pass |
| `workbook/KB.tsv` (**125 rows, max KB-LIQ-125**, 13 cols, 267,966 B) | the durable-findings track and, since 8/28, **the de-facto thesis pivot log** | permanent record — the real brain |
| `workbook/KILL_MEMO_HY_OAS_260.md` (36,259 B, 233 ln) | the two-sided ladder. Header state block (`:7`, "STATE AS-OF 2026-08-23") · **H-2 same-kill counting rule (`:26`)** · **★ GATE-HY-REKILL — THE CANONICAL LETTER** (`:45`, WQ-162 Will-ruled 2026-09-02 21:29 ET, folded 9/03; **this file is the registry's `definition_surface`**) with 5 grader's conventions incl. `UNGRADEABLE-PENDING-PUBLICATION` and post-fire TERMINAL · trigger ladder (`:64`) · Trigger B RETIRED as a kill (`:93`, WQ-106) · tape-vs-substance guard (`:123`) · **`## Drill log` (`:229`) — n=1, the 2026-07-01 row** | **the fleet's best-written trigger ladder — with an empty fire history**, and the one surface the sweep flags (STALE 25d) |
| `workbook/FUNDING_SEIZURE_GATE_SCOPED.md` (18,548 B) | GATE-LIQ-079 spec (`:2` Registered 2026-07-17), **signed off with riders R1–R4 by BROCK 2026-07-20**; DEWEY calibration input | live rail |
| `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` (34,770 B) | GATE-LIQ-076's 3-leg amplification conjunction (SOFR-short / dealer warehouse / MOVE), 2-of-3 fire rule; "as-of 8/18" | live rail — **largest workbook .md** |
| `workbook/EXPECTED_SIGNALS_TRACKER.md` (10,319 B) | absence-is-data ES-LIQ-01..05 (`:2` Born 2026-07-11). **`## ★ REVIEW 2026-08-24`** (`:21`) — "two bands and two SOURCES were wrong; one nearly produced a false 🔴"; ES-LIQ-04 band **re-derived**; **`## Resolved / fired log` (`:57`) carries its FIRST row** — ES-02/03/04 cluster, 2026-08-24, 🟢 `DID_NOT_APPEAR`, episode *"HY 7/23→8/03 excursion to 287bps"* | live rail — **the old profile's "empty through the qualifying episode" is CLOSED** |
| `workbook/ORCL_FALLEN_ANGEL_MAP.md` (8,237 B) | GATE-LIQ-069 leg-5 sharpener; cross-agency ladder; **"⚠️ CHECKED 2026-08-24 … NO CHANGE"** (`:3`) | live rail, 24d stamp |
| `workbook/{DECOUPLING_TESTS_VIX_HY_2026-08-10, T3_DECOUPLING_TEST_A_DRYRUN, HY_HORMUZ_LAGGING_TELL_WATCH, DEMAND_HOLE_AUCTION_PREREG_2026-07, BDC_MARK_CONVERGENCE_MONITOR}.md` | the pre-registration layer: forum-registered test battery (Tests B/C CLOSED; Test A v1 ruled **UNGRADEABLE-UNDERPOWERED**, WQ-113 Will-ruled 8/28, no grade owed — `STATUS.md:96`) · the 8/28 dry-run that **grades nothing by instruction** · the Hormuz tell that **graded NEITHER pre-registered path** · auction demand-hole (Built 2026-07-06) · BDC Q2 mark card (Built 2026-04-16, light-populated 6/12, card 7/18) | **pre-registration discipline is this desk's signature** |
| `workbook/{TIC_FRAMEWORK, AUCTION_FRAMEWORK}.md` | TIC rewritten 2026-08-23 on ZHAO's Belgium-proxy falsification (`:38-49`) + China-rotation withdrawal (`:62`); auction grading template | method |
| `workbook/{CATALYSTS.tsv (26 rows, 8 cols incl. `date_class`), PREDICTIONS.tsv (LIQ-01..06), FLOW.tsv, VX.tsv}` | machine docket (boot countdown) · small durable prediction log · **FLOW/VX FROZEN 2026-07-11** | ledgers |
| `workbook/LIQ-04_KERNEL_NATIVE_COMPANION.json` + `kernel_staging/` (4 CMD JSONs + README) | Gate C Increment 2 **staged, explicitly NOT live** — "a LIQUID command exists only at `outbox/kernel/submissions/` under carve-out ④, and that path is inactive until Will's window ruling" | correctly fenced |
| `scripts/` (7 `.py`) | **`boot.py` (36,748 B)** — 3-dashboard live sweep + catalyst countdown + predictions due-scan + `watcher_echo()` (`:539`); `--selftest` **PASS** at HEAD (CATALYSTS 26 rows/8 cols · PREDICTIONS timeframes parse · KB 125 rows/13 cols); **exit code = FETCH health only, never alert state (`:24`)** · **`hy_oas_watch.py`** — systemd-timed daily unattended watcher (`:12`), **now with a delivery leg** (see §4) · `sofr_dispersion.py` (drift-robust successor to a dead band; `--baserate` re-prints realised fire rates, `:212`) · `fp_backtest_079.py` (calibration artifact — see the ⚠️ in §5.12) · `t3_decoupling.py` · `cftc_tff_rates.py` · `gate069_legs.py` | tooling — **strong, and self-base-rated** |
| `MEMORY.md` (**64,873 B**, 306 ln) | `## Session Notes` with dated CURRENT/PRIOR blocks back to 6/13 (log stops 2026-09-03), then **`### NEXT SESSION`** (`:283`) = the owed-work table + standing cautions. **Also the canonical record of two retracted own-figures** (`:20`, `:111-113`) | **the richest narrative surface and the one most at risk** |
| `NEXUS_BRIEF.md` (20,328 B) · `CALENDAR.md` (32,060 B) · `CLOSEOUT.md` (11,476 B) · `IDENTITY.md` · `STRATEGY.md` · `USER.md` · `CREDIT_THRESHOLDS.md` (`:2` Date 2026-02-28, Status HISTORICAL) · `CATCHUP_PUNCHLIST.md` (`:3` **FROZEN 2026-07-10**) · `LAST_COMPLETION.md` | cross-agent brief (rewritten not re-stamped 8/23, with a banner-history block at `:9`) · event twin of CATALYSTS, **"NO LIVE LEVELS IN THIS FILE" rule adopted 2026-08-20 (`:17`)** · 4-tier closeout (Bounce/Light/Standard/Heavy) · boot docs · decision playbook · frozen episode punchlist · last-delivery record | state + boot docs |
| `board_log.tsv` (167,390 B, 264 ln) | WALTER v0.2 delivery-lane ledger | intake ledger |
| `registry/corrections_receipts.tsv` (4 receipts + header) | R1 correction receipts | compliance — **1 named correction currently unreceipted**, see §4 (i) |
| `archive/` (53) · `domain/sources/` (26) · `outbox/` (25) · `reports/` (2, 7/11) · `research/` (1, 7/11) · `analysis/` (1) | rotation + foundations. **`analysis/2026-07-30_hy-attribution.md` (17,782 B) is load-bearing**, not archive: it is the artifact behind "the level fired on a mechanism the ladder was not built for" | reference + one live analysis |

## 3. Per-dimension local representation

| Dimension | Where it lives | Form / local titling | Rich? |
|---|---|---|---|
| Thesis structure | `thesis/THESIS.md` §1/§3 + `thesis/CHANGELOG.md` running-revision table | **legs A / B / C** (Fed-control / foreign-bid / basis-leverage) — unchanged since v2.0 (5/19). ⚠️ *"Path A/B" was never a LIQUID construct* (LIQ-02/03 resolution-path residue). **Channel-kill vs full-thesis-kill** at `THESIS.md:98` (DAEDALUS calls this the *migration theorem*, PAT-013), used live 7/30 | strong frame, stale version |
| Convergence / scoring | **no 5-point overlay** — LIQUID uses a **conviction %** on `THESIS.md:3` plus gate STATE tokens | **DORMANT → ARMED → TAGGED → TRIGGERED** vocabulary; conviction re-marked with a written both-ways derivation | local form, coherent; **not blueprint-shaped** |
| Invalidation / exit | `THESIS.md:85` §7 Kill Conditions · `KILL_MEMO_HY_OAS_260.md` (the ladder + **the canonical letter at `:45`**) · `STRATEGY.md:29` (playbook restatement — ⚠️ **disagrees with the letter**, see §4 (e)) · 5 `PROME/GATES.tsv` rows · the pre-registration layer (§2) | **two-sided by construction** (kill AND confirm on one series) · a **tape-vs-substance false-kill guard** with an arbiter (`KILL_MEMO…:123-188`) · `UNGRADEABLE-PENDING-PUBLICATION` ≠ `NOT-FIRED` · post-fire **TERMINAL, one kill, no re-count** · **H-2 counting rule** (`:26`) | **letter-quality is fleet-best; the fire RECORD is the weak half** |
| Thresholds | `CLAUDE.md:152-183` KEY THRESHOLDS (snapshot **self-labelled stale**) + the re-stamped state-flip list (`:156-166`) + **the basis canon (`:167`)** · `STATUS.md:57` · GATES condition cells | **The basis canon is the durable asset:** yields on FRED H.15 (CBOE same-day proxy only) · price triggers on **raw unadjusted closes** (`auto_adjust=False`) · auction % on accepted basis · Brent on the **ICE front-month settle** · USD/JPY on the **5pm ET NY close** · H.4.1 dated by its **as-of Wednesday**. *Declare the basis when you write a number.* Plus **Rule Zero on TIC: a holdings LEVEL change is NOT a flow** | exemplary |
| Predictions | `workbook/PREDICTIONS.tsv` (6 rows) | LIQ-01 ACHIEVED · LIQ-02 MISS (graded at the letter) · **LIQ-03 ACHIEVED — a MISS reversed by adversarial verify**, successor arm split out as LIQ-04 · LIQ-04 OPEN · **LIQ-05 VOID by Will-approved pre-registration discipline** · LIQ-06 ACHIEVED. Small ledger, **method fleet-exemplary** | exemplary method, thin volume |
| Gates (the real forward rail) | `PROME/GATES.tsv` (5 owned rows) + per-gate `definition_surface` files in `workbook/` | Every owned row carries a `review_by`. State at HEAD: **HY-REKILL** LIVE 0-of-2 (review 9/30) · **069** LIVE — ARMED 1-of-2, **graded 2026-09-12 against an owner-set `review_by` of 2026-09-15, i.e. three days early** (successor 10/15, set by PROME on LIQUID's *recommendation* — LIQUID explicitly declined to self-set it) · **072** LIVE (9/30) · **076** LIVE 0-of-3, legs moving away [8/28] (9/30) · **079** LIVE / NOT ARMED, FIRE legs `UNGRADEABLE-until-banded` (10/31) | **the strongest gate hygiene measured this pass** |
| Cross-agent routing | `CLAUDE.md:126-150` send/receive · `CLOSEOUT.md:90-99` Chunk 3 · `outbox/` · `board_log.tsv` | **SIGNALS → WALTER; ANALYSIS/PACKETS → direct**, corrected 2026-09-03 (`CLAUDE.md:64-65`) on the DAEDALUS route-around census. ⚠️ **`CLOSEOUT.md:95` ("self-commit it, carve-out ①") and `:96` ("Do NOT commit files outside `AGENTS/LIQUID/`") contradict each other** — live defect | conformant with one live defect |
| Unattended monitoring | `scripts/hy_oas_watch.py` + `alerts/` (gitignored) + `boot.py:539 watcher_echo()` | systemd `liquid-hy-watch.timer`, Mon–Fri 13:00 ET (`hy_oas_watch.py:12`). **Live at HEAD**: `alerts/watch.log` last line `2026-09-16 13:00 HY OAS 276bps 🟡yellow (sev 1, prev 1yellow, sub260 0, obs 2026-09-15 NEW) ok` — matches a live FRED pull (2.76, obs 2026-09-15). **Delivery leg BUILT 2026-08-27** (`d0126416e`): `:179-227` writes an idempotent packet to `PROME/inbox/` (repo ROOT — the constant carries its own `# repo ROOT, not AGENTS/PROME/` comment at `:179`) **and** appends a row to `AGENTS/SIGNALS.md`, never raises, and discloses in the packet body (`:211-212`) that it is machine-authored and uncommitted | **fleet-first: an unattended process with a routed output** |

## §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows — PAT-088)

⚠️ **`falsification_scan.py` sees TWO LIQUID surfaces** (run 2026-09-17 on the fixed working-tree build, `--agent LIQUID --tsv`): `workbook/KILL_MEMO_HY_OAS_260.md` **STALE-FLAGGED** at 25d (stamp 2026-08-23 vs live ref 2026-09-17, threshold 21d), and `thesis/CHANGELOG.md` **CURRENT** (stamp 2026-08-28, 20d, CitedVer v2.0). The other nine rails below are invisible to it because they do not match `SURFACE_PATTERNS` (`falsification_scan.py:38-43`). Full hand-derived inventory:

| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `thesis/THESIS.md:85` §7 Kill Conditions | the **thesis** (6 conditions, legs A/B/C) | `THESIS.md:3` `Last Updated: 2026-06-25` — **84d** | conviction re-mark + a CHANGELOG/KB pivot row |
| `workbook/KILL_MEMO_HY_OAS_260.md` — the ladder + **§★ canonical letter (`:45`)** | the **credit axis**: `GATE-HY-REKILL` = HY OAS strictly <260.0 bp on **TWO consecutive published observations**, as-first-published, terminal on fire | `:7` "STATE AS-OF **2026-08-23**" (**25d — the scan's flag**); body current to 2026-09-03 (WQ-162 fold) | `## Drill log` (`:229`) — **n=1, the 2026-07-01 TAGGED row** |
| `thesis/CHANGELOG.md` — running revision table (`:7`) | records what moved in the thesis without a version bump | `:3` TWO-STATED 2026-08-28 | 8 pointer rows, each naming its own dated record |
| `PROME/GATES.tsv` — 5 `owner=LIQUID` rows | per-gate arm/fire | each row's `last_checked` + `review_by` cells | `state` cell + a `STATE_HISTORY` pointer |
| `workbook/FUNDING_SEIZURE_GATE_SCOPED.md` | GATE-LIQ-079 — funding seizure as a **separate root** (R1: never "X1 MET") | `:2` Registered 2026-07-17 · BROCK sign-off 2026-07-20 | GATES 079 state cell (`FIRE legs UNGRADEABLE-until-banded`, declared 9/3) |
| `workbook/DEALER_POSITIONING_NEXUS_WATCH.md` | GATE-LIQ-076 — 2-of-3 amplification conjunction ⇒ a **write-up deliverable, NOT a position trigger** | "as-of 8/18" | GATES 076 `0-of-3, legs moving away [8/28]` |
| `workbook/ORCL_FALLEN_ANGEL_MAP.md` | GATE-LIQ-069 leg-5 / R1 second-agency fire | `:3` "CHECKED **2026-08-24** … NO CHANGE" (**24d**) | in-file ladder + GATES 069 `ARMED 1-of-2` |
| `workbook/EXPECTED_SIGNALS_TRACKER.md` | **absence-is-data** ES-LIQ-01..05 (FHLB / sponsored-repo / MMF WAM / FTD / CCY-basis) | `:2` Born 2026-07-11 · **`## ★ REVIEW 2026-08-24`** (`:21`) | `## Resolved / fired log` (`:57`) — **1 row**, ES-02/03/04 cluster `DID_NOT_APPEAR` |
| `workbook/DECOUPLING_TESTS_VIX_HY_2026-08-10.md` + `T3_DECOUPLING_TEST_A_DRYRUN.md` | VIX-vs-HY **independence** (is HENRY's VIX leg and the HY leg one factor measured twice?) | filename dates · dry-run "Run: 2026-08-28" | Tests B and C **CLOSED**; Test A v1 **UNGRADEABLE-UNDERPOWERED** (WQ-113, Will-ruled 8/28, no grade owed — `STATUS.md:96`); only live leg = T3 v2, **first decidable 2026-09-23** (`archive/status_snapshots/STATUS_PROSE_2026-09-12_rotation.md:39`) |
| `workbook/HY_HORMUZ_LAGGING_TELL_WATCH.md` | the oil→HY lagging tell | `:2` Registered 2026-07-17, KB-LIQ-081 | **graded NEITHER pre-registered path** — base case died on its own antecedent (Brent never round-tripped <$75; KB-LIQ-101). A pre-registration defect, recorded as such (`CHANGELOG.md:16`) |
| `workbook/DEMAND_HOLE_AUCTION_PREREG_2026-07.md` · `BDC_MARK_CONVERGENCE_MONITOR.md` | auction demand-hole · BDC Q2 mark pre-reg card (KB-083; NEXUS R3 / BROCK wrapper-leads X1 half) | Built 2026-07-06 · Built 2026-04-16, light-populated 2026-06-12, card added 2026-07-18 | card lines; the BDC Q2 window (7/25→early-Aug) is **past and the card is ungraded** |
| `archive/CONSUMER_CREDIT_MONOLINES_PREREG_GRADED_2026-08-24.md` | *(retired)* consumer-monolines pre-reg | filename | **GRADED REFUTE + ARCHIVED 2026-08-24** (KB-LIQ-103) — the correct terminal form |

## 4. Deviations from standard (+ why)

**Better than blueprint**
1. **Two-sided falsification on one series.** A single instrument carries both the kill (<260) and the confirm (>280/>320), with the counting rule, the vintage rule, the publication rule and the terminality rule all written down in one Will-ruled letter. Most desks write a kill and forget the confirm.
2. **The pre-registration layer, including its own defects.** Two registered tests resolved to *"the letter was unusable"* rather than a market verdict — the Hormuz tell graded **neither path** and Test A v1 was ruled **UNGRADEABLE-UNDERPOWERED** with **no grade owed**. Recording a pre-registration defect as a defect is the harder discipline and it is this desk's habit.
3. **Bands get base-rated, and the base rates themselves get audited.** `SOFR75−IORB ≥0 ×3 non-Q-end days` is **dead as a 2026 tripwire** — *"cleared by the median day; satisfied 27 consecutive sessions while STATUS read 'need 3'"* — but **dead by DRIFT, not by construction** (`MEMORY.md:25`). ⚠️ **Do NOT cite the 59.9% figure**: LIQUID retracted it the same session — it was computed on a window truncated by its own `limit=900` fetch arg; the **true full-window figure is 30.7%** (`MEMORY.md:20`). Its successor `sofr_dispersion.py` ships with `--baserate`, and that script's own first drift flag was re-cut after firing on **60.8%** of sessions (`sofr_dispersion.py:92,:205`). **Four registered bands died in six days, three of them dead-LOUD** (`thesis/CHANGELOG.md:19`).
4. **The unattended watcher now routes.** The old profile's flag #2 (detection correct, delivery zero) is **BUILT**: `hy_oas_watch.py:179-227` writes an idempotent `(kind, obs_date)`-keyed packet to `PROME/inbox/` (repo root, correctly, with the comment on the constant) and appends to `AGENTS/SIGNALS.md`, wrapped so a delivery failure never costs the detection — and the packet says in its own body *"written to disk by an unattended process and is NOT committed by it… If you are reading it, it survived to a session — commit it."*
5. **Levels are banned from state files.** "NO LIVE LEVELS IN THIS FILE — run `scripts/boot.py`" is adopted in `CALENDAR.md:17` and in `STATUS.md`'s pointer block, after the same list went inverted three times. The failure was a hand-restamped list; the fix was to stop carrying levels, not to restamp harder.
6. **Correction provenance is kept, not overwritten.** `CATCHUP_PUNCHLIST.md:5` carries `🔴 CORRECTED 2026-08-24: "Tracked in STATUS.md Open Monitors" was FALSE — it was never tracked there`; `NEXUS_BRIEF.md:9` keeps a **banner history** block precisely because this file has a record of banners going stale.

**Divergences that are equivalent, not debt**
- **No 5-point convergence overlay and no Independence column.** LIQUID runs conviction-% + gate STATE tokens instead. Months of evidence say the local form works. **The open question is whether the overlay is worth building at all, or whether this is the map's problem** — carried as Q2.
- **Multi-doc threshold split** (`CREDIT_THRESHOLDS.md` HISTORICAL-by-banner, dated 2026-02-28; live thresholds in STATUS + KILL_MEMO + GATES) is deliberate and correct; not an archival candidate.
- **`outbox/` is crisis-only.** Not a volume gap.
- **`alerts/` is `.gitignore`d BY DESIGN** (`AGENTS/LIQUID/.gitignore`: *"P1b HY OAS watcher runtime state — regenerated each run, never commit"*). Never "fix" the gitignore; write packets elsewhere (the watcher already does).

**Live debt (verified at HEAD 2026-09-17)**
- **(a) THESIS.md is unversioned since v2.0 (6/25) through a documented 8/23–8/28 rework.** The rework is real and is recorded — in `CHANGELOG.md`'s running-revision table and in KB rows — but `THESIS.md:1` still reads `v2.0` and `:3` still reads `Conviction: 61%`. The CHANGELOG's own rewrite trigger says v3.0 waits for a structural leg to move; **five of the eight rows in its revision table are leg-level**. Whether that clears the trigger is LIQUID's call — but the *header* is what every reader grades.
- **(b) `STATUS.md` is over the read-cap budget** (34,662 B = 106%; `read_cap_check --agent LIQUID` rc=1, over budget but not over the 54,250 B cap).
- **(c) `MEMORY.md` session log stops at 2026-09-03** and its `NEXT SESSION` block (`:283`) is re-cut 2026-08-27.
- **(d) `IDENTITY.md:18` carries a live-sounding level from 6/24** — *"HY OAS **276** (6/24), cushion above the 260 KILL 16bps"*, 85 days old and phrased as current. The nastiest one on the desk (and coincidentally 276 is also today's print, which makes it harder, not easier, to catch).
- **(e) `STRATEGY.md:29` states a kill count that disagrees with the ruled letter** — "<260 sustained **≥3 sessions**" vs the WQ-162 letter's **TWO consecutive published observations**.
- **(f) 18 of 26 `CATALYSTS.tsv` rows are past-dated.**
- **(g) no LIQUID `.tsv` carries a two-clock header** and there is **no `workbook/LEDGER_GLOB`**, so `ledger_staleness.py` sees 5 TSVs (0 stale) and **none of the 13 `workbook/*.md` rails**. Unchanged from the old profile.
- **(h) `thesis/TIMELINE.md` (7/06) branch tree** — resolved rows still unretired; 73d; **NOT re-verified in detail this pass**.
- **(i) One named R1 correction is unreceipted** — `corrections_boot_check.py LIQUID` → **rc=1 BLOCK**: `COR-20260915-02 [LIVE] 2026-09-15`, pointer `BOARD/SIG-W-20260915-002-CORRECTION-wal-cycle-two-already-fired.md`. This blocks LIQUID's own boot check until receipted.

## 5. Load-bearing context / DO NOT TOUCH

1. **⛔ KILL_MEMO filename LOCK.** `workbook/KILL_MEMO_HY_OAS_260.md` is referenced by CLAUDE/STATUS/IDENTITY/STRATEGY/THESIS/TIMELINE/CHANGELOG **and is the `definition_surface` for `GATE-HY-REKILL` in `PROME/GATES.tsv`.** Never rename — including while fixing its drill log. The `_260` in the name is now historically inaccurate (it is two-sided) and that is fine.
2. **The canonical GATE-HY-REKILL letter is Will-ruled (WQ-162, 2026-09-02 21:29 ET) and lives at `KILL_MEMO…:45`.** Strictly **<260.0 bp**, **TWO consecutive published observations**, **as-first-published**, **terminal on fire**, unit = FRED percent × 100. **A count is CLOSED at 2 or reset by a published obs ≥260.0.** Do not restate this count anywhere in a different number — `STRATEGY.md:29` currently does.
3. **`UNGRADEABLE-PENDING-PUBLICATION` is never `NOT-FIRED`.** BAMLH0A0HYM2 is T+1.
4. **H-2 counting rule (Will-ruled 2026-08-10, `KILL_MEMO…:26`):** a joint fire of `GATE-HY-REKILL` and HENRY's `<260-sustained-5` soft-kill leg is **ONE event on ONE series** — never reported as two confirmations.
5. **X1 is CONJUNCTIVE.** HY>280 sustained **AND** BROCK's wrapper-leads half. **No HY level alone can make this "X1 MET"** — even 287 with sustain 3-of-3 did not fire it. **BROCK adjudicated its half NOT ARMED on 2026-08-28** (KB-BRK-219, commit `17d87df22`; recorded at `STATUS.md:105`). **The `contested` branch in the memo is SPENT and must not be actioned.**
6. **GATE-LIQ-079 is a SEPARATE ROOT** under riders R1–R4 (BROCK 2026-07-20): R1 never "X1 MET" · R2 opens no X1 sizing gate · R3 suspends BROCK's wrapper-leads read · R4 RRP is the wrong regime variable.
7. **⛔ The private-credit gate count is RETIRED-AND-REPOINTED (`CLAUDE.md:69`, closed 2026-09-12).** LIQUID holds no gate count; the registered instrument is **BROCK's `GATE-BRK-R2`** (definition surface `AGENTS/BROCK/workbook/PC_REDEMPTION_REGISTER.tsv`, header + `gate_status` column). **Read BROCK's count; never keep a second, coarser one here.** BROCK's 2026-09-09 ruling stands (`CLAUDE.md:74`): **a pro-rated tender is NOT a gate** — it is the facility operating as designed at its stated cap.
8. **The Belgium-as-China-proxy INFERENCE is FALSIFIED** (ZHAO 8/21, Will-ruled; rho = **+0.050**, n=41; Belgium bought in **15 of 27 (56%)** China-selling months — `TIC_FRAMEWORK.md:40,:45`). The **>$500B route survives as a BARE LEVEL alert with no China attribution** (`:49`; Belgium $482.5B [Jun-26], $17.5B from the line). Reinstate only at **rho < −0.5 rolling-24m** (`:48`). **Rule Zero on every TIC read: a holdings LEVEL change is NOT a flow.**
9. **The basis canon (`CLAUDE.md:167`) binds every count.** FRED H.15 for yields · raw unadjusted closes for price triggers · accepted basis for auction % · ICE front-month **settle** for Brent · 5pm-ET NY close for USD/JPY · H.4.1 dated by its as-of Wednesday. **Declare the basis when you write a number.** (LIQ-03's grade once flipped on `auto_adjust`.)
10. **GATE-079 false-positive figures cite in DENOMINATOR FORM ONLY** — **5 of 8 → 2 of 8 episodes, n=1 TP** (`MEMORY.md:111,:113`). LIQUID's own fleet-routed rule, adopted 7/30 on BROCK's flag: *never a bare "62%"* — a bare percentage travels stripped of its denominator.
11. **LIQ-05 VOID is Will-approved pre-registration discipline — never re-grade, and a sweep must not read VOID as incomplete.** **LIQ-03's long `Notes` cell is the audit trail of a reversed grade — never compress.**
12. **⚠️ `fp_backtest_079.py` should be treated as pinned evidence — but nothing in LIQUID's tree says so.** Re-running it on a moved window would silently change a published false-positive census (the 5-of-8 → 2-of-8 figures above). The "pinned calibration artifact" designation exists only in DAEDALUS's prior profile (`profiles/LIQUID.md:34`); the script header carries no banner. **Owner ask: write the pin into the script.** **`ofr_stfm.py` lives in DEWEY's tree** (`AGENTS/DEWEY/scripts/ofr_stfm.py`) — the planned stage-2 extension is a cross-agent ask, not a LIQUID build.
13. **`config.py` is imported, never forked** — `from config import classify, get_agent` (`hy_oas_watch.py:108`), resolving to **`FORGE/tools/market-data/config.py`**, not a LIQUID file; the watcher and boot share SENTRY-retuned bands so a retune flows through automatically. **`boot.py`'s exit code is FETCH health only** (`:24`) — a red thesis trigger still exits 0; parse stdout.
14. **`alerts/` is gitignored by design; `hy_oas_watch.py` delivers OUTSIDE it** (to `PROME/inbox/` + `AGENTS/SIGNALS.md`). Never move delivery back into `alerts/`, and never commit `alerts/`.
15. **`kernel_staging/` is NOT live.** A LIQUID Kernel command exists only at `outbox/kernel/submissions/` under root carve-out ④, and that path is inactive until Will's window ruling.
16. **FLOW.tsv / VX.tsv hard-FROZEN 2026-07-11; `CREDIT_THRESHOLDS.md` is HISTORICAL-by-banner (dated 2026-02-28) and is correct as-is; `CATCHUP_PUNCHLIST.md` is FROZEN 2026-07-10.** None is an archival candidate.
17. **Migration/attribution redundancy — never dedupe.** `THESIS.md:98` ("Channel-kill vs full-thesis-kill is the key distinction") and the 7/30 attribution are restated in several places on purpose. The attribution is the evidence: **68–84% broad DM HY beta · 15–30% AI/data-center · ~0% bank/CRE, HIGH confidence** (`CLAUDE.md:163`; `analysis/2026-07-30_hy-attribution.md`; `KILL_MEMO…:12`; `CHANGELOG.md:89`). ⚠️ *The slogan "the level fired on a mechanism the ladder was not built for" is a DAEDALUS gloss, not a LIQUID quotation — do not attribute it to a LIQUID file.*
18. **Read any future 280-cross against that attribution before treating it as credit recognition.**

## 6. Maturity snapshot

**Per `FLEET_MAP.tsv` LIQUID row at HEAD: L4 / conf H / last-scored 2026-09-17** (re-cut by PR#6, commit `7bfee0060`, 2026-09-17 09:53 ET; classification not restated here). Work queue → `AGENTS/DAEDALUS/upgrades/LIQUID_CARD.md`.

Section read at 2026-09-17: **exemplary** on Invalidation-letter quality, Thresholds/basis canon, Gate hygiene, Pre-registration discipline, and Prediction *method*; **strong** on Tooling (7 scripts, selftested, base-rated, and self-retracting on its own figures); **weak** on the **fire RECORD** (drill log n=1 through the ladder's only ever tag) and on **header currency** (THESIS v2.0 / conviction 61% / IDENTITY 6/24 levels).

The current `Next_upgrade` cell names four legs: rotate STATUS under 32,550 B and then under 22,785 B · bump THESIS off v2.0 to reflect the 8/23-8/28 rework · restate the (a)-(d) legs on a live surface or strike them · add the 8/28 HY-260 row to the KILL_MEMO drill log. **All four are TRUE-STILL at HEAD.** The prior row's `Gaps` claim *"Dark since 8/28"* was **REFUTED** and has been removed: LIQUID self-authored **31** commits after 2026-08-28, the last on 2026-09-12.

## 7. Open questions / comprehension gaps

- **Q1 — Does an UN-FIRE deserve delivery?** `hy_oas_watch.py` is escalation-only by construction (`:5-8` docstring; no de-escalation branch at HEAD). It correctly watched the entire 7/31→8/6 round-trip and, per spec, said nothing — and the 8/3 break is exactly what made five surfaces go stale in the ARM direction. Adding un-fire delivery is a **spec change, LIQUID's call, Will-visible.** Carried from 2026-08-07, unresolved.
- **Q2 — Is the 5-point convergence overlay worth building here, or is the blocker the map's?** Carried from the 8/7 profile. Read: the conviction-% + gate-token form is coherent and the gate layer is doing the work an overlay would. **Recommend DAEDALUS adjudicate the requirement before asking LIQUID to build it.**
- **Q3 — Does the 8/23–8/28 rework clear the CHANGELOG's own v3.0 trigger?** The trigger is "a structural leg added, retired, or inverted." The revision table records a channel *retired as specified*, an instrument *permanently lost*, an inference *falsified*, a mechanism *re-based*, and a *candidate new leg not promoted* — ≥1 leg-level event on a plain reading, but the call is LIQUID's and the file names the arbiter. **NOT-ADJUDICATED.**
- **Q4 — What are "the 8/7 legs (a)–(d)"?** No (a)-(d) enumeration was located in either the old profile or the LIQUID tree, so the FLEET_MAP row's claim that they are ungradeable cannot itself be graded. **CANNOT-EVALUATE** — needs the PR#4/8-07 source.
- **Q5 — Is the BDC Q2 mark pre-reg card owed a grade?** `BDC_MARK_CONVERGENCE_MONITOR.md:4` holds a 7/18 pre-reg card for the 7/25→early-Aug window; the window is 7 weeks past and no grade was found. KB-083 was re-dated and the X1 wrapper half was adjudicated by BROCK on 8/28, which may have mooted it. **CANNOT-EVALUATE.**
- **Q6 — `thesis/TIMELINE.md` branch-tree currency.** Carried from the old profile ("4-of-8 resolved rows unretired, 43d"); the file is unchanged since 7/06 (now 73d) and the 8 branches were not re-walked. **NOT-ADJUDICATED this pass.**

## 4b. 🔴 Findings the first reader missed — LIQUID

| # | Finding | Locator |
|---|---|---|
| **V-L1** | **`STATUS.md:120` advertises a KB range that is 3 rows short of the ledger.** The heading reads `## Durable Signals Log → workbook/KB.tsv (KB-LIQ-001..**122**)` while `KB.tsv` holds **125** rows, max `KB-LIQ-125` (confirmed twice: `grep -c` and `boot.py --selftest`). A stale mirror on a **live boot-read heading** — a reader who trusts it will believe KB-LIQ-123/124/125 do not exist, and KB-LIQ-124 is the row that produced the route-around-WALTER self-audit. | `AGENTS/LIQUID/STATUS.md:120` vs `AGENTS/LIQUID/workbook/KB.tsv` |
| **V-L2** | **The draft banked a figure LIQUID had already retracted.** §4 item 3 cites `59.9% of non-Q-end sessions, n=615` as the measurement that killed `SOFR75−IORB ≥0`. `MEMORY.md:20` records that same figure as a **self-caught error** (window truncated by a `limit=900` fetch arg; true full-window **30.7%**), and `MEMORY.md:25` says the band died by **drift**, not by the median-day argument. `n=615` appears nowhere in the tree. This is exactly the desk's own lesson — *"a claim born inside a retraction inherits the retraction's credibility"* (`MEMORY.md:23`) — landing on its reviewer. | `AGENTS/LIQUID/MEMORY.md:20,:23,:25` |
| **V-L3** | **`fp_backtest_079.py` is protected only by a DAEDALUS-side note.** Both the draft and the 2026-08-07 profile call it "pinned / do-not-touch", but the script (`:1-14`) and every LIQUID surface are silent. A future LIQUID session re-running it on a moved window would silently change the published 5-of-8 → 2-of-8 census with no guard firing. The pin must live in the script. | `AGENTS/LIQUID/scripts/fp_backtest_079.py:1-14`; designation at `AGENTS/DAEDALUS/profiles/LIQUID.md:34` |

---

## Verifier's closing note

Three commits landed between the reader's HEAD (`b824b5a13`, 09:31 ET) and this verification (`e6abbfd1b`), and one of them — **PR#6, `7bfee0060`, 09:53 ET** — re-cut the FLEET_MAP rows both drafts grade. Every §6 claim in the draft was correct when written. The CARL row is additionally being edited in the working tree right now (uncommitted, last-scored bumped to 2026-09-17). **When installing, take §6 from this file, not from the draft** — and re-read the CARL row at commit time, because it is moving under both of us `[[finding_directive_overtaken_between_authorship_and_delivery]]`.

The draft is strong: **117 of 146 graded claims verified exactly**, including every byte size, every tool-run transcript, and an 80,967 B hand-measurement that reproduced to the byte. **Six claims FAILED**, and the defect concentration is in **three narrow classes**, all locator-integrity rather than judgment: (1) **boot-step numbers written as line numbers** on CARL, the one charter where that is systematically ambiguous; (2) **line counts read as row counts** on comment-heavy TSVs (PHAN's 46-line file → "45 predictions"; actual 7) and the same slip on the stale-ledger count (16 vs 17); (3) **a figure quoted past its own retraction** — the 59.9% SOFR base rate that LIQUID had already withdrawn in favour of 30.7%. None touched a thesis judgment.

**And one class landed on me.** My first pass graded the reader's two `falsification_scan` claims FAILED because I ran the working-tree build — which DAEDALUS had fixed *that morning, crediting this very reader's flag D-1*. I tested the cure and graded the diagnosis. Both claims are correct against the committed scanner, the root cause reproduces exactly (`"STALE-VINTAGE" in head.upper()` matching prose at `CARL/thesis/THESIS.md:2`), and the verdicts are withdrawn above. **Standing lesson for the next verifier slot: before grading any tool-output claim, run `git status` on the tool.** `[[finding_a_pinned_reproduction_cannot_confirm_a_cure]]` · `[[finding_instrument_reports_clean_against_the_wrong_reference]]`
