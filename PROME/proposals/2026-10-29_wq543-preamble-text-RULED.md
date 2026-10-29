# WQ-543 — BRENT routine boot preamble: four text clarifications — RULED

**Ruled:** 2026-10-29 14:34 ET, Will in the PROME window, verbatim *"approve"*, answering the ⚖️ WQ-543 block whose rec was APPROVE (a)(b)(c), DEFER (d). Registered 14:3x ET the same sitting from the independent reader's ledger (`PROME/reports/2026-10-29_L526-AC-reader.md`, Opus, 0 ❌ / 4 ⚠️). Authority context: WQ-510 A approved the preamble "as drafted" (02156ded7), so its text is Will-gated; this ruling amends that text and nothing else.

## The ruling
- **(a) APPROVED** — step 2: "If HEAD is not on master (detached or another branch): `git checkout master`" replaces "If HEAD is detached". Closes reader #12 (a harness session branch would otherwise be fast-forwarded and committed off master under a healthy receipt).
- **(b) APPROVED** — step 1: "If the fetch fails, STOP and name the error"; the receipt line gains the post-merge HEAD short sha. Closes reader #13 (a failed fetch could print a false quiet path against stale refs).
- **(c) APPROVED** — "never rebase" → "the preamble never forces, resets or rebases". Closes reader #16 (the protocol's push-time `git pull --rebase` is not forbidden by the preamble).
- **(d) DEFERRED** — on `venv=present`, re-running the pinned pip install. Moot while containers arrive without a venv (reader #14, #11). Reopens if a container ever arrives with a venv.

## Execution
BRENT edits its draft (`AGENTS/BRENT/setups/2026-10-23_L526_routine-boot-preamble-DRAFT.md`) and re-installs the block in all four saved prompts through `RemoteTrigger update`, paired with its 11/1 DST cron re-set: one install, one validation run, saved images + sha256 in a new audit directory, receipt packet to `PROME/inbox/`. The receipt format change in (b) is one appended field; the spec's AC4 string is restated by DAEDALUS if finding #11 (frozen container snapshot) holds after Friday's 20:15Z run. PROME records at DOCKET L526 (re-dated 10/31 for the Friday observation).

## Not moved
No money, no account, no external send, no authority change. AC2 and AC4 remain UNOBSERVED; this ruling does not close L526.
