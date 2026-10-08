# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure. **Last session update:** 2026-10-08T16:46:23-04:00 — ninth wake (WQ-390, PROME `prome-7c`): 30Y reopening, F2 buyback, FR2004 9/30, PMMS, official 10/8 curve, whole WALTER lane drained. **Last real data refresh: 2026-10-08.**

October8 primary Treasury curve and October7 credit observations below are separate frontiers. Full evidence, auction arithmetic and source gaps: `analysis/2026-10-08_ninth-wake/REPORT.md` (prior: `analysis/2026-10-07_catchup/REPORT.md`).

## Current judgment

**The 30Y reopening cleared clean at the highest 30Y auction yield since August 2000, and the long end then rallied.** 10/8 30Y-R indirect 72.32% of competitive accepted vs the frozen 63.89 bar; high yield 5.618%; official 30Y closed 5.60% (−7bp). Expensive, not broken. Downgrade counter now 2, below 3 required.

**The 9/23 dealer build that MET the WQ-291 kill letter unwound in one week** (3–6Y $60.079B → $52.885B as-of 9/30). The letter's window is closed and stays MET on its first-published cell; not re-graded. The unwind supports rider ① (net inventory is not warehousing). **WQ-357 LATER/path C to October14; NO-ADD (WQ-280) unchanged.** Operational exit recommendation remains via TERRY and Will; funding window UNGRADED. TLT Oct16 82P ×1 and TBT10 per the 10/7 broker capture; no fill inferred. WQ-339 drafting only; WQ-360 fill unapproved.

## Regime
<!-- bond-state: thesis=v1.2.11; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=HOLD-NO-ADD -->
C-36 TWO-PART: policy-path channel alive; term-premium contribution remains separate. Governor Waller (10/8, primary per WALTER -030) anticipates "additional hikes"; vendor strip still prices about one hike by year-end. No new policy decision, capital approval or thesis version change.

## Current dashboard

| Metric | Observation | Source / basis |
|---|---|---|
| 2Y / 5Y / 10Y / 20Y / 30Y | 4.75 / 4.99 / 5.22 / 5.64 / 5.60%; daily−2/−4/−6/−7/−7bp | [CONF PRIMARY Treasury official par CSV10/8, pulled10/8 16:38ET] |
| 2s10s / 2s30s | 47 / 85bp; daily−4/−5 | [EST same-date Treasury subtraction10/8] Bull flattener |
| Real5Y / 10Y / 30Y | 2.62 / 2.87 / 3.31%; daily−4/−5/−5bp | [CONF PRIMARY Treasury real CSV10/8]; 30Y real 6bp under 3.37[10/5], the 2026 high |
| 10Y / 30Y nominal minus real | 2.35 / 2.29%; daily−1/−2bp | [EST same-date par−real10/8]; rally mostly real-led |
| 5Y5Y forward | 2.35%,15bp below2.50 | [CONF MIRROR FRED T5YIFR10/7] |
| ACM10Y TP / KW10Y TP | 0.9848%[10/7] /1.0847%[10/2] | [EST NYFed model / FRED model mirror]; windows differ |
| Fed path | October hold/+25 proxy18%; calendar-weighted YE≈+24.2bp vsEFFR3.88[10/7] | [EST CBOT ZQ vendor evolving bar10/8 16:41ET, NOT settlement]; Nov3.925/Dec4.065; independent FedWatch/OIS unavailable |
| HY / CCC / IG OAS | 309 /1229 /82bp[10/7]; daily+6/+15/−1 | [CONF MIRROR FRED ICE latest vintage]; tail deterioration continues |
| BBB / BB / B OAS | 102 /189 /308bp[10/7]; daily0/+4/+6 | [CONF MIRROR FRED ICE latest vintage] |
| CCC−BB | 1040bp[10/7] | [EST1229−189]; not an aggregate issuance freeze |
| SOFR−IORB | −2bp[10/7:3.88−3.90] | [CONF MIRROR FRED same-date]; LIQUID owns funding interpretation |
| FR2004 long end | $133.1B[9/30],−$7.5B w/w;3–6Y$52.885B (−$7.194B) | [CONF NYFed as-of9/30, pulled10/8 16:37ET]; next as-of10/7 due10/15. Stock≠auction flow |
| Mortgage survey | PMMS7.40%[10/8]; survey minus same-date10Y218bp | [CONF Freddie / EST difference];180–230 rearm band not breached; not MBSOAS |
| Global rates / metals / oil / volatility | HANS/SAM · MIDAS · BRENT · VIOLET | Owner sources; Bund fitted10Y3.57[10/8 Bundesbank] for VX19 only |

## Gate distances and derived counts

| Gate | Observation / state |
|---|---|
| Real10Y ≥2.50 sustained | Treasury10/8 2.87, through37bp; Treasury2026-series run21. WQ246 H.15 five-close sustain remainsMET; NO-ADD |
| OLD auction add rearm | MET9/23, add DECLINED WQ280; no new fire10/6–10/8 |
| Paired kill WQ291 | MET10/1:3–6Y$60.079B vs$56.586B; window closed, first-published governs; as-of9/30 $52.885B reported, not graded. Will deferred to10/14 |
| Inflation anchoring | T5YIFR2.35[10/7],15bp below2.50 |
| HY row4 / issuance | HY309[10/7],9bp through300 marker,41bp below350; capital gate separate |
| CCC escalation | 1229[10/7]>1100, fired previously; no invented score5 rule |
| Credit-equity lead | HY+46 from263;29–54bp short of+75–100; VIX leg→VIOLET; inactive |
| 30Y ≥5.00 | Treasury2026 scan through10/8:83/194 observations,current run67. No carried FRED rank for the later Treasury cell |

