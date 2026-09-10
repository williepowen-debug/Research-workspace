# CARL SCRATCH
**Last session:** **2026-09-10 (Thu) ~12:23 → ~13:5x ET** — PROME-spawned Tier-1 **ruling-implementation** session (Will *"spawn all three"* 12:22). Dark since 9/5.
**Type:** Two Will rulings encoded + whole-inbox drain (7→0) + a calibration audit worked. **NO vector moved — 53/70 (76%) holds, 11th consecutive cycle.**

---

## ⏭️ NEXT SESSION, FIRST TWO THINGS
1. **⛔ THE 9/30 PREDICTION CLUSTER IS NOW 20 DAYS OUT AND STILL UNTOUCHED — 3rd session carried.** **CRL-05** (+ its basis question, **7th session carried — do not carry it an eighth**), **CRL-08** (window closes ~9/30, gap 35.4¢), **CRL-17**, **CRL-21**. **Do not let these resolve by expiry.**
2. **STATUS rotation #11 — STRUCTURAL, not a byte-trim. It grew again today (43,794 → 45,101 B, 1.39× budget).** Order is fixed and is STUE's diagnosis, not mine: **(c) audit the dashboard for rows that are not VALUES and move them out** → **(b) read-mode change** (bounded head + grep body) → **(a) rotation as a standing step.** Measure the boot-read TOTAL in **BYTES** and report it **even if it rises.**

---

## WHAT HAPPENED — the two rulings landed, and one of them was already done

### ✅ WQ-182 — V16's drop-back branch RATIFIED AS WRITTEN, and the flag is discharged
Will, **2026-09-10 11:22 ET (15:22Z)**, Decision Deck tap **`APPROVE`**. The branch letter is **unchanged**; what is removed is `[provisional structure — Will review at next matrix pass]`. **RIDER, binding (WQ-175 ②): the 2-of-2 count runs on the vintage in force at each print — a later revision of print 1 ANNOTATES, never re-counts.**
- ⇒ **August's print-1 status is FIXED** at what published 9/4 (**+162K with +55K net up-revisions**). An October revision cannot un-count it.
- ⇒ Symmetrically, a later up-revision cannot **manufacture** a print-1 — which is exactly what the 9/4 retraction did to the escalate leg (**escalate is 0 of 2, not 1 of 2**).
- **Encoded on 5 surfaces** (THESIS V16 COL7 · STATUS mirror · CATALYSTS 10-02 · CALENDAR 10-02 · ROADMAP_THREADS) + CHANGELOG + KB-CARL-433.
- 🔴 **Resolver = September NFP ~Fri 10/2. LABOR grades the PRINT; CARL grades the BRANCH.** Positive-with-up-revisions ⇒ 2 of 2 ⇒ **4→3 candidate to Will**; negative OR net down-revisions ⇒ **RESETS to 0**. ⚠️ **Do not step down on one print** — the letter's own *"single-month discipline applies in both directions"* clause held V16 at 3 against June's +57K on 7/2 and binds symmetrically.
- 🔑 **The 9/5 escalation got exactly what it asked for: the branch was ratified BEFORE it resolves, not after.**

### ✅ WQ-183 — the PARENT holds the pen on a sub-agent card. ⚠️ **Its ACTION was already satisfied when it arrived.**
The packet said *"apply the read-mode + placement change to STUE's `CLAUDE.md` at your next boot."* **All three amendments were already on the card** — STUE applied them itself on **9/5** on Will's *separate* word (*"I do want you able to edit your local CLAUDE.md and boot instructions"*). **I verified all three at the artifact before touching anything** (bounded head as an explicit SECTION LIST · values-and-pointers in Doc Ownership · rotation as `On Session End` 3b) and applied **only the un-encoded half — the pen ruling**, as a dated ruling on the card, story to `CLAUDE_PROVENANCE.md` §P-PEN.
- 🔑 **Re-applying would have duplicated the rule and read, forever after, as two independent authorities saying the same thing.** `[[finding_directive_overtaken_between_authorship_and_delivery]]` — and the inverse of `[[finding_record_of_an_action_is_not_the_action]]`: here the RECORD said "owed" and the ARTIFACT said "done".
- **Riders on the card:** a card edit is a dated ruling in the parent's tree · the two-correction stop binds it · ⛔ **STUE's 9/5 refusal was CORRECT and stays its standing behaviour** — a sub-agent never rewrites its own card on a peer session's say-so.

