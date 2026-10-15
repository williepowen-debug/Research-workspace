# COMMISSION — what is widening the CCC tier alone? Consumer-exposed issuers tested against named rivals

**Commissioned by:** Will, in the NEXUS session, 2026-10-14 21:21 ET, verbatim: *"start the draft now, and commission #3"*. Item #3 as NEXUS put it to him minutes earlier: *"Ask CARL, OTTO and LIQUID whether consumer-exposed borrowers explain the CCC widening."* · **Spec author:** NEXUS (asks; integrates; grades nothing of yours) · **Owners:** CARL · OTTO · LIQUID · **due: 2026-10-19** (before the DOCKET L558 sitting, where the successor split gate must admit a credit-class candidate) · **Cost: $0; bounded — one session each, existing data and reachable public sources, no new gate, no threshold, no trade words.**

## 1. The fact being explained (FRED, first-published cells, pulled 2026-10-14 ~21:2x ET)

| | 9/24 | 10/1 | 10/13 | since 9/24 | since 10/1 |
|---|---:|---:|---:|---:|---:|
| CCC & lower OAS (`BAMLH0A3HYC`) | 1,112 | 1,215 | **1,267** | +155 | **+52** |
| B OAS (`BAMLH0A2HYB`) | 286 | 329 | 317 | +31 | −12 |
| BB OAS (`BAMLH0A1HYBB`) | 164 | 204 | 191 | +27 | −13 |
| HY OAS (`BAMLH0A0HYM2`) | 280 | 324 | 316 | +36 | −8 |

**The CCC−B gap widened on every one of the 12 published sessions 9/25 → 10/13** (826 → 950bp; the 10/12 ICE cell is a bond-holiday carry-forward and is excluded), **including the three sessions on which B tightened** (10/2 −17 · 10/6 −12 · 10/9 −5). A pure beta story (CCC moves more than B in the same direction) cannot produce a widening gap on a B-tightening day.

**Already tested and not the answer (do not redo):** rates — LIQUID 10/9, lagged-rates fit R² 0.020 on the B residual; AI disruption at the **B** tier — VULCAN 10/9 (`AGENTS/VULCAN/reports/2026-10-09_wq341-disruption-attribution.md`), named single-B incumbents flat on the widening days (equity proxy, lag untested). LIQUID 10/9: sectors NO_INSTRUMENT at the index.

## 2. Hypotheses — pre-registered before any owner reads (the commissioned one is H1; the rivals are named so a negative is informative)

| | Hypothesis | What it predicts on the gap-widening sessions |
|---|---|---|
| **H1** | **Consumer-exposed issuers** (consumer finance, subprime auto, consumer lenders, rent-to-own; consumer-facing retail/services in the CCC/B tiers) carry the move — consistent with OTTO's fixed subprime-auto panel 9 of 9 worse y/y in August (`AGENTS/OTTO/workbook/PANEL_10D.tsv`) and real hourly earnings −0.7% y/y [BLS 10/14] | named consumer issuers widen (bonds/CDS) or fall (equity, beta-adjusted) beyond noise |
| H2 | **AI-disrupted names that already migrated to CCC** — VULCAN's 10/9 list names Getty, Optimum (ex-Altice), Rackspace, iHeart as CCC; VULCAN's test covered the B tier only | those names move; consumer names flat |
| H3 | **Index mechanics** — the ICE month-end rebalance (9/30 → 10/1: CCC +36, gap +23), B→CCC rating migration adding wider names, or a few large distressed names (LME / missed coupon / default) dominating a thin tier | the move concentrates in the rebalance session or in ≤3 names |
| H4 | **Broad risk-off in the weakest credits** that no sector owns | moves spread across sectors in proportion to weight |

These are not exclusive; the answer can be "H1 + H3". **⚠️ Shared antecedent, count once:** real wages −0.7% y/y is headline CPI deflating nominal pay (RED 10/14) — it is one datum, not a second consumer signal.

## 3. The test for H1 (fixed now, so the answer cannot be fitted to it)

- **Sessions:** primary = the 7 published sessions **10/2 → 10/13** (the gap widened while B net-tightened); secondary = **9/25 → 10/1** (5 sessions). Report both; the primary governs.
- **Issuers:** OTTO and CARL name the consumer-exposed issuers with bonds in the US HY index at CCC or B (rating source + date, verified, never from memory — VULCAN's 10/9 method). LIQUID adds any it can identify.
- **Measure, best reachable first:** bond price/yield or CDS → else equity total return, beta-adjusted vs SPY (VULCAN's z = (r − β·SPY)/σ, β and σ fitted out of sample on 2026-03-02 → 09-23).
- **Verdict, first match:**
  1. fewer than **2** named issuers with reachable daily data ⇒ **NO_INSTRUMENT** (n = 0 or n = 1 both land here);
  2. **≥ half** the named issuers move beyond **\|z\| ≥ 1.0 in the widening direction** on **≥ half** the primary sessions ⇒ **SUPPORTED**;
  3. **≥ half** the named issuers sit within **\|z\| ≤ 0.3** on **≥ half** the primary sessions ⇒ **NOT SUPPORTED** (VULCAN's bar);
  4. otherwise ⇒ **MIXED**.
  Counterexamples: 4 issuers, 2 beyond \|z\| 1.0 on 4 of 7 sessions ⇒ SUPPORTED (exactly half counts) · 4 issuers, 1 beyond ⇒ falls to rule 3/4 · an issuer with an idiosyncratic dated event (downgrade, bridge, LME) is reported as such and still counted — say which.
- **Disc-A, separately:** a SUPPORTED result is TRUE-in-spirit only if the issuers' own dated events or data (delinquency, bridge extensions, guidance) sit in or just before the window; a move with no consumer-credit event is recorded as "co-moved, cause unnamed".

## 4. Who does what (each a one-line return in your own file; NEXUS cites the owner artifact)

| Owner | Ask |
|---|---|
| **OTTO** | Name the consumer-finance / subprime-auto / consumer-lender issuers in the US HY index at CCC or B (verified rating + date) and every dated issuer event 9/24 → 10/13 (downgrades, bridge extensions such as CRMT's, LMEs, missed payments, 10-D trigger breaches). Run §3 on them if their data is reachable. |
| **CARL** | Name consumer-facing CCC/B issuers outside lending (retail, restaurants, consumer services) the same way; state whether any dated consumer-credit release or event in 9/24 → 10/13 could carry a CCC move, and how CRL-29 / V16 read it. Run §3 on your names if reachable. |
| **LIQUID** | Test H3: does the gap widening concentrate in the 9/30 → 10/1 rebalance session or in a few names; is any sector decomposition of the CCC index now reachable (else confirm NO_INSTRUMENT); extend your 10/9 beta read to CCC vs B (excess over beta per session). Give H2 one line if VULCAN's CCC names are reachable to you. |

## 5. What NEXUS does with the answers

Integrates them on STATUS (R3 / R4 / T-27) and on the DOCKET L558 draft as the evidence for or against a consumer-credit candidate. **Nothing here installs a root, moves a Conf %, or opens a position path.** A NOT SUPPORTED or NO_INSTRUMENT answer is a result, not a failure; it narrows the field for the successor gate.
