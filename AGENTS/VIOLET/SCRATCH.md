# VIOLET SCRATCH — September 4, 2026 (Fri ~13:1x ET — **third session of one day, spawned by Will to boot and check for crash residue. There was residue, and finding it was worth more than the session it recovered.**)

> **Scope as given (Will):** *"boot up. We had a crash so we may have some incomplete files ideas from the previous session. Please check."* Boot + crash diagnosis + recovery. No thesis bump, no proposal, no edits outside `AGENTS/VIOLET/`.
> **🔑 The session's shape: the crash had already been silently absorbed. Everything was committed, everything was pushed, and every automated check ran green over three handoff files that were 79 minutes stale. The recovery took twenty minutes; the reason nothing caught it is the finding.**

---

## THE CRASH — WHAT WAS ACTUALLY BROKEN

**Three VIOLET sessions ran on 9/4.** The second one died mid-write-back:

| Surface | Left at | State |
|---|---|---|
| `STATUS.md` | **10:06** (`ef3e0be9c`) | ✅ current — NFP grade landed |
| `SIGNAL_INTAKE.md` | **10:08** (`bc6017fd2`) | ✅ current — MOVE re-arm recorded |
| `SCRATCH.md` | 08:47 (`756bf3397`) | 🔴 **79 min stale** |
| `LAST_COMPLETION.md` | 08:47 (`756bf3397`) | 🔴 **79 min stale** |
| `NEXUS_BRIEF.md` | 08:47 (`756bf3397`) | 🔴 **79 min stale — Amendment 10 breach** |

- **Nothing was lost.** Both commits were complete and **already pushed** (origin 0/0 at boot). The NFP grading work, the card-defect finding, the news sweep — all on disk.
- **One half-done mechanical act:** `SIG-W-20260904-001` had its `board_log` disposition row written at 08:46 but the file was never `git mv`'d to `processed/`. Log said done, lane said pending. Completed this session.
- **What was actually damaged was the OUTBOUND state** — the three files that are read by someone who is not me.

## 🔑 WHY NOTHING CAUGHT IT — AND WHY THIS IS THE THIRD TIME

At this session's boot: `boot.py` **14/14 OK** · `ledger_staleness.py` **rc=0** · `corrections_boot_check.py` **rc=0** · `closeout_guard.py` red only on the pre-existing COT contract. **Four checks, all green, over a live breach of a rule this desk had already written down.**

**The rule was not missing.** `CLAUDE.md` write-back step 12 states NEXUS Amendment 10 in explicitly checkable form: *"the brief's commit timestamp ≥ the session's last STATUS commit timestamp."* **That is a comparison of two integers. It had been sitting there as a sentence for 31 days.**

⚠️ **Third instance in six weeks of this desk's own named class — a ritual is not a mechanism:**
| | Rule existed as | Cost |
|---|---|---|
| KB-VIO-165 | "validate enums against SCHEMA" | 11 rows violating, **one for 109 days** |
| KB-VIO-190/226 | a registered mechanical MOVE re-arm line | **3 sessions** booted past it |
| **KB-VIO-234** | an arithmetic comparison in step 12 | **31 days**, caught by a crash |

**And the timing bias is the part I had not seen before:** a tail step performed from memory fails *precisely when the session ends badly* — crash, interrupt, context exhaustion — **which is exactly the population where the handoff surfaces matter most.** A discipline that holds on every good day and breaks on every bad one is not a control. It is a control's shadow.

---

## WHAT I DID

