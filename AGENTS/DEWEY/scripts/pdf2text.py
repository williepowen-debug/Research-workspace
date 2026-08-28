#!/usr/bin/env python3
"""
PDF-to-text wrapper (pdfminer.six) — closes the BACKLOG.md "FL OIR / FL Realtors
PDFs return as unparseable binary to WebFetch" blocker. Reads a PDF from a URL
(downloaded with a proper UA) or a local path and prints extracted text.

Usage:
  python3 pdf2text.py https://www.floir.com/.../rate-filing.pdf
  python3 pdf2text.py /path/to/local.pdf --grep "uncapped"
  python3 pdf2text.py URL --pages 0-3            # only pages 0,1,2,3
  python3 pdf2text.py URL --grep "+18.8" --context 3

Engine: pdfminer.six (already in the repo .venv per root CLAUDE.md). Run with
the venv python: .venv/bin/python3 AGENTS/DEWEY/scripts/pdf2text.py ...
"""

import sys, os, re, argparse, tempfile, urllib.request, urllib.error

UA = "Research DEWEY williepowen@gmail.com"


class PdfError(Exception):
    """A reportable PDF-fetch/parse failure — never a traceback."""


def _materialize(src):
    """Return a local path; download if src is a URL."""
    if re.match(r"^https?://", src):
        req = urllib.request.Request(src, headers={"User-Agent": UA})
        # A transport failure is a REPORTABLE RESULT, not a crash — a traceback
        # reads as "the tool is broken" instead of "that PDF is not there".
        # Class swept 2026-08-27 with fetch_url/edgar_fetch/edgar_doc.
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
        except urllib.error.HTTPError as e:
            hint = "\n  some hosts want a BROWSER UA here (see fetch_url.py --ua)" \
                   if e.code in (401, 403) else ""
            raise PdfError(f"HTTP {e.code} for {src}{hint}") from e
        except urllib.error.URLError as e:
            raise PdfError(f"transport error for {src}: "
                           f"{type(e.reason).__name__}: {e.reason}") from e
        if not data.startswith(b"%PDF"):
            # Fail LOUD: an HTML error page saved as .pdf parses to junk or to
            # nothing, and "0 chars extracted" reads as an empty PDF rather than
            # as the login/404 page it actually is.
            head = data[:80].decode("utf-8", "replace").replace("\n", " ")
            raise PdfError(f"{src} did not return a PDF ({len(data)} bytes, "
                           f"starts {head!r}) — likely an HTML error/login page")
        fd, path = tempfile.mkstemp(suffix=".pdf")
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        return path, True
    return src, False


def _parse_pages(spec):
    if not spec:
        return None
    out = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return sorted(out)


def extract(src, pages=None):
    try:
        from pdfminer.high_level import extract_text
    except ImportError:
        sys.exit("pdfminer.six not available — run with .venv/bin/python3 (pip install pdfminer.six)")
    path, tmp = _materialize(src)
    try:
        txt = extract_text(path, page_numbers=_parse_pages(pages))
    finally:
        if tmp:
            os.unlink(path)
    return txt


def main():
    ap = argparse.ArgumentParser(description="PDF -> text (pdfminer.six)")
    ap.add_argument("src", help="URL or local path to a PDF")
    ap.add_argument("--pages", help="page range e.g. 0-3 or 0,2,5")
    ap.add_argument("--grep"); ap.add_argument("--context", type=int, default=2)
    ap.add_argument("--max", type=int, default=0)
    a = ap.parse_args()

    txt = extract(a.src, a.pages) or ""
    print(f"=== {a.src} ({len(txt):,} chars) ===\n")
    if a.grep:
        lines = [l for l in txt.split("\n")]
        pat = re.compile(re.escape(a.grep) if not any(c in a.grep for c in ".*[](){}^$") else a.grep, re.I)
        for i, ln in enumerate(lines):
            if pat.search(ln):
                lo, hi = max(0, i - a.context), min(len(lines), i + a.context + 1)
                print("\n".join(x for x in lines[lo:hi] if x.strip()))
                print("  ---")
    else:
        print(txt[:a.max] if a.max else txt)


if __name__ == "__main__":
    try:
        sys.exit(main() or 0)
    except PdfError as e:
        sys.stderr.write(f"{e}\n")
        sys.exit(1)
