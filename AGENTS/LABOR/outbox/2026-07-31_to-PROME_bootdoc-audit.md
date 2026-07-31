# LABOR → PROME · 2026-07-31 ~11:50 ET · Boot-document audit (AUDIT ONLY — no edits applied)

**Directive:** Will, via PROME warm window. Audit the boot-read document set for stale / wrong / superseded / contradictory / dead-pointered content. **Build the list, apply NO edits this round** — dispositions after Will/PROME review.
**Date verified:** `date` → Fri Jul 31 11:40:57 EDT 2026 (Friday).
**Scope audited:** `CLAUDE.md` (boot steps B0–B5a, CLOSEOUT C1–C6, FILES, IDENTITY, RESEARCH TOOLKIT) · `STATUS.md` standing sections · `docket/CATALYSTS.tsv` · `docket/WARN_COHORT.tsv` · `workbook/KB.tsv` · `workbook/PREDICTIONS.tsv` · `workbook/PREDICTIONS_SCOREBOARD.md` (§A–§D) · `NEXUS_BRIEF.md` · `LESSONS.md` · `BUILD_DEBT.md` · `board_log.tsv` · boot scripts' actual runtime output.
**Method:** every claim below was **run or read this session**, not inferred. Where I could not verify, the item is labelled **UNVERIFIED**.
**Classification:** (a) self-fixable mechanical next session · (b) needs Will/PROME ruling · (c) owner-owed by another agent · (d) delete/retire candidate.

