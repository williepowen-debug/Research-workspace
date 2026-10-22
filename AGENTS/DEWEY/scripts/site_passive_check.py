#!/usr/bin/env python3
"""
Passive website check — what a bank's or vendor's public homepage openly
declares about its software, which certificate authority issued its TLS
certificate, and which outside hosts its login/online-banking links point to.
Built 2026-10-22 (Will-greenlit) from the bank legacy-technology and vendor
studies (26 banks, 13 vendors). Stdlib only.

GUARDRAIL (Will-approved scope, 2026-10-22): ONE normal homepage page load per
domain with a browser user agent, plus the TLS handshake any browser makes.
No scanning, no probing, no extra paths. Findings about named banks stay in the
desk report — never post them to the BOARD as a list of exposed banks.

Usage:
  python3 site_passive_check.py westernalliancebank.com ozk.com my100bank.com
  python3 site_passive_check.py --file domains.txt --out checks.json

Records: final URL, HTTP status, Server / X-Powered-By / Via / X-Generator headers,
<meta name="generator">, CMS markers (WordPress: wp-content/wp-includes/wp-json;
Drupal: drupal-settings-json/data-drupal//sites/default/files; AEM; Sitecore),
jQuery file versions, external login hosts, and the served certificate's issuer.
Flags: PHP_CMS (WordPress/Drupal = PHP underneath), PHP_DECLARED (version shown),
EMUDHRA_CERT.

CAVEATS: homepages are marketing sites, usually separate from online banking and
core systems; a PHP-based site is POSSIBLE exposure to a PHP flaw, not a confirmed
vulnerability; CDN headers hide the origin server; ~1 in 4 bank sites return 403
to scripted reads — report them as "not observed".
"""
import argparse, datetime, json, re, socket, ssl, sys, urllib.parse, urllib.request

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
HEADERS = ["Server", "X-Powered-By", "X-AspNet-Version", "X-Generator", "Via", "X-Cache"]


def issuer(host):
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((host, 443), timeout=10) as s:
            with ctx.wrap_socket(s, server_hostname=host) as ss:
                c = ss.getpeercert()
        iss = dict(x[0] for x in c["issuer"])
        return f'{iss.get("organizationName", "?")} / {iss.get("commonName", "?")}'
    except Exception as e:
        return f"ERR {type(e).__name__}"


def check(domain):
    host = domain if domain.startswith("www.") or domain.count(".") > 1 else "www." + domain
    r = {"domain": domain, "checked_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")}
    try:
        req = urllib.request.Request(f"https://{host}/", headers={"User-Agent": UA, "Accept": "text/html"})
        with urllib.request.urlopen(req, timeout=25) as resp:
            body = resp.read(1_500_000).decode("utf-8", "ignore")
            r["final_url"], r["status"] = resp.geturl(), resp.status
            for k in HEADERS:
                if resp.headers.get(k):
                    r[k] = resp.headers.get(k)
    except Exception as e:
        r["error"] = f"{type(e).__name__}: {str(e)[:80]}"
        body = ""
    if body:
        r["generator"] = "; ".join(re.findall(r'<meta[^>]+name=["\']generator["\'][^>]+content=["\']([^"\']+)', body, re.I)[:2])
        wp = [m for m in ("wp-content", "wp-includes", "wp-json") if m in body]
        dr = [m for m in ("drupal-settings-json", "data-drupal", "/sites/default/files") if m in body]
        r["cms"] = ("WordPress " + "+".join(wp)) if wp else ("Drupal " + "+".join(dr)) if dr else \
                   ("AEM" if ("/etc.clientlibs" in body or "/content/dam" in body) else "Sitecore" if "sitecore" in body.lower() else "")
        r["jquery"] = sorted(set(re.findall(r"jquery[.-]?(\d\.\d+(?:\.\d+)?)(?:\.min)?\.js", body, re.I)))[:3]
        base = urllib.parse.urlparse(r.get("final_url", "")).hostname or host
        root = ".".join(base.split(".")[-2:])
        hosts = set()
        for m in re.finditer(r'(?:href|action)=["\'](https?://[^"\'/]+)', body, re.I):
            hn = urllib.parse.urlparse(m.group(1)).hostname or ""
            ctx = body[max(0, m.start() - 200):m.end() + 200].lower()
            if hn and root not in hn and (m.group(0).lower().startswith("action") or
                                          any(k in ctx for k in ("log in", "login", "sign in", "online banking", "olb", "enroll"))):
                hosts.add(hn)
        r["login_hosts"] = sorted(hosts)[:8]
    r["cert_issuer"] = issuer(host)
    flags = []
    if r.get("cms", "").startswith(("WordPress", "Drupal")):
        flags.append("PHP_CMS")
    if "php" in (r.get("X-Powered-By", "") + r.get("Server", "")).lower():
        flags.append("PHP_DECLARED")
    if "emudhra" in r["cert_issuer"].lower() or "emsign" in r["cert_issuer"].lower():
        flags.append("EMUDHRA_CERT")
    r["flags"] = flags
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("domains", nargs="*")
    ap.add_argument("--file")
    ap.add_argument("--out")
    a = ap.parse_args()
    doms = a.domains + ([l.split()[0] for l in open(a.file) if l.strip() and not l.startswith("#")] if a.file else [])
    res = []
    for d in doms:
        r = check(d); res.append(r)
        show = {k: v for k, v in r.items() if k not in ("domain", "checked_utc") and v not in ("", [], None)}
        print(f"{d:28s} {json.dumps(show)[:400]}")
    if a.out:
        json.dump(res, open(a.out, "w"), indent=1)


if __name__ == "__main__":
    main()
