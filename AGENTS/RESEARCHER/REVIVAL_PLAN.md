# RESEARCHER — Revival Plan of Attack

**Author:** WALTER (Will-directed, 2026-06-20)
**Status:** PROPOSED — awaiting Will sign-off on phasing + open decisions before Phase 1 build.
**Why this doc exists:** Will asked to revive RESEARCHER as a standing deep-research agent. The work is multi-step; this doc is the canonical phased plan so it survives context resets and we don't try to do it all in one overwhelmed pass. Each phase is a separate working session with a clean handoff.

---

## GOAL

Revive `AGENTS/RESEARCHER/` as the network's **standing deep-research (Tier 2) identity** — the on-demand, deep, cited research function that complements (does not duplicate) WALTER's shallow/continuous routing role. Keep RESEARCHER's good bones (citation discipline, mandatory counter-evidence, structured output, self-improvement loop); modernize the *engine* from its old hand-rolled scripts to the current `/deep-research` skill + FORGE tools; wire it into the existing operation (WALTER routing + the Phase 2.8 deep-research-flag loop + the future Scout).

---

## CURRENT STATE (audit, 2026-06-20)

**What exists in `AGENTS/RESEARCHER/`:**
- `CLAUDE.md` — full agent spec (find-verify-deliver facts; NOT an analyst; every claim cited w/ source-quality tags PRIMARY→UNSOURCED; counter-evidence MANDATORY; "say I don't know"; Cold vs Thesis modes; structured output Key Finding→Evidence→Counter-Evidence→Source Quality→References; mandatory Process Report self-improvement section). **The spec is good and largely still valid.**
- `CONTEXT.md` — Thesis-mode domain context. **STALE — frozen late-Feb 2026** ("US/Israel military action against Iran began Feb 28"; pre-dates the current 11-cluster taxonomy, WALTER/BOARD, the deep-research skill).
- `scripts/` — `fred_pull.py` + `edgar_fetch.py`. **REDUNDANT** — superseded by `FORGE/tools/market-data/` (FRED/equity) + `FORGE/tools/filing-watch/poll_edgar.py` (EDGAR) + the `/deep-research` skill's own web fetch.
- `output/` — 6 reports dated 2026-02-28 (WAL base case, Block fintech contagion, Block layoff reaction, Iran/Hormuz oil, military/economic timing, WAL Stupin/Cantor). **Proof of value — genuinely solid cited work.** Keep as archive.

**Dormant since:** ~early March 2026 (Session 4). Predates almost the entire current operation.

**Not in REGISTRY.tsv** — RESEARCHER is currently an off-registry ghost dir.

**The capability already runs today** via the `/deep-research` skill (Will ran it 6/19 → the S-FL packet → routed as SIG-W-20260619-008; the Phase 2.8 flag→deliverable→route loop is already validated end-to-end). So this is **reviving an identity for a capability we already use**, not building a new capability.

---

## TARGET ARCHITECTURE

Three roles, one chain (WALTER is the spine):

```
SCOUT (Tier 1, future)        WALTER (exists)                 RESEARCHER (Tier 2, this revival)
broad/continuous/cheap   →    triage + route; via Phase 2.8   →   deep/on-demand/expensive
scripts, no LLM               flag candidates + write prompt      /deep-research engine + cited discipline
posts raw → group             route research-output (SIG-008)  ←   output/ + handoff to WALTER
```

- **Engine swap:** RESEARCHER's discipline + identity ride on top of the `/deep-research` skill instead of the old scripts.
- **No second router:** RESEARCHER produces reports; WALTER decides what's a signal and routes. Preserves "WALTER = single entry point."
- **Phase 2.8 already half-wired:** `DEEP_RESEARCH_FLAGGED_LOG.tsv` + CHECKLIST v0.18 Phase 2.8 (flag) + v0.19 Phase 2.8b (returning-deliverable handling: one `research-output` BOARD signal + per-recipient delta wrapper + ledger close). The only change is the executor goes from "Will runs the skill" → "RESEARCHER runs the skill (Will-triggered/approved)."

---

## DESIGN DECISIONS — RESOLVED (Will, 2026-06-20)