## Convergence Matrix

| # | Target/Vector | Score | Status | Key signal | Upgrade trigger |
|---|---|---:|:--:|---|---|
|1|Long end/duration (VX-BND-05 / VX-BND-12 / VX-BND-14)|5|🔴🔴|30Y auction stop 5.618, highest since 2000-08; prior paired kill confirmed|Top score |
|2|Treasury auction health (VX-BND-01 / VX-BND-08 / VX-BND-13)|4|🔴|10Y and 30Y clean after the 3Y marker; counter2|Second composition failure with confirmed mechanism leg |
|3|Dealer absorption (VX-BND-04 / VX-BND-16)|2|🟡|FR2004 9/30 long end −7.5B, 3–6Y build unwound; four F2 reads OFF|Two total-stock builds with weak composition or funding confirmation; F2 newest-vintage fire |
|4|HY market function (VX-BND-02 / VX-BND-11)|3|🟠|HY309/CCC1229[10/7], bifurcated; no comprehensive pulled-deal census|HY>350 or verified pulled-deal cluster |
|5|IG market function (VX-BND-03 / VX-BND-10)|1|🟢|IG82[10/7],38bp below120|IG>120 or verified failed syndication |
|6|CDX/cash basis (VX-BND-06)|1|🟢|No new true-CDX observation; source gap persists|Confirmed fast-layer lead |
|7|Credit-equity lead (VX-BND-07)|1|🟢|HY+46 from263, spread leg unmet|HY+75–100 from263 withVIX<20 |

**Composite17/35 =5+4+2+3+1+1+1, unchanged10/8.** One5,one4,one3,one2,three1. October8 30Y-R indirect72.316983%, dealer6.793651%, BTC2.54; clean on pooled63.89 and alternate61.20. **Counter0→1 (10/7 10Y)→2 (10/8 30Y).** No second confirmed mechanism failure.

Outside composite: VX-BND-15=2; VX-BND-17=1 (PMMS spread218bp inside band); VX-BND-18=2; VX-BND-19=3, disorderly qualifier NOT defined 10/8 (no bar authorized; base rate prepared, re-dated10/14); VX-BND-20=2, next review10/14.

## Exit / falsification and positions

1. WQ157 paired kill: I-prime plus non-auction confirmation. WQ291 9/23 dealer leg MET; recommendation remains exit-all-duration-shorts via TERRY/Will, deferred under WQ357. Net inventory≠warehousing (9/30 unwind −$7.194B); funding window UNGRADED. I-prime alone is a rarity marker. Leg② PARKED.
2. Position-specific:10Y<4.15 AND30Y<5.0 for3 sessions AND clean refunding; current levels do not meet. TLT Oct16 82P×1 and TBT10 per 10/7 capture; TERRY owns sell-or-roll management. No executable marks here.
3. Convergence downgrade: three consecutive nominal coupons with indirect≥own median AND dealer≤own median. **Counter2 as of10/8.** TIPS/FRN excluded. Next nominal coupon 10/21 20Y-R could reach3.
4. Predictions OPEN0; next curve-shape registration due10/21. VX-BND-09 auction tails RETIRED/unscoreable.

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| **Thu10/8 ✅** | COMPLETED: 30Y-R clean, counter2; F2 OFF (4/4); FR2004 9/30 read; PMMS7.40; official curve | VX19 qualifier NOT defined → re-dated10/14 |
| **Wed10/14** | WQ357 decision clock; CPI08:30; BeigeBook14:00; VX-BND-20 review; VX19 define-or-retire ruling | Same-date real/nominal split;Will/TERRYreview |
| **Thu10/15** | F2op10–20Y; FR2004as-of10/7; PMMS | Carrier read to RED; stock vintage |
| **Fri10/16** | Held TLT82P expiry | TERRY sell-or-roll rail; Will approval, no automatic order |
| **10/21 ·10/22 ·10/26–29** | 20Y-R;5YTIPS;2Y/5Y/FRN/7Ycluster | Bars at announcements;FRN excluded from I-prime; 20Y-R can make counter3 |
| **Wed10/28 14:00** | OctoberFOMC; UK Budget same day | Register curve-shape row with base rate by10/21 |
| **10/27 ·11/4** | F2op;QRAandF2op11/4 | F1/F3;schedule window ends |
| **11/9 ·11/13 ·12/1 ·2027-01-25** | FHLBQ3;FRBNYFX;USsovCDSretest;Norwegian expert report | As docketed |
| **12/9 14:00 ·2027-01-27** | DecemberFOMC+SEP;JanuaryFOMC | Prediction rows by12/2 and1/20 |
| **—STANDING—** | MOFFX;Warsh task force;FR2004;credit;F2carrier | Own source frontiers and recorded scope |

---


## BOTTOM LINE

Real money bought the 30Y at a 26-year-high auction yield without flinching, and the long end rallied 7bp afterward; the auction mechanism is working, the price of duration is what keeps rising. The dealer build that triggered the kill letter unwound within a week, which reads as distribution rather than stuffing — the letter stays MET as ruled and the exit decision stays Will's on 10/14. Independent dated FedWatch/OIS, true CDX, paid MBS OAS, comprehensive failed-deal coverage and executable broker data remain unavailable.
