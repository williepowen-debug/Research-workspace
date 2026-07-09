#!/usr/bin/env python3
"""
trace_bond — single-name corporate-bond IDENTIFICATION + honest price-wall helper.

WHAT THIS DOES (and honestly does NOT do):
  - RESOLVES an issuer/ticker -> its bond instruments (coupon, maturity, FIGI, TRACE listing)
    via OpenFIGI (free, no key needed; a key raises the rate limit). This is the leg that is
    genuinely hard to do by hand and it WORKS.
  - For a live PRICE / YIELD / SPREAD it does NOT fabricate. Per-CUSIP TRACE last-price is
    NOT available from any reliable free/unauth endpoint (probed 2026-07-09: FINRA per-trade
    corporate data needs an authenticated account; the legacy Morningstar bond endpoint is
    dead). `quote` therefore emits the resolved instruments + the exact manual-lookup URL and
    states plainly that the price leg needs a FINRA-authenticated API or a terminal.
    A cited "no free price source" beats an invented number (DEWEY discipline).

WHY IT EXISTS: single-name HY spreads are the fleet credit-canary instrument (CRWV 2030/2031,
  APLD 2030, DISH, any HY issuer slide). This helper does the resolution + codifies the price
  wall so each run doesn't re-discover it. Surfaced by BACKLOG (2nd surface: prompts 05 + 18).

Usage:
  python3 trace_bond.py resolve "CoreWeave"                 # issuer name -> its bonds
  python3 trace_bond.py resolve "CRWV" --type Corp          # ticker works too
  python3 trace_bond.py map 12345AB67 --idtype ID_CUSIP     # CUSIP/ISIN -> security identity
  python3 trace_bond.py quote "CoreWeave"                    # bonds + manual price-lookup path
  python3 trace_bond.py resolve "Applied Digital" --json     # raw JSON out

Run with the repo-root venv:
  /home/willi/Research-workspace/.venv/bin/python3 AGENTS/DEWEY/scripts/trace_bond.py resolve "CoreWeave"

Optional: set OPENFIGI_API_KEY in env to raise the OpenFIGI rate limit (search works without it).
"""

import argparse, json, os, sys, time, urllib.request, urllib.error

OPENFIGI_SEARCH = "https://api.openfigi.com/v3/search"
OPENFIGI_MAP = "https://api.openfigi.com/v3/mapping"
# Manual price-lookup surface for a human/terminal (the honest fallback for the price leg):
FINRA_MARKETS_BOND = "https://www.finra.org/finra-data/fixed-income/corp-and-agency"
UA = "DEWEY-research williepowen@gmail.com"


def _post(url, payload, retries=3, backoff=1.5):
    """POST JSON with a UA header + SSL/transient retry (BACKLOG item 6: SEC/FRED/FINRA
    single calls drop occasionally). Returns parsed JSON or raises the last error."""
    body = json.dumps(payload).encode()
    headers = {"Content-Type": "application/json", "User-Agent": UA}
    key = os.environ.get("OPENFIGI_API_KEY", "")
    if key:
        headers["X-OPENFIGI-APIKEY"] = key
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=body, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=25) as resp:
                return json.loads(resp.read().decode())
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as e:
            last = e
            if attempt < retries - 1:
                time.sleep(backoff * (attempt + 1))
    raise last


def resolve(query, sec_type="Corp"):
    """Issuer name or ticker -> list of matching bond instruments (paged via OpenFIGI)."""
    out, start = [], None
    while True:
        payload = {"query": query, "securityType2": sec_type}
        if start:
            payload["start"] = start
        data = _post(OPENFIGI_SEARCH, payload)
        rows = data.get("data", [])
        out.extend(rows)
        start = data.get("next")
        if not start or len(out) >= 200:  # cap: don't page forever
            break
    return out


def map_id(id_value, id_type="ID_CUSIP"):
    data = _post(OPENFIGI_MAP, [{"idType": id_type, "idValue": id_value}])
    if data and isinstance(data, list) and data[0].get("data"):
        return data[0]["data"]
    return []


def _fmt(rows):
    if not rows:
        return "  (no instruments found — try the issuer's legal name, or --type Corp/Govt)"
    lines = [f"  {'TICKER (coupon/maturity)':<34} {'DESCRIPTION':<26} {'FIGI':<14} EXCH"]
    for r in rows:
        lines.append(f"  {r.get('ticker',''):<34} {r.get('securityDescription',''):<26} "
                     f"{r.get('figi',''):<14} {r.get('exchCode','')}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Single-name corp-bond resolver + price-wall helper")
    sub = ap.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("resolve", help="issuer/ticker -> bond instruments")
    r.add_argument("query")
    r.add_argument("--type", default="Corp", help="securityType2 (Corp default; Govt, Muni, ...)")
    r.add_argument("--json", action="store_true")

    m = sub.add_parser("map", help="CUSIP/ISIN -> security identity")
    m.add_argument("id_value")
    m.add_argument("--idtype", default="ID_CUSIP", help="ID_CUSIP | ID_ISIN | ID_BB_GLOBAL")
    m.add_argument("--json", action="store_true")

    q = sub.add_parser("quote", help="bonds + manual price-lookup path (price leg is NOT free)")
    q.add_argument("query")
    q.add_argument("--type", default="Corp")

    a = ap.parse_args()
    try:
        if a.cmd == "resolve":
            rows = resolve(a.query, a.type)
            print(json.dumps(rows, indent=2) if a.json else
                  f"=== {a.query} — bond instruments (OpenFIGI/TRACE) ===\n{_fmt(rows)}")
        elif a.cmd == "map":
            rows = map_id(a.id_value, a.idtype)
            print(json.dumps(rows, indent=2) if a.json else
                  f"=== {a.idtype} {a.id_value} ===\n{_fmt(rows)}")
        elif a.cmd == "quote":
            rows = resolve(a.query, a.type)
            print(f"=== {a.query} — instruments ===\n{_fmt(rows)}\n")
            print("PRICE / YIELD / SPREAD: not available from any free/unauth source.")
            print("  Per-CUSIP TRACE last-price needs a FINRA-authenticated API account or a")
            print("  terminal (ICE/Bloomberg). Route the live spread to LIQUID/HENRY's terminal.")
            print(f"  Manual lookup (human/terminal): {FINRA_MARKETS_BOND}")
            print("  (This tool resolves the instrument identity; it will NOT invent a price.)")
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
