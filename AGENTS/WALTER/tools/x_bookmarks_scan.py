#!/usr/bin/env python3
"""
x_bookmarks_scan.py — read Will's NEW X bookmarks and hand them to the signal path.

Sibling of phone_scan.py. Authority: WQ-373 RULED by Will 2026-10-03.
Acceptance: AGENTS/WALTER/design/X_BOOKMARKS_ACCEPTANCE.md
Setup card:  AGENTS/WALTER/design/X_BOOKMARKS_SETUP_CARD.md

WHAT THIS IS
------------
Will bookmarks a post on X instead of screenshotting it. At a WALTER launch this
tool reads his bookmarks, drops the ones already consumed, and prints each NEW one
for routing (filter -> BOARD -> handoff -> delivery_log, tagged `source: x-bookmark`).
Phase 1 is Will's PRIMARY X channel (his words 2026-10-03 09:31).

🔴 GOVERNING PRINCIPLE (from phone_scan): NEVER SILENTLY DROP A WILL SIGNAL.

DEDUP MODEL (corrected 2026-10-03 after coldread read-1, WQ-229)
----------------------------------------------------------------
Bookmarks are deduped on a SEEN-SET of post IDs, never on a numeric "floor".
A snowflake ID encodes when a post was CREATED, not when Will BOOKMARKED it, so a
floor on post ID silently drops an OLD post he bookmarks today — his main use case
(read-1 X1 / CX7). Instead: `--authorize` seeds the seen-set with EVERY bookmark
that already exists (so pre-existing ones are excluded while the seen-file lives),
and every launch surfaces whatever is NOT in the seen-set, in the API's own
newest-bookmarked-first order. Deleting the seen-file re-surfaces everything — the
safe direction (over-surface, never drop).

--mark MODEL (corrected 2026-10-03, read-1 X2 / CX8b)
-----------------------------------------------------
The report run (no flag) STAGES the IDs it printed to a pending-file. `--mark`
consumes exactly that staged list and never re-fetches, so a bookmark added between
the report run and the mark run can never be consumed un-routed.

HARD BOUNDARIES (acceptance §2)
-------------------------------
- READ-ONLY. Scopes tweet.read users.read bookmark.read offline.access. NEVER bookmark.write.
- NO POST BODIES IN GIT. Seen-file and pending-file hold post IDs ONLY. Text is printed
  for routing and survives in BOARD as WALTER's own paraphrase, never persisted verbatim.
- TOKEN NEVER IN GIT. Secrets live in AGENTS/WALTER/.env (gitignored). A full token is
  never printed.
- NO UNATTENDED RUNS. Launch-time only ("regularly between launches" = WQ-369, out of scope).

USAGE
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --authorize   # one-time, in Will's browser
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py               # report NEW bookmarks (stages them)
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --mark        # consume the staged list (AFTER routing)

STATUS: BUILT, UNIT-TESTED (pure logic) + coldread read-1 fixes applied. NOT "working"
until read-2 closes and a live first-run on Will's token passes (acceptance §4). The
network/authorize paths (L1-L4) are exercised only by that live first-run.
"""
import argparse
import base64
import hashlib
import json
import os
import secrets
import sys
import time
import urllib.parse
from pathlib import Path

WALTER = Path(__file__).resolve().parent.parent

# --- paths, with ALL-OR-NOTHING test isolation --------------------------------
# read-1 A8/CX6: isolating only one of {env, seen} announced TEST MODE while a LIVE
# file stayed in use. Fix: if EITHER test var is set, isolate BOTH — the unset one
# is derived beside the set one, so a live file is never touched in test mode.
_ENV_SET = "WALTER_X_ENV" in os.environ
_SEEN_SET = "WALTER_X_SEEN" in os.environ
_TEST_MODE = _ENV_SET or _SEEN_SET
if _TEST_MODE:
    ENV_PATH = Path(os.environ["WALTER_X_ENV"]) if _ENV_SET else None
    SEEN = Path(os.environ["WALTER_X_SEEN"]) if _SEEN_SET else None
    _base = (ENV_PATH.parent if _ENV_SET else SEEN.parent)
    if ENV_PATH is None:
        ENV_PATH = _base / ".env"
    if SEEN is None:
        SEEN = _base / "x_bookmarks_seen.json"
else:
    ENV_PATH = WALTER / ".env"
    SEEN = WALTER / "registry" / "x_bookmarks_seen.json"

