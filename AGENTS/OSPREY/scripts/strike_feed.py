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

MONTHS = "january|february|march|april|may|june|july|august|september|october|november|december"
_SEP = r"[\s\-–]+"
WIN_RE = (r"(\d{1,2})(?:st|nd|rd|th)?" + _SEP + r"(?:(" + MONTHS + r")" + _SEP + r")?(?:to" + _SEP + r")?"
          r"(\d{1,2})(?:st|nd|rd|th)?" + _SEP + r"(" + MONTHS + r")" + _SEP + r"(\d{4})")

def bulletin_window(text):
    """(start, end) of a dated-window bulletin ("21st - 27th September 2026", "28th-september-4th-october-2026",
    "22-29-june-2026"), or (None, None). L624: staleness and newest-selection key on the window END -- the
    legacy slug date is the FIRST day of a within-month window and the LAST day of a cross-month one."""
    m = re.search(WIN_RE, (text or "").lower())
    if not m:
        return (None, None)
    d1, m1, d2, m2, y = int(m[1]), m[2], int(m[3]), m[4], int(m[5])
    try:
        end = dt.datetime.strptime(f"{d2} {m2} {y}", "%d %B %Y").date()
        mon1 = m1 or m2
        y1 = y - 1 if dt.datetime.strptime(mon1, "%B").month > end.month else y
        start = dt.datetime.strptime(f"{d1} {mon1} {y1}", "%d %B %Y").date()
    except ValueError:
        return (None, None)
    if not (0 <= (end - start).days <= 14):
        return (None, None)
    return (start, end)

def pick_newest(items, today):
    """L624 (read-1 X2): the followed bulletin is the link with the latest window END, never items[0] --
    document order put an older 'most read' link first and the real newest was dropped with no trace.
    Window read from the anchor TITLE first, slug second (a live slug, ...-7th-13th-september-2026-1, is
    titled 14th-20th September). A START after the run date is a typo, ineligible as newest, and named.
    Returns (item, eligible, notes); eligible=False => no usable date => the row reads BULLETIN_UNDATED."""
    dated, future, notes = [], [], []
    for i, it in enumerate(items):
        s, e = bulletin_window(it["title"]); basis = "title"
        if s is None:
            s, e = bulletin_window(it["url"]); basis = "slug"
        if s is None and it["date"]:
            s = e = it["date"]; basis = "slug date"
        it["win"], it["win_basis"] = (s, e), basis
        if s is None:
            continue
        if s > today:
            future.append(it); continue
        dated.append((e, -i, it))
    if future:
        notes.append(f"{len(future)} link(s) with a FUTURE date ignored as newest: " + ", ".join(f["url"] for f in future[:3]))
    if dated:
        return max(dated, key=lambda x: (x[0], x[1]))[2], True, notes
    return items[0], False, notes

