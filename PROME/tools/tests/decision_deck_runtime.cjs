// Execute the production UI/store scripts in an isolated DOM + database stub.
// No browser, network, live artifacts, or external packages are involved.
const assert = require('node:assert/strict');
const vm = require('node:vm');
const source = JSON.parse(require('node:fs').readFileSync(0, 'utf8'));
function element(id='', dataset={}) {
  const classes = new Set();
  return {id, dataset, hidden:false, disabled:false, textContent:'', listeners:{}, attrs:{},
    classList:{add(...xs){xs.forEach(x=>classes.add(x));}, remove(...xs){xs.forEach(x=>classes.delete(x));},
      contains(x){return classes.has(x);}, toggle(x,on){on ? classes.add(x) : classes.delete(x);}},
    setAttribute(k,v){this.attrs[k]=v;}, addEventListener(k,fn){this.listeners[k]=fn;},
    querySelector(){return null;}, querySelectorAll(){return [];}, closest(){return null;}};
}
function ui(view, ids, saved, hash='') {
  const panels=ids.map(x=>element(x));
  const tabs=ids.map(x=>element('tab-'+x,{for:x}));
  const card=element('wq-4'), toggle=element();
  card.closest=()=>panels[panels.length-1]; card.querySelector=()=>toggle;
  const storage=new Map([['deck.tab.'+view,saved],['deck.min.wq-4','1']]);
  const ctx={document:{body:{dataset:{view}},
      querySelectorAll(s){return {'.tab':tabs,'.panel':panels,'.card':[card],'.lnk[data-all]':[]}[s] || [];},
      getElementById(id){return id===card.id?card:panels.find(p=>p.id===id);}},
    localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)},location:{hash},
    window:{claude:{use(){throw Error('Reference UI must never open a store');}}}};
  vm.runInNewContext(source.ui, ctx);
  return {panels,tabs,card,toggle,storage};
}
let u=ui('reference',['decided','flight','docket'],'owed');
assert.equal(u.panels[0].hidden,false); assert.equal(u.panels[1].hidden,true);
assert.equal(u.toggle.attrs['aria-expanded'],'false');
u.toggle.listeners.click(); assert.equal(u.toggle.attrs['aria-expanded'],'true');
u.tabs[1].listeners.click(); assert.equal(u.panels[1].hidden,false);
assert.equal(u.storage.get('deck.tab.reference'),'flight');
u=ui('owed',['owed','key'],'decided','#missing'); assert.equal(u.panels[0].hidden,false);
u=ui('reference',['decided','flight','docket'],'decided','#wq-4'); assert.equal(u.panels[2].hidden,false);
u=ui('reference',['decided','flight','docket'],'flight','#bad[selector'); assert.equal(u.panels[1].hidden,false);
u=ui('owed',['owed','key'],null); assert.equal(u.panels[0].hidden,false);

async function rulingTest() {
  const store=element('store'), toast=element('toast'), card=element('wq-1'), state=element();
  const note={value:'  useful note  '};
  const buttons=['APPROVE','DECLINE'].map(v=>element('',{v}));
  const wrap=element('',{wq:'1'}); wrap.querySelectorAll=()=>buttons;
  buttons.forEach(b=>b.closest=()=>wrap); card.querySelector=()=>state;
  let snapshot, writes=[], rejectWrite=false;
  const db={collection(name){assert.equal(name,'rulings');return {
    onSnapshot(fn){snapshot=fn;},
    doc(id){return {set(payload){writes.push({id,payload});return rejectWrite?Promise.reject({code:'DENIED'}):Promise.resolve();}}}
  };}};
  const ctx={document:{body:{dataset:{build:'fixture-build'}},querySelectorAll:()=>buttons,
      getElementById:id=>({'store':store,'toast':toast,'wq-1':card,'note-1':note}[id])},
    setTimeout:()=>0,clearTimeout:()=>{},window:{}};
  // Offline fallback disables ruling controls without throwing.
  vm.runInNewContext(source.rulings,ctx); assert(buttons.every(b=>b.disabled));
  assert.match(store.textContent,/Reading only/);
  // Fake native runtime: same timestamp for two changes of mind, unique event IDs.
  let random=0;
  ctx.window={claude:{use(name){assert.equal(name,'db');return Promise.resolve(db);}}};
  ctx.Math=Object.create(Math);ctx.Math.random=()=>{random+=0.1;return random;};
  ctx.Date=class extends Date {constructor(...args){super(...(args.length?args:['2026-09-15T12:00:00.123Z']));}};
  vm.runInNewContext(source.rulings,ctx);
  await new Promise(setImmediate);
  assert(buttons.every(b=>!b.disabled));
  snapshot({docs:[{data:()=>({wq:'1',verdict:'DECLINE',ts:'2026-09-15T12:01:00Z',consumed:true})},
                  {data:()=>({wq:'1',verdict:'APPROVE',ts:'2026-09-15T12:00:00Z'})}]});
  assert.match(state.textContent,/DECLINE.*picked up/);
  buttons[0].listeners.click();assert(buttons.every(b=>b.disabled));
  await new Promise(setImmediate);
  buttons[1].listeners.click();await new Promise(setImmediate);
  assert.equal(writes.length,2);assert.notEqual(writes[0].id,writes[1].id);
  assert.equal(writes[0].payload.ts,writes[1].payload.ts);
  assert.deepEqual(JSON.parse(JSON.stringify(writes[1].payload)),{
    wq:'1',verdict:'DECLINE',note:'useful note',ts:'2026-09-15T12:00:00.123Z',build:'fixture-build',consumed:false,source:'decision-deck'});
  rejectWrite=true;buttons[0].listeners.click();await new Promise(setImmediate);
  assert.match(state.textContent,/Not recorded \(DENIED\)/);assert(buttons.every(b=>!b.disabled));
}

