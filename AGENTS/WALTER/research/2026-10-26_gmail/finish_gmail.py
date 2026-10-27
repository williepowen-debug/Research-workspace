"""Persist manually reviewed envelope/content dispositions; no mailbox changes."""
from pathlib import Path
from datetime import datetime, timezone
import csv,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[4]; OUT=Path(__file__).resolve().parent
def main():
    data=json.loads((OUT/'content-map.json').read_text())
    dispatch=json.loads((OUT/'dispatch-summary.json').read_text())
    byslug={r['slug']:r['signal_id'] for r in dispatch['rows']}
    homes={
      (1,1):'trepp-q3-credit-recap',
      (2,1):'sf-office-ai-recovery-context',(2,2):'florida-office-transactions',
      (2,4):'florida-office-transactions',(2,5):'wells-fargo-center-south-note-sale',
      (3,1):'seniors-housing-maturity-cohort',
      (5,1):'jbi-data-center-credit-dispersion',
      (6,1):'insurance-related-party-teaser',(6,2):'insurance-related-party-teaser',
      (7,1):'texas-data-center-permitting-context',(7,2):'texas-data-center-permitting-context',
      (18,1):'pjm-planned-data-maintenance',(19,1):'pjm-planned-data-maintenance'}
    duplicates={
      (9,6):'SIG-W-20261027-019: Pacific Seafood event/date, AP source-read card.',
      (15,1):'SIG-W-20261027-003: original Anthropic sections already source-qualified.',
      (15,5):'SIG-W-20261026-005 and SIG-W-20261027-006: voluntary offer, not realized exits.',
      (15,7):'SIG-W-20261026-001: authorized/launched/future financing amounts distinguished.',
      (15,13):'SIG-W-20261027-008: primary Intel agreement, conditional closing.',
      (16,6):'SIG-W-20261016-036: Two Sigma retreat already on BOARD.'}
    folds={(4,1):'Same episode430 promotion already in emails2/3; podcast itself not played.',
           (13,1):'Existing AI capex/Meta and credit coverage; author framework, no new verified observation or gate.',
           (14,1):'Existing reserve/credit coverage; author liquidity heuristic and crypto flows not independently reproduced.',
           (6,4):'Historical PHL/Golden Gate BOARD20260521-021 and20260928-024; no new October failure established.'}
    noaction={(2,7),(9,7),(9,10),(9,11),(11,2),(11,3),(11,4),(11,5),(11,6),(12,2),(16,5),(16,9),(16,13),(16,15)}
    rows=[]; n=0
    for e in data:
      for j,title in enumerate(e['items'],1):
        n+=1;k=(e['email_n'],j)
        if k in homes: disp='DISPATCH'; ref=byslug[homes[k]]; reason='Full email text reviewed; cited source and verification limits travel on the card.'
        elif k in duplicates: disp='DUP';ref=duplicates[k];reason='Same named event; no headline-only source upgrade inferred.'
        elif k in folds:disp='FOLD';ref=folds[k];reason='Retain context/basis limits; no new verified event or threshold.'
        elif k in noaction:disp='NO-ACTION';ref='REVIEW.md#source-quality';reason='Promotional, keyword collision, technical-price commentary or no concrete relevant event in delivered text.'
        else:disp='NOTE';ref='REVIEW.md#remaining-leads';reason='Qualified pointer only: original linked article/filing/video or chart not reviewed; no actionable event adopted.'
        rows.append(dict(n=n,email_n=e['email_n'],part=j,gmail_id=e['gmail_id'],title=title,disposition=disp,ref=ref,reason=reason))
    with (OUT/'content-dispositions.tsv').open('w') as f:
      w=csv.DictWriter(f,fieldnames=list(rows[0]),delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(rows)
    tool=ROOT/'AGENTS/WALTER/tools/batch_manifest.py'
    for r in rows:
      subprocess.run([sys.executable,str(tool),'--item','BM-20261027-05',str(r['n']),r['disposition'],r['ref']+'; '+r['title']+'; '+r['reason']],cwd=ROOT,check=True,capture_output=True)
    for e in data:
      subprocess.run([sys.executable,str(tool),'--item','BM-20261027-04',str(e['email_n']),'FOLD','Envelope only; expanded to '+str(len(e['items']))+' content items in BM-20261027-05; content-dispositions.tsv'],cwd=ROOT,check=True,capture_output=True)
    for batch in ['BM-20261027-04','BM-20261027-05']:
      p=subprocess.run([sys.executable,str(tool),'--close',batch],cwd=ROOT,check=True,capture_output=True,text=True);print(p.stdout.strip())
    from collections import Counter
    print(json.dumps(dict(content_items=len(rows),dispositions=dict(Counter(r['disposition'] for r in rows)))))
if __name__=='__main__':main()

