# HANS — DAEDALUS Comprehension Profile

**Built by:** DAEDALUS · **Body date:** 2026-09-05 (whole rewrite; prior body 2026-07-10) · **Method:** solo full-tree read + **the subject's own guards RUN, both directions** (UPGRADE_PROTOCOL ★ rule)
**Sources read:** `CLAUDE.md` · `STATUS.md` (238 ln / 30,883 B) · `registry/{THRESHOLDS.tsv,HANS_T_FIRED_LOG.tsv,README.md}` · `thesis/{KILL_TREE.md,ECB_2026-09-10_PREREGISTRATION.md}` · `workbook/{VX,FLOW,PREDICTIONS,KB,ML}.tsv` · `research/` · `reports/` · `inbox/` + `outbox/delivered/` · recipient trees (HENRY/BOND/TERRY/WALTER/BRENT/HAWK)
**Guards executed:** `scripts/test_hans.py` → **`Ran 36 tests … OK`** · `scripts/ledger_staleness.py --nudge HANS` → clean · registry row/class counts recomputed from the TSV · every delivery claim re-checked at the RECIPIENT's tree
**Staleness:** refresh at the **next post-9/10 session** (HNS-05 graded) or **>45d** → checkpoint **2026-10-20**

> ⚠️ **THE 2026-07-12 BODY WAS OBSOLETE IN EVERY SECTION, NOT STALE AT THE EDGES.** It described a *parked* desk with "zero registries," an empty forward prediction book, an undelivered outbox and a false revival checkbox. HANS was **revived 2026-08-28** (Will-spawned, after 43 days dark) and rebuilt in one session: threshold registry, fire ledger, kill tree, pre-registration, boot script, European primary pull, a ship-gate and a 36-test suite — **none of which existed when the old body was written.** Nothing from that body is carried forward; its text lives in git history. *(This is the cost of a 56-day profile clock on a desk that had a revival session in the gap — the map said "L3, parked" while the desk was doing L4 work.)*

---

## 1. Identity

**European macro through the U.S.-market lens** — Market class, **Tier-2 spawn-as-needed**, spawnable by PROME or Will. WALTER-coded domain `EUROPE_MACRO,GEOPOL_NON_ENERGY`; **BOND is the time-critical backup and that limit binds** (this is not a fast lane).

**The seat in one line:** Europe as an *independent source* of US-relevant stress — PMI→ISM lead, ECB/Fed divergence, EU custody of USTs, sovereign level+spread, EU gas/storage as a cost input, and the euro-area bank↔private-credit seam.

**Two scope rulings that define the current desk (both 2026-08-28, both Will/self-settled — do not re-litigate):**
- ✅ **UK IS IN** — gilts, BoE, UK sovereign/LDI. HANS took it, answering WALTER's 8/18 either/or. Reasoning is charter-based: the charter already claimed "sovereign-spread/LDI stress," gilt-LDI 2022 is *the* canonical Europe→US funding event, and `FLOW-HANS-5 UK_Pension_Stress` + `VX-HANS-1.01` were already in the book. *Only the label was missing.*
- ✅ **EU BANK / PRIVATE CREDIT AT FULL DEPTH — WILL-RULED IN-SESSION**, verbatim *"I do want HANS to handle the EU bank / private-credit scope depth."* Settles a **genuine two-consumer disagreement**: REGINALD said triage-fire-only, LIQUID said "scope it to HANS." Both well-reasoned from their own charters — which is precisely why it was a Will ruling and not a peer call. **A live self-binding constraint survives the ruling:** no onward routing of ECB FSR / ESRB findings until the May-2026 FSR special article is read **at primary**. Owning a lane does not retroactively verify what was surfaced in it.

**Ceded, unambiguously:** Japan→SAM · China→ZHAO · US domestic→HENRY · military/geopolitics→HAWK · barrels→BRENT (HANS keeps TTF/storage/LNG as a *cost-and-inflation input*, never as a war narrative). The old "Geopolitics (energy-geo)" mislabel is **fixed** — WALTER corrected the registry 8/18 and the WAR CONTEXT section was retired 8/28.

