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
  assert.match(state.textContent,/② Received by PROME \(pickup stamp not recorded\).*DECLINE.*receipt is not execution/);
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
  // read 2 ❌X2: a PLAIN unit's APPROVE stores the verb's stated meaning as choice.text
  const btnAp=element('ap-2.HBAN',{v:'APPROVE'}), meaning={textContent:'sell it (card A)'};
  const wrapP=element('tap-2.HBAN',{wq:'2',did:'2.HBAN'}); wrapP.classList.add('tap','unit');
  wrapP.querySelectorAll=s=>s==='.opt'?[]:[btnAp]; wrapP.querySelector=s=>s==='.tapstate'?state:(s==='.otext[data-for="APPROVE"]'?meaning:null);
  btnAp.closest=()=>wrapP;
  ctx.document.getElementById=id=>({'store':store,'toast':toast,'wq-2':card,'tap-2.TLT':wrap,'note-2.TLT':note,'tap-2.HBAN':wrapP,'note-2.HBAN':{value:''}}[id]);
  ctx.document.querySelectorAll=()=>[btnA,btnLater,btnAp];
  writes.length=0; vm.runInNewContext(source.rulings,ctx); await new Promise(setImmediate);
  btnAp.listeners.click(); await new Promise(setImmediate);
  assert.equal(writes.length,1);
  assert.deepEqual(JSON.parse(JSON.stringify(writes[0].payload.choice)),{label:'APPROVE',text:'sell it (card A)',consequence:''});
  assert.equal(writes[0].payload.decision_id,'2.HBAN'); assert.deepEqual(JSON.parse(JSON.stringify(writes[0].payload.options_shown)),[]);
  assert.match(state.textContent,/APPROVE — sell it \(card A\)/);
  // episode 2 E6: a whole-row document (no decision_id) on a multi-unit card lands on the ROW line, never in a unit;
  // the card tint follows the latest ts across units and row
  const rowline=element('rowstate-2'); rowline.classList.add('tapstate','rowstate');
  ctx.document.getElementById=id=>({'store':store,'toast':toast,'wq-2':card,'tap-2.TLT':wrap,'note-2.TLT':note,'tap-2.HBAN':wrapP,'note-2.HBAN':{value:''},'rowstate-2':rowline}[id]);
  let snap2; const db2={collection(){return {onSnapshot(fn){snap2=fn;},doc(id){return {set(p){return Promise.resolve();}}}};}};
  ctx.window={claude:{use(){return Promise.resolve(db2);}}};
  vm.runInNewContext(source.rulings,ctx); await new Promise(setImmediate);
  snap2({docs:[{data:()=>({wq:'2',verdict:'APPROVE',ts:'2026-10-01T00:00:00Z',consumed:true})},
               {data:()=>({wq:'2',decision_id:'2.TLT',verdict:'CHOICE',choice:{label:'B',text:'Hold'},ts:'2026-10-09T17:00:00Z'})}]});
  assert.match(rowline.textContent,/Whole-row tap \(no unit\): ② Received by PROME .*APPROVE/);
  assert.equal(rowline.hidden,false);
  assert(card.classList.contains('ruled-choice')); assert(!card.classList.contains('ruled-approve'));   // latest ts wins
}
// Change B (ACCEPTANCE_deck_changeB_2026-10-09.md AC-B7/AC-B11): pipeline stamps + disposition render.
async function pipelineTest() {
  const store=element('store'), toast=element('toast'), card=element('wq-7'), state=element();
  const buttons=[]; let snap;
  const db={collection(){return {onSnapshot(fn){snap=fn;},doc(){return {set(){return Promise.resolve();}}}};}};
  const ctx={document:{body:{dataset:{build:'b'}},querySelectorAll:()=>buttons,
      getElementById:id=>({'store':store,'toast':toast,'wq-7':card}[id])},
    setTimeout:()=>0,clearTimeout:()=>{},window:{claude:{use(){return Promise.resolve(db);}}}};
  card.querySelector=()=>state;
  vm.runInNewContext(source.rulings,ctx); await new Promise(setImmediate);
  // ② with a pickup stamp
  snap({docs:[{data:()=>({wq:'7',verdict:'APPROVE',ts:'2026-10-09T21:00:00Z',consumed:true,picked_up:'2026-10-09T22:30:00Z'})}]});
  assert.match(state.textContent,/② Received by PROME /); assert.doesNotMatch(state.textContent,/stamp not recorded/);
  assert.match(state.textContent,/receipt is not execution/);
  // ③ disposition rendered only because the doc carries it
  snap({docs:[{data:()=>({wq:'7',verdict:'APPROVE',ts:'2026-10-09T23:00:00Z',consumed:true,picked_up:'2026-10-09T23:10:00Z',disposition:'encoded at GATES row',disposition_ts:'2026-10-09T23:20:00Z'})}]});
  assert.match(state.textContent,/③ Disposition recorded .*: encoded at GATES row/);
  assert.doesNotMatch(state.textContent,/receipt is not execution/);
}

