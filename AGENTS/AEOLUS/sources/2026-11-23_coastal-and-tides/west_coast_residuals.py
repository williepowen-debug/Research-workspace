import json,urllib.request as u,statistics as s
S={'9410230':'La Jolla','9410660':'Los Angeles','9414290':'San Francisco','9419750':'Crescent City','9432780':'Charleston OR'}
P=[('Aug','20260801','20260831'),('Sep','20260901','20260930'),('Oct1-19','20261001','20261019'),('Oct20-28','20261020','20261028'),('Nov1-22','20261101','20261122')]
b="https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?station=%s&begin_date=%s&end_date=%s&datum=STND&units=english&time_zone=gmt&format=json&application=research-bot&product=%s&interval=h"
def g(x):
    try:return json.load(u.urlopen(x,timeout=60))
    except Exception as e:return {'e':str(e)}
for k,n in S.items():
    o=[]
    for l,a,e in P:
        h=g(b%(k,a,e,'hourly_height'))
        if 'data' not in h:
            h=g((b%(k,a,e,'water_level')).replace('&interval=h',''))
        p=g(b%(k,a,e,'predictions'))
        if 'data' not in h or 'predictions' not in p:o.append((l,'FAIL',str(h)[:80]));continue
        pm={x['t']:float(x['v']) for x in p['predictions']}
        r=[float(x['v'])-pm[x['t']] for x in h['data'] if x['v'] and x['t'] in pm]
        o.append((l,round(s.mean(r),2),len(r)))
    print(n,o)
print('predicted highs next days')
for k,n,mi in(('8724580','Key West',7.47),('8723214','Virginia Key',13.68),('8722670','Lake Worth',34.35),('8721604','Trident',23.69),('9414290','San Francisco',13.02)):
    p=g((b%(k,'20261124','20261231','predictions')).replace('time_zone=gmt','time_zone=lst_ldt'))
    d={}
    for x in p['predictions']:d[x['t'][:10]]=max(d.get(x['t'][:10],-9),float(x['v']))
    top=sorted(d.items(),key=lambda z:-z[1])[:4];print(n,'minor',mi,'11/24-27',[d['2026-11-%d'%i] for i in(24,25,26,27)],'top to 12/31',top)
