# FLG — EXIT PROTOCOL (kill rail)

**Kill rail re-derived: 2026-08-20** *(this in-content stamp is the vintage the Falsification Freshness Sweep dates from — never mtime, PAT-039/044)*
**Author:** DAEDALUS at build · **Status:** ⚠️ **PROVISIONAL — authored against the SEED, not against a thesis.** `THESIS.md` is v0.1 (a skeleton of open questions), so these legs kill a *stance*, not a finished thesis. **FLG re-derives this rail at first live session and re-stamps it.** Until then, cite it as build scaffolding.

---

## What this rail is for

The stance at build: *FLG carries the cohort's worst instrumented CRE concentration, credit quality and reserve coverage, and no desk has ever written a thesis on it.* This file names what would prove that stance wrong — **in both directions** — before anyone builds a position on it.

**Channel-kill vs thesis-kill (blueprint §4).** Three channels below are independent enough to die separately. A dead channel is not a dead thesis; say which one died and name the migration path. ⚠️ **But see the Independence note** — this is a single name, so the channels share one antecedent (the multifamily book) more than a multi-name thesis would. Two legs failing on the same root count once.

---

## K-1 — THE COUNTER-THESIS: deleveraging works

**This leg is listed first deliberately.** It is the leg the seed data already partly supports, and a rail that buries its strongest counter-evidence is decoration.

| | |
|---|---|
| **Fires from state** | STANCE-BEARISH (the only state where it means anything) |
| **Instrument** | `workbook/MI3_FLG.tsv` → `loans_qoq_pct`, `total_loans_k`, `total_assets_k` (FFIEC Call Report, RSSD 694904) |
| **Kill condition** | `loans_qoq_pct > 0` for **2 consecutive filed quarters** AND nonaccrual rate falling across the same 2 quarters |
| **What HEALTHY looks like** | The series is populated and moving: 12 quarters present, QoQ values ranging −10.9% to +12.7% (observed). **A frozen or all-zero column means the instrument died, not that the bank stabilised** (PAT-060) |
| **If it fires** | The run-off stopped while credit improved. The bear framing is not "early" — it is **wrong on mechanism**. Re-derive from scratch; do not re-date and hold |
| **Migration path** | None. This is a **thesis-kill**, not a channel-kill |

**Already-known evidence AGAINST the bear stance, recorded at build:** assets −21.1% and loans −28.8% (2023-09-30 → 2026-06-30), MI3 `v1_pct` 5.28% → 3.65%. The bank has been shrinking for eleven quarters. **This leg is close to live, not hypothetical.**

---

## K-2 — The concentration ratio is a denominator artifact

| | |
|---|---|
| **Fires from state** | STANCE-BEARISH-ON-CONCENTRATION |
| **Instrument** | Call Report CRE composition (construction / multifamily / non-owner-occ NFNR, separately) + total risk-based capital, both as levels |
| **Kill condition** | The **CRE numerator in dollars** is flat-or-falling across ≥3 filed quarters while the ratio rises — i.e. the ratio moved on the denominator |
| **What HEALTHY looks like** | Both numerator and denominator quoted as **dollar levels** beside the ratio. **A ratio published without its two levels cannot test this leg at all** (`finding_spread_metric_blind_to_common_mode`) |
| **If it fires** | Channel-kill on concentration. The credit-quality channel (K-3) survives independently |
| **Migration path** | Drop concentration to a reported-not-scored channel; the thesis migrates onto nonaccrual + coverage |

⚠️ **This is the OPEN CONSTRUCT-VALIDITY QUESTION from the charter, in kill-leg form.** It is unresolved at build and routed to REGINALD. **No concentration threshold registers before it is answered.**

---

## K-3 — Credit quality repairs

