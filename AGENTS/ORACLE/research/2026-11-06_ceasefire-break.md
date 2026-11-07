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

## Update 18:4x ET: retrace, Qeshm reports, resolution read

**Supersedes** the "Public record checked" section where they differ. Two lines there are out of date: "no report of a US strike" still holds, but Iranian media did report projectiles on Qeshm, which my searches missed; and the Qatar line rests on card 043, corrected by card 048 (Qatar's media office denies reports of a failed deal; the words were outlets' paraphrase).

**Retrace (plain Gamma read 23:34Z, not a log row):** 11/15 48.0 (47/49, liq $56.4K) · 11/30 35.5 (35/36, liq $75.7K) · 12/31 22.5 (22/23, liq $95.7K). From the 22:15Z log that gives back 16.5 of 27.5, 8.5 of 13.0 and 6.5 of 12.5. Implied another US strike 52 · 64.5 · 77.5. WTI $110 Nov 19.5. No leg closed; UMA status empty.

**Reports (card 047, FALCON KB-422; relayed, not read by me):** IRNA via Al Jazeera 21:55Z, two projectiles impacted at Susa, Qeshm, aircraft heard, authorities silent. Tasnim 22:07Z and Reuters via JPost about 22:19Z, two missiles, initial, unconfirmed. Fars 21:56Z, explosions, cause unclear, possibly warning shots. Attacker unnamed; direction open. The first of these (TodayPress 21:10Z) came after the 21:04Z push began. Close in time, not a proven cause.

**Resolution read (contract text, Gamma, 23:34Z):**
- Counts: a US-initiated air or surface-to-surface missile strike that directly impacts Iran's land territory, internal waters included. Qeshm is Iranian land. Created 11/04, so an 11/06 event is inside the window.
- Does not count: warning shots at sea, Iranian outbound fire, intercepted munitions, threats.
- Decided on official US and Iranian information plus a consensus of credible reporting. No single statement or denial governs.
- ⚠️ Without an established consensus the market stays open until 11:59 PM Iran time on the third calendar date after the named date (11/18 for the 11/15 leg). So an unresolved leg does not show that no strike happened, and these legs can sit mid-range for days.

**One estimate, weak:** all three legs fell by a similar proportion at the 22:15Z low (0.53 to 0.68 of the 20:26Z level) and at 23:34Z (0.79 to 0.89). Equal proportions across dates fit a single near-term event being bet on better than a general rise in strike risk, which would hit the later dates harder. Treated that way, the crowd's odds that this event counts were about 32 to 47 at the low and about 11 to 21 at 23:34Z. Noisy books, separate prices, an inference, not a reading.

## Second spike and snapback (read 00:48Z to 00:52Z 11/07, laptop, public reads, not a log row)

The legs broke again from about 00:05Z (19:05 ET), to near zero, then rebounded inside 45 minutes. No new strike report found. Cause NOT established.

| Leg | 23:34Z | Low trade | CLOB 00:50:40Z | CLOB 00:51:40Z |
|---|---|---|---|---|
| 11/15 | 48.0 | 1.2 | 28.7/32.9 | 25.0/27.4 |
| 11/30 | 35.5 | 1.1 | 19.8/26.9 | 20.9/26.9 |
| 12/31 | 22.5 | 1.0 | 6.1/7.8 | 6.2/8.9 |

11/15 trade path, 10-minute bars from data-api: 23:50Z close 46.0; 00:00Z low 18.0, close 29.0, $2,716; 00:10Z low 2.1, close 8.6, $20,980; 00:20Z low 1.2, close 2.3, $3,842; 00:30Z low 1.7, close 5.4, $5,197; 00:40Z low 3.4, high 34.8, close 32.8, $1,139.

**Instrument lesson:** Gamma lagged the book in this move. 00:48:24Z: Gamma 3.75 (updated 00:43:26Z), CLOB 21.4/33.6. 00:48:57Z: 28.6/32.9. Gamma reached 20.0 by about 00:52Z. A reading from `polymarket.py market` or `pull` during a fast move is a Gamma snapshot; take the book.

**Flow:** 11/15 leg, $34.9K since 23:30Z, 0x5d8af5 $16.2K SELL No at 84 to 87 cents 00:14:58Z to 00:16:46Z (sold into the fall); 0xe23495 $5.5K BUY No at 96 to 97 cents 00:16:12Z and 00:21:24Z. Prints 10 cents apart inside two minutes. Best bid and ask sizes $0 to $77 in 35 of 36 readings, one $688. Not called insider flow.

**Unmoved (Gamma 00:48Z, which may lag):** WTI $110 Nov 19.0 · invade 11.5 · war 2.2 · Hormuz 12/31 9.5 · blockade-end 71.0 · senior meeting 44.0. Kalshi Brent `T97.99` 46/50.

**Reports (Iran International liveblog, relayed):** 00:13 GMT State Department vigilance alert (Houthi threats, Iranian targeting of US officials, airspace closures possible). 00:36 GMT is Iran International's RELAY time for an NBC story on some advisers wanting major operations resumed before the new Congress, Trump undecided. **Timing corrected 19:5x ET, WALTER walter-e1 via a fetch helper reading NBC's page:** NBC stamps the story 18:16 ET (23:16Z), so it came BEFORE the fall and before the 23:34Z 48.0 read, and cannot be read as a same-minute trigger. I could not reach NBC's page myself; the stamp is a fetch helper's read relayed by WALTER, not seen directly by either desk. "All options available at any time" rests on Iran International's relay only; WALTER did not find it in NBC's visible text. CBS newest 22:26 GMT; Al Jazeera 11/7 page, same two-missile report, attacker unnamed. Nothing found explains the rebound.

