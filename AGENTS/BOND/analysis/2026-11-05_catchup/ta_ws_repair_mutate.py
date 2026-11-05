import subprocess,sys,shutil,os
M=sys.argv[1]; PY=sys.argv[2]
def run():
    bad=[]
    for cmd in ([PY,"-B","ta_ws_schema.py","--selftest"],[PY,"-B","docket_check.py","--selftest"],[PY,"-B","-m","unittest","test_monitor_repairs"]):
        r=subprocess.run(cmd,cwd=M,capture_output=True,text=True,timeout=120)
        if r.returncode!=0: bad.append(cmd[2].split('.')[0] if 'unittest' not in cmd else 'unittest')
    return bad
print("baseline",run())
T="ta_ws_schema.py";D="docket_check.py";G="grade_auction.py"
muts=[(T,f'    "{k}": "{v}",\n','') for k,v in [("auctionDate","competitiveAuctionCloseDate"),("tips","inflationProtected"),("primaryDealerAccepted","primaryDealersCompetitiveParAwarded"),("indirectBidderAccepted","indirectBiddersCompetitiveParAwarded"),("directBidderAccepted","directBiddersCompetitiveParAwarded")]]
muts+=[
(T,"                conflicts.append(old)\n","                pass\n"),
(T,'                conflicts.append("competitiveAccepted")\n',"                pass\n"),
(T,"            if have_new and not have_old:","            if have_new and old not in r:"),
(T,'    if iso_date(r.get("auctionDate")) is None:\n','    if False:\n'),
(T,'        if r.get(k) not in ("Yes", "No"):\n','        if False:\n'),
(T,'    if r.get(CONFLICT):\n        return','    if False:\n        return'),
(T,'        if not isinstance(r, dict) or r.get("securityType") not in KNOWN_TYPES:\n','        if False:\n'),
(D,"    if feed_horizon(data) is None:\n","    if False:\n"),
(D,"    why = schema_refusal(rows, today)\n    if why:   #","    why = None\n    if why:   #"),
(D,"        if ad < today - dt.timedelta(days=STALE_UPCOMING_DAYS):\n","        if False:\n"),
(D,"        why = coupon_row_defect(r, fields=())\n        if why:\n","        why = None\n        if why:\n"),
(G,"    if not coupons:\n","    if False:\n"),
(G,'r.get("floatingRate") == "Yes" or r.get("cusip") in frn:','r.get("floatingRate") == "Yes":'),
(G,'''        print(f"[grade] ⚠️ FRN list pull returned no CUSIPs; using cached {FRN_CACHE.name}", file=sys.stderr)\n''',''),
(G,'''        why = coupon_row_defect(r)\n        if why:\n            print(f"[grade] ⛔ GAP — TA_WS schema''','''        why = None\n        if why:\n            print(f"[grade] ⛔ GAP — TA_WS schema'''),
(G,"    elif ip:\n","    elif False:\n"),
(G,"        if why and r.get(CONFLICT):      #","        if False:      #"),
(G,"        if why:                          # pool","        if False:                          # pool"),
(G,'''    why = type_defect(rows)\n    if why:\n        raise''','''    why = None\n    if why:\n        raise'''),
]
surv=0
for f,a,b in muts:
    p=os.path.join(M,f); o=open(p).read()
    assert a in o,a
    open(p,"w").write(o.replace(a,b,1))
    try: k=run()
    finally: open(p,"w").write(o)
    print(("KILLED by "+",".join(k)) if k else "SURVIVED",'|',f,'|',a.strip()[:62])
    surv+= (not k)
print("survivors",surv,"of",len(muts))
