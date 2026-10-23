# eMudhra key compromise: will Chrome's 27 Oct root removal break non-browser financial software?
**Date:** 2026-10-22 (research 21:35–21:45 ET) | **Mode:** Thesis | **Confidence:** High on trust-store actions read at the primaries (Google, Oracle, OpenJDK, Mozilla, CERT-In, eMudhra); Medium on the breakage read (no measured breakage; dependency map incomplete)
**Commission:** Will-directed in the DEWEY session, 21:33 ET (Will's pick #2). No REQ. Tests CYPHER FLOW `FL-CYP-17` (CA trust failure → root removed → non-browser trading software breaks; UNTESTED) and CYPHER docket row 2026-10-27. WALTER pointer folded in: the OpenJDK advisory (BOARD 045).

## Key Finding
**The 27 Oct date is a Chrome-only event. Non-browser financial software is mostly governed by other trust stores, and those have already acted.**
- **Chrome** removes **emSign ECC Root CA - G3** from the Chrome Root Store on "Tuesday morning, October 27, 2026 PDT". Google says "Some legitimate certificates chaining to this root will cease to function in Chrome". That affects Chrome and Chrome-Root-Store consumers, not Java, Windows or Linux system stores.
- **Bank and vendor software** mostly runs on Java, Windows Schannel or Linux system stores:
  - **Oracle Java and standalone OpenJDK** block only the **eight compromised intermediates** (Oracle: "distrusts the set of impacted intermediate CA certificates related to eMudhra").
  - **Windows** blocks the intermediates "without modifying Trusted Root Certification Authorities".
  - eMudhra says those intermediates issued no end-entity certificates (NEWS), so blocking them should break nothing legitimate.
- **The real breakage channel is Linux and open-source bundles that *removed roots* on 19–20 Oct:** Mozilla NSS 3.131.1, Python certifi, curl's bundle, Debian, Ubuntu, Alpine. Linux-packaged Java inherits those removals. **Debian, and Ubuntu before 22.04, also removed the old Sectigo "AAA Certificate Services" root**, which is unrelated to eMudhra and so is a wider knock-on (DEWEY reading of the chains).
- **No breakage in finance has been reported**, and RBI, SEBI, NPCI, NSE and BSE have issued no statement. India's regulated digital-signature (DSC/eSign) system is on separate infrastructure and "not impacted" (CERT-In).
- **So what for 27 Oct:** expect little financial-system effect from Chrome's step itself. Watch for Linux-hosted API clients failing against servers still using eMudhra or legacy-AAA chains. That started on 19–20 Oct, not on 27 Oct.
- **Premise correction:** this was a **key compromise** (weak randomness at a 30 Apr 2025 key ceremony, per eMudhra), credited to a community reporter on 17 Oct. **No Cisco Talos report was found.** DEWEY's earlier watch-legs report relayed a search summary attributing it to Talos; that line is corrected in the same commit as this report.

## Evidence

### 1. Trust-store actions

| Store | Action | Effective | Scope | Source | Basis (Class 12) |
|---|---|---|---|---|---|
| Chrome Root Store | CRLSet blocks the intermediates' public keys; **removes emSign ECC Root CA - G3** | Block 17 Oct 19:45 UTC; removal released ~27 Oct AM PDT | Chrome and Chrome-Root-Store consumers | [PRIMARY: Google, 20 Oct](https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/) | PRIMARY-VERIFIED (DEWEY read). The post says "eight" in its summary and "six" in its CT paragraph; six TLS + two code-signing = 8 |
| Android / Googlebooks | Equivalent block via Play Services | ~22:00 UTC "Monday" (19 Oct) | Devices; no system root-store change found | same | PRIMARY-VERIFIED |
| Oracle Java SE | Security Alert CVE-2026-91403: distrusts the impacted **intermediates**; no root removal mentioned | 21 Oct | 8u511, 11.0.33, 17.0.21, 21.0.13, 25.0.5, 27.0.1; GraalVM 17/21 | [PRIMARY: Oracle](https://www.oracle.com/security-alerts/alert-CVE-2026-91403.html) | PRIMARY (helper read) |
| OpenJDK | "CVE-2026-91403 concerns eight compromised intermediate CA certificates"; CVSS 9.1; the **listed versions are the AFFECTED ones** (27.0.1, 25.0.5, 21.0.13, 17.0.21, 11.0.32.1, 8u504 and earlier), **not the fixed ones as relayed in a cross-session message**. Interim fix: replace `lib/security/blocked.certs` (JDK 8: `blacklisted.certs`), which works by fingerprint. OS-packaged Java "most likely uses the operating system's certificates" | 21 Oct | JDK 8–27 | [PRIMARY: OpenJDK](https://openjdk.org/groups/vulnerability/advisories/2026-10-21) | PRIMARY (helper read). *Corrects the "fixed in" wording in WALTER's cross-session message to DEWEY (21:34 ET); BOARD 045 itself correctly says "affects Java 8, 11, 17, 21, 25, 27" (re-worded 21:47 ET on WALTER's flag)* |
| Microsoft Windows | Intermediates added to Untrusted; trusted roots untouched | 20 Oct | Schannel, Authenticode | [community tracker run by Mozilla's Dennis Jackson](https://emudhra.we-have-a-problem.com) | SECONDARY-SOURCE (no Microsoft notice found) |
| Mozilla OneCRL / Firefox | Intermediates blocked; Firefox 158.0.1 / ESR updates (CVE-2026-113470) | 17 / 20 Oct | Firefox | PRIMARY: Mozilla security blog, 20 Oct (full URL not captured) | PRIMARY (helper read) |
| **Mozilla NSS 3.131.1** | **Root removed**; which roots is in conflict: G3 only (The Hacker News) vs G3 + emSign Root CA - C1 + ECC C3 (Rescana) | 20 Oct | Everything built on NSS: curl, certifi, Node, distros | same | PRIMARY (unnamed root); root list unresolved |
| Python certifi / curl / Perl Mozilla::CA | G3 dropped (certifi 2026.10.19) | 19–20 Oct | requests, pip, curl | community tracker; Rescana | SECONDARY-SOURCE |
| Debian (DSA-6572-1) / Ubuntu (USN-8944) | Remove **emSign ECC G3 and Comodo/Sectigo AAA Certificate Services** (Ubuntu: AAA only before 22.04) | 20 Oct | System store, including OS-packaged OpenJDK | [NEWS: The Hacker News](https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html) | SECONDARY-SOURCE |
| RHEL (RHSB-2026-012) | Affected; packages pending 21 Oct | — | RHEL 6–10 | same | SECONDARY-SOURCE |
| Apple | Intermediates blocked (date conflict: 19 vs 22 Oct); macOS `/etc/ssl/cert.pem` not updated | — | — | community tracker | SECONDARY-SOURCE |
| Go / Node.js | Go 1.27.3 / 1.26.10 block the keys (rebuild needed); Node 22/24/26 updates adopt NSS 3.131.1 | 19–21 Oct | — | Rescana | SECONDARY-SOURCE |

### 2. What was compromised
- Eight intermediates: EM DV/OV/EV TLS CA - G3B and G3C (6 TLS), plus EM OV CS CA - G3B and G3C (2 code-signing). Each is cross-signed by Sectigo under AAA Certificate Services. eMudhra revoked them on 18 Oct and Sectigo revoked its cross-signs on 19 Oct ([oss-security](https://www.openwall.com/lists/oss-security/2026/10/20/1), PRIMARY, helper read).
- eMudhra (21 Oct, PRIMARY): a flawed 30 Apr 2025 key ceremony; "The weak keys were the ones published to the browser root stores." DSC and eSign run on separate infrastructure and are unaffected. Global TLS is ~1% of revenue. Per NEWS: only 1 of the 8 was in production, none issued end-entity certificates, and a BSE filing says there was no data breach. Shares fell 20% on 21 Oct. On 22 Oct eMudhra announced its exit from global SSL/TLS (headline only).
- Mozilla (19 Oct, PRIMARY): "there are other intermediates under these roots which have been used by eMudhra to sign customer certificates. Consequently, removing trust in these roots may cause some servers to become unavailable." **This is the mechanism behind the root-removal breakage channel.**

### 3. Who in finance depends on it
- **India:** CERT-In CIAD-2026-0050 (21 Oct, PRIMARY): CCA-regulated DSC and eSign are "not impacted". Its advisory urges organisations to check runtimes, containers and embedded devices that carry their own CA bundles, and says it does "not establish confirmed malicious exploitation". No named bank, NPCI, NSE/BSE or SEBI TLS customer was found. Reuters (via DQIndia, UNVERIFIED) names the income-tax portal among eMudhra TLS customers.
- **Scale:** ~30,000 certificates chain to G3 (UNVERIFIED, search summary).
- **Global banks/vendors:** no named dependency found. **SEARCH-NOT-FOUND** (weak).

### 4. Precedents
- Entrust distrust (2024): SSLMate predicted non-browser bundles would diverge and warned about "API endpoints… accessed by non-browser clients", but **documented no actual outages and no finance cases**. Symantec 2017–18 was not reached.

### 5. CYPHER FLOW `FL-CYP-17` read
The route "root removed → non-browser trading software breaks" needs a *non-browser* store to remove the root. That **has happened** (NSS, certifi, curl, Debian, Ubuntu, Alpine, on 19–20 Oct). **Observed breakage is zero so far**, so the row stays UNTESTED → candidate NOT-OBSERVED pending ~2 weeks of silence. The 27 Oct Chrome step does not test it.

## Counter-Evidence
- **For breakage:** Mozilla itself warns that root removal "may cause some servers to become unavailable". About 30,000 certificates chain to G3, and the Debian AAA removal reaches far beyond eMudhra. Containerised Linux services (common at fintechs) update CA bundles with base images, so failures could surface erratically over weeks and be misattributed.
- **Against breakage:** eMudhra says global TLS is ~1% of its revenue, and its India digital-signature business is untouched. Java and Windows (the bank and vendor mainstream) block only intermediates that issued no customer certificates. CERT-In and Indian officials say the impact was "very limited and for a very short period" (NEWS). Precedent distrusts produced no documented finance outages.

## Source Quality Assessment
Strong on Chrome, Oracle, OpenJDK, Mozilla, eMudhra and CERT-In (primaries). Medium on the Linux distro actions (news). Weak on the finance dependency map (no named customers; RBI, SEBI and NPCI silent). Java `cacerts` root content was not confirmed (ops.java returned 403).

## References
- Google: https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/
- Oracle alert: https://www.oracle.com/security-alerts/alert-CVE-2026-91403.html
- OpenJDK advisory: https://openjdk.org/groups/vulnerability/advisories/2026-10-21
- Mozilla security blog post, 20 Oct 2026: blog.mozilla.org/security/2026/10/20/… (full slug not captured)
- oss-security: https://www.openwall.com/lists/oss-security/2026/10/20/1
- Community tracker: https://emudhra.we-have-a-problem.com
- The Hacker News: https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html
- CERT-In CIAD-2026-0050: https://www.cert-in.org.in/
- SSLMate (Entrust): https://sslmate.com/

## Process Report
**Searches run:** one helper (26 tool calls, DATA-RETURN, no repo writes), with WALTER's Java pointer relayed mid-run. DEWEY re-read the Google primary.
**Data gaps:** Java `cacerts` content, Microsoft and Apple primaries, the exact NSS root list, named finance customers, RBI/SEBI/NPCI statements, Symantec precedent.
**Source frustrations:** ops.java returned 403. The Mozilla blog post names no root.
**Confidence in findings:** High on what each store did; Medium on "little financial breakage".
**If I had more time/tools:** read NSS certdata to settle the root list; check eMudhra's BSE filing text.
**Suggestions:** CYPHER could re-time its 10/27 docket row to "19–20 Oct root removals (NSS / Debian / certifi) + 27 Oct Chrome". The breakage watch belongs on the earlier date.
