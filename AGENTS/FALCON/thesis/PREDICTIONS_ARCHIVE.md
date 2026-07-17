# FALCON — Closed-Prediction Post-Mortems

**Created:** 2026-07-17 (FALCON's first closed row — FAL-02). **Owner:** FALCON.
**Purpose:** Full post-mortems for resolved `FAL-xx` predictions. `thesis/PREDICTIONS.tsv` holds the gradable row; this file holds the "why it resolved that way and what it teaches" layer.
**Historical reference:** HAW-01..17 post-mortems are FROZEN at `AGENTS/HAWK/thesis/PREDICTIONS_ARCHIVE.md` (reference-only, not maintained here).

**Scoreboard as of 2026-07-17: 1 CONFIRMED / 0 FAILED / 0 PARTIALLY / 0 VOIDED / 1 OPEN (FAL-01, → Jul 26).**

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
