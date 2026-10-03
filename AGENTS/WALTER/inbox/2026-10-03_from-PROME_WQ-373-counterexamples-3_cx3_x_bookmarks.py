#!/usr/bin/env python3
"""cx3 — read-3 counterexamples for AGENTS/WALTER/tools/x_bookmarks_scan.py @ 805d9cc43.
Never writes inside the repository: every case runs in a child process with WALTER_X_ENV /
WALTER_X_SEEN set to ABSOLUTE paths under a fresh /tmp dir; the network is faked by
replacing the module's API functions; only the tool's own localhost authorize server is hit.
Run:  /home/willi/Research-workspace/.venv/bin/python cx3_x_bookmarks.py
"""
import hashlib
import json
import os
import socket
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO = Path("/home/willi/Research-workspace")
TOOLDIR = REPO / "AGENTS/WALTER/tools"
TOOL = TOOLDIR / "x_bookmarks_scan.py"
PY = str(REPO / ".venv/bin/python")
LIVE = [REPO / "AGENTS/WALTER/.env", REPO / "AGENTS/WALTER/registry/x_bookmarks_seen.json",
        REPO / "AGENTS/WALTER/registry/x_bookmarks_pending.json"]

RESULTS = []


def record(name, ok, detail):
    RESULTS.append((name, ok, detail))
    print(f"{'PASS' if ok else 'FAIL'}  {name}  — {detail}")


def free_port():
    s = socket.socket()
    s.bind(("localhost", 0))
    p = s.getsockname()[1]
    s.close()
    return p


def live_state():
    return [(str(p), p.read_bytes() if p.exists() else None) for p in LIVE]


# ----------------------------------------------------------------------------- child side
CHILD_PRELUDE = r'''
import sys, json, threading, time, urllib.parse, urllib.request
sys.path.insert(0, %(tooldir)r)
import x_bookmarks_scan as xbm
CALLS = {"list": 0}
BOOKMARKS = json.loads(%(bookmarks)r)
SEED_FAILS = %(seed_fails)r

def fake_api(user_id, token, pagination_token=None):
    CALLS["list"] += 1
    if SEED_FAILS:
        raise RuntimeError("network unreachable (faked)")
    return BOOKMARKS, {"a1": "qtr"}, {}

class FakeResp:
    def __init__(self, j): self._j = j
    def raise_for_status(self): pass
    def json(self): return self._j

class FakeRequests:
    class HTTPError(Exception):
        def __init__(self, resp=None): self.response = resp
    @staticmethod
    def post(url, data=None, auth=None, timeout=None):
        return FakeResp({"access_token": "ACC_NEW", "refresh_token": "REF_NEW"})
    @staticmethod
    def get(url, headers=None, timeout=None):
        return FakeResp({"data": {"id": "42"}})

xbm._require_requests = lambda: FakeRequests
xbm.api_get_bookmarks = fake_api

def browser(url):
    q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
    st = q["state"][0]
    def hit():
        time.sleep(0.3)
        urllib.request.urlopen(f"{xbm.REDIRECT_URI}?code=CODE&state={st}", timeout=5).read()
    threading.Thread(target=hit, daemon=True).start()
import webbrowser
webbrowser.open = browser
'''


def run_child(tmp, body, bookmarks=None, seed_fails=False, argv_extra=None, extra_env=None):
    code = CHILD_PRELUDE % {"tooldir": str(TOOLDIR), "bookmarks": json.dumps(bookmarks or []),
                            "seed_fails": seed_fails} + body
    env = {k: v for k, v in os.environ.items() if not k.startswith("WALTER_X")}
    env["WALTER_X_ENV"] = str(Path(tmp) / ".env")
    env["WALTER_X_SEEN"] = str(Path(tmp) / "seen.json")
    env["WALTER_X_REDIRECT"] = f"http://localhost:{free_port()}/callback"
    if extra_env:
        env.update(extra_env)
    return subprocess.run([PY, "-c", code], env=env, capture_output=True, text=True, timeout=60)


def bm(i, text="t", author="a1"):
    return {"id": i, "author_id": author, "text": text, "created_at": "2026-10-03T00:00:00Z"}


def rb(p):
    p = Path(p)
    return p.read_bytes() if p.exists() else None


AUTH = 'rc = xbm.main(["--authorize"]); print("RC", rc, "LISTCALLS", CALLS["list"])\n'
REPORT = 'rc = xbm.main([]); print("RC", rc, "LISTCALLS", CALLS["list"])\n'
MARK = 'rc = xbm.main(["--mark"]); print("RC", rc)\n'