### ★ THE DAEDALUS AS-MADE AUDIT — 19 candidates, 9 refuted, 10 sustained, and the finding is bigger than the flags
⛔ **The audit tool has a THIRD limit it did not name: an ID can be REASSIGNED to a different claim.** `4e8c98359` (2026-03-09, verified earliest by `git log --reverse`) uses a different ID→claim map — its CRL-05=Fannie MF, 06=Student 90+, 07=CC 90+, 08=Foreclosures ⇒ **today's CRL-03/04/05/06**. Four flags compared **two different predictions**, both cells real confidences.
🔑 **This is the only branch a careful reader would have BANKED.** The two *named* limits fail loudly — a `98% → 6%` swing on a CONFIRMED row is self-evidently a value cell; two of the flags read a percentage out of a **masthead sentence**. **Five more flags were the ledger's own `(was Y)` chain working exactly as WQ-112 designed it** — the tool takes the first percentage and read past the history.

🔴 **THE CALIBRATION RESULT, AND IT IS NOT A WASH.** Four SUSTAINED rows are RESOLVED, so their Brier vintage changes — **and all four move the same direction, worse:**

| ID | outcome | scored at | should be | ΔBrier |
|---|---|---|---|---|
| CRL-03 | MISSED | .5184 | **.8100** | **+0.2916** |
| CRL-06 | CONFIRMED | .0484 | .0900 | +0.0416 |
| CRL-11 | MISSED | .6889 | .7225 | +0.0336 |
| CRL-04 | CONFIRMED | .0004 | .0144 | +0.0140 |
| | | | **sum** | **+0.3808** |

⛔ **The mechanism is benign, which is why it is dangerous.** A desk re-prices a live prediction — correct behaviour — and overwrites the confidence cell. **But the walk is SELECTED FOR: the row that got re-priced is the row that was hard and moved a lot, i.e. the row carrying the most Brier weight.** ⛔ **And it flatters BOTH ways** — on the CONFIRMED rows the ledger sat **above** the as-made, on the MISSED row **below**. **A mean-zero assumption about the drift is unsafe.** Same shape as LABOR's 0.299 → 0.342. KB-CARL-434/435; new auto-memory `[[finding_confidence_walk_is_selected_for_on_the_rows_that_carry_the_most_brier_weight]]`.
✅ **I did NOT recompute CARL's aggregate Brier** — the **9/14 ladder sitting** owns the scoreboard; I owe it corrected **inputs**. ⚠️ **CRL-10/11/17 are marked EARLIEST RECORDED, not as-made** (Date_Made precedes first STATUS appearance) — **a recovered-but-unprovable as-made is not the same object as a proven one.**

### ✅ Dated rows — 2 of 4 gradeable today, both graded at the primary
- **L281 / L151 — FSA `PortfoliobyLoanStatus.xls` POLLED 2026-09-10 16:35 UTC: `Last-Modified: Thu 18 Jun 2026 21:05 GMT`, MD5 `4732c453…d007`, 133,120 B — UNCHANGED, byte-identical to the 9/5 pull AND STUE's 8/13 copy.** ⇒ **FY2026-Q3 has NOT posted; 2nd consecutive CHECKED ABSENCE recorded as a non-event.** L281 ⇒ NO CHANGE, re-date +1wk (**~9/18, docketed**); L151 window (9/1–9/30) PENDING, 20d left. ES-01/04/06 unmoved.
- ⛔ **TWO INSTRUMENT DEFECTS, both found only by RUNNING it (KB-CARL-437): ① the path is CASE-SENSITIVE — `PortfoliobyLoanStatus.xls`, lowercase `b`. DOCKET L281 spells it with a CAPITAL B, which returns HTTP 404 — and a 404 reads as "withdrawn", a WRONG FINDING, not an error.** ② 🔑 **The ETag IS `<MD5>:<epoch>` — a HEAD request alone proves byte identity; never download the 133KB file.** Routed to PROME (owns the DOCKET text).
- **NOT gradeable today, dates stated:** **L152** SAVE→RAP first-tranche read — **9/29–10/1** · **L153** RAP auto-pay deadline — **9/30**.

### ✅ Other inbox work
- **LABOR claims refreshed: 206,000 w/e 9/5, 4-wk MA 206,000** (w/e 8/29 revised 206→207K; prior MA 207,250→207,500). Kill-rule leg `<220K` **stays SATISFIED — the verdict never moved, only the figures.** ⛔ **The MA's −1,500 is the 212,000 roll-off, NOT easing.** ⚠️ Next week the roll-off is 207,000 ⇒ an identical print moves it **−250, 6.0× smaller** — a reader without the roll-off sees "improvement slowing" where nothing changed. 🔴 **LABOR's T-01 now routes to CARL; its bound `X > 1,000,000 − (W2+W3+W4)` is re-solved weekly (383,000 → 382,000 on 9/10) — quote the FORMULA, never the number.**
- **`roadmap_index.py --check` PATCHED** (PROME's 9/5 build) and **falsified before trusting it**: T1 clean ⇒ 0 · **T2 (Codex's false-pass case: Next Step mutated, thread name kept) ⇒ 1** · T7 dup anchor ⇒ 1 · restored ⇒ 0. It now compares the **rendering**, not a name set.
- **COR-20260905-02 emitted** (ES-02 reading-rule defect, direction **HOLD** with the re-derivation figures in the cell) + **COR-20260905-01 receipted APPLIED**; `corrections_boot_check.py CARL` rc=0.
- **STUE tracker banner-vs-body: PROME's INFERRED flag PARTLY REFUTED.** No substantive contradiction — the banner is about *generalisation*, the body about the *checker implementation*, and both are true. **The defect is one word: "FALSIFIED against live data"** describes a rule reproducing, on its own fitting data, a boundary its author had already picked. Routed to STUE with the suggested wording; **I did not edit STUE's workbook** (the pen ruling scopes to the CARD).