// Change B — AC-B2/B3/B4: the chip filter never hides a pinned card, saved chips restore, headings follow.
function chipTest() {
  function cardEl(id,pin,kchip,dom){const c=element(id,{pin,kchip,dom});return c;}
  const pinned=cardEl('wq-10','1','Trade',''), ruleCard=cardEl('wq-11','0','Rule',''), domCard=cardEl('wq-12','0','Chore','Credit');
  const grp=element('g1'); grp.classList.add('grp');
  grp.nextElementSibling=pinned; pinned.nextElementSibling=ruleCard; ruleCard.nextElementSibling=domCard; domCard.nextElementSibling=null;
  pinned.classList.add('card'); ruleCard.classList.add('card'); domCard.classList.add('card');
  const chipAll=element('',{chip:'All'}), chipTrade=element('',{chip:'Trade'}), chipCredit=element('',{chip:'Credit'});
  const bar={querySelectorAll:()=>[chipAll,chipTrade,chipCredit]};
  const storage=new Map([['deck.chip.owed','Credit']]);              // a SAVED domain chip
  const ctx={document:{body:{dataset:{view:'owed'}},
      querySelector:s=>s==='.chipbar'?bar:null,
      querySelectorAll:s=>({'.tab':[], '.panel':[], '.card':[], '.lnk[data-all]':[],
                            '#owed .card':[pinned,ruleCard,domCard],
                            '#owed .card, #owed .ovrow, #owed .ovtile':[pinned,ruleCard,domCard],
                            '#owed .grp':[grp]}[s]||[]),
      getElementById:()=>null},
    localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)},location:{hash:''},window:{}};
  vm.runInNewContext(source.ui,ctx);
  // saved 'Credit' applied on load: pinned stays visible, Rule card hidden, Credit-domain card visible
  assert.equal(pinned.classList.contains('chiphide'),false,'a saved chip must never hide a pinned card (AC-B3/B4)');
  assert.equal(ruleCard.classList.contains('chiphide'),true);
  assert.equal(domCard.classList.contains('chiphide'),false);
  assert.equal(grp.classList.contains('chiphide'),false);
  // tap Trade: pinned visible (matches anyway), others hidden; heading survives via the pinned card
  chipTrade.listeners.click();
  assert.equal(pinned.classList.contains('chiphide'),false);
  assert.equal(domCard.classList.contains('chiphide'),true);
  assert.equal(storage.get('deck.chip.owed'),'Trade');
  // All restores
  chipAll.listeners.click();
  assert.equal(ruleCard.classList.contains('chiphide'),false);
  // read 2 ❌2: a deep link to a hidden card shows All WITHOUT overwriting the saved chip
  storage.set('deck.chip.owed','Credit');
  const ctx2={document:{body:{dataset:{view:'owed'}},
      querySelector:s=>s==='.chipbar'?bar:null,
      querySelectorAll:s=>({'.tab':[], '.panel':[], '.card':[], '.lnk[data-all]':[],
                            '#owed .card':[pinned,ruleCard,domCard],
                            '#owed .card, #owed .ovrow, #owed .ovtile':[pinned,ruleCard,domCard],
                            '#owed .grp':[grp]}[s]||[]),
      getElementById:id=>id==='wq-11'?ruleCard:null},
    localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)},location:{hash:'#wq-11'},window:{},
    Intl:Intl, Date:Date};
  vm.runInNewContext(source.ui,ctx2);
  assert.equal(ruleCard.classList.contains('chiphide'),false,'deep-linked card must be visible');
  assert.equal(storage.get('deck.chip.owed'),'Credit','the saved chip must survive a deep-link visit');
}

