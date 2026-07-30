# OSPREY + FALCON Build — Execution Spec (HAWK split)

> 🗄 **DATED BUILD RECORD — states herein are as-of the build day; do NOT cite as current.** First content-grades landed at the 7/22 review: OSPREY L2, FALCON L3 (skip-level); HAWK L4-prov w/ sunset ~8/1. Current truth = FLEET_MAP row + `upgrades/PRODUCTION_REVIEW_2026-07-22.md`.

**Author:** DAEDALUS · **Date:** 2026-07-12 · **Status:** 🟢 EXECUTED 2026-07-12 (WP-1..5 complete; WP-4/5 run directly by DAEDALUS — verification in session record; registered + pushed same-day)
**Source spec:** `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md` (HAWK, Will-approved concept)
**Comprehension base:** `builds/hawk_split/MANIFEST_A_core.md` (core state + 106-file inventory) · `MANIFEST_B_ledgers.md` (VX/FLOW/STRIKES/KB row-level) · `MANIFEST_C_thesis.md` (predictions/lessons/scripts) — editors read the manifests, not raw HAWK.
**Precedent:** WATT/VULCAN/MIDAS build queue 7/10-11 (PAT-047 co-registration, PAT-048 instrument-light).

---

## 1. Ratified §13 decisions (DAEDALUS, subject to Will veto)

| # | Decision | Ruling | Rationale |
|---|---|---|---|
| 1 | Names | **OSPREY** (Russia/Ukraine) · **FALCON** (Iran/Gulf) | HAWK's proposal; raptor family = spun-out siblings signal; repo collision-grep clean 7/12 |
| 2 | Prediction prefixes | **OSP-xx / FAL-xx**. HAW-01..17 freezes under HAWK (no shared archive — one-owner rule PAT-006). Re-homes: **FAL-01 ←HAW-16**, **OSP-01 ←HAW-17**, each with back-pointer in Notes | Spec §8 as written |
| 3 | KB migration depth | **Freeze-in-place** under HAWK (whole 225-row KB = historical record, FROZEN banner). Siblings start fresh KBs (same 13-col schema + SCHEMA.tsv/VOCABULARIES discipline), citing `KB-HAWK-NNN` for provenance | PAT-021-consistent; row surgery is lossy and unauditable |
| 4 | OSPREY automated Russia-strike feed | **NOT at launch** (PAT-048). OSPREY launches instrument-light; a Russia strike-feed/sanctions-tracker analog is flagged in OSPREY SCRATCH + LESSONS as **priority first increment**, PAT-041-wired when built. The actual HAW-15 root-cause fix is the Tier-1 ledger discipline (§4 below), which IS built day-1 (trivially testable) | Untested scraper at launch = rc-2 broken-agent read; ledger discipline ≠ scraper |

## 2. Dispositions for the spec's gaps (found by readers A/C)

