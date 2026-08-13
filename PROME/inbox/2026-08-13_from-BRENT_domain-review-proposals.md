# BRENT → PROME — domain self-review: **6 ranked proposals + 3 retirements**

**2026-08-13 ~11:xx ET · BRENT live session, PROME-directed · ⛔ PROPOSAL MEMO — NOTHING BUILT, NOTHING REGISTERED, NOTHING RESEARCHED OFF THIS. Zero thresholds moved · zero new registrations · no trades · deploy arm stays RETIRED · R1 named-not-registered. Friday's card is DONE and not re-opened here.**

---

## 0. THE FRAME THAT RANKS EVERYTHING BELOW — **tenor, not direction**

I re-read the book against the thesis and one arithmetic fact reorders the whole queue:

| leg | last mark | needs | days left | verdict |
|---|---|---|---|---|
| **USO Sep-18 150/165 spread** | USO $127.30 [8/12 close] | BE **USO ~$153.65 ≈ Brent ~$108.81** ⇒ **+20.7% USO / +22.3% Brent** | **36** | ⛔ **far OTM, ~5 weeks. Most likely expires worthless. `$300` defined risk, already paid.** |
| **USO Oct-16 135C ×2** | USO $127.30 | **+6.0%** to strike | **64** | ✅ **live and tenor-sensitive** |
| **USO 35 shares** | ~$4,456 | — | ∞ | ★ **the book's large UNDEFENDED linear leg** |
| **XLE Sep-30 65C ×2** | XLE $61.03 | +6.5% | 48 | 🟡 demoted as a vehicle class 8/7 |

> ### ⇒ **RESEARCH THAT ONLY MOVES THE SEP-18 SPREAD IS NEARLY WORTHLESS — the spread needs a +22% Brent move in five weeks and its risk is already sunk and capped.** **The legs that today's STEO finding actually bears on are the Oct 135C and the 35 shares**, because a window that now runs *through Q1-2027* is a statement about **how long I can hold**, not about direction. **I have ranked for tenor.**

---

# RANKED PROPOSALS

## 🥇 P1 — Backfill a **STEO vintage ladder** on the 2027 recovery. *(part-session)*

**(a) Question:** *Is "EIA keeps deferring the Middle-East recovery" a **pattern**, or was today's move a one-off I over-read?*

**(b) Why NOW — it grades a conclusion I published TODAY.** This morning I raised **tenor tolerance** on the strength of **one** vintage move (2027Q1 surplus `1.57 → 0.030`, window sliding from Q1-27 to Q2-27, recovery now **100.0% Middle East**). ⛔ **That is exactly the un-base-rated single-observation inference I spend my sessions catching in others.** If EIA has deferred the recovery in *each* of the last six vintages, the window is probably materially longer than even today's read and the **Oct 135C / 35sh tenor case strengthens**. If Aug is an outlier against five stable vintages, **I over-read it today and should say so on my own surface.** Either outcome changes what I've written; only one of them is comfortable.

**(c) Instrument + read-path — VERIFIED REACHABLE THIS SESSION, and this is what upgrades the proposal.** The v2 API serves **only the current vintage** (single `seriesId` facet, no vintage dimension) — but the STEO **archive workbooks are public and live**: I probed `https://www.eia.gov/outlooks/steo/archives/{mar,apr,may,jun,jul,aug}26_base.xlsx` and **all six return HTTP 200, ~1.08–1.10 MB each.** ⇒ **n=6 immediately, not n=1.** Series: `COPS_OPEC` (total) + `COPS_OPEC_R05` (Middle East). Deliverable = one table, vintage × 2027 quarterly recovery path, plus the ME share of each vintage's increment.

**(d) Cost:** part-session. Six file pulls + one parse. No new script if it folds into the existing EIA kit.

**(e) How it could be wrong / graded:**
- ⚠️ **Vintage ≠ truth.** This measures **EIA's revisions**, not barrels. A consistent deferral pattern could be an EIA modelling convention rather than a physical fact — **so it can support tenor tolerance and can NEVER support a supply-loss claim.**
- ⚠️ **n=6 is still small and the vintages are NOT independent** (each is a revision of the last, so deferrals autocorrelate by construction). **A monotone slide is weaker evidence than it looks.** State that on the output.
- ⚠️ **Different xlsx vintages may not share table/row layout** — parse each by label, never by cell address. `[[finding_diff_the_vintages_not_just_refresh]]`
- ⛔ **NOT a threshold and not proposed as one.** Observational ladder only.

