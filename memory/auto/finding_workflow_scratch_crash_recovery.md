---
name: finding_workflow_scratch_crash_recovery
description: a crashed OR RATE-LIMITED sub-agent leaves its outputs recoverable in /tmp scratch — salvage before re-running AND before accepting any declared gap; the salvage can reverse the parent's conclusion
symptoms: "sub-agent died on session limit", "agent returned nothing", "leg never reported", "You've hit your session limit", "idleReason: failed", "declared the gap and shipped", "teammate produced no result"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 09e30781-0aec-4b05-a735-6920f23899ff
---

When a `/deep-research` or Workflow session is booted/crashes mid-run, the sub-agent (task) outputs persist on disk and are recoverable — don't assume the work is lost or re-run the whole fan-out.

Location: `/tmp/claude-1000/<munged-cwd>/<session-uuid>/tasks/<id>.output` (munged-cwd = the agent's working dir with `/`→`-`). These are the raw data-gathering outputs (fetched source text, grep dumps, filing extracts) — i.e. the EXPENSIVE source-discovery+fetch step. 0-byte `.output` files = sub-agents killed before producing (often the synthesis stage). Strip nulls with `tr -d '\0'` for readability.

**Why:** source-gathering is ~70% of a deep-research run's cost; the synthesis is cheap to redo. Salvaging the scratch turns a full re-run into "synthesize + fill the few gaps."

**How to apply:** on a "we got booted mid-research" report — BEFORE re-running — `find /tmp/claude-1000 -path '*<AGENT>*' -name '*.output' -mtime -1`, copy survivors into the agent's `output/_recovered_<date>_<topic>/`, harvest the evidence, then only re-run gap-fill searches + synthesis. /tmp can be swept, so preserve into the repo first. Relates to [[finding_closeout_as_writeback_tail]] (save artifacts incrementally) and [[finding_workflow_concurrency_529]].

---

## EXTENSION 2026-09-10 (DEWEY, REQ-002) — two things the original misses, and the second is the important one

**(1) A plain `Agent` TEAMMATE that dies leaves its work somewhere ELSE.** The path above (`.../<session-uuid>/tasks/<id>.output`) is where **Workflow** sub-agent output lands. A named teammate spawned via the `Agent` tool gets **its own session scratchpad**:

```
/tmp/claude-1000/<munged-cwd>/<THE SUB-AGENT'S OWN session-uuid>/scratchpad/
```

Not your session's uuid — **a sibling directory**. So find by directory age, not by your own session id:
```bash
find /tmp/claude-1000 -type f -newermt "<today> HH:MM" \( -name "*.md" -o -name "*.txt" \) | grep -v "<YOUR-session-uuid>"
```
Live instance: 385 files, including a hand-built notes file the agent had clearly written *for* the parent and never got to send.

**(2) ⚠️ THE REASON TO SALVAGE IS NOT COST. IT IS CORRECTNESS.** The original framing here is economic — "source-gathering is ~70% of the cost, salvaging turns a re-run into a synthesis." **True, and it undersells the case.** On 2026-09-10 the salvaged work **REVERSED the parent's already-drafted conclusion**: DEWEY had written that Lucent's vendor-financing exposure peaked at FY2000 and concluded *"the lead time was zero — revenue and provisions broke in the same fiscal year."* The salvaged series showed commitments peaked **1999-12-31 at $9.8B**, ~12 months earlier, making the real finding *"the commitment level is the only instrument that ever led."* **The report would have shipped the opposite of its own headline finding.**

⇒ **Salvage before accepting any declared gap, not merely before re-running.** A gap you are about to write down as "not reached" is exactly the gap the dead agent may have filled.

**(3) A rate limit defeats the return-partial guardrail.** `[[finding_workflow_rate_limit_resume_recovery]]` step 2 recommends prompting sub-agents to "return what you have rather than dying mid-work." **That guardrail cannot fire against a session limit** — the agent has no budget left to transmit with. It still helps against budget exhaustion; it does **nothing** here. The only recovery is the scratch sweep.

**(4) Salvaged work is still SUB-AGENT work — verify before promoting it.** DEWEY re-verified **5 of 5** load-bearing salvaged figures at the primaries before use (all matched), and shipped the one block it could not re-verify **tagged as unverified in place** rather than blended into the verified material. Same session had just corrected a false `[VERIFIED]` claim of its own (`COR-20260908-01`), which is why tagging-by-verifier rather than by convenience was the minimum bar. `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]`

*(n=3: 2026-07-16 three agents ran 69 min past parent exit with legs declared "never reported"; 2026-07-10 rate-limit kill; 2026-09-10 rate-limit kill whose salvage reversed the parent's conclusion.)*
