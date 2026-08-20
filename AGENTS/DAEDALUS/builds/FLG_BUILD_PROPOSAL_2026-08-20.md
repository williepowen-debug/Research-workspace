# BUILD PROPOSAL — FLG (Flagstar Financial) as a standalone per-bank agent

**Author:** DAEDALUS · **Date:** 2026-08-20 16:21 EDT · **Status:** 🟡 PROPOSED — Will-gated, nothing scaffolded
**Requested by:** Will, in-session, off REGINALD's rebuilt convergence matrix (`75f0dd18b`, 2026-08-20 16:04 EDT — 17 min before this file)
**Job:** #1 Build · **Blueprint:** `BLUEPRINTS/market-agent.md` · **Template:** FERT re-charter `595ac2306` (greenfield), *not* WAL (promotion)

---

## RECOMMENDATION IN ONE LINE

**Build it — standalone `AGENTS/FLG/`, seeded from REGINALD's validated Call-Report pipeline, launched instrument-light, scoped to the *mechanism* not the bank.** And fill the promotion-queue seat that has sat **UNASSIGNED for 26 days** (`PROME/ROSTER.md:176` — *"Nominations are DAEDALUS's lane via maturity review, Will-gated"*). FLG is the nomination.

---

## 1. WHAT

A standalone market-class agent at `AGENTS/FLG/` owning **one bank and one transmission mechanism**:

> **NYC rent-regulated multifamily repricing → CRE concentration → nonaccrual formation → reserve adequacy → capital.**

Not "Flagstar the company." The scope is the mechanism, fixed at build time in *structure* (a closed instrument list + an exclusions register), not in prose — PAT-002 / PAT-018, because an open-ended "watch the bank" mandate drifts and goes stale.

| Element | Ship at build | Deferred |
|---|---|---|
| `CLAUDE.md` charter (market-agent blueprint, §1–§8) | ✅ | — |
| `STATUS.md` + BOTTOM LINE | ✅ | — |
| `workbook/KB.tsv` seeded from REGINALD's FLG rows | ✅ | — |
| `workbook/MI3_FLG.tsv` — 12 validated quarters, RSSD 694904 | ✅ | — |
| `workbook/TRIGGERS.tsv` — seeded `[EST]`-marked, **unratified** | ✅ | ratify at first live session |
| `workbook/PREDICTIONS.tsv` — cut empty, Class-3 enum + `Resolve_By` + `If_Falsified_Action` | ✅ | first rows after base-rating |
| `boot.py` — wall clock + ledger-staleness marker contract + predictions-due + triggers-due | ✅ | — |
| **Dated falsification surface** (blueprint §4, L3 requirement) | ✅ **day 1, non-negotiable** | — |
| THESIS.md v0.1 | ✅ skeleton + open questions | thesis-of-record after first live session |
| Any new scraper / fetcher | ❌ **PAT-048** | inherit REGINALD's proven FFIEC path |

---

## 2. WHY — and the "why" is stronger than the gap REGINALD named

REGINALD's stated gap is *"FLG is now my top-scored name and I have no thesis file on it."* True, and sufficient on its own. But the measurement underneath it says something sharper, and it is a **capital-allocation** fact, not a documentation one.

### 2a. The desk owns puts on the mid-pack names and has zero exposure to its own #1

| Name | v1 score (**dead**) | v2.0 score | In the book? (FORGE reconcile 2026-08-14) |
|---|---|---|---|
| **FLG** | 8 — *last* | **🔴 6 — 1st** | **Nothing.** |
| EGBN | 20 — 1st= | not in the ranked head | Nothing |
| WAL | 20 — 1st= | 2 — mid | ✅ Sep-18 67.5P + 70P — marks **0.05 / 0.10**, from 0.85 |
| OZK | 13 | mid | ✅ 42.5P + 45P Aug-21 — 42.5P marks **$0.05** |
| CFG | 15 — 3rd | 0 — *last* | Nothing |

*(v1/v2 scores: `AGENTS/REGINALD/BANK_EXPOSURE_MATRIX.md` §5 + ranked table, `75f0dd18b`. Marks: `FORGE/STATUS.md`, reconciled 2026-08-14, **intraday ~09:45 ET, not closes**.)*

Three of the bank legs mark at exactly **$0.05** and FORGE's own D-21 caveat says that residual **should not be read as realizable**. So: the bank book is spent, it is spent on names the rebuilt instrument calls mid-pack, and the name that instrument ranks first has never had a thesis file.

REGINALD wrote the finding himself and it belongs in this proposal verbatim:

