# TERRY same-day triage — Cable One skipped coupon, Car-Mart 13th bridge, VIOLET timing check

**Written:** 2026-11-17 09:59 EST (system clock) · TERRY, Claude Code, Claude Opus 5.5 · task from PROME prome-19 (WQ-696 handoff; Will's standing word 2026-11-10 18:03 ET).
**Answer:** **NO window is lost by waiting to Wed 11/18 (D:L1128). NO CARD on Cable One, NO CARD on Car-Mart. No order. $0.**

## 1. Boot and dependencies

| Item | State |
|---|---|
| Repo root | `/home/willi/Research-workspace` (resolved with `git rev-parse --show-toplevel`; every path below is root-relative) |
| Instructions read | root `CLAUDE.md` (24,449 B) and `AGENTS/TERRY/CLAUDE.md` (23,176 B) loaded from those root-resolved paths; `AGENTS.md`, `USER.md`, `STATUS.md`, `RISK_RULES.md` read explicitly. No `AGENTS/TERRY/AGENTS.md` exists. |
| `boot.py` | ran; ledger sweep clean; BOARD: 52 addressed, all logged; inbox 7 unprocessed |
| Market data | yfinance via `.venv` works. Negative control: IWM lists 29 expiries in the same minute that CABO and CRMT list 0, so the empty chains are the names, not the feed. |
| Missing | Bond prices for the Cable One 4.00% 2030 notes: no zero-cost quote source on this box (TRACE not reached; no paid data per task limits). VIX November future: the vendor has no quote for it (404). MCP servers mtnewswire and definite failed to connect; not needed. |

## 2. What instruments exist (live, 2026-11-17)

| Name | Listed equity | Listed options | Other | Vendor quote |
|---|---|---|---|---|
| Cable One (CABO) | NYSE common | **none** (0 expiries, 09:57 ET) | 4.00% senior notes due 2030, over the counter, no quote reachable; other debt not checked | $3.0005, +1.0% vs $2.97 prior close; bid/ask $2.95 / $3.13 (6% wide); 12,421 shares by 09:57 vs about 573,000 average; market value about $17.0M on 5.68M shares; short interest 38.0% of float (vendor, date of the short figure not given); vendor marks the feed 20 minutes delayed, last trade stamped 09:57:10 ET |
| Car-Mart (CRMT) | Nasdaq common | **none** (0 expiries, 09:57 ET) | none tradeable known | $0.9479, +1.9% vs $0.93; vendor bid/ask crossed ($1.45 / $0.96), unusable; market value about $7.9M; short interest 30.6% of float (vendor) |

## 3. Cable One — NO CARD

BROCK's handoff carries all four WQ-696 parts (implication, horizon, invalidation, unknowns). Its direction: restructuring or exchange in which equity and the 2030 notes take terms. PROME's caveat travels: the missed payment and the stated intent are ESTABLISHED (8-K 0000950157-26-001261, accepted 11/16 16:41 ET); that it could pay from freely available cash is NOT (the about $675M is a 9/30 balance), and no motive is established.

Why no card:
1. **The owner's direction has no defined-risk instrument.** No puts exist. A short sale of a $3 stock with 38% short interest has unbounded loss and a squeeze path on the exact event BROCK names as the invalidator (a financing that leaves equity intact). Non-Negotiable #2 (defined loss) fails.
2. **The defined-risk instrument that does exist points the other way.** Long shares (max loss = the cost) is a bet that equity survives the financing, which is against the owner's read; Hard Boundary 3: I do not supply a direction. It would also be a call-side entry on a green tape (+1.0%), the wrong colour under root rule #6, with no measurement refuting the proxy.
3. **The notes** are the instrument the event actually prices, and they are not reachable or priceable here.
4. **Market reaction is small:** first session after the filing, the stock is up about 1% on thin volume after falling about 77% over 30 days (vendor 30-day range $2.96 to $15.38). Little left for a short to capture on the equity; the value now sits in the debt.

**Why waiting loses nothing:** no tradeable instrument exists for the owner's direction today or tomorrow. Clocks for the full read (BROCK's, partly INFERRED): grace ends about Wed 12/16; NYSE plan due about 12/28; MBI hearing 12/4 by press vs 11/13 in the 10-Q, unreconciled.

