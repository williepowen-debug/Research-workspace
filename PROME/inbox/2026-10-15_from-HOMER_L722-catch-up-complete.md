# HOMER → PROME: L722 full data catch-up — 11 series pulled at issuer, rail 0/5 fired, Trepp MF mat-adj kill EXECUTED, inbox 9 → 0

**Written:** 2026-10-15 ~12:20 ET · HOMER (spawned by prome-81, Tier 1, DOCKET L722; Will's 10/14 ask) · Claude Code, model Opus 5.5; session ID not exposed (UNKNOWN) · **$0, no trade, no threshold or score moved.**
**Method:** five read-only data helpers (Opus) pulled at issuer; HOMER spot-verified every grading figure at the source file (Trepp PDF text, NAR page, freddiemac.com/pmms, ICE PDF text, FMHPI recomputed from Freddie's CSV, ABR 10-Q and Millrose exhibit) before writing it to a ledger. The crashed session's transcripts (`2dbc5187…`) are not on this machine under `~/.claude/projects/`, so they were not used.

## Series pulled (value · period · publication · source)

| Series | Value | Period / published | Source tier |
|---|---|---|---|
| Trepp CMBS **MF DQ** | **8.04%, +35bp** (2026 high; 12-mo 6.59%); overall 8.02% | Sep / 10-02 | ISSUER PDF (trepp.com/hubfs) |
| Trepp CMBS **MF special servicing** | **8.54%, +17bp** (Apr peak 9.08); overall 11.49% | Sep / 10-13 | ISSUER PDF |
| Trepp MF **maturity-adjusted** | **ABSENT at source** (overall-only 9.66%) | Sep / 10-02 | ISSUER PDF, full-text grep |
| Trepp Oct hard maturities, MF slice | $877.6M; one $569.2M loan at 5.87% DY | Oct cohort / 10-06 | ISSUER |
| **PMMS 30Y** | **7.40% [10/08] (+12) · 7.40% [10/15] (flat)**; 15Y 6.71% | weekly | ISSUER page + FRED |
| 10Y-FRM spread | ~212bps [10/08] (10Y flat ⇒ ~all spread); ~219 [10/15] PROVISIONAL | — | FRED DGS10 |
| **NAR EHS** | **3.99M SAAR** (+1.5% MoM); Aug revised 3.98 → ~3.93M (inferred) | Sep / 10-13 | ISSUER |
| **ICE Mortgage Monitor** | cure LEVEL 7.8% (Jul 8.0); **all-loans YoY NOT PRINTED**; FHA cures −37% YoY; GSE new defaults +18% | Aug / 10-05 | ISSUER PDF |
| **FMHPI** | **+2.19% YoY SA**; **July revised +2.31 → +1.89** | Aug / 09-30 | ISSUER CSV, computed |
| ICE HPI | +1.44% YoY; 3-mo annualized ~0.1–0.3% | Aug–early Sep / 10-05 | ISSUER |
| Realtor.com | list −1.4%, $/sqft −1.7%, active +5.4%, price-cut share 20.8% | Sep / 09-30 | ISSUER |
| **Redfin gap** | **62.6% more sellers than buyers (record)**; buyers 928,892 (modelled, record low); Aug restated 57.9 → 56.9 | Sep / 10-14 | ISSUER |
| Redfin monthly | pending −4% MoM (lowest since spring-2014 ex-Apr-2020); median +1.3% | Sep / 10-12 | ISSUER |
| MBA apps | purchase −4% WoW, −16% YoY; MBA 30Y 7.50% | wk 10/9 / 10-14 | MBA NewsLink (mba.org 403) |
| MND 30Y | 7.45% [10/14]; 52-wk high 7.61 [10/5] | daily | MND |

**Not released at 10/15 noon (not a gap of mine):** NAHB Oct HMI (scheduled **Mon 10/19 10:00 ET**, from an archived NAHB schedule — the live page dropped the row) · ICE First Look Sept (~10/22–28) · ATTOM Sept monthly / Q3. **Not pulled:** TX October CRE auction list (time; lapsed since ~10/05).

## Rules graded

| Rule | Grade |
|---|---|
| **GATE-HOMER-THESIS-KILL** (THESIS §9) | **0 of 5 legs fired ⇒ 🔴 holds.** C1 0/3 (no print) · C2-CMBS 0/3, **"for" flip MET** (> 7.71%) · C2-GSE 0/3 (no print) · A1 ½ of first conjunct, unchanged · A2 0/4 (PMMS 7.40, 90bps above the kill) · A3 0/3 (no print). Review 11/20 unchanged; §7 V5 holds (no FALSIFIED/PARTIAL possible). C2's handle trigger met — **re-score held to 11/20 per §8a** (composite stays 19/25) |
| **Trepp MF maturity-adjusted dated kill** | ⛔ **EXECUTED 2026-10-15**, inside the 10/31 deferral. Absent at source for Jul, Aug and Sep data; the Sep PDF was read in full, so the "unreachable, not absent" objection is answered. Leg re-spec'd onto **MF special servicing** (replacement instrument, never reported as the mat-adj rate), as pre-committed 8/22 (Will-approved plan). Docket row RESOLVED; no band or C2 level moved |
| 30-Yr PMMS band | RED, 40bps through; no uncrossed rung |
| Cure Rates band | **UNGRADED for August** — ICE did not print its native statistic; last graded YELLOW (Jul −28%). Chart-derived −25 to −29% is INFERRED and not used; it sits inside YELLOW either way |
| Existing Home Sales band | RED (<4.0M) crossed by 10K, inside revision noise |
| Builder Price Cuts / A3 | ORANGE 38% (Sep); waits on 10/19 |

## Inbox: 9 → 0 (all logged in `AGENTS/HOMER/board_log.tsv`, moved to `processed/`)
WALTER: -20261002-019 (Hunterbrook LEN/Millrose: amendment permits BTR purchases, sales undisclosed) · -20261008-026 (UWM overlays + MBA) · -20261009-002 (Trepp, confirmed at PDF) · -20261012-035 + -20261014-006 (Redfin) · -20261013-025 (Las Vegas) · -20261015-006 (correction; receipt COR-20261015-06 NO-OP). CREED Arbor label ask: **confirmed at the ABR 10-Q** with two refinements; reply in `AGENTS/CREED/inbox/2026-10-15_from-HOMER_arbor-label-check-confirmed.md`. PROME 10/14 evidence JSON: F1/F2/F3 re-read at source and integrated as one figure each.

## ASK
- **PROME:** close DOCKET L722 as delivered-PARTIAL (only not-yet-released prints and the TX list remain; all dated in HOMER's docket). A HOMER wake on/after **Mon 10/19** grades NAHB (A3) and re-computes the 10/15 spread; the late-October First Look + GSE prints fit one wake ~10/28–30.
- **Will:** nothing.

## COMPLETION — HOMER — 2026-10-15
STATUS: ⚠️ PARTIAL — every lapsed series pulled or checked; NAHB Oct, ICE First Look Sept, ATTOM Q3 not yet released; TX Oct auction list not pulled
CHANGED: AGENTS/HOMER/{STATUS,SCRATCH,NEXUS_BRIEF,LAST_COMPLETION(new)}.md, board_log.tsv, docket/CATALYSTS.tsv, thesis/THESIS.md §9, workbook/{MULTIFAMILY,RATES,PRICING,PIPELINE,BUILDER,STATE_HSG}.tsv, registry/corrections_receipts.tsv, reports/2026-10-15_catchup_evidence/, archive/STATUS_bottom_line_2026-10-15-AM.md, 9 inbox items → processed/; AGENTS/CREED/inbox packet; this memo
RESULT: 11 series at issuer — Trepp MF DQ 8.04% Sep (+35bp, 2026 high), MF SS 8.54%, PMMS 7.40% (10/08 + 10/15), EHS 3.99M, FMHPI +2.19% (Jul rev 1.89), Redfin gap 62.6% record. Rail 0/5 fired, 🔴 holds; Trepp MF mat-adj dated kill EXECUTED (successor MF SS); Cure band UNGRADED (statistic not printed). Inbox 9 → 0.
GAPS: NAHB Oct out Mon 10/19; ICE First Look Sept ~10/22–28; ATTOM Q3 not released; TX Oct auction list not pulled (time); 10/15 spread provisional (Wed DGS10 not on FRED at 12:02 ET)
WILL_NEEDS: None
FOLLOW-UP: HOMER wake ≥10/19 for NAHB (A3) + spread recompute; ~10/28–30 for First Look (C1) + GSE MF (C2); 11/20 formal grade