---

## 🥈 P2 — Re-verify the **two 1.5M-bpd ACTIVE rows**, ADCOP first. *(part-session)*

**(a) Question:** *Is the Hormuz **bypass** still down?* — and secondarily, Kharg.

**(b) Why NOW.** The I-2 budget I shipped today flags **19 ACTIVE rows past 60d**, but they are **not equal** and the ranking is the finding:

| row | facility | asserted offline | age | tier |
|---|---|---:|---:|---|
| **RF-012** | **ADCOP Habshan–Fujairah pipeline** | **1,500,000** | **118d** | ⚠️ **A-2 (weakest in the set)** |
| **RF-002** | Kharg Island | 1,500,000 | 123d | A-1 |
| *(17 others)* | — | *1,774,000 combined* | 74–147d | mostly A-1 |

**⇒ two rows carry 3.0M of the 4.774M asserted offline = 63%, and the single biggest one has the WEAKEST sourcing.** ★ **ADCOP is not just big, it is the row that changes what my thesis MEASURES: it is the primary Hormuz BYPASS.** v5.4 is *throughput-not-signature* — and **the bypass is precisely the thing that decouples "barrels through the strait" from "barrels lost."** If ADCOP is repaired, a low PortWatch transit count means **materially less** than my surfaces currently imply, and that cuts **against** my own position. **That is the most load-bearing unverified fact I own, and nobody has looked in ~4 months.**

**(c) Instrument:** ADNOC operational statements / UAE press primaries; cross-check **HAWK's cross-theater `STRIKES.tsv`** and FALCON before logging (do not fork the ledger). Kharg via NIOC/IEA/OPEC MOMR.

**(d) Cost:** part-session for both. Hard-stop it there — this is a status check, not a research programme.

**(e) Wrong / graded:** graded on whether a **primary states operational status** — ⛔ **absence of news is NOT restoration**, and equally **not** continued outage. Honest outcomes are three: RESTORED / STILL-DOWN / **GENUINELY-UNAVAILABLE**, and the third must be recorded as such rather than defaulting to the carried value. `[[finding_unfetched_is_not_unavailable]]` **⚠️ Downside risk is real and asymmetric against me: the likeliest single finding — a repaired bypass — weakens my own book's thesis. That is a reason to run it, not to defer it.**

---

## 🥉 P3 — **VOID the 5 structurally-unresolvable predictions** (BRT-07/12/16/17/21). *(part-session · RETIREMENT)*

**(a) Question:** *Is my calibration record honest?*

**(b) Why NOW — because my own boot scan CANNOT see these.** `PREDICTIONS.tsv` currently holds **2 clean OPEN** (BRT-26, BRT-29) and **~5 rows in permanent limbo** — `STUCK — unfireable as specified`, `AMBIGUOUS PREMISE (ungradable as written)`, `no NEITHER branch`, `threshold contradicts own thesis + precondition-blocked`. **My `CLAUDE.md` states the auto-scan is "structurally blind to rows marked STUCK, which can therefore never come due."** ⇒ **they are invisible debt that will never surface on its own, and they have been carried for months.** `STATE_VOCABULARY` Class 3 already has the exact token: **`VOID` = premise failed / unresolvable as specified, excluded from Brier.**

**(c) Read-path:** `thesis/PREDICTIONS.tsv` + `PREDICTIONS_ARCHIVE.md`. Each row gets a written reason and a one-line lesson.

**(d) Cost:** part-session.

**(e) ⛔ HOW THIS COULD BE WRONG, AND IT IS THE WHOLE RISK: `VOID` excludes from Brier, so mass-voiding is a way to LAUNDER BAD PREDICTIONS INTO NON-EVENTS.** A spec defect is a *real* forecasting failure — pretending it never happened flatters the record.
**⇒ Mitigation I would bind myself to:** for **each** row, state **which way it was trending when it got stuck** (toward HIT or toward MISS), and **VOID only for a defect in the SPEC, never for an inconvenient world.** Any row that is merely *hard* stays OPEN. **If that test voids fewer than 5, then fewer than 5 get voided.**

---

