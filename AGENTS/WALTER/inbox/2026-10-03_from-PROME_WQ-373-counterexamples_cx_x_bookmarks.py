"""Coldreader counterexamples for AGENTS/WALTER/tools/x_bookmarks_scan.py @0b90fae4d.
Imports the module by path in subprocess-isolated fashion; never writes inside the repo."""
import importlib.util, io, json, os, subprocess, sys, tempfile
from contextlib import redirect_stdout
from pathlib import Path
TOOL = "/home/willi/Research-workspace/AGENTS/WALTER/tools/x_bookmarks_scan.py"
PY = "/home/willi/Research-workspace/.venv/bin/python"
TMP = Path(tempfile.mkdtemp(prefix="cx_xbm_"))
os.environ["WALTER_X_ENV"] = str(TMP / ".env"); os.environ["WALTER_X_SEEN"] = str(TMP / "seen.json")
spec = importlib.util.spec_from_file_location("xbm", TOOL); xbm = importlib.util.module_from_spec(spec); spec.loader.exec_module(xbm)
R = []
def rec(name, ok, detail): R.append((name, "PASS" if ok else "FAIL", detail))
def run(name, fn):
    try: fn()
    except SystemExit as e: rec(name, False, f"SystemExit {e.code!r}")
    except BaseException as e: rec(name, False, f"UNCAUGHT {type(e).__name__}: {e}")
U = {"a1": "u"}
def bm(i, text="hello"): return xbm.parse_bookmark({"id": i, "author_id": "a1", "text": text}, U)

# CX1 A2: real snowflake lengths (18 vs 19 digits), floor and seen as int/str
def cx1():
    floor = "999999999999999999"          # 18 digits
    a, b, c = "1000000000000000000", "1844674407370955161", "99999999999999999"  # 19,19,17
    out = [x["id"] for x in xbm.select_new([bm(c), bm(a), bm(b)], [], floor)]
    out2 = [x["id"] for x in xbm.select_new([bm(a), bm(b)], [int(b)], int(floor))]
    rec("CX1 A2 snowflake 17/18/19-digit + int seen/floor", out == [b, a] and out2 == [a], f"{out} / {out2}")
run("CX1", cx1)

# CX2 A5: valid JSON, wrong shape
for label, content in [("list []", "[]"), ("string", '"x"'), ("consumed null", '{"consumed": null}'),
                       ("consumed as string", '{"consumed": "1200", "pilot_start_id": "100"}'),
                       ("pilot_start_id non-numeric", '{"consumed": [], "pilot_start_id": "abc"}'),
                       ("non-UTF8 bytes", None)]:
    p = TMP / f"seen_{abs(hash(label))}.json"
    if content is None: p.write_bytes(b"\xff\xfe\x00garbage")
    else: p.write_text(content)
    def f(p=p, label=label):
        d = xbm.load_seen(p)
        out = xbm.select_new([bm("1200")], d["consumed"], d["pilot_start_id"])
        rec(f"CX2 A5 seen-file {label}", False, f"load_seen ACCEPTED it; select_new -> {[x['id'] for x in out]} (no refusal)")
    def g(f=f, label=label):
        try: f()
        except SystemExit as e:
            rec(f"CX2 A5 seen-file {label}", "REFUSING" in str(e.code), f"SystemExit: {str(e.code)[:70]}")
    run(f"CX2 {label}", g)

# CX3 A6: .env edge cases
def cx3():
    p = TMP / "e1.env"
    p.write_bytes(b"# top comment\nX_CLIENT_ID=abc=def\nNOTE=has # hash\nX_BOOKMARK_ACCESS_TOKEN=old\nLAST=nonl")
    xbm.rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": "new", "X_BOOKMARK_REFRESH_TOKEN": "r2"}, p)
    raw = p.read_text(); env = xbm.load_env(p)
    ok = (env["X_CLIENT_ID"] == "abc=def" and env["NOTE"] == "has # hash" and env["LAST"] == "nonl"
          and env["X_BOOKMARK_ACCESS_TOKEN"] == "new" and raw.count("X_BOOKMARK_ACCESS_TOKEN") == 1
          and "# top comment" in raw and oct(p.stat().st_mode & 0o777) == "0o600")
    rec("CX3a A6 '=' in value, '#' in value, no trailing newline, in-place replace", ok, repr(raw))
