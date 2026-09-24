---
signal_id: SIG-W-20260924-022
date: 2026-09-24
timestamp: 2026-09-24T20:41:13Z
time_dispatched: 2026-09-24T20:41:13Z
source: RESEARCH-INTAKE
origin: ["RESEARCH-INTAKE lane run 2026-09-24T18:47Z, newssweep DEVELOPMENT position-pe (BM-20260924-02 item 11)", "Read by WALTER: Investing.com 2026-09-24 14:16 ET (body fetched; the article says it was AI-generated and editor-reviewed)", "WALTER pull: APO daily closes, Yahoo, 9/18-9/24"]
domain: PRIVATE_CREDIT
cluster: PC_STRESS
precedence: PRIORITY
action: ["BROCK"]
info: ["SHADE"]
entities: ["APO", "Apollo-Global-Management", "Athene", "APO-options-flow"]
confidence: 0.60
confidence_language: one AI-assisted options-flow article with an intraday snapshot (13:40 ET), not an end-of-day OCC tally; the direction (hedge vs short) is not knowable from volume
signal_type: context
resources: 2
safety_net: clear
word_count: 330
verdict: "Investing.com (9/24 14:16 ET, AI-assisted): APO options volume reached 80,673 contracts by 13:40 ET, puts a RECORD 79,823 vs 850 calls (~94:1). Four Oct-16-2026 put strikes ($105/$110/$115/$125) carried 56,004 contracts; at $115 and $105, 19,001 contracts each traded against open interest of only 484 and 507, i.e. NEW positions. APO closed $120.69 on 9/24 (Yahoo), -2.95% on the day and -5.6% from $127.91 on 9/21. The flow is consistent with either a hedge or a directional short; the article itself gives both readings."
---

# Apollo (APO): record put volume, about 94 puts per call, mostly new October positions

**Short version:** By **1:40 PM ET on 9/24**, APO options had traded **80,673 contracts**. **79,823 were puts, a record, against 850 calls (~94:1).** Four **Oct-16-2026** put strikes carried **56,004** of them:

| Strike (Oct-16) | Volume | Open interest before |
|---|---|---|
| $125 | 9,001 | 10,851 |
| $115 | **19,001** | **484** |
| $110 | 9,001 | 11,744 |
| $105 | **19,001** | **507** |

At $115 and $105, volume is about 40× the prior open interest, so these are **new positions, not rolls**. **APO closed $120.69 [9/24, Yahoo daily], −2.95% on the day and −5.6% since $127.91 [9/21].** 3-month implied vol: 36.39% (article).

## Why BROCK and SHADE
- **BROCK:** APO is a named PE/alt-manager name in BROCK's book. The FORGE mirror lists an **APO $95 put, Dec-18** as a BROCK thesis vehicle (mirror vintage per its own header; the off-repo broker is truth). **The flow is at Oct-16 strikes $105–125, not that strike or expiry.** Recent context on the same lane: Blue Owl marking a private loan to near zero (`SIG-W-20260914-019`).
- **SHADE:** Apollo/Athene is the canonical PE-insurer nexus.

## Caveats
1. **Source quality:** the article says it was **generated with AI support and reviewed by an editor**. The figures are an **intraday snapshot (13:40 ET)**, not an end-of-day OCC tally. WALTER has not checked them against an exchange or OCC primary.
2. **Direction is unknown.** The round lots (9,001 / 19,001 at four strikes) look like **one structured order, possibly a single counterparty**. A put ladder like this can be a hedge on a long position as easily as a short. **Do not read "record put volume" as "the market is betting on an Apollo collapse."**
3. **No catalyst was found in this item.** WALTER did not search for an APO-specific news event behind the 9/24 drop.

## Requested action
BROCK: decide whether this changes your read of APO or the vehicle. Checking OCC end-of-day volume, and whether 9/25 open interest confirms the new positions, is BROCK's call. SHADE: info.
