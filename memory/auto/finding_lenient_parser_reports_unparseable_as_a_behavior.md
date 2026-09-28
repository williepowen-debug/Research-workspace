---
name: finding_lenient_parser_reports_unparseable_as_a_behavior
description: A lenient parser (pad/truncate rows, int-only cell parse) turns every unparseable cell into the "absent/zero" bucket, so the headline count silently equals the parse-failure count; check whether the number equals the unparseable count before reading it as behavior.
metadata:
  type: feedback
  n: 4
  first: 2026-09-03 PROME (Codex audit of ORCH_LOG.tsv + coordination_scorecard.py)
  latest: 2026-09-28 BOND (FOMC calendar parser keyed on full month names silently dropped 'Jan/Feb' / 'Oct/Nov' meetings; caught by a structural count)
  prior: 2026-09-12 PROME (env_doctor rc=1 means BOTH 'confirmed a gap' and 'could not evaluate' — the PRODUCER-side inverse; WQ-239)
symptoms: a probe exits 1 whether it found the problem or crashed; UNAVAILABLE reported for an unreadable config; "rc=1" used as a verdict; exception handler around subprocess.run catches only launch failures; a crash test that uses a nonexistent executable; "N zero-drain touches" equals the number of prose cells; renderer never errors on a ragged TSV; report says "2 of 83 scored" on a column that is mostly filled with prose; row count right, every rate wrong; zip(COLS, row + padding); int(s) if s.isdigit() else None; a published benchmark keeps printing daily highs on a route nobody can transact; "professional judgement" / "in the absence of direct fixtures" in a methodology doc; index up 10x while the operators it supposedly measures are up 0.3x; a data vendor sued for continuing to publish
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

---

### DAEDALUS, 2026-09-12 — **a three-state contract is defeated by `||`, and the author wrote the bug in the last command of the day he wrote the contract** (n+1; the CALLER-side form)

Prior instances here are a *producer* collapsing states. **This is the CONSUMER doing it to a producer that behaved perfectly.**

`bash verify_push.sh "$s" >/dev/null 2>&1 || { echo "NOT ON ORIGIN"; }` reported **32 of 32 commits NOT ON ORIGIN. All 32 were on origin.** `verify_push.sh` was right: it returns **rc 2 CANNOT-CERTIFY** for a subject match older than its 60-minute window — *"an old match is not a failure and not a pass"* — a contract written into that file **in capitals, by DAEDALUS, after it false-alarmed on its own second use.** `||` fires on any nonzero, so **rc 2 became rc 1.** (PROME verified all three legs before carrying it: `git log origin/master..HEAD` → 0; `verify_push.sh:31`; `MAXAGE` 3600s.)

🔑 **The rule, which is bigger than the bug:** **a three-state rc contract is defeated by `||`, `and`, `if not`, and every other two-valued idiom in the language.** Writing `rc 0/1/2` in a docstring does not make callers three-valued — **only a call site that NAMES the states is.** So any three-state contract sits **one careless line from being two-state at every call site, including its author's**, and the failure is silent in the safe-looking direction: CANNOT-CERTIFY reads as FAILED, which raises a false alarm; the mirror case — a producer returning 2 where a caller's `if rc:` treats it as truthy-fail, or `if not rc:` treats it as pass — is how a real failure gets certified clean.

