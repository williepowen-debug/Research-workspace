# SAM STATUS

**Last written: 2026-09-24 ~17:2x ET — 2nd pass (core-file sync: THESIS, V18 candidate, JGB supply/demand, insurer tracker, KB-SAM-257); 1st pass committed 16:57 ET `976c760c1` (its "~17:3x" stamp was written ahead of the clock). Will-directed catch-up after Silver Week (prior block 2026-09-20).** 🔴 **Three facts moved: (1) USD/JPY went THROUGH the 9/18 rate-check level on 9/23 (close 158.266) and is ~158.9 live (H 159.036) — ~30h+ above it with NO intervention; the T1 "hours to ~1 day" window LAPSED; Katayama 9/24 "principles since the previous joint intervention remain alive" = standing readiness, not T2/T3. (2) JGB 10Y touched 3.075% on the 9/24 reopen, highest since 1996 (Bloomberg/CNBC, quote basis), OSE futures circuit breaker (REPORTED) — and the BOJ did not cap (ops record checked: SAM-33 un-fired through 9/24). (3) CFTC Sep-15: speculators +120,359 net LONG yen after the largest 2-week swing in 1,360 reports — and the yen then fell ~3 yen against them.** BOJ OIS restored (9/24 chart; Dec 68%, cum 2.18 to Apr-27 — MORE hawkish while the yen weakened). VECTOR-5 leg (c) met in letter; test still NONE. ⛔ **Nothing re-arms: book FLAT, v1.7 stands, 160 gate VOID.** Boot 13/14 (boj_ois needed the visual review, done).

**Signal Status:** ⚰️ **CARRY-CONVEXITY TAIL — RETIRED TO LOW (THESIS v1.7, 2026-08-07). Leg-1 SPF FIRED. Position FLAT; $0 was at risk.** · **v2.0 KILLED 8/20–27** (BIS K1 fired; RED killed it four more ways — `thesis/V20_CROSSREAD_2026-08-27.md`; nothing was owed to Will). · 🕯️ **v1.8 is a CANDIDATE in a SEPARATE document** (`thesis/V18_CANDIDATE_PILLAR1.md`), gated on SAM-41 + a separately-registered FX co-condition + RED pass + Will sign-off — **never on BIS.** SAM-41 historically confirmed but current gaps sit back above both bars (**0/5**); use its dated rider, not the archived Aug-7 case. ⛔ **NO SUCCESSOR FRAME DECLARED — v1.7 stands, and that is the honest state, not a gap to be filled.**

🔴 **The 8/7 print broke the frame.** CFTC Aug-4 **−45,473 = 24.2% of the corrected peak R = −188,077** — through the **−108K/60% leg-1 invalidation line**; character **REVERSAL, not liquidation**; book FLAT, $0 at risk. ⛔ The **"25.3% of −180K" form is RETIRED** (Will-ratified 8/11). 📌 Calibration residue: **45% assigned to CONFIRM, ~25% to what happened.** **Forensics and full lesson → `STATUS_ARCHIVE.md` § 2026-08-07 FRAME-BREAK FORENSICS.**

**Predictions:** **16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 1 OPEN (SAM-33)** — re-derived FROM `thesis/PREDICTIONS.tsv` (34 rows, 0 unclassified), not carried forward. 🔧 **SAM-28 `QUALIFIED / NO-VERDICT` · SAM-31 FALSE** — this read "SAM-28/31 both FAILED Sep-18" while the SAME sentence counted "1 qualified", and `PREDICTIONS.tsv` has carried the regrade since 9/19. **The CATO R4 cascade reached four STATUS sites, both trade docs and the brief, and missed the derived-count line** (METSUKE Run-22 E2). Canonical: `thesis/PREDICTIONS.tsv`.


*Detail → `thesis/THESIS.md` v1.7 · `CHANGELOG.md` 2026-08-07 · `outbox/2026-08-07_to-TERRY-PROME_RESOLVER-COMPLETE-section8-DE-LOAD-leg1-fired-frame-LOW.md` · pre-print re-pencil `thesis/REPENCIL_2026-08-07_PREPRINT.md` (committed BEFORE the print).*


---

## LIVE MARKET DATA

*Refreshed 2026-09-24 ~20:40Z (catch-up after Silver Week). Each row keeps its own clock. FX = own hourly bars, Europe/London sessions (WQ-162); **9/24 is a LIVE bar, never scored.** JGB = MOF curve **Sep-18** (published 9/24 ~08:58 JST after the holiday blackout; Sep-24 publishes Fri).*

