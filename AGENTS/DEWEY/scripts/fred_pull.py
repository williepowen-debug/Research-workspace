#!/usr/bin/env python3
"""
FRED Data Pull — Reusable script for Federal Reserve Economic Data
Usage:
  python3 fred_pull.py SERIES_ID                    # Latest 10 observations
  python3 fred_pull.py SERIES_ID --limit 50         # Latest 50
  python3 fred_pull.py SERIES_ID --start 2024-01-01 # From date (whole range)
  python3 fred_pull.py SERIES_ID --all              # Full history (live API)
  python3 fred_pull.py SERIES_ID --csv              # Output as CSV
  python3 fred_pull.py SERIES_ID --archive          # History via Wayback (see below)
  python3 fred_pull.py SERIES_ID --splice           # Archive history + live, merged

⚠️ THE TRUNCATION TRAP (why --archive/--splice exist)
FRED's free API serves ICE BofA (`BAML*`) series as a ROLLING ~3-YEAR WINDOW
— every BAML* series starts at 2023-07-17 (a licensing cut, verified 2026-07-16
across BAMLH0A0HYM2/BAMLC0A0CM/BAMLH0A3HYC; control series are unaffected).
It fails SILENTLY: ask for 2020 and you get 2023 data with NO error. This
module WARNS on stderr whenever the returned first-date is later than the
requested --start. Do not ignore that warning; confirm the first date.

  --archive : recover FULL history from a Wayback snapshot of FRED's raw
              text endpoint (fred.stlouisfed.org/data/<ID>.txt). Provenance
              header is intact ("Source: Ice Data Indices, LLC") = [PRIMARY].
              BAMLH0A0HYM2 → 1996-12-31..2023-12-11. Archive-only: the LIVE
              /data/ endpoint is dead (HTTP 000).
  --splice  : archive history + live API, merged (archive before the live
              cut, live after). Self-validates on the overlap window and
              reports any mismatch. This is how you get 1996→today.

Dead paths — do NOT retry (verified 2026-07-16):
  fredgraph.csv?cosd=...  → truncated identically
  ALFRED vintage_date     → truncated identically
  live /data/<ID>.txt     → HTTP 000 (blocked)

Common series:
  BAMLH0A0HYM2  — HY OAS (ICE BofA)      [TRUNCATED — use --splice for history]
  BAMLC0A0CM    — IG OAS                 [TRUNCATED — use --splice for history]
  SOFR          — Secured Overnight Financing Rate
  SOFR99        — SOFR 99th percentile
  IORB          — Interest on Reserve Balances (IOER pre-2021-07-29)
  RRPONTSYD     — Reverse Repo
  U6RATE        — U-6 Unemployment
  UNRATE        — Unemployment Rate
  ICSA          — Initial Jobless Claims
  CCSA          — Continuing Claims
"""

import json, os, sys, time, urllib.request, urllib.parse, urllib.error

# Series families known to be licence-truncated on the free API.
_TRUNCATED_PREFIXES = ("BAML",)
# Verified-good snapshots, used when the CDX index is unavailable (it 503s often).
_KNOWN_SNAPSHOTS = {
    "BAMLH0A0HYM2": "20231212182755",
    "BAMLC0A0CM": "20240623204207",
}
_UA = {"User-Agent": "DEWEY-research/1.0 (research agent; contact via repo)",
       "Accept-Encoding": "gzip"}

def _fred_key():
    """Env first, else the gitignored FORGE market-data .env (single per-machine home).
    Hardcoded copies scrubbed 2026-07-01 (public-prep) — never hardcode this key."""
    import pathlib
    k = os.environ.get("FRED_API_KEY", "")
    if k:
        return k
    p = pathlib.Path(__file__).resolve().parents[3] / "FORGE/tools/market-data/.env"
    if p.exists():
        for line in p.read_text().splitlines():
            if line.startswith("FRED_API_KEY="):
                return line.split("=", 1)[1].strip()
    print("WARN: FRED_API_KEY not found (env or FORGE/tools/market-data/.env) — FRED pulls will fail", file=sys.stderr)
    return ""

