# BOND -> PROME: catch-up delivery under Will's 09:42 ET word, 2026-11-05

**ACTION for PROME:** close L859; re-date L226 to 11/13 or return it; land the R3 set below; commission the L859 independent read. Nothing here needs a ruling from Will.

## Rows

| Row | State | What |
|---|---|---|
| L859 | ✅ DONE 11/2, before your list | Bars frozen 11/2 for 3Y 11/9, 10Y 11/10, 30Y 11/12: `AGENTS/BOND/registry/auction_bars/2026-11-09_91282CRW3.json`, `2026-11-10_91282CRX1.json`, `2026-11-12_912810UY2.json`; commit ceea78c6a, KB-BND-522. CUSIPs appeared 11/2, ahead of the row's 11/4 assumption. BOND sent no packet then, which is why the row still read PENDING. Downgrade graded today: auction health 4→3, KB-BND-531. WQ-536 not reopened. |
| L406 | ✅ CURRENT | 11/4 10–20Y read routed to RED, seventh of seven OFF-THE-RUN (0.22%). sb0607 window ended 11/4, so the carrier now runs Treasury's eight long-end ops 11/17→2/9/2027. Metric, 50% cut and verdict logic unchanged; selftest 0 failures. ⚠️ Those ops are outside sb0607's original window: whether FT-11 v1.1 reads them is RED's call, flagged in its packet. |
| L226 | ⛔ NOT DONE, dependency unmet | The base rate needs the FHLB Combined Financial Report. REGINALD's calendar (`AGENTS/REGINALD/CALENDAR.md` line 62) dates it Fri 11/13, not Mon 11/9; Preliminary Highlights $798.4B [9/30] do not complete it. Not verified at the issuer: two guessed Office of Finance URLs returned 404. Setting the number would also be a level change, outside this packet's limits. ASK: re-date L226 to 11/13 and say who rules the number. BOND's mirror is re-dated. |
| L565 R3 | ✅ ANSWERED below | |
| Inbox | ✅ 8 of 8 | Your seven: five INFO noted at boot; two ACTION assessed, CCC KB-BND-534, Holy Redeemer KB-BND-535. One new card, flag 4. |
| BOND docket | ✅ CURRENT | Blind span verified at Treasury's XML through December; February QRA, 7Y conversion and an 11/19 bar-freeze row added. |

## R3 WATCH_FOR verdicts, by name (WALTER packet 2026-10-01)

| Phrase | Verdict |
|---|---|
| `term premium` | Rejection ADOPTED. Replace with `Treasury term premium`, `term premium yields`, `term premium bond` |
| `real yields` | Rejection ADOPTED. Replace with `TIPS yield` |
| `basis trade` | Rejection ADOPTED. Replace with `hedge funds basis trade` |
| `Treasury auction` | Rejection ADOPTED. Replace with `Treasury note auction` |
| `swap spreads` | KEEP as-is. ⚠️ Recall unproven; singular `swap spread` stays rejected |
| Pulled-deal query | DECLINED as written: US HY recall unproven, returned only non-USD pulls |

## What changed for the record

- **QRA (`sb0678`, read at Treasury):** every coupon size unchanged Nov–Jan. F1 and F3 NOT FIRED, sb0607 reading stands (KB-BND-528). ⚠️ F1 has no number; a reader using the $38B→$70B headline as the size test would disagree. ⚠️ The dated-window ground for rejecting YCC weakened.
- **Guidance (KB-BND-529):** August "at least the next several quarters", November "the next several quarters". TBAC: increases warranted later in FY27, likely second half, mostly 2Y–10Y.
- **WQ-592:** you left Treasury's statement to BOND's record. It confirms TERRY's read: 10Y $42B and 30Y $25B equal August. The decline holds.
- **Composite 17/35** (was 18). THESIS v1.2.13. Token moved on all surfaces.
- **For LIQUID, from Treasury:** TGA $850B end-December, peak up to $1.025T ± $50B. Recorded by BOND only.

## Flags

1. **VX-BND-07 reading, stated before the cell:** HY held the 338–363 band 10/30–11/3, VIX under 20 on one session. VIX 16.61 [11/4, FRED]. If the HY 11/4 cell is ≥338, BOND reads the upgrade as met; the letter does not say consecutive. Score only, 2→3, no capital consequence.
2. **Independent read owed:** L859's note says an independent reader is owed on the `ta_ws_schema` repair and that you commission at BOND's next wake. I found no record it ran (DOCKET, your inbox, CATO's SCRATCH, commit subjects). The 11/9 registered grades run through that code. Its selftest passes; that is not an independent read.
3. **Clean check:** `closeout_check` returns rc=1 on 4 date-pattern hits, all correctly labelled dated data; 3 clear when FR2004 as-of 10/28 lands.

4. **New card after your list: WALTER SIG-W-20261105-001 (BoE +25bp to 4.00%, 8–1).** Read: long-end reaction muted on intraday reads, gilt 30Y +1bp and US 30Y flat, no closes yet; HANS owns the grade (KB-BND-537). The card's phrase "time-critical gilt limit" names nothing I can find in BOND's records; ASK WALTER what it refers to if it is an obligation.
5. **Consumer scan on 18/35:** 22 hits, none BOND's: ISHM's own composite or dated records. No packets owed.

## COMPLETION — BOND — 2026-11-05
STATUS: ⚠️ PARTIAL
CHANGED: AGENTS/BOND STATUS, SCRATCH, RECEIPT, NEXUS_BRIEF, TRADE, thesis/THESIS.md, thesis/CHANGELOG.md, workbook KB and VX, docket, monitors/buyback_f2.py, monitors/WATCH_DATES.tsv, registry/f2_reads.tsv, board_log.tsv, analysis/2026-11-05_catchup/; AGENTS/RED/inbox F2 packet.
RESULT: QRA graded with F1 and F3 NOT FIRED; auction health 4→3 and composite 17/35; 8 of 8 WALTER cards consumed; KB-BND-527 to 537 added.
GAPS: L226 waits on the 11/13 report. FR2004 as-of 10/28, PMMS 11/5 and HY 11/4 were unpublished at writing. EA AAA leg of dm_cross_section returned HTTP 504 twice. Not closed out, per your packet.
WILL_NEEDS: None.
FOLLOW-UP: BOND refreshes those three cells today and addends only if a score moves.
