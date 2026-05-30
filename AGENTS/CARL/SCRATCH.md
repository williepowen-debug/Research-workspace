# CARL SCRATCH
> ✅ Clean & synced to origin after this session's push (folder-architecture cleanup).

**Last session:** 2026-05-30 ~21:15 UTC (Sat PM, short architecture pass)
**Type:** Folder-architecture / stale-file cleanup (Will-directed, scoped 1+2+4 of 7 surveyed)

**PRIORITY-1:** **Run boot scans then handle the early-June data wall.** `.venv/bin/python3 AGENTS/CARL/scripts/docket_countdown.py` will surface the cluster starting **Jun 1**: ISM Mfg → JOLTS Apr Jun 2 → ISM Svc Jun 3 → **NFP May Jun 5** (V16 second realized print, CRL-11 hires watch) → DG Q1 Jun 2. Process as they land, prune fired docket rows at write-back. JOLTS Jun 2 is CRL-09-adjacent (just-missed last release; new release decides direction-stickiness).

**PRIORITY-2:** **V12 thesis pass — 3 hardening datapoints loaded** (Waller pivot 5/22 + GDP Q1 2nd-est stagflation composition 5/28 + Apr Core PCE 3.3% cycle-high 5/28). Re-read THESIS.md Vector #12 vs "locked + hawkish + possibly hiking"; decide v2.5.2 minor. Score-upgrade review V1/V8/V12. **Hold formal V12 call for Jun 16-17 SEP** (decisive), but a dedicated thesis pass before then is warranted.

---

## WHAT HAPPENED
1. **Boot** (Sat 5/30 ~5pm ET) after 1d gap. Clean & synced; inbox clean; docket countdown shows no same-day fires; PREDICTIONS scan shows 17 OPEN, none past-due as of today.
2. **Folder-architecture survey** — surveyed CARL root + subdirs; identified 7 architecture/stale-file candidates ranked by behavioral impact.
3. **Will approved 1+2+4 (lightest-risk-clearest-scoped triage).** Executed:
   - **(1) `User Input/` migration** → `git mv` `CARL KB_VECT convo.md` → `archive/external_reviews/2026-05-03_CARL_KB_VECT_thesis_stress_test.md` (NEW dir created); `:Zone.Identifier` Windows-artifact preserved alongside; `rmdir` empty parent. Content was the external-LLM stress test that drove v2.5.1 masking framework narrowing (per ROADMAP 5/3 PM).
   - **(2) `handoff_RED/README_old.md` purged** (`git rm`) — pre-v2.5-spinout doc, superseded by current README.md (May 1). Self-flagging `_old` suffix made it an obvious cleanup.
   - **(4) `TRADE.md` archive + thin stub.** Mar 10 v2.1-framed version → `archive/TRADE_2026-03-10.md`; new TRADE.md (~52 lines) flags staleness vs v2.5.1 mechanism (masking 12-24mo visibility-lag invalidates short-dated SYF/ALLY puts as written; V12 regime shift inverts HYG easing assumption; K-shape convergence rewrites OMF/IWM bottom-60% framing; CRL-08 not-sustained changes OMF entry). Stub points to FORGE for live positions; CARL holds none directly.
4. **CLAUDE.md FILES table** — TRADE.md row updated to reflect stub state + archive pointer.
5. **ROADMAP RECENTLY RESOLVED** entry added with full deferred-backlog enumeration. Timestamp bumped.

## STATUS CHANGES
| Item | Change |
|------|--------|
| `User Input/` dir | DELETED (content migrated to `archive/external_reviews/`) |
| `handoff_RED/README_old.md` | DELETED (superseded by README.md May 1) |
| `TRADE.md` | ARCHIVED (Mar 10 → archive/) + STUB installed (v2.5.1 staleness flag) |
| `archive/external_reviews/` | NEW dir + 2 files (the .md + :Zone.Identifier sibling) |
| CLAUDE.md FILES table | TRADE.md row updated |
| ROADMAP.md | timestamp + RECENTLY RESOLVED entry |

No data mutations this session — STATUS / PREDICTIONS / CHANGELOG / KB / VX untouched. Pure architecture + stale-doc hygiene.

---

## NEXT SESSION SHOULD

### IMMEDIATE (boot + 24h)
1. **Run boot scans 7a/7b** — docket countdown + PREDICTIONS due/stale (`awk` helper). Same protocol as 5/29.
2. **Early-June data wall starts Jun 1** (ISM Mfg). Then JOLTS Jun 2 / ISM Svc Jun 3 / NFP Jun 5. Integrate + prune docket rows.

### THIS WEEK / NEXT 2 WEEKS
3. **Jun 10** CPI May · **Jun 12** UMich prelim · **Jun 16** Retail Sales + NAHB + LEN FQ2 · **Jun 16-17 FOMC + SEP** (V12 decisive).

