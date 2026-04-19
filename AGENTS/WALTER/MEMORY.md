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

### CHANGES SINCE LAST SESSION (Apr 19 — full-day session, 5 batches)
- **Heaviest single-day in WALTER history.** AM carry-forward (3) + PM-1 image batch (3) + PM-2 image batch (4) + PM-3 image batch (5) + PM-4 image batch (3) + PM-5 image batch (5) = **23 routed, 7 killed.** Total dispatched on BOARD: 16 → 39.
- **Bear cluster matured to ~16 nodes + 3 counter-channels + MULTIPLE counter-channel candidates.** Composition:
  - Positioning pillar (**5 channels, STRONGEST**): SIG-006 GS Prime HF cover, SIG-008 DB financials gap, SIG-016 BofA largest MMF outflow ever, SIG-018 S3 $93B short positions covered MTD + GS most-shorted +13% wk + UBS weak +9% + profitless tech +14% wk, SIG-023 CPC 0.66 most bullish since 2021
  - Vol-pricing pillar (4 channels, IMPLIED-only per SIG-012): SIG-002 VIOLET SKEW divergence, SIG-003 VIOLET POSTURE 🟠, SIG-007 Altrichter OVX divergence, SIG-008 DDS rally extremity
  - Valuation pillar (2 channels): SIG-005 Buffett 232%, SIG-004b NDX 25yr parabolic
  - Breadth pillar (2 channels, mid/long-horizon-only per SIG-011): SIG-003 NDX RSI + SPX neg breadth, SIG-009 Zaccardi finviz interior drawdowns
  - Pattern (2 channels): SIG-004a Wyckoff distribution
  - Iran/oil (3 channels): SIG-006 Trump WH Sit Room w/ Bessent, SIG-010 (superseded by 014), SIG-014 Iran SoH re-closure Apr 18 verified
  - Credit pillar (**2 channels**): SIG-015 NFIB small-biz CapEx GFC-low + Sub-V +67% YoY; SIG-020 ATTOM Q1 foreclosure +26% YoY (Completed +45%)
  - **Counter-channels (3):** SIG-011 Detrick short-term breadth bullish (80% above 20-day MA), SIG-012 Sethi/Morningstar realized-vol normal (15% YTD), SIG-017 Bilello combined (VIX -43.7% = 5th biggest crash + SPX +11.9% = 13th biggest 3-wk gain since 1950, both with bullish-leaning forward returns)
  - **Counter-channel candidates (adds):** SIG-013 Barchart BRK.A -39pts vs SPY (composition caveat); SIG-019 LTM equity-flow modest on AUM-normalized (0.4% vs 7.7% bonds) = retail-YOLO-framing counter; SIG-021 MS 1990-vs-2026 oil-shock structural comparison (all 6 axes favor 2026) = oil-shock-to-recession transmission counter-frame
  - **Iran-posture (new):** SIG-022 @neetintel EAM/HFGCS+E-6B simultaneous Apr 19 19:20 UTC — 🔍 VERIFY flag, confidence 0.40 reflecting observation-vs-interpretation asymmetry
- **Verify-research spawn caught 2 misframed virals this session.** (1) BOJ ¥330B (PM-1) — actually BOJ's annual JP-ETF disposal policy from Sept 2025, not Apr 18 US-ETF outflow. (2) WhaleInsider/AK "ZERO Hormuz tankers / first in history" (PM-3) — actually ≥8 tankers (Al Jazeera/Argus); historic event is Feb 28 onset, not Apr 18. Both FALSE-MISFRAMED, killed. WhaleInsider underlying event (Iran re-closed SoH Apr 18 after brief Apr 17 partial reopening; ~95% transit collapse since Feb 28) preserved as SIG-014 IMMEDIATE → BRENT under proper attribution.
- **Iran/Hormuz state CORRECTED twice intra-session.** PM-2: bifurcation framing (Apr 17 OPEN vs Apr 18 fragile). PM-3: bifurcation collapsed (re-closure verified Apr 18; both operational + political lean re-escalate). SIG-010 INDEX row carries correction pointer to SIG-014. Use SIG-014's verified state, not SIG-010's framing.
- **Cluster steelman maturation pattern.** Bear thesis was assembled in earlier sessions. Counter-evidence channels arriving in PM-3/PM-4 are the SECOND-ORDER product of routing extreme positioning data — when something is 11+ standard deviations, counter-narratives form quickly. RED now has actual material (3 counter-channels) to argue with, not just "lose with grace."
- **Will requested mid-closeout interpretation in PM-4 (msg 713).** Sent synthesis (msg 714): two stories TRUE simultaneously, different time horizons. Asymmetric-into-Tuesday trade MORE attractive (more positioning to potentially unwind), but post-Tuesday view should NOT assume regime change. Frame as 2-day catalyst convexity, NOT regime call.
- **Cross-author combine precedent established as standing operating method.** SIG-010 (Flightradar + Hague), SIG-017 (cross-batch Bilello). Per FORMAT_SPEC same-author/same-theme rule, theme-identity is now operative test, not author-identity.
- **PM-5 batch surfaced 3 process questions Will flagged.** (1) Confidence scoring has no rubric for observation-vs-interpretation asymmetry — EAM image got 0.40 on judgment call. (2) signal_type enum may not cover "thesis-frame" for institutional analytical content (used on MS oil-shock slide). (3) Analytical-content vs data-point distinction is weak in current FILTER_SPEC. All three could benefit from FORMAT_SPEC / FILTER_SPEC v-next treatment in the review trigger.

