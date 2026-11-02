**DAEDALUS independent reader report — MIDAS structured evidence, predictions, thresholds and instrumentation**  
**Review date:** November 2, 2026. **Authority:** USER WQ-590; overdue/gaps review authorized.  
**Role:** read-only comprehension helper; no MIDAS ownership, grading or promotion.

Repository: `/home/willi/Research-workspace`; launch directory: `AGENTS/DAEDALUS`. Runtime: OpenAI Codex; requested model `gpt-6.1-sol`. An independent backend model identifier was not exposed. No files were changed, no production boot or market fetch ran, and no messages, commits or agents were created. This final response is the raw reader artifact for the caller’s outer `-o` persistence.

Paths below are repository-relative unless linked.

**Principal result**

The structured record is substantially richer than the September profile describes: 244 KB rows, 17 predictions, named-contract price binding, three-metal COT freshness, and six content-checked metal KB views. Predictions MIDAS-09/10 now have terminal November 2 grades.

The main structural findings are:

1. Invalid prediction inputs can silently produce a clean due scan.
2. VX identifies the watch as measuring standalone ETF band legs that it does not compute.
3. Gold COT freshness misses same-vintage value changes that the Ag/Pt/Pd leg detects.
4. The LME baseline accepts severely stale or incomplete history without the advertised degradation warning.
5. Historical on-demand instruments have material reuse limits; their successful execution cannot certify current questions.

These are bounded code/record findings, not a maturity verdict.

**1. Structured profile slice**

| Surface | Observed structure and role | Important local form |
|---|---|---|
| `workbook/KB.tsv` | 244 data rows; 244 unique IDs; nine columns | Permanent evidence authority. Dates, source tier and caveats travel with the fact. |
| `workbook/SCHEMA.tsv` | Nine field-definition rows | Describes KB fields; it is not a schema definition for every workbook ledger. |
| `workbook/PREDICTIONS.tsv` | 17 predictions; ten columns | Criteria, pre-committed consequences and long resolution records remain together. Resolved rows stay live for consumers. |
| `workbook/VX.tsv` | Five rows | Four scored channels plus an unscored M1 positioning sub-vector. Actual scores carried here are 4/1/1/2; positioning is explicitly `n/a`. |
| `workbook/FLOW.tsv` | Five rows | Monetary, silver, copper, PGM and liquidation transmission paths, with named consumers. |
| `KB_METALS.tsv` | Reviewed ID-to-metal classifications | Feeds generated views; multi-metal rows appear in `shared/KB.tsv`. |
| `<metal>/KB.tsv`, `shared/KB.tsv` | Six generated views | `refresh_metal_kbs.py --check` compares actual bytes with canonical ledger-plus-tags output. |
| `registry/corrections_receipts.tsv` | Two receipt rows | October 12 APPLIED receipt names KB-MIDAS-123 and the originating correction. |
| `sources/cot_vintages_consumed.tsv` | Ten gold vintage rows | A row means read and integrated, not merely published. Latest recorded vintage: October 27. |
| `sources/cot_metals_vintages_consumed.tsv` | Twelve rows: four vintages × three metals | Separate metal/code/value identities; latest recorded vintage October 27. |
| `workbook/MIDAS-06_KERNEL_NATIVE_COMPANION.json` | Typed question, forecast, close and resolution fields | Native TSV letter governs if interpretation differs. |

All five workbook TSVs parsed with consistent row widths and no missing or surplus columns in this read. This proves structural parsability, not factual correctness.

The desk’s instrumentation is deliberately distributed:

- `boot.py`: orchestration, freshness and due detection.
- `metals_watch.py`: named futures, pointer diagnostics, GSR, rate/gold patterns, weekly kill rail and copper inventory.
- `cot_gold.py`, `cot_metals.py`: source extraction and reconciliation.
- Dated analysis/source calculators: standalone band arithmetic and research.
- Historical graders: closed questions, deliberately outside standing boot execution.

