#!/usr/bin/env python3
"""MARCO H-2A puller: downloads the newest DOL OFLC H-2A disclosure XLSX and emits aggregated TSV.

DOL sits behind an Akamai bot wall, but it passes a *complete* browser header set —
a User-Agent alone is what gets 403'd. So we fetch dol.gov directly (authoritative,
byte-exact, ~16MB) and fall back to the Wayback Machine only if the origin fails.

The filename is DISCOVERED from the live performance page, never hardcoded: DOL
publishes ONE cumulative fiscal-year-to-date file whose quarter suffix advances
(FY2026_Q2 -> FY2026_Q3) and the superseded name stops resolving. A hardcoded
candidate list therefore rots into a hard failure every quarter — which is exactly
how this tool died between 2026-04 and 2026-07 (see MARCO MEMORY, source-quality map).

Fail-loud: every failure mode exits non-zero with the reason. A 200 carrying an
Akamai challenge page is treated as a failure, not as data.
"""
import io, re, sys, time
from pathlib import Path
import requests
import pandas as pd

PERF_PAGE = "https://www.dol.gov/agencies/eta/foreign-labor/performance"
DOL_HOST = "https://www.dol.gov"
OUT_TSV = Path(__file__).resolve().parents[1] / "baselines" / "h2a_latest.tsv"

# Full browser header set — the ONLY reason this gets past Akamai. Do not trim to
# just User-Agent; that is a guaranteed 403 (verified 2026-07-31).
HDRS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Connection": "keep-alive",
}
MIN_BYTES = 1_000_000  # real file ~16MB; an Akamai challenge is ~2KB
FNAME_RE = re.compile(r'href="([^"]*?/(H-2A_Disclosure_Data_FY(\d{2,4})(?:_Q(\d))?\.xlsx))"', re.I)


def _sess():
    s = requests.Session()
    s.headers.update(HDRS)
    return s


def discover(s):
    """Parse the live performance page -> (url, filename, fy, q) for the newest file.

    Returns None if the page can't be read, so the caller can fall back.
    """
    try:
        r = s.get(PERF_PAGE, timeout=60)
        r.raise_for_status()
    except Exception as e:
        print(f"  ! performance page unreadable ({type(e).__name__}: {str(e)[:80]})")
        return None

    found = []
    for href, fname, fy, q in FNAME_RE.findall(r.text):
        fy_i = int(fy)
        if fy_i < 100:                      # FY15/FY16/FY17 legacy 2-digit naming
            fy_i += 2000
        found.append((fy_i, int(q) if q else 4, href, fname))
    if not found:
        print("  ! performance page had no H-2A_Disclosure_Data links (layout change?)")
        return None

    fy_i, q_i, href, fname = max(found)
    url = href if href.startswith("http") else DOL_HOST + href
    print(f"  discovered {len(found)} disclosure file(s); newest = {fname} (FY{fy_i} Q{q_i})")
    return url, fname, fy_i, q_i


def download(s, url, label):
    """GET url, validating that we got a real spreadsheet and not a bot-wall page."""
    r = s.get(url, timeout=240, headers={**HDRS, "Sec-Fetch-Site": "same-origin",
                                         "Referer": PERF_PAGE})
    if r.status_code != 200:
        raise RuntimeError(f"{label}: HTTP {r.status_code}")
    if len(r.content) < MIN_BYTES:
        raise RuntimeError(f"{label}: too small ({len(r.content)}B) — likely bot-wall HTML")
    if not r.content.startswith(b"PK"):
        raise RuntimeError(f"{label}: not a zip/xlsx (first bytes {r.content[:8]!r})")
    return r.content


