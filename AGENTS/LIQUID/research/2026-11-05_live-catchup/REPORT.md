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

### 14.5 What the November 5 print does to the tier rule, computed 13:59 ET (no rule changed)

September 25 ordered rule, applied to a November 5 print. 15-session base is October 15, levels IG 84, BBB 105, BB 197 (latest-revised FRED, so first-published may differ by a point).

| Outcome | Needs on November 5 |
|---|---|
| REVERSES, checked first | CCC at or below 1,288 and B at or below 347 |
| BROADENS, 15-session clause | IG at or above 90 (+6), or BBB at or above 112 (+7), or BB at or above 216 (+19). IG is 91 and BBB 113 [November 4] |
| BROADENS, daily clause | B or CCC wider and IG +2, BBB +2 or BB +9 on the day |

**⚠️ Unless REVERSES repeats, or IG and BBB both tighten at least 2 bp, the rule prints BROADENS on the 15-session clause, even on a flat day.** That clause does not require B or CCC wider. So a November 5 BROADENS alone carries little news. The information is in the day's changes: the daily clause separates new spreading up the quality ladder from arithmetic left over from October.

### 14.6 Wider funding-stress sweep, 14:15 ET, one-off, no new monitor

Bill auctions November 5 (TreasuryDirect, closed 11:30 ET): 4-week 2.46x, $115B offered, high rate 3.890%, against 3.10 / 2.82 / 2.56 / 2.40 prior four; 8-week 2.68x, against 2.63 / 2.57 / 2.26 / 2.77. Tape 14:14 ET, not closes, against November 4: ^TNX 4.829 from 4.894, ^FVX 4.601 from 4.689, ^IRX 3.987 from 4.025, gold 4,110.9 from 4,073.0, DXY 101.48 from 101.51, USD/JPY 157.79 from 158.47, MOVE 99.88 from 93.88, PFF −1.95%, PGX −1.15%, AT1.L −0.12% (London session, check close time). Fed dollar swap lines: latest row returned October 28, ECB $164M, BoE $5M, ordinary size; no November 4 row returned. Commercial paper on FRED stale here: nonfinancial 30-day 3.98% [November 3], financial last row October 20. OFR stress index through November 3, before today. Not a dash for cash: Treasuries and gold up, dollar flat. Not reachable: cross-currency basis, swap spreads, prime-brokerage margin, repo haircuts, Treasury bid-ask.

### 14.7 Close read, 16:19 ET: Gate 076 W2 and the L4 stock leg

GATE-LIQ-076 W2 as-of October 28, NY Fed, first published by 16:19 ET: G10 −9,739 (−10,277 prior), G5L10 −379 (−1,861 prior), NOT MET. As-of October 28 predates the November 5 selloff. W3 does not meet on November 5: VIX 26.86 (WALTER vendor 16:05 ET) or 27.77 (yfinance 16:19 ET), the two vendors differ and neither is under 20; MOVE 97.95. Corrected: both reads predated the final prints, WALTER card 057 has VIX about 28.17 vendor 16:22 ET, Cboe history not yet posted. W3 unaffected. Window October 23→November 5, 1 of 3. W1 as-of November 3 due November 6.

L4 stock leg, yfinance raw closes 16:08 ET, not official: IREN 18.03 (−16.95%, from 21.71), NBIS 120.37 (−14.94%, 8 cents above its line), APLD 14.17 (−14.69%, 5 cents above), CRWV 43.66 (−9.83%). IREN alone meets the ANY ONE name letter, with a 42-cent margin to 18.45. `gate069_legs.py` at 16:19 ET: still grades the November 4 session, L4 NOT FIRED; November 5 UNGRADEABLE-PENDING-PUBLICATION until HY November 5 prints. HY 337 or wider first-published fires L4. HY 357 is WALTER's +25 bp routing safety net, not a LIQUID gate.

