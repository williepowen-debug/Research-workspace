# CARL SCRATCH
> ✅ Clean & synced to origin after this session's push (folder-architecture pass-2).

**Last session:** 2026-05-31 ~21:30 UTC (Sun PM continuation of yesterday's architecture pass)
**Type:** Folder-architecture / stale-file cleanup pass-2 — SIGNAL_INTAKE.md trim + SPAWN_PROTOCOL.md update

**PRIORITY-1:** **Run boot scans then handle the early-June data wall.** `.venv/bin/python3 AGENTS/CARL/scripts/docket_countdown.py` will surface tomorrow's first fire (**Jun 1 ISM Mfg PMI**) and the rest of the wall: JOLTS Apr Jun 2 → ISM Svc Jun 3 → **NFP May Jun 5** (V16 second realized print, CRL-11 hires watch) → DG Q1 Jun 2. Process as they land, prune fired docket rows. JOLTS Jun 2 is CRL-09-adjacent (just-missed last release); new release decides direction-stickiness.

**PRIORITY-2:** **V12 thesis pass — 3 hardening datapoints loaded** (Waller pivot 5/22 + GDP Q1 2nd-est stagflation composition 5/28 + Apr Core PCE 3.3% cycle-high 5/28). Re-read THESIS.md Vector #12 vs "locked + hawkish + possibly hiking"; decide v2.5.2 minor. Score-upgrade review V1/V8/V12. **Hold formal V12 call for Jun 16-17 SEP** (decisive), but a dedicated thesis pass before then is warranted.

---

## WHAT HAPPENED
1. **Boot** (Sun 5/31 ~5pm ET) — clean & synced from yesterday's push; inbox clean; docket countdown unchanged (Jun 1 ISM is next fire); PREDICTIONS scan shows 17 OPEN, none past-due.
2. **SIGNAL_INTAKE.md trim** (Apr 19 → 5/31). Removed: ACTIVE THRESHOLDS table (Gas $4.06, Fannie 0.74%, CC 12.70%, SYF 5.8% Feb, FC starts 82,631 — all 6-week-stale, would have actively misled a spawn citing them as current); Earnings Events list (Apr 21-May 7 all passed); old HAWK lag note (now 3-4d Iran-cluster + 17-18d both-directions). Kept: priority levels, routing categories, keyword patterns, what-not-to-send. Added pointer table → STATUS / docket / LIAISON / PREDICTIONS / VX for live state. Honored [[project_messaging_overhaul]] memory (don't extend routing infra here; new logic → LIAISON). Net 164→161 lines, +173/−188 content turnover.
3. **SPAWN_PROTOCOL.md update** (Apr 9 → 5/31). Phase 1 "Boot & Assess" deleted (duplicated/contradicted CLAUDE.md's 14-step boot with docket+PREDICTIONS scans). Cleaned workbook refs (`ML.tsv` archived May 3, `PLATFORM.tsv` never existed → generic "sub-agent domain TSV"). Codified auto-memory patterns inline: 4-rule prompt discipline ([[feedback_subagent_prompt_discipline]]), parallel-spawn ([[feedback_parallel_spawn_independent_agents]], Principle #2 + Rule #9), adversarial-pair brief ([[feedback_adversarial_brief_for_pair_teams]]). Counter-Signal Detection points to handoff_RED/COUNTER_LOG. Added POLLY K-shape Selection cascade example. Scope banner at top distinguishes from CLAUDE.md boot. Net 221→209 lines.
4. **ROADMAP RECENTLY RESOLVED** entry + timestamp bump.

## STATUS CHANGES
| Item | Change |
|------|--------|
| `SIGNAL_INTAKE.md` | 42d stale → 5/31; ACTIVE THRESHOLDS table + Earnings Events removed (stale); routing rules preserved |
| `SPAWN_PROTOCOL.md` | 52d stale → 5/31; Phase 1 boot dedup + ML/PLATFORM refs removed + auto-memory patterns codified |
| ROADMAP.md | timestamp + RECENTLY RESOLVED entry for 5/31 |

No data mutations — STATUS / PREDICTIONS / CHANGELOG / KB / VX / docket all untouched. Pure architecture + stale-doc hygiene (matches 5/30 pattern).

---

## NEXT SESSION SHOULD

### IMMEDIATE (boot + 24h)
1. **Run boot scans 7a/7b** — docket countdown + PREDICTIONS due/stale.
2. **Early-June data wall — TOMORROW (Jun 1) ISM Mfg PMI** is first fire. Then JOLTS Jun 2 / DG Q1 Jun 2 / ISM Svc Jun 3 / NFP Jun 5. Integrate + prune docket rows.

### THIS WEEK / NEXT 2 WEEKS
3. **Jun 10** CPI May · **Jun 12** UMich prelim · **Jun 16** Retail Sales + NAHB + LEN FQ2 · **Jun 16-17 FOMC + SEP** (V12 decisive).

### WATCH / CONDITIONAL
4. **CRL-03 invalidation watch** — May Fannie (~Jun 26) = month 2 of <0.65% test.
5. **CRL-08 AAA pump** — dormant unless Brent re-spikes on Iran-kinetic.

### THESIS / WORKBOOK
6. **V12 thesis pass + score-upgrade review** (V1/V8/V12) — PRIORITY-2 above.
7. **Workbook session** — ~16 KB candidates pending (GDP 2nd-est / Apr PCE Core 3.3% / savings 2.6% / CRL-08 5d-breach + 12 carried); VX 26d stale (FOMC/GAS/HSG/K-shape-WAGE); SAV-vector update for 2.6%.
8. **LIAISON cycle 1** — OVERDUE ~25d (since May 6); next deferred architecture item.
9. **Sub-agent staleness** — all 7 now 44+ days. **DOC spawn candidate** (healthcare-services GDP drag).
10. **5/6-5/13 BOARD backlog** (~70 sigs) — mechanical ledger sync.

### ARCHITECTURE BACKLOG (deferred — Will to scope next cleanup pass)
11. **Workbook transitional artifacts** — `AUDIT_2026-05-02.md`, `ITEM_2.5_PLAN.md`, `ITEM_2.5_DISPOSITIONS.md`. Pending Item #3 (validator) decision.
12. (closed this session — SPAWN_PROTOCOL + SIGNAL_INTAKE pass complete.)

### BACKLOG (no deadline)
13. HY OAS refresh (~51d). Workbook Item #3 (validator) + #6 (INDEX). v2.5.1 8 PENDING_VERIFY. ABS_BASELINE Mar 10-Ds. POLLY/MARCO refresh. 6 Apr-17 outbox signals (deferred per messaging-overhaul).

---

## OUTBOX (6 Apr 17 signals deferred per messaging-overhaul; unchanged)
| File | To | Summary |
|------|----|---------|
| SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md | REGINALD | 7-lever auto-lender translation |
| SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md | REGINALD | Santander/Bridgecrest/Exeter 60+ DQ |
| SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md | LIQUID | BNPL ABS structured-credit sub-vector |
| SIG-CARL-LABOR-20260417-FL-UI-Wave2-gig-surge.md | LABOR | FL UI Wave 2 + $4.09 FL gas + 22% gig |
| SIG-CARL-LABOR-20260417-NFIB-SB-hiring-pullback.md | LABOR | NFIB Mar SB metrics |
| SIG-CARL-REGINALD-20260417-IEEPA-refund-SB-liquidity-injection.md | REGINALD | SCOTUS IEEPA + $166B refunds |

## INBOX (0 items, clean)
## HANDOFF_RED (4 files + README, unchanged — README_old.md purged 5/30)
## HANDOFF_WALTER — LIAISON cycle 1 OVERDUE ~25d (last touched May 6) — next deferred architecture item

---

## WORKBOOK HEALTH (unchanged from 5/29; architecture-only session)
| TSV / file | Rows | Last Mod | Note |
|-----|------|----------|------|
| **docket/CATALYSTS.tsv** | 34 | May 29 | run countdown at boot |
| PREDICTIONS | 24 | May 29 | 17 OPEN, scan clean today |
| CHANGELOG.md | — | May 29 | still owes V12/K-shape-wage backfill |
| STATUS.md | 250 | May 29 | at target |
| ROADMAP.md | — | **May 31** | timestamp bumped this session |
| KB | 279 | May 5 | 26d — ~16 candidates pending |
| VX | 117 | May 5 | 26d — FOMC/GAS/HSG/K-shape-WAGE pending |
| BOARD_LOG | 193 | May 27 | INDEX unmoved — no diff owed |
| LIAISON.md | 7 turns | May 6 | cycle 1 OVERDUE ~25d |
| FLOW / STATE_DIFFUSION / BNPL_STRESS | 24/62/59 | Apr 17 | **44d** |
| ABS_BASELINE | 72 | Apr 16 | **45d** |
| TRENDS | 39 | Apr 6 | **55d** |
| **TRADE.md** | 42 | May 30 | stub installed |
| **SIGNAL_INTAKE.md** | 161 | **May 31** | trimmed to durable routing rules |
| **SPAWN_PROTOCOL.md** | 209 | **May 31** | updated; Phase 1 dedup + auto-memory patterns codified |

---

## URGENT
- Early-June data wall starts **TOMORROW (Jun 1, ISM Mfg)** — boot with docket countdown.
- **CRL-03 May Fannie (~Jun 26)** = invalidation decider (month 2 of <0.65%).
- **Jun 16-17 FOMC + SEP** = V12 decisive catalyst.

## SESSION FINDINGS WORTH CARRYING
- **Stale-process-doc pattern is broader than TRADE.md.** SIGNAL_INTAKE.md had the same shape — descriptive of how things "currently" work, with embedded dated tables (thresholds, earnings dates) that decayed silently. Generalized fix: any process doc with a "current values" or "upcoming events" table should refer-out to the live source instead of carrying its own snapshot. The dated tables in SIGNAL_INTAKE were 6 weeks stale and contradicted STATUS.md on 5 of 8 rows; removing them is a behavioral fix not a cosmetic one.
- **SPAWN_PROTOCOL.md Phase 1 ≠ CLAUDE.md SPAWN PROTOCOL.** Both files had a section called "spawn protocol" doing two different things (boot vs. sub-agent spawning). Renaming SPAWN_PROTOCOL.md's session steps to "Phase A/B/C" + adding a SCOPE banner removes the confusion. If a third such file ever shows up, follow the same disambiguation pattern.
- **Auto-memory patterns belong in the doc that governs the behavior, not just in memory.** I'd been citing `[[feedback_subagent_prompt_discipline]]` ad-hoc; making it Section "SUB-AGENT PROMPT DISCIPLINE" in SPAWN_PROTOCOL.md means a future spawn that reads the protocol gets the rule even without me re-citing memory. Memory still anchors why the rule exists; the doc tells you what to do.
