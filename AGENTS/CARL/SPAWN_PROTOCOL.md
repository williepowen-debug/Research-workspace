# CARL Spawn Protocol

**Purpose:** CARL delegates data gathering to domain-specific sub-agents and focuses on cross-domain synthesis. Sub-agents gather; CARL connects.

**Last meaningful update:** 2026-07-10 (post-restructure: SV-channel canon, DATA-REFRESH checklist, downward-propagation rule, roster reality — see DAEDALUS `CARL_SUBAGENT_AUDIT_2026-07-10.md`) | **Prior hygiene pass:** 2026-05-31

---

## SCOPE OF THIS FILE

CARL's boot/session-end protocol lives in `CLAUDE.md` SPAWN PROTOCOL (14 steps, including docket countdown + PREDICTIONS scan). **This file is about spawning sub-agents** — when, how, with what prompt. Roster + staleness lives in `TEAM.md`; which sub-agent each upcoming catalyst maps to lives in `docket/CATALYSTS.tsv` (`who_cares` column).

**Roster reality (2026-07-10 restructure):** **standing** = STUE, HOMER, DOC, GIG · **dossier-mode** = PHAN (ad-hoc spawns against `PHAN/DOSSIER.md`; CLAUDE/STATUS frozen) · **standing pending refresh-then-demote at catalyst** = POP (Jul-24 Sub-V) and POLLY (Q2 P&C ~late Jul) · **frozen** = META (harvested 7/10) · COOK never built (disposition: dead as standing agent — DOC dossier-section or ad-hoc spawn if OBBBA/SNAP fires, Dec-2026 window).

**SV channel (canonical, 2026-07-10):** each sub-agent delivers state vectors to **its own `state_vectors/` dir** (`SV-<NAME>-YYYY-MM-DD-NN.md`). CARL harvests there at Phase B. The old `../SHARED/state_vectors/` path never existed — any remaining reference is a defect. GIG migrated from `outbox/` delivery 2026-07-10; pre-migration SVs remain in `GIG/outbox/` as history.

---

## PRINCIPLES

1. **Sub-agents gather, CARL synthesizes.** No sub-agent sees the full picture. CARL's value is connecting gas squeeze + housing pipeline + student loan cascade + gig oversupply + insurance K-shape Selection into one coherent thesis.
2. **Parallel over sequential.** Independent sub-agent spawns go in ONE message with multiple Agent tool calls — never sequentially (auto-memory [[feedback_parallel_spawn_independent_agents]]). Don't wait for one to finish before starting the next.
3. **Sonnet for gathering, Opus for synthesis.** Sub-agents run on Sonnet (cheaper, fast). CARL synthesizes on Opus. Follow the cost model.
4. **Files are the handoff.** Sub-agents write to their own STATUS.md and workbook TSVs. CARL reads those files. No verbal handoff needed.
5. **Staleness + catalyst drives spawning.** Check TEAM.md staleness; check docket for which sub-agent owns the next catalyst. Spawn any BUILT agent that is stale AND has a near-term catalyst.

---

## SPAWN TYPES

### 1. DATA REFRESH
**When:** Sub-agent is stale (>7d for monitoring; >3d if a catalyst just fired in its domain) or has a catalyst approaching in the docket.
**What:** Sub-agent pulls latest data via web search, updates STATUS.md and workbook TSVs.
**Cost:** ~$0.02-0.05 per spawn.

