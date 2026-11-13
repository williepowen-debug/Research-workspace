# ISHM due-row session — 2026-11-13

**Assignment:** PROME prome-72 due-row wake (WQ-184, WQ-667 B); PROME's words, not Will's. Runtime: Claude Code, Opus 5.5 (claude-opus-5-5). Started 10:17 ET Friday 2026-11-13 by the system clock.
**Boot:** `boot.py` rc 1 (three due rows, one past-due; the AAR-BREADTH row-47 date note and unscored VX-ISH-08 are the known carries); corrections check rc 0; FRED current on all 7 series.
**Rules applied:** graded only by the desk's own written rules; no level, band, threshold, score or trade changed.

## Row results

| Row key (docket/CATALYSTS.tsv) | Result | Basis |
|---|---|---|
| `2026-11-13 [CASS-SHIP] Cass Freight Index, Oct 2026` | **NOT PUBLISHED, nothing graded.** Re-dated to Monday 2026-11-16 (desk recheck date, not an issuer date) | At 10:17 and 10:19 ET: `cass-transportation-indexes/october-2026` HTTP 404 (`sources/cass_october-2026_404_at_1017ET.html`); index page's newest report September; historical XLSX `Last-Modified: Mon, 12 Oct 2026 20:39:21 GMT` (`sources/xlsx_headers.txt`), newest row September 1.062; FRED FRGSHPUSM649NCIS newest September 1.062; trade-press search found no October 2026 figure. Issuer cadence is only "typically released on the 13th" (RULE-DERIVED). No PRINTS row written: an unpublished print gets no row |
| `2026-11-13 J2 base-rate sample: add matured months only` | **One matured window added; no new freight month.** Re-dated 2026-11-16 to add the October Cass month when it publishes | See § J2 below |
| `2026-11-12 Deere fiscal-Q 4 date check` (the past-due row) | **GRADED: date found at the issuer.** Re-dated to `2026-11-25 [EARNINGS] Deere fiscal Q4 2026 results`, P2, FIRM | Deere newsroom (deere.com/en/news/, HTTP 200, read 10:19 ET), notice dated November 11: "will hold its fourth-quarter 2026 earnings call on Wednesday, Nov. 25, beginning at 9 a.m. Central time" (10:00 ET). PRIMARY-VERIFIED. Results-document release time not stated in the notice. Excerpt: `sources/deere_q4_notice_excerpt.txt` |

## J2 — matured months only

Script: `j2_matured_update.py` (reads the frozen first-session `J2_monthly_sample.csv` unchanged; fills only windows that have completed). Outputs `J2_monthly_sample_2026-11-13.csv`, `J2_BASE_RATES_2026-11-13.json`. The first-session files are not modified.

| Item | Value |
|---|---|
| Fresh HY OAS pull (FRED BAMLH0A0HYM2, read 2026-11-13) | 2023-11-14 to 2026-11-12; matches the frozen October 23 snapshot on 772 overlapping days, max difference 0.00 |
| October 2026 HY monthly mean | 3.222% (22 trading days); September 2.755%, July 2.743% |
| Window matured | **July 2026** forward three months (Cass shipments −4.84% y/y, third consecutive negative month): **+47.9 bp** |
| Not entering any freight-down denominator | August (+2.06%) and September (+1.92%) are freight-up months |
| Not addable yet | October freight month (Cass unpublished); August/September forward windows mature only after November/December complete |

| Count (freight y/y < 0) | Before | After |
|---|---|---|
| Forward 3-month widening ≤ 0 bp | 19/32 | **19/33** |
| Forward ≤ 25 bp | 28/32 | **28/33** |
| Forward ≤ 50 bp | 30/32 | **31/33** |
| Trailing 3-month, all cuts | 18/30, 26/30, 28/30 | unchanged |

**Reading (descriptive, not a band or credit verdict):** the newest matured freight-down month is the fifth of 33 followed by more than 25 bp of widening. The order matters: Cass turned positive in August and September **before** October's widening, so this is not freight-led credit stress. It is still chiefly one freight episode, with endpoint overlap and no GFC/COVID, so no independent-cycle probability. LIQUID owns the spread read and RED the probability read; both packeted.

**J2 rail state unchanged:** the proposed (unregistered) deterioration test needs negative Cass y/y on two consecutive releases plus a negative four-week AAR comparison. September Cass +1.9% and positive October rail weeks: **NOT-MET**, and no October Cass to test.

## Inbox — every sender and lane

| Item | Disposition | Surface |
|---|---|---|
| `inbox/2026-11-12_from-DAEDALUS_WQ678-harness-lines.md` | INTEGRATE (STATUS record). Changelist A: none for ISHM. Changelist B (S-32..S-35, optional): **DECLINED this session.** PROME's assignment puts charters out of scope, and B is optional; carried to the next owner session that is not a fenced due-row wake. S-35 verified: `AGENTS/ISHM/registry/` does not exist (no receipt written yet) | STATUS § Completion |
| `inbox/WALTER/SIG-W-20261109-008.md` | LOG KB-ISH-065 (Union Pacific CEO rate threat, X relay). Pricing, not volume | board_log, KB |
| `inbox/WALTER/SIG-W-20261111-002.md` | LOG KB-ISH-064; combo:ai-supply-crowding (KB-ISH-057) member plus counterevidence | board_log, KB |

## Routing

- LIQUID, RED: J2 matured-window packet (P2, routing table "J2 result").
- TERRY: **no packet.** No material finding: Cass unpublished, Deere is a date, and the J2 change is one descriptive denominator. The HY widening itself is LIQUID's figure, not an ISHM finding.
- PROME: delivery packet `PROME/inbox/2026-11-13_from-ISHM_due-rows.md`.

## Process note

Four untracked 404/403 download stubs this session created in `sources/` were deleted with `rm`, not `trash` (root rule #11). They were never committed and held no content beyond error pages.
