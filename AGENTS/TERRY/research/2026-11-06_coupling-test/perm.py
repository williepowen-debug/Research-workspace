import random,statistics as st,json
d={2007:58,2008:-187,2009:326,2010:-145,2011:-195,2012:-195,2013:-29,2014:-202,2015:20,2016:-186,2017:-180,2018:-203,2019:-195,2020:-46,2021:33,2022:334,2023:142,2024:325,2025:-203}
A=json.load(open('data/ao_pass.json')); ao=set(A['pass_card_read']); an={int(k):v for k,v in A['anom'].items()}
Y=list(d); P=[y for y in Y if y in ao]; obs=st.mean(d[y] for y in P)-st.mean(d[y] for y in Y if y not in ao)
random.seed(631); k=len(P); N=100000; c=0
for _ in range(N):
    S=set(random.sample(Y,k)); v=st.mean(d[y] for y in S)-st.mean(d[y] for y in Y if y not in S)
    if abs(v)>=abs(obs): c+=1
print('AO pass years',P); print('AO hold-minus-sell gap',round(obs),'two-sided permutation p',round(c/N,3))
yrs=list(an); P2=[y for y in yrs if y in ao]; o2=st.mean(an[y] for y in P2)-st.mean(an[y] for y in yrs if y not in ao); c=0
for _ in range(N):
    S=set(random.sample(yrs,len(P2))); v=st.mean(an[y] for y in S)-st.mean(an[y] for y in yrs if y not in S)
    if abs(v)>=abs(o2): c+=1
print('AO temp gap',round(o2,2),'F p',round(c/N,3))
c14=list(range(2012,2026)); P3=[2013,2016,2017,2025]; o3=st.mean(an[y] for y in P3)-st.mean(an[y] for y in c14 if y not in P3); c=0
for _ in range(N):
    S=set(random.sample(c14,4)); v=st.mean(an[y] for y in S)-st.mean(an[y] for y in c14 if y not in S)
    if abs(v)>=abs(o3): c+=1
print('CPC 12/3 temp gap',round(o3,2),'F p',round(c/N,3))
