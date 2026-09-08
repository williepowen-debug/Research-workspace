# HAWK Predictions — Calibration Archive

Full post-mortems for **closed** predictions (CONFIRMED / FAILED / PARTIALLY / VOIDED). Reference-only — **NOT loaded at boot**. The live record (date, confidence, status, outcome) stays in [`PREDICTIONS.tsv`](PREDICTIONS.tsv); the one-line calibration warnings live in that file's scoreboard preamble. This file holds the blow-by-blow.

Created 2026-06-26 as part of the SAM thesis-bundle model adoption (predictions relocated `workbook/` → `thesis/`). Each section = one Pred_ID (anchor `#hawk-NN`); text is the verbatim Outcome + Notes from PREDICTIONS.tsv at time of relocation.

---

## HAW-01
**US strikes Iranian nuclear facilities before end Q1 2026** | made 2026-02-18 | conf 25% | Q1 2026 | CONFIRMED 2026-02-28 | Operation Epic Fury launched

Originally HAWK-01.

---

## HAW-02
**Iran retaliates by disrupting Hormuz within 72h of US strike** | made 2026-02-18 | conf 60% | Conditional | CONFIRMED 2026-03-03 | Hormuz closed, fire-upon warning

Originally HAWK-02.

---

## HAW-03
**No US military intervention in Venezuela in 2026** | made 2026-02-18 | conf 95% | 2026 | FAILED 2026-06-20 | FALSE

Outcome: US ran Operation Absolute Resolve Jan 3 2026 - captured Maduro in Caracas (>150 aircraft; cyber+airstrike+ground raid), preceded by Dec-17-2025 naval blockade of sanctioned tankers. Both invalidation conditions met ~5.5mo before resolution. Verified A1 (CNN live/NBC/AlJazeera/CBS/UK-HoC-Library Jun 20).

Notes: Resolved Jun 20 2026 (event Jan 3). STATUS + VX-HAWK-VEN-01 carried "rhetoric only" ~5.5mo stale - dormant secondary vector never re-swept while Iran absorbed bandwidth (see LESSONS). Now post-intervention NORMALIZATION: sanctions lifted on acting-pres Delcy Rodriguez (Apr), oil sector reopened to US firms, dark-fleet blockade still enforced. KB-HAWK-194. **Lesson: re-sweep dormant secondary vectors; a 95%-conf prediction failed because the disconfirming event had already happened unobserved.**

---

## HAW-04
**Scenario B (sustained campaign) is base case through Q2** | made 2026-03-01 | conf 55% | Q2 2026 | FAILED 2026-04-20 | Scenario D became base case (75% by Apr 20) as Phase 3 infrastructure campaign and Hormuz reclosure confirmed C→D transition

Notes: REASSESSED Mar 6→Apr 20: B base case broke by Apr 1 as Qatar FM, ADCOP fire, storage crisis confirmed Scenario D path. **Lesson: scenario-base-case calls can be outrun by a faster infra-campaign escalation.**

---

## HAW-05
**Hezbollah stays dormant (no mass activation)** | made 2026-03-01 | conf 65% | Conditional | PARTIALLY 2026-04-20 | Hezbollah active at reduced scale (Lebanon front, attacks reduced post-ceasefire) but did not achieve "mass activation" threshold through Apr 20

Notes: Araghchi demanded Lebanon in any deal; reactivation risk remains as ceasefire deadline approaches.

---

## HAW-06
**Ceasefire lapses Apr 21 8pm without extension (Scenario D trigger)** | made 2026-04-20 | conf 70% | Apr 21-22 2026 | FAILED 2026-04-21 | Trump extended ceasefire indefinitely Apr 21 at Munir/Sharif request citing 'fractured Iranian government'; Vance Islamabad trip postponed but no lapse occurred. Sources: NPR/Axios/CBS Apr 21 2026.

Notes: **CALIBRATION ANCHOR (Jun 8): pattern is conflict produces armed pauses (deferral dynamic on ally request), not clean breaks.** Lesson informs Jun 8 D-scenario held-flat justification; see KB-HAWK-162.

---

## HAW-07
**Brent closes >$105 within 5 sessions if ceasefire lapses without extension** | made 2026-04-20 | conf 65% | Apr 22-26 2026 | VOIDED 2026-04-21 | Premise (Apr 21 8pm lapse) failed — HAW-06 FAILED. Conditional prediction voided. Note: Brent did hit $109.96 Apr 28 / $113.99 Apr 29 within 5-6 sessions for unrelated reasons (Phase 3 facility targeting + blockade enforcement), NOT the failed-lapse mechanism. No credit for right-for-wrong-reasons.

