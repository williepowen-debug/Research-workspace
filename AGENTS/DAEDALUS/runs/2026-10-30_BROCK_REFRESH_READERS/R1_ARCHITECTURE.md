# R1 — ARCHITECTURE reader — BROCK whole-profile refresh (Mode-A)

**Reader:** R1 of 3 (DAEDALUS-spawned) · **Started:** Fri 2026-10-30 13:17 EDT (`date`) · **HEAD at start:** 75555a7cf
**Baseline:** `AGENTS/DAEDALUS/profiles/BROCK.md` (vintage 2026-09-17, STALE banner 10/21)
**Tree check before any script:** `git status --porcelain -- AGENTS/BROCK/` → *(empty — clean)* at 13:17 EDT

*(sections written incrementally; all sections A–H complete)*

## A. What BROCK is and does NOW

**Identity (unchanged in substance):** BDC / private-credit / alt-manager / PE-insurance desk — *"Early warning system for private credit stress and its transmission to banks and insurance"* (`AGENTS/BROCK/CLAUDE.md:4`). Core thesis verbatim unchanged since 9/17: *"Private Credit's Public Reckoning — PIK masks a ~6% shadow default rate (vs reported 2.1%)…"* (`CLAUDE.md:12`); second layer insurance/reinsurance reflexivity (`CLAUDE.md:14`). Domain scope / "do NOT own" cessions unchanged (`CLAUDE.md:195-210`). **New since 9/17:** an ALWAYS-LOADED §STANDING TRAPS block of 7 write-time traps adopted 10/2 from CREED (`CLAUDE.md:20-30`) — *"A trap earns a place only by having bitten BROCK while writing a number"* (`:22`).

**Current judgment (STATUS vintage `2026-10-30T09:1x-04:00`, `STATUS.md:3`):**

| Item | Desk's words / figure | Cite |
|---|---|---|
| Convergence | **58/70 🔴🔴 — RESCORED 2026-09-25 (Duration 3→4)**; arithmetic printed and I re-summed it: 5+5+3+4+4+3+5+3+3+5+5+4+4+5 = 58 ✅ | `STATUS.md:83-84` |
| Narrative phase | *"STAGE 2→3. Substance FIRMED / transmission DORMANT / X1 NOT MET"* | `STATUS.md:54` |
| Exit §3 | *"NOT FIRING — 2 of 3"* (PIK and NDFI both downgraded 9/3) | `STATUS.md:85`, `:102` |
| Gates | GATE-BRK-R2 (a) FIRED ×2 (North Haven 9/25, OCIC 10/2); review **2026-10-31** (tomorrow); OCIC final (b) 29.8% NOT FIRED 10/28 | `STATUS.md:66` |
| Software-mark thesis | ARCC guide NOT MET 10/28 + HTGC *"THESIS FAILS FOR Q3"* 10/29 = *"two bellwether non-confirmations; no registered downgrade leg ⇒ no rescore"* | `STATUS.md:15`, `:72` |
| Predictions resolved since 9/17 | BRK-02 RESOLVED-FALSE 10/2; BRK-10 RESOLVED-FALSE 10/29; (BRK-22 RESOLVED-FALSE 10/28 per `catchups/INDEX.md`) | `STATUS.md:106`, `:109` |
| Live dated reads | CRMT 8th-bridge STD Sun 11/01 (reads 10/30 after ~16:30 + 11/02 AM); CABO Q3 10-Q Thu 11/05 AMC; FSK Q3 11/05; North Haven final ~11/05 | `STATUS.md:12-19` |
| Bottom line | *"Convergence 58/70, unchanged"* | `STATUS.md:116` |

**Book / position as the desk describes it (off-repo truth; not resolved here):** *"APO $130 sustained → FIRED 8/12; Will RULED HOLD 8/13 … FORGE 10/14: Dec18 $95P ×1, exact capture/mark time UNKNOWN … Any disposition is Will's; TERRY constructs. $0 moved."* (`STATUS.md:97`). Vintage = FORGE 10/14 mirror. Tape cited in the 10/30 catch-up: APO $118.56 [10/29 close] (`catchups/2026-10-30.md` §Other).

**Runtime as operated — TWO runtimes, both self-recorded per session:**
- **Claude Code, Opus 5.5, PROME-spawned due-row wakes** (cwd `PROME/`, explicit charter reads via `PROME/tools/boot_read.py`): *"Runtime: Claude Code, Opus 5.5, spawned by PROME (cwd PROME/; charters read explicitly via `PROME/tools/boot_read.py`, all to eof …)"* (`catchups/2026-10-30.md:5`; same form `catchups/2026-10-29.md:5`, `catchups/2026-10-09.md:24`).
- **OpenAI Codex, Will's own-window sessions** — 10/14 (*"Actual ask received in this continuing Codex session"*, `catchups/2026-10-14.md:82`) and 10/25 (*"Runtime: OpenAI Codex, exact model UNKNOWN, thread 01a173ad-…; no subagents"*, `catchups/2026-10-25.md:5`). **27 of BROCK's 70 self-commits since 9/17 (10 on 10/14, 17 on 10/25) carry no Claude trailer** — the Codex sessions; the other 43 carry Claude Opus trailers (5.5 / 5 / 4.7). The 10 Fable trailers on BROCK-path commits are PROME/NEXUS commits, not BROCK's.
The desk is runtime-portable as the root amendment intends; see F for one runtime-correlated canon defect.

**Live-session evidence (git log `-- AGENTS/BROCK/`, after 2026-09-17):** 242 commits touching the dir; **70 BROCK-authored** subjects on 17 distinct days — 09-18 (2) · 09-21 · 09-25 (3) · 09-26 · 10-02 (15) · 10-08 · 10-09 (5) · 10-14 (10) · 10-15 (2) · 10-16 · 10-21 (3) · 10-22 · 10-23 · 10-25 (17) · 10-28 (2) · 10-29 (4) · 10-30. Newest: `BROCK: L795 CABO graded NOT CLOSED, TRO hearing 11/13 press-only; L794 CRMT armed` (10/30 ~10:19). **Not dark** — longest gap 9/26→10/2 (6 d).


## B. File anatomy (measured 2026-10-30 13:20 EDT, `wc -c`; % of the 32,550 B budget)

Tree: **719 tracked files** (was 334 at 9/17 — growth almost entirely `inbox/` 428 and `research/` 142).