## 2. File anatomy (where the richness lives)

| Cluster | Files | State / where the richness is |
|---|---|---|
| **Charter** | `CLAUDE.md` (~200 ln) | LIVE and dense. Carries **RULE #2** (`finding_check.py` gate must be *imported into the research script*, not run as a checklist step) and a rebuilt FILES table. ⚠️ Two counts in it are stale — see §6 F-2/F-5. |
| **Live state** | `STATUS.md` — **238/250 ln, 30,883 B** | **Primary memory, and genuinely rich.** The frame-flip table (7/16 vs 8/28, dimension by dimension), the three-part term-premium **discriminator**, the energy structural read, cross-agent flag table, graded book. Cap-aware: the desk rotated §SECOND LIVE SWEEP to `workbook/` *before* breaching 250. |
| **Registry** ⭐ | `registry/THRESHOLDS.tsv` (**14 rows**) · `HANS_T_FIRED_LOG.tsv` (5 fires, 4 backdated) · `README.md` | **The best-built surface on the desk, and new.** Per-row `cadence` + `scannable` **class**, `value_basis`, `recipient_chain`. Fires carry `dispatch_artifact`. Built 8/28 when WALTER asked whether the new UK bands were registered — *the answer was "informal, and so was everything else here."* |
| **Falsification** ⭐ | `thesis/KILL_TREE.md` (21 KB) · `thesis/ECB_2026-09-10_PREREGISTRATION.md` | Per-claim kill tables naming **instrument + status**, each load-bearing claim tied to a registered prediction. The pre-registration is **SAM's form, adopted**, with a hard edit-lock and pre-committed discriminating signatures. **Time-critical — see §6 F-1.** |
| **Workbook** | `VX.tsv` 67 rows (**40 live / 27 FROZEN-or-RETIRED on purpose**) · `FLOW.tsv` 10 · `PREDICTIONS.tsv` **9 (5 OPEN)** · `KB.tsv` 40 (ZHAO schema, `Stale_By` boot-enforced) · `ML.tsv` 430 | Two-state discipline is **real**: every frozen VX row carries a dated banner *and a named UPGRADE SOURCE* — not "stale," but "here is the feed that would unfreeze it." PREDICTIONS carries `Resolve_By` **and** `Anchor_Type`. |
| **Instruments** ⭐ | `scripts/boot.py` (7 sections) · `fetch_eu.py` (ECB Data Portal keyless + GIE AGSI+) · `finding_check.py` (ship-gate) · `test_hans.py` (**36 tests, OK**) · `pmi_ism_lead_test.py` | Regression-first suite: the falsy-zero staleness bug, the AGSI `trend`-as-string crash, the `country=EU` silent-empty trap, and **the exact claim/robustness pair from the 8/28 retraction**. `pmi_ism_lead_test.py` calls `gate()` inline **and correctly FAILS** — the retracted finding stays refuted in code. |
| **Research / reports** | `research/` 9 files (5 at Jun-25 vintage) · `reports/` 3 incl. a self-authored maturity roadmap and a HANS-vs-SAM/ZHAO peer comparison | The 8/28 PMI→ISM lead test is the substantive one and carries **its own verification pass that overturned its own headline**. |
| **Mail** | inbox: 1 BOND + **6 unread WALTER SIGs** (incl. `20260904-007` France 10Y > Italy, first since 2008 — names T-09/T-10 by ID) · `outbox/delivered/` 17 · `outbox/closed_undelivered/` (empty, exists by design) | ⛔ **Charter forbids inbox processing on normal spawns** — it is a separately-spawned task. |

## 3. Per-dimension local representation

