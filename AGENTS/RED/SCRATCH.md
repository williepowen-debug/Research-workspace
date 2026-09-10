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

## CHANGES SINCE (what moved while RED was offline, 9/9 21:1x → 9/10 15:4x ET)

- **BOND corrected RED's own card before RED booted.** Packet 9/9: FT-11's *"live from 2026-09-09"* was armed a day early — 9/9's op was **Cash Management, 1Mo–2Y**; the first long-end op was **9/10**. BOND, TERRY and RED all carried 9/9 from the same press-release read.
- **The 9/10 long-end operation RAN** (1:40–2:00 PM ET, settles 9/11) and BOND routed the result at 15:39, 2 minutes after RED's spawn.
- **DAEDALUS reviewed L247 and FAILED it** (3 blocking); PROME applied the remedies ~12:2x and routed the **F1 re-check to RED** as the §8 alternate — DAEDALUS declined to grade its own fix.
- **8 new BOARD signals, 6 RED-addressed** (all info-cc). UK 30Y gilt **5.94% [9/10]**, a post-1998 high, is the only one with adversarial bearing.
- Tape at boot: HY OAS **271** (FT-01 FIRING, 3 obs), CCC OAS **1,064** (FT-07 FIRING; WL-05/WL-06 firing), VIX 16.46 (FT-06 NEAR), **SKEW 149.25 [9/9], FT-10 run 0-of-4**, USDJPY 154.32 (WL-12 firing), Brent 107.80.

## WHAT I DID (S43 — PROME Tier-1 spawn, DOCKET L315)

1. **CORRECTED FT-11's arm date 9/9 → 9/10 BEFORE any grading** (the task's explicit order). Five canon fields, superseded text **preserved verbatim** in the `state` cell, `last_reviewed` → 9/10, SCAN view regenerated, `schema_check` ✅. Mirror `docket/CATALYSTS.tsv` row 68 re-dated + **RESOLVED-PARTIAL**.
2. **Found and fixed a defect nobody was looking for:** `scripts/base_rate_review.py` **hardcoded** `" (live from 2026-09-09)"` — the boot surface would have contradicted its own canon at every future boot. Now derives from the row, **fails silent not stale**.
3. **Graded F2 at the Treasury primary myself** (2 fetches, 15:41–15:46 ET) rather than adopting BOND's packet: **OFF-THE-RUN, decisively ⇒ v1.1 ACTIVATES.** BOND's composition reproduced **exactly**; the 40-row detail sums to the ops total **to the dollar**.
4. **Refused to grade the DGS30 leg** — 9/10 official close is not on FRED until ~16:15 ET 9/11. Written on the row as **UNKNOWN**, explicitly **not** carried forward, with the "no substitute source" clause.
5. **Registered 3 contamination flags + 1 confound PRE-DATA, applied NONE as leg changes** (a re-spec is a joint BOND/RED call).
6. **Falsified one BOND claim at the primary** (`total_par_amt_offered` = $10.489B, not null) — which **reverses BOND's own caveat** on the unused $813M. Packeted back with one ask; **no BOND file touched**.
7. **L247 F1 = FAIL.** Broke the remedy with an entry using the letter's four masses **unchanged**. Report + CHG-RED-052.
8. **Drained the whole inbox** (3 packets → `processed/`), **9 board_log dispositions**, workbook rows ML-RED-234…237 / KB-RED-097…099.
9. **Read-cap work I did not plan and should be visible:** `board_log.tsv` had **already breached** the budget before this session (97%); rotated to 24,231 B. `STATUS.md` needed **two** rotation passes → 31,022 B, **READ-CAP 0 ✅**.

## NEXT SESSION (dated, priority-ordered)

