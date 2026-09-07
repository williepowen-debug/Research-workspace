# LABOR — LESSONS

LABOR-specific mistake-patterns to avoid. Read at boot (B3); written at closeout (C5).
**Scope:** durable LABOR-domain learnings — including LABOR-specific applications of general patterns that live in auto-memory (each such row cites the auto-memory slug it partners with). One lesson per entry. Newest at top.

---

> 🔒 **HOT / COLD SPLIT 2026-08-28** (DAEDALUS P1 read-cap, Will-ruled). This file was **81,816 B = 251% of the 32,550 B budget** and is a **boot-mandated B3 read**, so it was **returning a partial file with no error**. **ROTATION 3 — 2026-09-07:** L-30 added (the as-made audit) + its PM addendum (the self-authored-suite finding); **L-21, L-22 and L-23** demoted to the index with their rules retained verbatim, worked cases → `archive/LESSONS_ARCHIVE_2026-09-07_L21_worked_case.md`. **ROTATION 2 — 2026-09-04:** L-27 and L-28 were added the same day and pushed this file to **35,155 B, over the 32,550 B budget**; per the standing convention the three oldest full sections (**L-18, L-19, L-20**) were demoted to the index, **rules retained verbatim**, worked cases moved to `archive/LESSONS_ARCHIVE_2026-09-04_L18-L20_worked_cases.md`. **The 8 most recent lessons stay in FULL below. Every older lesson KEEPS ITS RULE, one line, in the index — only its worked case moved.** Full pre-split file, byte-for-byte, CRC32 `671ad173` re-hashed and verified: `archive/LESSONS_ARCHIVE_2026-08-28_pre-split.md`.

## COLD INDEX — rules retained; worked cases in the archive

- **L-23** — Evidence about an UPSTREAM quantity must move a DOWNSTREAM-graded instrument LESS, not more, when the mapping adds a step the evidence never touches; and a counterfactual conditioned on an OUTCOME may not be cashed on a DIRECTION *(worked case → `archive/LESSONS_ARCHIVE_2026-09-07_L21_worked_case.md`)*
- **L-22** — A figure you hand a peer in a PACKET is a publication with one consumer and no ledger row, and nothing in the closeout sweep watches it: `consumer_check` scans YOUR files, so a number that rots in someone else's tree is invisible — add the row to `PUBLISHED.tsv` with the recipient in `consumers` *(worked case → `archive/LESSONS_ARCHIVE_2026-09-07_L21_worked_case.md`)*
- **L-21** — The pathspec rule survives every commit that HAS files and dies on the one that doesn't: `--allow-empty` with no pathspec is functionally `git commit -a` on a shared index — the pathspec is the guard, not the target *(worked case → `archive/LESSONS_ARCHIVE_2026-09-07_L21_worked_case.md`)*
- **L-18** — A frozen card's branch set must PARTITION on ONE surface, or your post-hoc judgment picks the winner *(generalised to two axes by L-27)*
- **L-20** — A "what did I miss?" sweep is the query shape most vulnerable to date-inference failure
- **L-19** — A CONSERVATIVE restatement gets no exemption from the check you would apply to the claim itself
- **L-16** — A finished judgement filed under a NON-TERMINAL disposition token re-enters the queue forever: the six parks were one wrong word, not six failures to assess
- **L-15** — Base-rate a threshold BEFORE building it: a LEVEL bar is usually a descriptor, and "don't build it" is a legitimate answer
- **L-14** — A GROSS FLOW cannot falsify a claim about a NET count; and check whether the decoupling is rare *in general* or rare *except right now*
- **L-17** — A frozen card cannot help if nobody boots; and the branch that "cannot happen" is the one you forgot to enumerate
- **L-13** — An N-of-M implication test must be BALANCED between intentions and realized counts, or it fires on the intentions half alone
- **L-12** — A cross-check with a FREE PARAMETER validates nothing; and `[CONF]` must name a primary, not a consensus of secondaries
- **L-11** — Propagating a correction is a per-surface READ, not a pattern-match: sweeps fail in BOTH directions, and the over-correction deletes true statements
- **L-10** — A "holds through DATE" prediction is N draws, not one call — decompose to per-draw survival; and a risk LABEL is not a REPRICE
- **L-09** — An ABSENCE-tell is only evidence if the instrument had room to speak; and diff like-for-like (statement↔statement, minutes↔minutes)
- **L-08** — A WARN cohort must be ≥~10% of the weekly claims base to be visible in the national SA series; below that, the threshold is untestable and the *specification* is the defect
- **L-07** — Book the announcement TYPE (voluntary offer vs involuntary RIF); verify WARN filings exist before attributing a WARN surge to a company
- **L-06** — Ratio-gauge thresholds (U-3) can be silently defeated by the DENOMINATOR; playbook grids need a supply-artifact branch
- **L-05** — Cross-domain signals can be scored on the WRONG SIDE of the convergence matrix
- **L-04** — Structured ledgers (VX/KB/FLOW) drift months behind the narrative STATUS
- **L-03** — DOGE/government YoY comps are base-effect-poisoned
- **L-02** — Track the *revised* NFP series, not just the first print
- **L-01** — Company-tier revenue ≠ industry employment

