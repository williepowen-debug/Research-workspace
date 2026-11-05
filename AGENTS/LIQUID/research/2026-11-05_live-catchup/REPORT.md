# LIQUID live catch-up, 2026-11-05

**Trigger:** Will in PROME's window 09:42 ET, verbatim in `inbox/2026-11-05_from-PROME_catch-up-to-live-data.md` (commit 7dac94dc1). **Runtime:** Claude Code, Opus 5.5. **Clock:** captures 09:45 to 09:50 ET. **Basis:** first-published FRED/ALFRED unless stated. ALFRED realtime labels on ICE rows are backdated and are not availability timestamps. Vendor equity bars are the yfinance mirror; a bar dated November 5 is intraday, not a close.

**No trade, order, level, operator, instrument or consequence moved.**

## 1. Verdict

Funding stayed calm on the first clean post-month-end day: the overnight tail is +12 bp, 18 bp under the 079 line, and repo take-up is $0. The stress that moved is narrower: the AI-infrastructure cohort fell 7% to 11% on November 4 against an up tape, CoreWeave 5Y CDS widened, and Oracle and Meta CDS tightened. That is single-cohort equity and CDS repricing, not funding stress. No registered gate changed state.

## 2. Gate grades

| Gate | Grade at this read | Cells | Open |
|---|---|---|---|
| **GATE-LIQ-079** | **NOT ARMED, review grade final.** | SOFR99 4.02 − IORB 3.90 = **+12 bp [November 4, first-published]**; first non-calendar day, absent from `GATE079_CALENDAR_EXCLUDED.tsv` (October 28 to November 3 excluded). ARM needs ≥+30 on 2 consecutive. FIRE not graded while unarmed. | None. PROME sets the next review. |
| **GATE-LIQ-069** | **2-of-2 FIRED unchanged; nothing re-counted.** L1 NOT FIRED [BB 203, November 3]. L4 NOT FIRED through November 3. **November 4 cannot fire on the equity half:** worst IREN −11.24% (exact), none ≤−15%. Formal November 4 row needs HY. | L2 standard 5Y see §3. L3 NO_INSTRUMENT. L5 primary still inaccessible, no R1 supported. | November 4 HY/BB/CCC, about 16:15 ET. |
| **GATE-LIQ-076** | **Current window NOT MET 1 of 3 (W3).** Original October 22 episode preserved; no reset, no second write-up. | W1 as-of October 27: −2,535,985, weekly −162,945 (CME full-name key). Not ≤−2,950,000, not cover >+300,000. W2 as-of October 21 aged out, not improved; G5L10 −1,861, G10 −10,277. W3 yfinance witness MOVE 93.88 / VIX 16.61 [November 4]; VIOLET governs edge closes. | W2 as-of October 28 about 16:15 ET; W1 as-of November 3 due November 6 about 15:30 ET. Actionable-life denominator stays CANNOT-CERTIFY. |
| **GATE-HY-REKILL** | **NOT FIRED 0 of 2** through November 3. | HY 340 [November 3]. No below-260 observation. | November 4 unpublished, not a non-fire. |
| **GATE-LIQ-072** | **Price leg NOT FIRED** through November 3 (not due until December 31). | IG 93, basis 247. No new issuer instance in the sourced DTCC set; broader search not certified. | None due. |

**HY and CCC run counts, first-published:** renewed >320 run stays **4 observations** (326 / 344 / 343 / 340 [October 29, 30, November 2, 3]). CCC 1,316 [November 3]. No new cell exists at this read: November 4 was absent from FRED at 09:45 ET. PROME's dashboard figures are confirmed by primary cells and are not newer than them.

## 3. Named CDS, DTCC SEC file November 4 (1,642 rows)

| Name | Standard 5Y (2031-12-20) | Versus November 3 | Basis and limits |
|---|---|---|---|
| CoreWeave | Upfront 18.50 pt (17:03Z) and 20.38 pt (20:46Z) ⇒ clean 1,103 / 1,183, dirty 1,130 / 1,211 bp | Wider: 18.14–18.39 pt, 1,088–1,124 bp | Model-derived, flat hazard, unsigned upfront assumed buyer-pays, not executable. The 20.38 pt print is CAPPED (notional 5,000,000+, upfront scaled to the cap) and a CORR. Same-minute 4Y and 4.5Y capped prints sit on a consistent curve. |
| Oracle | Converted 288–297 bp; disseminated 292 bp (18:56Z, underlier 6EC42L) | Tighter: 300 disseminated, 293–295 converted | One November 4 MODI row carries spread 0.000211 (2.1 bp) on reference obligation XSSNRREFOBL0. Quarantined as on November 3, never a level or a card void. |
| Meta | Disseminated 109–110 bp | Tighter: 120 on the same 2031-12-20 tenor, checked | Near-coupon conversions (105–109) not adopted, sign unknowable. |

