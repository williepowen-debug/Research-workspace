# Digest reader C: 10 briefs (LABOR, FLG, ISHM, OTTO, SHADE, HOMER, AEOLUS, MARCO, WAL, YURI)

Reader: fresh-context, read-only. Written 2026-11-10 11:14 EST (from `date`). All 10 briefs were read whole. The baseline is NEXUS's last brief pass, 2026-11-04 ~15:37 ET. Figures are quoted as the briefs write them. Nothing here is computed by this reader, except the commit-order facts from `git log`.

## Pin check (`python3 scripts/brief_pin_check.py ... --quiet`, rc=0)
Summary line: `BRIEF-PIN 0 OK: 10 brief(s) — OK-PINNED 5 · OK-SAME-COMMIT 3 · UNPINNED 2`. A PASS proves the pin, never the content.

| Desk | Verdict | Detail |
|---|---|---|
| LABOR | ✅ OK-PINNED | ab3851403c = STATUS HEAD |
| FLG | ✅ OK-PINNED | a83cf06805 = STATUS HEAD |
| ISHM | ✅ OK-PINNED | 5f377f1a14 = STATUS HEAD |
| OTTO | ✅ OK-PINNED | f04e92eca7 = STATUS HEAD |
| SHADE | ⚠️ UNPINNED | No hash in the header. The brief commit 5b514d55e (11/6 17:23) is **BEFORE** STATUS HEAD 3ce339a84 (11/6 20:40, "SHADE: record WQ-644 A, X1 and T-SHADE-01 stay two named tests"). STATUS is one commit ahead on the same day, so this is the amendment-11 lag case. The ruling content is not in the brief. |
| HOMER | ⚠️ UNPINNED | No hash in the header. The brief commit a92a0b5b5 (11/6 07:59) comes AFTER STATUS HEAD a4cbc0c8b (11/5 18:39), so the brief is the last fold. |
| AEOLUS | ✅ OK-SAME-COMMIT | f908dc61e |
| MARCO | ✅ OK-SAME-COMMIT | fd6995b9f |
| WAL | ✅ OK-PINNED | fd153358d9 = STATUS HEAD |
| YURI | ✅ OK-SAME-COMMIT | 850427799 |

Last brief commits: LABOR 11/8 14:33 · FLG 11/7 11:10 · ISHM 11/6 20:42 · OTTO 11/6 18:23 · SHADE 11/6 17:23 · HOMER 11/6 07:59 · AEOLUS 11/6 07:44 · MARCO 11/5 18:22 · **WAL 11/4 18:13** · **YURI 11/2 08:55**.

---

## LABOR
- **HEADER:** As of 2026-11-08 14:32 ET. The 14:32 bump was a no-change re-bump; the data catch-up ran at 12:16 ET. STATUS pin `ab3851403c`.
- **VIEW:** Freeze-thaw v2 FIRED on 11/6, and the low-hire half of the "Hotel California" thesis stood down on its own kill rule. The low-fire half stands: claims are 189K and the JOLTS layoffs rate is 1.0%. The labour realization channel to credit is "still closed". The new tension is a headline hiring recovery against thin quality underneath (involuntary part-time +339K).
- **MOVED SINCE 11/4:**
  - Claims, graded 11/5 (DOL 11/5): initial **189,000** (w/e Oct 31), band B · 4-week MA **194,750** (−2,250) · CC **1,718,000** (w/e Oct 24 per the FORWARD row; "+23K, 32,000 under 1,750K"). v13 run 3, v7 run 8, record-only. R13-c graded 11/5 at 0.9886, no action.
  - Challenger Oct **43,994** ("lowest October since 2023"). v5 holds 4 because tech +21.5% blocks the demote by 0.0149.
  - Productivity Q3 **+3.6%** on hours +0.1%; labor share **53.0%**, a record low (BLS 11/5). Recorded, not attributed.
  - NFP October, BLS USDL-26-1632 11/6: **+165K** vs the +150K bar · Aug rev **+186K** · Sep rev **+60K** · 3-month avg `411/3 = 137.0K` · EPOP **59.3** (T-03 bar ≤58.6, not fired) · U-3 **4.1** · LFPR **61.9** · AHE **+3.1% YoY, $38.00** (Sep 3.0%) · involuntary part-time **+339K** · long-term unemployed **27.6%** (status line). Aggregate LF `170,683 − 170,078 = +605K` above May. Prime-age LF `142K` below May (was 624K at the August read).
  - **FIRES/GRADES:** 🔴 **Freeze-thaw v2 FIRED 11/6** (card §3d row 1). v4/v6/v7 stood down at a floor of 1; v17 2 → 1; **score 27 → 22/80** (floor of 1 ruled by Will 11/6, WQ-634 A). **LAB-19 ✅.** T-03, T-04, T-06, T-08, T-13 and Kill A **did not fire**. v8 counter 1 of 2 after the 11/6 net +84K revision. JOLTS Sep graded 11/5: Aug rev NET +96K, Sep P **+83K**, LEG C MET, v4 holds 2 (before the 11/6 stand-down). Layoffs rate 1.0% (Sep P, BLS 11/3).
  - Catch-up 11/8 12:16 ET: state claims breadth w/e Oct 31: **6 of 51** states up YoY; sum of states `176,301 / 213,752 − 1 = −17.5%`. **Florida 4-week avg 5,182 vs 5,583, −7.2% YoY** (ETA 539, pulled 11/8). WARN leads verified at state primaries. Staffing Q3: v14 re-arm NOT MET. Canada re-check #2: **NO EVIDENCE**. No score, band or gate moved: 22/80.
  - WARN (T-07): LayoffAlert Oct **22,453**, 27,547 below the 50,000 bar, not fired `[2ND]`. FL unemployment 4.4% (Sep).
  - New predictions registered 11/5: LAB-20 55% (Dec 3) · LAB-21 68% (Dec 1) · LAB-22 40% (Dec 31) · LAB-23 58% (Nov 20). LAB-24: "first to second fell ≥16K `22/44 = 50.0%`".