# --- OAuth2 / API constants ---------------------------------------------------
AUTHORIZE_URL = "https://x.com/i/oauth2/authorize"
TOKEN_URL = "https://api.x.com/2/oauth2/token"
API_BASE = "https://api.x.com/2"
SCOPES = "tweet.read users.read bookmark.read offline.access"   # read-only; NO bookmark.write
REDIRECT_URI = os.environ.get("WALTER_X_REDIRECT", "http://localhost:8723/callback")
PAGE_SIZE = 50           # bookmarks come newest-first; a launch's new ones are at the top
MAX_PAGES = 10           # safety cap; X4: a cap hit is WARNED, never silent


def _pending_path():
    """Staging file for the report->mark handoff. Beside the (possibly test) seen-file."""
    return Path(SEEN).parent / "x_bookmarks_pending.json"


# ============================================================================
# PURE LOGIC  (no network; this is what test_x_bookmarks_scan.py exercises)
# ============================================================================
def load_env(path=None):
    """Parse KEY=value .env into a dict. Missing file -> {}. Surrounding quotes stripped (CX3d)."""
    path = Path(path or ENV_PATH)
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, _, v = s.partition("=")
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
            v = v[1:-1]
        out[k.strip()] = v           # last occurrence wins (consistent with rewrite_env)
    return out


def rewrite_env(updates, path=None):
    """
    Write `updates` into the .env, preserving other keys, comments and blank lines
    (A6). ALL occurrences of an updated key collapse to ONE line (CX3b: no stale
    duplicate wins). Original CRLF/LF style preserved (CX3c). Atomic (temp+replace,
    CX3b/token-rotation safety). 0600 perms. Never prints token values.
    """
    path = Path(path or ENV_PATH)
    raw = path.read_bytes() if path.exists() else b""
    nl = "\r\n" if b"\r\n" in raw else "\n"
    lines = raw.decode("utf-8").split(nl) if raw else []
    if lines and lines[-1] == "":
        lines = lines[:-1]           # don't let split() add a phantom trailing element
    remaining = dict(updates)
    out = []
    for line in lines:
        s = line.strip()
        if s and not s.startswith("#") and "=" in s:
            k = s.split("=", 1)[0].strip()
            if k in updates:
                if k in remaining:
                    out.append(f"{k}={remaining.pop(k)}")   # first hit keeps position
                # any further duplicate lines for this key are dropped
                continue
        out.append(line)
    for k, v in remaining.items():
        out.append(f"{k}={v}")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes((nl.join(out) + nl).encode("utf-8"))
    try:
        os.chmod(tmp, 0o600)
    except OSError:
        pass
    os.replace(tmp, path)            # atomic


def _refuse(path, why):
    sys.exit(f"REFUSING TO RUN: {path} {why}. Delete it to re-surface every bookmark "
             f"(the safe direction — over-surface, never drop).")


def load_seen(path=None):
    """
    Seen-file holds post IDs (+ an opaque pilot marker). Any corruption -> REFUSE
    with a fix instruction (A5/CX2): bad bytes, bad JSON, non-object, or a
    `consumed` that is not a list all fail CLOSED and LOUD.
    """
    path = Path(path or SEEN)
    if not path.exists():
        return {"consumed": [], "pilot_start_id": None}
    try:
        raw = path.read_bytes()
    except OSError as e:
        _refuse(path, f"is unreadable ({e})")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        _refuse(path, f"is not valid UTF-8 ({e})")
    try:
        d = json.loads(text)
    except json.JSONDecodeError as e:
        _refuse(path, f"is not valid JSON ({e})")
    if not isinstance(d, dict):
        _refuse(path, "is not a JSON object")
    if not isinstance(d.get("consumed", []), list):
        _refuse(path, "`consumed` is not a list")
    d.setdefault("consumed", [])
    d.setdefault("pilot_start_id", None)
    return d


def save_seen(seen, path=None):
    """Persist post IDs only (A7). Refuse any stray key — a text leak must fail, not assert-away."""
    path = Path(path or SEEN)
    stray = set(seen) - {"consumed", "pilot_start_id"}
    if stray:                        # explicit check, not an `assert` (survives python -O)
        raise ValueError(f"seen-file would persist unexpected keys {stray}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"consumed": sorted(set(str(x) for x in seen["consumed"])),
                                "pilot_start_id": seen.get("pilot_start_id")}, indent=2) + "\n",
                    encoding="utf-8")


def load_pending(path=None):
    path = Path(path or _pending_path())
    if not path.exists():
        return []
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return []                    # a lost stage just means "nothing staged"; the report run re-stages
    return [str(x) for x in d] if isinstance(d, list) else []


def save_pending(ids, path=None):
    path = Path(path or _pending_path())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([str(i) for i in ids]) + "\n", encoding="utf-8")