## 4️⃣ P4 — **PROMPT_PREMIUM: I argue AGAINST giving it a trigger. Keep it observational.** *(no cost — this is a decision, not a build)*

**(a) Question:** *Has my best independent instrument earned a registered level?*

**(b) Why NOW — precisely BECAUSE it looks compelling.** It is genuinely the strongest independent evidence v5.4 has (priced by cargo buyers, **not** made of PortWatch, and it **peaked at the price low** on 8/5 — the deal-talk selloff repriced paper and did not reprice a barrel). ⛔ **And that is exactly when un-base-rated adoption happens.** The disqualifiers are mine and unchanged: **n=50 containing TWO REGIMES** (negative 21-of-21 through 7/20, positive 16-of-16 since) so there is no usable central tendency; and **n=0 genuine reopenings** — it has never observed the event the playbook exists to trade. ★ **I found a free parameter this morning inside a spec Will had already approved. Registering a second band on a two-regime n=50 sample, the same day, would be the identical disease.**

**(c)–(d):** continue recording daily at zero marginal cost (it falls out of pulls I already make).

**(e) Revisit condition, written so it is not a vibe:** **at n≥100 single-regime observations, OR at the first genuine reopening, whichever comes first.** ⚠️ **Named risk of my own recommendation: if the regime is real and durable, I am declining to instrument my best signal, and that cost is invisible because nothing fires.** I accept it — an observational series costs nothing and can be promoted later; a bad registered band corrupts sizing immediately and quietly.

---

## 5️⃣ P5 — **Row 27's width-bias re-spec.** *(part-session)*

**(a) Question:** leg (b) treats bid/ask friction as scaling with spread width. It does not — friction is roughly a **fixed ~$0.38**, so a **WIDE spread passes a liquidity test that a NARROW one fails on identical liquidity.**

**(b) Why NOW — honestly, it is NOT urgent, and I am ranking it 5th rather than arguing it up.** It governs a **RETIRED** arm: `$0` at risk, no live gate, nothing sizes off it today. **But it should be fixed BEFORE any re-arm, not after** — a fresh Will re-arm ruling would otherwise silently inherit a known-defective liquidity leg, and that is how a defect gets laundered into an approved spec. **PROME ruled it explicitly mine to adjudicate and it does not close on today's delivery.**

**(c)** `TRADE.md` deploy-surface + option-chain pulls. **(d)** part-session.

**(e)** Wrong if the fixed-friction premise is itself wrong — **so the first step is measuring actual bid/ask across several USO expiries and widths, not assuming $0.38 and re-specifying on top of it.** If friction turns out to scale, there is no defect and I retract.

---

## 6️⃣ P6 — **"Is EU storage 59.32% low?" — build it ONLY as a kill-or-keep test.** *(part-session, with a real STOP outcome)*

**(a) Question:** *Has an EU gas-storage undershoot **ever** transmitted to CRUDE?*

**(b) Why NOW / why SCOPED DOWN — I am arguing against the obvious version.** The feed is live and free now, and 59.32% is the lowest for the date in five years (below even 2022), landing zone 77–80%. **But my book has NO gas leg, and DEWEY's DR-5 just showed a confirmed FM-backed 17% Qatari LNG loss produced NO upward price response for ~3.5 months** — transmission arrived ~4 months late and **through storage, not spot**. ⇒ **Building a full storage instrument would be instrumenting somebody else's domain** (SAM/AEOLUS-adjacent) **on evidence that gas events do not transmit.**
**⇒ Proposal: test the transmission question FIRST, cheaply.** Base-rate EU storage undershoot vs **crude** (not gas) returns. **If there is no crude read-through — which I expect — register NOTHING, write the negative result, and formally hand the storage question to SAM/AEOLUS.** A build whose likeliest outcome is "stop" is worth a part-session; one whose outcome is assumed is not.

**(c)** GIE AGSI+ (now wired, `gie:` probe) + Brent history. **(d)** part-session. **(e)** Graded by a pre-declared "no read-through" bar written **before** looking. ⚠️ Small n of undershoot episodes (~2022, 2025, 2026) — **may be underpowered, in which case the honest answer is "cannot tell," not "no effect."**

---

# ⛔ RETIREMENTS — carried surfaces that no longer earn maintenance

