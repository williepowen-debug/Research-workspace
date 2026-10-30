# CREED charter — history moved out 2026-10-30 (verbatim, line-mapped)

⛔ **HISTORY, NOT CURRENT — do not cite as current. The rules are in `AGENTS/CREED/CLAUDE.md`.** Moved 2026-10-30 under Will's instruction (pasted in CREED's session, 18:41 ET): *"Fix the 11 wrong statements, cut the duplicates, and move the history word for word into an archive file … Keep every rule, warning and step number … List every line you removed and show where it now lives in the archive file, so nothing is silently dropped."* Review: `research/2026-10-30_CHARTER_REVIEW.md`.

**Pre-change charter:** 40,535 B, git blob at commit `a475b7cb7` (`git show a475b7cb7:AGENTS/CREED/CLAUDE.md`), crc32 `28bbbcb9`. **Method:** every non-blank line of the old file that is not present word for word in the new file is reproduced below, under its OLD line number, with a crc32 of the line, its disposition, and where its rule now lives. Lines kept verbatim are not repeated. A script checked that the set below equals the set of changed lines (83 lines, none unmapped).

**Dispositions:** FIXED = the statement was wrong on 2026-10-30 · DUPLICATE = the same rule lives elsewhere (named) · HISTORY = reasons/incidents/dates, rule kept · COMPRESSED = rule kept in shorter form, full text here · CHANGED = Will-ruled change (boot reads, 2026-10-30) · REWORDED/MERGED = same rule, new wording or place.

## Index

