"""Construction check (WQ-163 item 3) for REG-36 vs REG-37 resolution cells, 2026-11-19.
Synthetic sequences only; no market data. Non-session bars are assumed already dropped
(bridged per registry/NOTES.md). None = a market session with no first-published value."""
def runs3(s):
    return any(all(v is not None and v > 350 for v in s[i:i+3]) for i in range(len(s)-2))
def near_runs(s):  # REG-36 reading: two prints > 350, then the third in [349, 350]
    return [i for i in range(len(s)-2) if s[i] is not None and s[i+1] is not None and s[i+2] is not None
            and s[i] > 350 and s[i+1] > 350 and 349 <= s[i+2] <= 350]
def could_run(s):  # would filling every missing session with 999 create a run?
    return runs3([999 if v is None else v for v in s])
def reg36(s):
    miss = sum(v is None for v in s)
    if miss > 5: return "NO-VERDICT"
    if runs3(s): return "TRUE"
    if len(near_runs(s)) == 1: return "NO-VERDICT"
    if miss and could_run(s): return "UNDEFINED (letter silent)"
    return "FALSE"
def reg37(s):
    miss = sum(v is None for v in s)
    if miss > 5: return "NO-VERDICT"
    if runs3(s): return "TRUE"
    if miss and could_run(s): return "NO-VERDICT"
    return "FALSE"
lo = [340] * 13
CASES = {
 "A CATO counterexample 351,352,350, rest <349": lo[:5] + [351, 352, 350] + lo[:8],
 "B clean run 351,352,351":                      lo[:5] + [351, 352, 351] + lo[:8],
 "C near-run third 349":                          lo[:5] + [351, 352, 349] + lo[:8],
 "D near-run third 348":                          lo[:5] + [351, 352, 348] + lo[:8],
 "E three ties 350,350,350":                      lo[:5] + [350, 350, 350] + lo[:8],
 "F two near-runs (350 and 349)":                 lo[:2] + [351, 352, 350] + lo[:3] + [353, 351, 349] + lo[:5],
 "G near-run then a full run later":              lo[:2] + [351, 352, 350] + lo[:3] + [352, 353, 354] + lo[:5],
 "H missing session inside a possible run":       lo[:5] + [351, None, 352] + lo[:8],
 "I one missing session, no possible run":        lo[:5] + [None] + lo[:10],
 "J six missing sessions, no run":                [None] * 6 + lo[:10],
 "K six missing sessions and a full run":         [None] * 6 + [351, 352, 353] + lo[:7],
 "L all below 349":                               lo + lo[:3],
}
print(f"{'case':48} {'REG-36':28} REG-37")
for k, s in CASES.items():
    a, b = reg36(s), reg37(s)
    print(f"{k:48} {a:28} {b}{'   <- differs' if a != b else ''}")
