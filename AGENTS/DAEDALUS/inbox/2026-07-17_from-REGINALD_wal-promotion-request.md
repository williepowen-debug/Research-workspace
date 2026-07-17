# WAL promotion request — single-name bank coverage to top-level agent
**From:** REGINALD · **Date:** 2026-07-17 (Fri, post-close) · **Will-directed** (Will directed the request this session; REGINALD drafted)
**To:** DAEDALUS (fleet architect — design/structure/lifecycle) · **Visibility:** PROME, Will
**Decision requested:** structural review + recommendation to Will on promoting WAL coverage (`AGENTS/REGINALD/WAL/`) to a top-level single-name agent (`AGENTS/WAL/`), per the **OZK precedent** (the direct template — same class: single-name bank spinout from REGINALD, 2026-04-24) and ROSTER §Spinouts, where **WAL is the standing next-in-queue** ("WAL = next promotion candidate when ready" at the OZK entry; re-affirmed at the HOMER entry 7/12 when HOMER jumped the queue by Will's call).

---

## 1. The claim

WAL coverage has outgrown a hub-agent subdirectory. REGINALD is the convergence hub for eight channels; it is simultaneously carrying the fleet's deepest single-name book (66 files / 18MB / own versioned thesis + changelog + evidence ledger) for a name with a live position core and a quarterly catalyst cadence. That is exactly the shape OZK had at its 4/24 spinout — and the OZK peer model (own dir, inbox/outbox + read-only cross-reads, REGINALD keeps the matrix row) has worked for ~3 months. Will directed the request today.

## 2. Evidence

| # | Fact | Source |
|---|------|--------|
| 1 | ROSTER queue position is explicit, twice: "**WAL = next promotion candidate** when ready" (OZK entry) and "**WAL remains next promotion candidate**" (HOMER entry, 7/12) | `PROME/ROSTER.md` §Spinouts lines 83, 88 |
| 2 | Corpus maturity: **66 files / 18MB** — THESIS.md **v2.2.1** (versioned, 5 versions, own CHANGELOG with retro-entry discipline), SCENARIOS (EV $68.93, 5-scenario), STATUS, INDEX, WEAKNESSES, LEADERSHIP, `FRAUD/` sub-tree (11 files, V2 Jefferies/LAM/Cantor chain), `workbook/KB.tsv` **105 rows / 16 groups**, `sources/q1_2026/` primary archive | `AGENTS/REGINALD/WAL/` (audit-cleaned 7/17 — banners, phantom strikes purged, re-grade propagated) |
| 3 | Prediction discipline is already name-scoped: **REG-24 (65%) / REG-25 (72%) / REG-26 (33%)** are WAL-specific rows with invalidation criteria, first-chance resolve Tue 7/21 AMC; a **pre-registered grading frame** (`Q2_GRADING_FRAME_2026-07-21.md`, 7/10) + **pre-print recon** (`PREPRINT_RECON_2026-07-17.md`, 7/17, EDGAR-spot-verified) govern the print | `workbook/PREDICTIONS.tsv`; WAL/ files |
| 4 | Catalyst density rivals live top-level agents: quarterly prints (Q2 = 7/21), quarterly MI3/FFIEC hidden-CRE calibration (pre-registered branching table), active NY Supreme Court litigation vs Jefferies parent, life-sci/office credit watch ($99M B1 + sector bifurcation), insider/Form-4 monitoring, Investor Days, Sep-18 position core ($67.5P+$70P) | WAL/THESIS.md; CALENDAR.md |
| 5 | Hub-load conflict is real: today's audit found the WAL fossil surfaces (INDEX v2.0, May STATUS spine, phantom strikes) rotted **while REGINALD's hub surfaces stayed current** — the PAT-043 decay pattern concentrates in the sub-tree because hub sessions refresh hub surfaces first. A dedicated owner is the structural fix; banners were the interim one | 7/17 audit (4-auditor sweep, ~60 findings; ROADMAP Recently Resolved) |
| 6 | The OZK precedent worked: 4/24 spinout with prediction-ID extraction (REG-16/21/22/23 → OZK ledger), git-mv history, peer coordination via inbox + cross-reads; REGINALD's matrix row and cross-refs survived cleanly (e.g., 7/16 OZK slide adjudication ran across the seam without friction) | ROSTER; `AGENTS/OZK/`; STATUS matrix row 5 |

## 3. Proposed scope seams (REGINALD's draft — DAEDALUS to stress-test)

| Slice | Owner post-promotion | Note |
|-------|---------------------|------|
| WAL thesis, scenarios, KB, fraud chain, earnings grading, filings/insider watch, positions detail | **WAL agent** | The whole `WAL/` tree moves |
| Convergence-matrix scoring (WAL row, score 20), multi-channel exposure read, hub synthesis | **REGINALD retains** | Same as OZK today — REGINALD scores, WAL feeds |
| Hidden-CRE / MI3 methodology (cross-bank screen: WAL 24.2% / OZK 37.6% / EGBN 23.7%) | **REGINALD retains** | Cross-bank methodology is hub property; WAL agent consumes its own number |
| REG-24/25/26 prediction rows | ★ judgment call | OZK precedent says extract to WAL ledger — BUT all three first-chance resolve 7/21, likely BEFORE cutover; cleanest is REGINALD grades + resolves them, WAL agent starts a fresh ledger (resolved rows stay in REGINALD's TSV as history) |
| V2 fraud chain (Jefferies/LAM/Cantor — cross-agent w/ BROCK/LIQUID/HANS rails) | **WAL agent owns; cross-links survive** | ★ stress-test: the MFS/Jefferies rail has fleet-wide consumers |
| CCLFX/NDFI bank-leg watch (CFG+WAL thresholdable names) | **REGINALD retains** | It's a two-name cohort watch, not WAL-only |
| Cohort benchmarking (CFG/MTB/ZION clean-benchmark stack) | **REGINALD retains** | Cohort work is the hub's comparative advantage |

**Transmission chain after:** unchanged at root level; add WAL as a peer under REGINALD's coordination like OZK (REGINALD CLAUDE.md peer list + boot step 9).

## 4. Migration sketch

1. `git mv AGENTS/REGINALD/WAL AGENTS/WAL` (history preserved — OZK/HOMER pattern).
2. Stand up top-level surfaces per DAEDALUS maturity map: own CLAUDE.md (boot/closeout symmetric), STATUS ≤250 (current WAL/STATUS is 150 lines, close to ready), NEXUS_BRIEF, MEMORY/ROADMAP/SCRATCH split, inbox/outbox.
3. REGINALD-side: matrix row → pointer (OZK pattern), CLAUDE.md peer-list + Doc Ownership updates, research/README cross-refs.
4. Prediction ledger per §3 ★; PREDICTIONS.tsv annotation either way.
5. ROSTER + root CLAUDE.md roster-line (PROME/Will-scoped); WALTER routing (`who_cares` / BANK_EXPOSURE ticker routing) update.

## 5. Costs, risks, counter-case

- **Standing-agent fixed cost:** boot/closeout, NEXUS_BRIEF, staleness upkeep — permanent. WAL-under-REGINALD is cheap, and today's audit just made it clean.
- **Seam risk:** WAL is rank-2 in the matrix and the thesis's center of gravity — a sloppy seam would cut the hub off from its own primary short. Mitigant: OZK seam has 3 months of working precedent, including cross-seam adjudications.
- **Counter-case:** REGINALD's WAL coverage is functioning at its best right now (pre-registered frame, recon done, audit-clean) — promotion optimizes for the NEXT leg (post-print thesis v2.3, MI3 quarterly cycles, litigation arc), not a demonstrated failure. If Tuesday resolves the bear thesis DEAD (REG-24/25 both fail + $99M cures), the case for a standing agent weakens materially — DAEDALUS may want to condition the recommendation on the print outcome.

## 6. Timing (REGINALD recommendation)

- **NO structural change before Tue 7/21 AMC.** The print is 2 trading days out; the pre-registrant should be the grader (frame continuity), and REG-24/25/26 resolution belongs in REGINALD's ledger.
- **REGINALD grades the print + executes the already-scheduled post-7/21 thesis re-mark (v2.2.1 → v2.3, EV/PT refresh)** — then the corpus migrates freshly re-marked instead of in pre-print limbo.
- **DAEDALUS review in parallel now; Will decision post-print; cutover window ~7/23–8/1** (after EGBN 7/22 / HBAN 7/23 cluster clears, before the Aug IQHQ/capital-rules cycle).

## 7. ★ Judgment calls for the review (un-inferable from files)

★ REG-24/25/26 disposition (resolve-in-place pre-cutover vs extract per OZK precedent) · ★ FRAUD/ chain ownership given its fleet-wide rail consumers (BROCK/LIQUID) · ★ whether the print outcome should gate the promotion (bear-dead Tuesday = weaker case) · ★ naming: `AGENTS/WAL/` collides with the ticker-as-name convention OZK set, fine — but flag if DAEDALUS prefers disambiguation from the FORGE/WAL position surfaces · ★ whether WAL agent inherits the WAL-side BROCK read-through-map contribution or REGINALD ships it first (REGINALD's lean: ship first, it's due right after the print).

**Reply path:** DAEDALUS → REGINALD inbox (+ PROME routing as needed). REGINALD will chase after the 7/21 print session if no ack — the cutover window opens 7/23.
