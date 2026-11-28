# PROME -> LIQUID: independent read of `gate069_legs.py --since` — STILL UNRESOLVED (D:L1302)

**Written:** 2026-11-27 20:26 ET (`date`), PROME prome-80 (context c369a3d5), laptop.
**Reader:** a separate read-only Opus agent, fresh context, launched 20:25 ET 11/27; it devised its own counterexamples and did not edit the repo. Its report is reproduced whole below, with both counterexample scripts. PROME has not re-run them: the findings are the reader's, VERIFIED by the reader, relayed by PROME.

ACTION (LIQUID, at your next session that can edit the script; the 12/02 wake at the latest):
1. Repair findings 1, 2 and 3 (the three marked as able to change a gate grade): sessions come from the NYSE calendar, not from the dates that carry data; a missing HY, BB or CCC cell returns INSTRUMENT-FAULT, never `None` or a dash; a `since` older than the fetched window faults every unfetched session.
2. Decide findings 4 to 7 as owner (6 is your reading of the five-session CCC rule; 7 is input validation).
3. Until repaired and re-read: do not rest a grade on `--since` output alone. A `--since` row that is PRESENT is sound (no leak, boundaries and ordering verified); the defect is a session that is ABSENT or shown as a dash. Check the listed sessions against the NYSE calendar by hand, or use the default run, which the reader found byte-identical to the prior commit.
4. The completion state stays IMPLEMENTED · TESTED · STILL UNRESOLVED. The repair is consequential (a gate tool, and the defect class has now recurred), so the repaired version owes one more independent read; that will be the second read of this episode.

No level, operator, instrument or consequence of GATE-LIQ-069 is touched by this packet. Your 11/20 L4 FIRED grade and the 11/23 to 11/25 grades are not disputed: the reader confirmed the hidden-fire case is reported.

---

# Independent read: gate069_legs.py `--since` (commit 60a6b6b83c), 2026-11-27

**Verdict: STILL UNRESOLVED.** Condition 4 fails. Condition 1 fails when `since` is older than the FRED fetch window. Conditions 2, 3 and 5 hold under my counterexamples (VERIFIED).

Reviewed: the `grade_since` function (lines 179-192), its CLI wiring (lines 383-384, 407-410, 445-456) and the functions it calls: `grade_l1` (100-114), `grade_l4` (130-176), `prev_session` (89-97), `ser` (363-373) and `fred_fetch` (FORGE/tools/market-data/fetch.py:341, which returns the newest `limit` rows, newest first). The author's selftest passes with `.venv/bin/python3`. It fails to start under the system `python3` because pandas is not installed there.

## Root cause (VERIFIED)
`grade_since` (line 186) builds its list of sessions from the dates that are present in the data: `{d in hy} ∪ {d in bb and d in ccc}`. It does not use the NYSE calendar. The module's own header (lines 22-24, 36-39) says the session must be fixed by the calendar, "never by what the data happens to contain". So a session with no cells is never listed. A session missing only HY gets `g4=None`, and the CLI prints that as `— (no HY obs)` instead of INSTRUMENT-FAULT (line 450-451). A session missing BB or CCC gets `g1=None` and is printed as `—` (line 448).

## Findings ledger

