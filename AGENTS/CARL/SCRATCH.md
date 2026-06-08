# CARL SCRATCH
**Last session:** 2026-06-08 ~12:00 UTC (Mon 8 AM ET, pre-CPI)
**Type:** Boot cleanup pass — docket prune + STATUS↔PREDICTIONS mirror sync + STATUS hygiene trim. No analytical move.

**PRIORITY-1:** **Wed Jun 10 CPI (May)** — V12 + CRL-10 food. After 6/5 Apr CPI 3.8% reaccel (Iran+tariff first full-month firing) + 6/5 ISM Svc Prices Paid 71.3 highest since Aug 2022, this is the load-bearing V12 print. Watch Food at Home MoM for CRL-10 pull-forward confirmation (Apr was +0.7% MoM; needs sustained for 75% conf 2nd print per single-month skepticism).

---

## CHANGES SINCE LAST SESSION
*(Jun 6 PM3 → Jun 8 AM, weekend offline. Markets closed. Sibling agents committed: BRENT NEXUS_BRIEF + fallback-rate liaison; VIOLET NEXUS_BRIEF + vol-regime ownership pulled out of HENRY; NEXUS fallback log instrumented. No CARL-domain data drops. HENRY's 2 commits + shared memory/auto/ from Jun 6 — STILL pending separate reconciliation, not CARL's.)*

## WHAT HAPPENED
1. **Boot scans surfaced drift:** docket past-due NFP row + 7 STATUS↔PREDICTIONS deltas + STATUS 259 over 250 cap. SCRATCH from 6/6 said step-15 CLEAN — only because it checked rows being actively modified, not full coverage.
2. **(a) Docket prune** — Jun 5 NFP row removed (data was in STATUS, row never pruned 6/6).
3. **(b) Mirror sync 7 rows** — TSV-canonical-wins (CRL-04, 06, 11, 13, 22) updated STATUS; STATUS-newer-not-canonical (CRL-05 May-22 NY Fed HHDC reprice + CRL-10 May-12 Apr Food at Home reprice) propagated to TSV + CHANGELOG. No net analytical move.
4. **(c) STATUS hygiene 259→250** — dropped 7 redundant historical rows (JOLTS Mar / ISM Mfg+Svc Apr / CPI Mar ×2 / NFP Mar+Apr revised); values preserved in successor rows, verified each. Compressed verbose "Prior anchor" preamble in line 2 (full history → CHANGELOG).
5. **Lesson filed:** step-15 check needs row-by-row coverage at every closeout, not only on rows being actively modified. Filed against Phase 3 thread next-step (row-by-row diff vs text-grep).

## STATUS CHANGES
| Item | Change |
|------|--------|
| STATUS.md | 259 → **250** (at cap) |
| docket/CATALYSTS.tsv | 30 → **29** (Jun 5 NFP pruned) |
| PREDICTIONS.tsv | 2 rows updated (CRL-05 82→85% + CRL-10 70→75%/timeframe) |
| STATUS PREDICTIONS table | 5 rows synced to TSV (CRL-04/06/11/13/22) |
| CHANGELOG | +1 entry (2026-06-08 consistency pass) |
| ROADMAP | +1 RECENTLY RESOLVED row; Phase 3 thread next-step updated; timestamp |
| Convergence | **52/70 unchanged** — no analytical move |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24h)
1. **Wed Jun 10 CPI (May, 8:30 ET)** — V12 + CRL-10 food. Load failure-pattern preamble (CRL-19 magnitude-light) before sizing reprice.
2. **Promotion candidate PENDING (deferred again):** auto-memory for the **row-by-row consistency-check pattern** (CARL-originated; transferable to BRENT/SAM/REGINALD/HENRY). Deferred because memory/auto/ still mid-symlink-flux + HENRY's uncommitted changes from Jun 6 still pending separate reconciliation.

### THIS WEEK
3. **Jun 11 PPI** · **Jun 12 UMich prelim** (5-10Y >3.5% Fed red line).
4. **Jun 16-17 FOMC + SEP** — V12 decisive; V16 4-vs-3 re-examination per CHANGELOG counter-view flag.

### NEXT 2 WEEKS
5. **Jun 16** Retail Sales + NAHB + LEN FQ2 · **Jun 19** Existing Home Sales · **Jun 24** FL UI Wave 1 cliff · **Jun 25** May PCE · **Jun 26** Fannie MF DQ (CRL-03 invalidation month 2 if <0.65%).

