import sys,itertools,random,json
sys.path.insert(0,sys.argv[1]+'/PROME/tools')
import argus_policy as p
# Direct textual matcher; no production parser, state, atom or helper calls.
def match(pat,path):
 a,b=pat.split('/'),path.split('/'); rec=a[-1]=='**'
 if rec:a=a[:-1]
 if (rec and len(b)<=len(a)) or (not rec and len(b)!=len(a)):return False
 return all(x=='*' or (x.startswith('*.') and y.endswith(x[1:])) or x==y for x,y in zip(a,b))
def classify(rows,path):
 return next((c for a,c,_ in rows if match(a,path)),'UNATTRIBUTED')
segments=['a','b','.md','x.md','.x.md','a.x.md','é','\n','.gitx']
patterns=['r/**','r/*','r/a','r/*.md','r/*.x.md','r/*/a','r/a/**','r/b/**','r/*/**','s/*/a']
rules=[(x,c,'independent') for x in patterns for c in ['OWNED','EXCLUDED']]
cases=list(itertools.product(rules,repeat=2))
rng=random.Random(1104835)
cases += [tuple(rng.choice(rules) for _ in range(rng.randrange(3,12))) for _ in range(150)]
queries=['r','r/a','r/b','r/é','s']
count=0
for rows in cases:
 policy=p.compile_policy(rows)
 for directory in queries:
  # All fixed tokens <= 3; enumerate independently through absolute depth 5,
  # two levels beyond maximum fixed depth, with a complete alphabet for this domain.
  expect=False
  for n in range(1,max(1,5-len(directory.split('/')))+1):
   for tail in itertools.product(segments,repeat=n):
    path=directory+'/'+ '/'.join(tail)
    cls=classify(rows,path)
    assert policy.classify(path)[0]==cls,(rows,path)
    count+=1
    if cls!='EXCLUDED':expect=True;break
   if expect:break
  actual=policy.has_protected_descendant(directory)
  assert actual==expect,(rows,directory,actual,expect)
# Novel complement case: excluded suffix leaves non-suffix dotfiles protected.
a=p.compile_policy([('r/*.md','EXCLUDED','x'),('r/*','OWNED','x'),('r/**','EXCLUDED','x')])
assert a.has_protected_descendant('r') and a.classify('r/é')[0]=='OWNED'
# Novel full shadow: both finite exact and recursive exclusion cover later suffix ownership.
a=p.compile_policy([('r/*','EXCLUDED','x'),('r/*/**','EXCLUDED','x'),('r/*.x.md','OWNED','x')])
assert not a.has_protected_descendant('r')
# Genuine resource exhaustion, no method replacement.
try:a.has_protected_descendant('r',state_limit=1)
except p.EvaluationError:pass
else:raise AssertionError('limit did not refuse')
print(json.dumps({'seed':1104835,'policies':len(cases),'queries':len(cases)*len(queries),'concrete_comparisons':count,'result':'PASS'}))