---

## L-30 — "Verified in git" names an ARTIFACT, and the artifact I verified against did not exist when the value I was verifying was set

**Bought 2026-09-07, on my own calibration record, while sourcing a routine backfill.**

`PREDICTIONS_SCOREBOARD.md` §A scores every prediction at its **as-made** confidence, says so in bold, explains *why* in three sentences, and states that the as-made was **"verified in git … not read off the current ledger value."** All of that was true. **Four of twelve rows were still scored at a walked-down number**, and the book's headline Brier was **0.299 when it should have been 0.342**.

| | |
|---|---|
| **What I verified against** | `workbook/PREDICTIONS.tsv` |
| **When that file was created** | **2026-03-04**, by a fleet-wide bulk seeding for 24 agents |
| **What the seeding stamped** | `Date_Made = 2026-02-18` on **seven** LABOR rows at once |
| **When six of those rows were actually live** | **2026-02-02**, in `STATUS.md`, at their true as-made values |
| **What a walk-down between 2/02 and 3/04 does** | it is captured by the seeding **as if it were the registration value** |

**So the verification could not have failed.** The ledger is downstream of the registration surface, and every later commit of it agrees with the first — which is what "verified across commits `b50c6ada`/`0838327f`" actually measured: **agreement among vintages that all postdate the event.** Corrections: **LAB-02 65→70 · LAB-05 55→70 · LAB-07 65→60 · LAB-13 30→55.**

⇒ **The rule: "verified" is a two-part claim — the METHOD and the ARTIFACT — and only the method gets stated.** Before writing *verified*, name the artifact and ask **"did this artifact exist, in this form, at the moment the value I am checking was set?"** If it was created later, agreement inside it is not evidence about the event.

⚠️ **The three second-order costs, because the number was never the worst of it.** (1) It changed **sentences about my own conduct**: LAB-05 at a walked-down 55% read as *"mild overconfidence on a coin-flip call"*; at its as-made 70% it is a high-conviction single-firm miss. (2) It **manufactured a finding**: "LAB-17 and LAB-13 are two consecutive correctly-hedged threshold calls" was the one genuinely new positive result in two months, and **LAB-13 was never a hedge**. (3) It **understated the book's central regularity** — 0-for-4 at ≥60%, not 0-for-5 — *in the very sentence used to justify a reprice*, which is L-25 one level down.

🔒 **Mechanical fix, installed the same day** (a rule alone is what already failed): as-made comes from the **earliest `STATUS.md` blob** carrying the row's confidence cell — never the TSV for any row with `Date_Made` ≤ 2026-03-04, never a later commit of the TSV for any row. Written into `PREDICTIONS_SCOREBOARD.md` §A and §D.

**Cross-refs:** L-29 (same shape, one day earlier — the figure is right and the sentence naming what it is a figure OF is wrong; **this is instance 6**) · L-25 (the corrective inherits its anchor) · `[[finding_instrument_reports_clean_against_the_wrong_reference]]` **n=25** · `[[finding_adoption_is_not_validation]]` · `[[finding_crosscheck_with_free_parameter_validates_nothing]]` — *a check whose reference postdates the event has a free parameter and cannot fail.*

---

