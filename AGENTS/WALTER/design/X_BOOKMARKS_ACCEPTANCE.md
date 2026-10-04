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
- **X5 (cost basis)** — see §7 for the corrected basis (newest-first until an all-seen page: **1–2 pages / up to ~100 posts on a normal launch, up to ~500 max**, plus a one-time seed read); per-post-vs-per-request billing is a portal unknown and the $10/mo cap is the backstop. `PAGE_SIZE` lowered 100→50. *(The earlier "up to PAGE_SIZE reads per launch" wording here was itself wrong — corrected read-3 N2.)*
- **Card flags 1–7** — all addressed in the setup card rewrite (who runs it / where, `.env` creation, start dir + which python, portal steps marked "as the portal appears — confirm", cost basis, a failure/troubleshooting section). Flag 1 (the false "start line" promise) is void under the exclusion-set model.

**Two cx cases that now "FAIL" BY DESIGN** (they encoded the old, wrong floor semantics this fix removed — NOT regressions):
- **CX1** asserted the numeric floor filters/sorts; the floor is retired, so `select_new` returns all-unseen in API order.
- **CX2 "pilot_start_id non-numeric"** asserted a non-numeric `pilot_start_id` is corrupt; it is now an opaque ISO timestamp marker, so `"abc"`-shaped values are valid.
Net on the reader's own file: **20 PASS / 2 FAIL (both by-design)**. Read-2 writes fresh counterexamples against this model.

## 7. Coldread read-2 dispositions (2026-10-03 — ❌2 / ⚠️13; read-1's four ❌ confirmed CLOSED)
Read-2 verdict NOT MET on `0fe87931c`. Disposition on the next fix commit:

**❌ fixed**
- **X6 (re-authorize consumed un-routed bookmarks)** — FIXED. The seed now runs ONLY on the first `--authorize` (no seen-file yet); a re-authorize refreshes tokens and touches neither `consumed` nor the stage. The refresh-failure message says so. cx2 **CX-B PASS**.
- **X5 (cost basis contradicted by the paging code)** — FIXED as an honesty fix: the card and §6 now state the real basis (newest-first until an all-seen page → **1–2 pages / up to ~100 posts on a normal launch, up to ~500 max**, plus a one-time seed read). The safe all-seen-page stop is kept (stopping at the first seen ID would drop a new bookmark sitting below a re-bookmarked one).

**⚠️ fixed**
- **A5 residual** — `load_seen`/`save_seen` now reject a `consumed` that isn't a list of scalars (CX-I1 PASS); `fetch_new_bookmarks` str-coerces seen ids so hand-edited int ids match the paging stop (CX-I2 mechanism fixed).
- **A8 residual** — test mode now REFUSES a partial or relative config instead of deriving onto a live file (CX-F/CX-F2 PASS); a new test asserts the live seen-file is byte-untouched during a test-mode write. "API input isolated": in test mode the `.env` is isolated → no real token → the network is never reached; documented here.
- **X9 (seed cap silent)** — the first-authorize seed now warns when the account exceeds `MAX_PAGES×PAGE_SIZE` (CX-A2 PASS).
- **X10 (idless item re-fires forever)** — an id-less item gets a stable `noid:<hash>` dedup key, so once routed and marked it stops re-firing (CX-J PASS).
- **X11 (inner-element guard)** — `save_seen` rejects a non-scalar element (an inner dict with text), explicit raise.
- **X12 (BOM `.env`)** — `load_env`/`rewrite_env` read with `utf-8-sig` (CX-H2 PASS).
- **Card flags 1, 2, 5, 6, 7** — fixed in the card: re-bookmark limit stated (1), refresh-failure is now safe + documented (2), portal banner marks facts "confirm on screen" (5), WSL2 localhost reachability called out as the one untested-live step (6), review clock tied to first successful scan not a fixed date (7).

