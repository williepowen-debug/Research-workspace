# Digest reader B — 10 briefs (LABOR HOMER OTTO MARCO CORAL WAL FLG SHADE ORACLE ISHM)

**Written:** 2026-11-16 21:00 EST (-0500), from `date`. Read-only digest reader for NEXUS; model Opus 5.5 (Claude Code subagent). Repo root `/home/willi/Research-workspace`. Every brief read whole. Baseline per brief = last commit at or before 2026-11-10 11:19 ET.

**Working tree:** none of the 10 briefs nor their `STATUS.md` shows ` M` or `??` in `git status --short` at read time — every version read is the committed HEAD version.

## Pin check (verbatim)

```
BRIEF-PIN 1 STALE: 10 brief(s) checked against amendment 11 (pin-follows-STATUS-HEAD) — OK-PINNED 5 · OK-SAME-COMMIT 3 · STALE-PIN 2. A PASS proves the pin, never the brief's content; UNPINNED briefs are not A11-checked.
  ✅ LABOR     OK-PINNED       pin 6989d77e67 = STATUS HEAD
  ✅ HOMER     OK-SAME-COMMIT  brief and STATUS last committed together in a5608acfe
  ✅ OTTO      OK-PINNED       pin 4dfdf0f923642c08492cac886b909f164aa8b817 = STATUS HEAD
  ✅ MARCO     OK-SAME-COMMIT  brief and STATUS last committed together in 70d3fb82d
  ⛔ CORAL     STALE-PIN       pin 8c9ef1ff6b is 4 STATUS commit(s) behind HEAD 6b3aa4048 — STATUS was re-committed after the brief fold; re-pin and re-commit the brief
  ✅ WAL       OK-PINNED       pin 60ee841c40aeca6e2d40b868c2cb0ee01f510668 = STATUS HEAD
  ⛔ FLG       STALE-PIN       pin 34d6a74649 is 1 STATUS commit(s) behind HEAD 09d458c9b — STATUS was re-committed after the brief fold; re-pin and re-commit the brief
  ✅ SHADE     OK-PINNED       pin cc777cfe8a = STATUS HEAD
  ✅ ORACLE    OK-SAME-COMMIT  brief and STATUS last committed together in edd3e2630
  ✅ ISHM      OK-PINNED       pin c14d3613be2181339f5d37343adf70b7748bdc4c = STATUS HEAD
```
(exit code 1, because of the two STALE-PIN rows)

**What the two stale pins hide (read at STATUS, not graded):**
- **CORAL** — STATUS after the pin adds: falsify grade breakdown (C1 HALF, C2 MET, C3 NOT MET, C4–C6 NOT MET), **WQ-690 A (Will 11/16): any falsify score below 2 reads 🟠 unqualified**, WQ-691 A, **next falsify grade 2027-02-16 (DOCKET L1156)**, next MSI #16 on Nov 26, BKU $21.3M CRE 60–89 as the item to re-read at the 12/31 Call Report, "ATTOM refresh owed (C3 instrument)". The brief's As-of line carries the 1.5 of 6 result but none of the rest. This is a substantive lag (§4.4 trigger (a) fires: 4 commits behind).
- **FLG** — the one later STATUS commit (09d458c9b) only records PROME's acceptance of the DOCKET L810 charter leg (14:10 ET). Administrative; no figure moved.

## Commit times (`git log -1 --format=%ci`)

| Desk | Brief | STATUS | Size (B) | Baseline commit |
|---|---|---|---|---|
| LABOR | 2026-11-12 09:01:17 -0500 | 2026-11-12 09:00:38 -0500 | 19,100 | afc408c651 |
| HOMER | 2026-11-12 12:39:25 -0500 | 2026-11-12 12:39:25 -0500 | 18,712 | a92a0b5b52 |
| OTTO | 2026-11-13 10:29:20 -0500 | 2026-11-13 10:28:50 -0500 | 17,833 | 223c6ca8ba |
| MARCO | 2026-11-11 10:34:38 -0500 | 2026-11-11 10:34:38 -0500 | 16,099 | fd6995b9f1 |
| CORAL | 2026-11-16 11:30:50 -0500 | 2026-11-16 12:46:58 -0500 | 16,171 | d673dd41d8 |
| WAL | 2026-11-16 14:10:19 -0500 | 2026-11-16 14:09:55 -0500 | 16,388 | bd3ca2dc1d |
| FLG | 2026-11-16 14:08:57 -0500 | 2026-11-16 14:10:22 -0500 | 7,278 | d50a809da4 |
| SHADE | 2026-11-16 10:20:28 -0500 | 2026-11-16 10:18:38 -0500 | 12,116 | 5b514d55e4 |
| ORACLE | 2026-11-12 10:18:20 -0500 | 2026-11-12 10:18:20 -0500 | 3,857 | 8cbeac5ec8 |
| ISHM | 2026-11-16 10:23:30 -0500 | 2026-11-16 10:22:40 -0500 | 8,732 | e7b10ac079 |

No brief is over ~22 KB (largest LABOR 19,100 B).

---

## LABOR

- **HEADER:** As of 2026-11-12 09:00 ET (from `date`); STATUS commit `6989d77e67`. Status 🟡.
- **VIEW:** Freeze thesis stood down 11/6 on its own kill rule (freeze-thaw v2 FIRED: Oct NFP +165K vs +150K bar); low-fire holds, low-hire is the half that failed. Realization channel (separations → UI → delinquency) still closed: claims 200,000 band B, JOLTS layoffs rate 1.0%. Score 22/80.
- **MOVED SINCE baseline (one commit, 3d43c4a753, the 11/12 claims grade):**
  - Initial claims w/e Nov 7 **200,000, band B** (DOL primary, RAW SA, 11/12); prior week w/e Oct 31 revised 189,000 → 191,000.
  - 4-week MA **195,250**, unchanged (was 194,750 at the 11/5 read); described as "equal to its w/e 1969-10-11 level on FRED's current vintage — a count, not a rate" (prior wording "lowest since Sep 1969" replaced).
  - Continuing claims **1,697,000** (−20K; "53,000 under 1,750K"), was 1,718,000.
  - T-01 distance `54,750` on MA basis; T-02 `100,000`. v13 `<200,000` run ended at 3; v7 (stood down) run 9, record-only. R13-c return letter graded 11/12: 1.0000, no action.
  - Next claims card (11/19) frozen 11/12: `(X − 195,000)/4`; T-01 bound `X > 414,000`; notes Oracle (the company) ~800 layoffs effective 11/13, 0.4% of a week.
  - WALTER cards -012 (WE Soda WY 350, staged from Q1 2027) and -005 (NFIB Oct jobs) logged as combination items. **No score, band or gate moved.**
  - No fire, grade, kill or retraction beyond the 11/12 claims grade. (Freeze-thaw v2 FIRED 11/6 is before the baseline.)
