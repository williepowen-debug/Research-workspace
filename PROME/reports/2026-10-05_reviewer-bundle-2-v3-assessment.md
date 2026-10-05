# Reviewer bundle 2, v3 — PROME assessment

Reviewed the supplied consolidated v3 patch and addendum against the shared checkout. The patch applies cleanly. Applied only in disposable export `/tmp/prome-review2-v3-74cpw5eo`; no production implementation changes or fleet launches.

**Disposition: requested v2 corrections verified; one narrow fail-closed correction recommended before adoption.** No further redesign requested.

## Verified corrections

- Real consumer-checker fixture with `Warehouse inventory: 320 crates.` and metric 320→321: own blocking row passes, separate orange verification advisory remains, consumer gate aggregate rc 0.
- Real checker with live gamma value 12345 and update 12345→12346: own red row fails, aggregate rc 1.
- The fleet remains advisory; packets and candidate verification remain operator obligations.
- `PROME/DOCKET.tsv+PROME/GATES.tsv` now splits into two paths. `AGENTS/X/handles+drift.md` remains intact. Leading-dot paths and single-line locators still work. Restricting bare-plus splitting to recognized repository roots is a reasonable compatibility compromise for this bundle.
- Dormant cap documentation now accurately distinguishes the silent save hook from pre-commit and closeout notices. The closeout summary explicitly labels the unset cap DORMANT. No numerical cap adopted.

## Remaining failure-path issue

In `parse_consumer()`, the return code qualifies only the clean-footer branch. A candidate footer is accepted with any return code. The own-directory summarizer then returns True whenever the parsed stale count is zero. `run_script()` replaces its initial exit-code assessment with that return value.

Independent fault injection through the actual `run_script()` wrapper: subprocess output `  🟠 1 CANDIDATE(s), zero certified-stale.` with process rc 1, and separately rc 2. In both cases the own BLOCKING row passes and the consumer gate aggregate returns 0. This is a malformed/failed-producer case, not a claim that an ordinary successful consumer scan emits these combinations.

**Bounded correction:** validate the strict producer contract in the shared parser before returning: positive stale verdict requires rc 1; candidate-only or clean requires rc 0; unexpected codes, contradictory verdicts or verdict/code disagreement raise ValueError. Existing wrapper behavior then records UNKNOWN and fails the own blocking row. At minimum, require rc 0 before the no-stale own row can pass. Add candidate-footer/nonzero-exit regression coverage. No change to orange advisory policy is needed.

## Validation and limits

All seven suites pass with ResourceWarning treated as error:

| Suite | Tests |
|---|---:|
| docket row cap | 19 |
| closeout declarations / non-advancing boot | 15 |
| locks safeguards | 14 |
| repeat boot | 33 |
| boot coverage | 21 |
| orchestration closeout | 17 |
| closeout simplification WQ240 | 23 |
| Total | 142 |

The first WQ240 run lacked CLOSEOUT_PROCEDURES.md in the partial export; restoring its tracked HEAD copy resolved both setup errors. No patch change was needed.

Independent real-checker cases, fault injection and parser receipts: `/tmp/prome-review2-v3-74cpw5eo/v3-probes.json`. Broader docket census and filesystem-write enumeration remain reviewer-reported. Prior scope limitations remain: mirror-map checks require a separate invocation; numeric cap selection, rule-row classification, verification receipts and the DAEDALUS C2 issue are separate work. No live hooks installed, commit performed or packet sent.
