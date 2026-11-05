# DEWEY -> PROME: L567 three-issuer refresh delivered; 003R PARKED after a corrected availability read
**Date:** 2026-11-04 | **Session:** DEWEY, Claude Code, claude-opus-5-5, dewey-f0, Will-launched; Will's go 20:45 ET. **Cost:** $0.
| Row | Result |
|---|---|
| **D:L567** | Capital One Q3 10-Q (0000927628-26-000152) read in full. Domestic modified cohort delinquent $645M to $993M (+54.0%, book +11.1%), share 25.2% vs 15.7-18.0% prior. Scale 113.31 bp (June 119.27). Three-issuer refresh complete. Cause UNKNOWN; causal test NOT COMPUTABLE. CARL owns next. |
| **REQ 003R** | PARKED. FFIEC 4,259 of 4,268 Q3 filers; FDIC BankFind 0 rows. The unavailable-data deferral is not met and was not recorded. Will was told the deferral first, then the correction. |
- ⚠️ `scripts/edgar_doc.py`, `edgar_fetch.py` and other DEWEY tools hard-code Will's personal email in the SEC User-Agent. One `exhibits` call this session sent it; remaining pulls used a generic client. Pre-existing. Will is asked, in the DEWEY window, how to handle it. BACKLOG row added.
- WQ-495.CDR: FFIEC token expires November 5. The row is open; DEWEY cannot see renewal state.
```
STATUS: ⚠️ PARTIAL — L567 delivered; 003R residual not run (PARKED)
CHANGED: AGENTS/DEWEY/{output/2026-11-04_carl-dr1-cof-q3-fdm-three-issuer-final.md, output/INDEX.tsv, research/2026-11-04_cards/, CONTEXT.md, scripts/BACKLOG.md, board_log.tsv}; packets AGENTS/CARL/inbox (1), AGENTS/WALTER/inbox/DEWEY (2), PROME/inbox (1)
RESULT: Three-issuer Q3 card refresh complete; Capital One scale 113.31 bp and an unexplained cohort delinquency rise to $993M (+54.0%). 003R parked on a measured 4,259 of 4,268 FFIEC filers against 0 FDIC rows.
GAPS: Cause of the Capital One move unknown, filing silent, no primary transcript. 003R band, EGBN and VLY residuals not done because the registered FDIC feed has no Q3 rows.
WILL_NEEDS: None beyond WQ-495.CDR renewal and his answer on the email User-Agent.
FOLLOW-UP: PROME updates DOCKET L567 on consumption; CARL reads; WALTER logs and updates the 003R ledger note.
```
