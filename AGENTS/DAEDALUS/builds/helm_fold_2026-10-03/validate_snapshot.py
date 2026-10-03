from pathlib import Path
import sys, json,hashlib,subprocess,datetime as dt,re,contextlib,io
from unittest.mock import patch
root=Path('/tmp/daedalus-helm-q7ivlt_b/repo');sys.path.insert(0,str(root/'PROME/tools'))
import fleet_dashboard as fd,will_handbook as wh,_baseline_fleet_dashboard as oldfd,_baseline_will_handbook as oldwh,measure
meta=json.loads(Path('/tmp/daedalus-helm-snapshot.json').read_text())
state=['PROME/state/brief_snapshot.json','PROME/state/brief_changes.jsonl','PROME/tools/dashboard_state.json','PROME/tools/dashboard_build.json']
# Neighbour suites may change their ISOLATED receipt; restore pinned state before probe.
for n in state:
 p=root/n
 data=subprocess.run(['git','show',meta['source_head']+':'+n],cwd=root,capture_output=True)
 if data.returncode==0:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data.stdout)
def hashes():return {n:hashlib.sha256((root/n).read_bytes()).hexdigest() if (root/n).exists() else None for n in state}
class Frozen(dt.datetime):
 @classmethod
 def now(cls,tz=None):
  t=cls(2026,10,3,22,30,tzinfo=dt.timezone.utc)
  return t.astimezone(tz) if tz else t.replace(tzinfo=None)
before=hashes();out={};rendered={}
with patch.object(dt,'datetime',Frozen),patch.object(fd.agent_freshness.time,'time',return_value=Frozen.now().timestamp()):
 for tag,mod in [('before',oldwh),('after',wh)]:
  mod.ALERTS.clear();dest=root.parent/(tag+'.html')
  with patch.object(sys,'argv',['helm','--no-feed','-o',str(dest)]),patch.object(wh.wb,'_persist_state',side_effect=AssertionError('feed write')),patch.object(fd,'write_build_receipt',side_effect=AssertionError('receipt write')),patch.object(fd,'build',side_effect=AssertionError('dashboard build invoked')):
   with contextlib.redirect_stdout(io.StringIO()):rc=mod.main()
  out[tag]={'rc':rc,'alerts':mod.ALERTS.copy(),'measure':measure.measure(str(dest)),'max_line_bytes':max(map(len,dest.read_bytes().splitlines()))}
  rendered[tag]=dest.read_text()
 out['state_before']=before;out['state_after']=hashes();assert before==hashes()
 fleets=[];snaps=[];pages=[]
 for mod in (oldfd,fd):
  real=mod.make_snapshot
  def capture(*args,**kw):fleets.append(args[4]);return real(*args,**kw)
  with patch.object(mod,'run_rc',return_value=0),patch.object(mod,'make_snapshot',side_effect=capture):
   page,snap=mod.build(dt.date(2026,10,3),'2026-10-03 18:30')
  snaps.append(snap);pages.append(page)
 assert fleets[0]==fleets[1], 'fleet extraction changed rows'
 assert snaps[0]==snaps[1], 'snapshot contract changed'
 # Entire donor page must be identical except the approved retirement notice.
 notice='  <p>RETIRED as a published page 2026-10-02 (WQ-372) — <a href="https://claude.ai/code/artifact/ee088d08-bf26-48ab-bad2-7ee9155da12a">the Helm</a> carries this; built for the gate only.</p>\n'
 assert pages[0]==pages[1].replace(notice,''), 'unintended donor page change'
 out['fleet_rows']=fleets[1];out['fleet_count']=len(fleets[1]);out['donor_snapshot_identical']=True;out['donor_page_only_notice_changed']=True
 diag=[];g=fd.parse_gates(dt.date(2026,10,3),diagnostics=diag)
 assert not diag,diag
 out['gate_counts']={kind:sum(r['kind']==kind for r in g) for kind in ('live','crit','resolved')}
 assert oldfd.parse_gates(dt.date(2026,10,3))==g
 for name,mod in [('before',oldwh),('after',wh)]:
  text=rendered[name];manual=text[text.index("<div id='tab-manual'"):text.index("<footer")]
  out[name]['manual_sha256']=hashlib.sha256(manual.encode()).hexdigest()
 assert out['before']['manual_sha256']==out['after']['manual_sha256']
 assert out['before']['alerts']==out['after']['alerts']
 assert out['after']['measure']['bytes']<250000
 links=re.findall(r'href=[\'"]docket.html#([^\'"]+)',rendered['after']);docket=(root.parent/'docket.html').read_text()
 assert all(re.search(r'id=[\'"]'+re.escape(x)+r'[\'"]',docket) for x in links)
 out['local_docket_links_resolved']=len(links)
 out['header_deck_link_preserved']=wh.DECK_URL in rendered['after'];assert out['header_deck_link_preserved']
 out['hosted_and_standard_gate']='OWNER-DEPENDENT; not run. Donor equivalence probe stubs run_rc; does not certify full gate.'
Path('/tmp/daedalus-helm-validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='fleet_rows'},indent=2))