- **CROSS-DOMAIN / CALIBRATION:**
  - To CARL/REGINALD: realization channel stays shut, nothing to escalate. To CORAL/MARCO: Florida NSA initial claims 4-wk avg 5,182 vs 5,583 a year earlier (ETA 539, w/e 2026-10-31, pulled 11/08) — "Florida is not a rising-claims state"; DIAGNOSTIC, not base-rated. To MARCO: aggregate LF +605K above May; prime-age LF 142K below May (A-9 + A-10, 11/6). To RED: takes no view on HY.
  - Calibration: mean Brier 0.348 over 13 scored rows, "worse than a coin flip"; 0-for-6 at ≥60% on threshold calls, 3-for-3 on mechanism calls. Tensions: RED's soft-landing-via-supply frame "gained ground on 9/4"; MARCO's supply thesis contested by aggregate LF, survives in prime-age cohort.
  - Uncertain about: (1) whether October hiring survives revision and whether involuntary part-time +339K was noise; (2) whether Sep preliminary JOLTS survives the Dec 1 revision; (3) seasonal share of October courier/temp gain (unmeasured); (4) no return letter for v7 and no re-arm letter for v4/v6/v7.
- **FORWARD:** Thu 11/19 claims (card frozen) · 11/20 FL unemployment rate · Tue 12/1 10:00 JOLTS Oct (Sep revised; NET ≤0 ⇒ v4 2→3 and LEG C lost; layoffs rate ≥1.2% ⇒ escalate CARL + REGINALD) · Thu 12/3 05:30 Challenger Nov (tech under +20% with share leg ⇒ v5 4→2; card owed ~11/26) · Fri 12/4 08:30 NFP Nov (LAB-24; LAB-18 Nov EPOP ≤58.8 fires T-03; card owed ~11/27).
- **NEXUS-NAMED (verbatim):**
  - L10: "> 📐 **HOT/COLD SPLIT 2026-09-24 (READ_CAP).** NEXUS reads this brief whole (NEXUS `CLAUDE.md` BOOT step 6, Tier-1 in full), so the root 32,550 B budget binds it. …"
  - L25 (SENDING row, To = "CARL · HENRY · REGINALD · NEXUS · TERRY"): "🔴 **Freeze-thaw v2 FIRED 11/6, card §3d row 1.** v4/v6/v7 stood down at the floor of 1, 27 → 22/80 (WQ-634 A, Will 11/6). ⚠️ Sep JOLTS preliminary, revises Dec 1; a lost LEG C leaves row 2, still fired. First print 15K over the bar; first to second fell ≥16K `22/44 = 50.0%` (LAB-24). Involuntary part-time +339K. No un-fire letter exists" — receipt "DELIVERED 11/6"; mechanism "The labor side of the chain has not broken: claims 200,000 (11/12), layoffs rate 1.0%. This is a hiring read".
  - L96 footer: "**Ratified by NEXUS ★8/07** — verified 2026-09-29 at `AGENTS/NEXUS/BRIEFS_MAP.md` …"
- **FLAGS (internal contradictions — brief-vs-own-body):**
  - VIEW says "prime-age LF is 624K below May"; the CROSS-DOMAIN MARCO row says 142K below May as of 11/6 and that 624K "was … at the August read". VIEW is stale.
  - CALIBRATION open book lists "LAB-19 81% (… one more LF >0 resolves ✅)" and "LAB-18 10% (… Oct ≤58.6 · Nov ≤58.8 left)"; the header says "LAB-19 ✅" and the EPOP row says "LAB-18, now 5%". Two stale probabilities.
  - VIEW bullet 2 ("The book is one print weaker than on 9/3 … Every freeze-thaw leg moved toward firing on 9/4; none fired") is September text left under an 11/6 fire.
  - CALIBRATION "LT-unemployed share 27.0% (on the >27% restore bar)" vs header "27.6% long-term unemployment".
  - FORWARD table still carries a pre-event "🔴 Fri Nov 6 08:30 NFP October" row beneath the ✅ GRADED row for the same event.
  - Brief as-of 11/12, 4 days old; no LABOR catalyst fell 11/13–11/16, so not stale against its own docket.

## HOMER

- **HEADER:** As of "2026-11-12 ~12:1x ET (data through 2026-11-12 noon)"; no explicit pin hash (OK-SAME-COMMIT a5608acfe). Status 🔴. ⚠️ Typed approximate clock (`~12:1x`), the form the stamp rule bans on records others grade from.
- **VIEW:** Foreclosure pipeline still converting (FC sales +14.5% YoY, inventory +37% YoY, Sept) while the front door narrows (FC starts −2.9% YoY, first negative). Multifamily stress now arriving at maturity dates (Trepp MF special servicing 9.22% Oct, 2026 high). Turnover collapse at Red (NAR Oct EHS 3.75M) with prices flat-positive. Thesis 0/5 legs killed.
- **MOVED SINCE baseline (3 commits: 85b9717627 11/11, 4ff19c7ac7 and a5608acfe2 11/12):**
  - 🔴 **HOM-03 HIT:** NAR October existing-home sales **3.75M** (−5.5% MoM, −8.8% YoY; NAR issuer 11/12); Sept revised ~3.97M (DERIVED); 5.1 months; median $416,700 (+0.4% YoY); West −9.7% MoM; NAR "lowest since Aug 2010 (its first-print claim)". Red band "250K through".
  - **PMMS 7.11% [11/12]**, −7bp, fourth fall, lowest in 7 weeks (Freddie issuer); spread ~213bp on Tue 10Y 4.98%. Desk: "my 11/11 'stops falling' call was wrong." A2 kill 61bp away. (Baseline 7.18% [11/05].)
  - **Trepp CMBS MF special servicing 9.22% Oct, +69bp = new 2026 high** (TreppTalk 11/09; Apr peak 9.08); Blackjack $517.7M transferred at fully extended maturity 10/09; DQ–SS gap 113bp (Sep 50).
  - **Rates:** 10Y 4.84 → 4.98%, 2Y 4.46 → 4.73% [11/05 → 11/10, Treasury CSV]; MND 30Y 7.30% [11/10], +12bp; "Dec hike ~85% priced (SECONDARY)".
  - **Arbor Q3** (8-K 10/30, issuer): non-performing 32 loans $647.6M (was 19 / $428.8M), REO $491.2M, dividend SUSPENDED; stock −62% in 29 sessions (vendor); −29.1% on 10/30. Blackjack → BX 2021-21M CMBS bondholders (INFERRED), no Arbor link.
  - **United Fidelity Bank** (PROME report, relayed): $2.14B MF nonaccrual, bank-held, unsecuritized; maturity/trigger/containment UNRESOLVED (narrowed 11/12 "12:4x" on PROME/CATO DB5–DB7). Wording narrowed in a5608acfe2 to match PROME's corrected source.
  - **NY Fed Q3** (pub 11/10): mortgage 90+ 1.13% (Q3-25 0.83); flow into 90+ 1.60% (1.28); FC notations 61,900, +13% YoY; NV mortgage 90+ 1.98% (0.99%). ICE Monitor Nov: FHA cures −46% YoY; all-loans cure YoY not printed (band UNGRADED, 2nd month).
  - **loanDepot Q3** (8-K 11/09): net loss $28.7M; servicing 60+ DQ 2.0% (1.5%); ~$19B MSRs sold since July. Replaces the earlier non-bank servicer row (PFSI/UWM/RKT).
  - Redfin October median sale −0.4% YoY "first decline in 3 years; 36% of sales with a price drop (record)" (relabelled from "third negative week").
  - CORAL row added: addresses only for FL statewide values (NY Fed HHD Q3 p.36; ICE Nov appendix p.22).
