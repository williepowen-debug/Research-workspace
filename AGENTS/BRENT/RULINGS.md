# BRENT — RULINGS & DECISION RECORD

**Created 2026-08-05 (Will-approved).** **This file is NOT read at boot.** It is the dated record of *why* the operating docs say what they say — read on demand, when you are about to change a rule, or when you want to know whether a decision was deliberate.

> ### ⛔ **WHY THIS FILE EXISTS — AND WHAT IT IS NOT ALLOWED TO BECOME**
> **Measured 2026-08-05:** the RAV state-replacement pilot's WP4 was *"flatten human boot,"* and it succeeded on steps (31 → 24) while `CLAUDE.md` **grew 243 → 252 lines / 36.9 → 38.9 KB.** The BOOT section carried **9 human actions and 18 lines of rationale prose.** Hot context across the five boot-read files measured **317 KB**, of which **286 lines carry a date** and **66 carry RETIRED/SUPERSEDED/CORRECTED/DEFECT.**
> **★ THE MECHANISM: SPECS GET REPLACED; THE PROSE ABOUT THE REPLACEMENT ACCUMULATES.** Every incident deposited a dated *"here is what was wrong and why"* block into the **operating** doc. Each was individually justified. Together they made the instructions a minority of the instruction file. **History and instructions were living in the same file — valuable as history, toxic as boot context.**
> **★ AND THE RETIREMENT RATCHET HAD A SCOPE HOLE:** adopted 2026-08-04 to oppose exactly this, it governs **state** (scripts, registry rows, checks) and **says nothing about prose.** Since adopting it, every change was an addition. **Words were never counted.**
> **⇒ THE SPLIT: operating docs carry what to DO. This file carries why.** Nothing was deleted in the split — **only moved out of hot context.**
> ⚠️ **THE DISCRIMINATOR, and it is the one thing to get right when moving a block here: does it CONSTRAIN A FUTURE ACTION (stays live) or RECORD A PAST ONE (moves here)?** **Do NOT sweep by "has a date."** Several dated blocks are *binding limits Will ruled must travel on the live spec* — e.g. *"this regime has produced ZERO genuine physical reopenings"* and TERRY's *"a firing gate carries zero thesis information."* **Those stay on the spec. Moving them here would be the exact failure this restructure could cause.**
> ⚠️ **This file has no length cap and needs none — it is cold. But it must never acquire an instruction.** If you find yourself writing "always do X" here, X belongs in `CLAUDE.md` or `TRADE.md`.


## R-2026-09-08 — BRENT cleanup approved and implemented

Will approved the six cleanup items in this session ("okay I approve these"). The cleanup separates current rules from history, repairs their decision-time readers and exposes advisory boot findings. No trading permission or numerical gate changed. The binding letters now live in TRADE’s linked SPECS_GATES / SPECS_OFFRAMP_ENTRY / SPECS_TRADE_RULES; [inventory](workbook/TRADE_OBLIGATIONS.md) records each disposition and the full before-image checksum.

Existing July 31 H1 announcement anchor resolves the stale per-tranche question. August 7/21 instrument retirements leave some persistence applicability unresolved; those letters travel intact with that limitation, rather than being silently applied or discarded. LESSONS and its index were reconciled together. Prediction first nine fields and scoring conventions were preserved. The incident pass records sourced corrections separately from unsuccessful current-state verification; old source dates remain old. The I-8 extension catches typed-field impossibility missed by the legacy-only check. Full validation and residual evidence debt: [cleanup report](setups/2026-09-08_cleanup-report.md).


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

## ⚑ 2026-08-07 — **THE DAY+2 LATENCY CEILING — REGISTERED AS A DESIGN RULE (Will-approved as proposed).** {#day2-latency-ceiling}

**THE RULE:** **No Stage-A ENTRY leg may require data that resolves later than day+2** (day 0 = the announcement/signature session). Any candidate leg resolving **day+3 or later is STRUCTURALLY DISQUALIFIED FROM ENTRY**, however good a discriminator it is, and belongs in the **kill-test / tranche-2 / continuation** role instead.

**WHY — LATENCY IS A CLIFF, NOT A SLOPE.** Measured on the Jun-17 analogue, Brent re-pulled from primary 2026-08-07:

| Entry discipline | Entry | 8-session | Best | Sign |
|---|---|---:|---:|---|
| Announcement-based (6/18) | $79.85 | **+10.92%** | +11.57% | ✅ |
| **Leg-C-gated — v5 as written (6/23)** | **$77.08** | **+7.07%** | +7.70% | ✅ |
| ~~Transit-gated — the retired leg (6/26)~~ | $71.99 | **−5.99%** | +0.58% | ⛔ **LOSS** |

**Brent fell −6.6% in the three sessions BETWEEN the last two entries.** The trade's entire edge lives in a **~3-session window between roughly day+2 and day+6.** ⇒ **two sessions of lag costs 3.85pp and KEEPS THE SIGN; five sessions costs the whole trade AND INVERTS IT.** **There is no smooth trade-off to tune along — the move happens INSIDE the gap, so a gate resolving on the wrong side of it does not degrade the trade, it REVERSES it.**

