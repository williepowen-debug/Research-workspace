# DEWEY — Revival Plan of Attack

**Author:** WALTER (Will-directed, 2026-06-20)
**Status:** Phase 1 ✅ (2026-06-20 AM) + Phase 2 ✅ (2026-06-20 PM, Will-approved, all 4 tightenings). **Next: Phase 3 (first live run)** — gated on the CONTEXT.md refresh (Phase 3 hard gate below).
**Why this doc exists:** Will asked to revive DEWEY as a standing deep-research agent. The work is multi-step; this doc is the canonical phased plan so it survives context resets and we don't try to do it all in one overwhelmed pass. Each phase is a separate working session with a clean handoff.

---

## GOAL

Revive `AGENTS/DEWEY/` as the network's **standing deep-research (Tier 2) identity** — the on-demand, deep, cited research function that complements (does not duplicate) WALTER's shallow/continuous routing role. Keep DEWEY's good bones (citation discipline, mandatory counter-evidence, structured output, self-improvement loop); modernize the *engine* from its old hand-rolled scripts to the current `/deep-research` skill + FORGE tools; wire it into the existing operation (WALTER routing + the Phase 2.8 deep-research-flag loop + the future Scout).

---

## CURRENT STATE (audit, 2026-06-20)

**What exists in `AGENTS/DEWEY/`:**
- `CLAUDE.md` — full agent spec (find-verify-deliver facts; NOT an analyst; every claim cited w/ source-quality tags PRIMARY→UNSOURCED; counter-evidence MANDATORY; "say I don't know"; Cold vs Thesis modes; structured output Key Finding→Evidence→Counter-Evidence→Source Quality→References; mandatory Process Report self-improvement section). **The spec is good and largely still valid.**
- `CONTEXT.md` — Thesis-mode domain context. **STALE — frozen late-Feb 2026** ("US/Israel military action against Iran began Feb 28"; pre-dates the current 11-cluster taxonomy, WALTER/BOARD, the deep-research skill).
- `scripts/` — `fred_pull.py` + `edgar_fetch.py`. **REDUNDANT** — superseded by `FORGE/tools/market-data/` (FRED/equity) + `FORGE/tools/filing-watch/poll_edgar.py` (EDGAR) + the `/deep-research` skill's own web fetch.
- `output/` — 6 reports dated 2026-02-28 (WAL base case, Block fintech contagion, Block layoff reaction, Iran/Hormuz oil, military/economic timing, WAL Stupin/Cantor). **Proof of value — genuinely solid cited work.** Keep as archive.

**Dormant since:** ~early March 2026 (Session 4). Predates almost the entire current operation.

**Not in REGISTRY.tsv** — DEWEY is currently an off-registry ghost dir.

**The capability already runs today** via the `/deep-research` skill (Will ran it 6/19 → the S-FL packet → routed as SIG-W-20260619-008; the Phase 2.8 flag→deliverable→route loop is already validated end-to-end). So this is **reviving an identity for a capability we already use**, not building a new capability.

---

## TARGET ARCHITECTURE

Three roles, one chain (WALTER is the spine):

```
SCOUT (Tier 1, future)        WALTER (exists)                 DEWEY (Tier 2, this revival)
broad/continuous/cheap   →    triage + route; via Phase 2.8   →   deep/on-demand/expensive
scripts, no LLM               flag candidates + write prompt      /deep-research engine + cited discipline
posts raw → group             route research-output (SIG-008)  ←   output/ + handoff to WALTER
```

- **Engine swap:** DEWEY's discipline + identity ride on top of the `/deep-research` skill instead of the old scripts.
- **No second router:** DEWEY produces reports; WALTER decides what's a signal and routes. Preserves "WALTER = single entry point."
- **Phase 2.8 already half-wired:** `DEEP_RESEARCH_FLAGGED_LOG.tsv` + CHECKLIST v0.18 Phase 2.8 (flag) + v0.19 Phase 2.8b (returning-deliverable handling: one `research-output` BOARD signal + per-recipient delta wrapper + ledger close). The only change is the executor goes from "Will runs the skill" → "DEWEY runs the skill (Will-triggered/approved)."

---

## DESIGN DECISIONS — RESOLVED (Will, 2026-06-20)

