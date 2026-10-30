import sys, datetime
sys.path.insert(0,'.')
from rpc import call
P='https://ethereum-rpc.publicnode.com'
TR='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef'
tok={'USDT':'0xdac17f958d2ee523a2206206994597c13d831ec7','USDC':'0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'}
START=26296000; END=int(call('eth_blockNumber',[],P)[0],16)
def pad(a): return '0x'+a[2:].rjust(64,'0')
def logs(addr,topics):
    out=[]; s=START
    while s<=END:
        e=min(s+4999,END)
        r,_=call('eth_getLogs',[{'address':addr,'topics':topics,'fromBlock':hex(s),'toBlock':hex(e)}],P); out+=r; s=e+1
    return out
for t,a in [(x.split(':')[0],x.split(':')[1]) for x in sys.argv[1:]]:
    for direction,topics in (('IN',[TR,None,pad(a)]),('OUT',[TR,pad(a),None])):
        L=logs(tok[t],topics); tot=0
        for l in L:
            v=int(l['data'],16)/1e6; tot+=v
            frm='0x'+l['topics'][1][-40:]; to='0x'+l['topics'][2][-40:]
            if v>=1e6: print(t,a[:10],direction,int(l['blockNumber'],16),'from',frm,'to',to,f'{v:,.0f}')
        print(f'== {t} {a} {direction} n={len(L)} total={tot:,.2f}')
