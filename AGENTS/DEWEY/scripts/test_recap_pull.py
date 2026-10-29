#!/usr/bin/env python3
"""
Acceptance tests for recap_pull.py, run against a LOCAL fake CourtListener.
No network; nothing touches the real API.

  .venv/bin/python3 AGENTS/DEWEY/scripts/test_recap_pull.py

The four acceptance tests (BACKLOG 2026-09-27 row, reviewer-specified):
  T1 two agents requesting the same document share ONE retrieval
  T2 a restart preserves the cache (a new process fetches nothing)
  T3 throttling pauses correctly: the shared budget waits, a 429 Retry-After
     is honored, and a wait beyond RECAP_MAX_WAIT exits 3 instead of hanging
  T4 a wrong-case document is rejected (exit 4, quarantined), and an
     unreadable image-only header is UNVERIFIED (exit 5), never accepted
Added 2026-10-29 (OTTO packet 10/28, CourtListener now 401s anonymous search):
  T6 an API 401 exits 7 "TOKEN REQUIRED" (or "TOKEN REJECTED" with a token
     set), says it is not "no results", and is never cached
  T7 `feed` states its window: entry count, oldest date, and the 30-entry
     cap warning when at the cap; it always fetches fresh
"""

import http.server, json, os, subprocess, sys, tempfile, threading, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "recap_pull.py")
PY = sys.executable


def make_pdf(text):
    """Minimal one-page PDF with a text line (enough for pdftotext)."""
    stream = f"BT /F1 10 Tf 40 750 Td ({text}) Tj ET".encode() if text else b""
    objs = [b"<< /Type /Catalog /Pages 2 0 R >>",
            b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
            b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] "
            b"/Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
            b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream",
            b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>"]
    out, offs = bytearray(b"%PDF-1.4\n"), []
    for i, o in enumerate(objs, 1):
        offs.append(len(out))
        out += b"%d 0 obj\n" % i + o + b"\nendobj\n"
    x = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    out += b"".join(b"%010d 00000 n \n" % o for o in offs)
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs) + 1, x)
    return bytes(out)


DOCS = {
    "/recap/good.pdf": make_pdf("Case 8:26-bk-10986-MH Doc 88 Filed 09/08/26 Entered 09/08/26 Nano Banc owed"),
    "/recap/wrong.pdf": make_pdf("Case 8:26-bk-11647-MH Doc 77 Filed 09/08/26 Conejo Loan Investors"),
    "/recap/scan.pdf": make_pdf(""),
}
def make_rss(n):
    items = "".join(
        f"<item><title>Entry {i}</title><link>https://example/{i}</link>"
        f"<pubDate>Mon, {10 + i % 18:02d} Oct 2026 12:00:00 -0000</pubDate></item>"
        for i in range(n))
    return (f'<?xml version="1.0" encoding="utf-8"?><rss version="2.0"><channel>'
            f"<title>docket</title>{items}</channel></rss>").encode()


def make_atom(n):
    """CourtListener's real docket-feed format (Atom), shaped on the live 10/29 feed."""
    items = "".join(
        f"<entry><title>Entry #{4000 - i} in Test v. Case</title>"
        f'<link href="https://example/docket#entry-{4000 - i}" rel="alternate"/>'
        f"<published>2026-10-{29 - i % 20:02d}T00:00:00-07:00</published>"
        f'<summary type="html">Motion {i}</summary>'
        f'<link href="https://ecf.example/doc1/{i}" length="0" rel="enclosure" type="None"/></entry>'
        for i in range(n))
    return (f'<?xml version="1.0" encoding="utf-8"?><feed xml:lang="en-us" '
            f'xmlns="http://www.w3.org/2005/Atom"><title>Docket updates</title>{items}</feed>').encode()


FEEDS = {"/docket/123/feed/": make_rss(3), "/docket/999/feed/": make_atom(30)}
HITS = Counter()
STATE = {"429_once": True}


