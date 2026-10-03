# WQ-286 — fresh independent reader report, October 3, 2026

Reader: Codex Astra `review_ledger`, separate review agent; did not write the production fixes. Requested by DAEDALUS for catch-up steps 1–2. This is a fresh review, **not a recovered or reconstructed October 2 Opus transcript**. Synthesis/closure destination: `runs/2026-10-03_CATCHUP.md`. No production or owner files changed by this reader. New independent regression suite: `tests/test_ledger_catchup_20261003.py`.

REVIEW: required — changes to guard interpretation and trigger labels; scope `scripts/ledger_staleness.py` content clocks lines 122–177, attention aliases 363–384 and 511–532, header boundary 464–481, scan/report/CLI paths 885–end; `scripts/corrections_boot_check.py` receipt parsing and named/ALL branching 121–220, receipt path/main and selftests; reader Codex Astra review_ledger; disposition **initial G1 FAIL, remedy reviewed before implementation; G2 PASS-WITH-RESIDUE; R2 PASS-WITH-RESIDUE**. Any parent edit after this initial read is POST-REVIEW until independently re-read below.

## Authority and artifact pins

Read root `CLAUDE.md`, local `CLAUDE.md`, `UPGRADE_PROTOCOL.md` review rules 4/4a/4b and `BLUEPRINTS/CHECK_STANDARD.md` especially production acceptance, exit contracts and absence proof. Compared against the actual ruling `PROME/proposals/2026-09-24_wq-batch-284-252-285-286-RULED.md` WQ-286 row and `runs/2026-10-02_WQ286_ACCEPTANCE_AND_BUILD.md` including its amended acceptance conditions and seven residues.

Initial SHA-256 pins:

| File | SHA-256 |
|---|---|
| scripts/ledger_staleness.py | bacf9585542b2837a7a71c783c1624c4c82f602e34d9ec102796c364e9a81383 |
| scripts/corrections_boot_check.py | a60120317679154b97390c3e6519d2255e6a43f7753215b08e19c13c820c1110 |

A bounded filename search of `runs/` and `/tmp` found the acceptance record and two copies under a PROME scratch isolation, but did not recover the named October 2 reader ledger. The `/tmp` scan returned **rc2 permission errors**, so it establishes no complete absence claim. The existing acceptance file is a positive control for reading the own runs surface. No global session-history excavation was performed.

## Reader's counterexamples, findings and remedies

The counterexample to a clean G1 verdict is a recent date appearing in prose after an unrelated pipe beyond column 100, which should not be mistaken for a declared attention segment. A separate no-alias ledger using a legacy key tests G1's preservation promise. Both refute the initial implementation. A repeated alias with the newest occurrence second refutes the function's newest-clock claim. For R2, a RETIRED multi-target row with a passed cap and a receipt at only another target would refute the verdict if it cleared this target; the own-receipt code path and fixture checks preserve blocking.

| Finding | Reproduction and observed result | Disposition |
|---|---|---|
| G1-A unrelated pipe permits prose alias | `# LIVE | ` + 140 `x` + ` Planned future label Staleness sweep: 2026-10-01` becomes attention Oct 1, despite no declared segment at that key | **Blocker on claiming G1 review complete**; restrict far-right waiver to a new alias immediately after the last pipe with whitespace only between |
| G1-B waiver expands four legacy keys | Same far-right form with `Last reviewed:` (also all other three legacy keys), no new alias anywhere, now parses whereas the old cap rejected it | **Blocker on G1 no-alias preservation**; legacy keys retain single search plus original column cap |
| G1-C repeated alias chooses first occurrence | `# Staleness sweep: 2026-07-01 | Staleness sweep: 2026-10-01` returns July 1; malformed first date and valid second returns None | **Blocker on newest valid new-alias clock claim**; iterate new-alias matches, date-validate each, choose newest accepted |
| G2 qualified oldest | Oct 1 plain clock plus Apr 20 `(HAWK rows)` clock returns Apr 20; duplicate Oct 1 returns one distinct clock | PASS within declared grammar and first-eight-line scope |
| G2 row text | A first-eight-lines TSV data cell mentioning `Last real data refresh: 2026-04-20` becomes a clock | Existing declared residue, alarm direction; no boundary change proposed in this repair |
| G2 ninth line | Old clock on line 9 ignored | Existing declared scope limit, not repaired or represented as certified |
| R2 named RETIRED | No receipt, cap passed: rc1 and explicit RETIRED receipt-required label | PASS |
| R2 receipts | APPLIED / NO-OP / DEFERRED / CONTESTED each clears rc0; blank or invalid action rc2 | PASS; any valid action is the ruling, not application verification |
| R2 wrong target / ALL | Other named target: rc0; ALL cap passed: INFO rc0; ALL cap future: WARN rc0 | PASS; unchanged broadcast contract |
| R2 dead count | RETIRED with cap passed is omitted from DEAD-AT-CAP count | Existing cosmetic residue; block itself survives |

