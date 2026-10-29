#!/usr/bin/env python3
"""fetch_primary.py — read a government release from the SAVED FILE, never from a summary.

BD-35 / L-33. On 2026-09-17 a fetch tool's summary of dol.gov/ui/data.pdf returned a
complete, plausibly-shaped claims release (213,000 / 216,000 / 1,641,000) for a document
that said 206,000 / 207,000 / 1,774,000. This tool closes that path:

  1. download the primary with curl, trying request shapes in order (the DOL/BLS wall
     flips with request shape — L-24: bare curl → DOL PDF, research-bot UA → BLS HTML,
     browser UA → an Akamai stub), each with a dated cache-busting query string;
  2. save the bytes and REJECT anything that is not the document (wrong magic bytes,
     block/stub pages, tiny bodies) — a rejected fetch is UNKNOWN, never "as summarized";
  3. text-extract the saved file (pdfminer for PDF, tag-strip for HTML);
  4. print the release/date lines found in the extracted text;
  5. for every figure passed with --expect, report FOUND (with its context) or NOT FOUND.

It never prints a figure that it did not find in the extracted text.

USAGE
  fetch_primary.py URL [--expect 194,000 --expect 1,728,000 ...] [--show REGEX ...]
                   [--out DIR] [--no-bust]
  fetch_primary.py --file SAVED.pdf [--expect ...]       # re-read an already-saved file

EXIT CODES
  0  document fetched + extracted, every --expect figure FOUND
  1  document fetched + extracted, at least one --expect figure NOT FOUND
  2  UNKNOWN — no request shape returned the document, or extraction failed

Run from anywhere; pdfminer comes from the repo venv (.venv/bin/python3).
"""
import argparse
import datetime as dt
import hashlib
import html
import pathlib
import re
import subprocess
import sys

