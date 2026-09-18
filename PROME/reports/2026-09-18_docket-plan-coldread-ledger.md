# COLDREADER · DOCKET_plan.md · 8,696 B · 41 claims · PLAN read, 2026-09-18

SCORE: 28/41 ✅ · 8 ⚠️ · 5 ❌
Read-only. Verified with `wc`/`awk`/`sed`/`grep`/`git show`. No repo write. No market call made (not needed — every price claim was checkable against three committed artifacts).

---

## ❌ BLOCKING — five

### ❌1 · A MAGNITUDE IS WRITTEN WITH A VERDICT NOUN — the exact error the plan says it is guarding against
**Plan L50:** *"What dies is the MAGNITUDE: a $0.47 crossing shown as $4.53."*
**Plan L49, the sentence immediately before it:** *"CLV26 $99.53 and CLX26 $95.47 are BOTH below $100, so the verdict is identical either way."*

Nothing crossed. `$0.47` and `$4.53` are **distances below the $100 line** ($100 − $99.53; $100 − $95.47). "Crossing" names the verdict event that the previous clause denies. And on the other available reading — that these are the day's *move* — both numbers are simply wrong: October moved $101.91 → $99.53 = **$2.38 / −2.34%**, and `CL=F` showed **$6.44 / −6.32%**; neither is $0.47 or $4.53.

HAWK's own committed text keeps the number and drops the noun — `a0d16be99` commit body: *"It destroys the MAGNITUDE ($0.47 shown as $4.53). **A defect that moves a DISTANCE is not automatically one that moves a VERDICT**; claiming otherwise is over-reach in the opposite direction."*

⚠️ This phrasing is **already propagating**: `memory/auto/finding_continuous_front_ticker_rolls_so_deltas_lie.md` (*"a $0.47 crossing displayed as $4.53"*) and `AGENTS/BRENT/inbox/2026-09-18_from-PROME_…md` (*"a **$0.47** crossing, not the **$4.53** collapse"*). The DOCKET would be the fourth surface and the canonical one.
**Repair (exact):** `"What dies is the MAGNITUDE: on the honest October contract WTI sits $0.47 under the $100 line ($99.53); CL=F shows it $4.53 under ($95.47). Neither is a crossing, and the day's real October move was −2.34%, not −6.32%."`

### ❌2 · CHANGE 1 BURIES A ~9/22 HAZARD IN A ROW DATED 9/24 THAT DOES NOT NAME ITS OWNER
**Plan L44 admits it:** *"DATED EXPOSURE ~2026-09-22 (October expiry), EARLIER than this row's own 9/24 date."* The plan then does nothing about it.

Three things make this blocking, not cosmetic:
1. **The date cell is the enforcement.** `PROME/DOCKET.tsv` L2: *"the boot-time overdue check is the enforcement; no new machinery."* Auto-injected `PROME/CLAUDE.md` WQ-184: PROME spawns the owner *"at the first boot on/after the date."* A 9/22 hazard on a 9/24 row wakes nobody until two days after the contract expires.
2. **L409's owners cell does not contain BRENT.** Verified verbatim: `PROME (owns FORGE tools…) / DAEDALUS (raised it…) / LIQUID · TERRY (gate owners…)`. The 9/22 decision is **BRENT's** — HAWK's ASK: *"decide whether BRENT's `MKT-CL-F-ABOVE-100` needs its contract basis pinned before Oct expiry ~9/22."* Anyone scanning owners for who is on the hook by 9/22 finds PROME, DAEDALUS, LIQUID and TERRY, and not BRENT.
3. **The file carries the opposite precedent, in PROME's own words.** `DOCKET.tsv` L385 owners cell: *"PROME (registered; **made the call to carry this as a SEPARATE row rather than widen L384**)"*, reasoned in its state cell: *"widening L384 would have put an October hazard under a September review, which is the silent-ride failure the row itself warns about."* The plan's contrary justification (L58–59: *"A separate row would split one repair across two dates"*) never mentions L385 and is answered by it — those genuinely **are** two dates and two owners: a PROME code repair (9/24) and a BRENT basis decision (~9/22).

