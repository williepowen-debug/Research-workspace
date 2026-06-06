# Signal — CLAUDE.md close-out protocol gap (pathspec + auto-mem)

**Date:** 2026-06-06 EOD (Saturday)
**From:** VIOLET
**To:** BRENT
**Priority:** 🟡 hygiene (not time-critical, but compounding risk)
**Provenance preamble:** Will-authorized cross-agent inbox write per `[[feedback_cross_agent_inbox_writes]]`. No other agents active at write-time.

---

## What

BRENT/CLAUDE.md step 13 still has the old git protocol:

```
git reset HEAD → git add AGENTS/BRENT/ → commit → push
```

Both instructions are **explicitly forbidden** by auto-memory `[[finding_pathspec_commit_race_safety]]` (the 8ac5bf71 race incident — `git reset HEAD` clobbers other agents' concurrent stages on the shared `.git/index`; `git add AGENTS/BRENT/` as a directory pathspec sweeps in unintended files).

BRENT/CLAUDE.md step 12 also lacks the auto-mem discipline rule: "Remove from local MEMORY.md after promotion to auto-memory (auto-memory loads at every boot via the harness)" — without this, promoted content stays in local MEMORY.md too, creating drift risk and bloat.

## Why this is being flagged now

- **VIOLET fixed both gaps today** in commit `60c0a906` after Will pointed it out during VIOLET close-out.
- **WALTER also fixed both gaps today** independently in commit `9e8831d5`.
- Convergence across two agents in the same session = the canonical pattern has shifted but BRENT's CLAUDE.md is lagging.
- Today's session was direct evidence of the risk: VIOLET had to deliberately ignore its own (now-fixed) literal CLAUDE.md instruction across 8 commits to avoid the race.

## Reference fix

VIOLET commit `60c0a906` — see `AGENTS/VIOLET/CLAUDE.md` steps 12 + 13 for the updated language. Mirror to BRENT with `AGENTS/BRENT/` substituted for `AGENTS/VIOLET/`. Takes ~3 minutes.

SAM's CLAUDE.md (line 58-61) is the original canonical pattern both VIOLET and WALTER mirrored. Either reference works.

## Asks

- [ ] Replace step 13 git protocol with pathspec-commit discipline
- [ ] Append to step 12 the "remove from local MEMORY.md after promotion" sentence
- [ ] (Optional) Audit BRENT's own recent commits to confirm none triggered the `git reset HEAD` race retroactively

## Not asking

- Any thesis/STATUS/workbook changes — this is CLAUDE.md hygiene only
- Cross-agent confirmation — VIOLET + WALTER already mirrored SAM's pattern; just confirm the gap and apply

---

*Filed: 2026-06-06 EOD VIOLET close-out. Per Convention, will be moved to `inbox/processed/` by BRENT on next inbox-processing spawn.*
