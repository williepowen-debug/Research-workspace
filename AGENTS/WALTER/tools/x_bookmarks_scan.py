#!/usr/bin/env python3
"""
x_bookmarks_scan.py — read Will's NEW X bookmarks and hand them to the signal path.

Sibling of phone_scan.py. Authority: WQ-373 RULED by Will 2026-10-03
("373 approved go with your recs"). Acceptance conditions:
  AGENTS/WALTER/design/X_BOOKMARKS_ACCEPTANCE.md
Setup card for Will's hands:
  AGENTS/WALTER/design/X_BOOKMARKS_SETUP_CARD.md

WHAT THIS IS
------------
Will bookmarks a post on X instead of screenshotting it. At a WALTER launch this
tool reads his bookmarks NEWER THAN the pilot-start floor, dedups on post ID, and
prints each new one for routing through the normal path (filter → BOARD → handoff
→ delivery_log, tagged `source: x-bookmark`). Phase 1 is Will's PRIMARY X channel
(his words 2026-10-03 09:31), not a side test.

🔴 GOVERNING PRINCIPLE (inherited from phone_scan): NEVER SILENTLY DROP A WILL SIGNAL.
Every failure mode here SURFACES rather than skips: a malformed API item, a missing
field, a token error — all reported LOUD and still handed over or stopped on, never
swallowed.

HARD BOUNDARIES (see acceptance §2)
-----------------------------------
- READ-ONLY. Scopes tweet.read users.read bookmark.read offline.access. NEVER bookmark.write.
- NO POST BODIES IN GIT. The seen-file holds post IDs ONLY. Post text is printed for
  routing and survives in BOARD as WALTER's own paraphrase — never persisted verbatim.
- TOKEN NEVER IN GIT. Everything secret lives in AGENTS/WALTER/.env (gitignored).
- NO UNATTENDED RUNS. Launch-time only; "regularly between launches" = WQ-369, out of scope.

USAGE
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --authorize   # one-time, in Will's browser
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py               # report NEW bookmarks
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --mark        # record them as seen (AFTER routing)

STATUS: BUILT, UNIT-TESTED (pure logic). PENDING an independent read (WQ-229) and a
live first-run on Will's token before it may be called "working" (acceptance §4).
The network/authorize paths (L1–L4) are exercised only by that live first-run.
"""
import argparse
import base64
import hashlib
import json
import os
import re
import secrets
import sys
import urllib.parse
from pathlib import Path

WALTER = Path(__file__).resolve().parent.parent

# --- paths, with test-mode isolation (phone_scan 2026-08-03 lesson: isolate the
#     seen-file too, never just the input) -------------------------------------
ENV_PATH = Path(os.environ.get("WALTER_X_ENV", WALTER / ".env"))
_DEFAULT_SEEN = WALTER / "registry" / "x_bookmarks_seen.json"
SEEN = Path(os.environ.get("WALTER_X_SEEN", _DEFAULT_SEEN))
_TEST_MODE = ("WALTER_X_ENV" in os.environ) or ("WALTER_X_SEEN" in os.environ)

# --- OAuth2 / API constants ---------------------------------------------------
AUTHORIZE_URL = "https://x.com/i/oauth2/authorize"
TOKEN_URL = "https://api.x.com/2/oauth2/token"
API_BASE = "https://api.x.com/2"
SCOPES = "tweet.read users.read bookmark.read offline.access"   # read-only; NO bookmark.write
REDIRECT_URI = os.environ.get("WALTER_X_REDIRECT", "http://localhost:8723/callback")
PAGE_SIZE = 100          # max_results ceiling for the bookmarks endpoint
MAX_PAGES = 10           # safety cap — a launch should never page forever


# ============================================================================
# PURE LOGIC  (no network; this is what test_x_bookmarks_scan.py exercises)
# ============================================================================
def load_env(path=ENV_PATH):
    """Parse a KEY=value .env into a dict. Missing file → {}. Blank/`#` lines ignored."""
    out = {}
    if not Path(path).exists():
        return out
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, _, v = s.partition("=")
        out[k.strip()] = v.strip()
    return out


