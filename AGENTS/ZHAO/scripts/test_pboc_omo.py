"""Closure tests for CATO MC1 (2026-11-10): the PBOC rate check must not pass on an OLDER notice.
Run: python3 AGENTS/ZHAO/scripts/test_pboc_omo.py   (offline; fake fetch, no network)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import boot  # noqa: E402

LIST = "https://example.test/list/index.html"


def notice(rate_cell, fixed=True):
    kind = "固定利率、数量招标" if fixed else "利率招标"
    return (f"<html><body><p>2026-11-11 09:20</p><p>{kind}</p>"
            f"<table><tr><td>隔夜</td><td>{rate_cell}</td></tr></table></body></html>")


def site(*pages):
    """pages newest-first: list of notice HTML strings."""
    links = "".join(f'<a href="n{i}.html">公开市场业务交易公告 [2026]第{220 - i}号</a>'
                    for i in range(len(pages)))
    docs = {LIST: f"<html>{links}</html>"}
    for i, p in enumerate(pages):
        docs[f"https://example.test/list/n{i}.html"] = p

    def fetch(url):
        return docs[url]
    return fetch


def down(url):
    raise RuntimeError("HTTP 503")


CASES = [
    # (name, fetch, stored, expected decided, expected alert, substring in text)
    ("MC1: newest malformed (full-width %) 1.50 + older 1.25, stored 1.25 => UNAVAILABLE, not match",
     site(notice("1.50％"), notice("1.25 %")), "1.25 overnight", False, 0, "UNAVAILABLE"),
    ("ordinary latest match", site(notice("1.25 %")), "1.25 overnight", True, 0, "matches"),
    ("ordinary latest mismatch", site(notice("1.10 %")), "1.25 overnight", True, 1, "MISMATCH"),
    ("non-fixed-rate newest is skipped, older fixed-rate read",
     site(notice("1.30 %", fixed=False), notice("1.25 %")), "1.25 overnight", True, 0, "第219号"),
    ("network failure => UNAVAILABLE, age test decides", down, "1.25 overnight", False, 0, "UNAVAILABLE"),
]


def main():
    fails = 0
    for name, fetch, stored, dec, alert, sub in CASES:
        d, a, text = boot._pboc_source_verdict(stored, False, LIST, fetch)
        ok = (d == dec and a == alert and sub in text)
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {name}\n      -> decided={d} alert={a} {text}")
    print(f"\n{len(CASES) - fails}/{len(CASES)} passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
