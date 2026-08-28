#!/usr/bin/env python3
"""
Australian wheat x ONI base rate — AEOLUS C2, built 2026-08-27 (Will-directed).

REPRODUCES: KB-AEO-101 / 102 / 103.

INPUTS (both primary, neither committed — re-pull before use):
  psd_grains_pulses.csv  <- unzip of
      https://apps.fas.usda.gov/psdonline/downloads/psd_grains_pulses_csv.zip   (no auth)
  oni.txt                <- https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt

RUN FROM a directory holding both files.

READ BEFORE TRUSTING ANY NUMBER THIS PRINTS
-------------------------------------------
1. The PRIMARY block below was pre-specified BEFORE any result was computed. Do not
   re-pick the anchor season after seeing the answers -- the sensitivity rows exist to
   show robustness, NOT to select a winner.
2. The linear detrend is reported for continuity ONLY. It MISFITS the post-2020 yield
   regime by ~0.41 MT/ha, which is LARGER than the El Nino effect (~0.22), and it made
   strong El Ninos read as near-harmless. PREFER the regime-aware normalization.
   -> A trend that misfits by more than the effect size cannot measure the effect.
3. The most recent Market_Year is a PRE-HARVEST FORECAST (Australian harvest is Nov-Dec).
   USDA's own August-vintage forecast error is NOT yet base-rated -- see KB-103.
"""
import csv, statistics as st

# ---------- PRE-SPECIFIED BEFORE LOOKING AT ANY RESULT ----------
# 1. ANCHOR SEASON = ASO of the same calendar year as PSD Market_Year.
#    Australian wheat is an austral WINTER crop: sown Apr-Jun, yield set largely by
#    Aug-Oct spring rain / grain fill, harvested Nov-Dec. ASO is the physiological window.
#    Other seasons are reported as SENSITIVITY ONLY and are NOT used to select the answer.
# 2. PRIMARY VARIABLE = YIELD, detrended. Production conflates area (price/policy) with weather.
# 3. DETREND = residual from a linear fit on year (no free parameters);
#    a centered 9-yr moving-mean % deviation is reported as a robustness check.
# 4. CLASSIFICATION = CPC convention on the anchor season: >= +0.5 El Nino, <= -0.5 La Nina.
PRIMARY_SEASON='ASO'
# ----------------------------------------------------------------

psd={}
for r in csv.DictReader(open('psd_grains_pulses.csv',encoding='utf-8-sig')):
    if r.get('Country_Name')=='Australia' and r.get('Commodity_Description')=='Wheat':
        psd.setdefault(r['Attribute_Description'],{})[int(r['Market_Year'])]=float(r['Value'])
yld=psd['Yield']; prod=psd['Production']; area=psd['Area Harvested']

oni={}
for line in open('oni.txt').read().split('\n')[1:]:
    p=line.split()
    if len(p)==4: oni[(p[0],int(p[1]))]=float(p[3])

def lin_resid(pairs):
    xs=[p[0] for p in pairs]; ys=[p[1] for p in pairs]; n=len(xs)
    mx,my=st.mean(xs),st.mean(ys)
    b=sum((x-mx)*(y-my) for x,y in pairs)/sum((x-mx)**2 for x in xs)
    a=my-b*mx
    return {x: y-(a+b*x) for x,y in pairs}, b

def corr(a,b):
    n=len(a); ma,mb=st.mean(a),st.mean(b)
    sa,sb=st.pstdev(a),st.pstdev(b)
    if sa==0 or sb==0: return float('nan')
    return sum((x-ma)*(y-mb) for x,y in zip(a,b))/(n*sa*sb)

years=[y for y in sorted(yld) if (PRIMARY_SEASON,y) in oni and y<=2025]
pairs=[(y,yld[y]) for y in years]
resid,slope=lin_resid(pairs)
print(f"AUSTRALIAN WHEAT vs ONI — PSD Online x CPC oni.ascii.txt")
print(f"anchor season {PRIMARY_SEASON} (pre-specified) | years {min(years)}-{max(years)} | n={len(years)}")
print(f"yield trend = {slope:+.4f} MT/ha per year  (technology trend removed before any test)")
print()

for lbl,seas in [('PRIMARY  '+PRIMARY_SEASON,PRIMARY_SEASON)]+[('sens '+s,s) for s in ['JJA','JAS','SON','OND','NDJ','MJJ']]:
    ys=[y for y in years if (seas,y) in oni]
    o=[oni[(seas,y)] for y in ys]; r=[resid[y] for y in ys]
    print(f"{lbl:<12} n={len(ys):<3} corr(ONI, detrended yield) = {corr(o,r):+.3f}")
