"""One-time approved mailbox workflow; preserves sources, never mutates Gmail/Git."""
from pathlib import Path
from datetime import datetime,timezone
from html import escape
import json,re,hashlib,collections,csv
ROOT=Path(__file__).resolve().parents[4]
LIB=ROOT/'AGENTS/WALTER/debug/realestate-library-2026-10-27'
OUT=ROOT/'AGENTS/WALTER/debug/realestate-review-2026-10-27'
OUT.mkdir(parents=True,exist_ok=True)

QUEUE={
"Leasing in Manhattan's Office Market Stays Strong":'Reconcile reported OZK takeout and original payoff evidence; preserve office-market counterevidence.',
'IOS attracts Wall Street':'Check industrial outdoor-storage rent and AI staging-demand definitions against original data.',
'CBRE: Deals Stall Into 2027':'Primary earnings checked; distinguish sales revenue from property transaction volume. Call-derived 2027 forecast remains unverified.',
'UDR, Apollo to Form $2Bln Apartment Venture':'Primary terms checked; October 29 closing is conditional, equity is not yet demonstrated funded.',
'Toil and Trouble':'Separate author commentary/anecdotes from original housing, builder and AI evidence. Full paid continuation not delivered.',
'Chicago Office Loans Face Lease Rollover Risk Ahead of Maturity':'Lease-risk balances are whole loans, not expected losses; preserve two named distress cases with source/event-date limits.',
'Deeper Dive Shows Outlier Impacting Credit Metrics':'Read with October 16 source: a seasoned loan pool reverses the aggregate lending-quality inference.',
'Trouble Brewing in Denver Multifamily Sector?':'Primary watchlist figures checked; 98% of watchlisted balance is current, not defaulted.',
'Nearly 1 in 4 Loans Can’t Refi':'Primary model checked; loan count differs from balance, future refinancing coupons differ from existing fixed-rate resets.',
'Blackstone Goes AI-In':'Separate current holdings, financing, pipeline and commentary; verify original exposure perimeter before adoption.',
'Power decides where to build':'Verify survey population and proposed-versus-delivered electricity capacity before using as an investment signal.',
'Sun Belt Starts Fall 75% From Peak':'Reconcile region, starts/completions and peak-versus-year-over-year bases with housing records.',
'How Higher Rates Squeezed a Property':'Natick refinancing already mentioned on BOARD; examine added coupon/cash-in/coverage details without treating a refinance as default.',
'Only the South is cutting rents':'Check rental-platform population and observation dates against existing rent/concession series.',
'Uncomfortable Truths':'Separate the Lennar/Millrose reported transaction from commentary; verify originals and prior builder coverage.',
'Life Insurers Are Taking Bigger Risks':'Check insurance/CRE allocation and risk denominators against existing insurer coverage.',
'On the Road Again':'Retain original author analysis for primary-source review; do not infer nationwide conditions from a field trip.',
'The Gift That Keeps on Giving':'Retain original author analysis; identify claims and source gaps before adoption.',
"What We Don't Know Matters":'Retain original author analysis and distinguish missing evidence from observed deterioration.',
'Under the Covers':'Retain original author analysis for source checking; commentary is not a validated research finding.'}
REFERENCE_OCT={"It's Alive! San Francisco's Office Market Rises From the Dead",'Seniors Housing Faces $2.24B of Hard Maturities Through 2027','Concessions Flash Back to 2010','Hurricane Isaias Damages Estimated at $3Bln','Multifamily Delinquency Concentrated in NY, San Francisco','CMBS Lenders Really Like Trophy Offices','Domestic CMBS Market Keeps Cooking','Delinquent Multifamily Loans: Where Are They?','CMBS Lenders Stay Conservative This Year'}

