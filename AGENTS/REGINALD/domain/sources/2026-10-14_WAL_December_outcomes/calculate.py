"""Volatility-scale diagnostic beside a separately identified subjective first mark."""
from pathlib import Path
from datetime import date
import json,math

p=Path(__file__).resolve().parent
raw=json.loads((p/'quote-and-chain.json').read_text())
S=raw['quote']['regularMarketPrice']
vol=next(r['impliedVolatility'] for r in raw['puts'] if r['strike']==72.5)
days=(date(2026,12,18)-date(2026,10,14)).days
T=days/365
bounds=[55,65,75,85]
N=lambda z:.5*(1+math.erf(z/math.sqrt(2)))
def diagnostic(v):
    cumulative=[N((math.log(k/S)+.5*v*v*T)/(v*math.sqrt(T))) for k in bounds]
    probs=[cumulative[0]]+[cumulative[i]-cumulative[i-1] for i in range(1,4)]+[1-cumulative[-1]]
    assert abs(sum(probs)-1)<1e-12
    return {'vol':v,'zero_drift_terminal_bin_probabilities':probs,'below65':cumulative[1],'approx_one_sigma_dollar_scale':S*v*math.sqrt(T)}
subjective=[.05,.20,.35,.25,.15]
assert abs(sum(subjective)-1)<1e-12
out={'made':'2026-10-14','terminal_date':'2026-12-18','terminal_object':'WAL regular-session unadjusted vendor close USD;one date,not minimum or any-touch probability','days':days,'quote':raw['quote'],'bins':[{'low_inclusive':lo,'high_exclusive':hi,'subjective_probability':prob} for lo,hi,prob in zip([None]+bounds,bounds+[None],subjective)],'subjective_below65':sum(subjective[:2]),'subjective_at_least65':sum(subjective[2:]),'subjective_at_least75':sum(subjective[3:]),'public_IV_diagnostic':diagnostic(vol),'vol_sensitivity':[diagnostic(v) for v in [.30,.45]],'original_Fidelity65P_basis682_65_for4_expiry_breakeven':65-682.65/400,'status':'First dated REGINALD analytical probability assessment explicitly requested by Will;not canonical WAL probability re-mark or registered/scored fleet prediction','limits':['Subjective branch probabilities are judgment assignments,not an estimated statistical or Bayesian posterior. No historical calibrated distribution or numeric REGINALD prior for same event/horizon.','The zero-drift lognormal model sets arithmetic expected stock return to zero. It is neither risk-neutral pricing nor a physical forecast. No assumed measured risk-free rate,dividend,skew,jump or volatility path.','Near-ATM vendor IV and chain bid/ask timing unverified;American exercise and discrete dividends matter. No calibrated digital/ITM probability inferred from put delta or option quotes.','Subjective25pct below65 is mildly more constructive than zero-drift30pct;operating counterevidence supplies judgment motivation but does not prove unpriced optimism or a5pp posterior update.','A rough20-35pct assessment range for below65 is not a statistical confidence interval or additional probability mass.','No within-bin law is assigned;no exact probability below63.293375,below70 orbelowcurrent spot follows from these bins.','No probability of touching a price,earlier option profit,fill or management action is supplied.']}
(p/'assessment.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'days':days,'subjective':subjective,'sum':sum(subjective),'below65':out['subjective_below65'],'diagnostic':out['public_IV_diagnostic'],'original_cost_expiry_breakeven':out['original_Fidelity65P_basis682_65_for4_expiry_breakeven']}))