| Dimension | Where it lives | Local form | Rich? |
|---|---|---|---|
| Thesis structure | `STATUS.md` frame-flip table + §DISCRIMINATOR | Dimension-by-dimension **old-vs-verified** table, then a named three-part exclusion argument | ⭐ strong |
| Convergence / scoring | `workbook/VX.tsv` (67 banded vectors, 11 groups) | Banded Yellow/Orange/Red per vector; **no composite score** and deliberately so | good, no composite |
| Invalidation / exit | `thesis/KILL_TREE.md` | Per-claim **"what kills it / instrument / status"** tables + explicit apparatus self-challenges | ⭐ strong |
| Thresholds | `registry/THRESHOLDS.tsv` (canonical) → `CLAUDE.md` + `STATUS.md` mirrors | **Registry authoritative, mirrors declared as mirrors.** Class column distinguishes daily-scannable / monthly-print / event / compound / uninstrumented / qualitative | ⭐ strong (counts stale, F-2) |
| Predictions | `workbook/PREDICTIONS.tsv` + STATUS table + pre-registration | `Resolve_By` **and** `Anchor_Type` per row; continuous-monitoring anchor used correctly on HNS-08 | ⭐ strong (HNS-09 missing from STATUS, F-3) |
| Cross-agent routing | STATUS §CROSS-AGENT FLAGS + `recipient_chain` per registry row + `outbox/` | Per-recipient flag table with priority; fires name their action owner | good (BRENT leg broken, F-4) |

### §3b. Invalidation-surface inventory (Falsification-Sweep canonical rows)

| Surface (file) | Kills / flips what | Stamp (in-content) | Fired-state form |
|---|---|---|---|
| `thesis/KILL_TREE.md` | Each load-bearing claim C-1…C-n (term-premium source; PMI→ISM lead direction; bank-channel-quiet) | `**Created:** 2026-08-28` + per-claim cadence line ("re-grade every session") | Per-row `Status` cell — "Not firing (83 / 83.6bp)" with the live value beside the band |
| `thesis/ECB_2026-09-10_PREREGISTRATION.md` | HNS-05 **and** the §3b tactical-vs-regime read; §3c refutes the term-premium call | `Written 2026-08-28` + **hard edit-lock "nothing may be edited after 2026-09-01"** | §3a conditional prior table; §4 pre-committed wrong-list |
| `workbook/PREDICTIONS.tsv` | Individual calls | `Date_Made` + `Resolve_By` + `Anchor_Type` columns | `Status` OPEN/RESOLVED + `Outcome` HIT/MISS |
| `registry/HANS_T_FIRED_LOG.tsv` | Whether a registered band actually fired | `fired_date` + `as_of` (two clocks, correctly separated) | `state` OPEN / SUPERSEDED-BY-<id> |
| `STATUS.md` §PREDICTIONS graded block | Prior-session book | `Updated:` header + per-row grade note | ✅HIT / ❌MISS with a calibration paragraph |

**Vintage rule:** all five stamp **in-content**, none rely on mtime or git-time (PAT-039/044 compliant).

## 4. Deviations from standard (+ why) — all legitimate

1. **No composite convergence score.** 67 banded vectors, no roll-up. Correct for this desk: its live finding is that two Europe→US channels are **opposite-signed** (growth leg dead, duration leg live) — a composite would net them to nothing. *(PAT-067: a seeded handle collapsing opposite-signed sub-mechanisms into one number.)* **Do not propose one.**
2. **No `TRADE.md`.** HANS states levels and explicitly refuses proposals — its BOND/TERRY flag reads *"No proposal, no gate call — level statement only."* Trade construction is TERRY's. **N/A for this desk, not a gap.**
3. **Registry mirrors are declared, not deduped.** `CLAUDE.md` and `STATUS.md` both mirror the threshold table with "the registry is authoritative; this table is a reader's mirror. On disagreement the registry wins." That is the *right* form — and it is also exactly where F-2 landed, which is the standing cost of any mirror (PAT-137).
4. **Every spread threshold is paired with an absolute LEVEL threshold** (added 8/28 after spread-only bands read all-clear through a +33bp common-mode Bund move to a 15-year high). Two rows are **COMPOUND two-leg** — neither leg fires alone. ⭐ **This is a fleet-transferable instrument design** and a PATTERNS candidate — see §7.
5. **A qualitative, non-numeric threshold (`T-14`) sits in a numeric registry**, with an explicit note distinguishing it from the uninstrumented `T-12`: *"T-12 has no feed and cannot fire; T-14 has a feed (WALTER routing + ECB/ESRB) and is simply not numeric. A qualitative row with a live feed is trippable; an unfed numeric band is not. Do not fold them into one class."* ⭐ Correct and unusually well-reasoned.