Preserve top-level script locations, frozen letters, consumed-vintage meaning, source/basis labels, and the distinction between actual scores and counterfactual band levels.

**2. Contracts and threshold mapping**

| Rule or contract | Inspected implementation | Scope and limits |
|---|---|---|
| Explicit futures map | `metals_watch.py:113` | Gold GCZ26, silver SIZ26, copper HGZ26, platinum PLF27, palladium PAZ26. Hand-maintained. |
| Map review | `contract_map_review()`, line 129 | Review date October 30; now overdue. This is already acknowledged in `OPEN_ITEMS.md:3`. |
| Named-price eligibility | `read_contract_snapshot()`, line 182 | Checks metal prefix, delivery month, prior-bar date, seven-calendar-day age and positive volume. |
| Pointer discriminator | `DYING_VOL_SHARE=0.05` | Pointer volume below 5% of mapped contract volume produces review. It does not discover the liquid month independently. |
| GSR | `primary_gsr()`, line 230 | Requires matching dates and delivery months; named prices only. |
| GSR bands | Line 333 | Code uses inclusive 85/90/95 boundaries. Charter table prints `>85/>90/>95`; VX additionally describes a three-session sustain for its score consequence. One watch alert does not establish that sustain. |
| Copper inventory | Lines 343, 369–418 | +25/+50/+100% against rolling-history median. |
| Copper collapse conjunction | `copper_conjunction_context()`, line 242 | Inventory measured; price leg expressly UNMEASURED. No manufactured conjunction verdict. |
| M1 weekly rail | `measure_weekly_shape()`, line 279 | Four Friday-as-of common endpoints spanning three intervals; positive endpoint yield and GLD changes. Weekly-continuous is printed but has no grading effect. |
| Gold COT | Code 088691 | Canonical gold parser; totals and long-side reportable identity checked. |
| Other precious-metal COT | Codes 084691/076651/075651 | Exact market names, both reportable identities, valid dates and common vintage checked. |
| Standalone ETF bands | MIDAS `CLAUDE.md:139–166` | Separate trend, crash and upside legs; CROSSING eligibility; November 1 floor; crash decay; shared-root treatment. These are not implemented in the standing watch. |

Standalone numerical bands inspected:

| Metal | Trend levels 2/3/4 | Crash levels 2/3/4 | Upside levels 2/3 |
|---|---|---|---|
| Silver | −5/−12/−20% | −20/−30/−40% | +30/+40% |
| Platinum | −10/−15/−20% | −20/−30/— | +30/+40% |
| Palladium | −12/−20/−25% | −20/−30/−40% | +30/+40% |

Trend and upside use d200; crash uses dd252 with the registered decay mechanics. M2 takes the maximum of silver and GSR; I2 takes the maximum of Pt, Pd and supply. State legs do not permanently latch recovered levels.

**3. Invalidation-surface inventory**

| Surface | What it can invalidate or change | Clock / observed disposition |
|---|---|---|
| `THESIS.md:37–39` | Legacy gold shelf, quarterly CB floor, weekly divergence rail, gold/rate downside flip | Historical weekly fire retained; certified settlement still gates the downside flip. |
| `metals_watch.py:279–316, 640–699` | Mechanical weekly endpoint shape | Prints endpoint and declined continuous alternative separately; mechanism attribution remains unmeasured. |
| `workbook/PREDICTIONS.tsv`, each `if_falsified` cell | Specific claim and its registered consequence | Seventeen distinct letters; no generic blanket scoring consequence. |
| `CLAUDE.md:139–166` | Silver/Pt/Pd band eligibility and composite contribution | November 1 floor passed; qualifying crossings and current states still govern. |
| `VX.tsv`, threshold/source cells | Channel score and instrument mapping | Useful comparison surface; contains the standalone-band instrument mismatch below. |
| `FLOW.tsv`, FL-MIDAS-05 | Liquidation transmission interpretation | Instrument classification is distinguished from proof of forced sales. |
| `gold/research/2026-10-23_WQ451-decomposition-letter.md:48–58` | Liquidation, haven and official-flow claims | L1 November 5 close/retrieve November 6; L2 next ten stress days; monthly SAFE/TIC/WGC tests. |
| Same letter, section 5 | One-/three-month outlook | GLD price, trust tonnes, sustained rates/USD, or second liquidation event. Distinct from MIDAS-11/12 grading. |
| `TRADE.md:33–47` | Outlook checks and report-to-PROME/TERRY consequence | Snapshot through October 28; later October 30 report records the downside crossing. |
| `TRADE.md:49–55` | Unfreezing the research-to-construction surface | Registered fire, T+1 confirmation on both bases, and signal with falsifier routed to TERRY. |
| MIDAS-06 Kernel companion | Four-branch outcome mapping and scoring exclusion | YES/NO/AMBIGUOUS projection; binary calibration prohibited. |
| Retired M1 successor | No currently armed successor test | Retirement recorded by KB-MIDAS-236 and THESIS banner. Do not reactivate from historical dates. |

