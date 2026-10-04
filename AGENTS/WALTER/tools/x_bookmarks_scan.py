#!/usr/bin/env python3
"""
x_bookmarks_scan.py — read Will's NEW X bookmarks and hand them to the signal path.

Sibling of phone_scan.py. Authority: WQ-373 RULED by Will 2026-10-03.
Acceptance: AGENTS/WALTER/design/X_BOOKMARKS_ACCEPTANCE.md
Setup card:  AGENTS/WALTER/design/X_BOOKMARKS_SETUP_CARD.md

WHAT THIS IS
------------
Will bookmarks a post on X instead of screenshotting it. At a WALTER launch this tool
reads his bookmarks, drops the ones already consumed, and prints each NEW one for
routing (filter -> BOARD -> handoff -> delivery_log, tagged `source: x-bookmark`).
Phase 1 is Will's PRIMARY X channel (his words 2026-10-03 09:31).

🔴 GOVERNING PRINCIPLE (from phone_scan): NEVER SILENTLY DROP A WILL SIGNAL.

DEDUP MODEL (exclusion-set; corrected across coldread reads 1 & 2, WQ-229)
--------------------------------------------------------------------------
Dedup is membership in a SEEN-SET of dedup-keys (a post ID, or for a rare id-less API
item a content hash), never a numeric "floor" — a snowflake is creation time, not
bookmark time (read-1 X1). The seen-set is seeded ONCE, at the FIRST `--authorize`,
with every bookmark that already exists; a RE-authorize refreshes tokens and touches
NEITHER the seen-set NOR the stage (read-2 X6 — re-seeding would consume a bookmark
Will added since the last launch, and the tool's own refresh-recovery sends him to
re-authorize). Deleting the seen-file has TWO outcomes: delete then run a normal scan
re-surfaces everything to route (safe); delete then --authorize re-seeds from scratch
(marks all current bookmarks seen) — only do the latter to start over.

--mark MODEL (read-1 X2 / read-2 X7)
------------------------------------
The report run STAGES the dedup-keys it printed (with a timestamp); `--mark` consumes
exactly that stage and never re-fetches. `--mark` prints what it is consuming and
refuses a stale stage (>24h). Across a crash the un-routed items re-surface at the
next report run (self-healing), so nothing is lost.

HARD BOUNDARIES (acceptance §2)
-------------------------------
- READ-ONLY. Scopes tweet.read users.read bookmark.read offline.access. NEVER bookmark.write.
- NO POST BODIES IN GIT. Seen-file and stage hold dedup-keys ONLY. Text is printed for
  routing and survives in BOARD as WALTER's own paraphrase, never persisted verbatim.
- TOKEN NEVER IN GIT. Secrets live in AGENTS/WALTER/.env (gitignored). A full token is
  never printed.
- NO UNATTENDED RUNS. Launch-time only. ("Regularly between launches" is a separate,
  UNREGISTERED WALTER-autonomy question, out of scope — NOT WQ-369, whose registered scope is
  narrowly "PROME wakes a dark desk on urgent in-theater news".)

USAGE
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --authorize   # one-time, in Will's browser
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py               # report NEW bookmarks (stages them)
  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --mark        # consume the staged list (AFTER routing)

STATUS: BUILT + unit-tested + coldread reads 1&2 fixes applied. NOT "working" until a
final read closes and a live first-run on Will's token passes (acceptance §4).
"""
import argparse
import base64
import hashlib
import json
import os
import re
import secrets
import sys
import time
import urllib.parse
from pathlib import Path

WALTER = Path(__file__).resolve().parent.parent

