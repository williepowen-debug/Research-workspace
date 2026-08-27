# BRENT SELF-AUDIT — canonical + load-bearing surfaces
**2026-08-12 Wed ~18:0x ET · PROME-directed, Will-facing · adversarial pass on my own files**

**Premise:** today I found **n=4 of one defect class** in six days and the **most extreme observation in my throughput record sitting one row outside the window I graded.** Neither was found by a check. This audit assumes there is more.
**Scope discipline:** everything ruled/retracted/packeted earlier today is **CLOSED and not re-litigated here.** This covers only what nobody had looked at.
**⛔ Zero capital, zero trades, zero thresholds moved or registered.**

---

## 0. COVERAGE DENOMINATOR — read this before the findings

**20 files/groups in scope · 11 systematically audited · 9 mechanically swept only or unread.**

### ✅ Systematically audited (11)
`STATUS.md` · `SCRATCH.md` · `CLAUDE.md` · `TRADE.md` · `NEXUS_BRIEF.md` · `thesis/THESIS.md` · `demand_destruction/TRACKER.md` · **`workbook/REGISTRY.tsv` (read in full, all 21 columns × every row incl. notes)** · `docket/CATALYSTS.tsv` (all 16 rows, date-checked) · `MEMORY.md` · `RULINGS.md` (swept + targeted reads)

### ⛔ NOT READ — listed with reason, because a coverage limit is a blocker not a footnote
| File | Size | Why not read | Risk of the gap |
|---|---|---|---|
| **`refinery_damage/INCIDENTS.tsv`** | 62 rows / 27KB | **Ran out of session. No sweep of any kind ran against it.** | 🔴 **The largest gap.** A live ledger I append to; it has a known **pending** row (Novorossiysk 8/11-12) and a documented double-count hazard (`bpd_offline_est=0` convention). **Unaudited.** |
| `thesis/CHANGELOG.md` | 764 ln / 115KB | Dead-path swept only; not read line-by-line | Append-only historical record — lowest actionability, but superseded-claim residue would live here |
| `thesis/PREDICTIONS.tsv` | 64 rows / 68KB | Crude-label swept only; the 5 known-unresolvable rows (BRT-07/12/16/17/21) not re-audited | Duplicates a known open item; low |
| `board_log.tsv` | 182 rows / 173KB | Not audited (I appended to it this session) | Append-only ledger; low |
| `LESSONS.md` + `workbook/LESSONS_INDEX.tsv` | 96 ln / 42KB | `lessons_check.py --prose` ran **clean (0 drift)** at boot, so mechanically covered — **but I did not read the prose** | Medium: the checker is deliberately narrow and does **not** semantically compare an `asserts` value to a paragraph |
| `setups/` (9 pre-8/12 files) | 10 files | Dead-path swept only | Mostly superseded prereg records; low |
| `SCHEDULED_RUNS.md` · `docket/FASTOW*.md` | 3 files | Swept only | Low |

**⚠️ Read the findings below as a LOWER BOUND.** They come from the 11 audited files.

---

## 1. FINDINGS — ranked by severity

### 🔴 F-1 — CONFIRMED — A live position's break-even is understated because the 8/7 retraction never reached the arithmetic that used it
**`TRADE.md:386` (mirrored `STATUS.md:52`) · owner: MINE · ✅ FIXED THIS SESSION**

The 8/7 "closes" `Brent $82.27 / WTI $77.08` were intraday prints, corrected 8/10 to settles `$83.55 / $78.18`. **The strike-through fix was applied four lines above this block. The derived arithmetic kept the bad input.**

| | published | correct | error |
|---|---:|---:|---|
| USO/Brent ratio | 1.4340 | **1.4121** | — |
| ratio drift vs 1.3966 @7/23 | +2.68% / 15d | **+1.11% / 15d** | **2.4× too fast** |
| USO $165 ⇒ Brent | ~$115.1 | **~$116.85** | understated **$1.79** |
| **break-even USO $153.65 ⇒ Brent** | **~$107.2** | **~$108.81** | **understated $1.67** |

