# groupC addendum — `HKMA buys` live test, 2026-10-09 (walter-50)

Asked by PROME before landing ZHAO's 10/9 R3 set: `HKMA buys` was SUGGESTED in groupC §4 row 8 prose but never SCORED.
Run: `tools/watch_for_harness.py --desk ZHAO --phrase "HKMA buys" --live "HKMA buys Hong Kong dollars" --live "HKMA Hong Kong dollar peg" --live "HKMA intervenes" --live-days 365 --synthetic "HKMA buys HK$3.2 billion to defend peg"` (~10:4x ET).
Result: lane 12,063 headlines (6/29→10/8) = 0 hits · live 53 headlines / 3 queries / 365d = 0 hits · synthetic FIRES.
Verdict: ✅ PASS on precision (0 FALSE); recall UNPROVEN (no matching headline in the live sample). Caveat carried from groupC: the long form "Hong Kong Monetary Authority buys …" cannot match (HKMA is a required ALL-CAPS token, no alias).