## 5. DO-NOT-TOUCH

1. **ID sequences:** `ML-HANS-` (next 431) · `VX-HANS-` vector IDs · `HANS-T-` · `HANS-F-` · `HNS-` · `KB-HANS-` — all cited across STATUS, research and other desks' trees.
2. **The 27 FROZEN/RETIRED VX rows.** Boot excludes them **by design**; each names its upgrade source. ⛔ Never "helpfully" refresh one — read its named source first.
3. **`thesis/ECB_2026-09-10_PREREGISTRATION.md` is EDIT-LOCKED past 2026-09-01.** Corrections go in a **dated appendix**, never as an edit. This is the file's own integrity rule and it is load-bearing for the 9/10 grade.
4. **The backdated fire rows (F-002/F-004 onset caveats, F-005 evidentiary down-weighting).** Each records *why* it is weak beside the fact that it counts. ⛔ Do not "clean up" a backdate — the caveat is the content.
5. **The LIQUID no-onward-routing constraint** on FSR/ESRB findings. Live until the primary read happens.
6. **The retracted PMI regime caveat.** It is refuted **in prose, in the kill tree, and in code** (`pmi_ism_lead_test.py` fails its own gate on purpose). Do not resurrect it as a caveat; it is an untested hypothesis, not a finding.

## 6. Findings — all re-verified by DAEDALUS at the artifact (2026-09-05)

**🔴 F-1 — THE PRE-REGISTRATION'S CONDITIONAL UPDATE NEVER FIRED, AND ITS EDIT WINDOW HAS CLOSED. `HNS-05` RESOLVES IN 5 DAYS.**
`ECB_2026-09-10_PREREGISTRATION.md` §3a pre-commits to moving the prior on the **Sept-1 euro-area flash HICP**: ≥3.2% → ~88% · 2.9–3.1% → unchanged 75% · ≤2.8% → ~55% *with H2 becoming live.* **The desk has been dark since 2026-08-28** (last HANS-authored commit; 9/1 and 9/4 commits under `AGENTS/HANS/` are WALTER routing, not HANS sessions). The 9/1 print — **🔴 on HANS's own catalyst docket** — passed unattended, so the update was never applied. The file's own rule (*"nothing below may be edited after 2026-09-01; corrections go in a dated appendix"*) is now binding, which makes this **an appendix job, not an edit**. §5 additionally pre-commits to grading **§3b (tactical-vs-regime) beside the binary** — the document says in its own words that reporting only the HNS-05 HIT *"is the failure this document exists to prevent."* **This is the single highest-value item on the desk and it is date-bound.**

**🔴 F-2 — THE REGISTRY COUNT IS WRONG IN FOUR PLACES, AND THE TWO ROWS DROPPED ARE THE NEWEST AND HOTTEST.**
Recomputed from the TSV: **14 rows · 6 SCANNABLE-DAILY** (3 monthly-print · 1 event · 2 compound · 1 uninstrumented · 1 qualitative). Prose says **"12 rows"** at `STATUS.md:160`, `CLAUDE.md:143`, `registry/README.md:34`, and **"5 of the 12"** at `STATUS.md:160` and `:226`. `CLAUDE.md:197` and `README.md:12,17` say **14 / 6 correctly** — so both files **contradict themselves internally** (PAT-109: the later or stronger binding silently wins and every prose claim points at the loser). **Why it bites:** the desk's own safety sentence is *"a clean scan of the 5 does not mean the 12 are clear"* — a rule computed on wrong denominators. The two rows outside the count are **`T-13`** (UK 30Y gilt, **20bp of headroom, at/near the highest since 1998**, and the *actual* LDI instrument for `FLOW-HANS-5`) and **`T-14`** (EU bank/private-credit, the row Will just ruled to full depth). T-13 and T-14 were added late on 8/28 and the count was never re-cut behind them. *(`finding_scan_keyed_on_naming_reads_local_form_as_absence` inverted: here the count, not the scan, is the instrument that under-reports.)*

