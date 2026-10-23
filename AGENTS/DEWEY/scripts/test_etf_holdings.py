"""Offline regressions for etf_holdings.py (no network).

Run: python3 AGENTS/DEWEY/scripts/test_etf_holdings.py
Synthetic fixtures in each fund's real layout: HYG CSV, HYG XML-spreadsheet XLS
(with the bare-entity case), JNK XLSX.
"""

import importlib.util
import io
import tempfile
import unittest
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("etf_holdings", HERE / "etf_holdings.py")
eh = importlib.util.module_from_spec(spec)
spec.loader.exec_module(eh)

HDR = ("Name,Sector,Asset Class,Market Value,Weight (%),Notional Value,Par Value,CUSIP,ISIN,SEDOL,Price,"
       "Location,Exchange,Currency,Duration,YTM (%),FX Rate,Maturity,Coupon (%),Mod. Duration,Yield to Call (%),"
       "Yield to Worst (%),Real Duration,Real YTM (%),Market Currency,Accrual Date,Effective Date")


def csv_file(date, rows):
    out = ["iShares iBoxx $ High Yield Corporate Bond ETF", f'Fund Holdings as of,"{date}"', "", HDR]
    for name, w, px, ytw, cpn in rows:
        out.append(f'"{name}","Other","Fixed Income","1","{w}","1","100","X","X","-","{px}","US","-","USD",'
                   f'"3","{ytw}","1","Oct 01, 2031","{cpn}","3","-","{ytw}","3","{ytw}","USD","-","-"')
    out.append('"BLK CSH FND","Cash and/or Derivatives","Money Market","1","0.9","1","1","X","X","-","1",'
               '"US","-","USD","0","4","1","-","4","0","-","4","0","4","USD","-","-"')
    return "\n".join(out).encode()


def xls_file(date, rows):
    cols = ["Name", "Sector", "Asset Class", "Market Value", "Weight (%)", "Par Value", "Price", "Maturity",
            "Coupon (%)", "Yield to Worst (%)"]
    def row(vals):
        return "<ss:Row>" + "".join(f'<ss:Cell><ss:Data ss:Type="String">{v}</ss:Data></ss:Cell>' for v in vals) + "</ss:Row>"
    body = [row(["Fund Holdings as of", date]), row(cols)]
    for name, w, px, ytw, cpn in rows:
        body.append(row([name, "Other", "Fixed Income", "1", w, "100", px, "Oct 01, 2031", cpn, ytw]))
    return ('<?xml version="1.0"?><ss:Workbook xmlns:ss="urn:schemas-microsoft-com:office:spreadsheet">'
            '<ss:Worksheet ss:Name="Holdings"><ss:Table>' + "".join(body) +
            "</ss:Table></ss:Worksheet></ss:Workbook>").encode()


def xlsx_file(date, rows):
    strings, sheet_rows = [], []
    def s(v):
        strings.append(v); return f'<c t="s"><v>{len(strings) - 1}</v></c>'
    def cell(col, v, r):
        if isinstance(v, str):
            return s(v).replace("<c ", f'<c r="{col}{r}" ')
        return f'<c r="{col}{r}"><v>{v}</v></c>'
    grid = [["Fund Name:", "JNK"], ["Ticker Symbol:", "JNK"], ["Holdings:", f"As of {date}"], [],
            ["Name", "Identifier", "SEDOL", "Weight", "Coupon", "Par Value", "Market Value", "Local Currency", "Maturity"]]
    grid += [[n, "US0", "-", w, c, par, mv, "USD", "10/01/2031"] for n, w, c, par, mv in rows]
    for i, g in enumerate(grid, 1):
        sheet_rows.append(f'<row r="{i}">' + "".join(cell("ABCDEFGHI"[j], v, i) for j, v in enumerate(g)) + "</row>")
    ns = 'xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"'
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("xl/worksheets/sheet1.xml", f"<worksheet {ns}><sheetData>{''.join(sheet_rows)}</sheetData></worksheet>")
        z.writestr("xl/sharedStrings.xml", f"<sst {ns}>" + "".join(f"<si><t>{t}</t></si>" for t in strings) + "</sst>")
    return buf.getvalue()


class T(unittest.TestCase):
    def test_csv_and_xls_match_across_coupon_formats(self):
        # XLS writes coupon "10", CSV "10.00"; " Prvt" vs " 144A". Both must match.
        base = xls_file("Oct 13, 2026", [("COREWEAVE INC 144A", "0.5", "90", "13", "10"),
                                         ("ACME CABLE Prvt", "0.5", "50", "30", "8"),
                                         ("UKG INC 144A", "0.2", "100", "8", "6")])
        end = csv_file("Oct 22, 2026", [("COREWEAVE INC 144A", "0.5", "81", "15", "10.00"),
                                        ("ACME CABLE 144A", "0.5", "40", "35", "8.00"),
                                        ("UKG INC 144A", "0.2", "99", "8.2", "6.00")])
        (a1, r1), (a2, r2) = eh.parse(base), eh.parse(end)
        self.assertEqual((a1, a2), ("2026-10-13", "2026-10-22"))
        self.assertEqual(len(r2), 3)  # cash line excluded
        buckets = [(b, __import__("re").compile(rx)) for b, rx in eh.BUCKETS]
        res = eh.compare(r1, r2, buckets, min_ytw=12)
        self.assertEqual(res["sleeve"], 2)          # UKG at 8% YTW is outside the sleeve
        self.assertEqual(res["skipped"], [])
        self.assertEqual(set(res["agg"]), {"ai_builder", "other"})
        self.assertAlmostEqual(res["agg"]["ai_builder"]["wdp"], 0.5 * -10.0)
        self.assertAlmostEqual(res["agg"]["other"]["wdp"], 0.5 * -20.0)

    def test_jnk_xlsx_drops_zero_par_and_derives_price(self):
        raw = xlsx_file("22-Oct-2026", [("A CORP SR 144A 10/31 9", 0.6, 9.0, 1000.0, 850.0),
                                        ("EXITED CORP 10/27 4", 0.0, 4.0, 0.0, 0.0)])
        asof, rows = eh.parse(raw)
        self.assertEqual(asof, "2026-10-22")
        self.assertEqual(len(rows), 1)
        self.assertAlmostEqual(rows[0]["price"], 85.0)
        self.assertEqual(rows[0]["maturity"], "Oct 01, 2031")

    def test_save_is_idempotent_and_refuses_html(self):
        with tempfile.TemporaryDirectory() as d:
            raw = csv_file("Oct 22, 2026", [("X 144A", "1", "90", "9", "5.00")])
            self.assertEqual(eh.save("HYG", raw, d)[3], "saved")
            self.assertEqual(eh.save("HYG", raw, d)[3], "already saved, identical")
            with self.assertRaises(ValueError):
                eh.save("HYG", b"<html>product page</html>", d)


if __name__ == "__main__":
    unittest.main()
