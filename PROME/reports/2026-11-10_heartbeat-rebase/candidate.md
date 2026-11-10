# HEARTBEAT.md
**Base:** Tuesday evening, 2026-11-10, THIRTY-NINTH base, PROME prome-07. Market levels: the PROME dashboard pull of Tuesday 2026-11-10 16:35:10 ET (`PROME/reports/2026-11-10_heartbeat-rebase/dashboard.txt`) plus `fetch.py price` for SPY, QQQ, SMH, RSP, HYG, GLD, ORCL and NVDA at about 16:36 ET; individual observation dates below. Owner evidence: the November 9 and 10 desk returns filed in `PROME/inbox/processed/` (list: `PROME/reports/2026-11-10_heartbeat-rebase/sources.md`); this is not a whole-fleet refresh, and the desks not woken since the 38th base are named there. **Amendment chain: 0.** Prior base and its three amendments, verbatim: `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-11-10.md`. Plan, verification and declared review residue: `PROME/plans/2026-11-10_heartbeat-39th-rebase-PLAN.md`.

> **DERIVED SURFACE — owner evidence wins:** `PROME/GATES.tsv`, `PROME/DOCKET.tsv`, `PROME/WILL_QUEUE.md`, desk letters and Will's rulings. Observation, publication and retrieval dates differ. Vendor futures bars are not exchange settlements; after-hours quotes are not closes. Missing observations and owner grades stay missing. Binding older limits remain in `PROME/HEARTBEAT_COLD.md` (§KOS through §KOS.16 except named retirements).

**Central judgment — PROME synthesis:** Tuesday November 10 was a rates day, not an equity day. October core CPI printed +0.3% (+0.296%) and headline +0.4%, each 0.1 over consensus and the third straight 0.3 core (HENRY, agency index data; the BLS release page unread). The larger move came before the print: at 04:00 ET Governor Waller's London speech backed a December hike and said 50 bp should be considered if core ran about 0.3 or higher, and December pricing went from 82% to 99% in that minute (HENRY). December ended at +28.2 bp, more than one full hike [vendor last trade 16:01 ET, not a settlement]. Treasury par 2Y 4.73 (+17 bp), 10Y 4.98, 30Y 5.35 [11/10]: a front-led bear flattener. Two refunding auctions drew soft indirect demand against BOND's frozen bars (3Y 11/9, 10Y 11/10); direct bidders took the shortfall and dealers did not warehouse, so no composition failure and no score moved. Equities absorbed it: S&P 7,520.93 (−0.38%) and VIX 19.46, under 20 on the print (VIOLET: LOW_VOL holds); SPY is +1.99% from Friday's close. Nvidia −5.47% is single-name for a second day (HENRY). Credit retraced: HY 334 [11/9] from the 348 high [11/5], LIQUID's tier rule reads STALLS, and funding eased a fifth day. Oil lost its deal premium: Brent settled 92.57 [11/9] from 98.32 [11/6] on an unconfirmed Qatar interim-terms report and Trump calling strikes "highly unlikely"; no barrels returned (BRENT). Gold fell 2.68% [GLD, vendor]; MIDAS has not graded it. Price deterioration becoming a financing constraint is still not shown. The new open question is whether a Fed hiking into 0.3 cores reprices long real rates and credit: HYG's fall today was a rates move, not a measured spread move (TERRY), and the 11/10 HY cell publishes 11/11. The AI-funding web is still not one loop: SoftBank reported loan-to-value 15.9% at September 30; SAM's roll-forward to today's Arm price is 22.5%, under its own 25% ceiling. CoreWeave and TSMC's October revenue report tonight and are ungraded at this cut. Next discriminating observations: the 11/10 HY cell, the 30Y auction 11/12 (I′ bar 63.89), claims 11/12, PPI 11/13, Nvidia 11/17, the FOMC 12/9. NEXUS's regime split is retired to judgment, no number (WQ-664 B). **X1 CLOSED / DON'T-SIZE; energy STAND DOWN. One approved card is fired and unfilled (HYG ×5); $0 deployed by PROME.**

