---
name: finding_verify_runtime_context_before_tool_broken
description: Before calling a tool invocation broken, reproduce from the ACTUAL runtime cwd/context — a failure from the wrong directory isn't a bug
metadata:
  type: finding
---
2026-07-01: I declared a "fleet-wide bug" — that the 6 agents' `python3 scripts/ledger_staleness.py <NAME>` boot call (a repo-root-relative path) would fail because root CLAUDE.md launches agents with `cd AGENTS/<NAME> && claude`. I "confirmed" it by running the command from `AGENTS/HAWK/` (exit 2, file-not-found) and filed the claim into 5 docs before checking the premise.

It was a **false alarm.** The fleet runs *tools* from **repo root** by convention (REGINALD's boot literally says "from workspace root"; LIQUID's canonical `AGENTS/<NAME>/scripts/boot.py`, the `FORGE/tools/...` calls, and `scripts/safe-push.sh` are ALL repo-root-relative and demonstrably work). The `cd AGENTS/<NAME>` line governs where **CLAUDE.md auto-loads from**, NOT the cwd tools execute in. From the real runtime cwd (repo root) the check works fine (exit 0) — and BRENT ran it that same session and froze stale ledgers, live proof.

**Why:** a command's success depends on its runtime context (cwd, env, PATH, venv). A test that fails from a context the tool is never actually run in proves nothing — and a confidently-filed false "bug" burns trust and pollutes multiple docs (I had to retract it across 5).

**How to apply:** before calling any relative-path / tool invocation broken, establish the ACTUAL context it runs in (here: what cwd do agents execute tools from?) and reproduce from THERE. Cross-check sibling invocations that demonstrably work — if `boot.py` / `safe-push.sh` use the same path convention and function, your target almost certainly does too. Environmental cousin of [[finding_verify_reader_before_source]] and [[finding_injection_claim_is_openclaw_vestige]]. Corollary: I only caught it because Will pushed ("what is it?") after I self-asserted — don't self-verify a load-bearing claim; reproduce it, ideally with an independent check. (Same session, the applied cross-agent edits were independently adversarially audited rather than self-verified — that pass caught 2 real wording errors my self-read missed.)
