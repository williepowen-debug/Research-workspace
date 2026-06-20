# PROME HANDOFF

**Purpose:** Single live continuity surface for Prome across OpenClaw and Claude Code. Keep this file short: latest 3–5 entries only. Archive older entries to `PROME/archive/`.

**Archive:** Full pre-merge OpenClaw + Claude Code handoff history through 2026-06-14 is preserved in `PROME/archive/HANDOFF_2026Q2.md`.

---

## 2026-06-19 ~21:15 ET — Closeout after CORAL Phase 1 + Geneva heartbeat

**Status:** CORAL Phase 1 maturity scaffold is on origin. Geneva gate resolved de-escalatory and `HEARTBEAT.md` was updated locally; heartbeat + this closeout are local-only unless Will asks to push. Current market read: energy shock deferred, HY **263 [FRED 6/17]** still 3bp above <260 kill, banks/VIX calm, carry red.

**What landed:** CORAL got mature-agent boot surfaces and protocol: `SCRATCH.md`, `NEXUS_BRIEF.md`, `board_log.tsv`, and CLAUDE boot/write-back/WALTER intake rules. CORAL peer-integration drift fix and Phase 1 commit were both pushed. Heartbeat now reflects U.S.–Iran MOU / Hormuz reopening / 60-day fuse.

**Files edited:** `HEARTBEAT.md`, `PROME/SCRATCH.md`, `PROME/TODAY.md`, `PROME/STATUS.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/HANDOFF.md`, `memory/2026-06-19.md`. Agent files were edited only under Will-scoped CORAL Phase 1 and pushed before this closeout.

**Next suggested work:** fresh boot should verify git ahead/behind first. If market lane, refresh HY/dashboard and check Jun20 CFTC. If CORAL lane, consume pending WALTER handoffs `SIG-W-20260619-002` and `SIG-W-20260619-007` through `board_log.tsv` + `git mv`.

**Risks / blockers:** local-only heartbeat/closeout commits are not on origin until pushed. Do not edit WALTER specs from Prome; WALTER owns future tuning. No trade/expiry action without broker/Will truth.

---

## 2026-06-19 ~15:45 ET — Final synced closeout; WALTER v0.18 active

**Status:** Repo was rebased over origin and pushed cleanly; final state expected clean/synced. WALTER ratified the deep-research candidate flag as CHECKLIST **v0.18** and Prome verified the landed spec/ledger/doctor/STATE/CLAUDE surfaces. Market regime unchanged: HY OAS **263 [FRED 6/17]** near <260 kill; banks/VIX benign; carry red.

**What landed:** Prior Prome closeout commit was rebased and pushed. Final Prome state now updates from “greenlit/local-only” to “WALTER v0.18 active / repo synced.” Daily log appended with rebase/push + WALTER verification.

**Next suggested work:** fresh boot should find repo clean/synced. If system lane, monitor WALTER v0.18 behavior/doctor output rather than editing specs. If market lane, refresh HY/dashboard and watch <260 / bank-PC offset. If SAM lane, check Jun20 CFTC against v1.6 convexity survival gates.

**Risks / blockers:** no Prome edits to WALTER specs; WALTER owns future tuning. Quick-WALTER still cannot judge fresh news or deep-research flags. No trade/expiry action without broker/Will truth.

---

## 2026-06-19 ~14:53 ET — Closeout local-only; WALTER deep-research flag greenlit

**Status:** Closeout edits are local-only per Will's instruction to stop short of pushing. Prome reviewed SAM/HAWK pushed changes, the ORC/WALTER deep-research candidate proposal, and refreshed the Jun19 dashboard. Market regime unchanged: HY OAS **263 [FRED 6/17]** remains 3bp above the <260 kill line; banks/VIX benign; carry red.

**What landed in Prome state:** `PROME/SCRATCH.md`, `PROME/TODAY.md`, `PROME/STATUS.md`, `PROME/ACTIVE_DECISIONS.md`, this HANDOFF entry, and `memory/2026-06-19.md` capture the session. Commit should be local-only; push only when Will approves.