**Downstream:** the live **USO Sep-18 150/165** spread needs Brent **~$1.67 further** than the card said to break even. **The error flattered the book** — it made the position look closer to paying off than it is.
> ⚑ **DELTA BASIS CORRECTED 2026-08-12 (PROME verification, and it runs AGAINST me).** I first reported **$1.61 / $1.75**, measured against the **rounded figures printed on the card** ($107.2 / $115.1). PROME reported **$1.67 / $1.79**, measured against **what the published ratio actually yields** ($107.1435 / $115.0581). **PROME's basis is the correct one and I have adopted it:** comparing to the rounded printed number **launders the card's own rounding into the delta.** *(The card printed `1.4340`; 117.98/82.27 is `1.434059`, i.e. `1.4341` — so the card was already rounded the wrong way.)* **⇒ the understatement was slightly LARGER than I self-reported.**
✅ **What survives, checked not assumed:** the ruling itself (*no Brent translation from a stored ratio*) is **strengthened** — this is a second, independent way the frozen number rotted. The **roll-yield diagnosis holds on corrected numbers**: corrected Brent−WTI is **$5.37**, still wider than PROME's $3.83 on 8/3 while the ratio rose anyway. Vehicle conclusion (USO HOLDS) never depended on this.
**Fix applied:** recomputed, superseded text preserved verbatim, **no strike/threshold/size moved.**
★ **Why it matters beyond the $1.67: this is the SAME bad print I already corrected once, publicly, on 8/10. My correction covered the display value and not the computation. `[[finding_verification_correction_downstream_propagation]]`**

### 🔴 F-2 — CONFIRMED — Two LIVE registry rows assert the same event on different instruments and disagree 5.1% of the time
**`workbook/REGISTRY.tsv` rows `MKT-BZ-F-ABOVE-100` and `FRED-DCOILBRENTEU-ABOVE-100` · owner: WILL to rule (registry change) · NOT edited**

Both `status=live`. One grades front-month **futures**, the other **dated spot**. Measured over **254 common sessions (1yr)**:

| Registered pair | disagree | rate | direction |
|---|---:|---:|---|
| **ABOVE-100** | **13 / 254** | **5.1%** | spot breached, futures not — **13 of 13** |
| **ABOVE-120** | **9 / 254** | **3.5%** | spot breached, futures not — 9 of 9 |
| ABOVE-140 | 0 / 254 | 0.0% | — |

> ⚑ **DENOMINATOR RECONCILED 2026-08-12 (PROME verification) — CITE THE COUNT, NOT THE RATE.** **PROME's numerators reproduce mine EXACTLY: 13 / 9 / 0, all one-directional ⇒ the disagreeing SET is agreed by both desks.** Only the denominator differs — **mine 254, PROME's 247**, so the rates read 5.1%/3.5% vs 5.3%/3.6%. Mine is the **strict intersection of both series' printing days** (FRED 260 valued rows ∩ 259 `BZ=F` sessions; 5 futures-only days incl. 8/12, 6 FRED-only days). **I cannot see PROME's construction, so I am NOT claiming its 247 is wrong** — `[[finding_reconcile_mismatch_does_not_say_which_side_is_wrong]]`. ⇒ **This finding goes to Will as a COUNT with its denominator stated (13 of 254), never as a bare percentage.** The finding is unaffected either way.

**Nothing in the registry says which governs.** A boot grading run can therefore report "Brent >$100 BREACHED" and "Brent >$100 NOT BREACHED" in the same pass, and on 7/24 it would have.
⛔ **This is TODAY'S OWN RULING'S BLIND SPOT.** I ruled the instrument basis per surface for prose, packets and the tape — **and never opened the machine registry.** The defect I spent the session on was sitting inside the file that is supposed to be the single source of machine truth.
**Recommendation to Will (not applied):** either mark one basis authoritative per level and demote the other to `informational`, or rename both to carry their basis (`BRENT-FUT-ABOVE-100` / `BRENT-SPOT-ABOVE-100`) so a grader can never present them as one test.

### 🟠 F-3 — CONFIRMED — Six registry thresholds are keyed to a CONTINUOUS series that rolls contracts underneath them
**`workbook/REGISTRY.tsv`: `MKT-BZ-F-ABOVE-140/120/100`, `MKT-BZ-F-BELOW-85/75/70` · owner: WILL to rule · NOT edited**

