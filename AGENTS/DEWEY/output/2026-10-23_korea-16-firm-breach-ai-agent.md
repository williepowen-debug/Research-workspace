# South Korea's 16-firm financial breach: what the regulator says, and is it an AI-agent attack?
**Date:** 2026-10-23 (research 15:55–16:10 ET) | **Mode:** Thesis | **Request:** Will-approved follow-on (slate #3, "approved go ahead" 15:54 ET); CYPHER row CYB-INC-022; no WALTER REQ | **Confidence:** High on the regulator's facts (FSC primaries read in Korean). Medium on the AI-tool use (one vendor, moderate confidence). Low on any AI *speed* effect (none measured).

## Key Finding
**AI involvement is vendor-attributed, not regulator-confirmed, and no speed effect is measured.**
- **Regulator.** Korea's Financial Services Commission confirmed **16 firms breached and ~100,000 records** taken: names, contacts, resident registration numbers and emails. It confirmed **no** passwords or card numbers. Its own written release says AI involvement is only **"under examination"**.
- **Vendor.** CrowdStrike assesses with **moderate confidence** that a Chinese-speaking, financially motivated actor used **ARTEX**, an LLM-driven automated penetration-testing tool. Its evidence covers at least two of the bank breaches.
- **How they got in.** The regulator names the entry points as **missing or bypassable authentication** on loan-broker and employee web systems: basic failures, not new exploits.

**For the fleet's AI-exploitation thesis:** the leg moves from NOT-OBSERVED to **"AI tooling in use (vendor, moderate confidence); speed effect asserted generically, not measured."**

## Evidence

### (1) Regulator primaries (FSC press PDFs, read in Korean; text-checked by DEWEY)
| Date | Release | Load-bearing content |
|---|---|---|
| 10/2 | FSC 1st emergency meeting (fsc.go.kr no010101/87869) | Shinhan leak (reported to FSC 9/30) and the KB attacks; orders checks for "인증 없이 내부정보에 접근할 수 있는 경로" (paths into internal data without authentication). **No AI mention.** |
| 10/4 | FSC chairman's all-sector meeting (no010101/87876) | Named cause: systems used by "대출모집인·위탁업체 등 외부인력과 임직원" (loan brokers, contractors and staff) where "인증 절차가 누락되거나 우회될 수 있는" (authentication is missing or bypassable). AI appears only as future policy ("AI공격은 AI로 방어"). |
| **10/14** | FSC 2nd emergency meeting (no010101/87927) | "총 16개사 침해사고 확인, 동일주체 여부 등은 정밀 조사중" (16 firms confirmed breached; whether it is one actor is under detailed investigation). Data: "약 10만건(성명, 연락처, 주민등록번호, 이메일 등)"; "계좌 비밀번호, 카드번호 등" (account passwords and card numbers) **not** confirmed leaked. The count "더 확대될 수 있다" (may grow). **AI:** "AI해킹 가능성 등에 대해 심도 있게 확인중" (AI-hacking possibility being examined in depth). |

[PRIMARY: FSC press releases, fsc.go.kr; Korean quotes verified in the extracted PDF text.]

**The 16 firms (FSC 10/14):**
- Banks: Shinhan, KB Kookmin, Busan, Hana
- Savings banks: Yegaram, Welcome, DB, OK
- Specialised credit: Hyundai Capital, KDB Capital
- P2P lenders: PFCT, Mouda
- E-payment: Brightfix
- Crypto: Streami, Prabang
- Mutual: Saemaul Geumgo central federation

**CYPHER's row omits Hyundai Capital, PFCT, Mouda, Brightfix and the Saemaul federation.**

**Checklist (FSC 10/14).** Of 555 firms checked, 130 reported shortfalls. The shortfalls cited are unpatched systems, end-of-support systems, no 24-hour monitoring, and missing authentication or no MFA on external systems.

**Other official sources:**
- **Police:** a case opened under the Information and Communications Network Act, with 28 investigators. They are keeping "중국발 AI를 활용한 동시다발 해킹 가능성" (possible simultaneous hacking using China-origin AI) in mind [NEWS: YTN 10/6].
- **FSS:** 28 unique attack IPs across about 12 countries. The FSS cautions that IP location cannot be taken as the attacker's location [NEWS: inews24 10/6].

### (2) Where the AI-agent claim came from
| Date | Source | Words | Weight |
|---|---|---|---|
| 10/2 | Korea Herald, relaying local reports | "traces of an AI penetration-testing tool called ARTEX AI … Neither the bank nor the financial authorities have officially confirmed" | [NEWS] |
| 10/4 | FSC Chairman (spoken) | "인공지능(AI)를 활용한 공격 가능성도 배제할 수 없다" (an AI-assisted attack cannot be ruled out) | [NEWS: SBS Biz 10/4] possibility only |
| **10/7** | **CrowdStrike Counter Adversary Operations** | "moderate confidence based on the use of the Chinese-developed tool ARTEX and observed Chinese-language prompts". LLM back-ends: DeepSeek, GLM and Grok. Exposed directories showed Claude Code session histories. AI tooling "can enable a financially motivated threat actor to conduct multiple intrusions within a short time span". | [INSTITUTIONAL: https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/; quote DEWEY-verified] |
| 10/14 | FSC written release | AI possibility "확인중" (being examined) | [PRIMARY] |

**What CrowdStrike does *not* establish:**
- It describes 2 breaches (consistent with Shinhan and KB), not all 16.
- It names no CVE.
- It does not split the work between AI and humans.
- It makes no timing measurement. "Multiple intrusions within a short time span" describes many targets hit quickly, not a vulnerability exploited faster.

**Attribution.** A possible individual in Guangdong, which CrowdStrike calls "not reliable enough to confirm". **No state actor and no North Korea link** appears in any source.

### (3) The firms' own disclosures
- **Shinhan Financial Group** 6-K (10/1): "an external party had accessed certain services and had obtained customer information … not in a position to reasonably quantify the specific impact" [PRIMARY: SEC 0001193125-26-409712]. No AI mention.
- **KB Financial Group:** no cyber 6-K filed 10/2–10/21 [PRIMARY: EDGAR].
- **Per-firm counts from press:**
  - Shinhan ~25,700 (66 resident registration numbers)
  - KB 119
  - Hana 89
  - PFCT 302 (link not confirmed)
  - Prabang 20
  - BNK 11

  [NEWS: Korea Herald 10/2; JoongAng 10/4]
- **No firm has stated a financial cost.**

### (4) Status as of 10/23
- **No arrests.** The firm count is still 16.
- National Assembly audits on 10/8 and 10/19: the FSS governor says CEO responsibility will be taken up "for the first time" in a hacking case [NEWS: News1 10/22]. **No sanctions yet.**
- **Policy:** vulnerability assessments rise to at least twice a year for large firms [PRIMARY 10/14].

## Counter-Evidence
- **The regulator frames basic-control failures**, not AI capability: missing authentication, unpatched systems, no MFA. Korean experts: AI did not create "완전히 새로운 공격 기법" (an entirely new attack technique) (SK Shields); the same weaknesses "AI가 없었던 과거에도 계속 뚫렸던" (were breached before AI existed) (Prof. Kim Myung-joo) [NEWS: Weekly Khan 10/12]. Banks with MFA reportedly blocked the same attack.
- **The 16 may not be one campaign.** Same-actor IPs were reported at only 7 firms [NEWS: eToday 10/4]. The FSC has not ruled on "동일 주체" (same actor), and PFCT's 9/27 breach is not confirmed as linked.
- **The attack vector is unresolved.** Press reports low-volume AI-paced credential stuffing (Hankyung); the FSC describes bypassed or missing authentication.

## Source Quality Assessment
- The FSC primaries are strong and were read in the original.
- CrowdStrike is one institutional vendor at moderate confidence.
- The AI claims are otherwise from unnamed officials or reporters.
- Per-firm counts rest on press relays of bank statements.

## References
(accessed 2026-10-23)
- FSC: https://www.fsc.go.kr/no010101/87869 (10/2), /87876 (10/4), /87927 (10/14), with PDF attachments.
- CrowdStrike blog (10/7): URL above.
- SEC Shinhan 6-K: 0001193125-26-409712.
- News URLs per the sub-agent's notes: Korea Herald 10/2; SBS Biz 10/4; eToday 10/4; JoongAng 10/4; YTN 10/6; inews24 10/6; BleepingComputer 10/5; Weekly Khan 10/12; Hankyung; News1/fnnews 10/22.

## Process Report
**Searches run:**
- One Opus leg: 49 tool calls, Korean and English.
- DEWEY verified the FSC 10/14 Korean text (firm list, record count, AI sentence) and the CrowdStrike "moderate confidence" sentence on the fetched page.

**Data gaps:**
- DART filings for Hana, BNK and the others.
- PIPC, KISA and police primaries.
- The police "hard to confirm AI" sentence (search summary only).
- The Yonhap original of the ARTEX finding.

**Source frustrations:** WebFetch would not reproduce the FSC releases verbatim; downloading the PDFs and extracting text worked. SEC rejects generic user-agents.

**Confidence:** High on facts; Medium on AI use; Low on AI speed.

**If I had more time/tools:** read the DART filings; follow the FSC's next release for the same-actor ruling and any count change.

**Suggestions:**
- CYPHER: correct the firm list in CYB-INC-022.
- FL-CYP-14: re-grade the AI-use leg to OBSERVED (vendor, moderate confidence). The speed leg stays NOT-OBSERVED.
