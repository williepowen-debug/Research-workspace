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

1. ✅ **DONE 9/4 — inbox lane 7/7, both lanes empty; WQ-177 packet delivered to PROME; `test_daily_log` fixed 43/43.** Nothing carried forward from this item.
2. ✅ **BUILT 9/4 PM — `scripts/skew_integrity.py`.** Compares VALUES cell-by-cell vs CBOE; **independently reproduced RED's 2025-12-24 disagreement** (161.30 vs 160.529999) before I trusted it. **Run it whenever a `^SKEW` value is consumed and paste its verdict beside the claim** — deliberately NOT boot-wired. *(was: re-derive against values, not bar counts —)* RED's 253-session base rate found a second defect mode — a **wrong value** (2025-12-24) beside the known omission — and a completeness check is blind to it. **My previously-written remedy does not work as specified.** Compare against CBOE cell-by-cell at the moment of use and record the result with the claim.
3. 🔴 **Watch FT-10's chain: 9/4 · 9/8 · 9/9.** Pull CBOE at each **close**. `^SKEW` is **EOD-only — zero intraday bars, verified empirically twice today** — so no intraday session can move the count. **Any bar <150 resets to 0. Never say "fired" before the fourth bar.**
4. ✅ **FIXED 9/4 PM — schedule-aware, 14-check selftest, guard green.** *(was: fix the COT staleness contract —)* It printed its guaranteed false DARK again this morning — ledger 8/25, 10d, and **8/25 is the correct latest report**; the 9/1 report released today 15:30 ET. Correct spec is derived and already written on `CANARY_MAP.md`: **DARK iff max ledger date is older than the latest Tuesday whose Friday release has passed.** Self-calibrating, no constant.
5. 🔴 **`^SKEW` back-sweep — owed, and now weaker on BOTH modes.** A healed omission is invisible to a re-pull (KB-VIO-221) **and** a wrong value was never visible to a structural check at all (KB-VIO-236). It can bound neither cleanly. **Say that in the finding rather than implying coverage.** Open and unchecked: whether `VX_DAILY.tsv` retains a snapshot that closes the 2025-12-24 vintage question RED had to mark UNKNOWN.
6. ✅ **BUILT 9/4 PM — `scripts/twin_check.py`, BLOCKING at closeout. It refuses to name a winner.** *(was: build it to compare against the SOURCE, not the twin —)* KB-VIO-235 is the reason: a check that asks only *whether* two surfaces agree turns every disagreement into propagation of whichever was touched last, which is exactly how I overwrote the closer MU date with the further one.
7. 📅 **Grade `VIO-FOMC-0916`** at the 9/16 and 9/23 closes off the frozen card. Contango leg crosses the roll break (KB-VIO-218). ✅ **The MU leg-2 confound is WITHDRAWN** — MU is CONFIRMED 2026-09-30 (own primary verification 9/4), **outside** leg 2's 9/16→9/23 window, so **leg 2 grades clean**. KB-VIO-235.
8. ✅ **`catalyst_countdown.py` holiday table BUILT** (Labor Day now 0d; CPI 4d, FOMC 7d) · ✅ **`move.py` phantom GATE-VIO-116 leg REMOVED.** Remaining: 🟠 CALENDAR↔CATALYSTS twin-divergence check (still a ritual without a mechanism — **the same class as KB-VIO-234, and now the obvious next one to mechanize**) · 🟠 DAEDALUS sfg-sweep ACTION 2 · 🟠 Path A F2 audit · 🟠 VIX9D/VIX base rates.
9. 🟡 **MAINTENANCE.md 317 lines vs ~300 cap** — boot flags it every session; archive oldest entries before the next structural append.

---

## CARRY-FORWARD

