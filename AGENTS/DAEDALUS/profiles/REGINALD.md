<!-- INSTALLED 2026-10-30 by DAEDALUS (whole-profile refresh, seventh of the accepted nine). Mode-A: four Opus readers (R1 architecture, R2 ledgers/guards, R3 flows/review, R4 per-bank tree), read-only, REGINALD never launched or messaged; DAEDALUS re-verified every 🟠 at the artifact. Record: runs/2026-10-30_REGINALD_REFRESH.md; reader reports runs/2026-10-30_REGINALD_REFRESH_READERS/ (index REGINALD_REFRESH_READER_REPORTS.md). Prior body (vintage 2026-08-07 + banners to 10/21) preserved at profiles/_prior/REGINALD_2026-10-30_before_refresh.md (crc32 1434954275). -->
# Agent Profile — REGINALD

**Profile vintage:** 2026-10-30 · **FULLY REWRITTEN: 2026-10-30** (Mode-A, HEAD `9f0975860`; REGINALD not live during the read: last REGINALD commit `9ebedf3e2` 10/30 09:15, `git status -- AGENTS/REGINALD/` clean at every reader's start and end check 16:41–16:52)

**Built by:** DAEDALUS · **Method:** Mode-A, 4 parallel readers over file clusters; synthesis + artifact re-verification by DAEDALUS
**Sources read:** charter whole · STATUS whole · LESSONS, CALENDAR, MEMORY, ROADMAP, SCRATCH, NEXUS_BRIEF, SUB_AGENTS, BANK_RESEARCH_STANDARD whole · cold STATUS_* family, DECK_EVIDENCE, BANK_EXPOSURE_MATRIX (structure + banners) · `thesis/`, `kernel/` · every `registry/` file · `workbook/` headers + every PREDICTIONS row + VX row scan · `scripts/` (boot.py whole, thresholds.py, vx_ladder_check.py, guards) · git since 8/07 · inbox/outbox/`.consumed.tsv` · per-bank `domain/` + `archive/per-bank/` census · `reports/` since 8/07 (frames vs grades) · `research/` vintage census. **Not read:** ~100 October report bodies, `archive/` beyond per-bank, boot.py's network subprocess legs (not run). Exact coverage: each reader's coverage section.
**Staleness:** refresh when ANY fires — (1) the 11/07 Call Report re-score lands (STATUS CONVERGENCE MATRIX scores move off the v2.0 8/20 basis); (2) `STATUS.md:87` "Kill rail re-derived" stamp changes; (3) the count of OPEN predictions leaves **7** (REG-01/03/06/27/28/29/30); (4) `scripts/thresholds.py` gains a non-zero breach exit (the 🟠 guard fix); (5) `read_cap_check --agent REGINALD` leaves rc 1 or the charter leaves 77%; (6) >45 days (→ 2026-12-14).

## 1. Identity

Regional-bank **convergence hub**, the terminus of the credit chain (LABOR → CARL → REGINALD → repricing; AGENTS.md). Single-name depth arrives from specialist desks (OZK, WAL, FLG; GIBBS for the large-bank comparison group), national CRE from CREED, private credit from BROCK, plus the WALTER board lane. **WQ-484 A (Will 10/22) makes it the obliged consumer of OZK and WAL output**, and it does that duty in the checkable form (per-entry ACKs in `AGENTS/{OZK,WAL}/REGINALD_CHANNEL.md`; 66-row `inbox/processed/.consumed.tsv`). Current judgment (STATUS:7, 10/30): stress is *concentrated, not tier-wide*. Signature method: the Hidden-CRE screen (FFIEC Memo Item 3 / RCON2746), whose OZK 37.6% anchor was refuted at the primary 8/07 and is now **KILL-ON-SIGHT in the charter** (`CLAUDE.md:127`).

What changed since the 8/07 profile: the per-bank tree was bannered (8/10) and **retired** to `archive/per-bank/` (8/13, MTB 10/22); THESIS.md and TIMELINE.md were retired to stubs (8/13, 8/20) with STATUS as thesis-canonical; the exit rail was re-derived and dated (10/22); a resolve-by sidecar and a boot past-due check were added; STATUS split into hot STATUS + cold DASHBOARD/MATRIX/BEAR_LEDGER. The 8/07 "went dark 8 days with 15 packets queued" pattern is gone: the last 5 sessions pushed, drained the inbox to zero and re-pinned the NEXUS brief to STATUS HEAD.

## 2. File anatomy — HEAVY (~1,650 files; most in archive/, inbox/processed/, domain/sources/, research/)

| Cluster | State 10/30 (bytes; % of 32,550 B budget) |
|---|---|
| **Charter** `CLAUDE.md` 24,977 B **77% rotate-tier** | +1,637 B from the 10/22 fix commit that applied DAEDALUS's own review; MEMORY:55 "trim pending Will" has no WILL_QUEUE/DOCKET row |
| **Hot boot reads** STATUS 23,487 (72%) · CALENDAR 23,495 (72%) · ROADMAP 23,400 (72%) · MEMORY 17,576 (54%) · LESSONS 13,201 (41%) · SCRATCH 5,257 · BANK_RESEARCH_STANDARD 6,368 | rotated under 70% on 10/28, regrowing (~670 B/day on STATUS) |
| **Cold** STATUS_DASHBOARD **33,571 B (103%)** · STATUS_MATRIX 8,953 · STATUS_BEAR_LEDGER 4,136 · MEMORY_REFERENCE · ROADMAP_BACKLOG | DASHBOARD over budget (not a boot read); three cold banners name re-check dates that lapsed (10/02, 10/14) |
| **Derived** NEXUS_BRIEF 21,619 (pin = STATUS HEAD ✓) · DECK_EVIDENCE 24,091 (FROZEN 7/09, corrections 8/10, 10/10) · BANK_EXPOSURE_MATRIX 24,946 (v2.0 8/20; re-score 11/07) | current-to-vintage |
| `thesis/` THESIS + TIMELINE retired stubs · CHANGELOG 20,270 B, **newest entry 10/12** | no entry for the 10/22 exit-leg retirement or 10/30 L801 |
| `workbook/` 24 files: KB.tsv (257 rows → ML-REG-260, 10/30) · PREDICTIONS.tsv (25 rows) · VX.tsv · FLOW.tsv · 8 cohort TSVs (MI3, NDFI, AOCI, FUNDING, RUNWAY, ACL, CRE_RCN, WORKOUT_OUTCOME_BRIDGE) · 4 orphan feeds FROZEN | `ledger_staleness` rc 0, 16 ledgers; VX row-level rot under a fresh header (§4) |
| `registry/` THRESHOLDS.tsv (9 rows × **13 cols**) · NOTES.md (rationale companion; REG-06 EDGAR instrument) · PREDICTION_RESOLVE_BY.tsv (sidecar; REG-01/06 Kernel-pinned) · REG_T02_EXIT_LOG.tsv · corrections_receipts | live; 7 of 8 `threshold_thesis_ref` anchors dangle |
| `scripts/` 22 tools; `boot.py` orchestrator (0/1/2, fails closed on its builtins) | `thresholds.py` cannot fail (§4) |
| `TRADE.md` (two-clock 10/22, RECONCILED 10/22, §2b no-candidate log) · `POSITIONS.md` (stacked headers :5-11) · `trade/` | one position event behind FORGE (§4) |
| `reports/` 145 · `research/` 267 (incl. `research/EGBN/` copy hub + verifier, `research/FHLB/copies/`) · `earnings_briefs/` · `sources/` | freeze-before-print discipline continuing (4 Q3 frames + checklist; 2 frozen 11/07 protocols) |
| `domain/` 481 (sources mainly) · `archive/` 370 incl. `archive/per-bank/` (EGBN, CFG, ZION, MTB, FITB, PNC, RF) · `archive/sub-agents/` (CREED, BELT) | per-bank layer retired; no README in `archive/` or `archive/per-bank/` |
| `kernel/` REG-01/REG-06 companions + `staged_increment2/` (NOT submitted) | frozen prep, correct posture |
| `inbox/` (+ `WALTER/`, `processed/` with `.consumed.tsv`) · `outbox/` 13 + lifecycle README | 4 unprocessed, all arrived after the 10/30 09:15 close |

## 3. Per-dimension local representation

| Dimension | Local form |
|---|---|
| Current judgment | STATUS:7 head block (dated 10/30). `## BOTTOM LINE` (STATUS:124) is undated, points at 10/20 and is not the last section |
| Convergence matrix | STATUS:35-40 live line + STATUS_MATRIX cold narratives; scores frozen on v2.0 (8/20) until the 11/07 re-score (DOCKET L180) |
| Exit rules | STATUS:85-96, **"Kill rail re-derived: 2026-10-22"**; CBRE leg retired with its definition; CRE anchor re-keyed to WAL-01/02 (NOT FIRED, dated); HY<260 = REVIEW reframe intact |
| Predictions | PREDICTIONS.tsv (10 cols, Kernel-pinned rows) + `registry/PREDICTION_RESOLVE_BY.tsv` sidecar with Anchor_Type; 7 OPEN, resolve-by 2027-01-05…2027-08-09; Brier ≈ 0.19, n = 8 (`reports/2026-10-23_historical-learning-review.md:23`) |
| Thresholds | `registry/THRESHOLDS.tsv` + NOTES.md; live reads in STATUS §THRESHOLD STATUS (REG-T-07 office CMBS 12.16% Sept, secondary) |
| Trade | TRADE.md feeds TERRY; §2b dated "No candidate" log per print cluster (10/22, 10/23, 10/28) implements Will's 10/20 trade-ideas route |
| Signals out | NEXUS_BRIEF (pinned); cited at 10/27–10/29 vintage by NEXUS, LIQUID, BROCK, CARL, FLG, WAL, OZK, CREED |
| Signals in | channel ACKs (OZK, WAL); `.consumed.tsv`; WALTER lane scanned by boot.py |

## 3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)

| Surface | Kind | Stamp | State |
|---|---|---|---|
| STATUS EXIT RULES | STATE | 2026-10-22 (cells refreshed 10/28) | in force ✓ |
| STATUS §THRESHOLD STATUS | STATE | per-row source dates to 10/27–10/28 | current ✓ |
| `registry/THRESHOLDS.tsv` + NOTES | STATE | 10/28 | live; 7/8 thesis-ref anchors dangle 🟡 |
| `workbook/PREDICTIONS.tsv` + RESOLVE_BY sidecar | APPEND-ONLY | newest registration 10/23 | 7 OPEN, past-due check fires both ways ✓; malformed-row/`TBD` fail-open 🟡 |
| `workbook/VX.tsv` | STATE | header 10/28 | 🟠 14 rows carry live tokens on 8/12 values; 3 contradict STATUS |
| `registry/REG_T02_EXIT_LOG.tsv` | APPEND-ONLY | 10/29 | live; GATE-TERRY-ROLL70-EXIT last_checked 10/11 (PROME's) |
| `thesis/CHANGELOG.md` | APPEND-ONLY | 10/12 | 🟡 behind two thesis-level events |
| CALENDAR prediction checkpoints | EVENT | 10/28 | 🟡 two orphan rows, stale section count |
| NEXUS_BRIEF | STATE | 10/30 pin | current ✓ |
| BANK_EXPOSURE_MATRIX | STATE | v2.0 8/20, re-score 11/07 | declared deferral ✓ |
| DECK_EVIDENCE | FROZEN | 7/09 + corrections | ✓ (37.6% struck :25) |
| `reports/2026-07-30_bank-side-HY-attribution.md` | FROZEN report, cited live | 7/30 | 🟠 :122 asserts OZK 37.6% unflagged; STATUS:60 and CLAUDE:152 send REG-T-03 readers here |
| KB.tsv ML-REG-098/115/129/133 | APPEND-ONLY | Feb–Mar | 🟠 cite 37.6% as validating, no correction row |
| `archive/per-bank/*` | FROZEN | 8/10–10/22 | retired ✓; CFG STATUS:5 "VALIDATED" header survives under a dead-figure banner 🟡 |

## 4. Deviations from standard (+ why)

| # | Sev | Deviation | Receipt | Owner |
|---|---|---|---|---|
| 1 | 🟠 | **`scripts/thresholds.py` cannot fail.** Only exit path is the yfinance import (`:18`); a KRE <$60 breach and a total fetch failure both exit 0; `boot.py` grades it OK (not in TRI_STATE). Also grades intraday prices against close-based triggers and covers 2 of 8 registered triggers plus 7 hard-coded unregistered levels | `thresholds.py:11-18`, `:92-155`; R2 fixture E10 | REGINALD |
| 2 | 🟠 | **VX.tsv row-level rot under a fresh header**: 15.02 10Y "ORANGE … approaching RED" at 4.67% vs STATUS:113 4.99% (past the row's own RED band); 6.04 WAL "$4.13 above $78" vs REG-T-02 FIRED $77.80 (10/29); 15.01 SOFR−IORB GREEN 0bp vs STATUS:115 +5bp (the row's YELLOW). The header discloses "other rows retain own vintages", but the cells still read LIVE | `VX.tsv:47,64`; STATUS:113,115 | REGINALD (rows); DAEDALUS (tool perimeter) |
| 3 | 🟠 | **OZK 37.6% survives in two live-cited places** despite the charter's own kill-on-sight rule | §3b rows | REGINALD |
| 4 | 🟠 | **Trade surface one position event behind FORGE**: `KRE $68P Nov-27-2026 ×10` at `FORGE/STATUS.md:71` (owner UNKNOWN, D-74) in neither TRADE.md nor POSITIONS.md; `ledger_staleness --trade` grades both ok because it keys on STATUS, not the FORGE reconcile | grep 68P → 0 | REGINALD (mirror) · PROME (owner of the leg) · DAEDALUS (tool) |
| 5 | 🟠 | **Charter 77%**, needs −2,193 B to reach the 70% stop | `read_cap_check --agent REGINALD` | REGINALD (+ Will if the trim needs his word) |
| 6 | 🟠 | **read_cap rc 1** from one 39,509 B BOARD signal (121%) via the `BOARD/SIG-W-*.md whole` class row; the 10/22 reading-companion row (67%) does not shadow it | READS 488/489 | PROME + DAEDALUS (tool) |
| 7 | 🟠 | **READS perimeter UNKNOWN**: attestation 10/20 stale (charter changed 4× since; COMPLETION_SPEC 10/29); the every-boot reads of `AGENTS/{WAL,OZK}/REGINALD_CHANNEL.md` (89%, 78%) have no REGINALD row | `reads_check.py --agent REGINALD` | REGINALD → PROME |
| 8 | 🟡 | BOTTOM LINE undated/not last; 10/29 session left no STATUS stamp | STATUS:124 | REGINALD |
| 9 | 🟡 | FLG ladder `vx_ladder_check.py` is an absorbing ALERT (rc 1 every run since 9/16) so boot never reaches all-clear | R2 E9 | REGINALD |
| 10 | 🟡 | Frozen feeds (DARKPOOL, SHORT_INTEREST, SHORT_VOL) carry post-freeze rows to 9/29–10/12; `options_oi.py` appends with no frozen guard | R2 rank 7 | REGINALD |
| 11 | 🟡 | ~20 genuinely retirement-eligible files (>60 d, no live reference) | R4 §C | REGINALD |
| 12 | 🟡 | Glued words written after the 10/22 flag (CALENDAR ≈14, STATUS, VX, charter) | R1 rank 12 | REGINALD |

## 5. Load-bearing context / DO NOT TOUCH

**Held and re-verified:** POSITIONS canonical over the matrix column · HY<260 = REVIEW, not auto-exit (Will 6/19) · THRESHOLDS contract (now **13 columns**) + NOTES.md companion, never folded into the TSV · REG-T-07 evaluates against Trepp; divergence from CREED's trigger is deliberate · MI3 *method* as signature (the OZK number is dead) · recursive drift-grep, never an enumerated list · frozen feeds stay frozen · boot-9b + BOARD schema · WAL seam pointer-only (one exception: the EXIT RULES CRE anchor, STATUS:94, restates WAL's graded figures (NCO 30bp, dated, sourced to WAL's ledger); unratified, so the owner confirms it is intended) · banners name their rewrite triggers · CREED/BELT freeze banners verbatim (`archive/sub-agents/`) · historical WAL provenance refs · the 7/18 pre-registered frames, graded fills and STAGING files · the 7/25 EGBN reserve-read discriminator (now under `research/EGBN/historical/`).
**New:** the resolve-by **sidecar** (never edit Kernel-pinned PREDICTIONS bytes) · `.consumed.tsv` consumption ledger · TRADE §2b "No candidate" log · `outbox/README.md` lifecycle · exit-rail retirement written with the definition it retired · `research/EGBN/` copy hub with INVENTORY + verifier and `research/FHLB/copies/` MANIFEST (Will-requested 10/20, 10/22 — design, not clutter) · the 10/23 ranking-test and 10/28 borrowing-screen FROZEN files (sha-pinned, graded 11/07) · the FL Q3 frame until its ~11/14 final grade · "flagged, not overwritten" for dead figures in frozen reports (fix by a dated head note, never by editing the body).
**Retired from this list:** "547% FLAGGED not overwritten" (superseded by the v2.0 rebuild's denominator explanation, `BANK_EXPOSURE_MATRIX.md:33`) · "NOT a position name" for FITB/PNC/RF and ZION/TODO §0 (moot — archived) · "4-cluster independence framing" (no longer on live surfaces; superseded by "2 channels instrumented, rest owner-held", STATUS:18-20).

**Distinctive strength to protect:** it still finds and records its own errors in the unflattering direction (CFG $12.852B vintage, MEMORY:58; the 10/28 cash read corrected same evening) and fixes review findings fast — four of DAEDALUS's 10/22 gaps closed 66 minutes after the row was written (`233ba18f7` 11:31 → `f8405c6f2` 12:37).

## 6. Maturity snapshot (per-leg; Market class; readings A and B ratified)

| Level | Leg | Verdict | Receipt |
|---|---|---|---|
| L0 | dir + charter | PASS | 166 lines |
| L1 | STATUS + current judgment (reading B) | PASS | STATUS:7 dated 10/30 |
| L2 | structured record, valid schema, accruing | PASS | KB 257×15 to 10/30; PREDICTIONS 25×10; BOARD_LOG 579×11; `ledger_staleness` rc 0 |
| L3 | convergence matrix | PASS | STATUS:35-40; re-score scheduled 11/07 |
| L3 | exit rules | PASS | STATUS:85-96 dated 10/22 |
| L3 | predictions resolving | PASS | 7 OPEN with resolve-by; REG-08/10 graded 10/23; Brier ≈ 0.19 n = 8 |
| L3 | **dated falsification surface** | **PASS** (was AT RISK on the 10/22 row) | kill-rail stamp 10/22; REG-06 EDGAR scans 10/31, 11/30, 1/05; REG-28 checkpoint run on time 10/29 |
| L4 | trade surface (reading A) | PASS (thin) | TRADE.md feeds TERRY; dated no-candidate log; one leg behind FORGE (§4 #4) |
| L4 | signals flowing / consumed | PASS | 8 consumers at 10/27–10/29 vintage |
| L5 | clean closeouts | PASS with debt | 5 sessions pushed + drained; BOTTOM LINE stale, 10/29 unstamped |
| L5 | current | **PARTIAL** | trade mirror one leg behind; VX rows contradict STATUS; boot can print all-clear over a breach |
| L5 | mechanical-QC | N/A | WQ-181 ② |

**Grade: L4 / H retained. L5 NOT AWARDED** — on §4 #1, #2 and #4 plus the BOTTOM LINE. All are owner-fixable in one session.

## 7. Open questions / comprehension gaps

- Is the KRE $68P Nov-27 ×10 leg REGINALD-scope? FORGE marks it UNKNOWN (D-74); PROME owns the answer.
- Recognition-lane exit is a 3-leg AND whose REG-03 leg resolves ~late Feb 2027: is a ~4-month inability to stand down intended? (owner)
- FLG K-3 framework question (does a post-break-window kill pass?) routed to REGINALD, ruled nowhere; not REGINALD's to rule — pick up at the FLG refresh.
- Topology vs traffic: `CORAL → REGINALD` and `SHADE → REGINALD` have never carried a packet; `REGINALD → VIOLET` has no consumption (PROME, topology owner).
- About 100 October report bodies were census-only; a claim keyed on a specific report should be read there.
