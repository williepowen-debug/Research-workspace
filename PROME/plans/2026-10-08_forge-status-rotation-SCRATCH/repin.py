# Re-pin FORGE/position_management.tsv rows sourced to FORGE/STATUS.md after a reviewed byte change.
import sys, csv, hashlib, pathlib, subprocess
ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
tsv=ROOT/'FORGE/position_management.tsv'; raw=tsv.read_text(encoding='utf-8'); assert '\r' not in raw and raw.endswith('\n')
sha=hashlib.sha256((ROOT/'FORGE/STATUS.md').read_bytes()).hexdigest()
lines=raw.split('\n')[:-1]; hdr=lines[0].split('\t'); si=hdr.index('source'); shi=hdr.index('source_sha256'); ci=hdr.index('checked')
n=0
for k in range(1,len(lines)):
    c=lines[k].split('\t'); assert len(c)==len(hdr),(k,len(c))
    if 'FORGE/STATUS.md' in c[si]:
        print(f'  L{k+1} {c[1]} {c[2]} {c[3]}: {c[shi][:12]} -> {sha[:12]} (checked {c[ci]} -> 2026-10-08)')
        c[shi]=sha; c[ci]='2026-10-08'; lines[k]='\t'.join(c); n+=1
tsv.write_text('\n'.join(lines)+'\n',encoding='utf-8'); print('re-pinned', n, 'rows to', sha[:16])
