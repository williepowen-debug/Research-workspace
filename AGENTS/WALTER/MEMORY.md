# WALTER MEMORY

*Curated cross-session memory. Read at boot, write before finishing. Cap at 100 lines — promote to design docs/CLAUDE.md or delete, never just accumulate.*

*Distinct from STATUS.md (operational state) and LAST_COMPLETION.md (latest session's deliverables). This file holds durable learnings that shape how WALTER works, not what WALTER did.*

---

## Feedback

- [2026-04-07] Will directed iterative COP architecture ("treat this as a living process, iterate as we learn") rather than comprehensive upfront design. Apply: ship Layer 1 before designing Layer 2/3 in detail.
- [2026-04-07] Will raised achievability concern on elaborate workflows — scoped realistic cycle: boot → read STATUS files → update COP → write signals → ping Telegram if FLASH → done. Apply: when proposing new infrastructure, budget against the real session cadence, not the theoretical capacity.
- [2026-04-10] Will challenged duplication on SIG-001/SIG-002 draft pair. "One file per action recipient" in FORMAT_SPEC means dispatch mechanics, not content splitting. Apply: never split the same underlying data into multiple signals because different agents care about different angles — frame it once, route to multiple recipients via to/info fields.
- [2026-04-11] When uncertain about canonical source for a spec change, ask before editing dependents. Canonical-source-first rule added to CLAUDE.md as Rule 8 + canonical-source lookup table. Apply: before modifying any design doc, check the lookup table to find the owning doc, edit there first, then propagate.
- [2026-04-14] When asked "is the architecture built correctly?", give honest POV not reflexive agreement. Will wants the real answer, not the comfortable one. Apply: when Will frames a question as "I'm just asking," he still wants a genuine recommendation.
- [2026-04-14] **Delivery policy ACTIVATED (BOARD-only):** every signal → BOARD archive always. FLASH = BOARD + Telegram alert to Will only (no inbox push at all). IMMEDIATE/PRIORITY/ROUTINE = BOARD-only. Will accepted that other agents will miss signals until their boot-sequence is updated. Apply: do NOT push to inboxes for non-FLASH; do NOT push to inbox even for FLASH (just Telegram-alert Will). Will spawns the relevant agent if action needed.
- [2026-04-14] **Image-intake batch workflow:** Will sends image batches via Telegram, WALTER processes and replies with batch summary (one line per signal: ID → domain → precedence → recipient → kill reason). Auto-spawn verify-research sub-agents when claims need source-checking — no permission per-spawn. Tag signals with 🔍 VERIFY criteria: secondhand source citing primary = verify; named senator on video / Bloomberg-bylined = no verify. Flag friction in real time, not at closeout.
- [2026-04-14] **Don't kill on lede alone.** When Will offers full body, read it before classifying. Lede-only kill missed 3 hard data points in Seeking Alpha KRE piece (KRE-XLF YTD gap, FLG #1 holding with Fitch upgrade, $936B CRE maturity). Reversed kill → filed as PRIORITY counter-evidence. Apply: distinguish weak author synthesis from named-aggregator stats (Morningstar, Redfin, BLS). A low-credibility author can still surface a real citable stat.
- [2026-04-14] **Domain vocabulary gaps surface from real signals.** When 2+ signals in one session don't fit the canonical 13 codes, that's a vocab gap signal. Resolution: add to FORMAT_SPEC FIRST per canonical-source rule, then propagate to ROUTING_TABLE. Done Apr 14 for ASIA_CONTAGION + UST_FOREIGN.
- [2026-04-14] **Honest framing over thesis-defense.** When Will asks "is X positive for our position?" give the real read — mixed/negative if that's the truth, with the strongest counter-data named. Don't soften. KRE-XLF gap widening reframed our thesis as "may be early, not wrong" — that's the rigorous answer.
- [2026-04-19] **Check target-agent KB before writing "missed context" findings.** Verify-research sub-agents often surface domain knowledge the target agent already holds in depth. SIG-030 Qatar LNG verify taught WALTER about Mar 2 Iran drone strikes on Ras Laffan/Mesaieed, QatarEnergy force majeure, IEA 400Mb coordinated release — all of which BRENT already tracks (STATUS.md L112 "PERMANENT FM 13M t/yr removed", archive/DECK_EVIDENCE.md, recon/STAGE2_FINDINGS_2026-03-15.md). Apply: before filing a "network is 7 weeks behind on X" finding or writing backfill signals, grep the target agent's own files first. WALTER doesn't need to hold BRENT's domain depth; target-agent KB >> WALTER synthesis on specialist domains. Don't conflate "WALTER didn't know this" with "the network didn't know this." Verify-research still valuable for: (a) confirming extraordinary claims, (b) surfacing framing errors (SIG-029 "first NATO state-response" was wrong — France already activated via IEA-coordinated draw).

## Findings

- [2026-04-11] `/COP.md` existed on disk since Apr 7 (commit 62eb644a) while NEXT_SESSION.md claimed it didn't. **Trust disk over memory.** Run `ls` on the file before believing a handoff doc that says something doesn't exist.
- [2026-04-11] Stale-agent flagging in the registry is the single highest-leverage boot output. Agents with Status/Updated/Focus columns >5 days old should be surfaced explicitly, not buried in the STATUS table — drives RED/HAWK/NEXUS refresh cycles.
- [2026-04-11] SAM pioneered `git pull --rebase --autostash` for dirty-tree cases. Autostash captures tracked changes only; leaves untracked files (other agents' new work) untouched. Safer than manual `git stash push --`.
- [2026-04-13] Islamabad talks outcome was a multi-agent delta (SAM/HAWK/BRENT/LIQUID/HENRY all had to reprice). A single geopolitical event can invalidate multiple COP domains simultaneously — flag convergent changes explicitly in the refresh.
- [2026-04-13] FORGE/STATUS.md staleness (now 19 days) has operational cost: every COP requires an Exposure caveat, and any trade approval flows through stale position data. Escalating to Will is overdue after Prome flag went unanswered.
- [2026-04-14] `outbox/` doing double duty as drafts + archive is an architectural bug at scale. Fixed Apr 14 — drafts in `outbox/`, dispatched signals in `signals/` as append-only archive.
- [2026-04-14] **BOARD relocation done.** Moved `AGENTS/WALTER/signals/` → `/BOARD/` at repo root via `git mv` (preserves history). Matches `/COP.md` precedent — shared assets at root, WALTER still owns writes. References updated in: WALTER/CLAUDE.md (boot + key files + git stage), COP.md footer, design/COP_TEMPLATE.md footer, design/SIGNAL_PROCESSING_CHECKLIST.md (replace_all). NEXT_SESSION.md not updated (overwritten each session).
- [2026-04-15] **Iran state stale within 24h.** COP framing of "blockade announced, ceasefire dead" was correct Apr 13 but stale by Apr 14: blockade is SELECTIVE (Iranian-port-only per CENTCOM), 3 sanctioned tankers transited Hormuz, Trump publicly dangled talks resumption (Pakistan/Geneva, Vance/Araghchi), Brent -4% on talks-hope to $94-100. **COP staleness has positioning cost** — SIG-006 framing ("HFs covered into dead ceasefire") was correct at write but partially undermined within hours. Apply: if processing oil/Hormuz/Iran signals, spot-check state before anchoring; ceasefire expiry is **Apr 21 not Apr 22** (our COP was off by 1 day).
- [2026-04-15] **KRE-XLF relative analysis: regional outperformance is mechanical, not thesis-killing.** XLF underperformance YTD is driven by payment networks (V/MA), IB/brokers (GS/MS), asset managers (BX/KKR — direct PC contagion), Berkshire concentration. KRE has zero exposure to any. Our short-KRE thesis is OZK/WAL/ZION catalyst-week, not YTD drift. Stress is real but in a different part of financials than our positioning. Don't confuse "my thesis isn't showing in YTD" with "my thesis is wrong" — they're different questions.

## References

- **Root `CLAUDE.md`** — git protocol (commit/push steps), agent lifecycle rules, cost model, hierarchy of 🟢/🟡/🟠/🔴 status keys.
- **`AGENTS/WALTER/CLAUDE.md`** — spawn protocol, canonical-source lookup table, the 8 RULES, closeout checklist including 11a-11f git steps.
- **`AGENTS/WALTER/design/`** — all spec docs. Change FORMAT_SPEC first for signal-schema changes, ROUTING_TABLE for routing, FILTER_SPEC for filter, CHECKLIST for process.
- **`AGENTS/WALTER/research/distilled/`** — the 10 distilled principles (ESI triage, military messaging, ATC, pub/sub, IC dissemination, emergency dispatch, scientific alerts, open output systems, newsroom editorial, trading desk). Source material for all architectural decisions.
- **`/COP.md`** — live at repo root. Refreshed each WALTER session. Template at `design/COP_TEMPLATE.md`.
- **Market data:** `.venv/bin/python3 FORGE/tools/market-data/dashboard.py` (needs venv, not system python).

## Session Notes

### CHANGES SINCE LAST SESSION (Apr 19 late — short handoff session)
- Brief continuation of Apr 19 PM-8 close. Boot clean; no pull needed (CARL has an uncommitted inbox-move in their dir — left alone per protocol).
- **Answered Will's two routing-architecture questions** with exact paths:
  1. **Where agents pull new messages:** `/BOARD/INDEX.md` at repo root. Scan the table for rows where your name is in `Action → Info` column; read the linked signal file from `/BOARD/`. Do not rely on inbox/ — current policy is FLASH = BOARD + Telegram-to-Will only (no inbox push).
  2. **Where each agent declares what it wants:** `AGENTS/<NAME>/SIGNAL_INTAKE.md`. Template at `AGENTS/WALTER/design/SIGNAL_INTAKE_TEMPLATE.md`.
- **CARL produced SIGNAL_INTAKE.md today (Apr 19 22:21 UTC).** Roster now 4/14 Tier 1 agents: SAM, BRENT, VIOLET, CARL. CARL's is the richest reference yet (8.4KB; Active Thresholds with specific levels — gas $4.50, Fannie MF DQ 0.80%, CC 90+ 13.74%, claims 4-wk MA 275K, Brent <$80 sustained; 3-tier keyword confidence; explicit NOT-TO-SEND list; earnings calendar pre-staged 🔴). **Recommend CARL as primary reference for next rollouts, not SAM/BRENT.**
- **Retrospective check:** every Apr 19 signal routed to CARL (SIG-015 NFIB, SIG-020 ATTOM, SIG-007 PPI) correctly matches CARL's new subscription spec — zero miss-routes on Apr 19 batch.
- **Drafted two tailored prompts** for HENRY + RED. Front-loaded with domain-specific hints from each agent's STATUS.md (HENRY: Active Thresholds, delegation discipline re VIOLET/LIQUID, positioning pillar; RED: adversarial-inverted intake with falsification rules AS thresholds, counter-evidence primary, bull-case steelman feeder). **Prompts currently in conversation transcript only — not yet saved to disk.**
- **Two-lever rollout framing crystallized for Will:** (a) `SIGNAL_INTAKE.md` per agent = subscription spec; (b) `CLAUDE.md` boot-step addition per agent = pull step. **Neither lever is complete network-wide.** Without both, signals remain invisible to the agent network regardless of BOARD dispatch volume.
- **No BOARD dispatches this session. No kills. Spec changes: none.** Total BOARD unchanged at 46.

### NEXT SESSION
1. **Apr 21 (Tuesday, 2 days):** WAL + ZION earnings + Iran ceasefire expiry into 8-channel Iran cluster. Pre-position checklist outstanding. Frame as 2-day catalyst convexity, NOT regime call (per PM-4 synthesis).
2. **HENRY + RED SIGNAL_INTAKE.md** — if Will ran the drafted prompts, read their output at boot and cross-reference against recent BOARD routings for miss-match. If not yet run, prompts are in prior conversation transcript.
3. **NEXUS cluster classification MASSIVELY overdue** — 19 bear nodes + 3 validated counter-channels (Detrick, Sethi, Bilello) + 5+ candidates (BRK, LTM flows, MS oil-shock frame, GS macro L/S, @infraa_) + 8-channel Iran day-cluster with verified Qatar LNG mechanism.
4. **RED refresh STILL OVERDUE** — HY OAS <300 Day 9+. Richest adversarial material yet.
5. **ZHAO spawn** pending — China material 17d+ stale.
6. **FORGE/STATUS.md** ~25d stale.
7. **Filter v1→v2 review** at 46 dispatches, 36 past trigger. Urgent. PM-5 surfaced 3 spec-level gaps (confidence asymmetry rubric, signal_type "thesis-frame" coverage, analytical-vs-data distinction).
8. **SIGNAL_INTAKE rollout priorities after HENRY/RED:** REGINALD (BANK_CRE, heavy BOARD traffic), LIQUID (funding), BROCK (PC), then HAWK/NEXUS and Tier 2.
9. **Mon 2026-04-20 EU oil open:** watch Germany (EBV) / France (further SAGESS) / Italy (OCSIT) for Dutch LCP-O Phase 1 follow-through (SIG-029).
10. **OZK Apr 16 earnings backfill** still pending if Will wants (REGINALD likely processed).
11. **COP refresh** still OFF. Resume trigger?
12. **Iran day-cluster reference state: 8 channels** (SoH re-closure + rejected talks + EAM + carrier build-up + Navy intercept + Iran attacks on ships + Netherlands LCP-O + Qatar LNG >90% verified crash via Mar 2 drone strikes).

### OPEN DESIGN DECISIONS (need Will)
- **Agent CLAUDE.md boot-step rollout** — SIGNAL_INTAKE coverage is useless without corresponding "scan /BOARD/INDEX.md" step in each agent's boot sequence. Rollout still not begun across any Tier 1.
- COP refresh cadence — currently OFF (deprioritized). Resume trigger?
- Filter v1→v2 review trigger: 10 dispatches or 30 days — **at 46 dispatches (36 past threshold)**, date target ~May 11. Dispatch target long passed; session-by-session growth is accelerating.
