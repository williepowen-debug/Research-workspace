#!/usr/bin/env python3
"""MARCO sub-annual FL migration proxy tracker (workbook/MIGRATION_PROXIES.tsv).

Built by DAEDALUS 2026-07-10 (Will-approved, Tier-3 gap #6 — see
AGENTS/DAEDALUS/outbox/2026-07-10_to-PROME_tier3-gaps-and-power-agent-memo.md).

FRAMING RULE: Proxies are DIRECTION/DERIVATIVE tells for VX-MARCO-3.03 between
annual Census prints — they NEVER restate the canonical level (different bases:
registered voters / licensed drivers / K-12 families != total population;
vintage/basis traps are the fleet's worst error class). Canonical: FL net
domestic migration +22,517 (2025, Census); next print ~Dec 2026.
USPS COA excluded by design: paywalled since 2023, not free.

LEGS
  VOTER_REG_NET        monthly, AUTOMATED here — FL DOS "New and Removed Voters
                       by County" (current-year xlsx + prior-year archive zip,
                       URLs discovered live from the DOS reports page).
                       yoy_pct is computed on NEW valid voters: removals are
                       dominated by list-maintenance purge cycles, so net swings
                       on purges, not migration.
  FLHSMV_LICENSE_INFLOW  quarterly, MANUAL — free MIAMI-Realtors publications
                       (~Jan/Apr/Jul/Oct); FLHSMV raw data is not free.
  FLDOE_ENROLLMENT     2x/school-yr, MANUAL — Survey 2 ~Dec-Jan, Survey 3 ~Feb-Mar.

USAGE
  python3 AGENTS/MARCO/tools/fl_migration_proxies.py            # fetch + report
  python3 AGENTS/MARCO/tools/fl_migration_proxies.py --quick    # no network: cadence + verdict from TSV
  python3 AGENTS/MARCO/tools/fl_migration_proxies.py --append   # also append newest voter month to the TSV

RC: 0 = ok · 1 = a leg is overdue past its cadence window · 2 = fetch/parse
failure (fails LOUD on stderr; never fabricates).  Stdlib-only.
"""
import io, re, sys, urllib.request, zipfile
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path

MARCO = Path(__file__).resolve().parents[1]
TSV = MARCO / "workbook" / "MIGRATION_PROXIES.tsv"
PAGE = ("https://dos.fl.gov/elections/data-statistics/"
        "voter-registration-statistics/voter-registration-reports/")
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
# leg -> (overdue threshold: months since latest row's period end, cadence hint)
CADENCE = {
    "FLHSMV_LICENSE_INFLOW": (5, "quarterly — MIAMI Realtors publishes ~Jan/Apr/Jul/Oct"),
    "VOTER_REG_NET":         (2, "monthly — FL DOS posts with ~1mo lag (this script)"),
    "FLDOE_ENROLLMENT":      (9, "2x/school-yr — Survey 2 ~Dec-Jan, Survey 3 ~Feb-Mar"),
}
FLDOE_FIRST_DUE = date(2027, 1, 31)  # empty leg not overdue until Survey-2 window has passed


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    return urllib.request.urlopen(req, timeout=120).read()


