# DIGEST R3: digest reader 3 of 3, NEXUS full pass 2026-10-31

**Reader:** fresh-context, read-only digest reader (Claude Code, Opus 5.5). **Scope:** 11 briefs (LABOR, MIDAS, VULCAN, ISHM, HOMER, RED, VIOLET, ORACLE, SAM, HENRY, BOND), each read whole. "MOVED" is measured against NEXUS's last full read at 2026-10-26 23:39 ET. Figures are quoted from the briefs. Anything taken from outside a brief is marked **[non-brief]**.

## Pin check (`python3 scripts/brief_pin_check.py`, run 2026-10-31 from repo root)
Summary line: `BRIEF-PIN 1 STALE: 31 brief(s) checked ... OK-PINNED 15 · OK-SAME-COMMIT 14 · STALE-PIN 1 · UNPINNED 1`. The single STALE-PIN belongs to a desk outside this set.
| Desk | Result |
|---|---|
| LABOR | ✅ OK-PINNED 4eff54b75 = STATUS HEAD |
| MIDAS | ✅ OK-SAME-COMMIT 4be44045f |
| VULCAN | ✅ OK-PINNED 2259e91f0 |
| ISHM | ✅ OK-PINNED 0dbba244d |
| HOMER | ✅ OK-SAME-COMMIT 055a9ab6f |
| RED | ⚠️ **UNPINNED**: no STATUS hash in the header. The A10 fallback finds brief commit c16b86f94 **before** STATUS HEAD 0c09cce9b. Both later commits say state unchanged: 12163ddef records the charter-trim ruling, and 0c09cce9b is "S57-c closeout ... state unchanged, HOLD 72 / net-bear 68". |
| VIOLET | ✅ OK-PINNED 614e9ad57 |
| ORACLE | ✅ OK-SAME-COMMIT a9fa63d7f (the header says "see git log" rather than giving a hash) |
| SAM | ✅ OK-PINNED 536b1afd4 |
| HENRY | ✅ OK-SAME-COMMIT add5c4282 |
| BOND | ✅ OK-SAME-COMMIT d5d579fdc (no hash in the text) |
A PASS proves only the pin. It says nothing about whether the content is right.

---

## LABOR
- **HEADER:** As of 2026-10-30 09:11 ET. STATUS `4eff54b75`. 17,995 B.
- **VIEW:** "The freeze holds; the realization channel is quiet." Claims 194K (band B), MA 196,750, CC 1,701K, JOLTS layoffs 1.0%. "Low-fire holds; low-hire is loosening." Score 27/80.
- **MOVED:** **ECI Q3 graded 10/30** (BLS USDL-26-1620): civilian compensation 3.4% (Q2 3.4) ⇒ E1-c, "no wage pressure". Private wages 3.1% flat. AHE↔ECI wedge `3.0 − 3.1 = −0.1`, closed from the AHE side, nothing re-opened. Benefits 3.9%, private health 6.4%, real private wages −0.6%. **Claims 10/29 graded:** 194,000 (w/e Oct 24), band B, MA 196,750 (−1,250), CC 1,701,000. v13 run 2, v7 run 7, record-only. R13-c 0.9937, no action. Score 26/75 → **27/80** (after the "10/28 v3 late grade + v17 creation"). Nothing fired. No packet and no new prediction.
- **CROSS-DOMAIN / CAL:** "For the rate path (BOND/HENRY/ORACLE's): no labour-cost reason for a December hike — direction against the hike pricing, not for it; the hike case rests on inflation, which ECI does not measure." T-07 WARN is UNMEASURABLE ("silent, not clear"). FL claims −8.5% YoY (w/e 10/10). Brier 0.348 over 13 rows. Uncertain about: prime-age LF recovery, LEG C surviving JOLTS 11/3, and the one-way v13/v7 letters.
- **FORWARD:** Tue 11/3 10:00 JOLTS Sep (re-check LEG C; NET ≤0 ⇒ v4 2→3; layoffs ≥1.2% ⇒ escalate). ~11/2 and ~11/4 ISM employment (record-only). Thu 11/5 05:30 Challenger. Thu 11/5 claims (T-01 bound X>411,000; R13-c X≥317,000). **Fri 11/6 NFP:** v2 LEG A bar +150K, a fire stands down v4/v6/v7; Oct EPOP ≤58.6 fires T-03. 11/9 Canada re-check #2.
- **NEXUS-NAMED:** none addressed to NEXUS beyond the schema footer.
- **FLAGS:** Fresh, under cap. The Challenger row says "Card owed ~10/29" and no grading card is shown (watch item).