The old profile’s invalidation inventory is incomplete for this current tree. Its WQ-421 contradiction is also superseded: current `OPEN_ITEMS.md` explicitly records approval consumed October 20 and supersedes older OPEN language.

**4. Prediction resolution and routing evidence**

| Rows | Current ledger evidence | Consequence / routing evidence |
|---|---|---|
| MIDAS-01/02 | HIT; October 1 resolution records multiple bases and source limitations | Resolved letters retained. Underlying full resolution report not independently re-audited here. |
| MIDAS-03 | HIT, with explicit admission that actual yield direction fell outside the written branches | Do not describe this as a literal complete-branch success. |
| MIDAS-04/05 | NO-FIRE | No collapse escalation owed under their recorded antecedent/consequent tests. |
| MIDAS-06 | HIT, terminal branch (a), graded after the lagged observation published | Records M1 3→4 and BOND/LIQUID escalation; Kernel exclusion observed separately. |
| MIDAS-07 | INDETERMINATE | No branch fired. Known b/c overlap preserved; corrected base-rate claims recorded in resolution. |
| MIDAS-08 | INDETERMINATE | Branch (c) did not fire, so public correction obligation to BOND was not owed. INFO packet path is recorded. |
| MIDAS-09 | RESOLVED-c November 2; ratio change +17.35% | `THESIS.md:47`, KB-245 and `NEXUS_BRIEF.md:3` carry result and HENRY/LIQUID interpretation with liquidation confound. |
| MIDAS-10 | RESOLVED-c November 2; ratio change +5.85% | Records mistaken palladium tilt, unconfirmed UBS call and unchanged I2; peer brief names HAWK/HENRY. |
| MIDAS-11/12 | OPEN | November 20 / January 20 issuer-close sign calls; probabilities explicitly unassigned. |
| MIDAS-13/17 | OPEN | November 20 rebound-window and rate-residual calls. |
| MIDAS-14/15 | OPEN | November 2 endpoint; first retrieval November 3. Today’s due flag is not evidence of a missed permissible retrieval. |
| MIDAS-16 | HIT October 30 | COT value 46.9875% versus 52.4490%; KB-241 carries disaggregated composition caveat. |

Saved November 2 retrieval evidence exists at:

`AGENTS/MIDAS/shared/sources/2026-11-02_MIDAS-09-10_grade/retrieval.txt`

It contains the four resolving ETF observations, full-precision close dictionary and reproduced rounded ratio changes. This is saved evidence inspection; no new quotes were fetched.

Routing distinctions:

- MIDAS-09/10 results are demonstrably published in the owner’s peer-facing brief.
- Recipient consumption was not established. A bounded search of HENRY/LIQUID/HAWK inboxes and their `NEXUS_BRIEF.md` files returned no matching new result strings; this does not prove nondelivery through all possible surfaces.
- Whole `PROME/DOCKET.tsv` rows L819–L822 confirm registration of the WQ-451 L1/SAFE/TIC/WGC work. They expressly classify these as desk-letter tests, not action gates.
- Those four docket rows do **not** register MIDAS-13/16/17 individually; THESIS’s nearby “DOCKET L819–L822” citation should not be read as proof that they do.

