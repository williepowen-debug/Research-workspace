# TERRY → PROME · 2026-09-26 Sat 15:14 ET (`date`) · WQ-292: two ITM put management cards, prepared (preparation only)

**`$0` moved · no order · no trade proposed · no gate or threshold moved.** The cards go back to Will under root rule #5.

## Bottom line
Both puts are in the money on the **2026-09-25 close**. Today is Saturday, so that close is the freshest. Figures are screening marks from `fetch.py` and `chain_fetch.py --no-cache`, pulled 15:09 ET 9/26.

| line (mirror: qty/cost `[9/10 CLOSE view]`) | underlying 9/25c | ITM by | bid/ask | ×2 at bid vs cost | card |
|---|---|---|---|---|---|
| TLT Oct-16 $82P ×2 | $79.32 | $2.68 (TLT needs +3.38% to reach the strike) | 3.00/3.10 | **$600 vs $336 (+$264)** | `AGENTS/TERRY/setups/TLT_oct16-82P_ITM-management-card_2026-09-26.md` |
| HBAN Oct-16 $16P ×2 | $15.64 | $0.36 (HBAN needs +2.30%) | 0.45/0.80 (56% wide) | **$90 vs $192 (−$102)** | `AGENTS/TERRY/setups/HBAN_oct16-16P_ITM-management-card_2026-09-26.md` |

- **Named UNKNOWN on both cards:** what Fidelity does, in this IRA, with an ITM long put and no shares at expiry: auto-exercise, close-out or lapse.
  - Fidelity's public pages were read 2026-09-26. They state auto-exercise at ≥$0.01 ITM and a Do-Not-Exercise phone deadline of 16:15 ET on the last trading day. DNE forfeits the intrinsic value.
  - They say **nothing** about the case where exercise would create a short stock position in an IRA (SEARCH-NOT-FOUND). The FAQ's list of allowed IRA strategies omits short stock, but that is an omission, not a stated policy.
  - Both cards carry **one question** for Will to ask Fidelity, covering both lines in a single call.
- **Dated decision point: Wed 10/14 close. Backstop: Fri 10/16 before 16:00 ET.**
- **TLT card:** choices are A harvest / B hold to expiry / C hold, then close by 10/14; D (DNE) is dominated.
  - A vs C is a thesis call (Will, with BOND/HENRY). The structure read is that B is the only branch that runs through the unknown.
  - ⚠️ DOCKET's **10/1 FR2004 row** names this leg under BOND's duration-short kill rail. WQ-291 is HELD. The card does not pre-empt it.
- **HBAN card:** Will's 7/18 letter ("rides to expiry, do not pay to close") **stands**.
  - Its premise has failed: it was written for ~$20 of OTM dust where the commission roughly equalled the proceeds. Now it is $1.30 of commission against ~$90.
  - "Zero effort" also fails if HBAN is below $16 on 10/16, because the put then enters Fidelity's exercise process.
  - The letter does not call for DNE. Re-rule options R-A (sell to close) and R-B (close on 10/16 if still ITM) are listed, not recommended. TERRY did not re-rule.
  - HBAN reports Q3 on **10/22 BMO**, after expiry (HBAN IR schedule), so construction rule #18 is not engaged.
- **Holdings "confirmed" only as far as the mirror goes.** Both lines' quantities sit on the **9/10 CLOSE** clock. The 9/16 capture and the 9/18 receipt do not cover them. WQ-274 gaps ① (Activity view) and ⑤ (current-book capture) touch both. The account type (Traditional IRA) is itself INFERRED.

## Also this session
- Inbox drained 1/1: the BRENT F1 packet. It was info-only, is logged `noted`, and was moved to processed/.
- BOARD scan run: 21 action-line signals, all logged.
- Cards use `MGMT-` ids and are registered in `setups/INDEX.md`, with no SETUPS row, because the SETUPS/TRADE_BOOK rotations are still owed.
- `ledger_sweep` CLEAN (A–H) · `read_cap_check` rc=0 · weekday claim_check clean.

## COMPLETION — TERRY — 2026-09-26
STATUS: ✅ DONE
CHANGED: AGENTS/TERRY/setups/{TLT_oct16-82P,HBAN_oct16-16P}_ITM-management-card_2026-09-26.md (new), setups/INDEX.md, setups/HBAN_oct16-16P_stub.md (pointer), STATUS.md, board_log.tsv, inbox BRENT packet→processed — commit 40e12ee0a; this memo
RESULT: 2 management cards built for WQ-292. TLT 82P ITM $2.68, ×2 $600 at bid vs $336 cost. HBAN 16P ITM $0.36, ×2 $90 vs $192 (9/25 close, screening). The Fidelity IRA ITM-no-shares expiry handling is the named UNKNOWN on both, with one question to ask. HBAN 7/18 letter stands and its premise failed (commission $1.30 vs ~$90). Decision point Wed 10/14.
GAPS: Fidelity's IRA short-on-exercise handling is not on any public Fidelity page read (3 pages, 9/26), so it needs Will's call. Quantities are 9/10-view (WQ-274 ①⑤ open). CPI/FOMC dates before 10/16 not verified by TERRY.
WILL_NEEDS: (1) Ask Fidelity the single question on both cards (by Mon 9/28 ideally). (2) Confirm qty ×2 each + IRA account. (3) By Wed 10/14: TLT choice A/B/C; HBAN ruling stands or re-rule R-A/R-B.
FOLLOW-UP: A consumer read of DOCKET 10/1 FR2004 (BOND kill rail, WQ-291) bears on the TLT 82P. SETUPS/TRADE_BOOK rotations still owed at TERRY's next full session.
