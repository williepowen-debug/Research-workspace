# NEXUS_BRIEF_SCHEMA — decision log + review history (COLD)

**Split out:** 2026-08-28 ~15:0x ET, by NEXUS's own `scripts/read_cap_check.py --agent NEXUS` measurement (schema was **42,103 B = 78% of cap, over the 32,550 B boot budget**).
**Source:** `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` §§6-7. **Integrity:** `crc32 = 3f13bf74` over the verbatim payload below. **Bytes: 20,074.**

> ⚠️ **VERBATIM — nothing reworded, re-dated or renumbered.** This is a **hot/cold split, not a rotation of dead content**: §6's decision rows are still cited by number (row 19 governs the compact-variant revert; row 8 the section priority; rows 20/21 amendments 10/11). **They are COLD because they are looked up on demand, not read at boot** — the live spec (§§1-5) is what a brief author needs in hand.
> **Lookup contract:** cite as `SCHEMA decision row N` and read it here. The live file keeps the pointer and the amendment-12 block.
> ⛔ **Never raise the read budget** (the instrument's own words) — this is the sanctioned remedy: two-state split, verbatim, crc-stamped.

---

## 6. KEY DESIGN DECISIONS (locked from review)

| # | Decision | Rationale |
|---|----------|-----------|
| 1 | Position info: structural only, no P/L | `[[feedback_position_cost_basis_not_authoritative]]` — marks rot fast; structural refs survive |
| 2 | Failure patterns: terse anchors, full scoreboard in PREDICTIONS | Anti-drift; single source of truth |
| 3 | Falsification: sub-bullet of NEXT DECISION POINT | Separate from CALIBRATION's view-uncertainty; different scope |
| 4 | RED output: fold into CALIBRATION as 1-2 lines, reference red/ log | Anti-bloat; anti-drift |
| 5 | Thesis version in header: optional | Some agents version (SAM v1.5.1), some don't |
| 6 | Canonical brief location: `AGENTS/<NAME>/NEXUS_BRIEF.md` | Predictable path enables mechanical sweep |
| 7 | Brief-default + raw STATUS fallback on triggers (a) (b) (c) | Mechanical stale-check (a) + judgment-based convergence/uncertainty drill-down (b) (c). Preserves NEXUS's catch-omissions function |
| 8 | Section priority under cap pressure | CROSS-DOMAIN > CALIBRATION-divergence > VIEW > NEXT DECISION > WATCH |
| 9 | Cap is measurement, not aspiration | Pilot SAM brief sets the cap; cap calibrates to heaviest real domain |
| 10 | Cap-burst on settled agent = fragmentation hypothesis | Investigative signal for sub-agent spinout, not auto-trigger |
| 11 | RECENT THESIS PIVOTS: required single-line in header | NEXUS R3 amendment 1. Pivot timing is often the leading edge of a convergence; version stamp alone insufficient. |
| 12 | Cross-agent tensions known to me: REQUIRED (not optional) | NEXUS R3 amendment 2. Optional fields decay silently; "None active this cycle" forces look each pass. |
| 13 | WATCH → FORWARD CATALYSTS rename; NEXT DECISION POINT carved as action-trigger subset | NEXUS R3 amendment 3. Disambiguates monitoring-list from agent-actioned move. |
| 14 | Status emoji semantics LOCKED to CLAUDE.md key | NEXUS R3 amendment 5. Fleet-wide comparability requires shared semantics. |
| 15 | Conviction decomposition OPTIONAL per agent | NEXUS R3 amendment 6. Forcing direction/timing/level creates fake decomposition for HAWK/BROCK-style domains. |
| 16 | Scope: Tier-1 agents only | NEXUS R3 amendment 8. Tier-2 spawn-as-needed agents skip the brief; NEXUS reads their STATUS directly when active. |
| 17 | Single SENDING table (no STANDING/THIS-CYCLE split, no drop-rule) | Will arbitration (against NEXUS amendment 4 drop-rule). Refresh discipline at session closeout owns freshness load. Instrument informally — revisit if SAM brief shows stale SENDING rows over 3-4 sessions. |
| 18 | **CROSS-DOMAIN WAITING FOR: "Expected by" column required** | **NEXUS R3 amendment 7** (raised post-pilot consumer review Sun Jun 7 PM). Lets NEXUS catch waiting-on-waiting deadlock at fleet level. Use date format for hard dates, condition format for open-ended waits. |
| 19 | **✅ COMPACT VARIANT blessed for utility/single-seam agents** | **NEXUS amendment 9 — RATIFIED, Will-approved 2026-07-31** (drafted same day; docketed 7/17, consumed-in-practice since). Utility/single-seam agents (WATT, MIDAS, AEOLUS, VULCAN — narrow domain, few live edges) may run a **"curated cross-agent sync" variant**: routing-table-FIRST (per-recipient SENDING rows = the whole body), no §VIEW/CALIBRATION headers required, header stamp + as-of + waiting-for retained. Rationale: for a 1-2-edge domain the full schema is scaffolding around an empty core; the compact form protects exactly the load-bearing section (CROSS-DOMAIN) the cap-priority rule already ranks first. Evidence: MIDAS 7/17 + VULCAN 7/30 graded exemplary-for-consumption in BRIEFS_MAP; ~6 weeks of NEXUS consumption with zero brief-gap fallbacks logged against variant briefs. Constraint: an agent grown to ≥3 persistent live edges or carrying a thesis version reverts to full schema. Ratification path: NEXUS-drafted as owner 7/31, Will-approved same day (R3 precedent honored — fleet-facing format change got Will's look). |
| 21 | **✅ `pin-follows-STATUS-HEAD` — the pin must EQUAL STATUS HEAD at commit time** | **NEXUS amendment 11 — RATIFIED 2026-08-07 by NEXUS SELF-RULING** under `AGENTS/DAEDALUS/BLUEPRINTS/DELEGATION_TIER.md` (adopted by Will in-session, forum slate S8). Supersedes amendment 10's timestamp check with a hash equality. **A CHECK on the obligation §4.1 already imposes — no new duty, and expressly NOT an added closeout step in any agent's instructions** (that propagation would fail test 1). Origin: LABOR, n=4 consecutive sessions, three stale pins in one multi-workstream session 8/7; measured cost = SHADE's 8/4 brief carrying "ARCC UNGRADED" five minutes after the grade landed, which NEXUS then carried on its board for three days. Full five-test grading + the anti-self-serving guard: §4.1 SELF-RULED block. First exercise of the tier. |
| 20 | **✅ Closeout ORDERING rule: brief fold = LAST write-back** | **NEXUS amendment 10 — RATIFIED, Will-approved 2026-07-31** (same-day: drafted from the Will-directed fleet brief audit). The brief is written as the session's final write-back — after the last STATUS write, immediately before git. Evidence: audit batches 1+2 found every CONTENT-STALE brief (5-of-5: WAL/CORAL/OSPREY/HAWK/BROCK) was a mid-session write followed by post-brief STATUS work, including a gate FIRE (OSPREY 7/24) and a prediction falsification (HAWK FLOW-13) landing minutes-to-hours after the brief; **zero agents skipped the refresh — all sequenced it wrong**, so the fix is ordering, not compliance. Checkable: brief commit time ≥ last STATUS commit time of the session. Applies to full and compact variants alike. Propagation: audited-5 notified in their audit packets; fleet-wide via PROME (packet 7/31). |

---

## 7. REVIEW HISTORY (Will → PROME → NEXUS → SAM iterations)

| Round | Reviewer | Key correction |
|-------|----------|----------------|
| R1 | PROME (initial) | Reframe: motivation isn't token reduction — it's compression-to-edge. Cap should be tighter. Reference, don't restate. Hash-fallback mandatory. Pilot before fleet. |
| R2 (this round, after Will pushback) | PROME (final) | **Type A vs Type B distinction is the resolver.** Within-domain misses NOT NEXUS's job; cross-agent connective tissue IS. Brief is *better* input than raw STATUS for Type B because comparison is easier in standard schema. CROSS-DOMAIN + CALIBRATION-divergence are load-bearing; protect under cap pressure. SAM-proposes / NEXUS-ratifies / Will-arbitrates is healthy org template. |
| R2 SAM corrections accepted | | (a) Q7 widened to triggers (a)(b)(c) per § 4.4; (b) connective-tissue-first design intent baked in; (c) explicit section priority; (d) CROSS-DOMAIN mechanism framing in SENDING table column; (e) optional cross-agent-tensions sub-bullet in CALIBRATION; (f) cap is measurement not aspiration |
| **R3 (Sun Jun 7 PM, post-NEXUS E-phase)** | **NEXUS (consumer)** | **6 amendments + 1 scope clarification:** Recent Thesis Pivots required; Cross-agent tensions required; WATCH→FORWARD CATALYSTS rename + NEXT DECISION carve-out; emoji semantics locked; conviction decomp optional; Tier-1 scope only. Will arbitrated to reject the proposed SENDING drop-rule (kept single table); applied 6 amendments + scope to schema. SAM drafted pilot brief at canonical path. |
| **Amendment 9 (2026-07-31)** | **NEXUS (owner, drafted) → Will (approved same day)** | **Compact "curated cross-agent sync" variant RATIFIED for utility/single-seam agents** (WATT/MIDAS/AEOLUS/VULCAN class): routing-table-first, no VIEW/CALIBRATION headers; header stamp + as-of + waiting-for retained; **revert condition = ≥3 persistent live edges OR a thesis version → full schema.** Origin: 7/17 BRIEFS_MAP observation (decision docketed, not forced); ~6 weeks consumed-in-practice with zero brief-gap fallbacks against variant briefs. Consumers notified by packet 7/31. |
| **Amendment 10 (2026-07-31)** | **NEXUS (owner, drafted) → Will (approved same day)** | **Closeout ORDERING rule RATIFIED: the brief fold is the session's LAST write-back** (post-final-STATUS-write, pre-git). Origin: Will-directed fleet brief audit 7/31 — 5-of-5 CONTENT-STALE briefs were mid-session writes with post-brief STATUS work; zero skipped refreshes. Sharpens §4.1's "every closeout" with the ordering constraint it lacked. Audited-5 notified in audit packets; fleet propagation via PROME. |
| **Amendment 11 (2026-08-07)** | **NEXUS (owner) — SELF-RULED, no Will gate** | **`pin-follows-STATUS-HEAD` RATIFIED.** First exercise of `AGENTS/DAEDALUS/BLUEPRINTS/DELEGATION_TIER.md` (Will-adopted in-session, forum slate S8; the blueprint's CHECK-versus-DO worked case is this amendment). Origin: LABOR n=4. **Routing correction on the record: NEXUS had itself routed this to Will as WILL_QUEUE row 38 on the amendments-9/10 precedent, and named that as its own error in `FORUM/2026-08-07_system-review/04_will-time-automation/03_NEXUS_delegation-tier-reply.md` §4 — the precedent was applied by SURFACE, not by KIND.** Five tests re-graded at ruling time, not inherited from the blueprint; the grading surfaced a scope constraint the proposal did not carry (no fleet-wide closeout-step propagation, or test 1 fails) and an anti-self-serving guard (do not cite a falling `stale` rate as brief-health evidence). |
| **R3 amendment 7 (Sun Jun 7 PM, post-pilot consumer review)** | **NEXUS (consumer review of pilot)** | **Pilot brief load-bearing test passed** ("would do Type-B synthesis pass without raw STATUS fallback"). 5 brief polish edits surfaced + 1 schema escalation: WAITING FOR "Expected by" column raised from brief-edit to schema amendment given fleet-wide cross-agent value. Brief edits applied: status one-liner trim to single claim; position info moved from VIEW to header; VIEW bullet 3 lead-with-synthesis rewrite; failure-pattern counts+IDs stripped for NEXUS consumption; 🔴🔴 → single 🔴+bold. |

---

## 8. OPEN ITEMS FOR NEXUS RATIFICATION — ✅ ALL RESOLVED (section closed 2026-07-31)

*All five June-vintage items were resolved in practice within weeks of writing; the checklist sat open-looking for ~8 weeks (found by the 7/31 closeout-doc audit — same dead-pending class as the PREDICTIONS past-trigger intro). Dispositions:*

- [ ] 🔴 ~~Section ordering — resolved by practice: consumed as-is across 20+ passes, no reorder need surfaced; cap-priority rule (decision 8) covers consumption order.~~ **STRUCK 2026-08-28 — THIS CLOSURE WAS WRONG (HOMER, 8/22, verified fleet-wide by NEXUS).** **Decision 8 is a TRIM rule — it governs what the AUTHOR DELETES under length pressure. Truncation is a READ rule — it cuts by POSITION, at the consumer, regardless of priority. A priority ranking and a physical ordering are different mechanisms and only the second determines what a reader receives.** The question was closed on the authority of a rule that does not reach it. **Measured:** HOMER's brief cuts at line 74, exactly where `## CROSS-DOMAIN` begins ⇒ **~12% of bytes lost, 100% of the routing content, at full compliance with the only length control the schema has.** ⚠️ **Why "20+ passes" could not have caught it: the consumer across those passes was NEXUS reading whole files deliberately, not an agent taking one truncated read at boot — the practice that certified the ordering never exercised the failure mode.** A validation defect, not a design defect, and the more dangerous kind: 20+ clean passes read as evidence. **Re-opened; resolves at amendment 12.**
- [x] (b)/(c) fallback triggers — **resolved YES-parseable**: two formal rollups (7/17, 7/28) instrumented them; zero refinement requests.
- [x] Brief path — **resolved 6/7**: `AGENTS/<NAME>/NEXUS_BRIEF.md` (agent-owned), locked as decision 6; mechanical sweeps run against it fleet-wide.
- [x] Cap ceiling — **resolved via SAM pilot**: cap-as-measurement (decision 9), calibrated to the heaviest real domain.
- [x] RECENT THESIS PIVOTS field — **resolved 6/7 as R3 amendment 1** (decision 11): required single-line in header.

*Open items: **ONE — amendment 12, PROPOSED 2026-08-28 and ESCALATED TO WILL (not self-ruled).** See the block below.*

*Prior open items: **NONE.** Amendment 11 (`pin-follows-STATUS-HEAD`, LABOR-originated n=4) was **RATIFIED 2026-08-07 by NEXUS self-ruling** under DELEGATION_TIER — decision row 21, record block in §4.1, digest row in `AGENTS/SELF_RULINGS.tsv`. WILL_QUEUE row 38 closes without a Will ruling. All prior items closed (amendment 9 ratified 7/31, row 19; amendment 10, row 20).*

### 🔴 §4.4 COMPANION DEFECT — **NO CANONICAL PIN TOKEN, AND A POINTER IS NOT A VALUE** *(found 2026-08-28; NEXUS's own defect, measured after publishing a wrong count)*

**§4.4 defines trigger (a) as comparing *"the STATUS commit hash in the brief header"* to STATUS HEAD and calls it *"mechanical / always fires."* It never specified the TOKEN that carries the hash.** Measured across all 26 briefs:

| Class | n | Detail |
|---|---:|---|
| **A — hash present, comparable** | **10** | BROCK · CARL · FALCON · LABOR · MARCO · ORACLE · OTTO · SAM · VULCAN · WAL — **in three different string forms**: `STATUS commit: \`h\`` · `STATUS commit \`h\`` (no colon) · `STATUS pin: \`h\`` · `STATUS-HEAD PIN: \`h\`` |
| **B — field absent** | **12** | AEOLUS · BOND · BRENT · HENRY · HOMER · LIQUID · MIDAS · RED · REGINALD · SHADE · WATT · ZHAO |
| **C — field present, VALUE absent** 🔴 | **4** | CORAL · HAWK · OSPREY · VIOLET — *"see `git log -1 -- …`"*, *"see session commit below"*, *"written this session, refresh at close"* |

⇒ **trigger (a) cannot fire on B + C = 16 of 26 = 62% of the fleet**, and a check keyed on any ONE literal string is **also blind to the class-A briefs written in the other forms.**

⛔ **Class C is the sharper half: a field PRESENT but carrying a POINTER instead of a VALUE defeats the consuming check AND passes a presence audit** — strictly worse than absence, which at least fails a coverage grep. *(This is VULCAN's "absent required field is untrippable by construction" one level deeper.)*

**RULED (form/invariant, NEXUS's own §4.4 — not fleet-facing, so not escalated):**
1. **Canonical token: `STATUS commit: \`<hash>\`` — that exact string, hash in backticks, 7+ hex.** Existing class-A variants are **grandfathered and must NOT be rewritten**; the canonical form is required going forward and any checker must accept the four known variants until owners next touch their headers.
2. **A pointer is not a pin.** *"see `git log …`"* / *"refresh at close"* **does not satisfy §4.4** — if the hash is unknown at write time, Amendment 10 (fold LAST) already puts the fold after the STATUS write, so the hash IS knowable. Write it or say `STATUS commit: NONE (reason)` so it fails loudly.
3. **Any pin sweep reports COVERAGE and CLASS (A/B/C), never a bare defect count** — a rate over a population the instrument cannot see is not a rate.
4. ⚠️ **Detector rule, from how this was found: never publish an "N lack X" figure off a single string grep. Sample-re-read the hits first** (`[[finding_scan_keyed_on_naming_reads_local_form_as_absence]]`). Two detectors here disagreed on **7 of 26 desks** while their totals differed by **one** — the near-agreement was the trap.

*Origin: VULCAN raised the class n=1 (8/21); NEXUS ran the test and published **15 of 26**, which was wrong in composition on 7 desks; LABOR's 8/28 re-pin — a CORRECT pin my sweep scored as missing — exposed it within the hour. Corrections issued to VULCAN, BROCK, HOMER, PROME.*

### ⚠️ AMENDMENT 12 — **PROPOSED 2026-08-28, ESCALATED TO WILL VIA PROME. NOT RATIFIED. ⛔ NOBODY REORDERS UNTIL WILL RULES.**

> **Proposal: extend amendment 9's routing-first ordering to the FULL variant — `CROSS-DOMAIN` above `VIEW`/`CALIBRATION`.** Zero new obligations, zero new text, no content changed; it aligns physical order with the priority the schema already declares. **Precedent: amendment 9's own ratification rationale, applied to the population it excluded.**
>
> **Origin:** HOMER packet 2026-08-22 (finding HOMER's; truncation measurement DAEDALUS's). **Sharpest supporting fact:** amendment 9 reasoned out the correct ordering on 7/31 and **granted it to WATT/MIDAS/AEOLUS/VULCAN — the 1-2-edge agents with the LEAST routing content to lose — while the full variant, carried by the agents with the MOST, kept the inverted order.** The fleet already had the fix, in the variant that needed it least.
> **Escalation call (NEXUS, 2026-08-28):** a fleet-facing format change gets Will's look by amendments 9/10's own precedent (and R3's before them). This one re-orders every full-variant brief. **Not taken under DELEGATION_TIER self-ruling.**
> **Coupled ruling:** VULCAN's amendment-9 **revert condition is MET (decision row 19) but execution is STAYED** — VULCAN's brief is almost entirely CROSS-DOMAIN and currently routing-first, so a revert under the present order would push its routing content BELOW the truncation cut. **The defect makes a compliance-correct action harmful.** Revert executes after 12 is ruled, either way.

### ✅ AMENDMENT-12 WATCH — **GRADED `MISSED` 2026-09-02, ON ITS OWN LETTER. FINAL.**

> 🔒 **GRADE OF RECORD (added 2026-09-02, WQ-105 ACTION (a)).** **Verdict: `MISSED`.** **Anchor:** PROME `PROME/proposals/2026-09-01_wq-batch-RULED.md` row 105, Will 2026-09-01 17:22 ET — *"approve all of those with your recs."* PROME's ruling, verbatim in intent: *"The amendment-12 watch prediction (opened 8/07, due 9/18) is graded MISSED on its own letter. The falsifier said 'if a twelfth amendment is PROPOSED' — it was proposed 8/28. **No grader discretion on 'proposed' vs 'accreting text'.**"*
> **Consequence clause DISCHARGED in the same ruling:** amendment 12 **ADOPTED** as a zero-text defect repair **AND** the schema-amendment **CAP adopted in the same word** — *"the accretion question is answered by the cap, not by declining a valid fix."* Both are encoded in `templates/NEXUS_BRIEF_SCHEMA.md` (§2 order + §4.1 entry + **§4.6 CAP**) on 2026-09-02.
> ⚠️ **What NEXUS got wrong, recorded because it is the transferable part:** this desk **had the resolver and did not run it.** The falsifier fired on 8/28 by its own plain letter and NEXUS wrote it up as *"the consequence clause, and I am NOT ruling it myself"* — correct on the consequence, **and it deferred the GRADE along with the ruling.** The grade needed no authority; only the consequence did. ⭐ **Escalating a decision does not escalate the measurement that precedes it — grade first, then escalate.**

*(Prior header, superseded 2026-09-02: "🔴 AMENDMENT-12 WATCH — RESOLVED EARLY 2026-08-28: THE PREDICTION FAILED, 21 DAYS BEFORE ITS GRADE DATE")*

**The registered prediction** (opened 8/07, `FORUM/2026-08-07_system-review/02_repair-burden/06_NEXUS_canon-mass-reply.md`): DAEDALUS's discriminator held that **amendment 11 — the only FORMAT rule in the set — ENDS its class**, while the ten RECOGNITION amendments keep generating successors. **Registered falsifier: *"Grade 2026-09-18: if a twelfth amendment is proposed, the prediction fails and the schema is an accreting surface that needs a cap rather than another rule."***

**A twelfth amendment was proposed on 2026-08-28. ⇒ THE PREDICTION IS FALSIFIED.** And it fails in the sharpest available way: **amendment 12 is itself a FORMAT/ordering rule — a second member of the class the discriminator said was closed** — not a recognition-class successor.

⚠️ **DATE-KEYED-SCANNER DEFECT, caught here:** the grade was keyed to **9/18**, so a due-date scan run any time before then would have read this as all-clear while the resolver had already fired. `[[finding_date_keyed_scanner_cannot_see_an_early_resolver]]`. **A registered prediction needs a resolver that fires on the EVENT, not only a date to be checked on.**

⚠️ **The consequence clause, and I am NOT ruling it myself.** The falsifier's own words are that the schema *"needs a cap rather than another rule"* — which is an argument **against the very amendment that triggered it.** There is a real case that 12 is the one class that does not accrete (it adds no text and no obligation; it MOVES existing sections), and there is an obvious objection to me making that case: **arguing my own amendment out of the falsifier my own amendment fires is exactly the configuration Disc-J §5 says a grader should not be trusted on.** ⇒ **Routed to Will and DAEDALUS with the amendment, unresolved by me: does a purely-ordering amendment count as accretion?** Both the prediction's failure and this question travel in the escalation packet. **If the answer is "it counts," then the correct fix is a schema cap and amendment 12 should be declined even though its finding is valid** — and I will take that.

*⚠️ Original watch text, for the record — **Amendment-12 watch opened 2026-08-07.** The standing question from `FORUM/2026-08-07_system-review/02_repair-burden/06_NEXUS_canon-mass-reply.md`: DAEDALUS's discriminator predicts that amendment 11 — the only FORMAT rule in the set — ends its class, while the ten RECOGNITION amendments keep generating successors. **Grade 2026-09-18: if a twelfth amendment is proposed, the prediction fails and the schema is an accreting surface that needs a cap rather than another rule.** The tier's own falsifier runs in parallel: one Will reversal of any self-ruling by 2026-10-06 narrows or kills the tier.*

## §A12 — 2026-09-07 rotation from the HOT schema (verbatim; rotated to hold §§1-5 under the 32,550 B read budget after §4.1-R was added)

*(crc32 139898325, 385 B)*

  - **Measured cost of the gap, this file's own consumer:** SHADE's brief was folded ~11:15 on 8/4 carrying "ARCC pre-reg UNGRADED/overdue" — **five minutes after that grade landed at ~11:10** in the same session. NEXUS read the brief on 8/7 and wrote the stale claim onto its board in two places, where it sat three days as a false accusation against a desk that had done the work.

*(crc32 409567714, 331 B)*

  - Origin: LABOR, flagged **four consecutive sessions** (8/5→8/7); the pin went stale three times in one multi-workstream session on 8/7. Amendment 10 is an ORDERING rule, and ordering alone does not survive a second STATUS write in one session — a distinct, real residual from the 5-of-5 evidence that produced amendment 10.

*(crc32 2715162176, 611 B)*

  - **Origin: HOMER's truncation defect, accepted verbatim.** §1's section-priority list has ranked **CROSS-DOMAIN #1 — "protect this section first"** since R1, and the §2 layout put it **third**. So every truncation, cap-trim, partial read or context-window cut removed **the highest-value section first**, and did so silently. **The schema's own stated priority and its own layout disagreed, and the layout is what executes.** ⭐ `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` in its structural form: a priority written in prose is not a priority until it is the order of the file.
