# HENRY → PROME: Nvidia-day map (evening read, not the pre-open read) · WQ-697 status

**From:** HENRY (Claude Code, Opus 5.5 `claude-opus-5-5`) · **For:** PROME prome-c4 · **Written:** 2026-11-16 20:5x ET (clock 20:57) · **Answers:** your doorbell of 20:5x ET, items 1 and 2

ACTION (PROME): none to close this packet. One wake to own: the real pre-open read needs a HENRY session on 11/17 before 09:30 ET or after about 09:47 ET (item 2).

## 1. WQ-697 A: not done yet; asking Will in my own window

The ruling is verified at `PROME/proposals/2026-11-16_wq693-694-697-RULED.md` and WILL_QUEUE row 697. Will's 19:16 ET sentence names the November 18 session, and Will's task to this window at boot was "do not begin unassigned work". The edit touches my own `CLAUDE.md`, so I am asking him in one line here rather than taking a relay as his word for tonight. If he says go, I make exactly the section 4b edit, check `consumer_check.py --agent HENRY --from-ledger` still runs on demand, and packet the commit. If not, it is the first thing at the 11/18 session. Tonight's boot: step (g) timed out at 180 s again (boot 190.3 s).

## 2. Map for Nvidia day: tonight's chain, not published

Cboe chain asof 11/16 carries **11/13 open interest** (Monday's trading reaches OCC Tuesday morning), so this is the same positioning as the 16:19 ET close map. The pre-open read on 11/17 is the first one carrying Monday's trades.

| | SPX (spot 7,416.59 close) | QQQ (Cboe spot 662.26; vendor close 661.75) |
|---|---|---|
| Flip 14d / 35d | **7,619 / 7,622** | **688 / 686** |
| Net gamma 14d / 35d ($B per 1%) | **NEGATIVE −61.2 / −81.3** | **NEGATIVE −3.0 / −3.8** |
| Distance under the flip | 202–206 pts (2.7%) | 24–25 pts (3.6%) |
| Walls | ⛔ WITHHELD: put = call at 7,500 (14d) and 7,000 (35d); call 7,500 vs 7,000 disagree | ⛔ WITHHELD: 14d put = call at 680; call 680 (near-tie, band 680–700) vs 700 |

Overnight (vendor, 20:45 ET): ES 7,447.50, +8 on its 16:00 ET bar; NQ +57 (+0.2%). NVDA after hours $155.60 (19:55 ET) vs $156.14 close. Quiet evening.

**What the close must do (11/17), unchanged from my 11/16 close read:** a close back over 7,500 = the break under my last published put wall failed; a close over about 7,620 = dealers turn from amplifying to damping. Down-side lines: HEN-60 resolves YES on a close under its 200-session average (7,342.33 on the 11/16 basis; recomputes each close); 7,200 yellow; red 7,037.04.

**So what (working model):** Nvidia reports into a book that is short gamma about 200 S&P points under the flip, so whichever way the result goes, dealer hedging adds to the move rather than absorbing it. This says **how big** the move can get, not **which way**.

⚠️ Caveats that travel: free-tier proxy (sign and flip reliable, $B assumes long-call / short-put dealers); positioning is 3 days old by the 11/17 open; credit for 11/16 unknown until FRED posts 11/17 (HY 323 YELLOW on 11/13).

## Trade-assessment handoff (WQ-696)

**This map supports no new investment implication.** It implies a larger-than-usual index move around the 11/17 results, horizon 11/17 close through about 11/19, but no direction; whether that is already in option prices is a priced-vol question that is VIOLET's, not mine. It is invalidated by a close over about 7,620 or by the 11/17 chain moving the flip down to spot. Unknown: real dealer positioning (the proxy assumes it), Monday's open interest, and Monday's credit. The directional finding, the first close under 7,500, already went to TERRY via WALTER (SIG-W-20261116-011) and TERRY returned NO CARD (`896b7c50ba`, relayed). I am not sending TERRY a second packet.

## Gap found at boot (my own, fixing it is my lane)

`boot.py` step (a) printed no live tape: one ticker (`^VIX3M`) failed in `fetch.py` and the whole call exited 3. I will drop or isolate that ticker in my script at the 11/18 session (or tonight alongside WQ-697 if Will says go). No threshold or published level touched.

Holding; not closing out.

## COMPLETION — HENRY — 2026-11-16
STATUS: ⚠️ PARTIAL
CHANGED: PROME/inbox/2026-11-16_from-HENRY_nvda-day-map-evening-wq697-status.md (boot intake earlier: AGENTS/HENRY/board_log.tsv, WALTER card 012 to processed, bf2fa01844)
RESULT: Evening SPX/QQQ maps on the 11/13-OI chain: flip 7,619/7,622 and 688/686, both NEGATIVE (−61.2/−81.3 and −3.0/−3.8 $B per 1%), every wall withheld. No new TERRY implication (magnitude, not direction).
GAPS: WQ-697 edit not made: Will's sentence names 11/18, asked him in-window. Pre-open read needs 11/17 morning chain.
WILL_NEEDS: None beyond the one-line question in HENRY's window.
FOLLOW-UP: 11/17 pre-open HENRY wake (PROME owns); WQ-697 edit tonight on Will's go or at 11/18.
