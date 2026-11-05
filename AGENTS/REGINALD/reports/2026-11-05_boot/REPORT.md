# REGINALD: Will-authorized catch-up, 2026-11-05 (Thu, 10:30 ET onward)

**Authority:** Will in the PROME window 10:30 ET, verbatim "open Vulcan and REGINALD. Drain your whole inbox and bring your files current to live data inside your approved workstreams." No trades, and no change to any level, operator or consequence on a gate or frozen letter. **Runtime:** Claude Code, Opus 5.5 (`claude-opus-5-5`), desktop `DESKTOP-BC6EF81`, session `aa57a6c2-03d6-41de-aeb0-61ed5ff2c9e5`. Tools used: Bash, Read, Write, Edit, SendMessage. FFIEC JWT live on this desktop (own pull 10:33 ET). MCP `definite` and `mtnewswire` failed to connect, not needed. Pull refused: other desks' dirty tracked files (AEOLUS); local 52 ahead, 0 behind origin at boot; no stash, no reset. $0. No score, threshold, prediction, probability, position or trade change.

## 1. Bottom line

| Row | Result |
|---|---|
| **L895** FFIEC Q3 short-list tail | **DONE.** All 4 filed. 138 of 138 live charters on the list. 6 flags, unchanged. Frozen universe borrowings −$6.54B net (was −$5.70B), deposits +$32.70B (was +$39.20B). Concentration verdict still waits for the FDIC posting |
| **L516** Nano Banc P&A | ★ **POSTED TODAY** (FDIC page "Last Updated: November 5, 2026"), read in full. **The schedules that would settle the allocation are REDACTED.** 0.85% premium and no loss-share confirmed. Shared figure ≈ $120M ≈ 17% and the 32–42% scenario UNCHANGED. WAL O1 not answered |
| **L521** VLY Q3 10-Q | **NOT FILED** at SEC at 10:33 ET. Nothing to grade; the six asks stay owed. Row date 11/09 stands |
| **L763** OZK 10-Q attribution | **NOT FILED** at FDIC at 10:36 ET (FLNG rc 0, nothing after id 12022). EDGAR is the wrong route. −$313M stays one named migration plus ≈ −$207M un-itemized. Q3 Call Report adds: `RIAD5409` flat, OREO +$127.9M |
| **CREED-T-01a** bank read | **Bank transmission NOT established.** REG-T-07 NOT FIRED (12.33 vs >15 ×3), 2.67pp below. Overlap is metro-level only, no loan-level link. Exit-rail CMBS leg run 0 |
| **REG-T-04** vs HY 332 [11/04] | **NOT FIRED.** 18bp below strict >350, run 0 of 3. Today's selling is not in this print |
| **GATE-TERRY-ROLL70-EXIT** | **Recommend RETIRE, not re-grade.** A re-grade would still read 0 of 3 through 11/04. Not changed |
| FL frame (L227 bank leg) | **Three of four names now final HOLDS (SBCF, SSB, AMTB).** NO TRANSMISSION line reached on A3 (H = 3, T + m = 1); BKU's 10-Q cannot flip it. Label stays PROVISIONAL until BKU files, per §5 |
| Inbox | 3 general + 18 WALTER drained; 19 BOARD rows (18 + −009); WAL channel ACK; corrections 0 |

## 2. L895: short-list tail (WQ-184 lineage, frozen rule sha256 verified 10:31 ET)

**Instrument:** `scripts/borrowing_shortlist_ffiec.py`, run 10:33:05 → 10:36:37 ET, rc 0, route check passed on all 14 cohort banks. The laptop's cache does not exist on this desktop, so **all 138 were pulled fresh**, which also serves as an amendment test. Line-by-line diff against the 10/31 file: **0 of 134 rows changed, 4 rows added.** Output to a NEW dated file; the 10/28 and 10/31 files are untouched. `apply_frozen_2026-10-31.py` re-applied unchanged.

**Files:** `domain/sources/2026-10-28_boot/borrowing_shortlist/borrowing_shortlist_Q3_2026-11-05.md` · `apply_frozen_2026-10-31_rerun-2026-11-05.txt`.

