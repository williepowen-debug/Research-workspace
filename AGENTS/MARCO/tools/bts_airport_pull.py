#!/usr/bin/env python3
"""MARCO BTS T-100 airport puller — monthly enplanements by airport, optionally by carrier.

WHY THIS EXISTS
---------------
Two MARCO data gaps were carried for months and BOTH were path problems, not data
problems:

  * MCO was recorded "BLOCKED" from session 16 to session 22 (flymco/GOAA is
    JS-rendered with no downloadable PDF). It gated predictions MAR-22 and MAR-24.
  * FLL's documented route DIED on 2026-08-21 — broward.org was rebuilt as a
    Next.js SPA, the legacy document tree 404s, and search engines still index the
    dead URLs so a link-level check looks healthy until you fetch.

BTS T-100 closes both in one source, and MIA as a third for cross-check. It had
never been tried. ⚠️ `finding_unfetched_is_not_unavailable`: UNCHECKED is not
UNAVAILABLE — classify before writing "blocked".

WHAT THE NUMBERS ARE
--------------------
⚠️ These are **enplanements** (departing passengers on carriers reporting to BTS),
NOT the enplaned+deplaned "total passengers" airports publish. BTS runs roughly
HALF the airport-reported figure — MIA May 2026 is 2.21M here against ~4.6M in
Miami-Dade's own report. **Never compare a BTS level to an airport-reported level.**
YoY and multi-year stacks computed *within* this series are valid and are what
MARCO scores on.

Data runs ~3 months behind (May 2026 available on 2026-08-21).

THE CARRIER SPLIT IS THE POINT
------------------------------
Passing a carrier code turns this from a level feed into a *mechanism* instrument.
MARCO pre-registered that an airport going negative on carrier-failure capacity
deletion rather than visitor withdrawal must resolve TRUE-IN-LETTER / FALSE-IN-
SPIRIT. On 2026-08-21 that test ran for real: MCO's May flip to -1.81% looked like
the predicted demand collapse, but Spirit (NK) went 212,196 -> 3,150 at the
liquidation, removing 276,008 enplanements — **6.4x larger than MCO's entire YoY
decline**. Ex-Spirit MCO GREW +11.13%. Without the carrier split the prediction
would have been scored correct for the wrong reason.

USAGE
    python3 bts_airport_pull.py MCO FLL MIA          # all carriers
    python3 bts_airport_pull.py --carrier NK MCO FLL # one carrier (mechanism test)
"""
import json
import re
import sys
import time
from pathlib import Path

import requests

URL = "https://transtats.bts.gov/Data_Elements.aspx?Data=1"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
OUT = Path(__file__).resolve().parents[1] / "baselines" / "bts_airport_pax.tsv"


def _hidden(html, name):
    """ASP.NET postback tokens. The page is a WebForm — a GET alone returns the
    default airport, so the VIEWSTATE/EVENTVALIDATION pair must be echoed back."""
    m = re.search(r'id="' + name + r'"[^>]*value="([^"]*)"', html)
    return m.group(1) if m else ""


def pull(airport, carrier="All", session=None):
    """Return {(year, month): (domestic, international, total)} of enplanements."""
    s = session or requests.Session()
    s.headers.update({"User-Agent": UA})
    html = s.get(URL, timeout=90).text
    payload = {
        "__VIEWSTATE": _hidden(html, "__VIEWSTATE"),
        "__VIEWSTATEGENERATOR": _hidden(html, "__VIEWSTATEGENERATOR"),
        "__EVENTVALIDATION": _hidden(html, "__EVENTVALIDATION"),
        "__EVENTTARGET": "", "__EVENTARGUMENT": "",
        "CarrierList": carrier, "AirportList": airport, "Submit": "Submit",
    }
    r = s.post(URL, data=payload, timeout=120)
    if r.status_code != 200:
        raise RuntimeError(f"{airport}/{carrier}: HTTP {r.status_code}")
    out = {}
    for row in re.findall(r"<tr[^>]*>(.*?)</tr>", r.text, re.S):
        cells = [re.sub(r"<[^>]+>", "", c).replace("&nbsp;", " ").strip().replace(",", "")
                 for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S)]
        # A data row is YEAR, MONTH, DOMESTIC, INTERNATIONAL, TOTAL. Anchoring on
        # both a 4-digit year AND a 1-2 digit month keeps the TOTAL/summary rows
        # (which carry a blank or text month) out of the monthly series.
        if len(cells) >= 5 and re.fullmatch(r"(19|20)\d\d", cells[0]) \
                and re.fullmatch(r"\d{1,2}", cells[1]):
            try:
                out[(int(cells[0]), int(cells[1]))] = (
                    int(cells[2]), int(cells[3]), int(cells[4]))
            except ValueError:
                continue
    if not out:
        raise RuntimeError(f"{airport}/{carrier}: parsed 0 monthly rows — "
                           f"form layout may have changed; inspect before trusting a cached TSV")
    return out


def main():
    args = [a for a in sys.argv[1:]]
    carrier = "All"
    if "--carrier" in args:
        i = args.index("--carrier")
        carrier = args[i + 1]
        del args[i:i + 2]
    airports = args or ["MCO", "FLL", "MIA"]
    s = requests.Session()
    lines = [f"# MARCO BTS T-100 airport enplanements | carrier={carrier} | "
             f"pulled={time.strftime('%Y-%m-%d')}",
             "# ⚠️ ENPLANEMENTS (departing), NOT airport-reported enplaned+deplaned totals —",
             "#   BTS runs ~HALF the airport figure. Compare YoY/stacks WITHIN this series only.",
             "# Last real data refresh: " + time.strftime("%Y-%m-%d"),
             "airport\tyear\tmonth\tdomestic\tinternational\ttotal"]
    for ap in airports:
        d = pull(ap, carrier, s)
        latest = max(d)
        print(f"  {ap}: {len(d)} monthly rows, latest {latest[0]}-{latest[1]:02d}")
        for (y, m) in sorted(d):
            dom, intl, tot = d[(y, m)]
            lines.append(f"{ap}\t{y}\t{m}\t{dom}\t{intl}\t{tot}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,}B)")


if __name__ == "__main__":
    main()
