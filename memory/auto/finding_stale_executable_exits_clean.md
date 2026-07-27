---
name: finding_stale_executable_exits_clean
description: "An inherited/frozen script with hardcoded constants exits 0 and prints stale values as current — defeating the caller's success check; RUN legacy tooling before judging it, because reading shows intent while running shows what it asserts"
metadata: 
  node_type: memory
  type: finding
  originSessionId: fc3e71c7-82d9-4929-bc1c-b5c4f3b21422
  modified: 2026-07-27T23:22:19.455Z
---

A **frozen/legacy executable with hardcoded state** is more dangerous than a broken one. It exits `rc=0`, prints clean formatted output, and asserts constants that were true months ago as if they were measured today. Nothing anywhere reports an error.

**FALCON, 2026-07-27.** Five HAWK legacy scripts had been designated "frozen, explicitly NOT ported" since a build spec judged they carried *"stale hardcoded data that would look authoritative."* Executing them showed worse than "looks authoritative":

- `war_monitor.py` → `War Day 148` (actual 149), `D 82% / C 12% / B 6%` (live marks `B10/C40/D50`), and **"No significant developments reported"** on a week containing a 400 kbpd refinery strike, a broken four-year truce, and a 13-night campaign pausing.
- `oil_infrastructure.py` → **`Yanbu OPERATIONAL`** — that facility had been attacked two days earlier. Facility states frozen 98 days.
- `sanctions_tracker.py` → hardcoded `BASELINE_METRICS` rendered as live readings, declaring `Stable` without measuring anything.

**Why it bites — three compounding failures:**
1. **`rc=0` defeats the caller.** The parent `boot.py` checked `returncode == 0` to decide success. Every stale script passed. A caller's health check cannot catch a callee that lies confidently.
2. **A "frozen" designation is not enforcement.** The files were documented as do-not-use *and were still executable and still wired into a live `BOOT_SEQUENCE`* — unconditionally, no skip flag, no staleness guard. Documentation doesn't stop execution.
3. **Silence rendered as an all-clear.** "No significant developments" was an empty search result printed as an affirmative negative — the same false-quiet class as a dead monitoring feed (see [[finding_never_received_is_not_doesnt_hold]]).

**How to apply:**
- **Run legacy/inherited tooling before ruling on it.** Reading tells you what a script *intends*; running tells you what it *asserts*. The decisive evidence here was three lines of output, not the source.
- When you inherit or freeze executable tooling, **check whether anything still invokes it** (`grep` the callers), not just whether it's documented as dead.
- If stale tooling must stay runnable, make it **exit non-zero** or print a staleness banner once its constants age past N days — so the caller's existing success check actually fires.
- Constants-in-code age invisibly. Prefer a dated, sourced data file with a staleness clock ([[finding_completion_stamp_skip_reads_as_current]]) over a hardcoded list, and grade it at boot.

Related: [[finding_fail_loud_on_incomplete_data]] (your own summary logic falling through to green on zero data — this is the sibling case where the data is non-zero but *stale*), [[finding_silent_blank_evades_review]], [[finding_read_the_artifacts_own_header_first]].