**⚠️ dispositioned / declined-with-reason (recorded, not silently dropped)**
- **X7 stale stage (CX-D)** — MITIGATED, not fully enforced. The report run and `--mark` are **separate OS processes** by protocol (run tool → route → run `--mark`), so "a `--mark` with no report run in *this session*" cannot be detected by process identity. Mitigations: the stage carries a timestamp and `--mark` **refuses a stage >24h old or without a valid timestamp** and **prints the ids it is consuming (first 10, then "…")**; and a crash between report and mark self-heals — the un-routed items are still unseen, so the next report run re-surfaces and re-stages them (CX-D2 PASS). CX-D runs `--mark` seconds after the stage, so it is consumed (by design); the residual risk is an out-of-protocol blind `--mark`, now loud and bounded.
- **X8 re-bookmark invisible (CX-C)** — DOCUMENTED LIMIT (reader concurred). A post already in the seen-set won't re-surface if re-bookmarked; stated in the card ("send it by Telegram"). Changing this needs bookmark-event timestamps the endpoint doesn't give.
- **CX-I2 `api.calls==1`** — the int-coercion defect is fixed; the specific `==1` assertion isn't reachable for its fixture (598 genuinely-unseen bookmarks legitimately require paging, and the resulting cap warning is correct, not false).

Net on read-2's file: **15 PASS / 4 FAIL** (CX-C, CX-D, CX-E, CX-I2 — all dispositioned above). Read-1's file still **20 PASS / 2 FAIL** (unchanged by-design pair). A final read closes the episode; "working" still also needs the live first-run (L1–L2).

