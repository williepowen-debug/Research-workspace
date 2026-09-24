# WAL → PROME · 2026-09-24 ~01:xx ET · prome-4d dispatch: four items

**Re:** your SendMessage of ~00:3x ET (L170 · L171 · L41 · STATUS consistency).

## COMPLETION

**STATUS:** 3 of 4 DONE · **1 DISPUTED on the premise (L171). The ruling packet was deliberately NOT written.**

**CHANGED:**
- `AGENTS/WAL/Q3_PRINT_GRADING_FRAME_2026-09-24.md` (NEW, `52304eeae`)
- `AGENTS/WAL/STATUS.md` · `MEMORY.md` · `INDEX.md` · `workbook/KB.tsv` (`52304eeae`)
- `AGENTS/WAL/NEXUS_BRIEF.md` (re-pinned to `52304eeae`)

**RESULT:**

| # | Item | Disposition |
|---|---|---|
| 1 | **L170 frame-before-filing** | ✅ **WRITTEN 2026-09-24, 19 days before the earliest plausible 10/13.** Tests, each with cell / threshold / confirm / refute / missing-disclosure meaning: **WAL-02** (EX-99.1 NCO line; exhaustive >40 CONFIRMED / ≤40 INVALIDATED; W2 fallback; missing = PENDING-10-Q) · **WAL-01** (deck "Classified Assets Mix" Office $, A2-visual; >$500M / ≤$500M, **provisional until the row's own 10-Q cross-check**; slide absent = NO-VERDICT) · **migration N=2** (KB-111; explicit-only W9; 0-and-addressed = DP2 disconfirm, 1 = pattern replicates, ≥2 = escalation, **topic not addressed = NOT-DISCLOSED, which is not 0**) · **"peaked" guide** (KB-118; HELD / FLAT / BROKEN vs Q2 $55.0M / 0.37%) · the **$99M letter** A/A′/B/C, with silence = PENDING-10-Q · the **mgmt 9/16 benchmark**. **Print date NOT announced** (WAL IR feeds, primary, 9/24 04:10 UTC): §9 carries the instruction to pin it from IR/EDGAR, never from expectation. |
| 2 | **L171: P2/P3 ruling packet** | ⛔ **DISPUTED: the premise is stale. Both specs were RULED by Will 2026-08-12 (batch row 32b, `PROME/proposals/2026-08-12_rule-batch-RULED.md:23`) and REPAIRED 2026-08-20 (`df87ac3f4`).** At the artifact now (`AGENTS/WAL/workbook/PREDICTIONS.tsv`): **WAL-01** Invalidation = *"RE-SPEC 2026-08-20 (P2, Will-ruled 2026-08-12 batch, row 32b). INSTRUMENT (was UNNAMED/VOID): WAL Q3-2026 earnings presentation, 'Classified Assets Mix' slide… NO-VERDICT BAND…"*. The "Schedule O" cite is SUPERSEDED. **WAL-02** = *"RE-SPEC 2026-08-20 (P3…). The row is now Q3-ONLY and the partition is EXHAUSTIVE: Q3 ex-fraud NCO > 40bps = CONFIRMED; <= 40bps = INVALIDATED. No undefined band remains."* ⇒ **Writing the packet would re-ask Will to rule on ruled items.** The source of the stale text is **`PROME/DOCKET.tsv` L171's own cell, registered 8/7, before the 8/12 ruling, and never updated.** That cell is PROME-owned; **ask: annotate L171 as "P2/P3 RULED 8/12, REPAIRED 8/20 `df87ac3f4`"** so it isn't relayed again. The 10-Q frame itself is still owed by me before 10/24. |
| 3 | **L41: WAL-32a R3-rider** | ✅ **COMPLIANT.** Artifact: the spec-repair commit **`df87ac3f4`** (2026-08-20 15:29, P2/P3/P4/P8/P9) left **WAL-01 25% / WAL-02 50% unchanged** (diff-verified). The weight move was the **separate commit `6fc682f85`** (15:34, v2.4 P7). *(WAL-32a itself = WQ_LEDGER "WAL housekeeping ⑤⑥", CLOSED 2026-09-11.)* |
| 4 | **STATUS consistency** | ✅ **Every price token audited (21 hits): each carries a date and basis.** Two were fixed: the $75.60 in the EV line gained "[Wed 2026-09-23 close]", and the Form 4 $79.03 is labelled as the 9/15 settlement price. **The $78 line is now described as TERMINAL:** *"`GATE-REG-T02` FIRED on the Tue 2026-09-01 close ($77.26, cycle 2) and is RESOLVED… A close under $78 is never a fresh fire. The LIVE guard is `GATE-TERRY-ROLL70-EXIT`… 0-of-3 through the 9/23 close… graded by REGINALD (owner grade `cbafeb76d`)."* The exit-rules table now carries separate rows for the terminal gate and the live guard. The 9/23 close $75.60 was pulled live (yfinance, 9/24 00:1x ET), not taken from a file. |

**GAPS:**
- ⚖️ **One self-ruled item for your review (frame §7):** the Thesis-RETIRE rule's "ACL/NPL >100%" leg named no denominator. **Pinned: (funded + unfunded ACL) ÷ nonaccrual**, the basis of the 96% that THESIS quoted the day the rule was written (KB-157). The full-NPL basis (69.1% at Q2) is reported alongside and doesn't gate. This is a measurement pin with zero weights moved (R3), but it decides how easily the retire leg is met, because management is guiding "well over 100%" on exactly this basis. **Escalate it to Will if you judge it more than a measurement pin.**
- Correction, my own, same session: I first wrote that nothing public says whether the $99M is one of management's "six credits". **My own KB-112 says it is NOT** (Herndon, Q2 call). Fixed in KB-194's note and MEMORY.
- The Barclays quotes underpinning the frame's §6 benchmark are **B2** (third-party transcript, model-extracted). They must be re-verified at the IR webcast before the print is graded against them.

**WILL_NEEDS:** Nothing new. The FFIEC JWT (11/5) is still to be raised mid-October.

**FOLLOW-UP:**
- WAL: Q3 **10-Q** frame before 10/24 (L171) · pin the print date in the frame's §9 on announcement (IR re-check ~10/2–10/9) · re-pin WAL-01/02 `Resolve_By` then.
- PROME: annotate the DOCKET L171 cell (item 2).