def rewrite_env(updates, path=ENV_PATH):
    """
    Write `updates` into the .env, PRESERVING every other key, comment and blank line
    (acceptance A6). Keys already present are replaced in place; new keys are appended.
    Never prints token values. Writes with 0600 perms.
    """
    path = Path(path)
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    remaining = dict(updates)
    out = []
    for line in lines:
        s = line.strip()
        if s and not s.startswith("#") and "=" in s:
            k = s.split("=", 1)[0].strip()
            if k in remaining:
                out.append(f"{k}={remaining.pop(k)}")
                continue
        out.append(line)
    for k, v in remaining.items():
        out.append(f"{k}={v}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out) + "\n", encoding="utf-8")
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def load_seen(path=SEEN):
    """Seen-file holds post IDs ONLY (+ pilot_start_id). Corrupt → fail CLOSED (A5)."""
    path = Path(path)
    if not path.exists():
        return {"consumed": [], "pilot_start_id": None}
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
        d.setdefault("consumed", [])
        d.setdefault("pilot_start_id", None)
        return d
    except (json.JSONDecodeError, OSError) as e:
        sys.exit(f"REFUSING TO RUN: {path} is unreadable ({e}). Fix or delete it — "
                 f"deleting re-surfaces every new bookmark, which is the safe direction.")


def save_seen(seen, path=SEEN):
    """Persist IDs only. Asserts no stray post-text key ever leaks in (A7)."""
    path = Path(path)
    assert set(seen) <= {"consumed", "pilot_start_id"}, \
        f"seen-file would persist unexpected keys {set(seen) - {'consumed', 'pilot_start_id'}}"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(seen, indent=2) + "\n", encoding="utf-8")


def parse_bookmark(item, users_by_id):
    """
    Normalize one API tweet object. NEVER raises for content reasons — returns a
    `warn` list instead (A4). `users_by_id` maps author_id → username (from includes).
    """
    warn = []
    pid = item.get("id")
    if not pid:
        warn.append("MALFORMED: bookmark item has no `id` — surfaced, cannot dedup")
    author_id = item.get("author_id")
    username = users_by_id.get(author_id) if author_id else None
    if not username:
        warn.append(f"author @handle not resolved (author_id={author_id!r})")
    text = item.get("text")
    if not text or not text.strip():
        warn.append("EMPTY TEXT — bookmark carries no body")
        text = ""
    return {"id": str(pid) if pid else None, "author_id": author_id,
            "username": username, "created_at": item.get("created_at"),
            "text": text.strip(), "warn": warn}


def select_new(bookmarks, seen_ids, pilot_start_id):
    """
    Return bookmarks strictly NEWER than the pilot floor AND not already consumed,
    newest-first. IDs are snowflakes → compare as INTEGERS (A2), never strings.
    An unparseable/missing id is surfaced but cannot be deduped, so it is INCLUDED
    (never-silently-drop) with its warning intact.
    """
    floor = int(pilot_start_id) if pilot_start_id not in (None, "") else 0
    seen = set(str(s) for s in seen_ids)
    out = []
    for b in bookmarks:
        if b["id"] is None:
            out.append(b)              # malformed — surface, do not drop
            continue
        try:
            newer = int(b["id"]) > floor
        except (TypeError, ValueError):
            out.append(b)              # non-numeric id — surface
            continue
        if newer and b["id"] not in seen:
            out.append(b)
    out.sort(key=lambda b: (int(b["id"]) if (b["id"] and b["id"].isdigit()) else -1),
             reverse=True)
    return out


def format_boot_line(n_new, m_dispatched):
    """Acceptance A9 — the one-line boot-report shape PROME asked for (point b)."""
    return f"{n_new} new bookmark{'' if n_new == 1 else 's'} since last launch, {m_dispatched} dispatched"


