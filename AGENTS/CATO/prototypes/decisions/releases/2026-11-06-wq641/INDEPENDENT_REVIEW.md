# WQ-641 independent follow-up review

**Verdict: ACCEPT WITH NAMED RESIDUE, scoped to the authorized fallback only.**

- B1 is closed, and items 1, 2, 5, 6 and 7 are closed.
- No new blocker was found, so the fallback can install if the conditions in section 2 are met.
- App-only stays OFF. This read gives no evidence of live PROME alerts and makes no live wake claim.

## 1. Review identity

| Item | Value |
|---|---|
| Reviewer | Claude Opus 5.5 (`claude-opus-5-5`), as stated by the runtime |
| Runtime | Same headless session as the prior review, Claude Code 2.1.319 |
| Session | `63863863-8638-4638-8638-638638638638` |
| Candidate | `/tmp/cato-wq638/AGENTS/CATO/prototypes/decisions/mvp`, base HEAD `219752ac53a3c094fe37d541e94e6106e3163d06` |
| Reviewed | 2026-11-06, finishing about 15:13 EST |

All 14 entries in `/tmp/wq641-candidate-sha256.txt` matched at the start and end:

```text
3e3f64d0acf64e77e76c4fdd67c0200cea5d5750f5380ce687ec339b73ff6f48  README.md
279e449a06a1ca098121c7721c0def46b732802186096529714cf62aea1d1410  WQ638.md
7b83f27c26e6dbb4184900c77896130e8e6fb9f86e95c7bb4ef315c431997255  app.py
904b774adc1390f350150ab2f2f16e6f37600e1dd35998de9da99601357d5645  authorization.py
25b64b9d04a8aef928b2ba2b639e87245bda7a7141048cbdb9fc4ec8fa71bcad  desk.html
ef895e59ffdc764ddea2f9becd1a45b71c4fe10de7945e2fa082f56724efb4d1  notification_hook.py
907cbae198854df6c6cdc102e812821a5b222ac161a63c6690086d5223014b52  notifications.py
5c1444893735a5a5fa19f0136a9963bdb122148ad1cb271fd02d80ef88c96fe7  owner_receipt.py
09f17926a62cb557cbb5dbac41cd1e30b1cbf9bc8eaa74ba67143a1be6c5c4d2  pilot_files.py
49df10d7e11f37b8d647d8f8806d82a6ce4ad3f0014b0d4a0105772a19d6e271  test_batch.py
8caa321ab87b1f6b9b2265d5015e980703e946be14f082b4d9d08a4e8fa31392  test_desk.py
7ce66c1efcde528dad74b1e860df9487ea7a7d017eecbd2df0bf81466a99c6d8  test_desk_review.py
1518015b5ac77f44415ad952ebc59bf26ec0ad9b9d1f6fb8738e3536a985b4c6  test_wq638.py
d199fd11b23d635c1ab09d01f850a4d4c47bea81549f939358495aac36205145  test_wq641.py
```

`delivery.py`, `queue_store.py` and `options.py` still match the prior freeze.

**Note for the acceptance record:** the manifest omits unchanged build files such as `delivery.py` and `queue_store.py`. The acceptance `build_hashes` must come from the full `build_hashes()` output, not from this manifest.

**Boundaries kept:** I did not spawn anything, boot a desk, contact owners, fetch production, change the candidate, or make any repair. Everything I wrote was in disposable `/tmp` paths.

**Coverage limits:**
- The delta patch includes `test_wq641.py`, so I saw part of the author tests while reading the patch, before my own pass. My counterexamples came from the prior findings and the changed code, but this was not a fully blind first pass.
- The read took longer than the six-minute aim.
- No browser was run. UI and status findings come from reading `desk.html`, plus the desk data returned by `Desk.display()`.
- Real `claude` sessions were not used for hooks. Takeover ran with real processes, a synthetic parent and `interactive=True`. `/clear` itself was not exercised.
- The `"mode": "app"` search (residue R1) covered the candidate's HEAD, not freshly fetched production.

## 2. Install conditions for the fallback

1. Publish `app-acceptance.json` with `app_only_enabled: false`, `matching_chat_confirmation: true`, `confirmation_policy: explicit-reversible-internal/1`, the full frozen `build_hashes()` and the published review reference.
2. Do not install `notification-hooks.json`.
3. Do not author `mode: app` sources while the fallback is active, unless the packet wording in R1 is corrected first. If one does appear, PROME must follow intake's `requires_chat_confirmation: true`, not the packet.
4. Expect any answers saved under the old build to go stale on install, because snapshots bind the `desk.html` hash. They would need to be answered again.

## 3. Prior findings

### B1: closed

This rerun used received receipts that were published first and app-only acceptance enabled. The control case was accepted, which proves the refusals below come from the stale-source guard and not from the new earlier guards.

| Change after the answer | Ruling published | App-only `prepare` | Result |
|---|---|---|---|
| None (control) | n/a | **Accepted, receipt `/2`** | Correct |
| Row moved to a new `chat`/`trade` source | after | Refused: terms changed | Closed |
| Row reworded to a held-position trade | after | Refused: terms changed | Closed |
| Row removed from OPEN | after | Refused: queue item unavailable | Closed |
| Source reclassified in place | before | Refused: option terms changed | Closed |
| Source reclassified in place | after | Refused: option terms changed | Closed |
| Recommendation changed | before | Refused: terms changed | Closed |
| Row marked waiting | before | Refused: options no longer bind the row | Closed |
| New: prose-only change to the source file | before | Refused: option terms changed | Closed |

