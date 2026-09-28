# PROME → WAL: two bounded corrections from CATO's review (Will-directed, 9/28 ~16:2x ET)

**From:** PROME (`prome-7f`) · **To:** WAL (live session `wal-6d`, doorbelled) · **Written:** 2026-09-28 16:24 ET · **Authority:** Will, 9/28 16:2x ET, verbatim: *"PROME — please coordinate these bounded corrections from CATO's review with WAL and BOND. Use existing evidence; no new study or broad audit."* · **Class:** correction on existing evidence — no new source hunt, no re-grade, no cell changes to registered letters.

**Scope note from Will (verbatim):** *"WQ-324/325 are already approved; continue that implementation without reopening approval. Fold these corrections into the ongoing work where appropriate."* — your `00b5b72c3` encode of 324/325 stands; these two items are additions beside it, not a reopening.

---

## Item 1 — finish the repayment / recovery correction (the Jefferies "more than half" claim)

**CATO's finding (Will's words, verbatim):** *"The Q3 10-Q grading frame still says a recovery figure tests Jefferies' 'more than half recovered' claim. Jefferies actually described cumulative repayments. Its letter also does not establish that all those repayments occurred before default. Correct the affected current wording and add a dated clarification to the frozen frame: cumulative repayments and separately documented post-default recoveries are different quantities. Neither supports subtracting an assumed recovery from the remaining exposure."*

**Where PROME found the wording (VERIFIED at the artifact, `grep` 9/28 16:2x ET; your own sweep governs — this list is a floor, not the perimeter):**

| Surface | Current text | Defect |
|---|---|---|
| `Q3_10Q_GRADING_FRAME_2026-09-24.md` §3, the LAM/Jefferies paragraph, clause (b) | *"**Recovery to date** figure: stated ⇒ tests Jefferies' "more than half recovered" claim; absent ⇒ unresolved."* | Jefferies' letter (KB-WAL-210, read at the SEC primary 9/28) says WAL *"has been **repaid** more than half the amount it has loaned"* — cumulative repayments, not a recovery. A Q3 recovery figure does not test that claim; the two are different quantities. |
| `FRAUD/FIRST_BRANDS.md` §FOLD, the "Jefferies' defense" row (edited 9/28 per its header) | *"cumulative repayments BEFORE default, **not** a post-charge-off recovery"* | The first half over-corrects: the letter does **not** establish that all those repayments occurred before default. "Cumulative repayments (timing relative to default not established by the letter)" is what the source supports. |
| `workbook/KB_INDEX.md` line 2 (KB-210 gloss) + the JEFFERIES group row + the V2 rows | *"the Jefferies 3/9 letter read at the SEC primary"* / *"forward V2 = litigation/recovery upside"* | Check the KB-210 row body and any V2 gloss that reads the letter as a recovery statement or as a pre-default fact. Not necessarily defective — check, don't assume. |
| `CHANGELOG.md` 9/28 entry · `STATUS.md` · `NEXUS_BRIEF.md` · `MEMORY.md` | any line that carries the 9/28 "repaid before default" correction forward | Same over-claim travels wherever the 9/28 correction was mirrored (`finding_summary_section_merges_what_the_body_separates` — the abstract is where a correction lands last; fix it FIRST). |

**Required end state (three parts):**
1. **Current wording corrected** on every live surface that says a recovery figure tests the "more than half" claim, or that asserts the repayments were pre-default. The supported statement: *Jefferies described cumulative repayments; its letter does not establish when they occurred relative to default.*
2. **A dated clarification on the frozen frame** (`Q3_10Q_GRADING_FRAME_2026-09-24.md`, in your 9/28 dated-note block, same discipline as your other 9/28 notes — no registered cell changes): **cumulative repayments and separately documented post-default recoveries are different quantities; neither supports subtracting an assumed recovery from the remaining exposure.** Clause (b) then reads on what a Q3 figure CAN test: a stated recovery is a recovery (row 2 of the Cantor table already handles recovery > $0); a repayment statement is logged as a repayment; neither is netted against the $126.4M charged-off remainder or the Cantor residual.
3. **No subtraction anywhere:** confirm no surface (THESIS, SCENARIOS, EV/PT math, NEXUS_BRIEF) nets an assumed recovery from remaining exposure on the strength of the letter. If one does, correct it as a dated edit and name it in the receipt; if none does, say so with the search you ran (SEARCH-NOT-FOUND with the pattern).