| Bank | Assets 9/30 | Borrowings 6/30 → 9/30 | Deposits Q3 | Frozen flag | Read |
|---|---|---|---|---|---|
| **HSBC Bank USA** | $163.4B (−5.6%) | $7.17B → $6.34B (−$831M, −11.6%) | **−$7,693M (−5.4%)** | No: borrowings fell | Largest deposit fall on the list by more than 4×; brokered about flat at $21.41B. ⚠️ HSBC USA Inc 10-Q (acc 0000083246-26-000028) explains its YEAR-TO-DATE decline as lower affiliate and commercial deposits, including withdrawals from "a few large corporate clients". That sentence compares with 12/31, so it is not a Q3 attribution. Balance sheet shrank with deposits; nothing here is a borrowing lead |
| **East West Bank** | $85.6B (+1.5%) | $4.44B → $4.62B (+$183M, +4.1%) | +$1,347M | No | Under both bars |
| **Beacon Bank & Trust** | $21.8B (−1.7%) | $0.69B → $0.47B (−$212M, −30.9%) | −$202M | No | Borrowings fell |
| **First Hawaiian Bank** | $23.8B (+0.5%) | $0.020B → $0.037B (+$17M, +83%) | +$49M | No | Passes the 25% bar, fails the $100M bar, deposits up |

Own 6/30 FFIEC route check on these four: borrowings and deposits equal FDIC on all four, including 031 filer HSBC.

| Set | n | Borrowings | Deposits | Prior (10/31) |
|---|---|---|---|---|
| **Frozen universe: small commercial, ex probable acquirers** | **131** | **−$6.54B** (gross +$13.64B / −$20.18B) | **+$32.70B** | n=127, −$5.70B, +$39.20B |
| Increasers | 53 of 131 | top-10 share 63.0% (⚠️ a LIST figure, not the frozen measure) | | 51 of 127, 64.0% |
| Probable acquirers | 4 | unchanged | unchanged | Santander, Prosperity, Arrow, Sunwest |
| Reconciliation (a check, not a gate): list incl. acquirers, Webster netted vs H.8 NSA +$4.3B | | **−$0.14B**, gap $4.4B, inside the $10B line | | +$0.70B, gap $3.6B |

**Flags: 6, unchanged, same banks** (Regions, Renasant, Simmons, The Bancorp, Bank of Hawaii, Israel Discount NY), each already read at the issuer 10/31 as a funding-mix shift. **Concentration verdict: not computed.** FDIC BankFind index still dated 2026-08-19, 0 rows at REPDTE 20260930 (10:36 ET), so `borrowing_screen.py` stays refused. **TERRY: no packet;** the rule routes only after a CONCENTRATED or MIXED verdict. The remaining unfiled entry is Webster, which no longer exists (merged into Santander 8/20).

**So what:** adding the two big banks moved the read further the same way. Among banks holding 75% of small-bank borrowing, borrowing fell and deposits rose in Q3.

## 3. L516: Nano Banc purchase-and-assumption agreement