`BZ=F` is the continuous front-month. Measured across its Sep-26 → Oct-26 roll:

| date | BZ=F | BZV26 | gap |
|---|---:|---:|---:|
| 2026-07-29 | 90.74 | 88.09 | **2.65** |
| 2026-07-31 | 90.12 | 87.93 | **2.19** |
| **2026-08-03** | 83.77 | 83.77 | **0.00 ← rolled** |

**⇒ The registered instrument stepped ~$2.2 from the ROLL ALONE, with no price move.** On `MKT-BZ-F-BELOW-85` that is **2.6% of the line** — a roll can trip or un-trip a registered threshold on zero market movement, and nothing in the row records the roll date.
**Recommendation (not applied):** either pin threshold rows to a named contract with a documented roll rule, or add a roll-adjustment note to the row. **This is the same class as F-2 and today's ruling; it just lives in the machine layer.**

### 🟠 F-4 — CONFIRMED — My single thesis-invalidation falsifier cannot be acted on inside the window that matters
**`KILL-LEG2-TRANSIT` (`status=live`) · owner: mine to re-spec, WILL to rule any budget change · NOT edited**

Validity and executability are orthogonal axes and I had only ever tested validity. The falsifier — *transits >35/day ×2 consecutive ⇒ thesis FALSIFIED* — is graded off IMF PortWatch, whose **publication lag I measured at 3–8 days** (8 days at my 8/10 boot; 3 days today).
**⇒ If Hormuz genuinely reopened today, my own thesis-kill signal would reach me in 3–8 days.** The instrument is fine; the **latency versus the decision** is not. The positions it governs are dated options.
**This is not a reason to weaken the falsifier** — it is a reason to say plainly that it is a **post-hoc confirmer, not a live exit trigger**, and that any exit inside the lag window must run on something else (the prompt premium adopted today publishes daily and is a candidate — **not proposed as a trigger here; it would need its own N1 build**).

### 🟡 F-5 — CONFIRMED — 11 stale provenance pointers on live surfaces
**`TRADE.md` ×10, `RULINGS.md` ×2, `TRACKER.md` ×1, `REGISTRY.tsv` ×3 · owner: MINE · ✅ FIXED**
Eight distinct packets cited as `outbox/X.md` had been archived to `outbox/delivered/X.md`. Every citation was a dead link — a reader chasing provenance on the arm adjudication, the Stage-A proposal or the COT verdict got nothing. **All repointed and verified to resolve; REGISTRY re-parsed clean (21 cols uniform).** `[[finding_dead_path_regrows_unless_senders_repointed]]`

### 🟡 F-6 — CONFIRMED — The catalyst retention rule has no enforcement and silently stopped running
**`docket/CATALYSTS.tsv` · owner: MINE · REPORTED, deliberately NOT pruned**
My closeout protocol says *"prune fired rows past 1-week retention."* **2 of 16 rows are past it** — 8/03 (9d) and 8/05 (7d), both fired **and** graded. The 8/11 STEO row (1d) is correctly retained as my declared open item.
**Not pruned on purpose:** pruning is a deletion and the finding is not the tidiness — it is that **a rule with no check quietly stopped executing for two sessions.** Same shape as the guards I have been adding all week.

### 🟡 F-7 — MEASURED — 54 of 150 crude figures on live surfaces still lack an instrument label
**Owner: MINE, mostly acceptable · counts reported rather than mass-edited**

Answering PROME's question directly — **how many violations of today's own ban remain on my files:**

| | count | share |
|---|---:|---:|
| Prices bound to "Brent"/"WTI" on 15 live surfaces | **150** | — |
| Carry an instrument label | **96** | **64%** |
| Carry only the word "close" *(weak — "close" is exactly what bit me 4×)* | **10** | 7% |
| **Fully bare** | **44** | **29%** |