**⚠️ ADDENDUM 2026-09-07 PM — the same defect, one layer up, found in the FIX for it, by the reviewer and not by me.**

Hours after writing L-30 I shipped `card_partition_check.py` with **10 self-tests, all passing**, and wrote *"falsified before adoption"* in the docstring, the build register, the commit message and STATUS. **CODEX wrote 5 independent cases and all 5 returned a false PASS.** One of them was a card with a **single band**, where coverage never ran at all and the tool printed ✅.

⇒ **A self-authored test suite is not falsification — it is the design restated as assertions.** Every one of my ten tests encoded a case I had already thought of, so the suite could only confirm the shape of my own attention. `[[finding_self_attack_defends_the_argument_not_the_apparatus]]`.

🔑 **The generalisation that makes this L-30 and not a separate lesson:** *"falsified"* is the same two-part claim as *"verified"* — a **METHOD** and an **ADVERSARY** — and **only the method gets written down.** "10 self-tests pass" names a method. It does not name who tried to break it, and I was the only one who had.

⇒ **Forward rule — and CODEX's correction to my first draft of it is the better version.** My draft said *a guard is unfalsified until someone who did not build it has tried to break it*. **That makes every maintenance tool wait on another agent, which is a bottleneck, not a control.** The rule that survives: **never write "falsified" as a certification; ship CONCRETE, REPRODUCIBLE completion evidence that states precisely what was tested AND what was not.** *"19 self-tests pass; scope is single-axis interval tables; multi-table and ambiguous-axis cards report UNVERIFIED"* is checkable and invites the review. *"Falsified before adoption"* is a claim about my own thoroughness and invites nothing. ⚠️ **v2 then repeated the error at a higher level:** I fixed all five of CODEX's cases, ran 15 tests, and called it falsified again — **and four NEW cases broke it, all SCOPE failures rather than parser bugs**, because the tool emitted a card-level PASS that a single good table could earn. **The pattern is not that my parser is weak; it is that I keep certifying the whole object when I have only checked a part of it.** v3 reports per-table dispositions and no longer certifies a card at all. **The same session also had me claim ACTION 3 was discharged while the footer pin it was supposed to fix still read the stale value, with my own sentence beside it saying it had been repointed.** Both were caught by the same outside read. **Two completion claims, same day, both passing my review and neither true.**

---

## L-29 — Every defect found in me on 2026-09-07 was in the sentence NAMING what a figure was a figure OF, never in the figure

**n=5 in one session, across two domains (analysis and tooling), all caught by reviewers, none by me.**

| # | The figure | The sentence around it |
|---|---|---|
| 1 | July 2026 `−23K → +21K = +44K`, rank 44/44 — **correct** | Offered as calibration for **RED-23, which resolves on first→THIRD**. On that cut July **has no value at all** (2 vintages) and +74K/+67K/+49K beat it. I named the right cut one paragraph earlier. |
| 2 | `diff −3.4K, SE 18.7K, t = −0.18` — **correct** | Reported as *"the split does not exist in this data."* The 95% CI is **[−40K, +33K]**. **Not detected ≠ absent.** |
| 3 | Feb-2026 current vintage `−156K` — **correct** | Called HAWK's `−92K` *"stale by 64K"* — equating a **first-print** statement with a **current-vintage** level, one message after reading RED's explicit written fence against exactly that. |
| 4 | `58.9 − 59.2 <= −0.3` passes — **correct** | Reported as *"the boundary is falsified."* It was **one fixture on the lucky side of a float comparison**; `59.1 − 59.4` fails, and **12 of 20** boundary levels missed T-03. |
| 5 | `range(85,105)`, 20 levels, all pass — **correct** | Comment said *"EPOP 58.5 .. 60.4."* It tested **8.5–10.4**. I then published a failure count off it and printed `missed at EPOP = [8.8, 9.3, …]` — impossible values for this series — without reading them. |

**The rule I am taking from it:** a verified number does not verify the claim it is embedded in. **Before publishing a figure, state the object separately from the value** — *which series, which vintage, which horizon, which domain, which sample* — and check the object against the question actually asked. My verification discipline runs on values and stops at the sentence boundary; every reviewer this session entered through that gap.

