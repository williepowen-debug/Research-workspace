---
name: Break Multi-File Updates Into Chunks
description: Don't batch 4-5 file updates in a single pass — break into discrete tasks with checkpoints
type: feedback
originSessionId: 3892d800-cf09-4821-98e2-dc6bafc1869e
---
When presented with multiple stale files to update, don't attempt all changes in one pass — break into manageable per-file tasks with checkpoints between.

**Why:** Multi-file rewrites burn context and lose Will's ability to redirect mid-stream. Each file is its own decision surface; batching them removes the natural review points. Will raised this explicitly when RED proposed a 5-file stale-info sweep in one session.

**How to apply:** When the natural unit of work spans 3+ non-trivial files, propose a sequence of chunks, not a single pass. Do one chunk, surface the output, wait for direction before continuing. Exception: pure mechanical updates (header annotations, moves) can be grouped since there's nothing to redirect.
