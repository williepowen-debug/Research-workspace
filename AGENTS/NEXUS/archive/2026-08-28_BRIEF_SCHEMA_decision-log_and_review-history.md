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

## §A13 — 2026-10-24T16:19:07-04:00: Stage-2 repair of the HOT schema (Will-authorized 2026-10-24 16:06 ET). The pre-rewrite file was 32,443 B, crc32 469cd368 over the whole file as committed at 8678bec2a. Eight verbatim blocks below (crc32 over each block body, lines joined by \n, no trailing newline). Every governing rule they carried is restated in the hot file; what moved is history, superseded text and the 2026-06 proposal.

### §A13a — the superseded amendment-11 header text (old line 8) (crc32 80767657, 1,140 B)

> **SUPERSEDED 2026-08-07:** *"**ONE amendment PENDING (Will-gated): proposed amendment 11 — `pin-follows-STATUS-HEAD`** (the brief's STATUS pin must equal STATUS HEAD *at commit time*, re-pinned after any same-session STATUS re-commit — an invariant checked at commit, not an ordering remembered). Origin: LABOR, flagged **four consecutive sessions** (8/5→8/7): amendment 10 is an ORDERING rule and ordering alone does not survive a second STATUS write in one session — on 8/7 the pin went stale three times in one multi-workstream session. NEXUS endorses (the amendment-10 audit's 5-of-5 evidence was about ordering; LABOR's n=4 is about re-commits — a distinct, real residual). **Not ratified — amendments 9/10 precedent: fleet-facing format changes get Will's look. Routed via PROME.**"* — preserved verbatim per DELEGATION_TIER rider R2. The routing judgment in that final sentence was itself the error the tier corrected: the amendments-9/10 precedent was applied **by surface** (it touches the brief format) rather than **by kind** (9 and 10 changed what a brief IS; 11 only checks a requirement §4.1 already imposes).

### §A13b — the 2026-06-07 Tier-1 scope list with its 7/22–7/31 annotations (old line 13) (crc32 b8c3f713, 807 B)

