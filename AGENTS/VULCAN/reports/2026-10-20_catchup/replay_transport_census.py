from pathlib import Path
import csv,json,re,datetime
R=Path(__file__).resolve().parents[4];A=R/'AGENTS';O=A/'VULCAN/reports/2026-10-20_catchup'
regs=sorted(set(A.glob('*/workbook/CATALYSTS.tsv'))|set(A.glob('*/docket/CATALYSTS.tsv')))
roster=(R/'PROME/ROSTER.md').read_text();names={p.name for p in A.iterdir() if p.is_dir() and re.search(r'\|\s*'+re.escape(p.name)+r'\s*\|',roster)}
records={};errors=[];dates={}
for p in regs:
 try:
  with p.open() as f: rows=list(csv.DictReader((l for l in f if l.strip() and not l.startswith('#')),delimiter='\t'))
  records[p]=rows
  for x in rows:
   day=x.get('date') or x.get('Date') or x.get('trigger_date') or ''
   try:datetime.date.fromisoformat(day)
   except ValueError:continue
   dates.setdefault(p.parts[-3],set()).add(day)
 except Exception as e:errors.append({'path':str(p.relative_to(R)),'error':type(e).__name__})
pairs=[];skipped=[]
for p,rows in records.items():
 owner=p.parts[-3]
 for n,x in enumerate(rows,2):
  recipients=' '.join(str(x.get(c) or '') for c in ['who_cares','agent_domain','routes_to','agents','recipients'])
  targets={name for name in names if re.search(r'(?<![A-Z])'+name+r'(?![A-Z])',recipients)}-{owner}
  day=x.get('date') or x.get('Date') or x.get('trigger_date') or ''
  try:datetime.date.fromisoformat(day)
  except ValueError:
   if targets:skipped.append({'path':str(p.relative_to(R)),'line':n,'date':day})
   continue
  for target in sorted(targets):pairs.append({'publisher':owner,'source':str(p.relative_to(R)),'line':n,'date':day,'recipient':target,'date_carried':day in dates.get(target,set()),'recipient_has_registry':target in dates})
matched=sum(x['date_carried'] for x in pairs)
res={'structured_registers':len(regs),'structured_rows':sum(map(len,records.values())),'recipient_date_pairs':len(pairs),'date_carried':matched,'date_not_carried':len(pairs)-matched,'unparseable_addressed_rows':len(skipped),'errors':errors,'markdown_calendars_not_classifiable':len(list(A.glob('*/CALENDAR.md'))),'method':'READ ONLY. Roster-name token match in explicit recipient columns; strict date parsed. Date-only correspondence, not event identity or delivery/read acknowledgment. Historical and future rows pooled descriptively; missing recipient registry explicit. No per-desk grade. Markdown/prose not pooled.','finding_scope':'The original fleet-wide claim is not established by this structured/date-only census. If most matching dates are present, this weakens the claim of general filing gaps, but says nothing about actual transport; do not declare fleet failure from local VULCAN misses.'}
(O/'transport-census.json').write_text(json.dumps({'summary':res,'pairs':pairs,'unparseable':skipped},indent=2)+'\n')
print(json.dumps(res,indent=2))
