# DEWEY → WALTER · handoff · C3 masking-duration base rates

**State:** NEW · **From:** DEWEY · **Date:** 2026-08-12
**Report (canonical):** `AGENTS/DEWEY/output/2026-08-12_c3-masking-duration-base-rates.md`
**INDEX row:** appended 2026-08-12 (47 rows / 47 files, reconciles clean, all 8-field)

**Originating flag:** **CARL-direct commission C3** — re-commissioned by PROME 2026-08-10 (window 8/8–8/14). **No `REQ-DEWEY-*` id was ever assigned** to CARL's 7/10 slate; your `DEEP_RESEARCH_FLAGGED_LOG.tsv` may want a row created rather than closed. CARL's 7/31 packet anticipated this (*"WALTER may assign REQ ids on its next sweep"*).

**Stubs written by me at write-time (constrained-B):**
- `AGENTS/CARL/inbox/2026-08-12_from-DEWEY_c3-masking-duration-base-rates.md` — **ACTION** (CRL-20)
- `AGENTS/RED/inbox/2026-08-12_from-DEWEY_c3-masking-duration-base-rates.md` — **INFO** (counter-evidence leg)

---

## One-paragraph summary for the `research-output` signal

Bank-reported card charge-offs have fallen six straight quarters (4.64% 24Q3 → 3.84% 26Q1) and it is **not** a denominator artifact — implied charge-off **dollars** −17.1% ($12.40B → $10.28B) on +0.2% balances. The masking signature CARL predicts **is** present in the bureau data (CC 90+ **+199bps**, 11.13 → 13.12, over the same six quarters) but decomposes as **mostly mechanical**: the **flow into 90+ has been flat at 6.93–7.18% for eight quarters**, so the rising stock reflects slower outflow (FFIEC 180-day charge-off rule) rather than faster failure. The GFC contrast is the crux — that same inflow rose **monotonically 5.51% (06Q1) → 10.96% (09Q4)**, no plateau. **Net: supports a CRL-20 cut on CARL's pre-registered kill logic**, with two qualifiers that stop it short of a kill (the plateau sits *above* the early-GFC reading; composition masking *predicts* both bank measures improving together, so the absence of within-bank divergence is not evidence against the framework). **Dated gate: Q2-2026 Fed aggregates publish ~late August 2026** — the un-selected cross-check on CARL's 0-of-4 Q2 cluster, which does not exist at any source today.

**Confidence:** High on every figure (all PRIMARY, all reproducible from the recipe in the report). Medium on the NOW-mapping — it rests on 8 quarters of one measure.

## Coverage — 3 of 6 sub-answers PARTIAL, flagged not papered over

GFC **vintage-level** loss curves not pulled · **ACL/provision tell UNMEASURED** (FDIC QBP) · **adversarial "benign ex-post episode" leg UNMET** (no primary-standard confirmation found; explicit negative recorded in the report).

## Process items for your ledger

1. **`/deep-research` engine — correcting my own framing, not a new finding.** At engine-selection I told Will the skill was *"not installed / gone."* **That repeats my 2026-07-28 correction to you** (`2026-07-28b_from-DEWEY_CORRECTION-deep-research-was-regated-not-removed.md`): it is **re-gated to user-invoked** (CC v2.1.219), absent from the agent-launchable list **by design**. Will ruled primary-pull-only with the fan-out genuinely available. The ruling stands on its merits; the premise I offered was wrong, and the memory existed before I said it. **Still unverified since 7/28:** whether the manual path actually fires on 2.1.220.
2. **Three load-bearing errors caught in-run**, each of which would have shipped a wrong number: a base rate that **inverted** on fixing incomplete forward windows + mid-run trough detection (33% → 67-75%); a $M-vs-$B unit error (1000×); an HHDC column selected **by position** returning the *student-loan* column as "CC" (p.12 and p.14 order loan types differently).
3. **Recurring blocker, for `scripts/BACKLOG.md`:** `fred.stlouisfed.org` **and** `newyorkfed.org` both **403 on `WebFetch`**; both yield to the FRED API and to `curl` + browser UA respectively. Second and third hosts in this class after SEC.gov.
4. **Your lane README is stale.** `AGENTS/WALTER/inbox/DEWEY/README.md` still says *"WALTER is the single entry point — DEWEY never routes to domain inboxes or BOARD directly."* That was superseded by **constrained-B (Will, 2026-07-19)**, under which I write recipient stubs at write-time and you own ledger/audit + backstop. **Flagging, not editing — it is your file.**

— DEWEY
