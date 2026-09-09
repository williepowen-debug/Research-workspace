#!/usr/bin/env python3
"""OSPREY strike feed — fetch-and-diff, no classification (PAT-048 instrument-light).

Built 2026-09-09 on Will's word ("all approved go ahead"), spec in
AGENTS/DAEDALUS/inbox/2026-09-08_from-OSPREY_BUILD-SPEC-strike-feed-*.md.

What it does:  fetch a small config-listed set of dated sources (a weekly maritime
security bulletin index, a vessel-intelligence blog, four RSS feeds), keep items whose
title/summary matches any config token, and DIFF them against STRIKES.tsv on
date +/-1 day + shared facility/vessel token. Emits one TSV per run under
domain/energy-strikes/FEED_CANDIDATES_YYYY-MM-DD.tsv. Fetch failures are ROWS,
never silent skips (an absent feed must look different from a quiet one).

What it must NOT do: classify, score, write STATUS/KB, commit, push, or fetch
paywalled sources. A human rows every NONE.

Usage:  python3 scripts/strike_feed.py [--days N] [--config PATH] [--quiet]
Exit codes: 0 = ran (see summary); 2 = config/ledger unreadable.
"""
import argparse, csv, datetime as dt, html, io, json, os, re, sys, urllib.request, urllib.error
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)  # AGENTS/OSPREY
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.8,ru;q=0.5,uk;q=0.5"}
COLS = ["run_date", "pub_date", "source", "title", "url", "matched_tokens", "ledger_match", "note"]