**By file (bare + close-only):** `TRACKER.md` **36** · `TRADE.md` 8 · `STATUS.md` 7 · `PREDICTIONS.tsv` 2 · `THESIS.md` 1.
⚠️ **36 of the 54 are inside TRACKER's dated historical ladder and snapshot blocks** (Apr–Aug weekly rows), which my own canon permits as dated records — **I am not mass-editing history.** ⛔ **But the honest read is that "bare Brent $X is banned" is currently true of 64% of my live surfaces, not 100%**, and the ban has no checker. **Recommendation: a `basis_check` that scans only NON-dated blocks — offered as a finding, not built** (retirement ratchet: it would need to name what it supersedes, and I would rather Will/PROME decide whether the kit needs a tenth script).

---

## 2. CHECKS THAT PASSED — reported plainly, because a clean result is a result

| # | Check | Result |
|---|---|---|
| **C-1** | **Dead things carried as live** — is the RETIRED arm or R1 armable anywhere? | ✅ **CLEAN.** All three `GATE-V3-*` rows are `status=retired`. **R1 (OVX >68.97) appears ONLY inside the notes field of retired rows, every time explicitly labelled "named-not-registered"** with the re-arm-requires-fresh-Will-ruling text attached. `STAGE-A-AIS`, `HY-ENERGY-OAS`, `WAR-RISK-HALVES`, `SPR-OPERATIONAL-400` all correctly `retired`. **No live-vocabulary residue found outside dated historical blocks.** |
| **C-2** | **★ The COMPLETE-check** — asserted side effects verified at the TARGET artifact | ✅ **CLEAN — 9 candidates, 0 confirmed defects.** "packet sent to RED" ✅ exists · "routed to FALCON" ×2 ✅ exists · "routed to TERRY" ✅ (5 BRENT packets in TERRY's inbox) · 2 hits were prose *about* a past defect, not claims. **1 unverifiable by me:** *"two spec findings routed to Will"* (`STATUS.md:59`) — Will is off-repo, so I record it as **unverifiable, not verified.** ⚠️ **Caveat: my search vocabulary was 7 phrases. A claim phrased differently would not have been caught.** |
| **C-3** | `INSTRUMENTS.tsv` flagged as a dead path | ✅ **FALSE POSITIVE.** `RULINGS.md:134` correctly *documents* that it was absorbed into `REGISTRY.tsv` — an extend-don't-add record, not a pointer. |
| **C-4** | Dead-path sweep, 47 raw hits | ✅ **46 of 47 resolvable** once searched properly (bare basenames + `outbox/delivered/`). Only F-5 was real. **A grep hit is a candidate until read — my own first pass was 47-for-47 candidates and 8 real.** |
| **C-5** | Registry schema integrity | ✅ **21 columns uniform across every row**, before and after my edit. |

---

## 3. WHAT I FIXED vs WHAT I STOPPED ON

**✅ Fixed (mechanical, unambiguously mine):** F-1 arithmetic (superseded text preserved verbatim; no strike/threshold/size moved) · F-5 eleven pointers repointed and verified.
**⛔ Stopped and reported, did not resolve in my own favour:** F-2 and F-3 are **registry changes → Will's** · F-4 is a **falsifier re-spec → needs a ruling, and I will not quietly weaken my own kill-switch** · F-6 is a **deletion** · F-7 is a **mass edit of dated history plus a possible new script.**

## 4. CONFIDENCE

**All 7 findings are CONFIRMED, not candidates** — each was read in context and, where numeric, re-derived from a primary this session (FRED full series, CFTC, yfinance per-contract, PortWatch). **F-2 and F-3 rest on measured disagreement/roll rates over 254 sessions, not on inspection.**
**The load-bearing caveat is coverage, not confidence:** the findings come from **11 of 20** in-scope files. **`refinery_damage/INCIDENTS.tsv` received no sweep of any kind** and is the gap I would close first.

## 5. THE PATTERN ACROSS F-1, F-2 AND F-3

All three are **one defect wearing three costumes: a number whose BASIS moved while its label stayed still.** F-1 is a retracted input surviving inside a derived figure; F-2 is two bases registered as one event; F-3 is a basis that shifts on a roll.
★ **And the uncomfortable part: I spent this entire session ruling on exactly this, wrote the canon, packeted seven desks — and all three of these were sitting in my own files while I did it.** ⇒ **A ruling changes what I write next. It does not touch what is already written, and nothing in my kit scans for it.** That, not any individual number, is what I would want Will to take from this audit.