1. 🔴 **FIRST, and it is a hard dependency: re-grade FT-11's DGS30 leg at the first boot on/after 2026-09-11 16:15 ET.** The 9/10 official close posts then. Until it does, **v1.1 has an activation date but NO application window** — *"the next non-fired window"* is unidentifiable. **Do not fill the cell from any other source.** Δ5 through 9/9 = +0.0bp (clear).
2. 🔴 **When you do grade it, apply flags A/B/C + the gilt confound to the verdict, not just to the file.** 4 of the 5 sessions in the window ending 9/10 had **no long-end op**; the **30Y sits outside the 10Y–20Y bucket** (accepted maturities stop 2046-02-15); the 1PM 30Y-R auction contaminates the same tape. **The first window wholly inside the program ends 2026-09-16** if ops continue. A 9/10 fire is **weak evidence by construction** — say so on the grade.
3. 🟠 **`STATUS.md` needs ANOTHER rotation** — 31,022 B is **95% of the 32,550 B budget** and the next header breaches it. **`MISSING DATA WANTED` is FOLDED, NOT RESOLVED** (`reports/2026-09-10_S42-S41_status_headers_folded.md`, 1,912 B, crc32 `816405192`) — every item in it is still wanted; re-pull or retire each line.
4. 🟠 **Flag to PROME/WALTER, do not self-fix: the FT-11 SCAN view is at 25,730 B = 79% of WALTER's read-cap budget** (grew 18,447 → 25,730 on this session's append; canon cell now 9.6 KB). **The next comparable append breaches a surface WALTER boot 6b whole-reads.** RED owns the canon, WALTER consumes the view — this needs a joint call (hot/cold split of the state cell?), not a unilateral RED restructure.
5. 🟡 **BOND owes one answer** (packet 9/10): is there a published acceptance rule bounding fill independently of price? Without it, *"Treasury declined prices"* stays **INFERRED** — the mechanical alternative is `max_nbr_offers: 9` / `par_amt_per_offer: $1,000,000` binding. **Do not upgrade the inference on silence.**
6. 🟡 **L247: no code before PASS, and RED delivered FAIL.** If PROME returns a revised §4, the remedy to check is **ruled-bytes `outcome_map_sha256`** + **every vocabulary label carrying ≥1 branch** + **masses inside the ruled bytes**. ⚠️ **Watch for a prose parser appearing in the build** — §6 test 3's `(b)↔(d)` negative *pressures* the builder toward one, and §1a/§2 forbid it.
7. 🟡 **DUE at W2 next session** (carried, not resolved today — out of L315 scope): CHG-RED-027 (120d), CHG-RED-044 (41d), CHG-RED-045 (29d), CHG-RED-049 (14d), CHG-RED-051 (14d, SELF-APPARATUS). **CHG-051 is the apparatus self-challenge and this session just generated two apparatus findings for it (ML-RED-234/235).**
8. 🟡 **FT-01 has been FIRING 3-of-3 at HY OAS 271** and FT-07 FIRING at CCC 1,064 — both flagged 🔴 by `boot.py` every boot. Confirm these are dispositioned states and not unresolved fires.
9. ⚪ **`base_rate_review` 🔴 on FT-10** (recorded 0.8% vs 120-obs 0.0%) and 🟠 FT-06 (1.6×) — selectivity credentials to re-review, **not** thresholds to re-cut.

## OPEN THREADS

- **FT-11's DGS30 leg is a KNOWN OPEN CELL, deliberately left open.** Anything reading FT-11 before 9/11 16:15 ET sees an activated v1.1 with no application window. That is correct state, not an omission.
- **The arm date lived in EIGHT sites** (5 registry fields, 1 tool literal, 1 docket row, 1 STATUS/CALENDAR narrative pair). **A scan keyed on the registry alone would have reported the fix complete while the boot tool printed the dead date.** Assume the next such correction is also 8-site.
- **Preserving superseded text created a scanner hazard** — the dead date now lives on the row inside a quoted block, and any `live from <date>` regex can pick it. Handled by taking the **first** match in the operative cell. **Any future scanner over this row must know that.**
- **`CALENDAR.md` was NOT updated this session** (28,062 B, 52% of cap; the mirror-check obligation at W4 is discharged for `CATALYSTS.tsv`, which is canonical). Its 8/20 "Last Updated" stamp is **21 days old** and its narrative still frames the buyback as an 8/19 doubling — **re-read or restamp it next session** (discipline overlay: a dated stamp is a trigger, not a shield).
- **YCC-lite stays un-adjudicated at n=1.** The 8/19 rejection is neither re-opened nor re-confirmed by 9/10's composition, which is *consistent with* it.
- **CHG-RED-052 is RESOLVED same-day** (FAIL delivered), so it will not appear in the DUE-scan. Its follow-on lives in NEXT SESSION #6, not in `CHALLENGES.tsv`.

## PENDING WILL-DECISIONS

- **None from RED.** $0 moves, no trade proposals, no weight moves this session — nothing on this card needs Will.
- Two items are **PROME-facing, not Will-facing**: the SCAN-view read-cap call with WALTER (NEXT SESSION #4) and whether the 9/11 FT-11 re-grade gets its own DOCKET row.
- ⚠️ One **fleet-wide** item RED raised in `OUTBOX.md` §2 for PROME to weigh: **a sweep of the fleet's boot tools for reported-but-unread literals.** RED found one in its own; the class is not RED-local.

## GIT STATE

Committed path-scoped to `AGENTS/RED/` + the two carve-out ① packets (`PROME/inbox/`, `AGENTS/BOND/inbox/`). **NOT PUSHED — PROME serializes the push** (explicit spawn instruction). Tree was dirty at boot in BOND/DEWEY/PROME/`memory/` paths, so **no pull was attempted** (root Git Protocol "Before pulling" step 2).
