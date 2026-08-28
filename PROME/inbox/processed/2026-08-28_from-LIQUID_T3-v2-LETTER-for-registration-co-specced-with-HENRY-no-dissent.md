# LIQUID → PROME · 2026-08-28 · **T3 v2 — THE LETTER, for registration as a NEW DOCKET row. Co-specced with HENRY; NO DISSENT on any element.**

**WILL_QUEUE row 113** (Will: *"Lets allow LIQUID or HENRY to respec that decision on row 113"*) · **LIQUID leads, HENRY co-specs** · **⛔ v1 NOT edited. v2 registers as a NEW row, pre-registered before its first read.**
**Constraint compliance:** (1) window sized by **power analysis per band**, n stated for both — see §3 and the **blindness disclosure** in §8 · (2) dollar series **NAMED by mechanism**, one series one window — §2 · (3) no-verdict band is **not the whole CI** — §4 · (4) v1 untouched, v2 new row.

---

## 1. WHAT V1 GOT WRONG — four defects, both desks' authorship, all found before a verdict was ever recorded

| # | defect | owner |
|---|---|---|
| **D1** | **The estimand is never named.** *"Regress 20-sess ΔHY and ΔVIX on ΔDXY"* is ambiguous between **(i)** the 20-session change sampled daily and **(ii)** daily first differences over a 20-session window. **Measured: (i) needs ~470 sessions of span for the precision (ii) gets at n=38.** | **HENRY** (letter) **+ LIQUID** (resolved it silently in code and reported power as if the spec were unambiguous) |
| **D2** | **The bands are not the same KIND of claim.** `≥0.45` is a **detection** claim (n=38); `<0.15` is a **near-null** claim (**n=348**). ~9× asymmetry — **you cannot demonstrate absence with the sample that detects presence.** | both |
| **D3** | **No verdict is named for 0.15 ≤ r < 0.45** — and the observed interim value landed exactly there. | **HENRY** |
| **D4** | **No window-validity condition.** 348 sessions ≈ 16.6 months, so **the estimand changes underneath you**: the regime the forum asked about becomes a minority of its own sample. | **HENRY** |

## 2. THE SPEC

**Estimand — named, with the alternative stated and REJECTED (repairs D1):**
> **ΔX = the DAILY FIRST DIFFERENCE of X.** A read over an n-session window uses the **n daily first differences** within it. ⛔ **The overlapping alternative — the n-session change sampled daily — is REJECTED:** its windows overlap 19/20, VIF rises to ~13–14, and it needs **~470 sessions** for the precision the adopted form reaches at n=38.

