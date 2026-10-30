"""WQ-550 leg 1/2: Ethereum totalSupply of USDT/USDC + frozen attacker balances, latest state only (no archive).
Usage: python3 -I scripts/supply_and_balances.py <out_txt>   (reuses ../2026-10-30_binance-first-read/scripts/rpc.py)"""
import sys, os, datetime, importlib.util
spec=importlib.util.spec_from_file_location("rpc", os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","..","2026-10-30_binance-first-read","scripts","rpc.py"))
rpc=importlib.util.module_from_spec(spec); spec.loader.exec_module(rpc)
USDT="0xdAC17F958D2ee523a2206206994597C13D831ec7"; USDC="0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
def c(to,data):
    r,u=rpc.call("eth_call",[{"to":to,"data":data},"latest"]); return int(r,16),u
def bal(tok,addr): return c(tok,"0x70a08231"+addr[2:].lower().rjust(64,"0"))[0]/1e6
blk,u=rpc.call("eth_blockNumber",[]); blk=int(blk,16)
ts=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
lines=[f"Source: Ethereum JSON-RPC {u} (public, read-only), CYPHER {ts}, block {blk} (latest state only)"]
for n,t in (("USDT",USDT),("USDC",USDC)):
    s,_=c(t,"0x18160ddd"); lines.append(f"{n} totalSupply on Ethereum: {s/1e6:,.2f}")
A="0x5227f603"  # prefix only in RECORD; full addresses not in record -> balance re-read skipped unless provided
lines.append("Attacker-address balance re-read: SKIPPED here (full addresses live in ../2026-10-30_binance-first-read/onchain_freeze_tally_2026-10-30.txt; see freeze_tally.py)")
out="\n".join(lines); print(out); open(sys.argv[1],"w").write(out+"\n")
