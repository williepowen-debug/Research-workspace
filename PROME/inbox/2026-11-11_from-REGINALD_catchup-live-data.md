# REGINALD → PROME: 11/11 catch-up wake, live data and inbox drained (prome-2b)

**Answering:** PROME prome-2b task of 2026-11-11, on Will's 09:24 ET word ("Lets make sure we get all our agents caught up to the live data and news"). Runtime: Claude Code, Opus 5.5. Research only: no trade, card, gate, band, threshold or charter change; no spend; no external send. Commits `32a42bff7d` (records) and `cb1c820db5` (NEXUS brief); not yet pushed (push rides closeout).

## What changed in my read since my last session (11/08; the 11/09 entry was a machine-switch closeout only)

1. **Preferred Bank's late loans aged instead of curing, and my own forecast lost.** Its Q3 10-Q, filed with the FDIC on 11/09, shows **$150.2M of commercial real-estate loans 60–89 days late against $29.8M 30–59 days late** at 9/30 (6/30: $80.5M against $10.1M). Real-estate loans on the watch grade ("special mention") rose to **$148.4M** from $19.6M at year-end. I had put 40% on exactly this (REG-31); it resolved TRUE. The filing does not say which loans these are or whether any cured after 9/30, so the key questions stay open. Preferred is outside my 14 and outside Will's book. If those loans are still late at 12/31, they show as bad loans on the year-end Call Report (late January).
2. **Rates jumped, and regional bank stocks did not treat it as bank stress.** From 11/05 to 11/10 the 2-year went **4.46% → 4.73%** and the 10-year **4.84% → 4.98%** (Treasury, verified). On my October fit, a 14bp rise in the 10-year means about −1.0% for the regional-bank ETF (KRE); KRE instead rose **1.1%** ($72.31 → $73.09). Four sessions, weak fit: no conclusion beyond "not priced as stress yet."
3. **What a hiking Fed does here, in one line:** it moves the risk on my names from deposits to loans. Bond losses cut book value but, for most of my 14, not regulatory capital; funding costs rise most at banks living on brokered and wholesale money (Valley); funding plumbing is calm today. The channel that matters is commercial real estate that must refinance at maturity: Trepp's apartment special servicing hit 9.22% in October on maturity defaults (HOMER), EGBN has about $525M of loans maturing 11/30 to 12/30, and Preferred's late bucket sits in the same kind of book. That shows up in Q4 results and year-end Call Reports, not in daily prices.
4. **High-yield spreads came back in:** 348 [11/05] → 342 → 334 [11/09]. The 350 trigger never fired.
5. **The breadth test I named is still waiting on the FDIC:** the 9/30 bank-by-bank data had **0 rows at 09:52 ET** (6/30 has 4,313); expected about 11/19 (ESTIMATE). Until it posts, my "concentrated, with a weak BROADER qualifier" read stands unchanged.

No score, threshold, gate, band or judgment change. **Will decision required: none.**

> **For routing (your call, since this wake returns one packet):** under Will's 11/10 always-look-for-the-trade rule, item 1 together with HOMER's maturity-default item is material enough for a TERRY tradeability read. My 11/05 record says Preferred's options are not tradeable for Will, so a "no card" on the name is the likely answer; any cohort-level expression is TERRY's to judge. REGINALD sent no TERRY packet.

## Row-by-row (dated as shown; settled closes only, 11/11 bars excluded)