L2 stays counted once. A wider CoreWeave print re-counts nothing.

## 4. AI cohort equity, vendor mirror

| Name | Nov 3 close | Nov 4 close | Nov 4 move | 09:47 ET Nov 5 **intraday** | Intraday move |
|---|---:|---:|---:|---:|---:|
| CRWV | 53.74 | 48.42 | −9.90% | 44.995 | −7.1% |
| IREN | 24.46 | 21.71 | −11.24% | 19.67 | −9.4% |
| APLD | 17.81 | 16.61 | −6.74% | 14.97 | −9.9% |
| NBIS | 151.64 | 141.52 | −6.67% | 125.80 | −11.1% |
| SPY | 754.35 | 766.81 | +1.65% | 756.07 | −1.4% |

⚠️ **The November 5 column is first-minutes tape, not a close, and no L4 reading.** No cause is established; none was searched. L4 for November 5 needs the close and the November 5 HY cell, published November 6. If a name closes at or below −15% (NBIS at about $120.29) the equity half is met and the HY half decides. L4 is already counted once, so a fire would be a new observation, not a re-count.

## 5. Funding and Fed

First-published [November 4 rates, read November 5]: SOFR 3.94, SOFR1 3.86, SOFR75 4.00, SOFR99 4.02, IORB 3.90, EFFR 3.88. So SOFR−IORB +4 bp, SOFR99−SOFR1 16 bp, EFFR−IORB −2 bp. Repo take-up $0 [November 4]. Reserves $2,893.770B and TGA $999.727B stay as-of October 28; the next H.4.1 is due tonight.

## 6. Gate 069 L4 repair (DAEDALUS WITHHELD packet, actions 1 to 7)

| Action | Result |
|---|---|
| 1 Keep hold | Kept. CLI prints WITHHELD, exit 4. |
| 2 Treat non-cent closes | **Option (a):** vendor value at 4dp, storage noise only. `as published` and `Compare the UNROUNDED ratio` already say this. Options (b) and (c) would each add a rule. |
| 3 Record in KB-LIQ-069 | Note appended; letter text unchanged. "2dp" is read as describing the ordinary close, not as a rounding instruction. |
| 4 Replace line 257, add CLI-path test | `vendor_close()` / `vendor_closes()` are the one read path. Test feeds both DAEDALUS cases as float32 through that path, then `grade_l4`. Commit 303bae4a7. |
| 5 Test against old line | **Corrected after DAEDALUS read 2:** the 3-check failure covers a copy that changes `vendor_close` to 2dp: SELFTEST FAIL, 3 ✗ (CRWV false fire, NBIS false miss, half-cent lost). It does **not** cover the literal old line restored at the `main()` call site: that copy leaves selftest PASS, because the checks named "CLI path" never run `main()`. My packets said the test "fails on the old line", which overclaimed. A `main()` test is owed once the hold is removed; it cannot change a grade at this file. |
| 6 Correct the count | "43 sessions" was 42 NYSE sessions plus September 7, not a session. This pull, wider start: **44 NYSE sessions September 2 to November 3**, exact oracle 0 disagreements, 0 changed versus 2dp, 1 fire (October 14, CRWV −15.461%, HY +9). **Six closes change under normalization:** CRWV 54.235 [October 23], IREN 44.125 [September 25], IREN 24.905 [October 23], APLD 20.325 [October 14], APLD 17.815 [October 30], NBIS 237.355 [September 29]. |
| 7 Request one read | Packet to DAEDALUS at this commit. |

**Closed 2026-11-05:** DAEDALUS read 2 RELEASE at 303bae4a7, WQ-603 RULED A (Will, 10:32 ET, "603 A"), PROME order confirmed. Hold block deleted, CLI exit 0 on a live run (`gate069_live_first_run.txt`). New `main()` and stored-tie tests catch all three mutants, including the literal old line at the call site; they are **TESTED, not INDEPENDENTLY VERIFIED**.

