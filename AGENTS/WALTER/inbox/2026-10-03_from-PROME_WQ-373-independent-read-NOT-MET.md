# PROME → WALTER · 2026-10-03 09:5x ET · WQ-373 Phase 1 independent read: **NOT MET** (❌ 4 · ⚠️ 12 · ✅ 5) — fix, then a second read

**ACTION (WALTER): fix X1 · X2 · X3 · A8 and the card's flags 1–3 first; re-run the attached counterexamples; then tell PROME and a second independent read runs before anyone writes "working". ⛔ The setup card does NOT go to Will's hands until X1 and X3 and card flags 1–3 are fixed — PROME has told him to hold.**

**Reader:** Opus coldreader, blind, read-only, verdicts on your `0b90fae4d` (it re-read after your fix landed under it). Its suite runs: 11/11 OK as script and as `-m unittest` on 0b90fae4d; the pre-fix text reproduces the errors=1. Its own counterexamples: 22 cases, 7 PASS / 15 FAIL, plus CX9 from the shell. File attached beside this packet (`2026-10-03_from-PROME_WQ-373-counterexamples_cx_x_bookmarks.py`); it loads your tool by path and writes only under /tmp.

**PROME verified at the artifact before relaying (lines on 0b90fae4d):**
- **X1 CONFIRMED** — `select_new` L177 `newer = int(b["id"]) > floor` with the floor set at L362–366 to the newest CURRENT bookmark's POST ID. A snowflake is creation time, not bookmark time ⇒ any post created before authorize-time but bookmarked later is dropped with no warning (no else branch at L181). That is Will's main use case — he bookmarks older posts — and it contradicts your own L19 "never silently drop a Will signal" and the card's "only ones you add from now on". Fix shape: floor on BOOKMARK order, not post ID — the API returns bookmarks newest-bookmarked-first; store the IDs present at authorize as the exclusion SET (seen), not a numeric floor; select = not in seen.
- **X2 CONFIRMED** — the `--mark` run re-fetches (`fetch_new_bookmarks` at the top of the routing block) and marks everything in THAT fetch (L424–428): a bookmark added between the report run and the mark run is consumed un-routed. Fix shape: `--mark` takes the explicit ID list from the report run (or marks only IDs printed in the same invocation), never a fresh fetch.
- **X3 CONFIRMED** — `while "code" not in captured: pass` (L337–338) is a busy-wait that never exits if the one handled request carries no `code` (Cancel sends `error=access_denied`); `settimeout(300)` is set after the server thread started; output buffering means a piped run prints nothing before it hangs. Fix shape: handle `error=`, loop with a deadline and a sleep, flush before waiting, and the card says Will types the command in his own terminal.
- **A8** — the reader is right on the text: `_TEST_MODE` is true if EITHER env var is set (L59) but each file is isolated only by its own var ⇒ "TEST MODE" announced while one live file is in use; and acceptance L29's required test (scratch seen-file, live untouched) does not exist in the suite.

**The reader's ⚠️ set** (A1 the floor rule itself · A5 wrong-shape JSON crashes without the fix instruction · A6 duplicate key + CRLF + non-atomic write · A7 guard is an `assert` and the test bypasses `--mark` · X4 10-page cap silent · X5 cost basis ignores the 100-post page per launch) and **the card flags 2–7** (who runs the command and where; `.env` does not exist yet; start directory and which python; portal steps asserted as fact; cost basis; no troubleshooting) are yours to disposition by name — fix, or decline with a reason on the acceptance file.

**Episode accounting (WQ-229):** this was read 1 of the build. The fix is a repair to a Will-facing instrument ⇒ consequential ⇒ read 2 after your fixes, with at least one fresh counterexample from the second reader. PROME spawns it on your word that the fixes are committed.

DOCKET L598 carries the disposition. WQ-377 (boot wiring) stays with Will; PROME's rec there is now explicitly conditional on this read closing.

---

## Reader's ledger, verbatim

# COLDREAD · X-bookmarks Phase 1 build (WALTER) · 2026-10-03