**False hypothesis corrected:** false `held` does **not** erase stale status or produce a clean exit. A full scan/report fixture with Apr 20 data and Oct 3 STATUS returned `stale=true`, `attention_held=true`, `+166d behind`, and one stale result, with the warning marker. The finding is a false assertion that somebody looked, especially misleading in the non-quiet held tag; it is not a suppressed stale rc. The correction must preserve this distinction.

Additional inherited residue: an attention date in the future (Oct 1, 2027 against Oct 3, 2026) returns negative age and may be held. This predates the new alias class through the common attention-age policy; not changed by this narrowly reviewed remedy. Invalid G2 dates are skipped under existing fallback policy. No global parser-hardening claim is made.

## Remedy review before implementation

Reviewed algorithm: for the four legacy keys, keep `rx.search` and `match.start() < MARKER_COL_CAP`; for `Staleness sweep` and `Last staleness check` only, use `finditer`, accepting either the existing column-cap range or a pipe whose remaining prefix to the key contains whitespace only. Preserve colon requirement, header boundary and newest valid accepted-date aggregation. No state token, output schema, return-code contract, file scope or consumer command changes.

Counterexample to this remedy: a real FERT/FLG clock beyond column 100 ceases to parse, or any no-alias ledger changes its attention result. Tested both directions. Production inventory first used 233 `AGENTS/*/workbook/*.tsv`; then expanded to **323 unique files from every agent directory's declared LEDGER_GLOB or default workbook glob**. The candidate changes **zero attention_info outputs** against the initial production implementation on those 323 files. This is an attention-result comparison, not a full fleet output byte comparison. All current FERT/FLG immediate pipe forms survive. WAL has repeated historical aliases but its newer front-loaded declaration dominates; FALCON has a legacy far-right old mention already dominated by a newer front-loaded line.

The independent suite contains nine test methods with multiple subcases. Against original code: five methods pass; four fail (six assertion failures and one TypeError caused by the missing second-match result). Against the reviewed in-memory candidate: **9/9 PASS**. This is evidence the tests distinguish the defect, not only agree with the remedy.

Consumer search used bare `rg -n 'ledger_staleness|corrections_boot_check' scripts PROME/tools AGENTS --glob '*.py' --glob '*.sh'`, rc0 with actual producer/consumer hits. Examined real wrapper code and dynamically exercised **FERT, FLG, WATT, VULCAN and MIDAS** `run_alert` functions by mocking only subprocess return: rc0 clean -> 0; rc1 -> 1; rc0 with warning marker -> 1; rc2 -> 2. Read DAEDALUS gate rc mapping, PROME `run_script` and corrections call, LABOR staleness aggregation, OZK relay, shared importers consumer_check and position_agreement_check (unchanged `is_frozen`/TRADE_GLOBS imports). MARCO/BRENT/HANS/BOND/SAM callers were located; their full boot/closeout was not executed. Because the remedy changes only attention annotation and neither rc nor markers nor any file/token boundary, their interface remains unchanged; **this is not a general correctness certification of every wrapper**.

## Commands and receipts