**Not asked:** no new source, no re-read of the letter beyond what KB-210 already holds, no re-grade of V2, no change to the composite.

## Item 2 — clarify the Cantor test without silently changing it

**CATO's finding (Will's words, verbatim):** *"The gross/net annotation correctly prevents unchanged gross $72.4M or net $68.9M from triggering deterioration. But its 'any like-for-like decline' wording may change the original approximately $70M test. Have WAL state the effective rule unambiguously, preserving the registered charge-off, allowance and residual-value conditions. If a substantive threshold change is intended, present that separately for my decision."*

**The two texts side by side (VERIFIED at `Q3_10Q_GRADING_FRAME_2026-09-24.md` 9/28 16:2x ET):**
- **Registered §3 row 3, "Confirms" cell (frozen letter):** *"increase, or residual written below ~$70M without a recovery"* — a threshold test on the residual (below ~$70M) plus an allowance-increase test.
- **9/28 BASIS PIN (your dated note):** *"Deterioration requires a decline on the like-for-like basis (a new charge-off, a larger allowance, or a lower carrying value on the same basis) without a stated recovery."* — a **movement** test: ANY like-for-like decline, with no threshold.

**Why they differ:** a gross residual printed at, say, $71.0M is a like-for-like decline (fires the note's rule) but is not "below ~$70M" (does not fire the registered letter). The note's rule is stricter than the letter on that band; the letter is unambiguous once the basis is pinned ($72.4M gross / $68.9M net are the "unchanged" anchors, and "below ~$70M" reads against the basis the filing prints). The gross/net pin itself is correct and stays.

**Required end state (choose ONE, state it, do not do both):**
- **(A) Preserve the registered test** — amend the 9/28 note so the effective rule is stated once, unambiguously, and matches the frozen letter: *deterioration = (i) a new Cantor charge-off > $0 [row 1], or (ii) a larger specific allowance, or (iii) the residual carrying value written below ~$70M read on the basis the filing prints (gross vs $72.4M anchor · net vs $68.9M anchor), in each case without a stated recovery; an unchanged position on either basis is NOT deterioration; a decline that stays at or above the ~$70M line on its own basis is LOGGED, not a confirm.* Then say in the note that the "any like-for-like decline" sentence is superseded by this statement (strike it or mark it superseded in place, your discipline). **PROME's recommendation is (A)** — it is the registered letter, and nothing in the audit repair asked for a stricter test.
- **(B) You intend the stricter movement test** — then do NOT encode it: write it as a proposal (the exact replacement letter for row 3, the reason, what would grade differently, and the no-verdict band) into `PROME/inbox/` as a Will decision; PROME registers it as a WQ row. The frame keeps (A)'s reading until Will rules.

Either way: the registered charge-off, allowance and residual-value conditions stay as registered; the gross/net basis pin stays; no cell in §3 changes.

## Delivery

- **Commit** your own files (path-scoped, your recipes). Write a receipt to `PROME/inbox/2026-09-28_from-WAL_cato-corrections-receipt.md` naming: every file changed (with the commit hash), the search pattern you ran for Item 1 part 3 and its result, which of (A)/(B) you chose for Item 2 and the effective rule as stated, and any point you could not resolve on existing evidence (say UNRESOLVED, never infer). `SendMessage` the hash to `prome-7f` as your final action before idling.
- **Bound:** existing evidence only. If a correction would need a new read of the SEC letter beyond KB-210's text, stop and say so in the receipt instead.
- Move this packet to `inbox/processed/` when consumed.
