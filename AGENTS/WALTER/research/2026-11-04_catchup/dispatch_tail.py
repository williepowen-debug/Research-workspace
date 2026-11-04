from dispatch import *
D.clear()
items=json.loads((OUT/'intake-items.json').read_text())
groups=[('Apple-source-lead','Apple earnings headline retains source and vintage gaps','VULCAN','ZHAO','AI_INFRA_CAPEX','AI_CAPEX',[211]),('UK-consumer-source-leads','UK company and consumer-policy headlines need dated source reconciliation','HANS','CARL LABOR','CONSUMER_STAGFLATION','EUROPE_MACRO',[215,217,219,220]),('AGOA-source-lead','Reported AGOA removal needs the dated legal instrument','HAWK','MIDAS','MISC','GEOPOL_NON_ENERGY',[228]),('Labadee-source-leads','Reported Labadee suspension extension needs operator confirmation','CRUISE','','MISC','CONSUMER_CREDIT',[1,10,15])]
for slug,title,action,info,cluster,domain,nums in groups:
 refs='\n'.join(f'- Intake {i}, {items[i-1]["date"]}: {items[i-1]["title"]}. [Locator]({items[i-1]["link"]})' for i in nums)
 body=f'''Residual source leads from the November 2 intake snapshot. The titles below are read; original bodies and primary records remain unread. None of the implied amounts, effective dates, headcounts or mechanisms is certified. Publication date is not event date; overlap with existing owner work remains unresolved. UK employment is not US payroll; proposed company measures are not realized effects. Trade-policy headlines do not establish a signed effective instrument or a metals supply disruption.

ACTION {action}: reconcile with existing authorized work at the next normal review, obtain decisive original evidence before changing any grade, and discard stale or duplicated stories. No new study, monitor or desk launch is commissioned. INFO recipients receive context only.

{refs}'''
 add(slug,title,action,info,cluster,domain,action,body,'RESEARCH-INTAKE intake-items.json; exact positions and links above',confidence=.4)
write(D,65)
