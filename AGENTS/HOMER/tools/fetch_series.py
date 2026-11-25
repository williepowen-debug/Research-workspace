#!/usr/bin/env python3
"""Fetch four public housing series, save dated copies, fail loudly. Grades nothing.

Built 2026-11-25 on Will's word (18:28 ET, "yes go ahead and build"; scope
reports/2026-11-25_script1-scope-DRAFT.md, option A). It writes ONLY under data/series/
and never touches a ledger, STATUS, a reading cell, a band or a prediction.
Reading the issuer's release stays required.

Feeds: pmms (Freddie PMMS) · fmhpi (Freddie FMHPI) · treasury (daily par curve) ·
apartment_list (city rent estimates, roster-100 extract for tools/rent_breadth.py).

Per feed, a run FAILS (nonzero exit, nothing saved for that feed, other feeds still run) on:
  HTTP not 200 · header not as expected · nothing parsed · fewer rows than the last save of
  the same file · newest period older than the last save · (apartment_list) a roster city missing.
A feed whose kept extract is byte-identical to the last save is UNCHANGED (logged, not re-saved).
A refusal or block stops that feed. Never retry with another identity, address or proxy.

Fetching is plain `curl` with its default client string, exactly as tested by hand on 2026-11-25.

Usage (from AGENTS/HOMER/):
  python3 tools/fetch_series.py                # all four feeds
  python3 tools/fetch_series.py pmms treasury  # named feeds only
  python3 tools/fetch_series.py --selftest     # malformed inputs must FAIL; no network
Exit: 0 all requested feeds NEW or UNCHANGED · 1 any feed FAILED · 2 bad usage.
Log: data/series/FETCH_LOG.tsv (one row per feed per run, failures included).
"""
import csv, datetime as dt, hashlib, io, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DESK = os.path.normpath(os.path.join(HERE, ".."))
OUT = os.path.join(DESK, "data", "series")
LOG = os.path.join(OUT, "FETCH_LOG.tsv")
ROSTER = os.path.join(DESK, "workbook", "RENT_BREADTH_ROSTER.tsv")
LOG_COLS = ["fetched_at_et", "feed", "result", "newest_period", "rows_kept", "rows_full",
            "bytes_full", "sha256_full", "saved_path", "url", "note"]


class FeedError(Exception):
    pass


def now_et():
    out = subprocess.run(["date", "+%Y-%m-%d %H:%M"], capture_output=True, text=True,
                         env={**os.environ, "TZ": "America/New_York"})
    return out.stdout.strip()


def fetch(url):
    """Return bytes; raise FeedError on anything but HTTP 200."""
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        path = tf.name
    try:
        r = subprocess.run(["curl", "-sL", "--max-time", "120", "-o", path, "-w", "%{http_code}", url],
                           capture_output=True, text=True)
        code = r.stdout.strip()
        if r.returncode != 0 or code != "200":
            raise FeedError(f"HTTP {code or '-'} (curl rc {r.returncode}); feed stopped, no retry")
        with open(path, "rb") as fh:
            return fh.read()
    finally:
        os.unlink(path)


def rows_of(data, need):
    text = data.decode("utf-8-sig", errors="strict")
    rd = csv.reader(io.StringIO(text))
    try:
        header = next(rd)
    except StopIteration:
        raise FeedError("empty file")
    header = [h.strip() for h in header]
    if header[:len(need)] != need:
        raise FeedError(f"header changed: expected {need}, got {header[:len(need)]}")
    rows = [r for r in rd if any(c.strip() for c in r)]
    if not rows:
        raise FeedError("no data rows")
    return header, rows


def mdy(s):
    try:
        return dt.datetime.strptime(s.strip(), "%m/%d/%Y").date()
    except ValueError:
        raise FeedError(f"unparseable date {s!r}")


def to_csv(header, rows):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    w.writerows(rows)
    return buf.getvalue().encode()


# ---- feed parsers: (raw bytes, last state or None) -> dict(newest, kept bytes, rows_kept, rows_full, show)

PMMS_COLS = ["date", "pmms30", "pmms30p", "pmms15", "pmms15p"]


def parse_pmms(data, last):
    header, rows = rows_of(data, PMMS_COLS)
    dated = sorted(((mdy(r[0]), r) for r in rows), key=lambda x: x[0])
    for d, r in dated[-60:]:
        try:
            float(r[1])
        except ValueError:
            raise FeedError(f"pmms30 not a number on {d}: {r[1]!r}")
    newest, latest = dated[-1]
    kept = to_csv(header, [r for _, r in dated[-60:]])
    prev = dated[-2][1][1] if len(dated) > 1 else "-"
    return dict(newest=newest.isoformat(), kept=kept, rows_kept=60, rows_full=len(rows),
                show=f"30Y {latest[1]}% [{newest}] (prior week {prev}%); 15Y {latest[3]}%")


