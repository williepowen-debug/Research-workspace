import mmap,re,os
p=os.path.realpath(os.path.expanduser('~/.local/share/claude/versions/2.1.319'))
f=open(p,'rb'); m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
i=m.find(b'function Tlt({processId')
print(m[i+1250:i+3100].decode('utf8','replace').replace('\n',' '))
for k in (rb'function ye\(\)\{[^}]{0,120}\}',rb'function eWt\(\)\{[^}]{0,200}\}',rb'function N0\(e,n\)'):
    for x in list(re.finditer(k,m))[:2]:
        print('==',m[x.start():x.end()+60].decode('utf8','replace'))