# --- paths, with ALL-OR-NOTHING, ABSOLUTE test isolation ----------------------
# read-2 A8/CX-F: deriving the unset path beside a RELATIVE set path could land on the
# LIVE .env under a TEST MODE banner. Fix: test mode requires BOTH vars, both ABSOLUTE,
# or it refuses — so a live file can never be touched in a test. Production (neither
# set) uses the real paths.
_ENV_SET = "WALTER_X_ENV" in os.environ
_SEEN_SET = "WALTER_X_SEEN" in os.environ
_TEST_MODE = _ENV_SET or _SEEN_SET
if _TEST_MODE:
    if not (_ENV_SET and _SEEN_SET):
        sys.exit("REFUSING: test mode needs BOTH WALTER_X_ENV and WALTER_X_SEEN set, so no "
                 "live file is ever used under a test banner. Set both (to absolute paths).")
    ENV_PATH = Path(os.environ["WALTER_X_ENV"])
    SEEN = Path(os.environ["WALTER_X_SEEN"])
    if not (ENV_PATH.is_absolute() and SEEN.is_absolute()):
        sys.exit("REFUSING: WALTER_X_ENV and WALTER_X_SEEN must be ABSOLUTE paths in test mode "
                 "(a relative path resolves against cwd and can hit a live file).")
else:
    ENV_PATH = WALTER / ".env"
    SEEN = WALTER / "registry" / "x_bookmarks_seen.json"

# --- OAuth2 / API constants ---------------------------------------------------
AUTHORIZE_URL = "https://x.com/i/oauth2/authorize"
TOKEN_URL = "https://api.x.com/2/oauth2/token"
API_BASE = "https://api.x.com/2"
SCOPES = "tweet.read users.read bookmark.read offline.access"   # read-only; NO bookmark.write
REDIRECT_URI = os.environ.get("WALTER_X_REDIRECT", "http://localhost:8723/callback")
PAGE_SIZE = 50
MAX_PAGES = 10           # safety cap; a cap hit is WARNED (fetch AND seed), never silent
STAGE_MAX_AGE_S = 24 * 3600   # --mark refuses a stage older than this (crash-stale guard)


def _pending_path():
    return Path(SEEN).parent / "x_bookmarks_pending.json"


# ============================================================================
# PURE LOGIC  (no network; this is what test_x_bookmarks_scan.py exercises)
# ============================================================================
def load_env(path=None):
    """Parse KEY=value .env -> dict. Missing file -> {}. Tolerates a UTF-8 BOM (CX-H2);
    strips surrounding quotes (CX3d); last occurrence wins (consistent with rewrite_env)."""
    path = Path(path or ENV_PATH)
    out = {}
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8-sig").splitlines():   # utf-8-sig eats a BOM
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, _, v = s.partition("=")
        v = v.strip()
        if len(v) >= 2 and v[0] == v[-1] and v[0] in ("'", '"'):
            v = v[1:-1]
        out[k.strip()] = v
    return out


def rewrite_env(updates, path=None):
    """Write `updates`, preserving other keys/comments; duplicate keys collapse to one
    (CX3b); CRLF preserved (CX3c); atomic temp+replace; 0600. Never prints token values."""
    path = Path(path or ENV_PATH)
    raw = path.read_bytes() if path.exists() else b""
    nl = "\r\n" if b"\r\n" in raw else "\n"
    lines = raw.decode("utf-8-sig").split(nl) if raw else []
    if lines and lines[-1] == "":
        lines = lines[:-1]
    remaining = dict(updates)
    out = []
    for line in lines:
        s = line.strip()
        if s and not s.startswith("#") and "=" in s:
            k = s.split("=", 1)[0].strip()
            if k in updates:
                if k in remaining:
                    out.append(f"{k}={remaining.pop(k)}")
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
    os.replace(tmp, path)


def _refuse(path, why):
    sys.exit(f"REFUSING TO RUN: {path} {why}. Delete it to re-surface every bookmark "
             f"(the safe direction — over-surface, never drop).")


def _scalar_ids_ok(xs):
    # bool is an int subclass — exclude it so `True` can't masquerade as an id (read-3 e5)
    return isinstance(xs, list) and all(isinstance(x, (str, int)) and not isinstance(x, bool) for x in xs)


