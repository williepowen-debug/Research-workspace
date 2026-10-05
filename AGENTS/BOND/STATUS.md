# BOND — Status

**Agent:** BOND · **Domain:** US bond-market structure (+ MBS/FHLB + EU rates per the 6/27 extension; + the sovereign-credibility instrument set per the 8/10 forum — scope in `CLAUDE.md`)
**Last session:** 2026-10-05T10:38:00-04:00 — live primary-source research refresh; WQ-357/L608 written read delivered. Official rates through 10/2, credit through 10/2, dealer as-of 9/23, vendor quotes stamped individually. Full read: `analysis/2026-10-05_WQ-357_rebound-research.md`.

> 📕 **HOT/COLD SPLIT — NOTHING DELETED.** Pre-rotation snapshots (`domain/sources/`): **`2026-10-01_STATUS_full-snapshot_pre-refresh-rotation.md` (crc32 `735109674`)** · `2026-09-29b_…pre-intraday-rotation` (`2392892541`) · `2026-09-29_…pre-row4-rotation` (`2518256656`) · `2026-09-28e` (`2516058915`) · `2026-09-28d` (`319142979`) · `2026-09-28c` (`1800580424`) · `2026-09-28b` (`2552442073`) · older `2026-09-28_` · `2026-09-24`. **Budget 32,550 B; rotate-tier ≥75% — rotate, never raise.**

**Canonical elsewhere — no second copy here:** thesis → `thesis/THESIS.md` · predictions → `thesis/PREDICTIONS.tsv` · catalysts → `docket/CATALYSTS.tsv` · gates/positions → `TRADE.md` · learnings → `MEMORY.md` · handoff → `SCRATCH.md`.

---

## 🔴 TOP OF FILE — what changed since 9/29

**CURRENT PRIORITY — 2026-10-05T10:38:00-04:00. WQ-357 LATER stands: hold recorded sleeve on TERRY path C to 10/14, NO-ADD unchanged. L608 written rebound research delivered to PROME today; no new trade recommendation.** Latest completed evidence shows policy-path relief and Friday credit tightening, while long real yields remain high. Composite 17/35 unchanged; kill MET remains operational, funding window UNGRADED, inventory is not proof of warehousing. WQ-339 is card drafting only; WQ-360 fill unapproved. Research → `analysis/2026-10-05_WQ-357_rebound-research.md`.

**Fresh results:** HY 310 / CCC 1202 / IG 85bp [10/2]; Treasury 10Y 5.28 / 30Y 5.63%, real 10Y 2.92% [10/2]. The 10/1 F2 read is OFF-THE-RUN (newest-vintage share 0%); the full $6B cap was accepted and a durable RED packet filed. TGA draw verified at $90.347B, but the 10/1 operation settled 10/2, so the proposed same-day buyback attribution fails. Jefferson speech does not explicitly attribute yields to term premium; prior wording corrected. Prior event detail preserved at `domain/sources/2026-10-05_STATUS.md_pre-live-refresh` and dated reports.

**Next:** 10/6–8 $119B coupon auctions; frozen two-decimal hand-grading selected while the tool tie-band defect stays open. FOMC minutes 10/7 at 14:00 ET; FR2004 and F2 operation 10/8; CPI and held-position clock 10/14.

## Regime (one-line)
<!-- bond-state: thesis=v1.2.11; regime=C-36-TWO-PART@2026-09-01; gate_a=MET@2026-09-10; rearm=MET@2026-09-23; add=DECLINED@WQ-280; kill=MET-REC@2026-10-01; posture=HOLD-NO-ADD -->

**Real-rate / higher-for-longer. Policy-path relief since 9/28 is recorded; the latest vendor proxy still prices about one year-end hike.** C-36 TWO-PART (ruled 9/1): policy-path channel ALIVE · term premium drove the July delta. **9/16 FOMC +25bp to 3.75–4.00 (12–0); the curve priced ABOVE the SEP median (4.125) and then kept going (`BND-26`).** **Auctions: "expensive, not broken" is UNDER TEST — first OLD-conjunctive fire on the live-graded record (9/23 5Y); its WQ-291 dealer leg printed MET 10/1 (3–6Y +$12.1B) ⇒ kill letter MET ⇒ recommendation via TERRY + Will — **EXIT DEFERRED BY WILL 10/3; PATH C TO 10/14 (WQ-357)**; funding window UNGRADED.** Full ruling → `thesis/THESIS.md` **v1.2.11**.

