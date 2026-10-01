#!/usr/bin/env python3
"""CREED TreppTalk listing sweep (process approved by Will 2026-09-30, in-session).

STATUS 2026-09-30 ~20:5x ET: WORKING, NOT WIRED. It runs end to end (210 posts parsed, 9/9 pages),
but it is NOT yet a boot step: wiring it into CLAUDE.md is a charter edit, owed to Will next session.
KNOWN LIMITS (unfixed): (1) ~14 rows stay undated because they appear only on the 'all' page, whose
cards carry no date; (2) SEEN = the slug string appears somewhere under AGENTS/CREED/, so on first use
nearly everything reads NEW, and a slug quoted in this script's own docstring would read SEEN;
(3) the HTML regexes are tied to Trepp's current HubSpot template and will fail closed (exit 2) if it changes.

Fetches Trepp's public TreppTalk listing pages, lists every post dated within the window,
and marks each SEEN (its URL slug appears anywhere under AGENTS/CREED/) or NEW.
Read-only. Never writes. Exit 0 = nothing new; 1 = new items to look at; 2 = sweep could
not run (network / parse) -- a 2 is NOT a pass: say "sweep unavailable" in the session record.

Why it exists: in September 2026 Trepp published >10 property-type refinancing screens
(office sub-breakeven DSCR 8/20 + 8/28, office LTV 8/17, LA lease rollover 8/21, Florida MF
insurance 8/27, TPPI 6/11 ...) and CREED found them only when Will pasted links on 9/30.
A listing fetch costs seconds; a missed office screen costs a session.

Usage: python3 AGENTS/CREED/scripts/trepptalk_sweep.py [--days 45] [--all]
  --all  prints SEEN rows too (default: NEW only, plus a count of SEEN)
"""
import re, sys, os, html, subprocess, argparse, datetime, urllib.request

BASE = "https://www.trepp.com/trepptalk/"
PAGES = ["topic/office-real-estate", "topic/industrial-real-estate", "topic/multifamily-real-estate",
         "topic/retail-real-estate", "topic/lodging-real-estate", "topic/self-storage-real-estate",
         "topic/operating-expenses", "topic/cmbs-news", "all"]  # dated topic cards first; 'all' last (its cards carry no date)
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
DATE_RE = re.compile(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?) (\d{1,2})(?:st|nd|rd|th)?,? (20\d\d)')
LINK_RE = re.compile(r'href="(https://www\.trepp\.com/trepptalk/(?!topic/|author/|all\b|page/)([^"#?/]+))"[^>]*>\s*([^<]{12,220})<')


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def parse(raw):
    out = {}
    matches = list(LINK_RE.finditer(raw))
    for i, m in enumerate(matches):
        url, slug, title = m.group(1), m.group(2), html.unescape(m.group(3).strip())
        if title.lower().startswith("read more") or slug in out:
            continue
        end = matches[i + 1].start() if i + 1 < len(matches) else m.end() + 1500
        d = DATE_RE.search(raw[m.end():min(end, m.end() + 1500)])  # this card only, never the next card's date
        if not d:  # some layouts print the date ABOVE the title: look back, but not past the previous card
            start = matches[i - 1].end() if i > 0 else max(0, m.start() - 600)
            d = DATE_RE.search(raw[max(start, m.start() - 600):m.start()])
        date = None
        if d:
            mon = MONTHS.get(d.group(1)[:3].lower())
            if mon:
                date = datetime.date(int(d.group(3)), mon, int(d.group(2)))
        out[slug] = (title, date, url)
    return out


def seen_in_desk(slug, root):
    # grep -rlF: literal slug anywhere under AGENTS/CREED (KB, board_log, research, catchups, packets)
    r = subprocess.run(["grep", "-rlF", "--include=*.tsv", "--include=*.md", "--include=*.txt", slug,
                        os.path.join(root, "AGENTS", "CREED")], capture_output=True, text=True)
    return [p.replace(root + "/", "") for p in r.stdout.split()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=45)
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    today = datetime.date.today()
    posts, failed = {}, []
    for p in PAGES:
        try:
            for k, v in parse(fetch(BASE + p)).items():
                if k not in posts or (posts[k][1] is None and v[1] is not None):
                    posts[k] = v
        except Exception as e:  # noqa
            failed.append(f"{p}: {type(e).__name__}")
    if not posts:
        print(f"TREPPTALK SWEEP UNAVAILABLE -- no posts parsed ({len(failed)} page(s) failed: {failed}). NOT a pass.")
        return 2
    cutoff = today - datetime.timedelta(days=a.days)
    rows = []
    for slug, (title, date, url) in posts.items():
        if date is not None and date < cutoff:
            continue
        hits = seen_in_desk(slug, root)
        rows.append((date or datetime.date.min, slug, title, url, hits))
    rows.sort(key=lambda r: r[0], reverse=True)
    new = [r for r in rows if not r[4]]
    print(f"TREPPTALK SWEEP -- {today} -- {len(posts)} posts parsed from {len(PAGES) - len(failed)}/{len(PAGES)} pages; "
          f"{len(rows)} within {a.days}d (or undated); NEW {len(new)} / SEEN {len(rows) - len(new)}")
    if failed:
        print(f"  ⚠️  pages failed: {failed}")
    undated_shown = 0
    for date, slug, title, url, hits in rows:
        tag = "NEW " if not hits else "SEEN"
        if tag == "SEEN" and not a.all:
            continue
        if date == datetime.date.min:
            undated_shown += 1
            if undated_shown > 12:
                continue
        ds = date.isoformat() if date != datetime.date.min else "undated  "
        print(f"  {tag}  {ds}  {title[:96]}")
        print(f"        {url}" + (f"   [{hits[0]}]" if hits else ""))
    n_und = sum(1 for r in rows if r[0] == datetime.date.min and not r[4])
    if n_und > 12:
        print(f"  ... {n_und - 12} more undated NEW rows not shown (only on the 'all' page, which carries no dates; --all to list)")
    print("  A NEW row is a prompt to LOOK, not a signal. 'SEEN' = the slug appears somewhere under AGENTS/CREED/, "
          "which is not proof it was read closely.")
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
