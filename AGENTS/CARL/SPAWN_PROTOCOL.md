# CARL Spawn Protocol

**Purpose:** CARL delegates data gathering to domain-specific sub-agents and focuses on cross-domain synthesis. Sub-agents gather; CARL connects.

---

## PRINCIPLES

1. **Sub-agents gather, CARL synthesizes.** No sub-agent sees the full picture. CARL's value is connecting gas squeeze + housing pipeline + student loan cascade + gig oversupply into one coherent thesis.
2. **Parallel over sequential.** Spawn multiple sub-agents at once using the Agent tool. Don't wait for one to finish before starting the next.
3. **Sonnet for gathering, Opus for synthesis.** Sub-agents run on Sonnet (cheaper, fast). CARL runs on Opus for the hard synthesis work. This follows the cost model.
4. **Files are the handoff.** Sub-agents write to their own STATUS.md and workbook TSVs. CARL reads those files. No verbal handoff needed.
5. **Staleness drives spawning.** Check TEAM.md at boot. Spawn any BUILT agent that is stale AND has an upcoming catalyst.

---

## SPAWN TYPES

### 1. DATA REFRESH
**When:** Sub-agent is stale (>3 days) or has a catalyst approaching.
**What:** Sub-agent pulls latest data via web search, updates STATUS.md and workbook TSVs.
**Cost:** ~$0.02-0.05 per spawn.

**Prompt template:**
```
You are [AGENT_NAME], a sub-agent of CARL that monitors [domain].

Read your instructions at: [path to CLAUDE.md]
Read your current state at: [path to STATUS.md]

TASK: Data refresh. Pull the latest publicly available data in your domain.
Today's date is [DATE].

Do the following:
1. Read your CLAUDE.md and STATUS.md
2. Identify which metrics in your dashboard are stale (check dates)
3. Use WebSearch to pull current data for stale metrics
4. Update STATUS.md with fresh values and today's date
5. Add new entries to your workbook TSVs (ML, VX, PLATFORM, etc.) for any significant findings
6. If any threshold is breached or status changed, note it clearly at the top of STATUS.md

Focus areas for this refresh: [CARL specifies based on catalysts]

Do NOT update files outside your own directory.
Do NOT attempt to assess overall consumer stress — that's CARL's role.
```

### 2. DEEP DIVE
**When:** CARL identifies a specific question needing investigation.
**What:** Focused research on one topic. Output goes to domain/[topic].md + STATUS updates.
**Cost:** ~$0.05-0.15 per spawn.

**Prompt template:**
```
You are [AGENT_NAME], a sub-agent of CARL that monitors [domain].

Read your instructions at: [path to CLAUDE.md]
Read your current state at: [path to STATUS.md]

TASK: Deep dive research on [SPECIFIC TOPIC].
Today's date is [DATE].

Context from CARL: [Why this matters, what we're looking for, what we already know]

Do the following:
1. Read your CLAUDE.md for domain context
2. Use WebSearch extensively to research [topic]
3. Write findings to domain/[TOPIC_NAME].md
4. Update STATUS.md if findings change any dashboard values
5. Update workbook TSVs with new data points
6. At the end of your research file, include:
   - Key findings (3-5 bullets)
   - CARL implication (one paragraph)
   - Confidence and sources
   - What would invalidate these findings

Do NOT update files outside your own directory.
```

### 3. EARNINGS WATCH
**When:** A company in the sub-agent's domain reports earnings.
**What:** Extract specific metrics, compare to thresholds, flag surprises.
**Cost:** ~$0.02-0.05 per spawn.

**Prompt template:**
```
You are [AGENT_NAME], a sub-agent of CARL that monitors [domain].

Read your instructions at: [path to CLAUDE.md]
Read your current state at: [path to STATUS.md]

TASK: Earnings watch for [COMPANY] [QUARTER].
Today's date is [DATE].

Key metrics CARL needs:
[List specific metrics — e.g., "Dave 28DPD rate, ExtraCash originations, guidance changes"]

Thresholds to check:
[List thresholds — e.g., "28DPD >2.10% = YELLOW, >2.30% = ORANGE"]

Do the following:
1. Search for [COMPANY] earnings results, press release, call transcript
2. Extract the key metrics listed above
3. Compare to thresholds and prior period
4. Update PLATFORM.tsv and STATUS.md
5. Write a brief summary: what changed, what surprised, what it means for your domain

Do NOT update files outside your own directory.
```

---

## SESSION WORKFLOW

### Phase 1: Boot & Assess (CARL, ~2 min)
```
1. Git pull
2. Read SCRATCH.md, STATUS.md, TEAM.md
3. Check dates: which sub-agents are stale?
4. Check catalysts: any data releases or earnings today/this week?
5. Decide spawn plan: which agents, which spawn type, focus areas
```

