# BOND L410 quarterly I' re-freeze (2026-10-01). Re-runnable: prints the seven per-tenor
# trailing-12 bars strictly prior to 2026-10-01 with the CLEAN tool (FRN filter, cycle_term,
# degenerate guard), the provenance of each OLD-test extreme (contamination check, banner item 4),
# and RED's positive-boundary fixture (a print exactly ON each 2dp bar must NOT fire under STRICT).
import sys, io, contextlib
sys.path.insert(0, "monitors")
import grade_auction as G
import numpy as np
AS_OF = "2026-10-01"
_err = io.StringIO()
with contextlib.redirect_stderr(_err):
    recs = G.load()
print(f"[refreeze] as-of {AS_OF} (strictly prior) · n=12 · %-of-competitive-accepted · P15 linear · STRICT")
print(f"[refreeze] loader notes: " + " | ".join(l.strip() for l in _err.getvalue().splitlines() if l.strip()))
print(f"[refreeze] degenerate rows excluded: {len(G.DEGENERATE)}")
frn = G.frn_cusips()
rows = []
for term in ("2-Year", "3-Year", "5-Year", "7-Year", "10-Year", "20-Year", "30-Year"):
    b = G.bench(recs, term, False, AS_OF, 12)
    h = [x for x in recs if x["term"] == term and not x["tips"] and x["date"] < AS_OF and x["btc"] is not None][-12:]
    imin = min(h, key=lambda x: x["ind"]); dmax = max(h, key=lambda x: x["dlr"])
    def prov(x):
        flags = []
        if x["cusip"] in frn: flags.append("FRN!")
        if x["secterm"] and G.TERM_MAP.get(x["secterm"], x["secterm"]) != term and not str(x["secterm"]).startswith(term.split("-")[0]):
            flags.append(f"secterm={x['secterm']}")
        flags.append("reopen" if x["reopening"] else "new")
        return f"{x['date']} {x['cusip']} ({','.join(flags)})"
    bar2 = round(b["ind_p15"], 2)
    # RED positive-boundary fixture: print exactly ON the frozen 2dp bar
    on_frozen = not (bar2 < bar2)            # frozen-bar compare: must be NOT FIRED
    on_float = (bar2 < b["ind_p15"])          # tool's float compare: True = the tool would FIRE a print ON the 2dp bar
    ro = b.get("ind_p15_reopen_only")
    print(f"\n{term:8} window {b['from']}→{b['to']} n={b['n']}")
    print(f"   I' P15 = {b['ind_p15']:.4f} → frozen {bar2:.2f}   (reopen-only alt {ro:.2f}, n={b['n_reopen']})" if ro is not None
          else f"   I' P15 = {b['ind_p15']:.4f} → frozen {bar2:.2f}   (reopen-only alt n/a, n_reopen={b['n_reopen']})")
    print(f"   OLD: indirect MIN {b['ind']['min']:.2f} @ {prov(imin)}")
    print(f"        dealer   MAX {b['dlr']['max']:.2f} @ {prov(dmax)}")
    print(f"   BTC MIN {b['btc']['min']:.2f} · ind median {b['ind']['median']:.2f} · dealer median {b['dlr']['median']:.2f}")
    print(f"   RED fixture: print ON frozen bar {bar2:.2f} → frozen-compare {'NOT FIRED ✅' if on_frozen else 'FIRED ❌'} · "
          f"float-compare {'FIRES ⚠️ (tie band ' + f'[{bar2:.2f},{b[chr(105)+chr(110)+chr(100)+chr(95)+chr(112)+chr(49)+chr(53)]:.4f}))' if on_float else 'NOT FIRED'}")
    rows.append((term, b, bar2))
print("\n[refreeze] 9/23 5Y OLD-test contamination check (banner item 4): window strictly prior to 2026-09-23")
b5 = G.bench(recs, "5-Year", False, "2026-09-23", 12)
h5 = [x for x in recs if x["term"] == "5-Year" and not x["tips"] and x["date"] < "2026-09-23" and x["btc"] is not None][-12:]
for x in sorted(h5, key=lambda x: -x["dlr"])[:3]:
    print(f"   dealer {x['dlr']:.2f}  {x['date']} {x['cusip']} secterm={x['secterm']} reopen={x['reopening']} FRN={x['cusip'] in frn}")
print(f"   max {b5['dlr']['max']:.2f} (9/23 print 15.77 ⇒ margin {15.77 - b5['dlr']['max']:+.2f}pp)")
