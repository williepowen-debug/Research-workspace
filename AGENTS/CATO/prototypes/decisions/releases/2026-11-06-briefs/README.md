# Live Decisions explanation update — activation handoff

**Applied and verified:** PROME activated this package at `2e4f7cd82d` on November 6 at 12:45 ET. CATO verified publication, build hashes, enabled replies and WQ-632 brief/options. Do not apply the patch again. The steps below are the historical installation record. Ordinary-use benefit remains unmeasured.

Will directed live-app work on November 6 and asked to reduce review/test round trips. Runtime code is in `AGENTS/CATO/prototypes/decisions/mvp/`, used by the existing launcher. No new preview app or service.

CATO prepared `activation.patch` without editing PROME's active queue/acceptance files. It changes exactly:

- `PROME/WILL_QUEUE.md`: add one options-source pointer to the unchanged open WQ-632 terms.
- `PROME/proposals/2026-11-06_wq632-decision-brief.md`: publish PROME's existing explanation/choices, with both hashes rebound to the row including the pointer.
- `PROME/decisions/app-acceptance.json`: current build hashes and the direct-live instruction; historical review and confirmation requirement retained, no new independent verdict asserted.

Only WQ-632 remains OPEN among the supplied examples. WQ-599 and WQ-635 must stay closed. The authored WQ-632 source hash matched the live row before adding its pointer. This is an installation handoff, not a request for another review.

PROME: from Git root, inspect `git apply --stat AGENTS/CATO/prototypes/decisions/releases/2026-11-06-briefs/activation.patch`, then `git apply --check` on the same path. If current inputs match, apply and commit only the three exact paths under root protocol; publish via safe-push. If a source changed, reconcile that change before regenerating the affected hash rather than forcing the patch. `activation-inputs.json` preserves before/after bytes' SHA-256; `build-hashes.json` identifies runtime dependencies. Recheck build hashes before recording enablement; do not repin unrelated newer changes without inspecting them.

After publication, run `python3 -B AGENTS/CATO/prototypes/decisions/mvp/app.py --check --state /tmp/decisions-brief-activation-check` and directly check `app.accepted(Repo(reader.ROOT))` from the app directory. Confirm WQ-632 has its brief and choices and closed examples are absent from current cards. Reopen Decisions; no real answer needs to be submitted for the check.

Author checks: 35 existing queue/revision tests passed; seven focused brief tests passed; twenty native Chrome checks passed across desktop and narrow layouts. The pre-existing revision-delivery fixture discrepancy reproduced under PATH=/usr/bin:/bin and is repaired using a POSIX-shell hook; that witness passes in both environments. The unchanged current claim checker passes its 67-case selftest. `browser-results.json` and screenshots preserve browser evidence; they use disposable WQ-901 mapped from PROME's real WQ-632 wording, never a live answer.

No response export, user database, receipt, underlying decision or trade was changed. Activation is verified as noted above; ordinary-use benefit remains unmeasured.