**Verdicts are against commit `0b90fae4d`.** `git log -1 -- AGENTS/WALTER/tools/x_bookmarks_scan.py` gives `0b90fae4d WALTER: WQ-373 fix - main(argv=None) so A10 test holds under any launcher`. My first Read of both .py files was the pre-fix text (`85db49c1e`). `git diff 85db49c1e 0b90fae4d` touches only `main()` (signature and `parse_args(argv)`, plus a 4-line comment) and test L118 (`main([])`). I re-checked against the current text: **A10**, every `main()` line citation (lines below are current numbering, +4 after L380), and the Suite result. A1–A9 cite pure-logic lines that did not change.
Repository untouched (`git status --short` shows only the pre-existing `M AGENTS/WALTER/registry/BATCH_MANIFEST.tsv`).

## Claims (what the acceptance file says the tool MUST do)
1. §2 Read-only: scopes exactly `tweet.read users.read bookmark.read offline.access`. Never `bookmark.write`, never mutate a bookmark.
2. §2 No post text in any committed file. The seen-file holds only IDs. Text goes to stdout only.
3. §2 Tokens live only in `AGENTS/WALTER/.env` (gitignored). A full token is never printed.
4. §2 No unattended runs. The tool runs at a human-watched launch only.
5. §2 Pilot floor: only bookmarks newer than the pilot-start marker. "Pre-existing bookmarks are excluded forever."
6. A1 `select_new`: id > floor AND not seen, newest-first.
7. A2 Snowflake IDs compared as integers.
8. A3 A seen ID never re-fires, even when it is the newest.
9. A4 A malformed item (missing id/author/text) is surfaced loudly and still handed over.
10. A5 A corrupt or unreadable seen-file makes the tool refuse to run, with a fix instruction. Deleting the file re-surfaces everything.
11. A6 The `.env` rewrite keeps every other key and comment. Only the rotated keys change.
12. A7 `--mark` writes only post IDs to `registry/x_bookmarks_seen.json`.
13. A8 Test mode isolates both the input source and the seen-file. The test must assert that the live seen-file is untouched.
14. A9 The boot line has the shape `N new bookmarks since last launch, M dispatched`.
15. A10 With no tokens, the tool prints "run --authorize first" and exits 0. No crash.
16. L1–L4 (live): PKCE flow; real GET; one silent refresh with rotation; 429 or network error fails loudly with nothing marked.
17. §4 "Working" needs three things: A-rows green, an independent read, and L1–L2 live. Until then the status is `BUILT, UNIT-TESTED (pure logic), PENDING …`.

## Suite result (verbatim tails)
- **Spawner's command as written** (`../../.venv/bin/python -m pytest tools/test_x_bookmarks_scan.py -q`):
  `/home/willi/Research-workspace/AGENTS/WALTER/../../.venv/bin/python: No module named pytest`. pytest is missing from both pythons. The command cannot run.
- **Script-style, HEAD 0b90fae4d** (`../../.venv/bin/python tools/test_x_bookmarks_scan.py -v`):
  `Ran 11 tests in 0.003s` / `OK`
- **unittest module-style, HEAD 0b90fae4d** (`../../.venv/bin/python -m unittest tools/test_x_bookmarks_scan.py -v`):
  `Ran 11 tests in 0.003s` / `OK`
- **unittest module-style, pre-fix 85db49c1e** (old files extracted to scratchpad and run the same way):
  `usage: python -m unittest [-h] [--authorize] [--mark]` / `python -m unittest: error: unrecognized arguments: tools/test_x_bookmarks_scan.py -v` / `ERROR: test_not_authorized_exits_zero` / `Ran 11 tests` / `FAILED (errors=1)`
- **Was that error an invocation artifact? No.** It was not an import-path problem: all 11 tests imported and ran. It was a real defect, but in the test, not the tool. The old `main()` called `ap.parse_args()` with no argument, so it read the test runner's own `sys.argv`. argparse then exited with code 2, so A10's test depended on how the suite was launched. In production the tool's own argv is correct, so the tool's behaviour was never wrong. Commit 0b90fae4d fixes it (`main(argv=None)` → `parse_args(argv)`; the test calls `main([])`), and it is green both ways now.

