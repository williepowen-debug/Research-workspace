# FALCON SCRATCH — 2026-07-30 Thu **CLOSED** (Will-requested boot + news integration → a marks session AND a correction session)

**Purpose:** Ephemeral session handoff — read at boot (step 2), rewritten at closeout (step 13). Durable learnings → `MEMORY.md`; cross-agent twin → `NEXUS_BRIEF.md`.

---

## CURRENT MARKS (one line)
- Scenario **B 5 / C 35 / D 60** · Convergence **43/50** (**P 23/25 · K 15/20 · R 13/20** — 🔴 **R1 and R2 have LEFT THE FLOOR**; only R3 remains at 1) · Kinetic **US-Iran RESUMED (heavy wave 7/29)** / Iran launching **daily** / **FIRST FATALITY 7/30 (Kuwait)** · **FAL-03 FAILED, FAL-04 OPEN @ 62% closes Aug 20** · Scoreboard **1C / 2F / 1 OPEN**.
- **⚠️ UNLIKE 7/27, THE NUMBERS DID MOVE.** Do not carry forward any 7/27 mark.

## CHANGES SINCE LAST SESSION (7/29 → 7/30)

### 🔴 THE HEADLINE IS NOT THE WAR NEWS — IT IS THAT MY OWN KILL-SWITCH WAS ALREADY TRIPPED WHEN I WROTE IT
- **FAL-03 RESOLVED FAILED on day 4 of a 21-day window**, on two routes with completely different characters:
  - **(b) JAZAN** — Aramco **SHUT** the 400 kbpd refinery **7/27**, restart tentatively **8/15** [Reuters citing IIR 7/28]. Genuine in-window development, a real miss. ⚠️ Only 4 days elapsed; the ≥7d leg **realizes 8/3**.
  - **(a) RAS LAFFAN** — QatarEnergy **force majeure on LNG live since 2026-03-24**, ~12.8 Mtpa ≈ **17% of Qatar's export capacity**, **3-5 YEAR** repair, extended to **Asian** buyers 7/28. **ALREADY TRUE AT REGISTRATION.**
- **⇒ FAL-03 could never have resolved CONFIRMED. I published an already-tripped kill-switch as OPEN and kept exporting the thesis it guarded. A RESEARCH failure, not a calibration failure — the 58% was never a real number.**
- **Root cause 1 — I asserted an unchecked negative.** My own published R2: *"None current (Bapco + Ras Laffan were March)."* I knew the strike; **I treated a March EVENT as a closed STATE and never asked whether the FM had been LIFTED.** An event has a date; **a force majeure has a DURATION.**
- **Root cause 2 (the generalizable one) — I WIDENED THE SCOPE AND KEPT A NARROW INSTRUMENT.** The 58% was derived off `STRIKES.tsv`, an **oil-complex STRIKE ledger** that structurally cannot see an **LNG force majeure**. The "ZERO across 109 days" was an artifact of the instrument's blind spot. **Forward rule adopted + auto-memory written.**
- **Fifth wording-wedge instance:** HAW-10 locus → HAW-14 catalyst → HAW-15 mechanism → FAL-01 actor → **FAL-03 MOLECULE + EVENT-vs-STATE.**
- **No rescue attempted** — a crude-only reading and a "newly declared" reading were both available and **both refused as unregistered.** Mirror of FAL-01, where I refused an unregistered *output-loss* requirement. **The discipline has to cut both ways.**

