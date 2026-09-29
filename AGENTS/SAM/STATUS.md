# SAM STATUS

**Last written: 2026-09-29 08:55 ET (from `date`) — Will-directed news catch-up (prior block 2026-09-24).** 🟠 **Four facts moved: (1) The US and Japan ran a JOINT verbal campaign for a stronger yen — Trump raised yen weakness with Takaichi (disclosed 9/25), Bessent: *"the desirability of a strong yen"* (9/25), Mimura: *"take that message at face value"* (9/28) — and USD/JPY fell from the 159.036 peak [9/24] to 156.498 [9/28 low], completed closes 158.755 → 157.185 → 157.433. NO rate check or intervention found; graded T2-EQUIVALENT, not T3 (playbook 2026-09-29). (2) CFTC Sep-22: the long-yen spec book was cut 40% (+120,359 → +71,982) INTO the 158–159 grind; open interest −164,101, mostly the Sep contract's delivery (June showed the same step). (3) 40Y auction 9/29 BTC 3.096× — firmest of its n=3 series; MOF 10Y 3.082% / 5Y 2.441% (9/28) = new highs on MOF basis; BOJ still did not cap (ops audited through 9/29). (4) BOJ OIS 9/29 repriced hawkish again: Oct 36% / Dec 72%, cum 2.48 hikes to Apr-27.** ⛔ **Nothing re-arms: book FLAT, v1.7 stands.** Boot 12/14 (oil_roll_check failed CLOSED — handled by matched contracts; boj_ois needed the visual review, done).

**Signal Status:** ⚰️ **CARRY-CONVEXITY TAIL — RETIRED TO LOW (THESIS v1.7, 2026-08-07). Leg-1 SPF FIRED. Position FLAT; $0 was at risk.** · **v2.0 KILLED 8/20–27** (BIS K1 fired; RED killed it four more ways — `thesis/V20_CROSSREAD_2026-08-27.md`; nothing was owed to Will). · 🕯️ **v1.8 is a CANDIDATE in a SEPARATE document** (`thesis/V18_CANDIDATE_PILLAR1.md`), gated on SAM-41 + a separately-registered FX co-condition + RED pass + Will sign-off — **never on BIS.** SAM-41 historically confirmed but current gaps sit back above both bars (**0/5**); use its dated rider, not the archived Aug-7 case. ⛔ **NO SUCCESSOR FRAME DECLARED — v1.7 stands, and that is the honest state, not a gap to be filled.**

🔴 **The 8/7 print broke the frame.** CFTC Aug-4 **−45,473 = 24.2% of the corrected peak R = −188,077** — through the **−108K/60% leg-1 invalidation line**; character **REVERSAL, not liquidation**; book FLAT, $0 at risk. ⛔ The **"25.3% of −180K" form is RETIRED** (Will-ratified 8/11). 📌 Calibration residue: **45% assigned to CONFIRM, ~25% to what happened.** **Forensics and full lesson → `STATUS_ARCHIVE.md` § 2026-08-07 FRAME-BREAK FORENSICS.**

**Predictions:** **16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 1 OPEN (SAM-33)** — re-derived FROM `thesis/PREDICTIONS.tsv` (34 rows, 0 unclassified), not carried forward. 🔧 **SAM-28 `QUALIFIED / NO-VERDICT` · SAM-31 FALSE** — this read "SAM-28/31 both FAILED Sep-18" while the SAME sentence counted "1 qualified", and `PREDICTIONS.tsv` has carried the regrade since 9/19. **The CATO R4 cascade reached four STATUS sites, both trade docs and the brief, and missed the derived-count line** (METSUKE Run-22 E2). Canonical: `thesis/PREDICTIONS.tsv`.


*Detail → `thesis/THESIS.md` v1.7 · `CHANGELOG.md` 2026-08-07 · `outbox/2026-08-07_to-TERRY-PROME_RESOLVER-COMPLETE-section8-DE-LOAD-leg1-fired-frame-LOW.md` · pre-print re-pencil `thesis/REPENCIL_2026-08-07_PREPRINT.md` (committed BEFORE the print).*


---

## LIVE MARKET DATA

*Refreshed 2026-09-29 12:47–12:55Z. Each row keeps its own clock. FX = own hourly bars, Europe/London sessions (WQ-162); **9/29 is a LIVE bar, never scored.** JGB = MOF curve **Sep-28**.*

