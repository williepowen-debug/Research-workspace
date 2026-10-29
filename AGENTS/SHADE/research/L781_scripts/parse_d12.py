import re, sys, json
txt = open(sys.argv[1]).read().splitlines()
cus = re.compile(r'^\s+([0-9A-Z#@*]{6}-[0-9A-Z#@*]{2}-[0-9A-Z#@*])\s+(.*)$')
sub = re.compile(r'^\s+(\d{10})[\.\s-]+\s*(Subtotal|Total)')
desig = re.compile(r'^\.*([A-Z]{1,4})?\.*(\d\.[A-G]?)$')
num = re.compile(r'^\(?[\d,]+\)?$')
def cells(tokens):
    out=[]
    for t in tokens:
        s=t.strip('.')
        if s=='' :
            if len(t)>=8: out.append(None)
            continue
        if num.match(s): out.append(int(s.strip('()').replace(',',''))*(-1 if s.startswith('(') else 1))
        elif re.match(r'^-?[\d.]+$',s): out.append(s)
        else: out.append(s)
    return out
holdings=[]; pending=[]; subs=[]
i=0
while i < len(txt):
    L=txt[i]
    m=cus.match(L)
    if m:
        toks=m.group(2).split()
        di=None
        for k,t in enumerate(toks):
            if desig.match(t): di=k; break
        if di is None:
            print("NODESIG",L[:200],file=sys.stderr); i+=1; continue
        dm=desig.match(toks[di]); rcode=dm.group(1) or ''
        desc=' '.join(toks[:di])
        # restricted code may also be a separate token just before desig
        rest=toks[di+1:]
        sym=[]
        while rest and re.match(r'^[A-Z*]+$',rest[0].strip('.')) and rest[0].strip('.')!='':
            sym.append(rest[0].strip('.')); rest=rest[1:]
        while rest and set(rest[0])=={'.'} and len(rest[0])<8: rest=rest[1:]
        c=[x for x in cells(rest)]
        nums=(c+[None]*4)[:4]
        if len(c)<4: print('SHORT',L[:220],file=sys.stderr)
        h=dict(cusip=m.group(1),desc=desc[:60],rcode=rcode,desig=dm.group(2),sym=' '.join(sym),cost=nums[0],par=nums[1],fv=nums[2],bacv=nums[3])
        pending.append(h); holdings.append(h)
        i+=1; continue
    s=sub.match(L)
    if s:
        code=s.group(1); label=L.strip(); j=i
        vals=None
        while j < len(txt) and j < i+6:
            seg=txt[j]
            ns=re.findall(r'\(?[\d,]{3,}\)?(?=\s|$)',seg.split('XXX')[0] if j>i or True else seg)
            ns=[x for x in ns if x.strip('()').replace(',','').isdigit() and not re.match(r'^\d{10}$',x)]
            if len(ns)>=4: vals=ns; break
            if j>i: label+=' '+seg.strip()
            j+=1
        bacv=int(vals[3].strip('()').replace(',','')) if vals else None
        subs.append(dict(code=code,label=label[:220],bacv=bacv,n=len(pending),sumh=sum((h['bacv'] or 0) for h in pending)))
        for h in pending: h['line']=code
        pending=[]
        i=j+1; continue
    i+=1
json.dump(dict(holdings=holdings,subs=subs),open(sys.argv[2],'w'),indent=0)
for s in subs: print(s['code'], s['n'], s['bacv'], s['sumh'], 'OK' if s['n']==0 or s['sumh']==s['bacv'] else 'MISMATCH', s['label'][14:120])
print(len(holdings),'holdings; leftover',len(pending))
