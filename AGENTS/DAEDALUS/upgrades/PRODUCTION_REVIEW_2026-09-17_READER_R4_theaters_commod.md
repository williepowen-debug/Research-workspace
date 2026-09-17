# PRODUCTION REVIEW #6 — READER R4 (war theaters / commodities / power / semis)

**Reader:** DAEDALUS fan-out reader R4 · **Date:** 2026-09-17 (Thu) · **Review period:** 2026-09-01 00:00 → now
**Cohort:** HAWK · FALCON · OSPREY · MIDAS · FERT · WATT · VULCAN
**Baseline commit for all period diffs:** `e6fc35eafe6097c02dc4e049a20d029b22d8ebd4` (last commit before 2026-09-01 00:00)
**Read-only pass.** Every claim below carries a `path:line` or a commit hash. Where I could not ground a verdict I wrote NOT-ADJUDICATED or CANNOT-EVALUATE rather than guessing.

---

## HAWK — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-01

### 1. Period production
84 commits touch `AGENTS/HAWK/` since 9/1 — **24 self-authored, 60 routed-in** (subject prefixed by another desk). Last self-commit **2026-09-17** (today); **dark-days 0**.
What shipped: the 9/8 catch-up battery (`54accb874` implement approved catch-up controls; `a0763c0cd` repair boot continuity; `e50b97f2c` batch2 rule proposals + measurement contracts), the WQ-160 HAW-19 LEG-A repair (`3b0d54de0`, ≥45d → ≥14d, `Resolve_By` held), the WQ-208/211/212 encodings (`6fd24c71e`), and today's commissioned cross-war oil synthesis (`b28680b9e` + delivery `584283c5c`). New build: `AGENTS/HAWK/scripts/derived_freshness.py` (117 lines, born `54accb874`). Tree delta **218 files, +18,397 / −782**.

### 2. Row-claim test (`Gaps` + `Next_upgrade`)

| # | Claim in the row | Verdict | Locator |
|---|---|---|---|
| 1 | "September 8 owner work ongoing; prior dark-since claim withdrawn" | **TRUE-STILL** (and understated — 24 self-commits since, through today) | `git log --after=2026-09-01 -- AGENTS/HAWK/` |
| 2 | "Owner **defers structural freshness checker**" | **REFUTED** — it was BUILT on the same 9/8 day, and updated today | `AGENTS/HAWK/scripts/derived_freshness.py:1-19`; commits `54accb874` (9/8), `b28680b9e` (9/17); wired at "HAWK CLAUDE boot 6a-3 and closeout 13b" (`derived_freshness.py:4`) |
| 3 | "Owner defers **KB-238 instruction propagation**" | **REFUTED** — propagated into the instruction file 9/8 | `AGENTS/HAWK/CLAUDE.md:29` ("Reconcile by belligerent dyad… KB-HAWK-238"); commit `a0763c0cd` (2026-09-08), confirmed by `git log -S "KB-HAWK-238" -- AGENTS/HAWK/CLAUDE.md` |
| 4 | "As-made audit: four candidates, three false matches, one two-vintage HAW-18 decision; 14 NOT-FOUND remain unverified" | **CANNOT-EVALUATE** on the 14 NOT-FOUND (no surface enumerates them); the **HAW-18 decision leg is DISCHARGED** | `AGENTS/HAWK/thesis/FALSIFICATION.md:9` — "WQ-208 (HAW-18's scored mark is the 55%)", Will-ruled 2026-09-10 |
| 5 | "Current tree active; no broad completion or regrade asserted" | **TRUE-STILL** | — |
| 6 | NEXT: "Full profile refresh and current ladder assessment at PR6" | **DUE NOW** — this section discharges the ladder half; the profile refresh is **NOT DONE** (see §4) | `AGENTS/DAEDALUS/profiles/HAWK.md:5` |
| 7 | NEXT: "HAW-18 scoring decision with PROME/Will September 11 before H2 September 14" | **DISCHARGED EARLY** — ruled 2026-09-10, one day ahead | `AGENTS/HAWK/thesis/FALSIFICATION.md:9` |
| 8 | NEXT: "Do not impose redesign on the active owner session" | **TRUE-STILL** and still the right instruction — the desk ran 6 sessions in the period | — |

**Row verdict: 2 REFUTED / 4 TRUE-STILL (2 discharged) / 1 CANNOT-EVALUATE.** The two REFUTED cells are 9 days stale and both point the same way: the row records deferrals the owner had already closed **in the same commit the row was written from**.

### 3. Ladder walk — Market class, at L4 (current) and L5 (next)

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L4 | TRADE.md feeding proposals | **NOT MET — and N/A by charter, never formally waived** | `AGENTS/HAWK/STATUS.md:2` "No trade book"; `AGENTS/DAEDALUS/profiles/HAWK.md:11` "Holds no trade book." No `AGENTS/HAWK/TRADE.md` exists |
| L4 | Signals flowing | **MET, decisively** | `584283c5c` "HAWK -> BRENT, WALTER, PROME: cross-war synthesis packets + NEXUS brief pinned to b28680b9e" (9/17); inbound consumption receipts `de40a30c8`, `e411f228a` (BRENT), `ba3898d86` (OSPREY) |
| L5 | Clean closeouts | **NOT MET** | Two outside-desk corrections routed into HAWK's tree inside the period: `de40a30c8` "BRENT -> HAWK: recover full pipeline restart source and bound sales evidence" and `e411f228a` "BRENT -> HAWK: identify consumed cross-war baselines" (both 9/16). Also `AGENTS/HAWK/thesis/FALSIFICATION.md:19` — HAW-19 LEG A was **structurally unfireable for the first 21 of the row's 42 days**, ruled a DEFECTIVE INSTRUMENT with no calibration credit (WQ-212) |
| L5 | Zero YEYOU flags | **NOT-ADJUDICATED — the instrument cannot fire** | YEYOU retired 2026-09-05 (WQ-181 ①); `AGENTS/DAEDALUS/CLAUDE.md` § AUTHORITY box: the leg is "a default-zero instrument that can never fire (PAT-060)" |
| L5 | Current | **MET** | last self-commit 2026-09-17 |

**Recommendation: HOLD L4, confidence H.** I read the deciding artifacts myself. L5 is blocked on *clean closeouts*, not on staleness — and the block is real rather than bookkeeping: an open prediction spent half its window unfireable and two correction packets arrived from a peer desk in the last 48 hours of the period. The `Gaps` cell should be re-cut: it currently names two deferrals that no longer exist.

### 4. Profile trigger

> **Vintage:** `profiles/HAWK.md:7` — "**FULLY REBUILT:** 2026-08-07 eve"
> **Trigger:** `profiles/HAWK.md:7` — "refresh when **EXIT_PROTOCOL.md gains a stamp of ANY kind — rewrite OR freeze**, when the **dormant book gains/loses a row**, or when a **FLOW-HAWK-19/20 in-row stamp changes** — whichever first."
> **Banner:** `profiles/HAWK.md:5` — "⚠️ STALE — TRIGGER FIRED, unserviced (PR#5 2026-09-01) … Refresh checkpoint: **2026-09-15**."

**Verdict: FIRED — on two independent legs — and the 9/15 checkpoint has also passed unserviced (2 days).**
- **FLOW-HAWK-19/20 in-row stamps changed** in the period, and a **new row FLOW-HAWK-21 was added**: `git diff e6fc35eaf..HEAD -- AGENTS/HAWK/workbook/FLOW.tsv` shows both `FLOW-HAWK-19` and `FLOW-HAWK-20` rows rewritten plus `FLOW-HAWK-21` ("Chokepoint ton-miles -> freight INDEX -> listed tanker/gas-carrier EQUITY") inserted.
- **Dormant book changed**: `AGENTS/HAWK/workbook/VX.tsv` now carries **11 data rows** (+23 lines of diff in the period).

**Profile statements now FALSE (the PR6 ask):**

| # | Profile statement | Live state | Locator |
|---|---|---|---|
| a | Δ-block ② "**Falsification VACUUM is the live state**: frozen rail + HAW-18 RESOLVED-FAILED eff. 8/4 + **0 OPEN predictions** = no live instrument" | **FALSE on all three limbs.** A dated successor surface exists and was refreshed **2026-09-16**; **2 OPEN** predictions (HAW-19, HAW-20); K2's instrument was **repaired 9/10** under WQ-160 and the row "tests its own headline claim" again | `AGENTS/HAWK/thesis/FALSIFICATION.md:3` (born 8/20), `:7` ("Refreshed: 2026-09-16"), `:19` (K2 "LIVE AGAIN — REPAIRED 2026-09-10") |
| b | Δ-block ⑤ "**STATUS 152 ln** (cap ≤120)" | **FALSE — 63 lines / 8,827 B (27% of the 32,550 B read cap).** The over-cap defect is fixed | `AGENTS/HAWK/STATUS.md` (63 ln) |
| c | Δ-block ⑥ "**KB 270 ln → KB-HAWK-266**" | **FALSE — 381 lines, newest `KB-HAWK-377`** (111 rows later) | `AGENTS/HAWK/workbook/KB.tsv` tail |
| d | Δ-block ③ "**Dormant book = 10 rows**" | **FALSE — 11 data rows** | `AGENTS/HAWK/workbook/VX.tsv` |
| e | **Internal contradiction**: "Identity in one line" says "a **9-row** dormant book" while Δ-block ③ in the same file says "**10 rows**" | Both are wrong now, and they were **mutually inconsistent when written** — the profile carries two different counts of the same object on two adjacent screens | `profiles/HAWK.md:11` vs `profiles/HAWK.md:9` |
| f | Δ-block ⑦ "NEXUS_BRIEF fold-goes-LAST ADOPTED (:76)" | **CANNOT-EVALUATE** — a bare line anchor into a file that edits itself; `:76` no longer identifies the claimed text. This is the exact dangling-anchor class OSPREY's rail already documented (`AGENTS/OSPREY/CLAUDE.md:144`, "Cite the SECTION, not the line") | `profiles/HAWK.md:9` |
| g | Δ-block ⑨ "PAT-051 stands (zero self-initiated sessions)" | **TRUE-STILL** — every period session traces to a PROME/Will commission (`e4b198a71` PROME -> …, `b28680b9e` "commissioned cross-war oil synthesis") | — |

**The profile's own class line, "cross-war SYNTHESIS + dormant geopolitical book … sunset STOOD DOWN 8/3", is still accurate.** What has rotted is every *quantity* in it. That is the shape worth naming: the Δ-block was written as a rescue for a stale body and has itself become the stale layer — **six of its nine numbered corrections are now wrong**, while the qualitative identity paragraph above it survived untouched.

### 5. Falsification read
**Not in scope** (HAWK is neither scanner-flagged nor on the no-thesis-file list). Noted anyway because it bears on §3: `AGENTS/HAWK/workbook/EXIT_PROTOCOL.md:3` is correctly **🧊 FROZEN 2026-08-10** with a prescriptive-voice danger banner, and the live rail is `thesis/FALSIFICATION.md`. The 8/20 split is clean and the frozen file says so loudly.

### 6. Negative-resolution leg
**Opened:** `AGENTS/HAWK/thesis/PREDICTIONS.tsv` (21 rows: 6 CONFIRMED / 9 FAILED / 1 PARTIALLY / 1 VOIDED / 2 REHOMED / **2 OPEN**).

| Row | Negative-class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **HAW-19** | **YES** — "BOTH legs unfired at 2026-09-30 = CONFIRMED" | **YES** — three named: (1) FALCON's and OSPREY's ledgers, (2) CENTCOM's enforcement tally at its own account, (3) a Kpler-or-Vortexa flow check | **YES** — "CONFIRMED requires a **logged, dated pull**… CONFIRMED must mean 'I looked and found nothing', never 'I did not look'" (fleet convention ratified by Will 2026-08-17) |
| **HAW-20** | **YES** — "Through 2026-10-31, **NO instrument** on the cross-theater codification axis moves DOWN a status step" | **YES** — Federal Register + USTR docket (a,b); US CIT/CAFC docket for injunctions; Majlis records or IRNA/Fars (c); signatory foreign-ministry statements (d) | **YES** — "'No softening found' is only admissible with **the pull logged and dated**" |

**Counts: 2 candidates opened / 2 confirmed negative-class / 0 lacking instrument / 0 lacking a dated precondition.** Both rows also name their **ANCHOR TYPE: IMMOVABLE** in-cell, citing `finding_resolver_anchored_to_expected_event_inherits_slip_risk`. This is the best negative-resolution hygiene in the cohort.

### 7. As-made receipt
**n/a** (HAWK is not MARCO/REGINALD/HENRY).

### 8. Cross-agent threads / pattern candidates
- **To PROME:** HAW-19 resolves **2026-09-30** as a ruled DEFECTIVE INSTRUMENT with no calibration credit, and its **capacity-only successor was owed by 2026-09-25 (DOCKET L321) and is "NOT YET REGISTERED and not ready on data"** — `AGENTS/HAWK/thesis/FALSIFICATION.md:19`. That is **8 days out** and is the only thing standing between this desk and a fresh 0-OPEN-calibration gap after 9/30.
- **PATTERNS candidate:** *A Δ-block written to rescue a stale profile becomes the stale layer, and it rots faster than the body it rescued* — evidence: `profiles/HAWK.md:9`, six of nine numbered corrections now false after 33 days, while the qualitative body above survived. The corollary is the actionable half: **a correction block should carry pointers, not counts**; counts are what rot.