- **CROSS-DOMAIN / CALIBRATION:** Uncertain about (1) whether October hiring survives revision and whether involuntary part-time +339K was noise; (2) whether Sep JOLTS prelim flows and layoffs survive the Dec 1 revision; (3) how much of October's courier and temp gain is seasonal (not measured); (4) v7 has no return letter and v4/v6/v7 have no re-arm letter. Tensions: RED's soft-landing-via-supply frame "gained ground"; MARCO's supply thesis is "contested by the aggregate LF and survives in the prime-age cohort". Brier 0.348 over 13 rows; 0-for-6 at ≥60% on THRESHOLD calls.
- **FORWARD:** Thu **11/12** claims (card frozen 11/5; T-01 MA bound `X > 421,000`) · Tue **12/1** JOLTS Oct (NET ≤0 ⇒ v4 2→3 and LEG C lost; layoffs rate ≥1.2% ⇒ escalate CARL + REGINALD) · Thu **12/3** Challenger Nov (under +20% tech with the share leg held ⇒ v5 4→2) · Fri **12/4** NFP Nov (LAB-18 last draw, Nov EPOP ≤58.8 fires T-03; LAB-24: Oct <+150K ⇒ ✅).
- **NEXUS-NAMED (verbatim):** SENDING row to "CARL · HENRY · REGINALD · NEXUS · TERRY": "🔴 **Freeze-thaw v2 FIRED 11/6, card §3d row 1.** v4/v6/v7 stood down at the floor of 1, 27 → 22/80 (WQ-634 A, Will 11/6). ⚠️ Sep JOLTS preliminary, revises Dec 1; a lost LEG C leaves row 2, still fired. First print 15K over the bar; first to second fell ≥16K `22/44 = 50.0%` (LAB-24). Involuntary part-time +339K. No un-fire letter exists" · Mechanism: "The labor side of the chain has not broken: claims 189,000, layoffs rate 1.0%. This is a hiring read". Footer: "**Ratified by NEXUS ★8/07**".
- **FLAG: internally inconsistent, VIEW and CALIBRATION are partly stale against the header.** Size 18,679 B, under cap.
  - VIEW bullet 1 says "**The freeze holds**", but the header says the freeze thesis stood down.
  - VIEW bullet 3 says prime-age LF "**624K below May**"; the SENDING row (11/6) says **142K**.
  - CALIBRATION says LT-unemployed "27.0%"; the header says 27.6%. These may be different vintages.
  - CALIBRATION lists LAB-19 81% open and LAB-18 10%. The header says LAB-19 ✅ and SENDING says LAB-18 "now 5%".
  - CALIBRATION says "v7 dropped to 2 on 10/8"; v7 was stood down 11/6.
  - FORWARD still carries a 🔴 pending "Fri Nov 6" row beside the ✅ graded one.
  - NEXT DECISION "When" lists 11/9 Canada re-check #2, which the header says was already done 11/8.
  - Cite the header and SENDING rows, not VIEW or CALIBRATION.

## FLG
- **HEADER:** As of 2026-11-07 11:1x ET. STATUS pin `a83cf06805`. Thesis v1.0.5 (11/07).
- **VIEW:** 🔴. The $2.8B non-accrual book carries only a 5.5% specific reserve. The live signal is the reserve and the exit channel, not the 322.11% concentration ratio. Q3 cures jumped to 56% of outflow, cause undisclosed. The 2027 MF wall (MF $8,519M reprices or matures into the rent freeze) is the stress window.
- **MOVED SINCE 11/4 (Q3 10-Q read, v1.0.5 dated 11/07; the brief does not state the 10-Q filing date):**
  - **FLG-02 and FLG-03 HIT.** Direction unchanged. "Nothing is healing" withdrawn as a flat claim after Q3 cures of $144M. Rail re-derived, no condition changed.
  - Non-accrual **$2,817M** (9/30) · specific reserve **$155M = 5.5%** of non-accrual · **$1,548M carries no allowance** on management's collateral claim · total ACL **$869M** flat in Q3 · coverage **30.85%**, a series low (10-Q). The flat ACL hides MF + CRE reserve −$24M and C&I +$20M.
  - 9M gross formation **$1,053M** replaced 87.0% of outflow. H1 outflow: 87.5% payoff, 1.6% cure. Q3 *derived*: 29.7% payoff, **56.3% cure ($144M)**, class and cause undisclosed. MF criticized + classified **+$483M** in Q3.
  - **~$216M buyback in Q3** (derived). CET1 **13.16% → 12.38%**. Buybacks paused in Q4 and resume in 2027 (call).
  - SR 07-1 **322.11% at 9/30** (327.52% at 6/30; Call Report, FLG pull 11/01), down 12 straight quarters. NAL rate 4.90% → 4.55%. MF −3.56% in Q3; C&I +$2.0B in Q3.
  - Private-credit slice **$1,069M → $2,139M**; "~$0.5B recode from C&I open".
  - Q3 Call Report: MF 30–89 DPD **$233M → $392M (+68%)** (Q1 $676M, n=3, "watch, not trend") · bank net income **$34.5M → $12.1M**.
  - FLG-01 setup: H2 formation < $600M; Q3 $273M, so Q4 must be < $327M.