**Authority judgement, as held before the ruling:** code change sits inside the existing bounded repair (`ACCEPTANCE.md`: no threshold, operator, instrument, calendar, missing-input rule or consequence change). The "2dp" reading of a gate letter is flagged to PROME and Will rather than treated as settled.

**Still open:** whether a vendor half-cent matches an official exchange close. `published_cent_closes.json` is generated by rounding (`reconcile.py` line 12), so it is not a second source. Limit of the test: it covers the read path, not a live yfinance call; `main()` stays held. Float32 exactness is argued for closes under $1,024, and cohort closes are well below that.

## 7. L829 I1 XCCC

The standing line remains encoded at STATUS §1, last refreshed at source October 29. **Refresh blocked:** BondBloxx page HTTP 403 at 09:47 ET [saved `xccc_page.html`]. The same page alternated 403 and 200 on October 29 and 30. One same-method retry is planned after 16:15 ET; no workaround.

## 8. Q3 BDC card and Q2 owed fields

SEC access returned at 09:50 ET (PROME; `PROME/MACHINE_LOCAL.md`, verified by live EDGAR calls here). Full tables at `workbook/BDC_MARK_CONVERGENCE_MONITOR.md`.

Card registered and committed 09:48 ET (d8e72e264) before this desk read any Q3 print. **Correction from EDGAR:** ARCC filed October 27, BXSL and OBDC November 4, FSK November 5, so the card pre-dates filings only for GSBD and MAIN. Lines transcribed unchanged.

**Partial grade, four of six filed, PROVISIONAL, neither CONFIRM nor REFUTE.** NAV −0.11% (FSK), −1.10% (BXSL), +0.42% (OBDC), −0.21% (ARCC). All four FV/Cost up (+0.14 to +1.26pp). Non-accruals by fair value: FSK 3.8→3.4, BXSL 1.8→2.1, OBDC 0.8→0.8, ARCC 1.4→1.4. No regular dividend cut; OBDC supplemental $0.02→$0.01. P/NAV fell on all six against the August 23 column. CONFIRM route 1 now needs both GSBD and MAIN.

**So what:** marks did not catch down while wrapper prices kept falling, so the gap stayed open. ⚠️ FV/Cost up is not healing: BXSL's cost base fell $606M and its NAV and non-accruals still worsened.

**Q2 owed fields closed:** M3 Q1→Q2 FSK 4.2→3.8, BXSL 3.1→1.8, OBDC 1.0→0.8, ARCC 1.2→1.4, MAIN 1.2→1.1; GSBD unread. ARCC M1 0.9950→0.9890, −0.60pp, NAV leg short. Verdict stays CONFIRM. Three names fell >1pt on FV/Cost, so route 2 was also met in Q2.

No X1 half, sizing or fire follows: this absolute card has no manager comparator.

## 9. Inbox and cards

WALTER SIG-W-20261104-076 and -078, ISHM backlog and DAEDALUS packet consumed. ISHM rail volumes are physical-volume counterevidence only, no funding clearance. Oil's fall [November 4, per WALTER's vendor and CNBC read, no deal established] does not bear on any LIQUID gate; WQ-545 energy-to-credit stays unestablished.

**PROME C10 packet held, not done.** It asks for a whitespace edit to `AGENTS/LIQUID/CLAUDE.md` line 14. This session does not edit CLAUDE.md on a peer's request, so that one line waits for Will's direct word. Nothing depends on it.

## 10. Blocked or not progressed

| Item | State |
|---|---|
| Q3 card final | Waits on GSBD and MAIN 10-Qs. GSBD non-accrual % not extractable from text read. |
| October HY issuance subtotal | Blocked: SIFMA HY workbook leads to a contact form, not submitted (external send). |
| AI new-issue concessions, L5 primary re-verification | No instrument; S&P connector is Will's call. |
| Test C (DOCKET L19), Test B/T4 closure | Not progressed. Grading Test C now needs a new look-back on a window that closed August 26; recorded for PROME, not started. |
| ES01 denominator, ES05 sign | No recoverable definition. No new study. |
| Car-Mart cash bridge, Brazil settlement/LFT, JetBlue identity, equity-financing bridges | Conditional on sources not obtained; no recurring search. |
| DAEDALUS 10/8 asks ②④ | Letter-precision wording on 072/069/079; held under the catch-up limit on frozen letters. |
| `boot.py` ledger-stamp fix | Trigger is the next touch of `boot.py`; not touched. |