The added `fetch` is exercised by `test_prepare_refreshes_remote_before_current_check`. Historical replay independence is covered by `test_historical_valid_receipt_survives_later_change_and_fallback`. Both passed. I did not write separate counterexamples for these two.

### Named items

| Item | Status | Evidence |
|---|---|---|
| 1. `test_batch` regression | Closed | 21 of 21 pass. The key moved to per-item output, and the test now expects that. |
| 2. Status display | Closed in code | A dedicated status line is written by `load`, including `load(false)` and Sync. Focused editing uses `refreshConnection`. A failed load shows unknown. Not run in a browser. |
| 5. `/clear`-style turnover | Closed in fixture | Reproduced with real processes (details below). |
| 6. Malformed source | Closed | All 8 malformed forms stayed on one card. Save and deliver were refused on the bad card, and the other card stayed answerable. |
| 7. Read before ruling | Closed | Both modes refuse before `received`, and refuse while `received` is unpublished. |

**Lease results for item 5:**
- `SessionEnd` then immediate `SessionStart` ended `listening` under the new session.
- During takeover, status showed `unknown` with beat 0 until the new watcher held the lock.
- The old watcher exited, and the old session's `SessionEnd` and a stale-identity heartbeat changed nothing.
- `PostToolUse` from a foreign session could not steal the lease, and a same-session rearm made no duplicate.

### Hazard D1 (dormant under fallback): closed in fixture

`interactive_parent` returned False for `-p`, `--print`, `--print=x`, the combined flag `-dp`, and non-terminal stdin, including the first three with terminal stdin. It returned True for a plain terminal, `--resume`, and `--model ... -- prompt`.

It also returned False for a prompt beginning `-p` after `--`. That wrongly refuses a watcher, but fails safe. It would matter only if hooks are ever enabled.

## 4. New controls

**Global mode:** each of these left app-only off in the fixture, and `Desk.display()`, intake and `prepare` all stayed chat-required:
- `app_only_enabled` absent, `false`, `"true"` or `1`;
- `app_only_since` missing, null, naive, garbage or in the future;
- activation after the answer, so older answers cannot be upgraded.

A dirty local acceptance file and a build-hash mismatch also turned it off.

**Fallback end to end on an app-eligible card:**
- `accepted()` passed, and the desk was deliverable with `requires_confirmation: true`.
- Status read `unknown`, which is honest with no hooks.
- App-only and no-confirmation rulings were refused.
- A chat ruling produced receipt `/1`, replayed as `received`, `integrated`, and the desk showed History.

**Receipt `/2` replay:** a `/2` root was refused, as were `/2` after `needs_clarification` and after `rejected_stale`. `/2` after `received` was accepted. A legacy `/1` integrated root was retained.

**Reply and receipt corruption:**

| Corruption | Result |
|---|---|
| Non-JSON reply | Desk-wide refusal |
| Reply with no record | Desk-wide refusal |
| Orphan receipt | Desk-wide refusal |
| Corrupt receipt on a real answer | Desk-wide refusal |
| Reply that is a list, or has null display or integer `wq_id` | `display()` raises, so the desk fails closed |
| Reply naming a WQ, with a bad hash | Isolated to that card |

The raise comes from an uncaught `TypeError`. It refuses safely but gives no clean message (R3).

## 5. Named residue

| # | Finding | Evidence | Consequence |
|---|---|---|---|
| R1 | Under fallback, the packet for a `mode: app` card still says "App-only eligible". `delivery.py` was not changed and packet text cannot follow the global mode. | Reproduced | Contradicts "chat on every answer" in PROME's inbox. `prepare` and intake still enforce chat, and I found no `"mode": "app"` source in the candidate's proposals or queue. Covered by install condition 3. |
| R2 | A hand-written `/2` receipt with valid attestation replays as integrated under fallback, and the desk shows it as recorded. Replay ignores enablement by design. | Reproduced | Needs a deliberate bypass of `prepare` under the same login. It falls inside the accepted identity weakness, but "OFF" is enforced for new preparation only. |
| R3 | Three reply-corruption shapes raise an uncaught `TypeError` instead of a clean refusal. | Reproduced | Fails closed, but the desk gives no useful message. |
| R4 | "Confirm the same response in PROME's chat" disappears once a receipt exists, and `received` is now mandatory. | Code read | The confirmation note still appears in the reply and review dialogs, but the card no longer reminds Will after PROME reads. |

**Deferred with Will's approval, not re-raised:** prior residue 3, 4 and 8, same-login identity, and owner attestations.

## 6. Author tests, run after my own pass

| Suite | Tests | Result |
|---|---|---|
| `test_wq641` | 9 | OK |
| `test_batch` | 21 | OK |
| `test_wq638` | 49 | OK |
| `test_desk` | 27 | OK |
| `test_desk_review` | 8 | OK |

Other suites were not run, as this read was scoped to the changes.

## 7. App-only

App-only remains OFF pending real interactive proof. This reader is headless and its hooks are disabled, so nothing here proves a live alert. Enabling app-only later needs that proof, an acceptance record that names the build, and a valid `app_only_since`.

Repro scripts are in `/tmp/wq641-rev`: `a.py` (B1), `b.py` (enablement), `c.py` (fallback), `d.py` (receipt chains), `e.py` (isolation and corruption), `f.py` (lease and interactive gate). Fixtures are in `/tmp/wq641-rev/fx`.