FMHPI_COLS = ["Year", "Month", "GEO_Type", "GEO_Name", "GEO_Code", "Index_NSA", "Index_SA"]
FMHPI_KEEP = {("US", "USA"), ("State", "CA"), ("State", "NV"), ("State", "TX")} | {("CBSA", c) for c in (
    "15980", "19660", "27260", "29460", "29820", "31080", "33100", "36100", "36740", "37340",
    "39460", "41740", "41860", "45300", "19100", "26420")}
# FL statewide deliberately NOT kept: CORAL owns every statewide Florida figure (charter Scope).


def parse_fmhpi(data, last):
    header, rows = rows_of(data, FMHPI_COLS)
    keep, newest = [], None
    for r in rows:
        try:
            ym = (int(r[0]), int(r[1]))
        except ValueError:
            raise FeedError(f"bad Year/Month {r[:2]}")
        newest = max(newest or ym, ym)
        key = (r[2], r[3] if r[2] != "CBSA" else r[4])
        if key in FMHPI_KEEP:
            keep.append(r)
    keep = [r for r in keep if (int(r[0]), int(r[1])) >= (newest[0] - 5, newest[1])]
    found = {(r[2], r[3] if r[2] != "CBSA" else r[4]) for r in keep}
    if found != FMHPI_KEEP:
        raise FeedError(f"geographies missing: {sorted(FMHPI_KEEP - found)}")
    us = {(int(r[0]), int(r[1])): r for r in keep if r[2] == "US"}
    cur, yago = us.get(newest), us.get((newest[0] - 1, newest[1]))
    if not cur or not yago:
        raise FeedError("national row or its year-ago row missing")
    yoy = (float(cur[6]) / float(yago[6]) - 1) * 100
    keep.sort(key=lambda r: (r[2], r[4], r[3], int(r[0]), int(r[1])))
    return dict(newest=f"{newest[0]}-{newest[1]:02d}", kept=to_csv(header, keep), rows_kept=len(keep),
                rows_full=len(rows), show=f"national {newest[0]}-{newest[1]:02d} YoY SA {yoy:+.2f}% (computed from Index_SA)")


def fmhpi_revisions(old, new):
    """Count kept rows whose Index_SA changed between two saves (months present in both)."""
    def idx(b):
        rd = csv.reader(io.StringIO(b.decode()))
        next(rd)
        return {(r[2], r[4], r[3], r[0], r[1]): r[6] for r in rd}
    a, b = idx(old), idx(new)
    common = a.keys() & b.keys()
    changed = sum(1 for k in common if a[k] != b[k])
    return f"{changed} of {len(common)} index values revised since the last save"


TSY_COLS = ["Date", "1 Mo"]


def parse_treasury(data, last):
    header, rows = rows_of(data, TSY_COLS)
    for need in ("2 Yr", "10 Yr"):
        if need not in header:
            raise FeedError(f"column {need!r} missing")
    dated = sorted(((mdy(r[0]), r) for r in rows), key=lambda x: x[0])
    newest, r = dated[-1]
    i2, i10 = header.index("2 Yr"), header.index("10 Yr")
    return dict(newest=newest.isoformat(), kept=to_csv(header, [x for _, x in dated]), rows_kept=len(dated),
                rows_full=len(rows), show=f"[{newest}] 2Y {r[i2]}% · 10Y {r[i10]}%")


AL_PAGE = "https://www.apartmentlist.com/research/category/data-rent-estimates"
AL_COLS = ["location_name", "location_type", "location_fips_code", "population", "state", "county",
           "metro", "bed_size"]


def roster_fips():
    lines = [l for l in open(ROSTER, encoding="utf-8").read().splitlines() if l and not l.startswith("#")]
    fips = {l.split("\t")[1] for l in lines[1:]}
    if len(fips) != 100:
        raise FeedError(f"roster has {len(fips)} cities, expected 100")
    return fips