def parse_bookmark(item, users_by_id):
    """
    Normalize one API tweet object. NEVER raises for content reasons (CX4b: a
    non-string `text` is coerced, not crashed) — returns a `warn` list instead (A4).
    An int id of 0 or a missing id is MALFORMED (id=None) and surfaced.
    """
    warn = []
    raw_id = item.get("id")
    pid = str(raw_id) if raw_id else None    # 0, "", None all -> malformed
    if pid is None:
        warn.append("MALFORMED: bookmark item has no usable `id` — surfaced, cannot dedup")
    author_id = item.get("author_id")
    username = users_by_id.get(author_id) if author_id else None
    if not username:
        warn.append(f"author @handle not resolved (author_id={author_id!r})")
    text = item.get("text")
    text = "" if text is None else str(text)
    if not text.strip():
        warn.append("EMPTY TEXT — bookmark carries no body")
    return {"id": pid, "author_id": author_id, "username": username,
            "created_at": item.get("created_at"), "text": text.strip(), "warn": warn}


def select_new(bookmarks, seen_ids, _unused=None):
    """
    Return bookmarks NOT already consumed, in the API's given order (newest-bookmarked
    first) — NO post-ID floor (read-1 X1), NO re-sort. A malformed (idless) item cannot
    be deduped, so it is always surfaced (never-silently-drop). `_unused` is a retired
    floor parameter kept only so old callers/counterexamples don't error on the arity.
    """
    seen = set(str(s) for s in seen_ids)
    return [b for b in bookmarks if b["id"] is None or b["id"] not in seen]


def format_boot_line(n_new, m_dispatched):
    """A9 — the one-line boot-report shape (PROME point b)."""
    return f"{n_new} new bookmark{'' if n_new == 1 else 's'} since last launch, {m_dispatched} dispatched"


# ============================================================================
# NETWORK  (live paths L1-L4; isolated so the pure logic above tests clean)
# ============================================================================
def _require_requests():
    try:
        import requests  # noqa
        return requests
    except ImportError:
        sys.exit("REFUSING: `requests` not importable. Run via .venv/bin/python3.")


def api_get_bookmarks(user_id, token, pagination_token=None):
    """One page of GET /2/users/:id/bookmarks. Returns (data, users, meta). Raises on HTTP error."""
    requests = _require_requests()
    params = {"max_results": PAGE_SIZE, "tweet.fields": "created_at,author_id",
              "expansions": "author_id", "user.fields": "username"}
    if pagination_token:
        params["pagination_token"] = pagination_token
    r = requests.get(f"{API_BASE}/users/{user_id}/bookmarks",
                     headers={"Authorization": f"Bearer {token}"}, params=params, timeout=30)
    r.raise_for_status()
    j = r.json()
    users = {u["id"]: u["username"] for u in j.get("includes", {}).get("users", [])}
    return j.get("data", []), users, j.get("meta", {})


def refresh_access_token(client_id, refresh_token, client_secret=None):
    """POST grant_type=refresh_token. X ROTATES the refresh token — caller MUST persist both (L3)."""
    requests = _require_requests()
    data = {"grant_type": "refresh_token", "refresh_token": refresh_token, "client_id": client_id}
    auth = (client_id, client_secret) if client_secret else None
    r = requests.post(TOKEN_URL, data=data, auth=auth, timeout=30)
    r.raise_for_status()
    j = r.json()
    return j["access_token"], j.get("refresh_token", refresh_token)