Closes, yfinance 16:19 ET, against November 4: HYG −0.31%, JNK −0.27%, BKLN −0.68%, LQD +0.15%, SJNK −0.17%, ANGL −0.32%, BIZD −0.79% (−1.70% at 13:56 ET), ARCC −0.57%, OBDC +0.46%, BXSL +1.05%, FSK +1.75%, GS −6.36%, MS −5.94%, JPM −4.19%, KRE −2.47%, WAL −4.24%, PFF −2.02%, PGX −0.90%. S&P 500 −4.36%. Credit funds fell about a tenth of the S&P move and BDCs did not follow it. That is a fund read, not the cash index, and fund prices can lag cash bonds on a day like this.

### 14.8 H.4.1 release November 5, read 16:37 ET, first-published, as of November 4

Week average to November 4 against October 28: reserves (WRESBAL) $2,930.088B from $2,893.770B, +$36.3B; TGA (WTREGEN) $957.175B from $999.727B, −$42.6B, so the rise is largely Treasury cash leaving the TGA. Line <$2.8T, $130.1B clear. Wednesday levels: reserves (WRBWFRBL) $2,962.804B, TGA $936.248B. Primary credit $9.983B week average (+$0.482B), $9.219B Wednesday. Secondary credit 0. Fed repos: $5M week average, 0 Wednesday. Foreign repo pool $338.205B week average (+$8.043B), $334.278B Wednesday. Liquidity swaps $169M Wednesday. Nothing here can show November 5; it ends the day before.

## 15. Addendum: November 5 credit print, Gate 069 L4, GSBD and Will's funding sweep, November 6 (session wake under WQ-626 A, DOCKET L970; written 10:17 ET)

**Verdict.** Credit finally moved with the AI cohort and funding did not. HY 348 is the highest print of 2026 and BB took the biggest step of any rung relative to its own history, yet the overnight funding gauges were quieter on November 5 than on November 4. Price stress widened; no financing restriction is shown. That is a working read of one print, and the blind spots in §15.6 are exactly where a restriction would show first.

### 15.1 November 5 credit, FRED first-published, read 10:10 ET November 6

| Tier | Nov 4 | Nov 5 | d/d | d/d rank | 15-session from Oct 15 | Rule line |
|---|---:|---:|---:|---:|---:|---|
| IG | 91 | 93 | +2 | 96.3% | +9 | d/d +2 met; 15s +6 met |
| BBB | 113 | 116 | +3 | 97.7% | +11 | d/d +2 met; 15s +7 met |
| BB | 199 | 213 | +14 | 98.2% | +16 | d/d +9 met; 15s +19 missed |
| B | 351 | 367 | +16 | 98.0% | +41 | wider |
| CCC | 1,297 | 1,320 | +23 | 97.2% | +42 | wider |
| HY | 332 | 348 | +16 | 98.0% | +25 | |

Ranks: `transmission_check.py`, 784 daily changes, 2023-11 to 2026-11, a calm window (§5 of STATUS). HY−IG 255, CCC−BB 1,107, CCC−B 953, B−BB 154. First-published equals latest-revised on all six cells at this read. **HY 348 and HY−IG 255 are the 2026 highs on FRED latest-revised rows (prior 346 and 253, both March 30).**

**Tier rule: BROADENS, on the daily clause.** REVERSES fails (CCC +23, B +16). All three daily conditions met at once, so §14.5's warning about arithmetic does not apply: this print did spread up the ladder. The clause does not distinguish a one-day beta move from a lasting one. HY >320 first-published run = 6 observations: 326 / 344 / 343 / 340 / 332 / 348.

### 15.2 Gate grades on this print (LIQUID rows only)

