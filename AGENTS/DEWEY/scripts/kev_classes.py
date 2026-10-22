#!/usr/bin/env python3
"""
CISA KEV by product class (+ optional NVD published-CVE counts by keyword).
Answers "is product type X the kind that gets exploited in the wild?" Built
2026-10-22 (Will-greenlit) from the bank-vendor product-class study (0 of 1,754
KEV entries were banking software; file transfer 61% ransomware-linked). Stdlib only.

Usage:
  python3 kev_classes.py                       # class table from the live KEV feed
  python3 kev_classes.py --since 2023-01-01    # adds a "dateAdded since" column
  python3 kev_classes.py --list "file transfer"           # entries in one class
  python3 kev_classes.py --nvd Fiserv "Jack Henry" MOVEit  # NVD keyword CVE counts
  python3 kev_classes.py --cve CVE-2026-109618 CVE-2026-109619   # are these in KEV?

Classes are regex rules on vendorProject + product, applied in order (first hit
wins) — edit CLASSES below to add a class. "other" holds ~36%; spot-check before
citing a small class. NVD keywordSearch counts description mentions, not only
flaws in that vendor's products (PHP/WordPress counts include apps and plugins);
NVD allows ~5 requests / 30 s without a key, so --nvd sleeps 7 s between terms.
"""
import argparse, collections, json, re, sys, time, urllib.parse, urllib.request

KEV = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
NVD = "https://services.nvd.nist.gov/rest/json/cves/2.0"
CLASSES = [
    ("banking/fintech software", r"fiserv|jack henry|\bfis\b|fidelity national|finastra|temenos|q2 |alkami|ncino|\bncr\b|diebold|"
                                 r"evertec|corelation|hyland|bottomline|aci worldwide|flexcube|finacle|symitar|backbase"),
    ("file transfer", r"moveit|goanywhere|accellion|kiteworks|crushftp|serv-u|cleo|wing ftp|sftp|filezilla"),
    ("edge: VPN/firewall/gateway", r"fortinet|forti|ivanti|pulse|citrix|netscaler|sonicwall|palo alto|pan-os|cisco asa|firepower|"
                                   r"adaptive security|f5|big-ip|barracuda|zyxel|check point|checkpoint|juniper|sophos|watchguard|"
                                   r"array networks|sangfor|draytek"),
    ("PHP runtime / PHP apps & CMS", r"\bphp\b|wordpress|drupal|joomla|magento|vbulletin|phpmyadmin|thinkphp|laravel|craft cms|"
                                     r"roundcube|zimbra|horde|cacti|glpi|elfinder|wp "),
    ("open-source libs/runtimes (non-PHP)", r"apache|log4j|struts|spring|jenkins|openssl|redis|elasticsearch|confluence|jira|"
                                            r"atlassian|gitlab|nginx|tomcat|rails|node|python|linux kernel|sudo|polkit|bash|exim|samba"),
    ("Microsoft", r"microsoft|windows|exchange|sharepoint|office|internet explorer|\.net"),
    ("Apple/Google/mobile/browser", r"apple|ios|macos|safari|google|chrome|android|webkit|mozilla|firefox|samsung|qualcomm"),
    ("VMware/virtualization/backup", r"vmware|vcenter|esxi|veeam|commvault"),
]
CR = [(n, re.compile(p, re.I)) for n, p in CLASSES]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=90).read())


def cls(x):
    s = x["vendorProject"] + " " + x["product"]
    return next((n for n, r in CR if r.search(s)), "other")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--since", default="2023-01-01")
    ap.add_argument("--list", help="print the entries in one class")
    ap.add_argument("--nvd", nargs="*", help="NVD keyword terms to count")
    ap.add_argument("--cve", nargs="*", help="check whether these CVE IDs are in KEV")
    a = ap.parse_args()

    d = get(KEV); v = d["vulnerabilities"]
    print(f"KEV catalog {d['catalogVersion']} · released {d['dateReleased'][:10]} · {len(v)} entries")
    if a.cve:
        ids = {x["cveID"]: x for x in v}
        for c in a.cve:
            x = ids.get(c)
            print(f"  {c}: " + (f"IN KEV, added {x['dateAdded']} ({x['vendorProject']} {x['product']}; ransomware {x['knownRansomwareCampaignUse']})" if x else "NOT in KEV"))
    by, rec, rw = collections.Counter(), collections.Counter(), collections.Counter()
    for x in v:
        c = cls(x); by[c] += 1
        rec[c] += x["dateAdded"] >= a.since
        rw[c] += x.get("knownRansomwareCampaignUse") == "Known"
    tr = sum(rec.values())
    print(f"\n{'class':38s} {'all':>5s} {'share':>6s} {'since '+a.since:>17s} {'share':>6s} {'ransomware':>11s}")
    for c, n in by.most_common():
        print(f"{c:38s} {n:5d} {n/len(v)*100:5.1f}% {rec[c]:17d} {rec[c]/tr*100 if tr else 0:5.1f}% {rw[c]:5d} ({rw[c]/n*100:3.0f}%)")
    if a.list:
        print(f"\nentries in '{a.list}':")
        for x in sorted((x for x in v if cls(x) == a.list), key=lambda x: x["dateAdded"]):
            print(f"  {x['dateAdded']} {x['cveID']:18s} {x['vendorProject']} {x['product']} · ransomware {x['knownRansomwareCampaignUse']}")
    if a.nvd:
        print("\nNVD published CVEs by keyword (description match, rejected excluded):")
        for t in a.nvd:
            try:
                n = get(f"{NVD}?keywordSearch={urllib.parse.quote(t)}&resultsPerPage=1&noRejected")["totalResults"]
            except Exception as e:
                n = f"ERR {type(e).__name__}"
            print(f"  {t:40s} {n}", flush=True)
            time.sleep(7)


if __name__ == "__main__":
    main()
