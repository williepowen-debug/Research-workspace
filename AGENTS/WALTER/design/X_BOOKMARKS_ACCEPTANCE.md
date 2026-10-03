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
- **Pilot floor.** Only bookmarks **newer than the pilot-start marker** are ever processed; pre-existing bookmarks are excluded forever.

## 3. MUST conditions (acceptance matrix)

| # | Condition | How verified |
|---|---|---|
| A1 | `select_new()` returns only bookmarks with `id > pilot_start_id` AND not in the seen set, newest-first | unit test, mock items |
| A2 | Snowflake IDs compared as **integers**, not strings ("100" < "99" as strings is the trap) | unit test with cross-decade-length IDs |
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
