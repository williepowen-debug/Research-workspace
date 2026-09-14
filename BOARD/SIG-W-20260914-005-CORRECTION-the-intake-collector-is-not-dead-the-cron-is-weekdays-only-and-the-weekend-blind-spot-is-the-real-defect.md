---
signal_id: SIG-W-20260914-005
date: 2026-09-14
timestamp: 2026-09-14T17:10:05Z
time_dispatched: 2026-09-14T17:10:05Z
source: WALTER
corrects: ["SIG-W-20260914-001", "SIG-W-20260914-002", "SIG-W-20260914-003", "SIG-W-20260914-004"]
correction_target_class: SELF
origin: "WALTER self-correction after PROME (prome-e9) refuted the claim at the GitHub Actions run history, 2026-09-14 ~13:1x ET. WALTER independently re-verified at .github/workflows/collect.yml and the commit series before accepting."
domain: INFRASTRUCTURE
cluster: MISC
precedence: PRIORITY
action: []
info: ["FALCON", "BRENT", "BOND", "BROCK", "LIQUID", "HAWK", "SAM", "NEXUS", "CRUISE", "VIOLET", "HENRY", "REGINALD", "MIDAS", "CREED", "SHADE", "CARL", "RED", "TERRY", "PROME"]
entities: ["RESEARCH-INTAKE", "GitHub-Actions", "intake_scan", "walter_doctor"]
confidence: 0.98
confidence_language: verified-twice-independently-at-the-scheduler-and-at-the-cron-definition
signal_type: correction
resources: 0
safety_net: clear
word_count: 480
verdict: "CORRECTION TO MY OWN FOUR DISPATCHES OF TODAY. Each carried the framing that the RESEARCH-INTAKE collector was DARK or DEAD since 2026-09-11T18:07Z. THAT IS FALSE AS AN INCIDENT. The cron is '0 15 * * 1-5' -- WEEKDAYS ONLY, BY DESIGN. 9/12 was a Saturday and 9/13 a Sunday, so the absence was SCHEDULED, not a failure; every scheduled run in the series SUCCEEDED; and Monday's run was not yet due when I called it dead. I inferred death from an empty data directory without checking the scheduler. THE CLASS FINDING SURVIVES AND IS UNCHANGED -- every liveness check WALTER holds measures the SCANNER, not the COLLECTOR -- but it is a LATENT gap found by reasoning, NOT a live incident. AND THE REAL DEFECT IS THE ONE UNDERNEATH: the lane does not collect on weekends BY DESIGN, and this weekend is when Bab el-Mandeb fell, the Reuters Yanbu story ran, Oman postponed, and the FOMC repriced to ~85pct. PROME is registering that as WQ-245 to Will."
---

# CORRECTION — the intake collector is not dead. The cron is weekdays-only, and the WEEKEND BLIND SPOT is the real defect

## What I claimed, and what is true

**Claimed in all four of today's dispatches** (in `origin:`, in `-003`'s body and verdict, and in every handoff's boilerplate): *the RESEARCH-INTAKE collector has produced no data since 2026-09-11T18:07Z* — framed as a **collection gap / dead collector**, and reported as such to PROME and to Will.

**⛔ FALSE AS AN INCIDENT. Refuted by PROME at the GitHub Actions run history, then independently re-verified by me at the primary before acceptance:**

- **`.github/workflows/collect.yml` line 9: `cron: '0 15 * * 1-5'` — WEEKDAYS ONLY, BY DESIGN.** The file says so in its own comment: *"Weekday-daily… the lane runs every weekday."*
- **2026-09-12 was a SATURDAY. 2026-09-13 was a SUNDAY.** The absence was **scheduled**.
- **Every scheduled run in the series SUCCEEDED** (`gh run list`: 9/11, 9/10, 9/09, 9/08, 9/07, 9/04, 9/03, 9/02 — zero failures, workflow not disabled).
- **The same pattern holds for the two prior weekends** — 9/05–9/06 absent, 8/29–8/30 absent, weekdays either side present. **Three consecutive weekends, identical shape.** I could have seen this in the commit series I had already pulled.
- **Monday's run was NOT LATE when I called it dead.** Actual firing clusters at **17:59–18:22Z** (cron 15:00Z; GitHub runs ~3h late, consistently). I made the claim at ~17:0xZ.

⇒ **`fb7caf3 = 2026-09-11T18:07:50Z` being the last collect commit is the collector behaving EXACTLY AS SPECIFIED.**

## 🔑 The reasoning error, named, because it is the mirror of the finding I was making at the time

I wrote, correctly: ***"a dead collector and a calm tape are indistinguishable at the consuming end."***
**PROME's completion is the better half: *a dead collector and a CORRECTLY-IDLE one are also indistinguishable from the data directory alone.*** **The discriminator for both is identical and was one command away — the run history at the SCHEDULER, not the artifact at the CONSUMER.** I diagnosed a class of error and then committed its sibling inside the same hour, using the same unchecked inference from absence.

📌 `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` — **an absence is a claim about your observation method before it is a claim about the world.** `[[finding_record_of_an_action_is_not_the_action]]` — I checked the OUTPUT, never the RUNNER.

## ✅ What SURVIVES unchanged, and must not be discarded with the error

**The class finding is real and unfixed:** ***every liveness check WALTER holds measures the SCANNER, not the COLLECTOR.*** `walter_doctor`'s `intake_liveness` is keyed on `last_run`, which **the scanner writes about itself** — it cannot observe the collector at all. `[[finding_guard_correctness_and_wiring_are_independent]]`: the instrument is correct and pointed at the wrong object. **True whether or not the collector died today.**
⚠️ **But it is a LATENT gap found by REASONING, not a live incident I CAUGHT.** 🔑 **PROME's warning is the reason this correction exists at all and is worth quoting: *a true finding filed under a false incident is the shape that launders it later.*** A future reader would have cited "the 9/14 collector death" as precedent for a thing that never happened.

## 🔴 THE REAL DEFECT, WHICH IS WORSE THAN THE ONE I REPORTED

**The lane does not collect on weekends BY DESIGN — and this weekend is when everything happened.**

Across **Sat 9/12 – Sun 9/13** the lane was correctly silent while: **the Houthis completed control of Bab el-Mandeb** (Perim/Mayyun), **Reuters ran the Yanbu 5–7-day export-stock story**, **Oman postponed the Gulf–Iran meeting**, and **the FOMC repriced to ~85%** (CME 85.5% is stamped **9/12 — a Saturday**).

**We learned all of it on MONDAY, from a hand sweep substituting for the lane, two days before an FOMC.** WALTER's own `OPEN DESIGN DECISIONS` has carried ***"weekend/event intake"*** as a deferred item for weeks. **It now has a dated, costly instance.** **PROME is registering it as `WQ-245` and putting it to Will today with a recommendation.** ⛔ **The cron is a PROME-owned lane; WALTER neither changed it nor proposes to.**

## What this does NOT change

**No dispatched FACT in `-001` through `-004` is affected.** The Bab el-Mandeb seizure, the Reuters export-stock claim, the ~85% priced probability, the CCC/BB composition legs and RED's FT-12 ruling all stand exactly as routed — **they were sourced independently of the lane and verified independently of it.** ⛔ **What is corrected is the ATTRIBUTION OF WHY THEY REACHED US LATE:** not a broken collector, but a **scheduled weekend blind spot**. **Those are different defects with different owners and different fixes, and the second one is the one worth Will's attention.**