### 9. Reviewer-side defects
- The `Gaps` cell asserted two owner deferrals (`derived_freshness.py`, KB-238 propagation) that **the same 9/8 session had already closed**. Both were verifiable at the artifact on the day the row was cut.
- `profiles/HAWK.md:9` shipped with an internal contradiction (9-row vs 10-row dormant book) on the day it was written.

---

## FALCON — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-01

### 1. Period production
76 commits, **31 self-authored / 45 routed-in**. Last self-commit **2026-09-16**; **dark-days 1**.
Shipped: `thesis/THESIS.md` rewritten (+179/−…), `workbook/EXIT_PROTOCOL.md` amended three times (9/07, 9/08, 9/10), the D 75→85 rung REGISTERED by Will 9/8, six dated `reports/` (gate2-kylo 9/7, theater-catchup 9/8, petroline-tell2 9/11 ×2, gate-review 9/14, cross-war 9/16), and **FAL-05 registered 9/7**. Two self-corrections of pushed work: `5e91d4170` (9/10, timestamps re-stamped from the clock, WALTER-caught) and `c4b8c83b9` (9/11, "external review found 5 wrong claims in pushed work — corrected across 16 surfaces").

### 2. Row-claim test
The `Gaps` cell is a 9/1 RE-CUT and is now the **most stale row in the cohort** — every live blocker it names has been discharged.

| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | "the prior Next_upgrade premise ('VX-FALCON-SUNK-01 ABSENT') was FALSE when written" | **TRUE-STILL** (correct self-indictment, retained) | — |
| 2 | "**L5 NOT reachable** — YEYOU STATE.tsv Open_Findings=1 (YEY-002, STATUS **253 lines** over own 250 cap; still 253 at 9/1)" | **REFUTED twice over.** STATUS is **70 lines / 9,019 B**, far inside the desk's own 250-line cap. And the instrument itself is retired | `AGENTS/FALCON/STATUS.md` (70 ln); cap at `AGENTS/FALCON/CLAUDE.md:96` and `:143`; YEYOU retired 2026-09-05 (WQ-181 ①) |
| 3 | "**EXIT_PROTOCOL.md rewrite trigger DOUBLY FIRED and unrewritten** (:3 still 'REWRITTEN 2026-07-30')" | **REFUTED — serviced, and the desk says so in DAEDALUS's own words.** `:3` now reads "REWRITTEN 2026-07-30 · **AMENDED 2026-09-07** (this is the RE-STAMP DAEDALUS PR#5 item 1 demanded)… TOUCHED 2026-09-08… **AMENDED 2026-09-10**" | `AGENTS/FALCON/workbook/EXIT_PROTOCOL.md:3`, `:6` |
| 4 | "§2 dated-rail defect stands (column header + one in-cell date)" | **CANNOT-EVALUATE** — §2 was rewritten on 9/8 when Will registered the D→85 rung; the specific header/in-cell defect is not separable from the rewrite without the original packet text | `AGENTS/FALCON/workbook/EXIT_PROTOCOL.md:49` |
| 5 | "**FAL-05 successor OWED** — grep '^FAL-05' = 0, the ledger has read 0 OPEN since 8/20" | **REFUTED** — FAL-05 registered **2026-09-07**, 30-day window 9/07→10/07, currently the desk's 1 OPEN row | `AGENTS/FALCON/thesis/PREDICTIONS.tsv` FAL-05 (Status=OPEN) |
| 6 | "**Lowest self-ratio in cohort (7 self / 32 inbound)**" | **REFUTED** — 31 self / 45 routed = **41% self, second-highest in the cohort** after VULCAN | period `git log` |
| 7 | "Profile: no dated trigger, Δ 8/15, 17d — DAEDALUS lane" | **TRUE-STILL, and worse** — now Δ+33d and the 9/15 refresh checkpoint has passed | `profiles/FALCON.md:3` |
| 8 | NEXT: "L5 on: STATUS ≤250 + EXIT_PROTOCOL REWRITE + FAL-05 registered" | **ALL THREE NOW MET** (see 2, 3, 5) | as above |

**Row verdict: 4 REFUTED / 2 TRUE-STILL / 1 CANNOT-EVALUATE — and all three named L5 gates cleared.**

### 3. Ladder walk

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L4 | TRADE.md feeding proposals | **NOT MET — N/A by charter, never formally waived** | `profiles/FALCON.md:9` — "this is why there is deliberately **no TRADE.md**/CALENDAR.md (CLAUDE:7, :330)" |
| L4 | Signals flowing | **MET** | `7947d0654` "FALCON -> HAWK, BRENT, PROME, WALTER: deliver oil review and YASREF disposition" (9/16); rung ruling consumed by PROME/Will 9/8 |
| L5 | Clean closeouts | **NOT MET — and this is now the only blocker** | `c4b8c83b9` (2026-09-11) "**external review found 5 wrong claims in pushed work** — corrected across 16 surfaces"; `5e91d4170` (2026-09-10) "re-stamp all 9/10 times from the clock — the narrative ran ~1h ahead (**WALTER-caught**)"; and `EXIT_PROTOCOL.md:60` — a 9/8 annotation ("NO SECOND SINKING") that "**was FALSE when written**… only a WALTER dispatch surfaced it" |
| L5 | Zero YEYOU flags | **NOT-ADJUDICATED — instrument retired, cannot fire** (PAT-060) | WQ-181 ① |
| L5 | Current | **MET** | last self-commit 9/16 |

**Recommendation: HOLD L4, confidence H.** The three gates the row named are discharged, so the row's stated L5 path is spent — but the ladder's own *clean closeouts* leg is independently REFUTED by three outside-caught defects in pushed work inside 48 hours (9/10–9/11). **The row needs a re-cut regardless of the grade**: it currently blocks L5 on a 253-line STATUS that is 70 lines and on a rail rewrite that happened three times.

⚠️ **Worth recording in FALCON's favour:** the desk **found and published its own** rail defects rather than absorbing them — `EXIT_PROTOCOL.md:80` states plainly that the trigger "fired on 8/20 and again on 9/1 and **neither was noticed by any FALCON boot step** — it took an OUTSIDE desk (DAEDALUS PR#5) to surface it. **Boot has no check that reads this line. Building one is owed.**" A desk that writes its own missing-guard into its own rail is doing the L5 behaviour even while failing the L5 leg.

### 4. Profile trigger

> **Vintage:** `profiles/FALCON.md:5` — "**Built:** 2026-08-07… **Staleness:** work-volume-keyed (PAT-085) — **trigger FIRED 8/15**"
> **Banner:** `profiles/FALCON.md:3` — "⚠️ **NO DATED STALENESS TRIGGER (PR#5 2026-09-01)**: this profile names no day clock or floor, so `scripts/profile_clock_check.py` reports it NO-DATED-CLOCK and cannot certify it. Add one at the next refresh (checkpoint **2026-09-15**)."

**Verdict: CANNOT-EVALUATE by construction** (there is no dated trigger to test) — **plus the 9/15 checkpoint has passed, unserviced.** The work-volume key **did** fire: the period ran 31 self-commits across ≥7 sessions, including two heavy Will-active sittings (9/8 rung ruling, 9/11 external review).

**Profile statements now false:**
- `profiles/FALCON.md:7` Δ-block ② "`domain/vessel-incidents/VESSELS.tsv` (19 rows/20 cols… **currently outside the `ledger_staleness` workbook glob, nothing reads it**)" — **now load-bearing**: `EXIT_PROTOCOL.md:49` resolves the Hercules Star and Al-Salmi rulings *at* `VESSELS.tsv` (`VI-2026-0030`, `VI-2026-0033`). The file went from unread to a rail's pre-committed resolver in 33 days, and it is still outside the glob.
- `profiles/FALCON.md:9` "owner of the fleet's **reference dated falsification rail** (EXIT_PROTOCOL.md, **REWRITTEN 2026-07-30**)" — the parenthetical date is 48 days stale; the file has three amendment stamps since.
- `profiles/FALCON.md:7` Δ-block ③ "twice-refuted first-fatality claim live in the rail §3.5 AND `VX.tsv:6`" — **CANNOT-EVALUATE**; `VX.tsv` changed 19 lines in the period and a bare line anchor no longer resolves.

### 5. Falsification read
**Not in scope** (FALCON is on neither list). Observed in passing: FALCON's rail is the healthiest in the cohort — `EXIT_PROTOCOL.md:80` records that the 9/10 trigger fire was "**the first time this file's dated trigger has been caught inside the session the leg fired**, rather than by an outside desk six days late," and then adjudicates *rewrite-not-due* **in writing, with reasons, "so the next reader can overrule it rather than re-derive it."** That sentence is the shape every dated rail should copy.

### 6. Negative-resolution leg
**Opened:** `AGENTS/FALCON/thesis/PREDICTIONS.tsv` (2 FAILED / 1 CONFIRMED / 1 PARTIALLY / **1 OPEN**).

| Row | Negative-class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **FAL-05** | **YES** — "**No NEW** confirmed loss of Gulf-ally or Iranian CRUDE/CONDENSATE supply to market between 2026-09-07 and 2026-10-07" | **YES** — a three-branch RESOLVABILITY GUARD names **Kharg Island loading state** as "the named leg that must be AFFIRMATIVELY closed at window close", with routes (a) operator/state force majeure, (b) ≥100 kbpd offline ≥7 consecutive days *actually elapsed*, (c) named-source attribution | **PARTIAL — the one gap in the cohort.** The guard fixes an *affirmative-evidence* obligation at window close (10/07) but sets **no dated floor or ceiling** for the search itself, which is exactly the defect OSP-04 documented and OSP-06/FERT-12 then fixed with an explicit window |

**Counts: 1 candidate opened / 1 confirmed negative-class / 0 lacking instrument / 1 lacking an explicit dated search-attempt window.**
⚠️ Mitigation, stated fairly: FAL-05's guard is *stronger* than a bare attempt-log in one respect — it demands **affirmative evidence of continuation**, not merely a failed search, and it has "**NO VOID PATH (HAW-07)**". The gap is narrow and mechanical: borrow OSP-06's dated ceiling.

### 7. As-made receipt — **n/a**

### 8. Cross-agent threads / pattern candidates
- **To PROME (routed by FALCON, confirm it landed):** `EXIT_PROTOCOL.md:49` ⑤ — the base rate disclosed at the D→85 registration, "**(c) 0 in 193 days**", is **FALSE**: the Al-Salmi (a laden 2M-bbl KPC VLCC) was struck by an Iranian drone at Dubai Port 2026-03-31. "**A 193-day absence asserted from a 59-day-blind instrument**" (`VESSELS.tsv` perimeter starts 2026-07-11). The letter is immutable and untouched; the corrected rate is ≥1 in 193 days.
- **PATTERNS candidate (strong):** *A base rate computed from your own ledger inherits that ledger's perimeter, and the perimeter is invisible in the resulting number.* Evidence: `EXIT_PROTOCOL.md:49` ⑤. This is a sharper, self-caught instance of `finding_instrument_measures_a_superset_of_the_thesis_subject` running the other way — a **subset** instrument producing a confident absence.
- **To DAEDALUS/PROME:** `EXIT_PROTOCOL.md:80` — "a fired trigger with no owner-visible affordance rots… **Boot has no check that reads this line. Building one is owed.**" This is a named, owner-requested build sitting unassigned. It is also the generalisable fix for `finding_dated_carry_item_has_no_expiry_check`.

### 9. Reviewer-side defects
- **The FALCON row is the cohort's worst rot case.** All three Next_upgrade gates were discharged 9/7–9/10 and the row still names them. Its `Gaps` cell also asserts "7 self / 32 inbound" — wrong by a factor of 4 as of today.
- **DAEDALUS's own 8/7 promotion record is defective.** `upgrades/PRODUCTION_REVIEW_2026-08-07.md:15` promotes FALCON L3→L4 with the blanket phrase "**all legs cleared by more than asked**" — but FALCON has **no TRADE.md by charter**, so the L4 "TRADE.md feeding proposals" leg cannot have cleared. The leg was not enumerated; it was absorbed. This is precisely the omission the Meta-L5 note in `AGENTS/DAEDALUS/CLAUDE.md` was written to forbid ("Promotion adjudications should enumerate EVERY ladder leg with a per-leg verdict so a skipped leg reads as a blank, not an omission"). See the cohort-level finding below.

---

## OSPREY — Market · FLEET_MAP L2 / Conf H / last_scored 2026-09-01

### 1. Period production
42 commits, **19 self-authored / 23 routed-in**. Last self-commit **2026-09-16**; **dark-days 1**.
Shipped: `scripts/strike_feed.py` (245 lines, built 9/8, diff-rule v2 9/10), `strike_feed_config.json` (154 lines), `thesis/THESIS.md` **v1.0** (first owner-written version, 9/8), `PLAN_2026-09-08_remediation.md`, the §1b downgrade path RULED IN FORCE, and a fully evidenced cross-war research bundle (`research/2026-09-16_cross-war-oil/` — REPORT + VALIDATION + `collect.py` + `retrieval.json` + `source_hashes.json` + both consumer_check outputs).

