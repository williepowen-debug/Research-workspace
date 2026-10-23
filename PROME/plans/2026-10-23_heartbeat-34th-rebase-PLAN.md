# HEARTBEAT thirty-fourth base — plan, inputs ledger and read record

**Owner:** PROME · **Opened:** 2026-10-23 11:4x ET (session prome-03 fresh context, DESKTOP) · **Status:** DRAFT — inputs collected before the close; the candidate is written AFTER the 16:00 ET close and gets its plan read then. Domain refresh under standing HEARTBEAT ownership, not a process change. Prior plan: `2026-10-19_heartbeat-33rd-rebase-PLAN.md` (its operation, invariants and read budget carry over unchanged).

## Why a new base
The 33rd base (Mon 10/19) carries three amendments (chain at 3; the boot gate flags a 4th). Its one-liner, § Stress dashboard and § Book state are dated 10/15–10/19 and are now superseded in every channel by the amendments; a reader must traverse three dated blocks to reach today. Measured size at this boot: `measure.py` reads 23,727 B (under the 32,550 B cap, under the 75% rotate line), so size is not the trigger — the amendment-chain rule is.

## Operation (unchanged from the 33rd plan)
Snapshot the whole live `HEARTBEAT.md` verbatim to `PROME/archive/HEARTBEAT_PREREBASE_SNAPSHOT_2026-10-23.md` with a `measure.py` crc; verify the archived body byte-for-byte; install the reviewed candidate from `PROME/reports/2026-10-23_heartbeat-rebase/HEARTBEAT_candidate.md`, preserving the opening Brent dashboard parser anchor. No cold file or rule changes. Levels come from ONE post-close dashboard pull (BOOT.md step 5, ruling 2026-10-16 A3) beside the candidate; owner grades at their own commits; the book sentence pasted whole from `will_brief.py --book-line`.

