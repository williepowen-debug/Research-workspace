# SAM → PROME: no re-opener filing. SoftBank's first Tokyo session after the results was a failed sell-off: closed ¥3,855 (−0.44%), low ¥3,465, ¥3,400 held (D:L1110, WQ-184), 2026-11-11

**Row keys:** DOCKET **D:L1110** (WQ-184 wake, prome-2b). USD/JPY side grade (not a row). **Scope:** research only, $0; no trade, card, gate, band, threshold, prediction or charter moved. LIQUID's Tokyo-hours credit leg not duplicated.
**Record:** `AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-11_TOKYO_SESSION_READ.md`; STATUS header, SoftBank line and the 160 threshold row updated; KB-SAM-262 member added.

**Plain words for Will:** Tokyo marked SoftBank down 7% at the open on the loss, then bought it all back by the close on heavy volume. The panic line (¥3,400) was not tested. Nothing new was filed, so TERRY's "no trade" stands. The yen is 0.6 yen from 160, the line where Japan has stepped in before, but it is drifting there slowly, not lurching.

## D:L1110, item by item (completed 11/11 session, 09:00–15:30 JST)

| Item | Read | Against | Basis |
|---|---|---|---|
| Close | **¥3,855, −¥17, −0.44%** | ¥3,872 | vendor daily (yfinance) = kabutan, exact match on O/H/L/C/V; both secondary, JPX not read |
| Open / low / high | **¥3,592 (−7.2%) / ¥3,465 (09:15 JST bar) / ¥3,903** | low vs ¥3,400: **held by ¥65**; 11/9 intraday low ¥3,358 | same; low→close +11.3% |
| Volume | **82,666,600 = 1.28×** | 64.8M | same; highest of eight sessions |
| Dated "wrong if" (close < ¥3,400 on volume > 64.8M) | **NOT fired**: volume leg yes, price leg no | — | — |
| Context | Nikkei +1.30% (vendor, bar maybe not final): SoftBank lagged by ~1.7 points. ADR SFTBY 11/10 −4.09% on the vendor's revised close $11.26 (−4.00% quoted 11/10) | — | vendor |
| Leverage roll | **22.7% (22.9% with the ¥140.2B settlement); ABB-inclusive 23.6–24.0% unchanged; 25% at Arm ~$145** | Arm **$181.49, 11/10 close** = latest completed Arm session at the Tokyo close; USD/JPY 158.81 at 06:00Z | `ltv_lookup.py`; unchanged because Arm has not traded since |
| New 9984 TDnet filing | **NONE**: full 11/11 list read, 8 pages, 08:00–21:00 JST, no 99840 entry; 11/10 had only the 15:30 results | — | TDnet primary, fetched ~08:42 ET |
| Arm sale / collar / share-backed loan | **None found**: Arm's SEC filings show nothing since the 11/4 6-Ks | ⚠️ an SBG-only filing would not index under Arm's CIK | EDGAR submissions API, ~08:45 ET |
| Call transcript | **Not posted**: IR page has transcripts for Q1 only; Q2 paths 404; 11/10 webcasts are video | — | group.softbank, ~08:44 ET |

**Not found:** what drove the intraday recovery (one secondary search, no same-day report). Rating action after the results: LIQUID's leg, not searched.

## USD/JPY side grade: PROME dashboard 159.37 at 08:35 ET (vendor) against the 160 line

| Item | SAM's own read |
|---|---|
| Live | **159.382** (13:00 London hourly bar close, high 159.389; boot spot 159.38 at 13:38Z). PROME's 159.37 **consistent**, separate feed, not blended. A live print, not a session |
| Basis | 11/10 completed London-label session 158.704 (matches `USDJPY.tsv`); 11/11 so far +0.68 yen (+0.43%), range 0.73 yen |
| Distance | **0.62 yen under 160**; highest since 9/1 (8/28–9/1 sessions closed 159.35–160.19); 160 last touched 70 days ago |
| Speed | a grind, far under the fast-move bar (≥1.5–2%/day or 2–3 yen in 1–2 sessions) |
| Official words 11/11 | none found (one secondary search; not evidence of absence) |
| **Grade** | **160 not crossed**; an investigation level, not a trigger; no SAM signal to WALTER. The risk side of the carry read stays the 160 / MOF leg, no unwind signature |

## Inbox drained (every sender)

WALTER SIG-W-20261110-012 (correction of card 010, relaying SAM's own 11/10 read): noted, filed; COR-20261110-12 receipted NO-OP. No other inbox items, no `MSG-*`.

## COMPLETION — SAM — 2026-11-11
STATUS: ✅ DONE
CHANGED: AGENTS/SAM/research/outputs/2026-11-06_softbank/2026-11-11_TOKYO_SESSION_READ.md, AGENTS/SAM/STATUS.md, AGENTS/SAM/workbook/KB.tsv, AGENTS/SAM/board_log.tsv, AGENTS/SAM/registry/corrections_receipts.tsv, AGENTS/SAM/inbox/WALTER/processed/SIG-W-20261110-012.md, boot workbook rows; this packet
RESULT: D:L1110 read in full: 9984.T closed ¥3,855 (−0.44%) on 82.7M (1.28×), low ¥3,465 above ¥3,400, the dated "wrong if" did not fire; roll 22.7% / 22.9% at Arm $181.49; no TDnet or Arm SEC filing, so TERRY's NO CARD re-opener is not met; Q2 transcript still 404. USD/JPY 159.38 (own bars) confirms PROME's 159.37, 0.62 yen under 160, a grind.
GAPS: Recovery driver not found (no same-day report in one search). JPX official figures not fetched (two vendors agree). Rating actions and Tokyo-hours credit are LIQUID's.
WILL_NEEDS: None.
FOLLOW-UP: The roll moves at the 11/11 US Arm close. CFTC (11/13) is the first print covering the 11/5–6 selloff. SAM holds the window for PROME's closeout ask.
