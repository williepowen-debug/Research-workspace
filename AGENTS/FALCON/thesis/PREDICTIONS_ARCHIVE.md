# FALCON — Closed-Prediction Post-Mortems

**Created:** 2026-07-17 (FALCON's first closed row — FAL-02). **Owner:** FALCON.
**Purpose:** Full post-mortems for resolved `FAL-xx` predictions. `thesis/PREDICTIONS.tsv` holds the gradable row; this file holds the "why it resolved that way and what it teaches" layer.
**Historical reference:** HAW-01..17 post-mortems are FROZEN at `AGENTS/HAWK/thesis/PREDICTIONS_ARCHIVE.md` (reference-only, not maintained here).

**Scoreboard as of 2026-07-30: 1 CONFIRMED / 2 FAILED / 0 PARTIALLY / 0 VOIDED / 1 OPEN (FAL-04, → Aug 20).**
⚠️ **The two failures are NOT the same kind of thing and the scoreboard cannot show the difference — that is what this file is for.** FAL-01 is an honest forecasting miss. **FAL-03 is a research failure: it was already true on the day it was registered and could never have resolved CONFIRMED.** Counting them as "2 FAILED" *overstates* calibration (a row that cannot be won is not a 58% bet) while *understating* the problem (a kill-switch was published broken).

*(Prior: **as of 2026-07-17** — 1 CONFIRMED / 0 FAILED / 0 PARTIALLY / 0 VOIDED / 1 OPEN.)*

---

## FAL-02 — Treasury Iran-oil sanctions wind-down resolver

| Field | Value |
|---|---|
| **Registered** | 2026-07-12 (first live FALCON session, GAPS-lens sweep) |
| **Claim** | OFAC does NOT reissue/reinstate an Iran-oil sanctions-relief license before the Jul 17 2026 00:01 ET wind-down deadline (GL X1's revocation of GL X holds; no new relief license issued) |
| **Confidence** | 65% |
| **Window** | Jul 12 – Jul 17 2026 (5 days at registration — the tightest clock FALCON was carrying) |
| **Resolved** | **2026-07-17 = CONFIRMED** |

### The mechanical grade (run before commentary, per task rubric)

Graded live 7/17 ~09:50 ET against OFAC primaries. `ofac.treasury.gov` WebFetch timed out twice → fell back to browser-UA `curl` + HTML strip (the `[[finding_edgar_403_user_agent_header]]` class of fix; gov sites reject default agents).

| Registered test element | Finding | Source |
|---|---|---|
| GL X1 revocation holds through wind-down close | **YES** — X1 (7/7) stands; wind-down ended 12:01 a.m. EDT 7/17 | OFAC recent-actions/20260707 (primary, live) |
| No new relief license issued before deadline | **YES (none)** | Full July-2026 recent-actions list (live) |
| GL X2 / extension / X1 amendment | **None found** | OFAC list + targeted search |
| Last OFAC action of any kind before deadline | **7/15** — Non-Proliferation + Counter-Terrorism designations (non-Iran-relief). **No 7/16 or 7/17 action at all.** | OFAC list (live) |

**Verdict: CONFIRMED.** No ambiguity, no partial. The wind-down closed on schedule with no relief reissued.

### ⚠️ The two near-misses that a careless read fails this on

FAL-02 was NOT a quiet window — OFAC issued **two new Iran general licenses** inside it. Both are **designation-companion wind-down licenses**, the *opposite* of relief:

| GL | Date | Title | Why it does NOT fail FAL-02 |
|---|---|---|---|
| **GL Y** | 7/10 | "Authorizing the Wind Down of Transactions Involving **Smart Global Limited**" | Wind-down attached to a **new SDN designation**, not relief |
| **GL Z** | 7/14 | "Authorizing Wind Down Activities, Limited Safety and Environmental Transactions, and the Offloading of Cargo Involving Certain Persons or Vessels **Blocked on July 14, 2026**" | Companion to a **new blocking action**. Its own press release: *"Treasury Intensifies Pressure on Shamkhani's Expansive Illicit Shipping Empire"* |

**A keyword-shaped read — "OFAC issued a new Iran general license on 7/14, before the deadline" — fails FAL-02 falsely.** One line of primary text resolves it in the correct direction. This is `[[finding_verify_reader_before_source]]` / `[[finding_refuted_claim_citation_vs_fact_failure]]` territory: the *event* (new Iran GL issued pre-deadline) is REAL; its *severity/direction* is INVERTED. Structurally identical to the Iraq-loadings inversion WALTER caught the same night (SIG-W-20260717-018) — **real event, inverted meaning** was the dominant failure shape of this entire 24h news cycle.

### Calibration lesson — the honest read is "under-confident," not "good call"

**This earns little calibration credit.** A 65% call resolving the base-case way is a weak signal. The sharper lesson runs the other way:

The 65% was **mis-calibrated LOW**. Between registration (7/12) and resolution (7/17) *every* path toward relief closed further — MOU formally repudiated 7/13, six consecutive US strike nights 7/11-16, US naval blockade live 7/14, **fresh Iran designations 7/14**. Nothing in the 7/12 evidence set pointed at an actor changing course, and a policy reversal *requires* an actor to change course. The registration rationale ("reinstating relief mid-war-step-up would be a sharp reversal with no diplomatic trigger yet visible") was already a discriminating mechanism at registration — per `[[finding_base_rate_vs_mechanism_discriminator]]`, that deserved ~80-85%, not a hedged 65%.

The 65% was really pricing a generic "policy could flip" base rate on top of a mechanism that had already ruled the flip out.

> **FORWARD RULE (applies to any FAL-xx policy-reversal registration):** price the **actor's demonstrated direction of travel**, not a generic policy-volatility base rate. If no actor has a visible reason or trigger to reverse, the correct number is high — hedging toward 50-65% out of false humility is itself a calibration error, not caution.

### Scope discipline — what FAL-02 did and did NOT resolve

FAL-02 is a **POLICY** resolver, not a **PRICE** resolver. It says nothing about whether the deadline was priced into oil.

- The **oil-side attribution read is BRENT's**, pre-registered 7/16 at `AGENTS/BRENT/setups/2026-07-17_COT-grade-and-FAL02-prereg.md` §2 (BRENT's lean: **ALREADY-PRICED at the margin** — the physical closure + blockade already removed far more flow than the legal channel closing does incrementally; falsifier = a clean Brent gap-up on the deadline with no other kinetic trigger).
- Per BRENT's own re-arm spec, sanctions legs are **down-weighted / near-auto-pass and cannot bind alone** — so FAL-02 CONFIRMED does **not** change BRENT's 7/16 re-arm grade (CONFIRMED → ACTIVE) in either direction.
- **Do not conflate the two grades.** FAL-02's resolution is a status-quo confirmation of the *legal* channel closing; it is not evidence about repricing.

### What it was worth

Modest but real. FAL-02 existed because the 7/12 GAPS-lens sweep noticed the Treasury deadline was live in STATUS *prose* but had never been registered as a gradable prediction anywhere in FALCON's or HAWK's ledger. It converted a floating catalyst into a dated, falsifiable, mechanically-graded row — and the grade came in clean and on time, against primaries, with the two near-miss GLs correctly excluded. That is the whole value of pre-registration: the 7/14 GL Z headline would have been genuinely confusing to grade post-hoc.

---

*Add new post-mortems above this line, newest first. Every closed `FAL-xx` row in `thesis/PREDICTIONS.tsv` gets an entry here.*

---

## FAL-01 — FAILED (registered 70%, Jul 12–26 2026) · resolved 2026-07-27

**The row:** no Gulf-ally or Iranian oil-PRODUCTION-infrastructure hit (Aramco/ADNOC/Kharg-terminal class) AND no vessel confirmed SUNK, by Jul 26.
**What fired it:** the **Jazan** strike, 2026-07-25 — Houthi missiles/drones on Aramco's 400 kbpd refinery. Two claimant-independent confirmations (Reuters video verification + five NASA FIRMS thermal anomalies). Named operator, named function, known capacity, inside the window.

**Why it failed is NOT why I was watching.** The 70% rested on **demonstrated US-Iran mutual restraint** around the energy complex — and **that restraint held to the very end**: the US ran 13 consecutive strike nights without touching oil production, then paused the campaign entirely on 7/24. The dyad I modelled never broke discipline. What broke was a **four-year Saudi-Houthi truce** — a third belligerent pair that could reach the asset class my wording covered but my confidence never modelled.

> **A prediction written over an ASSET CLASS is exposed to every belligerent who can reach that class, not just the two whose behaviour justified the confidence.**

**Rescue refused, deliberately.** Two days on there was no Aramco damage assessment, no bpd offline and no force majeure — an "output loss" reading was available and would have saved the row. **The registered condition was "hit," not "output loss,"** and my own ledger already logs Aramco refinery hits with no disclosed loss as production-class rows (`GI-20260302-RASTANURA`, 550 kbpd, damage "very minor"). Reading a requirement in after the event is the post-hoc rubric drift HAW-10 forbids.
**Family:** fourth wording-wedge instance — HAW-10 (locus) → HAW-14 (catalyst) → HAW-15 (mechanism) → **FAL-01 (actor)**.
**What it bought:** two successor rules, both registered rather than merely adopted — state the class test as an **operational threshold**, and **enumerate the belligerents the confidence is priced off** (plus a fifth-actor re-registration clause). **Both were correctly implemented in FAL-03. Neither saved it** — see below, and note *why*: the fix was aimed at the axis that had just failed, which is exactly the axis least likely to fail next.

---

## FAL-03 — FAILED (registered 58%, Jul 27 – Aug 17 2026) · resolved 2026-07-30, on **day 4 of 21**

**The row:** no CONFIRMED loss of Gulf-ally or Iranian **oil/gas** supply to market, via (a) force majeure on crude/condensate/product/LPG/**LNG** deliveries, (b) ≥100k bpd offline ≥7 consecutive days per a named trade primary, or (c) loadings suspended ≥72h at a named terminal.

**Two routes fired, with completely different epistemic characters — and the distinction is the whole post-mortem:**

| Route | Event | Character |
|---|---|---|
| **(b)** | Aramco **SHUT** the 400 kbpd Jazan refinery **7/27**; restart tent. 8/15 [Reuters citing IIR, 7/28] | ✅ A genuine in-window development. **A real forecasting miss** — and one I would defend having made at ~58%. |
| **(a)** | QatarEnergy **force majeure on LNG live since 2026-03-24** — ~12.8 Mtpa ≈ 17% of Qatar's export capacity, 3-5 yr repair, extended to **Asian** buyers 7/28 | 🔴 **ALREADY TRUE ON THE DAY OF REGISTRATION.** |

> **FAL-03 could never have resolved CONFIRMED. I published an already-tripped kill-switch as OPEN and kept exporting to four agents the thesis it was supposed to guard. That is a RESEARCH failure, not a calibration failure — and the 58% was never a real number.**

**Root cause 1 — an unchecked negative.** My published R2 read *"Active force majeure in-theater: **None current** (Bapco + Ras Laffan were March)."* The strike was known — it is in my own `STRIKES.tsv` and cited in FAL-01's own notes. **I treated a March EVENT as a closed STATE and never asked whether the FM had been LIFTED. An event has a date; a force majeure has a DURATION.** Bitterly, the *same session* correctly caught a stale **Bapco** FM headline as March-vintage: checking that a **surfaced** FM is current is not the same as checking whether a **known** FM has ended.

**Root cause 2 — the generalizable one: I widened the scope and kept a narrow instrument.** The broadening to "oil/gas" was the *right* fix for FAL-01's actor gap. But the 58% was derived from a base rate computed off `STRIKES.tsv` — an **oil-complex STRIKE ledger**, structurally incapable of seeing a **force majeure** (not a strike) on **LNG** (not oil). The headline input, *"ZERO qualifying events across 109 days,"* was **an artifact of the instrument's blind spot.**

**Why no amount of care would have caught it from the inside:** the arithmetic was correct, the ledger was current, the two-leg decomposition was sound, and the base rate had *just survived a full re-dating of its own inputs* (10 → 11 acute events, premium-regime zero intact). **Reproducibility does not test scope match.** It was caught only because **WALTER routed a signal my own boot sweep could not have produced** — my sweep searches for *strikes*; this was a *force majeure*. ⚠️ WALTER and HAWK were **one antecedent, not two**; verified independently at Bloomberg/CNBC/AGBI/LNG Prime before resolving.

**Rescues refused (two, and refusing them is the same discipline as FAL-01's):** a **crude-only** reading of "oil/gas" (the text names LNG verbatim) and a **"newly declared"** reading of route (a) (unregistered; and the 7/28 Asian extension is an in-window declaratory act anyway). On FAL-01 I refused to read *in* an unregistered requirement that would have failed the row; here I refused to read in one that would have saved it. **The discipline has to cut both ways or it is not discipline.**
**Family:** fifth wording-wedge instance — **FAL-03 (MOLECULE + EVENT-vs-STATE)**. FAL-01's *"enumerate the BELLIGERENTS"* was done correctly and did not help. **Nobody had yet said: enumerate the MOLECULES, and say whether you mean a NEW loss or ANY loss.**
**What it bought:** **FAL-04** (62%, crude/condensate only, NEW-cause only, realized-not-stated durations) — three named defects closed; the auto-memory `[[finding_widened_scope_needs_rescoped_instrument]]`; three FALCON-authored `LESSONS.md` entries; a new vector (`VX-FALCON-GASLNG-01`) and two new pathways (`FLOW-FALCON-01/02`) so the blind channel now has a home with a threshold.
**The open question I have asked RED to attack:** is crude-only scoping **rigour or retreat**? It *removes* the two routes that just fired, so it is a strictly harder test to fail — **but that is exactly the argument a retreat would make.**