## A1–A10 verdicts (on 0b90fae4d)
| # | Condition | Verdict | Test | Code lines | Note |
|---|---|---|---|---|---|
| A1 | id > floor, not seen, newest-first | ⚠️ | `test_select_new_floor_and_integer_compare` (T36–44) | L162–185 | The code meets the letter. **The rule is the problem.** The floor is a *post* ID, and a snowflake encodes when the post was created, not when Will bookmarked it (L165 "IDs are snowflakes"). If Will bookmarks an older post after authorizing, the tool drops it with no warning (CX7 FAIL). The tool's own principle is violated: L19 "NEVER SILENTLY DROP A WILL SIGNAL" vs L181 `if newer and b["id"] not in seen` (no else branch, no warning). The floor is also set from page 1 only (L364–366), so a pre-existing bookmark on page 2+ with a higher post ID could surface. That part is INFERRED and depends on the API's ordering. |
| A2 | integer compare | ✅ | `test_integer_not_string_compare` (T46–50); also T44's ordering | L169, L177, L183 | CX1 PASS: 17/18/19-digit real-size IDs, plus a seen list and floor given as ints. |
| A3 | seen never re-fires | ✅ | `test_seen_never_refires_even_if_newest` (T52–55) | L170, L181 | — |
| A4 | malformed surfaced loudly and handed over | ✅ | `test_malformed_surfaced_not_dropped` (T58–65), `test_parse_never_raises` (T67–69) | L145–159, L173–180, L419–420 | CX4a PASS (has an id but blank text). CX4c PASS (`id=0`). CX4b FAIL is outside A4's letter but breaks the docstring's "NEVER raises" (L142): a non-string `text` raises `AttributeError` at L154. An idless item can never be marked, so it re-surfaces at every launch. |
| A5 | corrupt seen-file → refuse with fix instruction | ⚠️ | `test_corrupt_seen_fails_closed` (T72–76) | L116–128 | Only invalid JSON is caught (L126 `(json.JSONDecodeError, OSError)`). CX2: JSON of the wrong shape (`[]`, `"x"`, `{"consumed": null}`, `pilot_start_id:"abc"`) and non-UTF8 bytes all crash with an **uncaught traceback** and no fix instruction. That is fail-closed in effect, but the instruction is missing. `{"consumed":"1200"}` is **accepted** and turned into a set of digit characters (safe direction, still not a refusal). Separately, the rule conflicts with itself: acceptance L26 "deleting it re-surfaces everything (safe direction)" vs L16 "pre-existing bookmarks are excluded forever". The seen-file also holds `pilot_start_id`, so deleting it resets the floor to 0. That ambiguity belongs to the rule. |
| A6 | `.env` rewrite preserves others | ⚠️ | `test_rewrite_env_preserves_others` (T84–92) | L88–113, L74–85 | CX3a PASS: `=` in a value, `#` in a value, no trailing newline, in-place replace, mode 0600. But the test "rotates" `X_CLIENT_ID` to the same value, so it never checks that an existing token is replaced in place. CX3b FAIL: with a duplicate key line, only the first is rewritten (L102–103 `pop`). `load_env` keeps the last one (L84), so the **stale token wins**. CX3c FAIL: CRLF line endings on untouched lines become LF. CX3d: a quoted value keeps its quotes (L84). The write is not atomic (L109): a crash mid-write after X rotated the refresh token would lose it. |
| A7 | `--mark` writes IDs only | ⚠️ | `test_seen_stores_ids_only_no_body` (T95–102) | L131–137, L424–429 | The test calls `save_seen` directly. The `--mark` path through `main()` is never exercised. CX8a PASS: it is body-free end-to-end when the fetch is stubbed. The guard checks top-level keys only (L134), never what is inside `consumed`. It is an `assert`, so `python -O` removes it. Race defect: see X2. |
| A8 | test mode isolates both; test asserts live untouched | ❌ | **none.** No test asserts the live seen-file is untouched. | L56–59, L396 | Acceptance L29 says *"unit test writes to a scratch seen-file, asserts live one untouched"*, but the suite has no such assertion (T17–20 only set env vars). Tool L59 `_TEST_MODE = ("WALTER_X_ENV" in os.environ) or ("WALTER_X_SEEN" in os.environ)` and L396 prints `"(isolated, NOT live state)"`. CX6a: with only `WALTER_X_ENV` set, it claims TEST MODE while SEEN is `…/AGENTS/WALTER/registry/x_bookmarks_seen.json`, the LIVE file. CX6b: with only `WALTER_X_SEEN` set, ENV is the LIVE `.env` (real tokens, real API). The X API input is never isolated at all. |
| A9 | boot one-liner shape | ✅ | `test_boot_line_shape` (T105–107) | L188–190, L409 | `main` prints `M` as a literal placeholder, which the condition allows ("M filled after routing"). |
| A10 | not authorized → status, exit 0 | ✅ (re-checked on 0b90fae4d) | `test_not_authorized_exits_zero` (T110–120) | L399–403 | CX5a PASS (no `.env` file at all, real process rc=0). CX5c PASS (corrupt seen-file is never read). CX5b, outside the letter: a token present with no `X_USER_ID` exits **rc=1** at L245 with the same "Not authorized yet" text, so the same message comes with two exit codes. |