**Kernel provenance slice**

Four canonical submission files exist: RegisterQuestion, SubmitForecast, CloseQuestion and ProposeResolution. Their native references pair the MIDAS-06 TSV record with typed JSON pointers and full source commits.

- Initial three: `80c6346c58166a13839fc246b87a51eef8bf86f1`.
- Resolution proposal: `a1f1a4c0c4a252a6e7d8e4510547dc5a8a157dfb`.

`KERNEL/tools/native.py:210–255` checks committed source existence, selected-byte hash and material-field reconciliation. I inspected that interface; I did not rerun its historical Git-boundary verification.

`KERNEL/views/CALIBRATION.tsv:14` contains MIDAS-06 as YES with blank Brier score and `OUTCOME_VOCABULARY_MISMATCH`. The view identifies itself as SHADOW, non-authoritative, rendered September 2. This supports the historical exclusion claim, not current Kernel health.

**5. Executed checks and PASS limits**

Every Python execution used `PYTHONDONTWRITEBYTECODE=1` and `-B`. Executable review harnesses installed an audit hook rejecting filesystem writes, mutations, subprocess launches and socket connect/bind. Watch tests used a synthetic `fetch` module, avoiding the real client’s re-exec, credentials and cache behavior.

| Check actually executed | Result | What it proves |
|---|---|---|
| `test_metals_watch_inputs.InputTests`, excluding vendor-adapter test | **22 passed**, zero failures/errors | Production watch logic discriminates tested wrong-pointer, unavailable-contract, stale/date/month, GSR, inventory and weekly-clock cases under injected inputs. |
| Ag/Pt/Pd freshness, in-memory ledger | Equal→0; unread→1; source older→2; missing metal→2 | Both clean and alert/failure paths discriminate these cases. |
| Actual KB content check | **0**, six views current | Generated bytes agree with current canonical ledger and reviewed tags. |
| Remove one tag in memory | Rejected KB-MIDAS-245 as unclassified | Missing classification cannot silently disappear from generated output. |
| Boot KB-leg propagation | Injected 0/1/2 produced boot 0/1/2 and correct named footer | KB-leg state reaches aggregate verdict. Other boot legs were mocked clean. |
| Actual prediction due scan | MIDAS-14 and MIDAS-15 listed | Calendar-date detection works for these valid rows. |
| MIDAS-07 grader | Historical input→no branch; overlap input→both b/c | Frozen ambiguity remains visible rather than silently resolved. |
| COT #3 grader | Stale self-comparison→3; registered historical print→0/FIRES | Historical stale guard and firing path execute. |
| Adversarial checks below | Reproduced | Establish specific false-clean or acceptance limits. |

The supplied `test_boot_cot_metals.py` and `test_metal_kbs.py` suites create temporary files. I inspected them but did not run them wholesale. Their relevant pure behaviors were tested with in-memory substitutes.

One harness attempt stopped because my synthetic ledger lacked `.name`; I corrected the harness and reran the affected checks. That error was not a MIDAS defect.

No result above certifies live feed availability, exchange settlement, current liquidity leadership, third-party adapter behavior, or the complete production boot.

**6. Ranked structural findings**

**F1 — High: malformed prediction inputs can report clean.**

Anchor: [boot.py:147](/home/willi/Research-workspace/AGENTS/MIDAS/boot.py:147), `predictions_due()`.

Missing date/status columns return `(0, [])`; malformed dates are skipped. A missing file is also treated as newborn/empty. Consequently, corruption of an established ledger can be indistinguishable from no due work.

Executed counterexamples:

```text
OPEN row, resolve_date="garbage" → (0, [])
OPEN row, resolve_date column absent → (0, [])
Valid old OPEN row → one due row
```

