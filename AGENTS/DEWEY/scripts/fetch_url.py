#!/usr/bin/env python3
"""
Browser-UA URL fetcher — closes the BACKLOG.md "Fed-family 403 on WebFetch"
blocker (3rd+ recurrence; hand-rolled three times in one session during the
2026-07-28 C4 run, where it blocked two load-bearing primaries).

Same class as the solved EDGAR 403 (`edgar_doc.py`): the host does not block
scripted access, it blocks the *generic WebFetch UA*. A declared browser UA
over urllib returns 200. Stdlib only.

KNOWN-GOOD with a BROWSER UA (verified live 2026-08-02):
  newyorkfed.org · richmondfed.org · federalreserve.gov

⚠️ THE UA IS NOT ONE UA — it is per-host, and the two walls want OPPOSITE things:
  sec.gov / data.sec.gov  want a DECLARED-CONTACT UA ("Research NAME email") and
  return **403 to a browser UA** — the exact inverse of the Fed family. Caught
  2026-08-02 testing this tool's own first version, whose docstring had listed
  sec.gov as known-good on the assumption that one UA fixes every 403. It does
  not. Handled automatically by CONTACT_UA_HOSTS below; `--ua` forces either.

KNOWN-BAD (do NOT retry with this tool — the wall is not UA-shaped):
  spglobal.com   — true bot-block; 403 even with a declared browser UA.
                   Ratings pages go through the Will paste-path (PROME ruling
                   2026-07-31), not through here.
  fico.com       — failed with HTTP/2 INTERNAL_ERROR; use --http1.1.

Usage:
  python3 fetch_url.py https://www.newyorkfed.org/microeconomics/hhdc
  python3 fetch_url.py URL --grep "delinquency transition"
  python3 fetch_url.py URL --grep "partial claim" --context 3
  python3 fetch_url.py URL --raw                 # no HTML strip (JSON/CSV/txt)
  python3 fetch_url.py URL --http1.1             # HTTP/2 INTERNAL_ERROR fallback
  python3 fetch_url.py URL --status              # print status only, fetch nothing

The --status mode is a PRIMARY-GRADE NEGATIVE, not a convenience: establish
"not yet released" by HTTP status (e.g. Q2 QHDC -> 302 vs Q1 -> 200) rather
than trusting a search summary's silence. Promoted as a technique from the
C4 run; see BACKLOG.md 2026-07-28 row.
"""

import sys, os, re, gzip, argparse, subprocess, urllib.request, urllib.error
from html.parser import HTMLParser

# A real browser UA. This is the whole fix for the Fed-family wall.
BROWSER_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
# SEC wants the OPPOSITE: a declared contact, and 403s the browser UA.
CONTACT_UA = "Research DEWEY williepowen@gmail.com"
CONTACT_UA_HOSTS = ("sec.gov", "data.sec.gov", "efts.sec.gov")


def pick_ua(url, override=None):
    """Per-host UA. The Fed family wants a browser; SEC wants a contact."""
    if override == "browser":
        return BROWSER_UA
    if override == "contact":
        return CONTACT_UA
    h = _host(url)
    for d in CONTACT_UA_HOSTS:
        if h == d or h.endswith("." + d):
            return CONTACT_UA
    return BROWSER_UA


def headers_for(url, override=None):
    return {
        "User-Agent": pick_ua(url, override),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip",
    }

# Hosts where a UA does NOT open the door — fail fast with the reason instead of
# burning a run re-discovering it.
HARD_WALLS = {
    "spglobal.com": ("true bot-block, not UA-shaped (verified 2026-07-28). "
                     "Use the Will paste-path — PROME ruling 2026-07-31."),
    "www.spglobal.com": ("true bot-block, not UA-shaped (verified 2026-07-28). "
                         "Use the Will paste-path — PROME ruling 2026-07-31."),
}


class _Text(HTMLParser):
    """Strip HTML to readable text; drop script/style; keep block breaks."""
    def __init__(self):
        super().__init__()
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style", "noscript"):
            self.skip += 1
        if tag in ("p", "br", "div", "tr", "li", "h1", "h2", "h3", "h4", "table"):
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in ("script", "style", "noscript") and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)

    def text(self):
        t = "".join(self.out)
        t = re.sub(r"[ \t\xa0]+", " ", t)
        t = re.sub(r"\n\s*\n\s*\n+", "\n\n", t)
        return "\n".join(line.strip() for line in t.split("\n")).strip()


def _host(url):
    m = re.match(r"^https?://([^/]+)", url)
    return m.group(1).lower() if m else ""


def _check_hard_wall(url):
    h = _host(url)
    for bad, why in HARD_WALLS.items():
        if h == bad or h.endswith("." + bad):
            sys.stderr.write(f"REFUSING {h}: {why}\n")
            sys.exit(3)


def _decompress(data, resp):
    if resp.headers.get("Content-Encoding", "").lower() == "gzip":
        try:
            return gzip.decompress(data)
        except OSError:
            return data          # some hosts mislabel; fall through
    return data


def fetch_urllib(url, timeout=45, ua=None):
    """Returns (status, final_url, bytes). Raises on transport failure."""
    req = urllib.request.Request(url, headers=headers_for(url, ua))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.geturl(), _decompress(r.read(), r)
    except urllib.error.HTTPError as e:
        # An HTTP error is a RESULT (403/404/302 are all findings), not a crash.
        return e.code, url, _decompress(e.read(), e)


