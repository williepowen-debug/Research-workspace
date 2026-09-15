# Independent reviewer cases retained from /tmp; only harness path made relative.
import sys,runpy,unittest,json,hashlib,types
from pathlib import Path
from unittest.mock import patch
source=Path(sys.argv[1]).resolve()
sys.argv=[sys.argv[0],str(source)]
n=runpy.run_path(str(Path(__file__).with_name('2026-09-14_contract-review-counterexamples.py')),run_name='independent_harness')
Base=n['Review'];metadata=n['metadata'];B=n['B']
class NewReview(Base):
 def test_decimal_fraction_timestamp_not_rounded_into_validity(self):
  for side in ['BZ=F','BZU26.NYM']:
   with self.subTest(side=side):
    self.table['BZ=F']['regularMarketTime']=B
    self.table['BZU26.NYM']['regularMarketTime']=B
    self.table[side]['regularMarketTime']='1000000.00000000001'
    r=self.probe()
    print('NEW-FRACTION',side,json.dumps(r,sort_keys=True))
    self.assertTrue(r['verdict'].startswith('REFUSED-'),r)
    self.table[side]['regularMarketTime']=B
 def test_unknown_nonmatch_time_remains_advisory(self):
  self.table['BZV26.NYM']['regularMarketTime']=False
  r=self.probe();self.assertEqual(r['verdict'],'IDENTIFIED');self.assertIn('unknown-candidate-times',r['control'])
 def test_bad_extra_candidate_cannot_poison_valid_control(self):
  self.table['BZX26.NYM']=metadata('CLX26.NYM',100)
  r=self.fetch.contract_probe('BZ',horizon=3)
  self.assertEqual(r['verdict'],'IDENTIFIED');self.assertIn('metadata-symbol-mismatch',r['dropped']['BZX26.NYM'])
 def test_malformed_candidate_container_is_dropped(self):
  self.table['BZX26.NYM']=['not','metadata']
  r=self.fetch.contract_probe('BZ',horizon=3)
  self.assertEqual(r['verdict'],'IDENTIFIED');self.assertIn('BZX26.NYM',r['dropped'])
 def test_negative_zero_and_symbol_normalization(self):
  for price in [-100,0]:
   self.table['BZ=F']=metadata(' bz=f ',price)
   self.table['BZU26.NYM']=metadata(' bzu26.nym ',price)
   self.assertEqual(self.probe()['verdict'],'IDENTIFIED')
 def test_invalid_matched_time_types(self):
  for value in [True,0,-1,1.5,[],{},'nan','inf','not-a-date']:
   with self.subTest(value=value):
    self.table['BZU26.NYM']['regularMarketTime']=value
    self.assertTrue(self.probe()['verdict'].startswith('REFUSED-'))
 def test_cache_partial_refresh_can_fail_old_success_and_recover(self):
  clock=[10000]
  self.stack.enter_context(patch.object(self.fetch.time,'time',side_effect=lambda:clock[0]))
  original=sys.modules['yfinance'].Ticker;owner=self;phase=[0]
  class DynamicTicker(original):
   @property
   def fast_info(self):
    if (phase[0]==0 and self.symbol=='BAD') or (phase[0]==1 and self.symbol=='BZ=F'):
     raise RuntimeError('new fixture failure')
    return dict(lastPrice=owner.quote,previousClose=99,lastVolume=10)
  self.table['BAD']=metadata('BAD',100)
  self.stack.enter_context(patch.object(sys.modules['yfinance'],'Ticker',DynamicTicker))
  a=self.fetch.price_fetch(['BZ=F','BAD']);self.assertIn('error',a['BAD'])
  phase[0]=1;clock[0]+=1;self.quote=110
  b=self.fetch.price_fetch(['BZ=F','BAD']);self.assertIn('error',b['BZ=F']);self.assertEqual(b['BAD']['price'],110)
  phase[0]=2;clock[0]+=1;self.quote=120
  c=self.fetch.price_fetch(['BZ=F','BAD']);self.assertEqual(c['BZ=F']['price'],120);self.assertEqual(c['BAD']['price'],120)
  calls=len(self.calls);clock[0]+=1;self.quote=130
  d=self.fetch.price_fetch(['BZ=F','BAD']);self.assertEqual(d,c);self.assertEqual(len(self.calls),calls)
  print('NEW-CACHE',json.dumps(dict(first=a,second=b,recovery=c,complete_hit=d,calls=self.calls),sort_keys=True))
print('REVIEWED-SHA256',hashlib.sha256(source.read_bytes()).hexdigest())
suite=unittest.TestSuite(NewReview(name) for name in NewReview.__dict__ if name.startswith('test_'))
r=unittest.TextTestRunner(verbosity=2).run(suite)
sys.exit(not r.wasSuccessful())