| Instrument | Level / vintage | Note |
|---|---|---|
| USD/JPY | Completed closes **9/24 158.755 · 9/25 157.185 · 9/28 157.433** (9/24 H **159.036** = peak; 9/28 L 156.498) · 9/29 **LIVE ~157.3–157.4** [~12:50Z] | **Yen-side move:** DXY ~flat (101.29 → 101.20, 9/24 → 9/28) while crosses fell too. Largest session range **1.92 yen [9/25] ≈ 1.2%**, under the disorder watch and in the yen-STRENGTH direction. 159 not re-tested; **160 not touched this month since ~9/2** (usdjpy.py "160 → 27d"). |
| ✅ **BOJ meeting OIS — 2026-09-29 15:15 JST** | **Oct-30 36% / OIS 1.3163% · Dec 72% · Jan-27 46% · Mar-27 57% · Apr-27 37%; cumulative 2.48 hikes to Apr-2027** | SAM visual transcription, chart SHA `ed4f664d…`, arithmetic cross-checked (differences chain; each % = diff ÷ 0.25), validated, ledger written. **vs 9/24: Oct 27→36, Dec 68→72, cum 2.18→2.48 — hawkish for the 2nd straight chart.** Bloomberg's "~30% Oct" (9/25 pm) is a different source and time, not a conflict. ⛔ Incremental 25bp equivalents are NOT next-hike-timing probabilities; cumulative counts are NOT probabilities. 🔴 **Source-age expiry Sat Oct-3 15:15 JST** (`MAX_AGE=4d`). |
| Brent — **matched contracts only** | **Dec `BZZ26`: 9/24 $100.22 → 9/25 97.44 → 9/28 97.83 → 9/29 live ~96.2**; Nov `BZX26` 9/24 **$106.60** (settle basis) | 🔧 **9/24 corrected:** STATUS had Nov/Dec 107.31 / 100.77 = POST-SETTLE vendor trades (BRENT 9/25 packet); settle basis **106.60 / 100.22**. **BZ=F moved Nov → Dec on 9/29** in this vendor (96.17) — the boot `oil_roll_check` failed CLOSED; no cross-roll % is quoted. Nov expires ~Sep-30. Wire reports Brent >$108 on 9/28 after Trump rejected Iran's Hormuz plan — **contract unstated, not reconciled here; BRENT owns.** Benchmark-mismatch caveat stands. |
| JGB MOF **Sep-28** | **2Y 1.981 · 5Y 2.441 · 10Y 3.082 · 20Y 3.888 · 30Y 4.122 · 40Y 4.124%** | **New MOF-basis highs on 10Y and 5Y** (5Y = record per Reuters). vs 9/24 MOF: 10Y +0.9bp, 30Y +0.7bp, 40Y +2.1bp — a grind, not a break. 30Y/40Y inversion **closed** (40Y 4.124 ≥ 30Y 4.122). ⚠️ Reuters reports a **10Y 3.115% intraday "last week"** — day not pinned, NOT verified here; never difference quote vs MOF. |
| **CFTC legacy JPY, Sep-22** | **Net +71,982 LONG** (L 192,274 / S 120,292); **OI 378,701** | Δ net **−48,377** (L −45,677 / S +2,700) — **40% of the long cut while USD/JPY rose 155 → 158.** OI **−164,101**: June's delivery week showed the same step (520,825 → 431,030 across the Jun-17 delivery, net ~flat) ⇒ the 9/15 **"OI series record" was partly delivery-week inflation** (inference, n=1 comparison). The net cut is real. Next print Fri Oct-2 (Sep-29 positions). |
| CFTC TFF, Sep-22 | Leveraged **+7,423** / asset-manager **+41,629** / dealer **−108,284** | Lev −15,747 (near flat), AM −12,216. Both spec cohorts **still net long** yen, smaller. |
| FXY | **58.22** [9/28 close] | Was 57.68 [9/24]. |
| Cross-pairs, **9/29 live** | EURJPY **178.47** / GBPJPY **208.03** / AUDJPY **109.97** | vs 9/24 live 180.75 / 210.02 / 111.38: yen **stronger vs all three** (~−1.0 to −1.3%) ⇒ yen-specific. |
| US–JP differential, **Sep-28** | **5Y 2.619pp / 10Y 2.158pp** (US 5.06 / 5.24%) | **Wider again** (9/24: 2.630 / 2.107) — the yen firmed while the 10Y gap widened ⇒ the 9/25–28 move was NOT rate-driven. SAM-41 bars not near. |
| JGB auctions | **40Y Sep-29: BTC 3.096× · highest accepted 4.125% · ¥299.7B** — descriptive only (ruling 9/11) | **Firmest of the 40Y's n=3 series** (May 2.702 · Jul 2.824); Bloomberg: strongest since 2020. Priced at the MOF 9/28 40Y (4.124%). Buyer identity not shown — "insurers came back" is inference. Next: **Sep-30 2Y** → **Oct-8 30Y** (frozen bars apply). |
| MOF weekly foreign LT debt | **+¥1,082.9B BUYING**, Sep-6–12 (still latest) | ⚠️ **Wk Sep-13–19 STILL NOT PUBLISHED** at 9/29 12:48Z (CSV + PDF Last-Modified 9/16 22:50Z). Cause not established. Next scheduled Thu Oct-1. 4-week −¥1.61T flag is carried entirely by the 8/16–22 week. |
| U.S. / Japan funding | SOFR 3.90 / IORB 3.90 ⇒ **0bp** [FRED 9/28]; HY **293** / IG **81bp** [9/25] → **`STATUS_REFERENCE.md` § FUNDING** | **LIVE STATE: no U.S. funding stress; SOFR at IORB into quarter-end.** HY +20bp in two sessions (HENRY's domain). None measures offshore FX swaps. |
| Carried context (ADRs, DXY, VIX, S&P, UST) | → **`STATUS_REFERENCE.md` § CARRIED MARKET CONTEXT** (refreshed 9/29) | UST 10Y/30Y **5.17 / 5.49%** [FRED 9/25]; ^TNX 5.24 [9/28]. |
| Japan macro / flow reference | → **`STATUS_REFERENCE.md` § DURABLE REFERENCE ROWS** | Services PPI Aug **+3.7% y/y** (Jul +3.6%), fastest in 2+ yrs [BOJ, rel 9/25; wires, not re-pulled]. |
| BOJ JGB purchase ops | **9/28: 1–3Y ¥355.0B · 10–25Y ¥100.0B · linkers ¥30.0B** = the same bucket sizes as 9/2 / 9/9; no 25Y+ op 9/24–9/29 | ✅ SAM-33 falsifier un-fired through **9/29** (`ope20260925/28/29.xlsx`: scheduled sizes + securities lending + funds-supplying only). Next: Oct–Dec schedule **Sep-30 17:00 JST**. |
| BOJ July MPM minutes (rel 9/28) | Hawkish: goal shifting from *raising* underlying CPI to 2% to *anchoring* it; one member warned of a "double shock" from a late response | 2+ outlets, not read at the primary. SoO for the Sep MPM Oct-1. |

**Durable reference rows → `STATUS_REFERENCE.md` § DURABLE REFERENCE ROWS** (warm, on-demand; current and citable). Holds the Aug-2026 CGPI figures, the 2025-base Japan CPI canon, the insurer hedge ratio, Tankan, and the July trade-balance/crude-volume detail. ⛔ The supersede warnings travel with them — never cite the 2020-base CPI pair or the old July 7.2% / June 7.1% PPI pair.

## CARRY UNWIND PROBABILITY

**Last assessed August 7: 7d ~3 / 30d ~8 / 60d ~13 — a HISTORICAL decomposed estimate, not a fresh rolling forecast.** Amplifier and residual OFF at that assessment; no re-pencil since. **No retired entry gate re-arms.** Method, vintage caveats and re-pencil rules → `STATUS_REFERENCE.md` § CARRY UNWIND PROBABILITY; method canon → `thesis/THESIS.md`.

## INTERVENTION STATUS — MOF posture

🟠 **LIVE STATE (9/29): a JOINT US–Japan verbal campaign (9/25–9/28) took USD/JPY from the 159.036 peak to a 156.498 low with NO operation found. Ladder graded T2-EQUIVALENT, not T3 — with a US leg the ladder has no row for.** ⛔ **NO intervention confirmed.** Hard record lands **tomorrow: MOF monthly (Aug-27→Sep-28), ~Sep-30 19:00 JST.**

| Field | Reading |
|---|---|
| Last tells | **T1 rate check ~158, Sep-18** (REPORTED). Then **words, not money:** Katayama 9/25 (Trump raised yen weakness with Takaichi; "counter excessive volatility and disorderly moves"), **Bessent 9/25 *"the desirability of a strong yen"*** (CONFIRMED), **Mimura 9/28 *"take that message at face value"* / funding: *"absolutely no such concern"*** (CONFIRMED, Reuters). Katayama 9/29 maintenance tone. |
| Level | Peak **159.036 [9/24]**; completed closes 158.755 → **157.185 [9/25]** → 157.433 [9/28]; 9/29 live ~157.3. |
| Speed | 9/25 range **1.92 yen ≈ 1.2%**, yen-STRENGTH direction — below the disorder watch; no fast yen-weakening leg has printed since 9/18. |
| Read | **9/24's reading (2) "MOF standing aside" is contradicted in its strong form** — the authorities answered the level break within ~24h, jointly with Washington. **Reading (1) (speed, not level) is untested.** ⚠️ A verbal campaign that works makes an operation LESS likely at these levels; the US endorsement is a WORD — a US operating leg is established only for 7/30–31 (FRBNY Q3 ~Nov-13). Detail → playbook 2026-09-29. |
| Adjacent | CFTC Sep-22: spec long-yen book **cut 40%** INTO the 158–159 grind (before the verbal campaign). UBS AM "sell yen into intervention" stays one manager's stated view. |

**Sep-7/8 attribution OPEN** (bears on SAM-31's qualification). Next hard evidence: **MOF monthly ~Sep-30** (Aug-27→Sep-28) · MOF quarterly **~Nov-9** · FRBNY Q3 **~Nov-13**. Full evidence + ladder → `STATUS_REFERENCE.md` § INTERVENTION STATUS and `MOF_INTERVENTION_PLAYBOOK.md` (S1/S1-A govern).

## KEY THRESHOLDS

> 🆕 **BASIS (WQ-162 convention) → `STATUS_REFERENCE.md` § USD/JPY MEASUREMENT BASIS.** LIVE STATE, one line: every USD/JPY level and USD/JPY-derived COUNT on this desk reads yfinance `USDJPY=X`, hourly bars aggregated to **Europe/London**-labelled **COMPLETED sessions only** (current bar never scored), **as LAST REVISED** in a 30-day window. ⛔ **NOT** the BOJ 17:00 JST reference rate and **NOT** the MOF curve — never blend or difference across bases. Rotated out of STATUS 2026-09-18 under the read-cap rule; **current and citable, not archived.**

| Level | Significance | Status |
|---|---|---|
| USDJPY 160 | Historical MOF zone; disorder, not level | Below: peak **159.036 [9/24]**, then back to **157.433** [9/28 close] on the joint verbal campaign — **~2.6 yen away.** Not the reaction zone (the 9/18 check fired at ~158); the retired gate stays VOID. No ≥160 count registered. |
| USDJPY 155 | Yen-strength watch; investigate mechanism | **ABOVE** — 10 straight completed closes above 155 (9/15→9/28); 9/28 low 156.498 = **1.5 yen above**. The mechanism question is already live: official words, not flows or positioning, moved the 9/25–28 leg. |
| USDJPY 158 | VECTOR-5 re-open leg (c) | 🔵 **LAPSED 9/25** — completed closes back below 158 (157.185 / 157.433). Held in letter 9/23–9/24 only. Was: 🟠 **LETTER MET 9/23: completed close 158.266 > 158 "while Brent holds"** (Nov 103.87 [9/18] → 103.08 [9/23]). ⚠️ **Spirit confounded:** the leg names the terms-of-trade channel "rather than the rate differential" — and the differential **widened** over the same window (10Y gap +8bp on 9/18; UST 10Y 5.01 → 5.11%). One close. **The re-open test needs ALL THREE legs: (a) MET [Aug crude volume +3.6% YoY], (c) MET-in-letter, (b) NOT MET ⇒ answer stays NONE.** Packet → PROME (VECTOR-5 owner, DOCKET L328). |
| USDJPY 147 / 145 | Carry / insurer investigation levels | Above both. |
| JGB 10Y 2.40% | Stress crossover | Above at **3.082%**, MOF **Sep-28** (new MOF-basis high). |
| JGB 30Y 4.0% | Contested demand-floor zone | Above: 30Y **4.122%** / 40Y **4.124%**, MOF Sep-28 — inversion closed. **40Y auction 9/29 BTC 3.096× at 4.125%** = firmest of its series (the named bid under ~4% reads live, buyer unidentified). SAM-33 op-record verified **through Sep-29**; next check **Sep-30 17:00 JST**. |
| JGB 30Y 4.5% | Contested impairment tail | **37.8bp away** on MOF Sep-28; no forced-sale inference. |
| Brent $90 / $120 | Oil context / shock watch | **Dec `BZZ26` $97.83** [9/28] (~96.2 live 9/29); Nov expires ~9/30. $90 is $7.83 away on Dec; $120 is ~$22 above Dec. Never compare across rolls (`oil_roll_check.py` failed CLOSED at the 9/29 roll). |
| Oil-in-yen ¥18,000/bbl | VECTOR-5 re-open leg (b) | **NOT MET.** Dec × completed close 9/28 ≈ 97.83 × 157.433 ≈ **¥15,402**; Nov 9/24 settle × close ≈ 106.60 × 158.755 ≈ ¥16,923. Close-on-close approximation; the gap is far outside that error. Needs 5 consecutive sessions. |
| CFTC −108K / −140K / −153K | Retired frame's short-side lines | Moot in direction — **Sep-22 net +71,982 LONG** (from +120,359). **No rearm.** ⚠️ The mirror question (a long-yen crowd squeezed by yen weakness) has **NO registered line** — and the crowd cut 40% before any squeeze print. None is invented here. |

## WHAT TO WATCH (forward only — full docket → `docket/CALENDAR.md`)

Retired entry triggers remain void; this is a research docket.

| When | Event | Why it matters |
|---|---|---|
| 🟠 **Wed Sep-30** | **MOF monthly intervention total (Aug-27→Sep-28), ~19:00 JST (date = cadence estimate)** · BOJ Oct–Dec purchase schedule 17:00 JST · **METI Aug crude-by-source 13:30 JST** · 2Y auction · Aug IP / retail 08:50 JST | MOF: ¥0 ⇒ the 9/18 check and the 9/25 move were words only; non-zero ⇒ an op in-window (dates only via ~Nov-9 quarterly). BOJ schedule = **next SAM-33 check** (scheduled taper change does NOT count). RED CH-009 graded on the 9/30 MOF 30Y close (≥4.300 ⇒ NO-VERDICT; now 4.122). |
| Thu Oct-1 | BOJ Summary of Opinions (Sep MPM) + Tankan · MOF weekly (Sep-13–19 still missing) | SoO: is oil named, and how. MOF weekly: does the missing week appear with the next one? |
| Fri Oct-2 | Tokyo CPI (Sep) · **CFTC (Sep-29 positions)** | 🔧 METI crude-by-source moved to **Wed Sep-30 13:30 JST** (observed at METI, KOYOMI Run 23; Oct-2 was an unlabelled estimate). Tokyo CPI Fri Oct-2 / Tankan Thu Oct-1 **confirmed at the Stats Bureau and BOJ calendars** — the wire's weekday was a timezone rendering. CFTC: does the long keep shrinking? |
| **Sat Oct-3 15:15 JST** | BOJ OIS quote expires (4-day rule) | Re-transcribe the chart — SAM's job. |
| Oct-8 | 30Y auction | Next test the frozen FIRM/SOFT bars apply to. |
| Standing | **A fast yen-WEAKENING leg** (≥1.5–2%/day or ~2–3 yen over 1–2 sessions) | The only thing that tests reading (1). Semi-confirm any spike via BOJ current-account projections vs broker forecasts ~2 business days later. |
| ⚠️ **owed, undated** | **RED salvage ④ — a real JPY xccy-basis instrument** | Still owed; the fixed CME proxy stays expired and is not revived. |

## POSITION — FLAT

No FXY position was opened during the retired convexity-tail episode; $0 was at risk in that frame. Earlier trading history is separate and preserved; the last Will-confirmed flat state was June 29. No frame-specific close/P&L is created. TRY-FIRE-007 stands down. Retired entry gates are void; any re-entry requires a fresh independently argued thesis and Will's approval. Historical decision records remain in `TRADE.md` and CHANGELOG.

## CHANNELS · BOJ · FED

**BOJ policy rate 1.25% — RAISED 25bp at the September 17–18 MPM, effective September 24 2026** (primary `k260918a.pdf`, parsed in-session). Complementary deposit facility 1.25%; basic loan rate 1.50%. Highest since 1995. The **0.75%** Takaichi mortgage-ceiling threshold is now breached by 50bp. 🔧 **Home corrected 2026-09-20: it is `AGENTS/SAM/CLAUDE.md:235`, NOT root `CLAUDE.md`** (root has zero hits) — the misattribution pointed the fix at a Will-gated file instead of SAM's own (METSUKE Run-22 E3). Channel 1 remains RETIRED and requires direct foreign SALES at ≥2 institutions across ≥2 consecutive windows; yields and ESR are co-conditions, never substitutes. Carry-convexity/positioning frames remain retired. **Mechanism canon → `thesis/THESIS.md`; September MPM source detail and the officials' record → `STATUS_REFERENCE.md` § CHANNELS · BOJ · FED.**

## PREDICTIONS

✅ **CATO R4 SETTLED 2026-09-19** — upheld 4 of 5; nothing graded TRUE. → [ruling](docket/2026-09-19_CATO-R4-RULING.md). ⚠️ **SAM-31's FALSE carries a qualification that must travel with any citation** — on a strict single-episode reading it is QUALIFIED, because the one candidate episode (Sep-8/9) has OPEN official attribution, and open attribution prevents confirmation rather than establishing failure.

**16 CONFIRMED / 15 FAILED / 1 special / 1 qualified / 1 OPEN (SAM-33)** — re-derived FROM `thesis/PREDICTIONS.tsv` (34 rows, 0 unclassified), never carried by hand. `boot.py --predictions` derives OPEN rows and checks the sidecar; it never grades.

- **SAM-28:** ≥1 eligible tail route ≥+3% FXY by Sep-18, 40%, 🟠 **RESOLVED — QUALIFIED / NO-VERDICT.** Four routes NO-FIRE on fact; the fifth (sustained MOF #3) **fired as operations** (7/30–31) with **an attribution window the registration never fixed** — that alone carries the no-verdict. 🔑 The record favouring this reading was one the governing packet **ordered** me to consult and I consulted only after challenge. Withdrawn: Episode-B control, the "correctly calibrated" label, the "+2% blended" argument. **Full prose → `STATUS_ARCHIVE.md` § SAM-28 / SAM-31.**
- **SAM-31:** yen-haven re-couples by Sep-18, 35%, 🔴 **RESOLVED FALSE — always report it WITH its qualification; a bare "FAILED" drops information that matters.** An **interpretive owner judgement** on the regime reading, on same-clock evidence only (n=24 risk-off, yen stronger on 7 = 29.2%, mean −0.154%; window VIX max 20.66). ⚠️ **Three things are NOT settled and travel with every citation:** ① on a strict **single-episode** reading it is **QUALIFIED** — the only candidate, **9/8–9/9**, has **OPEN** attribution, which *prevents confirmation rather than establishing failure*; ② **a window mean cannot exclude the channel returning LATE**, and 9/8–9/9 are the window's last risk-off sessions; ③ **7/13** stays unresolved (same-clock FXY −0.493% vs 4-of-4 cross strength). **Matched intraday cross-pair data settles ①–③ and is owed, not scheduled — if obtained, THE ROW IS RE-OPENABLE.** Full prose → `STATUS_ARCHIVE.md`; reasoning → [ruling](docket/2026-09-19_CATO-R4-RULING.md) §§ ADDENDUM, ADDENDUM 2.
- **SAM-33:** no BOJ emergency long-end capping through Dec-31, 72%, OPEN (activation MET 8/17 ⇒ a genuine test). ✅ **Ops record audited through Sep-29** (`ope20260924/25/28/29.xlsx`: securities lending, funds-supplying, and outright purchases at the SAME bucket sizes as earlier September ops — 1–3Y ¥355.0B, 10–25Y ¥100.0B; no 25Y+ op, no fixed-rate op). 9/24 was the first real stress day and the BOJ did not cap; 9/25–29 the long end ground another ~1–2bp (MOF) and the 40Y auction cleared firm. **Next: Sep-30 17:00 JST Oct–Dec schedule** (a scheduled taper change does NOT count).
- **SAM-39:** RESOLVED CONFIRMED Sep-4, **TRUE-IN-LETTER / FALSE-IN-SPIRIT** — range cleared the bar without proving the named official-action mechanism. **A successor owes a preregistered SHAPE leg.** Registered instrument = `usdjpy.py` hourly-derived intraday **RANGE**, **≥2.5-yen bar** — ⛔ **not a ≥160 level count; no such count exists on this desk.** Basis blockquote: § KEY THRESHOLDS (canonical home).

Calibration residue: **naming a risk and underweighting it is distinct from missing it.** As-made audit dispositioned 9/10 (one scoring vintage moved, SAM-07 75%→48%; scoreboard unchanged) → `audits/2026-09-10_asmade-disposition.md`. Full post-mortems → `thesis/PREDICTIONS_ARCHIVE.md`.

---

Thesis v1.7 → `thesis/THESIS.md`; audit → `thesis/CHANGELOG.md`; cross-agent synthesis → `NEXUS_BRIEF.md`. No successor declared.