The positive control refutes “the scanner never detects anything.” Current real rows are well-formed; this is a demonstrated failure mode, not evidence that today’s ledger is corrupt.

Owner review priority: distinguish invalid established inputs from a legitimately empty ledger. Any implementation remedy changes what fires and needs its own consumer review.

**F2 — High: VX overstates standalone-band instrumentation.**

Anchors: `workbook/VX.tsv#VX-MIDAS-M2`, `#VX-MIDAS-I2`; [metals_watch.py:452](/home/willi/Research-workspace/AGENTS/MIDAS/metals_watch.py:452).

The VX source cells identify the boot watch as providing “SLV band legs” and “PPLT/PALL band legs.” The entire watch contains no d200, dd252, crash-decay, qualifying-crossing or standalone-band calculation. It prints ETF spot cross-checks.

Dated calculators do produce band arithmetic; for example, `shared/sources/2026-10-28_close/calculate.py` computes d200/crossings and writes results. Thus:

- “Standalone bands have no calculation evidence” is refuted.
- “This named boot command measures those bands” is unsupported by its code.

A watch PASS cannot certify the standalone-band state or post-floor eligibility. This finding does not imply automatic composite scoring should be added.

**F3 — Medium: gold freshness accepts same-vintage value disagreement.**

Anchor: [boot.py:179](/home/willi/Research-workspace/AGENTS/MIDAS/boot.py:179), `cot_vintage_leg()`; comparison at `cot_metals_vintage_leg()`.

Executed counterexample: preserve the report date, alter parsed gold net/OI by +1 percentage point. Gold leg still returns **0**, “current vintage already consumed.”

The Ag/Pt/Pd implementation explicitly returns **2** for same-date source-value disagreement. Gold’s consumed ratio is read but not compared in its equal-date branch.

This is a missed revision/disagreement notification. Detecting it need not authorize regrading a frozen prediction; stand-with-annotation and freshness detection are separate questions.

**F4 — Medium: LME baseline can accept stale, incomplete and duplicated coverage.**

Anchor: [metals_watch.py:369](/home/willi/Research-workspace/AGENTS/MIDAS/metals_watch.py:369).

The function silently skips failed year pages, checks 60 observations before selecting the window, and defines the window relative to the newest returned observation. It does not deduplicate dates or enforce present-day freshness.

Executed counterexamples:

```text
Only one page succeeds; 60 observations ending 2020-03-01
→ accepted median 200000, n=60

All three requested pages return the same 60 observations
→ accepted median 200000, n=180
```

The caller prints the result as a “2yr median.” The docstring promises a degradation flag; no such explicit warning is returned. Displaying `n` leaves an expert a clue, but does not establish two-year coverage.

This demonstrates acceptance limits under synthetic responses, not that current Westmetall data are wrong.

**F5 — Lower, historical-tool boundary: on-demand success is narrower than the descriptions suggest.**

Anchors: `grade_cot3.py:90,192`; `settle_check.py:62–64`; `grade_midas07.py:39–48`.

- COT #3 rejects non-advancing dates but accepts any later date. The same historical values labeled `2030-01-01` returned **0/FIRES**. Default programmatic mode returns 3 rather than actually driving the advertised pull/grade workflow.
- `settle_check.py` uses naive local wall time, labels any time after 13:30 as SETTLED, and does not implement its own documented after-18:00 in-flight distinction.
- MIDAS-07’s printed historical priors retain the subsequently corrected “structurally unreachable” claim, although its actual branch grader preserves the frozen frame correctly.

These tools are intentionally excluded from boot. That exclusion is correct and materially contains exposure. Preserve their historical record; do not treat them as current general-purpose certifiers.

**7. Refuted hypotheses and findings withheld**

