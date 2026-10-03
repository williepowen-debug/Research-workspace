#!/usr/bin/env python3
"""cx2 — read-2 counterexamples for x_bookmarks_scan.py @0fe87931c. Never touches the repo:
all state under a /tmp dir; network replaced by fakes; authorize handler hit on a local socket."""
import io, json, os, socket, subprocess, sys, tempfile, threading, time, types, urllib.parse, urllib.request
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

REPO = Path("/home/willi/Research-workspace")
TOOL = REPO / "AGENTS/WALTER/tools/x_bookmarks_scan.py"
BASE = Path(tempfile.mkdtemp(prefix="cx2_xbm_"))
def freeport():
    s = socket.socket(); s.bind(("localhost", 0)); p = s.getsockname()[1]; s.close(); return p
os.environ["WALTER_X_ENV"] = str(BASE / ".env")
os.environ["WALTER_X_SEEN"] = str(BASE / "seen.json")
os.environ["WALTER_X_REDIRECT"] = f"http://localhost:{freeport()}/callback"
sys.path.insert(0, str(TOOL.parent))
import x_bookmarks_scan as xbm  # noqa

RESULTS = []
def rec(cid, ok, what, obs):
    RESULTS.append((cid, "PASS" if ok else "FAIL", what, obs))
    print(f"[{cid}] {'PASS' if ok else 'FAIL'} — {what}\n        observed: {obs}")

def fresh(name):
    d = BASE / name; d.mkdir(); xbm.ENV_PATH = d / ".env"; xbm.SEEN = d / "seen.json"; return d

def raw(pid, text="BODYTEXT-" , author="a1"):
    return {"id": pid, "author_id": author, "text": f"{text}{pid}", "created_at": "2026-10-03T00:00:00Z"}

class FakeAPI:
    """Pages a list of raw items newest-bookmarked-first, PAGE_SIZE per page, next_token = offset."""
    def __init__(self, items, fail_on_call=None):
        self.items, self.calls, self.fail_on_call = items, 0, fail_on_call
    def __call__(self, user_id, token, pagination_token=None):
        self.calls += 1
        if self.fail_on_call and self.calls == self.fail_on_call:
            raise RuntimeError("simulated network error on page %d" % self.calls)
        off = int(pagination_token or 0); n = xbm.PAGE_SIZE
        page = self.items[off:off + n]
        meta = {"next_token": str(off + n)} if off + n < len(self.items) else {}
        return page, {"a1": "someone"}, meta

class R:
    def __init__(self, j): self._j = j
    def raise_for_status(self): pass
    def json(self): return self._j
fake_requests = types.SimpleNamespace(
    HTTPError=type("HTTPError", (Exception,), {}),
    post=lambda *a, **k: R({"access_token": "ACC-SECRET", "refresh_token": "REF-SECRET"}),
    get=lambda *a, **k: R({"data": {"id": "U1"}}))
xbm._require_requests = lambda: fake_requests

def run_authorize(browser_script):
    """Run the REAL do_authorize; webbrowser.open is replaced by `browser_script(url)` which
    talks to the real local HTTPServer over a localhost socket."""
    import webbrowser
    xbm.REDIRECT_URI = f"http://localhost:{freeport()}/callback"
    out, err = io.StringIO(), io.StringIO()
    webbrowser.open = lambda url: threading.Thread(target=browser_script, args=(url,), daemon=True).start()
    t0 = time.time(); rc = None
    with redirect_stdout(out), redirect_stderr(err):
        try: rc = xbm.do_authorize()
        except SystemExit as e: rc = e.code
    return rc, out.getvalue(), time.time() - t0

def hit(path_qs):
    time.sleep(0.2)
    try:
        r = urllib.request.urlopen(xbm.REDIRECT_URI.rsplit("/callback", 1)[0] + path_qs, timeout=5)
        return r.status
    except Exception as e:
        return repr(e)

def state_of(url):
    return urllib.parse.parse_qs(urllib.parse.urlparse(url).query)["state"][0]

# ---------------------------------------------------------------------------
# CX-A  seed when authorize-time fetch spans 3 pages (130 bookmarks): page 2+ seeded?
d = fresh("A"); d.joinpath(".env").write_text("X_CLIENT_ID=cid\n")
api = FakeAPI([raw(str(9000 - i)) for i in range(130)]); xbm.api_get_bookmarks = api
rc, out, _ = run_authorize(lambda url: hit(f"/callback?code=C&state={state_of(url)}"))
seen = json.loads((d / "seen.json").read_text())
rec("CX-A", rc == 0 and len(seen["consumed"]) == 130 and api.calls == 3,
    "authorize seed follows next_token through page 3 (130 items, PAGE_SIZE 50)",
    f"rc={rc} seeded={len(seen['consumed'])} api_calls={api.calls}")

