# OTTO COMPLETION — 2026-09-02 (session 021)

> **One sentence for the next boot:** the 9/9 deliverable landed **seven days early** and the corrected basis **did not move the finding** — 30 of 30 still worse YoY — but the four things learned getting there are all defects in OTTO's own instruments, and one of them is that a catalyst row was re-keyed forward across the window in which its event had already fired.

## STATUS
✅ **PROME-spawned dark-owner drain, executed in full.** Inbox **15 → 0** (5 root + 10 WALTER). DOCKET **L246 / WQ-107 CLOSED**. Read-cap breach **FIXED** (rc 1 → 0). Two letters pre-registered with numeric bands **before** their dates. No prediction overdue (11 OPEN, 0 due). No thesis moved. No trade.

## CHANGED
- **`workbook/PANEL_10D.tsv`** — 14 → **15 columns**, `collection_period` at position 6, **137/137 rows populated**, 133 → 137 rows (EART July pulled on).
- **`scripts/panel_10d.py`** — label-anchored collection-period reader for all three disclosed shapes + a loud one-time legacy-14-col migration so a pre-backfill row is never discarded as ragged.
- **`scripts/backfill_collection_period.py`** (new) — one-shot, positive-control gated, atomic write.
- **`STATUS.md` 69,591 → 32,427 B** + **`STATUS_COLD.md`** (new, 53,795 B, explicitly not a boot read) — verbatim hot/cold split, pointers both ways.
- **`research/outputs/RP-OTT-5.1_CRMT_TRICOLOR_PREREGISTERED_LETTERS.md`** (new) — Letters 1 (9/4) and 2 (9/7) pre-registered; Letter 3 grades the Tricolor ladder.
- **`workbook/SHELF_ACTIVITY.tsv`** — FROZEN banner + cadence declared EVENT-DRIVEN + now named in STATUS (DAEDALUS staleness #4 / PAT-095 answered).
- **`docket/CATALYSTS.tsv`** — 2 rows swept, 1 retired-with-reason, **5 new rows** (grade dates, the 9/9 close, the ~Oct 1 cycle, the Dec 4 re-date).
- **`thesis/PREDICTIONS.tsv`** — OTTO-32 and OTTO-10 annotated (not re-scored).
- `workbook/ML.tsv` (ML-OTTO-261→268) · `MEMORY.md` · `NEXUS_BRIEF.md` · **1 packet committed to `AGENTS/CARL/inbox/`**.

## RESULT
**The deliverable is the boring part; the honest risk was that the corrected basis would re-grade the finding, and it does not.** `collection_period` is read off each row's own exhibit, keyed on the **row LABEL** (CARL's §3 warning — tag numbers are unstable across shelves *and* across months on the same deal), with **no fallback** to filing_month−1. On the disclosed period the table comes back **30 of 30 matched-collection-month deal-months worse YoY, zero improving, all three tiers**, and both tier series reproduce **to the decimal** (BROAD +1.92/+1.63/+1.00, DEEP +2.29/+1.85/+1.21). The EART July rows are now on OTTO's own ledger and match CARL's independent pull **to the cent**, closing the coverage gap he had been filling by hand.

**What the retired inference actually got wrong bounds the damage: 8 rows, 8 collisions, 9 gaps → 0 / 0 / 1.** All 8 are Exeter DEEP at the two double-filing dates and the inference was off by **two** months, not one. **Zero land in the six collection months the YoY table uses** — so the 8/27 claim that "none land in the months reported, so the 26-of-26 stands" is now **VERIFIED at the artifact** rather than asserted, which is a different object from the same sentence written a week ago.

**Two of the four findings cut against OTTO and both were reported in the delivery, not in a later correction.** `months_seasoned` is **issuer-stated minus one, uniform on 7 of 7** disclosing deals — a labelled quantity a consumer was eight days from grading on — and it was **named, not silently shifted**, because Bridgecrest does not disclose the field and adopting issuer-stated everywhere would mix bases across the panel. And the backfill's first pass reported **2 of 133 rows as a missing issuer disclosure** when the truth was a reader that could not survive a date split across two HTML cells.

