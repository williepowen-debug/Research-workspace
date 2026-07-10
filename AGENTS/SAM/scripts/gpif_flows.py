#!/usr/bin/env python3
"""
SAM GPIF Portfolio / Flows Tracker

Tracks Japan's Government Pension Investment Fund (GPIF) — the world's
largest public pension fund (~¥293.6T AUM, FY2025) — via its published
English-language investment-results reports. GPIF is the primary named
Japanese super-long/duration demand-leg gap (CH-010 thread, SAM-32
post-mortem): no other SAM instrument tracks GPIF's own buy/sell stance.

CADENCE (own this honestly — GPIF is laggy by construction):
  - Quarterly "update report" PDFs: published ~5 weeks after quarter end
    (1Q Apr-Jun -> ~Aug 1; 2Q Jul-Sep -> ~early Nov; 3Q Oct-Dec -> ~early Feb)
  - Annual summary PDF + portfolio-holdings Excel: published ~Jul 1-3,
    for the fiscal year just ended (Apr Y -> Mar Y+1)
  - There is NO higher-frequency public GPIF disclosure. This script's job
    is to never miss a release when one lands, not to invent an interim
    read between releases. A run that finds "0 new reports" between
    known release windows is correct, not a failure.

SOURCE: https://www.gpif.go.jp/en/performance/latest-results.html
  (GPIF rotates report links into this page in place; URLs contain
  non-predictable per-upload folder IDs, so this script scrapes the
  live page rather than guessing a URL pattern.)

WHAT THIS PULLS (per report, best-effort, never fabricated):
  - Asset size (¥bn) as of period-end
  - Period rate of investment return (%)
  - Asset allocation by category: Domestic bonds / Foreign bonds /
    Domestic equities / Foreign equities (%, ¥bn)
  - Annual-report-only: net rebalancing flow by asset class (¥bn) —
    the closest GPIF gets to publishing a "flow" number; this is the
    field most relevant to the Japan-duration-extension question.

KNOWN GAP (documented, not silently dropped): the "Portfolio holdings by
asset category" Excel workbook (published alongside the annual summary)
contains security-level detail across 5 sheets (Domestic/Foreign Bonds,
Domestic/Foreign Equities, Alternatives). This script logs its URL for
discovery/never-miss-a-release purposes but does NOT parse it — the
sheet structure is security-level granular and a reliable stdlib-only
parse was out of scope for this build. A future targeted read could
open it by hand if a specific question needs security-level detail.

Appends to workbook/GPIF_FLOWS.tsv, idempotent by report URL.

Usage:
  .venv/bin/python3 AGENTS/SAM/scripts/gpif_flows.py
"""

import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

SAM_DIR = Path(__file__).resolve().parent.parent
WORKBOOK = SAM_DIR / "workbook"
FLOWS_TSV = WORKBOOK / "GPIF_FLOWS.tsv"

GPIF_RESULTS_URL = "https://www.gpif.go.jp/en/performance/latest-results.html"
HEADERS = {"User-Agent": "Mozilla/5.0 (SAM-Research)"}

TSV_HEADER = (
    "discovered_date\tperiod_label\treport_type\turl\t"
    "asset_size_jpy_bn\tperiod_return_pct\t"
    "domestic_bonds_pct\tdomestic_bonds_jpy_bn\t"
    "foreign_bonds_pct\tforeign_bonds_jpy_bn\t"
    "domestic_equities_pct\tdomestic_equities_jpy_bn\t"
    "foreign_equities_pct\tforeign_equities_jpy_bn\t"
    "domestic_bonds_flow_jpy_bn\tforeign_bonds_flow_jpy_bn\t"
    "domestic_equities_flow_jpy_bn\tforeign_equities_flow_jpy_bn\t"
    "parse_status\n"
)

# Policy asset mix (2026): 25% each, +-6% deviation limit on bonds/equities
# domestic/foreign split, +-9% on domestic-vs-foreign at the 50% level.
# A category approaching the 31%/19% band edge signals active tilt.
POLICY_TARGET_PCT = 25.0
POLICY_BAND_PCT = 6.0


def fetch_url(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}")
        return None