What would change it: listed options appear; a named public lender, BDC or other listed holder of the Cable One or MBI paper (BROCK KB-BRK-446 says no BDC holding is established); or a signed financing whose terms set an equity value.

### 3b. BROCK's liquidity follow-up (packet `2026-11-17_from-BROCK_cabo-liquidity-established-from-filings.md`, read 10:00 EST) — answer unchanged

BROCK, from the 10-Q (0001632127-26-000038) and 8-Ks: the $674.8M of 9/30 cash is borrowed (revolver $1.05B drawn at 9/30, the last $200.0M drawn 10/8, availability $0); $478.9M of it is claimed by the MBI put, held up by CoBank's restraining order; the issuer says its sources "will be insufficient" for its 2027 to 2028 maturities and uses Chapter 11 language; a 2030-notes default cross-defaults other debt; a delisting triggers the 2028 converts' put at par. BROCK corrects its morning "can pay, choosing not to": still a choice for this coupon only; for the company, reading (b), cannot meet its maturities without new financing. **Direction unchanged, severity higher.** Invalidation tests unchanged.

Effect on the trade read: **none on the verdict.** Higher severity strengthens the owner's direction, but the only instrument for it is still an unbounded short of a $17M market-value stock with 38% short interest, and a financing or restraining-order headline can still squeeze it. The converts' par put and the 2030 notes are where the severity is priced, and neither is reachable here. Still NO CARD, still no window lost by waiting.

## 4. Car-Mart — NO CARD (unchanged)

BROCK states "no new investment implication" with its reason (same standstill, shorter leash). The 13th bridge runs only to Wed 11/18 (8-K 0001171843-26-007505, accepted 11/17 08:00 ET; KB-BRK-501). Still no listed options, $0.95 stock, about $7.9M market value: a short has unbounded loss, a long is against the owner. 11/13 and 11/16 NO CARD basis stands. BROCK reads the follow-through Thu 11/19 AM; nothing on TERRY's side expires before that.

## 5. VIOLET handoff (PROME packet 2026-11-16 21:17 ET) — timing check only

Two windows do close before tomorrow's session: Nvidia reports tonight (Tue 11/17 after the close) and the November VIX contracts settle on Wed 11/18 morning. **Neither holds a card, so nothing tradeable is lost:**
- VIOLET states "no direction is forced"; PROME's packet asks for no pre-event card.
- Live at about 09:43 ET (vendor, 15 minutes delayed): VIX 22.83, VIX9D 23.32 (VIX9D/VIX 1.021, the event premium sits at the front, as VIOLET says), VIX3M 22.87, VVIX 111.02. Buying front-end vol now is paying for the event premium at its height, the case root rule #6's test exists to stop; selling it is not a defined-risk structure for this book.
- The Nvidia call-spread card (`IDEA-NVDA-CEOGAP-NOV12`, NOT approved) is a post-print card by design, window 11/18 to 11/20, so the print does not consume it. NVDA $155.96 (−0.1%, 09:58 vendor), $7.16 above the $148.80 invalidation low.
- Side read, QQQ 200-day card (`IDEA-QQQ-200D-NOV05`, NOT approved): T1 NOT MET at 09:58: VIX3M/VIX 1.002 but QQQ $662.15 +0.06%, not a red session. No grade beyond that.

The packet stays in the inbox for its own ask at the 11/18 session.

## 6. Inbox disposition

- Consumed and filed: `2026-11-17_from-BROCK_cabo-skipped-coupon-crmt-13th-bridge-trade-read.md` → `inbox/processed/`.
- Consumed and filed: `2026-11-17_from-BROCK_cabo-liquidity-established-from-filings.md` (arrived about 10:00; moved after BROCK committed it, bbe8d977b5) → `inbox/processed/`.
- Read for timing, left for 11/18: `2026-11-16_from-PROME_VIOLET-vol-handoff-nvda-soq-and-OTTO-turn-offer.md`.
- Left unread for 11/18 (ACTION lines checked: none due today): DAEDALUS ledger-sweep check E repaired; PROME outside-audit items; PROME postmortems thesis grades; PROME Will-word reconcile no-card report; PROME WQ-696 reader findings.

Gates, kill rules, bands and frozen predictions: none touched.
