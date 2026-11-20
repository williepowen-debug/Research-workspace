# Fetch log 2026-11-20 (YURI, PROME prome-77 C8 letter; cards SIG-W-20261120-005 and -011)

Raw HTML kept off-repo in the session scratchpad; text extracts here. Times UTC.

| Time | Request | Result |
|---|---|---|
| 16:48:06Z | kremlin.ru events/president/news, page 2, acts/news (http, browser UA) | 200 ×3; listings `kremlin.ru_*_listing.txt` |
| 16:48:25Z | kremlin.ru 81305, 81308, 81313, 81316, acts 81312 | 200 ×5; `kremlin-*.txt` |
| 16:48:48Z | mid.ru (http) /press_service/spokesman/briefings/, /foreign_policy/news/ | "Request Rejected" (WAF refusal, 301 B). Not retried |
| 16:48:48Z | mid.ru / www.mid.ru (https) same paths | 200 but JavaScript bot challenge page (bobcmn), no content. Unusable; not retried |
| 16:48:48Z | netherlands.mid.ru, poland.mid.ru (http) | "Request Rejected" (WAF refusal). Not retried |
| 16:48:48Z | mil.ru http and https | timeout (curl exit 28), this box's request, not a host fact |
| 16:50:04Z–16:51:05Z | t.me/s/ public web previews: mod_russia, MID_Russia, MariaVladimirovnaZakharova (+ earlier pages) | 200; coverage MoD 19.11 16:18Z→20.11 16:22Z, MFA 19.11 14:32Z→20.11 16:44Z, Zakharova 19.11 03:50Z→20.11 16:17Z. `tg-*.txt` |
| 16:50:04Z | t.me/s/ambrus_nl, rusembpoland (guessed channel names) | 302 (no such public channel); not pursued |
| 16:51:35Z | tass.ru/politika | captcha/challenge page. Unusable; not retried |
| 16:51:35Z | tass.com/politics, ria.ru/politics | 200 pages with captcha markup; not parsed. Agencies read via Telegram instead |
| 16:51:35Z–16:52Z | t.me/s/tass_agency, rian_ru (+ back pages) | 200; TASS 19.11 20:19Z→20.11 16:50Z, RIA 19.11 15:52Z→20.11 16:44Z; 215 distinct posts. `tg-tass_agency*.txt`, `tg-rian_ru*.txt` |
| 16:53:57Z | kremlin.ru/supplement/6618 and 81303 (YUR-007 re-read) | 200; title "Декларация глав государств России, Китая и США о мире", dated 19 ноября 2026 года |
