# VULCAN — SCRATCH ARCHIVE 2026-09

> **FROZEN — never cite a row here as current.** `SCRATCH.md` is the next-session pickup; this file holds session blocks rotated off it under READ_CAP rules 16-17 (the August blocks are in `SCRATCH_ARCHIVE_2026-08.md`).

---

## ROTATED 2026-09-11 from `SCRATCH.md` — the two 2026-09-06 blocks (PM CODEX-review block + AM Will-directed block) — VERBATIM, crc32 `0x8c967b99`, 18,453 B
> Cut at the 9/11 session start: SCRATCH stood at 31,689 B against a 32,550 B budget with a session block to write. The 9/6 START-HERE items that were still live are re-stated in the 9/11 block; the rest is record.

> # ⛔ 2026-09-06 (Sun) PM — CODEX REVIEW, TWO PASSES. READ THIS BEFORE THE BLOCK BELOW.
>
> ## ONE LINE: two external review passes, 7 findings, ALL accepted. **No score, band, threshold or market datum moved** — composite 15/25, fired-count 0 of 5, thesis-kill 1 of 3. Every finding was about instruments and instructions, not the tape.
>
> ## 🔴 THE ONE THAT IS MINE AND WORST: I MISREPRESENTED THE REVIEWER, IN THE FLATTERING DIRECTION
> CODEX wrote that Silicon Data *"distinguishes on-demand, interruptible spot, and reserved pricing in its methodology explanation"* — **true, and exactly what the methodology does.** I restated it as a claim that the vendor **publishes three separate series**, which CODEX never made, then "corrected" the stronger claim I had authored for it, and told Will *"CODEX had the mechanism backwards."*
> - **Reading the reviewer as wrong made my own contribution look larger.** `[[finding_impeachment_must_be_scoped_to_the_claim_not_the_source]]` + `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`, n+1 in the same day.
> - 🔑 **The normalization detail I added is a genuine ADDITION to CODEX's flag, not a refutation of it.** Corrected at the artifact (`GPU_INSTRUMENT_SPEC` §3b) and to Will.
>
> ## 🔴 AND I REPRODUCED A ONE-DAY-OLD LESSON WHILE WRITING THE CORRECTION FOR IT
> Pass 1 downgraded KB-148 to PROVISIONAL and reopened the discrepancy — **then left the original conclusions standing in the same cells** (*"the stated multiple is the reproducible one"*, *"robust to vintage"*, *"the carried USD range is the wrong leg"*). A reader meeting those sentences meets a **settled** row.
> - **That is `[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]` — the exact defect logged ONE DAY EARLIER on WATT's 55 GW wording**, and the lesson was cited in the very pass that reproduced it `[[finding_adoption_is_not_validation]]`.
> - Now **REPLACED, not annotated.** One consistent statement: **reported 4-5x · conditional 4.05-5.67x · discrepancy UNRESOLVED.** Also scoped back: recovering the old answer at USD/KRW 1333.3 does **not** establish I substituted that rate — it is *one plausible* explanation.
>
> ## ✅ WHAT WAS BUILT (the durable half)
> - 🆕 **`scripts/test_validate_workbook.py` — 31-case runnable regression suite, 21 defects + 10 real-form controls, WRONG: 0.** ⚠️ **It sandboxes into a temp tree and NEVER writes a real ledger** — because my ad-hoc harness didn't restore between cases and nine "catches" were measuring a leftover. **A CONTROL case failing is the only reason that surfaced.** Every case carries its own control.
> - **Validator now ENFORCES what the schema declares** — numeric sets/bounds, Float must be FINITE, closed sets retyped `Enum`, new `EnumPrefix` for parameterised tokens (S4 `band`). **Rule: a closed set declares `Enum`; `String` means free text.**
> - **READ-CAP 0 for the first time** — but STATUS breached its budget **twice today on its own correction text**, and the warning I wrote about that breached it a **third** time. Headroom is **431 B**. **Rotate history in the same pass that writes a correction.**
>
> ## 📋 LEDGER-NUDGE DISPOSITION (step 1c-bis — 9 ledgers named, NONE refreshed, and that is the correct answer)
> **Not one is rotting, and refreshing any of them tonight would be a research defect, not hygiene.**
> - **`S2_SERIES` · `MAG7_SERIES` · `LAYER_SERIES` — 🔴 DO NOT REFRESH, and this is the load-bearing one.** All three are on **pre-committed cadences** (Fri 9/11 post-close). The S2 re-arm rule counts *"3+ **consecutive readings**"* and mag7 grades a **duration** test, so **whoever picks the run times picks the readings [L-21]. Curing a staleness nudge with an unscheduled reading is exactly the sampling selection the cadence exists to prevent.** Markets are also CLOSED (Sunday) — a "refresh" would restate Friday's tape as a new observation.
> - **`S4_SERIES` — correctly event-cadenced and the cadence is MONTHLY.** Latest row Jul-2026 **is** the latest month TSMC has published; next 6-K **~9/10**. A refresh today fetches nothing. Owner-confirmed to DAEDALUS 9/6.
> - **`EDGAR_SEEN` — swept 9/3; boot leg 8 reads 3d fresh** against its derived 3-day bound. Event-cadenced.
> - **`GPU_SERIES` — ZERO rows DELIBERATELY.** First reading is 9/11 and only after `GPU-PANEL-01` is frozen. Writing a row to satisfy a nudge would hand the series a baseline from an unspecified panel — the precise failure the empty ledger exists to prevent.
> - **`PREDICTIONS` — rows resolve on DATES; earliest is 9/30.** Nothing is due.
> - **`FLOW` · `VX` — change rarely by design.** No pathway was created or killed this afternoon (`FL-VULCAN-12` moved LIVE→CANDIDATE in the AM and is logged); no vector state moved because **no market datum was observed**. The validator reconciles VX against the STATUS matrix and returns clean.
> - ⚠️ **n+3 on a defect ALREADY routed to DAEDALUS: the nudge counts STATUS-WRITES, not elapsed time, so a multi-pass session inflates every count.** FOUR STATUS writes today (AM close · two review passes · PM closeout) are most of the "behind" figures above — `S4_SERIES` reads *22 behind* while being as current as the world allows. **Confirming instance, NOT a new finding — do not re-report it.**
>
> ## 🔔 FLAGGED, NOT DONE — `memory/auto/finding_test_the_guard_not_just_the_guarded.md` is dirty in the tree (WATT's n+5 append, uncommitted). **I hold an n+6 instance for it** (a suite written to embody that finding whose own controls could not fail). ⚠️ **NOT appended: it is another desk's uncommitted file and editing it would collide.** Flag to PROME.

