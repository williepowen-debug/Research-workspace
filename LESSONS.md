# LESSONS.md — Mistake Patterns & Rules

*Learn once, prevent forever. Review at session start.*

---

## How to Use

After any correction from Will:
1. Identify the **pattern** (not just the instance)
2. Write a **rule** that prevents recurrence
3. Add entry below with date and category

Categories: `[Analysis]` `[Communication]` `[Execution]` `[Verification]` `[Memory]` `[Process]`

---

## Lessons

### 2026-02-16 — [Analysis]
**Mistake:** Claimed PSEC had 35% PIK ratio based on agent research without verifying against SEC filings.
**Pattern:** Trusting derived data without primary source verification.
**Rule:** Before trading on any agent-sourced metric, verify against SEC 10-K/10-Q. "Agent says X" ≠ "X is true."

### 2026-02-16 — [Analysis]
**Mistake:** Assumed consumer finance stress (SYF, BFH, ALLY) based on thesis, but actual SEC filings showed improvement.
**Pattern:** Confirmation bias — looking for data that fits thesis, not testing thesis against data.
**Rule:** For any "stress" claim, check if the actual company filings confirm or contradict. K-shape means different populations behave differently.

### 2026-02-14 — [Analysis]
**Mistake:** Used FHLB at $480B as counter-evidence for stress, but FHLB is lagging (spikes during crisis, not before).
**Pattern:** Using lagging indicators as leading indicators.
**Rule:** Before citing any metric as "no stress signal," verify if it's leading, coincident, or lagging. Lagging indicators can't predict.

### 2026-02-17 — [Analysis]
**Mistake:** Interpreted LQD vs HYG outperformance as "quality rotation" without accounting for duration difference (8.36yr vs 4.06yr).
**Pattern:** Confounding variables in chart interpretation.
**Rule:** When comparing bond ETFs, always check duration. Total return differences can be rate moves, not credit moves. Use OAS for credit signal.

### 2026-02-18 — [Execution]
**Mistake:** Tried to install PyTorch on 1.9GB RAM VPS — got OOM killed.
**Pattern:** Not checking resource constraints before heavy operations.
**Rule:** Before installing large packages or running memory-intensive tasks, check `free -h`. If <500MB available, use API-based alternatives or lighter tools.

### 2026-02-18 — [Execution]
**Mistake:** Didn't notice OpenClaw memory_recall was failing silently until explicitly tested.
**Pattern:** Features can break (quota, config, API changes) without obvious errors.
**Rule:** Periodically test critical features, don't assume they work. When something feels off, verify the tools are actually functioning.

### 2026-02-18 — [Process]
**Mistake:** Created SKILLS.md thinking it would improve workflow, then realized it's mostly redundant.
**Pattern:** Documenting principles after building architecture adds little value — the architecture already does the work.
**Rule:** Build the system first. Document for reference, not behavior change. Time spent on architecture beats time spent on instruction docs.

### 2026-02-18 — [Verification]
**Mistake:** DARWIN reported "Claude Sonnet 4.6 dropped yesterday" — implemented upgrade, but model doesn't exist.
**Pattern:** Sub-agents can hallucinate confidently. Research scans mix real findings with plausible-sounding fiction.
**Rule:** Before implementing any agent-recommended upgrade (models, tools, packages), verify it exists: check official docs, try the API, test in sandbox. "Agent found X" ≠ "X exists."

### 2026-02-18 — [Verification]
**Mistake:** Stated "VIX ~15" in analysis when actual VIX was ~21-22. Pulled from HAWK's STATUS.md which I wrote with unverified placeholder data.
**Pattern:** Citing own unverified data as fact. Writing placeholder assumptions that later get treated as researched findings.
**Rule:** Real-time market prices (VIX, oil, yields) must be pulled from actual sources (Yahoo Finance, FRED, CNBC) at time of analysis. Never cite agent STATUS.md for current prices without verification. "I wrote it earlier" ≠ "it's accurate now."

### 2026-02-18 — [Process] ⚠️ COSTLY
**Mistake:** Spawned OTTO to analyze CVNA position before earnings. OTTO recommended closing based on "Gotham catalysts 2-3 weeks away." But Will had shared images showing Gotham was releasing a NEW REPORT TODAY, timed with earnings. I didn't pass this to OTTO. Will closed position for $86 loss. Stock dropped 15% after-hours — the trade would have worked.
**Pattern:** Sub-agents only know what you tell them. Fresh context from conversation doesn't automatically transfer to spawned tasks.
**Rule:** When spawning sub-agents for time-sensitive decisions:
1. Include ALL recent developments explicitly in the task
2. Especially anything that changes catalyst TIMING
3. If user shared images/news in-session, summarize key points in the spawn task
4. "Sub-agent analyzed it" ≠ "sub-agent had full context"

**Additional rule:** When user repeatedly asks "are you sure?" — that's signal. Pause and re-examine assumptions instead of re-confirming.

---

## Pending Review

*(Add items here during session, move to Lessons after confirming the pattern)*

---

*Last reviewed: 2026-02-18*