| Hypothesis | Refuting evidence / disposition |
|---|---|
| Contract identity guard is still absent, as the old profile warned | Refuted by named-contract binding, map review and passing adversarial tests. Liquid-month selection remains manual. |
| Ag/Pt/Pd COT has no standing invocation | Refuted: boot leg 4 invokes it and uses per-metal consumed rows. |
| All graders should be boot-wired | Refuted by their frozen-question scope and demonstrated reuse limits. |
| MIDAS-09/10 remain unresolved | Refuted by full rows, KB-245, retrieval file, THESIS and peer brief. |
| WQ-421 remains an unresolved owner-state contradiction | Refuted by explicit October 20 consumption/supersession notes. |
| GSR can silently substitute the wrong continuous pointer | Refuted in tested cases: named failure blocks grading; wrong-pointer prices cannot manufacture the ratio. |
| Weekly-continuous persistence is secretly required | Refuted: printed as declined alternative; endpoint shape controls. |
| MIDAS-06 is currently binary-scored despite incompatible mass | Refuted within the inspected historical Kernel view: exclusion is explicit. |
| New results definitely reached consumers | Withheld: owner publication observed; recipient consumption unverified. |
| Current settlement source is adequate for the gold downside flip | Withheld: no source validation performed; owner records retain certification gap. |

**8. Complete coverage and limits**

**Read whole:** all specifically requested primary files—`boot.py`, `metals_watch.py`, `cot_gold.py`, `grade_cot3.py`, `settle_check.py`, `test_boot_cot_metals.py`, `test_metals_watch_inputs.py`, `test_metal_kbs.py`—plus dependency files `cot_metals.py`, `refresh_metal_kbs.py`, and `grade_midas07.py`.

**Ledger semantics read whole:** all 17 prediction rows; all five VX and five FLOW rows; SCHEMA; both correction receipts; both consumed-COT ledgers. Selected KB rows were read with **every column intact**: 112, 123, 127, 173, 187, 236, 240–245. All 244 KB rows and classifications were structurally processed by the read-only view checker; that is not a semantic review of every historical fact.

**Other whole or bounded substantive reads:** prior `profiles/MIDAS.md`; UPGRADE_PROTOCOL including Step 0 and review rules; OPERATIONS maturity ladder; root/local operating instructions and runtime mechanics; THESIS and TRADE; WQ-451 letter; Kernel companion and staging README; current resolution submission; saved November 2 retrieval; whole docket rows L819–L822.

**Partial/source-interface reads:** MIDAS charter threshold/boot/routing-related sections; OPEN_ITEMS and NEXUS_BRIEF relevant blocks; band-study source excerpts; dated close calculator anchors; FORGE client import/configuration preflight; Kernel native verification/material-field sections and calibration renderer. Initial oversized outputs clipped; decisive ledger rows and primary-code material were subsequently obtained separately. No claim relies on a clipped portion.

**Not read or not established:**

- Every historical KB fact, source bundle, archived report, lesson and packet.
- Full standalone band study and complete crossing/decay history.
- WQ-451 classifier/forward/stress implementation or its underlying datasets.
- Full Kernel acceptance/replay history, verifier receipts, activation validity or commit/hash revalidation.
- Full shared ledger-staleness or correction-check implementation.
- Current market facts, current broker holdings, live feed behavior or certified settlements.
- Third-party yfinance adapter test; full temporary-file test suites.
- Complete recipient inbox/archive consumption history.
- Concurrent owner changes after the individual reads.

No grade, promotion, owner mutation, research commission or remedy implementation follows from this slice. The caller should preserve these limits beside any synthesis and reconcile each ranked finding against owner-facing routing before claiming it handled.

**COMPLETION — DAEDALUS reader — 2026-11-02**

STATUS: DONE — bounded independent comprehension slice.  
CHANGED: None; raw artifact returned for outer `-o` persistence.  
RESULT: Inventoried five workbook TSVs, inspected 17 prediction rows, passed 22 isolated watch tests, and reproduced five ranked instrumentation limits.  
GAPS: Production/live-source certification and broader historical/consumer coverage remain unverified for the reasons above.  
WILL_NEEDS: None for this reader deliverable.  
FOLLOW-UP: Caller synthesis, coverage preservation and finding-by-finding routing reconciliation; no reader sends authorized.