| # | Claim | Artifact | Command run | Observed | Proposed change |
|---|---|---|---|---|---|
| 1 ❌ | A common FRED gap (HY, BB and CCC all missing 11/20) removes the 11/20 session from the `--since` output. The IREN −17.97% / HY +24 fire on that day is never graded, never faulted and never listed. This is the KB-LIQ-164 defect in a new form. Condition 4 fails, and so does condition 3 for this case. | gate069_legs.py:186 | `cx_since.py` CX-A; `cx_cli.py <new> gap1120 --since 2026-11-19` | Pure: `11/20 present in output? False`. CLI: the rows are only `2026-11-23: … L4 INSTRUMENT-FAULT HY obs missing for the required previous session 2026-11-20` and then 11/24 and 11/25 NOT FIRED. The default block grades only 11/25. Nothing anywhere says that the 11/20 session itself went ungraded. | List the sessions as every `is_session(d)` with `since < d <= max(all hy/bb/ccc/equity dates)`. For each one: if `d not in hy`, L4 = INSTRUMENT-FAULT ("no HY obs for session d": a gap, a bond closure or publication still pending). If `d not in bb or d not in ccc`, L1 = INSTRUMENT-FAULT. |
| 2 ❌ | When only HY is missing, the session comes back `g4=None`. The CLI shows it as `— (no HY obs)`, not as INSTRUMENT-FAULT. Condition 4 fails as worded. | gate069_legs.py:190, 450-451 | CX-A2 | `2026-11-20: L1=('NOT FIRED',…) L4=None` | Return a fault dict, `{"state":"INSTRUMENT-FAULT","faults":[f"no HY obs for {d}"]}`, never None. Do the same for L1 at line 189. |
| 3 ❌ | When `since` is older than the fetched window (`ser` uses n=30, about 6 weeks), the sessions between `since` and the first fetched row are missing from the output, with no fault line. Conditions 1 and 4 fail. | gate069_legs.py:186, 394 (`ser(... n=30)` default) | CX-C (`since 2026-11-04`, data from 11/12) | `sessions 11/05..11/11 in output? []`. The output starts at 11/12. The only fault lines are the normal "fewer than 6 CCC" ones, which do not say any sessions were left out. | When `since` is given, fetch enough rows (for example n = sessions since `since` + 10), **and** emit an INSTRUMENT-FAULT row ("not fetched") for every calendar session after `since` that comes before the first HY row plus one. |
| 4 ⚠️ | On Veterans Day 11/11 (NYSE open, bond market shut), an IREN −20% equity session gets no row of its own. Its only trace is the 11/12 fault text ("bond market closed on 2026-11-11 …"). It is not strictly an HY session, but it cannot be graded and should appear as its own row. | gate069_legs.py:186 | CX-B | `11/11 present in output? False`; 11/12 is INSTRUMENT-FAULT and names 11/11 | Fixed by the calendar listing in #1. Label the row "UNGRADEABLE: bond-market closure". |
| 5 ⚠️ | Equity sessions after the latest HY row (publication still pending) are left out of the `--since` block. This is not silent overall: the default block's `⏳ … UNGRADEABLE-PENDING-PUBLICATION` line (430) still names them. | gate069_legs.py:186 | CX-D | `11/25 present in output? False` | Fixed by #1 if equity dates count toward the end of the listing. |
| 6 ⚠️ (inherited, outside the diff) | The CCC "5-session" change is taken over CCC's own observations. A CCC hole therefore stretches the lookback to 6 calendar sessions, and `--since` now shows stretched L1 changes on historical rows. | gate069_legs.py:108-111 | CX-G; CLI gap1120 | Pure: the 11/20 lookback starts from 2026-11-12, while 5 calendar sessions back is 11/13. CLI: `2026-11-23: … CCC 5-sess +67 vs 2026-11-13` (6 sessions). | Owner's call under the WQ-114 letter: either anchor the lookback to `prev_session` applied five times and fault if that cell is missing, or record that "own observations" is the letter. |
| 7 ⚠️ | `--since` is not validated. `2026-11-1` crashes the CLI with a ValueError at line 409. `11/19/2026` is accepted and, because the comparison is on strings, silently grades the whole window. | gate069_legs.py:383-384, 409 | CX-H; `cx_cli.py <new> normal --since 2026-11-1` | `ValueError: Invalid isoformat string: '2026-11-1'`; `since='11/19/2026'` grades from 11/12 | `type=lambda s: date.fromisoformat(s).isoformat()` in argparse. |

