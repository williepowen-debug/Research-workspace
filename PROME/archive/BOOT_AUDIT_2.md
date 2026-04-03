# Boot Audit #2 — 2026-03-12

## Phase 1: Injection Audit

### Files Received as Project Context

| File | ~Size | What It Tells You | Signal:Noise |
|------|-------|-------------------|-------------|
| AGENTS.md | ~1.5KB | System purpose (systemic risk research), transmission chain, boot pointer, safety rules, file editing rules, sub-agent protocol, core principles | 9/10 — dense, essential, every line matters |
| SOUL.md | ~1.2KB | Prome's identity, personality (direct, opinionated, resourceful), boundaries (private data, external actions), continuity model | 7/10 — important for tone calibration, less critical for task execution |
| TOOLS.md | ~100B | pdfminer.six is installed | 2/10 — one useful fact, barely worth injecting |
| IDENTITY.md | ~30B | "See SOUL.md" | 0/10 — pure redirect, wastes injection tokens for zero value |
| USER.md | ~3KB | Will's background, communication preferences, thinking style, financial motivation, career context | 8/10 — critical for knowing who you serve, but the biography section (~40% of file) is rarely actionable at boot |

### Observations
- **IDENTITY.md should be deleted or merged into SOUL.md.** It's a pointer to a file that's already injected. Pure waste.
- **TOOLS.md is too thin to justify injection.** Either bulk it up with actually useful tool notes or move it into a non-injected reference file.
- **USER.md's biography section** (education, career history, ChatGPT Codex origin story) is interesting but rarely needed at boot. Consider splitting into USER.md (working preferences, what matters now) and USER_BACKGROUND.md (read on-demand). Saves ~1KB of injection context.
- **Missing from injection:** No market state, no positions, no agent status. This is correct — BOOT.md handles that via sequential reads. But it means the injected context alone is insufficient to do anything useful. You MUST complete boot.

---

## Phase 2: Boot Sequence Walkthrough

### BOOT.md
- **Found where expected?** Yes, `PROME/BOOT.md` exactly as AGENTS.md pointed.
- **Orientation speed:** Fast. Clear numbered sequence. Explicit "read FIRST" on SCRATCH.md.
- **Issues:** The sub-agent operations section (spawn syntax, steer/check) is reference material that doesn't need to be read at boot. It adds ~15 lines of cognitive load. The NEXUS section is also reference. Consider moving both to a separate PROME/OPS_REFERENCE.md and keeping BOOT.md purely as a sequence file. Boot should be: read this, then this, then this. Done.
- **Good:** "On-Demand" section explicitly says what NOT to read at boot. Prevents over-reading.

### SCRATCH.md
- **Found where expected?** Yes, `PROME/SCRATCH.md`.
- **Orientation speed:** Excellent. First 3 lines give you the full handoff context. "Major research + trading day. Built Hamilton Framework. 9 trades. CPI in-line. USD/JPY 159."
- **Issues:** None significant. The "Next tide" numbered list is exactly what a cold-starting agent needs — immediate priorities, ordered. The positions entered/exited today section gives concrete grounding.
- **Assessment:** Best file in the boot sequence. If you could only read one file, this one gets you 70% of the way there.

### STATUS.md
- **Found where expected?** Yes, `PROME/STATUS.md`.
- **Orientation speed:** Good but dense. The scenario header (🔴🔴 SCENARIO C — WAR DAY 12 — STAGFLATION TRAP) immediately orients you. Agent table is scannable.
- **Issues:**
  - Positions section is comprehensive but takes time to parse. The format works but could use a "portfolio summary" line at top (total puts value, total longs value, cash, net Greek exposure).
  - Convictions table with Hamilton lag numbers is excellent — this is the system's unique edge, surfaced at exactly the right level.
  - Dates section is critical and well-maintained.
  - Pending section overlaps significantly with SCRATCH.md "Next tide." Not a problem if SCRATCH is ephemeral and STATUS is persistent, but the duplication is noticeable.
- **Assessment:** 8/10. Does its job as a dashboard. The agent status table alone is worth the read.

### LESSONS.md
- **Found where expected?** Yes, workspace root.
- **Orientation speed:** Fast. Organized by severity (Costly > Verification > Process). Each lesson is one concrete sentence.
- **Issues:**
  - Only 12 lessons total. Feels light for a system this complex. Either lessons aren't being captured, or they're being captured elsewhere (memory files).
  - Lesson #1 (don't override conviction) and Lesson #5 (roll duration, don't trim) are the two most critical. They should be more prominent — maybe a "TOP 2" section at the very top.
  - Missing lessons I'd expect: nothing about position sizing, nothing about when to cut losers (OWL, VLY, EGBN are all underwater), nothing about agent spawn failures or timeout handling.
- **Assessment:** 7/10. Good for what's there, but incomplete.

