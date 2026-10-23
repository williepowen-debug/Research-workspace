# CYPHER evidence record: evening intake, 2026-10-23 (16:58 to 17:25 ET)

**Scope:** WALTER signals SIG-W-20261023-041, -044 and -045, plus five inbox packets (BRENT, FALCON, VULCAN boundary confirmations; DEWEY Korea; DEWEY NCUA). **Commits:** 44fa81df3 (ledgers), 3bbb27366 (brief and catalyst), 62c2fff5d (intake rule), 5f8693abb (re-pin). **Result:** no escalation row fired; 6 incident rows added (026 to 031); CYB-INC-022 upgraded; 2 KB rows (036, 037).

This file keeps the exact quotes and URLs behind those rows. The rows carry the verdicts; this file carries the reads.

## 1. Primary reads

| Item | URL (read by CYPHER, 2026-10-23) | Verbatim / exact content | Ledger |
|---|---|---|---|
| GitLab CVE-2026-110264 | docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-1-released/ (WebFetch 17:0x ET; the about.gitlab.com URL 301-redirects) | Title "Integer Overflow issue in Regular Expression Compiler impacts GitLab CE/EE"; CVSS 10.0, `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`; "under certain conditions, could have allowed an unauthenticated user" to run arbitrary code; all versions from 7.0; fixed 19.5.1, 19.4.3, 19.3.6, 19.2.9, 19.1.9, 19.0.10, 18.11.13; GitLab.com and Dedicated "remains patched"; Dedicated on 19.3.5-internal0 / 19.4.2-internal0 or later already fixed; two detections: "Onigmo native worker crash" and "Org mode render error burst"; 12 CVEs in the release; **no exploitation statement**; release date 2026-10-21 | CYB-INC-026 |
| Node.js CVE-2026-111497 | nodejs.org/en/blog/vulnerability/october-2026-security-releases (WebFetch 17:0x ET; page dated Wednesday 2026-10-21) | "Node.js Brotli decoder out-of-bounds write permits remote code execution (CVE-2026-111497) - (high)"; "An attacker who can supply Brotli data that an application decompresses with `node:zlib` can corrupt process memory, which can lead to a crash, disclosure of process memory, or remote code execution"; affects 26.x, 24.x, 22.x; reported by OpenAI Codex Security (Khai Tran, Sylvie Mayer); fixed lines v22.23.4, v24.22.1, v26.12.1 (from the Downloads section, not the entry); **no CVSS, no workaround line, no exploitation statement** | CYB-INC-027 |
| Korea FSC 2nd emergency meeting | fsc.go.kr/no010101/87927 (WebFetch 17:1x ET; release 2026-10-14) | "총 16개사로 파악되었다" (16 firms); "약 10만건(성명, 연락처, 주민등록번호, 이메일 등)" (~100,000 records: name, contact, resident registration number, email); "직접적 부정결제 우려가 있는 정보 유출(계좌 비밀번호, 카드번호 등)은 확인되지 않았다" (no leak enabling direct fraudulent payment, e.g. account passwords or card numbers, confirmed); "동일주체 여부 등은 정밀 조사중" (same actor under detailed investigation); "AI해킹 가능성 등에 대해 심도 있게 확인중에 있다" (AI-hacking possibility being examined); 16 firms by sector: banks Shinhan, KB Kookmin, Busan, Hana; savings banks Yegaram, Welcome, DB, OK; credit finance Hyundai Capital, KDB Capital; online lenders PFCT, Mouda; e-finance Brightfix; crypto Streami, Prabang; mutual Saemaul Geumgo federation | CYB-INC-022 (REPORTED/SECONDARY to CONFIRMED/PRIMARY-VERIFIED) |
| CISA KEV | cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json (curl 17:0x ET) | Catalog v2026.10.23, released 2026-10-23T19:30:18.9209Z, 1,756 entries. ABSENT: CVE-2026-110264, CVE-2026-111497, CVE-2026-109618, CVE-2026-109619, CVE-2026-115560. Latest GitLab entries in KEV: CVE-2021-39935, CVE-2023-7028, CVE-2021-22205 | Rows 026, 027 KEV keys; watch row 2 |

## 2. Reads that failed

| URL | Result | Consequence |
|---|---|---|
| openai.com/index/securing-our-frontier-model-training-environment/ | HTTP 403 (WebFetch 17:1x ET); WALTER's helper also got 403 | KB-CYP-036 carries the screenshot text and one secondary (AlphaSignal, incident 9/20); primary unread, date unread |
| about.gitlab.com/releases/2026/10/21/patch-release-gitlab-19-5-1-released/ | 301 to docs.gitlab.com/releases/ (index only) | Recorded in DATA_ROUTES; the patch post was found at the docs.gitlab.com/releases/patches/ path |