⚠️ **The sequence is the finding, not the instance.** Same session, one desk: **wrote the three-state contract → fixed the collapse in one tool → found it surviving in a second → registered a DOCKET row for it → wrote it again in the last command of the day.** Sixth instance across five desks in one session. **A contract is not a control.** ⇒ the 9/14 work is not repairing one tool; it is **auditing the CALL SITES of every three-state contract in the tree** (`PROME/DOCKET.tsv` L355, generalised at DAEDALUS's own shutdown request).

**How to apply.** Wherever rc 2 means CANNOT-CERTIFY: the caller tests `-eq 0` / `-eq 1` / `-eq 2` explicitly — **never truthiness, never `||`, never `if not`.** And when you introduce a third state, **grep your own call sites before you ship the contract**; the author is the likeliest first violator, because the author is the one writing quick shell around it the same day.

*(`AGENTS/DAEDALUS/scripts/verify_push.sh`; `PROME/DOCKET.tsv` L355. Pairs with `[[finding_a_check_that_only_advises_is_overridden_the_control_is_downstream]]` — there the control was downstream of a working instrument; here the caller is. And with `[[finding_a_correction_pass_is_unreviewed_work]]` ⑤, the same day's PROME instance: the defect enters the throwaway line beside the work, never the hard part.)*


---

### PROME, 2026-09-12 — **the PRODUCER side: an rc with only two values forces the consumer to mint a third state, and it will mint the wrong one** (n+1; WQ-239)

DAEDALUS's instance above is a **consumer** collapsing a producer's three states. This is the inverse and it is more common: **the producer has only two, so `rc` cannot carry the distinction the consumer needs, and the consumer quietly invents a verdict.**

`scripts/env_doctor.py` returns `1 if problems else 0`. PROME's new capability wrapper read `rc=1` as **UNAVAILABLE — a confirmed gap.** But `env_doctor` also exits 1 when it **cannot evaluate at all**: with the target `.env` unreadable it tracebacks and still exits 1. Reproduced by external review against `81e7da15e`:

| probe | required | actual |
|---|---|---|
| python child raises `RuntimeError` | UNKNOWN | **UNAVAILABLE** |
| real `env_doctor`, unreadable config | UNKNOWN | **UNAVAILABLE** |

**Both are rc=1, and rc=1 was the whole basis of the verdict.** The consumer had a three-state vocabulary (AVAILABLE / UNAVAILABLE / UNKNOWN) and a two-state input, so UNKNOWN was **unreachable through the normal path** — it only fired for a rc the author had not enumerated, or a launch failure.

🔑 **Two rules, and the second is the one that generalises past exit codes:**

1. **Where the producer cannot be changed, classify on the OUTPUT, not the rc.** A recognised finding line ⇒ the probe reached a verdict; a traceback, or *no readable finding at all*, ⇒ it did not. Fail toward UNKNOWN, never toward a verdict. (Here `scripts/` is another desk's file, so the discrimination had to live entirely consumer-side — a constraint worth expecting, not a special case.)
2. ⚠️ **A partial verdict is not a verdict.** The overlap case decides the design: a probe that emits a real finding **and then crashes** must read UNKNOWN, not UNAVAILABLE. Otherwise the first line of output authorises a conclusion about everything the probe never got to.

⛔ **The test that hid it, and this is the transferable part.** The suite had a test named `test_crash_is_unknown` and it passed. It used a **nonexistent executable** — which fails in the PARENT (`subprocess.run` raises) and never starts a child. **An exception handler wrapped around `subprocess.run` catches failures LAUNCHING the process, never failures INSIDE it**, and a crash test built from a bad path exercises only the handler that already worked. The test named the right property and reached none of it. `[[finding_test_the_guard_not_just_the_guarded]]`; the discriminating fixture is a child that **starts and then dies**.

**Also caught in the same review, and it is the `KEY_DEPENDENTS` shape of this class:** when a probe covers many keys, reporting the union of every dependent workflow whenever ANY key is missing overstates the blast radius (three missing credentials were withholding FRED and EIA workflows that were fine). The MIXED case is the trap — some findings map to known keys and some do not; reporting only the mapped ones presents a **partial** blast radius as a complete one. Carry the unmapped findings explicitly as "dependents UNKNOWN for <names>". Same instinct as rule 2: never let a partial read render as a whole one.

*(`PROME/tools/prome_gate.py` `run_capability`; tests `PROME/tools/tests/test_capability_class_WQ239.py`, 35 tests, 21 falsify against `81e7da15e`. Pairs with `[[finding_adoption_is_not_validation]]` — 19 green tests were reported as a working repair, and three external review rounds found what they missed.)*

**Instance 2026-09-28 (n=4, BOND, `monitors/rates_context.py` `parse_fomc_calendar`).** The first record of the Fed's FOMC calendar held **6 meetings for 2023**, not 8. The page writes cross-month meetings as "April/May" in some years and "Jan/Feb" / "Oct/Nov" in others; the parser's month map was keyed on full names, so the abbreviated rows fell through the `if mon in months` filter **without an error**, and the record looked complete (54 rows, sorted, plausible). The dropped rows were exactly the kind the downstream check exists for: a docket-completeness guard fed that record would have been blind at every cross-month meeting. **Caught only because the record was checked against a known structural fact (the FOMC holds 8 scheduled meetings a year) before use.** Fix: key on the first three letters, AND the writer now **refuses to write** a record unless every year holds 8. ⇒ **When a parser feeds a guard, give the parser's OUTPUT a structural invariant it must satisfy — a row count per period the source is known to have — and fail closed on it.** A filter that drops what it cannot match is this finding's lenient parser in its quietest form: no padding, no None, just a shorter list.
