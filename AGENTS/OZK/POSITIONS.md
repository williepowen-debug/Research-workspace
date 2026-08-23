> **🧊 FROZEN 2026-07-04 — position book UNRECONCILED (Will 7/4: minimal/uncertain OZK exposure; broker/FORGE reconcile required before unfreezing). Agent LIVE since 2026-07-18; STATUS §Positions is the current-state warning surface. Positions below are April-vintage; do not cite as current.** *(Freeze: DAEDALUS TRADE-staleness sweep, PAT-025, Will-approved. Banner re-worded 7/22 per DAEDALUS 7/22 packet — "dormant/archive-source" label was false post-revival; the freeze itself stands.)*

> **📌 FREEZE ANNOTATION 2026-08-23 (OZK, orch session) — the banner above is kept, and it is now partly stale. Read this line with it.** ① Its "positions below are April-vintage" clause is **DEAD**: the April table was replaced 2026-08-07 by the `FORGE/STATUS.md` mirror off the **2026-08-02 ANVIL broker-export reconcile**, which is the very *"broker/FORGE reconcile"* the freeze named as its own unfreeze condition — i.e. **the stated condition was met 21 days ago and nobody lifted the freeze.** ② It is also now moot in the direction that matters: **the book is EMPTY.** Both remaining legs expired worthless 2026-08-21; there is no live position for a stale table to mis-state. ③ **The freeze itself is NOT lifted here.** It was set by a DAEDALUS staleness sweep under Will approval (PAT-025), and OZK does not unilaterally lift another desk's Will-approved freeze on the strength of its own reading that the condition was met. **RETURNED to PROME as a disposition question** (lift / re-scope to "no positions — re-freeze on any new fill" / leave standing). Until ruled, treat this file as: **authoritative for the CLOSED book, and carrying no live-position claim at all.**

# OZK — Thesis Positions
**Updated:** 2026-08-23 — **BOOK CLOSED. Both Aug-21 legs EXPIRED WORTHLESS at the 2026-08-21 OPEX** under Will's standing **RIDE** ruling (8/4). **OZK has ZERO open option positions as of 2026-08-22.** Prior 2026-08-07 (table re-based to mirror `FORGE/STATUS.md`, ANVIL 8/2 broker export; marks were 7/31 close — that table is now the *closed* book, preserved below). | **Live total: 0 contracts, 0 lines.**

Only OZK positions. **Position truth is off-repo (Will/broker direct); `FORGE/STATUS.md` is the fleet's mirror and this file mirrors it.** Never treat this file as the source.

---

## CLOSED — Aug-21 legs, EXPIRED $0 at the 2026-08-21 OPEX

| Strike | Expiry | Qty | Cost basis | Underlying at expiry | Moneyness | Settle | Realized P&L |
|--------|--------|-----|-----------|----------------------|-----------|--------|--------------|
| **$45P** | **Aug-21-2026** | **4** | **$1,474.70** ($3.69/ct) | **$49.42** | **8.94% OTM** | **$0.00 — expired worthless** | **−$1,474.70 / −100.0%** |
| **$42.5P** | **Aug-21-2026** | **1** | **$211.67** ($2.12/ct) | **$49.42** | **14.02% OTM** | **$0.00 — expired worthless** | **−$211.67 / −100.0%** |
| | | **5** | **$1,686.37** | | | | **−$1,686.37 / −100.0%** |

**Underlying:** OZK closed **$49.42** on **Fri 2026-08-21** (regular-session close; own pull, yfinance `OZK` history, 2026-08-23 — markets closed 8/22-23, so 8/21 is final-for-week). Independently reported by REGINALD off `scripts/market.py` the same figure [`inbox/processed/2026-08-23_from-REGINALD_…expired…`]. Both strikes finished materially out-of-the-money; there is no in-the-money branch to adjudicate.

**Cost bases** are the fees-in figures from the **2026-08-02 ANVIL broker-export reconcile** carried in `FORGE/STATUS.md` (back-computed exactly from that file's own mark/value/P&L cells at both the 8/2 and 8/14 captures: $1,474.70 and $211.67). ⚠️ **The $0 settle is inferred from the tape, not broker-confirmed** — an expiry graded off the close is an inference (root rule #4). **Broker-export confirmation that both lines are ABSENT from the next Fidelity capture rides the standing export ask** (REGINALD's owed item; PROME/ANVIL own the export). Until that capture lands, the realized figures above are labeled-derived, not broker-truth.