**Repair (exact):** append the tool-defect leg to L409 as proposed **minus** the 9/22 material, and open a second row at EOF: `date 2026-09-22 · owners "BRENT (owns MKT-CL-F-ABOVE-100 and the decision) / PROME (registered; tool owner, grades nothing)" · state PENDING`, body = the contract-basis pinning before October expiry, pointing at L409 for the code repair and at L386 for the class rule. Note in it that **BRENT already holds this item on its own surfaces** (`AGENTS/BRENT/NEXUS_BRIEF.md` L88: *"Sep 22 (Tue) … CLV26 expiry … resolve `CL=F` identity with a negative control"*; `SCRATCH.md` L18 the same) — so the row is a carrier, not news.

### ❌3 · CHANGE 1 IS REGISTERED AWAY FROM THE CLASS ROW THAT ALREADY OWNS THIS DEFECT — L386, never mentioned
The plan proves novelty for CHANGE 2 (*"verified this session: no DOCKET row carries it"*, L65) and performs no such check for CHANGE 1. There is a registered, undated **class row** for exactly this subject:

`DOCKET.tsv` **L386**, date cell `next-any-continuous-spread-read`: *"🔑 CLASS ROW, NO CLOCK BY DECLARATION — `CRACK-ROLL-DESYNC-METHOD`. THE CONTINUOUS-CONTRACT DESYNC IS A MONTHLY-RECURRING STRUCTURAL FEATURE, NOT A SEPTEMBER EVENT, AND ANY DATE OFFERED AS A *SAFE-AFTER* BOUNDARY IS WRONG BY CONSTRUCTION — 2026-09-22 INCLUDED."*

Its mandatory guard is *"resolve BOTH legs' `expireDate` AT EVERY PULL, PLUS A NEGATIVE CONTROL"* — and **HAWK's facet 4 is precisely the case that defeats that guard**: the tool prints the contract identity itself, so the reader believes the check already ran (`memory/…deltas_lie.md`: *"it defeats every detector above by appearing to have already run one"*). L386's own named consumers are *"HENRY · BRENT · TERRY · VIOLET · PROME (HEARTBEAT §1)"*. Under the plan as written, **not one of them ever learns their class row has a known bypass**, because the finding lands in a PROME tool-repair row dated 9/24.

L386 also states how to attach a clock to it: *"if it needs periodic review, review it from a SEPARATE dated row that points here and never by dating this one."* That is the shape the plan should have used.
**Repair (exact):** add one clause to L386's state cell naming the wrapper-label form as a fifth form that its stated guard does not reach, and have the new 9/22 row (❌2) point at L386. Do not date L386.

### ❌4 · I6 RUN IN REVERSE — a correction PROME made is written under HAWK's name
**Plan L48–49:** *"⚠️ SCOPED BY ITS OWNER: HAWK first claimed the defect decided whether BRENT's >$100 line was crossed, then **CHECKED and withdrew that**."*
**HAWK's own record, `a0d16be99` commit body:** *"**PROME's correction to my own framing, accepted** and written INTO the memory as the consequence-discipline rule: I claimed the defect decided whether a >$100 line was crossed. It does not…"*
**The memory file itself (line 106):** *"Consequence discipline, and it cuts the claim DOWN — **PROME's correction to HAWK's first framing, accepted**."*

HAWK did not check and withdraw; **PROME** corrected and HAWK accepted. The plan's own I6 (L20) says *"Every claim not established BY PROME carries its owner's name. Relaying is asserting."* This is the mirror failure and it is worse for the record: it hands PROME's correction to another desk, which removes PROME as the party accountable for it.

Compounding: the clause's cited source is *"packet fa081e7d8 §3"*, and that committed packet **still carries the un-withdrawn claim** — `PROME/inbox/2026-09-18_from-HAWK_…md`: *"Whether the line is crossed depends entirely on which contract it means, and the ticker's own label is wrong."* A reader following the row's pointer finds the opposite of what the row asserts, with no note that the packet was superseded.
**Repair (exact):** *"HAWK's packet claimed the defect decided whether BRENT's >$100 line was crossed. **PROME corrected that and HAWK accepted the correction into the memory file (`a0d16be99`); the claim still stands un-annotated in the packet `fa081e7d8` §3.**"*

