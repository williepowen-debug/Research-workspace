import re, zlib, sys, difflib
SRC='PROME/GATES.tsv'; OUTDIR=sys.argv[1]
txt=open(SRC,encoding='utf-8').read(); lines=txt.split('\n')
cols=lines[13].split('\t'); assert len(cols)==12
hist=[]
def rotate_cell(g,c,v):
    m=re.search(r'(?i)(?<![A-Za-z])prior(?:\s*\([^)]*\))?\s*:',v)
    if not m: return v
    cur=v[:m.start()].rstrip().rstrip('.;—·‖').rstrip()
    tail=v[m.start():]
    hist.append(f"\n## {g} · {c} — Prior: chain rotated 2026-09-03 (WQ-166 step 2, Will 'pull step 2 forward' 12:45)\nentry-crc32: {zlib.crc32(tail.encode('utf-8'))} · bytes: {len(tail.encode('utf-8'))} · rotated 2026-09-03\n\n{tail}\n")
    if 'hist→GATES_STATE_HISTORY' not in cur: cur+=' · hist→GATES_STATE_HISTORY'
    return cur
rows={}
order=[]
for i,l in enumerate(lines):
    if i>13 and l.strip() and not l.startswith('#'):
        r=dict(zip(cols,l.split('\t'))); rows[r['gate_id']]=(i,r); order.append(r['gate_id'])
for g in order:
    i,r=rows[g]
    for c in ['last_checked','consumed_by','review_by']:
        r[c]=rotate_cell(g,c,r[c])
# ③ USO135C source
r=rows['GATE-TERRY-USO135C'][1]; a='PROME/inbox/2026-09-01_from-TERRY_'; assert r['source'].count(a)==1; r['source']=r['source'].replace(a,'PROME/inbox/processed/2026-09-01_from-TERRY_')
# ④ HY-REKILL
r=rows['GATE-HY-REKILL'][1]
a='definition_surface mirrors this cell (LIQUID owes the fold)'; assert r['condition'].count(a)==1
r['condition']=r['condition'].replace(a,'definition_surface does NOT yet hold this letter — LIQUID owes the fold (the ruled exception in header ENVELOPE COLUMNS)')
r['last_checked']="2026-09-03 12:5x (PROME, step-2 package; observation-chain gloss, no count moved): 263 is the AS-OF value on BOTH 8/27 and 8/31 — two observations, one level; the 8/28 as-of print = 260, PUBLISHED 8/31 (as-of vs publication dates labelled). Then: "+r['last_checked']
# ⑥ TERRY-007 gloss
r=rows['GATE-TERRY-007'][1]; a='8 runs ≥5 ⇒ CALIBRATED not structural'; assert r['last_checked'].count(a)==1
r['last_checked']=r['last_checked'].replace(a,'8 runs ≥5 ⇒ CALIBRATED not structural (8 runs at 80% below is consistent: the 209-close run alone is 42% of the sample; closes are autocorrelated, not i.i.d.)')
# ❌1 (pre-edit read 2): 007 review_by pointed at a read this pass rotates out
r=rows['GATE-TERRY-007'][1]; a="is in last_checked"; assert r['review_by'].count(a)==1, r['review_by'][:300]
r['review_by']=r['review_by'].replace(a,"is in GATES_STATE_HISTORY_2026-09-03_step2.md (GATE-TERRY-007 · last_checked; the OWNER grade of 9/1 is the live last_checked)")
# ⚠️11/⚠️14: REG-T02 (RESOLVED) points at the successor guard row; its current consumed_by/review_by text rotates to history
r=rows['GATE-REG-T02'][1]
for c,newv in [('consumed_by',"— (terminal: FIRED 9/1, consumed by ROLL70 9/2; the EXIT guard WAL ≥81.90 ×3 lives on GATE-TERRY-ROLL70-EXIT since 9/3 — that row seeds the S9 registry, not this one) · hist→GATES_STATE_HISTORY"),('review_by',"— (terminal; successor clock = GATE-TERRY-ROLL70-EXIT review_by 2026-12-04; this row rotates to GATES_TERMINAL_ROWS ≥7d after 9/1) · hist→GATES_STATE_HISTORY")]:
    old=r[c]; hist.append(f"\n## GATE-REG-T02 · {c} — current text superseded 2026-09-03 (guard re-homed to GATE-TERRY-ROLL70-EXIT)\nentry-crc32: {zlib.crc32(old.encode('utf-8'))} · bytes: {len(old.encode('utf-8'))} · superseded 2026-09-03\n\n{old}\n"); r[c]=newv