| Instrument | Level / vintage | Note |
|---|---|---|
| USD/JPY | Completed closes **9/21 157.311 · 9/22 157.470 · 9/23 158.266** (H 158.401) · 9/24 **LIVE ~158.89, H 159.036** [20:40Z] | **First completed close above the 9/18 rate-check high (158.054) = 9/23**; first hourly print above it 9/23 ~13:00Z (WALTER -019, re-verified here). 7 straight completed closes above 155. Weekly 9/18 close 156.855 → ~158.9 = **+1.3%, orderly** (largest session range 9/23 0.98y). 9/19 row in the TSV is a vendor phantom (O=H=L=C), not a session. |
| ✅ **BOJ meeting OIS — 2026-09-24 15:15 JST** | **Oct-30 27% / OIS 1.2950% · Dec 68% · Jan-27 40% · Mar-27 45% · Apr-27 39%; cumulative 2.18 hikes to Apr-2027** | SAM visual transcription, chart SHA `1f79f491…`, validated `--no-write`, ledger written. **vs Sep-18: Oct 22→27, Dec 63→68, cum 1.94→2.18 = the path repriced HAWKISH while the yen weakened.** ⛔ Incremental 25bp equivalents are NOT next-hike-timing probabilities; cumulative counts are NOT probabilities. JST assumed. 🔴 **Source-age expiry Mon Sep-28 15:15 JST = 02:15 ET** (`MAX_AGE=4d`); Oct-30 is the separate decision expiry. |
| Brent (matched contracts) | **Nov `BZX26` $107.31 · Dec `BZZ26` $100.77** [9/24 close] | Nov 9/18→9/24 **+3.3%**; Dec **+1.5%**; low 9/22 (99.25 / 95.41). ✅ `oil_roll_check`: no roll 9/17→9/24 (BZ=F = BZX26). ⚠️ Vendor **revised 9/18** to 103.87 / 99.29 (STATUS had 103.10 / 98.68). Nov−Dec **$6.54** backwardation; Nov expires ~Sep-30. Cause of the 9/23–24 rise **unsourced** (WALTER -015). Benchmark-mismatch caveat stands (~37% of receipts WTI-Midland-led). |
| JGB MOF **Sep-18** · 🔴 **9/24 quote basis** | MOF: **10Y 2.981 / 20Y 3.812 / 30Y 4.044 / 40Y 4.033%** · 9/24 reopen: **10Y touched 3.075% (highest since Aug-1996), close ~3.070**; 20Y ~3.91; 30Y ~4.13–4.16; 40Y ~4.20 | ⛔ **Different bases — never difference quote vs MOF.** 9/24: 10Y/5Y/20Y ~+10bp (Bloomberg/CNBC headlines, verified by SAM); **OSE dynamic circuit breaker on JGB futures** (Nikkei, REPORTED); driver = global rout (UST 10Y 5.18 / 30Y 5.47% par 9/24, highest since 2004 on 30Y). **No super-long record** (30Y 4.21% / 40Y 4.40% highs, quote basis). BOJ ops 9/24: securities-lending only — **no capping op.** MOF 9/24 curve publishes Fri. Sep-18 (hike day): 10Y −1.2bp, 30Y −0.3bp vs Sep-17 — long end **did not sell off on the hike.** 30Y/40Y still inverted. Level alone identifies neither sales nor capping. |
| **CFTC legacy JPY, Sep-15** | **Net +120,359 LONG** (L 237,951 / S 117,592); **OI 542,802** | Δ net **+109,563** (L +59,160 / S −50,403). 🔴 **2-week swing Sep-1→15 = +212,586, the LARGEST of 1,360 weekly reports since 2000-08-29** (own parse of CFTC annual files, 2000–2026); OI **= series record**. ⛔ **NOT a record LEVEL** — record long +179,212 [2025-04-29]. The three largest 1-week net-long swings in the series are all 2026 (8/4, 9/15, 9/8). Motive and forced flow not identified. Next print Fri 9/25 (Sep-22 positions). |
| CFTC TFF, Sep-15 | Leveraged **+23,170** / asset-manager **+53,845** / dealer **−168,570** | Lev funds flipped from −49,098 [9/8]; AM from −570. **Both spec cohorts net LONG yen at ~155 — and USD/JPY has since risen ~3.8 yen AGAINST them** [9/15 close 155.092 → 9/23 158.266]. Whether they held is the 9/25 print's question. |
| FXY | **57.68** [9/24 close] | Was 58.48 [9/18]. Vendor has no 9/22 bar (US was open — vendor gap). |
| Cross-pairs, **9/24 live** | EURJPY **180.75** / GBPJPY **210.02** / AUDJPY **111.38** | vs 9/18 closes 179.20 / 208.54 / 111.09: yen weaker vs EUR & GBP, ~flat vs AUD. Mixed ⇒ not a clean yen-specific move; DXY 100.22 → 101.31 carries part of USD/JPY. |
| US–JP differential, **Sep-18** | **5Y 2.555pp / 10Y 2.029pp** (US 4.86 / 5.01%) | **WIDENED ~10bp / 8bp on hike day vs Sep-17** — the BOJ hike did not compress the gap. US 10Y then **5.18% [par 9/24]** vs JGB 10Y ~3.07 (quote basis) ⇒ ~211bp **indicative only, mixed bases**; no MOF same-date gap after 9/18. SAM-41 runs 0/5. |
| JGB auctions | Last: **20Y Sep-15 AMBIGUOUS** (BTC 4.005× / tail 1.3bp) | None Sep-16→24. Next: Fri 9/25 T-bill + liquidity-enhancement (**no super-long bearing**); **Sep-29 40Y (descriptive only)** → **Oct-8 30Y** (frozen bars apply). |
| MOF weekly foreign LT debt | **+¥1,082.9B BUYING**, Sep-6–12 | ⚠️ **Wk Sep-13–19 NOT published Thu 9/24** (CSV Last-Modified 9/16 22:50Z at 9/24 20:45Z) — shift to Fri is UNVERIFIED. 4-week −¥1.608T flag is carried entirely by the 8/16–22 week, which rolls out at the next print. Not UST-specific. |
| U.S. / Japan funding | SOFR 3.87 / IORB 3.90 ⇒ **−3bp**; HY 273 / IG 77bp [FRED 9/23] → **`STATUS_REFERENCE.md` § FUNDING** | **LIVE STATE: no U.S. funding stress across the FOMC hike.** Japan O/N last recorded pre-hike. None measures offshore FX swaps. |
| Carried context (ADRs, DXY, VIX, S&P, UST, FXY IV) | → **`STATUS_REFERENCE.md` § CARRIED MARKET CONTEXT** (refreshed 9/24) | UST 10Y/30Y **5.18 / 5.47%** [Treasury par 9/24; 5.11/5.40 on 9/23]; FXY ATM IV (proxy) 16.2% → **11.0%** — event premium gone. |
| Japan macro / flow reference | → **`STATUS_REFERENCE.md` § DURABLE REFERENCE ROWS** | **LIVE STATE: the VECTOR-5 denominator holds — the oil shock is ~4% of ONE month's CA surplus.** |
| BOJ **Sep-16** JGB purchase ops | 25Y+ offered **750** = scheduled; BTC 1.84× | ✅ SAM-33 falsifier un-fired through Sep-16. No ops held Sep-21–23 (holidays). Next: Oct–Dec schedule **Sep-30 17:00 JST**. |
| FOMC Sep-16 — SETTLED | Hiked 25bp → 3.75–4.00%, 12–0; SEP medians UP | SAM-28's Fed route anti-fired. |