// Change A (L660) — AC3: a tap on a decision UNIT stores the exact terms shown; a unit LATER stores choice=null.
async function unitTapTest() {
  const store=element('store'), toast=element('toast'), card=element('wq-2'), state=element();
  const note={value:' after CPI '};
  const otext=a=>({textContent:a}), opt=(label,text,cons)=>{const o=element('',{label});const t=otext(text),c=otext(cons);o.querySelector=s=>s==='.otext'?t:s==='.ocons'?c:null;return o;};
  const opts=[opt('A','Sell it now','≈ $100'),opt('B','Hold to 10/14','nothing')];
  const btnA=element('ch-2.TLT-A',{v:'CHOICE',label:'A'}), btnLater=element('lt-2.TLT',{v:'LATER'});
  const wrap=element('tap-2.TLT',{wq:'2',did:'2.TLT'}); wrap.classList.add('tap','unit');
  wrap.querySelectorAll=s=>s==='.opt'?opts:[btnA,btnLater]; wrap.querySelector=s=>s==='.tapstate'?state:null;
  btnA.closest=s=>s==='.opt'?opts[0]:wrap; btnLater.closest=()=>wrap; card.querySelector=()=>state;
  let writes=[];
  const db={collection(){return {onSnapshot(fn){fn({docs:[]});},doc(id){return {set(p){writes.push({id,payload:p});return Promise.resolve();}}}};}};
  const ctx={document:{body:{dataset:{build:'fixture-build'}},querySelectorAll:()=>[btnA,btnLater],
      getElementById:id=>({'store':store,'toast':toast,'wq-2':card,'tap-2.TLT':wrap,'note-2.TLT':note}[id])},
    setTimeout:()=>0,clearTimeout:()=>{},window:{claude:{use(){return Promise.resolve(db);}}}};
  ctx.Date=class extends Date {constructor(...args){super(...(args.length?args:['2026-10-09T17:00:00.500Z']));}};
  vm.runInNewContext(source.rulings,ctx); await new Promise(setImmediate);
  btnA.listeners.click(); await new Promise(setImmediate);
  assert.match(state.textContent,/CHOICE A — Sell it now — after CPI/); assert(opts[0].classList.contains('chosen')); assert(card.classList.contains('ruled-choice'));
  btnLater.listeners.click(); await new Promise(setImmediate);
  assert.equal(writes.length,2);
  assert.deepEqual(JSON.parse(JSON.stringify(writes[0].payload)),{wq:'2',verdict:'CHOICE',note:'after CPI',ts:'2026-10-09T17:00:00.500Z',build:'fixture-build',consumed:false,source:'decision-deck',
    decision_id:'2.TLT',options_shown:[{label:'A',text:'Sell it now'},{label:'B',text:'Hold to 10/14'}],choice:{label:'A',text:'Sell it now',consequence:'≈ $100'}});
  assert.equal(writes[1].payload.verdict,'LATER'); assert.equal(writes[1].payload.choice,null); assert.equal(writes[1].payload.decision_id,'2.TLT');
  assert.match(writes[0].id,/^2-20261009170000500-/);
  assert.match(state.textContent,/: LATER — after CPI/);
  assert(opts[0].classList.contains('chosen')===false); // LATER was the last tap: no option highlighted
  assert(card.classList.contains('ruled-later'));
}
rulingTest().then(unitTapTest).then(()=>console.log('UI, ruling and unit-tap runtime fixtures passed')).catch(e=>{console.error(e);process.exitCode=1;});
