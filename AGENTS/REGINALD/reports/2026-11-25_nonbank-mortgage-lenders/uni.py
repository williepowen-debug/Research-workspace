import csv,glob,os,sys
csv.field_size_limit(10**9)
def por(d):
    f=glob.glob(os.path.join(d,"FFIEC CDR Call Bulk POR *.txt"))[0]; r=csv.reader(open(f,encoding="latin-1",newline=""),delimiter="\t"); next(r)
    return {x[0].strip():(x[5].strip(),x[8].strip() if len(x)>8 else "") for x in r if x and x[0].strip()}
def load(d,codes):
    k=por(d); o={}
    for f in glob.glob(os.path.join(d,"FFIEC CDR Call Schedule *.txt")):
        r=csv.reader(open(f,encoding="latin-1",newline=""),delimiter="\t"); c=[x.strip('"') for x in next(r)]; next(r)
        ix=[(i,x) for i,x in enumerate(c) if x[4:] in codes]
        if not ix: continue
        for row in r:
            if not row: continue
            s=row[0].strip().strip('"')
            if s not in k: continue
            e=o.setdefault(s,{})
            for i,x in ix:
                if i<len(row) and row[i].strip() and x not in e: e[x]=row[i].strip()
    return k,o
def g(e,c,p=("RCON","RCFD")):
    for q in p:
        if q+c in e: return float(e[q+c])