def parse_apartment_list(data, last):
    text = data.decode("utf-8-sig")
    lines = text.splitlines()
    header, rows = rows_of(data, AL_COLS)
    months = [h for h in header if re.fullmatch(r"\d{4}_\d{2}", h)]
    if not months:
        raise FeedError("no YYYY_MM month columns")
    fips = roster_fips()
    kept_lines = [lines[0]]
    got = set()
    for line in lines[1:]:
        r = next(csv.reader([line])) if line.strip() else None
        if r and r[1] == "City" and r[7] == "overall" and r[2] in fips:
            kept_lines.append(line)
            got.add(r[2])
    if got != fips:
        raise FeedError(f"{len(fips - got)} roster cities missing from the file")
    newest = max(months).replace("_", "-")
    return dict(newest=newest, kept=("\n".join(kept_lines) + "\n").encode(), rows_kept=len(kept_lines) - 1,
                rows_full=len(rows), show=f"newest month {newest}; then run tools/rent_breadth.py on the saved extract")


def al_url():
    page = fetch(AL_PAGE).decode("utf-8", errors="replace")
    # The page links protocol-relative ("//assets.ctfassets.net/..."), seen 2026-11-25.
    urls = ["https:" + u if u.startswith("//") else u for u in re.findall(
        r"((?:https:)?//[^\"'<> ]*?ctfassets\.net/[^\"'<> ]*?/Apartment_List_Rent_Estimates_\d{4}_\d{2}\.csv)", page)]
    if not urls:
        raise FeedError("no Apartment_List_Rent_Estimates_YYYY_MM.csv link on the data page")
    return max(set(urls), key=lambda u: re.search(r"(\d{4}_\d{2})\.csv$", u).group(1))


FEEDS = {
    "pmms": (lambda: "https://www.freddiemac.com/pmms/docs/PMMS_history.csv", parse_pmms),
    "fmhpi": (lambda: "https://www.freddiemac.com/fmac-resources/research/docs/fmhpi_master_file.csv", parse_fmhpi),
    "treasury": (lambda: "https://home.treasury.gov/resource-center/data-chart-center/interest-rates/"
                 f"daily-treasury-rates.csv/{dt.date.today().year}/all?type=daily_treasury_yield_curve"
                 f"&field_tdr_date_value={dt.date.today().year}&page&_format=csv", parse_treasury),
    "apartment_list": (al_url, parse_apartment_list),
}


