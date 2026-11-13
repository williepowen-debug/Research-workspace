---
signal_id: "SIG-W-20261113-004"
date: "2026-11-13"
timestamp: "2026-11-13T16:47:02Z"
dispatched: "2026-11-13T16:47:02Z"
source: "RESEARCH-INTAKE + X bookmarks (Will)"
origin: ["RESEARCH-INTAKE data/2026-11-13/news.json (collector commit e1bd850, run 43450867615)", "X bookmarks staged 2026-11-13T15:18:06Z (stage fa19db91)", "US Treasury ESF August 2026 statement notes, home.treasury.gov/system/files/206/ESF-August-2026-FS-Trunc-Notes.pdf, read by WALTER 2026-11-13T16:44Z"]
action: ["SAM"]
info: ["BRENT", "CYPHER", "LABOR", "VULCAN", "PROME"]
precedence: "PRIORITY"
signal_type: "small-items"
confidence: 0.8
confidence_language: "item 1 confirmed at the Treasury primary; item 2 unverified; others as labeled"
resources: 1
safety_net: "clear"
cluster: "MISC"
domain: "JAPAN_BOJ"
entities: ["US Treasury ESF", "yen intervention", "USDJPY", "Volgograd refinery", "Lukoil", "TruStage", "Wake County", "TrendForce", "Microsoft Exchange Online"]
word_count: 420
dispatch_note: "WQ-622 A small-items card. combo tags per item. One ask (SAM). Dups and kills listed so the batch is fully dispositioned."
event_window: "closed"
---
# Small items, Nov 13 midday: the US July 31 yen intervention was $500M per Treasury's ESF statement (SAM); Volgograd refinery fire photo, unverified; TruStage recovery into 2027; Wake County hiring freeze; 27 dups and kills

**1. combo:SAM/yen-intervention: the US leg was $500 million.** Treasury's Exchange Stabilization Fund statement for August 2026 says: "Yen FCDAs increased by $500 million, while Euro FCDAs decreased by $500 million, following operations undertaken on July 31, 2026 that settled on August 5, 2026." Bloomberg ran it Nov 13 01:12 GMT as "US Confirms $500 Million Spent on Yen Intervention, With Euros" (body not read; paywall). ECB's Lagarde had put it at €500M (Jiji, Sep 10; never carded). Press had cited a $5 to 10 billion plan. The Japanese leg was $75 to 85B (SIG-W-20260817-001). USD/JPY was 159.94 at 11:46 ET (vendor), after the 160.04 to 159.30 drop on Nov 12 (SIG-W-20261112-010, intervention unconfirmed). **Ask:** SAM: record the confirmed US leg size against your joint-intervention capacity read. Folded: Yahoo "Asia FX: yen intervention in focus" (context only).

**2. combo:BRENT/russia-refinery-strikes: Volgograd refinery fire, UNVERIFIED.** A Will-bookmarked photo (@Maks_NAFO_FELLA, Nov 12 21:45Z, "the situation at the refinery as of now") shows a night-time refinery skyline with several large fires. WALTER found no wire report of a Nov 12 strike; the indexed reports are of earlier attacks (Reuters, Nov 6, 2025). The photo carries no date and the account is partisan. INFO BRENT.

**3. combo:CYPHER/financial-cyber.** TruStage, the US credit-union insurer, says some recovery work will continue into 2027 (CU Today, Nov 12). A Wisconsin retiree is nearing a $60K payout months after the attack (Channel 3000, Nov 13). Both follow on from SIG-W-20261022-043. Separately, Microsoft 365 reported Exchange Online access problems in the Americas, Nov 12 17:54Z (EX1550543). It is a service incident with no attack claimed. INFO CYPHER.

**4. combo:LABOR/public-sector-hiring.** Wake County, NC put in a hiring freeze (ABC11, Nov 13). It is a single county. INFO LABOR.

**5. combo:VULCAN/memory-cycle.** TrendForce: TSMC pushes back on 3D DRAM rumors (Nov 13). A TrendForce piece on SpaceX, Starlink and Qualcomm Dragonwing was NO-ACTION. NOTE VULCAN.

**Duplicates and kills (no re-push):** 12 Nvidia CEO-exit headlines (DUP SIG-W-20261112-002/-003); 4 Houthi East-West pipeline/Yanbu claims, 3 intake and 1 bookmark (DUP -009; still claims, nothing new confirmed); 3 Russian diesel-exports-double (DUP -005); Mimura yen warning (DUP -005); N-able zero-days (DUP; CYPHER CYB-INC-065); Philadelphia bank failure (Aug 24 repost; DUP SIG-W-20260828-005); Western Sydney CRE ("gating" keyword false positive, KILL); TrendForce Jul 30 memory outlook (stale, KILL); FirstSquawk October core PPI 5.0% y/y as expected (bookmark; DUP, HENRY HEN-58 NONE); MTSlive DePue relay (FOLD into SIG-W-20261113-003); GPU_FINANCE_REVIEW Tech Times "Nvidia Signs $500B Wall Street GPU Bond Deal" (dated Aug 11; the $500B was a financing alliance, the June bond was about $25B; KILL).

No position action follows from this card. $0.
