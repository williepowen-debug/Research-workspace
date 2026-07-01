---
name: finding_verify_runtime_context_before_tool_broken
description: "Reproduce a suspected-broken (or suspected-fine) tool invocation from the ACTUAL launch cwd, both ways — \"convention\" claims about runtime context are hypotheses, not evidence"
metadata: 
  node_type: memory
  type: finding
  originSessionId: 1024a372-529b-4a79-a25a-8fceaa7c7976
---

2026-07-01: I declared a "fleet-wide bug" — that the 6 agents' `python3 scripts/ledger_staleness.py <NAME>` boot call (a repo-root-relative path) would fail because root CLAUDE.md launches agents with `cd AGENTS/<NAME> && claude`. I "confirmed" it by running the command from `AGENTS/HAWK/` (exit 2, file-not-found) and filed the claim into 5 docs before checking the premise. I then retracted it as a false alarm.

**The retraction itself proved wrong the same day (7/1 PM).** I had cleared the claim on convention-inference ("the fleet runs tools from repo root — REGINALD's boot says 'from workspace root'; boot.py/safe-push work") and verified only from repo root. That afternoon BRENT's boot failed exactly the predicted way in production (rc=2 from its own-dir launch cwd) and mis-diagnosed it as "script missing repo-wide" (outbox signal). An empirical sweep then showed there IS no uniform convention: 6 agents' ledger-staleness lines + SAM/BROCK's market-data lines assume root cwd, while ORACLE's boot lines assume own-dir cwd — everything works only when the session happens to sit in the right directory. Will-approved fix: cwd-proof `"$(git rev-parse --show-toplevel)"` invocations; the script itself self-locates (`os.path.abspath(__file__)`) and needed no change.

**Why:** a command's success depends on its runtime context, and BOTH directions of the check matter. A failure from a cwd the tool never runs in proves nothing — AND a pass from a cwd you merely *assume* is the runtime one proves nothing either. "By convention" is a hypothesis about runtime context, not evidence; the launch mechanics (`cd AGENTS/<NAME> && claude` sets the initial shell cwd to the agent's dir) are the ground truth to test against.

**How to apply:** before ruling a relative-path invocation broken OR fine, establish the ACTUAL context empirically — what cwd does a fresh session start in? does anything cd before this step? — and reproduce from THERE, testing both the failing and the passing case. Don't accept "sibling invocations work" as proof: siblings may run at a different point in the sequence where cwd differs, and a fleet can mix path idioms. When the fix is cheap (cwd-proof `$(git rev-parse --show-toplevel)` or an explicit cd), prefer removing the cwd-sensitivity over litigating the convention. Environmental cousin of [[finding_verify_reader_before_source]] and [[finding_injection_claim_is_openclaw_vestige]]; pairs with [[finding_verify_recommended_fix_not_just_finding]].

Two beats of the same discipline failure: the original false "bug" rode until Will pushed ("what is it?"), and the false *retraction* rode until production evidence (BRENT's signal) landed. The check that clears a claim needs the same rigor as the check that files it — in both cases the miss was substituting inference (sibling behavior, stated convention) for a reproduction in the real context.