| File / dir | Role in BROCK's words | Bytes (% budget) | Boot-read? charter · READS.tsv | Richness / note |
|---|---|---|---|---|
| `CLAUDE.md` | charter; boot 0–5b, closeout 6–12, traps | **31,274 (96%)** | auto/explicit (BASIS row `READS.tsv:230`, "boot-defining") | 🟠 grew +6,586 B (+27%) since 9/17; 1,276 B to budget; see D |
| `STATUS.md` | *"HOT current state: §Standing Obligations … Byte-budgeted"* (`CLAUDE.md:133`) | 22,729 (70%) | boot 1 · `READS.tsv:235` whole | ✅ richest live surface; Standing Obligations table (`:7-44`) is new since 9/17 |
| `LESSONS.md` | *"Numbered mistake patterns … Append-only"* (`CLAUDE.md:136`) | 23,596 (72%) | boot 2 · `READS.tsv:236` whole | numbered through **#39** (10/29); rotation pointers keep index of rotated #23–#30 |
| `SCRATCH.md` | *"Overwrite-only handoff; boot step 0b"* (`CLAUDE.md:252`) | 1,432 (4%) | boot 0b · `READS.tsv:239` whole | ✅ 46,122 → 1,432 B; rewritten every session day since 10/2 (13/13 days in git log) |
| `catchups/` (13 day files + `INDEX.md`) | *"One file per session, verbatim narrative; INDEX.md names the CURRENT one"* (`CLAUDE.md:134`) | INDEX 4,929 (15%); members 3,201–15,392 (max 47%) | boot 1 (INDEX + CURRENT) · `READS.tsv:240-241` | ✅ new layer; per-session Runtime + boot-check lines |
| `NEXUS_BRIEF.md` | cross-agent brief (NEXUS schema) | 15,715 (48%) | not BROCK boot; **read whole by NEXUS:6** (read_cap owner notice) | composite now **58/70** = STATUS ✅; **no BROCK charter step names it** (see C) |
| `MAINTENANCE.md` | *"structural change-log … plus the modernization backlog"* (`:3`) | 9,636 (30%) | no · no | ✅ 10/2 CREED-adoption entry is exemplary; backlog table not refreshed (F) |
| `LAST_COMPLETION.md` | 9/21 completion block | 5,347 (16%) | no · no | ✅ `HISTORICAL — banner added October14` (`:1`) |
| `EXPECTED_SIGNALS.md` | *"Signal interpretation methodology + thresholds"* (`CLAUDE.md:142`) | 4,655 (14%) | no · no | 🔴 untouched since 2026-03-06 (`git log`); thresholds disagree with live matrix (F1) |
| `OPEN_ITEMS_2026-09-03.md` | Will-commissioned inventory | 9,375 (29%) | no | ✅ HISTORICAL-bannered 10/14 (`:1`) |
| `OPEN_THREADS_2026-07-09.md` | July thread list | 3,699 (11%) | no | 🟡 no banner, >60 d, no live ref ⇒ retirement-eligible |
| `ARCH_REPORT_2026-06-26.md` | June self-report | 4,663 (14%) | no | 🟡 same; >60 d, no banner |
| `board_log.tsv` | WALTER consumption ledger | 154,003 (473%) | boot 5 grep-only · `READS.tsv:238` grep | append-only; never read whole (I did not) |
| `workbook/` (16) | KB 391,710 · PREDICTIONS 56,215 (scoped, `READS.tsv:237`) · VX · FLOW · PC_REDEMPTION_REGISTER · PUBLISHED · RESEARCH_INDEX.md · SCHEMA · VX_HISTORY · 2 FROZEN · ARCHIVE/SCOREBOARD · **`LEDGER_GLOB` (28 B, new)** | — | PREDICTIONS scoped (boot 3) | R2/R3 cluster; `LEDGER_GLOB` = `workbook/*.tsv docket/*.tsv` ✅ |
| `docket/CATALYSTS.tsv` (1) | *"Full dated catalyst docket (STATUS carries only owed/near items)"* (`CLAUDE.md:255`) | **49,425 (152%)** | no · no (by design — STATUS carries near items) | in `LEDGER_GLOB` ✅; 152% would matter only if anyone read it whole |
| `scripts/` (1) | `brock_selfcheck.py` 6,829 B — closeout 6c | — | closeout | ✅ new 10/2; I ran it: `CLEAN … rc=0` |
| `tools/` (1 tracked + `__pycache__`) | `soi_nonaccrual.py` 8,275 B (9/3) | — | no | unchanged |
| `reports/` (1) | `2026-10-21_self-sweep.md` 9,494 B — *"report only; nothing fixed"* | — | no | ✅ 28-row ranked self-audit, Will-asked via PROME |
| `registry/` (1) | `corrections_receipts.tsv` 3,236 B | — | 5b conditional · `READS.tsv:243` scoped | R1 rc 0 on 10/30 (`catchups/2026-10-30.md:5`) |
| `archive/` (33) | rotations: STATUS ×9, LESSONS ×3, SCRATCH ×2, NEXUS_BRIEF ×1, PRESPLIT, + `research-outputs/`, `domain-sources/` | — | no | crc-stamped rotations |
| `domain/` (35) | `sources/` 34 + `PRIVATE_CREDIT_CONTAGION_TRACKER.md` | — | no | tracker now HISTORICAL-bannered 10/14 (`:1`) ✅ |
| `research/` (142 tracked; 207 on disk, 65 gitignored `*_facts.json` etc.) | memos/deep dives | — | no | 20 of 39 top entries dated 2026-10 |
| `trade/` (7) | TRADE.md FROZEN 7/27 · NAMES.md HISTORICAL 10/14 · CROSS_ANALYSIS · APO/ (4) | — | no | |
| `inbox/` (428) | 3 pending top-level (all arrived 10/30 after the 09:xx session) · `processed/` 143 · `WALTER/` 0 pending · `WALTER/processed/` 282 | — | boot 5 (WALTER lane only) | |
| `outbox/` (27) | 26 top-level (Apr–Oct) + `delivered/` | — | no | 🟡 14 Apr–Jun signal files to non-PROME desks still top-level (pre-9/3 routing residue) |
| `AGENTS.md` shim | **none in `AGENTS/BROCK/`** | — | — | n/a |


## C. Boot and closeout wiring

Declared symmetry: *"Boot and closeout are one symmetric sequence: what you READ at boot, you WRITE BACK at closeout … SCRATCH (read 0b → rewrite 6b); STATUS + CURRENT catch-up (read 1 → write 6); PREDICTIONS (scan 3 → disposition 7a)."* (`CLAUDE.md:36`)

**BOOT** (`CLAUDE.md:42-54`)