print()

o=[oni[(PRIMARY_SEASON,y)] for y in years]; r=[resid[y] for y in years]
mean_y=st.mean([yld[y] for y in years])
def bucket(v): return 'El Nino' if v>=0.5 else ('La Nina' if v<=-0.5 else 'Neutral')
groups={}
for y in years: groups.setdefault(bucket(oni[(PRIMARY_SEASON,y)]),[]).append(y)
print(f"CONDITIONAL MEANS — detrended yield residual (MT/ha), and as % of the {mean_y:.2f} MT/ha series mean")
for g in ['El Nino','Neutral','La Nina']:
    gs=groups.get(g,[]); v=[resid[y] for y in gs]
    print(f"  {g:<8} n={len(gs):<3} mean {st.mean(v):+.3f} MT/ha ({100*st.mean(v)/mean_y:+5.1f}%)   median {st.median(v):+.3f}")
print()
print("STRONG El Nino only (ONI ASO >= +1.5):")
strong=[y for y in years if oni[(PRIMARY_SEASON,y)]>=1.5]
print(f"  n={len(strong)}  years {strong}")
if strong:
    v=[resid[y] for y in strong]
    print(f"  mean residual {st.mean(v):+.3f} MT/ha ({100*st.mean(v)/mean_y:+.1f}%)  median {st.median(v):+.3f}")
    for y in sorted(strong):
        print(f"    {y}  ONI {oni[(PRIMARY_SEASON,y)]:+.2f}  yield {yld[y]:.2f}  resid {resid[y]:+.3f}  prod {prod[y]:,.0f} kMT")

print()
print("="*78)
print("WHERE DOES 2026 SIT?")
# what does the 2026 PSD forecast imply for yield residual?
y26=yld.get(2026); p26=prod.get(2026); a26=area.get(2026)
xs=[p[0] for p in pairs]; ys=[p[1] for p in pairs]
mx,my=st.mean(xs),st.mean(ys)
b=sum((x-mx)*(yy-my) for x,yy in pairs)/sum((x-mx)**2 for x in xs); a=my-b*mx
trend26=a+b*2026
print(f"  PSD 2026 (forecast vintage): production {p26:,.0f} kMT | area {a26:,.0f} kHA | yield {y26:.2f} MT/ha")
print(f"  trend yield at 2026 = {trend26:.2f} MT/ha  ->  implied residual {y26-trend26:+.3f} MT/ha ({100*(y26-trend26)/mean_y:+.1f}% of series mean)")
print(f"  El Nino conditional mean residual = {st.mean([resid[y] for y in groups['El Nino']]):+.3f} ({100*st.mean([resid[y] for y in groups['El Nino']])/mean_y:+.1f}%)")
print()
print("  ONI trajectory check — did MJJ ~+1.4 become ASO >= +1.5 historically?")
cand=[y for y in range(1950,2026) if ('MJJ',y) in oni and 1.0<=oni[('MJJ',y)]<=1.8]
for y in cand:
    print(f"    {y}  MJJ {oni[('MJJ',y)]:+.2f} -> ASO {oni.get(('ASO',y),float('nan')):+.2f} -> NDJ {oni.get(('NDJ',y),float('nan')):+.2f}")
print(f"    2026  MJJ {oni[('MJJ',2026)]:+.2f} -> ASO NOT YET PUBLISHED")
print()
print("="*78)
print("PRODUCTION YoY BASE RATE — how unusual is USDA's -22.2%?")
yy=sorted([y for y in prod if y-1 in prod and y<=2025])
ch={y: 100*(prod[y]/prod[y-1]-1) for y in yy}
alln=[ch[y] for y in yy]
print(f"  ALL YEARS      n={len(alln)}  median {st.median(alln):+.1f}%  {sum(1 for v in alln if v<=-22.2)} of {len(alln)} were <= -22.2% ({100*sum(1 for v in alln if v<=-22.2)/len(alln):.0f}%)")
for g in ['El Nino','Neutral','La Nina']:
    v=[ch[y] for y in groups[g] if y in ch]
    print(f"  {g:<14} n={len(v):<3} median {st.median(v):+6.1f}%  mean {st.mean(v):+6.1f}%  {sum(1 for x in v if x<=-22.2)} of {len(v)} were <= -22.2% ({100*sum(1 for x in v if x<=-22.2)/len(v):.0f}%)")
