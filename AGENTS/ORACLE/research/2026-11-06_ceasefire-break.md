# Effective-ceasefire legs broke after the 11/06 close

**Written:** 2026-11-06 about 17:25 ET, from pulls at 22:15–22:20Z. Bounded check on Will's close-refresh word, not a research thread. Cause NOT established.

## What moved (Polymarket, event `us-iran-effective-ceasefire-continues-through...`)

| Leg | Log 20:26Z | Log 22:15Z | Book 22:20Z | CLOB 21:00Z → 21:15Z | Implied strike by date, book mid | 24h vol | Liq |
|---|---|---|---|---|---|---|---|
| Through 11/15 | 59.0 | 31.5 | 35/37, then 30/33 at 22:23Z | 60.0 → 42.5 | about 64 to 68.5 | $172.2K | $64.3K |
| Through 11/30 | 40.0 | 27.0 | 26/28 | 39.5 → 29.5 | about 73 | $66.3K | $71.3K |
| Through 12/31 | 28.5 | 16.0 | 15/17 | 29.0 → 18.5 | about 84 | $57.1K | $96.9K |

The 11/15 leg is still swinging: Gamma 31.5 at 22:15Z, 36.0 (35/37) at 22:18Z and 22:20Z, 31.5 (30/33) at 22:23Z; raw CLOB top 33/34 at 22:18Z. Quote it as a 31.5–36 range, implied strike about 64 to 68.5. 11/30 and 12/31 stayed within 1 point (27.5 and 15.5 at 22:23Z). No leg has resolved (`closed` false, 22:23Z).

## Timing and tape (Polymarket v2 trades, 20:30Z to 22:14Z)

- Flat until 16:00 ET: the 11/15 leg sat at 57.0–60.5 from 12:30Z to 21:00Z (15-min CLOB).
- First push 21:04:01Z (16:04 ET): about $6.1K in one second on 11/15, three wallets, $5.0K of it one wallet (`0x60a92c`).
- Sharpest push 21:12:55Z (16:12 ET): about $9.0K from one wallet (`0x5d8af5`), 52 → 42 on 11/15.
- Partial bounce to 48.0 at 21:30Z, then lower to 36.0–39.0.
- Notional since 20:30Z: $48.6K on 11/15 (339 trades, 102 wallets, top wallet 25.5%), $25.5K on 11/30 (51 wallets), $15.9K on 12/31 (28 wallets). All three legs net toward strike ($28.2K, $11.8K, $2.7K, my side classification).
- The 500-trade API limit did not cut this window.
- ⚠️ Resting depth near the touch was small at 22:18Z: top four levels held bids of $270, $135 and $448. The liq figures above overstate how much money it takes to move these legs.

## What did not move (20:30Z → 22:15Z)

| Market | Before | After | Source |
|---|---|---|---|
| WTI $110 Nov | 20.0 | 19.5 | PM CLOB, liq $36.5K |
| US invade Iran <2027 | 10.5 | 11.5 | PM CLOB, vol $78.3M; had been 11.5 at 19:00–20:00Z |
| US declares war by 12/31 | 2.35 | 2.25 | PM CLOB |
| Iranian regime fall <2027 | 3.0 | 2.85 | PM CLOB |
| Hormuz normal by 12/31 | 9.5 | 9.5 | PM CLOB |
| WTI Dec `CLZ26` | 90.57 (21:00Z) | 90.34 (21:55Z) | Yahoo 5-min last, not a settlement |
| Brent Jan `BZF27` | 97.94 (21:00Z) | 97.76 (21:55Z) | Yahoo 5-min last, not a settlement |
| S&P future `ES=F` | 7,401.25 (21:00Z) | 7,404.0 (21:55Z) | Yahoo 5-min last |

Reading: the move is confined to the contract that resolves on one strike of any size. A qualifying strike need not be large: the 11/2–11/3 Qeshm action counted on the retired legs (KB-ORC-111). Flat invade and war legs fit a crowd pricing a limited strike, or a few traders on a narrow book. These data cannot separate the two.

## Public record checked

- WALTER card SIG-W-20261106-043 (22:15Z): Qatar's Prime Minister said no comprehensive deal and urged a good one, read at 17:52Z and 19:03Z, three hours BEFORE the break. "Mediation ended" and "so it's war" unsupported. Shafaq, one source: CENTCOM "completed preparations", not established.
- Al Jazeera live blog, modified 22:07Z: Trump says the US is talking to Tehran's representatives, after a call with Qatar's emir; IRGC claims a US drone downed over Qeshm and tankers hit. Page text read only in part; item times not recovered. A drone shoot-down is not a qualifying action.
- Three web searches returned nothing dated after the break and no report of a US strike on 11/06. ⚠️ The search index lags, so this is weak evidence of absence. Wire desks, CENTCOM and UKMTO not reached.
- Kalshi: `search "Iran strike"` 0 hits, NOT CERTIFIED (page cap). No independent venue read.

## Not established

Cause; whether any trader had information; whether the level holds into Monday. Do not call this insider flow (`CLAUDE.md` Type 3 needs liquidity and public-news checks; the news check is incomplete).