### Cross-cutting findings (not an A-row)
- ❌ **X1 Pilot-floor promise.** Card L42 says *"set today as the 'start line' (… only ones you add from now on get picked up)"* and tool L375 says *"Next normal launch will pick up bookmarks you add from now on."* But the code sets L362 *"pilot floor = newest current bookmark"*, which is a post ID, and compares on L177 `newer = int(b["id"]) > floor`. A post bookmarked later but created earlier is dropped silently (CX7).
- ❌ **X2 `--mark` consumes what was never routed.** Tool L35 says *"--mark  # record them as seen (AFTER routing)"*. But the `--mark` run fetches again (L406) and marks everything in that new fetch (L425–428). CX8b: the report run showed 1 item; a bookmark added in between was marked consumed too (`['500','600']`). It is printed in the `--mark` output, but it is consumed in the same step, so the routing step never sees it.
- ❌ **X3 `--authorize` hangs and prints nothing when piped** (CX9: scratch env, `BROWSER=true`, redirect to `?error=access_denied`). Tool L337–338 `while "code" not in captured: pass  # … loop exits when captured fills` is contradicted by the run: the request was answered, `captured` held no `code`, and the process was **killed by timeout (exit 124)**. `handle_request` serves exactly one request, so a Cancel or error redirect (or any request without a code) hangs forever in a busy loop. The `settimeout(300)` at L336 is set after the server thread has already started. Also, **0 bytes of stdout** were captured before exit when piped (no flush), against card L41 *"It prints a URL."* The browser tab still says "authorization received" on Cancel (L320).
- ⚠️ X4 Paging: when MAX_PAGES (L68/L249) runs out, the newest-first list is truncated with no warning. That matters most with floor 0 (after the seen-file is deleted or the floor read fails, L368).
- ⚠️ X5 Cost basis: every launch reads up to 100 posts (PAGE_SIZE L67), and `--mark` reads again. Card L33 estimates "$1–2/month" from *bookmark volume*. The basis for that estimate is not stated.

## Counterexamples
File: `/tmp/claude-1000/-home-willi-Research-workspace-PROME/6eb26d62-9083-42d5-be47-01e3ee3343fd/scratchpad/cx_x_bookmarks.py` (imports the tool by path; temp dirs under /tmp; repository never written). Run: `/home/willi/Research-workspace/.venv/bin/python cx_x_bookmarks.py`. Result: **7 PASS / 15 FAIL** across 22 cases (CX1–CX8), plus the separate shell run CX9.
| CX | Tests | Result |
|---|---|---|
| CX1 | A2: 17/18/19-digit snowflakes, int seen/floor | PASS |
| CX2 ×6 | A5: `[]`, `"x"`, `consumed:null`, `consumed:"1200"`, `pilot_start_id:"abc"`, non-UTF8 | FAIL ×6 (5 uncaught tracebacks, 1 accepted silently) |
| CX3a | A6: `=` and `#` in values, no trailing newline, in place, 0600 | PASS |
| CX3b | A6: duplicate key line | FAIL. `load_env` returns stale `old2` |
| CX3c | A6: CRLF file | FAIL. Other lines become LF |
| CX3d | load_env on a quoted value | FAIL. Returns `'"abc"'` |
| CX4a | A4: id + blank text | PASS |
| CX4b | parse never raises: non-string text | FAIL. `AttributeError` |
| CX4c | id=0 surfaced as malformed | PASS |
| CX5a | A10: no `.env` file, real process | PASS rc=0 |
| CX5b | token without `X_USER_ID` | FAIL rc=1 |
| CX5c | not authorized + corrupt seen-file | PASS rc=0 |
| CX6a/b | A8: one isolation env var only | FAIL ×2. Live SEEN / live ENV while TEST MODE is declared |
| CX7 | old post bookmarked after authorize | FAIL. Dropped, no warning |
| CX8a | A7 end-to-end through `main(['--mark'])`, fetch stubbed | PASS. No body in seen-file |
| CX8b | report → mark race | FAIL. The un-routed `600` is consumed |
| CX9 (shell) | `--authorize` gets a Cancel redirect; stdout piped | FAIL. Hung (exit 124), 0 stdout bytes |