def fetch_report_links():
    """Scrape latest-results.html for (url, title, kind) tuples.

    kind is one of: quarterly_update, annual_summary, portfolio_holdings_xlsx
    """
    raw = fetch_url(GPIF_RESULTS_URL)
    if raw is None:
        return None
    html = raw.decode("utf-8", errors="replace")

    links = []
    for m in re.finditer(
        r'<a\s+[^>]*href="([^"]+\.(?:pdf|xlsx))"[^>]*>(.*?)</a>',
        html, re.S | re.I,
    ):
        url, inner = m.groups()
        title = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", inner)).strip()
        if url.lower().endswith(".xlsx"):
            kind = "portfolio_holdings_xlsx"
        elif re.search(r"\bfor\s+\d?Q\s+of\s+fiscal\s+\d{4}", title, re.I):
            kind = "quarterly_update"
        elif re.search(r"fiscal\s+\d{4}", title, re.I):
            kind = "annual_summary"
        else:
            continue  # unrecognized link on the page; skip rather than guess
        links.append((url, title, kind))
    return links


def period_label(title, kind):
    if kind == "quarterly_update":
        m = re.search(r"for\s+(\d)Q\s+of\s+fiscal\s+(\d{4})", title, re.I)
        if m:
            return f"FY{m.group(2)}_{m.group(1)}Q"
    m = re.search(r"fiscal\s+(\d{4})", title, re.I)
    if m:
        return f"FY{m.group(1)}_ANNUAL"
    if kind == "portfolio_holdings_xlsx":
        # Title reads "...as of Mar 31, YYYY" -> Japanese FY ends Mar 31,
        # so this is FY(YYYY-1) (e.g. "Mar 31, 2026" = FY2025 = Apr25-Mar26).
        m = re.search(r"as of \w+ \d+,\s*(\d{4})", title, re.I)
        if m:
            return f"FY{int(m.group(1)) - 1}_HOLDINGS"
    return "UNKNOWN"


def num(s):
    try:
        return float(s.replace(",", ""))
    except (ValueError, AttributeError):
        return None


def parse_annual_pdf(text):
    """Parse the annual summary PDF (clean label-adjacent-to-number layout)."""
    out = {}
    m = re.search(r"Asset size\s*¥\s*([\d,]+\.\d+)\s*billion", text)
    if m:
        out["asset_size"] = num(m.group(1))

    # PDF layout puts both sentences' numbers AFTER both sentences' text
    # ("...is\n\n...is\n\n16.47%.\n\n¥41,399.5 billion.") — capture jointly.
    m = re.search(
        r"The rate of investment return for FY\s*\d{4}\s+is\s*"
        r"The amount of investment returns for FY\s*\d{4}\s+is\s*"
        r"([\d.\-]+)%\.\s*¥\s*([\d,]+\.\d+)\s*billion", text,
    )
    if m:
        out["return_pct"] = num(m.group(1))
        out["return_amount_jpy_bn"] = num(m.group(2))

    # Composition block: "Domestic bonds\n26.91%\n¥80,679.1 billion" (order varies)
    labels = {"Domestic bonds": "domestic_bonds", "Foreign bonds": "foreign_bonds",
              "Domestic equities": "domestic_equities", "Foreign equities": "foreign_equities"}
    comp_found = 0
    for label, key in labels.items():
        m = re.search(
            re.escape(label) + r"\s*\n?\s*([\d.]+)%\s*\n?\s*¥\s*([\d,]+\.\d+)\s*billion",
            text,
        )
        if m:
            out[f"{key}_pct"] = num(m.group(1))
            out[f"{key}_jpy_bn"] = num(m.group(2))
            comp_found += 1

    # Rebalancing flows: "...Domestic bonds Foreign bonds Domestic equities
    # Foreign equities Allocated/withdrawn +14,753.2 +2,653.0 -10,693.2 -4,201.3"
    m = re.search(
        r"Allocated/withdrawn\s*([+\-−][\d,]+\.\d)\s*([+\-−][\d,]+\.\d)\s*"
        r"([+\-−][\d,]+\.\d)\s*([+\-−][\d,]+\.\d)",
        text,
    )
    if m:
        vals = [v.replace("−", "-") for v in m.groups()]
        out["domestic_bonds_flow"] = num(vals[0])
        out["foreign_bonds_flow"] = num(vals[1])
        out["domestic_equities_flow"] = num(vals[2])
        out["foreign_equities_flow"] = num(vals[3])

    status = "OK" if comp_found == 4 and "asset_size" in out and "return_pct" in out else "PARTIAL"
    return out, status