## MIDAS
- **HEADER:** The top block is "October 30". There is no as-of stamp and no hash in the text; the pin check gives same-commit 4be44045f (10/30 16:53 ET). 15,209 B.
- **VIEW:** "Liquidation proximate, moderate confidence; margin-call/forced element unproven." Gold is "trading as a risk asset" (20-session GLD/SPY correlation +0.72) and "gave no hedge on the 10/30 stress day". Scores: actual 8/20, counterfactual 13/20.
- **MOVED:** **10/30: GLD $355.78 (−3.47%, MIRROR close)**, its first close below the July 16 low of $364.96 and the lowest since 2025-10-02. Gold fell against its drivers: real 10Y 2.63→2.60, 2Y −5bp, DXY −0.15%. The WQ-451 classifier returned residual −3.93% (2.80 sd) with equity stress ⇒ **LIQUIDATION-candidate** (the tonnes leg prints the next business day). **WQ-451 one-month downside line $360.71 CROSSED**; the 3-month lines have not crossed. COT as-of 10/27: net/OI 46.99%, the sixth straight weekly decline (Other Reportables −14,956 longs, managed money +1,538). **[non-brief: STATUS and commit 4be44045f record "MIDAS-16 HIT"; the brief does not name the grade.]** 10/28: Fed hold 10–2, real 10Y 2.64 [10/27] → 2.67 [10/28]. PPLT recovered above −20% on 10/27 (band 3), then all three ETFs were back at trend-level 4 on 10/30. **10/29: WQ-522 M1 successor draft RETIRED by Will.** First Quantum copper guidance cut from 405–475 to 405–435 kt. M1 flip still UNRESOLVED (no certified settle).
- **CROSS-DOMAIN / CAL:** For LIQUID/VIOLET/HENRY: gold gave no hedge. For BOND: real 10Y 2.60 (10/30). For TERRY: the $360.71 line was crossed, and there is "no bounce edge after prior liquidation days (64% = unconditional)". For ZHAO: Oyu Tolgoi paused 10/29 and restart began 10/30; the −41.3% figure is June crude, not copper. Copper tightness on late-October data versus an August-dated ICSG surplus: "different clocks; I1 stays 1". BEA gold exports: "no Treasury-funding inference".
- **FORWARD:** Floor 11/1 21:40 ET. MIDAS-14/15 on the 11/2 close. Per STATUS [non-brief]: DOCKET L819 11/06, L820 11/07, L821 11/18, MIDAS-11/13/17 11/20, Fed 12/09.
- **NEXUS-NAMED:** none.
- **FLAGS:** **Format defects.** Older blocks contain glued words and numbers ("versus23", "real 10Y2.66%", "d200−20.09%", "M2would-be"), which breaks the root Output Canon. The brief is append-on-top: older blocks (10/25–10/26) sit below the current reads and say "Earlier dated blocks ... remain historical". Its "Next existing clocks: October 30 forecasts/map review" line is now past. The brief has no VIEW/CALIBRATION/FORWARD section structure, so it is not schema-shaped.