# CX-A2 seed beyond MAX_PAGES (600 bookmarks): is the seed cap warned like the fetch cap (X4)?
d = fresh("A2"); d.joinpath(".env").write_text("X_CLIENT_ID=cid\n")
api = FakeAPI([raw(str(90000 - i)) for i in range(600)]); xbm.api_get_bookmarks = api
rc, out, _ = run_authorize(lambda url: hit(f"/callback?code=C&state={state_of(url)}"))
seen = json.loads((d / "seen.json").read_text())
warned = "cap" in out.lower() or "not seeded" in out.lower() or "⚠" in out
rec("CX-A2", warned, "seed cap (MAX_PAGES*PAGE_SIZE=500) hit on a 600-bookmark account is WARNED",
    f"seeded={len(seen['consumed'])}/600, warning printed={warned}; success line: "
    f"{[l for l in out.splitlines() if 'Authorized' in l]}")

# CX-A3 seed fails on page 2: are page-1 IDs kept, and is the failure loud?
d = fresh("A3"); d.joinpath(".env").write_text("X_CLIENT_ID=cid\n")
api = FakeAPI([raw(str(8000 - i)) for i in range(120)], fail_on_call=2); xbm.api_get_bookmarks = api
rc, out, _ = run_authorize(lambda url: hit(f"/callback?code=C&state={state_of(url)}"))
seen = json.loads((d / "seen.json").read_text())
rec("CX-A3", rc == 0 and "could not read current bookmarks" in out,
    "seed failure on page 2 is loud and fails toward over-surface",
    f"rc={rc} seeded={len(seen['consumed'])} (page-1's 50 discarded too) loud={'could not read' in out}")

# CX-B  RE-authorize (the tool's own instruction after refresh failure) with an un-routed new bookmark
d = fresh("B"); d.joinpath(".env").write_text("X_CLIENT_ID=cid\nX_USER_ID=U1\nX_BOOKMARK_ACCESS_TOKEN=old\n")
xbm.save_seen({"consumed": ["700", "600", "500"], "pilot_start_id": "2026-10-03T00:00:00Z"})
items = [raw("12345"), raw("700"), raw("600"), raw("500")]          # 12345 = bookmarked since last launch
xbm.api_get_bookmarks = FakeAPI(items)
before = [b["id"] for b in xbm.fetch_new_bookmarks(xbm.load_env(), xbm.load_seen())]
xbm.api_get_bookmarks = FakeAPI(items)
rc, out, _ = run_authorize(lambda url: hit(f"/callback?code=C&state={state_of(url)}"))
xbm.api_get_bookmarks = FakeAPI(items)
after = [b["id"] for b in xbm.fetch_new_bookmarks(xbm.load_env(), xbm.load_seen())]
rec("CX-B", after == ["12345"],
    "a bookmark added before a re-authorize (refresh-failure recovery) still surfaces afterwards",
    f"surfaced before re-auth={before}; after re-auth={after}; authorize said: "
    f"{[l.strip() for l in out.splitlines() if 'seeded' in l]}")

# CX-C  removed then re-bookmarked: a post consumed earlier, un-bookmarked, re-bookmarked today
d = fresh("C"); xbm.save_seen({"consumed": ["4242"], "pilot_start_id": None})
api_items = [raw("4242")]   # back at the TOP of newest-bookmarked-first order
out = xbm.select_new([xbm.parse_bookmark(i, {}) for i in api_items], xbm.load_seen()["consumed"])
rec("CX-C", len(out) == 1, "re-bookmarking an already-seen post (fresh act by Will) surfaces it",
    f"surfaced={len(out)} — re-bookmark is invisible; acceptance/card silent on it")

# CX-D  stale stage: stage from a crashed prior session, then --mark with NO report run this session
d = fresh("D"); d.joinpath(".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=U1\n")
xbm.save_seen({"consumed": [], "pilot_start_id": None})
xbm.api_get_bookmarks = FakeAPI([raw("111"), raw("222")])
with redirect_stdout(io.StringIO()): xbm.main([])                     # session 1 prints + stages, then 'crashes'
stage_after_crash = xbm.load_pending(); seen_after_crash = xbm.load_seen()["consumed"]
buf = io.StringIO()
with redirect_stdout(buf): xbm.main(["--mark"])                       # session 2 runs --mark first
consumed = xbm.load_seen()["consumed"]
rec("CX-D", consumed == [], "a --mark with no report run in THIS session refuses a stale stage",
    f"after crash: stage={stage_after_crash} seen={seen_after_crash} (state is safe); "
    f"session-2 --mark consumed={consumed} un-routed; msg={buf.getvalue().strip().splitlines()[-1]!r}")

