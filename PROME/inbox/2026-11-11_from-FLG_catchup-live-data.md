# FLG → PROME: 11/11 catch-up wake, live data and inbox drained (prome-2b)

**Answering:** PROME prome-2b task of 2026-11-11, on Will's 09:24 ET word ("Lets make sure we get all our agents caught up to the live data and news"). Runtime: Claude Code, model Opus 5.5 (`claude-opus-5-5`); session ID not exposed beyond the harness scratchpad UUID `b2f519e1…`; worktree = the shared checkout, master. Tools used: Bash, FFIEC CDR (own credentials), Treasury CSV, `fetch.py`, one web search ×2, one web-fetch helper. Research only: no trade, card, gate, band, threshold or charter change; no spend; no external send. Commits `fa9e28efe4` (records) and `37970789e7` (NEXUS brief); not pushed (push rides closeout).

## What changed in my read since my last session (11/07)

**Nothing graded moved, and this week's news does not change the read.** The bear case on Flagstar is still a thin specific reserve ($155M, 5.5% of a $2.8B non-accrual book) leaning on a refinance market the bank does not control.

1. **The Q3 Call Report is the same filing I graded on 11/01.** Re-pulled from the FFIEC this morning: byte-identical, no amendment. The row's 11/14 date was the rule-of-thumb estimate; Flagstar filed on 10/30. Concentration (SR 07-1) stays **322.11%** of total risk-based capital at 9/30.
2. **A December hike barely touches Flagstar's income or its regulatory capital.** This comes from the bank's own Q3 10-Q tables. A 100bp rise in short rates adds **0.68%** to next-year net interest income, so 25bp is roughly +$3M a year (my scaling). Bond losses sit in accumulated other comprehensive loss, **−$839M at 9/30**, which is outside regulatory capital. I derived that from the Q3 capital bridge; it was not stated as a policy. So a hike does not push the concentration ratio up through capital. It costs book value: the bank's economic value of equity falls 4.0% per +100bp.
3. **Where the hike does matter is refinancing, and that leans bearish, but it is inferred and nothing grades it.** Apartment and commercial-property loans refinance off the 5- to 10-year Treasury plus a spread, not the Fed funds rate. At the 11/10 close the 5-year was **4.81%** and the 10-year **4.98%**: 28–31bp below the 9/30 quarter-end, but 50–57bp above July 1. A hiking Fed means no rate relief is coming for the **$12B of loans with coupons under 3.9% resetting through 2027**. In Q3 the payoff exit channel slowed to $76M, its lowest since Q2-2024.
4. **Peer stress is in the same channel but in different books.** HOMER's Trepp figure (apartment special servicing 9.22% in October, driven by maturities) and REGINALD's Preferred Bank aging are logged as context. National CMBS loans and LA/DC regional banks are not NYC rent-stabilized bank loans, so no Flagstar figure moves.
5. **Rent-freeze lawsuit: the docket read is closed.** Per Will's 11/10 drop, docket entries after 253 are recorded NOT OBTAINED. The emergency-relief and merits risks are now unreadable from this system. Today's check of reachable sources (press and the Fordham decisions catalog) found no ruling; the judge's end-of-year marker stands.

**Will decision required: none.** **TERRY:** no new material finding. The hike read is inferred and ungraded, so I sent no TERRY packet. If PROME routes the HOMER/REGINALD maturity-default item to TERRY, FLG's input is KB-FLG-116.

## Row-by-row (dated as shown)

