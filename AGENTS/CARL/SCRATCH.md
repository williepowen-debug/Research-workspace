# CARL SCRATCH
**Last session:** 2026-06-08 ~18:00 UTC (Mon EOD, pre-CPI)
**Type:** AM boot cleanup + PM DOC + HOMER sub-agent integration (3 spawn rounds incl. error-correction) + EOD MEMORY.md infrastructure build (CARL caught up to sibling agents' pattern).

**PRIORITY-1:** **Wed Jun 10 CPI (May) 8:30 ET** — V12 + CRL-10 food. New specific watch from DOC: **hospital services MoM** (Apr -0.3% sign flip from Mar +0.4%) — if May prints negative/flat = 2nd-print care-avoidance pricing through. Highest-signal Medical Care line.

---

## CHANGES SINCE LAST SESSION
*(Boot Jun 6 → now Jun 8. Two sub-agent refreshes integrated this afternoon. HOMER discovered + self-corrected a year-misread that briefly suggested CRL-03 should drop to 30% — resolved back to 72% after disambiguator. Net analytical state: V14 Mercer-benefits candidate staged; multifamily mechanism reframed extend-and-pretend; housing leading-edge list-price decline added; no score moves.)*

## WHAT HAPPENED — AM
1. **Boot scans surfaced 3 drift items:** docket NFP past-due + 7 STATUS↔PREDICTIONS deltas + STATUS 259/250 over cap.
2. **Docket pruned** (NFP row); **PREDICTIONS↔STATUS sync** (5 STATUS rows synced to TSV-canonical; 2 STATUS-newer reprices CRL-05/CRL-10 propagated to TSV + CHANGELOG); **STATUS hygiene trim** (7 redundant historicals dropped, Updated-line preamble compressed → 250 lines).
3. **Lesson filed:** step-15 needs row-by-row coverage, not text-grep. Phase 3 thread next-step updated.

## WHAT HAPPENED — PM
4. **DOC sub-agent refreshed** (60d stale). 3 SVs written: SV-01 ACA cliff realized (RED), SV-02 Mercer +6.7% (ORANGE), SV-03 NIPA care-avoidance (ORANGE). DOC predictions reweighted (P01 70→85% ↑, P03 55→35% ↓, P06 65→75% ↑, P07 70→80% ↑, +DOC-P10 NIPA-drag).
5. **HOMER refreshed (3 rounds).** Round 1 lean: CRL-03 72→30% on "Trepp May -46bps cross-confirms Fannie -14bps." Round 2 disambiguator (REO/mod/MF-FC) caught **year-misread** — Trepp -46bps was May 2025, not 2026. Actual Trepp Apr 2026 = **7.71% NEW ATH (+56bps MoM)**. Round 3 cleanup: HOMER files purged of round-1 framing (5 sites beyond masthead corrected); SV-01 moved to `corrected/` with header pointing to SV-03; year-verification rule codified in HOMER spec.
6. **CRL-03 holds 72%** (Will decision). Mechanism intact via Trepp-documented extend-and-pretend. Threshold rule NOT redefined; instead added 2 shadow-tracker VX rows.
7. **STATUS integration:** Multifamily reframed (Fannie + CMBS rows now 🟠 headline / 🔴 mechanism); 8 new rows (Mercer + ACA + Medical CPI + NIPA + ICE FC + MBA Q1 NDS + Realtor.com list price + Redfin gap); 8 trims to stay at 250.
8. **LEN FQ2 date corrected Jun 16 → Jun 11** (4:00 PM ET). Docket fixed.

## WHAT HAPPENED — EOD (architectural)
9. **MEMORY.md infrastructure built** — CARL was missing the per-agent MEMORY.md pattern that SAM/BRENT/HENRY/REGINALD/VIOLET already have. Now exists as the persistent Feedback (Will-given) + Findings (CARL-discovered, not yet promoted) + References layer. Distinct role from SCRATCH (handoff) / ROADMAP (process) / STATUS (data).
10. **CLAUDE.md updated** — added MEMORY.md read at BOOT step 1b + update at CLOSEOUT step 13b + FILES table entry.
11. **3 today's lessons landed in MEMORY.md** as Findings (sub-agent year-verification + row-by-row consistency check + disambiguator-round on load-bearing claims). All marked promotion candidates for global auto-mem when validated next session.
12. **Will-feedback landed** — domain discipline rule (CARL stays consumer-stress, doesn't synthesize upstream). Codified as the first MEMORY.md Feedback entry so future sessions don't repeat the Iran-STATUS-update scope creep.

## STATUS CHANGES
| Item | Change |
|------|--------|
| Multifamily mechanism framing | Two-thermometer reversal → **EXTEND-AND-PRETEND regime** (Trepp documented) |
| Fannie MF row status color | 🟠 → **🟠 headline / 🔴 mechanism** (split) |
| 30Y mortgage | Apr 30 6.30% → **Jun 4 6.48%** (5-wk stale closed) |
| NAHB HMI | Apr 34 → **May 37** (bounce, not recovery) |
| Realtor.com list price | NEW row — **-2.4% YoY May, steepest since 2017** (leading edge) |
| ICE Active FC | NEW row — **276K +32% YoY, above Mar 2020** |
| MBA Q1 NDS | NEW row — **4.44% +18bps QoQ, FHA + VA FC inventory decade-plus highs** |
| Mercer Benefits | NEW row — **+6.7% 2026, 15-yr high, V14 candidate** |
| ACA mid-year attrition | NEW row — **-17% nat'l / -21% federal-marketplace, $113→$178 premium** |
| Medical Care CPI | NEW row — **Apr 2.5%, hospital MoM -0.3% sign flip = Wed watch** |
| NIPA care-avoidance | NEW row — confirmed primary data (BEA Q1) |
| VX.tsv | 117 → **121 rows** (4 new) |
| docket LEN FQ2 | **Jun 16 → Jun 11** corrected |
| STATUS.md | 250 → 250 (at cap; 8 added, 8 trimmed) |
| Convergence | **52/70 unchanged** — no score moves |

---

## NEXT SESSION SHOULD

### IMMEDIATE (this session / 24h)
1. **Wed Jun 10 CPI (May, 8:30 ET)** — load failure-pattern preamble (CRL-19 magnitude-light) + DOC's hospital-services-MoM 2nd-print watch + CRL-10 Food at Home pull-forward confirmation. Multi-domain print.
2. **CPI pre-grade sheet (~10 min, do FIRST at boot, before CPI fires)** — build 5-row "if X prints, then Y" decision sheet in SCRATCH PRE-GRADE section. Pre-grade headline +0.5% MoM (V12 hardens), Core +0.4% MoM (Fed-no-cut locks), Food at Home +0.5% 2nd consec (CRL-10 75→85%), Medical Care hospital MoM ≤0 (DOC care-avoidance confirmed), Energy MoM small-pos (CRL-08 intact). Build so Wed grading is 30 sec, not 20 min.
3. **handoff_RED V16 counter-case staging (~20 min)** — acute-employment-strength legs (JOLTS 1.03 un-inverted, 3-mo NFP avg +93K revisions, AHE decel) staged for RED. Overdue since Jun 6; needed before Jun 16-17 V16 4-vs-3 review. CARL stages, RED maintains.
4. **V14 unified upgrade proposal (~15 min)** — bundle DOC's Mercer +6.7% benefits-cost (top-40% employer crowd-out) + HOMER's housing-deflation leading-edge (-2.4% YoY list price = top-40% asset deflation incoming) into a single V14 3→4 upgrade proposal at `thesis/proposals/2026-06-08_V14_upgrade_proposal.md`. Pre-stages Jun 16-17 FOMC decision packet.
5. **SPAWN_PROTOCOL year-verification rule (~2 min)** — bake HOMER's Jun-8 calibration rule into `SPAWN_PROTOCOL.md` as a sub-agent spawn-prompt discipline item so future POLLY/STUE/GIG/PHAN/POP refreshes inherit it automatically.
6. **HOMER open data gaps (pre-FOMC, ~20 min HOMER side-spawn):** Fannie Q1 10-Q MF mod/forbearance exhibits (paywalled, needs EDGAR pull); Fannie MF REO completions monthly Apr-May; Trepp special-servicing transfer rate baseline pull for VX-CARL-MF-04.

### THIS WEEK
3. **Thu Jun 11** LEN FQ2 4:00 PM ET + BLS PPI + **Census QSS Q1 release** (DOC drilling NIPA segments) · **Fri Jun 12** UMich prelim (5-10Y >3.5% red line).
4. **Stage handoff_RED counter-case** (V16 4→3 residual — bull case on acute-employment legs Jun 1-5). Owed since Jun 6; quick session.

### NEXT 2 WEEKS
5. **Jun 16-17 FOMC + SEP** — V12 decisive + **V14 Mercer-benefits-cost reinforcement decision** (top-40% transmission channel) + V16 4-vs-3 re-examination per CHANGELOG counter-view.
6. **Jun 16** Retail Sales + NAHB + LEN passes · **Jun 19** Existing Home Sales · **Jun 24** FL UI Wave 1 cliff · **Jun 25** May PCE · **Jun 26** Fannie MF DQ (CRL-03 invalidation month 2 watch).

### BACKLOG (no deadline)
7. **Auto-memory promotion** — sub-agent year-verification discipline (transferable to BRENT/SAM/REGINALD/HENRY web-pulling sub-agents) + row-by-row consistency-check pattern. Both deferred per memory/auto/ flux. *(OPEN THREAD)*
8. **Closeout hardening Phase 3** — `scripts/consistency_check.py` row-by-row diff per Pred_ID. *(OPEN THREAD)*
9. **Sub-agent refresh burst** — POLLY/STUE/GIG/PHAN/POP still stale 50-60d (DOC + HOMER now refreshed).
10. **Workbook session** — FLOW 52d stale; KB prior candidates pending.
11. **LIAISON cycle 1 (WALTER)** — overdue ~33d.

---

## OUTBOX (7 signals: 1 Jun 6 to-PROME + 6 Apr 17 deferred — unchanged from AM)

## INBOX (0 items, clean)

---

## WORKBOOK HEALTH
| TSV / file | Rows | Last Mod | Note |
|-----|------|----------|------|
| docket/CATALYSTS.tsv | 29 | Jun 8 PM | LEN date corrected |
| PREDICTIONS.tsv | 24 | Jun 8 AM | 18 OPEN; CRL-03 held 72% PM |
| STATUS.md | 250 | Jun 8 PM | at cap |
| ROADMAP.md | 125 | Jun 8 PM | +1 PM RECENTLY RESOLVED |
| CHANGELOG.md | ~1180 | Jun 8 PM | Jun 8 PM entry added |
| VX.tsv | **121** | Jun 8 PM | +4 rows (MF-03/04 shadow + HSG-03 list-price + HC-01 Mercer) |
| KB.tsv | 287 | Jun 5 (origin) | DOC + HOMER findings not yet KB-rowed (deferred to next session) |
| FLOW.tsv | 25 | Apr 17 | **52d stale** |
| CLAUDE.md | 260 | Jun 6 | closeout-hardened (Phases 1+2) |
| BOARD_LOG.tsv | 193 | May 27 | check INDEX diff at next boot |

---

## CONSISTENCY CHECK (step 15) — PM run: CLEAN
- THESIS 52/70 == STATUS 52/70 ✓ · PREDICTIONS OPEN IDs == STATUS table ✓ (CRL-03 held 72% in both) · docket CATALYSTS == CALENDAR ✓ (LEN Jun 11 in both)

## URGENT
- **Wed Jun 10 CPI** = next fire. Multi-domain: V12 + CRL-10 food + DOC hospital-services MoM 2nd-print watch.
- **Jun 11 LEN FQ2 4:00 PM ET** — CRL-23 builder GM compression baseline; FY27 tariff guidance is the load-bearing language.
- **Jun 16-17 FOMC + SEP** = V12 decisive + V14 Mercer-reinforcement decision + V16 4-vs-3 review.

## WILL-ACTION ITEMS (not CARL work; for Will's queue)
- **Ping BRENT** — Iran-Israel Jun 7 escalation is in BRENT's Monday data file but not propagated to STATUS or outbox. Ask BRENT to update STATUS + flag CARL if downstream pump pass-through changes materially.
- **HENRY 2 commits + shared `memory/auto/`** from Jun 6 still pending separate reconciliation (blocks 2 auto-memory promotions).

## SESSION FINDINGS WORTH CARRYING
- **Disambiguator round earned its keep.** Round 2 wasn't sent to catch an error — it was sent to test a hypothesis. Agent self-corrected. Sub-agent year-verification discipline is the cross-agent transferable lesson; auto-memory promotion candidate.
- **Extend-and-pretend is now the canonical multifamily read.** Headline DQ can be suppressed by mods/extensions for quarters at a time. Shadow trackers (VX-CARL-MF-03/04) are the leading-indicator workaround — but they need baseline pulls.
- **Mercer +6.7% benefits = new transmission channel.** First measurable top-40% cost shock via employer crowd-out. V14 (Upper-Decile Wealth Stress, currently 3) reinforcement candidate — staged for Jun 16-17 FOMC packet, not moved today on aggregator-only signal.
- **Housing aggregate is rolling.** Realtor.com list -2.4% YoY (steepest since 2017) is the leading edge; Freddie HPI +1.4% YoY is a 60-90d lagging echo. V10 + CRL-06 reinforced.