### 🔧 Structural fix found in passing
**The two threads the 9/5 split session added lived as PROSE in `ROADMAP.md`, outside the generated index — invisible to the drift gate.** The split's own first session used the pre-split method. Both moved into `ROADMAP_THREADS.md` as rows, one ✅-closed thread moved to RECENTLY RESOLVED, index rebuilt: **28 → 31 threads, ROADMAP 31,946 → 29,614 B.** `[[finding_a_ruling_governs_the_next_write_not_the_existing_state]]` — **a new convention touches NOTHING already on disk.**

---

## STATUS CHANGES
| Item | Change |
|------|--------|
| **V16 Employment** | **HOLDS 4.** Drop-back branch **RATIFIED (WQ-182)** + vintage rider; **LIVE 1 of 2**, resolver ~10/2. Escalate **0 of 2** |
| **Claims** | **206,000 w/e 9/5, MA 206,000** — supersedes 206K/207,250. Kill-rule leg SATISFIED |
| **FSA defaults** | **FY2026-Q3 NOT POSTED** (polled 9/10) — 2nd checked absence; re-poll ~9/18 |
| **Calibration** | 🔴 **4 resolved rows re-marked, ΔBrier sum +0.3808, all WORSE.** Inputs owed 9/14 |
| **Convergence** | **NO CHANGE — 53/70 (76%), 11th cycle** |
| KB | 432 → **437** rows (KB-CARL-433…437) |
| Inbox | **7 → 0**, all filed to `processed/` |

---

## NEXT SESSION SHOULD

### IMMEDIATE
1. **Pull gas first** (standing rule). Last read **AAA $4.146 (9/5)**, diesel **$5.882**, Brent **$96.02 (9/1)** — **all stale by 5 days.** V5 cushion was 14.6¢ and WIDENING; CRL-08 gap 35.4¢, **window closes ~9/30.** The 9/1 crude re-rise reaches the pump ~9/11–9/18.
2. **August CPI printed Fri 9/11 — INTEGRATE IT.** CARL's leg is the pump input and it **inverts from July**: August FRED weeklies ≈ **$4.06** vs July ≈ **$3.93** ⇒ **gasoline CPI should print POSITIVE MoM** where July was base-effect-protected negative. ⛔ **Modest, not a spike** — a positive-but-small print is compatible with BOTH HEN-41 CONFIRM and DENY, and **HEN-41 is HENRY's letter, not CARL's.** UMich Sept prelim same morning — do not let CPI absorb it.
3. **9/14 DAEDALUS ladder sitting — the corrected as-made inputs are OWED** (docketed). Supply inputs only.
4. **~9/15 SDART/BLAST August 10-D** — first live application of the ruled leg. **Matched collection month, YoY, per deal, in pp. ⛔ NEVER MoM.** Deep tier files ~9/30; **the tier verdict defers to the later-filing tier ⇒ the real V2 grade is ~9/30.**
5. **FOMC 9/15-16** — V12 un-fire needs a dovish pivot returning a 2026 cut to the dots **across 2 consecutive meetings**; this is **meeting 1 of 2**, first surface where dots exist.

### THIS WEEK / CARRIED
6. **~9/18 FSA re-poll** (docketed). **HEAD only; lowercase `b`.**
7. **9/8 PHAN spawn is now +56d and was NOT done today** — gate fired 8/27. Affirm/Klarna **AND** the COCKROACH/REGULATORY sweep.
8. **⚠️ CRL-05 BASIS QUESTION, 7th session carried.** Resolves on a **LEVEL** (>13.74%, Equifax-3.0 era) against VantageScore-4.0 prints. **A basis change is never a threshold trigger:** re-base or declare **NO-VERDICT-by-basis**, then packet PROME.
9. **`abs_monitor.py` coverage fix — still owed, 3rd session.** It structurally cannot see V2's registered panel (tracks the four newest Exeter CIKs; registered panel is EART 2022-2/2022-3/2023-1/2024-1). **A monitor that cannot see its own panel is worse than none, because it reports clean.**
10. **CARL-DR-5 at DEWEY is now +12d past due** (grocery volume: POLICY vs CYCLE vs MEASUREMENT ARTIFACT). Pre-registered both ways — **it can score a strike against my own evidence.** Chase it.
11. **Ask STUE to reconcile the tracker wording** (packet delivered) and to confirm at its next boot that it read the pen ruling **from the card**, not from my packet.
12. `housing_pulse.py:226` hardcoded 3.98M under the live 4.06M; Fannie URL 404s. **Same class as the FSA case-sensitivity defect found today.**
13. **WATT-10 (FERC Door A/Door B, ~10/12, outer 10/31)** — Door A socialises data-center cost to ~65M PJM ratepayers = CARL's CPI channel. ⛔ **Do NOT put an LMP spike in a CPI story** — residential bills run an ANNUAL tariff clock.

