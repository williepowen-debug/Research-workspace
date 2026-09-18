# PLAN — three DOCKET registrations, PROME session prome-5d, 2026-09-18 ~17:5x ET

This is a PLAN read under WQ-178 and the two-correction stop. NOTHING BELOW IS ON DISK YET.
⛔ **SUPERSEDED IN PART — READ THIS BEFORE EXECUTING ANY CHANGE BELOW.** CHANGE 1's sentence *"What dies is the MAGNITUDE: a $0.47 crossing shown as $4.53"* was **REFUTED** by ❌1 of the companion cold-read ledger (`PROME/reports/2026-09-18_docket-plan-coldread-ledger.md`): $0.47 and $4.53 are DISTANCES BELOW the $100 line, nothing crossed, and neither is the day's move (−$2.38 / −2.34%). Four more ❌ follow it there. **Use the ledger's exact repairs, never this plan's original text.** Only CHANGE 1's 9/22 half was executed, as DOCKET L427; the L409 amendment, the L386 class-row clause and CHANGE 2 are CARRIED.

## Why a cold read is required at all
`PROME/DOCKET.tsv` took TWO correction commits this session (bc5f3141d — carrying AEOLUS's
unrounded-column caveat onto L426; 431f1f9b2 — correcting L426's framing after its owner
disputed it). Root canon two-correction stop: further edits to that file need an independent
cold read FIRST. This plan is the object of that read.

## Invariants that must hold for ALL THREE changes
I1. DOCKET citation convention (WQ-138): rows are cited by PHYSICAL LINE NUMBER. Never insert,
    delete or reorder. New rows APPEND AT EOF ONLY. File is currently 426 physical lines, so a
    new row becomes L427. Edits to an existing row change CELL CONTENT IN PLACE only.
I2. Exactly 6 tab-separated columns per row: date | headline | owner | state | source | notes.
I3. No literal tab or newline inside any cell.
I4. A date cell is either ISO `YYYY-MM-DD`, an ISO range `A..B`, or a session key
    (`next-<X>-session`). An UNDATED-BY-DESIGN row uses a session key, never a blank.
I5. Nothing here grades a gate, moves a threshold, proposes a trade, or moves capital.
I6. Every claim not established BY PROME carries its owner's name. Relaying is asserting.

---

## CHANGE 1 — amend L409 in place: name HAWK's third defect leg
**Current L409** (verified at the artifact this session):
  date  2026-09-24
  head  "FORGE MARKET-DATA VINTAGE + FALLBACK REPAIR (PROME-standard tools; WQ-229 consequential
         class — touches gate instruments): fetch.py::fred_fetch (≈:330-357) sends no realtime_*
         ⇒ returns LATEST-REVISED values, ARRIVAL-keyed on vintage, while GATE-HY-REKILL and
         GATE-TERRY-007 declare AS FIRST PUBLISHE…"
  owner "PROME (owns FORGE tools; writes acceptance conditions, repairs) / DAEDALUS (raised it,
         Wiring Sweep #2; independent reader candidate) / LIQUID · TERRY (gate owners…)"
  state "PENDING — registered 2026-09-17 10:1x ET from DAEDALUS packet ce9dc5f90 ask 5; NOT
         started (L407 + L404 first today) · INSTANCE 2026-09-17 21:4x ET …"

**Proposed:** APPEND to the `state` cell (in place, no reorder), text to the effect of:
  "· THIRD LEG REGISTERED 2026-09-18 17:5x ET — GENERIC-TICKER CONTRACT MISLABEL + CROSS-ROLL
  DAY-CHANGE, raised by HAWK (packet fa081e7d8 §3) and REPRODUCED LIVE BY PROME before
  registration, not relayed: CL=F printed $95.47 / −6.32% labelled 'Oct 2026 (CLV26)' while being
  BYTE-IDENTICAL to CLX26 (November) at the same volume 300,567; the real October CLV26 read
  $99.53 / −2.34%. BZ=F $98.77 / −5.77% = BZZ26 $98.77 / −1.16%, volume 43,844 identical. Two
  defects in one call: wrong contract attribution AND a day-change dividing the NEW month's price
  by the OLD month's prior close ($95.47/$101.91−1 = −6.32% against November's real −1.81%).
  DATED EXPOSURE ~2026-09-22 (October expiry), EARLIER than this row's own 9/24 date — after it
  CL=F becomes November. Stopgap only so far: a banner at the top of FORGE/tools/market-data/
  README.md (4ba52bdf5), which states it does NOT close this row. BRENT packeted (its
  MKT-CL-F-ABOVE-100 line is keyed literally on CL=F); PROME re-graded nothing.
  ⚠️ SCOPED BY ITS OWNER: HAWK first claimed the defect decided whether BRENT's >$100 line was
  crossed, then CHECKED and withdrew that — CLV26 $99.53 and CLX26 $95.47 are BOTH below $100, so
  the verdict is identical either way. What dies is the MAGNITUDE: a $0.47 crossing shown as
  $4.53. ⛔ Do not record 'the un-fire was an artifact' — nobody established that.
  n=3 UNCOORDINATED DESKS ON THIS CLASS IN ONE DAY (SAM's withdrawn −7.5% Brent roll artifact,
  HAWK's here, BRENT's own 9/22 flag) ⇒ [[finding_n_independent_deviations_is_a_sample_size_not_n_defects]]:
  measures the FIELD. WQ-229 prefer-an-existing-control: SAM's AGENTS/SAM/scripts/oil_roll_check.py
  (512ac5a1c, boot-wired) is the PROMOTABLE control and the repair candidate, NOT a fourth
  hand-written guard."

