#!/usr/bin/env python3
"""
CourtListener / RECAP retrieval helper: one shared cache and one shared
request budget for every agent on this box. Document identity is recorded
at download.

Built 2026-09-27 (Will go-ahead, bounded build; BACKLOG row 2026-09-27).
It closes two defects from the Nano Banc run:
  (1) four parallel sub-agents each called the API and exhausted the shared
      allowance in ~40 min; and
  (2) a filing was saved under ANOTHER case's docket id, and a guessed RECAP
      path nearly shipped as a citation.

A filename or a guessed URL NEVER establishes which case a document belongs
to. The document's own page-1 header does ("Case 8:26-bk-10986-MH Doc 88
Filed 09/08/26").

Usage:
  recap_pull.py search '"Nano Banc"' --type rd --court cacb
  recap_pull.py doc URL --case 8:26-bk-10986 --entry 88     # verify + cache
  recap_pull.py text <sha256|URL> --grep "Nano Banc"        # page-numbered
  recap_pull.py status        # budget windows, blocked-until, cache size
  recap_pull.py usage         # CourtListener Usage API (token required)

Scope (deliberately narrow, not a research platform):
  * Cache: search JSON and PDFs persist on disk across restarts. Identical
    requests are served from the cache, and concurrent identical requests
    wait on a per-key lock, so one retrieval serves both.
  * Throttle: rolling windows shared by every process via a locked budget
    file. Defaults are CourtListener's DOCUMENTED AUTHENTICATED limits (5/min,
    50/hr, 125/day). ⚠ Anonymous calls have no documented allowance (the
    anonymous Nano run was throttled at "50/hour"), so the defaults are a
    ceiling, not a promise. Honors `Retry-After` on 429. Falls back to parsing
    "Expected available in N seconds" from the body.
  * Storage PDFs (storage.courtlistener.com) are not API-metered. They are
    cached and deduplicated but do not draw on the API budget.
  * Identity: `doc` requires the expected case number (and entry). The
    page-1 header is read. MATCH → accepted. MISMATCH → rejected, exit 4,
    kept in quarantine. Unreadable header (image-only scan) → UNVERIFIED,
    exit 5, never silently accepted.

Environment:
  COURTLISTENER_TOKEN   optional API token (enables auth + the Usage API)
  RECAP_CACHE           cache dir (default ~/.cache/dewey_recap)
  RECAP_LIMITS          e.g. "5/60,50/3600,125/86400" (count/seconds)
  RECAP_MAX_WAIT        max seconds to sleep for budget (default 90)
  RECAP_API_BASE / RECAP_STORAGE_BASE   override hosts (used by the tests)

Exit codes: 0 ok · 2 usage · 3 THROTTLED (wait exceeds RECAP_MAX_WAIT; the
wait is printed) · 4 identity MISMATCH · 5 identity UNVERIFIED · 6 HTTP or
transport error.

Stdlib only. The PDF-text fallback uses pdfminer (run with .venv/bin/python3).
"""

import argparse, fcntl, hashlib, json, os, re, shutil, subprocess, sys, time
import urllib.error, urllib.parse, urllib.request
from contextlib import contextmanager

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_url import headers_for, _decompress  # reuse: per-host UA + gzip

API_BASE = os.environ.get("RECAP_API_BASE", "https://www.courtlistener.com/api/rest/v4")
STORAGE_BASE = os.environ.get("RECAP_STORAGE_BASE", "https://storage.courtlistener.com")
CACHE = os.path.expanduser(os.environ.get("RECAP_CACHE", "~/.cache/dewey_recap"))
LIMITS = [tuple(int(x) for x in w.split("/"))
          for w in os.environ.get("RECAP_LIMITS", "5/60,50/3600,125/86400").split(",")]
MAX_WAIT = float(os.environ.get("RECAP_MAX_WAIT", "90"))
TOKEN = os.environ.get("COURTLISTENER_TOKEN", "").strip()