- **CROSS-DOMAIN / CALIBRATION:** Uncertain about (1) what the $144M Q3 cure was; (2) who finances buyers of exiting loans ("10-Q silent"); (3) par-basis loss at exit; (4) the Kenilworth v. RGB freeze ruling. Kill leg K-3 is **UNSET**, so no falsifier is held. Cross-agent tensions: "None active this cycle". Waits on REGINALD's 11/07 re-score: is FLG an outlier or the cohort's leading edge? The cure share cannot be base-rated against peers (FR Y-14Q is non-public).
- **FORWARD:** Rent-freeze merits ruling (T-12) "by Dec 31". Nothing else grades before the FY2026 10-K ~2027-03-01. Q4 Call Report ~2027-02-14.
- **NEXUS-NAMED (verbatim):** SENDING row "NEXUS | M-05 / R10 inputs: FLG RED [10/23]. Coverage 30.85% (10-Q) is a series low; specific reserve 5.5% of non-accrual | 🔴 | Named-regional CRE level fire stays lit; recognition row = reserve, not provision".
- Not stale. 6,409 B.

## ISHM
- **HEADER:** As of 2026-11-06 20:43 ET. STATUS pin `5f377f1a14…`.
- **VIEW:** 🟡. Physical equipment buying is well supported. The factory upturn is strong but slowing, and its durability is unproved. Is order strength end demand, or buyers locking in stock and prices?
- **MOVED SINCE 11/4:**
  - **R1 moved toward-real from CANNOT-FIRE to NOT-MET** on the original S&P October final (11/6). **R1 re-pointed to the November S&P final, 12/1** (WQ-643 A, 11/6 20:31 ET). "No flip fired, and no score, band, gate or threshold changed."
  - S&P Oct final **54.9** SA vs 55.9 Sep (released 11/2). Output and new orders both slower; new work slowest since March; output prices steepest since Sep 2022; lead times longest since Aug 2022; hiring steepest since April 2021.
  - ISM prices **75.2** from 77.9 · ISM employment **52.4** from 52.7 · "ISM <47 NOT-FIRED".
  - Class 8 Oct prelim: **ACT 13,500, −45% y/y** (dated 11/4) · FTR 15,600, −36% y/y, YTD 278,201, +74%. Both cite EPA 2027 uncertainty. J2 input, "no condition fires".
  - AAR week of Oct 31 **+3.0%/+3.9% y/y**.
  - Factory payrolls Oct first print **+19K** to 12,681K (LABOR owns).
  - Parker FY27 Q1 (11/5): rolling 12-month orders +13% vs +12%; organic +11.5%; backlog $13.7B (organic split NOT-STATED after the Filtration Group acquisition).
  - Computer imports Sep **+150.96% y/y**; Q3 +28.639% q/q (Census, read 11/6).
  - Scores unchanged: 18/35 raw, shared-root 13/25. Six `combo:` themes logged.
- **CROSS-DOMAIN / CALIBRATION:** Physical strength "can coexist with LIQUID credit/funding stress; financing transmission is not cleared by these prints". VULCAN owns the AI-capex verdict. The three J1 legs are not independent: BEA equipment includes imports, and ISM and S&P share one month. Survey-band recommendation: register none.
- **FORWARD:** 11/13 Cass Oct · 11/17 and 11/24 Fed G.17 Oct and annual revision · ~11/20 ACT Oct final · 11/25 BEA Q3 second estimate and durables Oct advance · **12/1** S&P final 09:45 ET (R1 two-branch grade) and ISM 10:00 ET (strict <47) · 12/2–12/8 rail, M3, FT-900. Deere date check 11/12.
- **NEXUS-NAMED:** none.
- Not stale. 7,590 B.

## OTTO
- **HEADER:** As of 2026-11-06 18:23 ET. STATUS pin `f04e92eca7…`. Thesis v1.6 (11/05, `4e765ec13`).
- **VIEW:** 🔴🔴 on fraud and recovery losses. **Both systemic-transmission legs DISCONFIRMED.** Convergence **32/50**, with 21 points from one root. The Invisible Exit conviction is LOW, and borrower exit is UNVERIFIED.
- **MOVED SINCE 11/4:**
  - s041 (11/05): THESIS v1.6. Carvana DORMANT, V5 2→1, **composite 33→32**. Borrower exit relabelled an unverified hypothesis. OTTO-34 50→85, OTTO-33 60→70. OTTO-36 and OTTO-37 registered.
  - Exeter Sep recoveries **19.14/15.70/21.04/26.51%**, 4/4 below 28%, EART 2024-1 re-crossed. **Re-fired 11/05.** "One month on small dollars; six-month means flat".
  - s042 (11/06): **OTTO-37 FALSIFIED**: Manheim Oct **206.8** vs 207.0, as-made 60%, Brier 0.36. Manheim +2% YoY, "hinge test not fired".
  - **MFIC: US Auto 0.40 to 0.11** (legacy workout stake). LendingPoint non-accrual is one loan, no auto link.
  - s043 close refresh: Tricolor auction 9,082 vehicles, **$63.09M net through 10/31**, "~3% stands". The trustee's $53.78M at 9/30 differs by $2.53M, unexplained.
  - Hertz 2021-2 **$1,000M at 9/30, was $2,000M**. No amortization event, not fired. All $300M of 2021-A Class B holders were replaced at 12.46%.
  - Court sweep 11/05: trustee Rule 2004 ~24 motions; Ares and AllianceBernstein on file as Tricolor lenders; US v. James moved to Judge Caproni; FB §721 granted 11/02. OTTO-33 70%.
  - s039 retired the mixed bank-loss aggregate ("No comparable current767M total").
