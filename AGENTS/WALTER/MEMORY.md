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

### CHANGES SINCE LAST SESSION (Apr 19 PM-2 → Apr 19 PM-3)
- **Third image-intake batch this session.** Will sent 6 Telegram screenshots at 20:49 UTC. Triage: 5 routed, 2 killed, 1 verify-research spawn caught a viral misframing.
- **5 BOARD signals dispatched:**
  - **SIG-W-20260419-011** (PRIORITY → RED counter; HENRY, NEXUS info): Ryan Detrick CMT — SPX above-20-day-MA over 80%; late-March positive breadth divergence preceded current rally. **First counter-evidence channel against the cluster's breadth-weak pillar** — different time horizon (short-term momentum strong vs cluster's mid/long-term breadth weak). All can be true; cluster refines.
  - **SIG-W-20260419-012** (PRIORITY → RED counter; HENRY, LIQUID, NEXUS info): Neil Sethi/Morningstar — US stock vol 2026 YTD through Apr 10 = 15% = long-run average. **Second counter-evidence channel** — realized vol normal. Refines cluster's vol thesis to source from IMPLIED-vol surface anomalies (SKEW, OVX, VVIX) only, not realized-vol elevation.
  - **SIG-W-20260419-013** (PRIORITY → HENRY; CARL, RED, NEXUS info): Barchart — BRK.A trailing SPY by ~-39pts since Buffett retirement. Quality/defensive proxy NOT participating in rally; rally is beta/momentum-led. 12th-node candidate w/ composition caveat (BRK has zero AI-mega-cap exposure).
  - **SIG-W-20260419-014** (IMMEDIATE → BRENT; HAWK, SAM, LIQUID, RED, PROME info): Iran re-closed Strait of Hormuz Apr 18 after brief Apr 17 partial reopening. Transit volumes ~95% below normal since Feb 28 onset. **Built atop killed @WhaleInsider/@AKpercentage "ZERO tankers / first complete shutdown in history" framing** — verify-research sub-agent confirmed FALSE on both claims (Al Jazeera at least 8 tankers; Argus 2 crude + 2 product confirmed; historic event is Feb 28 onset, not Apr 18). Verified underlying event preserved under proper attribution. SIG-010 framing requires correction (Apr 17 openness was a brief reopening, not running state).
  - **SIG-W-20260419-015** (PRIORITY → CARL; BROCK, RED info): NFIB Small Business Optimism — CapEx-plans index at GFC-area low + Sub-V (small-business) bankruptcies +67% YoY. Forward indicator of NPL formation in Q2/Q3 — relevant to WAL/ZION (Apr 21) and OZK (Apr 24) earnings.
