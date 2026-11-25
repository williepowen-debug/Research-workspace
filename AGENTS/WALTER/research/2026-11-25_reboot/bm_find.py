import glob,re,os,json,datetime,sys
R='/home/willi/Research-workspace/'
pats={'SOFTBANK':r'softbank|\bSBG\b|9984','ORACLE':r'oracle(?! (action|info|owns|desk|read|grade|row|\())|\bORCL\b'}
seen=set()
for name,p in pats.items():
    print('#####',name)
    for f in sorted(glob.glob(R+'BOARD/SIG-W-2026*.md')):
        s=open(f,errors='ignore').read()
        if not re.search(p,s,re.I if name=='SOFTBANK' else 0) and not (name=='ORACLE' and re.search(r'\bORCL\b|Oracle (Corp|bond|CDS|debt|5Y|credit|Q\d|shares|stock|capex|loan|financ)|Oracle\b',s)): continue
        if not re.search(r'bookmark|x\.com/|X post|\b2[01]\d{17}\b|x-bookmark',s,re.I): continue
        n=len(re.findall(p,s,re.I))
        t=re.search(r'^# (.*)$',s,re.M)
        prec=re.search(r'^status: (.*)$',s,re.M)
        print(os.path.basename(f)[6:18],n,(prec.group(1) if prec else '-'),'|',(t.group(1) if t else '')[:170])