class Throttled(Exception):
    def __init__(self, wait, why):
        super().__init__(f"THROTTLED: {why}; next slot in {wait:.0f}s "
                         f"(> RECAP_MAX_WAIT={MAX_WAIT:.0f}s). Retry later or raise the wait.")
        self.wait = wait


class FetchError(Exception):
    pass


# ---------------------------------------------------------------- cache paths
def _p(*parts):
    path = os.path.join(CACHE, *parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def _key(s):
    return hashlib.sha256(s.encode()).hexdigest()


@contextmanager
def _locked(name):
    """Exclusive cross-process lock (flock). Released when the process dies,
    so a crashed agent can't wedge the box."""
    with open(_p("locks", name + ".lock"), "a+") as fh:
        fcntl.flock(fh, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(fh, fcntl.LOCK_UN)


# ---------------------------------------------------------------- the budget
def _load_budget():
    try:
        with open(_p("budget.json")) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"calls": [], "blocked_until": 0}


def _save_budget(b):
    tmp = _p("budget.json.tmp")
    with open(tmp, "w") as f:
        json.dump(b, f)
    os.replace(tmp, _p("budget.json"))


def _wait_needed(b, now):
    """Seconds until every rolling window has room (0 = go now)."""
    waits = [max(0.0, b.get("blocked_until", 0) - now)]
    for count, secs in LIMITS:
        inwin = sorted(t for t in b["calls"] if t > now - secs)
        if len(inwin) >= count:
            waits.append(inwin[len(inwin) - count] + secs - now)
    return max(waits)


def _reserve_slot():
    """Block (up to MAX_WAIT) until the shared budget admits one API call,
    then record it. Recording BEFORE the call is deliberately conservative."""
    deadline = time.time() + MAX_WAIT
    while True:
        with _locked("budget"):
            b = _load_budget()
            now = time.time()
            longest = max(s for _, s in LIMITS)
            b["calls"] = [t for t in b["calls"] if t > now - longest]
            w = _wait_needed(b, now)
            if w <= 0:
                b["calls"].append(now)
                _save_budget(b)
                return
        why = "server Retry-After" if b.get("blocked_until", 0) > now else "shared budget full"
        if now + w > deadline:
            raise Throttled(w, why)
        time.sleep(min(w, 5) + 0.05)


def _note_429(headers, body):
    """Record the server's own reset time. Retry-After first; body text fallback."""
    wait = None
    ra = headers.get("Retry-After") if headers else None
    if ra:
        try:
            wait = float(ra)
        except ValueError:
            pass
    if wait is None:
        m = re.search(rb"available in (\d+) seconds", body or b"")
        wait = float(m.group(1)) if m else 60.0
    with _locked("budget"):
        b = _load_budget()
        b["blocked_until"] = max(b.get("blocked_until", 0), time.time() + wait)
        _save_budget(b)
    return wait


# ---------------------------------------------------------------- HTTP
def _http(url, metered):
    """GET with per-host UA. Returns bytes; a 429 re-queues itself within MAX_WAIT."""
    for _ in range(3):
        if metered:
            _reserve_slot()
        h = headers_for(url)
        if url.startswith(API_BASE):
            # ⚠ headers_for() asks for text/html, and the API then serves its
            # HTML "browsable" view, not JSON (caught on the first live call).
            h["Accept"] = "application/json"
            if TOKEN:
                h["Authorization"] = f"Token {TOKEN}"
        req = urllib.request.Request(url, headers=h)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return _decompress(r.read(), r)
        except urllib.error.HTTPError as e:
            body = e.read()
            if e.code == 429:
                _note_429(e.headers, body)
                continue           # _reserve_slot now waits out blocked_until
            raise FetchError(f"HTTP {e.code} for {url}: {body[:200]!r}") from e
        except urllib.error.URLError as e:
            raise FetchError(f"transport error for {url}: {e.reason}") from e
    raise FetchError(f"still 429 after 3 attempts: {url}")


def _cached_get(url, metered, suffix, refresh=False):
    """Serve from disk if present; else fetch once, even with concurrent callers."""
    k = _key(url)
    path = _p("raw", k + suffix)
    with _locked("key-" + k):             # a concurrent identical call waits here
        if os.path.exists(path) and not refresh:
            _log("HIT", url)
            with open(path, "rb") as f:
                return f.read(), path, True
        data = _http(url, metered)
        # NEVER cache an invalid body. A cached error page is served to every
        # later caller as if it were the answer (first live call cached an
        # HTML page, and the retry got the same junk without re-fetching).
        if suffix == ".json":
            try:
                json.loads(data)
            except ValueError:
                raise FetchError(f"{url} returned non-JSON ({len(data)} bytes, starts "
                                 f"{data[:60]!r}); NOT cached")
        elif suffix == ".pdf" and not data.startswith(b"%PDF"):
            raise FetchError(f"{url} did not return a PDF ({len(data)} bytes, starts "
                             f"{data[:60]!r}); NOT cached")
        tmp = path + ".part"
        with open(tmp, "wb") as f:
            f.write(data)
        os.replace(tmp, path)
        _log("FETCH", url)
        return data, path, False


def _log(kind, url):
    with open(_p("requests.log"), "a") as f:
        f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%S')}\t{kind}\t{url}\n")


# ---------------------------------------------------------------- identity
_HDR = re.compile(r"Case\s+([0-9]{1,2}:[0-9]{2}-[a-z]{2}-[0-9]{4,6})(?:-[A-Z]{2,4})*"
                  r".{0,40}?(?:Doc(?:ument)?)\s+([0-9]+(?:-[0-9]+)?)"
                  r".{0,40}?Filed\s+([0-9/]+)", re.S)
_HDR_BK = re.compile(r"Case\s+([0-9]{2}-[0-9]{4,6})(?:-[A-Z]{2,4})*"
                     r".{0,40}?Doc\s+([0-9]+(?:-[0-9]+)?).{0,40}?Filed\s+([0-9/]+)", re.S)


def _page_texts(path):
    """List of page strings, 1-indexed by position+1. pdftotext first (splits
    pages on \\f); pdfminer fallback."""
    if shutil.which("pdftotext"):
        p = subprocess.run(["pdftotext", "-layout", path, "-"], capture_output=True)
        if p.returncode == 0:
            return p.stdout.decode("utf-8", "replace").split("\f")
    from pdf2text import extract
    out, i = [], 0
    while True:
        try:
            t = extract(path, pages=str(i))
        except Exception:
            break
        if not t and i > 0:
            break
        out.append(t); i += 1
    return out


def _norm_case(c):
    # "8:26-bk-10986-MH" and "8:26-bk-10986" are the same case; judge suffix optional
    return re.sub(r"(-[A-Z]{2,4})+$", "", c.strip()).lower()


def _entry_ok(got, want):
    """'88' matches '88'. '1-1' must match '1-1' exactly, so an attachment
    never passes for its sibling. A bare '1' asks for the main document and
    matches '1' only."""
    return got == want


def read_identity(path):
    pages = _page_texts(path)
    first = re.sub(r"\s+", " ", pages[0] if pages else "")
    m = _HDR.search(first) or _HDR_BK.search(first)
    if not m:
        return None, len(pages), len(first.split())
    return {"case": m.group(1), "entry": m.group(2), "filed": m.group(3)}, len(pages), len(first.split())


def _manifest(rec):
    with _locked("manifest"):
        with open(_p("manifest.jsonl"), "a") as f:
            f.write(json.dumps(rec) + "\n")


def get_doc(url, case, entry=None, court=None):
    if not url.startswith("http"):
        url = STORAGE_BASE.rstrip("/") + "/recap/" + url.lstrip("/")
    data, rawpath, hit = _cached_get(url, metered=url.startswith(API_BASE), suffix=".pdf")
    if not data.startswith(b"%PDF"):
        raise FetchError(f"{url} did not return a PDF ({len(data)} bytes)")
    sha = hashlib.sha256(data).hexdigest()
    ident, npages, words = read_identity(rawpath)
    want_case, want_entry = _norm_case(case), (str(entry) if entry else None)
    if ident is None:
        status = "UNVERIFIED"
        why = (f"page-1 header unreadable ({words} words extracted; image-only scan?). "
               f"Render it (pdftoppm -r 80 -png) and confirm by eye before citing")
    elif _norm_case(ident["case"]) != want_case or (want_entry and not _entry_ok(ident["entry"], want_entry)):
        status = "MISMATCH"
        why = f"header says {ident['case']} Doc {ident['entry']}; expected {case} Doc {entry or '?'}"
    else:
        status = "VERIFIED"
        why = f"header {ident['case']} Doc {ident['entry']} Filed {ident['filed']}"
    dest_dir = {"VERIFIED": "docs", "MISMATCH": "quarantine", "UNVERIFIED": "unverified"}[status]
    dest = _p(dest_dir, sha + ".pdf")
    if not os.path.exists(dest):
        shutil.copyfile(rawpath, dest)
    body_words = sum(len(x.split()) for x in _page_texts(dest))
    sparse = npages and body_words < 50 * npages
    if sparse:
        why += (f" · ⚠ body is mostly image ({body_words} words / {npages} pp): "
                f"`text --grep` will MISS content; render pages (pdftoppm -r 80 -png) and read them")
    rec = {"sha256": sha, "url": url, "court": court, "expected_case": case,
           "expected_entry": entry, "header": ident, "identity": status,
           "pages": npages, "body_words": body_words, "image_only_body": bool(sparse),
           "path": dest, "cache_hit": hit,
           "retrieved_at": time.strftime("%Y-%m-%dT%H:%M:%S%z")}
    _manifest(rec)
    return rec, why


# ---------------------------------------------------------------- commands
def cmd_search(a):
    q = {"q": a.query, "type": a.type}
    if a.court:
        q["court"] = a.court
    if a.order:
        q["order_by"] = a.order
    url = f"{API_BASE}/search/?{urllib.parse.urlencode(q)}"
    data, _, hit = _cached_get(url, metered=True, suffix=".json", refresh=a.refresh)
    d = json.loads(data)
    print(f"# {d.get('count', '?')} results{' (cache)' if hit else ''} — {url}")
    print("# docket\tentry[-att]\tfiled\tdescription\tstorage_url (cite ONLY after `doc --case` VERIFIES it)")
    for r in d.get("results", [])[: a.limit]:
        # type=r nests documents under a docket (docketNumber); type=rd rows are
        # documents and carry only docket_id (verified on the first live call)
        docket = r.get("docketNumber") or r.get("docket_number") or f"docket_id={r.get('docket_id', '?')}"
        for rd in (r.get("recap_documents") or [r]):
            fp = rd.get("filepath_local") or ""
            num = rd.get("document_number") or rd.get("entry_number") or ""
            att = rd.get("attachment_number")
            print("\t".join(str(x) for x in (
                docket, f"{num}-{att}" if att else num, rd.get("entry_date_filed", ""),
                (rd.get("description") or rd.get("short_description") or "")[:140],
                (STORAGE_BASE + "/" + fp) if fp else "")))
    return 0


def cmd_doc(a):
    rec, why = get_doc(a.url, a.case, a.entry, a.court)
    print(f"{rec['identity']}: {why}")
    print(f"  sha256 {rec['sha256']} · {rec['pages']} pp · {rec['path']}"
          f"{' · (cache)' if rec['cache_hit'] else ''}")
    return {"VERIFIED": 0, "MISMATCH": 4, "UNVERIFIED": 5}[rec["identity"]]


def _find_doc(ref):
    if re.fullmatch(r"[0-9a-f]{64}", ref):
        for d in ("docs", "unverified", "quarantine"):
            p = os.path.join(CACHE, d, ref + ".pdf")
            if os.path.exists(p):
                return p, d
        raise FetchError(f"no cached document {ref}")
    if not ref.startswith("http"):
        ref = STORAGE_BASE.rstrip("/") + "/recap/" + ref.lstrip("/")
    # the most recent identity verdict for this URL governs
    try:
        with open(os.path.join(CACHE, "manifest.jsonl")) as f:
            recs = [json.loads(l) for l in f if l.strip()]
    except FileNotFoundError:
        recs = []
    mine = [r for r in recs if r["url"] == ref]
    if mine:
        r = mine[-1]
        d = {"VERIFIED": "docs", "MISMATCH": "quarantine", "UNVERIFIED": "unverified"}[r["identity"]]
        return r["path"], d
    p = os.path.join(CACHE, "raw", _key(ref) + ".pdf")
    if os.path.exists(p):
        return p, "raw (identity not checked; run `doc` first)"
    raise FetchError(f"{ref} not cached; run `doc URL --case ...` first")


def cmd_text(a):
    path, where = _find_doc(a.ref)
    pages = _page_texts(path)
    if where != "docs":
        print(f"⚠ identity: {where}; do not cite without resolving it", file=sys.stderr)
    else:
        print(f"# identity VERIFIED · {path}", file=sys.stderr)
    if not a.grep:
        for i, t in enumerate(pages, 1):
            print(f"=== p.{i} ===\n{t}")
        return 0
    rx, n = re.compile(a.grep, re.I), 0
    for i, t in enumerate(pages, 1):
        flat = re.sub(r"\s+", " ", t)
        for m in rx.finditer(flat):
            n += 1
            print(f"p.{i}: …{flat[max(0, m.start() - a.context):m.end() + a.context]}…")
    if not n:
        print(f"NO MATCH for {a.grep!r} across {len(pages)} pages "
              f"({sum(len(t.split()) for t in pages)} words extracted"
              f"{'; near-zero ⇒ image-only scan, not absence' if sum(len(t.split()) for t in pages) < 50 * max(1, len(pages)) else ''})")
        return 1
    return 0


def cmd_status(a):
    with _locked("budget"):
        b = _load_budget()
    now = time.time()
    for count, secs in LIMITS:
        used = sum(1 for t in b["calls"] if t > now - secs)
        print(f"window {secs:>6}s: {used}/{count} used")
    bu = b.get("blocked_until", 0)
    print(f"server block: {'until ' + time.strftime('%H:%M:%S', time.localtime(bu)) if bu > now else 'none'}")
    print(f"next slot in: {max(0, _wait_needed(b, now)):.0f}s · auth: {'token' if TOKEN else 'ANONYMOUS'} · cache: {CACHE}")
    return 0


def cmd_usage(a):
    if not TOKEN:
        print("Usage API requires authentication (anonymous requests get HTTP 401). "
              "Set COURTLISTENER_TOKEN. `status` shows the local shared budget instead.")
        return 2
    data = _http(f"{API_BASE}/usage/", metered=True)
    print(data.decode("utf-8", "replace"))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("query")
    s.add_argument("--type", default="rd"); s.add_argument("--court")
    s.add_argument("--order", default="entry_date_filed desc")
    s.add_argument("--limit", type=int, default=40); s.add_argument("--refresh", action="store_true")
    d = sub.add_parser("doc"); d.add_argument("url")
    d.add_argument("--case", required=True, help="expected case no., e.g. 8:26-bk-10986")
    d.add_argument("--entry", help="expected docket entry, e.g. 88"); d.add_argument("--court")
    t = sub.add_parser("text"); t.add_argument("ref", help="sha256 or URL")
    t.add_argument("--grep"); t.add_argument("--context", type=int, default=200)
    sub.add_parser("status"); sub.add_parser("usage")
    a = ap.parse_args()
    try:
        return {"search": cmd_search, "doc": cmd_doc, "text": cmd_text,
                "status": cmd_status, "usage": cmd_usage}[a.cmd](a)
    except Throttled as e:
        print(e, file=sys.stderr); return 3
    except FetchError as e:
        print(f"ERROR: {e}", file=sys.stderr); return 6


if __name__ == "__main__":
    sys.exit(main())
