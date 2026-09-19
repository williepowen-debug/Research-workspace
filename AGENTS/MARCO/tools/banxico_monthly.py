#!/usr/bin/env python3
"""banxico_monthly.py — Banxico CE81: MONTHLY national remittances (value / count / average).

WHY THIS EXISTS
---------------
Built 2026-09-19 (session 27) after the boot sweep printed a green
"⏩ Banxico remittances — current (56d < 85d cadence), skip" while the July CE81
print had been owed since ~Sep 1.

The boot step named "Banxico remittances" was wired to `banxico_reverse.py`, which
fetches **idCuadro=CE100** — remittances by *Mexican state*, **quarterly**. The
SDL-01 count tell is written on **idCuadro=CE81** — the *national monthly* table.
Different table, different cadence. The check was green, correct about its own
referent, and silent about the thing that was actually owed
(`finding_instrument_reports_clean_against_the_wrong_reference`). An 85-day cadence
could not flag a monthly release even if it had been pointed at the right table.

WHAT CE81 CONTAINS (row indices are into the raw sheet, header row 9 = dates)
  row 12  ● Remesas Totales (Millones de dólares)            -> value_musd
  row 17  ● Número de Remesas Totales (Miles de operaciones) -> count_thousands   <- the SDL-01 tell
  row 22  ● Remesa Promedio Total (Dólares)                  -> avg_usd

⚠️ Rows are located by LABEL, not by position — Banxico has re-laid these sheets
before, and a positional read that silently returns the wrong row is exactly the
failure `tsvutil.col()` was written to prevent. Fails loud if a label moves.

⚠️ PUBLICATION LAG: month M lands ~first business day of M+2 (July -> ~Sep 1).
So a month counts as available 32 days after month end. August is NOT owed until
~Oct 1 — a carried "July AND August are both unpulled" was half wrong.

Output: baselines/banxico_monthly.tsv, carrying a PAT-044 two-clock header whose
"Last real data refresh" is the NEWEST DATA MONTH, not the pull date — mtime is
restamped by git sync and fails false-negative.

Constraints: stdlib + requests + pandas. One-shot. Fail loudly.
"""
import datetime
import pathlib
import sys

import pandas as pd
import requests

URL = ("https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do"
       "?accion=consultarCuadro&idCuadro=CE81&sector=1&locale=es"
       "&fechaInicio={fi}&fechaFin={ff}&formatoXLS.x=1")

OUT = pathlib.Path(__file__).resolve().parents[1] / "baselines" / "banxico_monthly.tsv"

MES = {"Ene": 1, "Feb": 2, "Mar": 3, "Abr": 4, "May": 5, "Jun": 6,
       "Jul": 7, "Ago": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dic": 12}

WANT = {
    "value_musd":       "Remesas Totales (Millones de d",
    "count_thousands":  "Número de Remesas Totales (Miles",
    "avg_usd":          "Remesa Promedio Total (Dólares)",
}


def fetch(start_year=2005):
    fi = int(datetime.datetime(start_year, 1, 1).timestamp() * 1000)
    ff = int(datetime.datetime.now().timestamp() * 1000)
    r = requests.get(URL.format(fi=fi, ff=ff), timeout=90,
                     headers={"User-Agent": "Mozilla/5.0 MARCO/banxico_monthly"})
    r.raise_for_status()
    if len(r.content) < 2000:
        raise RuntimeError(f"Banxico returned <2KB: {r.content[:300]!r}")
    tmp = OUT.parent / "_ce81_raw.xls"
    tmp.write_bytes(r.content)
    try:
        raw = pd.read_excel(tmp, header=None, sheet_name="Hoja1")
    finally:
        tmp.unlink(missing_ok=True)

    months = []
    for j in range(2, raw.shape[1]):
        tok = str(raw.iloc[9, j]).split()
        if len(tok) == 2 and tok[0] in MES:
            months.append((int(tok[1]), MES[tok[0]], j))
    if len(months) < 24:
        raise RuntimeError(f"CE81: parsed only {len(months)} month columns — layout changed")

    rowidx = {}
    for key, needle in WANT.items():
        hits = [i for i in range(raw.shape[0]) if needle in str(raw.iloc[i, 1])]
        if len(hits) != 1:
            raise RuntimeError(f"CE81: label {needle!r} matched {len(hits)} rows, expected 1 "
                               f"— sheet re-laid; fix the label, never fall back to a position")
        rowidx[key] = hits[0]

    out = []
    for y, m, j in months:
        rec = {"period": f"{y}-{m:02d}"}
        for key, i in rowidx.items():
            try:
                rec[key] = float(raw.iloc[i, j])
            except (TypeError, ValueError):
                rec[key] = None
        if rec["count_thousands"] is not None:
            out.append(rec)
    return out


def main():
    rows = fetch()
    newest = rows[-1]["period"]
    hdr = [
        "# MARCO Banxico CE81 — MONTHLY national remittances (value / count / average).",
        "# Source: banxico.org.mx consultarCuadro idCuadro=CE81 (primary XLS).",
        "# ⚠️ count_thousands = THOUSANDS of operations. This is the SDL-01 tell series.",
        "# ⚠️ NOT CE100 — that is the QUARTERLY by-Mexican-state table (tools/banxico_reverse.py).",
        f"# Last real data refresh: {newest}-01   <- NEWEST DATA MONTH, not the pull date (PAT-044).",
        f"# pulled={datetime.date.today()} months={len(rows)} newest={newest}",
        "period\tvalue_musd\tcount_thousands\tavg_usd",
    ]
    body = ["\t".join(
        (r["period"],
         "" if r["value_musd"] is None else f"{r['value_musd']:.6f}",
         f"{r['count_thousands']:.6f}",
         "" if r["avg_usd"] is None else f"{r['avg_usd']:.0f}"))
        for r in rows]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(hdr + body) + "\n")
    print(f"Wrote {OUT} ({OUT.stat().st_size:,}B) — {len(rows)} months, newest {newest}")


if __name__ == "__main__":
    main()