run("CX3a", cx3)
def cx3b():
    p = TMP / "e2.env"
    p.write_text("X_BOOKMARK_ACCESS_TOKEN=old1\nX_BOOKMARK_ACCESS_TOKEN=old2\n")
    xbm.rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": "NEW"}, p)
    got = xbm.load_env(p)["X_BOOKMARK_ACCESS_TOKEN"]
    rec("CX3b A6 duplicate key line -> rotated value is what load_env returns", got == "NEW", f"load_env returns {got!r}; file={p.read_text()!r}")
run("CX3b", cx3b)
def cx3c():
    p = TMP / "e3.env"
    p.write_bytes(b"X_CLIENT_ID=abc\r\nOTHER=1\r\n")
    xbm.rewrite_env({"X_BOOKMARK_ACCESS_TOKEN": "t"}, p)
    rec("CX3c A6 CRLF .env preserved byte-for-byte on other lines", b"\r\n" in p.read_bytes(), repr(p.read_bytes()))
run("CX3c", cx3c)
def cx3d():
    p = TMP / "e4.env"
    p.write_text('X_CLIENT_ID="abc"\n')
    rec("CX3d load_env strips quotes from a quoted value", xbm.load_env(p)["X_CLIENT_ID"] == "abc", repr(xbm.load_env(p)["X_CLIENT_ID"]))
run("CX3d", cx3d)

# CX4 A4: id present but empty text / non-string text / id 0
def cx4():
    p = xbm.parse_bookmark({"id": "2000", "author_id": "a1", "text": "   "}, U)
    out = xbm.select_new([p], [], "1000")
    rec("CX4a A4 id + whitespace text -> warned AND handed over", len(out) == 1 and any("EMPTY" in w for w in p["warn"]), f"warn={p['warn']} out={len(out)}")
run("CX4a", cx4)
def cx4b():
    p = xbm.parse_bookmark({"id": "2001", "author_id": "a1", "text": 12345}, U)
    rec("CX4b A4 non-string text never raises", True, f"returned {p}")
run("CX4b", cx4b)
def cx4c():
    p = xbm.parse_bookmark({"id": 0, "author_id": "a1", "text": "t"}, U)
    rec("CX4c id=0 (int) classed MALFORMED, surfaced", p["id"] is None and len(xbm.select_new([p], [], "5")) == 1, str(p["warn"]))
run("CX4c", cx4c)

# CX5 A10: not-authorized states, real process exit codes
def sub(env_text, extra=None, seen_text=None, args=()):
    d = Path(tempfile.mkdtemp(prefix="cx_sub_"))
    env = dict(os.environ, WALTER_X_ENV=str(d / ".env"), WALTER_X_SEEN=str(d / "seen.json"))
    if env_text is not None: (d / ".env").write_text(env_text)
    if seen_text is not None: (d / "seen.json").write_text(seen_text)
    if extra: env.update(extra)
    r = subprocess.run([PY, TOOL, *args], env=env, capture_output=True, text=True, timeout=30)
    return r
r = sub(None); rec("CX5a A10 no .env file at all -> rc 0 + authorize hint", r.returncode == 0 and "--authorize" in r.stdout, f"rc={r.returncode}")
r = sub("X_BOOKMARK_ACCESS_TOKEN=t\n"); rec("CX5b A10-adjacent: token but no X_USER_ID (half-authorized) -> rc 0?", r.returncode == 0, f"rc={r.returncode} stderr={r.stderr.strip()[:90]!r}")
r = sub("# empty\n", seen_text="{ bad"); rec("CX5c not-authorized + corrupt seen-file -> still rc 0 (seen never read)", r.returncode == 0, f"rc={r.returncode}")

