#!/usr/bin/env python3
"""MARCO slaughter_pull — weekly federally-inspected slaughter (cattle/hogs/poultry).

Sources: AMS live SJ_LS712 (livestock) + NW_PY017 (poultry); esmis archive
pages 1-5 for ~52wk livestock history. Each livestock file yields 3 dated rows
(current week, prior week, same-week-year-ago). Writes TSV to baselines/.

⚠️ MERGE, NEVER REWRITE (fixed 2026-10-14, MAINTENANCE T2-E). Until s32 this tool
rebuilt the whole baseline from only the rows one run fetched: on 2026-10-10 the
esmis archive pages 404'd for recent weeks, the live file yielded only current /
prior / year-ago, and the run DROPPED the 2026-09-12 and 2026-09-19 rows — exit 0,
well-formed file. Same class as the BTS writer defect (charter airport block item 2).
Now:
  - rows are merged by week_ending; a week this run did not fetch is KEPT verbatim;
  - a fetched cell overwrites an existing one only when its NUMBER differs (the
    live file's current week is an estimate and is revised the next week);
  - the row set can never shrink (asserted before writing);
  - a run that fetches nothing new leaves the file BYTE-IDENTICAL (not rewritten).
`--selftest` proves those four properties offline against a temp copy.
"""
import argparse, io, re, sys, pathlib, shutil, tempfile, datetime as dt

LIVE_LIV = "https://www.ams.usda.gov/mnreports/sj_ls712.txt"
LIVE_POU = "https://www.ams.usda.gov/mnreports/nw_py017.txt"
ESMIS = "https://esmis.nal.usda.gov"
IDX = ESMIS + "/concern/publications/{pid}?page={p}"
OUT = pathlib.Path(__file__).resolve().parents[1] / "baselines" / "slaughter_weekly.tsv"
UA = {"User-Agent": "MARCO/1.0 (research)"}
DATE_RE = re.compile(r"^\s*(\d{1,2}-[A-Za-z]{3}-\d{2})\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s*$")

COLS = ["week_ending", "cattle_head", "calves_head", "hogs_head", "sheep_head", "liv_src",
        "young_chickens_000", "total_hens_000", "ducks_000", "total_turkeys_000", "pou_src"]
LIV_VALS = ["cattle_head", "calves_head", "hogs_head", "sheep_head"]
POU_VALS = ["young_chickens_000", "total_hens_000", "ducks_000", "total_turkeys_000"]


def fetch(url):
    import requests
    r = requests.get(url, headers=UA, timeout=30); r.raise_for_status(); return r.text


def parse_liv(text, src):
    block = re.search(r"Livestock Slaughter \(head\).*?-{5,}", text, re.S)
    if not block: raise ValueError(f"no liv block {src}")
    rows = []
    for line in block.group(0).splitlines():
        m = DATE_RE.match(line)
        if not m: continue
        wk = dt.datetime.strptime(m.group(1), "%d-%b-%y").date()
        rows.append({"week_ending": wk.isoformat(),
                     "cattle_head": int(m.group(2).replace(",", "")),
                     "calves_head": int(m.group(3).replace(",", "")),
                     "hogs_head": int(m.group(4).replace(",", "")),
                     "sheep_head": int(m.group(5).replace(",", "")),
                     "liv_src": src})
    if not rows: raise ValueError(f"no date rows {src}")
    return rows


def parse_pou(text, src):
    m = re.search(r"Week ending\s+(\d+-[A-Za-z]+-\d+)", text)
    wk = dt.datetime.strptime(m.group(1), "%d-%b-%Y").date()
    ch = re.search(r"^Head\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)", text, re.M)
    tk = re.search(r"Live Turkeys.*?^Head\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)\s+([\d,]+)", text, re.S|re.M)
    if not (ch and tk): raise ValueError(f"poultry parse fail {src}")
    return {"week_ending": wk.isoformat(),
            "young_chickens_000": int(ch.group(1).replace(",", "")),
            "total_hens_000": int(ch.group(4).replace(",", "")),
            "ducks_000": int(ch.group(5).replace(",", "")),
            "total_turkeys_000": int(tk.group(5).replace(",", "")),
            "pou_src": src}


