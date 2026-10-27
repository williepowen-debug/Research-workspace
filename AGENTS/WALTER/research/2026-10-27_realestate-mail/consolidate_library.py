"""Will-approved one-time source consolidation. Never mutates Gmail or Git.

Private source data and the generated searchable library remain in gitignored
debug/. This script preserves newsletter evidence; it does not grade research.
"""
from pathlib import Path
from html.parser import HTMLParser
from html import unescape,escape
from urllib.parse import urlparse,urlunparse,parse_qsl,urlencode,unquote
from datetime import datetime,timezone
import json,re,base64,collections,hashlib,zipfile

ROOT=Path(__file__).resolve().parents[4]
OLD=ROOT/'AGENTS/WALTER/debug/realestate-2026-10-27'
OUT=ROOT/'AGENTS/WALTER/debug/realestate-library-2026-10-27'
OUT.mkdir(parents=True,exist_ok=True)
HIGHLIGHTS=set(json.loads((OUT/'highlight-ids.json').read_text()))

def read(name):return json.loads(name.read_text())
def prepare():
    old=read(OLD/'plan-final.json');keep={e['id'] for e in old if e['decision']=='RETAIN'}
    rows=[e for e in read(OLD/'clean.json') if e['id'] in keep]
    plan=[]
    for i,e in enumerate(rows,1):
        f=e['from_'];s=e['subject'];kind=None
        if 'globest@' in f:kind='GlobeSt story roundup'
        elif 'connect.media' in f:kind='Connect CRE news digest'
        elif 'nationalmortgagenews' in f:kind='Mortgage industry digest'
        elif 'commercialobserver.com' in f:kind='Commercial Observer issue/interview pointer'
        elif 'trepptalk@' in f and s.startswith('PODCAST'):kind='Trepp podcast episode pointer'
        elif 'info.credaily.com' in f and 'No Cap' in s:kind='CRE Daily podcast episode pointer'
        protected=e['id'] in HIGHLIGHTS or any(l in e['labels'] for l in ['STARRED','CATEGORY_PERSONAL']) or e.get('has_attachment')
        if re.search(r'payment|receipt|invoice|renewal|subscription|unsuccessful',s,re.I):protected=True
        plan.append({'i':i,'id':e['id'],'n':e['n'],'subject':s,'date':e['email_ts'],'sender':f,'kind':kind or 'Substantive analysis/report or protected source','decision':'CONSOLIDATE' if kind and not protected else 'KEEP','protected':bool(protected),'old_labels':e['labels']})
    (OUT/'plan.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
    print(json.dumps({'messages':len(plan),'decision_counts':collections.Counter(e['decision'] for e in plan),'consolidation_types':collections.Counter(e['kind'] for e in plan if e['decision']=='CONSOLIDATE')}))

class Links(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.a=None;self.out=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if tag=='a':
            self.a={'href':d.get('href') or '', 'label':''}
        elif tag=='img' and self.a:self.a['label']+=' '+(d.get('alt') or '')
    def handle_data(self,data):
        if self.a:self.a['label']+=' '+data
    def handle_endtag(self,tag):
        if tag=='a' and self.a:self.out.append(self.a);self.a=None

def normalize_url(raw):
    u=unescape(raw).strip().rstrip('.,;')
    for _ in range(4):
        prev=u
        parsed=urlparse(u)
        if parsed.scheme not in ['http','https']:return None
        q=dict(parse_qsl(parsed.query))
        if 'safelinks.protection.outlook.com' in parsed.netloc and q.get('url'):u=q['url']
        elif 'awstrack.me' in parsed.netloc:
            m=re.search(r'/L\d/([^/]+)/\d/',parsed.path)
            if m:u=unquote(m.group(1))
        elif parsed.netloc.endswith(('law.com','alm.com','globest.com')):
            for part in parsed.path.split('/'):
                if part.startswith('aHR0'):
                    try:u=base64.urlsafe_b64decode(part+'='*(-len(part)%4)).decode();break
                    except (ValueError,UnicodeError):pass
        if u==prev:break
    p=urlparse(u)
    if p.scheme not in ['http','https']:return None
    query=[(k,v) for k,v in parse_qsl(p.query,keep_blank_values=True) if not(k.lower().startswith(('utm_','_hs','mc_')) or k.lower() in ['fbclid','gclid','mkt_tok','trk','user_id'])]
    # Other parameters and all opaque tracking destinations are preserved.
    return urlunparse((p.scheme,p.netloc.lower(),p.path,p.params,urlencode(query),p.fragment))

def text_clean(m):
    # Reuse the reviewed standard-library text extraction; never compare only boilerplate alternatives.
    import sys
    sys.path.insert(0,str(OLD));from prepare import clean
    plain=m.get('plain','')
    if not m.get('html') or len(plain)>200 and not any(x in plain for x in ['Email Management Area','view it in your browser']):return clean({'plain':plain})
    return clean(m)

def source_links(m,subject):
    links=[]
    if m.get('html'):
        h=Links();h.feed(m['html']);links+=h.out
    plain=m.get('plain','').replace('\r\n','\n')
    # HTML carries real headline anchors; its plain alternative often contains
    # only boilerplate or repeats the same destination with a tracking wrapper.
    for match in re.finditer(r'https?://[^\s<>]+',plain if not m.get('html') else ''):
        before=plain[max(0,match.start()-300):match.start()]
        label=before.split('\n\n')[-1].strip().rstrip('([ ')
        label=re.sub(r'https?://\S+','',label)
        links.append({'href':match.group().rstrip(')'), 'label':label})
    out=[];seen=set()
    for l in links:
        url=normalize_url(l['href'])
        if not url:continue
        label=re.sub(r'\s+',' ',unescape(l['label'])).strip()
        path=urlparse(url)
        if any(t in url.lower() for t in ['unsubscribe','emailpreferences','email_preference','email-preference','manage-preferences','myaccount.aspx','privacy-policy','privacy?','/terms','/share?','/refer?','/referral','/subscribe','/subscription','mailto:']):continue
        if any(x in path.netloc for x in ['facebook.com','twitter.com','instagram.com','linkedin.com','x.com','doubleclick.net']):continue
        if any(x in path.netloc for x in ['rs-stripe.','media.beehiiv.com','images.','cdn.','calendly.com','magic.beehiiv.com','sponsy.']):continue
        if path.netloc in ['alm.com','www.alm.com','at.law.com','store.law.com']:continue
        if path.path.rstrip('/') in ['/the-rundown','research-and-insights','trepp-training-solutions-cmbs-cre-certification-programs','treppwire-podcast','contact-rundown']:continue
        if re.search(r'^(?:manage (?:your )?(?:subscription|email)|welcome to trepp|share your cre|more from trepp|log in|sign in|\* [^\[]*\[(?:newsletters|podcast|cre events calendar|market reports|fear & greed))',label,re.I):continue
        if re.search(r'\.(?:png|jpe?g|gif|webp|svg)(?:\?|$)',url,re.I):continue
        if label.casefold() in ['about us','about alm','conferences','creative','resources','research','news','advertise with us','contact','newsletter','manage subscription','central florida','south florida','north florida','gulf coast','florida','florida & gulf coast','new call-to-action','get connect cre news','new york & tri-state','texas','atlanta & southeast','california','chicago & midwest','seattle & northwest','washington dc & mid-atlantic']:continue
        if not path.path.strip('/') and not path.query:continue
        if label.casefold() in ['view in browser','view online','view as web page','manage preferences','email preferences','contact us','advertise','get connect daily','unsubscribe','submit a press release','newsletters','connectcre','learn more about revenuestripe...']:continue
        if m.get('html') and len(label.split())<5 and not re.search(r'episode|podcast|listen|watch|report|research|read more|download|magazine|sit.down',label,re.I):continue
        if not label or len(label)<8 or label.casefold() in ['read more','read more ...','read more →','click here','learn more','watch now','listen now','download now','read now','click to view newsletters links']:
            label=subject+' — linked source'
        label=label[:350]
        key=url
        if key not in seen:out.append({'url':url,'label':label,'original_url':l['href']});seen.add(key)
    return out

def load_bodies():
    bodies={}
    for f in sorted(OLD.glob('bodies-*.json')):
        for m in read(f):bodies[m['id']]=m
    for f in [OLD/'repairs.json',*sorted(OLD.glob('html-repairs-*.json')),OLD/'missing-bodies.json']:
        for m in read(f):bodies[m['id']]=m
    fresh={}
    for f in sorted(OUT.glob('fresh-*.json')):
        for m in read(f):bodies[m['id']]=m;fresh[m['id']]=m
    return bodies,fresh

def build():
    plan=read(OUT/'plan.json');bodies,fresh=load_bodies()
    sources=[];groups={};updated=[];all_links=0
    for row in plan:
        row=dict(row);m=bodies[row['id']]
        if row['decision']=='CONSOLIDATE':
            assert row['id'] in fresh, 'Fetch fresh evidence before consolidation: '+row['id']
            labels=m['labels'];blocked=not 'Label_17' in labels or any(l in labels for l in ['TRASH','SPAM','STARRED','CATEGORY_PERSONAL','Label_26']) or m.get('attachments')
            if blocked:row.update(decision='KEEP',protected=True,kind='Protected or changed since inventory')
            row['before_labels']=labels
        raw={'id':m['id'],'plain':m.get('plain',''),'html':m.get('html',''),'headers':[h for h in m.get('headers',[]) if h['name'].lower() in ['from','date','subject','message-id','x-newsletter']]}
        text=text_clean(raw);links=source_links(raw,row['subject']);all_links+=len(links)
        assert text.strip(), row['id']
        if not links and row['decision']=='CONSOLIDATE':row.update(decision='KEEP',protected=True,kind='Needs source-link extraction review')
        topics=[];t=(row['subject']+' '+text).casefold()
        for topic,rx in [('Florida',r'florida|miami|orlando|tampa|palm beach|boca raton|fort lauderdale|jacksonville'),('Credit & refinancing',r'loan|cm(b|o)s|refinanc|delinquen|maturit|default|foreclos|bank'),('Housing & rent',r'apartment|multifamily|housing|rent|homebuy'),('AI & infrastructure',r'data center|data centre|artificial intelligence|power|industrial|logistics'),('Office & other CRE',r'office|hotel|retail|warehouse|commercial')]:
            if re.search(rx,t):topics.append(topic)
        source={**row,'text':text,'links':links,'topics':topics,'body_sha256':hashlib.sha256(json.dumps(raw,sort_keys=True).encode()).hexdigest(),'raw':raw}
        sources.append(source);updated.append(row)
        for l in links:
            # Destination grouping preserves every original URL and source/date variant.
            opaque=any(x in urlparse(l['url']).netloc for x in ['email.connectcre.com','arz.omeclk.com','link.commercialobserver.com','link.mail.beehiiv.com'])
            # Exact headline grouping is a navigation convenience, not a same-event
            # verdict. Every dated original destination remains in variants.
            k=(urlparse(l['url']).netloc+'::'+l['label'].casefold()) if opaque and len(l['label'].split())>=5 and '— linked source' not in l['label'] else l['url']
            g=groups.setdefault(k,{'url':k,'title':l['label'],'sources':[],'variants':[],'topics':[]})
            if len(l['label'])>len(g['title']) and '— linked source' not in l['label']:g['title']=l['label']
            if row['id'] not in g['sources']:g['sources'].append(row['id'])
            v={'source':row['id'],'date':row['date'],'label':l['label'],'original_url':l['original_url']}
            if v not in g['variants']:g['variants'].append(v)
            g['topics']=sorted(set(g['topics']+topics))
    catalog={'built_at':datetime.now(timezone.utc).isoformat(),'scope':'965 retained newsletter messages from October 27 first-pass inventory','limits':'Source preservation and destination deduplication only; linked articles, podcasts and publisher claims remain unverified unless separately researched. Counts are not signal counts.','sources':sources,'links':list(groups.values())}
    (OUT/'catalog.json').write_text(json.dumps(catalog,ensure_ascii=False))
    (OUT/'plan-reviewed.json').write_text(json.dumps(updated,ensure_ascii=False,indent=2))
    with zipfile.ZipFile(OUT/'source-backup.zip','w',zipfile.ZIP_DEFLATED) as z:
        z.writestr('README.txt','Private newsletter source backup. Plain/HTML email bodies and outbound URLs are evidence, not verified research. The local search index is index.html. No external resources are fetched automatically.\n')
        for s in sources:z.writestr('sources/'+s['id']+'.json',json.dumps(s,ensure_ascii=False))
    # Restore/check archive records before any Gmail mutation.
    with zipfile.ZipFile(OUT/'source-backup.zip') as z:
        assert z.testzip() is None
        for s in sources:
            r=json.loads(z.read('sources/'+s['id']+'.json'))
            assert r==s and hashlib.sha256(json.dumps(r['raw'],sort_keys=True).encode()).hexdigest()==s['body_sha256']
    make_html(catalog)
    proof={'scope_messages':len(plan),'source_records':len(sources),'consolidate':sum(s['decision']=='CONSOLIDATE' for s in sources),'keep':sum(s['decision']=='KEEP' for s in sources),'link_mentions':all_links,'link_groups':len(groups),'zip_records':len(sources),'zip_crc':'PASS','restored_record_equality':'PASS','protected_trash_candidates':sum(s['protected'] for s in sources if s['decision']=='CONSOLIDATE'),'catalog_sha256':hashlib.sha256((OUT/'catalog.json').read_bytes()).hexdigest(),'index_sha256':hashlib.sha256((OUT/'index.html').read_bytes()).hexdigest(),'backup_sha256':hashlib.sha256((OUT/'source-backup.zip').read_bytes()).hexdigest()}
    assert len(plan)==len(sources)==965 and not proof['protected_trash_candidates']
    (OUT/'coverage-proof.json').write_text(json.dumps(proof,indent=2))
    print(json.dumps(proof))

def make_html(c):
    # Avoid raw headers/HTML in the UI. Source HTML remains only in the local JSON/ZIP backup.
    data={**c,'sources':[{k:v for k,v in s.items() if k!='raw'} for s in c['sources']]}
    payload=json.dumps(data,ensure_ascii=False).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
    template='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; base-uri 'none'; form-action 'none'"><title>Real Estate Research Library</title>
<style>body{margin:0;background:#f4f5f2;color:#20302c;font:16px system-ui,sans-serif}main{max-width:1120px;margin:auto;padding:32px 22px}h1{font-size:34px;margin:0 0 10px}p{line-height:1.5}.muted{color:#626d68}header{border-bottom:1px solid #cbd3cc;padding-bottom:20px}.controls{display:flex;gap:12px;flex-wrap:wrap;position:sticky;top:0;background:#f4f5f2;padding:18px 0}input,select,button{font:inherit;padding:10px;border:1px solid #abbab0;border-radius:6px;background:white}input{flex:1;min-width:240px}article{background:white;padding:18px 22px;margin:12px 0;border:1px solid #d4ded5;border-radius:9px}h2{font-size:18px;margin:0 0 9px}a{color:#185f50;overflow-wrap:anywhere}.tag{font-size:12px;background:#e8f0e9;border-radius:5px;padding:3px 7px;display:inline-block;margin:0 6px 5px 0}pre{white-space:pre-wrap;font:14px/1.55 system-ui;overflow-wrap:anywhere}summary{cursor:pointer;color:#285d50;margin:10px 0}.small{font-size:13px}details+details{margin-top:12px}footer{padding:25px 0}.stats{font-weight:600}</style>
<main><header><h1>Real Estate Research Library</h1><p>Searchable newsletter text and source links preserved before Gmail consolidation.</p><p class="stats" id="stats"></p><p class="muted small">These are email records and link groups, not verified signals. Matching destinations or exact headlines are grouped for navigation; dated original links remain available. No external content loads automatically.</p></header>
<div class="controls"><input id="q" aria-label="Search library" placeholder="Search a property, bank, city, phrase or figure"><select id="mode" aria-label="View"><option value="sources">Newsletter text</option><option value="links">Grouped source links</option></select><select id="topic" aria-label="Topic"><option value="">All topics</option></select><select id="scope" aria-label="Mail disposition"><option value="all">All source records</option><option value="CONSOLIDATE">Consolidated from Gmail</option><option value="KEEP">Kept in Gmail</option></select><button id="export">Export link CSV</button></div><p id="count" class="muted"></p><section id="results"></section><button id="more">Show more</button><footer class="muted small">Private local copy · October 27, 2026 · The adjacent catalog.json and source-backup.zip preserve source text, original links, dates and provenance. Source article access and facts require separate verification.</footer></main>
<script>const DATA=__DATA__;const E=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));const byId=Object.fromEntries(DATA.sources.map(s=>[s.id,s]));let limit=100;const $=s=>document.getElementById(s);$('stats').textContent=DATA.sources.length+' email records · '+DATA.links.length+' source-link groups';const topics=[...new Set(DATA.sources.flatMap(s=>s.topics))].sort();for(const t of topics){const o=document.createElement('option');o.value=t;o.textContent=t;$('topic').append(o)}
function tags(ts){return ts.map(t=>'<span class="tag">'+E(t)+'</span>').join('')}
function link(l){return '<a target="_blank" rel="noopener noreferrer" href="'+E(l.url)+'">'+E(l.label??l.title)+'</a>'}
function source(s){return '<article><h2>'+E(s.subject)+'</h2><p class="muted small">'+E(s.date.slice(0,10))+' · '+E(s.sender)+' · '+(s.decision==='CONSOLIDATE'?'Preserved locally; consolidated from Gmail':'Kept in Gmail')+'</p>'+tags(s.topics)+'<details><summary>Read delivered newsletter text (publisher claims unverified)</summary><pre>'+E(s.text)+'</pre></details><details><summary>'+s.links.length+' extracted source links</summary>'+s.links.map(l=>'<p>'+link(l)+'</p>').join('')+'</details></article>'}
function group(g){return '<article><h2>'+link(g)+'</h2>'+tags(g.topics)+'<p class="muted small">'+g.sources.length+' source email(s) · '+E(new URL(g.url).hostname)+'</p><details><summary>Source dates and link variants</summary>'+g.variants.map(v=>'<p class="small">'+E(v.date.slice(0,10))+' · '+E(byId[v.source].subject)+'<br><a target="_blank" rel="noopener noreferrer" href="'+E(v.original_url)+'">'+E(v.label)+'</a></p>').join('')+'</details></article>'}
function render(reset=true){if(reset)limit=100;const words=$('q').value.toLowerCase().trim().split(/\\s+/).filter(Boolean),topic=$('topic').value,scope=$('scope').value,mode=$('mode').value;let rows=mode==='sources'?DATA.sources:DATA.links;rows=rows.filter(r=>{const ss=mode==='sources'?[r]:r.sources.map(id=>byId[id]);if(topic&&!r.topics.includes(topic))return false;if(scope!=='all'&&!ss.some(s=>s.decision===scope))return false;const hay=(mode==='sources'?r.subject+' '+r.sender+' '+r.text:r.title+' '+r.url+' '+r.variants.map(v=>v.label).join(' ')).toLowerCase();return words.every(w=>hay.includes(w))});rows.sort((a,b)=>mode==='sources'?b.date.localeCompare(a.date):b.sources.length-a.sources.length);$('count').textContent=rows.length+' matches · showing '+Math.min(rows.length,limit);$('results').innerHTML=rows.slice(0,limit).map(mode==='sources'?source:group).join('');$('more').hidden=rows.length<=limit}
for(const id of ['q','mode','topic','scope'])$(id).addEventListener(id==='q'?'input':'change',()=>render());$('more').onclick=()=>{limit+=100;render(false)};$('export').onclick=()=>{const quote=v=>'"'+String(v).replaceAll('"','""')+'"';const csv=[['title','url','source_email_count'],...DATA.links.map(l=>[l.title,l.url,l.sources.length])].map(r=>r.map(quote).join(',')).join('\\n');const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([csv],{type:'text/csv;charset=utf-8'}));a.download='real-estate-source-links.csv';a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)};render();</script></html>'''
    (OUT/'index.html').write_text(template.replace('__DATA__',payload))

if __name__=='__main__':
    import sys
    build() if '--build' in sys.argv else prepare()
