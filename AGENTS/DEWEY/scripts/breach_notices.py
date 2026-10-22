#!/usr/bin/env python3
"""
State attorney-general breach-notice puller — California + Washington lists,
filtered by organization name and date, with optional notice-text fetch and a
keyword pass that SUGGESTS a breach route. Built 2026-10-22 (Will-greenlit) from
the bank legacy-technology study (88 bank/credit-union notices) and the vendor
study (vendor-filed notices). Stdlib only.

Sources (public, no key):
  CA: https://oag.ca.gov/privacy/databreach/list?field_sb24_org_name_value=<term>&page=N
      (each row links a notice page; notice PDFs hang off that page)
  WA: https://data.wa.gov/resource/sb4j-ca4h.json (Socrata; lists only breaches of
      500+ WA residents; includes residents affected and an attack-type code)
  Maine's database was OFFLINE on 2026-10-22 ("will remain offline").

Usage:
  python3 breach_notices.py --name bank --name "credit union" --name FCU --since 2023-01-01 --out notices.tsv
  python3 breach_notices.py --name Fiserv --name Marquis --since 2020-01-01 --out vendors.tsv
  python3 breach_notices.py --name bank --since 2026-01-01 --out n.tsv --fetch-text --textdir notice_text/

The --fetch-text pass downloads each CA notice page + PDFs (text via pdfminer when
the venv is used) and writes `suggested_route` from keywords. It is a FIRST PASS:
the 2026-10-22 classification was read notice by notice. Lawyer-written notices
omit the entry route ~25% of the time; "not stated" is not "ruled out". WA's
attack-type "Ransomware" also tags MOVEit data theft — do not read it as a route.
"""
import argparse, csv, html, json, os, re, sys, time, urllib.parse, urllib.request

BROWSER = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
CA_LIST = "https://oag.ca.gov/privacy/databreach/list?"
WA_API = "https://data.wa.gov/resource/sb4j-ca4h.json"
ROUTES = [  # order matters: first hit wins
    ("FILE_TRANSFER", r"moveit|goanywhere|accellion|kiteworks|cleo|crushftp|file transfer|sftp"),
    ("EDGE", r"fortinet|citrix|ivanti|pulse secure|sonicwall|barracuda|firewall|vpn"),
    ("EMAIL", r"email account|e-mail account|phishing|business email|mailbox"),
    ("VENDOR", r"third[- ]party (vendor|service provider)|our vendor|a vendor|service provider"),
    ("RANSOMWARE/OWN_NETWORK", r"ransomware|encrypt|network intrusion|unauthorized access to (our|its) network"),
    ("WEBAPP", r"credential stuffing|online (application|portal)|web application"),
]
OLD = re.compile(r"(outdated|unpatched|end[- ]of[- ]life|unsupported|legacy) (software|system|server|version)", re.I)


def fetch(url, timeout=60):
    for i in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": BROWSER})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except Exception as e:
            err = e; time.sleep(2 * (i + 1))
    raise err


