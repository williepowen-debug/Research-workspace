"""WQ-550 leg 2: re-read balances at every address blacklisted in the leg-1 window (from the leg-1 tally file),
and scan for new blacklist / DestroyedBlackFunds events since a start block, across the public RPC fallback list.
Usage: python3 -I scripts/freeze_recheck.py <leg1_tally_txt> <start_block> <out_txt>"""
import sys, os, re, datetime, importlib.util
spec=importlib.util.spec_from_file_location("rpc", os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","2026-10-30_binance-first-read","scripts","rpc.py"))
rpc=importlib.util.module_from_spec(spec); spec.loader.exec_module(rpc)
USDC='0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48'; USDT='0xdac17f958d2ee523a2206206994597c13d831ec7'
T={'USDC_BL':'0xffa4e6181777692565cf28528fc88fd1516ea86b56da075235fa575af6a4b855','USDT_ABL':'0x42e160154868087d6bfdc0ca23d96a1c1cfa32f1b72ba9ba27b69b98a0d819dc','USDT_DBF':'0x61e6e66b0d6339b2980aecc6ccc0039736791f0ccde9ed512e789a7fbdd698c6'}
tok={'USDC':USDC,'USDT':USDT}
out=[]; P=lambda s: (print(s), out.append(s))
blk,u=rpc.call('eth_blockNumber',[]); END=int(blk,16)
P(f"Source: Ethereum JSON-RPC fallback list {rpc.RPCS} (public, read-only); CYPHER {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%MZ')}; latest block {END} via {u}")
rows=[l.split() for l in open(sys.argv[1]) if re.match(r'^(USDC|USDT) 2026',l)]
tot={'USDC':0.0,'USDT':0.0}
P("--- balances now at the 22 addresses blacklisted in the leg-1 window (10/29 20:10Z .. 10/30 14:54Z); leg-1 balance in brackets")
for r in rows:
    name,addr,old=r[0],r[3],float(r[4].replace(',',''))
    d='0x70a08231'+addr[2:].rjust(64,'0'); res,_=rpc.call('eth_call',[{'to':tok[name],'data':d},'latest'])
    b=int(res,16)/1e6; tot[name]+=b
    P(f"{name} {addr} {b:,.2f} [{old:,.2f}]{'  CHANGED' if abs(b-old)>0.005 else ''}")
for n in tot: P(f"{n} TOTAL now at those addresses: {tot[n]:,.2f}")
START=int(sys.argv[2])
def logs(addr,topic,step=2000):
    got=[]; s=START
    while s<=END:
        e=min(s+step-1,END)
        r,_=rpc.call('eth_getLogs',[{'address':addr,'topics':[topic],'fromBlock':hex(s),'toBlock':hex(e)}]); got+=r; s=e+1
    return got
for label,addr,topic in (('USDC Blacklisted',USDC,T['USDC_BL']),('USDT AddedBlackList',USDT,T['USDT_ABL']),('USDT DestroyedBlackFunds',USDT,T['USDT_DBF'])):
    try:
        L=logs(addr,topic); P(f"--- {label} events since block {START}: {len(L)}")
        for l in L:
            a='0x'+(l['topics'][1][-40:] if len(l['topics'])>1 else l['data'][2:66][-40:])
            P(f"  block {int(l['blockNumber'],16)} {a} data {l['data'][:80]} tx {l['transactionHash']}")
    except Exception as ex:
        P(f"--- {label}: getLogs FAILED on every RPC ({ex}) -> UNKNOWN, not zero")
open(sys.argv[3],'w').write('\n'.join(out)+'\n')