| Step | Line | Surface | READS.tsv | Write-back end | Executed? (evidence) |
|---|---|---|---|---|---|
| 0 pull | :43 | git | — | 12 | 10/30: *"Pull: not run — tree carries PROME's dirty `PROME/state/` files; `git fetch` shows origin has nothing we lack"* — correct under root Git Protocol (`catchups/2026-10-30.md:5`) |
| 0b SCRATCH | :44 | `SCRATCH.md` | `:239` ✅ | 6b `:61` ✅ | ✅ SCRATCH committed on all 13 BROCK session days since 10/2 |
| 1 STATUS + §Standing Obligations + CURRENT catch-up | :45 | `STATUS.md`, `catchups/INDEX.md` → CURRENT | `:235`, `:240-241` ✅ | 6 `:60` ✅ | ✅ INDEX CURRENT = `catchups/2026-10-30.md`; "check at every boot" obligation (FORUM-5 W2) carried `STATUS.md:34` |
| 2 LESSONS | :46 | `LESSONS.md` | `:236` ✅ | 11 (append) | not receipted in 10/30 boot line (receipt names predictions/ledger/R1/inbox only) — 🟡 cannot confirm |
| 3 PREDICTIONS scoped + ledger_staleness | :47-48 | PREDICTIONS (scoped) | `:237`, `:244` ✅ | 7a `:63` ✅ | ✅ 10/30: *"predictions — no OPEN/STUCK row past Resolve_Date; ledger staleness rc 0"* |
| 4 dashboard | :49 | dashboard.py | `:245` ✅ | — | ✅ *"Dashboard 09:06: HY OAS 314 [10/28] …"* |
| 5 WALTER lane | :50-53 | `inbox/WALTER/*.md`, `board_log.tsv` (grep) | `:238`, `:242` ✅ | append + `git mv` | ✅ *"drain 0/0"*; lane empty today |
| 5b R1 corrections | :54 | `corrections_boot_check.py` | `:233`, `:243`, `:246` ✅ | receipts | ✅ *"R1 corrections rc 0 (0 unreceipted)"*. (On 10/21 it was **skipped** — self-sweep row 28: *"Skipped boot controls this morning (bounded spawn): git pull, LESSONS read, PREDICTIONS scan, dashboard, R1 corrections check"*, `reports/2026-10-21_self-sweep.md`) |

Attestation: `ATTESTATION BROCK … manifest-complete BROCK:0-5b … 2026-10-02` (`READS.tsv:247`) — **second filing, after 0b was added**. ✅ The prior 🔴 three-way disagreement is resolved at all three surfaces.

**CLOSEOUT** (`CLAUDE.md:59-72`)

| Step | Line | Tier | Executed? |
|---|---|---|---|
| 6 STATUS write-back + catchups + bytes-not-lines + audit-by-obligation | :60 | ALWAYS | ✅ 10/30 packet: *"STATUS is back under 70% of budget (`read_cap_check.py` rc 0). Two done obligation rows were compacted, with verbatim originals in `catchups/2026-10-30.md` § Rotated"* (`PROME/inbox/processed/2026-10-30_from-BROCK_L795-CABO-weekly.md:35`) |
| 6b SCRATCH rewrite | :61 | ALWAYS | ✅ (above) |
| 6c `brock_selfcheck.py` | :62 | ALWAYS | ✅ *"`brock_selfcheck.py` CLEAN after one fix: the FIRED marker on GATE-BRK-R2 in the new BOTTOM LINE"* (same packet `:35`) — the guard **caught a real propagation miss in the session that wrote it**. Receipts live in PROME packets, not catch-ups (0 "selfcheck" hits in 11 of 13 catch-ups) |
| 7a predictions disposition | :63 | ALWAYS | ✅ BRK-10 resolved 10/29 on its invalidation clause (`STATUS.md:109`) |
| 7b workbook | :64 | SCALED | ✅ KB-BRK-409 (10/30) |
| 8 forward state → `docket/CATALYSTS.tsv` | :65 | SCALED | ✅ CATALYSTS rows 11/05 + 11/13 added 10/30 (SCRATCH `:5`); **now present tense** — prior "Phase 2 will replace" wording is gone |
| 9 research + retirement rule | :66-67 | SCALED | 🟡 retirement sweep owed: self-sweep row 23 counted *"34 files in domain/sources + research >60 days old"*; `domain/sources/` still holds 23 undated-prefix (pre-Aug) files |
| 10 cross-agent packets | :68 | SCALED | ✅ |
| 11/11b promotion + memory check | :69-70 | SCALED / conditional | not assessed |
| 12 git + pre-commit status check | :71-72 | ALWAYS | ✅ commits land same-day (git log) |

