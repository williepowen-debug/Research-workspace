# Locks feedback — response to reviewer reply, 2026-10-05

Source: Will's pasted reviewer reply in this session. Assessment only; no operational changes or launches.

**VERIFIED — disputed subject reproduction.** Repeated against the exact original hook in fresh disposable repo `/tmp/locks-repro-nu8whn5z`. Hook executable, effective core.hooksPath points to that hook directory. No bypass flag. Actual argv:

```python
subprocess.run([
    "git", "commit", "--allow-empty", "-m",
    "x" * 60 + "\n" + "y" * 60,
], cwd=repo, check=True)
```

Commit succeeds. `git log -1 --format=%s` yields the first paragraph folded into one subject: 60 x's, a space, 60 y's. The reviewer's single-line/leading-comment tests do not exercise this case. `git stripspace --strip-comments` leaves the two lines separate; selecting only its first line still loses the second half of the subject. Actual hardened text is not supplied, so its behavior is **UNKNOWN**. Always stripping comments also needs reconciliation with `--cleanup=verbatim` and comment configuration. Keep the original review's first-paragraph/NFC acceptance requirement.

**Reviewer-reported Python 3.11 evidence.** Reviewer now reports original parse failure and patched 36/36 selftest success on 3.11.15. Accept this as supplied reviewer verification; distinguish it from PROME's local 3.12.3 36/36. My prior “direct verification outstanding” described the evidence available in my run, not a disproof of theirs. Exact test transcript/artifact remains unavailable in the pasted reply.

**Agreed dispositions.** Repair advisory delivery with exit-0 JSON context. Preserve existing hooksPath and warn rather than overwrite. Repo fingerprint checks are necessary for any user-scope dispatcher. Flag failed unshallowing. Banner should not checkout/merge or repair the routine's virtual environment; the broader BRENT recurrence remains owned by the routine until its other causes are addressed.

**Board consumption.** Boot currently advances; refresh does not. Agree with holding automatic default boot. Flipping the default changes an existing runner contract and must include its callers/receipt semantics; it is not established as the only solution by the reply. Do not apply it incidentally to hook installation.

**GitHub recommendation — correct direction, narrower configuration.** Server-side denial of non-fast-forward updates covers all clients, including client-hook bypass. GitHub branch protection defaults exempt administrators/custom bypass roles unless those restrictions are explicitly applied. A ruleset also requires checking its bypass list. No claim that a repository administrator can never change/disable repository policy is warranted.

Blocking force pushes and requiring linear history are separate policies: linear history rejects merge commits. Existing repository merge examples: `1d36dc511`, `5b7bcb752`, `6efdd1c83` from `git log -3 --merges --format='%h %s'`. Existing merges are not themselves proof a new rule is incompatible, but adding this constraint changes allowed future integrations and needs a separate scope decision. First inspect current protection/plan capability and any bypass permissions; prepare a minimal master non-fast-forward/deletion protection preserving authorized direct fast-forward closeout pushes. No repository setting was inspected or changed in this review.

Source: [GitHub protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches), checked 2026-10-05; [ruleset rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets).

Disposition: retain the agreed repairs; subject hook remains unapproved pending actual revised text and this counterexample. No operator approval requested; this report responds to feedback rather than authorizing implementation.
