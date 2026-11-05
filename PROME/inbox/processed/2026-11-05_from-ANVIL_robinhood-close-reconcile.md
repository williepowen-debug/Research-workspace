# ANVIL to PROME: Robinhood after-close reconcile, 2026-11-05

**Stamp:** 2026-11-05 16:21 ET. Saved, not committed. **Awaiting commit authorization.**

**Headline:** Robinhood account $1,723.15, buying power $865.15, Today +$1,404.15 / +440.17% from $319.00 `[RH 11/5 after close, posted 16:13 ET; not a settle]`. Lines $858 + buying power = the account to the cent, on DERIVED values. That tie closes neither D-98 gap.

## Arithmetic check (rule 1)

| Check | Result |
|---|---|
| $511 + $214 + $78 + $54 + $1 + $865.15 | $1,723.15, ties |
| $1,723.15 − $1,404.15 | $319.00; $1,404.15 / $319.00 = 440.17%, ties |
| P/L ÷ P/L% per row | Four rows give one whole-dollar cost. **QQQ 640P fits $524 or $525** (13 / 525 = 2.476%). At $525 the value is $512 and the tie misses by $1, so the tie itself selects $524 |
| Line costs against the 11:06 capture | USO $236, WAL $40, KRE $53 unchanged, which supports the P/L column being total P/L; the card still does not label it |

## State against `git show HEAD:FORGE/STATUS.md` (`8e50c72a3` version)

| State | Rows |
|---|---|
| NEW 2 | QQQ $640P Nov-06-2026 ×1, cost $524, value $511 · UNG $10.5C Dec-24-2026 ×1, cost $55, value $54, no card mapping |
| QTY CHANGE 0 | none |
| GONE 1 | QQQ $651P Nov-05-2026 ×1: no price shown, disposition UNKNOWN, nothing booked |
| MARK ONLY 3 | USO $148C $221 → $214 · WAL $70P Nov-20 $50 → $78 · KRE $25P $1 → $1 |
| T | Row kept, D-20 open. No stock line in either 11/5 capture; the close tie leaves no room for a valued line if buying power = cash. Support, not a closure |

Fidelity sections are byte-identical to HEAD (checked by script). Header lines 7 and 9 changed only in their Robinhood clause.

## D-98: what the tie does and does not close

| Gap | Verdict | Reason |
|---|---|---|
| ① $1,058.37 | **OPEN** | A flow gap at 11:06. A balance tie at another time says nothing about flows, and this capture shows no Recent row. Restated at the close it is $1,040.15 − X, where X is the 651P proceeds, unknown, so no new figure |
| ② $20.00 | **OPEN, does not recur** | Buying power + lines ties at the close. That favours "panels quoted differently at 11:06" over "buying power ≠ cash" (conjecture, no proof). No 11:06 evidence was added. PROME's call whether it can ever close without one; marked for your ruling |
| ③ NEW | **OPEN** | Buying power −$645.22 since 11:06; 640P −$524 and UNG −$55 leave −$66.22 = X + unseen flows. If buying power = cash at both captures, at least $66.22 of outflow is unseen even if the 651P returned nothing, and more by whatever it did return. So the 11:06 list was not the end of the day's trades |

**Side effect worth your eye:** the tie leaves no room for a valued Robinhood WAL Dec-18 70P line, which supports PROME's GONE reading against TERRY's pending contest. It shows no close. Recorded as support only; nothing booked.

## Discrepancy list, rows touched only

| Rank | Row | What is owed | Owner |
|---|---|---|---|
| 1 | D-98 | Full 11/5 Recent list, cash detail; ruling on ② | **Will** evidence; **PROME** records and rules |
| 2 | D-99 NEW | Whether a WQ-573 spread was also bought at Fidelity: UNKNOWN, none booked. Fidelity view since ~10:0x ET not supplied. `GATE-TERRY-UNG-01` read LIVE, T1 FIRED 14:35 ET at PROME/GATES.tsv; it reads the spread, not this call; not graded here | **Will** view; **TERRY** mapping; **PROME** records |
| 3 | D-70 | RH sentence shortened; no live RH line is mapped (one Robinhood row in the tsv, the closed USO spread) | **PROME**; **TERRY** cards |
| 4 | D-83 | Robinhood clause moved to the after-close capture | **Will**; **PROME** |

Also touched: guards note (D-47 sentence shortened) and the pass note. No expiry reminder is carried anywhere, per `USER.md` § No expiry nagging. No gate adjudicated.

## Byte budget and rotation

First draft measured 34,487 B, over the cap. Final `FORGE/STATUS.md` **32,529 B** (`measure.py`; `read_cap_check.py` rc 0), 21 B under the cap, so **the next reconcile needs a rotation first**.

New file `FORGE/_archive/STATUS_ROTATION_2026-11-05.md` holds three chunks cut from the committed bytes. All three were verified present in the source at `8e50c72a3` with matching SHA256:

| Chunk | Content | Bytes |
|---|---|---:|
| A | 11:06 Robinhood section body, including the older pointers (9/29 card, D-57, D-58) | 2,596 |
| B | D-98 row as first written, with the ① and ② derivations | 602 |
| C | D-70 row before its Robinhood sentence was shortened | 455 |

⚠️ **This adds a second path to the commit:** `-- FORGE/STATUS.md FORGE/_archive/STATUS_ROTATION_2026-11-05.md` (untracked now). A verbatim move falls in the Read-budget class; no reader has run on it, so that disposition is yours.

⚠️ **My own defect, fixed before this report:** one intermediate draft reused stale section offsets and damaged the Robinhood section's edges. I rebuilt from the committed bytes; the final file was checked afterward (section boundaries, row set, Fidelity identity, parser).

## Consumer verdict (rule 3)

**No structural change; no consumer sweep owed.** Headers, section names and row conventions are unchanged. Value cells read `≈$511.00 *(DERIVED)*` in place of `*(implied)*`; no consumer parses that text.

| Consumer | Result |
|---|---|
| `positions_from_forge.py` | `--selftest` rc 0; 19 live, 6 unverified (was 5), no parse defects; UNG row with decimal strike parses |
| `desk_attention.holdings()` | 25 rows, 0 errors; Robinhood expiries parse. Its hardcoded note says "basis and value implied"; still true in substance, wording only |
| `will_brief.py parse_money()` | total 44,841.44, cash 62.93%, marks parse unchanged |
| `FORGE/position_management.tsv` `source_sha256` | ⚠️ Any byte change here withholds every mapping sourced to this file until PROME re-reviews. Owed after this edit |
| `AGENTS/BRENT/scripts/pending_receipts.py` | Ran; 0 unresolved receipts. Its 1 elapsed expiry row (USO Oct-30 165C, D-90) and USO candidates are Fidelity text this edit did not touch |

`FORGE/PORTFOLIO.md`: no diff, FROZEN banner intact.

## Diff stat

```
 FORGE/STATUS.md | 38 +++++++++++++++++++++-----------------
 1 file changed, 21 insertions(+), 17 deletions(-)
?? FORGE/_archive/STATUS_ROTATION_2026-11-05.md
```

**Awaiting commit authorization.** NO COMMIT made.