// Change C (ACCEPTANCE_deck_changeC AC-C1/C2/C4/C5/C6): view toggle persists, table sorts, the peek
// relocates the REAL node and returns it, a preset never hides a pinned card.
function viewTest() {
  let keyFn=null;
  function container(){ const kids=[]; const c={children:kids,
    insertBefore(n,ref){ if(n.parentNode&&n.parentNode.removeChild)n.parentNode.removeChild(n); const i=kids.indexOf(ref); kids.splice(i<0?kids.length:i,0,n); n.parentNode=c; },
    appendChild(n){ if(n.parentNode&&n.parentNode.removeChild)n.parentNode.removeChild(n); kids.push(n); n.parentNode=c; },
    removeChild(n){ const i=kids.indexOf(n); if(i>=0)kids.splice(i,1); n.parentNode=null; }}; return c; }
  const listC=container(), peekC=container();
  const cardA=element('wq-7',{wq:'7',pin:'0',kchip:'Rule',dom:'',due:'2099-01-01',grp:'owed'}); cardA.classList.add('card');
  const cardB=element('wq-8',{wq:'8',pin:'1',kchip:'Trade',dom:'',due:'2026-10-09',grp:'owed'}); cardB.classList.add('card');
  listC.appendChild(cardA); listC.appendChild(cardB);
  const tileA=element('t7',{wq:'7',pin:'0',kchip:'Rule',dom:'',due:'2099-01-01',grp:'owed'}); tileA.classList.add('ovtile');
  const tileB=element('t8',{wq:'8',pin:'1',kchip:'Trade',dom:'',due:'2026-10-09',grp:'owed'}); tileB.classList.add('ovtile');
  // table stub with two sortable rows
  const tb=container();
  const rowA=element('r7',{wq:'7',pin:'0',due:'2099-01-01',since:'9/1',grp:'owed'}); rowA.classList.add('ovrow');
  const rowB=element('r8',{wq:'8',pin:'1',due:'2026-10-09',since:'10/1',grp:'owed'}); rowB.classList.add('ovrow');
  tb.appendChild(rowA); tb.appendChild(rowB);
  const thWq=element('',{sort:'wq'}), thDue=element('',{sort:'due'}); thDue.classList.add('sorted');
  const ovTable={hidden:false,querySelector:s=>s==='tbody'?{querySelectorAll:()=>tb.children.slice()}:null,
    querySelectorAll:s=>s==='th[data-sort]'?[thWq,thDue]:[]};
  // patch: sortTable appends into tb via each row's reinsertion — emulate by giving tbody appendChild
  ovTable.querySelector=s=>s==='tbody'?Object.assign(tb,{querySelectorAll:()=>tb.children.slice()}):null;
  const ovGrid={hidden:false}; const listWrap=element('listwrap');
  const peekEl={hidden:true}; const pkPos=element('pk-pos');
  const chipAll=element('',{chip:'All'}); const bar={querySelectorAll:()=>[chipAll]};
  const pAll=element('',{preset:'all'}), pToday=element('',{preset:'today'});
  const vList=element('',{view:'list'}), vTable=element('',{view:'table'}), vBoard=element('',{view:'board'});
  const storage=new Map();
  const units=[cardA,cardB,rowA,rowB,tileA,tileB];
  const ctx={document:{body:{dataset:{view:'owed'}},
      querySelector:s=>({'.chipbar':bar,'.ovtable':ovTable,'.ovgrid':ovGrid}[s]||null),
      querySelectorAll:s=>({'.tab':[], '.panel':[], '.card':[], '.lnk[data-all]':[],
        '.pbtn':[pAll,pToday], '.vbtn':[vList,vTable,vBoard],
        '#owed .card, #owed .ovrow, #owed .ovtile':units,
        '#owed .ovrow':[rowA,rowB], '#owed .ovtile':[tileA,tileB], '#owed .grp':[]}[s]||[]),
      getElementById:id=>({'listwrap':listWrap,'peek':peekEl,'peekbody':peekC,'pk-pos':pkPos,'wq-7':cardA,'wq-8':cardB}[id]||null),
      createComment:()=>({parentNode:null}), addEventListener:(k,fn)=>{ if(k==='keydown') keyFn=fn; }},
    localStorage:{getItem:k=>storage.get(k),setItem:(k,v)=>storage.set(k,v)},location:{hash:''},window:{},Intl:Intl,Date:Date};
  vm.runInNewContext(source.ui,ctx);
  // AC-C1: toggle persists
  vBoard.listeners.click();
  assert.equal(storage.get('deck.viewmode.owed'),'board'); assert.equal(ovGrid.hidden,false); assert.equal(ovTable.hidden,true);
  assert(listWrap.classList.contains('ovhide'));
  // AC-C2: sort by wq re-orders ascending; default due sort had put pinned/due row first
  assert.equal(tb.children[0].dataset.wq,'8','due sort: pinned+due row first');
  thWq.listeners.click();
  assert.equal(tb.children[0].dataset.wq,'7','wq sort ascending');
  // AC-C4: peek relocates the SAME node and returns it to its slot
  tileA.listeners.click();
  assert.equal(peekC.children[0],cardA,'peek holds the identical node'); assert.equal(peekEl.hidden,false);
  assert(cardA.classList.contains('peeked'));
  tileB.listeners.click();
  assert.equal(peekC.children[0],cardB,'peek swaps to the next real node');
  assert.equal(listC.children.indexOf(cardA),0,'first card returned to its original slot');
  vList.listeners.click();                               // switching to list closes the peek
  assert.equal(peekEl.hidden,true);
  assert.equal(listC.children.indexOf(cardB),1,'second card returned on close');
  assert(!cardB.classList.contains('peeked'));
  // read 1 ❌5: a saved 'waiting' preset with zero blocked rows must fall back to Everything, unsaved
  const storage2=new Map([['deck.preset.owed','waiting']]);
  const cardC=element('wq-9',{wq:'9',pin:'1',kchip:'Trade',dom:'',due:'2026-10-09',grp:'owed'}); cardC.classList.add('card');
  const empty2={hidden:true};
  const ctx3={document:{body:{dataset:{view:'owed'}},
      querySelector:s=>({'.chipbar':{querySelectorAll:()=>[element('',{chip:'All'})]},'.ovempty':empty2}[s]||null),
      querySelectorAll:s=>({'.pbtn':[], '.vbtn':[], '#owed .card, #owed .ovrow, #owed .ovtile':[cardC],
        '#owed .ovrow':[], '#owed .ovtile':[], '#owed .grp':[], '.tab':[], '.panel':[], '.card':[], '.lnk[data-all]':[]}[s]||[]),
      getElementById:()=>null, addEventListener:()=>{}, createComment:()=>({parentNode:null})},
    localStorage:{getItem:k=>storage2.get(k),setItem:(k,v)=>storage2.set(k,v)},location:{hash:''},window:{},Intl:Intl,Date:Date};
  vm.runInNewContext(source.ui,ctx3);
  assert.equal(cardC.classList.contains('chiphide'),false,'the blank saved view must fall back to Everything');
  assert.equal(storage2.get('deck.preset.owed'),'waiting','the fallback must NOT overwrite the saved preset');
  // read 1 ❌3: arrow keys are ignored while the target is an input
  // (the real exercise is viewTest's keyFn calls against the production handler)
  // read 1 ❌3/❌4: typing guard + minimize restore, against the production handler
  cardA.classList.add('min');
  tileA.listeners.click();                                  // peek the minimized card
  assert(!cardA.classList.contains('min'),'peek expands the card');
  assert(keyFn,'keydown handler captured');
  keyFn({key:'ArrowRight',target:{tagName:'INPUT'}});       // typing in a note box: must NOT step
  assert.equal(peekC.children[0],cardA,'arrow key ignored while typing');
  keyFn({key:'Escape',target:{tagName:'DIV'}});             // Esc outside an input closes
  assert.equal(peekEl.hidden,true);
  assert(cardA.classList.contains('min'),'minimized card restored minimized (read 1 ❌4)');
  cardA.classList.remove('min');
  // AC-C5: the today preset hides the non-pinned future card everywhere, never the pinned one
  pToday.listeners.click();
  assert.equal(cardB.classList.contains('chiphide'),false,'pinned card visible under My action today');
  assert.equal(cardA.classList.contains('chiphide'),true);
  assert.equal(tileA.classList.contains('chiphide'),true); assert.equal(rowA.classList.contains('chiphide'),true);
  assert.equal(storage.get('deck.preset.owed'),'today');
  pAll.listeners.click();
  assert.equal(cardA.classList.contains('chiphide'),false);
}

rulingTest().then(unitTapTest).then(pipelineTest).then(chipTest).then(viewTest).then(()=>console.log('UI, ruling, unit-tap, pipeline, chip and view runtime fixtures passed')).catch(e=>{console.error(e);process.exitCode=1;});