API_KEY = _fred_key()
BASE = "https://api.stlouisfed.org/fred/series/observations"

def fetch(series_id, limit=None, start=None, all_data=False, _warn=True):
    """limit=None means unbounded. A `start` with no explicit `limit` returns the
    WHOLE range: capping an ascending-sorted range would silently return only the
    oldest N rows of it (the caller asks for 11 years, gets 10 days of 2015)."""
    params = {
        "series_id": series_id,
        "api_key": API_KEY,
        "file_type": "json",
        "sort_order": "desc",
    }
    if start:
        params["observation_start"] = start
        params["sort_order"] = "asc"
    if not all_data and limit is not None:
        params["limit"] = limit

    url = f"{BASE}?{urllib.parse.urlencode(params)}"
    data = json.loads(_get(url, timeout=30))
    obs = data.get("observations", [])

    # The truncation trap: FRED licence-caps BAML* to a rolling ~3yr window and
    # returns the WRONG ERA with no error. Never let that pass silently.
    if _warn and start and obs and obs[0]["date"] > start:
        trunc = series_id.upper().startswith(_TRUNCATED_PREFIXES)
        print(f"WARN: {series_id} requested from {start} but first observation is "
              f"{obs[0]['date']} — you did NOT get the range you asked for.",
              file=sys.stderr)
        if trunc:
            print(f"WARN: {series_id} is in the licence-TRUNCATED ICE BofA family "
                  f"(rolling ~3yr). Use --splice for real history (1996->today).",
                  file=sys.stderr)
        else:
            print("WARN: may simply be the series' true start — verify before citing.",
                  file=sys.stderr)
    return obs

def _get(url, retries=3, timeout=60):
    """GET with retry + gzip. SSL/503 drops are routine on both FRED and Wayback."""
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=_UA)
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    import gzip
                    raw = gzip.decompress(raw)
                return raw.decode("utf-8", "replace")
        except Exception as e:                     # noqa: BLE001 — retry anything transient
            last = e
            if i < retries - 1:
                time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"GET failed after {retries} tries: {url} ({last})")


def _resolve_snapshot(series_id):
    """Find a Wayback snapshot timestamp for the raw data endpoint.

    CDX first (authoritative), then the known-good table, then Wayback's
    nearest-snapshot redirect. NOTE: archive.org/wayback/available returns
    FALSE NEGATIVES (reported 0 snapshots for a URL with 5) — do not use it.
    """
    target = f"fred.stlouisfed.org/data/{series_id}.txt"
    try:
        cdx = (f"http://web.archive.org/cdx/search/cdx?url={target}"
               "&output=json&filter=statuscode:200&collapse=digest")
        rows = json.loads(_get(cdx, retries=2, timeout=45))
        if len(rows) > 1:
            return rows[-1][1]          # newest 200 == longest history
    except Exception:
        pass                            # CDX 503s constantly; fall through
    if series_id in _KNOWN_SNAPSHOTS:
        return _KNOWN_SNAPSHOTS[series_id]
    return "2024"                       # Wayback resolves a bare year to nearest


def _parse_fred_txt(text):
    """Parse FRED's raw /data/<ID>.txt dump.

    Three traps this handles, each of which silently corrupts a naive parse:
      * CRLF line endings  -> strip \\r or every value carries one
      * ~67 header lines   -> data starts only after the 'DATE  VALUE' line
      * missing values '.' -> dropped, not coerced to 0
    """
    meta, obs, in_data = {}, [], False
    for line in text.replace("\r", "").split("\n"):
        if not in_data:
            if line.startswith("DATE") and "VALUE" in line:
                in_data = True
            elif ":" in line:
                k, _, v = line.partition(":")
                if k and not k[0].isspace():
                    meta[k.strip()] = v.strip()
            continue
        parts = line.split()
        if len(parts) >= 2 and parts[0][:4].isdigit():
            if parts[1] != ".":                     # '.' == no observation
                obs.append({"date": parts[0], "value": parts[1]})
    return obs, meta