def month_totals(blob):
    """{month_index 1-12: (new, removed_active, removed_inactive)} from a DOS xlsx (stdlib parse)."""
    zf = zipfile.ZipFile(io.BytesIO(blob))
    sst = []
    if "xl/sharedStrings.xml" in zf.namelist():
        for si in ET.fromstring(zf.read("xl/sharedStrings.xml")).iter(NS + "si"):
            sst.append("".join(t.text or "" for t in si.iter(NS + "t")))
    rns = "{http://schemas.openxmlformats.org/package/2006/relationships}"
    rels = {r.get("Id"): r.get("Target") for r in
            ET.fromstring(zf.read("xl/_rels/workbook.xml.rels")).iter(rns + "Relationship")}
    rid = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id"
    out = {}
    for sh in ET.fromstring(zf.read("xl/workbook.xml")).iter(NS + "sheet"):
        name = sh.get("name")
        if name not in MONTHS:
            continue
        target = rels[sh.get(rid)]
        path = target if target.startswith("xl/") else "xl/" + target.lstrip("/")
        for row in ET.fromstring(zf.read(path)).iter(NS + "row"):
            cells = {}
            for c in row.iter(NS + "c"):
                v = c.find(NS + "v")
                if v is None or v.text is None:
                    continue
                col = "".join(ch for ch in c.get("r", "") if ch.isalpha())
                cells[col] = sst[int(v.text)] if c.get("t") == "s" else v.text
            if str(cells.get("A", "")).strip().upper() == "TOTALS":
                try:
                    out[MONTHS.index(name) + 1] = tuple(
                        int(float(cells[k])) for k in ("B", "C", "D"))
                except (KeyError, ValueError):
                    pass  # month sheet present but not yet populated
    return out


def pull_voter_reg(today):
    """Fetch DOS current-year xlsx + prior-year archive; return newest-month reading dict."""
    html = fetch(PAGE).decode("utf-8", "replace")
    cur = re.search(r'/media/\d+/new-and-removed-voters-by-county-(\d{4})[^"\']*\.xlsx', html)
    if not cur:
        raise RuntimeError("DOS reports page: no new-and-removed-voters xlsx link found "
                           "(page layout changed?) — %s" % PAGE)
    year = int(cur.group(1))
    cur_tot = month_totals(fetch("https://dos.fl.gov" + cur.group(0)))
    if not cur_tot:
        raise RuntimeError("current-year xlsx parsed but no populated month sheets")
    zm = re.search(r'/media/\d+/%d-archived\.zip' % (year - 1), html)
    if not zm:
        raise RuntimeError("DOS reports page: no %d archive zip link found" % (year - 1))
    zf = zipfile.ZipFile(io.BytesIO(fetch("https://dos.fl.gov" + zm.group(0))))
    member = [n for n in zf.namelist() if "new-and-removed" in n and n.endswith(".xlsx")]
    if not member:
        raise RuntimeError("%d archive zip lacks a new-and-removed xlsx" % (year - 1))
    pri_tot = month_totals(zf.read(member[0]))
    m = max(cur_tot)
    new, ra, ri = cur_tot[m]
    yoy = (new / pri_tot[m][0] - 1) * 100 if m in pri_tot and pri_tot[m][0] else None
    ytd_c = sum(cur_tot[i][0] for i in cur_tot if i <= m)
    ytd_p = sum(pri_tot[i][0] for i in pri_tot if i <= m)
    return {"period": "%d-%02d" % (year, m), "new": new, "net": new - ra - ri,
            "yoy": yoy, "ytd_yoy": (ytd_c / ytd_p - 1) * 100 if ytd_p else None}


def load_rows():
    rows = []
    if TSV.exists():
        for ln in TSV.read_text().splitlines():
            if ln.startswith("#") or ln.startswith("period\t") or not ln.strip():
                continue
            f = ln.split("\t")
            if len(f) >= 9:
                rows.append(dict(zip(
                    ["period", "leg", "geography", "value", "yoy_pct",
                     "direction_read", "source", "retrieved", "notes"], f)))
    return rows


def period_end(p):
    y, rest = int(p[:4]), p[5:]
    if rest.startswith("H"):
        m = 6 * int(rest[1])
    elif rest.startswith("Q"):
        m = 3 * int(rest[1])
    else:
        m = int(rest) if rest.isdigit() else 12
    return y, m