# ② new LIVE guard row
new={
'gate_id':'GATE-TERRY-ROLL70-EXIT',
'registered':"2026-09-03 (WQ-166 step 2 package, Will 'pull step 2 forward' 12:45; the guard itself was registered 9/1 inside GATE-REG-T02 / GATE-TERRY-ROLL70 — re-homed to a LIVE row because both carriers are RESOLVED and the ~7-day terminal rotation would remove an OPEN position's only guard)",
'owner':'REGINALD (grades) / TERRY (proposal) / Will (executes)',
'condition':"WAL OFFICIAL CLOSE ≥ $81.90 on THREE CONSECUTIVE sessions (= the REG-T-02 EXIT registered 9/1 as ROLL70's guard; a close <81.90 resets the count). Count 0-of-3 at the 9/2 close $79.12. FULL LETTER → definition_surface (ROLL70 card, guard section) — this cell is summary + pointer only",
'consequence_on_fire':"TERRY builds the close-out proposal for the WAL Dec-18-2026 $70P ×1 (ROBINHOOD) next session → Will [Approve]; Will's hand at the broker (root rules #4/#5); nothing self-executes. Time stop 2026-12-04 stands independently",
'state':"LIVE — EXIT count 0 of 3; WAL $79.12 [9/2 close] = $2.78 below the line (9/3 12:20 intraday 80.05, TERRY c8c58a363 — not a close) · hist→GATES_STATE_HISTORY",
'last_checked':"2026-09-03 12:5x REGISTERED (PROME, step-2 package): count 0-of-3 carried from the REG-T02 / ROLL70 cells through the 9/2 close; REGINALD grades each official close from 9/3 (its NOTES.md §REG-T-02 STATE RULING is the grading surface)",
'source':'AGENTS/TERRY/setups/WAL_dec18-70P-duration-roll_2026-09-01.md (the letter) + AGENTS/REGINALD/registry/NOTES.md §REG-T-02 STATE RULING (the grading surface) + PROME/proposals/2026-09-01_wq-batch-RULED.md row 143; provenance rows GATE-REG-T02 / GATE-TERRY-ROLL70 (RESOLVED; they rotate to GATES_TERMINAL_ROWS ~9/8 — this row does not depend on them)',
'consumed_by':'PRICE:WAL_official_close>=81.90 ×3 consecutive | TERRY close-out proposal → Will [Approve] | TERRY (REGINALD grades)',
'scannable':'INSTRUMENT',
'definition_surface':'AGENTS/TERRY/setups/WAL_dec18-70P-duration-roll_2026-09-01.md',
'review_by':'2026-12-04 (ROLL70 time stop — the guard dies with the position; earlier only on a fill of the exit)',
}
assert len(new)==12 and list(new)==cols
# ⑤ header §8 rewrite of the 9/3 note (placeholder for measured size)
H8=lines[7]; a=H8.index(' ⚠️ 9/3 blind read #2:'); H8_REMOVED=H8[a+1:]; H8=H8[:a]
nt=" Next touch (registered): live rows' 'Prior:' history chains in last_checked/consumed_by/review_by → GATES_STATE_HISTORY, to get under the 32,550 B budget."; assert H8.count(nt)==1; H8=H8.replace(nt,''); H8_REMOVED=nt.strip()+"  ‖  "+H8_REMOVED
lines[7]=H8+" ✅ STEP 2 EXECUTED 2026-09-03 (Will 'pull step 2 forward' 12:45, pre-edit blind read on the proposed diff): every 'Prior:' chain in last_checked / consumed_by / review_by rotated VERBATIM (crc) to PROME/archive/GATES_STATE_HISTORY_2026-09-03_step2.md (its last section = the 9/3 blind-read note this stamp replaced: at 52,763 B a whole-file read truncated at 'row 27 of 33' by that reader's own line count); file {SIZE} B after — ⚠️ that is AT the ~50,000 B practical ceiling ({HEAD}), so the NEXT registration breaches it: step 3 is dated, not optional (DOCKET L251 = this step's record; L256 = step 3). CAPS DEFINED: 54,250 B = the physical whole-file read ceiling at which a reader dropped rows on 9/3 (readers ALSO truncated at ~52.7 KB — treat ~50,000 B as the practical ceiling, not 54,250); 32,550 B = the READ_CAP budget (canon AGENTS/DAEDALUS/BLUEPRINTS/READ_CAP.md). Still over BUDGET after step 2 ⇒ STEP 3 (DOCKET L256) = condition cells → summary + pointer per ENVELOPE COLUMNS (owner confirms; LIQ-069/072/076/079 · CORAL-MSI-01 · FLG-T08 · HY-REKILL by ruling stays) — a DESIGN to Will, registered on DOCKET."
L6=lines[5]; a6='Full prior cell text lives VERBATIM at PROME/archive/GATES_STATE_HISTORY_2026-08-29.md keyed by gate_id with entry-crc32 (recompute, never trust).'; assert L6.count(a6)==1
lines[5]=L6.replace(a6,'Full prior cell text lives VERBATIM in the PROME/archive/GATES_STATE_HISTORY_*.md family (one file per rotation pass — 2026-08-29 = superseded state cells; 2026-09-03_step2 = rotated Prior-chains from last_checked/consumed_by/review_by), keyed by gate_id with entry-crc32 (recompute, never trust; grep by gate_id, never whole-read).')
def render():
    out=lines[:14]
    for g in order:
        i,r=rows[g]; out.append('\t'.join(r[c] for c in cols))
        if g=='GATE-TERRY-ROLL70': out.append('\t'.join(new[c] for c in cols))
    return out