1. **Trigger model — who fires DEWEY?** → **Will + WALTER-Phase-2.8-flag.** WALTER flags a candidate + writes the prompt; Will opens a DEWEY session and feeds it. Scout-surfaced leads later (Phase 4).
2. **Execution model — how does it run?** → **(A) Its own Claude Code session Will launches** — like CARL/REGINALD/SAM/RED. Boots, takes the question, runs `/deep-research` with its discipline, archives the cited report, hands to WALTER. CLAUDE.md gets a real boot + closeout. Registered **Tier-2, Claude Code, Will-launched.** (Confirmed: the skill is a session-level harness, so a WALTER-spawned sub-agent can't cleanly invoke it — own-session is the only shape that supports skill-as-engine.)
3. **Relationship to the `/deep-research` skill** → **DEWEY calls the skill** (skill = engine; DEWEY = disciplined wrapper + archive + routing handoff).
4. **Autonomy ceiling** → **on-demand only for v1**; revisit after the Scout exists.
5. **CONTEXT.md scope** → refresh from CLUSTER_TAXONOMY + REGISTRY (no re-interview).

**🆕 TWO-LEVEL ROLE (Will, 2026-06-20):** DEWEY operates on two levels, not one:
- **Level 1 — Deep research (on-demand):** Will spawns it for a specific deep-research task → runs `/deep-research` + discipline → cited report → WALTER routes.
- **Level 2 — Data-pull script home:** DEWEY's `scripts/` is the **canonical home for the data-pull tooling** ("the scripts that pull data for us"). The scripts are dumb/shared; DEWEY-the-agent runs them when spawned, AND a scheduled cron (the Scout/SENTRY layer) can run the same scripts to post digests. Housing the scripts here ≠ making collection an LLM agent — the scripts stay deterministic; DEWEY just owns the code. **Implication:** do NOT trash the old `scripts/` — modernize + position `scripts/` as the data-pull library; the Scout's collection scripts will likely live here too (reconcile in the Scout track). This means the earlier "separate SENTRY scout vs DEWEY" split likely collapses — DEWEY becomes the single research home (tooling + deep-research), and the Scout is just a cron that runs DEWEY's scripts. Confirm scope when the Scout track starts.

---

## PHASED PLAN

Each phase = one focused session. Do not chain more than one phase per pass (Will's context-overwhelm guard).

### Phase 0 — Sign-off (this pass)
- ✅ Audit complete (above).
- ✅ This plan doc written.
- **Will:** react to phasing + answer the 5 open decisions (terse is fine). No build until then.

### Phase 1 — Identity & spec modernization
- Rewrite `DEWEY/CLAUDE.md`: current role (Tier-2 deep-research executor), engine = `/deep-research` skill, kept discipline (citations/counter-evidence/process-report), integration points (WALTER + Phase 2.8), output + handoff conventions, boot/closeout if standing agent (per decision #2).
- Refresh `CONTEXT.md` to current 11-cluster thesis set + active domains (per decision #5).
- Retire old `scripts/` (move to `scripts/legacy/` or trash; point spec at FORGE tools + skill).
- Add a **DEWEY row to `REGISTRY.tsv`** (in WALTER's scope).
- **Deliverable:** DEWEY is a coherent, current, registered identity — but not yet test-run.

### Phase 2 — Integration wiring
- Wire the Phase 2.8 loop to DEWEY as executor: update CHECKLIST Phase 2.8/2.8b references ("Will runs /deep-research" → "DEWEY executes; Will triggers/approves") — small, canonical-source-first edits in WALTER's CHECKLIST.
- Define the DEWEY→WALTER handoff (output/ → WALTER consumes → routes as `research-output` per the SIG-008 pattern already codified). Confirm `DEEP_RESEARCH_FLAGGED_LOG` columns cover an executor field.
- Output archive + filename conventions (`YYYY-MM-DD_topic.md`, already established).
- **Deliverable:** the flag→execute→route loop names DEWEY end-to-end on paper.
- **✅ SHIPPED 2026-06-20 (Will-approved, all 4 tightenings):** CHECKLIST v0.19→**v0.20** (Phase 2.8 executor → DEWEY; Phase 2.8b deliverable-arrival via `inbox/DEWEY/` + `git mv`-to-`processed/` NEW→ROUTED→PROCESSED lifecycle) + WALTER CLAUDE.md **spawn-protocol step 7d** (boot-scan of `inbox/DEWEY/`) + `DEEP_RESEARCH_FLAGGED_LOG` **+`executor` column** (SIG-007 backfilled = Will) + created `AGENTS/WALTER/inbox/DEWEY/` (+ `processed/` + README) + DEWEY/CLAUDE.md handoff-lifecycle note + STATE §1 sync + version_drift ✓. Scoped commit; push deferred.

### Phase 3 — Live test & validate
- **🔴 HARD GATE (Will, 2026-06-20) — refresh `CONTEXT.md` BEFORE the first live run.** It's stale (Iran framing pre-dates the 6/20 Hormuz re-closure re-stamp in `AGENTS/WALTER/anchors/IRAN_WAR.md`); refresh from CLUSTER_TAXONOMY + REGISTRY + the IRAN_WAR anchor. Wired into `DEWEY/CLAUDE.md` BOOT step 3 as a gate. Do not run live research on a stale-domain question until this is done.
- Pick one real, pending research question (e.g. an open thesis tiebreaker — a CRE-credit June-print question, or a current candidate) and run it **end-to-end through revived DEWEY**: flag → prompt → `/deep-research` run → cited report in `output/` → handoff to WALTER → routed as `research-output`.
- Validate the way SIG-008 validated Phase 2.8. Capture the Process Report; tune the spec from what was hard.
- **Deliverable:** first live revived-DEWEY report routed; loop proven.

### Phase 4 — (optional/later) Scout integration + autonomy
- Once the Scout (SENTRY revival) exists: wire Scout-surfaced leads → WALTER flag → DEWEY.
- Consider scheduled/standing research threads if on-demand proves too reactive.
- **Deliverable:** the full Scout→WALTER→DEWEY chain live.

---

## OWNERSHIP / COMMIT NOTE

Reviving DEWEY touches files **outside WALTER's normal commit scope** (`AGENTS/DEWEY/*`). This is Will-directed cross-agent work (2026-06-20). DEWEY has no active session, so no live-tree collision risk. WALTER will commit DEWEY files under this authorization, scoped by explicit pathspec (never `git add -A`), and note it in closeout. `REGISTRY.tsv` + `CHECKLIST` edits are inside WALTER's own scope. Push stays Will-coordinated per protocol.

---

## THE SCOUT TRACK (separate build — captured 2026-06-20 so the thinking isn't lost)

The Scout = the broad/continuous/cheap feed-collection tier (vs DEWEY's deep/on-demand tier). Discussed at length the same session; **not yet built.** Capturing the decisions + diagnosis here so a future session resumes cold.

**Diagnosis of the old (dead) feeds — and why they died:**
- **SIGNALS / SENTRY** = a GitHub Action (`.github/workflows/feeds.yml`) that fetched RSS/Atom twice daily then `git add→commit→push` **straight to master**. That auto-commit-to-master was the merge-friction Will remembered. **It was deliberately DISABLED 2026-06-02 by Will/Prome** (the workflow file says so) — NOT broken. It only runs on manual `workflow_dispatch` now. → So "SIGNALS 18d stale" is by-design, not a failure to escalate.
- **news-sweep + filing-watch** = local cron (`cron_sweep.sh`) whose crontab path is `/home/moltbot/.openclaw/workspace/...` → they ran on the **OpenClaw VPS, which has been down since ~mid-May.** Not a config bug; the host is down. (news-sweep itself only writes files + sends a Telegram summary; it doesn't push — the OpenClaw agent loop committed its outputs.)
- **Correction to WALTER's standing framing:** these are NOT "3 dead crons → escalate to PROME/SENTRY to revive." They're *intentionally-off* (SENTRY) + *VPS-down* (news-sweep/filing-watch). The go-forward is the Scout rebuild below, not an escalation.

**Target Scout architecture (Will-aligned, not yet built):**
- **"Fetch → Telegram, never git."** A GitHub Action on a cron runs the (dumb, deterministic) fetch scripts and **posts a digest to the WALTER+PROME group** — it never commits to master. The only thing that ever commits is WALTER, through its normal scoped pipeline, after triaging. Kills the merge-conflict class by construction. This is the "Git = shared brain, Telegram = cockpit" model validated 6/17.
- **No second router.** Scout gathers raw candidates → posts → WALTER triages + routes. WALTER stays the single entry point.
- **Posting mechanism:** one `curl` to Telegram `sendMessage`; bot token lives in a **GitHub repo Secret** (`${{ secrets.TELEGRAM_BOT_TOKEN }}`), never in the YAML.
- **Dedicated feeds bot** (NOT WALTER's live-relay token). The old `cron_sweep.sh` already used a separate token (`8533568512:...`) — but it's sitting **in plaintext in git history**, so: rotate it (BotFather) + move to a Secret + add the bot to the group. Visual separation: digests post as a distinct identity, not as WALTER.
- **Dedup** via GitHub Actions cache, not a repo commit (no seen.json churn).
- **Cadence:** lean — once daily pre-market (~8am ET), not twice. Keep a `workflow_dispatch` manual trigger for test-fires + on-demand.
- **Feeds to revive (lean):** news-sweep (15 thesis RSS queries) + filing-watch (EDGAR). Leave SENTRY/SIGNALS dead unless it proves value. Google Alerts fold in as RSS (one mechanism, many sources).

**🆕 Likely consolidation (Will, 2026-06-20):** Will wants DEWEY to *hold the data-pull scripts* (Level-2 role above). That suggests the SENTRY-vs-DEWEY split collapses: **DEWEY becomes the single research home (tooling + deep-research); the Scout is just a cron that runs DEWEY's scripts and posts to Telegram.** Confirm this scope when the Scout track starts — it may make "SENTRY" just a workflow name, not a separate agent.

**Ownership note:** the Scout touches `.github/workflows/` + `FORGE/tools/` (shared infra, PROME/SENTRY-owned) — coordinate with PROME or get explicit Will authorization for those specific files; not WALTER's normal commit scope.

DEWEY (this plan) and the Scout can be built independently. The Scout gets its own plan/session when Will greenlights it.