def ca_rows(term):
    rows, page = {}, 0
    while True:
        q = urllib.parse.urlencode({"field_sb24_org_name_value": term, "page": page})
        t = fetch(CA_LIST + q).decode("utf-8", "replace")
        found = 0
        for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", t, flags=re.S):
            m = re.search(r'href="(https://oag\.ca\.gov/ecrime/databreach/reports/(sb24-\d+))">(.*?)</a>', tr)
            if not m:
                continue
            cells = [re.sub(r"<[^>]+>", "", c).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", tr, flags=re.S)]
            rows[m.group(2)] = {"source": "CA", "id": m.group(2), "url": m.group(1), "name": html.unescape(m.group(3)).strip(),
                                "breach_dates": cells[1] if len(cells) > 2 else "", "reported": cells[-1] if cells else ""}
            found += 1
        if not found or 'title="Go to next page"' not in t:
            break
        page += 1; time.sleep(0.5)
    for r in rows.values():
        try:
            r["reported"] = time.strftime("%Y-%m-%d", time.strptime(r["reported"], "%m/%d/%Y"))
        except ValueError:
            pass
    return list(rows.values())


def wa_rows(term, since):
    where = f"upper(name) like '%{term.upper().replace(chr(39), '')}%' AND datesubmitted >= '{since}T00:00:00'"
    q = urllib.parse.urlencode({"$where": where, "$limit": 5000})
    out = []
    for r in json.loads(fetch(f"{WA_API}?{q}")):
        out.append({"source": "WA", "id": r.get("id", ""), "name": r.get("name", ""),
                    "url": "https://www.atg.wa.gov/data-breach-notifications",
                    "breach_dates": (r.get("datestart", "")[:10] + " to " + r.get("dateend", "")[:10]).strip(" to"),
                    "reported": r.get("datesubmitted", "")[:10], "wa_residents": r.get("washingtoniansaffected", ""),
                    "wa_cause": r.get("databreachcause", ""), "wa_attack_type": r.get("cyberattacktype", "")})
    return out


def notice_text(r, textdir):
    page = fetch(r["url"]).decode("utf-8", "replace")
    parts = [re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", page)))]
    for i, pdf in enumerate(sorted(set(re.findall(r'href="(https://oag\.ca\.gov/system/files/[^"]+\.pdf)"', page, flags=re.I)))):
        try:
            b = fetch(pdf)
            try:
                import io
                from pdfminer.high_level import extract_text
                parts.append(extract_text(io.BytesIO(b)))
            except ImportError:
                parts.append("[pdfminer not available: run with the venv python]")
        except Exception as e:
            parts.append(f"[pdf fetch failed: {e}]")
    t = "\n".join(parts)
    if textdir:
        os.makedirs(textdir, exist_ok=True)
        open(os.path.join(textdir, r["id"] + ".txt"), "w").write(t)
    return t


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--name", action="append", required=True, help="organization-name term (repeatable)")
    ap.add_argument("--since", default="2023-01-01")
    ap.add_argument("--exclude", default=r"Bankers Life|Food Bank|Cryobank|BankCard USA|American Bankers")
    ap.add_argument("--out", required=True)
    ap.add_argument("--fetch-text", action="store_true", help="CA only: fetch notice pages/PDFs and suggest a route")
    ap.add_argument("--textdir")
    a = ap.parse_args()
    excl = re.compile(a.exclude, re.I) if a.exclude else None
    rows = {}
    for term in a.name:
        for r in ca_rows(term) + wa_rows(term, a.since):
            if r["reported"] >= a.since and not (excl and excl.search(r["name"])):
                rows[(r["source"], r["id"])] = r
        print(f"  {term}: {len(rows)} notices so far", file=sys.stderr)
    out = sorted(rows.values(), key=lambda r: r["reported"])
    if a.fetch_text:
        for i, r in enumerate(out):
            if r["source"] != "CA":
                continue
            try:
                t = notice_text(r, a.textdir).lower()
            except Exception as e:
                r["suggested_route"] = f"FETCH_FAILED {type(e).__name__}"; continue
            r["suggested_route"] = next((n for n, p in ROUTES if re.search(p, t)), "NOT_STATED")
            r["old_software_phrase"] = (OLD.search(t).group(0) if OLD.search(t) else "")
            if i % 20 == 0:
                print(f"  text {i}/{len(out)}", file=sys.stderr)
            time.sleep(0.3)
    cols = ["source", "id", "reported", "name", "breach_dates", "url", "wa_residents", "wa_cause", "wa_attack_type",
            "suggested_route", "old_software_phrase"]
    with open(a.out, "w", newline="") as fo:
        w = csv.DictWriter(fo, fieldnames=cols, delimiter="\t", extrasaction="ignore"); w.writeheader(); w.writerows(out)
    print(f"{len(out)} notices -> {a.out} (CA {sum(r['source']=='CA' for r in out)}, WA {sum(r['source']=='WA' for r in out)})")


if __name__ == "__main__":
    main()