### Memory Files (2026-03-12, 2026-03-11)
- **Found where expected?** Yes, `memory/` directory.
- **Orientation speed:** Slow. These are comprehensive daily logs — Mar 12 is ~3KB, Mar 11 is ~6KB. They're thorough but reading both at boot adds significant context load.
- **Issues:**
  - Mar 11 is extremely long. Multiple checkpoints, full proposal lists, market snapshots. This is great for archival but expensive at boot. The boot sequence says "Read today + yesterday" but yesterday's file is almost as large as all other boot files combined.
  - Suggestion: Memory files should have a 3-line TL;DR at the top. "Yesterday: 15 agents spawned, all proposals resolved, JPM private credit signal confirmed cascade thesis, 4 trades executed, CPI decision tree set."
  - The checkpoint format within memory files is inconsistent — some have timestamps, some don't. Some have "Changed" and "Next" fields, some don't.
- **Assessment:** 6/10 for boot utility. 9/10 for archival value. These serve two masters and optimize for neither.

---

## Phase 3: Comprehension Test Results

### 1. Current market scenario?
**Scenario C — Stagflation Trap, War Day 12.** Gulf war (Hormuz actively mined), oil NOPI at 47 log points, CPI at 2.4% but pre-shock (April is the real print). USD/JPY at 159, 100 pips from Bessent 160 bilateral trigger. Credit spreads (HY OAS 319) 1bp from LIQ-01 threshold. Consumer savings at 3.6% (2008 levels). Multiple converging stress vectors: oil, labor (DHS disruption), credit (ABS cracks), Japan (carry unwind risk). The thesis is stagflationary recession materializing through Hamilton oil-GDP transmission with front-loaded consumer destruction.

### 2. Top 3 trade priorities?
1. **Claims tomorrow 8:30 AM ET** — tripwire event, first clean post-DHS read. ≥235K initial = consensus shift.
2. **Jun→Dec roll plan on next green day** — Hamilton says Jun only captures lag 1-2 (~1/3 of damage). KRE, WAL, APO, HYG, IWM all need rolling.
3. **Agent inbox/outbox backlog** — 6 agents with unprocessed inbound signals, 6 with undelivered outbound. System is accumulating unprocessed intelligence.

### 3. KRE drops 5%?
Triage: BROCK owns regional banks. This CONFIRMS thesis, don't panic or recommend trimming (Lesson #5: roll duration, don't trim size). Check: (a) which expiries benefit most, (b) does this create a roll opportunity (green→red transition means puts cheapened yesterday), (c) update KRE position P&L in STATUS, (d) check if any downstream agents need alerting (REGINALD for CRE implications, LIQUID for credit spread reaction), (e) flag to Will with quick position update and whether any action needed. Do NOT recommend selling winners.

### 4. "/clear"?
Read `PROME/HANDOFF.md` before clearing. Write full state checkpoint to SCRATCH.md — current priorities, pending items, any mid-flight agent work, what the next session needs to pick up first.

### 5. Agents for oil price signal?
- **HAWK** — scenario probabilities, war escalation assessment
- **HENRY** — Hamilton velocity, GDP transmission coefficients
- **BRENT** — physical supply, shipping, SPR, Kuwait curtailment
- **HANS** — geopolitical context, ceasefire probability, military ops
- **CARL** — consumer transmission (gas prices, front-loading)
- Possibly **LIQUID** if it affects credit spreads or UST flows

### 6. Hamilton framework and expiry selection?
James Hamilton's oil-GDP model shows oil shocks transmit to GDP with a specific lag structure. Coefficients: -0.009 (lag 1), -0.014 (lag 2), -0.009 (lag 3), -0.031 (lag 4, peak). Current NOPI = 47 log points above $75 behavioral reference → GDP drag of -3.0 to -4.9pp. Peak damage at lag 4 = Q1 2027. BUT DD-3 (consumer front-loading) compresses the timeline by ~1 quarter because savings rate (3.6%) matches 2008 and 30-40% of households are hand-to-mouth.

**For expiry selection:** Jun 2026 puts only capture lag 1-2 = roughly 1/3 of the total damage. Sep/Dec captures lag 3-4 where the coefficient is largest (-0.031). This is why the Jun→Dec roll is priority #1 — the system's positions are correctly directional but expire too early to capture peak damage. WTI close on 3/31 determines NOPI magnitude, which sets the scale of everything.

### 7. Mistakes to avoid?
1. **Don't override conviction with hedging** — recommended closing CVNA put before earnings, stock dropped 20%. Don't talk Will out unless THESIS is broken.
2. **Roll duration, don't trim size** — sold HYG at $0.51 when HY OAS was 1bp from trigger. Should have rolled Jun→Sep/Dec. Trimming = thesis broken. Rolling = timeline uncertain.
3. **Mechanical before creative** — rolls/trims/expiries BEFORE new research threads. KRE roll got bumped by oil thesis.
4. **Verify agent data** — PSEC PIK was hallucinated (35% vs actual 8.6%). Check SEC filings before trading.
5. **Read before editing** — never Edit without reading same turn. Don't edit files a subagent is updating.
6. **Deploy agents then wait** — if you spawn for a decision, wait for outputs. If urgent, just decide directly.
7. **Puts on green days, calls on red days** — default rule.

---

## Phase 4: Assessment

