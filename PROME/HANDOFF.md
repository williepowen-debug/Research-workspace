# PROME HANDOFF

**Purpose:** Single live continuity surface for Prome across OpenClaw and Claude Code. Keep this file short: latest 3–5 entries only. Archive older entries to `PROME/archive/`.

**Archive:** Full pre-merge OpenClaw + Claude Code handoff history through 2026-06-14 is preserved in `PROME/archive/HANDOFF_2026Q2.md`.

---

## 2026-06-16 ~13:00 ET — Post-rebase closeout before clear

**Status:** Repo successfully rebased onto latest `origin/master`; local branch is clean except untracked SHADE raw PDFs/venv and is **ahead 1** with `38fd272a PROME: recover SHADE Athene audit artifacts`. No push performed. Safe to clear and reboot; first boot should check git state before deciding whether to push.

**What just happened:**
- Reviewed SAM post-BOJ commits and ORC/SAM follow-ups. SAM’s resolution work is directionally correct; later origin now includes Phase 1b propagation/cleanup and Phase 2 local reconciliation protocol. Remaining SAM lane: Phase 3 compression/TB/expiry cleanup.
- Reviewed CARL commits. CARL FOMC packet + `NEXUS_BRIEF.md` are useful; main issue was downstream NEXUS registry/scope propagation, not CARL analysis. Later origin includes CARL/NEXUS closeout updates.
- Discussed adding KIMI as a read-only verifier/auditor: no edits, no trades, no outbound messages; use for hallucination/consistency guard, pre-merge review, post-catalyst sweeps.
- Pulled/rebased 24 remote commits cleanly. Local recovery commit hash changed from prior `f9a59f33` to `38fd272a` after rebase.

**Next suggested work:** Boot fresh via `PROME/BOOT.md`, then choose one lane: (1) ask Will whether to push `38fd272a`; (2) decide SHADE raw PDF/venv handling; (3) codify Prome generic fleet reconciliation protocol if approved; (4) refresh HEARTBEAT/TODAY only if decision-relevant; (5) keep position reconciliation separate.

**Guardrails:** no push without Will; raw PDFs stay out of Git absent explicit approval; no broad git ops; no trade execution; live market levels need refresh before use.

---

## 2026-06-15 ~13:35 ET — Pre-new-session handoff after MARCO/HENRY pull

**Status:** Local Prome repo is clean and fast-forward synced with origin at `6ed25b4f`. Safe to start a new Prome session from the current local tree. No active OpenClaw child sessions visible; external Claude Code agents may still be working independently.

**What just happened:**
- Pulled HENRY + MARCO closeouts from GitHub. Latest commits include MARCO `326f7b83` / `6ed25b4f` and HENRY `a1d569f1` / `32f52deb` / `eddb026a`.
- MARCO post-push verification: core thesis work is good, but surface hygiene failed. Needs small cleanup commit only: `THESIS.md` contradiction (“funding stronger” then “weaker”), `NEXUS_BRIEF.md` still says v2.4 / MAR-26 78, `SCRATCH.md` stale closeout rows/push-state/78 refs, `STATUS.md` header still session 13.
- HENRY verification: structural work good. `refresh_status.py` retired, `boot.py --selftest` passes, eval suite exists but baseline not run, boot/closeout hardening proposal remains draft-only. Needs small `STATUS.md` cleanup: FRED 6/11/278/CCC956 stale refs, HEN-30 row, “zero cuts” paragraph, credit-drift wording.

**Recommended new-session first move:** follow `PROME/BOOT.md`, but do a lean boot. Do not re-review everything. Immediate queue: (1) coordinate/verify MARCO + HENRY cleanup commits if they push; (2) refresh Prome surfaces (`HEARTBEAT.md`, `PROME/TODAY.md`) only after integrating the cleaned agent surfaces or if decision-relevant; (3) keep position/broker reconciliation separate.

**Guardrails:** no `AGENTS/*` edits by Prome unless Will explicitly approves; pathspec-only; no trade execution; prices/levels need live refresh before citing; if agents are still working, fetch before judging origin state.

---

## 2026-06-15 ~00:05 ET — Context-weight cleanup closeout

**Status:** Prome context surfaces are lighter and synced. Repo should boot clean from latest origin.

**What landed:**
- `44271ffe PROME: prune context surfaces` — compressed root `MEMORY.md`, archived pre-prune memory, slimmed/clarified `BOOT.md`, corrected `STATUS.md` agent map, added prune plan + weight report.
- `0147347a PROME: add lean tool output protocol` — compact diagnostics first; full reads/diffs when correctness requires.

**Key decisions / corrections:**
- Root `MEMORY.md` now holds durable kernels, not historical dossiers.
- `PROME/STATUS.md` no longer assumes HENRY/NEXUS/WALTER stale from the old map; verify current file content before decision use.
- Lean tool-output protocol is active to reduce transcript bloat/compaction pressure.
- OpenClaw update check found installed `2026.5.6`, npm latest `2026.6.6`, beta `2026.6.8-beta.1`; recommendation was stable update when Will wants maintenance.