### ⚖️ Authority — **RIDE to expiry** (Will, 2026-08-04). Ruled, executed, closed.
**Will RULED RIDE on 2026-08-04: the residual rides to the 8/21 OPEX.** Verified at the record this session, three independent places: `PROME/WILL_QUEUE.md` roll-off line ("row 29 (OZK salvage RULED RIDE 8/4, terminus = 8/21 OPEX DOCKET row)") · `PROME/DOCKET.tsv` row dated 2026-08-21 ("OZK residual rides to $0 or salvage (RULED RIDE 8/4, queue row 29)") · `PROME/DOCKET.tsv` row 162 ("D1 OZK salvage ruled RIDE by Will 8/4 session 4"). `FORGE/STATUS.md` D-26 carries the same ruling on the Aug-21 cluster.

**The ruled outcome and the realized outcome are the same thing: RIDE → expired $0.** The loss was **pre-accepted by the ruling** — the alternative on the table on 8/4 was a ~$41.75 salvage that TERRY's rebuild had already shown arithmetically dead (~$45 live realizable against $675 assumed). ⛔ **This is a LEDGER ROW, not a grade.** No grade of the ruling is offered or owed, and **D1 / OZK-salvage is RULED-CLOSED** — not re-presented, not re-litigated, no successor proposed. An expiry-as-ruled is not materially new state.

### Derived-line sweep (the class this write-back exists to catch)
Surfaces that carried a *count* or a *live-leg* claim rather than the position row itself, all corrected or dated-tagged this session: `STATUS.md` §Positions ("5 contracts, 2 lines") · `INDEX.md` positions line ("Aug 21 lines unverified") · `CALENDAR.md` (expiry row now ✅) · `SCENARIOS.md` §position banner · `IQHQ_PLAYBOOK.md` §position reads · `SEVEN_CREDIT_DEEP_DIVE.md` §position reads. **No OZK surface carries either leg as live after 2026-08-21.**

### Correction — what this table used to say (recorded, not hidden)
The pre-8/7 table showed **11 contracts across 4 lines**: two May-15 lines (**$42.5P ×2** and **$47.5P ×2**) that **expired 2026-05-15**, plus **$42.5P Aug-21 ×3** and **$45P Aug-21 ×4**. Against the 8/2 broker reconcile the Aug-21 lines are **$45P ×4** (matches) and **$42.5P ×1** (recorded as ×3 — **over-stated by 2 contracts**). The stale "🔴 ROLL PENDING → Jan27 $42.5P ×2, hard deadline ~May 8" note is **dead** — that deadline passed unlogged in May and no such position exists. *(Prior `THREAD3_ROLL_MATH.md` reference retired with it.)*

**This is a record correction only. Zero position actions and zero recommendations were made in the 2026-08-07 session** — that session's scope was the pre-registered LOG-ONLY Q2 Call Report pull (`CALL_REPORT_2026Q2_LOG.md`).

---

## Key Context

- Thesis = RESERVOIR v1.5 (`THESIS.md` is canonical for the version). IQHQ RaDD maturity Aug 2026 = core catalyst; **the thesis is unchanged by this expiry** — the position expired, the credit story did not resolve. Management's own 7/22 call guidance pushed RaDD disclosure to the Q3 call (~Oct, the self-set "~92 days"), which is *after* every strike this desk held.
- **May-15 lines (4 ct):** expired 2026-05-15, unlogged at the time; recorded retroactively in §Correction below.
- **Aug-21 lines (5 ct):** expired 2026-08-21 worthless — §CLOSED above. ~~hold through IQHQ maturity~~ ***[dated-tag 2026-08-23: superseded — the expiry has happened; the maturity has not resolved.]***
- **The desk now holds no options.** Any future OZK expression is a NEW trade requiring a Will-gated proposal built by TERRY — not a roll, not a successor, and explicitly not owed here.
- Cross-reference: `STATUS.md` (signal dashboard), `IQHQ_PLAYBOOK.md` (scenario tree). *(`THREAD3_ROLL_MATH.md` retired to `archive/` 2026-07-06 — dead.)*