# CX-D2 crash after report, NEXT session runs report normally: re-surfaced (safe direction)?
d = fresh("D2"); d.joinpath(".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=U1\n")
xbm.save_seen({"consumed": [], "pilot_start_id": None})
xbm.api_get_bookmarks = FakeAPI([raw("111"), raw("222")])
with redirect_stdout(io.StringIO()): xbm.main([])
xbm.api_get_bookmarks = FakeAPI([raw("333"), raw("111"), raw("222")])
with redirect_stdout(io.StringIO()): xbm.main([])
st = xbm.load_pending(); pend_raw = xbm._pending_path().read_text()
rec("CX-D2", st == ["333", "111", "222"] and "BODYTEXT" not in pend_raw,
    "after a crash the next report re-surfaces + re-stages all un-marked; stage holds IDs only",
    f"stage={st}; body in stage file={'BODYTEXT' in pend_raw}")

# CX-E  request count per launch with ONE new bookmark (card: 'up to ~50 per launch')
d = fresh("E"); d.joinpath(".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=U1\n")
old = [str(5000 - i) for i in range(200)]
xbm.save_seen({"consumed": old, "pilot_start_id": None})
api = FakeAPI([raw("99999")] + [raw(i) for i in old]); xbm.api_get_bookmarks = api
new = xbm.fetch_new_bookmarks(xbm.load_env(), xbm.load_seen())
rec("CX-E", api.calls == 1, "one new bookmark costs one page (~50 posts read) as the card says",
    f"new={[b['id'] for b in new]} api_calls={api.calls} (~{api.calls * xbm.PAGE_SIZE} posts read)")

# CX-F  isolation with ONE var given as a RELATIVE path, from WALTER's own launch dir
code = ("import importlib.util as u;s=u.spec_from_file_location('m',%r);m=u.module_from_spec(s);"
        "s.loader.exec_module(m);print(m._TEST_MODE, m.ENV_PATH.resolve(), m.SEEN.resolve())" % str(TOOL))
envv = {k: v for k, v in os.environ.items() if not k.startswith("WALTER_X_")}
envv["WALTER_X_SEEN"] = "scratch_seen.json"
o = subprocess.run([sys.executable, "-c", code], env=envv, cwd=str(REPO / "AGENTS/WALTER"),
                   capture_output=True, text=True).stdout.strip()
live_env = str(REPO / "AGENTS/WALTER/.env")
rec("CX-F", live_env not in o.split(), "WALTER_X_SEEN=scratch_seen.json (relative) from AGENTS/WALTER isolates .env",
    f"TEST_MODE, ENV, SEEN = {o}")
envv2 = {k: v for k, v in os.environ.items() if not k.startswith("WALTER_X_")}
envv2["WALTER_X_ENV"] = ""
p = subprocess.run([sys.executable, str(TOOL)], env=envv2, cwd=str(BASE), capture_output=True, text=True)
rec("CX-F2", p.returncode == 0 or "REFUS" in (p.stdout + p.stderr),
    "WALTER_X_ENV set but EMPTY → clean refusal, not a traceback",
    f"rc={p.returncode} tail={(p.stderr or p.stdout).strip().splitlines()[-1][:120]!r}")

# CX-G  authorize handler: error=access_denied (prompt exit?), no-query request, second request
rc, out, dt = run_authorize(lambda url: hit(f"/callback?error=access_denied&state={state_of(url)}"))
d = fresh("G"); d.joinpath(".env").write_text("X_CLIENT_ID=cid\n")
rc, out, dt = run_authorize(lambda url: hit(f"/callback?error=access_denied&state={state_of(url)}"))
rec("CX-G1", isinstance(rc, str) and "denied" in rc and dt < 10 and not (d / "seen.json").exists(),
    "error=access_denied ends the wait promptly, saves nothing", f"exit={rc!r} after {dt:.1f}s; seen exists={(d/'seen.json').exists()}")
codes = {}
def noquery_then_code(url):
    codes["noq"] = hit("/callback"); codes["fav"] = hit("/favicon.ico")
    codes["code"] = hit(f"/callback?code=C&state={state_of(url)}")
