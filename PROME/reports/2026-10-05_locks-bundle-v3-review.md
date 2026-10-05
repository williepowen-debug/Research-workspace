# Revised locks bundle — v3 review, 2026-10-05

Source: `/mnt/c/Users/willi/Downloads/LOCKS_PATCH_BUNDLE.md`, reread after Will supplied revised version. Review only; no operational changes and no agents spawned. This supplements the initial review and reviewer-reply assessment; it is not implementation approval.

**Disposition: improved, still not paste-ready.** The exact updated commit-msg hook closes the disputed multiline-subject reproduction. However, the document retains instructions that contradict agreed repairs, and the new hook retains cleanup/character-count defects.

## Assertion ledger

| Claim | Exact artifact | Verification | Observed result | Proposed change |
|---|---|---|---|---|
| v3 measures the entire first paragraph | Bundle item 1 v3 commit-msg | Exact hook executable in throwaway repo; real Git commit with 60 x's + newline + 60 y's | **VERIFIED:** blocked as 121 characters. Exact-100, short subject with long body, and short multiline paragraph allowed. | Retain paragraph folding; disputed reproduction is resolved. |
| v3 measures the subject Git actually records after cleanup | Same hook, unconditional `git stripspace --strip-comments` | Real Git commit with `--cleanup=verbatim` and `#` followed by 101 x's | **VERIFIED defect:** commit succeeds and records the 102-character subject; hook stripped that line. | Account for actual cleanup/comment behavior; do not unconditionally discard `#` lines while claiming equivalence to recorded `%s`. |
| v3 preserves the existing character-count contract | Same hook `wc -m`; existing `PROME/tools/hooks/commit_subject_guard.py` NFC contract | Real Git commits using 60 decomposed e-acute characters, and 60 precomposed e-acute characters under LC_ALL=C | **VERIFIED defect:** both blocked as 120. First is 60 after NFC normalization; second has 60 Unicode characters but is counted as 120 in C locale. | Use deterministic Unicode/NFC measurement matching the established contract. |
| v3 handles missing information visibly | Same hook input redirection/pipeline | Direct hook call with nonexistent message path | **VERIFIED:** shell error on stderr, hook exits 0. No real Git missing-message case claimed. | Explicitly define and test error handling; avoid treating a failed read as an empty valid subject. |
| Corrected installer preserves an existing hooksPath | Item 1 corrected install block versus later old install block | Full document read | **VERIFIED contradiction:** new block warns/preserves; later paste-ready block still unconditionally overwrites a different hooksPath. The stale safe-push root-cd insertion locator remains. | Remove the superseded block; provide one authoritative installation instruction against the actual script. |
| Agreed advisory repair is incorporated | Item 4 settings/archive instructions | Full document read versus reviewer's reply | **VERIFIED contradiction:** still directs deletion and archival of pipeline advisory; no exit-0 JSON additionalContext repair supplied. | Replace stale deletion instructions with the agreed advisory-delivery repair and narrow settings changes. |
| Failed unshallowing is flagged | Item 2 replacement code | Source inspection | **VERIFIED defect:** unshallow return code still discarded; ordinary fetch status still replaces it. | Incorporate the accepted error capture/recheck before claiming this repair supplied. |
| Global hook commands are repository-scoped | Item 5 heading versus item 4 actual JSON | Source inspection | **VERIFIED gap:** fingerprint requirement added in prose, but pasted commands contain no fingerprint checks. | Supply actual repo-scoped command/dispatcher text. |
| GitHub protection proposal respects merge workflow | Item 7 | Document read; prior official GitHub documentation check | **VERIFIED text improvement:** includes administrator/no-bypass restrictions and leaves linear-history requirement off. Existing server configuration and plan availability remain **UNKNOWN**. Administrators can still change policy; protection is against prohibited pushes while enforced, not immutable administration. | Retain the direction; inspect current rules before proposing an exact server change. |

Test artifacts: `/tmp/locks-v3-review-bw1blcdr/receipt.json` and the fixture's executable `hooks/commit-msg`. All commits were confined to that disposable repo; no live hooks/configuration/board state modified.

Python compatibility recommendation remains accepted on supplied reviewer-reported 3.11.15 verification plus PROME's prior local 3.12.3 selftests. Default boot consumption remains on hold; no incidental runner-default change proposed here.

Next useful step is a consolidated corrected patch reflecting the agreed dispositions, not another explanatory review of the same stale blocks. No operator decision requested in this assessment.