NOT_READ_TITLES = ("FETCH_FAILED", "EMPTY_FEED", "PARSER_STALE")
NOT_READ_MATCHES = ("BULLETIN_STALE", "BULLETIN_UNDATED")

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
        with open(a.config, encoding="utf-8") as cf:
            cfg = json.load(cf)
        ledger, lstats = load_ledger(os.path.join(ROOT, cfg["ledger"]))
    except Exception as e:
        print(f"strike_feed: cannot read config/ledger: {e}", file=sys.stderr); return 2
    days = a.days or cfg.get("days_back", 10)
    today = dt.date.today(); cutoff = today - dt.timedelta(days=days)
    atok = [t.lower() for t in cfg["asset_tokens"]]; ptok = [t.lower() for t in cfg["place_tokens"]]; ctok = [t.lower() for t in cfg["context_tokens"]]; mtok = [t.lower() for t in cfg.get("maritime_tokens", [])]
    out_rows, summary, match_rows = [], [], []
    for src in cfg["sources"]:
        sid = src["id"]
        followed, f_notes, f_label = None, [], ""
        try:
            txt = fetch(src["url"])
            if src["kind"] == "rss":
                items = parse_rss(txt)
            else:
                items = parse_html_index(txt, src.get("link_pattern", ""), src["url"])
        except Exception as e:
            out_rows.append([today.isoformat(), "", sid, "FETCH_FAILED", src["url"], "", "", str(e)[:120]])
            summary.append(f"{sid}: FETCH_FAILED ({str(e)[:60]})"); continue
        n_index = len(items)
        if src.get("follow_newest") and items:
            # L624: ONE followed bulletin -- the newest by window END (pick_newest). Every other index link is
            # dropped here, on body success AND on body failure (read-1 X1: on failure the whole index used to
            # bypass the age filter). Its freshness is LABELLED, never silently assumed (read-1 X2/d_stale).
            followed, eligible, f_notes = pick_newest(items, today)
            followed["followed"] = True
            s, e = followed["win"]
            if not eligible:
                f_label = "BULLETIN_UNDATED — read manually; no usable bulletin date, freshness unknown: treat as NOT read until opened"
            elif e < cutoff:
                f_label = f"BULLETIN_STALE — newest bulletin window ends {e.isoformat()} < cutoff {cutoff.isoformat()} ({(today - e).days} d before run): publisher stopped, or index cached — treat as NOT read"
            else:
                f_label = "BULLETIN — read manually"
            if eligible:
                f_notes.append(f"window {s.isoformat()}..{e.isoformat()} ({followed['win_basis']}); newest of {n_index} index links")
            try:
                body = norm(fetch(followed["url"]))
                followed["summary"] = body[:20000]
                if len(body) < 1500:
                    f_notes.append(f"[body not machine-readable — client-rendered page; open the URL] (body {len(body)} chars"
                                   + ("; EMPTY — possible bot-block stub" if not body else "") + ")")
                items = [followed]
            except Exception as ex:
                stale = "" if f_label.startswith("BULLETIN —") else " | " + f_label.split(" — ")[0]
                out_rows.append([today.isoformat(), followed["date"].isoformat() if followed["date"] else "", sid, "FETCH_FAILED (newest post)", followed["url"], "", "",
                                 str(ex)[:120] + stale + " | " + "; ".join(f_notes)])
                items = []  # the FETCH_FAILED row IS this source's one row
        kept = 0
        # Guard applies to EVERY source kind (DAEDALUS finding (3)): an html_index yielding
        # zero items used to emit no row at all — a dead scraper looked like a quiet week.
        if not n_index:
            out_rows.append([today.isoformat(), "", sid, "EMPTY_FEED (HTTP 200, zero items — indistinguishable from a bot-block stub; treat as NOT read)", src["url"], "", "", f"kind={src['kind']}"])
        elif n_index < int(src.get("expect_min_items", 0) or 0):
            out_rows.append([today.isoformat(), "", sid, f"PARSER_STALE ({n_index} items < expect_min_items {src['expect_min_items']} — the parser, not the source, is the likely cause; treat as NOT fully read)", src["url"], "", "", ""])
        for it in items:
            # The age-filter exemption covers exactly ONE item, the followed bulletin (L624 read-1 ❌9); its
            # freshness is carried by f_label instead (BULLETIN_STALE / BULLETIN_UNDATED count as NOT read).
            if it["date"] and it["date"] < cutoff and not it.get("followed"):
                continue
            note, carry, lfac = "", [], ""
            text = it["title"] + " " + it["summary"]
            ah, ph, ch, mh = tokens_in(text, atok), tokens_in(text, ptok), tokens_in(text, ctok), tokens_in(text, mtok)
            if it.get("followed"):
                hit = ["BULLETIN"] + ah + mh
                match = f_label
                note = "; ".join(f_notes)
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
        summary.append(f"{sid}: {n_index} items, {kept} kept" + (f" (followed: {f_label.split(' — ')[0]})" if followed is not None else ""))
    os.makedirs(os.path.join(ROOT, cfg["out_dir"]), exist_ok=True)
    outp = os.path.join(ROOT, cfg["out_dir"], f"FEED_CANDIDATES_{today.isoformat()}.tsv")
    with open(outp, "w", encoding="utf-8", newline="") as f:
        f.write("# OSPREY strike feed — fetch-and-diff output. NONE = no STRIKES.tsv row within ±1 day sharing a PROPER-NOUN facility/vessel token (df<4): a human rows it or dismisses it with a reason. A <strike_id> row is a CLAIM, not a fact — its note carries the tokens that made the match; confirm the named ledger facility is the one in the headline before dismissing. FETCH_FAILED / EMPTY_FEED / PARSER_STALE (title) and BULLETIN_STALE / BULLETIN_UNDATED (ledger_match) mean the source was NOT read (absent ≠ quiet; stale ≠ quiet).\n")
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
    none_n = sum(1 for r in out_rows if r[6] == "NONE"); fail_n = sum(1 for r in out_rows if str(r[3]).startswith(NOT_READ_TITLES) or str(r[6]).startswith(NOT_READ_MATCHES))
    if not a.quiet:
        print(f"ledger {lstats['total']} lines, {lstats['usable']} usable, {len(lstats['skipped'])} skipped" + (f" ({'; '.join(lstats['skipped'])})" if lstats["skipped"] else ""))
        print(f"strike_feed {today}: {len(out_rows)} rows -> {os.path.relpath(outp, ROOT)} | NONE={none_n} NOT_READ={fail_n} MATCHED={len(match_rows)} (audit -> {os.path.relpath(mp, ROOT)}) | " + " · ".join(summary))
    return 0

if __name__ == "__main__":
    sys.exit(main())
