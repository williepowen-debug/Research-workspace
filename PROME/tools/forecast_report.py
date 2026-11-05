#!/usr/bin/env python3
"""forecast_report.py — the monthly forecasting report (WQ-619 A, Will 2026-11-05).

A REPORT, not a gate or checker: always exits 0 on a completed read; edits no ledger.
Reuses DAEDALUS's ledger registry (scorecards/LEDGERS.tsv) and status map (scorecard.bucket),
so one mapping serves both surfaces. Desks missing from that registry are listed in EXTRA.

  python3 PROME/tools/forecast_report.py [--write PATH] [--sample N --seed S --sample-out PATH] [--selftest]

Per-desk Brier is deliberately NOT printed: the first report proves grading consistency,
no desk ranking (WQ-619 A). Fleet tables carry n, exclusions and a 95% Wilson interval.
"""
import argparse, csv, datetime as dt, importlib.util, json, math, os, random, re, subprocess, sys

ROOT = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
EXTRA = ["AGENTS/CYPHER/workbook/PREDICTIONS.tsv", "AGENTS/GIBBS/workbook/PREDICTIONS.tsv",
         "AGENTS/ISHM/workbook/PREDICTIONS.tsv", "AGENTS/VIOLET/workbook/PREDICTIONS.tsv"]
NOT_READ = "CARL and MARCO sub-agent ledgers, NEXUS markdown monitors, TERRY CALIBRATION.tsv, ORACLE, REGINALD's EGBN research copy; CORAL and SHADE have no ledger"
PCT = re.compile(r"(?<![\d.])(\d{1,3}(?:\.\d+)?)\s*(?:%|pct\b)")
# Unambiguous typed forms scorecard.TOKEN_MAP leaves UNMAPPED; a local reading, the owner's map is not edited.
LOCAL = {"RESOLVED-HIT": "HIT", "RESOLVED-CONFIRMED": "HIT", "RESOLVED-CONFIRM": "HIT", "RESOLVED-MISS": "MISS"}
DEC = re.compile(r"P\(TRUE[^)]*\)\s*=\s*(0?\.\d+)")


def load_bucket():
    p = os.path.join(ROOT, "AGENTS/DAEDALUS/scripts/scorecard.py")
    sys.path.insert(0, os.path.dirname(p))
    sp = importlib.util.spec_from_file_location("scorecard", p)
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return m.bucket


def registry():
    rows = []
    with open(os.path.join(ROOT, "AGENTS/DAEDALUS/scorecards/LEDGERS.tsv"), encoding="utf8") as f:
        for l in f:
            if l.startswith("#") or l.startswith("path\t") or not l.strip():
                continue
            c = l.rstrip("\n").split("\t")
            rows.append((c[0], c[1], c[4]))
    have = {r[0] for r in rows}
    for p in EXTRA:
        if p not in have and os.path.exists(os.path.join(ROOT, p)):
            rows.append((p, "Status", "Outcome"))
    return rows


def prob(conf, pred=""):
    """Latest dated mark governs scoring (WQ-112): the first figure in the cell. '(was X%)' is first-call."""
    s = conf or ""
    if re.match(r"\s*(UNSCORED|NOT SCORED|PROVISIONAL|UNASSIGNED|ASSUMPTION|\(unstated\)|—|-\s*$)", s, re.I):
        return None
    rg = re.match(r"\s*(\d{1,3})\s*-\s*(\d{1,3})\s*(?:%|pct\b)", s)
    if rg:
        return (float(rg.group(1)) + float(rg.group(2))) / 200
    m = re.search(r"SCORE AT\s*" + PCT.pattern, s, re.I) or PCT.search(s)
    if m:
        v = float(m.group(1)) / 100
    else:
        m = DEC.search(s) or DEC.search(pred or "")
        if not m:
            return None
        v = float(m.group(1))
    return v if 0 < v <= 1 else None


def first_call(conf):
    m = re.search(r"\(was\s+" + PCT.pattern, conf or "", re.I)
    return float(m.group(1)) / 100 if m else None


def norm_rows(path):
    txt = open(os.path.join(ROOT, path), encoding="utf8", errors="replace").read().splitlines()
    L = [l for l in txt if l.strip() and not l.startswith("#")]
    if not L:
        return [], []
    hdr = [h.strip() for h in L[0].split("\t")]
    return hdr, [l.split("\t") for l in L[1:]]


