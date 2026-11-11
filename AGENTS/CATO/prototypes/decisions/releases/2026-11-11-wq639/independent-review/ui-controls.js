const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync('/tmp/cato-wq639-independent-review/tree/AGENTS/CATO/prototypes/decisions/mvp/desk.html','utf8');
const fn=html.split('\n').find(l=>l.startsWith('function recommendationButtons('));
let nodes=[];const ctx={recommendedChoice:()=>({id:'A',label:'Bounded task'}),inlineConditions:{},add:(tag,text,parent,cls)=>{let n={tag,text,parent,cls,dataset:{}};nodes.push(n);return n;},openRecommendation:()=>{}};
vm.createContext(ctx);vm.runInContext(fn,ctx);
for(const state of ['integrated','received',undefined]) {
 nodes=[];let card={unit:{id:'901.queue'},can_respond:true,receipt:state?{state}:undefined};
 const shown=ctx.recommendationButtons(card,{});
 assert.equal(shown,state!=='integrated');
 assert.equal(nodes.filter(n=>n.tag==='button').length,state==='integrated'?0:2);
 console.log(state||'no receipt','PASS');
}
nodes=[];ctx.recommendationButtons({unit:{id:'901.queue'},can_respond:false,receipt:{state:'received'}},{});
assert(nodes.filter(n=>n.tag==='button').every(n=>n.disabled));console.log('received read-only buttons remain disabled PASS');