> ## ▶ START HERE (unchanged and still the hard clock)
> 1. 🔴 **`GPU-PANEL-01` FROZEN BEFORE FRI 2026-09-11** or 9/11 is a MISSED READING. **Now with three corrections folded in:** the Silicon Data index is **LIVE NOW** ($2.53/GPU-hr, `SDH100RT`, **NEO-CLOUD** — record the SEGMENT, it is one side of the 3-6x dispersion); full series is **PAID** (a COST blocker, not unreachable); its **reference basis is UNESTABLISHED**, so `term_normalized` + `spread_pct=UNGRADEABLE` pending the reference spec.
> 2. 🔴 **Fri 9/11 `semi_watch.py` + `mag7.py` POST-CLOSE** — slot 4 of 8, three already lost.
> 3. **ORCL window opens 9/8 · TSMC August 6-K ~9/10 (cite the CUMULATIVE).**
> 4. **Run `scripts/test_validate_workbook.py` after ANY edit to the validator or to SCHEMA type declarations.**
> 5. **Owed back to PROME:** the GPU source-order correction is packeted, not yet acknowledged.



> # ⛔ 2026-09-06 (Sun) — READ THIS BLOCK FIRST. Will-directed collaborative session, 11:19 ET →. 3 dark days before it (9/3 → 9/6).
>
> ## THE ONE-LINE STATE: nothing in the market moved. Composite **15/25, ninth session**, all five channels 3, fired-count **0 of 5**, thesis-kill **1 of 3** (re-read leg by leg, entry in the rail). **No score, band or threshold moved, and no market datum was observed.** This was a correction/consumption pass.
>
> ## 🔴 THE HEADLINE IS A CORRECTION I CONTESTED AND WON AT THE PRIMARY — AND ALMOST DIDN'T
> **WALTER `SIG-W-20260904-001` ruled NVDA's *"primarily related to the procurement of memory"* exists in NO primary. It exists VERBATIM, 1 hit**, in 8-K acc `0001045810-26-000073` → `q2fy27cfocommentary.htm` = **Exhibit 99.2, CFO Commentary of Colette M. Kress**, Item 2.02, filed 8/26. Own EDGAR pull; exhibit identity confirmed in the 8-K body.
> - **KB-118 IS CORRECT AS WRITTEN — including its "VULCAN own EDGAR pull" source line. Accepting the correction would have STRUCK A CORRECT ROW.** This is the **MU-date episode with the roles reversed, one week later**: on 9/2 reconciling to *my* number would have destroyed VIOLET's correct copy; this week the correct copy was mine.
> - **HOW THE ERROR HAPPENED, and WALTER's own table discloses it:** the 10-Q row carries **two** independent checks and is **right**; the two 8-K rows carry **one** (DEWEY), and Ex-99.2 is wrong. **One desk's read of one exhibit became "no primary document" in a verdict header.**
> - 🔑 **WHAT SURVIVES IS BETTER THAN THE DISPUTE: two NVDA documents filed the SAME DAY attribute the SAME $119B→$279B differently** — Ex-99.2 says *"procurement of memory"*, the 10-Q says *"data center infrastructure systems, primarily memory AND MANUFACTURING FACILITIES"*. **And the 8-K says on its face the CFO Commentary is "furnished and shall not be deemed filed" (§18)** ⇒ **the NARROW attribution everyone quoted is in a FURNISHED exhibit; the BROADER wording is in the FILED 10-Q. Prefer the filed wording. Quote the CFO line AS CFO commentary, never as the filing's operative words.**
> - **Adopted anyway (their direction call is right): the memory SHARE is undisclosed in both ⇒ `FL-VULCAN-12` downgraded LIVE → CANDIDATE — direction intact, CANNOT BE SIZED.** S2 stays 3. [KB-147]
>
> ## 🔴 THE MOST UNCOMFORTABLE FINDING IS MINE — A 33-DAY DEFECT INSIDE MY OWN KB CELL
> **WATT retracted *"~55 GW nameplate interconnection ceiling"* as its own imprecision on 2026-08-04.** I recorded the corrected FACT in **KB-087 on 8/13 and wrote the RETRACTED WORDING into the same cell as the ADOPT-VERBATIM instruction.**
> - **A correction and the instruction it kills, side by side in one cell. The instruction is the half that travels.** It propagated to **STATUS ×4 · CHANNEL_DETAIL ×2 · THESIS · VX · EXIT_PROTOCOL · NEXUS_BRIEF ×2**, was broadcast to NEXUS, and **DAEDALUS cited it 9/5 as "the strongest cross-desk form I have seen on the fleet"** while it carried a withdrawn population.
> - 🔑 **WHY EVERY CHECK PASSED: nothing was factually wrong, no number was wrong, and the eight surfaces AGREED WITH EACH OTHER — which is what a PROPAGATED INSTRUCTION produces, and is indistinguishable from corroboration.** It took a **third party (CODEX, reviewing WATT)** to read WATT's retraction against my instruction. WATT's STATUS claimed my files carried its wording *"verbatim"* **without ever grepping them** (its L-46). **Neither desk's own checks could fire.**
> - **Fixed on all 8 + KB-087 annotated at source + KB-146. Disclosed to DAEDALUS against my own Conf M→H grade.** `[[finding_correction_beside_an_instruction_leaves_two_live_instructions]]` · `[[finding_adoption_is_not_validation]]` at its limit case.
>
> ## ✅ WHAT ELSE GOT DONE
> - **WALTER lane DRAINED 4/4**, all in `board_log.tsv` with reasons (`acted`×3, `noted`×1 **with its reopen condition**).
> - **VIOLET's 9/4 flag applied** — the *"headroom goes from ~1 day to ~6-13 days"* clause was **INVERTED** by the confirmed 9/30 print and sat live in **VULCAN-02/-11/-12** for 4 days after the date was corrected everywhere else. **A corrected date does not correct the argument built on the old one.** Struck in place, 8/27 block retained verbatim, correction appended. Brief CLOCK rows 243/244 rebuilt.
> - **HBM3E multiple resolved: carry the STATED 4–5×.** At USD/KRW **1351.1** the LTA range 500-700k won = **$370–518** ⇒ **4.05–5.67×** vs $2,100 spot. WALTER's computed 5.25–7× needs USD/KRW **1,667–2,333**. **FX artifact, not a source disagreement.** ⚠️ **The ~70%-locked figure NOT carried** — "reportedly" in every outlet, UNVERIFIED-RELAY on the same test I applied to Bernstein. [KB-148]
> - **GPU-RENTAL INSTRUMENT ENCODED** (PROME ruled it mine 9/3): 11th ledger `GPU_SERIES.tsv` + schema + `workbook/GPU_INSTRUMENT_SPEC.md` + **cadence PRE-COMMITTED with ZERO ROWS WRITTEN** + registered in CATALYSTS + **surfacing at boot leg 6 the same session**.
> - **DAEDALUS answered** — lesson phrasing with a **testable discriminator** against PAT-115 (*"if the guarded event happens at the EARLIEST time it ever has, does this guard still fire before it? If no, it is a miss-detector, not a guard"*), `S4_SERIES` owner-confirm (NOT stale — monthly cadence, latest row IS the latest published month), profile trigger re-dated off the refuted 9/17 window.
> - **WATT: seam closed AT MY ARTIFACT** with the line quoted back. Its ask ① answered: **`FL-WATT-08` is WATT's row, not mine**, and no VULCAN surface took backup dispatch as observed — **KB-145 already said authorised-not-operated because I adopted WATT's own guard.**
>
> ## 🔧 FOUR INSTRUMENT DEFECTS FIXED — THREE IN MY OWN GUARDS
> 1. **`validate_workbook.py` could not grade an EMPTY ledger** (header taken from `data[0].keys()`) ⇒ a correct header with zero rows reported EVERY column missing. **Blocked the correct discipline.** Fixed; **3 injections, 3/3 fire, no false positive.**
> 2. **My own fix printed a false certification** — the new note said *"header conforms"* **before** the drift check. Caught by injection 1. **Reordered.** `[[finding_a_correction_pass_is_unreviewed_work]]`, measured on myself inside one session.
> 3. **`catalyst_countdown.py` had NO holiday calendar** — reported 9/08 as "2d trd" over **Labor Day 9/07**. Every trading-day distance past a holiday overstated, **in the reassuring direction**. Rule-based NYSE calendar added; **10/10 exact match** vs an independently derived 2026 list.
> 4. **My own `semi_watch.py` cadence was 3-of-8 REGISTERED** — five slots lived only in CLAUDE.md prose. **PAT-063 transport gap on my own rule.** All registered.
>
> ## ▶ START HERE NEXT SESSION
> 1. 🔴 **`GPU-PANEL-01` MUST BE FROZEN BEFORE FRI 2026-09-11 or 9/11 is a MISSED READING and is recorded as one.** Six things it must specify → `workbook/GPU_INSTRUMENT_SPEC.md` §5. **Do NOT write a row from an unspecified panel.**
> 2. 🔴 **Fri 9/11 `semi_watch.py` post-close — slot 4 of 8, THREE already lost.** Run it regardless of the tape.
> 3. **9/11 is a FOUR-WAY DAY:** semi_watch + GPU panel/reading 1 + self-grade CHECKS 1-3 (baselines frozen 8/21).
> 4. **ORCL window opens 9/8 (1 trd) · TSMC August 6-K ~9/10 (3 trd, cite the CUMULATIVE).**
> 5. **The 9/30 stack is a 10/01 stack.**
>
> ## ✅ BOTH DECISIONS RULED BY WILL THE SAME SESSION — AND BOTH EXECUTED
> - ✅ **`PREDICTIONS.tsv` SPLIT DONE. 57,244 B (106% of cap) → 37,332 B (69%). 0 over the cap.** ⚠️ **Still above the 60% BUDGET and I am saying so rather than rounding to compliance** — the remaining 8 rows are all OPEN and live, so there was nothing further to move honestly. 8 resolved rows → `archive/PREDICTIONS_RESOLVED_2026-09.tsv` **verbatim, conservation proven (16 in == 8 archived + 8 live, byte-identical, no mutation)**, crc `0xc3603220`; banner + reasoning in the companion `.README.md` (the TSV stays a pure TSV so the calibration record remains machine-readable, and a resolved row is **self-marking** via its own `status` column).
>   - 🔴 **THE TRAP REGISTERED ON 9/3 WAS REAL, AND IT CAUGHT EXACTLY ONE ROW.** All 8 resolved rows were read individually for forward commitments. **`VULCAN-07` is the only one carrying a live standing rule** — *"≥2 of 4 change useful-life → promote obsolescence to a full channel (S6)"*, state **0 of 4**. It was archived **only because `STATUS.md`'s exit triad states that gate self-containedly — rule, state AND verdict — rather than merely referencing the prediction.** ⚠️ **If that STATUS row is ever reduced to a pointer, the standing rule must move back into a live ledger first.** That note is now ON the STATUS row itself, not just here.
>   - ⚠️ **`VULCAN-08` (OPEN, resolves 2027-02-15) is the January re-test registered off `VULCAN-07`** — it stays live; its antecedent is in the archive. Indexed in the README so the ID never dead-ends.
>   - ⚠️ **Pre-edit review was done BY ME, not by a blind cold reader** (I did not spawn one). **That is a weaker check than the 9/3 deferral asked for and I am naming it rather than letting "reviewed" stand unqualified.** What substituted: an exhaustive per-row forward-marker scan, a live-citation scan across every non-archive surface, and a byte-level conservation proof.
> - ✅ **`mag7.py` CADENCE PRE-COMMITTED** — post-close Fridays **09-11 · 09-18 · 09-25 · 10-02 · 10-09 · 10-16 · 10-23 · 10-30**, sharing the Friday slot with `semi_watch.py`, registered and surfacing at boot.
>   - 🔑 **THE ARGUMENT IS NOT STALENESS AND THAT MATTERS: thesis-kill LEG 2 is a DURATION test (*"Mag-7 ≤28% held 3+ MONTHS"*), and this desk's own rule is that "sustained" carries N+ sessions — so on an IRREGULAR series "sustained" was UNGRADEABLE BY CONSTRUCTION, on my own primary S1 instrument.** The 9/2 yellow trip could only be called *"n=2, not sustained"* because the readings happened to fall close together. Nothing guaranteed that.
>   - ⚠️ **`DUPLICATE-VINTAGE` rows are WRITTEN, never skipped** — if SSGA has not published a new `holdings_asof`, record the row and mark it. **Skipping on a condition correlated with anything is sample selection**, the same defect as running off-cadence [L-21].
>   - ⚠️ **RENEWAL RULE: extend by 8 more Fridays BEFORE the last committed slot fires, never after.** Renewing after seeing the readings a renewal would schedule is selection.
>   - **No threshold was set or moved.** The bands are unchanged; the cadence makes the EXISTING ones gradeable over time.
>
> ## ❌ STILL OPEN
> - 🟠 **`CLAUDE.md` grew 59,354 → 66,071 B this session.** Auto-loaded, so not READ_CAP-bound, but it costs context every boot and I made a watched problem worse. **Watch, don't rotate** — flag to PROME if it keeps growing.
> - 🟠 **`mag7.py` has NO pre-committed cadence** and it is **thesis-kill leg 2's instrument**, with the yellow band freshly tripped and the series 5 days old. Either pre-commit one or say why not.
> - 🟠 **CARRIED FORWARD 2026-09-06 FROM THE 8/27 BLOCK, WHICH WAS ROTATED THIS SESSION:** **PROME's L-21 routing to Will is still UNRULED.** ⚠️ It was written in the 8/27 block and appeared on **no other surface** — not STATUS, not `PROME/WILL_QUEUE.md`, not the register. The READ-CAP rule-17 obligation enumeration is the only reason it was found; rotating that block without this line would have deleted the only copy `[[finding_live_claim_in_a_closed_container_is_invisible]]`.
> - **Hyperscaler long-dated-issuance check** (KB-096, one query, carried since 8/13) · **QQQ sector variant** (blocker NAMED: Invesco 406s its domain) · **boot step 8 channel-liveness still has no leg in `boot.py`** (DAEDALUS flag ①, accepted, still queued).