Commands below were run bare (tool-provided process rc, not a pipe's last rc). Rerun from DAEDALUS unless root paths are indicated.

| Command | Result |
|---|---|
| `python3 ../../scripts/ledger_staleness.py --selftest` | rc0, 33/33 |
| `python3 ../../scripts/corrections_boot_check.py --selftest` | rc0, 21/21 |
| `python3 -m unittest discover -s tests -p test_ledger_catchup_20261003.py -v` | Initial rc1, discriminates G1 defects as above |
| `python3 /tmp/daedalus-wq286-independent-review.py` | rc0; independent synthetic G1/G2/R2 cases and live 233-file inventory, results transcribed above |
| `python3 /tmp/daedalus-wq286-remedy-review.py` | rc0; candidate 9/9, 323-file comparison zero attention-result deltas, five real wrapper functions all four expected outcomes |
| `python3 ../../scripts/ledger_staleness.py HOMER --quiet` | rc1; STATE_HSG +42d; three clocks Aug 22 / Sep 14 / Sep 29, oldest governs; 10 scanned, three outside perimeter explicitly printed |
| `python3 ../../scripts/ledger_staleness.py FERT --quiet --days 0` | rc1; five named files +1d, attention ~3d all recognized; frozen duplicate board_log absent from stale set |
| `python3 ../../scripts/corrections_boot_check.py DAEDALUS` | rc0; 32 register rows, zero unreceipted named, one expired ALL |
| `python3 ../../scripts/corrections_boot_check.py SAM` | rc0; three receipts, zero named debt; old documented defective SAM production case has been overtaken |

`/tmp` scripts are scratch reproducibility aids, not durable deliverables. The durable test module plus these exact inputs and output tables carry the review. Live registry/header state is point-in-time and may change as other sessions work.

## Coverage and limits

Read: this desk's relevant authority/acceptance files, shared production scripts, declared-ledger header population, named consumer paths above, WALTER register header and live parsed rows. WALTER's header already defines RETIRED as VERIFIED closure and per-target receipts; this review does **not** certify completion of WALTER's separately owned specification assignment. No edits to WALTER or PROME. No market-source validation, semantic validation of owner attention declarations, actual receipt actions, all-depth TSV content review, network calls, full-fleet boot executions, BARON freeze recertification or grade assessment. Historical Opus evidence remains unrecovered. Own DAEDALUS surfaces are included in the declared-glob population and its corrections production control; no claim of whole-desk review.

## Final artifact re-read — October 3, after parent repair

Parent applied the previously reviewed remedy; reader re-read the actual `attention_info` body (lines 511–536) and reran the independent tests against that production module. It matches the reviewed algorithm: legacy single-match/cap behavior preserved, only new aliases receive the immediate pipe-segment exception, and all valid accepted alias occurrences compete on newest date. This paragraph explicitly closes the POST-REVIEW interval for that repair only.

Final pin: `scripts/ledger_staleness.py` SHA-256 **117789ab8fa4aa00241bf2a92f49550e363891b8d218aa788e109f187b79b93a**. Corrections pin remains **a60120317679154b97390c3e6519d2255e6a43f7753215b08e19c13c820c1110**.

Final independent suite **9/9 PASS, rc0**; built-in ledger suite **33/33 PASS, rc0**, each process return code collected explicitly via subprocess. Final production-vs-saved-before attention-result comparison across **323 declared-glob files: zero changes**. Consumer contract remains unchanged by code inspection; five wrapper discriminator tests above remain applicable without edits to their interface.

**Final verdict: G1 PASS-WITH-RESIDUE (three reviewed defects repaired); G2 PASS-WITH-RESIDUE; R2 PASS-WITH-RESIDUE. Zero unresolved blockers within this bounded repair.** The inherited parser limits and owner-dependent specification assignment remain the residues explicitly listed above. No historical review evidence was fabricated or claimed recovered.

REVIEW: required — attention-clock interpretation; scope final `scripts/ledger_staleness.py:511–536` plus final regression suite and 323-file comparison; reader Codex Astra review_ledger; disposition **APPLIED 3 · RESIDUE declared above; final artifact independently re-read**.
