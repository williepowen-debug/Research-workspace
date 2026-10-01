"""Saved cases for scripts/trepptalk_sweep.py (exit contract, page coverage, date binding, --all).

Built 2026-09-30 for CATO's 9/30 review finding RC4 (verified by PROME, packet 1193d4d7d). Cases R1-R4 are
CATO's four counterexamples, transcribed from AGENTS/CATO/runs/2026-09-30_2132_system-commit-probe.py
(trepp_cases), whose saved output shows the v1 failures: rc 0 on 8/9 fetch failures, "9/9 pages" on 8
parse-empty pages, 12 of 15 undated rows under --all, and the 9/30 post dated 2026-08-01. Cases C1-C5 are
controls, so a fix that simply always exits 2 cannot pass. No network: fetch is mocked; seen_in_desk is mocked.

Run: python3 AGENTS/CREED/scripts/test_trepptalk_sweep.py   (exit 0 = all pass; read-only)
"""
import contextlib
import datetime as dt
import importlib.util
import io
import pathlib
import sys
from unittest.mock import patch

HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("sweep", HERE / "trepptalk_sweep.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

TODAY = dt.date.today()
D = TODAY.strftime("%B %d, %Y")


def card(slug, title, date_text, above=False):
    """A card in Trepp's live shape (div.bop--listing--item block, date in post-item--published BELOW the title),
    or with the date ABOVE the title when above=True."""
    d = f'<span class="post-item--published">{date_text}</span>'
    t = f'<h2><a href="https://www.trepp.com/trepptalk/{slug}" class="no--underline">{title}</a></h2>'
    return f'<div class="bop--listing--item block"><div class="bop--listing--item--title">{(d + t) if above else (t + d)}</div></div>'


def topic_page(*slugs):
    return "".join(card(s, f"Synthetic article {s} long title", D) for s in slugs)


def invoke(argv, fetch, seen=lambda slug, root: []):
    out = io.StringIO()
    with patch.object(sys, "argv", ["t", *argv]), patch.object(mod, "fetch", fetch), \
            patch.object(mod, "seen_in_desk", seen), contextlib.redirect_stdout(out):
        rc = mod.main()
    return rc, out.getvalue()


def by_page(mapping):
    def f(url):
        for p, v in mapping.items():
            if url.endswith(p):
                if isinstance(v, Exception):
                    raise v
                return v
        raise AssertionError(url)
    return f


ALL_OK = {p: topic_page(f"post-{i}") for i, p in enumerate(mod.PAGES)}
ALL_OK["all"] = '<h3><a href="https://www.trepp.com/trepptalk/post-0" class="x">Synthetic article post-0 long title</a></h3>'
SEEN = lambda slug, root: ["AGENTS/CREED/KB.tsv"]
results = []


def check(name, cond, detail=""):
    results.append((name, bool(cond), detail))


# R1 -- eight of nine fetches fail, the one readable page holds a SEEN article: v1 rc 0, NEW 0.
m = {p: TimeoutError("synthetic") for p in mod.PAGES}
m[mod.PAGES[0]] = topic_page("known-article")
rc, out = invoke([], by_page(m), SEEN)
check("R1 8/9 fetch failures -> rc 2, INCOMPLETE", rc == 2 and "INCOMPLETE" in out and "1/9" in out, f"rc={rc}")

# R2 -- eight pages download but parse empty (template change), one SEEN article: v1 printed "9/9 pages", rc 0.
m = {p: "<html>template changed</html>" for p in mod.PAGES}
m[mod.PAGES[0]] = topic_page("known-article")
rc, out = invoke([], by_page(m), SEEN)
check("R2 8/9 parse-empty -> rc 2, not counted as covered", rc == 2 and "1/9" in out and "unusable" in out
      and "9/9" not in out, f"rc={rc}")

# R3 -- fifteen undated NEW posts with --all: v1 showed 12 then advised --all.
many = "".join(f'<h3><a href="https://www.trepp.com/trepptalk/slug-{n:02d}" class="x">Synthetic article {n:02d} title</a></h3>'
               for n in range(15))
m = dict(ALL_OK)
m["all"] = many
rc, out = invoke(["--all"], by_page(m))
shown = sum(1 for n in range(15) if f"/slug-{n:02d}" in out)
check("R3 --all shows all 15 undated rows", shown == 15 and "more undated" not in out, f"shown={shown}")
rc, out = invoke([], by_page(m))
shown = sum(1 for n in range(15) if f"/slug-{n:02d}" in out)
check("R3b default still caps undated NEW at 12 and says how many are hidden", shown == 12 and "3 more undated" in out,
      f"shown={shown}")

# R4 -- dates ABOVE titles (CATO's exact raw, <article> cards): v1 gave the 9/30 post the next card's 8/1 date.
raw = ('<article>September 30, 2026 <a href="https://www.trepp.com/trepptalk/newest-post">Newest office article</a></article>'
       '<article>August 1, 2026 <a href="https://www.trepp.com/trepptalk/older-post">Older office article</a></article>')
got = {s: v[1] for s, v in mod.parse(raw).items()}
check("R4 date-above <article> cards bind to their own card",
      got == {"newest-post": dt.date(2026, 9, 30), "older-post": dt.date(2026, 8, 1)}, str(got))

# C1 -- live template shape, date BELOW title (the layout v1 handled): must still bind correctly.
raw = card("a-post", "First office article title", "September 10th, 2026") + card("b-post", "Second office article title", "August 28th, 2026")
got = {s: v[1] for s, v in mod.parse(raw).items()}
check("C1 live bop card, date below title", got == {"a-post": dt.date(2026, 9, 10), "b-post": dt.date(2026, 8, 28)}, str(got))

# C2 -- live template shape, date ABOVE title.
raw = card("a-post", "First office article title", "September 30, 2026", above=True) + \
      card("b-post", "Second office article title", "August 1, 2026", above=True)
got = {s: v[1] for s, v in mod.parse(raw).items()}
check("C2 live bop card, date above title", got == {"a-post": dt.date(2026, 9, 30), "b-post": dt.date(2026, 8, 1)}, str(got))

# C3 -- no card markers at all: no date is guessed (and a topic page so shaped is UNUSABLE, exit 2).
raw = ('September 30, 2026 <a href="https://www.trepp.com/trepptalk/x-post">An unstructured article</a>'
       ' August 1, 2026 <a href="https://www.trepp.com/trepptalk/y-post">Another unstructured one</a>')
got = {s: v[1] for s, v in mod.parse(raw).items()}
check("C3 no card markers -> no guessed dates", got == {"x-post": None, "y-post": None}, str(got))
m = dict(ALL_OK)
m[mod.PAGES[0]] = raw
rc, out = invoke([], by_page(m), SEEN)
check("C3b topic page with links but no dated cards -> rc 2", rc == 2 and "0 dated inside a card" in out, f"rc={rc}")

# C4 -- full coverage, everything SEEN: the only quiet pass, rc 0.
rc, out = invoke([], by_page(ALL_OK), SEEN)
check("C4 full coverage, nothing new -> rc 0, COMPLETE", rc == 0 and "COMPLETE" in out and "9/9" in out, f"rc={rc}")

# C5 -- full coverage, NEW rows -> rc 1; and partial coverage WITH new rows -> rc 2 but the rows still print.
rc, out = invoke([], by_page(ALL_OK))
check("C5 full coverage, NEW -> rc 1", rc == 1 and "NEW " in out, f"rc={rc}")
m = dict(ALL_OK)
m[mod.PAGES[1]] = TimeoutError("synthetic")
rc, out = invoke([], by_page(m))
check("C5b partial coverage with NEW -> rc 2, NEW rows still printed", rc == 2 and "/post-0" in out, f"rc={rc}")

# C6 -- nothing parses anywhere -> UNAVAILABLE, rc 2.
rc, out = invoke([], lambda url: "<html></html>")
check("C6 nothing parsed -> rc 2 UNAVAILABLE", rc == 2 and "UNAVAILABLE" in out, f"rc={rc}")

w = max(len(n) for n, _, _ in results)
for n, ok, det in results:
    print(f"  {'PASS' if ok else 'FAIL'}  {n.ljust(w)}  {'' if ok else det}")
fails = sum(1 for _, ok, _ in results if not ok)
print(f"{len(results) - fails}/{len(results)} pass")
sys.exit(1 if fails else 0)
