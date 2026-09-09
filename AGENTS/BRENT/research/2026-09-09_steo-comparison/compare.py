"""Offline same-series vintage comparison; no grades or thresholds are changed.

Run with repository .venv Python. Flow quarters are simple monthly means,
matching the saved BRENT ladder, not EIA's day-weighted quarterly columns.
Stock quarters are quarter-end. Positive world stock change means DRAW.
"""
import calendar
import hashlib
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parent / "2026-09-09_squeeze-review"
SELECTION = {
    "3atab": ["papr_world", "patc_world", "t3_stchange_world", "pasc_oecd_t3"],
    "3ctab": ["papr_opecplus"],
    "3dtab": ["cops_opec", "cops_opec_r05"],
    "2tab": ["BREPUUS", "WTIPUUS", "DSWHUUS_$"],
    "4atab": ["DFPSPUS"],
}
STOCKS = {"pasc_oecd_t3", "DFPSPUS"}
MONTHS = [f"{y}-{m:02d}" for y in (2026, 2027) for m in range(1, 13)]

def extract(path):
    result = {}
    for sheet, keys in SELECTION.items():
        frame = pd.read_excel(path, sheet_name=sheet, header=None).fillna("")
        years = frame.iloc[2].replace("", pd.NA).ffill()
        for key in keys:
            rows = frame[frame.iloc[:, 0] == key]
            assert len(rows) >= 1, (sheet, key)
            # Table 3a repeats the world total under two production groupings.
            # Permit identical repeated rows, but never conflicting definitions.
            assert len(rows.drop_duplicates()) == 1, (sheet, key, "conflicting duplicate rows")
            row = rows.iloc[0]
            monthly = {}
            for col in range(2, frame.shape[1]):
                month = str(frame.iloc[3, col]).strip()
                if years.iloc[col] not in [2026, 2027] or month not in (
                        "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()):
                    continue
                m = pd.to_datetime(month, format="%b").month
                date = f"{int(years.iloc[col])}-{m:02d}"
                assert date not in monthly, (key, date)
                monthly[date] = float(row.iloc[col])
            assert sorted(monthly) == MONTHS, (key, sorted(monthly))
            quarterly = {}
            day_weighted = {}
            for year in [2026, 2027]:
                for quarter in range(1, 5):
                    values = [monthly[f"{year}-{m:02d}"] for m in range(quarter*3-2, quarter*3+1)]
                    quarterly[f"{year}Q{quarter}"] = values[-1] if key in STOCKS else sum(values)/3
                    days = [calendar.monthrange(year, m)[1] for m in range(quarter*3-2, quarter*3+1)]
                    day_weighted[f"{year}Q{quarter}"] = (values[-1] if key in STOCKS else
                        sum(value*day for value, day in zip(values, days))/sum(days))
            units = ("million barrels" if key in STOCKS else
                     "dollars/barrel" if key in {"BREPUUS", "WTIPUUS"} else
                     "dollars/gallon" if key == "DSWHUUS_$" else "million barrels/day")
            result[key] = dict(sheet=sheet, label=str(row.iloc[1]), units=units,
                quarterly_method="quarter-end" if key in STOCKS else "simple monthly mean",
                monthly=monthly, quarterly=quarterly, quarterly_day_weighted=day_weighted)
    for month in MONTHS:
        assert abs(result["patc_world"]["monthly"][month] - result["papr_world"]["monthly"][month]
                   - result["t3_stchange_world"]["monthly"][month]) < 1e-6
    return result

def main():
    manifest = json.loads((ROOT / "source-manifest.json").read_text())
    assert hashlib.sha256((OLD/"aug26_base.xlsx").read_bytes()).hexdigest() == manifest["august_baseline"]["sha256"]
    for source in manifest["sources"]:
        assert hashlib.sha256((ROOT/source["file"]).read_bytes()).hexdigest() == source["sha256"]
    august, september = extract(OLD/"aug26_base.xlsx"), extract(ROOT/"sep26_base.xlsx")
    # Independent published PDF Table 3a cross-check, at the table's precision.
    for q, printed in {"2026Q3": 2.96, "2026Q4": 1.71, "2027Q1": -3.01, "2027Q2": -5.05}.items():
        assert round(september["t3_stchange_world"]["quarterly_day_weighted"][q], 2) == printed
    for q, printed in {"2026Q3": 2651, "2026Q4": 2568, "2027Q1": 2634, "2027Q2": 2774}.items():
        assert round(september["pasc_oecd_t3"]["quarterly"][q]) == printed
    for old in json.loads((OLD/"august-steo-baseline.json").read_text())["series"]:
        for frequency in ["monthly", "quarterly"]:
            for date, value in old[frequency].items():
                assert abs(value-august[old["series_id"]][frequency][date]) < 1e-9
    revisions = {}
    for key in august:
        assert august[key]["label"] == september[key]["label"]
        revisions[key] = {frequency: {date: september[key][frequency][date]-value
                         for date, value in august[key][frequency].items()}
                         for frequency in ["monthly", "quarterly"]}
    for frequency in ["monthly", "quarterly"]:
        for date, draw in revisions["t3_stchange_world"][frequency].items():
            assert abs(draw-(revisions["patc_world"][frequency][date]-revisions["papr_world"][frequency][date])) < 1e-6
    bridges = {name: {key: vintage[key]["quarterly"]["2026Q4"]-vintage[key]["quarterly"]["2026Q3"]
                     for key in ["papr_world", "patc_world", "t3_stchange_world", "papr_opecplus"]}
               for name, vintage in [("august", august), ("september", september)]}
    # HTTP 200 is not sufficient proof of a successful EIA page capture.
    source_checks = {s["file"]: ("ERROR_PAGE_NOT_EVIDENCE" if b"Unexpected Error" in
        (ROOT/s["file"]).read_bytes() else "captured; see report for content verification")
        for s in manifest["sources"]}
    output = dict(august=august, september=september, september_minus_august=revisions,
                  q3_to_q4=bridges, source_content_checks=source_checks,
                  validation="PASS: source hashes, 24-month coverage, consistent repeated IDs/unique dates, identical labels, saved August baseline reproduction, both-vintage balances, revision decomposition and independent PDF draw/stock cross-check")
    (ROOT/"comparison.json").write_text(json.dumps(output, indent=2)+"\n")
    print(output["validation"])
    for key in august:
        print(key, "; ".join(f"{q}: {august[key]['quarterly'][q]:.4f} -> {september[key]['quarterly'][q]:.4f} ({revisions[key]['quarterly'][q]:+.4f})"
              for q in ["2026Q3", "2026Q4", "2027Q1", "2027Q2"]))
    print("Q3->Q4", json.dumps(bridges))
    for key in ["cops_opec", "cops_opec_r05", "DFPSPUS", "t3_stchange_world"]:
        print(key, json.dumps(september[key]["monthly"]))
    print("CONTENT CHECKS", source_checks)

if __name__ == "__main__":
    main()
