# BRENT — RULINGS & DECISION RECORD

**Created 2026-08-05 (Will-approved).** **This file is NOT read at boot.** It is the dated record of *why* the operating docs say what they say — read on demand, when you are about to change a rule, or when you want to know whether a decision was deliberate.

> ### ⛔ **WHY THIS FILE EXISTS — AND WHAT IT IS NOT ALLOWED TO BECOME**
> **Measured 2026-08-05:** the RAV state-replacement pilot's WP4 was *"flatten human boot,"* and it succeeded on steps (31 → 24) while `CLAUDE.md` **grew 243 → 252 lines / 36.9 → 38.9 KB.** The BOOT section carried **9 human actions and 18 lines of rationale prose.** Hot context across the five boot-read files measured **317 KB**, of which **286 lines carry a date** and **66 carry RETIRED/SUPERSEDED/CORRECTED/DEFECT.**
> **★ THE MECHANISM: SPECS GET REPLACED; THE PROSE ABOUT THE REPLACEMENT ACCUMULATES.** Every incident deposited a dated *"here is what was wrong and why"* block into the **operating** doc. Each was individually justified. Together they made the instructions a minority of the instruction file. **History and instructions were living in the same file — valuable as history, toxic as boot context.**
> **★ AND THE RETIREMENT RATCHET HAD A SCOPE HOLE:** adopted 2026-08-04 to oppose exactly this, it governs **state** (scripts, registry rows, checks) and **says nothing about prose.** Since adopting it, every change was an addition. **Words were never counted.**
> **⇒ THE SPLIT: operating docs carry what to DO. This file carries why.** Nothing was deleted in the split — **only moved out of hot context.**
> ⚠️ **THE DISCRIMINATOR, and it is the one thing to get right when moving a block here: does it CONSTRAIN A FUTURE ACTION (stays live) or RECORD A PAST ONE (moves here)?** **Do NOT sweep by "has a date."** Several dated blocks are *binding limits Will ruled must travel on the live spec* — e.g. *"this regime has produced ZERO genuine physical reopenings"* and TERRY's *"a firing gate carries zero thesis information."* **Those stay on the spec. Moving them here would be the exact failure this restructure could cause.**
> ⚠️ **This file has no length cap and needs none — it is cold. But it must never acquire an instruction.** If you find yourself writing "always do X" here, X belongs in `CLAUDE.md` or `TRADE.md`.

---

## 2026-08-05 — LEG T v6: THE MEASUREMENT MOMENT MOVED (Will-ruled) {#legT-v6}

**Live spec → `TRADE.md` §STAGE-A Leg T.** Record only.

**The defect:** Leg T was graded day-0 **close-to-close** while sizing fires **tranche 1 on day 0** ⇒ knowable exactly when the day-0 fill became impossible. **Zero-minute window — the DEPLOY GATE v2 defect in a second ratified gate.** Root cause was one word in the ratified sizing rationale: *"both are observable on the announcement session."* **Observable is not actionable.**