## 11. Evidence

Series JSON, `raw_closes.json`, `dtcc_2026-11-04.json`, `crwv_grade.txt`, `dtcc_probe_*.txt`, `reconcile.py`/`.txt`, `cftc.txt`, `collect.py`, `supplement.py`, `xccc_page.html`, all in this folder. The dealer series JSON still ends as-of October 21. Remaining publications read after 16:15 ET go in an addendum.

## 12. Addendum: November 4 credit, read 10:33 ET

**Correction:** I said November 4 ICE cells publish about 16:15 ET. They were absent at 09:45 ET and present by 10:33 ET on November 5, per the first CLI run and `after_1033/collection.txt`. ALFRED's labels are backdated, so this observed window is the only availability evidence.

First-published [November 4]: HY 332 (−8), IG 91 (−2), BBB 113 (−3), BB 199 (−4), B 351 (−11), CCC 1,297 (−19). HY−IG 241, CCC−BB 1,098, CCC−B 946. 15 sessions from October 14: IG +7, BBB +9, BB 0, B +22, CCC +15, HY +7.

| Key | Result |
|---|---|
| Tier rule | **REVERSES**, replacing BROADENS. Ordered September 25 rule, first row: CCC −19 ≤ −9 and B −11 ≤ −4. The rule's parenthetical speaks of giving back half of September 23; I apply the numeric lines as it directs for each following print. One print, not a trend. Levels stay wide. |
| HY >320 run | **5 observations**, 332. |
| GATE-HY-REKILL | NOT FIRED 0 of 2 through November 4. |
| GATE-LIQ-069 | **Review grade final, 2-of-2 FIRED unchanged.** First run of the restored CLI: L1 NOT FIRED (BB 199), L4 NOT FIRED (HY −8, worst IREN −11.24%), exit 0. The CLI reads latest-revised; its BB, CCC and HY cells match first-published here. |
| GATE-LIQ-072 | Price leg NOT FIRED: IG 91 fails >94, basis 241 fails <180. |
| GATE-LIQ-076 | Unchanged. W2 as-of October 28 still unpublished at 10:33 ET. |
| DOCKET L829 I1 | Retry 10:33 ET: HTTP 403 again. `etf_holdings.py` covers HYG and JNK only. Line stays October 29; **blocked**, no further tries. |

**So what:** credit tightened across every tier on the day the AI cohort fell 7–11%. On that session cohort stress did not reach index credit, which supports a single-cohort read. It proves nothing about November 5, whose tape was weaker at the open.

## 13. Addendum: Will's follow-on list, 10:39 ET

**XCCC (DOCKET L829 I1): refreshed.** Correction: I told Will I had stopped trying. curl returned 403 at 09:47 and 10:33 ET; one ordinary WebFetch returned HTTP 200 at about 10:40 ET, so the refusal was client-specific, not a site outage. No proxy or unblocking service was used. Holdings as of November 4: 178 securities (177 bonds plus cash), 124 issuers. `after_1040/xccc_rows_2026-11-04.txt` is transcribed by the fetch agent. **Validated:** all ten rows of the page's Top 10 Issuers table reconcile to the cent; rows sum to 100.05%.

| Bucket | Weight | Basis |
|---|---:|---|
| AI builders | **0%** | Same name screen as October 29 |
| Cable, telecom, media | 18.71% | Desk name bucket, includes Connect Holding (Brightspeed, from my knowledge of the name, not read from the filing) and Viasat |
| Software | 5.76% (3.75% without athenahealth) | Desk name bucket |
| Other | 75.53% | Remainder |

Issuer sector taxonomy was not in the fetched text, so Technology 7.71% and Communications 17.02% stay October 29; do not difference the buckets against them. "Download CSV" exposed no link target. **Cross-check:** XCCC N-PORT for July 31 (BondBloxx ETF Trust CIK 1879238, S000075710, filed September 25, accession 0001003715-26-003711): 182 positions, AI name hits none.

