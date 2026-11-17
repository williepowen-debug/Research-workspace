#!/usr/bin/env python3
"""forecast_report.py — the monthly forecasting report (WQ-619 A, Will 2026-11-05).

A REPORT, not a gate or checker: always exits 0 on a completed read; edits no ledger.
Reuses DAEDALUS's ledger registry (scorecards/LEDGERS.tsv) and status map (scorecard.bucket),
so one mapping serves both surfaces. Desks missing from that registry are listed in EXTRA.

  python3 PROME/tools/forecast_report.py [--write PATH] [--no-history] [--sample N --seed S --sample-out PATH] [--selftest]

Timing and first-logged probability (2026-11-17, acceptance file
PROME/tools/tests/ACCEPTANCE_forecast_report_timing_archives_2026-11-17.md) come from each row's GIT RECORD:
every committed version of the desk's prediction ledgers that holds the row. The row's own Date_Made cell
is never used as a bound or as evidence of timing. Forward only: rows known on or before REPORT1_CUT are
report 1's closed population and are counted, not classed.

Per-desk Brier is deliberately NOT printed: the first report proves grading consistency,
no desk ranking (WQ-619 A). Fleet tables carry n, exclusions and a 95% Wilson interval.
"""
import argparse, csv, datetime as dt, glob, importlib.util, json, math, os, random, re, subprocess, sys, zoneinfo

# FORECAST_REPORT_ROOT points the tool at a fixture repository (tests and independent readers); unset, it reads this one.
ROOT = os.environ.get("FORECAST_REPORT_ROOT") or subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
EXTRA = ["AGENTS/CYPHER/workbook/PREDICTIONS.tsv", "AGENTS/GIBBS/workbook/PREDICTIONS.tsv",
         "AGENTS/ISHM/workbook/PREDICTIONS.tsv", "AGENTS/VIOLET/workbook/PREDICTIONS.tsv"]
# Resolved calls a desk rotated out of its live ledger. Patterns, not file lists: a new archive file is read when it appears.
ARCHIVE_GLOBS = ["AGENTS/BOND/thesis/archive/PREDICTIONS_resolved_*.tsv", "AGENTS/VULCAN/archive/PREDICTIONS_RESOLVED_*.tsv",
                 "AGENTS/WATT/workbook/PREDICTIONS_ARCHIVE.tsv"]
REPORT1_CUT = dt.date(2026, 11, 5)   # report 1's population is closed (Will 2026-11-05); timing classes start after it
ET = zoneinfo.ZoneInfo("America/New_York")
ISO = re.compile(r"(20\d\d)-(\d\d)-(\d\d)")
NOT_READ = "CARL and MARCO sub-agent ledgers, NEXUS markdown monitors, TERRY CALIBRATION.tsv, ORACLE, REGINALD's EGBN research copy"
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


def registry_full():
    """[(path, status_col, outcome_col, date_col, date_source, kind)]: DAEDALUS's registry, then EXTRA, then archive patterns."""
    rows = []
    with open(os.path.join(ROOT, "AGENTS/DAEDALUS/scorecards/LEDGERS.tsv"), encoding="utf8") as f:
        for l in f:
            if l.startswith("#") or l.startswith("path\t") or not l.strip():
                continue
            c = l.rstrip("\n").split("\t")
            rows.append((c[0], c[1], c[4], c[2], c[3], "registry"))
    have = {r[0] for r in rows}
    for p in EXTRA:
        if p not in have and os.path.exists(os.path.join(ROOT, p)):
            rows.append((p, "Status", "Outcome", "Date_Resolved", "COLUMN", "extra"))
            have.add(p)
    for pat in ARCHIVE_GLOBS:
        for full in sorted(glob.glob(os.path.join(ROOT, pat))):
            p = os.path.relpath(full, ROOT)
            if p not in have:
                rows.append((p, "Status", "Outcome", "Date_Resolved", "COLUMN", "archive"))
                have.add(p)
    return rows


def registry():
    return [(r[0], r[1], r[2]) for r in registry_full()]


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