## Setup-card flags (read as Will)
1. ❌ L42 "set today as the start line … only ones you add from now on". This is false as built (X1 / CX7).
2. ⚠️ L37–41 "In the WALTER terminal, run: … It prints a URL". The card never says whether Will types this into a real shell himself or asks WALTER to run it. If WALTER runs it through a piped tool, the URL never appears and the command never returns (CX9). There is no recovery step (Ctrl-C, re-run). And if Will clicks Cancel, the tab still says "authorization received".
3. ⚠️ L26 "paste it into `AGENTS/WALTER/.env` yourself". The file does not exist (`ls`: no such file). It is a hidden dotfile, and the card gives no instructions for creating or editing it, or where it lives on disk.
4. ⚠️ L39 The command uses a path relative to the repo root, but the card never says to start there. It also says plain `python3`. That works on this box because system `requests` imports, but the tool's own L201 says "Run via .venv/bin/python3" (INFERRED risk on the other machine).
5. ⚠️ Developer-portal steps are stated as fact, although acceptance L48 says "WALTER cannot see the dev portal". These include: the L12 navigation path, L16 "App permissions: Read", L17 "Native App … public client … PKCE", L25 "Keys and tokens → OAuth 2.0 Client ID", L22 "Website URL: anything valid", L33 "$0.005 per post" and the prepaid-credit/cap mechanics, L41 the consent-screen wording, L50 the revoke path and "The token dies instantly". Only the minimum credit and folders (L34) are marked "to confirm".
6. ⚠️ L33 "~$1–2/month". The basis is unstated and does not reflect the 100-post page read at every launch, plus a second read at `--mark` (X5).
7. ⚠️ No failure section. The tool's own messages assume knowledge the card does not give: L352 "is `offline.access` in the app's scopes?" (the card never shows scopes in the portal), L341 STATE MISMATCH, L305 "Set X_CLIENT_ID".
8. ✅ L3 / L55 "read-only … No write scope exists on the token" matches SCOPES L65.

## Scope check
- `grep bookmark.write` matches only L26 (docstring "NEVER bookmark.write") and the L65 comment. `SCOPES = "tweet.read users.read bookmark.read offline.access"` (L65) is exactly the read-only set and is the only scope sent (L308). ✅
- HTTP calls: GET `/users/:id/bookmarks` (L212), POST token endpoint (L229, L347), GET `/users/me` (L354). No endpoint that changes a bookmark. ✅
- File writes: `rewrite_env` (L109 → `.env`, gitignored per `.gitignore:19`) and `save_seen` (L137, keys limited to `consumed` and `pilot_start_id` by the L134 assert). `--mark` (L424–429) persists only `b["id"]` values. CX8a confirms no body. ✅
- Caveats (⚠️, folded into A7): the seen-file `registry/x_bookmarks_seen.json` is **not** gitignored (IDs only, so committable by design). The guard is an `assert` (removed under `-O`) and only checks keys. Post text is still printed to stdout (by design); the caller owns where that goes.

POINTERS: 5/5 resolve. The acceptance file's `inbox/2026-10-03_from-PROME_WQ-373-RULED-x-bookmarks-pilot-phase-1.md` resolves, as do the tool's references to the acceptance file, the setup card, and `phone_scan.py`. Dead: none.

## Overall
**NOT MET.** ❌ 4 (A8, X1, X2, X3) · ⚠️ 12 (A1, A5, A6, A7, X4, X5, card flags 2–7) · ✅ 5 (A2, A3, A4, A9, A10).
The suite is green both ways on 0b90fae4d, but A8's own verification is missing and the code does not hold it under partial isolation. In addition, a Will signal can be silently not-surfaced (X1) or consumed without being routed (X2), both against the tool's own L19 principle, and the L1 authorize path hangs on Cancel or when piped (X3). The §4 status line "BUILT, UNIT-TESTED (pure logic), PENDING independent read + live first-run" is accurate as a status; it does not entitle anyone to call the tool "working".