def archive_urls(pid, fname, pages=5):
    urls = []
    for p in range(1, pages+1):
        html = fetch(IDX.format(pid=pid, p=p))
        urls += [ESMIS+m.group(1) for m in re.finditer(
            rf'href="(/sites/default/release-files/{pid}/[^"]+/{fname})"', html)]
    return sorted(set(urls))


# ---------------- merge (pure, text-level, no network) ----------------

def read_rows(path):
    """Existing TSV -> (header, {week: {col: text}}), cells kept as their exact text."""
    if not path.exists():
        return list(COLS), {}
    lines = path.read_text(encoding="utf-8").split("\n")
    header = lines[0].split("\t")
    if header != COLS:
        raise SystemExit(f"REFUSE: {path} header {header} != expected {COLS} — not merging into an unknown layout")
    rows = {}
    for ln in lines[1:]:
        if not ln.strip():
            continue
        cells = ln.split("\t")
        cells += [""] * (len(COLS) - len(cells))
        rows[cells[0]] = dict(zip(COLS, cells))
    return header, rows


def _num(text):
    try:
        return float(text) if text != "" else None
    except ValueError:
        return None


def merge(existing, fetched):
    """Merge fetched dict rows into existing text rows. Returns (rows, log)."""
    rows = {w: dict(r) for w, r in existing.items()}
    log = {"added": [], "revised": [], "filled": []}
    for f in fetched:
        w = f["week_ending"]
        if w not in rows:
            rows[w] = {c: "" for c in COLS}; rows[w]["week_ending"] = w
            log["added"].append(w)
        r = rows[w]
        for group, src in ((LIV_VALS, "liv_src"), (POU_VALS, "pou_src")):
            if not any(c in f for c in group):
                continue
            changed = False
            for c in group:
                new = f.get(c)
                if new is None:
                    continue
                old = _num(r[c])
                if old is None:
                    r[c] = str(int(new)); changed = True
                    if w not in log["added"]: log["filled"].append(f"{w}:{c}")
                elif old != float(new):
                    log["revised"].append(f"{w}:{c} {r[c]}->{int(new)}")
                    r[c] = str(int(new)); changed = True
            if changed:
                r[src] = f[src]
    return rows, log


def render(rows):
    out = ["\t".join(COLS)]
    for w in sorted(rows):
        out.append("\t".join(rows[w][c] for c in COLS))
    return "\n".join(out) + "\n"


def write_merged(path, fetched):
    header, existing = read_rows(path)
    before = path.read_text(encoding="utf-8") if path.exists() else None
    rows, log = merge(existing, fetched)
    missing = set(existing) - set(rows)
    if missing or len(rows) < len(existing):
        raise SystemExit(f"REFUSE: merge would drop {len(missing)} week(s): {sorted(missing)[:5]}")
    text = render(rows)
    if before is not None and text == before:
        return "unchanged", log, len(rows)
    if before is not None and render(existing) != before:
        # The file on disk is not in canonical render form (e.g. a hand edit). Refuse rather
        # than silently re-format every row under cover of a data update.
        raise SystemExit(f"REFUSE: {path} is not in canonical form (render(existing) != file) — inspect before merging")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return "written", log, len(rows)


# ---------------- selftest (offline, temp copy only) ----------------

