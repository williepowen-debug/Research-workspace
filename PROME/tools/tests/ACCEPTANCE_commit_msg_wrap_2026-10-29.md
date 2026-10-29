# ACCEPTANCE — `scripts/githooks/commit-msg` wraps an over-long subject instead of rejecting it
**Written 2026-10-29 13:0x ET BEFORE the edit** (WQ-229). Will 13:01 ET: *"How do we fix this? Can you fix this?"* on PROME's friction list item 6 (the hook bounced four PROME commits today for 1–3 characters each; every bounce is a round trip with no safety value). Root Git Protocol 4d (WQ-171 ①, Will 2026-09-03) is unchanged: the SUBJECT stays ≤100 characters; receipts go in the body. Process change 3 of 5 this session. Owner: PROME (hook installed 2a72c60bc).

## The defect, in its own terms
The hook enforces a formatting rule by refusing the commit, so the cost of a 102-character subject is a failed commit, a re-edit and a retry — and in an `&&` chain, every command after it silently not running (two of today's bounces broke the chain that wrote the next message file). The property wanted: **the rule is satisfied by the hook, not by the author's retry.**

## Acceptance conditions
1. A subject ≤100 characters passes unchanged (byte-identical message).
2. A subject >100 characters is split at the last space at or before column 100; the head becomes the subject, the tail becomes the FIRST body paragraph, separated from the subject by one blank line; any existing body follows after another blank line, unchanged.
3. The hook prints one notice to stderr naming the split and exits 0; the commit proceeds.
4. A subject with no space before column 100 (one 120-character token) is NOT silently truncated: the hook refuses as before (rc 1) — the only remaining refusal.
5. Comment lines, `-F` files and `-m` strings behave the same (the existing stripspace path is kept); the trailer `Co-Authored-By:` stays last.
6. The rewritten file is what Git commits (the hook writes back to `$1`).

## Neighbours
ordinary: short subject ⇒ untouched (1) · overlap: subject exactly 100 ⇒ untouched; 101 with a space at 100 ⇒ split there (2) · wrong owner: N/A — the hook reads only its own message file · missing information: empty message ⇒ Git's own refusal, hook never reached; no-space subject ⇒ (4) · concurrent: N/A — per-commit file, no shared state.

## Completion
IMPLEMENTED · TESTED · INDEPENDENTLY VERIFIED · STILL UNRESOLVED — below after the edit.

## Completion note — 2026-10-29 13:0x ET
- **IMPLEMENTED:** `scripts/githooks/commit-msg` rewrites the message file: split at the last space at or before column 100, tail → first body paragraph, existing body and trailer follow unchanged; no-space subject still refused.
- **TESTED:** five cases run against the hook script directly (scratchpad `hooktest/`): short unchanged · exactly 100 unchanged · 165-char subject wrapped at 97 with body and trailer kept · 120-char no-space token refused rc 1 · 101 chars with a space at 98 split there. The committing commit of this file carries a deliberately over-long subject so condition 6 (Git commits the rewritten file) is proven by the record itself: see `git log -1 --format=%B -- scripts/githooks/commit-msg`.
- **INDEPENDENTLY VERIFIED:** not claimed — small self-contained fix (WQ-229: no gate, no shared contract, no recurrence).
- **STILL UNRESOLVED:** none.