---

## URGENT / DISCIPLINE
- **⚠️ A RULING'S ACTION LINE CAN BE STALE ON ARRIVAL, AND THE RULING STILL BINDS.** WQ-183's ACTION was satisfied two days before the ruling was written. **Verify at the artifact before executing a directive, even a Will-ruled one** — the ruling's AUTHORITY is not evidence about the world's STATE. Re-applying it would have produced two authorities for one rule.
- **⚠️ THE FAILURE MODE THAT LOOKS PLAUSIBLE IS THE ONE THAT GETS BANKED.** DAEDALUS's tool failed three ways today. Two produced absurdities and were caught in seconds; the third produced two believable confidences and would have been accepted. **When you list an instrument's limits, ask which of them fails QUIETLY — that is the one to engineer against.**
- **⚠️ MY OWN BRIER IS FLATTERED AND I FOUND IT BY BEING AUDITED, NOT BY LOOKING.** Four for four in the same direction. **The re-pricing that corrupts the record is the same act as good forecasting** — there is no version of this I would have caught by being more careful. **It needed a column, not a discipline.**
- **⚠️ A 404 IS A FINDING-SHAPED OBJECT.** The capital-B path returns HTTP 404 with a 10-byte body. Polled without care that reads as *"the release was pulled"* — a **wrong finding**, not an error. **Case-sensitivity in a wake-surface row is a silent-wrong-answer defect.**
- **✅ Kept from 9/5 and still true:** `open(path,"w")` truncates before it writes. **Every edit this session built the string first, asserted a minimum length, wrote `.tmp`, then `os.replace`.** Zero incidents.

---

## WORKBOOK HEALTH
| File | Size / rows | Note |
|---|---|---|
| **STATUS.md** | **45,101 B** | 🔴 **1.39× the 32,550 B budget, +1,307 B today.** Rotation #11 owed and STRUCTURAL — order (c) → (b) → (a). **Do NOT byte-trim** |
| **MEMORY.md** (local) | 46,494 B / 97 lines | 🔴 **3 lines from the 100-line cap. NOT grown today — the lessons went to auto-memory, which is what the cap rule asks.** ⛔ Flag to PROME; do not compact |
| **ROADMAP.md** | **29,614 B** | ✅ **0.91× budget.** 31 threads (28 + the 2 orphans recovered + 1 new). Index GENERATED, gate now compares the RENDERING |
| **ROADMAP_THREADS.md** | 31,423 B | grep-only, off the boot path |
| KB.tsv | **437 data rows** | +5 (KB-CARL-433…437). All 15-field verified, no dup IDs |
| PREDICTIONS.tsv | 29 (15 OPEN) | ⚠️ **CRLF — binary-mode edits ONLY** (honoured today). **10 rows re-marked with as-made.** Still +60d behind STATUS on `ledger_staleness` — **freeze or refresh next session** |
| CATALYSTS.tsv | 25 data | +2 (9/14 ladder, 9/18 FSA re-poll); CALENDAR twin synced by hand |
| board_log.tsv | 62 lines | untouched — no BOARD lane traffic this session |

---

## OUTBOX / PACKETS SENT (3, all committed under carve-out ①)
- **DAEDALUS ×1** — as-made audit worked; **19 triaged (9 refuted / 10 sustained)**, the **third tool limit (ID reassignment)** with a cheap fix, and the **ΔBrier table for the 9/14 sitting**.
- **STUE ×1** — tracker banner-vs-body **partly refuted**, the one-word defect, the suggested wording, and *"read the pen ruling from the card, not from this packet."*
- **PROME ×1** — the COMPLETION memo (this session), incl. the **DOCKET L281 case-sensitivity defect** and the **ETag=MD5** improvement.

## INBOX — **7 consumed, 7 filed, AT ZERO**
`find inbox -maxdepth 2 -name "*.md" -not -path "*/processed/*"` → **0**. ⛔ **Never count with `ls inbox/*.md`.**