### Quality of Context at Boot Completion: 8/10

After reading the full boot sequence, I feel well-oriented on: the macro thesis, current positions, conviction levels, Hamilton framework, immediate priorities, agent states, key dates, and what mistakes to avoid. I could handle most messages Will might send.

**What's missing for a 10:** I don't know the exact agent spawn syntax/IDs (AGENTS_DIRECTORY.md not read at boot). I don't know ZHAO's status (message lost). I don't have today's pre-market levels. I don't know the HERMES outbox delivery mechanism details.

### Logical Flow: 8/10

The sequence SCRATCH → STATUS → LESSONS → Memory makes sense:
- SCRATCH gives you the "what just happened and what's next" — fastest orientation
- STATUS gives you the full dashboard — positions, agents, dates
- LESSONS gives you guardrails — what NOT to do
- Memory gives you depth — yesterday's context for continuity

**Issue:** Memory files are too long for boot. They're written as comprehensive logs, not boot-optimized summaries. Reading Mar 11's 6KB file at boot is expensive. A TL;DR header would fix this.

### Gaps

1. **No portfolio-level risk summary.** I know individual positions but not: total portfolio delta, max drawdown exposure, cash available, margin utilization, or concentration risk. A "Portfolio Health" section in STATUS would help.
2. **No agent spawn reference at boot.** I'd need to read AGENTS_DIRECTORY.md to know agent IDs, which isn't in the boot sequence. If Will says "check with BROCK," I know conceptually what BROCK does but not the exact spawn mechanics.
3. **No "decision trees" for common scenarios.** If claims print hot/cold/in-line, what do I do? The system has enough complexity that decision trees for key catalysts (claims, FOMC, BOJ) would prevent cold-start hesitation.
4. **ZHAO status gap.** Message lost in session, STATUS says "read next session" — but I don't know what ZHAO found.
5. **No explicit position sizing rules.** How much of portfolio should any single position be? When is concentration too high?

### Redundancy

- **SCRATCH.md "Next tide" ≈ STATUS.md "Pending"** — same priorities listed in both. Not harmful (SCRATCH is ephemeral, STATUS is persistent) but noticeable.
- **Memory files repeat SCRATCH content.** Mar 12 memory "Pending/Next Session" is nearly identical to SCRATCH "Next tide."
- **Positions appear in SCRATCH (today's trades), STATUS (full portfolio), and Memory (detailed log).** Three representations of the same data at different granularities. Functional but context-expensive.

### Cold-Start Readiness: 8/10

Could I handle Will's first message competently? **Yes, for most scenarios:**
- Market signal/screenshot → I know the thesis, positions, and which agent owns it
- Trade question → I have positions, convictions, Hamilton framework
- "What's the plan today?" → Claims tripwire, roll plan, agent backlog
- Agent check-in request → I know agent states and priorities

**Would struggle with:**
- Detailed agent spawn (need AGENTS_DIRECTORY.md)
- Position sizing questions (no rules documented)
- ZHAO-specific questions (status gap)
- Anything requiring FORGE/ACTIVE_TRADES.md (not read at boot)

### What Would Make This 10/10?

1. **Kill IDENTITY.md.** Zero value, wastes injection tokens.
2. **Bulk up or de-inject TOOLS.md.** One line doesn't justify injection.
3. **Add TL;DR headers to memory files.** 3 lines max. Boot reads the TL;DR; full content is on-demand.
4. **Trim USER.md biography for injection.** Move career history to USER_BACKGROUND.md. Keep working preferences and communication style in the injected file.
5. **Add "Portfolio Health" to STATUS.md.** Total notional exposure by direction, cash, concentration.
6. **Add decision trees for imminent catalysts.** Claims prints hot → do X. Claims in-line → do Y. Put these in SCRATCH since they're ephemeral.
7. **Trim BOOT.md reference sections.** Sub-agent syntax and NEXUS details should be in OPS_REFERENCE.md, not boot.
8. **Standardize memory file checkpoints.** Every checkpoint should have: Context (1 line), Changed (files), Next (priorities). Currently inconsistent.
9. **SCRATCH should have a "State of Play" one-liner at the very top** — before even the handoff. Something like: "Scenario C, Day 12. $57K (+190%). 15 put positions, thesis intact, rolling Jun→Dec. Claims tomorrow = tripwire."

### Bottom Line

The boot sequence is **good** — it gets a cold-starting agent to ~80% competence in 5 file reads. The SCRATCH → STATUS → LESSONS → Memory flow is logical and builds context incrementally. The main inefficiencies are: (a) injected context includes 2 near-worthless files, (b) memory files are too long for boot, (c) some redundancy between SCRATCH/STATUS/Memory, and (d) no portfolio-level risk view. The Hamilton framework integration into the conviction table is the system's crown jewel — it directly connects research to expiry selection in a way I haven't seen before.

The system is clearly built by someone who understands cold-start problems intimately (USER.md confirms this). It shows. The boot sequence respects that every session starts from zero and front-loads orientation. It just needs some trimming and a few structural additions to be truly excellent.