def oldest_was(conf):
    """Cells are written newest first, so the LAST '(was X%)' is the oldest mark the cell still carries."""
    m = re.findall(r"\(was\s+" + PCT.pattern, conf or "", re.I)
    v = float(m[-1]) / 100 if m else None
    return v if v is not None and 0 < v <= 1 else None


def parse_iso(s):
    m = ISO.search(s or "")
    try:
        return dt.date(*map(int, m.groups())) if m else None
    except ValueError:
        return None


def full_dates(s):
    """Full dates only (YYYY-MM-DD, M/D/YY, M/D/YYYY). No lower bound is applied: the caller compares, never Date_Made."""
    out = set()
    for y, m, d in ISO.findall(s or ""):
        try: out.add(dt.date(int(y), int(m), int(d)))
        except ValueError: pass
    for m, d, y in re.findall(r"(?<![\d/.$-])(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})(?![\d/%])", s or ""):
        try: out.add(dt.date(int(y) + (2000 if len(y) == 2 else 0), int(m), int(d)))
        except ValueError: pass
    return out


def split_ledger(text):
    L = [l for l in text.splitlines() if l.strip() and not l.startswith("#")]
    if not L:
        return [], []
    return [h.strip() for h in L[0].split("\t")], [l.split("\t") for l in L[1:]]


def classify(st, o, bucket):
    """(bucket or None, basis) from a status cell and an outcome cell. None = not decided."""
    b = LOCAL.get(re.sub(r"[-_ ]+", "-", st.upper()).split(" ")[0]) or bucket(st)
    basis = "status"
    if b == "RESOLVED-UNTYPED":
        b2 = bucket(re.sub(r"^[^A-Za-z]+", "", o))
        if b2 in ("HIT", "MISS", "PARTIAL", "NO-VERDICT", "ANNULLED"):
            b, basis = b2, "outcome"
    return b, basis


def norm_rows(path):
    return split_ledger(open(os.path.join(ROOT, path), encoding="utf8", errors="replace").read())


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
    seen = {}
    for path, sc, oc, dc, dsrc, kind in registry_full():
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
        idt = col(hdr, dc, "Date_Resolved", "Resolution_Date") if dsrc == "COLUMN" and dc != "NONE" else None
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
            b, basis = classify(st, o, bucket)
            if c[0].strip() in stated:
                b, basis = stated[c[0].strip()], "owner-convention"
            key = (desk, c[0].strip())
            if key in seen and seen[key] != path:      # one ID in a live and an archive file: the first file read wins
                defects.append((path, f"{c[0].strip()} already read from {seen[key]}, counted once"))
                continue
            seen.setdefault(key, path)
            out.append({"desk": desk, "id": c[0].strip(), "status": st, "outcome": o, "conf": g(icf),
                        "pred": g(ipr), "made": g(imd), "bucket": b or "OPEN", "basis": basis,
                        "p": prob(g(icf), g(ipr)), "first": first_call(g(icf)), "path": path, "kind": kind,
                        "resolved": parse_iso(g(idt)) if idt is not None else parse_iso(o)})
    return out, defects


DECIDED = ("HIT", "MISS", "PARTIAL", "NO-VERDICT", "ANNULLED", "RESOLVED-UNTYPED")


def is_decided(b, status, resolved=None):
    """Decided in a committed version. scorecard.bucket returns UNMAPPED, not None, for every status outside its six
    open prefixes, open-type (STUCK, AT-RISK, RESOLVING ...) and final (LIKELY MISSED, GRADED-MIXED, KILLED ...) alike.
    An UNMAPPED status counts as decided when its token begins RESOLVED, or when that same version carries a resolved
    date: an owner dates a row when it is finished, and leaves the date empty while it is open."""
    return b in DECIDED or (b == "UNMAPPED" and ((status or "").strip().upper().startswith("RESOLVED") or resolved is not None))


def norm_text(x):
    return re.sub(r"\s+", " ", (x or "").lower()).strip()