## Inputs ledger (collected 11:2x–11:5x ET; each item names its source and date; nothing here is a grade PROME made)
| Channel | Input | Source / date | Owner grade state |
|---|---|---|---|
| Credit | HY OAS 340 bp (+13) · CCC 1,340 bp (+33), the 10/22 cell published 10/23 | dashboard 11:26 ET pull (FRED) | LIQUID: >320 run was VERIFIED 6 at its 10/22 grade (c121a9eec); the 10/22 cell makes a 7th ONLY when LIQUID grades it — not yet graded |
| Credit | REG-T-04 (REGINALD): HY >350 for 3 consecutive closes ⇒ issuance-freeze chain (REGINALD / LIQUID / Will). 340 is 10 bp under the line | WALTER SIG-W-20261023-015 (14:29Z) · REGINALD STATUS row 111 (23 bp away at its 10/21 cell) | REGINALD's desk letter, not a PROME action-gate; no fire |
| Credit | HY new-issue market shutting: ~$7B October to 10/21 vs ~$51B September; >$5B of deals delayed (Bloomberg via syndicated copy) | WALTER SIG-W-20261023-016 (14:35Z) → REGINALD, LIQUID | ungraded |
| Credit | Is the widening AI-concentrated or broad? REQ-DEWEY-20261023-002 (Will-directed 11:12 ET in WALTER's window; deliver by Mon 10/26) | WALTER packet 10923410a | DEWEY live now (dewey-08); answer owed by 10/26 |
| Banks | FLG Q3 miss: adj. EPS $0.01 (incl. $22M tax benefit), pre-tax −$10M; FY26 provision guide $90–140M → $160–170M; FY27 EPS $1.60–1.70 → $0.85–0.95; NAL $2,817M; buyback ~$216M, CET1 13.16% → 12.38%. Frame items A/B/D fire; R1/R3/R4/R5 surprise lines fire | FLG memo 550757f53 (PROME/inbox/processed/2026-10-23_from-FLG_L522-q3-print-grade.md); full grade `AGENTS/FLG/reports/2026-10-23_Q3-2026_PRINT_GRADE.md` | FLG graded; L522 print leg closed; 10-Q leg ~11/9 |
| Banks | AXP Q3: deposit cost fell (derived ~3.16% vs 3.25%), NII $4,940M (+6.3% QoQ), OCC $350M BSA/AML penalty (enforcement, not credit). Q3 perimeter census CLOSED 64/64 | GIBBS `AGENTS/GIBBS/research/2026-10-23_axp-q3-print.md` (e6188194c) | GIBBS; no thresholds (WQ-426) |
| Macro | US flash PMI Oct: mfg 56.0 (53-month high) but production/new orders slowed; selling prices fastest since Aug 2022; services 57.9 | WALTER SIG-W-20261023-010 (13:48Z) → CARL ACTION | CARL grades |
| Europe | France flash PMI 48.4; OAT 5.13 / Bund 3.38 / spread 174.6 bp [i-i close 10/22], T-10 OPEN AND DEEPENING; Moody's France review TONIGHT (Fri 10/23) | WALTER SIG-W-20261023-011 · HANS STATUS 10/22 ~20:45 ET (ff21bfa01) | HANS; Moody's outcome = HANS wake only if the rating moved (SCRATCH) |
| Energy | Brent Dec `BZZ26` $116.13 (+2.96) at 11:26 ET — vendor intraday, NOT a settle; BRENT's COT #11 (as-of 10/20) posts ~15:30 ET → GATE-BRENT-COT-35B grade | dashboard 11:26 ET · GATES row 12 · BRENT STATUS | BRENT grades (its routine graded #10 same evening at 20:17Z); PROME consumer read after |
| Tape (intraday, 11:26 ET, re-pull after the close) | KRE 72.71 · OZK 50.42 · WAL 76.71 · APO 113.90 · TLT 81.52 · VIX 19.34 · MOVE 104.39 · USD/JPY 156.78 · 10Y 5.13 [10/21 cell] · SOFR 3.90 [10/22] | dashboard 11:26 ET | — |
| Fleet | ISHM (industrials) desk built + registered 10/23 (WQ-506/507; ROSTER TIER-2 7); first P1 10/27 durables, ISM 11/02 | PROME 10923410a-era commits; SCRATCH ★ NEXT | Will launches its first session |
| Book | `will_brief.py --book-line` at boot: Book $39,876.06 · cash 39.64% · broker export received 2026-10-22 · marks as-of 2026-10-22 intraday · 1d since receipt — not live | FORGE ec5a7058b | re-run at the candidate |

## After the close (the write)
1. ONE dashboard pull (cite its time) + `fetch.py price` only for names it does not carry; Brent settle from BRENT's record if posted, else the vendor bar labelled next-session.
2. BRENT COT #11 consumer read at `AGENTS/BRENT/workbook/COT_VINTAGES.tsv` / Friday grade file; GATES row 12 state cell updated only from BRENT's grade.
3. VULCAN L804 wake (after 16:00 ET; ListAgents first; Tier 1) — its mag7 slot 7 / GPU panel 7 / S2 results land as pointers if they return before the candidate is cut, otherwise at the next amendment.
4. Candidate: one-liner · eight channel leads · § Book state (book line verbatim) · § Stress dashboard (post-close levels) · § Thresholds (closest live lines: REG-T-04 10 bp away at the 10/22 cell, LIQ-076 MET 2-of-3 W2, HY-REKILL 0/2, COT-35B #11, FALCON-001 review 10/28) · Kill-on-sight carried from am.#1–#3 plus new: "HY 340 is LIQUID's 7th" (ungraded until LIQUID says so); "REG-T-04 fired" (it needs 3 closes >350); "the issuance freeze is on" (volume leads price; the trigger is the price line); "Moody's moved France" (unknown until the release); "Brent $116 is a settle".
5. Plan read on the candidate (ONE, Sonnet per WQ-447 reader class), fix ❌ only, declare residue here; install; result read (ONE); record both here. Review budget: `PROME/CLAUDE.md` § Review budget.

## Invariants (the 33rd plan's seven, re-stated by number only)
1 date classes distinguishable · 2 no PROME-made bar count · 3 no invented disposition, book line verbatim · 4 no threshold/consequent/grade moved · 5 pointers resolve · 6 bytes retained, under the 70% stop · 7 the opening is inference from dated evidence, not a new score. Plus, this base: **no expiry language on any held line** (`USER.md` § No expiry nagging).

## Reads and residue
Reads: 0 performed. Budget: one plan read, one result read. Nothing installed; no review-completion claim.
