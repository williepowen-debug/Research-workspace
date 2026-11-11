# REGINALD catch-up, Wed 2026-11-11 (PROME prome-2b, on Will's 09:24 ET word)

**Session:** reginald, Claude Code, Opus 5.5, booted 09:49 ET. Research only: no trade, card, gate, band, threshold or charter change; no spend; no external send. Prior session: 11/09 09:31 ET machine-switch closeout (`4ebbb4b148`); last working session 11/07–11/08.

## 0. What changed in my read since 11/08

1. **Preferred Bank's late loans got older, not newer, and my REG-31 forecast resolved TRUE against my own 40%.** The Q3 10-Q (FDIC FLNG 12041, filed 11/09, read 11/11) shows commercial real-estate loans **60–89 days late $150.2M against $29.8M 30–59 days late** [9/30]; at 6/30 it was $80.5M against $10.1M. Real-estate special mention is **$148.4M** [9/30] against $19.6M [12/31/25]. The 10-Q does not say which loans, whether they matured, or whether they cured after quarter end, so CATO's questions stay UNRESOLVED. Outside my 14 and outside Will's book.
2. **Rates rose and regional banks did not trade it as bank stress.** 2-year **4.46% → 4.73%** and 10-year **4.84% → 4.98%** from 11/05 to 11/10 (Treasury par curve). My 57-day fit (10/23) says +14bp on the 10-year is about −1.0% on KRE; KRE went **$72.31 → $73.09 (+1.1%)**. Funding plumbing is calm. The hike mostly works on my names through CRE refinancing at maturity, which shows up in quarters, not days (§2).
3. **High-yield spreads came back in.** HY OAS **348 [11/05] → 342 [11/06] → 334 [11/09]**; REG-T-04 never fired (run 0 of 3).
4. **Nothing moved on the bank-wide breadth question.** The FDIC's 9/30 bank universe is still not posted (**0 rows, 09:52 ET**), so the Friedberg and reserve-release counts stay UNKNOWN; the 11/07 BROADER-but-weak qualifier stands.

No score, threshold, gate, band or judgment change. One prediction resolved (REG-31 TRUE).

## 1. Grades on my own letters (settled bars only; 11/11 bars not settled)

| Row key | Letter | Reading | Grade |
|---|---|---|---|
| `REG-T-02` (WAL <$78; exit ≥$81.90 ×3) | exit run | **$77.20 [11/09], $76.30 [11/10]**, Yahoo and Nasdaq agree (`scripts/settled_bars.py`, rc 0, 09:50 ET) | FIRED stays; exit **0 of 3**; log now **50 rows**; needs +7.34% from $76.30. 11/11 vendor $75.81, not graded |
| `REG-T-01` (KRE <$60) | level | **$73.45 [11/09], $73.09 [11/10]**, both routes agree | UN-FIRED, $13.09 above |
| `REG-T-03` (HY >320; exit ≤300 ×5) | exit run | **342 [11/06], 334 [11/09]** (FRED `BAMLH0A0HYM2`, own fetch 09:51 ET); 11/10 not yet published | FIRED stays; exit run 0 |
| `REG-T-04` (HY >350 ×3) | fire run | 342, 334 | **NOT FIRED**, run 0 of 3; cycle peak stays 348 [11/05]. 11/11 Veterans Day bar, when it appears, is a forward-fill: excluded, run bridged (`registry/NOTES.md` line 183) |
| `REG-34` (HY >350 ×3 by 12/31, 25%) | — | as above | OPEN |
| `VX-REG-18.04` CCC/HY >3.6× | ratio | **3.85× [11/06]** (1,317/342), **3.93× [11/09]** (1,311/334) | HARD-FIRE continues; HY fell 8bp, CCC 6bp: the ratio rose because HY tightened faster, **NO escalate** |
| B-tier OAS (ORANGE >330 watch row) | level | 361 [11/06], **350 [11/09]**; BB 208, 200 | still above 330; no trigger |
| `REG-T-08` (SOFR−IORB >+15 ×3) | spread | **−1bp [11/06]** (3.89−3.90), **−2bp [11/09]** (3.88−3.90) | NOT FIRED |
| `VX-REG-6.03` FLG ladder | state machine | last settled **$10.51 [11/10]** = −26.2% vs frozen $14.24; **24** settled closes below RED $11.39 since 10/7 | RED, unchanged (`vx_ladder_check.py`) |
| `REG-31` (PFBC 60–89 ≥ 30–59 + $5,000K, 40%) | MECE on the filed table | **a = 150,223, b = 29,832 ($K)**, row Real estate mortgage / Commercial, 9/30/26 (10-Q p.16 aging table) | **RESOLVED TRUE** (a ≥ b + 5,000). Forecast 40%: my reason for under 50% (new late loans usually start in 30–59) was wrong for this quarter |
| `REG-T-07` office CMBS DQ | — | 12.33% [Oct] unchanged; next Trepp print ~early Dec | not touched |
| `REG-T-06` FHLB | — | grades Fri 11/13 from the CFR | not touched |