⚠️ **Why it will recur without a mechanism.** All five passed my own checks *because my checks test values*. Four came from outside review and one from a peer's fence I had already read and quoted. **Self-review at the value layer cannot catch a wrong-object claim** — the value is right. → the pre-write question is now **"what is this a number OF, and is that what was asked?"**, not "is this number right?"

🔗 Extends **L-25** (a corrective inherits the anchor it corrects) and the 2026-08-28 `~7×` rule in `CLAUDE.md` § OUTPUT RULES — *"the figures were fine; the prose about them was not."* **That was n=1 and a rule. This is n=5 in a day and a measured pattern.** Related: `[[finding_instrument_reports_clean_against_the_wrong_reference]]` · `[[finding_level_and_rate_look_like_agreement_until_you_name_which]]` · `[[finding_float_precision_empties_the_tie_set_and_voids_the_operator]]`.

---

## L-28 — A claim can do every job a prediction does without ever being one; then no gate runs on it and no scoreboard ever sees it

**Bought 2026-09-04, and not by any check I own — by Will asking "why did we believe the headline call originally?"**

For two sessions my sharpest published line was: **"T-03 fires on a FLAT EPOP print of 58.9."** It travelled **seven live surfaces** — `STATUS.md`, `NEXUS_BRIEF.md`, the frozen card, `docket/CATALYSTS.tsv`, `KB-LAB-171`, `PROME/DOCKET.tsv` L259, `PROME/WILL_QUEUE.md` row 159 — and reached **Will**, who ruled on it as **WQ-159**. EPOP printed **59.1** and it did not fire.

**It was never a registered prediction.** No `LAB-xx` row. No confidence value on any of the seven surfaces. Verified by grep, not memory.

### The three things that follow, and they are all structural

1. **No §C gate ever ran on it.** Every gate fires at *registration* (boot B4, *"before writing any NEW prediction"*). An unregistered claim is invisible to all fifteen. Gate **#3** — threshold-vs-mechanism — is the one that mattered: this was a **threshold** call, and my record is **0-for-5 at ≥60% on thresholds against 3-for-3 on mechanisms** *(🔧 2026-09-07: was 0-for-4 here; the as-made audit moved LAB-05 into the ≥60% bucket)*. The single gate built for exactly this failure mode never saw it.
2. **It cannot reach the calibration record.** `PREDICTIONS_SCOREBOARD.md` §A scores rows. The miss is real, public, and **invisible to my Brier** — so the book cannot learn from its most-published claim of the month.
3. **The escalation asked the wrong question.** WQ-159 put *"should T-03 be retuned?"* to Will — a question about the threshold's **letter**. Nobody, me included, was ever asked **"how likely is it to fire?"** A claim can pass all the way to the operator and back without anyone attaching a number to it.

### Why it felt like it did not need one

The published phrasing was **"it fires on no deterioration at all."** That is a true statement about the threshold's *sensitivity* — and it silently swaps the question. The real question is *"will EPOP print ≤58.9?"*; the phrasing converts it to *"will EPOP deteriorate?"*, which sounds like it only needs the status quo. **It actually needs EPOP not to RISE, and I never wrote that sentence anywhere.** A sensitivity claim reads as a forecast while feeling like arithmetic, which is exactly why no one — including me — thought to price it.

### ⚠️ The base rate partly EXONERATES the call, and that must be said

Computed after the fact, from FRED `EMRATIO`: a monthly rise of **≥+0.2** occurred in **1 of the 23 months before the call = 4.3%**; 2/42 since 2023 = 4.8%; 1/30 since 2024 = 3.3%. **The branch that broke it was roughly a 1-in-23 event in the prevailing regime.** The call was **not reckless** — it was well-supported and an uncommon branch landed. *(Recording this because `[[finding_a_charitable_reading_of_your_work_is_the_one_to_check]]` has a missing mirror: an UNFLATTERING self-claim is the least-audited sentence in the room, and "I was overconfident" would have been the comfortable, wrong conclusion here.)*

**But the long-run rate is 19.3% (182/941), and `19.3 / 4.3 = 4.5×`.** That factor **is the regime assumption.** The 4% only holds while the labor force keeps contracting — and my own CORE TENSION said that contraction was an *immigration-signature supply shock*. **A shock is precisely the thing that reverses.** I used the regime to earn confidence and never asked what would end it. August was the reversal and nothing else: labor force **+683K** after −720K and −264K.