- **CROSS-DOMAIN / CALIBRATION:** Routes FL statewide to CORAL ("CORAL owns the statewide figure"); bank exposure to REGINALD/DEWEY; insurance to AEOLUS; BOND carries 221bp for the 10/15 mortgage spread. Uncertain about: how far Trepp MF falls if Cove ($210M) reverts; whether the +9bp spread move is timing or real; whether ICE prints the cure YoY again; Fannie/Freddie selloff cause rests on secondary reports. Diverges from NAR's Yun ("rates could be topping out").
- **FORWARD:** Tue 11/17 10:00 NAHB HMI (HOM-04: cutters 43% vs RED >45%) · 11/18 Census NRC · formal thesis grade 11/20 · ~11/24 Case-Shiller Sept · 11/25 new-home sales; Q3 GDP residential (−3.3%, confirm 11/25) · MBA Q3 NDS "~11/12–14 (not out 11/11)" decides HOM-02 · Trepp Nov DQ ~12/01–05 (HOM-05) · ICE Monitor Dec ~12/07–14 · ATTOM Q3 (not out at 11/11).
- **NEXUS-NAMED:** only the rotation banner (L7): "> ♻️ **ROTATED 2026-09-24** — the pre-rotation brief is preserved byte-for-byte at `archive/NEXUS_BRIEF_2026-09-24_pre-rotation-VERBATIM.md` (crc 267930108). …" — no line addresses NEXUS.
- **FLAGS:**
  - VIEW contradicts header/body on rates: VIEW "Rates fell three weeks running to 7.18% (the easing reversed 11/10: MND 7.30%)" vs Status/SENDING "PMMS 7.11% [11/12] … fourth fall" and "my 11/11 'stops falling' call was wrong". VIEW omits the HOM-03 HIT entirely.
  - NEXT DECISION POINT and WATCH still list NAR EHS 11/12, Trepp ~11/13, loanDepot 11/06, NY Fed 11/10 as upcoming (all done).
  - MBA Q3 NDS "~11/12–14" is past with no grade; HOM-02 decider status unknown as of the brief.
  - **Disc-E:** "Dec hike ~85% priced (SECONDARY)" is a priced-odds figure not cited to ORACLE (ORACLE 11/12: +25 at 90.5 PM / 88 Kalshi).
  - Rates row cites PMMS 7.18% [11/05] while the row above carries 7.11% [11/12] — two vintages in two live rows.
  - Glued words in CALIBRATION counter-evidence: "rental demand+19.2%", "asking rent+2.2%", "inventory−7.24%", "67vs75".
  - Typed clocks `~12:1x`, `12:4x`.

## OTTO

- **HEADER:** As of 2026-11-13 10:28 ET; STATUS commit `4dfdf0f923642c08492cac886b909f164aa8b817`. Thesis v1.6 (2026-11-05). Status 🔴🔴 fraud/recovery losses; both systemic-transmission legs DISCONFIRMED.
- **VIEW:** Four established fraud case tracks and severe recovery damage are the core (Carvana DORMANT, allegation-only; Car-Mart not a fifth fraud case). Deteriorating collateral, continued conditional financing access, fraud losses and bank propagation are separate propositions; general Invisible Exit conviction LOW. Convergence 32/50 "is an index over correlated local colours, not probability", 21 points from one root.
- **MOVED SINCE baseline (3 commits; s044 11/11, s045 11/12, s046 11/13 — each says "No probability, colour, threshold or score change"):**
  - s044 (11/11): Tricolor §341 NOT held, continued to 2027-03-17 10:00 CT (Verita Dkt 1496, filed 11/09); "~3% recovery stands". NY Fed Q3 auto flow into 90+ **3.0232%** (Q2 3.0028), "a series high by 2bp", balance $1.734T; <620 origination share 16.8% "is not OTTO-10's Equifax measure".
  - s045 (11/12): **EART 2026-5 graded ABSENT** from its 10/20–11/12 launch window (EDGAR FTS 0 vs control 69); "a halt candidate; not lost market access"; OTTO-07 unmoved 15%; next check ~11/30.
  - s046 (11/13): BROCK graded Car-Mart a **twelfth bridge** (relief to 11/16; 8-K Item 1.01, KB-BRK-489); OTTO held V9 🔴 4 by rule. (SENDING row still shows the eleventh bridge, KB-BRK-472, 11/09 → 11/12.)
- **CROSS-DOMAIN / CALIBRATION:** "A December hike (ORACLE's odds) raises new-deal and warehouse costs, reaches none of OTTO's open predictions." Hertz/credit read is LIQUID's; Car-Mart grade is BROCK's; bank sizing REGINALD/WAL. Flags `WAL AUDITOR_NEXUS.md L20/L90 now stale (WAL's to fix)`. Forecast score: strict 3/9, mean Brier 0.286111 vs constant 50% = 0.25, "No demonstrated forecasting edge." Uncertain/gaps: Trust V outcome UNKNOWN; OTTO-11 STUCK 60%; OTTO-10 NEEDS_VERIFY; borrower exit UNVERIFIED; Chu ruling not public through ECF 198 (11/10); last week's search coverage thin (s040).
- **FORWARD:** SDT ~11/15 (second observation; VIEW pre-states "will be NO VERDICT") · Car-Mart relief expiry Mon 11/16, BROCK grade 11/16 after ~16:30 ET or Tue 11/17 AM (D:L1139), backstop #9 Wed 11/18 · First Brands hearings 11/16–11/18 (D&O, DIP sweep) · Chu check ~11/20 · Tricolor sales deadline 11/30 · Ares response 11/30 · EART October 10-Ds ~11/30 (OTTO-36; EART 2026-5 re-check) · OTTO-36 grade 12/04 · Manheim Nov 12/07 · Tricolor §341 2027-03-17.
- **NEXUS-NAMED (To column includes NEXUS; first cell of each quoted verbatim, full rows at L17–L37):**
  - L17 "s045 (11/12): EART 2026-5 absent from its 10/20–11/12 launch window (EDGAR FTS 0 vs control 69); Exeter's ESART 2026-2 launched 9/17"
  - L18 "s044 (11/11): Tricolor §341 NOT held, continued to 2027-03-17 10:00 CT (Verita Dkt 1496, filed 11/09); NY Fed Q3 auto flow into 90+ 3.0232% (Q2 3.0028), a series high by 2bp, balance $1.734T"
  - L19 "s043 close refresh: Tricolor auction 9,082 vehicles, $63.09M net through 10/31, ties to the old figure at 4/30; Hertz 2021-2 $1,000M at 9/30, was $2,000M"
  - L20 "s039 mixed bank-loss aggregate retired; original SDT commentary explicitly corrected"
  - L21 "Edmunds Q3 dated depth update; watchlist labels qualified"
  - L22 "s037 financing comparison: ten tranche rows/five pairs across three selected shelves"
  - L23 "CPS class coupons/initial protection higher with both deals completed; issuer weighted-coupon prose/table mismatch preserved"
  - L24 "EART2026-4 closing date corrected August28→August31"
  - L25 "Bounded Ally Q3 transcript pass completed, secondary source"
  - L26 "October25 catch-up readout: actual Ally Q3 and visually checked credit deck; primary KBRA and Edmunds source upgrades"
  - L28 "Exeter September collections loaded: recovery 19.14/15.70/21.04/26.51%, 4/4 below 28%, EART 2024-1 re-crossed; re-fired 11/05"
  - L31 "LIQUID/PROME WQ524 historical First Brands → Point Bonita/SPV → WAL loss and lender response consumed"
  - L37 (To = "NEXUS · PROME"): "L708 remains NO_INSTRUMENT; earlier consumption settled" | 🟡 | "No verified corporate-bond/rating/index/date join; supplemental equities MIXED cannot establish consumer attribution of CCC widening or absence of credit transmission."