---

## Current Dashboard

*Rates: Treasury official10/2 par/real CSV, independently re-pulled10/5 10:23 ET; H15 frontier remains10/1. Credit10/2: HY/CCC/IG first-published and latest-vintage agree; tiers latest-vintage. Futures10/5 evolving vendor bars, not exchange settlement. Raw source snapshots and method at `analysis/2026-10-05_live-refresh/`.*

| Metric | Current | Status | Source / Date |
|---|---:|---|---|
| 30Y par (DGS30) | **5.63%** [10/2] | 🔴🔴 | [CONF **U.S. Treasury par curve 10/2**; +2bp on day, −1bp 2-day vs 9/30 5.64] — long end gave back much of Thursday’s rally; 20Y 5.67 on 10/2 versus 5.68 on 9/30. Historical ranks require the dated whole-series calculation |
| 10Y par (DGS10) | **5.28%** [10/2] | 🔴 | [CONF Treasury10/2; re-pulled10/5] +4bp d/d; only−1bp vs9/30. Official completed par yield, not10/5 live screen |
| 5Y par (DGS5) | **5.06%** [10/2] | 🔴 | [CONF Treasury **10/2**; +5bp on day, −3bp 2-day vs 9/30 5.09] — belly held some of the NFP rally but less than the 2Y |
| 2Y · 1Y · 3M par | **4.83% · 4.46% · 4.19%** [10/2] | 🔴 | [CONF Treasury **10/2**; 2Y +5 on day, **−5bp 2-day vs 9/30 4.88 — the Fed-path leg of the dovish repricing**] — 2s10s +45 (vs +41 9/30, +4), **2s30s +80** (vs +76 9/30, +4): Friday was a **bear flattener** after Thursday’s bull steepening; over both days, 2s10s and 2s30s steepened by 4bp |
| **10Y real (DFII10)** | **2.92%** [10/2] | 🔴🔴 **GATE THROUGH · SUSTAIN MET** | [CONF **Treasury real curve 10/2**; +4bp on day vs 10/1 2.88; **−1bp 2-day vs 9/30 2.93**] — **30Y real 3.34** (versus 3.33 on 9/30); 5Y real 2.69 (+4 on day, −4 2-day); the day was **real-yield-led, breakevens flat/down**. WQ-246 sustain met; authorises no add |
| 5Y5Y fwd (T5YIFR) | **2.35%** [10/2] | 🟡 | [CONF FRED10/2 latest-vintage,10/5 pull] 15bp below2.50; Treasury-derived frontier leads H15 |
| 10Y BE | **2.36** [10/2 par−real] | 🟡 | [10/2 par−real: 5.28−2.92 = 2.36; 5Y BE 2.37, 30Y BE 2.29] — BE flat on day; real yield did the lifting ⇒ supports the thesis directly (real-rate-driven, not inflation-exp) |
| ACM 10Y TP · KW TP | **0.9050** [10/1] · **1.0203** [9/25] | 🟠 | [EST NY Fed ACM Daily latest-vintage;FRED KW,10/5] ACM+2.0bp1obs/+17.8bp5obs. Distinct models/windows, not a causal decomposition with FF |
| **Fed path (FF futures)** | **10/28 hold/+25 proxy≈22%; YE≈+25.9bp vs EFFR3.88** | 🟠 | [EST CBOT ZQ via yfinance10/5 10:23 evolvingbar;EFFR10/2] November3.935/December4.080; calendar-weighted YE=(31×Dec−9×Nov)/22. About one hike; not OIS/FedWatch verification. Full strip peak remains a separate horizon, see live tool report |
| **HY OAS** | **310bp** [10/2] | 🟠 | [CONF FRED first-published=latest-vintage,10/5] −14d/d from324;10bp through300,40bp below350;row4 remains3 |
| **CCC OAS** | **1202bp** [10/2] | 🔴 | [CONF FRED first-published=latest-vintage,10/5] −13d/d from1215;1100 escalation remains fired. Legacy1200 field crossed by2; explicit score letter →4@1100 preserved, no invented →5 rule |
| IG · BBB · BB · B OAS | **85 ·104 ·191 ·312bp** [10/2] | 🟢 ·🟢 ·🟡 ·🟡 | [CONF FRED10/2;IG first-published checked,tiers latest-vintage] Friday−1/−2/−13/−17bp |
| CCC−BB tail gap | **1011bp** [10/2] | 🔴 | [EST same-date FRED subtraction1202−191,10/5] tail stress remains despite Friday credit relief |
| **FR2004 long-end** | **$140.5B** [as-of 9/23] | 🟡 | [NY Fed, published 10/1 between 16:13 and 16:15 ET] — **−$3.8B w/w**; 7-11Y $34.2B (−0.9), 11-21Y $68.5B (0.0), >21Y $37.8B (−3.0). **3–6Y $60.079B (+$12.093B) = WQ-291 MET** (`KB-BND-383`); 6–7Y $23.199B (−4.646). Next: as-of 9/30 Thu 10/8 |
| **SOFR − IORB** | **−2bp** [10/2 shared date] | 🟡 | [CONF FRED SOFR3.88−IORB3.90,10/5] latest funding context; does not grade the UNGRADED9/23 auction funding window. LIQUID owns interpretation |
| TLT · TBT | **$77.25 -0.30% ·$42.80 +0.61%** | 🟠 | [vendor yfinance captured 2026-10-05T10:23:03.784786-04:00] Momentary quotes; re-pull at a decision. Broker positions not newly confirmed |
| Mortgage30Ysurvey | **7.28%** [10/1] | 🟠 | [CONF FreddieMacPMMS10/1,+25bpw/w] Survey−same-date10Y=204bp,inside180–230band;notMBSOAS. VX17still1 |
| Global 10Y | → HANS (EU/UK) · SAM (JGB) | `[HANS/SAM own]` | WQ-317 page (`KB-BND-375`) carries the 9/21→9/30 table; 10/1 Bund rallied ~8–9bp (HANS correction). Name the basis (`KB-BND-319`) |
| USD/JPY · oil · VIX | **cite SAM · BRENT · VIOLET** | — | this desk keeps no copy (vendor Brent front quote on 9/28 looks like a roll artifact — do not use) |

