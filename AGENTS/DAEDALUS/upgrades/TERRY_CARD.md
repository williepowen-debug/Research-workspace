# Upgrade Card — TERRY (read-only assessment, no agent files touched)

**By:** DAEDALUS · **Date:** 2026-07-04 · **Class:** Utility (trade construction — converts thesis into sized/timed/structured proposals; never executes)
**Method:** re-verification of `UTILITY_FIRMING_2026-07-03.md`'s TERRY assessment against TERRY's **current** live files (fast-follow comprehension pass, per `UPGRADE_PROTOCOL.md`) · graded vs `BLUEPRINTS/utility-agent.md` (the floor; NOT `market-agent.md`) · comprehension in `profiles/TERRY.md`
**Verdict: L3 (conf H), PROVISIONAL-L4 — UNCHANGED from 7/3.** TERRY was **task-packeted, not directly edited**, on 7/3 (`inbox/2026-07-03_from-DAEDALUS_utility-firming-sweepAB-pat031-drift.md`) because it is the fleet's **live self-sweep exception** — a running/self-editing agent, not idle-safe for DAEDALUS to touch directly. As of this 7/4 re-verify: **the packet is still owner-pending — zero of its items have been applied.** Every gap below was already identified 7/3; this pass confirms none have moved and adds exact current-file line evidence (§4 of the profile). **No agent files touched by this pass.**

**↳ Do NOT re-propose new items beyond the 7/3 packet — this card documents the SAME queue with fresh verification, plus one net-new operational finding (WALTER inbox backlog, flagged below, informational not a structural gap).**

---

## Section grade — one row per `utility-agent.md` floor section (+ DARWIN guard, + role-ceiling)