def main():
    catalog=json.loads((LIB/'catalog.json').read_text());sources=[s for s in catalog['sources'] if s['decision']=='KEEP'];assert len(sources)==294
    rows=[];units=[];groups={};protected=set(json.loads((LIB/'highlight-ids.json').read_text()))
    for i,s in enumerate(sources,1):
        subject=s['subject'];report='trepptalk@' in s['sender']
        if subject.startswith('Your payment receipt '):status='REFILE_RECEIPT';reason='Personal account receipt, not research; preserve in Receipts.'
        elif report:status='REFERENCE';reason='Dated report or data-series source. Keep history and access/model limits; not a new verified signal.'
        elif subject in QUEUE:status='RESEARCH_QUEUE';reason=QUEUE[subject]
        elif subject in REFERENCE_OCT:status='REFERENCE';reason='Dated context or prior source-qualified coverage; retain cohort/definition limits.'
        else:status='EXTRACTED_TO_LIBRARY';reason='Delivered content split into local source items and preserved in the library. Article claims remain attributed/unverified unless separately checked; container consolidated.'
        row={'i':i,'id':s['id'],'subject':subject,'date':s['date'],'status':status,'reason':reason,'source_body_sha256':s['body_sha256'],'highlight':s['id'] in protected}
        if row['highlight']:assert status in ['REFERENCE','RESEARCH_QUEUE']
        text=s['text'];points=[0]+[m.start() for m in re.finditer(r'(?m)^(?:➯ |\* \[|#{1,3} )',text) if m.start()>0]+[len(text)]
        parts=[text[a:b] for a,b in zip(points,points[1:])];assert ''.join(parts)==text
        refs=[]
        for j,part in enumerate(parts,1):
            uid=f'EMAIL-{i:03d}-ITEM-{j:03d}';norm=re.sub(r'\s+',' ',part).strip();h=hashlib.sha256(norm.encode()).hexdigest()
            first=next((l.strip() for l in part.splitlines() if l.strip()),subject)
            u={'item_id':uid,'source_email_id':s['id'],'source_subject':subject,'published_at':s['date'],'item_title':first[:240],'text':part,'content_hash':h,'mail_status':status,'research_status':'UNVERIFIED_PUBLISHER_CONTENT','amounts_mentioned':list(dict.fromkeys(re.findall(r'\$[\d,.]+(?:\s?(?:billion|million|trillion|B|M|T))?',part))),'percentages_mentioned':list(dict.fromkeys(re.findall(r'\d+(?:\.\d+)?%',part)))}
            units.append(u);groups.setdefault(h,[]).append(uid);refs.append(uid)
        row['item_ids']=refs;rows.append(row)
    (OUT/'email-plan.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    (OUT/'source-items.json').write_text(json.dumps(units,ensure_ascii=False))
    (OUT/'duplicate-item-groups.json').write_text(json.dumps([v for v in groups.values() if len(v)>1],indent=2))
    # All source items survive; repeated blocks retain source/date references.
    byid={s['id']:s for s in sources}
    for r in rows:assert ''.join(u['text'] for u in units if u['source_email_id']==r['id'])==byid[r['id']]['text']
    links={s['id']:s['links'] for s in sources}
    sections=[]
    for status,title in [('RESEARCH_QUEUE','Research queue'),('REFERENCE','Reference'),('EXTRACTED_TO_LIBRARY','Consolidated source notes'),('REFILE_RECEIPT','Account record')]:
        cards=[]
        for r in rows:
            if r['status']!=status:continue
            items=[u for u in units if u['source_email_id']==r['id']]
            body=''.join('<details><summary>'+escape(u['item_title'])+'</summary><pre>'+escape(u['text'])+'</pre></details>' for u in items)
            ls=''.join('<p><a target="_blank" rel="noopener noreferrer" href="'+escape(l['url'],quote=True)+'">'+escape(l['label'])+'</a></p>' for l in links[r['id']])
            cards.append('<article data-search="'+escape((r['subject']+' '+r['reason']+' '+byid[r['id']]['text']).casefold(),quote=True)+'"><h3>'+escape(r['subject'])+'</h3><p>'+escape(r['date'][:10])+' · '+escape(r['reason'])+'</p>'+body+'<details><summary>Source links</summary>'+ls+'</details></article>')
        sections.append('<section data-status="'+status+'"><h2>'+title+' ('+str(len(cards))+')</h2>'+''.join(cards)+'</section>')
    html='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; base-uri 'none'"><title>Real Estate Review Queue</title><style>body{font:16px system-ui;background:#f3f5f2;color:#24362e;margin:0}main{max-width:1100px;margin:auto;padding:28px}h1{margin-bottom:8px}input,select{font:inherit;padding:10px;border:1px solid #a9b6ab;border-radius:5px}input{width:58%}.bar{position:sticky;top:0;background:#f3f5f2;padding:16px 0}article{border:1px solid #cdd8ce;border-radius:8px;background:white;padding:15px 20px;margin:12px 0}h3{margin:0}pre{white-space:pre-wrap;font:14px/1.5 system-ui;overflow-wrap:anywhere}a{color:#17634d;overflow-wrap:anywhere}summary{cursor:pointer;padding:7px 0}p{line-height:1.5;color:#4b5b50}</style><main><h1>Real Estate Review Queue</h1><p>Email processing states and delivered source notes. Item counts are navigation units, not verified claims or signals. The original library and ZIP preserve the complete captured sources.</p><div class="bar"><input id="q" placeholder="Search a property, lender, figure or phrase" aria-label="Search"><select id="status" aria-label="Status"><option value="RESEARCH_QUEUE">Research queue</option><option value="REFERENCE">Reference</option><option value="EXTRACTED_TO_LIBRARY">Consolidated notes</option><option value="all">All records</option></select><span id="count"></span></div>__SECTIONS__<p>Original source library: <a href="../realestate-library-2026-10-27/index.html">open library</a>. Primary-source review is separate from preservation. Received email text remains publisher-attributed; owner grades are unchanged.</p></main><script>function filter(){const words=document.getElementById('q').value.toLowerCase().trim().split(/\\s+/).filter(Boolean),state=document.getElementById('status').value;let count=0;for(const s of document.querySelectorAll('section')){s.hidden=state!=='all'&&s.dataset.status!==state;for(const a of s.querySelectorAll('article')){a.hidden=!words.every(w=>a.dataset.search.includes(w));if(!s.hidden&&!a.hidden)count++}}document.getElementById('count').textContent=' '+count+' emails'}for(const id of ['q','status'])document.getElementById(id).addEventListener(id==='q'?'input':'change',filter);filter();</script></html>'''
    (OUT/'index.html').write_text(html.replace('__SECTIONS__',''.join(sections)))
    proof={'email_records':len(rows),'source_items':len(units),'duplicate_source_blocks':sum(len(v)-1 for v in groups.values()),'source_text_reconstruction':'PASS for all 294 emails','decisions':dict(collections.Counter(r['status'] for r in rows)),'source_items_sha256':hashlib.sha256((OUT/'source-items.json').read_bytes()).hexdigest(),'index_sha256':hashlib.sha256((OUT/'index.html').read_bytes()).hexdigest(),'limits':'Partitioning and exact-block deduplication preserve source text; they do not establish novelty, source truth or owner integration.'}
    (OUT/'coverage-proof.json').write_text(json.dumps(proof,indent=2));print(json.dumps(proof))
if __name__=='__main__':main()
