"""Recompute conditional reference forecasts from supplied derived states, offline.
Does not reconstruct states from underlying prices or yields or activate a forecast.
"""
from pathlib import Path
import ast, hashlib, json, shutil
import numpy as np
import pandas as pd
p=Path(__file__).resolve().parent
s=pd.read_csv(p/'base_rate_state_series_thru_20261030.csv',index_col=0,parse_dates=True)
assert len(s)==5059 and s.index.is_unique and s.index.is_monotonic_increasing
assert list(s.columns)==['corr','vol','beta','brate'] and np.isfinite(s.to_numpy()).all()
assert str(s.index[-1].date())=='2026-10-30'
j=pd.concat([s,s.shift(-63).add_suffix('_f')],axis=1).dropna()
j['C1']=np.where(j.corr_f<=.863,'persist',np.where(j.vol_f<.20,'calm_norm','stress_norm'))
j['C3']=np.where(j.brate_f<-.03,'neg',np.where(j.brate_f>.03,'pos','zero'))
def dist(mask,col,labels):
 x=j.loc[mask,col]; c=x.value_counts()
 return {'n':len(x),'counts':{k:int(c.get(k,0)) for k in labels},'probabilities':{k:float(c.get(k,0)/len(x)) for k in labels}}
r={'scope':'Reproduced from supplied derived state CSV, not from raw prices/yields','rows':len(s),'start':str(s.index[0].date()),'end':str(s.index[-1].date()),'last_row':s.iloc[-1].to_dict(),'forward_pairs':len(j),'last_conditioning_date':str(j.index[-1].date()),'C1':dist(j['corr']<.863,'C1',['persist','calm_norm','stress_norm']),'C2':{'n':int((j.beta<.5).sum()),'successes':int((j.loc[j.beta<.5,'beta_f']>=.8).sum()),'probability':float((j.loc[j.beta<.5,'beta_f']>=.8).mean())},'C3':dist(j.brate<-.03,'C3',['neg','zero','pos'])}
code=(p/'resolver_chat_copy.py').read_text();tree=ast.parse(code)
pdf=(p/'combined_pdf_text.txt').read_text();import textwrap
part=textwrap.dedent(pdf[pdf.index('        def stats('):pdf.index('        def main():')])
chat_stats=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='stats')
r['stats_ast_matches_pdf']=ast.dump(chat_stats,include_attributes=False)==ast.dump(ast.parse(part).body[0],include_attributes=False)
r['chat_copy_sha256']=hashlib.sha256(code.encode()).hexdigest()
r['matches_claimed_resolver_hash']=r['chat_copy_sha256']=='b98e22f29d3f49a7bd9add75021ba4621d139e49d4d1ba707861eaf45dc9fae3'
(p/'state_series_checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
