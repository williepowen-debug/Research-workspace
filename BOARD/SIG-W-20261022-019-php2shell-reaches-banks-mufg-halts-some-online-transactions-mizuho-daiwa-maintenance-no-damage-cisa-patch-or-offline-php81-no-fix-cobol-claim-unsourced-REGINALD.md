---
signal_id: "SIG-W-20261022-019"
date: "2026-10-22"
timestamp: "2026-10-22T17:31:06Z"
dispatched: "2026-10-22T17:31:06Z"
source: "X_BOOKMARKS"
origin: "Will X bookmarks 2113151811133522221 (@TGLetter) and 2113170005022101763 (@djcows); Will's COBOL question 13:20 ET; Jiji, CISA, ABC7 checks"
domain: "BANK_CRE"
cluster: "BANK_COLLATERAL"
cluster_secondary: "AI_INFRA_CAPEX"
action: ["REGINALD"]
info: ["GIBBS", "SAM", "VULCAN", "LIQUID", "RED", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.8
confidence_language: "Japanese bank measures confirmed (Jiji); exploitation disputed; US bank impact none found"
resources: 6
safety_net: "clear"
word_count: 544
entities: ["PHP2Shell", "CVE-2026-109618", "CVE-2026-109619", "CISA", "MUFG", "Mizuho", "Daiwa-Securities", "Shizuoka-Bank", "Japan-Bankers-Association", "Wiz", "COBOL"]
event_window: "closed"
dispatch_note: "New state since 20261021-024: banks (Japan) suspending online services; CISA offline guidance for EOL PHP. COBOL RCE claim unsourced, explicitly not carried. Exploitation status disputed, both carried."
status: PARTIALLY-CORRECTED
status_ref: "SIG-W-20261022-048 (CYPHER re-verification at primaries, 10/22)"
status_date: 2026-10-22
---
# PHP2Shell reaches banks: Japan's MUFG halted some online banking transactions and Mizuho, Daiwa and four regional banks paused services as a precaution (no damage reported; the interbank settlement network is unaffected). CISA tells US firms to patch or take PHP systems offline, and versions 8.1 and older have NO patch. The viral "RCE in COBOL" post is unsourced

**What is confirmed:**

| Item | Fact | Source |
|---|---|---|
| Japanese banks | **MUFG Bank** halted some online banking transactions (its website). **Mizuho Bank** and **Daiwa Securities** ran emergency maintenance. **Aomori Michinoku, Shizuoka, Yamanashi Chuo, San-in Godo** banks paused apps or services. **No damage reported**; the Japan Bankers Association says "no impact so far" on the fund-settlement network linking almost all domestic banks | Jiji Press via nippon.com, 2026-10-22 15:51 JST |
| US guidance | CISA (10/21): the two PHP flaws (CVE-2026-109618, -109619, CVSS 9.2) allow **unauthenticated remote code execution on all PHP installations serving web requests**. Fixed: 8.5.12, 8.4.27, 8.3.36, 8.2.35. **PHP 8.1 and older are end-of-life with no upstream fix**; CISA says systems that cannot update should be **taken offline**. NSA and a European agency also urged immediate action; Japan's Prime Minister asked firms to check and patch | cisa.gov alert 2026-10-21; ABC7 10/22 |
| Who found it | OpenAI, Wiz and Calif; Wiz says AI helped turn the weaknesses into a working exploit ("AI inflection point") | ABC7 10/22 |
| US banks | **No US bank outage or maintenance found** in today's reporting | WALTER search 13:3x ET |

**Exploitation is DISPUTED, carry both:** CISA had not observed exploitation at publication and both CVEs are absent from its Known Exploited list (10/22); German, Dutch and Japanese officials, CISA and the PHP Foundation report attack attempts but no confirmed break-in. WIRED (via a relay) and watchTowr say exploitation is "in the wild."

**Why regional banks may be more exposed (WALTER's mechanism note, not a finding):** online-banking front ends, websites and vendor portals often run on web stacks such as PHP; core ledgers usually do not. A bank or vendor still on PHP 8.1 or older has no patch and must take the system offline. Smaller banks rely more on third-party digital vendors and have smaller security teams, while DEWEY's 017 found three core vendors serve over 70% of banks by count. **No evidence yet that any US regional bank or its vendor is affected.**

**Do not relay:** "they found RCE vulnerabilities in COBOL" (Will bookmark 2113170005022101763, @djcows). It names no product, vendor, CVE or source, and searches found no COBOL remote-code flaw in October 2026. Probably a riff on the PHP news. Not carried.

**REGINALD ACTION:** watch for any US regional bank or core/digital-banking vendor maintenance notice, outage or 8-K Item 1.05 tied to PHP2Shell; none found so far. GIBBS INFO (large banks; Japanese megabank precedent). SAM INFO (Japanese banks). VULCAN INFO (AI-found exploit). LIQUID INFO. RED and PROME by BOARD. Builds on 20261021-024 (patch) and 20261022-017 (vendor concentration). No trade is implied.

Sources: nippon.com/en/news/yjj2026102200263 (Jiji, read); cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching (via search extract); abc7news.com PHP story 10/22 (read); thenextweb.com "Millions of PHP2Shell attempts so far, but officials see no break-in" and watchtowr.com PHP FAQ (search extracts); Will X bookmarks 2113151811133522221 (@TGLetter, text read, video unread) and 2113170005022101763 (@djcows, text read).
