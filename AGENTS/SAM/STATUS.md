# SAM STATUS

**Last written: 2026-09-18T15:15+00:00 — Will-directed boot / dark-period catch-up (September 18 ET). BOJ MPM, FOMC and the August trade/CPI prints all landed while SAM was dark 9/15→9/18.** [Prior report](reports/2026-09-15_news-sweep.md). Book last recorded FLAT, not newly broker-reconciled.

**Signal Status:** ⚰️ **CARRY-CONVEXITY TAIL — RETIRED TO LOW (THESIS v1.7, 2026-08-07). Leg-1 SPF FIRED. Position FLAT; $0 was at risk.** · **v2.0 KILLED 8/20-27** (BIS K1 fired; RED's CHG-RED-048 killed it four more ways independently; cross-read `thesis/V20_CROSSREAD_2026-08-27.md` — nothing was owed to Will). · **v1.8 (`thesis/V18_CANDIDATE_PILLAR1.md`) is a SEPARATE document**, gated on SAM-41 + a separately-registered FX co-condition + RED pass + Will sign-off — **never on BIS**. ⛔ **NO SUCCESSOR FRAME DECLARED — v1.7 stands, and that is the honest state, not a gap to be filled.**

🔴 **The 8/7 print broke the frame.** CFTC Aug-4 **−45,473 = 24.2% of the corrected peak R = −188,077** — through the **−108K/60% leg-1 invalidation line by 62,527 contracts**; character **REVERSAL, not liquidation**; book FLAT, $0 at risk. ⛔ The **"25.3% of −180K" form is RETIRED** (Will-ratified 8/11; contract gates unaffected, only percentage labels moved). 📌 Calibration residue: **45% assigned to CONFIRM, ~25% to what happened** — third of the over-confidence cluster (SAM-08 @90%, SAM-20 @60%), opposite direction. **Forensics, resolver narrative and the full lesson are verbatim in `STATUS_ARCHIVE.md` § 2026-08-07 FRAME-BREAK FORENSICS — not restated here.**

**Predictions:** 16 CONFIRMED / 14 FAILED / 1 special / 3 OPEN (SAM-28/31/33). SAM-39 closed Sep-4; SAM-41 historically confirmed. Canonical: `thesis/PREDICTIONS.tsv`.

🕯️ **v1.8 CANDIDATE ONLY:** `thesis/V18_CANDIDATE_PILLAR1.md`. SAM-41 historically confirmed; current gaps have widened back above both bars (0/5). Promotion requires a separately registered FX co-condition, RED review and Will sign-off. No successor, no entry trigger; use the candidate's dated rider, not its archived August 7 case. **Distinguish FX level, cohort stocks and measured liquidation.**

*Detail → `thesis/THESIS.md` v1.7 · `CHANGELOG.md` 2026-08-07 · `outbox/2026-08-07_to-TERRY-PROME_RESOLVER-COMPLETE-section8-DE-LOAD-leg1-fired-frame-LOW.md` · pre-print re-pencil `thesis/REPENCIL_2026-08-07_PREPRINT.md` (committed BEFORE the print).*


---

## 2026-09-18 — BOJ MPM GRADE (owner grade; PROME DOCKET L34 closed on this)

**BOJ raised the policy rate 25bp to 1.25%, vote 7–2, effective September 24** — highest since 1995. Primary `k260918a.pdf`, text-extracted in-session; vote footnote read verbatim, not relayed. **FOMC hiked the same week** to 3.75–4.00%, 12–0, with SEP medians moving **UP** (2026 3.8→4.1 / 2027 3.6→4.1%).

**SAM's three-leg pre-registration, graded on its own terms — no leg re-tuned at scoring time:**

| Leg | Registered | Outcome | Grade |
|---|---|---|---|
| Vote split | "2+ dissent **for a faster pace**" | 2 dissents, **both for HOLD** (Asada: core "below 2 percent", *maintain*; Sato: "not substantially accelerated") | 🔴 **HAWKISH SURPRISE DID NOT FIRE** — count matched, sign is the mirror image |
| Oil naming | activity ⇒ dovish · price ⇒ hawkish | named both ways, **activity dominant**; price side reaches only PPI | 🟢 **DOVISH-FOR-PACE** |
| Balance sheet | "a change is the surprise" | **no JGB purchase-plan change**; only a unanimous technical climate-ops change | 🟢 **NO SURPRISE** |

⚠️ **Composite clause graded a MISS.** Registered: *"The surprise is a HOLD, and it is yen-NEGATIVE."* No hold printed. The yen weakened anyway (154.82 [9/15] → **157.34** [9/18]) — but via the **dovish split + full pricing**, not the named mechanism. ⛔ Logged as a calibration loss, not a directional hit: right call on a wrong mechanism is a miss under this desk's mechanism-direction failure class.

**Substance:** the BOJ hiked with **core CPI at 1.7%, below its own target** — Asada's dissent turns on exactly that. **CH-004 confirmed a third time: a fully-priced hike does not unwind carry.** **Consequences to the frame: none.** v1.7 RETIRED-to-LOW stands; no retired gate re-arms; 160 gate VOID, not re-armed; book FLAT. **SAM-33 un-falsified**, verified at `ope20260916.xlsx` (25Y+ offered 750 = exactly scheduled; no fixed-rate/unscheduled op) — at the record, not inferred from silence.

**Full grade, dark-period ledger and the primaries → [`reports/2026-09-18_boj-mpm-grade.md`](reports/2026-09-18_boj-mpm-grade.md).**

---

## 2026-09-15 — News integration · Historical September 10–11 notes

↪️ **MOVED 2026-09-18 → `STATUS_ARCHIVE.md` § 2026-09-15 NEWS INTEGRATION (rotated).** Both blocks were settled and already carried before-image pointers; rotated under the READ-CAP rule when the 9/18 BOJ grade pushed STATUS into the rotate tier. Their findings survive in the tables below.

## LIVE MARKET DATA

*Refreshed September 14 ET / September 15 JST. Each row retains its observation clock; rows not refreshed retain older dates. Intraday observations and completed sessions are distinct.*

| Instrument | Level / vintage | Note |
|---|---|---|
| USD/JPY | **157.34** [Sep-18 15:01:50 UTC, Yahoo `USDJPY=X`] | Live vendor observation, post-BOJ. Was 154.82 [Sep-15 02:27 UTC]. PROME's dashboard read **157.86 [10:21 ET]** — a different clock, not a disagreement; do not blend. Completed-session basis (WQ-162) not re-derived this session. |
| **BOJ September pricing — SPENT** | Pre-decision **99% / OIS 1.2238%** [Sep-15 11:15 JST] | ⚰️ Meeting RESOLVED, hike delivered ⇒ fully priced, therefore **not** hawkish-of-priced. Later-meeting equivalents from that image are stale vintages, not current pricing. Boot 9/18 could NOT refresh: `boj_ois.py` returned an unreviewed chart (SHA256 `1105fdfc…`) needing visual review — **no current BOJ pricing on this desk.** |
| Brent / oil-in-yen | **$99.56**, BZ=F [Sep-18 14:51:21 UTC] | Continuous context quote; was $106.90 [Sep-15]. Back through $100 to the DOWNSIDE despite Petroline shut since 9/11 (WALTER SIG-W-20260917-001). No fresh synchronized oil-in-yen product or completed-session five-day count asserted. |
| JGB MOF **Sep-17** | **10Y 2.993 / 30Y 4.047 / 40Y 4.036%** | MOF curve, distinct from on-the-run quotes. All three above their watch levels; level alone identifies neither sales nor emergency capping. Pre-dates the 9/18 hike. |
| CFTC legacy JPY, Sep-8 | **Net +10,796**; long 178,791 / short 167,995; OI 499,635 | Δ long +61,622 / short −41,401 / net +103,023 / OI +87,753. New longs and short covering coexist; motive and forced liquidation are not identified. |
| CFTC TFF, Sep-8 | Leveraged net **−49,098**; asset-manager **−570** | Leveraged longs +23,231 / shorts −29,859; both TFF sides reconcile to OI. [Resolved review](docket/2026-09-11_CFTC_REVIEW.md). |
| FXY | **58.30** [Sep-18 15:01:25 UTC] | Live vendor observation; was 59.43 [Sep-14 close]. The Sep 2–9 rally to 59.70 has been given back. YCS/EWJ/DXJ not refreshed this session (Sep-14 closes 51.64 / 97.58 / 177.19). No SAM-28 route attribution or grade — that is the close-of-18 adjudication. |
| Cross-pair, **Sep-18 live** | EURJPY **180.36** / GBPJPY **210.21** / AUDJPY **111.83** [15:01:4x UTC] | Yen weaker on every cross, not a USD story — consistent with a domestic (BOJ) driver rather than a haven rotation. Bears on SAM-31; **not a grade.** |
| ⚠️ **NOT refreshed — Sep-14/15 vintages** | ADRs MUFG 23.89 / SMFG 27.24 / MFG 11.33 · DXY 99.583 · VIX 17.10 · S&P 7,619.98 · FXY ATM IV 16.24% (Oct-16) / 18.97% (Sep-18) · MOF Aug lifer LT −¥137.3B / trust +¥2,332.6B | **Carried, NOT re-marked — all pre-date both hikes; do not read as current.** Later tape at its own basis in WALTER SIG-004 (VIXCLS 17.71 [9/16]; ^VIX 15.44 intraday [9/17]). Thin ETF proxy ≠ FX vol; trust ≠ GPIF; LT debt ≠ UST. |
| US–JP differential, **Sep-17** | **5Y 2.458pp / 10Y 1.947pp** (US 4.78 / 4.94%) | Narrowed ~4bp/3.5bp from Sep-14 but still above both SAM-41 bars; runs **0/5**. **Pre-dates both hikes** — the two 25bp moves broadly offset, so no compression is claimed from this print. Historical SAM-41 confirmation unchanged. |
| JGB auctions | **20Y Sep-15 BTC 4.005× / tail 1.3bp; cutoff 3.869%: AMBIGUOUS** | Neither frozen branch fires; tail misses FIRM by 0.3bp. Generic script “Orderly” is not the grade. Counter 0/2; Sep-29 40Y descriptive only. Sep-3 30Y SOFT remains PRECISION-LIMITED. |
| MOF weekly foreign LT debt | **+¥1,082.9B BUYING**, Sep-6–12 | 🔧 **4-week LT −¥1.608T** (prior window −¥1.55T) — still 🟡 above the ¥1.4T upper, **but carried entirely by the 8/16–22 week (−¥1.978T), which rolls out next week.** Weekly is BUYING and improving three straight (−0.824 → +0.112 → +1.083T), nowhere near the ≥¥1.5T weekly SELLING bar. **Flag and trend now point opposite ways.** Not UST-specific. |
| U.S. / Japan funding | Sep-11 SOFR **3.62%**, IORB **3.65%**, spread **−3bp**; HY **265bp**, IG **80bp** | Sep-14 Japan O/N provisional **0.977%**, repo T+1 **1.000%**. GC T/N ~1.005% is separate; none measures offshore swaps. |
| Japan domestic data | Q2 GDP **+1.4% ann.**; July wages **+4.1% YoY**; **July current account +¥2,988.9B (+15.6% YoY)**, rel Sep-8 | BoP goods −¥399.9B, services −¥512.9B, **primary income +¥4,289.6B** (MOF `bp202607.pdf`). BoP goods ≠ customs (revised −¥638.3B). **The VECTOR-5 denominator: the oil shock is 4.0% of ONE month's CA surplus.** |
| New macro/flow context | July IIP **−0.2% m/m** (METI Sep-14); FY2027 requests **¥143.0656T** (MOF Sep-4); August foreign equity/fund net **+¥1.2983T** (MOF Sep-8) | IIP shipments +2.1%; requests ≠ enacted spending/issuance; flows ≠ NISA-only or measured FX trades. [Sources](reports/2026-09-15_news-sweep.md). |
| BOJ **Sep-16** JGB purchase ops | **3–5Y ¥320B / 5–10Y ¥335B / 25Y+ ¥75B**; 25Y+ BTC **1.84×** | ✅ Verified at the record (`ope20260916.xlsx`): 25Y+ offered **750** = exactly the Aug-31 scheduled size (`mpr260831a.pdf`); no fixed-rate, unscheduled or enlarged op ⇒ **SAM-33 falsifier un-fired.** 25Y+ cover fell 2.51× [Sep-9] → 1.84× — a BOJ *purchase-op* ratio, **not an auction BTC**; no demand grade drawn. Next: Oct–Dec schedule, Sep-30 17:00 JST. |
| **FOMC Sep-16 — RESOLVED** | **Hiked 25bp → 3.75–4.00%, 12–0.** SEP medians **2026 3.8→4.1 / 2027 3.6→4.1%** | Dots moved UP. SAM's registered Fed-side tripwire is an actual **dot walk-back** — this is its opposite by 50bp on the 2027 median; that SAM-28 route **ANTI-FIRED**. Pre-decision pricing is moot and not restated. |

**Durable reference rows → `STATUS_REFERENCE.md` § DURABLE REFERENCE ROWS** (warm, on-demand; current and citable). Holds the Aug-2026 CGPI figures, the 2025-base Japan CPI canon, the insurer hedge ratio, Tankan, and the July trade-balance/crude-volume detail. ⛔ The supersede warnings travel with them — never cite the 2020-base CPI pair or the old July 7.2% / June 7.1% PPI pair.

## CARRY UNWIND PROBABILITY

**Last assessed August 7: 7d ~3 / 30d ~8 / 60d ~13 — a HISTORICAL decomposed estimate, not a fresh rolling forecast.** Amplifier and residual OFF at that assessment; no re-pencil since. **No retired entry gate re-arms.** Method, vintage caveats and re-pencil rules → `STATUS_REFERENCE.md` § CARRY UNWIND PROBABILITY; method canon → `thesis/THESIS.md`.

## INTERVENTION STATUS — MOF posture

**LIVE STATE: Sep-7/8 attribution remains OPEN.** Sep-10/11/14 finals all reconcile to provisional or forecast within ±¥90B; no operation size inferred from residuals, and Japan settlement data cannot exclude a US-only leg. Official-reserve funding/account split unresolved. **No new signature in the 9/15→9/18 window.** 160 gate VOID, not re-armed (USD/JPY 157.34).

**Full evidence, the confirmation ladder, the Aug-3 detector ambiguity, official windows and the pending FRBNY (~Nov-13) / MOF quarterly (~Nov-9) primaries → `STATUS_REFERENCE.md` § INTERVENTION STATUS.** `MOF_INTERVENTION_PLAYBOOK.md` S1/S1-A governs.

## KEY THRESHOLDS

> 🆕 **BASIS (WQ-162 convention, encoded 2026-09-11 — a CONVENTION line, never a revision claim).** Every USD/JPY level and every USD/JPY-derived COUNT on this desk is read on: yfinance `USDJPY=X`, 1-hour bars aggregated to sessions labeled in **Europe/London** (the index's own zone), **COMPLETED sessions only** — the current bar is never scored. Intraday range = session high − session low, in yen. Observations are taken **as LAST REVISED** inside a 30-day upsert window (`usdjpy.py --revise-window`), **not as first published**. ⛔ This is **NOT** the BOJ 17:00 JST reference rate and **NOT** the MOF curve: never blend or difference across bases. `dashboard.py` and `fetch.py price USDJPY=X` read the SAME yfinance series and are basis-compatible; the BOJ 17:00 JST fix is not. ⚠️ **The vintage direction is deliberately OPPOSITE to LIQUID's GATE-HY-REKILL letter ("as FIRST published")** — HY OAS revisions are rare and first-publication protects a closed count, whereas this instrument's revisions **are its bug fix** (it silently under-stated 7/31 as 2.17y against a true 3.655y, so first-publication grading would have resolved SAM-39 FALSE on a known-defective measurement). Declaring the direction is the point of the convention.

| Level | Significance | Status |
|---|---|---|
| USDJPY 160 | Historical MOF zone; disorder, not level | Below at live 154.82; completed Sep-14 154.31. Retired gate remains VOID; no ≥160 count registered. |
| USDJPY 155 | Yen-strength watch; investigate mechanism | Below at live 154.82; completed Sep-14 154.31. No mechanism grade. |
| USDJPY 158 | VECTOR-5 re-open leg (c) | Not crossed on latest completed Sep-14 close 154.31. Joint Brent condition not re-evaluated; no re-open. |
| USDJPY 147 / 145 | Carry / insurer investigation levels; no forced-flow inference | Above both. |
| JGB 10Y 2.40% | Stress crossover | Above at 2.988%, MOF Sep-14. |
| JGB 30Y 4.0% | Contested demand-floor zone | Above: 30Y and 40Y 4.040%, MOF Sep-14. SAM-33 op-record review remains through Sep-9; next Sep-16. |
| JGB 30Y 4.5% | Contested impairment tail | 46bp away on MOF Sep-14; no forced-sale inference. |
| Brent $90 / $120 | Oil context / shock watch | BZ=F $106.90, Sep-15 02:15:18 UTC. Continuous context quote, not a registered contract-specific count. |
| Oil-in-yen ¥18,000/bbl | VECTOR-5 re-open leg (b) | Not re-evaluated this boot: synchronized contract-specific five-completed-session observations required. Prior Sep-11 assessment FALSE; no fresh count. |
| CFTC −108K / −140K / −153K | Retired frame's leg-1 invalidation + historical DE-LOAD / reclaim lines | −108K **fired Aug-7**; the others are **moot in direction** — Sep-8 printed **+10,796, NET LONG**, and retired short-side lines cannot fire on a long book. No rearm. OI **499,635, +87,753** [Sep-8]; aggregate growth cannot exclude forced short covering within a cohort. New print today 15:30 ET. |

## WHAT TO WATCH (forward only — full docket → `docket/CALENDAR.md`)

Retired entry triggers remain void; this is a research docket.

| When | Event | Why it matters |
|---|---|---|
| **Sep-16** | 25Y+ BOJ operation date · **Japan August trade balance 08:50 JST** · FOMC | 25Y+ date = repeat the KB-SAM-238 schedule check for SAM-33. **Trade balance is leg (a) of the VECTOR-5 re-open test AND the honest test of the oil-in-yen inversion — read crude VOLUME, not value** (Jul: value +87.8% YoY, volume +5.5%). |
| ✅ **Sep-18 RESOLVED** | **BOJ MPM — hiked to 1.25%, 7–2** · National CPI Aug **1.9 / 1.7 / 1.9** (2025 base) | **Owner grade of the three-leg pre-registration → § 2026-09-18 BOJ MPM GRADE below.** Headline: the registered hawkish surprise (2+ dissent *for a faster pace*) **did NOT fire — both dissents were for HOLD.** |
| **Sep-18 close — TODAY, PENDING** | SAM-28 and SAM-31 | Both still OPEN at 40% / 35%; grade AFTER the 16:00 ET close per the registered terms. `docket/2026-09-18_SAM28_SAM31_REVIEW.md` carries evidence/ambiguities. **Two of SAM-28's five routes resolved NO-FIRE today** (§ below). The MOF-episode endpoint and the Sep 2–9 attribution remain the unresolved legs — do not pick the convenient endpoint at scoring time. |
| ⚠️ **owed, undated** | 🆕 **RED salvage ④ — a REAL JPY xccy-basis instrument** | **The v2.0 kill salvaged four things; ④ is the sizing/basis instruments, and RED called the JPY cross-currency basis *"the single highest-value output of the review… the nearest thing to a DISCRIMINATING observation that exists"* — a ~$400B swap-funded book is invisible to CFTC but **not to its funding market**. ⛔ **On 2026-09-11 I let the fixed CME proxy lapse (correctly — it sign-flips on the 9/18 hike) and wrote that "no threshold, gate, prediction or trade trigger depends on it." That was true and INCOMPLETE: this salvage obligation did, and it was tracked nowhere.** The defective proxy still should not be activated; what is owed is a genuine instrument (policy rate as an INPUT, a reader that rejects rounded/desynced legs, two same-session official pairs). Registered here so it stops being invisible. |
| Sep-29 | 40Y auction | September 11 ruling: descriptive BTC only, no FIRM/SOFT grade; uniform-price has no tail. Counter remains 0-of-2. |
| Sep-30 17:00 JST | BOJ Oct–Dec JGB purchase schedule | Per `mpr260831a.pdf`. A scheduled taper-plan adjustment does **NOT** count against SAM-33; an unscheduled capping op would. |

## POSITION — FLAT

No FXY position was opened during the retired convexity-tail episode; $0 was at risk in that frame. Earlier trading history is separate and preserved; the last Will-confirmed flat state was June 29. No frame-specific close/P&L is created. TRY-FIRE-007 stands down. Retired entry gates are void; any re-entry requires a fresh independently argued thesis and Will's approval. Historical decision records remain in `TRADE.md` and CHANGELOG.

## CHANNELS · BOJ · FED

**BOJ policy rate 1.25% — RAISED 25bp at the September 17–18 MPM, effective September 24 2026** (primary `k260918a.pdf`, parsed in-session). Complementary deposit facility 1.25%; basic loan rate 1.50%. Highest since 1995. The root-CLAUDE.md 0.75% Takaichi mortgage-ceiling threshold is now breached by 50bp. Channel 1 remains RETIRED and requires direct foreign SALES at ≥2 institutions across ≥2 consecutive windows; yields and ESR are co-conditions, never substitutes. Carry-convexity/positioning frames remain retired. **Mechanism canon → `thesis/THESIS.md`; September MPM source detail and the officials' record → `STATUS_REFERENCE.md` § CHANNELS · BOJ · FED.**

## COMPRESSED SESSION-NOTE POINTERS
*Narratives → `thesis/timeline/TIMELINE.md`; full bodies in git history. Compression passes: 7/11, 7/23, 8/02, 8/13, 8/14, 8/17, 8/20, **8/23**.*

> ### ↪️ MOVED: § PRE-REGISTRATION — INTERVENTION CHARACTER (written 2026-08-03, pre-print)
> **Now at `thesis/INTERVENTION_CHARACTER_2026-08-03_PREREGISTRATION.md`** (verbatim, moved 2026-08-10; consumer check run first). Closes `MSG-PROME-20260803-001#SAM-01`; falsifiable form = **SAM-39**, RESOLVED CONFIRMED Sep-4 (true-in-letter / false-in-spirit). Verdict was **FATTEN, MEDIUM**. 🔧 leg 3 ("the carry crowd is the only structural seller") **DIED with the frame on 8/7**; legs 1-2 are **frame-independent and survive**, which is why SAM-39 is graded on its own terms.
>
> ### ↪️ MOVED: § BOJ MPM PRE-REGISTRATION · § GRADE · SAM-38 contamination clause
> **Now at `thesis/BOJ_2026-07-31_PREREGISTRATION.md`** (verbatim, 2026-08-02 compression pass).
>
> ⚠️ **Both redirects are kept because EXTERNAL CONSUMERS CITE THESE SECTIONS BY NAME** — notably `AGENTS/WALTER/design/SIGNAL_PROCESSING_CHECKLIST.md` §v0.30 (the fleet-wide pre-decision-contamination guard) and WALTER's processed 7/31 packet. Per `[[finding_external_consumer_check_before_restructure]]`: **do not delete either line without re-checking who points here.**

## PREDICTIONS

**16 CONFIRMED / 14 FAILED / 1 special / 3 OPEN**, unchanged pending today's close. Canonical rows: `thesis/PREDICTIONS.tsv` — original conditions and the calibration warning live there. `boot.py --predictions` derives OPEN rows and checks the reminder sidecar against condition hashes; it never grades or changes terms.

- **SAM-28:** ≥1 eligible tail route produces ≥+3% FXY by Sep-18, 40%, **OPEN — grades at today's 16:00 ET close.** The MAGNITUDE bar has been cleared more than once; the **ROUTE leg has never been.** 🔴 **Two routes died today and are now settled NO-FIRE:** Fed-dot walk-back **anti-fired** (SEP medians moved UP 2026 3.8→4.1 / 2027 3.6→4.1) · hawkish-of-priced BOJ **did not fire** (99% priced, hike delivered, both dissents dovish, yen weakened). Risk-off ✗ and oil-MOU ✗ (anti-correlated through the September episode). **The only live candidate is the Jul-30→Aug-3 MOF episode (+4.22%)**, whose episode/"sustained" endpoint convention is **unresolved** per `docket/2026-09-18_SAM28_SAM31_REVIEW.md`. ⛔ **Do not retrofit a route, and do not pick the endpoint that produces the preferred grade — disclose the alternatives and the sensitivity.** Direction is not a grade.
- **SAM-31:** yen-haven re-couples by Sep-18, 35%, **OPEN — grades at today's close.** Evidence runs against the row: no genuine VIX-spike regime in the window (VIX 17.71 [9/16], 15.44 intraday [9/17]; 2026 low 14.13), and the yen **weakened** through both central-bank decisions. **No numeric VIX bar has been invented and none may be at scoring time.**
- **SAM-33:** no BOJ emergency long-end capping through Dec-31, 72%, OPEN. Activation MET / VOID clause lifted 8/17 ⇒ a genuine test, not a free TRUE. ✅ **Sep-16 ops audited AT THE RECORD (`ope20260916.xlsx` vs `mpr260831a.pdf`): 25Y+ offered 750 = exactly scheduled, no fixed-rate, unscheduled or enlarged op ⇒ falsifier un-fired through Sep-16.** The 9/18 hike does not bear on it (a policy-rate move is not a long-end capping op). A DISORDER response does not falsify; a scheduled taper-plan change is excluded by the row's own terms. **Next check: Sep-30 17:00 JST Oct–Dec schedule.**
- **SAM-39:** RESOLVED CONFIRMED Sep-4, **TRUE-IN-LETTER / FALSE-IN-SPIRIT** — range cleared the bar without proving the named official-action mechanism. **A successor owes a preregistered SHAPE leg.** Registered instrument = `usdjpy.py` hourly-derived intraday **RANGE**, **≥2.5-yen bar** — ⛔ **not a ≥160 level count; no such count exists on this desk.** Basis blockquote: § KEY THRESHOLDS (canonical home).

Calibration residue: **naming a risk and underweighting it is distinct from missing it.** As-made audit dispositioned 9/10 (one scoring vintage moved, SAM-07 75%→48%; scoreboard unchanged) → `audits/2026-09-10_asmade-disposition.md`. Full post-mortems → `thesis/PREDICTIONS_ARCHIVE.md`.

---

Thesis v1.7 → `thesis/THESIS.md`; audit → `thesis/CHANGELOG.md`; cross-agent synthesis → `NEXUS_BRIEF.md`. No successor declared.
