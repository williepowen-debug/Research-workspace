# The week ahead, sequenced — Mon 9/28 → Fri 10/02 (Will 2026-09-26 15:54: *"Sequence the existing October 1–2 obligations by deadline, position exposure and dependencies, combining genuinely overlapping wakes. Don't add routine cadence work to those days."*)
**Written 2026-09-26 15:59 ET (`prome-1d`) from `spawn_list.py --horizon 7` (dated DOCKET/GATES rows, owners, last self-commits) and the queue. Ordering keys, in priority order: (1) a HARD DEADLINE that cannot be re-run, (2) POSITION EXPOSURE (a live line the row can change), (3) DEPENDENCIES (a row another row consumes). Overlapping wakes for one desk are ONE session. WQ-295 R2 stays HELD: no cadence-only wake is added to any day below; the 10/01–10/02 cadence clocks (HOMER · MARCO · REGINALD · SAM · HANS · ORACLE · VIOLET · WATT) roll to the first later boot with cap room.**

## Mon 9/28
| # | Wake | Why here | Combines |
|---|---|---|---|
| 1 | **LIQUID ~16:15 ET** (L492 HY 9/25 cell → RED-FT-01 day 2; L510 the ISDA-benchmark validation for WQ-301 (b); GATE-HY-REKILL / LIQ-072 / LIQ-076 reviews due 9/30 taken in the same session) | position exposure: the HY line is the book's credit tell; a Will decision (301 b) waits on the validation | one LIQUID session, four rows |
| 2 | **OTTO** (L469 full-session wake, any boot) | dated wake owed since 9/24; no dependency | — |
| 3 | Will's hands (from the report): the Fidelity question (WQ-302), the NYSCEF search (WQ-279, before 10/01), the Vortexa form (WQ-296; Kpler was sent by email 9/26 16:00) | deadlines 10/01 and the cards' 10/14 clock | — |
| — | ORACLE v4 October roll (L299) is WILL-owned — re-presented, not spawned | | |

## Tue 9/29
| # | Wake | Why here | Combines |
|---|---|---|---|
| 1 | **HENRY** (L489 blind verdict on BRT-12; L385 roll-mismatch October window due 9/30; L475 FORUM-7 verdict prep for 10/01) | dependency: BRENT's BRT-12 rule waits on the verdict; L385 touches the TLT put's roll hazard (position) | one HENRY session, three rows |
| 2 | **CRUISE** (L221 CCL Q3 print ~9/28–29; L502 the ratio-form successor letter; CRU-09 grades by 10/03) | hard print date; L502 is owner work Will's WQ-242 waits on | one CRUISE session |
| 3 | FALCON GATE-FALCON-001 review (9/29) | judgement review with a date; FALCON last self-commit 9/22 | — |

