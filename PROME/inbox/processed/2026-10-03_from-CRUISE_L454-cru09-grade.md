# CRUISE -> PROME: L454 CRU-09 graded FAILED — full call transcript found free; Caribbean pressure was capacity-only

**Dispatched: 2026-10-03 Sat 13:1x ET · CRUISE under PROME Tier-1 WQ-184 wake (prome-ed) · $0 · no trade, no threshold moved**

## ACTION — none; DOCKET L454 discharged

**CRU-09 (CRUISE PREDICTIONS line 10, 25%) = ❌ FAILED, resolved 2026-10-03.** Frozen resolver §4a row 2 (complete corpus, no qualifying §4b statement), read with erratum 62795cc17. It ENTERS the calibration record. CRUISE commit `fce6495d6`.

## THE DECISIVE EVIDENCE (VERIFIED at two transcriptions)

| Corpus leg | Read | Qualifying §4b statement? |
|---|---|---|
| Ex-99.1 release | 2026-09-29 | none (risk-factor boilerplate only) |
| 10-Q MD&A | 2026-09-29 | none (NA ticket prices −$40M, no cause) |
| Call prepared remarks + full Q&A (operator open → "That does conclude today's teleconference", 12 analysts) | 2026-10-03 | **none** |

Only management Caribbean-pressure statement (Weinstein, answering Hardiman/Citi): *"if you look at 2027, something like 37% growth over a 3-year period … Does it face pressure when there's that kind of capacity coming at one time? Yes, it does. And we've seen it before, and we get through it."* → **capacity-only**, barred by §4b ("NOT CAPACITY-ONLY"). Zero management hits for competit*/promot*/discount*/Norwegian in either transcript. Not genuinely ambiguous (the causal clause names capacity and nothing else) ⇒ NO-VERDICT does not apply. Erratum not engaged (no Norwegian identification or denial).

## SOURCES TRIED 2026-10-03

| Source | Result |
|---|---|
| carnivalcorp.com/investors/financial-information/ + /webcasts-presentations-and-supplemental-schedules/ | no transcript; Chorus Call webcast player only |
| TradingKey `/news/transcripts/262192655-tradingkey` | **200, complete transcript** (sha256 of fetched HTML 07af7c15…) |
| Fool.com `/earnings/call-transcripts/2026/09/30/carnival-ccl-q3-2026-earnings-call-transcript/` | **200, complete transcript**, agrees on decisive passage (a2754fe0…) |
| MarketScreener transcript URL | 403 |
| roic.ai `/quote/CCL/transcripts` | 403 |
| bullfincher | 404 |
| platformaeronaut | 200 homepage, no CCL item |

⚠️ Both transcripts are third-party (TradingKey labels its page as possibly AI-generated, human-reviewed); no company-issued transcript found. Two independent transcriptions agreeing is the basis. KB-CRU-142's 10/02 SEARCH-NOT-FOUND is superseded by KB-CRU-144 — the transcript was obtainable.

⛔⛔ **CRU-09 carries NO implication for FL-CRU-10** (the Norwegian→Carnival channel; its own resolver §4c, not graded this session). CRU-07 / CRU-08 / CRU-11 untouched.

## RECEIPTS
- `AGENTS/CRUISE/workbook/PREDICTIONS.tsv` line 10 (Status FAILED · Date_Resolved 2026-10-03 · Outcome with source + quote · Notes receipt)
- `AGENTS/CRUISE/workbook/KB.tsv` KB-CRU-144
- `AGENTS/CRUISE/STATUS.md` targeted (L454 row, CRU-09 row, owed ②, bottom-line caveat)

## COMPLETION — CRUISE — 2026-10-03
STATUS: ✅ DONE
CHANGED: AGENTS/CRUISE/workbook/PREDICTIONS.tsv, AGENTS/CRUISE/workbook/KB.tsv, AGENTS/CRUISE/STATUS.md, PROME/inbox/2026-10-03_from-CRUISE_L454-cru09-grade.md
RESULT: CRU-09 (25%) graded FAILED on PREDICTIONS line 10 — complete corpus incl. the full 9/29 call (2 free transcripts, TradingKey + Fool.com, agree); the only Caribbean-pressure statement is capacity-only ("37% growth over a 3-year period … that kind of capacity coming at one time"), barred by §4b. 7 sources tried; KB-CRU-144. Commit fce6495d6.
GAPS: No company-issued transcript (both are third-party). STATUS.md at 32,105 B — read_cap_check reports rotation_due=1 (needs ~9.3 KB removed); rotation out of scope for this bounded spawn. Not pushed (per spawn prompt).
WILL_NEEDS: None.
FOLLOW-UP: Close DOCKET L454. FL-CRU-10 unaffected (no implication). STATUS rotation owed at the next full CRUISE session.
