# Consolidated locks bundle v4 — assessment, 2026-10-05

Source: Will supplied revised `/mnt/c/Users/willi/Downloads/LOCKS_PATCH_BUNDLE.md`. Inspection and throwaway tests only. No operational changes, configuration changes, server changes or agents launched.

**Disposition: substantial improvement; three concrete corrections remain before installation.** The revised subject hook resolves the original multiline case, retained-comment case and Unicode/NFC counting cases. The installer no longer has contradictory overwriting instructions; advisory retention, actual fingerprint commands, error capture for unshallowing and the boot-consumption hold are incorporated.

## Assertion ledger

| Claim | Exact artifact | Verification | Observed result | Proposed change |
|---|---|---|---|---|
| Subject cap retains prior tested semantics | v4 item 1 commit-msg | Exact bundled hook executable in disposable Git repo; real commits | **VERIFIED:** multiline 121 blocked; exact 100 and short subject/long body allowed; verbatim `#` subject of 102 blocked; decomposed 60-character NFC subject allowed; 60 multibyte characters under C locale allowed, 101 blocked. | These previously disputed cases are resolved. No claim of exhaustive cleanup/editor compatibility. |
| Pipeline warning only delivers advice | v4 item 5 replacement `_handle` branch | Temporary in-memory substitution into existing source; confirmed-hit input; JSON capture; official Claude output contract | **VERIFIED:** exit 0 produces context AND `permissionDecision: "allow"`. **VERIFIED contract defect:** allow skips normal permission prompting subject to documented exceptions, deny/ask rules and other hook precedence. This is not a neutral advisory. | Remove the permissionDecision field entirely. Return hookEventName and additionalContext only; retain exit 0. |
| Native subject hook handles read failures | v4 item 1 redirection/pipeline | Direct executable invocation with nonexistent message file | **VERIFIED defect:** error printed, exit 0. This is a direct error-handling fixture, not evidence Git normally supplies a missing message. Python or pipeline failures also lack explicit handling in the proposed source. | Capture failures explicitly and choose/document the error contract; do not silently count failed input as a valid empty subject. Check dependent tools and successful installation before retiring existing coverage. |
| Installer locations are executable instructions | v4 item 3; actual `scripts/safe-push.sh` | Source inspection / `rg -n 'cd ' scripts/safe-push.sh` | **VERIFIED:** safe-push still has no root cd at the stated insertion point. | Provide a real insertion anchor, or explicitly add root resolution/cd with its error behavior. |
| Unshallow failure is reported accurately | v4 item 4 FLAGS text | Source inspection | **VERIFIED improvement:** rc retained. **INFERRED limitation:** failure alone does not prove the clone remains shallow or that graph divergence is false; timeout/partial success and real divergence are possible. | Recheck shallow state or label ancestry UNVERIFIED rather than asserting a false fork. |

Corrected advisory payload, with no permission decision:

```python
sys.stdout.write(json.dumps({"hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": text}}))
```

Source for permission behavior: [Claude hook decision control](https://code.claude.com/docs/en/hooks#pretooluse-decision-control), checked 2026-10-05. This documentation states allow skips the prompt with exceptions; it does not mean allow overrides every configured denial. Successful stderr remains a debug-log copy, not the human-visible transcript copy claimed by the patch comment.

Test receipt: `/tmp/locks-v4-review-ve0li978/receipt.json`. Test repository and executable hook are within that directory. Advisory branch was executed against the existing recognizer using an in-memory patched source, not installed live. No actual Claude permission prompt experiment performed; the permission finding is established by payload inspection and primary documentation.

Declared residue: editor/comment cleanup false positives remain acknowledged in item 1 and require explicit acceptance before claiming full replacement equivalence. Global hook launch coverage, merging/deduplication and timeout behavior remain installation acceptance work; pasted JSON drops existing PROME validator/clock timeouts and adds hook classes at root, so preserve those settings unless their change is intentionally scoped. Python 3.11 verification remains reviewer-reported, as recorded in the prior response. Branch protection direction remains sensible; current server configuration/plan availability not inspected. Item 2 still tests non-fast-forward force pushes rather than proving every use of a force flag refused. No operator decision requested by this assessment.