**Key decisions / reads:** WALTER deep-research candidate flag is greenlit for **WALTER-owned ratification**, not Prome direct edits. v1 shape: Full-WALTER-only Phase 2.8, mandatory materiality gate, dispatched signals only, 11-col TSV ledger with `prompt_ref` + `deadline`, no FORMAT_SPEC header, and narrow `walter_doctor` overdue-pending check. SAM v1.6 EV table supports hold-small-stub / no add; Jun20 CFTC is next gate. HAWK audit fixes look clean.

**Next suggested work:** pull/verify repo; if WALTER has landed the feature, inspect actual CHECKLIST/ledger/doctor diff + version-drift output. If market lane, refresh HY/dashboard and watch <260 / bank-PC offset.

**Risks / blockers:** do not push local closeout without Will. Do not edit WALTER specs from Prome; WALTER owns ratification. No trade/expiry action without broker/Will truth.

---

## 2026-06-18 ~14:05 ET — Closeout before fresh session; Quick-WALTER paused for fresh news

**Status:** Repo is clean/synced. WALTER/Prome/ORC resolved the mini-WALTER boundary after the Moscow MNPZ A/B test. Full Claude Code WALTER is the signal desk. Prome/Quick-WALTER is paused for fresh news and may route only pre-registered RED-FT / REG-T / safety-net trigger fires with fixed recipient_chain, plus non-routing delivery repair/backfill for existing BOARD signals. Fresh screenshots/news/Visegrad/aggregator/source-confidence/recipient-selection all queue/escalate to Full WALTER.

**What landed:** WALTER docs/specs pushed through the registry-only Quick boundary + UTC timestamp discipline; Moscow MNPZ timestamp fixed to true UTC; RED delivery_log row fixed to valid `COMMITTED`; HEARTBEAT/TODAY/Prome state updated. `walter_doctor` reconciles BOARD at 286 and shows all WALTER handoffs delivered; only known stale upstream feeds remain.

**Market state:** HY OAS **263 [FRED 6/17]** is 3bp above the <260 R3/blended-credit kill line. Claims were benign/yellow; VIX/banks faded stress; USDJPY/FXY carry worsened. Broad cascade unconfirmed, kill line close.

**Next suggested work:** fresh boot from `HEARTBEAT.md`, `PROME/SCRATCH.md`, `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md`. Choose lane: market monitoring (HY <260 / TIC-FXY / banks-PC), or system design for a group-chat VERIFY/CONTEXT helper that fact-packs signals without routing authority.

**Risks / blockers:** do not spawn Quick-WALTER for fresh news; do not create parallel signal artifacts. Legacy parallel artifacts remain historical (30 `FORGE/signals/*.md`, 14 generic agent inbox signal files) and need a deliberate archive/leave decision. No trade/expiry action without broker/Will truth.

---

## 2026-06-17 ~21:32 ET — WALTER v2 proven; delivery/push model next

**Status:** WALTER Routing v2 is now validated end-to-end on the real path. Real `agentId=walter` Quick mode passed Case A delivery and Case B Iran-anchor refusal/escalation. BRENT and HAWK consumed their backfills; doctor shows zero WALTER handoffs in flight and zero awaiting delivery. Local unpushed commits now include Prome's operating-model correction plus WALTER/OpenClaw consume rollout for remaining OpenClaw recipients.

**Key correction from Will:** serious domain-agent work mostly happens in Claude Code terminals on desktop/laptop, not inside VPS/OpenClaw. Treat VPS/OpenClaw as Prome's Telegram orchestration/interface layer. Therefore origin push is the practical visibility boundary for routed WALTER signals, even if same-clone OpenClaw delivery works immediately for tests.

**What landed / is local:** Prome memory correction (`Real Agent-Work Surface Is Claude Code`) plus WALTER consume-step scaffolding for BROCK, LIQUID, HENRY, LABOR, NEXUS, VIOLET, SHADE. BRENT + HAWK are already pushed/durable.

**Next suggested work:** brainstorm and choose WALTER/Prome delivery-push policy: immediate push for every route vs urgency-tiered push vs explicit pending-route flush queue. Recommendation to test: urgency-tiered push with visible pending-route queue and manual flush command.

**Risks / blockers:** latest local commits are not pushed yet; Claude Code sessions cannot see them until origin is updated. PROME push automation for FLASH/IMMEDIATE to Claude Code recipients remains owed. No trade/position work without broker/Will truth.

---
