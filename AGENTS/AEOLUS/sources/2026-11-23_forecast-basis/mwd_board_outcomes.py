import json,urllib.request as u,urllib.parse as q,collections,time
B='https://webapi.legistar.com/v1/mwdh2o/'
def g(x):
    for a in range(5):
        try:return json.load(u.urlopen(B+x,timeout=40))
        except Exception as e:time.sleep(3+3*a)
    raise SystemExit("fail "+x)
ev=g("events?$filter="+q.quote("EventDate ge datetime'2025-01-01' and EventDate lt datetime'2026-11-20'"))
ev=[e for e in ev if 'Board of Directors' in e['EventBodyName']]
print(len(ev),collections.Counter(e['EventBodyName'] for e in ev))
C=collections.Counter();rows=[];seen=set();col=[]
for e in ev:
    for i in g(f"events/{e['EventId']}/eventitems?AgendaNote=1"):
        n=i.get('EventItemAgendaNumber') or '';t=i.get('EventItemTitle') or '';m=i.get('EventItemMatterFile')
        if n.startswith('8-') and m and (m,e['EventId']) not in seen and 'closed session' not in t.lower():
            seen.add((m,e['EventId']));s=i.get('EventItemMatterStatus');C[s]+=1
            if 'Colorado' in t or 'Reclamation' in t:col.append((e['EventDate'][:10],n,m,s,t[:110]))
            rows.append((e['EventDate'][:10],n,m,s,'DEFER' in t.upper() or 'WITHDRAWN' in t.upper(),t[:60]))
    time.sleep(.2)
print(C,'n',len(rows),'title flagged deferred/withdrawn',sum(r[4] for r in rows))
print('Colorado items');[print(' ',c) for c in col]