### ❌5 · I2's COLUMN NAMES CONTRADICT THE FILE'S OWN HEADER ROW
**Plan L15:** *"I2. Exactly 6 tab-separated columns per row: date | **headline** | **owner** | state | **source** | notes."*
**`PROME/DOCKET.tsv` L77 (the file's literal header row):** `date · catalyst · owners · state · artifacts_citing · notes`

Three of six names are wrong, and one is wrong in **direction**: column 5 is `artifacts_citing` — artifacts that cite this row — not `source`. CHANGE 2 is the only change that writes a column-5 value, and it writes provenance there (*"AGENTS/CATO/runs/…A3 + the detailed brief…"*). Live practice does use col 5 for sources (L409, L426, L386 all do), so the **content is defensible and the invariant is not** — a cold reader validating the edit against I2 checks the wrong schema.
**Repair (exact):** restate I2 as the header row at L77 verbatim, and add one line saying col 5 is used in practice as sources/related artifacts despite its name.

*Column COUNT is verified correct: 420 of 426 lines have exactly 6 tab-separated fields; the other 6 are `#` comment lines (see ⚠️7).*

---

## ⚠️ NON-BLOCKING — eight

**⚠️1 · Every price in CHANGE 1 has no time or basis, and the $0.47 halves on another surface.** The plan cites `CLV26 $99.53` with no timestamp and no settle/intraday label. `AGENTS/BRENT/STATUS.md` L16 carries, for the same contract on the same day: *"Tape 15:31 ET … CLV26 $99.78 (−2.09%, below $100 intraday…"*. At 15:31 the distance to the line is **$0.22**, at ~17:5x it is **$0.47** — the surviving MAGNITUDE finding more than doubles depending on which intraday bar you pick, and no settle is quoted anywhere. `finding_distance_to_a_threshold_is_a_claim_about_its_basis`. A stranger cannot reproduce $0.47. **Needs:** the pull time and whether `MKT-CL-F-ABOVE-100` is a close-basis or intraday-basis line.

**⚠️2 · "the un-fire" has no antecedent in the row.** Plan L51: *"⛔ Do not record 'the un-fire was an artifact' — nobody established that."* The row never says the line **fired**. Only `FORGE/tools/market-data/README.md` does: *"BRENT's `MKT-CL-F-ABOVE-100`, which fired 2026-09-14."* A cold reader at L409 meets a prohibition on recording something they cannot identify. **Needs:** one clause — "the line fired 2026-09-14; today's sub-$100 read is the candidate un-fire."

**⚠️3 · n=3 is not reproducible and mixes two different kinds of observation.** Plan L52–54: *"n=3 UNCOORDINATED DESKS ON THIS CLASS IN ONE DAY (SAM's withdrawn −7.5% Brent roll artifact, HAWK's here, BRENT's own 9/22 flag) ⇒ [[finding_n_independent_deviations_is_a_sample_size_not_n_defects]]."* Two of the three are **deviations**; BRENT's is a **correct avoidance** — HAWK's packet: *"BRENT dodged it this morning only by pulling named contracts instead."* And a fourth party is omitted: `AGENTS/SAM/scripts/oil_roll_check.py` docstring, *"**TERRY caught the identical roll on the identical series the same day**"* (CATO raised it as R1 against SAM). Depending on what counts, n is 2, 3 or 4. The finding invoked is specifically about *deviations*. **Needs:** state the inclusion rule in the cell, and name TERRY.

**⚠️4 · `volume 43,844` exists in no artifact anywhere.** Plan L41: *"BZ=F $98.77 / −5.77% = BZZ26 $98.77 / −1.16%, volume 43,844 identical."* Repo-wide grep for `43,844`/`43844` across `*.md`, `*.tsv`, `*.py`: **0 hits** (SEARCH-NOT-FOUND). HAWK's packet, the BRENT packet, the memory file and the README all state the CL leg's `300,567` and **none** states a BZ volume. The clause's cited source is `fa081e7d8 §3`, which does not contain it. It is presumably from PROME's live pull, which is exactly why it needs its own instrument + timestamp. **Needs:** `(PROME pull, fetch.py, 2026-09-18 17:5x ET)` beside it, or drop the figure.

**⚠️5 · CHANGE 3's target cell is not decided.** Plan L97: *"APPEND to the `state` **or** `notes` cell, in place."* Under I1 the cell is the only degree of freedom in the whole edit, so naming two is not an executable instruction — and it decides where a future grep finds the promotion flag. **Needs:** pick one.

**⚠️6 · CHANGE 3 folds a different kind of "promotion" into L425, whose owners cell does not name HAWK.** L425 is a **create-or-extend** decision on a *new* candidate — its head: *"AUTO-MEMORY PROMOTION CANDIDATE … ⛔ DEDUP-BEFORE-CREATE IS NOT DONE"*, owners *"PROME … / HENRY · VIOLET (flagged it…)"*. CHANGE 3's item is a **COLD→HOT tier promotion of an existing file**. One word, two decisions, one row, and the second party is not in the owners cell. Also: the row's date cell is `next-PROME-flow-pass` while the plan itself states (L104–105) *"MEMORY.md measured 71% of cap … below the ≥75% demotion trigger — so this is a PROMOTION judgment, not a forced compaction"* — verified (18,243 B / 25,600 = **71.3%**), but it means **nothing currently schedules the event this row waits on**, and an undated row is outside the dated spawn driver. **Needs:** either a separate row, or a sentence naming what triggers the flow pass.

**⚠️7 · Two invariants are narrower than the file they describe.** (a) I2's *"Exactly 6 tab-separated columns per row"* fails on lines 1, 2, 53, 54, 55, 56 (`NF=1`, all `#` comments) — the invariant needs "non-`#` rows". (b) I4 (L17–18) says a session key has the form *"`next-<X>-session`"*, yet CHANGE 3's own target is `next-PROME-flow-pass` (plan L94, verified at L425), and the file also runs `next-PROME-closeout`, `next-WALTER-spec-pass`, `next-any-continuous-spread-read`, `next-DAEDALUS-vocabulary-pass` — plus one date cell `~2026-11-15` (L240) that I4 forbids and that L55's legend puts in *notes*, not the date cell. **Internal contradiction (plan L17–18 vs plan L94); non-blocking because no change edits a date cell.**

**⚠️8 · CHANGE 2: three small overreaches in cells that are otherwise clean.**
 (a) **"no carrier" overstates.** Plan L77: *"A3 has no carrier, which is what this row fixes."* CATO **designated** one — brief L3: *"Prepared for Will to share, consistent with his earlier delivery preference; no peer message or inbox packet sent."* The true statement is "the designated carrier is Will's hand-off, which is undated and has not happened."
 (b) **The absence claim's perimeter is undeclared.** Plan L75–77: *"PROME verified every fleet inbox: the only CATO finding ever routed to an owner is the 9/17 LIQUID one."* A stranger cannot tell whether "every fleet inbox" covered `inbox/`, `inbox/processed/` and `inbox/WALTER/`. My own sweep agrees on substance but finds two wrinkles: the LIQUID artifact is a **9/17 review routed on 2026-09-18** (`AGENTS/LIQUID/inbox/2026-09-18_from-PROME_cato-liquid-review-…md`, commit `59b56f1c8` 09:29 9/18) — "the 9/17 LIQUID one" reads as a routing date; and `PROME/inbox/processed/2026-09-15_from-CATO_manual-integration-proposal.md` is a second CATO→recipient artifact unless "owner" is defined to exclude PROME. Per STATE_VOCABULARY Class 13 this is **SEARCH-NOT-FOUND**, not VERIFIED, until the perimeter is written down.
 (c) **The row's date may fire after the obligation.** The cutoff is **2026-09-30 17:00 ET** and the row is dated **2026-09-30**; the spawn driver wakes the owner *"at the first boot on/after the date"*, which can be after 17:00 — and BOND could finalize BND-26 at any boot between now and then. **Needs:** date it `2026-09-19..2026-09-30` (the file carries 61 range rows, so the form is supported) or `2026-09-22`.

**Also noted, not scored (sub-⚠️):** the plan weakens PROME's own already-delivered wording — BRENT packet: *"PROME did not establish that **and it is not true**"*; plan L51: *"nobody established that."* Two strengths of the same instruction on two PROME surfaces. And *"BOND has been DARK all day"* (L70) is a live-pane claim with no artifact; it is consistent with the record (BOND's last self-commit `8b3c008ad`, 2026-09-17 16:06).

