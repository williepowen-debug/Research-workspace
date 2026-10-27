"""One-time authoring of manually reviewed Gmail research cards; no fetch, commit or push."""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, yaml
ROOT=Path(__file__).resolve().parents[4]
DESK=ROOT/'AGENTS/WALTER'
OUT=Path(__file__).resolve().parent
def main():
    cards=json.loads((OUT/'cards-reviewed.json').read_text())
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    day=stamp[:10]; compact=day.replace('-','')
    existing=list((ROOT/'BOARD').glob(f'SIG-W-{compact}-*.md'))
    start=max([int(p.name.split('-')[3]) for p in existing]+[0])+1
    paths=[]; rows=[]
    for offset,c in enumerate(cards):
        sid=f'SIG-W-{compact}-{start+offset:03d}'
        p=ROOT/'BOARD'/f'{sid}-{c["slug"]}.md'
        assert not p.exists(),p
        body=c['body']
        hdr=dict(signal_id=sid,date=day,timestamp=stamp,dispatched=stamp,source='WALTER',
                 origin=c['sources'],domain=c['domain'],cluster=c['cluster'],
                 action=c['action'],info=c['info'],precedence=c.get('precedence','PRIORITY'),
                 signal_type='research',confidence=c['confidence'],
                 confidence_language='confirmed' if c['confidence']>=.90 else 'reports' if c['confidence']>=.70 else 'unconfirmed',
                 entities=c.get('entities',[c['slug']]),resources=1,safety_net='clear',
                 event_window='closed',word_count=len(body.split()),
                 dispatch_note='Will-directed Gmail review; email text and cited source scope only. No owner grade, new study or trade. Publication, delivery and consumption remain separate.')
        if 'case' in c: hdr['case']=c['case']
        if 'role' in c: hdr['signal_role']=c['role']
        p.write_text('---\n'+yaml.safe_dump(hdr,sort_keys=False,allow_unicode=True,default_flow_style=None)+'---\n# '+c['title']+'\n\n'+body+'\n\nEvidence: AGENTS/WALTER/research/2026-10-26_gmail/REVIEW.md\nSources: '+'; '.join(c['sources'])+'\n')
        paths.append(str(p.relative_to(ROOT)))
        with (DESK/'routed/route_log.tsv').open('a') as f:
            csv.writer(f,delimiter='\t',lineterminator='\n').writerow([stamp,sid,'Gmail / issuer and attributed research sources',c['title'],hdr['precedence'],','.join(c['action']),','.join(c['info']),c['confidence']])
        handoffs=[]
        for role,agents in [('ACTION',c['action']),('INFO',c['info'])]:
            for agent in agents:
                if role=='INFO' and agent in {'CARL','RED','PROME','TERRY'}:continue
                q=ROOT/'AGENTS'/agent/'inbox/WALTER'/f'{sid}.md'
                assert not q.exists(),q
                q.parent.mkdir(parents=True,exist_ok=True)
                requested=('Follow the '+agent+' ACTION sentence in the kernel. Existing coverage only; source limits bind.' if role=='ACTION' else 'Awareness only. No recipient-directed research ask.')
                q.write_text(f'# {sid} — {c["title"]}\nBOARD: /{p.relative_to(ROOT)}\nPriority: {hdr["precedence"]}\nRole: {role}\nFrom: WALTER\nDate: {day}\n\n## Kernel\n'+body+'\n\n## Why you got this\nExisting domain responsibility; source-qualified event/context.\n\n## Requested action\n'+requested+'\n\n## Confidence / caveats\n'+str(c['confidence'])+'; the kernel states actual source access and unresolved bases. No owner grades changed.\n\n## Cross-refs\nAGENTS/WALTER/research/2026-10-26_gmail/REVIEW.md\n'+'\n'.join(c['sources'])+'\n\nWritten locally; committed/on-origin delivery and recipient incorporation require separate proof.\n')
                rel=str(q.relative_to(ROOT));paths.append(rel);handoffs.append(rel)
                with (DESK/'routed/delivery_log.tsv').open('a') as f:
                    csv.writer(f,delimiter='\t',lineterminator='\n').writerow([stamp,sid,agent,role,'CODEX',hdr['precedence'],rel,'written_not_delivered_pending_push','Gmail research review; no publication or consumption claim'])
        rows.append(dict(signal_id=sid,slug=c['slug'],board_path=str(p.relative_to(ROOT)),handoffs=handoffs))
    (OUT/'dispatch-summary.json').write_text(json.dumps(dict(timestamp=stamp,signals=len(rows),handoffs=sum(len(r['handoffs']) for r in rows),rows=rows,paths=paths),indent=2)+'\n')
    print(json.dumps(dict(timestamp=stamp,signals=len(rows),first=rows[0]['signal_id'],last=rows[-1]['signal_id'],handoffs=sum(len(r['handoffs']) for r in rows))))
if __name__=='__main__':main()