# ============================================================================
# NETWORK  (live paths L1–L4; isolated so the pure logic above tests clean)
# ============================================================================
def _require_requests():
    try:
        import requests  # noqa
        return requests
    except ImportError:
        sys.exit("REFUSING: `requests` not importable. Run via .venv/bin/python3.")


def api_get_bookmarks(user_id, token, pagination_token=None):
    """One page of GET /2/users/:id/bookmarks. Returns (data, includes, meta). Raises on HTTP error."""
    requests = _require_requests()
    params = {"max_results": PAGE_SIZE,
              "tweet.fields": "created_at,author_id",
              "expansions": "author_id", "user.fields": "username"}
    if pagination_token:
        params["pagination_token"] = pagination_token
    r = requests.get(f"{API_BASE}/users/{user_id}/bookmarks",
                     headers={"Authorization": f"Bearer {token}"},
                     params=params, timeout=30)
    r.raise_for_status()
    j = r.json()
    users = {u["id"]: u["username"] for u in j.get("includes", {}).get("users", [])}
    return j.get("data", []), users, j.get("meta", {})


def refresh_access_token(client_id, refresh_token, client_secret=None):
    """
    POST grant_type=refresh_token. X ROTATES the refresh token, so the caller MUST
    persist both returned values (acceptance L3). Returns (access, new_refresh).
    """
    requests = _require_requests()
    data = {"grant_type": "refresh_token", "refresh_token": refresh_token, "client_id": client_id}
    auth = (client_id, client_secret) if client_secret else None  # confidential vs public(PKCE) client
    r = requests.post(TOKEN_URL, data=data, auth=auth, timeout=30)
    r.raise_for_status()
    j = r.json()
    return j["access_token"], j.get("refresh_token", refresh_token)


def fetch_new_bookmarks(env, seen):
    """
    Live orchestration (L2/L3): page the endpoint, refreshing once on 401, stopping
    early when a page is entirely at/under the pilot floor. Returns parsed, selected
    list. Fails LOUD on any unrecoverable error — nothing is marked on failure.
    """
    requests = _require_requests()
    user_id = env.get("X_USER_ID")
    token = env.get("X_BOOKMARK_ACCESS_TOKEN")
    if not (user_id and token):
        sys.exit("Not authorized yet. Run:  x_bookmarks_scan.py --authorize   (see setup card).")

    floor = int(seen.get("pilot_start_id") or 0)
    collected, refreshed, page_token = [], False, None
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
        # stop early once a whole page is at/under the floor (older than pilot start)
        ids = [int(p["id"]) for p in parsed if p["id"] and p["id"].isdigit()]
        if ids and max(ids) <= floor:
            break
        page_token = meta.get("next_token")
        if not page_token:
            break

    return select_new(collected, seen.get("consumed", []), seen.get("pilot_start_id"))