**🔴 F-3 — `HNS-09` IS OPEN IN THE LEDGER AND ABSENT FROM STATUS ENTIRELY.**
`PREDICTIONS.tsv` carries 9 rows, **5 OPEN: HNS-05/06/07/08/09**. STATUS's forward-book table lists **only HNS-05…08**; `grep -c HNS-09 STATUS.md` = **0**. The missing row is *"at Q3-2026 European bank results (late Oct–Nov), the sector shows NII/earnings holding with NO material rise in cost-of-risk"* — 70%, `Resolve_By 2026-11-30`. It is the **only registered instrument on the bank-channel claim Will just ruled to full depth**, and the desk's primary memory does not know it exists. *(PAT-098: content right, machine representation wrong — and the representation is what the next boot acts on.)*

**🟠 F-4 — TWO OPEN FIRES CITE THE SENDER'S OWN STATUS AS THEIR DISPATCH ARTIFACT, AND BRENT — A NAMED ACTION OWNER ON BOTH — RECEIVED NOTHING.**
`HANS-F-003` (TTF L2 €66.19 → **BRENT**, HAWK) and `HANS-F-004` (storage gap orange → **BRENT**, HENRY) both record `dispatch_artifact = AGENTS/HANS/STATUS.md`. Verified at the recipient trees: HAWK **did** receive a real packet (`AGENTS/HAWK/inbox/2026-08-28_from-HANS_eu-energy-fires-current-in-place-of-a-closed-june-packet.md`) — that leg is genuinely delivered. **BRENT has nothing**: `find AGENTS/BRENT -iname "*HANS*"` = 0, and no HANS file in `AGENTS/BRENT/inbox/` or `inbox/processed/`. Both fires read OPEN-and-dispatched. **This is HANS's own written rule failing on HANS's own ledger** — STATUS §Standing hygiene says *"verify delivery at the RECIPIENT's tree, never from `outbox/delivered/`"*, and a `dispatch_artifact` pointing into the sender's own tree cannot satisfy it. *(PAT-102 — the evidence lived, the routing died; `[[finding_record_of_an_action_is_not_the_action]]`.)* HANS's STATUS separately notes WALTER is holding four staged BRENT/HAWK energy signals, and says *"European gas tightening while US crude buffers sit at multi-decade lows is a joint read neither desk can make alone"* — **so the one recipient who cannot make the joint read is the one who was never sent the half.**

**🟠 F-5 — TEST COUNT: CHARTER SAYS 27, STATUS SAYS 36, THE SUITE SAYS 36.** `CLAUDE.md:196` FILES table reads "27 offline tests"; `STATUS.md:221` reads 36; I ran it — **`Ran 36 tests in 3.844s … OK`**. STATUS is right, the charter is a same-evening vintage (the suite grew from 27→36 in the session that wrote the line). Cheap fix, but it is the FILES table a booting reader trusts.

**🟡 F-6 — 8 DAYS DARK, WITH ONE 🔴 DOCKET ROW ALREADY PASSED AND THE NEXT IN 5 DAYS.** Not a defect — a Tier-2 desk is spawned, not always-on — but it is the *mechanism* behind F-1, and the 9/10 ECB is the desk's first forward grade since revival. 6 unread WALTER SIGs are queued, one of which (`SIG-W-20260904-007`: France 10Y 4.20 now yields **more** than Italy, first since 2008) **names `T-09` and `T-10` by ID and reports both legs inside their bands** — i.e. WALTER is already doing HANS's compound-row read for it.