⇒ **Whenever a base rate is regime-conditional, name the regime and state what would end it — in the same sentence as the number.** A conditional rate quoted without its condition is a forecast wearing a statistic's clothes.

### The rule

> **If a claim would change what another desk does, it needs a registered row with a confidence — whatever surface it lives on.** The test is not *"is this a forecast?"* but **"if this is wrong, does anything in my system find out?"** Arithmetic about a threshold's *sensitivity* is not exempt: the moment it is published as a reason to expect an outcome, it is a forecast and must be registered, gated and scored.

**Executed the same session:** **LAB-18** registered (T-03 fires on any 2026 print, **15%**, threshold call capped per gate #3, with the gate #12 per-draw and gate #15 resolution arithmetic on the row) and **LAB-19** (the mechanism counterpart, **60%** — the labor-force reversal persists — which tests my own CORE TENSION in the direction that would refute it).

🔴 **And the sweep this lesson forced immediately found a second instance in my own open book:** **LAB-12** needs U-3 **4.1% → ≥5.0%**, a 0.9pp rise in ~4 prints. Base rate `11/302 = 3.64%` ex-covid since 2000. It was sitting at **30%** — `30 / 3.64 = 8.2×` — and I had *held* it there that same morning while writing *"mechanism cuts both ways"* on the row, which is **gate #13's unpriced-update pattern committed while quoting gate #13.** Repriced to **8%** (as-made 60% still governs scoring). Same shape as **L-25**: a number stays far above its base rate because nobody re-runs the arithmetic after registration — and **both times the trigger was someone else asking, not a check of mine firing.**

**Cross-refs:** L-25 (the corrective inherits the anchor it corrects — same failure, one level up) · L-27 (today's other two findings from the same grade) · L-10 (multi-draw) · `[[finding_registered_gate_captures_attention]]` — **the un-gated instrument is the exposure, and this is its sharpest form: not a stale registered row, but a load-bearing claim that was never registered at all.**

---

## L-27 — A two-axis band table must PARTITION on BOTH axes, and the cell it omits is the one your thesis says cannot happen

**Bought 2026-09-04 on the NFP August grade — the most multi-loaded print in the book, on a card frozen ~36h early.**

My card's §3b graded U-3 **jointly with LFPR** (correct — that is L-06, and grading U-3 alone is exactly the failure L-06 exists to stop). The table enumerated:

| U-3 | LFPR | assignment |
|---|---|---|
| ≥4.3 | flat or up | 🔴 genuine slack |
| ≥4.3 | down | ⚠️ NO-SIGNAL on slack, T-06 still fires |
| 4.2 | any | no band |
| **≤4.1** | **down** | ⚠️ NO-SIGNAL, denominator effect |
| ≥5.0 | any | LAB-12 resolves |

**August printed U-3 4.1% with LFPR UP (61.4 → 61.6) and the labor force +683K. That cell does not exist on the card.**

**Why it was omitted, which is the whole lesson:** the `≤4.1 / down` row is written the way it is because my CORE TENSION says a falling U-3 in this regime is a *supply* artifact — U-3 down, LFPR down, labor force shrinking. **The thesis supplied the only branch I bothered to write.** The cell I left out is precisely the one that refutes the tension — and it is the one that printed.

⇒ **The rule: enumerate the band table by CROSS-PRODUCT of its axes, not by walking the branches your thesis expects.** If an axis has 3 states and the other has 2, there are 6 cells; write all 6 or state explicitly which are unreachable and why. **"No band" is a legitimate assignment — an ABSENT cell is not**, because on the day it forces you to either improvise a band (which is what cards exist to prevent) or take no score at all.

**What I did on the day:** took **zero** score movement and logged the defect. That is the conservative default and it was right, but it is a *degraded* outcome — the card was supposed to tell me what the print MEANT and on this axis it told me nothing.

⚠️ **Companion finding from the same grade, and it may be the more transferable of the two: A FROZEN THRESHOLD COMPUTED OFF A REVISABLE SERIES IS NOT ACTUALLY FROZEN.** My card pre-computed freeze-thaw LEG A as **"August ≥ +303K"** from `(20 − 23 + X)/3 ≥ 100`. But June and July were **revised in the same release that carried August** — to +31K and +21K — so the real bar was `(31 + 21 + X)/3 ≥ 100` ⇒ **+248K**. **The frozen number was wrong by 55K before the print was even read**, and only survived as a *correct grade* because the card explicitly ordered the recompute (*"recompute with the revised numbers FIRST, per L-02, before reading August"*).

⇒ **Any pre-registered threshold denominated in a REVISABLE series must ship with its recompute instruction, not just its value.** Write the **formula** as the frozen object and the number as an illustration of it — never the reverse. A card that had frozen only "+303K" would have graded the wrong bar with complete confidence and left no trace of the error.

**Cross-refs:** L-18 (a card's branch set must partition on ONE surface — this is its two-axis generalisation) · L-17 (the branch that "cannot happen" is the one you forgot to enumerate — L-27 names *why* it gets forgotten: the thesis writes the branch list) · L-02 (track the revised series) · L-06 (grade U-3 jointly with LFPR).

**Wired forward:** the `docket/CATALYSTS.tsv` row for **NFP September, 2026-10-02**, carries both requirements — enumerate both LFPR directions at every U-3 level, and RECOMPUTE LEG A on the revised vintage rather than carrying the 9/4 arithmetic forward. Card owed ~2026-09-25.

---

## L-26 — A modeled catalyst date that slips EARLIER is invisible to every check I own, because every check assumes dates slip LATER

**The instance (2026-09-01).** `CATALYSTS.tsv` carried JOLTS July as **`~2026-09-02`** — modeled, not source-confirmed. **It printed 2026-09-01 at 10:00 ET.** My boot ran that evening and `catalyst_countdown.py` showed it as **upcoming, 1 day out**, in the IMMINENT block. The countdown was working correctly and was reporting a released figure as a future event.

**Why every guard missed it.** B5's rule reads *"modeled dates within ~1wk should be re-verified against the source schedule **before relying on them**"* — which is a rule about **not acting too early on a date that may move out**. **There is no symmetric check for a date that moved IN**, and there cannot be a countdown-based one: a countdown that says "1 day out" is, by construction, not going to tell you the thing already happened. **B2a does not cover it either** — the spine gate reads *claims* series only, so a landed JOLTS print is outside its perimeter, and it returned a clean ✅ PASS on the same boot. **B5b does not cover it** — there was no frozen card for JOLTS, and B5b enumerates cards, not events.

🔴 **What actually caught it was WALTER routing a signal.** Not one of my own instruments. That is luck of routing, not a control — and the same print landing in a week when WALTER is quiet would have sat until my next boot, or indefinitely if no session ran (the summons gap, `BUILD_DEBT.md` BD-23).

**The asymmetry stated plainly:** a date that slips **later** costs me a wasted look. A date that slips **earlier** costs me *the grade*, because a catalyst I have pre-committed bands for gets read after I have already seen the number elsewhere — which is precisely the condition a frozen card exists to prevent.

**Fix (cheap, and it is a boot step, not a new tool):** for every `~`-prefixed row inside the IMMINENT block, **check the series for a landed observation before trusting the countdown** — for anything on FRED that is one `fetch.py` call, and `boot.py` already pulls JOLTS. **The data to detect this was in my own boot output on the same run:** `labor_data.py` printed `JOLTS openings … 2026-07-01` — a **July** reference month, which can only exist if the July release has happened. **I read that line as a stale spine and it was a landed print.** Partner: `[[finding_dated_carry_item_has_no_expiry_check]]`.

**First seen:** JOLTS July, 2026-09-01. Cost: none this time — the grade was still done same-day, off the pre-committed bands, because the routing happened to be there.

---

## L-25 — A corrective is anchored to the number it is correcting, and no gate in this book ever re-grades the correction

**The instance (2026-08-28, LAB-08).** On 2026-08-07 I repriced LAB-08 **65% → 35%**, 21 days before its gate, under §C gate #14. The reprice was *good* work by every process test it was built to pass: declared pre-print with a commit receipt, unforced (no new data — pure arithmetic nobody had run), symmetric, and it **explicitly cited LABOR's 0-for-4 record at ≥60% on threshold calls as its reason (c)** *(quoted as cited; the record on corrected as-made values was already 0-for-5 — see the scoreboard §A audit 2026-09-07)*. Then the print landed at **−79,000**, card §4 **Band E**, whose pre-committed assignment is **4%**.

🔴 **35% was still ~8.75× the honest number *(corrected 8/28: 35/4 = 8.75, not the asserted ~7)*. The corrective that was made *specifically because my threshold calls run too hot* was itself too hot, by the same failure mode, in the same direction.**

**Why it happens.** A reprice is framed as a *move from* the standing number, so the standing number sets the scale of the move. "65 is too high, cut it hard" produces 35 — a 30-point cut *feels* large precisely because it is measured against 65. **Nothing in the procedure ever asks the independent question: *what number would I write if I had never published 65?*** The card's own §3 decomposition answered that (bands × conditionals ≈ 0.33) — but the band probabilities feeding it were themselves set beside a 65% prior, so the "independent" derivation inherited the anchor and returned a number confirming it. **A decomposition anchored at its inputs looks like arithmetic and functions as a rationalisation.**

**The measurement, so this is not a story:** card §3 put **P = 0.275** on the band that actually occurred — 72.5% of my mass on bands that did not happen — while the card simultaneously claimed to be correcting for over-confident threshold calls. ⚠️ **VINTAGE QUALIFIER, added 2026-08-28 ~11:3x after recovering content I had destroyed unread: 0.275 is the FROZEN 8/07 card's §3 figure and is the correct one for SCORING. My LIVE pre-print view was better — on 8/27 I re-weighted to `P(<450K-or-up) = 0.65` on Berger + RED's primary verification. Both are real; they answer different questions. Saying "0.275 on the band that occurred" WITHOUT this qualifier understates my going-in calibration by ~2.4×.** ⛔ **This does NOT weaken the finding: the finding is about the 65% → 35% REPRICE being anchored, and 35% was ~8.75× the honest 4% regardless of what the band table said *(corrected 8/28: the ~7 was asserted, 35/4 = 8.75)*.** 

**Fix (and it is one line at C2, not a new gate):** when repricing a prediction, **write the number twice — once as a move from the standing value, once cold from base rates with the standing value not visible — and if they disagree by more than ~2×, take the cold one and record both.** Then, at resolution, **score the CORRECTIVE as its own row, not just the as-made value.** LABOR's scoreboard grades as-made 65% and is blind to the fact that the 35% was also wrong; a book that never grades its own repricing steps cannot learn that its repricing is mis-calibrated. ⚠️ **This partners with C2-0 but is not the same thing:** C2-0 sweeps *stale* high-confidence rows. **This one fires on the freshly-repriced row — the one that just received attention and therefore looks safest.** Partner auto-memory: `[[finding_corrective_inherits_the_anchor_it_corrects]]`.

**First seen:** LAB-08, 2026-08-28 (QCEW preliminary benchmark = −79,000; card §4 Band E → 4%; the 8/07 reprice to 35% was **~8.75×** high). *(🔧 8/28: “~7×” was asserted, never computed — 35/4 = 8.75×.)*

---

## L-24 — A reachability probe grades the moment it ran; it is not a property of the wall — and the wall is a HOST, not the object

> 🔧 **L-24 COMPRESSED 2026-08-28 — it had grown to 16,008 B (20% of the file) because I corrected it THREE TIMES in one session.** **The settled rule is above. The full sequence — four mechanism claims, three peer challenges, ~46 probes, and the two self-audit corrections that followed — is in `archive/LESSONS_ARCHIVE_2026-08-28_pre-split.md`.** **Settled mechanism:** `bls.gov` runs a **UA DENYLIST nothing rescues** (`curl`/`Wget`/`python-requests`/empty) **plus a browser-impersonation completeness check**; three passing paths — honest non-browser UA alone · browser UA + full header set · browser UA + a genuine contact token. **Working recipe:** `curl -sS -A "research-bot/1.0 (contact <email>)" <url>`. **The durable half is not about BLS: a reachability probe grades the moment it ran, and a recipe published in TIDIED form is not reproducible until the PUBLISHED form is run.**

