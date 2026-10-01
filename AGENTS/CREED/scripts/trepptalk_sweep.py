#!/usr/bin/env python3
"""CREED TreppTalk listing sweep (process approved by Will 2026-09-30, in-session).

STATUS 2026-10-01: MANUAL TOOL. Will declined wiring it into boot (and a WALTER intake hand-off) on 2026-10-01;
run it by hand when a session is about Trepp.
REPAIRED 2026-09-30 evening (CATO 9/30 review RC4, verified by PROME, packet 1193d4d7d). The v1 reported a
quiet success on incomplete coverage. Four defects fixed, each pinned by a saved case in
scripts/test_trepptalk_sweep.py (CATO's four, plus controls):
  (1) a failed page fetch now makes the run INCOMPLETE (exit 2), never a quiet 0;
  (2) a page that downloads but parses to nothing usable is counted as UNUSABLE, not as a covered page;
  (3) a date binds to its OWN card (card boundaries, not the gap to the next link), so a date-above-title
      layout can no longer hand one post the next post's date;
  (4) --all shows every row (v1 capped undated rows at 12 even under --all).
KNOWN LIMITS (unfixed): (a) rows that appear only on the 'all' page stay undated, because its entries
carry no date; (b) SEEN = the slug string appears somewhere under AGENTS/CREED/, which is not proof of a
substantive read, and a slug quoted in this script would read SEEN; (c) the card and link regexes are tied
to Trepp's current HubSpot template. A template change now fails CLOSED per page (UNUSABLE -> exit 2).

Fetches Trepp's public TreppTalk listing pages, lists every post dated within the window,
and marks each SEEN (its URL slug appears anywhere under AGENTS/CREED/) or NEW.
Read-only. Never writes.
Exit contract:
  0 = EVERY page fetched and parsed usably, and nothing is new  (the only quiet pass)
  1 = every page fetched and parsed usably, and there are NEW rows to look at
  2 = coverage INCOMPLETE or UNKNOWN: a page failed to fetch or parsed unusable, or nothing parsed.
      A 2 is NOT a pass, even when no NEW row printed: say "sweep incomplete" in the session record.
      NEW rows found on the pages that did work are still printed and still need a look.
A topic page is USABLE only if it yields >=1 post and >=1 post dated inside its own card. The 'all'
page is usable if it yields >=1 post (its entries carry no dates by design).

Why it exists: in September 2026 Trepp published >10 property-type refinancing screens
(office sub-breakeven DSCR 8/20 + 8/28, office LTV 8/17, LA lease rollover 8/21, Florida MF
insurance 8/27, TPPI 6/11 ...) and CREED found them only when Will pasted links on 9/30.
A listing fetch costs seconds; a missed office screen costs a session.

Usage: python3 AGENTS/CREED/scripts/trepptalk_sweep.py [--days 45] [--all]
  --all  prints every row, SEEN included (default: NEW only, a count of SEEN, at most 12 undated NEW)
"""
import re, sys, os, html, subprocess, argparse, datetime, urllib.request

BASE = "https://www.trepp.com/trepptalk/"
PAGES = ["topic/office-real-estate", "topic/industrial-real-estate", "topic/multifamily-real-estate",
         "topic/retail-real-estate", "topic/lodging-real-estate", "topic/self-storage-real-estate",
         "topic/operating-expenses", "topic/cmbs-news", "all"]  # dated topic cards first; 'all' last (its entries carry no date)
UNDATED_PAGES = {"all"}
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
DATE_RE = re.compile(r'((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?) (\d{1,2})(?:st|nd|rd|th)?,? (20\d\d)')
LINK_RE = re.compile(r'href="(https://www\.trepp\.com/trepptalk/(?!topic/|author/|all\b|page/)([^"#?/]+))"[^>]*>\s*([^<]{12,220})<')
# Card starts: Trepp's live template (<div class="bop--listing--item block">, checked 2026-09-30) or a generic
# <article>. The class must be exactly the bare token, not bop--listing--item--title and friends.
CARD_RE = re.compile(r'<article\b|class="(?:[^"]*\s)?bop--listing--item(?:\s[^"]*)?"')
UNDATED_CAP = 12


