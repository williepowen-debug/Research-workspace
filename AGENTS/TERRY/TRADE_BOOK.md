# TERRY TRADE BOOK
**Created:** 2026-06-20

Human-readable ledger of Terry-reviewed trade plans. Full cards should live under `setups/YYYY-MM-DD_ticker_structure.md` when created.

| Date | Setup | Thesis owner | Terry verdict | Will decision | Status | Card |
|---|---|---|---|---|---|---|
| 2026-06-20 | Terry scaffold | Prome/Will | N/A | Approved scaffold | Created | — |
| 2026-07-16 | TRY-FIRE-004 TLT Sep-18 duration-short (arm-#2 fired 7/13) | BOND (VX-BND-05) / HENRY | BOOK-AWARE: ADD NOTHING / bank $500 (Will already owns grind via TBT+85P+82P ≈$1,150; 81/76 spread redundant; crash-tail 77P = only non-redundant add) | Ladder structure approved; Terry recommends bank + re-fire | PROPOSED | setups/FLOW-TRIGGER_duration-TLT-put.md |
| 2026-07-16 | USO 7/17 calls triage (120C/127C expire tomorrow) | BRENT (energy re-arm) / Will | SALVAGE 120C (protect ~$204, don't feed extrinsic to theta into 2-way 1DTE catalyst @ OVX 61); 127C near-dead lottery; keep shares | Pending Will | PROPOSED | outbox/2026-07-16_to-PROME_uso-0717-calls-triage.md |
| 2026-07-17 | WAL grind put-spread (77.5P/67.5P Jan-2027) — properly-tenored bank expression from Part B tenor diagnostic | REGINALD / Will (NOT TERRY) | CONDITIONAL — clean structure, gated on thesis-owner confirm + post-7/21 entry + not-already-broken-down; spread is the $500-cap-compliant version (outright 77.5P $605 breaches). Preferred as ROLL TARGET for dying Sep WAL puts, not additive | Pending (not armed/fired) | CONDITIONAL | setups/WAL_grind-putspread_2026-07-17.md |
| 2026-07-17 | TRY-FIRE-006 Kharg-strand USO OTM call spread (flow-anchored PRE-BUILD) | RED (finding A) + BRENT (Scenario-C/$200) + FALCON (Kharg tripwire); PROME-routed, Will-approved pre-build | Structure Medium — spread mandatory (OVX p93 vol tax); trigger = Kharg EXPORT-loadings strand, explicitly NOT the Hormuz transit count (86.6% base rate). $200 NEW tranche, separate from 004's $500. Rule #6 green-day break pre-authorized (gap-continuation). OPEN DEP: Kharg-loadings data source to freeze with FALCON before ARM | Pending (built ≠ armed ≠ deployed) | PRE-BUILT/SHELVED | setups/FLOW-TRIGGER_kharg-strand-USO-call.md |
| 2026-07-17 | TRY-BUILDER-DHI-PHM homebuilder put spread (DHI 7/21 / PHM 7/22 earnings) — surfaced by fleet trade-scan | HOMER (housing) [CONFIRM_NEEDED] | CONDITIONAL — front-week naked puts = BAD STRUCTURE (IV ~52% crushes to ~40%); only defensible as a Sep put SPREAD (Path A post-print continuation = cleanest, or Path B pre-print green-Mon-only). Bad news partly priced (both −2-3% today, ±5-6% expected move), rich vol, and it deepens the SAME higher-for-longer book as 004 (not a diversifier) | Pending (not armed/fired) | CONDITIONAL | setups/HOMER_builder-putspread_2026-07-17.md |
| **2026-07-20** | **★ TRY-FIRE-004 re-fire — FIRST LIVE FIRE** (TLT Sep-30-26 77P gap-tail) | BOND (VX-BND-05, real-policy-path/term-premium channel) | **CLEAN** — arm-#2 LIT/latched + rule-#6-clean GREEN-TLT entry + live 77P ask $0.11 ≤ no-chase $0.12; non-redundant gap-tail (Will owns the grind, not the 77 tail). Pays on a GAP not a grind; small conditional lottery | **APPROVED + FILLED 30× @ $0.11 = $330 at risk** (~$170 of $500 bank dry) | FIRED/ACTIVE | setups/FLOW-TRIGGER_duration-TLT-put.md |

## Status Values

- `DRAFT` — under construction, not ready for approval.
- `PROPOSED` — ready for Will approve/reject.
- `APPROVED` — Will approved; execution still external/manual.
- `REJECTED` — Will rejected.
- `ACTIVE` — known open position; requires broker truth.
- `CLOSED` — closed with postmortem complete.
- `EXPIRED/SUPERSEDED` — no longer actionable.