def load_seen(path=None):
    """Seen-file holds dedup-keys (+ an opaque pilot marker). Any corruption REFUSES
    with a fix instruction (A5/CX2): bad bytes/JSON, non-object, or a `consumed` that is
    not a list of SCALARS (CX-I1: a nested list would later crash --mark)."""
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
    if not _scalar_ids_ok(d.get("consumed", [])):
        _refuse(path, "`consumed` is not a list of plain id values")
    if not isinstance(d.get("pilot_start_id"), (str, type(None))):
        _refuse(path, "`pilot_start_id` is not a string")
    d.setdefault("consumed", [])
    d.setdefault("pilot_start_id", None)
    d["consumed"] = [str(x) for x in d["consumed"]]   # normalize so --mark never mixes int/str (read-3 f2)
    return d


def save_seen(seen, path=None):
    """Persist dedup-keys only (A7/X11). Reject a stray key AND a non-scalar element
    (an inner dict with text would leak a body), with an explicit raise (survives -O)."""
    path = Path(path or SEEN)
    stray = set(seen) - {"consumed", "pilot_start_id"}
    if stray:
        raise ValueError(f"seen-file would persist unexpected keys {stray}")
    if not _scalar_ids_ok(seen.get("consumed", [])):
        raise ValueError("`consumed` must be a list of plain id values (no nested structures)")
    if not isinstance(seen.get("pilot_start_id"), (str, type(None))):
        raise ValueError("`pilot_start_id` must be a string or null")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"consumed": sorted(set(str(x) for x in seen["consumed"])),
                                "pilot_start_id": seen.get("pilot_start_id")}, indent=2) + "\n",
                    encoding="utf-8")


def load_pending(path=None):
    """Return the staged dedup-key list (IDs only). A lost/garbled stage -> []."""
    path = Path(path or _pending_path())
    if not path.exists():
        return []
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return []
    if isinstance(d, dict):
        d = d.get("ids", [])
    return [str(x) for x in d] if isinstance(d, list) else []


def pending_stamp(path=None):
    """Epoch seconds the current stage was written, or None."""
    path = Path(path or _pending_path())
    if not path.exists():
        return None
    try:
        d = json.loads(path.read_text(encoding="utf-8"))
        return d.get("staged_at") if isinstance(d, dict) else None
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return None


def save_pending(ids, path=None):
    path = Path(path or _pending_path())
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"ids": [str(i) for i in ids], "staged_at": int(time.time())}) + "\n",
                    encoding="utf-8")


def _dedup_key(raw_id, author_id, created_at, text):
    if raw_id:
        return str(raw_id)
    basis = f"{author_id}|{created_at}|{text}"           # stable key for a rare id-less item (X10)
    return "noid:" + hashlib.sha256(basis.encode()).hexdigest()[:16]


def _host_of(url):
    try:
        netloc = urllib.parse.urlparse(url).netloc.lower()
    except Exception:  # noqa
        return ""
    netloc = netloc.split("@")[-1].split(":")[0]          # strip userinfo + port
    return netloc[4:] if netloc.startswith("www.") else netloc


def _is_self_or_shortener(url):
    """True for the tweet's own platform host or the t.co shortener — a HOST match, never a
    substring. The old `"x.com" in url` test wrongly dropped vox.com / fox.com / any URL with
    `x.com` in a query string (CATO review 2026-10-04)."""
    h = _host_of(url)
    return (h in ("x.com", "twitter.com", "mobile.twitter.com", "t.co")
            or h.endswith(".x.com") or h.endswith(".twitter.com"))


def _url_entities(container):
    """urls[] from an entities dict; tolerates ANY malformed shape without raising (CX4b)."""
    if not isinstance(container, dict):
        return []
    ent = container.get("entities")
    urls = ent.get("urls") if isinstance(ent, dict) else None
    return urls if isinstance(urls, list) else []


def _collect_links(item):
    """External links from BOTH top-level entities AND long-form note_tweet.entities
    (long-form posts carry their URLs only in note_tweet — CATO review 2026-10-04)."""
    links, note = [], item.get("note_tweet")
    for u in _url_entities(item) + _url_entities(note):
        if not isinstance(u, dict):
            continue
        exp = u.get("expanded_url") or u.get("url")
        if isinstance(exp, str) and exp and not _is_self_or_shortener(exp) and exp not in links:
            links.append(exp)
    return links