| Gate | Grade |
|---|---|
| GATE-LIQ-069 L4 | 🔴 **FIRED, session November 5.** IREN 18.03 from 21.71, −16.95%. Nasdaq historical close (`api.nasdaq.com`, read 10:11 ET) equals yfinance raw on both dates for all four names: NBIS 120.37 from 141.52, −14.94%; APLD 14.17 from 16.61, −14.69%; CRWV 43.66 from 48.42, −9.83%. HY +16 ≥ +5. CLI verdict FIRED, November 6 session UNGRADEABLE-PENDING-PUBLICATION. New observation of a leg already fired on the October 14 session; fired-leg count unchanged, no new consequence. |
| GATE-LIQ-069 L1 | NOT FIRED. BB 213, 7 bp under 220 (strict). CCC 5-session −5, flat. **BB is at its highest since March 30 (222, latest-revised); BB >220 with CCC flat is the next line.** |
| GATE-LIQ-076 | Window October 24→November 6: 1 of 3 on published (W3), W2 NOT MET as of October 28, W1 as-of November 3 pending about 15:30 ET. |
| GATE-LIQ-079 | NOT ARMED. SOFR99−IORB +10 bp [November 5], non-calendar, under +30. |
| GATE-LIQ-072 | NOT FIRED. IG 93 fails strict >94, basis 255 fails strict <180. |
| GATE-HY-REKILL | 0 of 2. |

Not LIQUID's to grade, print supplied only: VIOLET credit-flat (HY 5-session 326→348, +22), TERRY 344 and 350, REG-T-04 (REGINALD), RED lines, BROCK ladder row 10.

⚠️ **IREN timing.** The Q1 FY27 8-K was accepted about 16:03 ET November 5 (EDGAR 21:03Z), after that close, so the fall preceded results. IREN vendor intraday 21.25 at 10:11 ET today, about +17.9%; not a close and it does not touch the grade. Only one of four names met the line, and two missed by 8 and 5 cents. ANY ONE NAME is the letter (WQ-170), so the fire stands.

### 15.3 What cards and packets add (read, no grade moved)

- **VIOLET close signal:** VIX 28.18, VIX3M/VIX 0.9067 inverted, VVIX 134.99. The inversion routes to LIQUID and HENRY: no LIQUID line keys on it. W3 needs VIX under 20, so it does not count November 5.
- **ORACLE:** December hike odds fell about 17 points (Polymarket 80.5→63.5, Kalshi 81→65), cause not established. 2-year par yield fell 12 bp the same day, 4.58→4.46 [Treasury], the largest move on the curve, consistent with a repriced Fed path and not with a funding squeeze.
- **WALTER card 004 (action, read against gates):** 23 of 24 data-centre high-yield bonds wider, CoreWeave unsecured +42 to +73 bp, ZeroHedge tables on TRACE, secondary and unchecked; TRACE not reachable here. L3 (new-issue concessions) stays NO_INSTRUMENT: secondary widening is not a concession. KB-LIQ-073 basket has no numeric line, and CCC +23 on the day means the "CCC flat" signature is not met on that session; no fire claimed. ING's $500M loan auction (bids November 19) and the Bank of England's questions are logged, no gate reads them.
- **CYPHER (Arkéa, Finzly, Abrigo):** no rail effect on any LIQUID surface; see §15.5 and the reply packet. These surfaces cannot see a European payment rail.
- **LABOR freeze-thaw v2 fired this morning, hiring read only, layoffs unchanged:** context; no LIQUID line reads it.

### 15.4 GSBD Q3 and the Q3 BDC card

10-Q accepted 17:00 ET, 8-K 18:04 ET November 5. NAV $11.70 from $12.06, −2.99% (−2.74% against adjusted $12.03). FV/Cost 0.9195 (2,857,960 / 3,108,109) from 0.9368, −1.73 pp. Non-accruals 4.2% of fair value from 2.9%, 7.3% of cost from 5.0%, 11 companies; one restored to accrual, two new names placed, further tranches at two existing names. Regular dividend held at $0.32; no supplemental declared post-quarter ($0.03 the quarter before). NII $0.32 covers it exactly; EPS $(0.04). Net debt/equity 1.21x from 1.35x. The book shrank: $371.2M sales and repayments against $40.5M commitments.