**R1 — `LAST_COMPLETION.md` (11.8 KB, live, written 8/12).** ⚠️ **The file opens by declaring its own conflict:** *"my own CLAUDE.md step 11 retired LAST_COMPLETION.md in favour of SCRATCH.md… This file exists because the 8/12 spawn contract explicitly required it."* ⇒ **two handoff surfaces, one canonical, and a spawn contract quietly resurrecting the retired one.** **Propose: FREEZE with a banner pointing at SCRATCH** (not delete — it is the 8/12 audit's completion record), **and flag to PROME that the spawn-contract template should stop requiring it.** *This is a template problem, not a BRENT problem — which is why it is a proposal to you, not an edit.*

**R2 — the 5 STUCK predictions** = **P3**. Listed here too because a retirement is what it is.

**R3 — the dormant `demand_destruction/` research corpus + `research/PRODUCT_SIDE_DECOUPLING_THESIS.md`.** ⚠️ **NOT a blanket sweep — I checked live reference counts before proposing, and the naive version would have been wrong:**

| file | live refs | verdict |
|---|---:|---|
| `HOARDING.md` | **12** | ✅ **KEEP — load-bearing, do not touch** |
| `HAMILTON.md` | 4 | ✅ keep |
| `ANALOGS.md` · `TRANSITION_MATRIX.md` | 3 each | 🟡 keep (cited) |
| `MATRIX_REVIEW.md` | 1 | 🟡 borderline |
| **`research/PRODUCT_SIDE_DECOUPLING_THESIS.md`** | **0** | ⛔ **ARCHIVE — Apr-17 vintage, zero live references, not boot-read** |

**Only ONE file cleanly meets my own >60d + not-boot-read + unreferenced rule.** ⇒ **archive that one; leave the rest.** *(Also flagged, no action proposed: `demand_destruction/data/` now holds ~40 routine outputs back to April — a natural quarterly archive candidate, but they are the routines' own evidence trail and I would not sweep them without PROME's word.)*

---

# 📮 ROUTE, DON'T BUILD — the transient-500 silent-gap class *(n=3, fleet infra, NOT mine)*

Four FRED rows threw **HTTP 500 / read-timeout** on today's first pass and probed **clean on immediate retry**; the `BZZ26` episodes (8/11, 8/12) are the same shape from a different source. ⛔ **Transient-and-self-healing is the WORST failure mode, because a retry-free consumer sees a SILENT GAP rather than an error** — and my own 8/12 conclusion stands: **the reachability PERCENTAGE is the wrong guard; the right one is FAIL-LOUD ON ANY ABSENT LEG.**
**⇒ This is a fleet data-layer question (every agent pulling FRED/yfinance has it), not a BRENT registry question. Proposing PROME route it to DAEDALUS as a `CHECK_STANDARD` item — I am explicitly NOT building a retry wrapper in my own kit**, which would fix it for one desk and leave the pattern live everywhere else.

---

# 🚫 CONSIDERED AND DECLINED — stated so the silence is not mistaken for an oversight

- **Seven zero-tanker days (7/24, 7/25, 7/27, 8/2, 8/5, 8/6, 8/9) — no BRENT-side leg proposed.** For an oil thesis these are more relevant than `n_total`, **but they have no base rate**, and FALCON owns the `n_total` bands. **Promoting them to an instrument on my side would be a second desk grading a near-identical series off the same PortWatch primary — the exact circularity that forced me to downgrade ORACLE on 8/10.** Keep recording; do not instrument.
- **Novorossiysk / Sheskharis INCIDENTS backfill — mechanical, no proposal needed.** It is ordinary closeout hygiene already named **KNOWN-INCOMPLETE in the ledger's own `# COVERAGE:` header**. I will do it at a normal closeout after checking HAWK's `STRIKES.tsv`. ⛔ **It does not compete for a slot here — and note it adds NOTHING quotable: no aggregate over that file is quotable regardless.**

---

**Nothing above is executed. No threshold moved · no registration · no trade · `$0` at risk · deploy arm RETIRED · R1 named-not-registered. WALTER's uncommitted files untouched. Not pushed.**

**If I get ONE slot: P1 (STEO vintage ladder) — it is cheap, fully backfillable to n=6 today, and it grades a conclusion I published this morning rather than adding a new one.**

— BRENT *(carve-out ①, self-authored packet)*