Notes: **Calibration: VOIDED is the correct disposition for conditional predictions whose premise fails; CONFIRMED would over-credit incidental directional accuracy.** Defer Brent levels to BRENT.

---

## HAW-08
**Iran executes retaliatory kinetic action for Apr 19 US ship seizure within 7 days** | made 2026-04-20 | conf 55% | Apr 19-26 2026 | CONFIRMED 2026-04-22 | Iran launched attack drones at US ships in the window (no damage reported); Apr 22 Iran navy seized 2 container ships in Hormuz under "maritime violations" pretext. Drones-at-US-ships satisfies direct-kinetic-on-US-asset rubric regardless of intercept outcome. Sources: NBC/CNN/Al Jazeera/CNBC Apr 19-22 2026.

Notes: **Resolution rubric set BEFORE evidence search (per director Jun 8): direct kinetic on US asset = CONFIRMED, proxy/asymmetric only = PARTIALLY, gunboat/diplomatic only = FAILED.** Drones-at-US-ships = direct kinetic execution; intercept/no-damage caveat noted but rubric is action-based not outcome-based.

---

## HAW-09
**Iran returns to Pakistan-mediated talks (mechanism) by Jun 15 (threshold). Walkback / partial-MOU-confirm.** | made 2026-06-08 | conf 35% | Jun 1-15 2026 | CONFIRMED 2026-06-13 | TRUE

Outcome: CONFIRMED. Mechanism FIRED + threshold MET, both inside window. Iran re-engaged the Pakistan/Qatar channel after the Jun 1 walk; Sharif claimed "final, agreed-upon text" Jun 12 (both sides agreed MOU text, awaiting final approval) = exactly the "partial-MOU-confirm" specified — signature is B's bar, not this prediction's. Corroborated by Trump Jun 11 strike-cancel ("final contours approved") + Araghchi "never been closer" Jun 13; external/independent (multi-outlet). CONTAMINATION CAVEAT (KB-178): director CONFIRMED-lean was in the pasted Jun 12 packet despite DO-NOT-TRANSCRIBE — not gradable as fully independent, but public record forces CONFIRMED regardless of key; landed DIFFERENTLY on HAW-10 (not echoing). CAVEAT NEUTRALIZED for this call (Jun 13): advisor "Orc" independently derived CONFIRMED from primary news without the pasted lean — second independent path, same disposition. Logged KB-HAWK-179.

Notes: Date_Made Jun 8 (today; per director). Window Jun 1-15 = observation window since Iran walk Jun 1 (KB-HAWK-156); BRT-27 mirrors this date. Mechanism + threshold separable per [[finding_threshold_vs_mechanism]]. Deferral-dynamic favors muddle not clean return. Calibration learning from HAW-06 informs lower confidence (was 45% draft). **Lesson: pre-registered mechanism+threshold + 2nd-independent-path neutralizes a contamination caveat.**

---

## HAW-10
**Houthi commercial-vessel kinetic attack (mechanism) on Bab al-Mandab (threshold) by Jul 1.** | made 2026-06-08 | conf 25% | Jun 1 - Jul 1 2026 | FAILED 2026-07-08 | No Bab-al-Mandab-PROPER commercial-vessel strike occurred by window close Jul 1 (mechanism fired Gulf-of-Aden 6/8-9 only; locus stayed unmet through a 7/8 gap-sweep — no July reporting found). Registered-text locus rubric applies per LESSONS.md wording-wedge discipline: FAILED, not CONFIRMED-on-mechanism.

Notes: Date_Made Jun 8. Houthi quiet through 2026 to date (no commercial-vessel attacks per WashInstitute/MARAD); Iran rhetorical-only Jun 1 ("activate" threat). BRT-28 mirrors this date. Promotion of Bab al-Mandab from emerging to core convergence vector on confirm. | Jun 18 check: no Bab-al-Mandab-PROPER strike since the 6/8-9 Gulf-of-Aden mechanism-fire; registered locus still unmet; held to window close Jul 1. | Resolved 7/8 (8 days stale at resolution — flag for boot predictions-scan discipline): FAILED, locus never met. **Lesson: prediction and promotion-threshold text must be written identically — same class as HAW-10's own LESSONS.md entry 1 (locus wording wedge).** `[backfilled-at-split 2026-07-12 — mechanical; source LESSONS.md #1 for the wording-wedge discipline]`