| Old lines | Disposition | Rule now lives at |
|---|---|---|
| 16 | FIXED (stale: MF scoring is HOMER's since 7/27; case-ledger role was missing) | §Mission "Own" — multifamily data + named cases; new case-ledger bullet; "Do not own" multifamily scoring |
| 26 | HISTORY removed (the 7/27 correction story); rule kept | §Mission "Feed" — CARL non-MF, multifamily routes to HOMER |
| 39 | HISTORY removed (6/28 consolidation note); rule kept | §Route Matrix italic note |
| 46 | FIXED (pointed at "the caveat below", now a one-line rule) | §Route Matrix S5 row |
| 50 | FIXED ("PROME to reflect" — done, _NETWORK.md:97-98); history trimmed | §Route Matrix pension row |
| 54 | FIXED (said PROME git mv's CREED's inbox; CREED files its own) | §Route Matrix standing rule |
| 60 | FIXED + HISTORY (said full versions live in SCRATCH — inverted; promotion history) | §Standing traps preamble ("This copy is canonical") |
| 62 | COMPRESSED (trap #1: rule + one example kept; incident record here) | §Standing traps #1 |
| 63 | COMPRESSED (trap #2: rule + one example kept; incident record here) | §Standing traps #2 |
| 64 | COMPRESSED (trap #3: rule + one example kept; incident record here) | §Standing traps #3 |
| 65 | COMPRESSED (trap #4: rule + one example kept; incident record here) | §Standing traps #4 |
| 66 | COMPRESSED (trap #5: rule + one example kept; incident record here) | §Standing traps #5 |
| 67 | COMPRESSED (trap #6: rule + one example kept; incident record here) | §Standing traps #6 |
| 68 | COMPRESSED (trap #7: rule + one example kept; incident record here) | §Standing traps #7 |
| 69–72 | COMPRESSED (trap #7 instances ①–③ and the closing rule; rule + example ③ kept) | §Standing traps #7 |
| 74 | FIXED + COMPRESSED (trap #8: "check 1 is file-level" false since 2026-10-30; incidents here) | §Standing traps #8 |
| 80 | HISTORY removed (creation note) | Boot step 0 |
| 84 | HISTORY removed (REVIVAL_PLAN slot note) | Boot step 4 |
| 86 | HISTORY removed (build date, runtime) | Boot step 4c |
| 87–88 | HISTORY (why the scan was built; fixture record) | Boot step 4c (rule only); MAINTENANCE.md §2026-08-27 |
| 89 | COMPRESSED (n=12 counter build history) | Boot step 4c "🟠 DUE" bullet |
| 90 | COMPRESSED (rule kept) | Boot step 4c "Read the UNSCANNABLE register" bullet |
| 91 | COMPRESSED (rule kept) | Boot step 4c "TRIPPED" and "LEG k/n" bullets |
| 92 | FIXED (stale: T-06b now wired to VX-5.03, T-06 to VX-5.01 [QUALITATIVE-VALUE]) | — (resolved; no rule) |
| 93 | HISTORY removed (path-move note) | Boot step 5; §Source Archive |
| 95 | HISTORY removed (re-pointing history); rule kept | Boot step 6.1 |
| 96 | HISTORY removed (why demoted 9/30); rule kept | Boot step 6.2 |
| 97 | REWORDED (adds the MECHANISMS.md pointer) | Boot step 6.3 |
| 98 | CHANGED (Will 2026-10-30: read the newest 3 entries at boot) | Boot step 6.4 |
| 99 | CHANGED (Will 2026-10-30: ON DEMAND, not a boot read) | Boot step 6.5 |
| 100 | MERGED with old line 209 (duplicate S8a rule); stale "read its header" note dropped | Boot step 6.6 |
| 101 | CHANGED (Will 2026-10-30: ON DEMAND, not a boot read) | Boot step 6.7 |
| 102 | HISTORY removed (split date, 107% figure); rule kept | Boot step 7 |
| 103 | HISTORY removed (ruling and wording-edit parentheticals); rule kept | Boot step 7b |
| 111 | FIXED (LEDGER_GLOB also carries cases/*.tsv) + HISTORY removed ("Six files" story) | §Workbook first paragraph |
| 122 | COMPRESSED (mtime-find replacement history; rule kept) | §Workbook "No file-level check sees a stale ROW" note |
| 124 | REWORDED (rule kept) | §Workbook calibration note |
| 132–140 | HISTORY (8/13 courier-kill decision record; premise ② now false — Trepp is PRIMARY-READ since 8/20); the standing rule kept | §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row |
| 149 | HISTORY removed (CATO attribution); rule kept | Closeout step 2 |
| 150 | HISTORY removed (CATO attribution); rule kept | Closeout step 3 |
| 151 | HISTORY removed (BROCK BRK-29 anecdote); rule kept | Closeout step 4 |
| 154 | HISTORY removed (why added); rule kept | Closeout step 6b |
| 155 | REWORDED (Tier-2 rationale trimmed); rule kept | Closeout step 7 |
| 156 | HISTORY removed (layout dates, NEXUS note); rule kept | Closeout step 8 |
| 157 | HISTORY (retired 320-line recipe pointer) | MAINTENANCE.md §2026-09-30 |
| 158 | COMPRESSED (dates, falsification record); rule kept; check ① wording updated to the line-scoped form | Closeout step 8b |
| 159 | HISTORY (why the self-check exists) | MAINTENANCE.md (2026-08-20 sweep) |
| 160 | COMPRESSED (claim_check scoping lesson); rule kept | Closeout step 8b first note |
| 161 | REWORDED (rule kept) | Closeout step 8b second note |
| 162 | HISTORY removed (why added); rule kept | Closeout step 8c |
| 169 | DUPLICATE trimmed (third copy of the path-move story) | §Source Archive first paragraph |
| 179–180 | FIXED (dead reference to a file deleted 6/28) | — (no rule; file gone) |
| 182–183 | MERGED into the Source Archive list | §Source Archive list, last bullet |
| 198 | FIXED ("June" packs are June–July) | §Current Stale-State Warning |
| 204 | DUPLICATE (of boot step 6) | §Current Rails first paragraph (pointer to step 6) |
| 206–208 | DUPLICATE (same files as boot steps 6.3–6.5) | Boot steps 6.3–6.5 |
| 209 | DUPLICATE + HISTORY (S8a rule twice; old pointer-lag story) | Boot step 6.6; §Current Rails S8a bullet |
| 210 | DUPLICATE (boot step 6.7) | Boot step 6.7 |
| 212 | DUPLICATE (boot step 6.2) | Boot step 6.2 |
| 214 | REWORDED (bullet form) | §Current Rails second bullet |
| 220–227 | DUPLICATE of thesis/THESIS.md §Current State Classification (incl. Will's WQ-356 wording) | thesis/THESIS.md §Current State Classification; §Working Hypothesis pointer |
| 233 | DUPLICATE trimmed (path-move history, third copy); rule kept | §Guardrails first bullet |

## Verbatim lines

### Old L16 — crc32 `a5b99ea9` → §Mission "Own" — multifamily data + named cases; new case-ledger bullet; "Do not own" multifamily scoring

- multifamily stress outside Florida-specific CORAL scope

### Old L26 — crc32 `db8b09af` → §Mission "Feed" — CARL non-MF, multifamily routes to HOMER

- `CARL` — **housing-consumer spillovers (non-MF)**. ⚠️ **Multifamily moved to HOMER 2026-07-27** — this line said *"multifamily / housing-consumer"* until the 7/27 LIQUID/CORAL/HENRY-CARL survey caught it **contradicting CREED's own Route Matrix below**, which already read *(non-MF)*. Fourth surface hit by the same one-surface S5 edit.

### Old L39 — crc32 `25241609` → §Route Matrix italic note

*Consolidated 2026-06-28 per DAEDALUS BATCH_01 — single lookup; the per-signal Response lines in `thesis/THESIS.md` §Expected Signals + §Agent Handoffs stay canonical for detail.*

### Old L46 — crc32 `8541a2c2` → §Route Matrix S5 row

| Multifamily CMBS row / term-default / Sun-Belt realization **(S5 — HOMER-OWNED as of 2026-07-27)** | **HOMER** | 🟠 | the MF row from CREED's whole-Trepp pull; MF-relevant lender evidence. **HOMER owns the SCORING and JUDGMENT. CREED does not score S5 or publish it as an independent CREED vote.** ⚠️ **Ownership of the DATA PULL is a SEPARATE assignment and must be stated, not assumed** — see the caveat below |

### Old L50 — crc32 `442069f2` → §Route Matrix pension row

| **CRE assets migrating onto PENSION balance sheets** (fast→slow recognition holder; added 2026-10-22, Will-approved *"okay go ahead now"*; found by eval case 02) | **SHADE** (info) + PROME (info) | 🟡 | named transactions, size and holding vehicle; SHADE owns the combined-sink question. Info-only until a live case shows an ACTION route is needed. Canonical topology: `AGENTS/_NETWORK.md` (PROME to reflect) |

### Old L54 — crc32 `4d183215` → §Route Matrix standing rule

Standing rule: route to the **domain owner**, one signal at a time, transmission-relevant only. CREED reports inbox dispositions; PROME `git mv`s. No outbox spam.

### Old L60 — crc32 `03dca1dd` → §Standing traps preamble ("This copy is canonical")

> **Why these are duplicated here instead of only in `SCRATCH.md`.** HENRY's eval suite makes the distinction sharp: **a principle expressed as a BOOT STEP is not in the always-loaded surface.** `SCRATCH.md`, `STATUS.md` and `COVERAGE.md` are boot *steps* — they load if boot runs and is read closely. **The always-loaded surface is this file's body plus auto-memory.** Every trap below fires **while writing a number**, not at boot — so a session that skims boot would lose exactly the ones that cost CREED most. Full versions stay in `SCRATCH.md`; **these eight are load-bearing enough to live here.** *(#6 and #7 promoted 2026-08-20 morning; **#8 promoted 2026-08-20 late — it bit TWICE the same day and survived both a dedicated sweep and a self-audit of that sweep, which is the strongest promotion case the block has seen.** #6 and #7 both fired at write-time during the `CREED-T-02` session, and #7 is the defect that made trap #3 dangerous in its old blanket form. ⚠️ Promotion has a cost: this block is always-loaded, so it is curated, not a dumping ground — a trap earns a place here only by having actually bitten CREED while writing a number.)*

### Old L62 — crc32 `0b757108` → §Standing traps #1

1. **Never cite a CRE mREIT price move without checking corporate actions first.** ARI printed **−33.4% in a single session** on a total-return-*positive* day — the $3.75 return-of-capital going ex 7/16. The tell is not "mREIT"; it is **any vehicle that returns capital** (liquidating trusts, wind-downs, special dividends, spin-offs). PROME logged **five instances of this class fleet-wide on 2026-07-27 alone.**

### Old L63 — crc32 `f79bb020` → §Standing traps #2

2. **A real number carrying the WRONG BASIS is the dominant failure mode — not a fabricated number.** ARI's ~$1.3B was real: a *cash* line on a *pre-close* date, labelled "post-sale." **CREED-held post-sale size is $2.2B total assets / BVPS $12.05 at the 4/24/26 close.**

### Old L64 — crc32 `86cef60a` → §Standing traps #3

3. **Trepp source tier is MONTH-SCOPED — CHECK `AGENTS/WALTER/sources/` BEFORE ASSUMING EITHER WAY.** *(Rewritten 2026-08-20; this trap previously read "Trepp PDFs are paywalled ⇒ PRIMARY-CITED, not PRIMARY-READ" and that blanket form had become actively harmful.)* **Apr–Aug 2026 are archived there as readable PDFs and were read directly** (`pdfminer`), which is how `CREED-T-02` was verified before firing and how the July maturity-adjusted DQ — recorded by CREED *and* HOMER as "not published" — turned out to be published all along at **9.62%**. 🆕 *(Widened 2026-09-30, Will-approved: the August DQ + SS PDFs have been archived since 9/27; the 9/02 "gated" belief about August was a retrieval-shape error, trap #7.)* 🆕 **September 2026 is archived in a DIFFERENT place:** `AGENTS/WALTER/research/2026-10-16_finish/credit-trepp-dq.pdf` / `credit-trepp-ss.pdf` (read 2026-10-21) — **so check `AGENTS/WALTER/research/*/credit-trepp-*.pdf` too, not only `sources/`** (a single-folder check is the trap-#7 retrieval-shape failure). **For a month in neither place, try the public `trepp.com/hubfs/` PDF (browser UA) before calling it paywalled;** only if that fails is paywalled/primary-CITED the default. ⚠️ **Never let this trap talk you out of trying:** an always-loaded "you can't read it" is exactly the unfetched-is-not-unavailable failure, encoded where every session sees it. The co-circulating **"retail 12.95%" is UNVERIFIED — do not cite.**

### Old L65 — crc32 `4238b84b` → §Standing traps #4

4. **Anchor a threshold to a DISTRIBUTION, not to the most recent number.** `PRED-CREED-006` was written against "the Q1 pace of +$3.3B" — a **seasonal trough** — so a routine +$11B print would have resolved it TRUE carrying zero information. **The bar failed on its baseline, not its threshold.** One prior observation cannot tell you whether it is representative.

### Old L66 — crc32 `49e41765` → §Standing traps #5

5. **MBA FIGURES ARE ATTRIBUTED BY A PERIMETER YOU MUST NAME BEFORE YOU QUOTE ONE — and the perimeter is never in the number.** **The $775B life-insurer line is WHOLE-LOANS-ONLY.** MBA attributes to the **note-holder**, so insurer-held CMBS sits in the separate CMBS/CDO/ABS bucket (~$637B). **It is a FLOOR on insurer CRE exposure, not a measure of it** — never present it as "what insurers hold in CRE," and never let it be summed against a differently-constructed perimeter. `KB-CREED-017`. 🆕 **WIDENED 2026-08-28, second instance, different MBA product:** the **CREF Loan Maturity Volumes survey** reports **PROPERTY type in PERCENT** (*"Thirteen percent of mortgages backed by multifamily properties will mature in 2026"*) and **LENDER type in DOLLARS** ($396B depositories · $200B CMBS/CLO/ABS · **$163B** credit companies/warehouse/other · $39B GSE-FHA-Ginnie). ⇒ **there is no multifamily dollar in it**, and converting the share into one requires a denominator the survey does not give you (**trap #6 + the derived-quantity trap**). 🔴 **AND THE `$160B+` MF MATURITY WALL IS SETTLED — RETIRED 2026-08-28, VERDICT NOT ATTACHABLE (`KB-CREED-028`). DO NOT CITE IT, AND DO NOT RE-OPEN THE SEARCH.** **It was never Trepp's:** the sentence is attributed **by its own source article** (Multifamily Dive 2026-05-12) to **a SPONSOR — Tyler Chesser, CF Capital** — sitting in a piece whose **headline credits Trepp for a different figure**. ⭐ **PROVENANCE BY CO-LOCATION: a figure inherits the source named nearest it, and the mislabel then survives every re-sourcing attempt because a wrong attribution fails as an ABSENCE, not as an error.** **The decisive structural fact: Freddie Mac sources its OWN MF-maturity exhibits to MBA, and MBA publishes multifamily as a PERCENTAGE with no dollar** — so the dollar is not public at all. **Replacement, sourced: "13% of MF-backed mortgage balances mature in 2026" [MBA CREF survey, rel. 2026-02-09] — a SHARE.** ⚠️ **CREED's own 8/28-morning `$163B` lender-type hypothesis is REFUTED** (the MF figure runs **+50% YoY** while MBA's total ran **−9%**; opposite directions cannot be one series) — **it shipped with a test attached and died on it, which is the instrument working.** `KB-CREED-017` + `KB-CREED-027` + `KB-CREED-028`.

### Old L67 — crc32 `e6453dbd` → §Standing traps #6

6. **🆕 A SHARE IS NOT A TREND WHEN ITS DENOMINATOR MOVES — name the denominator before you write any shape word.** `CREED-T-02`'s share read **70 → 65 → 66** and was reported onward as *"peaked in May, not a wave starting."* The denominator swung **2.3×**, and the underlying quantity ran **$1.10B → $2.83B → $1.72B → $3.96B — July was the PEAK.** Both readings are arithmetically correct and they support **opposite theses.** **Before writing "peaked" / "building" / "decaying" / "plateauing" about any share: ① is this a ratio or a quantity? ② if a ratio, did the denominator move?** If you can't answer, **report the component levels and say the shape is ungraded.** ⚠️ **Verifying the figures does NOT verify a shape claim built across them** — the series here was correctly sourced, correctly dated and primary-verified, and the shape verdict was still backwards.

### Old L68 — crc32 `85302a4d` → §Standing traps #7

7. **🆕 ABSENCE INFERRED FROM RETRIEVAL SHAPE — `n=3`, ONE DOCUMENT CLASS. "NOT PUBLISHED" USUALLY MEANS "NOT FETCHED"; "NOT IN THE TABLE" USUALLY MEANS "IT IS IN THE PROSE."** ⚠️ **This trap was WIDENED 2026-08-27 because its old wording would not have caught its own third instance.** It read only *"NOT PUBLISHED almost always means NOT FETCHED"* — and instance ③ never said "not published." It said **"no metro detail is reachable, so no FL slice exists to send,"** which the trap's trigger phrase does not match. **The common defect is not the word; it is concluding a FACT is absent from the failure of ONE retrieval shape.**

### Old L69 — crc32 `ccbb97cb` → §Standing traps #7

   - ① **July maturity-adjusted DQ** — CREED (8/13) and HOMER (8/12) both recorded it unpublished. **Both had reached only the Connect-CRE secondary; the figure sat in the Trepp PDF in plain prose at 9.62%.** **Two readers of one upstream are ONE source** — agreement proved a shared CHANNEL, not an absence.

### Old L70 — crc32 `7c22ab63` → §Standing traps #7

   - ② **`PRED-CREED-009`** held at 30% *explicitly* because *"CREED does not receive the composition split monthly"* — **false when written** (Trepp prints the split in prose every month), and it resolved TRUE. ⚠️ **Never price a prediction's confidence on an untested resolvability assumption:** a confidence low for a false reason **scores as well-calibrated when it resolves FALSE and teaches nothing when it resolves TRUE.**

### Old L71 — crc32 `55724c29` → §Standing traps #7

   - ③ 🆕 **The CORAL FL slice** — blocked 24 days on *"no loan-level/metro detail reachable ⇒ no FL-specific slice exists."* **The FL content was in the named-loan NARRATIVE the whole time**, and it was a Florida hotel portfolio that moved the national lodging rate 79bp. **Trepp's monthlies contain exactly two tables, both national — so the table CREED was waiting for does not exist and never will.** Meanwhile WALTER found the same asset in the prose and routed it directly.

### Old L72 — crc32 `b840513d` → §Standing traps #7

   ⇒ **BEFORE writing that a figure is unavailable, name WHICH SHAPE you looked for and say whether you checked the others** — table, narrative, footnote, chart label. ⚠️ **Waiting for a shape that does not exist is indistinguishable from waiting for data that has not printed**, and it fails silently for as long as you keep waiting.

### Old L74 — crc32 `b8fc935e` → §Standing traps #8

8. **🆕 A PARTIAL REFRESH OF A BLOCK CERTIFIES THE PART YOU DIDN'T TOUCH — RE-READ THE WHOLE UNIT BEFORE CLOSING AN EDIT.** Editing one cell, bullet or clause **freshens the entire unit's apparent vintage**, so the stale neighbours **inherit the fresh edit's credibility and become HARDER to catch than if you'd left the block alone.** ⚠️ **This bit CREED TWICE on 2026-08-20 and survived a dedicated staleness sweep *and* a self-audit of that sweep:** `THESIS`'s convergence blockquote had its first bullet refreshed to **25/45** while its closing sentence still read ***"Nothing FIRED"*** — ten lines below the fire record, on the canonical thesis surface, asserting the opposite of the day's headline — **and the same block's "20/40" arithmetic was silently wrong on the new basis (22/40), so the *reasoning* had gone stale, not just the number.** `COVERAGE`'s blind-spot intro read *"four of the five"* while its own table held **seven** rows and its own closing line said **5 of 7** — **a line that had ALREADY drifted once and carried a correction note about it.** **A note about a past drift does not prevent the next one.** ⚠️ **`creed_selfcheck` is blind to this by construction** — check 1 is **file-level**, so a file with fire markers *elsewhere* passes clean. **Both instances were found by DAEDALUS's structural review, not by CREED's guards** (`PAT-117`, n=2 cross-desk in one day). **Refresh at the UNIT boundary, not the file.** 🆕 **A GRADE IS NOT A PROPAGATION** *(added 2026-09-30, Will-approved)*: when a source is graded, **list every vector the source feeds and update each one.** 2026-09-29: grading the MBA Q2 pair did not reach `VX-10.05` until CATO caught it.

### Old L80 — crc32 `8b087749` → Boot step 0

0. **Read `AGENTS/CREED/SCRATCH.md` FIRST** — the handoff surface: what the last session was mid-way through, next-boot first moves, open threads, and the standing traps. **Ephemeral and lowest-authority: if SCRATCH disagrees with STATUS, STATUS is right.** *(Created 2026-07-27 after an unclean shutdown left CREED with no surface describing its own in-flight work.)*

### Old L84 — crc32 `cdac3639` → Boot step 4

4. **Read `AGENTS/CREED/COVERAGE.md`** — the map of the territory: what each lane covers, its **data vintage** (not its touch date), how well-built it is, and the **blind-spot register with the FINDER recorded**. *(`REVIVAL_PLAN.md` held this slot until 2026-07-27; it is a closed episode doc, now FROZEN and out of the boot order — its two live items were forked up to §Guardrails and `MAINTENANCE.md`.)*

### Old L86 — crc32 `06dac547` → Boot step 4c

4c. **🔴 RUN THE THRESHOLD SCAN NOW — `python3 AGENTS/CREED/scripts/threshold_scan.py`** *(built 2026-08-27; ~30ms, read-only, exit 0 clean / exit 1 needs attention).* Current vector values vs all frozen bands, **at boot, before the session does any work** — the same logic as 4b: **a trigger sitting past its band is information this session needs BEFORE it starts, not a thing to discover at closeout.**

### Old L87 — crc32 `384156bf` → Boot step 4c (rule only); MAINTENANCE.md §2026-08-27

   > **Why it exists — this is `CREED-T-02`'s root cause, unbuilt for three sessions.** On 2026-08-13 CREED wrote **"66% of $6.0B"** into its own workbook — the T-02 metric, against a frozen band of **50** — **and did not grade it.** The fire was effective at the June print and went unnoticed **~6 weeks**. The FORUM-5 K5 test **falsified the obvious explanation**: dark cadence was NOT the defect. **CREED was awake, holding the number, with the band written down, and nothing connected the two.** No boot step read the registry.

### Old L88 — crc32 `c983b38d` → Boot step 4c (rule only); MAINTENANCE.md §2026-08-27

   > **Verified against the real event, both wirings** *(fixtures, 2026-08-27)*: on today's wiring it reports `CREED-T-02` **TRIPPED**; on the actual 8/13 wiring — where `VX-CREED-3.04` did not yet exist — it reports it **UNTRIPPABLE BY CONSTRUCTION**, which is the diagnosis that would have prompted building `3.04` six weeks earlier. **It catches the event by two different lines, and the second is the more useful one.**

### Old L89 — crc32 `87cdd89b` → Boot step 4c "🟠 DUE" bullet

   > 🆕 **It is also obligation (D)'s n=12 COUNTER** *(implemented 2026-09-29, CATO CW5; it had been named as the counter since 8/27 but never counted).* It counts distinct `CANONICAL` numeric periods per banded vector in `VX_HISTORY.tsv`, prints `n=X/12`, and prints `🟠 DUE` (rc 1) when a per-band base-rating memo is owed. That is not a fire. Boundary-tested on fixtures: 11 → not due; 11 + a DUPLICATE row → still 11; 12 → DUE; no Role column → FAIL-LOUD.

### Old L90 — crc32 `e5197956` → Boot step 4c "Read the UNSCANNABLE register" bullet

   > ⚠️ **READ THE UNSCANNABLE REGISTER, NOT JUST THE GREEN.** A numeric pass covers only rows carrying **both** a numeric band **and** a metric vector — a minority — and **says nothing about the rest.** The scan enumerates every unscannable row by name and reason on every run for exactly this reason. **`⛔ BLOCKED` is NOT clear**: it means the comparison is not a valid verdict on the registered basis, which is a *worse* state than being near a band.

### Old L91 — crc32 `bce1b929` → Boot step 4c "TRIPPED" and "LEG k/n" bullets

   > ⚠️ **A `🔴🔴 TRIPPED` line is an instruction to GO GRADE THE TRIGGER AT PRIMARY. It is not a fire.** *(Since 2026-10-30 a sustain trigger whose leg is already graded prints `🟠 LEG k/n` instead — only when the registry state cell names that leg, value and period; any new print reverts it to TRIPPED.)* Adjudication is a CREED act against primary sources, recorded in `registry/CREED_T_FIRED_LOG.tsv`. **The scan reads state and never writes any.**

### Old L92 — crc32 `393602e7` → — (resolved; no rule)

   > 🆕 **Live finding from its first run:** **`CREED-T-06` and `CREED-T-06b` carry numeric bands with NO metric vector — the identical K5 shape, n=2, never counted.** Not adjudicated here; see `MAINTENANCE.md`.

### Old L93 — crc32 `46e53336` → Boot step 5; §Source Archive

5. Treat legacy CREED material under `AGENTS/REGINALD/archive/sub-agents/CREED/` as **source archive**, not current truth. *(Path updated 2026-10-22: REGINALD moved it from `sub-agents/CREED/` on 2026-08-13, commit `a7bae0d06`, Will-directed.)*

### Old L95 — crc32 `236ef5bf` → Boot step 6.1

   1. 🔴 **CURRENT STATE — `AGENTS/CREED/STATUS.md` (the HOT file: header + §Standing Obligations + §BOTTOM LINE), then the CURRENT catch-up named at `catchups/INDEX.md` (whichever file INDEX marks **CURRENT**; this step deliberately names no date so it cannot lag — re-aligned 2026-09-30 with step 8), then `registry/THRESHOLDS.tsv` + `registry/CREED_T_FIRED_LOG.tsv` + the newest `registry/PREREG_*_TREPP_PRINT.md` (frozen letter ABOVE its line; graded record BELOW it) + the newest `workbook/KB.tsv` rows.** *(Re-pointed **2026-09-26** in the SAME COMMIT as the STATUS hot/cold split — catch-ups no longer live in STATUS, so this slot names the INDEX, not a dated section, and cannot be orphaned by the next catch-up. Prior pointer (§2026-09-02 + KB-022/023/024/029 + PREREG_2026-09) preserved in git history; §2026-09-02 now lives at `catchups/2026-09-02.md`.)* 🔴 **§Standing Obligations is a boot read in its own right** — a byte-clean split can silently delete an owed action while every byte check passes (NEXUS 9/02).

### Old L96 — crc32 `961051c3` → Boot step 6.2

   2. **ON DEMAND, not a boot read** *(changed 2026-09-30, Will-approved: it was a closed pack read whole at every boot, at 100% of the read budget)*: `AGENTS/CREED/research/REFRESH_2026-07-27.md` — **PRIOR PACK, historical reference.** Open it only when a question needs its source trail. Still the best source-trail for the CRE lender leg, June SS resolution and life-science bifurcation. ⚠️ **It predates the T-02 fire and the Trepp source-tier upgrade — read it as a trail, not as current state.** (`REFRESH_2026-07-04.md` = June-Trepp / recognition-cluster trail; `REFRESH_2026-06-21.md` = FDIC-Q1 / maturity-wall trail.)

### Old L97 — crc32 `e292e710` → Boot step 6.3

   3. `AGENTS/CREED/thesis/THESIS.md`

### Old L98 — crc32 `a64baad9` → Boot step 6.4

   4. `AGENTS/CREED/thesis/CHANGELOG.md`

### Old L99 — crc32 `dc037e21` → Boot step 6.5

   5. `AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md`

### Old L100 — crc32 `49bda398` → Boot step 6.6

   6. `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md` — ⚠️ **read its header first**; the S8a level and its *direction* were both revised on 2026-08-20 (afternoon). **Recompute with `scripts/s8a_relative.py` before citing S8a.**

### Old L101 — crc32 `93226069` → Boot step 6.7

   7. `AGENTS/CREED/archive/LEGACY_PULL_FORWARD_2026-06-21.md`

### Old L102 — crc32 `08943d39` → Boot step 7

7. **Read `AGENTS/CREED/workbook/VX.tsv`** (the live metric layer — 34 vectors mapped to the Expected Signals) **and run the staleness check below.** ⚠️ **Since 2026-09-26 its Notes column is HOT-TRUNCATED** (VX.tsv had reached 107% of the hard read cap): full verbatim notes, including every basis/perimeter caveat, live in `notes/VX_NOTES.md`. **Read that file on demand, grepping by vector ID; it is not a boot read.** Read a vector's full note before citing its value in a caveat-sensitive way, and write new notes there, not into the cell.

### Old L103 — crc32 `d607cab9` → Boot step 7b

7b. **R1 corrections check (fleet-wide — FORUM-6 ruling ①, Will-approved 2026-08-17):** `python3 "$(git rev-parse --show-toplevel)/scripts/corrections_boot_check.py" CREED` — §9 rc 0/1/2; **rc=1 = a NAMED correction is unreceipted:** read the pointer, then `--receipt <id> --action <A>` with the WQ-399 fields in the script header (the writer refuses an incomplete receipt, rc 2). Then commit `registry/corrections_receipts.tsv`. *(Receipt line updated 2026-10-21 per SIG-W-20261008-033, a C4 own-charter wording edit; no authority, route or threshold moved.)* *(Wired 2026-08-28, DAEDALUS wiring sweep leg ①, batch Will-approved in-session.)*

### Old L111 — crc32 `987ebd26` → §Workbook first paragraph

The workbook (`AGENTS/CREED/workbook/`, built 2026-07-27) is the **live metric layer** under the prose rails. **Nine files:** six TSVs — `SCHEMA.tsv` · `VX.tsv` · `FLOW.tsv` · `KB.tsv` · `PREDICTIONS.tsv` · `VX_HISTORY.tsv` — plus `PREDICTIONS_SCOREBOARD.md`, `WORKBOOK_DESIGN.md`, and **`LEDGER_GLOB`** (added 2026-08-20: the staleness-enforcement declaration, `workbook/*.tsv registry/*.tsv` — ⚠️ **it exists because `registry/` had been outside ALL staleness enforcement, the exact surface class whose staleness produced K5**). *(Said "Six files" until 2026-08-20 while `README.md` correctly listed eight — the two files disagreed with each other for ~3 weeks. Counts are now checked mechanically at closeout by `scripts/creed_selfcheck.py`.)* **The threshold registry is separate and does NOT live here — see `registry/` below.**

### Old L122 — crc32 `e5f4409d` → §Workbook "No file-level check sees a stale ROW" note

> ⚠️ **Replaced 2026-09-29 (CATO CW5): this step used to be an mtime `find`.** Git sync rewrites mtime, so the old check failed false-negative: a just-touched file with stale ROWS read fresh. The fleet tool above reads each ledger's `Last real data refresh` header first. **Neither version sees a stale ROW inside a recently refreshed file.** Before citing a vector, read that row's own `Last_Updated` (VX) or period (VX_HISTORY). A fresh file header certifies only the rows that edit touched (trap #8).

### Old L124 — crc32 `c221751c` → §Workbook calibration note

> **Calibration note — this alert is not an accusation.** CREED is **Tier-2 spawn-on-need**; staleness *between* spawns is the expected steady state, not neglect. The alert exists to force a refresh **before** citing, not to imply a missed duty.

### Old L132 — crc32 `956c7a37` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

> ⚠️ **S5 SOURCING — courier arrangement KILLED 2026-08-13, after ONE cycle, per PROME ruling row 47 (2026-08-12, `PROME/proposals/2026-08-12_rule-batch-RULED.md`).** History for the source trail: the 7/27 circular-citation defect (CREED cites HOMER, HOMER's figure attributed to "(CREED 7/4 pull)" — `finding_circular_corroboration_via_state_file`) led HOMER to ratify option (b) on 7/31: *CREED couriers the whole-Trepp MF row monthly; HOMER scores and cites "Trepp via CREED pull, <date>."* **The July cycle (~8/4 print) was the first live test. CREED was dark 7/27→8/12 (17 days, no spawn); no packet went out; HOMER waited, got nothing, and self-pulled from Connect CRE/Chandan** — HOMER's 8/12 packet named the design flaw precisely: *"a courier that never couriers produces no artifact to detect."* Ruled item #1 of the 8/13 launch brief: either a heartbeat artifact per cycle, or kill.

### Old L133 — crc32 `1363f226` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

>

### Old L134 — crc32 `1883c5d4` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

> **KILLED, not heartbeat-repaired — reasoning (CREED's call, 2026-08-13):**

### Old L135 — crc32 `0490902b` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

> 1. **The circular-citation problem the courier was built to fix is already solved by HOMER's own disclosure practice**, independent of any courier: HOMER now marks inherited figures "(CREED 7/4 pull)" explicitly and cites fresh prints straight to Connect CRE/Chandan. No double-count risk survives either way.

### Old L136 — crc32 `d1a231b8` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

> 2. **The courier added zero source-tier improvement.** CREED's own MF-row citation is *itself* SECONDARY — `VX-CREED-1.01`/`1.02` read "Trepp Jun via Connect CRE/Yield PRO ~7/2 **(SECONDARY)**" — the same Connect CRE channel HOMER now cites directly. Routing through CREED added a hop, not a source tier.

### Old L137 — crc32 `d83cd9b6` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

> 3. **The arrangement's single point of failure was CREED's own spawn cadence** — Tier-2, Will-gated, unpredictable (17 days dark this cycle) — for a function (monthly-cadence delivery) a spawn-as-needed agent cannot structurally guarantee. That is not a discipline failure "try harder" fixes (per the ruling's own words); it is a mismatch between the arrangement's implicit SLA and CREED's operating model.

### Old L138 — crc32 `27626734` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

> 4. **A heartbeat artifact doesn't close the actual gap.** Even a boot-time reconciliation check (courier-sent? how many days late?) only fires when CREED happens to be spawned — the exact variable that caused the miss. It would add a new TSV and boot step for a channel that already failed its only real test, with no source-quality payoff per (2).

### Old L139 — crc32 `1363f226` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

>

### Old L140 — crc32 `092cc9c7` → §Workbook "S5 sourcing (rule)"; §Route Matrix S5 row

> **Standing state now:** HOMER's disclosed-secondary pull (Connect CRE / Chandan, cited plainly, cross-corroborated) is the sole, standing MF-print method — no change owed on HOMER's side. **CREED may still pass along whatever it reads in its own monthly whole-Trepp pull, opportunistically, cited "CREED pull, <date>" when it happens** — but carries no cadence commitment and is not "the arrangement." Routed to HOMER + confirmed-encoded to PROME 2026-08-13.

### Old L149 — crc32 `1102d1a5` → Closeout step 2

2. Append `VX_HISTORY.tsv` rows for any new monthly print — **one row per vector per print.** A level is not a trend. 🆕 *(2026-09-29, CATO CW3)* Fill `Role` and `Basis`: `Date` = the OBSERVATION PERIOD (`YYYY-MM` / `YYYY-Qn` / `YYYY-MM-DD`), never the pull date. **Exactly one `CANONICAL` numeric row per vector and period.** A correction marks the old row `SUPERSEDED` rather than deleting it; placeholders are `PLACEHOLDER`, other providers `CONTEXT`. `creed_selfcheck` check ③ enforces this.

### Old L150 — crc32 `935a3347` → Closeout step 3

3. Log session findings to `KB.tsv` with an **Admiralty score** (A1–F6, never a percentage) and the **source-remove** marked (`PRIMARY-READ` / `PRIMARY-CITED` / `SECONDARY`) **in `Source`**. `Epistemic` is EMPIRICAL / ESTIMATE / ASSUMPTION / ANALYTICAL; `Status` is the claim's lifecycle token; a task disposition goes in Notes as `DISPOSITION:` *(SCHEMA.tsv; CATO CW4, 2026-09-29; check ③ enforces it)*.

### Old L151 — crc32 `e767051b` → Closeout step 4

4. Update `PREDICTIONS.tsv` `Status`/`Outcome` on any resolution **AND `workbook/PREDICTIONS_SCOREBOARD.md` in the same session — both writes, or neither counts.** A narrative grade in STATUS prose is **not** a substitute for the ledger row *(BROCK's `BRK-29` sat `Status=OPEN` for 5 days past its own resolve date on exactly this gap)*. **A prediction that cannot resolve (instrument unavailable, metric unpublished) is `STUCK` — a Status change, never a confidence cut.**

### Old L154 — crc32 `b3bc2710` → Closeout step 6b

6b. **Re-list `inbox/` and `inbox/WALTER/` immediately before the closeout commit.** Anything that arrived during the session is logged and dispositioned, or named in SCRATCH as carried. *(Added 2026-10-30, DAEDALUS profile-refresh item 4: HOMER's 10/28 packet landed 10 minutes before that closeout and no surface recorded it.)*

### Old L155 — crc32 `e9d9f0a8` → Closeout step 7

7. **Rewrite `SCRATCH.md`** — it is overwritten, not appended. If the session changed CREED's *structure* (a doc/folder created/retired/moved, a schema or protocol amendment, an ownership boundary shift), add an entry to `MAINTENANCE.md`. **`MAINTENANCE.md` is consult-on-structural-work, NOT a per-session ritual** — CREED is Tier-2 and process weight is what makes a spawn-on-need agent expensive to wake.

### Old L156 — crc32 `25c59fc7` → Closeout step 8

8. **Catch-ups go to `catchups/`, never into STATUS** *(layout since the 2026-09-26 hot/cold split; this step re-aligned 2026-09-30, Will-approved, CATO CK3)*. A session that needs a catch-up writes **`catchups/YYYY-MM-DD.md`** and marks it **CURRENT** in `catchups/INDEX.md` (the previous one → superseded). `STATUS.md` stays the HOT file (header, §Standing Obligations, thesis, rails, BOTTOM LINE) and must stay under the fleet read budget: check with `scripts/read_cap_check.py --agent CREED`, and at the rotate tier move settled content out **verbatim** (crc-stamped, with a do-not-cite-as-current banner) rather than delete it. **Never raise the budget.** Before any rotation, audit by **obligation**, not bytes (§Standing Obligations exists because a byte-clean split once deleted owed actions).

### Old L157 — crc32 `39e1b310` → MAINTENANCE.md §2026-09-30

   > *History:* the retired recipe (a line-count trigger at 320 that `git mv`'d the oldest STATUS catch-up section into `archive/STATUS_CATCHUPS_*.md`) is preserved verbatim in `MAINTENANCE.md` §2026-09-30 (crc32 `f2ad27ce`).

### Old L158 — crc32 `746bea3a` → Closeout step 8b

8b. **Run the self-check — `python3 AGENTS/CREED/scripts/creed_selfcheck.py`** *(added 2026-08-20; ~20ms, CREED-scoped, exit 0 clean / exit 1 findings).* Three narrow checks: **① fired-trigger cross-surface consistency** (a trigger in `CREED_T_FIRED_LOG.tsv` must show a fire marker on every surface that names it), **② asserted counts vs actual** (VX / KB / PREDICTIONS-open / workbook-file counts claimed in prose vs reality), and 🆕 **③ field semantics** *(added 2026-09-29, CATO CW4/CW5)*: KB Conf / Epistemic / Status against `SCHEMA.tsv`; VX Source, Cross_Links and date fields; **VX Status colour vs its own numeric bands** (disclosed exceptions 4.01 and 9.03 are printed as info, not findings); VX_HISTORY exactly one `CANONICAL` numeric row per vector and period. Falsified against the pre-fix files before adoption: it caught both CW2 colours, the 9.03 column shift and 48 vocabulary defects.

### Old L159 — crc32 `3e4b9609` → MAINTENANCE.md (2026-08-20 sweep)

   > **Why it exists:** a Will-directed sweep on 2026-08-20 found 14 stale-surface defects **that no existing tool could see.** `consumer_check.py` scans superseded **VALUES**; the two worst findings were a superseded **STATE** (`CREED-T-02` fired and `THRESHOLDS.tsv` — the registry that *declares* it — said nothing) and superseded **COUNTS**. Different objects, so a clean `consumer_check` meant nothing. **On its first run it also found a 15th defect the manual sweep had missed.**

### Old L160 — crc32 `e552d58e` → Closeout step 8b first note

   > ⚠️ **Deliberately NOT a general claim-detector** — `claim_check.py`'s scoping lesson (13 decision files → 1 flag; whole tree → 131 flags) is why both checks are scoped to named CREED files and enumerable (check ① is line-scoped since 2026-10-30: a marker must sit on a line that names the trigger). **Safe to gate a closeout on: every surface it reads is CREED-owned**, so unlike a bare `--strict` it can never block you on another agent's work.

### Old L161 — crc32 `a4147d6b` → Closeout step 8b second note

   > ⚠️ **Scope limit, stated rather than implied:** check ② matches **known prose phrasings only.** Invent a new way to write a count and it is not covered — **add the pattern to `ASSERTIONS` in the same edit that introduces the phrasing.**

### Old L162 — crc32 `de6d35de` → Closeout step 8c

8c. **Record one CHECKS line in the session's catch-up:** `creed_selfcheck` rc · `threshold_scan` rc · `read_cap_check` result · `claim_check` · `orphan_check`, and name any step SKIPPED. *(Added 2026-10-30, DAEDALUS item 10: no check result was recorded for the 10/21, 10/22 or 10/28 closeouts.)*

### Old L169 — crc32 `88873955` → §Source Archive first paragraph

Legacy CREED lived as a REGINALD sub-agent. **Since 2026-08-13 the material lives under `AGENTS/REGINALD/archive/sub-agents/CREED/`** (moved by REGINALD, commit `a7bae0d06`, Will-directed; these paths read `sub-agents/CREED/` until 2026-10-22, dead for ten weeks):

### Old L179 — crc32 `a4279657` → — (no rule; file gone)

Top-level stale inbox (⚠️ **removed 6/28**, commit 5a7ac1aa — fully triaged into `research/INBOX_TRIAGE_2026-06-21.md` and its signals promoted into THESIS; the file no longer exists, kept here for source-trail only):

### Old L180 — crc32 `8f661fe8` → — (no rule; file gone)

- ~~`AGENTS/CREED/inbox/2026-02-24_signals.md`~~ (deleted)

### Old L182 — crc32 `30b5241a` → §Source Archive list, last bullet

Legacy sub-agent stale inbox:

### Old L183 — crc32 `f8dc6ba2` → §Source Archive list, last bullet

- `AGENTS/REGINALD/archive/sub-agents/CREED/inbox/2026-02-27_office_reit_selloff.md`

### Old L198 — crc32 `64805cd0` → §Current Stale-State Warning

Use the current rails (STATUS header + the CURRENT catch-up) for thesis state; the June 2026 source packs are trail, not state. Fresh data is still required before quoting any live market level, monthly CMBS print, FDIC update, or trade-relevant number beyond the dated source pack.

### Old L204 — crc32 `8d0178c6` → §Current Rails first paragraph (pointer to step 6)

Thesis rails. These are mandatory before CREED makes current analytical claims (current state itself lives in STATUS + the CURRENT catch-up + the workbook):

### Old L206 — crc32 `a60b3946` → Boot steps 6.3–6.5

- `AGENTS/CREED/thesis/THESIS.md`

### Old L207 — crc32 `6c205231` → Boot steps 6.3–6.5

- `AGENTS/CREED/thesis/CHANGELOG.md`

### Old L208 — crc32 `d77bb192` → Boot steps 6.3–6.5

- `AGENTS/CREED/research/INBOX_TRIAGE_2026-06-21.md`

### Old L209 — crc32 `c00b58b5` → Boot step 6.6; §Current Rails S8a bullet

- `AGENTS/CREED/research/REIT_EQUITY_TAPE_MODULE_2026-06-21.md` (**method and history module; its 2026-08-20 snapshot is PRE-FIRE and not current.** Current S8a lives in `VX-CREED-7.01`: **`CREED-T-08a` FIRED 2026-09-24** (TR −10.12; −13.06 on 9/25); **S8a = 4, Will-ruled 9/28.** *(Read `VX-CREED-7.01` for the current figure, not this line.)* *(This line taught the 8/20 "+0.07pp TR" level as live until 2026-09-29, PROME C5.)*) ⚠️ *Recompute with `.venv/bin/python3 AGENTS/CREED/scripts/s8a_relative.py` before citing S8a — never quote the point alone, and never call a sub-2-sigma move a trend.* ⚠️ *This pointer read "7/2" until 2026-08-20 while the file's own header read 7/27 — it had lagged three weeks. **Read the file's header, not this line, and fix this line when they diverge.***

### Old L210 — crc32 `147f12c8` → Boot step 6.7

- `AGENTS/CREED/archive/LEGACY_PULL_FORWARD_2026-06-21.md`

### Old L212 — crc32 `44e4ada2` → Boot step 6.2

**Historical source packs, ON DEMAND (not mandatory reads; changed 2026-09-30, Will-approved):** `research/REFRESH_2026-07-27.md` (prior pack: CRE lender leg, June SS, life-science bifurcation; predates the T-02 fire and the August prints) · `REFRESH_2026-07-04.md` (June-Trepp / recognition-cluster trail) · `REFRESH_2026-06-21.md` (FDIC-Q1 / maturity-wall trail).

### Old L214 — crc32 `06a664c6` → §Current Rails second bullet

Every trade-relevant number still needs a source/date. Refresh monthly CMBS, FDIC, or REIT/broker tape before treating levels as current.

### Old L220 — crc32 `e456b4bf` → thesis/THESIS.md §Current State Classification; §Working Hypothesis pointer

Legacy hypothesis:

### Old L222 — crc32 `da3bb8c1` → thesis/THESIS.md §Current State Classification; §Working Hypothesis pointer

> CRE stress is real, but bank recognition timing depends on mods, forbearance, refi capacity, employment, and bank concentration.

### Old L224 — crc32 `cff561c4` → thesis/THESIS.md §Current State Classification; §Working Hypothesis pointer

Current thesis state:

### Old L225 — crc32 `20bc92ba` → thesis/THESIS.md §Current State Classification; §Working Hypothesis pointer

1. **extensions absorbing maturities, pretend contested** — Maturities are being absorbed partly by extensions. At large banks the evidence is contested: on average extension terms tightened (Glancy, FEDS 2026-025), but weakly capitalized banks extended distressed loans to preserve capital (Crosignani & Prazad, NY Fed SR 1130, rev. June 2026). Smaller banks are untested. In CMBS the drag is slow resolution. *(reworded WQ-356, Will 2026-10-01 13:23 ET: "approved"; was "extend-and-pretend still absorbing — still active in banks and large-loan cures"; evidence `KB-CREED-053`)*,

### Old L226 — crc32 `17561015` → thesis/THESIS.md §Current State Classification; §Working Hypothesis pointer

2. **selective CRE recognition accelerating** — current base case,

### Old L227 — crc32 `e01b4c46` → thesis/THESIS.md §Current State Classification; §Working Hypothesis pointer

3. **broad CRE-to-bank transmission beginning** — not confirmed.

### Old L233 — crc32 `329fdfa9` → §Guardrails first bullet

- **Full legacy migration stays DEFERRED** *(forked up from the now-frozen `REVIVAL_PLAN.md`, 2026-07-27)*: the source archive now sits at `AGENTS/REGINALD/archive/sub-agents/CREED/` (REGINALD moved it 2026-08-13, `a7bae0d06`, Will-directed; CREED's references were not updated until 2026-10-22). It stays there as **source archive**: do not move or delete it further without Will, and update CREED's references in the same commit as any move.
