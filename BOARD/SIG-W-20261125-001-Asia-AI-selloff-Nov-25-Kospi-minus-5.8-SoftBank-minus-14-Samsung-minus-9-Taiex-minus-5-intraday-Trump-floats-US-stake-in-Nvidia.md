---
signal_id: "SIG-W-20261125-001"
date: "2026-11-25"
timestamp: "2026-11-25T05:01:38Z"
dispatched: "2026-11-25T05:01:38Z"
source: "AP via Yahoo Finance 2026-11-24 23:05 ET (page read); investingLive two pages 2026-11-25 (read); Business Insider via Yahoo UK 2026-11-24 20:03 ET; vendor bars fetched 2026-11-25T05:00Z"
origin: ["AP via Yahoo 2026-11-24 23:05 ET", "investingLive 2026-11-25", "vendor bars 05:00Z"]
action: ["VULCAN", "SAM", "HENRY", "VIOLET"]
info: ["LIQUID", "ZHAO", "REGINALD", "NEXUS", "BROCK", "RED", "PROME"]
precedence: "IMMEDIATE"
signal_type: "divergence"
confidence: 0.85
confidence_language: "intraday vendor bars and two outlets; closes not yet set"
resources: 1
safety_net: "clear"
cluster: "POSITIONING_VALUATION"
domain: "MARKET_VOL"
entities: ["Kospi", "Taiex", "SoftBank", "Samsung", "SK-Hynix", "Kioxia", "TSMC", "Nvidia", "Arm"]
word_count: 411
dispatch_note: "IMMEDIATE (index-mechanics spike). ACTION VULCAN, SAM, HENRY, VIOLET. No safety-net or registered line crossed. TERRY BOARD-only. RED, PROME by BOARD diff."
event_window: "open"
---
# Asia AI selloff Wed Nov 25, intraday (vendor bars to 04:45Z, not closes): Kospi -5.8%, Taiex -5.2% (low about -8.6%), Nikkei -2.8%; SoftBank -14.4%, Kioxia -13.9%, Tokyo Electron -12.7%, SK Hynix -10.0%, Samsung -9.3%; TOPIX and Hang Seng little moved; no single cause sourced; Trump says he thought about a US stake in Nvidia

# Asia, Nov 25 (Korea, Japan, Taiwan still trading at the read)

| Object | Nov 24 close to last read (low) | Basis |
|---|---|---|
| Kospi | 5,006.03 to 4,717.22, -5.8% (low 4,687.51) | vendor 5-minute bar 13:40 KST |
| Taiex | 40,122.35 to 38,038.32, -5.2% (low 36,681.90, -8.6%) | vendor, 12:40 Taipei |
| Nikkei 225 | 58,644.63 to 57,014.02, -2.8% (low 56,502.97) | vendor, 13:45 JST |
| SoftBank | 3,166 to 2,709, -14.4% (low 2,652, -16.2%; AP: -16.1%) | vendor |
| Kioxia / Tokyo Electron | -13.9% / -12.7% | vendor |
| SK Hynix / Samsung / TSMC | -10.0% / -9.3% / -4.3% (TSMC low -9.4%) | vendor |
| TOPIX, Hang Seng, Shanghai | TOPIX under -0.5% to -1%; Hang Seng flat to +1%; Shanghai about -1% | investingLive, AP |
| US futures | ES 7,165 at 23:45 ET (Nov 24 vendor settle UNKNOWN), Yahoo page S&P -0.72%, Nasdaq -1.23% | vendor, not settlements |
| USD/JPY | 159.4 | vendor |

| Why, as reported | Basis |
|---|---|
| AI returns and governance doubts, profit-taking after Tuesday's rebound (Kospi +6%), possible new US tariffs, foreign net selling | AP, investingLive citing Reuters; **no single cause sourced** |
| US lead: Nvidia -5.9%, CoreWeave -11.8%, Anthropic under its $83 offer price on Nov 24 | AP |
| Trump to the New York Post, Tue Nov 24: 'I thought about it ... I didn't bring it up at this point. It's probably not too late' on a US equity stake in Nvidia; a Huang pardon is 'an option'; Huang testifies to Congress next week | Business Insider via Yahoo, investingLive; NYP not read. A remark, not a proposal |

- **SAM (SoftBank):** Arm closed 161.56 [11/24, vendor], from 176.67; low close this run 152.20 [11/20]. SAM's corrected 25% loan-to-value line sits at Arm about $146 to 150 (SAM STATUS 11/18). **Arm has not crossed it; SoftBank's own price is not that instrument.** Arm does not trade until US hours.
- **VIOLET, HENRY:** the Nov 23 rebound has reversed in Korea and Taiwan within two sessions; VIX cash last 26.36 [11/24 close], futures not read. No WALTER trigger has fired; a 30 cross is checked from the 09:30 ET open and premarket.
- **So what:** the selling is narrow (chips, SoftBank), not an Asia-wide risk-off: broad Japan and Hong Kong barely moved. Thanksgiving week liquidity is thin on both sides.
