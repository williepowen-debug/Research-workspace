#!/usr/bin/env python3
"""Closeout rotation bundle, 2026-10-03 PM (prome-ed, post-/clear sitting) — four boot-read surfaces at rotate tier
(READ_CAP rule 5: rotate verbatim until <70% of the 32,550 B budget; `read_cap_check.py --agent PROME --require-manifest`).
Moves are VERBATIM with a block crc32 per cut (zlib.crc32 over the exact bytes between the markers, exclusive of the
marker lines and their newlines). `--plan` writes PROME/plans/2026-10-03_closeout-rotations-PLAN.md and touches no live
file; `--apply` writes the archives and the live files. NEW texts (the resume block, the STATUS stamp) are filled by the
closeout before --plan; placeholders make --apply refuse.
BOOT.md (76%) is NOT in this bundle: a manual, so its stamp-chain + fleet-memory pointerization is a canon pass of its own."""
import sys, re, zlib, os, subprocess, datetime
ROOT = subprocess.run(["git","rev-parse","--show-toplevel"],capture_output=True,text=True).stdout.strip()
P = lambda *a: os.path.join(ROOT,*a)
TODAY = "2026-10-03"
def B(s): return len(s.encode())
def crc(s): return zlib.crc32(s.encode())
def block(name, body, archive):
    archive.append(f"## {name}\nblock-crc32: {crc(body)} · bytes: {B(body)} · rotated {TODAY}\n<!-- {name.split(' —')[0]} BEGIN -->\n{body}\n<!-- {name.split(' —')[0]} END -->\n")
