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

import sys, os, re, argparse, tempfile, urllib.request

UA = "Research DEWEY williepowen@gmail.com"


def _materialize(src):
    """Return a local path; download if src is a URL."""
    if re.match(r"^https?://", src):
        req = urllib.request.Request(src, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
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
    main()