def fetch(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")

def norm(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", s or ""))).strip()

def tokens_in(text, tokens):
    t = text.lower()
    hits = []
    for k in tokens:
        if len(k) <= 5 and re.fullmatch(r"[a-z\-]+", k):
            if re.search(r"(?<![a-z])" + re.escape(k) + r"(?![a-z])", t): hits.append(k)
        elif k in t:
            hits.append(k)
    return hits

def parse_rss(xml_text):
    items = []
    try:
        root = ET.fromstring(xml_text.encode("utf-8"))
    except ET.ParseError as e:
        raise RuntimeError(f"rss parse error: {e}")
    ns = {"atom": "http://www.w3.org/2005/Atom", "dc": "http://purl.org/dc/elements/1.1/"}
    for it in root.iter("item"):
        title = norm(it.findtext("title"))
        link = (it.findtext("link") or "").strip()
        desc = norm(it.findtext("description"))
        pub = it.findtext("pubDate") or it.findtext("dc:date", namespaces=ns) or ""
        d = None
        try:
            d = parsedate_to_datetime(pub).date() if pub else None
        except Exception:
            m = re.search(r"(\d{4})-(\d{2})-(\d{2})", pub)
            d = dt.date(int(m[1]), int(m[2]), int(m[3])) if m else None
        items.append({"title": title, "url": link, "summary": desc, "date": d})
    if not items:  # Atom
        for it in root.iter("{http://www.w3.org/2005/Atom}entry"):
            title = norm(it.findtext("atom:title", namespaces=ns))
            l = it.find("atom:link", ns); link = l.get("href") if l is not None else ""
            pub = it.findtext("atom:published", namespaces=ns) or it.findtext("atom:updated", namespaces=ns) or ""
            m = re.search(r"(\d{4})-(\d{2})-(\d{2})", pub)
            items.append({"title": title, "url": link, "summary": norm(it.findtext("atom:summary", namespaces=ns)), "date": dt.date(int(m[1]), int(m[2]), int(m[3])) if m else None})
    return items

def parse_html_index(html_text, link_pattern, base):
    seen, out = set(), []
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', html_text, flags=re.S | re.I):
        href, inner = m.group(1), norm(m.group(2))
        if link_pattern not in href or href in seen:
            continue
        if href.startswith("/"):
            from urllib.parse import urljoin; href = urljoin(base, href)
        seen.add(href)
        # date guesses: in the slug or the anchor text
        d = None
        mm = re.search(r"(\d{1,2})(?:st|nd|rd|th)?[- ]+(?:to[- ]+)?(?:\d{1,2}(?:st|nd|rd|th)?[- ]+)?(january|february|march|april|may|june|july|august|september|october|november|december)[- ]+(\d{4})", (href + " " + inner).lower())
        if mm:
            try: d = dt.datetime.strptime(f"{mm[1]} {mm[2]} {mm[3]}", "%d %B %Y").date()
            except ValueError: d = None
        out.append({"title": inner or href.rsplit("/", 1)[-1], "url": href, "summary": "", "date": d})
    return out

def load_ledger(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith("#") or ln.startswith("strike_id\t") or not ln.strip():
                continue
            c = ln.rstrip("\n").split("\t")
            if len(c) < 16: continue
            try: d = dt.date.fromisoformat(c[1][:10])
            except ValueError: continue
            words = set(w for w in re.findall(r"[a-zа-яіїє0-9\-]{5,}", (c[4] + " " + c[5]).lower())) - STOP
            rows.append({"id": c[0], "date": d, "words": words})
    return rows

STOP = {"russia", "russian", "ukraine", "ukrainian", "drone", "drones", "strike", "struck", "attack", "attacks", "refinery", "region", "oblast", "black", "after", "with", "from", "that", "this", "were", "have", "been", "over", "into", "near", "said", "says", "kills", "killed", "military", "forces", "general", "staff", "vessel", "vessels", "cargo", "crude", "terminal", "facility", "facilities", "krasnodar", "leningrad", "waters", "approaches", "district", "republic", "port"}

def diff(cand, ledger):
    if not cand["date"]:
        return "UNDATED"
    words = set(w for w in re.findall(r"[a-zа-яіїє0-9\-]{5,}", (cand["title"] + " " + cand["summary"][:600]).lower())) - STOP
    best = None
    for r in ledger:
        if abs((r["date"] - cand["date"]).days) <= 1:
            shared = words & r["words"]
            if shared and (best is None or len(shared) > best[1]):
                best = (r["id"], len(shared))
    return best[0] if best else "NONE"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=os.path.join(HERE, "strike_feed_config.json"))
    ap.add_argument("--days", type=int, default=None)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    try:
        cfg = json.load(open(a.config, encoding="utf-8"))
        ledger = load_ledger(os.path.join(ROOT, cfg["ledger"]))
    except Exception as e:
        print(f"strike_feed: cannot read config/ledger: {e}", file=sys.stderr); return 2
    days = a.days or cfg.get("days_back", 10)
    today = dt.date.today(); cutoff = today - dt.timedelta(days=days)
    atok = [t.lower() for t in cfg["asset_tokens"]]; ptok = [t.lower() for t in cfg["place_tokens"]]; ctok = [t.lower() for t in cfg["context_tokens"]]; mtok = [t.lower() for t in cfg.get("maritime_tokens", [])]
    out_rows, summary = [], []
    for src in cfg["sources"]:
        sid = src["id"]
        try:
            txt = fetch(src["url"])
            if src["kind"] == "rss":
                items = parse_rss(txt)
            else:
                items = parse_html_index(txt, src.get("link_pattern", ""), src["url"])
                if src.get("follow_newest") and items:
                    newest = items[0]
                    try:
                        body = norm(fetch(newest["url"]))
                        newest["summary"] = body[:20000]
                        if len(body) < 1500:
                            newest["summary"] += " [body not machine-readable — client-rendered page; open the URL]"
                        items = [newest]
                    except Exception as e:
                        out_rows.append([today.isoformat(), "", sid, "FETCH_FAILED (newest post)", newest["url"], "", "", str(e)[:120]])
        except Exception as e:
            out_rows.append([today.isoformat(), "", sid, "FETCH_FAILED", src["url"], "", "", str(e)[:120]])
            summary.append(f"{sid}: FETCH_FAILED ({str(e)[:60]})"); continue
        kept = 0
        if src["kind"] == "rss" and not items:
            out_rows.append([today.isoformat(), "", sid, "EMPTY_FEED (HTTP 200, zero items — indistinguishable from a bot-block stub; treat as NOT read)", src["url"], "", "", ""])
        for it in items:
            if it["date"] and it["date"] < cutoff:
                continue
            text = it["title"] + " " + it["summary"]
            ah, ph, ch, mh = tokens_in(text, atok), tokens_in(text, ptok), tokens_in(text, ctok), tokens_in(text, mtok)
            if src.get("follow_newest"):
                hit = ["BULLETIN"] + ah + mh
                match = "BULLETIN — read manually"
            else:
                # keep rule: an ASSET token; OR a PLACE token with a strike/drone or maritime token; OR maritime + strike/drone
                if not (ah or (ph and (ch or mh)) or (mh and ch)):
                    continue
                hit = ah + ph + mh + ch
                match = diff(it, ledger)
            out_rows.append([today.isoformat(), it["date"].isoformat() if it["date"] else "", sid, it["title"][:200], it["url"], ",".join(hit[:8]), match, ""])
            kept += 1
        summary.append(f"{sid}: {len(items)} items, {kept} kept")
    os.makedirs(os.path.join(ROOT, cfg["out_dir"]), exist_ok=True)
    outp = os.path.join(ROOT, cfg["out_dir"], f"FEED_CANDIDATES_{today.isoformat()}.tsv")
    with open(outp, "w", encoding="utf-8", newline="") as f:
        f.write("# OSPREY strike feed — fetch-and-diff output. NONE = no STRIKES.tsv row within ±1 day sharing a facility/vessel token: a human rows it or dismisses it with a reason. FETCH_FAILED rows mean the source was NOT read (absent ≠ quiet).\n")
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(COLS)
        for r in out_rows: w.writerow([str(x).replace("\t", " ") for x in r])
    none_n = sum(1 for r in out_rows if r[6] == "NONE"); fail_n = sum(1 for r in out_rows if str(r[3]).startswith(("FETCH_FAILED", "EMPTY_FEED")))
    if not a.quiet:
        print(f"strike_feed {today}: {len(out_rows)} rows -> {os.path.relpath(outp, ROOT)} | NONE={none_n} FETCH_FAILED={fail_n} | " + " · ".join(summary))
    return 0

if __name__ == "__main__":
    sys.exit(main())