## VULCAN
- **HEADER:** As of 2026-10-30T16:50:31-04:00. STATUS `2259e91f0`. 10,726 B.
- **VIEW:** "The payers are not cutting." "Friday's sell-off was a chipmaker unwind (Intel −29%, SOXX −8%) with the hyperscalers down about 1.5%: that lowers concentration and lifts equal weight, so the S1 red test moves further away." The composite is 15/25 and S5 financing is the only fired channel.
- **MOVED:** **§4b RESOLVED NO-VERDICT** (confirm 0, falsify 1). AMZN held capex at ≈$220B and says 2027 will be "meaningfully more". MSFT trimmed to ≈$170B. **WQ-551.HELD ENCODED** (EXIT §4c): a ≥5% after-hours fall on a held-or-raised guide in ≥2 prints counts as a CONFIRM leg. WQ-551.FIRM is DEFERRED to DEWEY L834. **Mag7 slot 8: 33.2351% [SPY holdings 10/29], RSP−SPY 63d −0.50pp, YELLOW, NOT FIRED** (priced 10/29, so the 10/30 sell-off is not in it). L800 re-cut: AMZN −$65.8B, five-name −$169.6B. **Amazon 10-Q: new secured supplier Loan Facility up to ≈$80.0B**, plus $115.1B of long-term debt raised in 9M. **MSFT $25.0B bond priced.** Hubbard $5–7B HY take-out shelved (NOT SCORED). GPU reading 8: H100 mean $4.64, unchanged. S2 memory: MU+SNDK 1-month −25.39%, DDR5 spot +0.27%, memory score stays 2. 10/30 closes: QQQ −3.47%, SPY −1.77%, RSP −0.79%, SOXX −8.24%, INTC −28.58%, NVDA −4.22%.
- **CROSS-DOMAIN / CAL:** "No funding-forced cut in the five." ⚠️ "AMZN's −7.30% after-hours fall closed 10/30 at −1.41%: the after-hours measure can catch a fall that does not hold." 17 predictions, 5 OPEN, none due. Self-corrections: L-87 (the FCF figure was TTM) and L-88 (Samsung date mismatch).
- **FORWARD:** 11/06 Mag7 slot 9 and GPU reading 9. 11/08 VULCAN-13 sweep owed. 11/09 CFTC GPU futures review ends and CoreWeave Q3 (modeled). **11/10 BIS 50% rule returns, MOFCOM No.70 suspension ends, TSMC October revenue.** 11/15 EXIT backstop and VULCAN-13/-15 grading. 11/16 FERC EL26-67. ~11/19 NVDA 10-Q (VULCAN-17 reading 1). 11/20 NEXTDC AGM.
- **NEXUS-NAMED:** none. **FLAGS:** Fresh. INTC is rounded to −29% in the VIEW and given as −28.58% in the table (rounding only).