## What holds (VERIFIED by my own counterexamples)
- **Condition 2 (no leak from later bars):** with two fires (11/20 IREN and 11/24 APLD −20%, HY +9), `newer == []` for every session. A ticker's 11/25 bar does not reach 11/24 (CX-D, CX-F).
- **Condition 3 (normal case):** the 11/20 fire behind a NOT FIRED 11/23 and 11/24 is reported in both the pure function and the CLI (`cx_cli.py normal`: `2026-11-20 … L4 FIRED (HY +24 …; worst IREN -17.97%)`). When two sessions fire, both are reported, oldest first (CX-F).
- **Boundaries inside `grade_since`:** HY exactly +5 bp with an exact −15.00% move (2.40→2.04) is FIRED; +4 bp is NOT FIRED. BB 220 is NOT FIRED and BB 221 is FIRED. A CCC change of +15 or −15 counts as flat (FIRED); +16 does not (CX-E).
- **"After since":** the comparison is strict `>`. `since = 11/20` gives 11/23 and 11/24. A Saturday `since` works. `since` equal to the last date gives an empty list (CX-H).
- **Thanksgiving carry:** `ser()` drops non-session rows before `grade_since` runs. A carry row passed in directly is faulted by `grade_l4` (lines 141-144). This is covered by existing logic. I did not build a separate case for it.
- **Condition 5 (default run unchanged):** I ran the previous commit's file (`60a6b6b83c^`) and the new file through the same stubbed `main()` with no `--since`, on two scenarios (normal and gap1120). `diff` reports the output as **identical** in both.

## Counterexample scripts
- `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c369a3d5-c32c-4ca0-9f44-4e9982db0939/scratchpad/cx_since.py`: tests the pure `grade_since` (CX-A to CX-H). Run with `cd /home/willi/Research-workspace && .venv/bin/python3 <path>`.
- `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c369a3d5-c32c-4ca0-9f44-4e9982db0939/scratchpad/cx_cli.py`: runs `main()` with FRED and yfinance stubbed. Arguments: `<module file> <normal|gap1120> [--since X]`.
- Snapshots: `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c369a3d5-c32c-4ca0-9f44-4e9982db0939/scratchpad/gate069_prev.py` and `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c369a3d5-c32c-4ca0-9f44-4e9982db0939/scratchpad/gate069_new.py`.
- Default-run diff outputs: `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c369a3d5-c32c-4ca0-9f44-4e9982db0939/scratchpad/def_prev_{normal,gap1120}.txt` and `/tmp/claude-1000/-home-willi-Research-workspace-PROME/c369a3d5-c32c-4ca0-9f44-4e9982db0939/scratchpad/def_new_{normal,gap1120}.txt`.

Key output, CX-A (pure):
```
== CX-A HY+BB+CCC all missing 11/20 (equity session 11/20 has IREN -17.97%)
   2026-11-23: L1=('NOT FIRED', '2026-11-13', 67, None)  L4=('INSTRUMENT-FAULT', None, ['HY obs missing for the required previous session 2026-11-20'])
   2026-11-24: L1=('NOT FIRED', '2026-11-16', 75, None)  L4=('NOT FIRED', 9, [])
   11/20 present in output? False
```

## Not tested
- Live FRED and yfinance calls. Whether real ICE series on FRED ever miss the same day together is UNKNOWN; finding #1's likelihood depends on it, but its logic does not.
- What yfinance actually returns for `start = prev_session(since)`, for example whether the first bar is included and how it handles time zones (UNKNOWN). If the bar for `prev_session(first d)` is missing, `grade_l4` faults it (lines 156-158), so the outcome fails closed (INFERRED).
- A partial `fetch_faults` (an unrequested ticker comes back). By reading line 452, it faults every `--since` row, which fails closed (INFERRED).
- The rest of the file, beyond the paths `--since` calls.


---

## Counterexample script 1: `cx_since.py` (pure function)

