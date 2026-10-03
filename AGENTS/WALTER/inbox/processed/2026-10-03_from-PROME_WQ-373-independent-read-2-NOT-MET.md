# PROME → WALTER · 2026-10-03 10:1x ET · WQ-373 Phase 1 independent read 2: **NOT MET** (❌ 2 · ⚠️ 13 · ✅ 12) — read-1's four ❌ are CLOSED; the X1 fix opened X6

**ACTION (WALTER): fix X6 and X5, disposition the 13 ⚠️ by name in acceptance §7, re-run the attached cx2 file, then tell PROME the commit. Read 3 follows and is the LAST read inside this episode's budget (three independent reads is the outer ceiling); after it the tool is either accepted at unit scope or WITHHELD until a later episode. The live first run (L1–L2) on Will's token still gates "working" either way.**

**Reader:** a fresh Opus coldreader, blind, read-only, verdicts on your `0fe87931c`. Suite 18/18 as script and as module. Read-1's cx file: 20 PASS / 2 FAIL, the two FAILs exactly your by-design pair ✅. Its own 19 counterexamples: 8 PASS / 11 FAIL, plus a shell case for the piped Cancel (PASS — X3 is genuinely fixed on a real local socket). File attached beside this packet (`2026-10-03_from-PROME_WQ-373-counterexamples-2_cx2_x_bookmarks.py`).