def parse_bookmark(item, users_by_id, media_by_key=None):
    """Normalize one API tweet object. NEVER raises for content reasons (CX4b). An id of
    0/''/None is MALFORMED (id=None) but still gets a stable `dedup_key` so it can be
    consumed and stops re-firing once marked (read-2 X10)."""
    warn = []
    raw_id = item.get("id")
    pid = str(raw_id) if raw_id else None
    if pid is None:
        warn.append("MALFORMED: bookmark item has no usable `id` — surfaced via a content key")
    author_id = item.get("author_id")
    username = users_by_id.get(author_id) if author_id else None
    if not username:
        warn.append(f"author @handle not resolved (author_id={author_id!r})")
    text = item.get("text")
    text = "" if text is None else str(text)
    if not text.strip():
        warn.append("EMPTY TEXT — bookmark carries no body")
    created_at = item.get("created_at")
    # --- enrichment (2026-10-04, §9a "dig by default"; hardened per CATO review): full text,
    # media, links + DIG hints. dedup_key stays on the ORIGINAL `text`, so in every tested case
    # the seen/mark set is byte-unchanged. Every read below tolerates a MALFORMED shape without
    # raising (CX4b). These are the INPUTS to a dig — the image-vision / body fetch itself is a
    # session step per §9a, NOT performed here.
    note = item.get("note_tweet")
    full_text = (note.get("text") if isinstance(note, dict) else None) or text
    full_text = str(full_text).strip()
    media_by_key = media_by_key if isinstance(media_by_key, dict) else {}
    att = item.get("attachments")
    mkeys = att.get("media_keys") if isinstance(att, dict) else None
    media = []
    for k in (mkeys if isinstance(mkeys, list) else []):
        m = media_by_key.get(k) if isinstance(k, (str, int)) and not isinstance(k, bool) else None
        m = m if isinstance(m, dict) else {}
        media.append({"type": m.get("type"), "url": m.get("url") or m.get("preview_image_url")})
    links = _collect_links(item)
    body_wo_links = re.sub(r"https?://\S+", "", full_text).strip()
    dig = []
    if media:
        dig.append("media")
    if links:
        dig.append("link")
    if links and len(body_wo_links) < 120:
        dig.append("pointer")   # headline+link: the signal lives behind the link, not the text
    return {"id": pid, "dedup_key": _dedup_key(raw_id, author_id, created_at, text.strip()),
            "author_id": author_id, "username": username, "created_at": created_at,
            "text": text.strip(), "full_text": full_text, "media": media, "links": links,
            "dig": dig, "warn": warn}


def select_new(bookmarks, seen_ids, _unused=None):
    """Bookmarks whose dedup_key is NOT consumed, in the API's given order. No floor, no
    re-sort. `_unused` is a retired floor arg kept for old-caller arity."""
    seen = set(str(s) for s in seen_ids)
    return [b for b in bookmarks if b["dedup_key"] not in seen]


def format_boot_line(n_new, m_dispatched):
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
    requests = _require_requests()
    params = {"max_results": PAGE_SIZE,
              "tweet.fields": "created_at,author_id,note_tweet,entities",
              "expansions": "author_id,attachments.media_keys",
              "media.fields": "url,preview_image_url,type",
              "user.fields": "username"}
    if pagination_token:
        params["pagination_token"] = pagination_token
    r = requests.get(f"{API_BASE}/users/{user_id}/bookmarks",
                     headers={"Authorization": f"Bearer {token}"}, params=params, timeout=30)
    r.raise_for_status()
    j = r.json()
    inc = j.get("includes", {})
    users = {u["id"]: u["username"] for u in inc.get("users", [])}
    media = {m["media_key"]: m for m in inc.get("media", []) if m.get("media_key")}
    return j.get("data", []), users, media, j.get("meta", {})


def refresh_access_token(client_id, refresh_token, client_secret=None):
    requests = _require_requests()
    data = {"grant_type": "refresh_token", "refresh_token": refresh_token, "client_id": client_id}
    auth = (client_id, client_secret) if client_secret else None
    r = requests.post(TOKEN_URL, data=data, auth=auth, timeout=30)
    r.raise_for_status()
    j = r.json()
    return j["access_token"], j.get("refresh_token", refresh_token)


