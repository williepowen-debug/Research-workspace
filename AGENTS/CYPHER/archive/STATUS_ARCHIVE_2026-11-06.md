# CYPHER STATUS archive — rotated 2026-11-06 (one contiguous block from STATUS, verbatim; cksum at rotation 3866338930, 2330 B; rotated because STATUS crossed 75% of the read budget at the 11/06 close refresh)

## News sweep 10/29 (Will's ask; `research/2026-10-29_news-sweep/RECORD.md`)

- **Jack Henry (core vendor for >900 banks, >700 CUs) had a cyber incident on 8/31** (CYB-INC-048): voice phishing by ShinyHunters, corporate environment only, PII of <10 client FIs, no processing disruption, no 8-K. The 10/23 map missed it because it was press-release-only; core-vendor checks now include newsrooms and trade press (KB-CYP-074).
- **Central Bank of India** (CYB-INC-049): ~$1.7M moved via 187 unauthorized transfers through payment messaging 10/15-17. Non-US, NO OWNER, off-wave.
- **Sharetec** (CYB-INC-050, CHK-36): 9/15 cooling failure took 23 credit unions offline for days. An accident, but the multi-institution shape row 8 watches for.
- **Print/mail vendors** (CHK-37): Citizens/Frost and Citi customer data in 2026 came through them.
- **Second pass (bank software, 13:32 ET):** **the MSP route has carried traffic.** An N-able N-central flaw (MSP remote-management tool) was exploited from 7/31, NYDFS warned on 8/11 that attackers use compromised MSPs to move into their customers' networks; a NYDFS spokesperson told American Banker it was "aware of impact to a limited number of covered entities" (CYB-INC-051, CHK-38). A small NY bank closed its branches about a week citing a vendor flaw (052; the N-central link is unconfirmed). The 10/23 read "little observed traffic" (KB-CYP-020) is revised. Also: Citizens' new CA AG notice, breach 9/10 (053); Sefas named behind Frost's April data (CHK-37); SitusAMC (CHK-39). Base rate ~1 bank-supplier incident a month, 3 in August (KB-CYP-076).
- **Standing watch (Will 13:29 ET, "keep an eye out for bank issues like that"):** bank-vendor and payment-plumbing cluster watch, weekly from 11/05. Escalates on 2+ new confirmed incidents at distinct core, CU-vendor or payment-messaging suppliers within 30 days, or one multi-institution processing outage of 1 business day or more (catalyst row; WALTER asked to route matching stories).
- Nothing new on PHP2Shell victims, file-transfer products, Fiserv/FIS/Broadridge, insurers or election-week warnings. Packets: WALTER, REGINALD, LIQUID, GIBBS, PROME.

**Banking sub-folder (Will 13:49 ET):** `banking/`: the bank cyber / software / vendor-risk thread. README indexes the rows; `THREAD_2026-10-29.md` is the current reading.