def owner_events(path):
    """A desk's own '# CONVENTION' line may state event outcomes by ID: EVENT HAPPENED: X-01 06 ... / EVENT DID NOT HAPPEN: ..."""
    out = {}
    for l in open(os.path.join(ROOT, path), encoding="utf8", errors="replace"):
        if not l.startswith("# CONVENTION"):
            continue
        for label, val in (("EVENT HAPPENED", "HIT"), ("EVENT DID NOT HAPPEN", "MISS"), ("UNREADABLE", "RESOLVED-UNTYPED")):
            m = re.search(label + r":\s*([^.:]*?)(?:[.,]|$)", l)
            if not m:
                continue
            pre = None
            for tok in m.group(1).split():
                k = re.match(r"([A-Z]+-)?(\d+)$", tok)
                if not k:
                    continue
                pre = k.group(1) or pre
                out[f"{pre}{k.group(2)}"] = val
    return out


def col(hdr, name, *alts):
    low = [h.lower() for h in hdr]
    for n in (name,) + alts:
        if n and n.lower() in low:
            return low.index(n.lower())
    for n in alts:
        for i, h in enumerate(low):
            if n and n.lower() in h:
                return i
    return None


def read_all(bucket):
    out, defects = [], []
    for path, sc, oc in registry():
        if not os.path.exists(os.path.join(ROOT, path)):
            defects.append((path, "missing file"))
            continue
        hdr, rows = norm_rows(path)
        if not hdr:
            continue
        ist = col(hdr, sc, "status", "state")
        iout = col(hdr, oc, "outcome", "result", "resolution")
        icf = col(hdr, "Confidence", "conf_tier", "conf", "prob")
        imd = col(hdr, "Date_Made", "made", "Date")
        ipr = col(hdr, "Prediction", "prediction")
        if ist is None:
            defects.append((path, "no status column"))
            continue
        desk = path.split("/")[1]
        stated = owner_events(path)
        for c in rows:
            g = lambda i: c[i].strip() if i is not None and i < len(c) else ""
            if not c[0].strip():
                continue
            st, o = g(ist), g(iout)
            if re.match(r"^(ID|Pred_ID|id)$", c[0].strip()):
                continue
            b = LOCAL.get(re.sub(r"[-_ ]+", "-", st.upper()).split(" ")[0]) or bucket(st)
            basis = "status"
            if b == "RESOLVED-UNTYPED":
                b2 = bucket(re.sub(r"^[^A-Za-z]+", "", o))
                if b2 in ("HIT", "MISS", "PARTIAL", "NO-VERDICT", "ANNULLED"):
                    b, basis = b2, "outcome"
            if c[0].strip() in stated:
                b, basis = stated[c[0].strip()], "owner-convention"
            out.append({"desk": desk, "id": c[0].strip(), "status": st, "outcome": o, "conf": g(icf),
                        "pred": g(ipr), "made": g(imd), "bucket": b or "OPEN", "basis": basis,
                        "p": prob(g(icf), g(ipr)), "first": first_call(g(icf))})
    return out, defects


