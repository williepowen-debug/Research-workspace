# WILL_QUEUE open rows — plain first sentence + two Type relabels — PLAN

**Owner:** PROME (prome-34) · **Written:** 2026-10-30 21:46 ET · **Authority:** Will 21:45 ET in PROME's chat, verbatim *"Ok cato is working you do your part?"* — to PROME's 21:4x ET message naming suggestions 1 and 2 as PROME's part (ideas list rows of 21:4x ET). **Why:** CATO's Decisions desk uses each open row's Item cell as the card headline (cut at 180 characters); today those cells run 390–1,152 characters written for agents, and two of Will's own time-bound tasks are typed so the desk files them under "Follow-through". **Review:** WILL_QUEUE is past the two-correction stop this session ⇒ independent plan read here, then ONE scripted edit, then a result read. Process change 4 of 5 (harness session prome-34).

## Edit 1 — prepend ONE plain sentence to the Item cell of each of the ten OPEN rows
Form: `**<sentence>** ` inserted at the very start of the Item cell (bold, then one space), the existing cell text kept byte for byte after it. Each sentence ≤120 characters, says what Will does and by when, in plain words.

| Row | Sentence to prepend |
|---|---|
| 559 | Decide which day FALCON runs the dated check on its prediction FAL-07: Thu Dec 31 (recommended) or Sat Jan 2, 2027. |
| 556 | Decide whether WALTER cuts the flood of FYI news copies to desks that rarely use them (recommended A). |
| 548 | Your hands: post one Fidelity Activity screenshot covering 10/22–10/29 so last week's trades can be booked. |
| 547 | Your hands: look up three Florida condo-association bankruptcy dockets (one free, two on PACER, under $5). |
| 531 | Your hands: make a free CourtListener account and token so the desks' court-record searches work again. |
| 495 | Your hands by Thu 11/5: renew the FFIEC bank-data login (recorded as the same renewal as WQ-31's item ①). |
| 477 | Your hands, about 5 minutes: capture two entries from FLG's New York rent-freeze court case (no login, no cost). |
| 463 | Your hands, about 2 minutes: check the Florida condo-records portal for CORAL's request; any fee needs your OK. |
| 422 | Your hands: share any access you already have to Clear Spring Life's insurer financial statements for SHADE. |
| 31 | Your hands, one sitting around Sun 11/1: renew three credentials before the FFIEC bank-data token expires Thu 11/5. |

## Edit 2 — Type relabels (Type cell only)
- **WQ-31:** `ACTION` → `HANDS`. Its open content is a Will credential sitting (his hands). Because WQ-538 A parks HANDS rows in boot reports unless a re-present marker is due, prepend `⏰ re-present 2026-11-01 · ` to its Notes cell so the Sunday sitting still surfaces.
- **WQ-495:** `MIXED` → `HANDS`. Its Rec cell records that 495.NPORT was ruled A 2026-10-30 11:10 ET and the row stays OPEN "for 495.CDR only (your hands, 11/5)". Prepend `⏰ re-present 2026-11-03 · ` to its Notes cell (two days before the 11/5 need).
- Nothing else changes: no Needed-by, Since, Rec text, ruling, number or order.

## Invariants and pass criterion
- Row count and order of OPEN unchanged; each changed row still has 7 cells; `table_check.py` clean; `willq_view.py --check` clean after `--write`; `wq_ledger.py sync` then `check` clean.
- Each changed line, with the prepended text removed, equals its original except the two Type cells and two Notes prefixes listed.
- `claim_check.py --check weekday,glued PROME/WILL_QUEUE.md` adds no new flag.
- Rendered check: CATO's desk built read-only on a scratch database shows each card's headline starting with the new sentence, and WQ-31 and WQ-495 under "Tasks for me".
- The "Notes begins with ⛔ waits" blocked-row rule is not triggered by the ⏰ prefix (neither row is a waits row).

## Read log
- Plan read: PENDING.
