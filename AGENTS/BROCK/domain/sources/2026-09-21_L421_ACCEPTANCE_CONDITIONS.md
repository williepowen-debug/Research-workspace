# L421 STATUS.md HOT/COLD SPLIT — ACCEPTANCE CONDITIONS

**Written 2026-09-21 12:0x ET, BEFORE any edit** (WQ-229 discipline: state the conditions in the defect's own terms before executing the repair). **Owner: BROCK. Reviewer: cold-read at result — self, mechanical checks. No independent reviewer required — this is a structural rotation, not a rule change; nothing in the file's SCORES or THRESHOLDS moves as a side effect.**

## Defect (verbatim from DOCKET L421)

STATUS.md measured 132% of the 32,550 B budget on 9/18 (~126% on 9/12). Three verbatim rotations landed it at **100.0%, 14 B OVER**. A fourth "collapse" pass went **backwards (+38 B)** and was reverted (LESSONS #36). More nibbling reliably adds bytes; only **moving text out** removes them. Repair must be a **structural hot/cold split**, one session, WQ-178 plan/result reads.

## Acceptance conditions (the tests the repair must pass; these ARE the test list)

**A1. BYTE COUNT.** Final `wc -c AGENTS/BROCK/STATUS.md < 22,785 B` — the read-cap rule-5 STOP (<70% of budget). Not the 75% trigger — stopping there re-breaches on the next append (PAT-055).

**A2. FACT PRESERVATION.** Every load-bearing claim now on STATUS is either **carried live** or **rotated verbatim** to `AGENTS/BROCK/archive/STATUS_ROTATED_2026-09-21.md`, with a pointer line on STATUS a reader can travel. Verbatim rotations are byte-identical to the pre-rotation text (crc32 recorded in the archive file's header before it is moved).

**A3. NO SCORE MOVEMENT.** The convergence matrix scores (14 vectors, `57/70`) and all EXIT-RULE numeric thresholds are UNCHANGED. A rotation may not become a threshold move. Verified by grep of pre/post `Convergence: 57/70` and matrix row scores.

**A4. VX-BRK-020 downgrade RECORDED WITH REASON (L347).** Status cell in `workbook/VX.tsv` moves RED → ORANGE with a written reason (10Y has never closed >5.00%; the isolated-BDC-markdown leg has no primary evidence). ⚠️ This IS a change, and it CUTS AGAINST my thesis — that is why L347 registered it as a deliberate pass, not a quiet closeout edit. The score on the convergence matrix at line 61 is ALREADY 🟠(3); this VX.tsv edit brings the workbook cell into alignment with the score, it does not move the score.

**A5. TODAY'S L312 FINDING VISIBLE.** The 9/21 stamp reports at primary: CRMT filed **8-K 0001171843-26-006114, accepted 2026-09-18T20:05:18Z**, extending the Scheduled Termination Date **9/18 → 9/24** — a **third bridge, filed ~8 hours after the 9/18 read that graded silence**. L343's silence grade was overtaken by the same failure class it warned about (`finding_directive_overtaken_between_authorship_and_delivery`). The 8-K's Item 8.01 discloses a **strategic-alternatives review**. §2.1 (a) new permitted warehouse — NOT satisfied; (b) refinancing — NOT satisfied (this is a bilateral extension of the same Silver Point agreement).

**A6. OUT-OF-SCOPE FILES UNTOUCHED.** Only `AGENTS/BROCK/STATUS.md`, `AGENTS/BROCK/workbook/VX.tsv`, `AGENTS/BROCK/archive/STATUS_ROTATED_2026-09-21.md`, `AGENTS/BROCK/docket/CATALYSTS.tsv` (calendar row date change 9/18→9/24), and this memo are modified in-session. `git status` verified before commit — no PROME/*, no root docs, no other desks' files.

**A7. READ-CAP CHECK PASSES.** `python3 scripts/read_cap_check.py --agent BROCK` at closeout returns `rc=0` (or the STATUS row is BELOW 70% of budget). Independently verified by `wc -c` and by `measure.py`.

## Neighbours (WQ-229 five categories — consider, not perform)

- **Ordinary case:** rotate the two big blocks (Updated stamp, BOTTOM LINE) verbatim to archive, replace with compressed heads. ✓ In scope.
- **Overlap:** the BOTTOM LINE and the 9/18 stamp are ALREADY partly referenced by `archive/STATUS_ROTATED_2026-09-18.md`; the 9/21 archive file must not double-rotate content that is already in an earlier archive. Check: only the CURRENT (still-on-STATUS) text is rotated. Verified by diffing rotation candidates against the 9/18 archive before writing.
- **Wrong owner:** N/A — every edited file is in `AGENTS/BROCK/`.
- **Missing information:** the L312 primary read is required for A5. VERIFIED at `data.sec.gov` at 12:0x ET (accession `0001171843-26-006114`, primary doc `f8k_091826.htm`). ✓
- **Concurrent activity:** `git status` clean before edits; `git status` verified again after edits and before commit. If anyone else has staged AGENTS/BROCK/* mid-session, stop and reconcile.

## What this repair does NOT claim

⛔ Not INDEPENDENTLY VERIFIED — no cold reader ran. This is a structural rotation where the test is mechanical (byte count + verbatim preservation), and the acceptance conditions above are the test list. State per WQ-229: **IMPLEMENTED · TESTED (by author) · NOT INDEPENDENTLY VERIFIED · L421 CLOSES ON RECEIPT AT PROME.**
