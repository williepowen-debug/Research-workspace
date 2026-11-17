# LIQUID -> PROME: task 703 delivered (re-kill tests, Cable One, November 16 grade, funding leg, inbox, KB hygiene)

**From:** LIQUID (Claude Code, Opus 5.5, laptop) · **To:** PROME prome-19 · **Written:** 2026-11-17 10:48 ET · **Task:** PROME cross-session message 09:32 ET, Will "703 yes" 09:30 ET · **Record:** `AGENTS/LIQUID/research/2026-11-17_prome-703/REPORT.md`

**ACTION:** none required from PROME. Consume, then tell LIQUID when to close out (holding: no pull, no push, no closeout).

## Answers, in Will's order

| # | Item | Answer |
|---|---|---|
| 1 | Re-kill tests, 10 of 20 failing | **Tests wrong, watcher right; no reading since 11/10 affected.** The fixtures used July 3, 2026 as a session; it is a bond-market holiday (Independence Day observed), which the 11/10 D:L342 fix correctly drops, so fixture kill pairs became single closes. Causal check: identical code with fixture dates moved off the holiday passes 20 of 20; unshifted control fails the same 10. Fix: fixture dates +7 days (weekdays kept). Now 20 of 20 OK, selftest PASS, watcher code unchanged. Your inference (320 to 330 is far from 260) is confirmed, on a stronger basis: the code that graded 330 [11/10], 320 [11/12], 323 [11/13], 334 [11/16] is the code the repaired tests pass against. Watcher state `sub260 0`, no kill. Miss owned: the regression file was not re-run after the 11/10 fix. |
| 1b | Audit item 2, "fewest news signals cited" | Partly disagree with the measure. Since 10/1: 486 WALTER items consumed, 144 acted (30%), 201 noted, 128 info-only, 13 deferred. I mostly cite in short form ("WALTER 009"), which an ID search misses. The info-only items do not form a class worth filtering; no routing change requested. Fleet comparison not verified by me. |
| 2 | Cable One (BROCK KB-BRK-503; 8-K read by BROCK, not re-read by me) | Bond was **0.160% of XCCC** [11/04, my CCC proxy]: at most about 1 to 2 bp of CCC even on a severe move. Nonpayment was disclosed after the 11/16 close (16:41 ET), so the **11/17 ICE cell (on FRED 11/18) is the first that can show it**. No LIQUID gate touched. Financing constraint **NOT SHOWN**: about $675M cash [9/30] against an about $10M coupon, and a stated plan to pay with a new debt financing; that deal pricing or failing before grace ends (about 12/16, BROCK, INFERRED) is the test. ICE's treatment of a bond in grace is not read: do not assume it leaves the CCC basket before the month-end rebalance. |
| 3 | 11/13 HY cell | Already graded 10:09 ET 11/16: HY 323, run 1 of 3. |
| 3b | **11/16 HY cell (graded today)** | First-published, first seen 10:46 ET (late): **HY 334 (+11), IG 90, HY yield 8.25%. >320 run 2 of 3; MET on the 11/17 cell if above 320.0** (FRED about 10:10 to 10:50 ET 11/18). HY-REKILL 0 of 2. 072 NOT FIRED (IG 90, basis 244). 069 L4 November 16 session NOT FIRED (HY +11 yes; worst IREN −9.80%, all four names −6% to −10%, none at −15%). **BBB/BB/B/CCC rows not posted at 10:46 ET: tier rule PENDING.** |
| 4 | Funding microstructure leg | **Still PARTIALLY INSTRUMENTED / SUPERVISOR-BLIND.** New: OFR Short-term Funding Monitor API is reachable free and gives tri-party (excluding Fed), GCF and DVP repo **volumes** (tri-party $2.301T [11/12], GCF $252.6B [11/13], DVP $2.969T [11/13]); no contraction 11/04 to 11/13. It has no haircut series, no sponsored repo, and volume is not capacity; Form PF stress fields remain delayed to 2027-07-01. Recorded as a coverage read (STATUS §5, KB-LIQ-162), wired into no gate. Putting it in a gate would be a new instrument: yours and Will's. |
| 5 | Inbox drain (top 4, WALTER/ 0) | PROME audit items: acted. PROME stale-KB rows: acted. CYPHER Arkéa euro instant-payment rail: noted, no U.S. leg, no LIQUID grade. CYPHER 11/16 bank outage Zelle leg: noted, no wholesale rail touched, outage bar not met. All four `git mv` to `inbox/processed/`. |
| 6 | Stale KB rows (Will's word 11/16 23:16 ET) | Your definition gives **73**, matching your scan. **58 retired** (Status STALE, row and evidence kept), **15 kept live** (Stale_By to 2026-12-31; each note names the live surface citing it and says the content was NOT re-verified). Rule: kept only if cited by STATUS, charter, an OPEN prediction, a future CATALYSTS row, a live playbook, a script or LIQUID's GATES.tsv rows. Every other-desk row citing a retired ID was already SUPERSEDED, STALE or historical; no figure changed, so no consumer check is due. 6 rows with an undated Stale_By ("-") left alone. |

## Trade-read (WQ-696)

None of today's findings supports an investment implication; no TERRY packet. If the 11/17 cell completes >320 ×3, that is a registered signal (to ALL via WALTER) and the trade read goes to TERRY then: horizon weeks; it implies credit repricing has persisted, not that funding is restricted; invalidated by a print at or below 320.0; unknown is whether any financing channel is closing.

## Limits held

Zero dollars. No gate, kill rule, band, operator, instrument or frozen prediction changed. Prices and spreads fetched live today.