def fetch_new_bookmarks(env, seen):
    """Page newest-first, refresh once on 401, stop as soon as a whole page is already
    consumed. seen-keys coerced to str so hand-edited int IDs still match (CX-I2). Fails
    LOUD on any unrecoverable error — nothing marked on failure."""
    requests = _require_requests()
    user_id, token = env.get("X_USER_ID"), env.get("X_BOOKMARK_ACCESS_TOKEN")
    seen_ids = set(str(s) for s in seen.get("consumed", []))
    collected, refreshed, page_token, capped = [], False, None, True
    for _ in range(MAX_PAGES):
        try:
            data, users, media, meta = api_get_bookmarks(user_id, token, page_token)
        except requests.HTTPError as e:
            code = e.response.status_code if e.response is not None else None
            if code == 401 and not refreshed:
                cid, rt = env.get("X_CLIENT_ID"), env.get("X_BOOKMARK_REFRESH_TOKEN")
                if not (cid and rt):
                    sys.exit("Access token rejected (401) and no refresh token on file — re-run --authorize.")
                try:
                    token, new_rt = refresh_access_token(cid, rt, env.get("X_CLIENT_SECRET"))
                except Exception as re_e:  # noqa
                    sys.exit(f"Token refresh FAILED ({re_e}). Re-run --authorize in Will's browser "
                             "(a re-authorize does NOT discard bookmarks you have not routed yet).")
                rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": token, "X_BOOKMARK_REFRESH_TOKEN": new_rt})
                env["X_BOOKMARK_ACCESS_TOKEN"], env["X_BOOKMARK_REFRESH_TOKEN"] = token, new_rt
                refreshed = True
                continue
            if code == 429:
                sys.exit("Rate-limited (429) by X. Nothing marked consumed. Retry at next launch.")
            sys.exit(f"X API error {code}. Nothing marked consumed. ({e})")
        except Exception as e:  # noqa
            sys.exit(f"Bookmark fetch failed ({e}). Nothing marked consumed.")

        parsed = [parse_bookmark(it, users, media) for it in data]
        collected.extend(parsed)
        page_keys = {p["dedup_key"] for p in parsed}
        if not page_keys or page_keys <= seen_ids:
            capped = False
            break
        page_token = meta.get("next_token")
        if not page_token:
            capped = False
            break
    if capped:
        print(f"⚠️  reached the {MAX_PAGES}-page read cap ({MAX_PAGES * PAGE_SIZE} bookmarks) without "
              f"hitting an all-seen page — any older new bookmarks beyond that surface next launch.",
              flush=True)
    return select_new(collected, seen.get("consumed", []))


def _all_existing_bookmark_ids(user_id, token):
    """Seed set for the FIRST --authorize. Returns (ids, capped) — capped True if the
    account has more bookmarks than MAX_PAGES*PAGE_SIZE could read (read-2 X9)."""
    ids, page_token, capped = [], None, True
    for _ in range(MAX_PAGES):
        data, _u, _m, meta = api_get_bookmarks(user_id, token, page_token)
        ids.extend(str(b["id"]) for b in data if b.get("id"))
        page_token = meta.get("next_token")
        if not page_token:
            capped = False
            break
    return ids, capped