def main():
    argv = sys.argv[1:]
    quick, append = "--quick" in argv, "--append" in argv
    today = date.today()
    rows = load_rows()
    vr = None
    if not quick:
        try:
            vr = pull_voter_reg(today)
            print("VOTER_REG_NET %s: new %s (%s%% YoY on new; YTD new %+.1f%%) · "
                  "net %+d (net is purge-noisy — direction from NEW voters)" % (
                      vr["period"], format(vr["new"], ","),
                      "%+.1f" % vr["yoy"] if vr["yoy"] is not None else "n/a",
                      vr["ytd_yoy"], vr["net"]))
            if append and not any(r["leg"] == "VOTER_REG_NET" and r["period"] == vr["period"]
                                  for r in rows):
                note = ("New %s vs prior-yr same month; net = new - removals (removals "
                        "purge-cycle-dominated); YTD new %+.1f%% YoY." % (
                            format(vr["new"], ","), vr["ytd_yoy"]))
                tone = ("no inflow-collapse signal" if (vr["ytd_yoy"] or 0) >= 0
                        else "inflow softening")
                read = "inflow direction: new voters %s%% YoY, YTD %+.1f%% — %s" % (
                    "%+.1f" % vr["yoy"] if vr["yoy"] is not None else "n/a",
                    vr["ytd_yoy"], tone)
                with TSV.open("a") as fh:
                    fh.write("\t".join([vr["period"], "VOTER_REG_NET", "FL statewide",
                                        "%+d" % vr["net"],
                                        "%+.1f" % vr["yoy"] if vr["yoy"] is not None else "NA",
                                        read, PAGE, today.isoformat(), note]) + "\n")
                rows = load_rows()
                print("  appended %s row to %s" % (vr["period"], TSV.name))
        except Exception as e:
            print("FAIL (voter-reg fetch/parse): %s" % e, file=sys.stderr)
            return 2
    # cadence check
    overdue = []
    newest = {}
    for leg, (thresh, hint) in CADENCE.items():
        mine = [r for r in rows if r["leg"] == leg]
        if not mine:
            if leg == "FLDOE_ENROLLMENT" and today <= FLDOE_FIRST_DUE:
                print("FLDOE_ENROLLMENT: no rows yet — first pull due ~Dec 2026 (Survey 2). %s" % hint)
            else:
                overdue.append(leg)
                print("OVERDUE %s: no rows at all (%s)" % (leg, hint))
            continue
        r = max(mine, key=lambda r: period_end(r["period"]))
        newest[leg] = r
        y, m = period_end(r["period"])
        age = (today.year - y) * 12 + today.month - m
        if age > thresh:
            overdue.append(leg)
            print("OVERDUE %s: newest row %s is %dmo old (window %dmo) — %s" % (
                leg, r["period"], age, thresh, hint))
    if today.month in (1, 4, 7, 10):
        print("HINT: FLHSMV window — check MIAMI Realtors for a new license-exchange piece this month.")
    if today.month in (12, 1):
        print("HINT: FLDOE Survey-2 (Oct count) lands ~Dec-Jan.")
    if today.month in (2, 3):
        print("HINT: FLDOE Survey-3 (Feb count) lands ~Feb-Mar.")
    # verdict
    def leg_bit(leg, label):
        r = newest.get(leg)
        if leg == "VOTER_REG_NET" and vr:
            return "voter new %s%% YoY / net %+d (%s)" % (
                "%+.1f" % vr["yoy"] if vr["yoy"] is not None else "n/a", vr["net"], vr["period"])
        return "%s %s%% YoY (%s)" % (label, r["yoy_pct"], r["period"]) if r else "%s pending" % label
    print("FL migration proxies: %s · %s · %s — direction tells only, "
          "canonical VX-MARCO-3.03 +22,517/2025 unchanged" % (
              leg_bit("FLHSMV_LICENSE_INFLOW", "FLHSMV inflow"),
              leg_bit("VOTER_REG_NET", "voter-net"),
              leg_bit("FLDOE_ENROLLMENT", "FLDOE")))
    return 1 if overdue else 0


if __name__ == "__main__":
    sys.exit(main())