### 2. Row-claim test

| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | "September 8 owner resumed work and supplied strike-feed proposal" | **TRUE-STILL** | `2a2ae41e4` (9/8) |
| 2 | "**No strike_feed.py build verified**" | **REFUTED** — built 9/8, improved 9/10, wired into boot | `AGENTS/OSPREY/scripts/strike_feed.py` (15,323 B); `2a2ae41e4` "strike feed built, first run finds Kstovo 8/26 + Novorossiysk 9/9"; `e5fadbdc8` (9/10) "diff rule v2 — false absorption 15.2% → 2.0%"; wired at `AGENTS/OSPREY/CLAUDE.md:37` boot step 5b(iv) |
| 3 | "**Phase 1.1 explicitly awaits item-specific authorization**" | **REFUTED** — authorized in-session | `AGENTS/OSPREY/PLAN_2026-09-08_remediation.md:24` — "**RULED DIRECTLY BY WILL 2026-09-08 ~23:0x ET, in-session, verbatim *'all approved go ahead'*** — 1.1 built by OSPREY the same night" |
| 4 | "Six design questions captured in `design/2026-09-08_OSPREY_STRIKE_FEED_INTAKE.md`" | **TRUE-STILL** (file present, superseded by the ruling) | — |
| 5 | "Full profile stale; existing relative >21d trigger contradicts the old no-trigger assertion" | **TRUE-STILL** | `profiles/OSPREY.md:3` vs `:5` |
| 6 | NEXT: "Review spec September 12; build only after authorization" | **OVERTAKEN** — authorization came 9/8, build followed the same night; DAEDALUS reviewed on 9/10 | `e5fadbdc8` commit subject "(DAEDALUS review)" |
| 7 | NEXT: "**Revisit tool-specific L3 dependency at September 14 ladder sitting**" | **DUE — discharged here** (see §3) | — |
| 8 | NEXT: "full profile checkpoint September 15" | **MISSED** — 2 days overdue | `profiles/OSPREY.md:3` |

**Row verdict: 2 REFUTED / 3 TRUE-STILL / 3 overtaken-or-due.** The row was cut 9/1 and the desk cleared its two blockers on 9/8; the row is 9 days behind the artifact.

### 3. Ladder walk — the PR6 ask: are the L3 legs now met?

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L2 | Structured record, valid schema, accruing | **MET** | `workbook/KB.tsv` (+131 lines in period), `VX.tsv`, `FLOW.tsv`, `WARRISK.tsv`, `SCHEMA.tsv`; `domain/energy-strikes/STRIKES.tsv` 98,103 B |
| **L3** | **Convergence matrix** | **MET** | `AGENTS/OSPREY/STATUS.md:22-27` — THREE-CHANNEL DASHBOARD: per channel score · mark state · upgrade test · **clock / downgrade test**, each with a numbered clock (1/30, 7/30, 12/21) |
| **L3** | **Exit rules** | **MET, and RULED** | `AGENTS/OSPREY/CLAUDE.md:142` § EXIT RULES; **§1b downgrade path in force** after the objection window closed with no objection from either consumer — `AGENTS/OSPREY/STATUS.md:42` (HAWK packet 9/10; **BRENT verified at its own `board_log.tsv` 9/10 12:06** — "the absence of a reply is EXPLAINED, not merely observed"); record `domain/energy-strikes/L308_DOWNGRADE_WINDOW_CLOSED_2026-09-15.md` |
| **L3** | **Predictions resolving** | **MET** | `thesis/PREDICTIONS.tsv`: **2 CONFIRMED / 3 FAILED / 1 OPEN**, with a calibration read, not just a count ("OSP-02 and OSP-03 were correctly calibrated; OSP-01 was not"). OSP-04 resolved 9/2, OSP-05 FAILED, OSP-06 registered 9/2 |
| **L3** | **Dated falsification surface** | **MET** | `AGENTS/OSPREY/CLAUDE.md:144` — "**Kill rail re-derived: 2026-08-15; re-read 2026-09-08; RULED 2026-09-08** (Will: geography qualifier §1, downgrade path §1b, re-centre withdrawn §5, buyer-pullback limb retired to Channel 2)", with per-section clock readings (§1 C1 0/30 · C2 7/30 · C3 4/21) and a **30-day standing re-read rule** at `CLAUDE.md:198` |
| L4 | TRADE.md feeding proposals | **NOT MET — N/A by charter** | No `AGENTS/OSPREY/TRADE.md`; `thesis/THESIS.md:21` — "**BRENT owns every price** (Brent, cracks, freight, floating storage, Urals)" |
| L4 | Signals flowing | **MET** | `ba3898d86` "OSPREY -> HAWK, BRENT, PROME, NEXUS: refresh Russia oil evidence and consumed baseline" (9/16); consumption verified at BRENT's own `board_log.tsv` (`STATUS.md:42`) |

**Recommendation: PROMOTE L2 → L3, confidence H.** Every L3 leg is MET and I read each deciding artifact myself. The two things the 9/1 row held OSPREY at L2 for — *no strike_feed build* and *Phase 1.1 awaiting authorization* — were both closed on 9/8 by Will's direct in-session ruling.

⚠️ **L4 is one leg short and the missing leg is the charter-exempt one.** OSPREY meets "signals flowing" as decisively as FALCON does and has no TRADE.md for the same reason FALCON has none. I am **not** recommending L4 here, because promoting on a leg that has never been formally waived would repeat the 8/7 FALCON defect rather than fix it. **The waiver question belongs at the ladder sitting, not in a reader's report** — see the cohort-level finding.

### 4. Profile trigger

> **Vintage:** `profiles/OSPREY.md:5` — "**Built:** 2026-08-07"; receipt-updated 9/8 (`:3`)
> **Trigger:** `profiles/OSPREY.md:5` — "re-read when THESIS v0.2 lands, when the ~8/20 Channel-3 kill clock resolves, or **when STATUS's stamp leads this vintage >21d**"
> **Banner:** `profiles/OSPREY.md:3` — "⚠️ NO DATED STALENESS TRIGGER… checkpoint **2026-09-15**"

**Verdict: FIRED on the THESIS leg; NOT FIRED on the 21d leg; checkpoint MISSED.**
- **THESIS leg FIRED and overshot**: the trigger names "THESIS v0.2"; what landed on 9/8 is **v1.0**, a full first owner-written version superseding the v0.1 seed — `thesis/THESIS.md:1,3`. The trigger fired on a bigger event than it was written for.
- **21d leg NOT FIRED**: STATUS stamp 9/16 vs profile vintage 9/8 = 8 days.
- **Checkpoint 9/15 MISSED** by 2 days.

**Profile statements now false:**
- `profiles/OSPREY.md:3` and `:5` **contradict each other on the same screen** — the 9/8 receipt says "its existing >21d relative trigger is real, **despite the older no-trigger banner below**," and the no-trigger banner is still sitting below it, unretracted. Two live instructions where there should be one (`finding_correction_beside_an_instruction_leaves_two_live_instructions`).
- `profiles/OSPREY.md:7` Δ-block ⑤ "**THESIS.md still v0.1** — bannered 8/15 (good banner, NO clock; v0.2 registration pending)" — **FALSE**, v1.0 landed 9/8.
- `profiles/OSPREY.md:7` Δ-block ⑧ "**L3 promotion review owed at next touch**… verify OSP-01/02/03 at the TSV letter first (reader read them only via STATUS restatement)" — **TRUE-STILL and discharged here**: I read OSP-01…OSP-06 at `thesis/PREDICTIONS.tsv` directly, not via STATUS.
- `profiles/OSPREY.md:5` "**Grade at build:** L3-blocked-on-instrumentation" — the instrumentation block is now **removed** (`strike_feed.py` built and wired).

### 5. Falsification read — **IN SCOPE** ("thesis but no separate surface": AEOLUS · MIDAS · **OSPREY**)

**Where the rail actually lives:** `AGENTS/OSPREY/CLAUDE.md:142-198`, § EXIT RULES — **not** a separate file, deliberately. `CLAUDE.md:146` states why: "*OSPREY does NOT inherit `workbook/EXIT_PROTOCOL.md` — that file is 100% Iran-coded and went to FALCON per build spec §2b. This section is the Russia-coded falsification layer; `thesis/THESIS.md` § 'What would change this thesis' **defers here — single home, don't duplicate**.*" `THESIS.md:53` closes the loop from the other side: "→ `CLAUDE.md` § EXIT RULES… **Not duplicated here.**"