> *"The desk's attention has been on WAL and OZK; on instrumented CRE concentration and credit quality, **FLG, EGBN and AMTB** are the elevated names and **WAL and OZK are mid-pack**."*

**Two of the fleet's 31 seats are dedicated per-bank agents — OZK and WAL — and both are now mid-pack.** That is a structural misallocation of fleet attention, it was invisible until the instrument became reproducible, and correcting it is exactly the design-layer call I own.

### 2b. FLG is tradeable, and this desk has already traded it

- **Live: $13.49, −1.46%, 2026-08-20** (`FORGE/tools/market-data/fetch.py`, pulled for this proposal — not a STATUS quote).
- **Held before:** `FLG $13P ×3, $45` — `AGENTS/RED/research/POSITION_RECONCILE_2026-06-10.md:37`; FLG also appears in RED's Jul-17 expiry cluster (`CALENDAR.md:160`).

The $13 strike is ~ATM today. This is not a research curiosity with no trade path — it is an optionable name with an existing execution precedent at the money.

### 2c. REGINALD cannot absorb this, and we already diagnosed why

REGINALD's own FLEET_MAP row (last re-cut 8/7): **15 unprocessed inbox packets · VX.tsv +126d stale · THESIS v1.4 own trigger expired · 7 OPEN predictions 165d untouched.** The desk just produced the fleet's best work of the week — its *analysis* capacity is not the problem; its *maintenance* capacity is, which is PAT-061 exactly (analysis structurally crowds out maintenance on print-driven agents).

And the WAL promotion — the closest precedent — was justified on this identical finding, in REGINALD's own words at the time:

> *"Hub-load conflict is real: today's audit found the WAL fossil surfaces rotted **while REGINALD's hub surfaces stayed current**. A dedicated owner is the structural fix; banners were the interim one."* (`inbox/processed/2026-07-17_from-REGINALD_wal-promotion-request.md`)

Handing the #1-ranked name to the most backed-up desk in the fleet re-runs a failure we have already written down (PAT-043).

---

## 3. SHAPES CONSIDERED, AND WHY THE OTHER THREE LOSE

| Option | Verdict | Reason |
|---|---|---|
| **(a) Standalone `AGENTS/FLG/`, seeded greenfield** | ✅ **RECOMMENDED** | Dedicated owner = the diagnosed fix (§2c). Seed corpus is real (§4), so this is not an empty labyrinth. FERT proves the greenfield path works — 4 days ago, one commit. |
| (b) Sub-agent `AGENTS/REGINALD/FLG/`, seed-then-promote (the WAL path) | ❌ | The *only* validated path — OZK/CORAL/HOMER/WAL were all promotions — but it puts the new corpus inside the desk that measurably cannot maintain it. **Choosing it knowingly repeats a failure we diagnosed and already paid to fix once.** |
| (c) One "elevated cohort" agent — FLG + EGBN + AMTB | ❌ | Efficient-looking, and wrong. Three different mechanisms (FLG = NYC rent-regulated MF · EGBN = DC-area CRE · AMTB = Miami/LatAm). Merging them buries the mechanism and leaves no single thesis-of-record — the one thing OZK and WAL are actually graded on. PAT-002. |
| (d) No new seat — REGINALD writes a thesis file | ❌ *as the whole answer* | It is the right **interim** move and costs one session. But it does not fix §2a, and §2c says it rots. **Worth doing anyway if (a) is declined** — see FALLBACK. |

**Precedent note, stated plainly because it cuts against me:** every per-bank agent this fleet has (OZK Apr, WAL Jul) was a *promotion* of an existing sub-tree. FLG would be the **first greenfield per-bank build**. The de-risking answer is that the seed is not zero (§4) and that FERT — my own build, 2026-08-16 — established the greenfield template with a Will-ruled "gates ratify at first live session **after** base-rating, nothing registered yet" discipline. FLG ships under that same discipline.

---

## 4. THE SEED IS REAL — this is not PAT-001 dead scaffolding

| Asset | Where it is now | State |
|---|---|---|
| **12 quarters of FFIEC Call Report data**, FLG RSSD **694904** (FLAGSTAR BANK, N.A.), 9/30/2023 → 6/30/2026 | `AGENTS/REGINALD/workbook/MI3_COHORT.tsv` | **Validated** — last 4 quarters marked `REPRODUCES`; MDRM denominators declared per row |
| Scored matrix row with **named instrument + externally-anchored band** (SR 07-1, 300% supervisory line) | `BANK_EXPOSURE_MATRIX.md` v2.0 | Fresh, 2026-08-20, method-documented |
| 9 KB rows | `REGINALD/workbook/KB.tsv` | Cohort-level |
| Known mechanism + public record | — | Former **NYCB** (`AGENTS/VOCABULARIES.tsv:90`); 2024 crisis, capital raise, MSR sale, ongoing deleveraging |