out=render(); body='\n'.join(out)
def fill(b,sz): return b.replace('{SIZE}',f"{sz:,}").replace('{HEAD}',(f"{sz-50000:,} B over" if sz>50000 else f"{50000-sz:,} B under"))
size=len(fill(body,50000).encode('utf-8'))+1; size=len(fill(body,size).encode('utf-8'))+1; body=fill(body,size)+'\n'; assert len(body.encode('utf-8'))==size
open(f'{OUTDIR}/GATES_proposed.tsv','w',encoding='utf-8').write(body)
HDR=("# GATES.tsv history — step 2 of the WQ-166 split (2026-09-03, Will 'pull step 2 forward' 12:45 ET)\n\n*Each section = the VERBATIM 'Prior…:' tail rotated out of ONE cell (`last_checked`, `consumed_by` or `review_by`) of the named gate_id, byte-exact; `entry-crc32` = zlib.crc32 over the section body (UTF-8), `bytes` = its UTF-8 length. Recompute to verify — never trust the banner. The live cell keeps its CURRENT text and the suffix `· hist→GATES_STATE_HISTORY` (the family name — one file per rotation pass, `ls PROME/archive/GATES_STATE_HISTORY_*.md`; grep by gate_id, never whole-read). The 2026-08-29 file holds superseded STATE cells; this file holds Prior-chains. Also appended here: the header §8 text this pass replaced (last section).*\n")
hist.append(f"\n## HEADER §8 (TERMINAL-ROW ARCHIVE) — the 9/3 blind-read note replaced by the step-2 stamp\nentry-crc32: {zlib.crc32(H8_REMOVED.encode('utf-8'))} · bytes: {len(H8_REMOVED.encode('utf-8'))} · rotated 2026-09-03\n\n{H8_REMOVED}\n")
open(f'{OUTDIR}/HISTORY_STEP2_proposed.md','w',encoding='utf-8').write(HDR+''.join(hist))
# invariants
rep=[]
prow=[l for l in body.split('\n')[14:] if l.strip() and not l.startswith('#')]
rep.append(f"rows: {len(prow)} (expected 19 = 18 + GATE-TERRY-ROLL70-EXIT)")
rep.append(f"columns: {set(len(l.split(chr(9))) for l in prow)} (expected {{12}})")
mx=max(len(l.split('\t')[cols.index('state')]) for l in prow); rep.append(f"max state chars: {mx} (≤220)")
ok=all(l.split('\t')[cols.index('state')].startswith(('LIVE','RESOLVED','LAPSED','RETIRED','FIRED-UNEXECUTED')) for l in prow); rep.append(f"lead tokens valid: {ok}")
rep.append(f"history entries: {len(hist)}; crc round-trip: "+str(all(zlib.crc32(h.split('\n\n',1)[1].rstrip('\n').encode())==int(re.search(r'entry-crc32: (\d+)',h).group(1)) for h in hist)))
rep.append(f"no 'Prior…:' chain left in last_checked/consumed_by/review_by (regex incl. 'Prior (…):'): "+str(not any(re.search(r'(?i)(?<![A-Za-z])prior(?:\s*\([^)]*\))?\s*:', l.split('\t')[cols.index(c)]) for l in prow for c in ['last_checked','consumed_by','review_by'])))
rep.append(f"bytes: {len(txt.encode())} → {len(body.encode())} (physical cap 54,250; budget 32,550)")
rep.append("rotated-text conservation (every removed Prior-tail appears VERBATIM in the step-2 history file): "+str(all(h.split('\n\n',1)[1].rstrip('\n') in (HDR+''.join(hist)) for h in hist)))
rep.append("trailing newline present: "+str(body.endswith('\n')))
rep.append("DOCKET L251 pointer retained in header: "+str('L251' in body.split('\n')[7]))
rep.append(f"history file: NEW PROME/archive/GATES_STATE_HISTORY_2026-09-03_step2.md, {len((HDR+''.join(hist)).encode())} B (the 2026-08-29 file is untouched at 59,037 B)")
rep.append("DECLARED non-rotation edits in this pass (each VERIFIED at source before the edit): HY-REKILL condition pointer sentence (letter UNCHANGED; supersessions log row added) · HY-REKILL last_checked observation-chain gloss (263 as-of 8/27 = LIQUID grade 8/28 cell; 263 as-of 8/31 = HANDOFF 9/1 officials; 260 as-of 8/28 published 8/31 = HEARTBEAT) · TERRY-007 base-rate gloss (209/499 = 41.9%) + review_by pointer repair · USO135C source re-path (dead → processed/) · REG-T02 consumed_by/review_by → successor pointers (old text archived) · new row GATE-TERRY-ROLL70-EXIT · header §6/§8 stamps")
open(f'{OUTDIR}/INVARIANTS.txt','w').write('\n'.join(rep)+'\n')
d=difflib.unified_diff(txt.split('\n'),body.split('\n'),'GATES.tsv (current)','GATES.tsv (proposed)',lineterm='',n=0)
open(f'{OUTDIR}/DIFF.txt','w',encoding='utf-8').write('\n'.join(d))
print('\n'.join(rep))
