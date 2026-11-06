# ZHAO -> PROME: close refresh, PBOC anchor missed, ZHA-24 needs a ruling

**Written 2026-11-06 ET on Will's refresh, relayed by prome-51.** Record: KB-ZHAO-237 to 240. Packet because two figures others may cite moved.

## Figures that moved

| Figure | Was | Now (date, basis) | Band or score |
|---|---|---|---|
| PBOC main policy rate | 1.40% 7-day reverse repo | **1.25% overnight reverse repo, since 11/02** (Xinhua and Reuters 11/02; PBOC site not read) | VX-6.06 label held; letter reads Yellow, label says ORANGE, flagged not re-derived |
| China 10Y | 1.63% (10/29) | **1.59%** (11/06, TradingEconomics, secondary) | VX-2.08 **YELLOW to ORANGE by its letter** (<1.60). Provisional band, 1bp inside. No vector keys on it |
| China-US 10Y gap | ~337bp (10/29) | ~327bp (11/06), directional only | Unchanged, ORANGE |

Desk total stays **29/60**. No forecast re-marked. No gate moved.

## The miss

The PBOC notice came 10/30 and the first daily overnight operation came 11/02, RMB 541B at 1.25%. STATUS named this as the change to watch and still showed 1.40% until tonight. Today's 11:18 memo carried ZHA-24 on the old rate. No WALTER card on it surfaced by title in BOARD, so the fleet may have missed it too. A pattern search found no other desk's STATUS or brief carrying 7-day 1.40; the bare-number consumer check returned 4,169 unfiltered candidates, 0 certified, and I sent nothing from it.

## Decision for PROME: ZHA-24

ZHA-24 (12%, registered 11/06 11:20 ET, DOCKET L1040) grades on the 7-day rate falling from 1.40%. That rate had already stopped being the anchor four days earlier.

- A multi-rate 7-day tender could print below 1.40 with no policy act: a false YES.
- A real cut would land on overnight, which the letter scores NO.
- So the row no longer measures PBOC easing.

**Recommendation:** withdraw it as defective at registration and re-register on the overnight rate from 1.25%, with a fresh base rate. I have not amended the row. Its Notes cell carries a flag pointing to KB-238; letter, confidence and status are untouched. The 2b check found only DOCKET L1040 naming it, no operator ruling.

## 11/10 clocks

| Clock | State at this read |
|---|---|
| MOFCOM 公告70 | No re-suspension at 06:21 Beijing 11/07. Page stamps 20:24 Beijing 11/06 bound what that proves |
| BIS stay | 2026-22793 still on public inspection for 11/09. ZHA-19 not graded |
| USTR ships | **No USTR document on public inspection for the 11/9 or 11/10 issues** at 17:20 ET 11/06. Suspension ends 11/9 23:59 ET. A special filing or site notice stays possible |
| US-China call | USTR readout 11/06: Greer and Bessent with He Lifeng; "concrete actions to fully implement" commitments on farm purchases, rare earths, critical minerals. Silent on 11/10 and 公告70. China's readout not found |

ZHA-20 stays 85%, held under your bound. That mark predates the call, the first adverse input since it. I will weigh it at L482 on 11/9. The "two-thirds of commitments" figure reached me only through a social-media summary citing the FT: unverified, do not relay.

## Run-book defect fixed

The MOFCOM unit API returns HTTP 200 and an empty list unless `parseType=bulidstatic` is sent. Read as written, the run book would have produced a false "nothing filed" on 11/9 or 11/10. Fixed in the run book, CATALYSTS and STATUS.

## COMPLETION — ZHAO — 2026-11-06
STATUS: ⚠️ PARTIAL (refresh done; ZHA-24 and two charter lines wait on others)
CHANGED: AGENTS/ZHAO STATUS, NEXUS_BRIEF, VX 8 rows, KB-237..240, ZHA-24 Notes flag, CATALYSTS, run book, 2 correction receipts.
RESULT: Data through the 11/06 close. VX-2.08 to ORANGE by letter. No score, grade or forecast moved.
GAPS: SAFE Oct reserves and gold, GACC Oct trade unpublished, cells left missing. PBOC site, ChinaBond and China's call readout not read. SOFR 11/05 stays latest; NY Fed API not re-read. Kospi, HSI, Nikkei 11/06 closes unavailable.
WILL_NEEDS: His word in ZHAO's window on the two CLAUDE.md lines (unchanged). The STATUS and brief PBOC line was stale; anything relayed from them before tonight needs correcting.
FOLLOW-UP: PROME rules on ZHA-24. ZHAO runs L482 Mon 11/9, then ZHA-19 and ZHA-20 at 11/10 to 11/11.
