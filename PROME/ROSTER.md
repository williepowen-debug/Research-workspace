# PROME/ROSTER.md — Verified Agent Roster
**Owner:** Prome · **Last verified:** 2026-06-27 (commit-activity + STATUS-recency pass) · folder-existence reconciled 2026-06-30 · **ZHAO reactivated dormant→active 2026-07-05** (8 commits 7/4, Will-approved) · **counts refreshed 2026-07-10** (PROME commit-activity re-run — classification UNCHANGED; no active/tier-2/dormant flips) · **OZK flipped dormant→active 2026-07-22** (revived 7/18 exactly on its revival gate — Q2 print 7/21; ~15 commits incl. the four-rail Stage-1 grade; DAEDALUS added its first FLEET_MAP row L4 same day) · **WAL REGISTERED ACTIVE 2026-07-25 on cutover day** (Will-approved 7/22; DAEDALUS WP-W0 → WP-W1 `ed1ce777` git-mv `AGENTS/REGINALD/WAL` → `AGENTS/WAL`; ACTIVE count 29→30; ~~WP-W2 open~~ **WP-W2 EXECUTED same day `37ee2748e` — stale-open claim caught by spine-audit #7, 8/3** — see ††††† ) · **VIRGIL registered OFF-FLEET 2026-08-19** (Will-directed in-session; a NEW non-fleet section — ACTIVE/TIER-2/DORMANT membership and all five responsibility classes UNCHANGED, so no root `CLAUDE.md:26` mirror edit is owed) · **FERT REGISTERED ACTIVE 2026-08-16 on cutover completion** (Will-ruled RE-CHARTER same day, `PROME/proposals/2026-08-16_fert-recharter-RULED.md` §2, WAL precedent; DAEDALUS build landed `595ac2306` beating the 8/23 checkpoint by 7d; ACTIVE count 30→31; out of ARCHIVE SOURCES — see ††††††)

**Method:** classification by **30/60-day git-commit activity** (the "is it actually running" signal) + STATUS mtime + self-declared domain — *not* a prose guess. Re-verify by re-running the activity map (`git log --since=<60d> --pretty=%s | grep -cE '^NAME'` per agent) and diffing against this table.

> **★ PHASE 1 TAXONOMY PASS EXECUTED 2026-08-05** (roster-responsibility migration, RAV plan v4 → Will-ruled Phase 0 → RAV preflight → this pass). The flat `ACTIVE — persistent domain owners (30)` bucket is now split into five descriptive classes. **Membership is unchanged: 30 agents in, 30 agents out, verified by name-set diff — this pass re-labels, it does not add, remove, promote or demote anyone.** Rulings artifact: `PROME/proposals/2026-08-04_roster-phase0-ruling-table-RULED.md`. Preflight: `PROME/inbox/processed/2026-08-05_from-RAV_roster-phase0-preflight-addendum.md` (durable copy: `AGENTS/RAV/runs/2026-08-05_roster-phase0-preflight-addendum.md`). **Out of scope by ruling and untouched:** TIER-2, DORMANT, RETIRED, ARCHIVE SOURCES, SPECIAL, TOOL-CLASS, spinouts, coverage notes, transmission chain.

> Root `CLAUDE.md` carries the short Active/Tier-2 lists for boot orientation. **This file is the full verified classification + the evidence.** When they disagree, re-run the pass and reconcile. ✅ **Root mirror RECONCILED 2026-08-05 (Will-approved in-session)** — root `CLAUDE.md:26` now names the five descriptive classes and points here for the per-agent assignment, deliberately *without* re-listing agents by class (a duplicated high-churn field rots independently — root points, it does not mirror the churny part). Draft + rationale: `PROME/proposals/2026-08-05_root-claudemd-mirror-edit-DRAFT.md`.

---

### ROSTER RESPONSIBILITY MODEL — ruled 2026-08-04 by Will
*(source: RAV roster-responsibility plan v4, accepted 8/4; rulings: `PROME/proposals/2026-08-04_roster-phase0-ruling-table-RULED.md`; preflight: `PROME/inbox/processed/2026-08-05_from-RAV_roster-phase0-preflight-addendum.md` (durable copy: `AGENTS/RAV/runs/2026-08-05_roster-phase0-preflight-addendum.md`))*

**Column ownership — put the fact in the owner file and POINT; do not restate.**

| Fact | Owner file |
|---|---|
| Agent existence · human bucket · cadence posture | `PROME/ROSTER.md` *(this file)* |
| Class / authority type · maturity level · next structural gap | `AGENTS/DAEDALUS/FLEET_MAP.tsv` → generated `FLEET_DIRECTORY.md` |
| Routing / delivery status | `AGENTS/WALTER/REGISTRY.tsv` + routing table |
| Synthesis-read requirement · brief schema/order invariants | `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` |
| Will-facing priority / decision state | `PROME/WILL_QUEUE.md` · `GATES.tsv` · `DOCKET.tsv` · `BRIEF.md` |
| Off-repo routine schedule / state | PROME if PROME-deployed; **domain owner** for state + registered alert lines |
| Recurring-sweep cadence / service rules | `AGENTS/DAEDALUS/sweeps/REGISTRY.tsv` (checked by `sweeps_due.py`) — **not ROSTER prose** |

**Ownership rule:** every recurring responsibility or shared figure needs **one owner of record, one accountable artifact, and one escalation path**; **overlap is allowed** where agents reconcile to the owner-of-record figure/state rather than siloing (root canon: CORAL↔MARCO, AEOLUS↔CORAL — reconcile to one figure, never silo).

⚠️ **Labels below are DESCRIPTIVE ONLY.** They do not change routing, boot priority, DAEDALUS grading, WALTER delivery, or NEXUS read obligations until an explicit later operational ruling. **Neither `PROVISIONAL ACTIVE` nor `EVENT-DRIVEN SPECIALIST` is a demotion or a statement of lesser authority** — the first means the agent exists and should run with proof criteria still pending; the second describes catalyst/print-driven *cadence and scope*, not standing. Both carry real analytical authority in their lanes.

**Cadence and authority are separate fields only where they diverge or could mislead** — the qualifying set is marked with an **Authority** column below. Where one label carries both truthfully (the `DOMAIN ACTIVE` bucket), the omission is **deliberate**, not missing.

⚠️ **MIRROR — Will-gated:** this file's active list is mirrored into root `CLAUDE.md:26`, which is **auto-injected fleet-wide**. Any roster-taxonomy change owes that mirror a matching edit, **drafted by PROME and ruled by Will — never applied silently.** This pair has rotted before (WP-W2 read "still open" 9 days past its own closing commit `37ee2748e`; OZK lagged to 7/25). Nav-class mirrors that also need alignment: `AGENTS/_INDEX.md` (canonical roster table) and root `AGENTS.md` (31-row agent table — count corrected 8/6, was mis-stated "20-row" from authoring) — navigation surfaces, **not** the same class as auto-injected root canon.

---

## ACTIVE (32) — split by responsibility class *(30→31 at the 2026-08-16 FERT registration; 31→32 at the 2026-08-20 FLG build)*
*Phase 1 taxonomy pass, 2026-08-05. Previously one flat bucket headed "persistent domain owners (30)", which mixed domain owners, organizing/service agents, a review lane, event-driven specialists and newborns under a header claiming all thirty were persistent domain owners.* Verified by recent commit cadence; each runs as its own Claude Code session.

> **The count column is a vintage snapshot (as-of the header date), NOT live** — it rots within days (re-run the Method command to refresh). **Classification is the signal, not the raw count.** *(Vintage-stamp added 2026-07-10 — same "hardcoded-Current value silently rots" defect DAEDALUS fixed in CARL's sub-agent CLAUDE.md files the same day.)*

### ORGANIZING / SERVICE (3)
*Produces a consumed system service without being a domain owner.*

| Agent | Domain | Authority (≠ cadence) | 30d commits (as-of 2026-07-10) |
|---|---|---|---:|
| PROME | Coordinator / chief of staff | Operator rail — decision/approval gates, Will-facing synthesis; **not** the owner of every mechanism | 322 |
| WALTER | Signal & news routing | Intake / delivery / BOARD; schema + routing rulings escalate to PROME | 229 |
| NEXUS | Cross-agent synthesis | Dense cross-agent synthesis + brief schema and freshness/order invariants | 18 |

### REVIEW / QC (1)
*Reviews work; read-only or bounded-repair depending on lane. YEYOU and RAV are review agents too but sit in **SPECIAL**, outside ACTIVE.*

| Agent | Domain | Authority (≠ cadence) | 30d commits (as-of 2026-07-10) |
|---|---|---|---:|
| RED | Adversarial red-team | Challenge / counter-case / falsification triggers; **not** domain ownership | 44 |

### DOMAIN ACTIVE (17)
*Standing source-detail and thesis owners. One label carries both cadence and authority here — deliberately.*

| Agent | Domain | 30d commits (as-of 2026-07-10) |
|---|---|---:|
| SAM | Japan — BOJ / JGB / carry | 85 |
| LIQUID | HY / credit spreads / liquidity | 76 |
| VIOLET | VIX / vol term structure / vol-of-vol | 74 |
| BRENT | Oil — Brent / WTI | 61 |
| HENRY | Macro velocity / market trends | 44 |
| CARL | Consumer & credit-transmission macro | 42 |
| LABOR | Labor market (claims / JOLTS / NFP) | 41 |
| BROCK | Private credit / BDC / non-traded credit | 36 |
| HAWK | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† ‡ | 35 |
| TERRY | Trade construction / risk scoring ‡‡ | 33 |
| REGINALD | Regional banks | 32 |
| MARCO | Florida migration / tourism (FL sub; reconcile w/ CORAL) | 32 |
| ORACLE | Prediction-market diagnostics ‡‡‡ | 31 |
| BOND | US bond-market structure / auctions / rates | 30 |
| CORAL | Florida (whole-state, 10 pillars) | 23 |
| SHADE | Insurer-lender / PE-insurance-captive | 21 |
| ZHAO | China macro — UST demand / capital flows / Korea | 13† |

> **‡ HAWK** — kept `DOMAIN ACTIVE`, not organizing: its synthesis is **inside** the geopolitical/oil-risk domain (reconciling OSPREY/FALCON), not a fleet-coordination function (RAV preflight, contested row 2).
> **‡‡ TERRY** — **ruled `DOMAIN ACTIVE` 2026-08-05 (Will), overriding the preflight's `ORGANIZING / SERVICE` placement.** Trade construction is its domain and it holds **canon authority**: root `CLAUDE.md` names TERRY the *canonical owner* of trade-construction rules (`AGENTS/TERRY/RISK_RULES.md`), whose numbered Non-Negotiables are a **stable API** that live fire-cards cite by number. An agent that owns canon in its lane is a domain owner. *(RAV's delivered preflight addendum carries the superseded `ORGANIZING / SERVICE` placement in its original 2026-08-04 text, preserved deliberately as provenance and corrected in its own **"Correction Block — 2026-08-05"** appended to both copies at `61d71d974`. **This row is the governing assignment either way.** ⚠️ When first written this pointed at a correction note that did not yet exist — a forward reference, caught by RAV's independent verification pass and repointed here.)*
> **‡‡‡ ORACLE** — `DOMAIN ACTIVE`, not service: it owns a substantive information domain with external signal content, not merely a workflow service (RAV preflight recommendation, accepted).

### PROVISIONAL ACTIVE (7)
*Exists and should run; proof criteria not fully met. **Not a demotion** — see the model block above.*

| Agent | Domain | Authority (≠ cadence) | 30d commits (as-of 2026-07-10) |
|---|---|---|---:|
| AEOLUS | Climate → economy (macro; insurance/ag/energy-demand channels) | Full domain authority; DAEDALUS `L2` w/ spawn-cadence debt + missing falsification surface | 5 |
| WATT | Power/grid — PJM stress → wholesale price → industrial/data-center cost | Full domain authority; proof criteria pending | new†† |
| VULCAN | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | Full domain authority; proof criteria pending | new†† |
| MIDAS | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | Full domain authority; proof criteria pending | new†† |
| OSPREY | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | Full theater authority; proof criteria pending | new††† |
| FALCON | US/Israel/Iran-Gulf war theater — A/B/C/D ladder, Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | Full theater authority; **DAEDALUS `L3` + live signal flow** — stronger than the other newborns, provisional only because maturity/consumption proof is still settling | new††† |
| HOMER | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | Full domain authority; proof criteria pending | new††† |

> ⚠️ **Cross-reference, do not re-derive:** five of these seven — **AEOLUS · MIDAS · OSPREY · VULCAN · WATT** — are DAEDALUS's own **F5 finding** (2026-08-03: *"5 agents carry a live thesis and NO falsification surface … all 5 my builds, one blueprint cause"*), reached independently. **DAEDALUS has already ruled the disposition: a dated retrofit trigger, NOT an instant demotion** (PAT-075 grandfathering — nobody loses a level on the day a rule lands). The retrofit trigger is DAEDALUS's lane at Phase 2; this label must not be read as duplicating or pre-empting it.

### EVENT-DRIVEN SPECIALIST (4)
*Narrow agents expected to run around print/catalyst/event windows. **Cadence and scope description — NOT lower authority.***

| Agent | Domain | Authority (≠ cadence) | 30d commits (as-of 2026-07-10) |
|---|---|---|---:|
| OZK | Bank OZK specialist (RESG construction / classified-migration watch) | **Real analytical authority** in-lane, DAEDALUS `L4`; cadence is print-driven (revival gate → Q2 print) | revived†††† |
| WAL | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3) | **Real analytical authority** in-lane, owner of its thesis-of-record; cadence is print-driven | new††††† |
| FLG | Flagstar Financial specialist (NYC rent-regulated multifamily → CRE concentration → nonaccrual → reserve adequacy; formerly NYCB) | **Real analytical authority** in-lane, DAEDALUS grade pending first session; cadence is print-driven (Call Report ~QE+45d) | new‡ |
| FERT | Fertilizer supply/price/policy → food-CPI transmission → CF positioning (nitrogen + phosphate; China policy = LIVE vector; **potash → FERT at TRIAGE DEPTH, Will-ruled 2026-08-18** — routing only, log+flag, no deep-dive until the charter edit [DAEDALUS-owed] + benchmark row land together; ⚠️ potash = a FOURTH benchmark family on a desk re-chartered over a basis mislabel. ⛔ Prior cell read "potash EXCLUDED-UNOWNED fleet-wide" — never a Will ruling, an inference off the 8/16 re-charter's positive scoping, propagated as fact) | **Real analytical authority** in-lane; cadence is trigger-driven (TRIGGERS.tsv wake register; weekly-to-monthly decision tempo) | re-chartered†††††† |

> **‡ FLG** built 2026-08-20 — the fleet's FIRST GREENFIELD per-bank build (no sub-tree promotion; FERT re-charter as template), Will-ruled in-session verbatim "Yes build it" on DAEDALUS's proposal off REGINALD's matrix v2.0 (FLG ranked 1st of 14 scored banks after v1 ranked it last — the reversal is the origin story). Build record `AGENTS/DAEDALUS/builds/FLG_BUILD_2026-08-20.md`; zero gates registered at birth (FERT discipline: base-rate first, register second); root CLAUDE.md:26 mirror 31→32 = Will-gated, drafted at registration — ✅ **EXECUTED 2026-08-21 (`326181484`, root-batch word; name-set proven 32/zero-lost; AGENTS.md row landed same commit)**.
> **AEOLUS** built + wired by DAEDALUS 2026-06-28 (spec: `AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md`). *(Stale "no commit history yet" note removed 7/9 — self-commits exist 6/28 + 7/9 catch-up `564d689d`; row reconciled.)* Macro climate owner; CORAL keeps Florida (boundary handshake RESOLVED 7/9: AEOLUS global/macro, CORAL FL-canonical, reconcile-to-one-number).
> **† ZHAO** reactivated 2026-07-05 (Will-approved) after ~2.5mo dormancy — the "13" = the 7/4 reactivation burst (8: STATUS rewrite, KB-076…087, VX/FLOW/PREDICTIONS refresh, `boot.py`, `NEXUS_BRIEF.md`) + the 7/9 catch-up (~5), not yet steady multi-week cadence — recount next pass. Domain is load-bearing: China genuine UST exit ($651.1B, 18yr low) feeds the long-end flow question *(demand-hole refuted at flow level 7/9 — live thread = who-is-the-transient-bid, ZHA-11, TIC 7/16 arbiter)*; Korea (KRW ~1,530) feeds SAM. Ran 7/9 catch-up (China-leg pre-reg, activity current). DAEDALUS maturity-profile + NEXUS BRIEFS_MAP add routed 2026-07-05.

> **†† WATT / VULCAN / MIDAS** — the 3-agent build queue, built + wired by **DAEDALUS 2026-07-10→11** (Will-directed; specs `AGENTS/DAEDALUS/builds/{WATT,VULCAN,MIDAS}_SPEC.md`). All market-agents, active-by-intent; 0 commit history yet → the "new" is honest, reconcile at the next activity pass (PAT-019). **WATT** = grid-stress→power-price→cost (spun out of HENRY's provisional power leg; AEOLUS C3 detects, WATT prices; consumed by HENRY HEN-36 FCF + CARL retail). **VULCAN** = AI-capex/semi/memory as systemic risk (owns the concentration *mechanism* behind VIOLET's Path-B; feeds HENRY + WATT). **MIDAS** = dual-channel metals (gold as debasement/real-rate tell — two-way w/ BOND; copper as China-demand thermometer — two-way w/ ZHAO; safe-haven → LIQUID; PGM supply → HAWK). Maturity: all L1 in `AGENTS/DAEDALUS/FLEET_MAP.tsv`.

> **††† OSPREY / FALCON / HOMER** — built/promoted by **DAEDALUS 2026-07-12** (Will-directed, same-day execution). 0 commit history yet → reconcile at the next activity pass (PAT-019). **OSPREY + FALCON** = the HAWK war-agent split (root cause: HAW-15 structural-overload miss — one agent holding two acute independent wars starves the secondary theater; spec `AGENTS/HAWK/design/2026-07-12_war-agent-split-spec.md`, build `AGENTS/DAEDALUS/builds/OSPREY_FALCON_BUILD.md`). OSPREY inherits the 32-row RU-UA strike ledger + channel model (OSP-01 ←HAW-17); FALCON inherits the Iran scenario ladder + convergence matrix + baghdad_watch (FAL-01 ←HAW-16; founding mandate = Gulf-Iran strike-ledger backfill). **HAWK residual** = cross-war synthesis + dormant book, single ROUTINE outward interface ({OSPREY,FALCON}→HAWK→market agents; acute 🔴 direct to BRENT, HAWK cc'd); HAW-01..17 calibration record stays HAWK's. **HOMER** = housing promoted from `AGENTS/CARL/sub_agents/` (case + review: `AGENTS/DAEDALUS/builds/homer_promotion/`; ★ rulings Will-approved 7/12: Trepp CMBS-MF one-owner = HOMER [CREED keeps non-MF CMBS, S5→HOMER-fed cross-ref; REGINALD consumes HOMER's figure]; CRL-06/23 stay CARL's w/ HOMER as data owner; HOMER owns mortgage-rate surface). Maturity: OSPREY/FALCON L1-seeded, HOMER L2-at-entry in `AGENTS/DAEDALUS/FLEET_MAP.tsv`.

## TIER-2 — spawned as needed (4)
| Agent | Domain | Note |
|---|---|---|
| CREED | National CRE / CMBS | committed 6/27; spawn for CMBS / REIT-tape work |
| DEWEY | Deep on-demand research | self-identified Tier-2 "go deep on one question"; stateless (INDEX.tsv only) |
| HANS | Europe macro (PMI→ISM lead, ECB/Fed divergence, EU UST custody) — US-market lens | ~4 commits/30d; label fixed 7/10 (was "Geopolitics (energy-geo)" — PAT-042, DAEDALUS catch vs `AGENTS/HANS/CLAUDE.md`; military ceded to HAWK) |
| OTTO | Auto-industry fraud & stress | 13/30d; STATUS 6/09 |

## DORMANT — revive only on explicit need (2)
| Agent | Domain | Why dormant |
|---|---|---|
| SENTRY | Cross-domain signal pipeline | CI pipeline live but human-idle since 6/02; STATUS frozen 5/09 (Will → dormant 6/27) |
| BARON | Trump financial-policy network | dormant since 5/08 |

*(ZHAO moved dormant→ACTIVE 2026-07-05 — reactivated 7/4, Will-approved; see ACTIVE table. OZK moved dormant→ACTIVE 2026-07-22 — revived 7/18 on its own revival gate exactly as the old row predicted; see ACTIVE table + †††† note.)*

> **††††† WAL** — **registered ACTIVE 2026-07-25 on cutover day** (Will-approved 7/22 off DAEDALUS's promotion review + 5 rulings; DAEDALUS ran WP-W0 precondition then **WP-W1 landed `ed1ce777`**: `AGENTS/REGINALD/WAL` → `AGENTS/WAL` by `git mv`, history preserved, root-gitignore source-ignore block replicated at the new path in the SAME changelist per ruling 4). Registered on **cutover completion, not thesis completion** — the directory is a standing agent (own `CLAUDE.md`/`STATUS.md`/`THESIS.md` v2.3/workbook/research/sources) and REGINALD's gating lane closed the same day (Stage-2 7/22 · v2.3 re-mark · BROCK bank→PC map). **WP-W2 CLOSED same day (`37ee2748e` — INDEX + WEAKNESSES rewritten to v2.3 per the CHANGELOG handoff table; EV $73.92, PT $52-74 now carried correctly).** *This paragraph claimed WP-W2 "known-open" for 9 days after its own registration commit closed it — spine-audit #7 (8/3) caught it here AND in root `CLAUDE.md`'s mirror, whose fix is Will-gated; the worst-case effect was a reader distrusting WAL's correct v2.3 values as stale.* No commit-activity count yet (first standalone session pending) — first FLEET_MAP row + L-grade are DAEDALUS's at its next pass; recount at the next activity pass (PAT-019). **Root `CLAUDE.md` reconciled same session (Will-approved 2026-07-25):** WAL added to the active list + the "next promotion candidate" pointer retired. Same pass also fixed a pre-existing lag — **OZK** was missing from root's active list despite its 7/22 dormant→ACTIVE flip here (exactly the root-vs-ROSTER disagreement this file's own header says to reconcile).
>
> **†††† OZK** — flipped dormant→active 2026-07-22 (PROME, per DAEDALUS Production-Review ask): revived **7/18** on its registered revival gate (Q2 print 7/21), ran the staleness sweep + pre-print freeze + four-rail Stage-1 grade (~15 commits 7/18-7/21) + Stage-2 spawned 7/22 eve. First FLEET_MAP row added by DAEDALUS 7/22 at **L4** (first-scan). Recount at the next activity pass (PAT-019).

> **†††††† FERT** — **RE-CHARTERED (not revived) 2026-08-16, Will-ruled** (`PROME/proposals/2026-08-16_fert-recharter-RULED.md`; graded record = `PROME/research/2026-08-16_fert-revival-assessment.md` — March STATUS graded 1 HIT / 1 PARTIAL / 1 INDET / 2 MISS, cite only as history). Registered ACTIVE on **cutover completion** (WAL precedent): DAEDALUS build `595ac2306` landed 8/16, 7d inside the 8/23 DOCKET checkpoint — new charter (market-agent blueprint, benchmark+unit+date discipline, PAT-073 exclusions register) + `boot.py` (4 capable cases watched) + re-cut `PREDICTIONS.tsv` + `TRIGGERS.tsv` 10-row wake register; old charter archived intact. **Gates ratify at its first live session AFTER base-rating — nothing registered yet; do-not-re-register `urea NOLA >$800`** (ruling §3). First-live-session window rec: before ~8/25 (RCF award ~8/18 + DTN 8/20 land fresh). WALTER routing re-wired by DAEDALUS packet (row 7); ~~potash dropped from scope = UNOWNED fleet-wide~~ **⛔ SUPERSEDED 2026-08-18 (Will-ruled in-session): potash → FERT at TRIAGE DEPTH** — see the FERT row above for the live scoping; the struck text was an inference off the re-charter's positive wording ("nitrogen AND phosphate" — zero occurrences of "potash"), never a Will ruling (WALTER self-caught 8/18). 0 commits on the new charter yet → reconcile at the next activity pass (PAT-019).

## RETIRED — moved out of the live tree
**In `AGENTS/_archive/`** (archived 2026-06-27): **BUFFER** (shock-absorber / containment), **DOC** (system-health monitor), **EARNINGS** (corporate-earnings monitor), **FOREX** (FX monitor) — scaffolded but never launched (skeleton + empty workbooks, no STATUS, zero session commits); **DARWIN** (archived earlier). **Folders removed entirely** (2026-06 public-prep prune; recoverable from git history): **HERMES** (mail-carrier, deprecated by the messaging overhaul `[[project_messaging_overhaul]]`), **REITS** (REIT tape → absorbed into CREED), **TRADES** (trade scratchpad → superseded by TERRY).

## ARCHIVE SOURCES — do not launch (folder left in place)
CRUISE (Will's personal-interest — ⚠️ label FLAGGED FALSE by DAEDALUS's 8/16 orphaned-threshold sweep: de-facto ACTIVE, 4 Will-directed sessions since 8/14, arm-CCL ladder unregistered; re-classification + registration = PROME-lane follow-up, decision packet at Will since 8/14 — do not re-derive here) · ATHENA (reading / knowledge). *(FERT removed 2026-08-16 → ACTIVE/EVENT-DRIVEN SPECIALIST, see ††††††.)*

## SPECIAL
**YEYOU** — repo-wide reviewer on a manual/branch model (not a domain agent; stays manual per Auto-push Decision C).
**DAEDALUS** — fleet architect (meta-agent: design/structure/maturity/lifecycle). On-demand, spawnable by PROME/Will; persistent meta-memory. Merged + wired 2026-06-27 (Phases 0–3 done, dry-run-proven; Phase 4 = first real maintenance pass). On fleet auto-push.
**RAV** — deep factual/analytical reviewer + bounded repair (Codex CLI, Will-driven, on-demand; author `rav-codex@local`, commits directly on master under per-run direction). **Charter RATIFIED as-drafted by Will 2026-08-02** (`AGENTS/DAEDALUS/builds/RAV_CHARTER.md`): §3 repair/flag split (repair = mechanical + reversible + witnessed-inside-the-artifact, ALL three; anything else flags to the run report, never resolved in the diff) · fences (a) not-precedent for any regular agent's cross-dir commits, (b) one-line inbox note per touched agent, (c) no-silent-deletions (WALTER words (c) into its registry row, cited from the charter). **Classification: Meta per PAT-027 (authority to mutate structure), keeping WALTER's Tier-2 cadence label** — different questions, both true. Interim sole-QC pending YEYOU revival (run-reports must be self-sufficient; on revival the two COMPOSE — YEYOU flags-never-fixes, and YEYOU observing RAV cross the §3 line is a finding, not insubordination). Scaffold `AGENTS/RAV/` + FLEET_MAP row = DAEDALUS's next acts, IN THAT ORDER after this row (PAT-047 co-registration). Run history: 7/29 repair push (4 commits inside the usage outage; the 2 §3-class misses are what the charter encodes) · 8/1 read-only QC pass → `PROME/codex/RAV_QC_LEDGER.md` (RAV/PROME handoff surface; PROME writes dispositions back).

## TOOL-CLASS INSTRUMENTS — not agents; do NOT audit as agents
*(Named spawn skeletons whose definitions live in `.claude/agents/` — the HARNESS registry, deliberately outside `AGENTS/`. They have no `AGENTS/<NAME>/` dir, no STATUS, no roster seat, no standing sessions; each instance is ephemeral and its contract file is its memory. **A roster-activity audit that finds their names in commit history should match them HERE and stop** — a "missing `AGENTS/<NAME>/` dir" for a name on this list is correct, not a gap.)*
- **ANVIL** — FORGE reconcile clerk (`.claude/agents/anvil.md`, Will-directed 2026-07-30). PROME's standing instrument for broker-export reconciles of `FORGE/STATUS.md` + FORGE mechanical follow-ups; spawned per export, commits only on per-run PROME authorization (FORGE owner = PROME, root `CLAUDE.md` line 30). **First proof run: the 2026-07-30 FORGE full reconcile to the ~09:40 ET Fidelity IRA export** (first since 7/20 — VIXCS box closed at −$111.60, single-account banner added, 10-item discrepancy section; `git log --grep="ANVIL reconcile"` finds it). *Was cited here as hash `69515d7a`, which **resolves to no object** — the commit was rewritten by the 2026-07-31 11:46 rebase and now reads `25c2204f6`. Found by `claim_check` on the 8/5 Phase 1 pass and fixed by **describing the run instead of re-pinning a hash**: per `PROME/CLOSEOUT.md` ("behavior-language over hash-pinning") a second hash would rot the same way, and the searchable subject cannot.* Promotion to a real agent = DAEDALUS maturity lane, Will-gated, only if cadence proves out.
*(**RAV** moved to SPECIAL 2026-08-02 on charter ratification — a commit-history audit matching `rav-codex@local` lands on the SPECIAL row above now. The 7/30 interim-QC ruling and YEYOU-seat-not-vacant note are carried there.)*

## OFF-FLEET — Will-personal sessions (1) · NOT part of the research operation
*(Launchable Claude Code sessions that serve **Will directly**, not the fleet. They own no domain, route no signals, hold no thesis, and produce no market judgment. **Distinct from TOOL-CLASS above** — those are ephemeral `.claude/agents/` spawn skeletons; these are persistent interactive sessions with their own home dir + `CLAUDE.md`. **Distinct from SPECIAL** — those serve the FLEET. ⚠️ **Do not audit these as fleet agents; do not migrate them into ACTIVE; do not give them fleet obligations.**)*

- **VIRGIL** — Will's personal coding / learning coach. **Home: `WILL/private/fellowship/` (GITIGNORED)** · launch `cd ~/Research-workspace/WILL/private/fellowship && claude`. Born **2026-08-19** (PROME-built, Will-directed) to prepare an **external technical assessment** *(dated + private; the specifics live in its own charter and are deliberately NOT restated in a shared file — routing fact here, content there)*. **KEPT STANDING after that event as an ongoing Python/CS teaching lane — Will-ruled 2026-08-19 in-session.** Modes: DRILL · PROCTOR · DEBRIEF · BUILD · STUDY · INTERVIEW. Named for Dante's guide, who takes the pilgrim to the threshold of Paradise and cannot cross it — the name encodes its hard rule: **it is closed during any real assessment or live interview** (Anthropic's AI-use policy; candidates have been removed for breaching it).
  ⚠️ **Why every fleet audit will read VIRGIL as broken — and why each reading is CORRECT, not a gap to close:**
  ① **No `AGENTS/VIRGIL/` dir.** By design. A folder-existence pass should match this row and stop (the TOOL-CLASS precedent above).
  ② **Zero commits, ever.** Its home is gitignored and its charter forbids `git add/commit/push`. **This file's Method — 30/60-day commit activity — is structurally blind to it**, so "no activity" is NOT a dormancy signal here and must never trigger a dormant/retired flip. Its redundancy is `backup.sh` → OneDrive, not git.
  ③ **Invisible to repo-root greps.** The harness `grep` honors `.gitignore`, so sweeps from the root skip its files silently — name the path explicitly. `[[finding_grep_respects_gitignore_so_ignored_zones_are_invisible]]`
  ④ **No STATUS.md · no inbox/outbox · no FLEET_MAP row · no WALTER REGISTRY row · no NEXUS read obligation · no transmission-chain position · no GATES/DOCKET rows.** All absent on purpose.
  ⑤ **DESKTOP-ONLY** — gitignored ⇒ does not travel on push (see the `WILL/private/` row in `PROME/MACHINE_LOCAL.md`).
  **PROME's only standing interest:** VIRGIL may doorbell PROME over cross-session messaging at milestones. ⛔ **Never route fleet signals to it, and never carry Will's personal material into fleet files.**

## Spinouts & promotions (provenance)
*(Relocated from root `CLAUDE.md` 2026-07-01 — root keeps only the live "reconcile-to-one-figure, don't-silo" rule + Florida priority; the archival history lives here.)*
REGINALD sub-scopes promoted to peer agents (each ran as a REGINALD sub before getting its own `AGENTS/<NAME>/`):
- **OZK** ← REGINALD, **2026-04-24** (`REGINALD/OZK/` → `AGENTS/OZK/`). Bank-OZK specialist. **WAL = next promotion candidate** when ready.
- **CORAL** ← REGINALD, **2026-06-19** (`REGINALD/sub-agents/CORAL/` → `AGENTS/CORAL/`). Whole-Florida, 10 pillars (`AGENTS/CORAL/COVERAGE.md`). MARCO overlap (FL migration/tourism) intentional — reconcile to one figure.
- **AEOLUS** — *not* a REGINALD spinout; net-new, built + wired by **DAEDALUS 2026-06-28** (spec: `AGENTS/DAEDALUS/builds/AEOLUS_SPEC.md`). Macro climate owner (insurance / ag-food / energy-demand channels); CORAL keeps FL climate/coastal, reconcile FL numbers upward.
- **WATT / VULCAN / MIDAS** — net-new, built + wired by **DAEDALUS 2026-07-10→11** (the 3-agent build queue: power → AI-semis → metals; specs in `AGENTS/DAEDALUS/builds/`). WATT spun out of HENRY's provisional power leg (`power_watch.py` moved FORGE→`AGENTS/WATT/`); VULCAN + MIDAS net-new. None are REGINALD spinouts.
- **OSPREY / FALCON** ← HAWK, **2026-07-12** — the war-agent split (HAWK's two acute war loads → theater siblings; HAWK reclassified to cross-war synthesis + dormant book). Raptor-family naming = spun-out-sibling signal. Built by DAEDALUS at Will's direction, HAWK-authored domain spec.
- **HOMER** ← CARL, **2026-07-12** (`AGENTS/CARL/sub_agents/HOMER/` → `AGENTS/HOMER/`, git-mv history preserved). Housing as top-level domain. Jumped the WAL queue by Will's call 7/12 (WAL was next-in-line and stayed there until 7/25).
- **WAL** ← REGINALD, **2026-07-25** (`AGENTS/REGINALD/WAL/` → `AGENTS/WAL/`, git-mv history preserved — OZK/HOMER precedent). Western Alliance specialist; **the long-standing "next promotion candidate" line is now CLOSED.** Cutover WP-W1 `ed1ce777` executed the same day REGINALD's pre-cutover lane completed (Stage-2 · v2.3 re-mark · BROCK map) and DAEDALUS ran WP-W0. Ruling-4 detail worth preserving as pattern: the root-gitignore source-ignore block was replicated at the new path **in the same changelist as the move**, so the 9 ignored binary sources kept their semantics across the rename and no `.md` synthesis was swept — the promotion-hygiene step OZK/CORAL/HOMER each had to discover. **WP-W2 (INDEX/WEAKNESSES fold to v2.3) EXECUTED same day (`37ee2748e`)** — see ††††† in the ACTIVE table.
- *(Next promotion candidate: **UNASSIGNED** as of 2026-07-25 — the queue that ran OZK → CORAL → HOMER → WAL has no named successor. Nominations are DAEDALUS's lane via maturity review, Will-gated.)*

---

## Coverage notes — explicit-unowned gaps (on record, not silently orphaned)
- **Korea macro (broad)** — UNOWNED as of 2026-07-22 (KOSPI coverage-gap disposition, DAEDALUS 7/22 Production Review, closes the 7/11 thread). The owned slivers: SK-Hynix/HBM/KOSPI-as-semis-proxy → **VULCAN S2** scope line; Korean leveraged-ETF amplifier → **VIOLET** watch line; KRW + BoK-as-BOJ-tell → **ZHAO/SAM** (existing). Everything else Korea (fiscal, politics, housing, broad KOSPI) has NO owner — a Korea-macro event routes to PROME for ad hoc disposition until Will assigns one. *(DEWEY 7/20: the KOSPI-8,200 re-contagion anchor is NOT affirmable — 2x chip-ETF complex de-risking under FSS restriction, launches halted 7/16.)*

## Transmission chain (reference)
LABOR → CARL → REGINALD → market repricing. HENRY (velocity), LIQUID (amplification), SAM (Japan, parallel trigger). {OSPREY (Russia/Ukraine), FALCON (Iran/Gulf)} → HAWK (geopol synthesis) → BRENT (oil/energy); acute theater signals OSPREY/FALCON → BRENT direct, HAWK cc'd. HOMER → {CARL (consumer transmission), REGINALD (Path C bank collateral)} + HENRY (wealth effect). VIOLET (vol regime), BOND (rates/auctions), BROCK → SHADE (private credit → insurer-lender double-jeopardy), CORAL / MARCO (Florida). AEOLUS → {BRENT (energy demand), CORAL (FL insurance/property), MARCO (food-CPI/migration)} (climate → economy). AEOLUS C3 → WATT → {HENRY (FCF), CARL (retail)}; BRENT → WATT (gas→power). VULCAN → {VIOLET (concentration-unwind mechanism), HENRY (HEN-36 FCF), WATT (compute→power demand)}; {ZHAO, HAWK} → VULCAN (China/Taiwan supply). {BOND (gold↔real-rates), ZHAO (copper↔China)} ↔ MIDAS → {LIQUID (safe-haven), HENRY (growth tell)}; HAWK → MIDAS (PGM supply).