def parse_quarterly_pdf(text):
    """Parse a 1Q/2Q/3Q update PDF (interleaved numbers-before-labels layout)."""
    out = {}
    m = re.search(r"Total assets\(￥billion\)([\d,]+\.\d+)\(End of ([^)]+)\)", text)
    if not m:
        m = re.search(r"Total assets\(￥billion\)([\d,]+\.\d+)\(End of ([^)]+)\)", text)
    if m:
        out["asset_size"] = num(m.group(1))

    m = re.search(r"Rate of investment return.{0,40}?([+\-＋－]?[\d.]+)%\s*\(Not annualized\)", text, re.S)
    if m:
        raw = m.group(1).replace("＋", "+").replace("－", "-")
        out["return_pct"] = num(raw)

    # Composition: 4 (value, pct) pairs + a total pair, in fixed document
    # order [Domestic bonds, Domestic equities, Foreign equities, Foreign
    # bonds, Total] — verified against the doc's own domestic/foreign
    # sub-total checksum (see module docstring / build notes).
    pairs = re.findall(r"([\d,]+\.\d)(\d{1,3}\.\d{2})%", text)
    if len(pairs) >= 5:
        vals = [(num(v), num(p)) for v, p in pairs[:5]]
        cat_vals, total = vals[:4], vals[4]
        pct_sum = sum(p for _, p in cat_vals)
        val_sum = sum(v for v, _ in cat_vals)
        if abs(pct_sum - 100.0) < 0.5 and total[0] and abs(val_sum - total[0]) < max(1.0, total[0] * 0.01):
            order = ["domestic_bonds", "domestic_equities", "foreign_equities", "foreign_bonds"]
            for key, (v, p) in zip(order, cat_vals):
                out[f"{key}_jpy_bn"] = v
                out[f"{key}_pct"] = p
            comp_ok = True
        else:
            comp_ok = False
    else:
        comp_ok = False

    status = "OK" if comp_ok and "asset_size" in out and "return_pct" in out else "PARTIAL"
    return out, status


def parse_pdf_report(url, kind):
    raw = fetch_url(url, timeout=25)
    if raw is None:
        return {}, "FETCH_FAILED"
    tmp_path = WORKBOOK / f"_tmp_gpif_{Path(url).name}"
    try:
        tmp_path.write_bytes(raw)
        from pdfminer.high_level import extract_text
        text = extract_text(str(tmp_path))
    except Exception as e:
        print(f"  ERROR parsing PDF {url}: {e}")
        return {}, "PARSE_FAILED"
    finally:
        if tmp_path.exists():
            tmp_path.unlink()

    if kind == "annual_summary":
        return parse_annual_pdf(text)
    else:
        return parse_quarterly_pdf(text)


def load_existing_urls():
    existing = set()
    if FLOWS_TSV.exists():
        with open(FLOWS_TSV) as f:
            next(f, None)
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) >= 4:
                    existing.add(parts[3])  # url column
    else:
        WORKBOOK.mkdir(exist_ok=True)
        with open(FLOWS_TSV, "w") as f:
            f.write(TSV_HEADER)
    return existing


def append_row(row):
    with open(FLOWS_TSV, "a") as f:
        f.write("\t".join(str(row.get(c, "")) for c in TSV_HEADER.strip("\n").split("\t")) + "\n")


def band_flag(pct):
    if pct is None:
        return ""
    lo, hi = POLICY_TARGET_PCT - POLICY_BAND_PCT, POLICY_TARGET_PCT + POLICY_BAND_PCT
    dist_to_edge = min(pct - lo, hi - pct)
    if dist_to_edge < 0:
        return " \U0001F534 OUTSIDE BAND"
    elif dist_to_edge < 2.0:
        return " \U0001F7E0 near band edge"
    return ""