---

## The plan's own six questions, answered

**(a) Any invariant I1–I6 broken?**
- **I1 — HOLDS.** File is **426 physical lines** (`wc -l` = 426; `awk END{NR}` = 426; last byte is `0a`), so an appended row is L427. Header L1 confirms the convention verbatim: *"rows are cited by PHYSICAL LINE NUMBER; never insert, delete or reorder rows — append new rows at EOF only."* All three changes respect it.
- **I2 — BROKEN as stated (❌5), satisfied in count.** Names wrong vs L77; 420/426 lines have 6 fields, 6 are `#` comments (⚠️7a).
- **I3 — HOLDS in intent, untestable from the plan.** The proposed cells are displayed as wrapped multi-line blocks; nothing in them requires an embedded tab or newline, but a careless paste of CHANGE 2's six labelled blocks would introduce five.
- **I4 — the invariant itself is wrong** (⚠️7b); no change violates the file's actual practice.
- **I5 — HOLDS, narrowly.** No gate graded, no threshold moved, no trade, no capital. Closest call: CHANGE 1 asserts *"the verdict is identical either way"* about BRENT's registered line. That is a statement about another desk's line, but it asserts **no change** and explicitly bars the stronger version. Say in the cell that BRENT owns the verdict and PROME asserts only contract identity.
- **I6 — BROKEN, in mirror (❌4).**

