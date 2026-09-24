# LESSONS.md — OZK Mistake Patterns & Rules

*Read at boot. Learn once, prevent forever. Verified mistakes that burned us, each with a prevention rule. Will's preferences and data-source recipes live in `MEMORY.md` (Feedback + Findings). Seeded from REGINALD/LESSONS.md at the 2026-04-24 spinout; restructured 2026-09-24 (grouped by type, retraction banners folded into clean rules — prior wording in git history).*

---

## A. Data & sources

### Verify agent data against primary filings
**Mistake:** PSEC was reported at 35% PIK — actual 8.6% per filing; consumer-finance names assumed stressed showed improvement in their filings.
**Rule:** before any metric informs a trade or a grade, verify it against the 10-K/10-Q. For OZK that means the **FDIC-filed** 10-Q (cert 110) — agent research is a starting point, not ground truth.

### Verify real-time prices before building narratives
**Mistake:** STATUS carried Brent $118-125 and built an FL energy-shock cascade on it; actual was $81.40.
**Rule:** confirm levels from a live source, with the vintage label, before modeling anything downstream. A 45% input error produces garbage on every output.

### Date your data
**Rule:** every metric carries a date and a basis ("Q2'26 Call Report", "as of 9/23 close"). An undated number in STATUS will be read as current.

### Resolve dates must be anchored to the event and checked against its history
**Mistake (found 2026-09-24):** PREDICTIONS carried OZK-02/03/04 as resolving at the "Feb 27 2027 earnings" — a **Saturday**, while OZK's Q4 prints landed **Jan 16-20** in 2023-26 (FDIC FLNG). It sat there for months because the weekday checker was never pointed at PREDICTIONS.
**Rule:** write resolve dates as the **event** ("the Q4'26 print") plus an estimate grounded in the filer's own history ("~mid/late Jan; Q4 prints Jan 16-20, 2023-26"). Include `workbook/PREDICTIONS.tsv` in every `claim_check.py --check weekday` run.

---

## B. Analysis

