# SAM repair completion check

September 21, 2026. Will asked whether SAM is now good after `12a32ef0b` / `d4539289d`. Inspected at shared HEAD `b6e05070b`. Bounded verification of the preceding three findings and closeout; no new domain audit, owner edits, sends, launches or trades. Other sessions' work preserved.

## Result: partial completion, not all three closed

- **KB endpoint finding closed.** `AGENTS/SAM/workbook/KB.tsv:190` now explicitly distinguishes high 158.054 and close 156.855 relative to intraday 157.34. Differences round to 0.71 and 0.49 yen. No fresh price-source or causal certification implied.
- **Propagation history partially fixed.** Brief, CHANGELOG and TIMELINE now distinguish the outage from the same-day committed correction interval. However, `AGENTS/SAM/MEMORY.md:49` still says the brief told peers it was dark “for 5 days after it wasn't.” This is the exact previously identified surviving claim, not a new audit topic. Also describe 82 minutes as the rounded interval between commits, not a precisely established exposure duration.
- **Verification scope partially fixed.** Local MEMORY, brief and timeline narrow the claim. But `memory/auto/finding_output_shape_implies_more_than_the_measurement.md:85` still says “every number SAM published was correct and independently reproduced by a reviewer”; the later paragraph still says every measurement layer was clean. The shared file was not changed by either repair commit. Prior finding concerning estimated/residual intervention allocation also remains within this same scope qualification. The receipt's universal “every single defect ... never the measurement” does not establish that generalization.

The `12a32ef0b` message says the residual sweep returns zero. The two quoted survivors directly contradict a complete semantic sweep. The already identified shared memory was outside the repair's actual path list. Do not interpret these known omissions as evidence for an unspecified new problem, or interpret smaller findings as proof nothing else could exist.

## Closeout checks

Ran full `python3 -B AGENTS/SAM/scripts/closeout_check.py`: exit 0, explicitly structural-only. Docket/counts/sidecar/handoff/brief ordering/tree checks pass. The same twelve-ledger and read-cap advisories remain; dispositions and limits in the [full closeout review](2026-09-21_0853_sam-full-closeout-verification.md) stand. The brief is committed after the other repair files. Remote ancestry confirmed through the fresh-fetch closeout receipt below/in-session; original owner receipt itself remains quoted evidence.

One operator-facing date correction: the pasted message says OIS live until 15:15 JST “today.” The record says **September 22, 2026, 15:15 JST**; at this September 21 review that is tomorrow. Use the absolute timestamp. No publisher refresh or live market data checked.

## Suggested completion

Correct the surviving local-memory duration and shared-memory certification paragraphs, retaining estimated/residual qualification; use the absolute OIS deadline in the receipt. Then existing applicable checks and closeout suffice. No new study or blanket review gate proposed or authorized. A future cold-read proposal can be considered separately; existing METSUKE and semantic consumer review already demonstrated relevant coverage when used.

Only this report and SAM's CATO continuity entry authored. Exact-path Git receipt follows in-session. Next: orient and await Will; other CATO instances unaffected.
