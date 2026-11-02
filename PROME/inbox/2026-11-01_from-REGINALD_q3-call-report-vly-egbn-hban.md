# REGINALD → PROME: Q3 Call Report read: VLY, EGBN, HBAN, Friedberg plan (WQ-587)

**Date:** 2026-11-01, 23:16–23:30 ET (`date`). **Spawn:** PROME C9 commission (WQ-587), one bounded session, $0. **Runtime:** Claude Code, model Opus 5.5 (claude-opus-5-5), session id UNKNOWN (not exposed), repo `/home/willi/Research-workspace`, branch master. Tools used: Bash, WebSearch, SendMessage. **Boot reads (bounded reader, all to `eof: true`):** root `CLAUDE.md` 5 pages · `AGENTS.md` 1 · `USER.md` 2 · `AGENTS/REGINALD/CLAUDE.md` 5. Then STATUS, LESSONS, CALENDAR, MEMORY, ROADMAP, BANK_RESEARCH_STANDARD read whole.
**Full report:** `AGENTS/REGINALD/reports/2026-11-01_Q3-call-report_VLY-EGBN-HBAN/REPORT.md` (+ `primary-rows.tsv`, `retrieval.tsv`). Basis: bank-level FFIEC Call Report, my own pull 11/01 23:18 ET with the renewed token; all nine SDFs hash-identical to WALTER's, so the source is the same and the arithmetic is mine.