# ----------------------------------------------------------------------------- (a) X6
def case_a():
    # a1: first authorize, no seen-file -> seeds
    t = tempfile.mkdtemp(prefix="cx3a1_")
    Path(t, ".env").write_text("X_CLIENT_ID=cid\n")
    r = run_child(t, AUTH, bookmarks=[bm("1"), bm("2"), bm("3")])
    seen = json.loads(Path(t, "seen.json").read_text()) if Path(t, "seen.json").exists() else None
    record("a1 first --authorize seeds", seen is not None and seen["consumed"] == ["1", "2", "3"],
           f"consumed={seen and seen['consumed']} out_tail={r.stdout.strip().splitlines()[-2:]}")

    # a2: re-authorize with seen-file + live stage present -> both byte-identical, no list call
    t = tempfile.mkdtemp(prefix="cx3a2_")
    Path(t, ".env").write_text("X_CLIENT_ID=cid\nX_BOOKMARK_ACCESS_TOKEN=old\nX_USER_ID=42\n")
    Path(t, "seen.json").write_text(json.dumps({"consumed": ["1"], "pilot_start_id": "P"}, indent=2) + "\n")
    Path(t, "x_bookmarks_pending.json").write_text(json.dumps({"ids": ["9"], "staged_at": int(time.time())}) + "\n")
    s0, p0 = rb(Path(t, "seen.json")), rb(Path(t, "x_bookmarks_pending.json"))
    r = run_child(t, AUTH, bookmarks=[bm("9"), bm("1"), bm("2")])
    ok = rb(Path(t, "seen.json")) == s0 and rb(Path(t, "x_bookmarks_pending.json")) == p0 and "LISTCALLS 0" in r.stdout
    env_after = Path(t, ".env").read_text()
    record("a2 re-authorize (seen+stage present) byte-identical", ok and "ACC_NEW" in env_after,
           f"seen same={rb(Path(t,'seen.json'))==s0} stage same={rb(Path(t,'x_bookmarks_pending.json'))==p0} "
           f"tokens refreshed={'ACC_NEW' in env_after} {r.stdout.strip().splitlines()[-1]}")

    # a3: seen-file exists but EMPTY of consumed ids -> still no re-seed
    t = tempfile.mkdtemp(prefix="cx3a3_")
    Path(t, ".env").write_text("X_CLIENT_ID=cid\n")
    Path(t, "seen.json").write_text(json.dumps({"consumed": [], "pilot_start_id": None}, indent=2) + "\n")
    s0 = rb(Path(t, "seen.json"))
    r = run_child(t, AUTH, bookmarks=[bm("7"), bm("8")])
    record("a3 re-authorize, seen-file empty of ids -> untouched", rb(Path(t, "seen.json")) == s0 and "LISTCALLS 0" in r.stdout,
           f"seen same={rb(Path(t,'seen.json'))==s0} {r.stdout.strip().splitlines()[-1]}")

    # a4: refresh-failure path leads to the re-authorize -> seen + stage byte-identical
    t = tempfile.mkdtemp(prefix="cx3a4_")
    Path(t, ".env").write_text("X_CLIENT_ID=cid\nX_BOOKMARK_ACCESS_TOKEN=old\nX_BOOKMARK_REFRESH_TOKEN=r\nX_USER_ID=42\n")
    Path(t, "seen.json").write_text(json.dumps({"consumed": ["1"], "pilot_start_id": "P"}, indent=2) + "\n")
    Path(t, "x_bookmarks_pending.json").write_text(json.dumps({"ids": ["9"], "staged_at": int(time.time())}) + "\n")
    s0, p0 = rb(Path(t, "seen.json")), rb(Path(t, "x_bookmarks_pending.json"))
    body401 = r'''
class R: status_code = 401
def api401(u, tkn, pt=None):
    raise FakeRequests.HTTPError(R())
def badrefresh(*a, **k):
    raise RuntimeError("invalid_grant (faked)")
xbm.api_get_bookmarks = api401
xbm.refresh_access_token = badrefresh
try:
    xbm.main([])
except SystemExit as e:
    print("EXIT", repr(e.code))
'''
    r1 = run_child(t, body401)
    msg_ok = "does NOT discard" in r1.stdout
    s1, p1 = rb(Path(t, "seen.json")), rb(Path(t, "x_bookmarks_pending.json"))
    r2 = run_child(t, AUTH, bookmarks=[bm("10"), bm("9"), bm("1")])
    ok = (s1 == s0 and p1 == p0 and rb(Path(t, "seen.json")) == s0
          and rb(Path(t, "x_bookmarks_pending.json")) == p0 and "LISTCALLS 0" in r2.stdout)
    record("a4 refresh-fail -> re-authorize leaves seen+stage byte-identical", ok and msg_ok,
           f"refresh msg says safe={msg_ok}; after-fail same={s1==s0 and p1==p0}; after-reauth same="
           f"{rb(Path(t,'seen.json'))==s0 and rb(Path(t,'x_bookmarks_pending.json'))==p0}")

    # a5 (neighbour): first authorize whose SEED READ FAILS writes an empty seen-file and tells
    # Will "Re-run --authorize once reachable to seed". Does the re-run seed?
    t = tempfile.mkdtemp(prefix="cx3a5_")
    Path(t, ".env").write_text("X_CLIENT_ID=cid\n")
    r1 = run_child(t, AUTH, bookmarks=[bm("1"), bm("2")], seed_fails=True)
    said = "Re-run --authorize once reachable to seed" in r1.stdout
    created = Path(t, "seen.json").exists()
    r2 = run_child(t, AUTH, bookmarks=[bm("1"), bm("2")], seed_fails=False)
    seen = json.loads(Path(t, "seen.json").read_text())
    r3 = run_child(t, REPORT, bookmarks=[bm("1"), bm("2")])
    resurf = r3.stdout.count("  1. ") + r3.stdout.count("  2. ")
    record("a5 seed-failure instruction 'Re-run --authorize ... to seed' actually seeds",
           seen["consumed"] == ["1", "2"],
           f"msg printed={said}; seen-file written on failure={created}; after re-run consumed={seen['consumed']}; "
           f"re-run said: {r2.stdout.strip().splitlines()[-1][:90]!r}; next report surfaces "
           f"{'all pre-existing' if 'NEW bookmarks to ROUTE — 2' in r3.stdout else 'not all'} as NEW")


