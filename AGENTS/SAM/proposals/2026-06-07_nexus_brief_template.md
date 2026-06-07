<!--
NEXUS_BRIEF TEMPLATE — copy this file to AGENTS/<YOUR_AGENT>/NEXUS_BRIEF.md and fill in.

Schema spec (full rationale): AGENTS/SAM/proposals/2026-06-06_nexus_brief_schema.md
Worked example (heaviest domain — Japan macro, 4 channels, 5 cross-agent edges):
  AGENTS/SAM/NEXUS_BRIEF.md

Amendments applied (NEXUS R3, 2026-06-07):
  1. Recent thesis pivot: REQUIRED single line (named what + why)
  2. Cross-agent tensions: REQUIRED (write "None active this cycle" if empty — do not delete the bullet)
  3. WATCH renamed FORWARD CATALYSTS; NEXT DECISION POINT carved out as the agent-actioned subset
  4. SENDING: single table (no STANDING/THIS-CYCLE split, no drop rule). Refresh discipline at session closeout.
  5. Status emoji: per CLAUDE.md key only — 🟢 none / 🟡 monitoring / 🟠 elevated / 🔴 active/critical
  6. Conviction decomposition: OPTIONAL per agent (direction/timing/level if your domain has clean math; single-letter conviction otherwise)
  Scope: Tier-1 agents only (CARL, REGINALD, OZK, SAM, RED, BROCK, LIQUID, HENRY, HAWK, BRENT, VIOLET, WALTER + NEXUS). Tier-2 spawn-as-needed agents skip the brief.

Maintenance:
  - Update at every session closeout per SPAWN PROTOCOL discipline.
  - No-material-change session → refresh As-Of stamp + STATUS commit hash only.
  - Material change → content updates same session.
  - NEVER restate canonical content (PREDICTIONS scoreboard, full RED log, full thesis). REFERENCE with anchor.
  - Length: pending pilot measurement, provisional cap 100 lines. SAM pilot lands at 75.

REMOVE this top comment block when you copy the template. Section-level <!-- comments --> below
are also instructional and should be removed when you fill in your brief.
-->

# <AGENT> — NEXUS Brief

<!--
Status banner: emoji + thesis-version + ONE PRIMARY CLAIM. ≤120 chars hard cap.
Emoji per CLAUDE.md key: 🟢 none / 🟡 monitoring / 🟠 elevated / 🔴 active/critical
The primary claim should be the single thing NEXUS most needs to know about your domain right now.
NOT a list of three claims joined by semicolons. Pick the load-bearing one.
-->
**Status:** [🟢🟡🟠🔴] vX.Y.Z — <ONE primary claim, ≤120 chars>

<!--
Domain: one line. What you own, what transmission edges you sit on. NOT a manifesto.
-->
**Domain:** <one-line scope — what this agent owns + key transmission edges>