## Findings
| Item | Result |
|---|---|
| WALTER's VLY figures | VERIFIED: nonaccrual $462.629M → $511.390M; Q3 NCO $37.078M; equity +0.30%; deposits +1.96%. Q2 NCO is $22.046M (WALTER printed 22.045, a $1K difference; the bank's release prints 22,046). |
| VLY drivers | Nonaccrual +$48.8M = construction +$30.1M (one loan) + an $18.5M loan to a nondepository financial institution (NDFI; RC-N Memo 9, from $0) − NOO CRE −$7.0M. The rise in net charge-offs (+$15.0M) is multifamily +$11.1M and C&I +$7.1M. |
| VLY allowance | Did not keep pace: loan allowance −$9.8M ($590.1M → $580.3M); allowance ÷ nonaccrual 127.55% → 113.47% (bank level). By category, CRE −$15.5M and construction −$4.1M, commercial +$12.8M. Q3 provision $27.3M was below NCO of $37.1M. |
| VLY release vs filing | Agrees on amounts. The release's "higher non-accrual C&I" is, on the Call Report, the $18.5M NDFI loan: the issuer's C&I line = Call Report C&I + all other loans + leases, to the dollar. BROCK packeted. |
| L521 (MF 30–59 cohort) | Mostly MODIFIED, not paid: MF 30–89 $101.5M → $21.7M while MF performing modifications to borrowers in difficulty rose +$73.5M (INFERRED from category totals). New NOO CRE 30–89 $0 → $61.4M. Six asks for the 10-Q (~11/6–11/9) are in report §1d. |
| EGBN | VERIFIED: $136.915M → $179.722M (+31.27%); coverage 88.48% → 67.20%. Driver: multifamily nonaccrual +$46.6M (11.9% of the MF book), consistent with the $56.0M Prince George's loan (L791; RED owns the tree). Q3 NCO $4.2M with zero MF charge-off vs Q2 $47.9M: two separate clocks. Parent-vs-bank nonaccrual gap ($111.1M/$166.0M vs $136.9M/$179.7M) unreconciled. |
| HBAN M3 | STEP-CANDIDATE on the existing detector as written: +28.6% with loans +0.9%. Unfunded M3 commitments rose too (funded + unfunded +23.7%, method from FLG's packet), so new commitments look likelier than a relabel (INFERRED). A prompt to look at the 11/07 run, not a finding. |
| My instrument defect | The detector rounds to one decimal before testing "> 25", so it missed EGBN at 6/30/2026 (−25.02%). Fix at the 11/07 roll, with a boundary fixture; not changed tonight. |
| Friedberg "95 of 4,295" | Primary statement SEARCH-NOT-FOUND (three web searches; in the repo it first appears 10/13 as a quote pasted in chat). 4,295 ≈ the FDIC-insured Call Report population (INFERRED). Four candidate measures, each with a like-for-like universe count, are written into the 11/07 plan (report §4; CALENDAR 11/07 row). The 14-bank samples cannot settle it: a random 14 would show zero hits 73% of the time at a 2.2% base rate. |

**Thesis meaning, one line per held name (context only; TERRY constructs, Will approves):** VLY: the bank-specific early flag holds, not escalated (problem loans up, reserves released, modifications instead of cash; realized loss still small). ZION/OZK/WAL/KRE: not re-verified here; the "concentrated, not tier-wide" claim is unchanged. FLG: FLG desk's read, consumed (its packet e9f170314), not duplicated.
**No score, threshold, gate or prediction move.** REG-30's Q3 baseline equals the Call Report; evidence points both ways; probability unchanged.

## Inbox drain (whole inbox, every sender; BOARD_LOG rows, `consume:REGINALD` commits)
11 items: 9 WALTER (-026 and -009 INTEGRATED; -007, -010, -011, -018, -023, -024, -025 INFO_ONLY), PROME FFIEC-token packet INTEGRATED (JWT expiry refreshed on every live surface: STATUS, CALENDAR, charter, LESSONS, BANK_EXPOSURE_MATRIX, FHLB README), FLG packet (arrived after launch; doorbelled by PROME) INTEGRATED. Inbox now empty.

## Skipped controls (named)
Boot step 7 (prices, vx_ladder, boot.py), 7a ledger staleness, and the WAL/OZK channel ACKs: SKIPPED, outside this commission. The NEXUS brief fold was SKIPPED on purpose: thesis state is unchanged. `read_cap_check` rc 1 (over_budget=1) is pre-existing; MEMORY records it as a DAEDALUS tool item. Consumer check: two kinds of old JWT-date references remain by design. Dated reports and the writer-emitted TSV headers (re-emitted at the next run) were left as history.

## COMPLETION — REGINALD — 2026-11-01
STATUS: ✅ DONE
CHANGED: AGENTS/REGINALD/reports/2026-11-01_Q3-call-report_VLY-EGBN-HBAN/{REPORT.md,primary-rows.tsv,retrieval.tsv}, STATUS.md, CALENDAR.md, MEMORY.md, ROADMAP.md, CLAUDE.md, LESSONS.md, BANK_EXPOSURE_MATRIX.md, research/FHLB/README.md, workbook/KB.tsv, board/BOARD_LOG.tsv, 11 inbox files → processed/, AGENTS/BROCK/inbox/2026-11-01_to-BROCK_vly-q3-ndfi-nonaccrual-under-issuer-c-and-i-label.md
RESULT: WALTER's VLY/EGBN/HBAN Call Report figures verified at the primary (one $1K arithmetic difference). VLY nonaccrual +$48.8M = construction +$30.1M + NDFI +$18.5M, with allowance −$9.8M (coverage 127.55% → 113.47%) and the MF cohort mostly modified. EGBN MF nonaccrual +$46.6M (coverage 67.20%). HBAN M3 +28.6% = STEP-CANDIDATE. Friedberg test written for 11/07. 11 inbox items drained.
GAPS: Friedberg primary not found (pasted in chat 10/13, never committed). EGBN parent-vs-bank nonaccrual gap unreconciled. Step-detector rounding fix deferred to the 11/07 roll. Universe for the Friedberg test depends on the FFIEC/FDIC 9/30 posting.
WILL_NEEDS: Optional: the original link or clip of the Friedberg "95 of 4,295" claim, if he has it. Desktop .env still needs the new token at the next machine switch.
FOLLOW-UP: VLY 10-Q (~11/6–11/9): six asks in report §1d. 11/07 run: Friedberg universe counts, detector fix, HBAN 10-Q look.
