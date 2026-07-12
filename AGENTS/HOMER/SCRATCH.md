# HOMER SCRATCH — 2026-07-12 (first live session, post-promotion-rebuild; ROUND 2 below)

**Purpose:** Canonical ephemeral session handoff. Read at boot; rewrite at closeout. Durable findings → `MEMORY.md`/workbook; live state → `STATUS.md`.

---

## CHANGES THIS SESSION

First real session since the same-day promotion build (which was a rebuild/scaffold pass, not a live-data session). This session executed the 5-task PROME packet: inheritance verification, CRL-06 data package, docket/resolver hardening, 4-lens domain sweep, STATUS/NEXUS_BRIEF refresh.

- **Inheritance verification:** spot-checked 4 load-bearing inherited figures against primaries (Fannie MF DQ May 0.58%, Trepp CMBS-MF June 7.23%/9.53% mat-adj, ATTOM Q1 82,631 starts, PMMS). **0 value-drifts found** — every copied number checked out exact against a live primary/near-primary source. **3 staleness gaps found and fixed** (not copy errors — rows that aged out since the 6/26-7/4 cutover pulls): PMMS (3wk stale), ICE pipeline trio (Apr→May), NAR EHS (docket had it as a future catalyst; it already released 7/9).
- **CRL-06 data package delivered:** `reports/2026-07-12_CRL-06-data-package.md` — full ATTOM starts/filings/REO dataset, Q2 run-rate build, and the finding that metric-choice is outcome-determinative (starts/filings confirm, REO doesn't).
- **Docket hardened:** `docket/CATALYSTS.tsv` — 4 dates corrected with confirmed times (NAHB Jul 16 10am ET, Census starts Jul 17, DHI Jul 21 8:30am ET [was 7/22], PHM Jul 22 8:30am ET [was 7/23]), Case-Shiller pinned to confirmed Jul 28, EHS catalyst corrected from a stale ~7/23 assumption to Aug 10 (next actual release).
- **4-lens domain sweep run:** `reports/2026-07-12_domain-sweep.md` — 9 findings tabled, TOP 3 + 2 route-outs for PROME. Biggest catch: REGINALD is citing an 8-month-stale GSE Fannie/Freddie MF figure (0.75% Nov-2025) that materially contradicts HOMER's current 0.58%/improving read — the 7/12 handoff packet to REGINALD only fixed the Trepp leg, missed the GSE leg.
- **Workbook refreshes:** `PIPELINE.tsv` (+7 rows: ICE May pipeline trio, ATTOM May starts/REO monthly nationals), `BUILDER.tsv` (+3 rows: NAR June EHS, Freddie PMMS Jul 9, rate trajectory), both two-clock headers updated.
- **STATUS.md:** Inheritance Verification note added to the vintage header; Foreclosure Pipeline + Mortgage Rates tables refreshed; Open Items rewritten (items 1/3 closed-or-substantially-addressed); Catalysts table rebuilt with confirmed dates; Bottom Line rewritten.

**Not done in round 1 (deliberately out of scope; first two SUPERSEDED — both done in ROUND 2 below):**
- ~~FL condo reconciliation with CORAL~~ → DONE round 2 (package delivered).
- ~~Opening HOM-01~~ → DONE round 2 (registered).
- UST 10Y/30Y leg refresh (10Y-FRM spread numerator) — still Jun 22 vintage.
- MBA weekly purchase-apps refresh — still Apr 24 vintage.

## WHAT I DID THIS SESSION

Read (in order): root CLAUDE.md, HOMER's CLAUDE.md/STATUS.md/LESSONS.md/MEMORY.md/SCRATCH.md/NEXUS_BRIEF.md, docket/CATALYSTS.tsv, all 6 workbook TSVs, inbox (empty except processed/), archive/ (4 files, all correctly bannered, no action needed), state_vectors/ listing. Verified CREED and REGINALD inbox packets still on disk/unconsumed (expected). Cross-read REGINALD's STATUS.md for its independent Trepp/GSE citations — found the stale-GSE issue there. Web-verified: Fannie MF DQ, Trepp CMBS-MF, Freddie PMMS (full page + trajectory), NAHB release schedule, Census starts schedule, NAR EHS (report + schedule page — found it already released), Case-Shiller schedule, DHI/PHM earnings-date press releases, ATTOM archive page + May report (direct), ICE First Look May 2026 (businesswire + housingwire mirror). Read `PROME/packets/DOMAIN_SWEEP_LENSES.md` and applied all 4 lenses.

## ROUND 2 (same day, PROME-directed after round-1 acceptance; round-1 route-outs confirmed DELIVERED by PROME, commit 40357f1d — GSE-leg → REGINALD w/ fix-before-7/14 framing, CRL-06 pointer → CARL)

1. **HOM-01 REGISTERED** — first HOMER-native prediction (`thesis/PREDICTIONS.tsv`): Freddie FMHPI national nominal YoY rolls over. Leg 1 (direction): Jun- or Jul-data release prints YoY below prior month, as-published; Leg 2 (level): YoY ≤ +1.0% by the Aug-data release (~Sep 30). BOTH legs = CONFIRMED; 60% PROVISIONAL. Early-kill: Jun AND Jul data both accelerate >+1.9%. **Registration-time verification catch:** the inherited "Mar +0.7% cycle low" was a vintage print — FMHPI revises monthly; per the May release the trough is Jan 2026 +0.9% (CalculatedRisk 6/30, verified live). Grading = as-published figures per release. Resolver rows added to docket + STATUS Catalysts (~Jul 30 / ~Aug 31 / ~Sep 30); STATUS Freddie-HPI dashboard row updated with the revision note.
2. **FL condo reconciliation package DELIVERED** — `reports/2026-07-12_FL-condo-reconciliation-package.md` (HOMER's side; CORAL delivery via PROME route-out — did NOT write to CORAL's dir). Built the like-for-like from a read-only pass of CORAL's STATUS. Key result: the price "divergence" that motivated the docket item mostly dissolves on scope (statewide −6.1% vs Miami-Dade −10% epicenter median = expected; HOMER already carries the −6.1% itself in STATE_HSG.tsv). **One real conflict found: HOMER's "FL Condo Inventory 12.9mo" is probably Miami-Dade-specific mislabeled as statewide** (CORAL: statewide 8.9mo FL Realtors Apr, Miami-Dade 12.9mo By The Sea Realty Apr; HOMER's own KB-HMR-016 "Miami 13.2mo" Q1 corroborates — it's the row's own prior). RECONCILE FLAG added in place on all 3 HOMER surfaces (STATUS state table, MULTIFAMILY.tsv, STATE_HSG.tsv) — relabel executes on CORAL confirm, per verify-before-propagating. Package: like-for-like table, proposed 6-row figure-ownership split, 5 questions for CORAL. Docket row flipped from "first-boot (ad hoc)" to "awaiting-CORAL".

## NEXT SESSION

1. **CORAL reconciliation response** — on CORAL's answers: relabel the 3 flagged 12.9mo rows, adopt agreed ownership split, close the docket row.
2. **HOM-01 first resolver ~Jul 30** (FMHPI June data): Leg-1 read + early-kill arm 1. Boot-time resolution scan applies — never OPEN-but-stale.
3. **UST 10Y/30Y + MBA weekly purchase-apps refresh** — still owed, lower priority.
4. **Confirm ATTOM's Q2/June reports land** — neither existed as of 7/12; re-check cadence.
5. **Verify REGINALD acted on the GSE-leg fix** (delivered w/ fix-before-7/14 framing) and **check whether CARL adjusted CRL-06** off the data package.

## OPEN THREADS

- GSE-vs-CMBS divergence — WIDENING, both legs confirmed-fresh this session. Next Fannie print (~late-Jul) and next Trepp print (~late-Jul) are the co-determining resolvers.
- May's REO deceleration (-20% MoM) — the one leg of the CRL-06 Q2 dataset where direction isn't locked; watch June ATTOM data.
- HOM-01 OPEN — first own-name prediction on the clock.
- Round-1 route-outs delivered by PROME (40357f1d); round-2 route-out (FL condo package → CORAL) pending PROME delivery. Verify consumption at those agents' next sessions.
