#!/usr/bin/env python3
"""
recurrence_rate.py — turn auto-memory `n=` INSTANCE COUNTS into a RATE with a denominator.

WHY THIS EXISTS (PROME, 2026-08-23, Will-directed):
  `n=` counters are monotone instance counts with no denominator, so they cannot answer the
  only question that matters about a banked lesson: **is it recurring MORE or LESS often?**
  A count that only goes up looks like failure even when the rate is falling.
      "the most-banked lesson in the system is also its most-repeated failure"
  was asserted off a bare count and could not be checked. This makes it checkable.

DENOMINATOR — and it is canonical, not invented:
  Will ruled 2026-08-23 that a SESSION is "the context window with that agent for that period,
  before a closeout to get a fresh window" => the observable proxy is AGENT-AUTHORED COMMIT-DAYS
  (same-day commits dedupe to one sitting). This script uses exactly that ruling.
  ⚠️ The proxy UNDERCOUNTS same-day multi-sessions, so true rates are LOWER than reported here.
     The bias has a fixed sign: reported rate is an UPPER BOUND.

⛔ THE CONFOUND, PRINTED WITH EVERY RESULT — do not read a falling rate as improvement alone:
  instances are DETECTED instances. Detection improved materially over this window (peer-review
  culture, new checks). A rising rate may be rising CATCH; a falling rate may be falling ATTENTION.
  This instrument measures recorded-instances-per-session. It does NOT measure error incidence.
  [[finding_ranked_head_sample_is_not_the_population]] · [[finding_measure_actionable_not_gross_rate]]

⛔ KNOWN LIMITATION, v1 — THE NUMERATOR IS UNDER-CAPTURED AND YOU MUST NOT READ AROUND IT:
  instances are parsed from PROSE. The regex catches the `n=<N>, <date>, <AGENT>` form and
  misses everything written another way ("WALTER, three:" under a shared date header, tables,
  inline mentions). Measured on the slug this tool was built for
  (finding_instrument_reports_clean_against_the_wrong_reference): **6 of 16 known instances
  parsed = 38%**, agent-attribution 50%. So:
      → the reported RATE is a LOWER BOUND on recorded instances
      → and combined with the session-proxy bias (below) the two errors point OPPOSITE ways
      → ⛔ DO NOT quote a level from this tool. Trends within one slug are the usable output,
        and only where the parse rate is stable across the compared periods.
  THE FIX IS CHEAP AND IT IS THE SAME FIX AS THE UNDERLYING PROBLEM: append instances with a
  structured first line — `n=<N> | <YYYY-MM-DD> | <AGENT> | <one-line form>` — then the parse
  rate goes to ~100% forward and this tool becomes trustworthy without touching history.
  ⚠️ Nothing here should be backfilled by hand: a hand-rebuilt numerator is a new claim with
  no independent check ([[finding_loadbearing_number_must_be_reproducible]]).

USAGE
  python3 PROME/tools/recurrence_rate.py                 # fleet-wide, by ISO week
  python3 PROME/tools/recurrence_rate.py --slug <name>   # one memory
  python3 PROME/tools/recurrence_rate.py --by-agent      # per-agent recurrence (repeat vs first-time)
"""
import re, subprocess, argparse, collections, datetime, pathlib, sys

ROOT = pathlib.Path(subprocess.run(["git","rev-parse","--show-toplevel"],
                    capture_output=True,text=True).stdout.strip())
MEM = ROOT/"memory"/"auto"
AGENT = re.compile(r"\b([A-Z][A-Z0-9_]{2,11})\b")
# instance marker: n=N ... ISO-date ... (optional AGENT)
INST = re.compile(r"n=(\d+)[^\n]{0,40}?(\d{4}-\d{2}-\d{2})([^\n]{0,90})")
NOT_AGENTS = {"THE","AND","NOT","BUT","FOR","ONE","TWO","ALL","NEW","OLD","ITS","WAS","HAS",
              "PAT","KB","VX","ISO","UTC","ET","YES","NO","N","EVENING","MORNING","SAME","DAY",
              "FIVE","FOUR","THREE","SIX","SEVEN","EIGHT","NINE","TEN","FORM","INSTANCE","WRONG",
              "ARTIFACT","SCOPE","NAME","LABEL","QUANTITY","COVERAGE","DEPENDENCY","AUTHORSHIP"}

def roster():
    out = subprocess.run(["git","log","--format=%s"],capture_output=True,text=True,cwd=ROOT).stdout
    c = collections.Counter()
    for line in out.splitlines():
        m = re.match(r"^([A-Z][A-Z0-9_]{2,11})(?![A-Za-z])", line)
        if m: c[m.group(1)] += 1
    return {a for a,n in c.items() if n >= 5 and a not in NOT_AGENTS}

