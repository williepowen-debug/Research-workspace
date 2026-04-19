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

### CHANGES SINCE LAST SESSION (Apr 16 → Apr 19)
- **3-day dark interval, no WALTER session Apr 17-18.** Apr 18 saw Prome run a refactor + revert + cleanup cycle on root files (4 commits): tried PROME/identity/+state/ subdirs, OpenClaw injection broke, reverted to root. Net: HEARTBEAT/MEMORY/SOUL/USER/IDENTITY back at root unchanged; IRA/, agent-configs/, transcripts/ moved to archive/; data/ deleted; trade/ARES → AGENTS/BROCK/research/ARES/. Working tree was clean, fast-forward pull, no WALTER conflicts.
- **3 inbox signals processed (all 4d-stale from Apr 15):**
  - **SIG-W-20260419-001** (PRIORITY → REGINALD action; BROCK + RED info): OTTO Tricolor exposure-map expansion. MTB confirmed 5th named bank (American Banker) — was "watch tier" Feb 16. Tricolor ABS notes <10¢ on dollar = 2nd transmission channel beyond warehouse losses (investment-book marks). Timeline correction: vehicle-sale deadline is Apr 30 (not Mar 31) — Q2 prints carry revisions, not Q1. Reframes the OZK Apr 16 / WAL Apr 21 catalyst reads slightly: any Tricolor-ABS holders push real fingerprint to July.
  - **SIG-W-20260419-002** (PRIORITY → HENRY; RED, LIQUID, VIOLET info): VIOLET Apr 15 VIX-family refresh. VIX 18.08↓, VVIX 98.77↓ but SKEW 149.94↑ approaching 150. Three observations (SKEW divergence, term contango, credit-vol co-compression). #3 confirms RED HY OAS <300 falsification day-count.
  - **SIG-W-20260419-003** (IMMEDIATE → HENRY; RED, LIQUID, PROME, NEXUS info): VIOLET POSTURE 🟡→🟠 ELEVATED. 19yr backtest: SKEW-VIX-VVIX divergence pattern is 1% base rate, 15/16 (94%) → VIX +15% in 60d; revised P(new VIX event 60d) 30%→66%. Cross-link to BOARD signals: -20260416-003 (NDX RSI + SPX neg-breadth) + -20260414-006 (HF short cover) + -20260414-008 (DB financials gap) = **4-point positioning-wrong-footed cluster into Apr 21 / Apr 28 catalyst stack.**
- **VIOLET registry locked:** Tier 1 / CC / ORANGE / VIX-family + SKEW/VVIX domain. Confirmed by Will Apr 19.
- **Apr 16 batch-summary Telegram reply SKIPPED** per Will (3 days stale, just historical).
- **Inbox cleared.** All 3 originals trashed via gio after BOARD archive.

### NEXT SESSION
1. **OZK earnings Apr 16** — 3-day-old result, never intook by WALTER. If REGINALD already processed, no action; if Will wants WALTER to capture the result + market reaction as a backfill signal, surface and route.
2. **Apr 21 (Tuesday — 2 days)**: WAL + ZION earnings + Iran ceasefire expiry. Big day. Consider pre-position checklist Mon evening or Tue AM.
3. **Iran state — re-verify before anchoring.** Last verified Apr 15: blockade selective, talks rumored-resuming, Brent $94-100. State moves cycles in days. Spot-check before any new oil signal.
4. **Convergence: 4-pt positioning-wrong-footed cluster** (HF short cover + DB financials + equity internals + VIOLET SKEW divergence) is a real convergence-flag candidate. NEXUS got info copy; consider proactive ping if NEXUS hasn't recognized.
5. **Convergence: oil physical-tightness 3-pt cluster** (Kpler destocking + Corio fire + Baker Hughes rigs flat) still pending BRENT/HAWK reclassification — was flagged Apr 16, no follow-up Apr 17-18 due to dark interval.
6. **RED refresh STILL OVERDUE** — HY OAS <300 falsification at Day 9+. Will owns spawn. With VIOLET now formalizing a vol-side adversarial frame, RED + VIOLET could pair productively.
7. **ZHAO awaiting spawn** for SIG-W-20260414-010/-011 China material — now 17d+ stale.
8. **FORGE/STATUS.md** still Mar 25 (~25d). Prome flag from Apr 11 unanswered. Every COP refresh requires Exposure caveat as cost.
9. **COP refresh** deprioritized; COP is now ~6 days stale and Iran/blockade/ceasefire facts have moved 2-3 cycles. Reconsider before Apr 21.
10. **Filter v1→v2 review** — at 19 dispatches vs 10-trigger. Overdue by 9 dispatches.
11. **Telegram MCP** held connection through this session (4-message conversation). State stable Apr 19 AM.

### OPEN DESIGN DECISIONS (need Will)
- **Other-agent boot-sequence rollout** — still pending. Until rolled, agents won't pull from BOARD; only see signals if Will spawns/directs.
- COP refresh cadence — currently OFF (deprioritized). When to turn back on?
- Filter model v1→v2 review trigger: 10 dispatches or 30 days — at 19 dispatches (THRESHOLD HIT 9 ago), target was ~May 11. Review kill_log/route_log, adjust gate thresholds.
