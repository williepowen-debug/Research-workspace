# VULCAN -> PROME: L800 hyperscaler funding-gap re-cut at the Q3 prints (D:L800)

**Date:** 2026-10-29 (from 09:01:08 ET, `date`) · **Spawn:** prome-90, WQ-184 Tier-1 due-row wake · **Runtime:** Claude Code, Opus 5.5
**Key:** D:L800 · L782 table updated · L811 Oracle cell below
**Report:** `AGENTS/VULCAN/reports/2026-10-29_L800_funding-gap-Q3-prints.md` [KB-VULCAN-318..325]
**Boot reads (bounded reader, all to eof:true):** root CLAUDE.md 4 pages · AGENTS.md 1 · USER.md 2 · AGENTS/VULCAN/CLAUDE.md 6. boot.py rc0 (leg 8 META 10-Q model FAIL carried, pre-existing).

## Result

| Company | New primary | 2026E gap: DEWEY → VULCAN (USD B) | Capex change and class |
|---|---|---|---|
| MSFT | 8-K Ex 99.1 + 10-Q (10/28); preliminary 424B2 acc 0001193125-26-437008 (10/29 11:33 ET) | −26.8 → **−26.1 headline**; −5.8 → **−1.5 cash basis** (Q1 gap **+6.5**) | ≈ $175B → ≈ $170B, **SUPPLY-TIMING** (delayed third-party capacity), still up YoY ⚠️ period FY vs CY conflicted in secondaries |
| GOOGL | 8-K Ex 99.1 (10/28) + 10-Q acc 0001652044-26-000084 (10/29) | −34.4 → **−31.6** (−41.7 on 9M actual + Q4 run-rate); Q3 gap **−12.0** | none ($195–205B held) |
| META | no print (Q3 was **10/21**, not 10/28); equity 424B5s 10/28 | −15.3 unchanged | none; **$37.5B equity-linked priced** (first common raise) |
| AMZN | **PENDING** after the close 10/29 | −69.5 (DEWEY) stands | — |
| ORCL | Investor Day 8-K 7.01 (10/28) | FY27 −40.5 unchanged | FY29 step-down is a **plan**; market raises capped |
| Tesla (outside gate) | KB-263 | — | ≈ $20B from > $25B = **DEMAND-SIDE / discretionary, not funding-forced (INFERRED)**; the row's "−$20B" is the new level, the cut is ≈ −$5B+ |

- **Five-name sum ≈ −$183.0B mixed basis** (DEWEY −$186.5B); ≈ −$158.4B with MSFT on cash basis.
- **No funding-forced capex cut.** All five payers now raise outside money: Microsoft's first USD bond in years launched today (size blank; ≥ $25B reported, T2).
- **L782 table:** ranks unchanged. Mechanism changes: Oracle's risk moves from bond buyers to vendors, customers and prepayments; Alphabet's own 10-Q shows **$48.0B** of data-center credit backstops (≈ $80.8B contingent notional with guarantees and the JV), which ties the payer tier to the developer tier.
- **Composite 15/25 and S5 4 (n=2) UNCHANGED.** Nothing forced a change: no YoY capex cut, no flex, no PULLED deal.
- ⚠️ **DEWEY's MSFT and GOOGL base cells do not replay on DEWEY's stated method.** MSFT gives −19.8 / −44.4, not −5.8 / −26.8. DEWEY has a packet; VULCAN quotes its own replayable figures and the like-for-like change.

## L811 cell — Oracle credit / Ellison web

At Oracle's 10/28 Investor Day (8-K 7.01, acc 0001193125-26-435853), Oracle capped further capital-markets raises at **$20B through FY30** ($10B equity and $10B gross debt, refinancing excluded). That is on top of the $20B Q1 ATM. It guided **positive FCF in 2H FY28** and **≥ $30B FCF in FY29**, put investment-grade ratings first, and set a net debt / adj. EBITDA target **< 3.5× in FY29**, with vendor financing and leases counted in net debt. ORCL closed **$144.54, +10.73%** on 10/28 (fetch.py, read 10/29 09:04 ET, prior close). On the credit side this is a plan, not cash. Against DEWEY's FY27 gap of about −$40.5B and an FY28 floor of about −$51.8B, the cap implies roughly **$50B+** over FY27–FY28 must come from vendor financing, customer-provided hardware, prepayments and cash (INFERRED, VULCAN arithmetic). That leans harder on suppliers and a few large customers, the OpenAI-centred concentration the Ellison web maps. **Not refreshed by VULCAN:** ORCL CDS, Paramount legacy CDS, SKYD, EDGAR CIK 0002041610. Those stay with PROME's L811.

## Drain

- **Count:** 2 top-level packets (DEWEY MSFT XBRL packets, now KB-318; ZHAO truce instrument, now KB-325) and 18 WALTER cards. Dispositions: 7 acted, 1 noted, 5 info-only, 5 skipped. Each is logged in `board_log.tsv` with source INBOX_WALTER, and all 20 were moved with `git mv` to their processed/ directories.
- **CATALYSTS:** the 10/26 and 10/27 rows were swept by row. The cluster, EXIT-rewrite and S2 hynix/Samsung rows are re-dated to 10/29 and are still **owed** after the AMZN and Samsung prints.

## Commits

| sha | What |
|---|---|
| d0a2554ed | research, STATUS, KB, board_log, drain |
| ce120e169 | DEWEY packet |

Continuity and this memo are in the closeout commit named in the SendMessage. **Not pushed** (spawn prompt; push delegated to PROME).

## COMPLETION — VULCAN — 2026-10-29
STATUS: ✅ DONE
CHANGED: AGENTS/VULCAN/{reports/2026-10-29_L800_funding-gap-Q3-prints.md, STATUS.md, SCRATCH.md, NEXUS_BRIEF.md, LESSONS.md, board_log.tsv, docket/CATALYSTS.tsv, archive/CATALYSTS_FIRED_2026-10.tsv, workbook/KB_GENERAL.tsv, workbook/KB.tsv, inbox moves ×20}; AGENTS/DEWEY/inbox/2026-10-29_from-VULCAN_L800-base-arithmetic-does-not-replay.md; this memo
RESULT: L800 re-cut. MSFT FY27E −1.5 cash / −26.1 headline, with its first USD bond in years launched 10/29. GOOGL 2026E −31.6, Q3 gap −12.0, backstops $48.0B. META $37.5B equity-linked priced. ORCL capped market raises at $20B. Sum ≈ −183.0 mixed basis. No funding-forced cut; ≈ $5B MSFT trim is supply-timing. Composite 15/25 and S5 4 unchanged. Drain 2+18 done. L811 Oracle cell is in the memo.
GAPS: AMZN and AAPL pending tonight. MSFT capex period (FY vs CY) and bond size are T2/unpriced. Official transcripts not read. No CDS refresh. The DEWEY base cells do not replay. The §4b cluster grade, EXIT rewrite and S2 grade are owed after the 10/29 prints.
WILL_NEEDS: None
FOLLOW-UP: Re-spawn VULCAN after the AMZN and Samsung prints, for the cluster §4b grade, EXIT rewrite, S2 grade and AMZN row, plus the MSFT bond pricing flex check. DEWEY should answer the replay packet.