| Row key | Figure | Basis |
|---|---|---|
| **DOCKET L52** (D:L52) / `workbook/TRIGGERS.tsv` T-01 | Q3 Call Report **POSTED 10/30, GRADED 11/01** (KB-FLG-099). Re-pulled 11/11 10:13 ET: sha256 `8cf81ff12e2b…` identical, last-update 20261030, **no amendment**. SR 07-1 322.11% = 31,580,906 / 9,804,386 $K. **Answer for L52's date: nothing left to grade on 11/14; the next print is the Q4 Call Report, T-01 2027-02-14.** The SCOPE CHECKPOINT grade stays PROME/Will's (inputs: `reports/2026-11-07_Q3-2026_10Q_LEG.md` §9) | FFIEC CDR RSSD 694904, PRIMARY · `KB.tsv` KB-FLG-114 |
| `workbook/KB.tsv` KB-FLG-115 | NII: +0.68% per +100bp short; −0.26% per −100bp short; parallel +1.5% / +2.7% (+100/+200). EVE −4.0% / −8.2%. AOCI −$839M [9/30] (−$489M [12/31/25]), outside CET1 (DERIVED: Q3 OCI −$292.0M vs CET1 −$224.0M) | 10-Q acc 0000910073-26-000084, PRIMARY |
| `workbook/KB.tsv` KB-FLG-116 | 5Y 4.24 → 5.09 → **4.81**; 10Y 4.48 → 5.29 → **4.98**; 2Y 4.17 → 4.88 → **4.73** [7/1 → 9/30 → 11/10]. 12/9 FOMC +25bp 85.5% (your ORACLE relay, unverified by FLG). Consequence INFERRED; **no FLG letter keys on a rate level** (BOND's call) | Treasury par CSV, PRIMARY |
| `workbook/EXIT_PROTOCOL.md` K-1 / K-2 / K-4 | K-1 **0 of 2**, not fired; K-2, K-4 untouched; K-3 UNSET. Nothing this week reaches a kill leg (all grade on filings) | own rail, unchanged 11/07 |
| `workbook/PREDICTIONS.tsv` FLG-01 | **OPEN**, Resolve_By 2027-03-15, 50%; FLG-02/03 HIT 11/07. No touch this week | — |
| `workbook/KB.tsv` KB-FLG-117 | Trepp MF special servicing 9.22% Oct (HOMER relay); PFBC CRE 60–89 $150.2M vs 30–59 $29.8M [9/30] (REGINALD). **Logged, not scored** (WQ-622) | MIRROR, relays |
| `workbook/TRIGGERS.tsv` T-07 · VX-REG-6.03 | FLG **$10.45** intraday 11/11 (`fetch.py`, −0.52%); settled **$10.51** [11/10]; RED is REGINALD's row; T-07 unchanged | `fetch.py`; REGINALD `vx_ladder_check` |
| `workbook/TRIGGERS.tsv` T-12 · `KB.tsv` KB-FLG-118 · CALENDAR · THESIS · STATUS · NEXUS_BRIEF | **WQ-477 recorded:** index 453580/2026 doc 244 and every entry after doc 253 = **NOT OBTAINED, DROPPED BY WILL 2026-11-10**; risks (a) emergency relief and (b) merits = **UNREADABLE from this system**; ask not carried, not re-raised. Reachable sources 11/11: no ruling (Fordham 2415 = 8/21 venue order; 2497 = 9/16 discovery order, merits reserved). Next_Check stays **2026-12-31** | PROME packet 11/10 → `inbox/processed/` |
| `inbox/` | **1 of 1 drained** (PROME 11/10, INTEGRATE); WALTER sub-inbox empty; corrections check rc 0 | `boot.py` rc 1 → cleared |

⚠️ **Open discrepancy, no letter depends on it:** the Fordham catalog dates the Richmond venue order 8/21, while FLG's 10/21 correction treated 8/21 as the return date of the order to show cause. The catalog entry is a summary and the PDF was not opened.

**Not obtained:** FOMC pricing at a primary (relay only); Trepp at its primary; any November Flagstar news (one search, none found).

## COMPLETION — FLG — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/FLG/{STATUS.md, CALENDAR.md, THESIS.md, NEXUS_BRIEF.md, workbook/KB.tsv (KB-FLG-114..118), workbook/TRIGGERS.tsv (T-01, T-12 notes), sources/ffiec_2026-11-11/, inbox/processed/ (1)}; this packet
RESULT: Q3 Call Report re-pulled and unamended (SR 07-1 322.11%), so D:L52 has nothing left to grade. A hike barely moves NII (+0.68% per +100bp short rates) and does not reach regulatory capital; it bears on refinancing (5Y 4.81 / 10Y 4.98), inferred and ungraded. WQ-477 drop recorded on 6 surfaces. 0 letters moved.
GAPS: FOMC odds and Trepp unverified at primary (relays); rent-freeze docket unreadable by Will's ruling.
WILL_NEEDS: None.
FOLLOW-UP: None new. Next prints: Q4 Call Report 2027-02-14, FY2026 10-K ~2027-03-01; T-12 check 2026-12-31. Window held open for closeout.
