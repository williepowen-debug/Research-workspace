"""census_v3.py — pinned, reconciled fleet prediction census.

Answers CATO's four points (2026-10-01):
 1. exclusion_reason is ONE mutually exclusive value per row; quality flags are separate columns.
 2. p_first = the Confidence cell at the FIRST commit in which the Pred_ID appears in any of the desk's
    ledger files (git history, oldest-first). This is the best available registration probability.
    first_seen_is_file_birth=1 means the row was already present in the file's first commit, so the
    true registration value may be earlier than git can see.
 3. OPEN rows are split not_due / overdue / undated against the pinned date; terminal non-binary rows
    carry their raw status token; a bias check compares p_first across scored vs excluded classes.
 4. Everything reads from one pinned commit (PIN). Population = LIVE ledgers + resolved-row ROTATION
    archives, deduped by (desk, pred_id) with LIVE winning; snapshot copies (before/, cleanup/) and
    markdown archives are listed in provenance but not parsed.
Read-only. Run from repo root. Outputs to the scratchpad.
"""
import csv, re, subprocess, datetime as dt, collections, sys
PIN = sys.argv[1] if len(sys.argv) > 1 else 'origin/master'
PIN = subprocess.check_output(['git','rev-parse',PIN],text=True).strip()
AS_OF = dt.date(2026,10,1)
OUT = '/tmp/claude-0/-home-user-Research-workspace/5d5e7d1c-f558-5999-a452-41b2e3c35b67/scratchpad/'
def show(sha,f):
    try: return subprocess.check_output(['git','show',f'{sha}:{f}'],text=True,stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError: return ''
allfiles=[f for f in subprocess.check_output(['git','ls-tree','-r','--name-only',PIN],text=True).split()
          if re.search(r'PREDICTIONS[^/]*\.tsv$',f) and '/_archive/' not in f]
def classify_file(f):
    if '/before/' in f or '/cleanup/' in f or 'thesis-reconciliation' in f: return 'SNAPSHOT'
    if '/archive/' in f or 'ARCHIVE' in f or 'RESOLVED' in f.upper().split('/')[-1] and 'archive' in f.lower(): return 'ROTATION'
    if 'SCOREBOARD' in f or 'MIRROR' in f: return 'DERIVED'
    return 'LIVE'
def desk(f):
    p=f.split('/'); return p[1] if p[2]!='sub_agents' else p[1]+'/'+p[3]
POS=('CONFIRMED','HIT','TRUE','ACHIEVED','RESOLVED-TRUE','RESOLVED YES','RESOLVED CONFIRMED','RESOLVED-CONFIRM','CORRECT','HELD','OBSERVED')
NEG=('FAILED','MISSED','MISS','FALSE','FALSIFIED','RESOLVED-FALSE','RESOLVED-FAILED','FROZEN-FAILED','RESOLVED_MISS','RESOLVED NO','RESOLVED MISSED','KILLED','WRONG','DISCONFIRMED','REFUTED','RESOLVED-MISS','NOT OBSERVED')
OPENW=('OPEN','ACTIVE','TRACKING','STRENGTHENING','WEAKENING','DUE-UNRESOLVED','ARMED','WATCH')
def m(txt,words): return any(re.match(r'^\W*'+re.escape(w)+r'(\b|$)',txt) for w in words)
def classify(status,outcome):
    s=status.strip().upper().replace('✅','').replace('❌','').strip(); o=outcome.strip().upper().lstrip('✅❌⚠️ ⛔[')
    if any(s.startswith(w) or w in s for w in OPENW) and not s.startswith('RESOLVED'): return 'OPEN'
    if m(s,NEG): return 'FAILED'
    if m(s,POS) and 'MISS' not in s.split('/')[0]:
        if '/ MISS' in s or '/MISS' in s: return 'OTHER'
        return 'CONFIRMED'
    if s.startswith('RESOLVED') or s=='RESOLVED':
        if m(o,NEG) or o.startswith('NO ') or o.startswith('NO —'): return 'FAILED'
        if m(o,POS): return 'CONFIRMED'
        return 'OTHER'
    return 'OTHER'
def conf(c):
    c=(c or '').strip()
    if c.startswith('SCORE AT'): c=c[8:]
    mm=re.match(r'^\W*(\d{1,3})\s*(%|pct)',c)
    return int(mm.group(1))/100 if mm else None
def parse_date(s):
    s=s or ''
    mm=re.search(r'(20\d\d)-(\d\d)-(\d\d)',s)
    if mm:
        try: return dt.date(*map(int,mm.groups()))
        except ValueError: pass
    mm=re.search(r'\b(20\d\d)-(\d\d)\b',s)
    if mm:
        y,mo=map(int,mm.groups()); return dt.date(y+(mo==12),1 if mo==12 else mo+1,1)-dt.timedelta(1)
    mm=re.search(r'\bQ([1-4])\s*(20\d\d)|\b(20\d\d)\s*Q([1-4])',s)
    if mm:
        q=int(mm.group(1) or mm.group(4)); y=int(mm.group(2) or mm.group(3)); return dt.date(y,3*q,[31,30,30,31][q-1])
    mm=re.search(r'\b(end[- ]|by )?(20\d\d)\b',s)
    if mm and 'FY' in s.upper(): return dt.date(int(mm.group(2)),12,31)
    return None
def read_ledger(txt):
    lines=[l for l in txt.splitlines() if l.strip() and not l.startswith('#')]
    r=list(csv.reader(lines,delimiter='\t'))
    if not r: return None,[]
    h=[x.strip() for x in r[0]]; return h,r[1:]
def col(h,*names):
    hl=[x.lower() for x in h]
    for n in names:
        if n.lower() in hl: return hl.index(n.lower())
    return None
# ---------- population ----------
prov=[]; parsed={}  # (desk,id) -> row dict
for f in sorted(allfiles):
    cls=classify_file(f); d=desk(f)
    h,body=read_ledger(show(PIN,f))
    if h is None: prov.append((cls,f,0,'empty')); continue
    ii=col(h,'Pred_ID','ID','id','pred_id'); si=col(h,'Status','status'); co=col(h,'Confidence','conf_tier','confidence')
    oi=col(h,'Outcome','Result','resolution','Outcome_Notes','outcome'); pi=col(h,'Prediction','prediction','claim')
    wi=col(h,'Resolve_By','Resolve_Date','Resolves_On','resolve_date','Resolution_Date','Timeframe','window','Window','Deadline')
    if ii is None or si is None: prov.append((cls,f,len(body),'no Pred_ID/Status column — not parsed')); continue
    if cls in('SNAPSHOT','DERIVED'): prov.append((cls,f,len(body),'listed, not parsed (copy of live)')); continue
    used=0
    for x in body:
        g=lambda i: x[i] if i is not None and i<len(x) else ''
        pid=g(ii).strip()
        if not pid: continue
        key=(d,pid)
        if key in parsed and parsed[key]['src_class']=='LIVE': continue   # live wins
        k=classify(g(si),g(oi)); craw=g(co); p=conf(craw); due=parse_date(g(wi))
        reason=''; sub=''
        if k=='OPEN':
            reason='open'; sub='undated' if due is None else ('overdue' if due<AS_OF else 'not_due')
        elif k=='OTHER': reason='terminal_non_binary'; sub=g(si).strip().upper()[:24]
        elif p is None:
            reason='no_numeric_probability'; sub=('tier_label' if craw.strip() and not re.match(r'^\W*\d',craw.strip()) else 'no_confidence_column' if co is None else 'empty')
        parsed[key]=dict(desk=d,file=f,src_class=cls,pred_id=pid,status_raw=g(si).replace('\n',' ')[:50],cls=k,
            conf_raw=craw.replace('\n',' ')[:50],p_scored=p,outcome_raw=g(oi).replace('\n',' ')[:80],due=due,
            reason=reason,sub=sub,text=g(pi).replace('\n',' ')[:100])
        used+=1
    prov.append((cls,f,len(body),f'parsed; {used} rows kept'))
# ---------- first-committed probability via git history ----------
first={}   # (desk,pid) -> (date, sha, conf)
birth={}   # file -> first commit date
for f in sorted({r['file'] for r in parsed.values()} | {f for c,f,n,_ in prov if c=='LIVE'}):
    log=subprocess.check_output(['git','log',PIN,'--format=%H %cs','--reverse','--',f],text=True).split('\n')
    log=[l.split() for l in log if l.strip()]
    if not log: continue
    birth[f]=log[0][1]; d=desk(f)
    for sha,date in log:
        h,body=read_ledger(show(sha,f))
        if h is None: continue
        ii=col(h,'Pred_ID','ID','id','pred_id'); co=col(h,'Confidence','conf_tier','confidence')
        if ii is None: continue
        for x in body:
            pid=(x[ii] if ii<len(x) else '').strip()
            if not pid or (d,pid) in first: continue
            first[(d,pid)]=(date,sha[:9],conf(x[co] if co is not None and co<len(x) else ''))
# ---------- rows ----------
rows=[]
for key,r in parsed.items():
    fd=first.get(key); pf=fd[2] if fd else None
    rows.append([r['desk'],r['file'],r['src_class'],r['pred_id'],r['status_raw'],r['cls'],r['reason'],r['sub'],
        r['conf_raw'],'' if r['p_scored'] is None else f"{r['p_scored']:.2f}",'' if pf is None else f'{pf:.2f}',
        fd[0] if fd else '',fd[1] if fd else '', 1 if (fd and birth.get(r['file'])==fd[0]) else 0,
        1 if (pf is not None and r['p_scored'] is not None and abs(pf-r['p_scored'])>0.005) else 0,
        r['due'].isoformat() if r['due'] else '',r['outcome_raw'],
        '' if r['cls'] not in('CONFIRMED','FAILED') or r['p_scored'] is None else f"{(r['p_scored']-(r['cls']=='CONFIRMED'))**2:.4f}",
        '' if r['cls'] not in('CONFIRMED','FAILED') or pf is None else f"{(pf-(r['cls']=='CONFIRMED'))**2:.4f}",r['text']])
hdr=['desk','file','src_class','pred_id','status_raw','class','exclusion_reason','sub_reason','confidence_raw','p_scored','p_first_committed',
     'first_commit_date','first_commit_sha','first_seen_is_file_birth','remarked_since_registration','due_date','outcome_raw','brier_scored','brier_first','prediction_text']
with open(OUT+'rows_v3.tsv','w') as fh: w=csv.writer(fh,delimiter='\t'); w.writerow(hdr); w.writerows(rows)
# ---------- summary ----------
def stats(pairs):
    if not pairs: return None
    n=len(pairs); bs=sum((p-o)**2 for p,o in pairs)/n; b=sum(o for p,o in pairs)/n; ref=b*(1-b)
    return dict(n=n,bs=bs,base=b,ref=ref,skill=(1-bs/ref) if ref>0 else None,meanp=sum(p for p,o in pairs)/n)
per=collections.OrderedDict()
for r in rows:
    d=r[0]; st=per.setdefault(d,dict(n=0,scored=0,ps=[],pf=[],both=[],remarked=0,birth=0,open_nd=0,open_od=0,open_un=0,tnb=collections.Counter(),nonum=0,excl_pf=[]))
    st['n']+=1; k=r[5]; p=float(r[9]) if r[9] else None; pf=float(r[10]) if r[10] else None
    if str(r[14])=='1': st['remarked']+=1
    if str(r[13])=='1': st['birth']+=1
    if k in('CONFIRMED','FAILED'):
        o=1.0 if k=='CONFIRMED' else 0.0
        if p is not None:
            st['scored']+=1; st['ps'].append((p,o))
            if pf is not None: st['pf'].append((pf,o)); st['both'].append((p,pf,o))
        else: st['nonum']+=1
    elif k=='OPEN':
        st['open_'+{'not_due':'nd','overdue':'od','undated':'un'}[r[7]]]+=1
        if pf is not None: st['excl_pf'].append(('open',pf))
    else:
        st['tnb'][r[7]]+=1
        if pf is not None: st['excl_pf'].append(('tnb',pf))
hdr2=['desk','rows','scored','base_rate','brier_scored_conf','brier_first_conf(n)','climatology_baseline','skill_scored','skill_first','remarked_rows','rows_at_file_birth','open_not_due','open_overdue','open_undated','terminal_non_binary','no_numeric_prob','mean_p_first_scored','mean_p_first_excluded(n)']
out=[hdr2]; A=[]; B=[]; BOTH=[]; EX=[]
for d,st in per.items():
    s=stats(st['ps']); sf=stats(st['pf']); A+=st['ps']; B+=st['pf']; BOTH+=st['both']; EX+=st['excl_pf']
    exp=[pf for _,pf in st['excl_pf']]; scp=[pf for p,pf,o in st['both']]
    out.append([d,st['n'],st['scored'],'' if not s else f"{s['base']:.2f}",'' if not s else f"{s['bs']:.3f}",'' if not sf else f"{sf['bs']:.3f} ({sf['n']})",
        '' if not s else f"{s['ref']:.3f}",'' if not s or s['skill'] is None else f"{s['skill']:+.2f}",'' if not sf or sf['skill'] is None else f"{sf['skill']:+.2f}",
        st['remarked'],st['birth'],st['open_nd'],st['open_od'],st['open_un'],sum(st['tnb'].values()),st['nonum'],
        '' if not scp else f"{sum(scp)/len(scp):.2f}",'' if not exp else f"{sum(exp)/len(exp):.2f} ({len(exp)})"])
S=stats(A); SF=stats(B)
scp=[pf for p,pf,o in BOTH]; exp=[pf for _,pf in EX]
out.append(['FLEET',sum(v['n'] for v in per.values()),S['n'],f"{S['base']:.3f}",f"{S['bs']:.4f}",f"{SF['bs']:.4f} ({SF['n']})",f"{S['ref']:.4f}",f"{S['skill']:+.3f}",f"{SF['skill']:+.3f}",
    sum(v['remarked'] for v in per.values()),sum(v['birth'] for v in per.values()),sum(v['open_nd'] for v in per.values()),sum(v['open_od'] for v in per.values()),sum(v['open_un'] for v in per.values()),
    sum(sum(v['tnb'].values()) for v in per.values()),sum(v['nonum'] for v in per.values()),f"{sum(scp)/len(scp):.2f}",f"{sum(exp)/len(exp):.2f} ({len(exp)})"])
with open(OUT+'summary_v3.tsv','w') as fh: csv.writer(fh,delimiter='\t').writerows(out)
with open(OUT+'provenance_v3.txt','w') as fh:
    fh.write(f'PIN={PIN}\nAS_OF={AS_OF}\nrows_kept={len(rows)}\n\nFILES (class, path, data rows, disposition):\n')
    for c,f,n,disp in prov: fh.write(f'{c}\t{f}\t{n}\t{disp}\n')
    fh.write('\nRULES: class from Status (+Outcome when Status=RESOLVED) via token lists in script; p_scored = current Confidence cell leading integer %; '
             'p_first = Confidence cell at first commit containing the Pred_ID in that file (oldest-first git log); '
             'exclusion_reason mutually exclusive: open | terminal_non_binary | no_numeric_probability; '
             'OPEN sub_reason by due-date column vs AS_OF; dedupe (desk,pred_id) LIVE over ROTATION.\n')
for r in out: print('\t'.join(str(c) for c in r))
n=len(BOTH); print(f"\nPINNED {PIN[:9]}  rows {len(rows)}  scored {S['n']}")
print(f"RE-MARKED SINCE REGISTRATION (scored rows with p_first != p_scored): {sum(1 for p,pf,o in BOTH if abs(p-pf)>0.005)} of {n} with history")
print(f"  Brier on those rows: at scored conf {sum((p-o)**2 for p,pf,o in BOTH if abs(p-pf)>0.005)/max(1,sum(1 for p,pf,o in BOTH if abs(p-pf)>0.005)):.3f}  at first-committed conf {sum((pf-o)**2 for p,pf,o in BOTH if abs(p-pf)>0.005)/max(1,sum(1 for p,pf,o in BOTH if abs(p-pf)>0.005)):.3f}")
tnb=collections.Counter(); [tnb.update(v['tnb']) for v in per.values()]
print('TERMINAL NON-BINARY status tokens:',dict(tnb.most_common(12)))
print(f"EXCLUSION-BIAS CHECK: mean p_first scored={sum(scp)/len(scp):.3f} (n={len(scp)})  open={sum(pf for k,pf in EX if k=='open')/max(1,sum(1 for k,pf in EX if k=='open')):.3f} (n={sum(1 for k,pf in EX if k=='open')})  terminal_non_binary={sum(pf for k,pf in EX if k=='tnb')/max(1,sum(1 for k,pf in EX if k=='tnb')):.3f} (n={sum(1 for k,pf in EX if k=='tnb')})")
