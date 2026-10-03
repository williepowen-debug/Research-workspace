# X-Bookmarks Phase 1 — Acceptance Conditions

**Owner:** WALTER · **Authority:** WQ-373 RULED by Will 2026-10-03 09:28 ET ("373 approved go with your recs"); build asks in `inbox/2026-10-03_from-PROME_WQ-373-RULED-x-bookmarks-pilot-phase-1.md` + two PROME build-note relays (09:31 primary-channel framing; design points a–d).
**Discipline:** WQ-229 — these conditions are written BEFORE the code is called "working," and an independent read is required before that claim (see §4).

This is the definition of done. `x_bookmarks_scan.py` is "working" only when every MUST row passes a test or a named live check.

## 1. What it is
Will bookmarks posts on X instead of screenshotting them. WALTER reads his **new** bookmarks at launch, routes each through the normal signal path (filter → BOARD → handoff → delivery_log, `source: x-bookmark`), and records the post IDs as consumed. Phase 1 is Will's **primary** X intake channel (his words 09:31), not a side test. Telegram/screenshots keep working in parallel; nothing is cut over.

## 2. Scope boundaries (hard)
- **Read-only.** Scopes `tweet.read users.read bookmark.read offline.access`. **NEVER `bookmark.write`** — the tool must never create, delete, or modify a bookmark.
- **No post bodies in git.** The seen-file and any committed artifact store **post IDs + WALTER's own signal text only**. Post text is printed to stdout for routing and lives in BOARD signals as WALTER's paraphrase — never persisted verbatim in a committed file (honours X's 24h-deletion term).
- **Token never in git.** `X_CLIENT_ID` / access / refresh tokens / user id live in `AGENTS/WALTER/.env` (gitignored repo-wide: `.env`, `.env.*`). The tool reads and rotates them there; it never prints a full token to stdout.
- **No unattended runs.** Phase 1 runs only at a WALTER launch, by a human-watched session. "Regularly between launches" = Phase 1b / WQ-369, explicitly OUT.
- **Exclusion set, not a floor** *(corrected after read-1 X1).* Dedup is membership in a **seen-set of post IDs**, never a numeric post-ID floor — a snowflake is *creation* time, not *bookmark* time, so a floor silently drops an old post bookmarked today (Will's main use case). `--authorize` seeds the seen-set with every pre-existing bookmark; while the seen-file lives, those stay excluded. **Deleting the seen-file re-surfaces everything** — the safe direction (over-surface, never drop). These two facts are consistent: "excluded" is a property of the seen-file's contents, not a permanent floor.

## 3. MUST conditions (acceptance matrix)

| # | Condition | How verified |
|---|---|---|
| A1 | `select_new()` returns bookmarks **not in the seen-set**, in the API's given order (newest-bookmarked-first) — no floor, no re-sort; an idless item is always surfaced | unit test `test_select_new_is_set_membership_order_preserved` + `test_old_post_bookmarked_today_is_surfaced` |
| A2 | *(retired with the floor, read-1 X1)* — dedup is string set-membership, not a numeric compare; the old integer-floor trap no longer exists | n/a (no numeric comparison in the model) |
| A3 | A bookmark already in the seen set never re-fires, even if still the newest | unit test |
| A4 | A malformed item (missing id / author / text) is **surfaced LOUD and still handed over**, never silently dropped | unit test |
| A5 | Corrupt/unreadable seen-file → **refuse to run** (fail closed), with a fix instruction; deleting it re-surfaces everything (safe direction) | unit test |
| A6 | `.env` rewrite on token rotation preserves all other keys and comments; only the rotated keys change | unit test |
| A7 | `--mark` records **post IDs only** to `registry/x_bookmarks_seen.json`; no post text written | unit test asserts no body substring in file |
| A8 | Test mode isolates BOTH the input source AND the seen-file (phone_scan 2026-08-03 lesson) | unit test writes to a scratch seen-file, asserts live one untouched |
| A9 | Boot one-liner emits `N new bookmarks since last launch, M dispatched` shape (N from tool; M filled after routing) | unit test on the formatter |
| A10 | Not-yet-authorized state (no `.env` tokens) → clean "run --authorize first" status, **exit 0, not a crash** | unit test |

### Live conditions (cannot be unit-tested; need Will's token — gate the "working" claim)
| # | Condition | How verified |
|---|---|---|
| L1 | `--authorize` completes the OAuth2 PKCE flow in Will's browser; WALTER never sees his password; tokens land in `.env` | live first-run with Will |
| L2 | A real `GET /2/users/:id/bookmarks` returns his bookmarks; the newest routes correctly | live first-run |
| L3 | Access-token expiry → one silent refresh (rotating the refresh token in `.env`) → retry succeeds; a failed refresh fails LOUD with a re-authorize instruction | live, or forced-401 live test |
| L4 | Rate-limit (429) and network error → fail LOUD, exit non-zero, nothing marked consumed | live or injected |

## 4. "Working" is not claimable until
1. All A-rows pass (`test_x_bookmarks_scan.py` green), **and**
2. An **independent read** of the tool (coldreader or a fresh-context reviewer) — WQ-229, because a correction/build pass is itself unreviewed work, **and**
3. L1–L2 pass on Will's live token at least once (the first-successful-scan date starts the L599 two-week clock — report it to PROME).

Until all three: status is **BUILT, UNIT-TESTED (pure logic), PENDING independent read + live first-run.**

## 5. Open portal questions (Will/browser only — WALTER cannot see the dev portal)
- Minimum prepaid credit (pilot plan §2 "not confirmed"); Will confirms at purchase, cap $10/mo.
- Whether bookmark **folders** need Premium — a dedicated folder would keep Will's personal bookmarks out of WALTER's queue (PROME point c). v1 reads the **default (all) bookmarks**; folder-scoping is a v1.x change if the portal allows it without Premium.
- Exact redirect URI must match the app settings (tool defaults to `http://localhost:8723/callback`).
- Whether a bookmarks read bills **per post** or **per request** (drives the cost basis in §6 X5).

## 6. Coldread read-1 dispositions (2026-10-03 — every ❌/⚠️ by name)
Reader verdict NOT MET (❌4 · ⚠️12 · ✅5) on `0b90fae4d`. Disposition on the fix commit:

**❌ fixed**
- **X1 / A1 (floor drops old posts)** — FIXED. Exclusion-set model; `--authorize` seeds pre-existing IDs; `select_new` keeps API order. Regression test `test_old_post_bookmarked_today_is_surfaced`; cx **CX7 now PASS**.
- **X2 / A7 (`--mark` consumes un-routed)** — FIXED. Report run stages printed IDs to `x_bookmarks_pending.json`; `--mark` consumes exactly the stage, never re-fetches. Test `test_mark_consumes_only_staged_ids_no_body`; cx **CX8b PASS**.
- **X3 (`--authorize` hangs on Cancel / piped)** — FIXED. `serve_forever` + `threading.Event` with a 300s deadline; handles `error=`; flushes before waiting; distinct Cancel/timeout messages. (Live-verified at read-2 / first-run; CX9 is a shell case.)
- **A8 (partial isolation announced TEST MODE over a live file)** — FIXED. All-or-nothing: either test var isolates BOTH (unset one derived beside the set one). Tests `test_partial_env_still_isolates_seen` / `_env`; cx **CX6a/b PASS**.

**⚠️ fixed**
- **A5** (wrong-shape JSON) — `load_seen` now refuses non-UTF8, bad JSON, non-object, and `consumed`-not-a-list, each with the delete-to-re-surface instruction. cx CX2 5/6 PASS (the 6th is by-design, below).
- **A6** (duplicate key / CRLF / non-atomic) — duplicate keys collapse to one; CRLF preserved; atomic temp+`os.replace`; `load_env` strips quotes. cx CX3b/c/d PASS.
- **A7 guard** — `save_seen` stray-key check is now an explicit `raise ValueError` (survives `python -O`), and `--mark` is exercised end-to-end through `main()`.
- **CX4b** — non-string `text` is coerced (`str()`), never raises.
- **CX5b** — token present but no `X_USER_ID` → clean "Partially authorized" status, **rc 0**.
- **X4** (page cap silent) — a MAX_PAGES cap hit now prints a warning naming what was deferred.

**⚠️ dispositioned / declined-with-reason**
- **X5 (cost basis)** — the card now states the real driver (up to `PAGE_SIZE` reads per launch, not just new-bookmark count) and marks per-post-vs-per-request billing as a portal unknown; the $10/mo cap is the backstop. `PAGE_SIZE` lowered 100→50.
- **Card flags 1–7** — all addressed in the setup card rewrite (who runs it / where, `.env` creation, start dir + which python, portal steps marked "as the portal appears — confirm", cost basis, a failure/troubleshooting section). Flag 1 (the false "start line" promise) is void under the exclusion-set model.

**Two cx cases that now "FAIL" BY DESIGN** (they encoded the old, wrong floor semantics this fix removed — NOT regressions):
- **CX1** asserted the numeric floor filters/sorts; the floor is retired, so `select_new` returns all-unseen in API order.
- **CX2 "pilot_start_id non-numeric"** asserted a non-numeric `pilot_start_id` is corrupt; it is now an opaque ISO timestamp marker, so `"abc"`-shaped values are valid.
Net on the reader's own file: **20 PASS / 2 FAIL (both by-design)**. Read-2 writes fresh counterexamples against this model.
