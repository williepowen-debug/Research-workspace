# WQ-638 option A: independent review

**Verdict: BLOCK.** This returns to Will; the install authorization does not take effect.

One blocker: `owner_receipt.py prepare --app-only` skips the current-source check. A stale answer can therefore be recorded with no chat confirmation, including on a card PROME has since reclassified as a trade, or a card that has been closed.

The native notification path also remains unproven. The probe reminder did not reach me, and this run could not have delivered it (section 3).

No repair was attempted. Candidate code was not changed.

## 1. Review identity

| Item | Value |
|---|---|
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), as stated by the runtime |
| Runtime | Claude Code 2.1.319, `claude -p --model opus`, entrypoint `sdk-cli` |
| Session | `63863863-8638-4638-8638-638638638638` |
| Candidate | `/tmp/cato-wq638/AGENTS/CATO/prototypes/decisions/mvp`, working tree diff against HEAD `219752ac53a3c094fe37d541e94e6106e3163d06` |
| Reviewed | 2026-11-06, 13:56 to about 14:12 EST |

Frozen hashes, checked with `sha256sum -c` at the start and end of the review (all 12 matched both times):

```text
a37a0222bccf9672c42a28706f1e0f2db8135e2933efde4ca9004521028a1594  app.py
b9ddfc62194bc962aa7207ad1eeefba956db54df72dbe41260da639f22288f83  desk.html
c025e18810081711a331000957e803cea39d06aad9e572d1b12001cd5508987e  options.py
905873ef9b8bf604b65afe807ddf7523f82da456b60545575f8806467a268084  queue_store.py
6d132836f209954ee50e224e578072e6ced3ec1d3503bd67a546605d31f4ae50  owner_receipt.py
3fea5172198f508be5860ac973bcb585d3f9c00ccd1614a4d9d1875dda0c6287  pilot_files.py
0a51089baa5c162385a1e122d9aba2a95522de7368f62425f4c7afa9c284102d  delivery.py
634a528e6ea6570003da5b5f4f99de73f85c77713a8c61c55bad5a03b1e399e9  authorization.py
c5b7ffcf301b515c1ba2cd5f1259031dcee6e480b30642c57df171da80b2b106  notifications.py
6410ecdbe6d28504269b309e8c9b18fdd724a273beb2363933f3a5771c33dedb  notification_hook.py
91bba417469f43ffa25d901d48084455c610f752b555adc0d252fc148c47eda1  notification-hooks.json
8e2fbf3a2ea86660e133789c6d9928ac1ec429aeb8def8b0f4596a279e925363  WQ638.md
```

**Boundaries kept:** I did not boot PROME or any desk, contact owners, spawn helpers, commit, deploy or fetch production, and I did not read the live checkout. All execution ran in disposable copies. I read CATO's author tests only after my first pass, and I read none of CATO's reports.

**Beyond the candidate files, I read these, read-only:**
- this session's transcript;
- the probe's isolated state database;
- the installed Claude Code binary, to explain the probe result.

## 2. Blocker

### B1: app-only recording bypasses the stale-source refusal

**Requirement broken:**
- "Preserve ... current concurrency/stale source refusals."
- `WQ638.md`: "A changed policy, recommendation, brief or queue row invalidates a pending answer."

**Cause:**
- `prepare()` (`owner_receipt.py:35`) with `app_only=True` runs `validate_app_integration` and `assert_latest_app_answer`. Neither calls `check_current_snapshot`.
- The only term check, at `authorization.py:57`, compares the source at the `ruling['commit']` that PROME supplies. It does not compare against the current source.
- `inspect_event` does make the current check, but `prepare` never calls it.
- `read_receipts` then replays the receipt as valid, so the desk would show "Decision recorded".

**Results.** After a published answer on an app-eligible card, each mutation below was published and an otherwise valid authorization ruling was used:

| Change after the answer | Ruling published | `inspect_event` | `prepare --app-only` |
|---|---|---|---|
| Row moved to a new source classified `chat`/`trade` | after the change | refused | **ACCEPTED, receipt `/2`** |
| Row reworded to a held-position trade, with no options source | after the change | refused | **ACCEPTED** |
| Row removed from OPEN | after the change | refused | **ACCEPTED** |
| Source edited in place to `chat`/`trade` | before the change | refused | **ACCEPTED** |
| Recommendation changed from A to B | before the change | refused | **ACCEPTED** |
| Row marked waiting on someone else | before the change | refused | **ACCEPTED** |
| Source edited in place to `chat`/`trade` | after the change | refused | refused, correctly |

