# PROME HANDOFF
**Date:** 2026-05-15 22:16 ET
**Status:** ✅ Clear-ready — fresh session should use updated BOOT sequence. New Claude Code Prome planning artifacts are discoverable; next build step is Phase 1 bootstrap files.

---

## Claude Code Prome Build Pointer

Will wants a persistent **Claude Code Prome**: same Prome identity, repo-native implementation surface.

Read these before continuing that work:

1. `PROME/CLAUDE_CODE_PROME_PLAN.md` — architecture/rationale.
2. `PROME/CLAUDE_CODE_PROME_TASKS.md` — restart-safe phase/task ladder.

Current state:

- Phase 0 planning is complete.
- **Phase 1 bootstrap files are complete**:
  - `PROME/CLAUDE.md`
  - `PROME/CLAUDE_CODE_PROME.md`
  - `PROME/CLAUDE_CODE_HANDOFF.md`
- Next step is **Phase 2 — Architecture Integration**:
  - update `AGENTS_DIRECTORY.md`
  - add full runtime split section to `PROME/SYSTEM.md`
  - update `PROME/BOOT.md` for post-scaffold Claude Code handoff behavior
- Do not commit yet; leave diffs unless Will explicitly approves.

---

## Immediate State

Will asked to clear for a fresh session and prep handoff.

**Current working posture:**
- Regime: **BDC/private-credit credit + mark stress confirmed, but public-credit contagion unconfirmed.**
- FSK Q1 was **Strong Bear / near Max Bear**: NAV -9.9% QoQ, adjusted NII $0.41, distribution reset to $0.42, non-accruals 8.1% cost / 4.2% FV, net debt/equity 1.31x, KKR support package + revolver amendment.
- Public tape still refuses cascade: **HY OAS 282bps, VIX 17.85** as of May 14 08:26 dashboard.
- Stress is concentrated in **Brent/gas, USD/JPY near red, BIZD red, KRE/WAL yellow**, while broad credit/vol remain benign.
- New gamma/momentum screenshots were logged/routed as a 🔴 market-structure signal: positive gamma / 0DTE may be suppressing VIX despite underlying BDC/bank/energy stress.

**No trades executed. No external messages sent. No active spawns.**

---

## Files Updated This Session

### Updated
- `PROME/CLAUDE_CODE_PROME_PLAN.md` — draft architecture plan for one-Prome/two-surfaces design.
- `PROME/CLAUDE_CODE_PROME_TASKS.md` — restart-safe task ladder with clear checkpoints; Phase 1 marked complete.
- `PROME/CLAUDE.md` — Claude Code Prome bootstrap.
- `PROME/CLAUDE_CODE_PROME.md` — Claude Code Prome operating manual.
- `PROME/CLAUDE_CODE_HANDOFF.md` — dedicated Claude Code Prome handoff file.
- `PROME/BOOT.md` — now points fresh sessions to the Claude Code Prome plan/task ladder when relevant.
- `PROME/HANDOFF.md` — now includes this Claude Code Prome build pointer.
- `HEARTBEAT.md` — refreshed May 14 08:26 ET with dashboard levels, claims, and gamma/momentum routing note.
- `FORGE/signals/2026-05-14_gamma_momentum_factor_squeeze.md` — signal log from Will screenshot batch.

### Routed signal inbox notes
- `AGENTS/HENRY/inbox/signal_2026-05-14_gamma_momentum_factor_squeeze.md`
- `AGENTS/VIOLET/inbox/signal_2026-05-14_gamma_momentum_factor_squeeze.md`
- `AGENTS/LIQUID/inbox/signal_2026-05-14_gamma_momentum_factor_squeeze.md`
- `AGENTS/NEXUS/inbox/signal_2026-05-14_gamma_momentum_factor_squeeze.md`

---

## Current Market / Thesis Read

### Base read
**Fragile melt-up / mechanically calm surface, deteriorating understructure.**

- **Not all-clear:** BDC/private-credit stress is real; FSK validates deterioration in marks/income and sponsor-support stabilization.
- **Not cascade-confirmed:** HY OAS <300 and VIX <20 block broad panic-short posture.
- **Tape explanation:** Momentum + positive gamma + 0DTE can keep VIX suppressed and indices stable even while internals and credit-adjacent equities weaken.

### Actionable implication
- Do **not** add broad cascade/panic shorts just because gamma is extreme.
- Do **prepare** targeted downside where evidence exists: BIZD/BDC complex, select PE-credit names, and regional banks if Call Reports/tape confirm.
- APO/ARES June: thesis may be directionally right but timing risk is high; do not throw good premium after bad without fresh confirmation.
- Watch **WAL/KRE + BIZD + VIX together**. If banks/BDCs weaken and VIX wakes up despite gamma, regime may be shifting.

---

## Latest Dashboard Levels