xbm.api_get_bookmarks = FakeAPI([raw("1")])
rc, out, dt = run_authorize(noquery_then_code)
rec("CX-G2", rc == 0 and codes.get("noq") == 204, "a request with no query is ignored (204) and the wait continues",
    f"rc={rc} statuses={codes} dt={dt:.1f}s")
codes2 = {}
def code_then_evil(url):
    codes2["first"] = hit(f"/callback?code=GOOD&state={state_of(url)}")
    codes2["second"] = hit("/callback?code=EVIL&state=WRONG")
posted = {}
fake_requests.post = lambda *a, **k: (posted.setdefault("code", k["data"]["code"]),
                                      R({"access_token": "ACC-SECRET", "refresh_token": "REF-SECRET"}))[1]
rc, out, dt = run_authorize(code_then_evil)
rec("CX-G3", rc == 0 and posted.get("code") == "GOOD" or (isinstance(rc, str) and "STATE" in rc),
    "a second redirect after the first cannot swap in a different code",
    f"rc={rc!r} statuses={codes2} code exchanged={posted.get('code')}")
leak = "ACC-SECRET" in out or "REF-SECRET" in out
rec("CX-G4", not leak, "authorize stdout never prints a token", f"token in stdout={leak}")

# CX-H  .env rewrite: file missing entirely; key three times; BOM; tmp left behind
d = fresh("H"); p = d / "sub" / ".env"
xbm.rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": "a"}, p)
ok1 = p.read_text() == "X_BOOKMARK_ACCESS_TOKEN=a\n" and oct(p.stat().st_mode & 0o777) == "0o600"
p.write_text("# head\nK=1\nX=keep\nK=2\n# mid\nK=3\n")
xbm.rewrite_env({"K": "NEW"}, p)
t = p.read_text(); ok2 = t == "# head\nK=NEW\nX=keep\n# mid\n"
rec("CX-H1", ok1 and ok2, "rewrite_env: missing file+dir created 0600; triple key → one line at first position",
    f"missing-file ok={ok1}; triple → {t!r}; tmp left={any(x.name.endswith('.tmp') for x in p.parent.iterdir())}")
p.write_bytes("﻿X_CLIENT_ID=cid\n".encode("utf-8"))
rec("CX-H2", xbm.load_env(p).get("X_CLIENT_ID") == "cid", "a BOM-prefixed .env (some editors) still yields X_CLIENT_ID",
    f"keys={list(xbm.load_env(p))}")

# CX-I  seen-file shapes that pass load_seen validation
d = fresh("I"); d.joinpath(".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=U1\n")
(d / "seen.json").write_text('{"consumed": [["1"]]}'); xbm.save_pending(["5"])
err = io.StringIO()
try:
    with redirect_stdout(io.StringIO()): xbm.main(["--mark"]); r = "no error"
except SystemExit as e: r = f"SystemExit {str(e.code)[:60]}"
except Exception as e: r = f"TRACEBACK {type(e).__name__}: {e}"
rec("CX-I1", r.startswith("SystemExit") and "REFUS" in r, "consumed=[[\"1\"]] refuses with the fix text (A5), not a traceback", r)
(d / "seen.json").write_text('{"consumed": [5000, 4999]}')
api = FakeAPI([raw(str(5000 - i)) for i in range(600)]); xbm.api_get_bookmarks = api
buf = io.StringIO()
with redirect_stdout(buf): new = xbm.fetch_new_bookmarks(xbm.load_env(), xbm.load_seen())
rec("CX-I2", api.calls == 1, "int IDs in consumed (hand-edit) are matched as seen by the paging stop",
    f"api_calls={api.calls}; cap warning={'cap' in buf.getvalue()}; new={len(new)} (select_new itself str-coerces)")

# CX-J  idless item: surfaced, never staged → re-surfaces at EVERY launch forever?
d = fresh("J"); d.joinpath(".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=U1\n")
xbm.save_seen({"consumed": [], "pilot_start_id": None})
counts = []
for _ in range(3):
    xbm.api_get_bookmarks = FakeAPI([{"text": "no id here", "author_id": "a1"}])
    b = io.StringIO()
    with redirect_stdout(b): xbm.main([]); xbm.main(["--mark"])
    counts.append("MALFORMED" in b.getvalue())
rec("CX-J", counts == [True, False, False], "an idless item, once routed + marked, stops re-firing",
    f"surfaced at launch 1/2/3 = {counts} (never consumable)")

print("\nSUMMARY:", sum(r[1] == "PASS" for r in RESULTS), "PASS /", sum(r[1] == "FAIL" for r in RESULTS), "FAIL")
