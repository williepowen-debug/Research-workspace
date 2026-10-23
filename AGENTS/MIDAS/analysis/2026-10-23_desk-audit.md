# MIDAS desk audit — stale, broken, owed, incomplete, missing (2026-10-23)

Will-directed sweep, started 16:00 ET (`date`). Read-only: nothing in this list was fixed by the sweep itself.

**Fix pass (Will: "Yes approved go ahead", 16:03 ET):** FIXED #11 (WQ-421 lines rewritten in STATUS/OPEN_ITEMS; NEXUS/SCRATCH copies archived), #12 (SCRATCH now one forward list), #13 (STATUS stale blocks rotated, scoring rows and top-3 rewritten), #14 (NEXUS_BRIEF older sections rotated, current state block added), #16 (SOURCES.md CFTC row and an access-facts table), #17 partially (OPEN_ITEMS stale lines replaced; sections otherwise kept), #19 (TLT82P removed from live surfaces), #26 (CLAUDE.md file table lists the tests), #27 (8 outbox files and the July report moved to `archive/`, index links fixed). Everything moved is verbatim in the `analysis/*_ARCHIVE_2026-10.md` files. **Still open:** #1–#10 (dated work and decisions), #15, #18, #20–#25. **Needs Will:** #20 (certified settlement source) and #6 (retire or register the M1 successor draft). Priority: **H** = blocks a grade or contradicts itself on a boot-read file · **M** = misleads a reader · **L** = housekeeping.

## Clean (checked, no finding)

0 broken relative links across all MIDAS markdown · every path named in CLAUDE.md exists · 42/42 tests pass · KB views current and every KB row has a source and an as-of date · ledger staleness OK (FLOW/KB/PREDICTIONS/VX) · read cap rc 0 · no unreceipted named corrections · inbox empty · COT legs current (10/20 consumed) · no predictions past due.

## Owed (dated, MIDAS's to do)

| # | P | Item | Due |
|---|---|---|---|
| 1 | H | Certified GCZ26 settle for 10/22 and 10/23 vs $4,050 (M1 flip rule UNRESOLVED; secondary $4,042.80 vs vendor $4,060.40) | Mon 10/26 |
| 2 | H | Nornickel 9M grade against the pre-registered lines (DOCKET L701) | Mon 10/26 |
| 3 | H | MIDAS-09/10 resolve on the 10/30 close (first retrieval 11/2, backstop 11/6); MIDAS-16 on the as-of 10/27 COT (~10/30) | 10/30 |
| 4 | M | MIDAS-14/15 (11/2 close) · L819 (11/06) · L820 SAFE (11/07) · L821 TIC (11/18) · MIDAS-11/13/17 (11/20) · L822 WGC (~12/04) · MIDAS-12 (2027-01-20) | calendar |
| 5 | H | Closeout: push the ~15 local commits (safe-push) and send the receipt PROME asked for | today |
| 6 | M | **M1 successor DRAFT** (`analysis/2026-10-12_M1-successor-DRAFT.md`): review was due 10/19, never done, still unregistered. Decide retire vs register; the WQ-451 instrument may supersede it | overdue |
| 7 | L | Resolved MIDAS-01..08 still in the live PREDICTIONS ledger; CLAUDE.md says resolved rows move to an archive with post-mortems. No archive file exists | — |
| 8 | L | DOCKET 2026-08-10 row (DFII10 8/7 print), owner MIDAS, still "SUPERSEDED · PENDING": ask PROME to close it | — |
| 9 | L | DOCKET L409 (9/30): every desk with a level threshold on a generic ticker. MIDAS repaired this on 10/12 (named contracts) but no by-name confirmation to PROME was found | — |
| 10 | M | Weekly contract-map review | next 10/30 |

## Stale

