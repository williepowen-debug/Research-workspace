# HAWK Split-Spec — two war-agents + a synthesis HAWK

**Status:** DRAFT for DAEDALUS (build) + PROME (roster/coordination). **Author:** HAWK. **Date:** 2026-07-12. **Approver:** Will (concept approved 2026-07-12; Q1 = "HAWK stays synthesis + dormant-theaters"; Q2 = "draft for DAEDALUS/PROME").
**One-line:** Split HAWK's two dense, independent war-tracking loads (Russia/Ukraine · US/Israel/Iran) into two sibling domain agents; HAWK becomes the cross-war **synthesis** layer + the **dormant geopolitical portfolio**. Fold the Tier-1 documentation fixes into each new agent from day one.

---

## 1. Why (root-cause, not cosmetic)

The 2026-07-12 HAW-15 miss (Ukraine crude-export terminals struck in-window; my ledger was 22 days stale + gappy; I twice concluded "unstruck") was a **structural overload symptom**, not a search failure. One agent holding two acute, independent wars predictably starves the secondary theater — my own `LESSONS.md` documents this twice (Venezuela 5.5mo stale; Russia ledger 22d stale while I was deep in the Gulf). Patching one overloaded agent's ledger doesn't fix the attention asymmetry; splitting the load does. Precedent: OZK/CORAL/AEOLUS spun out of broader agents (see `PROME/ROSTER.md`).

## 2. Target structure