| Row key | Figure | Basis |
|---|---|---|
| `workbook/PREDICTIONS.tsv` · REG-31 | **RESOLVED TRUE 2026-11-11**: a = $150,223K (60–89), b = $29,832K (30–59), Real estate mortgage / Commercial [9/30]; forecast 40% | PFBC Q3 10-Q, FDIC FLNG cert 33539 filing 12041, aging table p.16, PRIMARY |
| `workbook/KB.tsv` · ML-REG-294 | PFBC: RE special mention $148.4M; nonaccrual held for investment $103.2M + held for sale $56.6M; NPAs 2.27% of assets; Q3 net charge-offs 0.00%; $56.6M mixed-use not sold by 9/30; named relationship $51.8M unchanged. `combo:late-loans-outside-14` | same 10-Q, PRIMARY; "mostly multifamily" is INFERRED from my 9/30 Call Report pull |
| `registry/REG_T02_EXIT_LOG.tsv` · 2026-11-09, 2026-11-10 | WAL **$77.20, $76.30**; REG-T-02 FIRED, exit **0 of 3**, 50 rows; needs +7.34% to $81.90 | Yahoo + Nasdaq agree (`scripts/settled_bars.py` rc 0, 09:50 ET) |
| STATUS §THRESHOLD · KRE (`REG-T-01`) | **$73.45 [11/09], $73.09 [11/10]**; UN-FIRED, $13.09 above $60; shares 54.80M, −1.2% vs 11/08 | same; KRE float script |
| STATUS §THRESHOLD · HY OAS (`REG-T-03`, `REG-T-04`, REG-34) | **342 [11/06], 334 [11/09]**; REG-T-03 FIRED stays (exit run 0); **REG-T-04 NOT FIRED**, run 0 of 3; 11/11 holiday bar excluded, run bridged | FRED `BAMLH0A0HYM2`, own fetch 09:51 ET |
| STATUS §THRESHOLD · CCC/HY (`VX-REG-18.04`) | **3.85× [11/06], 3.93× [11/09]**; rise is HY tightening faster, NO escalate; B 350 [11/09], above the 330 watch line | FRED CCC, B, BB OAS |
| STATUS §THRESHOLD · 10Y / 30Y / 2Y | **4.98 / 5.35 / 4.73 [11/10]**; 4.88 / 5.26 / 4.56 [11/09]; bond market closed 11/11 | Treasury par-curve CSV, PRIMARY (matches your context) |
| STATUS §THRESHOLD · Funding plumbing (`REG-T-08`) | SOFR−IORB **−2bp [11/09]**, −1 [11/06]; RRP $0.152B [11/10]; primary credit $9.219B [11/04] | FRED; next H.4.1 Thu 11/12, H.8 Fri 11/13 |
| STATUS §THRESHOLD · VIX | 19.46 [11/10], 19.92 [11/09] | FRED VIXCLS |
| `VX-REG-6.03` FLG ladder | last settled **$10.51 [11/10]**, −26.2% vs frozen $14.24; RED, 24 closes below $11.39 | `vx_ladder_check.py` |
| Market quotes (your context check) | OZK **$50.77**, WAL $76.30, KRE $73.09 [11/10] agree with your figures | settled bars, two routes for WAL/KRE |
| DOCKET L180 / CALENDAR 11/07 row (FDIC breadth counts) | FDIC 9/30 universe **0 rows [11/11 09:52 ET]**; Friedberg and reserve-release counts (d)(e)(f) UNKNOWN; ~11/19 ESTIMATE | `api.fdic.gov/banks/financials` |
| DOCKET L514 / REG-03 (QBP Q3) | no FDIC date found; Q3 2025 printed 11/24/2025, so ~late Nov ESTIMATE | one web search, 11/11 |
| **DOCKET L798** (vendor-risk guidance, shared with GIBBS) | Comments close **Mon 11/16**. Nothing owed before the close; I will not file a comment (no external send). After 11/16 I read the posted comments for bank statements of core-vendor dependence and any agentic-AI access statement. Docket number not found in one search | Skadden via CLS Blue Sky 10/05; DEWEY 10/22 output |
| `workbook/KB.tsv` · ML-REG-295 | Trepp bank multifamily criticized rate, Q2: Phoenix 38.6%, Houston 35.5%, Dallas 35.3%, national 22.5% (your HOMER relay); lead only, not tied to any of my 14 | SECONDARY (TreppTalk 11/05) |
| `workbook/KB.tsv` · ML-REG-296 | NEXUS PRED-38 miss: no US bank disclosed ≥$100M Q3 charge-offs on non-bank finance borrowers; counterevidence on `bank-lending-to-private-credit` | NEXUS 5fbaf8fc83 via WALTER |
| `board/BOARD_LOG.tsv` · SIG-W-20261109-012, 20261110-002, 20261110-005 | INFO_ONLY, INFO_ONLY, INTEGRATED (PRED-38 line); WALTER inbox 0 open | cards read whole |
| `inbox/processed/` · GIBBS 11/08 | Its ask (does my cohort criticized line have a Q3 direction?) answered **NO** (split by name); no reply per its "reply only if yes" rule | — |
| `board/BOARD_LOG.tsv` · SIG-W-20261106-044 | own-record correction: printf-mangled note restored | — |
| Insider (SEC Form 4, 11/10) | EGBN: one director bought 1,470 sh at $33.91, another sold 16,669 sh at $33.63–$33.87; net selling, small; no record change | insider script |

**Not obtained:** cohort securities-duration / AOCI dollar sensitivity (not measured); December FOMC pricing at a primary (cmegroup.com blocks this box; the "above one full move" figure stays secondary); WAL Q3 Basel III disclosure (WAL desk's). **Unverified relays used only as context:** HOMER's Trepp figures and CBS pricing.

Report: `AGENTS/REGINALD/reports/2026-11-11_catchup/REPORT.md`.

## COMPLETION — REGINALD — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/REGINALD/{STATUS.md, CALENDAR.md, MEMORY.md, ROADMAP.md, NEXUS_BRIEF.md, reports/2026-11-11_catchup/REPORT.md, registry/REG_T02_EXIT_LOG.tsv, workbook/{PREDICTIONS,KB}.tsv, board/BOARD_LOG.tsv, archive/{STATUS,MEMORY}_rotation_2026-11-11.md, scripts/.kre_float_state.json, inbox/processed (1), inbox/WALTER/processed (3)}; this packet
RESULT: 4 inbox items drained (every sender). REG-31 RESOLVED TRUE (PFBC 60–89 $150.2M vs 30–59 $29.8M [9/30]); WAL/KRE graded through 11/10 (exit 0-of-3, 50 rows); HY 334 [11/09], REG-T-04 not fired. Hike read: CRE refinancing is the channel, funding calm. FDIC 9/30 still 0 rows.
GAPS: FDIC 9/30 universe unposted (expected ~11/19), so breadth counts stay UNKNOWN; L798 comment file only readable after the 11/16 close; FOMC pricing not verified at a primary (CME blocks this box).
WILL_NEEDS: None.
FOLLOW-UP: PROME decides the TERRY route above. REGINALD reads H.4.1 11/12, H.8 and FHLB CFR (REG-T-06 grade) 11/13, L798 comments after 11/16, FDIC counts when posted. Window held open for closeout.
