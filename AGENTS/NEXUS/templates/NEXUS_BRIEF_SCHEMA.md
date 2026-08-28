# NEXUS Brief Schema — LOCKED (R3 + amendments 7, 9, 10, 11)

**★ OWNER-OF-RECORD (encoded 2026-08-07 per PROME Roster-migration Phase 2, Will-accepted RAV plan v4 / Phase-0 rulings Part D):** **this file is the owner-of-record for WHICH agents owe a `NEXUS_BRIEF.md` and in WHAT FORM and ORDER** — the synthesis-read requirement, the schema/form invariants (full vs compact variant, amendment 9), and the ordering invariant (brief fold = the session's LAST write-back, amendment 10). `PROME/ROSTER.md` POINTS here and restates nothing. The LIVE coverage census stays in `AGENTS/NEXUS/BRIEFS_MAP.md` (no count is carried here).
**★ ROSTER CLASSES CHANGE NOTHING HERE (the load-bearing negative, recorded 2026-08-07):** the five descriptive classes ROSTER introduced 8/5 (ORGANIZING/SERVICE · REVIEW/QC · DOMAIN ACTIVE · PROVISIONAL ACTIVE · EVENT-DRIVEN SPECIALIST) are **DESCRIPTIVE ONLY and change ZERO brief obligations** — no agent gains or loses a NEXUS_BRIEF duty, read-tier, form, or ordering requirement by its class. Do not infer a read-obligation change from the taxonomy.

**Status:** Locked 2026-06-07 — schema R3 + amendment 7 (Expected by column) + **amendment 9 (compact variant for utility/single-seam agents — RATIFIED, Will-approved 2026-07-31, decision row 19)** + **amendment 10 (closeout ORDERING: brief fold = LAST write-back — RATIFIED, Will-approved 2026-07-31, decision row 20)** + **amendment 11 (`pin-follows-STATUS-HEAD` — RATIFIED 2026-08-07 by NEXUS SELF-RULING under `AGENTS/DAEDALUS/BLUEPRINTS/DELEGATION_TIER.md`, decision row 21; see the SELF-RULED block in §4.1)**. Iterations beyond this route through NEXUS as the canonical owner. **No amendment is pending.**

> **SUPERSEDED 2026-08-07:** *"**ONE amendment PENDING (Will-gated): proposed amendment 11 — `pin-follows-STATUS-HEAD`** (the brief's STATUS pin must equal STATUS HEAD *at commit time*, re-pinned after any same-session STATUS re-commit — an invariant checked at commit, not an ordering remembered). Origin: LABOR, flagged **four consecutive sessions** (8/5→8/7): amendment 10 is an ORDERING rule and ordering alone does not survive a second STATUS write in one session — on 8/7 the pin went stale three times in one multi-workstream session. NEXUS endorses (the amendment-10 audit's 5-of-5 evidence was about ordering; LABOR's n=4 is about re-commits — a distinct, real residual). **Not ratified — amendments 9/10 precedent: fleet-facing format changes get Will's look. Routed via PROME.**"* — preserved verbatim per DELEGATION_TIER rider R2. The routing judgment in that final sentence was itself the error the tier corrected: the amendments-9/10 precedent was applied **by surface** (it touches the brief format) rather than **by kind** (9 and 10 changed what a brief IS; 11 only checks a requirement §4.1 already imposes).
**Canonical location:** `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` (this file) + `NEXUS_BRIEF_TEMPLATE.md` (fleet-rollout template)
**Canonical brief path:** `AGENTS/<NAME>/NEXUS_BRIEF.md` (agent-owned)
**Author / pilot:** SAM (schema R1-R3 + iter-2 pilot at `AGENTS/SAM/NEXUS_BRIEF.md` — proves cap-as-measurement works for heaviest real domain)
**Reviewers:** PROME (R1+R2 green-lit) → NEXUS (R3 consumer review — 6 amendments converged independently with SAM; amendment 7 added Expected-by column)
**Scope:** required for Tier-1 active agents (CARL, REGINALD, OZK, SAM, RED, BROCK, LIQUID, HENRY, HAWK, BRENT, VIOLET, WALTER). Tier-2 spawn-as-needed agents (LABOR, HERMES, DARWIN, ZHAO, etc.) skip; NEXUS reads their STATUS directly when active. *(⚠️ Scope list is 2026-06-07 vintage, kept verbatim because the schema is LOCKED — the LIVE coverage index is `AGENTS/NEXUS/BRIEFS_MAP.md`, which carries the count; **no brief count is stated here** [the 7/22 annotation's bracketed "23" had itself rotted by 7/31 — the anti-rot note re-introduced the rot; de-hardcoded per the same-day CLAUDE.md census fix]. HERMES/DARWIN dropped 6/27; LABOR promoted to the Tier-1 read-set; WALTER/OZK/SHADE remain brief-less by design. Annotation added 2026-07-22, amended 2026-07-31; schema mechanics unchanged.)*

---

## 1. DESIGN INTENT — connective-tissue-first

The brief exists to serve **NEXUS's exclusive value: cross-agent connective-tissue detection.** Per PROME's Type A vs Type B distinction:

- **Type A (within-domain misses)** — e.g., CARL missed an indicator inside the US-macro domain. **Not NEXUS's job.** NEXUS holding opinions about domains it doesn't own is a stated anti-pattern. Type A is the agent's job, or RED's, or it lives in CALIBRATION's "uncertain about X."
- **Type B (cross-agent connective tissue)** — e.g., BRENT sees energy deflating, HAWK sees de-escalation, REGINALD sees duration stress; only NEXUS, seeing the whole board, catches that *together* they un-trap the Fed and threaten the TLT thesis. **Type B is NEXUS's actual function.**

**Implication for schema design:** Type B detection is fundamentally a *comparison* problem across agents. Comparison is dramatically easier when N inputs share a schema than when they're N idiosyncratic files *(the "13" originally written here = the June-2026 design-time fleet size, retained conceptually only — live count lives in `BRIEFS_MAP.md`)*. The brief is optimized for "see the whole board at once" — not for compressing tokens.

**Section priority under cap pressure (load-bearing → scaffolding):**

1. **CROSS-DOMAIN** — the connective tissue *is* the graph formed by overlapping CROSS-DOMAIN edges across agents. This is where NEXUS does its real work. Protect this section first.
2. **CALIBRATION (divergence + counter-signal lines)** — where cross-agent tensions surface. Protect second.
3. **VIEW** — context. Compressible.
4. **NEXT DECISION POINT** — useful for tasking but not synthesis. Compressible.
5. **WATCH** — forward-looking; secondary to current-state synthesis. Most compressible.

When trimming under cap pressure, compress upward from WATCH/VIEW. Never compress CROSS-DOMAIN or CALIBRATION's divergence line.

---

## 2. SCHEMA

```markdown
# <AGENT> — NEXUS Brief

**Status:** [🟢🟡🟠🔴] <one-line situation, ≤120 chars>
**Domain:** <one-line scope — what this agent owns>
**Thesis version:** vX.Y.Z (optional — agents that version)
**As of:** YYYY-MM-DD HH:MM ET | STATUS commit: <short-hash>

---

## VIEW

<3-5 bullets — current read in domain terms. Compressed claims, not STATUS recap.
Things only this agent knows by virtue of watching the domain. CONTEXT for NEXUS,
not where synthesis happens. Compressible under cap pressure.>

---

## CALIBRATION

- **Conviction (decomposed if applicable):** direction-[H/M/L] · timing-[H/M/L] · level-[H/M/L]
- **Diverge from market by:** <claim, magnitude, why — preserve the framing>
- **Cross-agent tensions known to me:** <optional — [agent] + nature of tension. Captures
  what this agent has already noticed via inbox/outbox signals.>
- **Uncertain about:** <what I don't know that would change my view>
- **Failure patterns to mind:** <1-2 anchor patterns + reference to PREDICTIONS.tsv,
  not a restated scoreboard>
- **RED counter-frame (if applicable):** <strongest current counter-case + my response,
  1-2 lines. Anchor to red/ log, don't dual-maintain.>

---

## CROSS-DOMAIN

**SENDING:**
| To | Signal | Priority | Mechanism it triggers in recipient's domain |
|----|--------|----------|---------------------------------------------|

**WAITING FOR:**
| From | Input | Expected by | Why it matters | How it changes my view |
|------|-------|-------------|----------------|------------------------|

---

## NEXT DECISION POINT

- **What:** <the next thing this agent will act on>
- **When:** <date or trigger condition>
- **What would change my view:** <falsification or pivot conditions, 1-2 lines>

---

## WATCH (next 2-4 weeks)

| Date | Event | Threshold / Signal |
|------|-------|---------------------|

---
```

---

## 3. SECTION DESIGN NOTES (for the agent drafting a brief)

### 3.1 VIEW

- 3-5 bullets, declarative claims.
- "What I'm thinking right now" — NOT a STATUS recap, NOT a CHANGELOG.
- Cite specific levels/dates/probabilities where load-bearing.
- The agent generates novel content here; this is NOT a reference-only section.
- Compressible under cap pressure. If the agent can't compress further, the thesis hasn't matured into a 1-2 sentence shape yet.

### 3.2 CALIBRATION

- **Most load-bearing line:** "Diverge from market by" — preserve the framing, not just the number. "SAM-21 70% vs market 96% — earned discount from 2 prior Takaichi-ceiling failures; direction-of-conviction matches market" is the right shape. "SAM 70% / market 96%" alone tells NEXUS the wrong story.
- **"Cross-agent tensions known to me" is optional but high-value when it exists.** Captures asymmetric information — what THIS agent has already noticed via signals/outbox that wouldn't show in another agent's STATUS. Example: if SAM has received a LIQUID signal contradicting SAM's view, surface it here rather than waiting for NEXUS to derive it.
- **Failure patterns: REFERENCE, don't restate.** Format: `<1-2 anchor pattern names> — see PREDICTIONS.tsv preamble`. Restated scoreboard silently forks from canonical source.
- **RED counter-frame: REFERENCE, don't restate.** Format: `<strongest current counter, 1 line> + <my response, 1 line> — see red/<file>`. Avoid dual-maintenance.

### 3.3 CROSS-DOMAIN

**This is the single most important section.** NEXUS's connective-tissue detection works by reading these edges across all agents and finding the graph.

- **SENDING table — the 4th column is critical.** "Mechanism it triggers in recipient's domain" forces the agent to think about what the signal DOES, not just what it IS. "SAM → LIQUID: net selling >¥1T/month" is a data point. "SAM → LIQUID: net selling >¥1T/month → reduces UST demand → puts upward pressure on 10Y / steepens curve in LIQUID's domain" is a connective-tissue claim NEXUS can use.
- **WAITING FOR table — the 3rd column ("Expected by") + 4th and 5th columns are critical.** "Expected by" gives NEXUS a date/trigger to detect waiting-on-waiting deadlock when scanning the fleet (e.g. if CARL hasn't surfaced an awaited input by its Expected-by date, that's a chain-break worth flagging). "Why it matters" + "How it changes my view" tell NEXUS what edge to weight when it sees the upstream agent's brief. Use date format (`Wed Jun 10`) for hard dates, condition format (`Open — watch X signal`) for open-ended waits.
- **Tables can be empty.** If SAM has nothing waiting from HAWK this week, leave WAITING FOR's HAWK row out. Better than placeholder noise.
- **No P/L, no money figures, no position $ amounts.** Per `[[feedback_position_cost_basis_not_authoritative]]` — references position structurally (e.g., "long FXY 13sh + Jun-18 $58C") but never marks/P&L.

### 3.4 NEXT DECISION POINT

- 3 bullets, tight.
- "What" + "When" + "What would falsify" — sufficient for NEXUS tasking.
- Falsification belongs HERE (not in CALIBRATION) — view-falsification vs decision-falsification differ; keep them separated.

### 3.5 WATCH

- 2-4 weeks forward only.
- 3-6 rows. Reference CALENDAR for full forward dates; this is the subset that matters for THIS agent's view.
- Most compressible section under cap pressure.

---

## 4. MAINTENANCE DISCIPLINE

### 4.1 Update trigger

- **Mandatory write-back in agent's SPAWN PROTOCOL closeout, every session.** Even no-change sessions update the AS OF stamp + STATUS commit hash. Forces the agent to look at the brief each session — staleness becomes self-correcting.
- **Amendment 10 (ORDERING — RATIFIED, Will-approved 2026-07-31): the brief fold is the LAST write-back of the session, after the final STATUS write and immediately before git commit.** A brief written mid-session and left untouched while STATUS work continues is the fleet's dominant CONTENT-STALE mechanism — the 7/31 audit found **5-of-5** stale briefs (WAL, CORAL, OSPREY, HAWK, BROCK) had refreshed-then-kept-working; zero had skipped the refresh. "Refreshed every closeout" without the ordering constraint permits exactly this failure. Checkable form: the brief's commit timestamp ≥ the session's last STATUS commit timestamp.
- **Amendment 11 (INVARIANT — RATIFIED 2026-08-07, NEXUS self-ruled): `pin-follows-STATUS-HEAD`. The brief's STATUS commit hash must EQUAL that agent's STATUS HEAD at the moment the brief is committed.** If a session commits STATUS again after the brief fold — the multi-workstream case — the pin is re-stamped and the brief re-committed. This supersedes amendment 10's *timestamp* check (`brief commit time ≥ last STATUS commit time`) with a *hash equality*, which is exact where a timestamp can tie or run non-monotonically across a rebase.
  - **This is a CHECK on an obligation §4.1 already imposes** ("Even no-change sessions update the AS OF stamp + STATUS commit hash"). **It adds no new duty to any agent** and it must NOT be shipped as an added closeout step in any agent's `CLAUDE.md` — see the scope constraint in the SELF-RULED block below.
  - Origin: LABOR, flagged **four consecutive sessions** (8/5→8/7); the pin went stale three times in one multi-workstream session on 8/7. Amendment 10 is an ORDERING rule, and ordering alone does not survive a second STATUS write in one session — a distinct, real residual from the 5-of-5 evidence that produced amendment 10.
  - **Measured cost of the gap, this file's own consumer:** SHADE's brief was folded ~11:15 on 8/4 carrying "ARCC pre-reg UNGRADED/overdue" — **five minutes after that grade landed at ~11:10** in the same session. NEXUS read the brief on 8/7 and wrote the stale claim onto its board in two places, where it sat three days as a false accusation against a desk that had done the work.

**SELF-RULED 2026-08-07 (DELEGATION_TIER):** May NEXUS, as schema owner-of-record, ratify amendment 11 itself rather than routing it to Will?
→ Yes — ratified as an INVARIANT, expressly NOT as an added closeout step in any agent's instructions. Tests 1-5 PASS. Riders: R1 (dated), R2 (superseded header text preserved verbatim above), R3 (n/a — no confidence, probability or weight moved in this edit).
- **Test 1 SCOPE — PASS, and it is the binding one.** The ruling changes one file inside `AGENTS/NEXUS/`. It passes under the tier's CHECK-versus-DO refinement *because §4.1 already requires the hash stamp*; amendment 11 makes an existing obligation checkable, it does not create one. ⚠️ **This is why the ruling carries a scope constraint: if amendment 11 were ever propagated as "every agent adds a step to its closeout doc," it would change ~26 files outside this directory and test 1 would FAIL.** The invariant is enforced at the check, not by fleet-wide instruction edits.
- **Test 2 REVERSIBILITY — PASS.** Undoing it edits this file only. The `AGENTS/SELF_RULINGS.tsv` row is an append-only audit record; a reversal appends, it does not delete.
- **Test 3 NO-CAPITAL — PASS.** A commit-time equality check on a pointer. It gates, sizes, prices, selects strikes for, and sets exits for nothing.
- **Test 4 ANTI-SELF-SERVING — PASS, with a guard recorded rather than assumed.** The ruling makes NEXUS *easier* to catch being wrong (the SHADE class is exactly what it detects) and makes no threshold easier to satisfy — the fallback rollup's decision rule keys on `brief-gap` rate, which this does not touch. ⚠️ **The self-serving edge, named:** a falling `stale`-cause fallback rate after this ships would make NEXUS's own brief-health instrument look healthier. **NEXUS will not cite a post-amendment-11 `stale`-rate drop as evidence of brief quality** — it is a real improvement in pin accuracy, not a measurement of content.
- **Test 5 DATA-VS-INSTRUMENT — PASS.** The subject is whether a pointer in NEXUS's own artifact equals the head of the file it points at: a property of this instrument, not of the world. It is not revision handling, vintage, publication cadence, unit base, or weekday convention, and no second authority could rule it differently (contrast MIDAS L-15, which is fleet-wide by subject).

- Material STATUS change → brief content updates same session.
- No-material-change session → AS OF + hash stamp refresh only.

### 4.2 Cap discipline — measurement, not aspiration

- **No fixed cap until pilot measurement completes.** The SAM pilot brief sets the empirical ceiling for the heaviest real domain. If SAM compresses cleanly to 50, cap is 50. If SAM bursts to 95, cap is 95 (not "force-trim SAM").
- **Cap is calibrated to the heaviest real domain, not picked aspirationally.**
- **Cap-burst on a settled agent = fragmentation hypothesis** (not an auto-trigger). If SAM consistently bursts after pilot calibration, that's a signal to investigate whether SAM's domain has fragmented and warrants sub-agent spinout (like OZK from REGINALD). Investigation, not automatic action.

### 4.3 Reference, never restate (the anti-drift rule)

The brief must REFERENCE canonical content with anchors, never duplicate it:

| Content | Lives in | Brief format |
|---------|----------|--------------|
| Failure patterns | `PREDICTIONS.tsv` preamble | 1-2 anchor names + reference |
| RED counter-frames | `red/<file>.md` | 1-line summary + reference |
| Full thesis | `thesis/THESIS.md` | thesis version stamp in header |
| Forward catalysts | `docket/CALENDAR.md` | WATCH = subset that matters for VIEW |
| Cross-agent signals | `inbox/`, `outbox/` | CROSS-DOMAIN tables (steady-state surface) |
| Live market data | `STATUS.md` | Specific levels only when load-bearing for VIEW/CALIBRATION |

**Exception:** VIEW generates novel compressed claims. It's not a reference-only section. But VIEW must compress STATUS, not restate it.

### 4.4 Stale-check + STATUS fallback (Q7 amendment)

**Mechanical stale-check:** NEXUS compares the STATUS commit hash in the brief header to current STATUS HEAD for the agent's directory. Mismatch → brief is "N commits stale."

**Fallback to raw STATUS triggers (NEXUS-side):**

NEXUS reads raw STATUS for an agent when ANY of:

- **(a) Mechanical staleness:** brief hash ≠ STATUS HEAD AND mismatch is >1 commit (single-commit lag tolerated to avoid hair-trigger).
- **(b) Convergence-suspicion (Type B drill-down):** two or more briefs hint at a convergence neither explicitly names. Example: BRENT brief mentions "energy deflating"; HAWK brief mentions "de-escalation tape"; neither names the Fed-untrap. NEXUS drills both STATUSes to chase the thread.
- **(c) Cross-domain uncertainty surfacing:** a CALIBRATION "uncertain about X" item names something in another agent's domain. NEXUS drills the OTHER agent's STATUS to see if the uncertainty resolves there.

**(a) is mechanical / always fires.** (b) and (c) require NEXUS-side judgment, which is exactly the work NEXUS should be doing.

**Drill-down is for chasing cross-agent threads, NOT for auditing within-domain work.** NEXUS reading raw STATUS to second-guess CARL's US-macro detail is the anti-pattern. Reading raw STATUS to chase a convergence neither CARL nor BRENT named is the correct application.

### 4.5 Length

- Hard ceiling: pending pilot measurement (provisionally 100 lines; revise after SAM pilot).
- Headers, separators, section markers count.

> ⚠️ **RULED 2026-08-28 (NEXUS, on VULCAN's §4.5 ask + HOMER's ordering packet): THE 100-LINE CEILING IS ON THE WRONG AXIS AND IS NOT ENFORCED PENDING AMENDMENT 12.** Measured fleet-wide this session (all 26 briefs): **12 of 26 are over the cap** — it is not binding, it is being ignored by half the fleet — and **line count is nearly uncorrelated with byte load**: `WATT` 37 lines / **20.4 KB** (550 B/line) vs `OSPREY` 75 lines / **11.5 KB** (153 B/line); `SHADE` 42 lines / 22.5 KB; heaviest are `SAM` 318/105.9 KB, `HOMER` 165/94.7 KB, `VULCAN` 187/92.8 KB. **A brief can sit 60% under the cap and carry more bytes than one twice over it.** ⛔ **A byte cap alone is the WEAKER fix and is NOT adopted** — HOMER flagged against its own interest that a cap on the wrong axis *rewards compression into longer lines*, and the fleet's highest B/line figures are all short files, which confirms it. **No agent is to cut content against this cap until amendment 12 is ruled** (VULCAN told so explicitly, at 187 lines). The binding control is POSITION, not length — see the §6 strike below.
- "N/A" sections allowed but must include a one-line reason (`N/A — no active cross-agent threads this cycle`).

---

## 5. INTEGRATION WITH NEXUS

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

### 🔴 AMENDMENT-12 WATCH — **RESOLVED EARLY 2026-08-28: THE PREDICTION FAILED, 21 DAYS BEFORE ITS GRADE DATE**

**The registered prediction** (opened 8/07, `FORUM/2026-08-07_system-review/02_repair-burden/06_NEXUS_canon-mass-reply.md`): DAEDALUS's discriminator held that **amendment 11 — the only FORMAT rule in the set — ENDS its class**, while the ten RECOGNITION amendments keep generating successors. **Registered falsifier: *"Grade 2026-09-18: if a twelfth amendment is proposed, the prediction fails and the schema is an accreting surface that needs a cap rather than another rule."***

**A twelfth amendment was proposed on 2026-08-28. ⇒ THE PREDICTION IS FALSIFIED.** And it fails in the sharpest available way: **amendment 12 is itself a FORMAT/ordering rule — a second member of the class the discriminator said was closed** — not a recognition-class successor.

⚠️ **DATE-KEYED-SCANNER DEFECT, caught here:** the grade was keyed to **9/18**, so a due-date scan run any time before then would have read this as all-clear while the resolver had already fired. `[[finding_date_keyed_scanner_cannot_see_an_early_resolver]]`. **A registered prediction needs a resolver that fires on the EVENT, not only a date to be checked on.**

⚠️ **The consequence clause, and I am NOT ruling it myself.** The falsifier's own words are that the schema *"needs a cap rather than another rule"* — which is an argument **against the very amendment that triggered it.** There is a real case that 12 is the one class that does not accrete (it adds no text and no obligation; it MOVES existing sections), and there is an obvious objection to me making that case: **arguing my own amendment out of the falsifier my own amendment fires is exactly the configuration Disc-J §5 says a grader should not be trusted on.** ⇒ **Routed to Will and DAEDALUS with the amendment, unresolved by me: does a purely-ordering amendment count as accretion?** Both the prediction's failure and this question travel in the escalation packet. **If the answer is "it counts," then the correct fix is a schema cap and amendment 12 should be declined even though its finding is valid** — and I will take that.

*⚠️ Original watch text, for the record — **Amendment-12 watch opened 2026-08-07.** The standing question from `FORUM/2026-08-07_system-review/02_repair-burden/06_NEXUS_canon-mass-reply.md`: DAEDALUS's discriminator predicts that amendment 11 — the only FORMAT rule in the set — ends its class, while the ten RECOGNITION amendments keep generating successors. **Grade 2026-09-18: if a twelfth amendment is proposed, the prediction fails and the schema is an accreting surface that needs a cap rather than another rule.** The tier's own falsifier runs in parallel: one Will reversal of any self-ruling by 2026-10-06 narrows or kills the tier.*