- **FLAGS:**
  - As of 11/13: two of its own dated items have now passed un-folded — SDT ~11/15 and the Car-Mart 11/16 relief expiry. Stale against its own docket.
  - SENDING Car-Mart row (eleventh bridge) is one bridge behind CALIBRATION s046 and WAITING FOR (twelfth bridge).
  - Heavy glued words through CALIBRATION and older SENDING rows: "current767M", "original3total", "mean7107 aboveQ2 6884, belowQ1 7183", "EART2026-4", "August28→August31", "closing8-K Item1.01", "October14 relay037", "remains25%", "original55%", "remainsUNKNOWN", "no8-K", "lateOctober25", "remains8%", "Modeled10-Q check~November5", "STUCK60%", "at`965d875ae`", "inspected990753244", "lastSDT runAugust14", and more.
  - Stale CALIBRATION references to "October30 final-thesis timing" / "OT1/finalv1.6 staysOctober30".

## MARCO

- **HEADER:** As of 2026-11-11 10:34 ET (session 40, catch-up wake via PROME prome-2b; closeout); STATUS "folded in the same commit as this brief" (OK-SAME-COMMIT 70d3fb82d). Thesis v3.2 unchanged. Status 🟠.
- **VIEW:** Energy → airfares (`ENR-02`) SUSTAINED 11/11: fare stage transmitting into the winter booking window, Florida demand NOT graded. Amendment 3 changes the Florida question, not the score (Channel 3 MED-LOW). Channel 2 (Canadian travel) remains the strongest transmitting channel; Channel 1 (remittances vs CPS) split, price transmission unproved.
- **MOVED SINCE baseline (2 commits, 94fefe5a12 and 70d3fb82dc, both 11/11):**
  - **`ENR-02` SUSTAINED 11/11:** October CPI airfares 327.822 vs Oct-24 265.939 = +23.27% 2-yr (Sep +26.36%); national series; Spirit co-driver.
  - October CPS (context only): foreign-born labor force **33,121k, +842K m/m** ("largest Sep→Oct 2007–2026"), +686K vs Oct-2024. MAR-29 70 → 90%.
  - Amendment 3 figure changed **62.01% → 61.98%** unofficial, "one figure with CORAL"; certification 11/17.
  - NEXT DECISION POINT rolled from `ENR-02` (11/10, done) to `ID-01` leg 2 (StatCan October land-vs-air gap, ~11/13 est.).
  - New SENDING rows 11/11: WALTER (ENR-02), TERRY (airfares tradeability: "MARCO sees no clean expression … NO CARD is a complete answer"), CORAL (61.98% adopted), PROME (catch-up packet; D:L986–L988 not pulled forward).
- **CROSS-DOMAIN / CALIBRATION:** Shared FL metrics with CORAL (Amendment 3, MIA, migration "documented-not-merged"); LABOR (January CPS population-control size; "nativity not a control dimension"; foreign-born Dec→Jan +632K); REGINALD (winter 2026–27 FL loss estimate ⛔ retracted, do not model). Says "CORAL's live STATUS/brief carry the superseded MIA clean-tell premise". Uncertain about: later LAS filings, January CPS control size (LABOR), current comparable FL migration (CORAL), H-2A court state. Conviction direction HIGH · timing MEDIUM · magnitude LOW.
- **FORWARD:** ~11/13 StatCan October / `ID-01` decision · H-2A court checkpoint 11/12–13 · ~11/15 OFLC Q4 / BTS · ~11/17–19 Amendment 3 certification / CA second check · ~11/30–12/4 LVCVA Oct, Banxico Oct, November CPS (grades `SDL-01`, MAR-29), `AZ-01` · H-2A December 30 court deadline.
- **NEXUS-NAMED (verbatim):** L46: "| NEXUS | Channel-1 re-instrumentation is a **measurement** change, not a direction change — and the s32 `SDL-01` flip is one print, not a reversal | 🟡 | Avoids reading either as a thesis reversal |"
- **FLAGS:**
  - **Stale as-of (11/11, 5 days):** its own NEXT DECISION POINT (`ID-01`, ~11/13) and ~11/15 OFLC item have passed with no fold; H-2A 11/12–13 checkpoint also unreported.
  - MARCO's claim that CORAL still carries the MIA clean-tell premise is contradicted by CORAL's brief (10/29 block: "'MIA is the clean tell' WITHDRAWN"; VIEW: "⛔ the 'MIA clean tell' is WITHDRAWN (MARCO 10/25)"). MARCO's WAITING FOR row and CALIBRATION line are stale.
  - Glued words: "SAVED10/25", "underWALTER", "CBO2025", "superseded10/25", "throughWALTER", "endsFebruary 2023", and VIEW "latest BEA nominalSA Travel actual trailing12months throughAugust shows−$3.125B,ELEVATED".
  - The BEA travel figure "−$3.125B" carries no as-of date beyond "through August".

## CORAL

- **HEADER:** As of "2026-11-16 11:3x ET (Mon, coral-ag, due-row wake …)"; STATUS commit `8c9ef1ff6b` — **STALE-PIN, 4 STATUS commits behind HEAD 6b3aa4048** (see top). Thesis Coral Bleaching v1.1. Status 🟠 ELEVATED. ⚠️ Typed approximate clock `11:3x`.
- **VIEW:** Thesis split holds: household/condo stress confirmed; bank-loss transmission NOT confirmed (bank rail NOT met, NOT armed; REGINALD Q3 frame FINAL 11/06: NO TRANSMISSION, BKU MIXED). Supply-side MSI leg 🟠 since 9/13, Cape Coral at series lows. "Florida real estate is stressed" still does not equal "Florida banks are breaking."
- **MOVED SINCE baseline (3 brief commits: a61acce034 11/11, 49b6d61109 and b6c40d4565 11/16):**
  - **11/15 falsify grade run 11/16 (one day late): 1.5 of 6, 🟠 holds** — bank half C1 HALF + C2 MET, household half 0 of 4 (As-of line only).
  - MSI #15 (data 11/15): 4-of-5, Cape Coral **5.74** (new low; As-of line). MSI #14 (data 11/10): Tampa 7.24 · PG 6.20 · NP 6.22 · Cape Coral 5.82 · Lakeland 6.27.
  - **CORAL-02 not graded:** Florida Realtors October not posted (re-dated to first print).
  - ⛔ **Correction 11/11 — one rain figure 24.69 in, Malabar 1.9 SE** (WPC final storm summary 11/03; preliminary total 11/01–11/03); corrects 11/09 "24 in in 24 h"; Palm Beach was a second core (West Palm Beach 2.4 N 22.83 in). No federal declaration (OpenFEMA 11/11).
  - "December hike priced above one move (HENRY 11/10: +28.2bp; 10Y 4.98%)": from November the condo-vs-SF GSE financed-sales instrument is rate-confounded and needs a national control.
  - Citizens 215,397 at 11/06 (−1,035 w/w). DBPR records request closed, not resubmitted (Will 11/10); three bankruptcy docket reads dropped (Will 11/10).