The pipeline that produced the Call Report rows is **REGINALD's, proven, and reproducing**. FLG inherits its *output* by extraction — it does not get a new scraper on day 1 (PAT-048).

---

## 5. ⚠️ THE COUNTER-CASE — state it before building, not after

**The seed data partly undercuts the bear framing, and a new agent built off a "worst-ranked" score is at risk of being built to prove it.**

From the same MI3 rows, FLG 9/30/2023 → 6/30/2026:

| Measure | 9/30/2023 | 6/30/2026 | Δ |
|---|---|---|---|
| Total assets | $111.17B | $87.71B | **−21.1%** |
| Total loans | $85.92B | $61.19B | **−28.8%** |
| MI3 `v1_pct` | 5.28% | 3.65% | **−1.63pp** |

The bank is shrinking hard, loans faster than assets, and the MI3 measure is *falling*. A thesis that reads 327.5% as a pure danger signal has to explain why the balance sheet it sits on has contracted by a fifth.

**Sharper, and it is a construct-validity question about the instrument itself:** channel 1 is `(construction + multifamily + non-owner-occ NFNR) / total risk-based capital`. If the easier-to-exit assets left first — and for FLG they plausibly did, given the mortgage/MSR disposals — then **the CRE ratio can RISE while absolute CRE risk FALLS**, because the numerator is the stickiest part of a shrinking book. That is PAT-090 inverted (*"ask whether the measure can fall because things got better"* → here, whether it can *rise* because things got better).

I cannot resolve this from the repo — it needs the CRE-composition and capital series, which is REGINALD's instrument. **It is not a refutation and I am not asserting one.** It is a question that must be routed to the instrument's owner and answered *before* FLG registers a threshold. Consequences for the build spec, both binding:

1. **Dated falsification surface ships day 1** (blueprint §4), and the deleveraging counter-thesis is its first entry.
2. **No threshold registers before it is base-rated** — FERT's Will-ruled discipline, applied here by default.

---

## 6. THREE LIVE DEFECTS — fixable now, independent of this ruling

These are consequences of the matrix rebuild that a new agent would **not** fix, and that building one might mask. Flagged here, routed by packet; **I edit none of them** (all outside my pathspec, all live-owner surfaces).

| # | Defect | Evidence | Owner |
|---|---|---|---|
| **1** | **WALTER's live dispatch cache carries the dead score.** FLG sits at `TIER-2, score 8, Primary thesis: —` in a file WALTER greps *at signal-dispatch time*. Signals on the #1-ranked name are being routed at second-tier priority off a score REGINALD just killed. *(The file's own header says trust REGINALD's TSV over the cache — self-aware, and still stale at the point of use.)* | `AGENTS/WALTER/design/CROSS_REFS/REGINALD.md:55` | WALTER |
| **2** | **FLG is invisible to the fleet's 8-K monitor.** CIK never resolved — `FLG \| Unknown \| Needs first check`. The top-ranked name cannot trigger a filings alert. | `AGENTS/OTTO/EDGAR_8K_MONITOR.md:83,110` | OTTO |
| **3** | **The dead v1 scores have already been cited into a live decision.** REGINALD's own commit message: *"Anyone citing 'EGBN 20' — including TERRY, in a packet that fed a live card decision — could not have reproduced it."* TERRY has the publisher-side packet; the consumer sweep for the other five dead scores is worth confirming as complete. | `75f0dd18b`; `AGENTS/TERRY/inbox/2026-08-20b_from-REGINALD_*` | REGINALD / TERRY |

Defect 1 is the one I would fix today whatever Will rules on the agent — it is a live routing error on the name we just decided matters most.

---

## 7. EFFORT

| Phase | Scope | Estimate |
|---|---|---|
| **Build** | Charter + STATUS + THESIS skeleton + 4 workbook ledgers + `boot.py` (capable cases watched per CHECK_STANDARD §3) + falsification surface | **1 session** — FERT was 5 files, one commit |
| **Registration** | 16-surface checklist (`builds/REGISTRATION_CHECKLIST.md`): ROSTER first per PAT-047 → root `CLAUDE.md` → `AGENTS.md` → `_INDEX` → `_NETWORK` → 5 thematic group pages → WALTER routing → FLEET_MAP → directory regen → REGINALD seam + **behavioral-registry grep (item 13, PAT-063)** → my own script registries | same session |
| **Seed extraction** | FLG rows out of `MI3_COHORT.tsv` + KB — REGINALD-owned, by packet, or direct if idle+approved | ~½ session, REGINALD-gated |
| **First live session** | Base-rate → ratify triggers → thesis-of-record v1.0 | separate, FLG's own |