- **2 kills logged:**
  - **Bare SPX chart (image #1)** — within-batch dup of Detrick (image #2 carried full attribution + commentary).
  - **WhaleInsider/AK Hormuz framing (image #5)** — verify-research sub-agent KILLED on credibility (verifiably wrong on 2 specific claims). Underlying event preserved as SIG-014.
- **Cluster character refined (not broken).** 11-pt cluster gained 2 counter-evidence channels (Detrick + Sethi). Bear thesis must now source vol from IMPLIED surface only and breadth from mid/long-horizon only. Asymmetric-into-catalyst still works but with crisper framing. RED has steelman material to actually push back on cluster pillars.
- **Iran re-escalation Apr 21 = operational + political simultaneously.** SIG-010's "operational openness vs political fragility" bifurcation (PM-2 framing) is now obsolete — both legs lean re-escalate (operational re-closure Apr 18, political Sit Room Apr 18, ceasefire expires Apr 21). Bifurcation collapsed to single-direction risk.
- **Verify-research caught a viral misframing.** WhaleInsider's "ZERO / first in history" claim was being shared widely on X. Sub-agent's multi-source check (Al Jazeera, Argus, CNN, Bloomberg, USNI, Wikipedia) caught both the false count and the false historical framing. ROI on auto-spawn pattern reaffirmed twice this session (Buffett route + WhaleInsider kill).

### CHANGES SINCE PREVIOUS (Apr 19 PM → Apr 19 PM-2)
- **Second image-intake batch.** Will sent 5 Telegram screenshots at 18:15 UTC. Triage: 4 routed, 0 killed, 1 combined (cross-author per same-theme rule — first WALTER use of cross-author combine).
- **4 BOARD signals dispatched:**
  - **SIG-W-20260419-007** (PRIORITY → HENRY; BRENT, RED, LIQUID, NEXUS info): Kurt Altrichter CFP/CRPS Apr 16 — six-panel CBOE vol indices. VIX/VXD/VXN/RVX crushed, OVX still in crisis zone, GVZ mixed. "Non-confirmation" framing — equity vol pricing deal, oil vol not. 9th node in cluster.
  - **SIG-W-20260419-008** (PRIORITY → HENRY; RED, LIQUID, NEXUS info): Data Driven Stocks Apr 17 — author-asserted "biggest 13-day SPX rally of the century, 0.63% probability / 1-in-160." Internal text-vs-chart inconsistency (12.20% on chart panel vs 0.63% in text). Routed with strong methodology caveat as cluster-augmentation channel only. 10th node.
  - **SIG-W-20260419-009** (PRIORITY → HENRY; RED, LIQUID, NEXUS info): Mike Zaccardi CFA/CMT Apr 17 — Finviz S&P 500 treemap heatmap. Index records, interior mostly red. MSFT -24%, NFLX -27%, LLY/JNJ/TSLA -18-19%, BRK-B -12%. Visual augmentation of SIG-W-20260416-003. 11th node.
  - **SIG-W-20260419-010** (PRIORITY → BRENT; HAWK, SAM, RED, PROME info): Combined Flightradar24 dense Doha/Gulf overflight + OSINT Technical/Peter Hague Celestyal Discovery cruise ship Hormuz transit (different authors, same theme — **first cross-author combine in WALTER history**; precedent in -003 already). Confirms SELECTIVE-blockade reality.
- **Iran state bifurcation crystallized:** operational openness Apr 17 (cruise ship + dense aviation) vs political fragility Apr 18 (Trump WH Sit Room + Bessent). Both can be true into Apr 21 ceasefire expiry.
- **Cross-author combine precedent set.** SIG-W-20260416-003 was first (Bloomberg + ZeroHedge); SIG-W-20260419-010 is second (Flightradar + OSINT Technical/Peter Hague). Same-theme criterion is now the operative test, not author-identity.

### CHANGES SINCE PREVIOUS (Apr 19 AM → Apr 19 PM)
- **Image-intake batch session.** Will sent 6 Telegram screenshots at 17:41 UTC. Triage: 3 routed, 2 killed, 1 combined into routed.
- **3 BOARD signals dispatched:**
  - **SIG-W-20260419-004** (PRIORITY → HENRY; RED, LIQUID, NEXUS info): @FinanceLancelot — combined 2 charts per FORMAT_SPEC same-author/same-theme rule: SPX Wyckoff Distribution ("Upthrust After Distribution / We are here") + NDX 25-yr log-scale parabolic with dot-com analog. Pattern speculation alone is weak — counts as channels 7+8 in valuation/positioning convergence cluster.
  - **SIG-W-20260419-005** (PRIORITY → HENRY; RED, LIQUID, NEXUS info): Buffett Indicator (Wilshire 5000 / U.S. GDP) at 232.6% — VERIFIED via parallel research sub-agent against Fortune Apr 19 + 5 corroborators (Invezz, Advisor Perspectives, Current Market Valuation, Longtermtrends, Motley Fool, GuruFocus 223.5% on GNP basis). Surpasses dot-com (~190%) and Q4 2021 (~210-215%). Methodology caveat: 232.6% is high end of variants — denominator (GDP vs GNP) gap, not data integrity gap.
  - **SIG-W-20260419-006** (IMMEDIATE → BRENT; HAWK, SAM, LIQUID, PROME, RED info): @BarakRavid (Axios) — Trump WH Situation Room Sat Apr 18 on Iran, **Treasury Secretary Bessent attending** (atypical Treasury at NatSec Sit Room signals financial-stability/sanctions angle). Sit Room ~24h before intake. Iran ceasefire expires **Apr 21 Tuesday** = same catalyst day as WAL/ZION earnings.
- **2 kills logged:**
  - **BOJ ¥330B (image #4)** — verify-research sub-agent confirmed MISFRAMED. ¥330B is BOJ's annual book-value disposal of JAPANESE ETFs (TOPIX/Nikkei/JPX-400/J-REITs), policy announced Sept 19 2025 — not Apr 18 2026 U.S. ETF outflow event. Structural unwind ("100+ years to fully unwind"), not capital-flow event. @CryptoNobler has prior pattern of inflated BOJ headlines.
  - **Ravid duplicate (image #6)** — within-batch dup of image #5.
- **8-point valuation/positioning convergence cluster crystallized on BOARD:** (1) HF short cover, (2) DB financials gap, (3) NDX RSI + SPX neg-breadth, (4) VIOLET VIX-family SKEW divergence, (5) VIOLET POSTURE 🟠 ELEVATED, (6) Buffett 232%, (7) Wyckoff distribution, (8) NDX 25-yr parabolic. Convergence-flag candidate awaiting NEXUS classification.
- **Verify-research auto-spawn pattern reaffirmed.** Two parallel sub-agents spawned (Buffett + BOJ) without per-spawn permission. One verified PRIORITY-route, one killed MISFRAMED. ROI on verify-spawning held: caught 1 misframed-claim that would have polluted BOARD.

### NEXT SESSION
1. **Apr 21 (Tuesday — 2 days)**: WAL + ZION earnings + Iran ceasefire expiry. **Bifurcation framing is dead** — operational (Apr 18 SoH re-closure verified) AND political (Apr 18 Sit Room w/ Bessent) BOTH lean re-escalate. Pre-position checklist Monday: catalyst stack is now single-direction-risk into Tuesday, not bifurcated.
2. **11-pt cluster + 2 counter-channels (Detrick + Sethi) + 12th-node candidate (Barchart BRK)** on BOARD — cluster has 14 nodes / counter-channels total. Surface to NEXUS proactively for formal classification. RED also has counter-evidence to actually steelman against, not just "lose with grace."
3. **SIG-010 correction note** — INDEX has been updated with correction pointer to SIG-014. Subsequent oil/Iran signals should use SIG-014's verified state (re-closed Apr 18, ~95% transit collapse since Feb 28), not SIG-010's "operationally OPEN" framing.
4. **OZK earnings Apr 16 backfill** — still pending if Will wants. REGINALD likely processed.
5. **Oil 3-pt cluster** (Kpler + Corio + Baker Hughes) still pending BRENT/HAWK reclassification. With Iran SoH re-closed, the physical-tightness thesis aligns rather than competes.
6. **RED refresh STILL OVERDUE** — HY OAS <300 falsification at Day 9+. Buffett 232% + cluster + Iran re-escalation + 2 counter-channels = richest adversarial setup yet. Will owns spawn.
7. **ZHAO awaiting spawn** for China material — now 17d+ stale.
8. **FORGE/STATUS.md** still Mar 25 (~25d).
9. **COP refresh** still deprioritized; gap continues to grow.
10. **Filter v1→v2 review** — at 31 dispatches vs 10-trigger. Overdue by 21 dispatches.
11. **PM-4 batch (6 images, msg 704-709)** received during PM-3 closeout — to be triaged immediately after PM-3 commit/push.

### OPEN DESIGN DECISIONS (need Will)
- **Other-agent boot-sequence rollout** — still pending. Until rolled, agents won't pull from BOARD; only see signals if Will spawns/directs.
- COP refresh cadence — currently OFF (deprioritized). When to turn back on?
- Filter model v1→v2 review trigger: 10 dispatches or 30 days — at 19 dispatches (THRESHOLD HIT 9 ago), target was ~May 11. Review kill_log/route_log, adjust gate thresholds.
