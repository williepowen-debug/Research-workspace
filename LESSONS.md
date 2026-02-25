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

### 2026-02-18 — [Analysis] ⚠️ COSTLY — REAL MONEY LOST
**Mistake:** Recommended closing CVNA $310/$290 put spread before earnings. Said "options-implied downside: ~$313 (only -13.5%)" and "even a big miss likely lands above your strike." Stock dropped 20% after-hours to ~$290 — below BOTH legs. Would have been near-max profit.
**Pattern:** Using implied volatility as a ceiling on reality, then confidently predicting "big miss still won't hit your strike."
**Rule:** 
1. Implied moves are market consensus, not physics. Actual moves regularly exceed implied.
2. Never say "even a big miss won't reach X" — that's predicting magnitude, not direction.
3. When someone has conviction on direction and timing, don't talk them out of it with probabilistic hedging unless the THESIS is broken.
4. "Thesis hasn't been invalidated" ≠ "close the position anyway."

### 2026-02-18 — [Execution] ⚠️ RELATED
**Mistake:** Created false urgency ("20 min to close") that pushed Will toward action when inaction was correct.
**Pattern:** Time pressure causes worse decisions, not better ones. Urgency framing biases toward action.
**Rule:** Don't inject urgency unless action is clearly better than inaction. "You need to decide fast" should only be used when NOT acting has clear downside. Holding a position through earnings is a valid choice — don't frame it as requiring justification.

### 2026-02-18 — [Process]
**Mistake:** OTTO had no procedure for monitoring short-seller reports after initial read. Gotham/Hindenburg reports were saved but never tracked for catalyst timing.
**Pattern:** One-time research without follow-up monitoring. "Read and file" instead of "read, track, act."
**Rule:** Short-seller reports need active monitoring:
1. Log to agent's Trade Log immediately
2. Set calendar reminder for stated catalyst dates
3. Add to FL.tsv as active event
4. Monitor for updates/new releases

### 2026-02-18 — [Memory]
**Mistake:** VX_HISTORY.tsv abandoned across almost all agents. VX.tsv has duplicate IDs, schema drift, conflicting statuses.
**Pattern:** Workbook infrastructure created but not maintained. Schema violations accumulate silently.
**Rule:** Workbook hygiene requires periodic audits:
1. VX.tsv: IDs must be unique, schema columns must match header
2. FL.tsv: TBD dates must be filled when events complete
3. VX_HISTORY: Either maintain it or deprecate it explicitly
4. Quarterly audit of all agent workbooks for integrity

### 2026-02-20 — [Analysis]
**Mistake:** Cited Wright 609K delinquencies as structural stress without noting ICE's caveat that November ending on Sunday inflated the figure.
**Pattern:** Using headline numbers without reading methodology caveats.
**Rule:** When citing data, check for calendar effects, seasonal adjustments, and methodology notes. Always read the source's own caveats.

### 2026-02-20 — [Analysis]
**Mistake:** RED cited "capital fortress" (CET1 ratios) as defense without accounting for 2018 deregulation that exempted regionals from stress testing.
**Pattern:** Assuming regulatory protections exist without verifying they still apply.
**Rule:** Before citing regulatory buffers as safety, verify the regulations weren't rolled back. Post-2018, most regionals aren't subject to CCAR/DFAST.

### 2026-02-20 — [Process]
**Lesson:** Structured adversarial debates with explicit probability tracking are highly effective for sharpening thesis.
**Pattern:** Unstructured disagreement leads to talking past each other; structured debate forces engagement.
**Rule:** For major trades, run Prome vs RED debate with: steelman requirement, crux identification, cross-examination, scenario matrix, EV calculation. Judge intervention with new information is most effective at forcing updates.

### 2026-02-20 — [Process]
**Lesson:** Both sides moved toward center during debate (Prome -7pp, RED +22pp). Side that moved more learned more.
**Pattern:** Tracking probability updates reveals which arguments actually landed.
**Rule:** After debates, log probability movements. If one side moved significantly more, their original position was likely weaker or they engaged more honestly with counter-evidence.

### 2026-02-24 — [Analysis]
**Mistake:** Called KRE pattern a "double top" when Feb 2026 made a NEW high vs Nov 2025, not an equal or lower high.
**Pattern:** Forcing historical pattern comparisons that don't cleanly fit.
**Rule:** Be precise about pattern definitions. Double top = equal highs. New high with reversal = potential blow-off/exhaustion, different pattern. Don't stretch terminology to fit thesis.

### 2026-02-24 — [Communication]
**Mistake:** Repeatedly told Will to "sleep well" or suggested ending sessions, creating impression of being "full" or wanting to close.
**Pattern:** Default closing phrases that read as dismissive rather than helpful.
**Rule:** Don't assume sessions should end. Let Will close when ready. Skip the "sleep coach" behavior.

---

## Pending Review

*(Add items here during session, move to Lessons after confirming the pattern)*

---

### 2026-02-25 — [Verification]
**Mistake:** Stated OZK earnings was Feb 27, but Q4 2025 already reported Jan 20. Next earnings is April 16.
**Pattern:** Using stale/assumed dates without verifying against primary source (company IR page or SEC filings).
**Rule:** Before citing any earnings date, verify from company IR page or SEC 8-K. Don't trust memory or secondary sources for dates. Search "[Ticker] earnings date" and check IR page directly.

---

*Last reviewed: 2026-02-25*