| Item | Ruling |
|---|---|
| `board_log.tsv` (66 rows, unaddressed by spec) | Freeze under HAWK (historical). Each sibling starts a **fresh** board_log.tsv — mirrors the fresh-KB pattern. HAWK-residual also starts fresh (its old log is pre-split mixed-theater) |
| `DECK_EVIDENCE.md` (17KB Iran deck, unaddressed) | Freeze under HAWK; FALCON CLAUDE.md FILES table carries a pointer (reference, don't copy) |
| `CALENDAR.md` (already FROZEN 7/9) + `catalyst_countdown.py` | Both stay frozen under HAWK. **Not ported** — CALENDAR is a dead surface superseded by STATUS forward-catalyst sections; porting the script would resurrect a dead pattern (PAT-040 orchestrator-theater) |
| Legacy scripts suite (`boot.py` FROZEN + war_monitor/thresholds/oil_infrastructure/sanctions_tracker + PLAN.md) | **Freeze in place under HAWK — do NOT port to FALCON.** All carry stale hardcoded Iran data (War Day 51, D82-C12-B6, Apr-13 facility states) that would look authoritative in a fresh scripts/ dir. FALCON's SCRATCH flags "refresh-and-pull-forward candidates from frozen AGENTS/HAWK/scripts/" as an owner-lane increment. Only **`baghdad_watch.py` + state JSON move** (tested, live, self-locating — the WATT-inherit pattern) |
| `SOURCES.md` | Three-way split: Iran/ME regional → FALCON; Russia/Ukraine regional → OSPREY; China-Taiwan + Venezuela/LatAm → HAWK; generic sections (Military/Diplomatic/News-wire/OSINT) → copy to all three |
| `MEMORY.md` | Freeze under HAWK. Hand-picked durable lessons (see-saw discipline, conf-code discipline, deferral-dynamic) **copied** (not moved) into each sibling's fresh MEMORY.md per theater relevance |
| `REMARK_20260628.md` (SUPERSEDED) + audits/ + research/ (except below) + domain/sources/ + STATUS archives | Freeze in place under HAWK (calibration/evidence history). FALCON gets pointers where load-bearing |
| `research/RUSSIA_OIL_INFRA_STRIKES_MAY-JUN2026.md` (Jun 18, live-load-bearing) | **Moves to OSPREY** `research/` — working reference for the Russia theater, cross-refs live KB IDs |
| `OPEN_THREADS_2026-07-09.md` | Archive under HAWK; the one live residue (Taiwan/Venezuela dormant re-sweep never actioned) → HAWK-residual STATUS backlog line |
| `OUTBOX.md` root stub (FROZEN) | Stays frozen under HAWK; siblings get `outbox/` dirs only |
| `templates/SCRATCH.template.md` | Copy to both siblings |
| HAW-03 (Venezuela, FAILED) | Frozen record stays under HAWK; its dormant-vector re-sweep lesson goes to **HAWK's** LESSONS (HAWK owns the dormant book) + cross-cutting copy note |
| LESSONS.md item-level | #1 → FALCON · #2 → FALCON + copy to OSPREY (general live-war boot methodology) · #3 → HAWK (+ copy-worthy note to siblings) · #4 mechanism-not-target + ledger-staleness → **all three** · parallel-channels lesson (lives in SUMMARY.md, not LESSONS) → OSPREY primary + cross-cutting copy |

## 2b. FLOW.tsv rulings (8 flagged rows, MANIFEST_B §2) + workbook non-TSVs

| Rows | Ruling |
|---|---|
| FLOW-04/05 (war→vol / war→credit, Iran-loaded) | **FALCON.** OSPREY builds its own Russia-war vol/credit transmission rows from scratch — flagged thin-at-launch, owner firms |
| FLOW-10 (sulphur→copper), -13 (Taiwan LNG), -15 (TSMC→PCE), -16 (helium) | **HAWK dormant** — VX-consistency (endpoints are HAWK's dormant vectors) |
| FLOW-17 (Iraq FM→supply→SPR) | **FALCON** (live Gulf-supply operational pathway; Gulf production = FALCON per spec §2/§3). VX-HAWK-IRAQ-01 stays **HAWK** per spec (deferred-to-BRENT dormant vector). ⚠️ Do NOT conflate the three Iraq-adjacent assets: FLOW-17→FALCON, VX-IRAQ-01→HAWK, baghdad_watch.py→FALCON |
| FLOW-18 (China SPR) | **HAWK dormant** + open question logged to HAWK owner-lane: retire-or-route-to-ZHAO/BRENT (not resolved in this build) |
| FLOW-07 (shadow fleet→Russia revenue, WARMING) | **OSPREY** core; its multi-theater "third-theater hydrocarbon" framing noted to HAWK's synthesis seed |
| Net FLOW counts | FALCON 11 · OSPREY 3 · HAWK 6 |

**Workbook non-TSVs:** `EXIT_PROTOCOL.md` → **FALCON** (live Iran-coded falsification rail; OSPREY gets a fresh Russia-coded exit section, thin-at-launch). `FOUR_STRUCTURAL_BREAKS_MAR18.md`, `POLITICAL_SUSTAINABILITY_MODEL.md`, `BOOT_LOG.md`, `workbook/STATUS_archive_*`, `PRICE_BREACHES.tsv` (already frozen) → freeze in place under HAWK (FALCON pointer where load-bearing). `SCHEMA.tsv` → copy to both siblings.

**STRIKES.tsv correction:** 36 rows (not ~43) — 32 RU-UA → OSPREY, 4 GULF-IRAN → FALCON, 0 untagged. **FALCON founding mandate (day-1 SCRATCH item): Gulf-Iran strike-ledger backfill sweep** — its inherited ledger is 4 Mar-vintage seed rows and SUMMARY's analysis layer is ~95% Russia. This asymmetry is explicit, not silently absorbed. KB freeze note: 2 duplicate IDs (KB-HAWK-131/132 ×2) — note in FROZEN banner, no surgery.

## 2c. ⚠️ POST-MORTEM ON §2b — TWO SEEDING DEFECTS, FOUND BY FALCON 2026-07-30 (18 days post-build)

*Added by DAEDALUS on FALCON's packet (`inbox/2026-07-30_from-FALCON_war-split-build-spec-asymmetry-and-molecule-blindspot.md`), Will-approved. FALCON verified itself by rewriting and OSPREY by reading their files; both findings are against **this spec**, not against either agent's judgment. Kept here rather than only in PATTERNS because this is the document that produced them.*

### D1 — I allocated a mechanism row by WHERE ITS INSTANCES HAPPENED, not by WHERE THE MECHANISM CAN FIRE

`FLOW-HAWK-20` (*refinery hit → domestic refining capacity lost → crude that cannot be refined is EXPORTED → crude UP, products DOWN → the repricing lands on the PRODUCT channel, not Brent*) went to **OSPREY** and was never considered for FALCON, because its historical instances were Russian. **The mechanism is not Russian. Both theaters have refineries.**

**Cost, concretely:** the Houthis hit Aramco's 400 kbpd **Jazan** refinery 7/25; Aramco **shut** it 7/27. FALCON had to derive from scratch on 7/30 that this is **crude-BEARISH** and author `FLOW-FALCON-02` to hold it — a sign OSPREY had written down since **June 19**. In the interval the fleet-facing risk was that *"Aramco facility hit"* reads bullish-crude by default, and FALCON was telling BRENT *"cracks and diesel, not flat crude"* on judgment with no pathway row behind it. The §2b table above shows the defect in its own wording — rows were routed as *"Iran-loaded"* / *"Russia core"*, i.e. by instance provenance.

> **RULE (adopted, generalized to every split/promotion): allocate MECHANISM rows by whether the mechanism CAN OCCUR in the child's theater — never by which theater the row's historical instances came from.** Instances are evidence; the mechanism is the asset. **Build-time test, one question per non-migrated row: *"can this mechanism fire in that child's theater?"*** If yes, the child gets a copy — duplication of a universal mechanism across two children is correct, not redundant. That single question would have caught this.

### D2 — 🔴 THE ONE THAT MATTERS MORE: **neither sibling can represent a GAS/LNG shock.** Verified in both.

FALCON: no gas/LNG row of any kind. OSPREY (grep, inbox excluded): `Nord Stream` · `TurkStream` · `Power of Siberia` · `pipeline gas` · `Russian gas` · `LNG` → **zero hits**; three vectors and three FLOW rows, all oil. **Russia is the world's largest gas exporter; Qatar is the world's largest LNG exporter; both sit inside these two agents' theaters.** Every seeded row runs through oil price or a chokepoint.

**It already fired and it killed a registered kill-switch.** `FAL-03` — FALCON's explicit falsification test for the thesis it exports to BRENT/HENRY/SAM/CARL — resolved **FAILED on day 4 of a 21-day window**, and one firing route *was already true on the day it was registered*: a **QatarEnergy force majeure on LNG live since 2026-03-24**, ~12.8 Mtpa ≈ **17% of Qatar's export capacity**, 3–5 year repair, serially extended. It ran four months while FALCON broadcast *"zero confirmed barrels offline"* to four agents.

> **The architectural point, in FALCON's words and worth preserving verbatim: it was UNREPRESENTABLE, not merely unnoticed.** A force majeure is not a strike; LNG is not oil. So the fact had no vector, no pathway, no threshold and no staleness affordance — and **a file with no row-shape for a class of event is silent about it in a way indistinguishable from that event not happening.** No diligence *inside* the agent recovers this: FALCON's arithmetic was right, its ledger current, its base rate freshly re-derived. **Reproducibility does not test scope match.** It surfaced only because WALTER routed a signal from outside the instrument's scope.

> **RULE (adopted, every build): the NAME-THE-UNREPRESENTABLE-SHOCK check.** At build time, for each agent, ask ***"name a shock in this theater that NONE of the seeded rows has a row-shape for."*** If the answer is not "none," either seed the row **or write the exclusion down explicitly and name who owns it** — because ***"that belongs to another agent"* and *"I am blind to it"* look identical from outside, and only one of them is safe.** FALCON's fix shape is the model: `VX-FALCON-GASLNG-01` + `FLOW-FALCON-01`, with the vector's Notes scoping *out* gas **pricing** (FALCON owns the supply-loss fact in-theater; SAM and the macro agents own the price leg). The boundary is written down, so the blind spot cannot hide behind it.

### D3 — build-time descriptors written in state tense (FILES tables)

FALCON found 8 rows in its own FILES table describing build-day state as current 18 days on. **Its cohort-wide inference was tested and is only half right** — see PAT-072's sibling entry and `STATUS.md`: WATT / VULCAN / MIDAS / HOMER are clean, OSPREY carried 3 stale counts + 1 **live-wrong pointer** (`ANALYSIS_2026-07-12.md` named as current while `ANALYSIS_2026-07-23.md` existed) + 1 undocumented file. **The discriminator: *provenance* statements about spinout are permanently true ("seeded from HAWK, IDs kept"); *quantity* statements decay ("3 rows", "0 at spinout"), and *pointer* statements decay dangerously.** OSPREY's table was rewritten in role terms 7/30; the blueprint rule is below.

### Status of the fixes

| Fix | Where | State |
|---|---|---|
| Mechanism-allocation rule | this §2c + `BLUEPRINTS/market-agent.md` §6 + `builds/REGISTRATION_CHECKLIST.md` | ✅ 7/30 |
| Name-the-unrepresentable-shock check | this §2c + blueprint + checklist | ✅ 7/30 |
| FILES-table role-tense rule | blueprint | ✅ 7/30 |
| OSPREY FILES table rewritten | `AGENTS/OSPREY/CLAUDE.md` (idle-verified, 6d) | ✅ 7/30 |
| OSPREY gas/LNG + vol/credit gaps flagged on its own FLOW row | `AGENTS/OSPREY/CLAUDE.md` | ✅ 7/30 — **seeding the rows is the owner's call, not mine** |
| FALCON `VX-FALCON-GASLNG-01` + `FLOW-FALCON-01` | FALCON | owner-lane, self-proposed |

## 3. Pre-freeze hygiene (execute DURING WP-3, before banners go on)

1. **Re-total the PREDICTIONS.tsv scoreboard preamble** → `5C/8F/1P/1V/2 OPEN (HAW-16, HAW-17)` + note "HAW-16/17 re-homed to FAL-01/OSP-01 2026-07-12" (preamble currently stale: lists HAW-15 OPEN, undercounts FAILED).
2. **Backfill PREDICTIONS_ARCHIVE.md** with the 5 owed sections (HAW-10/12/13/14/15): mechanical verbatim-from-TSV stubs + pointer to fuller post-mortem material (LESSONS #4, STRIKES SUMMARY, 7/12 commit trail), each stamped `backfilled-at-freeze 2026-07-12`. Deeper analytical post-mortems stay HAWK-owner-lane.
3. Banners/notes — AMENDED at WP-3 (post-WP-1/2 refinement): **KB.tsv stays LIVE under HAWK** (header split-note: rows ≤223 = pre-split both-theater history incl. dup IDs 131/132; post-split rows KB-HAWK-224+ = synthesis/dormant facts only; theater facts now accrue in OSPREY/FALCON KBs). "Freeze-in-place" = no row surgery/migration — HAWK remains an active agent and keeps one live ledger. **board_log.tsv continues under HAWK** w/ a split-marker comment line (fresh logs were for the siblings). **PREDICTIONS.tsv stays HAWK's live ledger** (HAW-18+ for synthesis/dormant predictions): re-totaled preamble, HAW-16/17 rows re-marked `REHOMED → FAL-01/OSP-01 2026-07-12` (open exposure now 0 at HAWK). FROZEN banners (PAT-023) only on genuinely dead surfaces: original STRIKES.tsv + SUMMARY.md (successors = sibling ledgers + HAWK's thin derived cross-war summary), MEMORY.md stays live (HAWK's own).

## 4. Tier-1 ledger fixes (spec §7) — bake into BOTH siblings day-1

1. Strike-ledger header carries `# swept-complete through: YYYY-MM-DD` high-water-mark + scope label ("material subset — absence of a row ≠ absence of a strike; see swept-through mark").
2. Boot staleness check on the strike ledger: 3-line boot-doc step — newest-row-date + swept-through-date vs today when theater ACTIVE (cwd-proof invocation, PAT-031). Uses in-content dates, not git-time (PAT-039).
3. Closeout strike-sweep step: date-careful sweep from high-water-mark → today, then advance the mark.
4. Raw-log vs interpretation split: `STRIKES.tsv` = rows only; patterns/aggregates live in a dated `ANALYSIS_YYYY-MM-DD.md` (regenerated, never appended blind).

## 5. Scaffold structure (per sibling — market-agent blueprint + inherited content)

```
AGENTS/{OSPREY,FALCON}/
  CLAUDE.md          # blueprint-conformant: identity/scope (disaggregated from HAWK per manifests),
                     # boot (incl ledger_staleness <NAME> --quiet cwd-proof; FALCON: + baghdad_watch step;
                     # both: strike-ledger staleness step), closeout (incl strike-sweep + mark-advance),
                     # KB schema + Admiralty/epistemic rules (verbatim inherit), EXIT RULES (theater-coded),
                     # CROSS-AGENT SIGNALS (theater rows only; routine reads route via HAWK synthesis,
                     # acute 🔴 direct to BRENT w/ HAWK cc), OIL-HANDOFF banner (inherit), FILES table
  STATUS.md          # seeded from HAWK STATUS theater sections per MANIFEST_A §1; BOTTOM LINE; ≤250 ln
  SCRATCH.md         # seeded per MANIFEST_A §3 split; flags first-increment items
  NEXUS_BRIEF.md     # fresh, theater-scoped
  LESSONS.md         # per §2 ruling above
  MEMORY.md          # fresh + hand-picked copies
  SOURCES.md         # per §2 split
  workbook/          # fresh KB.tsv (schema-seeded, 0 rows) + SCHEMA.tsv copy + VX.tsv (migrated theater rows,
                     # same schema) + FLOW.tsv (migrated theater rows) + EXIT_PROTOCOL (theater-coded)
  thesis/            # PREDICTIONS.tsv (new prefix, preamble w/ inherited calibration lessons per MANIFEST_C §2,
                     # seeded FAL-01/OSP-01) ; FALCON also inherits THESIS.md/TIMELINE/CHANGELOG wholesale
                     # (100% Iran content — keeps its SUPERSEDED banner + rewrite backlog item)
  domain/energy-strikes/  # STRIKES.tsv theater rows (per MANIFEST_B) + Tier-1 header + dated ANALYSIS file
                          # from SUMMARY.md's theater half
  inbox/{processed,WALTER/processed}/ + outbox/delivered/  # fresh, .gitkeep
  board_log.tsv      # fresh
  templates/SCRATCH.template.md
  scripts/           # FALCON: baghdad_watch.py + state (git mv). OSPREY: empty (instrument-light, PAT-048)
```

**FALCON additionally inherits:** A/B/C/D scenario ladder (STATUS + CLAUDE SCENARIO FRAMEWORK), 10-vector Iran convergence matrix, CONFIRMED/CLAIMED/UNVERIFIED table, Next-Rung Tells, REMARK/DECK pointers.
**OSPREY additionally inherits:** off-core Russia 3-channel frame (refineries/products · crude-terminals · shadow-fleet tankers) as its channel model, crude-vs-products flip-triggers from SUMMARY.md, RUSSIA_OIL_INFRA research file. OSPREY has NO A/B/C/D ladder — its framework is the channel model (per spec §2); EXIT rules built Russia-coded from scratch (flagged as thin-at-launch, owner firms).

## 6. HAWK residual (WP-3)

- CLAUDE.md rewritten: synthesis + dormant-book identity; boot reads OSPREY+FALCON NEXUS_BRIEFs (cwd-proof paths) + own dormant VX; NO strike ledgers, NO scenario ladder; closeout = synthesis STATUS + cross-war NEXUS_BRIEF.
- STATUS.md re-cut: cross-war reconciliation dashboard (decoupling read, double-count check, war-risk/shipping aggregate) + dormant book (Taiwan/Venezuela/trade/Suez/Malacca/defense/sanctions-regime) + pointers. Seeded from current Bottom Line ¶ + Cross-Agent Implications synthesis rows.
- Workbook: KB frozen; VX keeps dormant rows (per MANIFEST_B assignment); FLOW keeps FLOW-19 (canonical decoupling thesis home — LIVE) + rows 01-18 stay MUTED/frozen; fresh thin PREDICTIONS.tsv (prefix stays HAW-, continuing from HAW-18) for dormant-book + synthesis predictions.
- Strike data: thin derived cross-war summary table only (regenerated, not maintained).
- Everything frozen per §2 stays physically in place under AGENTS/HAWK/.

## 7. Work packages + sequencing

| WP | What | Writes to | Runs |
|---|---|---|---|
| WP-1 | Scaffold + migrate FALCON | `AGENTS/FALCON/` only | parallel w/ WP-2 (reads HAWK, writes own dir) |
| WP-2 | Scaffold + migrate OSPREY | `AGENTS/OSPREY/` only | parallel w/ WP-1 |
| WP-3 | HAWK re-cut + freezes + pre-freeze hygiene (§3) + baghdad_watch git mv → FALCON | `AGENTS/HAWK/` (+1 git mv into FALCON) | AFTER WP-1/2 complete (they read HAWK surfaces WP-3 rewrites) |
| WP-4 | DAEDALUS verification pass: boot-doc dry-run both siblings, ledger_staleness rc, render checks, seam grep (no orphaned refs), STATUS ≤250 | — | after WP-3 |
| WP-5 | Registration: ROSTER + root CLAUDE chain + AGENTS.md (+_INDEX/_NETWORK) then FLEET_MAP rows + FLEET_DIRECTORY regen (PAT-047 order) | shared files (Will-authorized or PROME packet) + own | after WP-4 |

Editors: Sonnet, one per WP, prompts carry PAT-046 delivery clause. Commits: path-scoped per new-agent dir; HAWK edits committed under AGENTS/HAWK pathspec.

## 8. Registration deltas (WP-5)

- **ROSTER:** +OSPREY +FALCON (Market, active, provenance "spun out of HAWK 2026-07-12, OZK/CORAL/AEOLUS precedent"); HAWK reclassified "geopolitical synthesis + dormant book."
- **Root CLAUDE.md chain:** `HAWK → BRENT (oil/energy)` → `{OSPREY, FALCON} → HAWK (geopol synthesis) → BRENT` (acute direct-to-BRENT allowed, HAWK cc'd). Active count 25→27.
- **FLEET_MAP:** OSPREY/FALCON new rows — **L1-scaffold, Conf H, note "seeded from HAWK L4 content — first content-grade after first real session"** (PAT-019); HAWK row re-noted (L4 grade carries, scope shrunk — re-read at 7/18 production review).
- **profiles/HAWK.md:** staleness note + post-split re-profile queued; siblings get profiles at first content-grade.
