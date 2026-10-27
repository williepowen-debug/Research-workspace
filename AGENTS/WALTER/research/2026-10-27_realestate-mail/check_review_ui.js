// Verify the generated local worklist's actual filter script with its source records.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const base=process.argv[2];
const html=fs.readFileSync(base+'/index.html','utf8');
const plan=JSON.parse(fs.readFileSync(base+'/email-plan.json','utf8'));
const items=JSON.parse(fs.readFileSync(base+'/source-items.json','utf8'));
const controls={q:{value:''},status:{value:'RESEARCH_QUEUE'},count:{}};
for(const c of Object.values(controls))c.addEventListener=()=>{};
const sections=[...new Set(plan.map(p=>p.status))].map(status=>({dataset:{status},articles:plan.filter(p=>p.status===status).map(p=>({dataset:{search:(p.subject+' '+p.reason+' '+items.filter(i=>i.source_email_id===p.id).map(i=>i.text).join('')).toLowerCase()}})),querySelectorAll(){return this.articles;}}));
const ctx={document:{getElementById:id=>controls[id],querySelectorAll:()=>sections}};
vm.createContext(ctx);vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1],ctx);
assert.equal(controls.count.textContent,' 20 emails');
controls.status.value='REFERENCE';ctx.filter();assert.equal(controls.count.textContent,' 28 emails');
controls.status.value='all';ctx.filter();assert.equal(controls.count.textContent,' 294 emails');
controls.q.value='zzzz_no_such_property_zzzz';ctx.filter();assert.equal(controls.count.textContent,' 0 emails');
controls.q.value='Denver';ctx.filter();assert(parseInt(controls.count.textContent)>0);
console.log('PASS: actual UI script; queue/reference/all counts and positive/negative search. DOM stub, not browser rendering.');