### ✅ Where the desk is genuinely strong (recorded so the findings above are read in proportion)
Its guards **run and discriminate** — 36/36 pass, and `pmi_ism_lead_test.py` *fails its own gate on purpose* so a retracted finding stays refuted in code rather than in prose. It ships **retractions and corrections as delivered packets** (`…g_from-HANS_RETRACTION-my-regime-finding-was-a-crisis-artifact.md`). It graded its own book honestly, naming the uncomfortable pattern — *two hits that were momentum continuations and one miss that was the only call requiring a turn* — and then wrote HNS-06 deliberately on the opposite side of that error. Its pre-registration states the awkward part first (*"I am below consensus… if consensus is ~90% and I am at 75%, I am asserting the market is overconfident, and I must be able to say why"*). **The 8/28 session's own verdict on itself is the right prior and should be preserved: four defects, all found from outside, every one on a surface it had just written and therefore trusted.**

## 7. Fleet-transferable candidate (DAEDALUS lane, not HANS's)

**Pair every spread threshold with an absolute-level threshold; make the joint condition COMPOUND where both legs matter.** HANS's spread-only bands read *all clear* straight through the actual event (+33bp common-mode Bund move to a 15-year high) and would have passed a row-count audit clean. The fleet memory `[[finding_spread_metric_blind_to_common_mode]]` names the **diagnosis**; HANS's registry is the first **fix form** on disk. Candidate for a `BLUEPRINTS/` threshold-design line and/or a PATTERNS row — **dedup-before-create against PAT-119/PAT-120/PAT-133 first** (all three are band-construction anti-patterns and may already cover it; if they do, extend Evidence rather than mint an ID).

**Also owed on MY side, not HANS's:** `scripts/finding_check.py` fleet adoption — HANS's charter and STATUS both say *"Fleet adoption is DAEDALUS's to rule; HANS-local until then."* Registered as **WQ-117 A** in my build queue since 8/28 and unmoved.

## 8. Grade — **L4 (H) HELD.** Per-leg verdicts (UPGRADE_PROTOCOL review-rule 2)

| Ladder leg (Market class) | Verdict | Basis |
|---|---|---|
| L1 STATUS + BOTTOM LINE | **PASS** | 238 ln, TWO-SENTENCE SUMMARY present |
| L2 structured record, valid schema, accruing | **PASS** | VX/FLOW/PREDICTIONS/KB/ML + registry + fire log; schemas valid, ML at 430 |
| L3 convergence matrix | **PASS** | VX 67 banded rows, 11 groups (no composite — deviation 4.1, legitimate) |
| L3 exit rules | **PASS** | Bidirectional bands, compound two-leg rows, wrong-sign retirements exercised |
| L3 predictions resolving | **PASS** | 4 resolved with grades + calibration prose; 5 OPEN with `Resolve_By` + `Anchor_Type` |
| L3 dated falsification surface | **PASS** | KILL_TREE + pre-registration, both in-content stamped |
| L4 TRADE.md feeding proposals | **N/A** | Desk states levels and explicitly refuses proposals; TERRY owns construction (deviation 4.2) |
| L4 signals flowing **and consumed** | **PARTIAL** | HENRY 5 · BOND 5 · TERRY 1 · WALTER 1 · HAWK 1 confirmed at recipient trees; **BRENT 0 against two OPEN fires naming it** (F-4) |
| L5 clean closeouts, 2 cycles | **FAIL (1 of 2)** | Only the 8/28 revival cycle; no HANS-authored session since |
| L5 zero YEYOU flags | **WAIVED** | No YEYOU feed exists fleet-wide (`REVIEW_LOG.tsv` empty all-time) — waiver is charter-standing, not a HANS concession |
| L5 current | **FAIL** | 8d dark; 9/1 🔴 docket row passed unattended; F-1 conditional update unapplied |

**Conf H** — held: I read the artifacts and **ran the guards** rather than reading their claims. **Not a demotion.** L4 is a fair reading of a desk that rebuilt itself in one session; the L5 legs are dated and near — leg (b) resolves **2026-09-10**, and a single post-ECB session that lands the appendix, the count fix and the BRENT dispatch would close (a) leg 2 and (c) together.

**L5 next-upgrade line:** *cycle 2 clean — a session after the 9/10 ECB with HNS-05 **and the §3b tactical-vs-regime read** both graded, the F-1 appendix filed, the 14/6 registry counts re-cut, HNS-09 surfaced in STATUS, and the BRENT dispatch closed at BRENT's tree.*
