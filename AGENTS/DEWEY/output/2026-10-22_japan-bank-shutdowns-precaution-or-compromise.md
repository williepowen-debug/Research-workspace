# Japan's financial-firm service suspensions after PHP2Shell (21–22 Oct 2026): precaution or hidden compromise?
**Date:** 2026-10-22 (research 21:35–21:40 ET; evidence as of ~10:00 JST 23 Oct) | **Mode:** Thesis | **Confidence:** Medium that these were precautions; Low that nothing happened (no firm's own notice read)
**Commission:** Will-directed in the DEWEY session, 21:33 ET (Will's pick #4; WALTER candidate thread 2). No REQ.

## Key Finding
**Every reading so far points to precaution, and no compromise has been reported. But the evidence is news-relayed, so "not reported" is not "ruled out".** MUFG Bank called its suspensions "臨時メンテナンス" (emergency maintenance), and named no PHP or intrusion. Mizuho reopened branch-visit booking on 22 Oct. Shizuoka Bank restored its app by the evening of the 22nd. Jiji reports that the regional and shinkin banks checking their sites have "いずれも現時点で不正アクセスなどの被害は確認されていない" (none has so far confirmed damage such as unauthorized access). The Japanese Bankers Association said the interbank settlement network had "no impact at this time". **Nomura's involvement is UNVERIFIED:** its own news page (read ~10:00 JST 23 Oct) shows no notice, and only English search summaries name it. JPCERT/CC itself warns that finding no traces does not prove a system wasn't attacked.

## Evidence

| Firm | When (JST) | What stopped | Stated reason | Compromise mentioned? | Restored | Source | Basis (Class 12) |
|---|---|---|---|---|---|---|---|
| MUFG Bank | 22 Oct, as of 08:00 | Parts of MUFG Direct (fund account opening, NISA, address change, iDeCo), mortgage pre-screening and "My Page", account-opening and My Number apps, Net-de-Loan e-contract | 「臨時メンテナンス」 (emergency maintenance). The link to PHP is the newspaper's own view ("PHPの問題を受けた対応とみられる", "appears to be a response to the PHP problem") | No | Not found | [NEWS: Fukui Shimbun](https://www.fukuishimbun.co.jp/articles/-/2728327); [NEWS: Jiji](https://www.jiji.com/jc/article?k=2026102200263) | SECONDARY-SOURCE (bk.mufg.jp loaded, but no notice was visible) |
| Mizuho Bank | 22 Oct | Branch-visit booking (来店予約); securities arm "some online services" | "emergency maintenance" (Jiji English) | No | Booking reopened 22 Oct (「一時停止していた来店予約サービスを２２日、再開」, "resumed on the 22nd the visit-booking service it had paused") | [NEWS: Jiji](https://www.jiji.com/jc/article?k=2026102200263); [nippon.com](https://www.nippon.com/en/news/yjj2026102200263/) | SECONDARY-SOURCE (mizuhobank.co.jp returns 403) |
| Shizuoka Bank | 21 Oct | Online banking app, site and app | "will resume the service once its safety has been confirmed" | No | Restored by evening 22 Oct (「ネットバンクアプリなどを復旧させた」, "restored its net-banking app and other services"; Jiji 19:00, updated 20:02) | [NEWS: Jiji](https://www.jiji.com/jc/article?k=2026102200263) | SECONDARY-SOURCE (the bank's notice list loads by JavaScript) |
| Nomura | ~22 Oct | "some internet services" | "emergency measure" (search summary) | No | Not found | Search summaries only. Jiji, Fukui and The Next Web don't name Nomura; [Nomura news page](https://www.nomura.co.jp/introduc/news/) shows no notice | **UNVERIFIED** |
| 77 Bank | 21–22 Oct | Web services | 「予防的な措置として」 (as a precautionary measure) | No | — | [NEWS: Jiji](https://www.jiji.com/jc/article?k=2026102200263) | SECONDARY-SOURCE |
| Others named (Daiwa Securities, Hokuyo, Hokkaido, Daishi Hokuetsu, au Jibun, Hachijuni, Fukuoka, Aomori Michinoku, Yamanashi Chuo, San-in Godo, Nishi-Nippon City) | 21–22 Oct | Various web services | piyolog: the notices it saw do not mention PHP | No | — | [piyolog, 21 Oct](https://piyolog.hatenadiary.jp/entry/2026/10/21/174516) | SECONDARY-SOURCE |

**Government and regulators**
- **JPCERT/CC, JPCERT-AT-2026-0033 (22 Oct, revised the same day):** confirms the product is "widely used in Japan". It reports **no domestic exploitation** and does not mention financial institutions. It lists compromise indicators (abnormal PHPSESSID cookies, multipart requests with memory-limit or HTTP 500 errors, crashing PHP workers) and warns that finding no trace is not proof. PRIMARY-VERIFIED (read by the helper; [JPCERT](https://www.jpcert.or.jp/at/2026/at260033.html)).
- **Chief Cabinet Secretary Kihara:** "no attacks exploiting the flaws had been confirmed". This is The Next Web's paraphrase of Bloomberg, with no transcript found. A separate, unopened summary (attributed to the Japan Times / Kathmandu Post) has him describing ministry website suspensions, with no "no attacks" line. **Both versions are carried.** SECONDARY-SOURCE / UNVERIFIED.
- **Japanese Bankers Association (全銀協), 22 Oct:** interbank settlement network 「現時点で影響がないことを確認している」 ("we have confirmed there is no impact at this time"). SECONDARY-SOURCE (Jiji).
- **Prime Minister Takaichi** (X, 21 Oct): an "urgent request" to act that night. IPA and the National Cybersecurity Office issued patch alerts. SECONDARY-SOURCE (piyolog).
- **FSA (金融庁):** no statement found by these searches.
- **Personal Information Protection Commission notification / TDnet timely disclosure:** none found (TDnet was not searched directly).

## Counter-Evidence
- **For "hidden compromise":** "emergency maintenance" is the standard Japanese corporate phrasing whether or not there was an intrusion, and Japanese firms often publish investigation results days later. PHP2Shell compromises are low-footprint (JPCERT's own caveat; CrowdStrike's lab finding in REQ-008). In 2024, a different PHP flaw (CVE-2024-4577) led IPA to confirm web shells planted at multiple Japanese organizations (UNVERIFIED, search summary). The breadth of the response (a PM request, a dozen-plus banks) shows how seriously it was taken, though that is not evidence of harm.
- **For "precaution":** the services pulled were peripheral web front-ends (booking, account opening, mortgage portals), not core banking or settlement. Several firms restored within 1–2 days, and a 1–2-day restore is a patch-and-recheck shape, not incident response. The bankers' association confirmed no settlement-network impact. No firm, regulator or newspaper has reported unauthorized access.

## Source Quality Assessment
Weak at the firm level: none of the four named firms' own notices was read (403s, JavaScript-loaded lists, no visible notice). The JPCERT advisory is the only primary read. Jiji is the backbone and consistent. Nomura is unconfirmed. Kihara's line has no transcript.

## References
(accessed 2026-10-22 ~21:35–21:40 ET by a DEWEY helper; the JPCERT and Jiji pages were opened)
- Jiji: https://www.jiji.com/jc/article?k=2026102200263
- nippon.com: https://www.nippon.com/en/news/yjj2026102200263/
- Fukui Shimbun: https://www.fukuishimbun.co.jp/articles/-/2728327
- JPCERT/CC: https://www.jpcert.or.jp/at/2026/at260033.html
- piyolog: https://piyolog.hatenadiary.jp/entry/2026/10/21/174516
- The Next Web: https://thenextweb.com/news/php2shell-millions-exploit-attempts-no-confirmed-breaches
- Nomura news: https://www.nomura.co.jp/introduc/news/

## Process Report
**Searches run:** one DATA-RETURN helper made 26 tool calls (English and Japanese queries). The helper wrote nothing to the repo.
**Data gaps:** the firms' own notices, Nomura confirmation, the Kihara transcript, the FSA site, TDnet, and restoration times for MUFG and Mizuho Securities.
**Source frustrations:** Mizuho (403), Bloomberg JP (403), Japan Times (402), and JavaScript-only notice lists.
**Confidence in findings:** Medium on precaution, Low on "nothing happened".
**If I had more time/tools:** a re-check of TDnet and each firm's investigation notices around 29 Oct, which aligns with the 008R rerun.
**Suggestions:** fold the "Japan precautionary suspensions → later disclosure?" check into the 10/29 008R rerun rather than running a separate pass.