| | |
|---|---|
| **Fires from state** | STANCE-BEARISH-ON-CREDIT |
| **Instrument** | Nonaccrual / total loans; ACL / nonaccrual — both from the Call Report |
| **Kill condition** | Nonaccrual rate below the **cohort median** for 2 consecutive filed quarters **OR** ACL/nonaccrual coverage above 100% for 2 consecutive filed quarters |
| **What HEALTHY looks like** | Both ratios present and moving quarter to quarter. **Coverage pinned at an identical value across quarters is a parse failure, not stability** — check the underlying cells |
| **If it fires** | Channel-kill on credit quality. Concentration (K-2) survives independently |
| **Migration path** | Thesis migrates onto the concentration + rent-regulation mechanism alone — **which is weaker, and say so at the time** |

*Seed reads: nonaccrual 4.88% vs cohort median ~0.89% (implied by REGINALD's "5.5× the median"); coverage 29%. Both are MIRROR-grade and re-verify at first live session.*

---

## K-4 — The mechanism itself is wrong

| | |
|---|---|
| **Fires from state** | ANY |
| **Instrument** | NYC RGB published rent-guideline orders + FLG multifamily nonaccrual trend |
| **Kill condition** | RGB grants rent increases materially above the recent run-rate for 2 consecutive annual votes **AND** FLG multifamily nonaccrual falls across the same window |
| **What HEALTHY looks like** | RGB publishes an order annually; a missing order means the vote slipped, not that rents were frozen |
| **If it fires** | The rent-regulation transmission is severed. **This kills the reason FLG is a separate desk at all** — escalate to PROME for a scope review, do not quietly re-scope |
| **Migration path** | None that keeps this desk distinct from REGINALD's cohort view |

⚠️ **Compound-gate audit on K-4** (blueprint §3, PAT-072): two legs, `AND`-joined. **Not base-rated — admitted, not hidden.** The RGB series is annual, so this gate can fire at most once per year and needs ≥2 years to satisfy. **Base-rate it at first live session or retire it**; an un-base-rated compound kill is the exact shape that fails silently.

---

## BIDIRECTIONAL FLIP — the cleanest single read each way

*Blueprint §4: name the one thing that falsifies the stance in BOTH directions, testable at the next data release.*

**Next testable release: Q3-2026 Call Report, ~2026-11-14** (RULE-anchored: quarter-end + 45d).

| Direction | The single read | Threshold |
|---|---|---|
| **Confirms the stance** | ACL/nonaccrual coverage falls further while nonaccrual rises | coverage < 29% **and** nonaccrual > 4.88%, same filing |
| **Falsifies the stance** | Coverage rebuilds while loans stop shrinking | coverage > 50% **or** `loans_qoq_pct > 0`, same filing |

**Both readings come off ONE filing, and neither needs an intervening judgment.** That is the property to preserve when this rail is re-derived.

---

## Standing discipline on this rail

- **Every `AND` above states the state it fires FROM.** A kill that cannot fire is indistinguishable from a thesis that is still true — and unlike a broken deploy gate, nobody ever complains about it (blueprint §4).
- **"Sustained" carries a count everywhere it appears** — here always in *filed quarters*, never in days, because the instrument is quarterly. A day-count on a quarterly instrument is untrippable by construction.
- **No leg above was already satisfied at write time.** Verified at build: coverage 29% (not >50%), `loans_qoq_pct` +0.9% at 2026-06-30 — ⚠️ **one quarter positive already.** K-1 needs two consecutive; it is **one quarter from firing.** This is the single most important line in this file.
- **Executability (`finding_executability_is_a_separate_audit_axis`):** every leg grades off a quarterly filing available to any reader at a public source. No leg needs an instrument that quotes faster than the claim it grades.

---

## Re-derivation log

| Date | By | What changed |
|---|---|---|
| 2026-08-20 | DAEDALUS (build) | Rail authored against seed evidence. PROVISIONAL — no thesis exists yet. K-1 flagged one quarter from firing. |
| *(next)* | FLG, first live session | **Re-derive against `THESIS.md` v1.0, re-verify every seed figure at a primary, re-stamp the date above.** |
