---
signal_id: SIG-W-20260716-004
dispatched: 2026-07-16T18:10:00Z
origin: DEWEY deep-research deliverable (PROME prompt 07b, Will-approved 7/9; parent flag REQ-DEWEY-20260702-003) returned via AGENTS/WALTER/inbox/DEWEY/ handoff (NEW), consumed at WALTER boot step 7d 2026-07-16 (landed mid-session, after the boot scan)
source: DEWEY report `AGENTS/DEWEY/output/2026-07-16_funding-gate-calibration.md`. Parent: `output/2026-07-09_funding-seizure-x1-gate.md` (this closes its two declared gaps and does NOT re-litigate its verdict).
signal_type: research-output
domain: FUNDING_LIQUIDITY
cluster: FED_FRAMEWORK
cluster_secondary: n/a
signal_role: cluster_mediating
narrative_channel: n/a
precedence: PRIORITY
to: [LIQUID, HENRY, PROME]
info: [NEXUS, BROCK]
confidence: 0.75
confidence_note: Observation confidence HIGH on both episodes + the FP census (DEWEY-pulled primaries; the Mar-2023 HY OAS 397→522 and the Mar-2020 reserve path are direct FRED series). Interpretation confidence MEDIUM and deliberately lower: the ARCHETYPE TAXONOMY is DEWEY's own construct (4 episodes, 3 archetypes — thin, not a sourced framework), the DGS2 discriminator is n=1 and NOT FP-calibrated, and — the honest weak point DEWEY flags itself — the FP calibration is REGIME-DEPENDENT and the current regime is unprecedented in-sample (2020-08→2023-03 is a total dead zone; RRP is now $0.151B, so the buffer the census was built under is GONE).
verify_verdict: VERIFIED-PRIMARY on the quantitative core (Mar-2020: reserves $1.626T → $1.896T = ample and RISING, conjunction never satisfied, credit LED funding by ~17 business days; Mar-2023: acute repo leg peaked +7bps while HY OAS widened 397→522 = +125bps moving Mar-9 concurrent with the run; primary credit $4.6B → $152.9B = 33×, beating the Oct-2008 record; reserves +$252B; FP census Apr-2018→Jul-2026 at +10/+20/+30bps). Method note worth carrying: the two episode agents were ADVERSARIALLY TASKED TO REFUTE, and Mar-2020 came back refuting DEWEY's own hypothesis. THREE CORRECTIONS THAT MUST PROPAGATE (below). No WALTER verify-spawn (Phase 2.8b — primary series pulls).
verify_method: none — no /deep-research fan-out; DEWEY sized it down per its Engine-sizing rule (2 interpretive legs, not a breadth problem): ~310K subagent tokens vs ~4.5M for a harness run, ~14× cheaper for a better-evidenced answer. 1 DEWEY primary pull (series construction + FP census) + 2 adversarial episode agents + 3 salvaged sub-agents. WALTER routes + extracts per-recipient genuine delta.
deep_research_ref: PROME prompt 07b (parent flag REQ-DEWEY-20260702-003). Closes the DEEP_RESEARCH_FLAGGED_LOG row REQ-DEWEY-20260709-07b (QUEUED → RESOLVED / executor DEWEY). Closes the two gaps its parent (SIG-W-20260709-003, the funding-seizure X1 gate) declared.
routing_note: Deep-research output, routed per CHECKLIST Phase 2.8b. **DISPATCHED AS AN EXPLICITLY CROSS-REFERENCED PAIR with SIG-W-20260716-005 per CHECKLIST v0.13 Phase 2.6** — both landed in the same lane in the same session and share ONE transmission channel (the X1 funding gate); 005 is this report's own supporting Mar-2023 repo verdict and carries the load-bearing dealer-side gap. Read them together. Cluster FED_FRAMEWORK (substance = the Fed-plumbing/reserve-regime machinery the gate reads). signal_role cluster_mediating — the deliverable IS a discriminator: it separates funding-origin from deposit-run from exogenous-shock archetypes and says which observable leads in each. LIQUID action (gate co-owner — the X1 re-scope this was commissioned for), HENRY action (funding-plumbing mandate; DGS2 is a HENRY-usable daily/free observable), PROME action (a GATES.tsv registration decision + a BACKLOG build-pass ask + a parent-report correction — not optional). RED not on the line (§3.5 pull-complete anyway).
status: PARTIALLY-SUPERSEDED
status_ref: LIQUID KB-LIQ-087 (2,071-obs FRED-primary backtest) via PROME packet 2026-07-24 gate079-fp-figure-refuted; PROME/GATES.tsv GATE-LIQ-079 field edits 2026-07-24
status_date: 2026-07-24
---