1. **Booted clean and diagnosed the residue** — git-log timestamps on the four surfaces, not narrative. Confirmed 0 behind / 0 ahead, so nothing was unpushed.
2. **Executed WQ-177** (Will verbatim **"Okay approved" 11:11 ET**, packet landed 11:12 — *after* the crash). `TRADE.md` §LIVE DECISION FRAMEWORK: banner added, heading token **ARMED → RETIRED-SUPERSEDED**, body untouched. KB-VIO-113 → **SUPERSEDED**, KB-VIO-230 → **CONFIRMED/resolved**.
3. **Built `scripts/writeback_order_check.py`** and wired it **BLOCKING** into `closeout_guard.py`.
4. **Falsified it before trusting it.** Ran against the live *unfixed* repo state — fired on 3 of 3 lagging surfaces, rc=1. Then proved the **wiring separately** by running the guard and confirming the new contract appears in its RED list. Two independent properties, two tests.
5. **Completed the half-done WALTER consume** (`git mv` to `processed/`; lane now empty).
6. **KB-VIO-234 filed**; STATUS ⓪/⓪ᵇ + a gate row for the stood-down framework; the three handoff surfaces rewritten.
7. **DRAINED THE TOP-LEVEL INBOX LANE 7/7** (Will: *"ok do it"*) — every item dispositioned in `board_log.tsv` (`source=INBOX_ROOT`) and `git mv`'d to `processed/`. Both lanes now empty. **Three of the seven were live corrections to claims I had published that same morning.** KB-VIO-235→238 filed; packets out to PROME and VULCAN.

---

## NEXT SESSION (priority-ordered)

> **The full triaged register — DAEDALUS 🟠/🟡 rows 6–18 with a per-row disposition, plus two DECLINED-BY-DESIGN with reasons — is in `STATUS.md § RESEARCH QUEUE`. Not duplicated here.** Top five only:

1. 🔴 **Backfill `VX_DAILY.tsv`** (missing 8/28 · 8/31 · 9/1 · 9/3; no `skew` 8/27 · 9/4) + a completeness check vs the trading calendar. **This is the ledger every `^SKEW` sustain count is derived from.**
2. 🔴 **Call `skew_integrity.py` from `cheap_tail.py`** — the window is **OPEN 4/4 on an unchecked mirror**, and the tool exists.
3. 🔴 **`^SKEW` back-sweep** — can BOUND, never CLEAR. Say so in the finding.
4. 🔴 **Read the thesis against its trail** — 31 rows / 3 retractions since v4.0, over threshold, still the only open item that is a judgement rather than a build.
5. 📅 **FT-10 chain 9/8 · 9/9** (CBOE at each close; any bar <150 resets) · **grade `VIO-FOMC-0916` 9/16 and 9/23.**

---

## CARRY-FORWARD

