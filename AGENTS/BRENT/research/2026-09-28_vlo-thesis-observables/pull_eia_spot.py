import sys, json, urllib.request, pandas as pd
sys.path.insert(0, "."); import fetch
k=fetch.EIA_API_KEY
def q(route,s,freq,start):
    out=[];off=0
    while True:
        u=f"https://api.eia.gov/v2/{route}/data/?api_key={k}&frequency={freq}&data[0]=value&facets[series][]={s}&start={start}&sort[0][column]=period&sort[0][direction]=asc&offset={off}&length=5000"
        d=json.load(urllib.request.urlopen(u,timeout=60))["response"]["data"]; out+=d
        if len(d)<5000: break
        off+=5000
    return pd.Series({r["period"]:float(r["value"]) for r in d if r["value"] is not None} if False else {r["period"]:float(r["value"]) for r in out if r["value"] is not None},name=s)
S={"NYH_ULSD":"EER_EPD2DXL0_PF4_Y35NY_DPG","USGC_ULSD":"EER_EPD2DXL0_PF4_RGC_DPG","NYH_GAS":"EER_EPMRU_PF4_Y35NY_DPG","USGC_GAS":"EER_EPMRU_PF4_RGC_DPG","BRENT":"RBRTE","WTI":"RWTC"}
df=pd.concat([q("petroleum/pri/spt",v,"daily","2021-06-01").rename(n) for n,v in S.items()],axis=1)
df.index=pd.to_datetime(df.index); df=df.sort_index()
df.to_csv("/tmp/claude-1000/-home-willi-Research-workspace-AGENTS-BRENT/8559dc24-ba02-4177-b750-2b918883ff37/scratchpad/spot.csv")
print(df.tail(3)); print(df.count())
c=q("petroleum/sum/sndw","W_EPC0_SAX_YCUOK_MBBL","weekly","2026-07-01"); print("Cushing",c.tail(6).to_dict())