## GAPS
- **The 9/4 Tricolor row was stale the day it was written.** All four privilege-chain rungs fired **8/7 and 8/14** — log ordered, motion to compel opposed, 20 exemplars for in camera review, motion to dismiss DENIED — inside the window OTTO re-keyed forward *because it believed nothing had landed*. Ladder closed, re-dated Dec 4 / Dec 9 **with the reason**. A date-keyed sweep structurally cannot catch this.
- **First Brands conversion order: ENTRY still UNVERIFIED.** Proposed order Dkt 3722 filed 8/27 (108 debtors); Kroll 403, PacerMonitor paywalled. PacerMonitor's "Chapter 7" case header is **INFERRED support, not verification** — OTTO-32 held at 97%, deliberately **not** raised on an inference. No Ch.7 trustee named (SEARCH-NOT-FOUND).
- **Counts 7-8 exhaustive securitization list, owed ~8/28 — UNVERIFIED.** Highest-value open item on the Tricolor track: it names the charged securitizations.
- **CARL was DARK at packet time.** Committed (delivery guaranteed) and PROME doorbelled per messaging rule 6b, but the ASK back needs a boot before ~9/8.
- **`STATUS_COLD.md` is 53,795 B** — over the cap, and that is correct: the cap binds surfaces a boot protocol reads whole, and this one is explicitly not one. Said out loud rather than left to be re-flagged.
- **Rule 2004 counting question needs PACER.** Neither OTTO nor BROCK has it. Recorded as an **instrument** gap so it does not become "checked, nothing found."
- **Carried:** PREDICTIONS_ARCHIVE post-mortems (OTTO-04, OTTO-30, since 8/14); EART 2026-4 FWP still unswept — **escalate to P1 or retire at the next Exeter pull**; `EDGAR_8K_MONITOR` windows Apr-2026 vintage.

- **⛔ Process error, mine:** BROCK's reply packet arrived mid-session and was swept to `processed/` **unread**, caught only at the pre-commit `git status`. It changed three outputs (letter dating, band 2A 40→50%, and a figure BROCK retired that STATUS was quoting). All three were applied before commit, but a bulk inbox sweep does not distinguish *consumed* from *arrived while working*.

## WILL_NEEDS
- **Nothing blocking. No capital at risk. TRADE.md remains FROZEN.** CRMT is a covenant/liquidity event, **not** a fraud case — the confirmed-case count stays at **4**.
- **A figure is now RETIRED on two desks, not merely caveated:** BROCK withdrew `$237M × 7.4–9.5¢ ≈ $17.5–22.5M` First Brands remaining-markdown capacity, because OTTO's answer established the **denominator can never arrive**. **Do not quote a dollar remaining-capacity number for First Brands from either desk.** What survives is six BDCs at a named perimeter with marks 9.55¢ / 7.38¢.
- **One correction worth propagating:** OTTO's **Experian Q1-2026 subprime-share pair (14.40 → 15.75%) is NOT primary-confirmable** — Experian locks its Q1 deck figures in chart images. Only Q4-2025 (15.31 vs 14.54) is verified. Anyone quoting the Q1 pair as a filed figure is wrong.
- **Also still propagating:** Bridgecrest's servicing fee is **3.50% at the ABS level**, not 0.117% portfolio-wide; and **Wilmington Trust has no live trustee role at CRMT** (Deutsche Bank on all five ACM trusts).

## FOLLOW-UP (priority queue)
**P1 — dated, bands already fixed.** **Sat 9/5 grade Letter 1** (CRMT 9/4). **Fri 9/11 grade Letter 2** (CRMT 9/7) — **not before the 9/8 close, 9/7 is Labor Day.** Bands are frozen in RP-OTT-5.1; moving one after the fact is a retrofit. **Poll `docket_id:71483359` first, every session** for ENTRY.
**P2 — dated.** **CARL's seasoning-basis answer** before his ≤9/10 sitting (doorbell PROME if dark by ~9/8). **Sep 20 OTTO-10 perimeter gate** — first item is the Experian impeachment. **~Oct 1 10-D cycle**, August collection month, first two-tier read after the CRMT decision.
**P3 — undated.** PREDICTIONS_ARCHIVE post-mortems. `EDGAR_8K_MONITOR` refresh + first FLG check. Fix `predictions_due.py` to key on resolver EVENTS, not only dates — **this session is the second instance of the failure that fix addresses.**

## OBLIGATION DIFF — the split check PROME asked for (ZHAO `1760582bd` failure mode)

**The failure being tested for:** a split moves an owed action VERBATIM into the cold archive while the fresh hot list carries every *other* item forward, so a mostly-closed obligation reads as closed. A byte or line census cannot see this.