1. **Trigger model — who fires RESEARCHER?** → **Will + WALTER-Phase-2.8-flag.** WALTER flags a candidate + writes the prompt; Will opens a RESEARCHER session and feeds it. Scout-surfaced leads later (Phase 4).
2. **Execution model — how does it run?** → **(A) Its own Claude Code session Will launches** — like CARL/REGINALD/SAM/RED. Boots, takes the question, runs `/deep-research` with its discipline, archives the cited report, hands to WALTER. CLAUDE.md gets a real boot + closeout. Registered **Tier-2, Claude Code, Will-launched.** (Confirmed: the skill is a session-level harness, so a WALTER-spawned sub-agent can't cleanly invoke it — own-session is the only shape that supports skill-as-engine.)
3. **Relationship to the `/deep-research` skill** → **RESEARCHER calls the skill** (skill = engine; RESEARCHER = disciplined wrapper + archive + routing handoff).
4. **Autonomy ceiling** → **on-demand only for v1**; revisit after the Scout exists.
5. **CONTEXT.md scope** → refresh from CLUSTER_TAXONOMY + REGISTRY (no re-interview).

**🆕 TWO-LEVEL ROLE (Will, 2026-06-20):** RESEARCHER operates on two levels, not one:
- **Level 1 — Deep research (on-demand):** Will spawns it for a specific deep-research task → runs `/deep-research` + discipline → cited report → WALTER routes.
- **Level 2 — Data-pull script home:** RESEARCHER's `scripts/` is the **canonical home for the data-pull tooling** ("the scripts that pull data for us"). The scripts are dumb/shared; RESEARCHER-the-agent runs them when spawned, AND a scheduled cron (the Scout/SENTRY layer) can run the same scripts to post digests. Housing the scripts here ≠ making collection an LLM agent — the scripts stay deterministic; RESEARCHER just owns the code. **Implication:** do NOT trash the old `scripts/` — modernize + position `scripts/` as the data-pull library; the Scout's collection scripts will likely live here too (reconcile in the Scout track). This means the earlier "separate SENTRY scout vs RESEARCHER" split likely collapses — RESEARCHER becomes the single research home (tooling + deep-research), and the Scout is just a cron that runs RESEARCHER's scripts. Confirm scope when the Scout track starts.

---

## PHASED PLAN

Each phase = one focused session. Do not chain more than one phase per pass (Will's context-overwhelm guard).

### Phase 0 — Sign-off (this pass)
- ✅ Audit complete (above).
- ✅ This plan doc written.
- **Will:** react to phasing + answer the 5 open decisions (terse is fine). No build until then.

### Phase 1 — Identity & spec modernization
- Rewrite `RESEARCHER/CLAUDE.md`: current role (Tier-2 deep-research executor), engine = `/deep-research` skill, kept discipline (citations/counter-evidence/process-report), integration points (WALTER + Phase 2.8), output + handoff conventions, boot/closeout if standing agent (per decision #2).
- Refresh `CONTEXT.md` to current 11-cluster thesis set + active domains (per decision #5).
- Retire old `scripts/` (move to `scripts/legacy/` or trash; point spec at FORGE tools + skill).
- Add a **RESEARCHER row to `REGISTRY.tsv`** (in WALTER's scope).
- **Deliverable:** RESEARCHER is a coherent, current, registered identity — but not yet test-run.

### Phase 2 — Integration wiring
- Wire the Phase 2.8 loop to RESEARCHER as executor: update CHECKLIST Phase 2.8/2.8b references ("Will runs /deep-research" → "RESEARCHER executes; Will triggers/approves") — small, canonical-source-first edits in WALTER's CHECKLIST.
- Define the RESEARCHER→WALTER handoff (output/ → WALTER consumes → routes as `research-output` per the SIG-008 pattern already codified). Confirm `DEEP_RESEARCH_FLAGGED_LOG` columns cover an executor field.
- Output archive + filename conventions (`YYYY-MM-DD_topic.md`, already established).
- **Deliverable:** the flag→execute→route loop names RESEARCHER end-to-end on paper.

### Phase 3 — Live test & validate
- Pick one real, pending research question (e.g. an open thesis tiebreaker — a CRE-credit June-print question, or a current candidate) and run it **end-to-end through revived RESEARCHER**: flag → prompt → `/deep-research` run → cited report in `output/` → handoff to WALTER → routed as `research-output`.
- Validate the way SIG-008 validated Phase 2.8. Capture the Process Report; tune the spec from what was hard.
- **Deliverable:** first live revived-RESEARCHER report routed; loop proven.

### Phase 4 — (optional/later) Scout integration + autonomy
- Once the Scout (SENTRY revival) exists: wire Scout-surfaced leads → WALTER flag → RESEARCHER.
- Consider scheduled/standing research threads if on-demand proves too reactive.
- **Deliverable:** the full Scout→WALTER→RESEARCHER chain live.

---

## OWNERSHIP / COMMIT NOTE

Reviving RESEARCHER touches files **outside WALTER's normal commit scope** (`AGENTS/RESEARCHER/*`). This is Will-directed cross-agent work (2026-06-20). RESEARCHER has no active session, so no live-tree collision risk. WALTER will commit RESEARCHER files under this authorization, scoped by explicit pathspec (never `git add -A`), and note it in closeout. `REGISTRY.tsv` + `CHECKLIST` edits are inside WALTER's own scope. Push stays Will-coordinated per protocol.

---

## RELATIONSHIP TO THE SCOUT (separate track)

The Scout (consolidated feed-collection = SENTRY revived as a Telegram-posting scout, no master commits) is a **separate, parallel build** discussed the same session. RESEARCHER (deep) and Scout (broad) are the two tiers of the research function; both hand off through WALTER. They can be built independently — this plan covers RESEARCHER only. Scout has its own plan when Will greenlights it.