### 🎯 THESIS CORRECTED — it is MOLECULE-SPLIT, and that is now the export
- **CRUDE ✅ premium regime HOLDS** (zero confirmed crude barrels offline · Petroline **operational**, ~5 mb/d available · Yanbu loading ~3.3 mb/d · **Brent $90.21 / WTI $84.45** own pull 7/30, ~10% *below* the 7/23 $100.69 peak *through* a heavy strike wave and a shut refinery).
- **GAS/LNG 🔴 supply-loss since MARCH** · **REFINED PRODUCT 🔴 supply-loss since 7/27.**
- **Fleet phrasing fix ADOPTED (HAWK's): "zero confirmed *CRUDE* barrels offline."** Propagated to STATUS, NEXUS_BRIEF, THESIS.md, TIMELINE.md.

### 🔥 THE WAR RESUMED
- **7/28** Iran broke the pause — IRGC ballistics at a US base in **Jordan**, intercepted. **7/29 overnight** US **and Saudi** struck Tehran-backed sites in **Iraq**. **7/29 ~22:00 ET** CENTCOM **"heavy wave," DOZENS of IRGC targets**; 3 civilians killed at Qeshm. **7/30** Jordan intercepts five more; **KUWAIT struck, one worker killed — FIRST FATALITY OF THE EXCHANGE.**
- **🔑 The TARGET SET is the finding, not the tempo:** *"military command centers, missile and drone facilities, coastal surveillance and defense sites, and maritime capabilities."* **The energy complex has now been spared across the RESUMPTION as well as the original 13 nights** — the load-bearing input to FAL-04's 62%. ⚠️ Cuts both ways on Hormuz: striking the *enforcement apparatus* aims at **reopening** the strait.
- **Diplomacy did NOT collapse** — Iran hosted Hormuz calls with **Saudi + Oman** 7/28; Trump "good talks." **I HELD the Diplomacy vector at 3 deliberately: my registered threshold needs "talks collapse AND strikes resume" and only ONE leg fired.**

### ✅ THINGS THAT CLOSED CLEANLY
- **GATE-FALCON-001 leg-3: the 7/29 flagged basis risk is RESOLVED, not just flagged.** AGBI 7/28 pins *"Red Sea exports averaged 4.7 million bpd"* Mar-Jun = **TOTAL LIQUIDS**. The alarming **−42.6% "crude-only"** read was crude-2.7 vs a **total-liquids** 4.7 — apples-to-oranges. Correctly scaled ≈ **−32%**. **All bases land −23% to −32%, under the frozen −36% bar. NOT FIRED, verified.** (`KB-FALCON-066`)
- **HAWK's boot.py refutation ACCEPTED** — my *"last touched 7/9 so live"* inference was wrong; **the mtime was the FREEZE commit.** Same family as `[[finding_mtime_is_corrupted_by_git_sync]]`.
- **War-risk re-pull (my own 7-day boot gate fired on schedule): NO NEWER PRIMARY EXISTS.** Hormuz stays **7.5-10%** [Marsh/Platts 7/22]. **Did NOT advance the data clock** — added a third `Last re-pull ATTEMPTED` clock instead, because *"old because nothing newer was published"* ≠ *"old because nobody looked."*

### 🧹 SELF-DIRECTED STALENESS SWEEP (Will: *"take care of ourselves first before we send messages outward"*) — 15 defects closed
**The sweep found more than the news did, and one finding was sitting in my own boot instructions.**
- **🔴 A HARDCODED THRESHOLD THAT FAILS FALSE-NEGATIVE — the worst class found.** The bypass collapse floor is **30% of a rolling 60-day mean** and had drifted **15,684 → 16,224 → 20,105 (+28% in 14 days)**, while `THESIS.md`, `TIMELINE.md`, `BYPASS_INTEGRITY_BASELINE.md` **and `CLAUDE.md` boot step 5b-3** all carried it as a constant. **A stale LOW floor is the dangerous direction: throughput of ~18,000 reads *above* the stale 15,684 (no alarm) and *below* the true 20,105 (alarm) — the gauge stays silent through a real collapse.** All four de-hardcoded. *(Throughput itself rose ~43% to 100,068 t/d — the bypass is absorbing MORE, which is the strongest quantitative statement of the crude thesis this repo holds.)*
- **🔴 `VX.tsv` HAD LOGGED NOTHING SINCE 7/23** — through a 13-night campaign, a pause, a break and a resumption. 7 vectors refreshed; **the Kuwait fatality was in no vector at all.** ISR-01 given a **VERIFIED-DORMANT** stamp — *"no update"* and *"checked, unchanged"* are indistinguishable in a `Last_Updated` column.
- **🔴 `VX-FALCON-GASLNG-01` CREATED — the first FALCON-originated vector, and its ABSENCE was the failure.** Every inherited vector tracks **kinetic events against oil**, so a 4-month LNG force majeure had no row, no threshold, no staleness affordance. **It was unrepresentable, not merely unnoticed.**
- **🔴 `FLOW.tsv` untouched since spinout; every pathway ran through oil price or a chokepoint.** Added `FLOW-FALCON-01` (LNG → FM → Asian/European winter inventory) and `FLOW-FALCON-02` (**refinery outage → PRODUCT cracks — crude-BEARISH**, the sign-flip channel).
- **🔴 `LESSONS.md` had ZERO FALCON-authored items after 18 days and TWO failed predictions.** Added 3. **A post-mortem is not a lesson until it lives where boot step 3 reads it** — `PREDICTIONS.tsv` Outcome fields are not read at boot.
- **🔴 `EXIT_PROTOCOL.md` REWRITTEN — it was March-vintage throughout, not just mis-numbered.** The 7/27 banner flagged an orphaned "Scenario A"; on reading, the rail gated thesis-exit on **Fujairah repairs** and **ADNOC cold-restart** (neither live) with a D-watch list of **Kent letter / PSAB / Jebel Ali**. **Its own dated trigger ("when FAL-03 resolves") fired, so the banner is DISCHARGED, not re-stamped.** Thesis-kill is now **0/7 and MOLECULE-SCOPED**.
- **🔴 `THESIS.md` v2.0 → v2.1** — header *and body*. v2.0's core sentence ("failed to take barrels off the market") was **false without a molecule qualifier and had been since March**; ⓶ was labelled **DORMANT** while already fired; R was stated as 8/20 with "R1-R3 all at the floor."
- **`CLAUDE.md` FILES table was describing SPINOUT state, not current state** — 8 rows (STRIKES "4 rows, backfill owed" → 31 rows swept through 7/30; KB "0 rows" → 66; board_log "header only"; VX "7 rows"; FLOW "11 rows"). **A systematic class, not isolated typos.**
- Also: **`IRAQ_PMF_DISCRIMINATOR_REVIEW.md`** (12d stale, said *unfired* — it is now **firing on the actor axis**; and `baghdad_watch.py` printed QUIET on 7/30, **three days after Iraq-launched drones hit Abqaiq** = live proof of its own dead-channel finding) · **`PREDICTIONS_ARCHIVE.md`** (FAL-01 + FAL-03 post-mortems, absent) · **`CHANGELOG.md`** (v2.1 entry; flagged that the header says *reverse* chronological while practice is ascending) · **`SOURCES.md`** (untouched since spinout — IIR, AGBI, LNG Prime, NASA FIRMS, CTP/ISW, PortWatch FeatureServer all missing) · **`MEMORY.md`** (4 durable findings) · **`ANALYSIS_2026-07-27.md`** + **`FAL-01_REREGISTRATION_SCAFFOLD.md`** bannered with **dated** regeneration triggers.

## WHAT I DID THIS SESSION
- Full day-by-day gap sweep 7/27→7/30 per LESSONS item 2, plus a **mechanism** sweep (LESSONS item 4) that is exactly what surfaced the Jazan shutdown and the Petroline status.
- **Verified WALTER's and HAWK's Ras Laffan claim independently before acting on it** — they are **ONE antecedent, not two** (`[[finding_shared_antecedent_independence_test]]`).
- Resolved FAL-03 FAILED with a full post-mortem; registered **FAL-04** with three named defects closed.
- Re-marked scenarios + convergence + the full P/K/R split; updated STRIKES.tsv (Jazan status + swept mark → 7/30), WARRISK.tsv, 6 KB rows, THESIS.md, TIMELINE.md.
- **Drained BOTH mail lanes** (6 WALTER + 2 root), 8 `board_log.tsv` rows, all `git mv`'d.
- Delivered **3 packets**: SAM (🔴 correction), BRENT (🔴 acute), PROME outbox (cc RED/HAWK/WALTER/NEXUS).

## NEXT SESSION (dated, future-verifiable)
1. **🔴 DOES JAZAN RESTART ON 8/15?** Now the highest-value number on the board — decides whether the product-side loss is a 19-day blip or a regime. **Also: on 8/3 the ≥7d duration realizes** regardless.
2. **🔴 Is 7/29 a one-off wave or a resumed NIGHTLY tempo?** D 60 vs 70 turns on exactly this. Check the strike-night count daily.
3. **🔴 A SECOND fatality — especially a US one.** The 7/30 Kuwait death crossed the casualty threshold; the ratchet is what follows. **This is the single most likely character-change trigger.**
4. **GATE-FALCON-001 leg-2** — TANKER-SPECIFIC **BAB** transits, ≥2 print-days sub-~8/day. ⚠️ **Do NOT fire it on Hormuz prints** (Hormuz tankers are now 2-4/day, but that is the wrong theater — `[[finding_theater_check_before_gate_check]]`).
5. **Leg-3 re-pull 8/1-2** for a 7DMA holding more post-strike days (the basis question is closed; only the freshness remains).
6. **War-risk re-pull again by 8/3** — treat 7.5-10% as a **FLOOR**, not a current read.
7. **RED's red-team on FAL-04's 62%** — I asked for it explicitly and framed the attack for them: *is crude-only scoping rigour, or a retreat to a claim I can win?* **Treat as a real test.**
8. **Ask SAM whether JKM/TTF actually repriced.** If Asian gas absorbed a 17% Qatari outage for four months **without** repricing, that **partially rescues the premium frame on the molecule I just conceded** — a genuinely two-way test I do not own.
9. ✅ **`workbook/EXIT_PROTOCOL.md` REWRITTEN 2026-07-30 — closed, not deferred a third time.** Its own trigger fired when FAL-03 resolved. Next rewrite trigger: **FAL-04 resolving / a 5th axis / a dated Oman framework / 2026-09-01.**
10. **`ANALYSIS_2026-07-27.md` REGENERATION — bannered 7/30 but NOT regenerated; still owed.** ⚠️ Nothing watches this file's staleness (boot 5c grades `STRIKES.tsv` only). **Dated trigger: the next session that adds or status-changes a STRIKES.tsv row, or 2026-08-06, whichever first.**
11. **`reports/` has NO retirement or staleness rule at all** (7 files, 7/12-7/29) — noticed during the sweep, not fixed. Root CLAUDE.md's >60-day archive rule would not bite for weeks, but there is no boot-time affordance either. Decide a rule or accept it explicitly.
12. **Re-review the Iraq/PMF discriminator** on any further Iraq-origin kinetic event, or by **2026-08-13**.

## OPEN THREADS / WATCHES
- 🔴 **Jazan restart 8/15** — the number that decides the product leg
- 🔴 **First fatality (Kuwait 7/30)** — the ratchet; watch for a second, and for any US casualty
- 🔴 **Two counter-moving wars AND two counter-moving molecules** in one file — the P/K/R split handles the first; the molecule split is now the second axis
- 🟠 **R3 is the last floor row standing** (no ≥72h suspension at a named terminal). R1 and R2 have gone. **R3 is effectively the whole surviving thesis.**
- 🟠 **Yanbu** — 92% of Saudi seaborne crude, defended by a **consumable** interceptor; **the Petroline is the undefendable route to the same objective** (claim-only, line operational as of 7/28)
- 🟠 **WC Saudi war-risk 0.1%** — the transit→origin falsifier, still the cheapest early warning of a crude-side P→R conversion
- 🟠 **Iraq/PMF firing on the ACTOR axis** — US+Saudi struck Iraq 7/29; watch for a *damaging* follow-on
- 🟡 **MRPL "avoid Hormuz AND Red Sea" tender precedent** — a buyer-side avoidance channel my hull-counting gauges structurally miss. WALTER's registered test: 2+ more Indian refiners within 3-4 weeks
- 🟡 **Magnitude gap unchanged** — no shuttle-run volume series exists anywhere
- 🟢 bypass **HOLDING** (100,068 t/d vs 20,105 floor, thru 7/24) · Hormuz **10/88** thru 7/23 · baghdad quiet · kharg 0 = **uninformative, not a strand**

## PREDICTIONS DUE / DECISIONS PENDING
- **FAL-04 OPEN, closes 2026-08-20.** Nothing due before then, but **the Jazan restart leg can move it any day**.
- **Will decision PENDING (soft):** the re-mark **B 5 / C 35 / D 60 + convergence 43/50** is applied as my own call. Cleanly revertible.
- **⚠️ Flagged for Will explicitly:** the FAL-03 failure is a research failure, not a calibration failure, and **the scoreboard line (1C/2F) understates it.** I would rather that be visible than tidy.

## MAIL STATE (one line per surface)
- **Inbox (root): DRAINED** (BRENT co-belligerency, HAWK legacy-scripts refutation) — both `acted`, `git mv`'d. **WALTER lane: DRAINED** — 6 signals (004, 006, 006-CORRECTION, 011, 013, 20260730-001), all logged and `git mv`'d. **8 board_log rows.**
- **Outbox:** `2026-07-30_to-PROME_fal03-failed-already-true-at-registration-remark.md` (🔴, cc RED/HAWK/WALTER/NEXUS).
- **Packets authored into others' inboxes (committed per carve-out ①):** → **SAM** (🔴 LNG correction — the heaviest read-through) · → **BRENT** (🔴 Jazan shut + molecule split + leg-3 basis closed).
- ⚠️ **Re-learned 7/27's lesson the easy way this time: checked mail at boot AND the lane was already loaded — SIG-W-20260730-001 had arrived 09:42 the same morning.**

## AUTO-MEMORY WRITTEN THIS SESSION (step 15 promotion scan)
- `finding_widened_scope_needs_rescoped_instrument` — widening a prediction's scope while keeping the old base-rate instrument can make it **already-failed at registration**, invisibly from inside the derivation

## PENDING PUSH / GIT
- All work committed path-scoped to `AGENTS/FALCON/` + two self-authored packets (SAM, BRENT) per carve-out ①. Orphan check run. **Spawned-mode? NO — live session, auto-push at closeout per protocol.**