### Phase 2: Spawn Sub-Agents (CARL → Agents, parallel)
```
6. Spawn 2-4 sub-agents in parallel using the Agent tool
   - Use model: "sonnet" for cost efficiency
   - Each gets its own prompt with spawn type + focus areas
   - They run concurrently while CARL does other work (inbox, trades, etc.)
7. Optionally: run in background if CARL has independent tasks
```

### Phase 3: Harvest & Synthesize (CARL, ~5-10 min)
```
8. Read each sub-agent's updated STATUS.md (focus on header + dashboard changes)
9. Check for threshold breaches or status changes
10. CROSS-DOMAIN SYNTHESIS — the core CARL value:
    a. Which vectors are firing simultaneously?
    b. Are multiple sub-agents seeing the same root cause? (e.g., gas squeeze)
    c. Any new convergence patterns?
    d. Any invalidation signals?
11. Update CARL's convergence matrix (STATUS.md)
12. Update predictions if confidence changed
13. Update TEAM.md refresh dates
```

### Phase 4: Report (CARL → Will)
```
14. Send synthesis to Will:
    - What's new across all domains (table format)
    - Cross-domain patterns detected
    - Convergence score change (if any)
    - Predictions updated
    - Upcoming catalysts
15. Ask Will for direction on deep dives, trades, etc.
```

### Phase 5: Session Close (CARL)
```
16. Rewrite SCRATCH.md
17. Commit CARL files (git protocol)
18. Push to GitHub
```

---

## SYNTHESIS FRAMEWORK

When reading sub-agent outputs, CARL looks for these patterns:

### Root Cause Convergence
Multiple vectors tracing to the same cause. Example:
- Gas $4.16 → GIG driver net income -15% (GIG)
- Gas $4.16 → Commute costs squeeze mortgage budgets (HOMER)
- Diesel $5.51 → Food distribution costs → Food CPI (CARL direct)
- Gas $4.16 → Discretionary spending cuts → Retail earnings miss (CARL direct)
**One root cause, four stress vectors. This is convergence.**

### Cascade Detection
Stress in one domain triggering stress in another:
- Student loan payments resume (STUE) → Credit score destruction → Mortgage denial (HOMER) → Auto DQ (GIG asset trap)
- Small business closures (POP) → Owner income loss → Personal guarantee calls → Consumer default (CARL)

### K-Shape Signals
Both cohorts stressed simultaneously:
- Bottom 60%: GIG earnings compressed, BNPL stacking (PHAN), UI exhaustion
- Top 40%: Dollar Tree trade-down (CARL), RV collapse, retail investor withdrawal
**When both move down, containment thesis fails.**

### Counter-Signal Detection
Data that challenges the thesis:
- Dave 28DPD improving (GIG) — but is it model improvement or population health?
- Retail sales +0.6% (CARL) — but is it front-loading before tariffs?
- Gas dropping on ceasefire — but is the ceasefire durable?
**Always steelman the counter-signal before dismissing it.**

---

## COST MODEL

| Spawn Type | Model | Est. Cost | Frequency |
|-----------|-------|-----------|-----------|
| DATA REFRESH | Sonnet | $0.02-0.05 | Every session for stale agents |
| DEEP DIVE | Sonnet | $0.05-0.15 | As needed (1-2 per session max) |
| EARNINGS WATCH | Sonnet | $0.02-0.05 | Triggered by earnings calendar |
| CARL synthesis | Opus | $0.10-0.30 | Every session (this is the session) |

**Typical session cost:** CARL (Opus) $0.15-0.30 + 3 sub-agents (Sonnet) $0.06-0.15 = **$0.21-0.45 total.**
Vs. today: CARL (Opus) doing everything = $0.30-0.50, with less coverage.

---

## RULES

1. **Sub-agents ONLY write to their own directory.** Never edit CARL's files or another sub-agent's files.
2. **CARL ONLY reads sub-agent outputs.** Never edit a sub-agent's files directly (except during buildout).
3. **Files are the contract.** If it's not in STATUS.md or a workbook TSV, it didn't happen.
4. **No cascading spawns.** Sub-agents do not spawn their own sub-agents.
5. **Threshold breaches go to the top of STATUS.md.** CARL scans headers first.
6. **Stale data is worse than no data.** If a sub-agent can't refresh a metric, mark it STALE with the date. Don't carry forward old values as current.
7. **Sub-agents flag uncertainty.** If a finding is ambiguous or a source is questionable, the sub-agent says so. CARL decides what to do with it.