def fetch_curl(url, http11=False, timeout=45, ua=None):
    """curl fallback — carries --http1.1 for the HTTP/2 INTERNAL_ERROR class."""
    cmd = ["curl", "-sS", "-L", "--compressed", "--max-time", str(timeout),
           "-w", "\n__HTTP_STATUS__%{http_code}", "-A", pick_ua(url, ua)]
    if http11:
        cmd.append("--http1.1")
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(f"curl failed rc={p.returncode}: "
                           f"{p.stderr.decode('utf-8', 'replace').strip()}")
    body = p.stdout
    status = 0
    m = re.search(rb"\n__HTTP_STATUS__(\d+)$", body)
    if m:
        status = int(m.group(1))
        body = body[:m.start()]
    return status, url, body


def status_only(url, timeout=30, ua=None):
    """HEAD-ish probe. Reports the status WITHOUT following redirects, because
    the redirect itself is the signal (302 = not yet released)."""
    class _NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None
    op = urllib.request.build_opener(_NoRedirect)
    req = urllib.request.Request(url, headers=headers_for(url, ua), method="HEAD")
    try:
        with op.open(req, timeout=timeout) as r:
            return r.status, r.headers.get("Location", "")
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Location", "") if e.headers else ""


def grep(text, pattern, context=0, ignorecase=True):
    flags = re.I if ignorecase else 0
    lines = text.split("\n")
    hits, seen = [], set()
    for i, line in enumerate(lines):
        if re.search(pattern, line, flags):
            lo, hi = max(0, i - context), min(len(lines), i + context + 1)
            for j in range(lo, hi):
                if j not in seen:
                    seen.add(j)
                    hits.append(f"{j+1}: {lines[j]}")
            if context:
                hits.append("--")
    return hits


def main():
    ap = argparse.ArgumentParser(description="Browser-UA URL fetcher (Fed-family 403 fix)")
    ap.add_argument("url")
    ap.add_argument("--grep", help="regex; print only matching lines")
    ap.add_argument("--context", type=int, default=0, help="lines of context around --grep hits")
    ap.add_argument("--raw", action="store_true", help="no HTML strip (JSON/CSV/plain text)")
    ap.add_argument("--http1.1", dest="http11", action="store_true",
                    help="force HTTP/1.1 via curl (HTTP/2 INTERNAL_ERROR fallback, e.g. fico.com)")
    ap.add_argument("--curl", action="store_true", help="force the curl path")
    ap.add_argument("--status", action="store_true",
                    help="print HTTP status + Location only; do not follow redirects")
    ap.add_argument("--timeout", type=int, default=45)
    ap.add_argument("--save", help="write the fetched bytes to this path")
    ap.add_argument("--ua", choices=("browser", "contact"),
                    help="force a UA. Default is per-host: browser for the Fed "
                         "family, declared-contact for sec.gov (which 403s a browser UA).")
    args = ap.parse_args()

    _check_hard_wall(args.url)

    if args.status:
        code, loc = status_only(args.url, args.timeout, args.ua)
        print(f"HTTP {code}" + (f" -> {loc}" if loc else ""))
        # 2xx = live; 3xx/4xx = a primary-grade negative, cite it as such.
        sys.exit(0 if 200 <= code < 300 else 1)

    if args.curl or args.http11:
        status, final, data = fetch_curl(args.url, http11=args.http11,
                                         timeout=args.timeout, ua=args.ua)
    else:
        try:
            status, final, data = fetch_urllib(args.url, timeout=args.timeout, ua=args.ua)
        except Exception as e:
            sys.stderr.write(f"urllib path failed ({e}); retrying via curl\n")
            status, final, data = fetch_curl(args.url, timeout=args.timeout, ua=args.ua)

    if status >= 400:
        used = "contact" if pick_ua(args.url, args.ua) == CONTACT_UA else "browser"
        other = "browser" if used == "contact" else "contact"
        sys.stderr.write(
            f"HTTP {status} for {args.url}  (tried the {used} UA)\n"
            f"  FIRST try the other UA: --ua {other}. The two 403 walls are inverses —\n"
            "  the Fed family wants a browser UA, sec.gov wants a declared contact.\n"
            "  Only if BOTH fail is it a TRUE bot-block: record it in scripts/BACKLOG.md\n"
            "  as NOT UA-fixable rather than retrying.\n")
        sys.exit(2)

    if args.save:
        with open(args.save, "wb") as f:
            f.write(data)
        sys.stderr.write(f"saved {len(data)} bytes -> {args.save}\n")

    body = data.decode("utf-8", "replace")
    if not args.raw:
        p = _Text()
        p.feed(body)
        body = p.text()

    if args.grep:
        hits = grep(body, args.grep, args.context)
        if not hits:
            # An explicit negative is the product — say it on stderr, exit 1.
            sys.stderr.write(f"NO MATCH for /{args.grep}/ in {final} "
                             f"({len(body)} chars fetched, HTTP {status})\n")
            sys.exit(1)
        print("\n".join(hits))
    else:
        print(body)


if __name__ == "__main__":
    main()
