"""CARL 2026-11-17: October advance retail (Census CB26-181) + October import/export prices (BLS via FRED mirror).
Pulls FRED levels (vintage = as published 2026-11-17), writes pulled.json + derived.json beside this file."""
import json, os, urllib.request, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "../../../.."))
key = [l.split("=",1)[1].strip().strip('"') for l in open(os.path.join(ROOT,"FORGE/tools/market-data/.env")) if l.startswith("FRED_API_KEY=")][0]
S = ["RSAFS","RSFSXMV","RSXFS","RSMVPD","RSGASS","RSBMGESD","RSFSDP","RSNSR","RSGMS","RSDBS","RSCCAS","RSFHFS","RSHPCS","RSMSR","RSEAS","RSSGHBMS",
     "IR","IREXFUELS","IREXFDFLS","IR10","IR0","IR1","IR2","IR3","IR4","IQ","IQ11","IQAG","IQEXAG",
     "CUSR0000SAF11","CUSR0000SEFV","CPIAPPSL","CUSR0000SACL1E"]
d = {}
for s in S:
    u = "https://api.stlouisfed.org/fred/series/observations?"+urllib.parse.urlencode(dict(series_id=s,api_key=key,file_type="json",observation_start="2025-08-01"))
    d[s] = {o["date"][:7]: (None if o["value"]=="." else float(o["value"])) for o in json.load(urllib.request.urlopen(u,timeout=30))["observations"]}
json.dump(d, open(os.path.join(HERE,"pulled.json"),"w"), indent=1)
v = lambda s,m: d[s][m]
pct = lambda a,b: round(100*(a/b-1),3)
O,S9,A8,J7 = "2026-10","2026-09","2026-08","2026-07"
Y,Y9 = "2025-10","2025-09"
def ctrl(m): return v("RSAFS",m)-v("RSMVPD",m)-v("RSGASS",m)-v("RSBMGESD",m)-v("RSFSDP",m)
def xag(m): return v("RSFSXMV",m)-v("RSGASS",m)
out = {"retail": {
 "headline_mom": {m: pct(v("RSAFS",m), v("RSAFS",p)) for m,p in [(O,S9),(S9,A8),(A8,J7)]},
 "headline_yoy_oct": pct(v("RSAFS",O), v("RSAFS",Y)),
 "ex_autos_mom_RSFSXMV": {m: pct(v("RSFSXMV",m), v("RSFSXMV",p)) for m,p in [(O,S9),(S9,A8)]},
 "retail_trade_ex_food_services_mom_RSXFS": pct(v("RSXFS",O), v("RSXFS",S9)),
 "ex_autos_gas_mom": {m: pct(xag(m), xag(p)) for m,p in [(O,S9),(S9,A8)]},
 "control_level": {m: ctrl(m) for m in [O,S9,A8,Y]},
 "control_mom": {m: pct(ctrl(m), ctrl(p)) for m,p in [(O,S9),(S9,A8)]},
 "control_yoy_oct": pct(ctrl(O), ctrl(Y)),
 "control_real_mom_core_goods_cpi": round(pct(ctrl(O),ctrl(S9)) - pct(v("CUSR0000SACL1E",O), v("CUSR0000SACL1E",S9)),3),
 "core_goods_cpi_mom": pct(v("CUSR0000SACL1E",O), v("CUSR0000SACL1E",S9)),
 "categories_mom": {s: pct(v(s,O), v(s,S9)) for s in ["RSMVPD","RSGASS","RSBMGESD","RSFSDP","RSNSR","RSGMS","RSDBS","RSCCAS","RSFHFS","RSHPCS","RSMSR","RSEAS","RSSGHBMS"]},
 "dollar_contrib_mom_musd": {s: v(s,O)-v(s,S9) for s in ["RSAFS","RSMVPD","RSGASS","RSNSR","RSMSR","RSHPCS","RSFSDP","RSBMGESD","RSDBS","RSFHFS","RSCCAS"]},
 "gas_share_of_total": {m: round(100*v("RSGASS",m)/v("RSAFS",m),3) for m in [O,S9,Y]},
 "T1b_gm_share": {m: round(100*v("RSGMS",m)/v("RSXFS",m),3) for m in [O,S9,Y]},
}}
# T1-a / T1-c need October-2025 CPI, which BLS did not publish (not collected). Substitute: geometric interpolation Sep-25..Nov-25 (LABELLED, not BLS).
def interp(s): return (v(s,"2025-09")*v(s,"2025-11"))**0.5
cpi = {k: pct(v(k,O), interp(k)) for k in ["CUSR0000SAF11","CUSR0000SEFV","CPIAPPSL"]}
r = out["retail"]
r["T1_SUBSTITUTE_interpolated_Oct25_CPI"] = {
 "grocery_real_yoy": pct(v("RSDBS",O)/v("RSDBS",Y), v("CUSR0000SAF11",O)/interp("CUSR0000SAF11")),
 "restaurant_real_yoy": pct(v("RSFSDP",O)/v("RSFSDP",Y), v("CUSR0000SEFV",O)/interp("CUSR0000SEFV")),
 "apparel_real_yoy": pct(v("RSCCAS",O)/v("RSCCAS",Y), v("CPIAPPSL",O)/interp("CPIAPPSL")),
 "cpi_yoy_interp": cpi, "method": "ratio: nominal growth / CPI growth (registered method), Oct-25 CPI = sqrt(Sep25*Nov25); not BLS"}
ip = {}
for s in ["IR","IREXFUELS","IREXFDFLS","IR10","IR0","IR1","IR2","IR3","IR4","IQ","IQ11","IQAG","IQEXAG"]:
    ip[s] = {"mom_oct": pct(v(s,O),v(s,S9)), "mom_sep": pct(v(s,S9),v(s,A8)),
             "yoy_sep": pct(v(s,S9),v(s,Y9)), "oct26_vs_sep25_13mo": pct(v(s,O),v(s,Y9)),
             "oct26_vs_nov25_11mo": pct(v(s,O),v(s,"2025-11")), "oct25_published": v(s,Y) is not None}
# implied fuel weight from rounded indexes, and fuel / ex-fuel contribution to the headline
h, xf, f = ip["IR"]["mom_oct"], ip["IREXFUELS"]["mom_oct"], ip["IR10"]["mom_oct"]
w = (h-xf)/(f-xf)
ip["_split"] = {"implied_fuel_weight": round(w,3), "fuel_contrib_pp": round(w*f,3), "exfuel_contrib_pp": round((1-w)*xf,3),
  "exfuel_mom_range_from_rounding": [pct(v("IREXFUELS",O)-0.05, v("IREXFUELS",S9)+0.05), pct(v("IREXFUELS",O)+0.05, v("IREXFUELS",S9)-0.05)],
  "headline_mom_range_from_rounding": [pct(v("IR",O)-0.05, v("IR",S9)+0.05), pct(v("IR",O)+0.05, v("IR",S9)-0.05)]}
out["import_export"] = ip
json.dump(out, open(os.path.join(HERE,"derived.json"),"w"), indent=1)
print(json.dumps(out, indent=1))