### OZK CIB/NDFI is not monolithic
**Mistake pattern:** treating CIB or NDFI as one bucket. Fund Finance, Lender Finance, Indirect and the RESG debt-on-debt book have different collateral, credit and competitive dynamics (Q1'26: Munn said OZK is *pulling back* from Fund Finance while written Mgmt Comments showed it growing $210M → $1.275B YoY; Q3'25: PE-fund NDFI loans −$213M in one quarter).
**Rule 1:** decompose by sub-segment (Call Report Memo-10 `PV05-09` ≡ the 10-Q's NDFI breakdown) before assessing risk.
**Rule 2:** disclosures that appear on the call but vanish from the written Mgmt Comments are the leading signal.

### MI3 ("hidden CRE") for OZK — what the recipe measures, and why the 37.6% died
**The recipe:** FFIEC RC-C Memo item 3 (`RCON2746`, CRE-purpose loans **not secured** by RE) ÷ item 4 C&I; flag >20%.
**What went wrong:** (1) "OZK 37.6%, worst in screen" was carried for months and **reproduces at no quarter** on four independent paths (OZK's 18-qtr FFIEC series, REGINALD's 14-bank re-run, FDIC API, FDIC ratio series); REGINALD retracted it 8/23 — **OZK ranks 5th of 14**, live **9.35%** (Q2'26). The cause was a single-cell defect at the 12/31/2025 vintage. (2) The **denominator is a category mismatch for OZK**: its entire MI3 balance sits in item **9.a** (`RCONPV09` ≡ `RCON2746` every quarter), not item 4.
**What MI3 actually is for OZK:** the **RESG debt-on-debt book** — `RCON2746` equals management's 10-Q debt-on-debt balance at 5/5 quarters checked ($1.20B 6/25 → $0.77B 9/25 → $0.43B 6/26). → `MI3_2025Q3_ADJUDICATION.md` §6.
**Rules:** report **both bases, labeled** (÷ item 4 and ÷ items 4+9). **37.6% is kill-on-sight.** ⛔ **Scope fence:** MI3 says nothing about the **secured** book (RESG, IQHQ/RaDD, classified, the 11 tracked credits) — never read an MI3 fall as a CRE-thesis weakening.

### Distinguish the three masking levels — and rank them from live evidence
1. **Extend-and-pretend** (don't force refinancing) · 2. **Mark-to-model** (don't write down) · 3. **Classification** (carry CRE as C&I).
All three can coexist. On the live evidence OZK's primary vectors are **(1) mark-to-model** — nonaccrual $296.6M carried at collateral FV $281.5M, **$250.4M of it with $0 ALL** (Q1'26 10-Q) — and **(2) extend-and-pretend**, described by management itself on 7/22 (RaDD extension + recap, interest from reserves, "will remain a pass-rated credit"). The old "classification is primary" ranking was derived from the dead 37.6% and died with it.
**Watch for:** foreclosed transfers at prior-appraisal values; substandard accrual with no specific reserve; SpecMention "churn" that migrates into classified.

### A threshold on a transit bucket is mis-specified
**Mistake:** THESIS kill-§1 thresholds *past-due* — a bucket credits pass **through** — and "fired" at Q2'26 when 30-89 fell −88% while NPA rose +31.9% QoQ. The fall can mean cures **or** migration, and balances can't tell which. **Second mistake, same case (CATO OZ2, 9/24):** we then dismissed the fired warning as "migration-through" on an implied roll-forward — but the same endpoints fit a flow with zero migration from the bucket. A dismissal built on an inference leaves the warning ambiguous, not harmless.
**Rule:** threshold a **stock**, not a transit bucket. Ask: *can this fall because things got better AND because they got worse?* If yes, pair it with the destination buckets (30-89 + nonaccrual + OREO). When such a criterion fires, record it as **fired**; call it harmless only on credit-level or disclosed roll-forward evidence, never on balance endpoints (see §"Net endpoints"). (Re-spec = P-OZK-4, Will-gated.)

### Reproduce the baseline before you grade against it
**Mistake (2026-08-07, n=2 desks):** OZK's 37.6% and WAL's "+8.7pp over 2 quarters" (really 6) were both load-bearing for months with the recipe written down the whole time.
**Rule:** recompute from the primary on the stated basis before a number grades anything; if it doesn't reproduce, the output is a **basis dispute, not a verdict.** Two-endpoint claims carry their interval — the shape of a series is not recoverable from its endpoints. **Recording a recipe is not running it.**

### Net endpoints cannot exclude a transfer offset by runoff
**Mistake (2026-09-24, CATO RB2):** the L181 verdict first called within-NDFI reclassification **REFUTED** because the other buckets grew only +$68M and "9.a would stay flat." A transfer of 432,181 PV09→PV06 plus 409,544 of PV06 runoff fits every reported cell exactly; "9.a would stay flat" was simply false.
**Rule:** quarter-end balances show **stocks, not flows**. Without gross flow evidence or an issuer statement, the strongest honest token is **"not supported by endpoints, not excluded."** Write verdicts in layers — **OBSERVED / INFERRED / NOT EXCLUDED**. A commitments line moving the same way doesn't discriminate either.

---

## C. Records, claims & surfaces

### Compressing a finding drops its qualifier — and the qualifier IS the finding
**Mistake (written 8/23, caught 8/28):** "OZK files 10-Q with the **FDIC**… there is no **SEC** 10-Q" was restated as "OZK files no 10-Q — do not plan research around an MD&A that does not exist." Dropping **SEC** turned a routing fact into a non-existence claim and closed this desk's most productive primary (the source of the debt-on-debt pillar) for 5 days.
**Rule 1:** re-read the row you are compressing first; the qualifier (`SEC`, `as-reported`, `segment`, `average-basis`) is usually the whole content.
**Rule 2:** never let a compression stand beside its source — replace or cross-link; a file that argues with itself resolves by recency, not correctness.
**Rule 3:** "not at source X" is never "does not exist" — grep `raw/` and the KB before writing "there is no Y." [[finding_scope_negative_needs_the_counterparty_standard]]

### A negative finding carries its window IN THE SENTENCE — and a ✅ is where it rots
**The rule (WAL + OZK, independently, 2026-08-28):** "no ruling", "zero buys", "no catalyst" decay into general claims once the window is implicit. OZK's instance: "zero buys continue" off a 53-day-old pull.
**Rule 1:** write the window into the claim — "no ruling **as of 9/24**" — never a bare present tense for a dated check.
**Rule 2:** never tick ✅ a negative that has a re-check trigger (the Aimco "re-check with Q2 prep" trigger fired 7/21 and nobody acted because the tick made it look settled).
**Rule 3:** say **UNSWEPT** vs **SWEPT-AND-EMPTY** in the words themselves — both render as silence. (The Aug RaDD window was held as a calendar negative until the 8/31 sweep actually ran.)
**Cross-desk corollary:** a self-audit keyed on your own tokens is blind to claims about another desk's book — OZK missed a false negative about WAL's book that WAL found the same day. Cross-desk claims want a pass by the **cited** desk.

### A queue that keeps its finished items hides its open ones
**Mistake (found 2026-09-24):** TODO had grown since April in layered sections, ~25 ✅/obsolete items interleaved with open ones. Two real opens went unworked for months inside it: the severity-comp refresh (due 7/31) and the Affinius maturity verification (open since 4/22). STATUS had the same shape — a ~2 KB session log in its header, five resolved Open Items, a "Recent Developments" table two months stale.
**Rule:** a queue or dashboard holds **only live state**. When an item closes, it leaves (one-line retired list + git history), it isn't struck through in place. Rebuild, don't append, when a surface's sections start carrying dates older than its own cadence.

### STATUS is a dashboard, not a log
**Rule:** STATUS holds current state, thresholds, positions and forward dates. The header is a **stamp** (date + pointer), never a session narrative — session history goes to MEMORY, evidence to `research/`, header history to git. Charter cap ≤250 lines; keep it well under the 32,550 B read-cap (rebuilt 9/24 to ~14 KB).

### Root `CLAUDE.md` and `AGENTS/OZK/CLAUDE.md` are two different files — cite the path
**Mistake (2026-08-07):** the 37.6% was reported as living in **root** `CLAUDE.md` (Will-gated) in five surfaces; root had zero hits — every quote was `AGENTS/OZK/CLAUDE.md:16`, which auto-loads alongside root. It inflated a Will-facing proposal's blast radius.
**Rule:** grep the exact path before attributing a quote to a shared doc; cite `file:line`, never from recall. Mis-crediting *upward* (agent-local → root) escalates into Will's gated surface.

---

## D. Tools & machine-read surfaces

### Banner vocabulary in a machine-scanned header is a TOKEN, not prose
**Mistake (2026-08-28):** writing "re-anchored to the **frozen** Option-2 window" in `PREDICTIONS.tsv`'s header silently reclassified a LIVE ledger as FROZEN in `ledger_staleness.py`.
**Rule:** the block above a TSV's data boundary is a machine-read namespace — no banner words (FROZEN/RETIRED/SUPERSEDED/ARCHIVED) even descriptively; **re-run the consuming tool after editing a file a tool classifies.** [[finding_test_the_guard_not_just_the_guarded]]

### A watch script must fail closed on missing data
**Mistake (2026-09-24, CATO RB3):** the first `flng_watch.py` printed QUIET on an empty list/object and crashed with rc 1 (the NEW code) on a row missing its id — an incomplete response could have advanced a real-world claim.
**Rule:** validate schema + coverage before any quiet verdict; malformed/incomplete → UNKNOWN; wrap `__main__` so a crash can't emit a meaningful rc; ship fixture tests (`--selftest`); word rc 0 as "no newer filing RETURNED", never "confirmed". [[finding_loosening_a_check_to_kill_a_false_alarm_inverts_the_failure_direction]]

---

*Last reviewed: 2026-09-24 — restructured into A-D; MI3 + masking-level sections rewritten as clean rules (retraction history → git); +2 rules (resolve dates; queues hold only live state); STATUS rule re-based to the charter (the old "10KB" figure conflicted with ≤250 lines). Prior: 2026-08-07 · 2026-04-24 (seeded from REGINALD).*
