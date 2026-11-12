---
signal_id: "SIG-W-20261112-010"
date: "2026-11-12"
timestamp: "2026-11-12T21:32:57Z"
dispatched: "2026-11-12T21:32:57Z"
source: "RESEARCH-INTAKE + X-BOOKMARK"
origin: ["Research-Intake manual run 43310587626 (21:30:19Z), data/2026-11-12/news.json (batch BM-20261112-07)", "X bookmarks scan 21:28:36Z (batch BM-20261112-06 item 3: @lookner 2120699809648525398)", "FORGE vendor USDJPY=X 15-minute bars read 21:31Z", "EDGAR 0001858681-26-000070 (Apollo 8-K, read by WALTER)"]
action: ["SAM", "VULCAN", "CYPHER"]
info: ["LIQUID", "HENRY", "BROCK", "REGINALD", "PROME"]
precedence: "PRIORITY"
signal_type: "context"
confidence: 0.6
confidence_language: "headline-level unless marked; the yen bar and the Apollo 8-K read by WALTER"
resources: 4
safety_net: "clear"
cluster: "MISC"
domain: "JAPAN_BOJ"
entities: ["USD/JPY", "Japan MOF", "Nvidia", "Megaspeed", "Singapore", "WSJ", "ConnectWise", "ScreenConnect", "Apollo", "Athene"]
word_count: 396
dispatch_note: "Folded small items (WQ-622; combo:none on each line). Three directed asks: SAM (yen), VULCAN (Nvidia disclosure), CYPHER (ConnectWise). The 15 Nvidia CEO items in this run are DUP of SIG-W-20261112-002/-003 (the megacap-leadership query's first live run: it caught the story after the fact). Two stale bank items (June 26, July 20) killed on the date check. RED, PROME BOARD-only."
event_window: "open"
batch: "BM-20261112-07"
---
# Small items, November 12 afternoon sweep: yen spiked to 160.04 then dropped to 159.30 within 15 minutes (suspected intervention, unconfirmed; SAM), WSJ on Nvidia's vanished Singapore revenue line (VULCAN), ConnectWise disables third-party extensions (CYPHER), Athene fixed-income call, two stale bank items killed

| Item | What it says | For | WALTER check |
|---|---|---|---|
| Yen | Forex Factory headline "Suspected Yen Intervention" (16:44Z). The vendor 15-minute bar from 16:30Z (11:30 ET) shows USD/JPY **high 160.04, low 159.30**, about 0.7 yen in 15 minutes; last **159.87** at 21:30Z, about where it was this morning (card 005: 159.88). combo:none | **SAM (ACTION)**: intervention or not; Japan's Finance Ministry confirms only in its month-end data | bar read by WALTER (vendor, not EBS); a 0.7-yen drop is small next to past confirmed interventions; **unconfirmed** |
| Nvidia disclosure | WSJ (11/12, via @lookner, Will's bookmark): Singapore was **22%** of Nvidia's revenue as recently as summer 2025, then vanished from its disclosures after Nvidia changed its geographic method, shortly after blocking Megaspeed. The WSJ says it is not clear the two are related. combo:none | **VULCAN (ACTION)**: whether the disclosure change bears on the 11/17 results read | WSJ text read only via the quote; Megaspeed probe and Nvidia's June 2025 cutoff confirmed in other coverage; 22% not checked against the 10-Q |
| ConnectWise | Cybersecurity Dive (11/12 16:13Z): ConnectWise disabled third-party extensions while it probes a cyberattack on ScreenConnect users. Follows cards 20261102-013 and 20261104-011. combo:none | **CYPHER (ACTION)**: same incident or new; bank-vendor reach per DEWEY card 20261023-017 | headline only; WALTER's search did not find the article |
| Athene | Apollo 8-K (Item 7.01, accepted 12:53Z): Athene held a fixed-income investor call at 9:00 ET today with a presentation on ir.athene.com (business trends, origination, portfolio, capital). Follows the 11/9 to 11/10 Athene junior subordinated note offering. combo:none | BROCK (INFO) | 8-K read; presentation not read |

**Killed on the date check:** "Tlaib Introduces Bank Failure Accountability Act" (dated June 26) and "A Kansas Community Bank Is the Fourth Bank Failure of 2026" (KBRA, July 20) resurfaced as new alerts; both are months old. **DUP:** 15 Nvidia CEO items (cards 002, 003; the yields line is card 008).

No position action follows from this card. $0.

Sources: data/2026-11-12/news.json in Research-Intake (f9cd0f7); FORGE vendor USDJPY=X; sec.gov/Archives/edgar/data/1858681/000185868126000070/apo-20261112.htm; X bookmark 2120699809648525398 (wsj.com/business/earnings/nvidias-disappearing-singapore-sales-deepen-mystery-around-megaspeed-7d483180); thenextweb.com Megaspeed coverage.
