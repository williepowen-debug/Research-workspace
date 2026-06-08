# NEXUS Brief Schema — LOCKED (R3 + amendment 7)

**Status:** Locked 2026-06-07 — schema R3 + amendment 7 (Expected by column). Iterations beyond this route through NEXUS as the canonical owner.
**Canonical location:** `AGENTS/NEXUS/templates/NEXUS_BRIEF_SCHEMA.md` (this file) + `NEXUS_BRIEF_TEMPLATE.md` (fleet-rollout template)
**Canonical brief path:** `AGENTS/<NAME>/NEXUS_BRIEF.md` (agent-owned)
**Author / pilot:** SAM (schema R1-R3 + iter-2 pilot at `AGENTS/SAM/NEXUS_BRIEF.md` — proves cap-as-measurement works for heaviest real domain)
**Reviewers:** PROME (R1+R2 green-lit) → NEXUS (R3 consumer review — 6 amendments converged independently with SAM; amendment 7 added Expected-by column)
**Scope:** required for Tier-1 active agents (CARL, REGINALD, OZK, SAM, RED, BROCK, LIQUID, HENRY, HAWK, BRENT, VIOLET, WALTER). Tier-2 spawn-as-needed agents (LABOR, HERMES, DARWIN, ZHAO, etc.) skip; NEXUS reads their STATUS directly when active.

---

## 1. DESIGN INTENT — connective-tissue-first

The brief exists to serve **NEXUS's exclusive value: cross-agent connective-tissue detection.** Per PROME's Type A vs Type B distinction:

- **Type A (within-domain misses)** — e.g., CARL missed an indicator inside the US-macro domain. **Not NEXUS's job.** NEXUS holding opinions about domains it doesn't own is a stated anti-pattern. Type A is the agent's job, or RED's, or it lives in CALIBRATION's "uncertain about X."
- **Type B (cross-agent connective tissue)** — e.g., BRENT sees energy deflating, HAWK sees de-escalation, REGINALD sees duration stress; only NEXUS, seeing the whole board, catches that *together* they un-trap the Fed and threaten the TLT thesis. **Type B is NEXUS's actual function.**

**Implication for schema design:** Type B detection is fundamentally a *comparison* problem across agents. Comparison is dramatically easier when 13 inputs share a schema than when they're 13 idiosyncratic files. The brief is optimized for "see the whole board at once" — not for compressing tokens.

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

---

## 7. REVIEW HISTORY (Will → PROME → NEXUS → SAM iterations)

| Round | Reviewer | Key correction |
|-------|----------|----------------|
| R1 | PROME (initial) | Reframe: motivation isn't token reduction — it's compression-to-edge. Cap should be tighter. Reference, don't restate. Hash-fallback mandatory. Pilot before fleet. |
| R2 (this round, after Will pushback) | PROME (final) | **Type A vs Type B distinction is the resolver.** Within-domain misses NOT NEXUS's job; cross-agent connective tissue IS. Brief is *better* input than raw STATUS for Type B because comparison is easier in standard schema. CROSS-DOMAIN + CALIBRATION-divergence are load-bearing; protect under cap pressure. SAM-proposes / NEXUS-ratifies / Will-arbitrates is healthy org template. |
| R2 SAM corrections accepted | | (a) Q7 widened to triggers (a)(b)(c) per § 4.4; (b) connective-tissue-first design intent baked in; (c) explicit section priority; (d) CROSS-DOMAIN mechanism framing in SENDING table column; (e) optional cross-agent-tensions sub-bullet in CALIBRATION; (f) cap is measurement not aspiration |
| **R3 (Sun Jun 7 PM, post-NEXUS E-phase)** | **NEXUS (consumer)** | **6 amendments + 1 scope clarification:** Recent Thesis Pivots required; Cross-agent tensions required; WATCH→FORWARD CATALYSTS rename + NEXT DECISION carve-out; emoji semantics locked; conviction decomp optional; Tier-1 scope only. Will arbitrated to reject the proposed SENDING drop-rule (kept single table); applied 6 amendments + scope to schema. SAM drafted pilot brief at canonical path. |
| **R3 amendment 7 (Sun Jun 7 PM, post-pilot consumer review)** | **NEXUS (consumer review of pilot)** | **Pilot brief load-bearing test passed** ("would do Type-B synthesis pass without raw STATUS fallback"). 5 brief polish edits surfaced + 1 schema escalation: WAITING FOR "Expected by" column raised from brief-edit to schema amendment given fleet-wide cross-agent value. Brief edits applied: status one-liner trim to single claim; position info moved from VIEW to header; VIEW bullet 3 lead-with-synthesis rewrite; failure-pattern counts+IDs stripped for NEXUS consumption; 🔴🔴 → single 🔴+bold. |

---

## 8. OPEN ITEMS FOR NEXUS RATIFICATION

- [ ] Does the schema's section ordering match NEXUS's reading pattern, or should sections be reordered for consumption efficiency?
- [ ] Are the (b) and (c) fallback triggers parseable for NEXUS, or do they need refinement?
- [ ] Should `NEXUS_BRIEF.md` live at `AGENTS/<NAME>/NEXUS_BRIEF.md` or under a dedicated NEXUS-owned dir (`AGENTS/NEXUS/briefs/<AGENT>.md`)? Path is structural — NEXUS picks.
- [ ] Cap ceiling after SAM pilot measurement: confirm whatever the SAM brief lands at, or adjust based on consumption ergonomics.
- [ ] Should the brief carry a "RECENT THESIS PIVOTS" field (e.g., v1.5 → v1.5.1) to help NEXUS detect whose-view-moved-recently, or is the version stamp + commit hash sufficient?
