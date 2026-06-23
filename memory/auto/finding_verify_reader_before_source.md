---
name: finding_verify_reader_before_source
description: "a confident \"the tool/source is broken\" verdict can actually be a READER bug — verify the reader before declaring the source broken (e.g. a non-deterministic glob over a proliferated multi-file cache picks a stale file)"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 39d64915-90f3-4c17-9d9a-59f23fc2a3d0
---

VIOLET (2026-06-23) declared `fred_fetch.py` "broken" at boot — HY/IG "frozen at 2025-04-01", credit gate "UNCONFIRMED" — and propagated that across STATUS/SCRATCH/NEXUS_BRIEF/CALENDAR + KB-VIO-103, **including the cross-agent NEXUS surface**. The fetcher was fine. The bug was in the VERIFICATION: `glob.glob(code+"_*.csv")[0]` non-deterministically grabbed a stale older-dated cache file out of 8 per series; the freshly-written file held current data (CCC 9.47, gate actually LIFTED).

**Why:** date-stamped cache filenames (`{id}_{start}_{end}.csv` with end=today) proliferate one file per day, so any ad-hoc "read the latest" glob can pick the wrong one. A confident-wrong "broken" diagnosis is worse than "unknown" — it propagates into shared state and gets acted on before anyone re-checks.

**How to apply:** when a fetch/tool *looks* broken, first verify the READER before declaring the SOURCE broken or writing "broken/unconfirmed" into shared state — read the EXACT canonical file (not a glob), date-SORT before trusting `tail`/`[0]`, and re-run the tool's own success path. Structurally, prefer one canonical file per series (overwrite/merge-in-place) + a `latest_value()` reader over date-stamped proliferation; the proliferation is the root cause, the glob is just where it surfaced. Same family as [[feedback_suspect_fresh_pull_over_curated_record]] (suspect the pull) and [[finding_number_carries_threshold_unit_source]] (a number carries its provenance) — here the provenance failure lives in the reader, not the source. Fleet agents with date-stamped FRED/data caches (BROCK, LIQUID) are exposed to the same trap.