The first case is the consequential one: a card reclassified as money-related can be recorded on app authority alone. The same bypass holds in the normal order. `s5.py` wrote and published a `received` receipt, reclassified the card to `chat`/`trade`, and the app-only receipt was still accepted and replayed as `['received', 'integrated']`.

**Why CATO's test missed it:** `test_changed_policy_refuses` covers only an in-place edit published before the ruling, which is the one row above that refuses.

**Related gap:** the `prepare` CLI does not fetch, unlike `pending` and `intake`. It therefore evaluates a possibly stale `origin/master`. This comes from reading the code and was not reproduced.

**Reproduce:**

```bash
cd /tmp/wq638-rev/scripts && PYTHONDONTWRITEBYTECODE=1 python3 s2.py && PYTHONDONTWRITEBYTECODE=1 python3 s5.py
```

**Completion conditions:**
1. App-only `prepare` must fail unless the answer is current against freshly fetched published state, using the same stale check `inspect_event` applies.
2. `read_receipts` replay must stay historical. A later source change must not invalidate a receipt that was valid when written.
3. Regression tests must cover all seven rows above, plus the same cases after a `received` receipt.
4. A candidate change requires new frozen hashes and a new decision from Will on the next review, because this authorization covered ONE read.

## 3. Native notification probe

| Question | Answer |
|---|---|
| Did I personally receive the Decisions system reminder? | **No** |
| Event ID from `/tmp/wq638-native-probe.json` | `237d7a28ebc64211a613a80f7d11701a` |
| Hash from `/tmp/wq638-native-probe.json` | `707827f6e9678d988bdc486453197d397b11847c23f1a4602cfd07af2fc45ab3` |
| Did it arrive during active review? | **No.** No such reminder entered my context at any point, up to the end of this review at about 19:12Z (14:12 EST) |

**What the record shows:**
- The candidate hook ran and exited 2, marked the notice attempted, and recorded a listener row.
- The transcript holds a `hook_non_blocking_error` attachment at `18:56:57.448Z`, before my prompt was enqueued at `.483Z`. It carries `exitCode: 2`.
- That transcript record is not delivery to the model. I found the probe text there only by searching the log. Wrapper exit 2 and the `attempted` row prove emission only.

**Why it did not arrive:**
- In the 2.1.319 binary, a hook runs in the background only when `asyncRewake` is set and the session is interactive or has streaming input. This session used plain `claude -p`, so the hook ran in the foreground and the rewake path never ran.
- I found the rewake wrapper code in the binary, so the feature exists. In this run it was not exercised.

**Conclusion:** this probe is neither positive nor negative evidence for the live alert. It shows that the hook code runs and exits as designed. It does not prove delivery to the model, wake while active, wake while idle, current live PROME registration, or owner intake.

The 1 to 2 minute alert requirement therefore has **no positive real-runtime evidence**. Before install, or as an explicit Will-accepted condition:
1. In an interactive Claude Code session with PROME's settings, confirm a harmless fixture reminder reaches the model while a turn is active.
2. Repeat while the session is idle, and confirm it arrives within 2 minutes.
3. Record the exact text seen. The runtime prefixes it `Stop hook blocking error from command ...:` unless an internal `rewakeMessage` is set, and PROME should not read that as a failure.

### Deployment hazard found through the probe

- **Headless Claude sessions can hang at startup (D1).** If `claude -p` runs without streaming input from `PROME/` with these settings, the watcher runs in the foreground. When no other watcher holds the lock and no notice is pending, the run can block for up to about 12 hours.
- **Evidence level:** this is from the binary logic plus this run's foreground ordering. I did not execute it, because helpers were barred.
- **Exposure:** I found no such caller in `scripts`, `PROME/tools` or the main PROME docs. The only tracked mention is a ruling that declined a `claude -p` timer. Machine-local jobs were not checked.
- **Condition:** verify that none exist, or make the hook exit at once in non-interactive sessions.

## 4. Named residue

Each item below would be acceptable to name on its own. Items 1 and 2 should be fixed in the same return, because they touch stated requirements or repository checks.

