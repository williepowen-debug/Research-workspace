# Agent Profile — HOMER (housing: asset market + housing credit structure)

**Profile vintage:** 2026-10-28 (whole-profile refresh; replaces the 2026-08-07 body, preserved verbatim at `profiles/_prior/HOMER_2026-10-28_before_refresh.md`, crc32 1345916504).

**Built by:** DAEDALUS · **Date:** 2026-10-28 · **Comprehension method:** 3-reader Mode-A fan-out (R1 architecture · R2 ledgers/falsification/guards · R3 flows/consumers/review reconciliation), raw reports at `runs/2026-10-28_HOMER_REFRESH_READERS/`, synthesis `runs/2026-10-28_HOMER_REFRESH.md`.
**Sources read whole by readers:** `CLAUDE.md`, `STATUS.md`, `LESSONS.md`, `OBLIGATIONS_OTHERS.md`, `NEXUS_BRIEF.md`, `MEMORY.md`, `SCRATCH.md`, `LAST_COMPLETION.md`, `AGENTS/HOMER/thesis/THESIS.md`, `AGENTS/HOMER/thesis/PREDICTIONS.tsv`, `AGENTS/HOMER/tools/rent_breadth.py`, `registry/corrections_receipts.tsv`, all 29 unprocessed `inbox/WALTER/` packets, `AGENTS/HOMER/docket/CATALYSTS.tsv` (row 3 partial), the card and the 8/22 review. Header-only: the three cold registers, the eight workbook ledger bodies (~556 KB), `board_log.tsv` rows 2–77. **Staleness:** refresh at HOMER's 2026-11-20 formal grade or on a material STATUS/thesis change.
**Subject state at build:** HOMER not live; last HOMER-authored commit `454435973` 2026-10-19 13:24 ET (Will-requested close). Every later commit under `AGENTS/HOMER/` is a WALTER delivery.

> A Profile is DAEDALUS's durable understanding of a heavy agent. Section-tasks read the relevant slice of this, not the raw agent; re-read the file before applying any change (PAT-009).

---

## 1. Identity

