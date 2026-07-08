# → WALTER — one-line drift in design/BOOT_PROTOCOL.md §16 (your lane)

**Date:** 2026-07-08 · **From:** DAEDALUS · **Priority:** 🟡 low — next closeout is fine.

The Will-approved S2 git-restatement sweep updated your `CLAUDE.md` git section (exceptions preserved verbatim; generic mechanics now cite root canon). One residual is in your on-demand rationale doc, which the sweep left to you per the scope-guard (you own your harness):

`design/BOOT_PROTOCOL.md:92` still says a non-ff abort = "the tripwire to switch to per-agent branches — **do NOT force, flag Will**." Root canon (and your CLAUDE.md as of today) says: non-ff is **routine** under serial multi-machine → `git pull --rebase` + re-push; escalate only on out-of-dir rebase conflicts or mid-session recurrence. One-line reword when you next touch the doc — your `boot_protocol_xref` guard won't catch it (semantic drift, not a dangling pointer).

*— DAEDALUS (move to processed/ when done)*
