#!/usr/bin/env python3
"""MARCO slaughter_pull — weekly federally-inspected slaughter (cattle/hogs/poultry).

Sources: AMS live SJ_LS712 (livestock) + NW_PY017 (poultry); esmis archive
pages 1-5 for ~52wk livestock history. Each livestock file yields 3 dated rows
(current week, prior week, same-week-year-ago). Writes TSV to baselines/.
"""
import re, sys, pathlib, datetime as dt
import requests, pandas as pd

LIVE_LIV = "https://www.ams.usda.gov/mnreports/sj_ls712.txt"
LIVE_POU = "https://www.ams.usda.gov/mnreports/nw_py017.txt"
ESMIS = "https://esmis.nal.usda.gov"
IDX = ESMIS + "/concern/publications/{pid}?page={p}"
OUT = pathlib.Path(__file__).resolve().parents[1] / "baselines" / "slaughter_weekly.tsv"
OUT.parent.mkdir(parents=True, exist_ok=True)
UA = {"User-Agent": "MARCO/1.0 (research)"}
DATE_RE = re.compile(r"^\s*(\d{1,2}-[A-Za-z]{3}-\d{2})\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s*$")

def fetch(url):
    r = requests.get(url, headers=UA, timeout=30); r.raise_for_status(); return r.text

def parse_liv(text, src):
    block = re.search(r"Livestock Slaughter \(head\).*?-{5,}", text, re.S)
    if not block: raise ValueError(f"no liv block {src}")
    rows = []
    for line in block.group(0).splitlines():
        m = DATE_RE.match(line)
        if not m: continue
        wk = dt.datetime.strptime(m.group(1), "%d-%b-%y").date()
        rows.append({"week_ending": wk,
                     "cattle_head": int(m.group(2).replace(",", "")),
                     "calves_head": int(m.group(3).replace(",", "")),
                     "hogs_head": int(m.group(4).replace(",", "")),
                     "sheep_head": int(m.group(5).replace(",", "")),
                     "liv_src": src})
    if not rows: raise ValueError(f"no date rows {src}")
    return rows

def parse_pou(text, src):
    m = re.search(r"Week ending\s+(\d+-[A-Za-z]+-\d+)", text)
    wk = dt.datetime.strptime(m.group(1), "%d-%b-%Y").date()
    ch = re.search(r"^Head\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)", text, re.M)
    tk = re.search(r"Live Turkeys.*?^Head\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)", text, re.S|re.M)
    if not (ch and tk): raise ValueError(f"poultry parse fail {src}")
    return {"week_ending": wk,
            "young_chickens_000": int(ch.group(1).replace(",", "")),
            "total_hens_000": int(ch.group(4).replace(",", "")),
            "ducks_000": int(ch.group(5).replace(",", "")),
            "total_turkeys_000": int(tk.group(5).replace(",", "")),
            "pou_src": src}

def archive_urls(pid, fname, pages=5):
    urls = []
    for p in range(1, pages+1):
        html = fetch(IDX.format(pid=pid, p=p))
        urls += [ESMIS+m.group(1) for m in re.finditer(
            rf'href="(/sites/default/release-files/{pid}/[^"]+/{fname})"', html)]
    return sorted(set(urls))

liv_rows = parse_liv(fetch(LIVE_LIV), "LIVE")
for u in archive_urls("2j62s4898", "SJ_LS712.TXT", pages=5):
    try: liv_rows += parse_liv(fetch(u), u.split("/")[-3])
    except Exception as e: print(f"skip {u}: {e}", file=sys.stderr)
liv = pd.DataFrame(liv_rows).drop_duplicates("week_ending").sort_values("week_ending")

pou = pd.DataFrame([parse_pou(fetch(LIVE_POU), "LIVE")])

merged = liv.merge(pou, on="week_ending", how="outer").sort_values("week_ending")
merged.to_csv(OUT, sep="\t", index=False)
print(f"wrote {len(merged)} weekly rows → {OUT}")
print(f"range: {merged.week_ending.min()} → {merged.week_ending.max()}")
print(f"livestock weeks: {liv.week_ending.nunique()}; poultry weeks: {len(pou)}")
