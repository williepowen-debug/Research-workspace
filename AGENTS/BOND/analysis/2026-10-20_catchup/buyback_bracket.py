"""Recompute the prior dig with the now-published October15 closing curve; preserve original inputs/output."""
from pathlib import Path
H=Path(__file__).resolve().parent
old=H.parent/'2026-10-15_buyback-dig'/'dig.py'
s=old.read_text()
s=s.replace("Path('/home/willi/Research-workspace/AGENTS/BOND/analysis/2026-10-15_post-PPI/raw')","Path("+repr(str(H/'raw'))+")")
s=s.replace("open(H/'derived.json','w')","open(Path("+repr(str(H/'buyback-bracket.json'))+"),'w')")
exec(compile(s,str(old),'exec'),{'__file__':str(old),'__name__':'__main__'})
