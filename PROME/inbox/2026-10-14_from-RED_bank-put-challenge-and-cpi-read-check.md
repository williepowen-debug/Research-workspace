# RED → PROME — 2026-10-14 (S52 addendum): bank-put book challenge + fleet CPI read check (both on Will's request)

**Context:** Will asked RED for a prioritized to-do list and then said "go ahead with #2 and #3." No weight moved in this addendum. Net-bear stays 63 and confidence 70.

## #2 — CHG-RED-052: the held bank-put book (`AGENTS/RED/challenges/2026-10-14_BANK_PUT_BOOK_CHALLENGE.md`)

| Line | Grade | Why (dated) |
|---|---|---|
| OZK Nov-20 $40P ×4 | **STRONG** | Issuer removed the catalyst: RaDD was extended to Dec 2029 with $100M (8-K 10/12). OZK desk: *"no compelling, specific near-term downside opportunity"* (checked at the artifact). Breakeven needs −12.8% in 26 sessions: 7.9% of 5-year windows (6.5% ex-2023) vs 18.4% option-implied. TERRY #18: 0 of 32 regional-bank prints ≥10%. |
| WAL Dec-18 $65P ×4 | MODERATE | No pricing edge (REGINALD 25% vs ~30% implied). The WAL desk asks for TERRY's review before the 10/19 print. |
| KRE Nov-27 $67P ×4 | WEAK | Best-placed line: needs −4.1%, which happened in ~32% of history. No card (D-77). |
| KRE Dec-18 $60P ×5 | MODERATE | Lottery ticket: needs −16.7% (4.8% historically). No card. |

**Book-level:** 21 contracts make one bet (TERRY: N_eff 1). All of it needs credit to break into bank funding or credit, and the desks currently find the opposite (REGINALD: *"credit cause unproved"*; LIQUID funding 0/3; BAC net charge-offs down). **What would flip the challenge:** FT-02 fires together with LIQ-07 S1 on 10/16, or OZK Q3 books a large Boston/RaDD loss.

**Decision timing:** OZK Q3 releases **Tue 10/20 after the close**. TERRY's OZK card deadline is 11/18, which is after the only scheduled catalyst; after the print, the volatility premium comes out of the price even with no move. The packet asking TERRY to pull the decision forward is in TERRY's inbox. **TERRY liveness: UNKNOWN.** TERRY is not in ListAgents at 20:4x ET, and Codex sessions are not enumerable from this runtime, so RED is not asserting it is dark and makes no spawn recommendation. This needs Will's decision under root rule #5 if he wants to act before 10/20.

## #3 — Did the fleet over-read CPI? (`AGENTS/RED/reports/2026-10-14_S52_CPI_read_check.md`)

**No outright over-read.** Every desk that wrote kept the headline/core split. Three framing gaps, one double-count and one blind spot:
1. **WALTER SIG-W-20261014-001 tags** (`pump_pass_through` + `CONSUMER_STAGFLATION` beside `RED-FT-08`) read "stagflation via pump" to any tag-only consumer. The body predates RED's NOT-MET grade. Packet sent to WALTER.
2. **NEXUS live STATUS** :50 (reads like oil→core), :85 (says RED's grade is uncommitted; it is committed), and :72 (counts real wages and headline CPI as two bear items; **they are one datum**, since real earnings are deflated by headline). Packet sent to NEXUS.
3. **For your next HEARTBEAT re-base (anti-laundering):** carry the caveat in substance: *"FT-08 fired: core is hot again; not via oil (airfares under the bar); 5y5y flat; long end rallied."*
4. **Blind spot:** falling real wages (−0.5% m/m) argue **against** a wage-price spiral, because wages are losing to prices. RED weights that 60/40 for "no spiral" as a counter to the Stag bucket at the next re-derivation.
5. **No certified post-CPI Fed odds exist.** BOND's futures proxy (~36% for a +25bp move on 10/28, uncertified) is the only number on file, and ORACLE last wrote on 10/9. Route ORACLE before a brief cites Fed odds.

## COMPLETION — RED — 2026-10-14 (addendum)
STATUS: ✅ DONE
CHANGED: AGENTS/RED/challenges/2026-10-14_BANK_PUT_BOOK_CHALLENGE.md (new), reports/2026-10-14_S52_CPI_read_check.md (new), workbook/{CHALLENGES,ML}.tsv, STATUS.md, SCRATCH.md, OUTBOX.md, NEXUS_BRIEF.md, docket/CATALYSTS.tsv; packets AGENTS/{TERRY,WALTER,NEXUS}/inbox/2026-10-14_from-RED_*.md; this memo
RESULT: Bank-put book challenged: OZK STRONG, WAL and KRE-Dec-60 MODERATE, KRE-Nov-67 WEAK. The decision point is before OZK's 10/20 after-close release. CPI read: no over-read; 3 framing gaps, one double-count, one anti-spiral blind spot; packets sent to the owners.
GAPS: Quotes from BOND, VIOLET, BRENT and WALTER :7 were relayed by an evidence agent and not re-checked by RED. Option quotes are indicative (after-hours). TERRY liveness UNKNOWN.
WILL_NEEDS: Whether to act on the OZK challenge before 10/20 (root rule #5; TERRY's card)
FOLLOW-UP: FT-10 official 10/14 bar; CARL CHG-049 by 10/19; re-derivation to include the anti-spiral counter.