**Scope:** required for Tier-1 active agents (CARL, REGINALD, OZK, SAM, RED, BROCK, LIQUID, HENRY, HAWK, BRENT, VIOLET, WALTER). Tier-2 spawn-as-needed agents (LABOR, HERMES, DARWIN, ZHAO, etc.) skip; NEXUS reads their STATUS directly when active. *(⚠️ Scope list is 2026-06-07 vintage, kept verbatim because the schema is LOCKED — the LIVE coverage index is `AGENTS/NEXUS/BRIEFS_MAP.md`, which carries the count; **no brief count is stated here** [the 7/22 annotation's bracketed "23" had itself rotted by 7/31 — the anti-rot note re-introduced the rot; de-hardcoded per the same-day CLAUDE.md census fix]. HERMES/DARWIN dropped 6/27; LABOR promoted to the Tier-1 read-set; WALTER/OZK/SHADE remain brief-less by design. Annotation added 2026-07-22, amended 2026-07-31; schema mechanics unchanged.)*

### §A13c — §4.1-R rollout state at adoption + the VIOLET/OSPREY open question (old lines 159–160) (crc32 2be4f9b2, 1,470 B)

**Rollout state at adoption, VERIFIED at the artifacts 2026-09-07 (not relayed):** 18 briefs carry both sections; **4 conformant (VULCAN · HOMER · LABOR · and the schema's own §2 layout)**, **14 `pre-A12`** (SAM · FALCON · OTTO · BRENT · CARL · BROCK · RED · REGINALD · HAWK · HENRY · ZHAO · LIQUID · CORAL · MARCO), **8 `n/a`** (no `## CROSS-DOMAIN` header: MIDAS · BOND · WAL · AEOLUS · WATT · SHADE · ORACLE, plus VIOLET and OSPREY which carry `## VIEW` but no `## CROSS-DOMAIN`). ⚠️ **DAEDALUS's packet counted 15 `pre-A12` including LABOR; LABOR reordered at `5ee78189c` (2026-09-07 12:27 ET) between that measurement and this one, taking `CROSS-DOMAIN` from byte 55,629 to byte 2,952 — so the 🔴 set halved from two to one while the packet was in flight.** `[[finding_directive_overtaken_between_authorship_and_delivery]]` — the target was re-measured before acting, and that check is what removed 13 of the 14 packets this ACTION would otherwise have generated.
🟡 **Separate question, NOT adjudicated here and owed to a later pass:** VIOLET and OSPREY carry `## VIEW` with **no `## CROSS-DOMAIN`**, which matches neither the FULL variant nor amendment 9's COMPACT variant (COMPACT is defined by having *no VIEW/CALIBRATION split*, §4.1 amendment-12 note). They are marked `n/a` on the conformance cell rather than silently counted as compliant — **`n/a` here means "the amendment cannot apply," never "this brief is fine."**

### §A13d — the amendment-11 SELF-RULED five-test record (old lines 173–179) (crc32 dbafafcb, 2,351 B)

**SELF-RULED 2026-08-07 (DELEGATION_TIER):** May NEXUS, as schema owner-of-record, ratify amendment 11 itself rather than routing it to Will?
→ Yes — ratified as an INVARIANT, expressly NOT as an added closeout step in any agent's instructions. Tests 1-5 PASS. Riders: R1 (dated), R2 (superseded header text preserved verbatim above), R3 (n/a — no confidence, probability or weight moved in this edit).
- **Test 1 SCOPE — PASS, and it is the binding one.** The ruling changes one file inside `AGENTS/NEXUS/`. It passes under the tier's CHECK-versus-DO refinement *because §4.1 already requires the hash stamp*; amendment 11 makes an existing obligation checkable, it does not create one. ⚠️ **This is why the ruling carries a scope constraint: if amendment 11 were ever propagated as "every agent adds a step to its closeout doc," it would change ~26 files outside this directory and test 1 would FAIL.** The invariant is enforced at the check, not by fleet-wide instruction edits.
- **Test 2 REVERSIBILITY — PASS.** Undoing it edits this file only. The `AGENTS/SELF_RULINGS.tsv` row is an append-only audit record; a reversal appends, it does not delete.
- **Test 3 NO-CAPITAL — PASS.** A commit-time equality check on a pointer. It gates, sizes, prices, selects strikes for, and sets exits for nothing.
- **Test 4 ANTI-SELF-SERVING — PASS, with a guard recorded rather than assumed.** The ruling makes NEXUS *easier* to catch being wrong (the SHADE class is exactly what it detects) and makes no threshold easier to satisfy — the fallback rollup's decision rule keys on `brief-gap` rate, which this does not touch. ⚠️ **The self-serving edge, named:** a falling `stale`-cause fallback rate after this ships would make NEXUS's own brief-health instrument look healthier. **NEXUS will not cite a post-amendment-11 `stale`-rate drop as evidence of brief quality** — it is a real improvement in pin accuracy, not a measurement of content.
- **Test 5 DATA-VS-INSTRUMENT — PASS.** The subject is whether a pointer in NEXUS's own artifact equals the head of the file it points at: a property of this instrument, not of the world. It is not revision handling, vintage, publication cadence, unit base, or weekday convention, and no second authority could rule it differently (contrast MIDAS L-15, which is fleet-wide by subject).

### §A13e — §4.2 cap discipline — the 2026-06 pilot text (old lines 184–188) (crc32 856f6494, 679 B)

### 4.2 Cap discipline — HISTORICAL PILOT; superseded by §4.5

> - **No fixed cap until pilot measurement completes.** The SAM pilot brief sets the empirical ceiling for the heaviest real domain. If SAM compresses cleanly to 50, cap is 50. If SAM bursts to 95, cap is 95 (not "force-trim SAM").
> - **Cap is calibrated to the heaviest real domain, not picked aspirationally.**
> - **Cap-burst on a settled agent = fragmentation hypothesis** (not an auto-trigger). If SAM consistently bursts after pilot calibration, that's a signal to investigate whether SAM's domain has fragmented and warrants sub-agent spinout (like OZK from REGINALD). Investigation, not automatic action.

### §A13f — §4.5 historical pilot text + the 2026-08-28 100-line-ceiling ruling paragraph (old lines 223–230) (crc32 ae5055f0, 1,985 B)

**Historical pilot text — superseded 2026-08-28; 100-line ceiling UNENFORCED:**

> - Hard ceiling: pending pilot measurement (provisionally 100 lines; revise after SAM pilot).
> - Headers, separators, section markers count.

Root `CLAUDE.md` §Data Hygiene's byte budget still binds alongside amendment12's section order. No new cap or §4.6 re-spec is installed.

> ⚠️ **RULED 2026-08-28 (NEXUS, on VULCAN's §4.5 ask + HOMER's ordering packet): THE 100-LINE CEILING IS ON THE WRONG AXIS AND IS NOT ENFORCED. ✅ **AMENDMENT 12 IS NOW RULED (2026-09-01) — the ordering fix shipped; the ceiling remains UNENFORCED and the binding control is POSITION, not length (§2 order + amendment 12).** 🔒 **And it can no longer be fixed by a thirteenth amendment — a line/byte-axis re-spec is now RE-SPEC-SITTING work under §4.6.**** Measured fleet-wide this session (all 26 briefs): **12 of 26 are over the cap** — it is not binding, it is being ignored by half the fleet — and **line count is nearly uncorrelated with byte load**: `WATT` 37 lines / **20.4 KB** (550 B/line) vs `OSPREY` 75 lines / **11.5 KB** (153 B/line); `SHADE` 42 lines / 22.5 KB; heaviest are `SAM` 318/105.9 KB, `HOMER` 165/94.7 KB, `VULCAN` 187/92.8 KB. **A brief can sit 60% under the cap and carry more bytes than one twice over it.** ⛔ **A byte cap alone is the WEAKER fix and is NOT adopted** — HOMER flagged against its own interest that a cap on the wrong axis *rewards compression into longer lines*, and the fleet's highest B/line figures are all short files, which confirms it. **No agent is to cut content against this line cap — it is not enforced, and amendment 12 (ruled 9/1) fixed the real defect by ORDER instead** (VULCAN was told so explicitly at 187 lines; ✅ **VULCAN's held revert is RELEASED this session — its condition was MET, and under the new order it no longer pushes routing below the cut**). The binding control is POSITION, not length — see the §6 strike below.

### §A13g — §4.6 'why a cap answers accretion' rationale paragraph (old line 253) (crc32 d8f2470f, 505 B)

**Why a cap answers accretion better than declining the fix (PROME's ruling, adopted verbatim in intent):** twelve amendments arrived because each one was individually correct — including amendment 12, which repairs a defect that made the schema cut its own most valuable section first. **Declining valid repairs to control accretion trades a real defect for a tidy count.** The cap puts the pressure where it belongs: on the **13th** change, which must now buy a full re-derivation rather than a rider.

### §A13h — §5 INTEGRATION WITH NEXUS — the 2026-06 proposal (old lines 259–287) (crc32 0ffeaf0e, 1,412 B)

## 5. INTEGRATION WITH NEXUS — HISTORICAL PROPOSAL; ratification superseded by header

### 5.1 NEXUS BOOT change

Current NEXUS BOOT step 6: "read each agent's STATUS.md headers, first ~30 lines... do NOT read full STATUS files unless flagged."

Proposed amendment (post-ratification): **"read each agent's `NEXUS_BRIEF.md`. Read raw STATUS only when fallback trigger (a), (b), or (c) fires per § 4.4."**

One-line change to the WHAT YOU READ table. Surgical integration.

### 5.2 NEXUS ratification

This schema is a **proposal** until NEXUS reviews and ratifies. NEXUS owns the interface — the consumer of the brief should sign off on the format before fleet adoption. Ratification scope:

- Schema sections + ordering
- Section design notes (§3)
- Maintenance discipline (§4)
- Fallback triggers (§4.4)

NEXUS is mid-E-phase with a Mon 6/9 deadline. **Do not interrupt E.** Ratification window opens post-E.

### 5.3 Rollout sequence

1. **NEXUS ratifies** (post-E). Iterations expected.
2. **Pilot 1:** SAM brief consumed by NEXUS on 1-2 synthesis passes. Surface gaps. Iterate.
3. **Pilot 2:** add one tight-domain agent (HENRY or BRENT — single-channel domains) to stress-test the schema at the *light* end.
4. **Iterate** on schema gaps surfaced by both pilots.
5. **Fleet rollout:** other 11 agents draft briefs against the iterated schema. Add brief write-back to each agent's SPAWN PROTOCOL.

### §A13i — §4.1-R as written 2026-09-07 — heading, rule, three parts, standing consequence (old lines 147–157) (crc32 4f7a5293, 2,767 B) — added after the independent read found these passages restated but not archived

#### 4.1-R 🆕 ROLLOUT RULE — the missing half of every amendment (added 2026-09-07; DAEDALUS packet 2026-09-07, `8df8756d2`; NEXUS owns the schema and rules this itself under the 2026-08-07 DELEGATION_TIER block below)

> **A schema amendment that changes what a WRITER does is NOT IN FORCE when it is ratified. It is in force when every full-variant brief conforms, and until then its state is `RATIFIED-NOT-ROLLED-OUT` and its protection is ZERO.**

**Three parts, and the owner is named for each — the defect being repaired is that amendment 12 had a surface list and no owner (DAEDALUS PAT-139 (d)).**

1. **TRIGGER — each desk reorders at its NEXT RE-PIN. This adds NO new duty:** §4.1 already makes the fold mandatory every session, so the reorder rides a write the desk is already performing. A desk is non-conformant only after its next re-pin, never before it.
2. **OWNER — NEXUS**, and the obligation is discharged by **an `order` conformance cell in `BRIEFS_MAP.md`** (`A12` · `pre-A12` · `n/a`), *not* by a packet round. ⚠️ **This is a deliberate DEPARTURE from DAEDALUS's recommendation** (*"NEXUS packets every full-variant brief owner once"*), and the reason is `[[finding_hand_fixing_named_rows_is_not_fixing_the_class]]`: **a one-time packet to 14 owners is a SAMPLE that rots the moment a 15th brief is created, while the map is re-read at every drift pass and cannot silently go missing.** The map is the mechanism; packets are the escalation.
3. **ESCALATION — NEXUS packets ONLY the desks whose non-conformance is CURRENTLY LOAD-BEARING**, defined as: **the byte offset of `## CROSS-DOMAIN` exceeds the single-read cap (54,250 B, READ_CAP rule 1).** 🔑 **This is the discriminating measurement and it is not the same as "the file is over cap."** Measured 2026-09-07 at 13:5x ET across all 26 briefs: **6 files exceed the cap, but only ONE has `CROSS-DOMAIN` beyond it (SAM).** Amendment 12's protection is *positional* — on a 20 KB brief the order is cosmetic; it only bites where a truncation actually lands. **Sorting the rollout by conformance would have produced 14 packets; sorting it by consequence produces one.**

**⚠️ Standing consequence for the NEXT amendment, whatever it is:** an amendment is not ratifiable without naming its trigger, its owner and its observable-conformance surface **in the same word that ratifies it.** Amendment 12 was ratified 2026-09-01 and was still unrolled on 2026-09-07 because none of the three was written down — six days in which the schema asserted a protection the files did not have. *(This costs nothing: §4.6's CAP means amendment 12 is the last one, so this rule governs the amendment-cap re-spec and any successor schema rather than a queue of pending amendments.)*


### §A13j — §4.1 bullets as written — mandatory write-back, amendment 10 with its checkable form, amendment 11 with its scope note, amendment 12 with origin / MISSED-watch bullets (old lines 162–171) (crc32 57794de9, 2,928 B) — added after the independent read found these passages restated but not archived

- **Mandatory write-back in agent's SPAWN PROTOCOL closeout, every session.** Even no-change sessions update the AS OF stamp + STATUS commit hash. Forces the agent to look at the brief each session — staleness becomes self-correcting.
- **Amendment 10 (ORDERING — RATIFIED, Will-approved 2026-07-31): the brief fold is the LAST write-back of the session, after the final STATUS write and immediately before git commit.** A brief written mid-session and left untouched while STATUS work continues is the fleet's dominant CONTENT-STALE mechanism — the 7/31 audit found **5-of-5** stale briefs (WAL, CORAL, OSPREY, HAWK, BROCK) had refreshed-then-kept-working; zero had skipped the refresh. "Refreshed every closeout" without the ordering constraint permits exactly this failure. Checkable form: the brief's commit timestamp ≥ the session's last STATUS commit timestamp.
- **Amendment 11 (INVARIANT — RATIFIED 2026-08-07, NEXUS self-ruled): `pin-follows-STATUS-HEAD`. The brief's STATUS commit hash must EQUAL that agent's STATUS HEAD at the moment the brief is committed.** If a session commits STATUS again after the brief fold — the multi-workstream case — the pin is re-stamped and the brief re-committed. This supersedes amendment 10's *timestamp* check (`brief commit time ≥ last STATUS commit time`) with a *hash equality*, which is exact where a timestamp can tie or run non-monotonically across a rebase.
  - **This is a CHECK on an obligation §4.1 already imposes** ("Even no-change sessions update the AS OF stamp + STATUS commit hash"). **It adds no new duty to any agent** and it must NOT be shipped as an added closeout step in any agent's `CLAUDE.md` — see the scope constraint in the SELF-RULED block below.

- 🆕 **Amendment 12 (SECTION ORDER — RATIFIED 2026-09-01, Will-approved via PROME WQ-105: *"approve all of those with your recs"*; decision row 22): in the FULL variant, `## CROSS-DOMAIN` is the FIRST body section, above `## VIEW` and `## CALIBRATION`.** Zero text added or removed — **ORDER only.**
  - **Origin: HOMER's truncation defect, accepted verbatim** — §1 has ranked CROSS-DOMAIN **#1** since R1 while §2 put it **third**, so every truncation removed the highest-value section first, silently. 📦 full text → the archive companion §A12.
  - **The COMPACT variant (amendment 9) is UNCHANGED** — it has no VIEW/CALIBRATION split to reorder.
  - ⛔ **This is a zero-text DEFECT REPAIR, not an accretion.** The accretion question it raised is answered by §4.6's CAP, adopted in the same word — **not by declining a valid fix.**
  - ⚠️ **The watch-prediction that should have caught this was GRADED `MISSED` on its own letter** (see §4.6). NEXUS registered a falsifier saying *"if a twelfth amendment is PROPOSED"* — one was, on 8/28 — and did not grade it until PROME did on 9/1. **The rule that fires on my own accretion is the one I failed to run.**