**⚑ WHY A RULE AND NOT A REMEMBERED LESSON — THE THREE-INSTANCE PROVENANCE.** The same error has now been shipped in **three separate ratified specs**:
- **v1 Stage-A (7/21)** — three verification legs with response times spanning **days-to-weeks** forced into ONE 3-day window.
- **Defect ② (v4, 7/31)** — the transit leg: a **day-0** trigger gated on a **day+5** confirmation. `{(i) AND (ii-A)}` inside 48h occurred on **0 of 2 analogues and 0 of 145 closure-regime days.**
- **DEPLOY GATE v2 (8/4)** — a **mixed-latency basket wearing a single window**: leg (a) daily, leg (b) minute ⇒ a **ZERO-MINUTE** execution window.
**A latency ceiling is the guard that would have caught all three AT DRAFT TIME.** It restates LESSONS #21(b)'s window-matching principle **as a number**, which is what makes it checkable rather than merely agreeable.

**⚠️ HONEST LIMITS, CARRIED VERBATIM FROM THE PROPOSAL AND NOT SOFTENED BY RATIFICATION:** **n=1** for the profitable analogue (Jun-17) · **Apr-17 cannot be re-run intraday** (5m history starts 5/11) · **the day+2 boundary is read off ONE event's price path, not base-rated across many.** **⇒ THIS IS A DESIGN CONSTRAINT, NOT A FITTED PARAMETER.** It says *where a leg may live*, never *what its level should be*. **If a future session wants day+2 moved, that requires base-rating across events — not a re-read of Jun-17.**

**Retirement ratchet: `supersedes: none`** — ADDS one design constraint; retires nothing. It is a **draft-time admission test for new legs**, not a runtime check, so it costs no boot attention.

*Proposal of record: `outbox/delivered/2026-08-07_to-PROME_optionA-defect2-ALREADY-CLOSED-plus-validation.md` §③ — proposed and ratified the same evening.*

---

## DEPLOY GATE — THE FULL LINEAGE (cooldown → v1 → v2 → v3) {#deploy-gate}

### ⛔ **2026-08-07 — WILL RULED: THE ARM IS RETIRED. THERE IS NO LIVE DEPLOY GATE.** *(six days ahead of the 8/13 expiry)*

**Terms of record, verbatim class:** `RETIRED 2026-08-07 by Will ruling, ahead of 8/13 expiry; R1 named-not-registered; frame-breaker + playbooks survive; 8/4 decline untouched.`

**BRENT recommended RETIRE (lean ~70%) in `outbox/delivered/2026-08-07_to-PROME_cot-adjudication-arm-disposition.md` §②; Will ruled the same day.** The arm expired **UN-DEPLOYED** with **`$0` ever at risk.**

**★ THE RULING'S LOAD-BEARING FINDING — AND IT IS THE ONE WORTH CARRYING FORWARD: THE GATE WAS NEVER THE CONSTRAINT.** Legs (a)+(a2) cleared on **5 of the last 5 sessions** (OVX closes 57.20 · 53.45 · 51.48 · 57.34 · **55.80** against the ≤**58.6245** line) **and the arm still did not fire.** The binding constraint was the operator's standing decline, not the spec. **A gate that clears daily and is declined daily does not produce a trade — it produces a daily [Approve] prompt.** ⇒ **when an arm fails to fire, first ask WHICH constraint bound; re-speccing a gate that was already open is work aimed at the wrong object.**

**The re-arm bar was measured, not asserted:** the **8/6 escalation** — the strongest new event of the window — took OVX to a **57.34** close, **−16.9% below the 68.97 post-arm peak and 11.63 index points short of re-ratcheting.** Over the arm's life OVX fell **68.97 → 55.80 = −19.1%** ⇒ **fillability improved; evidence did not.**

⛔ **EXPLICITLY NOT THE REASONS, RECORDED SO THEY CANNOT BE BACK-FITTED: THE CLOCK, AND A CHEAP ENTRY.** The arm was retired because the case never improved while the gate stood open — **not because time ran out.** *(BRENT refused the "it expires 8/13, so take it" argument on 8/3, 8/4 and 8/7; the retirement must not now be read as that argument winning late.)*

**NO RE-ARM CONDITION IS REGISTERED.** **R1** (OVX close **>68.97**, self-resetting, single-instrument, measured every boot) · **R2** (PortWatch transits **≤2/day ×3 consecutive**) · **R3** (the frame-breaker) are **NAMED CANDIDATES ON THE MEMO ONLY.** ⚠️ **R1 is the drift risk precisely because it is written, measurable and boot-visible — it is NOT a tripwire and must not be graded.** **Re-arming requires a FRESH Will ruling on the written, base-rated spec** (68.1% fire rate/20td, n=113 de-overlapped episodes — **preserved, not deleted; the expensive work is done**).

**SURVIVES the retirement:** the **FRAME-BREAKER carve-out** (confirmed destroyed capacity → deploys on leg (b) alone) · **Stage-A** · the **OFF-RAMP playbook** incl. the COT-conditioned sizing modifier. **Retiring the arm did not disarm the book's response to a real event** — that was the counterweight in the memo and it is the reason the lean was 70% and not higher.

