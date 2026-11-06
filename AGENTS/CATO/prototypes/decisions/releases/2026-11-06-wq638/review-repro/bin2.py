import mmap,re,os
p=os.path.realpath(os.path.expanduser('~/.local/share/claude/versions/2.1.319'))
f=open(p,'rb'); m=mmap.mmap(f.fileno(),0,access=mmap.ACCESS_READ)
pos=[x.start() for x in re.finditer(rb'\.asyncRewake|asyncRewake:[a-zA-Z!]|rewakeMessage\b.{0,40}\?\?',m)]
print(len(pos))
last=-99999
for i in pos:
    if i-last<1500 or i<282500000: continue
    last=i
    print('---',i); print(m[max(0,i-500):i+900].decode('utf8','replace').replace('\n',' '))