UAS = [
    ("bare-curl", None),
    ("research-bot", "research-bot/1.0"),
    ("browser", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0 Safari/537.36"),
]

# Bodies that are a wall, not the document. Matched case-insensitively on the first 4 KB.
BLOCK_MARKERS = [r"access denied", r"request rejected", r"captcha", r"are you a robot",
                 r"akamai", r"cloudflare", r"enable javascript", r"just a moment",
                 r"error\s*40[34]", r"page not found"]
MIN_BYTES = 2048

DATE_LINE = re.compile(
    r"(for release|embargo|release date|released|transmission of material|"
    r"week ending|(january|february|march|april|may|june|july|august|september|"
    r"october|november|december) \d{1,2}, 20\d\d)", re.I)


def kind_of(data):
    head = data[:1024].lstrip()
    if data[:5] == b"%PDF-":
        return "pdf"
    if head[:1] == b"<" or b"<html" in head.lower():
        return "html"
    sample = data[:8192]
    printable = sum(1 for c in sample if c in (9, 10, 13) or 32 <= c < 127 or c >= 0xC2)
    if sample and printable / len(sample) >= 0.97:
        return "text"   # BLS/DOL also publish plain-text releases (e.g. empsit .txt)
    return "other"


def rejection(data, want_kind):
    """Return a reason string if these bytes are not the document, else None."""
    if len(data) < MIN_BYTES:
        return f"body {len(data)} B < {MIN_BYTES} B (stub)"
    k = kind_of(data)
    if k == "other":
        return "not a PDF, HTML page or plain text (binary or corrupt)"
    if want_kind and k != want_kind:
        return f"expected {want_kind}, got {k}"
    if k != "pdf":
        sample = data[:4096].decode("utf-8", "ignore").lower()
        for m in BLOCK_MARKERS:
            if re.search(m, sample):
                return f"block/stub marker /{m}/ in first 4 KB"
    return None


def fetch(url, out_dir, bust=True):
    want = "pdf" if url.lower().split("?")[0].endswith(".pdf") else None
    stamp = dt.datetime.now().strftime("%Y%m%d%H%M")
    urls = []
    if bust:
        urls.append(url + ("&" if "?" in url else "?") + f"_={stamp}")
    urls.append(url)
    tries = []
    for u in urls:
        for name, ua in UAS:
            cmd = ["curl", "-s", "-L", "--max-time", "40", "-w", "%{http_code}", "-o", "-"]
            if ua:
                cmd += ["-A", ua]
            cmd.append(u)
            try:
                r = subprocess.run(cmd, capture_output=True, timeout=60)
            except subprocess.TimeoutExpired:
                tries.append(f"{name} {u}: timeout")
                continue
            body, code = r.stdout[:-3], r.stdout[-3:].decode("ascii", "ignore")
            why = None if code == "200" else f"HTTP {code}"
            why = why or rejection(body, want)
            tries.append(f"{name} {'busted' if u != url else 'plain'}: HTTP {code}, "
                         f"{len(body)} B, {kind_of(body)} -> {'OK' if not why else 'REJECT: ' + why}")
            if not why:
                ext = {"pdf": ".pdf", "html": ".html"}.get(kind_of(body), ".txt")
                base = re.sub(r"[^A-Za-z0-9._-]+", "_", url.split("://", 1)[-1])[:80]
                path = out_dir / f"{dt.date.today():%Y-%m-%d}_{base}{'' if base.endswith(ext) else ext}"
                path.write_bytes(body)
                return path, tries
    return None, tries


def extract(path):
    data = path.read_bytes()
    if kind_of(data) == "pdf":
        from pdfminer.high_level import extract_text
        return extract_text(str(path))
    t = data.decode("utf-8", "ignore")
    if kind_of(data) == "text":
        return t
    t = re.sub(r"<script.*?</script>|<style.*?</style>", " ", t, flags=re.S | re.I)
    t = re.sub(r"<br\s*/?>|</p>|</tr>|</h\d>|</li>|</div>", "\n", t, flags=re.I)
    return html.unescape(re.sub(r"<[^>]+>", " ", t))


def figure_regex(fig):
    """Match a figure as a whole token: '194,000' must not match inside '1,194,000'."""
    return re.compile(r"(?<![\d.,])" + re.escape(fig) + r"(?![\d])")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("url", nargs="?")
    ap.add_argument("--file", type=pathlib.Path, help="re-read an already-saved file")
    ap.add_argument("--expect", action="append", default=[], help="figure that must appear verbatim")
    ap.add_argument("--show", action="append", default=[], help="regex; print matching lines")
    ap.add_argument("--out", type=pathlib.Path, default=pathlib.Path("."), help="where to save")
    ap.add_argument("--no-bust", action="store_true", help="no cache-busting query string")
    a = ap.parse_args(argv)

    if a.file:
        path = a.file
        if not path.exists():
            print(f"UNKNOWN: {path} does not exist"); return 2
        why = rejection(path.read_bytes(), None)
        if why:
            print(f"UNKNOWN: saved file is not a document — {why}"); return 2
    elif a.url:
        a.out.mkdir(parents=True, exist_ok=True)
        path, tries = fetch(a.url, a.out, bust=not a.no_bust)
        for t in tries:
            print(f"  try  {t}")
        if not path:
            print("UNKNOWN: no request shape returned the document. Do NOT fall back to a "
                  "fetch-tool summary (L-33); grade nothing from this source.")
            return 2
    else:
        ap.error("give a URL or --file")

    data = path.read_bytes()
    print(f"SAVED  {path}  {len(data):,} B  sha256 {hashlib.sha256(data).hexdigest()[:16]}  ({kind_of(data)})")
    try:
        text = extract(path)
    except Exception as e:  # noqa: BLE001 — any extraction failure is UNKNOWN
        print(f"UNKNOWN: extraction failed — {type(e).__name__}: {e}"); return 2
    lines = [re.sub(r"\s+", " ", l).strip() for l in text.splitlines()]
    lines = [l for l in lines if l]
    if len(" ".join(lines)) < 200:
        print("UNKNOWN: extracted text under 200 chars — scanned image or empty document"); return 2

    print("DATE LINES (from the extracted text):")
    for l in [l for l in lines if DATE_LINE.search(l)][:8]:
        print(f"  | {l[:160]}")

    for rx in a.show:
        print(f"SHOW /{rx}/:")
        for l in [l for l in lines if re.search(rx, l, re.I)][:10]:
            print(f"  | {l[:200]}")

    flat = " ".join(lines)
    missing = 0
    for fig in a.expect:
        m = figure_regex(fig).search(flat)
        if m:
            ctx = flat[max(0, m.start() - 80): m.end() + 60]
            print(f"FOUND      {fig}   …{ctx}…")
        else:
            missing += 1
            print(f"NOT FOUND  {fig}   — absent from the extracted text; do not quote or grade it")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