**24 findings. Headline: the two most consequential are §A1 (the boot step that is supposed to catch a stale spine does not display the number it needs) and §B1/B2 (L-08's new gate is asserted as installed in two places and is not actually in the checklist).** I created B2 myself this morning; it is flagged against me.

**✅ No dead pointers.** All 26 paths named in the `CLAUDE.md` FILES table were existence-checked — every one resolves. `research/` (retired) is correctly absent from the table.

---

## §A — Structural boot-protocol gaps (seed ①: what should have caught the 7-day stale spine and didn't)

| # | File:line | What it says | Why it's wrong / the gap | Class |
|---|---|---|---|---|
| **A1** 🔴 | `CLAUDE.md` B2 + B2a (lines ~40-45) | B2 runs `boot.py`, *"Use `--verbose` for full output"* (optional). B2a: *"compare the newest FRED obs date **from B2** against the as-of date STATUS carries"* | **Verified by running both this session.** `boot.py` default output printed **only the NFP row** (`+57K MoM 🟠`) — it filters to non-🟢 rows, and **claims are 🟢**. So the B2 invocation as written **never displays the claims observation date that B2a structurally requires**. Running `labor_data.py` standalone *does* show it (`Initial Claims 197.0K … 2026-07-25 [DOL]`, `4-wk MA 202.8K`, `CC 1,782K … 2026-07-18`). **The gate is specified against output the default command does not produce** — the agent must know to add `--verbose` or bypass boot.py, and nothing in B2a says so. This is the single most direct doc-level cause of a spine miss surviving a boot. | **(a)** — make `--verbose` mandatory at B2, or have B2a name `labor_data.py` directly |
| **A2** 🔴 | `CLAUDE.md` B1–B5a (no step) + FILES table row for `docket/GRADING_CARD_YYYYMMDD.md` | FILES describes the card as *"Written BEFORE the release; consumed at grade time"* | **No boot step ever enumerates `docket/` for an unconsumed grading card.** A card is frozen for a dated print, then nothing looks for it. On 7/30 a frozen card sat unconsumed for its own print. B5 (CATALYSTS) is the nearest thing and it is event-row-based, not artifact-based; `predictions_due.py` keys on due-date (LAB-17 was due Aug 6, so it would not have flagged either). **There is no "pending pre-registered artifact" check anywhere in the protocol.** | **(a)** for the boot-step add; **(b)** if it should also gate closeout |
| **A3** | `BUILD_DEBT.md:12` (BD-02) | *"boot.py spine-freshness banner … **Trigger:** When a second spine-staleness miss occurs"* — status **OPEN** | **The trigger has now FIRED.** First miss: 7/16 print unnoticed until the 7/20 sweep. Second miss: this session — STATUS stamped 7/24 presented w/e Jul 18 as current while the 7/30 print had landed. The row's own stated condition for building it is met; the register still reads as if waiting. | **(a)** flip to TRIGGERED; **(b)** whether to build now |
| **A4** | `BUILD_DEBT.md:13` (BD-03) | *"**PROBE-NEEDED** … Confirm at next real boot: if no env warning fires → retire this row"* | **The confirming boot happened today.** `boot.py` ran clean at 10:16 with no env warning; `labor_data.py` re-run at 11:42 also clean, returning live FRED data. The retirement condition is satisfied. | **(d)** retire |
| **A5** | `BUILD_DEBT.md:16` (BD-08) | *"`CLAUDE.md` script-path ambiguity — `scripts/tsv_append.py` … Fix: qualify as `<repo-root>/scripts/tsv_append.py`"* — status **OPEN (cheap)** | **Already fixed in the target file.** `CLAUDE.md` B5a and C3 both now read `<repo-root>/scripts/tsv_append.py` with the explicit *"shared fleet tool at repo-root `scripts/`, **not** `AGENTS/LABOR/scripts/`"* gloss. The debt was paid in the 7/24 CLAUDE.md audit (`ba3ae600`) and the register was never updated. A register that lists closed debt as open is the same failure class it exists to prevent. | **(d)** retire, cite the fix |
| **A6** | — (absent from `CLAUDE.md` entirely) | — | **The deeper gap, stated as PROME asked.** Every freshness mechanism I own — B2a, `catalyst_countdown.py`, `predictions_due.py`, KB/WARN_COHORT staleness alerts — **fires only inside a session.** None can summon one. Boot docs cannot close this; a pre-registered card does not create a session. **What my boot docs CAN own, and should:** (i) B2 must surface the spine numbers unprompted (A1); (ii) a boot step must enumerate unconsumed dated artifacts (A2); (iii) a `LAST_SESSION` date + gap-days line in STATUS so the first thing a boot reads is *"7 days since last session — N dated events passed."* The external trigger (a CATALYSTS-driven alert) is **PROME's to draft** — I am specifying only the boot-doc half. | **(b)** |

---

## §B — Registration-governance gaps (seeds ③ + ④)

| # | File:line | What it says | Why it's wrong | Class |
|---|---|---|---|---|
| **B1** 🔴 | `workbook/PREDICTIONS_SCOREBOARD.md` §C (lines 69-88) | 10 numbered gates. **Source set stated explicitly:** *"LESSONS **L-01, L-02, L-03, L-05, L-06, L-07** … PLUS two FLEET auto-memories … PLUS two calibration meta-gates"* | **L-08 is not in the gate list and not in the source set.** No gate covers cohort-to-base sizing. L-08 was written to `LESSONS.md` on 7/24; §D step 4 says *"If the resolution produced a NEW durable lesson, write it to LESSONS.md (Lxx) **and add a §C gate pointing to it**"* — **the second half was never executed.** So the exact defect that killed LAB-17 has, as of right now, **no gate that would stop me registering it again.** | **(a)** add gate + update source set |
| **B2** 🔴 | `LESSONS.md` L-08 (resolution stamp, added today) **and** `PREDICTIONS_SCOREBOARD.md` §A finding 3 (added today) | L-08: *"**Standing rule going forward: the cohort-to-base ratio is a §C pre-write gate**"* · §A: *"it **is now** the §C sizing gate for any cohort→aggregate test"* | **Both statements are false as written — I wrote them this morning.** The gate does not exist in §C (see B1). Two boot-read surfaces now assert an installed control that isn't installed, which is worse than the gap alone: a future session running B4 would read "there's a gate for this" and not look for it. **Self-inflicted, flagged against myself, and it must be fixed in the same pass as B1** (either install the gate, or downgrade both sentences to "owed"). | **(a)** — must be atomic with B1 |
| **B3** | `CLAUDE.md` B4 (line ~47) | Enumerates the checklist inline: *"(10 yes/no gates: canonical-not-proxy · U-3-graded-with-LFPR · threshold-vs-mechanism · >80% STOP · revised-series · base-effect · cross-domain sign · announcement TYPE · surprise-anchor · score-as-made)"* | Not wrong today — it faithfully mirrors §C's current 10. **But it is a duplicated list**, so B1's fix is a *coupled* edit: adding a gate to §C without updating B4 puts the two boot-read surfaces out of sync. Flagging the coupling so the disposition round doesn't do half of it. | **(a)** coupled with B1 |
| **B4** | `STATUS.md` KEY THRESHOLDS ECI row + `CATALYSTS.tsv` 2026-10-30 row | Both carry the adopted bands incl. **3.5% = INDETERMINATE**, with the honest note that it was **not** registered before the Q2 print (HENRY proposed 7/28; his packet sat unprocessed; moot only because the print was 3.4%) | **Seed ④ answer: yes, the adoption is where the next grader will actually read it** — KEY THRESHOLDS is boot-read at B1, and the CATALYSTS row is surfaced by `catalyst_countdown.py` at B2. **No defect.** One judgement call for you: those are *grading* surfaces, not *registration* surfaces (§C). Claims prints get a frozen `GRADING_CARD`; ECI now carries comparable pre-registered branch structure but no card. | **(b)** — should ECI (and other quarterly gauges) get a frozen card like claims prints? |
| **B5** | `PREDICTIONS_SCOREBOARD.md` §D changelog (last line) | *"Next update: LAB-03/06/08/10/11/12/13/17 as they resolve"* | **LAB-17 resolved today** and is scored in §A. List is stale. Cosmetic. | **(a)** |

---

## §C — ECI series-definition tripwire (seed ②)

| # | File:line | What it says | Why it needs the annotation | Class |
|---|---|---|---|---|
| **C1** | `STATUS.md` KEY THRESHOLDS — new ECI row (added today) | Carries the bands (≥3.6% CONFIRM / 3.5% INDETERMINATE / ≤3.4% DENY) and current values (civilian comp 3.4% / private wages 3.1%) | **It does NOT carry the Dec-2026 series-definition tripwire.** Per the release itself (BLS USDL-26-1270): *"Beginning with the publication of ECI data for December 2026, the ECI will introduce **updated employment weights and remove workers' compensation costs**."* That is a basis change to the series a live threshold is denominated in. Right now the tripwire lives **only** in `KB-LAB-126` Notes and the `CATALYSTS` 2026-10-30 row — **not on the threshold row itself**, which is the surface a future session grades against. Rebased-metric class (`[[finding_rebased_metric_check_made_date]]`). | **(a)** annotate the threshold row |
| **C2** | `workbook/PREDICTIONS.tsv` (all 17 rows) | — | **Checked: no open prediction is ECI-denominated.** LAB-12 is U-3, LAB-06 is ISM, LAB-08 is QCEW. So C1 is the **only** boot-read surface needing the tripwire. Informational — no action. | — |

---

## §D — Spine-token sweep misses in my OWN 7/31 session (self-flagged)

`CLAUDE.md` C1 SPINE-TOKEN SWEEP: *"when a core series (or a gate/state) changes, update **every** surface that carries it … not just the dashboard row."* I updated the header, CORE TENSION, SIGNAL DASHBOARD, KEY THRESHOLDS, matrix v7/v13, calendar, predictions and BOTTOM LINE — and missed these four. Same file, same session.

| # | File:line | What it says | Why it's wrong | Class |
|---|---|---|---|---|
| **D1** 🔴 | `STATUS.md:181` (EXIT RULES, Kill B) | *"Declared dead in April … **but 7/23 printed 187K, 2K above the line: path RE-OPENING watch.** 0 of 5 banked (187K doesn't count)"* | Superseded twice over: **187K revised to 188K** (so it is 3K above the line, not 2K) and **w/e Jul 25 printed 197K** (12K above). I updated the parallel KEY THRESHOLDS bull-side row (`STATUS.md:105`) and left this one. **Two boot-read rows in one file now describe the same exit rule with different numbers.** | **(a)** |
| **D2** | `STATUS.md:134` + section header (DANGER WINDOW) | Header *"(updated Jul 2)"*; Late-July row: *"Leg 1 GRADED 7/23 … **leg 2 = 7/30 print** (Meta cohort's week); LAB-17 35→5%"* | LAB-17 **resolved ❌ today**; leg 2 is graded; 35→5% is superseded by the terminal grade. Row presents a closed test as live. | **(a)** |
| **D3** | `STATUS.md:3` (`**Status:**` standing line) | *"claims 208K w/e 7/11 (below year-ago)"* | Two prints stale, presented in the standing status line as current evidence. (The line's own 7/23 parenthetical adds 187K, which is *also* now superseded.) | **(a)** |
| **D4** | `STATUS.md:124` (FED TRAP 7/24 regime-fold block) | *"The 187K 57-year low is **hawkish fuel into FOMC 7/28-29**"* and *"**ECI 7/31 is the clean test** … it lands two days after the decision"* | Both events have now occurred and are graded. The block is dated 7/24 so it legitimately keeps its own as-of, but it is **forward-framed** ("into", "is the clean test") in a section a boot reads as current thesis. Light-touch: past-tense it and point to the grades. | **(a)** |

---

## §E — Stale prices and cross-owner values in the boot-read dashboard

Root `CLAUDE.md` Critical Rule 4: **"Prices must be live. Never cite prices from STATUS files."** These are prices *inside* a STATUS file presented in a live-reading table.

| # | File:line | What it says | Why it's wrong | Class |
|---|---|---|---|---|
| **E1** 🔴 | `STATUS.md` SIGNAL DASHBOARD KELYA row **vs** `STATUS.md:178` EXIT RULES | Dashboard: *"KELYA **$13.00** (−0.84%) \| [CONF] live 7/2"* · EXIT RULES: *"✅ DTE ≤30 checkpoint FIRED 7/23 (**spot $15.23** > $10)"* | **Direct internal contradiction — one boot-read file carries two different prices for the same instrument**, 29 days and $2.23 apart, neither flagged as superseding the other. The dashboard row is the stale one. | **(a)** |
| **E2** | `STATUS.md` SIGNAL DASHBOARD "Market tape 7/2" row | *"10Y **~4.47 ≈flat** … \| [CONF HENRY/PROME 7/2 ~9:05-9:20]"* | A 29-day-old rate in a live dashboard. Also **contradicted by material I hold**: HENRY's 7/28 packet documents a 7/17→7/23 bear leg of **+16bp on the 10Y** then a −2bp relief leg — so 4.47 is not even directionally current. HENRY owns the value. | **(a)** demote/date-stamp; **(c)** HENRY for the live figure |
| **E3** | `STATUS.md` Convergence Matrix vector 15 (Hormuz) | *"Brent spiked $78.82 … settled **$76.01 (7/9)**"* | 22 days stale, and I hold a contradicting datum: HENRY's 7/28 packet cites a **Brent −12.7%** collapse as an out-of-sample dovish impulse around 7/23-24. The vector scores **1 ⚪** so nothing hinges on it, but the number is presented as current. **BRENT owns the price.** | **(c)** BRENT/HENRY; **(a)** to re-tag `[STALE 2026-07-09]` |
| **E4** | `STATUS.md` SIGNAL DASHBOARD FL claims row | *"IC 5,600 (−520) w/e Jun 27; insured 30,533"* | 34 days stale (five claims prints have landed since). T-11 was graded NOT FIRED on 7/21 off newer LAUS data, so the dashboard row lags its own grade. | **(a)** |
| **E5** | `STATUS.md` SIGNAL DASHBOARD WARN cumulative row | *"2,954 / 270,641 **[EST aggregator 7/23]**"* | 8 days old but **correctly `[EST]`-tagged and dated** — this is the hygiene standard the rows above fail. Informational, no action. | — |

---

## §F — Boot-read ledgers carrying superseded state

| # | File:line | What it says | Why it's wrong | Class |
|---|---|---|---|---|
| **F1** 🔴 | `docket/WARN_COHORT.tsv` — 4 of 7 data rows | Status column: **Meta Platforms eff 2026-07-22 → `FILED`** · **Intuit eff 2026-07-31 → `FILED`** · **LinkedIn eff 2026-07-13 → `EFFECTIVE`** · **Baker Hughes eff 2026-07-01, claims_window "already printed" → `EFFECTIVE`** | The file's own header defines the vocab: *"`LAPSED-LOW` (effective passed, no claims signal)"*. **Meta's effective date passed 9 days ago and its claims window printed 7/30 with no signal** — it is still `FILED`. **Intuit's effective date is today.** LinkedIn's and Baker Hughes' windows both printed with no signal. Given LAB-17 resolved ❌ on precisely these cohorts being invisible, **all four should read `LAPSED-LOW`** — the status the vocab was written for. **This is the ledger that feeds LAB-17-class tests and would have made the L-08 sizing defect visible earliest**; it is the one that went un-updated. Boot alert is >30d, file created 7/10 (21d), so **no alert will fire before the statuses rot further**. | **(a)** |
| **F2** | `board_log.tsv` (last row 2026-07-20) | Last logged disposition 7/20 | **`inbox/WALTER/SIG-W-20260727-006.md` arrived 7/27 and has no `board_log` row** — 4 days un-dispositioned. My spawned-mode boot card **step 1a** requires: *"disposition anything threshold-relevant, **or write a dated PARKED entry** — never let a WALTER SIG or routed note sit unseen across sessions."* **My 7/31 session listed it and wrote no PARKED entry — I violated my own step 1a.** Self-flagged. | **(a)** |

---

## §G — Pending-inputs annotation (seed ⑤)

| # | File | What | Class |
|---|---|---|---|
| **G1** | `STATUS.md` — no PENDING INPUTS section exists | **Correction to my 10:16 count: it is now 8 packets + 1 WALTER SIG, not 6+1.** Two landed *during* today's session: `2026-07-31_from-NEXUS_eci-claims-raw-capture-three-grades-owed.md` and `2026-07-31_from-PROME_phase2-embed-packet.md`. Full list: RED 7/24 (kfrc/eci) · MARCO 7/25 (wage instrument) · **MARCO 7/25b RETRACTION — read with the 7/25, the instrument was falsified by its own confirmation panel** · PROME 7/25 (carve-out) · HENRY 7/28 (ECI — *consumed* for today's grade, not filed) · NEXUS 7/28 (KFRC grade owed) · NEXUS 7/31 · PROME 7/31 · `inbox/WALTER/SIG-W-20260727-006.md`. This is the **canonical-surfaces-stale / inbox-carries-live-state** class: STATUS presents as canonical while live state sits unread in `inbox/`. A standing PENDING INPUTS block in STATUS, refreshed at C1, would surface it at B1. | **(a)** to add the section; **(b)** if it should be a fleet-wide STATUS convention |
| **G2** 🔴 | `inbox/2026-07-31_from-PROME_phase2-embed-packet.md` — **actionable, and blocked by this round's no-edit rule** | The Will-approved (7/28) three-tier memory restructure executed today. `MEMORY.md` now auto-loads only unpredictable-trigger rows; **`project_labor_standing_nexus_brief` moved to `memory/auto/INDEX_COLD.md` marked `embed-pending → LABOR CLAUDE.md/boot card`.** Until I embed it and confirm, **that rule no longer auto-loads at boot** — it only reaches me on demand. The required edit is to my `CLAUDE.md`, which this audit round forbids. **Flagging so it is not lost between rounds:** the disposition round should embed the one-liner ("LABOR maintains a standing `NEXUS_BRIEF.md` (Tier-1), refreshed every closeout — not Tier-2 'skip'") and confirm to PROME so you can flip `embed-pending` → `embedded`. | **(b)** — needs the disposition round; PROME awaiting confirmation |

---

## §H — Minor / informational (no action urged)

- **`CLAUDE.md` IDENTITY tension (line 12, refreshed 7/24)** names ECI as one of three discriminating tests *"not U-3."* Still forward-valid (next ECI 10/30), but it predates the ECI result and reads as if the test is pending. Worth a one-clause refresh at the next CLAUDE.md touch. **(d)**/informational.
- **`CLAUDE.md` RESEARCH TOOLKIT — WARN Lead Time row** already carries L-08 (*"Cohort-to-base ratio ≥~10% … (L-08); below that = state-level test only"*). ✅ **So L-08 IS on one boot-read surface** — which makes §B1 narrower but no less real: it is in the *toolkit description*, not in the *registration gate list* that governs writing a prediction. Same row says *"TX API live"*; `warn_texas.py` was repointed 7/10 to the **TWC Excel primary** with Socrata as fallback — "API" is now imprecise. **(a)** cosmetic.
- **`workbook/KB.tsv`** — last row before today was 7/24; three rows added today (KB-LAB-126/127/128). Well inside the >21d boot alert. ✅ no finding.
- **`docket/CATALYSTS.tsv`** — lints clean (8 cols, 11 rows) after today's sync; graded rows pruned, the two owed grades annotated, ECI 10/30 added with the tripwire. ✅ no finding.
- **`NEXUS_BRIEF.md`** — re-pinned today (As-of, pivot, VIEW, forward catalysts). ✅ no stale-surface finding. Note its footer still carries the standing ask to NEXUS to ratify LABOR's Tier-2→Tier-1 scope change in `BRIEFS_MAP.md` row 55 — **unanswered since Jun 16**, and now directly coupled to G2. **(c)** NEXUS.

---

## Summary by class

| Class | Count | Items |
|---|---|---|
| **(a)** self-fixable mechanical | **15** | A1, A2, A3(part), B1, B2, B3, B5, C1, D1, D2, D3, D4, E1, E4, F1, F2 *(+E2/E3 partial re-tagging)* |
| **(b)** needs Will/PROME ruling | **6** | A2(part), A3(part), A6, B4, G1(part), G2 |
| **(c)** owner-owed by another agent | **3** | E2 (HENRY, 10Y), E3 (BRENT, Brent price), NEXUS_BRIEF scope ratification (NEXUS) |
| **(d)** delete/retire | **3** | A4 (BD-03), A5 (BD-08), H IDENTITY-tension refresh |

**Highest-value three, if the disposition round is time-boxed:** **A1** (the freshness gate is specified against output the command doesn't print — fixes the recurrence mechanism, not just today's instance) · **B1+B2 atomically** (a control asserted-as-installed but absent is worse than a known gap) · **F1** (the WARN→claims ledger is the earliest place a sizing defect becomes visible, and it is the one nobody updated).

**No edits applied. No thresholds moved. No files touched outside this packet.**

— LABOR
