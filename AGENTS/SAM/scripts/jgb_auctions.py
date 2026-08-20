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
    """Fetch MOF auction result HTML for a given date.

    Returns (html_or_None, url, status) where status is one of:
      "ok"            — page fetched
      "absent"        — MOF returned 404: there is genuinely no auction that day
      "error:<what>"  — we could NOT reach MOF / it failed: says NOTHING about auctions

    ⚠️ WHY THE THIRD VALUE EXISTS (fixed 2026-08-17, DAEDALUS sweep
    `AGENTS/DAEDALUS/sweeps/SILENT_FALLBACK_GREEN_SWEEP_2026-08-17.md`; verified at
    source before applying). This function used to return a bare `(None, url)` for
    EVERY failure — a dead `if e.code == 404: return None, url` / `return None, url`
    pair plus a catch-all `except Exception: return None, url`. So a timeout, a DNS
    failure, a 403 and a 500 were all byte-identical to "no auction was held," and
    the caller printed the reassuring "No auction results found in the last 8 days."
    with rc=0.

    That is not generic hygiene here. **An unreachable MOF renders as an ABSENCE of
    auction demand — and absence is exactly what SAM's own Pillar-2 read treats as
    thesis-CONFIRMING** ("soft/absent 20Y + steepening curve = the demand-vacuum
    firing"). A network failure could therefore masquerade as the most
    thesis-favourable outcome available, on a promoted adjudicator. Never collapse
    "the source said no" into "we could not ask."

    Sibling of the fallback class in [[finding_fail_loud_on_incomplete_data]] — but
    the INVERTED form: cpi_japan.py served STALE DATA as fresh; this served ABSENCE
    as evidence. Both render as "a quiet week."
    """
    ymd = date_obj.strftime("%Y%m%d")
    url = MOF_URL_TEMPLATE.format(ymd=ymd)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8", errors="replace"), url, "ok"
    except urllib.error.HTTPError as e:
        if e.code == 404:
            # The ONLY failure that legitimately means "no auction that day".
            return None, url, "absent"
        return None, url, f"error:HTTP {e.code}"
    except urllib.error.URLError as e:
        return None, url, f"error:unreachable ({e.reason})"
    except Exception as e:
        return None, url, f"error:{type(e).__name__}"


