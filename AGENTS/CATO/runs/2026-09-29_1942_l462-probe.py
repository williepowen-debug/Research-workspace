"""Independent L462 cases; reuse only the owner's isolated vendor/dashboard harness."""
import importlib.util, json, pathlib, sys
sys.dont_write_bytecode = True
ROOT = pathlib.Path(__file__).resolve().parents[3]
p = ROOT / 'PROME/tools/tests/test_fetch_evening_bar_L462.py'
spec=importlib.util.spec_from_file_location('l462_harness',p); h=importlib.util.module_from_spec(spec); spec.loader.exec_module(h)
h.TODAY='2026-09-29'
t=h.EveningBar(); t.setUp(); d=h.DashboardEveningBar(); d.setUp()
try:
 def show(label,r):
  e=d.entry('BZX26.NYM',**r)
  print(json.dumps({'case':label,**{k:r.get(k) for k in ['price','prev','asof','prev_asof','session','trade_date','change_pct','change_basis','session_basis']},'dashboard_stamp':d.d._date_stamp(e),'dashboard_flags':e['flags'],'dashboard_change':e['change'],'cli_stamp':t.fetch._session_stamp(r,r.get('asof'),'2026-09-29','BZX26.NYM')},ensure_ascii=False))
 def run(label,last_trade,bars=((2026,9,28),(2026,9,29)),**kw):
  sym=t.future(last_trade=last_trade,bars=bars,**kw); r=t.fetch_one(sym); show(label,r); return r
 run('saved 18:03 day control',h.et(2026,9,29,16,59,30),price=102.67,prev=105.28)
 run('saved 19:29 evening shape',h.et(2026,9,29,19,15,41),price=102.94,prev=105.28)
 run('correct relabelled next-date evening',h.et(2026,9,29,19,15,41),bars=((2026,9,28),(2026,9,30)))
 run('two-day-old noon trade under current bar',h.et(2026,9,27,12,0))
 run('zero epoch',0)
 run('boolean epoch',True)
 run('old genuine evening bar must retain age warning',h.et(2026,9,23,20,47),bars=((2026,9,22),(2026,9,23)))
 run('day-gap stale bar',h.et(2026,9,23,12,0),bars=((2026,9,21),(2026,9,23)))
 run('extra Sunday prior bar',h.et(2026,9,28,12,0),bars=((2026,9,27),(2026,9,28)))
 run('Sunday-labelled bar reason',h.et(2026,9,27,19,0),bars=((2026,9,25),(2026,9,27)))
 run('London timezone noon ET',h.et(2026,9,29,12,0),tz='Europe/London')
 run('Pacific timezone 18:30 ET',h.et(2026,9,29,18,30),tz='America/Los_Angeles')
 sym=t.future(last_trade=h.et(2026,9,29,16,59,30),bars=((2026,9,28),(2026,9,29)),price=102.67,prev=105.28)
 t.vendor[sym]['fast_info']['lastPrice']=102.94
 show('fresh evening quote paired with older day metadata',t.fetch_one(sym))
finally:
 d.doCleanups(); t.doCleanups()
