# PROME/ROSTER.md — Verified Agent Roster
**Owner:** Prome · **Last verified:** 2026-06-27 (commit-activity + STATUS-recency pass) · folder-existence reconciled 2026-06-30 · **ZHAO reactivated dormant→active 2026-07-05** (8 commits 7/4, Will-approved) · **counts refreshed 2026-07-10** (PROME commit-activity re-run — classification UNCHANGED; no active/tier-2/dormant flips) · **OZK flipped dormant→active 2026-07-22** (revived 7/18 exactly on its revival gate — Q2 print 7/21; ~15 commits incl. the four-rail Stage-1 grade; DAEDALUS added its first FLEET_MAP row L4 same day) · **WAL REGISTERED ACTIVE 2026-07-25 on cutover day** (Will-approved 7/22; DAEDALUS WP-W0 → WP-W1 `ed1ce777` git-mv `AGENTS/REGINALD/WAL` → `AGENTS/WAL`; ACTIVE count 29→30; ~~WP-W2 open~~ **WP-W2 EXECUTED same day `37ee2748e` — stale-open claim caught by spine-audit #7, 8/3** — see ††††† )

**Method:** classification by **30/60-day git-commit activity** (the "is it actually running" signal) + STATUS mtime + self-declared domain — *not* a prose guess. Re-verify by re-running the activity map (`git log --since=<60d> --pretty=%s | grep -cE '^NAME'` per agent) and diffing against this table.

> Root `CLAUDE.md` carries the short Active/Tier-2 lists for boot orientation. **This file is the full verified classification + the evidence.** When they disagree, re-run the pass and reconcile.

---

## ACTIVE — persistent domain owners (30)
Verified by recent commit cadence; each runs as its own Claude Code session.

> **The count column is a vintage snapshot (as-of the header date), NOT live** — it rots within days (re-run the Method command to refresh). **Classification is the signal, not the raw count.** *(Vintage-stamp added 2026-07-10 — same "hardcoded-Current value silently rots" defect DAEDALUS fixed in CARL's sub-agent CLAUDE.md files the same day.)*

| Agent | Domain | 30d commits (as-of 2026-07-10) |
|---|---|---:|
| PROME | Coordinator / chief of staff | 322 |
| WALTER | Signal & news routing | 229 |
| SAM | Japan — BOJ / JGB / carry | 85 |
| LIQUID | HY / credit spreads / liquidity | 76 |
| VIOLET | VIX / vol term structure / vol-of-vol | 74 |
| BRENT | Oil — Brent / WTI | 61 |
| RED | Adversarial red-team | 44 |
| HENRY | Macro velocity / market trends | 44 |
| CARL | Consumer & credit-transmission macro | 42 |
| LABOR | Labor market (claims / JOLTS / NFP) | 41 |
| BROCK | Private credit / BDC / non-traded credit | 36 |
| HAWK | Geopolitical synthesis (cross-war reconciliation, oil-decoupling thesis, war-risk/shipping) + dormant book (Taiwan/Venezuela/trade/chokepoints/defense/sanctions) — theaters split out 7/12††† | 35 |
| TERRY | Trade construction / risk scoring | 33 |
| REGINALD | Regional banks | 32 |
| MARCO | Florida migration / tourism (FL sub; reconcile w/ CORAL) | 32 |
| ORACLE | Prediction-market diagnostics | 31 |
| BOND | US bond-market structure / auctions / rates | 30 |
| CORAL | Florida (whole-state, 10 pillars) | 23 |
| SHADE | Insurer-lender / PE-insurance-captive | 21 |
| NEXUS | Cross-agent synthesis | 18 |
| ZHAO | China macro — UST demand / capital flows / Korea | 13† |
| AEOLUS | Climate → economy (macro; insurance/ag/energy-demand channels) | 5 |
| WATT | Power/grid — PJM stress → wholesale price → industrial/data-center cost | new†† |
| VULCAN | AI-capex / semiconductor / memory cycle → systemic risk (concentration, memory, power-demand, Taiwan chokepoint) | new†† |
| MIDAS | Metals — monetary (gold/silver: debasement, real-rates) + industrial (copper/PGM: growth, China, supply) | new†† |
| OSPREY | Russia/Ukraine war theater — energy-strike campaign, crude-vs-products channel, shadow-fleet kinetic strikes, Baltic/Black-Sea ports | new††† |
| FALCON | US/Israel/Iran-Gulf war theater — A/B/C/D ladder, Hormuz, Gulf targeting, Bab-al-Mandab/Houthi, Baghdad watch | new††† |
| HOMER | Housing — asset market + housing credit structure (pipeline, GSE+CMBS multifamily, builders, HPI, mortgage-rate surface) | new††† |
| OZK | Bank OZK specialist (RESG construction / classified-migration watch) | revived†††† |
| WAL | Western Alliance Bancorp specialist (Office/B1-migration/MI3 idiosyncratic bear; thesis-of-record v2.3) | new††††† |

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

## RETIRED — moved out of the live tree
**In `AGENTS/_archive/`** (archived 2026-06-27): **BUFFER** (shock-absorber / containment), **DOC** (system-health monitor), **EARNINGS** (corporate-earnings monitor), **FOREX** (FX monitor) — scaffolded but never launched (skeleton + empty workbooks, no STATUS, zero session commits); **DARWIN** (archived earlier). **Folders removed entirely** (2026-06 public-prep prune; recoverable from git history): **HERMES** (mail-carrier, deprecated by the messaging overhaul `[[project_messaging_overhaul]]`), **REITS** (REIT tape → absorbed into CREED), **TRADES** (trade scratchpad → superseded by TERRY).

## ARCHIVE SOURCES — do not launch (folder left in place)
FERT · CRUISE (Will's personal-interest) · ATHENA (reading / knowledge).

## SPECIAL
**YEYOU** — repo-wide reviewer on a manual/branch model (not a domain agent; stays manual per Auto-push Decision C).
**DAEDALUS** — fleet architect (meta-agent: design/structure/maturity/lifecycle). On-demand, spawnable by PROME/Will; persistent meta-memory. Merged + wired 2026-06-27 (Phases 0–3 done, dry-run-proven; Phase 4 = first real maintenance pass). On fleet auto-push.
**RAV** — deep factual/analytical reviewer + bounded repair (Codex CLI, Will-driven, on-demand; author `rav-codex@local`, commits directly on master under per-run direction). **Charter RATIFIED as-drafted by Will 2026-08-02** (`AGENTS/DAEDALUS/builds/RAV_CHARTER.md`): §3 repair/flag split (repair = mechanical + reversible + witnessed-inside-the-artifact, ALL three; anything else flags to the run report, never resolved in the diff) · fences (a) not-precedent for any regular agent's cross-dir commits, (b) one-line inbox note per touched agent, (c) no-silent-deletions (WALTER words (c) into its registry row, cited from the charter). **Classification: Meta per PAT-027 (authority to mutate structure), keeping WALTER's Tier-2 cadence label** — different questions, both true. Interim sole-QC pending YEYOU revival (run-reports must be self-sufficient; on revival the two COMPOSE — YEYOU flags-never-fixes, and YEYOU observing RAV cross the §3 line is a finding, not insubordination). Scaffold `AGENTS/RAV/` + FLEET_MAP row = DAEDALUS's next acts, IN THAT ORDER after this row (PAT-047 co-registration). Run history: 7/29 repair push (4 commits inside the usage outage; the 2 §3-class misses are what the charter encodes) · 8/1 read-only QC pass → `PROME/codex/RAV_QC_LEDGER.md` (RAV/PROME handoff surface; PROME writes dispositions back).

## TOOL-CLASS INSTRUMENTS — not agents; do NOT audit as agents
*(Named spawn skeletons whose definitions live in `.claude/agents/` — the HARNESS registry, deliberately outside `AGENTS/`. They have no `AGENTS/<NAME>/` dir, no STATUS, no roster seat, no standing sessions; each instance is ephemeral and its contract file is its memory. **A roster-activity audit that finds their names in commit history should match them HERE and stop** — a "missing `AGENTS/<NAME>/` dir" for a name on this list is correct, not a gap.)*
- **ANVIL** — FORGE reconcile clerk (`.claude/agents/anvil.md`, Will-directed 2026-07-30). PROME's standing instrument for broker-export reconciles of `FORGE/STATUS.md` + FORGE mechanical follow-ups; spawned per export, commits only on per-run PROME authorization (FORGE owner = PROME, root `CLAUDE.md` line 30). First proof run `69515d7a`. Promotion to a real agent = DAEDALUS maturity lane, Will-gated, only if cadence proves out.
*(**RAV** moved to SPECIAL 2026-08-02 on charter ratification — a commit-history audit matching `rav-codex@local` lands on the SPECIAL row above now. The 7/30 interim-QC ruling and YEYOU-seat-not-vacant note are carried there.)*

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
