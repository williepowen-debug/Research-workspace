import zipfile,os,csv,sys,re
csv.field_size_limit(10**7)
base=sys.argv[1]
K=['Acct_997','ACCT_010','ACCT_400J2','ACCT_400J3','ACCT_DL0111','ACCT_DL0112','ACCT_DL0108','ACCT_DL0109','ACCT_DL0110','ACCT_DL0146','ACCT_RB0177','ACCT_1061','ACCT_400T1']
for tag,zz,xx in (('2025-12','cu_2025-12.zip','x2025-12'),('2026-03','cu_2026-03.zip','x2026-03'),('2026-06',None,'x')):
    root=os.path.realpath(os.path.join(base,xx))
    if zz:
        z=zipfile.ZipFile(os.path.join(base,zz))
        for i in z.infolist():
            assert os.path.realpath(os.path.join(root,i.filename)).startswith(root+os.sep)
        z.extractall(root)
    fo=[f for f in os.listdir(root) if f.upper().startswith('FOICU.')][0]
    cu=None
    names=sorted(os.listdir(root))
    v={}
    for f in names:
        if not re.match(r'(?i)FS220.*\.txt',f): continue
        for r in csv.DictReader(open(os.path.join(root,f),errors='replace')):
            if r.get('CU_NUMBER')=='15732':
                for k in K:
                    for kk in (k,k.upper(),k.replace('ACCT','Acct')):
                        if kk in r and r[kk] not in('',None): v[k]=r[kk]
    print(tag,{k:(round(float(v[k])/1e6,1) if k in v and float(v[k])>1e4 else v.get(k)) for k in K})