def main():
    now = datetime.now()
    today = now.strftime("%Y-%m-%d")
    print(f"\n{'='*70}")
    print(f"  SAM GPIF Portfolio / Flows Tracker — {now.strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*70}")
    print(f"  Cadence: quarterly update PDFs (~5wk lag) + annual summary/holdings (~Jul 1-3).")
    print(f"  Source:  {GPIF_RESULTS_URL}")

    links = fetch_report_links()
    if links is None:
        print("\n  ERROR: GPIF results page fetch failed. No data pulled — reporting failure, not substituting.")
        return 1
    if not links:
        print("\n  ERROR: GPIF results page fetched but no report links matched. Page structure may have changed.")
        return 1

    existing = load_existing_urls()
    new_links = [l for l in links if l[0] not in existing]

    print(f"\n  Found {len(links)} report link(s) on page; {len(new_links)} new since last run.")
    if not new_links:
        print("  Nothing new — correct behavior between GPIF release windows, not a stale pull.")

    appended = 0
    for url, title, kind in new_links:
        label = period_label(title, kind)
        print(f"\n  NEW: {label} [{kind}]")
        print(f"    {title}")
        print(f"    {url}")

        row = {
            "discovered_date": today,
            "period_label": label,
            "report_type": kind,
            "url": url,
        }

        if kind == "portfolio_holdings_xlsx":
            row["parse_status"] = "LINK_ONLY"
            print("    (Excel holdings workbook — link logged only, not parsed; see script docstring)")
        else:
            data, status = parse_pdf_report(url, kind)
            row["asset_size_jpy_bn"] = data.get("asset_size", "")
            row["period_return_pct"] = data.get("return_pct", "")
            for key in ("domestic_bonds", "foreign_bonds", "domestic_equities", "foreign_equities"):
                row[f"{key}_pct"] = data.get(f"{key}_pct", "")
                row[f"{key}_jpy_bn"] = data.get(f"{key}_jpy_bn", "")
            for key in ("domestic_bonds_flow", "foreign_bonds_flow",
                        "domestic_equities_flow", "foreign_equities_flow"):
                row[f"{key}_jpy_bn"] = data.get(key, "")
            row["parse_status"] = status

            print(f"    Parse status: {status}")
            if data.get("asset_size"):
                print(f"    Asset size:   ¥{data['asset_size']:,.1f}bn")
            if data.get("return_pct") is not None:
                print(f"    Period return: {data['return_pct']:+.2f}%")
            for key, name in (("domestic_bonds", "Domestic bonds"), ("foreign_bonds", "Foreign bonds"),
                               ("domestic_equities", "Domestic equities"), ("foreign_equities", "Foreign equities")):
                pct = data.get(f"{key}_pct")
                if pct is not None:
                    print(f"    {name:<18} {pct:>6.2f}%{band_flag(pct)}")
            flows = [data.get(k) for k in ("domestic_bonds_flow", "foreign_bonds_flow",
                                            "domestic_equities_flow", "foreign_equities_flow")]
            if any(f is not None for f in flows):
                print(f"    Rebalancing flow (¥bn): DomBonds {data.get('domestic_bonds_flow','?'):+.1f}  "
                      f"ForBonds {data.get('foreign_bonds_flow','?'):+.1f}  "
                      f"DomEq {data.get('domestic_equities_flow','?'):+.1f}  "
                      f"ForEq {data.get('foreign_equities_flow','?'):+.1f}")

        append_row(row)
        appended += 1

    print(f"\n  Appended {appended} row(s) to GPIF_FLOWS.tsv")

    # Next-expected-release hint (own the cadence honestly)
    month = now.month
    if 4 <= month <= 6:
        hint = "3Q update due ~early Feb (already past if late in window) — check page"
    elif month == 7:
        hint = "Annual summary/holdings typically land ~Jul 1-3; 1Q FY update due ~Aug 1"
    elif month in (8, 9):
        hint = "1Q update should be posted (~Aug 1); next is 2Q ~early Nov"
    elif month in (10, 11):
        hint = "2Q update due ~early Nov"
    else:
        hint = "3Q update due ~early Feb"
    print(f"  Next expected release: {hint}")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