**Check:** failed-bank page 200, "Last Updated: November 5, 2026", new link `/bank-failures/purchase-assumption-agreement-nano-banc-irvine-ca.pdf`. Retrieved 10:38:52 ET: 87 pages, 8,157,719 B, sha256 `a3d23553cccd44c0fbf2c5579ba5db83f2a08f95efe573725f3c01fa5a4c5d33`. The PDF is not committed (URL and hash are the pointer, CREED's Trepp pattern); extracted text → `domain/sources/2026-11-05_nano-pa/nano-banc_PA_text.txt`. Text extraction returned empty schedules, so pp. 61–62, 66–67, 71–72 and 74–75 were rendered and read as images. **Redaction is the FDIC's.** No attempt was made to read beneath it.

Each L516 READ question graded separately, as DEWEY's 10/14 boundary memo said it must be:

| L516 question | Answer at the P&A | Token |
|---|---|---|
| Which assets Sunwest bought (~$476M) vs the receiver kept (≈$215M) | Schedule 3.1(n) "Acquired Assets in Optional Loan Pools": **2 pages fully redacted**. Schedule 3.1(a) marketable securities: redacted | NOT-DISCLOSED |
| Pool sizes, and which pool is Pool A / D | Pool descriptions sit in the bidder Information Package ("Optional Loan Pool" definition, §1.3); names "may not reflect the quality or nature" of the assets | NOT-DISCLOSED |
| $97.1M held-for-sale pool | No mention. Schedules 3.5(l) and 3.5(s) (Other Excluded Assets) redacted | NOT-DISCLOSED |
| Purchase discount | Schedule 3.2(j): optional pools "As set forth on the Bid". Non-pool loans at Book Value. Confirms the bid summary is the price record; adds no new price | CONFIRMS, nothing new |
| Deposit premium | Art. VII: **0.85%**, on all Assumed Deposits including reciprocal, **excluding Schedule 7** | VERIFIED |
| Premium base | Schedule 7 excludes DTC-brokered (offered as an option) and listing-service deposits. No non-DTC brokered. **Amounts redacted.** So the $5.1–5.3M premium stays an upper figure ("≤") as the 10/9 report stated | VERIFIED direction, dollars NOT-DISCLOSED |
| Loss-share | "Basic P&A, All Deposits"; no loss-share term anywhere in the text | VERIFIED: none |
| Other real estate | Schedule 3.1(o): NONE | VERIFIED |
| ~$81M deposits gap (≈$22M residual) | Not answered; Schedule 7 final numbers "provided post-closing" | NOT-DISCLOSED |
| WAL O1 (Nano's four deeds of trust) | No loan named | NOT ANSWERED, branches stay open |

⚠️ **One small inconsistency, unexplained:** the bid summary's "Optional securities pool: Yes" sits beside Schedule 3.1(c) Optional Securities: "NONE". Securities may be under the redacted 3.1(a); not established.

**Shared figure: ≈ $120M ≈ 17% of $690.9M (9/22 base) UNCHANGED, and the ≈ $70–90M ≈ 32–42% retained-pool scenario UNCHANGED** (direction VERIFIED, magnitude INFERRED, a desk scenario, not an allocation). The reconstruction's two brackets for Pools B + C ($199.5M to $227M) cannot be narrowed. L516's premise that this document "SETTLES" the allocation is false for the public version.

**Disposition for PROME:** the POSTING question is closed. Weekly check stops. What remains open moves to the rows that can still print it: L515 (FDIC disposition, check-by 2027-06-25), L517, and the Fed OIG Material Loss Review (~3/25/27). Claims bar date 2027-01-20 unchanged. An unredacted schedule would need a records request: an external send, Will's call. **I do not recommend it now:** the shared figure moves no gate, and the sale print at L515 is the better evidence. Offered, not requested.

## 4. L521: VLY

SEC submissions checked 10:33 ET: no 10-Q and no 8-K since 10/26. The 11/01 Call Report leg stands. The six asks (report 11/01 §1d) stay owed. CHECK-BY 11/10 stands; the 11/09 row date is PROME's estimate. Nothing graded.

## 5. L763: OZK attribution

**Route:** OZK files with the FDIC, not the SEC, so EDGAR silence proves nothing. `AGENTS/OZK/scripts/flng_watch.py` rc 0 at 10:36 ET: 184 filings, schema and coverage OK, none after id 12022 (Q3 8-K bundle, 10/20). **Q3 10-Q not filed at that time.** Q3 10-Qs were filed 11/5/2024 and 11/5/2025, so it may land today. The OZK desk owns this row.

| −$313M special mention ($616M → $303M) | State | Basis |
|---|---|---|
| Named migration | Boston land $105.9M SM → substandard accrual | OZK Q3 MC Fig 23, OZK desk 10/21 |
| Remainder ≈ −$207M | **UN-ITEMIZED.** Upgrade, payoff or other: not attributable before the 10-Q | Q3 Call Report cannot help: no risk-grade schedule |
| RaDD reserve | Not disclosed; pass by elimination, INFERRED by the OZK desk | OZK STAGE-2 read |

**Call Report, own FFIEC pull 11/05 (RSSD 107244), for OZK's own tests, not graded here:** `RIAD5409` YTD **$42,437K at 6/30 and $42,437K at 9/30**, so the Q3 increment is **$0**. OREO `RCON2150` **$288.1M → $416.0M (+$127.9M)**, against the $420M the release reports (a bank-level vs company-level difference is possible; not reconciled). OZK's check-by for the `RIAD5409` line is 11/16; the figure goes to the OZK channel. The row's "same day the FFIEC JWT expires" note is stale: expiry is 2027-01-31.

## 6. CREED-T-01a: the bank-exposure review (WALTER -001 ACTION REGINALD; CREED packet 11/05)

**Fact:** Trepp October office 12.33% after September 12.16%, fired effective 11/2 (CREED primary read). A return, not a record (January 12.34). Will ruled S1 3 → 4 in CREED's window 10:32 ET; that score is CREED's.

| My instrument | Reading | State |
|---|---|---|
| **REG-T-07** office DQ >15 ×3 | 12.33 [Oct], primary via CREED | **NOT FIRED**, 2.67pp below, sustain 0. The bars diverge deliberately |
| Exit rail, CMBS flows | Office DQ rose +17bp; office new-delinquency dollars not printed by Trepp | Leg needs 2 negative prints: **run 0**, UNREAD at new-delinquency grain |
| REG-01 (>10% through 2026) | 12.33 | On track, not resolved |
| Bank tier leg (CREED-T-03 / L514) | FDIC Q3 QBP ~late Nov | Not graded |

**The +17bp is not acceleration evidence** (CREED KB-095: $384.29M Wilshire Courtyard likely a round trip, CREED inference). I adopt the caveat, not a stronger read. **Mechanism readings moved mixed:** maturity-adjusted 9.66 → 9.56, foreclosure 2.90 → 3.12, performing matured balloon 1.64 → 1.69.

**Metro overlap against bank exposure.** ⛔ These are CMBS loans, not bank-held. No filing or Trepp text links any cohort bank to any of these loans. Overlap below is geographic only, so it is a place to look, not a transmission.

| Metro (CREED/Trepp) | Cohort exposure on file | Basis and date | Read |
|---|---|---|---|
| **Los Angeles** | OZK RESG commitments $1,490M; OREO LA land $54.5M, Santa Monica office $40.8M | OZK GEOGRAPHY, Q3-26 | Largest overlap. Already recognised as OREO. Nano's book (SoCal) is a separate n=1 |
| **Chicago** | OZK $654M | OZK GEOGRAPHY, Q3-26 (−42.1% since Q1-25) | Shrinking. OREO life sci $47.5M |
| **Washington DC / N. Virginia** | EGBN office $534M (VA 45%, MD 32%, DC 22%); OZK $983M ⚠️ Q1-25 vintage | top-3 report 9/26, Q2 data; EXPOSURE_MAP | EGBN office is largely recognised (criticized $287M → $77M); EGBN's live problem is multifamily. Not re-measured today |
| **Tiburon CA** ($210M Cove, MF) | SEARCH-NOT-FOUND in my cohort files | grep of cohort reports | Trepp: may revert if a six-month extension is granted |
| **New Orleans hotel** | SEARCH-NOT-FOUND | same | WAL hotel franchise criticized $75M → $185M is national, no link |

**Verdict:** the fire raises nothing at bank level today. **Unknown that gates this:** no Q3 office-by-metro bank data exists in Call Reports, and the FDIC QBP (~11/25) plus L180 at the 11/07 run are the first real tests. SLOOS October tightening (CREED KB-101, direction only) is S3 context, not an input here. **Kernel:** I am the named verifier on `PRED-CREED-001`; nothing is asked of me yet. Spot-check of its condition against CREED's record: 12.16 [Sep] and 12.33 [Oct] consistent with WALTER -001; I did not re-render the Trepp PDF.

## 7. HY 332 [11/04] against REG-T-04

Own FRED fetch 10:3x ET, agrees with WALTER -009 (15:08Z): **HY OAS 332bp [11/04]**; 340 [11/03]; 343 [11/02]; 344 [10/30]; 326 [10/29]; 314 [10/28].

| Row | Letter | Reading | State |
|---|---|---|---|
| **REG-T-04** | >350, 3 consecutive closes | 332 | **NOT FIRED, run 0 of 3, 18bp below** (5.1%). Peak this cycle 344 [10/30], so it has never crossed 350 |
| REG-T-03 | >320 ×3; exit ≤300 ×5 | 332 | FIRED, no re-fire, exit run 0, 32bp above exit line |
| CCC/HY `VX-REG-18.04` | >3.6× | 3.91× (CCC 1,297 / 332) | HARD-FIRE continues. CCC −19bp, HY −8bp: ratio rose on HY tightening, not a CCC-led re-cross, **NO escalate** |
| HY exit rail <260 | review only | 332 | NOT FIRED |

WQ-512 single-issuer rider: not triggered (fires only at a REG-T-04 fire). Bank cross-check not re-run (needed at a fire); last BANK-ABSENT ~0.7 [10/22]. LIQUID's "BROADENS" tier call (WALTER -076) is LIQUID's.

⚠️ **Two things the 332 does not show.** (1) It predates today: at 10:31 ET, vendor quotes not closes, SPY −2.4%, QQQ −4.4%, VIX $22.62, HYG −0.35%, and the 11/05 HY print arrives ~11/06. Earliest possible fire is the third close of a new run; 11/11 is a bridged non-session. (2) **B-tier OAS is back above my 330 ORANGE row since 10/29** (first crossed 10/16, back under 10/27): 332, 360, 363, 362, 351 [11/04]; BB 199. TRADE.md lists "B-tier holding >300 into >330" as one thing that would make this a credit bet. It is a watch row, no trigger, and the other credit legs have not moved.

**At 10:31 ET regionals were not trading with the selloff:** vendor KRE $74.68 (+0.74%), OZK +0.85%, EGBN +0.96%, WAL −1.51%. Not settled, no cause inferred. ⚠️ **Overtaken by 11:36 ET, see §14.**

## 8. GATE-TERRY-ROLL70-EXIT: re-grade or retire

**Recommendation: RETIRE. PROME owns the row; I changed nothing.**

| Fact | Source |
|---|---|
| State cell reads LIVE, "exit 0/3 through 10/9 close $74.27"; `last_checked` carries PROME's 10/30 read of 10/27–10/29 | GATES.tsv row 16 |
| Card DEAD: "written off, tracking stopped; holding UNKNOWN" (Will 10/29, "all dead") | TERRY TRADE_BOOK L97, setups/INDEX, SETUPS.tsv |
| Consequence: TERRY builds a close-out proposal for Robinhood WAL Dec-18 70P ×1 | row condition |
| review_by: "the guard dies with the position" | row |
| My log, the actual grade: **46 rows through 11/04, run 0 of 3**; 11/03 $76.77, 11/04 $79.24 (Yahoo and Nasdaq agree) | `registry/REG_T02_EXIT_LOG.tsv` |

**Why retire:** the consequence has no live recipient, because TERRY stopped tracking the card. A re-grade changes nothing: same 0 of 3, and WAL needs +3.35% to reach even the first qualifying close. **Nothing is lost:** `REG-T-02` stays live at this desk, graded every settled close, and an exit is still announced to WAL and PROME. The Fidelity WAL Dec-18 70P ×2 and 65P ×4 were never under this gate (TRADE.md §2), both visible on the 11/5 capture.

⚠️ **The one caveat that survives:** Will's word was a write-off, not a close. TERRY's interim postmortem says so, and Robinhood has not been captured since 9/29, so the contract may still exist (TERRY PB-0006 stays OPEN). Retiring the gate means that line, if it exists, runs with no exit guard. The 12/04 time stop dies with the card too. That matches "tracking stopped", but it is Will's to know. If he wants the line tracked, the fix is a card, not this row.

**Correction to carry:** TERRY's 11/5 postmortem says the REGINALD exit "was last graded 0 of 3 through 10/9, so its record stops 27 days ago". That describes the gate's state cell, not the record. The log never stopped.

## 9. Florida frame: 10-Q cells (frozen 9/24, Amendments A1–A3, unedited)

10-Qs read at SEC 11/05: SBCF 11/04 (acc 0001628280-26-070242), SSB 10/30 (acc 0001193125-26-439976), AMTB 11/03 (acc 0001734342-26-000088). **BKU not filed at 10:33 ET.**

| Name | Cell | Q2 | Q3 | Bar | Cell |
|---|---|---|---|---|---|
| **SBCF** | CRE + construction 30–89 accruing (primary) | $7.09M (60–89 $1.02M) | **$7.24M** (30–59 $5.67M, 60–89 $1.57M) | ≥$12.48M and 60–89 ≥$3M | **HOLDS** |
| SBCF | CRE + construction nonaccrual | $43.42M | **$33.14M** | >$55.8M | **HOLDS** |
| SBCF | Criticized + classified | 2.88% | 2.90% | ≥3.20% | HOLDS (10/28) |
| SBCF | Residential nonaccrual (sub-read, EXCLUDED) | $28.6M | **$27.37M** | >$36M | Build stopped |
| **SSB** | Classified accrual share | 86.7% | **86.4%** ($2,089.7M classified, $284.3M nonaccrual) | falls ≥5pp | **HOLDS** |
| AMTB | SFR nonaccrual rate (sub-read, EXCLUDED) | 1.60% | **1.44%** ($31.08M / $2,159.7M) | ≥1.80% | Not building |

All pools summed for SBCF (portfolio + acquired non-PCD + PCD), Q2 basis. Total accruing past due ties: $27.45M vs the release's $27.4M. SSB classified from XBRL (Commercial segment, substandard $2,089.445M + doubtful $0.282M).

| Name | Class | Status |
|---|---|---|
| AMTB | HOLDS | FINAL |
| SSB | HOLDS (P NCO 9bp, T = 0, all cells read) | **FINAL 11/05** |
| SBCF | HOLDS (P HOLDS, T = 0, all cells read) | **FINAL 11/05** |
| BKU | HOLDS-PENDING-P | 10-Q unread |

**Aggregate (A3): H = 3, T = 0, m = 1, so T + m = 1 < 2: the NO TRANSMISSION line is reached. BKU alone cannot reach two TRANSMITS.** §5 and A2.4 hold the FINAL label until all four are read, so it stays PROVISIONAL, by the frame's own text. No CORAL/PROME trip (needs two TRANSMITS). **Exit rail recognition leg (1):** on track to be met; legs (2) L180 and (3) REG-03 remain open.

**Two evidence limits closed:** SBCF's $8.4M reserve is a measurement-period adjustment on an acquired loan found to be PCD as of the 10/1/2025 acquisition date; it sits in CRE non-owner-occupied (10-Q ACL note). The past-due rise was not CRE: CRE + construction is about flat. **REG-27:** SSB NPL = $284.3M + $10.6M accruing 90+ = $295.0M, matches the release basis (0.57%); not met, row OPEN, unchanged.

## 10. BaaS perimeter: CCB Q3 10-Q (filed 11/05, acc 0001437958-26-000082)

Partner valuation allowance $45.6M, from $46.0M, "substantially support[s]" the initial allowance; the $22.8M specific provision stands; one unnamed partner. If the partner fails its obligations the bank "could be exposed". $6.29B of CCBX deposits swept off balance sheet at 9/30. **The 10-Q does not name Bluevine and gives no partner-concentration percentage**, so the release's $452.4M stays the figure. Q3 net charge-offs $49.9M, 4.43% of average loans (5.37% a year earlier); the 10-Q credits efforts to improve CCBX credit quality. No gate, threshold or trade (WQ-228). CASH and GDOT still no filing at SEC since 10/26.

## 11. Tape and registered grades (settled closes, Yahoo and Nasdaq agree, retrieved 10:36 ET)

| Name | 11/03 | 11/04 | 11/05 | State |
|---|---|---|---|---|
| WAL | $76.77 | **$79.24** | $78.05 vendor 10:31 ET, NOT graded | REG-T-02 FIRED, exit 0 of 3, log 46 rows |
| KRE | $72.88 | **$74.13** | $74.68 vendor | REG-T-01 UN-FIRED, $14.13 above line |
| FLG | $10.54 | **$10.96** | $10.86 vendor | Ladder RED, 20 settled closes below $11.39. Ladder check exit: ALERT (via boot.py), state unchanged |

Claims **189K** [w/e 10/31], first print on my read; 111K of buffer. VIX 16.61 [VIXCLS 11/04] then $22.62 vendor. SOFR−IORB +4bp [11/04], +7 [11/03]. DGS10 4.95 [11/03]. FDIC failures CSV re-pulled 10:36 ET: **6 in 2026, unchanged.** H.4.1 due today ~16:30 ET and H.8 11/06: not yet read. FHLB CFR 11/13.

**Insider, SEC Form 4 via boot:** CUBI open-market sales 11/02–11/04: Sidhu 50,000 at $87.40, Way 48,796 at $83.88 + 723 at $85.16, Watkins 5,500 at $86.17. Three reporters in three days, observation only, no credit inference. FLG director buy 10,000 at $10.14 (known).

## 12. Intake

| Lane | Items | Disposition |
|---|---|---|
| PROME L891 Brent citation | 1 | DONE: STATUS Brent row now names BRENT as owner; caveats kept |
| WAL Q3 extraction | 1 | ACK in channel, no change; the figures are inputs to the 11/07 run, WAL's item-4 basis is not my cross-bank denominator |
| CREED T-01a | 1 | §6; reply packet sent |
| WALTER action | 2 (-001, -042) | INTEGRATED |
| WALTER info | 16 | All INFO_ONLY per BOARD_LOG; none moves a figure |
| BOARD diff | -009 read beyond the lane (names REG-T-04) | INFO_ONLY, logged |

Ueno (Paraguay): no US exposure established; nothing in this desk's perimeter. Capital One modified-card cohort: not relayed as a class signal; GIBBS and CARL own. BoE +25bp to 4%: context.

**Book truth (11/5 capture, intraday, Fidelity •1326):** all REGINALD-scope legs in TRADE §2 present, plus VLY 12P Dec-18 ×1 and FLG 10P Mar-19-2027 ×1 now listed. Robinhood not captured. No disposition inferred.

**Trade-idea route:** no candidate. L895 has no verdict; FL frame holds; T-01a is not a bank fire; REG-T-04 not fired. Recorded in TRADE §2b.

## 13. Not done, with why

- BKU, FLG, EGBN, VLY, CUBI, ZION, MTB 10-Qs: not filed at 10:33 ET.
- OZK 10-Q: not filed at 10:36 ET; re-checked before this packet.
- 11/07 run, L180, ranking test, Friedberg, reserve-release count, cohort-selection decision: scheduled, not pre-run. Desktop token and route now proven.
- `V1V3-ACCELERATE` rename: re-dated 11/07.
- NEXUS brief: a closeout step; held until PROME or Will asks for closeout.

## 14. Addendum 11:36 ET: the selloff reached banks (WALTER FLASH -20261105-017, ACTION REGINALD)

The 10:31 ET read above no longer holds. Vendor quotes 11:36 ET, not closes: WAL $76.79 (−3.09%), KRE $73.36 (−1.05%), ZION −1.52%, CFG −1.55%, FLG $10.73 (−2.10%), VLY −1.07%, EGBN −1.02%, SSB −0.83%, OZK −0.37%. SPY −2.71%, QQQ −4.34%, VIX $23.00. HYG −0.26%, ^TNX 4.84%.

**Read:** regionals are falling less than the market, with WAL the outlier. Cause not established; no bank filing or 8-K explains it, and FLNG and SEC checks at 11:35 ET show no new OZK, VLY, EGBN, FLG or BKU filing. **State:** WAL under $78 intraday changes nothing: REG-T-02 is already FIRED, a sub-78 close is a suppressed re-entry, and the row grades the settled close. REG-T-01 UN-FIRED. Credit proxies calm; no cash spread for 11/05 exists yet. LIQUID's REVERSES (-021) covers 11/04 only and says nothing about today.

## 15. Addendum 14:30 ET: bank-vendor cluster (CYPHER P1, 11/05)

**No consequence in this lane today; no score, threshold or gate moves.** Finzly (payments middleware) and Abrigo (Sageworks lending software) met CYPHER's count limb. No cohort bank is named in its record. SEC 8-K full text, 10/29–11/05: Finzly 0, Sageworks 0, Abrigo 1, a Colony Bankcorp exhibit filed 11/02 naming Abrigo as reserve-model provider, not an incident. **Not a clearance:** client lists are not public, an 8-K is filed only if material, and 10-Qs were not searched. **Re-judge on** a regional 8-K or a late 10-Q citing either vendor. CYPHER rechecks 11/09 and 11/12.