NEW = {}  # filled at closeout: 'SCRATCH_NEXT', 'STATUS_STAMP', 'STATUS_WQ299_CURRENT', 'AD_STAMP', 'HANDOFF_ENTRY', 'HANDOFF_HEADER_SENTENCE'
def main(mode):
    plan=[f"# PLAN — closeout rotation bundle, {TODAY} PM (`prome-ed` post-`/clear` sitting)", "",
          "**Rule:** READ_CAP rule 5 — rotate verbatim until under 70% of the 32,550 B budget (22,785 B). Every cut is archived byte-exact with a block crc32; the new text carries every still-live obligation or names the row that does. Sizes = `PROME/tools/measure.py` after apply, never this file.", ""]
    arch={}; out={}
    # ---------- HANDOFF: three oldest entries → archive; header paragraph rewritten ----------
    h=open(P('PROME/HANDOFF.md'),encoding='utf-8').read(); parts=re.split(r'(?m)^(?=## )',h)
    keep=[parts[0]]; moved=[]
    for p in parts[1:]:
        if p.startswith(('## October 2 — `prome-96`','## October 1 night — `prome-e4`','## October 1 evening — `prome-2f`')): moved.append(p)
        else: keep.append(p)
    assert len(moved)==3, [m[:40] for m in moved]
    A=[f"# HANDOFF rotation — {TODAY} `prome-ed` PM closeout: three entries + the header paragraph, VERBATIM","Each block's crc32 is zlib.crc32 over the exact bytes between its markers (UTF-8, exclusive of the marker lines and their newlines) — recompute, never trust. The accounts of these sittings are `memory/2026-10-01.md` and `memory/2026-10-02.md`.",""]
    hdr_lines=parts[0].split('\n'); hdr_para=[l for l in hdr_lines if l.startswith('**Resume:**')][0]
    block("HEADER — the Resume/rotation paragraph as it stood", hdr_para, A)
    for i,m in enumerate(moved,1): block(f"ENTRY {i} — {m.split(chr(10),1)[0][3:90]}", m.rstrip('\n'), A)
    arch['PROME/archive/HANDOFF_ROTATED_2026-10-03_prome-ed-pm.md']="\n".join(A)
    new_hdr=NEW.get('HANDOFF_HEADER_SENTENCE','<<HANDOFF_HEADER_SENTENCE>>')
    new_entry=NEW.get('HANDOFF_ENTRY','<<HANDOFF_ENTRY>>')
    out['PROME/HANDOFF.md']=parts[0].replace(hdr_para,new_hdr)+new_entry.rstrip('\n')+"\n\n"+"".join(keep[1:])
    plan.append(f"## HANDOFF — {B(h)} B → rotate three entries ({' · '.join(m.split(chr(10),1)[0][3:60] for m in moved)}; {sum(B(m) for m in moved)} B) + the {B(hdr_para)} B header paragraph → `PROME/archive/HANDOFF_ROTATED_2026-10-03_prome-ed-pm.md`; add this sitting's entry; header paragraph → one sentence + `ls PROME/archive/HANDOFF_ROTATED_*`.\nNEW header sentence:\n> {new_hdr}\n\nNEW entry:\n> {new_entry[:3000]}\n")
    # ---------- WILL_QUEUE: RECENTLY DONE rows done before 9/26 → roll-off archive ----------
    t=open(P('PROME/WILL_QUEUE.md'),encoding='utf-8').read()
    head,done=t.split('## RECENTLY DONE',1)
    lines=done.split('\n'); cut=datetime.date(2026,9,26); old=[]; kept=[]
    for l in lines:
        if l.startswith('| **'):
            cells=[c.strip() for c in l.strip().strip('|').split(' | ')]
            mm=re.search(r'(2026-\d\d-\d\d)',cells[1] if len(cells)>1 else '')
            if mm and datetime.date.fromisoformat(mm.group(1))<cut: old.append(l); continue
        kept.append(l)
    assert len(old)==31, len(old)
    idx=" · ".join(f"**{re.match(r'\| \*\*(\d+)',l).group(1)}** · {re.search(r'(2026-\d\d-\d\d)',l).group(1)[5:]} · {crc(l)}" for l in old)
    W=[f"# WILL_QUEUE RECENTLY-DONE roll-off — {TODAY} (DESKTOP, `prome-ed` post-`/clear` sitting, closeout)",
       f"**Rolled off per W5** (Done 9/20–9/25, ≥7 days at roll on {TODAY}; every row carried its durable anchor at write; the boot gate had flagged the overdue roll-off as an advisory). {len(old)} verbatim rows below in their WILL_QUEUE order; crc32 (UTF-8, no trailing newline) per row line in the index. Rows here are HISTORY; `PROME/WILL_QUEUE.md` is canonical for anything still open.","",
       f"**Index (row · Done · crc32):** {idx}","","| Item | Done | Record |","|---|---|---|"]+old
    arch['PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md']="\n".join(W)+"\n"
    summary=f"*Rolled off {TODAY} (closeout, `prome-ed` PM): {len(old)} rows done 9/20–9/25 → `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md` (per-row crc32 in its index).*"
    new_done="\n".join(kept).rstrip('\n')+"\n\n"+summary+"\n"
    out['PROME/WILL_QUEUE.md']=head+'## RECENTLY DONE'+new_done
    plan.append(f"## WILL_QUEUE — {B(t)} B → {len(old)} RECENTLY DONE rows done before 2026-09-26 ({sum(B(l)+1 for l in old)} B) → `PROME/archive/WILL_QUEUE_ROWS_2026-10-03_rolloff.md`; a one-line roll-off summary appended to § RECENTLY DONE. OPEN untouched.\n")
    # ---------- STATUS: line 2 stamp + the WQ-299 row's prior sitting statements → STATUS_HISTORY ----------
    S=open(P('PROME/STATUS.md'),encoding='utf-8').read().split('\n'); assert S[1].startswith('**Updated:**')
    wq=[i for i,l in enumerate(S) if l.startswith('| **WQ-299 RULED 9/26')]; assert len(wq)==1; wi=wq[0]
    cells=S[wi].split(' | '); state=cells[-1]
    # the current statement = from '**2026-10-03' if present else keep whole; prior statements = everything before the last bold-dated statement
    m=list(re.finditer(r'\*\*2026-\d\d-\d\d [^*]*closeout[^*]*\*\*',state))
    new_stamp=NEW.get('STATUS_STAMP','<<STATUS_STAMP>>'); new_299=NEW.get('STATUS_WQ299_CURRENT','<<STATUS_WQ299_CURRENT>>')
    H=[f"## {TODAY} — rotated at the `prome-ed` PM Standard closeout (byte flow: STATUS at 94% of budget at the 16:08 boot gate): the whole `Updated:` stamp line (the 12:2x Standard stamp + Light addenda 4/5 + the prome-dc and prome-96 priors) and the WQ-299 row's prior sitting statements, verbatim (crc32 per block over the exact bytes between the markers, UTF-8, zlib.crc32).",""]
    block(f"{TODAY} prome-ed-pm STAMP", S[1], H); block(f"{TODAY} prome-ed-pm WQ299-STATE", state.rstrip(' |'), H)
    hist=open(P('PROME/archive/STATUS_HISTORY.md'),encoding='utf-8').read().rstrip('\n')+"\n\n"+"\n".join(H)+"\n"
    arch['PROME/archive/STATUS_HISTORY.md']=hist
    S2=list(S); S2[1]=new_stamp; cells[-1]=new_299+(' |' if state.rstrip().endswith('|') else ''); S2[wi]=' | '.join(cells)
    out['PROME/STATUS.md']="\n".join(S2)
    plan.append(f"## STATUS — {sum(B(l)+1 for l in S)} B → L2 stamp ({B(S[1])} B) and the WQ-299 row's state cell ({B(state)} B) → `PROME/archive/STATUS_HISTORY.md` § {TODAY}; replaced by this sitting's stamp and the current statement.\nNEW stamp:\n> {new_stamp[:2500]}\n\nNEW WQ-299 state:\n> {new_299[:1500]}\n")
    # ---------- ACTIVE_DECISIONS: TERRY row 'Earlier:' tail + DEWEY row (terminal) + L2 stamp ----------
    Al=open(P('PROME/ACTIVE_DECISIONS.md'),encoding='utf-8').read().split('\n'); assert Al[1].startswith('**Updated:**')
    ti=[i for i,l in enumerate(Al) if l.startswith('| **TERRY duration/TLT-put fire-card TRY-FIRE-004**')][0]
    tc=Al[ti].split(' | '); nx=[i for i,c in enumerate(tc) if c.startswith('**10/3 (2026-10-03')][0]
    nxt=tc[nx]; k=nxt.index('Earlier:'); tail=nxt[k:]; headpart=nxt[:k].rstrip()
    di=[i for i,l in enumerate(Al) if l.startswith('| **DEWEY deep-research batch 2')][0]
    R=[f"# ACTIVE_DECISIONS rotation — {TODAY} (byte-flow, PROME `prome-ed` PM Standard closeout; trigger = rotate-tier at the 16:08 boot gate)",
       "**Manifest:** the TERRY 004 row's Next-cell `Earlier:` tail (pre-rewrite text verbatim below) · the whole DEWEY batch row, made TERMINAL (SUPERSEDED: entitlements settled by WQ-300 on 2026-09-26 — free tier approved, paid lines declined; the drain = its DOCKET rows) · the prior header stamp. `block-crc32` is zlib.crc32 over the exact bytes between the markers — recompute, never trust. Standing guards of the TERRY row are byte-identical before and after.",""]
    block(f"{TODAY} TERRY-NEXT-TAIL", tail, R); block(f"{TODAY} DEWEY-ROW", Al[di], R); block(f"{TODAY} AD-STAMP", Al[1], R)
    arch['PROME/archive/ACTIVE_DECISIONS_ROTATION_2026-10-03.md']="\n".join(R)
    tc[nx]=headpart+f" Earlier narrative (TERRY's cards on file · the 10/1 book · BOND's kill letter · WQ-213 VLO) → `PROME/archive/ACTIVE_DECISIONS_ROTATION_{TODAY}.md`."
    A2=list(Al); A2[ti]=' | '.join(tc)
    A2[di]=f"| **DEWEY deep-research batch 2 + entitlements + batch 3** | `SUPERSEDED {TODAY}` — entitlements settled by WQ-300 (Will 2026-09-26: free-tier rating actions APPROVED, paid lines DECLINED); the batch-3 drain lives on DEWEY's DOCKET rows; row verbatim → `PROME/archive/ACTIVE_DECISIONS_ROTATION_{TODAY}.md` | DEWEY (its DOCKET rows) | none here | — | the archive + `PROME/WILL_QUEUE.md` RECENTLY DONE row 300 |"
    A2[1]=NEW.get('AD_STAMP','<<AD_STAMP>>')
    out['PROME/ACTIVE_DECISIONS.md']="\n".join(A2)
    plan.append(f"## ACTIVE_DECISIONS — {sum(B(l)+1 for l in Al)} B → TERRY Next-cell tail ({B(tail)} B) + DEWEY row ({B(Al[di])} B, made terminal SUPERSEDED by WQ-300) + prior stamp ({B(Al[1])} B) → `PROME/archive/ACTIVE_DECISIONS_ROTATION_{TODAY}.md`.\nNEW DEWEY row:\n> {A2[di]}\n\nNEW stamp:\n> {A2[1][:1200]}\n")
    # ---------- SCRATCH: five blocks → archive; ★ NEXT rewritten ----------
    sc=open(P('PROME/SCRATCH.md'),encoding='utf-8').read()
    nb=sc.index('## ★ NEXT SESSION — START HERE'); ne=sc.index('## ⚠️ CAUTIONS FOR THE FRESH SESSION')
    nextblk=sc[nb:ne]
    C=[f"# SCRATCH rotation — {TODAY} `prome-ed` PM Standard closeout: the ★ NEXT block as it stood (every sub-block), VERBATIM","Each block's crc32 is zlib.crc32 over the exact bytes between its markers (UTF-8, exclusive of the marker lines and their newlines) — recompute, never trust. Still-live obligations were CARRIED into the new ★ NEXT or named by their DOCKET/WQ rows there.",""]
    block(f"{TODAY} NEXT-BLOCK", nextblk.rstrip('\n'), C); block(f"{TODAY} SCRATCH-STAMP", sc.split('\n')[1], C)
    arch['PROME/archive/SCRATCH_ROTATED_2026-10-03_prome-ed-pm.md']="\n".join(C)
    new_next=NEW.get('SCRATCH_NEXT','<<SCRATCH_NEXT>>'); new_sstamp=NEW.get('SCRATCH_STAMP','<<SCRATCH_STAMP>>')
    sl=sc.split('\n'); sl[1]=new_sstamp; sc2="\n".join(sl); nb2=sc2.index('## ★ NEXT SESSION — START HERE'); ne2=sc2.index('## ⚠️ CAUTIONS FOR THE FRESH SESSION')
    out['PROME/SCRATCH.md']=sc2[:nb2]+new_next.rstrip('\n')+"\n\n"+sc2[ne2:]
    plan.append(f"## SCRATCH — {B(sc)} B → the whole ★ NEXT block ({B(nextblk)} B) + the stamp line → `PROME/archive/SCRATCH_ROTATED_2026-10-03_prome-ed-pm.md`; rewritten as this sitting's resume (DOCKET-VIEW and Pending-Will blocks untouched — generated).\nNEW ★ NEXT:\n> {new_next[:6000]}\n")
    plan.append("## Projected sizes after apply (plan-time arithmetic; cite `measure.py` after apply)\n"+"\n".join(f"- `{k}`: {B(v)} B" for k,v in out.items() if k!='PROME/WILL_QUEUE.md')+f"\n- `PROME/WILL_QUEUE.md`: {B(out['PROME/WILL_QUEUE.md'])} B (not cap-bearing; the roll-off is W5 hygiene)\n")
    plan.append("## Invariants the reads check\n1. Every archived block equals the bytes that left the live file (crc recomputes).\n2. No live obligation lost: each owed item in the rotated SCRATCH/HANDOFF text is carried, named by a DOCKET/WQ/GATES row, or stated done with its evidence.\n3. The TERRY row's standing guards are byte-identical; the DEWEY row's terminal state names its authority (WQ-300).\n4. New statements are true at their sources; no figure a reader can recompute is restated as current; every clock came from `date`.\n5. A stranger can resume from the new SCRATCH alone.\n")
    if mode=='--plan':
        open(P('PROME/plans/2026-10-03_closeout-rotations-PLAN.md'),'w',encoding='utf-8').write("\n".join(plan)); print("plan written; projected:",{k:B(v) for k,v in out.items()})
    elif mode=='--apply':
        for k,v in out.items(): assert '<<' not in v, f"placeholder left in {k}"
        for k,v in arch.items():
            if k.endswith('STATUS_HISTORY.md'): pass
            else: assert not os.path.exists(P(k)), k
            open(P(k),'w',encoding='utf-8').write(v)
        for k,v in out.items(): open(P(k),'w',encoding='utf-8').write(v)
        print("applied", {k:B(v) for k,v in out.items()})
if __name__=='__main__': main(sys.argv[1])
