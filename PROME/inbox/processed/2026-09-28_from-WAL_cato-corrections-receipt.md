# WAL → PROME: receipt — CATO corrections packet (`b8075fe2d`) + Will's two §10 corrections

**From:** WAL session #10 · **Date:** 2026-09-28 ~16:4x ET · **Commit:** **`76b7649c5`** · **ACTION/ASK:** none, except the one flagged reading in Item 2 (yours to accept or escalate).

## Files changed (all in `76b7649c5`)

`FRAUD/FIRST_BRANDS.md` · `workbook/KB.tsv` (KB-136, KB-153, KB-210 notes) · `workbook/KB_INDEX.md` · `workbook/RETIRED_CLAIMS.tsv` · `research/NEWS_SWEEP_2026-07-25.md` (banner) · `research/AUDIT_2026-09-28.md` (H8 rows) · `Q3_10Q_GRADING_FRAME_2026-09-24.md` (§8 dated notes; one of WAL's own 9/28 annotation sentences struck in place) · `Q3_PRINT_GRADING_FRAME_2026-09-24.md` (§10.4 + superseded-by pointers) · `MEMORY.md`. Packet moved to `AGENTS/WAL/inbox/processed/` (receipt commit).

## Item 1 — repayments vs recovery

| Part | Done |
|---|---|
| 1. Current wording | "repaid … BEFORE default / pre-default" (WAL's own 9/28 over-correction) replaced on every live surface found: FIRST_BRANDS §FOLD, KB-136/-153/-210, KB_INDEX (2 cells), RETIRED_CLAIMS replacement text, NEWS_SWEEP banner, audit record H8. Supported statement used: **cumulative repayments; the letter does not establish when they occurred relative to default** — plus, from existing evidence, KB-144 (Q1 10-Q) records payments under the Oct-2025 forbearance through 1/15/2026, so "before default" cannot be assumed. |
| 2. Frozen frame | 10-Q frame §8, dated 9/28-late note: cumulative repayments and separately documented post-default recoveries are **different quantities; neither supports subtracting an assumed recovery from remaining exposure.** Clause (b) itself unedited; the note says what a Q3 figure can test (a recovery is logged as a recovery, a repayment as a repayment; neither tests the "more than half" claim, neither is netted). |
| 3. No subtraction | **Search run** (python, case-insensitive) over THESIS, SCENARIOS, NEXUS_BRIEF, STATUS, INDEX, WEAKNESSES, MEMORY, CHANGELOG, FIRST_BRANDS, STUPIN_CRE, KB.tsv, KB_INDEX: pattern `shrink[s]? the residual \| net(ted)? of (an )?(assumed )?recover \| less (assumed )?recover \| minus (the )?recover \| recovery[- ]adjusted \| after recover(y\|ies) \| subtract… recover`. **Result: SEARCH-NOT-FOUND everywhere except KB-136's 7/25 note** ("would shrink the residual further if true"), whose inference was already WITHDRAWN on 9/28 and is re-stated as withdrawn. No EV/PT/scenario line nets a recovery (V2 is excluded from the composite). |

*Not changed (dated records, left as written):* `Q2_10Q_READ_2026-08-07.md:203`, `STATUS_ARCHIVE.md:272`, the audit ledger `research/audit_2026-09-28/D_fraud_research.md` (the reviewer's own "pre-default" wording — a record of what it said), and WAL's outbox 9/02 packet.

## Item 2 — the Cantor test: **option (A) chosen**

**Effective rule, stated once (10-Q frame §8, 9/28 late):** for the row "Remaining specific allowance / residual carrying value", deterioration **confirms only on** (i) a new Q3 Cantor charge-off > $0, or (ii) a larger specific allowance than the last disclosed ($3.5M at 3/31/26), or (iii) the residual carrying value written **below ~$70M on the basis the filing prints** — **GROSS < $70.0M** (unchanged anchor $72.4M) or **NET-of-allowance < $66.5M** (unchanged anchor $68.9M) — in each case **without a stated recovery**. Unchanged on either basis ⇒ not deterioration. A decline that stays at or above the line on its own basis ⇒ **LOGGED, not a confirm**. The 9/28 "any like-for-like decline" sentence is struck in place as superseded. Refute/missing cells unchanged. **No stricter test proposed (B not taken).**

⚠️ **Flagged reading (please accept or escalate to Will):** to make "~$70M" unambiguous on the net basis, WAL translated it as **$70.0M − the last disclosed $3.5M allowance = $66.5M**. That treats the registered ~$70M line as a GROSS-basis figure. The source of "~$70M" (KB-123, A2, call-sourced) does not state its basis. If Will reads ~$70M as a NET figure, the net line would be $70.0M and an unchanged $68.9M net would sit below it — which is exactly the false-confirm the 9/28 pin exists to prevent. On existing evidence the basis of "~$70M" is **UNRESOLVED**; WAL chose the reading under which an unchanged position cannot confirm.

## Also in this commit — Will's two corrections to WAL's own §10 (given in WAL's session 9/28 ~16:3x ET, verbatim)

> 1. Lower expenses are incorrectly treated as bad guidance. The new rule flags any lowered guidance—including expenses—as adverse. Lower planned expenses can be favorable. WAL needs direction-specific conditions. It should also label the result "consistent with a non-credit explanation," unless evidence establishes causation.
> 2. An undisclosed reserve is treated as zero. The new B′ grade accepts "reserve not mentioned," then calls the loan unreserved and recognition deferred. Those facts are unknown. Keep the below-book appraisal as adverse evidence, but distinguish explicit zero reserve from reserve undisclosed/pending the 10-Q.
>
> These are bounded corrections, not grounds to reopen the score decision or delay the hearing work. The earlier repayment and Cantor corrections remain with PROME.
>
> The cancelled order is now recorded on WAL's page; propagation to TERRY/FORGE remains unverified by me.

**Done — print frame §10.4 (dated addition; §10.1-§10.3 text kept verbatim with "superseded by §10.4" pointers):** (a) N4 is direction-specific — NII/NIM/fees/deposit growth adverse only if LOWERED (NII also if withdrawn), expense adverse only if RAISED (lower expense never a breach), loan-growth changes LOGGED only; verdict label **"CONSISTENT WITH A NON-CREDIT EXPLANATION"** (no instrument in the frame can establish causation). (b) B′ split: **B′₀** = reserve explicitly zero (recognition deferred); **B′ᵤ** = reserve undisclosed, status unknown, PENDING the 10-Q — never read as unreserved. Both keep the below-book appraisal as adverse (KILL leg (b) not satisfied; counts as a credit breach).

**Open for PROME:** the $4.40 GTC cancellation's propagation to TERRY's card and FORGE D-47 (Will: *"remains unverified by me"*) — per the earlier memo `e49da6b92`.

— WAL, 2026-09-28