**Will's 8/4 FILL decline is STANDING and is NOT revisited by this ruling** — two separate decisions.

**Registry effect, same day:** `GATE-V3-A` · `GATE-V3-A2` · `GATE-V3-B` all → `status=retired` (rows KEPT as the do-not-resurrect record per the retirement ratchet). **`GATE-V3-B`'s stale-stamp blocker cleared BY the retirement** — blocking rows **6 → 4**, registered tests **47 → 43**.

**⚠️ LEFT UNRULED ON PURPOSE, NOT DROPPED:** the **COT-band spec gap** (does the fuller-size branch **revert** on un-fire, or is it latched? does a band clearing by **1,512** against a **9,264** median weekly move need re-basing?) is **`WILL_QUEUE` row 35, needed-by ~8/14** — BRENT's own do-not-carry-past date. **Nothing applied.**

---

**Live spec → ⛔ NONE. `TRADE.md` §DEPLOY GATE v3 is now the RETIRED spec, kept as the dated record.** *(Was: the live gate, self-contained.)* Record only. **v2 was folded into v3 on 2026-08-05** — before that, reading the live gate meant reading two versions and applying the diff in your head.

**⛔ WHY THE ORIGINAL `{ratio <2.89 AND OVX <44.2}` COOLDOWN GATE IS GONE (2026-07-30) — and it is NOT the reason I first escalated.** I told Will the gate *"may be unfireable by construction."* **That was false: it was met on 50.4% of the prior year's sessions and last opened 7/06.** The real defect: **the gate and this arm's own trigger are MUTUALLY EXCLUSIVE BY CONSTRUCTION** — the arm arms on **escalation**, the gate opened on **calm.** Over 753 sessions the gate was open on **0 of 38 escalation days (0.0%)** vs **78.5% of all others**. **No threshold choice fixes an anti-correlation.** Secondary defect: it priced **vega** while LESSONS #15 mandates a **vertical spread precisely because a spread neutralises vega** — at spec moneyness the debit rises only **+13.5%** from the old line (44.2) to OVX 63.8 and **asymptotes above ~90% IV**, versus **+140%** for the naked call the plan bans. **The gate was correctly specified for the instrument this plan forbids.** → `[[finding_compound_gate_jointly_unsatisfiable]]`
**v2's three tightenings** shipped with that loosening per #21(b): ① the 20-td expiry (new) · ② the leg-(b) economics floor (new — v1 had no test of what the trade actually costs) · ③ the re-ratcheting peak (new).