# ----------------------------------------------------------------------------- (b) stale stage
def case_b():
    def mark_with_stage(stage_obj, label, expect_consume):
        t = tempfile.mkdtemp(prefix="cx3b_")
        Path(t, ".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=42\n")
        Path(t, "seen.json").write_text(json.dumps({"consumed": ["1"], "pilot_start_id": None}) + "\n")
        Path(t, "x_bookmarks_pending.json").write_text(json.dumps(stage_obj) + "\n")
        r = run_child(t, 'try:\n    rc = xbm.main(["--mark"]); print("RC", rc)\nexcept BaseException as e:\n    print("RAISED", type(e).__name__, e)\n')
        consumed = json.loads(Path(t, "seen.json").read_text())["consumed"]
        did = "9" in consumed
        record(label, did == expect_consume,
               f"consumed={consumed} out={[l for l in r.stdout.splitlines() if 'mark' in l or 'RC' in l or 'RAISED' in l][-2:]} err={r.stderr.strip()[-80:]!r}")
    now = int(time.time())
    mark_with_stage({"ids": ["9"], "staged_at": now - 23 * 3600}, "b1 stage 23h old -> consumed", True)
    mark_with_stage({"ids": ["9"], "staged_at": now - 25 * 3600}, "b2 stage 25h old -> REFUSED, nothing consumed", False)
    mark_with_stage({"ids": ["9"]}, "b3 stage with NO timestamp -> refused (fail closed)?", False)
    mark_with_stage(["9"], "b4 legacy list-shaped stage (0fe87931c format, no stamp) -> refused?", False)
    mark_with_stage({"ids": ["9"], "staged_at": 0}, "b5 staged_at=0 (epoch) -> refused?", False)
    mark_with_stage({"ids": ["9"], "staged_at": "yesterday"}, "b6 staged_at non-numeric -> refused, no traceback?", False)


