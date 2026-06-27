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

## HAW-11
**Defense intercept failure (mechanism) produces Gulf energy infrastructure hit Aramco/ADCOP/Yanbu/Fujairah/Barakah-redux class (threshold) before Jun 22.** | made 2026-06-08 | conf 20% | Jun 8-22 2026 | FAILED 2026-06-22 | FALSE

Outcome: NO Gulf energy-infra hit occurred Jun 13-22; the Jun-20 declaratory Hormuz re-closure was NOT an infra hit. Kill-switch did NOT fire = DECOUPLING THESIS REINFORCED (per the prediction's own framing: HAW-11 expiry -> decoupling reinforced). Resolved at window close.

Notes: Date_Made Jun 8. **THESIS KILL-SWITCH for decoupling/salvo-regime read (FLOW-HAWK-19).** If HAW-11 fires: channel was dormant not muted; market was complacent. If HAW-11 expires: decoupling thesis reinforced. Calibration-load-bearing. | Jun 18 check: no Gulf energy-infra hit Jun 13-18; ceasefire SIGNED Jun 17 makes a hit in the final 4 days low-prob — trending toward EXPIRE (decoupling reinforced). Resolve at window close Jun 22. | Jun 19 sub-agent sweep: still NO Gulf energy-infra hit (last realized Mar-Apr); Kharg threat-only (cancelled Jun 11). EXPIRE path firm. | Jun 20 PM: Iran re-declared Hormuz closed (declaratory, NOT an energy-infra hit) - EXPIRE-leaning holds but re-closure+'first step' raise final-2-day tail-risk. KB-200. **Lesson: the named kill-switch expiring is itself the strongest confirming datum for the decoupling thesis — a declaratory chokepoint re-closure with no infra hit + no Brent spike.**
