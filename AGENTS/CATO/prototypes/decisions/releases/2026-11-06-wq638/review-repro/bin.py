import mmap,re,glob,os
p=os.path.realpath(os.path.expanduser('~/.local/share/claude/versions/2.1.319'))
f=open(p,'rb'); m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
seen=set()
for key in (b'asyncRewake',b'hook_non_blocking_error'):
    i=0;n=0
    while n<6:
        i=m.find(key,i)
        if i<0: break
        s=m[max(0,i-260):i+420].decode('utf8','replace')
        h=s[200:330]
        if h not in seen:
            seen.add(h); print('---',key.decode(),i); print(s.replace('\n',' '))
            n+=1
        i+=len(key)+2000