**(b) Any claim stated as PROME's that is actually CATO's / HAWK's / SAM's / BRENT's?**
No — and CHANGE 2 is exemplary on this: *"⚠️ THE FINDING IS CATO'S, NOT PROME'S — PROME has NOT inspected BND-26's evidence, the H.15 cells, or the grading branches, and asserts nothing about the grade"* is correct, well-scoped, and matches CATO's brief exactly. **The failure runs the other way** (❌4): a correction PROME made is attributed to HAWK. One softer instance: CHANGE 1's *"SAM's … `oil_roll_check.py` … is the PROMOTABLE control and the repair candidate"* is PROME's judgment about SAM's file and does not say the promotion is SAM's to accept — see (f).

**(c) A MAGNITUDE written as a VERDICT (or the reverse)?**
**Yes — ❌1**, and it is the same word HAWK's own record deliberately avoids. No instance of the reverse (a real verdict softened into a magnitude): the un-fire framing is correctly barred in both the plan and the packet.

**(d) Does CHANGE 1 belong on L409, and does folding ~9/22 into a 9/24 row hide the earlier date?**
**The tool-defect leg belongs on L409. The ~9/22 exposure does not, and folding it does hide the date — ❌2.** What I would do instead, exactly: (i) append to L409 only the FORGE-tool half (mislabel + cross-roll day-change, reproduction, README stopgap, SAM's script as the promotable control); (ii) open a new row at EOF dated **2026-09-22**, owners *"BRENT (owns the line and the decision) / PROME (registered; tool owner, grades nothing) / HAWK (raised the defect)"*, carrying the contract-basis decision and pointing at L409 and L386 — and recording that BRENT already holds the item on `NEXUS_BRIEF.md` L88 and `SCRATCH.md` L18, so the row is a carrier and not a surprise; (iii) add the fifth-form clause to **L386** (❌3). That is three registrations plus CHANGE 2 and CHANGE 3, and it puts each date under the owner who has to act on it.

**(e) Is CHANGE 2's "no carrier" claim supportable?**
**Mostly yes; it overreaches by one word.** VERIFIED: no DOCKET row anywhere carries the obligation (`grep -i "cutoff\|17:00 ET"` returns four unrelated rows; no BND-26 row mentions a publication cutoff; L410 `2026-10-01 BOND QUARTERLY REFRESH` carries two other decisions). VERIFIED: CATO sent nothing (*"no peer message or inbox packet sent"*) and claims no acknowledgment (*"No owner acknowledgment of this updated brief is claimed"*). VERIFIED: BOND's last self-commit is `8b3c008ad` 2026-09-17 16:06, before the 14:10 brief. The overreach is that a carrier **was designated** — Will — so the accurate claim is "the designated carrier is an undated hand-off by Will that has not happened" (⚠️8a). And the row's own date may fire after the cutoff (⚠️8c).

**(f) Anything reading as authority to edit another desk's files or grade another desk's gate?**
**No explicit authority claim — the disclaimers are strong and correct.** CHANGE 2 says *"⛔ This row registers a DATE and an OWNER. It does not grade, re-date, or pre-judge BND-26, and it is NOT authority to edit BOND's files."* CHANGE 1 says *"PROME re-graded nothing"*; CHANGE 3 attributes facet 4's distinctness *"in HAWK's words and not PROME's."* Two residues: (i) *"SAM's … `oil_roll_check.py` … is the PROMOTABLE control and the repair candidate, NOT a fourth hand-written guard"* — a PROME disposition of a SAM-owned file, in a PROME-owned ledger, with no sentence saying **SAM owns that decision**; promoting it into FORGE would be a cross-desk change and the row should name who rules on it. (ii) CHANGE 1's *"the verdict is identical either way"* is PROME speaking about BRENT's registered line (see I5).

---

## Claim ledger — 41 load-bearing claims

### Structure / invariants
1. DOCKET.tsv is 426 physical lines → **VERIFIED** (`wc -l`=426, `awk END{NR}`=426, trailing `0a`).
2. A new row becomes L427 → **VERIFIED** (follows from 1 + trailing newline).
3. Citation convention is physical line number, append-at-EOF only → **VERIFIED** verbatim at DOCKET L1.
4. Rows carry exactly 6 tab-separated columns → **VERIFIED for count** (420/426; 6 `#` comment lines at `NF=1`). ⚠️7a
5. Column names `date|headline|owner|state|source|notes` → **❌ FALSE**; L77 reads `date|catalyst|owners|state|artifacts_citing|notes`. ❌5
6. Date cell is ISO / ISO-range / `next-<X>-session` → **⚠️ INCOMPLETE**; 18 non-ISO cells, most not `-session`; one `~2026-11-15`. ⚠️7b
7. State token `PENDING` is legal → **VERIFIED** at DOCKET L55 legend.
8. Nothing here grades a gate / moves a threshold / moves capital → **VERIFIED** (see I5 above).
9. Every non-PROME claim carries its owner's name → **❌ BROKEN in mirror**. ❌4

### Session premise
10. `bc5f3141d` = AEOLUS unrounded-column caveat onto L426 → **VERIFIED** (2026-09-18 17:22:08, `PROME/DOCKET.tsv` 1 insertion).
11. `431f1f9b2` = L426 framing corrected by its owner → **VERIFIED** (17:22:44; also touched `PROME/state/ORCH_LOG.tsv` — immaterial).
12. Two correction commits ⇒ independent cold read required → **VERIFIED** against auto-injected `PROME/CLAUDE.md` § Session Process Controls (two-correction stop + WQ-178 read budget).

### CHANGE 1
13. L409 date cell = `2026-09-24` → **VERIFIED**.
14. L409 head text as quoted (fetch.py fred_fetch ≈:330-357, no realtime_*, GATE-HY-REKILL / GATE-TERRY-007 as-first-published) → **VERIFIED** verbatim.
15. L409 owners as quoted → **VERIFIED** verbatim — and **does not contain BRENT**. ❌2
16. L409 state as quoted (registered 2026-09-17 10:1x from DAEDALUS packet `ce9dc5f90` ask 5; INSTANCE 9/17 21:4x) → **VERIFIED**; `ce9dc5f90` is real (2026-09-17 10:06, DAEDALUS→PROME).
17. HAWK raised it in packet `fa081e7d8` §3 → **VERIFIED** (commit real, 17:50:53; `PROME/inbox/2026-09-18_from-HAWK_europe-rearm-tree-opened-plus-a-shared-tool-defect.md` §3).
18. `CL=F` $95.47 / −6.32% labelled "Oct 2026 (CLV26)" → **VERIFIED** at 3 committed artifacts (packet, README, memory).
19. `CL=F` byte-identical to `CLX26`, volume 300,567 → **VERIFIED** at the same 3.
20. Real October `CLV26` $99.53 / −2.34% → **VERIFIED** at the same 3; ⚠️ no time/basis, and BRENT's 15:31 bar reads $99.78. ⚠️1
21. `BZ=F` $98.77 / −5.77% = `BZZ26` −1.16% → **VERIFIED**.
22. BZ volume 43,844 identical → **SEARCH-NOT-FOUND** — 0 hits repo-wide. ⚠️4
23. $95.47/$101.91−1 = −6.32% vs November's real −1.81% → **VERIFIED** (arithmetic checks; figures in all 3 artifacts).
24. Reproduced live by PROME before registration, not relayed → **INFERRED** (asserted identically in the README and the BRENT packet, both PROME-authored; no third-party receipt).
25. Dated exposure ~2026-09-22 (October expiry), earlier than the row's 9/24 → **VERIFIED and self-admitted**. ❌2
26. Stopgap banner at `FORGE/tools/market-data/README.md` (`4ba52bdf5`) states it does not close the row → **VERIFIED** verbatim: *"This banner is a stopgap, not the repair, and it does not close L409."*
27. BRENT packeted; its line is keyed literally on `CL=F`; PROME re-graded nothing → **VERIFIED** (`AGENTS/BRENT/inbox/2026-09-18_from-PROME_…md`, commit `4ba52bdf5`).
28. HAWK claimed the defect decided the >$100 verdict, then **CHECKED and withdrew** → **❌ FALSE as to who checked**; HAWK's record says PROME corrected and HAWK accepted. ❌4
29. Both contracts below $100 ⇒ verdict identical either way → **VERIFIED** on the quoted levels; ⚠️ basis unstated, and the line fired 2026-09-14 (README) so the live question is the un-fire. ⚠️1 ⚠️2
30. "a $0.47 crossing shown as $4.53" → **❌ MISLABELLED QUANTITY**. ❌1
31. "Do not record 'the un-fire was an artifact' — nobody established that" → **VERIFIED in substance**; the BRENT packet states it more strongly (*"and it is not true"*) and "un-fire" is undefined here. ⚠️2
32. n=3 uncoordinated desks in one day (SAM / HAWK / BRENT) → **⚠️ NOT REPRODUCIBLE** — mixes a deviation class with an avoidance; TERRY omitted. ⚠️3
33. SAM's `oil_roll_check.py` exists, is boot-wired, commit `512ac5a1c` → **VERIFIED** (2026-09-18 16:32:37; `AGENTS/SAM/scripts/oil_roll_check.py` 154 lines + `scripts/boot.py` +1).
34. SAM's withdrawn −7.5% Brent roll artifact → **VERIFIED** (`AGENTS/SAM/NEXUS_BRIEF.md` L11, `STATUS.md` L49/L89, `MAINTENANCE.md` L30 — corrected on CATO R1 with TERRY's evidence).
35. "Amend rather than open a new row" is the right call → **❌ CONTRADICTED by the file's own precedent at L385**, and by L386 being the class carrier. ❌2 ❌3