### Gate distances *(recomputed this session, never carried)*

| Gate | Distance | State |
|---|---:|---|
| **DFII10 ≥2.50 — TLT-put add-gate(a)** | 🔴 **THROUGH by42bp** [2.92,Treasury10/2] | WQ246five-close sustainMET. Treasury real-series run**17**from9/10;FREDH15frontier10/1 separate. NO-ADD remains; no capital approval |
| **Auction re-arm (OLD conjunctive) — TLT-put add-gate** | 🔴 **MET 9/23 (5Y)** | ✅ **ADD DECLINED — WQ-280 RULED 9/24 13:17 ET.** Spent on 004 |
| **Kill dealer leg, 9/23 5Y (WQ-291)** | 🔴 **MET by +$3.493B** [3–6Y $60.079B vs $56.586B, as-of 9/23] | ✅ **KILL LETTER MET 10/1 ⇒ RECOMMENDATION — TERRY card `MGMT-DURSHORT-EXIT-WQ291` written; EXIT DEFERRED BY WILL 10/3; PATH C TO 10/14 (WQ-357 LATER; decision clock 10/14); no action**; funding window **UNGRADED** by ruling |
| T5YIFR >2.50 | **15bp** [2.35,FRED10/2] | 🟡 unbreached |
| DGS30 >5.00 · DGS10 >4.50 | — | 🔴 BREACHED. Treasury30Y2026-series maximal run**63**[10/2],79of190 year observations; separate FRED whole-series run62[10/1]. No frontier mixing |
| HY OAS >300 (BOND row4 marker; X1 capital gate remains separate) | **THROUGH by10bp** [310,10/2] | 🟠 marker remainsMET; no capital reopen |
| CCC >1100 escalation | **FIRED 9/24** (+12; +28 on 9/25) | 🔴 `BND-27` FALSE |
| Credit-equity lead (HY+75–100from263,VIX<20) | **28–53bp** | 🟡 HY310[10/2]=+47; below338–363; VIX→VIOLET |

