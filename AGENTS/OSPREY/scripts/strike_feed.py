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
        # urljoin FIRST, then test link_pattern (DAEDALUS 9/10 finding (3)): an absolute-host
        # pattern silently yields zero items the moment the publisher serves relative hrefs.
        if href.startswith("/") or not re.match(r"[a-z]+:", href):
            from urllib.parse import urljoin; href = urljoin(base, href)
        if link_pattern not in href or href in seen:
            continue
        seen.add(href)
        # date guesses: in the slug or the anchor text
        d = None
        mm = re.search(r"(\d{1,2})(?:st|nd|rd|th)?[- ]+(?:to[- ]+)?(?:\d{1,2}(?:st|nd|rd|th)?[- ]+)?(january|february|march|april|may|june|july|august|september|october|november|december)[- ]+(\d{4})", (href + " " + inner).lower())
        if mm:
            try: d = dt.datetime.strptime(f"{mm[1]} {mm[2]} {mm[3]}", "%d %B %Y").date()
            except ValueError: d = None
        out.append({"title": inner or href.rsplit("/", 1)[-1], "url": href, "summary": "", "date": d})
    return out

DF_MAX = 4          # a token shared by >=4 ledger rows is a CATEGORY, not an identity (DAEDALUS 9/10)
CAND_RE = r"[a-z\u0430-\u044f\u0451\u0456\u0457\u0454\u04390-9\-]{5,}"
PROPER_RE = r"[A-Za-z\u0410-\u044f\u0401\u0451\u0406\u0456\u0407\u0457\u0404\u04540-9\-]{5,}"

