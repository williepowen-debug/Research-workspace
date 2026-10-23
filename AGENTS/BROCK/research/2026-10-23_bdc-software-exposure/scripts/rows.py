import re,sys,html
def rows(path):
    s=open(path,encoding='utf-8',errors='replace').read()
    for m in re.finditer(r'<tr[^>]*>(.*?)</tr>',s,re.S|re.I):
        r=m.group(1)
        cells=re.findall(r'<td[^>]*>(.*?)</td>',r,re.S|re.I)
        texts=[re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',c))).strip() for c in cells]
        texts=[t for t in texts if t and t not in ('$',')','%')]
        facts=re.findall(r'<ix:nonFraction[^>]*?name="([^"]+)"[^>]*?contextRef="([^"]+)"|<ix:nonFraction[^>]*?contextRef="([^"]+)"[^>]*?name="([^"]+)"',r)
        f=[(a or d, b or c) for a,b,c,d in facts]
        yield texts,f
if __name__=="__main__":
    pat=re.compile(sys.argv[2])
    out=list(rows(sys.argv[1])); n=0
    for i,(t,f) in enumerate(out):
        if any(pat.fullmatch(x) for x in t):
            for t2,f2 in out[max(0,i-2):i+6]: print(len(f2), t2[:8])
            print('---'); n+=1
            if n>=2: break
