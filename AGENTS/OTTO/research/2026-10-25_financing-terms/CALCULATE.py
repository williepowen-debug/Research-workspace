from pathlib import Path
from decimal import Decimal as D
import json,csv,io,hashlib,gzip
out=Path('AGENTS/OTTO/research/2026-10-25_financing-terms')
rows=[
('Exeter','EART 2026-3','2026-06-16','FWP/prospectus dated','A-3','S&P AAA / Moody Aaa',267.470,1.38,'I-CRV',59,4.512,4.470,'1.50% ABS to 5% call','eart3_fwp'),
('Exeter','EART 2026-4','2026-08-26','FWP/underwriting agreement dated','A-3','S&P AAA / Moody Aaa',246.630,1.37,'I-CRV',52,4.611,4.560,'1.50% ABS to 5% call','eart4_fwp'),
('Exeter','EART 2026-3','2026-06-16','FWP/prospectus dated','D','S&P BBB / Moody Baa3',194.310,3.59,'I-CRV',140,5.505,5.440,'1.50% ABS to 5% call','eart3_fwp'),
('Exeter','EART 2026-4','2026-08-26','FWP/underwriting agreement dated','D','S&P BBB / Moody Baa3',159.560,3.64,'I-CRV',140,5.710,5.640,'1.50% ABS to 5% call','eart4_fwp'),
('Bridgecrest','BLAST 2026-3','2026-07-21','prospectus/underwriting date; FWP filed July22','A-3','S&P AAA / DBRS AAA',134.720,1.24,'I-Curve',57,4.692,4.640,'1.75% ABS to 10% call','blast3_fwp'),
('Bridgecrest','BLAST 2026-4','2026-10-08','prospectus/underwriting date; FWP filed October9','A-3','S&P AAA / DBRS AAA',119.330,1.32,'I-CRV',62,5.155,5.100,'1.75% ABS to 10% call','blast4_fwp'),
('Bridgecrest','BLAST 2026-3','2026-07-21','prospectus/underwriting date; FWP filed July22','D','S&P BBB / DBRS BBB',107.250,3.24,'I-Curve',135,5.660,5.590,'1.75% ABS to 10% call','blast3_fwp'),
('Bridgecrest','BLAST 2026-4','2026-10-08','prospectus/underwriting date; FWP filed October9','D','S&P BBB / DBRS BBB',114.710,3.27,'I-CRV',165,6.556,6.460,'1.75% ABS to 10% call','blast4_fwp'),
('CPS','CPS 2026-C','2026-07-22','closing date; pricing date undisclosed','D','S&P BBB / DBRS BBB',81.530,3.21,'UNDISCLOSED',None,None,5.720,'10% pool call; original/remaining OC targets differ','cps_c_sec_release'),
('CPS','CPS 2026-D','2026-10-21','closing date; pricing date undisclosed','D','Moody Baa2 / DBRS BBB',71.120,3.31,'UNDISCLOSED',None,None,6.550,'10% pool call; original/remaining OC targets differ','cps_d_sec_release')]
fields=['issuer','deal','date','date_basis','tranche','ratings','size_millions','modeled_wal_years','benchmark_as_printed','spread_bp','yield_pct','coupon_pct','prepayment_call_basis','source_key']
b=io.StringIO();w=csv.writer(b,delimiter='\t',lineterminator='\n');w.writerow(fields);w.writerows(rows);(out/'PRICING.tsv').write_text(b.getvalue())
pairs=[]
for a,z in [(0,1),(2,3),(4,5),(6,7),(8,9)]:
 x,y=rows[a],rows[z];r={'issuer':x[0],'tranche':x[4],'earlier':x[1],'later':y[1],'coupon_change_bp':str((D(str(y[11]))-D(str(x[11])))*100)}
 if x[9] is not None:
  r['spread_change_bp']=y[9]-x[9];r['yield_change_bp']=str((D(str(y[10]))-D(str(x[10])))*100);r['yield_less_spread_residual_change_bp']=str(D(r['yield_change_bp'])-D(r['spread_change_bp']))
 r['interpretation']='Descriptive new-issue comparison; no causal attribution or current secondary quote. CPS coupons are not yields/spreads.';pairs.append(r)
cps={
'C':{'amount_millions':['317.300','99.900','113.110','81.530','105.040'],'coupon_pct':['4.52','4.84','5.05','5.72','7.65'],'publisher_weighted_coupon_pct':'5.90'},
'D':{'amount_millions':['356.340','111.470','118.090','71.120','110.830'],'coupon_pct':['5.14','5.59','6.01','6.55','8.56'],'publisher_weighted_coupon_pct':'6.68'}}
for r in cps.values():
 am=list(map(D,r['amount_millions']));co=list(map(D,r['coupon_pct']));r['listed_amount_sum_millions']=str(sum(am));r['table_implied_principal_weighted_coupon_pct']=str(sum(a*c for a,c in zip(am,co))/sum(am));r['publisher_less_table_bp']=str((D(r['publisher_weighted_coupon_pct'])-D(r['table_implied_principal_weighted_coupon_pct']))*100)
calc={'pairs':pairs,'cps_weighted_coupon_reconciliation':cps,'cps_table_implied_change_bp':str((D(cps['D']['table_implied_principal_weighted_coupon_pct'])-D(cps['C']['table_implied_principal_weighted_coupon_pct']))*100),'limits':'CPS issuer prose and table disagree; no claim about actual all-in effective borrowing cost. Benchmark residual is algebra, not an independently observed rate series.'}
(out/'CALCULATIONS.json').write_text(json.dumps(calc,indent=2));print(json.dumps(calc,indent=2))
manifest=json.loads((out/'sources.json').read_text());bad=[]
for k,r in manifest.items():
 if 'path' in r and hashlib.sha256(gzip.decompress(Path(r['path']).read_bytes())).hexdigest()!=r['raw_sha256']:bad.append(k)
assert not bad
(out/'VERIFY.json').write_text(json.dumps({'hash_checked':sum('path' in r for r in manifest.values()),'bad':bad,'pricing_rows':len(rows),'pairs':len(pairs),'checks':'All 10 selected rows cross-read at source. Five pairs preserve issuer/rating/WAL/date/benchmark basis. CPS arithmetic uses listed amounts/rates and retains prose mismatch.'},indent=2))