def fetch(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "ignore")


def to_date(m):
    mon = MONTHS.get(m.group(1)[:3].lower())
    try:
        return datetime.date(int(m.group(3)), mon, int(m.group(2))) if mon else None
    except ValueError:
        return None


def parse(raw):
    """slug -> (title, date or None, url). A date is taken ONLY from inside the post's own card.
    Without card markers no date is assigned at all: the gap between two links is ambiguous
    (date below this title, or above the next), so guessing would misdate posts silently."""
    out = {}
    starts = [m.start() for m in CARD_RE.finditer(raw)]
    for m in LINK_RE.finditer(raw):
        url, slug, title = m.group(1), m.group(2), html.unescape(m.group(3).strip())
        if title.lower().startswith("read more") or slug in out:
            continue
        date = None
        if starts:
            before = [s for s in starts if s <= m.start()]
            if before:
                lo = before[-1]
                after = [s for s in starts if s > m.start()]
                hi = after[0] if after else len(raw)
                d = DATE_RE.search(raw, lo, hi)
                date = to_date(d) if d else None
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
    posts, failed, unusable = {}, [], []
    for p in PAGES:
        try:
            got = parse(fetch(BASE + p))
        except Exception as e:  # noqa
            failed.append(f"{p}: {type(e).__name__}")
            continue
        n_dated = sum(1 for v in got.values() if v[1] is not None)
        if not got:
            unusable.append(f"{p}: 0 posts parsed")
        elif p not in UNDATED_PAGES and n_dated == 0:
            unusable.append(f"{p}: {len(got)} posts, 0 dated inside a card")
        for k, v in got.items():
            if k not in posts or (posts[k][1] is None and v[1] is not None):
                posts[k] = v
    usable = len(PAGES) - len(failed) - len(unusable)
    complete = usable == len(PAGES)
    if not posts:
        print(f"TREPPTALK SWEEP UNAVAILABLE -- no posts parsed; {len(failed)} page(s) failed {failed}, "
              f"{len(unusable)} unusable {unusable}. NOT a pass.")
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
    state = "COMPLETE" if complete else "INCOMPLETE -- NOT a pass"
    print(f"TREPPTALK SWEEP -- {today} -- coverage {state}: {usable}/{len(PAGES)} pages fetched AND parsed usably; "
          f"{len(posts)} posts; {len(rows)} within {a.days}d (or undated); NEW {len(new)} / SEEN {len(rows) - len(new)}")
    if failed:
        print(f"  ⛔ pages failed to fetch: {failed}")
    if unusable:
        print(f"  ⛔ pages fetched but parsed unusable (template change?): {unusable}")
    undated_shown = hidden = 0
    for date, slug, title, url, hits in rows:
        tag = "NEW " if not hits else "SEEN"
        if tag == "SEEN" and not a.all:
            continue
        if date == datetime.date.min:
            undated_shown += 1
            if undated_shown > UNDATED_CAP and not a.all:
                hidden += 1
                continue
        ds = date.isoformat() if date != datetime.date.min else "undated  "
        print(f"  {tag}  {ds}  {title[:96]}")
        print(f"        {url}" + (f"   [{hits[0]}]" if hits else ""))
    if hidden:
        print(f"  ... {hidden} more undated NEW rows not shown (only on the 'all' page, which carries no dates; --all to list)")
    print("  A NEW row is a prompt to LOOK, not a signal. 'SEEN' = the slug appears somewhere under AGENTS/CREED/, "
          "which is not proof it was read closely.")
    if not complete:
        print("  ⛔ Coverage incomplete: exit 2. A quiet result here does NOT mean nothing new was published.")
        return 2
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main())