**Durable reference rows → `STATUS_REFERENCE.md` § DURABLE REFERENCE ROWS** (warm, on-demand; current and citable). Holds the Aug-2026 CGPI figures, the 2025-base Japan CPI canon, the insurer hedge ratio, Tankan, and the July trade-balance/crude-volume detail. ⛔ The supersede warnings travel with them — never cite the 2020-base CPI pair or the old July 7.2% / June 7.1% PPI pair.

## CARRY UNWIND PROBABILITY

**Last assessed August 7: 7d ~3 / 30d ~8 / 60d ~13 — a HISTORICAL decomposed estimate, not a fresh rolling forecast.** Amplifier and residual OFF at that assessment; no re-pencil since. **No retired entry gate re-arms.** Method, vintage caveats and re-pencil rules → `STATUS_REFERENCE.md` § CARRY UNWIND PROBABILITY; method canon → `thesis/THESIS.md`.

## INTERVENTION STATUS — MOF posture

🟠 **LIVE STATE (9/24): T1 rate check fired 9/18 at ~158 → its "hours to ~1 day" strike window LAPSED → USD/JPY then went through ~158 (9/23) and sits ~158.9 with no strike. Ladder step UNCHANGED.** ⛔ **NO intervention confirmed.**

| Field | Reading |
|---|---|
| Last tell | **T1 rate check ~midnight JST Sep-19** (REPORTED, press only, no official confirmation). None since. |
| Level vs tell | First above 158.054 on **9/23 ~13:00Z**; 9/23 close **158.266**; 9/24 live H **159.036**. **~30h+ through the tell level.** |
| Speed | Orderly: largest session range Sep-21→23 **0.98 yen**; +1.3% over four sessions. **CH-011 says speed/disorder triggers, not level — this is not a trigger-shaped move.** |
| Official words | Katayama 9/24 ~11:07 JST (Reuters): *"the principles since the previous joint intervention remain alive"*, no level ⇒ **T0-plus** (standing joint-action readiness), not T2 "excessive/one-sided", not T3 "decisive/ready to act". No Mimura/Kihara/Bessent yen remark found. |
| Read | Two readings not yet separable: **(1)** the 9/18 check was a SPEED warning at a speed moment (CH-011 model, no change needed) or **(2)** MOF standing aside at these levels (new). **Discriminator = the next FAST leg, on the registered disorder watch (≥1.5–2%/day or ~2–3 yen over 1–2 sessions).** Under S1-A, silence still does not lower P(strike). Detail → playbook 2026-09-24. |
| Adjacent | CFTC Sep-15 spec book was **net LONG yen** at ~155 → a squeeze adds yen-selling speed (inference). UBS AM (Zhao) says it would sell yen into any intervention — one manager's stated view, wording unverified, not positioning. |

