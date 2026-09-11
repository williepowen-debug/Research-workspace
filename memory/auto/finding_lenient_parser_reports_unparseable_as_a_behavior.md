---
name: finding_lenient_parser_reports_unparseable_as_a_behavior
description: A lenient parser (pad/truncate rows, int-only cell parse) turns every unparseable cell into the "absent/zero" bucket, so the headline count silently equals the parse-failure count; check whether the number equals the unparseable count before reading it as behavior.
metadata:
  type: feedback
  n: 2
  first: 2026-09-03 PROME (Codex audit of ORCH_LOG.tsv + coordination_scorecard.py)
  latest: 2026-09-11 HAWK (Baltic Exchange TD3C — the 'parser' is a human panel, VECTOR-1 read / DOCKET L324)
symptoms: "N zero-drain touches" equals the number of prose cells; renderer never errors on a ragged TSV; report says "2 of 83 scored" on a column that is mostly filled with prose; row count right, every rate wrong; zip(COLS, row + padding); int(s) if s.isdigit() else None; a published benchmark keeps printing daily highs on a route nobody can transact; "professional judgement" / "in the absence of direct fixtures" in a methodology doc; index up 10x while the operators it supposedly measures are up 0.3x; a data vendor sued for continuing to publish
---

**What happened (2026-09-03):** `PROME/state/ORCH_LOG.tsv` carried 83 touch rows whose `drained` cell was written as prose ("13→1", "6 (5 root + 1 WALTER)", "n/a (drained at touch 1)") on a ledger whose header declared "N or n/a". Four rows were malformed (three 9-col, one with two records fused into 18). DAEDALUS's `coordination_scorecard.py` padded/truncated rows with `zip` and parsed integers with `isdigit()`, so every non-plain cell became `None`. The render said **"63 zero-drain touches of 83"** — and 63 was exactly the number of unparseable cells. After typing the column: 25 zero + 2 unknown. The brief-defect leg had the same shape ("2 of 83 scored" on a column 41 rows actually scored). Caught by an external (Codex) read one day before the first scheduled render; PROME had authored every row and never noticed because the renderer never complained.

**Why:** a parser that never fails routes every failure into whichever bucket `None`/empty maps to — usually the "nothing happened" bucket — and the totals still foot. Row counts, dates and "renderer ran clean" all verify. `[[finding_silent_blank_evades_review]]` is the cell-level cousin; `[[finding_instrument_reports_clean_against_the_wrong_reference]]` the reference-level one; `[[finding_adoption_is_not_validation]]` is why an authored-and-consumed ledger felt safe.

**How to apply:**
1. Before quoting any count from a rendered ledger, ask: **how many cells did the parser reject or null?** If the headline equals (or nearly equals) that number, the metric is parseability.
2. Typed columns (integer-or-EMPTY, EMPTY = UNKNOWN never 0) + **fail closed on width** (rc 2, render nothing) — never pad or truncate. Prose goes in a notes column.
3. A ledger's WRITER (here PROME) must write to the declared type; "N or n/a" in a header is a type declaration, and 63 of 83 rows broke it without any check firing — put the width/type check on the writer's append path, not only in the reader.
4. Regenerate reports, never patch them; a patched report hides the parser's behavior.

---

**Second instance, 2026-09-11 (HAWK, `KB-HAWK-366`) — and it generalizes the class beyond code: THE LENIENT PARSER CAN BE A HUMAN PANEL.** The Baltic Exchange's **TD3C** (VLCC Middle East Gulf → China) names a route — Ras Tanura → Ningbo — that had become commercially inaccessible to much of the international market. The index did not stop; its methodology permits panellists, *"when no direct fixtures are available,"* to use **"professional judgement"** by referencing comparable routes. So panellists extrapolated from **Yanbu** fixtures plus an estimated risk premium, and TD3C printed **$423,736/day (2026-03-02, against a prior record of $264,072/day in 2020)** and later above **$600,000/day** — on voyages nobody was fixing. A chartering analyst: *"Does anybody pay such freights at the moment? Nope."* Realized was ~**$13/bbl** Yanbu-China against ~**$18/bbl** implied by the peak. **Mercuria sued the Baltic Exchange in the UK High Court** for hundreds of millions on exactly this ground; the Baltic's defence — *continued lawful passage means the route can still be assessed* — is the institutional form of `isdigit() else None`: a fallback that never returns "unmeasurable."

**What made it invisible, and it is the same three things as the 2026-09-03 case:** the series was **continuous** (no gaps to notice), **well-formed** (a number every day, correct units, plausible magnitudes) and **widely consumed** (FFAs, floating-rate contracts and an ETF settle on it). Every structural check downstream passes. `[[finding_adoption_is_not_validation]]` again — heavy consumption felt like validation.

**The tell that actually worked, and it is cheap:** compare the instrument against a *realized* twin measuring the same underlying. **BWET** (~90% FFA, priced off TD3C) was **+1034.4%** from 2026-02-27 to the 2026-09-10 close while **FRO**, an actual VLCC owner, was **+27.5%** over the identical span; and **Dorian LPG's SEC filing** showed realized TCE of **$75,926/available day** against a ~$170,000/day index peak. **A ~10x divergence between an index and the operators it purports to measure is the same signature as "the headline count equals the unparseable count."**

**How to apply (additions):**
5. **Ask of any external benchmark what you ask of your own parser: what does it print when the thing is unmeasurable?** Read the methodology for a judgement/fallback clause. A benchmark with no "cannot assess" state is a lenient parser with a committee.
6. **Pair every assessed series with a realized twin before using it as a resolver or trigger** — audited operator results, fixture-based comparables, settled transactions. Divergence between the two is the finding, not noise.
7. **Litigation, regulatory challenge or a public methodology dispute over a benchmark is a first-class staleness signal** — cheaper to find than the defect itself, and it dates the problem for you.
8. ⚠️ **Shape questions are more exposed than level questions.** A judgement-extrapolated series manufactures *persistence*, because in the absence of clearing prices the panel carries the last premium forward. Anything resolving on "sticky vs decaying" is biased toward "sticky" by the defect itself — directionally, not randomly. (Live case: RED's `CHG-RED-042`, a 2026-09-30 bear/bull residual keyed on freight-rate stickiness; routed 2026-09-11.)