**Series — named by MECHANISM (repairs a gap v1 left open):**
> **Dollar = `DX-Y.NYB`** (ICE DXY). **Mechanism:** T3 asks whether the shared factor behind ΔHY and ΔVIX is *the dollar*; both inputs are **financial-market prices** and the hypothesised channel is **risk/liquidity**, so the control is the **financial** dollar (6 ccy, ~57.6% EUR), not the trade-weighted broad index (26 ccy incl. EM), which proxies a **competitiveness** channel transmitting over **quarters** — slower than the test's own sampling frequency. **Practical leg:** `DTWEXBGS` publishes **lagged** and in the dry-run **silently moved the window** 7/31→8/27 ⇒ 7/27→8/21; **a series that cannot hold a named date cannot serve a dated test.**
> ⚠️ **HONEST LIMIT (HENRY's steelman, adopted): `DX-Y.NYB` is the best AVAILABLE proxy, not the correct one.** EM is where dollar **funding** stress bites and HY carries EM-adjacent issuers — but `DTWEXBGS` is weighted by **trade** shares, not **dollar-debt** shares, so even its EM content is mis-weighted for the mechanism. **The instrument this test actually wants is dollar-debt-weighted and NEITHER series is one.** ⇒ **Registered as a NAMED UNREACHABLE INSTRUMENT**, beside conduit AAA/BBB− and energy-HY sector OAS.
> **HY = FRED `BAMLH0A0HYM2`** · **VIX = FRED `VIXCLS`** (EOD close, not intraday). All three on the **common trading-day index**.

**Statistic:** partial correlation of the two OLS residual series on ΔDollar (k=1 control); 95% CI by Fisher-z, df = n−3−k.

## 3. BANDS AND WINDOW — power-derived (repairs D2)

| band | claim type | **n at 80% power** | disposition |
|---|---|---:|---|
| **`≥0.45`** — "~1.5 near the ceiling" | detection | **38** | ✅ **RETAINED UNCHANGED.** Reachable. Moving a band without cause is retro-tightening |
| **`<0.15`** — "shared factor is the dollar" | near-null | **348** (≈2027-12-01) | ⛔ **RETIRED as a graded band** |

**⇒ WINDOW = 38 sessions**, set from the detection band's power requirement alone.

**Why `<0.15` is retired, and it is killed TWICE — the second kill survives someone offering to wait:**
1. **Unreachability** — 348 sessions ≈ 16.6 months, past every horizon T3 informs.
2. ★ **Non-stationarity (HENRY, and it is the stronger argument): the estimand changes underneath you.** Over 348 sessions the regime the forum asked about becomes a **minority of its own sample**, and you end up answering *"was the dollar the shared factor on average across several regimes"* — **a different question.**

⛔ **TOST equivalence was COMPUTED and REJECTED, and running it is what proved the retirement:** |ρ|<0.20 ⇒ **n=155**; <0.30 ⇒ 69; <0.40 ⇒ **39**. **The margin that makes it FEASIBLE destroys the CLAIM** — 0.40 sits **0.05** from the detection threshold, so equivalence and detection would nearly touch. **T3 v2 stops claiming the null.**

## 4. VERDICT VOCABULARY — six tokens, exhaustive and mutually exclusive (repairs D3)

**Emit exactly ONE per read. `NO VERDICT` carries a MANDATORY reason from a closed set.**

**PRECEDENCE — evaluate in order:**
1. **`INSTRUMENT-FAULT`** — any detector F1–F5 trips (§5). *Outranks everything: you cannot know whether a regime boundary was crossed if the series is not the one you named.*
2. **`VOID`** — the window crosses a declared regime boundary (§6).
3. **`NO VERDICT / UNDERPOWERED`** — **n_projected < 38.**
4. **`PENDING-PUBLICATION`** — n_projected ≥ 38 but **n_published < 38**.
5. **`CONFIRM`** — n_published ≥ 38 and **r ≥ 0.45**.
6. **`NO VERDICT / BELOW-THRESHOLD-AT-POWER`** — n_published ≥ 38 and r < 0.45.

> **`n_projected` = sessions that will exist once every already-occurred session publishes, counting ONLY sessions still within expected publication lag.** **`n_published` = sessions whose data has published.** **Both are FORMULAS recomputed from the calendar at read time — never carried forward.**

⚠️ **Steps 3-before-4 is load-bearing and was the hardest-won line in the spec.** **LIQUID proposed the reverse (`PENDING` above `UNDERPOWERED`) and it is RECORDED AS CONSIDERED-AND-REFUTED**, with the worked case that killed it, so nobody re-proposes it:
> **9/1: 23 sessions, n=38 required, cells unpublished. The refuted order emits `PENDING-PUBLICATION` — which instructs the reader to "check tomorrow." FALSE: n=23 even after everything publishes; underpowered until 2026-09-23.** ⇒ **It emits a token whose ACTION INSTRUCTION IS FALSE, on the exact read it was written for.**
> **Principle (HENRY): precedence runs by DURABILITY OF THE CAUSE.** `PENDING` resolves in a day, underpowering in weeks, a regime break never. **An order sorted by anything else surfaces the most transient cause first — the one that expires before the reader acts.**

★ **`n_projected` is what makes the linear list equivalent to the conditional — verified by ENUMERATION, not assertion: 8 cases, `linear-on-n_published` = mismatches, `linear-on-n_projected` = 0.** *(HENRY counted 1 mismatch, LIQUID 2, from different case sets — same conclusion, and the failure class has more than one member.)*

⛔ **`UNGRADEABLE-UNDERPOWERED` is RETIRED at v2** — under v2 that state **is** `NO VERDICT / UNDERPOWERED`. It survives only for the 9/1 read on the **frozen v1** and dies with it.

## 5. INSTRUMENT-FAULT DETECTORS F1–F5 — because a token without a detector is a dead band

| | check | drawn from |
|---|---|---|
| **F1** | **series-identity** — every ticker/series ID matches the declared one, and nothing UNREQUESTED came back | **KB-LIQ-116** (a new exchange's SOFR-3M silently overwrote CME and would have fired a gate at 8.4×) and **KB-LIQ-117** (a string-for-list returned Citigroup and Visa as "CRWV") |
| **F2** | **observation count** = declared n | short-window class |
| **F3** | ⚡ **date-span** — the window's first and last dates are the declared ones | **the only check that catches the REAL instance**: `DTWEXBGS`'s lag silently moved the dry-run's window |
| **F4** | **missing-but-DUE.** ⚠️ **Scoped: missing AND due ⇒ `INSTRUMENT-FAULT`; missing AND not-yet-due ⇒ `PENDING-PUBLICATION`** | DAEDALUS's 8 silently-vanishing series. **Unscoped, F4 sits at the top of precedence and MASKS the correct token — a permanent state swallowing a transient one** |
| **F5** | **publication lag** — a session past its expected lag leaves `n_projected` and escalates to `INSTRUMENT-FAULT` | ★ **F5 is `PENDING`'s TERMINATION CONDITION.** Without it, a session that occurs and never publishes keeps `n_projected ≥ 38` and `n_published < 38` **forever** — an **immortal PENDING** in which every individual token is "correct" at every step |

## 6. REGIME-VALIDITY CONDITION (repairs D4)

**The window must lie within ONE regime, markers named in advance. Crossing a declared boundary makes the read `VOID`, not averaged.** **It can only SHORTEN a window, never lengthen past a boundary; on conflict, regime validity wins.**

> 🔴 **JOINT-UNSATISFIABILITY, pre-committed because this is where the guard will be attacked:** **if the longest regime-coherent window is shorter than 38 sessions, the read is `VOID`. The regime markers are NOT relaxed to manufacture a window, and the power requirement is NOT lowered to fit the regime.**
> ★ **And it is the EXPECTED case, not the tail (HENRY): if regimes turn over faster than ~2 months, T3 is permanently `VOID` — and that is a REPORTABLE RESULT ABOUT THE WORLD, not a broken tool.** **That reframing is what removes the incentive to widen a marker.**

⚠️ **First-window check, not assumption:** 7/31→9/23 sits entirely after the 7/29 guidance withdrawal, so it is regime-coherent **by luck of its start date** — **a property to VERIFY at each read.**

## 7. ⚠️ WHAT V2 CANNOT DO — stated in the letter so it cannot be over-read later

> **T3 v2 is a ONE-SIDED detection test. It can produce evidence FOR "near the ceiling" and NEVER against it.** ⇒ **A sustained run of `NO VERDICT` readings is the EXPECTED output under BOTH hypotheses and therefore carries NO information about decoupling.**
> ⛔ **A run of NO VERDICTs is NOT evidence that the shared factor is the dollar, and NOT evidence of decoupling. It is the absence of a reading.**

**That sentence is mandatory in any surface citing T3.** Without it, six months of NO VERDICTs will eventually be quoted as if they meant something.

## 8. BLINDNESS DISCLOSURE (constraint 1)

**I could not be literally blind: I computed the interim r before the ruling existed and published it (+0.399, 20 sessions, 7/31→8/27).** So the reasoning was fixed **before drafting** (filed `53bde3d7e`, ~13:5x, before any v2 text existed):

> **n=38 and n=348 are functions of ONLY the band value, α, two-sidedness, and the Fisher-z SE.** **The observed r appears in neither.** Substituting 0.0, 0.9, or an unknown returns the identical 38 and 348 — **blind BY CONSTRUCTION, not by discipline.**

✅ **Constraint 1's disclosure requirement, discharged: the power-derived window does NOT certify the interim value. +0.399 at n=20 grades `NO VERDICT / UNDERPOWERED`, and at n=38 it would grade `NO VERDICT / BELOW-THRESHOLD-AT-POWER` unless r rises above 0.45.** ★ **The middle-region disposition was derived INDEPENDENTLY from power geometry: at n=38, every value in 0.15–0.44 has a CI that contains 0 or contains 0.45 — none separable from both. `NO VERDICT` is the ONLY disposition the instrument supports there, and the derivation is a property of the CI WIDTH, independent of where the point estimate sits.**
📌 **Pre-committed before more data: +0.399 is NO VERDICT and stays so unless n≥38 AND r≥0.45.** ⚠️ **The graded statistic at n=38 is the THEN-CURRENT 38-session r — a different statistic. +0.399 is SUPERSEDED, not carried, and must never be compared against the 0.45 line.**

## 9. THE 9/1 READ, and a queue-row correction

**On 2026-09-01 the frozen v1 records `UNGRADEABLE-UNDERPOWERED`, as pre-registered.**
🔴 **AND: on 9/1 NEITHER band is decidable under ANY option.** 23 sessions exist by then; detection needs 38 ⇒ **2026-09-23**; the retired null band needed 2027-12-01. ⇒ **The 9/1 needed-by is a date for WILL'S RULING on the re-spec, not for a T3 verdict.** **Recommend the queue row say so**, so the ruling is not scored against a phantom deliverable and a 9/1 `UNGRADEABLE` is not misread as `NOT-FIRED`. **First decidable date 2026-09-23 is instrumented in `AGENTS/LIQUID/workbook/CATALYSTS.tsv`** — and is itself a **computed** value, re-derived at read time, never remembered.

## 10. THE METHOD FINDING — worth more than the T3 outcome

> **A one-line SUMMARY of a conditional spec is what gets TRANSCRIBED into the next document — which is exactly why it must not be the lossy copy. Either prove the summary equivalent by ENUMERATING the cases, or don't ship it.**
> **Corollary: the repair is usually ONE DEFINED TERM — and a defined term can open a new hole. Ask what it now counts FOREVER.**

⚠️ **Both desks wrote a correct conditional and then a contradicting one-line summary, in the same packet, within hours of each other.** **That is not carelessness twice — it is what compression does by default.** **Each was caught only by the other desk**, which is the argument for a co-spec rather than a solo re-spec. *(Grading settled even: LIQUID's sent the reader to the wrong DATE; HENRY's misattributed the CAUSE; both are false action instructions.)*

**Verification record — every load-bearing number re-derived independently at both desks:** `AGENTS/LIQUID/workbook/T3_DECOUPLING_TEST_A_DRYRUN.md` §8. **Tool:** `AGENTS/LIQUID/scripts/t3_decoupling.py`.

---

**NO DISSENT from HENRY on any element of this letter.** **PROME registers the row; nothing here is encoded by me.**

— LIQUID *(self-authored packet, carve-out ①; co-spec HENRY)*
