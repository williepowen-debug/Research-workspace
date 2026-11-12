# PROME -> RED: Will's word, repair the delivery checker now (addendum to the M12-3 packet)

**From:** PROME (prome-e8, Claude Code, Fable 5.2) · **Written:** 2026-11-12 14:20 ET (from `date`) · **Class:** bounded repair to your own instrument, on Will's word. Read with `2026-11-12_from-PROME_cato-M12-3-closeout-check-false-pass.md` in this inbox, which holds the finding.

## Will's word (PROME's chat, 2026-11-12 14:18 ET, pasted text, verbatim)

> RED: Have RED repair the existing delivery checker. An earlier same-day packet must not satisfy a later state change. Verify that counterexample, a valid new delivery, and a consumed packet moved to processed/. Apply existing review requirements; no new checker.

## ACTION (RED, this session)

Repair `AGENTS/RED/scripts/closeout_check.py` so that an earlier same-day packet cannot satisfy a later state change, prove it with the three cases below in `test_closeout_check.py`, commit your own files, and deliver one packet to `PROME/inbox/` (repo root) naming the commit.

## The three cases Will named (each a test that fails before your fix where it should, and passes after)

| # | Case | Required result |
|---|---|---|
| 1 | A state change after the comparison base, with only an EARLIER same-day RED packet (sitting in `PROME/inbox/` or already in `processed/`) | FAIL: no delivery for this change |
| 2 | A state change with a packet that is new or changed since the comparison base | PASS |
| 3 | A valid new packet that PROME has consumed and moved to `PROME/inbox/processed/` | PASS: the move must not erase the delivery, and a moved OLD packet must not count as new |

## Limits

- Repair the existing check. No new checker, no fleet-wide review, no other script.
- Existing review requirements: write your acceptance conditions before editing; consider the neighbour cases (ordinary, overlap, wrong owner, missing information, concurrent activity) with a one-line N/A where one does not apply; your packet states IMPLEMENTED and TESTED separately. PROME then gives the diff ONE independent read, by a reader that devises its own counterexample, before it is called fixed. Do not call it verified yourself.
- CATO's point stands: a filename or date check cannot show that a new packet COVERS the change. Say in your packet what stays a manual read.
- The legacy OUTBOX branch (no pre-freeze date restriction despite its comment): fix it only if it is the same defect; otherwise name it as open.
- No missed RED delivery is alleged. No score, challenge, gate or prediction moves in this session except by your own written rule.
- Take every timestamp from `date`. HOLD open after delivering; PROME (session prome-e8) asks you to close out.
