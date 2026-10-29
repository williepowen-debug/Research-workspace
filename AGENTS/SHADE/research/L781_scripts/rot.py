import sys, pdfplumber, collections
def rot_lines(pg, tol=2.0):
    rows=collections.defaultdict(list)
    for c in pg.chars:
        key=round(c['x0']/tol)
        rows[key].append(c)
    out=[]
    for k in sorted(rows):
        cs=sorted(rows[k], key=lambda c: -c['bottom'])
        s=''; last=None
        for c in cs:
            if last is not None and last-c['bottom']>c.get('size',6)*0.6: s+=' '
            s+=c['text']; last=c['top']
        out.append(s)
    return out
if __name__=='__main__':
    pdf=sys.argv[1]; pages=[int(x) for x in sys.argv[2].split(',')]
    with pdfplumber.open(pdf) as p:
        for n in pages:
            pg=p.pages[n-1]
            print('=====PAGE',n, pg.rotation)
            for l in rot_lines(pg): print(l)
