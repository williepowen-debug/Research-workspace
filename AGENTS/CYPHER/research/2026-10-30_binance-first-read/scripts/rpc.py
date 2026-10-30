import json, sys, urllib.request
RPCS=["https://ethereum-rpc.publicnode.com","https://eth.llamarpc.com","https://cloudflare-eth.com","https://rpc.ankr.com/eth"]
def call(method, params, rpc=None):
    last=None
    for u in ([rpc] if rpc else RPCS):
        try:
            req=urllib.request.Request(u, data=json.dumps({"jsonrpc":"2.0","id":1,"method":method,"params":params}).encode(), headers={"Content-Type":"application/json","User-Agent":"Mozilla/5.0"})
            r=json.load(urllib.request.urlopen(req, timeout=30))
            if "error" in r: last=(u,r["error"]); continue
            return r["result"], u
        except Exception as e:
            last=(u,str(e))
    raise RuntimeError(last)