### NEXT SESSION
1. **Apr 21 (Tuesday — 2 days)**: WAL + ZION earnings + Iran ceasefire expiry. **Bifurcation framing is dead** — operational (Apr 18 SoH re-closure verified) AND political (Apr 18 Sit Room w/ Bessent) BOTH lean re-escalate. Plus: cluster's positioning pillar now 4 channels, RED has 3 counter-channels to steelman. Frame the trade as 2-day catalyst convexity, NOT a regime call.
2. **Cluster classification by NEXUS overdue.** ~15 bear nodes / 3 counter-channels / 1 12th-node candidate. Surface proactively. RED has actual material to argue with; should run the cluster through formal adversarial review pre-Tuesday.
3. **SIG-010 correction** — INDEX has correction pointer to SIG-014. Subsequent oil/Iran signals use SIG-014 verified state.
4. **OZK earnings Apr 16 backfill** — still pending if Will wants. REGINALD likely processed.
5. **Oil 3-pt cluster** (Kpler + Corio + Baker Hughes) still pending BRENT/HAWK reclassification. With Iran SoH re-closed, the physical-tightness thesis aligns rather than competes.
6. **RED refresh STILL OVERDUE** — HY OAS <300 falsification at Day 9+. Buffett 232% + cluster + Iran re-escalation + 3 counter-channels + 4 positioning channels = richest adversarial setup yet. Will owns spawn.
7. **ZHAO awaiting spawn** for China material — now 17d+ stale.
8. **FORGE/STATUS.md** still Mar 25 (~25d).
9. **COP refresh** still deprioritized; gap continues to grow.
10. **Filter v1→v2 review** — at 34 dispatches vs 10-trigger. Overdue by 24 dispatches.
11. **Cumulative session pipeline: 23 routed / 7 killed across 5 batches.** Heaviest single-day signal-routing session in WALTER history. Pattern: counter-evidence channels arriving in PM-3/PM-4/PM-5 represent maturing of the cluster — initial bear thesis was assembled in earlier sessions, the steelman is now arriving as a deliberate result of routing extreme positioning data. PM-5 added 5 more signals: cluster's positioning pillar = 5 channels, consumer-credit pillar = 2 channels, counter-channels staying at 3 validated + multiple candidates.
12. **PM-5 process-question surfacing:** Will asked protocol walkthrough mid-session. Written answer identified 3 spec-level gaps (confidence asymmetry, signal_type enum, analytical-vs-data distinction). Candidates for FORMAT_SPEC / FILTER_SPEC v-next review when triggered.

### OPEN DESIGN DECISIONS (need Will)
- **Other-agent boot-sequence rollout** — still pending. Until rolled, agents won't pull from BOARD; only see signals if Will spawns/directs.
- COP refresh cadence — currently OFF (deprioritized). When to turn back on?
- Filter model v1→v2 review trigger: 10 dispatches or 30 days — **at 34 dispatches (24 past threshold)**, target was ~May 11. Review kill_log/route_log, adjust gate thresholds. Session-by-session dispatch growth is accelerating — review more urgent than the date trigger suggests.