- **CROSS-DOMAIN / CALIBRATION:** Deep pools are worsening while broad indexes are stable: "Ally YoY loss rate is nearly flat; KBRA broad nonprime DQ nearly flat YoY; Cox adjusted mid-month prices rebound". Forecast record 3/9, Brier 0.286 vs 0.25. Car-Mart is BROCK's to grade. WAL `AUDITOR_NEXUS.md` L20/L90 "now stale (WAL's to fix)". The HY/CCC credit read is LIQUID's. OTTO-11 is STUCK.
- **FORWARD:** BROCK CRMT 11/09 (Car-Mart tenth bridge expires) · James government response 11/09 · NY Fed 11/10 · Tricolor §341 11/11 · EART 2026-5 window 11/12 · Chu check ~11/13 · **SDT ~11/15** (expected NO VERDICT; OTTO decides whether to propose a redesign) · EART Oct 10-Ds ~11/30 (resolves OTTO-36) · Tricolor sales deadline 11/30 · Ares response 11/30 · Manheim Nov 12/07.
- **NEXUS-NAMED (verbatim, rows addressed to NEXUS):**
  - "WALTER · LIQUID · CARL · BROCK · NEXUS | s043 close refresh: Tricolor auction 9,082 vehicles, $63.09M net through 10/31, ties to the old figure at 4/30; Hertz 2021-2 $1,000M at 9/30, was $2,000M"
  - "REGINALD · NEXUS · PROME | s039 mixed bank-loss aggregate retired; original SDT commentary explicitly corrected"
  - "NEXUS · PROME | L708 remains NO_INSTRUMENT; earlier consumption settled | … No verified corporate-bond/rating/index/date join; supplemental equities MIXED cannot establish consumer attribution of CCC widening or absence of credit transmission."
  - "REGINALD · NEXUS · RED | LIQUID/PROME WQ524 historical First Brands → Point Bonita/SPV → WAL loss and lender response consumed | … not a newly disclosed bank or October funding spiral"
  - Further rows name NEXUS for Edmunds Q3, the s037 financing comparison, CPS coupons, EART closing-date correction, Ally Q3 and Exeter.
- **FLAG: over-long and degraded.** 15,813 B. Many cells have glued words ("current767M", "Q3 mean7107 aboveQ2 6884", "remainsUNKNOWN"), which violates the root Output Canon. The CALIBRATION section is mostly a session log. WAITING FOR still shows past dates (Oct 28/30, Nov 2/4) without results.

## SHADE
- **HEADER:** As of 2026-11-06T17:23:10-05:00. "STATUS commit: same commit as this fold". The brief is UNPINNED in fact, and STATUS has since moved one commit (11/6 20:40, WQ-644 A).
- **VIEW:** 🟠. Structural and latent insurer-wrapper stress; evidence remains partial. Vector #1 is single-name DLIC FIRING; composite 20/30 unchanged. A current liquidity crisis, illiquidity breach and cohort cascade are all unproven.
- **MOVED SINCE 11/4 (Athene/Apollo Q3 read, 11/6):**
  - AI funding (deck 10/30): **$12.9B funded 9/30, ~3% of gross invested assets**. The 10-Q adds SVF II Finco **$3,097M (+$1,033M Q3)** outside that total; Big Sky commitments $4.9B + $1.3B VIE; SoftBank-linked $4,846M; Oracle $2.4B. Funded **$16.0B = 3.8%**; with commitments **$22.2B = 5.2%** (a ceiling). "No loss on any AI position in a filing." Card 041 relabels SoftBank's $10B loan as not an OpenAI-share margin loan.
  - Secured funding 9/30: S2 **34.2% from 36.2%**; FABN **$32.6B**; FHLB **$29.9B drawn, $33.8B drawable**, room **$3.9B from $6.1B**; restricted **$120,089M = 28.80%** of investments; S1 ~$2.3B derived. "Canary ungraded until the deck, call 11/12."
  - Athene investment loss **$3,418M**: mortgage marks $1,875M, derivatives $1,399M, provision $82M, instrument-specific est. $33M. Mortgage 90+/non-accrual principal **$1,818M → $3,453M YTD** (ARI cohort not separated). Level 3 **+$14,877M**, "$123M under A1's confirm line".
  - **`T-SHADE-01` read 11/6: NOT MET.** 9/24→11/6 RAW wrappers +0.79%, managers +4.14%. Level MET on 30 sessions through 348 [11/5]. No dig.
  - **Falsifier F-SHADE-01 now written, test 2027-03-31.** BROCK 11/6: X1 CONCUR, two named tests (to Will via PROME). IREN Mackenzie loan: no insurer established as a holder.
  - AAIA Q3, the Q3 FI deck and DLIC Q3 were **not posted at 17:23 ET 11/6**.