**Refresh exit-checklist (mandatory — the TSV half was systematically skipped for 3 months; audit must-fix #1):**
- [ ] STATUS.md dashboard values updated (source+date each)
- [ ] **Every workbook TSV touched or `[STALE — <date>]`-marked** — no TSV left silently at prior vintage
- [ ] **Every own-ledger prediction past its resolver dispositioned** — resolve / re-arm with reason / `⚠ DUE-UNRESOLVED [DATA-NEEDED: …]`
- [ ] State vector written to own `state_vectors/`
- [ ] KB row logged for new facts

### 2. DEEP DIVE
**When:** CARL identifies a specific question needing investigation.
**What:** Focused research on one topic. Output goes to `domain/sources/[topic].md` + STATUS updates.
**Cost:** ~$0.05-0.15 per spawn.

### 3. EARNINGS WATCH
**When:** A company in the sub-agent's domain reports earnings (from docket).
**What:** Extract specific metrics, compare to thresholds, flag surprises.
**Cost:** ~$0.02-0.05 per spawn.

---

## SUB-AGENT PROMPT DISCIPLINE

Per auto-memory [[feedback_subagent_prompt_discipline]] — four rules for sub-agent research prompts:

1. **Decision-lead** — open with the decision the spawn enables ("CARL needs to know whether to upgrade V12 score before Jun 16-17 SEP"), not the topic.
2. **Word cap** — give a target length ("under 400 words" / "verdict + 3 bullets"). Without one, models pad.
3. **Decision-usefulness** — every section in the spawn's output must change something CARL would do; if it wouldn't, cut it from the prompt.
4. **Verdict-first** — require the spawn to lead with its conclusion, then evidence. CARL reads verdicts first; evidence on demand.

Don't over-template. The four rules apply to all three spawn types; pasting a long boilerplate template usually violates rule 3.

### Adversarial-pair spawns (when used)
Per auto-memory [[feedback_adversarial_brief_for_pair_teams]] — when spawning a pair to disagree (e.g., bull vs. bear take on the masking framework, or RED steelman + CARL bear), brief them explicitly toward genuine disagreement. Without the framing, both default to the same default-judicious tone and the second voice adds nothing.

---

## PROMPT TEMPLATES

These are starting points, not boilerplate. Adapt per the four rules above.

### DATA REFRESH
```
You are [AGENT_NAME], a sub-agent of CARL monitoring [domain].

DECISION THIS SUPPORTS: [one sentence — what CARL will do differently based on this refresh]

Read CLAUDE.md and STATUS.md in your directory. Today's date is [DATE].

Refresh stale dashboard metrics in your STATUS.md using WebSearch. Focus areas: [CARL specifies — usually 2-4 specific metrics tied to upcoming docket catalysts].

For each refreshed metric: update STATUS.md value + date, log a KB row, update VX if threshold band changed. If any threshold breaches, put it at the top of STATUS.md.

Output back to CARL: verdict (1 line: "no change" / "X breached" / "Y newly stale"), then up to 5 bullets of evidence. Under 300 words.

Do NOT update files outside your own directory.
```

### DEEP DIVE
```
You are [AGENT_NAME], a sub-agent of CARL monitoring [domain].

DECISION THIS SUPPORTS: [what CARL will conclude or do differently]

Topic: [SPECIFIC QUESTION]
What CARL already knows / has ruled out: [paste 3-5 lines]

Research the topic via WebSearch. Write findings to domain/sources/[TOPIC].md with:
- Verdict (1-2 sentences leading the file)
- 3-5 key findings (bullets)
- CARL implication (one paragraph: what this changes for the thesis / a vector / a prediction)
- Confidence + sources
- What would invalidate

Update STATUS.md only if findings change a dashboard value. Update workbook TSVs.

Output back: verdict + which CARL artifact you wrote to. Under 400 words.

Do NOT update files outside your own directory.
```

### EARNINGS WATCH
```
You are [AGENT_NAME], a sub-agent of CARL monitoring [domain].

DECISION THIS SUPPORTS: [usually: whether [VECTOR] or [PREDICTION] needs to move]

Earnings: [COMPANY] [QUARTER], reported [DATE].

Metrics CARL needs (extract these exactly): [list]
Thresholds to compare against: [list with bands]

Search for press release + call transcript. Extract metrics, compare to prior period + thresholds.

Update PLATFORM/CARRIER/SECTOR TSV (your sub-agent's domain TSV) + STATUS.md. Log a KB row.

Output back: verdict (1 line: beat/miss/neutral on thesis), then metric table + 3 lines of management commentary that matter. Under 250 words.

Do NOT update files outside your own directory.
```

---

## SESSION WORKFLOW (sub-agent phases — boot is in CLAUDE.md)

### Phase A: Spawn (CARL → sub-agents, parallel)
- Spawn 2-4 sub-agents in ONE message with multiple Agent calls — model: sonnet (or opus for synthesis-heavy deep dives).
- Each gets its own prompt per the four discipline rules above.
- Use `run_in_background: true` if CARL has independent work (workbook updates, STATUS edits) it can do while they run.

### Phase B: Harvest & Synthesize (CARL, ~5-10 min)
- Read each sub-agent's STATUS.md header + dashboard changes. Don't re-read whole files unless verdict says something material.
- Check for threshold breaches or status changes.
- **Cross-domain synthesis (the core CARL value):**
  - Which vectors are firing simultaneously?
  - Are multiple sub-agents seeing the same root cause? (e.g., gas squeeze hits GIG + HOMER + PHAN at once)
  - New convergence patterns?
  - Invalidation signals?
- Update CARL's STATUS.md (convergence matrix mirror, dashboard rows).
- Update PREDICTIONS.tsv if confidence changed; log to CHANGELOG.md.
- Update TEAM.md refresh dates.

### Phase C: Close
- Update docket (prune fired catalysts; add new).
- Update ROADMAP.md (RECENTLY RESOLVED + OPEN THREADS).
- Rewrite SCRATCH.md per CLAUDE.md template.
- Commit + push (per root CLAUDE.md git protocol).

---

## SYNTHESIS FRAMEWORK

When reading sub-agent outputs, CARL looks for these patterns:

### Root Cause Convergence
Multiple vectors tracing to one cause. Example shape:
- Gas pump up → GIG driver net income down (GIG)
- Gas pump up → commute costs squeeze mortgage budgets (HOMER)
- Diesel up → food distribution costs → Food CPI (CARL direct)
- Gas pump up → discretionary cuts → retail comps (CARL direct)
**One root cause, four stress vectors = convergence.**

### Cascade Detection
Stress in one domain triggering stress in another:
- Student loan payments resume (STUE) → credit score destruction → mortgage denial (HOMER) → auto DQ (GIG asset trap)
- Small business closures (POP) → owner income loss → personal guarantee calls → consumer default (CARL)
- Insurer membership culling (POLLY) → forced consumption persists at higher cost → savings depletion (CARL Real DPI)

### K-Shape Signals
Both cohorts stressed simultaneously:
- Bottom 60%: GIG earnings compressed, BNPL stacking (PHAN), UI exhaustion, plasma donations
- Top 40%: Dollar Tree trade-down (CARL), RV collapse, retail-investor withdrawal, condo K-shape (HOMER)
**When both move down, containment thesis fails.**

### Counter-Signal Detection
Data that challenges the thesis (per auto-memory [[feedback_red_edge]] — always steelman):
- BNPL issuer profitable (Klarna Q1) — but is consumer cohort distress unchanged?
- Headline NCO clean (SYF/ALLY) — but is it masking framework (12-24mo visibility lag)?
- Gas reverting — but is the next Iran-kinetic re-spike still loaded?
**Counter-signals route to RED via `handoff_RED/COUNTER_LOG.md`. CARL does not maintain those files (May 1 architectural decision).**

---

## COST MODEL

| Spawn Type | Model | Est. Cost | Frequency |
|-----------|-------|-----------|-----------|
| DATA REFRESH | Sonnet | $0.02-0.05 | Every session for stale agents with near-term catalyst |
| DEEP DIVE | Sonnet | $0.05-0.15 | As needed (1-2 per session max) |
| EARNINGS WATCH | Sonnet | $0.02-0.05 | Triggered by docket earnings dates |
| CARL synthesis | Opus | $0.10-0.30 | Every session (this is the session) |

**Typical session cost:** CARL (Opus) $0.15-0.30 + 3 sub-agents (Sonnet) $0.06-0.15 = **$0.21-0.45 total.**

---

## RULES

1. **Sub-agents ONLY write to their own directory.** Never edit CARL's files or another sub-agent's files.
2. **CARL ONLY reads sub-agent outputs.** Never edit a sub-agent's files directly (except during buildout). Per root CLAUDE.md Critical Rule #2.
3. **Files are the contract.** If it's not in STATUS.md or a workbook TSV, it didn't happen.
4. **No cascading spawns.** Sub-agents do not spawn their own sub-agents.
5. **Threshold breaches go to the top of STATUS.md.** CARL scans headers first.
6. **Stale data is worse than no data.** If a sub-agent can't refresh a metric, mark it STALE with the date. Don't carry forward old values as current.
7. **Sub-agents flag uncertainty.** If a finding is ambiguous or a source is questionable, the sub-agent says so. CARL decides what to do with it.
8. **Per [[feedback_subagent_prompt_discipline]]**: decision-lead, word cap, decision-usefulness, verdict-first. Don't over-template.
9. **Per [[feedback_parallel_spawn_independent_agents]]**: independent spawns in ONE message with multiple Agent calls — never sequential.
10. **Downward propagation (standing rule, 2026-07-10 — audit must-fix #5, PAT-044 root fix).** Any CARL parent-level move that supersedes a sub-domain fact (catch-up gather, workbook freeze, CRL invalidation, refuted prior) **writes down to the owning sub-agent's STATUS/dossier in the same session** — or stamps that surface `BYPASSED <date>` explicitly. Never key TEAM.md freshness on SV-receipt: freshness = the canonical surface's own state (the Jun-22 GIG bypass laundered a 66d-stale STATUS into "🟢 fresh" and let it assert falsified facts for 18 days).