class Fake(http.server.BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def do_GET(self):
        path = self.path.split("?")[0]
        HITS[self.path] += 1
        if path in DOCS:
            time.sleep(1.0)                     # slow, so concurrent callers overlap
            body = DOCS[path]
            self.send_response(200); self.send_header("Content-Type", "application/pdf")
            self.send_header("Content-Length", str(len(body))); self.end_headers()
            self.wfile.write(body); return
        if path in FEEDS:
            body = FEEDS[path]
            self.send_response(200); self.send_header("Content-Type", "application/rss+xml")
            self.send_header("Content-Length", str(len(body))); self.end_headers()
            self.wfile.write(body); return
        if path == "/api/search/" and "needauth" in self.path:
            body = b'{"detail":"Authentication credentials were not provided."}'
            self.send_response(401); self.send_header("Content-Length", str(len(body)))
            self.end_headers(); self.wfile.write(body); return
        if path == "/api/search/":
            if "htmlonce" in self.path and STATE.setdefault("html_once", True):
                STATE["html_once"] = False
                body = b"<!DOCTYPE html><html>browsable API</html>"
                self.send_response(200); self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(body))); self.end_headers()
                self.wfile.write(body); return
            if "application/json" not in (self.headers.get("Accept") or ""):
                body = b"<html>DRF browsable view</html>"
                self.send_response(200); self.send_header("Content-Type", "text/html")
                self.send_header("Content-Length", str(len(body))); self.end_headers()
                self.wfile.write(body); return
            if "ratelimited" in self.path and STATE["429_once"]:
                STATE["429_once"] = False
                body = b'{"detail":"Request was throttled. Expected available in 2 seconds."}'
                self.send_response(429); self.send_header("Retry-After", "2")
                self.send_header("Content-Length", str(len(body))); self.end_headers()
                self.wfile.write(body); return
            body = json.dumps({"count": 0, "results": []}).encode()
            self.send_response(200); self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body))); self.end_headers()
            self.wfile.write(body); return
        self.send_response(404); self.end_headers()


def run(args, env, **kw):
    return subprocess.run([PY, TOOL] + args, env=env, capture_output=True, text=True, **kw)


