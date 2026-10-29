# DEWEY -> PROME: L800 base-cell replay (figures CONFIRMED, wording corrected) + whole-inbox drain
**Date:** 2026-10-29 10:12 ET | **Row:** D:L800 · REQ-DEWEY-20261022-005 | **Spawned by:** prome-90 (Tier 1, Will's "can we fix these 3 things now?")
**Runtime:** Claude Code, model claude-opus-5-5, session 80ec96b9 (PROME cwd). **Boot reads, all carried to eof:true with `boot_read.py`:** root CLAUDE.md 4 pages · AGENTS.md 1 · USER.md 2 · AGENTS/DEWEY/CLAUDE.md 7.

## Task 1: replay of VULCAN's two cells

**Outcome (a): no figure moves; the method description was wrong.** VULCAN's arithmetic on the inputs Table 1 *displays* is correct (MSFT -19.8 / -44.4, GOOGL -42.0). The 2026E cells were never built from those inputs. The 10/22 calc script was recovered from the 10/22 DEWEY session transcript (`~/.claude/projects/...AGENTS-DEWEY/6ad84bf0.../subagents/agent-ac065...jsonl`, line 303); the 10/22 scratchpad had died. It is now saved as `AGENTS/DEWEY/research/2026-10-29_L800-replay/replay.py`, and it reproduces all five 2026E cells and the sum to the $M.

| Cell | Netting that produces it ($B) |
|---|---|
| MSFT headline -26.8 | calendar-2026 OCF 193.6 (102.1 filed Jan-Jun 2026 + 2 x TTM/4) - 175.0 (CY2026 guide, counts finance leases at signing; Hood call 2026-07-29) - 0 FL principal - 45.4 payouts (22.7 filed + 2 x Q4-FY26 rate) |
| MSFT cash -5.8 | 193.6 - 150.4 (175.0 - 24.6 FY26 FL ROU additions) - 3.6 FL principal - 45.4 |
| GOOGL -34.4 | 177.7 (84.9 filed H1-26 + 2 x TTM/4) - 200.0 guide mid - 1.5 FL principal - 10.6 dividends (buybacks zero since Q4-25) |

- **Inputs re-verified [PRIMARY]:** MSFT against the saved 10/28 XBRL (FY26 10-K acc 0001193125-26-323660). GOOGL against new saved XBRL packets (Q2-26 10-Q acc 0001652044-26-000071) plus the 10-Q face for H1 dividends of 5,231.
- **Downstream:** the -186.5 sum is CONFIRMED (-186,456 $M), as is -165.4 with MSFT on cash basis. The 2027E floors are unchanged. The ORCL cell and the Oracle weak-link framing are unchanged.
- **The defects were wording:** "OCF flat at TTM" (true only for 2027E); payout run-rate unstated; MSFT row is calendar 2026, not FY; the header formula subtracts FL principal, which MSFT's headline correctly does not.
- **Where it is recorded:** a dated erratum in the report itself (pointer under the Key Finding plus a full § "2026-10-29 replay" after the method notes; the 10/22 text is kept as written) and in INDEX.tsv (DEWEY's only ledger/KB).
- **Packet:** `AGENTS/VULCAN/inbox/2026-10-29_from-DEWEY_L800-base-cells-replayed.md`. No corrected total exists to send, because none changed.
- **Flagged, not computed:** GOOGL's 6.25% mandatory convertible preferred dividend (quarterly from 8/15/2026, cash or shares) is missing from the H2 run-rate. The 2026E vintage is pre-Q3; VULCAN's 10/29 re-cut is the current figure.

## Task 2: whole-inbox drain (7 top-level + WALTER lane), logged to `board_log.tsv`, filed to `processed/`

| Packet | Disposition |
|---|---|
| VULCAN L800 replay | acted (above) |
| PROME nano-banc relative pointers | acted: 4 pointer lines qualified (nano 344/538/539, meta-review 102; line 4 already qualified); targets verified present |
| MARCO DR-1 adopted | integrated: impact backfilled to the INDEX row |
| PROME CARL-DR-1 card leg (10/01) | noted and filed: SYF Q3 delivered 10/25, BFH Q3 10/28; **COF Q3 still owed by 11/13 under DOCKET L567** |
| CARL x2 (10/12) | noted and filed: limits and the counterfactual ASK carry into the COF Q3 leg |
| OTTO CourtListener token | noted only (WQ-531, Will's hands). The fail-loud-401 and RSS-mode tool asks are unbuilt and carried |
| WALTER/README.md | lane README, not a REQ; stays. 0 REQs queued |

Census after: top-level 0 · WALTER/ 1 (README).

```
STATUS: ✅ DONE
CHANGED: AGENTS/DEWEY/output/2026-10-22_hyperscaler-ai-funding-gap-ig-capacity.md, output/INDEX.tsv, output/2026-09-27_nano-banc-primary-documents.md, output/2026-10-23_dewey-research-history-meta-review.md, board_log.tsv, research/2026-10-29_L800-replay/replay.py, research/edgar_xbrl/2026-10-29_0001652044_* (4 packets), inbox/ -> processed/ (7), AGENTS/VULCAN/inbox/2026-10-29_from-DEWEY_L800-base-cells-replayed.md, this memo
RESULT: D:L800 / REQ-DEWEY-20261022-005: MSFT -26.8/-5.8 and GOOGL -34.4 reproduce exactly from the recovered 10/22 script (CY2026 filed YTD + run-rate, not the displayed TTM inputs); all five cells and the -186.5 sum CONFIRMED; method wording corrected by a dated erratum (10/22 text kept); VULCAN packeted. Inbox drained 7/7 to processed/, logged.
GAPS: GOOGL preferred-dividend omission flagged, not sized (no new figure in scope). COF Q3 card leg owed by 11/13 (L567). recap_pull fail-loud/RSS changes unbuilt.
WILL_NEEDS: None new (CourtListener token stays WQ-531).
FOLLOW-UP: VULCAN: cite the corrected method wording; DEWEY: COF Q3 FDM leg when filed (L567, by 11/13).
```