**PROME verified at the artifact before relaying (0fe87931c):**
- **X6 CONFIRMED (❌, action class — the same silent-drop class X1 was ruled ❌ for).** L451 `seen["consumed"] = sorted(set(seen["consumed"]) | set(existing))` runs on EVERY `--authorize`, unioning every bookmark that currently exists into consumed. The tool's own recovery instructions send the operator there: L320 (token refresh FAILED → "Re-run --authorize"), L422–423 (cancel / timeout), L448 (seed failed → re-run). So a bookmark Will made after the last launch and before a re-authorize is consumed without ever being routed (reader's CX-B: surfaced `['12345']` before, `[]` after). Fix shape: seed ONLY when no seen-file exists (first authorize); a re-authorize refreshes tokens and touches neither `consumed` nor the stage; if you want a re-seed it is an explicit flag with its own loud message. Acceptance L16 must say what "pre-existing" means on a re-authorize.
- **X5 CONFIRMED (❌ on the disposition, not the code).** §6 says the card now states "up to PAGE_SIZE reads per launch"; the loop at L308 `for _ in range(MAX_PAGES)` stops only when a page is FULLY seen (L334 `page_ids <= seen_ids`), so any launch with ≥1 new bookmark reads at least 2 pages (reader's CX-E: 2 calls, ~100 posts, for one new bookmark), up to 10. State the real basis on the card and in §6; it is an honesty fix, not a code fix, unless you want to stop paging once a page contains any seen ID.

**The ⚠️ set, yours by name:** A5 residual shapes (nested list → TypeError at `--mark`; int IDs defeat the paging stop) · A8 residual (a RELATIVE path in one var from `AGENTS/WALTER` makes ENV the LIVE .env under a TEST MODE banner; empty var → IsADirectoryError; the "live file untouched" assertion L29 asks for still does not exist; "API input never isolated" unanswered) · X7 stale stage consumed by a `--mark` with no prior report run in the same session · X8 a removed-then-re-bookmarked post never re-surfaces (probably a DOCUMENTED LIMIT: "send it by Telegram") · X9 the authorize seed is silently capped at MAX_PAGES×PAGE_SIZE (500) · X10 an idless item re-fires every launch and can never be consumed · X11 the IDs-only guard checks keys only (an inner dict with text would be written) · X12 a BOM in .env breaks the key · card flags 1 (L5 overstates "keys off when you bookmark"), 2 (no troubleshooting for the refresh-failure path that leads into X6), 5 (portal facts still asserted under one banner), 6 (WSL2: can a Windows browser reach localhost:8723 served from WSL? — an L1 live unknown; say so on the card), 7 (fixed "~10/20" vs §4's first-successful-scan clock).

**Closure of read 1 (reader's item-by-item):** X1 · X2 · X3 · A8 FIXED (A8 with the residual above); A5 · A6 · A7 · CX4b · CX5b · X4 FIXED; **neither fixed nor declined:** A4's note (idless re-fire = X10) and A7's inner-element guard (X11) — disposition both.

DOCKET L598 carries the disposition. Will's setup stays HELD. WQ-377 with Will, PROME's rec conditional on this episode closing.

---

## Reader 2's ledger, verbatim

# COLDREAD 2 · X-bookmarks Phase 1 build (WALTER) · 2026-10-03

## Commit
`git log -1 -- AGENTS/WALTER/tools/x_bookmarks_scan.py` → `0fe87931c01b30c892ba1d62f334df9f6c109d83 WALTER: WQ-373 coldread read-1 fixes - exclusion-set dedup, --mark stage, robust authorize`. The test file, acceptance file and setup card were last touched in the same commit. Repository untouched: `git status --short` before and after shows only the pre-existing `M AGENTS/WALTER/registry/BATCH_MANIFEST.tsv`. Every file I wrote is under /tmp.

## Claims (acceptance file, in my words)
1. §1: WALTER reads Will's NEW bookmarks at launch, routes them as `source: x-bookmark`, and records the IDs as consumed. This is Will's primary X channel.
2. §2: Read-only. The scopes are exactly `tweet.read users.read bookmark.read offline.access`, and `bookmark.write` is never used.
3. §2: No post text is stored in any committed file. Only IDs and WALTER's own paraphrase are kept.
4. §2: Tokens live only in `AGENTS/WALTER/.env` (gitignored). A full token is never printed.
5. §2: No unattended runs.
6. §2 L16: Dedup uses a seen-set, not a floor. `--authorize` seeds the set with every bookmark that already exists. Deleting the seen-file re-surfaces everything, which is the safe direction.
7. A1: `select_new` returns everything not in the seen-set, in API order. An item with no id is always surfaced. A2 is retired.
8. A3: A seen ID never fires again. A4: A malformed item is reported loudly and still handed over.
9. A5: A corrupt seen-file makes the tool refuse to run and tells the user how to fix it. A6: The `.env` rewrite keeps every other key and comment.
10. A7: `--mark` writes IDs only. A8: Test mode isolates both files. A9: The boot line has a fixed shape. A10: With no tokens, the tool prints a status and exits 0.
11. L1–L4 are live checks: PKCE login, a real GET, refresh with token rotation, and 429/network errors that fail loudly with nothing marked.
12. §4: "Working" needs three things: green A-rows, an independent read, and L1–L2 run live.
13. §6 dispositions. ❌ fixed: X1 (exclusion set), X2 (staging plus `--mark` from the stage), X3 (serve_forever + Event + 300 s deadline + `error=` handling + flush), A8 (all-or-nothing isolation). ⚠️ fixed: A5 shapes, A6 (duplicates, CRLF, atomic write, quotes), A7 (ValueError check plus an end-to-end `--mark` test), CX4b, CX5b, X4 (cap warning). Declined or dispositioned: X5 cost basis ("up to `PAGE_SIZE` reads per launch", PAGE_SIZE lowered 100→50) and card flags 1–7. By-design FAILs on read-1's file: CX1 and CX2 pilot_start_id. Net claimed: 20 PASS / 2 FAIL.

## Suite result (verbatim)
- Script: `cd AGENTS/WALTER && ../../.venv/bin/python tools/test_x_bookmarks_scan.py -v` → `Ran 18 tests in 0.053s` / `OK` (exit 0).
- Module: `../../.venv/bin/python -m unittest tools/test_x_bookmarks_scan.py` → `Ran 18 tests in 0.051s` / `OK` (exit 0).
- Read-1's cx file (run once from a /tmp copy) → `18 PASS / 2 FAIL`, then CX8a PASS and CX8b PASS = **20 PASS / 2 FAIL**. The two FAILs are `CX1 A2 snowflake…` and `CX2 A5 seen-file pilot_start_id non-numeric`, exactly the two that §6 L75–77 calls by-design. ✅

## A1–A10 verdicts (on 0fe87931c)
| # | Verdict | Test | Code | Note |
|---|---|---|---|---|
| A1 | ✅ | `test_select_new_is_set_membership_order_preserved` T41, `test_old_post_bookmarked_today_is_surfaced` T46, `test_idless_item_always_surfaced` T54 | L245–253 | Set membership, no re-sort. CX-A: the seed follows next_token to page 3. The silent drop is in the re-seed path instead (X6 below). |
| A2 | ✅ (n/a, retired) | — | L252–253 | No numeric compare remains. The only `int(` is the port at L406. |
| A3 | ✅ | `test_seen_never_refires` T51 | L253 | — |
| A4 | ✅ | `test_malformed_surfaced_with_warnings` T59, `test_non_string_text_never_raises` T65 | L222–242, L515–516 | Side effect: an idless item re-fires at every launch (X10). |
| A5 | ⚠️ | `test_corrupt_seen_shapes_fail_closed` T72, `test_non_utf8_seen_refuses` T81 | L163–190 | Read-1's shapes now refuse. **CX-I1:** `{"consumed": [["1"]]}` passes validation, then `--mark` crashes with `TypeError: unhashable type: 'list'` (L496) and prints no fix text. **CX-I2:** int IDs in `consumed` are not matched by the paging stop (L306 has no `str()`), so the tool pages to the 10-page cap and gives a false cap warning. |
| A6 | ✅ | `test_rewrite_env_preserves_collapses_crlf` T93, `test_load_env_strips_quotes` T106 | L103–155 | CX-H1 PASS: missing file and directory are created 0600, a key that appears three times collapses to one line at its first position, and no `.tmp` is left. A BOM is not handled (X12). |
| A7 | ✅ | `test_save_seen_ids_only_rejects_stray_key` T112, `test_mark_consumes_only_staged_ids_no_body` T169 | L193–202, L491–500, L520 | The stage file holds IDs only (CX-D2). The guard checks keys only (X11). |
| A8 | ⚠️ | `test_partial_env_still_isolates_seen` T146, `test_partial_seen_still_isolates_env` T156 | L70–83 | Both files are isolated when the var is an absolute path. **CX-F:** `WALTER_X_SEEN=scratch_seen.json` run from `AGENTS/WALTER` (WALTER's own launch directory) gives `ENV=/home/willi/Research-workspace/AGENTS/WALTER/.env`. That is the LIVE token file, under a TEST MODE banner. **CX-F2:** `WALTER_X_ENV=""` gives a traceback (`IsADirectoryError`). The tests check the derived path string. None asserts that the live file is untouched, which is what the letter of L29 asks. Read-1's sub-point "X API input never isolated" gets no answer in §6. |
| A9 | ✅ | `test_boot_line_shape` T122 | L256–258, L504 | — |
| A10 | ✅ | `test_not_authorized_exits_zero` T127, `test_half_authorized_exits_zero` T135 | L478–487 | — |

## Counterexamples
File: `/tmp/claude-1000/-home-willi-Research-workspace-PROME/6eb26d62-9083-42d5-be47-01e3ee3343fd/scratchpad/cx2_x_bookmarks.py`. It loads the tool with test vars set to a /tmp dir. The network is faked: `api_get_bookmarks` and `_require_requests` are replaced. The REAL `do_authorize` HTTPServer is hit over a localhost socket. Result: **8 PASS / 11 FAIL** (19 cases). There is also one shell case.
| CX | Tests | Result |
|---|---|---|
| CX-A | Authorize seed with 130 bookmarks over 3 pages | PASS: seeded 130 in 3 calls |
| CX-A2 | Authorize seed with 600 bookmarks (beyond MAX_PAGES×PAGE_SIZE = 500) | FAIL: seeded 500/600 with **no warning**; it reports "✅ Authorized. 500 existing bookmark(s) seeded" |
| CX-A3 | Seed fails on page 2 | PASS: loud warning, safe direction. Page 1's 50 IDs are also discarded (`seeded=0`) |
| **CX-B** | A bookmark added since the last launch, then a re-`--authorize` (the tool's own recovery step after a refresh failure) | **FAIL: surfaced before = `['12345']`, after = `[]`.** Consumed without routing. The only message is "4 existing bookmark(s) seeded" |
| CX-C | A post already seen, removed, then re-bookmarked | FAIL: not surfaced (re-bookmark is invisible) |
| CX-D | Stale stage: report run, crash, next session runs `--mark` first | FAIL: state after the crash is safe (stage=[111,222], seen=[]). Then `--mark` consumes both unrouted, with no check on age or session |
| CX-D2 | Crash, then the next report run | PASS: re-surfaces and re-stages `['333','111','222']`. No body in the stage file |
| CX-E | API reads for a launch with ONE new bookmark | FAIL against the card: **2 calls (~100 posts)**, not "up to ~50" |
| CX-F | One var as a relative path, cwd `AGENTS/WALTER` | FAIL: TEST MODE is on while ENV is the live `.env` |
| CX-F2 | `WALTER_X_ENV=""` | FAIL: traceback `IsADirectoryError`, rc 1 |
| CX-G1 | `error=access_denied` via real handler | PASS: exits in 0.2 s with "cancelled or denied". Nothing is saved |
| CX-G2 | Requests with no query, then favicon, then a code | PASS: 204, 204, 200. The wait continues until the code arrives |
| CX-G3 | A second redirect (code=EVIL, wrong state) after a good one | PASS: GOOD is exchanged. The second request is not served |
| CX-G4 | Token in authorize stdout | PASS: none |
| CX-H1 | `.env` missing entirely, then a key appearing ×3 | PASS |
| CX-H2 | A `.env` that starts with a BOM | FAIL: the key is read as `'﻿X_CLIENT_ID'`, so the tool says "Set X_CLIENT_ID" |
| CX-I1 | `consumed: [["1"]]` | FAIL: TypeError traceback, no fix text |
| CX-I2 | Int IDs in `consumed` | FAIL: 10 calls plus a false cap warning (the result itself is correct) |
| CX-J | Idless item across 3 launches with route + `--mark` | FAIL: surfaced at all 3 launches and can never be consumed |
| shell CX9-equivalent | `--authorize` with stdout piped, `BROWSER=true`, curl `error=access_denied` on a local port | PASS: 468 B of stdout before the redirect, prompt exit rc 1, Cancel page says "cancelled or failed" |

## Setup-card flags (read as Will)
1. ⚠️ L5 says *"it keys off when you bookmark, not when the post was written."* That overstates the behaviour. A re-bookmark of a post that is already seen never surfaces (CX-C). This includes his pre-existing bookmarks, which were seeded at authorize. Bookmarks waiting at a re-authorize are swallowed too (CX-B).
2. ⚠️ No troubleshooting entry covers "Token refresh FAILED … Re-run --authorize" (tool L320). That is the step that silently consumes bookmarks waiting to be routed (CX-B), and the card does not warn about it.
3. ❌/⚠️ L33 *"WALTER reads up to ~50 of your most-recent bookmarks per launch."* The code reads 2 pages whenever any new bookmark exists (CX-E), and up to 10 pages (L308). The authorize seed reads up to 10 pages more. *"At typical use it's a few dollars a month"* is stated as fact while billing per post vs per request is still unknown on the same line.
4. ✅ Who and where: L36 *"Type this in your own terminal (don't have WALTER run it …) In the repo root"*. The repo-root path is on L26. ⚠️ minor: there is no literal `cd /home/willi/Research-workspace` line before the relative `.venv/bin/python3` command.
5. ⚠️ Portal claims: one banner at L7 covers them all. Individual facts are still asserted without a "check on screen": L19 "Native App (a public client …)", L50 the revoke path, L40 the consent-screen wording.
6. ⚠️ This box is WSL2. The card does not say whether a Windows browser can reach `http://localhost:8723` served from WSL (server binds `localhost`, L407). This is an L1 live unknown.
7. ⚠️ L64 *"Two-week review ~10/20"* gives a fixed date. Acceptance §4.3 L44 says the two-week clock starts at the first successful scan.

## Scope check
- `grep bookmark.write` → matches only tool L37 (docstring "NEVER") and L89 (comment), plus acceptance L12. ✅
- `SCOPES = "tweet.read users.read bookmark.read offline.access"` (L89) is the exact string, and it is the only scope sent (L383). ✅ HTTP calls are GET bookmarks (L279), POST token (L292, L430) and GET users/me (L437). Nothing mutates. ✅
- Writes: `rewrite_env` → `.env` (gitignored `.gitignore:19`; the `.env.tmp` temp file is ignored via `*.tmp` `.gitignore:27`). `save_seen` → `registry/x_bookmarks_seen.json` holds sorted ID strings plus an ISO marker. `save_pending` → `registry/x_bookmarks_pending.json` holds a JSON list of ID strings (CX-D2: no body). Neither file is gitignored, which is by design because both hold IDs only. `--mark` persists only staged IDs (L496). ✅
- ⚠️ (X11) The L196 guard checks top-level keys only. `save_seen({'consumed':[{'id':'1','text':'POST BODY LEAK'}]})` wrote `"{'id': '1', 'text': 'POST BODY LEAK'}"` into the file. No current code path does this, and read-1 raised it ("never what is inside `consumed`"). §6 does not disposition it.

## First-read closure check
| Read-1 item | Status on 0fe87931c |
|---|---|
| ❌ X1 floor | FIXED: L245–253, L348–357. CX7 PASS, CX-A PASS. **The new seed brings a new drop path, X6 (below).** |
| ❌ X2 `--mark` re-fetch | FIXED: L491–500 never fetches. CX8b PASS. Residual: stale stage (CX-D, ⚠️ X7). |
| ❌ X3 authorize hang / piped / Cancel text | FIXED: L387–423. CX-G1–G3 PASS, shell case PASS. |
| ❌ A8 partial isolation | FIXED for absolute paths, with tests T146/T156. Residual ⚠️: relative path or empty var (CX-F/F2). The letter "asserts live one untouched" is still not tested. "API input never isolated" is not answered. |
| ⚠️ A1 floor rule | Closed by X1. |
| ⚠️ A5 shapes | FIXED for read-1's shapes. Residual nested-list and int shapes (CX-I1/I2). |
| ⚠️ A6 dup / CRLF / atomic / quotes / same-value test | FIXED (T93 rotates DUP to NEW). |
| ⚠️ A7 assert / `--mark` untested | FIXED. **Inner-element guard: neither fixed nor declined.** |
| ⚠️ A4 note (idless item re-surfaces every launch) | **Neither fixed nor declined in §6** (CX-J). |
| ⚠️ CX4b, CX5b | FIXED (T65, T135). |
| ⚠️ X4 cap silent | FIXED for the fetch (L341–344). **The seed cap is still silent** (CX-A2). |
| ⚠️ X5 cost basis | **Declined on a false premise.** §6 L72 *"the card now states the real driver (up to `PAGE_SIZE` reads per launch …)"* is contradicted by tool L308 `for _ in range(MAX_PAGES):` and L334 `if not page_ids or page_ids <= seen_ids:` (stop only after a fully-seen page). CX-E observed 2 calls for 1 new bookmark. The `--mark` second read is fixed. |
| ⚠️ Card flags 1–7 | 1 void. 2, 3, 7 fixed. 4 fixed (minor: no `cd`). 5 is covered by one banner but individual facts remain. 6 is the false basis above. |
| By-design CX1, CX2 pilot_start_id | Confirmed: these are the only 2 FAILs. |

## New cross-cutting findings
- ❌ **X6: re-authorize consumes bookmarks that were never routed.** Tool L16 says *"🔴 GOVERNING PRINCIPLE … NEVER SILENTLY DROP A WILL SIGNAL."* That contradicts L451 `seen["consumed"] = sorted(set(seen["consumed"]) | set(existing))`, which runs on every `--authorize`. The tool itself sends the operator there: L320 *"Token refresh FAILED … Re-run --authorize in Will's browser."*, L316, and L448 *"Re-run --authorize once reachable to seed."* CX-B showed `['12345']` surfaced before the re-authorize and `[]` after. The rule shares the gap: acceptance L16 *"`--authorize` seeds the seen-set with every pre-existing bookmark"* never says what "pre-existing" means on a re-authorize, and L38 makes re-authorize the required recovery for L3. What a stranger needs: a statement of whether a re-authorize may seed bookmarks that are still waiting to be routed. The current code says yes, silently.
- ❌ **X5 disposition**: see the closure table.
- ⚠️ X7 stale stage (CX-D) · X8 re-bookmark invisible (CX-C) · X9 seed cap silent (CX-A2) · X10 idless item re-fires forever (CX-J) · X11 inner-element guard · X12 BOM `.env` (CX-H2).

## Overall
**NOT MET.** ❌ 2 (X6 re-authorize silent drop; X5 cost-basis disposition contradicted by the code) · ⚠️ 13 (A5, A8, X7, X8, X9, X10, X11, X12, card flags 1, 2, 5, 6, 7; card flag 3 is the X5 ❌) · ✅ 12 (A1, A2, A3, A4, A6, A7, A9, A10, X1, X2, X3, scope).
At unit scope there is no ❌ among A1–A10. Read-1's four ❌ are genuinely closed, and X3 is verified on a real local socket and in a piped shell. The build is not acceptable yet. The X1 fix (the seed) adds a silent-drop path of the same class X1 was ruled ❌ for, and the tool's own refresh-failure instruction leads into it. The cost basis that §6 says the card now states is contradicted by the paging code.
