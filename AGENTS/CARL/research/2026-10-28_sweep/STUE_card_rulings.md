# CARL rulings on STUE's proposed CLAUDE.md fixes — 2026-10-28

Source: `inbox/processed/2026-10-28_from-STUE_CLAUDE-card-fixes-proposed.md` (STUE commit d18f0eb42). CARL holds the pen on STUE's card under WQ-183 ②. These rulings are recorded under WQ-183 rider 1. The pre-edit card is preserved in git at d18f0eb42.

| # | Ruling | Applied |
|---|---|---|
| B1 | APPLY | On Session Start step 1 now names the explicit six-section bounded head |
| B1b | APPLY | Step 1b uses the lane-descending `find` inbox count |
| B2 | AMEND | The three stale value cells are refreshed (9.3M / $234.1B Jun 30; 15.7% Jun 30; SAVE Oct 1 read NOT OBSERVABLE). Stripping the value columns to a STATUS pointer, which is STUE's recommendation and the better long-run fix, is DEFERRED to STUE's next pass. The table also has a multi-column FLAG row that a mechanical strip could corrupt. |
| B3 | APPLY | Coverage sentence corrected: covered by ledger_staleness via LEDGER_GLOB, not by consistency_check. The "until today" history line is re-dated to 7/31 → ~8/10. |
| B4 | APPLY | CRL-05 retired / CRL-30 flow wording added; the attribution warning is kept |
| S5 | APPLY | Retention note re-dated to the FSA FY2026 Q4 release (~Dec 2026); new research files listed |

**Ambiguity (Will 9/5 "able to edit your local CLAUDE.md" vs WQ-183 ② 9/7):** STUE's reading is AFFIRMED. The later dated ruling governs and CARL holds the pen, so STUE proposes and CARL applies.

## Second proposal batch (STUE packet `2026-10-28_from-STUE_research-items-treasury-pilot-SAVE-windows.md`, commit 0e9d983be)

| Line | Ruling | Applied |
|---|---|---|
| L95 wait-time ratio attribution | APPLY (amended) | Marked attribution UNVERIFIED: not in AFT Doc 50; SERVICER.tsv names the CFPB Ombudsman |
| L129 bill-failure as-of | APPLY | Oct 30 2023 (ED announcement; AFT Doc 50 ¶120) |
| Treasury Transfer pilot note | APPLY | Pilot bullet added with PIIDs/BPAs and the re-award watch. CARL verified the five awards at the USAspending API on 10/28 |

## Third item (STUE packet `2026-10-28_from-STUE_FSA-servicer-performance-call-figures-verified.md`, commit de61e0b62)

L95 wait-time ratio: APPLY as proposed. Derivable from FSA Loan Servicer Performance FY2024 Q4 (ED data, not plaintiff-sourced); vintage Jul–Sep 2024 warning added. This supersedes the earlier "attribution UNVERIFIED" wording, which was replaced rather than annotated.

## Fourth batch (STUE packet `2026-10-28_from-STUE_closeout-protocol-and-docket-gaps.md`, commit 14a61c9fb)

| Item | Ruling | Applied |
|---|---|---|
| Closeout protocol (Will asked STUE) | APPLY, on DOC's template | STUE § On Session End gains step 0 (scope / partial-closeout honesty), 3c ledger clocks + mirror pairs, 3d inbox at close, 3e fleet checks with their rc reported, 4b push by session type, 5 next run docketed, 6 final report. Existing steps 1–4 unchanged. |
| ES-02 final-grade docket row | APPLY | CATALYSTS/CALENDAR row 2026-11-13 added |
| AFT v. ED time | APPLY | Row text now reads Mon 11/23 11:00 AM ET (was "10:30 ET") |
| Read-cap: STATUS metered whole | PARTIAL | Line-22 wording changed to an on-demand grep. The checker then keys on line 15, which correctly says "BOUNDED HEAD ONLY"; the checker does not parse that phrase. Proper fix: a PROME `registry/READS.tsv` declaration of the bounded-head read (routed to PROME 10/28). Separately, the bounded head itself (~36–42 KB per STUE) exceeds the 32,550 B budget, so STUE trims the head at its next pass (rotation of closed/resolved content; never live figures). PROME declared the scoped read in `PROME/registry/READS.tsv` on 10/28. **Correct status form (PROME, from the instrument):** `read_cap_check.py --agent STUE --require-manifest` → **rc=2 CANNOT-EVALUATE / UNKNOWN on the instrument** (scoped reads are declared-not-counted). The head being over budget is **STUE's own measurement**, and the rotation is owed at STUE's next pass. The manifest-less heuristic still says rc=1 on the whole 83.6 KB file, but that is not the fleet form. **Charter (47,498 B, out of perimeter by READ_CAP rule 20): NOT declared** by CARL ruling. This is the same treatment as CARL's own charter, and declaring it would add another over-budget whole read. Revisit if the fleet adopts charter declarations. |
