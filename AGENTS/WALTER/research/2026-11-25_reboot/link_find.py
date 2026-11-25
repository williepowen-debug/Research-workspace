import glob,re
rows=[]
for d in ('VULCAN','BROCK','LIQUID','SAM','SHADE'):
    for f in glob.glob(f'AGENTS/{d}/workbook/KB*.tsv'):
        for l in open(f,errors='ignore'):
            rows.append((d,l.rstrip('\n')))
def find(label,must,win=230,n=4,since='2026-08'):
    print('##',label); c=0
    out=[]
    for d,l in rows:
        p=l.split('\t'); date=next((x for x in p[:4] if re.match(r'2026-\d\d-\d\d',x)),'')
        if date<since: continue
        for m in re.finditer(must[0],l,re.I):
            s=l[max(0,m.start()-win):m.end()+win]
            if all(re.search(q,s,re.I) for q in must[1:]): out.append((date,d,p[0],s)); break
    for o in sorted(out,reverse=True)[:n]: print(f'[{o[1]} {o[2]} {o[0]}] {o[3]}\n')
find('OpenAI-CoreWeave',['CoreWeave','OpenAI',r'contract|customer|backlog|RPO|revenue'])
find('OpenAI-Oracle',['Oracle','OpenAI',r'RPO|contract|tenant|lease'])
find('SB Energy',['SB Energy','OpenAI|Nvidia'])
find('Nvidia guarantee',[r'guarant','Nvidia|NVDA','OpenAI|SB Energy|CoreWeave|neocloud'])
find('Stargate',['Stargate|Jupiter','Oracle','SoftBank|OpenAI|Blue Owl'])
find('MUFG',['MUFG|Mitsubishi UFJ','CoreWeave|SoftBank|Oracle|Jupiter'])
find('Morgan Stanley',['Morgan Stanley','CoreWeave|SoftBank|Oracle'],n=3)
find('JPM',['JPMorgan|JPM','CoreWeave|SoftBank|Oracle|Jupiter'],n=3)
find('Athene',['Athene','Oracle','SoftBank'],n=2)
find('Blue Owl',['Blue Owl','Oracle|CoreWeave'],n=3)
find('HSBC SocGen ING',['HSBC|SocGen|Societe|ING ','Oracle|Jupiter|New Mexico|Stargate'],n=3)
