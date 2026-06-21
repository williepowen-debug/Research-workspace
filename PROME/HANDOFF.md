# PROME HANDOFF

**Purpose:** Single live continuity surface for Prome across OpenClaw and Claude Code. Keep this file short: latest 3–5 entries only. Archive older entries to `PROME/archive/`.

**Archive:** Full pre-merge OpenClaw + Claude Code handoff history through 2026-06-14 is preserved in `PROME/archive/HANDOFF_2026Q2.md`.

---



## 2026-06-20 ~20:05 ET — Closeout after heartbeat/auto-memory/DEWEY cleanup + pushed-agent audit

**Status:** Repo was clean/synced at closeout start. Current regime source is `HEARTBEAT.md`: signed-but-fraying MOU; Jun20 Hormuz re-closure declared; contested/not kinetic; energy tail re-fat; broad cascade unconfirmed. HY remains **263 [FRED 6/17]** near <260 kill, VIX/banks calm, carry red.

**What landed:** HEARTBEAT refreshed and pushed for Jun20 Hormuz declaration; `memory/auto/MEMORY.md` compacted under the load cap with all 143 links preserved; active-agent push train pulled/audited cleanly; root DEWEY naming aligned in `HEARTBEAT.md` + `AGENTS_DIRECTORY.md`. WALTER-specific drift was identified but deliberately not edited — Will will handle with WALTER.

**Files edited in this closeout:** `PROME/SCRATCH.md`, `PROME/STATUS.md`, `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/HANDOFF.md`, `memory/2026-06-20.md`.

**Next suggested work:** fresh boot should verify repo state, then use `HEARTBEAT.md` for the market frame. Market lane: Jun22 Brent/Hormuz tape response + HY <260 + CFTC/carry. System lane: wait for WALTER’s own cleanup before touching WALTER. DEWEY lane: CONTEXT refresh before first live run.

**Risks / blockers:** do not repeat shared auto-memory index edits during active agent work; coordinate a push/rebase window first. Do not treat Hormuz closure as kinetic without physical/tape confirmation. No trade/expiry action without broker/Will truth.

---
## 2026-06-20 ~14:59 ET — Closeout after CORAL inbox + thesis rails install

**Status:** Repo is clean/synced to origin. CORAL boot hardening, WALTER inbox processing, and thesis rails are installed and pushed. Market regime unchanged from HEARTBEAT: Geneva de-escalation branch fired, HY **263 [FRED 6/17]** near <260 kill, banks/VIX calm, carry red.

**What landed:** CORAL now has `scripts/boot.py`, processed WALTER inbox (`SIG-W-20260619-002/007/008` moved to processed with `board_log.tsv` rows), updated STATUS/SCRATCH/NEXUS/MEMORY/workbooks, and installed `thesis/THESIS.md` + `thesis/CHANGELOG.md`. Bank-upgrade rail requires ≥2 FL-exposed banks deteriorating or explicit USCB condo-association loan deterioration with corroboration.

**Files edited:** `PROME/SCRATCH.md`, `PROME/STATUS.md`, `PROME/TODAY.md`, `PROME/ACTIVE_DECISIONS.md`, `PROME/HANDOFF.md`, `memory/2026-06-20.md`; CORAL files under `AGENTS/CORAL/` were edited under explicit Will scope and pushed before Prome closeout.

**Next suggested work:** fresh boot should find repo clean/synced. If CORAL lane, build per-metro convergence grid or Q2 FL-bank prep. If market lane, refresh HY/dashboard and check Jun20 CFTC/SAM. If WALTER lane, monitor v0.18 behavior; do not edit WALTER specs from Prome unless scoped.

**Risks / blockers:** no trade/expiry action without broker/Will truth. CORAL thesis values must stay in STATUS/workbooks, not THESIS. Do not upgrade CORAL bank transmission on collateral/household stress alone.

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
