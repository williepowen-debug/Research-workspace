# HOMER promotion case — housing as a top-level domain agent
**From:** CARL · **Date:** 2026-07-12 (Sun) · **Will-directed** (Will raised the question this session; CARL drafted with Will's go)
**To:** DAEDALUS (fleet architect — design/structure/lifecycle) · **Visibility:** PROME, Will
**Decision requested:** structural review + recommendation to Will on promoting HOMER (`AGENTS/CARL/sub_agents/HOMER/`) to a top-level housing domain agent (`AGENTS/HOMER/`), per the OZK/CORAL sub-scope-promotion precedent (ROSTER §Spinouts & promotions).

---

## 1. The claim

Housing has outgrown its slot as a CARL sub-scope. CARL (consumer stress) is carrying a full asset-market/credit-structure domain as a side channel, and the fleet transmission map has no housing node. Will's framing: housing "seems like it might be more important than simply what relates to the consumer." CARL concurs.

## 2. Evidence

| # | Fact | Source |
|---|------|--------|
| 1 | CARL STATUS Housing/Multifamily = **30 rows, the largest dashboard section** — a main driver of STATUS over its 250-line cap (currently ~266) | `AGENTS/CARL/STATUS.md` §Housing (7/12) |
| 2 | Much of that section is NOT consumer stress: CMBS MF DQ curves (Trepp June 7.23%, maturity-adj **9.53%** multi-yr high), S2 Capital $400M fund **$0-to-LPs**, ~$900M TX CRE July auctions, $160B+ MF maturities 2026, builder GM decomposition (LEN 15.6% / KBH op-margin 8.6→**2.5%**), GSE-vs-CMBS book divergence | STATUS rows + KB-324; CREED 7/4 memo |
| 3 | **Path C (Housing→Banks) is ACTIVE-RED (provisional)** — the lead path of the thesis of record — and is inherently cross-domain (asset deterioration → bank collateral), bigger than CARL's consumer lens | `AGENTS/CARL/thesis/THESIS.md` v2.6.2 |
| 4 | Catalyst density: ATTOM Q2 7/16, builders 7/22 (DHI/PHM), HPI monthlies (Freddie/Case-Shiller/FHFA), Trepp CMBS monthlies, NAHB monthly, MBA NDS quarterly — housing has more standing catalysts than several live top-level agents | `AGENTS/CARL/docket/CATALYSTS.tsv` |
| 5 | The single best open housing question — **GSE MF improving (Fannie 0.58% May, CRL-03 invalidated) vs CMBS MF deteriorating (maturity-adj 9.53%)** — is currently split across two owners: HOMER (Fannie side, CARL sub) and CREED (Trepp side, dormant Tier-2 with a `REVIVAL_PLAN.md`) | STATUS; `AGENTS/CREED/` |
| 6 | Root CLAUDE.md transmission chain (LABOR → CARL → REGINALD) has **no housing node**; housing signals route through a consumer-stress agent by historical accident | root `CLAUDE.md` |
| 7 | HOMER seed corpus already exists: 6 workbook TSVs (~294 rows incl. BUILDER/MULTIFAMILY/PIPELINE/STATE_HSG), KB.tsv 67 rows (FROZEN 7/10 w/ delegation provenance), state_vectors, domain/ — verified clean in the 7/10 restructure pass | `sub_agents/HOMER/` |

## 3. Proposed scope seams (CARL's draft — DAEDALUS to stress-test)

| Slice | Owner post-promotion | Note |
|-------|---------------------|------|
| HPI (nominal/real), supply, months-supply, listings, existing/new sales | **HOMER** | Asset-market core |
| Foreclosure pipeline (ATTOM/ICE/MBA), servicer stress | **HOMER** | CARL *receives* the consumer-stress read (foreclosure-as-household-event) like it receives gas-pump from HAWK data |
| Builders (GM compression, CRL-23 tariff leg) | **HOMER** | CRL-23 prediction ownership migrates or stays parent-CARL w/ HOMER as data owner — ★ judgment call |
| MF: GSE book (Fannie/Freddie) + CMBS book (Trepp) | **HOMER absorbs CREED's CMBS-MF lane** | Puts ONE owner on the GSE-vs-CMBS divergence. CREED disposition: retire lane or keep CREED for non-MF CMBS (office/retail) — ★ judgment call |
| Consumer-stress transmission (affordability squeeze, condo K-shape as K-shape evidence, "help with mortgage" behavioral, housing→V7/V8/V10 scoring) | **CARL retains** | CARL keeps convergence-matrix scoring; HOMER feeds it — same pattern as LABOR→CARL |
| Bank collateral / lender exposure (WAL/OZK/KRE, C&D lending) | **REGINALD unchanged** | HOMER→REGINALD becomes a first-class chain edge (Path C formalized) |
| FL geography | **Split stays as-is** | HOMER state-level housing; MARCO migration; CORAL whole-FL — reconcile-to-one-figure rule applies |

**Transmission chain after:** LABOR → CARL → REGINALD stays; add **HOMER → {CARL, REGINALD}** (+ HENRY wealth-effect edge on HPI). Root CLAUDE.md chain edit is Will-scoped.

## 4. Migration sketch

1. `git mv AGENTS/CARL/sub_agents/HOMER → AGENTS/HOMER` (history preserved; KB FROZEN banner + delegation provenance survive verbatim — unfreeze-and-renumber is NOT required day-1; new rows go to a fresh live ledger).
2. Stand up top-level surfaces per DAEDALUS maturity map: own CLAUDE.md rewrite (domain scope, boot/closeout symmetric), STATUS ≤250, NEXUS_BRIEF, docket, SCRATCH/MEMORY/ROADMAP split.
3. CARL STATUS sheds ~20 of 30 housing rows (keeps ~10 consumer-transmission rows w/ pointer to HOMER STATUS) — solves the B1/B5 over-cap backlog item as a side effect.
4. Prediction ledger: CRL-06 (foreclosures >70K/qtr) and CRL-23 (builder GM) — migrate vs parent-retain ★; CRL-03 already resolved (record stays in CARL CHANGELOG).
5. CREED CMBS-MF lane absorb/reconcile per §3 ★.
6. ROSTER + root CLAUDE.md roster-line + transmission-chain updates (PROME/Will-scoped); WALTER routing rules (BOARD `who_cares`) updated.

## 5. Costs, risks, counter-case

- **Standing-agent fixed cost:** boot/closeout, NEXUS_BRIEF, git discipline, staleness maintenance — permanent. HOMER-under-CARL is cheap.
- **Seam risk:** housing touches CARL/REGINALD/MARCO/CORAL/AEOLUS; a sloppy seam creates a 3-way overlap instead of today's 2-way. The §3 table is CARL's best cut — needs DAEDALUS adversarial pass.
- **Queue precedence:** ROSTER lists **WAL as next promotion candidate**; HOMER jumping the queue is a Will call.
- **Counter-case:** CARL's housing coverage has functioned (CRL-03 invalidation was caught cleanly, on its pre-registered trigger, by the current structure). Promotion optimizes for the NEXT leg (Path C realization, MF maturity wall) rather than fixing a demonstrated failure.

## 6. Timing (CARL recommendation)

- **This week (7/14–7/24): NO structural change.** Densest catalyst window of the month (CPI 7/14 / ATTOM 7/16 / builders 7/22 / Sub-V 7/24). HOMER runs its already-owed data refresh under CARL as-is — that refresh becomes the seed corpus either way.
- **DAEDALUS review in parallel** this week; Will decision after; **cutover in the post-7/24 quiet window** (~7/25–8/5, before NY Fed Q2 HHDC ~8/15).

## 7. ★ Judgment calls for the review (un-inferable from files)

★ CREED disposition (absorb CMBS-MF into HOMER vs keep CREED for non-MF CMBS) · ★ CRL-06/CRL-23 prediction ownership (migrate vs parent-retain) · ★ WAL-vs-HOMER promotion queue order · ★ whether HOMER also takes the rate/mortgage-spread surface (30Y PMMS, 10Y-FRM spread) or leaves it referenced-only (BROCK/HENRY own rates upstream).

**Reply path:** DAEDALUS → CARL inbox (+ PROME routing as needed). Silence ≠ received on this one — CARL will chase after the 7/16 ATTOM session if no ack.