<!--
Thesis version: optional (some agents version, some don't). Use SAM-style vX.Y.Z if you version.
-->
**Thesis version:** vX.Y.Z (optional)

<!--
Recent thesis pivot: REQUIRED single line. Format: <old version> → <new version> (<date>) — <reason in 1 clause>
The REASON is what NEXUS cares about — version stamp alone says "something moved" but not "what + why."
If no version pivot yet, write the most recent material view shift: "<view> → <view> (<date>) — <reason>"
Keep to ONE clause. The structural detail lives in CHANGELOG / VIEW; the brief gets the headline.
-->
**Recent thesis pivot:** <old> → <new> (<date>) — <one-clause reason>

<!--
As-Of: timestamp when you last touched the brief. If STATUS data is older than the As-Of stamp
(e.g. weekend, market closure, refresh lag), tag inline: "(STATUS data through Fri X/Y close)"
NEXUS uses the commit hash for mechanical stale-check (§4.4 of schema).
-->
**As of:** YYYY-MM-DD ~HH:MM ET | STATUS commit: <short-hash>

---

## VIEW

<!--
3-5 bullets. Compressed novel claims — "what I'm thinking right now."
NOT a STATUS recap. NOT a CHANGELOG. Cite specific levels/dates/probabilities where load-bearing.
This is the only section where you generate novel content (the rest reference canonical sources).
If you can't compress to 5 bullets, the thesis hasn't matured into a 1-2 sentence shape yet.
Most compressible section under cap pressure (after WATCH).
-->

- **<claim 1>** — <evidence + level/date/prob>
- **<claim 2>** — <evidence + level/date/prob>
- **<claim 3>** — <evidence + level/date/prob>
- **<claim 4>** — <evidence + level/date/prob>
- **<claim 5 — optional>** — <evidence + level/date/prob>

---

## CALIBRATION

<!--
The "Diverge from market by" line is the single most load-bearing line in the brief.
Preserve the FRAMING (not just the number): "SAM 70% vs market 96% — earned discount from prior failures"
not "SAM 70% / market 96%." The framing tells NEXUS the story; the number alone tells a wrong one.
-->

- **Conviction (decomposed if applicable):** direction-[H/M/L] · timing-[H/M/L] · level-[H/M/L]
  <!-- Single-letter conviction OK if your domain doesn't decompose cleanly (HAWK direction-only, BROCK direction+timing). -->

- **Diverge from market by:** <claim, magnitude, why — preserve framing, not just number>

<!--
Cross-agent tensions: REQUIRED. Write "None active this cycle" if empty — do NOT delete the bullet.
Captures asymmetric info — what YOU noticed via inbox/outbox that wouldn't show in another agent's STATUS.
Optional sub-line: "Forming tension with [agent] if [condition]" — flags emerging convergences.
-->
- **Cross-agent tensions known to me:** <None active this cycle | tension content>

- **Uncertain about:** <(1) what I don't know that would change my view; (2) ...; (3) ... — tag which agent owns the answer>

<!--
Failure patterns: REFERENCE, don't restate. 1-2 anchor names + cite to PREDICTIONS.tsv preamble.
Restated scoreboard silently forks from canonical.
-->
- **Failure patterns:** <pattern 1 + count> · <pattern 2 + count> — see `thesis/PREDICTIONS.tsv` preamble (or equivalent)

<!--
RED counter-frame: REFERENCE, don't restate. 1-2 lines + cite to red/ log. Skip if no active counter.
-->
- **RED counter-frame:** <strongest current counter, 1 line> + <my response, 1 line> — see `red/<file>`

<!--
Type B convergence candidate (OPTIONAL): a synthesis-flag for NEXUS — "here's a thread I noticed
that crosses domains; you might want to look." Skip if nothing active. Don't force.
-->
- **Type B convergence candidate I'm flagging:** <thread description + cross-domain edges + when to surface>

---

## CROSS-DOMAIN

<!--
SINGLE MOST IMPORTANT SECTION. NEXUS does its real work here — reading these edges across all
agents and finding the graph. Protect under cap pressure first.

SENDING table — the 4th column ("Mechanism it triggers in recipient's domain") is what makes the
brief useful vs raw STATUS. Force yourself to think about what the signal DOES, not just what it IS.
  Bad: "SAM → LIQUID: net selling >¥1T/month"
  Good: "SAM → LIQUID: net selling >¥1T/month → reduces UST demand → upward 10Y pressure"

Single table per Will. No STANDING/THIS-CYCLE split. Refresh discipline at session closeout —
stale rows are your responsibility to age out.

No P/L, no money figures, no position $ amounts. Reference position structurally only.
-->

**SENDING:**

| To | Signal | Priority | Mechanism it triggers in recipient's domain |
|----|--------|----------|---------------------------------------------|
| <agent> | <signal content> | 🟢/🟡/🟠/🔴 | <mechanism in recipient's domain — what does this DO> |
| <agent> | <signal content> | 🟢/🟡/🟠/🔴 | <mechanism in recipient's domain> |

<!--
WAITING FOR — the 3rd and 4th columns are critical. "Why it matters" + "How it changes my view"
tell NEXUS what edge to weight when it sees the upstream agent's brief.
Empty tables are fine — don't add placeholder rows.
-->

**WAITING FOR:**

| From | Input | Why it matters | How it changes my view |
|------|-------|----------------|------------------------|
| <agent> | <input I need> | <why it matters to my view> | <how it changes my mark/conviction> |
| <agent> | <input I need> | <why it matters> | <how it changes my view> |

---

## NEXT DECISION POINT

<!--
The next agent-actioned move (NOT just monitoring). Subset of FORWARD CATALYSTS that triggers
a brief refresh / mark move / position decision / cross-agent signal.

What/When/Falsify — 3 bullets, tight. Falsification belongs HERE (decision-falsification),
NOT in CALIBRATION (which captures view-uncertainty — different scope).
-->

- **What:** <the next thing I will act on — a mark move, a position decision, a signal trigger>
- **When:** <date OR trigger condition>
- **What would falsify the trigger:** <1-2 conditions that would prevent the default action>

---

## FORWARD CATALYSTS (next 2-4 weeks)

<!--
3-6 rows. Reference your domain CALENDAR for the full forward list; this is the SUBSET that matters
for YOUR view. Most compressible section under cap pressure.

NEXT DECISION's "What" should appear as one row here (cross-ref it: "see NEXT DECISION").
Don't dual-maintain the falsification logic — it lives in NEXT DECISION.
-->

| Date | Event | Threshold / Signal |
|------|-------|---------------------|
| 🟢/🟡/🟠/🔴 <date> | <event> | <threshold / signal interpretation> |
| 🟢/🟡/🟠/🔴 <date> | <event> | <threshold / signal interpretation> |
| 🟢/🟡/🟠/🔴 <date> | <event> | <threshold / signal interpretation> |

---

<!--
Footer: optional. Use for schema-version stamp + any agent-specific notes.
Remove if not useful.
-->

*Brief format follows NEXUS_BRIEF schema (R3 amendments). Updated at every session closeout per SPAWN PROTOCOL discipline.*