**Card state: CONFIRM is closed on all three routes, REFUTE not met, MIXED only in part.** Route 1 needs two names; GSBD is one and MAIN's NAV rose. Route 2 needs three and only two names were left. Route 3 needed a fresh regular cut; GSBD and MAIN both held. MIXED's letter has FSK and GSBD marking down while MAIN and ARCC hold, but FSK did not (NAV −0.11%, FV/Cost up). PROVISIONAL until MAIN's 10-Q, not on EDGAR at 10:12 ET, so its 117% stays rounded. Detail: `workbook/BDC_MARK_CONVERGENCE_MONITOR.md`.

### 15.5 Will's funding sweep (word 15:40 ET November 5), one-off, no new monitor

**Answer: no sign of a dash for cash or a funding squeeze through November 5, or this morning where a reading exists.** Overnight rates eased, the Fed's backstop was unused, Treasuries and gold rose with the dollar flat. Banks and preferreds took the equity hit; credit funds fell far less than cash spreads implied.

| Gauge | Reading | Against | So what |
|---|---|---|---|
| Fed standing repo | $0 [November 5], $0 this morning's 08:15 ET operation [November 6] | $0 [November 4] | Unused |
| Overnight RRP | $0.125B [November 5] | $0.225B | No flight into the Fed |
| SOFR−IORB / 75th / 99th | +2 / +7 / +10 bp [November 5] | +4 / +10 / +12 | Eased |
| TGCR−IORB, EFFR−IORB | 0, −2 bp [November 5] | +3, −2 | Eased |
| Bills | Last auctions November 5, 4-week 2.46x, 8-week 2.68x, held during the fall; none since | §14.6 | Soft 4-week, not a failure; next test November 9 |
| Treasury par curve [Treasury, November 5] | 3M 4.17, 2Y 4.46, 5Y 4.59, 10Y 4.84, 30Y 5.25 | 4.21, 4.58, 4.69, 4.90, 5.28 | Rally led by the front end |
| Gold, DXY, USD/JPY (vendor closes) | 4,113.5 +0.99%, 101.55 +0.04%, 158.36 −0.07% | November 4 | No dollar scramble |
| MOVE (vendor) | 97.92 +4.30% | 93.88 | Rates vol up a little |
| PFF, PGX, AT1.L (vendor) | −2.02%, −0.90%, −0.12% | November 4 | Bank-capital paper weak but not disorderly; AT1.L London close |
| Bond funds (vendor) | HYG −0.31, JNK −0.27, BKLN −0.68, LQD +0.15, SJNK −0.17, ANGL −0.32, BIZD −0.79 | November 4 | Funds fell far less than the +16 bp cash move implies; that gap may close |
| Banks (vendor) | GS −6.36, MS −5.94, C −5.04, JPM −4.19, BAC −3.62, WAL −4.24, KRE −2.46 | November 4 | Dealers hit hardest; equity, not funding evidence |
| Fed dollar swap lines | Trade date November 4: ECB $159M, BoE $10M, BoJ $2M | October 28: ECB $164M, BoE $5M | Ordinary size; predates November 5 |
| Commercial paper (FRED) | Nonfinancial 30-day 3.95 [November 4]; 2-month 4.15 from 4.09; financial 2-month 4.12 from 4.02; financial 30-day no row since before October 28 | Prior day | Predates November 5 and stale |
| OFR stress index | −2.162 [November 4], funding −0.123 | −1.484 [November 3] | Predates November 5 |

**This morning, tape 10:15 ET, not closes:** SPY +1.10%, VIX 24.09, ^TNX 4.876, ^FVX 4.666, DXY 102.17 +0.61%, gold −1.41%, HYG +0.05%, BIZD +0.68%, banks +0.4 to +2.4%. Yields and the dollar rose after payrolls.

### 15.6 Blind spots (unchanged, and they matter more now)

Cross-currency basis, swap spreads, prime-brokerage margin, repo haircuts and Treasury bid-ask are not reachable from this box. Commercial paper, the OFR index and swap lines stop at November 4, so they cannot show November 5. H.4.1 next prints November 12. Calm repo does not clear private or offshore channels. If leveraged funds were being squeezed on November 5, margin and haircuts would show it first, and those are the ones I cannot see.

