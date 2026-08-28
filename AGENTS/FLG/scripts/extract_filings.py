import re,html,sys,os,json

MONTHS=r'(?:January|February|March|April|May|June|July|August|September|October|November|December)'
DATE=re.compile(MONTHS+r'\s+\d{1,2},\s*\d{4}')
NUMRE=re.compile(r'\(?\s*(\d[\d,]*(?:\.\d+)?)\s*\)?')

def totext(p):
    s=open(p,encoding='utf-8',errors='replace').read()
    s=re.sub(r'(?is)<(script|style).*?</\1>',' ',s)
    s=re.sub(r'(?is)<br\s*/?>','\n',s)
    s=re.sub(r'(?is)</(tr|p|div|table|h[1-6])>','\n',s)
    s=re.sub(r'(?is)</t[dh]>',' | ',s)
    s=re.sub(r'(?s)<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    return [l for l in s.split('\n')]

def nums(line):
    """numbers on a line, with dates removed first so a year is never read as a value"""
    line=DATE.sub(' ', line)
    out=[]
    for m in NUMRE.finditer(line):
        raw=m.group(0); v=float(m.group(1).replace(',',''))
        if raw.strip().startswith('('): v=-v
        out.append(v)
    return out

def val_at(lines,i,lookahead=2,pick=0):
    """value for the label on line i: this line, else the next lines.
    pick=0 -> FIRST number on the value line. These filings put the CURRENT period
    in the left column, so a two-column ratio row (31.04 % | 34.62 %) must be read
    at index 0; taking [-1] silently returns the PRIOR period and lags the series."""
    for k in range(i,min(i+1+lookahead,len(lines))):
        n=nums(lines[k])
        if n: return n[pick if pick < len(n) else 0]
    return None

LAB=[('new non-accrual','new'),('charge-offs','co'),('transferred to other','xfer'),
     ('loan payoffs','payoff'),('restored to performing','cure'),
     ('transferred to held for sale','hfs'),('transferred to repossessed','repo'),
     ('acquired from acquisition','acq'),('transferred to other real estate','ore')]

def rollforward(lines):
    for i,l in enumerate(lines):
        ll=l.lower()
        if 'changes in non-accrual loans' in ll or 'changes in nonaccrual loans' in ll:
            seg=lines[i:i+20]; res={}; bals=[]
            for j,s in enumerate(seg):
                sl=s.lower().strip()
                if sl.startswith('balance at'):
                    v=val_at(seg,j)
                    if v is not None: bals.append((DATE.search(s).group(0) if DATE.search(s) else s.strip()[:40], v))
                # AT MOST ONE tag per line, first match wins. Some filings collapse two
                # categories onto one line ("New non-accrual, INCLUDING acquired from
                # acquisition") — matching both double-counts the inflow and the
                # identity still looks plausible unless you check it.
                for key,tag in LAB:
                    if key in sl:
                        if tag not in res:
                            v=val_at(seg,j)
                            if v is not None: res[tag]=v
                        break
            if len(bals)>=2:
                res['begin'],res['end']=bals[0][1],bals[-1][1]
                res['begin_at'],res['end_at']=bals[0][0],bals[-1][0]
                return res
    return None

def scalar(lines,needle,lookahead=2):
    for i,l in enumerate(lines):
        if needle.lower() in l.lower():
            return val_at(lines,i,lookahead)
    return None

def run(p):
    lines=totext(p)
    return {'file':os.path.basename(p),
            'roll':rollforward(lines),
            'cov':scalar(lines,'allowance for credit losses on loans and leases to non-accrual'),
            'narate':scalar(lines,'non-accrual loans to total loans held for investment')}

if __name__=='__main__':
    for p in sys.argv[1:]: print(json.dumps(run(p),default=str))