def load_ledger(path):
    """Return (rows, stats). Ledger match tokens are PROPER-NOUN tokens of the raw
    Facility+Region cell, minus any token carried by >= DF_MAX rows.

    Why (DAEDALUS review 2026-09-10, measured hold-one-out on this ledger): the v1 rule
    -- any shared lower-cased token >=5 chars not on STOP -- absorbed 15/99 real distinct
    events (terse) into a DIFFERENT strike_id, i.e. DELETED them, because region words
    (tatarstan, bashkortostan, novorossiysk) and generic words (tanker, re-struck, night)
    carried the match. Rows skipped by the parser are COUNTED and printed: the ledger you
    diff against must be visibly the ledger on disk."""
    rows, skipped = [], []
    total = 0
    with open(path, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith("#") or ln.startswith("strike_id\t") or not ln.strip():
                continue
            total += 1
            c = ln.rstrip("\n").split("\t")
            if len(c) < 16:
                skipped.append(f"{(c[0] if c else '?')}: short row ({len(c)} cols)"); continue
            try: d = dt.date.fromisoformat(c[1][:10])
            except ValueError:
                skipped.append(f"{c[0]}: unparseable date {c[1][:12]!r}"); continue
            cell = c[4] + " " + c[5]
            words = {w.lower() for w in re.findall(PROPER_RE, cell) if w[0].isupper()} - STOP
            rows.append({"id": c[0], "date": d, "words": words, "facility": c[4][:60]})
    df = {}
    for r in rows:
        for w in r["words"]: df[w] = df.get(w, 0) + 1
    generic = {w for w, n in df.items() if n >= DF_MAX}
    for r in rows:
        r["words"] = r["words"] - generic
    stats = {"total": total, "usable": len(rows), "skipped": skipped, "generic": sorted(generic)}
    return rows, stats

STOP = {"russia", "russian", "ukraine", "ukrainian", "drone", "drones", "strike", "struck", "attack", "attacks", "refinery", "region", "oblast", "black", "after", "with", "from", "that", "this", "were", "have", "been", "over", "into", "near", "said", "says", "kills", "killed", "military", "forces", "general", "staff", "vessel", "vessels", "cargo", "crude", "terminal", "facility", "facilities", "krasnodar", "leningrad", "waters", "approaches", "district", "republic", "port", "marine"}

def diff(cand, ledger):
    """Return (ledger_match, carrying_tokens, ledger_facility).

    A <strike_id> result is a CLAIM, not a fact -- it is the row a human does not open,
    so it must carry the evidence for its own match (DAEDALUS review finding (2))."""
    if not cand["date"]:
        return ("UNDATED", [], "")
    words = set(re.findall(CAND_RE, (cand["title"] + " " + cand["summary"][:600]).lower())) - STOP
    best = None
    for r in ledger:
        if abs((r["date"] - cand["date"]).days) <= 1:
            shared = words & r["words"]
            if shared and (best is None or len(shared) > best[1]):
                best = (r["id"], len(shared), sorted(shared), r["facility"])
    if not best:
        return ("NONE", [], "")
    return (best[0], best[2], best[3])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=os.path.join(HERE, "strike_feed_config.json"))
    ap.add_argument("--days", type=int, default=None)
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    try:
        cfg = json.load(open(a.config, encoding="utf-8"))
        ledger, lstats = load_ledger(os.path.join(ROOT, cfg["ledger"]))
    except Exception as e:
        print(f"strike_feed: cannot read config/ledger: {e}", file=sys.stderr); return 2
    days = a.days or cfg.get("days_back", 10)
    today = dt.date.today(); cutoff = today - dt.timedelta(days=days)
    atok = [t.lower() for t in cfg["asset_tokens"]]; ptok = [t.lower() for t in cfg["place_tokens"]]; ctok = [t.lower() for t in cfg["context_tokens"]]; mtok = [t.lower() for t in cfg.get("maritime_tokens", [])]
    out_rows, summary, match_rows = [], [], []
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
        # Guard applies to EVERY source kind (DAEDALUS finding (3)): an html_index yielding
        # zero items used to emit no row at all — a dead scraper looked like a quiet week.
        if not items:
            out_rows.append([today.isoformat(), "", sid, "EMPTY_FEED (HTTP 200, zero items — indistinguishable from a bot-block stub; treat as NOT read)", src["url"], "", "", f"kind={src['kind']}"])
        elif len(items) < int(src.get("expect_min_items", 0) or 0):
            out_rows.append([today.isoformat(), "", sid, f"PARSER_STALE ({len(items)} items < expect_min_items {src['expect_min_items']} — the parser, not the source, is the likely cause; treat as NOT fully read)", src["url"], "", "", ""])
        for it in items:
            if it["date"] and it["date"] < cutoff:
                continue
            note, carry, lfac = "", [], ""
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
                match, carry, lfac = diff(it, ledger)
                if carry:
                    note = f"matched on: {','.join(carry)} | ledger facility: {lfac} — CLAIM, not a fact: confirm this is the facility in the headline before dismissing"
            out_rows.append([today.isoformat(), it["date"].isoformat() if it["date"] else "", sid, it["title"][:200], it["url"], ",".join(hit[:8]), match, note])
            if carry:
                match_rows.append([today.isoformat(), it["date"].isoformat() if it["date"] else "", sid, it["title"][:200], it["url"], match, ",".join(carry), lfac])
            kept += 1
        summary.append(f"{sid}: {len(items)} items, {kept} kept")
    os.makedirs(os.path.join(ROOT, cfg["out_dir"]), exist_ok=True)
    outp = os.path.join(ROOT, cfg["out_dir"], f"FEED_CANDIDATES_{today.isoformat()}.tsv")
    with open(outp, "w", encoding="utf-8", newline="") as f:
        f.write("# OSPREY strike feed — fetch-and-diff output. NONE = no STRIKES.tsv row within ±1 day sharing a PROPER-NOUN facility/vessel token (df<4): a human rows it or dismisses it with a reason. A <strike_id> row is a CLAIM, not a fact — its note carries the tokens that made the match; confirm the named ledger facility is the one in the headline before dismissing. FETCH_FAILED / EMPTY_FEED / PARSER_STALE mean the source was NOT read (absent ≠ quiet).\n")
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(COLS)
        for r in out_rows: w.writerow([str(x).replace("\t", " ") for x in r])
    # The COMMITTED audit trail: one line per <strike_id> match with its carrying evidence.
    # FEED_CANDIDATES_*.tsv is git-ignored, so without this file the precision side of the
    # feed is unfalsifiable after the run (DAEDALUS finding (b)); recall alone cannot see a
    # false absorption, because a false <strike_id> produces no NONE row and no KB mention.
    mp = os.path.join(ROOT, cfg["out_dir"], f"MATCHES_{today.isoformat()}.tsv")
    with open(mp, "w", encoding="utf-8", newline="") as f:
        f.write(f"# OSPREY strike feed — COMMITTED match audit trail, run {today.isoformat()}. One row per candidate the diff absorbed into an existing strike_id.\n")
        f.write(f"# ledger: {lstats['total']} data lines, {lstats['usable']} usable, {len(lstats['skipped'])} skipped" + (f" ({'; '.join(lstats['skipped'])})" if lstats["skipped"] else "") + f"; {len(lstats['generic'])} generic tokens dropped at df>={DF_MAX}: {','.join(lstats['generic'])}\n")
        f.write("# Each row is a CLAIM. Precision leg of the acceptance test: of N rows here, M confirmed at the named ledger facility.\n")
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["run_date", "pub_date", "source", "title", "url", "ledger_match", "carrying_tokens", "ledger_facility"])
        for r in match_rows: w.writerow([str(x).replace("\t", " ") for x in r])
    none_n = sum(1 for r in out_rows if r[6] == "NONE"); fail_n = sum(1 for r in out_rows if str(r[3]).startswith(("FETCH_FAILED", "EMPTY_FEED", "PARSER_STALE")))
    if not a.quiet:
        print(f"ledger {lstats['total']} lines, {lstats['usable']} usable, {len(lstats['skipped'])} skipped" + (f" ({'; '.join(lstats['skipped'])})" if lstats["skipped"] else ""))
        print(f"strike_feed {today}: {len(out_rows)} rows -> {os.path.relpath(outp, ROOT)} | NONE={none_n} NOT_READ={fail_n} MATCHED={len(match_rows)} (audit -> {os.path.relpath(mp, ROOT)}) | " + " · ".join(summary))
    return 0

if __name__ == "__main__":
    sys.exit(main())