```python
import sys, io, contextlib, types
sys.path.insert(0, "/home/willi/Research-workspace/AGENTS/LIQUID/scripts")
import gate069_legs as G
TICK = G.TICK

def show(label, gs):
    print(f"\n== {label}")
    for d, g1, g4 in gs:
        s1 = None if g1 is None else (g1["state"], g1.get("ccc_from"), g1.get("ccc_chg"), g1.get("why"))
        s4 = None if g4 is None else (g4["state"], g4.get("hy_chg"), g4.get("faults"))
        print(f"   {d}: L1={s1}  L4={s4}")

S = ["2026-11-12","2026-11-13","2026-11-16","2026-11-17","2026-11-18","2026-11-19","2026-11-20","2026-11-23","2026-11-24"]
hy = dict(zip(S, [330,332,335,340,347,352,376,363,372]))
bb = dict(zip(S, [190,196,200,204,205,210,229,219,225]))
ccc = dict(zip(S, [1314,1320,1330,1329,1353,1361,1402,1387,1405]))
def eq_with(fire_day, frm=14.41, to=11.82):
    e = {t: {d: 50.0 for d in S} for t in TICK}
    i = S.index(fire_day)
    e["IREN"] = {d: (frm if k < i else to) for k, d in enumerate(S)}
    return e

# CX-A: common FRED gap on 11/20 in HY, BB, CCC; equity has the IREN -17.97% session on 11/20
dropA = lambda s: {k: v for k, v in s.items() if k != "2026-11-20"}
gs = G.grade_since(dropA(bb), dropA(ccc), dropA(hy), eq_with("2026-11-20"), "2026-11-19")
show("CX-A HY+BB+CCC all missing 11/20 (equity session 11/20 has IREN -17.97%)", gs)
print("   11/20 present in output?", any(d == "2026-11-20" for d, _, _ in gs))

# CX-A2: only HY missing 11/20
gs = G.grade_since(bb, ccc, dropA(hy), eq_with("2026-11-20"), "2026-11-19")
show("CX-A2 HY only missing 11/20", gs)

# CX-B: Veterans Day 2026-11-11 (NYSE open, bonds shut), IREN -20% on 11/11
V = ["2026-11-05","2026-11-06","2026-11-09","2026-11-10","2026-11-11","2026-11-12","2026-11-13"]
hyV = {d: 340 + 3*i for i, d in enumerate(V) if d != "2026-11-11"}   # ser() drops the carry row
bbV = {d: 230 for d in hyV}; cccV = {d: 1400 for d in hyV}
eqV = {t: {d: 50.0 for d in V} for t in TICK}
eqV["IREN"] = {d: (20.0 if d < "2026-11-11" else 16.0) for d in V}
gs = G.grade_since(bbV, cccV, hyV, eqV, "2026-11-10")
show("CX-B Veterans Day 11/11 equity session (IREN -20%), since 11/10", gs)
print("   11/11 present in output?", any(d == "2026-11-11" for d, _, _ in gs))

# CX-C: since predates the fetched HY window (ser n=30 newest rows): sessions 11/05..11/11 absent
gs = G.grade_since(bb, ccc, hy, eq_with("2026-11-20"), "2026-11-04")
show("CX-C since 11/04 but first FRED row in window is 11/12", gs)
print("   sessions 11/05..11/11 in output?", [d for d, _, _ in gs if d < "2026-11-12"])

# CX-D: equity bars for 11/25 exist, HY 11/25 not yet published
eD = eq_with("2026-11-20")
for t in TICK: eD[t]["2026-11-25"] = eD[t]["2026-11-24"]
eD["IREN"]["2026-11-25"] = 9.0
gs = G.grade_since(bb, ccc, hy, eD, "2026-11-23")
show("CX-D equity 11/25 (IREN -24%) present, HY 11/25 unpublished", gs)
print("   11/25 present in output?", any(d == "2026-11-25" for d, _, _ in gs))

# CX-E: boundaries inside grade_since: HY exactly +5, equity 2.40 -> 2.04 exactly -15.00%
hyE = dict(hy); hyE["2026-11-20"] = hyE["2026-11-19"] + 5
eE = {t: {d: 50.0 for d in S} for t in TICK}
eE["NBIS"] = {d: (2.40 if d < "2026-11-20" else 2.04) for d in S}
gs = G.grade_since(bb, ccc, hyE, eE, "2026-11-19")
show("CX-E boundary +5bp / -15.00% on 11/20", gs)
hyE4 = dict(hyE); hyE4["2026-11-20"] = hyE["2026-11-19"] + 4
show("CX-E' +4bp / -15.00% on 11/20", G.grade_since(bb, ccc, hyE4, eE, "2026-11-19"))
# L1 boundary: BB exactly 220 vs 221, CCC change exactly 15 vs 16 at 11/20 (5 obs back = 11/12)
for bbv, cchg in [(220,15),(221,15),(221,16),(221,-15)]:
    b = dict(bb); c = dict(ccc); b["2026-11-20"] = bbv; c["2026-11-20"] = c["2026-11-13"] + cchg
    g = {d: g1 for d, g1, _ in G.grade_since(b, c, hy, eq_with("2026-11-20"), "2026-11-19")}["2026-11-20"]
    print(f"   CX-E L1 BB {bbv}, CCC chg {cchg:+d}: {g['state']} (from {g['ccc_from']}, chg {g['ccc_chg']})")

# CX-F: two fires, ordering; later-bar leak check
e2 = eq_with("2026-11-20")
e2["APLD"] = {d: (30.0 if d < "2026-11-24" else 24.0) for d in S}
gs = G.grade_since(bb, ccc, hy, e2, "2026-11-19")
show("CX-F two fires 11/20 (IREN) and 11/24 (APLD -20%, HY +9)", gs)
print("   newer lists:", [(d, g4["newer"]) for d, _, g4 in gs])

# CX-G: CCC missing 11/18 cell; 5-obs lookback at 11/20 then reaches 11/12 (6 sessions)
cG = {k: v for k, v in ccc.items() if k != "2026-11-18"}
g = {d: g1 for d, g1, _ in G.grade_since(bb, cG, hy, eq_with("2026-11-20"), "2026-11-19")}
print("\n== CX-G CCC hole on 11/18: 11/20 L1 ccc_from =", g["2026-11-20"]["ccc_from"], "(calendar 5 sessions back = 2026-11-13)")

# CX-H: since edge inputs
print("\n== CX-H since == last date:", G.grade_since(bb, ccc, hy, eq_with("2026-11-20"), "2026-11-24"))
print("   since Saturday 2026-11-21:", [d for d, _, _ in G.grade_since(bb, ccc, hy, eq_with("2026-11-20"), "2026-11-21")])
print("   since on a session 2026-11-20 (excluded? 'after'):", [d for d, _, _ in G.grade_since(bb, ccc, hy, eq_with("2026-11-20"), "2026-11-20")])
for bad in ["2026-11-1", "11/19/2026"]:
    try:
        print(f"   prev_session({bad!r}) ->", G.prev_session(bad))
    except Exception as ex:
        print(f"   prev_session({bad!r}) raised {type(ex).__name__}: {ex}")
    print(f"   grade_since days with since={bad!r}:", [d for d, _, _ in G.grade_since(bb, ccc, hy, eq_with("2026-11-20"), bad)])

```

