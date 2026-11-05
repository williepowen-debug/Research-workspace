import urllib.request,urllib.parse,xml.etree.ElementTree as ET,concurrent.futures,email.utils,datetime as dt,json,re,glob
Q={
'funding':'(repo OR "funding stress" OR "margin call" OR "forced selling" OR liquidation OR deleveraging) markets',
'banks':'(regional bank OR "bank stock" OR FDIC OR "bank failure" OR "enforcement action" OR "consent order")',
'privcredit':'("private credit" OR BDC OR "redemption" OR "non-traded" OR "direct lending" OR gating)',
'bankrupt':'("Chapter 11" OR bankruptcy OR "going concern" OR default OR "missed payment" OR "forbearance") company',
'cre':'("commercial real estate" OR CMBS OR "office loan" OR foreclosure OR "special servicing")',
'housing':'(mortgage rates OR "home sales" OR homebuilder OR "Fannie Mae" OR "Freddie Mac" OR foreclosure housing)',
'ai':'(AI capex OR "data center" OR Nvidia OR neocloud OR hyperscaler OR semiconductor) financing OR delay OR cut',
'chips':'(chip stocks OR Samsung OR "SK Hynix" OR TSMC OR AMD OR Micron OR Broadcom) selloff OR earnings',
'vol':'(VIX OR "volatility" OR "circuit breaker" OR "hedge funds" OR "CTA" OR "leveraged ETF") stocks selloff',
'macro':'(Fed OR Powell OR Warsh OR "rate hike" OR payrolls OR inflation) today',
'treasury':'(Treasury auction OR "bond market" OR "Treasury yields" OR "basis trade" OR "swap spreads")',
'oil':'(oil prices OR Brent OR OPEC OR refinery OR "crude" OR LNG) today',
'iran':'(Iran OR Hormuz OR Tehran OR IRGC OR Araghchi)',
'russia':'(Ukraine OR Russia OR Kremlin OR Putin OR refinery strike)',
'china':'(China OR yuan OR PBoC OR "export controls" OR rare earths OR Taiwan)',
'japan':'(BOJ OR yen OR JGB OR "carry trade" OR Ueda OR "Japan intervention")',
'europe':'(ECB OR gilt OR "Bank of England" OR OAT OR Bund OR "French budget" OR TTF)',
'em':'(Brazil OR Mexico OR Argentina OR Turkey OR "emerging markets" OR Paraguay) bonds OR currency OR default',
'consumer':'(consumer OR "credit card" OR "auto loans" OR subprime OR layoffs OR "student loans")',
'labor':'(layoffs OR "job cuts" OR WARN OR hiring freeze OR unemployment)',
'cyber':'(cyberattack OR ransomware OR "data breach" OR "zero-day" OR outage) bank OR payment OR cloud',
'insurance':'(insurer OR reinsurance OR Athene OR "life insurance" OR "Florida insurance")',
'florida':'(Florida condo OR "Florida insurance" OR "Citizens Property" OR "Florida bank" OR Miami real estate)',
'climate':'(hurricane OR drought OR "polar vortex" OR "Rhine" OR "Colorado River" OR wildfire)',
'power':'(ERCOT OR PJM OR "grid emergency" OR "power prices" OR "capacity auction" OR utility rate)',
'metals':'(gold OR silver OR copper OR LME OR platinum) price today',
'crypto':'(bitcoin OR stablecoin OR Tether OR crypto exchange hack OR liquidation)',
'ag':'(fertilizer OR urea OR potash OR wheat OR "food prices")',
'freight':'(freight OR rail OR trucking OR tanker rates OR "Cass" OR shipping)',
'autos':'(Carvana OR "auto lender" OR "used car" OR "First Brands" OR Tricolor OR "Car-Mart")',
'cruise':'(Carnival OR "Royal Caribbean" OR "Norwegian Cruise")',
'muni':'(municipal bonds OR "state budget" OR "muni" OR "city budget" OR "public pension")',
}
def get(k):
    u='https://news.google.com/rss/search?'+urllib.parse.urlencode({'q':Q[k]+' when:1d','hl':'en-US','gl':'US','ceid':'US:en'})
    try:
        x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read()
        out=[]
        for it in ET.fromstring(x).iter('item'):
            d=email.utils.parsedate_to_datetime(it.findtext('pubDate')); out.append((d,it.findtext('title'),it.findtext('link')))
        return k,out
    except Exception as e: return k,repr(e)
with concurrent.futures.ThreadPoolExecutor(8) as ex: res=dict(ex.map(get,Q))
board=' '.join(open(f,encoding='utf-8').read().lower() for f in glob.glob('/home/willi/Research-workspace/BOARD/SIG-W-20261105-*.md')+glob.glob('/home/willi/Research-workspace/BOARD/SIG-W-20261104-*.md'))
now=dt.datetime.now(dt.timezone.utc)
seen=set();rows=[]
for k,v in res.items():
    if isinstance(v,str): print('ERR',k,v);continue
    for d,t,l in v:
        key=re.sub(r'\W+',' ',t.split(' - ')[0].lower()).strip()[:60]
        if key in seen: continue
        seen.add(key)
        rows.append(dict(k=k,d=d.strftime('%m-%d %H:%MZ'),age=round((now-d).total_seconds()/3600,1),t=t,l=l))
json.dump(rows,open('/home/willi/Research-workspace/AGENTS/WALTER/research/2026-11-05_sweep/headlines.json','w'),indent=0)
print(len(rows))
from collections import Counter
print(Counter(r['k'] for r in rows))