| # | Finding | Evidence | Consequence |
|---|---|---|---|
| 1 | Candidate fails an existing test. `intake()` dropped its top-level `requires_chat_confirmation`, so `test_batch.test_intake_receives_once_and_never_rules` raises `KeyError`. Baseline passes. | Reproduced | Repository suite is red. I found no non-test consumer in the paths searched. |
| 2 | The listener status is shown only in the top status line, and it can go stale or disappear. The 60-second `load(false)` never refreshes it, Sync replaces it, and it is dropped when limits or errors are present. | Code read | "Offline/unknown clearly shown" holds only at initial load and in the send message. A stale page can keep saying "listening". |
| 3 | Superseded notices are never acknowledged, so each new PROME session is alerted about them again. Acknowledgement also happens only while the desk is displaying. | Reproduced | Permanent noise. Only 20 notices are shown per pass, so real alerts can be delayed. |
| 4 | Emission is recorded before delivery and tried once per session, with no retry. | Code read; marking and exit reproduced | A lost alert stays lost for that session while the desk says "listening". The desk's "not yet read" status is still truthful. |
| 5 | `/clear`-style turnover: the old watcher holds the lock, so the new session's start fails to arm. Status stays OFFLINE, on a live session, until the next tool or stop event. | Reproduced with synthetic sessions, not real `/clear` | False OFFLINE while idle. |
| 6 | Non-string `mode` or `scope` raises `TypeError`, which the desk does not catch, so `display()` fails for every card. | Reproduced | Fails closed, but one bad source takes down the desk. |
| 7 | `integrated` is accepted with no prior `received` receipt. | Reproduced | Read and ruling receipts are distinct types, but the read step can be skipped. |
| 8 | Rearm gaps: no rearm or `SessionEnd` after `cwd` drifts from `PROME/`; no rearm on payloads over 200 KB; no watcher after 12 idle hours. | Code read | Status falls to UNKNOWN, which is honest, but no alert arrives. |

**Accepted weaknesses, not re-raised:** same-login identity, owner attestations about chat content, PROME's judgment on whether conditions stay in scope, and the fact that classification is declared, not inferred.

## 5. Checks that held

| Area | Result |
|---|---|
| Happy path | App-only receipt `/2` was accepted and replayed at HEAD and `origin/master`. Readback preserved conditions: `WQ-700: A — Do A` plus the condition text. |
| Attestation | Refused edited readback, wrong hash, naive or impossible times, false or non-boolean attestations, wrong scope, and an unpublished ruling. The readback-day rule was read, not tested with a real cross-day case. |
| Chat protection | Trade card refused app-only. A hand-forged receipt `/2` on that card was refused on replay. Protected scopes cannot be `mode: app`. Missing classification and legacy sources stay chat-required. |
| Concurrency | Superseded answers refused. `queue_chain` keeps its existing branch-conflict refusal (`assert_latest_app_answer` calls it); the branch case itself was not exercised. |
| UI | Approve selects the explicit recommended choice, and Disapprove is a `reply` with no selected option. Both route through Review, and only Send publishes. Stale briefs hide the buttons. This is from reading the code; no browser was run. |
| Execution | No automated execution was found in the changed code. |
| Notification | Unpublished answers are refused. The alert carries fixed paths and hashes only. A notice creates no receipt. A `received` receipt clears the matching notice. Cwd filtering holds in the fixture. |
| Legacy | Packet text is unchanged for sources without `confirmation`. Real-history intake output is byte-identical between baseline and candidate. |
| Acceptance gate | `app.py` requires `confirmation_policy: explicit-reversible-internal/1`, and the three new runtime modules are in `BUILD_FILES`. This comes from reading the code; replies should stay disabled until a new acceptance record names the frozen build. |

**Test results in disposable copies with candidate files overlaid:**

| Suite | Tests | Result |
|---|---|---|
| `test_wq638` | 49 | OK |
| `test_desk` | 27 | OK |
| `test_pilot_files` | 31 | OK |
| `test_revision_delivery` | 8 | OK |
| `test_desk_review` | 8 | OK |
| `test_briefs` | 7 | OK |
| `test_batch` | 21 | **1 error** (candidate); OK at baseline |

Not run: browser suites, `test_mvp`, `test_focused`, `test_import_isolation`.

## 6. What returns to Will

1. Fix B1 to its completion conditions.
2. Fix residue items 1 and 2 in the same return, or accept them explicitly.
3. Decide how to close the native alert gap in section 3 and hazard D1.
4. Decide whether the changed candidate gets another independent read. This review's single read is spent, and install is not authorized on these hashes.

Reproduction files are in `/tmp/wq638-rev/scripts`: `s1.py` (happy path), `s2.py` and `s5.py` (B1), `s3.py` (attestation, conflict, chat card, forgery, malformed policy), `s4.py` (notification). Fixtures are in `/tmp/wq638-rev/fx`.