def last_ok(feed):
    """Most recent NEW or UNCHANGED log row for this feed, or None."""
    if not os.path.exists(LOG):
        return None
    best = None
    with open(LOG, encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["feed"] == feed and r["result"] in ("NEW", "UNCHANGED"):
                best = r
    return best


def judge(feed, res, last, url):
    """Stale and shrink checks against the last good save. Raises FeedError."""
    if not last:
        return
    if res["newest"] < last["newest_period"]:
        raise FeedError(f"newest period {res['newest']} is OLDER than the last save {last['newest_period']} (stale copy)")
    same_file = last["url"] == url
    if same_file and res["rows_full"] < int(last["rows_full"]):
        raise FeedError(f"file has {res['rows_full']} rows, fewer than the last save's {last['rows_full']} (truncated?)")


def run_feed(feed, stamp):
    url_fn, parse = FEEDS[feed]
    row = dict(fetched_at_et=stamp, feed=feed, result="FAIL", newest_period="", rows_kept="", rows_full="",
               bytes_full="", sha256_full="", saved_path="", url="", note="")
    try:
        url = url_fn()
        row["url"] = url
        data = fetch(url)
        row["bytes_full"], row["sha256_full"] = str(len(data)), hashlib.sha256(data).hexdigest()
        res = parse(data, None)
        last = last_ok(feed)
        judge(feed, res, last, url)
        row.update(newest_period=res["newest"], rows_kept=str(res["rows_kept"]), rows_full=str(res["rows_full"]))
        kept_sha = hashlib.sha256(res["kept"]).hexdigest()
        prev_path = last and os.path.join(DESK, last["saved_path"])
        if feed == "fmhpi" and prev_path and os.path.exists(prev_path):
            res["show"] += "; " + fmhpi_revisions(open(prev_path, "rb").read(), res["kept"])
        if prev_path and os.path.exists(prev_path) and hashlib.sha256(open(prev_path, "rb").read()).hexdigest() == kept_sha:
            row.update(result="UNCHANGED", saved_path=last["saved_path"], note=res["show"])
        else:
            d = os.path.join(OUT, feed)
            os.makedirs(d, exist_ok=True)
            name = f"{stamp[:10]}_{stamp[11:].replace(':', '')}_{feed}_{res['newest']}.csv"
            with open(os.path.join(d, name), "wb") as fh:
                fh.write(res["kept"])
            row.update(result="NEW", saved_path=os.path.relpath(os.path.join(d, name), DESK), note=res["show"])
    except FeedError as e:
        row["note"] = str(e)
    except Exception as e:  # any surprise is a failure of this feed, never a silent pass
        row["note"] = f"{type(e).__name__}: {e}"
    return row


def log(rows):
    os.makedirs(OUT, exist_ok=True)
    new = not os.path.exists(LOG)
    with open(LOG, "a", encoding="utf-8", newline="") as fh:
        if new:
            fh.write("\t".join(LOG_COLS) + "\n")
        for r in rows:
            fh.write("\t".join(str(r[c]).replace("\t", " ").replace("\n", " ") for c in LOG_COLS) + "\n")


def selftest():
    """Malformed inputs must raise FeedError. No network, no files written."""
    good_pmms = b"date,pmms30,pmms30p,pmms15,pmms15p\n11/19/2026,7.28,,6.60,\n11/25/2026,7.21,,6.54,\n"
    good_tsy = b'Date,"1 Mo","2 Yr","10 Yr"\n11/24/2026,4.30,4.63,4.91\n11/25/2026,4.27,4.61,4.88\n'
    cases = [
        ("pmms truncated to header", lambda: parse_pmms(b"date,pmms30,pmms30p,pmms15,pmms15p\n", None)),
        ("pmms empty file", lambda: parse_pmms(b"", None)),
        ("pmms renamed column", lambda: parse_pmms(good_pmms.replace(b"pmms30,", b"rate30,", 1), None)),
        ("pmms non-numeric rate", lambda: parse_pmms(good_pmms.replace(b"7.21", b"n/a"), None)),
        ("pmms stale copy", lambda: judge("pmms", parse_pmms(good_pmms, None),
                                          {"newest_period": "2026-12-03", "url": "u", "rows_full": "2"}, "u")),
        ("pmms fewer rows, same file", lambda: judge("pmms", parse_pmms(good_pmms, None),
                                                    {"newest_period": "2026-11-25", "url": "u", "rows_full": "3000"}, "u")),
        ("treasury renamed column", lambda: parse_treasury(good_tsy.replace(b'"10 Yr"', b'"10 Year"'), None)),
        ("treasury bad date", lambda: parse_treasury(good_tsy.replace(b"11/25/2026", b"2026-11-25"), None)),
        ("fmhpi renamed column", lambda: parse_fmhpi(b"Year,Month,GEO_Type,GEO_Name,GEO_Code,Index_NSA,IndexSA\n2026,9,US,USA,.,1,1\n", None)),
        ("fmhpi geography missing", lambda: parse_fmhpi(b"Year,Month,GEO_Type,GEO_Name,GEO_Code,Index_NSA,Index_SA\n2026,9,US,USA,.,1,1\n2025,9,US,USA,.,1,1\n", None)),
        ("apartment_list roster cities missing", lambda: parse_apartment_list(
            (",".join(AL_COLS) + ",2026_09,2026_10\n").encode() + b"X,City,1,1,NY,,,overall,1,1\n", None)),
        ("apartment_list no month columns", lambda: parse_apartment_list((",".join(AL_COLS) + "\n").encode() + b"X,City,1,1,NY,,,overall\n", None)),
    ]
    bad = 0
    for name, fn in cases:
        try:
            fn()
            print(f"  FAIL (accepted malformed input): {name}")
            bad += 1
        except FeedError as e:
            print(f"  ok  refused: {name} — {e}")
    ok = parse_pmms(good_pmms, None)
    if ok["newest"] != "2026-11-25":
        print("  FAIL: clean pmms input misread"); bad += 1
    else:
        print(f"  ok  clean pmms input read: {ok['show']}")
    print(f"SELFTEST {'PASS' if not bad else 'FAIL'}: {len(cases)} malformed inputs, {bad} accepted")
    return 0 if not bad else 1


def main(argv):
    if argv == ["--selftest"]:
        return selftest()
    feeds = argv or list(FEEDS)
    unknown = [f for f in feeds if f not in FEEDS]
    if unknown:
        print(f"unknown feed(s) {unknown}; choose from {list(FEEDS)}")
        return 2
    stamp = now_et()
    rows = [run_feed(f, stamp) for f in feeds]
    log(rows)
    for r in rows:
        print(f"{r['result']:<9} {r['feed']:<15} {r['newest_period'] or '-':<11} {r['note']}")
    fails = [r["feed"] for r in rows if r["result"] == "FAIL"]
    print(f"FETCH {'FAILED: ' + ', '.join(fails) if fails else 'OK'} at {stamp} ET — grades nothing; log {os.path.relpath(LOG, DESK)}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
