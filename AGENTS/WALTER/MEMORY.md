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

### CHANGES SINCE LAST SESSION (Apr 14 → Apr 15)
- **Role redefinition (Will Apr 14):** WALTER's primary job is now image/screenshot signal intake from Will via Telegram. WALTER + Prome are the only Telegram agents; Prome's Kimi LLM can't read images, so WALTER owns visual intake. COP refresh deprioritized until further direction.
- **`/BOARD/` created at repo root** via `git mv AGENTS/WALTER/signals BOARD`. Network-shared archive, WALTER still owns writes. Path references updated in WALTER CLAUDE.md, COP.md footer, design/COP_TEMPLATE.md, design/SIGNAL_PROCESSING_CHECKLIST.md.
- **Delivery policy flipped to BOARD-only** for IMMEDIATE/PRIORITY/ROUTINE. FLASH = BOARD + Telegram-alert-to-Will only (no inbox push). Other-agent boot-sequence rollout NOT yet greenlit by Will.
- **FORMAT_SPEC v0.3→v0.4 + ROUTING_TABLE v0.3→v0.4:** added ASIA_CONTAGION + UST_FOREIGN canonical domain codes (ZHAO primary). Closes vocab gap surfaced by today's FT China signals.
- **WALTER/CLAUDE.md** boot sequence + git-staging steps updated for BOARD path.
- **13 signals dispatched today** (SIG-W-20260414-001 through -012). 3 kills logged. 3 verify-research sub-agent spawns (SEC PDT, IMF GFSR, March PPI; Iran state delta; FT China verify).
- **Telegram MCP disconnected ~13:00 UTC 2026-04-15** mid-session. Final exchanges with Will via direct in-session text. Closeout-prep prompted by Will.

### NEXT SESSION
1. **Boot from new files first.** STATUS.md is v0.6, MEMORY.md updated, LAST_COMPLETION.md fresh. CLAUDE.md boot now reads `/BOARD/INDEX.md` (not `signals/INDEX.md`). BOARD lives at repo root.
2. **Check Telegram MCP status** — was disconnected at end of last session. If reconnected, image-intake workflow resumes. If not, in-session text only.
3. **Live KRE/XLF check at open** — yesterday: KRE +6.50% YTD vs XLF -5.68% (gap widened from Mar 28). OZK earnings TODAY (Apr 16). If catalyst week confirms thesis, gap should start closing.
4. **Iran state delta** — last verified state: blockade selective (Iranian-port only), talks rumored-resuming (Trump floated Pakistan/Geneva, Vance/Araghchi as negotiators, nothing scheduled), Brent ~$94-100 (-4% on talks-hope). Ceasefire expiry **Apr 21 not Apr 22** — our COP was off by one day.
5. **ZHAO awaiting spawn** for SIG-010/-011 China material. ZHAO STATUS 13d stale.
6. **RED refresh STILL OVERDUE** — HY OAS <300 falsification now at Day 5+. Will is owner of RED spawn.
7. **FORGE/STATUS.md still stale** at Mar 25 (~21d). Prome flag from Apr 11 unanswered.
8. **COP refresh** is deprioritized but the COP is now stale — Iran state moved, ceasefire expiry date wrong, oil price moved. Reconsider when Will lifts the deprioritize.
9. **Domain vocabulary discipline:** FORMAT_SPEC + ROUTING_TABLE are both v0.4 with ASIA_CONTAGION + UST_FOREIGN. Use these codes for any future China/foreign-UST routing.

### OPEN DESIGN DECISIONS (need Will)
- **Other-agent boot-sequence rollout** — pending. Until rolled, agents won't pull from BOARD; they'll only see signals if Will explicitly directs them or spawns them.
- COP refresh cadence — currently OFF (deprioritized). When to turn back on?
- Filter model v1→v2 review trigger: 10 dispatches or 30 days — currently at 13 dispatches (THRESHOLD HIT), target was ~May 11. Review kill_log/route_log for false positives/negatives, adjust gate thresholds. Was supposed to happen around 10 dispatches; we're now at 13.
