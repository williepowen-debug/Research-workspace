# CYPHER — WAVE-2026-10 seven-day re-check (DOCKET L812) — 2026-10-29

**Session:** started 11:34 ET 2026-10-29 (boot.py wall clock). Runtime Claude Code, Opus 5.5. Will's word: "go" (11:59 ET) on the suggested L812 session.
**Method:** two read-only checkers (Opus) read the primaries for watch rows 1, 3, 5, 6, 7 and 8 and for the overdue follow-ups. Their ledgers are kept verbatim beside this file (`checker_wave_rows.md`, `checker_followups.md`). CYPHER read these itself: the CISA KEV JSON (curl), the Hanmi 8-K, the Palo Alto advisory, Dream's blog post and the American Banker article. Everything else carries the checkers' read, labelled as such.

## Verdicts

| Row | State | Basis of the call |
|---|---|---|
| 1 | NOT-FIRED | See § row-1 |
| 2 | FIRED (terminal) | KEV v2026.10.28 still lists both CVEs; federal due date 10/29 |
| 3 | NOT-FIRED | § row-3 |
| 4 | NOT-FIRED | boot.py leg 8: only AASP since 10/22 (rejected 10/26); leg 9 Hanmi = dividend boilerplate |
| 5 | NOT-FIRED | § row-5 |
| 6 | NOT-FIRED | § row-6 |
| 7 | NOT-FIRED | § row-7 |
| 8 | NOT-FIRED (candidate adjudicated) | § row-8 |
| 9 | NOT-FIRED | 20-trading-day rule until 11/18 |

## row-1

Rule: R1 requires "a **named** organisation's successful PHP2Shell compromise". **Dream** (an Israeli security firm), in its own blog post of 10/26, reports that a PHP2Shell + Fragnesia (CVE-2026-46300) chain rooted 24-25 firewalls of an undisclosed "large vendor", with post-exploitation against three servers in a "US government-affiliated environment" ("artifacts confirm credential extraction"). It found this through "proactive threat hunting" with its own product, and the post markets that product (VENDOR CLAIM). The victim is unnamed and nobody is attributed. **Palo Alto's** own advisory (updated 10/29, read by CYPHER) says: "Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet"; Exploit Maturity ATTACKED; severity Critical since 10/27. CISA added Fragnesia to KEV on 10/27.

**Call:** NOT-FIRED under the registered letter, because no organisation is named. The evidence has nevertheless moved: the wave is no longer "attempts only", since one research firm reports an unnamed production compromise. Both earlier firm claims in this wave were withdrawn or corrected (Unit 42 on 10/25, Sophos on 10/22). That base rate is why a single firm's post is held to the letter, and why a correction re-check is set for 11/04. ⚠️ If a named victim surfaces later, this is the MOVEit shape, and this row is the one that catches it.

## row-3

No named US bank, credit union or core/digital-banking vendor victim is tied to a wave vector. MSUFCU is a precautionary pause, not a compromise (row 8). Finzly remains a claim; per American Banker 10/20 the company says it is investigating and "fully operational".

## row-5

The latest NYDFS letter is still the 10/22 PHP alert. Nothing from the Fed, OCC, FDIC, FFIEC, NCUA, FS-ISAC or ECB meets the supervisory-concern test.

## row-6

No PCS designation can be seen (behind its subscription wall) and there is no loss estimate from any modeller. CyberCube's 10/23 piece is headed "Why PHP2Shell isn't a large-loss event today" (search title only).

## row-7

No US, UK or EU government has made an attribution. The attributions so far are private: Dream, CYFIRMA and Microsoft/ConnectWise.

## row-8

**MSUFCU** ($8.9B, East Lansing) took its website and digital banking offline on Wednesday 10/21 after the federal PHP warnings and restored them about 24 hours later, after patching. Branches, ATMs and cards stayed up. The credit union said "no impact to member information at this time". Source: American Banker 10/23, quoting the operator, read by CYPHER; no notice of its own was found. **Call:** NOT-FIRED, decided by the VX-CYP-02 bands registered on 10/22 before the event: "Precautionary pauses only, or an outage under one business day at a single institution" = YELLOW. FIRE (ORANGE) needs an operator-confirmed outage of one business day or more. The call applies the band as written; the band was not re-cut after the event. The 10/23 re-check missed this item.

## Follow-ups

| Item | Result | Basis |
|---|---|---|
| ConnectWise | Phased restoration began 10/28 16:00 UTC, Microsoft 365 first; **not restored**; no financial institution named | PRIMARY (checker) |
| Chrome G3 removal | G3 is absent from Chromium root store v43 source; release to devices unconfirmed by Google; no breakage reports found | ARTIFACT (checker) |
| Tailscale | v1.104.4 released 10/28; no exploitation claimed — **closed** | PRIMARY (checker) |
| 036-040 claims | None confirmed or denied by a victim or regulator | mixed |
| Park24 (043) | About 1.46M accounts eligible for JPY 3,000, about JPY 4.4B in total; JPY 5.5B extraordinary loss; net profit forecast cut from 44.0B to 38.5B | SECONDARY |
| FEC | The status page says "outage", now restored; the hack framing is Reuters' alone | PRIMARY / SECONDARY |
| Node2Shell CVE-2026-111497 | CISA KEV 10/27 (listed under Google Brotli) → CYB-INC-027 CONFIRMED at the flaw level; outside the wave root | PRIMARY (CYPHER) |
| BOND amendment | CHK-34 TAAPS, CHK-35 interdealer venues | packet |
| DEWEY 008R | Not in DEWEY output at ~12:08 ET (ls); re-dated to 10/30 | repo |
