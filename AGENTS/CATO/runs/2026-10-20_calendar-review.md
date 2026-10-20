# Calendar relocation and symmetry repair — independent CATO result review

## Disposition

**Accept the calendar relocation at `adbc76d18`; withhold acceptance of the symmetry repair's registration guarantee.** The moved projection is current against its committed DOCKET, repeat generation is byte-identical, stale/missing content is correctly distinguished, boot/closeout/direction references and paired skills are aligned. No rollback of the calendar move is recommended. Two bounded owner corrections remain: CM1's loose registration match and CM2's wrong description of the spawn slate's writer. Neither establishes that the committed calendar data is wrong.

Will requested this independent check on October 20, 2026, supplying PROME's account. Scope: commits `2f5efbf0d` and `adbc76d18`, their source/data snapshot, and the named producer/consumer instructions. No PROME edits, live boot/closeout run, BOARD advance, owner send or spawn. All mutation tests used temporary repositories or temporary document fixtures; only CATO's review records were saved in the shared tree. CATO did not implement this move/repair. This is one result review with fresh counterexamples, not a new helper launch. The acceptance file has no `reads:` line, so its prior independent-read count is UNKNOWN; this report records the present review without inventing the prior count. User-supplied owner account says outside review was pending.

## CM1 — MEDIUM, OPEN: missing registration still passes the final checker

**VERIFIED** at `PROME/tools/prome_gate.py:1202–1204`. The widened regex correctly harvests nine existing paths, including both lowercase-directory cases. But the registration test searches for the filename anywhere in the symmetry section rather than its actual registration row or one-way declaration.

Fresh independent counterexample against the final committed documents: remove only the table row whose first cell is `PROME/state/CALENDAR.md` from CLOSEOUT. Run the committed `check_symmetry()` against that modified fixture and the original BOOT. It still returns **True, "9 boot-read surfaces all registered"**. The DOCKET row still mentions `state/CALENDAR.md`; that incidental mention satisfies `Path(s).name in sym`. Replacing the calendar row's path with `AGENTS/BRENT/CALENDAR.md` also passes. A bare TODO comment mentioning `CALENDAR.md` can satisfy the same loose match.

This means the author's quoted row-removal test is not reproduced on the final snapshot. The narrower positive claim—lowercase directories now enter the harvested set—is verified. Actual registration happens to be present in the committed document; its absence is not reliably detected by the instrument.

Owner **PROME**. Correction: retain the improved path harvesting, but compare canonical paths to actual surface-column entries and explicit one-way declarations. Do not treat prose mentions, comments or another owner's identical filename as registrations. Add a regression which removes the calendar row while leaving all incidental references intact, and a wrong-owner same-basename case. Closure: ordinary final documents pass, missing/wrong-path fixtures fail, valid one-way references still work, and the changed implementation receives its applicable result check. No broader checker rewrite is requested.

## CM2 — LOW, OPEN: new one-way wording misstates the spawn slate's lifecycle

**VERIFIED:** `PROME/CLOSEOUT.md:65` calls `PROME/state/SPAWN_SLATE.md` "written by the boot gate itself, never at closeout." But `PROME/tools/prome_gate.py:1880–1882` invokes `spawn_slate.py --horizon ...` in the closeout path; its default `--out` is exactly that file (`spawn_slate.py:667`), and normal execution writes it (`:690–691`).

This is an instruction-description defect, not an observed failure of slate generation. The one-way classification can describe the absence of manual write-back, but the stated reason is wrong. Owner **PROME**: say that this is a gate-generated view at boot and closeout, with no separate manual write-back. Close when the declaration agrees with both caller paths. BOOT_MODULES as a procedure reference is a reasonable one-way entry; no compulsory edit on every closeout is implied.

## Accepted behavior and verification limits

**VERIFIED at the pinned snapshot:** BOOT step2 reads the calendar after SCRATCH; step8 uses it for catalysts; BOOT_MODULES, SYSTEM, STATUS and READS.tsv name the new home. CLOSEOUT's writer command targets it. Root and PROME-local boot skill copies match, as do the closeout copies. DOCKET was not edited by the move commit and remains canonical. SCRATCH has a pointer and no generated DOCKET block.

Executed the real generator from an isolated minimal Git repository containing pinned `scripts/docket_view.py`, DOCKET, SCRATCH and CALENDAR, using `--as-of 2026-10-20`:

- `--check-generated PROME/state/CALENDAR.md`: rc0, FRESH.
- `--write PROME/state/CALENDAR.md`: unchanged; all four fixture files remain byte-identical. The existing 6,000-byte generated-block budget advisory still prints; it is not a root read-cap failure or lost content.
- Deliberately alter generated content: rc1, STALE.
- Remove CALENDAR: rc2, assessed0; missing input is not a pass.
- `--check PROME/SCRATCH.md --section Calendar --ignore '\breviews?\b'`: rc0, zero dated claims, with its explicit zero-match limitation. That is expected for a pointer-only section; this result does not validate the calendar's dates. The separate generated-content comparison does.
- Root read-cap instrument passes `PROME/state/CALENDAR.md`. No full PROME boot, live source refresh, runtime read acknowledgment or full manifest attestation was certified by this scoped check.

Detailed observed outputs: [symmetry fixtures](2026-10-20_calendar-review/symmetry.json) and [generator execution](2026-10-20_calendar-review/execution.json). Reproduction requires only standard-library Python plus the pinned Git objects: obtain the pinned `check_symmetry` FunctionDef with `ast.parse`, execute it with `ROOT` set to a temporary directory and `record` collecting results, and write the two pinned documents to that directory. Remove only the exact CALENDAR surface row, retaining the DOCKET-row mention. The generator test copies the four named pinned paths to a temporary initialized Git root and runs the commands above there. No reliance on ignored raw captures or live owner state.

## Return to Will and stop condition

The requested review is complete. Keep the calendar move; PROME corrects CM1 and CM2 within the existing change episode and authorization limits. Do not count this external review as permission for another unrelated process change or a lifted session ceiling. No new monitoring, fleet launch or wider audit recommended. Resume CATO review on the changed repair and these preserved counterexamples if Will directs it; no equivalent whole-move rereview needed. Shared generator help still contains historical SCRATCH write examples; updating those at an authorized shared-tool maintenance touch would reduce the chance of reviving the old block, but this lower-impact residue does not block the PROME-local move.

Delivery checks: all intended inputs confirmed readable; weekday checker clean on PROME/DOCKET.tsv, GATES.tsv, WILL_QUEUE.md and CATO/CONTINUITY.md plus this report. Read-cap check passes the actual six startup files (CATO/AGENTS.md, CHARTER.md, CONTINUITY.md; root CLAUDE.md, USER.md, AGENTS.md), and separately the new calendar. Scoped whitespace check passes. Orphan advisory contains only WALTER caches outside CATO, untouched; no CATO-authored packet exists elsewhere. No auto-memory, STATUS ledger or domain figure changed, so those conditional checks do not apply. Exact-path commit and fresh-fetch publication receipt are supplied in-session; no separate dashboard publication is owed. Findings, tested behavior and unassessed runtime operation remain distinct.