**Main Street:** 8-K October 15 Ex. 99.1, company preliminary estimate: NAV $34.18–$34.26 at September 30, up $0.26–$0.34, or 0.8%–1.0%, after a $0.30 supplemental. An estimate, not the 10-Q. **Goldman:** reports after the close today, call November 6 09:00 ET (8-K October 5). With MAIN's estimate, CONFIRM routes 1 and 2 cannot be met; only a fresh regular cut at GSBD or MAIN remains.

**Dealer positions and H.4.1:** as-of October 28 still absent at 10:40 ET. Watchers running; nothing can bring these forward.

**C10:** done on Will's word ("work on these next", 10:39 ET). `CLAUDE.md` line 14 re-spaced, wording only.


## 14. Addendum: WALTER cards 013, 017, 024, 031, read 13:56 ET, written 13:58 ET

Tape below is vendor delayed, 13:56 ET November 5, against November 4 raw closes. **Not closes, not a grade.**

### 14.1 Card 017: funding and credit read

| Read | Value | Date and basis | So what |
|---|---:|---|---|
| Standing Repo take-up | $0 and $0, both operations | November 5, NY Fed results API | Nobody used the Fed's backstop today. Absence is weak evidence: a stressed dealer can still avoid it |
| Reverse repo | $0.125B | November 5, NY Fed | Empty, as it has been |
| SOFR−IORB, SOFR99−IORB | +4, +12 bp | November 4, first-published | **Predates today.** November 5 publishes about 08:00 ET November 6 |
| HYG, JNK, BKLN | −0.47%, −0.50%, −0.66% | tape | Proxy only; no cash spread for today exists |
| LQD | +0.11% | tape | Investment grade is rising, so this is no dash for cash on this read |
| BIZD, ARCC | −1.70%, −1.88% | tape | Weaker than bond funds, far less than AI names |
| GS, MS | −6.33%, −6.44% | tape | **Gap:** I have no prime-brokerage financing data, so I cannot say whether this is earnings fear or funding |
| XLF, KRE, WAL | −2.62%, −2.46%, −4.75% | tape | Banks now confirm the equity move. KRE was +0.75% at 10:29 ET |
| SPY | −3.98% | tape | |

**Read:** nothing I can see shows a financing constraint. Stress is equity-led and AI-centred, spreading into bank equities, not visibly into funding. That is working model only: every direct funding rate for today is unpublished, and proxies are weak in fast markets because ETFs and cash bonds can diverge.

**L4 tape, not a grade:** IREN 18.04 (−16.93%), NBIS 118.26 (−16.44%), APLD 13.96 (−15.98%), CRWV 42.59 (−12.04%). Three of four sit past −15%. L4 needs a raw close at or past −15% AND HY +5 bp or more on the same session, so HY at 337 or wider, first-published.

### 14.2 Card 031: Fed October SLOOS, Table 1 net percentages (owner read, primary)

Net percentage = tightened minus eased, computed from Table 1 and tied to Table 1 row 29.A (22.0 − 4.9 = 17.1). Full table: `after_1355/sloos_oct2026_net_pct.txt`. Survey covers about Q3; answers were due about October 5 per card 031, so it predates this week.

| Line | All | Large banks | Other banks |
|---|---:|---:|---:|
| Standards, business credit intermediaries | +22.0 | +20.0 | +23.4 |
| Standards, private equity funds | +15.4 | +5.0 | +21.9 |
| Standards, other NDFIs | +20.4 | +11.1 | +25.8 |
| Demand, business credit intermediaries | +10.7 | +10.0 | +11.1 |
| Demand, private equity funds | +5.4 | +15.0 | 0.0 |
| NDFI terms: spread over cost of funds | 0.0 | **−30.0** | +17.1 |
| NDFI terms: maximum line size | +5.4 | **−10.0** | +14.3 |
| NDFI terms: premium on riskier loans | +18.6 | +5.2 | +25.7 |
| Standards, construction and land | +15.6 | +10.0 | +18.5 |
| Standards, nonfarm nonresidential | +8.8 | +5.2 | +10.6 |
| Standards, multifamily | +8.8 | +5.0 | +10.8 |
| Demand, construction / nonfarm / multifamily | −25.8 / −10.6 / −22.8 | −40.0 / −10.5 / −25.0 | −18.4 / −10.6 / −21.6 |
| Standards, C&I large and middle | +1.7 | −4.5 | +5.2 |
| Terms, C&I large and middle: spreads | −15.0 | −22.7 | −10.5 |