def do_authorize():
    """One-time OAuth2 PKCE flow (L1/X3). Will approves in HIS browser; WALTER never sees
    his password. Robust to Cancel/denial/piping. SEEDS the seen-set only on the FIRST
    authorize; a re-authorize refreshes tokens and leaves the seen-set + stage alone (X6)."""
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
    except Exception:  # noqa
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

    # X6: seed ONLY on the first authorize (no seen-file). A re-authorize must not touch
    # the seen-set or the stage, or it would consume bookmarks added since the last launch.
    if Path(SEEN).exists():
        print(f"\n✅ Re-authorized. Tokens refreshed in {ENV_PATH}. Your seen-set and any staged "
              f"bookmarks are untouched — nothing waiting to be routed was consumed.", flush=True)
        return 0
    try:
        existing, capped = _all_existing_bookmark_ids(user_id, access)
    except Exception as e:  # noqa
        # N1 (read-3): do NOT write a seen-file on a failed seed. Leaving it absent keeps this a
        # "first authorize", so the re-run the message promises ACTUALLY re-seeds (otherwise the
        # re-run returns early at the Path(SEEN).exists() guard above and never seeds).
        print(f"⚠️  could not read your current bookmarks to seed the exclusion set ({e}). "
              f"NOTHING was marked seen and NO seen-file was written — re-run --authorize once "
              f"reachable and it WILL seed. Until then a normal scan surfaces your existing "
              f"bookmarks (safe, possibly noisy).", flush=True)
        return 1
    seen = {"consumed": sorted(set(existing)), "pilot_start_id": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    save_seen(seen)
    print(f"\n✅ Authorized. {len(existing)} existing bookmark(s) seeded as already-seen. "
          f"Tokens in {ENV_PATH} (gitignored).", flush=True)
    if capped:
        print(f"⚠️  you have MORE than {MAX_PAGES * PAGE_SIZE} bookmarks — only the most-recent "
              f"{MAX_PAGES * PAGE_SIZE} were seeded; older ones may surface at the first scan (safe, "
              f"but possibly noisy — tell WALTER if so).", flush=True)
    print("   From now on, bookmarks you add are surfaced at the next launch — including older "
          "posts you bookmark today.", flush=True)
    return 0


# ============================================================================
def main(argv=None):
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
        print("\n[status] Partially authorized — token present but no X_USER_ID. Re-run --authorize.")
        return 0

    seen = load_seen()

    if args.mark:
        pending = load_pending()
        if not pending:
            print("\n[--mark] nothing staged. Run without --mark first, route, then --mark.")
            return 0
        stamp = pending_stamp()
        # read-3 b3/b4/b5/b6: a stage with no timestamp, the legacy list form, staged_at<=0, or a
        # non-numeric stamp is UNVERIFIABLE — refuse rather than fail open. bool excluded (int subclass).
        if not isinstance(stamp, (int, float)) or isinstance(stamp, bool) or stamp <= 0:
            print("\n[--mark] REFUSING: the stage has no valid timestamp (legacy or hand-edited). "
                  "Run a fresh report run, route, then --mark.")
            return 0
        if (time.time() - stamp) > STAGE_MAX_AGE_S:
            age_h = (time.time() - stamp) / 3600
            print(f"\n[--mark] REFUSING: the stage is {age_h:.0f}h old (from a prior session). "
                  "Run a report run first so you mark what you just routed, not a stale list.")
            return 0
        print(f"\n[--mark] consuming {len(pending)} staged id(s): {', '.join(pending[:10])}"
              f"{' …' if len(pending) > 10 else ''}")
        seen["consumed"] = sorted(set(seen.get("consumed", [])) | set(pending))
        save_seen(seen)
        save_pending([])
        print(f"--mark: recorded {len(pending)} id(s) → {SEEN.name} (ids only).")
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
        digtag = f"  [DIG: {', '.join(b['dig'])}]" if b.get("dig") else ""
        print(f"  {i}. {b['id'] or b['dedup_key']}  {who}  {b['created_at'] or '—'}{digtag}")
        for w in b["warn"]:
            print(f"     ⚠️  {w}")
        body = (b.get("full_text") or b["text"]).replace("\n", " ")
        print(f"     │ {body[:1500]}{'…' if len(body) > 1500 else ''}")
        for m in b.get("media", []):
            print(f"     🖼  {m.get('type') or 'media'}: {m.get('url') or '(no url — expand media.fields)'}")
        for ln in b.get("links", []):
            print(f"     🔗 {ln}")
        print()

    save_pending([b["dedup_key"] for b in new])
    print("After routing, run:  python3 AGENTS/WALTER/tools/x_bookmarks_scan.py --mark")
    return 0


if __name__ == "__main__":
    sys.exit(main())