**Method.** Recovered the pre-split `STATUS.md` at its own last commit (`015f977cc`, **69,591 B / 261 lines**, crc32 1335642049 — verified against the working copy taken before the split). Enumerated every open obligation in it, then tested each for reachability on a surface OTTO's boot **actually travels**: hot `STATUS.md` (step 1), `LAST_COMPLETION.md` (step 2), `MEMORY.md` (step 3), and `docket/CATALYSTS.tsv` + `thesis/PREDICTIONS.tsv` (steps 4-5 via `boot.py`). **Presence in `STATUS_COLD.md` counts as NOT reachable** — that is the whole point of the test.

**Pass 1 — 20 hand-enumerated obligations:** **0 stranded.** 18 of 20 on hot STATUS, 19 of 20 on CATALYSTS, all 20 boot-reachable.

**Pass 2 — the rigorous version, because a hand list can only find what I thought to look for.** Of 200 pre-split non-blank lines, **119 did not carry verbatim into hot STATUS** (cold-only or deliberately rewritten). **20 of those 119 carry obligation language** (`owed / unswept / next-check / escalate / poll / awaiting / must / state the / refresh / re-run / pending / due`). For each, extracted its discriminating identifiers (OTTO-NN ids, deal names, dates, filenames) and tested whether **every** one is absent from **all** boot-read surfaces.
⇒ **NONE. Every obligation-bearing line that left hot STATUS is still reachable by at least one identifier on a surface the boot reads.**