### WATCH / CONDITIONAL
4. **CRL-03 invalidation watch** — May Fannie (~Jun 26) = month 2 of <0.65% test.
5. **CRL-08 AAA pump** — dormant unless Brent re-spikes on Iran-kinetic.

### THESIS / WORKBOOK
6. **V12 thesis pass + score-upgrade review** (V1/V8/V12) — PRIORITY-2 above.
7. **Workbook session** — ~16 KB candidates pending (GDP 2nd-est / Apr PCE Core 3.3% / savings 2.6% / CRL-08 5d-breach + 12 carried); VX 25d stale (FOMC/GAS/HSG/K-shape-WAGE); SAV-vector update for 2.6%.
8. **LIAISON cycle 1** — OVERDUE ~24d (since May 6); folder cleanup #6 surveyed-not-touched.
9. **Sub-agent staleness** — all 7 now 43+ days. **DOC spawn candidate** (healthcare-services GDP drag).
10. **5/6-5/13 BOARD backlog** (~70 sigs) — mechanical ledger sync.

### ARCHITECTURE BACKLOG (deferred from this session — surveyed but Will to decide next cleanup pass)
11. **(3) Workbook transitional artifacts** — `AUDIT_2026-05-02.md`, `ITEM_2.5_PLAN.md`, `ITEM_2.5_DISPOSITIONS.md`. CLAUDE.md says these archive when Item #3 (validator) ships. Either advance Item #3 OR move to `archive/workbook_hardening/`.
12. **(5) SPAWN_PROTOCOL.md (51d)** + **SIGNAL_INTAKE.md (41d)** — freshness scan. SIGNAL_INTAKE likely obsolete on messaging-overhaul.

### BACKLOG (no deadline)
13. HY OAS refresh (~50d). Workbook Item #3 (validator) + #6 (INDEX). v2.5.1 8 PENDING_VERIFY. ABS_BASELINE Mar 10-Ds. POLLY/MARCO refresh. 6 Apr-17 outbox signals (deferred per messaging-overhaul).

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
## HANDOFF_RED (4 files staged + README — 5/30 cleanup removed README_old.md; awaiting RED pickup, unchanged otherwise)
## HANDOFF_WALTER — LIAISON cycle 1 OVERDUE ~24d (last touched May 6) — deferred this session, item #8

---

## WORKBOOK HEALTH (unchanged from 5/29; this session was architecture-only)
| TSV / file | Rows | Last Mod | Note |
|-----|------|----------|------|
| **docket/CATALYSTS.tsv** | 34 | May 29 | run countdown at boot |
| PREDICTIONS | 24 | May 29 | 17 OPEN, scan clean today |
| CHANGELOG.md | — | May 29 | still owes V12/K-shape-wage backfill |
| STATUS.md | 250 | May 29 | at target |
| ROADMAP.md | — | **May 30** | timestamp bumped this session |
| KB | 279 | May 5 | 25d — ~16 candidates pending |
| VX | 117 | May 5 | 25d — FOMC/GAS/HSG/K-shape-WAGE pending |
| BOARD_LOG | 193 | May 27 | INDEX unmoved — no diff owed |
| LIAISON.md | 7 turns | May 6 | cycle 1 OVERDUE ~24d |
| FLOW / STATE_DIFFUSION / BNPL_STRESS | 24/62/59 | Apr 17 | **43d** |
| ABS_BASELINE | 72 | Apr 16 | **44d** |
| TRENDS | 39 | Apr 6 | **54d** |
| **TRADE.md** | 52 | **May 30** | NEW stub (was Mar 10 / 51 lines, archived) |

---

## URGENT
- Early-June data wall starts **Jun 1** (ISM) — boot with the docket countdown.
- **CRL-03 May Fannie (~Jun 26)** = invalidation decider (month 2 of <0.65%).
- **Jun 16-17 FOMC + SEP** = V12 decisive catalyst.

## SESSION FINDINGS WORTH CARRYING
- **Architecture pattern that worked:** survey-then-rank-by-behavioral-impact, present punch list, get Will to scope. Lightest 3 of 7 in one short session beats hand-wringing across all 7. The 4 deferred items are explicitly in next-session #11/12 + on existing backlog (#8 LIAISON, #7 workbook TSVs).
- **TRADE.md was the highest-leverage stale-doc fix.** It was the only file in CARL's root that could have actively misled a future spawn (pre-v2.5 framing on entry triggers + conviction). Other stale files are reference-shaped (KB historicals, BOARD log) or process-shaped (LIAISON cadence). Stub + archive-pointer pattern is reusable for other "stale but content-historically-useful" files when a refresh isn't this-session-scope.
- **Don't refresh TRADE.md mid-architecture session.** Conflating "fix the file" with "rewrite the trade frame under v2.5.1" would have made this a 2-hour content session disguised as cleanup. Stub + flag + defer is the discipline — refresh is a dedicated trade-spawn session.