def selftest(src):
    src_bytes = src.read_bytes()
    tmp = pathlib.Path(tempfile.mkdtemp()) / "slaughter_weekly.tsv"
    shutil.copyfile(src, tmp)
    orig = tmp.read_bytes()
    _, ex = read_rows(tmp)
    def as_fetched(r):
        d = {"week_ending": r["week_ending"]}
        for c in LIV_VALS:
            if r[c] != "": d[c] = int(float(r[c]))
        if r["liv_src"]: d["liv_src"] = r["liv_src"]
        if any(r[c] != "" for c in POU_VALS):
            for c in POU_VALS:
                if r[c] != "": d[c] = int(float(r[c]))
            d["pou_src"] = r["pou_src"]
        return d
    ok = True
    # A: canonical form — rendering the file as read reproduces it byte-for-byte
    a = render(ex).encode() == orig
    print(f"  {'✓' if a else '✗'} A canonical: render(read(file)) == file"); ok &= a
    # B: re-merging ALL its own rows is a no-op (byte-identical, not rewritten)
    st, _, _ = write_merged(tmp, [as_fetched(r) for r in ex.values()])
    b = st == "unchanged" and tmp.read_bytes() == orig
    print(f"  {'✓' if b else '✗'} B self-merge leaves the file byte-identical ({st})"); ok &= b
    # C: a run that fetches only the last 3 weeks (the 10/10 failure shape) drops NOTHING
    last3 = [as_fetched(ex[w]) for w in sorted(ex)[-3:]]
    st, _, n = write_merged(tmp, last3)
    c = st == "unchanged" and tmp.read_bytes() == orig and n == len(ex)
    print(f"  {'✓' if c else '✗'} C partial fetch (3 of {len(ex)} weeks) keeps every row, file untouched"); ok &= c
    # D: one new week appends exactly one row and changes nothing else
    st, log, n = write_merged(tmp, [{"week_ending": "2099-01-02", "cattle_head": 1, "calves_head": 2,
                                     "hogs_head": 3, "sheep_head": 4, "liv_src": "SELFTEST"}])
    new = tmp.read_bytes()
    d = (n == len(ex) + 1 and log["added"] == ["2099-01-02"]
         and new.startswith(orig) and new[len(orig):] == b"2099-01-02\t1\t2\t3\t4\tSELFTEST\t\t\t\t\t\n")
    print(f"  {'✓' if d else '✗'} D new week appends one row, existing bytes untouched"); ok &= d
    # E: a revised value changes that cell (and its src) only
    w0 = sorted(ex)[-1]; r0 = as_fetched(ex[w0]); r0["cattle_head"] = r0.get("cattle_head", 0) + 1000; r0["liv_src"] = "REVISED"
    st, log, n = write_merged(tmp, [r0])
    e = n == len(ex) + 1 and len(log["revised"]) == 1 and log["added"] == []
    print(f"  {'✓' if e else '✗'} E revised value: one cell revised, no rows added/dropped ({log['revised']})"); ok &= e
    # F (guard is wired, observed FAILING): inject a merge that drops a row; write_merged must refuse
    global merge
    real_merge = merge
    def dropping_merge(existing, fetched):
        rows, log = real_merge(existing, fetched); rows.pop(sorted(rows)[0]); return rows, log
    merge = dropping_merge
    before_f = tmp.read_bytes()
    try:
        write_merged(tmp, [])
        f_ok = False
    except SystemExit as ex_:
        f_ok = str(ex_).startswith("REFUSE: merge would drop") and tmp.read_bytes() == before_f
    finally:
        merge = real_merge
    print(f"  {'✓' if f_ok else '✗'} F a row-dropping merge is REFUSED and the file is left untouched"); ok &= f_ok
    src_ok = src.read_bytes() == src_bytes
    print(f"  {'✓' if src_ok else '✗'} G real baseline byte-identical after the selftest"); ok &= src_ok
    print(f"\n  {'✅ selftest PASS' if ok else '❌ selftest FAIL'} — temp copy {tmp}; real baseline not touched")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=pathlib.Path, default=OUT, help="baseline path (default: baselines/slaughter_weekly.tsv)")
    ap.add_argument("--selftest", action="store_true", help="offline merge-property test on a temp copy of --out")
    a = ap.parse_args()
    if a.selftest:
        return selftest(a.out)
    fetched = parse_liv(fetch(LIVE_LIV), "LIVE")
    for u in archive_urls("2j62s4898", "SJ_LS712.TXT", pages=5):
        try: fetched += parse_liv(fetch(u), u.split("/")[-3])
        except Exception as e: print(f"skip {u}: {e}", file=sys.stderr)
    # de-dup fetched livestock by week (first seen wins: LIVE is parsed first, so it beats the archive)
    seen, liv = set(), []
    for r in fetched:
        if r["week_ending"] not in seen:
            seen.add(r["week_ending"]); liv.append(r)
    pou = [parse_pou(fetch(LIVE_POU), "LIVE")]
    a.out.parent.mkdir(parents=True, exist_ok=True)
    status, log, n = write_merged(a.out, liv + pou)
    print(f"{status}: {n} weekly rows → {a.out}")
    print(f"fetched livestock weeks: {len(liv)} (newest {max(r['week_ending'] for r in liv)}); poultry week: {pou[0]['week_ending']}")
    print(f"added {len(log['added'])} {log['added'][-5:]} · revised {len(log['revised'])} {log['revised'][:5]} · filled {len(log['filled'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
