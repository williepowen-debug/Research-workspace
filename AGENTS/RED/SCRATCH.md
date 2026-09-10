# RED SCRATCH — Canonical Session Handoff

<!-- TEMPLATE — rewrite in place at W5 every session; git history versions this file.
     Section order (headings written WITHOUT the "##" here ON PURPOSE — see below):
       1. CHANGES SINCE   — what moved while RED was offline
       2. WHAT I DID
       3. NEXT SESSION    — dated, priority-ordered
       4. OPEN THREADS
       5. PENDING WILL-DECISIONS
       6. GIT STATE       — one line

     !! DO NOT restore the "##" prefixes to the list above. !!
     They were verbatim copies of the live body headings until 2026-08-12, which made every
     heading-anchored edit AMBIGUOUS: a scripted insert anchored on "## OPEN THREADS" matched
     THIS BLOCK first and wrote the content inside the comment. It happened three times on
     8/12; one instance was committed and pushed (4b3bb1b55) with two carry-forward threads
     rendering as nothing while present in the file.
     No check can see that class — claim_check, ledger_staleness, orphan_check and a content
     grep all PASS on a file whose content is commented out. (ML-RED-155)

     If you script an edit to this file: anchor on a body-unique string, and verify placement
     by heading OFFSET (which occurrence), never by presence.
-->

**🆕 S42 (2026-09-09, Wed, spawn ~21:0x → close ~21:2x ET — stamps from `date`; PROME Tier-1 due-row spawn on DOCKET L275, WQ-184 L0 rule) — FT-10's RUN IS BROKEN. Count 0-of-4. NO WEIGHT MOVED: HOLD 68 / net-bear 58 stand.**

## CHANGES SINCE (S41 close 9/6 ~12:5x → this spawn) — RED was DARK 3 days and the thing that moved was RED's own registered line

- **🔴 `RED-FT-10`'s run DIED while RED was dark.** CBOE published **148.86 [9/8]** — 1.14 below — resetting the run that had reached **2-of-4** (150.63 [9/3] · 151.58 [9/4]). **9/9 published 149.25** and did not open a new one. **Four RED-owned surfaces carried "COUNTING 2-of-4" for ~24 hours** after WALTER (`SIG-W-20260908-019`) and PROME (`PROME/reports/2026-09-08_evening-skew-recheck.json`) had both measured it. **Peer observation is not owner integration** — ML-RED-232.
- **3 packets landed** (LABOR ×2 on 9/7, ORACLE ×1 on 9/7); `inbox/WALTER/` empty.
- **⚠️ 23 RED-addressed BOARD signals accumulated since the 9/6 disposition, 2 action-addressed** — NOT consumed this session (bounded spawn). See NEXT SESSION #1.
- **Tape at close [own pulls / boot.py 9/9 ~21:0x]:** ^SKEW **149.25** [CBOE 9/9] · VIX **15.72** [FRED 9/8] · HY **267** · CCC **1,056** · Brent 101.29 · USDJPY 153.63 · 30Y-proxy 10Y 4.84.

## WHAT I DID