**Next suggested work:** see `PROME/SCRATCH.md`. Main options: OpenClaw stable update, TODAY/HEARTBEAT dedupe, position-state reconciliation before Jun18/19 expiry cleanup, or HENRY/NEXUS/WALTER content-freshness check if decision-relevant.

**Guardrails:** no `AGENTS/*` edits; no trade execution; broker/position truth unreconciled; push pathspec-only and Will-coordinated.

---

## 2026-06-14 ~20:58 ET — Protocol-prune closeout before reboot

**Status:** Prome startup/handoff cleanup completed and pushed. Safe for Will to reboot into the new lighter boot path.

**What landed this session:**
- `0c012e29 PROME add Jun15 week card and audit cleanup`
- `de95ae74 PROME clear resolved heartbeat blocker`
- `2d3c0216 PROME merge handoff surfaces`
- `b0736265 PROME harden boot and closeout protocols`

**Operational changes:**
- `PROME/HANDOFF.md` is now the single live cross-runtime handoff surface.
- `PROME/CLAUDE_CODE_HANDOFF.md` is a pointer stub; old history is archived at `PROME/archive/HANDOFF_2026Q2.md`.
- `PROME/BOOT.md` now checks repo status before pull/rebase and makes `FLEET_SCAN` / inbox scans conditional.
- `PROME/CLOSEOUT.md` now uses correct `git commit -m ... -- <paths>` syntax and treats push as Will-gated.

**Next reboot:** follow `PROME/BOOT.md`. Highest practical follow-up is still position-state reconciliation before Jun18/19 expiry cleanup, if Will wants trade hygiene.

**Guardrails:** no agent edits made; no trade work done; broker/position truth unreconciled; HYG Jun $75P dead/not actionable; pathspec-only git.

---

## 2026-06-14 ~20:40 ET — Handoff surface merge/prune

**Status:** Consolidated duplicate continuity surfaces.

**What changed:**
- Archived full old `PROME/HANDOFF.md` and `PROME/CLAUDE_CODE_HANDOFF.md` into `PROME/archive/HANDOFF_2026Q2.md`.
- `PROME/HANDOFF.md` is now the only live continuity surface for both OpenClaw and Claude Code Prome.
- `PROME/CLAUDE_CODE_HANDOFF.md` is now a pointer stub to avoid broken references.

**Next:** commit/push this prune bundle if Will approves. Use pathspec staging only.

**Guardrails:** no agent edits; no trade execution; old rails verification-required; push remains Will-coordinated.

---

## 2026-06-14 ~18:35 ET — OpenClaw Prome quick closeout before clear

**Status:** Boot surfaces coherent and synced from prior commits. Week card was created locally, then later committed/pushed in `0c012e29 PROME add Jun15 week card and audit cleanup`. HEARTBEAT stale blocker cleanup was committed/pushed in `de95ae74 PROME clear resolved heartbeat blocker`.

**What changed:**
- Confirmed GitHub was clean/synced at boot.
- Will approved creating `PROME/action-cards/WEEK_2026-06-15.md`.
- Created week card and updated pointers in `PROME/TODAY.md` and `HEARTBEAT.md`.
- Explained separate-clones migration. Will wants to think longer because agent cross-file visibility/messaging is valuable.

**Current follow-up lanes:**
1. Position-state reconciliation before Jun18/19 expiry cleanup if Will wants trade hygiene.
2. HENRY/NEXUS/WALTER dependency refreshes if decision-relevant.
3. WALTER feed-stack infra request.
4. Separate-clones migration — defer; preserve pathspec discipline meanwhile.
5. Prome execution-rails design debt.

---

## 2026-06-14 ~17:30 ET — OpenClaw Prome boot-surface refresh closeout

**Status:** Phase 0–3 boot-surface refresh completed, committed, and pushed as `43388ccb PROME boot-surface refresh 2026-06-14`.

**What happened:**
- Will asked Prome to refresh stale boot surfaces after a large GitHub pull.
- Constraint held: **do not edit agents**.
- Wrote Phase 0/1/2 audit trail files.
- Rewrote Prome/root boot surfaces: `TODAY`, `SCRATCH`, `STATUS`, `ACTIVE_DECISIONS`, `FLEET_SCAN`, `HEARTBEAT`.
- Wrote compaction-safe daily memory: `memory/2026-06-14.md`.
- Pulled upstream agent commits safely with scoped stash/reapply; no conflicts with Prome surfaces.

**Regime encoded:** surface tape de-risked while tail/private/physical stress stayed sticky. HY OAS tight, VIX faded, banks rallied, Brent sub-$90; CCC/SKEW/private-credit/consumer/Japan/physical energy still live.

**Near gates:** BOJ Jun16, FOMC/VIX expiry Jun17, TIC + expiry cleanup Jun18, HYG Jun19 dead/not actionable, HAW-11/T-08 through Jun22, BCRED/Q2/BDC/SAVE late-Jun/Jul.
