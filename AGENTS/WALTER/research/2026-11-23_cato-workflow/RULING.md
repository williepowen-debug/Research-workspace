# CATO workflow review: Will's approval and what WALTER changed

**Will, WALTER session, 2026-11-23 14:28 ET (prompt clock):** "Okay I think I agree with this:" above a pasted CATO reply. WALTER reads this as approval of CATO's revised 2, 3 and 4, with 1 and 5 proceeding under existing duties. CATO's report: `AGENTS/CATO/runs/2026-11-23_1400_walter-workflow.md` (616d5c33a2). Will's 14:17 ET message asked WALTER to analyze it; WALTER proposed five items at about 14:24 ET.

## CATO's revisions, as received (substance)

| # | Revision |
|---|---|
| 1 | Repair the twelve now; group into underlying stories; reuse reviewed sources. "Up to 34 more" is WALTER's estimate, not CATO-verified |
| 2 | Refresh on resumption and before market-dependent output: VIX and S&P before the first substantive response or dispatch in market hours, evaluate the applicable crossings, refresh other instruments before quoting them as current; one pull may support one response or batch; not before every unrelated card; crossings must be recognized and handled. A session-end scan already exists, so "only at boot" was incomplete |
| 3 | Selective source reading with a broader test: new deals, numbers, loan terms, AND corrections, contradictory evidence, meaningful qualitative developments. Duplicates may cite earlier reviewed evidence. The rest stays "title only; source not reviewed" |
| 4 | Correct older records without rewriting history: keep original closure dates, add a dated correction of what was reviewed; read unresolved items that still matter; do not recreate the historical workload |
| 5 | "Not found by my search"; an unverified report is not presented as fact but may be routed as a claim |
| Review | Use December 14. Removed: "if it fails again, automate it". A recurrence is first classified: stale quoting, missed resumption, inaccessible evidence, or insufficient monitoring |

## Applied

| # | Where |
|---|---|
| 2 | `CLAUDE.md` RUN MODE, Resumption refresh. WALTER's parameters: idle = last read over 15 minutes old; market hours 9:30 to 16:15 ET; high and low since the last read |
| 3 | `design/BOOT_PROTOCOL.md` 7e(g2), `CLAUDE.md` 7e(g2), `tools/intake_scan.py` printed procedure. Test file unchanged |
| 5 | `CLAUDE.md` 10.6 |
| 1, 4 | `registry/gpu_finance_review.json`: original fields kept, dated `corrections` appended; map in `GPU-RECONCILIATION.md` here |

Not changed: no new checker, scheduler, monitor, collector or audit. The boot read set is unchanged, so `PROME/registry/READS.tsv` is unchanged; `boot_basis_hashes.json` is re-attested for the three files WALTER edited only.
