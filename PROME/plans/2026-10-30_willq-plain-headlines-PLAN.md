# WILL_QUEUE open rows — plain first sentence + two Type relabels — PLAN

**Owner:** PROME (prome-34) · **Written:** 2026-10-30 21:46 ET · **Authority:** Will 21:45 ET in PROME's chat, verbatim *"Ok cato is working you do your part?"* — to PROME's 21:4x ET message naming suggestions 1 and 2 as PROME's part (ideas list rows of 21:4x ET). **Why:** CATO's Decisions desk uses each open row's Item cell as the card headline (cut at 180 characters); today those cells run 390–1,152 characters written for agents, and two of Will's own time-bound tasks are typed so the desk files them under "Follow-through". **Review:** WILL_QUEUE is past the two-correction stop this session ⇒ independent plan read here, then ONE scripted edit, then a result read. Process change 4 of 5 (harness session prome-34).

## Edit 1 — prepend ONE plain sentence to the Item cell of each of the ten OPEN rows
Form: `**<sentence>** ` inserted at the very start of the Item cell (bold, then one space), the existing cell text kept byte for byte after it. Each sentence ≤120 characters, says what Will does and by when, in plain words.

| Row | Sentence to prepend |
|---|---|
| 559 | Decide which day FALCON runs the dated check on its prediction FAL-07: Thu Dec 31 (recommended) or Sat Jan 2, 2027. |
| 556 | Decide whether WALTER sends quiet desks one dated news digest instead of a copy per item (recommended A). |
| 548 | Your hands: post one Fidelity Activity screenshot covering 10/22–10/29 so last week's trades can be booked. |
| 547 | Your hands: look up three bankruptcy dockets for CORAL (two Florida condo cases on PACER, one free), under $5. |
| 531 | Your hands: make a free CourtListener account and token so the desks' court-record searches work again. |
| 495 | Your hands by Thu 11/5: renew the FFIEC Call Report login (probably the same renewal as WQ-31's item ①). |
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
- **Plan read** 21:4x ET (blind Sonnet coldreader; ledger `willq-headlines-plan-read.md` in PROME's session scratchpad): **PROCEED WITH FIXES — 3 ❌ · 7 ⚠️.** **❌ fixed in the table above (before any edit):** 547 — the free docket is Brightline (FIHPNP LLC, Bankr. D.N.J.), not a Florida condo association; 556 — lever (a) is ALREADY in force, the ask is (b) one dated digest per quiet (dark ≥7 days) desk, with (c) case by case; 495 — no repo record links the 495.CDR login to WQ-31 item ① (DOCKET L180 ties the FFIEC CDR JWT to row 31, but no record names 495), so "recorded as" became "probably". **Declared residue (⚠️):** the 559 headline names only the date question, while the row carries two more points on the letter (the headline leads into the full row, which keeps them) · the WQ-31 marker puts the sitting on Sun 11/1 though DOCKET L219 asked it be raised from ~mid-October; the first boot after may be Mon 11/2 — the 11/1 DOCKET row also surfaces it · nothing yet says that doing WQ-31's sitting closes 495.CDR; PROME checks that at Will's report of the sitting, before the 11/3 marker re-asks · the scripted edit must not pass the sentences through an unquoted shell heredoc (the $5) — the edit reads them from this file in Python · the pass criterion gains: each prepended sentence is byte-identical to this table, and the result read re-checks each sentence against its row.
- **Executed** 21:5x ET, commit 23ea80693: sentences read from the table above in Python (no shell quoting); 10 rows changed; reversal proof 0 residual differences; table_check, wq_ledger, willq_view, claim_check clean; CATO's desk rendered read-only: 11 cards, no errors, every headline led by its sentence, WQ-31 and WQ-495 under "Tasks for me" (8 tasks, 2 decisions, 1 history).
- **Result read** 21:51 ET (blind Sonnet coldreader; ledger `willq-headlines-result-read.md`): **ACCEPT WITH RESIDUE — 0 ❌ · 5 ⚠️.** Byte match on all ten; exact reversal; commit scope queue + ledger only; every sentence true against its full row; tools clean. **Declared residue (not edited — WILL_QUEUE is past this session's correction stop):** ⚠️A 547 "two Florida condo cases on PACER, one free" can read as one of the two condo cases being free (the free one is the third, Brightline) · ⚠️B 477 "capture two entries" overstates — the row asks for doc 244 plus any entry after doc 253, which may be none · ⚠️C some jargon remains (FAL-07, Call Report, item ①, token) · ⚠️D this read log said PENDING — recorded here · ⚠️E the WQ-31 Sunday marker may first surface at a Monday boot (declared at the plan read). Fix A and B at the next PROME pass over the queue.