**The naive fix was refuted before it shipped** (LESSONS #21, base-rate before proposing). A live-at-the-ticket `T` **BLOCKS Jun-17 — the one analogue where the crude short made money — at four of six morning check times**: 09:45 **0.61** · 10:00 **0.95** · 10:30 1.06 · 11:00 **0.41** · 12:00 **0.92** · 14:00 1.55 · 15:00 1.19 · 15:30 1.43 · 15:45 1.51 · 15:55 1.68 · **close 1.68**.
**★ `T` IS A MAGNITUDE THAT GROWS THROUGH THE SESSION**, so a threshold calibrated on FULL-session moves is systematically too high at any PARTIAL-session moment. **A units mismatch, not a level to re-tune.**

**Agreement with the close-basis verdict** (n=59, 2026-05-12→08-05): 14:00 **93.2%** (false-pass 3.4%) · 15:00 89.8% (8.5%) · 15:30 91.5% (6.8%) · 15:45 94.9% (5.1%) · 15:55 100% (0%).
**Polling hazard, 5-min re-evaluation:** **66.1% of sessions flip the verdict at least once** (median 2, max 21); after 14:00 → 20.3% (median 0, max 6).

**Ruled:** grade ONCE at/after 14:00 ET, with T1 (one-grade-only) + T2 (close basis forfeits tranche 2) as a both-or-neither pair. Window **0 → 120 min**.
**Disclosed at ruling:** 14:00 is **not** empirically superior to 15:00 — 3.4% vs 8.5% is **2 vs 5 sessions at n=59**, noise, non-monotone; chosen for the **window**, not the base rate. **Apr-17 cannot be re-run** (5m history starts 2026-05-11) so false-dawn cover is **argued** intact via legs (i)/(C), **not measured**.

---

## 2026-08-05 — READING BASIS ADDED TO `instrument_check` {#reading-basis}

**Live schema → `workbook/REGISTRY.tsv` header.** Record only. `supersedes: instrument_check window logic v1 (single-basis)`.

v1 computed every same-session window as `action_close − LAST print` — right only for a reading needing the final value. It produced a **FALSE 🔴 on DEPLOY GATE v3 leg (a2)**, an existence test reported as a **0-minute** window when its real window is **390 min**, on the gate ratified the day before. **A false red on a live gate is corrosive twice: it makes the flagship class noisy, and a permanently-red row decays into decoration** — the disease that retired the `crack >$30` line on 7/31.

**Falsified before shipping, 7/7** (`[[finding_test_the_guard_not_just_the_guarded]]`): the superseded `:final` basis **still fires 🔴** (not weakened) · bare/undeclared still fires 🔴 · `:any` → 390min ✅ · `:at1400` → 120min ✅ · grade-before-open → 🔴 · grade-at-action-close → 🔴 · malformed → 🔴 refused rather than guessed. **Blocking 7 → 6 → 5 across the two fixes; every red removed was a false one.**

---

## 2026-08-05 — TWO STALE OWNERSHIP POINTERS (RAV Risk #1, realized) {#ownership-pointers}

`CLAUDE.md` and `thresholds.py`'s docstring both still declared `thesis/THESIS.md` the canonical threshold registry **four days after the pilot moved the machine home to `REGISTRY.tsv`**. `thresholds.py` carried **two contradictory ownership declarations in one file** and pointed readers at *"the tables below"* that the same commit had deleted.

**★ Both were CORRECT WHEN WRITTEN** — ratified by the F3 ruling of 7/31, whose entire subject was ownership. **F3 fixed the question once; the pilot moved the answer; nothing re-asked it.** **A stale pointer with a citation defends itself.** No check caught either — every check probes *levels and instruments*; **nothing probes "does this file name the right owner."** → `[[finding_ownership_claim_is_last_to_move]]`

**Also found:** the pilot's headline *"coverage 15 → 46"* counted **enrollment, not consolidation** — 10 of 47 rows had no machine-readable level, and `eia_weekly.py` is a fourth threshold home the pilot never touched (two of its hardcodes fire red at boot; refinery util >95% has no registry row at all). Full measurement → `workbook/PILOT_STATE_REPLACEMENT_MEASUREMENT.md`.

---

## 2026-08-04 — THE RETIREMENT RATCHET (Will-approved, RAV ruling) {#retirement-ratchet}

**Live rule → `CLAUDE.md` §Standing Rules.** Record only.

**Why:** this kit had a pure ADDITION ratchet. Every incident produced a new guard; **no incident had ever produced a deletion — 9 scripts, 0 ever retired.** `ledger_staleness` sat in boot for weeks scanning four FROZEN files. A threshold's identity had accreted **THREE live homes**, and `thresholds.py:81` carried a standing TODO naming that exact rot which nobody actioned **because adding is always easier than removing.**
**A guard that is never retired is not free — it costs attention, and attention is the scarce resource that made the original defect invisible.**
*(The instrument check absorbed the whole `INSTRUMENTS.tsv` registry into `REGISTRY.tsv` rather than standing up a second file — that is the extend-don't-add pattern.)*
⚠️ **2026-08-05: this ratchet governs STATE and not PROSE. That hole is what produced this file** — see the header.

---

## 2026-08-04 — `ledger_staleness.py` RETIRED FROM BRENT BOOT + THE WP5 RESIDUAL-GUARD DECISION {#ledger-staleness}

It scanned five `workbook/` ledgers of which **four are FROZEN**, so its normal output had decayed into confirming old architecture. **The script itself stays — other agents have live ledgers.** BRENT's live ledgers (`REGISTRY.tsv`, `CATALYSTS.tsv`, `INCIDENTS.tsv`, `PREDICTIONS.tsv`, `board_log.tsv`) were never in its scan path anyway. **Do not re-wire it into BRENT boot without a live unfrozen surface for it to inspect.**

**WP5 residual-guard decision** (RAV risk: *"removed without preserving the one useful guard it still provided"*): the residual need is *"a FROZEN ledger must never be written."* **Judged LOW risk and DELIBERATELY NOT replaced with a new check** — no closeout step targets those files, the closeout ledger step carries an explicit ANNOTATED SKIP naming all three as frozen, and any write would appear in the commit diff. `supersedes: ledger_staleness (BRENT boot only)`. ⚠️ **Revisit if a frozen file is ever actually modified** — but adding a guard for a risk that has never fired is the exact ratchet this pilot exists to oppose.

---

## 2026-07-31 — C6: A BARE STAMP BUMP ON UNVERIFIED CONTENT IS PROHIBITED (Will-ruled) {#c6}

**Live rule → `CLAUDE.md` closeout step 12.** Record only.

The retired minimum was *"refresh the `As of:` stamp + `STATUS commit:` hash so staleness self-corrects."* **That minimum is what let `NEXUS_BRIEF.md` publish a retired spec to a live consumer twice in eight days** — a filled position carried as *"pending fill"* 7/24→7/28, and retired Stage-A v2 semantics 7/24→7/31 — **through a step that RAN both times.** **A refreshed stamp on stale content makes the file look MORE current while staying wrong**: the stamp is a *freshness* check and the failure was *agreement*. `[[finding_freshness_check_cannot_catch_a_fresh_lie]]`
⚠️ **"I didn't change anything" is not a content re-verify.** The brief goes stale when the SPEC moves, not when the brief is edited — **that is exactly how both failures happened.**
**n+1 (2026-08-05):** C6 caught a third — the brief's NEXT DECISION POINT block still published **DEPLOY GATE v2** as the governing rule a day after v3 superseded it, *in the same file whose header recorded C6 catching that exact defect in the gate block.* **The gate block was rewritten; this one was not — a partial fix the header then described as done.** `[[finding_record_of_an_action_is_not_the_action]]`

---

## 2026-07-31 — C2: LESSON PROSE AND INDEX MOVE IN THE SAME COMMIT (Will-ruled) {#c2}

**Live rule → `CLAUDE.md` §Standing Rules.** Record only.

Four defects on 2026-07-30 shared one root cause: **two of my lessons disagreed, nothing forced a reconciliation, and WHICHEVER WAS WRITTEN FIRST WON BY DEFAULT when a spec got drafted.** L18 beat L19 into the ratified off-ramp gate; L18 beat **both** L11 and L16 on entry timing; L21 was violated by a falsifier written a day after L21's fix was ratified; L15's tenor was inherited by a trade it was never scoped to. **A prose lessons file cannot detect its own contradictions.** `🔴 UNDECLARED` is the dangerous class — neither lesson names the other, so nobody has ever adjudicated them.

**The `--prose` drift check was falsified before shipping, not just run:** against the live defect (L18 amended in index, prose unsynced) → fires · synthetic missing-prose row → fires · clean tree → exit 0. ⚠️ **Deliberately NARROW: it does NOT semantically compare an `asserts` value to a paragraph** — that would report false clean, the failure mode it exists to kill.

---

## 2026-07-31 — F3/F9/C3: THREE CLOSEOUT STEPS POINTED AT DEAD SURFACES {#dead-surfaces}

- **F3** — `CLAUDE.md` carried a SECOND threshold table which had silently diverged from THESIS **in both directions**: boot read one, the enforcer read the other. **Ruled: one table, one home, boot reads the pointer.** *(Superseded 2026-08-05 — the machine home is now `REGISTRY.tsv`; see [#ownership-pointers](#ownership-pointers).)*
- **F9** — the thesis closeout step pointed a LIVE write at `thesis/TIMELINE.md`, **FROZEN since 2026-07-01** ("SUPERSEDED, last maintained Apr-16") — **a no-op that reads as covered.** Forward state now lives in `docket/CATALYSTS.tsv` + `thesis/CHANGELOG.md`. **Do not resurrect TIMELINE**; if a forward-view doc is wanted again, create it deliberately rather than un-freezing a 3-month-stale one.
- **C3** — the workbook closeout step's OPENING clause told sessions to write to `KB.tsv` / `VX.tsv` / `FLOW.tsv`, **all FROZEN 2026-07-01.** Same class as F9.
- **F4/F3 threshold retirements** — `gasoline crack >$30` retired: **breached for months** (crack $58.25 on 7/29 vs the line = 60–95% above) and **not carried in `thresholds.py`**, so it alerted on nothing in either direction. **A permanently-breached tripwire is decoration.** `VLCC >WS200` retired: **no Worldscale feed has ever existed in this kit**, so it was never once evaluated. ⚠️ **Either one, if wanted again, is a NEW REGISTRATION with base rates — not a re-level.**

---

## 2026-07-28 — MAIL: TRIAGE AT BOOT, ARCHIVE AT CLOSEOUT {#mail}

**Live rules → `CLAUDE.md` boot step 6b + closeout step 13a.** Record only.

The legacy *"do not process inbox on normal spawns"* rule left **general agent packets with no protocol step at all**, so they were consumed only when a session's scope happened to touch them. `inbox/processed/` stopped 7/22 and **16 packets silently accumulated**, including a PROME readiness review and a DAEDALUS architecture audit carrying a dangerous defect.
Outbound had the mirror gap: `outbox/delivered/` was *defined* but **nothing ever walked it — 11 packets sat top-level 7/8→7/27 with their loops closed** (LIQUID/FALCON/TERRY had all replied; the PROME fill-outcome had landed).
**⚠️ Why it is not tidiness:** a consumed-but-unarchived packet is **indistinguishable from one never read**, and an undelivered-looking outbox manufactures "did they ever get this?" ambiguity for every counterparty. **The archive state IS the answer to "who knows what."** `[[finding_delivery_check_is_not_a_knowledge_check]]` · `[[finding_canonical_surfaces_stale_inbox_carries_live_state]]`

---

## 2026-07-28 — THE PENDING-ROW GUARD {#pending-guard}

**Live rule → `CLAUDE.md` boot step 6c.** Record only.

Born from a live position that sat **mis-stated as un-filled for three days** [7/27] on the canonical trade surface. Re-earned immediately: on 7/28 DAEDALUS found the *same* contradiction still live in the TRADE header, a TRADE narrative line and `NEXUS_BRIEF.md:61` — **surfaces my own 7/27 note had DECLARED fixed.**
**A remembered ritual is not a check** (`[[finding_mechanize_the_cap_not_the_ritual]]`), and **a partly-fixed defect that has been declared fixed is worse than an open one, because the declaration stops anyone looking** (`[[finding_record_of_an_action_is_not_the_action]]`).

---

## 2026-07-28 — THE SCHEDULED-GRADE CHECK WAS WIRED {#cot-grade}

`cot_grade.py` had existed since 7/17 **with ZERO references in `CLAUDE.md`**, so nothing durable told a fresh session to run the grader built for exactly this purpose [DAEDALUS W1]. **A tool nobody is told to run does not exist.**

---

## 2026-08-04 — MISC STRUCTURAL {#misc}

- **EXECUTE is deliberately UNNUMBERED.** It collided with closeout step 7, so "step 7" was ambiguous. **Closeout keeps 7–14 because those ARE cited by number** — `step 12` = the NEXUS fold, `step 11` = SCRATCH. **Do not renumber.**
- **STATUS overflow archives to `workbook/STATUS_archive_*.md`** — the pattern actually in use. *(Corrected 2026-07-30: this instruction previously named `domain/sources/`, **which does not exist and never has**. A boot instruction naming a nonexistent path is a silent no-op — the archive step reads as covered and isn't.)*