## 2. What a hiking Fed does to my lane (working model, not a forecast)

**Measured this session.** Treasury par curve (home.treasury.gov CSV, read 09:51 ET): 11/05 → 11/10, 3-month 4.17 → 4.30, 1-year 4.28 → 4.56, **2-year 4.46 → 4.73**, **10-year 4.84 → 4.98**, 30-year 5.25 → 5.35; 2s10s 38bp → 25bp. IORB 3.90 (FRED). The 3-month bill sits 40bp above IORB, which is consistent with a hike being priced; December pricing: first written here as unverified (cmegroup.com blocks this box); **verified at closeout by ORACLE's 11/11 read** (KB-ORC-133, `PROME/inbox/processed/2026-11-11_from-ORACLE_catchup-read.md`): 12/9 FOMC on Polymarket hold 3.5 · +25 85.5 · +50 or more 11.8; Kalshi hold 3 · +25 85 · +50 11; futures about +28.9bp. Priced odds are ORACLE's figures, cited, not re-derived.

| Channel | What a hike does | What I can see today | Read |
|---|---|---|---|
| **Securities marks** | Higher 1–5 year yields deepen unrealized losses on available-for-sale bonds; they cut tangible book value through AOCI | SBCF lost ~$1.63 of TBV/share to AOCI in Q3 (STATUS). For the Category IV and smaller names in my 14, AOCI is still outside regulatory capital (AOCI-inclusion rule is a proposal with a phase-in to 2032; no final rule seen 11/05) | Book-value and deal-math pain, **not a capital-ratio trigger**. No cohort dollar estimate this session: securities duration not measured |
| **Funding cost** | Deposit and wholesale costs re-price up with a lag | SOFR−IORB −2bp [11/09]; RRP $0.152B [11/10]; discount-window primary credit $9.219B [11/04]; small-bank borrowings $309.7B [w/e 10/28]. Next: H.4.1 Thu 11/12, H.8 Fri 11/13, FHLB CFR 11/13 | Plumbing calm; the cost bites hardest at wholesale-funded names (VLY: 97% loan-to-deposit, $5.3B brokered, KB ML-REG-188/189). A margin squeeze, not a run signal |
| **CRE refinancing** | Floating-rate and maturing loans re-price; more borrowers fail to refinance, extend or default | HOMER: Trepp multifamily special servicing **9.22% [Oct], +69bp, on maturity defaults** (TreppTalk 11/09). My named walls: EGBN Q4 ~$525M (11/30: $88.5M + $53.0M construction; 12/21 $56.0M; 12/23 $94.0M + $88.1M). PFBC 60–89 $150.2M [9/30] | **The live channel for my thesis.** It moves recognition, which prints at Q4 releases (late Jan) and the 12/31 Call Reports, not in daily prices |
| **Equity tape** | Regional banks have traded the 10-year: −0.72% KRE per +10bp (57-day fit, R² 0.13, `reports/2026-10-23_boot/REPORT.md` §4) | 11/05 → 11/10 KRE +1.08% against a fitted −1.0%; on 11/10 alone 10-year +10bp, KRE −0.49% (fit −0.72%). WAL +0.6%, OZK −0.6%, FLG −0.8%, VLY +1.8%, EGBN +1.3% | Four sessions: the hike is **not** being priced as bank stress. Weak fit; no conclusion beyond that |