## Wed 9/30 — the expiry day
| # | Wake | Why here | Combines |
|---|---|---|---|
| 1 | **TERRY** (L74 / L255 the 004 TLT Sep-30 $77P ×20 expiry; WQ-302 cards' Fidelity answer if Will has it) | position exposure: a live expiry; nothing else can move the book today | one TERRY session |
| 2 | **HAWK** (L491 HAW-19 DEFECTIVE encode; HAW-22 first window opens 10/01) | hard date on the ledger | one HAWK session |
| 3 | **BOND** — NOT today: its 10/01 print session below carries L410 + L478 + the WQ-291 grade + WQ-246 encode | avoid a second BOND wake 24h before the print | — |
| 4 | ZHAO (L481 ZHA-16 grade at window close) · MIDAS (L231 resolve) · VULCAN (L114 MU tripwire) · AEOLUS (L426 C5 re-scope, past cadence) · SHADE (L182, past cadence 29d) · CORAL (GATE-CORAL-MSI-01 review; L501 the re-fire letter — one session on 10/02 instead, see below) · FERT (GATE-FERT-G5 review + WQ-257 encode; L288 on 10/02 → ONE FERT session 10/02) · WALTER L334 (Will-launched) | dated graded rows, no position exposure; the cap of four takes TERRY · HAWK · ZHAO · MIDAS first, the rest slate to Will's word or roll to 10/01 | ZHAO, MIDAS, VULCAN, AEOLUS, SHADE each one session |

## Thu 10/01 — the print day (FR2004 ~16:15 ET)
| # | Wake | Why here | Combines |
|---|---|---|---|
| 1 | **BOND, evening after the print** (L478 grade the 9/23 5Y under the WQ-291 rule · L410 quarterly refresh with the WQ-246 count encode + the I′-extends-to-TIPS and degenerate-row items · FORUM-7 D3 · ZHAO's H.4.1 week-9/30 read) | hard print time; position exposure: a fired kill is a recommendation to exit all duration shorts (TLT 82P ×2 sit under it); dependency: HENRY's L475 verdict and CARL/ZHAO consume it | ONE BOND session, four rows |
| 2 | **FLG** (GATE-FLG-T08 fires 10/01 — NYC rent freeze effective; L236; Will's NYSCEF input if he ran it) | a gate FIRES today; PROME spawns FLG per the row | one FLG session |
| 3 | **HENRY** (L475 FORUM-7 verdict by the 10/02 boot — if not done Tue) | dependency for BOND #1 | rides Tue's session if done then |
| 4 | **BROCK** (L479 CRMT bridge-4 STD 10/01 · L494 X1 wrapper-half re-adjudication 10/02 · L480 backstop 10/07 watch) | dated corporate event + the X1 sitting: ONE session covers both days' rows | one BROCK session, Thu evening or Fri |
| 5 | CARL (L152 SAVE→RAP tranche read; WQ-287 encode) · RED (L484 CH-009 final grade) · OZK (L126 sub-notes reprice; L463 its 10/02 read → one OZK session Fri) · DEWEY (L468 CARL-DR-3 commission) | dated, no position exposure; beyond the cap → slate | CARL one session; RED one; DEWEY one |

## Fri 10/02 — NFP + the owed sets
| # | Wake | Why here | Combines |
|---|---|---|---|
| 1 | **LABOR ~08:30 ET** (L287 September NFP) | hard print; feeds the rates desks the same day | one LABOR session |
| 2 | **BRENT** (GATE-BRENT-COT-35B #8 review; the 10/04 OPEC+ prep L297) | instrument review with a date; COT prints Fri | one BRENT session |
| 3 | **DAEDALUS** (L490 owed set · L495 receiver-side canary · L496 unattended-instrument register · WQ-295 R4 SL-6 encode · L457 residue · the WQ-255 registries) | owed set with six consumers; no position exposure; DAEDALUS cadence WEEKLY declared | ONE DAEDALUS session, six rows |
| 4 | **PROME** (L503 root-doc sitting with spine audit #15 · L210 FORUM-6 legs (a)/(c) with DAEDALUS · L487 dark-desk gap · L500 retire the Carnival phrase · the paid-data pass is RULED) | PROME's own, sequenced after the desk wakes | the spine-audit sitting |
| 5 | CORAL (L501 re-fire letter + the 9/30 MSI review, past cadence 13d) · FERT (L288 Pink Sheet + G5 + WQ-257) · OZK (L463) · YURI (L434 Nestlé/Auchan; YUR-004 registration if not done) · CRUISE (L502 if not done Tue) | dated, no position exposure; beyond the cap → slate | one session each |

## The cap, honestly
Dated wakes alone exceed four on 9/30 (TERRY · HAWK · ZHAO · MIDAS + 5 more), 10/01 (BOND · FLG · BROCK · CARL + 3 more) and 10/02 (LABOR · BRENT · DAEDALUS · CORAL + 3 more). The order above is the priority within each day; rows past the fourth are SLATED in that day's boot report for Will's word, and roll to the next boot otherwise. No cadence-only wake is scheduled on any of these days.

## Position exposure, named
- 9/30: the 004 TLT $77P ×20 expiry (TERRY). 10/01: the WQ-291 kill leg graded on the print — a fired kill is a RECOMMENDATION through TERRY's card and Will's [Approve], never an execution; the TLT Oct-16 $82P ×2 (WQ-302) sit under it. 10/02: NFP moves the rates lines the same morning; nothing on the book is keyed to it directly.