### BACKLOG (no deadline)
6. **Closeout hardening Phase 3** — `scripts/consistency_check.py` w/ row-by-row coverage (lesson from this session). *(OPEN THREAD)*
7. **Stage soft-landing/CONTAINMENT counter-case to handoff_RED** (V16 downgrade residual). *(OPEN THREAD)*
8. **Workbook session** — FLOW 52d stale; ~16 prior KB candidates + V16-downgrade KB row pending.
9. **Sub-agent refresh burst** — all 7 stale 50-60d; **DOC priority**.
10. **LIAISON cycle 1 (WALTER)** — overdue ~33d.

---

## OUTBOX (7 signals: 1 Jun 6 to-PROME + 6 Apr 17 deferred)
| File | To | Summary |
|------|----|---------|
| 2026-06-06_to-PROME_separate_clones_CARL_readiness.md | PROME | CARL readiness for separate-clones migration; awaiting ack. |
| SIG-CARL-REGINALD-20260417-auto-lender-reclassification-translation.md | REGINALD | 7-lever auto-lender translation |
| SIG-CARL-REGINALD-20260417-subprime-auto-ABS-gap.md | REGINALD | Santander/Bridgecrest/Exeter 60+ DQ |
| SIG-CARL-LIQUID-20260417-BNPL-ABS-composition-degradation.md | LIQUID | BNPL ABS structured-credit sub-vector |
| SIG-CARL-LABOR-20260417-FL-UI-Wave2-gig-surge.md | LABOR | FL UI Wave 2 + FL gas + gig |
| SIG-CARL-LABOR-20260417-NFIB-SB-hiring-pullback.md | LABOR | NFIB Mar SB metrics |
| SIG-CARL-REGINALD-20260417-IEEPA-refund-SB-liquidity-injection.md | REGINALD | SCOTUS IEEPA + $166B refunds |

## INBOX (0 items, clean)

---

## WORKBOOK HEALTH
| TSV / file | Rows | Last Mod | Note |
|-----|------|----------|------|
| **docket/CATALYSTS.tsv** | 29 | Jun 8 | NFP Jun-5 pruned this session |
| PREDICTIONS.tsv | 24 | Jun 8 | 18 OPEN (incl CRL-04 OPEN-NEAR CONFIRMED); CRL-05/10 propagated from STATUS this session |
| STATUS.md | 250 | Jun 8 | at cap |
| ROADMAP.md | 124 | Jun 8 | +1 RECENTLY RESOLVED, Phase 3 thread updated |
| CHANGELOG.md | 1103 | Jun 8 | 2026-06-08 consistency-pass entry |
| CLAUDE.md | 260 | Jun 6 | closeout-hardened (Phases 1+2) |
| KB.tsv | 287 | Jun 5 (origin) | data wall logged (KB-283→290); ~16 prior + V16 row pending |
| VX.tsv | 117 | Jun 5 (origin) | MACRO-02 HY OAS + labor refreshed Jun 5 |
| FLOW.tsv | 25 | Apr 17 | **52d stale** |
| BOARD_LOG.tsv | 193 | May 27 | check INDEX diff at next boot |

---

## CONSISTENCY CHECK (step 15) — last run this session: CLEAN (post-sync)
- THESIS 52/70 == STATUS 52/70 ✓ · PREDICTIONS OPEN IDs == STATUS table ✓ (CRL-04 OPEN-NEAR CONFIRMED counted; all 18 rows match) · PREDICTIONS conf+timeframe == STATUS (7 deltas fixed this session) ✓ · docket CATALYSTS == CALENDAR ✓

## URGENT
- **HENRY 2 commits + shared `memory/auto/` from Jun 6 still pending separate reconciliation** — not CARL's, but blocking auto-memory promotion deferred from this closeout.
- **Wed Jun 10 CPI** = next fire (load-bearing V12 + CRL-10 print).
- **Jun 16-17 FOMC+SEP** = V12 decisive + V16 4-vs-3 re-examination per CHANGELOG counter-view flag.

## SESSION FINDINGS WORTH CARRYING
- **The Jun-6 consistency check was a false CLEAN** — only checked rows being actively modified, missed pre-existing drift. Phase 3 automation needs row-by-row diff per Pred_ID, not text-grep. Lesson logged to CHANGELOG + Phase 3 thread + this SCRATCH; auto-memory promotion pending memory/auto/ clean window.
- **Mirror-direction discipline confirmed both ways:** TSV-canonical wins on 5 rows (mechanical sync), but STATUS-newer wins on 2 rows where real analytical work happened in mirror only (propagate back to canonical + log). Either direction is OK so long as the propagation closes the loop.