def fetch_new_bookmarks(env, seen):
    """
    Live orchestration (L2/L3): page the endpoint newest-first, refreshing once on
    401, stopping as soon as a whole page is already consumed. Fails LOUD on any
    unrecoverable error — nothing is marked on failure.
    """
    requests = _require_requests()
    user_id, token = env.get("X_USER_ID"), env.get("X_BOOKMARK_ACCESS_TOKEN")
    seen_ids = set(seen.get("consumed", []))
    collected, refreshed, page_token, capped = [], False, None, True
    for _ in range(MAX_PAGES):
        try:
            data, users, meta = api_get_bookmarks(user_id, token, page_token)
        except requests.HTTPError as e:
            code = e.response.status_code if e.response is not None else None
            if code == 401 and not refreshed:
                cid, rt = env.get("X_CLIENT_ID"), env.get("X_BOOKMARK_REFRESH_TOKEN")
                if not (cid and rt):
                    sys.exit("Access token rejected (401) and no refresh token on file — re-run --authorize.")
                try:
                    token, new_rt = refresh_access_token(cid, rt, env.get("X_CLIENT_SECRET"))
                except Exception as re_e:  # noqa
                    sys.exit(f"Token refresh FAILED ({re_e}). Re-run --authorize in Will's browser.")
                rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": token, "X_BOOKMARK_REFRESH_TOKEN": new_rt})
                env["X_BOOKMARK_ACCESS_TOKEN"], env["X_BOOKMARK_REFRESH_TOKEN"] = token, new_rt
                refreshed = True
                continue
            if code == 429:
                sys.exit("Rate-limited (429) by X. Nothing marked consumed. Retry at next launch.")
            sys.exit(f"X API error {code}. Nothing marked consumed. ({e})")
        except Exception as e:  # noqa — network/JSON
            sys.exit(f"Bookmark fetch failed ({e}). Nothing marked consumed.")

        parsed = [parse_bookmark(it, users) for it in data]
        collected.extend(parsed)
        page_ids = {p["id"] for p in parsed if p["id"]}
        if not page_ids or page_ids <= seen_ids:   # whole page already consumed -> stop
            capped = False
            break
        page_token = meta.get("next_token")
        if not page_token:
            capped = False
            break
    if capped:
        print(f"⚠️  paged the {MAX_PAGES}-page cap ({MAX_PAGES * PAGE_SIZE} bookmarks) without "
              f"reaching an all-consumed page — older new bookmarks beyond that are not shown "
              f"this launch; they will surface next launch.", flush=True)
    return select_new(collected, seen.get("consumed", []))


def _all_existing_bookmark_ids(user_id, token):
    """Seed set for --authorize: every current bookmark ID, so pre-existing ones are excluded."""
    ids, page_token = [], None
    for _ in range(MAX_PAGES):
        data, _u, meta = api_get_bookmarks(user_id, token, page_token)
        ids.extend(str(b["id"]) for b in data if b.get("id"))
        page_token = meta.get("next_token")
        if not page_token:
            break
    return ids