def strip_tags(html_fragment):
    """Remove HTML tags and collapse whitespace."""
    text = re.sub(r"<[^>]+>", " ", html_fragment)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _date_matches(raw, date_obj):
    """True if `raw` (a MOF auction-date cell) denotes date_obj.

    MOF writes M/D/YYYY (e.g. "8/20/2026"); tolerate zero-padding and separator
    drift rather than failing closed on cosmetics. An UNRECOGNISED format returns
    False — the guard's whole point is that we must not stamp a row we cannot
    positively identify, and "I could not read the date" is not "the date matched."
    """
    if not raw:
        return False
    m = re.search(r"(\d{1,2})\s*[/\-.]\s*(\d{1,2})\s*[/\-.]\s*(\d{4})", raw)
    if m:
        mo, dy, yr = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return (yr, mo, dy) == (date_obj.year, date_obj.month, date_obj.day)
    # Also accept ISO / compact forms in case MOF re-lays-out the table.
    m = re.search(r"(\d{4})\s*[/\-.]?\s*(\d{2})\s*[/\-.]?\s*(\d{2})", raw)
    if m:
        yr, mo, dy = int(m.group(1)), int(m.group(2)), int(m.group(3))
        return (yr, mo, dy) == (date_obj.year, date_obj.month, date_obj.day)
    return False


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

    # 🔴 DATE-IDENTITY GUARD (added 2026-08-17, DAEDALUS sweep ACTION 2; verified
    # at source before applying). The `if not data_row` fallback above selects
    # "any <tr> containing a <td> starting with 'Year'" — it does NOT check whose
    # auction that row belongs to. So if MOF serves a page that is not the probed
    # date's result (an index, a redirect, a re-layout), the fallback happily
    # parses SOME auction's row and everything downstream stamps it with
    # `date_obj` — printing `✅ Orderly` and appending a WRONG-DATED row to
    # JGB_AUCTIONS.tsv, which is the ledger the Pillar-2 read is graded from.
    # A wrong row is strictly worse than no row: it is indistinguishable from a
    # real one after the fact. Require the parsed row to name its own date and to
    # agree with what we asked for.
    row_date_raw = cells[2].strip() if len(cells) > 2 else ""
    if not _date_matches(row_date_raw, date_obj):
        print(f"  ⚠️  UNPARSEABLE — page at {date_obj.isoformat()} returned a row "
              f"whose own auction date is {row_date_raw!r}, not {date_obj.isoformat()}.")
        print(f"     Refusing to stamp it. This is NOT an auction result; do not grade off it.")
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
        probed = 0
        fetch_errors = []       # dates we could NOT ask about — never "no auction"
        for _ in range(8):
            if probe.weekday() < 5:  # weekday
                probed += 1
                html, url, status = fetch_auction_page(probe)
                if status.startswith("error:"):
                    fetch_errors.append((probe, status[6:]))
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
                        # ⛔ DO NOT `break` HERE. This loop previously stopped at the
                        # FIRST auction found, so a boot captured AT MOST ONE auction per
                        # run — and Japan routinely runs 2+ auctions inside this 8-day
                        # probe window (August 2026 had seven). Measured cost: the 7/7 30Y
                        # and 7/14 20Y were both absent from the ledger while being cited
                        # in THESIS/STATUS/CALENDAR and in a BOND packet, and the 7/14 row
                        # was the COMPARISON BASE for the 8/20 CH-016 grade. The 8/18 5Y
                        # went missing the same way one week later.
                        # ⚠️ The fingerprint that proves it, preserved because it is how
                        # the defect was caught: JGB_AUCTIONS.tsv had 2026-08-20 sitting
                        # ABOVE 2026-08-18 — the boot wrote 8/20 and stopped; 8/18 only
                        # arrived later by a hand `--date` backfill.
                        # Found by KURA Run-12 (2026-08-20) from the ledger's ROW ORDER,
                        # not from reading this code. Class:
                        # [[finding_record_of_an_action_is_not_the_action]] — a boot that
                        # reports "ran cleanly, no alerts" is reporting on ONE probe.
            probe -= timedelta(days=1)
        if not found_any:
            # ⚠️ A clean "no auction" is only sayable if EVERY probe actually
            # reached MOF. If any probe errored, the correct statement is that we
            # do not know — see fetch_auction_page's docstring for why an
            # unreachable MOF reading as "no demand" is thesis-dangerous here.
            if fetch_errors:
                print(f"\n  🔴 COULD NOT REACH MOF on {len(fetch_errors)}/{probed} "
                      f"probed weekday(s) — THIS IS NOT 'no auction'.")
                for d, why in fetch_errors[:8]:
                    print(f"       {d.isoformat()}  {why}")
                print("     ⚠️  Absence of a result here is UNKNOWN, not evidence of "
                      "weak demand. Re-run or pull the MOF page by hand before grading.")
                print()
                return 1
            print(f"\n  No auction results found in the last 8 days "
                  f"(all {probed} weekday probe(s) reached MOF and returned 404).")
        elif fetch_errors:
            # Found one, but earlier/other probes failed — say so; a later date
            # could have had a result we never saw.
            print(f"\n  ⚠️  {len(fetch_errors)} probe(s) could not reach MOF "
                  f"({', '.join(d.isoformat() for d, _ in fetch_errors[:4])}) — "
                  f"result above is real, but coverage is INCOMPLETE.")
        print()
        return 0

    # Fetch each target date
    had_fetch_error = False
    for d, event in target_dates:
        print(f"\n  Checking: {d.strftime('%Y-%m-%d')} ({event})")
        html, url, status = fetch_auction_page(d)
        if status.startswith("error:"):
            # NOT "no page" — we never got an answer. Distinct line, distinct rc.
            print(f"  🔴 COULD NOT REACH MOF ({status[6:]}) — {url}")
            print(f"     ⚠️  This is UNKNOWN, not 'no auction'. Do not grade off it.")
            had_fetch_error = True
            continue
        if not html:
            print(f"  ⚪ MOF returned 404 — no auction published at {url}")
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

    if had_fetch_error:
        print("\n  🔴 One or more target dates could not be reached at MOF — "
              "coverage INCOMPLETE. Absence above is UNKNOWN, not 'no auction'.")
        print()
        return 1
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