**So what.** A hike moves the risk on my names from the deposit side to the loan side. The thing to watch is whether maturing CRE loans (EGBN 11/30 and 12/21–12/30, PFBC's 60–89 bucket, FLG's rent-regulated book) extend, cure or default into Q4. ⚠️ A falling 10-year remains the falsifier for any regional-bank put, and a hike that flattens the curve while the 10-year rises less than the 2-year helps that falsifier less than it looks.

## 3. FDIC Q3 count (the breadth test I named) and the QBP

- **FDIC 9/30 bank universe: NOT POSTED.** `api.fdic.gov/banks/financials` REPDTE 20260930 = **0 rows** [11/11 09:52 ET]; 6/30 = 4,313 rows. Q2 posted ~50 days after quarter end, so **~11/19 (ESTIMATE)**.
- When it posts: the four Friedberg measures ("95 of 4,295" like-for-like) and the reserve-release counts (d), (e), (f) per CALENDAR 11/07 row; plan `reports/2026-11-01_Q3-call-report_VLY-EGBN-HBAN/REPORT.md` §4. Until then the 11/07 L180 read stays **BROADER on the letter, weak, foreclosure limb only**, and the STATUS judgment keeps its qualifier.
- **QBP Q3:** no FDIC date found in one search (11/11); Q3 2025 printed 11/24/2025, so **~late Nov (ESTIMATE)**. It grades L514 (regional foreclosed CRE) and REG-03.

## 4. D:L798 — interagency third-party (vendor) risk guidance, comments close Mon 11/16 (shared with GIBBS)

