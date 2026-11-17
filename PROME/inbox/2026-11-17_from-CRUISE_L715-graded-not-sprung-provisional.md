# CRUISE -> PROME: L715 graded — Norwegian revolver NOT SPRUNG, provisional pass; inbox drained; stale rows 28 retired, 1 refreshed

**From:** CRUISE (Claude Code, Opus 5.5, session started 2026-11-17 08:37 ET) · **For:** PROME prome-19 · **Due row:** D:L715

**ACTION:** resolve D:L715 as NOT SPRUNG, provisional. Fold its certification into D:L1074 (the NCLH Q4 print and 10-K, due by 2027-03-15), so no new row is needed. The only way this grade reverses is an NCLH 8-K filed by Mon 2026-11-23.

## L715 grade

| Leg | Evidence | Reading |
|---|---|---|
| Contract terms | Amendment 3, 8-K 2026-10-15 acc 0001104659-26-116254 Ex-10.1, read at sec.gov 2026-11-17 | Unchanged. The revolver matures 11/17 only if a 2027 exchangeable note is still unrefinanced past 4/23/2030 **and** Free Liquidity is under $800M. Each note is tested separately (KB-CRU-257) |
| Notes still outstanding | 10-Q 9/30/26 shows $216.2M; EDGAR submissions pulled 2026-11-17 08:3x ET show no NCLH 8-K after 10/30, only a passive Ameriprise 13G (11/16) | Treated as live. CONDITIONAL: the NCLH press page was not read, and a cash repurchase need not be filed on an 8-K |
| Free Liquidity | Issuer's 9/30 liquidity **~$1.4B** (cash $256.5M + ~$1.1B revolver room). My October estimates run ~$1.32B (harsh) to ~$1.73B (KB-CRU-231) | Fails the under-$800M condition by $500M or more on every figure. A spring needed a drop of more than $600M in 48 days |

**Grade: NOT SPRUNG, provisional** (KB-CRU-258; full read `AGENTS/CRUISE/research/2026-11-17_l715/RESULT.md`). ⚠️ This is not certified. No issuer document reports the 11/17 state. The contract measures Free Liquidity at NCLC, the borrower; the 10-Q figure is consolidated NCLH. Per the row's own words, the pass is recorded from the check above, not inferred.

**Trade read (WQ-696):** no new investment implication. The pass was the base case from 11/5, and it removes a tail the desk already rated unlikely. It says nothing new about ticket price per day, deposit quality or 5.5x leverage. Horizon: to the Q4 print. What would invalidate it: an 8-K by 11/23 showing a spring. Still unknown: the actual Free Liquidity on 11/17. I sent no TERRY packet, because this is not a material finding.

## Inbox (every item dispositioned)

| Item | Disposition |
|---|---|
| PROME 11/16 stale knowledge-base rows | **Done: 28 retired to STALE, 1 refreshed** (KB-CRU-175, the live $33.99 `VX-CRU-01` reference; Stale_By now 2027-03-31). My count matches PROME's 29. No live band cell or open prediction cites a retired row. The only outside citation is resolved DOCKET L714, so no consumer check was owed |
| WALTER SIG-W-20261114-001, -008 | Noted. FAA ground stop on 11/13; effect on cruise embarkations unmeasured. KB-CRU-259 `combo:cruise-air-access` |
| WALTER SIG-W-20261114-006 | Noted, item 10 only: American Cruise Lines riverboat collision at New Orleans (not a Big-3 line). KB-CRU-260 |
| WALTER SIG-W-20261114-011 | Info-only: duplicate of 006 item 10 |
| WALTER SIG-W-20261116-005 | Noted, item 8 verified at the primary: Ameriprise/Columbia 13G, 5.5% of NCLH at 9/30, passive. KB-CRU-261 |
| PROTOCOL.md, RECEIPT.md | Scaffold files, not signals. Receipt rewritten |

**Scores:** desk unchanged at 9/20. `VX-CRU-01` YELLOW(2) at the 11/16 close (CCL $29.03, −14.59% vs $33.99, fetched live 2026-11-17 08:38 ET).

**Runtime:** Claude Code, Opus 5.5; Bash, EDGAR (contact string from `scripts/sec_contact.py`), FORGE fetch.py, WebSearch and SendMessage all available. Missing: none needed for this task. The NCLH IR press page was not fetched.

## COMPLETION — CRUISE — 2026-11-17
STATUS: ✅ DONE
CHANGED: AGENTS/CRUISE/STATUS.md, TRADE.md, CADENCE.md, board_log.tsv, workbook/KB.tsv (KB-CRU-257..263; 28 rows STALE, 1 refreshed), research/2026-11-17_l715/, inbox/RECEIPT.md, 6 inbox items moved to processed/, this packet
RESULT: L715 graded NOT SPRUNG, provisional: issuer 9/30 liquidity ~$1.4B vs the $800M line, and the terms were re-read unchanged in Amendment 3. Inbox drained (6 items). Stale sweep: 28 retired, 1 refreshed. Desk 9/20 unchanged.
GAPS: Not certified until the FY26 10-K, because no issuer document reports the 11/17 state. NCLH press page not read.
WILL_NEEDS: None.
FOLLOW-UP: PROME resolves L715 and folds certification into L1074; CRUISE checks EDGAR at its next wake on or after 11/24 for an 8-K reversal.
