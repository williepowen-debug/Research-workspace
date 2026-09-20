# SAM STATUS

**Last written: 2026-09-19T15:5x+00:00 — Will-directed Saturday session, market CLOSED (prior block 2026-09-18 18:05Z).** 🟠 **PM UPDATE — CATO R4 RULED: SAM-28 regraded FALSE → `RESOLVED — QUALIFIED / NO-VERDICT`; SAM-31 stays FALSE with its reasoning replaced.** CATO upheld on 4 of 5 points; nothing graded TRUE. The decisive point was found by neither reviewer: the contemporaneous registration record the governing packet **ordered** me to consult was consulted only after challenge, and it favours the reading I rejected. [Ruling](docket/2026-09-19_CATO-R4-RULING.md). AM: both graded FALSE one day past the boundary on frozen terms, after two self-caught defects in my own prep file, both running in my own favour. Boot sweeps 15:15Z / 00:32Z: 12-13/13-14 scripts, BOJ OIS still DARK. Market rows are the **Sep-18 close** vintage — nothing re-marked on a shut market. [Grade record](docket/2026-09-19_SAM28_SAM31_GRADE.md). Book last recorded FLAT, not newly broker-reconciled.

**Signal Status:** ⚰️ **CARRY-CONVEXITY TAIL — RETIRED TO LOW (THESIS v1.7, 2026-08-07). Leg-1 SPF FIRED. Position FLAT; $0 was at risk.** · **v2.0 KILLED 8/20-27** (BIS K1 fired; RED's CHG-RED-048 killed it four more ways independently; cross-read `thesis/V20_CROSSREAD_2026-08-27.md` — nothing was owed to Will). · 🕯️ **v1.8 is a CANDIDATE and a SEPARATE document** (`thesis/V18_CANDIDATE_PILLAR1.md`), gated on SAM-41 + a separately-registered FX co-condition + RED pass + Will sign-off — **never on BIS**. SAM-41 historically confirmed but current gaps have widened back above both bars (**0/5**); use its dated rider, not the archived Aug-7 case. Distinguish FX level, cohort stocks and measured liquidation. ⛔ **NO SUCCESSOR FRAME DECLARED — v1.7 stands, and that is the honest state, not a gap to be filled.**

🔴 **The 8/7 print broke the frame.** CFTC Aug-4 **−45,473 = 24.2% of the corrected peak R = −188,077** — through the **−108K/60% leg-1 invalidation line**; character **REVERSAL, not liquidation**; book FLAT, $0 at risk. ⛔ The **"25.3% of −180K" form is RETIRED** (Will-ratified 8/11; only percentage labels moved, contract gates unaffected). 📌 Calibration residue: **45% assigned to CONFIRM, ~25% to what happened.** **Forensics, resolver narrative and the full lesson → `STATUS_ARCHIVE.md` § 2026-08-07 FRAME-BREAK FORENSICS.**

**Predictions:** **16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 1 OPEN (SAM-33)** — re-derived FROM `thesis/PREDICTIONS.tsv` (34 rows, 0 unclassified), not carried forward. SAM-28/31 both FAILED Sep-18. Canonical: `thesis/PREDICTIONS.tsv`.


*Detail → `thesis/THESIS.md` v1.7 · `CHANGELOG.md` 2026-08-07 · `outbox/2026-08-07_to-TERRY-PROME_RESOLVER-COMPLETE-section8-DE-LOAD-leg1-fired-frame-LOW.md` · pre-print re-pencil `thesis/REPENCIL_2026-08-07_PREPRINT.md` (committed BEFORE the print).*


---

## 2026-09-18 — BOJ MPM GRADE

↪️ **ROTATED 2026-09-19 PM → `STATUS_ARCHIVE.md` § 2026-09-18 BOJ MPM GRADE** (settled; full record `reports/2026-09-18_boj-mpm-grade.md`). **LIVE STATE:** BOJ raised to **1.25%, vote 7–2, effective Sep-24** — highest since 1995; **both dissents were for HOLD**, so the registered hawkish surprise **did NOT fire**. Composite clause graded a **MISS** (right direction, wrong mechanism). **CH-004 confirmed a third time: a fully-priced hike does not unwind carry.** **Consequences to the frame: none.**

---

## 2026-09-15 — News integration · September 10–11 notes

↪️ **MOVED 2026-09-18 → `STATUS_ARCHIVE.md` § 2026-09-15 NEWS INTEGRATION (rotated).** Settled; findings survive in the tables below.

## LIVE MARKET DATA

*FX, oil and FXY re-marked **September 18 17:44 UTC** (boot sweep `20260918T174437Z`); JGB curve is the MOF **Sep-17** publication. Each row keeps its own observation clock. ⚠️ **Intraday observations and completed sessions are distinct** — nothing below is a completed-session close except where labelled.*

| Instrument | Level / vintage | Note |
|---|---|---|
| USD/JPY | **156.69** [Sep-18 17:44:39 UTC, Yahoo `USDJPY=X`] | Live vendor observation, post-BOJ. Intraday path today 157.34 [15:01:50Z] → **156.69** [17:44Z] = **−0.41% off the post-decision high**; the yen has clawed back part of the decision-day weakness. Was 154.82 [Sep-15 02:27 UTC]. PROME's dashboard read **157.86 [10:21 ET]** — a different clock, not a disagreement; do not blend. 🔧 **Completed-session basis (WQ-162) RE-DERIVED this session: latest completed session = Sep-17 close 155.942** (Sep-15 155.092 · Sep-16 156.227 · Sep-17 155.942). Sep-18 is the current bar and is **never scored**. |
| **BOJ September pricing — SPENT** | Pre-decision **99% / OIS 1.2238%** [Sep-15 11:15 JST] | ⚰️ Meeting RESOLVED, hike delivered ⇒ fully priced, therefore **not** hawkish-of-priced. Later-meeting equivalents from that image are stale vintages, not current pricing. Boot 9/18 could NOT refresh: `boj_ois.py` returned an unreviewed chart (SHA256 `1105fdfc…`) needing visual review — **no current BOJ pricing on this desk.** |
| Brent / oil-in-yen | **Dec `BZZ26` $98.68 close** [Sep-18]; Nov `BZX26` $103.10 | 🔧 **CORRECTED 2026-09-18 (CATO R1, TERRY's same-day matched-contract evidence).** The earlier **“−7.5% in three sessions”** was a **ROLL ARTIFACT**: `BZ=F` tracked Nov `BZX26` through the 9/17 close (104.82) and **stepped to Dec `BZZ26` on 9/18** — a $4.42 Nov–Dec spread booked as a price move. **Matched-contract 9/15→9/18: Dec −4.48% · Nov −5.20%**, against −7.46% on the continuous quote ⇒ **overstated by 3.0pp.** ⚠️ The old figure also compared an **intraday 02:15Z** Sep-15 quote to an intraday Sep-18 quote — two basis defects, not one. ✅ **The DIRECTION and the inference SURVIVE at reduced magnitude:** crude fell ~4.5–5.2% on a single named contract while Petroline stayed shut (WALTER SIG-W-20260917-001), so supply event and price still move opposite ways. ⛔ **Not established: that the whole decline was a roll** — CATO did not establish that and neither do I. Benchmark-mismatch caveat stands (proxy prices off Brent; ~37% of receipts are US WTI-Midland-led crude). |
| JGB MOF **Sep-17** | **10Y 2.993 / 30Y 4.047 / 40Y 4.036%** | MOF curve, distinct from on-the-run quotes. All three above their watch levels; level alone identifies neither sales nor emergency capping. Pre-dates the 9/18 hike. |
| CFTC legacy JPY, Sep-8 | **Net +10,796**; long 178,791 / short 167,995; OI 499,635 | Δ long +61,622 / short −41,401 / net +103,023 / OI +87,753. New longs and short covering coexist; motive and forced liquidation are not identified. |
| CFTC TFF, Sep-8 | Leveraged net **−49,098**; asset-manager **−570** | Leveraged longs +23,231 / shorts −29,859; both TFF sides reconcile to OI. [Resolved review](docket/2026-09-11_CFTC_REVIEW.md). |
| FXY | **58.48** [Sep-18 16:00 ET CLOSE] | ✅ Official close; the SAM-28 magnitude datum. **+2.976%** vs the Jun-22 registration 56.79 ⇒ **1.4 cents below the 58.4937 bar** — recorded but **NOT load-bearing** (the row is route-attributed; 470 of 1,953 ordered pairs in the window clear +3%, so magnitude discriminates nothing). Sat 15:15Z vendor read is the same stale close. YCS/EWJ/DXJ not refreshed (Sep-14: 51.64 / 97.58 / 177.19). |
| Cross-pair, **Sep-18 live** | EURJPY **179.94** / GBPJPY **209.87** / AUDJPY **111.63** [17:44:3x UTC] | Was 180.36 / 210.21 / 111.83 [15:01Z] — yen firmer on **all three** crosses into the afternoon, matching the USD/JPY retrace; the move is yen-side, not USD-side. Still net-weaker than pre-decision. Consistent with a domestic (BOJ) driver rather than a haven rotation. Bears on SAM-31; **not a grade.** |
| ⚠️ **Carried Sep-14/15 vintages** | ADRs · DXY · VIX · S&P · FXY ATM IV · MOF Aug lifer/trust → **`STATUS_REFERENCE.md` § CARRIED SEP-14/15 VINTAGES** | **Pre-date BOTH hikes; not current.** Later tape at its own basis in WALTER SIG-004. |
| US–JP differential, **Sep-17** | **5Y 2.458pp / 10Y 1.947pp** (US 4.78 / 4.94%) | Narrowed ~4bp/3.5bp from Sep-14 but still above both SAM-41 bars; runs **0/5**. **Pre-dates both hikes** — the two 25bp moves broadly offset, so no compression is claimed from this print. Historical SAM-41 confirmation unchanged. |
| JGB auctions | **20Y Sep-15 BTC 4.005× / tail 1.3bp; cutoff 3.869%: AMBIGUOUS** | Neither frozen branch fires; tail misses FIRM by 0.3bp. Generic script “Orderly” is not the grade. Counter 0/2; Sep-29 40Y descriptive only. Sep-3 30Y SOFT remains PRECISION-LIMITED. |
| MOF weekly foreign LT debt | **+¥1,082.9B BUYING**, Sep-6–12 | 🔧 **4-week LT −¥1.608T** (prior window −¥1.55T) — still 🟡 above the ¥1.4T upper, **but carried entirely by the 8/16–22 week (−¥1.978T), which rolls out next week.** Weekly is BUYING and improving three straight (−0.824 → +0.112 → +1.083T), nowhere near the ≥¥1.5T weekly SELLING bar. **Flag and trend now point opposite ways.** Not UST-specific. |
| U.S. / Japan funding | SOFR/IORB · HY/IG · Japan O/N + repo → **`STATUS_REFERENCE.md` § FUNDING** | Sep-11/14 vintages; none measures offshore FX swaps. **LIVE STATE: no funding stress — SOFR−IORB −3bp.** |
| Japan macro / flow reference | Q2 GDP · July wages · July CA · IIP · FY2027 requests · Aug equity flows → **`STATUS_REFERENCE.md` § DURABLE REFERENCE ROWS** | Durable, citable, not boot-read. **LIVE STATE: the VECTOR-5 denominator holds — the oil shock is 4.0% of ONE month's CA surplus.** |
| BOJ **Sep-16** JGB purchase ops | **3–5Y ¥320B / 5–10Y ¥335B / 25Y+ ¥75B**; 25Y+ BTC **1.84×** | ✅ Verified at the record (`ope20260916.xlsx`): 25Y+ offered **750** = exactly the Aug-31 scheduled size ⇒ **SAM-33 falsifier un-fired.** Cover 2.51× [Sep-9] → 1.84× is a *purchase-op* ratio, **not an auction BTC**; no demand grade. Next: Oct–Dec schedule, Sep-30 17:00 JST. |
| **FOMC Sep-16 — RESOLVED** | **Hiked 25bp → 3.75–4.00%, 12–0.** SEP medians **2026 3.8→4.1 / 2027 3.6→4.1%** | Dots moved UP. SAM's registered Fed-side tripwire is an actual **dot walk-back** — this is its opposite by 50bp on the 2027 median; that SAM-28 route **ANTI-FIRED**. Pre-decision pricing is moot and not restated. |

**Durable reference rows → `STATUS_REFERENCE.md` § DURABLE REFERENCE ROWS** (warm, on-demand; current and citable). Holds the Aug-2026 CGPI figures, the 2025-base Japan CPI canon, the insurer hedge ratio, Tankan, and the July trade-balance/crude-volume detail. ⛔ The supersede warnings travel with them — never cite the 2020-base CPI pair or the old July 7.2% / June 7.1% PPI pair.

## CARRY UNWIND PROBABILITY

**Last assessed August 7: 7d ~3 / 30d ~8 / 60d ~13 — a HISTORICAL decomposed estimate, not a fresh rolling forecast.** Amplifier and residual OFF at that assessment; no re-pencil since. **No retired entry gate re-arms.** Method, vintage caveats and re-pencil rules → `STATUS_REFERENCE.md` § CARRY UNWIND PROBABILITY; method canon → `thesis/THESIS.md`.

## INTERVENTION STATUS — MOF posture

**LIVE STATE: Sep-7/8 attribution remains OPEN.** Sep-10/11/14 finals all reconcile to provisional or forecast within ±¥90B; no operation size inferred from residuals, and Japan settlement data cannot exclude a US-only leg. Official-reserve funding/account split unresolved. **No new signature in the 9/15→9/18 window.** 160 gate VOID, not re-armed (USD/JPY 157.34).

**Full evidence, the confirmation ladder, the Aug-3 detector ambiguity, official windows and the pending FRBNY (~Nov-13) / MOF quarterly (~Nov-9) primaries → `STATUS_REFERENCE.md` § INTERVENTION STATUS.** `MOF_INTERVENTION_PLAYBOOK.md` S1/S1-A governs.

## KEY THRESHOLDS

> 🆕 **BASIS (WQ-162 convention) → `STATUS_REFERENCE.md` § USD/JPY MEASUREMENT BASIS.** LIVE STATE, one line: every USD/JPY level and USD/JPY-derived COUNT on this desk reads yfinance `USDJPY=X`, hourly bars aggregated to **Europe/London**-labelled **COMPLETED sessions only** (current bar never scored), **as LAST REVISED** in a 30-day window. ⛔ **NOT** the BOJ 17:00 JST reference rate and **NOT** the MOF curve — never blend or difference across bases. Rotated out of STATUS 2026-09-18 under the read-cap rule; **current and citable, not archived.**

| Level | Significance | Status |
|---|---|---|
| USDJPY 160 | Historical MOF zone; disorder, not level | Below at live **156.69**; latest completed **Sep-17 155.942**. Retired gate remains VOID; no ≥160 count registered. |
| USDJPY 155 | Yen-strength watch; investigate mechanism | 🔧 **DIRECTION CORRECTED — now ABOVE, not below.** Live **156.69**; latest completed **Sep-17 155.942**, the third straight completed close above 155 (Sep-15 155.092 · Sep-16 156.227 · Sep-17 155.942). The stale cell read "Below at live 154.82 / completed Sep-14 154.31" — a Sep-14 vintage left un-remarked when the table above it moved to Sep-18. **A yen-STRENGTH watch cannot fire on yen weakness**; the level is crossed the wrong way and no mechanism grade is drawn. |
| USDJPY 158 | VECTOR-5 re-open leg (c) | Not crossed: latest completed **Sep-17 155.942** (2.06 yen below); intraday high today 157.34 also short of it. Joint Brent condition not re-evaluated — and Brent is FALLING on a matched contract (Dec `BZZ26` 98.68 close, −4.48% over three sessions — **not** the −7.5% continuous figure, retired as a roll artifact), so leg (c) and the oil leg point apart. **No re-open.** |
| USDJPY 147 / 145 | Carry / insurer investigation levels; no forced-flow inference | Above both. |
| JGB 10Y 2.40% | Stress crossover | Above at **2.993%**, MOF **Sep-17** (was 2.988% Sep-14). Pre-dates the 9/18 hike. |
| JGB 30Y 4.0% | Contested demand-floor zone | Above: 30Y **4.047%** / 40Y **4.036%**, MOF **Sep-17** (was both 4.040% Sep-14) — 30Y and 40Y have **inverted** at the long end. 🔧 SAM-33 op-record review now verified **through Sep-16** at `ope20260916.xlsx`; next check **Sep-30 17:00 JST** (Oct–Dec schedule). |
| JGB 30Y 4.5% | Contested impairment tail | **45bp away** on MOF Sep-17 (4.047%); no forced-sale inference. |
| Brent $90 / $120 | Oil context / shock watch | **Dec `BZZ26` $98.68** / Nov `BZX26` $103.10, Sep-18 closes. 🔧 **The “−7.5% in three sessions” figure is RETIRED as a roll artifact** (CATO R1): matched-contract moves are **Dec −4.48% / Nov −5.20%**. Distance to the $90 marker is **contract-dependent** — $8.68 on Dec, $13.10 on Nov — so the marker is not quotable without naming the month. ⛔ **This row previously carried “never compared across rolls” beside a figure that did exactly that**; the rule was correct and the cell violated it. |
| Oil-in-yen ¥18,000/bbl | VECTOR-5 re-open leg (b) | Not re-evaluated this boot: synchronized contract-specific five-completed-session observations required. Prior Sep-11 assessment FALSE; no fresh count. |
| CFTC −108K / −140K / −153K | Retired frame's leg-1 invalidation + historical DE-LOAD / reclaim lines | −108K **fired Aug-7**; the others are **moot in direction** — Sep-8 printed **+10,796, NET LONG**, and retired short-side lines cannot fire on a long book. No rearm. OI **499,635, +87,753** [Sep-8]; aggregate growth cannot exclude forced short covering within a cohort. New print today 15:30 ET. |

## WHAT TO WATCH (forward only — full docket → `docket/CALENDAR.md`)

Retired entry triggers remain void; this is a research docket.

| When | Event | Why it matters |
|---|---|---|
| ✅ **Sep-18 RESOLVED** | **BOJ MPM — hiked to 1.25%, 7–2** · National CPI Aug **1.9 / 1.7 / 1.9** (2025 base) | Owner grade → § 2026-09-18 above. The registered hawkish surprise **did NOT fire — both dissents were for HOLD.** |
| ✅ **Sep-18 close — RESOLVED, then RULED** | **SAM-28 QUALIFIED / NO-VERDICT · SAM-31 FALSE** | Graded FALSE/FALSE 9/19 AM on frozen terms; **SAM-28 regraded 9/19 PM** on the CATO R4 challenge — 4 of 5 routes settled NO-FIRE on fact, the 5th **fired as operations** with its magnitude-attribution window left unfixed at registration. SAM-31's verdict survives on leg 1 + the episode screen, not the mean. ⛔ The close (FXY 58.48) is **context, not the instrument**. → [ruling](docket/2026-09-19_CATO-R4-RULING.md) · [grade record](docket/2026-09-19_SAM28_SAM31_GRADE.md) |
| ⚠️ **owed, undated** | 🆕 **RED salvage ④ — a REAL JPY xccy-basis instrument** | **The v2.0 kill salvaged four things; ④ is the sizing/basis instruments, and RED called the JPY cross-currency basis *"the single highest-value output of the review… the nearest thing to a DISCRIMINATING observation that exists"* — a ~$400B swap-funded book is invisible to CFTC but **not to its funding market**. ⛔ **On 2026-09-11 I let the fixed CME proxy lapse (correctly — it sign-flips on the 9/18 hike) and wrote that "no threshold, gate, prediction or trade trigger depends on it." That was true and INCOMPLETE: this salvage obligation did, and it was tracked nowhere.** The defective proxy still should not be activated; what is owed is a genuine instrument (policy rate as an INPUT, a reader that rejects rounded/desynced legs, two same-session official pairs). Registered here so it stops being invisible. |
| Sep-29 | 40Y auction | September 11 ruling: descriptive BTC only, no FIRM/SOFT grade; uniform-price has no tail. Counter remains 0-of-2. |
| Sep-30 17:00 JST | BOJ Oct–Dec JGB purchase schedule | Per `mpr260831a.pdf`. A scheduled taper-plan adjustment does **NOT** count against SAM-33; an unscheduled capping op would. |

## POSITION — FLAT

No FXY position was opened during the retired convexity-tail episode; $0 was at risk in that frame. Earlier trading history is separate and preserved; the last Will-confirmed flat state was June 29. No frame-specific close/P&L is created. TRY-FIRE-007 stands down. Retired entry gates are void; any re-entry requires a fresh independently argued thesis and Will's approval. Historical decision records remain in `TRADE.md` and CHANGELOG.

## CHANNELS · BOJ · FED

**BOJ policy rate 1.25% — RAISED 25bp at the September 17–18 MPM, effective September 24 2026** (primary `k260918a.pdf`, parsed in-session). Complementary deposit facility 1.25%; basic loan rate 1.50%. Highest since 1995. The root-CLAUDE.md 0.75% Takaichi mortgage-ceiling threshold is now breached by 50bp. Channel 1 remains RETIRED and requires direct foreign SALES at ≥2 institutions across ≥2 consecutive windows; yields and ESR are co-conditions, never substitutes. Carry-convexity/positioning frames remain retired. **Mechanism canon → `thesis/THESIS.md`; September MPM source detail and the officials' record → `STATUS_REFERENCE.md` § CHANNELS · BOJ · FED.**

## COMPRESSED SESSION-NOTE POINTERS

↪️ **ROTATED OUT 2026-09-18 → `STATUS_ARCHIVE.md` § COMPRESSED SESSION-NOTE POINTERS** (already held this block verbatim, both redirect stubs included). Moved sections live at `thesis/INTERVENTION_CHARACTER_2026-08-03_PREREGISTRATION.md` and `thesis/BOJ_2026-07-31_PREREGISTRATION.md`. Narratives → `thesis/timeline/TIMELINE.md`.

✅ **Its external-consumer warning was re-checked before removal and is SPENT** — WALTER's `SIGNAL_PROCESSING_CHECKLIST.md` §v0.30 now cites the thesis file directly and no longer references `AGENTS/SAM/STATUS.md` (verified 2026-09-18). Rationale → `MAINTENANCE.md`.

## PREDICTIONS

✅ **CATO R4 CHALLENGE RULED 2026-09-19 PM — the grades are no longer disputed.** CATO upheld on **4 of its 5** points (PROME's packet relayed 3; points 3 and 5 were not carried, and point 3 is one that moves SAM-28). ⛔ **Nothing graded TRUE; CATO never asked for that.** → [ruling](docket/2026-09-19_CATO-R4-RULING.md).

**16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 1 OPEN (SAM-33)** — re-derived FROM `thesis/PREDICTIONS.tsv` (34 rows, 0 unclassified), never carried by hand. `boot.py --predictions` derives OPEN rows and checks the sidecar; it never grades.

- **SAM-28:** ≥1 eligible tail route produces ≥+3% FXY by Sep-18, 40%, 🟠 **RESOLVED — QUALIFIED / NO-VERDICT** (regraded 2026-09-19 PM; was FALSE). Four of five routes settled NO-FIRE **on fact**. The fifth (sustained MOF #3) **fired as operations** — 7/30 and 7/31 official action — and the **attribution window for the move it produced is a convention the registration never fixed**: the op days themselves reached only +2.58% / +2.73%, while the episode peaked +4.22% on 8/3 and gave the whole move back by 8/10. 🔑 The contemporaneous record favours the reading I had rejected (`THESIS` § N tail-routes names the route *"MOF #3 sustained"* while *"sustained-unwind|fires ~0.20"* is a **separate** conditional) — **and I consulted it only after being challenged, though the governing packet ordered it.** Not TRUE either: registered magnitude given firing was **+2% blended**, below the bar. ⛔ Withdrawn: the Episode-B "no-route control" (my own STATUS says Sep-7/8 attribution is **OPEN** — unknown treatment is not known absence) and the "correctly calibrated" label.
- **SAM-31:** yen-haven re-couples by Sep-18, 35%, 🔴 **RESOLVED FALSE** — verdict **unchanged**, reasoning **replaced** (2026-09-19 PM). CATO is right that a negative **mean** cannot refute an existential **episode** claim, so the episode screen was run instead: on the three genuine VIX-rise episodes the yen did **not** bid broadly — 7/29 (VIX **20.66**, window max) FXY +0.232%, yen stronger on **1 of 4** crosses; 6/23 (19.49) +0.018%, 2/4; 7/17 (18.77) +0.106%, 2/4. The **one** broad-based yen bid, 9/8 (+1.517%, **4/4** crosses), came at **VIX 15.72** — not the *"genuine VIX-spike regime"* the row's **own note** requires, no bar invented — and sits inside the **OPEN**-attribution window, so it may be official action rather than a haven bid. **The relationship is inverted**: biggest VIX rises → no yen bid; only broad yen bid → no VIX spike. ⚠️ Conceded open: the packet asked for **matched intraday** cross-pair evidence (esp. Jul-13); daily cross-clock data cannot supply it and Jul-13 is that artifact. Not graded off it; leg 1 disposes of the row.
- **SAM-33:** no BOJ emergency long-end capping through Dec-31, 72%, OPEN. Activation MET / VOID clause lifted 8/17 ⇒ a genuine test, not a free TRUE. ✅ **Sep-16 ops audited AT THE RECORD (`ope20260916.xlsx` vs `mpr260831a.pdf`): 25Y+ offered 750 = exactly scheduled, no fixed-rate, unscheduled or enlarged op ⇒ falsifier un-fired through Sep-16.** The 9/18 hike does not bear on it (a policy-rate move is not a long-end capping op). A DISORDER response does not falsify; a scheduled taper-plan change is excluded by the row's own terms. **Next check: Sep-30 17:00 JST Oct–Dec schedule.**
- **SAM-39:** RESOLVED CONFIRMED Sep-4, **TRUE-IN-LETTER / FALSE-IN-SPIRIT** — range cleared the bar without proving the named official-action mechanism. **A successor owes a preregistered SHAPE leg.** Registered instrument = `usdjpy.py` hourly-derived intraday **RANGE**, **≥2.5-yen bar** — ⛔ **not a ≥160 level count; no such count exists on this desk.** Basis blockquote: § KEY THRESHOLDS (canonical home).

Calibration residue: **naming a risk and underweighting it is distinct from missing it.** As-made audit dispositioned 9/10 (one scoring vintage moved, SAM-07 75%→48%; scoreboard unchanged) → `audits/2026-09-10_asmade-disposition.md`. Full post-mortems → `thesis/PREDICTIONS_ARCHIVE.md`.

---

Thesis v1.7 → `thesis/THESIS.md`; audit → `thesis/CHANGELOG.md`; cross-agent synthesis → `NEXUS_BRIEF.md`. No successor declared.
