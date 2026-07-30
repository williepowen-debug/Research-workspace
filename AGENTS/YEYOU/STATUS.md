# YEYOU — STATUS

**Updated:** 2026-07-30 (revival prep — DAEDALUS, Will-approved; YEYOU idle, not yet run) | **Runtime:** Claude Code session on Will's current box — manual/on-demand, branch model *(OpenClaw/VPS cut 2026-06-26; this line read "GLM (Z.ai) on VM" until 2026-07-30 — a stale-runtime residue from the 7/7-7/8 harness strike, which corrected `CLAUDE.md:4` and missed this file, leaving YEYOU's own two docs contradicting each other for 3 weeks)* | **Phase:** 1 (digest-to-PROME only)

> Review agent (meta). Exempt from domain-agent sections (Convergence Matrix / EXIT / TRADE) — those are for market-domain agents. YEYOU's "dashboard" is the finding ledger at `reviews/REVIEW_LOG.tsv`.

---

## State

🟢 **BRANCH RECONCILED** — files created, ready for first live run:
1. CLAUDE.md created (boot protocol, closeout symmetry, state surfaces documented)
2. STATUS.md created (watermark, open-finding count, budget)
3. REVIEW_LOG.tsv created (finding ledger template)
4. STATE.tsv created (per-agent watermark template)
5. reviews/REVIEW_CHECKLIST.md created (rubric)
6. CLOSEOUT.md created (closeout procedure, aligned with PROME)

## 2026-07-30 — revival prep (DAEDALUS, Will-approved; YEYOU idle throughout)

Will intends to bring YEYOU up. Three residues cleared so revival is spawn-and-go rather than spawn-then-clean:

1. **Stale runtime line** — header above said `GLM (Z.ai) on VM`, cut 2026-06-26. Fixed, with provenance.
2. **Dangling `HANDOFF.md`** — referenced 3× in `CLOSEOUT.md` (:154 skip-rule, :193 comparison table, :203 key-differences); **the file has never existed** and the rule was obsolete anyway (cross-*runtime* continuity ended with the OpenClaw cut). Refs removed; `STATUS.md` is the continuity surface, as `CLOSEOUT.md`'s own comparison already said.
3. **Missing CONTRACT block** — added to `CLAUDE.md` (produces / consumed-by / proof-of-consumption). Encode-existing, no new obligation. Closes the last open row of the 2026-07-03 utility-cohort gap (PAT-033, 5-of-5 lacked it).

**Boot kit verified live: `scripts/boot.py` runs rc=0** (read-only by design, confirmed before running). It is well-built and self-diagnoses the actual blocker — see Watermark.

**Also recorded in `CLAUDE.md` IDENTITY:** the "Codex" half of YEYOU's two-reviewer funnel is **RAV**, live now while YEYOU is not, with a repair-vs-flag split (RAV may repair; YEYOU stays flag-never-fix). YEYOU composes with RAV on revival — it does not replace it.

4. **Enumeration fixed — and the investigation inverted my own diagnosis** (Will-approved as a 4th item; `scripts/boot.py`, read-only script, rc=0 verified on both code paths).

   **What I first claimed:** retired dirs (SENTRY/ATHENA/BARON/FERT/CRUISE) and `.claude` would get watermarks and clog the queue → filter against ROSTER's live set. **That was wrong on both halves:**
   - **`.claude` has zero commits, ever** — it can never enter the queue. Cosmetic only; I overstated the harm.
   - **Filtering by ROSTER liveness would have DESTROYED signal.** Those agents are not quiet — in the 60d to 7/30: **CRUISE 5 commits, FERT 3, BARON 1.** A commit landing in a supposedly-dead agent dir is exactly what a reviewer should see. It would also have restated a registry this script doesn't own.

   **What the enumeration was actually getting wrong — and it's the opposite problem:** an agent dir is now one that **contains a `CLAUDE.md`**, which correctly drops `.claude` *and* `AGENTS/PROME/` (a misrouting **stub** that regrows when agents mis-address packets — last drained `81cb8943`, 9 packets; it holds only a stray `inbox/`). Dormancy is not consulted at all.

   ★ **And the real find: YEYOU could not see PROME.** The coordinator's home is `PROME/` at the **repo root**, so an `AGENTS/`-only walk missed it entirely — while it is **the single busiest writer in the tree (525 commits in 60d).** Added via a named `EXTRA_TARGETS` constant (set it to `{}` to revert). Verified with a real baseline: **PROME now tops the queue at 9 commits / 17 files.** This is **n=4** of the `AGENTS/*`-globbing blind spot — after PROME's absence from DAEDALUS's `FLEET_MAP` (fixed 7/28), FORGE's from `ledger_staleness.py` (found 7/30), and `walter_doctor`'s `_registry_rows` self-skip (fixed 7/29 by RAV). **PAT-071:** the ownership unit and the enforcement unit must be the same unit.

## Watermark

**None yet — and this is the single thing standing between YEYOU and a first run.** `scripts/boot.py` names the decision and recommends the answer:

> *"⚠️ no watermarks in `STATE.tsv` — set a **DEFAULT** baseline (recommend current `origin/master`) so YEYOU reviews only NEW work, not full history."*

Will's call. Recommended: current `origin/master` at spawn time — reviewing forward from the spawn rather than backfilling 4 months of history, which would bury the first digest and is exactly what the boot kit warns against. **The enumeration prerequisite is now cleared** (item 4 above), so this is the last remaining step.

**Expect PROME at or near the top of your first queue.** That is correct, not a bug — it is the busiest writer in the repo and was invisible to this kit until 2026-07-30. Its files are Will-gated, so findings against `PROME/` route as findings; never edit them (root rule #2 and your own flag-never-fix boundary both apply).

## Open findings

None (not yet run).

## Escalation budget (today)

Direct inbox writes used: 0 / 2 per agent. **Phase 1 = digest-to-PROME only; no direct agent writes.**

---

## BOTTOM LINE

**Ready to run, and the only blocker is one decision.** Boot kit verified rc=0 on 2026-07-30; the three doc residues that would have wasted a first session (stale GLM runtime, dangling `HANDOFF.md` ×3, missing CONTRACT block) are cleared. **Next: filter the boot enumeration's dead agents → set the DEFAULT watermark to `origin/master` at spawn → run `scripts/boot.py` → first review pass.** The honest state of the contract is that `REVIEW_LOG.tsv` has zero rows all-time — YEYOU has never reviewed anything, which is what caps it at L2 and is *not* a design defect. The machinery is good; it has never been switched on. Meanwhile the deep-review half of the funnel (**RAV**, Codex) is running solo, so revival closes a pair, not a vacancy.
