#!/usr/bin/env python3
"""MARCO H-2A puller: downloads latest DOL OFLC H-2A disclosure XLSX and emits aggregated TSV.

DOL serves .xlsx behind an Akamai bot wall that blocks scripted clients, so we go
through the Wayback Machine's availability API + id_ raw download (byte-identical
to the origin). One-shot, fail-loud, no retries.
"""
import io, json, os, sys
from pathlib import Path
import requests
import pandas as pd

DOL_BASE = "https://www.dol.gov/sites/dolgov/files/ETA/oflc/pdfs"
CANDIDATES = [  # try newest first; stop on first Wayback hit
    "H-2A_Disclosure_Data_FY2026_Q1.xlsx",
    "H-2A_Disclosure_Data_FY2025_Q4.xlsx",
    "H-2A_Disclosure_Data_FY2025_Q3.xlsx",
]
OUT_TSV = Path(__file__).resolve().parents[1] / "baselines" / "h2a_latest.tsv"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def find_wayback(filename: str):
    """Use CDX API (more reliable than /wayback/available) to find newest 200 snapshot."""
    url = f"{DOL_BASE}/{filename}"
    r = requests.get("https://web.archive.org/cdx/search/cdx",
                     params={"url": url, "output": "json",
                             "filter": "statuscode:200", "limit": -1},
                     headers=UA, timeout=90)
    r.raise_for_status()
    rows = r.json()
    if len(rows) < 2:
        return None
    ts = rows[-1][1]  # newest timestamp
    return f"https://web.archive.org/web/{ts}id_/{url}", ts

def main():
    source_url = source_ts = source_file = None
    for fn in CANDIDATES:
        hit = find_wayback(fn)
        if hit:
            source_url, source_ts = hit
            source_file = fn
            break
    if not source_url:
        sys.exit(f"FAIL: no Wayback snapshot found for any of {CANDIDATES}. "
                 f"Check DOL performance page manually and update CANDIDATES.")
    print(f"Source: {source_file} (Wayback snap {source_ts})")
    print(f"URL:    {source_url}")
    r = requests.get(source_url, headers=UA, timeout=300)
    r.raise_for_status()
    if len(r.content) < 1_000_000:  # real file is 50-100MB; 1886B = Akamai challenge
        sys.exit(f"FAIL: {source_file} too small ({len(r.content)}B) — likely bot-wall HTML.")
    df = pd.read_excel(io.BytesIO(r.content), engine="openpyxl",
                       usecols=["CASE_STATUS","DECISION_DATE","EMPLOYER_STATE",
                                "WORKSITE_STATE","SOC_TITLE","JOB_TITLE",
                                "TOTAL_WORKERS_H2A_CERTIFIED","TOTAL_WORKERS_H2A_REQUESTED",
                                "WAGE_OFFER"])
    cert = df[df["CASE_STATUS"].str.contains("Certif", case=False, na=False)].copy()
    cert["DECISION_DATE"] = pd.to_datetime(cert["DECISION_DATE"])
    cert["FQ"] = cert["DECISION_DATE"].dt.to_period("Q-SEP")  # fiscal quarter (Oct-start)
    workers = "TOTAL_WORKERS_H2A_CERTIFIED"

    lines = [f"# MARCO H-2A aggregate | source={source_file} | snap={source_ts} | "
             f"rows={len(df)} | cert_rows={len(cert)} | total_workers_cert={int(cert[workers].sum())}"]
    def emit(title, series, n=None):
        lines.append(f"\n## {title}")
        lines.append("key\tworkers_certified")
        s = series.sort_values(ascending=False)
        if n: s = s.head(n)
        for k, v in s.items():
            lines.append(f"{k}\t{int(v)}")

    emit("By fiscal quarter (decision date)",
         cert.groupby("FQ")[workers].sum())
    emit("Top 15 worksite states",
         cert.groupby("WORKSITE_STATE")[workers].sum(), 15)
    emit("Top 10 SOC occupations",
         cert.groupby("SOC_TITLE")[workers].sum(), 10)
    emit("Top 15 job titles (crop/activity proxy)",
         cert.groupby("JOB_TITLE")[workers].sum(), 15)
    med_wage = cert["WAGE_OFFER"].median()
    lines.append(f"\n## Wage offer (USD)")
    lines.append(f"median\t{med_wage:.2f}")
    lines.append(f"mean\t{cert['WAGE_OFFER'].mean():.2f}")
    lines.append(f"total_requested\t{int(df['TOTAL_WORKERS_H2A_REQUESTED'].sum())}")

    OUT_TSV.parent.mkdir(parents=True, exist_ok=True)
    OUT_TSV.write_text("\n".join(lines) + "\n")
    print(f"Wrote {OUT_TSV} ({OUT_TSV.stat().st_size:,}B)")
    print(f"Total workers certified: {int(cert[workers].sum()):,}")

if __name__ == "__main__":
    main()