**Two Will-gates, not one:** ① approve the build (this file), ② PROME routes the ROSTER + root-canon edits, which are Will-scoped and never applied silently (`ROSTER.md:33`).

---

## 8. EXPECTED VALUE

- **Direct:** a thesis-of-record and a trade path on the cohort's top-scored name, at $13.49 with an ATM strike precedent — currently zero coverage.
- **Structural:** closes the promotion-queue seat open since 2026-07-25 and rebalances two per-bank seats that the rebuilt instrument now says are pointed at mid-pack names.
- **Method:** first **seeded greenfield** per-bank build — if it works it is the pattern for EGBN/AMTB; if it fails, it fails cheap (one session, one directory, clean `git mv` to `_archive/`).
- **Honest ceiling:** FLG lands at **L1–L2 at birth** and cannot reach L3 until predictions resolve and the falsification surface is dated and exercised. Nobody should read the build as an L3 agent arriving (PAT-019 / PAT-052 — newborn surfaces fossilize at build vintage within days).

---

## 9. FIRST STEP

**On Will's approval:** draft `AGENTS/FLG/CLAUDE.md` against `BLUEPRINTS/market-agent.md` with the §1 scope statement and the PAT-073 exclusions register written **first** — because the scope guard is the part that decides whether this agent is alive in six months, and because item 14② of the registration checklist (*"name a shock in this domain that no seeded row has a row-shape for"*) is answerable only against a written scope.

**Before that, and not gated on the ruling:** route defect 1 (WALTER dead-score cache) — one packet, live routing error, today.

## FALLBACK IF (a) IS DECLINED

Option (d), explicitly scoped so it does not silently become permanent: REGINALD writes `FLG_THESIS.md` in one session, and the FLG seat is registered on the promotion queue at `ROSTER.md:176` with a **dated** revisit — so that "interim" has an owner and an expiry instead of becoming the status quo by default (`finding_dated_carry_item_has_no_expiry_check`).

---

*Nothing in this proposal has been scaffolded, registered, or routed. Two guards hold: express permission, and an idle target.*

---

## ⚠️ CORRECTION — appended 2026-08-20 ~17:1x ET, post-approval, by the author

**§2c overstated REGINALD's current load, and §2c was a load-bearing argument.**

The figures there ("15 unprocessed inbox packets · VX.tsv +126d stale · 7 OPEN predictions 165d untouched") were quoted from REGINALD's `FLEET_MAP.tsv` row and **correctly stamped "last re-cut 8/7"** — but I used a 13-day-old row to support a **present-tense** claim that REGINALD cannot absorb new work. Re-measured at the artifact during closeout:

| §2c claim | Measured 2026-08-20 |
|---|---|
| 15 unprocessed inbox packets | **1** — and it is this build's own packet, sent minutes earlier |
| VX.tsv +126d stale | **Refreshed 2026-08-12**, with a documented four-bucket row disposition |
| ledgers stale | `python3 scripts/ledger_staleness.py REGINALD --quiet` prints **nothing** — clean |

**What survives, and what does not.** The *headcount* argument does not survive: REGINALD is current, not backed up. What survives is the **structural** argument, which never depended on today's queue depth — the hub-load pattern (PAT-043 / PAT-061: hub sessions refresh hub surfaces first, sub-trees rot) is why the WAL sub-tree fossilized *while REGINALD's own surfaces stayed current*, which is REGINALD's own diagnosis in its promotion request. That pattern is about **where a corpus lives**, not about how busy its owner is this week. The capital-allocation finding (§2a) and the OZK/WAL precedent are untouched.

**The recommendation is unchanged and the ruling stands.** But Will approved partly on a claim that was stale, and that is worth saying plainly rather than leaving the flattering version in the record.

**Two failures of my own, banked:**
1. `finding_dated_carry_item_has_no_expiry_check` — a carried assertion is a string; reading it never evaluates it. A stamp records vintage, it does not license present-tense use.
2. **PAT-050 again, and sharper than usual: the stale row was MINE.** `FLEET_MAP.tsv` is the file whose currency I own, and I used its 13-day-old cells as live evidence in a build proposal without re-measuring. The map is a hygiene input, not a source of current facts about another desk.

**Actions taken:** REGINALD's `FLEET_MAP` row annotated with the dated measurement (current-state correction only — the level is NOT re-graded here; that is a Production Review action against a real read). Correction relayed to PROME and REGINALD.
