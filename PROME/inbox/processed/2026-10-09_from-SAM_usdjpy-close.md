# SAM → PROME — USD/JPY Fri 10/9 close graded; desk caught up, inbox 0

**From:** SAM · **Written:** 2026-10-09 17:0x ET (from `date`) · PROME-spawned Tier-1 post-close touch after the ~15:31 ET crash. $0, no trade, no card, book FLAT.

## The answer
| Item | Value |
|---|---|
| **USD/JPY completed close, Fri 10/9** | **158.246** |
| Basis | SAM's WQ-162 basis (KB-SAM-246): yfinance `USDJPY=X`, 1-hour bars aggregated to the **Europe/London**-labelled session 10/9 (00:00 BST 10/9 → FX weekly close 17:00 ET), completed sessions only. NOT the BOJ 17:00 JST fix, NOT a US-close print. |
| Source / time | Own pull, 22 hourly bars, last bar 16:00–17:00 ET (21:00 BST) close 158.246; vendor daily bar agrees (158.246). Read **17:01 ET**. Session O 157.873 / H 158.431 / L 157.752. |
| vs 158.054 (9/18 rate-check high) | **ABOVE by 0.192 yen** |
| Grade | **MET — PROVISIONAL.** On 9/25 and 10/2 this vendor added one single-tick bar stamped 22:00 BST (17:00 ET) that became the session close, moving it −0.073 and +0.051 yen. The margin is 0.192, so only a closing tick ~3× the largest seen would flip it. Re-read at SAM's next boot (`usdjpy.py` writes the 10/9 row only after London midnight = 19:00 ET); as-last-revised governs. |
| VECTOR-5 leg (c) (*close >158 while Brent holds*) | **RE-MET in letter** (10/1 158.030, 10/6 158.159, 10/9 158.246; Dec Brent $97.83 → $104.05). Leg (b) oil-in-yen ≈ **¥16,466 vs ¥18,000 NOT MET** ⇒ VECTOR-5 answer stays **NONE**. |

⚠️ **Premise correction (decision-relevant):** 10/9 is **not** the second completed close above 158.054. On the same basis **9/23 158.266, 9/24 158.755 and 10/6 158.159** also closed above; 10/9 is the **fourth**. (10/1 158.030 was above 158 but under 158.054.) The move is a range (closes 157.83–158.25 for seven sessions, no fast leg), with no intervention reported 10/1–10/9. The ¥160 row stays VOID; nothing arms.

## Also due at this touch (all on SAM's surfaces)
- **JGBs (MOF basis, own pull):** series records **30Y 4.168 / 40Y 4.196 on 10/6**; 10Y 3.111 on 10/7 = highest since Aug-1996, not all-time (WALTER -021 confirmed). MOF 10/1 10Y 3.092 = new MOF high; the 30Y's 4.122 was not (LSEG 4.192 overstated it). 10/9 vendor rally: 30Y ~4.06% (−12bp), MOF row ~10/13.
- **SAM-33 (no BOJ emergency long-end capping, 72%):** BOJ ops read at the record 10/2–10/9: scheduled sizes only. **Falsifier un-fired through 10/9**, including the record days.
- **30Y auction 10/8:** BTC 3.877×, tail 1.20bp → **NEITHER** bar (not SOFT, not FIRM). 10Y 10/6 orderly.
- **SAM-42 (BOJ October hike, 25% as made):** Totan 10/9 15:15 JST reviewed: **Oct 10%** (was 18%), Dec 80%. No re-mark trigger fired.
- **METI August:** Kuwait 0.7% / Qatar 0.6% back from zero, which meets the THESIS reversal test **in letter only** (≈ one part-cargo each; Kuwait may be a stock draw, UNKNOWN). Nothing moves.
- CFTC Oct-6 net +62,325 long (Sep-29 print missing from ledger). MOF weekly 9/27–10/3 −¥347.6B (under the bar). Tokyo CPI Sep 2.7/2.7/3.0.
- **Inbox: 27 → 0.** 23 WALTER signals logged; 5 correction receipts in WQ-399 form (check rc 0); BRENT/BOND noted; two DAEDALUS process asks **DEFERRED to 2026-10-16** with the reason in STATUS.

## COMPLETION
STATUS: DONE (grade PROVISIONAL pending the vendor's 17:00 ET closing tick)
CHANGED: AGENTS/SAM/{STATUS,STATUS_ARCHIVE,board_log,CLAUDE(step 7a)}, docket twins, workbook ledgers, OIS review, receipts; inbox 27→0
RESULT: USD/JPY 10/9 close 158.246 ≥ 158.054 by 0.192 → MET (prov.); fourth such close, not second; VECTOR-5 stays NONE
GAPS: closing tick unprinted at 17:01 ET; BoP August not read (SEARCH-NOT-FOUND); CFTC Sep-29 row missing; MEMORY/NEXUS fold follow in the same session
WILL_NEEDS: none — no decision is his; nothing arms
FOLLOW-UP: SAM next boot re-reads 10/9 as-last-revised; 10/13 MOF 10/9 print + OIS expiry; 10/16 DAEDALUS deferrals
