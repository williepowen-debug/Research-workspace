---
name: WALTER STATUS.md Refactor Pattern (May 4-5 2026)
description: Sequenced-pass structural refactor recipe — diagnostic → plan → per-pass Will checkpoint → POV check mid-flight → persisted running list. Useful when any agent's STATUS.md or boot doc-set has grown sprawling.
type: project
originSessionId: c15e2ae9-4397-46c2-8fba-17e1cdbe3284
---
May 4-5 2026 STATUS.md refactor (WALTER): 204→110 lines / ~80k→~27.5k bytes / 7 commits / 3 new companion files.

**Why:** *Will may want to apply the same pattern to other agents' STATUS.md files later (CARL / REGINALD / BROCK have grown similarly large). Capturing the recipe so future-Claude doesn't re-derive it.*

**How to apply:**

1. **Diagnostic before plan, plan before exec.** Read all the boot docs first, then send a per-doc staleness diagnostic with pattern-level findings. Don't skip to "let me just start cutting" — Will picked the file to start on after seeing the diagnostic.

2. **One or two file changes per pass + per-pass Will checkpoint.** Per `feedback_break_multifile_updates`. STATUS.md refactor was 4 passes + REGISTRY refresh + LAST_COMPLETION rewrite + CLAUDE.md pointer + lead-paragraph rewrite — each landed as a separate commit with a Will-approval gate between.

3. **POV check mid-flight.** After Pass 3, Will asked "any friction?" — flagging 7 items including the Pass-4 prerequisite (REGISTRY refresh) Will hadn't asked for surfaced a real blocker. Without the check, Pass 4 would have been built on stale REGISTRY data.

4. **Persisted running list survives handoff.** `LAST_COMPLETION.md` FOLLOW-UP + OPEN DESIGN DECISIONS sections are canonical, with discoverability pointers in CLAUDE.md IDENTITY + boot step 3. Future-Claude reading boot finds the running list at step 3 every time.

5. **Three structural patterns introduced:**
   - **Companion-doc split**: STATUS doing N jobs → STATUS does live state, companion docs hold session history (`SESSION_LOG.md`), design completeness (`design/STATE.md`), macro anchors (`anchors/`).
   - **Verified-as-of stamp + re-verify trigger**: load-bearing macro state in single-purpose anchor file with explicit "verified-as-of {date}" + re-verify rule ("kinetic state-change OR every Nd OR pre-dispatch on cluster"). Beats embedding in STATUS where it goes stale invisibly.
   - **Regenerate-at-closeout**: any state with canonical source elsewhere (REGISTRY.tsv) regenerates each closeout instead of being snapshotted. Encoded in CLAUDE.md spawn-protocol step 12 as 4 sub-steps.

**Anti-pattern to avoid:** trying to do trim + restructure + content-rewrite in one big sweep. Will's "don't hammer it in one pass" feedback (Apr 20, also see `feedback_break_multifile_updates`) is the load-bearing rule.

**Net STATUS.md byte reduction by phase:** Pass 1 (trim) ~50k bytes cut (biggest). Pass 2 (design state split) ~4k cut (smaller — table NOTES were already concise). Pass 3 (anchor extraction) ~flat (replaced ~12 lines with 3-line pointer + new file). Pass 4 (table → regenerated subsection) ~flat (denser content in same byte budget). Lead-paragraph rewrite ~850 bytes cut (less prose, more structured bullets).

**Pattern transfers to:** any agent STATUS.md sprawling beyond ~5k tokens / ~25k bytes / mixing multiple concerns (live state + design completeness + history + curated snapshots). CARL / REGINALD / BROCK are likely candidates per Will-mentioned context.