ETF percentages are raw closes; yfinance's dividend file stops at September here, so an ex-dividend date inside the window is not ruled out.

### 15.7 MAIN 10-Q and the final Q3 BDC card (written 14:19 ET November 6)

10-Q accepted 11:46 ET November 6, accession 0001396440-26-000159. Figures are as of September 30, filing-primary.

| Metric | Q2 | Q3 | Change |
|---|---:|---:|---:|
| NAV per share | 33.92 | 34.22 | +0.88% |
| FV/Cost, 5,800,369 / 4,958,925 | 1.1551 | 1.1697 | +1.46 pp |
| Non-accruals, % fair value | 1.1 | 0.9 (3.5 at cost) | |
| Regular dividend | $0.265 monthly | $0.265 through December, plus $0.30 supplemental declared November | held |
| P/NAV, Q3 NAV on the 11/04 close of 57.62 | 1.718 (8/23 card) | 1.684 | |

The 10-Q does not contradict the release, so the card is **FINAL: no verdict line is met in full.** CONFIRM is closed on all three routes. REFUTE is not met: BXSL, GSBD and MAIN FV/Cost moved outside ±0.5 pt, GSBD non-accruals rose, and P/NAV fell on all six. MIXED is the nearest and is met in part only: GSBD marked down while MAIN and ARCC held, but FSK did not mark down (NAV −0.11%, FV/Cost up). No X1 half, no sizing, no fire. MIXED's letter routes names to REGINALD and CARL; asked of WALTER as INFO, marked partial.

⚠️ FV/Cost is composition-sensitive at MAIN too, with cost up $234.4M since December 31. My reading, not the filing's: a ratio above 1 mostly reflects holdings above cost, so this rise is weak evidence on debt marks.

### 15.8 WALTER card SIG-W-20261106-029, ACTION LIQUID (written 14:19 ET November 6)

Asked: read IREN's $6B target financing and Oracle's position under its offering price. Read at filings. No gate, level or count moved. IREN's call and Bloomberg's Oracle article remain unread.

**IREN (8-K EX-99.1 and 10-Q, November 5).**

| Fact | Figure, basis |
|---|---|
| Remaining planned FY27 capex from September 30 | $15B: $9B cash and committed; $6B target "subject to market conditions" |
| What the $6B is | GPU financing, prepayments, data center financing and other corporate level sources, "to drive future capacity targets" |
| What "fully funded" covers | Only the 0.3 GW program behind the >$4B ARR, and subject to funding conditions, escrow release and availability periods (note 5) |
| My sum toward the $9B, IREN does not itemize | Cash 3.522 + restricted 2.256 + undrawn GPU 1.0 of 1.657 + undrawn GPU 2.0 of 1.500 = $8.935B, before prepayments not yet received |
| Size against equity | $6B = 65% of about $9.18B market value (424.36M shares [October 30] × $21.63 Yahoo intraday 14:15 ET) |
| At-the-market | About $3.7B of $6B used through October 30, about $2.3B left on this supplement; the board can raise it |
| Cost ladder | GPU 1.0, Microsoft-backed: SOFR+225 and 5.96%. GPU 2.0: 9.0%, 30-month amortization. GPU 3.0: 9.51% |
| Dated term | GPU 2.0's $1.5B is available through December 31, 2026, funded on GPU acceptance at Mackenzie |
| Commitments | $18,947M, from $13,810M at June 30; some cancellable with charges |
| Debt principal | $10,041M: $8,061M recourse (derived), $1,980M non-recourse; converts $6,746M mature December 2029 to December 2033 |
| Quarter cash | Operations +$529M, investing −$5,146M, financing +$2,779M; cash plus restricted −$1,838M |
| Covenants | Compliant September 30. Guarantees carry no financial maintenance covenants; GPU 2.0 cross-default on payment; GPU 3.0 cross-acceleration above $500M |