def same_call(a, b):
    """Two committed versions of one row ID are a DIFFERENT call only when the prediction text changes at its start
    (word-sequence similarity of the first 12 words under 0.5) AND the probability or the Date_Made date changes with it.
    Text alone is not enough: owners extend a row's wording, and replace a resolved row's text with an archive pointer.
    A date alone is not enough: owners correct a mistyped Date_Made. Date_Made is used here only to tell calls apart."""
    if not (a[6] and b[6]) or a[6] == b[6]:
        return True
    import difflib
    wa, wb = re.findall(r"[a-z0-9]+", a[6])[:12], re.findall(r"[a-z0-9]+", b[6])[:12]   # words, not characters
    if difflib.SequenceMatcher(None, wa, wb).ratio() >= .5:
        return True
    da, db = parse_iso(a[5]), parse_iso(b[5])
    moved_date = bool(da and db and da != db)
    moved_p = a[2] is not None and b[2] is not None and abs(a[2] - b[2]) >= .0015
    return not (moved_date or moved_p)


def current_call(versions):
    """(the trailing run of versions that are the call scored today, True if earlier versions under the same ID were a different call)."""
    i = len(versions) - 1
    while i > 0 and same_call(versions[i - 1], versions[i]):
        i -= 1
    return versions[i:], i > 0


def git(*a):
    return subprocess.run(("git", "-C", ROOT) + a, capture_output=True, text=True, errors="replace").stdout


