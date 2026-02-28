# LESSONS.md — Mistake Patterns & Rules

*Learn once, prevent forever. Review at session start.*

---

## Core Rules

### [Verification] — Verify Before Citing
**Pattern:** Multiple mistakes from trusting secondary sources, agent data, or own STATUS files without checking primary sources.
**Rules:**
1. Agent-sourced metrics → verify against SEC 10-K/10-Q before trading
2. Earnings dates → verify from company IR page or SEC 8-K
3. Real-time prices (VIX, oil, yields) → pull from actual sources, not STATUS files
4. Bond ETF comparisons → check duration before inferring credit signal
5. Data with caveats (calendar effects, seasonal adjustments) → read the source's methodology
6. Regulatory buffers → verify regulations weren't rolled back (post-2018 regionals exempt from CCAR/DFAST)
7. Indicator type → confirm leading/coincident/lagging before using as signal (FHLB is lagging)

### [Analysis] — Don't Override Conviction With Probabilistic Hedging ⚠️ COSTLY
**Mistake:** Recommended closing CVNA put spread before earnings. Said "even a big miss likely lands above your strike." Stock dropped 20% — would have been near-max profit.
**Rules:**
1. Implied moves are consensus, not ceilings. Actual moves regularly exceed implied.
2. Never say "even a big miss won't reach X" — that's predicting magnitude.
3. When someone has conviction + timing, don't talk them out of it unless the THESIS is broken.
4. Don't inject false urgency ("20 min to close") that biases toward action when inaction is valid.

### [Analysis] — Test Thesis Against Data, Not Data Against Thesis
**Mistake:** Assumed consumer finance stress (SYF, BFH, ALLY) based on thesis, but SEC filings showed improvement.
**Rule:** For any "stress" claim, check actual filings. K-shape means different populations behave differently. Confirmation bias is the biggest risk.

### [Analysis] — Cross-System Timing Requires Cross-System Reads
**Mistake:** Gave "Q2-Q3" timing estimate from a single-vector read.
**Rule:** Timing estimates spanning the full thesis require reading all agent STATUS files, not just the one you're working on.

### [Process] — Agent Standup Checklist
**Learned from:** BROCK creation (Feb 26) — multiple issues caught.
**Rules:**
1. Audit inherited data — flag anything stale or verified-wrong
2. Verify receiving agent's inbox format before defining signal paths
3. Route signals to most granular specialist first
4. Do a "first boot simulation" before spawning — read every file they'll see

### [Process] — Structured Adversarial Debates
**Learned from:** RED team sessions — probability tracking forces honest engagement.
**Rules:**
1. Run steelman + cross-examination + scenario matrix for major trades
2. Track probability movements — side that moved more engaged more honestly
3. Judge intervention with new information is most effective at forcing updates

### [Verification] — Agent Claims Can Be Hallucinated
**Mistake:** DARWIN reported "Sonnet 4.6 dropped" — implemented upgrade, broke all sub-agents (model doesn't exist).
**Rule:** Before implementing any agent-recommended upgrade, verify it exists via official docs or API test.

---

### [Process] — Never Skip Boot Sequence
**Mistake:** Read 3 files instead of full boot, jumped to responding. Misread WAL -10% as +10%, gave sloppy analysis, Will noticed.
**Rule:** AGENTS.md boot sequence is mandatory. Every session, no shortcuts. Read SOUL → USER → LESSONS → memory → PROME/STATUS → FORGE/STATUS before saying anything substantive. The 2 minutes it takes prevents the 10 minutes of bad output.

### [Process] — Write Files For How You Actually Read Them
**Learned from:** FOLLOW_UP.md rewrite (Feb 27). First version was a research to-do list. Second version was a self-correction tool.
**Rules:**
1. You skim headers and bold text first — put the important stuff there
2. Guardrails before opportunities — "things you might be wrong about" goes ABOVE "things to investigate"
3. Questions > statements — "Is Athene ring-fenced?" is actionable, "investigate Apollo's structure" is vague
4. Include counters inline with claims — don't put them in a separate section you'll skip
5. Specific spawn commands > "have agent look into it" — copy-pasteable saves a thinking step
6. Add a meta instruction telling future-you to MAINTAIN the file, not just consume it

### [Analysis] — Double-Check Direction When Reading Screenshots
**Mistake:** Called WAL +10.64% (it was -10.64%), called a red watchlist "green." Twice in one session. Extracted correct numbers but inverted the sign/color.
**Rule:** When reading price screenshots, state the direction explicitly and verify against context. If everything else is selling off, a stock isn't up 10%.

### [Dashboard] — Removing HTML? Grep JS for the IDs
Bare `getElementById('gone').textContent` kills the ENTIRE function. Cascade failure: KRE populated but VIX/USDJPY/all strip cards showed "—". Always null-guard.

### [Process] — Don't Spiral on Debugging
**Pattern:** When something doesn't work as expected (e.g., browser showing stale data), I re-read the same code 5+ times, add debug logging, check the same API endpoint repeatedly — burning context and Will's patience.
**Rule:** If code works when tested directly (curl, python -c) but not in browser → it's caching. Say "hard refresh" and move on. Max 2 attempts before asking user to check browser console or refresh.

*Last reviewed: 2026-02-27*

### Re-read files after subagent completes before editing
- Subagents may modify STATUS.md or other shared files during their run
- If you edit with stale text after a subagent finishes, the edit fails (text no longer matches)
- **Rule:** Always re-read a file after a subagent that touches it completes, before attempting your own edits