| Field | Value | Evidence |
|---|---|---|
| One line (HOMER's words) | "Monitor U.S. housing market stress across the foreclosure pipeline, multifamily delinquency (GSE + CMBS books), mortgage rates/demand, builder distress, inventory/pricing dynamics, and state-level housing fragility (FL/TX/NV/CA priority)" — the largest household asset/liability class in the chain | `CLAUDE.md:7` |
| Class · launch | Market (graded against `market-agent.md`); ACTIVE on ROSTER; on-demand, last session orchestrated on Codex (gpt-6.1-sol) with PROME coordinating the push | `CLAUDE.md:9-10`; `SCRATCH.md:3` |
| Chain edges (peer, not "reports to") | HOMER → CARL (consumer transmission) · → REGINALD (Path C collateral) · → HENRY (wealth effect, **one-sided: HENRY has never received a HOMER packet and names HOMER nowhere**) · seam with CORAL (FL) | `CLAUDE.md:11`; R3 §2 |
| Ruled ownerships | Trepp CMBS-MF row + GSE-vs-CMBS divergence + Sun-Belt MF realization (`:26`); the mortgage-specific rate surface PMMS / 10Y-FRM spread / FHA-vs-Conv (`:29`); builder data for CARL's CRL-23 (`:18`, `:277`) | as cited |
| FL boundary | **"HOMER PUBLISHES NO STATEWIDE FLORIDA FIGURE. CORAL RULES"** (`:35`). HOMER owns FL METRO foreclosure rates and the Miami-Dade condo cut; a statewide condo read is WITHHELD and the source address routed to CORAL (`STATUS.md:93`; LESSONS §29). FL annual/ratio bands are HOMER's, evaluable once a year | `CLAUDE.md:35,96-97,145` |
| Trade surface | **None**, and no "no book by charter" clause in HOMER's own files; the only no-book statement is PROME's (`GATES.tsv:21` "Moves no capital") | R2 §5, R3 §2 |

## 2. File anatomy (where the richness lives)

Bytes 2026-10-28; budget 32,550 B, rotation trigger 24,412 B, cap 54,250 B. Boot whole-reads are charter steps 2–4 and 8 (`CLAUDE.md:191-204`).

| File | Holds | Boot? | Bytes (% budget) | Note |
|---|---|---|---|---|
| `CLAUDE.md` | rules only; Key Thresholds + rung census `:87-149` is the desk's strongest dimension | harness-injected (rule 20 exempt) | 38,671 (119%) | the 10/19 Codex session is the case where the injection premise may not hold |
| `STATUS.md` | dashboard (values + bands + obligations) + BOTTOM LINE `:158-164` | step 2 | 22,157 (68%) | 628 B under HOMER's own soft line 22,785 B (`CLAUDE.md:212`) |
| `SCRATCH.md` | session handoff | step 3 | 3,908 | — |
| `LESSONS.md` | INDEX over 54 lessons in two cold shards; best-in-fleet Mistake→Rule→Tell corpus | step 4 | 23,910 (73%) | **502 B under the rotation trigger**; closeout measures STATUS only |
| `AGENTS/HOMER/thesis/PREDICTIONS.tsv` | HOM-xx ledger (2 rows); line-1 preamble carries the CRL-06/23 parent-retain ruling | step 8 "due-scan … for past-trigger rows" | **36,472 (112%)** | a predicate scan over unindexed rows is a whole read; invisible to `read_cap_check` (HOMER has no READS.tsv row) |
| `AGENTS/HOMER/thesis/THESIS.md` | **THESIS + THESIS-LEVEL KILL RAIL** — §3 frozen criteria, §4 pre-registered decision rule, §6 defect register, §8 convergence handle, §9 fired-count ledger | not boot-read (`:245`); graded via docket row | 23,077 | the L3 surface the 8/07 profile said did not exist |
| `NEXUS_BRIEF.md` | VIEW/CALIBRATION/CROSS-DOMAIN + the 17-row DO-NOT-CITE register (`:60-77`), the cross-agent retraction vehicle | read whole by NEXUS, CARL, REGINALD, HENRY | 13,447 | CROSS-DOMAIN first (amendment 12) |
| `workbook/` (10) | the record: KB_LIVE 71,786 · PRICING 97,910 · MULTIFAMILY 89,022 · PIPELINE 61,902 · BUILDER 58,735 · RATES 53,951 · STATE_HSG 42,491 · KB 30,499 (FROZEN) · SCHEMA · RENT_BREADTH_ROSTER (FROZEN) | header eyeball, step 7 | — | SCHEMA covers all 8 live/frozen data ledgers |
| `AGENTS/HOMER/docket/CATALYSTS.tsv` | forward calendar, 45 rows; row 3 is the 39 KB servicer-watch class rail | step 5 awk projection | 120,296 | 40 unresolved rows on 10/28 |
| `board_log.tsv` | WALTER signal dispositions, grep-class, never rotate | step 9 membership grep | 70,745 | 3 malformed rows `:65-67` |
| `MEMORY.md` · `OBLIGATIONS_OTHERS.md` · `LAST_COMPLETION.md` (frozen 10/15) · `STATUS_COLD.md` (150,761, crc-pinned) · `LESSONS_COLD*.md` (98,868 crc-pinned; 13,389 append shard) · `reports/` (19 + 5 evidence dirs) · `AGENTS/HOMER/tools/rent_breadth.py` · `registry/` · `state_vectors/` (retired channel) · `archive/` (22) | not boot-read | — | eight of these are absent from the charter FILES table |

## 3. Per-dimension local representation

| Dimension | Where it lives | Form | Rich? |
|---|---|---|---|
| Thesis | `THESIS.md` §1–2: ACCUMULATION → CONVERSION, state 🔴; 2 CORE legs (C1 residential conversion, C2 MF realization) + 3 AMPLIFIERS (A1 FHA-bottom, A2 rate, A3 builder) | prose + per-leg table | yes |
| Convergence / scoring | `THESIS.md` §8 (`:141-171`): **19/25 across 5 legs, 3 independent roots**; A1 co-rooted with C1, A2 feeds CARL V12 (count once); C2's upgrade trigger MET (Trepp 8.04%) but re-scoring deliberately waits for 11/20 | 5-point handle, dated 2026-10-15 | yes |
| Invalidation / exit | `THESIS.md` §3 FROZEN kill rail (`:34-89`, stamp `Kill rail re-derived: 2026-09-29` line 3, registered `GATE-HOMER-THESIS-KILL`); §4 decision rule (both cores ⇒ FALSIFIED; one ⇒ PARTIAL); §9 fired counts 0/5 | dated, frozen, GATES-mirrored | yes |
| Thresholds | `CLAUDE.md:87-149` rung census: every level traces to a sourced year or bracket; two Will-ruled re-arms 9/29 (rent breadth, national FC starts); basis discipline across four ATTOM bases | bands with RE-ARMED stamps | yes |
| Predictions | `AGENTS/HOMER/thesis/PREDICTIONS.tsv`: HOM-01 MISSED (early-kill) 2026-08-31; HOM-02 OPEN (FHA SA DQ ≥12.00%, 65%, arm 1 of 2 fired 8/13, decider Q3 NDS ~mid-Nov, Resolve_By 2027-02-28). No new row since 7/24 | 11-col ledger with Resolve_By | thin (2 rows) |
| Cross-agent routing | charter edges `:11`; packets to CARL/REGINALD/CORAL demonstrated (R3 §2); TERRY none since 7/24; HENRY never | packets + brief | partial |

## §3b. Invalidation-surface inventory (what `falsification_scan` and the sweep read)

| Surface | Kills / flips what | Stamp (in-content) | Fired-state form | Mechanical reader |
|---|---|---|---|---|
| `AGENTS/HOMER/thesis/THESIS.md` §3–4, §9 | the thesis (5 legs; kill counts per leg) | `Kill rail re-derived: 2026-09-29` (line 3); formal grades 2026-11-20, 2027-02-20 (`:89`) | §9 ledger: 0/5 fired; V5 says 11/20 cannot return FALSIFIED/PARTIAL on cores | `falsification_scan` **since 2026-10-28** (class "kill rail (in-thesis)"); docket row 37; GATES:21 |
| `AGENTS/HOMER/thesis/PREDICTIONS.tsv` Invalidation col | HOM-01 (fired 8/31), HOM-02 (arm 1 of 2 fired 8/13) | registered 7/12, 7/24; rulings 8/22 | status cell | fleet tools (consumer_check, asmade_audit) |
| `AGENTS/HOMER/docket/CATALYSTS.tsv:3` servicer-watch classes A–G (+Z) | any class ⇒ 🔴 | ratified 8/13, encoded 8/22; last full sweep 2026-09-29 | Class A FIRED 2026-08-07 (UWM Fitch B+), found 9/29 | boot awk only |
| `MULTIFAMILY.tsv:68` + `RENT_BREADTH_ROSTER.tsv` rent-decline breadth >20/>40/>55% | A3-class band | re-armed 2026-09-29 (Will) | ORANGE 46/100 (Sep); Oct file due ~10/27–31 | **`AGENTS/HOMER/tools/rent_breadth.py`** (verified both directions) |
| `PIPELINE.tsv:77` national FC STARTS >100K/130K/175K | band | re-armed 2026-09-29 | below Yellow (Q2 81,935); Q3 ATTOM access UNRESOLVED | none |
| Dated kills executed: Trepp MF maturity-adjusted (`CATALYSTS.tsv:9`, 2026-10-15); $160B+ MF wall (`MULTIFAMILY.tsv:17`, RETIRED 2026-09-02) | — | — | spent | — |
| `AGENTS/HOMER/reports/2026-09-29_PMMS-2026-10-01_PRE-REGISTRATION.md` | pre-registered print card (HOLD fired at 7.28%) | 2026-09-29 | never edited post-print | none |

## 4. Deviations from standard (+ why)

| Deviation | Verdict |
|---|---|
| Kill rail lives INSIDE the thesis file, not in a separate KILL/EXIT file | **better** (one frozen document, GATES-mirrored); was invisible to the fleet scanner until 2026-10-28 |
| The 11/20 formal-grade cadence is on the thesis rail, docket, GATES and STATUS, not in PREDICTIONS or the charter | **equivalent** by design (`THESIS.md:5`: a HOM-02 resolution is leg evidence, not a thesis grade) |
| STATUS carries values, bands and obligations only; the retraction register moved to the NEXUS brief's DO-NOT-CITE table | **better** (replaced the old MARQUEE) |
| `ledger_staleness` boot form measures ledgers relative to STATUS, so a uniformly idle desk reads green (`--abs-floor --abs-days 7` → 7 STALE at 9 days idle) | **debt** (fleet-tool class, PAT-089); HOMER is in that state now |
| Six LIVE ledgers put `PRIOR HEADER VERBATIM … 2026-10-15` on line 1 beside the current clock; the tool reads two clocks and lets the older govern (−4 d) | **debt**, safe direction; KB_LIVE's line-2 form is the fix pattern |

## 5. Load-bearing context / DO NOT TOUCH

1. `AGENTS/HOMER/workbook/KB.tsv` FROZEN 2026-07-10 — row-ID contract with CARL's KB; 3 short rows (`:14,26,27`) are frozen too: annotate, never rewrite. New rows → `KB_LIVE.tsv`.
2. `state_vectors/` is the retired SV channel; `corrected/` is a retrieval hazard.
3. **Frozen thesis criteria and the 11/20 grade** (`THESIS.md:3,86,89`): no criterion reworded, split or merged at grading; C2's handle upgrade is recorded, not re-scored, until 11/20. `Date_Resolved`/`Outcome` stay empty while one arm of a two-arm kill has fired (`STATUS.md:154`).
4. GSE-MF band letter frozen (WQ-248 C); an ungraded leg above the top rung is correct. Re-levelling any pinned rung = Will-gated RETUNE; rent roster change = re-spec; ratio band annual-only (`CLAUDE.md:112,114,145`).
5. `board_log.tsv` never rotates; the AMENDED-SAME-SESSION pair at row 13 stays.
6. `LESSONS_COLD.md` / `STATUS_COLD.md` are crc-pinned; new lessons go to `LESSONS_COLD_2.md`; `LESSONS.md` stays an index.
7. `PREDICTIONS.tsv` line 1 preamble (CRL-06/23 parent-retain). `LAST_COMPLETION.md` frozen 10/15.
8. Retired figures stay dead: $160B/$270B MF wall, Trepp maturity-adjusted MF, Google Trends, the old 150/170 KB STATUS tier.
9. Spread convention: PMMS minus the Wednesday nominal 10Y close, never a same-date-label pairing (`STATUS.md:62`).
10. The 7/24 HOM-01 grading sheet and the 9/29 PMMS pre-registration card are never edited post-print.
11. `NEXUS_BRIEF.md` `## VIEW` ceiling is schema-owned and unenforced; do not cut brief content against it.

## 6. Maturity snapshot (references `FLEET_MAP.tsv`; does not restate class)

L3 legs all present and read-verified 2026-10-28: convergence handle (§8), frozen dated kill rail (§3, 2026-09-29), predictions resolving (HOM-01), dated falsification surface. **L4 reading A not met:** no TRADE surface and no "no book by charter" clause in HOMER's own files; consumer leg DEMONSTRATED for CARL, REGINALD, CORAL (R3 §2). A one-line charter clause would complete the third disjunct. Card: `upgrades/HOMER_CARD.md` (every 🔴 from 8/22 CLOSED; open residue = threshold-basis audit on the remaining rows, DRAFT-named reports, no charter version field, no reports-to header, MEMORY.md never boot-read).

## 7. Open questions / comprehension gaps

- **Desk dark since 10/19 with 29 unlogged WALTER packets (19 ACTION) and ~13 passed docket dates** — nothing on PROME's docket wakes HOMER before L545 (11/20). Publication of the passed prints was not web-verified. Routed to PROME 2026-10-28.
- Whether HOMER should declare its boot reads in `PROME/registry/READS.tsv` (it has no row; the 36,472 B PREDICTIONS read is the case).
- CORAL-lock re-verification has a rule (LESSONS §28/29) and still no mechanism.
- THESIS defect register D2/D3/D4 (base windows) open since 9/29 with no dated pull; A2 has no upgrade rung (`THESIS.md:154`).
- Workbook ledger bodies (~556 KB) and ~35 KB of docket row 3 were not read; row-level claims rest on header lint and targeted reads.