- **CROSS-DOMAIN / CALIBRATION:** Funding aggregate "is not usable collateral or available cash" (LIQUID/REGINALD). Group1001 issuer affiliate **5895→4898M, −997M YTD, not completed-exchange proof**. DLIC up to 6.5B parent plan, approval/closing unknown. HY 331 [10/16] is "LIQUID's/RED's/REGINALD's instrument". The AHL contingent guarantee on the Broadcom/Anthropic WHCO project has an unknown base O.
- **FORWARD:** Athene call **11/12** (canary grade). F-SHADE-01 test 2027-03-31. Other dated items are not stated.
- **NEXUS-NAMED:** Every SENDING row is addressed to NEXUS among others. Verbatim, the lead row: "**NEXUS / VULCAN / SAM / BROCK** | **AI funding now sized at Athene, and the deck's total is not the whole book.**" and "**NEXUS / LIQUID / REGINALD** | **Athene secured substitution continued in Q3.**" and "**NEXUS / BROCK / RED** | **Apollo's GAAP loss is marks on issuer attribution; delinquency is the counterweight.**"
- **FLAG: degraded and partly stale.** 10,664 B. Many cells are glued ("ApolloQ2 Note17 p94: AHL guarantees15%…"). Several rows are still dated Q2 or 10/21–10/29. There is no VIEW/CALIBRATION/FORWARD structure and it is UNPINNED. The STATUS commit after the brief (WQ-644 A, 11/6 20:40) is not folded in.

## HOMER
- **HEADER:** As of 2026-11-06 07:5x ET closeout (data through 2026-11-05). UNPINNED. The brief committed after STATUS HEAD.
- **VIEW:** 🔴. The foreclosure pipeline is still converting but "the front door is narrowing". MF stress shows under calmer GSE headlines. Rates fell to 7.18% while demand kept falling. Builder compression is broad, not uniform. "Thesis 0/5 killed."
- **MOVED SINCE 11/4 (the catch-up dated 11/5 carries 10/26–11/05 data):**
  - **PMMS 7.18% [11/05]** (7.24 [10/29]); spread ~228bp (vs 4.90 Wed 11/04); **10Y 4.84% on 11/05**. Still RED (>7.0%), 0/4.
  - **Fannie MF serious DQ 0.62% at 9/30**, verified at the 10-Q 11/05. MF provision $446M vs $259M.
  - Freddie Q3 10-Q: subordination **0.80% on $302.6B**; MF provision **$115M vs $57M** YoY.
  - Trepp CMBS MF DQ **8.09% Oct** (+5bp), "likely" all from the $210M Cove at Tiburon loan (INFERRED). **HOM-05** registered: November below 8.09% at 55%.
  - ICE Sept 90+/FC **882K**, ORANGE (10/27). FC starts −2.9% YoY (first negative).
  - MBA purchase **−19% YoY** wk 10/30 · Redfin pending **−16.4% YoY** (4 weeks to 11/01) · Redfin median sale −0.4% YoY.
  - FMHPI +1.94% Sep, with Aug revised +2.19 → +1.91.
  - Builders: DHI FQ1 guide 18–18.5%. CRL-23: the DHI leg ≤17.5% is 50bp below the guide's low end, resolver 2027-01-19.
  - Q3 GDP residential investment −3.3%.
  - Non-bank servicers Q3: PFSI 60+ **4.2% vs 3.4% YoY**; UWM D/E 1.77x; RKT liquidity $11.4B.
  - WQ-596 predictions HOM-03–06 registered (HOM-03: Oct EHS below 3.90M at 60%). Thesis defects D2 and D4 closed, D11 logged.