CRE standards moved from net easing in July (−3.7 / −11.3 / −5.7, same questions) to net tightening. The July table asked a different NDFI question (level of standards), so **no like-for-like NDFI change exists here**.

Why banks tightened NDFI lending, 21 respondents, very plus somewhat important: outlook 76.2%, NDFI borrower financial strength 71.4% (23.8% very), risk tolerance 66.7%, collateral risk 61.9%, correlated drawdowns 33.4%, **own capital 4.8%, own liquidity 4.8%**. Why NDFI demand rose, 13 respondents: working capital or liquidity needs 69.2%, refinancing needs 61.5%, shift from other banks 53.8%, shift from nonbank or capital markets 30.8%.

**Read:** supportive of tightening at the margin for nonbank lenders, and it refines the card's "tighter on all NDFI". Standards are tighter on every type, but **large banks cut spreads and raised line size on net** while smaller banks tightened; large banks as a group were still competing on price. Banks attribute it to the borrower, not to their own balance sheets, so this is a credit-selection story, not a funding constraint at the banks. The ⚠️ is the demand side: borrowers asking for more bank money for liquidity and refinancing while standards tighten is what an early squeeze would look like. n=13, small, one quarter, net percentages count banks rather than dollars. No gate leg reads SLOOS.

### 14.3 Cards 013, 024 (with 026, 029): Ueno and Paraguay, does a channel reach this book

**No channel reaches a registered gate or level on what is measured. That is not an all-clear; about 95% of the bond's holders are undisclosed.**

| Channel | Evidence | Read |
|---|---|---|
| US fund holdings | $17.9M face, 17 series, 5.1% of $350M, max 1.22% of a fund, pre-failure reports (REGINALD, N-PORT, CUSIP 903934AB3) | Small. About $332M undisclosed |
| US bank loans or correspondents | None named; Citi and BNY named as counterparties, role and size unknown (REGINALD) | Not found, not excluded |
| Sovereign spread | 119 → 138 bp, secondary, unverified | 19 bp, modest. Paraguay bond prices NOT read |
| Currency | Vendor PYG=X 5,661.7 [October 29] → 5,786.8 [November 4] → 6,030.9 tape, +4.2% today, +6.5% from October 29 | Largest market move and accelerating. Smaller than the secondary +9–10% REGINALD carried; vendor mid, not a primary, and those press levels (6,160–6,500) are not on this feed |
| Foreign Treasury holdings | Paraguay not named in TIC Table 5 major holders | Too small to list. Any reserve defence of the guaraní does not register at this scale; size of BCP Treasuries NOT read |
| EM funds | EMB −0.43% tape | Same order as HYG on a −4% equity day; cannot isolate Paraguay |

**Paraguay internally is the live contagion test**, not the US: Congress has not accepted the resignation; first guarantee payments unconfirmed; the other merger-facility banks (GNB, Sudameris, Continental) and Zeta as lender and trustee are REGINALD's relayed open tests, secondary. Balances at November 2 unknown. No withdrawal data found. Next steps belong to a live event, not a new study.

### 14.4 Other packets integrated

- **VULCAN, Oracle and Meta new issues, filing-primary:** reconciles with my CDS read as one picture. Meta 2031 +110 [November 3] against CDS 109–110 [November 4]; Oracle 2031 +275 [November 2] against CDS 292 [November 4]. Basis differs: bond over Treasuries at pricing against model-converted CDS, one and two days apart. Same-issuer widening of +145 to +175 (Oracle, since February) and +57 to +88 (Meta, since April) is the repricing; both deals cleared, which argues access, not closure. No trigger of mine fires on these.
- **BROCK:** Q3 card reconciled on FSK, BXSL, OBDC, ARCC. Ladder row 10 (VIX +3 without HY widening) grades on my November 5 print; added to owed.
- **CREED:** T-01a fired, info. Its open item on SLOOS percentages is answered in 14.2.
- Card 010's CoreWeave yields (15–16%) stay a screenshot, not priced here.

No gate, level, operator, instrument or consequence changed. No trade.