- **🔑 THE FINDING: A RULE ALREADY WRITTEN IN CHECKABLE FORM IS THE CHEAPEST MECHANISM AVAILABLE, AND THE EASIEST ONE TO NEVER BUILD.** Step 12 did not need drafting, negotiating or ratifying — it needed ten minutes of code. It got 31 days of being read and nodded at. **When auditing this desk, do not ask "is there a rule?" — ask "is there a rule stated as an arithmetic comparison that nothing computes?"** Those are free wins sitting in plain sight, and I have now found three.
- **⚠️ THE NEW CHECK COMPARES VINTAGE, NEVER CONTENT — DO NOT OVER-READ ITS GREEN.** A brief re-stamped with a fresh `As of:` line over a stale body passes it. That is `[[finding_header_edit_is_the_edit_most_mistaken_for_maintenance]]`, and this check is **blind to it by construction**. It catches the surface **left behind**, not the surface **refreshed badly** — different defects, and only one of them is now mechanized.
- **⚠️ THE PREVIOUS SESSION'S BEST DECISION WAS A REFUSAL, AND THE CRASH DID NOT COST IT.** It found `TRADE.md` **ARMED** on a 64-day-old gate whose legs today's tape satisfies, and **did not fix it** — because standing an authorized gate down is an **authorization** change, not a staleness edit, and PROME relaying a recommendation is not the operator speaking. It wrote the reasoning into the commit message. **Will's word arrived 63 minutes later and the edit took one minute.** `[[finding_relayed_recommendation_is_not_an_approval]]`
- **⚠️ CHECK THE LOG AGAINST THE ARTIFACT, NOT JUST THE LOG.** The WALTER lane read as closed in `board_log.tsv` while the file still sat unprocessed. **A disposition row is a record of an action, not the action.** `[[finding_record_of_an_action_is_not_the_action]]`
- **🔑 THREE OF SEVEN INBOX ITEMS WERE LIVE CORRECTIONS TO THINGS I PUBLISHED THAT MORNING, AND THE LANE HAD BEEN SITTING FOR TWO DAYS.** The gamma board I called "unmeasured" was measured 9/2. The MU date I "fixed" was corrected 9/2. The `^SKEW` hardening I proposed was refuted 9/2. **A deferred inbox is not neutral latency — it is a window in which you keep publishing claims that have already been answered**, and every one of mine was honestly caveated and wrong. `[[finding_dated_carry_item_has_no_expiry_check]]`
- **⚠️ A RECONCILE INSTRUCTION IS AN INSTRUCTION TO AGREE, NOT TO BE RIGHT — AND IT BREAKS TIES TOWARD APPARATUS.** VULCAN had an EDGAR tool and a "zero free parameters" derivation; I had a cell flagged `ESTIMATED, NOT CONFIRMED`. **The weaker-looking cell was the more accurate one, and its own honesty marker is what made it look losable.** Second-order and worth more than the date: **"zero free parameters" is not "no assumptions"** — a 52-week fiscal year was baked into VULCAN's arithmetic rather than exposed as a parameter, so the phrase described what could be tuned, never what was assumed.
- **⚠️ AN EMPTY INBOX CANNOT TELL YOU WHETHER NOTHING WAS SENT OR SOMETHING WAS LOST — CHECK THE SENDER'S RECIPIENT LIST FIRST.** Post-drain, PROME (fresh session after the crash) messaged *"yours is in your inbox under WQ-176."* **The reasonable move was to open my inbox, find nothing, and report a missing packet — manufacturing a delivery incident out of a correct state.** What resolved it was checking the *recipient list*: 11 packets exist, none pathed to VIOLET, and `grep VIOLET PROME/GATES.tsv` returns nothing — **I hold zero action-gate rows, so none was ever owed.** PROME had asserted it from the **count** without reading the list (their error #89; remedy adopted). 🔑 **The asymmetry is the point: "nothing sent" costs nothing and "something lost" costs an investigation, and the empty inbox looks identical in both — so the cheap default resolves toward the expensive reading, most often right after a crash, when the coordinator's own state is least reliable.** → **KB-VIO-239**
- **🔑 FIVE QUEUED TOOL DEFECTS BUILT IN ONE PASS, AND NOT ONE NEEDED NEW ANALYSIS.** Every remedy was already derived and written on a surface — the COT spec in full on CANARY_MAP, the holiday gap in SCRATCH, the phantom leg in STATUS *with its KB id*, both `^SKEW` modes in RED's packet. They sat as **prose** for between 2 days and 7 weeks. **The gap was never diagnosis; it was the hour of typing.** Same shape as KB-VIO-234 — **n=6 in one day.** → **KB-VIO-240**
- **⚠️ THE FALSIFICATION CAUGHT A BUG BEFORE THE COMMIT, WHICH IS THE ONLY REASON I TRUST ANY OF THIS.** `twin_check`'s first version read `date_class` from free prose, so a row correctly marked **CONFIRMED** reported as **MODELED** — because its own supersession note said *"CORRECTED from ~9/22 MODELED to 2026-09-30."* **The supersession note contained the superseded token.** `[[finding_marker_word_in_prose_disables_the_scanner_that_reads_for_it]]`
- **⚠️ `cmd | tail; echo $?` REPORTS TAIL'S EXIT CODE, NOT THE COMMAND'S — I got this wrong TWICE today** (read `closeout_guard` as 0 when it was 1, `skew_integrity` as 0 when it was 1). **Both times the tool was right and my measurement was wrong.** Measure without a pipe or use `PIPESTATUS`.
- **⚠️ MARKET STATE IS UNCHANGED AND I DID NOT RE-DERIVE IT.** VIX 14.06 · VVIX 82.23 · contango **+12.16%** · cheap-tail 🟣 **OPEN 4/4** · **FT-10 1 of 4** · convergence **26/55**. The 10:06 STATUS remains the current read; this session added no market judgement and should not be cited for one.

---

## OPEN HYPOTHESES *(flagged, not actionable — all three carried unchanged; none was tested this session)*

- **H1 — The far-tail bid and the front-end cheapening may be ONE trade, not two.** Selling the front to fund October convexity produces exactly this signature: SKEW ≥150, VVIX falling, contango steepening, October 30/35/60 calls +110–320%. **Strengthened but still untested** — the 9/4 external corroboration (conventional skew ~1st pctile vs 1M deep-OTM put convexity 66th pctile of 5y) is *consistent* with it and is **a relay, not my measurement**. 🔑 **AND THE DEALER-POSITIONING LEG I SAID I DID NOT HAVE WAS IN MY INBOX.** HENRY measured it 9/2: **NEGATIVE gamma, flip band 7,689–7,699, spot 23–33 BELOW, ≈ −$16B/1%, dealers AMPLIFY** — sign INVERTED from the 8/28 read, same source. **This does not confirm H1** (a funding leg is a flow claim; GEX is a positioning state) **but it removes the excuse for not testing it**, and an amplifying board under a far-tail bid into a decision-day expiry is the configuration H1 would matter most in.
- **H2 — RETIRED 9/4.** MOVE's −5.03 as a pre-NFP unwind is **superseded**: Waller's hold signal drove the 9/3 tape (Dow +600, yields fell), which explains both the MOVE drop and VIX 15.20→14.32. **The stronger observation is that the tail bid rose +4.52% INTO a relief rally.**
- **H3 — If FT-10's chain survives 9/4 and 9/8, the fourth bar lands 9/9** — two sessions before CPI, six before the FOMC. A sustain fire arriving *inside* the run-up to both catalysts is a different object from one in quiet tape. **No base rate exists for this; do not improvise one.**