| Agent | Owns | Framework |
|---|---|---|
| **Agent A — Russia/Ukraine war** *(proposed name below)* | Energy-strike campaign (Russia strike ledger), crude-vs-products channel, Ukraine-side shadow-fleet **kinetic** strikes, Druzhba/EU angle, front-line, Baltic/Black-Sea oil ports | Crude-vs-products channel model + flip-triggers (already exists in `SUMMARY.md`) |
| **Agent B — US/Israel/Iran war** *(proposed name below)* | A/B/C/D scenario ladder, Hormuz, Gulf-state targeting, Iran leadership, Hormuz tanker attacks, Bab-al-Mandab/Houthi, Baghdad watch | The Iran convergence matrix + A/B/C/D ladder (already exists in `STATUS.md`) |
| **HAWK — synthesis + dormant** | **Cross-war reconciliation** (one coherent geopolitical read to the market agents, no double-counting), the **shared oil-decoupling thesis** (spans both wars), the **global war-risk-insurance / shipping-disruption** synthesis (pulls from both theaters' shipping incidents), and the **dormant book**: Taiwan, Venezuela, trade war, general chokepoints (Suez/Malacca), defense spending, sanctions-regime | Thin/derived synthesis (see §6) |

## 3. Domain ownership map — the seams (where builds go wrong)

| Topic | Owner | Seam note |
|---|---|---|
| Russia refineries / crude terminals / Druzhba / Baltic-Black-Sea ports | **A** | — |
| Ukraine-side shadow-fleet **strikes** (kinetic destruction of tankers) | **A** | HAWK owns the *global war-risk/shipping* synthesis (pulls A + B) |
| Hormuz / Gulf-state targeting / Iran leadership / Kharg / Gulf-base retaliation | **B** | — |
| Hormuz tanker attacks + Iran oil-evasion shipping | **B** | HAWK owns the global war-risk/shipping synthesis |
| Oil PRICE levels | **BRENT** (unchanged, Mar-6 handoff) | A & B feed BRENT their theater's military inputs; **HAWK reconciles into ONE geopolitical oil-risk read** (routine); acute/time-sensitive signals go direct to BRENT with HAWK cc'd |
| Global shadow-fleet **enforcement / war-risk insurance / shipping disruption** | **HAWK** | Cross-cutting; derived from A + B incidents |
| Taiwan Strait / Venezuela / trade war / Suez / Malacca / defense spending | **HAWK** | Dormant book |
| Cross-agent transmission to HENRY/LIQUID/SAM/CARL/REGINALD | **HAWK** (single interface) | A & B feed HAWK; HAWK owns the outward geopolitical read so market agents get one voice |

## 4. Content migration (file-by-file)

| Current HAWK asset | Disposition |
|---|---|
| `STATUS.md` | Split: Iran sections → B's STATUS; Russia off-core → A's STATUS; HAWK's STATUS becomes a **synthesis dashboard** (cross-war read + dormant book). |
| `SCRATCH.md` / `NEXUS_BRIEF.md` | Each agent gets its own; HAWK's NEXUS_BRIEF becomes the **cross-war synthesis brief**. |
| `workbook/KB.tsv` (225 rows) | **Freeze in place as HAWK's historical record** (do NOT do lossy row-by-row surgery). A & B start **fresh KBs** seeded from current live STATUS, referencing frozen HAWK KB IDs for provenance. |
| `workbook/VX.tsv` | IRAN-01/02, USIRAN-KINETIC-01, GULFSTATE-01, DIPLOMACY-01, ISR-01, BABMANDAB-01 → **B**. UKR-01, SHADOW-01/02 → **A**. VEN-01, TWN-01, TRADE-01/02, SULPHUR-01, FININFRA-01, IRAQ-01, CEASEFIRE-01(retired) → **HAWK**. |
| `workbook/FLOW.tsv` | Split by theater; cross-war transmission pathways → HAWK. |
| `domain/energy-strikes/STRIKES.tsv` (36 rows, theater-tagged) | **Clean split**: `RU-UA` rows → A, `GULF-IRAN` rows → B. Each + Tier-1 fixes (§7). HAWK keeps only a **thin derived cross-war summary table** (not a maintained ledger). |
| `domain/energy-strikes/SUMMARY.md` | Split into A's + B's analysis files (§7 raw-vs-interpretation split). |
| `thesis/PREDICTIONS.tsv` + `PREDICTIONS_ARCHIVE.md` | **Freeze HAW-01..17 as the historical calibration record** (preserves the scoreboard preamble + failure-pattern synthesis — do NOT lose it). Re-home the 2 OPEN rows: **HAW-16 (Iran kill-switch) → B**, **HAW-17 (Russia tanker→crude) → A**, each re-registered under the new prefix with a `←HAW-16/17` pointer. New predictions use new prefixes (§8). |
| `scripts/baghdad_watch.py` (+ state) | → **B** (Iran/Iraq discriminator). |
| `LESSONS.md` | Iran lessons → B; Russia/ledger lessons → A; cross-cutting (mechanism-not-target, ledger-staleness) → all three (copy). |
| `thesis/` (THESIS.md etc.) | Split by theater; cross-war decoupling thesis → HAWK. |

## 5. What HAWK looks like after (the residual)

HAWK = **geopolitical synthesis + dormant book**. Concretely: a synthesis STATUS/NEXUS_BRIEF that (a) reconciles A's + B's reads into one geopolitical picture for the market agents, (b) maintains the shared oil-decoupling thesis, (c) owns global war-risk/shipping/shadow-fleet-enforcement synthesis, (d) keeps the dormant vectors (Taiwan/Venezuela/trade/Suez/Malacca/defense) on a periodic re-sweep cadence. HAWK holds NO trade book (unchanged).

## 6. The synthesis layer — design to avoid becoming the NEW rot point

**Risk:** three stale surfaces instead of one, if HAWK-synthesis lags A & B. **Mitigation — keep it thin + derived:**
- HAWK reads A's + B's `NEXUS_BRIEF.md` at its boot (like NEXUS reads agent briefs) and **reconciles**, it does NOT re-narrate their events.
- HAWK's synthesis STATUS is mostly **pointers + reconciliation deltas** ("A says crude channel re-armed; B says Hormuz decoupling holds; combined oil-risk read = X; double-count check = Y"), not a duplicate event log.
- The two wars are **loosely coupled** (separate roots) → synthesis load is real but bounded. The main recurring synthesis job is the **shared oil/decoupling read** (both wars feed Brent) and the **global war-risk/shipping** aggregate.
- HAWK can spawn A + B together in **teams-mode** for a live cross-war synthesis session when an event spans both.

## 7. Tier-1 documentation fixes — BAKE INTO A & B from day one (don't rebuild)

These are the fixes that would have prevented the HAW-15 miss; build them into each new agent's ledger design:
1. **Swept-through high-water-mark per theater** in the strike-ledger header (e.g. `swept-complete through YYYY-MM-DD`) — turns "no recent rows" into an explicit *"not swept past X"* (kills the completeness trap that caused the miss).
2. **Boot staleness alarm on the strike ledger** — add `domain/energy-strikes/*.tsv` to `scripts/ledger_staleness.py` glob (or a 3-line boot check: newest-row-date vs today when the theater is active). Currently STRIKES.tsv is invisible to the alarm (only `workbook/*.tsv` is scanned) AND is never boot-read.
3. **Closeout strike-sweep cadence** — when the theater is active, a date-careful sweep from the high-water-mark to today, then advance the mark. Replaces memory-driven logging.
4. **Raw-log vs interpretation split** — strike ledger = rows only; "Patterns/aggregates" move to a dated, regenerated analysis file (the current `SUMMARY.md` mixes them and drifted — Pattern ① claimed a clean sequential channel-switch the rows disprove).
5. **Scope label** — each ledger states "material subset — absence of a row ≠ absence of a strike; see swept-through mark."

## 8. Prediction ID namespace + calibration continuity

- **Freeze HAW-01..17** as HAWK's historical calibration record (the scoreboard preamble + failure-pattern synthesis is load-bearing calibration memory — must NOT be lost or fragmented).
- Each new agent gets its **own prefix** (e.g. `FAL-xx`, `OSP-xx` — final per naming). New predictions use the new prefix.
- The 2 live OPEN predictions re-home with a pointer: **HAW-16 → B**, **HAW-17 → A**.
- Each new agent's PREDICTIONS preamble carries forward the **relevant** historical calibration lessons (e.g. B inherits the deferral-dynamic anchor HAW-06; A inherits the crude-channel/ledger-staleness lessons).

## 9. Naming (proposal — Will/DAEDALUS ratify)

Keep HAWK's **raptor family** to signal spun-out siblings:
- **Agent A (Russia/Ukraine):** `OSPREY` (raptor; the Osprey also evokes the long-range-drone/strike character of that war) — alt: `KESTREL`.
- **Agent B (US/Israel/Iran):** `FALCON` (Gulf **falconry** — thematically native to the Gulf theater) — alt: `SAKER`.
- Identity-over-functional per fleet convention (auto-memory `[[finding_subagent_naming_identity_over_functional]]`). Defer final choice to Will/DAEDALUS.

## 10. Cross-agent transmission-chain updates (flag → PROME, owns root CLAUDE.md)

Root `CLAUDE.md` currently says `HAWK → BRENT (oil/energy)`. Update to:
`{OSPREY, FALCON} → HAWK (geopolitical synthesis) → {BRENT, HENRY, LIQUID, SAM, CARL, REGINALD}`; acute theater signals may go OSPREY/FALCON → BRENT direct (HAWK cc'd). PROME updates the transmission chain + `ROSTER.md` (active agents, spinout provenance = "spun out of HAWK 2026-07").

## 11. Risks + mitigations

| Risk | Mitigation |
|---|---|
| Synthesis HAWK becomes the new rot point | Thin/derived synthesis (§6); HAWK boot-reads A+B briefs, reconciles, doesn't re-narrate |
| Migration drift / lossy KB surgery | Freeze-in-place (KB, predictions historical) + fresh forward files, not row-by-row splitting (§4) |
| Calibration history fragmented | Freeze HAW-01..17; new prefixes carry forward relevant lessons (§8) |
| Shadow-fleet / shipping double-owned | Explicit seam: A/B own theater incidents, HAWK owns the global war-risk/shipping synthesis (§3) |
| Coordination overhead (3 agents vs 1) | Steady-state via NEXUS_BRIEFs; teams-mode only for cross-war live sessions |

## 12. Migration sequencing (phased — nothing breaks mid-flight)

1. **DAEDALUS** scaffolds OSPREY + FALCON dirs (CLAUDE.md, STATUS/SCRATCH/NEXUS_BRIEF templates, workbook, strike ledger w/ Tier-1 fixes, predictions w/ new prefix + inherited OPEN row).
2. Migrate content per §4 (HAWK freezes historical KB/predictions; A/B seed fresh from live STATUS).
3. HAWK STATUS/NEXUS_BRIEF re-cut to synthesis+dormant (§5).
4. **PROME** updates ROSTER + root CLAUDE.md transmission chain (§10).
5. First cross-war synthesis pass by HAWK reading OSPREY + FALCON briefs (validates §6).
6. Retire HAWK's now-migrated Iran/Russia sections (leave frozen archives + pointers).

## 13. Open decisions for DAEDALUS + PROME

1. **Final names** (OSPREY/FALCON vs alternatives).
2. **Prediction prefixes** + whether historical HAW-xx lives under HAWK or a shared archive.
3. **KB migration depth** — freeze-in-place (recommended) vs theater-split.
4. **Baghdad-watch-class scripts** — does OSPREY want an analogous automated feed (e.g. a Russia energy-strike scraper) built at the same time?
5. **Migration-lighter variant** (for DAEDALUS's technical consideration, not re-opening Will's decision): keep Iran-war AS HAWK and spin out ONLY Russia — cheaper migration (HAWK's whole stack is Iran-built), but HAWK stays a war-tracker-AND-synthesizer, diluting the role-clarity goal. **Recommendation: proceed with the full split per Will's decision** (pure-synthesis HAWK); noting the variant only so DAEDALUS sees the trade-off was considered.

---
*Drafted by HAWK 2026-07-12 at Will's direction. Build owner: DAEDALUS. Roster/coordination: PROME. HAWK provides domain input + content migration.*