1. **FT-10 OWNER-GRADED at the publisher, first-hand.** Pull 2026-09-09 **21:05:52 ET**, HTTP 200, 202,916 B, **9,223 obs**, 1990-01-02 → 2026-09-09. **The run that broke:** the one beginning 9/3, dead at 2. **The bar that broke it:** **9/8 = 148.86**, a published observation of an OPEN session ⇒ **clause 7 RESET**, not clause 6 (missing bar). **Broken clock is DEAD; nothing inherits.** ⛔ Kill on sight: *"FT-10 fired"* — it never has; max ever reached is 2-of-4.
2. **The 9/6 holiday ruling was PROVEN LOAD-BEARING one session after it was written.** 9/7 bridged as a NON-SESSION ⇒ the 9/8 bar sat *inside* the count domain and killed the run **on its value**. Under the rejected reading it dies on the **calendar**, a session earlier. **Same state, different fact — and the fact is what the next grade inherits** (ML-RED-233).
3. **NO WEIGHT MOVED, and the rule is written down:** the registered `ACUTE +2 / MANAGED −2` attaches to a **fire**; a non-fire is the default state and carries no action. Exit leg 0-of-4, 9.25 away. Only the **^SKEW counter-signal display cell** 50/50 → **55/45 bull**. **I did NOT bank "nearly fired and reset" as bull evidence** — that is the FT-01 descriptor defect from the other side.
4. **`boot.py` confirmed on the publisher at the exact path** — line 94 METRIC_MAP `("cboe",…)`, line 98 the declared URL, `cboe_run_length` date-aware. Tonight: `🟡 RED-FT-10 … NEAR live 149.25 [CBOE bar 09/09/2026] vs >=150 (dist -0.75) — run 0-of-4`. **The 9/3→9/6 false 🔴 FIRING is closed.**
5. **RED-23 AMENDED PRE-DATA on LABOR's corrected cut, both vintages readable.** Their "July ranks 44/44" finding is **withdrawn at source**: on first→third — RED's own resolving cut — **July 2026 has NO VALUE at all** (2 vintages exist). **Confidence HELD at 60%: the number did not move, the BASIS did** — off-horizon n=1 → registered **n=39, mean −33.5K, SE 8.8K, t=−3.8, 71.8% down**, plus shown arithmetic (sum needs ≥150K vs 214K ⇒ −64K buffer; only Aug's leg carries a full first→third cut ⇒ **58–71%**). Uncalibrated flag **partially** lifted; **Jul(2→3) and Jun(3→n) legs UNKNOWN and declared, not invented.**
6. **ORACLE recorded: the recession contract is a DISJUNCTION, RED's "unwinnable" branch is FALSIFIED, the row STAYS** (their call). Recorded **against RED's convenience:** leg 1's window reaches back to Q2-2025 into quarters already printed positive ⇒ RED's 4–12% and the 7.0% are **comparable in kind, not in perimeter**. STATUS's *"does not dispute the crowd"* sentence is **qualified, not deleted**.
7. **STATUS rotated under the READ_CAP budget** — 34,679 B (over the 32,550 budget) → **31,915 B, READ-CAP 0 ✅**; two blocks folded **verbatim + crc-stamped** to `reports/2026-09-09_S41-header_S29-reflection_folded.md`, nothing edited.
8. **Rows:** ML-RED-231/232/233 · KB-RED-094/095/096 · FT-10 card cols 8/16/17 · SCAN view regenerated (12 rows, 15,210 B) · `schema_check.py` ✅ · 3 `board_log` dispositions · inbox 3 → **0** (`git mv` to `processed/`).

## NEXT SESSION (dated, priority-ordered)

1. **🔴 THE BOARD BACKLOG — 23 RED-addressed signals undispositioned since 9/6, 2 of them ACTION.** This is boot 1.5's obligation and it was not run tonight. ⚠️ **And do not trust §⑤ to tell you next time:** it is the specified-not-built check from S41 — **not set-difference based, so it will read GREEN while a backlog exists.** Its current 🔴 is informative; a future 🟢 is not.
2. **🔴 FT-10 — next countable bar Thu 9/10; EARLIEST POSSIBLE FIRE Tue 9/15** on `9/10 · 9/11 · 9/14 · 9/15`. **Grade the published bar, read its own DATE, and an unavailable bar is UNKNOWN — never a reset, never a sub-150 bar.** ⚠️ **The publication schedule is STILL UNVERIFIED** (n=3 observed same-day availabilities is not a cadence); both withdrawn claims (`~9/10 earliest grade`, `~18:00–23:00 ET`) **stay withdrawn**. Any miss in the chain resets and pushes the earliest fire out. **The chain runs through Aug CPI 9/11 and lands on FOMC day one 9/15 — noted, NOT registered.**
3. **🔴 Fri 9/11 08:30 ET — August CPI** (FT-08 manual: core 3-mo annualized ≥3.0). **CHG-028: 9/11 is a pre-registered NON-EVENT for oil→core.**
4. **🟠 FT-11 went LIVE 9/9** — BOND routes the F2 read **per operation, never batched**. Also owed: FT-01 6/15-fire outcome grade + FT-06 8/11-fire grade at 20 obs.
5. **🟡 Sat 9/12 VX re-review** (dated CATALYSTS row, starts from 6 of 17) · **Tue 9/15 CHG-044 (BROCK) + CHG-049 (CARL) re-reviews** · 9/15–16 FOMC carries an SEP/dot plot.
6. **📏 `CALENDAR.md` is 28,062 B with an 8/20 HEADER — now the oldest untouched boot-read surface by a wide margin**, and it is the W4 narrative twin of `CATALYSTS.tsv`. Run the mirror check and rotate. **`board_log.tsv` (28,378 B) is rotate-tier too** — flagged tonight, not done.
7. **Carried re-spec:** registry-wide tie/precision audit (both ends, all rows) · FT-04/07/08 re-spec · full-registry ML-203 audit · registry prose split · **and the FT-10 holiday/NON-SESSION reasoning is generic to any sustain counter on an exchange-published daily series — flagged to PROME, still applied to FT-10 alone.**

## OPEN THREADS

- **🔴 Nothing compares `METRIC_MAP` against each row's `instrument_basis`.** FT-10 was mis-wired to the disqualified mirror for four days **with the correct basis written on its own card** — card and code disagreed and **no check reads both**. Specified-not-built since S41; survived S42. This is the single highest-value tooling item RED owns.
- **🔴 The S42 lesson, and it is cheap to state and easy to repeat: a RESET IS A RESULT AND IT HAS AN OWNER.** Two other desks measured 148.86 and four RED surfaces still said "counting 2-of-4." Nothing in the fleet could perform the corrective action — it was one desk's write. `[[finding_record_of_an_action_is_not_the_action]]`.
- **⚠️ FT-10's honest fence, which a reader will drop first:** 6 of the last 20 CBOE bars sit within 1.50 of the 150 line. **"The run broke" is not "the tail bid is gone."** Sustain-4 exists so a two-week camp at 148–151 does not score — and it has not.
- **L272 / ORACLE thread is CLOSED on structure** (disjunction, row stays) but **open on perimeter**: RED's 4–12% and the contract's 7.0% are not the same set. RED's own bucket-projection self-challenge (11–20%, 2–3× the crowd) is **still unresolved** — held 70/30 that the projection is meaningless; **the 30 is not decorative.**
- **LABOR's third-instance pattern is now measured at their desk** (right figures, wrong sentence naming what they are figures OF). **RED's half: RED did not catch the wrong-cut finding** — it was consumed for zero days only because LABOR self-corrected within hours.
- **CHG-RED-027 is 119+ days old**, oldest ACTIVE row; successor (EGBN Q3 ~late Oct) registered, the row itself needs a dated re-review or a close.
- `outbox/kernel/submissions/CMD-01a06273….json` is **IMMUTABLE** — never edit/move/delete; not a boot read.

## PENDING WILL-DECISIONS

- **`AGENTS/RED/CLAUDE.md:241`** still instructs the `LAST_COMPLETION.md` overwrite; PROME says the spec re-keyed 8/13 and again 9/5. **RED declined to act on a peer instruction — a session does not edit its own charter because another session asked.** Authority is Will's. *(Carried unchanged from S41; nothing new tonight.)*
- **Nothing new from S42.** No trade, no $ move, no threshold set or moved, no weight moved.

## GIT STATE (one line)

On master; S42 committed path-scoped from the repo root (`AGENTS/RED/` + carve-out ① packets to VIOLET and `PROME/inbox/`); **DO NOT PUSH — the spawn was instructed to leave the push to PROME**; several desks committing concurrently, so if a push is later attempted a non-ff is routine — root Git Protocol session-end step 3, never force.

---

*S41 block archived in git history; durable outcomes in the registry, workbook, `thesis/CHANGELOG.md` S42 and `MAINTENANCE.md` S42.*