def main():
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Fake)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    cache = tempfile.mkdtemp(prefix="recap_test_")
    env = dict(os.environ, RECAP_CACHE=cache, RECAP_API_BASE=base + "/api",
               RECAP_STORAGE_BASE=base, RECAP_WEB_BASE=base,
               RECAP_LIMITS="100/60", RECAP_MAX_WAIT="10")
    env.pop("COURTLISTENER_TOKEN", None)
    fails = []

    def check(name, cond, detail=""):
        print(f"{'PASS' if cond else 'FAIL'}  {name}{('  — ' + detail) if detail else ''}")
        if not cond:
            fails.append(name)

    # T1: two concurrent agents, same document → one retrieval
    url = base + "/recap/good.pdf"
    procs = [subprocess.Popen([PY, TOOL, "doc", url, "--case", "8:26-bk-10986", "--entry", "88"],
                              env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
             for _ in range(2)]
    outs = [p.communicate() for p in procs]
    check("T1 concurrent identical requests share one retrieval",
          HITS["/recap/good.pdf"] == 1 and all(p.returncode == 0 for p in procs),
          f"server hits={HITS['/recap/good.pdf']}, rcs={[p.returncode for p in procs]}")
    check("T1b identity VERIFIED from the page-1 header", all("VERIFIED" in o[0] for o in outs), outs[0][0].strip()[:90])

    # T2: a restart (new process) fetches nothing
    r = run(["doc", url, "--case", "8:26-bk-10986", "--entry", "88"], env)
    check("T2 restart preserves cache (0 new server hits)",
          HITS["/recap/good.pdf"] == 1 and r.returncode == 0 and "(cache)" in r.stdout,
          f"hits={HITS['/recap/good.pdf']} rc={r.returncode}")

    # T3a: shared budget pauses (limit 2 per 3 s → the 3rd call waits ~3 s)
    env3 = dict(env, RECAP_LIMITS="2/3", RECAP_CACHE=tempfile.mkdtemp(prefix="recap_t3_"))
    for q in ("a", "b"):
        run(["search", q], env3)
    t0 = time.time(); r = run(["search", "c"], env3); dt = time.time() - t0
    check("T3a budget full → the call WAITS, then succeeds", r.returncode == 0 and dt >= 2.0, f"waited {dt:.1f}s rc={r.returncode}")
    # T3b: wait beyond RECAP_MAX_WAIT → exit 3 with the wait, no hang
    run(["search", "d"], env3)
    t0 = time.time(); r = run(["search", "e"], dict(env3, RECAP_MAX_WAIT="0")); dt = time.time() - t0
    check("T3b wait > RECAP_MAX_WAIT → exit 3 THROTTLED immediately", r.returncode == 3 and dt < 2 and "THROTTLED" in r.stderr,
          f"rc={r.returncode} {dt:.1f}s {r.stderr.strip()[:80]}")
    # T3c: server 429 + Retry-After: 2 → honored, retried once, succeeds
    env3c = dict(env, RECAP_CACHE=tempfile.mkdtemp(prefix="recap_t3c_"))
    t0 = time.time(); r = run(["search", "ratelimited"], env3c); dt = time.time() - t0
    n429 = sum(v for k, v in HITS.items() if "ratelimited" in k)
    check("T3c 429 Retry-After honored (slept ≥2s, 2 server hits, success)", r.returncode == 0 and dt >= 1.9 and n429 == 2,
          f"rc={r.returncode} {dt:.1f}s hits={n429}")

    # T5: an invalid body is NEVER cached (the first-live-call defect)
    env5 = dict(env, RECAP_CACHE=tempfile.mkdtemp(prefix="recap_t5_"))
    r1 = run(["search", "htmlonce"], env5); r2 = run(["search", "htmlonce"], env5)
    nh = sum(v for k, v in HITS.items() if "htmlonce" in k)
    check("T5 non-JSON body → exit 6, NOT cached; the retry re-fetches and succeeds",
          r1.returncode == 6 and "NOT cached" in r1.stderr and r2.returncode == 0 and nh == 2,
          f"rc1={r1.returncode} rc2={r2.returncode} hits={nh}")

    # T4: wrong-case document → rejected + quarantined; image-only → UNVERIFIED
    r = run(["doc", base + "/recap/wrong.pdf", "--case", "8:26-bk-10986", "--entry", "77"], env)
    q = os.listdir(os.path.join(cache, "quarantine")) if os.path.isdir(os.path.join(cache, "quarantine")) else []
    check("T4 wrong-case document REJECTED (exit 4) and quarantined", r.returncode == 4 and "MISMATCH" in r.stdout and len(q) == 1,
          r.stdout.strip()[:100])
    r = run(["doc", base + "/recap/scan.pdf", "--case", "8:26-mj-00387", "--entry", "11"], env)
    check("T4b unreadable header → UNVERIFIED (exit 5), not accepted", r.returncode == 5 and "UNVERIFIED" in r.stdout, r.stdout.strip()[:100])
    r = run(["doc", url, "--case", "8:26-bk-10986", "--entry", "88-1"], env)
    check("T4c attachment number must match exactly (88 ≠ 88-1)", r.returncode == 4, r.stdout.strip()[:100])
    man = [json.loads(l) for l in open(os.path.join(cache, "manifest.jsonl"))]
    need = {"sha256", "url", "expected_case", "expected_entry", "header", "identity", "retrieved_at"}
    check("T4d manifest records identity fields on every document", all(need <= set(m) for m in man), f"{len(man)} records")

    # page-numbered quote
    r = run(["text", man[0]["sha256"], "--grep", "Nano Banc owed"], env)
    check("quotes carry a page number", r.returncode == 0 and r.stdout.startswith("p.1:"), r.stdout.strip()[:60])

    # T6: an API 401 is loud, distinct, and never cached
    env6 = dict(env, RECAP_CACHE=tempfile.mkdtemp(prefix="recap_t6_"))
    r1 = run(["search", "needauth"], env6); r2 = run(["search", "needauth"], env6)
    nh = sum(v for k, v in HITS.items() if "needauth" in k)
    check("T6 anonymous 401 → exit 7 TOKEN REQUIRED, 'NOT no results', not cached (2 hits)",
          r1.returncode == 7 and "TOKEN REQUIRED" in r1.stderr and "NOT 'no results'" in r1.stderr
          and r2.returncode == 7 and nh == 2, f"rc={r1.returncode} hits={nh} {r1.stderr.strip()[:90]}")
    r = run(["search", "needauth"], dict(env6, COURTLISTENER_TOKEN="bogus"))
    check("T6b 401 with a token set → exit 7 TOKEN REJECTED", r.returncode == 7 and "TOKEN REJECTED" in r.stderr,
          r.stderr.strip()[:90])

    # T7: feed states its window; at the cap it warns; it never serves from cache
    r = run(["feed", "123"], env)
    check("T7 feed below cap: count + oldest date + 'not verified', 3 rows",
          r.returncode == 0 and "3 entries, oldest 2026-10-10" in r.stdout and "not verified" in r.stdout
          and r.stdout.count("Entry ") == 3, r.stdout.splitlines()[0][:90] if r.stdout else r.stderr[:90])
    r = run(["feed", "999"], env)
    check("T7b Atom feed (the live format) at the 30 cap → oldest date + 'older entries are NOT in this feed'",
          r.returncode == 0 and "30 entries, oldest 2026-10-10" in r.stdout and "AT THE 30-ENTRY CAP" in r.stdout
          and "NOT in this feed" in r.stdout and "#entry-4000" in r.stdout and "ecf.example" not in r.stdout,
          r.stdout.splitlines()[1][:90] if r.stdout else r.stderr[:90])
    run(["feed", "123"], env)
    check("T7c feed always fetches fresh (2 server hits for 2 runs on docket 123)",
          HITS["/docket/123/feed/"] == 2, f"hits={HITS['/docket/123/feed/']}")

    srv.shutdown()
    print(f"\n{'ALL PASS' if not fails else str(len(fails)) + ' FAIL: ' + ', '.join(fails)}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
