"""Offline checks of only the inspected stats() function extracted from the PDF.
Not the original resolver; no downloads, operational resolution or hash attestation.
"""
from pathlib import Path
import json, textwrap
import numpy as np
import pandas as pd
p = Path(__file__).resolve().parent
text = (p / "combined_pdf_text.txt").read_text()
a = text.index("        def stats(")
z = text.index("        def main():", a)
code = textwrap.dedent(text[a:z])
ns = dict(np=np, pd=pd,
          TH=dict(corr=.863, vol=.20, beta=.80, brate_lo=-.03, brate_hi=.03),
          NEAR=dict(corr=.005, vol=.002, beta=.02, brate=.005))
exec(compile(code, "PDF-extracted stats function", "exec"), ns)
rng = np.random.default_rng(14)
dates = pd.bdate_range("2026-01-05", periods=64)
px = pd.DataFrame(100*np.cumprod(1+rng.normal(0,.01,(64,4)),axis=0),index=dates,columns=["KRE","KBWB","SPY","IWM"])
y = pd.Series(4+rng.normal(0,.02,64).cumsum(),index=dates)
short = ns["stats"](px, y, dates[1:63], dates[0])
bad = px.copy()
bad.loc[dates[10],"KRE"] = np.nan
bad.loc[dates[20],"KRE"] = np.nan
bad.loc[dates[30],"KBWB"] = np.nan
bad.loc[dates[40],"KBWB"] = np.nan
missing = ns["stats"](bad,y,dates[1:],dates[0])
result = {"method":"Synthetic data; PDF-extracted stats only, not original resolver replication", "short_window":{"n_returns_used":short["n_returns_used"],"status":short["status"]},"four_distinct_missing_sessions":{"n_returns_used":missing["n_returns_used"],"status":missing["status"],"missing":missing["missing"]}}
assert result["short_window"] == {"n_returns_used":62,"status":"RESOLVED"}
assert missing["n_returns_used"] == 59 and missing["status"] == "RESOLVED"
(p / "resolver_inspection_checks.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