## 8. Read-3 completion note (WQ-229 — post-ceiling fix; NEVER merged)
Read-3 (the last in the episode's Review budget) verdict: **NOT MET on two small items, no ❌ in A1–A10; A1–A10 MET at unit scope.** X6 confirmed (re-authorize byte-identical ×4), A8 refusal 18/18, noid:hash 5/5, all four §7 declined reasons judged TRUE. The two ❌ lose no bookmark (N1 over-surfaces ≤~500 once; N2 is a document).

**This fix commit is the post-ceiling repair. Its WQ-229 state:**
- **IMPLEMENTED: YES** — N1 (seed-failure writes no seen-file, so the "re-run to seed" instruction is true), N2 (§6 cost line corrected), the no-timestamp/legacy/`staged_at≤0`/non-numeric stage guard (refuse), the int-id `--mark` TypeError (consumed normalized to str in `load_seen`; bool excluded), `pilot_start_id` type validated, card flag 5 ("confirm on screen" added), card L41 + seed-failure troubleshooting, the delete-then-authorize note, and the literal `cd` line.
- **TESTED (author): YES** — suite 28/28 (script + `-m unittest`); cx3 44/45 (the one FAIL, f3, is a by-design consequence of fixing f2 — 125 is now correctly consumed, so it does not re-surface); cx1 still 20/2; cx2 CX-A3 now raises FileNotFoundError because N1 deliberately no longer writes a seen-file on a failed seed (it tested the pre-N1 behavior; cx3 a5 supersedes it and PASSES).
- **INDEPENDENTLY VERIFIED: NO** — no read follows this commit within budget (a fourth read is Will's to name; PROME's rec is "not needed").
- **STILL UNRESOLVED after it: none known at unit scope.** The remaining gate is the **live first-run (L1–L2)** on Will's token + the WSL2-localhost answer; "working" is claimable only after that.

### LIVE FIRST-RUN RESULT — 2026-10-03 12:44 ET → ✅ WORKING
- **L1 (PKCE authorize): PASS** — flow completed; access+refresh tokens + `X_USER_ID` written to the gitignored `.env`.
- **L2 (real GET + dedup): PASS** — seed read **287** existing bookmarks across pages; a follow-up normal scan reads clean and reports "0 new bookmarks" (dedup holds end-to-end).
- **WSL2 localhost: WORKED** — the one untested piece. Will's Windows browser reached the WSL server at `localhost:8723`; callback caught, no timeout. (`webbrowser.open` failed headless as expected — harmless; he opened the relayed URL manually.)
- **Seed 287, under the 500 cap** (no cap warning). **N1 seed-failure path NOT exercised** — X granted $20 free credit, so the seed succeeded; N1 remains author-tested (cx3 a5), not live-observed.
- **Authorize was run from WALTER's session and the URL relayed to Will**; he approved in his own browser. Security identical (login never left his browser; only the read-only token reached WALTER). The card's "your own terminal" line is amended to a should-not-must.
- **L3 (expired-token refresh) — ✅ NOW EXERCISED LIVE 2026-10-03 ~19:25Z** (see LIVE UPDATE below). ⚠️ **NARROW:** only the expired-token RECOVERY+retry succeeded. **L3-FAILURE (a refresh that itself fails → re-authorize path), N1 (seed-failure), and L4 (429 AND network/other errors — not just rate-limit) remain UNtested live.**
- **STATUS: WORKING** at unit scope + live L1–L2 (+ L3-success). First-successful-scan 2026-10-03 → L599 two-week review 2026-10-17. WQ-377 boot-wiring now unblocked.

### LIVE UPDATE — L3 expired-token refresh, 2026-10-03 ~19:25Z (walter-f0 bookmark-backlog diagnostic)
During a read-only backlog pull (via a throwaway script that imported the tool's own `load_env`/`api_get_bookmarks`/`refresh_access_token`/`rewrite_env` and pointed `WALTER_X_ENV` at the LIVE `.env` so rotation would land correctly), the ~12:44 ET access token had expired. A real `GET /bookmarks` returned **401 → `refresh_access_token` succeeded → live `.env` rotated (new access+refresh) → retry succeeded** (`refreshed=True`, 100 bookmarks fetched). ⇒ **L3's success leg (expiry → one silent refresh → retry) is now LIVE-VALIDATED.** ⛔ **What is STILL untested:** the FAILURE leg of L3 (a refresh that fails must fail LOUD with a re-authorize instruction — the message exists, the live path has not fired); N1 (seed-failure writes no seen-file); L4 (429 *and* network errors fail LOUD, nothing marked). Do not paraphrase this as "only 429 remains."

## 9. Triage method (standing — apply when routing bookmark items; bought by the CATO review 2026-10-03)

**The failure this prevents (n=2, measured 2026-10-03):** a bookmarked image/link was classified "unassessable, offload to Will" WITHOUT trying the cheap retrieval — and both turned out to be high-value research (a JPM oil note read whole from 4 images; a PE-insurer entanglement analysis). The bottleneck was RELEVANCE-JUDGMENT/EFFORT, not retrieval. (n=2 shows the failure MODE exists and is cheap to fix — NOT its prevalence across the backlog, and NOT that any item is "most valuable"; the OWNER judges value.)

**Classify on TWO independent axes — never collapse them:**
- **Relevance bucket:** `financial-research` · `system-improvement` (Claude/tooling/method items that bear on how we operate — a concise list for Will, NOT auto-commissioned; DAEDALUS is a *candidate* destination, not the automatic owner) · `personal / no-action`.
- **Assessment status:** `assessed` · `not-assessed`. ⛔ **`not-assessed` ≠ `rejected`.** An item I could not read is not an item I judged irrelevant. Keep them in separate piles so inaccessible material never disappears into the rejection pile.

**Retrieval discipline:**
- **Pull media/link METADATA by default** (expand the fetch: `media.fields`, `entities`, `attachments.media_keys`). ⚠️ **The production scanner does NOT yet do this** (`tools/x_bookmarks_scan.py` `api_get_bookmarks` requests `created_at,author_id` only) — a bounded code change is OWED; until then, a one-off expanded fetch is required for any media/link item.
- **Attempt the underlying content when relevance is PLAUSIBLE** — not "read everything." `pbs.twimg.com/media/*` images are public (no auth); download + Read (vision) works. Expanded-entity `expanded_url`s are WebFetch-able. Keep obvious personal exclusions cheap.
- **Video:** record "no transcript obtained through the attempted route," NOT "cannot read video" — the limit is the route, not an absolute. A financial video (e.g. a BoJ/Yen doc) is `financial / not-assessed`, flagged for the owner, not dropped.

**Dispatch by CONSEQUENCE, not backlog-status:** an old/backlog item can carry an urgent missed development (the current Riyadh escalation came FROM the backlog). Actionable / decision-relevant → full tracked dispatch (BOARD + route_log + handoff + delivery_log), as a dated/partially-verified **research lead** with a concrete owner question (*adds evidence / contradicts / duplicates?*) and explicit provenance. Keep INFO recipients SELECTIVE.
- ⚠️ **NOTE is NOT a lighter dispatch.** Per §3.5.1/§3.5.3 of `BOARD_CONSUMPTION_SPEC.md`, a NOTE writes no delivery_log/route_log/BOARD row (invisible to the doctor's consumption checks) and is **non-actionable CONTEXT only**. Reuse it ONLY for genuinely non-actionable material — never as a cheap substitute for a tracked dispatch.

**Backlog signal-density + dual-lens (observed 2026-10-03, slices 1–5):** financial signal appeared **front-loaded in the most-recent bookmarks** this pass — slice 1 (items 1–30) routed 6; slices 4–5 (91–150) routed 0; the tail (151–299, financial content un-triaged, only system-lens-scanned) looked older (back to Feb–May) and dev-tooling/academic/personal. ⇒ **on THIS backlog the diminishing returns justified stopping the financial pass at 150** — a session-specific judgment on observed yield, **NOT a universal rule.** ⛔ **A 0-route slice is NOT self-certifying and must NOT be read as "the filter is healthy."** It can be healthy filtering OR an **under-assessment MISS** — proven HERE: **slice 2 was first called "0 routable / mostly noise" and in fact held the two highest-value finds** (the JPM note + the PE-insurer analysis), recovered only on expanded retrieval. So on a 0-route slice: **verify retrieval/effort was actually spent before concluding anything, AND do not manufacture a dispatch to justify the pull** (MEMORY #3) — both failure directions are live. Never auto-stop on "two zeros"; weigh observed yield, retrieval confidence, and what the tail's dates suggest. **Scan once through BOTH lenses:** the same backlog yields a near-empty financial pass AND a rich *system-improvement* pass (the dev-tooling posts that are "off-domain" for signals are on-domain for how we operate — the fleet runs on Claude Code). Record the second-lens finds as a curated list for Will → DAEDALUS (a candidate owner, not automatic). **Position drift:** a bookmark's position shifts as Will adds/removes; "item N" is not stable, so the resumable record is the triage file, not an index.

### 9a. The DIG-DEEPER decision — when to pull body/media/link vs triage on text (added 2026-10-04, WALTER; Will-directed in-session "know when to dig deeper or not"; bought by the 10/04 12-item batch)

**The failure this prevents (measured 2026-10-04):** a 12-item Will-bookmark batch was triaged ENTIRELY off tweet text — 0 secondary pulls. The scan display TRUNCATED long tweets and caches IDs only, so full text was not even retained. A by-ID re-pull recovered material signal already dispatched without it: junkbondanalyst's post (folded as low-value "background") actually carried **PJT hired for an amend-and-extend, some debt due in ~2 months, Term Loans due 2028 trading in the 50s, "Chapter 22?"**, and its two attached images were **screenshots of the paywalled Bloomberg + AFR source articles** (the "international ops" sale = the Australian arm: $511.7M revenue, after-tax profit fell to $42.3M, 220+ locations). A discretionary "dig if it seems worth it" step decays under batch volume (`[[finding_mechanize_the_cap_not_the_ritual]]`) — hence a TRIGGER rule, not a reminder.

**KEY MECHANIC (why digging is usually CHEAP):** a tweet's attached image is often the paywalled article SCREENSHOTTED, and `pbs.twimg.com` is reachable (HTTP 200) while the source — and even free primaries — are bot-walled. 2026-10-04: WebFetch 403'd on CNBC AND on the UKMTO 150-26 PDF; curl-with-browser-UA also 403'd on UKMTO; `pbs.twimg.com` images downloaded 200 and read via vision, bypassing the paywall. ⇒ **"dig deeper" is NOT "spend the expensive tool" — the image+vision path is free and often sufficient.**

**DIG (pull body/media/link BEFORE dispositioning) when ANY:**
- (a) the tweet is a POINTER, not the content — bare headline+link, "click here for full product" (UKMTO), "my thoughts here: [link]" (QTR); the signal lives behind the link/image.
- (b) the tweet TEXT is truncated (scan display cut it, or a long-form `note_tweet`) — you cannot triage what you cannot see.
- (c) it has attached MEDIA from a data/analytical account — the chart, or the screenshotted article, IS the signal.
- (d) a niche / OSINT / analytical account (the channel's high-value, non-redundant class: junkbondanalyst, specialist commentators, OSINT) — earns a look by default.
- (e) a PRIMARY-source pointer (UKMTO / SEC / regulator / operator / exchange) — the fleet most wants primaries, and the tweet is only the pointer.
- (f) an extraordinary or state-reversing claim needing verification (a "closed" / "struck" / "plague" claim).

**DON'T dig (triage on text, route LIGHT, and label it) when:**
- a tier-1 WIRE headline whose body a domain desk + the RESEARCH-INTAKE lane already collect (CNBC / WSJ / CNN) — route light (BOARD ID-diff or one info handoff), let the owner read the primary; do not spend the heavy tool on redundancy.
- pure opinion / commentary AFTER a glance (no kill on the lede — glance first).
- already-ours / dup (grep BOARD first — MEMORY rule 1b).

**Tool ladder — CHEAPEST FIRST; never fire the cost-bearing tool first:**
1. attached media → download `pbs.twimg.com/media/*` (free, reachable) + Read (vision). Bypasses paywalls when the tweet screenshots the article.
2. X-native link (article / thread / long-form) → X API `note_tweet` / `article` fields + media expansions (free, authenticated by the pilot token).
3. external link → WebFetch (free; frequently 403s on wires and primaries).
4. external link that 403'd AND cleared a DIG trigger (primary or high-value) → a bot-bypass tool (Bright Data MCP; cost-bearing; NO key in env as of 2026-10-04, so unavailable until provisioned). Standing OK for the primary / high-value class; ask otherwise. Do NOT use it on a redundant wire a desk already covers.

**Label the read-state on every routed card:** `body read` · `image read (paywall bypassed via screenshot)` · `headline-triaged, body unreachable (403)` — so confidence is honest and the recipient knows whether WALTER read what Will actually bookmarked. (The 10/04 batch omitted this; corrected here.)

**✅ SHIPPED 2026-10-04 (Will: "make it the default"):** `tools/x_bookmarks_scan.py` `api_get_bookmarks` now requests `note_tweet,entities` + `expansions=author_id,attachments.media_keys` + `media.fields=url,preview_image_url,type` + `user.fields=username` BY DEFAULT, and `parse_bookmark` carries `full_text` (untruncated note_tweet), `media` (urls), `links` (expanded external URLs, self/x.com excluded) and a per-item `dig` hint (`media` / `link` / `pointer`). The scan output prints the full body (1500-char cap vs the old 300), the media URLs and the external links inline, with a `[DIG: …]` tag. ⚠️ **SCOPE OF "default" (corrected after CATO review 2026-10-04): the FETCH is automatic — the scan SURFACES full text, media URLs and links as the INPUTS to a dig. It does NOT itself download images, invoke vision, or retrieve article bodies; those remain a SESSION step per the §9a tool ladder, and `--mark` does not establish they happened. The read-state label on each card is the (manual) record that they did.** The 1500-char cap still truncates very long note_tweets. **Dedup invariant:** `dedup_key` and the seen/mark set are byte-unchanged in every tested case (enrichment adds fields; the dedup basis `text` is untouched; `_dedup_key` keys on the tweet ID for real tweets) — this is tested coverage, NOT a proof of impossibility. Scope: `tweet.read` already covers note_tweet/media — no new OAuth scope, same request count. **CATO-review hardening (2026-10-04, same batch):** link filter is now HOST-based (the substring test wrongly dropped vox.com / fox.com / x.com-in-query); long-form `note_tweet.entities` links are now extracted; malformed `note_tweet`/`attachments`/`entities`/url-entry shapes degrade without raising (CX4b). Covered by 32 tests green (incl. `test_enrichment_populates_and_dedup_key_unchanged`, `test_link_filter_is_host_based_not_substring`, `test_long_form_note_tweet_links_extracted`, `test_malformed_enrichment_metadata_never_raises`) + live first-run 2026-10-04. **NOT done by design:** a "known-analytical-account" dig flag — needs a maintained list that would rot (`[[finding_freshness_check_cannot_catch_a_fresh_lie]]`). **Independently read — WQ-384, Will-ruled 2026-10-04 ("CATO review does count"):** CATO's review (`e9367f5a8`) IS the WQ-229 independent read of the default-dig enrichment. ⚠️ **It covers the ORIGINAL change (`6882d10b0`), NOT the post-review fixes (`f2af81d44`, the host-filter / never-raise / UKMTO-narrowing pass), which remain UNREVIEWED — disclosed as such, never called "independently verified" (`[[finding_a_correction_pass_is_unreviewed_work]]`). A fresh read of `f2af81d44` is the open thread if one is wanted.