def archive_fetch(series_id, start=None):
    """Recover FULL history via a Wayback snapshot of FRED's raw text endpoint.

    Returns (observations, meta). The provenance header survives in meta
    ('Source', 'Date Range'), which is what makes this citable as [PRIMARY]
    rather than a republisher.
    """
    ts = _resolve_snapshot(series_id)
    url = (f"https://web.archive.org/web/{ts}id_/"
           f"https://fred.stlouisfed.org/data/{series_id}.txt")
    obs, meta = _parse_fred_txt(_get(url))
    if not obs:
        raise RuntimeError(f"archive snapshot parsed to 0 observations: {url}")
    if start:
        obs = [o for o in obs if o["date"] >= start]
    return obs, meta


def splice_fetch(series_id, start=None):
    """Archive history + live API, merged — the way to get 1996->today.

    Self-validates: where the two overlap they must agree. A mismatch is
    reported, never silently smoothed over.
    """
    arch, meta = archive_fetch(series_id)
    # MUST sort: the live API returns DESCENDING unless `start` is passed, so
    # live[0] would be the NEWEST row and the merge would cut at the wrong end.
    live = sorted(fetch(series_id, start=None, all_data=True, _warn=False),
                  key=lambda o: o["date"])
    if not live:
        return arch, meta, "live API returned nothing — archive only"
    cut = live[0]["date"]
    amap = {o["date"]: o["value"] for o in arch}
    overlap = [d for d in (o["date"] for o in live) if d in amap]
    mism = [d for d in overlap
            if amap[d] != next(o["value"] for o in live if o["date"] == d)]
    note = (f"overlap {len(overlap)} obs from {cut}: "
            + ("ALL MATCH ✓" if not mism else
               f"⚠️ {len(mism)} MISMATCH (first {mism[0]}) — DO NOT cite until resolved"))
    merged = [o for o in arch if o["date"] < cut] + live
    if start:
        merged = [o for o in merged if o["date"] >= start]
    return merged, meta, note


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python3 fred_pull.py SERIES_ID [--limit N] [--start YYYY-MM-DD] "
              "[--all] [--csv] [--archive] [--splice]\n"
              "  --archive : full history via Wayback (ICE BofA BAML* are API-truncated)\n"
              "  --splice  : archive + live merged, validated on the overlap")
        return

    series_id = args[0]
    limit = None
    start = None
    all_data = False
    csv_mode = False
    archive = False
    splice = False

    for i, a in enumerate(args[1:], 1):
        if a == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1])
        if a == "--start" and i + 1 < len(args):
            start = args[i + 1]
        if a == "--all":
            all_data = True
        if a == "--csv":
            csv_mode = True
        if a == "--archive":
            archive = True
        if a == "--splice":
            splice = True

    meta, note = {}, None
    if splice:
        obs, meta, note = splice_fetch(series_id, start)
    elif archive:
        obs, meta = archive_fetch(series_id, start)
    else:
        # Default to the latest 10 ONLY for a bare call. With --start, an unset --limit
        # means "the whole range" (see fetch()); capping it would silently drop the range.
        if limit is None and start is None:
            limit = 10
        obs = fetch(series_id, limit, start, all_data)

    # Provenance belongs on stderr so it survives a `--csv > file.csv` redirect
    # instead of corrupting the CSV.
    if meta:
        for k in ("Source", "Date Range", "Units", "Last Updated"):
            if k in meta:
                print(f"# {k}: {meta[k]}", file=sys.stderr)
    if note:
        print(f"# splice: {note}", file=sys.stderr)

    if csv_mode:
        print("date,value")
        for o in obs:
            print(f"{o['date']},{o['value']}")
    else:
        print(f"\n=== {series_id} (Latest {len(obs)} observations) ===\n")
        for o in obs:
            print(f"  {o['date']}  {o['value']}")

if __name__ == "__main__":
    main()