**Verdict: RAIL-IN-LOCAL-FORM — live, dated, and materially stronger than at run #2.**
- **Dated:** `CLAUDE.md:144` — "Kill rail re-derived: **2026-08-15**; re-read **2026-09-08**; **RULED 2026-09-08**". Three stamps, three distinct acts, each named.
- **Evidenced fire path:** the §1b downgrade rule went through a full objection cycle and is **in force** — `STATUS.md:42`, DOCKET L308 discharged 9/15 with **both consumers verified at their own artifacts**. Channel clocks are running with live counts (`STATUS.md:24-26`: 1/30, 7/30, 12/21).
- **Self-governance still exemplary:** `CLAUDE.md:144` records one §1 defect "surfaced and **ROUTED, not self-ruled**" (the Channel-3 kill letter's missing geography qualifier, OWED-32) — the desk again refused to amend its own falsifier.
- **One genuine gap, disclosed by the desk itself:** `STATUS.md:30` — "**War risk:** last dated rate observation 8/21 (**26 days old**)… **Do not infer flat premia.**" A rail input is 26 days dark and the desk labels it rather than smoothing it.

**Severity:** LOW. This is the strongest falsification layer in the cohort after FALCON's.

### 6. Negative-resolution leg
**Opened:** `AGENTS/OSPREY/thesis/PREDICTIONS.tsv` (3 FAILED / 2 CONFIRMED / **1 OPEN**).

| Row | Negative-class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **OSP-06** | **YES** — "by 2026-10-15 Russian seaborne crude exports will **NOT** sustain a recovery to ≥3.9 M bpd" | **YES, binding and exclusive** — "Bloomberg tanker-tracking 4-week-average… **No other series, aggregator or proxy may resolve this row**" | **YES, with a CEILING** — "a CONFIRMED verdict requires a dated recorded search… **WITHIN the window and no earlier than 2026-10-08**; an attempt dated after 2026-10-15 does NOT satisfy it" |

**Counts: 1 candidate opened / 1 confirmed negative-class / 0 lacking instrument / 0 lacking a dated precondition.**

🔑 **OSP-06 is the reference form for the whole fleet**, and its provenance is the reason: OSP-04's own resolution (`PREDICTIONS.tsv`, Outcome column) recorded **two defects against its author's own row, neither used to bend the verdict** — "(ii) PROCESS: the search-attempt guard fixed a date **FLOOR** and **NO CEILING**, so a desk dark for the entire window cured the guard **two days AFTER close**. On the letter that is legal; against the guard's own stated purpose… it is a near miss. **The fix… is ROUTED to DAEDALUS/PROME, not self-ruled.**" OSP-06 then adopted the ceiling prospectively. That is a complete learn→route→adopt cycle inside one ledger, and it is why the cohort's negative-resolution hygiene is as good as it is.

Also correctly handled: OSP-06 carries a **VOID PATH** that refuses to confirm on instrument silence — "it does NOT resolve CONFIRMED on the absence, because a negative established only by the instrument's silence is the OSP-04 defect repeated" — and the desk has distinguished *instrument dark* from *this desk cannot read it* under paywall (`KB-OSPREY-074`, "the instrument is **NOT dark**, this desk cannot read it; the VOID path does NOT arm").

### 7. As-made receipt — **n/a**

### 8. Cross-agent threads / pattern candidates
- **To PROME:** WQ-172's ruling has been applied *inside a frozen letter* at `PREDICTIONS.tsv` OSP-06 Notes — "**LETTER FROZEN as registered**; the WORLD-STATE test in the Invalidation column governs; the logged-search clause is a **PROCESS requirement on this desk, not a grading limb**". That is the correct disposal of an author-activity condition in an immutable row and is worth promoting as the reference handling.
- **PATTERNS candidate:** *A negative-existence guard needs a window, not a floor — a floor alone lets a dark desk cure the guard after the window closes.* Evidence: OSP-04 Outcome defect (ii) → OSP-06 ceiling → FERT-12 adopting floor+ceiling (`AGENTS/FERT/workbook/PREDICTIONS.tsv` FERT-12 Notes, "no earlier than 2026-11-25 and no later than 2026-12-02"). **n=3, three desks, and it propagated without a fleet packet** — which makes it a documented, not hypothesised, canon path.

### 9. Reviewer-side defects
- The 9/1 row held OSPREY at **L2** on "no strike_feed.py build verified" — a build blocker that Will unblocked in-session on 9/8 and the desk cleared the same night. The row has been a level low for 9 days.
- `profiles/OSPREY.md` carries a receipt banner (`:3`) that explicitly contradicts the banner immediately below it (`:3` no-trigger) without retracting it.

---

## MIDAS — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-08

### 1. Period production
53 commits, **24 self-authored / 29 routed-in**. Last self-commit **2026-09-11**; last touch (routed-in) 9/14. **Dark-days 6.**
Shipped: `metals_watch.py` +151 lines (the **contract-identity guard**, KB-047 closed), `sources/cot_vintages_consumed.tsv` (new, boot leg 3 alarms on an unread public vintage), the VECTOR-3 real-yield analysis, `MIDAS-06_KERNEL_NATIVE_COMPANION.json` +63, four Kernel command JSONs.

### 2. Row-claim test

| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | "MIDAS-08 terminal" | **TRUE-STILL** | `AGENTS/MIDAS/STATUS.md:31` — "MIDAS-08 (TERMINAL (b) 9/5…)" |
| 2 | "cot_gold recurring puller wired" | **TRUE-STILL** | `AGENTS/MIDAS/STATUS.md:5` — "COT via `cot_gold.py`, boot-wired as leg 3 on 9/5"; `sources/cot_vintages_consumed.tsv` (new in period) |
| 3 | "three terminal graders deliberately on demand" | **TRUE-STILL** | `STATUS.md:5` — "one-shot graders `settle_check.py` + `grade_cot3.py` + `grade_midas07.py`, **on-demand by design**" |
| 4 | "stale built-label and local-scale collision corrected" | **TRUE-STILL** | `STATUS.md:5` — "⛔ relabelled 9/5 from 'Maturity: L2'… Two scales, one token, on a surface peers read (DAEDALUS F-4)" |
| 5 | "DECLARED FLAT trade adaptation and BOND consumption satisfy L4" | **TRUE-STILL** | `STATUS.md:27` — the VECTOR-3 BOOK READ, "NO card, NO order, NO size, $0"; BOND adoption at `STATUS.md:32` ("adopted verbatim by BOND 9/1") |
| 6 | "**Contract-identity guard remains OPEN_ITEMS item 24**" | **REFUTED** — closed and mechanised 9/11 | `AGENTS/MIDAS/STATUS.md:3` — "✅ **KB-047 CLOSED — the contract-identity guard is LIVE in `metals_watch.py`** and grades all five `=F` pointers DYING (rc=1 REVIEW; `boot.py` clean on all four legs)"; `STATUS.md:21` gives the 9/10 evidence (GC=F vol 86 vs GCZ26 164,390) |
| 7 | NEXT: "**L5 not adjudicated**" | **ADJUDICATED HERE** (see §3) | — |
| 8 | NEXT: "do not re-wire closed-question graders" | **TRUE-STILL** and observed | — |
| 9 | NEXT: "Profile checkpoint 2026-09-26" | **NOT YET DUE** (9 days out) | `profiles/MIDAS.md:6` |

**Row verdict: 1 REFUTED / 6 TRUE-STILL / 2 due-or-pending.**

### 3. Ladder walk

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L4 | TRADE.md feeding proposals | **MET** | `AGENTS/MIDAS/TRADE.md` exists; `STATUS.md:27` is a live, dated, arithmetic-backed BOOK READ for TERRY/Will with an explicit **NO TRIM** decision and its reasoning ("root rule #6 applied to a SALE… selling a long into its own down-move is a chase") |
| L4 | Signals flowing | **MET** | `STATUS.md:32` "adopted verbatim by BOND 9/1"; DFII10 nowcast "**Routed to BOND, whose level it is**" (`STATUS.md:9`); VECTOR-3 one-pager to `PROME/inbox/` |
| L5 | Clean closeouts | **NOT MET** | `STATUS.md:24` records four standing instrument warnings "**each bought by a published error**", incl. ③ "the 8/27 bars this page carried as PROVISIONAL were wrong in **4 of 6 legs**… *(On 8/20 it reached Will as a mislabelled figure.)*" — pre-period, but the pattern of published-then-corrected figures continued: `STATUS.md:20` corrects the VECTOR-3 packet's own "`GC=F` $4,416 [9/9]" as a dying-contract quote off by **$44.70 / 1.00%** |
| L5 | Zero YEYOU flags | **NOT-ADJUDICATED — cannot fire** (PAT-060) | WQ-181 ① |
| L5 | Current | **NOT MET — 6 dark-days**, against a desk whose own STATUS says "**Re-measure the rolling-120-session gold–DFII10 beta against the −0.08 %/bp flip level — EVERY BOOT**" | `STATUS.md:36` item 2; last self-commit 9/11 |

**Recommendation: HOLD L4, confidence H.** L5 fails on two independent legs. The *current* leg is the more serious of the two: MIDAS wrote a standing every-boot re-measurement instruction on 9/11 and has not booted since, and the row it guards is the one that "moves a book."

🔴 **BLOCKING HYGIENE FINDING — MIDAS STATUS is at 99% of the fleet read cap.** `AGENTS/MIDAS/STATUS.md` = **32,158 B against the 32,550 B cap** (root `CLAUDE.md` § Data Hygiene) — **392 bytes of headroom**, 102 lines. The next appended sentence breaches it. The desk rotated on 9/11 (`STATUS.md:31`, 8 blocks → `analysis/STATUS_ARCHIVE_2026-09.md`) and is still at 99%, which means the rotation is not keeping pace with the append rate. This is the single most actionable item in the cohort and it needs a packet, not a note.

### 4. Profile trigger

> **Vintage:** `profiles/MIDAS.md:3` — "**Date:** 2026-09-05 (**FIRST BUILD**…)"; receipt-updated 9/8 (`:8`)
> **Trigger:** `profiles/MIDAS.md:6` — "**Staleness:** refresh at the **next COT-grade cycle** or **>21d** → checkpoint **2026-09-26**"

**Verdict: FIRED on the COT-grade leg; NOT FIRED on the 21d leg (checkpoint 9/26, 9 days out).**
The COT-grade cycle **did** turn inside the period: `STATUS.md:23` carries "Gold COT net/OI **54.9437%** [as-of 9/1…] — ratchet 53.19 → 54.44 → 54.69 → 56.86 → 54.94", MIDAS-08 graded TERMINAL (b) on 9/5, and boot leg 3 gained a vintage alarm. The profile has not been touched since the 9/8 receipt.

**Profile statement now false:** `profiles/MIDAS.md:16` — "Market class, ACTIVE, **L4 (H)**, graded 2026-09-08" is *correct*, but it disagrees with the desk's own STATUS (see §8) — the profile is right and the desk is wrong, which is the harder direction to notice.

### 5. Falsification read — **IN SCOPE** ("thesis but no separate surface")

**Where the rail actually lives:** three coupled surfaces, not one file.
1. **The registered letter** — `AGENTS/MIDAS/THESIS.md:48-51`, "**What KILLS v2**": #1 structural-floor failure (gold <$3,317 with DFII10 <2.6), #2 CB-buying collapse (WGC Q2 <100t), #3 re-decoupling UP (gold rises through rising real yields sustained 3+ weeks).
2. **The ruling layer** — `THESIS.md:53-77`, the SELF-RULED 2026-08-21 DELEGATION_TIER block on kill-cond #3's duration basis, with a 23-year base rate (endpoint 19.15% vs weekly-continuous 0.79%) and Will's 8/21 dispositions encoded 8/23.
3. **The live grading cell** — `AGENTS/MIDAS/STATUS.md:65`, the M1 matrix row, which carries all three conditions **with measured live values dated 9/9–9/10** and a fired-state.

**Verdict: RAIL-IN-LOCAL-FORM — live and dated, with an EVIDENCED fire path, but the registered letter has rotted in two cells.**

**Evidenced fire path (the strong half):** `STATUS.md:65` reads "**🔴 FIRED** (leg 3, on the 7/17→8/7 window). Legs 1–2 measured and clear." Kill-cond #2 was genuinely **graded**, not assumed — `workbook/KB.tsv` KB-MIDAS-034 (2026-08-07): "v2 kill-cond #2 **GRADED, NOT FIRED**… Q2 2026 = 288.9t net… 2.89x the 100t kill line. **Closes the M1 kill rail's UNMEASURED leg**: rail moves from '1 fired / 2 clear / 1 unmeasured' to '1 fired / 3 clear'." That is a kill condition resolved at a primary, against the desk's own interest, with a "~2 weeks overdue (MIDAS was dark for the ~late-July publication)" self-flag attached.

🔴 **Two REAL-STALE cells in the registered letter — and the second one is the dangerous shape:**

| Cell | Text as it stands today | Live state | Locator |
|---|---|---|---|
| **kill-cond #2 status** | "WGC Q2 GDT (~late July): CB net buying ≥150t = structural layer intact. ***(Still pending — kill-cond #2.)***" | **Graded NOT FIRED on 2026-08-07** — 41 days ago. `THESIS.md` was edited twice after the grade (8/21, 8/23) and this line survived both passes | `AGENTS/MIDAS/THESIS.md:45` vs `workbook/KB.tsv` KB-MIDAS-034 |
| **the "where we are" from-state** | "Gold basing in **$3,700–4,300** while DFII10 holds 2.2–2.5 = the floor forming well above the pre-run shelf. **✅ roughly where we are** (gold $4,021.90, DFII10 2.32)." | **FALSE on the file's own numbers.** Gold is **$4,407.30** (`GCZ26`, 9/10 settled) — **$107 ABOVE the stated basing band's top**, and DFII10 is **2.46** (FRED 9/9), above the stated 2.2–2.5 midpoint and approaching its ceiling. The "✅ roughly where we are" tick is certifying a band the market left | `AGENTS/MIDAS/THESIS.md:46` vs `AGENTS/MIDAS/STATUS.md:7` and `:11` |

**Why the second is the dangerous one:** it is not a missing update, it is a **live ✅ affirmation** attached to a stale measurement. A reader who opens the registered thesis letter to check the from-state is told, in the file's own voice, that the current level sits inside the band — when it sits outside it. `finding_plausible_stale_value_evades_review`, and `finding_header_edit_is_the_edit_most_mistaken_for_maintenance` running in reverse: the *body* was maintained (the 8/21 ruling block is meticulous) while the numbered list above it was not.

**Severity:** MODERATE. The rail *grades* correctly because grading happens at `STATUS.md:65`, which is current. The risk is entirely to a reader who treats `THESIS.md` as the letter — which is exactly what `THESIS.md` says it is.

### 6. Negative-resolution leg
**Opened:** `AGENTS/MIDAS/workbook/PREDICTIONS.tsv` (2 HIT / 2 NO-FIRE / 2 INDETERMINATE / **2 OPEN**).

| Row | Negative-class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **MIDAS-01** | **Negative-SHAPE, not negative-existence** — "stays bid (**does not sell off >10%** from the 7/10 baseline) even as 10Y real yields stay >2%" | **YES** — "gold (GC=F) close vs $4,113.70 [7/10 anchor] while DFII10 >2.0 by 9/30" | **N/A** — a continuously-published price series; there is no absence to establish |
| **MIDAS-02** | **Negative-SHAPE** — "Copper **does NOT roll >20%** with LME inventory building >100%" | **YES** — "copper (HG=F) spot QoQ vs $5.75 [4/9 anchor] + LME inventory LIVE w/ DEFINED baseline… the '+100%' RED leg now grades vs the **2yr median (=479kt)** not an undefined normal (KB-018, metals_watch leg 6)" | **N/A** — same reason |

**Counts: 2 candidates opened / 0 confirmed negative-EXISTENCE class / 0 lacking instrument.** Both rows are negatives about a *level* on a live series, which is the benign class — the canon's search-instrument requirement targets negatives about an *event's absence*, and neither row is that.

⚠️ **One live defect the desk has flagged five times and not repaired:** `STATUS.md:15` and `:17` — I1's registered bands "are **all downside** and cannot score tightening OR its reversal (L-13(a)); **fifth live demonstration, flagged not repaired**", and at `:13` a **sixth**. A scoring band that can only move one way is a one-sided instrument on a two-sided question. Flagged-not-repaired six times is past the point where flagging is the response.

### 7. As-made receipt — **n/a**

### 8. Cross-agent threads / pattern candidates
- 🔴 **To MIDAS (packet):** `AGENTS/MIDAS/STATUS.md:5` asserts "**this desk is L3** on it [the fleet maturity ladder]". **FLEET_MAP says L4, last_scored 2026-09-08** — three days *after* MIDAS wrote the L3 line on 9/5. The desk is publishing a grade one level below its own, on a surface the line itself says "**peers read**". See the cohort-level finding.
- 🔴 **To MIDAS (packet, urgent):** STATUS at **99% of the 32,550 B read cap**.
- **To PROME/BOND:** `STATUS.md:9` — DFII10 nowcast ~2.53 [INFERRED] would be "**the first ≥2.50 in 23 months** and is the book's own add-gate"; full FRED series n=5,926 has 111 obs ≥2.50, "the LAST on 2023-10-25". Routed to BOND 9/11; **no MIDAS session since**, so nobody on this desk has read the 9/11 16:15 ET print that was called "the single highest-value read of the next session" (`STATUS.md:35`).
- **PATTERNS candidate:** *A ✅ affirmation attached to a from-state is a claim with a shelf life, and it never self-expires.* Evidence: `THESIS.md:46`. Distinct from a bare stale number — the tick mark **certifies** the staleness, so a reader checking the letter gets a confident wrong answer rather than an obviously old one. Cf. `finding_dated_carry_item_has_no_expiry_check`, but the failure here is the *operator* (✅), not the date.

### 9. Reviewer-side defects
- The MIDAS row's `Gaps` cell asserts "Contract-identity guard remains OPEN_ITEMS item 24" — closed at the artifact on 9/11, 6 days before this review, and announced in the desk's own STATUS lead.
- `profiles/MIDAS.md` (built 9/5, my own file) records the grade correctly at L4 but no packet ever told the desk, which is how `STATUS.md:5` came to carry L3 for 12 days.

---

## FERT — Market · FLEET_MAP L3 / Conf H / last_scored 2026-09-08

### 1. Period production
14 commits, **6 self-authored / 8 routed-in** — the lowest volume in the cohort **by design**. Last self-commit **2026-09-15**; **dark-days 2.**
Shipped: GATE-FERT-G5 graded NOT FIRED on the 9/9 DTN print (`e42d3836f`), GATE-FERT-G3 graded NOT FIRED both legs with the China floor ladder dated at a named instrument (`107e6ccfe`, 9/15), T11 Pink Sheet graded (`1f33259ef`, 9/5), FL-FERT-06 downgraded Yes→Estimated (`d4d5fdaac`), plus new `workbook/GATE_GRADES.md` and `workbook/INSTRUMENT_GAPS.md`.

⚠️ **Read the volume correctly:** FERT is an **EVENT-DRIVEN SPECIALIST** — "wakes on named triggers, **no standing cadence**" (`profiles/FERT.md:15`). 6 self-commits against 4 graded gate/trigger events is a high hit rate, not a low one. A dark-days count is close to meaningless for this desk and I decline to treat it as a signal.

### 2. Row-claim test

| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | "Receipt verified: **FERT-11/12 OPEN**" | **TRUE-STILL** | `AGENTS/FERT/workbook/PREDICTIONS.tsv` — FERT-11 (resolve 2026-10-09), FERT-12 (resolve 2026-12-02), both Status=OPEN |
| 2 | "standing eight-vector matrix with Independence" | **CANNOT-EVALUATE** — I did not open the matrix surface itself; STATUS is 150 ln / 24,217 B and I read the workbook instead | — |
| 3 | "dated exit rail" | **TRUE-STILL** | `AGENTS/FERT/workbook/EXIT_PROTOCOL.md` (+22 lines in period); referenced as canonical by `AGENTS/FERT/TRADE.md:1` |
| 4 | "**G3/G5 ratification and T11 re-date verified**" | **TRUE-STILL, and both re-graded since** | G5 `e42d3836f` (9/9), G3 `107e6ccfe` (9/15), T11 `1f33259ef` (9/5) |
| 5 | "Prior zero-OPEN and trigger-only-matrix claims withdrawn" | **TRUE-STILL** | — |
| 6 | "The **OPEN-count incentive question** remains a September 14 policy item" | **OVERDUE — 3 days** | no artifact found in `AGENTS/FERT/` or the period commits dispositioning it |
| 7 | NEXT: "**L4 not adjudicated in this receipt read**" | **ADJUDICATED HERE** (see §3) | — |
| 8 | NEXT: "frozen TRADE has a dated re-look" | **TRUE-STILL** | `AGENTS/FERT/TRADE.md:3` — "**Next mandatory re-look: 2026-11-15** (or immediately if the EXIT_PROTOCOL §2 bullish flip fires…)" |
| 9 | NEXT: "Profile checkpoint 2026-09-26" | **NOT YET DUE** | `profiles/FERT.md:6` |

**Row verdict: 5 TRUE-STILL / 1 OVERDUE / 1 CANNOT-EVALUATE / 2 due-or-pending.** This is the cleanest row in the cohort.

### 3. Ladder walk — the PR6 ask: adjudicate L4

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L3 | Convergence matrix | **MET** (asserted in row, not re-verified by me) | — |
| L3 | Exit rules | **MET** | `AGENTS/FERT/workbook/EXIT_PROTOCOL.md` |
| L3 | Predictions resolving | **MET** | `workbook/PREDICTIONS.tsv`: 12 rows, **2 HIT / 3 MISS / 2 VOID / 1 HIT(partial) / 1 HIT(direction)-MISS(magnitude) / 1 MISS(so far) / 2 OPEN** — a genuinely graded ledger including two rows voided *as instruments* ("VOID (unfalsifiable-as-written)", "VOID (broken-as-instrument)"), which is the honest disposal |
| L3 | Dated falsification surface | **MET** | `workbook/EXIT_PROTOCOL.md` + `workbook/GATE_GRADES.md` (new in period) |
| **L4** | **TRADE.md feeding proposals** | **❌ NOT MET** | `AGENTS/FERT/TRADE.md:1` — "**🧊 FROZEN — freeze EXTENDED 2026-08-17 after a dated re-look; deliberately NOT revived. Every row below is DEAD, graded history; do not cite any row as current.**" Zero proposals in the period; `TRADE.md:13` — "FERT holds **zero capital and proposes zero trades this session**" |
| **L4** | **Signals flowing** | **✅ MET** | Gate grades routed and consumed: `9a9e6fff5` "FERT -> PROME: GATE-FERT-G5 + G3 both graded NOT FIRED… whole inbox drained 6/6" (9/2); `outbox/2026-09-15_from-FERT_G3-china-quota-floor-re-read-DOCKET-L204.md`; FERT cited in peers' live state at `AGENTS/CARL/NEXUS_BRIEF.md`, `AGENTS/MARCO/NEXUS_BRIEF.md`, `AGENTS/FLG/STATUS.md` |

**Recommendation: HOLD L3, confidence H.** L4 is **one of two legs met**. The blocked leg is `TRADE.md`, and I want to be precise about *why* I am not waiving it here: FERT's freeze is **deliberate, reasoned and dated**, and the reasoning is better than most live trade books — `TRADE.md:20-23`: "The nitrogen channel that justified the entire March book is **graded dead**, and the live channel (phosphate) has **no proposed expression** — I have not done the single-name work, and **inventing one to fill the table would be exactly the 'write a trade because the file expects a trade' failure**… **A frozen file that says *why* it is frozen and *when* it will be re-looked is a working surface. An un-bannered file with three dead rows is a trap.**"

That paragraph is a desk refusing to manufacture output to satisfy a ladder leg. **Penalising it is the wrong answer, and so is silently waiving it** — which is why this goes to the ladder sitting as a stated question rather than being resolved in a reader's report. See the cohort-level finding.

### 4. Profile trigger

> **Vintage:** `profiles/FERT.md:3` — "**Date:** 2026-09-05 (**FIRST BUILD**…)"; receipt-updated 9/8 (`:8`)
> **Trigger:** `profiles/FERT.md:6` — "**Staleness:** event-keyed (**next World Bank Pink Sheet / named trigger**) or **>21d** → checkpoint **2026-09-26**"

**Verdict: NOT FIRED.** The Pink Sheet event that the trigger keys on was graded **2026-09-05** (`1f33259ef`, T11 — "phosphate rock FLAT $170.0/mt Aug"), i.e. **on the profile's own build date**; the next edition is the October one, which FERT-11 resolves against on 2026-10-09. The 21d leg runs to 9/26. Both legs clean. **This is the only profile in the cohort whose trigger is genuinely not fired** — and it is not fired because it is *event-keyed to the desk's own publisher clock*, which is the form the other six should copy.

**No profile statement found false.** `profiles/FERT.md:15` "**L3 (H), graded 2026-09-08**" agrees with FLEET_MAP.

### 5. Falsification read — **not in scope**

### 6. Negative-resolution leg
**Opened:** `AGENTS/FERT/workbook/PREDICTIONS.tsv` (12 rows, 2 OPEN).

| Row | Negative-class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **FERT-11** | **NO** — a positive equality test ("prints FLAT at **exactly $170.0/mt** for September 2026") | **YES** — "World Bank Pink Sheet 'Phosphate rock'… as carried in `CMO-Pink-Sheet-October-2026.pdf` and in **row 2026M09 of `CMO-Historical-Data-Monthly.xlsx` (col 58 of sheet 'Monthly Prices')**" | **N/A**; has a CATCH-ALL instead: "no October-2026 edition published by Resolve_By ⇒ **NO-VERDICT, never a silent extension**" |
| **FERT-12** | **YES** — "DTN retail MAP… **does NOT print above $975/ton in ANY** weekly article published 2026-09-09 → 2026-11-25" | **YES** — "'MAP' in the DTN Progressive Farmer weekly retail fertilizer table, US NATIONAL AVERAGE — ⛔ **never** Pink Sheet MAP $/mt, **never** a NOLA barge $/st quote" | **YES, floor AND ceiling** — "**NEGATIVE-RESOLUTION GUARD (canon, amended WQ-172)**: this resolves on a negative, so the resolution requires a **DATED SEARCH ATTEMPT INSIDE the window** — at least one check of the dtnpf.com crops article index **no earlier than 2026-11-25 and no later than 2026-12-02**; the grade reads the **WORLD STATE**… never my own logging" |

**Counts: 2 candidates opened / 1 confirmed negative-class / 0 lacking instrument / 0 lacking a dated precondition.**

🔑 **FERT-12 is the best-specified negative-resolution row I read in this cohort**, and it is better than OSP-06 in one respect: it names all six WQ-162 elements (series, unit, vintage, operator+boundary with the boundary *owner* stated, consecutiveness, reset), plus a base rate computed at registration ("MAP printed $959 / $960 / $959 / $959 across the four articles 2026-08-12 → 2026-09-02"). It also states the vintage *choice* explicitly — "DTN publishes no revision cycle, so the WQ-162 default is the declared choice" — rather than leaving it inferable. FERT-11 does the same for a revisable series ("**TREATED AS REVISABLE**… A later restatement is **ANNOTATED** on this row, **never re-graded**"), which is the correct disposal of the ALFRED-vintage problem in a non-FRED series.

### 7. As-made receipt — **n/a**

### 8. Cross-agent threads / pattern candidates
- **To PROME:** the "**OPEN-count incentive question**" was a **2026-09-14 policy item** (FERT row `Gaps`) and is **3 days overdue** with no artifact in FERT's tree. It is a policy item about whether a desk is rewarded for carrying OPEN rows — worth resolving before the 9/19 sitting, because it bears directly on how every ladder walk in this review reads a prediction ledger.
- **PATTERNS candidate (promote FERT-12 outward):** *A negative-existence row needs the search window bounded at both ends AND the grade explicitly pointed at the world-state rather than the author's log.* FERT-12 does both in one clause and cites WQ-172 for the second. Pair it with OSP-06 as the reference forms. ⚠️ Per the DAEDALUS MEMORY MODEL rule, when promoting this outward, **scan the destination for rules that read as the opposite** — specifically anything that treats a logged search as sufficient.

### 9. Reviewer-side defects
- **"L4 not adjudicated" sat in the `Next_upgrade` cell for 9 days** with no named adjudication date, while the row's own `Gaps` cell carried a dated 9/14 policy item. A cell that says "not adjudicated" without a date is the bare-event class PAT-115 exists to prevent — it needs a `Resolve_By`.

---

## WATT — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-05

### 1. Period production
39 commits, **14 self-authored / 25 routed-in**. Last self-commit **2026-09-11**; last touch 9/15. **Dark-days 6.**
Shipped: P1 **5→3 executed 9/11** on the registered de-escalation letter (composite 16→14/20), the 9/10 grade dossier (`reports/2026-09-10_DOCKET-L249_202c-lapse-grade.md`, 83 lines), `power_watch.py` +65, a **695-line** `status_archive/STATUS_ARCHIVE_2026-09.md` rotation, `PREDICTIONS_ARCHIVE.tsv` (+12), and **WATT-11 registered 9/6** (the autumn quiet-season discriminator).

### 2. Row-claim test

| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | "PROMOTED L3→L4 (Conf H) 2026-09-05. BOTH named L4 legs verified at the artifacts" | **TRUE-STILL** | — |
| 2 | "**Inbox root is down to 2, processed/ holds 41**" | **REFUTED (improved)** — root is **1**, processed **48** | `ls AGENTS/WATT/inbox/` (1 root file + `WALTER/` + `processed/`); `processed/` = 48 entries |
| 3 | "AEOLUS/STATUS:157 renders the C3 convergence row as '**WATT canonical**'" | **TRUE-STILL, anchor moved** — the row is now at `AGENTS/AEOLUS/STATUS.md:86`, and it still reads "**WATT canonical** (PJM primary ×2); CPC GIS", now carrying WATT's 9/1–9/3 EEA-1 figures and the $1,868.78 peak | `AGENTS/AEOLUS/STATUS.md:86` |
| 4 | "VULCAN/STATUS:51 'VULCAN sizes MW, WATT prices the grid'" | **TRUE-STILL, anchor moved** — now `AGENTS/VULCAN/STATUS.md:53`, and the S3 wording was **corrected 9/6 and adopted verbatim across 8 surfaces** | `AGENTS/VULCAN/STATUS.md:53` |
| 5 | "🟢 PROFILE NOW HAS A DATED TRIGGER… keyed to the PJM Door-B / FERC action ~2026-10-12" | **TRUE-STILL** | `profiles/WATT.md:4` |
| 6 | "🟢 Behaviour worth keeping, STATUS:104 — WATT **REFUSED a stale-proxy spark** and used a same-vintage primary (+$48.12)" | **TRUE-STILL, anchor moved** (STATUS rotated 9/11; the refusal is preserved at `status_archive/STATUS_ARCHIVE_2026-09.md:92`) | `AGENTS/WATT/status_archive/STATUS_ARCHIVE_2026-09.md:92` |
| 7 | "🟡 **metered-vs-DR record-break split** carried to ~Sept and now due" | **TRUE-STILL — and now OVERDUE at the publisher** | `AGENTS/WATT/STATUS.md:92` item 10 — "**KB-WATT-034 metered-vs-DR split (PJM official was due ~early Sept — overdue)**" |
| 8 | NEXT: "L5 on **two consecutive clean cycles** (9/3 was one) + the metered-vs-DR split resolved" | **NOT MET on either limb** (see §3) | — |

**Row verdict: 1 REFUTED (improved) / 6 TRUE-STILL / 1 NOT MET.** ⚠️ **Three of the six TRUE-STILL cells verified only after chasing a moved line anchor** (claims 3, 4, 6). The *facts* survived; the *pointers* did not. Every one of them was written as `FILE:NN`.

### 3. Ladder walk

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L4 | TRADE.md feeding proposals | **MET** | `AGENTS/WATT/TRADE.md` exists and is live-referenced: `STATUS.md:20` — "**Still no deploy-posture change** — a fired-then-spent gate supplies no entry and no exit (TERRY Non-Negotiable #15); see `TRADE.md`" |
| L4 | Signals flowing | **MET, and at the strongest form** | `AGENTS/AEOLUS/STATUS.md:86` writes "**WATT canonical**" into its own convergence grid — a reader delegating authority over a metric, not merely receipting it; `AGENTS/VULCAN/STATUS.md:53` adopts WATT's corrected population wording **verbatim across 8 surfaces** |
| L5 | Clean closeouts — "two consecutive clean cycles" | **NOT MET** | The 9/11 cycle carried a self-corrected error: `STATUS.md:8` — "**9/10 printed one 5-min interval ≥$500 ($672.38 @15:45)** — a transient… and **a correction to yesterday's noon-read 'zero'** (L-52)". Correctly handled, but it is a corrected figure inside the cycle |
| L5 | metered-vs-DR split resolved | **NOT MET — and NOT WATT'S TO RESOLVE** | `STATUS.md:92` — "PJM official was due ~early Sept — **overdue**". The gate is publisher-side |
| L5 | Zero YEYOU flags | **NOT-ADJUDICATED — cannot fire** (PAT-060) | WQ-181 ① |
| L5 | Current | **NOT MET — 6 dark-days**, and `WATT-11`'s window **opened 9/15** with no session since | `STATUS.md:9` — "the autumn discriminator `WATT-11` opening 9/15" |

**Recommendation: HOLD L4, confidence H.**

⚠️ **One of the row's two named L5 gates is not the desk's to clear** — the metered-vs-DR split waits on a PJM publication that is itself overdue. A ladder gate keyed to a third party's publication schedule will sit unmet for reasons that say nothing about the desk. **Recommend re-cutting the WATT `Next_upgrade` to key L5 on the two-clean-cycles leg alone**, and moving the PJM split to a dated DOCKET row where a slipping publisher is visible as a publisher problem.

### 4. Profile trigger

> **Vintage:** `profiles/WATT.md:3` — "**Body:** 2026-08-07, **refreshed 2026-09-05**"
> **Trigger:** `profiles/WATT.md:4` — "**DATED TRIGGER ADDED**… refresh at the **PJM 2028/29 Base Residual Auction / FERC action on the Door-B filing (~2026-10-12)** or **21d** → checkpoint **2026-09-26**"

**Verdict: NOT FIRED.** 12 days since the 9/5 refresh (21d leg runs to 9/26); the FERC Door-B action is registered as `WATT-10` with "requested effective **10/12**" (`STATUS.md:13`) and has not issued. Both legs clean.

**Profile statement now false:** `profiles/WATT.md:10` — "STATUS **101 ln**" is now **110 ln / 23,439 B**; minor, and the profile explicitly tells the reader to take the live figure from `boot.py` leg 3 rather than from prose, which is the right construction.

### 5. Falsification read — **IN SCOPE, STALE-FLAGGED**: `KILL_MEMO.md` (scanner stamp 8/17 vs live 9/15)

**Two-vintage rule applied.** `KILL_MEMO.md` is a **STATE surface** (a pre-written cascade ladder, not an append-only log), so it is dated by its header's labelled freshness claim: `AGENTS/WATT/KILL_MEMO.md:3` — "**Created 2026-08-17**", with `:11` — "**Amendment log:** *(none yet — created 8/17)*". The scanner's 8/17 stamp is **correctly derived**.

### **Verdict: STALE-BUT-CONSISTENT — with one REFUTED from-state cell inside it.**

**Why STALE-BUT-CONSISTENT and not REAL-STALE — the decisive evidence is that the file was READ and EVALUATED three times in the period, by name:**
- `AGENTS/WATT/status_archive/STATUS_ARCHIVE_2026-09.md:341` (9/3 07:15 re-read) — "**NO EEA-2, no voltage reduction, no load shed ⇒ the KILL_MEMO cascade did NOT trip; P1 holds at 5, it does not go higher.**"
- `:435` (9/6) — "**KILL_MEMO cascade C1/C3 never tripped**", with the instrument question answered explicitly: "the board is a **CURRENT view, not a history**… **so the board cannot prove the negative** — the *tape* does: a load shed does not happen at a $437 peak."
- `workbook/KB.tsv` KB-WATT-099 (9/6) carries the same finding as a durable row.
- The live triad it serves is separately dated and **fresher**: `AGENTS/WATT/STATUS.md:110` § EXIT / INVALIDATION — "**Kill rail re-derived: 2026-09-02** *(TESTED, not rewritten, on 9/6 and again on 9/10.)*"

The file's 8/17 stamp is therefore **correct behaviour, not rot**: `KILL_MEMO.md:9` mandates it — "⚠️ **THIS FILE IS DECOUPLED FROM STATUS ON PURPOSE.** It must **not** be rewritten as part of a normal closeout… **and never while a trigger is live.** If you find yourself editing this file during an event, stop: that is the failure it was written to prevent." An unchanged amendment log on a file that was consulted three times during a live emergency is the design working.

🔴 **BUT one cell inside it is now factually REFUTED, and it is a from-state:**

`KILL_MEMO.md:25` (trigger **C1**, "Why a conjunction" column) reads:
> "Either alone is common enough to be noise. EEA-1 happened twice in July with no RED price; **$1,217.52 printed 8/16 with no posting at all. The pair has never co-occurred in this seat's record**"

**On 2026-09-02 the pair co-occurred.** PJM ran EEA-1 alerts on 9/1, 9/2 and 9/3 **and** the 5-min tape printed **$1,868.78 @19:30 on 9/2 with EIGHT CONSECUTIVE intervals ≥$1,000** (`status_archive/STATUS_ARCHIVE_2026-09.md:328`, `:339`). The base-rate sentence that justifies C1's conjunction is false 16 days after it was written, inside a file whose amendment log reads "(none yet)".

**Scoped precisely, because the distinction matters:** C1's *trigger letter* requires **EEA-2+**, and the September episode never exceeded EEA-1 — so **C1 correctly did not fire**, and the desk correctly recorded that it did not. What is stale is the **justification**, not the rule. But a cold reader opening this file in an emergency reads the justification column to decide whether the conjunction is still the right shape, and it now tells them the pair has never happened when it happened two weeks ago.

**Severity: LOW-MODERATE.** No grading consequence; one misleading sentence in the most-read column of a file designed to be read under time pressure, in a file whose own rules make it hard to fix. The correct disposal is the file's own: a **deliberate, dated amendment** to the C1 rationale cell — made now, on a quiet day, which is exactly when `KILL_MEMO.md:5` says to make it.

⚠️ **Second, smaller divergence worth recording:** `KILL_MEMO.md:25` writes C1 as `EEA2+ **AND** LMP ≥$1,000 2+ consecutive`, while the live triad at `AGENTS/WATT/STATUS.md:9` writes the →5 RED conjunction as `EEA2+ **OR** LMP ≥$1,000 2+ consecutive **AND** (emergency posting **OR** demand ≥97%)`. These are **different boolean shapes for the same phenomenon** living in two files. On 9/2 the live triad fired and the KILL_MEMO conjunction did not — both correctly, by their own letters, but a reader who assumed they were the same rule would have drawn opposite conclusions. `finding_correction_beside_an_instruction_leaves_two_live_instructions`, in its two-files form.

### 6. Negative-resolution leg
**Opened:** `AGENTS/WATT/workbook/PREDICTIONS.tsv` (**4 OPEN**, 0 resolved — all four registered forward).

| Row | Negative-class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **WATT-08** | NO (positive: "assigns costs PREDOMINANTLY to large loads") | YES — FERC eLibrary EL25-49 et al. | N/A |
| **WATT-09** | NO (positive: "proposes CONCRETE tariff revisions") | YES — FERC eLibrary / Federal Register, Docket EL26-67-000 | N/A |
| **WATT-10** | NO (positive: "FERC ACCEPTS the cost-assignment core") | YES — "FERC order on PJM's IRAS petition… **Resolve on the ORDER, not on comments or protests**" | N/A |
| **WATT-11** | **YES** — "**ZERO** EEA-class postings… and **ZERO** new DOE 202(c) orders… between 2026-09-15 and 2026-11-30" | **YES** — "**RESOLUTION SOURCE: PJM emergency-procedures board + DOE CESER 202(c) order index**", with an explicit MECE qualifying/not-qualifying list | **YES** — "**checked at every boot in the window and at close on 2026-11-30**" |

**Counts: 4 candidates opened / 1 confirmed negative-class / 0 lacking instrument / 0 lacking a dated precondition.**

⚠️ **One instrument-adequacy caveat on WATT-11, raised because the desk itself established the underlying fact and then did not carry it into the row.** WATT-11's named RESOLUTION SOURCE is "the PJM emergency-procedures board + DOE CESER order index". But `workbook/KB.tsv` KB-WATT-099 (9/6) records, as a durable finding, that **"the emergency-procedures page is a CURRENT view (msg_ids 105484-86, 105488-89 already dropped off) and cannot prove a historical negative"** — and `STATUS.md:8` reports a live instance: "**board ID #105506 is absent — UNKNOWN class.**" WATT-11 is a **76-day zero-event negative** resting on an instrument its own KB says cannot establish a historical negative.

**The mitigation is real and I want it on the record:** "checked at **every boot** in the window" converts the board from a history into an accumulating contemporaneous record, which is the correct workaround — *provided the desk actually boots inside the window*. **It has not booted since 9/11, and the window opened 9/15.** So the mitigation is currently not running, and there is already one UNKNOWN-class ID gap in the record. The durable fix is the one the desk already knows: **name the DM2 tape as the co-instrument in the row**, as `:435` does in prose ("the board cannot prove the negative — the *tape* does").

### 7. As-made receipt — **n/a**

### 8. Cross-agent threads / pattern candidates
- 🔴 **To WATT (packet) — a closed seam carried as open for 5 days, with a dead anchor.** `AGENTS/WATT/STATUS.md:37` (written 9/11) asserts: "⛔ **VULCAN seam OPEN ON MEANING** — agreed on the number, divergent on the population (`VULCAN/STATUS.md:27` still '55 GW **nameplate**' under 'SEAM CLOSED'); correction sent 9/6, **closure is at ITS artifact** (L-46)." **Both halves are false.** VULCAN adopted the correction **verbatim on 2026-09-06 — the same day WATT sent it** (`db3d4ae2b`, and `AGENTS/VULCAN/STATUS.md:53` "POPULATION WORDING CORRECTED 2026-09-06 (WATT, adopted verbatim; **8 surfaces**)"; also `:29` and `:73`, all three explicitly "**NOT a nameplate or queue figure**"). And `VULCAN/STATUS.md:27` is now the **matrix header row**, not the S3 row — the anchor points at a table header.
- **PATTERNS candidate (strong, and the sharpest lesson in this cohort):** *A desk that writes "closure is at their artifact" has stated the control and not exercised it.* WATT authored the exact right rule (**L-46**), cited it by number, and then wrote the open-seam flag five days after the artifact closed — without opening the artifact. The rule and the omission are in the same sentence. This is `finding_record_of_an_action_is_not_the_action` at its most instructive, because the desk **cannot** be accused of not knowing the rule. **The generalisable fix: a rule that says "verify at their artifact" needs a boot step that opens it, not a sentence that names it** — cf. `finding_a_check_that_only_advises_is_overridden_the_control_is_downstream`.
- **To WATT:** three FLEET_MAP evidence anchors (`AEOLUS/STATUS:157`, `VULCAN/STATUS:51`, `WATT/STATUS:104`) all drifted within 12 days. WATT's own STATUS anchors drift fastest in the fleet because it rotates aggressively (695 lines archived on 9/11). **Cite the section heading, not the line** — the rule OSPREY already wrote at `AGENTS/OSPREY/CLAUDE.md:144`.

### 9. Reviewer-side defects
- **I wrote three bare line anchors into WATT's `Gaps` cell on 9/5 and all three were dead within 12 days.** The facts survived; the pointers did not. The fix is mine, not WATT's: FLEET_MAP evidence cells must cite section headings or quoted strings.
- The `Next_upgrade` keys L5 partly on a **PJM publication** that is now overdue at the publisher — a gate the desk cannot clear by doing good work.

---

## VULCAN — Market · FLEET_MAP L4 / Conf H / last_scored 2026-09-05

### 1. Period production
57 commits, **30 self-authored / 27 routed-in** — the **highest self-ratio in the cohort (53%)**. Last self-commit **2026-09-13**; last touch 9/15. **Dark-days 4.**
Shipped: `tools/gpu_panel.py` (380 lines, new), `workbook/GPU_INSTRUMENT_SPEC.md` (237 lines, new), `scripts/test_validate_workbook.py` (174 lines, new — a test file for a validator), `validate_workbook.py` +108, `catalyst_countdown.py` +82, `workbook/EDGAR_SEEN.tsv` (+80), VULCAN-17 registered (NVDA guarantee-commitment level, DEWEY REQ-002), **GPU-PANEL-01 FROZEN** (`d437a068d`, 9/13), `SCHEMA.tsv` +31.

### 2. Row-claim test

| # | Claim | Verdict | Locator |
|---|---|---|---|
| 1 | "September 8 correction: the September 5 consumption read established adoption but **missed retracted population wording**" | **TRUE-STILL** (correct self-indictment, retained) | `profiles/VULCAN.md:8` |
| 2 | "**WATT/VULCAN now name utility-reported forecast and firm coincident peak, not queue nameplate**" | **TRUE-STILL — verified at VULCAN's artifact, three places** | `AGENTS/VULCAN/STATUS.md:29` ("~55 GW = **AGGREGATE UTILITY-REPORTED FORECAST**… ~32 GW = **FIRM COINCIDENT-PEAK**… Two bases, one number each. Never netted, never averaged"), `:53`, `:73` |
| 3 | "Owner S4 monthly cadence confirmed; **latest stored month July**" | **REFUTED** — latest stored month is **August**, pulled 9/11 | `AGENTS/VULCAN/workbook/S4_SERIES.tsv` last row: data month `2026-08-31`, filed `2026-09-10`, accession `0001046179-26-000658`, cum YoY `39.3`, pulled `2026-09-11T14:40:21Z`, validation `OK:3-recomputed-from-raw,worst-err=0.036pp` |
| 4 | "**Tripwire candidate n=1 retained for September 12**" | **CANNOT-EVALUATE** — no live "tripwire" surface found in `AGENTS/VULCAN/` (only the historical 8/31 mis-dated tripwire post-mortem at `THESIS.md:291-296` and `LESSONS.md` L-22). The 9/12 date has passed with no disposition I can locate | `grep -ri tripwire AGENTS/VULCAN/` |
| 5 | NEXT: "L5 on two consecutive clean cycles (**not adjudicated here**)" | **ADJUDICATED HERE** (see §3) | — |
| 6 | NEXT: "owner-confirmed MU print 2026-09-30, grading 10/01. **No 9/17 window**" | **TRUE-STILL — and today is 9/17, so this cell is doing its job** | `workbook/EXIT_PROTOCOL.md:227` — "MU FQ4 **CONFIRMED 2026-09-30 16:30 ET**, issuer press release 2026-08-26" |

**Row verdict: 1 REFUTED / 3 TRUE-STILL / 1 CANNOT-EVALUATE / 1 adjudicated.**

### 3. Ladder walk

| Level | Leg | Verdict | Locator |
|---|---|---|---|
| L4 | TRADE.md feeding proposals | **CANNOT-EVALUATE** — no `AGENTS/VULCAN/TRADE.md` in the tree; whether that is by charter (as with FALCON/OSPREY/HAWK) or a gap is not stated on any surface I read | `ls AGENTS/VULCAN/` |
| L4 | Signals flowing | **MET, at the strongest form** | `profiles/VULCAN.md:6` — "**four** readers carrying VULCAN's figures as canonical in their own live state"; in-period: `AGENTS/WATT/STATUS.md:37` (WATT tracking VULCAN's S3 wording), DEWEY REQ-002 integrated into VULCAN-17 (`e44593197`) |
| L5 | Clean closeouts — "two consecutive clean cycles" | **NOT MET** | The 9/13 cycle is clean in conduct but the period contains a self-found instrument defect: outbox `…cause-was-a-silent-defect-in-my-EDGAR-helper.md`, and `…a-date-correction-that-goes-against-me.md`. Both are *good* behaviour and both are defects in shipped work |
| L5 | Zero YEYOU flags | **NOT-ADJUDICATED — cannot fire** (PAT-060) | WQ-181 ① |
| L5 | Current | **MARGINAL — 4 dark-days**, but the desk's instruments are on a **pre-committed cadence** whose next slot is 9/18 post-close, and `EXIT_PROTOCOL.md:254` says so in advance | `workbook/EXIT_PROTOCOL.md:254` |

**Recommendation: HOLD L4, confidence H.**

🔴 **BLOCKING FINDING — VULCAN's own STATUS publishes the wrong grade.** `AGENTS/VULCAN/STATUS.md:5` reads:
> "**Class:** Market-agent (AI-capex/semi/memory → systemic risk) · **Spawnable by:** PROME or Will · **Maturity:** **L3** (DAEDALUS 8/7 Production Ready)"

FLEET_MAP says **L4, Conf H, last_scored 2026-09-05**, and `profiles/VULCAN.md:8` says "Market class, ACTIVE, **L4**". The desk has been publishing a grade **one level below its own for 12 days**, on the surface peers read. **This is a DAEDALUS-side propagation failure**, not a VULCAN error: I promoted the desk on 9/5, wrote it into FLEET_MAP and the profile, and never packeted the owner. See the cohort finding.

🟠 **Read-cap:** `AGENTS/VULCAN/STATUS.md` = **30,313 B = 93% of the 32,550 B cap**, 125 lines. Above the 75% rotate tier. Second-worst in the cohort after MIDAS.

### 4. Profile trigger

> **Vintage:** `profiles/VULCAN.md:3` — "**Body:** 2026-08-07, **refreshed 2026-09-05**"
> **Trigger:** `profiles/VULCAN.md:4` — "**DATED TRIGGER ADDED** (the prior body had none — it was UNEVALUABLE): refresh at the **MU FQ4 print (owner-confirmed 2026-09-30; grade 10/01)** or **21d** → checkpoint **2026-09-26**"

**Verdict: NOT FIRED.** MU FQ4 is 13 days out and confirmed at the issuer primary; the 21d leg runs to 9/26. Both legs clean, and the event leg is anchored to an **issuer press release (2026-08-26)** rather than an estimate — the strongest anchor form in the cohort.

**No profile statement found false.** `profiles/VULCAN.md:8`'s 9/8 correction ("Confidence stays H for the verified **structural consumption** leg, not as independent verification of market figures") is a precise scope statement and remains accurate.

### 5. Falsification read — **IN SCOPE, STALE-FLAGGED**: `workbook/EXIT_PROTOCOL.md` ("8/13 inferred, may be an event date")

**Two-vintage rule applied — and it is the rule that decides this one.** The file is a **hybrid**: §1–§7 are STATE (kill legs, channel rails, flip, cross-agent thresholds) but the file also carries an **append-only re-evaluation log** of dated closeout entries. Under the rule, the append-only portion is dated by its **newest ENTRY heading**.

- Newest entry heading: `workbook/EXIT_PROTOCOL.md:254` — "**🔴 THESIS-KILL RE-EVALUATION 2026-09-13** (PROME-spawned session, DOCKET L330; closeout step 3)". **Four days old.**
- Entry headings in the period alone: `:237` (9/06 PM), `:245` (9/11), `:254` (9/13). Prior: `:24`, `:28`, `:54`, `:66`, `:103`, `:120`.
- The header line the scanner read — `:3` "**Kill rail re-derived: 2026-08-13** *(first authored — VULCAN carried no kill tree… until today)*" — is a **provenance/authorship stamp**, not a labelled freshness claim. Its own parenthetical says so: "first authored."
- §7 carries an explicit, live, **dated rewrite trigger**: `:227` — "rewrite this rail when **MU FQ4 prints (🔴 CONFIRMED 2026-09-30 16:30 ET**, issuer press release 2026-08-26)… OR by 2026-11-15 — **whichever is FIRST**", graded **NOT DUE** at `:264` with the day count recomputed ("17 calendar / 13 trading days out, boot leg 6, holiday-correct").

### **Verdict: WITHDRAWN — the scanner misdated it.**

**Which rule it broke:** it applied the **STATE-surface** branch of the two-vintage rule to a **hybrid** surface, and then took a line containing the word "re-derived" as the labelled freshness claim when the same line's parenthetical identifies it as the authorship date. The scanner's own hedge — "8/13 **inferred**, **may be an event date**" — is the tell that it could not find a freshness label and fell back. **A file with nine dated re-evaluation headings, the newest four days old, is not a stale surface.** The correct reading for a hybrid is: newest entry heading governs freshness; the header governs provenance.

🔑 **And the withdrawal is the less interesting half. The file itself discloses a real defect the scanner could never have seen — its INSTRUMENTS are stale while the rail is fresh:**
- `:259` — "⚠️ **The instrument did NOT read this week — `mag7.py` slot 1 (9/11 post-close) is MISSED**, the first miss on a cadence registered only days earlier. **A duration leg on a series with a hole in it is the defect this cadence was created to prevent**, so the miss is recorded here and not only in STATUS."
- `:259` — the DRAM spot series "has now missed **four** pre-committed readings (8/27 · 8/28 · 09-04 · 09-11) and its last row is 2026-08-24 — **20 days stale**. That does not move the leg; it narrows the evidence the 9/30 grade will rest on."

Leg 2 requires "Mag-7 ≤28% and **holds 3+ consecutive months**" — a **duration** test — and its instrument now has a gap in it, 17 days before the rail's own rewrite trigger fires. **That is the finding the scanner was reaching for and missed by looking at the wrong vintage.**

**Severity: LOW for the flagged staleness (withdrawn); MODERATE for the disclosed instrument gap.** The rail is the best-maintained falsification surface in the cohort — nine dated re-evaluations, each recording *why* nothing moved, including `:28`'s self-indictment ("across passes 7-8 I wrote *'thesis-kill still 1 of 3'* into three commit messages and a NEXUS brief **without opening this file.** The count was correct — but a **restated** count is not a **re-evaluated** one"). A desk that writes that about itself is not the desk to flag for staleness.

### 6. Negative-resolution leg
**Opened:** `AGENTS/VULCAN/workbook/PREDICTIONS.tsv` (**9 OPEN**, 0 resolved-in-file — the largest live book in the cohort). Note the schema carries a dedicated **`anchor_type`** column, which no other desk in the cohort has.

| Row | Negative-class? | Names a SEARCH INSTRUMENT | Dated search-attempt precondition |
|---|---|---|---|
| **VULCAN-02** | Negative-SHAPE ("does NOT roll >25% QoQ") | YES — TrendForce/maker-guide contract price QoQ; with a pre-registered SPLIT rule (a/b/c) | N/A (published series) |
| **VULCAN-11** | Mixed | YES — 4Q26 DRAM contract + MU FQ4 guide, with an **EXPLICIT NO-VERDICT BAND** | N/A |
| **VULCAN-12** | Mixed | YES — MU FQ4 GAAP GM on a stated basis, **EXPLICIT NO-VERDICT BAND** | N/A |
| **VULCAN-15** | **YES — negative-existence** — "**NO mechanism** that FIRMLY reduces the ~55 GW / ~32 GW gap enters effect… **CONFIRMED if neither has occurred** by 2026-11-15" | **YES** — "a FERC order accepting PJM's IRAS including limb (c)" OR "NCBL becomes mandatory / takes effect in PJM" | **YES, and the row says why it is the strong form** — "⚠️ **ANCHOR IS `calendar`, DELIBERATELY, AND IT IS THIS BOOK'S FIRST NON-PUBLICATION ROW: gradeability does NOT depend on anyone publishing on schedule — on 2026-11-15 I look at the FERC docket and the answer is either 'an order exists' or 'it does not'. A FERC DELAY resolve[s]…**" |
| VULCAN-08/10/13/14/17 | NO (positive) | YES each (SEC filings, 6-K, filing-primary) | N/A |

**Counts: 9 candidates opened / 1 confirmed negative-existence class (+3 negative-shape on published series) / 0 lacking instrument / 0 lacking a dated precondition.**

🔑 **VULCAN-15 is the cohort's best answer to a problem the others work around rather than solve:** every other negative-existence row in this cohort depends on a publisher (Bloomberg, DTN, the PJM board) and therefore needs a VOID path for instrument silence. VULCAN-15 picks a **docket** instead of a **publication** — a docket's emptiness is itself the observation, so **a delay cannot make it ungradeable**. The row names this as a deliberate design choice and flags it as the book's first of the kind. That is worth promoting fleet-wide: **where a negative can be anchored to a registry rather than a publication, the VOID path disappears.**

### 7. As-made receipt — **n/a**

### 8. Cross-agent threads / pattern candidates
- 🔴 **To VULCAN (packet):** your STATUS publishes **L3**; FLEET_MAP and your profile both say **L4 (Conf H, 2026-09-05)**. `AGENTS/VULCAN/STATUS.md:5`. My fault, not yours — no packet was sent.
- 🔴 **To VULCAN (packet):** STATUS at **93% of the 32,550 B read cap**; rotate before the 9/30 MU session, which will be a heavy write.
- **To WATT:** your 9/11 STATUS still flags the S3 seam as open on meaning; VULCAN closed it 9/6 across 8 surfaces (see the WATT section).
- **PATTERNS candidate (promote, high value):** *Anchor a negative-existence prediction to a REGISTRY, not a PUBLICATION, and the VOID path disappears.* Evidence: `workbook/PREDICTIONS.tsv` VULCAN-15 criteria vs OSP-06's VOID path (`AGENTS/OSPREY/thesis/PREDICTIONS.tsv`) and FERT-12's publisher dependence. ⚠️ When promoting to `FORGE/PREDICTION_DISCIPLINE.md`, **scan the destination for apparent contradictions** — the existing search-instrument canon reads as *always name a search instrument and a dated attempt*, and this rule looks like an exemption. It is not: it **composes** — the registry IS the named instrument and the dated look IS the attempt; what disappears is only the *publisher-silence VOID branch*. Reconcile that in-line at the destination, per the MEMORY MODEL rule.
- **PATTERNS candidate:** *A "whichever is FIRST" trigger inherits every leg's date, so re-dating one leg silently re-dates the trigger — and nothing announces it.* VULCAN found this **twice in seven days, in opposite directions** (`workbook/EXIT_PROTOCOL.md:227`: 8/27 moved it earlier ~9/29→~9/22; 9/2 moved it later ~9/22→9/30). The desk's own diagnosis is the promotable sentence: "**The defect is not the direction, it is that a derived leg feeds a trigger with no publisher.**"

### 9. Reviewer-side defects
- **The scanner's REAL-STALE flag on `VULCAN/workbook/EXIT_PROTOCOL.md` is WITHDRAWN** and the misread is instructive: it took a line containing "re-derived" as a freshness label when the same line's parenthetical says "first authored." **A vintage scanner needs to detect the hybrid shape** (a STATE file carrying dated append-only entries) and prefer the newest entry heading. Recommend a `falsification_scan.py` change: when a file contains ≥2 dated entry headings newer than its header stamp, report the newest heading and mark the header as provenance.
- **VULCAN's L4 promotion (9/5, mine) never reached the desk.** 12 days of a wrong published grade.
- The `Gaps` cell's "latest stored month July" was superseded on 9/11 and the "tripwire candidate n=1 retained for September 12" item has no locatable disposition — a `Gaps` cell should not carry a dated item that no surface in the desk's tree can resolve.

---

# COHORT-LEVEL FINDINGS

### F1 🔴 The Market-L4 "TRADE.md feeding proposals" leg is applied inconsistently across four desks and has never been formally waived
Four of seven desks in this cohort have **no TRADE.md by charter** — HAWK ("Holds no trade book", `profiles/HAWK.md:11`), FALCON ("deliberately no TRADE.md", `profiles/FALCON.md:9`), OSPREY ("BRENT owns every price", `AGENTS/OSPREY/thesis/THESIS.md:21`), and VULCAN (absent, reason unstated). **Three of those four already sit at L4.** Meanwhile FERT is held at L3 with the leg counted against it, on a TRADE.md that is **deliberately frozen for a reasoned, dated cause** (`AGENTS/FERT/TRADE.md:20-23`).

The precedent was set without adjudication: `upgrades/PRODUCTION_REVIEW_2026-08-07.md:15` promotes FALCON L3→L4 on "**all legs cleared by more than asked**" — a blanket phrase that cannot be true of a desk with no TRADE.md. The leg was absorbed, not enumerated. That is exactly the failure the Meta-L5 note in `AGENTS/DAEDALUS/CLAUDE.md` forbids: "*Promotion adjudications should enumerate EVERY ladder leg with a per-leg verdict so a skipped leg reads as a blank, not an omission.*"

**Consequence:** the leg currently penalises the one desk that documented *why* it has no live book and waives itself for three desks that never had one. **This blocks a defensible OSPREY L4 and a defensible FERT L4, both of which meet every other leg.**
**Recommendation:** put it to the ladder sitting as a stated question — either (a) the leg reads "**TRADE.md feeding proposals, OR a charter clause assigning trade construction elsewhere, cited**", or (b) the four charter-exempt desks get an explicit per-desk waiver row. Not a reader's call; flagged, not acted on.

### F2 🔴 DAEDALUS publishes maturity grades that never reach the desks — and where they do reach, 2 of 3 are wrong
| Desk | FLEET_MAP | Desk's own STATUS | Delta |
|---|---|---|---|
| WATT | L4 (9/05) | "**Maturity: L4 (Conf H)** *(DAEDALUS 2026-09-05)*" `STATUS.md:4` | ✅ correct |
| **VULCAN** | **L4 (9/05)** | "**Maturity: L3** (DAEDALUS 8/7 Production Ready)" `STATUS.md:5` | 🔴 **one level low, 12 days** |
| **MIDAS** | **L4 (9/08)** | "**this desk is L3** on it" `STATUS.md:5` | 🔴 **one level low, 12 days** |
| HAWK · FALCON · OSPREY · FERT | L4 · L4 · L2 · L3 | **no maturity token at all** | grade never arrives |

**2 wrong of 3 present; 4 of 7 carry nothing.** Both wrong ones were promoted in the **same 9/5–9/8 pass**, and neither desk was packeted. MIDAS's line is the sharper case: it was written on 9/5 as a *deliberate correction* of a scale collision (`STATUS.md:5`, "Two scales, one token, on a surface peers read (DAEDALUS F-4)") — the desk fixed the token and got the value wrong, because nobody had told it the value.

**This is squarely my own closeout step 1c** (`consumer_check`): a maturity level is a figure I publish that other desks cite. I superseded VULCAN L3→L4 and MIDAS L3→L4 and ran no consumer check, sent no packet. **Recommendation:** send both packets (owners edit their own files — never edit them myself), and add the desk's own STATUS maturity token to the standing `render_directory.py` co-registration guard so the reverse direction is watched too. Cf. `finding_a_registry_reclassification_is_an_interface_consumers_guard_one_way`.

### F3 🔴 Read-cap: two desks are at or near breach
| Desk | STATUS bytes | % of 32,550 B cap |
|---|---|---|
| **MIDAS** | **32,158 B** | **99%** — 392 bytes of headroom |
| **VULCAN** | **30,313 B** | **93%** |
| FERT | 24,217 B | 74% |
| WATT | 23,439 B | 72% |
| OSPREY | 15,828 B | 49% |
| FALCON | 9,019 B | 28% |
| HAWK | 8,827 B | 27% |

MIDAS rotated 8 blocks on 9/11 and is **still at 99%**, which means the rotation cadence is losing to the append rate. Per root `CLAUDE.md` § Data Hygiene the response is rotation or a hot/cold split — **never raising the number**. Both need packets before their next heavy session (VULCAN's is 9/30, MU FQ4).

### F4 🟢 The negative-resolution canon has propagated fleet-wide — measured, not assumed
**Cohort totals: 21 OPEN rows opened / 10 negative-class confirmed / 0 lacking a named search instrument / 1 lacking an explicit dated search-attempt window (FAL-05, mitigated by an affirmative-evidence guard).**

Every desk that registered a negative-existence row named its instrument, and 9 of 10 carried a dated precondition. Three forms are now in service and they are complementary:
- **OSP-06** — publication-anchored, with a search window bounded at **both** ends (floor 10/08, ceiling 10/15) and a VOID path that refuses to confirm on instrument silence.
- **FERT-12** — the same shape plus all six WQ-162 elements, with the grade explicitly pointed at the **world state, never the author's log**.
- **VULCAN-15** — **registry-anchored** rather than publication-anchored, so the VOID path is structurally unnecessary.

And the propagation path is documented, not inferred: OSP-04's own resolution recorded the floor-without-ceiling defect **against its author's own row**, routed the fix to DAEDALUS/PROME rather than self-ruling it, and OSP-06 then FERT-12 adopted the ceiling. **That is a complete learn→route→adopt cycle visible in three ledgers across two desks.** Worth saying out loud at the sitting: this is the canon working as designed, and it is the strongest single result in the cohort.

### F5 🟠 Bare line anchors in FLEET_MAP evidence cells rot inside two weeks
Verifying the WATT row required chasing **three** dead anchors (`AEOLUS/STATUS:157` → `:86`; `VULCAN/STATUS:51` → `:53`; `WATT/STATUS:104` → rotated into `status_archive/`). All three facts survived; all three pointers died in ≤12 days. The same class hit `profiles/HAWK.md:9` (`:76`) and `profiles/FALCON.md:7` (`VX.tsv:6`). OSPREY already wrote the rule that fixes it — `AGENTS/OSPREY/CLAUDE.md:144`: "**Cite the SECTION, not the line** — a line anchor in a file that edits itself is a dangling pointer waiting to happen." **Recommendation:** adopt it for FLEET_MAP `Gaps`/`Notes` and `profiles/`: cite a section heading or a quoted string, never `FILE:NN`, for any surface that rotates.

### F6 🟠 Δ-blocks rot faster than the bodies they rescue
`profiles/HAWK.md:9` (Δ-block, 2026-08-15): **six of nine numbered corrections are now false** after 33 days, while the qualitative identity paragraph above it survived untouched. `profiles/OSPREY.md:3` vs `:5` carries a receipt banner that **contradicts the banner immediately below it** without retracting it — two live instructions where there should be one.
**The mechanism:** a Δ-block is written under time pressure as a *snapshot of counts* (STATUS lines, KB rows, inbox depth, book size). Counts are precisely the thing that moves. **Recommendation:** a Δ-block should carry **pointers and verdicts**, not counts — "STATUS is over its cap, see `read_cap_check`" instead of "STATUS 152 ln." Candidate PATTERNS row.

---

## COHORT SUMMARY

| Desk | Commits (self/routed) | Dark-days | Rec level / conf | Row-claims T/R/CE | Profile trigger | Falsification verdict | Neg-res (cand/neg/lacking) | Top finding (≤15 words) |
|---|---|---|---|---|---|---|---|---|
| **HAWK** | 24 / 60 | 0 | **HOLD L4 / H** | 4 / 2 / 1 | **FIRED** (FLOW-19/20 + book), checkpoint 9/15 missed | not in scope | 2 / 2 / 0 | Row names two deferrals the owner closed the same day it was written |
| **FALCON** | 31 / 45 | 1 | **HOLD L4 / H** | 2 / 4 / 1 | **CANNOT-EVALUATE** (no dated clock), checkpoint 9/15 missed | not in scope | 1 / 1 / **1** | All three named L5 gates cleared; row 16 days stale, clean-closeouts blocks |
| **OSPREY** | 19 / 23 | 1 | **PROMOTE L2 → L3 / H** | 3 / 2 / 0 | **FIRED** (THESIS v1.0 landed), checkpoint 9/15 missed | **RAIL-IN-LOCAL-FORM** (CLAUDE.md §EXIT RULES, ruled 9/8) | 1 / 1 / 0 | All four L3 legs met; strike_feed built 9/8, row still says unbuilt |
| **MIDAS** | 24 / 29 | 6 | **HOLD L4 / H** | 6 / 1 / 0 | **FIRED** (COT-grade cycle turned) | **RAIL-IN-LOCAL-FORM**, 2 REAL-STALE cells in the letter | 2 / 0 / 0 | STATUS at 99% of read cap; THESIS ✅-ticks a band gold has left |
| **FERT** | 6 / 8 | 2 | **HOLD L3 / H** | 5 / 0 / 1 | **NOT FIRED** (only clean trigger in cohort) | not in scope | 2 / 1 / 0 | L4 adjudicated: signals flow, TRADE.md frozen by reasoned design |
| **WATT** | 14 / 25 | 6 | **HOLD L4 / H** | 6 / 1 / 0 | **NOT FIRED** (9/26 or FERC ~10/12) | **STALE-BUT-CONSISTENT** — read 3× in period; one REFUTED from-state cell | 4 / 1 / 0 | Carries VULCAN seam as open; VULCAN closed it 9/6 across 8 surfaces |
| **VULCAN** | 30 / 27 | 4 | **HOLD L4 / H** | 3 / 1 / 1 | **NOT FIRED** (MU 9/30, issuer-primary anchor) | **WITHDRAWN** — hybrid surface, newest entry 9/13, not 8/13 | 9 / 1 / 0 | Own STATUS publishes L3; FLEET_MAP says L4 since 9/5, never packeted |

**Cohort totals:** 148 self-authored / 217 routed-in commits · **1 PROMOTE (OSPREY L2→L3), 6 HOLD, 0 DEMOTE** · row-claims **29 TRUE-STILL / 11 REFUTED / 4 CANNOT-EVALUATE** · profile triggers **3 FIRED, 3 NOT FIRED, 1 unevaluable** (and **3 of 7 profiles missed a 2026-09-15 checkpoint**) · falsification **1 WITHDRAWN, 1 STALE-BUT-CONSISTENT, 2 RAIL-IN-LOCAL-FORM** · negative-resolution **21 / 10 / 0 lacking instrument, 1 lacking a dated window**.

**The one-line read:** *the desks are in better shape than their FLEET_MAP rows say — 11 of 44 row-claims are refuted and every refutation runs in the desks' favour — while DAEDALUS's own layer has three live defects: an unadjudicated ladder leg (F1), two undelivered promotions (F2), and evidence anchors that rot in under two weeks (F5).*
