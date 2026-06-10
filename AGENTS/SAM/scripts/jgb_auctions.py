#!/usr/bin/env python3
"""
SAM JGB Auction Result Parser
Fetches and parses MOF JGB auction result pages.

URL pattern:
  https://www.mof.go.jp/english/policy/jgbs/auction/calendar/eresul/eresul{YYYYMMDD}.htm

Extracts:
  - Security type (e.g., "30-Year")
  - Competitive bids, bids accepted
  - Lowest accepted price + yield
  - Weighted average price + yield
  - Computes: BTC ratio, tail (bp)

Alerts:
  🔴 BTC < 2.0x  → buyer strike / insurer capitulation
  🟠 BTC < 2.5x  → demand softening
  🟠 Tail > 5bp  → demand quality problem (like Apr 2 10Y: 0.36 tail)

Appends to workbook/JGB_AUCTIONS.tsv.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_auctions.py                    # auto: today or most recent
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_auctions.py --date 2026-04-14  # specific date
  .venv/bin/python3 AGENTS/SAM/scripts/jgb_auctions.py --catalog          # fetch all auctions in CATALYSTS.tsv
"""

import re
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
DOCKET = SAM_DIR / "docket"
AUCTIONS_TSV = WORKBOOK / "JGB_AUCTIONS.tsv"
CATALYSTS_TSV = DOCKET / "CATALYSTS.tsv"

MOF_URL_TEMPLATE = "https://www.mof.go.jp/english/policy/jgbs/auction/calendar/eresul/eresul{ymd}.htm"

HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}


def jst_today():
    """Today's date in JST (UTC+9). MOF publishes results under JST dates;
    probing from the local (ET) date misses a result that is already live —
    e.g. a Jun-10 JST auction posted ~12:35 PM JST is still 'Jun 9' in ET."""
    return (datetime.now(timezone.utc) + timedelta(hours=9)).date()

TSV_HEADER = "Date\tSecurity\tIssue\tCompetitive_Bids_B\tAccepted_B\tBTC_Ratio\tLowest_Yield_Pct\tAverage_Yield_Pct\tTail_BP\tStatus\n"


def fetch_auction_page(date_obj):
    """Fetch MOF auction result HTML for a given date. Returns text or None."""
    ymd = date_obj.strftime("%Y%m%d")
    url = MOF_URL_TEMPLATE.format(ymd=ymd)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace"), url
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, url
        return None, url
    except Exception:
        return None, url


def strip_tags(html_fragment):
    """Remove HTML tags and collapse whitespace."""
    text = re.sub(r"<[^>]+>", " ", html_fragment)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def parse_auction(html, date_obj):
    """
    Parse MOF auction result HTML. Returns dict or None.
    MOF layout: a single data table with header + one data row.
    Header cells + data cells share the same visual order.
    """
    if not html:
        return None

    # Find the data row — contains a date in M/D/YYYY format matching the
    # auction date (e.g., "4/7/2026"). Scope to the first <tr> that contains
    # a date cell resembling the target.
    date_str = f"{date_obj.month}/{date_obj.day}/{date_obj.year}"

    # Split into <tr> blocks
    tr_blocks = re.findall(r"<tr[^>]*>(.*?)</tr>", html, re.DOTALL | re.IGNORECASE)
    data_row = None
    for block in tr_blocks:
        if date_str in block and "<td" in block.lower():
            data_row = block
            break

    if not data_row:
        # Fallback: find any row with a <td> containing "Year" (security type)
        for block in tr_blocks:
            if re.search(r"<td[^>]*>[^<]*Year", block) and "billion" not in block.lower():
                data_row = block
                break

    if not data_row:
        return None

    # Extract cells
    cells_html = re.findall(r"<td[^>]*>(.*?)</td>", data_row, re.DOTALL | re.IGNORECASE)
    cells = [strip_tags(c) for c in cells_html]

    if len(cells) < 13:
        return None

    # Based on observed structure (see docstring):
    #  0: Security (e.g., "30-Year")
    #  1: Issue Number
    #  2: Auction Date
    #  3: Issue Date
    #  4: Maturity Date
    #  5: Nominal Coupon
    #  6: Competitive Bids (billion yen)
    #  7: Bids Accepted (billion yen)
    #  8: Lowest Accepted Price
    #  9: Yield at Lowest Accepted Price
    #  10: Allotment at Lowest
    #  11: Weighted Average Price
    #  12: Yield at Average Price
    #  13: Non-comp I
    #  14: Non-comp II
    def num(s):
        s = s.replace(",", "").replace("%", "").strip()
        try:
            return float(s)
        except ValueError:
            return None

    try:
        security = cells[0]
        issue = cells[1]
        comp_bids = num(cells[6])
        accepted = num(cells[7])
        lowest_yield = num(cells[9])
        avg_yield = num(cells[12])
    except IndexError:
        return None

    if comp_bids is None or accepted is None or accepted == 0:
        return None

    btc = comp_bids / accepted
    tail_bp = None
    if lowest_yield is not None and avg_yield is not None:
        tail_bp = (lowest_yield - avg_yield) * 100  # convert % to bp

    # Status classification
    # Normal JGB auctions: BTC 3.0-3.5x, tail 0.5-2bp
    # Thresholds are safety nets — real signal is relative to rolling avg,
    # which requires history (future enhancement).
    status = "✅ Orderly"
    if btc < 2.0:
        status = "🔴 BUYER STRIKE"
    elif btc < 2.8 and (tail_bp is not None and tail_bp > 3):
        status = "🟠 Soft demand + quality problem"
    elif btc < 2.8:
        status = "🟠 Soft demand"
    elif tail_bp is not None and tail_bp > 5:
        status = "🟠 Quality problem"

    return {
        "date": date_obj.strftime("%Y-%m-%d"),
        "security": security,
        "issue": issue,
        "comp_bids_b": comp_bids,
        "accepted_b": accepted,
        "btc": btc,
        "lowest_yield_pct": lowest_yield,
        "avg_yield_pct": avg_yield,
        "tail_bp": tail_bp,
        "status": status,
    }


