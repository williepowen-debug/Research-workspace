# Three WQ copies — reader comparison

**October 30, 2026 · CATO author comparison · no live adoption.** Open [the rendered comparison](index.html). [Generated Markdown queue](queue.md) · [derived view data](view.json) · [desktop screenshot](preview.png) · [check receipt](validation.json).

PROME supplied the mappings and expected meanings in commit `e948bfdbf4b01038ad9f2f3cb707bcdf1ff83cc5`: [comparison and owner conditions](../../../../../PROME/prototypes/wq-record-copies-2026-10-30/COMPARISON.md). This reader consumes those committed copies and the draft schema at `ddb8148bcba7ce13204aceff865799fb66fb920b`. All referenced sources are read at their pinned commits. These are historical samples, not a current workload display.

## Result

| View | Units |
|---|---|
| Decisions | None in these three copies |
| Tasks for me | 495.CDR |
| Follow-through | 495.NPORT; 551.HELD; 551.FIRM |
| History | 495.REPO; 552.ROTATION |

495 generates one OPEN row with Type HANDS, the date explicitly attached to CDR, and settled parts labeled for context only. That row is 1,106 UTF-8 bytes. NPORT's README/one-selftest/no-schedule conditions remain visible. 551.FIRM has its own DEFERRED badge and return condition; it is not approved by the parent's RULED label. 552 is one decision unit with its implementation correction visible. All views are read-only: no approval, task-report or response controls are installed.

The source states completion for 552; the page attributes that to PROME's owner evidence. CATO did not independently verify the underlying implementation. Pending docket observations are likewise labeled **at the source snapshot**. Missing owner keys remain unknown. Ruling time is labeled separately from implementation information.

## Findings that change the interpretation

1. **The deferral already has a schema home.** `disposition.state=deferred` and `timing.revisit_condition` existed in draft 0.1. This comparison makes them visible in Follow-through and in a derived “Deferred — re-present on” queue section. The existing docket already contains a deferral registration rule in its header, and pinned L879 explicitly says PROME re-presents FIRM at L834's return. A display list can improve visibility; no new boot routine or source of authority was installed. PROME still owns the adoption decision about how that existing return instruction is consumed.
2. **Exact proposal text is not necessarily an exact display snapshot.** The 552 copy claims `exact` because Will named A and the committed proposal was unchanged. That establishes an identifiable option, not the entire chat rendering. The page preserves PROME's label and explicitly marks exact display evidence as unestablished here. 495.NPORT, 551.HELD and 551.FIRM remain `reconstructed`. None of these labels invalidates or reopens Will's recorded rulings. PROME can substantiate or revise 552's display-provenance label. For the future app, store immutable shown terms and bind the answer to their revision/hash; Git-before-every-answer is not required, and a commit alone would not prove display.
3. **Duplicate task identity needs a reference, not an inferred replacement.** PROME identifies 495.CDR and the first WQ-31 item as the same action. This sample includes only 495; it discloses the duplication but does not demonstrate cross-WQ deduplication. At adoption PROME should select one task identity and link both references. `supersedes_unit_id` means replacement of an earlier unit; do not use it merely as an alias without deciding that replacement semantics is intended. No second deadline or action should be inferred from two mentions.
4. **CATO's docket-key wording needed correction.** The initial schema README said not to use physical lines. DOCKET's canonical L-number is deliberately a stable physical-line key under its append-only convention. The README now preserves that rule, and the copy reader resolves those keys correctly. An initial diagnostic treated the comment-headed docket as a headered CSV and produced no relevant observations; it was discarded and corrected before any state claim. No docket data was changed.

## Disposition of PROME's ten comparison items

| Owner item | Demonstrated here / remaining condition |
|---|---|
| M-495-1 | Active parts generate HANDS. Live authoring/consumer adoption remains PROME's. |
| M-495-2 | Settled context is labeled; no old NPORT approval buttons. |
| M-495-3 | Duplicate disclosed; cross-WQ identity resolution remains pending at adoption. |
| M-495-4 | Task visible in the app; no briefing or reminder routine changed. Retain the parked-HANDS policy in any later integration. |
| M-551-1 | Deferral and return condition visible; no new authority, automatic re-ask or boot registration. PROME resolves the owner read-path at adoption using existing rules. |
| M-551-2 | Historical choices shown as mapping identifiers, without controls. Require explicit author-defined choices for new actionable records; do not synthesize unrecorded live alternatives. |
| M-551-3 | Reconstructed provenance displayed. Exact display binding remains a future event contract; 552's stronger claim is separately qualified. |
| M-552-1 | One bundled unit demonstrated; component names do not create new decisions. |
| M-552-2 | Ruling time labeled; owner completion and correction are separate. No one-date-is-everything inference. |
| M-552-3 | Owner-reported completion displayed with attribution. No CATO independent-verification claim. |

These are not ten new repairs assigned to CATO. The reader behavior needed for this bounded comparison is delivered. The remaining conditions concern owner interpretation/adoption or subsequent live integration; they do not authorize either automatically.

## Reproduction and checks

From the repository root:

```sh
python3 -B AGENTS/CATO/prototypes/decisions/comparison/render.py
python3 -B AGENTS/CATO/prototypes/decisions/comparison/test_render.py -v
```

The renderer writes only `index.html`, `view.json` and `queue.md` in this directory. It uses the installed `jsonschema` package and local Git objects; it does not fetch, pull, synchronize, execute source instructions or write owner files. Source links navigate to the original pinned GitHub blobs only when a reader selects them. The page itself makes no network calls.

Seventeen Python checks pass, including the expected placements, wrong-source/unknown-state cases, exact-claim qualification, current-versus-settled due date, escaping, empty input, duplicate IDs, source boundaries and unchanged input copies. Eight browser checks pass at each of 1440 × 1150 and 520 × 1100 (sixteen executions); screenshots inspected. PROME's existing mechanical checker was rerun on all three unchanged copies and passed. `validation.json` pins the renderer, tests and generated outputs. These are author checks, not independent acceptance. No general live owner-state parser, event transport, identity/authentication or cross-machine synchronization is implemented.

**Stop:** Will can inspect this comparison. PROME retains the mapping/provenance and adoption conditions above. No live queue switch, new schedule, private-store read, phone service or response intake follows automatically from the passing demo.
