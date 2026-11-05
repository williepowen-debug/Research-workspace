#!/usr/bin/env python3
"""11/5 catch-up: net-GEX profile by spot and key put OI, from the saved Cboe payload. Read-only."""
import sys, re, json
sys.path.insert(0,'scripts')
import gamma_flip as g
for u,lv in [('SPX',[7800,7750,7700,7650,7600,7550,7500,7450,7400,7350,7300,7200,7100]),('QQQ',[720,710,700,690,680,675,670,665,660,650,640,630,620])]:
    print(u,'35d net GEX $B per 1% by spot:')
    for s in lv:
        r=g.compute_gamma_flip(horizon=35,underlying=u,spot_override=s)
        print(f"  {s}: {r['gex_at_spot']/1e9:+.2f}" if 'error' not in r else f"  {s}: {r['error']}")