- **State:** comment period open; closes Mon 2026-11-16 (Skadden via CLS Blue Sky, 10/05; proposal FRB/FDIC/NCUA/OCC, Federal Register 2026-09-15 per DEWEY's Mayer Brown cite). One search did not find the regulations.gov docket number.
- **My part:** read the comment file AFTER the close for bank-side statements of core-vendor dependence and any regulator statement on agentic-AI access (DOCKET L798 text). **I do not file a comment** (no external send). Nothing is owed before 11/16. Logs to the `bank-vendor-breaches` combination theme (KB ML-REG-286). GIBBS holds the large-bank half.
- **Next step:** after 11/16, locate the docket on the agencies' pages and read what has posted; comment posting lags the close, so the read may slip into the following week.

## 5. Preferred Bank (PFBC) Q3 10-Q, read 11/11 (FDIC FLNG cert 33539, filing 12041, attachment 813,418 bytes, sha256 `20817448c10fea5d…`)

| Item | 9/30/26 | Prior | Source |
|---|---|---|---|
| Commercial RE mortgage, accruing 30–59 | $29.8M | $10.1M [6/30]; $122.3M [12/31/25] | aging table p.16 |
| Commercial RE mortgage, accruing 60–89 | **$150.2M** | $80.5M [6/30]; $62.2M [12/31/25] | same |
| Commercial RE 30–89 as share of the class | 5.76% of $3,127.7M | — | derived |
| Real-estate special mention / substandard | **$148.4M** / $102.8M | $19.6M special mention [12/31/25] | risk-grade table |
| Nonaccrual held for investment / held for sale | $103.2M / $56.6M | $38.9M / 0 [12/31/25] | p.16 |
| NPAs | $177.5M = 2.27% of assets | $54.8M [12/31/25] | MD&A |
| Q3 net charge-offs | 0.00% of loans | — | MD&A |
| Interest due, not recognized, on nonaccrual | $7.5M | $1.7M [12/31/25] | p.16 |

- **The $56.6M mixed-use loan:** moved to held for sale in Q3 and put on nonaccrual for late payments; **not sold by 9/30**; the 10-Q reports no significant subsequent events. So "did it close at par?" = **NO by 9/30; later UNKNOWN.**
- **The named relationship:** remaining **$51.8M**, unchanged from 6/30; Q3 sold zero, $7.9M foreclosed to OREO; resolution "by either note sales or foreclosure".
- **Which loans make up the $150.2M:** **not disclosed.** My 11/05 FFIEC pull had multifamily 30–89 $143.1M [9/30], so the bucket is mostly multifamily (INFERRED, two bases). Special mention ($148.4M) is close in size (INFERRED, could be the same loans). CATO's checks (which loans, cures vs renewals, continuing exposure, capital): **UNRESOLVED**; no further evidence in the filing.
- **Why it matters:** 60–89 days late at 9/30 means these loans first missed in July–August. If still late at 12/31 they show as nonaccrual or 90+ on the Q4 Call Report (~late Jan). A hike raises the refinancing bar for exactly this book (Los Angeles multifamily and mixed use). It is one bank outside my 14: a lead for the `late-loans-outside-14` combination theme, not a cohort signal.

## 6. Inbox and BOARD dispositions (all senders)

| Item | Disposition |
|---|---|
| GIBBS 11/08 (Schwab 10-Q; my 14 cohort lines consumed, zero tags changed) | **Read. Its one ask ("reply only if yes"): does my cohort criticized line have a Q3 direction? Answer NO** — criticized splits by name (EGBN, OZK down; FLG up; VLY flat with substandard up), and my L801 "problem loans" leg mixes nonaccrual, NPL and criticized. Per its rule, no reply sent. Filed to `inbox/processed/` |
| SIG-W-20261109-012 (small items) | INFO_ONLY. WAL Q3 Basel III disclosure not read by WALTER or me; capital is the WAL desk's and the 9/30 Call Report is on file. Paraguay teachers' strike: my 11/05 Ueno read found no US bank route; LIQUID owns |
| SIG-W-20261110-002 (NY Fed household debt Q3) | INFO_ONLY. Card flow into 90+ 6.87% (CARL's grade). Consumer credit is CARL's; no bank channel figure moves |
| SIG-W-20261110-005 (small results) | INTEGRATED for one line: NEXUS PRED-38 MISS (no US bank disclosed ≥$100M Q3 charge-offs on non-bank finance borrowers) → KB ML-REG-296 as counterevidence on the `bank-lending-to-private-credit` theme. Rest INFO_ONLY |
| HOMER via PROME (Trepp bank multifamily criticized by metro, Q2: Phoenix 38.6%, Houston 35.5%, Dallas 35.3%, national 22.5%) | Logged as a lead, KB ML-REG-295. ⚠️ Secondary (TreppTalk 11/05), Trepp's own loan sample, Q2; not tied to any of my 14. WAL is headquartered in Phoenix, but metro criticized rates are not WAL's book; no inference to WAL |
| Peer channels OZK, WAL | 0 entries above my last ACK |
| Corrections | 0 unreceipted |

**Small items, logged here only:** EGBN Form 4s 11/10: director Eric Newell bought 1,470 sh at $33.91; director A. Leslie Ludwig sold 16,669 sh at $33.63–$33.87 (insider script, SEC). Net selling, small. KRE shares outstanding 54.80M [11/11] vs 55.48M [11/08], −1.2% (redemptions; my 11/03 base rate says share contraction alone is not a bank-credit signal).

**Own-record correction:** BOARD_LOG row SIG-W-20261106-044 carried a printf-mangled note ("+14.5 0x0p+0fter -4.4 0n August"); restored to "+14.5% after -4.4% in August" (the `% a` and `% i` sequences had been read as format codes).

## 7. Not done

- WAL Q3 Basel III disclosure: not read (WAL desk owns capital).
- No securities-duration or AOCI dollar sensitivity for the cohort (not measured; would need each 10-Q's AFS table).
- FOMC pricing: verified at closeout via ORACLE KB-ORC-133 (see §2).
- BOARD backlog (2 May action cards, 40 info cards) still unlogged; carried.