---

## HAW-11
**Defense intercept failure (mechanism) produces Gulf energy infrastructure hit Aramco/ADCOP/Yanbu/Fujairah/Barakah-redux class (threshold) before Jun 22.** | made 2026-06-08 | conf 20% | Jun 8-22 2026 | FAILED 2026-06-22 | FALSE

Outcome: NO Gulf energy-infra hit occurred Jun 13-22; the Jun-20 declaratory Hormuz re-closure was NOT an infra hit. Kill-switch did NOT fire = DECOUPLING THESIS REINFORCED (per the prediction's own framing: HAW-11 expiry -> decoupling reinforced). Resolved at window close.

Notes: Date_Made Jun 8. **THESIS KILL-SWITCH for decoupling/salvo-regime read (FLOW-HAWK-19).** If HAW-11 fires: channel was dormant not muted; market was complacent. If HAW-11 expires: decoupling thesis reinforced. Calibration-load-bearing. | Jun 18 check: no Gulf energy-infra hit Jun 13-18; ceasefire SIGNED Jun 17 makes a hit in the final 4 days low-prob — trending toward EXPIRE (decoupling reinforced). Resolve at window close Jun 22. | Jun 19 sub-agent sweep: still NO Gulf energy-infra hit (last realized Mar-Apr); Kharg threat-only (cancelled Jun 11). EXPIRE path firm. | Jun 20 PM: Iran re-declared Hormuz closed (declaratory, NOT an energy-infra hit) - EXPIRE-leaning holds but re-closure+'first step' raise final-2-day tail-risk. KB-200. **Lesson: the named kill-switch expiring is itself the strongest confirming datum for the decoupling thesis — a declaratory chokepoint re-closure with no infra hit + no Brent spike.**

---

## HAW-12
**First US-Iran (Switzerland/Vance) negotiating round reconvenes with a confirmed date or is held by Jul 3** | made 2026-06-19 | conf 55% | Jun 19 - Jul 3 2026 | CONFIRMED 2026-06-22 | Switzerland/Vance round WAS held and concluded ~Jun 22 with US and Iran reporting a "roadmap towards final deal" (Al Jazeera/NBC 6/22) — well inside the Jun19-Jul3 window. CONFIRMED at 55% stated confidence.

Notes: Diplomatic sub-gate = B-vs-C discriminator. First round postponed->called off 6/18-19 over Lebanon; "direct meeting in coming days" is mediator-sourced (low-conf timing, KB-193). Lebanon trigger defused 6/19. | Resolved 7/8 (16 days stale at resolution — flag for boot predictions-scan discipline): CONFIRMED. Diplomatic-track sub-gate cleared even as the physical/liner gates (HAW-13) failed — negotiation and verification decoupled, per the "implementation ahead of negotiation" reversed to "negotiation ahead of physical-verification" frame by early July. `[backfilled-at-split 2026-07-12 — mechanical; deeper post-mortem = HAWK owner-lane, pointer: STRIKES SUMMARY/7-12 commit trail]`

---

## HAW-13
**At least ONE harder Hormuz verification gate clears by Jul 4: liner majors (Maersk/MSC/CMA-CGM/Hapag) resume Hormuz transit OR JWC lifts/steps-down listed-area JWLA-033** | made 2026-06-19 | conf 45% | Jun 19 - Jul 4 2026 | FAILED 2026-07-04 | Institutional Hormuz reopening scorecard 0/4, STALLED and partially REVERSED post-6/27, per DEWEY deep-research deliverable (WALTER SIG-W-20260702-002, explicitly framed as resolving HAW-13). Neither liner-majors nor JWLA-033 step-down cleared by Jul 4.

Notes: Physical gate already partially clearing (dark transits); this requires a HARDER gate (liner OR insurance). Sub-agent Jun 19: "wont normalize for months" (KB-192). Tests announced->verified. | Jun 20 PM: Hormuz RE-CLOSURE (KB-200) reverses any gate progress -> toward_fail HARDER; a gate clearing by Jul 4 now needs the closure to dissolve first. | Resolved 7/8 (4 days stale at resolution): FAILED per DEWEY 7/2 scorecard. Successor gate proposed by WALTER: JWC formal JWLA-033 de-listing + OFAC FAQ 1249 relief, both necessary — not yet registered as a new HAW-xx. `[backfilled-at-split 2026-07-12 — mechanical; deeper post-mortem = HAWK owner-lane]`

---

## HAW-14
**[RE-SCOPED 7/12 Will-directed] Iran does NOT execute direct kinetic retaliation against Israeli or US assets (ANY catalyst) within 30 days** | made 2026-06-19 | conf 70% | Jun 19 - Jul 19 2026 | FAILED 2026-07-12 | RE-SCOPED in-window 7/12 (Will-directed) from Lebanon-locus to catalyst-agnostic wording. FAILED: the direct-kinetic-on-US-assets floor breached 4x via NON-Lebanon catalysts — IRGC struck US bases in Bahrain+Kuwait 6/28 and 7/8, 8 missiles at a US base in Jordan 7/9, and the broadest 6-Gulf-state retaliation (Qatar/UAE/Bahrain/Kuwait +claimed Jordan/Oman) 7/12. Original Lebanon-locus wording would have closed CONFIRMED 7/19 = calibration artifact (literal clause holds while realized risk is far worse). Breaks strict pre-registration (floor already breached at re-scope time) — documented as Will-directed, not rubric drift.

Notes: THE D-trigger-stays-unfired prediction (30d window per Will). Bear: Israel structural incentive to keep Lebanon hot (Netanyahu-sabotage intel KB-191) + Iran made Lebanon a precondition. Bull/base rate: this war = threat + reduced-scale not full retaliation; Trump/US pressuring Israel = stabilizer. | Jun 20 PM: REVISED OFF toward_confirm. Iran acted on the resume-threat via the COERCIVE Hormuz lever ('first step', KB-200) - threshold (direct kinetic on Israel/US) still UNMET so prediction intact, but escalation ladder now engaged just below the kinetic line; a 'second step' going kinetic = FAIL path. Neutral. | **Jun 28: kinetic floor BREACHED (2nd time) but via a DIFFERENT catalyst chain than Lebanon** — IRGC struck US bases Kuwait+Bahrain 6/28 in response to the tanker-strike/US-strike chain, not the Lebanon issue named in this prediction's text. Literal Lebanon-path threshold stayed technically unmet; standing note flagged "re-examine/re-word at next closeout, do not silently carry as OPEN-clean." | **Jul 8: SAME pattern fires a 3rd time** — Iran claims an 85-site strike on US assets in Bahrain+Kuwait, again triggered by the tanker-attack/US-strike chain, again NOT the Lebanon issue. The named mechanism (direct Iranian kinetic on Israel/US assets) has now fired via a non-Lebanon catalyst on 6/28 AND 7/8 while the specific Lebanon-path clause remains formally unmet. Left OPEN on strict registered wording (window still runs to Jul 19; no Lebanon-triggered strike has occurred), but the prediction as originally scoped materially UNDERSTATES realized risk — the underlying "Iran direct-kinetic-on-US/Israel-assets" floor is not holding, it has broken twice on adjacent catalysts. Do not read OPEN as "quiet." Recommend Will/next-closeout re-scope to catalyst-agnostic wording per [[feedback_forward_discovery_prediction_spirit]]. | RESOLVED 7/12 FAILED (re-scoped): a locus-clause on a broad-mechanism risk understates realized risk — write the mechanism, not the trigger. Post-mortem owed -> PREDICTIONS_ARCHIVE.md#hawk-14. `[backfilled-at-split 2026-07-12 — mechanical; deeper post-mortem trail = SCRATCH.md 7/12 + LESSONS.md entry 4, HAWK owner-lane]`

---

## HAW-15
**Ukraine does NOT strike Russian CRUDE-export infrastructure (Baltic terminals Primorsk/Ust-Luga, Novorossiysk, or Druzhba pipeline) by Jul 15** | made 2026-06-19 | conf 65% | Jun 19 - Jul 15 2026 | FAILED 2026-07-12 | FAILED. CORRECTED after a Will-directed comprehensive sweep (my earlier 7/12 'trending CONFIRMED, terminals unstruck' was a research miss on a stale/gappy ledger). Ukraine DID strike Russian crude-export infrastructure IN-WINDOW: Primorsk (named Baltic crude terminal - fuel reservoir hit + leak ~6/25, Drozdenko pipeline->reservoir clarification, corroborated 4 outlets, OSINT loading-terminal damage) + NOVATEK-Ust-Luga oil/condensate export complex (processing+exports SUSPENDED 7/10) + Vysotsk Baltic oil port (7/6) + Port Kavkaz (6/20) + the 7/4 St-Petersburg 'Baltic oil gateway' op. PLUS the channel was never dormant (Novorossiysk/Sheskharis crude terminal re-hit 5/23+6/8, both pre-window, both missed in my ledger). MARKET NUANCE for BRENT: in-window terminal damage LIMITED/fast-repair so far (Primorsk shrapnel not berths; Ust-Luga=condensate not crude; Vysotsk/Kavkaz=products) -> flip-trigger #2 FIRED but crude exports NOT yet degraded (2026-highs mid-June) -> the valve is being shot at, not yet closed.

Notes: Brent flip-trigger #2 (SUMMARY.md): targeting refinery-only since Apr = product/crack not crude. If FAILED (pivot occurs), story moves from cracks to Brent/crude. Decision-relevant for BRENT. | Jul 12 check: products/refinery campaign continues; NO confirmed in-window CRUDE-export strike (Primorsk/Novorossiysk hits surfaced this session are April-dated, predate the Jun19-Jul15 window). Row technically unmet. DUE a final check before the Jul 15 window close. | Jul 12 TIGHTER CONFIRMATION (Will-directed): the 4 NAMED crude-export installations were NOT struck in-window — Primorsk/Ust-Luga = March-only; Novorossiysk/Sheskharis = Apr 6 + May 23 (both pre-window); Druzhba = Jan-Apr dispute, resolved 4/23. The HOT July campaign is shadow-fleet TANKERS (Azov/Black Sea, incl. crude tankers 'the Blue' + a suezmax off Novorossiysk) + a Rostov marine LOADING terminal + oil depots — a DIFFERENT channel, NOT the named crude-export hubs. Trending CONFIRMED-on-the-letter (the refineries->crude-export-TERMINAL pivot did NOT fire). HOLD OPEN to the Jul 15 window close: a named-terminal strike in the next 3 days flips it, and confirm the exact 'terminals' wording of the 7/9 Ukraine GS readout ('refinery, terminals, 18 vessels') at resolution. NOT re-scoped like HAW-14 (there the named event fired + only the locus was wrong; here the named event genuinely didn't fire) — the new tanker channel is captured forward in HAW-17. | RESOLVED 7/12 FAILED (Will-directed correction of my own same-day CONFIRMED-lean). Load-bearing lesson: my internal ledger was stale (6/20) AND had missed the 5/23+6/8 Novorossiysk re-strikes, so it under-baselined the crude channel; and a single-search-per-terminal sweep returned only Mar/Apr headlines. See KB-222/223 + LESSONS 2026-07-12. Post-mortem -> PREDICTIONS_ARCHIVE.md#hawk-15. `[backfilled-at-split 2026-07-12 — mechanical; deeper post-mortem trail = LESSONS.md entry 4 + OSPREY's founding calibration lesson, see AGENTS/OSPREY/LESSONS.md]`

---

## HAW-21

**Canadian counter-tariff entry into force** | made 2026-09-02 | registered confidence 65% | resolve-by 2026-09-15 | **CONFIRMED 2026-09-08**.

The registered letter expressly permits a Finance/CBSA notice stating the measure is in effect. On September8, the two September4 made orders P.C.2026-0785/0786 and the primary-indexed September7 CBSA26-23 paragraph4 met that limb. Independent Finance/order extraction matched all629 commodity items and rates:21 at15%,195 at25%,413 at50%, no mismatches. Dated Finance/Gazette/CBSA search attempts satisfy the search requirement. Full source trail and limits: [owner adjudication](2026-09-08_HAW-21_ADJUDICATION.md).

Calibration: the Canadian default required an affirmative legal act; that act appeared. This single confirmation does not validate importing its65% base rate into US section338 or the November10 suspension-expiry case. Brier contribution at the unchanged registered probability is0.1225. SOR registration identifiers/dates remain UNKNOWN; commencement is inferred from the combined permitted operative evidence. No tariff revenue, effective importer liability or employment loss follows from a commodity match. Importer remission/exceptions remain material. September9/11 documentary reconciliation is retained. Original letter and historical ledger rows are unchanged.
