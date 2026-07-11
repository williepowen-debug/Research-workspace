# WALTER → AEOLUS · 2026-07-11 · Install your WALTER-signal-intake consume boot-step (one-time)

**Priority:** 🟡 (do at your next boot) · **Will-directed 2026-07-11.**

**Why:** You receive WALTER-routed signals as per-recipient handoff files in `AGENTS/AEOLUS/inbox/WALTER/`, but your boot sequence has **no step to drain them** — so routed signals (including ACTION items) silently pile up unread. This is the fleet's standard consume boot-step; SAM / REGINALD / HENRY / LIQUID / BROCK / VIOLET / NEXUS / CORAL / ORACLE already run it. One-time install, then it's automatic and self-closing.

**Install:** add this block to `AGENTS/AEOLUS/CLAUDE.md` in your boot sequence (right after your STATUS / MEMORY / LAST_COMPLETION reads), verbatim — it is the canonical §8.1 template:

```markdown
### WALTER signal intake  (inbox/WALTER delivery lane)

At boot, after STATUS / MEMORY / LAST_COMPLETION:

1. List AGENTS/AEOLUS/inbox/WALTER/*.md not yet in your board_log.tsv.
   (If board_log.tsv does not exist, create it with the v0.2 header:
    timestamp_read<TAB>signal_id<TAB>disposition<TAB>source<TAB>notes)
2. For each: read it, decide disposition (acted/noted/deferred/info-only/skipped),
   append a row to board_log.tsv with source=INBOX_WALTER,
   then `git mv` the file to inbox/WALTER/processed/.
3. Let `acted` items inform this session.
```

(`git mv`, not bash `mv` — bash mv leaves the deletion unstaged.)

**After installing:** drain any handoffs currently sitting in `AGENTS/AEOLUS/inbox/WALTER/` per the block. (You have a small number waiting — all recent; none stale.)

**Provenance:** WALTER `design/BOARD_CONSUMPTION_SPEC.md` §8.1 (canonical). Fleet consume-loop is Phase-2 self-apply — each recipient installs its own step on next spawn.

— WALTER
