# Profile: AEOLUS (climate → economy)

**Built:** 2026-07-22 (single-reader, off the full QC read — light agent, sanctioned path; source: `upgrades/AEOLUS_QC_2026-07-22.md`)
**Class:** Market · **L2** (both L3 gate legs clock/consumption-shaped, not structure) · **Vintage of underlying read:** all surfaces at 2026-07-09 session state + 7/22 QC edits
**Built by DAEDALUS 2026-06-28** (market-agent blueprint, first post-blueprint build) — spec `builds/AEOLUS_SPEC.md`.

## §1 File anatomy (complete — the agent is small enough to enumerate)

| Surface | Role | State at profile time |
|---|---|---|
| `CLAUDE.md` | Identity, 5-channel scope, boot/closeout ritual, thresholds, routing | Current; C3→WATT verified at all 3 rows (:71/:111/:142); WALTER §8.1 consume block installed 7/22 (DAEDALUS) |
| `STATUS.md` | Primary memory — regime read, matrix, live reads, triad, BOTTOM LINE | 122 ln < 250. Vintage 7/9 EXCEPT Citizens row (QC-applied 7/22, canonical 278,246) |
| `THESIS.md` | Per-channel stage tables (the richness layer) | C1/C3 at 7/9; C2/C4/C5 self-bannered "unrefreshed, not re-confirmed" (6/28) — honest two-clock form |
| `TRADE.md` | 3 event-gated ideas (C1 convex tail · C5 freight · C3 watch) | LIVE 7/9; header rule-citation reworded 7/22 (was false-FROZEN-ing the enforcer, PAT-059) |
| `SCRATCH.md` | Pick-up-here + session log | Real discipline; 7/9 log matches STATUS/VX/FLOW exactly |
| `NEXUS_BRIEF.md` | 5-pt handle + routed-this-session, every closeout | 7/9; note its "Routed → MARCO (listed, not executed)" lines — routing intent ≠ delivery (see §4) |
| `LESSONS.md` | L-01..08 | Genuine build-design + domain lessons (L-05 NOAA NCEI discontinued; L-08 weekly-vs-ONI noise) |
| `OPEN_THREADS_2026-07-09.md` | Dated self-sweep artifact (questions/gaps/threads) | High quality; now in FILES table (7/22); fold-or-archive owed at next session |
| `workbook/` | KB (20 rows) · VX (8) · FLOW · PREDICTIONS (AEO-01..04) · SCHEMA | KB uses Stale_By + DerivedFrom + epistemic tiers properly; all 4 predictions OPEN, none past trigger (Nov'26+) |
| `inbox/` | 10 unprocessed items 7/10–7/21 (7 top-level + 3 WALTER SIGs) at QC time | The rot locus — see §5 |

## §2 Where the richness lives

- **The regime read** (STATUS top): ENSO as the single master variable with explicit sign map (suppresses C1/C4, lifts C3/C5) — the independence accounting is genuinely good (shared-root caveat on the composite, "1 root in N costumes" scored once).
- **Pre-registered escalation lines** (STATUS Hurricane-Season block): 4 dated trigger→route→priority rows — fire mechanically, no judgment needed at fire time.
- **KB epistemic discipline**: CFSv2 +4.01°C tail logged C3/ASSUMPTION/not-adopted — the agent resists dramatic single-model tails by construction.
- **Channels-first anti-drift** (PAT-018 operationalized): an empty channel is a *failure signal*. This is the DARWIN antidote and it held — no scope drift observed across 3 sessions.

## §3 Invalidation surfaces (Falsification-sweep inventory)

| Surface | Form | Location |
|---|---|---|
| Exit triad | per-channel standing rule + state@level + FIRED?, literal fired-count (0/5) | STATUS §EXIT/INVALIDATION |
| Channel-kill vs thesis-kill | benign season kills C1's read not the thesis; migration path stated (→C3/C5) | same + THESIS per-channel |
| Bidirectional flips | per-channel, testable at next data release | THESIS stage tables |
| Predictions | AEO-01..04 all carry if-falsified + tier + resolution criteria | workbook/PREDICTIONS.tsv |
| Escalation lines | 4 pre-registered, incl. the C1 reversal (ACE >90% re-arm) | STATUS Hurricane block |

## §4 Do-not-touch / quirks

- **The composite is deliberately NOT independent** — 12/25 carries an explicit correlated-through-one-root caution. Do not "fix" the composite arithmetic to weight for independence; the caveat IS the design (L-02).
- **Weekly-vs-ONI discipline (L-08):** the agent intentionally under-reacts to weekly Niño-3.4 prints. A reader seeing "+1.7°C flagged but not acted on" is looking at discipline, not lag.
- **TRADE.md is event-gated by design** — conviction 1–2 setups awaiting catalysts, not stale recommendations. Don't grade "no position taken" as rot.
- **NEXUS_BRIEF "routed (listed, not executed)" is a known seam**: AEOLUS logs routing *intent* in the brief; actual delivery historically depended on the deprecated outbox-sweeper. Verify delivery at the TARGET when auditing (the 6/28 C5→MARCO packet sat undelivered 24d — root-cause of the long "consumption unverified" gap).
- **C4 data feed is rewired** (NOAA NCEI discontinued Jul 2025 → reinsurer tallies, L-05/KB-AEO-015). Don't re-add NOAA NCEI.
- **FL numbers defer to CORAL** (pre-registered rule, STATUS handshake block). Citizens canonical = CORAL's primary pull, currently 278,246 total PIF Jun-30.

## §5 Standing risk profile (what breaks first)

**Spawn cadence is the single failure mode.** The agent's protocol demonstrably works when spawned (7/9 drained 5 SIGs, honest two-clock banners, boot↔closeout symmetry) — but nothing spawns it. Fixed-clock weather data + no self-session = stale-by breaches (freight 7/15, ENSO 7/23) and corrections rotting in inbox (3 live-figure corrections sat 1–12 days at QC time). PAT-051-adjacent: detection channels get event-spawned; a standing regime-monitor has no spawn driver. PROME spawn flag routed 7/22.

**Owner-owed at next session (QC docket, 7/22):** integrate CORAL 7/21 remainder (ROL 8.46% datum + Bertha) · KB-AEO-018 re-grade B2→A w/ metered-vs-DR split (PROME 7/16) · C3 re-score vs WATT 7/16 EEA-1 chain · ENSO + freight re-pulls (stale-by) · drain 3 WALTER SIGs via new consume block · PROME lane-query ratify · WATT LMP cross-check (optional) · fold-or-archive OPEN_THREADS.

**Re-profile when:** first post-7/22 owner session lands (expect matrix re-score + KB growth), or if WATT seam changes shape again.
