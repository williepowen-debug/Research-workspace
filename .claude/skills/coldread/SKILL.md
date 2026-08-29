---
name: coldread
description: Blind cold-read of one PROME-owned surface after a re-base or restructure, before commit — spawns the `coldreader` agent, scores it, applies the flags, re-runs until zero ❌. Use for "cold read this", "cold reader pass", after any HEARTBEAT re-base, root CLAUDE.md edit, SCRATCH rewrite, or a proposal going to Will/RAV.
user-invocable: true
---

# /coldread — blind cold-reader pass (PROME)

The reader knows nothing by design. Its value is that ignorance. Do NOT brief it on the system.

1. **Spawn `coldreader`** with exactly: the artifact path, and (optionally) the list of claims you expect it to carry (numbered). Nothing else. `isolation` not needed — it is read-only.
2. **Score** the report: `SCORE: ok/N · ⚠️ n · ❌ n`. A ❌ = internal contradiction or dead pointer — must be fixed. A ⚠️ = a stranger cannot tell — fix if the fix is one line (gloss the term, add the unit/basis/date, replace "row N" with "WQ row N"), otherwise judge.
3. **Apply fixes at the source** (owner surface first, then the view), never by annotating the reader's flag into the file.
4. **Re-run** the reader on the fixed file if there was any ❌. Stop at ❌ = 0. Record `<n>/<N>` in the commit message and the SCRATCH executed-list.
5. Two readers in one day is normal (WQ-120 and WQ-121 both went 16/16 on pass 2). A reader that scores 100% on pass 1 of a large re-base is suspicious — check it actually enumerated the claims.