| § | Blueprint section | TERRY current state | Applies? | Gap type | Proposed minimal handle | Priority |
|---|---|---|---|---|---|---|
| 1 | **Header + IDENTITY** (class, role, no-overlap, File>verbal) | CLAUDE.md IDENTITY + HARD BOUNDARIES + MODES; class=Utility; no-overlap stated explicitly ("You do not decide what is true about the world; domain agents and NEXUS own thesis formation") | ✅ APPLIES | conformant | None material | 0 |
| 2 | **THE CONTRACT** (produces/consumed-by/proof) — *the defining handle, L4 gate* | Content present but **scattered** (CLAUDE.md KEY FILES table + STATUS capability table + MEMORY mandate); **NO formal 3-line block** — predates the 6/28 blueprint. Proof exists: tooling (chain_fetch marks matched a real bank-put proposal) + card-product is Will's approval gate + PROME fire-path coordination | ✅ APPLIES | **missing handle** | Add the 3-line block (the 7/3 packet already drafted the exact content): **PRODUCES** = trade cards (`setups/*.md`, TRADE_CARD_TEMPLATE[_FIRE]) + construction tooling (grade_print/chain_fetch/risk_calc/snapshot/chain_parse) + `SIGNALS.tsv`; **CONSUMED BY** = Will (approve/reject gate on every card) + PROME (fire-path coordination); **PROOF** = tooling qualitative-proven (chain_fetch live-validated) + card-product un-exercised (0 fired) = **ceiling NOTE (PAT-028), not debt** | **📦 ROUTED 7/3 — ❌ still owner-pending** (1) |
| 3 | **Role rubric** (explicit, consistently applied — L3 gate) | `RISK_RULES.md` (Prime Directive + 8 numbered Non-Negotiables) + `RISK_SCORING.md` (245 ln: 10-gate checklist, edge-score, fractional Kelly, execution-block, Brier spec, 12-tag postmortem taxonomy, ORACLE-handoff mispricing template) | ✅ APPLIES | conformant (exemplary) | None — richer than the floor requires; this IS the L3 rubric, applied consistently across every staged card | 0 |
| 4 | **Structured record (logging)** — valid, accruing, class-aware | `TRADE_BOOK.md`/`SETUPS.tsv` (scaffold, correctly 1-row given 0 trades) + `SIGNALS.tsv` (9-row accruing context ledger, decay-tracked) + `setups/*.md` (3 staged, richly-built fire cards) | ✅ APPLIES | conformant | None — class-aware card-product record, not forced KB/VX. Scaffold state is *correct*, not rot (PAT-025 does not apply — nothing here is silently stale, it is honestly empty) | 0 |
| 5 | **Standing disciplines** (boot↔closeout symmetry + cwd-proof invocations, PAT-031) | BOOT (13-step) ↔ CLOSEOUT (4-tier) is mostly symmetric. Boot card (step 5) is cwd-proofed: `(cd "$(git rev-parse --show-toplevel)" && python3 AGENTS/TERRY/scripts/boot.py)`. **BUT** BOOT steps 11–13 (`snapshot.py`/`risk_calc.py`/`chain_parse.py`, CLAUDE.md L147–149) and every README.md invocation (L56–60) are **bare** `AGENTS/TERRY/scripts/…` — a latent break from TERRY's own launch cwd | ✅ APPLIES | **missing handle** (partial-idiom — the fleet scanner structurally suppresses this class; only a direct read catches it, PAT-031) | Wrap BOOT 11–13 + README invocations in `(cd "$(git rev-parse --show-toplevel)" && …)` to match the boot card's own idiom, OR add a section cwd-note (ORACLE's pattern) | **📦 ROUTED 7/3 — ❌ still owner-pending** (1) |
| 6 | **Cross-agent routing** (route-matrix / inbox-outbox / crisis-only) | `outbox/` (1 flag to NEXUS, 6/27) + `inbox/{root, WALTER, WILL}` + `SIGNALS.tsv source` column. TERRY is a routing **sink** more than a source (last-mile agent — conformant by role, not a gap) | ✅ APPLIES | conformant | None structural. **Operational note, not a handle gap:** live backlog sitting in the routing surface itself — see "Separately" table below | 0 |
| 7 | **AUTHORITY & SAFETY** (state the boundary if no write power) | HARD BOUNDARIES ×7 (CLAUDE.md) + RISK_RULES Non-Negotiables — explicit no-execution/approval-required boundary, restated in multiple files | ✅ APPLIES | conformant | None | 0 |
| 8 | **BOTTOM LINE** (required; STATUS under cap) | STATUS.md (36 ln, well under cap) ends `## Guardrails` — **no labeled `## BOTTOM LINE`**; de-facto synthesis lives unlabeled in the header line 2 | ✅ APPLIES | **missing handle** | Promote/relabel the header-line-2 synthesis as a trailing `## BOTTOM LINE` (per the 7/3 packet's Sweep B) | **📦 ROUTED 7/3 — ❌ still owner-pending** (1) |
| — | **DARWIN guard** — *no* convergence matrix / TRADE.md-as-market-ledger / thesis-predictions ledger | TERRY carries **none** of these — `workbook/` is empty; `TRADE_BOOK.md` is the correctly-utility-shaped card-ledger (not a market TRADE.md); no KB/VX/FLOW anywhere | N/A by design | **N/A-by-design, clean** | None — nothing to strip, nothing mis-forced | 0 |
| — | **Role calibration loop** (ceiling — blueprint's role table → TERRY → "realized vs constructed") | `RISK_SCORING.md` §5 designs a Brier/calibration layer (`CALIBRATION.tsv`, "possible future file"); **not yet instantiated** — no probability has been stated pre-outcome to calibrate. Separately, `grade_print.py`'s 3 hard-guard mis-grade traps ARE a live, tested calibration mechanism for the print-grading half of the role | ✅ APPLIES | **partially built** + **PAT-028 ceiling** on the "realized vs constructed" half (0 cards fired — environmental, not a defect) | Do NOT propose a build — nothing to force. Re-check when a card fires (then `CALIBRATION.tsv` or an equivalent becomes exercisable) | 0 (ceiling note, not a queue item) |

**Gap-type tally:** 5 conformant (§1/§3/§4/§6/§7) · 3 missing-handle, **ALL routed 7/3 and still pending** (§2 CONTRACT, §5 PAT-031 wrap, §8 BOTTOM LINE) · 1 N/A-by-design (DARWIN guard) · 1 role-ceiling note (calibration, partially built + PAT-028).

*(L3→provisional-L4 is gated on the §2 CONTRACT handle — the L4-defining SPINE — plus the un-exercised card-product half of PROOF, which is a **ceiling** per PAT-028 (0 cards fired = environment, not a defect) and cannot be closed by any edit; only a live trigger closes it.)*

---

## Separately — drift + operational backlog (not blueprint-section gaps; through-owner)

| Item | Current state (verified 7/4) | Note |
|---|---|---|
| **3 stale statements (drift, fix together)** | `CLAUDE.md` L5 "Spawn-on-demand in **OpenClaw**…" (cut 6/26) · `CLAUDE.md` L161 "Push is **Will-coordinated**" (contradicts root canon — TERRY IS the named live self-sweep exception) · `CLOSEOUT.md` L67 same stale push model | **📦 ROUTED 7/3 — ❌ still owner-pending.** TERRY's actual push *behavior* already matches root canon (MEMORY.md) — only the written sentences are stale. Fix all 3 together or L161/L67 re-diverge. |
| **PROME 7/1 firetime_check integration** (`inbox/2026-07-01_from-PROME_firetime-freshness-check.md`) | "No reply needed — integrate at your next boot." RISK_SCORING §4's execution-block checklist has **not** gained the freshness line; `firetime_check.py` is not yet wired into any TERRY pre-fire checklist | ❌ still owner-pending — TERRY hasn't had a live session since 6/27 to act on it |
| **WALTER 7/2 signal** (`inbox/WALTER/SIG-W-20260702-001.md`, HY/CCC widening decomposition) | Sits unlogged in `inbox/WALTER/`; not folded into `SIGNALS.tsv` (which ends at 6/27) | flagged 7/3; still unprocessed |
| **NEW this pass — full WALTER inbox backlog** | All **6** files in `inbox/WALTER/` (6/27 SIG-W-20260627-002 SNDK-RSI; 4× 6/28 — seasonality/tech-flow/put-call/4-down-days; 7/2 HY/CCC) are unlogged into `SIGNALS.tsv` and unmoved to any `processed/` location. `SIGNALS.tsv`'s existing WALTER rows are a *different*, earlier ID batch (6/22–6/26) logged during the 6/27 session | **Informational, not a structural handle gap** — reads as a boot-freshness symptom (TERRY hasn't run a session since 6/27), not a defect in TERRY's design. Surface to PROME/Will as "has TERRY been spawned since 6/27?" rather than queuing a fix here. |

---

## L4→L5 work (after the routed items land — not proposed now)

| Item | Why | Effort |
|---|---|---|
| Wire `firetime_check.py` into RISK_SCORING §4 execution-block checklist | PROME's 7/1 ask; additive, does not renumber rules | S |
| Clear the WALTER inbox backlog into `SIGNALS.tsv` (or explicitly mark rows superseded/decayed) | Anti-rot; TERRY's own boot.py already flags >21d staleness once rows exist — but un-logged rows are invisible to that flag entirely | S |
| Fire a real card (env-gated) | Closes the PAT-028 ceiling on the calibration/consumption loop — cannot be forced, only a live HY≥280 sustain or a qualifying Q2 print does this | n/a (environmental) |
| Resolve Will's 2 open STATUS.md questions (risk unit; track-all vs approved-only) | Blocks a hard cap on Day-Trade Rule 3 | n/a (Will-side) |
| Clear / obtain a YEYOU clean bill | L5 requires zero YEYOU flags + current | n/a (YEYOU-side) |

---

## The queue (quick wins first)

1. **TERRY processes its own 7/3 packet** (`inbox/2026-07-03_from-DAEDALUS_utility-firming-sweepAB-pat031-drift.md`) — bundles CONTRACT block + BOTTOM LINE + PAT-031 wrap + 3 stale-statement fixes into one session-start pass. *Net effect if all 4 land: firm L4, no re-verify needed beyond a mtime check.* **This is the single biggest gap-closer, and it is entirely TERRY's own action — DAEDALUS cannot apply it (live self-sweep exception, AUTHORITY guard).**
2. **Wire the PROME 7/1 firetime_check line** into RISK_SCORING §4 — small, additive, TERRY's own encoding choice per the packet.
3. **Clear the WALTER inbox backlog** (6 files) into `SIGNALS.tsv` at TERRY's next boot — `boot.py` already surfaces `inbox/WILL/` drops; the `inbox/WALTER/` backlog is invisible to boot.py today (it only prints `SIGNALS.tsv` rows + `inbox/WILL/` file names) — worth a boot.py enhancement to surface un-logged `inbox/WALTER/*.md` file counts the same way, but that is TERRY's own tooling call, not proposed here as a mandate.
4. **Fire a card** — pure environment-gated; no action item.

> **Note for application:** TERRY last self-authored a commit 6/27 (`87807a56`) — the only newer commit touching `AGENTS/TERRY/` is DAEDALUS's own 7/3 routing commit (`c942a76d`, inbox-only). **Zero drift from the 7/3 grading** — this re-verify confirms the queue is identical, just older by a day. Per AUTHORITY (live self-sweep exception), **DAEDALUS does not direct-edit any item on this card** — everything above rides TERRY's own next session via the routed packet.