## ISHM
- **HEADER:** As of 2026-10-26 23:41 ET. STATUS `0dbba244d...`. 10,070 B.
- **VIEW:** "Expansion has rail breadth; durability still blurred by prices, machinery mix and purchase timing." September ISM 54.5. S&P final 55.9 and October flash 56.0. AAR 17/20 carload categories growing. Score 18/35 raw.
- **MOVED:** **Nothing since 10/26.** The brief and STATUS both last moved 10/26 23:41. [non-brief: the latest commit touching ISHM's directory is an inbound HANS packet, 74cd84988 on 10/29.]
- **CROSS-DOMAIN / CAL:** It routes rail breadth as "counterevidence to broad goods collapse" to LIQUID/RED. The RED counter-frame "need not clear private/offshore funding stress". Uncertain about real imported/domestic AI equipment demand (a VULCAN verdict) and the financing consequences of a volume turn (LIQUID/RED). PREDICTIONS.tsv is empty.
- **FORWARD (as written; mostly past):** 10/27 durables and Richmond, 10/29 Q3 BEA equipment and CAT, **11/2 October ISM (strict first-published <47) and S&P final**, 11/4 FT-900, 11/5 PH method, 11/13 HY/freight review.
- **NEXUS-NAMED:** none.
- **FLAGS:** 🔴 **STALE BY CALENDAR, not by pin.** The 10/27 and 10/29 catalysts passed with no grade; the desk has been dark since 10/26. The WAITING items (HENRY pointer repair "October 27", WATT custody) are unresolved in the brief. If ISHM stays dark, the 11/2 ISM grade is unowned.

## HOMER
- **HEADER:** As of 2026-10-29 ~09:10 ET (L851 wake). Same commit as STATUS, 055a9ab6f. 13,892 B.
- **VIEW:** "The foreclosure pipeline is still converting, but the front door is narrowing." "CMBS stress at a 2026 high (8.04%) while the GSE book eased." "Volume is adjusting before price." Builder margin compression is now broad.
- **MOVED:** **ICE First Look September (10/27):** 90+/FC **882K = ORANGE, 118K from RED**. FC inventory 303K (+37% YoY). **FC starts 40.0K, −2.9% YoY, the first negative YoY.** FC sales +14.5% YoY. **Fannie MF serious DQ 0.62% at 9/30** (3bp below Orange); MF provision $446M vs $259M (+72%). **Freddie MF 0.58% September**, its first decline since April. Rent breadth 39/100 YELLOW; Apartment List rent +0.1% YoY, the first positive in 3+ years. NAR pending 66.0 (−7.3% MoM), MBA purchase −18% YoY. **PMMS 7.32% [10/22]**, spread ~219bp. **DHI FQ4 (10/29): GM 19.5% derived** (FQ3 20.7%), orders −7%, $91.4M MF impairment; the CRL-23 DHI leg is 200bp away. FBRT realized $(24.2)M. Thesis "0/5 killed".
- **CROSS-DOMAIN / CAL:** "BOND already carries 221bp for the October 15 mortgage spread." Uncertain why the mortgage spread widened ("lender capacity, MBS spreads or volatility"), and about Trepp MF composition. The DO-NOT-CITE list is carried.
- **FORWARD:** ~11/02 Trepp October DQ (MF 8.04%). ~11/02–13 ICE Mortgage Monitor. 11/12 NAR EHS (RED <4.0M). 11/17 NAHB. 11/18 and 11/25 NRC and new-home sales. **~mid-Nov MBA Q3 NDS decides HOM-02.** **Formal thesis grade 11/20.**
- **NEXUS-NAMED:** none. **FLAGS:** Fresh against its pin. A CREED → HOMER packet arrived 10/30 17:20 [non-brief] after the brief. The 10/29 PMMS print and DHI transcript are not yet in the brief.

## RED
- **HEADER:** "vS57 (2026-10-28 21:1x ET)". Unpinned; see the pin table. 8,133 B.
- **VIEW:** "Every stress price eased in the six days RED was dark, except the tail bid." "The Fed went hawkish into a softer tape." "Credit composition: broad, not AI." War is "hotter at sea".
- **MOVED:** **S57 discretionary re-derivation 10/28: net-bear 69 → 68, HOLD 72.** Stag 33 (−2), Managed 25 (+2), Acute 20 (flat), War 15 (+1), Soft 4, Rescue 3 (−1). "No registered-trigger STATE changed." **FT-11 apparatus defect, CHG-RED-055:** a COLLISION in which windows met FUNDAMENTAL and FLOW at once. It moves no weight; the precedence proposal goes to BOND by 11/13. **L739 gate payoff PAID** (weak evidence). Scorecard: 13 CORRECT, 10 WRONG, 2 ACTIVE. Standing fires: FT-02 (10/16), FT-08 (10/14), FT-10 (10/14). HY 340 [10/22] → 318 [10/27]. CCC 1,321. SKEW 149.22 [10/27].
- **CROSS-DOMAIN / CAL:** "rates, banks and part of HY share one antecedent, so count it once." The AI leg is ~10–15% of October's HY widening (DEWEY 10/23). It cites ORACLE's December hike at ~80% [10/28]. Uncertain about: whether Optimum explains CCC's +161bp; the scope of Sinokor enforcement; the post-midterm strike window.
- **FORWARD:** Sat 10/31 RED-25 re-review. 11/1 Sinokor enforcement. 11/3 midterms (FAL-07). ~11/5–11/9 OZK/WAL 10-Qs (CHG-054). **11/6 RED-23 resolves (Oct jobs).** **11/10 CPI: FT-08 exit only on core ≤0.0; CHG-028.** 11/13 BOND FT-11 ruling. 11/15 HHDC. 11/27 VX-006 Zweig (SPY > 683.39).
- **NEXUS-NAMED:** none. **FLAGS:** **The brief predates the 10/30 sell-off, so RED has no read on it.** It is unpinned. A BROCK → RED packet arrived 10/31 09:46 [non-brief]. Daily monitors are dated 10/28.

## VIOLET
- **HEADER:** As of 2026-10-30 16:52 ET. STATUS `614e9ad57`. 6,456 B.
- **VIEW:** "LOW_VOL on the 10/30 close at VIX 19.42, after an intraday excursion to 23.93 that reversed." Convergence 32/50, not re-scored. "The futures front inverted on a settle while the cash curve held — the one stress marker that survived the close. Correlation, not single-name event vol, drove the index."
- **MOVED:** **10/30 close:** VIX 19.42 (+12.9%; high 23.93 at 14:35 ET), VVIX 106.43 (high 124.06), VIX3M/VIX 1.070 (0.964 intraday). **No VIOLET trigger fired.** WALTER's +5 net un-fired on the close. **VX/X6 20.3603 > VX/Z6 19.7888 (M1:M2 −2.81%, deepest since 4/07)**: the third settle inversion this episode (10/22, 10/23, 10/30), unregistered. **COR1M 10.38 → 13.51 (+30%, ledger high; intraday 19.68).** VXAZN −25.7%, VXAPL +12.1%. **Oil-vol canary FIRE 10/28 (OVX/VIX 3.46, p96.5) → back to WATCH 10/30 (3.01).** The equity-concentration vector moved 2 → 3 (10/29 text). SKEW 148.74 [10/28], 151.03 [10/29]. HY 314 [10/28]. JPY RV10 7.02% CALM.
- **CROSS-DOMAIN / CAL:** "INTC −28.6%: substance yours" (to VULCAN/HENRY). "The concentration channel turned correlated intraday and partly unwound into the close." The oil canary rests on one official close. The credit-lead hit and lag rates are unreplicated.
- **FORWARD:** Settle-stamp 10/30 once Cboe History posts. 11/03 Election Day ("front already inverted"). 11/06 payrolls, 11/10 CPI. **11/17 credit-vol WATCH lag endpoint.** 11/18 VIX expiry. 12/16 L441.
- **NEXUS-NAMED:** none. **FLAGS:** The superseded 10/29 lines are labelled but still carry "COR1M 8.73 [10/28] still dispersed, so this is not a correlated selloff". That is RETAINED-HISTORY, and the 10/30 line overrides it.

## ORACLE
- **HEADER:** As of 2026-10-29T00:44–00:5xZ (10/28 20:44 ET). STATUS "see git log", same commit a9fa63d7f. 4,167 B.
- **VIEW:** "Fed held 10/28 as priced; December now ~80% hike. November $110 oil leg pinned at 52.5% on thin trading; Iran ceasefire priced to break in November."
- **MOVED:** Fed hold resolved (the crowd priced ~95%). **VX-ORC-11 retired unfired.** **VX-ORC-12 encoded** (Dec hike 79.5, read 1; de-alert if it collapses below 50.0). **December: PM hike 79.5 ($557.3K liq), Kalshi ≥1 more by Dec 83.0** (OI 50.0K). **Nov WTI $110 touch 52.5%** on $3.4K lifetime volume ("NOT armed, NOT an alert"). Iran ceasefire through 11/30 39.5. Any bank failure by 12/31 at 73.0% on a $1.7K book is flagged as "not a crowd view". The laptop cron routine is live (WQ-527 C).
- **CROSS-DOMAIN / CAL:** Tensions with BRENT/HAWK (thin $110), BOND/TERRY (par 10Y vs DGS10 basis, unconfirmed since 9/17) and RED (recession definitions).
- **FORWARD:** 10/30 L729 read (VX-ORC-04 fires if Nov ≥40.0 on the armed run). 10/31 the October $110 leg closes. 11/03 midterms (House D 92.5, Senate D 67.5). 11/06 jobs (Kalshi U3 >4.1 68.0). ~mid-Nov CPI (PM modal 3.7%). ~11/17 Nov $110 contract switch. **12/09 FOMC.**
- **NEXUS-NAMED:** none.
- **FLAGS:** 🟠 **Stale against its own data.** The cron pulls after the brief are ungraded and are not ORACLE's read [non-brief, `workbook/ODDS_LOG.tsv`]. At 2026-10-31T02:15Z (the 10/30 ET pull): PM "HIKE at Dec mtg" 0.705 ($518.8K liq), "NO change at Dec" 0.275, Kalshi `KXFED-26DEC-T4.00` 0.72. **Nov WTI $110 0.64**, with liquidity down to $11.9K. 10/30T02:15Z: 0.525. Taken together, the 10/30 VX-ORC-04 read may have met ≥40 three times, but no ORACLE session has graded it. **The brief's 79.5/83.0 [10/28] is the citable figure (Disc-E).**

## SAM
- **HEADER:** As of 2026-10-31T15:00:54Z (11:00 ET). STATUS `536b1afd4`. 4,233 B.
- **VIEW:** "The BOJ held and called 2% reached; the yen did not move and Japan is still not the source of current stress." "Hawkish hold; December stays live."
- **MOVED:** **BOJ 10/30: hold 1.25%, 8–1.** Takata dissented for 1.5%. Underlying inflation "generally consistent with" 2%. ETF sales ≈¥860B/yr from January 2027. The JGB plan is unchanged. USD/JPY 157.519 (−0.19%, 0.94-yen range). CFTC specs net **LONG +101,591** yen (10/27). MOF intervention ¥0 (9/29–10/28). **SAM-42 RESOLVED FALSE** (as-made 25%, Brier 0.0625). Record: 16 CONFIRMED / 16 FAILED, with SAM-33 OPEN at 72%.
- **CROSS-DOMAIN / CAL:** "no Japan-led long-end push and no active UST selling established. A December hike is a US-yield-relevant event only through the yen and the long end; neither moved on October 30." Offshore FX-swap funding is "not observed, not cleared". The asymmetric risk is a December skip or dovish messaging (yen weakens), which "is not the carry-unwind channel".
- **FORWARD:** 11/2 Outlook full text. 11/5 minutes and 10Y JGB auction. **11/10 30Y JGB auction (frozen bars), Summary of Opinions, US CPI.** ~11/9 and ~11/13 MOF and FRBNY. 11/30 December purchase dates (SAM-33).
- **NEXUS-NAMED:** "Schema owner NEXUS" (pointer only). **FLAGS:** Fresh. Post-decision OIS for December is unread (the Totan 82% figure is pre-decision, 10/29).

## HENRY
- **HEADER:** Owner fold 2026-10-30 16:50 ET (L885). Same commit as STATUS, add5c4282. 2,800 B.
- **VIEW:** "The 7,700 put wall broke on the 10/30 close (SPX 7,580.07, −1.82%) and dealer gamma is NEGATIVE at both horizons on SPX, QQQ and NDX into Monday 11/02 ... Index mechanics amplified a sector repricing; credit's one lead is HY +12bp [10/29]. No systemic-cascade or crash-timing conclusion."
- **MOVED:** **7,700 put wall BROKEN** (low 7,527.56). SPX flips ~7,732/~7,736, net −$38.6B/−$60.7B per 1%. The trough is at 7,400–7,450, with no second flip within −10%. **NDX flipped NEGATIVE both** (positive on 10/29). QQQ put wall 680 published. **Cascade layer-2 proxy MET** (SPX 117 pts under its 50-day of 7,697.1); layer 1 touched intraday but did not sustain. Rates 10/30: 2Y 4.56% (RED → ORANGE), 10Y 4.94%, 30Y 5.31%. **HY 326bp ⇒ YELLOW (+12) [10/29]**, CCC 1,325. Vol: same as VIOLET.
- **CROSS-DOMAIN / CAL:** OI caveat: 10/30 chains carry 10/29 OI, so it re-pulls before the open. The close-mechanics pin and month-end are "not instrumented". "NEXUS owns the duration letter, BOND the attribution." VULCAN: no capex cut, HEN-36 unchanged.
- **FORWARD:** Monday 11/02 pre-open OI re-pull. **11/18 Row 9 CYPHER grade** (PANW price leg and bank-stock leg).
- **NEXUS-NAMED:** "Rates ... NEXUS owns the duration letter, BOND the attribution." **FLAGS:** Fresh. Small brief; no CALIBRATION section.

## BOND
- **HEADER:** "Last refresh: 2026-10-29 catch-up". Same commit as STATUS, d5d579fdc (10/29 08:31). There is no hash in the text. 1,878 B.
- **VIEW** (pointer format, no VIEW section): "10/28 FOMC hold (10–2, two +25 dissents) bear-steepened 2s30s +10bp". Long-end auctions still clear. Matrix 19/35.
- **MOVED:** Curve 2Y/10Y/30Y **4.67/5.05/5.37 [10/28]**. **BND-32 FALSE.** **ACM 10/16–10/27 term premium −15.0bp vs expected +3.5bp** ("model accounting, not causal"). 20Y-R (10/21) and 5Y TIPS (10/22) clean. **2Y 10/26 AUDIT-ONLY I′ fire**, "record bid substitution (indirect 45.68 / direct 41.32)". **FR2004 as-of 10/14 long-end +$16.312B, a >21Y record weekly rise; VX-04 → 3.** SOFR−IORB +5 [10/27]. **Matrix 17 → 19/35** (dealer 2→3, credit-equity 1→2). WQ-536 A: audit-only fires never reset. OPEN predictions 0. TBT sale approved 10/15 and still held at 10/22.
- **CROSS-DOMAIN / CAL:** LIQUID owns funding. VIOLET owns the VIX close. HY 318 [10/27], CCC 1356 [10/23].
- **FORWARD:** 🔴 **"Refunding bars must be frozen 11/4–11/8"** [STATUS non-brief: 3Y 11/9 · 10Y 11/10 · 30Y 11/12 "or the refunding grades AUDIT ONLY"]. The downgrade is graded at that wake. VX-04 can un-fire on the as-of 10/21 data.
- **NEXUS-NAMED:** none (titled "BOND → NEXUS").
- **FLAGS:** 🟠 **Not schema-shaped:** no as-of time, no VIEW/CALIBRATION/FORWARD sections, no dated catalyst table. It is two days old, and the curve is 10/28, which predates HENRY's 10/30 par curve. It says nothing on the 10/30 Treasury bid.

---

## CROSS-BRIEF (≤10 lines)
1. **HY OAS:** RED and BOND give 318 [10/27]. VIOLET gives 314 [10/28]. HENRY gives **326 [10/29] (+12, YELLOW)**. These agree as a series: the re-widening began 10/29, and RED's FT-02 exit (<300 ×3) is further off. **CCC:** RED 1,321 (undated), BOND 1356 [10/23], HENRY 1,325 [10/29]. VIOLET's "CCC 13.07%" is a yield, a different unit.
2. **10/30 sell-off:** HENRY SPX −1.82%, MIDAS S&P −1.82%, VULCAN SPY −1.77% (SPX vs SPY basis, not a conflict). INTC −28.58% and SOXX −8.24% are given by VULCAN and HENRY. VIX 19.42 and intraday 23.93 match across VIOLET and HENRY.
3. **December Fed hike:** ORACLE 79.5 / 83.0 [10/28], also cited by RED (~80%). LABOR says there is "no labour-cost reason" (ECI 10/30). The ungraded cron shows ~70 / 72 by the 10/30 pull. The fall is not yet in any brief.
4. **Treasury curve:** BOND 4.67/5.05/5.37 [10/28] vs HENRY 4.56/4.94/5.31 [10/30]. These are different dates: 2Y and 10Y −11bp, 30Y −6bp from 10/28 to 10/30, a rally into the risk-off, with "only Treasuries bid" per MIDAS and HENRY.
5. **SKEW:** RED 149.22 [10/27], VIOLET 148.74 [10/28] and 151.03 [10/29], HENRY 151.03 [10/29]. Consistent.
6. **Thread neither names, cross-asset de-risking:** MIDAS (gold liquidated with equities, GLD/SPY correlation +0.72), VIOLET (COR1M +30% to a ledger high, VX front inverted on the settle) and HENRY (negative gamma on all three indices). Each frames the day as local to its own domain ("sector repricing" for HENRY, a liquidation-candidate for MIDAS). No brief joins them into a correlation regime shift.
7. **Thread neither names, IG and long-end supply meeting dealer capacity:** VULCAN (MSFT $25.0B priced, Amazon $115.1B LTD in 9M plus an $80B secured facility) and BOND (record dealer >21Y inventory build, the 2Y bid substitution, refunding on 11/4). Neither links mega-cap issuance to duration absorption.
8. **Two hawkish central banks in December:** SAM (BOJ "December stays live", Totan 82% pre-decision) and ORACLE (Fed ~80%). SAM says yen specs are net long, so no crowded short squeezes. No brief jointly prices a simultaneous December BOJ and Fed hike.
9. **Labor vs Fed:** LABOR's ECI E1-c and RED's Stag 33 / "hiking Fed is not a rescue" use the same 10/28 FOMC with opposite emphasis. Both are consistent with inflation-led, not wage-led, hawkishness.

---

## FOCUS QUESTIONS
**(a)** HENRY (10/30): "Index mechanics amplified a sector repricing". RSP −0.79%, HYG −0.19%. Credit's one lead is HY +12bp [10/29]. "No systemic-cascade ... conclusion", though cascade layer 2 is MET and gamma is negative into 11/02. VULCAN: "chipmaker unwind" (INTC −28.58%, SOXX −8.24%), hyperscalers −0.9% to −1.6%, S1 moves away, nothing fires. VIOLET: correlation drove the index (COR1M +30%, 13.51); the intraday spike un-fired on the close; **one stress marker survived: VX M1:M2 −2.81% on the settle, deepest since 4/07**. RED: **no read**, since the brief is from 10/28. RED's registered test is VIXCLS ≥20 before ~11/25, which would grade FT-10's tail bid as foresight; the close was 19.42. MIDAS adds gold liquidated alongside equities. **Net: the briefs call it a sector repricing with correlated-index and futures-curve warning marks, not yet broad de-risking.**
**(b)** BOND: refunding bars must be frozen 11/4–11/8 (3Y 11/9, 10Y 11/10, 30Y 11/12 per STATUS). ACM term premium −15.0bp vs expected +3.5bp (10/16–10/27). FR2004 long-end +$16.312B record. 2Y 10/26 audit-only fire. SAM: no Japan-led long-end push and no stated insurer UST sales. VULCAN: MSFT $25.0B and Amazon debt issuance. No brief gives a refunding-size view.
**(c)** ORACLE [10/28 20:44 ET]: December hike PM 79.5 ($557.3K liq), Kalshi ≥1 more by December 83.0. Ungraded cron [10/31T02:15Z]: 70.5 / 72. That is not ORACLE's read.
**(d)** RED vS57 (10/28): HOLD 72, net-bear 68 (Stag 33, Managed 25, Acute 20, War 15, Soft 4, Rescue 3). What would change it: HY <300 ×3 (−3 Acute); FT-12 HY <260 (bull win); FT-10 SKEW <140 ×4; VIXCLS ≥20 before ~11/25; the FT-08 exit at the 11/10 CPI (core ≤0.0); the next discretionary re-derivation after the 11/10 CPI or a registered fire.