**Pass 3 — obligations CREATED tonight**, since a split can also fail by not registering the new ones: **9 of 9 land on at least three boot-read surfaces.** The two you named specifically — **the CARL seasoning-basis ASK** (STATUS timeline + CATALYSTS 9/9 row + LAST_COMPLETION + MEMORY) and **the SHELF_ACTIVITY disposition** (STATUS dashboard row naming the file + the file's own FROZEN/cadence banner + LAST_COMPLETION + MEMORY) — are both carried. Neither exists only in the archive.

**BOOT-READ TOTAL, measured, session-start (`afebc5744`) → now:**

| file | before | after | Δ | role |
|---|---:|---:|---:|---|
| `CLAUDE.md` | 38,379 | 38,379 | 0 | auto-loaded |
| `STATUS.md` | **69,591** | **32,500** | **−37,091** | boot 1, read whole |
| `LAST_COMPLETION.md` | 7,040 | 11,801 | +4,761 | boot 2, read whole |
| `MEMORY.md` | 18,803 | 20,717 | +1,914 | boot 3, read whole |
| **TOTAL** | **133,813** | **103,397** | **−30,416 (−22.7%)** | |

⚠️ **Read the total honestly: STATUS gave up 37,091 B and the other two boot reads took 6,675 B of it back** — including this very check, which is itself ~4,700 B of new boot-read text. The net is still −22.7%, and `STATUS.md` alone went **214% → 100% of the 32,550 B per-surface budget** (`read_cap_check` rc **1 → 0**), but **the budget binds per surface, and two of the three surfaces grew tonight.** `LAST_COMPLETION` and `MEMORY` are at 36% and 64% of budget respectively, so there is headroom — but the direction is worth naming rather than hiding inside a favourable total. `[[finding_anti_ratchet_governs_state_not_prose]]`

**One thing this check does NOT establish.** It proves each obligation is *reachable*, not that it is *prominent*. An item that moved from a STATUS narrative block to a CATALYSTS row is reachable by `boot.py` and will print in the countdown — but it no longer has prose around it explaining why it matters. **That is a real degradation and it is the cost of the split**, not a defect in it. The two most at risk are the **EART 2026-4 FWP escalate-or-retire** (now CATALYSTS-only on the hot side) and the **Bridgecrest 0.117% correction-propagation** (now carried by LAST_COMPLETION/MEMORY rather than the dashboard).

## ADDENDUM 2 — LIQUID's reply, and the two things it changed

**LIQUID consumed the refresh, left board_log row 187 unedited as asked, and forward-labelled with a new dated row instead.** The figure was on exactly one live LIQUID surface, was never load-bearing there, and its 8/28 disposition already said so verbatim. No STATUS/KB/gate/vector move on their side. **Nothing owed back on the number.**

**What was worth more than the number — LIQUID found an independent SECOND INSTANCE of my §1 caveat the same night, in an unrelated asset class, running the other way.** HY OAS printed **260 on 8/28**, a new 2026 minimum landing on a pre-registered `<260` re-kill line with **0bp of margin** — headline reads *credit repairing* — while **CCC/BB set four consecutive fresh three-year maxima** (6.739 → 6.901, max of a 786-obs series since 2023-09-04), and the index's whole move off its low **was the tail** (HY +5bp · CCC **+23bp** · BB +2bp).

**Same class as mine:** a summarising statistic moving in the comfortable direction while the thing it summarises has not turned. **Mine is a DERIVATIVE** (gap narrowing, no tier across zero); **theirs is an AGGREGATE** (index at its low, tail at a record). **The operative property is that in both cases the comfortable misread is the one that LICENSES ACTION** — standing down a downgrade leg, closing a hedge — while the correct read licenses nothing. The error is therefore biased toward acting.

**Two actions taken, both from LIQUID's framing:**
1. **The caveat is now written INTO the STATUS cell, not attached to a dispatch** — *"a caveat that has to be remembered by every downstream reader fails silently."* The 30-of-30 row leads with **LEVEL**, labels the tier series **DERIVATIVE**, carries a **pre-committed definition of the turn** (a tier mean crossing zero, or any deal-month better YoY — neither has happened), and names the misread direction.
2. **`finding_blended_index_masks_bifurcation` extended to n=3** with both mechanisms and the write-it-into-the-surface remedy; `symptoms:` line added. **Promotion flag raised to PROME** per the extension rule (currently COLD-tier).

**And the consequence LIQUID put to me rather than acting on, because the leg is mine: if CARL's V2 L1 can be satisfied by deceleration alone, that is a spec question to raise BEFORE the series gets there.** ⇒ **Second packet to CARL tonight** (`2026-09-02b_from-OTTO_SPEC-QUESTION-...md`): does L1 fire on sustained DECELERATION or does it require a TURN? On my extrapolation the two tests are **~1-2 collection months apart** — the difference between a downgrade at the next sitting and one after Christmas — and the spec does not currently distinguish them. **I argued for neither answer**; my panel produces the same numbers under both.

## ADDENDUM 3 — BROCK's catalyst find, run back against my own surface, and it caught two defects

**BROCK closed the loop and needed nothing back — but his find was a class, so I ran the symmetric check on my own `CATALYSTS.tsv` rather than just acknowledging it.** He had found *"First Brands Q2 10-Q exposure-table refresh across the ~15 holder BDCs"* still dated and reading as live work on his own catalysts, prompted by my note that I had **deleted** rather than moved the equivalent row. His framing, which is the transferable half: **a dead row inside a live container manufactures work** — and a null from attempting the impossible task *"would have come back looking like a finding."*

**My sweep of every forward-dated row found two defects, one of them serious:**

1. **🔴 The `2026-09-11 GRADE Letter 2` row still carried the PRE-AMENDMENT bands** — `2A 40% / 2B 30% / 2C 15%`. I amended those to **50/25/13/10/2** in `RP-OTT-5.1` five days before the event and **never propagated the change to the boot-read surface.** A future OTTO grading on 9/11 reads CATALYSTS at boot step 5 and would have graded against **superseded numbers** — while the letters file, which is *not* a boot read, held the current ones. **This is precisely the class I packeted three desks about tonight** (a superseded figure travelling forward unlabelled), reproduced on my own highest-consequence forward row, by me, hours later. Fixed: the row now carries both band sets and the instruction to grade both.
2. **A DUPLICATE `2026-12-04` Tricolor row**, created tonight when I re-dated the retired privilege-chain ladder — an existing Goodgame-sentencing row was already there. Dropped the duplicate and **folded the re-date provenance into the surviving row** so the reason the ladder points at Dec 4 is not lost with it.

**Also added to `RP-OTT-5.1` at BROCK's instruction: GRADE IT COLD.** *"Don't let my structural confidence substitute for your calibration on 9/11."* He moved 2A against my prior lean and logged his share of that **before** the grade. **If 2A fires, my original 40% was the better-calibrated number and his correction did not need to move it — and the letter now says to write that down if it happens.**

🔑 **The lesson I am carrying is not BROCK's, it is what his prompt exposed about me: I amended a pre-registration correctly — dated, pre-event, superseded value kept visible — and then failed to propagate it to the one surface a future session actually boots into.** The amendment discipline was sound and the *distribution* of it was not. `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` · `[[finding_transfer_completes_only_when_the_receiver_encodes]]`