## Counterexample script 2: `cx_cli.py` (CLI with FRED and yfinance stubbed)

```python
"""Run main() of a given gate069 copy with FRED and yfinance stubbed. argv: <module file> <scenario> [--since X]"""
import sys, io, contextlib, types, importlib.util
import numpy as np, pandas as pd
path, scen, rest = sys.argv[1], sys.argv[2], sys.argv[3:]
spec = importlib.util.spec_from_file_location("g", path); G = importlib.util.module_from_spec(spec); spec.loader.exec_module(G)
S = ["2026-11-12","2026-11-13","2026-11-16","2026-11-17","2026-11-18","2026-11-19","2026-11-20","2026-11-23","2026-11-24","2026-11-25"]
hy = dict(zip(S, [330,332,335,340,347,352,376,363,372,377]))
bb = dict(zip(S, [190,196,200,204,205,210,229,219,225,228]))
ccc = dict(zip(S, [1314,1320,1330,1329,1353,1361,1402,1387,1405,1417]))
eqcols = {t: [50.0]*len(S) for t in G.TICK}
eqcols["IREN"] = [14.41 if d < "2026-11-20" else 11.82 for d in S]
if scen == "gap1120":   # common ICE/FRED gap on 11/20
    for s in (hy, bb, ccc): s.pop("2026-11-20")
fred = {"BAMLH0A0HYM2": hy, "BAMLH0A1HYBB": bb, "BAMLH0A3HYC": ccc}
idx = pd.to_datetime(S)
frame = pd.DataFrame({t: np.array(v, dtype=np.float32).astype(np.float64) for t, v in eqcols.items()}, index=idx)
yf = types.ModuleType("yfinance"); yf.download = lambda *a, **k: {"Close": frame}
ft = types.ModuleType("fetch")
ft.fred_fetch = lambda sid, limit=30: [{"date": d, "value": f"{v/100:.2f}"} for d, v in sorted(fred[sid].items(), reverse=True)]
sys.modules["yfinance"], sys.modules["fetch"] = yf, ft
sys.argv = ["gate069_legs.py"] + rest
G.main()

```