# CX6 A8: partial isolation still announced as test mode
def a8(only):
    env = {k: v for k, v in os.environ.items() if k not in ("WALTER_X_ENV", "WALTER_X_SEEN")}
    env[only] = str(TMP / "only")
    code = ("import importlib.util as u;s=u.spec_from_file_location('m',%r);m=u.module_from_spec(s);s.loader.exec_module(m);"
            "print(m._TEST_MODE, m.ENV_PATH, m.SEEN)") % TOOL
    return subprocess.run([PY, "-c", code], env=env, capture_output=True, text=True).stdout.strip()
o1 = a8("WALTER_X_ENV"); o2 = a8("WALTER_X_SEEN")
rec("CX6a A8 only WALTER_X_ENV set: TEST MODE declared but SEEN is LIVE", "registry/x_bookmarks_seen.json" not in o1, o1)
rec("CX6b A8 only WALTER_X_SEEN set: TEST MODE declared but ENV (live tokens) is LIVE", not o2.endswith("") or "/AGENTS/WALTER/.env" not in o2, o2)

# CX7 pilot floor is POST id, not bookmark time: old post bookmarked after authorize
def cx7():
    floor = "1974000000000000000"   # newest post id among existing bookmarks at authorize
    old_post_bookmarked_today = "1500000000000000000"
    out = xbm.select_new([bm(old_post_bookmarked_today)], [], floor)
    rec("CX7 old post bookmarked AFTER authorize is surfaced (setup card: 'ones you add from now on')", len(out) == 1, f"out={len(out)} -> dropped with NO warning")
run("CX7", cx7)

for n, s, d in R: print(f"{s:4}  {n}\n      {d}")
print(f"\n{sum(1 for r in R if r[1]=='PASS')} PASS / {sum(1 for r in R if r[1]=='FAIL')} FAIL")

# CX8 A7 end-to-end through main(['--mark']) with fetch stubbed; + report->mark race
R.clear()
d = Path(tempfile.mkdtemp(prefix="cx_mark_"))
xbm.ENV_PATH = d / ".env"; xbm.SEEN = d / "seen.json"
(d / ".env").write_text("X_BOOKMARK_ACCESS_TOKEN=t\nX_USER_ID=1\n")
xbm.save_seen({"consumed": [], "pilot_start_id": "100"}, xbm.SEEN)
BODY_A, BODY_B = "SECRET BODY ALPHA", "SECRET BODY BRAVO"
calls = {"n": 0}
def fake_fetch(env, seen):
    calls["n"] += 1
    items = [bm("500", BODY_A)] + ([bm("600", BODY_B)] if calls["n"] > 1 else [])
    return xbm.select_new(items, seen["consumed"], seen["pilot_start_id"])
xbm.fetch_new_bookmarks = fake_fetch
orig_load_env, orig_load_seen, orig_save = xbm.load_env, xbm.load_seen, xbm.save_seen
xbm.load_env = lambda path=None: orig_load_env(d / ".env")
xbm.load_seen = lambda path=None: orig_load_seen(d / "seen.json")
xbm.save_seen = lambda seen, path=None: orig_save(seen, d / "seen.json")
with redirect_stdout(io.StringIO()) as b1: xbm.main([])            # report run: routes A only
routed = [l for l in b1.getvalue().splitlines() if "SECRET" in l]
with redirect_stdout(io.StringIO()) as b2: xbm.main(["--mark"])    # B bookmarked in between
raw = (d / "seen.json").read_text()
rec("CX8a A7 --mark via main(): seen-file has no post text", "SECRET" not in raw and "ALPHA" not in raw, raw.replace("\n", " "))
rec("CX8b --mark marks ONLY what the report run showed (concurrent-bookmark race)", "600" not in json.loads(raw)["consumed"],
    f"report run routed {len(routed)} item(s); --mark run consumed {json.loads(raw)['consumed']}")
for n, s, dd in R: print(f"{s:4}  {n}\n      {dd}")