def _fmt(value, spec):
    """Format a value, returning empty string for None.
    Some auction formats (e.g., Climate Transition Bond uniform-price)
    omit weighted-average columns, leaving avg_yield_pct / tail_bp as None.
    """
    if value is None:
        return ""
    return format(value, spec)


def append_tsv(result):
    """Append result row to TSV, idempotent on (date, security)."""
    existing = set()
    if AUCTIONS_TSV.exists():
        with open(AUCTIONS_TSV) as f:
            next(f, None)
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) >= 2:
                    existing.add((parts[0], parts[1]))
    else:
        with open(AUCTIONS_TSV, "w") as f:
            f.write(TSV_HEADER)

    key = (result["date"], result["security"])
    if key in existing:
        return False

    with open(AUCTIONS_TSV, "a") as f:
        f.write(
            f"{result['date']}\t{result['security']}\t{result['issue']}\t"
            f"{_fmt(result['comp_bids_b'], '.1f')}\t{_fmt(result['accepted_b'], '.1f')}\t"
            f"{_fmt(result['btc'], '.3f')}\t"
            f"{_fmt(result['lowest_yield_pct'], '.3f')}\t{_fmt(result['avg_yield_pct'], '.3f')}\t"
            f"{_fmt(result['tail_bp'], '.2f')}\t{result['status']}\n"
        )
    return True


def print_result(result, url=None):
    """Print a single auction result."""
    print(f"\n  {result['date']}  —  {result['security']}  (Issue #{result['issue']})")
    print(f"  {'-'*60}")
    print(f"  Competitive bids:  ¥{result['comp_bids_b']:,.1f}B")
    print(f"  Accepted:          ¥{result['accepted_b']:,.1f}B")
    print(f"  BTC ratio:         {result['btc']:.3f}x")
    if result["lowest_yield_pct"] is not None:
        print(f"  Lowest accepted:   {result['lowest_yield_pct']:.3f}% yield")
    if result["avg_yield_pct"] is not None:
        print(f"  Weighted average:  {result['avg_yield_pct']:.3f}% yield")
    if result["tail_bp"] is not None:
        print(f"  Tail:              {result['tail_bp']:.1f} bp")
    print(f"  Status:            {result['status']}")
    if url:
        print(f"  Source:            {url}")


def load_catalyst_auction_dates():
    """Read CATALYSTS.tsv and return list of (date, event) tuples for JGB auctions."""
    if not CATALYSTS_TSV.exists():
        return []
    auctions = []
    with open(CATALYSTS_TSV) as f:
        header = f.readline().strip().split("\t")
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            d = dict(zip(header, parts + [""] * (len(header) - len(parts))))
            event = d.get("event", "").lower()
            if "jgb" in event and "auction" in event and "liquidity enhancement" not in event:
                try:
                    edate = datetime.strptime(d["date"], "%Y-%m-%d").date()
                    auctions.append((edate, d.get("event", "")))
                except ValueError:
                    continue
    return auctions


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*70}")
    print(f"  SAM JGB Auction Parser — {now}")
    print(f"{'='*70}")

    # Parse args
    target_dates = []

    if "--date" in sys.argv:
        idx = sys.argv.index("--date")
        if idx + 1 < len(sys.argv):
            try:
                d = datetime.strptime(sys.argv[idx + 1], "%Y-%m-%d").date()
                target_dates = [(d, "specified")]
            except ValueError:
                print(f"\n  ERROR: bad --date format. Use YYYY-MM-DD.")
                return 1
    elif "--catalog" in sys.argv:
        # Fetch all JGB auction dates from CATALYSTS.tsv that are in the past + today
        today = jst_today()
        target_dates = [
            (d, event) for d, event in load_catalyst_auction_dates()
            if d <= today
        ]
        if not target_dates:
            print(f"\n  No past auction dates in CATALYSTS.tsv.")
            return 0
    else:
        # Default: try today, then walk back up to 5 business days
        today = jst_today()
        probe = today
        found_any = False
        for _ in range(8):
            if probe.weekday() < 5:  # weekday
                html, url = fetch_auction_page(probe)
                if html:
                    result = parse_auction(html, probe)
                    if result:
                        print_result(result, url)
                        appended = append_tsv(result)
                        if appended:
                            print(f"\n  Appended to JGB_AUCTIONS.tsv")
                        else:
                            print(f"\n  TSV already has this auction")
                        found_any = True
                        break
            probe -= timedelta(days=1)
        if not found_any:
            print(f"\n  No auction results found in the last 8 days.")
        print()
        return 0

    # Fetch each target date
    for d, event in target_dates:
        print(f"\n  Checking: {d.strftime('%Y-%m-%d')} ({event})")
        html, url = fetch_auction_page(d)
        if not html:
            print(f"  ⚪ No page at {url}")
            continue
        result = parse_auction(html, d)
        if not result:
            print(f"  ⚠️  Page found but parse failed")
            continue
        print_result(result, url)
        if append_tsv(result):
            print(f"  ✅ Appended to JGB_AUCTIONS.tsv")
        else:
            print(f"  · Already in TSV")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