**So what.** Nothing here shows financing refused, and the $6B is not the money behind the $4B run-rate; WALTER's "weeks, not lost" reading holds. The open part is that 40% of the plan has no commitment behind it, and it is too large for equity alone at this price. GPU paper outside the Microsoft contract has cost 9.0% to 9.51%, against 5.96% on the Microsoft-backed notes. IREN also says it may commit to GPUs before arranging financing, in some cases before signing customers.

**Watch, my inference:** IREN blamed "supplier timing" in part, and GPU 2.0's undrawn $1.5B ends December 31. The filing does not say Mackenzie is affected. Separately, Microsoft's change extends delivery dates without delay credits, with fees, credits and cost reimbursements still under discussion, and $525M of USPP tranche 3 sat in escrow at October 1, bearing interest. **Counterevidence:** a five-year contract with the customer prepaying 90% of GPU capex, and H100s at double earlier pricing, both company-stated after quarter end; 10-Q says liquidity is adequate for 12 months.

**Oracle (424B2, 424B5, term sheet November 2; 8-K November 4; release October 28).**

| Fact | Figure, basis |
|---|---|
| Equity | 86,206,897 shares at $116, about $9.9B net, closed November 4 |
| Notes | $10B closed November 4. Spread to Treasury at pricing: +240 (2029), +275 (2031), +305 (2033), +310 (2037), +335 (2046); yields 7.062% to 8.667% |
| Ratings in the term sheet | Baa2 negative, BBB− stable, BBB stable, "expected", November 2 |
| Index on pricing day | BB 206, BBB 117 OAS [November 2, first-published]; a different basis from a new-issue spread |
| Closes against $116 | 126.19 [November 3], 123.73 [November 4], **115.16 [November 5], −0.72%** |
| November 6, Yahoo intraday, not a close | Low 109.21, −5.85%; 115.33 at 14:15 ET, −0.58% |
| Debt | $125.3B actual, $135.3B as adjusted [August 31 base]. Not reconciled to the ~$160B S&P July figure in `ORCL_FALLEN_ANGEL_MAP.md` |
| Company lock-up | 60 days from November 2, to about January 1, 2027, with carve-outs including up to 5% of shares for acquisitions |
| Oracle 5Y CDS, DTCC | Disseminated 292 [November 4] to 305 [November 5]; converted 290 to 311, last 306 at 21:47Z. Converted figures are approximations |

**So what.** Being under $116 has no contractual effect: this is plain common stock, and a term search finds no reset. It matters for the next raise, and there is meant to be no next raise. On October 28 Oracle committed to limit new capital-markets money for FY27 to FY30 to $20B, $10B equity and $10B gross debt, excluding refinancing, on top of the $20B at-the-market raise. By November 4 both halves were closed, in 7 days. So its stated plan has no new public money left through FY30. What remains is what it named: vendor financing, customer-provided hardware, customer prepayments, then positive free cash flow from the second half of FY28. Any extra public raise would break a one-week-old pledge, so that is the fact to watch.

CDS rose 13 bp on the disseminated basis in the session the stock fell 6.9%. That is above the 288 bp [October 15] that card 029 cites. The "3.25%" claim is unsupported through November 5, but the November 6 file publishes about 20:15 ET, so today is untested, not refuted.

**Gates.** 072: Oracle is the issuer already scored, so its wide pricing is no new instance. Its pricing spreads are all above BB OAS, on different bases. 069 L5: the term sheet shows no R1 as of November 2; agency primaries remain inaccessible and nothing after November 2 is tested. Secondary bond levels are unmeasured here, since TRACE is not reachable.

**Later note, 15:27 ET, card SIG-W-20261106-034.** WALTER corrected card 029: Reuters, citing Bloomberg, places the Oracle wind-down inside "a larger reassessment of billions of dollars in cloud partnerships". Nothing in this section used the "older capacity" framing, so nothing here is withdrawn. One line gains a caveat: "weeks, not lost" rests on company statements, and Microsoft is IREN's customer as well as Oracle's. No source names IREN, and the review's size and direction are unknown, so I read no change to IREN; a wider review reaching that contract would change the read. Logged to KB-LIQ-153. No gate moved.