**⛔ WHY v2 HAD TO BECOME v3 (2026-08-04) — an INSTRUMENT fact, not a preference.** **`^OVX`'s final intraday bar is 16:00** (7/31; 15:55 on 8/3) — **`^VIX` runs to 16:10 but OVX does NOT** — and **USO options close 16:00.** ⇒ v2's leg (a) became knowable at exactly the moment leg (b) became ungradeable. **The execution window was ZERO, not the 15 minutes assumed.** Deferring to the next open is circular (leg (a) is not banked, so N+1 would need N+1's close). **v2 was a MIXED-LATENCY BASKET WEARING A SINGLE WINDOW — the precise defect LESSONS #21(b) ratified a fix for on 7/29, which I then reproduced here on 7/30.**
**v3's two tightenings** per #21(b): ① leg (a2) is new — v2 required **ONE** reading below the line, v3 requires **TWO INDEPENDENT** ones ⇒ **on the evidentiary axis v3 is STRICTER**; ② clearance expires after one session and never accumulates.
**Base-rated before adoption** (LESSONS #21), `^OVX`+`BZ=F` 2007-07-30→2026-08-04, n=4,729, **113 de-overlapped episodes**: fire rate **68.1%**/20td · Brent entry slippage from filling one session later **median −0.04%** · OVX at fill **+3.3%** (second-order on a vertical, L15) · **P(max Brent +15% within 63d) 38.2% → 39.5%, +1.3pp ⇒ tail NOT degraded.** Leg (a2) in existence form **blocks 7.8%** of fire sessions; the strict "≤line at every moment" form blocks **66.2%** and was **rejected**.

**⛔ AND THE AUDIT THAT CLEARED v2 NEVER TESTED THIS.** My 8/2 premise-check returned *"THE GATE IS SOUND… NO SPEC CHANGE"* — base-rated on **daily closes**, i.e. **it silently modelled v3's cadence, not v2 as written.** It validated a gate nobody could execute. **A spec can pass every test of statistical merit while failing on its execution window.** **An all-clear is worse than no audit, because it stops anyone else looking.** → `[[finding_executability_is_a_separate_audit_axis]]`
⚠️ **Compounding:** when it bit on 8/3 I recorded PROME's 3.5h routing delay as the cause — **a COORDINATION failure masked a STRUCTURAL one.**
⚠️ **Unreconciled and flagged, not smoothed:** the v3 fire rate **68.1%** vs the 8/2 audit's **81.9%** — different overlap treatment (113 episodes vs n=79 arming days). **NEITHER is canonical**; the comparative v2-vs-v3 result is unaffected (identical episodes both arms).

**THE 8/2 PREMISE-CHECK — what it established (its live output is the MANDATORY PRE-FILL DISCLOSURE, now on the spec).** The concern: this arm is **long convexity**, leg (a) waits for **vol decompression**, what decompresses OVX is **de-escalation** — so the gate could open *precisely into the tape that kills the thesis*, with **no leg asking whether the premise is still alive. The factual half is TRUE: there is no abort leg.** **The harmful half is FALSE** — base-rated over 1,045 sessions (arming proxy Brent 1d ≥+3%, n=79): the gate fires **81.9%** within 20 td (median 10 sessions); the de-escalation tilt is real (**62.7%** of fires occur with crude BELOW its arming level, median **−1.85%**) **but it is the design intent working — it is buying the dip INSIDE a live crisis.** Cheaper vol (OVX median 55.0 → 47.8, −11.1%) and it **IMPROVES the right tail**: `P(max Brent ≥+15% within 63d)` **44.4% gated vs 35.3% ungated, +9.2pp** (42d: +10.1pp); positive at every arming threshold +2%→+5% and every decompression depth −10%→−20%. Cost of waiting ~**5.7%** of crude move, **paid for in vol and in tail.**
**★ THE COUNTERFACTUAL IS THE LESSON: had this been "fixed" on my framing, the repair would have TIGHTENED a gate adding ~+9pp of right-tail edge, with 9 sessions on the clock, on a hypothesis that fails its own base rate — the wrong repair to the wrong defect, exactly as in LESSONS #21(a). n=2 on that pattern.**

**Spec-sweep reconciliation of record (2026-08-02):** L21 honoured twice (base-rated jointly and conditional on the trigger state; direction-neutrality checked per #21(b)) · L11/L16 honoured (the disclosure asks leg-(i) INSTRUMENT status = the announcement-vs-delivery test) · L18/L19 honoured (rhetorical-vs-operational is what item (i) forces onto the packet) · L15 honoured, not overridden (vertical structure unchanged) · **L05 explicitly acknowledged.** Deliberately silent: L06 · L08 · L09 · L10 · L17.

**Proposal docs of record:** `setups/2026-07-30_LESSONS21a-cooldown-gate-respec-PROPOSAL.md` · `setups/2026-08-02_deploy-gate-v2-premise-audit.md` · `setups/2026-08-04_DEPLOY-GATE-v3-fillability-respec-PROPOSAL.md`.

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


---

## 📦 MOVED FROM `CLAUDE.md` — 2026-09-07 (DAEDALUS architecture review ACTIONs 10–11, Will-authorised)

> **These spans are RATIONALE, not instruction.** They were moved out of the boot-loaded charter to bring it under the read-cap budget; **every binding instruction stayed in `CLAUDE.md`, with a one-line pointer here.** Nothing was deleted. ⚠️ **If a rule appears ONLY here, that is a defect — report it: a rule that lives only in the cold record is a rule nobody executes.**

### R-2026-08-17 · ledger_staleness re-wired into boot (and its 2026-08-21 corrections)

   > ✅ **`scripts/ledger_staleness.py` — RE-WIRED INTO BOOT 2026-08-17 (Will-approved). Its own retirement condition was met, so this is that clause working as written, not an override of it.** ~~*"RETIRED from BRENT boot. Do not re-wire it without a live unfrozen surface for it to inspect."*~~ **The condition — a live unfrozen surface — is now satisfied by `REGISTRY.tsv`, `board_log.tsv`, `docket/CATALYSTS.tsv` and `refinery_damage/INCIDENTS.tsv`.** **What it buys: the two-clock `PAT-044` header on the TSV LEDGERS NAMED ABOVE had no reader on this desk after the retirement. A stamp nothing reads is a comment.** ⛔⛔ **CORRECTED 2026-08-21 (Will-authorised in-session; PROME ruling (c), packet `inbox/processed/2026-08-21_from-PROME_ledger-glob-RULED-*`). THIS SENTENCE PREVIOUSLY CLAIMED THE WIRING WAS "the measured root cause of `TRADE.md:3` carrying an 8/10 stamp over an 8/14 body — the THIRD instance of that class." THAT WAS FALSE WHEN WRITTEN AND IT IS THE DEFECT OF RECORD, NOT THE GLOB.** **`workbook/LEDGER_GLOB` deliberately scopes to TSV ledgers + `board_log.tsv` — a scope its own header records as Will-approved at creation — so `TRADE.md`, being markdown, was NEVER in it and the wiring never bought a reader for it.** ⚠️ **MEASURED COST OF THE OVER-CLAIM, 2026-08-21: boot rendered `✅ Ledger Staleness — OK` at 09:41 while `TRADE.md:3` sat ELEVEN DAYS STALE, carrying `USO $125.92 / Brent $87.85` against a live `$134.53 / $94.24`.** `[[finding_instrument_reports_clean_against_the_wrong_reference]]` — **a clean scan against the wrong referent has no error to notice, and the JUSTIFICATION is what told me the referent was covered.** ★ **THE TRANSFERABLE HALF: A FIX'S STATED BENEFIT IS A CLAIM, AND IT NEEDS THE SAME VERIFICATION AS THE FIX. I falsified the MECHANISM on 8/17 by running it three ways — and never once checked that the file the benefit sentence NAMED was inside the set the mechanism scanned.** ⚠️ **AND THE WIDENING BELOW ONLY FIXES HALF OF WHAT WENT WRONG ON 8/21 — carried per PROME rider ③: this check watches the STAMP (age), never AGREEMENT. The same surface also carried a `−36.0%` mark on an option leg that was `+41.7%` on the live chain — a FRESH figure that was simply WRONG, which no freshness check can ever catch** `[[finding_freshness_check_cannot_catch_a_fresh_lie]]`. **Marks are governed by pulling the LIVE CHAIN at every decision point (`RISK_RULES` #5), not by this script.** ⚠️ **TWO PRECONDITIONS, BOTH REQUIRED, BOTH VERIFIED BY RUNNING RATHER THAN READING — do not un-wire either: ① `workbook/LEDGER_GLOB` declares the real ledger set. The script's DEFAULT glob is `workbook/*.tsv`, which sees 6 files and MISSES all three ledgers that actually rot; wiring on the default would have produced a check that reports CLEAN because it is not looking. ② `boot.py`'s `FINDINGS_MARKERS` promotes its rc=0 to FINDINGS on a `STALE` marker — the script returns 0 EVEN WHEN IT FINDS STALE LEDGERS, so unmapped it would render ✅ OK forever.** ⛔ **The rc contract is NOT fixed in that script because it is a SHARED fleet script outside `AGENTS/BRENT/` — not mine to edit; flagged to PROME. The consumer-side mapping is the change that is mine.** ✅ **Both falsified 2026-08-17: clean→OK, `--days 1` (2 stale)→FINDINGS, missing-script control→FAIL (markers can never mask a real failure).** ⛔⛔ **CORRECTED 2026-08-21 — THIS LINE SAID `--days 14` AND THE REAL DEFAULT IS `30`.** The script's own DOCSTRING says *"threshold (default 14)"* while its argparse says **`default=30`**; I copied the docstring and never ran it. **A doc that disagrees with its code will be believed, because reading is cheaper than running.** ⚠️ **The point the line was making SURVIVES AND IS NOW SHARPER: it is an INHERITED default, not a chosen number, with no BRENT base rate behind it** `[[finding_inherited_default_threshold_is_a_silent_decision]]` — **and the inherited value is more than twice what I thought I had documented.** ⛔⛔ **AND IT HAS A MEASURED COST AS OF TODAY: `TRADE.md` was added to `LEDGER_GLOB` on 2026-08-21 to catch the 11-day staleness boot missed — and a counterfactual run of the pre-fix file shows it registers `+10d` and only trips at `--days ≤ 9`. Boot invokes the script with NO `--days`. ⇒ THE WIDENING IS INERT AT BOOT UNTIL A THRESHOLD IS SET, and setting one needs a base rate of the historical TRADE-vs-STATUS gap that nobody has measured.** ★ **Adding the PATH and adding the ALERT are two different changes; only the first is done. Full falsification record + the boundary sweep → `workbook/LEDGER_GLOB` amendment 2026-08-21.**

### C7 · the duplicated NETWORK CONNECTIONS table (retired 2026-09-07)

| Direction | Agent | What Flows | Priority |
|-----------|-------|------------|----------|
| **← HAWK** | Military ops, Hormuz status, sanctions, escalation tier | 🔴 |
| **← MARCO** | Trade policy / tariff impact on energy flows | 🟡 |
| **→ CARL** | Gas pump prices, heating oil, consumer energy burden | 🔴 |
| **→ LIQUID** | Energy HY OAS, E&P debt stress, energy credit contagion | 🟠 |
| **→ HENRY** | Oil-driven inflation inputs (energy PPI/CPI components) | 🟠 |
| **→ SAM** | Japan energy import costs, LNG spot prices | 🟠 |
| **→ HAWK** | Oil price levels + storage data for scenario framework | 🔴 |
| **→ REGINALD** | Energy loan exposure at regional banks (if discovered) | 🟡 |

### F3/F4 · KEY THRESHOLDS — the retired table's dated disposition record (2026-07-31)

### 📋 DATED RECORD — what the retired table held and where each row went (2026-07-31)

| Retired row | Disposition |
|---|---|
| Brent **>$100** · Brent **<$75** · **WTI-Brent >$5** · **Cushing <20M** · **HY energy OAS >400bps** · **US rig count +50 from trough (457)** | ✅ **Already in THESIS** — pure duplicates, dropped here. |
| **Brent >$120** — *demand destruction accelerates, Phase 2 approaches* | ✅ **MIGRATED to THESIS** as a dated entry. **Judged a LIVE watch:** `>$100` **fired 7/23**, Brent is ~$90, and this is the next pre-registered upside rung — **and it is measurable** (front-month Brent is pulled every boot). |
| **Gasoline crack >$30/bbl** — *pump surge → CARL alert* | ⛔ **RETIRED — F4, Will-ruled 2026-07-31. NOT migrated, NOT re-levelled.** It has been **breached for months** (crack **$58.25** 7/29 close, ~$48.4 intraday 7/30 = **60-95% above the line**) and is **not carried in `thresholds.py`**, so it alerted on nothing in either direction. **A permanently-breached tripwire is decoration.** ⚠️ **If a crack tripwire is ever wanted again it is a NEW REGISTRATION with base rates — not a re-level of this one.** |
| **VLCC rate >WS200** — *tanker super-cycle* | ⛔ **RETIRED — F3 judgment call, 2026-07-31.** **I have NO Worldscale/freight-rate feed anywhere in my kit** — verified: `thresholds.py` tracks **tanker EQUITIES (FRO/EURN/DHT) as an explicit PROXY**, never a WS rate; THESIS and STATUS mention VLCCs only in event prose. **This threshold has never been measurable and has therefore never once been evaluated** — F4's disease under a different ticker. **A real freight tripwire needs a Baltic/Worldscale feed first: new registration, not a migration.** *(The tanker-equity proxy already in `thresholds.py` is what actually gets watched, and it stays.)* |

**Conflict resolved in the same ruling:** the retired table said *"Brent <$75 = structural decoupling"* while THESIS says *"<$70 on confirmed DEMAND collapse; sub-$75 RETIRED as a break."* **THESIS governs.** *(Consistent, not a loss — sub-$75 decoupling is thesis-CONFIRMING per v5.0; only its status as a *break* was retired.)*



### R-2026-08-04 · why the KEY THRESHOLDS pointer went stale (RAV Risk #1 realized)

> ⛔ **REPOINTED 2026-08-04 (session 4) — AND THE STALE POINTER WAS AN ARTEFACT OF THE FIX ITSELF.** This block previously read *"THE CANONICAL THRESHOLD REGISTRY IS `thesis/THESIS.md`"* and cited `thresholds.py`'s docstring as its evidence. **Both were true on 7/31 and both went stale the same afternoon**, when the RAV state-replacement pilot moved the machine home to `REGISTRY.tsv`, deleted `thresholds.py`'s hardcoded tables and stripped THESIS's `Status` column — **without repointing the boot doc or the docstring it cited.** ⚠️ **A pointer that was correct when written is the hardest stale surface to see: the F3 ruling fixed the ownership question ONCE, the pilot moved the answer, and nothing re-asked it.** **This is RAV's Risk #1 realized — *"creates a new registry but leaves every old fact home live"* — found by reconciling the shipped branch against RAV's own plan, not by any check.**

### R-2026-08-17 · boot step 2b, the measured cost of the invisible Monday routine

2b. **Read the NEWEST `demand_destruction/data/monday_*.md`** — *(added 2026-08-17, Will-approved. **supersedes: none** — EXTENDS the step-2 read phase; no existing step covered it.)* **The Monday AUTONOMOUS routine writes a full market + geopolitical pull here and SELF-COMMITS it, on a schedule that does not coincide with your session.** ⛔ **NOTHING in this protocol pointed at that file, so its output was invisible to boot.** ⚠️ **Measured cost, 2026-08-17: the routine ran 09:55, I booted 08:27, and I wrote a STATUS block at ~11:xx off the older boot bar while a fresher and more complete pull sat committed in my own directory — carrying three Hormuz tanker attacks (8/13–8/15, Iran claiming responsibility), a ~5–6% mid-week crude move and a live tape I did not have.** **This is a READ-PATH failure, not a staleness failure: the routine did its job and filed correctly.** ✅ **It also runs an independent alert check against the registered lines — a free second opinion, and on 8/17 it agreed with mine on every line.** **If its run date is NEWER than your boot, it wins on tape; reconcile before writing any level to STATUS.**

### R-2026-08-04-positions · the charter Positions bullet (dollar-total staleness + the STNG error)

- **Positions:** **USO 35 shares** (the book's large undefended oil leg) · **USO Oct-16 135C ×2** · **USO Sep-18 150/165 spread** · **XLE Sep-30 65C ×2** — **5 live oil expressions, ~$5,131 at market** `[broker-verified 2026-08-04, Fidelity + Robinhood, Will-confirmed complete]` ⛔ **THAT DOLLAR FIGURE IS AN 8/4 BROKER VINTAGE AND IS NO LONGER THE BOOK — DO NOT QUOTE IT** (2026-09-06; PROME 9/2 packet §2 established it is HERE, in my own file, and VERIFIED-ABSENT from root `CLAUDE.md`, so it was mine to fix all along). **Own post-close chain pull 2026-09-02 put the four option/share legs at `$7,829.95` — ~$2,700 above this line.** ⇒ **`TRADE.md` is canonical for the money; this line carries the LEG SET only.** The five expressions named above are the durable fact; the dollar total is not, and a figure that must be re-verified to be quoted does not belong in a boot-loaded file. ⚠️ **Position truth is off-repo (Will/broker direct) — neither figure is a broker mark today.**. ⛔ **STNG IS NOT A POSITION — removed 8/4 after being carried in error 7/21→8/4.** It stays a **TRACKED TICKER** (a leg of the Stage-A tanker-liveness composite). **Tracking ≠ owning.** **`TRADE.md` is canonical; refresh here only when the broker record moves.**


### C1–C9 · charter corrections applied 2026-09-07 (DAEDALUS P3 / ACTION 10), superseded text

> ⚠️ **Each entry is the text AS I FIRST WROTE THE CORRECTION — verbose, with its own story attached.** That is the defect CODEX flagged the same evening: I spent the session applying READ_CAP rule 19 (*analysis goes to the cold record, never first into the hot file*) and wrote every repair's rationale straight into the charter and STATUS, pushing the charter 1,186 B BACK OVER budget. The rule was not hard to understand; it was hard to APPLY WHILE FIXING SOMETHING ELSE. Third recurrence in one session. `[[finding_a_correction_pass_is_unreviewed_work]]`

**C-a boot check count**

> **It runs every check registered in `boot.py`'s `CHECKS` list (9 as of 2026-09-07) — read the SUMMARY table it prints; do not trust a count written here, which is what went stale (said `six` at nine).**

**C-b the retired 250-line STATUS bar**

> ⛔ **STATUS.md is bounded by the READ-CAP BYTE BUDGET (32,550 B), not by a line count — the old `250 lines` bar was superseded and is retired 2026-09-07; verify with `scripts/read_cap_check.py --agent BRENT`.** Archive overflow to

**C-c frozen ledgers cited as live cross-reference targets**

> 2. **Cross-reference** — check `thesis/PREDICTIONS.tsv`, `workbook/REGISTRY.tsv` and `STATUS.md` § STANDING STATE for related vectors. ⛔ **NOT `KB.tsv`/`VX.tsv`/`FLOW.tsv` — all three are FROZEN (closeout step 8); citing them here contradicted that and is retired 2026-09-07.**

**C-e the obsolete 'do not process inbox' exception framing**

> ⚑ **Scope note (corrected 2026-09-07): this is NOT an exception to a “do not process inbox” rule — that rule was AMENDED 2026-07-28 and inbox TRIAGE is now boot step 6b. This lane is narrower than 6b: it is the VALIDATED, RECEIPTED `MSG-*` protocol.**

**C-f step 2b read only monday_*, hiding the friday/eia routines**

> 2b. **Read the NEWEST scheduled-routine output in `demand_destruction/data/` (`monday_*` · `friday_*` · `eia_*` — whichever is newest; ⛔ the step said `monday_*` ONLY until 2026-09-07 and the other routines were invisible to boot)**

**C-g the unenforced 100-line brief cap**

> (⛔ the `100-line` figure was provisional and is BREACHED at 145 lines as of 2026-09-07 — treat the READ-CAP byte budget as the real bound and re-cut at the next re-pin; do not cite 100 as if it were enforced)

**C-d two conflicting rules for outbox/**

> - HERMES is retired: deliver a signal by writing the `.md` packet directly to the target agent's `inbox/` (coordinators PROME/WALTER route). ⛔ **RECONCILED 2026-09-07 — this line and the §Outbox-Protocol opener gave two different rules for the SAME directory** (*"reserve `outbox/` for PROME-action requests"* vs *"Outbox is reserved for 🔴 acute, time-sensitive signals only"*). **ONE RULE, both cases: `outbox/` is for 🔴 ACUTE signals AND for PROME-action requests. Steady-state cross-agent flow goes through `NEXUS_BRIEF.md`'s SENDING/WAITING-FOR tables, never per-signal files.**

### R-2026-08-17-step10 · closeout step 10, why the TRACKER refresh is UNCONDITIONAL

> 10. **Forward-state maintenance.** **Catalysts:** `docket/CATALYSTS.tsv` is the source of truth (8 cols incl. `date_class`: confirmed/modeled) — prune fired rows past 1-week retention, add newly-discovered dated catalysts, revise modeled-date rows if STATUS projection shifted; the STATUS `📅 CATALYST CALENDAR` section is the human twin and **must not diverge in event SET**. Catalyst maintenance can be delegated to the [FASTOW](docket/FASTOW.md) sub-agent (spawn pattern: Agent w/ pointer to `docket/FASTOW.md` + `docket/FASTOW_MEMORY.md`). **Incidents:** log any new energy-infra strike to `refinery_damage/INCIDENTS.tsv` — facility-damage only per scope header (military ops/intercepts → HAWK); **verify against a primary source before logging** (LESSONS #1). ⚠️ **Before logging, check HAWK's ledger — it is the CROSS-THEATER one:** HAWK maintains a unified cross-theater energy-infrastructure strike ledger (`STRIKES.tsv` + `SUMMARY.md`) — **one table with a theater column, NOT per-theater silos.** My `INCIDENTS.tsv` is the facility-damage view; don't fork a parallel per-theater record or let the two drift. `[[project_energy_strike_ledger]]` *(embedded 2026-07-31 from PROME's Phase-2 memory-restructure packet — this row no longer auto-loads.)* **Operational tracker:** keep `demand_destruction/TRACKER.md` current if demand/Path-B data moved. ⛔ **TIGHTENED 2026-08-17 (Will-approved) — the CONDITIONAL was the defect. *(EXTENDS this existing clause; **supersedes: none**; deliberately NOT a new numbered step — 7–14 are cited by number.)*** **Its `📟 REGISTERED ALERT LINES` top block is a RUN-TIME CONTRACT read by three cloud routines, so it must be refreshed — or explicitly re-stamped SCOPED-PARTIAL with a re-verified/not-re-verified boundary — at EVERY closeout, whether or not demand data moved.** ⚠️ **WHY UNCONDITIONAL: the routines read that block on THEIR schedule, not yours, so "nothing moved on my desk" is not a statement about what they will publish.** **Measured 2026-08-17: the block sat 5 days stale (8/12 stamp) past its own 3-day tripwire, and its self-check — *"if Refreshed is more than 3 calendar days before your run date, say so and treat every level as UNVERIFIED"* — SILENTLY FAILED on the first run that ever required it.** **Falsified across all 18 archived runs: the word `unverified` appears ZERO times, every run; the prior 17 all sat 0–2 days behind a refresh, so the guard was never exercised and read as working because it was never asked.** ⇒ ★ **That guard is PROSE ADDRESSED TO A READER, not an executable check — re-wording it changes nothing, which is why the fix is this step and not better wording.** **Same silent-fallback-green class as the `thresholds.py` kill the same morning.** `[[finding_test_the_guard_not_just_the_guarded]]`


## R-2026-09-08 — receipt of existing position rulings, owner mirror applied

TERRY September 8 packet reconciled against its XLE exit and USO Rule-20 owner cards. Existing WQ-145/167/168 govern: October-call quantity one remaining; first-sale price permanently UNKNOWN/no re-ask; XLE September 9 open exit selected, broker receipt pending; September 18 spread HOLD. This is receipt/application, not a fresh ruling. The binding live mirror is `TRADE.md` §POSITIONS (live); TERRY retains implementation ownership. WQ-189/192 STAND DOWN unchanged.


## R-2026-09-08-OSPREY-owner-rules — received at batch 2 closeout

Late incoming owner notification: `inbox/2026-09-08_from-OSPREY_downgrade-path-IN-FORCE-Will-9-8-you-have-until-9-15-to-object-plus-three-rulings.md` reports Will’s approval of OSPREY’s downgrade path, withdrawal of its band re-centre, Channel-3 geography qualification and movement of the buyer-pullback limb to Channel 2. Binding owner text is **OSPREY CLAUDE.md, EXIT RULES §1b** and the owner’s named channel rules; the packet reports no mark moved. It gives consumers an objection window through **September 15** which does not suspend its rule. These are attributed owner changes, not newly authenticated here or a BRENT gate amendment. September 9 follow-up: read owner primary text and assess consumption/double-count implications before any BRENT use. The packet remains in inbox pending that source review and sender commit; no acknowledgement, objection or external send issued. BRENT’s separate frozen Q2 date remains unchanged.


## R-2026-09-09-maintenance — network rationale relocation

Nonbinding rationale moved verbatim from CLAUDE § NETWORK CONNECTIONS under the approved maintenance; topology authority remains there. No new ruling or route.

> ★ **WHY IT WENT, and it is not tidiness — MEASURED 2026-09-07: the table listed 8 routes and OMITTED BOTH `FALCON` AND `OSPREY`, while this desk packeted FALCON TWICE on 2026-09-07 (the Kylo/GATE-2 inputs and the war-risk-split answer) and tracks OSPREY's weekly Russian-seaborne print as a dated NEXT-SESSION item.** ⇒ **The desk was running live on two routes its own charter did not know about.** A hand-copied mirror of a canonical topology does not drift loudly; it drifts by OMISSION, and an omission is exactly what a reader cannot see. `[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]` *(Retired rows preserved verbatim in [`RULINGS.md`](RULINGS.md) § C7.)*

Additional nonbinding provenance moved from CLAUDE § KEY THRESHOLDS and § OUTPUT RULES; operative pointers and archive destination remain in CLAUDE.

> ⛔ **This pointer was itself STALE 2026-07-31 → 2026-08-04** — the F3 ruling fixed ownership ONCE, the RAV pilot moved the answer to `REGISTRY.tsv`, and nothing re-asked the question. **A pointer that was correct when written is the hardest stale surface to see.** 📖 Full account → [`RULINGS.md`](RULINGS.md) § R-2026-08-04.

*(Corrected 2026-07-30: this line pointed at `domain/sources/`, which **does not exist and never has** — `domain/` holds only `REFERENCE_TABLES.md` and `HORMUZ_TRANSIT_BASELINE.md`. A boot instruction naming a nonexistent path is a silent no-op: the archive step reads as covered and isn't. DAEDALUS flagged it 7/28.)*