def file_history(path, sc, oc, bucket, dc="Date_Resolved", dsrc="COLUMN"):
    """{row id: [(commit time, ET date, probability, decided, oldest-was, Date_Made cell, prediction text, resolved date)]} over every
    committed version, following renames. A version whose header has no status column or no confidence column
    contributes nothing: no probability and no decided mark."""
    vers, cur = [], None
    # No --reverse: with --follow, git applies --reverse before following and returns the creation commit alone
    # (seen 2026-11-17: 1 commit of 49). Read newest first, then turn the list round.
    for l in git("log", "--follow", "--format=@%H %ct", "--name-only", "--", path).splitlines():
        if l.startswith("@"):
            sha, ct = l[1:].split()
            cur = [sha, int(ct), None]
            vers.append(cur)
        elif l.strip() and cur:
            cur[2] = l.strip()
    vers.reverse()
    h = {}
    if not vers:
        return h
    cat = subprocess.Popen(["git", "-C", ROOT, "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    for sha, ct, name in vers:
        cat.stdin.write(f"{sha}:{name or path}\n".encode()); cat.stdin.flush()
        head = cat.stdout.readline().split()
        if len(head) < 3 or head[1] != b"blob":
            continue
        blob = cat.stdout.read(int(head[2])).decode("utf8", "replace"); cat.stdout.read(1)
        hdr, rows = split_ledger(blob)
        if not hdr:
            continue
        ist = col(hdr, sc, "status", "state"); iout = col(hdr, oc, "outcome", "result", "resolution")
        icf = col(hdr, "Confidence", "conf_tier", "conf", "prob"); ipr = col(hdr, "Prediction", "prediction")
        imd = col(hdr, "Date_Made", "made", "Date")
        idt = col(hdr, dc, "Date_Resolved", "Resolution_Date") if dsrc == "COLUMN" and dc != "NONE" else None
        if ist is None or icf is None:
            continue
        day = dt.datetime.fromtimestamp(ct, ET).date()
        for c in rows:
            g = lambda i: c[i].strip() if i is not None and i < len(c) else ""
            rid = c[0].strip()
            if not rid:
                continue
            b = classify(g(ist), g(iout), bucket)[0]
            res = parse_iso(g(idt)) if idt is not None else parse_iso(g(iout))   # the registry's date rule, applied to this version
            dec = is_decided(b, g(ist), res)
            h.setdefault(rid, []).append((ct, day, prob(g(icf), g(ipr)), dec, oldest_was(g(icf)), g(imd), norm_text(g(ipr)), res if dec else None))
    cat.stdin.close(); cat.wait()
    return h


def git_records(bucket):
    """{(desk, row id): versions oldest first}: the union across every ledger file of the desk, live and archive."""
    rec = {}
    for path, sc, oc, dc, ds, _k in registry_full():
        if not os.path.exists(os.path.join(ROOT, path)):
            continue
        desk = path.split("/")[1]
        for rid, v in file_history(path, sc, oc, bucket, dc, ds).items():
            rec.setdefault((desk, rid), []).extend(v)
    for v in rec.values():
        v.sort(key=lambda x: x[0])
    return rec


def timing(versions, p, resolved, outcome=""):
    """One class per scored row from its git record. Date_Made is not an input.
    versions: [(commit time, date, probability, decided, oldest-was)] oldest first; p: the probability the report scores with."""
    out = {"cls": None, "first_record": None, "value_date": None, "known": None, "p0": None, "look": None, "restarted": False}
    if versions and len(versions[0]) > 6:
        versions, out["restarted"] = current_call(versions)
    if not versions:
        out["cls"] = "NO-GIT-RECORD"
        out["known"] = resolved
        return out
    out["first_record"] = versions[0][1]
    for v in versions:
        if v[2] is not None:
            out["p0"] = v[4] if v[4] is not None else v[2]
            break
    decided = [v[1] for v in versions if v[3]]
    carried = [v[7] for v in versions if len(v) > 7 and v[3] and v[7] is not None]   # resolved dates decided versions carried, in case the live date was moved later
    known = min([d for d in (resolved, decided[0] if decided else None, min(carried) if carried else None) if d is not None], default=None)
    out["known"] = known
    vd = next((v[1] for v in versions if v[2] is not None and p is not None and abs(v[2] - p) < .0015), None)
    out["value_date"] = vd
    if versions[0][3]:
        out["cls"] = "BORN-DECIDED"
    elif vd is None:
        out["cls"] = "NO-GIT-RECORD"
    elif known is None:
        out["cls"] = "NO-KNOWN-DATE"
    elif vd > known:
        out["cls"] = "AFTER"
    elif vd == known:
        out["cls"] = "SAME-DAY"
    else:
        out["cls"] = "BEFORE"
        early = [d for d in full_dates(outcome) if d < vd]
        if early:
            out["look"] = min(early)
    return out


def unread_ledgers(read_paths):
    """Prediction-named .tsv files under AGENTS/ that no registry row, EXTRA entry or archive pattern reads."""
    names = [l for l in git("ls-files", "AGENTS").splitlines() if re.search(r"PREDICTIONS[^/]*\.tsv$", l, re.I)]
    return sorted(set(names) - set(read_paths))


def wilson(y, n, z=1.96):
    if not n:
        return (0, 0)
    p = y / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def brier(pairs):
    return sum((p - hit) ** 2 for p, hit in pairs) / len(pairs)


def render(rows, defects, rec=None, unread=None):
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
    arch = sorted({r["path"] for r in rows if r.get("kind") == "archive"})
    if arch:
        P.append(f"**Archive ledgers read:** {len(arch)} files, {sum(1 for r in rows if r.get('kind') == 'archive')} rows: " + ", ".join(arch) + ".")
    if unread is not None:
        P.append(f"**Prediction-named ledger files not read:** {len(unread)}" + (": " + ", ".join(unread) if unread else "")
                 + ". Snapshots and copies belong in this list; a rotated archive of resolved calls does not, and one found here is a gap in the score.")
    if defects:
        P.append("**Ledger read notes:** " + " · ".join(f"{a}: {b}" for a, b in defects))
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
        if rec is None:
            P.append("\n**Timing table and first-logged score: SKIPPED (--no-history).** Nothing in this report says whether any call was logged before its outcome.")
        else:
            T = [(r, timing(rec.get((r["desk"], r["id"]), []), r["p"], r.get("resolved"), r["outcome"])) for r in sc]
            fwd = [(r, t) for r, t in T if t["known"] is None or t["known"] > REPORT1_CUT]
            P.append(f"\n## When the probability used entered the record: calls known after {REPORT1_CUT}, forward only\n")
            P.append("Read from each row's git record: every committed version of the desk's prediction ledgers, live and archive, that holds the row. "
                     "Value date is the first commit date carrying the probability scored. Known date is the earlier of the owner's resolved date and the first commit in which the row is decided. "
                     "The row's own Date_Made cell is not used. A commit date is when the text entered the repository, not when the view was formed; a call held first in another file reads later than it was.")
            P.append(f"{len(T) - len(fwd)} scored calls known on or before {REPORT1_CUT} are report 1's closed population and are not classed here (Will 2026-11-05).")
            P.append("\n| Class | Calls | Rows |\n|---|---:|---|")
            lab = {"BEFORE": "BEFORE: value recorded before the known date", "SAME-DAY": "SAME-DAY: value and known date are one day, order not shown",
                   "AFTER": "AFTER: value first recorded after the known date", "BORN-DECIDED": "BORN-DECIDED: the row's first record is already decided",
                   "NO-GIT-RECORD": "NO-GIT-RECORD: no committed version holds the row or the value scored", "NO-KNOWN-DATE": "NO-KNOWN-DATE: no resolved date and never decided in a commit"}
            for cls in ("BEFORE", "SAME-DAY", "AFTER", "BORN-DECIDED", "NO-GIT-RECORD", "NO-KNOWN-DATE"):
                R = [r for r, t in fwd if t["cls"] == cls]
                ids = "not listed" if cls == "BEFORE" else (", ".join(f"{r['desk']} {r['id']}" for r in R) or "none")
                P.append(f"| {lab[cls]} | {len(R)} | {ids} |")
            rst = [r for r, t in T if t["restarted"]]
            P.append(f"\n**Row ID reused or call rewritten:** {len(rst)} scored row(s) carry an ID whose earlier committed versions were a different call (the prediction text changes at its start, together with the probability or the Date_Made date)"
                     + (": " + ", ".join(f"{r['desk']} {r['id']}" for r in rst) if rst else "")
                     + ". For these the record starts at the first version of the call scored today; the earlier call's dates and probabilities are not used.")
            look = [(r, t) for r, t in fwd if t["look"]]
            P.append(f"\n**LOOK, a prompt to read the row, not a verdict:** {len(look)} BEFORE row(s) whose outcome cell names a full date earlier than the value date"
                     + (": " + ", ".join(f"{r['desk']} {r['id']} ({t['look']} before {t['value_date']})" for r, t in look) if look else "")
                     + ". An outcome cell may cite an older reference date; an outcome that happened before it was recorded, with no full date in the cell, is not caught.")
            both = [(r, t) for r, t in T if t["p0"] is not None]
            if both:
                cur = brier([(r["p"], r["bucket"] == "HIT") for r, t in both])
                fst = brier([(t["p0"], r["bucket"] == "HIT") for r, t in both])
                h2 = sum(r["bucket"] == "HIT" for r, t in both) / len(both)
                ref2 = h2 * (1 - h2)
                chg = sum(1 for r, t in both if abs(t["p0"] - r["p"]) >= .0015)
                P.append(f"\n**First-logged probability beside the scored one, same {len(both)} calls:** Brier at the scored probability {cur:.3f}, at the first-logged probability {fst:.3f}; "
                         f"the hit-rate baseline on these calls is {ref2:.3f}, so the gain is {ref2 - cur:+.3f} scored and {ref2 - fst:+.3f} first-logged. "
                         f"{chg} of the {len(both)} were revised between first logging and scoring; {len(T) - len(both)} scored calls have no first-logged value and are in neither figure. "
                         "First-logged means first in a prediction ledger's git record (or the oldest '(was X%)' mark that first record already carried); a call stated earlier elsewhere is not seen. All history, not forward only: this is a score, no row is re-classed.")
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
    D = lambda x: dt.date(2026, 11, x)
    V = lambda ct, day, p, dec, was=None: (ct, D(day), p, dec, was)
    tc = [  # (name, versions, scored p, resolved, outcome cell, want class, want look)
        ("A1 born decided, Date_Made irrelevant", [V(1, 10, .6, True)], .6, D(9), "", "BORN-DECIDED", None),
        ("A1 born decided beats AFTER", [V(1, 12, .6, True)], .6, D(10), "", "BORN-DECIDED", None),
        ("A2 value after the resolved date", [V(1, 12, .6, False), V(2, 13, .6, True)], .6, D(10), "", "AFTER", None),
        ("A2 value after the first decided commit", [V(1, 6, .4, False), V(2, 10, .4, True), V(3, 12, .6, True)], .6, None, "", "AFTER", None),
        ("A3 same day", [V(1, 10, .6, False), V(2, 10, .6, True)], .6, D(10), "", "SAME-DAY", None),
        ("A4 ordinary before", [V(1, 6, .6, False), V(2, 12, .6, True)], .6, D(12), "", "BEFORE", None),
        ("A5 no record", [], .6, D(12), "", "NO-GIT-RECORD", None),
        ("A5 value never committed", [V(1, 6, .5, False), V(2, 12, .5, True)], .6, D(12), "", "NO-GIT-RECORD", None),
        ("A5 no known date", [V(1, 6, .6, False)], .6, None, "", "NO-KNOWN-DATE", None),
        ("A6 look, outcome cell date before the value", [V(1, 6, .6, False), V(2, 12, .6, True)], .6, D(12), "printed 2026-11-05: 3.1", "BEFORE", D(5)),
        ("A6 no look when the date is later", [V(1, 6, .6, False), V(2, 12, .6, True)], .6, D(12), "printed 2026-11-11: 3.1", "BEFORE", None),
    ]
    for name, vs, p, res, oc, want, look in tc:
        t = timing(vs, p, res, oc)
        if t["cls"] != want or t["look"] != look:
            bad.append((name, t["cls"], t["look"]))
    if timing([V(1, 6, .3, False), V(2, 9, .05, False, .3)], .05, D(12))["p0"] != .3: bad.append("A8 first-logged from the first record")
    if timing([V(1, 6, .3, False, .45), V(2, 9, .05, False, .3)], .05, D(12))["p0"] != .45: bad.append("A8 oldest was in the first record")
    if timing([V(1, 6, None, False), V(2, 9, .2, False)], .2, D(12))["p0"] != .2: bad.append("A8 first record without a probability")
    if oldest_was("5% [2026-07-23] (was 30% [2026-07-02]) (was 45% [2026-06-01])") != .45: bad.append("oldest_was")
    if full_dates("11/5/26, 2026-11-07, 10/31 and $3/4") != {D(5), D(7)}: bad.append(("full_dates", full_dates("11/5/26, 2026-11-07, 10/31 and $3/4")))
    if classify("RESOLVED", "HIT: printed", lambda x: {"RESOLVED": "RESOLVED-UNTYPED", "HIT: PRINTED": "HIT"}.get(x.upper())) != ("HIT", "outcome"): bad.append("classify")
    W = lambda ct, day, p, dec, made, pred: (ct, D(day), p, dec, None, made, norm_text(pred))
    reuse = [W(1, 1, .6, False, "2026-11-01", "OLD call: CPI above 3"), W(2, 12, .6, True, "2026-11-12", "NEW call: payrolls below 100k")]
    t = timing(reuse, .6, D(10))
    if t["cls"] != "BORN-DECIDED" or not t["restarted"] or t["p0"] != .6: bad.append(("reused ID must restart the record", t["cls"], t["restarted"]))
    rew = [W(1, 1, .45, False, "2026-06-01", "Iran strikes a Gulf export terminal before July"), W(2, 3, .7, False, "2026-06-01", "Brent settles above 100 on any session before July"), W(3, 12, .7, True, "2026-06-01", "Brent settles above 100 on any session before July")]
    t = timing(rew, .7, D(12))
    if t["p0"] != .7 or not t["restarted"] or t["cls"] != "BEFORE": bad.append(("rewritten call: first-logged is the new call's", t["p0"], t["cls"]))
    same = [W(1, 1, .6, False, "2026-11-01", "CPI above 3.0 pct in October"), W(2, 5, .6, False, "2026-11-01", "CPI above 3.0% in October (BLS, first print)"), W(3, 12, .6, True, "2026-11-01", "CPI above 3.0% in October (BLS, first print)")]
    t = timing(same, .6, D(12))
    if t["restarted"] or t["cls"] != "BEFORE" or t["first_record"] != D(1): bad.append(("a wording edit is the same call", t["restarted"], t["cls"]))
    ptr = [W(1, 1, .7, False, "2026-10-01", "No net loss of Gulf-ally crude supply to market"), W(2, 6, .7, True, "2026-10-01", "RESOLVED HISTORY, complete immutable row at archive/snapshots")]
    t = timing(ptr, .7, D(6))
    if t["restarted"] or t["cls"] != "BEFORE": bad.append(("a resolved row's text replaced by a pointer is the same call", t["restarted"], t["cls"]))
    fixd = [W(1, 1, .6, False, "2026-02-15", "JGB 30Y stays under 4.0% through Q1"), W(2, 5, .6, False, "2026-02-03", "JGB 30Y stays under 4.0% through Q1"), W(3, 12, .6, True, "2026-02-03", "JGB 30Y stays under 4.0% through Q1")]
    if timing(fixd, .6, D(12))["restarted"]: bad.append("a corrected Date_Made alone is the same call")
    for b, st, want in (("UNMAPPED", "STUCK", False), ("UNMAPPED", "AT-RISK", False), ("UNMAPPED", "RESOLVED-DENY", True), ("HIT", "HIT", True), (None, "OPEN", False), ("RESOLVED-UNTYPED", "RESOLVED", True)):
        if is_decided(b, st) != want: bad.append(("is_decided", b, st))
    for b, st, res, want in (("UNMAPPED", "LIKELY MISSED", D(4), True), ("UNMAPPED", "LIKELY MISSED", None, False), ("UNMAPPED", "STUCK", None, False), ("UNMAPPED", "KILLED", D(2), True), (None, "OPEN", D(2), False)):
        if is_decided(b, st, res) != want: bad.append(("is_decided with a resolved date", st, res))
    X = lambda ct, day, p, dec, res: (ct, D(day), p, dec, None, "2026-11-01", "call text", res)
    z9 = [X(1, 9, .6, is_decided("UNMAPPED", "LIKELY MISSED", D(4)), D(4)), X(2, 12, .6, True, D(4))]
    if timing(z9, .6, D(4))["cls"] != "BORN-DECIDED": bad.append("a final status outside the map, dated, first record: BORN-DECIDED")
    moved = [X(1, 2, .6, False, None), X(2, 6, .7, True, D(5)), X(3, 12, .7, True, D(11))]
    t = timing(moved, .7, D(11))
    if t["known"] != D(5) or t["cls"] != "AFTER": bad.append(("a resolved date moved later does not move the known date", t["known"], t["cls"]))
    stuck = [V(1, 1, .6, False), V(2, 3, .6, is_decided("UNMAPPED", "STUCK")), V(3, 10, .6, True)]
    t = timing(stuck, .6, D(10))
    if t["known"] != D(10) or t["cls"] != "BEFORE": bad.append(("a STUCK version is not decided", t["known"], t["cls"]))
    body = render([{"desk": "X", "id": "X-1", "bucket": "HIT", "p": .6, "basis": "status", "conf": "60%", "outcome": "", "resolved": None}], [], None, None)
    if "SKIPPED (--no-history)" not in body or "| BEFORE" in body: bad.append("A11 skipped history must say so")
    print("selftest", "FAIL " + str(bad) if bad else "PASS", len(cases) + 3 + len(tc) + 26)
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write"); ap.add_argument("--sample", type=int); ap.add_argument("--seed", type=int, default=619)
    ap.add_argument("--sample-out"); ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--no-history", action="store_true", help="skip the git record: no timing table, no first-logged score")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    bucket = load_bucket()
    rows, defects = read_all(bucket)
    rec = None if a.no_history else git_records(bucket)
    body = render(rows, defects, rec, unread_ledgers([r[0] for r in registry_full()]))
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