def sessions_by_week(agents):
    """denominator: agent-authored COMMIT-DAYS per ISO week (Will's ruled session proxy)"""
    out = subprocess.run(["git","log","--format=%ad|%s","--date=short"],
                         capture_output=True,text=True,cwd=ROOT).stdout
    seen, per_agent = set(), collections.Counter()
    for line in out.splitlines():
        if "|" not in line: continue
        d, s = line.split("|",1)
        m = re.match(r"^([A-Z][A-Z0-9_]{2,11})(?![A-Za-z])", s)
        if not m or m.group(1) not in agents: continue
        key = (m.group(1), d)
        if key in seen: continue
        seen.add(key); per_agent[m.group(1)] += 1
    weeks = collections.Counter()
    for a, d in seen:
        weeks[datetime.date.fromisoformat(d).isocalendar()[:2]] += 1
    return weeks, per_agent, seen

def instances(agents, slug=None):
    rows = []
    files = [MEM/f"{slug}.md"] if slug else sorted(MEM.glob("*.md"))
    for f in files:
        if not f.exists(): continue
        try: txt = f.read_text(encoding="utf-8")
        except Exception: continue
        for m in INST.finditer(txt):
            n, date, tail = m.group(1), m.group(2), m.group(3)
            who = [a for a in AGENT.findall(tail) if a in agents]
            rows.append({"slug": f.stem, "n": int(n), "date": date,
                         "agent": who[0] if who else None})
    return rows

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug"); ap.add_argument("--by-agent", action="store_true")
    a = ap.parse_args()
    agents = roster()
    weeks, per_agent_sessions, _ = sessions_by_week(agents)
    rows = instances(agents, a.slug)
    if not rows:
        print("no dated n= instances found"); return 0

    print("="*78)
    print("  RECURRENCE RATE — recorded instances per 100 agent-sessions")
    print("  denominator = agent-authored COMMIT-DAYS (Will's ruled session definition, 8/23)")
    print("="*78)
    attributed = sum(1 for r in rows if r["agent"])
    print(f"  instances parsed: {len(rows)}   attributed to an agent: {attributed}"
          f"  ({100*attributed//max(1,len(rows))}%)   slugs: {len({r['slug'] for r in rows})}")
    print(f"  ⚠️  {len(rows)-attributed} instance(s) carry no parseable agent — counted in the")
    print( "      fleet rate, EXCLUDED from the per-agent table. Not silently dropped.\n")

    byweek = collections.Counter()
    for r in rows: byweek[datetime.date.fromisoformat(r["date"]).isocalendar()[:2]] += 1
    print(f"  {'ISO week':<12}{'instances':>10}{'sessions':>10}{'per-100':>10}   trend")
    print("  " + "-"*54)
    prev = None
    for wk in sorted(set(byweek) | set(weeks)):
        i, s = byweek.get(wk,0), weeks.get(wk,0)
        if s == 0: continue
        rate = 100.0*i/s
        arrow = "" if prev is None else ("↑ rising" if rate > prev*1.15 else
                                         "↓ falling" if rate < prev*0.85 else "→ flat")
        print(f"  {wk[0]}-W{wk[1]:<7}{i:>10}{s:>10}{rate:>10.1f}   {arrow}")
        prev = rate

    if a.by_agent:
        print("\n  PER-AGENT — the repeat-vs-first-time question, which a bare count cannot answer")
        print(f"  {'agent':<10}{'instances':>10}{'sessions':>10}{'per-100':>10}   {'dates'}")
        print("  " + "-"*66)
        byagent = collections.defaultdict(list)
        for r in rows:
            if r["agent"]: byagent[r["agent"]].append(r["date"])
        for ag, ds in sorted(byagent.items(), key=lambda kv: -len(kv[1])):
            s = per_agent_sessions.get(ag,0)
            rate = f"{100.0*len(ds)/s:.1f}" if s else "n/a"
            uniq = sorted(set(ds))
            tag = "REPEATER" if len(uniq) > 1 else "first-time"
            print(f"  {ag:<10}{len(ds):>10}{s:>10}{rate:>10}   {tag}: {', '.join(uniq[:4])}")

    print("\n" + "="*78)
    print("  ⛔ READ THE CONFOUND BEFORE ACTING ON THE TREND")
    print("     These are DETECTED instances. Detection improved materially over this window.")
    print("     A rising rate may be rising CATCH; a falling rate may be falling ATTENTION.")
    print("     This measures recorded-instances-per-session, NOT error incidence.")
    print("  ⚠️  Denominator UNDERCOUNTS same-day multi-sessions => rates here are UPPER BOUNDS.")
    print("="*78)
    return 0

if __name__ == "__main__":
    sys.exit(main())