- **CROSS-DOMAIN / CALIBRATION:** Uncertain about how far the Trepp MF rate falls if Cove reverts; whether the +9bp spread is timing or real; whether ICE will print the cure YoY; and the cause of the Fannie/Freddie share selloff (secondary sources). NV credit-card 90+ 16.28% (Q4-25) is "CARL's lane". Florida statewide is CORAL-owned. BOND carries 221bp for the 10/15 mortgage spread.
- **FORWARD:** Preferred Bank 10-Q ~11/09 (REGINALD's) · **NY Fed Q3 household debt 11/10** · **NAR EHS 11/12** (HOM-03 <3.90M; RED <4.0M) · Trepp Oct SS and ICE Monitor ~11/13 (did Cove revert?) · NAHB 11/17 (HOM-04) · Census NRC 11/18 · new-home sales 11/25 · **MBA Q3 NDS ~mid-Nov** (HOM-02 decider: FHA SA ≥12.00%) · **formal thesis grade 11/20** · Case-Shiller Sep ~11/24 · Trepp Nov DQ ~12/01–05.
- **NEXUS-NAMED:** none.
- Somewhat long (14,911 B), but not stale for its date.

## AEOLUS
- **HEADER:** Last writeback 2026-11-06 07:44 ET (bounded session WQ-626 A; vortex read through GFS 11/6 06Z and ECMWF 11/6 00Z).
- **VIEW:** **Composite 17/30, fired 1/6.** The Rhine (C5) fired on the 40/180 key, score 5. Vortex T1 fired 11/5 with no descent; C3 stays 2. C6 Colorado water is up and the deal is unsigned (Yellow). "Nothing here is a trade."
- **MOVED SINCE 11/4:**
  - **Rhine C5 FIRED**: Kaub 18.010 / 22.260 / 19.260 and Duisburg 161.427 / 154.427 / 151.802 (11/03–05). Key met in 3 of 26 years. Contargo Kaub top row €1,075 per 20ft (€550 on 10/28). "Not a proven traffic halt".
  - **Vortex T1 FIRED 11/5**: ECMWF −0.279 [11/5 12Z], +0.240 [11/6 00Z]; GFS −0.357 [11/6 00Z], +0.463 [11/6 06Z]. No reversal at 30/50/100 hPa. Forecast dip −2.20 on 11/12.
  - C6: Powell 3,535.89, Mead 1,039.29 [11/04]; **AEO-10 50→80%**.
  - **AEO-03 55→90%** (1/1/27 reinsurance forecasts −7.5% to −20%). Aon 9M $91bn. FAO Oct cereals 116.8. USDM 43.98% [11/03]. **AEO-09 HIT, weaker on mechanism.** New predictions AEO-14 to AEO-17; combo themes KB-262 to -268.
- **CROSS-DOMAIN / CALIBRATION:** Root independence: "C5-Rhine (European basin) · ENSO cluster (C1/C2/C3/C5-Panama/C6) · coastal (wind + sea level) are separate roots." Cold after 11/19 is not ruled out; the coupling lag runs to about 12/3. TERRY owns entry to 11/20. The 12/04 downward-coupling log is owed to TERRY with no written test yet (WQ-631). The Palm Beach rain read is carried by CORAL.
- **FORWARD:** 11/10 WASDE and others · 11/12 CPC ENSO and the vortex window · ~11/15 Nov 24-Month Study (decides C6) · 11/26 SA CEC · **11/30 hurricane season end (AEO-01; C1 channel-kill)** · 12/02 C6 Orange window · 12/04 coupling log.
- **NEXUS-NAMED (verbatim):** "## WHAT NEXUS/PROME SHOULD KNOW — Root independence: C5-Rhine (European basin) · ENSO cluster (C1/C2/C3/C5-Panama/C6) · coastal (wind + sea level) are separate roots. **The C6 conditional still stands:** execution moves leg 2 to the 1,010 line; the November study decides whether it fires. **New predictions AEO-14 to AEO-17; 7 combination themes, KB-262 to -268.** **Nothing here is a trade.**"
- Compact (4,155 B). The vortex read is now 4 days old for a fast variable, so treat it as [STALE 2026-11-06] for vortex state.

## MARCO
- **HEADER:** As of 2026-11-05 18:22 ET (session 39, WQ-623 catch-up). STATUS in the same commit.
- **VIEW:** 🟠 v3.2. Florida Amendment 3 passed 11/3 (62.01% unofficial): the letter is MET, but the sign of net migration is not identified. The Las Vegas room-dollar decline survives Labor Day. The remittance run is 6 months. `AZ-01` is CRITICAL.
- **MOVED SINCE 11/4:**
  - **Amendment 3 passed 62.01% unofficial** (not certified). Residency line 12/31/2026. Pull-forward confound (INFERRED) routed to CORAL 11/5.
  - Las Vegas Aug+Sep RevPAR **−9.02%**, visitors −2.09%, YTD RevPAR +0.6%.
  - Remittances Sep count **−6.27%**, 2-year −9.63%.
  - **`AZ-01` October +35.3pp CRITICAL**, the first scored print ("any-cause stress").
  - BEA travel trailing 12 months through Aug **−$3.125B, ELEVATED**.
  - MAR-28..31 registered; six combo themes. (Most other rows are 10/14–10/28 vintage.)
- **CROSS-DOMAIN / CALIBRATION:** Uncertain about later LAS filings, the January CPS control size (LABOR), current Florida migration (CORAL) and H-2A court state. CORAL's live surfaces still carry the superseded "MIA clean tell" premise. "FL demand remains unidentified". The FL winter 2026–27 loss estimate is "⛔ unsupported/retracted-pending, do not model it" (REGINALD row).
- **FORWARD:** **11/10 Oct CPI airline fares** (ENR-02 leg 2: 2-yr ≥ +20.0% = SUSTAINED; either month below +15.0% = FADED) · 11/12–13 H-2A checkpoint and StatCan Oct · ~11/15 OFLC Q4 and BTS · ~11/17–19 Amendment 3 certification · ~11/30–12/4 LVCVA Oct, Banxico Oct, Nov CPS, `AZ-01` (MAR-28..30).
- **NEXUS-NAMED (verbatim):** "NEXUS | Channel-1 re-instrumentation is a **measurement** change, not a direction change — and the s32 `SDL-01` flip is one print, not a reversal | 🟡 | Avoids reading either as a thesis reversal".
- **FLAG:** 14,797 B. The SENDING table is mostly 9/19–10/28 history. Some glued words ("SAVED10/25", "nominalSA Travel actual trailing12months throughAugust").

## WAL
- **HEADER:** As of November 4 2026 18:13 ET. STATUS pin `fd153358d9…`. Thesis v2.5 (10/30).
- **VIEW:** Q3 materially weakened the near-term credit bear: WAL-01 and WAL-02 were INVALIDATED and reserve coverage rose to 118.4%. The live residual is the hotel/OREO/special-mention build plus capital and earnings pressure. The $99M life-science loan is NO-VERDICT. Bear-fast 2 / Bear-medium 12 / Base 49 / Bull 30 / Tail 7; EV $76.60.
- **MOVED SINCE 11/4 15:37:** Only the 11/4 18:13 interpretation follow-up. No new figures, and Will's clarification did not change any numeric state. The Call Report result (11/4, June 30 → Sep 30) may postdate NEXUS's 15:37 read:
  - **MI3 21.2042% → 19.8072%**, below the 25% thesis rail. "CRE not secured by real estate, not the secured-office $99M loan."
  - NDFI nonaccrual **$122.456M → $122.497M** (~0.774%).
  - Unused commitments **$4.884B → $5.900B (+20.80%)**, "especially private-equity-fund capacity, not demonstrated draws/losses".
  - Bank CET1 **11.5823% → 11.4458%**.
  - "Scores and weights held". Composite 13/25 is "**not yet re-judged**". The evidence-based assessment remains owed.
- **CROSS-DOMAIN / CALIBRATION:** Funding, cohort and severity are REGINALD's. Moody's trigger "capital below 11.0%" (measure unstated) vs parent CET1 10.9% preliminary: a lead only. NDFI 25.7% of HFI with mortgage-credit intermediaries at 16% of loans, the highest of 30 peers. Private-credit SPV joinders: First Eagle $100M commitment (10/1), Crestline 9/18. Nevada is $2.0B of $44.3B commercial loans. Hotel franchise finance criticized $75M → $185M.
- **FORWARD:** Makhijani status conference 11/30 (unverified) · WAL §523 hearing **12/9** · the Q4 call ($99M appraisal) · the Q4 Call Report.
- **NEXUS-NAMED:** none. "Peer notification/consumption UNKNOWN."
- **Nothing new since the ~11/4 as-of**, as expected. 13,771 B.

## YURI
- **HEADER:** As of 2026-11-02 ET (primary fetches 2026-11-02T13:48–13:50Z). STATUS in the same commit.
- **VIEW:** Score 2/5 unchanged. Rapprochement with the US runs alongside widening custody of Western assets. Producer diesel exports stay banned to 31.01.2027. No mobilisation declaration has been found.
- **MOVED SINCE 11/4:** **Nothing; the brief predates the baseline.** For reference, its latest items: YUR-005 HIT (Res. №1436, 31.10, Brier 0.16) · YUR-004 MISS 11/02 · YUR-F01 MISS (Will kept the desk).
- **CROSS-DOMAIN / CALIBRATION:** Uncertain about how the 500 kt diesel permission is administered, whether the №686 code list exists, and unpublished decree numbers. Putin offered fertilizer "in large quantity" to the US (21.10), and a Verkhnekamsk potash auction by-catch was routed to FERT.
- **FORWARD:** mid-Nov RU–US–UA talks · **YUR-006 grade 2026-11-15** (DOCKET L772) · YUR-F02 re-test 2026-11-28 (DAEDALUS).
- **NEXUS-NAMED:** none.
- **FLAG:** Stale (11/2). WAITING FOR still lists the YUR-005 window and the 10/24 YUR-F01 grade as open, although both resolved. 12,727 B.

---

## CROSS-BRIEF (≤10 lines)
1. **ISM Mfg employment**: LABOR "Mfg 52.4" (Oct, graded 11/2) and ISHM "52.4 from 52.7" agree. ISHM adds that S&P hiring was the "steepest since April 2021"; that is a survey disagreement in size, and LABOR keeps the figure.
2. **Factory/NFP**: ISHM factory payrolls +19K (Oct first print) sits inside LABOR's +165K. Same BLS release; one observation, not two.
3. **Carvana SEC closure**: OTTO (11/6) and WAL (11/4) agree on the facts. **Disagreement:** OTTO says WAL `AUDITOR_NEXUS.md` L20/L90 are "now stale (WAL's to fix)", while WAL says those rows were "corrected 10/30". Check at the artifact.
4. **Bank lending into private credit/fund finance is growing at multiple names, and nobody joins the dots.** FLG private-credit slice $1,069M → $2,139M (9/30) · WAL unused commitments +20.80% "especially private-equity-fund capacity" plus First Eagle $100M and Crestline SPV joinders · SHADE Athene SVF II Finco NAV loan $3,097M (+$1,033M Q3). Each desk frames it as composition or commitment, not stress. The cross-name trend is unnamed.
5. **Las Vegas/Nevada/Arizona cluster, unnamed.** MARCO LAS RevPAR −9.02% (Aug+Sep), NV-01 CRITICAL, `AZ-01` +35.3pp CRITICAL (Oct) · HOMER LV FMHPI −2.51%, fallthrough 18.58% (Sep), NV card 90+ 16.28% (Q4-25) · WAL (Phoenix-HQ; Nevada $2.0B of $44.3B commercial) hotel franchise finance criticized $75M → $185M. No brief links WAL's hotel and criticized build to MARCO's or HOMER's LV/AZ readings.
6. **Multifamily credit**: FLG MF 30–89 DPD +68% ($392M, Q3) and MF criticized +$483M; HOMER Fannie MF 0.62%, Freddie subordination 0.80%, Trepp 8.09% (Cove-inflated). Different books, same CREED/REGINALD recipients. FLG is NYC rent-regulated and HOMER is Sun Belt/GSE: two mechanisms, not one.
7. **Florida**: LABOR FL claims −7.2% YoY (w/e Oct 31) and "not a rising-claims state"; MARCO Amendment 3 pull-forward confound (INFERRED) on Q4 FL inflows; HOMER Cape Coral FMHPI −2.28%; AEOLUS no Gulf/FL system. No contradiction. CORAL is the reconciler, and MARCO says CORAL still carries the stale MIA premise.
8. **Labour realization vs consumer credit**: LABOR says the channel is "still closed" (layoffs 1.0%, claims 189K). OTTO's deep-pool auto recoveries (Exeter 4/4 below 28%, Sep) and HOMER's PFSI 60+ 4.2% vs 3.4% YoY point to affordability-driven credit stress without firing. That is consistent with LABOR's "where costs accrue" framing; neither brief names the other.
9. **Fertilizer/potash**: YURI (Putin's fertilizer offer to the US; Verkhnekamsk potash auction) is relevant to FERT only, and potash is triage-only there. No other brief touches it.

## NEXUS QUESTIONS

**(a) Labor and consumer after 11/4:**
- Initial claims **189,000** (w/e Oct 31; DOL 11/5), 4-week MA **194,750**.
- Continuing claims **1,718,000** (week per LABOR's FORWARD row: w/e Oct 24) [LABOR 11/8].
- Next claims print **Thu 11/12**; nothing later is in the briefs.
- Payrolls Oct **+165K**, Aug rev +186K, Sep rev +60K (BLS 11/6). EPOP 59.3, U-3 4.1, LFPR 61.9, AHE +3.1% YoY $38.00, involuntary part-time +339K, factory payrolls +19K [LABOR 11/8; ISHM 11/6].
- JOLTS Sep P NET +83K, layoffs rate 1.0% (BLS 11/3). Challenger Oct 43,994. WARN Oct 22,453 `[2ND]`. State claims 6 of 51 up YoY; FL −7.2% (w/e Oct 31) [LABOR].
- **Consumer credit and delinquency:** LABOR says "NOT mine → CARL". From the briefs:
  - PFSI 60+ day **4.2% vs 3.4% YoY** (Q3) [HOMER 11/6].
  - MBA purchase −19% YoY (wk 10/30) [HOMER].
  - Exeter Sep recoveries 19.14/15.70/21.04/26.51%, re-fired 11/05 [OTTO 11/6].
  - "Ally YoY loss rate is nearly flat; KBRA broad nonprime DQ nearly flat YoY" [OTTO, vintage October].
  - NV card 90+ 16.28% is Q4-25, old [HOMER].
  - NY Fed Q3 household debt is due **11/10**, with no result in the briefs [HOMER, OTTO].
  - No consumer-credit totals are in the briefs.

**(b) Regional bank and CRE:**
- **FLG Q3 10-Q** [FLG 11/7]. The brief does not state the filing date; the v1.0.5 read is dated 11/07.
  - FLG-02 and FLG-03 HIT. Non-accrual $2,817M; specific reserve $155M = 5.5%; $1,548M with no allowance; ACL $869M flat; coverage 30.85% (series low).
  - Q3 cures $144M = 56.3% of outflow, cause undisclosed. MF criticized + classified +$483M. Buyback ~$216M; CET1 13.16% → 12.38%.
  - SR 07-1 322.11%. Private-credit slice $1,069M → $2,139M (~$0.5B C&I recode open).
  - Call Report: MF 30–89 DPD $233M → $392M; bank net income $34.5M → $12.1M.
- **WAL** [WAL 11/4, nothing newer]: Call Report Jun 30 → Sep 30: MI3 19.8072%; NDFI nonaccrual $122.497M; unused commitments $5.900B (+20.80%); bank CET1 11.4458%. Composite 13/25 not re-judged; $99M NO-VERDICT.
- **KRE:** no levels with dates in any of these briefs. The only reference is "10/20 WAL +2.27% vs KRE +1.96%" [WAL], a daily percentage move.
- **Bank losses on non-bank financial borrowers:**
  - OTTO retired its mixed bank-loss aggregate ("No comparable current767M total"; REGINALD and WAL own sizing) [OTTO 11/6].
  - WQ524 First Brands → Point Bonita/SPV → WAL loss is "historical… not a newly disclosed bank or October funding spiral" [OTTO].
  - WAL NDFI nonaccrual is flat at $122.497M [WAL].
  - Mortgage REITs (non-banks): FBRT realized $(24.2)M and TRTX $30.1M MF foreclosure in Q3 [HOMER].
  - Preferred Bank 10-Q ~11/09 is REGINALD's; no result is in the briefs.
  - No new bank loss on an NDFI borrower is reported after 11/4.

**(c) Private credit and insurers (SHADE 11/6):**
- Athene investment loss $3,418M (mortgage marks $1,875M, derivatives $1,399M, provision $82M).
- Mortgage 90+/non-accrual $1,818M → $3,453M YTD. Level 3 +$14,877M.
- AI funding $12.9B funded (deck), $16.0B = 3.8% with SVF II Finco $3,097M; $22.2B = 5.2% with commitments.
- FHLB $29.9B drawn, room $3.9B. Restricted 28.80%.
- Transfers: Group1001 affiliate 5895 → 4898M (−997M YTD), "not completed-exchange proof". DLIC up to 6.5B parent plan, approval and closing unknown.
- T-SHADE-01 NOT MET (11/6). F-SHADE-01 test 2027-03-31.
- **A loan sold with a disclosed price, at or below 90 cents: not in briefs.** The nearest items are marks or statements, not sales:
  - OTTO: "MFIC: US Auto 0.40 to 0.11", a legacy workout stake mark.
  - FLG: "exits clear at 1–5% of the mark (B2) — loss vs carrying value, not vs par". That is a call statement, not a priced sale.
- AAIA Q3, the FI deck and DLIC Q3 were not posted as of 11/6 17:23 ET. The Athene call is 11/12.

**(d) Goods and industrial:**
- ISHM [11/6]:
  - **R1 NOT-MET** on the S&P Oct final (moved from CANNOT-FIRE 11/6), re-pointed to the **12/1** Nov S&P final.
  - **ISM <47 NOT-FIRED** (ISM employment 52.4; the ISM Mfg headline is not stated in the brief).
  - Existing physical-demand contraction warning (VULCAN) **NOT-MET**.
  - Class 8 ACT 13,500 −45% y/y is "J2 volume input only… no condition fires".
  - "No flip fired, and no score, band, gate or threshold changed."
- OTTO [11/6]: both systemic-transmission legs **DISCONFIRMED** · OTTO-37 **FALSIFIED** (Manheim Oct 206.8 vs 207.0) · Manheim "hinge test not fired" · Hertz 2021-2 amortization event **not fired** · Exeter recovery bar re-fired 11/05 (collateral severity, not a contraction trigger).
- LABOR notes ISM employment Oct: "R3-B leg 1 NOT met… earliest fire = Dec prints, early January".