def do_authorize():
    """
    One-time OAuth2 PKCE flow (L1). Will opens the printed URL in HIS browser, logs
    into HIS X account, approves. WALTER never sees his password — only the resulting
    code, exchanged for tokens. Sets the pilot-start floor to his newest current
    bookmark so pre-existing bookmarks are excluded forever.
    """
    import http.server
    import threading
    import webbrowser
    requests = _require_requests()

    env = load_env()
    client_id = env.get("X_CLIENT_ID")
    if not client_id:
        sys.exit("Set X_CLIENT_ID in AGENTS/WALTER/.env first (from your X app). See the setup card.")
    client_secret = env.get("X_CLIENT_SECRET")  # only if you made a Confidential client

    verifier = secrets.token_urlsafe(64)
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
    state = secrets.token_urlsafe(16)
    q = urllib.parse.urlencode({
        "response_type": "code", "client_id": client_id, "redirect_uri": REDIRECT_URI,
        "scope": SCOPES, "state": state, "code_challenge": challenge, "code_challenge_method": "S256"})
    url = f"{AUTHORIZE_URL}?{q}"

    captured = {}

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            qs = urllib.parse.urlparse(self.path).query
            captured.update(urllib.parse.parse_qs(qs))
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>WALTER: authorization received. You can close this tab.</h2>")

        def log_message(self, *a):
            pass

    port = int(urllib.parse.urlparse(REDIRECT_URI).port or 8723)
    srv = http.server.HTTPServer(("localhost", port), Handler)
    threading.Thread(target=srv.handle_request, daemon=True).start()

    print("\nOpen this URL in YOUR browser (where you are logged into X), approve, done:\n")
    print(f"  {url}\n")
    try:
        webbrowser.open(url)
    except Exception:  # noqa — headless is fine, Will opens it manually
        pass
    print(f"Waiting for the redirect to {REDIRECT_URI} ...")
    srv.socket.settimeout(300)
    while "code" not in captured:
        pass  # handle_request already ran on the thread; loop exits when captured fills

    if captured.get("state", [None])[0] != state:
        sys.exit("STATE MISMATCH — aborting (possible CSRF). Re-run --authorize.")
    code = captured["code"][0]

    data = {"grant_type": "authorization_code", "code": code, "redirect_uri": REDIRECT_URI,
            "client_id": client_id, "code_verifier": verifier}
    auth = (client_id, client_secret) if client_secret else None
    r = requests.post(TOKEN_URL, data=data, auth=auth, timeout=30)
    r.raise_for_status()
    tok = r.json()
    access, refresh = tok["access_token"], tok.get("refresh_token")
    if not refresh:
        sys.exit("No refresh_token returned — is `offline.access` in the app's scopes?")

    me = requests.get(f"{API_BASE}/users/me",
                      headers={"Authorization": f"Bearer {access}"}, timeout=30)
    me.raise_for_status()
    user_id = me.json()["data"]["id"]

    rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": access, "X_BOOKMARK_REFRESH_TOKEN": refresh,
                 "X_USER_ID": user_id})

    # pilot floor = newest current bookmark, so everything already bookmarked is excluded
    try:
        data0, _u, _m = api_get_bookmarks(user_id, access)
        ids = [int(b["id"]) for b in data0 if b.get("id")]
        pilot = str(max(ids)) if ids else "0"
    except Exception as e:  # noqa
        pilot = "0"
        print(f"⚠️  could not read current bookmarks to set the floor ({e}); floor=0 "
              f"means the FIRST scan will surface existing bookmarks — re-set if unwanted.")
    seen = load_seen()
    seen["pilot_start_id"] = pilot
    save_seen(seen)
    print(f"\n✅ Authorized. user_id stored, pilot floor = {pilot}. Tokens are in {ENV_PATH} (gitignored).")
    print("   Next normal launch will pick up bookmarks you add from now on.")
    return 0


# ============================================================================
def main(argv=None):
    # argv defaults to sys.argv in normal use; tests pass an explicit list so a
    # runner's own flags (python -m unittest <path>, pytest -v) never leak into the
    # tool's parser and exit(2). (PROME-found 2026-10-03; acceptance A10 must hold
    # regardless of how the suite is launched.)
    ap = argparse.ArgumentParser(description="Read Will's new X bookmarks for routing.")
    ap.add_argument("--authorize", action="store_true", help="one-time OAuth2 PKCE setup (Will's browser)")
    ap.add_argument("--mark", action="store_true", help="record listed bookmarks as consumed (AFTER routing)")
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

    seen = load_seen()
    new = fetch_new_bookmarks(env, seen)

    n = len(new)
    print(f"\n[{format_boot_line(n, 'M')}]   (M = how many you route below)")
    if not n:
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

    if args.mark:
        for b in new:
            if b["id"]:
                seen["consumed"] = sorted(set(seen.get("consumed", [])) | {b["id"]})
        save_seen(seen)
        print(f"--mark: recorded {sum(1 for b in new if b['id'])} post ID(s) → {SEEN.name} (IDs only)")
    else:
        print("After routing, run:  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --mark")
    return 0


if __name__ == "__main__":
    sys.exit(main())