**Sep-7/8 attribution OPEN** (bears on SAM-31's qualification). Next hard evidence: **MOF monthly ~Sep-30** (Aug-27→Sep-28 window) · FRBNY Q3 **~Nov-13** · MOF quarterly **~Nov-9**. Full evidence + ladder → `STATUS_REFERENCE.md` § INTERVENTION STATUS and `MOF_INTERVENTION_PLAYBOOK.md` (S1/S1-A govern).

## KEY THRESHOLDS

> 🆕 **BASIS (WQ-162 convention) → `STATUS_REFERENCE.md` § USD/JPY MEASUREMENT BASIS.** LIVE STATE, one line: every USD/JPY level and USD/JPY-derived COUNT on this desk reads yfinance `USDJPY=X`, hourly bars aggregated to **Europe/London**-labelled **COMPLETED sessions only** (current bar never scored), **as LAST REVISED** in a 30-day window. ⛔ **NOT** the BOJ 17:00 JST reference rate and **NOT** the MOF curve — never blend or difference across bases. Rotated out of STATUS 2026-09-18 under the read-cap rule; **current and citable, not archived.**

| Level | Significance | Status |
|---|---|---|
| USDJPY 160 | Historical MOF zone; disorder, not level | Below: 9/23 close **158.266**; 9/24 live H **159.036** — **~1 yen away.** The 9/18 rate check fired at ~158, so 160 is not the reaction zone; the retired gate stays VOID. No ≥160 count registered. |
| USDJPY 155 | Yen-strength watch; investigate mechanism | **ABOVE, wrong way** — 7 straight completed closes above 155 (9/15→9/23). A yen-STRENGTH watch cannot fire on yen weakness. |
| USDJPY 158 | VECTOR-5 re-open leg (c) | 🟠 **LETTER MET 9/23: completed close 158.266 > 158 "while Brent holds"** (Nov 103.87 [9/18] → 103.08 [9/23]). ⚠️ **Spirit confounded:** the leg names the terms-of-trade channel "rather than the rate differential" — and the differential **widened** over the same window (10Y gap +8bp on 9/18; UST 10Y 5.01 → 5.11%). One close. **The re-open test needs ALL THREE legs: (a) MET [Aug crude volume +3.6% YoY], (c) MET-in-letter, (b) NOT MET ⇒ answer stays NONE.** Packet → PROME (VECTOR-5 owner, DOCKET L328). |
| USDJPY 147 / 145 | Carry / insurer investigation levels | Above both. |
| JGB 10Y 2.40% | Stress crossover | Above at **2.981%**, MOF **Sep-18**. |
| JGB 30Y 4.0% | Contested demand-floor zone | Above: 30Y **4.044%** / 40Y **4.033%**, MOF Sep-18, still inverted. SAM-33 op-record verified **through Sep-16**; next check **Sep-30 17:00 JST**. |
| JGB 30Y 4.5% | Contested impairment tail | **46bp away** on MOF Sep-18; no forced-sale inference. |
| Brent $90 / $120 | Oil context / shock watch | **Nov $107.31 / Dec $100.77** [9/24]. $90 marker is contract-dependent ($17.31 / $10.77 away); $120 is $12.69 above Nov. Never compare across rolls (`oil_roll_check.py`, boot-wired). |
| Oil-in-yen ¥18,000/bbl | VECTOR-5 re-open leg (b) | **NOT MET.** Nov × completed USD/JPY close ≈ **¥15,6xx–16,3xx** 9/18→9/23 (9/23: 103.08 × 158.266 ≈ ¥16,314). ⚠️ Close-on-close approximation, not the synchronized matched-timestamp test; the gap (~¥1,700 ≈ Brent ~$114 at 158) is far outside that error. Needs 5 consecutive sessions. |
| CFTC −108K / −140K / −153K | Retired frame's short-side lines | Moot in direction — **Sep-15 net +120,359 LONG**; retired short-side lines cannot fire on a long book. **No rearm.** ⚠️ The mirror question (a long-yen crowd squeezed by yen weakness) has **NO registered line** and none is invented here. |

## WHAT TO WATCH (forward only — full docket → `docket/CALENDAR.md`)

Retired entry triggers remain void; this is a research docket.

| When | Event | Why it matters |
|---|---|---|
| 🔴 **Tonight → Fri** (Tokyo 9/25 session opens ~19:00–20:00 ET) | **USD/JPY ~158.9, ~1 yen under 160, ~30h+ above the rate-check level** | The live watch is **SPEED, not level** (CH-011): a fast leg through 159–160 in thin hours, a fresh rate-check report, or T2/T3 language ("excessive/one-sided", "decisive action"). Semi-confirm any spike via **BOJ current-account projections vs broker forecasts ~2 business days later**. § INTERVENTION. |
| Fri Sep-25 | **CFTC 15:30 ET (Sep-22 positions)** · MOF weekly (shift UNVERIFIED) · T-bill + liquidity-enhancement auctions · BOJ BIS banking stats Q2 | CFTC: did the +120K long-yen book hold through a ~3-yen move against it? MOF: 8/16–22 week rolls out of the 4-week flag. Auctions: no super-long bearing. BIS: not the global GLI, no v2.0 rearm. |
| Mon Sep-28 | BOJ July MPM minutes · **BOJ OIS quote expires 15:15 JST (02:15 ET)** | Re-transcribe the chart — SAM's job. |
| Sep-29 | 40Y auction | Descriptive BTC only (uniform-price ruling); counter 0-of-2. |
| Sep-30 17:00 JST | BOJ Oct–Dec JGB purchase schedule | **Next SAM-33 check.** A scheduled taper-plan adjustment does NOT count; an unscheduled capping op would. |
| Oct-1 / Oct-2 | BOJ Summary of Opinions + Tankan · Tokyo CPI + METI Aug crude-by-source | SoO: is oil named, and how. METI: do Kuwait/Qatar return from ZERO. |
| Oct-8 | 30Y auction | Next test the frozen FIRM/SOFT bars apply to. |
| ⚠️ **owed, undated** | **RED salvage ④ — a real JPY xccy-basis instrument** | Still owed; the fixed CME proxy stays expired and is not revived. A ~$400B swap-funded book is invisible to CFTC but not to its funding market. |

## POSITION — FLAT

No FXY position was opened during the retired convexity-tail episode; $0 was at risk in that frame. Earlier trading history is separate and preserved; the last Will-confirmed flat state was June 29. No frame-specific close/P&L is created. TRY-FIRE-007 stands down. Retired entry gates are void; any re-entry requires a fresh independently argued thesis and Will's approval. Historical decision records remain in `TRADE.md` and CHANGELOG.

## CHANNELS · BOJ · FED

**BOJ policy rate 1.25% — RAISED 25bp at the September 17–18 MPM, effective September 24 2026** (primary `k260918a.pdf`, parsed in-session). Complementary deposit facility 1.25%; basic loan rate 1.50%. Highest since 1995. The **0.75%** Takaichi mortgage-ceiling threshold is now breached by 50bp. 🔧 **Home corrected 2026-09-20: it is `AGENTS/SAM/CLAUDE.md:235`, NOT root `CLAUDE.md`** (root has zero hits) — the misattribution pointed the fix at a Will-gated file instead of SAM's own (METSUKE Run-22 E3). Channel 1 remains RETIRED and requires direct foreign SALES at ≥2 institutions across ≥2 consecutive windows; yields and ESR are co-conditions, never substitutes. Carry-convexity/positioning frames remain retired. **Mechanism canon → `thesis/THESIS.md`; September MPM source detail and the officials' record → `STATUS_REFERENCE.md` § CHANNELS · BOJ · FED.**

## PREDICTIONS

✅ **CATO R4 SETTLED 2026-09-19** — upheld 4 of 5; nothing graded TRUE. → [ruling](docket/2026-09-19_CATO-R4-RULING.md). ⚠️ **SAM-31's FALSE carries a qualification that must travel with any citation** — on a strict single-episode reading it is QUALIFIED, because the one candidate episode (Sep-8/9) has OPEN official attribution, and open attribution prevents confirmation rather than establishing failure.

**16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 1 OPEN (SAM-33)** — re-derived FROM `thesis/PREDICTIONS.tsv` (34 rows, 0 unclassified), never carried by hand. `boot.py --predictions` derives OPEN rows and checks the sidecar; it never grades.

- **SAM-28:** ≥1 eligible tail route ≥+3% FXY by Sep-18, 40%, 🟠 **RESOLVED — QUALIFIED / NO-VERDICT.** Four routes NO-FIRE on fact; the fifth (sustained MOF #3) **fired as operations** (7/30–31) with **an attribution window the registration never fixed** — that alone carries the no-verdict. 🔑 The record favouring this reading was one the governing packet **ordered** me to consult and I consulted only after challenge. Withdrawn: Episode-B control, the "correctly calibrated" label, the "+2% blended" argument. **Full prose → `STATUS_ARCHIVE.md` § SAM-28 / SAM-31.**
- **SAM-31:** yen-haven re-couples by Sep-18, 35%, 🔴 **RESOLVED FALSE — always report it WITH its qualification; a bare "FAILED" drops information that matters.** An **interpretive owner judgement** on the regime reading, on same-clock evidence only (n=24 risk-off, yen stronger on 7 = 29.2%, mean −0.154%; window VIX max 20.66). ⚠️ **Three things are NOT settled and travel with every citation:** ① on a strict **single-episode** reading it is **QUALIFIED** — the only candidate, **9/8–9/9**, has **OPEN** attribution, which *prevents confirmation rather than establishing failure*; ② **a window mean cannot exclude the channel returning LATE**, and 9/8–9/9 are the window's last risk-off sessions; ③ **7/13** stays unresolved (same-clock FXY −0.493% vs 4-of-4 cross strength). **Matched intraday cross-pair data settles ①–③ and is owed, not scheduled — if obtained, THE ROW IS RE-OPENABLE.** Full prose → `STATUS_ARCHIVE.md`; reasoning → [ruling](docket/2026-09-19_CATO-R4-RULING.md) §§ ADDENDUM, ADDENDUM 2.
- **SAM-33:** no BOJ emergency long-end capping through Dec-31, 72%, OPEN (activation MET 8/17 ⇒ a genuine test). ✅ **Ops record audited through Sep-24** (`ope20260917/18/24.xlsx`: securities-lending only). **The 9/24 reopen was the first real stress day of the test — 10Y to a 1996 high, super-long ~+7–10bp, futures circuit breaker — and the BOJ did NOT cap.** ~+7–10bp/session is below the row's ≥~20–40bp disorder bar, so it sits inside the falsifier's scope and the falsifier did not fire. **Next: Sep-30 17:00 JST Oct–Dec schedule** (a scheduled taper change does NOT count).
- **SAM-39:** RESOLVED CONFIRMED Sep-4, **TRUE-IN-LETTER / FALSE-IN-SPIRIT** — range cleared the bar without proving the named official-action mechanism. **A successor owes a preregistered SHAPE leg.** Registered instrument = `usdjpy.py` hourly-derived intraday **RANGE**, **≥2.5-yen bar** — ⛔ **not a ≥160 level count; no such count exists on this desk.** Basis blockquote: § KEY THRESHOLDS (canonical home).

Calibration residue: **naming a risk and underweighting it is distinct from missing it.** As-made audit dispositioned 9/10 (one scoring vintage moved, SAM-07 75%→48%; scoreboard unchanged) → `audits/2026-09-10_asmade-disposition.md`. Full post-mortems → `thesis/PREDICTIONS_ARCHIVE.md`.

---

Thesis v1.7 → `thesis/THESIS.md`; audit → `thesis/CHANGELOG.md`; cross-agent synthesis → `NEXUS_BRIEF.md`. No successor declared.
