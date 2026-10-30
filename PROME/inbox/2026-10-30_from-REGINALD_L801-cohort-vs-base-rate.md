# REGINALD -> PROME: DOCKET L801 decided — coverage-decline leg dropped as a predictor; inbox drained

**From:** REGINALD (Claude Code, claude-opus-5-5; PROME prome-a9 spawn, WQ-184 Tier 1 on the due row) · **Date:** 2026-10-30, written 09:15 ET (from `date`)
**Record:** `AGENTS/REGINALD/reports/2026-10-30_L801/REPORT.md` · KB `ML-REG-260` · STATUS current-judgment line · NEXUS brief re-pinned.

## Decision at REGINALD's letter (the row's ask)

| Leg (my answer to SIG-W-20261022-005) | Decision | DEWEY base rate cited (REQ-DEWEY-20261022-003) |
|---|---|---|
| Problem loans rising | **KEEP** — the predictive leg. Count is **7 of 10** [10/23], not the 6 of 6 the row quotes [10/22]. | 2007–10, n = 373: problem-loan rise vs later charge-offs ρ +0.464 |
| Reserve coverage falling | **DROP as a predictor** (weight zero); descriptive only, never cited without the base rate | Joint pattern → ≥25bp charge-off jump within 4Q in **2 of 10 episodes vs 41/166 (25%)** unconditional; coverage change vs losses ρ −0.064 (p ≈ 0.21); adds R² 0.088 → 0.094 after the problem-loan rise |

Why drop, not re-weight: the data give no positive weight at the asked horizon (20% vs 25%); the 8-quarter lift is pre-2020 only and belongs to the problem-loan half. Caveats kept: ~3 loss cycles; current episode unresolved since 2024Q1 with charge-offs flat; CECL makes today's coverage look safer than history; "collateral covers it" has a poor record at failed banks (failed-bank data).

**FLG cohort input (NEXUS brief 10/28):** cure share 59.5% → 1.6%, exits 87.5% payoff/disposition, $1,571M non-accrual with no allowance. Coverage now reads as a question about loans called safe on collateral, graded by loss on exit at the FLG 10-Q (~Nov 6–9). No peer base rate for cure share can be built (FR Y-14Q, non-public).

**Unchanged:** no score, threshold, prediction or probability. The matrix's coverage POINT (a level, channel 2) stays frozen until the 11/07 S1-vs-S2 ranking test; re-scoring now would change what that frozen test measures. REG-29 rests on appraisal refresh, not coverage. No TERRY candidate (a method decision, no print graded). Q3 Call Reports: FDIC BankFind 0 rows at 10/30 09:09 ET; not waited for. L805 not touched.

**For Will-facing synthesis (plain words):** the Q3 bank prints showed more bad loans and thinner reserve coverage. History says only the bad-loan rise has predicted losses, so falling coverage is no longer treated as a warning on its own. It still points at where to look: loans banks call safe because of collateral, mainly at Flagstar, whose bad loans now leave almost only by payoff or sale.

## Inbox drain (whole inbox, every sender: 13)

3 CYPHER (general) + 10 WALTER, all consumed and filed; 11 BOARD_LOG rows (10 + 1 BOARD backfill, SIG-W-20261029-026); 3 `.consumed.tsv` rows. One ACTION graded: SIG-W-20261029-036 bank-vendor watch = NO-BANK-CONSEQUENCE. SIG-W-20261029-017 integrated (HY 314 [10/28], CCC/HY 4.16×, REG-T-03 exit run 0, REG-T-04 not fired). COR-20261029-43 NO-OP receipt. CYPHER's 10/22 boundary ask answered (CONFIRMED; credit-union-only items → P3). WAL $77.80 / KRE $72.86 [10/29 settled]; REG-T-02 exit log +2 rows, run 0-of-3.

**Boot record:** four instruction files read with `boot_read.py` to `eof: true` — root `CLAUDE.md` 5 pages, `AGENTS.md` 1, `USER.md` 2, `AGENTS/REGINALD/CLAUDE.md` 5. Desk boot reads whole: STATUS, LESSONS, CALENDAR, MEMORY, ROADMAP, BANK_RESEARCH_STANDARD; COMPLETION_SPEC. Pull: origin had no new commits (fetch 09:05 ET); PROME's three dirty `PROME/state/` files would have refused a rebase pull, so none was attempted. Runtime Claude Code, model claude-opus-5-5, session ID UNKNOWN.

## COMPLETION — REGINALD — 2026-10-30
STATUS: ✅ DONE
CHANGED: AGENTS/REGINALD/{STATUS,MEMORY,ROADMAP,NEXUS_BRIEF}.md, reports/2026-10-30_L801/{REPORT.md,WAL-KRE-settled_and_FDIC-Q3-check.txt}, workbook/KB.tsv, board/BOARD_LOG.tsv, registry/{REG_T02_EXIT_LOG,corrections_receipts}.tsv, inbox/processed/.consumed.tsv, 13 inbox files filed, scripts/.kre_float_state.json; AGENTS/CYPHER/inbox/2026-10-30_from-REGINALD_boundary-confirmed.md
RESULT: L801 decided: problem-loan leg kept (7 of 10 up), coverage-decline leg dropped as a predictor on DEWEY's base rate (2 of 10 episodes vs 25% unconditional; ρ −0.064), written in the report, KB ML-REG-260 and STATUS. FLG roll-forward (cure 1.6%, payoff/disposition 87.5%) recast coverage as a loss-on-exit question for the FLG 10-Q. Inbox: 13 drained, 1 ACTION graded no-bank-consequence, 1 correction NO-OP.
GAPS: Q3 Call Reports not at FDIC (0 rows 10/30 09:09 ET) — not waited for per brief; CCB Q3 and H.4.1 (10/29) unread — outside this task.
WILL_NEEDS: None new (FFIEC JWT renewal before 11/05 stays WQ-495.CDR).
FOLLOW-UP: 11/04 FFIEC short-list re-run · FLG 10-Q ~Nov 6–9 loss-on-exit read · 11/07 Call Report run + frozen S1-vs-S2 test settles the matrix coverage point · DOCKET L801 can be annotated DECIDED (PROME-owned row).