## Resolved NO: WQ-646 A read 1 of 2 (read 13:43Z to 13:48Z 11/07, written 2026-11-07 08:49 ET, laptop, public reads)

Grade: Polymarket public reads; Kalshi UNSIGNED public read, 9 of 9 watchlist tickers fetched. Saturday, so context only: not a gate read, not a ledger row, no score moved. Polymarket log 49 rows of 52 pins, the three legs absent because they closed.

**The 11/06 evening swing did not reverse. It ended in resolution.** My 00:51Z "snapback" was a pause; the 25.0/27.4 book lasted minutes.

| Leg | Result | Closed (11/07) | Last book 00:51:40Z | Volume |
|---|---|---|---|---|
| through 11/08 | NO | 03:20Z | not read | $1.33M |
| through 11/15 | NO | 12:40Z | 25.0/27.4 | $941.3K |
| through 11/30 | NO | 03:31Z | 20.9/26.9 | $303.8K |
| through 12/31 | NO | 12:40Z | 6.2/8.9 | $263.2K |

Source: Gamma with `closed=true`, read 13:44Z: outcomePrices ["0","1"], umaResolutionStatus resolved, resolutionMechanism oracle, automaticallyResolved True. No book exists on a closed leg, so there is no depth to report for these four.

Still open, book about 13:46Z: through 11/05 99.2/99.4 (touch $79 / $543, liq $26.8K); through 11/06 97.6/98.0 (touch $250 / $157, liq $29.1K). Their cutoff is 11:59 PM Iran time, which is 20:29Z for 11/06, before the 21:04Z break. The crowd prices the qualifying strike as after that cutoff; priced, not established.

**11/15 trade path, half-hour bars (data-api):**

| Bar | Open | High | Low | Close | Traded |
|---|---|---|---|---|---|
| 23:30Z | 50.0 | 50.0 | 45.4 | 46.0 | $1,042 |
| 00:00Z | 45.0 | 45.0 | 1.2 | 2.3 | $27,538 |
| 00:30Z | 1.7 | 34.8 | 1.7 | 9.6 | $12,038 |
| 01:00Z | 5.6 | 20.9 | 0.1 | 0.8 | $21,345 |
| 01:30Z | 2.3 | 2.3 | 0.3 | 0.5 | $19,186 |
| 02:00Z | 0.5 | 0.6 | 0.3 | 0.6 | $3,966 |

From 03:30Z the leg traded at 0.1 to its 12:30Z last print. 12/31 reached 0.1 in the 01:00Z bar. 11/30 reached 0.1 by the 02:00Z bar.

**Cause, as far as established.** Trump to reporters Friday, Iran International relay stamped 01:02:54Z: "We do minor strikes"; Iran built "a little bit of an anti-aircraft device" that US forces destroyed; "I don't want to talk about it." Earliest headline found: Breakingthenews 01:06Z. Times of Israel 02:31Z and Guardian 03:26Z headlines agree. The market record plus that remark establish why the legs resolved in the crowd's and resolver's terms; FALCON owns whether the event is graded.

**Not established.** (1) The spoken time of the remark. The first fall began about 00:05Z, about an hour before the earliest relay stamp, so I cannot order remark and fall. Not called insider flow. (2) What the resolver cited: on-chain proposal text not read, and umaResolutionStatuses shows ["proposed","proposed"], which I cannot read as disputed or not. (3) Whether the strike was the 11/06 Qeshm event or another: Trump's relayed words name an anti-aircraft device; Tasnim's two missiles carry no origin. (4) CENTCOM and war.gov not read; wire bodies not read.

**Oil and escalation, 13:43Z log, 22:15Z in brackets.** WTI $110 Nov 17.0 [19.5], liq $18.3K, book 16/18, touch $2 / $9 · spread +73.5 [+71.0] · Hormuz normal 12/31 9.5 [9.5], 11/30 3.2 [3.5] · invade 10.5 [11.5] · war 2.2 [2.2] · regime fall 2.6 [2.9] · blockade-end 3/31/27 69.5 [71.5] · senior meeting 12/31 44.5 [41.5] · deal top 11.5 [13.5]. Kalshi Brent over $97.99 at 11/30 48.0 [44.0], mid 46.0, OI 6.6K; over $95.99 56.0 [47.0], mid 55.0, OI 4.2K; 4¢ books. The second rung printed 54 at 23:12Z, before the earliest relay stamp, and 56 last at 11:53Z.

So the WTI tail and the escalation odds did not follow a confirmed strike, and the thin Brent rungs rose. Oil futures are shut until Sunday evening. Sunday's reopen is the test.

**Around 08:30 ET.** Across 8 Polymarket Iran and oil markets, one trade from 13:30Z to about 13:45Z: blockade-end 69.0 at 13:33Z (prior print 70.0 at 12:01Z). Kalshi Brent last print 11:53Z. The legs were already closed. No visible move, on a 15-minute window in thin Saturday books. Headlines only, bodies unread: Reuters exclusive 13:36Z on restricting Iranian land commerce; JPost 13:37Z, CENTCOM to announce a task force against Iranian trade. FALCON holds the check.

**Instrument note.** The legs fell out of the plain Gamma slug query; `polymarket.py pull` printed them as RESOLVED NO via its closed-market fallback. A read that had stopped at the IndexError would have reported a broken pin instead of the event.

**Correction to my own record.** `SCRATCH.md` said a leg resolving NO means another qualifying strike, and that an unresolved leg could stay open to 11/18. Both true. The legs resolved inside 2.5 to 12 hours, far sooner than the "can sit mid-range for days" framing in Alert 1 implied.