---

## Convergence Matrix

| # | Vector | Score | Status | Rolls up (`workbook/VX.tsv`) | Key Signal | Upgrade Trigger |
|---|---|---:|:--:|---|---|---|
| 1 | Long-end / duration | **5** ▲ | 🔴🔴 | `VX-BND-05` · `VX-BND-12` · `VX-BND-14` | **▲4→5 10/1 on its letter: the paired kill's mechanism leg CONFIRMED (WQ-291 3–6Y MET, `KB-BND-383`).** 6 straight fresh DGS30 highs → 5.64 [9/30], highest since 2002-07-08; 10Y 5.29 > its 2007 high (`KB-BND-372`) | Top score. Watch: 10/7 10Y-R, 10/8 30Y-R (bars frozen 10/1, `KB-BND-377`) |
| 2 | Treasury auction health | **4** ▲ | 🔴 | `VX-BND-01` · `VX-BND-08` · `VX-BND-13` · ~~`VX-BND-09`~~ RETIRED (tail) | **▲3→4 10/1 on its letter: composition failure (9/23 5Y, OLD + `I'`, clean pool `KB-BND-377`) with the FR2004 leg CONFIRMED (WQ-291 MET, `KB-BND-383`).** BTC 2.21 < 2.28 cover bar; 7Y `I'` by 0.04pp. ⚠️ net inventory ≠ proof of warehousing; funding window UNGRADED | ⇒5: a second composition failure with a confirmed mechanism leg |
| 3 | Dealer absorption | **2** = | 🟡 | `VX-BND-04` ·`VX-BND-16` | FR2004latest9/23 TOTAL$140.545B,−$3.828B;two-buildletterunmet. F2allthreeopsOFF(10/1zero newest share) | Two consecutive TOTAL builds with weak composition, or positive funding; F2newest-vintage fire |
| 4 | HY market function | **3** = | 🟠 | `VX-BND-02` ·`VX-BND-11` | HY310/CCC1202[10/2];Fridayrelief recorded. Paramount9/30 securedfinancingpriced;oneissuerhasaccess,notbroadcensus | ⇒4:HY>350orverifiedpulled-dealcluster;capitalgate separate |
| 5 | IG market function | **1** = | 🟢 | `VX-BND-03` ·`VX-BND-10` | IG85bp[10/2];35bpbelow120;no comprehensive failed-syndicationcoverage | IG>120orverifiedfailedsyndication |
| 6 | CDX-cash basis | **1** = | 🟢 | `VX-BND-06` | HYG/IEF0.8651,z20+0.96[10/5evolving];rateconfounded,fastercashproxy | Genuine fast-layerleadwithcashconfirmation;trueCDXunavailable |
| 7 | Credit-equity lead | **1** = | 🟢 | `VX-BND-07` | Inactive;HY+47from263[10/2],28–53bpheadroom | HY+75–100from263withVIX<20 |

**Composite: 17/35 — re-summed 10/5; prior ▲2 on 10/1** (row 1 4→5 and row 2 3→4, each on its registered letter, on the WQ-291 dealer leg MET, `KB-BND-383`). Prior: 15 since 9/29. Distribution: 🔴🔴 1 · 🔴 1 · 🟠 1 · 🟡 1 · 🟢 3. **Re-summed: 5+4+2+3+1+1+1 = 17 ✅.** `VX-BND-01` / `-05` written back 10/1.

**Outside the composite:** `VX-BND-15` inflation anchoring (2) · `VX-BND-17` MBS relay (1) · `VX-BND-18` FHLB (2) · `VX-BND-19` EZ rates (3 — HANS: ECB T-04 no longer a hawkish lean; German 2027 debt service +38%; "disorderly" UNDEFINED → 10/1) · `VX-BND-20` benchmark UST demand (2, checkpoint 10/6).

### Prediction scoreboard *(canonical: `thesis/PREDICTIONS.tsv`)*

