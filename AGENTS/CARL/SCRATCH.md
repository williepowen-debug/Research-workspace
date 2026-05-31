# CARL SCRATCH
> ✅ Clean & synced to origin after this session's push (folder-architecture pass-3).

**Last session:** 2026-05-31 ~22:30 UTC (Sun PM, third architecture pass; ahead of Jun 1 ISM print)
**Type:** Folder-architecture cleanup pass-3 — workbook transitional artifacts archived

**PRIORITY-1:** **Run boot scans then handle the early-June data wall.** `.venv/bin/python3 AGENTS/CARL/scripts/docket_countdown.py` will surface tomorrow's first fire (**Jun 1 ISM Mfg PMI**) and the rest of the wall: JOLTS Apr Jun 2 → ISM Svc Jun 3 → **NFP May Jun 5** (V16 second realized print, CRL-11 hires watch) → DG Q1 Jun 2. Process as they land, prune fired docket rows. JOLTS Jun 2 is CRL-09-adjacent.

**PRIORITY-2:** **V12 thesis pass — 3 hardening datapoints loaded** (Waller pivot 5/22 + GDP Q1 2nd-est stagflation composition 5/28 + Apr Core PCE 3.3% cycle-high 5/28). Re-read THESIS.md Vector #12 vs "locked + hawkish + possibly hiking"; decide v2.5.2 minor. Score-upgrade review V1/V8/V12. **Hold formal V12 call for Jun 16-17 SEP** (decisive), but a dedicated thesis pass before then is warranted.

---

