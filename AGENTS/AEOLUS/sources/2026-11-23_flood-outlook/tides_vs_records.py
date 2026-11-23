import json,urllib.request as u
b="https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?station=%s&begin_date=20261122&end_date=20261123&datum=MLLW&units=english&time_zone=lst_ldt&format=json&application=research-bot&product=%s"
for s,n in(('9410230','La Jolla'),('9410170','San Diego'),('9410660','Los Angeles'),('9414290','San Francisco'),('9415144','Port Chicago')):
    try:
        o=json.load(u.urlopen(b%(s,'water_level'),timeout=40))['data'];p={x['t']:float(x['v']) for x in json.load(u.urlopen(b%(s,'predictions')+'&interval=6',timeout=40))['predictions']}
        m=max((float(x['v']),x['t']) for x in o if x['v'] and x['t'][:10]=='2026-11-23');print(n,'11/23 max MLLW',m,'pred',p.get(m[1]))
        e=json.load(u.urlopen(f'https://api.tidesandcurrents.noaa.gov/mdapi/prod/webapi/stations/{s}/datums.json?units=english',timeout=40))
        ml=[d['value'] for d in e['datums'] if d['name']=='MLLW'][0];print('   record high MLLW',round(e['max']-ml,2) if e.get('max') else None,e.get('maxdate'))
    except Exception as x:print(n,x)