- **🔑 THE FINDING: A RULE ALREADY WRITTEN IN CHECKABLE FORM IS THE CHEAPEST MECHANISM AVAILABLE, AND THE EASIEST ONE TO NEVER BUILD.** Step 12 did not need drafting, negotiating or ratifying — it needed ten minutes of code. It got 31 days of being read and nodded at. **When auditing this desk, do not ask "is there a rule?" — ask "is there a rule stated as an arithmetic comparison that nothing computes?"** Those are free wins sitting in plain sight, and I have now found three.
- **⚠️ THE NEW CHECK COMPARES VINTAGE, NEVER CONTENT — DO NOT OVER-READ ITS GREEN.** A brief re-stamped with a fresh `As of:` line over a stale body passes it. That is `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]`, and this check is **blind to it by construction**. It catches the surface **left behind**, not the surface **refreshed badly** — different defects, and only one of them is now mechanized.
- **⚠️ THE PREVIOUS SESSION'S BEST DECISION WAS A REFUSAL, AND THE CRASH DID NOT COST IT.** It found `TRADE.md` **ARMED** on a 64-day-old gate whose legs today's tape satisfies, and **did not fix it** — because standing an authorized gate down is an **authorization** change, not a staleness edit, and PROME relaying a recommendation is not the operator speaking. It wrote the reasoning into the commit message. **Will's word arrived 63 minutes later and the edit took one minute.** `[[finding_relayed_recommendation_is_not_an_approval]]`
- **⚠️ CHECK THE LOG AGAINST THE ARTIFACT, NOT JUST THE LOG.** The WALTER lane read as closed in `board_log.tsv` while the file still sat unprocessed. **A disposition row is a record of an action, not the action.** `[[finding_record_of_an_action_is_not_the_action]]`
- **🔑 THREE OF SEVEN INBOX ITEMS WERE LIVE CORRECTIONS TO THINGS I PUBLISHED THAT MORNING, AND THE LANE HAD BEEN SITTING FOR TWO DAYS.** The gamma board I called "unmeasured" was measured 9/2. The MU date I "fixed" was corrected 9/2. The `^SKEW` hardening I proposed was refuted 9/2. **A deferred inbox is not neutral latency — it is a window in which you keep publishing claims that have already been answered**, and every one of mine was honestly caveated and wrong. `[[finding_dated_carry_item_has_no_expiry_check]]`
- **⚠️ A RECONCILE INSTRUCTION IS AN INSTRUCTION TO AGREE, NOT TO BE RIGHT — AND IT BREAKS TIES TOWARD APPARATUS.** VULCAN had an EDGAR tool and a "zero free parameters" derivation; I had a cell flagged `ESTIMATED, NOT CONFIRMED`. **The weaker-looking cell was the more accurate one, and its own honesty marker is what made it look losable.** Second-order and worth more than the date: **"zero free parameters" is not "no assumptions"** — a 52-week fiscal year was baked into VULCAN's arithmetic rather than exposed as a parameter, so the phrase described what could be tuned, never what was assumed.
- **⚠️ AN EMPTY INBOX CANNOT TELL YOU WHETHER NOTHING WAS SENT OR SOMETHING WAS LOST — CHECK THE SENDER'S RECIPIENT LIST FIRST.** Post-drain, PROME (fresh session after the crash) messaged *"yours is in your inbox under WQ-176."* **The reasonable move was to open my inbox, find nothing, and report a missing packet — manufacturing a delivery incident out of a correct state.** What resolved it was checking the *recipient list*: 11 packets exist, none pathed to VIOLET, and `grep VIOLET PROME/GATES.tsv` returns nothing — **I hold zero action-gate rows, so none was ever owed.** PROME had asserted it from the **count** without reading the list (their error #89; remedy adopted). 🔑 **The asymmetry is the point: "nothing sent" costs nothing and "something lost" costs an investigation, and the empty inbox looks identical in both — so the cheap default resolves toward the expensive reading, most often right after a crash, when the coordinator's own state is least reliable.** → **KB-VIO-239**
- **🔑 "ALL TESTS PASS" IS A STATEMENT ABOUT COVERAGE, NOT CORRECTNESS — AND I QUOTED IT AS THE SECOND, THREE TIMES.** Three review rounds today each found real defects behind a fully green gate. **The gate was never lying; it was answering a narrower question than the one I reported.** ⇒ **When claiming a clean gate, state what it covers** — "six contracts green" means nothing without "and here is what none of them reads." → **KB-VIO-245**
- **⚠️ A FALSE DOCSTRING IS WORSE THAN A MISSING CHECK.** `check_map_agreement` **described** a map↔ledger comparison and **performed an age check** — and I read that docstring twice while auditing the file. It is what a reader trusts *instead of* looking. Now implemented for real, and **it caught a live error of mine on its first run: OVX published FIRE off an intraday tick on a canary that grades on the settle.**
- **⚠️ THREE OF MY NEW CHECKS SHIPPED INERT OR NOISY, AND ONLY FALSIFICATION FOUND IT** — an option strike list read as a convergence score, the date `9/4` read as an FT-10 count, a state comparison that could never fire, and a threshold label read as an asserted state. **Every one was caught by running the check against the real artifact with the real defect injected. None by reading the code.**
- **🔑 FOUR OF DAEDALUS'S FIVE 🔴 ARE ONE SHAPE: A CHECK EXISTED, RAN, AND WAS NOT LOAD-BEARING.** `convergence_score.py` could compute the score and **nothing called it**. The CANARY_MAP matcher ran every boot and **required a digits-only bracket**, so `[8/4 SETTLE]` and `[7/28 report]` were invisible — **its blind spot was my own house style**, and it reported clean on 2 of 6 while six cells sat 31–38 days stale. `closeout_guard` treated a **missing** check as a **pass**. `boot.py` treated an unparsed failure as clean. **In every case the instrument was present, ran, and returned green over the very thing it was built for.** ⇒ **"Is there a check?" and "does it SEE my data?" are different questions, and the second decays** — a matcher is written against the house style of the day it was written, and the house style keeps moving. **Audit a checker by feeding it the CURRENT artifact and counting what it FINDS against what is THERE, never by reading its source.** → **KB-VIO-244**
- **⚠️ THE SHARPEST SINGLE CELL: cheap-tail read `DORMANT 1/4` on CANARY_MAP for 31 days while `cheap_tail.py` printed `OPEN 4/4` at every boot.** The map and the live alert disagreed **maximally**, both were mine, both were read daily, and **nothing compared them.**
- **⚠️ AND THE CONVERGENCE FAULT WAS A CATEGORY ERROR, NOT ARITHMETIC.** Summing cheap-tail — an *opportunity* vector — into a *stress* score makes the score **rise as conditions get calmer**. Three wrong totals are what made me look; **the wrong thing was the design.**
- **🔑 I GOT THE SAME GUARD WRONG THREE TIMES, AND THE THIRD VERSION WAS FALSIFIED BY DATA IN THE LEDGER THAT GUARD READS.** v1 false-DARKed weekly (real bug); v2 assumed no holidays; v3 invented a Monday→Wednesday report-date shift. **`COT_VIX.tsv` contains `2026-05-26` — a Tuesday report directly after Memorial Day.** I never queried it, because I was testing whether the code implemented my belief rather than whether my belief was true. 🔑 **ALL THREE PASSED THEIR OWN SELFTESTS: a selftest cannot falsify the premise it was derived from, so a rising green test count (14→24) read as rising confidence and measured nothing.** ⇒ **When a guard models an external schedule, the FIRST test must be against observed history, not against the model.** → **KB-VIO-243**
- **⚠️ THE STRUCTURAL FIX WAS LESS MODEL, NOT A BETTER ONE.** v4 makes no calendar claim at all — cadence + grace from the ledger. Given a precise rule I keep getting wrong versus a loose rule derived from data, **the loose one wins here: the failure this guard catches persists and gets louder, while a false alarm is read once and dismissed.**
- **⚠️ MY FIRST SWEEP WAS COSMETIC — I FIXED THE SENTENCES THAT WERE QUOTED TO ME.** The RESEARCH QUEUE still carried **seven completed items as live**. **A reviewer's citations are a sample, not the population.** `[[finding_ranked_head_sample_is_not_the_population]]`
- **⚠️ A GUARD I WIRED INTO CLOSEOUT WAS INERT AT CLOSEOUT.** The provenance check returned early whenever the brief was dirty — and at closeout the brief is **always** dirty. I had tested that it was *correct* and never that it was *live on its own path*. `[[finding_guard_correctness_and_wiring_are_independent]]`
- **🔑 AN EXTERNAL REVIEW FOUND FOUR DEFECTS IN WORK I HAD CLOSED OUT "5/5 GREEN" 90 MINUTES EARLIER, AND ALL FOUR REPRODUCED.** Two of the five checks I shipped were materially under-specified; three handoff surfaces contradicted each other; the brief was stamped in its own future. **Every one of my own gates passed over all of it.** 🔑 **A SELFTEST PROVES THE CASES YOU ENUMERATED, NEVER THE ONE YOU DID NOT IMAGINE — AND THE ENUMERATION COMES FROM THE SAME HEAD THAT WROTE THE MODEL.** My COT invariant was contradicted by CFTC's own published release-schedule page, **which I did not open before asserting it. I verified my arithmetic and never verified my premise.** → **KB-VIO-242**
- **⚠️ FIXING ONE DIRECTION OF A SYMMETRIC CHECK LEAVES THE DEFECT ALIVE IN THE OTHER.** Correcting `twin_check` per the review exposed that my fix still **silently skipped past-dated rows on the CATALYSTS side** while reporting them on CALENDAR — and both surfaces carried the *same* three fired August rows. **Taking a review's scope as complete would have left half the bug.** `[[finding_verify_recommended_fix_not_just_finding]]`
- **🔑 FIVE QUEUED TOOL DEFECTS BUILT IN ONE PASS, AND NOT ONE NEEDED NEW ANALYSIS.** Every remedy was already derived and written on a surface — the COT spec in full on CANARY_MAP, the holiday gap in SCRATCH, the phantom leg in STATUS *with its KB id*, both `^SKEW` modes in RED's packet. They sat as **prose** for between 2 days and 7 weeks. **The gap was never diagnosis; it was the hour of typing.** Same shape as KB-VIO-234 — **n=6 in one day.** → **KB-VIO-240**
- **⚠️ THE FALSIFICATION CAUGHT A BUG BEFORE THE COMMIT, WHICH IS THE ONLY REASON I TRUST ANY OF THIS.** `twin_check`'s first version read `date_class` from free prose, so a row correctly marked **CONFIRMED** reported as **MODELED** — because its own supersession note said *"CORRECTED from ~9/22 MODELED to 2026-09-30."* **The supersession note contained the superseded token.** `[[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]]`
- **⚠️ `cmd | tail; echo $?` REPORTS TAIL'S EXIT CODE, NOT THE COMMAND'S — I got this wrong TWICE today** (read `closeout_guard` as 0 when it was 1, `skew_integrity` as 0 when it was 1). **Both times the tool was right and my measurement was wrong.** Measure without a pipe or use `PIPESTATUS`.
- **⚠️ MARKET STATE IS UNCHANGED AND I DID NOT RE-DERIVE IT.** VIX 14.06 · VVIX 82.23 · contango **+12.16%** · cheap-tail 🟣 **OPEN 4/4** · **FT-10 1 of 4** · **29/50** (10 stress vectors × 5 — cheap-tail removed as an *opportunity* vector; scale declared on STATUS). The 10:06 STATUS remains the current read; this session added no market judgement and should not be cited for one.

