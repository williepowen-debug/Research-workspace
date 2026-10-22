> **🟢 LIVE — UNFROZEN 2026-10-22** (D:L793 item 5). The 7/04 freeze condition was "broker/FORGE reconcile required before unfreezing"; that was met (DAEDALUS dates it 8/02, and the latest reconcile is ANVIL's 10/22 pass on Will's 11:01 ET Fidelity capture, `FORGE/STATUS.md` OZK row). The sections under "Entry rationale" and "Anti-trade" below are kept as the **historical** entry record (Mar–Jul 2026) — they are not current views. Current state is §Now. *(Freeze history: DAEDALUS TRADE-staleness sweep, PAT-025, Will-approved 7/04; banner re-worded 7/22.)*

# OZK TRADE.md

**Purpose:** Durable "why-we-entered" conviction record + anti-trade caution. Operational state lives elsewhere.

## Now (2026-10-22)

| Item | State |
|---|---|
| Book | Nov-20 $40P ×4, mark $0.05 / value $20 at 10/22 11:01 ET (FORGE reconcile). Will approved a sell 10/14 (WQ-428); not evidenced in the 10/22 capture. **Will manages his own expiries — this desk sends no expiry or sell reminders** (USER.md 10/20). Detail → `POSITIONS.md` |
| Thesis | RESERVOIR v1.7, conviction 🟡 LOW; scenarios Bear 20 / Base 50 / Bull 28 / Tail 2, EV $44.41 (P-OZK-8, 10/22) → `THESIS.md`, `SCENARIOS.md` |
| ⛔ Fence | D1 / OZK-salvage RULED-CLOSED — no re-present, no successor. Any OZK expression is a **new** trade |
| Candidate ideas on file | **None at 10/22.** At LOW conviction with live $49.46 (12:24 ET) ≈11% above the $44.41 EV, the desk has no idea it would bring; the gap alone is not a trigger |

## Candidate-idea route → TERRY (USER.md 2026-10-20, "we can loosen rules for trade ideas")

This desk **supplies evidence; TERRY constructs; Will approves every trade (root rule #5).** When the desk has an idea, it writes one packet to `AGENTS/TERRY/inbox/` (`YYYY-MM-DD_from-OZK_idea-<slug>.md`, carve-out ①: the desk commits its own packet) carrying:

| Field | Content |
|---|---|
| Label | **NOT-FIRED** or **FIRED** — whether the named trigger has actually printed |
| Trigger | The exact condition, its source and today's reading in figures (e.g. "THESIS invalidation 7 reversal: an OREO sale at <80% of 9/30 carrying — not printed at 10/22") |
| Direction / instrument idea | Plain words; strikes and expiries are TERRY's to build |
| Size and risk | In dollars, against the $500/card and X1 defaults (going past them is Will's choice per card) |
| What kills it | The figure that would make it wrong |

**Triggers that would generate an idea** (none fired at 10/22): the v1.7 reversal triggers (OREO sale well below carrying · SM → classified in the 10-Q · RaDD reserve/readvance · `RIAD5409` charging off again) on the bear side; THESIS invalidation 6 + 7 firing on the other side (the case for no OZK short at all). Price bands <$45 / <$40 page REGINALD + PROME; they are signals, not ideas.

**Operational docs:** `STATUS.md` (positions + thresholds) · `POSITIONS.md` (broker-confirmed lines) · `archive/THREAD3_ROLL_MATH.md` (May 8 roll decision — retired 2026-07-06) · `IQHQ_PLAYBOOK.md` (Aug scenarios) · `Q1_2026_ANALYSIS.md` (Apr 21 print synthesis)

---

## Frame

Every OZK trade is a bet on the core convergence: ~~hidden CRE (MI3 37.6% — worst in coverage)~~ + single-sponsor concentration (11 tracked problem credits, $719M) + private-credit deterioration (IQHQ/Bluerock stack) → credit recognition event. Two discrete 2026 catalysts: **IQHQ RaDD maturity (Aug 2026)** and **$350M sub notes reprice (Oct 1, 2026)**. ~~RESERVOIR v1.3.~~

> ⚠️ **[2026-08-28 sweep — two dead tokens struck in the line above; the rest of this doc is a FROZEN entry-rationale record and is deliberately NOT rewritten.]**
> **(1) `MI3 37.6% / "worst in coverage"` is RETRACTED — both halves**, on four independent paths; live **9.35% [Q2-26]**, rank **5th of 14**, and "worst" formally retracted by the screen's owner (REGINALD, 8/13). Full retraction → `LESSONS.md` §Hidden CRE Methodology · `CALL_REPORT_2026Q2_LOG.md` §3. **This was the first leg of the convergence bet and it did not survive contact with the primary** — that is a fact about the entry rationale, which is why it is struck here rather than deleted. ⛔ **Scope fence: MI3 is CRE NOT secured by real estate. RESG, IQHQ and every secured book are untouched.**
> **(2) Successor pillar (Will-ruled 2026-08-23, verbatim "approved"):** the ~**$430–490M debt-on-debt / note-assignment book** — two independent filings, **charging off in H1-26** (`RIAD5409` $42,437K, first nonzero in 18 quarters). Adopted as the pillar's **SUBJECT, not as a graded finding**; it inherits none of the dead ratio's evidentiary standing.
> **(3) Thesis version:** v1.3 was current at entry (Mar 2026) — accurate as history, not a live token. `THESIS.md` header is canonical (v1.7 at 2026-10-22).

---

## Conviction thesis (entry rationale, preserved — HISTORICAL, Mar 2026)

**Anchor:** Aug $42.5P + $45P × 2 each, entered ~$3.31 avg Mar 2026, conviction 4/5.

- OZK has the WORST hidden CRE ratio in the cohort (37.6% MI3).
- Apr 2026 Q1 earnings = first in-cohort print → sets tone.
- Aug expiry = adequate to capture Q1 print + any Q2 guidance reaction.
- Target exit: $8–12 on charge-off disclosure or hidden CRE acknowledgment.
- Invalidation: NPLs declining + explicit "Memo3 stable legacy" language + Chicago transaction volume recovers.

📌 **Resolved (2026-04-21):** Q1 print confirmed the leading indicator — past-due doubled QoQ $207M → $465M. Slow-grind, not fire. Book expanded to 11 contracts across 4 lines. Thread 3 roll pending (May $42.5P × 2 → Jan27 $42.5P × 2, deadline May 8). Full synthesis → `Q1_2026_ANALYSIS.md`.

---

## Anti-trade (written Apr 2026 at SI 14–15%; the crowding caution still applies — SI ~17.4% at 9/30)

> OZK is a real thesis. But short interest is elevated (14–15%) — the "easy" OZK short is **crowded**.
>
> **Trap:** "OZK is the most obvious short, let me add more."
> **Reality:** SI 14–15% = your edge is already in the premium. You're paying for what everyone knows. Crowded shorts with high SI can rip 20% on any positive catalyst (Fed intervention, Chicago settlement, OZK guidance beat).
>
> **Rule:** Further expansion of OZK exposure requires fresh catalyst confirmation, not thesis-grind. Thread 3 roll extends duration without adding net size — the right shape.

---

*Shrunk to one-pager 2026-04-24 (Mar 7 vintage blocks — earnings-season playbook, original 4-contract position assessment, cross-bank pointers — removed; available in git history). For live trade state → `STATUS.md` + `POSITIONS.md`.*
