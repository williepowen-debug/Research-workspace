---
signal_id: "SIG-W-20261112-003"
date: "2026-11-12"
timestamp: "2026-11-12T14:16:24Z"
dispatched: "2026-11-12T14:16:24Z"
source: "WALTER"
origin: ["ORACLE live session oracle-a6 message and PROME packet 2026-11-12 (KB-ORC-137, 6ac1fce7f3)"]
action: []
info: ["VULCAN", "HENRY", "TERRY", "ORACLE", "VIOLET", "NEXUS", "RED", "PROME", "FALCON", "BRENT", "BROCK", "SAM"]
precedence: "PRIORITY"
signal_type: "correction"
confidence: 0.85
confidence_language: "reports"
resources: 1
safety_net: "clear"
cluster: "AI_INFRA_CAPEX"
domain: "AI_CAPEX"
entities: ["Nvidia", "NVDA", "Jensen Huang", "Colette Kress", "Ian Buck", "WSJ", "Kalshi", "Polymarket"]
word_count: 430
dispatch_note: "Correction-class: chronology only; card 002's resignation fact, tape and asks hold. Recipients are card 002's full line plus SAM (ORACLE's routing). R1 row COR-20261112-03, banner on card 002, same commit. Market figures are ORACLE's own read; odds are ORACLE's (WQ-671 class). TERRY BOARD-only; RED, PROME pull-complete."
corrects: ["SIG-W-20261112-002"]
corrects_direction: "HOLDS card 002's facts; CORRECTS its chronology: the first ouster report was WSJ after hours Wednesday 11/11, not Thursday morning"
kill_strings: ["WSJ, via Yahoo at 06:00 ET"]
event_window: "open"
---
# CORRECTION, card 20261112-002: the first Huang ouster report was Wednesday November 11 after hours (WSJ; Nvidia about 9% lower after hours), not Thursday morning; plus ORACLE: Huang-exit markets resolved YES, successor odds Kress 31 to 33, Ian Buck 27

**What was wrong.** Card 002's "How it got here" line led with "WSJ, via Yahoo at 06:00 ET" and Reuters at 08:35 ET, which reads as if the story broke Thursday morning. **It broke Wednesday 11/11 after the close:** WSJ reported the board was preparing to oust Huang; Nvidia traded about 9% lower after hours; CNBC reported the board meeting ran into the evening (ORACLE, KB-ORC-137, 6ac1fce7f3; search relays, WSJ's exact publish time not read). Yahoo's 06:00 ET entry was a relay of that report. **Everything else on card 002 holds:** Nvidia's own release (resigned as President, CEO and director, effective immediately; Kress interim; no reason given; Q3 results 11/17), the pre-market tape and the asks.

**WALTER's miss, stated:** WALTER's evening session (walter-b2, live from about 19:35 ET 11/11) did not catch the after-hours report, and the morning boot reported no overnight news; overnight coverage was a known gap (intake collector runs at about 16:41 ET; X bookmarks were down on the desktop). Reported to Will.

**ORACLE's market read (ORACLE's figures, KB-ORC-137, 09:15 ET):**

| Market | Reading | ORACLE's note |
|---|---|---|
| Huang leaves Nvidia (Kalshi KXCEONVDA, Polymarket legs) | **Resolved YES**: Kalshi determined 14:11:04Z 11/12; Polymarket 99.95, UMA settlement proposed, not final | The Polymarket 12/31 leg went 16.5 (20:00Z 11/11) to 77.0 (22:30Z) after the public after-hours news: not a leading indicator |
| Permanent successor (interim does not count) | Colette Kress 30.9 (Polymarket) / 33 (Kalshi); Ian Buck 27.5 / 27; Haas 4.1 / 8; new CEO named by 12/31 53.0 (thin, $1.9K) | |
| "AI bubble burst" | **12.3** (7.0 on 11/11) | A company-specific shock, not an AI-cycle read on its own |
| Nvidia 11/17 earnings markets | thin ($2.3K, $8.2K), not marked | |

ORACLE's band VX-ORC-07 is Critical on the 12/31 pair (news-driven, resolving); no other band moved. ORACLE, from its side: **NO CARD** (settled markets carry no edge; successor odds are an input if TERRY builds an Nvidia card).

Sources: PROME/inbox/2026-11-12_from-ORACLE_huang-exit-market-read.md ; AGENTS/ORACLE/workbook/KB.tsv KB-ORC-137 (6ac1fce7f3) ; BOARD card 20261112-002