| # | P | Where | What |
|---|---|---|---|
| 11 | H | STATUS (3 places), OPEN_ITEMS (2), NEXUS_BRIEF (1), SCRATCH (2) | **WQ-421 still described as "OPEN, due October 29"** while other lines on the same files say APPROVED 10/15 and consumed 10/20: two live instructions on boot-read files |
| 12 | H | SCRATCH | **Two forward lists**: today's "Pick up here" and the older "One carry-forward list" (10/13). CLAUDE.md requires exactly one |
| 13 | M | STATUS | "Weekly review due October 19 remains outstanding" (done 10/23); top-3 items 1–3 dated 10/12; the 10/12 news section; the "Held GLD" section's 17-share beta arithmetic; mirrored TLT82P (expired 10/16) still mentioned |
| 14 | M | NEXUS_BRIEF (read whole by NEXUS) | Below today's block: October 9 prices (GCZ26 $4,216.30 …) and "17 GLD shares" read as current to a peer |
| 15 | M | THESIS I1/I2 and FLOW FL-MIDAS-03/04 | Still 10/12 evidence; today's PALL red crossing, PPLT orange, LME +47,525t (US tariff-arb), Teck strike notice and the Nornickel setup are not reflected |
| 16 | M | sources/SOURCES.md | Reviewed 10/12; says "October 6 vintage consumed" (now 10/20) and still records CFTC 403 (cleared today). **Missing today's access facts:** Treasury real/nominal par-curve CSV works (PRIMARY); CME settlements return "IP blocked"; SPDR archive serves an xlsx without an extension; Westmetall LME table |
| 17 | L | OPEN_ITEMS §20–28 | Dated 10/12; several partly closed (contract map done 10/23, CFTC access back) |
| 18 | L | TRADE.md | Body blocks from July–September (GLD 16 sh, MIDAS-06) are dated history under today's header; acceptable but long |
| 19 | L | References to TERRY's TLT82P (expired 10/16) | in STATUS, THESIS, OPEN_ITEMS, NEXUS_BRIEF, SCRATCH |

## Broken or structurally weak

| # | P | Item |
|---|---|---|
| 20 | H | **No certified settlement source.** CME blocks this box's IP; the $4,050 flip rule and any near-boundary futures grade require a certified settle. Needs a standing source: Will's broker statement, or approved CME data access. Until then near-boundary grades go UNRESOLVED |
| 21 | L | Boot can never read quiet: four vendor `=F` pointers sit on expiring months, so every boot says REVIEW even though those prices are excluded everywhere. Consider reclassifying to INFO (owner decision; touches `metals_watch.py`) |
| 22 | L | FRED DFII10 posts a day late; today's grade used the PRIMARY Treasury real curve. Worth naming as the default source for same-day grades |
| — | — | FORGE `fetch.py` rounds Close to 2dp (DOCKET 10/19, PROME owns the repair); MIDAS uses a local native-precision adapter. Not ours |

## Incomplete

| # | P | Item |
|---|---|---|
| 23 | M | Drafts: `2026-10-12_M1-successor-DRAFT.md` (see #6); `2026-08-28_row66-noverdict-band-DESIGN-DRAFT.md` (status not stated on its face; row66 NARROW is prospective-only per OPEN_ITEMS). The silver/PGM bands DRAFT is the adopted draft of record (fine) |
| 24 | M | Open evidence gaps: Section 232 critical-minerals status after ~July; silver lease rates; this week's global gold ETF flows; the primary Goldman CB note; India silver import tonnage; matched PGM stock/lease histories; China catalyst loadings; copper imports/lag; Platts sulfur quote |
| 25 | L | LESSONS: last entry L-53 (10/01). Candidates from today, not recorded: a media mechanism must be checked against the curve (the "hike bets" story vs a 2Y −16bp day); gold's stress-day behaviour measured, not assumed; a narrative clock can set a timer (now in fleet memory, not in desk lessons) |
| 26 | L | CLAUDE.md FILES table omits the three test files (`test_metals_watch_inputs.py`, `test_metal_kbs.py`, `test_boot_cot_metals.py`) |

## Retirement candidates (root Data Hygiene: older than 60 days, not boot-read, no live reference)

| # | P | Files |
|---|---|---|
| 27 | L | `outbox/` 8 files dated 7/17–8/23 (0 live references) → `git mv` to `archive/`; `reports/2026-07-12_domain-sweep.md` (index references only) |
