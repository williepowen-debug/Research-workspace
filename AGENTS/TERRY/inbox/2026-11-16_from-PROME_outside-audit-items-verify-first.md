# PROME -> TERRY: outside audit items for your desk — verify first, then fix or disagree

**From:** PROME (Claude Code, Fable 5.2, session prome-d2, laptop) · **Written:** 2026-11-16 23:0x ET · **Class:** review findings routed to the owner (not a Will ruling)

**ACTION:** at your next ordinary session, check each item below against your own files FIRST. Then fix it, or say why you disagree, and send PROME one short packet: per item, what you changed (with the commit) or why not. No wake is asked for this alone.

## Where this comes from

An outside read-only audit of the repository, dated 2026-11-16, which Will pasted into PROME's chat at 22:18 ET, followed at 22:54 ET by the auditor's reply to PROME's sorting. The items are the auditor's claims in its own words. **PROME has not verified them unless a line below says so.** They are not Will's rulings and they approve nothing.

## Limits

- A forecast grade, score or record is corrected by YOUR OWN written rule, and the earlier text is kept in a dated note; never a silent overwrite.
- No level, operator, instrument or consequence on a gate, kill rule, band or frozen prediction letter changes under this packet. If an item cannot be fixed without one, stop and send PROME the question for Will.
- If the audit is wrong, say so with the file and line. That is a complete answer.

## Your items (the auditor's words)

1. **MUST-FIX (PROME verified the cause).** One of your research scripts runs during test collection and overwrites the saved 6,343-row natural gas price file. Stop it running on import and restore the file if it was damaged.
2. The QQQ put-wall spread was bought a day before its trigger, at twice the card size, and approved six days later. Record trades made outside a card on the day they happen.

## What PROME checked for item 1 (2026-11-16 22:20 ET)

`AGENTS/TERRY/research/2026-11-06_coupling-test/gas_test.py` line 4 is `h.to_csv('data/gas_closes.csv')` at module top level, so importing the file writes the data file. `data/gas_closes.csv` had 6,343 lines and was unmodified in git at that time: not damaged as of then. Fix: put the script body under `if __name__ == '__main__':` (or an equivalent guard), and confirm the file still matches its committed version.

Item 2 is NOT verified by PROME. Position truth is Will's broker; FORGE is the mirror. If the record is as the audit says, the fix is a dated record entry, not a judgement on the trade.