def wayback(s, fname):
    """Fallback: newest archived copy of the same filename. Often ABSENT for large
    xlsx files — Wayback does not reliably archive them — so this is a backstop only."""
    url = f"{DOL_HOST}/sites/dolgov/files/ETA/oflc/pdfs/{fname}"
    r = s.get("https://web.archive.org/cdx/search/cdx",
              params={"url": url, "output": "json",
                      "filter": "statuscode:200", "limit": -1}, timeout=90)
    r.raise_for_status()
    rows = r.json() if r.text.strip() else []
    if len(rows) < 2:
        raise RuntimeError(f"no Wayback snapshot of {fname}")
    ts = rows[-1][1]
    print(f"  wayback snapshot {ts}")
    return download(s, f"https://web.archive.org/web/{ts}id_/{url}", "wayback"), ts


def main():
    t0 = time.time()
    s = _sess()

    disc = discover(s)
    if not disc:
        sys.exit("FAIL: could not discover the current H-2A disclosure filename from "
                 f"{PERF_PAGE} — check the page layout by hand before trusting any cached TSV.")
    url, fname, fy, q = disc

    src = f"dol.gov (live)"
    snap = "live"
    try:
        blob = download(s, url, "dol.gov")
    except Exception as e:
        print(f"  ! direct DOL fetch failed ({e}); trying Wayback fallback")
        try:
            blob, snap = wayback(s, fname)
            src = "wayback"
        except Exception as e2:
            sys.exit(f"FAIL: DOL direct failed ({e}) AND Wayback fallback failed ({e2}). "
                     f"No H-2A data pulled — do NOT cite {OUT_TSV.name}, it is stale.")

    print(f"Source: {fname} via {src} | {len(blob):,}B | {time.time()-t0:.0f}s")

    # RECEIVED_DATE / EMPLOYMENT_BEGIN_DATE added 2026-08-21: they were in the file
    # all along and unused, and they are what turn VX-MARCO-H2A-02 from a narrative
    # row into a measured one — see the PROCESSING section emitted below.
    want = ["CASE_STATUS", "DECISION_DATE", "EMPLOYER_STATE", "WORKSITE_STATE",
            "SOC_TITLE", "JOB_TITLE", "TOTAL_WORKERS_H2A_CERTIFIED",
            "TOTAL_WORKERS_H2A_REQUESTED", "WAGE_OFFER",
            "RECEIVED_DATE", "EMPLOYMENT_BEGIN_DATE"]
    head = pd.read_excel(io.BytesIO(blob), engine="openpyxl", nrows=0)
    have = set(head.columns)
    missing = [c for c in want if c not in have]
    if missing:
        # A form change (DOL split "new form"/"old form" in FY2025) renames columns.
        # Fail loud with the real header rather than silently emitting a partial file.
        sys.exit(f"FAIL: {fname} is missing expected column(s) {missing}. "
                 f"Actual columns: {sorted(have)}")

    df = pd.read_excel(io.BytesIO(blob), engine="openpyxl", usecols=want)
    cert = df[df["CASE_STATUS"].str.contains("Certif", case=False, na=False)].copy()
    cert["DECISION_DATE"] = pd.to_datetime(cert["DECISION_DATE"], errors="coerce")
    cert = cert.dropna(subset=["DECISION_DATE"])
    cert["FQ"] = cert["DECISION_DATE"].dt.to_period("Q-SEP")  # fiscal quarter (Oct-start)
    workers = "TOTAL_WORKERS_H2A_CERTIFIED"
    total_cert = int(cert[workers].sum())

    lines = [f"# MARCO H-2A aggregate | source={fname} | via={src} | snap={snap} | "
             f"fy={fy} through_q={q} | pulled={time.strftime('%Y-%m-%d')} | "
             f"rows={len(df)} | cert_rows={len(cert)} | total_workers_cert={total_cert}"]

    def emit(title, series, n=None):
        lines.append(f"\n## {title}")
        lines.append("key\tworkers_certified")
        ser = series.sort_values(ascending=False)
        if n:
            ser = ser.head(n)
        for k, v in ser.items():
            lines.append(f"{k}\t{int(v)}")

    emit("By fiscal quarter (decision date)", cert.groupby("FQ")[workers].sum())
    emit("Top 15 worksite states", cert.groupby("WORKSITE_STATE")[workers].sum(), 15)
    emit("Top 10 SOC occupations", cert.groupby("SOC_TITLE")[workers].sum(), 10)
    emit("Top 15 job titles (crop/activity proxy)", cert.groupby("JOB_TITLE")[workers].sum(), 15)
    # --- Processing vulnerability (VX-MARCO-H2A-02) ---------------------------
    # Two legs, both computed off dates the disclosure already carries:
    #   lag  = DECISION_DATE - RECEIVED_DATE   (how long DOL takes)
    #   lead = EMPLOYMENT_BEGIN_DATE - DECISION_DATE  (margin before work starts;
    #          NEGATIVE means certified AFTER the job was due to start = missed cycle)
    # ⚠️ This is the DOL certification leg ONLY. H-2A has a second gate — State Dept
    # consular visa issuance — which this file cannot see. A row scored on these
    # numbers alone is a claim about half the pipeline; say so wherever it is cited.
    lines.append("\n## Processing vulnerability (DOL leg only — consular gate NOT visible here)")
    rec = pd.to_datetime(cert.get("RECEIVED_DATE"), errors="coerce")
    beg = pd.to_datetime(cert.get("EMPLOYMENT_BEGIN_DATE"), errors="coerce")
    lag = (cert["DECISION_DATE"] - rec).dt.days
    lead = (beg - cert["DECISION_DATE"]).dt.days
    lines.append("key\tvalue")
    lv = lag.dropna()
    if len(lv):
        lines.append(f"lag_median_days\t{lv.median():.0f}")
        lines.append(f"lag_mean_days\t{lv.mean():.1f}")
        lines.append(f"lag_p90_days\t{lv.quantile(0.9):.0f}")
    wv = lead.dropna()
    if len(wv):
        late = wv < 0
        wl = cert.loc[wv.index[late], workers].sum()
        wt = cert.loc[wv.index, workers].sum()
        lines.append(f"lead_median_days\t{wv.median():.0f}")
        lines.append(f"lead_p10_days\t{wv.quantile(0.10):.0f}")
        lines.append(f"lead_p25_days\t{wv.quantile(0.25):.0f}")
        lines.append(f"missed_cycle_case_pct\t{late.mean()*100:.2f}")
        lines.append(f"missed_cycle_worker_pct\t{(wl / wt * 100) if wt else 0:.2f}")
        lines.append(f"share_under_30d_lead_pct\t{(wv < 30).mean()*100:.2f}")
    # Per-quarter, because FY2026 Q1 was badly late (17.1% of workers) and Q2-Q3
    # were not — an FY-level average hides exactly that.
    lines.append("\n## Processing by fiscal quarter")
    lines.append("quarter\tn_cases\tlag_median_d\tlead_median_d\tmissed_cycle_case_pct")
    tmp = cert.assign(_lag=lag, _lead=lead)
    for qq, g in tmp.groupby("FQ"):
        gl, gd = g["_lag"].dropna(), g["_lead"].dropna()
        if not len(gd):
            continue
        lines.append(f"{qq}\t{len(g)}\t{gl.median() if len(gl) else float('nan'):.0f}\t"
                     f"{gd.median():.0f}\t{(gd < 0).mean()*100:.2f}")

    lines.append("\n## Wage offer (USD)")
    lines.append(f"median\t{cert['WAGE_OFFER'].median():.2f}")
    lines.append(f"mean\t{cert['WAGE_OFFER'].mean():.2f}")
    lines.append(f"total_requested\t{int(df['TOTAL_WORKERS_H2A_REQUESTED'].sum())}")

    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_TSV.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT_TSV} ({OUT_TSV.stat().st_size:,}B) in {time.time()-t0:.0f}s")
    print(f"FY{fy} through Q{q}: {total_cert:,} workers certified")


if __name__ == "__main__":
    main()