**1. Energy —** Brent January `BZF27` $91.98 [11/10, vendor]; settled $92.57 [11/9] from $98.32 [11/6], −5.85%; low 89.15 at 08:40 ET 11/10. Boundary #1 (≥$120 ×3) not met, about $29 away. Dated Brent's newest print is still $107.03 [11/3]. EIA STEO [released 11/10]: the Q4 world balance flips from a 0.69 mb/d draw to a 1.47 mb/d build on supply, consumption unchanged; OPEC spare capacity 0.01 mb/d through March 2027: agency estimates, one agency. BRT-33 OPEN, 2 of 3 valid sessions. → `AGENTS/BRENT/STATUS.md`.

**2. Rates / funding / labor —** December hike +28.2 bp [HENRY, vendor last trade 11/10]. Treasury par 2Y 4.73, 10Y 4.98, 30Y 5.35 [11/10]; 2s10s 25 bp from 32; HEN-62 RESOLVED-HIT. On HENRY's bands 2Y is RED (>4.60), 10Y 2 bp under red. 10Y auction 11/10: indirect 61.23% vs the 65.05 bar, I′ FIRE, the second in two sessions (3Y 55.48 vs 57.44); dealers 9.77%, auction health holds at 3 (BOND). SOFR99−IORB +6 bp [11/9]: LIQ-079 NOT ARMED. Payrolls +165,000 [October]; claims Thursday. MOVE 92.43 [11/10]. → `AGENTS/BOND/STATUS.md` · `AGENTS/HENRY/STATUS.md` · `AGENTS/LABOR/STATUS.md`.

