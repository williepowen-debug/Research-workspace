import sys, pdfplumber, multiprocessing as mp
sys.path.insert(0,'.')
from rot import rot_lines
PDF=sys.argv[1]; a,b=int(sys.argv[2]),int(sys.argv[3]); out=sys.argv[4]; nw=int(sys.argv[5])
def work(chunk):
    res=[]
    with pdfplumber.open(PDF) as p:
        for n in chunk:
            pg=p.pages[n-1]
            if pg.rotation in (90,270): ls=rot_lines(pg)
            else: ls=(pg.extract_text(layout=True) or '').split('\n')
            res.append((n,'\n'.join(ls)))
            pg.close() if hasattr(pg,'close') else None
    return res
if __name__=='__main__':
    pages=list(range(a,b+1)); k=(len(pages)+nw-1)//nw
    chunks=[pages[i:i+k] for i in range(0,len(pages),k)]
    with mp.Pool(nw) as pool:
        allr=[r for rr in pool.map(work,chunks) for r in rr]
    with open(out,'w') as f:
        for n,t in sorted(allr): f.write(f'\n=====PAGE {n}=====\n{t}\n')