**Surfaces maintained with NO charter step (practice without rule — the prior 🔴's class):**
- 🟠 **`NEXUS_BRIEF.md`** — zero mentions in `CLAUDE.md` (grep `NEXUS_BRIEF|NEXUS` → no hits), not in the FILES table, yet updated on 6 days since 9/17 (09-25, 10-09, 10-14, 10-15, 10-25, 10-29) and **read whole at NEXUS boot 6** (`AGENTS/NEXUS/CLAUDE.md:105`; read_cap owner notice). Today it is correct (58/70); the wiring that keeps it correct is habit. 10/29 commit subject *"NEXUS_BRIEF pinned to STATUS df2cbea74"* shows the desk does pin it — the rule just isn't written.
- 🟡 `MAINTENANCE.md` — deliberately unwired (*"Do not wire it into the every-session closeout"*, `MAINTENANCE.md:11`): a declared choice, not a gap.

**Charter FILES table (`CLAUDE.md:246-271`) vs tree:** partially repaired 10/2 — now lists `catchups/`, `SCRATCH.md`, `scripts/brock_selfcheck.py`, `workbook/LEDGER_GLOB`, `docket/CATALYSTS.tsv` (`:251-255`). **Still absent (11):** `NEXUS_BRIEF.md`, `MAINTENANCE.md`, `LAST_COMPLETION.md`, `board_log.tsv` (boot step 5's dependency), `registry/`, `tools/`, `reports/`, `research/`, `workbook/{PC_REDEMPTION_REGISTER,PUBLISHED,PREDICTIONS_SCOREBOARD,PREDICTIONS_ARCHIVE,RESEARCH_INDEX.md}`, `trade/CROSS_ANALYSIS.md`+`APO/`, `outbox/delivered/`. **Mis-described (4):** `trade/TRADE.md` *"Trade targets derived from BROCK analysis"* (`:256`) — file is 🧊 FROZEN 7/27; `trade/NAMES.md` (`:257`) — HISTORICAL-bannered 10/14; `BANK_BDC_MATRIX.tsv` *"Bank ↔ BDC exposure mapping"* and `BDC_CASH_COVERAGE.tsv` *"tracking"* (`:266-267`) — both FROZEN.

**Doc Ownership table internal contradiction:** 🟠 `CLAUDE.md:141` — *"**outbox/** | Cross-agent signals (one file per signal). Acute/threshold/resolution/insight only — see Outbox Protocol"* — contradicts `:83` (*"requests for PROME action only"*), `:94` (*"SIGNALS … → WALTER"*) and `:271`. No "Outbox Protocol" heading exists in the file (grep: the only hit is `:141` itself). This is surviving residue of the exact route-around-WALTER defect the desk corrected on 9/3 (`:94`).

**Charter template rules that are stale or unexecuted:**
- 🟡 `CLAUDE.md:186-189` EXIT §4 Time-Based: *"Q2 2026 earnings = next major resolution event (~late April/May)"*, *"If no new stress signal by Jun 2026, reassess thesis freshness"* — dated template lines from March, past; STATUS §4 (`:105-110`) has replaced them with prediction-linked reads, but the charter still *requires* them. *"Review all predictions quarterly"* (`:187`) has no visible execution artifact (`workbook/PREDICTIONS_SCOREBOARD.md` mtime 7/09 — R2's cluster).
- 🟡 `CLAUDE.md:156` *"Required columns: `| Vector | Score | Current State | Threshold → Next Level | Last Updated |`"* vs actual `| Vector | current | Δ | Threshold → next level | Rescored |` (`STATUS.md:64`). Actual is better (Δ + per-vector rescore date); the charter spec lags it.
- 🟡 `CLAUDE.md:62` 6c is numbered before 7a/7b but must run after them (*"Run it AFTER 7a/7b write-back"*) — ordering wart, mitigated by the inline warning.


## D. Byte / read-cap

Tree before scripts: `git status --porcelain -- AGENTS/BROCK/` → empty (13:19:08 EDT). After `read_cap_check`, `brock_selfcheck`, `ledger_staleness --quiet`: empty (13:19:18 EDT). No script wrote to the tree.

**`python3 scripts/read_cap_check.py --agent BROCK` (root tool), rc=0 — key lines verbatim:**
```
READ-CAP [BROCK] — cap 54,250 B · budget 32,550 B (60%) · … perimeter: DECLARED in PROME/registry/READS.tsv — 17 cap-bearing (whole/programmatic) measured, 6 declared-not-counted … ATTESTED by the desk itself
  ✅ AGENTS/BROCK/LESSONS.md              23,596 B    72% of budget    (whole · BROCK:2)
      ↳ 70–75% BAND — … if this surface was JUST ROTATED it is NOT finished and owes 812 B more … if it has never breached 75%, NOTHING is owed. … ⚠️ Headroom to the trigger: 816 B.
  ✅ AGENTS/BROCK/STATUS.md               22,729 B    70% of budget    (whole · BROCK:1 · ALSO read whole by NEXUS:6, REGINALD:CLAUDE.md-Boot-9)
  ✅ AGENTS/BROCK/catchups/INDEX.md        4,929 B    15% of budget    (whole · BROCK:1)
  ✅ AGENTS/BROCK/SCRATCH.md               1,432 B     4% of budget    (whole · BROCK:0b)
  ▣ AGENTS/BROCK/catchups/*.md … 13 member(s) measured, 0 over budget, 0 over the CAP, largest 15,392 B (47% of budget)
  ◦ AGENTS/BROCK/workbook/PREDICTIONS.tsv 56,215 B  declared `scoped`
  ◦ AGENTS/BROCK/board_log.tsv        154,003 B  declared `grep`
  ℹ️  charter AGENTS/BROCK/CLAUDE.md = 31,274 B — OUT OF PERIMETER by rule 20 unless declared; injection UNCONFIRMED; explicit-read runtime coverage NOT assessed
     ✅ AGENTS/BROCK/NEXUS_BRIEF.md          15,715 B    48% of budget  under 75% of budget  ← read whole by NEXUS:6
READ-CAP-RESULT v1 mode=agent rc=0 … reads=17 over_budget=0 over_cap=0 manifest_defects=0 advisories=1 … rotation_due=0 … charter_bytes=31274
```
Other two scripts: `brock_selfcheck.py` → *"gates with FIRE RECORD: GATE-BRK-R2 · resolved predictions: 5 · matrix rows: 14 / CLEAN — covers only checks 1a/1b/2/3"* rc=0. `ledger_staleness.py BROCK --quiet` → *"13 ledger(s) scanned; 4 TSV(s) NOT scanned by this pass: registry/corrections_receipts.tsv, research/2026-10-14_wave/fsk_may8_commitments.tsv, research/2026-10-29_arcc-mfic-shared/PAIRS.tsv, research/NDFI_BANK_LEVEL_Q4_2025.tsv"* rc=0.

**Rotate-tier surfaces:**

| Surface | 9/17 | Now | Rule | Verdict |
|---|---|---|---|---|
| `STATUS.md` | 31,963 B (98%) | **22,729 B (70%)** | charter: *"keep STATUS under 70% of budget"* (`CLAUDE.md:60`, `:124`) | ✅ in compliance by **56 B** (70% = 22,785 B). Every session now ends with a rotation to get back under — 10/30 *"STATUS rotated back under 70%"*. The margin is structural, not slack: this is the next likely breach |
| `LESSONS.md` | 31,469 B (97%) | **23,596 B (72%)** | root rotate at ≥75% to <70% | ✅ CLOSED as a breach (rotated 10/2 to 21,535 B = 66%, `MAINTENANCE.md` 10/2 item 7); regrowth +2,061 B in 4 weeks (#37–#39), **816 B to the 75% trigger** — one more long lesson trips it |
| `SCRATCH.md` | 46,122 B (142%) | 1,432 B (4%) | overwrite-only | ✅ |
| `CLAUDE.md` (charter) | 24,688 B (76%) | **31,274 B (96%)** | root Data Hygiene: *"any surface a boot protocol tells a session to READ WHOLE stays under 32,550 B"*; COMPLETION_SPEC requires the explicit read, and the desk receipts it (*"BROCK CLAUDE.md 6 [pages] … all to eof"*, `catchups/2026-10-30.md:5`) | 🟠 **1,276 B headroom; not under any guard** — the tool rules it OUT OF PERIMETER (rule 20) and `READS.tsv:230` declares it `boot-defining`, not `whole`. Growth: +5,919 B on 10/2 (`22092d059`, CREED adoption: traps + new steps) then +667 B through 10/23 (incl. DAEDALUS WQ-508 harness line `d3488e641`). The always-loaded traps block was the right call; the charter carries ~3 KB of history prose (e.g. `:70` alone is 2,164 chars of memory-check incident narrative) that the root *"Rules only"* model would move to a provenance file |
| `NEXUS_BRIEF.md` | 34,501 B | 15,715 B (48%) | NEXUS reader's perimeter | ✅ (rotated 10/9 → `archive/NEXUS_BRIEF_ROTATED_2026-10-09.md`) |

Not cap-bearing but large: `docket/CATALYSTS.tsv` 49,425 B (152%) — +20 KB since 9/17 (29,434 B); not a boot read, so no breach; self-sweep row 21 counted *"13 past-dated rows with no CLOSED/RESOLVED marker … row 41 is blank"* (R2/R3 to verify current state).


## E. Prior-profile reconciliation (cluster items: §4 DEBT + §7 questions)

| Prior item (profile line) | Verdict | Receipt |
|---|---|---|
| §4 🔴 **SCRATCH claimed at both ends, wired at neither** (`profiles/BROCK.md:96`) | **CLOSED** | Boot 0b `CLAUDE.md:44`; closeout 6b `:61`; symmetry line `:36`; `READS.tsv:239` (added 10/2); re-attestation `READS.tsv:247` 2026-10-02; SCRATCH committed on 13/13 BROCK session days since 10/2; 46,122 → 1,432 B, old body `archive/SCRATCH_PRESPLIT_2026-10-02.md`; its 12 live debts moved to `STATUS.md:30-44` |
| §4 **STATUS 98% / LESSONS 97% rotate-tier** (`:95`) | **CLOSED (both), margins thin** | STATUS 22,729 B = 70% (56 B under the charter's own 70% line); LESSONS 23,596 B = 72%, 816 B to the 75% trigger (read_cap_check, D). Boot rotate-tier load 63,432 B → 46,325 B |
| §4 **No `thesis/` layer** (`:94`) | **OPEN, unchanged** | `git ls-files AGENTS/BROCK/thesis` = 0; `MAINTENANCE.md:8` still *"BROCK has no `thesis/CHANGELOG.md` yet"*; backlog #3 still *"Deferred Tier-2"*. **Consequence has sharpened:** the THESIS-KILL DECISION TREE now lives only in a superseded catch-up (F2) — exactly the "traced through STATUS prose … rotated" risk the prior profile named |
| §4 **`docket/CATALYSTS.tsv` future tense, unwired, unlinted** (`:97`) | **CHANGED → mostly CLOSED** | Future-tense line gone; now *"Dated catalysts live in `docket/CATALYSTS.tsv`; STATUS carries only owed/near items"* (`CLAUDE.md:65`) and FILES row `:255`. In `LEDGER_GLOB`. Not boot-read **by design** (STATUS §Standing Obligations carries near items). Grew 29,434 → 49,425 B. `date_class` lint + 13 past-dated open rows (self-sweep row 21) → R2/R3 |
| §4 **`domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md` silent rot** (`:98`) | **CLOSED** | `> **HISTORICAL — banner added October14,2026.** April2 cascade narrative is historical…` (`:1`) |
| §4 🔴 **Three live prediction counts disagree / SCOREBOARD 7/09** (`:99`) | **Out of my cluster (R2)** — one architectural datum | The desk **declined** the scoreboard on 10/2: *"Predictions scoreboard and evals: low value now"* (`MAINTENANCE.md` 10/2 "Deliberately NOT adopted") — but `MAINTENANCE.md` backlog row #1 still reads *"Do first (incremental)"* (F5) |
| §4 **NEXUS_BRIEF superseded composite 59/70** (`:100`) | **CLOSED (number) / CHANGED (wiring)** | `NEXUS_BRIEF.md:6` *"Convergence **58/70**, last rescore **9/25**, unchanged"* = `STATUS.md:83`; As-of 2026-10-29T00:08, pinned to STATUS `df2cbea74`. But no charter step names the brief (C) |
| §4 **EXPECTED_SIGNALS `Last reviewed: 2026-03-06`** (`:101`) | **OPEN, worse** | Still `Last reviewed: 2026-03-06` (`:5`); last git touch 2026-03-06 `d78a9eb2a` (238 days). Read in full this pass: its bands now **contradict the live matrix and the desk's own Standing Trap 1** (F1) |
| §4 **`trade/NAMES.md` `Last Updated: 2026-05-01`** (`:101`) | **CLOSED** (banner) / FILES table still says live | `> **HISTORICAL — banner added October14,2026.** May1 ranking is historical…` (`trade/NAMES.md:1`); but `CLAUDE.md:257` still describes it as the live tier list |
| §4 **FILES table behind tree** (`:102`) | **CHANGED — partial** | 5 rows added 10/2 (`CLAUDE.md:251-255`); 11 entries still absent incl. `board_log.tsv` and `NEXUS_BRIEF.md`; 4 rows mis-describe FROZEN/HISTORICAL files (C) |
| §4 **`workbook/LEDGER_GLOB` absent** (`:103`) | **CLOSED** | `workbook/LEDGER_GLOB` = `workbook/*.tsv docket/*.tsv` (28 B, 10/2); FILES row `CLAUDE.md:254`; `ledger_staleness` *"13 ledger(s) scanned"* rc 0 |
| §7 Q1 **Is SCRATCH boot-read?** (`:129`) | **ANSWERED: yes, 0b** | as row 1 |
| §7 Q2 **Is the APO Dec $95P still live?** (`:130`) | **Desk's answer (off-repo truth, not resolved):** *"FORGE 10/14: Dec18 $95P ×1, exact capture/mark time UNKNOWN"* | `STATUS.md:97` |
| §7 Q3 **BRK-02 basis (cost vs FV)** (`:131`) | **CLOSED — RESOLVED-FALSE 10/2** on the resolver of record, Octus industry aggregate **at cost** 1.90% from 2.02% | `catchups/2026-10-22.md` § Rotated; `STATUS.md:50`, `:106`; KB-BRK-312 |
| §7 Q4 **9/18 CRMT date on BROCK's own docket?** (`:132`) | **MOOT — read executed, row never added** | `CATALYSTS.tsv` has no 2026-09-18 row (only `2026-09-15` X1 review in that window), but the 9/18 read happened: *"My 9/18 12:06 ET silence grade was overtaken 8 hours after it was written"* (`LAST_COMPLETION.md` RESULT ①); CRMT now runs as a STATUS obligation through bridge 8 (`STATUS.md:12`) |
| §7 Q5 **What does EXPECTED_SIGNALS still govern?** (`:133`) | **ANSWERED: nothing live; and it contradicts what does** | Only references: `CLAUDE.md:142`, `:259`, `ARCH_REPORT_2026-06-26.md`, KB/board_log rows — no STATUS / workbook / script cite (grep). See F1 |
| §7 Q6 **SCOREBOARD cadence** (`:134`) | **ANSWERED by owner: declined 10/2** ("low value now") — R2 to grade | `MAINTENANCE.md` 10/2 entry |

**Prior DO-NOT-TOUCH items re-checked (`profiles/BROCK.md:107-119`):** Independence map ✅ intact verbatim (`STATUS.md:81`); `trade/TRADE.md` FROZEN ✅ (`:1`); two-clock headers — not re-read (R2/R3); never-read-whole rule ✅ intact (`CLAUDE.md:47`, `:51`); `git mv` consume ✅ (`:52-53`); pre-commit check ✅ *corrected 10/14* to forbid altering others' staging (`:72`); SIGNALS→WALTER ✅ (`:94`) — but contradicted by `:141` (C); BRK-xx ids ✅ (`:126`); cessions ✅ (`:205-210`). **THESIS-KILL DECISION TREE 2-of-3 — rule text intact but MOVED off the boot path (F2).** **§9 TRIGGER LADDER pointer chain — broken (F2).**


## F. New findings since 9/17 (ranked) + better-than-blueprint

### Findings

| # | Sev | Finding | Evidence |
|---|---|---|---|
| F2 | 🔴 | **The THESIS-KILL DECISION TREE (2-of-3 reversals override) and the §5 TRIGGER LADDER pointer were rotated off the boot path into a superseded catch-up, and the frozen-file pointer that routes to them is now false.** STATUS keeps only a pointer: *"§5. TRIGGER LADDER and THESIS-KILL STEP-2 check … rotated verbatim → `catchups/2026-10-22.md` § Rotated. ⚠️ STEP 2 still applies only once the literal kill fires"*. The rule text (*"STEP 2 needs 2 of 3 reversals to override"*) now exists only at `catchups/2026-10-22.md:38` — a SUPERSEDED catch-up, not a boot read. Charter Doc Ownership says catchups hold narrative and *"Does NOT contain … Current state or owed actions"* (`CLAUDE.md:134`). Chain for BRK-25/26 (`Action_If_Falsified` = *"… (TRADE.md §9)"*, resolve 12/31): `trade/TRADE.md:5` says §9 was migrated into *"`STATUS.md` § "EXIT RULES → 5. TRIGGER LADDER", which is now its only live home"* — STATUS no longer holds it → catch-up 10/22 → `archive/STATUS_ROTATED_2026-09-02.md`. **Four hops ending in archive.** The rotation was the desk's own recommendation for bytes: self-sweep row 20 *"Rotate by obligation (e.g. the 8/28 decision-tree paragraph → catch-up)"* (`reports/2026-10-21_self-sweep.md`). Near-term impact LOW (HY 314 [10/28] vs the 260 kill, `STATUS.md:92`); the defect is that a rule the prior profile listed DO-NOT-TOUCH now has no live home — the `thesis/` gap (E) made concrete. | `STATUS.md:112`; `catchups/2026-10-22.md:36-38`; `trade/TRADE.md:5`; PREDICTIONS BRK-25/26 col 9 |
| F1 | 🟠 (🔴 by the letter) | **`EXPECTED_SIGNALS.md` — the charter-named owner of *"Signal interpretation methodology + thresholds"* (`CLAUDE.md:142`, `:259`) — contradicts the live thresholds on three metrics and the desk's own Standing Trap 1.** (a) PIK: *">25% … RED, alert REGINALD"* (`EXPECTED_SIGNALS.md:19`) and *"PIK >20% at FSK or ARCC"* with no denominator (`:122`) vs charter route *"PIK rises above **20% of TOTAL INVESTMENT INCOME** at FSK or ARCC → REGINALD 🟠"* (`CLAUDE.md:223`) vs matrix next level *"Industry median >20% sustained"* (`STATUS.md:68`). (b) Non-accruals banded *"at Fair Value"* (`:46`) while Trap 1 names the cost/FV divergence (`CLAUDE.md:24`) and the desk reads and resolved BRK-02 **at cost** (`STATUS.md:50`). (c) NAV discount RED at *">-20%"* (`:78`) vs 🔴(4) with next level *">35% median sustained"* (`STATUS.md:69`). Unreviewed 238 days; no live surface cites it (grep). Impact is latent (no step reads it); a cold reader following the Doc Ownership table gets wrong bands. | `EXPECTED_SIGNALS.md:5,19,46,78,122` |
| F3 | 🟠 | **Glued words on the canonical STATUS surface — a root Output Canon violation (*"never glue words together to save bytes"*), introduced by the OpenAI Codex sessions.** 28 glued tokens on 12 STATUS lines, e.g. *"RJ sector32% as ofOctober8"* (`:99`), *"NextSept30semiannual"*, *"completedOctober14"*, *"satisfactionUNKNOWN"* (`:38`), *"give17.23%"*, *"5of6 NAVs/4of4"* (`:53`), *"other13"* (`:14`), *"all11"* (`:54`), *"August7"*, *"March31"* (`:41`, `:107`). `git log -S` attributes each sampled token to a Codex-session commit: `c95847c8a` 10/14 (ofOctober8, give17.23%), `44b8237bd` 10/14 (satisfactionUNKNOWN), `4e46f3e39` 10/25 (other13, all11). Also `gross87.0`, `October10 fire`, `March31 weights` → `c95847c8a`/`4e46f3e39` (10 tokens sampled, all Codex-origin). Same style on the 10/14 HISTORICAL banners (*"October14,2026"*, `LAST_COMPLETION.md:1`, `trade/NAMES.md:1`, `OPEN_ITEMS_2026-09-03.md:1`, tracker `:1`). **And it is propagating into the Claude runtime by imitation:** the BOTTOM LINE heading *"October29 (HTGC print)"* came in with Claude commit `f7c0d3f9e` (10/29) and *"October30 (CABO weekly read)"* (`STATUS.md:116`) with Claude commit `7f16f99a6` (10/30). Origin runtime-correlated → a PROME runtime-mechanics item; spread → an owner cleanup + a trap-style line. | `STATUS.md:14,22,34,37,38,41,53,54,58,99,107,116` |
| F4 | 🟠 | **Charter at 96% of budget and unguarded.** 31,274 B; read whole every boot by explicit read (receipted, `catchups/2026-10-30.md:5`) but OUT OF PERIMETER for `read_cap_check` (rule 20; `READS.tsv:230` = `boot-defining`). +6,586 B since 9/17. ~3 KB is incident history the root "Rules only" model would move out (`CLAUDE.md:70` alone = 2,164 chars). | D |
| F5 | 🟠 | **`NEXUS_BRIEF.md` maintained by habit, no charter step** — read whole at NEXUS boot 6; zero `CLAUDE.md` mentions; absent from FILES. Same class as the prior SCRATCH 🔴, currently harmless because the desk does it. | C |
| F6 | 🟠 | **Doc Ownership row contradicts the routing rule**: `CLAUDE.md:141` *"outbox/ \| Cross-agent signals (one file per signal) … see Outbox Protocol"* vs `:83`, `:94`, `:271`; the cited "Outbox Protocol" heading does not exist. Residue of the 9/3-corrected route-around-WALTER defect. | `CLAUDE.md:141` |
| F7 | 🟠 | **Byte pressure is now the desk's dominant architectural force.** STATUS sits 56 B under its 70% line and each session ends with a rotation (10/30 *"STATUS rotated back under 70%"*, `catchups/2026-10-30.md` §Other); F2 is a rotation of a live rule; F3's gluing is plausibly byte-saving (**INFERRED** — no commit says so). The structural relief the desk itself registered (`thesis/` layer, backlog #3) is the one not built. | `MAINTENANCE.md` backlog #3 |
| F8 | 🟡 | **DAEDALUS 10/8 asks, due "by Fri 10/30", not worked** — *"⚠️ NOT worked 10/30 (L795 session scope); carried to the 10/31 R2 session"* (`STATUS.md:27`). Carried with a reason and a date, so honest; DAEDALUS's wiring-17 run #4 packet (`inbox/2026-10-30_from-DAEDALUS_wiring-17-run4.md` row 2) already flags that the Medallia leg of this row was delivered 10/14. | `STATUS.md:27`; `catchups/2026-10-30.md` §Other |
| F9 | 🟡 | **`MAINTENANCE.md` change-log stopped at 10/2** though its own trigger (*"Touch it only when a session changes BROCK's structure — a doc/folder/script created/retired/moved"*, `:11`) fired at least 3× since: `reports/` created 10/21; HISTORICAL banners on 4 files 10/14; NEXUS_BRIEF rotation 10/9; pre-commit rule corrected 10/14 (`CLAUDE.md:72`). Backlog table not re-ranked after 10/2 although #1 (*"Do first"*) was declined and #2 (`boot.py`) was argued against (*"CREED's `boot.py`: retired by CREED"*) in the 10/2 entry. | `MAINTENANCE.md:11`, backlog rows 1-2 |
| F10 | 🟡 | **Charter FILES table** — 11 absent, 4 mis-described (C). | `CLAUDE.md:246-271` |
| F11 | 🟡 | **Stale charter template rules** — EXIT §4 Time-Based dated Apr/Jun 2026 (`CLAUDE.md:186-189`); matrix required-columns spec lags actual (`:156` vs `STATUS.md:64`). | C |
| F12 | 🟡 | **Retirement candidates** (root Data Hygiene: >60 d, not boot-read, no live ref): `OPEN_THREADS_2026-07-09.md`, `ARCH_REPORT_2026-06-26.md` (no banner, no live ref by grep); 15 pre-9/3 signal files to non-PROME desks at `outbox/` top level; 23 pre-August files in `domain/sources/` (self-sweep row 23 sweep still owed). | B |
| F13 | 🟡 | **Un-typed clock in stamps**: `STATUS.md:3` *"2026-10-30T09:1x-04:00"*, `SCRATCH.md:1` *"~09:1x ET"* — the `finding_a_stamp_written_from_narrative_drifts_from_the_wall_clock` form. | `STATUS.md:3` |

### Refuted predictions (results)
- SCRATCH still unwired — **refuted** (C, E).
- NEXUS composite still drifting from STATUS — **refuted** (58/70 both).
- Convergence arithmetic wrong — **refuted**; I re-summed to 58.
- Charter memory path (`~/.claude/projects/-home-willi-Research-workspace/memory/`, `CLAUDE.md:69`) disagrees with root `memory/auto/` — **refuted**: it is a symlink to `/home/willi/Research-workspace/memory/auto`.
- 10/30 drain missed the three pending top-level inbox packets — **refuted**: all three arrived after the 09:05–09:2x session (git log orders the VULCAN 10:19 commit after BROCK's; DAEDALUS packets 12:37 and 13:01).
- 10/30 wake skipped boot controls — **refuted** for 10/30 (receipt line); **confirmed** for 10/21 by the desk's own self-sweep row 28.

### Better than blueprint (new ✅ and retained)
1. ✅ **NEW — §STANDING TRAPS always loaded, with an admission rule**: *"A trap earns a place only by having bitten BROCK while writing a number. The block is curated, not a dumping ground"* (`CLAUDE.md:22`); each trap cites its LESSONS number.
2. ✅ **NEW — `brock_selfcheck.py` was falsified before adoption and catches real misses in production**: v1 *"MISSED VX-BRK-004 on the pre-fix files and was replaced"* (`MAINTENANCE.md` 10/2 item 5); on 10/30 it caught a missing FIRED marker on GATE-BRK-R2 in the new BOTTOM LINE (PROME packet `:35`). Its CLEAN line declares its own scope (*"covers only checks 1a/1b/2/3"*).
3. ✅ **NEW — Standing Obligations with a no-rotation clause**: *"An owed action leaves this table only by being DONE or by its owner's ruling, never by a rotation"* (`STATUS.md:8`) + closeout *"audit by OBLIGATION, not bytes"* (`CLAUDE.md:60`); the 10/2 split was audited at 28 owed-item tokens.
4. ✅ **NEW — date-free boot pointer**: *"read the CURRENT catch-up named in `catchups/INDEX.md` (this step names no date, so it cannot go stale)"* (`CLAUDE.md:45`).
5. ✅ **NEW — per-session runtime receipt** in every recent catch-up, across both runtimes (A).
6. ✅ **NEW — owner self-sweep** `reports/2026-10-21_self-sweep.md`: 28 ranked rows with VERIFIED/INFERRED tokens and a *"Nothing found broken in"* section; STATUS shows most rows since executed (BRK-31 reads done 10/25 `STATUS.md:14`; CFG basis KB379 `:14`; CCC/BB refreshed KB-BRK-360 `:18`; R1 rc 0 on 10/30).
7. ✅ **NEW — "Deliberately NOT adopted, with reasons"** list in the CREED adoption entry (`MAINTENANCE.md` 10/2), e.g. *"CREED's `boot.py`: retired by CREED (it keyed freshness on mtime)"*.
8. ✅ **NEW — the two-state rule applied to documents**: HISTORICAL banners 10/14 on `LAST_COMPLETION.md`, `OPEN_ITEMS_2026-09-03.md`, `trade/NAMES.md`, `domain/PRIVATE_CREDIT_CONTAGION_TRACKER.md`.
9. ✅ **NEW — pre-commit rule corrected to protect others' staging** (*"Preserve unexpected staging belonging to other owners; do not unstage or otherwise alter it"*, `CLAUDE.md:72`).
10. ✅ Retained: Independence map (`STATUS.md:81`); per-vector Δ + Rescored columns; ALWAYS/SCALED tiers + Live-event override with two clamps (`CLAUDE.md:38`); declared and attested READS manifest (19 rows); `TRADE.md` freeze banner (pointer now false, F2).


## G. Route list (ranked)

| Rank | To | Item | Ask (one line) |
|---|---|---|---|
| 1 | **BROCK owner** | F2 kill tree + §9 pointer | Give the THESIS-KILL DECISION TREE (2-of-3) and the trigger-ladder pointer a live home (STATUS §5 as a 2-line rule, or the charter EXIT section, or a `thesis/` stub) and fix `trade/TRADE.md:5`'s "only live home" line in the same commit; keep the 10/22 catch-up as history |
| 2 | **BROCK owner** | F1 EXPECTED_SIGNALS | Freeze it with a HISTORICAL banner pointing to VX.tsv/STATUS as threshold owners and re-point `CLAUDE.md:142`/`:259`, **or** re-band PIK (TII basis, 20%), non-accruals (cost basis) and NAV discount (35% median) to match live — owner's choice; not both live |
| 3 | **BROCK owner** | F3 glued words | One mechanical pass on STATUS (28 tokens, 12 lines) + the four 10/14 banners; candidate Standing Trap or SCRATCH line so the style stops propagating |
| 4 | **PROME** | F3 runtime correlation | Codex-runtime sessions (10/14, 10/25) introduced the gluing; root Output Canon already forbids it — ask whether `PROME/ORCHESTRATION_PLAYBOOK.md` § Runtime mechanics should carry an explicit Output-Canon reminder for non-Claude desks (fleet-level, not BROCK-only) |
| 5 | **BROCK owner** | F6 + F10 + F11 charter text | Fix `CLAUDE.md:141` outbox row; bring FILES table to tree (add NEXUS_BRIEF, MAINTENANCE, board_log, registry, tools, reports, research, workbook extras; mark TRADE/NAMES/2 ledgers FROZEN/HISTORICAL); retire dated EXIT §4 template lines; align matrix column spec to actual |
| 6 | **BROCK owner** | F5 NEXUS_BRIEF | Add one closeout line (SCALED: refresh + pin to STATUS commit when the composite, a gate or a resolution changes) and a FILES row |
| 7 | **BROCK owner** + **DAEDALUS** | F4 charter 96% | Owner: move incident narrative (e.g. `:70`, `:94` 9/3 history, `:172-175` WQ-106 history) to a provenance file per root "Rules only". DAEDALUS: decide whether `read_cap_check` should grade explicitly-read charters (rule 20 currently exempts them while COMPLETION_SPEC mandates the whole read) — fleet tooling question |
| 8 | **BROCK owner** | F9 MAINTENANCE | Log the 10/9, 10/14, 10/21 structural changes; re-rank backlog (#1 declined, #2 argued against, #3 now urgent per F2/F7) |
| 9 | **BROCK owner** | F12 retirement | `git mv` `OPEN_THREADS_2026-07-09.md`, `ARCH_REPORT_2026-06-26.md`, pre-9/3 non-PROME outbox files, eligible pre-August `domain/sources/` → `archive/` (after live-ref check) |
| 10 | **DAEDALUS-side** | F8 | Expect the 10/8 asks at the 10/31 R2 session; reconcile with wiring-17 run #4 row 2 (Medallia already delivered) so BROCK isn't asked twice |
| 11 | **DAEDALUS-side** | profile | Retire prior §4 bullets CLOSED in E (SCRATCH, rotate-tier, tracker, NEXUS composite, LEDGER_GLOB, NAMES banner); keep `thesis/` as the standing structural gap with F2 as its live consequence; new staleness legs: `grep -c '2 of 3 reversals' AGENTS/BROCK/STATUS.md` (F2 fix), `sed -n 5p AGENTS/BROCK/EXPECTED_SIGNALS.md` (F1), STATUS ≥75% |
| 12 | **DAEDALUS-side** | F13 | none — note only |


## H. Coverage

| Surface | Read | Ranges / method |
|---|---|---|
| `AGENTS/DAEDALUS/profiles/BROCK.md` | **whole** | 1-135 (via saved tool output, final line 135 seen) |
| `AGENTS/BROCK/CLAUDE.md` | **whole** | 1-80, 80-179, 180-271 (final line 271 seen) |
| `STATUS.md` | **whole** | 1-60, 60-116 (final line 116 seen) |
| `SCRATCH.md` | **whole** | 1-15 |
| `LAST_COMPLETION.md` | **whole** | 1-29 |
| `MAINTENANCE.md` | **whole, lines truncated at 450 chars** | 1-68; long lines' tails not read |
| `LESSONS.md` | **part** | 1-30 (cut 600 chars), heading/entry index (all), 56-88 (cut 260/500 chars) — structure + #31–#39 heads, not every body in full |
| `NEXUS_BRIEF.md` | **part** | 1-20 (cut 500), all `#`/convergence lines |
| `EXPECTED_SIGNALS.md` | **part** | 1-12, 11-22, 46-56, 71-79, all `###`/threshold lines; git log |
| `OPEN_ITEMS_2026-09-03.md`, `OPEN_THREADS_2026-07-09.md`, `ARCH_REPORT_2026-06-26.md` | heads | 1-8 each + banner grep + live-ref grep |
| `reports/2026-10-21_self-sweep.md` | **most** | 1-40 (cut 330 chars) |
| `catchups/` | list + INDEX whole (cut 300) + `2026-10-30.md` (whole, lines cut 500) + `2026-10-29.md` (grep) + `2026-10-22.md:28-45` + receipt greps across all 13 | |
| `trade/TRADE.md` | 1-9 + §9 grep | |
| `inbox/2026-10-30_from-DAEDALUS_wiring-17-run4.md` | whole | to avoid duplicating its rows |
| `PROME/registry/READS.tsv` | BROCK rows 229-247 + REGINALD row 476 (cut 330) | |
| `PROME/inbox/processed/2026-10-30_from-BROCK_L795-CABO-weekly.md` | grep for closeout receipts | |
| scripts run (root dir) | `read_cap_check.py --agent BROCK` rc0; `brock_selfcheck.py` rc0; `ledger_staleness.py BROCK --quiet` rc0 | tree clean before (13:19:08) and after (13:19:18) |
| `board_log.tsv`, `workbook/PREDICTIONS.tsv`, `workbook/KB.tsv` | **not read** (bytes only; PREDICTIONS cols 1+9 for BRK-25/26 via awk) | per instructions |
| **Skipped** | `scripts/brock_selfcheck.py` source (ran it, grep for writes only), `tools/soi_nonaccrual.py` body, `workbook/*` contents, `docket/CATALYSTS.tsv` contents (one awk filter), `research/`, `domain/sources/`, `archive/`, processed inbox | other readers' clusters (R2/R3) or out of scope |

**Report completed:** Fri 2026-10-30 13:25:55 EDT (`date`). BROCK tree `git status --porcelain -- AGENTS/BROCK/` empty at completion.