From `FORGE/tools/market-data/dashboard.py --compact` run May 14 08:26 ET:

- HY OAS **282bps 🟢**
- CCC OAS **937bps 🟡**
- Brent **$103.87 🔴**
- Gas weekly **$4.50 🔴**
- USD/JPY **157.89 🟡 / near red**
- Initial claims **200,000 🟢**; shadow-adjusted estimate **255,000**
- Continuing claims **1,766,000 🟢**
- SOFR-IORB **-0.06 🟢**
- 10Y yield **4.46 🟡**
- KRE **$67.14 🟡**
- WAL **$74.97 🟡 / bear-line breach**
- APO **$131.60 — still above $130 watch**
- BIZD **$12.57 🔴**
- VIX **17.85 🟢**

---

## Position Decisions Pending

| Priority | Decision | Current Rail |
|---|---|---|
| 🔴 | **APO puts — hold/roll/cut** | OBDC says hold/roll bias; no add. Reassess if APO >$130 for 3 sessions or HY OAS <260 sustained. |
| 🔴 | **Fresh BDC/private-credit downside** | FSK Strong Bear allows discussion, but needs live bid/ask and Will approval. Prefer liquid longer-dated BIZD/ARCC-type structures if pricing sane. |
| 🟠 | **ARES $95P Jun** | Hold only if FSK/GCRED/OTF/BDC wave shows continued mark pressure; otherwise June theta risk dominates. |
| 🔴 | **KRE/WAL/OZK bank shorts** | Use `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md`; next step is Call Report MI3/NDFI/ACL/liquidity checks. |
| 🟠 | **ZION Jul put** | Prior posture: kill/no-roll if usable bid unless Call Report MI3/RCON2746 surprises. ZION remains under-researched, not exonerated. |

---

## Highest-Value Next Actions for Fresh Session

1. **If continuing Claude Code Prome build, start with `PROME/CLAUDE_CODE_PROME_PLAN.md` + `PROME/CLAUDE_CODE_PROME_TASKS.md`.**
   - Current next step: Phase 2 architecture integration.
   - Keep work small and clearable.

2. **Run boot sequence from updated `PROME/BOOT.md`.**
   - If `git pull --rebase` is blocked by dirty/untracked files, stop and read status/handoff; do not stash/commit/reset without Will approval.

3. **Refresh live dashboard before citing levels.**
   - `python3 FORGE/tools/market-data/dashboard.py --compact`

4. **Regional-bank Call Report triage.**
   - Apply `PROME/action-cards/REGIONAL_BANK_WEEKEND_TRIAGE_MAY9.md`.
   - Focus: WAL, OZK, EGBN, CFG, VLY, ZION, FITB, SSB/HBAN as needed.
   - Extract only decision metrics: MI3/RCON2746, NDFI/warehouse/fund finance, ACL/NCO/nonaccrual migration, FHLB/brokered deposits/liquidity, CRE/multifamily maturity.

5. **BDC/private-credit decision prompt.**
   - Use `PROME/FSK_Q1_READ_MAY11.md` and `PROME/action-cards/FSK_MAY11_ACTION_CARD.md`.
   - Frame fresh downside only if live pricing is sane; do not rescue dead June premium by default.

6. **Gamma/vol-suppression follow-through.**
   - Check HENRY/VIOLET/LIQUID/NEXUS inboxes for the new signal.
   - Key question: is VIX <20 informational, or mechanically suppressed by positive gamma/0DTE?

---

## Rules / Constraints

- **No trade execution without Will approval.**
- **No external/public messages without approval.**
- **No broad bank-premium add** unless Call Reports/tape move to Bear / Strong Bear.
- **No broad cascade short** while HY OAS <300 and VIX <20.
- **No rolling every losing June contract.** Prefer one or two higher-delta candidates only if confirmed.
- **Do not spawn REGINALD, CARL, SAM, RED, or BRENT.** They are persistent/managed.
- **WALTER owns signal/news routing; Prome owns tasking, rails, and synthesis.**
- **Do not commit/stash/pull/reset dirty git state without Will approval.**

---

## Suggested Fresh-Session Prompt

> Continue from `PROME/HANDOFF.md`. Run the updated `PROME/BOOT.md` sequence, but do not force git if dirty. If working on Claude Code Prome, read `PROME/CLAUDE_CODE_PROME_PLAN.md` and `PROME/CLAUDE_CODE_PROME_TASKS.md` first; next step is Phase 2 architecture integration. Otherwise refresh live dashboard first. Current model: BDC/private-credit stress confirmed by FSK, but public cascade unconfirmed because HY OAS/VIX remain benign. Focus on regional-bank Call Report triage and BDC/private-credit decision rails. Treat the gamma/momentum signal as a vol-suppression / air-pocket overlay, not standalone short confirmation. Do not spawn REGINALD/CARL/SAM/RED/BRENT and do not trade without Will approval.
