# Closeout reader — overnight coverage repair

Will relayed CATO's medium finding from `AGENTS/CATO/runs/2026-09-16_1249_carl-prome-local-review.md` §2. Reproduced before repair: selected-date filtering discarded an unresolved prior-date touch. Four new regression cases failed on the original reader. No actual lost live helper established.

Repair: enumerate touches through the selected ET date, then validate closeout evidence before excluding earlier completed or explicitly WILL-owned touches. Earlier ASKED_WORKING, DARK_BEFORE_ASK and UNKNOWN remain individually named, with original dates and keys. No one-day lookback cutoff. A different touch's receipt cannot resolve an earlier touch. Complete inventory now covers selected-date plus unresolved prior touches; missing external inventory remains UNKNOWN. Future dates and CLOSE summary rows remain outside the touch population. Prior malformed completion evidence is retained as UNKNOWN; a valid receipt observed after midnight closes the original touch.

Validation: `python3 -B -m unittest discover -s tools/tests -p test_orch_closeout.py -v` — 17 tests pass, including overnight CLI output, multi-day carryover, invalid and valid closure, distinct touches and both existing advisory gate entry points. No live ledger mutation.

Live ledger read September16: 156 retained touches = 14 ASKED_RECEIPT current-day records + 142 prior UNKNOWN evidence records. Those 142 are historical evidence gaps, NOT evidence that 142 helpers are active. No automatic backfill, inferred receipt, or historical closure applied. This increases advisory output until historical evidence is reconciled; reporting uncertainty is deliberate. Native receipt authentication and complete runtime inventory remain separate open limitations. This repairs the date-boundary defect, not all L378 runtime acceptance conditions.

Files: `PROME/tools/orch_closeout.py`, `PROME/tools/tests/test_orch_closeout.py`. Owner-only code changes; other active desks' dirty files untouched. Local commit only; push deferred while other desk work is dirty.