**Why amend rather than open a new row:** same file, same owner, same WQ-229 consequential class,
same repair session. A separate row would split one repair across two dates.

---

## CHANGE 2 — NEW row at EOF (L427): BOND's dated publication cutoff
Raised by CATO (brief 2026-09-18_1410, item A3) and NOT registered anywhere — verified this
session: no DOCKET row carries it, and BOND has made no commit since before the brief was written.

  date   2026-09-30
  head   "🔴 BOND — RESPECT THE 2026-09-30 17:00 ET PUBLICATION CUTOFF BEFORE FINALIZING ANY
          UNRESOLVED BND-26 OUTCOME. Registered because the obligation existed ONLY inside CATO's
          review file, which no owner reads, and BOND has been DARK all day."
  owner  "BOND (owner of BND-25/BND-26 and of the grade) / PROME (registration + routing only —
          PROME grades nothing here) / CATO (raised it)"
  state  "PENDING — registered 2026-09-18 17:5x ET by PROME from CATO's action brief A3
          (AGENTS/CATO/runs/2026-09-18_1410_prome-updated-action-brief.md). ⚠️ NOT DELIVERED TO
          BOND: CATO states it sent no packet and claims no acknowledgment — 'prepared for Will to
          share'. PROME verified every fleet inbox: the only CATO finding ever routed to an owner
          is the 9/17 LIQUID one. A3 has no carrier, which is what this row fixes."
  source "AGENTS/CATO/runs/2026-09-18_1410_prome-updated-action-brief.md A3 + the detailed brief
          2026-09-18_1102_prome-action-brief.md (exact surfaces + acceptance cases)"
  notes  "⚠️ THE FINDING IS CATO'S, NOT PROME'S — PROME has NOT inspected BND-26's evidence, the
          H.15 cells, or the grading branches, and asserts nothing about the grade. Acceptance
          condition is CATO's: preserve the registered observation window and grading branches;
          do not finalize an unresolved outcome ahead of the cutoff. ⛔ This row registers a DATE
          and an OWNER. It does not grade, re-date, or pre-judge BND-26, and it is NOT authority
          to edit BOND's files. Companion CATO items at the same dark desk, NOT registered here
          because they carry no date: A2 (separate all I-prime fires from the 68% subgroup before
          publishing an implied 23/52 = 44.2%) and A4 (establish first-publication evidence or
          withhold the certification)."

---

## CHANGE 3 — amend L425 in place: HAWK's owed promotion flag
**Current L425** is the undated auto-memory promotion row registered 2026-09-18 16:3x ET
(date cell `next-PROME-flow-pass`), opened because HENRY and VIOLET both flagged a promotion
candidate and neither wrote it.

**Proposed:** APPEND to the `state` or `notes` cell, in place:
  "· SECOND CANDIDATE, SAME FLOW PASS, 2026-09-18 17:5x ET: HAWK extended the COLD-tier
  [[finding_continuous_front_ticker_rolls_so_deltas_lie]] with a FOURTH facet (a0d16be99, that
  memory FILE only — PROME verified MEMORY.md untouched; carve-out ③ correct). Per the
  auto-memory index header's Promotion rule (Will-approved 2026-08-21), extending a COLD row
  OBLIGATES a promotion flag to PROME carrying n=. n = 4 facets on the file, 3 uncoordinated
  desks in one day. HAWK did NOT self-promote and explicitly left execute-or-decline to PROME's
  flow pass. ⚠️ The flow rule does NOT fire on its own: MEMORY.md measured 71% of cap at this
  session's boot gate, below the ≥75% demotion trigger — so this is a PROMOTION judgment, not a
  forced compaction. Facet 4's claim to distinctness, in HAWK's words and not PROME's: facets
  1–3 describe the DATA disagreeing with itself while the reader identifies the contract; facet 4
  has the TOOL asserting the identity in a confident annotation that is false, so it defeats the
  file's own facet-2 detector by looking like that detector already ran."

---

## What the cold reader is asked to find
Not style. Specifically:
(a) Any invariant I1–I6 broken by any of the three changes.
(b) Any claim stated as PROME's that is actually CATO's, HAWK's, SAM's or BRENT's.
(c) Any place a MAGNITUDE finding is written as a VERDICT finding (the exact error HAWK made and
    withdrew) — or the reverse, a real verdict softened into a magnitude.
(d) Whether CHANGE 1 belongs on L409 at all, or whether folding a ~9/22 exposure into a row dated
    9/24 hides the earlier date.
(e) Whether CHANGE 2's "no carrier" claim is supportable from what is stated, or overreaches.
(f) Anything that would read as authority to edit another desk's files or grade another desk's gate.