## 3. Secondary reads (search excerpts, not opened)

| Claim | Search | Found | Verdict |
|---|---|---|---|
| Capcom "11.7M records" (DailyDarkWeb 10/23) | WebSearch "Capcom 11.7 million records leak October 2026" (17:1x ET) | Only the November 2020 Ragnar Locker attack (ppe.pl, pcwelt.de, cna.com.tw, siliconera.com): ~1 TB claimed, ~$11M ransom reported, Capcom disclosed ~390,000 people possibly affected | CYB-INC-030 REPORTED / UNANCHORED; likely recirculation, not refuted; re-check 2026-11-06 (CATALYSTS) |
| Comic Cmoa "up to ~4.2M log records" (DailyDarkWeb) | WebSearch "Comic Cmoa data breach leak 2026" (17:1x ET) | NTT Solmare release relayed by 4gamers.com.tw, pasqualepillitteri.it, smartscope.blog: access judged likely 10/15, service suspended; 10/16 data exfiltration confirmed (email, hashed password, birth date, gender, nickname); no card data stored; count under investigation. Same week: ACCESS Taiwan subsidiary CROS, 155,280 IDs and 1,305 card accounts | CYB-INC-031 CONFIRMED / SECONDARY-SOURCE; the 4.2M figure is NOT in the relayed release |

## 4. Carried from WALTER without a CYPHER re-read

| Item | Source named by WALTER | Where it sits |
|---|---|---|
| Hultquist: PHP2Shell exploitation "not validated", "may have already begun in a limited fashion and the threat is viable and very serious" | The Record 10/23 (not on a Google page) | CYB-INC-007 note; watch row 1 note |
| VirusTotal 10/21: ~5.1M IPs run PHP, ~758K end-of-life, ~80% hide version | VirusTotal blog (helper read) | CYB-INC-007 note (footprint, not vulnerable hosts) |
| Node2Shell: Express 5 / body-parser 2 decompress Brotli; Imperva PoC "did not succeed on every attempt"; no exploitation as of 10/22 | THN 10/23, Imperva 10/22 | CYB-INC-027 note |
| GitLab: none confirmed in the wild, no public PoC | SecurityOnline 10/21 | CYB-INC-026 note |
| EMARKETER (FulcrumSec, 15.8 TB, 15.3M profiles); Coop Italia (Qilin listing) | DailyDarkWeb / H4ckmanac relays | CYB-INC-028, -029 (UNANCHORED) |

## 5. Inbox packets

| Packet | Disposition | Surface |
|---|---|---|
| DEWEY Korea (16:10 ET) | INTEGRATE: firm list corrected to 16; FL-CYP-14 graded (stays NOT-OBSERVED: AI tooling in an intrusion, not AI-found flaws exploited faster); IP count conflict carried (28 per FSS via inews24 vs 33 earlier, both secondary) | CYB-INC-022, FLOW FL-CYP-14 |
| DEWEY NCUA (15:33 ET) | LOG | KB-CYP-037 (MSP channel) |
| BRENT, FALCON, VULCAN boundary | INTEGRATE: 5 of 11 owners now confirmed | STATUS § Standing conditions; NEXUS_BRIEF |

## 6. Process changes

- **Intake rule** (`inbox/PROTOCOL.md` rule 0, 62c2fff5d): WALTER ROUTING_TABLE v0.48 (0adecd021, Will-approved 17:16 ET) routes every cyber claim to CYPHER. Channel-less claims arrive as one folded ROUTINE card; one board_log row per card; INCIDENTS rows only for a financial or chokepoint-supplier victim, a claim a desk has cited, or a claim CYPHER has checked. WALTER adopted the one-line-per-claim card format (9f11bc019).
- **Errata on WALTER's cards** (0adecd021, the two BOARD card files; 804de5895 is WALTER's delivery-log token fix, not the errata): 041 now says the Node.js advisory is silent on workarounds; 045 now says the Comic Cmoa 4.2M figure is not in the NTT Solmare release.
- **Chokepoint map:** neither new flaw reaches a `CHOKEPOINTS.tsv` row. The map has no developer-tooling row, and bank use of self-managed GitLab is WALTER-asserted, not measured. No Wave_Touch cell changed.
- **Convergence matrix:** no score changed (neither flaw is exploited; VX-CYP-06 bands key on the wave's root flaw). Composite stays 21/40 raw, 15/40 shared-root-adjusted.