- **CROSS-DOMAIN / CALIBRATION:** Rain figure carried by AEOLUS under CORAL's name; FL–Canada air seats are MARCO's; bank read REGINALD's; rates HOMER/HENRY. To CARL: FL bankruptcy 225.9/100k, +21.3% YoY to 9/30/26, 1.256× US (AOUSC F-2, read 10/29). Conviction mechanism-HIGH · bank-transmission-LOW · timing-MEDIUM (winter 2026-27). RED counter-frame: if Q3 banks cure again and bankruptcy growth converges to US, CORAL is a real-estate/demand story.
- **FORWARD:** Mon 11/16 FL Realtors October (first full month for GSE financed-units read; not posted at brief time) · Nov 17 Amendment 3 certified · ~mid-Nov Avidia 10-Q, Citizens 10/31 month-end · weekly Federal Register DR-4955 notice (L784 re-date proposed 11/20) · ~Nov OIR Isaias claims (68,071 / $735.5M at 11/06) · Dec 11 NFIP authorization · (STATUS only, not in brief: MSI #16 Nov 26; next falsify grade 2027-02-16, DOCKET L1156).
- **NEXUS-NAMED (verbatim):**
  - L59: "| 5 | **MARCO correction applied:** \"MIA is the clean tell\" WITHDRAWN (MIA also carried Spirit); one number = MARCO's MIA Sep −1.82% YoY, trigger MET, mechanism CONFOUNDED | NEXUS — check your own demand premise |"
  - L84: "| NEXUS | Geography read: statewide firming vs SW/Central-FL MSI still above 6.00 in four of five metros, edging down — the stress is localized, not statewide | 🟠 | Synthesis should not treat FL as uniformly improving or uniformly breaking |"
  - L117 footer: "*Brief follows NEXUS schema R3+amendment 7. …*"
- **FLAGS:**
  - **Status line contradicts As-of:** Status says "Next: falsify grade 11/15" and "reading #14 (11/10)"; As-of says the grade ran 11/16 and MSI #15 is the current reading.
  - VIEW / CALIBRATION / NEXT DECISION are stale: "the bank half keeps curing" and "bank-transmission-LOW until Q3" vs the 11/16 grade's "bank half C1 HALF + C2 MET"; NEXT DECISION "late Oct → 11/15 … criterion 6 resolves 11/4"; WATCH "by Thu 11/19 MSI-01 reading #14" (#15 already read).
  - No 11/16 dated block in the body; the 11/16 result lives only in the As-of line. The WQ-690 A band rule and next grade date are absent (STATUS-only).
  - Schema order: VIEW and CALIBRATION precede CROSS-DOMAIN (amendment 12 says CROSS-DOMAIN first); footer cites "R3+amendment 7".
  - WAITING FOR "CREED — Next Trepp cycle (Oct DQ) ~early Nov" is past (HOMER carries Trepp Oct DQ 8.09%).
  - Typed clocks `11:3x`, `13:0x`, `14:5x`.

## WAL

- **HEADER:** As of November 16 2026, pinned to STATUS commit `60ee841c40aeca6e2d40b868c2cb0ee01f510668` (PROME prome-6f wake, Will's word 13:45 ET; Claude Code, Opus 5.5). Thesis v2.5 (2026-10-30): Bear-fast 2% / Bear-medium 12% / Base 49% / Bull 30% / Tail 7%; EV $76.60; PT $52–77; composite 13/25 "not yet re-judged".
- **VIEW:** Q3 materially weakened the near-term credit bear (WAL-01/02 INVALIDATED, reserve coverage 118.4%, nonaccrual $562M → $485M). The live residual is hotel/OREO/special-mention build plus tangible-capital and earnings pressure. The $99M life-science appraisal is NO-VERDICT (missing evidence, not adverse); higher-for-longer risk is CRE/hotel refinancing, logged not scored.
- **MOVED SINCE baseline (4 commits: 13d90796f8 and c7bac260c7 11/11, 9f8825a23c and ef42f2eef8 11/16):**
  - Price: WAL **$73.22 (−2.10%) at 14:02 ET 11/16**, "4.41% below EV $76.60" (KRE −1.15%); "no WAL filing since 11/11 and no WAL-specific fact behind it". Basis: intraday; vendor not named in the brief. Prior pin: $76.30 close 11/10 (vendor), $76.15 at 09:48 ET 11/11.
  - **Five forward Q4 predictions registered (OPEN):** WAL-03 Q4 NCO > 40bps 20% · WAL-04 hotel franchise finance nonaccrual > $0 at 12/31 35% · WAL-05 OREO properties > 27 at 12/31 50% · WAL-06 Q4 deposit-costs line > $165.4M 55% · WAL-07 $99M charge-off/reserve disclosed by the FY2026 10-K 25%.
  - Plaza Continental (Cantor collateral, Ontario CA): final cash-collateral hearing 11/17, unopposed, broker-reported 31% occupancy; H1–H11 no move (KB-295).
  - DEWEY's Q3 bank population: WAL's $10–100B band improved QoQ; smaller-bank deterioration "69% one bank, United Fidelity" (KB-296).
  - 11/11 pin: hiking-Fed sensitivity from WAL's own filings — Dec +25bp already in Q4 guide (KB-250); deposit-beta assumptions raised (avg 53 → 58%, ECR 70 → 77%, non-maturity 59 → 65%); NII +4.7% per +100bp, EVE −5.3%; per 25bp ~+$38M NII vs up to ~$58M ECR (linear, "roughly neutral pretax"); AFS loss −$1,223M at 9/30 marked at 5Y 5.09% / 10Y 5.29% vs 4.81% / 4.98% on 11/10 ⇒ est. ~+$170M pretax since quarter-end, ~$130M given back 11/05 → 11/10. 60-day beta to KRE 1.17; 20-day realized vol 33.4%; short interest 10/30 settlement 5.60M (−11.87%), 5.21% of shares.
  - Typed "~10:10 ET" stamp corrected to pin commit time 09:56 ET (c7bac260c7).
  - **No weight, score, EV, PT or grade change.**
- **CROSS-DOMAIN / CALIBRATION:** Funding/cohort/severity and price guards are REGINALD's; structure and position management TERRY's and Will's. Carvana SEC closure (auditor-nexus, V2 excluded): "`FRAUD/AUDITOR_NEXUS.md` rows corrected 10/30". Credit ratings: Moody's lead "capital below 11.0%" (measure unstated) vs Q3 parent CET1 10.9% preliminary (KB-265–267). Unknowns: borrower/loss attribution, parent/hedge reconciliation, $99M appraisal; "Peer notification/consumption UNKNOWN".
- **FORWARD:** 11/17 Plaza Continental final cash-collateral hearing · 11/30 Makhijani status conference (unverified; CourtListener refuses anonymous access) · Wed 12/9 WAL §523 hearing vs the Stupins · 12/31 WAL-04/WAL-05 measurement dates · Q4 call / $99M question (date not stated) · Q4 Call Report MI3 (standing quarterly).
- **NEXUS-NAMED (verbatim):**
  - L43: "- **Carvana (auditor-nexus, V2 excluded):** SEC closed its Jun-2025-subpoena investigation Sep 2026 with no enforcement recommendation (Carvana Q3 10-Q; issuer description, not exoneration; Jan-2025 report only). `FRAUD/AUDITOR_NEXUS.md` rows corrected 10/30; no score moved." (names the auditor-nexus file, not the NEXUS desk)
  - L49: "… No new queue, checker or cadence; THESIS/POSITIONS/NEXUS ownership, frozen grades and required delivery are unchanged."
- **FLAGS:**
  - **Schema non-conformance:** no CROSS-DOMAIN / VIEW / CALIBRATION / NEXT DECISION / FORWARD headings; the body is the 11/04 pin's content, labelled "still current except the price". Header carries three stacked pins (11/16, 11/11, 11/04).
  - Price $73.22 is an intraday 14:02 ET figure; root rule #4 — must not be cited as live from a STATUS/brief.
  - Old thesis table "Re-score rule Amendment 1 … Bear-medium **held at 16**" sits beside the current Bear-medium 12% — a historical rule application, labelled as such, but easy to misread.
  - OTTO's brief says WAL's AUDITOR_NEXUS L20/L90 are "now stale (WAL's to fix)"; WAL's brief says those rows were corrected 10/30. OTTO's row is the stale side.

## FLG

- **HEADER:** As of 2026-11-16 14:08 ET; STATUS commit `34d6a74649` — **STALE-PIN, 1 commit behind** (administrative only). Thesis v1.0.5. Status 🔴. "event-driven desk; this brief stands until the next print or owner session."
- **VIEW:** Start from the specific reserve, not coverage: $155M = 5.5% of $2.8B non-accrual (9/30, 10-Q); $1,548M carries no allowance. Q3 exit mix changed (cures 56.3% of outflow, $144M, cause undisclosed). The wall is 2027 (MF $8,519M reprices/matures into the rent freeze effective 10/1/26).
- **MOVED SINCE baseline (2 commits: 37970789e7 11/11, 66ec412e03 11/16):**
  - 11/16: no graded item changed. Logged (KB-FLG-120..124) who pays to extend: mostly Flagstar itself — $1,548M non-accrual with no reserve on appraised values re-tested each Q2; 2026 MF modifications add 1.2–1.5 years, running out ~late 2027 to early 2028; **43.9% of the $471M modified stock already past due**; who carries 2027 fixed maturities ($1,581M) and $3.0B rent-regulated resets is UNKNOWN.
  - 11/11: Q3 Call Report re-pulled, unamended (SR 07-1 322.11%); Dec hike barely moves NII (+0.68% per +100bp short rates, issuer); AOCI outside regulatory capital; refinancing channel at 5Y 4.81 / 10Y 4.98 [11/10]; "no rate relief for $12B of sub-3.9% resets through 2027 (INFERRED)".
  - Kenilworth v. RGB ruling: now "via press or filings only (docket read dropped by Will 11/10, WQ-477)".
- **CROSS-DOMAIN / CALIBRATION:** To REGINALD: non-accrual roll-forward cure share 59.5% (2023H1) → 1.6% (2026H1); cohort base rate cannot be built (FR Y-14Q non-public). To CREED: 2027 MF reset $8.4B incl. $2.9B ≥50% rent-regulated (call 10/23, B2). "Cross-agent tensions known to me: None active this cycle." Uncertain about: (1) what the $144M Q3 cure was; (2) who finances buyers of exiting loans; (3) par-basis loss at exit; (4) the freeze ruling. K-3 kill leg UNSET — "no falsifier is held there — do not infer one".
- **FORWARD:** by Dec 31 rent-freeze merits ruling (T-12) — the only item inside ~3 weeks. Later: Q4 Call Report ~2027-02-14; FY2026 10-K ~2027-03-01 (grades FLG-01: Q4 formation < $327M).
- **NEXUS-NAMED (verbatim):** L22: "| NEXUS | M-05 / R10 inputs: FLG RED [10/23]. Coverage 30.85% (10-Q) is a series low; specific reserve 5.5% of non-accrual | 🔴 | Named-regional CRE level fire stays lit; recognition row = reserve, not provision |"
- **FLAGS:** WAITING FOR REGINALD "Open — its 11/07 re-score" has no update. Otherwise clean, spaced text.

## SHADE

- **HEADER:** As of 2026-11-16T10:20:23-05:00; STATUS commit `cc777cfe8a` (PROME prome-6f due rows D:L240, D:L184, D:L185). "No grade, score or threshold changed this session." Status 🟠 structural/latent insurer-wrapper stress; evidence partial.
- **VIEW (from the Assessment paragraph; the brief has no VIEW section):** Research pass complete, evidence partial; the primary exposure map strengthens structural concern while correcting overstatement; a current liquidity crisis, illiquidity breach and cohort cascade are unproven. Vector #1 single-name DLIC (Delaware Life) FIRING; composite 20/30 unchanged.
- **MOVED SINCE baseline (3 commits: c6e8fbd3cc and df073440d7 11/11, 97b3f71407 11/16):**
  - **C2 withdrawal test EXECUTED 11/16:** penalty ✅ S1 ✅ S2 ❌ ⇒ **NOT WITHDRAWN** (C2 survives on S2 alone).
  - Q3 deck (11/12): Athene T+117 vs peers 95/99/93/80; penalty +25.25 bp like-for-like (Q2 +30.00; vendor JPM → Bloomberg). Canary Q3 mixed, no reading; **S3 now UNAVAILABLE** (deck dropped its syndication count); SHD-01 NO-VERDICT. LTM FA inflows $23B: FABN 24 / FABR 31 / FHLB 45%.
  - FHLB room $3.9B (10-Q basis) vs deck basis $3.5B (Q2 deck $4.4B), "never merged"; FHLB $29.9B drawn; FABN $32.6B; S2 34.2% from 36.2% [9/30].
  - New row: hiking Fed squeezes Athene's thinnest funding links and makes T-SHADE-01 harder to fire (INFERRED); 2Y 4.73 [11/10, Treasury]; Clear Spring affiliated ≈4.94× surplus [YE2025, cross-document].
  - New row: AI funding at Athene — deck $12.9B funded 9/30 (~3% of gross invested assets); 10-Q adds SVF II Finco $3,097M (+$1,033M Q3) outside that total; Big Sky commitments $4.9B + $1.3B VIE; SoftBank-linked $4,846M; Oracle $2.4B; funded $16.0B = 3.8%; with commitments $22.2B = 5.2% "a ceiling". "No loss on any AI position in a filing."
  - New row: ACRA BMA FY2025 (PRIMARY): 1A $44.5B of $49.0B and 2A $91.0B of $102.0B are funds withheld; direct Level 3 ex-embedded-derivative $194M / $161M; "never add to Athene Holding's Level 3".
  - DLIC Q3 statutory not posted 11/16 10:09 ET, re-dated 11/18.
- **CROSS-DOMAIN / CALIBRATION:** HY is "LIQUID's/RED's/REGINALD's instrument, not a SHADE trigger". Floating-rate BDCs earning more biases T-SHADE-01's sign leg toward NOT MET while credit worsens. Overturners listed (independently valued unaffiliated exchanges, resumed bank distribution, stable post-pause net flows). F-SHADE-01 falsifier test 2027-03-31.
- **FORWARD:** 11/18 DLIC Q3 statutory (re-dated) · 11/18 Catalina and ACRA related-party notes owed · T-SHADE-01 continuing reads · 2027-03-31 F-SHADE-01.
- **NEXUS-NAMED (To column includes NEXUS; signal cell quoted verbatim, full rows L10–L22):**
  - L10 "**A hiking Fed squeezes Athene's thinnest funding links; my trigger gets harder to fire.**"
  - L11 "**AI funding now sized at Athene, and the deck's total is not the whole book.**"
  - L12 "**Athene secured substitution continued in Q3; C2 survives on S2 alone.**"
  - L13 "**ACRA's own filings cannot show Level 3; the split lives at the cedants.**"
  - L14 "**Apollo's GAAP loss is marks on issuer attribution; delinquency is the counterweight.**"
  - L15 "**Specific primary AHL AI-infrastructure contingent guarantee.**"
  - L16 "**AMAPS and ACRA partial economic map now primary.**"
  - L17 "**DLIC denominator/vintage reconciled; affiliated bonds cannot all be formal ABS.**"
  - L18 "**Funding aggregate is not usable collateral or available cash.**"
  - L19 "**Group1001 execution/current distribution and post-pause flows still unknown.**"
  - L20 "**Rosner complaint recovered; PHL liquidation timing corrected from primary.**"
  - L21 "**AG55 rules clearer; actual submissions/SVO counts/TSR method remain gaps.**"
  - L22 "**System totals and loss allocation remain unreconciled.**"
- **FLAGS:**
  - **Brief gap:** latest T-SHADE-01 reading in the brief is the 11/6 close; STATUS carries a newer one (read 11/11, endpoint 11/10 close: NOT MET, RAW wrappers +2.62% vs managers +8.88%, both up; HY 334 [11/9], 2026 high 348 [11/5]). That figure should have been in the brief.
  - **Schema non-conformance:** no VIEW, CALIBRATION, NEXT DECISION or FORWARD sections; the SENDING table has no header.
  - **Severe glued words** in rows L15–L22 and the Evidence paragraph, e.g. "ApolloQ2 Note17 p94: AHL guarantees15% of WHCO", "Managementnotprobable", "FiveQ2AMAPS named issuer-risk positions$13.515B", "ALRe37%econs/100%votingACRA,ADIP63%", "Affiliatedbonds12.619338B>formalABS10.441030B", "FHLB27.7B drawn/33.8B estimatedtotal", "ClearSpring identity83607", "FreeSept16Doc1", "AdoptedAG55 effectiveYE25", "FedL116renumberedS1281.1.s June2026", "restart atSCRATCH, raw84files/25,601,491B". These rows are near-unreadable without the source.
  - Several older rows (L13–L22, "10/21", "10/29" paragraphs) are not dated in-row; figures like "Restricted120.985B" (Apollo Q2) carry a period only via "ApolloQ2".

## ORACLE

- **HEADER:** As of 2026-11-12T15:15Z gate read (Thu, routine e8c69052e6; desktop, Kalshi SIGNED), plus the "14:1xZ" Huang resolution read; folded "2026-11-12 10:3x ET"; STATUS commit "see `git log -1 -- AGENTS/ORACLE/STATUS.md` (same commit as this brief)" (OK-SAME-COMMIT edd3e2630). Status 🟠. Owner of the December FOMC priced path (WQ-671 A, 11/11). ⚠️ Typed approximate clocks.
- **VIEW:** December FOMC: a quarter-point hike at about 90, half-point odds halved, venues and futures agree. Huang (Nvidia CEO) exit resolved YES on both venues. Iran/oil: pause priced, $110 oil tail gone. No trade implied.
- **MOVED SINCE baseline (2 commits: 56d9a8fc83 11/11, edd3e2630e 11/12):**
  - **12/9 FOMC, priced odds (11/12 15:15Z; "cite this dated read"):** PM hold 3.4 · +25 **90.5** (liq $727.8K) · +50 or more 6.2 (11.8 at 11/11). Kalshi `KXFED-26DEC` hold 5 · +25 88 · +50 7 (OI 139K to 159K). Venues about +25.6bp. Futures `ZQZ26` 95.93 (Yahoo last trade 10:05 ET, not a settlement), EFFR 3.88 (11/10) ⇒ +26.8bp; `ZQF27` +29bp. Baseline (11/06): PM hike 76.5 / Kalshi 78.0. "Cause of the +50 fall not established."
  - **Nvidia:** Huang exit RESOLVED YES (Kalshi `KXCEONVDA` determined 14:11:04Z; PM legs 99.95, UMA proposed, not final). PM 12/31 leg 16.5 → 77 at 22:00–22:30Z 11/11 after public after-hours WSJ reporting: "reaction, not a leading indicator". Successor: Kress PM 30.9 / Kalshi 33 · Ian Buck 27.5 / 27. AI bubble burst 11.5 to 12.3 (7.0 on 11/11).
  - **Iran/oil:** WTI $110 Nov 5.5 (7.0) · invade 7.5 · war 1.6 · Hormuz normal 12/31 6.5 · pause by 11/30 66.5; by-11/8 pause leg 21.5 → 32.5 in 48h; spread +88.0pp. Baseline (11/08): WTI $110 Nov 17.0, invade 10.5, ~76 for another strike within 14 days.
  - CPI: October CPI market prices its fallback rule (September's 3.7) because BLS has no October 2025 index (KB-ORC-136). Recession PM 2.1 / Kalshi 3.0 (was 4.5 / 4.0). Any-bank failure 70.5 on a $2.6K book, "not a crowd view".
  - Tension 1 downgraded 🟠 → 🟡 (December size gap closed 11/12); tension 2 🔴 → 🟠.
- **CROSS-DOMAIN / CALIBRATION:** Routes Dec FOMC to LIQUID, HENRY, BOND, CARL; Nvidia to VULCAN, BROCK, TERRY; oil to BRENT, FALCON; Nov jobs to LABOR, HENRY. Open: 10Y resolution basis (Treasury par vs DGS10) unconfirmed since 9/17; recession definitions structural vs RED. Uncertain: cause of the +50 fall; spot oil rose (relay) while the $110 tail fell.
- **FORWARD:** Fri 11/13 gate read · Tue 11/17 Nvidia Q3 results (~1:20 pm PT) · 2026-11-17T01:00Z Nov $110 Active-Month switch (INFERRED) · 11/30 Hormuz normal (PM 1.4), Kalshi Brent `>$97.99` 25, pause 66.5 · 12/04 November jobs (`KXU3-26NOV`) · Wed 12/09 FOMC · ~12/10 October CPI fallback resolution (INFERRED date; PM 3.7% leg 94.9) · 2026-12-15 Kalshi gap-fill re-check (WQ-305).
- **NEXUS-NAMED:** none.
- **FLAGS:**
  - As of 11/12, 4 days old: the 11/13 and 11/16 routine gate reads are not folded. The Dec FOMC odds the fleet should cite are a 4-day-old read on the eve of Nvidia's 11/17 print and after Bessent's 11/15 allegation (no market read on either in the brief).
  - Schema non-conformance: no VIEW / CALIBRATION / NEXT DECISION sections (Status + "THE ONE THING" blocks + tensions + forward table).
  - Pin is a pointer ("see git log"), not a hash.
  - ORACLE's 90.5 [11/12] is the owner figure for Disc-E; HOMER's "~85% priced (SECONDARY)" and CORAL's "+28.2bp (HENRY 11/10)" are not ORACLE-cited.

## ISHM

- **HEADER:** As of 2026-11-16 10:23 ET; STATUS commit `c14d3613be2181339f5d37343adf70b7748bdc4c`. Status 🟡.
- **VIEW:** Physical equipment buying well supported; factory upturn strong but slowing, durability unproved. Scores unchanged: 18/35 raw, shared-root 13/25; equity thermometer UNKNOWN/excluded.
- **MOVED SINCE baseline (3 commits: 60d1a151e4, 3615ac7407 11/13, b4b24bf4e5 11/16):**
  - **11/16:** Cass October published — shipments **+5.9% y/y, NSA; SA m/m +1.7%**; J2 deterioration **NOT-MET**; Empire November general **7.8 from 25.5**, new orders 3.0 from 23.2, employment 18.1, sign positive, no band. J2 sample gained the October month (freight-up), counts unchanged.
  - **11/13:** Cass October not published at 10:21 ET (re-dated 11/16, nothing graded); J2 sample gained the matured July forward window: July 2026 Cass −4.84% y/y followed by **+47.9 bp HY widening**; forward 28/33 at ≤25 bp; "Cass had turned positive in August/September before the widening, so not freight-led". Deere Q4 call November 25 confirmed at the issuer (notice November 11).
  - `workbook/PRINTS.tsv` 89 → 92 rows. No score, band, gate or threshold changed.
- **CROSS-DOMAIN / CALIBRATION:** VULCAN owns the AI-capex verdict (computer imports Sept +150.96% y/y nominal, one Census vintage); CARL owns inflation (S&P output prices steepest since Sept 2022; ISM prices 75.2 from 77.9); LABOR owns factory payrolls (+19K Oct first print; ISM employment 52.4 from 52.7); LIQUID/RED own credit (J2 volume input only). "Physical equipment and freight strength can coexist with LIQUID credit/funding stress; financing transmission is not cleared by these prints." Uncertain: whether order strength is end demand or buyers locking in stock and prices.
- **FORWARD:** November 19 Philadelphia and Kansas City Fed (regional sign; band OWED) · November 20 ACT Class 8 October final (vs preliminary 13,500) · November 17 / 24 Fed G.17 October / annual revision · November 25 BEA Q3 second estimate, durables October advance, Deere fiscal Q4 (call 10:00 ET) · December 1 S&P final 09:45 ET (R1 two-branch grade, WQ-643 A) and ISM 10:00 ET (strict <47) · December 2 / 3 / 8 rail batch, October M3, October FT-900 · December 14 Cass November.
- **NEXUS-NAMED:** none.
- **FLAGS:** "Recent thesis pivot" line is the 11/6 pivot (fine, labelled). Clean, spaced text. The PROME row ("Six due items closed …") is 11/6 vintage under an 11/16 header but is dated inside ("Packets dated November 6").

---

## Cross-brief (my 10 desks)

1. **10Y 4.98% [11/10]** — HOMER (Treasury CSV), CORAL (via HENRY 11/10), WAL, FLG all agree; **5Y 4.81% [11/10]** WAL = FLG; **2Y 4.73% [11/10]** HOMER = SHADE. One market datum on four surfaces (one Disc-H class), now 6 days old.
2. **December hike pricing — five desks, three bases:** ORACLE (owner) +25 at 90.5 PM / 88 Kalshi, futures +26.8bp [11/12]; HOMER "~85% priced (SECONDARY)" [11/10, not ORACLE-cited]; CORAL "+28.2bp (HENRY 11/10)"; OTTO cites "ORACLE's odds"; WAL "Dec +25bp already in the issuer's Q4 guide"; FLG "+0.68% NII per +100bp (issuer)". No direction disagreement; HOMER's figure is the Disc-E defect.
3. **United Fidelity Bank:** HOMER "$2.14B MF nonaccrual, bank-held, unsecuritized (PROME report, relayed)"; WAL "smaller-bank deterioration is 69% one bank, United Fidelity (DEWEY, KB-296)". Both relayed; neither is an owner read. Possible single-name driver of a "small-bank deterioration" aggregate.
4. **Amendment 3:** MARCO and CORAL both 61.98% unofficial, certification 11/17 — reconciled (MARCO's baseline 62.01% superseded).
5. **MIA airport:** MARCO Sep −1.82% YoY (trigger MET, mechanism CONFOUNDED) = CORAL's carried figure. **Disagreement:** MARCO says CORAL still carries the "MIA clean tell"; CORAL's brief shows it WITHDRAWN. MARCO's row is stale.
6. **Labor supply:** LABOR prime-age LF 142K below May (11/6; its own VIEW still says 624K), aggregate LF +605K above May; MARCO foreign-born LF +842K m/m in October (CPS, "a record", context only). Population-control figures differ by series: LABOR "aggregate CLF −1.4M" (Jan 2026) vs MARCO "foreign-born Dec→Jan +632K" — different measures, not a contradiction, but both feed MARCO's `SDL-01` grade 12/4.
7. **ISM manufacturing employment 52.4 (October):** LABOR = ISHM (ISHM adds "from 52.7"). Factory payrolls +19K appear only in ISHM.
8. **Carvana SEC closure:** OTTO and WAL agree on facts; OTTO's "WAL AUDITOR_NEXUS L20/L90 now stale" is contradicted by WAL ("rows corrected 10/30").
9. **HY OAS:** SHADE carries 348 [11/5] (2026 high) and its last in-brief T-SHADE-01 read is 11/6; ISHM cites "+47.9 bp HY widening" for the July forward window. Neither brief reflects the context 320 [11/12] / 323 [11/13]. Nvidia/AI: only ORACLE (Huang exit YES, earnings 11/17) and SHADE (Athene AI funding $16.0B funded / $22.2B with commitments; Oracle $2.4B; SoftBank-linked $4,846M) touch it; no brief of mine mentions Bessent's 11/15 allegation.
10. **Multifamily maturity channel:** HOMER (Trepp MF SS 9.22% Oct, maturity defaults), FLG (2027 MF reset $8.4B; modifications expiring late 2027–early 2028), WAL (CRE/hotel refinancing "logged, not scored"), CORAL (bank rail not met) — one refinancing-wall mechanism seen from four desks (one Disc-F root, R1 rates/R3 credit), not four confirmations.

## Summary of flags

- Stale pins: CORAL (substantive, 4 commits), FLG (administrative, 1 commit).
- Stale as-of against own docket: MARCO (11/11; `ID-01` ~11/13 unfolded), OTTO (11/13; SDT ~11/15 and Car-Mart 11/16 unfolded), ORACLE (11/12; two gate reads unfolded), HOMER (11/12; MBA NDS ~11/12–14 unfolded).
- VIEW contradicts own header/body: LABOR (624K vs 142K; LAB-18/LAB-19 stale), HOMER (rates "fell three weeks to 7.18%" vs PMMS 7.11% fourth fall; HOM-03 HIT missing), CORAL (Status "Next: falsify grade 11/15" vs As-of "run 11/16"; "bank half keeps curing" vs C2 MET).
- Brief-gap candidate: SHADE (T-SHADE-01 11/10-close read in STATUS, not brief).
- Glued words: SHADE (severe), OTTO (heavy), MARCO (several), HOMER (four).
- Schema non-conformance (no VIEW/CALIBRATION sections): WAL, SHADE, ORACLE.
- Typed approximate clocks: HOMER, CORAL, ORACLE.
- Figures lacking date or basis: WAL price $73.22 (intraday, vendor unnamed); MARCO BEA travel −$3.125B (no as-of beyond "through August"); SHADE older rows (period only via "ApolloQ2"/"FY2025").
- Disc-E: HOMER's "Dec hike ~85% priced (SECONDARY)" not ORACLE-cited.
- No brief over ~22 KB.
