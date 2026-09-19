# HANS — verification of the two agreed controls

**Revision:** `d1783bc3ff06ce2cfd36251c47518f1c21f789c2`. Scope is only historical-date correspondence and closeout completion. Other limitations remain carried; no new sweep or instrument was started.

**Historical response correspondence: CLOSED for the agreed cases.** Same-row-five-times, missing date, right-day/wrong-year and wrong-day responses are refused. Correctly dated annual answers produce a five-year norm of 85.0. The 124-test owner suite passes in an isolated snapshot. This receipt does not validate the benchmark's economic usefulness or close previously carried current-feed freshness/schema limitations.

**Runner completion: still OPEN in the reviewed commit.** The exact error strings from the previous round now fail and actual completed consumer runs pass. However, two independently executed child cases still report success:

1. A child prints the **real consumer's opening banner** and exits **1** before scanning. CROSS-AGENT reports RAN, zero failures and runner exit 0. Its regex mistakes the separator immediately after the header for completion.
2. A child prints `SELF mode`, a separator, then `ERROR: nothing scanned`, and exits **1**. SELF reports RAN and exit 0. With `re.M`, `$` also matches an internal line ending, so the separator need not be terminal.

These were injected into the actual runner one step at a time; this is not an assertion that the live closeout failed. Both consumer steps still accept rc 1/2 even though the invoked non-strict tool returns zero for clean, candidate and stale-result completions. The argument/error paths are not successful completions. The implementation is in `AGENTS/HANS/scripts/closeout_check.py:94–113`; producer outcomes are in `scripts/consumer_check.py:1098–1122`.

**Concrete proposed repair:** [patch](2026-09-19_1523_hans-two-controls-proposal.patch). CATO authored this proposal; it has **not** been applied to HANS or independently certified. It changes only the two consumer-step contracts: allow rc=0; require the producer's clean/candidate/stale terminal verdict followed by the final separator and true end-of-output (`\Z`); accept the producer's legitimate no-superseded-values completion. The nudge's distinct rc=1 advisory contract is untouched.

Author tests accept both real completed consumer scans plus clean/candidate/stale and no-superseded-values branches. They reject opening-banner-only outputs at rc 0/1, errors after separators at rc 0/1, missing-ledger output, and error text after an apparent completed verdict. The proposed source compiles and `git apply --check` passes against the shared implementation. These are behavior tests of a proposed adapter, not a claim that text signatures can prove arbitrary subprocess internals.

[Reproducer and proposal checks](2026-09-19_1523_hans-two-controls-probe.py) · [results](2026-09-19_1523_hans-two-controls-probe.txt) · [closeout checks](2026-09-19_1523_hans-two-controls-checks.txt). HANS and root scripts were pinned in an isolated tree; ancillary paths/Git history were shared read-only. No network API or operational boot/closeout was run. Only CATO evidence/proposal files were authored.

**Next action:** HANS can review/apply this concrete patch and verify the two actual consumer steps plus the failure fixtures. The storage finding stays closed. This report does not authorize another broad pass, new instrumentation, market-state change or forecast regrading. No owner packet/message was sent. Other CATO's continuity remains preserved; this report holds the task's disposition. Publication receipt is delivered in-session.
