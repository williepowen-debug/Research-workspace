# CATO October 4 review — bounded BRENT correction pass

**Run:** 2026-10-04 22:3x–22:5x ET. **Scope:** BU1–BU7 only, starting from the concurrent working tree. No new broad audit, trade action, threshold, gate, prediction or thesis version. **$0.** CATO reproduction inputs: `AGENTS/CATO/runs/2026-10-04_brent-update-evidence/`.

## Dispositions

| Finding | Disposition | Evidence and resulting state |
|---|---|---|
| **BU1 — August IATA absent** | **REPAIRED WITH EVIDENCE** | `demand_destruction/DEMAND_COMPOSITE.md` now carries IATA's official August print released 9/30: global RPK −0.8% YoY, ASK +0.3%, load factor 85.1%; international −0.9%, domestic −0.5%, Middle East −14.6%, North America −2.2%, and ex-Middle-East global RPK +0.6%. Assessment changed from July's slight growth to headline contraction with a material regional-concentration caveat. Jet-fuel price remains at its own older vintage. Sources: `https://www.iata.org/en/publications/economics/reports/air-passenger-market-analysis-august-2026/` and `https://www.iata.org/en/pressroom/2026-releases/09-30-air-passenger-demand-slips-august/`. |
| **BU2 — Thursday connectors** | **UNRESOLVED — SPECIFIC DEPENDENCY** | Last effective evidence remains the 10/2 post-write fetch: Thursday had Gmail, Claude_Docs, Google_Drive, Quartr, Claude_Code_Remote and Canva; the other three had none, and API `mcp_connections: []` was ignored. No RemoteTrigger/routine-control tool is exposed here, so current live state cannot be re-fetched or changed. Exact Will action is recorded at the top of `SCHEDULED_RUNS.md`: open the Thursday routine in `claude.ai/code/routines`, remove all six integrations, save, reopen, verify zero connectors, and copy/export the live object for comparison. |
| **BU3 — Thursday early stop** | **UNRESOLVED — SAVED REPAIR COMPLETE; LIVE UI DEPENDENCY** | Corrected `after_thursday.txt`: an already-recorded core week produces `NO NEW CORE OBSERVATION`, but the routine continues through later supporting-file checks and records newly published support without duplicating the core print. Live cloud prompt replacement and re-fetch remain the UI action in BU2. |
| **BU4 — conflicting Git recovery / receipt** | **UNRESOLVED — SAVED REPAIR COMPLETE; LIVE UI DEPENDENCY** | Removed the legacy local `pull --rebase --autostash` and bare-`Pushed.` paragraphs from Monday/Wednesday/Thursday/Friday saved after-images. Each now has one instruction: follow current root Git Protocol and require the full fresh-fetch receipt. New SHA-256 prefixes are in `SCHEDULED_RUNS.md`. Live replacement/re-fetch remains the UI action in BU2. First-run acceptance remains separately pending; installation/configuration is not acceptance. |
| **BU5 — EIA parser** | **REPAIRED WITH EVIDENCE** | Table format is now selected from header structure (`Metric` plus identifiable current/prior/WoW columns), never date spelling. YoY is populated only from an identified YoY column. A missing YoY remains absent even when the row has `+2.0% WoW` and trailing prose has an unrelated `+9.9% YoY`; coverage reports `missing gas_yoy_latest`. Legacy parsing remains active unless a consolidated schema is positively identified. Tests reproduce Sep 2 and Sep 30, and retain April 29's supported fields. |
| **BU6 — Riyadh denominator/materiality** | **REPAIRED WITH EVIDENCE** | Removed “1% of Saudi crude runs.” The note now uses the dated matched capacity comparison only: 126 kb/d is about 3.8% of EIA's 3,291 kb/d 2023 Saudi domestic refining capacity. It explicitly separates nameplate capacity from actual throughput and confirmed loss. Damage, loss, duration, yield and materiality remain unknown; the conditional domestic-product transmission stands, but no outage or VLO-gate effect is assumed. A correcting board-log receipt supersedes the old assessment. |
| **BU7 — OPEC interpretation** | **REPAIRED WITH EVIDENCE** | The verified November hold and next meeting remain. Current notes, STATUS, NEXUS and CATALYSTS now say `COPS_OPEC` is September-vintage and OPEC-only, omitting participating Russia, Kazakhstan and Oman; it is conditional OPEC deliverability context, not a seven-country counterfactual. Removed “90% paper,” “near-zero physical,” and zero-expectations-gap precision from current analytical surfaces. Pre-meeting sourcing establishes expected direction only; no event-window pricing/signaling test was run. Historical board-log claims are explicitly superseded by a correcting row. |

## Verification

- `.venv/bin/python3 -m unittest discover -s AGENTS/BRENT/scripts/tests -p 'test_*.py' -v` → **70 tests passed**.
- `.venv/bin/python3 AGENTS/BRENT/scripts/eia_weekly.py --local` → **coverage complete** for saved wk-2026-09-25 / released 2026-09-30, including gasoline YoY +0.3%.
- `python -m py_compile` on the parser and tests → pass.
- `git diff --check -- AGENTS/BRENT` → pass.
- Saved-prompt scan → no legacy autostash/bare-receipt paragraph and no Thursday early-stop instruction in the four after-images.
- Calendar renderer/check and closeout checks are recorded in the commit receipt/final report.

**Ledger nudge disposition:** `CATALYSTS.tsv` and `board_log.tsv` were corrected in this pass and become current with this commit. `REGISTRY.tsv` and `COT_VINTAGES.tsv` did not move because no registered line or COT observation changed; `INCIDENTS.tsv` did not move because Riyadh damage remains unverified; `TRADE.md` did not move because no broker/position fact was established. `LESSONS_INDEX.tsv` requires the pre-existing substantive reconciliation and is outside this bounded correction pass; it was not falsely timestamped.

## What remains unverified / next observation needed

1. **Live routines:** Will's UI reconciliation plus an exported/re-fetched live prompt/config object is required to close BU2 and the live halves of BU3/BU4.
2. **First-run acceptance:** after installation is reconciled, observe Thu 10/8, Fri 10/9, Wed 10/14 and Thu 10/15 as already scheduled. This tests runtime behavior; it does not substitute for configuration verification.
3. **OPEC physical effect:** a matched participant-level deliverability/counterfactual, not an OPEC-only aggregate, is needed to quantify barrels. The Oct 6 STEO updates the OPEC context but does not by itself close the non-OPEC coverage gap.
4. **Riyadh:** an Aramco/Saudi/counting source establishing facility, actual throughput loss, duration and affected units is needed before materiality can be assessed.

Stop condition met: BU1–BU7 dispositioned; no wider audit opened.
