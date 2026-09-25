#!/usr/bin/env python3
"""WATCH_FOR harness — WALTER's test step under WQ-295 R3 (PROME record
PROME/proposals/2026-09-25_wq295-dark-desk-class-PROPOSAL.md).

Tests an owner's proposed WATCH_FOR phrases against the lane's REAL matcher
(`match_watch_for` in RESEARCH-INTAKE scripts/newsweep_config.py) over the
lane's own headline history, entirely in memory. Nothing is written to the
lane repo, which stays read-only to WALTER (charter 7e(a)).

Output per phrase: hit count + every hit headline (date | title). The tool does
NOT decide true vs false: a hit is a CANDIDATE for a human/agent reader to
classify. Under R3 a phrase with >0 FALSE hits is rejected by name; true hits are
the point. Exit 0 always on a completed run; rc 2 if the lane cannot be read.

Known matcher behaviour it surfaces (why the tool exists): words of <=3 chars
are dropped, so "PJM Max Gen" reduces to "PJM" (150 hits on 2026-09-25); ALL-CAPS
tokens of 2-5 chars are REQUIRED entity tokens matched case-sensitively.

Usage (from repo root):
  python3 AGENTS/WALTER/tools/watch_for_harness.py --desk WATT --phrase "PJM Maximum Generation" --phrase "PJM Max Gen"
  python3 AGENTS/WALTER/tools/watch_for_harness.py --desk CORAL --file /path/phrases.txt [--since 2026-08-01] [--show 8]
  python3 AGENTS/WALTER/tools/watch_for_harness.py --desk WATT --current      # re-test the list already landed
  --synthetic "headline"   (repeatable) positive controls, labelled SYNTHETIC in the output
  --live "google news query" (repeatable) ALSO test on a live Google-News RSS sample (last --live-days)

WHY --live EXISTS (2026-09-25, WALTER's own error): a 0-hit LANE result is UNINFORMATIVE when no
lane query fetches the phrase's subject. Four VULCAN phrases passed lane-only (0 hits) and then hit
76 / 77 / 2 / 6 false on live headlines, because the lane window ended before the Oracle
force-majeure story and never fetches export-control or Taiwan news. A lane-only run therefore
prints a warning, and every verdict should cite a live sample for any subject the lane does not fetch.
"""
import argparse, collections, glob, json, os, sys

LANE = "/home/willi/Research-Intake"


def load_matcher():
    sys.path.insert(0, os.path.join(LANE, "scripts"))
    try:
        import newsweep_config as C
    except Exception as e:  # lane absent / unreadable
        print(f"CANNOT-EVALUATE: lane matcher not importable from {LANE}/scripts ({e})")
        sys.exit(2)
    return C


def headlines(since):
    files = sorted(glob.glob(os.path.join(LANE, "data", "20*", "news.json")))
    files = [f for f in files if os.path.basename(os.path.dirname(f)) >= since]
    seen, out = set(), []
    for f in files:
        day = os.path.basename(os.path.dirname(f))
        try:
            x = json.load(open(f))
        except Exception as e:
            print(f"WARN unreadable {f}: {e}")
            continue
        items = x["items"] if isinstance(x, dict) and "items" in x else x
        for i in items if isinstance(items, list) else []:
            t = i.get("title", "") if isinstance(i, dict) else ""
            if t and t not in seen:
                seen.add(t)
                out.append((day, t))
    return files, out


def live_headlines(queries, days):
    import html, re, urllib.parse, urllib.request
    out = []
    for q in queries:
        url = ("https://news.google.com/rss/search?" + urllib.parse.urlencode(
            {"q": f"{q} when:{days}d", "hl": "en-US", "gl": "US", "ceid": "US:en"}))
        try:
            x = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read().decode("utf-8", "ignore")
        except Exception as e:
            print(f"WARN live fetch failed for {q!r}: {e}")
            continue
        out += [html.unescape(t) for t in re.findall(r"<item>.*?<title>(.*?)</title>", x, re.S)]
    return list(dict.fromkeys(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desk", required=True)
    ap.add_argument("--phrase", action="append", default=[])
    ap.add_argument("--file")
    ap.add_argument("--current", action="store_true", help="test the list already in WATCH_FOR[desk]")
    ap.add_argument("--synthetic", action="append", default=[])
    ap.add_argument("--since", default="2000-01-01")
    ap.add_argument("--show", type=int, default=10)
    ap.add_argument("--live", action="append", default=[], help="Google-News query for a live sample (repeatable)")
    ap.add_argument("--live-days", type=int, default=30)
    a = ap.parse_args()

    C = load_matcher()
    phrases = list(a.phrase)
    if a.file:
        phrases += [l.strip() for l in open(a.file) if l.strip() and not l.lstrip().startswith("#")]
    if a.current:
        phrases += list(C.WATCH_FOR.get(a.desk, []))
    phrases = list(dict.fromkeys(phrases))
    if not phrases:
        print("CANNOT-EVALUATE: no phrases given")
        sys.exit(2)

    C.WATCH_FOR = {a.desk: phrases}  # in memory only; the module file is never written
    files, heads = headlines(a.since)
    if not files:
        print(f"CANNOT-EVALUATE: no lane news.json on/after {a.since}")
        sys.exit(2)
    hits = collections.defaultdict(list)
    for day, t in heads:
        for _, item in C.match_watch_for(t):
            hits[item].append((day, t))

    first = os.path.basename(os.path.dirname(files[0]))
    last = os.path.basename(os.path.dirname(files[-1]))
    print(f"WATCH_FOR harness — desk {a.desk} · {len(phrases)} phrase(s) · {len(heads)} unique headlines "
          f"over {len(files)} lane days {first} → {last} · real matcher, in memory")
    for p in phrases:
        h = hits.get(p, [])
        tag = "0 hits (zero noise; recall UNPROVEN)" if not h else f"{len(h)} hit(s) — CLASSIFY each true/false"
        print(f"\n[{len(h):4d}] {p}   ← {tag}")
        for day, t in h[: a.show]:
            print(f"        {day} | {t[:140]}")
        if len(h) > a.show:
            print(f"        … {len(h) - a.show} more")
    if a.live:
        live = live_headlines(a.live, a.live_days)
        lh = collections.defaultdict(list)
        for t in live:
            for _, item in C.match_watch_for(t):
                lh[item].append(t)
        print(f"\n=== LIVE sample: {len(live)} unique Google-News headlines, {len(a.live)} query(ies), last {a.live_days}d ===")
        if not live:
            print("CANNOT-EVALUATE (live): the RSS fetch returned nothing; do not read the zeros below as clean")
        for p in phrases:
            h = lh.get(p, [])
            print(f"[{len(h):4d}] {p}" + ("" if h else "   ← 0 live hits"))
            for t in h[: a.show]:
                print(f"        | {t[:140]}")
    else:
        print("\n⚠️  LANE-ONLY RUN: a 0-hit result is UNINFORMATIVE for any subject no lane query fetches. "
              "Re-run with --live \"<subject query>\" before calling such a phrase clean.")
    for s in a.synthetic:
        print(f"\nSYNTHETIC control: {s[:110]} -> {[m[1] for m in C.match_watch_for(s)]}")
    print("\nVerdict rule (WQ-295 R3): reject by name any phrase with >0 FALSE hits; the reader classifies, not this tool.")


if __name__ == "__main__":
    main()
