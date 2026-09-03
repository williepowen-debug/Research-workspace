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