# ----------------------------------------------------------------------------- (c) A8 refusal
def case_c():
    tmp = tempfile.mkdtemp(prefix="cx3c_")
    variants = [
        ("c1 relative ENV + relative SEEN", {"WALTER_X_ENV": ".env", "WALTER_X_SEEN": "registry/x_bookmarks_seen.json"}),
        ("c2 empty ENV only", {"WALTER_X_ENV": ""}),
        ("c3 both empty", {"WALTER_X_ENV": "", "WALTER_X_SEEN": ""}),
        ("c4 ENV only (absolute)", {"WALTER_X_ENV": str(Path(tmp) / ".env")}),
        ("c5 SEEN only (absolute)", {"WALTER_X_SEEN": str(Path(tmp) / "seen.json")}),
        ("c6 absolute ENV + relative SEEN", {"WALTER_X_ENV": str(Path(tmp) / ".env"), "WALTER_X_SEEN": "registry/x_bookmarks_seen.json"}),
    ]
    for argv in ([], ["--mark"], ["--authorize"]):
        for label, ov in variants:
            before = live_state()
            env = {k: v for k, v in os.environ.items() if not k.startswith("WALTER_X")}
            env.update(ov)
            r = subprocess.run([PY, str(TOOL)] + argv, env=env, cwd=str(REPO / "AGENTS/WALTER"),
                               capture_output=True, text=True, timeout=30)
            after = live_state()
            ok = r.returncode != 0 and "REFUSING" in (r.stdout + r.stderr) and before == after \
                and "Traceback" not in r.stderr and "X-BOOKMARK scan" not in r.stdout
            record(f"{label} argv={argv}", ok, f"rc={r.returncode} live untouched={before==after} "
                   f"stdout_empty={r.stdout.strip()==''}")


# ----------------------------------------------------------------------------- (d) noid key
def case_d():
    t = tempfile.mkdtemp(prefix="cx3d_")
    Path(t, ".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=42\n")
    Path(t, "seen.json").write_text(json.dumps({"consumed": ["1"], "pilot_start_id": None}) + "\n")
    items = [{"author_id": "a1", "text": "no id here", "created_at": "2026-10-03T01:00:00Z"},
             {"author_id": "a1", "text": "a different idless post", "created_at": "2026-10-03T01:00:00Z"},
             bm("1")]
    r1 = run_child(t, REPORT, bookmarks=items)
    st1 = json.loads(Path(t, "x_bookmarks_pending.json").read_text())["ids"]
    r2 = run_child(t, REPORT, bookmarks=items)            # second launch, same items
    st2 = json.loads(Path(t, "x_bookmarks_pending.json").read_text())["ids"]
    record("d1 same idless item -> same key across two launches", st1 == st2 and all(k.startswith("noid:") for k in st1),
           f"launch1={st1} launch2={st2}")
    record("d2 two different idless items do not collide", len(set(st1)) == 2, f"keys={st1}")
    run_child(t, MARK)
    r3 = run_child(t, REPORT, bookmarks=items)
    record("d3 --mark consumes noid keys; next launch surfaces none", "NEW bookmarks — 0" in r3.stdout,
           f"consumed={json.loads(Path(t,'seen.json').read_text())['consumed']}")
    # d4 text-free check on the noid key: seen-file holds hash only, no post text
    raw = Path(t, "seen.json").read_text() + Path(t, "x_bookmarks_pending.json").read_text()
    record("d4 no post text in seen/stage after noid flow", "no id here" not in raw and "different" not in raw, "hash only")
    # d5 id=0 vs missing id with identical content share a key (both 'MALFORMED')
    sys.path.insert(0, str(TOOLDIR))
    os.environ["WALTER_X_ENV"] = str(Path(t, ".env")); os.environ["WALTER_X_SEEN"] = str(Path(t, "seen.json"))
    import x_bookmarks_scan as xbm
    a = xbm.parse_bookmark({"id": 0, "author_id": "a1", "text": "x"}, {})
    b = xbm.parse_bookmark({"author_id": "a1", "text": "x"}, {})
    c = xbm.parse_bookmark({"id": "", "author_id": "a1", "text": " x "}, {})
    record("d5 id 0/missing/'' with same content -> one key (expected; informational)",
           a["dedup_key"] == b["dedup_key"] == c["dedup_key"], f"{a['dedup_key']}")


