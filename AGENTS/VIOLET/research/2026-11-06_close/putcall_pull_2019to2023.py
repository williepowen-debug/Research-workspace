import subprocess,datetime,os,concurrent.futures as cf,json
days=[]
d=datetime.date(2019,10,7)
while d<datetime.date(2024,1,2):
    if d.weekday()<5: days.append(d)
    d+=datetime.timedelta(1)
def get(d):
    p=f"d2/{d}.json"
    if os.path.exists(p) and os.path.getsize(p)>100: return
    subprocess.run(["curl","-sL","-m","20","-A","Mozilla/5.0","-o",p,f"https://cdn.cboe.com/data/us/options/market_statistics/daily/{d}_daily_options"],check=False)
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(get,days))
ok=0;first=None
out=open('pc2.tsv','w')
for d in days:
    try:
        j=json.load(open(f"d2/{d}.json")); r={x['name']:x['value'] for x in j['ratios']}
        out.write(f"{d}\t{float(r['EQUITY PUT/CALL RATIO'])}\n"); ok+=1; first=first or d
    except Exception: pass
print(ok,first)