### CHANGE 2
36. CATO brief `2026-09-18_1410_prome-updated-action-brief.md` exists, item A3 as described → **VERIFIED** (file present; A3 verbatim: *"Respect the September 30, 17:00 ET publication cutoff before finalizing unresolved BND-26 outcomes; preserve the registered observation window and grading branches."*).
37. Companion brief `2026-09-18_1102_prome-action-brief.md` exists → **VERIFIED** (14,684 B). Both pointers resolve.
38. A2 and A4 quoted correctly (I-prime / 68% subgroup / implied 23/52 = 44.2%; first-publication evidence) → **VERIFIED** verbatim in the brief's retained-findings table.
39. Not registered anywhere in DOCKET → **VERIFIED** (no BND-26 row mentions a cutoff; `grep -i "cutoff\|17:00 ET"` returns four unrelated rows; L410 is a different obligation).
40. CATO sent no packet, claims no acknowledgment, "prepared for Will to share" → **VERIFIED** verbatim (brief L3 and L81). "No carrier" = ⚠️8a.
41. "PROME verified every fleet inbox: the only CATO finding ever routed to an owner is the 9/17 LIQUID one" → **SEARCH-NOT-FOUND, not VERIFIED** (perimeter undeclared; routing date is 9/18; a CATO→PROME artifact exists at `PROME/inbox/processed/2026-09-15_from-CATO_manual-integration-proposal.md`). ⚠️8b
42. BOND dark all day / no commit since before the brief → **VERIFIED for commits** (`8b3c008ad` 2026-09-17 16:06 is BOND's last self-commit); darkness itself is **UNKNOWN** from artifacts.

### CHANGE 3
43. L425 date cell = `next-PROME-flow-pass`, registered 2026-09-18 16:3x by PROME, HENRY+VIOLET flagged and neither wrote it → **VERIFIED** verbatim.
44. `a0d16be99` touched that memory FILE only; MEMORY.md untouched; carve-out ③ correct → **VERIFIED** (`git show --name-only` = 1 file).
45. The memory is COLD-tier → **VERIFIED** (`INDEX_COLD.md` L271; 0 hits in hot `MEMORY.md`).
46. Promotion rule ("extending a COLD-tier memory obligates a promotion flag to PROME … the row carries n=") → **VERIFIED** verbatim in the auto-memory index header, Will-approved 2026-08-21.
47. Not promotion-EXEMPT → **VERIFIED** (absent from `INDEX_COLD_EMBEDDED.md`; the `[embedded→]` exemption does not apply).
48. n = 4 facets / 3 uncoordinated desks → **VERIFIED for facets** (facets 1–4 present, plus two facet-3 sub-forms); **⚠️ for desks** (see ⚠️3).
49. HAWK did not self-promote, left execute-or-decline to PROME → **VERIFIED** (`a0d16be99` body: *"PROMOTION FLAG OWED … Raised to PROME directly … Not self-promoted."*).
50. MEMORY.md 71% of cap, below the ≥75% demotion trigger → **VERIFIED** (18,243 B / 25,600 = 71.3%; trigger text in the index header).
51. Facet 4's distinctness claim, "in HAWK's words and not PROME's" → **VERIFIED** — the plan's paraphrase matches the memory's facet-4 opening closely and the attribution is correct.

---

## POINTERS: 13/13 resolve; dead: none
`PROME/DOCKET.tsv` L409 ✅ · L425 ✅ · L426 ✅ · `fa081e7d8` ✅ · `a0d16be99` ✅ · `4ba52bdf5` ✅ · `512ac5a1c` ✅ · `bc5f3141d` ✅ · `431f1f9b2` ✅ · `ce9dc5f90` ✅ · `AGENTS/CATO/runs/2026-09-18_1410_prome-updated-action-brief.md` ✅ · `AGENTS/CATO/runs/2026-09-18_1102_prome-action-brief.md` ✅ · `AGENTS/SAM/scripts/oil_roll_check.py` ✅
*(Not a dead pointer but worth naming: `fa081e7d8` §3 resolves to a packet whose headline claim the plan describes as withdrawn, with no withdrawal recorded in it — ❌4.)*

## ONE-LINE VERDICT
**No — not as written.** CHANGE 2 is sound and should go in (fix the date and the "no carrier" wording); CHANGE 3 is sound but names two target cells and folds a tier-promotion into a create-or-extend row; **CHANGE 1 should not be executed in this shape** — it reprints a distance as a "crossing" in the canonical record, hands PROME's own correction to HAWK, and buries a 9/22 BRENT decision inside a 9/24 PROME row whose owners cell does not name BRENT and whose class already has a registered carrier at L386 that the plan never mentions.
