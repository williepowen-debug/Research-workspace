# SCRATCH.md — Ephemeral Session State
**Last Updated:** 2026-05-22 (CC-Prome session — 6/18 trigger set v0.1 + 3 SIGs filed)

## What Just Happened

Single focused CC-Prome session — FORGE rehab Step-5 follow-up.

Boot from fresh context; HEAD already at origin via WALTER's 5/21 closeout push-train. Comm-mirror check passed (2 inbound ACKed 5/21; channel quiet). Then walked through FORGE rehab open Will-decisions.

Initial framing was "sell/roll anything for June." Pushed back on ticket-cost asymmetry — the 6 theta-killers are roll-vs-let-expire decisions, not sell candidates. Will then surfaced the deeper vol-floor/ATH concern: rolling equity puts at suppressed vol pays rich premium. That's exactly the pattern saved in `feedback_put_vs_duration_expression` memory.

**Decision pivot:** from active "decide 6 dispositions now" → **pre-register triggers, default let-expire, only act on regime-break confirmation**. Closes BROCK LESSONS #16 execution-rails design loop. First instance of pre-registered cluster rails as a reusable artifact pattern.

**Trigger set v0.1 drafted + saved** (`FORGE/trigger-sets/JUN18_CLUSTER_2026-06-18.md`). 4 regime-break triggers (VIX / HY OAS ×2 / KRE), 5 position-specific (HYG / EGBN / WAL ×2 / KRE), hard backstop 6/16 16:00 ET. AAL + CF dropped (no domain owner; mechanical let-expire). TLT $85P × 3 (winner, +92%) routed separately.

**3 calibration SIGs filed in parallel** to BROCK / REGINALD / HENRY inboxes (untracked-by-design; recipients commit on integration). Default-pass 2026-05-24 EOD. PROME consolidates → v0.2 → single Will-approval packet (not 3 parallel conversations).

**Commit `dc63c709`** pushed via WALTER push-train (real-time, 2nd concrete instance of pattern). Origin landed at `32d619e6` containing my work + OTTO's 5/22 closeout + WALTER's 5/22 BOARD dispatches.

## Current Git State

Clean. Local HEAD = origin/master at `32d619e6`. My closeout commits (this file + memory daily log + HANDOFF entry + auto-memory) staged after this rewrite, awaiting commit + push.

Working tree at this entry:
- PROME-side staged + uncommitted: `PROME/SCRATCH.md`, `PROME/CLAUDE_CODE_HANDOFF.md`, `memory/2026-05-22.md`, auto-memory file
- Foreign uncommitted: `WILL/share/agents capture image.JPG` (Will's own)

Push-train risk if multiple closeouts collide: low — OTTO and WALTER both closed before me; SAM/BOND/BROCK/REGINALD/HENRY not active.

## Next Planned Work

**🟡 Trigger set v0.2 consolidation arrival window:**

By **2026-05-24 EOD** (default-pass deadline). Three possible arrivals:

1. **BROCK reply** — HY OAS R2/R4 thresholds + HYG roll target + sub-90¢/bank-PC trigger wording. Likely route: BROCK outbox file `REPLY-PROME-2026-05-22-credit-trigger-calibration.md` per Convention B (own-outbox routing), OR STATUS.md update.
2. **REGINALD reply** — KRE R3 + WAL break-zone + WAL/KRE/EGBN roll targets + late MI3/FFIEC PDD likelihood.
3. **HENRY reply** — VIX R1 + **TLT decision packet** (split + strike + expiry). TLT decision is the highest-urgency leg of HENRY's response since it needs Will-approval + execution before 6/13 EOD time trigger.

Next-session boot must scan all three agents' outboxes per `feedback_scan_agent_outboxes_at_boot`. If any reply landed, integrate → v0.2 → Will approval packet. If silent, default-pass: v0.2 = v0.1 + TLT strawman → Will approval packet.

**Will-approval packet target:** single document with (a) consolidated trigger set, (b) TLT decision recommendation, (c) execution-rails monitoring plan. Two outcomes from Will: green-light (adopt + monitor) or revise (specific edits).

**Other carries (unchanged):**

- 🟠 **VIOLET 4/15 VIX/SKEW trade adjudication** — 60d window from 4/13 closes ~6/12 (21 days). Decision overdue.
- 🟠 **FXY $58C reconciliation** — per SAM v1.4, missing from 5/21 CSV. Confirm with SAM (or wait for next CSV refresh).
- 🟠 **TLT $88P May 15 disposition** — was +100% pending Will at Mar 25; absent from 5/21 CSV. RED tax/perf check.
- 🟠 **APD long thesis tag** — 2 sh @ $294.79, unassigned in STATUS.
- 🔵 SAM Sep-18 $60C × 5-10 contracts — post-CPI cheaper entry; SAM-owned trigger.
- 🔵 TODAY.md Path B refresh (drafted but not shipped).
- 🔵 CALENDAR.md refresh (3/27 stale).
- 🔵 HEARTBEAT refresh-cadence design Q (self-referenced in HEARTBEAT).
- 🔵 OZK STATUS hygiene (low priority).

## Cautions for Next Session

- **Trigger set v0.1 is NOT yet adopted.** Will-approval gate is v0.2. Don't reference v0.1 as if it's the live monitoring rail until v0.2 ships.

- **TLT decision is the time-sensitive leg.** TLT $85P × 3 at +92% has theta acceleration starting now. The 6/13 EOD time trigger is the hard backstop; the conditional triggers ($85.50 trim signal, $82 hold-full signal) may fire sooner. If HENRY doesn't respond by 5/24 EOD, the strawman (trim 2 / roll 1 Sep $82P) becomes the de-facto recommendation to Will.

- **Push-train pattern fired in real-time today.** When I ran `git push`, WALTER had just pushed in the millisecond before, sweeping my commit + OTTO's. This means: closeout commits can land on origin via someone else's push before my own push reaches the server. **Next session boot should `git fetch` first to confirm true origin state** rather than assuming local = remote.

- **AAL + CF are mechanical let-expire** — no further action needed unless a domain owner emerges. AAL $10P × 2 ($180 cost) + CF $130C × 1 ($1,167 cost) → expected combined loss ~$1,015. Already absorbed in Will-decision.

- **No persistent-agent spawns at boot.** Do not spawn: CARL, REGINALD, OZK, SAM, RED, BRENT, Claude Code Prome. HENRY/VIOLET/BOND were teams-mode standing-by but released after 5/21 closeout — assume they're terminated unless explicitly respawned.

- **3 SIGs sitting untracked-by-design** in BROCK/REGINALD/HENRY inboxes. Agents own commits on integration. Don't pre-commit them.