# ----------------------------------------------------------------------------- (e) save_seen guards
def case_e():
    sys.path.insert(0, str(TOOLDIR))
    t = tempfile.mkdtemp(prefix="cx3e_")
    os.environ["WALTER_X_ENV"] = str(Path(t, ".env")); os.environ["WALTER_X_SEEN"] = str(Path(t, "seen.json"))
    import x_bookmarks_scan as xbm
    p = Path(t, "s.json")
    def tryit(label, seen, expect_reject):
        try:
            xbm.save_seen(seen, p)
            rej = False
            content = p.read_text()
        except ValueError as e:
            rej, content = True, f"ValueError: {e}"
        except Exception as e:
            rej, content = None, f"{type(e).__name__}: {e}"
        record(label, rej == expect_reject, content.replace("\n", " ")[:110])
    tryit("e1 nested list element rejected", {"consumed": [["1"]], "pilot_start_id": None}, True)
    tryit("e2 dict element with text rejected", {"consumed": [{"id": "1", "text": "LEAK"}], "pilot_start_id": None}, True)
    tryit("e3 float element rejected", {"consumed": [1.5], "pilot_start_id": None}, True)
    tryit("e4 None element rejected", {"consumed": [None], "pilot_start_id": None}, True)
    tryit("e5 bool element rejected? (bool is an int subclass)", {"consumed": [True], "pilot_start_id": None}, True)
    tryit("e6 nested value in pilot_start_id (text) rejected?", {"consumed": [], "pilot_start_id": {"text": "LEAK"}}, True)
    tryit("e7 int element accepted and written as str", {"consumed": [5], "pilot_start_id": None}, False)
    tryit("e8 consumed as a dict rejected", {"consumed": {"1": "LEAK"}, "pilot_start_id": None}, True)


# ----------------------------------------------------------------------------- (f) mixed str/int
def case_f():
    # f1: paging stop with consumed = [123, "124"] (hand-edited int) -> page 1 all seen -> stop at 1 page
    t = tempfile.mkdtemp(prefix="cx3f1_")
    Path(t, ".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=42\n")
    Path(t, "seen.json").write_text('{"consumed": [123, "124"], "pilot_start_id": null}\n')
    body = r'''
def paged(u, tkn, pt=None):
    CALLS["list"] += 1
    return [{"id": "124", "author_id": "a1", "text": "x"}, {"id": "123", "author_id": "a1", "text": "y"}], {}, {"next_token": "N%d" % CALLS["list"]}
xbm.api_get_bookmarks = paged
rc = xbm.main([]); print("RC", rc, "LISTCALLS", CALLS["list"])
'''
    r = run_child(t, body)
    record("f1 paging stop matches int+str consumed (1 page, 0 new)", "LISTCALLS 1" in r.stdout and "NEW bookmarks — 0" in r.stdout,
           r.stdout.strip().splitlines()[-1])
    # f2: same mixed seen-file, a NEW bookmark arrives -> report stages it -> --mark
    t = tempfile.mkdtemp(prefix="cx3f2_")
    Path(t, ".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=42\n")
    Path(t, "seen.json").write_text('{"consumed": [123, "124"], "pilot_start_id": null}\n')
    r1 = run_child(t, REPORT, bookmarks=[bm("125"), bm("124"), bm("123")])
    s0 = rb(Path(t, "seen.json"))
    r2 = run_child(t, 'try:\n    rc = xbm.main(["--mark"]); print("RC", rc)\nexcept BaseException as e:\n    print("RAISED", type(e).__name__, e)\n')
    consumed_ok = rb(Path(t, "seen.json")) != s0 and "125" in Path(t, "seen.json").read_text()
    record("f2 --mark with int+str consumed (state load_seen ACCEPTS) completes", consumed_ok and "RC 0" in r2.stdout,
           f"report staged={'125' in Path(t,'x_bookmarks_pending.json').read_text()}; mark out="
           f"{r2.stdout.strip().splitlines()[-1][:100]!r}; seen changed={rb(Path(t,'seen.json'))!=s0}")
    # f3: does the report re-surface 125 next launch (fail direction check)
    r3 = run_child(t, REPORT, bookmarks=[bm("125"), bm("124"), bm("123")])
    record("f3 after a failed --mark, 125 re-surfaces (safe direction, not dropped)", "NEW bookmarks to ROUTE — 1" in r3.stdout,
           "over-surface, not drop" if "NEW bookmarks to ROUTE — 1" in r3.stdout else r3.stdout[-120:])


if __name__ == "__main__":
    live0 = live_state()
    for fn in (case_a, case_b, case_c, case_d, case_e, case_f):
        print(f"\n=== {fn.__name__} ===")
        fn()
    assert live_state() == live0, "LIVE FILES CHANGED"
    npass = sum(1 for _, ok, _ in RESULTS if ok)
    print(f"\nTOTAL {npass} PASS / {len(RESULTS) - npass} FAIL of {len(RESULTS)} ; live repo files untouched: {live_state() == live0}")
