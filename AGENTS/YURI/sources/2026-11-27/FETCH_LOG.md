# Fetch log 2026-11-27 (YURI catch-up, PROME prome-80 letter)

Raw HTML and PDFs kept off-repo in the session scratchpad; text extracts here. Times UTC. All requests plain HTTP with User-Agent Mozilla/5.0 unless stated; t.me previews over HTTPS.

| Time | Request | Result |
|---|---|---|
| 23:02:20Z | kremlin.ru events/president/news, pages 2 and 3; acts/news pages 1 and 2 | 200 x5; `kremlin_listings.txt`. Coverage events/president/news 81372 (27.11 23:40 Moscow) back to 81167 (03.11); acts 81365 (26.11) back to 81121 (30.10) |
| 23:03:06Z | kremlin.ru events/president/news items dated 19.11 to 27.11: 81302 81303 81305 81308 81313 81316 81318 81323 81329 81337 81341 81342 81347 81350 81358 81359 81369 81370 81371 81372 | 200 x20. Full-text keyword scan (НАТО, нерасшир, вступлени Украин, Основополагающ, 1997, конфигурац, 2021, гарантии безопасности, Крымск, ответ). Extracts kept here for 81337 and 81369 only; the others are scan-only |
| 23:03Z to 23:05:41Z | kremlin.ru acts 81360 81348 81333 81332 81335 81363 | 200 x6 (slow, about 2.5 min) |
| 23:06:07Z | publication.pravo.gov.ru documents/block/government; government.ru /docs/ and /news/ | 200 x3; `pravo_listings.txt` |
| 23:06:39Z | pravo document 0001202611270001 (Постановление №1586) and 0001202611270041 (№1584): page and PDF | 200 x4; PDFs scanned (no text layer), rendered with .venv pypdfium2 and read visually: №1586 3/3 pages, №1584 2/2 pages |
| 23:07:33Z | pravo documents/block/president, index 1 and 2 | 200 x2; titles to Указ №883 (26.11) and 444-рп; `pravo_listings.txt` |
| 23:08:03Z | t.me/s/MID_Russia and t.me/s/MariaVladimirovnaZakharova, search q= Эстон, Меркурий, Ливи, Лукойл, Нидерланд, Спарта | 200 x12 |
| 23:10:06Z | same two channels, q= Польш, Destinus, Мост, ответ | 200 x8; selected posts in `tg-MFA-Zakharova-selected-posts.txt` |
| 23:11:33Z | government.ru/docs/60567/ (notice for №1586) | 200; text quoted in the session record §3 |

**Not requested (known blocks from 11/20, not retried):** mid.ru, tass.ru, poland.mid.ru, netherlands.mid.ru, mil.ru. **Not read:** Peskov's daily briefing transcripts; MoD Telegram this session; regulation.gov.ru (the MoD pay-delay draft).