def wilson(y, n, z=1.96):
    if not n:
        return (0, 0)
    p = y / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def render(rows, defects):
    P = []
    now = dt.datetime.now().strftime("%Y-%m-%d")
    cnt = lambda b: sum(1 for r in rows if r["bucket"] == b)
    dec = [r for r in rows if r["bucket"] in ("HIT", "MISS")]
    sc = [r for r in dec if r["p"] is not None]
    P.append(f"**Rows read:** {len(rows)} across {len({r['desk'] for r in rows})} desks, as of {now}. "
             f"Open {cnt('OPEN')} · HIT {cnt('HIT')} · MISS {cnt('MISS')} · PARTIAL {cnt('PARTIAL')} · NO-VERDICT {cnt('NO-VERDICT')} · "
             f"ANNULLED {cnt('ANNULLED')} · RESOLVED-UNTYPED {cnt('RESOLVED-UNTYPED')} · UNMAPPED {cnt('UNMAPPED')}.")
    P.append(f"**Scored:** {len(sc)} of {len(dec)} decided calls carry a usable probability; {len(dec)-len(sc)} do not. "
             f"{sum(1 for r in dec if r['basis']=='outcome')} decided rows took their direction from the Outcome cell, the status alone said RESOLVED.")
    P.append(f"**Not read:** {NOT_READ}.")
    if defects:
        P.append("**Ledger read defects:** " + " · ".join(f"{a}: {b}" for a, b in defects))
    if sc:
        br = sum((r["p"] - (r["bucket"] == "HIT")) ** 2 for r in sc) / len(sc)
        hr = sum(r["bucket"] == "HIT" for r in sc) / len(sc)
        ref = hr * (1 - hr)
        P.append(f"\n**Fleet Brier {br:.3f}** on n={len(sc)}. Always saying 50%: 0.250. Always saying the fleet hit rate ({hr:.0%}): {ref:.3f}. "
                 f"The second is the fairer baseline; beating it is what would show the percentages add information. Neither is a skill claim while calls overlap.")
        rng = random.Random(619); d = []
        for _ in range(2000):
            bs = [sc[rng.randrange(len(sc))] for _ in sc]
            h = sum(r["bucket"] == "HIT" for r in bs) / len(bs)
            d.append(h * (1 - h) - sum((r["p"] - (r["bucket"] == "HIT")) ** 2 for r in bs) / len(bs))
        d.sort()
        P.append(f"**Gain over the hit-rate baseline:** {ref-br:+.3f}, bootstrap 95% range {d[50]:+.3f} to {d[1949]:+.3f}, treating calls as independent, which overstates certainty because many calls share one root.")
        P.append("Scored on the latest pre-outcome probability (WQ-112), which measures the final forecast; it may differ from the original early judgment, which stays preserved in each row.")
        mids = [r for r in sc if re.match(r"\s*\d{1,3}\s*-\s*\d{1,3}\s*(?:%|pct)", r["conf"])]
        own = [r for r in sc if r["basis"] == "owner-convention"]
        P.append(f"**Disclosures:** {len(mids)} probability range(s) converted to a midpoint ({', '.join(r['id'] for r in mids) or 'none'}); {len(own)} scored rows take the event outcome from a later owner clarification, not from an independently verified outcome.")
        P.append("\n| Stated | Calls | Mean stated | Came true | 95% interval |\n|---|---:|---:|---:|---|")
        for lo, hi, lab in ((0, .3, "Under 30%"), (.3, .5, "30–49%"), (.5, .7, "50–69%"), (.7, .9, "70–89%"), (.9, 1.01, "90%+")):
            s = [r for r in sc if lo <= r["p"] < hi]
            y = sum(r["bucket"] == "HIT" for r in s)
            a, b = wilson(y, len(s))
            ms = sum(r["p"] for r in s) / len(s) if s else 0
            P.append(f"| {lab} | {len(s)} | {ms:.0%} | {(y/len(s) if s else 0):.0%} | {a:.0%} to {b:.0%} |")
    P.append("\n## Desk counts, alphabetical. Counts only, no desk score, no ranking\n")
    P.append("| Desk | Rows | Open | Decided | With a % | No-verdict | Annulled | Partial | Untyped or unmapped |\n|---|---:|---:|---:|---:|---:|---:|---:|---:|")
    for d in sorted({r["desk"] for r in rows}):
        R = [r for r in rows if r["desk"] == d]
        c = lambda *bs: sum(1 for r in R if r["bucket"] in bs)
        P.append(f"| {d} | {len(R)} | {c('OPEN')} | {c('HIT','MISS')} | {sum(1 for r in R if r['bucket'] in ('HIT','MISS') and r['p'] is not None)} | {c('NO-VERDICT')} | {c('ANNULLED')} | {c('PARTIAL')} | {c('RESOLVED-UNTYPED','UNMAPPED')} |")
    return "\n".join(P) + "\n"


def selftest():
    cases = [("55% [2026-11-05]", .55), ("5% [2026-07-23] (was 30% [2026-07-02])", .05), ("50pct", .5),
             ("UNSCORED-AS-MADE", None), ("PROVISIONAL", None), ("SCORE AT 40% [2026-01-01] -- x", .4), ("—", None)]
    bad = [(c, prob(c)) for c, w in cases if prob(c) != w]
    assert prob("57-60pct") == .585
    assert prob("", "P(TRUE | a verdict) = 0.60. x") == .6
    assert first_call("5% [2026-07-23] (was 30% [2026-07-02])") == .3
    a, b = wilson(5, 10)
    assert round(a, 2) == .24 and round(b, 2) == .76
    print("selftest", "FAIL " + str(bad) if bad else "PASS", len(cases) + 3)
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write"); ap.add_argument("--sample", type=int); ap.add_argument("--seed", type=int, default=619)
    ap.add_argument("--sample-out"); ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    rows, defects = read_all(load_bucket())
    body = render(rows, defects)
    if a.write:
        open(a.write, "w", encoding="utf8").write(body)
    print(body)
    if a.sample:
        pop = [r for r in rows if r["bucket"] != "OPEN"]
        s = random.Random(a.seed).sample(pop, a.sample)
        json.dump(s, open(a.sample_out, "w", encoding="utf8"), ensure_ascii=False, indent=0)
    return 0


if __name__ == "__main__":
    sys.exit(main())