**3. Credit —** HY 334 / CCC 1,311 bp [11/9, first-published]; 342 [11/6]; 2026 high 348 [11/5]. IG 91. Tier rule STALLS; >320 run MET, eight observations; REG-T-04 (350 ×3) 0 of 3; rekill 0 of 2 (LIQUID 11/9). Veterans Day 11/11 is not a session for these counts (LIQUID's fix 398a946b9a, owner-tested only). Car-Mart's lenders extended relief to Thursday 11/12, the eleventh bridge (BROCK). Card flow into 90+ delinquency 6.87% [Q3, NY Fed], down from 6.97. X1 CLOSED. → `AGENTS/LIQUID/STATUS.md` · `AGENTS/BROCK/STATUS.md` · `AGENTS/CARL/STATUS.md`.

**4. Japan / carry —** SAM: no carry unwind; the yen weakened on Waller, USD/JPY high 158.845 [11/10 11:30 ET, vendor], and the live risk is the approach to 160, where the Ministry of Finance has acted. BOJ December 76% [Totan 11/10, equivalents, not probabilities], from 52% [11/6]. Life insurers net bought ¥62.3B of foreign bonds in October, the first net buying since May (MOF). SoftBank: reported LTV 15.9% [9/30]; SAM's roll 22.5% at Arm $183.26; the 25% ceiling is reached near Arm $145; the finance chief named no asset sale (secondary transcript). → `AGENTS/SAM/STATUS.md`.

**5. Equity-vol —** 11/10 closes, vendor: S&P 7,520.93 (−0.38%), SPY $749.92, QQQ $674.76 (−0.68%), SMH $483.63 (−0.78%), RSP $220.88 (−0.03%), NVDA $168.89 (−5.47%). VIX 19.46 on Cboe's 16:15 ET print, intraday high 21.43; Cboe History unposted, so the basis is the print. VIX3M/VIX 1.061. Gamma: S&P closed above the 7,500 concentration and about 1.5% under the ~7,635 flip, map not re-run on the close; QQQ and NDX NEGATIVE at 11:19 ET with spot under the main strike (HENRY). HEN-57 NOT FIRED. → `AGENTS/HENRY/STATUS.md` · `AGENTS/VIOLET/STATUS.md`.

**6. AI capex —** VULCAN: no letter fired, 15/25 [11/9]; TSMC's October revenue and CoreWeave's Q3 (17:00 ET) are ungraded at this cut. Nvidia announced its own investigation 11/8 (AP). NEXUS: no bank's Q3 document attributes $100M or more of charge-offs to non-bank-finance borrowers (PRED-38 MISS; smaller filers due ~11/16 unread). IREN: $6B of $15B capex uncommitted, nothing shows financing refused; a Microsoft cut is not a default on its Blue Owl-held loan (BROCK's reading, not a lawyer's). ORCL $117.98 [11/10, vendor]. → `AGENTS/VULCAN/STATUS.md` · `PROME/themes/ellison/`.

**7. Banks / war / China —** REGINALD [Q3 Call Reports, read 11/7]: the frozen 8/20 risk score showed no skill (n = 14, one quarter); L180 BROADER, weak, so "concentrated" carries a qualifier until the FDIC count. Hormuz marks B 1 / C 14 / D 85 HELD, 7 ships lost (FALCON, cutoff 11/9); Qeshm [11/6] graded a US strike, not explicit; weekly review 11/11. China: every 11/10 clock re-suspended, next cluster January 9–11, 2027; the 11/27 clock covers graphite and is not addressed (ZHAO). → `AGENTS/REGINALD/STATUS.md` · `AGENTS/FALCON/STATUS.md` · `AGENTS/ZHAO/STATUS.md`.

**8. Metals / food —** GLD $369.36 (−2.68%) [11/10, vendor], ungraded by MIDAS, whose last read is 11/8: actual composite 13/20, no band touched; October 30 stays UNEXPLAINED-DOWN. Certified gold settlements stay unavailable. FERT: NASS cut corn yield to 179.6 bu/acre with no fertilizer cause stated; October food at home +0.4%, led by beef and snacks, cereals flat; the transmission question now closes on three clean months (WQ-665 B, WQ-666 A). → `AGENTS/MIDAS/STATUS.md` · `AGENTS/FERT/STATUS.md`.

## Stress dashboard
Source: PROME dashboard pull 2026-11-10 16:35:10 ET (`PROME/reports/2026-11-10_heartbeat-rebase/dashboard.txt`). Levels keep observation dates; dashboard colours are not owner grades.

| Measure | Latest carried observation | Basis / limit |
|---|---|---|
| HY / CCC OAS | 334 / 1,311 bp [Nov 9] | First-published; the Nov 10 cell lands about 10:10 ET Wed Nov 11 |
| Brent Jan BZF27 | $91.98 [Nov 10] | Vendor; no exchange settle claimed |
| 10Y (dashboard) / SOFR | 4.88% [Nov 9] / 3.88% [Nov 9] | Official observations; Treasury par 10Y 4.98 [Nov 10] |
| SOFR−IORB / CP−TBill | −2 / −3 bp [Nov 9] | Dashboard cells |
| VIX / MOVE | 19.46 / 92.43 [Nov 10] | Print / index, vendor |
| USD/JPY | 158.76 [Nov 10] | Vendor |
| KRE / OZK / WAL | $73.09 / $50.77 / $76.30 [Nov 10] | Vendor closes |
| APO / ARES | $122.74 / $139.41 [Nov 10] | Vendor closes |
| TLT / BIZD / ARCC | $80.88 / $12.69 / $19.44 [Nov 10] | Vendor closes |
| FSK / OBDC | $11.97 / $11.16 [Nov 10] | Vendor closes |
| Initial / continuing claims | 189,000 [wk Oct 31] / 1,718,000 [wk Oct 24] | Different weeks; LABOR interprets |
| Gas (weekly) / Cushing | $4.00 [Nov 9] / 27.25 [Oct 30] | Vendor |

## Missing links that matter next
These are evidence needs within existing work, not new commissions, thresholds or promises of unattended monitoring.

| Chain | Established / counterevidence | Next discriminating observation |
|---|---|---|
| Hike repricing → credit | HY retraced to 334 before CPI; HYG fell on rates today | 11/10 HY cell Wed; REG-T-04 needs 3 above 350 |
| Hike repricing → long real rates | Front-led flattener; two soft refunding indirects, dealers not warehousing | 30Y auction 11/12; PPI 11/13 |
| Price → financing constraint | Not shown; private and offshore unmeasured | IREN's $6B; CoreWeave tonight |
| Dealer gamma → path | S&P above 7,500, under the flip; QQQ and NDX negative at 11:19 ET | HENRY's pre-open map 11/11 |
| OpenAI → Oracle / SoftBank | Shared counterparty, not one loan chain; SoftBank under its ceiling | CoreWeave 11/10; Nebius and Athene's call 11/12; Oracle 10-Q ~12/15 |
| Deal premium → oil | Paper price fell, no barrels returned, Dated Brent unprinted since 11/3 | A dated Iran answer; the next Dated Brent print; IEA report mid-November |
| Bank funding → bad-loan formation | Q3 funding healthy; frozen score showed no skill; L180 BROADER, weak | FDIC Q3 count mid/late November |
| BOJ and Fed both hiking → carry | Differential did not close; yen weaker; no unwind | USD/JPY 160; the 12/18 BOJ decision |
| Card delinquency → consumer | Flow into 90+ eased two quarters; 90+ dollars rose | CARL's Q4 read; CHG-RED-045 to 11/17 |

## Thresholds and owner clocks
`PROME/GATES.tsv` remains the action-gate ledger. Its current condition, consequence, owner grade and review date control; this memo does not regrade other desks. The November 10 refresh gate passed at 16:14 ET (run directory under `/tmp`, not durable); that is not whole-fleet evidence freshness.

- **Credit:** HY >320 run MET, eight observations; strict <260 ×2 rekill 0 of 2; REG-T-04 (350) 0 of 3; 069 2-of-2 FIRED, unchanged (owner grade; L1 and L4 NOT FIRED on the 11/9 session, which adds no leg; L4 ungradeable 11/11 to 11/12); 076 1 of 3, review November 13; 069/079 review November 12 (LIQUID 11/9; GATES governs).
- **Cards (approval is not a fill):** HYG ×5 (WQ-615 A) FIRED on HY 348 [11/5] vs >344, UNFILLED as far as any desk knows; the up-day entry condition is waived on this card only (WQ-663 B); any session through December 4 at ≤$0.60, read off the broker; the order is Will's hand. HYG ×4 (WQ-513 A) NOT FIRED, 0 of 3 above 350; if it fires while the ×5 is filled the pair needs Will's word. ORCL card NOT FIRED. UNG ×5 ended by Will November 7, no fill.
- **Funding:** LIQ-079 NOT ARMED; ARM = SOFR99−IORB ≥+30 bp on 2 consecutive non-calendar days.
- **Private credit:** GATE-BRK-R2 review November 16, then December 7; leg (a) latched per WQ-563 A.
- **Energy / theaters:** BRENT boundary #1 not met; GATE-FALCON-001 review November 11.
- **Rates / equity:** HEN-57 NOT FIRED; HEN-62 RESOLVED-HIT; HEN-58 PPI ladder November 13; HEN-63 (hike at the 12/9 FOMC, 0.70) open; BOND 30Y I′ bar 63.89 on November 12.
- **Rhine / metals:** AEOLUS C5 →5 FIRED, score 5; metals actual 13/20; WQ-451 tests registered.
- **Near-term calendar:** Wed Nov 11 — Veterans Day, bond market closed; HY 11/10 cell; RED re-review; FALCON weekly; Skydance 10-Q if filed. Thu Nov 12 — claims, 30Y auction, Car-Mart standstill date, Nebius, Athene's call, RED FT-06. Fri Nov 13 — PPI, Cable One hearing, COT. Mon Nov 16 — GATE-BRK-R2 review. Tue Nov 17 — Nvidia, NEXUS weekly. → `PROME/state/CALENDAR.md`; `PROME/DOCKET.tsv`.

## Book state
Book $44,607.15 · cash 71.45% · broker export received 2026-11-10 · marks as-of 2026-11-10 intraday · 0d since receipt — not live, re-check before any fill

Generated by `python3 PROME/tools/will_brief.py --book-line`; broker truth and reconciliation belong to `FORGE/STATUS.md` (c4022901e8, ANVIL's reconcile of Will's 11/10 captures: Fidelity ties at $44,607.15; Robinhood $440.86 is derived and does not tie). Will declined the 8/8 history export (WQ-548): realized results before 11/2 stay DERIVED. Current dispositions are not inferred from calendar passage. No expiry reminders or sell/roll prompts (`USER.md`).

## Kernel
Gate C carve-out ④ remains INACTIVE pending its separate activation ruling. Planning or installation grants no operational authority. → `PROME/HEARTBEAT_COLD.md` §K / §K.1; DOCKET L247.

## Kill-on-sight at this cut
Do not assert: "CPI caused the December repricing" (Waller's 04:00 ET speech moved it 82% to 99% before the print); "the market prices 50 bp in December" (+28.2 bp, one hike plus about 13% of a second); "December +28.2 bp is a settlement" (vendor last trade); "the auctions failed" (soft indirect share, dealers under 10%, no composition failure); "VIX closed above 20" (19.46, on the print); "HY widened on CPI" (the 11/10 cell is unpublished; HYG fell on rates); "REG-T-04 fired" (334, 0 of 3); "the HYG card was filled" (no fill known); "the oil fall means supply returned" (no barrels; Qatar's interim terms unconfirmed and denied); "EIA measured a surplus" (a forecast); "SoftBank reported 22%" (15.9% at September 30; 22.5% is SAM's roll) or "SoftBank is over its ceiling"; "NEXUS weights are 26/41/33" as current (retired, WQ-664 B); "card delinquency is falling" without "90+ dollars rose"; "the kill rule fired at CARL" (the superseded wording only; the ratified rule reads NOT FIRED); "a Microsoft cut defaults IREN's loan" (BROCK's reading says no); "food at home shows fertilizer transmission" (beef and snacks, cereals flat); "the US confirmed striking Qeshm" or "the US did not strike Qeshm" (graded a US strike, not explicit); "Iron Gate is a strike or a campaign" (a staff unit); "the ceasefire legs prove the US struck first"; "mediation ended"; "the Call Report run confirmed breadth" or "the 8/20 score ranks the banks" (one unsized limb; no skill shown); "stress is spreading across the tier" and "concentrated, full stop"; "Flagstar's +$202M" as the signal (about $77M real); "the BDC discount fell" (a NAV refresh); "Oracle, Microsoft and SoftBank are one financing loop"; "Oracle CDS is at 3.25%" or "3.25% was never reached"; "Microsoft dropped older chips, contained"; "SoftBank has a $40B bridge wall" (repaid and cancelled); "IREN is fully funded" or "IREN was refused financing"; "the freeze thesis is dead on a strong print" (stood down on its letter by 15,000); "the diesel low is unpriced" (BRENT: PRICED); "no Hormuz halt means flow is normal" (flow NOT MEASURABLE); "October 30 gold was liquidation"; "funding is fine everywhere" (private and offshore unmeasured); "the ban runs through year-end" (January 31, 2027); "ORACLE graded a December hike" (raw cells); "Amazon cut capex"; "credit widening automatically pays regional puts"; "AI announced financing equals funded capex"; "gold score flipped". The prior cuts' lists stay binding in the exact archives.

## Pointers and binding limits
`PROME/HEARTBEAT_COLD.md`: §32.1/2/3/5/7/B retain older channel detail; §30.4 Japan; §29.8 metals; §KOS through §KOS.16 binding except named retirements; §B.1/§D.2/§K/§K.1/§R/§R.2/§C/§S standing rules; §19.2R vendor defects. The prior base and its amendments are preserved verbatim in the archive above. Prior spot levels, expired date language and superseded synthesis there are historical evidence. No guard is silently retired; current corrections replace the specific former claims only.

## HEARTBEAT Cadence / Ownership
PROME owns this file; cadence and HOT/COLD structure remain at cold §C. Byte budget 32,550 B; rotate at 75%, stop below 70%; channel paragraphs target ≤600 B. Measure with `PROME/tools/measure.py`. This is a DOMAIN synthesis refresh, no process-rule change. Plan/read record above carries declared residue and source limitations.

## Skip
Tuesday-evening synthesis of the dated evidence above. X1 CLOSED / DON'T-SIZE and energy STAND DOWN remain. $0 moved by PROME. Owner grades, current broker truth and future qualifying observations are not supplied by this memo. Research follow-through and coordination resume at `PROME/SCRATCH.md` § Next, in order.
