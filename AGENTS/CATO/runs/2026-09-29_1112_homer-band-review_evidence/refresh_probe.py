"""Isolated CATO counterexamples; run from any directory. Prints observed results; edits no owner files."""
import csv, io, json, subprocess, tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[4]
src=root/'AGENTS/CATO/runs/2026-09-29_1112_homer-band-review_evidence/apartment_list_top100_2026_09.csv'
script=root/'AGENTS/HOMER/tools/rent_breadth.py'
with src.open() as f:
 reader=csv.DictReader(f); fields=reader.fieldnames; data=list(reader)
results={}
def run(label,cols,rows):
 with tempfile.TemporaryDirectory(prefix='cato_homer_') as d:
  p=Path(d)/'fixture.csv'
  with p.open('w') as f:
   w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(rows)
  r=subprocess.run(['python3',str(script),str(p)],text=True,capture_output=True)
  lines=r.stdout.splitlines()
  results[label]={'returncode':r.returncode,'september':[l for l in lines if l.startswith('2026-09')],'latest':lines[-1:] ,'stderr':r.stderr}
run('baseline',fields,data)
run('missing_city',fields,data[:-1])
blank=[dict(r) for r in data];blank[0]['2025_09']=''
run('missing_cell',fields,blank)
zero=[dict(r) for r in data];zero[0]['2025_09']='0'
run('zero_cell',fields,zero)
run('missing_prior_september_column',[f for f in fields if f!='2025_09'],data)
reorder=fields.copy();a,b=reorder.index('2025_08'),reorder.index('2025_09');reorder[a],reorder[b]=reorder[b],reorder[a]
run('swapped_august_september_columns',reorder,data)
run('missing_unrelated_prior_july_column',[f for f in fields if f!='2025_07'],data)
reorder=fields.copy();a,b=reorder.index('2026_08'),reorder.index('2026_09');reorder[a],reorder[b]=reorder[b],reorder[a]
run('swapped_final_columns',reorder,data)
for count in [20,21,40,41,55,56]:
 rows=[dict(r) for r in data]
 for i,r in enumerate(rows):r['2025_09']='1000';r['2026_09']='900' if i<count else '1100'
 run(f'cutoff_{count}',fields,rows)
print(json.dumps(results,indent=2))