def do_authorize():
    """
    One-time OAuth2 PKCE flow (L1/X3). Will opens the printed URL in HIS browser, logs
    into HIS X account, approves. WALTER never sees his password — only the resulting
    code. Robust to Cancel/denial and to being piped: handles `error=`, waits on an
    Event with a deadline (no busy-loop), flushes before waiting.
    """
    import http.server
    import threading
    import webbrowser
    requests = _require_requests()

    env = load_env()
    client_id = env.get("X_CLIENT_ID")
    if not client_id:
        sys.exit("Set X_CLIENT_ID in AGENTS/WALTER/.env first (from your X app). See the setup card.")
    client_secret = env.get("X_CLIENT_SECRET")

    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
    state = secrets.token_urlsafe(16)
    url = f"{AUTHORIZE_URL}?" + urllib.parse.urlencode({
        "response_type": "code", "client_id": client_id, "redirect_uri": REDIRECT_URI,
        "scope": SCOPES, "state": state, "code_challenge": challenge, "code_challenge_method": "S256"})

    captured, done = {}, threading.Event()

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if "code" in q or "error" in q:
                captured.update({k: v[0] for k, v in q.items()})
                self.send_response(200)
                self.send_header("Content-Type", "text/html")
                self.end_headers()
                msg = ("authorization received — you can close this tab." if "code" in q
                       else f"authorization was cancelled or failed ({q.get('error', ['?'])[0]}).")
                self.wfile.write(f"<h2>WALTER: {msg}</h2>".encode())
                done.set()
            else:
                self.send_response(204)
                self.end_headers()

        def log_message(self, *a):
            pass

    port = int(urllib.parse.urlparse(REDIRECT_URI).port or 8723)
    srv = http.server.HTTPServer(("localhost", port), Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()

    print("\nOpen this URL in YOUR browser (where you are logged into X), approve, done:\n", flush=True)
    print(f"  {url}\n", flush=True)
    try:
        webbrowser.open(url)
    except Exception:  # noqa — headless is fine; Will opens it manually
        pass
    print(f"Waiting up to 5 min for the redirect to {REDIRECT_URI} ... (Ctrl-C to abort)", flush=True)
    done.wait(timeout=300)
    srv.shutdown()

    if "code" not in captured:
        if "error" in captured:
            sys.exit(f"Authorization was cancelled or denied ({captured['error']}). Re-run --authorize.")
        sys.exit("Timed out waiting for authorization (5 min). Re-run --authorize.")
    if captured.get("state") != state:
        sys.exit("STATE MISMATCH — aborting (possible CSRF). Re-run --authorize.")

    data = {"grant_type": "authorization_code", "code": captured["code"], "redirect_uri": REDIRECT_URI,
            "client_id": client_id, "code_verifier": verifier}
    auth = (client_id, client_secret) if client_secret else None
    tok = requests.post(TOKEN_URL, data=data, auth=auth, timeout=30)
    tok.raise_for_status()
    tok = tok.json()
    access, refresh = tok["access_token"], tok.get("refresh_token")
    if not refresh:
        sys.exit("No refresh_token returned — is `offline.access` among the app's scopes? Re-check and re-authorize.")

    me = requests.get(f"{API_BASE}/users/me", headers={"Authorization": f"Bearer {access}"}, timeout=30)
    me.raise_for_status()
    user_id = me.json()["data"]["id"]
    rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": access, "X_BOOKMARK_REFRESH_TOKEN": refresh, "X_USER_ID": user_id})

    # seed the seen-set with EVERY existing bookmark so pre-existing ones are excluded
    try:
        existing = _all_existing_bookmark_ids(user_id, access)
    except Exception as e:  # noqa
        existing = []
        print(f"⚠️  could not read current bookmarks to seed the exclusion set ({e}); the FIRST "
              f"scan will surface your EXISTING bookmarks. Re-run --authorize once reachable to seed.",
              flush=True)
    seen = load_seen()
    seen["consumed"] = sorted(set(seen["consumed"]) | set(existing))
    seen["pilot_start_id"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    save_seen(seen)
    print(f"\n✅ Authorized. {len(existing)} existing bookmark(s) seeded as already-seen. "
          f"Tokens in {ENV_PATH} (gitignored).", flush=True)
    print("   From now on, bookmarks you add are surfaced at the next launch — including older "
          "posts you bookmark today.", flush=True)
    return 0


# ============================================================================
def main(argv=None):
    # argv defaults to sys.argv in normal use; tests pass an explicit list so a
    # runner's own flags never leak into the parser (PROME-found 2026-10-03; A10).
    ap = argparse.ArgumentParser(description="Read Will's new X bookmarks for routing.")
    ap.add_argument("--authorize", action="store_true", help="one-time OAuth2 PKCE setup (Will's browser)")
    ap.add_argument("--mark", action="store_true", help="consume the staged list (AFTER routing)")
    args = ap.parse_args(argv)

    if args.authorize:
        return do_authorize()

    print("X-BOOKMARK scan — Will's new bookmarks")
    print("=" * 64)
    if _TEST_MODE:
        print(f"⚠️  TEST MODE — env={ENV_PATH}  seen={SEEN} (isolated, NOT live state)")

    env = load_env()
    if not env.get("X_BOOKMARK_ACCESS_TOKEN"):
        print("\n[status] Not authorized yet — no token in .env. This is NOT an error.")
        print("         Run:  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --authorize")
        print("         (one-time, in Will's browser — see design/X_BOOKMARKS_SETUP_CARD.md)")
        return 0
    if not env.get("X_USER_ID"):
        # CX5b: half-authorized (token but no user id) is a clean re-authorize prompt, not a crash
        print("\n[status] Partially authorized — token present but no X_USER_ID. Re-run --authorize.")
        return 0

    seen = load_seen()

    if args.mark:
        pending = load_pending()
        if not pending:
            print("\n[--mark] nothing staged. Run without --mark first, route, then --mark.")
            return 0
        seen["consumed"] = sorted(set(seen.get("consumed", [])) | set(pending))
        save_seen(seen)
        save_pending([])                      # clear the stage
        print(f"\n--mark: consumed {len(pending)} staged post ID(s) → {SEEN.name} (IDs only).")
        return 0

    new = fetch_new_bookmarks(env, seen)
    n = len(new)
    print(f"\n[{format_boot_line(n, 'M')}]   (M = how many you route below)")
    if not n:
        save_pending([])
        print("[NEW bookmarks — 0]  (nothing to route)")
        return 0

    print(f"\n[NEW bookmarks to ROUTE — {n}]  source: x-bookmark  (Will-originated — "
          "do not kill on Novelty without reading the body)\n")
    for i, b in enumerate(new, 1):
        who = f"@{b['username']}" if b["username"] else f"author_id:{b['author_id']}"
        print(f"  {i}. {b['id']}  {who}  {b['created_at'] or '—'}")
        for w in b["warn"]:
            print(f"     ⚠️  {w}")
        preview = b["text"].replace("\n", " ")
        print(f"     │ {preview[:300]}{'…' if len(preview) > 300 else ''}\n")

    save_pending([b["id"] for b in new if b["id"]])    # stage for --mark (IDs only)
    print("After routing, run:  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --mark")
    return 0


if __name__ == "__main__":
    sys.exit(main())