---

## OPEN HYPOTHESES *(flagged, not actionable — all three carried unchanged; none was tested this session)*

- **H1 — The far-tail bid and the front-end cheapening may be ONE trade, not two.** Selling the front to fund October convexity produces exactly this signature: SKEW ≥150, VVIX falling, contango steepening, October 30/35/60 calls +110–320%. **Strengthened but still untested** — the 9/4 external corroboration (conventional skew ~1st pctile vs 1M deep-OTM put convexity 66th pctile of 5y) is *consistent* with it and is **a relay, not my measurement**. 🔑 **AND THE DEALER-POSITIONING LEG I SAID I DID NOT HAVE WAS IN MY INBOX.** HENRY measured it 9/2: **NEGATIVE gamma, flip band 7,689–7,699, spot 23–33 BELOW, ≈ −$16B/1%, dealers AMPLIFY** — sign INVERTED from the 8/28 read, same source. **This does not confirm H1** (a funding leg is a flow claim; GEX is a positioning state) **but it removes the excuse for not testing it**, and an amplifying board under a far-tail bid into a decision-day expiry is the configuration H1 would matter most in.
- **H2 — RETIRED 9/4.** MOVE's −5.03 as a pre-NFP unwind is **superseded**: Waller's hold signal drove the 9/3 tape (Dow +600, yields fell), which explains both the MOVE drop and VIX 15.20→14.32. **The stronger observation is that the tail bid rose +4.52% INTO a relief rally.**
- **H3 — If FT-10's chain survives 9/4 and 9/8, the fourth bar lands 9/9** — two sessions before CPI, six before the FOMC. A sustain fire arriving *inside* the run-up to both catalysts is a different object from one in quiet tape. **No base rate exists for this; do not improvise one.**