**OPEN: 0.** **Resolved 10/1:** `BND-30` **TRUE** (70%; ACM 9/29 TP share 2.36, `KB-BND-373`) · `BND-31` **TRUE** (65%; JGB 30Y −2.8bp, `KB-BND-374`). 9/28: `BND-27` FALSE. 9/24: `BND-25` TRUE · `BND-26` FALSE. **Tally: 16 TRUE · 13 FALSE · 1 VOID.** Archives: `thesis/archive/PREDICTIONS_resolved_*`. **Owed: the 10/28 FOMC curve-shape row by 10/21** (OPEN = 0).

---

## Trade Interface *(full view → `TRADE.md`; construction is TERRY's lane)*

- **TLT Sep-30 77P — GONE** (sold 9/30 per PROME's spawn brief; FORGE/TERRY carry the fill). **The duration-short sleeve today = TLT Oct-16 82P ×1 + TBT 10 sh; NO-ADD holds (WQ-280).** Both add-gates read through and **neither is an add** (WQ-280 · 7/16 NO-ADD · root rule #5). *Posture, never a direction.*
- **HYG puts — closed at the INDEX level.** HY 302 [9/28] = BOND's 300 marker MET 9/29 — **analytical only, NOT a capital reopen**: the index-protection SIZING question sits behind LIQUID's X1 gate, CLOSED 8/28 (BROCK `KB-BRK-219`, wrapper half NOT ARMED; fail-safe DON'T-SIZE); it reopens only via BROCK's **10/02 re-adjudication sitting** (DOCKET L494), then TERRY's card + Will. CCC tail FIRED 1100 → expression single-name/CCC, **never HYG**. Registered HY lines: RED-FT-01 (RED's) · LIQUID X1. *(Corrected 9/28 15:22 ET on PROME's relay; provenance → snapshot `2026-09-29b`.)*
- **TLT Oct-16 82P ×1** (×2→×1 9/28: 1 SOLD @ $3.60, net $359.34 — FORGE `b997a01ce`; ITM) — **TERRY's management card** (`AGENTS/TERRY/setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md`); BOND carries no posture on it. **10/1: BOND's kill rec ⇒ TERRY exit card `MGMT-DURSHORT-EXIT-WQ291` (A both Fri 10/2 · B 82P only · C hold to 10/14) — WQ-357 LATER (Will 10/3), path C to 10/14.**
- **Credit-equity lead — inactive.**

---

## Exit / Falsification *(full set → `thesis/THESIS.md`)*

**1 · THESIS KILL (exit all duration shorts).** WQ-157 leg ① (Will 9/4): **`I'` + a NON-AUCTION mechanism confirmation** (FR2004 dealer stock and/or SOFR−IORB). 🔴 **9/23 5Y dealer leg RULED (WQ-291, Will 9/26; `KB-BND-342`): FR2004 3–6Y as-of 9/23 ≥ $56.586B (PRE $47.986B) — ✅ MET 10/1: $60.079B, margin +$3.493B (`KB-BND-383`).** Riders: net inventory ≠ proof of warehousing; funding window for this fire UNGRADED (quarter-end excluded by the letter); no predictive claim; a fire = recommendation via TERRY's card + Will. Latest funding context → dashboard, not a retrospective grade — the dealer leg alone satisfies the "and/or" ⇒ **KILL LETTER MET 10/1 ⇒ RECOMMENDATION "exit all duration shorts" via TERRY's card (`MGMT-DURSHORT-EXIT-WQ291`) + Will's [Approve] (WQ-357) — EXIT DEFERRED BY WILL 10/3; PATH C TO 10/14; no action by this desk.** Leg ② PARKED (Will 9/25; `I'` ALONE = MARKER, `KB-BND-335`). Unpaired `I'` fires: 9/15 20Y-R · 9/23 5Y · 9/24 7Y. Also: 10Y back below 4.15 ×3 with clean auctions ⇒ spent. `I'` bars → `monitors/AUCTION_HEALTH.md` §GRADING BASIS (grader fix `KB-BND-314`, disclose if pre-fix pools are re-cited). 🔴 Direction disclosed: `I'` is the easier test and its firing confirms this desk's own bear thesis. Full history → THESIS + snapshots `2026-09-28d` / `2026-09-29b`.

**2 · POSITION-SPECIFIC.** Duration shorts (Oct-16 82P ×1, TBT): kill on 10Y <4.15 AND 30Y <5.0 ×3 sessions AND a clean refunding (THESIS §2). The 82P card is TERRY's (sell-or-roll rail, Will's 9/30 standing practice).

**3 · CONVERGENCE DOWNGRADE (trim).** Three CONSECUTIVE nominal coupons passing both legs (indirect ≥ median AND dealer ≤ median). **Counter 0** (2Y failed the dealer leg 13.19 vs 11.33; 5Y and 7Y failed indirect). Next eligible: 10/6 3Y.

**4 · TIME-BASED.** **WQ-357 LATER recorded 10/5; research delivered 10/5, decision clock 10/14** · 10/6–10/8 refunding (bars frozen 10/1) · F2 reads **10/8 · 10/15 · 10/27 · 11/4** · `VX-19` 'disorderly' qualifier (NOT done 10/1; re-dated 10/8) · `VX-20` **10/6** · FOMC curve-shape row **by 10/21** · Oct-16 82P expiry (TERRY) · FHLB Q3 **11/9** · FRBNY FX **11/13** · US-sov-CDS re-test **12/1** · next `I'` re-freeze **2027-01-04**.

⚠️ **RETIRED, NOT REVIVABLE: the auction TAIL.** The 9/23 "2nd biggest tail ever" wire claim is `[med-conf]` and fires nothing.

---

## Immediate Catalysts *(source of truth `docket/CATALYSTS.tsv`; human twin — same event SET)*

| Date | Catalyst | What BOND watches |
|---|---|---|
| **Mon10/5 ✅ delivered ·Wed10/14 decision** | L608writtenreboundread delivered;WQ357LATER/pathC | Existing recommendation unchanged;Will/TERRYreview10/14 |
| **Tue10/6** | VX20review;3Y$58B91282CRQ6;tie-bandfallback | Agencytaxonomyclosed;mandatewatchopen;frozen2dp hand-grade |
| **Wed10/7** | 10Y-R$39B91282CRF0 13:00;FOMCminutes14:00 | Composition;policy-path evidence |
| **Thu10/8** | 30Y-R$22B912810UW6;F2op;FR2004as-of9/30;VX19qualifier | Publishedprimary results;noanticipatorygrade |
| **Wed10/14 ·Thu10/15** | CPI08:30;BeigeBook14:00;heldpositionclock;F2op10/15 | Same-date real/nominal split;Will/TERRYreview |
| **10/21 ·10/22 ·10/26–29** | 20Y-R;5YTIPS;2Y/5Y/FRN/7Ycluster | IssuerPDFvisuallyverified10/5;barsatannouncements;FRNexcludedfromI-prime |
| **Wed10/28 14:00** | OctoberFOMC | Registercurve-shaperowwithbaserateby10/21;livepath→dashboard |
| **10/27 ·11/4** | F2op;QRAandF2op11/4 | F1/F3;schedulewindowends |
| **11/9 ·11/13 ·12/1 ·2027-01-25** | FHLBQ3;FRBNYFX;USsovCDSretest;Norwegianexpertreport | Asdocketed |
| **12/9 14:00 ·2027-01-27** | DecemberFOMC+SEP;JanuaryFOMC | Predictionrowsby12/2and1/20 |
| **—STANDING—** | MOFFX;Warshtaskforce;FR2004;credit;F2carrier | Ownsourcefrontiersandrecordedscope |

---

## BOTTOM LINE

The latest completed evidence has not established a sustained long-end rebound. Friday credit tightening and weaker jobs support relief; high real yields and model term premium counter it. WQ-357 LATER keeps the recorded sleeve on path C to October14, NO-ADD unchanged; the kill remains MET as an operational recommendation, with inventory and funding caveats intact. The written research is delivered at `analysis/2026-10-05_WQ-357_rebound-research.md`. True CDX, paid MBS OAS/pulled-deal coverage, dated CME/OIS comparison and live broker truth remain unavailable.
