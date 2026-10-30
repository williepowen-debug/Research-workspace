import sys, json, datetime
sys.path.insert(0,'.')
from rpc import call
P='https://ethereum-rpc.publicnode.com'
USDC='0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'; USDT='0xdac17f958d2ee523a2206206994597c13d831ec7'
T_BL='0xffa4e6181777692565cf28528fc88fd1516ea86b56da075235fa575af6a4b855'
T_ABL='0x42e160154868087d6bfdc0ca23d96a1c1cfa32f1b72ba9ba27b69b98a0d819dc'
T_DBF='0x61e6e66b0d6339b2980aecc6ccc0039736791f0ccde9ed512e789a7fbdd698c6'
START=int(sys.argv[1]); END=call('eth_blockNumber',[],P)[0]; END=int(END,16)
def ts(b):
    blk,_=call('eth_getBlockByNumber',[hex(b),False],P); return datetime.datetime.fromtimestamp(int(blk['timestamp'],16),datetime.UTC).strftime('%Y-%m-%d %H:%M:%SZ')
def logs(addr,topic):
    out=[]; s=START
    while s<=END:
        e=min(s+4999,END)
        r,_=call('eth_getLogs',[{'address':addr,'topics':[topic],'fromBlock':hex(s),'toBlock':hex(e)}],P); out+=r; s=e+1
    return out
def bal(token,a,block='latest'):
    d='0x70a08231'+a[2:].rjust(64,'0')
    r,_=call('eth_call',[{'to':token,'data':d},block],P); return int(r,16)/1e6
print('window blocks',START,END, ts(START),'->',ts(END))
for name,tok,topic in (('USDC',USDC,T_BL),('USDT',USDT,T_ABL)):
    L=logs(tok,topic); tot=0
    print(f'--- {name} blacklist events: {len(L)}')
    for l in L:
        a = '0x'+(l['topics'][1][-40:] if len(l['topics'])>1 else l['data'][-40:])
        b=bal(tok,a); tot+=b
        print(name, ts(int(l['blockNumber'],16)), a, f'{b:,.2f}', l['transactionHash'])
    print(f'{name} TOTAL balance now at addresses blacklisted in window: {tot:,.2f}')
L=logs(USDT,T_DBF); print('USDT DestroyedBlackFunds events', len(L))