## WHAT HAPPENED
1. **Boot** (Sun 5/31 ~10pm ET, third pass of the weekend) — clean & synced; no new data drops; docket countdown unchanged (Jun 1 ISM is first fire tomorrow).
2. **Workbook transitional artifacts archived** (closed deferred item #3 from yesterday's survey).
   - `git mv workbook/{AUDIT_2026-05-02.md, ITEM_2.5_PLAN.md, ITEM_2.5_DISPOSITIONS.md}` → `archive/workbook_hardening/` (NEW dir).
   - Rationale: all three are May 2-3 sequence artifacts; the durable WORKBOOK DISCIPLINE rule (verify-by-reading-target / [FLAG] / conservative ref-cleanup) was extracted to CLAUDE.md back on May 3; the .md files have served only as audit-trail since.
   - CLAUDE.md FILES table: 2 transitional rows consolidated → 1 archived-pointer row.
   - ROADMAP OPEN THREADS row updated to point at `archive/workbook_hardening/AUDIT_2026-05-02.md`.
   - Result: `workbook/` now 8 TSVs flat, no .md noise — matches the convention that workbook/ is data-only.
3. **ROADMAP RECENTLY RESOLVED** entry + timestamp.

## STATUS CHANGES
| Item | Change |
|------|--------|
| `workbook/AUDIT_2026-05-02.md` | MOVED → `archive/workbook_hardening/` |
| `workbook/ITEM_2.5_PLAN.md` | MOVED → `archive/workbook_hardening/` |
| `workbook/ITEM_2.5_DISPOSITIONS.md` | MOVED → `archive/workbook_hardening/` |
| `archive/workbook_hardening/` | NEW dir (3 files) |
| `workbook/` | now 8 TSVs flat (was 8 TSVs + 3 .md) |
| CLAUDE.md FILES table | 2 transitional rows → 1 archived-pointer row |
| ROADMAP OPEN THREADS | path ref updated to archive location |

No data mutations. Pure architecture/tidiness — the WORKBOOK DISCIPLINE rule was already in CLAUDE.md so behavioral impact is zero.

---

## NEXT SESSION SHOULD

### IMMEDIATE (boot + 24h)
1. **Run boot scans 7a/7b** — docket countdown + PREDICTIONS due/stale.
2. **Jun 1 ISM Mfg PMI** — first early-June print, watch Prices Paid + New Orders (last Apr 84.6 / 53.5 — stagflation sub-component anchor). Then JOLTS Jun 2 / DG Q1 Jun 2 / ISM Svc Jun 3 / NFP Jun 5. Integrate + prune docket rows.

### THIS WEEK / NEXT 2 WEEKS
3. **Jun 10** CPI May · **Jun 12** UMich prelim · **Jun 16** Retail Sales + NAHB + LEN FQ2 · **Jun 16-17 FOMC + SEP** (V12 decisive).

### WATCH / CONDITIONAL
4. **CRL-03 invalidation watch** — May Fannie (~Jun 26) = month 2 of <0.65% test.
5. **CRL-08 AAA pump** — dormant unless Brent re-spikes on Iran-kinetic.

### THESIS / WORKBOOK
6. **V12 thesis pass + score-upgrade review** (V1/V8/V12) — PRIORITY-2 above.
7. **Workbook session** — ~16 KB candidates pending (GDP 2nd-est / Apr PCE Core 3.3% / savings 2.6% / CRL-08 5d-breach + 12 carried); VX 26d stale (FOMC/GAS/HSG/K-shape-WAGE); SAV-vector update for 2.6%.
8. **LIAISON cycle 1** — OVERDUE ~25d (since May 6); next architecture-adjacent item.
9. **Sub-agent staleness** — all 7 now 44+ days. **DOC spawn candidate** (healthcare-services GDP drag).
10. **5/6-5/13 BOARD backlog** (~70 sigs) — mechanical ledger sync.

### ARCHITECTURE BACKLOG (residual from weekend survey)
Closed this weekend: items 1 (User Input), 2 (handoff_RED stale README), 4 (TRADE.md stub), 5 (SPAWN_PROTOCOL + SIGNAL_INTAKE), 3 (workbook transitionals).
Still open: 6 (LIAISON), 7 (workbook TSV refresh — full data session, not architecture).

### BACKLOG (no deadline)
11. HY OAS refresh (~51d). Workbook Item #3 (validator) + #6 (INDEX). v2.5.1 8 PENDING_VERIFY. ABS_BASELINE Mar 10-Ds. POLLY/MARCO refresh. 6 Apr-17 outbox signals (deferred per messaging-overhaul). `inbox/processed/` rollup (59 files Feb-Mar) — cosmetic, mention only.

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
## HANDOFF_RED (4 files + README, unchanged)
## HANDOFF_WALTER — LIAISON cycle 1 OVERDUE ~25d (last touched May 6) — next architecture-adjacent item

---

## WORKBOOK HEALTH
| TSV / file | Rows | Last Mod | Note |
|-----|------|----------|------|
| **docket/CATALYSTS.tsv** | 34 | May 29 | run countdown at boot |
| PREDICTIONS | 24 | May 29 | 17 OPEN, scan clean today |
| CHANGELOG.md | — | May 29 | still owes V12/K-shape-wage backfill |
| STATUS.md | 250 | May 29 | at target |
| ROADMAP.md | — | **May 31 PM** | timestamp bumped this session |
| KB | 279 | May 5 | 26d — ~16 candidates pending |
| VX | 117 | May 5 | 26d — FOMC/GAS/HSG/K-shape-WAGE pending |
| BOARD_LOG | 193 | May 27 | INDEX unmoved — no diff owed |
| LIAISON.md | 7 turns | May 6 | cycle 1 OVERDUE ~25d |
| FLOW / STATE_DIFFUSION / BNPL_STRESS | 24/62/59 | Apr 17 | **44d** |
| ABS_BASELINE | 72 | Apr 16 | **45d** |
| TRENDS | 39 | Apr 6 | **55d** |
| **workbook/** | 8 TSVs flat | **May 31** | 3 transitional .md files → archive/workbook_hardening/ |
| TRADE.md | 42 | May 30 | stub |
| SIGNAL_INTAKE.md | 161 | May 31 | trimmed to durable routing rules |
| SPAWN_PROTOCOL.md | 209 | May 31 | updated; auto-memory patterns codified |

---

## URGENT
- Early-June data wall starts **TOMORROW (Jun 1, ISM Mfg)** — boot with docket countdown.
- **CRL-03 May Fannie (~Jun 26)** = invalidation decider (month 2 of <0.65%).
- **Jun 16-17 FOMC + SEP** = V12 decisive catalyst.

## SESSION FINDINGS WORTH CARRYING
- **Three-pass weekend pattern worked.** Pass 1 (TRADE + User Input + handoff_RED) = highest-behavioral-risk hits. Pass 2 (SPAWN_PROTOCOL + SIGNAL_INTAKE) = second-tier process-doc staleness. Pass 3 (workbook transitionals) = pure tidiness. Net: 5 of 7 survey items closed in three short sessions; only LIAISON (content work) + workbook TSV refresh (data session) remain. Lesson: an architecture survey that's been ranked by behavioral impact can be drained over multiple short sessions instead of one long one — keeps each session under 30 min and each commit narrowly-scoped.
- **Convention bleeding through:** `workbook/` is now 8 TSVs flat with no .md files (rule emerged: workbook/ is data-only, methodology rules go in CLAUDE.md, audit artifacts go in archive/). Same pattern applied to `docket/` (2 files: TSV + human twin) and `board/` (1 TSV). Worth memorializing as a directory-shape convention if a future agent (e.g., promoted sub-agent) needs to set up similar structure.