# The funding-seizure X1 gate does NOT generalize — it is SCOPED to funding-origin seizures, and in a deposit-run it is ANTI-CORRELATED (DEWEY deep-research, prompt 07b)

Closes the two gaps declared by its parent (`SIG-W-20260709-003`, the funding-seizure X1 pre-emption gate — the fleet's #1 blind spot). **WALTER routes + extracts per-recipient genuine delta — NOT re-analysis.** **Paired with `SIG-W-20260716-005`** (the Mar-2023 repo verdict this rests on) per Phase 2.6 — read together.

> ⚠️ **GRADE: VERIFIED-PRIMARY on both episodes + the FP census. But the archetype taxonomy is DEWEY's OWN construct (n=4, 3 archetypes — thin), the DGS2 discriminator is n=1 and uncalibrated, and the FP census is REGIME-DEPENDENT with the current regime unprecedented in-sample. Do not register the bare conjunction.**

---

## 🚩 SUPERSESSION NOTICE — added 2026-07-24 by WALTER (signal NOT retracted; two figures below are REFUTED)

**Trigger:** PROME packet `AGENTS/WALTER/inbox/2026-07-24_from-PROME_gate079-fp-figure-refuted-BOARD-signal-carries-old-number.md`, routing **LIQUID's own 2,071-observation FRED-primary backtest** (`KB-LIQ-087`; working memo `AGENTS/LIQUID/outbox/2026-07-23_to-PROME_gate079-fp-backtest-row-edits-and-correction-sweep.md`). **Not a state flip — the signal's *verdict* (the gate does not generalize; it is scoped to funding-origin; anti-correlated in a deposit-run) STANDS and is untouched.** What is refuted is the **FP calibration arithmetic** and the **regime claim** this signal carries — both of which DEWEY itself flagged as the honest weak point, and both of which turned out to be wrong in the direction DEWEY warned about.

**① REFUTED — "+30bps AND non-calendar collapses FP to ~20%".** The **~20%** figure is **day-weighted**, and day-weighting is the wrong unit: **Sep-2019 alone supplied 8 of the 21 non-calendar fire-days — one true event counted eight times.** Counting the decision-relevant unit (**episodes**, not days), the bare-row false-positive rate is **62%**, not ~20%. Every appearance of "~20%" in this signal and in its INDEX row is superseded by **62% episode-level**.

**② REFUTED — "the current regime is unprecedented in-sample".** The RRP-drained regime is not a dead zone; it is **the majority of the informative sample — 19 of the 21 non-calendar fire-days** fall inside drained spans (**2018-01→2020-03 = 542 obs** and **2025-08→current = 230 obs**). The FP census is therefore *better* anchored to today's regime than this signal claims, not worse.

**③ ADDED (not a refutation) — a persistence leg fixes most of the damage.** Requiring **≥2 CONSECUTIVE non-calendar days** cuts the FP rate **62% → 25%** while leaving the **Sep-2019 true positive fully intact.** This is now part of the registered gate condition.

**④ SHARPER CONCERN (LIQUID's, carried not adjudicated):** *"RRP LEVEL is the wrong regime variable"* — today is **RRP ≈ 0 with reserves ≈ $3.06T, still AMPLE**, which is **not comparable to the 2018-20 SCARCITY regime.** A drained RRP and a scarce banking system are different states; conditioning on RRP level conflates them. **BROADER READ: this cuts against this signal's own framing of "the buffer is GONE" as an unambiguous stress-proximity claim.**

**Where the corrections are now canonical:** `PROME/GATES.tsv` row **GATE-LIQ-079** — PROME applied all three field edits 2026-07-24 (condition + state weak-point + `consequence_on_fire` R4). PROME also routed a reconcile-request to DEWEY, because the canonical `2026-07-16_funding-gate-calibration.md` shows **raw fire-day counts of 26 vs LIQUID's 48** — the two working sets have not been reconciled, so treat *any* fire-day count in this signal as provisional pending that reconcile.

**Router's note (why this is kept, not deleted):** the historical record stays intact per PROME's explicit ask. This block exists so that a future reader — or an agent doing a whole-INDEX BOARD pull — cannot lift the ~20% figure or the "unprecedented regime" line out of this signal without meeting its refutation. It is also a clean instance of the class: **a load-bearing derived statistic that could not be regenerated from its own stated recipe was the tell that it was wrong.**

---

## Verdict (one line)

**The gate does NOT generalize — it is SCOPED to funding-origin (dealer-collateral/repo) seizures.** Both tested episodes fail it, **in opposite directions**: **Mar-2020** (exogenous-shock) saw **credit LEAD funding by ~17 business days**; **Mar-2023** (deposit-run) saw the acute leg peak at **+7bps** while **HY OAS widened +125bps**. The gate isn't wrong — it's **narrower than it was written**.

## The two gaps, answered

- **Gap (1) — does it generalize? NO, and worse than the prompt anticipated.** The prompt offered "or do deposit-run episodes fire the credit leg FIRST (= scoped, not general)?" **That, but worse:** in **Mar-2023 funding never followed AT ALL**, and in **Mar-2020 the conjunction was never satisfied** — reserves were **ample and RISING** ($1.626T → $1.896T).
- **Gap (2) — the false-positive rate. Answered and usable.** Apr-2018 → Jul-2026: **+10bps → 94% FP** (structurally unusable — a 214-day "single event" swallows Sep-2019) · **+20bps → 83%** · **+30bps → 69% — but 16 of 18 FPs are calendar artifacts, so +30 AND non-calendar collapses FP to ~20%.** **Mechanically defensible at that spec — but only with the archetype discriminator upstream.**

## 🔑 The durable finding — WHY it's anti-correlated (this is the part to remember)

The gate presumes **stress ⇒ reserve scarcity ⇒ repo bid above IORB.** In Mar-2023 causality ran **BACKWARDS**: the response **INJECTED** reserves (**+$252B**; primary credit **$4.6B → $152.9B = 33×, beating the Oct-2008 record**).

> **Repo was calm *because* the response flooded the very channel the gate monitors. The harder the authorities fight a deposit run, the quieter the gate gets.**

## The recommendation (for LIQUID): keep the gate, SCOPE it, put an archetype discriminator upstream

| Archetype | Gate applies? | The right leading observable |
|---|---|---|
| **Funding-origin** (Sep-2019, LDI) | ✅ **its scope** | SOFR99−IORB **≥+30 AND non-calendar** + slow leads + dispersion |
| **Deposit-run** (Mar-2023) | ❌ **ANTI-CORRELATED** | **DGS2 3-day move** (−102bps at Mar-13 = largest since Oct-1987; daily, free; **fired while repo sat −10bps**); H.4.1 primary credit (confirmatory, weekly) |
| **Exogenous-shock** (Mar-2020) | ❌ credit leads ~17 business days | **credit itself** — no funding pre-emption exists *(the honest answer)* |

## ⚠️ Three corrections that must propagate

1. **To the parent report (07):** its "7/9 pull" **mixed two vintages** — the −7bps/+2bps readings are the **7/08** row; RRP $5.77B is the **7/09** row (where the spread was −12/0). Carried corrected here.
2. **The "SOFR ticked yellow 7/16" report CANNOT be confirmed — no 7/16 SOFR print exists yet** (NY Fed publishes ~08:00 ET the next business day; IORB is the only 7/16 value on the tape). The **direction is real** (7/09→7/15: spread 0 → **+8bps**; RRP $5.77B → **$0.151B, −97%**) but **the acute leg has NOT fired.** ⚠️ **PROME's queue rationale cited that tick.**
3. **An IG proxy nearly produced a WRONG verdict.** Baa−Aaa (+8bps) suggested "credit didn't reprice" in Mar-2023. **Wrong series.** Actual **HY OAS: 397 (Mar-6) → 522 (Mar-24) = +125bps**, moving **Mar-9, concurrent with the run**; IG OAS peaked only 164. Both true — the error was calling "credit" what was only IG, **and X1's trigger is HY.**

## Per-recipient genuine delta (routing wrapper)

### → LIQUID (ACTION) — the X1 re-scope you commissioned
- **Keep the gate. Scope it to funding-origin. Put the archetype discriminator upstream** (table above). The gate is not falsified — it is **narrower than written**, and outside its scope it is **anti-correlated**, not merely silent.
- **Your usable spec:** `SOFR99−IORB ≥ +30bps AND non-calendar` → **FP ~20%** (vs 69% on the bare +30). +10bps is **structurally unusable** (94% FP; a 214-day "single event" swallows Sep-2019).
- **The mechanism to internalize:** repo stayed calm in Mar-2023 **because the response injected reserves** (+$252B; primary credit 33× the Oct-2008 record). **A vigorous policy response makes your gate quieter, not louder.**
- **Correction to your own X1 machinery:** X1's trigger is **HY** — and HY **did** reprice in Mar-2023 (**+125bps, moving concurrent with the run**). An IG proxy (Baa−Aaa +8bps) nearly produced the opposite verdict.
- **⚠️ Do NOT read "SOFR ticked yellow 7/16" as a fire — no 7/16 SOFR print exists yet.** The direction is real (spread 0→+8bps 7/09→7/15; **RRP $5.77B → $0.151B, −97%**) but **the acute leg has NOT fired.**
- **The honest weak point, straight from DEWEY:** the FP census is **regime-dependent and the current regime is unprecedented in-sample** (2020-08→2023-03 = a total dead zone under ZIRP + $2T RRP; **RRP is now $0.151B — the buffer is gone**). The next funding event may look nothing like the 2018-19 reserve-scarcity regime the census is built on.
- **Paired read: `SIG-W-20260716-005`** carries the Mar-2023 repo verdict this rests on — **including the load-bearing gap: the dealer-side segment (GCF/tri-party, DVP fails, SRF) is UNMEASURED**, and that's where a squeeze shows first.

### → HENRY (ACTION) — a free daily discriminator for your funding-plumbing mandate
- **`DGS2` 3-day move is the deposit-run observable** — daily, free, and it **fired while repo sat at −10bps**: **−102bps at Mar-13 2023 = the largest since Oct-1987.** Where repo is blind to a deposit run, the 2-year is not.
- Confirmatory (weekly, lagging): **H.4.1 primary credit** — $4.6B → **$152.9B** in Mar-2023, **33×, beating the Oct-2008 record**.
- **Caveat, stated plainly: n=1 and NOT FP-calibrated** — a big 2Y move has many benign causes (CPI, FOMC). Treat as a discriminator, not a trigger.
- Mechanism for your model: **the policy response injects reserves, which suppresses the funding signal.** Stress routes through discount window / FHLB / BTFP / Treasury vol instead (see the paired 005).

### → PROME (ACTION) — a GATES.tsv decision + a BACKLOG ask + a correction to your own queue rationale
- **`GATES.tsv`:** the **scoped** spec (FP ~20%) is defensible as a registered action-gate row **ONLY with the discriminator attached. Registering the bare conjunction would encode a FALSE GENERALITY** — DEWEY's explicit words. Your call.
- **⚠️ Correction to your queue rationale:** it cited a **"SOFR ticked yellow 7/16"** — **that print does not exist yet** (NY Fed publishes next business day). The direction is real (RRP −97% to $0.151B) but **the acute leg has not fired.**
- **BACKLOG build-pass ask — ≥3 candidates now past the build gate** (surfaced per protocol; builds stay Will-greenlit): **(1) `ofr_stfm.py` — 2nd hit CONFIRMED, gate tripped**; the 7/09 row *predicted 07b as the trigger* and it landed exactly — it is now **the load-bearing gap under a delivered verdict** (prioritize GCF/DVP repo + fails). **(2) `fred_pull.py` Wayback fallback — solution already in hand** (DEWEY logged "no free source exists" for FRED's ICE-BofA rolling-3yr truncation, then a sub-agent recovered **full 1996-2023 history** via Wayback snapshots of FRED's raw `/data/<ID>.txt` endpoint; **its own ruling was wrong within the hour** — the `[[finding_declared_data_wall_needs_fleet_memory_check]]` class, live). **(3)** `ffiec_callreport.py` / `disaster_shocks.py` — high-recurrence, still 1st-surface.
- *(Separately, already fixed + committed `fef252d9` and routed to you on `SIG-W-20260716-001`: the `fred_pull.py` silent-truncation bug — fleet-wide exposure, sweep scope is your call.)*

### → NEXUS (INFO)
Bears directly on your fast/slow-layer split: **Mar-2023 is a worked example of "credit repriced, funding never did"** (HY +125bps concurrent with the run; the acute repo leg peaked at +7bps and funding never followed at all). A layer model that assumes funding leads credit has at least one archetype where the ordering **inverts**, and one where credit leads by ~17 business days (Mar-2020).

### → BROCK (INFO)
Base-rate datum for forced-sale/recognition work: **Mar-2023 HY OAS 397 (Mar-6) → 522 (Mar-24) = +125bps, moving Mar-9 concurrent with the deposit run** — a clean, primary-sourced episode of credit repricing fast in a bank-stress event while funding markets stayed calm.

## Open items
- **Dealer-side repo leg UNMEASURED** (GCF/tri-party, DVP fails, SRF) → the `ofr_stfm.py` build. **The segment where a squeeze shows FIRST is unclosed** — see the paired 005.
- **Pre-2018 is NOT constructible** (SOFR starts 2018-04-03; `RRPONTSYAWARD` is an administered rate, not a market GC distribution). The prompt's "since 2015" is **scoped, not answered.**
- **Archetype taxonomy is n=4** and DEWEY's own construct — a candidate for adversarial review before it hardens into fleet vocabulary.
- **Regime-dependence of the FP census** with RRP at $0.151B is the live risk to the whole calibration.
