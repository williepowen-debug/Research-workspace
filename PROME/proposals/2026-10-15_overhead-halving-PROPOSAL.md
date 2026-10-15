# PROPOSAL — halve PROME's operational overhead without raising consequential-error risk (for the 2026-10-25 WQ-299 review)

**Written:** 2026-10-15 18:39 ET (PROME prome-06), in answer to Will's question after the post-close sitting ("Did we make much progress?") and an outside reviewer's follow-up he relayed: *"Of the verification and administrative procedures you performed today, which ones would you eliminate, simplify, or move into deterministic software if you had to cut your operational overhead in half — without increasing the likelihood of consequential errors?"* Status: PROPOSAL — nothing here is implemented; each item is a process change and goes through the ceiling and Will's word. Evidence base: this sitting's record `PROME/reports/2026-10-15_postclose-standard-closeout.md`, ORCH_LOG rows of 2026-10-15, the three L688 reader ledgers, the two HEARTBEAT read ledgers, ARGUS run 1. Companion measurement: DOCKET L739 (RED's two-week apparatus-vs-domain test, check 2026-10-29).

## The sitting's accounting (PROME's estimate, not an instrument; ~105 min from boot 16:19 to the closeout push)
| Lane | Minutes (est.) | What |
|---|---|---|
| Domain | ~25 | BROCK wake + consumption · three packets · HEARTBEAT content (closes, grades) |
| Verification | ~45 | three L688 reads + two fix passes · two HEARTBEAT reads + fixes · ARGUS run + 8 fixes |
| Administration | ~35 | boot reads to EOF (incl. a 114 KB hash log) · ledger rows and receipts by hand · five surfaces written with the same facts · six trim passes · the Deck page read for a no-op |

## Ranked cuts (saving first; each with the control that stays)
| # | Change | Class | Saves (est., per occurrence) | What stays |
|---|---|---|---|---|
| 1 | **Reader stop rule by historical occurrence.** A reader's ❌ forces a fix + another read ONLY if the failing shape occurs in the artifact's real history (e.g. the 60 FORGE headers) or in the writer's documented convention; a shape that has never occurred is declared residue and spawns no read. | rule (PROME/CLAUDE.md § Review budget — Will's word) | 2 Opus reads + ~25 min on L688 tonight (reads 2 and 3 found only 0-of-60 shapes) | the first independent read on any Will-facing change; the author's fixtures for every shape a reader names |
| 2 | **One home for session facts.** The closeout record + the day log hold the account; HANDOFF = one line pointing at the record; SCRATCH = the resume pointer and the operator card only; STATUS = state, never narrative. | rule (CLOSEOUT.md symmetry table) | ~40% of closeout writing; most of ARGUS's "two live versions" class (6 of tonight's 8 ❌) | the record, the day log, the audit |
| 3 | **Receipt writer for ORCH_LOG + a READ_ONLY_TERMINAL state.** `orch_log.py receipt --key … --ask … --receipt …` writes the closeout_v1 object (today: seven hand edits of the TSV); a helper spawned without a message tool gets READ_ONLY_TERMINAL at spawn, no ask/receipt bookkeeping. | tool (DAEDALUS writer; step-4 class of the wiring plan) | ~10 hand edits per closeout; the WQ-249 "dark before the ask" ritual for coldreaders/ARGUS | the ask + receipt for every desk and every helper that CAN answer |
| 4 | **Gate logs summarised.** The WQ-249 check prints the four state counts + the named UNKNOWN keys; the full log is on demand, not a boot read to EOF. | manual (BOOT.md step 5) | ~15 bounded-read calls per boot (114 KB of hashes tonight) | the gate's verdict and every named UNKNOWN |
| 5 | **Decide the Deck republish before reading the page** (the WQ-446 encode, DOCKET L738): hash the owed set first; read the hosted page only when a republish is owed. | tool (already ruled; L738) | ~100 KB of context per closeout | the read-before-republish rule when a republish happens |
| 6 | **Section-size instrument for the re-base** (`measure.py --sections HEARTBEAT.md` against a per-section target). | tool | ~5 trim passes (~15 min) per re-base | the 70% stop and the two blind reads |
| 7 | **Firetime allowlist cleanup** — renew or retire the expired rows behind the 49 carried flags. | hygiene (one-time) | one advisory re-triaged every boot | the fire-time check |

## Not cut, and why
The gate's blocking checks (cheap, deterministic, they stop real failures) · the FIRST independent read on anything Will sees (read 1 of L688 found two real misses) · the plan + result reads on a HEARTBEAT re-base (the plan read caught TERRY's crack ESTIMATE restated as a settlement — the class the hot file's own kill-on-sight names) · the ARGUS audit (kept honest records tonight; item 2 shrinks what it must audit) · the desk-spawn preflight (one command).

## The reviewer's two cautions, accepted
Sonnet for cold reads (WQ-447 A, encoded tonight) lowers the price of a check, not the number of checks — item 1 is what lowers the number. Six trim passes were reasoning spent on arithmetic — item 6.

## Test
RED's L739 (2026-10-29) already measures apparatus minutes vs domain minutes per desk, two weeks before vs after 2026-10-15; PROME reports its own split from the closeout records. Friday 10/16 (six catalyst wakes, no process work owed) is the first comparison sitting.
